---
name: science-fix-loop
description: Drain cl3-lattice-framework science-repair work without weakening retained-grade standards. Use when asked to run or resume the science-fix backlog, repair applied non-clean audits, recover quarantined or skipped audit rows, turn validated audit handoffs into source-side PRs, or keep audit/science repair progressing until only resource exhaustion or explicitly governed non-repair routes remain.
---

# Science Fix Loop

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Close source-side defects exposed by independent audit and return repaired rows
to audit. Treat every quarantine and skip as a routed work item, never as a
scientific verdict and never as a reason to lower the Nature-grade bar.

## Scope and cadence

Use this lane when source repair or an end-to-end repair drain is requested.
A general discovery task follows `docs/ai_methodology/SCIENCE_WORKFLOW.md`: keep
coherent candidate work moving with selective checks and milestone PRs/audits.
For a request to repair source only, complete the source and reviewable handoff;
do not automatically launch review, landing, or a new audit campaign. The full
drain steps below apply when that end-to-end operation is in scope.

## Authority boundary

- Read current `origin/main`; do not trust a stale local ledger or generated
  prompt as authority.
- Let `audit-loop` select independent auditors and apply verdicts. This skill
  never edits ledger verdict fields or claims that a repair is retained.
- Use a validated `audit_science_fix_handoff_v1` or the matching canonical
  applied ledger row before a non-clean verdict authorizes a scientific edit.
- Treat campaign exclusions, malformed responses, timeouts, transaction
  failures, and selector skips as operational evidence only.
- Use `physics-loop` for substantive source/runner repairs and `review-loop`
  for every PR before landing. A successful review does not replace re-audit.
- Do not introduce a new axiom, primitive, fitted input, hidden import, or
  widened scope merely to turn a row clean.

An explicit long-running request such as "drain", "keep going", or "do not
stop" is a persistence contract. If the caller explicitly requests a Codex
goal, create one for the concrete campaign; a goal is optional orchestration,
not a repair for pipeline state. Keep draining independent work when one row is
hard, quarantined, forensic-only, or awaiting a panel.

## Preflight

1. Work from a clean dedicated clone or worktree. Fetch `origin/main`.
2. Read the current repo copies of:
   - `docs/ai_methodology/skills/audit-loop/SKILL.md`
   - `docs/ai_methodology/skills/physics-loop/SKILL.md`
   - `docs/ai_methodology/skills/review-loop/SKILL.md`
   - `docs/audit/README.md`
   - `docs/repo/REVIEW_FEEDBACK_WORKFLOW.md`
3. Identify the exact audit campaign workdir from the drainer output or
   supervisor process. Do not infer that a campaign is healthy from a running
   PID, and do not recursively search unrelated user directories.
4. Preserve `campaign-row-exclusions.jsonl`, rejected responses, delivery
   envelopes, `campaign-selector-skips.jsonl`, `forensic-canary-*.jsonl`, and
   reports as incident provenance. Never commit them.

## Build the complete repair inventory

Use all three surfaces; none is complete alone.

### 1. Applied scientific verdicts

Prefer the invocation-bound handoff emitted by the audit batch:

```bash
python3 scripts/science_fix_loop.py \
  --handoff-file <campaign>/science-fix-handoff.json \
  --retry-failed --dry-run
```

If no handoff exists, regenerate the canonical prompt inventory and cross-check
each candidate against the current sharded ledger before launching work:

```bash
python3 docs/audit/scripts/generate_conditional_prompts.py
python3 scripts/science_fix_loop.py --dry-run
```

Only complete, applied `audited_conditional`, `audited_renaming`,
`audited_failed`, and `audited_numerical_match` records enter this lane.

### 1b. Archived advisories (post-invalidation recovery)

After a ledger-wide invalidation (premise-epoch reset, packet-requirement
change), zero applied verdicts exist and lane 1 is empty — but the archived
non-clean rationales and canonical repair instructions
(`notes_for_re_audit_if_any`) in `previous_audits[]` still name source defects
the invalidating event did not repair. Recover them as ADVISORY candidates:

```bash
python3 scripts/science_fix_loop.py --from-archived --dry-run
```

Selection is conservative: only rows whose LAST archived verdict is
non-clean qualify (a trailing clean means the defect was repaired and
re-audited before the reset, so plain re-audit is the right next step).
Archived verdicts are VOID and authorize nothing: every worker prompt binds
reproduce-first discipline — verify the named defect on current
`origin/main`, make no edit when it is already settled, and report
"settled on main" with evidence. The independent audit lane re-decides
everything.

