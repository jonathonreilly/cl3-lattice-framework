#!/usr/bin/env python3
"""Build the deterministic recovery archive for released #7315 scopes A.

The archive stores every original base-to-head path occurrence for #7011,
#7015, #7016, #7021, #7029, and #7032.  It also stores the two distinct
successor bodies that must remain recoverable: the exact-rational #7029
primary and the #7032 campaign-handoff append.  Generated citation manifests
are recovery data only; this script never writes the live manifest.
"""

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
    "backlog-released18-20260910/7315"
)
BINDINGS = EVIDENCE / "review-A" / "SOURCE_BINDINGS.json"
OUT = Path(__file__).with_name("ORIGINAL_OCCURRENCES.json.gz.b64")
INDEX = Path(__file__).with_name("ORIGINAL_OCCURRENCES_INDEX.json")


def git_blob(revision: str, path: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{revision}:{path}"]
    )


def record(pr: int, revision_kind: str, revision: str, path: str, expected: dict) -> dict:
    body = git_blob(revision, path)
    digest = hashlib.sha256(body).hexdigest()
    if digest != expected["sha256"] or len(body) != expected["bytes"]:
        raise RuntimeError(
            f"identity mismatch for {pr} {revision_kind} {path}: "
            f"{digest}/{len(body)}"
        )
    return {
        "pr": pr,
        "revision_kind": revision_kind,
        "revision": revision,
        "path": path,
        "bytes": len(body),
        "sha256": digest,
        "content_base64": base64.b64encode(body).decode("ascii"),
    }


def main() -> None:
    bindings = json.loads(BINDINGS.read_text())
    entries: list[dict] = []
    for row in bindings["rows"]:
        for path_row in row["paths"]:
            entries.append(
                record(
                    row["number"],
                    "original",
                    row["head"],
                    path_row["path"],
                    path_row["original"],
                )
            )
            if (
                path_row["path"]
                in {
                    "scripts/admissibility_dirac_kahler_quotient_gate_2026_08_20.py",
                    ".claude/science/physics-loops/CAMPAIGN_20260820_48H_HANDOFF.md",
                }
                and not path_row["original_equals_successor"]
            ):
                entries.append(
                    record(
                        row["number"],
                        "successor-distinct",
                        bindings["successor"],
                        path_row["path"],
                        path_row["successor"],
                    )
                )

    payload = {
        "format": "released7315-a-original-occurrences-v1",
        "source_bindings_sha256": hashlib.sha256(BINDINGS.read_bytes()).hexdigest(),
        "original_occurrence_count": sum(
            entry["revision_kind"] == "original" for entry in entries
        ),
        "successor_distinct_count": sum(
            entry["revision_kind"] == "successor-distinct" for entry in entries
        ),
        "entries": entries,
    }
    raw = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    compressed = gzip.compress(raw, compresslevel=9, mtime=0)
    OUT.write_text(base64.b64encode(compressed).decode("ascii") + "\n")

    index = {
        key: payload[key]
        for key in (
            "format",
            "source_bindings_sha256",
            "original_occurrence_count",
            "successor_distinct_count",
        )
    }
    index["archive_sha256"] = hashlib.sha256(OUT.read_bytes()).hexdigest()
    index["archive_bytes"] = OUT.stat().st_size
    index["entries"] = [
        {key: entry[key] for key in entry if key != "content_base64"}
        for entry in entries
    ]
    INDEX.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
