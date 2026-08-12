#!/usr/bin/env python3
"""Build, verify, install, and resolve the alphaX Codex plugin from Source."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from typing import Any, Callable


SOURCE_SCOPES = {"source-work", "source-review"}
PROJECT_SCOPES = {"project-work", "project-review"}
IGNORED_NAMES = {".DS_Store", "__pycache__"}
DOCTOR_SCHEMA_VERSION = 1
OCR_PACKAGE = "@alibaba-group/open-code-review"
OCR_MARKETPLACE_REPOSITORY = "https://github.com/alibaba/open-code-review.git"
OCR_PLUGIN_SELECTOR = "open-code-review-codex@open-code-review"


def run_command(
    argv: list[str], **_kwargs: Any
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(argv, text=True, capture_output=True, check=False)


def run_git(source_root: Path, *args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", "-C", str(source_root), *args],
        text=True,
        capture_output=True,
        check=False,
    )
    if check and completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip()
        raise ValueError(f"git {' '.join(args)} failed: {message}")
    return completed.stdout.strip()


def current_branch(source_root: Path) -> str:
    branch = run_git(source_root, "branch", "--show-current")
    return branch or "detached"


def is_dirty(source_root: Path) -> bool:
    return bool(run_git(source_root, "status", "--porcelain", "--untracked-files=all"))


def resolve_accepted_ref(source_root: Path, requested: str | None = None) -> str:
    candidates = [requested] if requested else []
    candidates.extend(["origin/main", "main"])
    for candidate in candidates:
        if not candidate:
            continue
        completed = subprocess.run(
            ["git", "-C", str(source_root), "rev-parse", "--verify", f"{candidate}^{{commit}}"],
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode == 0:
            return candidate
    raise ValueError("no accepted Source ref found; pass --accepted-ref")


def canonical_files(source_root: Path) -> list[Path]:
    required = [
        source_root / "plugin/plugin.template.json",
        source_root / "plugin/README.md",
        source_root / "plugin/skills/alphax/SKILL.md",
        source_root / "assets/icon.png",
        source_root / "scripts/alphax_plugin.py",
    ]
    for path in required:
        if not path.is_file():
            raise ValueError(f"missing canonical plugin input: {path.relative_to(source_root)}")
    source_skills = source_root / "skills"
    if not source_skills.is_dir():
        raise ValueError("missing canonical plugin input: skills/")
    visible = run_git(
        source_root,
        "ls-files",
        "--cached",
        "--others",
        "--exclude-standard",
    ).splitlines()
    files = [source_root / relative for relative in visible]
    files = [
        path
        for path in files
        if path.is_file()
        and not any(part in IGNORED_NAMES for part in path.relative_to(source_root).parts)
        and path.suffix not in {".pyc", ".pyo"}
    ]
    return sorted(set(files), key=lambda path: str(path.relative_to(source_root)))


def source_fingerprint(source_root: Path) -> str:
    digest = hashlib.sha256()
    for path in canonical_files(source_root):
        relative = path.relative_to(source_root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def source_identity(source_root: Path, accepted_ref: str | None = None) -> dict[str, Any]:
    source_root = source_root.resolve()
    accepted_ref = resolve_accepted_ref(source_root, accepted_ref)
    commit = run_git(source_root, "rev-parse", "HEAD")
    accepted_commit = run_git(source_root, "rev-parse", accepted_ref)
    dirty = is_dirty(source_root)
    branch = current_branch(source_root)
    return {
        "source_root": str(source_root),
        "source_commit": commit,
        "source_branch": branch,
        "working_branch": branch,
        "accepted_ref": accepted_ref,
        "accepted_commit": accepted_commit,
        "source_dirty": dirty,
        "source_fingerprint": source_fingerprint(source_root),
        "source_authority": "accepted" if commit == accepted_commit and not dirty else "candidate",
    }


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def copy_tree(source: Path, target: Path) -> None:
    remove_path(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(*IGNORED_NAMES))


def tree_fingerprint(root: Path) -> str:
    digest = hashlib.sha256()
    for relative, file_digest in sorted(tree_files(root).items()):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_digest.encode("ascii"))
        digest.update(b"\0")
    return digest.hexdigest()


def extract_ref(source_root: Path, commit: str, destination: Path) -> None:
    completed = subprocess.run(
        ["git", "-C", str(source_root), "archive", "--format=tar", commit],
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise ValueError(completed.stderr.decode(errors="replace").strip())
    safe_extract_archive(completed.stdout, destination)


def build_plugin(
    source_root: Path,
    out_dir: Path,
    *,
    allow_dirty: bool = False,
    accepted_ref: str | None = None,
) -> dict[str, Any]:
    source_root = source_root.resolve()
    out_dir = out_dir.resolve()
    identity = source_identity(source_root, accepted_ref)
    if identity["source_dirty"] and not allow_dirty:
        raise ValueError("dirty Source cannot produce a publishable plugin; use allow_dirty only for candidate tests")

    template = json.loads((source_root / "plugin/plugin.template.json").read_text(encoding="utf-8"))
    base_version = str(template["version"]).split("+", 1)[0]
    if identity["source_dirty"]:
        suffix = f"dirty-{identity['source_fingerprint'][:12]}"
    else:
        suffix = identity["source_commit"][:12]
    version = f"{base_version}+codex.{suffix}"
    template["version"] = version

    remove_path(out_dir)
    (out_dir / ".codex-plugin").mkdir(parents=True)
    (out_dir / "skills").mkdir()
    (out_dir / "assets").mkdir()
    (out_dir / "bin").mkdir()
    extract_ref(source_root, identity["accepted_commit"], out_dir / "source")
    (out_dir / ".codex-plugin/plugin.json").write_text(
        json.dumps(template, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    shutil.copy2(source_root / "plugin/README.md", out_dir / "README.md")
    shutil.copy2(source_root / "assets/icon.png", out_dir / "assets/icon.png")
    shutil.copy2(source_root / "scripts/alphax_plugin.py", out_dir / "bin/alphax_plugin.py")
    shutil.copytree(
        source_root / "plugin/skills/alphax",
        out_dir / "skills/alphax",
        ignore=shutil.ignore_patterns(*IGNORED_NAMES),
    )
    for skill_dir in sorted((source_root / "skills").iterdir()):
        if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").is_file():
            continue
        shutil.copytree(
            skill_dir,
            out_dir / "skills" / skill_dir.name,
            ignore=shutil.ignore_patterns(*IGNORED_NAMES),
        )

    provenance = {
        "schema_version": 2,
        "source_repository": "alpha-partner",
        "source_commit": identity["source_commit"],
        "source_branch": identity["source_branch"],
        "source_ref": identity["accepted_ref"],
        "accepted_commit": identity["accepted_commit"],
        "source_authority": identity["source_authority"],
        "source_dirty": identity["source_dirty"],
        "source_fingerprint": identity["source_fingerprint"],
        "package_source_commit": identity["source_commit"],
        "package_source_branch": identity["source_branch"],
        "package_source_authority": identity["source_authority"],
        "embedded_source_commit": identity["accepted_commit"],
        "embedded_source_ref": identity["accepted_ref"],
        "embedded_source_authority": "accepted",
        "embedded_source_fingerprint": tree_fingerprint(out_dir / "source"),
        "package_version": version,
        "builder": "scripts/alphax_plugin.py",
    }
    (out_dir / ".alphax-source.json").write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {**provenance, "version": version, "out_dir": str(out_dir)}


def tree_files(root: Path) -> dict[str, str]:
    if not root.is_dir():
        return {}
    result: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in IGNORED_NAMES for part in path.parts):
            continue
        relative = path.relative_to(root).as_posix()
        result[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def compare_trees(expected: Path, actual: Path) -> list[str]:
    expected_files = tree_files(expected)
    actual_files = tree_files(actual)
    diffs: list[str] = []
    for path in sorted(set(expected_files) - set(actual_files)):
        diffs.append(f"missing:{path}")
    for path in sorted(set(actual_files) - set(expected_files)):
        diffs.append(f"extra:{path}")
    for path in sorted(set(expected_files) & set(actual_files)):
        if expected_files[path] != actual_files[path]:
            diffs.append(f"content:{path}")
    return diffs


def validate_built_plugin(plugin_root: Path) -> list[str]:
    failures: list[str] = []
    manifest_path = plugin_root / ".codex-plugin/plugin.json"
    provenance_path = plugin_root / ".alphax-source.json"
    if not manifest_path.is_file():
        failures.append("missing-manifest")
        return failures
    if not provenance_path.is_file():
        failures.append("missing-provenance")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        failures.append("invalid-manifest")
        return failures
    if manifest.get("name") != "alphax":
        failures.append("wrong-plugin-name")
    if not isinstance(manifest.get("version"), str) or "+codex." not in manifest["version"]:
        failures.append("version-missing-source-identity")
    skills = plugin_root / "skills"
    if not (skills / "alphax/SKILL.md").is_file():
        failures.append("missing-entry-skill")
    if not (plugin_root / "bin/alphax_plugin.py").is_file():
        failures.append("missing-invocation-resolver")
    if not (plugin_root / "source/AGENTS.md").is_file():
        failures.append("missing-embedded-source")
    return failures


def verify_source(source_root: Path, *, allow_dirty: bool = True) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="alphax-plugin-source-") as tmp:
        first = Path(tmp) / "first"
        second = Path(tmp) / "second"
        build = build_plugin(source_root, first, allow_dirty=allow_dirty)
        build_plugin(source_root, second, allow_dirty=allow_dirty)
        diffs = compare_trees(first, second)
        failures = validate_built_plugin(first)
        source_skill_names = sorted(
            path.parent.name for path in (source_root / "skills").glob("*/SKILL.md")
        )
        built_skill_names = sorted(
            path.parent.name for path in (first / "skills").glob("*/SKILL.md") if path.parent.name != "alphax"
        )
        if source_skill_names != built_skill_names:
            failures.append("source-skill-set-mismatch")
        if diffs:
            failures.append("non-deterministic-build")
        return {
            "ok": not failures,
            "failure_classes": sorted(set(failures)),
            "diffs": diffs,
            "version": build["package_version"],
            "source_authority": build["source_authority"],
            "source_skills": source_skill_names,
        }


def verify_installed(
    source_root: Path,
    *,
    plugin_source: Path,
    cache_root: Path,
    require_accepted: bool = False,
    allow_dirty: bool = False,
) -> dict[str, Any]:
    failure_classes: list[str] = []
    diffs: list[str] = []
    with tempfile.TemporaryDirectory(prefix="alphax-plugin-expected-") as tmp:
        expected = Path(tmp) / "plugin"
        try:
            build = build_plugin(source_root, expected, allow_dirty=allow_dirty)
        except ValueError as exc:
            return {
                "ok": False,
                "failure_classes": ["source-not-publishable"],
                "diffs": [str(exc)],
            }
        if require_accepted and build["source_authority"] != "accepted":
            failure_classes.append("source-not-accepted")
        marketplace_diffs = compare_trees(expected, plugin_source)
        if marketplace_diffs:
            failure_classes.append("marketplace-content-drift")
            diffs.extend(f"marketplace:{item}" for item in marketplace_diffs)
        version = build["package_version"]
        cache = cache_root / version
        cache_diffs = compare_trees(expected, cache)
        if cache_diffs:
            failure_classes.append("cache-content-drift")
            diffs.extend(f"cache:{item}" for item in cache_diffs)
        for root, label in ((plugin_source, "marketplace"), (cache, "cache")):
            manifest = root / ".codex-plugin/plugin.json"
            if manifest.is_file():
                actual_version = json.loads(manifest.read_text(encoding="utf-8")).get("version")
                if actual_version != version:
                    failure_classes.append(f"{label}-version-drift")
        return {
            "ok": not failure_classes,
            "failure_classes": sorted(set(failure_classes)),
            "diffs": sorted(diffs),
            "version": version,
            "cache": str(cache),
            "source_authority": build["source_authority"],
        }


def safe_extract_archive(data: bytes, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:") as archive:
        for member in archive.getmembers():
            target = (destination / member.name).resolve()
            if target != root and root not in target.parents:
                raise ValueError(f"unsafe git archive member: {member.name}")
        archive.extractall(destination, filter="data")


def materialize_ref(source_root: Path, commit: str, cache_root: Path) -> Path:
    cache_root = cache_root.resolve()
    target = cache_root / commit
    if (target / "AGENTS.md").is_file():
        return target
    cache_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{commit[:12]}-", dir=cache_root) as tmp:
        staging = Path(tmp) / "source"
        extract_ref(source_root, commit, staging)
        if target.exists():
            return target
        staging.rename(target)
    return target


def normalize_scope(scope: str) -> str:
    normalized = scope.strip().lower().replace("_", "-").replace(" ", "-")
    if normalized not in SOURCE_SCOPES | PROJECT_SCOPES:
        raise ValueError(f"unsupported alphaX scope: {scope}")
    return normalized


def resolve_source(
    source_root: Path,
    *,
    scope: str,
    accepted_ref: str | None = None,
    cache_root: Path | None = None,
) -> dict[str, Any]:
    source_root = source_root.resolve()
    scope = normalize_scope(scope)
    identity = source_identity(source_root, accepted_ref)
    identity["scope"] = scope
    if scope in SOURCE_SCOPES:
        return {
            **identity,
            "resolved_root": str(source_root),
            "source_ref": "working-tree",
            "materialized": False,
        }

    accepted_commit = identity["accepted_commit"]
    if identity["source_commit"] == accepted_commit and not identity["source_dirty"]:
        resolved = source_root
        materialized = False
    else:
        cache_root = cache_root or Path.home() / ".cache/alphax/source"
        resolved = materialize_ref(source_root, accepted_commit, cache_root)
        materialized = True
    return {
        **identity,
        "source_commit": accepted_commit,
        "source_branch": identity["accepted_ref"],
        "source_authority": "accepted",
        "source_dirty": False,
        "resolved_root": str(resolved),
        "source_ref": identity["accepted_ref"],
        "materialized": materialized,
    }


def resolve_invocation(
    plugin_root: Path,
    *,
    scope: str,
    source_root: Path | None = None,
    accepted_ref: str | None = None,
) -> dict[str, Any]:
    plugin_root = plugin_root.resolve()
    scope = normalize_scope(scope)
    provenance_path = plugin_root / ".alphax-source.json"
    if not provenance_path.is_file():
        raise ValueError(f"missing plugin Source provenance: {provenance_path}")
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    package_fields = {
        "package_version": provenance.get("package_version"),
        "package_source_commit": provenance.get("package_source_commit", provenance.get("source_commit")),
        "package_source_branch": provenance.get("package_source_branch", provenance.get("source_branch")),
        "package_source_authority": provenance.get(
            "package_source_authority", provenance.get("source_authority")
        ),
    }
    if scope in SOURCE_SCOPES:
        if source_root is None:
            raise ValueError("source work/review requires an explicit live Source checkout")
        return {
            **resolve_source(source_root, scope=scope, accepted_ref=accepted_ref),
            **package_fields,
        }

    embedded = plugin_root / "source"
    expected_fingerprint = provenance.get("embedded_source_fingerprint")
    if not embedded.is_dir() or not expected_fingerprint:
        raise ValueError("plugin does not contain an identified embedded Source snapshot")
    actual_fingerprint = tree_fingerprint(embedded)
    if actual_fingerprint != expected_fingerprint:
        raise ValueError("embedded Source content drift: package snapshot does not match provenance")
    return {
        "scope": scope,
        "resolved_root": str(embedded),
        "source_commit": provenance["embedded_source_commit"],
        "source_branch": provenance["embedded_source_ref"],
        "source_ref": provenance["embedded_source_ref"],
        "source_authority": "accepted",
        "source_dirty": False,
        "source_fingerprint": actual_fingerprint,
        "materialized": True,
        **package_fields,
    }


def install_plugin(
    source_root: Path,
    *,
    plugin_source: Path,
    cache_root: Path,
    selector: str = "alphax@personal",
    codex: str = "codex",
    allow_candidate: bool = False,
    runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> dict[str, Any]:
    identity = source_identity(source_root)
    if identity["source_authority"] != "accepted" and not allow_candidate:
        raise ValueError("plugin install requires clean accepted Source")
    plugin_source = plugin_source.expanduser().resolve()
    plugin_source.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="alphax-plugin-install-") as tmp:
        built = Path(tmp) / "plugin"
        build = build_plugin(source_root, built, allow_dirty=allow_candidate)
        backup = Path(tmp) / "backup"
        if plugin_source.exists():
            shutil.copytree(plugin_source, backup, ignore=shutil.ignore_patterns(*IGNORED_NAMES))
        copy_tree(built, plugin_source)
        completed = runner(
            [codex, "plugin", "add", selector, "--json"],
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            if backup.exists():
                copy_tree(backup, plugin_source)
            raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
        verification = verify_installed(
            source_root,
            plugin_source=plugin_source,
            cache_root=cache_root,
            require_accepted=not allow_candidate,
            allow_dirty=allow_candidate,
        )
        if not verification["ok"]:
            if backup.exists():
                copy_tree(backup, plugin_source)
            raise RuntimeError(json.dumps(verification, ensure_ascii=False))
        return {
            "ok": True,
            "selector": selector,
            "version": build["package_version"],
            "plugin_source": str(plugin_source),
            "cache": verification["cache"],
            "source_authority": build["source_authority"],
        }


def _version_tuple(value: str) -> tuple[int, ...] | None:
    match = re.search(r"\d+(?:\.\d+)*", value)
    if not match:
        return None
    return tuple(int(part) for part in match.group().split("."))


def _check(
    check_id: str,
    scope: str,
    status: str,
    observed: str | None,
    required: str,
    installable: bool,
    action: str | None,
) -> dict[str, Any]:
    return {
        "id": check_id,
        "scope": scope,
        "status": status,
        "observed": observed,
        "required": required,
        "installable": installable,
        "action": action,
    }


def _run_probe(
    command_runner: Callable[[list[str]], subprocess.CompletedProcess[str]], argv: list[str]
) -> subprocess.CompletedProcess[str]:
    try:
        return command_runner(argv)
    except OSError:
        return subprocess.CompletedProcess(argv, 127, "", "")


def _json_object(completed: subprocess.CompletedProcess[str]) -> dict[str, Any] | None:
    if completed.returncode != 0:
        return None
    try:
        value = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return None
    if isinstance(value, dict):
        return value
    if isinstance(value, list):
        return {"items": value}
    return None


def _items(payload: dict[str, Any], key: str) -> list[dict[str, Any]]:
    value = payload.get(key, payload.get("items", []))
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def _marketplace_source(marketplace: dict[str, Any]) -> str | None:
    repository = marketplace.get("repository")
    if isinstance(repository, str):
        return repository
    marketplace_source = marketplace.get("marketplaceSource")
    if isinstance(marketplace_source, dict):
        source = marketplace_source.get("source")
        if isinstance(source, str):
            return source
    return None


def _probe_codex_state(
    command_runner: Callable[[list[str]], subprocess.CompletedProcess[str]],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    marketplaces = _json_object(
        _run_probe(command_runner, ["codex", "plugin", "marketplace", "list", "--json"])
    )
    plugins = _json_object(_run_probe(command_runner, ["codex", "plugin", "list", "--json"]))
    if marketplaces is None or plugins is None:
        capability = _check(
            "codex-plugin",
            "delegation",
            "blocked",
            None,
            "Codex plugin marketplace and list JSON commands",
            False,
            "install or repair a Codex CLI with plugin support",
        )
        unavailable = _check(
            "ocr-marketplace",
            "delegation",
            "blocked",
            None,
            OCR_MARKETPLACE_REPOSITORY,
            False,
            "repair Codex plugin capability before configuring OCR",
        )
        return capability, unavailable, _check(
            "ocr-plugin",
            "delegation",
            "blocked",
            None,
            OCR_PLUGIN_SELECTOR,
            False,
            "repair Codex plugin capability before configuring OCR",
        )

    capability = _check(
        "codex-plugin",
        "delegation",
        "pass",
        "plugin-json-supported",
        "Codex plugin marketplace and list JSON commands",
        False,
        None,
    )
    marketplace = next(
        (
            item
            for item in _items(marketplaces, "marketplaces")
            if item.get("name") == "open-code-review"
        ),
        None,
    )
    if marketplace is None:
        marketplace_check = _check(
            "ocr-marketplace",
            "delegation",
            "missing",
            "absent",
            OCR_MARKETPLACE_REPOSITORY,
            True,
            "add the Open Code Review marketplace from its approved repository",
        )
    elif _marketplace_source(marketplace) != OCR_MARKETPLACE_REPOSITORY:
        marketplace_check = _check(
            "ocr-marketplace",
            "delegation",
            "blocked",
            "source-mismatch",
            OCR_MARKETPLACE_REPOSITORY,
            False,
            "resolve the existing Open Code Review marketplace source manually",
        )
    else:
        marketplace_check = _check(
            "ocr-marketplace",
            "delegation",
            "pass",
            "approved-source",
            OCR_MARKETPLACE_REPOSITORY,
            False,
            None,
        )

    plugin = next(
        (
            item
            for item in _items(plugins, "plugins")
            if item.get("id") == OCR_PLUGIN_SELECTOR or item.get("pluginId") == OCR_PLUGIN_SELECTOR
        ),
        None,
    )
    if plugin is None:
        plugin_check = _check(
            "ocr-plugin",
            "delegation",
            "missing",
            "absent",
            "installed and enabled " + OCR_PLUGIN_SELECTOR,
            True,
            "install and enable the Open Code Review Codex plugin",
        )
    elif plugin.get("enabled") is not True:
        plugin_check = _check(
            "ocr-plugin",
            "delegation",
            "missing",
            "not-enabled",
            "installed and enabled " + OCR_PLUGIN_SELECTOR,
            True,
            "install and enable the Open Code Review Codex plugin",
        )
    else:
        plugin_check = _check(
            "ocr-plugin",
            "delegation",
            "pass",
            "enabled",
            "installed and enabled " + OCR_PLUGIN_SELECTOR,
            False,
            None,
        )
    return capability, marketplace_check, plugin_check


def _probe_alphax_state(
    source_root: Path,
    *,
    plugin_source: Path,
    cache_root: Path,
    alphax_verifier: Callable[..., dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        identity = source_identity(source_root)
    except (OSError, ValueError):
        return (
            _check(
                "alphax-source",
                "alphax-publication",
                "error",
                None,
                "clean accepted Source",
                False,
                "repair the AlphaX Source checkout before installation",
            ),
            _check(
                "alphax-parity",
                "alphax-publication",
                "blocked",
                None,
                "byte-identical generated package, marketplace, and cache",
                False,
                "verify an accepted AlphaX Source first",
            ),
        )
    if identity["source_authority"] != "accepted":
        source_check = _check(
            "alphax-source",
            "alphax-publication",
            "manual-gate",
            "candidate",
            "clean accepted Source",
            False,
            "clean or accept the AlphaX Source before production installation",
        )
        return source_check, _check(
            "alphax-parity",
            "alphax-publication",
            "manual-gate",
            "source-not-accepted",
            "byte-identical generated package, marketplace, and cache",
            False,
            "verify package parity after Source acceptance",
        )

    source_check = _check(
        "alphax-source",
        "alphax-publication",
        "pass",
        "accepted",
        "clean accepted Source",
        False,
        None,
    )
    try:
        verification = alphax_verifier(
            source_root,
            plugin_source=plugin_source,
            cache_root=cache_root,
            require_accepted=True,
        )
    except (OSError, ValueError):
        verification = {"ok": False, "failure_classes": ["verification-error"]}
    cache = Path(str(verification.get("cache", ""))) if verification.get("cache") else None
    if not plugin_source.is_dir() or cache is None or not cache.is_dir():
        parity_check = _check(
            "alphax-parity",
            "alphax-publication",
            "missing",
            "generated-path-absent",
            "byte-identical generated package, marketplace, and cache",
            True,
            "install AlphaX from clean accepted Source and verify parity",
        )
    elif verification.get("ok"):
        parity_check = _check(
            "alphax-parity",
            "alphax-publication",
            "pass",
            "byte-identical",
            "byte-identical generated package, marketplace, and cache",
            False,
            None,
        )
    else:
        parity_check = _check(
            "alphax-parity",
            "alphax-publication",
            "blocked",
            "drift-detected",
            "byte-identical generated package, marketplace, and cache",
            False,
            "repair AlphaX Source or regenerate the installed package",
        )
    return source_check, parity_check


def _overall_status(checks: list[dict[str, Any]]) -> str:
    required = [check for check in checks if check["id"] != "managed-mode"]
    if any(check["status"] in {"blocked", "incompatible", "error"} for check in required):
        return "blocked"
    if any(check["status"] in {"missing", "manual-gate"} for check in required):
        return "action-required"
    return "ready"


def doctor_setup(
    source_root: Path,
    *,
    install: bool = False,
    command_runner: Callable[[list[str]], subprocess.CompletedProcess[str]] = run_command,
    alphax_verifier: Callable[..., dict[str, Any]] = verify_installed,
    alphax_installer: Callable[..., dict[str, Any]] = install_plugin,
    platform_name: str | None = None,
    plugin_source: Path | None = None,
    cache_root: Path | None = None,
) -> dict[str, Any]:
    install_requested = install is True
    plugin_source = plugin_source or Path.home() / "plugins/alphax"
    cache_root = cache_root or Path.home() / ".codex/plugins/cache/personal/alphax"
    python_version = tuple(sys.version_info[:3])
    python_ready = python_version >= (3, 10)
    python_check = _check(
        "python",
        "core",
        "pass" if python_ready else "incompatible",
        ".".join(str(part) for part in python_version),
        ">=3.10",
        False,
        None if python_ready else "install Python >=3.10",
    )

    git_probe = _run_probe(command_runner, ["git", "--version"])
    git_version = _version_tuple(git_probe.stdout)
    git_status = "pass" if git_probe.returncode == 0 and git_version and git_version >= (2, 41) else (
        "missing" if git_probe.returncode != 0 else "incompatible"
    )
    git_check = _check(
        "git",
        "core",
        git_status,
        ".".join(str(part) for part in git_version) if git_version else None,
        ">=2.41",
        False,
        None if git_status == "pass" else "install Git >=2.41",
    )

    ocr_probe = _run_probe(command_runner, ["ocr", "version"])
    ocr_version = _version_tuple(ocr_probe.stdout)
    ocr_status = "pass" if ocr_probe.returncode == 0 and ocr_version else (
        "missing" if ocr_probe.returncode != 0 else "incompatible"
    )
    ocr_check = _check(
        "ocr-cli",
        "delegation",
        ocr_status,
        ".".join(str(part) for part in ocr_version) if ocr_version else None,
        OCR_PACKAGE,
        ocr_status == "missing",
        None if ocr_status == "pass" else "install " + OCR_PACKAGE,
    )

    if ocr_status == "missing":
        node_probe = _run_probe(command_runner, ["node", "--version"])
        npm_probe = _run_probe(command_runner, ["npm", "--version"])
        node_version = _version_tuple(node_probe.stdout)
        npm_version = _version_tuple(npm_probe.stdout)
        if node_probe.returncode != 0 or npm_probe.returncode != 0:
            node_status = "missing"
        elif node_version is None or node_version < (14,) or npm_version is None:
            node_status = "incompatible"
        else:
            node_status = "pass"
        node_observed = (
            f"node-{'.'.join(str(part) for part in node_version)} npm-{'.'.join(str(part) for part in npm_version)}"
            if node_version and npm_version
            else None
        )
    else:
        node_status = "pass"
        node_observed = "not-required"
    node_check = _check(
        "node-npm",
        "delegation",
        node_status,
        node_observed,
        "Node >=14 and runnable npm when OCR CLI is missing",
        node_status == "missing",
        None if node_status == "pass" else "install Node >=14 with npm",
    )

    codex_check, marketplace_check, plugin_check = _probe_codex_state(command_runner)
    source_check, parity_check = _probe_alphax_state(
        source_root,
        plugin_source=plugin_source,
        cache_root=cache_root,
        alphax_verifier=alphax_verifier,
    )
    managed_check = _check(
        "managed-mode",
        "managed",
        "manual-gate",
        "unapproved",
        "explicit endpoint and target-code egress approval",
        False,
        "obtain managed-model approval outside doctor",
    )
    checks = [
        python_check,
        git_check,
        codex_check,
        node_check,
        ocr_check,
        marketplace_check,
        plugin_check,
        source_check,
        parity_check,
        managed_check,
    ]
    payload = {
        "schema_version": DOCTOR_SCHEMA_VERSION,
        "mode": "install" if install_requested else "doctor",
        "overall": _overall_status(checks),
        "checks": checks,
        "changes": [],
        "residual_risk": ["managed-llm-unapproved"],
    }
    if not install_requested:
        return payload

    install_steps = [
        ("ocr-cli", "npm-install", ["npm", "install", "-g", OCR_PACKAGE]),
        (
            "ocr-marketplace",
            "marketplace-add",
            [
                "codex",
                "plugin",
                "marketplace",
                "add",
                "alibaba/open-code-review",
                "--ref",
                "main",
                "--json",
            ],
        ),
        (
            "ocr-plugin",
            "plugin-install",
            ["codex", "plugin", "add", OCR_PLUGIN_SELECTOR, "--json"],
        ),
    ]
    changes: list[dict[str, Any]] = []

    def record(
        check_id: str, command_class: str, status: str, action: str | None = None
    ) -> None:
        changes.append(
            {
                "id": check_id,
                "command_class": command_class,
                "status": status,
                "action": action,
            }
        )

    def finish() -> dict[str, Any]:
        refreshed = doctor_setup(
            source_root,
            command_runner=command_runner,
            alphax_verifier=alphax_verifier,
            alphax_installer=alphax_installer,
            platform_name=platform_name,
            plugin_source=plugin_source,
            cache_root=cache_root,
        )
        refreshed["mode"] = "install"
        refreshed["changes"] = changes
        return refreshed

    if (platform_name or sys.platform).lower() not in {"darwin", "linux"}:
        for check_id, command_class, _command in install_steps:
            record(check_id, command_class, "skipped", "run this installation manually on a supported platform")
        record("alphax", "alphax-install", "skipped", "install AlphaX manually on a supported platform")
        return finish()

    check_by_id = {check["id"]: check for check in checks}
    ocr_check = check_by_id["ocr-cli"]
    if ocr_check["status"] == "pass":
        record("ocr-cli", "npm-install", "already-satisfied")
    elif ocr_check["status"] != "missing" or check_by_id["node-npm"]["status"] != "pass":
        record("ocr-cli", "npm-install", "skipped", "repair Node/npm or OCR prerequisites first")
        return finish()
    else:
        _check_id, command_class, command = install_steps[0]
        completed = _run_probe(command_runner, command)
        reprobe = _run_probe(command_runner, ["ocr", "version"])
        if completed.returncode != 0 or reprobe.returncode != 0 or _version_tuple(reprobe.stdout) is None:
            record("ocr-cli", command_class, "failed", "install OCR CLI manually and retry")
            return finish()
        record("ocr-cli", command_class, "applied")

    marketplace_check = _probe_codex_state(command_runner)[1]
    if marketplace_check["status"] == "pass":
        record("ocr-marketplace", "marketplace-add", "already-satisfied")
    elif marketplace_check["status"] != "missing":
        record("ocr-marketplace", "marketplace-add", "skipped", marketplace_check["action"])
        return finish()
    else:
        _check_id, command_class, command = install_steps[1]
        completed = _run_probe(command_runner, command)
        reprobe = _probe_codex_state(command_runner)[1]
        if completed.returncode != 0 or reprobe["status"] != "pass":
            record("ocr-marketplace", command_class, "failed", "add the approved marketplace manually and retry")
            return finish()
        record("ocr-marketplace", command_class, "applied")

    plugin_check = _probe_codex_state(command_runner)[2]
    if plugin_check["status"] == "pass":
        record("ocr-plugin", "plugin-install", "already-satisfied")
    elif plugin_check["status"] != "missing":
        record("ocr-plugin", "plugin-install", "skipped", plugin_check["action"])
        return finish()
    else:
        _check_id, command_class, command = install_steps[2]
        completed = _run_probe(command_runner, command)
        reprobe = _probe_codex_state(command_runner)[2]
        if completed.returncode != 0 or reprobe["status"] != "pass":
            record("ocr-plugin", command_class, "failed", "install the OCR plugin manually and retry")
            return finish()
        record("ocr-plugin", command_class, "applied")

    source_check, parity_check = _probe_alphax_state(
        source_root,
        plugin_source=plugin_source,
        cache_root=cache_root,
        alphax_verifier=alphax_verifier,
    )
    if source_check["status"] != "pass":
        record("alphax", "alphax-install", "skipped", source_check["action"])
        return finish()
    if parity_check["status"] == "pass":
        record("alphax", "alphax-install", "already-satisfied")
    elif parity_check["status"] != "missing":
        record("alphax", "alphax-install", "skipped", parity_check["action"])
        return finish()
    else:
        def installer_runner(
            argv: list[str], **_kwargs: Any
        ) -> subprocess.CompletedProcess[str]:
            return command_runner(argv)

        try:
            alphax_installer(
                source_root,
                plugin_source=plugin_source,
                cache_root=cache_root,
                allow_candidate=False,
                runner=installer_runner,
            )
        except Exception:
            record("alphax", "alphax-install", "failed", "install AlphaX from accepted Source manually and retry")
            return finish()
        _source_check, reprobe = _probe_alphax_state(
            source_root,
            plugin_source=plugin_source,
            cache_root=cache_root,
            alphax_verifier=alphax_verifier,
        )
        if reprobe["status"] != "pass":
            record("alphax", "alphax-install", "failed", "verify AlphaX parity and retry")
            return finish()
        record("alphax", "alphax-install", "applied")

    return finish()


def default_source_root() -> Path:
    return Path(__file__).resolve().parents[1]


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=default_source_root())
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build")
    build.add_argument("--out", type=Path, required=True)
    build.add_argument("--allow-dirty", action="store_true")
    build.add_argument("--accepted-ref")

    verify_source_parser = subparsers.add_parser("verify-source")
    verify_source_parser.add_argument("--require-clean", action="store_true")

    installed = subparsers.add_parser("verify-installed")
    installed.add_argument("--plugin-source", type=Path, default=Path.home() / "plugins/alphax")
    installed.add_argument(
        "--cache-root",
        type=Path,
        default=Path.home() / ".codex/plugins/cache/personal/alphax",
    )
    installed.add_argument("--require-accepted", action="store_true")
    installed.add_argument("--allow-dirty", action="store_true")

    install = subparsers.add_parser("install")
    install.add_argument("--plugin-source", type=Path, default=Path.home() / "plugins/alphax")
    install.add_argument(
        "--cache-root",
        type=Path,
        default=Path.home() / ".codex/plugins/cache/personal/alphax",
    )
    install.add_argument("--selector", default="alphax@personal")
    install.add_argument("--codex", default="codex")
    install.add_argument("--allow-candidate", action="store_true")

    resolve = subparsers.add_parser("resolve-source")
    resolve.add_argument("--scope", required=True)
    resolve.add_argument("--accepted-ref", default=os.environ.get("ALPHAX_ACCEPTED_REF"))
    resolve.add_argument(
        "--cache-root",
        type=Path,
        default=Path(os.environ.get("ALPHAX_SOURCE_CACHE", Path.home() / ".cache/alphax/source")),
    )
    invocation = subparsers.add_parser("resolve-invocation")
    invocation.add_argument("--scope", required=True)
    invocation.add_argument("--plugin-root", type=Path, default=default_source_root())
    invocation.add_argument("--live-source-root", type=Path)
    invocation.add_argument("--accepted-ref", default=os.environ.get("ALPHAX_ACCEPTED_REF"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    if args.command == "build":
        emit(build_plugin(source_root, args.out, allow_dirty=args.allow_dirty, accepted_ref=args.accepted_ref))
        return 0
    if args.command == "verify-source":
        result = verify_source(source_root, allow_dirty=not args.require_clean)
    elif args.command == "verify-installed":
        result = verify_installed(
            source_root,
            plugin_source=args.plugin_source,
            cache_root=args.cache_root,
            require_accepted=args.require_accepted,
            allow_dirty=args.allow_dirty,
        )
    elif args.command == "install":
        result = install_plugin(
            source_root,
            plugin_source=args.plugin_source,
            cache_root=args.cache_root,
            selector=args.selector,
            codex=args.codex,
            allow_candidate=args.allow_candidate,
        )
    elif args.command == "resolve-source":
        result = resolve_source(
            source_root,
            scope=args.scope,
            accepted_ref=args.accepted_ref,
            cache_root=args.cache_root,
        )
    elif args.command == "resolve-invocation":
        result = resolve_invocation(
            args.plugin_root,
            scope=args.scope,
            source_root=args.live_source_root,
            accepted_ref=args.accepted_ref,
        )
    else:
        raise AssertionError(args.command)
    emit(result)
    return 0 if result.get("ok", True) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - CLI must surface one failure class.
        print(str(exc), file=sys.stderr)
        raise SystemExit(1) from exc
