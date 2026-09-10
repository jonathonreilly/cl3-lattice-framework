#!/usr/bin/env python3
"""Build and verify the byte-exact frozen PR 6485 -> 6515 recovery bundle."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[4]
OUTPUT = Path(__file__).with_name("ORIGINAL_SOURCE_BODIES.json")

RECORDS = (
    {
        "pr": 6485,
        "commit": "ad84cfcc857a65285389ba93b47cd7b718589be5",
        "path": ".claude/science/physics-loops/toe-axiom-closure-block109-global-dressing-involution-positivity-20260815/NO_GO_LEDGER.md",
        "git_blob": "9ffb058efd074e5bdec3ae6b9dc00a00b82abe44",
        "sha256": "1e321a487019c7468c52069b6de618517fad43c7dec5e9fa75617b0bc81fc4b7",
        "bytes": 2419,
    },
    {
        "pr": 6485,
        "commit": "ad84cfcc857a65285389ba93b47cd7b718589be5",
        "path": "docs/ADMISSIBILITY_DIRAC_KAHLER_GLOBAL_DRESSING_INVOLUTION_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "git_blob": "3ed51ad603b3c4dc9a0e9eb3c98e343b49c3b9ea",
        "sha256": "57d2409e70c69ba89767dd54b21621374f69b2168a52d05839ab2ab899cb1498",
        "bytes": 35876,
    },
    {
        "pr": 6485,
        "commit": "ad84cfcc857a65285389ba93b47cd7b718589be5",
        "path": "docs/audit/data/citation_graph_manifest.json",
        "git_blob": "e1b8fd5adc37993f6f44a7bf5ca8ec7a3a0223ac",
        "sha256": "1d1841fb2b3351ff4c76dceeb0e46439db716b81df63a5e101e8de4fc123344c",
        "bytes": 738610,
    },
    {
        "pr": 6485,
        "commit": "ad84cfcc857a65285389ba93b47cd7b718589be5",
        "path": "logs/runner-cache/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.txt",
        "git_blob": "a9e0a6e045cb34221aa1fdb876a93ab571f856ce",
        "sha256": "1485ef0775cb69098c530c8b0210e8c141b81996c8fffcf9345b4b8d50ed7a18",
        "bytes": 3528,
    },
    {
        "pr": 6485,
        "commit": "ad84cfcc857a65285389ba93b47cd7b718589be5",
        "path": "scripts/admissibility_dirac_kahler_global_dressing_involution_positivity_2026_08_15.py",
        "git_blob": "4facf35d1f8d91fa05d4df7c6e1fdc7b8047f048",
        "sha256": "de5668e1043e8cc76c376131d622f72b91cd6309fb4abecc4db95bef6f315a31",
        "bytes": 51611,
    },
    {
        "pr": 6515,
        "commit": "d6761278fca9cac617200792473a8f4da3a6cfff",
        "path": ".claude/science/physics-loops/toe-axiom-closure-block110-sector-signature-theorem-20260815/NO_GO_LEDGER.md",
        "git_blob": "b7ff3684a119dd03050566106efe2d6a2b8f5421",
        "sha256": "9c8e1432158f29dd470c61d09417b51e040678612757ef881b1299ddce680823",
        "bytes": 2123,
    },
    {
        "pr": 6515,
        "commit": "d6761278fca9cac617200792473a8f4da3a6cfff",
        "path": "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DRESSING_SECTOR_SIGNATURE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
        "git_blob": "8401946b778d8d41b0a553d0844f59e616c22e9f",
        "sha256": "f546d7d26ac2885edf44ff6ae598fa976531d838097e4a978a2bd80aecf5cd16",
        "bytes": 35027,
    },
    {
        "pr": 6515,
        "commit": "d6761278fca9cac617200792473a8f4da3a6cfff",
        "path": "docs/audit/data/citation_graph_manifest.json",
        "git_blob": "6467d60714c75b24558d87719509c86402156f38",
        "sha256": "cdfed846bddf6386ee445c27a8db0a3fade45ec953fdeceb7602fb1fcc78d227",
        "bytes": 738763,
    },
    {
        "pr": 6515,
        "commit": "d6761278fca9cac617200792473a8f4da3a6cfff",
        "path": "logs/runner-cache/admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15.txt",
        "git_blob": "57fe4458326634d26f003bdc5ffee4866d8de439",
        "sha256": "abd53257658782d6a964758417aefdf5b460eddfeb6f55bf2476a5c2cc32f64f",
        "bytes": 2945,
    },
    {
        "pr": 6515,
        "commit": "d6761278fca9cac617200792473a8f4da3a6cfff",
        "path": "scripts/admissibility_dirac_kahler_seam_dressing_sector_signature_2026_08_15.py",
        "git_blob": "853b86ecd81dfaedd6a84b8cc251d7913c54b6cf",
        "sha256": "1dd2328b94b9a9879b5ae28c2b0a82e287d05bb6be48356b14f112e5260d2850",
        "bytes": 35707,
    },
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_blob(blob: str) -> bytes:
    return subprocess.check_output(("git", "cat-file", "blob", blob), cwd=ROOT)


def verify_record(record: dict[str, object], data: bytes) -> None:
    assert len(data) == record["bytes"], (record["path"], len(data))
    assert sha256(data) == record["sha256"], record["path"]
    actual_blob = subprocess.check_output(
        ("git", "hash-object", "--stdin"), cwd=ROOT, input=data, text=False
    ).decode().strip()
    assert actual_blob == record["git_blob"], record["path"]


def build() -> None:
    bodies = []
    for source in RECORDS:
        data = read_blob(str(source["git_blob"]))
        verify_record(source, data)
        bodies.append({**source, "body_base64": base64.b64encode(data).decode("ascii")})
    payload = {
        "schema_version": 1,
        "purpose": "byte-exact recovery only; no live citation-graph authority",
        "constituents": {
            "6485": {
                "base": "8afe8dff5ccf531208238af0aaaec1f547d73874",
                "head": "ad84cfcc857a65285389ba93b47cd7b718589be5",
            },
            "6515": {
                "base": "ad84cfcc857a65285389ba93b47cd7b718589be5",
                "head": "d6761278fca9cac617200792473a8f4da3a6cfff",
            },
        },
        "distinct_paths": len({str(row["path"]) for row in RECORDS}),
        "body_versions": len(bodies),
        "encoding": "base64 of exact git-blob bytes; cache trailing whitespace preserved",
        "bodies": bodies,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def check() -> None:
    payload = json.loads(OUTPUT.read_text())
    assert payload["distinct_paths"] == 9
    assert payload["body_versions"] == 10
    assert len(payload["bodies"]) == len(RECORDS)
    for record, expected in zip(payload["bodies"], RECORDS, strict=True):
        assert {key: record[key] for key in expected} == expected
        data = base64.b64decode(record["body_base64"], validate=True)
        verify_record(record, data)
        assert data == read_blob(str(record["git_blob"])), record["path"]
    print("verified 10 source bodies across 9 distinct paths")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check()
    else:
        build()
        check()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
