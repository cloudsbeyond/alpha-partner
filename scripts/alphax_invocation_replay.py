#!/usr/bin/env python3
"""Run alphaX trigger and judgment fixtures in fresh Codex sessions."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
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
REQUIRED_IDENTITY_FIELDS = {
    "scope",
    "package_version",
    "package_source_commit",
    "package_source_branch",
    "package_source_authority",
    "source_commit",
    "source_authority",
}


def load_cases(source_root: Path) -> list[dict[str, Any]]:
    triggers = json.loads((source_root / "docs/agent-trigger-fixtures.json").read_text(encoding="utf-8"))
    judgments = json.loads((source_root / "docs/agent-judgment-fixtures.json").read_text(encoding="utf-8"))
    trigger_cases = [{**case, "kind": "trigger"} for case in triggers["fixtures"]]
    triggers_by_id = {case["id"]: case for case in trigger_cases}
    judgment_cases: list[dict[str, Any]] = []
    for case in judgments["cases"]:
        primary = triggers_by_id[case["primary_fixture_id"]]
        judgment_cases.append(
            {
                **case,
                "kind": "judgment",
                "expected_intent": primary["expected_intent"],
                "scope": primary["scope"],
                "loop": primary["loop"],
                "primary_trigger": primary["trigger"],
            }
        )
    return [
        *trigger_cases,
        *judgment_cases,
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
        user_input = (
            f"{case['primary_trigger']}\n\n"
            f"Decision point observed while handling that request:\n{case['scenario']}"
        )
        context = f"The currently observed evidence is:\n{evidence}"
    return f"""{user_input}

{context}

