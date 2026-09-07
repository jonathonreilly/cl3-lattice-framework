# Science-Fix Loop

**Status:** automation for closing missing-derivation rows via Codex CLI.

## What this is

`scripts/science_fix_loop.py` reads `docs/audit/MISSING_DERIVATION_PROMPTS.md`
and, for each row that hasn't been attempted yet, drives the configured Codex model (default gpt-5.6-sol)
(at xhigh reasoning) to attempt closing the chain and opens a PR for
human review and re-audit.

When source repair was explicitly requested, the audit batch may be run with
`--dispatch-science-fixes` to invoke this loop with `--handoff-file` after a
validated non-clean verdict lands. Dispatch is off by default. The handoff uses
schema `audit_science_fix_handoff_v1`; before any edit-capable worker starts,
the consumer refreshes `origin/main`, verifies the claim, invocation, verdict,
scope, rationale, load-bearing step, and repair target against the canonical
sharded ledger row, then reconstructs the prompt from those verified fields.
Malformed, stale, locally fabricated, or schema-invalid audit output is never
eligible: it is not a current scientific verdict and cannot authorize source
edits.

This is an explicitly invoked repair queue, not the default discovery
scheduler. Continuous research may pursue hard open targets and batch delivery
at coherent milestones; use `docs/ai_methodology/SCIENCE_WORKFLOW.md`. The loop only makes
candidate PRs. Those PRs still require review-loop before landing, and
the independent audit lane verifies correctness after merge.

## Mechanics

Candidate order (2026-07-18): within each difficulty bucket
(easy → medium → hard → unknown), mechanical categories before bridge
science (renaming → numerical_match → runner_artifact → scope →
open_gate → failed → missing_bridge_theorem), then descendants
descending. Publication-lane prioritization is deliberately absent: the
lane manifest is a shadow-only authority until the owner's cutover
ratification (dispatch-retarget design note, Ratification Log); the lane
term returns to the sort key only after that ratification.

For each prompt the loop:

1. Atomically reserves up to `--n` rows in `logs/science-fix-state.json`
   as `in_progress`
1b. Skips the row (`skipped_open_pr_exists`) when an OPEN science-fix PR
   for the claim already exists on the remote — the state file is
   per-clone, so this is the cross-workspace dedupe
2. Creates a clean worktree off `origin/main` on a new branch
   (`claude/science-fix/<claim-slug>-<run-id>`)
3. Runs `codex exec -C <worktree> -s workspace-write -m gpt-5.6-sol
   --config model_reasoning_effort=xhigh "<prompt body>"`
   with an explicit edit-only contract in both scientific and operational modes.
   Workers use physics-loop only with `--no-commit --no-pr --no-review-loop`;
   they do not stage, commit, change branches/worktrees, fetch/push, create PRs,
   run review/landing, or launch/apply audits. The controller owns that lifecycle.
4. After codex returns:
   - If no edits were made (codex punted) → record `no_edits`, move on
   - If timeout/stall/edit deadline interrupts the worker → record an incomplete
     result and preserve available edits with recovery paths; do not publish a PR
   - Only a successfully completed worker with edits enters candidate publication;
     completion is not a success or science verdict
   - Restore identified generated audit residue to the attempt's own `HEAD`,
     preserving controlled sidecars; reject an unexpected worker commit or a
     rename/copy crossing the generated-authority boundary
   - Before any restore/reset/unlink, preview staged and untracked destinations
     in a temporary index. Refuse uncertain source deletion/output transfers
     without changing the real index or deleting recovery bytes
   - Record a changed worker HEAD as `worker_changed_head`, even when its
     worktree is clean; preserve its commit, edits, and recovery path for review
   - Stage explicit source paths, commit, push, and prepare the PR; record
     `pr_opened` only after PR creation succeeds
   - On failure preserve dirty or unpushed work; record `recovery_worktree`,
     `branch`, and `recovery_reason` rather than deleting the only copy
