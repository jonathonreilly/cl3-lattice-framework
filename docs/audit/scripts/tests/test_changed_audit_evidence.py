"""Real local Git fixtures for committed and uncommitted review evidence scope."""

import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_changed_audit_evidence as gate


class ChangedEvidenceScopeTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="changed-evidence-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Local fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "core.hooksPath", "/dev/null")
        self.git("config", "commit.gpgsign", "false")
        for name in ["docs/staged.md", "docs/unstaged.md", "docs/moved name.md"]:
            self.write(name, "Original mathematical statement.\n")
        self.write(gate.LEGACY_EPOCH_BASELINE_PATH, "{}\n")
        self.git("add", ".")
        self.git("commit", "-qm", "base")
        self.git("update-ref", "refs/remotes/origin/main", "HEAD")
        self.git("checkout", "-qb", "candidate")
        self.ledger = Path(self.temp.name) / "ledger.json"
        self.ledger.write_text(json.dumps({"rows": {
            name: {"claim_type": "positive_theorem", "note_path": f"docs/{name}.md",
                   "runner_path": "scripts/missing-evidence.py"}
            for name in ["staged", "unstaged", "new"]
        }}))
        self.enter = contextlib.ExitStack()
        self.addCleanup(self.enter.close)
        self.enter.enter_context(mock.patch.object(gate, "REPO_ROOT", self.root))
        self.enter.enter_context(mock.patch.object(gate, "LEDGER_PATH", self.ledger))
        # The fixture supplies its own ledger; readiness itself is real.
        self.enter.enter_context(mock.patch.object(gate.ledger_io, "ensure_cache"))

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True)

    def write(self, path, body):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body)

    def report(self, include=True):
        return gate.build_report("origin/main", include_worktree=include)

    def assert_missing_evidence(self, claim_id):
        report = self.report()
        self.assertEqual([row["claim_id"] for row in report["checked"]], [claim_id])
        self.assertEqual(report["failures"][0]["issue"],
                         "runner_source_missing:scripts/missing-evidence.py")

    def test_committed_default_remains_backward_compatible(self):
        self.write("docs/staged.md", "Changed committed claim.\n")
        self.git("add", "--", "docs/staged.md")
        self.git("commit", "-qm", "claim")
        self.write("docs/unstaged.md", "Uncommitted claim.\n")
        self.assertEqual(gate.changed_paths("origin/main"), {"docs/staged.md"})
        self.assertEqual(self.report(False)["diff_scope"], "committed")

    def test_staged_only_claim_reaches_real_readiness_check(self):
        self.write("docs/staged.md", "Changed staged claim.\n")
        self.git("add", "--", "docs/staged.md")
        self.assertEqual(self.report(False)["checked"], [])
        self.assert_missing_evidence("staged")

    def test_unstaged_only_claim_reaches_real_readiness_check(self):
        self.write("docs/unstaged.md", "Changed unstaged claim.\n")
        self.assert_missing_evidence("unstaged")

    def test_untracked_only_claim_reaches_real_readiness_check(self):
        self.write("docs/new.md", "New mathematical claim.\n")
        self.assert_missing_evidence("new")

    def test_scope_union_keeps_staged_change_reversed_in_worktree(self):
        self.write("docs/staged.md", "Staged claim.\n")
        self.git("add", "--", "docs/staged.md")
        self.write("docs/staged.md", "Original mathematical statement.\n")
        self.write("docs/unstaged.md", "Unstaged claim.\n")
        self.write("docs/new.md", "New claim.\n")
        report = self.report()
        self.assertEqual({row["claim_id"] for row in report["failures"]},
                         {"staged", "unstaged", "new"})
        self.assertEqual(report["changed_path_count"], 3)
        self.assertEqual(report["control_failures"][0]["control"], "mixed_candidate_versions")

    def test_staged_bad_runner_cannot_pass_from_clean_worktree_bytes(self):
        self.write("docs/new.md", "Mathematical claim.\n")
        self.write("scripts/missing-evidence.py", "AUDIT_INPUT_PATHS = ['missing-input']\n")
        self.git("add", "--", "scripts/missing-evidence.py")
        self.write("scripts/missing-evidence.py", "print('Current working copy')\n")
        report = self.report()
        self.assertEqual(report["failures"], [])  # Working bytes alone are readable.
        self.assertEqual(report["control_failures"][0]["changed_surfaces"],
                         ["scripts/missing-evidence.py"])
        self.git("add", "--", "scripts/missing-evidence.py")
        self.assertEqual(self.report()["control_failures"], [])

    def test_staged_runner_deletion_cannot_pass_from_untracked_recreation(self):
        self.write("docs/new.md", "Mathematical claim.\n")
        runner = "scripts/missing-evidence.py"
        self.write(runner, "print('Original runner')\n")
        self.git("add", "--", runner)
        self.git("commit", "-qm", "runner")
        self.git("rm", "--", runner)
        self.write(runner, "print('Original runner')\n")
        self.assertEqual(self.git("diff", "--name-only"), "")
        report = self.report()
        self.assertEqual(report["failures"], [])
        self.assertEqual(report["control_failures"][0]["changed_surfaces"], [runner])

    def test_staged_deletion_with_ignored_recreation_is_also_ambiguous(self):
        runner = "scripts/missing-evidence.py"
        self.write(runner, "print('Original runner')\n")
        self.git("add", "--", runner)
        self.git("commit", "-qm", "runner")
        self.git("rm", "--", runner)
        self.write(".git/info/exclude", runner + "\n")
        self.write(runner, "print('Original runner')\n")
        self.assertEqual(self.git("ls-files", "--others", "--exclude-standard"), "")
        conflicts = gate.candidate_version_conflicts()
        self.assertEqual(conflicts[0]["changed_surfaces"], [runner])

    def test_staged_rename_with_ignored_old_path_recreation_is_ambiguous(self):
        runner = "scripts/missing-evidence.py"
        self.write(runner, "print('Original runner')\n")
        self.git("add", "--", runner)
        self.git("commit", "-qm", "runner")
        self.git("mv", "--", runner, "scripts/renamed.py")
        self.write(".git/info/exclude", runner + "\n")
        self.write(runner, "print('Original runner')\n")
        self.assertEqual(self.git("diff", "--cached", "--diff-filter=D", "--name-only"), "")
        self.assertEqual(gate.candidate_version_conflicts()[0]["changed_surfaces"], [runner])

    def test_disjoint_staged_and_unstaged_changes_are_unambiguous(self):
        self.write("docs/staged.md", "Staged change.\n")
        self.git("add", "--", "docs/staged.md")
        self.write("docs/unstaged.md", "Unstaged change.\n")
        self.assertEqual(self.report()["control_failures"], [])

    def test_rename_keeps_both_paths_and_preserves_filename_bytes(self):
        target = "docs/ renamed\nname.md"
        self.git("mv", "--", "docs/moved name.md", target)
        self.assertEqual(gate.changed_paths("origin/main", include_worktree=True),
                         {"docs/moved name.md", target})
        self.git("commit", "-qm", "rename")
        self.assertEqual(gate.changed_paths("origin/main"),
                         {"docs/moved name.md", target})

    def test_deleted_note_is_reported_missing(self):
        (self.root / "docs/unstaged.md").unlink()
        report = self.report()
        self.assertEqual(report["failures"][0]["issue"],
                         "target_source_missing:docs/unstaged.md")

    def test_staged_immutable_control_change_is_not_skipped(self):
        self.write(gate.LEGACY_EPOCH_BASELINE_PATH, '{"changed": true}\n')
        self.git("add", "--", gate.LEGACY_EPOCH_BASELINE_PATH)
        self.assertEqual(self.report(False)["control_failures"], [])
        self.assertEqual(self.report()["control_failures"][0]["control"],
                         "immutable_legacy_science_epoch_baseline")

    def test_cli_flag_returns_failure_and_names_candidate_scope(self):
        self.write("docs/new.md", "New claim.\n")
        output = io.StringIO()
        with mock.patch.object(sys, "argv", ["check", "--include-worktree", "--json"]), \
                contextlib.redirect_stdout(output):
            code = gate.main()
        self.assertEqual(code, 1)
        report = json.loads(output.getvalue())
        self.assertEqual(report["diff_scope"], "committed_and_worktree")
        self.assertEqual(report["failures"][0]["claim_id"], "new")


if __name__ == "__main__":
    unittest.main()