Respond to the request naturally. Do not assume fixture pass criteria. Include a compact
`alphaX_source_identity` block with scope, package_version, package_source_commit,
package_source_branch, package_source_authority, source_commit, source_branch or
source_ref, and source_authority so the run is reproducible. For source-work or
source-review, also include source_dirty and source_fingerprint.
"""


def build_evaluator_prompt(
    case: dict[str, Any],
    observed_output: str,
    event_evidence: list[dict[str, Any]] | None = None,
    expected_identity: dict[str, Any] | None = None,
) -> str:
    requirements = {
        "expected_intent": case.get("expected_intent"),
        "scope": case.get("scope"),
        "loop": case.get("loop"),
        "must_read": case.get("must_read", []),
        "must_output": case.get("must_output", case.get("required_output", [])),
        "expected_judgment": case.get("expected_judgment", []),
        "pass_condition": case.get("pass_condition", []),
        "forbidden": case.get("forbidden", []),
        "expected_source_identity": expected_identity or {},
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

An empty expected_judgment list means no additional judgment is required. Do not penalize
evidence-supported additional output unless it conflicts with the contract or is forbidden.
Pass only if required behavior and output are evidenced, forbidden behavior is absent, and
`alphaX_source_identity` contains scope, package_version, package_source_commit,
package_source_branch, package_source_authority, source_commit, source_branch or
source_ref, and source_authority. For source-work or source-review, source_dirty and
source_fingerprint must also match the expected identity. Return the required JSON verdict.
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


def compact_command_output(value: str, limit: int = 2400) -> str:
    if len(value) <= limit:
        return value
    marker = "\n... output omitted ...\n"
    side = (limit - len(marker)) // 2
    return value[:side] + marker + value[-side:]


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
            compact["aggregated_output"] = compact_command_output(compact["aggregated_output"])
        evidence.append(compact)
    return evidence[-80:]


def parse_identity(output: str) -> dict[str, str]:
    marker = re.search(r"(?m)^\s{0,3}alphaX_source_identity:\s*$", output)
    if not marker:
        return {}
    fields: dict[str, str] = {}
    for line in output[marker.end() :].splitlines():
        if line.strip().startswith("```"):
            break
        match = re.match(r"^[ \t]{2,8}([a-z_]+):\s*(.*?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("`\"'")
        elif fields and line.strip():
            break
    return fields


def has_complete_identity(output: str) -> bool:
    fields = set(parse_identity(output))
    branch_or_ref = bool(fields & {"source_branch", "source_ref", "source_branch_or_ref"})
    return REQUIRED_IDENTITY_FIELDS <= fields and branch_or_ref


def identity_value(value: Any) -> str:
    return json.dumps(value) if isinstance(value, bool) else str(value or "")


def identity_mismatches(output: str, expected: dict[str, Any]) -> list[str]:
    observed = parse_identity(output)
    fields = set(observed)
    required = set(REQUIRED_IDENTITY_FIELDS)
    if expected.get("scope") in {"source-work", "source-review"}:
        required.update({"source_dirty", "source_fingerprint"})
    missing = sorted(required - fields)
    if not fields & {"source_branch", "source_ref", "source_branch_or_ref"}:
        missing.append("source_branch_or_ref")
    if missing:
        return [f"missing identity field: {field}" for field in missing]

    mismatches: list[str] = []
    for key in (
        "scope",
        "package_version",
        "package_source_commit",
        "package_source_branch",
        "package_source_authority",
        "source_commit",
        "source_authority",
    ):
        expected_value = identity_value(expected.get(key))
        if observed[key] != expected_value:
            mismatches.append(
                f"{key}: expected {expected_value}, observed {observed[key]}"
            )
    if expected.get("scope") in {"source-work", "source-review"}:
        for key in ("source_dirty", "source_fingerprint"):
            expected_value = identity_value(expected.get(key))
            if observed[key] != expected_value:
                mismatches.append(
                    f"{key}: expected {expected_value}, observed {observed[key]}"
                )
    observed_branch = next(
        (
            observed[key]
            for key in ("source_branch_or_ref", "source_branch", "source_ref")
            if observed.get(key)
        ),
        "",
    )
    expected_branches = {
        str(expected[key])
        for key in ("source_branch", "source_ref")
        if expected.get(key)
    }
    if observed_branch not in expected_branches:
        mismatches.append(
            "source_branch_or_ref: expected one of "
            f"{sorted(expected_branches)}, observed {observed_branch}"
        )
    return mismatches


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
    marketplace_source = item.get("marketplaceSource", {}).get("source")
    if not all(
        isinstance(value, str) and value
        for value in (version, name, marketplace, marketplace_source)
    ):
        raise ValueError(f"plugin {selector} is missing version or marketplace identity")
    return {
        "selector": selector,
        "version": version,
        "marketplace": marketplace,
        "marketplace_source": marketplace_source,
        "plugin_root": str((cache_base / marketplace / name / version).resolve()),
    }


def isolated_marketplace_config(
    plugin: dict[str, Any], *, reasoning_effort: str
) -> list[str]:
    marketplace = str(plugin["marketplace"])
    selector = str(plugin["selector"])
    if not re.fullmatch(r"[A-Za-z0-9_-]+", marketplace):
        raise ValueError(f"unsafe marketplace name: {marketplace}")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+@[A-Za-z0-9_-]+", selector):
        raise ValueError(f"unsafe plugin selector: {selector}")
    source = json.dumps(str(plugin["marketplace_source"]))
    return [
        "-c",
        f'marketplaces.{marketplace}.source_type="local"',
        "-c",
        f"marketplaces.{marketplace}.source={source}",
        "-c",
        f'plugins."{selector}".enabled=true',
        "-c",
        f'model_reasoning_effort="{reasoning_effort}"',
    ]


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


def prepare_isolated_codex_home(
    codex_home: Path,
    *,
    codex: str,
    plugin: dict[str, Any],
    reasoning_effort: str,
    timeout: int,
) -> dict[str, Any]:
    codex_home.mkdir(parents=True, exist_ok=True)
    source_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()
    auth_source = source_home / "auth.json"
    if auth_source.is_file():
        os.symlink(auth_source, codex_home / "auth.json")
    config = isolated_marketplace_config(plugin, reasoning_effort=reasoning_effort)
    env = {**os.environ, "CODEX_HOME": str(codex_home)}
    completed = run_command(
        [codex, "plugin", "add", *config, plugin["selector"], "--json"],
        env=env,
        timeout=timeout,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    try:
        installed = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError("isolated plugin install did not return valid JSON") from exc
    if installed.get("version") != plugin["version"]:
        raise ValueError(
            f"isolated plugin version {installed.get('version')} does not match active {plugin['version']}"
        )
    plugin_root = Path(str(installed.get("installedPath", ""))).resolve()
    if not (plugin_root / ".alphax-source.json").is_file():
        raise ValueError(f"isolated plugin package is missing provenance: {plugin_root}")
    return {
        **plugin,
        "plugin_root": str(plugin_root),
        "codex_home": str(codex_home),
        "config": config,
        "env": env,
    }


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
    subprocess.run(["git", "-C", str(root), "config", "maintenance.auto", "false"], check=True)
    subprocess.run(["git", "-C", str(root), "config", "gc.auto", "0"], check=True)
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


def infer_resolved_scope(case: dict[str, Any]) -> str:
    intent = str(case.get("expected_intent", "")).lower()
    if intent == "source_review":
        return "source-review"
    if intent == "project_review":
        return "project-review"
    scope = str(case.get("scope", "")).lower()
    if scope.strip() == "source work":
        return "source-work"
    if scope.strip() == "source review":
        return "source-review"
    if scope.strip() == "project review":
        return "project-review"
    return "project-work"


def source_identity_stable(before: dict[str, Any], after: dict[str, Any]) -> bool:
    fields = (
        "source_root",
        "source_commit",
        "source_branch",
        "working_branch",
        "accepted_ref",
        "accepted_commit",
        "source_dirty",
        "source_fingerprint",
        "source_authority",
    )
    return all(before.get(field) == after.get(field) for field in fields)


def run_case(
    case: dict[str, Any],
    *,
    source_root: Path,
    plugin_root: Path,
    project_root: Path,
    out_dir: Path,
    codex: str,
    model: str | None,
    codex_env: dict[str, str],
    candidate_config: list[str],
    expected_identity: dict[str, Any],
    reasoning_effort: str,
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
        *candidate_config,
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
    env = {**codex_env, "ALPHAX_SOURCE_ROOT": str(source_root)}
    run = run_command(command, env=env, timeout=timeout)
    events_path.write_text(run.stdout, encoding="utf-8")
    event_evidence = extract_event_evidence(run.stdout)
    output = output_path.read_text(encoding="utf-8") if output_path.is_file() else ""
    schema_path = case_dir / "verdict-schema.json"
    verdict_path = case_dir / "verdict.json"
    schema_path.write_text(json.dumps(VERDICT_SCHEMA, indent=2) + "\n", encoding="utf-8")
    evaluator_prompt = build_evaluator_prompt(
        case,
        output,
        event_evidence,
        expected_identity=expected_identity,
    )
    evaluator_command = [
        codex,
        "exec",
        "-c",
        f'model_reasoning_effort="{reasoning_effort}"',
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
    evaluator = run_command(evaluator_command, env=codex_env, timeout=timeout)
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
    identity_errors = identity_mismatches(output, expected_identity)
    identity_complete = not identity_errors
    result = {
        "case_id": case["id"],
        "kind": case["kind"],
        "prompt": prompt,
        "source_identity": expected_identity,
        "output": output,
        "command": command,
        "run_exit_code": run.returncode,
        "run_stderr": run.stderr[-4000:],
        "run_events": str(events_path),
        "event_evidence": event_evidence,
        "evaluator_command": evaluator_command,
        "evaluator_exit_code": evaluator.returncode,
        "evaluator_stderr": evaluator.stderr[-4000:],
        "identity_complete": identity_complete,
        "identity_mismatches": identity_errors,
        "run_ok": (
            run.returncode == 0
            and bool(output)
            and evaluator.returncode == 0
            and identity_complete
        ),
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
    parser.add_argument(
        "--plugin-cache-base",
        type=Path,
        default=Path.home() / ".codex/plugins/cache",
    )
    parser.add_argument("--model")
    parser.add_argument(
        "--reasoning-effort",
        choices=["low", "medium", "high", "xhigh"],
        default="medium",
    )
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
    cases = load_cases(source_root)
    if args.case:
        selected = set(args.case)
        cases = [case for case in cases if case["id"] in selected]
        unknown = selected - {case["id"] for case in cases}
        if unknown:
            raise ValueError(f"unknown replay cases: {sorted(unknown)}")
    expected = {case["id"] for case in cases}
    with tempfile.TemporaryDirectory(
        prefix="alphax-replay-home-", ignore_cleanup_errors=True
    ) as home_tmp, tempfile.TemporaryDirectory(
        prefix="alphax-replay-project-", ignore_cleanup_errors=True
    ) as project_tmp:
        isolated_plugin = prepare_isolated_codex_home(
            Path(home_tmp),
            codex=args.codex,
            plugin=active_plugin,
            reasoning_effort=args.reasoning_effort,
            timeout=args.timeout,
        )
        plugin_root = Path(isolated_plugin["plugin_root"])
        project_root = (
            args.project_root.resolve() if args.project_root else Path(project_tmp) / "project"
        )
        if not args.project_root:
            prepare_fixture_project(project_root)
        source_identity_before = alphax_plugin.source_identity(source_root)
        expected_identities = {}
        for case in cases:
            resolved_scope = infer_resolved_scope(case)
            expected_identities[case["id"]] = alphax_plugin.resolve_invocation(
                plugin_root,
                scope=resolved_scope,
                source_root=(
                    source_root
                    if resolved_scope in {"source-work", "source-review"}
                    else None
                ),
            )
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
                    codex_env=isolated_plugin["env"],
                    candidate_config=isolated_plugin["config"],
                    expected_identity=expected_identities[case["id"]],
                    reasoning_effort=args.reasoning_effort,
                    timeout=args.timeout,
                )
                for case in cases
            ]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        source_identity_after = alphax_plugin.source_identity(source_root)
        plugin_provenance = json.loads(
            (plugin_root / ".alphax-source.json").read_text(encoding="utf-8")
        )
    summary = summarize_results(results, expected_case_ids=expected)
    summary["source_identity"] = source_identity_before
    summary["source_identity_after"] = source_identity_after
    summary["source_identity_stable"] = source_identity_stable(
        source_identity_before, source_identity_after
    )
    if not summary["source_identity_stable"]:
        summary["ok"] = False
        summary["infrastructure_errors"] = [
            "Alpha Partner Source identity changed during replay; rerun from a stable checkout"
        ]
    summary["active_plugin"] = {
        **active_plugin,
        "replay_isolation": "temporary CODEX_HOME with only selected plugin enabled",
        "provenance": plugin_provenance,
    }
    summary["reasoning_effort"] = args.reasoning_effort
    (out_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