5. Cleanup removes only clean work whose HEAD survives on main or the pushed
   branch. Unknown ignored artifacts also require preservation; ordinary regular
   `.pyc` files under `__pycache__` are disposable. An existing attempt directory
   is a recovery item, never discarded merely because its name collides.
6. State is persisted to `logs/science-fix-state.json`, so the same
   row is not re-attempted unless `--retry-failed` is passed

## State file

```json
{
  "attempts": {
    "<claim_id>": {
      "attempted_at": "2026-05-06T...",
      "outcome": "in_progress" | "stale_in_progress" | "pr_opened" | "no_edits" | "timeout" | "codex_failed" | "push_failed" | "pr_failed" | "skipped_open_pr_exists" | "error",
      "worker_id": "pid12345-abcd1234",
      "elapsed_sec": 248.3,
      "category": "renaming",
      "descendants": 435,
      "branch": "claude/science-fix/...",
      "pr_url": "https://github.com/.../pull/N"
    }
  }
}
```

The loop never auto-merges — and science-fix PRs are not DIRECT-merged
either: direct merges bypass the stage-18 citation-graph delta gate and
the landing conventions. Every successful attempt produces a PR that the
review-loop skill's parallel default entry reviews, fixes, confirms,
lands (fail-closed cherry-pick loop, manifest handling included), and
closes end to end — or closes with a reason. After landing, the pipeline
queues the changed row and the independent audit lane picks it up.

Concurrency budget: each attempt is one codex process for up to
`--codex-timeout-sec`; attempts share the machine's codex pool with
audit-lane seats and review-loop reviewers (keep the TOTAL at or under
~8-10; measured 2026-07-17: ~18 concurrent processes collapsed audit-lane
throughput ~20x).

## Commands

```bash
# Try the next 5 prompts (difficulty bucket, then mechanical categories, then descendants)
python3 scripts/science_fix_loop.py --n 5

# Dry-run: show targets without invoking codex
python3 scripts/science_fix_loop.py --n 10 --dry-run

# Restrict to one category
python3 scripts/science_fix_loop.py --n 5 --category renaming
python3 scripts/science_fix_loop.py --n 5 --category failed
python3 scripts/science_fix_loop.py --n 5 --category numerical_match
python3 scripts/science_fix_loop.py --n 5 --category open_gate

# Auditor-written audited_conditional cohorts (added 2026-05-08)
python3 scripts/science_fix_loop.py --n 5 --category conditional_runner_artifact_issue
python3 scripts/science_fix_loop.py --n 5 --category conditional_scope_too_broad
python3 scripts/science_fix_loop.py --n 5 --category conditional_missing_bridge_theorem

# Try a specific row
python3 scripts/science_fix_loop.py --claim-id <claim_id>

# Consume immediate repair candidates emitted by an audit batch
python3 scripts/science_fix_loop.py --handoff-file /tmp/audit_batch_.../science-fix-handoff.json --n 2

# Re-attempt rows that previously timed out / errored / punted
# (skips only rows that successfully opened a PR)
python3 scripts/science_fix_loop.py --n 5 --retry-failed

# Explicitly recover rows reserved by a known-dead worker.
# This is disabled by default; only run when no older worker is alive, or
# choose a cutoff longer than the maximum expected live worker runtime.
python3 scripts/science_fix_loop.py --n 5 --retry-failed --reclaim-stale-sec 7200

# Tighter timeout for exploratory runs
python3 scripts/science_fix_loop.py --n 5 --codex-timeout-sec 600
```

## Safety properties

- **Worktree isolation.** Every attempt runs in a fresh worktree under
  `/tmp/science-fix-worktrees/`. Failures never affect main or other
  audit operations.
- **Sandbox.** `codex exec -s workspace-write` lets codex edit files
  in the worktree but does not give it broader system access.
- **No auto-merge.** Successful attempts open PRs; humans review.
- **Per-row idempotence.** State file prevents re-attempting the same
  row until `--retry-failed` is passed.
