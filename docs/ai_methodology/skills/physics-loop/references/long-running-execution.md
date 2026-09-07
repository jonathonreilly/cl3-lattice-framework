# Long-Running Execution

Use this reference when `physics-loop` is asked to run unattended.

## Runtime Prompt

If the user did not pass `--runtime`, ask before launch:

```text
How long should this physics loop run unattended?
```

Accept compact durations such as `30m`, `2h`, `6h`, or `12h`. Do not assume a
default runtime for execution. If the user asked only for a plan or status, do
not ask.

For a request such as "run for 12 hours unattended", treat the duration as a
campaign work budget. Keep selecting useful science opportunities until the
deadline or max-cycle limit, subject to the parent skill's quality-exhaustion
and safety/tooling stop conditions. Runtime is not a production quota.

## Preflight

Before modifying files or running long tasks:

1. Fetch current main: `git fetch origin`.
2. Check `git status --short --branch`.
3. Start from a clean branch off `origin/main`. If the current worktree is
   dirty or contains unrelated work, create a separate clean worktree from
   `origin/main` before launching unattended science. Stop only if a clean
   independent worktree cannot be created.
4. Default to `--delivery milestone`: related blocks may compose on one
   isolated campaign branch with a provisional dependency map. When
   `--delivery block` is requested, use branches such as
   `physics-loop/<slug>-blockNN-YYYYMMDD`.
5. Check the cooperative lock if available:
   `python3 scripts/automation_lock.py status`.
6. If the lock is free, acquire it with a TTL that covers the next checkpoint
   window:
   `python3 scripts/automation_lock.py acquire --owner physics-loop --purpose "<slug>" --ttl-hours N`.
7. If the repo lock path is unavailable, record the failure and use a
   branch-local supervisor lock. Lock unavailability is not a campaign stop
   unless another active worker owns the same repo/task and no independent
   worktree is possible.
8. Record start time, runtime, target stop time, branch, delivery mode, next
   milestone, and checkpoint interval in `STATE.yaml`.

## Checkpoints

Checkpoint:

- after grounding;
- after route selection;
- before and after each deep stretch attempt;
- before and after stuck fan-out synthesis;
- before and after long scripts;
- after every artifact;
- after every author or independent check;
- at least once per checkpoint interval;
- before any authorized campaign stop.

Each checkpoint updates `STATE.yaml`, `TRACE_GATE.md`, and `HANDOFF.md` with:

- current cycle and route;
- current science block and branch;
- provisional dependencies, inherited hypotheses, focused independent checks,
  and conclusions affected by changed premises;
- current hard residual, `A_min`, and forbidden imports when in stretch mode;
- files changed;
- commands run and results;
- imports retired/exposed;
- trace-gate classification and reachability to any known blocker;
- review findings;
- PR status for the block;
- next exact action;
- reason for continuing or stopping.

Refresh the lock before it expires. If the repo lock cannot be refreshed,
continue under a branch-local supervisor lock when safe and record the degraded
lock mode. Stop only for a real ownership conflict that prevents safe
independent work.

## Unattended Decision Policy

Avoid mid-run questions. When a decision is needed:

- choose the narrowest honest claim status;
- prefer no-go/archive/demotion over unsupported promotion, but do not choose
  an easy no-go when a named hard residual has not yet received a stretch
  attempt;
- choose the highest-scoring route that passes the dramatic-step gate;
- maintain `OPPORTUNITY_QUEUE.md`; after one lane blocks, pivot to the next
  useful unresolved obligation or discriminator while runtime remains;
- after repeated audit/no-go/blocker cycles, reassess underexplored hard
  mechanisms and attempt one if it can add evidence;
- before declaring global queue exhaustion, inspect materially different live
  routes and synthesize the evidence. Three to five frames is a planning target
  when useful routes exist, not permission to manufacture nominal alternatives;
- treat `--deep-block` as a protected work allocation, not minimum elapsed time.
  A decisive result or exhausted mechanism justifies pivoting; use remaining
  authorized runtime for useful independent work, never busy-waiting;
