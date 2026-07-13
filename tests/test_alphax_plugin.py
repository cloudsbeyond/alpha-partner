from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import alphax_plugin  # noqa: E402


class AlphaXPluginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / "source"
        self.source.mkdir()
        self._write_source_fixture()
        self._git("init", "-b", "main")
        self._git("config", "user.name", "Test")
        self._git("config", "user.email", "test@example.com")
        self._git("config", "maintenance.auto", "false")
        self._git("config", "gc.auto", "0")
        self._git("add", ".")
        self._git("commit", "-m", "initial")

    def _write(self, relative: str, content: str | bytes) -> None:
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")

    def _write_source_fixture(self) -> None:
        self._write(
            "plugin/plugin.template.json",
            json.dumps(
                {
                    "name": "alphax",
                    "version": "0.1.0",
                    "description": "test plugin",
                    "author": {"name": "Test"},
                    "license": "MIT",
                    "skills": "./skills/",
                    "interface": {
                        "displayName": "alphaX",
                        "shortDescription": "test",
                        "longDescription": "test plugin",
                        "developerName": "Test",
                        "category": "Productivity",
                        "capabilities": ["Source work"],
                        "brandColor": "#2563EB",
                        "composerIcon": "./assets/icon.png",
                        "logo": "./assets/icon.png",
                        "defaultPrompt": ["@alphaX engage"],
                    },
                },
                indent=2,
            )
            + "\n",
        )
        self._write("plugin/README.md", "# alphaX\n")
        self._write(
            "plugin/skills/alphax/SKILL.md",
            "---\nname: alphax\ndescription: Use when alphaX is invoked.\n---\n# alphaX\n",
        )
        self._write("assets/icon.png", b"png")
        self._write(
            "alphaX/session-runbook.md",
            "---\ntype: SOP\ntitle: Session\ndescription: fixture\n---\n# Session\n",
        )
        self._write(
            "docs/agent-invocation-contract.md",
            "---\ntype: Contract\ntitle: Invocation\ndescription: fixture\n---\n# Invocation\n",
        )
        self._write(
            "scripts/alphax_plugin.py",
            (ROOT / "scripts/alphax_plugin.py").read_text(encoding="utf-8"),
        )
        self._write(
            "skills/problem-decomposer/SKILL.md",
            "---\nname: problem-decomposer\ndescription: Use when decomposing.\n---\n# A\n",
        )
        self._write(
            "skills/formal-development/SKILL.md",
            "---\nname: formal-development\ndescription: Use when formalizing.\n---\n# B\nSemantic Preservation\n",
        )
        self._write("skills/formal-development/references/rule.md", "rule\n")
        self._write("AGENTS.md", "accepted\n")

    def _git(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(self.source), *args], text=True
        ).strip()

    def test_build_is_one_way_from_source_and_records_commit(self) -> None:
        out = Path(self.temp.name) / "plugin-out"

        result = alphax_plugin.build_plugin(self.source, out)

        commit = self._git("rev-parse", "HEAD")
        manifest = json.loads((out / ".codex-plugin/plugin.json").read_text())
        provenance = json.loads((out / ".alphax-source.json").read_text())
        self.assertEqual(manifest["version"], f"0.1.0+codex.{commit[:12]}")
        self.assertEqual(provenance["source_commit"], commit)
        self.assertEqual(provenance["source_branch"], "main")
        self.assertEqual(provenance["source_authority"], "accepted")
        self.assertFalse(provenance["source_dirty"])
        self.assertEqual(result["version"], manifest["version"])
        self.assertEqual((out / "source/AGENTS.md").read_text(), "accepted\n")
        self.assertTrue((out / "source/alphaX/session-runbook.md").is_file())
        self.assertEqual(provenance["embedded_source_commit"], commit)
        self.assertEqual(provenance["embedded_source_authority"], "accepted")
        self.assertTrue((out / "bin/alphax_plugin.py").is_file())
        self.assertTrue((out / "skills/alphax/SKILL.md").is_file())
        self.assertTrue((out / "skills/problem-decomposer/SKILL.md").is_file())
        self.assertTrue((out / "skills/formal-development/SKILL.md").is_file())
        self.assertEqual(
            (out / "skills/formal-development/references/rule.md").read_text(),
            "rule\n",
        )

    def test_real_entry_skill_uses_package_local_source_resolution(self) -> None:
        entry = (ROOT / "plugin/skills/alphax/SKILL.md").read_text(encoding="utf-8")
        manifest = json.loads((ROOT / "plugin/plugin.template.json").read_text(encoding="utf-8"))

        self.assertIn("resolve-invocation", entry)
        self.assertIn("bin/alphax_plugin.py", entry)
        self.assertIn("package_version", entry)
        self.assertIn("package_source_commit", entry)
        self.assertIn("Risk, progress, re-entry, or focus", entry)
        self.assertIn("must not issue a completion", entry)
        self.assertIn("observing incomplete implementation or failed validation does not", entry)
        self.assertIn("even when alphaX is named as the loop", entry)
        self.assertIn("without declaring the project complete/incomplete", entry)
        self.assertIn("must name the Source-defined first-read", entry)
        self.assertIn("explicitly name the first", entry)
        self.assertIn("smallest reversible pilot", entry)
        self.assertIn("must not reveal a favored", entry)
        self.assertIn("Double Diamond research is likewise `project-work`", entry)
        self.assertIn("its findings and calls must concern Alpha Partner", entry)
        self.assertIn("judgment-contract statement", entry)
        self.assertIn("path-specific evidence gap", entry)
        self.assertIn("Develop and Deliver as blocked or deferred", entry)
        self.assertIn("first substantive user-visible section is `Findings`", entry)
        self.assertIn("mergeability, release, or summary conclusion before", entry)
        self.assertIn("confirm the command output contains that evidence", entry)
        self.assertIn("ignore checks, or a read command whose output", entry)
        self.assertIn("`asset_half_life`), exact signal entry", entry)
        self.assertIn("docs/agent-invocation-contract.md", entry)
        self.assertIn("only when behavior or tone requires it", entry)
        self.assertIn("Bounded project implementation fast path", entry)
        self.assertIn("do not read activation,", entry)
        self.assertIn("re-entry, operating-system, or loop-registry documents", entry)
        self.assertLessEqual(len(manifest["interface"]["defaultPrompt"]), 3)
        self.assertNotIn("/" + "Users/", entry)

    def test_replay_failure_boundaries_are_source_contracts(self) -> None:
        invocation = (ROOT / "docs/agent-invocation-contract.md").read_text(
            encoding="utf-8"
        )
        decomposer = (ROOT / "skills/problem-decomposer/SKILL.md").read_text(
            encoding="utf-8"
        )
        diamond = (ROOT / "skills/double-diamond-research/SKILL.md").read_text(
            encoding="utf-8"
        )
        fixtures = json.loads(
            (ROOT / "docs/agent-trigger-fixtures.json").read_text(encoding="utf-8")
        )
        loop_fixture = next(
            item
            for item in fixtures["fixtures"]
            if item["id"] == "F10-loop-verification-gate"
        )

        self.assertIn("does not by itself upgrade project work", invocation)
        self.assertIn("does not declare completion or merge readiness", invocation)
        self.assertIn("overridden_default names the Source scaffold", invocation)
        self.assertIn("including in the opening", invocation)
        self.assertIn("project review starts with findings", invocation)
        self.assertIn("discovery or listing alone is missing evidence", invocation)
        self.assertIn("source review findings and calls concern Alpha Partner Source only", invocation)
        self.assertIn("Double Diamond output always maps", invocation)
        self.assertIn("path-specific evidence gaps and validation approaches", invocation)
        self.assertIn("never invent a business or user objective", decomposer)
        self.assertIn("explicit weak-layer call", decomposer)
        self.assertIn("path-specific evidence and validation", diamond)
        self.assertIn("smallest reversible pilot", diamond)
        self.assertIn("must not name a favored candidate", diamond)
        self.assertIn("does not\nturn research into a completion review", diamond)
        self.assertIn("active\njudgment contract explicitly says", diamond)
        self.assertIn("Discover-Define-Develop-Deliver map is\ncomplete", diamond)
        self.assertIn("category (intelligence_ceiling or asset_half_life)",
                      (ROOT / "skills/insight-catcher/SKILL.md").read_text(encoding="utf-8"))
        self.assertEqual(
            loop_fixture["scope"],
            "project work unless the user explicitly requests Alpha Partner Source review or change",
        )

    def test_local_verifier_distinguishes_secret_names_from_values(self) -> None:
        verifier = (ROOT / "scripts/verify-local-alphaX.sh").read_text(
            encoding="utf-8"
        )

        self.assertIn("OPENAI_API_KEY[[:space:]]*[:=]", verifier)
        self.assertIn("sk-[A-Za-z0-9_-]{16,}", verifier)
        self.assertIn("ANTHROPIC_API_KEY[[:space:]]*[:=]", verifier)
        self.assertNotIn(
            '"BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY"',
            verifier,
        )

    def test_project_work_bounded_implementation_has_a_proportional_stop_rule(self) -> None:
        workflow = (ROOT / "alphaX/project-work/agent-workflow.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("bounded_implementation:", workflow)
        self.assertIn("known working project runner", workflow)
        self.assertIn("containing test module or smallest affected suite", workflow)
        self.assertIn("expand_validation_when", workflow)
        self.assertIn("does_not_waive", workflow)

    def test_dirty_source_requires_explicit_candidate_build(self) -> None:
        self._write("skills/problem-decomposer/SKILL.md", "changed\n")

        with self.assertRaisesRegex(ValueError, "dirty Source"):
            alphax_plugin.build_plugin(self.source, Path(self.temp.name) / "refused")

        out = Path(self.temp.name) / "dirty"
        result = alphax_plugin.build_plugin(self.source, out, allow_dirty=True)
        provenance = json.loads((out / ".alphax-source.json").read_text())
        self.assertRegex(result["version"], r"^0\.1\.0\+codex\.dirty-[0-9a-f]{12}$")
        self.assertTrue(provenance["source_dirty"])
        self.assertEqual(provenance["source_authority"], "candidate")

    def test_same_version_content_drift_is_a_hard_failure(self) -> None:
        expected = Path(self.temp.name) / "expected"
        plugin_source = Path(self.temp.name) / "marketplace"
        alphax_plugin.build_plugin(self.source, expected)
        alphax_plugin.copy_tree(expected, plugin_source)
        manifest = json.loads((plugin_source / ".codex-plugin/plugin.json").read_text())
        cache = Path(self.temp.name) / "cache" / manifest["version"]
        alphax_plugin.copy_tree(expected, cache)
        (cache / "skills/formal-development/SKILL.md").write_text("stale\n")

        result = alphax_plugin.verify_installed(
            self.source,
            plugin_source=plugin_source,
            cache_root=cache.parent,
            require_accepted=True,
        )

        self.assertFalse(result["ok"])
        self.assertIn("cache-content-drift", result["failure_classes"])
        self.assertTrue(any("formal-development/SKILL.md" in item for item in result["diffs"]))

    def test_missing_source_skill_is_a_hard_failure(self) -> None:
        expected = Path(self.temp.name) / "expected"
        plugin_source = Path(self.temp.name) / "marketplace"
        alphax_plugin.build_plugin(self.source, expected)
        alphax_plugin.copy_tree(expected, plugin_source)
        manifest = json.loads((plugin_source / ".codex-plugin/plugin.json").read_text())
        cache = Path(self.temp.name) / "cache" / manifest["version"]
        alphax_plugin.copy_tree(expected, cache)
        target = plugin_source / "skills/formal-development"
        for path in sorted(target.rglob("*"), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
        target.rmdir()

        result = alphax_plugin.verify_installed(
            self.source,
            plugin_source=plugin_source,
            cache_root=cache.parent,
        )

        self.assertFalse(result["ok"])
        self.assertIn("marketplace-content-drift", result["failure_classes"])

    def test_project_work_materializes_accepted_source_from_candidate_branch(self) -> None:
        self._git("switch", "-c", "feature")
        self._write("AGENTS.md", "candidate\n")
        self._git("add", "AGENTS.md")
        self._git("commit", "-m", "candidate")
        cache_root = Path(self.temp.name) / "accepted-cache"

        result = alphax_plugin.resolve_source(
            self.source,
            scope="project-work",
            accepted_ref="main",
            cache_root=cache_root,
        )

        resolved = Path(result["resolved_root"])
        self.assertEqual((resolved / "AGENTS.md").read_text(), "accepted\n")
        self.assertEqual(result["source_authority"], "accepted")
        self.assertEqual(result["source_ref"], "main")
        self.assertTrue(result["materialized"])
        self.assertNotEqual(result["source_commit"], self._git("rev-parse", "HEAD"))

    def test_candidate_package_embeds_accepted_source_for_project_invocations(self) -> None:
        accepted_commit = self._git("rev-parse", "main")
        self._git("switch", "-c", "feature")
        self._write("AGENTS.md", "candidate\n")
        self._git("add", "AGENTS.md")
        self._git("commit", "-m", "candidate")
        package = Path(self.temp.name) / "candidate-package"

        alphax_plugin.build_plugin(self.source, package, accepted_ref="main")
        result = alphax_plugin.resolve_invocation(package, scope="project-review")

        self.assertEqual((Path(result["resolved_root"]) / "AGENTS.md").read_text(), "accepted\n")
        self.assertEqual(result["source_commit"], accepted_commit)
        self.assertEqual(result["source_authority"], "accepted")
        self.assertEqual(result["package_source_authority"], "candidate")
        self.assertNotEqual(result["package_source_commit"], accepted_commit)

    def test_project_invocation_rejects_tampered_embedded_source(self) -> None:
        package = Path(self.temp.name) / "package"
        alphax_plugin.build_plugin(self.source, package)
        (package / "source/AGENTS.md").write_text("tampered\n", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "embedded Source content drift"):
            alphax_plugin.resolve_invocation(package, scope="project-work")

    def test_source_invocation_requires_and_identifies_live_checkout(self) -> None:
        package = Path(self.temp.name) / "package"
        alphax_plugin.build_plugin(self.source, package)
        self._git("switch", "-c", "feature")
        self._write("AGENTS.md", "candidate dirty\n")

        with self.assertRaisesRegex(ValueError, "live Source checkout"):
            alphax_plugin.resolve_invocation(package, scope="source-work")

        result = alphax_plugin.resolve_invocation(
            package,
            scope="source-work",
            source_root=self.source,
            accepted_ref="main",
        )
        self.assertEqual(result["resolved_root"], str(self.source.resolve()))
        self.assertEqual(result["source_authority"], "candidate")
        self.assertEqual(result["source_branch"], "feature")

    def test_source_work_records_candidate_working_tree_identity(self) -> None:
        self._git("switch", "-c", "feature")
        self._write("AGENTS.md", "candidate dirty\n")

        result = alphax_plugin.resolve_source(
            self.source,
            scope="source-work",
            accepted_ref="main",
            cache_root=Path(self.temp.name) / "cache",
        )

        self.assertEqual(result["resolved_root"], str(self.source.resolve()))
        self.assertEqual(result["source_branch"], "feature")
        self.assertEqual(result["source_authority"], "candidate")
        self.assertTrue(result["source_dirty"])
        self.assertFalse(result["materialized"])


if __name__ == "__main__":
    unittest.main()
