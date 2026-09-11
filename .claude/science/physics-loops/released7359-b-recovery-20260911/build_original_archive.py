#!/usr/bin/env python3
"""Build the deterministic original-occurrence archive for released #7359-B."""

from __future__ import annotations

import base64
import gzip
import hashlib
import json
from pathlib import Path
import subprocess


REPO = Path(__file__).resolve().parents[4]
EVIDENCE = Path(
    "/Users/jonreilly/Documents/Codex/toe-campaign-2026-09-07/"
    "backlog-released18-20260910/7359"
)
BINDINGS = EVIDENCE / "review-B" / "SOURCE_BINDINGS.json"
OUT = Path(__file__).with_name("ORIGINAL_OCCURRENCES.json.gz.b64")
INDEX = Path(__file__).with_name("ORIGINAL_OCCURRENCES_INDEX.json")


def git_blob(revision: str, path: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{revision}:{path}"]
    )


def main() -> None:
    bindings = json.loads(BINDINGS.read_text())
    entries = []
    for row in bindings:
        body = git_blob(row["head"], row["path"])
        digest = hashlib.sha256(body).hexdigest()
        if digest != row["sha256"]:
            raise RuntimeError(
                f"identity mismatch for {row['pr']} {row['path']}: {digest}"
            )
        entries.append({
            "pr": row["pr"],
            "revision_kind": "original",
            "revision": row["head"],
            "path": row["path"],
            "bytes": len(body),
            "sha256": digest,
            "content_base64": base64.b64encode(body).decode("ascii"),
        })

    payload = {
        "format": "released7359-b-original-occurrences-v1",
        "source_bindings_sha256": hashlib.sha256(BINDINGS.read_bytes()).hexdigest(),
        "original_occurrence_count": len(entries),
        "entries": entries,
    }
    raw = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    OUT.write_text(base64.b64encode(gzip.compress(raw, compresslevel=9, mtime=0)).decode("ascii") + "\n")

    index = {
        key: payload[key]
        for key in ("format", "source_bindings_sha256", "original_occurrence_count")
    }
    index["archive_sha256"] = hashlib.sha256(OUT.read_bytes()).hexdigest()
    index["archive_bytes"] = OUT.stat().st_size
    index["entries"] = [
        {key: value for key, value in entry.items() if key != "content_base64"}
        for entry in entries
    ]
    INDEX.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
