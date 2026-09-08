"""Mutation tests for the review-loop quality/safety contract."""

import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

import check_review_loop_skill_contract as contract  # noqa: E402


class ReviewLoopSkillContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        root = contract.REPO_ROOT
        cls.skill = (root / contract.SKILL_REL).read_text(encoding="utf-8")
        cls.command = (root / contract.COMMAND_REL).read_text(encoding="utf-8")
        cls.generator = (root / contract.GENERATOR_REL).read_text(encoding="utf-8")
        cls.pipeline = (root / contract.PIPELINE_REL).read_text(encoding="utf-8")
        cls.placement_references = {
            name: (root / path).read_text(encoding="utf-8")
            for name, path in contract.PLACEMENT_REFERENCES.items()
        }

    def missing(
        self, *, skill=None, command=None, generator=None, pipeline=None,
        placement_references=None,
    ) -> list[str]:
        return contract.validate_texts(
            self.skill if skill is None else skill,
            self.generator if generator is None else generator,
            self.pipeline if pipeline is None else pipeline,
            self.command if command is None else command,
            self.placement_references if placement_references is None
            else placement_references,
        )

    def assert_skill_mutation_fails(self, needle: str, family: str) -> None:
        mutated = self.skill.replace(needle, "REMOVED_BY_MUTATION")
        self.assertTrue(mutated != self.skill, f"mutation needle absent: {needle}")
        self.assertIn(family, self.missing(skill=mutated))

    def assert_command_mutation_fails(self, needle: str, family: str) -> None:
        mutated = self.command.replace(needle, "REMOVED_BY_MUTATION")
        self.assertNotEqual(mutated, self.command, f"mutation needle absent: {needle}")
        self.assertIn(family, self.missing(command=mutated))

    def mutate_skill_fence(self, marker: str, needle: str, replacement: str) -> str:
        start = self.skill.index(marker)
        end = self.skill.index("\n   ```", start)
        block = self.skill[start:end]
        mutated_block = block.replace(needle, replacement, 1)
        self.assertNotEqual(mutated_block, block, f"mutation needle absent: {needle}")
        return self.skill[:start] + mutated_block + self.skill[end:]

    def test_committed_contract_passes(self):
        self.assertEqual(self.missing(), [])

    def test_freshness_is_fail_closed(self):
        self.assert_skill_mutation_fails("## Skill Freshness", "freshness")

    def test_commented_freshness_is_fail_closed(self):
        start = self.skill.index("## Skill Freshness")
        end = self.skill.index("## Model And Tool Boundary")
        mutated = (
            self.skill[:start]
            + "<!--\n"
            + self.skill[start:end]
            + "-->\n"
            + self.skill[end:]
        )
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_unterminated_html_comment_is_fail_closed(self):
        start = self.skill.index("## Reviewer Fanout")
        mutated = self.skill[:start] + "<!--\n" + self.skill[start:]
        missing = self.missing(skill=mutated)
        self.assertIn("markdown_structure", missing)
        self.assertIn("reviewer_lenses", missing)

    def test_commonmark_commented_freshness_is_fail_closed(self):
        start = self.skill.index("## Skill Freshness")
        end = self.skill.index("## Model And Tool Boundary")
        mutated = (
            self.skill[:start]
            + "[//]: # (## Skill Freshness SKILL_FRESHNESS_CHECK.md origin/main)\n\n"
            + self.skill[end:]
        )
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_multiline_reference_definition_cannot_supply_freshness(self):
        start = self.skill.index("Before using this workflow")
        end = self.skill.index("## Model And Tool Boundary", start)
        positive = self.skill[start:end].rstrip()
        mutated = (
            self.skill[:start]
            + '[hidden-freshness]: <#> "title starts\n'
            + positive
            + '\n"\n\n'
            + self.skill[end:]
        )
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_next_line_reference_layouts_cannot_supply_freshness(self):
        start = self.skill.index("Before using this workflow")
        end = self.skill.index("## Model And Tool Boundary", start)
        positive = self.skill[start:end].rstrip()
        for prefix in (
            '[hidden]: <#>\n  "title starts\n',
            '[hidden]:\n  <#> "title starts\n',
        ):
            mutated = (
                self.skill[:start]
                + prefix
                + positive
                + '\n"\n\n'
                + self.skill[end:]
            )
            with self.subTest(prefix=prefix):
                self.assertIn("freshness", self.missing(skill=mutated))

    def test_negated_freshness_is_fail_closed(self):
        mutated = self.skill.replace(
            "Before using this workflow, inspect",
            "Before using this workflow, do not inspect",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("freshness", self.missing(skill=mutated))

    def test_authority_reads_are_fail_closed(self):
        self.assert_skill_mutation_fails(
            "**Mandatory authority read:**", "mandatory_authority_reads"
        )

    def test_negated_authority_reads_are_fail_closed(self):
        mutated = self.skill.replace(
            "judgment, read the current axiom memo",
            "judgment, do not read the current axiom memo",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("mandatory_authority_reads", self.missing(skill=mutated))

    def test_model_and_effort_are_fail_closed(self):
        self.assert_skill_mutation_fails("`gpt-6-astra`, `low`", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("**Astra xhigh**", "reviewer_model_and_effort")
        self.assert_skill_mutation_fails("its actual configuration stated", "reviewer_model_and_effort")

    def test_negated_model_and_effort_are_fail_closed(self):
        mutated = self.skill.replace(
            "use **Astra low**",
            "do not use **Astra low**",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_negated_configuration_clause_is_fail_closed(self):
        mutated = self.skill.replace(
            "If a requested", "Do not If a requested", 1
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_negated_owner_choice_clause_is_fail_closed(self):
        mutated = self.skill.replace(
            "Respect a later explicit owner", "Do not Respect a later explicit owner", 1
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_soft_wrapped_negations_cannot_supply_affirmative_clauses(self):
        for clause in ["If a requested", "Respect a later explicit owner"]:
            for prefix in ["Do not\n ", "Never\n  ", "Do not\n"]:
                with self.subTest(clause=clause, prefix=prefix):
                    mutated = self.skill.replace(clause, prefix + clause, 1)
                    self.assertNotEqual(mutated, self.skill)
                    self.assertIn("reviewer_model_and_effort", self.missing(skill=mutated))

    def test_each_reviewer_lens_is_fail_closed(self):
        for reviewer in (
            "CodeRunnerReviewer",
            "PhysicsClaimReviewer",
            "ProofObligationReviewer",
            "ImportSupportReviewer",
            "NatureRetentionReviewer",
            "NoGoDisciplineReviewer",
            "LabelingConventionReviewer",
            "RepoGovernanceReviewer",
            "MethodologySkillReviewer",
        ):
            with self.subTest(reviewer=reviewer):
                self.assert_skill_mutation_fails(reviewer, "reviewer_lenses")

    def test_negated_reviewer_sections_are_fail_closed(self):
        reviewers = (
            "CodeRunnerReviewer",
            "PhysicsClaimReviewer",
            "ProofObligationReviewer",
            "ImportSupportReviewer",
            "NatureRetentionReviewer",
            "NoGoDisciplineReviewer",
            "LabelingConventionReviewer",
            "RepoGovernanceReviewer",
        )
        for index, reviewer in enumerate(reviewers):
            start_marker = f"\n- `{reviewer}`"
            start = self.skill.index(start_marker)
            if index + 1 < len(reviewers):
                end = self.skill.index(f"\n- `{reviewers[index + 1]}`", start + 1)
            else:
                end = self.skill.index("\n### Optional Reviewer", start + 1)
            mutated = (
                self.skill[:start]
                + f"\n- Do not run `{reviewer}`.\n"
                + self.skill[end:]
            )
            with self.subTest(reviewer=reviewer):
                self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        methodology_start = self.skill.index(
            "Run `MethodologySkillReviewer` when files under"
        )
        methodology_end = self.skill.index("\n\n## Reviewer Prompt", methodology_start)
        mutated = (
            self.skill[:methodology_start]
            + "Do not run `MethodologySkillReviewer` when methodology files change."
            + self.skill[methodology_end:]
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_fenced_reviewer_sections_are_fail_closed(self):
        start = self.skill.index("### Required Reviewers")
        end = self.skill.index("## Reviewer Prompt", start)
        mutated = (
            self.skill[:start]
            + "```text\n"
            + self.skill[start:end]
            + "```\n\n"
            + self.skill[end:]
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_unterminated_fenced_reviewer_sections_are_fail_closed(self):
        start = self.skill.index("### Required Reviewers")
        mutated = self.skill[:start] + "```text\n" + self.skill[start:]
        missing = self.missing(skill=mutated)
        self.assertIn("markdown_structure", missing)
        self.assertIn("reviewer_lenses", missing)

    def test_indented_code_cannot_supply_reviewer_sections(self):
        start = self.skill.index("### Required Reviewers")
        end = self.skill.index("## Reviewer Prompt", start)
        indented = "\n".join(
            "    " + line for line in self.skill[start:end].splitlines()
        )
        mutated = self.skill[:start] + indented + "\n" + self.skill[end:]
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_optional_reviewer_heading_is_fail_closed(self):
        mutated = self.skill.replace(
            "### Optional Reviewer", "### Historical Example", 1
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_hidden_affirmative_reviewer_bodies_are_fail_closed(self):
        needles = dict(contract.REVIEWER_BODY_RULES)
        for index, (reviewer, pattern) in enumerate(needles.items()):
            match = re.search(
                pattern,
                self.skill,
                re.IGNORECASE | re.DOTALL | re.MULTILINE,
            )
            self.assertIsNotNone(match, reviewer)
            assert match is not None
            positive = match.group(0)
            replacement = (
                "  Do not run this reviewer.\n\n"
                f'[hidden-reviewer-{index}]: <#> "title starts\n'
                + positive
                + '\n"'
            )
            mutated = self.skill[: match.start()] + replacement + self.skill[match.end() :]
            with self.subTest(reviewer=reviewer):
                self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        match = re.search(
            contract.METHODOLOGY_BODY_RULE,
            self.skill,
            re.IGNORECASE | re.DOTALL | re.MULTILINE,
        )
        self.assertIsNotNone(match)
        assert match is not None
        positive = match.group(0)
        replacement = (
            "Do not run this reviewer.\n\n"
            '[hidden-methodology]: <#> "title starts\n'
            + positive
            + '\n"'
        )
        mutated = self.skill[: match.start()] + replacement + self.skill[match.end() :]
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_named_reviewer_negations_are_fail_closed(self):
        for reviewer in contract.REVIEWER_BODY_RULES:
            label = f"- `{reviewer}`\n"
            mutated = self.skill.replace(
                label,
                label + f"  Do not run `{reviewer}`.\n",
                1,
            )
            with self.subTest(reviewer=reviewer):
                self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        anchor = "Run `MethodologySkillReviewer` when files under"
        mutated = self.skill.replace(
            anchor,
            "Do not run `MethodologySkillReviewer`.\n\n" + anchor,
            1,
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_active_reviewer_contradictions_are_fail_closed(self):
        variants = (
            lambda reviewer: f"  However, do not run `{reviewer}`.\n",
            lambda reviewer: f"  `{reviewer}` must not run.\n",
            lambda reviewer: f"  - Skip `{reviewer}`.\n",
            lambda reviewer: f"  `{reviewer}` is not required.\n",
        )
        for reviewer, pattern in contract.REVIEWER_BODY_RULES.items():
            match = re.search(
                pattern,
                self.skill,
                re.IGNORECASE | re.DOTALL | re.MULTILINE,
            )
            self.assertIsNotNone(match, reviewer)
            assert match is not None
            for variant in variants:
                mutated = (
                    self.skill[: match.end()]
                    + "\n"
                    + variant(reviewer)
                    + self.skill[match.end() :]
                )
                with self.subTest(reviewer=reviewer, variant=variant(reviewer)):
                    self.assertIn("reviewer_lenses", self.missing(skill=mutated))

        match = re.search(
            contract.METHODOLOGY_BODY_RULE,
            self.skill,
            re.IGNORECASE | re.DOTALL | re.MULTILINE,
        )
        self.assertIsNotNone(match)
        assert match is not None
        mutated = (
            self.skill[: match.end()]
            + "\nHowever, do not run `MethodologySkillReviewer`."
            + self.skill[match.end() :]
        )
        self.assertIn("reviewer_lenses", self.missing(skill=mutated))

    def test_independent_math_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "independent route", "independent_math_and_mutations"
        )

    def test_proof_import_governance_is_fail_closed(self):
        self.assert_skill_mutation_fails("EQUIVALENT-GAP", "proof_import_governance")

    def test_no_go_is_fail_closed(self):
        self.assert_skill_mutation_fails("N1-N8", "no_go_discipline")

    def test_audit_boundary_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "## Audit-System Compatibility Gate", "audit_compatibility_boundary"
        )

    def test_same_session_confirmation_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "same reviewer thread/session", "same_session_confirmation"
        )

    def test_train_scheduler_is_fail_closed(self):
        for needle in (
            "trains of at most eight",
            "depart with the useful ready batch as soon as the coordinator is available",
            "do not wait for an arbitrary collection deadline or an unfinished reviewer",
            "open the next empty",
            "one-component trains",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "landing_train_scheduler")

    def test_coherent_unit_obligations_cannot_be_hidden_or_removed(self):
        start = self.skill.index("## Coherent review units and validation placement")
        end = self.skill.index("## Default Entry", start)
        section = self.skill[start:end]
        expected = {
            "coherent_unit_coverage",
            "unit_provenance_and_recheck",
            "shared_validation_placement",
        }
        for wrapper in ("<!--\n{}\n-->\n", "```text\n{}\n```\n"):
            mutated = self.skill[:start] + wrapper.format(section) + self.skill[end:]
            with self.subTest(wrapper=wrapper):
                self.assertTrue(expected <= set(self.missing(skill=mutated)))

    def test_unit_coverage_and_provenance_fail_closed(self):
        cases = (
            ("Run every applicable reviewer lens on the complete final unit",
             "Do not run every applicable reviewer lens on the complete final unit",
             "coherent_unit_coverage"),
            ("Unmapped content\nblocks unit confirmation.",
             "Unmapped content is acceptable.", "coherent_unit_coverage"),
            ("A changed PR head fails the provenance",
             "A changed PR head passes the provenance", "unit_provenance_and_recheck"),
            ("or semantic interaction reopens the affected conclusion",
             "or semantic interaction preserves the affected conclusion",
             "unit_provenance_and_recheck"),
            ("mark-ready is not PASS, and a still-draft PR cannot land.",
             "mark-ready is PASS, and a still-draft PR can land.", "unit_scope_and_close"),
            ("never delete its recovery branch for partial salvage.",
             "delete its recovery branch for partial salvage.", "unit_scope_and_close"),
        )
        for needle, replacement, family in cases:
            mutated = self.skill.replace(needle, replacement, 1)
            self.assertNotEqual(mutated, self.skill, needle)
            with self.subTest(needle=needle):
                self.assertIn(family, self.missing(skill=mutated))

    def test_shared_validation_identity_cannot_be_weakened(self):
        for needle in (
            "identical frozen base and candidate",
            "command/options, tool/runtime versions, declared inputs, and evidence",
            "accessible successful logs and their hashes",
            "already validated unit whose raw tree equals the whole integrated candidate",
            "changed base/tree/input, or changed validation scope invalidates reuse",
            "verify all non-generated bytes stayed identical",
            "again on each constituent or unit before enrollment",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "shared_validation_placement")

    def test_validation_placement_is_required_in_coupled_references(self):
        for name in contract.PLACEMENT_REFERENCES:
            for wrapper in ("REMOVED", "<!--\n{}\n-->", "```text\n{}\n```"):
                references = dict(self.placement_references)
                references[name] = wrapper.format(references[name])
                with self.subTest(name=name, wrapper=wrapper):
                    self.assertIn(f"shared_validation_reference_{name}",
                                  self.missing(placement_references=references))

    def test_command_unit_validation_is_fail_closed(self):
        for needle in (
            "complete constituent",
            "perform one full",
            "do not require duplicate per-PR or per-unit full runs",
            "collection wait",
            "Mark-ready is not PASS",
        ):
            with self.subTest(needle=needle):
                self.assert_command_mutation_fails(needle, "command_unit_validation")

    def _run_gate_fragment(self, marker: str, fail_at: int) -> tuple[int, list[str], str]:
        """Execute the actual documented shell with inert command substitutes.

        The substitutions only log calls and fail at a chosen call. No pipeline,
        audit, Git mutation, or external action runs in these behavioral tests.
        """
        scan = contract._markdown_scan(self.skill)
        blocks = [body for _, body in scan.fenced_blocks if marker in body]
        self.assertEqual(len(blocks), 1)
        with tempfile.TemporaryDirectory() as tmp:
            script = textwrap.dedent("""\
                gate_call() {
                  printf '%s\\n' "$*" >> calls
                  gate_count=$(wc -l < calls)
                  [ "$gate_count" -ne "$FAIL_AT" ] || return 7
                  if [ "$1" = git ] && [ "$2" = merge-base ]; then
                    printf '%s\\n' frozen-base
                  fi
                }
                bash() { gate_call bash "$@"; }
                python3() { gate_call python3 "$@"; }
                git() { gate_call git "$@"; }
                """)
            script += f"FAIL_AT={fail_at}\n" + blocks[0] + "\necho GATE_COMPLETED\n"
            proc = subprocess.run(["bash", "-c", script], cwd=tmp, text=True,
                                  capture_output=True, check=False)
            calls = (Path(tmp) / "calls").read_text().splitlines()
            return proc.returncode, calls, proc.stdout

    def test_combined_validation_runs_each_gate_once_and_short_circuits_failure(self):
        marker = "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate"
        status, calls, stdout = self._run_gate_fragment(marker, 0)
        self.assertEqual(status, 0)
        self.assertEqual(len(calls), 3)
        self.assertIn("GATE_COMPLETED", stdout)
        for fail_at in (1, 2, 3):
            with self.subTest(fail_at=fail_at):
                status, calls, stdout = self._run_gate_fragment(marker, fail_at)
                self.assertNotEqual(status, 0)
                self.assertEqual(len(calls), fail_at)
                self.assertNotIn("GATE_COMPLETED", stdout)

    def test_combined_diff_checks_fail_closed_at_every_command(self):
        marker = "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate"
        status, calls, stdout = self._run_gate_fragment(marker, 0)
        self.assertEqual(status, 0)
        self.assertEqual(len(calls), 4)
        self.assertIn("GATE_COMPLETED", stdout)
        for fail_at in (1, 2, 3, 4):
            with self.subTest(fail_at=fail_at):
                status, calls, stdout = self._run_gate_fragment(marker, fail_at)
                self.assertNotEqual(status, 0)
                self.assertEqual(len(calls), fail_at)
                self.assertNotIn("GATE_COMPLETED", stdout)

    def test_train_combined_gate_is_fail_closed(self):
        for needle in (
            "combined gate is mechanical",
            (
                "python3 docs/audit/scripts/check_changed_audit_evidence.py "
                "--base origin/main"
            ),
            'git diff --check "$review_base"..HEAD',
            "git diff --cached --check",
            'if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then',
            'if [ "$(git rev-parse \'HEAD^{tree}\')" != "$VALIDATED_TREE" ]; then',
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(
                    needle, "landing_train_combined_gate"
                )

    def test_train_combined_commands_are_bound_to_their_active_blocks(self):
        cases = (
            (
                "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate",
                "bash docs/audit/scripts/run_pipeline.sh",
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate",
                "python3 docs/audit/scripts/audit_lint.py --strict",
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate",
                "python3 docs/audit/scripts/check_changed_audit_evidence.py "
                "--base origin/main",
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate",
                'git diff --check "$review_base"..HEAD',
                "true # removed",
            ),
            (
                "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate",
                "git diff --check \\\n",
                "true # removed\n",
            ),
            (
                "TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate",
                "git diff --cached --check",
                "true # removed",
            ),
        )
        for marker, command, replacement in cases:
            mutated = self.mutate_skill_fence(marker, command, replacement)
            with self.subTest(command=command):
                self.assertIn(
                    "landing_train_combined_gate", self.missing(skill=mutated)
                )

    def test_train_validated_guards_must_stay_active_at_push_depth(self):
        for line in (
            '     if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then',
            '     if [ "$(git rev-parse \'HEAD^{tree}\')" != "$VALIDATED_TREE" ]; then',
        ):
            mutated = self.skill.replace(
                line,
                "     if false; then\n" + line + "\n     fi",
                1,
            )
            self.assertNotEqual(mutated, self.skill)
            with self.subTest(line=line):
                self.assertIn(
                    "landing_train_combined_gate", self.missing(skill=mutated)
                )

    def test_train_head_guard_is_fail_closed(self):
        for needle in (
            "PR_NUMBERS=(<pr-a-number> <pr-b-number> ...)",
            "PR_HEADS=(<pr-a-frozen-head-sha> <pr-b-frozen-head-sha> ...)",
            "verify_frozen_pr_heads()",
            "PR head moved; dissolve the train without pushing",
            "post-push head check",
            "force-with-lease=refs/heads/<head>:<frozen-head-sha>",
        ):
            with self.subTest(needle=needle):
                self.assert_skill_mutation_fails(needle, "landing_train_head_guard")

    def test_train_head_checks_must_bracket_push_and_close(self):
        for line in (
            "     if ! verify_frozen_pr_heads; then",
            '     if verify_frozen_pr_head "$pr" "$expected"; then',
        ):
            mutated = self.skill.replace(
                line,
                "     if false; then\n" + line + "\n     fi",
                1,
            )
            self.assertNotEqual(mutated, self.skill)
            with self.subTest(line=line):
                self.assertIn("landing_train_head_guard", self.missing(skill=mutated))

    def test_train_head_fetch_compare_and_failure_are_structurally_bound(self):
        marker = "VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>"
        mutations = (
            (
                'if ! git fetch -q origin "+pull/$pr/head:$live_ref"; then',
                "if ! true; then",
            ),
            ('[ "$actual" = "$expected" ]', '[ "$actual" != "$expected" ]'),
            (
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT,
                contract.TRAIN_PRE_PUSH_HEAD_CONTEXT.replace(
                    "       exit 1", "       true # nonfatal", 1
                ),
            ),
            (
                'if verify_frozen_pr_head "$pr" "$expected"; then',
                "if true; then",
            ),
        )
        for needle, replacement in mutations:
            mutated = self.mutate_skill_fence(marker, needle, replacement)
            with self.subTest(needle=needle):
                self.assertIn("landing_train_head_guard", self.missing(skill=mutated))

    def test_command_train_contract_is_fail_closed(self):
        for needle in (
            "continuously collected trains of at most eight",
            "double-buffered landing train",
            "next empty train",
            "immediately before push",
            "immediately before its own close",
            "--force-with-lease=<ref>:<frozen-head-sha>",
        ):
            with self.subTest(needle=needle):
                self.assert_command_mutation_fails(needle, "command_landing_train")

    def test_live_surface_routing_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "relevant sharded rows under `docs/audit/data/ledger/`",
            "live_surface_routing",
        )
        mutated = self.skill + "\nUse docs/publication/ci3_z3 as a live surface.\n"
        self.assertIn("live_surface_routing", self.missing(skill=mutated))

    def test_pipeline_evidence_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            "check_changed_audit_evidence.py", "pipeline_strict_and_evidence"
        )

    def test_manifest_landing_is_fail_closed(self):
        self.assert_skill_mutation_fails("before EVERY push attempt", "manifest_landing")

    def test_disk_worktree_guards_are_fail_closed(self):
        self.assert_skill_mutation_fails("5242880", "disk_and_worktree_guards")

    def test_landing_containment_is_fail_closed(self):
        self.assert_skill_mutation_fails(
            'if ! git merge-base --is-ancestor "$landed" origin/main; then',
            "fail_closed_landing",
        )

    def test_inert_landing_containment_tokens_are_fail_closed(self):
        mutated = self.skill.replace(
            'if ! git merge-base --is-ancestor "$landed" origin/main; then',
            'if false; then # git merge-base --is-ancestor "$landed" origin/main',
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_outer_conditional_containment_is_fail_closed(self):
        block = (
            '   if ! git merge-base --is-ancestor "$landed" origin/main; then\n'
            '     echo "FAILED: $landed not contained in origin/main" >&2\n'
            "     exit 1\n"
            "   fi"
        )
        mutated = self.skill.replace(
            block,
            "   if false; then\n" + block + "\n   fi",
            1,
        )
        self.assertNotEqual(mutated, self.skill)
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_whole_containment_context_outer_conditional_is_fail_closed(self):
        start = self.skill.index(contract.CONTAINMENT_CONTEXT)
        end = self.skill.index('   echo "LANDED $landed"', start)
        mutated = (
            self.skill[:start]
            + "   if false; then\n"
            + self.skill[start:end]
            + "   fi\n"
            + self.skill[end:]
        )
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_containment_context_in_heredoc_is_fail_closed(self):
        mutated = self.skill.replace(
            contract.CONTAINMENT_CONTEXT,
            "   cat <<'HIDDEN_CONTAINMENT'\n"
            + contract.CONTAINMENT_CONTEXT
            + "\nHIDDEN_CONTAINMENT",
            1,
        )
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_containment_context_in_second_heredoc_is_fail_closed(self):
        for opener in (
            "   cat <<'FIRST' <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' \\\n     <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' |\n     cat <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' &&\n     cat <<'HIDDEN-CONTAINMENT'\n",
            "   cat <<'FIRST' ||\n     cat <<'HIDDEN-CONTAINMENT'\n",
        ):
            mutated = self.skill.replace(
                contract.CONTAINMENT_CONTEXT,
                opener
                + "FIRST\n"
                + contract.CONTAINMENT_CONTEXT
                + "\nHIDDEN-CONTAINMENT",
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_containment_context_in_general_substitutions_is_fail_closed(self):
        for opener, closer in (
            ("   hidden=$( :\n", "\n   ) || true"),
            ("   hidden=$\\\n( :\n", "\n) || true"),
            ("   hidden=<( :\n", "\n   )"),
            ("   hidden=` :\n", "\n   ` || true"),
            ("   ( :\n", "\n   ) || true"),
        ):
            mutated = self.skill.replace(
                contract.CONTAINMENT_CONTEXT,
                opener + contract.CONTAINMENT_CONTEXT + closer,
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_unterminated_landing_shell_context_is_fail_closed(self):
        marker = '   echo "LANDED $landed"'
        mutated = self.skill.replace(marker, marker + "\n   hidden=$( :", 1)
        self.assertIn("fail_closed_landing", self.missing(skill=mutated))

    def test_generated_router_is_fail_closed(self):
        mutated = self.generator.replace("missing_authority_router_coverage", "removed")
        self.assertIn("generated_authority_router", self.missing(generator=mutated))

    def test_pipeline_registration_is_fail_closed(self):
        mutated = self.pipeline.replace("check_review_loop_skill_contract.py", "removed")
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_commented_pipeline_registration_is_fail_closed(self):
        mutated = self.pipeline.replace(
            "python3 docs/audit/scripts/check_review_loop_skill_contract.py",
            "# python3 docs/audit/scripts/check_review_loop_skill_contract.py",
            1,
        )
        self.assertNotEqual(mutated, self.pipeline)
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_conditional_pipeline_registration_is_fail_closed(self):
        command = "python3 docs/audit/scripts/check_review_loop_skill_contract.py"
        mutated = self.pipeline.replace(
            command,
            "if false; then\n" + command + "\nfi",
            1,
        )
        self.assertNotEqual(mutated, self.pipeline)
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_whole_pipeline_context_outer_conditional_is_fail_closed(self):
        start = self.pipeline.index(contract.PIPELINE_CONTRACT_CONTEXT)
        end = self.pipeline.index("\necho\n", start)
        mutated = (
            self.pipeline[:start]
            + "if false; then\n"
            + self.pipeline[start:end]
            + "\nfi\n"
            + self.pipeline[end:]
        )
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_pipeline_context_in_heredoc_is_fail_closed(self):
        mutated = self.pipeline.replace(
            contract.PIPELINE_CONTRACT_CONTEXT,
            "cat <<'HIDDEN_CONTRACT'\n"
            + contract.PIPELINE_CONTRACT_CONTEXT
            + "\nHIDDEN_CONTRACT",
            1,
        )
        self.assertIn("pipeline_contract_registration", self.missing(pipeline=mutated))

    def test_pipeline_context_in_general_heredocs_is_fail_closed(self):
        for delimiter in ("HIDDEN-CONTEXT", "1"):
            mutated = self.pipeline.replace(
                contract.PIPELINE_CONTRACT_CONTEXT,
                f"cat <<'{delimiter}'\n"
                + contract.PIPELINE_CONTRACT_CONTEXT
                + f"\n{delimiter}",
                1,
            )
            with self.subTest(delimiter=delimiter):
                self.assertIn(
                    "pipeline_contract_registration", self.missing(pipeline=mutated)
                )

    def test_pipeline_context_in_second_heredoc_is_fail_closed(self):
        for opener in (
            "cat <<'FIRST' <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' \\\n  <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' |\n  cat <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' &&\n  cat <<'HIDDEN-CONTRACT'\n",
            "cat <<'FIRST' ||\n  cat <<'HIDDEN-CONTRACT'\n",
        ):
            mutated = self.pipeline.replace(
                contract.PIPELINE_CONTRACT_CONTEXT,
                opener
                + "FIRST\n"
                + contract.PIPELINE_CONTRACT_CONTEXT
                + "\nHIDDEN-CONTRACT",
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn(
                    "pipeline_contract_registration", self.missing(pipeline=mutated)
                )

    def test_pipeline_context_in_command_substitutions_is_fail_closed(self):
        for opener, closer in (
            ("hidden=`\n", "`\n"),
            ("hidden=$(\n", ")\n"),
            ("hidden=$( :\n", ") || true\n"),
            ("hidden=$\\\n( :\n", ") || true\n"),
            ("hidden=>( :\n", ")\n"),
            ("( :\n", ") || true\n"),
        ):
            mutated = self.pipeline.replace(
                contract.PIPELINE_CONTRACT_CONTEXT,
                opener + contract.PIPELINE_CONTRACT_CONTEXT + "\n" + closer,
                1,
            )
            with self.subTest(opener=opener):
                self.assertIn(
                    "pipeline_contract_registration", self.missing(pipeline=mutated)
                )

    def test_unterminated_pipeline_shell_context_is_fail_closed(self):
        mutated = self.pipeline + "\nhidden=$( :\n"
        self.assertIn(
            "pipeline_contract_registration", self.missing(pipeline=mutated)
        )


@unittest.skipUnless(shutil.which("git") and shutil.which("bash"), "requires Git and Bash")
class ReviewLoopLandingSequenceTest(unittest.TestCase):
    """Run the documented landing shell against three real local Git branches.

    Each branch adds a separate note and changes the same one-line manifest.
    Thus one invocation must handle two successive manifest conflicts. Remote
    means a temporary local bare repository; these tests never use the network.
    """

    def run_sequence(self, fault=None, mutate_loop=False):
        env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                   GIT_AUTHOR_NAME="Fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
                   GIT_COMMITTER_NAME="Fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid",
                   GIT_AUTHOR_DATE="2026-09-07T01:00:00Z",
                   GIT_COMMITTER_DATE="2026-09-07T01:00:00Z")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            remote, work = root / "remote.git", root / "work"
            remote.mkdir()
            work.mkdir()

            def git(cwd, *args):
                proc = subprocess.run(["git", *args], cwd=cwd, env=env, text=True,
                                      capture_output=True, check=True)
                return proc.stdout.strip()

            def write(path, content):
                dest = work / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content)

            def commit(message):
                git(work, "add", ".")
                git(work, "-c", "commit.gpgsign=false", "commit", "-qm", message)
                return git(work, "rev-parse", "HEAD")

            manifest = "docs/audit/data/citation_graph_manifest.json"
            git(remote, "init", "--bare", "-q")
            git(work, "init", "-q", "-b", "main")
            git(work, "config", "commit.gpgsign", "false")
            write("source.txt", "base\n")
            write("notes/base.md", "base\n")
            write(manifest, '["base"]\n')
            write("docs/audit/scripts/run_citation_graph_build.py", "pass\n")
            write("docs/audit/scripts/write_citation_graph_manifest.py",
                  "from pathlib import Path\nimport json\n"
                  f"Path({manifest!r}).write_text(json.dumps(sorted("
                  "p.stem for p in Path('notes').glob('*.md'))) + '\\n')\n")
            base = commit("base")
            git(work, "remote", "add", "origin", str(remote))
            git(work, "push", "-q", "origin", "HEAD:main")
            heads = []
            for number, letter in enumerate("abc", 1):
                git(work, "checkout", "-q", "--detach", base)
                write(f"notes/{letter}.md", letter + "\n")
                write(manifest, json.dumps(sorted([letter, "base"])) + "\n")
                if fault == "later-source-conflict" and letter in "ac":
                    write("source.txt", letter + "\n")
                head = commit("unit " + letter)
                heads.append(head)
                git(work, "push", "-q", "origin", f"{head}:refs/pull/{number}/head")
            git(work, "checkout", "-q", "--detach", base)
            for letter in "abc":
                write(f"notes/{letter}.md", letter + "\n")
            write(manifest, json.dumps(["a", "b", "base", "c"]) + "\n")
            commit("validated candidate")
            tree = git(work, "rev-parse", "HEAD^{tree}")
            skill = (contract.REPO_ROOT / contract.SKILL_REL).read_text()
            blocks = contract._markdown_scan(skill).fenced_blocks
            code = next(body for _, body in blocks if "VALIDATED_BASE=<" in body)
            replacements = {
                "VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>": f"VALIDATED_BASE={base}",
                "VALIDATED_TREE=<combined-candidate-tree-sha>": f"VALIDATED_TREE={tree}",
                "COMMITS=(<pr-a-oldest> ... <pr-a-newest> <pr-b-oldest> ...)": "COMMITS=(" + " ".join(heads) + ")",
                "PR_NUMBERS=(<pr-a-number> <pr-b-number> ...)": "PR_NUMBERS=(1 2 3)",
                "PR_HEADS=(<pr-a-frozen-head-sha> <pr-b-frozen-head-sha> ...)": "PR_HEADS=(" + " ".join(heads) + ")",
            }
            for old, new in replacements.items():
                self.assertIn(old, code)
                code = code.replace(old, new)
            if mutate_loop:
                # A single conditional repair recreates the reviewed defect:
                # the second conflict reaches the final tree guard unresolved.
                old = 'while [ -z "$cherry_pick_complete" ]; do'
                self.assertIn(old, code)
                start = code.index(old)
                end = code.index("\n     done", start)
                code = (code[:start] + code[start:end].replace(old, 'if [ -z "$cherry_pick_complete" ]; then', 1)
                        + "\n     fi" + code[end + len("\n     done"):])
            prelude = f"CALL_LOG={shlex.quote(str(root / 'git-calls.log'))}\n"
            prelude += "sleep() { :; }\ngit() {\n  printf '%s\\n' \"$*\" >> \"$CALL_LOG\"\n"
            injections = {
                "inspect-fails": '[ "$*" != "diff --name-only --diff-filter=U" ] || return 7',
                "head-lookup-fails": '[ "$*" != "rev-parse --verify CHERRY_PICK_HEAD" ] || return 7',
                "stage-fails": f'[ "$*" != "add {manifest}" ] || return 7',
                # Simulate a staging tool reporting success without resolving
                # the index: real --continue must fail at the same commit.
                "no-progress": f'[ "$*" != "add {manifest}" ] || return 0',
                "continue-fails": '[ "$*" != "cherry-pick --continue" ] || return 7',
            }
            if fault in injections:
                prelude += "  " + injections[fault] + "\n"
            prelude += '  command git "$@"\n}\n'
            if fault == "generator-fails":
                prelude += "python3() { return 9; }\n"
            proc = subprocess.run(["bash", "-c", prelude + code], cwd=work, env=env,
                                  text=True, capture_output=True, timeout=20)
            calls = (root / "git-calls.log").read_text().splitlines()
            return {
                "exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                "pushes": sum(c.startswith("push ") for c in calls),
                "starts": sum(c.startswith("cherry-pick ") and not c.startswith("cherry-pick --") for c in calls),
                "continues": calls.count("cherry-pick --continue"),
                "remote_changed": git(remote, "rev-parse", "refs/heads/main") != base,
                "remote_tree": git(remote, "rev-parse", "refs/heads/main^{tree}"),
                "expected_tree": tree,
            }

    def test_three_units_resolve_two_manifest_conflicts_without_replay(self):
        result = self.run_sequence()
        self.assertEqual(result["exit"], 0, result)
        self.assertEqual(result["starts"], 1, result)
        self.assertEqual(result["continues"], 2, result)
        self.assertEqual(result["pushes"], 1, result)
        self.assertEqual(result["remote_tree"], result["expected_tree"], result)
        self.assertEqual(result["stdout"].count("CLOSE_READY"), 3, result)

    def test_single_repair_mutation_cannot_land_three_units(self):
        result = self.run_sequence(mutate_loop=True)
        self.assertNotEqual(result["exit"], 0, result)
        self.assertEqual(result["pushes"], 0, result)
        self.assertFalse(result["remote_changed"], result)

    def test_later_source_conflict_is_not_treated_as_another_manifest(self):
        result = self.run_sequence("later-source-conflict")
        self.assertNotEqual(result["exit"], 0, result)
        self.assertEqual(result["starts"], 1, result)
        self.assertEqual(result["continues"], 1, result)
        self.assertEqual(result["pushes"], 0, result)
        self.assertFalse(result["remote_changed"], result)
        self.assertIn("source conflict or sequencer failure", result["stderr"])

    def test_manifest_sequence_tool_failures_and_no_progress_fail_closed(self):
        for fault in ("inspect-fails", "head-lookup-fails", "stage-fails", "no-progress",
                      "continue-fails", "generator-fails"):
            with self.subTest(fault=fault):
                result = self.run_sequence(fault)
                self.assertNotEqual(result["exit"], 0, result)
                self.assertEqual(result["starts"], 1, result)
                self.assertEqual(result["pushes"], 0, result)
                self.assertFalse(result["remote_changed"], result)
                if fault == "no-progress":
                    self.assertIn("no sequencer progress", result["stderr"])


if __name__ == "__main__":
    unittest.main()
