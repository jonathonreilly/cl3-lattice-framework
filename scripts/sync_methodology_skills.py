#!/usr/bin/env python3
"""Check installed methodology skills; --apply installs a reviewed source snapshot.

The default checks only repo skill names already present in the destination.
Use repeated --skill NAME to select missing skills, or --all to install every
repo skill. No network operations are performed. Exit codes: 0 synchronized,
1 drift found by a check, 2 invalid input or unsuccessful application.
Applications retain snapshot backups and actual displaced originals outside
discovery; reported recovery directories are not automatically removed. The
sync lock coordinates this tool, not arbitrary concurrent editors.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_REL = Path("docs/ai_methodology/skills")
NAME_RE = re.compile(r"[a-z][a-z0-9-]*\Z")


class SyncError(Exception):
    """An unsafe input or changed snapshot prevented synchronization."""


def plain_path(path: Path) -> Path:
    """Reject traversal and symlink components, including dangling links."""
    path = path.expanduser()
    if ".." in path.parts:
        raise SyncError(f"Parent traversal is not allowed: {path}")
    if ".system" in path.parts:
        raise SyncError(f"System skill directories are not managed: {path}")
    path = path.absolute()
    for component in reversed((path, *path.parents)):
        if component.is_symlink():
            raise SyncError(f"Symlink is not allowed: {component}")
    return path


def tree_manifest(root: Path) -> dict:
    """Hash the whole tree, including extra local files and empty directories."""
    plain_path(root)
    if not root.is_dir():
        raise SyncError(f"Skill must be a regular directory: {root}")
    manifest = {}
    for path in [root, *sorted(root.rglob("*"))]:
        info = path.lstat()
        relative = path.relative_to(root).as_posix()
        entry = {"mode": stat.S_IMODE(info.st_mode)}
        if stat.S_ISLNK(info.st_mode):
            raise SyncError(f"Symlink is not allowed: {path}")
        if stat.S_ISDIR(info.st_mode):
            entry["type"] = "directory"
        elif stat.S_ISREG(info.st_mode):
            entry.update(type="file", sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        else:
            raise SyncError(f"Special file is not allowed: {path}")
        manifest[relative] = entry
    return manifest


def git_output(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "--no-optional-locks", "-C", str(repo), *args],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise SyncError(f"Cannot inspect source Git provenance: {result.stderr.strip()}")
    return result.stdout.strip()


def source_provenance(repo: Path) -> dict:
    if Path(git_output(repo, "rev-parse", "--show-toplevel")) != repo:
        raise SyncError("--repo-root must be the root of the source Git checkout")
    return {
        "repository": str(repo),
        "revision": git_output(repo, "rev-parse", "HEAD"),
        "worktree_dirty": bool(git_output(repo, "status", "--porcelain", "--untracked-files=normal")),
        "skills_dirty": bool(git_output(repo, "status", "--porcelain", "--untracked-files=normal", "--", str(SKILLS_REL))),
        "source_kind": "worktree snapshot; revision identifies its Git base, not uncommitted bytes",
    }


def make_plan(repo: Path, destination: Path, selected: list[str] | None, all_skills: bool) -> list[dict]:
    source_root = plain_path(repo / SKILLS_REL)
    if not source_root.is_dir():
        raise SyncError(f"Source skill directory is missing: {source_root}")
    if destination == source_root or destination in source_root.parents or source_root in destination.parents:
        raise SyncError("Source skills and destination must not overlap")
    if destination.exists() and not destination.is_dir():
        raise SyncError(f"Destination is not a directory: {destination}")
    available = {
        p.name for p in source_root.iterdir()
        if NAME_RE.fullmatch(p.name) and (p / "SKILL.md").exists()
    }
    if selected:
        for name in selected:
            if not NAME_RE.fullmatch(name) or name not in available:
                raise SyncError(f"Unknown or unsafe repo skill name: {name}")
        names = sorted(set(selected))
    elif all_skills:
        names = sorted(available)
    else:
        names = sorted(name for name in available if os.path.lexists(destination / name))

    plan = []
    for name in names:
        source = tree_manifest(source_root / name)
        if source.get("SKILL.md", {}).get("type") != "file":
            raise SyncError(f"Source SKILL.md is not a regular file: {name}")
        target = destination / name
        installed = tree_manifest(target) if os.path.lexists(target) else None
        changed = sorted(
            key for key in source.keys() | (installed or {}).keys()
            if source.get(key) != (installed or {}).get(key)
        )
        plan.append({
            "skill": name,
            "status": "missing" if installed is None else "drift" if changed else "in_sync",
            "changed_paths": changed,
            "source_manifest": source,
            "installed_manifest": installed,
        })
    return plan


def current_installed(target: Path) -> dict | None:
    return tree_manifest(target) if os.path.lexists(target) else None


def write_metadata(path: Path, metadata: dict) -> None:
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def install_one(
    repo: Path, destination: Path, backup: Path, item: dict,
    save_metadata: Callable[[], None],
) -> None:
    """Retain actual displaced bytes; editor activity is not covered by our lock."""
    name = item["skill"]
    source, target = repo / SKILLS_REL / name, destination / name
    expected, previous = item["source_manifest"], item["installed_manifest"]
    # The staging directory is outside skill discovery, beside the destination.
    with tempfile.TemporaryDirectory(prefix=".methodology-stage-", dir=destination.parent) as temp:
        stage = Path(temp)
        candidate = stage / "candidate"
        if tree_manifest(source) != expected:
            raise SyncError(f"Source changed after review snapshot: {name}")
        shutil.copytree(source, candidate, symlinks=True)
        if tree_manifest(candidate) != expected:
            raise SyncError(f"Staged source does not match snapshot: {name}")
        if current_installed(target) != previous:
            raise SyncError(f"Installed skill changed after check: {name}")
        if previous is not None:
            saved = backup / "installed" / name
            shutil.copytree(target, saved, symlinks=True)
            if tree_manifest(saved) != previous:
                raise SyncError(f"Backup does not match installed snapshot: {name}")
        if tree_manifest(source) != expected or current_installed(target) != previous:
            raise SyncError(f"Source or installed skill changed during backup: {name}")

        # Keep the actual renamed original, not just its earlier copied snapshot.
        # This durable directory is outside both discovery and TemporaryDirectory
        # cleanup. It stays beside the destination even when --backup-root is on
        # another filesystem, so recovery does not depend on a cross-device move.
        recovery = Path(tempfile.mkdtemp(
            prefix=f".methodology-recovery-{name}-", dir=destination.parent,
        ))
        displaced, unpublished = recovery / "previous", recovery / "unpublished"
        item["recovery_directory"] = str(recovery)
        item["recovery_state"] = "prepared"
        save_metadata()  # Record the durable location before displacing user data.
        moved_old = installed_new = False
        try:
            if previous is not None:
                os.replace(target, displaced)
                moved_old = True
                if tree_manifest(displaced) != previous:
                    raise SyncError(f"Installed skill changed at publication boundary: {name}")
            os.replace(candidate, target)
            installed_new = True
            if tree_manifest(target) != expected:
                raise SyncError(f"Installed bytes do not match source snapshot: {name}")
            item["recovery_state"] = "original_retained" if moved_old else "new_install"
        except Exception as exc:
            rollback_error = None
            try:
                if (installed_new or moved_old) and os.path.lexists(target):
                    # Preserve a changed publication, or a concurrently recreated
                    # destination, before attempting to restore the original.
                    os.replace(target, unpublished)
                if moved_old:
                    os.replace(displaced, target)
                item["recovery_state"] = "rolled_back"
            except Exception as restore_error:
                # Never clean this directory on error. The original and/or the
                # unexpected publication remain here or live at the destination.
                rollback_error = restore_error
                item["recovery_state"] = "rollback_incomplete"
            item["status"] = "failed"
            try:
                save_metadata()
            except OSError as metadata_error:
                rollback_error = f"{rollback_error}; metadata update failed: {metadata_error}"
            detail = f"; rollback incomplete: {rollback_error}" if rollback_error else ""
            raise SyncError(f"{exc}{detail}; durable recovery: {recovery}") from exc


def apply_plan(repo: Path, destination: Path, backup_root: Path, provenance: dict, plan: list[dict]) -> Path | None:
    changes = [item for item in plan if item["status"] != "in_sync"]
    if not changes:
        return None
    if backup_root == destination or destination in backup_root.parents:
        raise SyncError("Backups must be outside the skill discovery destination")
    source_root = repo / SKILLS_REL
    if backup_root == source_root or source_root in backup_root.parents:
        raise SyncError("Backups must be outside the source skill tree")
    destination.parent.mkdir(parents=True, exist_ok=True)
    lock = destination.parent / f".sync-{destination.name}.lock"
    try:
        lock.mkdir()
    except FileExistsError as exc:
        raise SyncError(f"Another sync or unrecovered sync lock exists: {lock}") from exc
    backup = None
    try:
        destination.mkdir(exist_ok=True)
        backup_root.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = Path(tempfile.mkdtemp(prefix=f"{stamp}-", dir=backup_root))
        metadata = {
            "schema_version": 1, "created_utc": stamp,
            "source": provenance, "destination": str(destination),
            "skills": changes,
        }
        manifest_path = backup / "metadata.json"
        write_metadata(manifest_path, metadata)
        for item in changes:
            if git_output(repo, "rev-parse", "HEAD") != provenance["revision"]:
                raise SyncError("Source Git revision changed after snapshot")
            install_one(
                repo, destination, backup, item,
                lambda: write_metadata(manifest_path, metadata),
            )
            item["status"] = "applied"
            write_metadata(manifest_path, metadata)
        return backup
    except Exception as exc:
        raise SyncError(f"Synchronization failed: {exc}. Recovery backup: {backup}") from exc
    finally:
        lock.rmdir()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--destination", type=Path, default=Path.home() / ".codex/skills")
    parser.add_argument("--backup-root", type=Path, help="Defaults to skill-backups beside destination; must be outside discovery")
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--skill", action="append", help="Select a repo skill; repeat to select several, including missing installs")
    selection.add_argument("--all", action="store_true", help="Explicitly select every repo skill, including missing installs")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Explicit read-only drift check (the default)")
    mode.add_argument("--apply", action="store_true", help="Install this source snapshot after reviewing it; default only checks")
    args = parser.parse_args(argv)
    try:
        repo, destination = plain_path(args.repo_root), plain_path(args.destination)
        provenance = source_provenance(repo)
        plan = make_plan(repo, destination, args.skill, args.all)
        backup = None
        if args.apply:
            backup_root = plain_path(args.backup_root or destination.parent / "skill-backups")
            backup = apply_plan(repo, destination, backup_root, provenance, plan)
        print(json.dumps({
            "mode": "apply" if args.apply else "check", "source": provenance,
            "destination": str(destination), "backup": str(backup) if backup else None,
            "skills": [{k: item.get(k) for k in (
                "skill", "status", "changed_paths", "recovery_directory", "recovery_state",
            )} for item in plan],
        }, indent=2, sort_keys=True))
        return 0 if args.apply or all(item["status"] == "in_sync" for item in plan) else 1
    except (SyncError, OSError) as exc:
        print(f"sync_methodology_skills: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
