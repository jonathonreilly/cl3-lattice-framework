#!/usr/bin/env python3
"""Verify and optionally extract the released #7315-D recovery archive."""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / "ORIGINAL_OCCURRENCES.json.gz.b64"
INDEX = HERE / "ORIGINAL_OCCURRENCES_INDEX.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extract", type=Path)
    args = parser.parse_args()

    index = json.loads(INDEX.read_text())
    if hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() != index["archive_sha256"]:
        raise SystemExit("archive envelope hash mismatch")
    packed = base64.b64decode(ARCHIVE.read_text().strip(), validate=True)
    payload = json.loads(gzip.decompress(packed))
    entries = payload["entries"]
    if len(entries) != 15 or payload["original_occurrence_count"] != 15:
        raise SystemExit("original occurrence count is not 15")
    if sum(entry["path"].endswith("citation_graph_manifest.json") for entry in entries) != 3:
        raise SystemExit("historical manifest occurrence count is not 3")
    for entry in entries:
        body = base64.b64decode(entry["content_base64"], validate=True)
        if len(body) != entry["bytes"]:
            raise SystemExit(f"byte mismatch: {entry['pr']} {entry['path']}")
        if hashlib.sha256(body).hexdigest() != entry["sha256"]:
            raise SystemExit(f"hash mismatch: {entry['pr']} {entry['path']}")
        if args.extract:
            target = args.extract / str(entry["pr"]) / entry["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
    print("PASS: recovered 15 original occurrences, including three manifest states")


if __name__ == "__main__":
    main()
