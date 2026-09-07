#!/usr/bin/env python3
"""Capture complete open-PR inventories and compare declared reading coverage.

Coverage means a matching, self-reported reading receipt, not scientific
correctness, proof review, audit status, or permission to land a PR. Capture
uses the authenticated gh CLI read-only; check works entirely offline.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


FIELDS = "number,title,body,headRefOid,baseRefName,baseRefOid,updatedAt,isDraft,files,changedFiles,url"
INDEX_FIELDS = "number,headRefOid,baseRefOid,updatedAt,changedFiles"
TOTAL_QUERY = """query($owner:String!,$name:String!){repository(owner:$owner,name:$name){
pullRequests(states:OPEN){totalCount}}}"""


class CoverageError(ValueError):
    """Invalid or incomplete evidence for planning coverage."""


def gh_json(*args: str):
    result = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
    if result.returncode:
        raise CoverageError(f"gh read failed: {result.stderr.strip()}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise CoverageError("gh returned invalid JSON") from exc


def inventory_rows(inventory: dict, *, allow_capped_files: bool = False) -> dict[int, dict]:
    if not isinstance(inventory, dict) or inventory.get("schema_version") != 1:
        raise CoverageError("inventory needs schema_version: 1")
    if not isinstance(inventory.get("repository"), str) or not re.fullmatch(
        r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", inventory["repository"]
    ):
        raise CoverageError("inventory needs repository")
    prs = inventory.get("pull_requests")
    count = inventory.get("total_count")
    if not isinstance(prs, list) or type(count) is not int or count != len(prs):
        raise CoverageError("open-PR total_count does not match the supplied list")
    rows = {}
    for pr in prs:
        if not isinstance(pr, dict):
            raise CoverageError("each PR must be an object")
        number = pr.get("number")
        if type(number) is not int or number < 1 or number in rows:
            raise CoverageError(f"invalid or duplicate PR number: {number!r}")
        for field in ("headRefOid", "baseRefOid"):
            if not isinstance(pr.get(field), str) or not re.fullmatch(r"[0-9a-f]{40}", pr[field]):
                raise CoverageError(f"PR #{number}: missing full {field} commit")
        for field in ("title", "body", "baseRefName", "updatedAt", "url"):
            if not isinstance(pr.get(field), str):
                raise CoverageError(f"PR #{number}: missing {field}")
        if type(pr.get("isDraft")) is not bool:
            raise CoverageError(f"PR #{number}: missing isDraft")
        files, expected = pr.get("files"), pr.get("changedFiles")
        if (not isinstance(files, list) or type(expected) is not int or expected < 0
                or len(files) > expected or (not allow_capped_files and len(files) != expected)):
            raise CoverageError(f"PR #{number}: incomplete changed-file list (expected {expected})")
        paths = set()
        for file in files:
            if not isinstance(file, dict) or not isinstance(file.get("path"), str):
                raise CoverageError(f"PR #{number}: malformed file entry")
            path = file["path"]
            if not path or path in paths:
                raise CoverageError(f"PR #{number}: empty or duplicate file path")
            paths.add(path)
            for field in ("additions", "deletions"):
                if type(file.get(field)) is not int or file[field] < 0:
                    raise CoverageError(f"PR #{number}: invalid {field} for {path}")
        rows[number] = pr
    return rows


def identity(pr: dict) -> str:
    """Bind head/base, proposal text, file set and discussion-change signal."""
    payload = {field: pr[field] for field in FIELDS.split(",") if field != "files"}
    payload["files"] = sorted(pr["files"], key=lambda item: item["path"])
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def index_signature(prs: list[dict]) -> list[tuple]:
    if not isinstance(prs, list):
        raise CoverageError("malformed final PR index")
    try:
        return sorted(tuple(pr[field] for field in INDEX_FIELDS.split(",")) for pr in prs)
    except (KeyError, TypeError) as exc:
        raise CoverageError("malformed final PR index") from exc


def capture(repository: str) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise CoverageError("repository must be owner/name")
    owner, name = repository.split("/")
    total_result = gh_json("api", "graphql", "-f", f"query={TOTAL_QUERY}",
                           "-F", f"owner={owner}", "-F", f"name={name}")
    try:
        total = total_result["data"]["repository"]["pullRequests"]["totalCount"]
    except (KeyError, TypeError) as exc:
        raise CoverageError("could not read the repository's open-PR total") from exc
    if type(total) is not int or total < 0:
        raise CoverageError("invalid open-PR total")
    limit = str(max(1, total + 1))
    prs = gh_json("pr", "list", "--repo", repository, "--state", "open", "--limit", limit,
                  "--json", FIELDS)
    if not isinstance(prs, list) or len(prs) != total:
        raise CoverageError("open PR set changed during capture; retry with a fresh snapshot")
    inventory = {"schema_version": 1, "repository": repository, "total_count": total,
                 "pull_requests": prs}
    inventory_rows(inventory, allow_capped_files=True)
    for pr in prs:
        if len(pr["files"]) != pr["changedFiles"]:
            pages = gh_json("api", f"repos/{repository}/pulls/{pr['number']}/files?per_page=100",
                            "--paginate", "--slurp")
            try:
                if not isinstance(pages, list) or any(not isinstance(page, list) for page in pages):
                    raise CoverageError(f"PR #{pr['number']}: malformed paginated files")
                pr["files"] = [{"path": f["filename"], "additions": f["additions"],
                                "deletions": f["deletions"]} for page in pages for f in page]
            except (KeyError, TypeError) as exc:
                raise CoverageError(f"PR #{pr['number']}: malformed paginated files") from exc
    inventory["pull_requests"] = sorted(prs, key=lambda item: item["number"], reverse=True)
    inventory_rows(inventory)  # Also detects server-side file-list caps.
    final = gh_json("pr", "list", "--repo", repository, "--state", "open", "--limit", limit,
                    "--json", INDEX_FIELDS)
    if index_signature(final) != index_signature(prs):
        raise CoverageError("PR heads, bases, metadata or file counts changed during capture; retry")
    return inventory


def read_receipts(paths: list[Path]) -> dict[int, dict]:
    receipts = {}
    for path in paths:
        for line_number, line in enumerate(path.read_text().splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise CoverageError(f"{path}:{line_number}: invalid JSON receipt") from exc
            if not isinstance(row, dict):
                raise CoverageError(f"{path}:{line_number}: receipt must be an object")
            number = row.get("number")
            if type(number) is not int or number < 1 or number in receipts:
                raise CoverageError(f"invalid or duplicate reading receipt for PR {number!r}")
            if not isinstance(row.get("read_coverage"), str) or not row["read_coverage"].strip():
                raise CoverageError(f"PR #{number}: receipt must describe what was actually read")
            if not isinstance(row.get("head"), str) or not re.fullmatch(r"[0-9a-f]{40}", row["head"]):
                raise CoverageError(f"PR #{number}: receipt needs its full read head commit")
            if not isinstance(row.get("inventory_identity"), str) or not re.fullmatch(
                r"[0-9a-f]{64}", row["inventory_identity"]
            ):
                raise CoverageError(f"PR #{number}: receipt needs the identity of its read inventory row")
            receipts[number] = row
    return receipts


def compare(current: dict, reviewed: dict, receipts: dict[int, dict]) -> dict:
    now, before = inventory_rows(current), inventory_rows(reviewed)
    if current["repository"] != reviewed["repository"]:
        raise CoverageError("current and reviewed inventories name different repositories")
    for number, receipt in receipts.items():
        if (number not in before or receipt["head"] != before[number]["headRefOid"]
                or receipt.get("inventory_identity") != identity(before[number])):
            raise CoverageError(f"PR #{number}: receipt does not bind to the reviewed inventory")
    matched, missing, stale = [], [], []
    for number in sorted(now, reverse=True):
        if number not in receipts:
            missing.append(number)
        elif identity(now[number]) != identity(before[number]):
            stale.append(number)
        else:
            matched.append(number)
    return {"schema_version": 1, "repository": current["repository"],
            "meaning": "matching self-reported reading coverage; not scientific validity or audit status",
            "open_count": len(now), "matched_review_receipts": matched,
            "missing_review_receipts": missing, "stale_review_receipts": stale,
            "no_longer_open": sorted(set(receipts) - set(now), reverse=True),
            "complete": not missing and not stale}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    snapshot = commands.add_parser("capture", help="read GitHub and refuse incomplete/drifting inventories")
    snapshot.add_argument("--repo", required=True)
    snapshot.add_argument("--output", type=Path, required=True)
    bind = commands.add_parser("receipt", help="record a reader's coverage statement against a saved inventory row")
    bind.add_argument("--reviewed", type=Path, required=True)
    bind.add_argument("--number", type=int, required=True)
    bind.add_argument("--read-coverage", required=True)
    check = commands.add_parser("check", help="compare current inventory with a reviewed snapshot and JSONL receipts")
    check.add_argument("--current", type=Path, required=True)
    check.add_argument("--reviewed", type=Path, required=True)
    check.add_argument("--receipts", type=Path, nargs="+", required=True)
    check.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "capture":
            result = capture(args.repo)
            args.output.write_text(json.dumps(result, indent=2) + "\n")
            print(f"Captured {result['total_count']} open PRs with complete changed-file lists.")
            return 0
        if args.command == "receipt":
            rows = inventory_rows(json.loads(args.reviewed.read_text()))
            if args.number not in rows or not args.read_coverage.strip():
                raise CoverageError("receipt needs a PR in the reviewed inventory and a nonempty coverage statement")
            pr = rows[args.number]
            print(json.dumps({"number": args.number, "head": pr["headRefOid"],
                              "inventory_identity": identity(pr), "read_coverage": args.read_coverage}))
            return 0
        result = compare(json.loads(args.current.read_text()), json.loads(args.reviewed.read_text()),
                         read_receipts(args.receipts))
        encoded = json.dumps(result, indent=2) + "\n"
        if args.output:
            args.output.write_text(encoded)
        print(encoded, end="")
        return 0 if result["complete"] else 1
    except (CoverageError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"open-pr-science-coverage: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
