#!/usr/bin/env python3
"""Fail closed if review-loop loses a quality, safety, or landing invariant."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_REL = "docs/ai_methodology/skills/review-loop/SKILL.md"
COMMAND_REL = ".claude/commands/review-loop.md"
GENERATOR_REL = "docs/audit/scripts/generate_skill_axiom_baselines.py"
PIPELINE_REL = "docs/audit/scripts/run_pipeline.sh"
FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
REFERENCE_START_RE = re.compile(r"^ {0,3}\[[^\]\n]+\]:")
PIPELINE_CONTRACT_LINE = (
    "python3 docs/audit/scripts/check_review_loop_skill_contract.py"
)
CONTAINMENT_CONTEXT = """   if ! git fetch -q origin \\
          +refs/heads/main:refs/remotes/origin/main; then
     echo "FAILED: could not refresh origin/main for containment verification" >&2
     exit 1
   fi
   if ! git merge-base --is-ancestor "$landed" origin/main; then"""
PIPELINE_CONTRACT_CONTEXT = """echo "==> 18b/18 check_review_loop_skill_contract.py (review quality/safety guard)"
python3 docs/audit/scripts/check_review_loop_skill_contract.py

if [[ "${PIPELINE_MODE}" == "full" ]]; then"""
TRAIN_VALIDATION_CONTEXT = """   TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate
   bash docs/audit/scripts/run_pipeline.sh
   python3 docs/audit/scripts/audit_lint.py --strict
   python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main"""
TRAIN_CLEAN_CONTEXT = """   TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate
   review_base=$(git merge-base origin/main HEAD)
   git diff --check "$review_base"..HEAD
   git diff --check
   git diff --cached --check"""
TRAIN_HEAD_FUNCTION_CONTEXT = """   verify_frozen_pr_head() {
     local pr="$1" expected="$2" live_ref actual
     case "$pr" in
       ''|*[!0-9]*) return 1 ;;
     esac
     live_ref="refs/tmp/review-loop-train-pr-$pr"
     if ! git fetch -q origin "+pull/$pr/head:$live_ref"; then
       return 1
     fi
     actual="$(git rev-parse --verify "$live_ref")" || return 1
     [ "$actual" = "$expected" ]
   }"""
TRAIN_PRE_PUSH_HEAD_CONTEXT = """     if ! verify_frozen_pr_heads; then
       echo "FAILED: PR head moved; dissolve the train without pushing" >&2
       exit 1
     fi
     if git push -q origin HEAD:main; then"""
TRAIN_POST_PUSH_HEAD_CONTEXT = """     if verify_frozen_pr_head "$pr" "$expected"; then
       printf 'CLOSE_READY %s %s\\n' "$pr" "$expected"
     else
       echo "LEAVE_OPEN $pr: PR head moved after landing" >&2
     fi"""

REVIEWER_BODY_RULES: dict[str, str] = {
    "CodeRunnerReviewer": r"^\s+Review changed Python/scripts/log-producing code\.",
    "PhysicsClaimReviewer": (
        r"^\s+Attack theorem notes, claims tables, publication surfaces, and prose\."
    ),
    "ProofObligationReviewer": (
        r"^\s+Trigger when changed content claims a theorem, proof, derivation, "
        r"reduction,"
    ),
    "ImportSupportReviewer": (
        r"^\s+Inventory every measured, fitted, literature, PDG, cosmological,"
    ),
    "NatureRetentionReviewer": r"^\s+Apply the hostile external-review bar\.",
    "NoGoDisciplineReviewer": (
        r"^\s+Scrutinize negative claims with the same rigor as positive ones\."
    ),
    "LabelingConventionReviewer": (
        r"^\s+Detect labeling/naming/convention content masquerading as a bounded"
    ),
    "RepoGovernanceReviewer": r"^\s+Check placement and authority surfaces\.",
}
METHODOLOGY_BODY_RULE = (
    r"^Run `MethodologySkillReviewer` when files under "
    r"`docs/ai_methodology/skills/`,\s+`docs/ai_methodology/`, or "
    r"`\.claude/commands/` changed\."
)
REVIEWER_DISABLE_RE = re.compile(
    r"(?:"
    r"\b(?:do\s+not|don't|never|must\s+not|should\s+not|shall\s+not|"
    r"need\s+not|cannot|can't)\b[^\n]*"
    r"\b(?:run|invoke|use|apply|execute|perform|review|required|enable)\w*\b"
    r"|\b(?:skip|disable|omit|bypass)\w*\b"
    r"|\b(?:is|are|be|remain)\s+(?:not\s+required|optional|disabled|omitted|skipped)\b"
    r"|\bno\s+need\s+to\b"
    r")",
    re.IGNORECASE,
)


# These are structural tripwires, not a substitute for methodology review.
# Exact positive clauses protect load-bearing commands from commented-out,
# negated, or inert-token mutations while allowing ordinary prose wrapping.
SKILL_RULES: dict[str, tuple[str, ...]] = {
    "freshness": (
        r"^## Skill Freshness\s*$",
        r"^Before using this workflow, inspect its applicability and correctness and use\s+"
        r"`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK\.md` to select one consistent\s+"
        r"source revision, including references\.",
        r"a user-requested prompt review/test uses the identified candidate under review",
    ),
    "mandatory_authority_reads": (
        r"^## Premise Authority\s*$",
        r"^\*\*Mandatory authority read:\*\* before any premise, import, wall, "
        r"or dependency\s+judgment, read the current axiom memo, primitive "
        r"registry check, registry data,\s+and every relevant primitive source "
        r"listed below\.",
        r"PRIMITIVE_REGISTRY_CHECK\.md",
        r"axiom_premise_nodes\.json",
        r"premise_decision_history\.json",
    ),
    "reviewer_model_and_effort": (
        r"^Review-loop is a text/code/math review path\. Run it with the user's "
        r"configured\s+highest-tier Codex reviewer model "
        r"and maximum available reasoning for this\s+repo\.",
        r"\.\s+Resolve the current model from the active configuration;",
        r"\.\s+Respect an explicit owner\s+choice of model or reasoning tier for the episode\.",
    ),
    "reviewer_lenses": (
        r"^- `CodeRunnerReviewer`\s*$",
        r"^\s+Review changed Python/scripts/log-producing code\.",
        r"^- `PhysicsClaimReviewer`\s*$",
        r"^\s+Attack theorem notes, claims tables, publication surfaces, and prose\.",
        r"^- `ProofObligationReviewer`\s*$",
        r"^\s+Trigger when changed content claims a theorem, proof, derivation, "
        r"reduction,",
        r"^- `ImportSupportReviewer`\s*$",
        r"^\s+Inventory every measured, fitted, literature, PDG, cosmological,",
        r"^- `NatureRetentionReviewer`\s*$",
        r"^\s+Apply the hostile external-review bar\.",
        r"^- `NoGoDisciplineReviewer`\s*$",
        r"^\s+Scrutinize negative claims with the same rigor as positive ones\.",
        r"^- `LabelingConventionReviewer`\s*$",
        r"^\s+Detect labeling/naming/convention content masquerading as a bounded",
        r"^- `RepoGovernanceReviewer`\s*$",
        r"^\s+Check placement and authority surfaces\.",
        r"^Run `MethodologySkillReviewer` when files under "
        r"`docs/ai_methodology/skills/`,\s+`docs/ai_methodology/`, or "
        r"`\.claude/commands/` changed\.",
    ),
    "independent_math_and_mutations": (
        r"independent route",
        r"mutation tests?",
        r"self-confirming tests",
    ),
    "proof_import_governance": (
        r"proof-search-governance\.md",
        r"Inventory every measured, fitted, literature",
        r"RepoGovernanceReviewer",
        r"EQUIVALENT-GAP",
    ),
    "no_go_discipline": (
        r"N1-N8",
        r"NoGoDisciplineReviewer.*blocks PASS|FAIL.*NoGoDisciplineReviewer blocks PASS",
        r"no_go_discipline_gate\.py",
    ),
    "audit_compatibility_boundary": (
        r"## Audit-System Compatibility Gate",
        r"must not run `docs/audit/scripts/apply_audit\.py`",
        r"must not.*apply audit verdicts",
    ),
    "same_session_confirmation": (
        r"same reviewer thread/session",
        r"do not launch a\s+new reviewer process",
        r"FINAL VERDICT: PASS",
        r"fail closed and do not land",
    ),
    "landing_train_scheduler": (
        r"Land confirmed PRs in continuously collected trains of at most eight",
        r"normal departure boundary is 60 minutes",
        r"absolute 75-minute boundary",
        r"open the next empty\s+collecting train immediately",
        r"one-component trains",
    ),
    "landing_train_combined_gate": (
        r"combined gate is mechanical",
        r"check_changed_audit_evidence\.py --base origin/main",
        r'git diff --check "\$review_base"\.\.HEAD',
        r"git diff --cached --check",
        r'if \[ "\$\(git rev-parse origin/main\)" != "\$VALIDATED_BASE" \]; then',
        r'if \[ "\$\(git rev-parse \'HEAD\^\{tree\}\'\)" '
        r'!= "\$VALIDATED_TREE" \]; then',
    ),
    "landing_train_head_guard": (
        r"PR_NUMBERS=\(",
        r"PR_HEADS=\(",
        r"verify_frozen_pr_heads\(\)",
        r"PR head moved; dissolve the train without pushing",
        r"post-push head check",
        r"force-with-lease=refs/heads/<head>:<frozen-head-sha>",
    ),
    "live_surface_routing": (
        r"docs/KEY_SCIENCE\.md",
        r"relevant sharded rows under `docs/audit/data/ledger/`",
        r"archive/publication/ci3_z3/` is record-only",
        r"docs/repo/FRONT_DOOR_STATUS\.md",
        r"docs/repo/RETAINED_BACKBONE\.md",
    ),
    "pipeline_strict_and_evidence": (
        r"run_pipeline\.sh",
        r"audit_lint\.py --strict",
        r"check_changed_audit_evidence\.py",
    ),
    "manifest_landing": (
        r"PROACTIVE rule",
        r"before EVERY push attempt",
        r"run_citation_graph_build\.py",
        r"write_citation_graph_manifest\.py",
        r"citation_graph_manifest\.json",
    ),
    "disk_and_worktree_guards": (
        r"5242880",
        r"mktemp -d",
        r"trap cleanup_review_wt EXIT",
        r"retained worktree for recovery",
        r"from science_fix_loop import cleanup_worktree",
    ),
    "fail_closed_landing": (
        r"for attempt in 1 2 3 4",
        r"landed=",
        r"refs/heads/main:refs/remotes/origin/main",
        r'^\s*if ! git merge-base --is-ancestor "\$landed" origin/main; then\s*$',
        r"landing did not complete after 4 attempts",
    ),
}

GENERATOR_RULES: dict[str, tuple[str, ...]] = {
    "generated_authority_router": (
        r"SPAN_AUTHORITY_ROUTER",
        r'key="review-loop"[\s\S]{0,220}spans=\(SPAN_AUTHORITY_ROUTER,\)',
        r"missing_authority_router_coverage",
    ),
}

PIPELINE_RULES: dict[str, tuple[str, ...]] = {
    "pipeline_contract_registration": (
        rf"^{re.escape(PIPELINE_CONTRACT_LINE)}$",
    ),
}

COMMAND_RULES: dict[str, tuple[str, ...]] = {
    "command_landing_train": (
        r"continuously collected trains of at most eight",
        r"double-buffered landing train",
        r"next empty train\s+opens as soon as the old membership freezes",
        r"verifies every frozen PR head\s+immediately before push",
        r"rechecks each head immediately before its own close",
        r"force-with-lease=<ref>:<frozen-head-sha>",
    ),
}


@dataclass(frozen=True)
class MarkdownScan:
    """Visible Markdown prose plus fenced command blocks and syntax defects."""

    visible: str
    prose: str
    fenced_blocks: tuple[tuple[str, str], ...]
    errors: tuple[str, ...]


def _strip_html_from_line(line: str, in_comment: bool) -> tuple[str, bool]:
    """Remove HTML comments from one non-fenced line, preserving visible text."""
    visible: list[str] = []
    rest = line
    while True:
        if in_comment:
            end = rest.find("-->")
            if end < 0:
                return "".join(visible), True
            rest = rest[end + 3 :]
            in_comment = False
        start = rest.find("<!--")
        if start < 0:
            visible.append(rest)
            return "".join(visible), False
        visible.append(rest[:start])
        rest = rest[start + 4 :]
        in_comment = True


def _markdown_scan(text: str) -> MarkdownScan:
    """Parse the CommonMark constructs that can make contract prose non-rendered.

    This intentionally is not a Markdown renderer. It recognizes the block forms
    that can hide requirements in this skill: HTML comments, fenced code blocks,
    and link-reference definitions (including multiline titles). Unterminated
    forms are syntax defects and make the contract fail closed.
    """
    visible_lines: list[str] = []
    prose_lines: list[str] = []
    fenced_blocks: list[tuple[str, str]] = []
    errors: list[str] = []
    fence_marker: str | None = None
    fence_width = 0
    fence_info = ""
    fence_body: list[str] = []
    in_comment = False
    in_reference_definition = False

    for raw in text.splitlines():
        if fence_marker is not None:
            indent = len(raw) - len(raw.lstrip(" "))
            candidate = raw[indent:] if indent <= 3 else ""
            run = len(candidate) - len(candidate.lstrip(fence_marker))
            if run >= fence_width and not candidate[run:].strip():
                fenced_blocks.append((fence_info, "\n".join(fence_body)))
                fence_marker = None
                fence_width = 0
                fence_info = ""
                fence_body = []
                visible_lines.append("")
                prose_lines.append("")
            else:
                fence_body.append(raw)
                visible_lines.append(raw)
                prose_lines.append("")
            continue

        line, in_comment = _strip_html_from_line(raw, in_comment)
        if in_comment:
            visible_lines.append(line)
            prose_lines.append(line)
            continue

        if in_reference_definition:
            visible_lines.append("")
            prose_lines.append("")
            if not line.strip():
                in_reference_definition = False
            continue

        fence = FENCE_OPEN_RE.match(line)
        if fence:
            token = fence.group("fence")
            info = fence.group("info")
            if token[0] != "`" or "`" not in info:
                fence_marker = token[0]
                fence_width = len(token)
                fence_info = info.strip().lower()
                visible_lines.append("")
                prose_lines.append("")
                continue

        # Four-space/tab indentation is a CommonMark code block. Keep its text
        # available to command-oriented tripwires, but never treat it as prose.
        if line.startswith("    ") or line.startswith("\t"):
            visible_lines.append(line)
            prose_lines.append("")
            continue

        if REFERENCE_START_RE.match(line):
            # A CommonMark definition may put its destination and multiline
            # title on following lines. Definitions are absent from the live
            # skill, so conservatively blank the whole block through its first
            # blank line rather than risk treating hidden title text as policy.
            in_reference_definition = True
            visible_lines.append("")
            prose_lines.append("")
            continue

        visible_lines.append(line)
        prose_lines.append(line)

    if fence_marker is not None:
        errors.append("unterminated fenced code block")
    if in_comment:
        errors.append("unterminated HTML comment")
    return MarkdownScan(
        visible="\n".join(visible_lines),
        prose="\n".join(prose_lines),
        fenced_blocks=tuple(fenced_blocks),
        errors=tuple(errors),
    )


@dataclass
class _ShellFrame:
    """One multiline shell lexical context."""

    kind: str
    paren_depth: int = 0


@dataclass(frozen=True)
class ShellScan:
    """Top-level shell text after inert lexical regions are blanked."""

    active: str
    errors: tuple[str, ...]


def _heredoc_word(line: str, start: int) -> tuple[str, int] | None:
    """Parse one shell heredoc delimiter with quote removal."""
    index = start
    while index < len(line) and line[index] in " \t":
        index += 1
    if index == len(line) or line[index] in ";|&()<>":
        return None

    value: list[str] = []
    quote: str | None = None
    while index < len(line):
        char = line[index]
        if quote is not None:
            if char == quote:
                quote = None
            elif char == "\\" and quote == '"' and index + 1 < len(line):
                index += 1
                value.append(line[index])
            else:
                value.append(char)
            index += 1
            continue
        if char in " \t;|&()<>":
            break
        if char in {"'", '"'}:
            quote = char
            index += 1
            continue
        if char == "\\" and index + 1 < len(line):
            index += 1
            value.append(line[index])
            index += 1
            continue
        value.append(char)
        index += 1
    if quote is not None:
        return None
    return "".join(value), index


def _continued_shell_unit(
    physical_lines: list[str], start: int
) -> tuple[list[str], str, int]:
    """Fold Bash physical continuations into one lexical command unit."""
    unit = [physical_lines[start]]
    folded = physical_lines[start]
    cursor = start + 1
    while cursor < len(physical_lines):
        trailing = len(folded) - len(folded.rstrip("\\"))
        escaped_newline = trailing % 2 == 1
        grammar_continuation = bool(
            re.search(r"(?:\|\||&&|\|&|\|)\s*$", folded)
        )
        if not escaped_newline and not grammar_continuation:
            break
        if escaped_newline:
            folded = folded[:-1] + physical_lines[cursor]
        else:
            folded = folded + " " + physical_lines[cursor]
        unit.append(physical_lines[cursor])
        cursor += 1
    return unit, folded, cursor


def _active_shell(text: str) -> ShellScan:
    """Structurally blank non-top-level shell text.

    The lexer tracks nested quotes, backticks, command/process substitutions,
    and the ordered payload queue for every heredoc attached to a command. A
    line that begins or ends in one of those contexts is inert for contract
    matching. Unterminated contexts fail closed through ``errors``.
    """
    lines: list[str] = []
    frames: list[_ShellFrame] = []
    heredocs: list[tuple[str, bool]] = []
    physical_lines = text.splitlines()
    cursor = 0

    while cursor < len(physical_lines):
        if heredocs:
            raw = physical_lines[cursor]
            cursor += 1
            delimiter, strip_tabs = heredocs[0]
            candidate = raw.lstrip("\t") if strip_tabs else raw
            lines.append("")
            if candidate == delimiter:
                heredocs.pop(0)
            continue

        unit, raw, cursor = _continued_shell_unit(physical_lines, cursor)
        started_in_inert_text = bool(frames)
        comment_at: int | None = None
        index = 0
        while index < len(raw):
            char = raw[index]
            frame = frames[-1] if frames else None

            if frame is not None and frame.kind == "single":
                if char == "'":
                    frames.pop()
                index += 1
                continue

            if char == "\\":
                index += 2
                continue

            if frame is not None and frame.kind == "double":
                if char == '"':
                    frames.pop()
                    index += 1
                    continue
                if char == "`":
                    frames.append(_ShellFrame("backtick"))
                    index += 1
                    continue
                if raw.startswith("$(", index):
                    frames.append(_ShellFrame("substitution", 1))
                    index += 2
                    continue
                index += 1
                continue

            if frame is not None and frame.kind == "backtick" and char == "`":
                frames.pop()
                index += 1
                continue

            if char == "'":
                frames.append(_ShellFrame("single"))
                index += 1
                continue
            if char == '"':
                frames.append(_ShellFrame("double"))
                index += 1
                continue
            if char == "`":
                frames.append(_ShellFrame("backtick"))
                index += 1
                continue

            if raw.startswith("$(", index) or (
                char in "<>" and index + 1 < len(raw) and raw[index + 1] == "("
            ):
                frames.append(_ShellFrame("substitution", 1))
                index += 2
                continue

            if frame is not None and frame.kind in {"substitution", "subshell"}:
                if char == "(":
                    frame.paren_depth += 1
                    index += 1
                    continue
                if char == ")":
                    frame.paren_depth -= 1
                    if frame.paren_depth == 0:
                        frames.pop()
                    index += 1
                    continue

            if char == "(":
                frames.append(_ShellFrame("subshell", 1))
                index += 1
                continue

            if raw.startswith("<<", index) and not raw.startswith("<<<", index):
                strip_tabs = raw.startswith("<<-", index)
                word_start = index + (3 if strip_tabs else 2)
                parsed = _heredoc_word(raw, word_start)
                if parsed is not None:
                    delimiter, index = parsed
                    heredocs.append((delimiter, strip_tabs))
                    continue

            if char == "#" and (index == 0 or raw[index - 1].isspace()):
                comment_at = index
                break
            index += 1

        active = raw[:comment_at].rstrip() if comment_at is not None else raw
        if started_in_inert_text or frames:
            lines.extend("" for _ in unit)
        elif len(unit) == 1:
            lines.append(active)
        else:
            # Preserve physical lines for exact multiline contract matching;
            # ``raw`` was used only for lexical parsing after continuation fold.
            lines.extend(unit)

    errors: list[str] = []
    if frames:
        errors.append("unterminated shell lexical context")
    if heredocs:
        errors.append("unterminated shell heredoc")
    return ShellScan(active="\n".join(lines), errors=tuple(errors))


def _section_disables_reviewer(body: str, reviewer: str) -> bool:
    """Reject any active instruction that disables its bound reviewer."""
    escaped_name = re.escape(reviewer)
    exact_name = re.compile(rf"(?:`{escaped_name}`|\b{escaped_name}\b)", re.I)
    for line in body.splitlines():
        if not REVIEWER_DISABLE_RE.search(line):
            continue
        if exact_name.search(line) or re.search(
            r"\b(?:this\s+)?reviewer\b", line, re.I
        ):
            return True
    return False


def _reviewer_structure_ok(prose: str) -> bool:
    """Bind every reviewer label to its own active, affirmative section body."""
    lines = prose.splitlines()

    def unique_index(needle: str) -> int | None:
        found = [i for i, line in enumerate(lines) if line.strip() == needle]
        return found[0] if len(found) == 1 else None

    def from_first_nonblank(start: int, end: int) -> str:
        first = next((i for i in range(start, end) if lines[i].strip()), end)
        return "\n".join(lines[first:end])

    fanout = unique_index("## Reviewer Fanout")
    required = unique_index("### Required Reviewers")
    optional = unique_index("### Optional Reviewer")
    prompt = unique_index("## Reviewer Prompt")
    if None in (fanout, required, optional, prompt):
        return False
    assert fanout is not None and required is not None
    assert optional is not None and prompt is not None
    if not fanout < required < optional < prompt:
        return False

    positions: list[tuple[str, int]] = []
    for reviewer in REVIEWER_BODY_RULES:
        label = f"- `{reviewer}`"
        found = [
            i
            for i in range(required + 1, optional)
            if lines[i].strip() == label
        ]
        if len(found) != 1:
            return False
        positions.append((reviewer, found[0]))
    if [position for _, position in positions] != sorted(
        position for _, position in positions
    ):
        return False

    flags = re.IGNORECASE | re.DOTALL | re.MULTILINE
    for index, (reviewer, start) in enumerate(positions):
        end = positions[index + 1][1] if index + 1 < len(positions) else optional
        body = "\n".join(lines[start + 1 : end])
        first_instruction = from_first_nonblank(start + 1, end)
        if _section_disables_reviewer(body, reviewer):
            return False
        if re.match(REVIEWER_BODY_RULES[reviewer], first_instruction, flags) is None:
            return False

    methodology = "\n".join(lines[optional + 1 : prompt])
    methodology_first = from_first_nonblank(optional + 1, prompt)
    return (
        not _section_disables_reviewer(methodology, "MethodologySkillReviewer")
        and re.match(METHODOLOGY_BODY_RULE, methodology_first, flags) is not None
    )


def _shell_depths(text: str) -> tuple[list[int], bool]:
    """Return shell compound-command depth before each line.

    The checked snippets use ordinary multiline Bash compound commands. Tracking
    their opening/closing tokens is enough to distinguish executable top-level
    gates from unchanged text nested under `if false`, a loop, case, function,
    brace group, or standalone subshell. Any imbalance fails closed.
    """
    depths: list[int] = []
    depth = 0
    valid = True
    for raw in text.splitlines():
        line = raw.strip()
        close_count = int(bool(re.match(r"^(?:fi|done|esac)\b", line)))
        close_count += len(re.findall(r"(?<![$\w])\}(?=(?:[;\s]|$))", line))
        close_count += int(line == ")")
        depth -= close_count
        if depth < 0:
            valid = False
            depth = 0
        depths.append(depth)

        open_count = int(
            bool(re.match(r"^(?:if|for|while|until|case|select)\b", line))
        )
        open_count += len(re.findall(r"(?<![$\w])\{(?=(?:[;\s]|$))", line))
        open_count += int(line == "(")
        depth += open_count
    return depths, valid and depth == 0


def _context_is_top_level(shell: str, context: str) -> bool:
    """Require one exact context whose first command is at shell depth zero."""
    scan = _active_shell(shell)
    lines = scan.active.splitlines()
    wanted = context.splitlines()
    starts = [
        i
        for i in range(0, len(lines) - len(wanted) + 1)
        if lines[i : i + len(wanted)] == wanted
    ]
    depths, balanced = _shell_depths(scan.active)
    return not scan.errors and balanced and len(starts) == 1 and depths[starts[0]] == 0


def _landing_context_is_top_level(scan: MarkdownScan) -> bool:
    candidates = [
        body
        for info, body in scan.fenced_blocks
        if info.split(maxsplit=1)[0] in {"bash", "sh", "shell", "zsh"}
        and CONTAINMENT_CONTEXT in body
    ]
    return len(candidates) == 1 and _context_is_top_level(
        candidates[0], CONTAINMENT_CONTEXT
    )


def _train_shell(scan: MarkdownScan) -> tuple[str, list[int]] | None:
    """Return the one active train-landing shell block and its command depths."""
    candidates = [
        body
        for info, body in scan.fenced_blocks
        if info.split(maxsplit=1)[0] in {"bash", "sh", "shell", "zsh"}
        and "VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>" in body
        and "PR_NUMBERS=(<pr-a-number> <pr-b-number> ...)" in body
    ]
    if len(candidates) != 1:
        return None
    shell_scan = _active_shell(candidates[0])
    depths, balanced = _shell_depths(shell_scan.active)
    if shell_scan.errors or not balanced:
        return None
    return shell_scan.active, depths


def _ordered_lines_at_depth(
    active: str, depths: list[int], expected: tuple[tuple[str, int], ...]
) -> bool:
    """Require unique active shell lines in the stated order and command depth."""
    lines = active.splitlines()
    positions: list[int] = []
    for wanted, depth in expected:
        matches = [
            index
            for index, line in enumerate(lines)
            if line.strip() == wanted and depths[index] == depth
        ]
        if len(matches) != 1:
            return False
        positions.append(matches[0])
    return positions == sorted(positions)


def _active_context_is_at_depth(
    active: str, context: str, expected_depth: int
) -> bool:
    """Require one exact active-shell context beginning at the requested depth."""
    lines = active.splitlines()
    wanted = context.splitlines()
    starts = [
        index
        for index in range(0, len(lines) - len(wanted) + 1)
        if lines[index : index + len(wanted)] == wanted
    ]
    depths, balanced = _shell_depths(active)
    return balanced and len(starts) == 1 and depths[starts[0]] == expected_depth


def _marked_train_shell(scan: MarkdownScan, marker: str) -> str | None:
    """Return one balanced active shell block carrying an executable marker."""
    candidates = [
        body
        for info, body in scan.fenced_blocks
        if info.split(maxsplit=1)[0] in {"bash", "sh", "shell", "zsh"}
        and marker in body
    ]
    if len(candidates) != 1:
        return None
    shell_scan = _active_shell(candidates[0])
    _, balanced = _shell_depths(shell_scan.active)
    if shell_scan.errors or not balanced:
        return None
    return shell_scan.active


def _train_combined_gate_structure_ok(scan: MarkdownScan) -> bool:
    validation = _marked_train_shell(scan, "TRAIN_COMBINED_VALIDATION_SCOPE=")
    clean = _marked_train_shell(scan, "TRAIN_COMBINED_CLEAN_SCOPE=")
    if validation is None or clean is None:
        return False
    if not _active_context_is_at_depth(validation, TRAIN_VALIDATION_CONTEXT, 0):
        return False
    if not _active_context_is_at_depth(clean, TRAIN_CLEAN_CONTEXT, 0):
        return False
    shell = _train_shell(scan)
    if shell is None:
        return False
    active, depths = shell
    return _ordered_lines_at_depth(
        active,
        depths,
        (
            ("VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>", 0),
            ("VALIDATED_TREE=<combined-candidate-tree-sha>", 0),
            ('if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then', 1),
            (
                'if [ "$(git rev-parse \'HEAD^{tree}\')" '
                '!= "$VALIDATED_TREE" ]; then',
                1,
            ),
            ("if git push -q origin HEAD:main; then", 1),
        ),
    )


def _train_head_guard_structure_ok(scan: MarkdownScan) -> bool:
    shell = _train_shell(scan)
    if shell is None:
        return False
    active, depths = shell
    if not _active_context_is_at_depth(active, TRAIN_HEAD_FUNCTION_CONTEXT, 0):
        return False
    if not _active_context_is_at_depth(active, TRAIN_PRE_PUSH_HEAD_CONTEXT, 1):
        return False
    if not _active_context_is_at_depth(active, TRAIN_POST_PUSH_HEAD_CONTEXT, 1):
        return False
    return _ordered_lines_at_depth(
        active,
        depths,
        (
            ("verify_frozen_pr_head() {", 0),
            ("verify_frozen_pr_heads() {", 0),
            ("if ! verify_frozen_pr_heads; then", 1),
            ("if git push -q origin HEAD:main; then", 1),
            ('if ! git merge-base --is-ancestor "$landed" origin/main; then', 0),
            ('if verify_frozen_pr_head "$pr" "$expected"; then', 1),
            ("printf 'CLOSE_READY %s %s\\n' \"$pr\" \"$expected\"", 2),
        ),
    )


def _missing(text: str, rules: dict[str, tuple[str, ...]]) -> list[str]:
    return [
        name
        for name, patterns in rules.items()
        if any(
            re.search(pattern, text, re.IGNORECASE | re.DOTALL | re.MULTILINE) is None
            for pattern in patterns
        )
    ]


def _append_once(items: list[str], name: str) -> None:
    if name not in items:
        items.append(name)


def validate_texts(
    skill: str,
    generator: str,
    pipeline: str,
    command: str | None = None,
) -> list[str]:
    """Return invariant-family names that are absent from the supplied texts."""
    scan = _markdown_scan(skill)
    active_skill = scan.visible
    command_scan = _markdown_scan(command) if command is not None else None
    active_command = command_scan.visible if command_scan is not None else ""
    pipeline_scan = _active_shell(pipeline)
    active_pipeline = pipeline_scan.active
    missing = (
        _missing(active_skill, SKILL_RULES)
        + _missing(generator, GENERATOR_RULES)
        + _missing(active_pipeline, PIPELINE_RULES)
        + (_missing(active_command, COMMAND_RULES) if command_scan is not None else [])
    )
    if scan.errors:
        _append_once(missing, "markdown_structure")
    if "docs/publication/ci3_z3" in active_skill:
        _append_once(missing, "live_surface_routing")
    if command_scan is not None and command_scan.errors:
        _append_once(missing, "command_landing_train")
    if pipeline_scan.errors:
        _append_once(missing, "pipeline_contract_registration")
    if not _reviewer_structure_ok(scan.prose):
        _append_once(missing, "reviewer_lenses")
    if not _landing_context_is_top_level(scan):
        _append_once(missing, "fail_closed_landing")
    if not _train_combined_gate_structure_ok(scan):
        _append_once(missing, "landing_train_combined_gate")
    if not _train_head_guard_structure_ok(scan):
        _append_once(missing, "landing_train_head_guard")
    if not _context_is_top_level(pipeline, PIPELINE_CONTRACT_CONTEXT):
        _append_once(missing, "pipeline_contract_registration")
    return missing


def validate_repo(repo_root: Path) -> list[str]:
    return validate_texts(
        (repo_root / SKILL_REL).read_text(encoding="utf-8"),
        (repo_root / GENERATOR_REL).read_text(encoding="utf-8"),
        (repo_root / PIPELINE_REL).read_text(encoding="utf-8"),
        (repo_root / COMMAND_REL).read_text(encoding="utf-8"),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    args = parser.parse_args(argv)
    root = Path(args.repo_root).resolve()
    missing = validate_repo(root)
    if missing:
        print("check_review_loop_skill_contract: FAIL")
        for name in missing:
            print(f"  missing invariant family: {name}")
        return 1
    family_count = (
        len(SKILL_RULES)
        + len(GENERATOR_RULES)
        + len(PIPELINE_RULES)
        + len(COMMAND_RULES)
    )
    print(
        "check_review_loop_skill_contract: OK "
        f"({family_count} families)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
