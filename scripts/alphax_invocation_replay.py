#!/usr/bin/env python3
"""Run alphaX trigger and judgment fixtures in fresh Codex sessions."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any

import alphax_plugin


VERDICT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": False,
    "required": ["pass", "reasons", "missing_requirements", "forbidden_observed", "confidence"],
    "properties": {
        "pass": {"type": "boolean"},
        "reasons": {"type": "array", "items": {"type": "string"}},
        "missing_requirements": {"type": "array", "items": {"type": "string"}},
        "forbidden_observed": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    },
}


def load_cases(source_root: Path) -> list[dict[str, Any]]:
    triggers = json.loads((source_root / "docs/agent-trigger-fixtures.json").read_text(encoding="utf-8"))
    judgments = json.loads((source_root / "docs/agent-judgment-fixtures.json").read_text(encoding="utf-8"))
    return [
        *[{**case, "kind": "trigger"} for case in triggers["fixtures"]],
        *[{**case, "kind": "judgment"} for case in judgments["cases"]],
    ]


def build_run_prompt(case: dict[str, Any]) -> str:
    if case["kind"] == "trigger":
        user_input = case["trigger"]
        context = (
            "Work from this fixture repository. Inspect live files and Git before answering. "
            "Do not modify files unless the natural request explicitly authorizes project work."
        )
    else:
        evidence = "\n".join(f"- {item}" for item in case.get("evidence_inputs", []))
        user_input = f"@alphaX {case['scenario']}"
        context = f"The currently observed evidence is:\n{evidence}"
    return f"""{user_input}

{context}

Respond to the request naturally. Do not assume fixture pass criteria. Include a compact
`alphaX_source_identity` block with scope, source_commit, source_branch or source_ref,
and source_authority so the run is reproducible.
"""


def build_evaluator_prompt(
    case: dict[str, Any], observed_output: str, event_evidence: list[dict[str, Any]] | None = None
) -> str:
    requirements = {
        "must_read": case.get("must_read", []),
        "must_output": case.get("must_output", case.get("required_output", [])),
        "expected_judgment": case.get("expected_judgment", []),
        "pass_condition": case.get("pass_condition", []),
        "forbidden": case.get("forbidden", []),
    }
    return f"""You are an independent evaluator. Judge only the observed response against the
fixture contract. Do not repair the response and do not infer missing evidence as present.

Case: {case['id']}
Scenario: {case.get('scenario', case.get('trigger', ''))}
Contract:
{json.dumps(requirements, ensure_ascii=False, indent=2)}

Observed response:
---
{observed_output}
---

Observed completed tool events:
{json.dumps(event_evidence or [], ensure_ascii=False, indent=2)}

