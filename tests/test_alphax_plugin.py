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


class ScriptedRunner:
    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def __call__(self, argv):
        self.calls.append(list(argv))
        code, stdout, stderr = self.responses[tuple(argv)]
        return subprocess.CompletedProcess(argv, code, stdout, stderr)


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
        self._write(
            "skills/formal-code-review/SKILL.md",
            "---\nname: formal-code-review\ndescription: Use when formal code review is requested.\n---\n# Formal Code Review\ndefault_mode: delegate\n",
        )
        self._write(
            "skills/formal-code-review/references/mode-and-evidence.md",
            "---\ntype: Reference\ntitle: Mode And Evidence\ndescription: fixture\n---\n# Mode And Evidence\n",
        )
        self._write(
            "skills/formal-code-review/references/use-cases/authority-and-promotion.md",
            "---\ntype: Reference\ntitle: Authority And Promotion\ndescription: fixture\n---\n# Authority And Promotion\n",
        )
        self._write(
            "skills/formal-code-review/references/use-cases/pattern-schema.md",
            "---\ntype: Reference\ntitle: Pattern Schema\ndescription: fixture\n---\n# Pattern Schema\n",
        )
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
        self.assertTrue((out / "skills/formal-code-review/SKILL.md").is_file())
        self.assertTrue(
            (out / "skills/formal-code-review/references/mode-and-evidence.md").is_file()
        )
        self.assertTrue(
            (out / "skills/formal-code-review/references/use-cases/authority-and-promotion.md").is_file()
        )
        self.assertEqual(
            (out / "skills/formal-development/references/rule.md").read_text(),
            "rule\n",
        )

    def test_real_formal_code_review_source_contract(self) -> None:
        skill = (ROOT / "skills/formal-code-review/SKILL.md").read_text(encoding="utf-8")
        mode = (
            ROOT / "skills/formal-code-review/references/mode-and-evidence.md"
        ).read_text(encoding="utf-8")
        authority = (
            ROOT
            / "skills/formal-code-review/references/use-cases/authority-and-promotion.md"
        ).read_text(encoding="utf-8")

        self.assertIn("name: formal-code-review", skill)
        self.assertIn("default_mode: delegate", skill)
        self.assertIn("managed_mode_requires_explicit_request: true", skill)
        self.assertIn("silent_mode_fallback: forbidden", skill)
        self.assertIn("review-coverage-incomplete", mode)
        self.assertIn("l2-contract-drift", mode)
        self.assertIn("project truth -> local review evidence -> sanitized pattern", authority)
        self.assertIn("Audit -> Confirm -> Apply", authority)
        self.assertIn("raw model reasoning", authority.lower())
        self.assertIn("forbid", authority.lower())

    def test_formal_development_composes_optional_code_review(self) -> None:
        formal = (ROOT / "skills/formal-development/SKILL.md").read_text(encoding="utf-8")
        coding = (
            ROOT / "skills/formal-development/references/coding-l0-l4.md"
        ).read_text(encoding="utf-8")

        self.assertIn("formal_code_review_gate:", formal)
        self.assertIn("skill: skills/formal-code-review/SKILL.md", formal)
        self.assertIn("required_when: user-or-project-review-gate", formal)
        self.assertIn("default_for_routine_review: delegation", formal)
        self.assertIn("does not make OCR mandatory", formal)
        self.assertIn("OCR review report", coding)
        self.assertIn("not human acceptance", coding)
        minimal_l4 = coding.split("Minimal coding L4:\n\n```yaml\n", 1)[1].split(
            "```", 1
        )[0]
        self.assertNotIn("OCR review report", minimal_l4)
        self.assertIn("Optional OCR review carrier", coding)

    def test_formal_code_review_routing_is_registered(self) -> None:
        invocation = (ROOT / "docs/agent-invocation-contract.md").read_text(encoding="utf-8")
        runbook = (ROOT / "alphaX/session-runbook.md").read_text(encoding="utf-8")
        operating = (ROOT / "alphaX/operating-system.md").read_text(encoding="utf-8")
        publication = (ROOT / "docs/alphax-plugin-publication.md").read_text(encoding="utf-8")
        manifest = json.loads((ROOT / "plugin/plugin.template.json").read_text(encoding="utf-8"))
        fixtures = json.loads((ROOT / "docs/agent-trigger-fixtures.json").read_text(encoding="utf-8"))
        review = next(item for item in fixtures["fixtures"] if item["id"] == "F11-formal-code-review")

        self.assertIn("formal_code_review:", invocation)
        self.assertIn("skills/formal-code-review/SKILL.md", invocation)
        self.assertIn("formal_code_review:", runbook)
        self.assertIn("formal_code_review:", operating)
        self.assertEqual(review, {
            "id": "F11-formal-code-review",
            "trigger": "用形式化研发的双模式代码审查检查这个分支",
            "expected_intent": "formal_code_review",
            "scope": "project work unless completion judgment is explicitly requested",
            "loop": "Project loop plus Formal Code Review",
            "must_read": [
                "skills/formal-development/SKILL.md",
                "skills/formal-code-review/SKILL.md",
                "target AGENTS.md",
                "current project source, contracts, and diff",
            ],
            "must_output": [
                "delegation mode by default or explicit managed mode",
                "review target and coverage",
                "verified findings",
                "L0-L3 routing",
                "validation evidence",
                "residual risk",
            ],
            "forbidden": [
                "silent mode fallback",
                "review output rewriting L0-L2",
                "automatic external write",
                "wiki-derived project decision",
            ],
        })
        self.assertIn("F01-F11", publication)
        self.assertIn("formal-code-review", manifest["keywords"])
        self.assertIn("Formal code review", manifest["interface"]["capabilities"])

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
        self.assertIn("Copy the resolved Source fields exactly", entry)
        self.assertIn("never append an intent or skill name", entry)
        self.assertIn("source_branch: <resolved source_branch>", entry)
        self.assertIn("source_ref: <resolved source_ref>", entry)
        self.assertNotIn("source_branch_or_ref:", entry)
        self.assertIn("P0 line must not prescribe an action", entry)
        self.assertIn("`durable_principle`", entry)
        self.assertIn("`short_lived_scaffold`", entry)
        self.assertIn("`prune_or_replace_action`", entry)
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
        self.assertEqual(manifest["interface"]["defaultPrompt"], [
            "@alphaX restore this project context.",
            "Use alphax:problem-decomposer on this task.",
            "Use alphax:formal-code-review to review this branch against main.",
        ])
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
        self.assertIn("pre-Develop P0 names no action", invocation)
        self.assertIn("project review starts with findings", invocation)
        self.assertIn("discovery or listing alone is missing evidence", invocation)
        self.assertIn("source review findings and calls concern Alpha Partner Source only", invocation)
        self.assertIn("Double Diamond output always maps", invocation)
        self.assertIn("path-specific evidence gaps and validation approaches", invocation)
        self.assertIn("copy scope and resolved source fields exactly", invocation)
        self.assertIn("scaffold half-life review names durable_principle", invocation)
        self.assertIn("never invent a business or user objective", decomposer)
        self.assertIn("explicit weak-layer call", decomposer)
        self.assertIn("path-specific evidence and validation", diamond)
        self.assertIn("smallest reversible pilot", diamond)
        self.assertIn("must not name a favored candidate", diamond)
        self.assertIn("P0 must not prescribe an action", diamond)
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

    def _doctor_responses(
        self,
        *,
        git_version: str = "2.41.0",
        ocr_code: int = 0,
        marketplaces: list[dict[str, object]] | None = None,
        plugins: list[dict[str, object]] | None = None,
        node_version: str = "v20.0.0",
        npm_version: str = "10.0.0",
    ) -> dict[tuple[str, ...], tuple[int, str, str]]:
        responses = {
            ("git", "--version"): (0, f"git version {git_version}\\n", ""),
            ("ocr", "version"): (ocr_code, "ocr 1.2.3\\n" if not ocr_code else "", "not found"),
            ("codex", "plugin", "marketplace", "list", "--json"): (
                0,
                json.dumps({"marketplaces": marketplaces or []}),
                "",
            ),
            ("codex", "plugin", "list", "--json"): (
                0,
                json.dumps({"plugins": plugins or []}),
                "",
            ),
        }
        if ocr_code:
            responses[("node", "--version")] = (0, f"{node_version}\\n", "")
            responses[("npm", "--version")] = (0, f"{npm_version}\\n", "")
        return responses

    def _ready_doctor_paths(self) -> tuple[Path, Path]:
        plugin_source = Path(self.temp.name) / "marketplace" / "alphax"
        built = alphax_plugin.build_plugin(self.source, plugin_source)
        cache_root = Path(self.temp.name) / "cache" / "personal" / "alphax"
        alphax_plugin.copy_tree(plugin_source, cache_root / built["version"])
        return plugin_source, cache_root

    def test_doctor_cli_parser_and_exit_contract(self) -> None:
        self.assertFalse(alphax_plugin.parse_args(["doctor"]).install)
        self.assertTrue(alphax_plugin.parse_args(["doctor", "--install", "--json"]).json)
        self.assertEqual(alphax_plugin.doctor_exit_code({"overall": "ready"}), 0)
        self.assertEqual(alphax_plugin.doctor_exit_code({"overall": "action-required"}), 2)
        self.assertEqual(alphax_plugin.doctor_exit_code({"overall": "blocked"}), 1)

    def test_formal_review_adopter_onboarding_is_a_source_contract(self) -> None:
        publication = (ROOT / "docs/alphax-plugin-publication.md").read_text(encoding="utf-8")
        root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese_readme = (ROOT / "docs/README.zh-CN.md").read_text(encoding="utf-8")
        plugin_readme = (ROOT / "plugin/README.md").read_text(encoding="utf-8")
        design = (ROOT / "docs/formal-code-review-integration.md").read_text(encoding="utf-8")
        verifier = (ROOT / "scripts/verify-alpha-source.sh").read_text(encoding="utf-8")
        implementation = (ROOT / "scripts/alphax_plugin.py").read_text(encoding="utf-8")
        self.assertIn('has_fixed() { rg -n -F -- "$1" "$ROOT/$2"', verifier)

        quickstart = (
            "python3 scripts/alphax_plugin.py doctor",
            "python3 scripts/alphax_plugin.py doctor --install",
        )
        for text in (publication, root_readme, chinese_readme):
            for command in quickstart:
                self.assertIn(command, text)
        for text in (root_readme, chinese_readme):
            self.assertEqual(text.count("python3 scripts/alphax_plugin.py doctor\n"), 1)
            self.assertEqual(text.count("python3 scripts/alphax_plugin.py doctor --install\n"), 1)
        self.assertIn("python3 scripts/alphax_plugin.py doctor --json", publication)
        self.assertIn("codex plugin marketplace list --json", publication)
        self.assertIn("codex plugin list --json", publication)
        for identity in (
            "@alibaba-group/open-code-review",
            "https://github.com/alibaba/open-code-review.git",
            "open-code-review-codex@open-code-review",
            "managed-llm-unapproved",
            "clean accepted Source",
            "ready: 0",
            "blocked: 1",
            "action-required: 2",
        ):
            self.assertIn(identity, publication)
        self.assertIn("docs/alphax-plugin-publication.md", plugin_readme)
        self.assertNotIn("python3 scripts/alphax_plugin.py doctor", plugin_readme)
        self.assertIn("](alphax-plugin-publication.md)", chinese_readme)
        self.assertIn("adopter_setup_implementation_status: validated-local", design)
        self.assertIn("managed_mode_evidence: guarded-unproven", design)
        self.assertIn("managed_mode_failure_class: managed-llm-unapproved", design)
        for constant in (
            'OCR_PACKAGE = "@alibaba-group/open-code-review"',
            'OCR_MARKETPLACE_REPOSITORY = "https://github.com/alibaba/open-code-review.git"',
            'OCR_PLUGIN_SELECTOR = "open-code-review-codex@open-code-review"',
            "allow_candidate=False",
        ):
            self.assertIn(constant, implementation)
            self.assertIn(constant, verifier)

    def test_source_verifier_treats_dash_prefixed_private_pattern_as_literal(self) -> None:
        verifier = (ROOT / "scripts/verify-alpha-source.sh").read_text(encoding="utf-8")
        helper = verifier.split("required_paths=(", 1)[0]
        root_assignment = 'ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"'
        self.assertIn(root_assignment, helper)
        helper = helper.replace(root_assignment, 'ROOT="$1"')

        with tempfile.TemporaryDirectory() as temporary:
            source_root = Path(temporary)
            (source_root / "marker.md").write_text("-n\n", encoding="utf-8")
            result = subprocess.run(
                ["bash", "-c", helper + '\nsource_rg -n -F "$2"', "bash", str(source_root), "-n"],
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("marker.md", result.stdout)

    def test_source_verifier_binds_doctor_installer_candidate_gate(self) -> None:
        verifier = (ROOT / "scripts/verify-alpha-source.sh").read_text(encoding="utf-8")
        helper = verifier.split("required_paths=(", 1)[0]
        implementation = (ROOT / "scripts/alphax_plugin.py").read_text(encoding="utf-8")
        self.assertIn("\nverify_doctor_installer_binding\n", verifier)

        def verify(source: Path) -> subprocess.CompletedProcess[str]:
            return subprocess.run(
                ["bash", "-c", helper + '\nverify_doctor_installer_binding "$2"', "bash", ".", str(source)],
                text=True,
                capture_output=True,
                check=False,
            )

        with tempfile.TemporaryDirectory() as temporary:
            temporary_root = Path(temporary)
            current = temporary_root / "current.py"
            current.write_text(implementation, encoding="utf-8")
            changed_value = temporary_root / "changed-value.py"
            changed_value.write_text(
                implementation.replace("allow_candidate=False", "allow_candidate=True", 1),
                encoding="utf-8",
            )
            moved_value = temporary_root / "moved-value.py"
            moved_value.write_text(
                implementation.replace("allow_candidate=False", "candidate_gate_removed=False", 1)
                + "\nallow_candidate=False\n",
                encoding="utf-8",
            )

            self.assertEqual(verify(current).returncode, 0)
            self.assertNotEqual(verify(changed_value).returncode, 0)
            self.assertNotEqual(verify(moved_value).returncode, 0)

    def test_render_doctor_covers_result_fields_without_unbounded_payloads(self) -> None:
        result = {
            "overall": "action-required",
            "checks": [
                {
                    "id": "git",
                    "status": "pass",
                    "observed": "2.41.0",
                    "required": ">=2.41",
                    "action": None,
                    "unexpected": "OPENAI_API_KEY=sentinel-secret",
                },
                {
                    "id": "ocr-cli",
                    "status": "missing",
                    "observed": None,
                    "required": "@alibaba-group/open-code-review",
                    "action": "install @alibaba-group/open-code-review",
                },
            ],
            "changes": [
                {
                    "id": "ocr-cli",
                    "command_class": "npm-install",
                    "status": "failed",
                    "action": "install OCR CLI manually and retry",
                }
            ],
            "residual_risk": ["managed-llm-unapproved"],
        }

        rendered = alphax_plugin.render_doctor(result)

        for value in (
            "action-required",
            "git",
            "pass",
            "ocr-cli",
            "missing",
            "failed",
            "install @alibaba-group/open-code-review",
            "managed-llm-unapproved",
        ):
            self.assertIn(value, rendered)
        self.assertNotIn("sentinel-secret", rendered)

    def test_doctor_probe_secret_is_absent_from_json_and_human_output(self) -> None:
        responses = self._doctor_responses(ocr_code=127)
        responses[("ocr", "version")] = (127, "", "OPENAI_API_KEY=sentinel-secret")
        result = alphax_plugin.doctor_setup(
            self.source,
            command_runner=ScriptedRunner(responses),
            plugin_source=Path(self.temp.name) / "missing-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "missing-cache" / "alphax",
        )

        self.assertNotIn("sentinel-secret", json.dumps(result))
        self.assertNotIn("sentinel-secret", alphax_plugin.render_doctor(result))

    def test_doctor_ready_is_read_only_and_reports_managed_gate(self) -> None:
        plugin_source, cache_root = self._ready_doctor_paths()
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[
                    {
                        "name": "open-code-review",
                        "repository": "https://github.com/alibaba/open-code-review.git",
                    }
                ],
                plugins=[
                    {
                        "id": "open-code-review-codex@open-code-review",
                        "enabled": True,
                    }
                ],
            )
        )

        result = alphax_plugin.doctor_setup(
            self.source,
            command_runner=runner,
            plugin_source=plugin_source,
            cache_root=cache_root,
        )

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(result["mode"], "doctor")
        self.assertEqual(result["overall"], "ready")
        self.assertEqual(result["changes"], [])
        self.assertEqual(result["residual_risk"], ["managed-llm-unapproved"])
        self.assertFalse(any("add" in call or "install" in call for call in runner.calls))

    def test_doctor_missing_dependencies_returns_ordered_actions(self) -> None:
        runner = ScriptedRunner(self._doctor_responses(ocr_code=127))

        result = alphax_plugin.doctor_setup(
            self.source,
            command_runner=runner,
            plugin_source=Path(self.temp.name) / "missing-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "missing-cache" / "alphax",
        )

        self.assertEqual(result["overall"], "action-required")
        self.assertEqual(
            [check["id"] for check in result["checks"] if check["status"] == "missing"],
            ["ocr-cli", "ocr-marketplace", "ocr-plugin", "alphax-parity"],
        )

    def test_doctor_install_applies_only_missing_steps_in_order(self) -> None:
        state = {"ocr": False, "marketplace": False, "plugin": False, "alphax": False}

        class InstallRunner:
            def __init__(self) -> None:
                self.calls: list[list[str]] = []

            def __call__(self, argv: list[str]) -> subprocess.CompletedProcess[str]:
                self.calls.append(list(argv))
                if argv == ["git", "--version"]:
                    return subprocess.CompletedProcess(argv, 0, "git version 2.41.0\n", "")
                if argv == ["ocr", "version"]:
                    return subprocess.CompletedProcess(argv, 0 if state["ocr"] else 127, "ocr 1.2.3\n" if state["ocr"] else "", "")
                if argv == ["node", "--version"]:
                    return subprocess.CompletedProcess(argv, 0, "v20.0.0\n", "")
                if argv == ["npm", "--version"]:
                    return subprocess.CompletedProcess(argv, 0, "10.0.0\n", "")
                if argv == ["codex", "plugin", "marketplace", "list", "--json"]:
                    marketplaces = ([{"name": "open-code-review", "repository": alphax_plugin.OCR_MARKETPLACE_REPOSITORY}]
                                    if state["marketplace"] else [])
                    return subprocess.CompletedProcess(argv, 0, json.dumps({"marketplaces": marketplaces}), "")
                if argv == ["codex", "plugin", "list", "--json"]:
                    plugins = ([{"id": alphax_plugin.OCR_PLUGIN_SELECTOR, "enabled": True}]
                               if state["plugin"] else [])
                    return subprocess.CompletedProcess(argv, 0, json.dumps({"plugins": plugins}), "")
                if argv == ["npm", "install", "-g", alphax_plugin.OCR_PACKAGE]:
                    state["ocr"] = True
                    return subprocess.CompletedProcess(argv, 0, "", "")
                if argv == ["codex", "plugin", "marketplace", "add", "alibaba/open-code-review", "--ref", "main", "--json"]:
                    state["marketplace"] = True
                    return subprocess.CompletedProcess(argv, 0, "", "")
                if argv == ["codex", "plugin", "add", alphax_plugin.OCR_PLUGIN_SELECTOR, "--json"]:
                    state["plugin"] = True
                    return subprocess.CompletedProcess(argv, 0, "", "")
                self.fail(f"unexpected command: {argv}")

        runner = InstallRunner()
        plugin_source = Path(self.temp.name) / "marketplace" / "alphax"
        cache_root = Path(self.temp.name) / "cache" / "personal" / "alphax"
        installer_calls: list[dict[str, object]] = []

        def verifier(*_args, **_kwargs):
            cache = cache_root / "installed" if state["alphax"] else None
            return {"ok": state["alphax"], "cache": str(cache) if cache else None}

        def installer(*_args, **kwargs):
            self.assertFalse(kwargs["allow_candidate"])
            installer_calls.append(kwargs)
            state["alphax"] = True
            plugin_source.mkdir(parents=True)
            (cache_root / "installed").mkdir(parents=True)
            return {"ok": True}

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            alphax_verifier=verifier,
            alphax_installer=installer,
            plugin_source=plugin_source,
            cache_root=cache_root,
        )

        self.assertEqual(
            [(c["id"], c["command_class"], c["status"]) for c in result["changes"]],
            [
                ("ocr-cli", "npm-install", "applied"),
                ("ocr-marketplace", "marketplace-add", "applied"),
                ("ocr-plugin", "plugin-install", "applied"),
                ("alphax", "alphax-install", "applied"),
            ],
        )
        self.assertEqual(result["overall"], "ready")
        self.assertEqual(len(installer_calls), 1)

    def test_doctor_install_marketplace_failure_stops_without_stderr(self) -> None:
        state = {"ocr": False, "marketplace": False, "plugin": False}

        class FailingMarketplaceRunner:
            def __init__(self) -> None:
                self.calls: list[list[str]] = []

            def __call__(self, argv: list[str]) -> subprocess.CompletedProcess[str]:
                self.calls.append(list(argv))
                responses = {
                    ("git", "--version"): (0, "git version 2.41.0\n", ""),
                    ("ocr", "version"): (0 if state["ocr"] else 127, "ocr 1.2.3\n" if state["ocr"] else "", ""),
                    ("node", "--version"): (0, "v20.0.0\n", ""),
                    ("npm", "--version"): (0, "10.0.0\n", ""),
                    ("codex", "plugin", "marketplace", "list", "--json"): (0, json.dumps({"marketplaces": []}), ""),
                    ("codex", "plugin", "list", "--json"): (0, json.dumps({"plugins": []}), ""),
                    ("npm", "install", "-g", alphax_plugin.OCR_PACKAGE): (0, "", ""),
                    ("codex", "plugin", "marketplace", "add", "alibaba/open-code-review", "--ref", "main", "--json"): (1, "", "marketplace failed"),
                }
                if argv == ["npm", "install", "-g", alphax_plugin.OCR_PACKAGE]:
                    state["ocr"] = True
                code, stdout, stderr = responses[tuple(argv)]
                return subprocess.CompletedProcess(argv, code, stdout, stderr)

        runner = FailingMarketplaceRunner()
        installer_calls: list[dict[str, object]] = []
        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            alphax_installer=lambda *_args, **kwargs: installer_calls.append(kwargs),
            plugin_source=Path(self.temp.name) / "missing-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "missing-cache" / "alphax",
        )

        self.assertEqual(
            [(change["id"], change["status"]) for change in result["changes"]],
            [("ocr-cli", "applied"), ("ocr-marketplace", "failed")],
        )
        self.assertNotIn("stderr", json.dumps(result))
        self.assertFalse(any(call[:4] == ["codex", "plugin", "add", alphax_plugin.OCR_PLUGIN_SELECTOR] for call in runner.calls))
        self.assertEqual(installer_calls, [])
        self.assertEqual(next(check for check in result["checks"] if check["id"] == "ocr-cli")["status"], "pass")
        self.assertNotEqual(next(check for check in result["checks"] if check["id"] == "ocr-marketplace")["status"], "pass")
        self.assertEqual(result["overall"], "action-required")

    def test_doctor_install_ready_records_already_satisfied_without_mutation(self) -> None:
        plugin_source, cache_root = self._ready_doctor_paths()
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[{"name": "open-code-review", "repository": alphax_plugin.OCR_MARKETPLACE_REPOSITORY}],
                plugins=[{"id": alphax_plugin.OCR_PLUGIN_SELECTOR, "enabled": True}],
            )
        )

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            alphax_installer=lambda *_args, **_kwargs: self.fail("installer must not run"),
            plugin_source=plugin_source,
            cache_root=cache_root,
        )

        self.assertEqual([change["status"] for change in result["changes"]], ["already-satisfied"] * 4)
        self.assertFalse(any("install" in call or "add" in call for call in runner.calls))

    def test_doctor_install_candidate_source_skips_alphax_installer(self) -> None:
        self._write("AGENTS.md", "dirty candidate\n")
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[{"name": "open-code-review", "repository": alphax_plugin.OCR_MARKETPLACE_REPOSITORY}],
                plugins=[{"id": alphax_plugin.OCR_PLUGIN_SELECTOR, "enabled": True}],
            )
        )
        installer_calls: list[dict[str, object]] = []

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            alphax_installer=lambda *_args, **kwargs: installer_calls.append(kwargs),
            plugin_source=Path(self.temp.name) / "candidate-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "candidate-cache" / "alphax",
        )

        self.assertEqual(installer_calls, [])
        self.assertEqual(result["changes"][-1]["id"], "alphax")
        self.assertEqual(result["changes"][-1]["status"], "skipped")

    def test_doctor_install_windows_skips_mutations_and_returns_manual_actions(self) -> None:
        runner = ScriptedRunner(self._doctor_responses(ocr_code=127))

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            platform_name="win32",
            plugin_source=Path(self.temp.name) / "windows-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "windows-cache" / "alphax",
        )

        self.assertEqual([change["status"] for change in result["changes"]], ["skipped"] * 4)
        self.assertTrue(all(change["action"] for change in result["changes"]))
        self.assertFalse(any("install" in call or "add" in call for call in runner.calls))

    def test_doctor_install_valid_ocr_never_probes_or_installs_npm(self) -> None:
        plugin_source, cache_root = self._ready_doctor_paths()
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[{"name": "open-code-review", "repository": alphax_plugin.OCR_MARKETPLACE_REPOSITORY}],
                plugins=[{"id": alphax_plugin.OCR_PLUGIN_SELECTOR, "enabled": True}],
            )
        )

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            plugin_source=plugin_source,
            cache_root=cache_root,
        )

        self.assertEqual(result["overall"], "ready")
        self.assertFalse(any(call[0] == "npm" for call in runner.calls))

    def test_doctor_install_never_replaces_mismatched_marketplace_source(self) -> None:
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[{"name": "open-code-review", "repository": "https://example.invalid/fork.git"}],
            )
        )

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            plugin_source=Path(self.temp.name) / "mismatch-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "mismatch-cache" / "alphax",
        )

        self.assertEqual(result["changes"][1]["status"], "skipped")
        self.assertNotIn(
            ["codex", "plugin", "marketplace", "add", "alibaba/open-code-review", "--ref", "main", "--json"],
            runner.calls,
        )

    def test_doctor_install_requires_literal_true_for_mutation(self) -> None:
        for value in (1, "false"):
            with self.subTest(value=value):
                responses = self._doctor_responses(ocr_code=127)
                mutation = ("npm", "install", "-g", alphax_plugin.OCR_PACKAGE)
                responses[mutation] = (0, "", "")
                runner = ScriptedRunner(responses)

                result = alphax_plugin.doctor_setup(
                    self.source,
                    install=value,
                    command_runner=runner,
                    plugin_source=Path(self.temp.name) / "literal-true-marketplace" / "alphax",
                    cache_root=Path(self.temp.name) / "literal-true-cache" / "alphax",
                )

                self.assertEqual(result["mode"], "doctor")
                self.assertEqual(result["changes"], [])
                self.assertNotIn(list(mutation), runner.calls)

    def test_doctor_install_repairs_missing_ocr_before_unavailable_codex(self) -> None:
        state = {"ocr": False}

        class CodexUnavailableRunner:
            def __init__(self) -> None:
                self.calls: list[list[str]] = []

            def __call__(self, argv: list[str]) -> subprocess.CompletedProcess[str]:
                self.calls.append(list(argv))
                responses = {
                    ("git", "--version"): (0, "git version 2.41.0\n", ""),
                    ("ocr", "version"): (0 if state["ocr"] else 127, "ocr 1.2.3\n" if state["ocr"] else "", ""),
                    ("node", "--version"): (0, "v20.0.0\n", ""),
                    ("npm", "--version"): (0, "10.0.0\n", ""),
                    ("codex", "plugin", "marketplace", "list", "--json"): (127, "", "not found"),
                    ("codex", "plugin", "list", "--json"): (127, "", "not found"),
                    ("npm", "install", "-g", alphax_plugin.OCR_PACKAGE): (0, "", ""),
                }
                if argv == ["npm", "install", "-g", alphax_plugin.OCR_PACKAGE]:
                    state["ocr"] = True
                code, stdout, stderr = responses[tuple(argv)]
                return subprocess.CompletedProcess(argv, code, stdout, stderr)

        runner = CodexUnavailableRunner()
        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            plugin_source=Path(self.temp.name) / "codex-unavailable-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "codex-unavailable-cache" / "alphax",
        )

        self.assertEqual(
            [(change["id"], change["status"]) for change in result["changes"]],
            [("ocr-cli", "applied"), ("ocr-marketplace", "skipped")],
        )
        self.assertEqual(next(check for check in result["checks"] if check["id"] == "ocr-cli")["status"], "pass")
        self.assertEqual(result["overall"], "blocked")

    def test_doctor_install_keeps_existing_ocr_satisfied_when_codex_is_unavailable(self) -> None:
        responses = self._doctor_responses(ocr_code=0)
        responses[("codex", "plugin", "marketplace", "list", "--json")] = (127, "", "not found")
        responses[("codex", "plugin", "list", "--json")] = (127, "", "not found")
        runner = ScriptedRunner(responses)

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            plugin_source=Path(self.temp.name) / "codex-unavailable-existing-ocr" / "alphax",
            cache_root=Path(self.temp.name) / "codex-unavailable-existing-cache" / "alphax",
        )

        self.assertEqual(result["changes"][0]["id"], "ocr-cli")
        self.assertEqual(result["changes"][0]["status"], "already-satisfied")

    def test_doctor_install_adapts_single_argument_runner_for_alphax_installer(self) -> None:
        plugin_source = Path(self.temp.name) / "adapter-marketplace" / "alphax"
        cache_root = Path(self.temp.name) / "adapter-cache" / "alphax"
        installed = {"value": False}
        responses = self._doctor_responses(
            marketplaces=[{"name": "open-code-review", "repository": alphax_plugin.OCR_MARKETPLACE_REPOSITORY}],
            plugins=[{"id": alphax_plugin.OCR_PLUGIN_SELECTOR, "enabled": True}],
        )
        responses[("codex", "plugin", "add", "alphax@personal", "--json")] = (0, "", "")
        runner = ScriptedRunner(responses)

        def verifier(*_args, **_kwargs):
            cache = cache_root / "installed" if installed["value"] else None
            return {"ok": installed["value"], "cache": str(cache) if cache else None}

        def installer(_source_root, *, runner, **_kwargs):
            completed = runner(
                ["codex", "plugin", "add", "alphax@personal", "--json"],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0)
            installed["value"] = True
            plugin_source.mkdir(parents=True)
            (cache_root / "installed").mkdir(parents=True)

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            alphax_verifier=verifier,
            alphax_installer=installer,
            plugin_source=plugin_source,
            cache_root=cache_root,
        )

        self.assertEqual(result["changes"][-1]["status"], "applied")

    def test_doctor_install_bounds_alphax_installer_exception(self) -> None:
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[{"name": "open-code-review", "repository": alphax_plugin.OCR_MARKETPLACE_REPOSITORY}],
                plugins=[{"id": alphax_plugin.OCR_PLUGIN_SELECTOR, "enabled": True}],
            )
        )

        def installer(*_args, **_kwargs):
            raise TypeError("private installer detail")

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            alphax_installer=installer,
            plugin_source=Path(self.temp.name) / "exception-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "exception-cache" / "alphax",
        )

        self.assertEqual(result["changes"][-1]["status"], "failed")
        self.assertNotIn("private installer detail", json.dumps(result))

    def test_doctor_install_freebsd_is_manual_only(self) -> None:
        responses = self._doctor_responses(ocr_code=127)
        mutation = ("npm", "install", "-g", alphax_plugin.OCR_PACKAGE)
        responses[mutation] = (0, "", "")
        runner = ScriptedRunner(responses)

        result = alphax_plugin.doctor_setup(
            self.source,
            install=True,
            command_runner=runner,
            platform_name="freebsd",
            plugin_source=Path(self.temp.name) / "freebsd-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "freebsd-cache" / "alphax",
        )

        self.assertEqual([change["status"] for change in result["changes"]], ["skipped"] * 4)
        self.assertTrue(all(change["action"] for change in result["changes"]))
        self.assertNotIn(list(mutation), runner.calls)

    def test_doctor_rejects_incompatible_git_and_node(self) -> None:
        runner = ScriptedRunner(
            self._doctor_responses(git_version="2.40.0", ocr_code=127, node_version="v13.0.0")
        )

        result = alphax_plugin.doctor_setup(
            self.source,
            command_runner=runner,
            plugin_source=Path(self.temp.name) / "missing-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "missing-cache" / "alphax",
        )

        self.assertEqual(result["overall"], "blocked")

    def test_doctor_blocks_marketplace_source_mismatch(self) -> None:
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[
                    {
                        "name": "open-code-review",
                        "repository": "https://example.invalid/fork.git",
                    }
                ]
            )
        )

        result = alphax_plugin.doctor_setup(
            self.source,
            command_runner=runner,
            plugin_source=Path(self.temp.name) / "missing-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "missing-cache" / "alphax",
        )

        marketplace = next(check for check in result["checks"] if check["id"] == "ocr-marketplace")
        self.assertEqual(marketplace["status"], "blocked")
        self.assertFalse(marketplace["installable"])
        self.assertNotIn("example.invalid", json.dumps(result))

    def test_doctor_blocks_fork_when_metadata_mentions_approved_source(self) -> None:
        runner = ScriptedRunner(
            self._doctor_responses(
                marketplaces=[
                    {
                        "name": "open-code-review",
                        "repository": "https://example.invalid/fork.git",
                        "metadata": {
                            "documentation": "https://github.com/alibaba/open-code-review.git"
                        },
                    }
                ]
            )
        )

        result = alphax_plugin.doctor_setup(
            self.source,
            command_runner=runner,
            plugin_source=Path(self.temp.name) / "missing-marketplace" / "alphax",
            cache_root=Path(self.temp.name) / "missing-cache" / "alphax",
        )

        marketplace = next(check for check in result["checks"] if check["id"] == "ocr-marketplace")
        self.assertEqual(marketplace["status"], "blocked")
        self.assertFalse(marketplace["installable"])
        self.assertNotIn("example.invalid", json.dumps(result))


if __name__ == "__main__":
    unittest.main()
