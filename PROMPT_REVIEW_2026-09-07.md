# Prompt review — 2026-09-07

Scope: the active repository instruction and command surface, all eleven
methodology skills and their task-relevant references, author/reviewer/auditor
prompt templates and worker wrappers, this planning branch, and the installed
local Codex research prompts. Historical conversations and captured prompts are
records, not current instructions; do not rewrite them to conceal earlier work.

The runtime instructions available to the current assistant were also examined
for their behavioral effect. Platform-supplied system/developer instructions
are not editable files in this repository. No change here claims to rewrite,
bypass, or replace them. Local command, skill, and profile changes affect later
loading; they do not erase instructions already loaded into a running session.

## Main behavioral corrections

- A request to examine a workflow is not an invocation of that workflow.
  Assess applicable skill instructions before relying on them.
- Target TOE completion without assuming an affirmative result exists. Reward
  concrete obligation closure and discriminating evidence, including honest
  counterexamples, rather than enforced positivity or artifact volume.
- Default to continuous discovery, selective independent checks, and milestone
  PRs/audits, as selected by the owner on 2026-09-07. Critical checks precede
  extensive downstream reuse; formal retention remains separate.
- Fixed numerical thresholds, route counts, worker quotas, elapsed time, and
  inability to imagine a counterexample are not scientific evidence.
- Standard mathematics can supply a missing proof. A theorem does not need a
  newly invented empirical prediction; empirical identifications do need
  explicit inputs, uncertainty, and protection against comparator leakage.
- Scope delegation and pipeline work to the actual task. A distinct agent name
  does not establish independent methods or evidence.
- Preserve dirty/unpushed work on failure. Refresh whole skill packages,
  including referenced procedures, with recoverable backups.

## Prompt ownership

| Surface | Owner and operation |
|---|---|
| Runtime system/developer instructions | Platform supplied; inspected for behavior, not rewritten |
| `AGENTS.md` on this branch | Versioned dispatcher/research operating instructions |
| Main `AGENTS.md` / `CLAUDE.md` | Entry points and source routing |
| Main `docs/ai_methodology/skills/` | Eleven current methodology skill packages |
| Main `.claude/commands/` | Scientific command prompts and adapters |
| Main `docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md` | Restricted independent-audit prompt |
| Main `scripts/science_fix_loop.py` and audit orchestration | Prompt rendering, permissions, publication/recovery mechanics |
| `prompt_profiles/CODEX_GLOBAL.md` | Versioned profile for local `~/.codex/AGENTS.md` |
| Local Codex installed research skills | Distribution copies; source review precedes synchronization |
| Local Claude global rules | General defaults reviewed for scientific-work conflicts |
| Bundled unrelated artifact/product skills | Task-specific tools; not scientific authority and not invoked by this review |

## Known bounded follow-ups

The current negative-claim packet validator still requires five route classes.
That quota is now identified as a procedural constraint, not mathematical proof.
Changing it requires coordinated evidence/schema migration and adversarial tests;
no certificate may fabricate route families or claim a bypass in the meantime.

Ordinary legacy/manual audit application does not universally enforce the same
transport provenance as the current automated runner path. New automated audit
workflows must use the invocation-bound path; a manual apply must not be described
as equivalent authenticated evidence. This review does not retroactively
re-audit science or promote/demote existing claims.