The consolidated backlog across all lanes (applied, archived-advisory,
evidence-repair by gate family) is generated nightly to
`docs/audit/data/science_fix_backlog.json` by
`docs/audit/scripts/compute_science_fix_backlog.py`; read it first when
deciding where to drain.

### 2. Campaign quarantines

Render the typed recovery plan first:

```bash
python3 docs/audit/scripts/audit_campaign_repair.py \
  --campaign-workdir <campaign> --json
python3 scripts/science_fix_loop.py \
  --campaign-workdir <campaign> --dry-run
```

The second command may create repair candidates, but it must reconstruct them
from current `origin/main` plus the typed operational record. It must never use
malformed audit prose as a scientific instruction.
This includes a failed final forensic canary: its
`schema_invalid_quarantined` record must select a
`campaign_schema_transport` operational worker even though the top-level audit
campaign exited successfully. Inspect the named preserved canary run log for
the exact validator sequence. Repair a reproducible packet-completion,
sanitized-guidance, retry-budget, or quarantine-control-flow defect with
tests; never edit the claim note or reinterpret the rejected JSON as a
verdict. If current `main` already contains the systemic repair, make no
duplicate edit and route the row to a fresh restricted-context seat in a new
campaign.
Use `--retry-failed` for a campaign incident only after its fingerprint or the
relevant source on `main` changes; do not spend repeated workers on an
identical seat-local record.

### 3. Non-quarantine skips

Read `campaign-selector-skips.jsonl` plus current row state. If the campaign
predates that durable surface, reconstruct it from the batch selector output.
Assign every skipped row one route from the table below. Record claim id,
current status, exact blocker, owner lane, next command, and evidence needed
for re-entry. "Skipped" without a route is an incomplete campaign result.

## Canonical route table

| State or result | Owner and repair | Re-entry proof |
| --- | --- | --- |
| `schema_invalid_quarantined` | Audit tooling. Preserve the rejected output and `forensic-canary-*.jsonl` when present; reproduce validator/transport behavior. Fix only a systemic prompt, schema, CLI, bounded completion, or claim-local quarantine/continue defect. A seat-local malformed answer gets no source edit. | Fresh restricted-context seat in a new campaign. |
| `compute_required` / `compute_required_quarantined` | Physics/runner repair. Produce a SHA-pinned cache, sliced deterministic certificate, faster equivalent runner, or independent derivation. Timeout alone is not a negative verdict. | Completed artifact plus full pipeline and strict lint, then a new campaign. |
| `blocked_row_reentry_quarantined` | Audit control-plane repair. Fix the recorded classifier promotion, dependency/status cycle, hash drift, or invalidation bug; do not mint a placeholder verdict. | One full pipeline convergence where the row does not immediately return to the same dep-ready state. |
| `claim_transaction_quarantined` | Audit control-plane repair. Reproduce and fix apply, pipeline, or strict-lint failure. The rolled-back delivery minted no verdict. | Clean full pipeline; normally a fresh seat in a new campaign. |
| Missing ledger row | Registration repair. Restore the canonical row/source registration and dependency honesty. | Seeder, full pipeline, and strict lint. |
| Ledger note hash lags source | Pipeline refresh, not science invention. | Seeder/full pipeline commit; reselect only after hashes agree. |
| Dependencies not retained | Repair or audit the cheapest blocking upstream dependency. Do not edit the downstream claim to conceal the edge. | Every direct dependency is retained-grade or the downstream scope is honestly narrowed and re-audited. |
| Awaiting repair after conditional | Science-fix from the canonical applied verdict and repair class. | Reviewed source PR landed; the same row becomes eligible through real source/runner/dependency drift. |
| `audit_in_progress` / awaiting second seat | Audit-loop resume. Do not launch a science worker. | Missing valid seat or panel transition completes. |
| No-go or forensic source shape | Audit-loop forensic lane. Do not convert it into ordinary science repair. | Forensic packet and required independent seat(s). |
| `judicial_panel_required` | Governed five-judge panel. A science worker cannot settle reviewer disagreement. | Valid invocation-bound 3-of-5 complete-tuple majority. |
| Meta, decoration, retained-grade, or non-auditable type | No repair unless current governance identifies a distinct source defect. | Record as non-actionable, not silently skipped. |
| Unknown result | Audit tooling triage. Preserve it, add a typed route/test, and keep other rows moving. | Reproducer plus a governed route; never guess a verdict. |

