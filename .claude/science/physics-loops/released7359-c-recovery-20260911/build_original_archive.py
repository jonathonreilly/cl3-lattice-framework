#!/usr/bin/env python3
"""Build the deterministic released-7359-C original-occurrence archive.

This program performs Git object reads, hashing, encoding, and delta checks.
It does not import or execute any science source.
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
    "backlog-released18-20260910/7359"
)
REVIEW = EVIDENCE / "review-C"
BINDINGS = REVIEW / "SOURCE_BINDINGS.json"
INVENTORY = EVIDENCE / "C-source-preparation" / "ACTUAL_ORIGINAL_INVENTORY.json"
REVIEW_DISPOSITIONS = REVIEW / "dispositions.json"
HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / "ORIGINAL_OCCURRENCES.json.gz.b64"
INDEX = HERE / "ORIGINAL_OCCURRENCES_INDEX.json"
DELTA_VERIFICATION = HERE / "ORIGINAL_DELTA_VERIFICATION.json"
BUILD_RECEIPT = HERE / "ARCHIVE_BUILD_RECEIPT.json"


def sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def git_bytes(*args: str) -> bytes:
    return subprocess.check_output(("git", "-C", str(REPO), *args))


def git_text(*args: str) -> str:
    return git_bytes(*args).decode().strip()


def commit(revision: str) -> str:
    return git_text("rev-parse", f"{revision}^{{commit}}")


def blob_or_none(revision: str, path: str) -> tuple[str | None, bytes | None]:
    spec = f"{revision}:{path}"
    probe = subprocess.run(
        ("git", "-C", str(REPO), "cat-file", "-e", spec),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if probe.returncode != 0:
        return None, None
    return git_text("rev-parse", spec), git_bytes("show", spec)


def name_status(base: str, head: str) -> list[str]:
    text = git_text("diff", "--name-status", "--no-renames", base, head)
    return text.splitlines() if text else []


def main() -> None:
    source = json.loads(BINDINGS.read_text())
    inventory = json.loads(INVENTORY.read_text())
    review_dispositions = json.loads(REVIEW_DISPOSITIONS.read_text())
    source_rows = source["rows"]
    inventory_rows = [
        {
            "pr": group["pr"],
            "base": group["base"],
            "head": group["head"],
            **path,
        }
        for group in inventory["rows"]
        for path in group["paths"]
    ]
    if len(source_rows) != 26 or len(inventory_rows) != 26:
        raise RuntimeError("expected 26 original path occurrences")
    if len({(row["pr"], row["path"]) for row in source_rows}) != 26:
        raise RuntimeError("duplicate PR/path occurrence in source bindings")
    if len({row["path"] for row in source_rows}) != 22:
        raise RuntimeError("expected 22 unique original paths")

    inventory_by_key = {(row["pr"], row["path"]): row for row in inventory_rows}
    source_by_key = {(row["pr"], row["path"]): row for row in source_rows}
    if set(inventory_by_key) != set(source_by_key):
        raise RuntimeError("inventory/source-binding occurrence sets differ")
    for key, row in source_by_key.items():
        other = inventory_by_key[key]
        for field in (
            "base", "head", "sha256", "bytes", "lines", "successor_byte_equal"
        ):
            if row[field] != other[field]:
                raise RuntimeError(f"inventory mismatch {field}: {key}")

    disposition_by_key = {
        (row["pr"], row["path"]): row for row in review_dispositions["rows"]
    }
    if set(disposition_by_key) != set(source_by_key):
        raise RuntimeError("review disposition occurrence set is incomplete")

    declared_deltas = {
        row["pr"]: row["delta"] for row in source["actual_deltas"]
    }
    delta_rows = []
    status_by_occurrence: dict[tuple[int, str], str] = {}
    groups = inventory["rows"]
    previous_head = None
    for group in groups:
        pr = int(group["pr"])
        base = commit(group["base"])
        head = commit(group["head"])
        if base != group["base"] or head != group["head"]:
            raise RuntimeError(f"noncanonical base/head identity for PR {pr}")
        ancestor = subprocess.run(
            ("git", "-C", str(REPO), "merge-base", "--is-ancestor", base, head)
        ).returncode == 0
        if not ancestor:
            raise RuntimeError(f"base is not an ancestor of head for PR {pr}")
        if previous_head is not None and base != previous_head:
            raise RuntimeError(f"released PR chain is discontinuous before PR {pr}")
        previous_head = head
        actual = name_status(base, head)
        expected_paths = [row["path"] for row in group["paths"]]
        actual_paths = [line.split("\t", 1)[1] for line in actual]
        if actual_paths != expected_paths:
            raise RuntimeError(f"complete changed-path order/set mismatch for PR {pr}")
        if declared_deltas.get(pr) != actual:
            raise RuntimeError(f"review-declared delta differs from Git for PR {pr}")
        statuses = {}
        for line in actual:
            status, path = line.split("\t", 1)
            if status not in {"A", "M"}:
                raise RuntimeError(f"unexpected delta status {status} for PR {pr}")
            statuses[path] = status
            status_by_occurrence[(pr, path)] = status
        patch = git_bytes("diff", "--binary", "--full-index", base, head)
        delta_rows.append({
            "pr": pr,
            "base": base,
            "head": head,
            "base_tree": git_text("rev-parse", f"{base}^{{tree}}"),
            "head_tree": git_text("rev-parse", f"{head}^{{tree}}"),
            "base_is_ancestor_of_head": ancestor,
            "complete_name_status": actual,
            "complete_changed_path_count": len(actual),
            "inventory_paths_match_complete_delta": actual_paths == expected_paths,
            "review_declared_delta_matches_git": declared_deltas.get(pr) == actual,
            "full_binary_diff_sha256": sha256_bytes(patch),
            "full_binary_diff_bytes": len(patch),
        })

    if previous_head != inventory["successor_head"]:
        raise RuntimeError("last original head differs from frozen successor")
    if source["successor"] != inventory["successor_head"]:
        raise RuntimeError("review source successor differs from inventory")

    entries = []
    for archive_index, row in enumerate(source_rows):
        key = (int(row["pr"]), row["path"])
        status = status_by_occurrence[key]
        head_blob, body = blob_or_none(row["head"], row["path"])
        if head_blob is None or body is None:
            raise RuntimeError(f"missing original head body: {key}")
        digest = sha256_bytes(body)
        lines = len(body.splitlines())
        if digest != row["sha256"] or len(body) != row["bytes"] or lines != row["lines"]:
            raise RuntimeError(f"original identity mismatch: {key}")
        base_blob, base_body = blob_or_none(row["base"], row["path"])
        if status == "A" and base_body is not None:
            raise RuntimeError(f"added path unexpectedly exists at base: {key}")
        if status == "M" and base_body is None:
            raise RuntimeError(f"modified path absent at base: {key}")
        successor_blob, successor_body = blob_or_none(source["successor"], row["path"])
        successor_equal = successor_body == body
        if successor_equal != row["successor_byte_equal"]:
            raise RuntimeError(f"successor equality mismatch: {key}")
        current_main_blob, current_main_body = blob_or_none(source["main"], row["path"])
        current_main_sha = sha256_bytes(current_main_body) if current_main_body else None
        if current_main_sha != row["current_main_sha256"]:
            raise RuntimeError(f"current-main identity mismatch: {key}")
        review_row = disposition_by_key[key]
        entries.append({
            "archive_index": archive_index,
            "pr": row["pr"],
            "base": row["base"],
            "head": row["head"],
            "revision_kind": "original_pr_head",
            "change_status": status,
            "path": row["path"],
            "bytes": len(body),
            "lines": lines,
            "sha256": digest,
            "head_git_blob": head_blob,
            "base_git_blob": base_blob,
            "base_sha256": sha256_bytes(base_body) if base_body else None,
            "successor_git_blob": successor_blob,
            "successor_sha256": sha256_bytes(successor_body) if successor_body else None,
            "successor_byte_equal": successor_equal,
            "current_main_git_blob": current_main_blob,
            "current_main_sha256": current_main_sha,
            "kind": review_row["kind"],
            "finding_ids": review_row["findings"],
            "archive_disposition": "preserved_exactly; historical evidence only",
            "review_disposition": review_row["disposition"],
            "content_base64": base64.b64encode(body).decode("ascii"),
        })

    delta_verification = {
        "schema": "released7359-c-original-delta-verification-v1",
        "status": "PASS",
        "repository": str(REPO),
        "current_main": source["main"],
        "frozen_successor": source["successor"],
        "source_bindings_sha256": sha256(BINDINGS),
        "actual_inventory_sha256": sha256(INVENTORY),
        "review_dispositions_sha256": sha256(REVIEW_DISPOSITIONS),
        "original_occurrence_count": len(entries),
        "unique_original_path_count": len({entry["path"] for entry in entries}),
        "all_original_head_bodies_match": True,
        "all_base_presence_matches_delta_status": True,
        "all_successor_equality_flags_match": True,
        "all_current_main_identities_match": True,
        "released_chain_continuous": True,
        "complete_deltas": delta_rows,
        "science_executed": False,
        "formal_audit": False,
    }
    write_json(DELTA_VERIFICATION, delta_verification)

    payload = {
        "format": "released7359-c-original-occurrences-v1",
        "source_bindings_sha256": sha256(BINDINGS),
        "actual_inventory_sha256": sha256(INVENTORY),
        "review_dispositions_sha256": sha256(REVIEW_DISPOSITIONS),
        "delta_verification_sha256": sha256(DELTA_VERIFICATION),
        "current_main": source["main"],
        "frozen_successor": source["successor"],
        "original_occurrence_count": len(entries),
        "unique_original_path_count": len({entry["path"] for entry in entries}),
        "entries": entries,
    }
    raw = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    packed = gzip.compress(raw, compresslevel=9, mtime=0)
    ARCHIVE.write_text(base64.b64encode(packed).decode("ascii") + "\n")

    index = {
        key: payload[key]
        for key in (
            "format", "source_bindings_sha256", "actual_inventory_sha256",
            "review_dispositions_sha256", "delta_verification_sha256",
            "current_main", "frozen_successor", "original_occurrence_count",
            "unique_original_path_count",
        )
    }
    index.update({
        "archive_sha256": sha256(ARCHIVE),
        "archive_bytes": ARCHIVE.stat().st_size,
        "decoded_payload_sha256": sha256_bytes(raw),
        "decoded_payload_bytes": len(raw),
        "gzip_bytes": len(packed),
        "gzip_mtime": 0,
        "entries": [
            {key: value for key, value in entry.items() if key != "content_base64"}
            for entry in entries
        ],
    })
    write_json(INDEX, index)
    receipt = {
        "schema": "released7359-c-archive-build-receipt-v1",
        "status": "PASS",
        "archive": {"path": ARCHIVE.name, "sha256": sha256(ARCHIVE), "bytes": ARCHIVE.stat().st_size},
        "index": {"path": INDEX.name, "sha256": sha256(INDEX), "bytes": INDEX.stat().st_size},
        "delta_verification": {
            "path": DELTA_VERIFICATION.name,
            "sha256": sha256(DELTA_VERIFICATION),
            "bytes": DELTA_VERIFICATION.stat().st_size,
        },
        "review_report_sha256": sha256(REVIEW / "REPORT.md"),
        "review_receipt_sha256": sha256(REVIEW / "RECEIPT.json"),
        "source_bindings_sha256": sha256(BINDINGS),
        "actual_inventory_sha256": sha256(INVENTORY),
        "review_dispositions_sha256": sha256(REVIEW_DISPOSITIONS),
        "original_occurrence_count": len(entries),
        "unique_original_path_count": len({entry["path"] for entry in entries}),
        "science_executed": False,
        "formal_audit": False,
    }
    write_json(BUILD_RECEIPT, receipt)
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