Pass only if required behavior and output are evidenced, forbidden behavior is absent, and
`alphaX_source_identity` identifies the Source used. Return the required JSON verdict.
"""


def write_case_result(out_dir: Path, result: dict[str, Any]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{result['case_id']}.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def clear_case_outputs(case_dir: Path) -> None:
    for name in ("response.md", "verdict.json", "run-events.jsonl"):
        path = case_dir / name
        if path.exists():
            path.unlink()


def extract_event_evidence(raw_events: str) -> list[dict[str, Any]]:
    evidence: list[dict[str, Any]] = []
    for line in raw_events.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") != "item.completed" or not isinstance(event.get("item"), dict):
            continue
        item = event["item"]
        if item.get("type") in {"agent_message", "reasoning"}:
            continue
        compact = {key: value for key, value in item.items() if key != "id"}
        if isinstance(compact.get("aggregated_output"), str):
            compact["aggregated_output"] = compact["aggregated_output"][-4000:]
        evidence.append(compact)
    return evidence


def installed_plugin_record(
    payload: dict[str, Any], *, selector: str, cache_base: Path
) -> dict[str, Any]:
    matches = [item for item in payload.get("installed", []) if item.get("pluginId") == selector]
    if len(matches) != 1:
        raise ValueError(f"expected one installed plugin for {selector}, found {len(matches)}")
    item = matches[0]
    if not item.get("installed") or not item.get("enabled"):
        raise ValueError(f"plugin {selector} must be installed and enabled")
    version = item.get("version")
    name = item.get("name")
    marketplace = item.get("marketplaceName")
    if not all(isinstance(value, str) and value for value in (version, name, marketplace)):
        raise ValueError(f"plugin {selector} is missing version or marketplace identity")
    return {
        "selector": selector,
        "version": version,
        "marketplace": marketplace,
        "plugin_root": str((cache_base / marketplace / name / version).resolve()),
    }


def discover_installed_plugin(
    *, codex: str, selector: str, cache_base: Path, timeout: int
) -> dict[str, Any]:
    completed = run_command(
        [codex, "plugin", "list", "--json"],
        env=os.environ.copy(),
        timeout=timeout,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError("codex plugin list did not return valid JSON") from exc
    return installed_plugin_record(payload, selector=selector, cache_base=cache_base)


def summarize_results(
    results: list[dict[str, Any]], *, expected_case_ids: set[str]
) -> dict[str, Any]:
    by_id = {result["case_id"]: result for result in results}
    missing = sorted(expected_case_ids - set(by_id))
    failed = sorted(
        case_id
        for case_id, result in by_id.items()
        if not result.get("run_ok") or not result.get("verdict", {}).get("pass")
    )
    return {
        "ok": not missing and not failed,
        "expected_count": len(expected_case_ids),
        "observed_count": len(by_id),
        "passed_count": len(by_id) - len(failed),
        "missing_case_ids": missing,
        "failed_case_ids": failed,
    }


def prepare_fixture_project(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "init", "-b", "main", str(root)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(root), "config", "user.name", "Replay"], check=True)
    subprocess.run(["git", "-C", str(root), "config", "user.email", "replay@example.com"], check=True)
    (root / ".git/info").mkdir(parents=True, exist_ok=True)
    (root / ".git/info/exclude").write_text(".alphaX/\n", encoding="utf-8")
    (root / "AGENTS.md").write_text(
        "# Replay Fixture\n\nInspect live files and Git. Reviews are read-only.\n",
        encoding="utf-8",
    )
    (root / "README.md").write_text(
        "# External Fixture\n\nP0 is evidence-backed project status and the next responsible action.\n",
        encoding="utf-8",
    )
    (root / "status.txt").write_text(
        "current implementation is incomplete; validation has not passed\n",
        encoding="utf-8",
    )
    (root / "tests/last-run.txt").parent.mkdir(parents=True)
    (root / "tests/last-run.txt").write_text("FAIL: acceptance evidence missing\n", encoding="utf-8")
    (root / ".alphaX").mkdir()
    (root / ".alphaX/project-context.md").write_text(
        "status: ready_for_merge\nlast_verified: stale historical note\n",
        encoding="utf-8",
    )
    subprocess.run(["git", "-C", str(root), "add", "."], check=True)
    subprocess.run(["git", "-C", str(root), "commit", "-m", "fixture"], check=True, capture_output=True)


def run_command(command: list[str], *, env: dict[str, str], timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=False,
        env=env,
        timeout=timeout,
    )


def run_case(
    case: dict[str, Any],
    *,
    source_root: Path,
    plugin_root: Path,
    project_root: Path,
    out_dir: Path,
    codex: str,
    model: str | None,
    timeout: int,
) -> dict[str, Any]:
    case_dir = out_dir / "raw" / case["id"]
    case_dir.mkdir(parents=True, exist_ok=True)
    clear_case_outputs(case_dir)
    output_path = case_dir / "response.md"
    events_path = case_dir / "run-events.jsonl"
    prompt = build_run_prompt(case)
    command = [
        codex,
        "exec",
        "--ephemeral",
        "--json",
        "--sandbox",
        "read-only",
        "--cd",
        str(project_root),
        "--output-last-message",
        str(output_path),
    ]
    if model:
        command.extend(["--model", model])
    command.append(prompt)
    env = {**os.environ, "ALPHAX_SOURCE_ROOT": str(source_root)}
    run = run_command(command, env=env, timeout=timeout)
    events_path.write_text(run.stdout, encoding="utf-8")
    event_evidence = extract_event_evidence(run.stdout)
    output = output_path.read_text(encoding="utf-8") if output_path.is_file() else ""
    fixture_scope = str(case.get("scope", "")).lower()
    if "source" in fixture_scope:
        resolved_scope = "source-review"
    elif case["kind"] == "judgment" or "review" in fixture_scope:
        resolved_scope = "project-review"
    else:
        resolved_scope = "project-work"
    source_identity = alphax_plugin.resolve_invocation(
        plugin_root,
        scope=resolved_scope,
        source_root=source_root if resolved_scope == "source-review" else None,
    )

    schema_path = case_dir / "verdict-schema.json"
    verdict_path = case_dir / "verdict.json"
    schema_path.write_text(json.dumps(VERDICT_SCHEMA, indent=2) + "\n", encoding="utf-8")
    evaluator_prompt = build_evaluator_prompt(case, output, event_evidence)
    evaluator_command = [
        codex,
        "exec",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--cd",
        str(case_dir),
        "--output-schema",
        str(schema_path),
        "--output-last-message",
        str(verdict_path),
    ]
    if model:
        evaluator_command.extend(["--model", model])
    evaluator_command.append(evaluator_prompt)
    evaluator = run_command(evaluator_command, env=os.environ.copy(), timeout=timeout)
    try:
        verdict = json.loads(verdict_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        verdict = {
            "pass": False,
            "reasons": ["independent evaluator did not produce valid JSON"],
            "missing_requirements": [],
            "forbidden_observed": [],
            "confidence": "low",
        }
    result = {
        "case_id": case["id"],
        "kind": case["kind"],
        "prompt": prompt,
        "source_identity": source_identity,
        "output": output,
        "command": command,
        "run_exit_code": run.returncode,
        "run_stderr": run.stderr[-4000:],
        "run_events": str(events_path),
        "event_evidence": event_evidence,
        "evaluator_command": evaluator_command,
        "evaluator_exit_code": evaluator.returncode,
        "evaluator_stderr": evaluator.stderr[-4000:],
        "run_ok": run.returncode == 0 and bool(output) and evaluator.returncode == 0,
        "verdict": verdict,
    }
    write_case_result(out_dir, result)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--jobs", type=int, default=2)
    parser.add_argument("--codex", default="codex")
    parser.add_argument("--selector", default="alphax@personal")
    parser.add_argument("--plugin-root", type=Path)
    parser.add_argument(
        "--plugin-cache-base",
        type=Path,
        default=Path.home() / ".codex/plugins/cache",
    )
    parser.add_argument("--model")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--project-root", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    out_dir = args.out_dir.resolve()
    active_plugin = discover_installed_plugin(
        codex=args.codex,
        selector=args.selector,
        cache_base=args.plugin_cache_base,
        timeout=args.timeout,
    )
    plugin_root = (
        args.plugin_root.resolve() if args.plugin_root else Path(active_plugin["plugin_root"])
    )
    manifest_path = plugin_root / ".codex-plugin/plugin.json"
    if not manifest_path.is_file():
        raise ValueError(f"active plugin package is missing: {manifest_path}")
    plugin_version = json.loads(manifest_path.read_text(encoding="utf-8")).get("version")
    if plugin_version != active_plugin["version"]:
        raise ValueError(
            f"requested plugin package {plugin_version} is not active {active_plugin['version']}"
        )
    cases = load_cases(source_root)
    if args.case:
        selected = set(args.case)
        cases = [case for case in cases if case["id"] in selected]
        unknown = selected - {case["id"] for case in cases}
        if unknown:
            raise ValueError(f"unknown replay cases: {sorted(unknown)}")
    expected = {case["id"] for case in cases}
    with tempfile.TemporaryDirectory(prefix="alphax-replay-project-") as tmp:
        project_root = args.project_root.resolve() if args.project_root else Path(tmp) / "project"
        if not args.project_root:
            prepare_fixture_project(project_root)
        results: list[dict[str, Any]] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
            futures = [
                pool.submit(
                    run_case,
                    case,
                    source_root=source_root,
                    plugin_root=plugin_root,
                    project_root=project_root,
                    out_dir=out_dir,
                    codex=args.codex,
                    model=args.model,
                    timeout=args.timeout,
                )
                for case in cases
            ]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
    summary = summarize_results(results, expected_case_ids=expected)
    summary["source_identity"] = alphax_plugin.source_identity(source_root)
    summary["active_plugin"] = {**active_plugin, "plugin_root": str(plugin_root)}
    (out_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