## Dispatch work

Partition the inventory by repair owner before launching agents.

### Scientific source or runner work

Use `scripts/science_fix_loop.py` with the smallest relevant candidate set.
Each worker must:

1. Start from current `origin/main`.
2. Read the target note, direct authorities, canonical harness, applied audit
   rationale, and exact repair target.
3. Use `physics-loop`; make the narrowest honest source/runner change.
4. Run the target harness and relevant tests.
5. Strip all generated audit outputs.
6. Verify the repair against
   `docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` section by section
   before the PR exists, and apply the cure that document states for anything
   it covers; its sections may be cited by number in worker instructions and
   findings, with the skill or script that section cites as the authority.
7. Deliver one coherent repair milestone for review. Related source changes
   can share a milestone; incomplete exploratory blocks remain checkpointed
   with their open obligations, rather than forcing a low-value PR.

If the physics cannot close, retain a bounded theorem, explicit open gate, or
no-go result as appropriate. Do not promote a partial attempt.

### Operational audit work

Use a code/tooling worker, not a scientific derivation prompt. Give it the
typed route, exact validator/pipeline errors, current canonical row metadata,
and saved artifact paths. Instruct it not to edit the claim note or infer a
verdict from rejected output. Require a regression test for the failure mode.

Seat-local malformed output with no reproducible tooling defect needs no PR:
record `fresh_seat_required` and move it to the next campaign.

### Review and landing

For every source-side PR in an authorized review-and-land operation:

1. Verify it is ready for review. Draft status is not permission to promote
   it: leave unrelated or unfinished drafts alone. Mark only this task's own
   completed authoring PR ready when the requested handoff includes review.
2. Pre-fix mechanical non-conformance against
   `docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` before a reviewer
   seat is spent on the PR, then run a fresh `review-loop` agent at the best
   available model and maximum reasoning. The pre-fixable set is the narrow
   mechanical one defined in `review-loop`'s Author Pre-Flight section: link
   resolution and portability, field presence and enum validity, removal of
   forbidden audit outputs, and deterministic command/gate hygiene. Never
   pre-fix dependency-edge intent, import classification, open-bridge
   ownership, claim scope, proof content, or runner logic — those are the
   reviewer's. Pre-fix confers no PASS; the reviewer still judges the final
   state.
3. Apply narrow findings, curing per the conformance spec where it covers the
   finding, then re-review changed files, validate, and land through
   the review-loop cherry-pick path onto current `main`.
4. Close the PR/delete its branch only after containment on `main` is proven.
5. At the requested audit milestone, start a fresh audit campaign for repaired
   rows. Until then record re-audit targets and keep source repair distinct from
   ratification. Never reuse the old
   campaign workdir; its exclusions are intentionally durable.

Limit aggregate Codex concurrency to the measured safe range. Audit seats,
science workers, and reviewers share the same pool.

## Drain loop

Repeat:

1. Refresh `origin/main` and the canonical ledger.
2. Recompute applied-verdict, quarantine, and skipped inventories.
3. Land review-clean repair PRs.
4. Run the full pipeline and strict audit lint for control-plane changes.
5. Start or resume audit-loop in a fresh campaign workdir.
6. Verify each repaired row changed route; detect recurrence by
   `(claim_id, reason, fingerprint)`.
7. Continue all other actionable rows when one recurrence is isolated.

A recurring identical operational failure is a tooling bug: open a focused
regression PR instead of burning fresh seats indefinitely. A changed failure
is new evidence and is reclassified normally.

## Completion

For a source-only request, completion is the reviewable source handoff and named
re-audit targets, with ratification explicitly pending. For an end-to-end drain,
stop only when one of these is evidenced:

- no applied scientific repairs remain, every campaign exclusion and selector
  skip has a typed disposition, all actionable PRs have completed
  review-loop, and a fresh audit campaign confirms the repaired routes; or
- the explicitly stated resource/credit budget is exhausted.

Hard/open physics, forensic rows, and judicial panels are honest dispositions,
not permission to claim success. Report them separately while continuing
independent repairable work. Include counts by route, PR URLs and landing
SHAs, re-audit state, recurring fingerprints, and the exact remaining
resource blocker.
