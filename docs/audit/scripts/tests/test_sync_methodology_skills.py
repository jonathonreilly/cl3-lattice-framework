"""Temporary local Git fixtures for safe, complete methodology skill sync."""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[4] / "scripts/sync_methodology_skills.py"
SPEC = importlib.util.spec_from_file_location("sync_methodology_skills", SCRIPT)
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class MethodologySkillSyncTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.source = self.repo / sync.SKILLS_REL
        self.destination = self.root / "codex/skills"
        self.backups = self.root / "codex/skill-backups"
        self.make_skill("review-loop")
        self.make_skill("audit-loop")
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.repo), *args], check=True,
            capture_output=True, text=True,
        ).stdout.strip()

    def make_skill(self, name):
        folder = self.source / name
        (folder / "references").mkdir(parents=True)
        (folder / "agents").mkdir()
        (folder / "SKILL.md").write_text(f"---\nname: {name}\n---\nCurrent body\n")
        (folder / "references/check.md").write_text("Current reference\n")
        (folder / "agents/openai.yaml").write_text("interface: {}\n")
        (folder / "empty").mkdir()
        return folder

    def install(self, name="review-loop"):
        self.destination.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.source / name, self.destination / name)
        return self.destination / name

    def run_sync(self, *args):
        output, error = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
            code = sync.main(["--repo-root", str(self.repo), "--destination", str(self.destination), *args])
        return code, json.loads(output.getvalue()) if output.getvalue() else None, error.getvalue()

    def test_default_check_finds_reference_drift_without_writes(self):
        installed = self.install()
        (installed / "references/check.md").write_text("Old reference\n")
        before = sync.tree_manifest(self.root)
        code, report, error = self.run_sync()
        self.assertEqual(code, 1, error)
        self.assertEqual(report["skills"][0]["changed_paths"], ["references/check.md"])
        self.assertEqual(sync.tree_manifest(self.root), before)
        self.assertFalse(self.backups.exists())
        self.assertFalse((self.destination / "audit-loop").exists())

    def test_default_check_does_not_create_missing_destination(self):
        before = sync.tree_manifest(self.root)
        code, report, error = self.run_sync()
        self.assertEqual(code, 0, error)
        self.assertEqual(report["skills"], [])
        self.assertEqual(sync.tree_manifest(self.root), before)

    def test_explicit_check_is_read_only_and_cannot_combine_with_apply(self):
        installed = self.install()
        (installed / "references/check.md").write_text("Old reference\n")
        before = sync.tree_manifest(self.root)
        code, report, error = self.run_sync("--check")
        self.assertEqual(code, 1, error)
        self.assertEqual(report["mode"], "check")
        self.assertEqual(sync.tree_manifest(self.root), before)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
            sync.main(["--check", "--apply"])
        self.assertEqual(caught.exception.code, 2)

    def test_explicit_missing_skill_installs_and_records_git_and_digests(self):
        code, report, error = self.run_sync("--skill", "review-loop")
        self.assertEqual(code, 1, error)
        self.assertEqual(report["skills"][0]["status"], "missing")
        code, report, error = self.run_sync("--skill", "review-loop", "--apply")
        self.assertEqual(code, 0, error)
        self.assertEqual(sync.tree_manifest(self.destination / "review-loop"), sync.tree_manifest(self.source / "review-loop"))
        metadata = json.loads((Path(report["backup"]) / "metadata.json").read_text())
        self.assertEqual(metadata["source"]["revision"], self.git("rev-parse", "HEAD"))
        self.assertFalse(metadata["source"]["worktree_dirty"])
        self.assertIn("sha256", metadata["skills"][0]["source_manifest"]["references/check.md"])
        self.assertNotIn(self.destination, Path(report["backup"]).parents)

    def test_customizations_are_backed_up_and_unrelated_skills_untouched(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Locally customized body\n")
        (installed / "custom.txt").write_bytes(b"custom bytes\x00\xff")
        (installed / "custom.txt").chmod(0o600)
        (installed / "empty-local-directory").mkdir()
        previous = sync.tree_manifest(installed)
        for name in ["custom-skill", ".system"]:
            (self.destination / name).mkdir()
            (self.destination / name / "SKILL.md").write_text("Unrelated\n")
        other = {name: (self.destination / name / "SKILL.md").read_bytes() for name in ["custom-skill", ".system"]}
        code, report, error = self.run_sync("--apply")
        self.assertEqual(code, 0, error)
        self.assertEqual(sync.tree_manifest(Path(report["backup"]) / "installed/review-loop"), previous)
        self.assertEqual(sync.tree_manifest(installed), sync.tree_manifest(self.source / "review-loop"))
        for name, expected in other.items():
            self.assertEqual((self.destination / name / "SKILL.md").read_bytes(), expected)
        self.assertFalse((self.destination / "audit-loop").exists())

    def test_all_installs_all_and_repeated_selection_deduplicates(self):
        code, report, error = self.run_sync("--skill", "review-loop", "--skill", "audit-loop", "--skill", "review-loop")
        self.assertEqual(code, 1, error)
        self.assertEqual(len(report["skills"]), 2)
        code, report, error = self.run_sync("--all", "--apply")
        self.assertEqual(code, 0, error)
        self.assertEqual({item["skill"] for item in report["skills"]}, {"review-loop", "audit-loop"})

    def test_dirty_source_is_reported_without_claiming_head_bytes(self):
        (self.source / "review-loop/references/check.md").write_text("Reviewed but uncommitted\n")
        code, report, error = self.run_sync("--skill", "review-loop", "--apply")
        self.assertEqual(code, 0, error)
        self.assertTrue(report["source"]["worktree_dirty"])
        self.assertTrue(report["source"]["skills_dirty"])
        self.assertEqual((self.destination / "review-loop/references/check.md").read_text(), "Reviewed but uncommitted\n")

    def test_unknown_traversal_and_system_names_are_refused(self):
        for name in ["missing", "../review-loop", ".system", "/tmp/review-loop"]:
            with self.subTest(name=name):
                code, _, error = self.run_sync("--skill", name, "--apply")
                self.assertEqual(code, 2)
                self.assertIn("Unknown or unsafe", error)
                self.assertFalse(self.destination.exists())

    def test_source_and_installed_symlinks_are_refused(self):
        installed = self.install()
        link = self.source / "review-loop/references/link.md"
        link.symlink_to(self.root / "outside")
        code, _, error = self.run_sync("--apply")
        self.assertEqual(code, 2)
        self.assertIn("Symlink", error)
        link.unlink()
        shutil.rmtree(installed)
        installed.symlink_to(self.source / "review-loop", target_is_directory=True)
        code, _, error = self.run_sync("--apply")
        self.assertEqual(code, 2)
        self.assertIn("Symlink", error)
        self.assertTrue(installed.is_symlink())
        self.assertFalse(self.backups.exists())

    def test_destination_symlink_and_backup_inside_discovery_are_refused(self):
        actual = self.root / "actual"
        actual.mkdir()
        self.destination.parent.mkdir()
        self.destination.symlink_to(actual, target_is_directory=True)
        code, _, error = self.run_sync("--all", "--apply")
        self.assertEqual(code, 2)
        self.assertIn("Symlink", error)
        self.destination.unlink()
        code, _, error = self.run_sync("--all", "--apply", "--backup-root", str(self.destination / "backups"))
        self.assertEqual(code, 2)
        self.assertIn("outside", error)
        self.assertFalse(self.destination.exists())

    def test_system_destination_is_refused(self):
        code, _, error = self.run_sync("--all", "--apply", "--destination", str(self.destination / ".system"))
        self.assertEqual(code, 2)
        self.assertIn("System skill directories", error)
        self.assertFalse(self.destination.exists())

    def test_source_change_after_plan_does_not_replace_installed_skill(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Previous local version\n")
        previous = sync.tree_manifest(installed)
        provenance = sync.source_provenance(self.repo)
        plan = sync.make_plan(self.repo, self.destination, None, False)
        (self.source / "review-loop/references/check.md").write_text("Concurrent source edit\n")
        with self.assertRaisesRegex(sync.SyncError, "Source changed"):
            sync.apply_plan(self.repo, self.destination, self.backups, provenance, plan)
        self.assertEqual(sync.tree_manifest(installed), previous)

    def test_local_change_after_plan_is_preserved(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Previous local version\n")
        provenance = sync.source_provenance(self.repo)
        plan = sync.make_plan(self.repo, self.destination, None, False)
        (installed / "custom.txt").write_text("Concurrent local edit\n")
        previous = sync.tree_manifest(installed)
        with self.assertRaisesRegex(sync.SyncError, "Installed skill changed"):
            sync.apply_plan(self.repo, self.destination, self.backups, provenance, plan)
        self.assertEqual(sync.tree_manifest(installed), previous)

    def test_failed_replacement_restores_original_and_keeps_backup(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Old body\n")
        previous = sync.tree_manifest(installed)
        real_replace = os.replace

        def fail_candidate(source, destination):
            if Path(source).name == "candidate":
                raise OSError("simulated installation failure")
            return real_replace(source, destination)

        with mock.patch.object(sync.os, "replace", side_effect=fail_candidate):
            code, _, error = self.run_sync("--apply")
        self.assertEqual(code, 2)
        self.assertIn("Recovery backup:", error)
        self.assertEqual(sync.tree_manifest(installed), previous)
        saved = next(self.backups.glob("*/installed/review-loop"))
        self.assertEqual(sync.tree_manifest(saved), previous)

    def test_last_check_to_rename_edit_is_restored_with_actual_bytes(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Old body\n")
        real_replace = os.replace
        late_bytes = b"last-second user edit\x00\xff"

        def edit_before_displacement(source, destination):
            if Path(source) == installed and Path(destination).name == "previous":
                (installed / "late-edit.bin").write_bytes(late_bytes)
            return real_replace(source, destination)

        with mock.patch.object(sync.os, "replace", side_effect=edit_before_displacement):
            code, _, error = self.run_sync("--apply")
        self.assertEqual(code, 2)
        self.assertIn("publication boundary", error)
        self.assertEqual((installed / "late-edit.bin").read_bytes(), late_bytes)
        self.assertEqual((installed / "SKILL.md").read_text(), "Old body\n")
        metadata = json.loads(next(self.backups.glob("*/metadata.json")).read_text())
        item = metadata["skills"][0]
        self.assertEqual(item["recovery_state"], "rolled_back")
        self.assertTrue(Path(item["recovery_directory"]).is_dir())

    def test_edit_to_displaced_original_after_validation_survives_success(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Old body\n")
        real_replace = os.replace

        def edit_displaced_before_publication(source, destination):
            if Path(source).name == "candidate":
                displaced = next(self.destination.parent.glob(".methodology-recovery-*/previous"))
                (displaced / "late-original.txt").write_text("Written through the old directory\n")
            return real_replace(source, destination)

        with mock.patch.object(sync.os, "replace", side_effect=edit_displaced_before_publication):
            code, report, error = self.run_sync("--apply")
        self.assertEqual(code, 0, error)
        item = report["skills"][0]
        recovery = Path(item["recovery_directory"])
        self.assertEqual(item["recovery_state"], "original_retained")
        self.assertEqual((recovery / "previous/late-original.txt").read_text(), "Written through the old directory\n")
        self.assertNotIn(self.destination, recovery.parents)
        self.assertEqual(sync.tree_manifest(installed), sync.tree_manifest(self.source / "review-loop"))

    def test_failed_publication_validation_preserves_changed_target(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Old body\n")
        original = sync.tree_manifest(installed)
        real_replace = os.replace

        def edit_published_target(source, destination):
            result = real_replace(source, destination)
            if Path(source).name == "candidate":
                (installed / "published-edit.bin").write_bytes(b"new user bytes\xff")
            return result

        with mock.patch.object(sync.os, "replace", side_effect=edit_published_target):
            code, _, error = self.run_sync("--apply")
        self.assertEqual(code, 2)
        self.assertIn("Installed bytes do not match", error)
        self.assertEqual(sync.tree_manifest(installed), original)
        metadata = json.loads(next(self.backups.glob("*/metadata.json")).read_text())
        recovery = Path(metadata["skills"][0]["recovery_directory"])
        self.assertEqual((recovery / "unpublished/published-edit.bin").read_bytes(), b"new user bytes\xff")

    def test_rollback_restore_failure_keeps_both_original_and_changed_target(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Old body\n")
        original = sync.tree_manifest(installed)
        real_replace = os.replace

        def edit_then_fail_restore(source, destination):
            if Path(source).name == "previous":
                raise OSError("injected restore failure")
            result = real_replace(source, destination)
            if Path(source).name == "candidate":
                (installed / "published-edit.txt").write_text("Keep both versions\n")
            return result

        with mock.patch.object(sync.os, "replace", side_effect=edit_then_fail_restore):
            code, _, error = self.run_sync("--apply")
        self.assertEqual(code, 2)
        self.assertIn("injected restore failure", error)
        metadata = json.loads(next(self.backups.glob("*/metadata.json")).read_text())
        item = metadata["skills"][0]
        recovery = Path(item["recovery_directory"])
        self.assertEqual(item["recovery_state"], "rollback_incomplete")
        self.assertEqual(sync.tree_manifest(recovery / "previous"), original)
        self.assertEqual((recovery / "unpublished/published-edit.txt").read_text(), "Keep both versions\n")

    def test_failed_target_preservation_leaves_live_edit_and_durable_original(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Old body\n")
        original = sync.tree_manifest(installed)
        real_replace = os.replace

        def edit_then_fail_preservation(source, destination):
            if Path(destination).name == "unpublished":
                raise OSError("injected preservation failure")
            result = real_replace(source, destination)
            if Path(source).name == "candidate":
                (installed / "live-edit.txt").write_text("Preserve me live\n")
            return result

        with mock.patch.object(sync.os, "replace", side_effect=edit_then_fail_preservation):
            code, _, error = self.run_sync("--apply")
        self.assertEqual(code, 2)
        self.assertIn("injected preservation failure", error)
        self.assertEqual((installed / "live-edit.txt").read_text(), "Preserve me live\n")
        metadata = json.loads(next(self.backups.glob("*/metadata.json")).read_text())
        recovery = Path(metadata["skills"][0]["recovery_directory"])
        self.assertEqual(sync.tree_manifest(recovery / "previous"), original)

    def test_custom_backup_location_does_not_receive_original_rename(self):
        installed = self.install()
        (installed / "SKILL.md").write_text("Old body\n")
        custom_backup = self.root / "separate-backup-location"
        real_replace = os.replace

        def refuse_cross_location_move(source, destination):
            if Path(source) == installed and custom_backup in Path(destination).parents:
                raise OSError("simulated cross-device rename")
            return real_replace(source, destination)

        with mock.patch.object(sync.os, "replace", side_effect=refuse_cross_location_move):
            code, report, error = self.run_sync("--apply", "--backup-root", str(custom_backup))
        self.assertEqual(code, 0, error)
        self.assertIn(custom_backup, Path(report["backup"]).parents)
        recovery = Path(report["skills"][0]["recovery_directory"])
        self.assertEqual(recovery.parent, self.destination.parent)
        self.assertEqual((recovery / "previous/SKILL.md").read_text(), "Old body\n")

    def test_in_sync_apply_creates_no_backup(self):
        self.install()
        before = sync.tree_manifest(self.root)
        code, report, error = self.run_sync("--apply")
        self.assertEqual(code, 0, error)
        self.assertIsNone(report["backup"])
        self.assertEqual(sync.tree_manifest(self.root), before)


if __name__ == "__main__":
    unittest.main()
