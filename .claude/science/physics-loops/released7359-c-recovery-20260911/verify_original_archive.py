#!/usr/bin/env python3
"""Verify and optionally extract the released-7359-C recovery archive."""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path
import subprocess


HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / "ORIGINAL_OCCURRENCES.json.gz.b64"
INDEX = HERE / "ORIGINAL_OCCURRENCES_INDEX.json"
DELTA_VERIFICATION = HERE / "ORIGINAL_DELTA_VERIFICATION.json"


def sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def git_bytes(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(("git", "-C", str(repo), *args))


def git_text(repo: Path, *args: str) -> str:
    return git_bytes(repo, *args).decode().strip()


def git_body_or_none(repo: Path, revision: str, path: str) -> bytes | None:
    spec = f"{revision}:{path}"
    probe = subprocess.run(
        ("git", "-C", str(repo), "cat-file", "-e", spec),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return git_bytes(repo, "show", spec) if probe.returncode == 0 else None


def verify_git(repo: Path, payload: dict, delta: dict) -> None:
    for entry in payload["entries"]:
        body = base64.b64decode(entry["content_base64"], validate=True)
        actual = git_bytes(repo, "show", f"{entry['head']}:{entry['path']}")
        if actual != body:
            raise SystemExit(
                f"Git head body mismatch: PR {entry['pr']} {entry['path']}"
            )
        base_body = git_body_or_none(repo, entry["base"], entry["path"])
        if entry["change_status"] == "A" and base_body is not None:
            raise SystemExit(f"added path exists at base: {entry['pr']} {entry['path']}")
        if entry["change_status"] == "M" and base_body is None:
            raise SystemExit(f"modified path absent at base: {entry['pr']} {entry['path']}")
        successor = git_body_or_none(repo, payload["frozen_successor"], entry["path"])
        if (successor == body) != entry["successor_byte_equal"]:
            raise SystemExit(
                f"successor equality mismatch: PR {entry['pr']} {entry['path']}"
            )

    for row in delta["complete_deltas"]:
        actual = git_text(
            repo, "diff", "--name-status", "--no-renames", row["base"], row["head"]
        )
        actual_lines = actual.splitlines() if actual else []
        if actual_lines != row["complete_name_status"]:
            raise SystemExit(f"complete delta mismatch: PR {row['pr']}")
        patch = git_bytes(
            repo, "diff", "--binary", "--full-index", row["base"], row["head"]
        )
        if sha256_bytes(patch) != row["full_binary_diff_sha256"]:
            raise SystemExit(f"full binary diff hash mismatch: PR {row['pr']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extract", type=Path)
    parser.add_argument(
        "--verify-git",
        type=Path,
        metavar="REPOSITORY",
        help="also verify every body and complete base-to-head delta against Git",
    )
    args = parser.parse_args()

    index = json.loads(INDEX.read_text())
    if sha256(ARCHIVE) != index["archive_sha256"]:
        raise SystemExit("archive envelope hash mismatch")
    if sha256(DELTA_VERIFICATION) != index["delta_verification_sha256"]:
        raise SystemExit("delta-verification hash mismatch")
    packed = base64.b64decode(ARCHIVE.read_text().strip(), validate=True)
    if not packed.startswith(b"\x1f\x8b") or packed[4:8] != b"\0\0\0\0":
        raise SystemExit("archive is not a deterministic mtime-zero gzip envelope")
    raw = gzip.decompress(packed)
    if len(raw) != index["decoded_payload_bytes"]:
        raise SystemExit("decoded payload byte count mismatch")
    if sha256_bytes(raw) != index["decoded_payload_sha256"]:
        raise SystemExit("decoded payload hash mismatch")
    payload = json.loads(raw)
    delta = json.loads(DELTA_VERIFICATION.read_text())
    entries = payload["entries"]
    if len(entries) != 26 or payload["original_occurrence_count"] != 26:
        raise SystemExit("original occurrence count is not 26")
    if len({entry["path"] for entry in entries}) != 22:
        raise SystemExit("unique original path count is not 22")
    seen = set()
    for entry in entries:
        identity = (entry["pr"], entry["path"])
        if identity in seen:
            raise SystemExit(f"duplicate occurrence: {identity}")
        seen.add(identity)
        relative = Path(entry["path"])
        if relative.is_absolute() or ".." in relative.parts or relative.as_posix() != entry["path"]:
            raise SystemExit(f"unsafe archive path: {entry['path']}")
        body = base64.b64decode(entry["content_base64"], validate=True)
        if len(body) != entry["bytes"]:
            raise SystemExit(f"byte mismatch: PR {entry['pr']} {entry['path']}")
        if len(body.splitlines()) != entry["lines"]:
            raise SystemExit(f"line mismatch: PR {entry['pr']} {entry['path']}")
        if sha256_bytes(body) != entry["sha256"]:
            raise SystemExit(f"hash mismatch: PR {entry['pr']} {entry['path']}")
        if args.extract:
            target = args.extract / str(entry["pr"]) / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
    stripped = [
        {key: value for key, value in entry.items() if key != "content_base64"}
        for entry in entries
    ]
    if stripped != index["entries"]:
        raise SystemExit("archive entries differ from the readable index")
    if delta.get("status") != "PASS" or len(delta.get("complete_deltas", [])) != 5:
        raise SystemExit("complete-delta verification record is incomplete")
    if args.verify_git:
        verify_git(args.verify_git.resolve(), payload, delta)
    suffix = " plus Git objects/deltas" if args.verify_git else ""
    print(f"PASS: recovered 26 original path occurrences across 22 paths{suffix}")


if __name__ == "__main__":
    main()