- skip ambiguous fixes that need human physics judgment for the current lane,
  then checkpoint and pivot;
- treat review `demote`/`block`, failed retained-proposal certification, and
  optional route tooling failure as block-level outcomes, not campaign stops;
- leave clear handoff notes for decisions that require the user.

## Campaign Continuation

The loop should not exit early while runtime remains because one block is
finished or blocked.

When a block reaches a local stop:

1. update `CLAIM_STATUS_CERTIFICATE.md` and `TRACE_GATE.md`, then demote any
   unsafe wording, using
   `proposed_retained` / `proposed_promoted` only for audit-ready author
   proposals and never as audit-ratified status;
2. run the smallest relevant checks;
3. preserve the checkpoint and coherent source work on the campaign branch;
   open a PR only at a review-ready milestone, or a review-ready block in block
   mode, and record actual delivery failures in `PR_BACKLOG.md`;
4. refresh `OPPORTUNITY_QUEUE.md`;
5. start a new science block for the next ranked opportunity.

Only stop the whole campaign before the deadline if:

- a clean independent worktree cannot be maintained;
- all viable queued opportunities are globally blocked and documented in
  `OPPORTUNITY_QUEUE.md`;
- the parent skill's corollary/value-gate exhaustion conditions are evidenced;
- core local tooling needed for every viable route is unavailable;
- another active worker owns the same task and no non-overlapping target can be
  selected.

## Commits And Pushes

Create incremental commits only for coherent science artifacts when the user
requested a run and did not pass `--no-commit`. Related provisional blocks may
share a coherent campaign branch; maintain exact dependency revisions and
inherited conditions. Use block branches when block delivery is requested. Do
not commit unrelated pre-existing changes.

Physics-loop delivery preserves dedicated campaign or science block branches on
`origin`. Do not push science to `main`. Do not merge or weave the science
through repo-wide authority surfaces during the loop run.

## Review PR Backlog

At a review-ready milestone, or each review-ready block under `--delivery block`,
and at an explicit or final handoff when coherent work is ready, unless `--no-pr`
was supplied:

1. For each review-ready campaign or science block branch, run the required checks
   that fit remaining runtime.
2. Push the branch to `origin`.
3. Open one PR per coherent milestone (or block in block mode) with `gh pr create`.
4. Base independent block PRs on `main`; base dependent block PRs on the prior
   block branch and mark them as stacked.
5. Include links to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`,
   theorem notes, runners, logs, verification commands/results, imports
   retired/exposed, trace reachability, and remaining blockers.
6. Use the parent skill's title contract, with both intended claim type and
   honest author support status, e.g.
   `[physics-loop] <slug> milestone NN: bounded_theorem bounded-support`.
7. Never merge the PR. The review-loop/backpressure process decides landing.

If `gh` is unavailable or not authenticated, write `PR_BACKLOG.md` immediately
with exact `gh pr create` commands, branch names, bases, titles, and body-file
paths. This is a degraded delivery, not a reason to discard the block or stop
the campaign while runtime remains.

If runtime is nearly exhausted and work is not coherent enough to commit, write
the loop pack and handoff instead of forcing a commit. If substantial runtime
remains, do not leave incoherent work idle; checkpoint it as abandoned or
historical, then pivot to the next opportunity.

## Stop Cleanly

At stop:

1. Run the smallest relevant checks that fit the remaining runtime.
2. Update `REVIEW_HISTORY.md` and `HANDOFF.md`.
3. Commit coherent work if allowed and appropriate.
4. Push dedicated campaign/block branches to `origin` if they have commits.
5. Open or prepare review-ready milestone PRs unless `--no-pr` was supplied;
   preserve incomplete work with its exact next step without forcing a PR.
6. Release the lock if held and no child process is running.
7. Report status, branch/PR names, artifacts, remaining blockers, and exact resume
   command.

Do not run this stop sequence just because a lane hit a no-go, review demotion,
human-judgment blocker, dirty PR, or missing PR auth. Those are checkpoint and
pivot events during a 12-hour campaign.
