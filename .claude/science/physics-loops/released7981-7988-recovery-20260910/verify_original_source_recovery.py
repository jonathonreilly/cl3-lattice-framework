#!/usr/bin/env python3
"""Verify byte-exact released 7981→7988 recovery bundles without writing."""

from __future__ import annotations

import base64
import gzip
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BUNDLES = tuple(sorted(HERE.glob("*_SOURCE_BODIES_PART*.json")))


def git_blob_id(body: bytes) -> str:
    header = f"blob {len(body)}\0".encode("ascii")
    return hashlib.sha1(header + body).hexdigest()


def git_body(commit: str, path: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(ROOT), "cat-file", "blob", f"{commit}:{path}"]
    )


def main() -> int:
    if not BUNDLES:
        raise SystemExit("no recovery bundles found")

    entries: list[dict[str, object]] = []
    for bundle_path in BUNDLES:
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
        if bundle.get("schema") != "released7981-7988-gzip-base64-bodies-v1":
            raise SystemExit(f"unexpected schema: {bundle_path}")
        entries.extend(bundle["entries"])

    decoded_digest = hashlib.sha256()
    for entry in sorted(
        entries,
        key=lambda item: (
            str(item["kind"]),
            str(item["head"]),
            str(item["path"]),
        ),
    ):
        if entry["encoding"] != "gzip+base64":
            raise SystemExit(f"unexpected encoding: {entry['path']}")
        encoded = "".join(entry["body_chunks"])
        body = gzip.decompress(base64.b64decode(encoded))
        actual_sha256 = hashlib.sha256(body).hexdigest()
        actual_blob = git_blob_id(body)
        if len(body) != entry["byte_count"]:
            raise SystemExit(f"byte-count mismatch: {entry['path']}")
        if actual_sha256 != entry["sha256"]:
            raise SystemExit(f"SHA-256 mismatch: {entry['path']}")
        if actual_blob != entry["git_blob"]:
            raise SystemExit(f"Git-blob mismatch: {entry['path']}")
        if git_body(str(entry["head"]), str(entry["path"])) != body:
            raise SystemExit(f"Git-source mismatch: {entry['head']}:{entry['path']}")
        decoded_digest.update(str(entry["kind"]).encode("utf-8") + b"\0")
        decoded_digest.update(str(entry["head"]).encode("ascii") + b"\0")
        decoded_digest.update(str(entry["path"]).encode("utf-8") + b"\0")
        decoded_digest.update(body)

    delta_entries = [
        entry for entry in entries if entry["kind"] == "constituent_delta_head_body"
    ]
    helper_entries = [
        entry for entry in entries if entry["kind"] == "historical_runtime_helper_body"
    ]
    path_counts = Counter(str(entry["path"]) for entry in delta_entries)
    shared = sorted(path for path, count in path_counts.items() if count == 2)
    if len(delta_entries) != 34 or len(path_counts) != 28 or len(shared) != 6:
        raise SystemExit(
            "delta topology mismatch: "
            f"occurrences={len(delta_entries)} unique={len(path_counts)} "
            f"shared={len(shared)}"
        )
    if len(helper_entries) != 4:
        raise SystemExit(f"historical helper count mismatch: {len(helper_entries)}")
    if any(count not in (1, 2) for count in path_counts.values()):
        raise SystemExit("unexpected repeated delta path")

    print(
        "PASS recovery bodies: "
        f"delta_occurrences={len(delta_entries)} unique_paths={len(path_counts)} "
        f"shared_versions={len(shared)} historical_helpers={len(helper_entries)}"
    )
    print(f"decoded_aggregate_sha256={decoded_digest.hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
