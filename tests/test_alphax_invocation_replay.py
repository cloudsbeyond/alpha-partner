from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import alphax_invocation_replay as replay  # noqa: E402


class AlphaXInvocationReplayTest(unittest.TestCase):
    def test_loads_all_trigger_and_judgment_cases(self) -> None:
        cases = replay.load_cases(ROOT)

        self.assertEqual(len(cases), 21)
        self.assertEqual({case["id"] for case in cases if case["kind"] == "trigger"}, {f"F{i:02d}" + suffix for i, suffix in [
            (1, "-risk-current-project"),
            (2, "-progress-reentry"),
            (3, "-before-merge-review"),
            (4, "-real-problem"),
            (5, "-source-self-critique"),
            (6, "-source-drift"),
            (7, "-nudge-check"),
            (8, "-engage"),
            (9, "-double-diamond-research"),
            (10, "-loop-verification-gate"),
        ]})
        self.assertIn("G11-project-delivery-loop-before-execution", {case["id"] for case in cases})

    def test_run_prompt_requires_source_identity_and_natural_case_input(self) -> None:
        case = {
            "id": "F01-risk-current-project",
            "kind": "trigger",
            "trigger": "@alphaX 帮我看看当前项目风险",
            "must_read": ["git status/diff"],
            "must_output": ["P0", "current state"],
            "forbidden": ["code edits"],
        }

        prompt = replay.build_run_prompt(case)

        self.assertIn("@alphaX 帮我看看当前项目风险", prompt)
        self.assertIn("alphaX_source_identity", prompt)
        self.assertNotIn("You must pass", prompt)
        self.assertNotIn("expected_intent", prompt)

    def test_evaluator_prompt_contains_fixture_and_observed_output(self) -> None:
        case = {
            "id": "G01-upstream-contract-gap",
            "kind": "judgment",
            "scenario": "ambiguous upstream objective",
            "expected_judgment": ["park downstream work"],
            "required_output": ["D0-D3 map"],
            "pass_condition": ["execution stops"],
            "forbidden": ["shipping downstream implementation"],
        }

        prompt = replay.build_evaluator_prompt(
            case,
            "observed agent response",
            [{"type": "command_execution", "command": "git status", "exit_code": 0}],
        )

        self.assertIn("independent evaluator", prompt)
        self.assertIn("park downstream work", prompt)
        self.assertIn("observed agent response", prompt)
        self.assertIn("shipping downstream implementation", prompt)
        self.assertIn("git status", prompt)

    def test_event_evidence_keeps_completed_tool_observations(self) -> None:
        events = "\n".join(
            [
                json.dumps({"type": "thread.started", "thread_id": "t"}),
                json.dumps(
                    {
                        "type": "item.completed",
                        "item": {
                            "type": "command_execution",
                            "command": "git status --short",
                            "aggregated_output": " M README.md\\n",
                            "exit_code": 0,
                            "status": "completed",
                        },
                    }
                ),
                json.dumps(
                    {"type": "item.completed", "item": {"type": "agent_message", "text": "done"}}
                ),
            ]
        )

        evidence = replay.extract_event_evidence(events)

        self.assertEqual(len(evidence), 1)
        self.assertEqual(evidence[0]["command"], "git status --short")
        self.assertEqual(evidence[0]["exit_code"], 0)

    def test_clear_case_outputs_prevents_stale_result_reuse(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            case_dir = Path(tmp)
            for name in ["response.md", "verdict.json", "run-events.jsonl"]:
                (case_dir / name).write_text("stale", encoding="utf-8")

            replay.clear_case_outputs(case_dir)

            self.assertFalse((case_dir / "response.md").exists())
            self.assertFalse((case_dir / "verdict.json").exists())
            self.assertFalse((case_dir / "run-events.jsonl").exists())

    def test_fixture_keeps_project_local_alphax_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "project"
            replay.prepare_fixture_project(root)

            tracked = subprocess.check_output(
                ["git", "-C", str(root), "ls-files", ".alphaX/*"], text=True
            ).strip()
            ignored = subprocess.run(
                ["git", "-C", str(root), "check-ignore", ".alphaX/project-context.md"],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(tracked, "")
            self.assertEqual(ignored.returncode, 0)

    def test_installed_plugin_record_resolves_selected_cache(self) -> None:
        payload = {
            "installed": [
                {
                    "pluginId": "alphax@personal",
                    "name": "alphax",
                    "marketplaceName": "personal",
                    "version": "0.1.0+codex.abc123",
                    "installed": True,
                    "enabled": True,
                }
            ]
        }

        result = replay.installed_plugin_record(
            payload,
            selector="alphax@personal",
            cache_base=Path("/cache"),
        )

        self.assertEqual(result["plugin_root"], "/cache/personal/alphax/0.1.0+codex.abc123")
        self.assertEqual(result["version"], "0.1.0+codex.abc123")

    def test_summary_fails_when_any_case_lacks_independent_pass(self) -> None:
        results = [
            {"case_id": "F01", "run_ok": True, "verdict": {"pass": True}},
            {"case_id": "G01", "run_ok": True, "verdict": {"pass": False}},
        ]

        summary = replay.summarize_results(results, expected_case_ids={"F01", "G01"})

        self.assertFalse(summary["ok"])
        self.assertEqual(summary["failed_case_ids"], ["G01"])

    def test_summary_fails_when_a_required_case_is_missing(self) -> None:
        results = [{"case_id": "F01", "run_ok": True, "verdict": {"pass": True}}]

        summary = replay.summarize_results(results, expected_case_ids={"F01", "G01"})

        self.assertFalse(summary["ok"])
        self.assertEqual(summary["missing_case_ids"], ["G01"])

    def test_report_persists_prompt_output_identity_and_verdict(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            result = {
                "case_id": "F01",
                "kind": "trigger",
                "prompt": "prompt",
                "source_identity": {"source_commit": "abc", "source_authority": "accepted"},
                "output": "answer",
                "command": ["codex", "exec", "--ephemeral"],
                "run_ok": True,
                "verdict": {"pass": True, "reasons": ["ok"]},
            }

            replay.write_case_result(out, result)

            payload = json.loads((out / "F01.json").read_text())
            self.assertEqual(payload["prompt"], "prompt")
            self.assertEqual(payload["source_identity"]["source_commit"], "abc")
            self.assertEqual(payload["output"], "answer")
            self.assertTrue(payload["verdict"]["pass"])


if __name__ == "__main__":
    unittest.main()