- **Concurrent workers do not overlap.** Real runs take a file lock and
  mark rows `in_progress` before starting work, so other workers skip
  those rows. Dry-runs only read state and never reserve rows.
- **Explicit stale recovery.** `--reclaim-stale-sec` is disabled by
  default. Use it only to recover rows from a known-dead worker; an
  automatic cutoff can misclassify a slow live worker as stale.
- **Per-attempt timeout.** Default 15 min; codex is killed if it
  exceeds that.

## Failure modes & what to do

| Outcome | Meaning | Action |
|---|---|---|
| `in_progress` | A worker has reserved the row and may still be editing | Leave it alone unless the worker is known dead |
| `stale_in_progress` | An explicit stale-reclaim run demoted an old reservation | Retry with `--retry-failed` after confirming no older worker is alive |
| `pr_opened` | Codex made edits, PR exists | Run review-loop on the PR; land or close |
| `skipped_open_pr_exists` | Another workspace already has an open PR for this claim | Nothing — review-loop drains that PR; retry only if it closes unlanded |
| `no_edits` | Codex punted — couldn't see how to close | This row is hard; either revise the note manually or accept the verdict |
| `timeout` | Codex didn't finish in budget | Try `--retry-failed` with longer `--codex-timeout-sec`, or skip |
| `codex_failed` | Codex crashed / returncode != 0 | Read the stderr in the state file; usually transient |
| `push_failed` | Codex made edits but git push failed | Check `logs/science-fix-runs/*.jsonl` for details |
| `pr_failed` | Push succeeded but gh pr create failed | Branch is on remote; open PR manually |
| `error` | Loop-level error (worktree creation, etc.) | Check the run log under `logs/science-fix-runs/` |

## Relationship to other loops

- **`physics-loop` skill** (Codex skill in `~/.codex/skills/physics-loop`):
  the user-driven version of the same idea. The science-fix loop is
  the autonomous wrapper.
- **`audit-loop` skill** (Codex skill, `~/.codex/skills/audit-loop`):
  audits claims after they're written. The science-fix loop produces
  PRs that the audit-loop will then check.
- **`codex_audit_runner.py`**: same auditor family (currently
  GPT-5.6-Sol at xhigh) but reads-only. Reads cached runner output and renders verdicts.
- **`compute_reaudit_candidates.py`**: when a science-fix PR merges
  and the upstream's audit changes, downstream rows show up here for
  re-audit via `codex_audit_runner.py --from-reaudit-candidates`, or
  equivalently through the `audit-loop` skill's cascade re-audit source
  before regular queue fall-through.

The full loop:

1. `science_fix_loop.py` opens PR with new derivation
2. A review-loop worker reviews, fixes, confirms, lands, and closes
   the PR end to end (parallel default entry; never a direct merge)
3. Pipeline regenerates (note hash drifts → seed_audit_ledger archives
   the prior verdict, resets to `unaudited`)
4. `codex_audit_runner.py --n 1` re-audits this specific row (via
   normal queue or `--from-reaudit-candidates` for downstream cascade)

### `audited_conditional` From `dependency_not_retained` Is Normal

When a science-fix PR ships a derivation that depends on an upstream
authority that is itself still `unaudited` or `audited_conditional`, the
downstream's first verdict can correctly be `audited_conditional` with
`notes_for_re_audit_if_any: dependency_not_retained`. This records that the
load-bearing input has not yet retained; it is not by itself a defect in the
downstream proof.

The cascade-resolution mechanism resolves these rows naturally:

1. the upstream authority eventually reaches retained-grade through its own
   audit;
2. `apply_audit.py` runs `compute_reaudit_candidates.py` after applying that
   verdict, which flags downstream rows in `reaudit_candidates.json`;
3. the next `audit-loop` invocation, or
   `codex_audit_runner.py --from-reaudit-candidates`, re-audits the
   downstream row against the now-retained upstream.

The science-fix loop should not over-engineer to avoid
`audited_conditional` verdicts when the only reason is
`dependency_not_retained`; the cascade stream is the canonical repair path.
