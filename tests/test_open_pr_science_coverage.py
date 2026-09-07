"""Regressions for silent PR omissions and stale reading coverage."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import open_pr_science_coverage as coverage


def pr(number=7, file_count=1):
    return {"number": number, "headRefOid": "a" * 40, "title": "Supplied model",
            "body": "Claim and explicit assumptions", "baseRefName": "main", "baseRefOid": "c" * 40,
            "updatedAt": "2026-09-04T00:00:00Z", "isDraft": False,
            "url": f"https://github.com/owner/repo/pull/{number}", "changedFiles": file_count,
            "files": [{"path": f"docs/note-{i}.md", "additions": 3, "deletions": 0}
                      for i in range(file_count)]}


def inventory(*prs):
    return {"schema_version": 1, "repository": "owner/repo",
            "total_count": len(prs), "pull_requests": list(prs)}


def receipt(p):
    return {"number": p["number"], "head": p["headRefOid"],
            "inventory_identity": coverage.identity(p),
            "read_coverage": "Read body and complete primary note; code not audited."}


class CoverageTests(unittest.TestCase):
    def test_rejects_truncated_open_inventory(self):
        incomplete = inventory(pr())
        incomplete["total_count"] = 2
        with self.assertRaisesRegex(coverage.CoverageError, "total_count"):
            coverage.inventory_rows(incomplete)

    def test_rejects_gh_hundred_file_cap(self):
        p = pr(file_count=114)
        p["files"] = p["files"][:100]
        with self.assertRaisesRegex(coverage.CoverageError, "incomplete changed-file"):
            coverage.inventory_rows(inventory(p))

    def test_capture_recovers_all_paginated_files(self):
        full = pr(file_count=114)
        capped = deepcopy(full)
        capped["files"] = capped["files"][:100]
        files = [{"filename": f["path"], "additions": f["additions"],
                  "deletions": f["deletions"]} for f in full["files"]]
        total = {"data": {"repository": {"pullRequests": {"totalCount": 1}}}}
        with patch.object(coverage, "gh_json", side_effect=[total, [capped],
                                                          [files[:100], files[100:]], [full]]) as gh:
            result = coverage.capture("owner/repo")
        self.assertEqual(result["pull_requests"][0]["files"], full["files"])
        self.assertIn("--paginate", gh.call_args_list[2].args)

    def test_capture_rejects_changes_during_pagination(self):
        p = pr()
        changed = deepcopy(p)
        changed["headRefOid"] = "b" * 40
        total = {"data": {"repository": {"pullRequests": {"totalCount": 1}}}}
        with patch.object(coverage, "gh_json", side_effect=[total, [p], [changed]]):
            with self.assertRaisesRegex(coverage.CoverageError, "changed during capture"):
                coverage.capture("owner/repo")

    def test_receipts_are_not_reused_after_semantic_or_metadata_change(self):
        p = pr()
        for field, replacement in (("headRefOid", "b" * 40), ("body", "Changed assumption"),
                                   ("title", "Broader theorem"), ("baseRefName", "other-base"),
                                   ("baseRefOid", "d" * 40),
                                   ("updatedAt", "2026-09-04T01:00:00Z"), ("isDraft", True)):
            with self.subTest(field=field):
                changed = deepcopy(p)
                changed[field] = replacement
                report = coverage.compare(inventory(changed), inventory(p), {7: receipt(p)})
                self.assertFalse(report["complete"])
                self.assertEqual(report["stale_review_receipts"], [7])

    def test_file_list_change_and_reordering_are_distinct(self):
        p = pr(file_count=2)
        reordered = deepcopy(p)
        reordered["files"].reverse()
        self.assertTrue(coverage.compare(inventory(reordered), inventory(p), {7: receipt(p)})["complete"])
        changed = deepcopy(p)
        changed["files"][0]["path"] = "docs/different.md"
        self.assertFalse(coverage.compare(inventory(changed), inventory(p), {7: receipt(p)})["complete"])

    def test_old_receipt_cannot_bind_to_a_replaced_snapshot_at_same_head(self):
        old = pr()
        changed = deepcopy(old)
        changed["body"] = "New assumptions at the same commit"
        with self.assertRaisesRegex(coverage.CoverageError, "does not bind"):
            coverage.compare(inventory(changed), inventory(changed), {7: receipt(old)})

    def test_capture_rejects_malformed_rows_before_pagination(self):
        total = {"data": {"repository": {"pullRequests": {"totalCount": 1}}}}
        malformed = [None, {}, {**pr(), "number": None}, {**pr(), "files": None},
                     {**pr(), "changedFiles": "114"}, {**pr(), "files": [None]}]
        for row in malformed:
            with self.subTest(row=row):
                with patch.object(coverage, "gh_json", side_effect=[total, [row]]):
                    with self.assertRaises(coverage.CoverageError):
                        coverage.capture("owner/repo")

    def test_capture_rejects_malformed_paginated_pages(self):
        total = {"data": {"repository": {"pullRequests": {"totalCount": 1}}}}
        for pages in (None, {}, [{}], [[None]], [[{"filename": "missing-counts"}]]):
            with self.subTest(pages=pages):
                capped = pr(file_count=114)
                capped["files"] = capped["files"][:100]
                with patch.object(coverage, "gh_json", side_effect=[total, [capped], pages]):
                    with self.assertRaises(coverage.CoverageError):
                        coverage.capture("owner/repo")

    def test_new_and_closed_prs_do_not_hide_missing_coverage(self):
        old, new = pr(7), pr(8)
        report = coverage.compare(inventory(new), inventory(old), {7: receipt(old)})
        self.assertEqual(report["missing_review_receipts"], [8])
        self.assertEqual(report["no_longer_open"], [7])
        self.assertFalse(report["complete"])

    def test_wrong_head_or_repository_cannot_certify_coverage(self):
        p = pr()
        wrong = receipt(p)
        wrong["head"] = "b" * 40
        with self.assertRaises(coverage.CoverageError):
            coverage.compare(inventory(p), inventory(p), {7: wrong})
        other = inventory(p)
        other["repository"] = "another/repo"
        with self.assertRaises(coverage.CoverageError):
            coverage.compare(other, inventory(p), {7: receipt(p)})

    def test_duplicate_receipts_cannot_mask_different_reads(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / "reads.jsonl"
            line = json.dumps(receipt(pr())) + "\n"
            p.write_text(line + line)
            with self.assertRaisesRegex(coverage.CoverageError, "duplicate"):
                coverage.read_receipts([p])

    def test_matching_receipt_is_explicitly_not_a_scientific_grade(self):
        p = pr()
        report = coverage.compare(inventory(p), inventory(p), {7: receipt(p)})
        self.assertTrue(report["complete"])
        self.assertEqual(report["matched_review_receipts"], [7])
        self.assertIn("not scientific validity", report["meaning"])


class CoverageCliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(coverage.__file__).resolve()), *map(str, args)],
            capture_output=True, text=True, check=False,
        )

    def test_documented_python_entry_points_and_offline_round_trip(self):
        for command in ("capture", "receipt", "check"):
            with self.subTest(command=command):
                result = self.run_cli(command, "--help")
                self.assertEqual(result.returncode, 0, result.stderr)
        with tempfile.TemporaryDirectory() as directory:
            snapshot = Path(directory) / "inventory.json"
            snapshot.write_text(json.dumps(inventory(pr())), encoding="utf-8")
            result = self.run_cli("receipt", "--reviewed", snapshot, "--number", 7,
                                  "--read-coverage", "Fixture read; no scientific grade.")
            self.assertEqual(result.returncode, 0, result.stderr)
            receipts = Path(directory) / "reads.jsonl"
            receipts.write_text(result.stdout, encoding="utf-8")
            result = self.run_cli("check", "--current", snapshot, "--reviewed", snapshot,
                                  "--receipts", receipts)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["matched_review_receipts"], [7])

    def test_invalid_utf8_cli_inputs_return_invalid_input_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            snapshot = directory / "inventory.json"
            snapshot.write_text(json.dumps(inventory(pr())), encoding="utf-8")
            receipts = directory / "reads.jsonl"
            receipts.write_text(json.dumps(receipt(pr())) + "\n", encoding="utf-8")
            invalid = directory / "invalid-utf8"
            invalid.write_bytes(b"\xff\xfe\xff")
            cases = [
                ("receipt", "--reviewed", invalid, "--number", 7, "--read-coverage", "Read"),
                ("check", "--current", invalid, "--reviewed", snapshot, "--receipts", receipts),
                ("check", "--current", snapshot, "--reviewed", invalid, "--receipts", receipts),
                ("check", "--current", snapshot, "--reviewed", snapshot, "--receipts", invalid),
            ]
            for args in cases:
                with self.subTest(args=args):
                    result = self.run_cli(*args)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertIn("open-pr-science-coverage:", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
