# /autopilot — Science Ops Status & Monitor

You are the Lab Operations monitor for the qubit-lattice axiom framework.

The legacy `AUTOPILOT_WORKLOG.md`-driven loop is retired (its last entry is
2026-04-08). Long-running unattended science now runs through `/physics-loop`
campaigns; the independent audit lane runs separately on `main`. This command
is the status dashboard across all of it.

## Commands

- `/autopilot status` — current locks, loops, PRs, and audit backlog
- `/autopilot history` — what landed recently
- `/autopilot launch` — redirect to `/physics-loop`

## /autopilot status

Freeze a current `origin/main` SHA when available and report its freshness.
Read main queue/status surfaces at that revision. Keep candidate campaign
branches separate; neither the current checkout nor an open PR is main.

1. Lock state:
   ```bash
   python3 scripts/automation_lock.py status
   ```
   Report holder, purpose, TTL remaining, or "free".
2. Candidate loops — for each relevant campaign branch/pack, report its revision,
   slug, route/target, delivery mode, next milestone, provisional dependency
   checks, last checkpoint, and stop condition. A recent checkpoint is historical
   evidence, not proof a worker is running. Use an owned task/lease status when
   available; otherwise mark activity unverified. Flag old packs as stale without
   claiming that their process is alive or dead.
3. In-flight science: `gh pr list --state open` — group science /
   physics-loop / methodology PRs; flag drafts (out of review-loop scope)
   and PRs with unresolved review findings.
4. Audit lane: queue depth from `docs/audit/AUDIT_QUEUE.md` at the pinned main
   revision, plus recent audit commits at that revision. A past audit commit
   does not prove that an audit process is currently running; report its timestamp.
5. Any `PR_BACKLOG.md` entries in loop packs (deliveries that need a human
   or auth to complete).

## /autopilot history

1. Freeze and report `origin/main`'s SHA and freshness. Use
   `git log <MAIN_SHA> --oneline --since="7 days ago" -- docs/ scripts/` for
   landed-main history. If the main ref is unavailable, say so; never substitute
   unmerged current-branch commits as landed work. Report useful candidate
   branch progress separately with its own source revision.
2. `gh pr list --state merged --search "merged:>={date-7d}"` and recently
   closed PRs (review-loop closes-with-salvage rather than merges; check
   `gh pr list --state closed` for salvaged content).
3. Audit movement: `git log <MAIN_SHA> --oneline --since="7 days ago" -- docs/audit/`.
4. For pre-April-2026 history, the legacy `AUTOPILOT_WORKLOG.md` remains as
   an archival record.

## /autopilot launch

Do not launch work from this command. Route to `/physics-loop` (it owns
planning, runtime negotiation, loop packs, checkpoints, PR policy, and
campaign continuation). Before redirecting, run the safety checks:

1. Lock free or owned by a finished session? If held by an active owner,
   report and stop — do not compete.
2. A loop pack or live task already covers the same target? Inspect its exact
   scope and recorded activity; point at its `STATE.yaml` / `HANDOFF.md` for
   resume or coordination. A recently edited file alone does not establish
   exclusive ownership of the target.

## Rules

- Read-only except lock operations you explicitly own. NEVER release a lock
  owned by another worker; never delete loop packs.
- Never start or resume science from here; that is `/physics-loop`.
- Never run the audit loop or touch `docs/audit/` surfaces — the audit lane
  is operated independently.
- Report staleness honestly: a dormant loop is not "running", an open PR is
  not "landed", and a landed note is not "retained" until the ledger says
  so.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
