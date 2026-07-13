#!/usr/bin/env python3
"""Build, verify, install, and resolve the alphaX Codex plugin from Source."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
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
