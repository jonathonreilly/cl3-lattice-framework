# ai/execution — AI execution surface (never merges)

Standing NON-science branch: the durable, versioned home for AI
planning/targeting surfaces — agent instructions (`AGENTS.md`, canonical home),
TOE closure scorecard (`TOE_SCORECARD.md`), versioned local prompt profiles, and (as they accrue) campaign
briefs, dispatch specs, strategy notes. Established at owner request
2026-08-07. Root docs on `main` (`CLAUDE.md`, pointer `AGENTS.md`) point here.

## Contract

- **This branch NEVER merges into `main`.** It is an orphan root (no shared
  history), so `git merge` refuses it as unrelated histories — a structural
  guard, not just a convention. `main` remains the sole authority for science
  content and audit status; everything here is derived, non-authoritative
  planning material.
- **Direct pushes are allowed here.** Science authors propose on branches/PRs;
  reviewed source lands through the independent review path. Routine audit
  application and mechanical refresh may push directly to `main` under their
  existing lane contracts. Commit messages
  carry `[skip ci]` so branch pushes don't trigger workflow runs.
- **The audit pipeline reads `main`'s tree only** — files here are invisible
  to the citation graph BY DESIGN. Never copy or check these files out into a
  `main` working tree: untracked docs in a working tree pollute the audit
  pipeline.
- **Language rules:** framework-terms-only applies to `main` PRs and notes,
  not here. Internal planning vocabulary (root labels, fanout rankings) is
  fine on this branch and must not migrate into science surfaces.
- **Pointer legend:** backticked `project_*` / `feedback_*` names are Claude
  session-memory pointers (local to the operating machine), not repo paths.
  References to `docs/...` files resolve on `origin/main`, not on this branch.

## Read (from any checkout, without touching your working tree)

Start active campaign work from `TOE_SCORECARD.md` and `CAMPAIGN_STATUS.md`.
Use `BACKLOG_STATUS.md` for current review, draft-triage and landing assignments.
`DRAFT_DISPOSITIONS.json` preserves exact source comparisons, reasons, open
review obligations and completed ready/close actions as triage progresses.
`OPEN_PR_INVENTORY.json` captures the open science, frozen heads, changed files
and known ancestry limits; `MAIN_STATUS_SNAPSHOT.json` records exact applied
ledger counts on main, separate from newly landed source.
`BATCH_REVIEW_PLAN.md` summarizes the landed coherent-unit review process.
`NEXT_REVIEW_UNITS.json` freezes proposed source partitions;
`BACKLOG_CONSOLIDATIONS.json` records duplicate closures and transferred
obligations. `backlog_evidence/wave1/` and `wave2/` contain verified landing receipts.
`backlog_evidence/coordinator-efficiency/` records the independent review of
the coverage/reuse clarification. The older scorecard is retained under `history/`.
`BATTERY_PR_SOURCE_MAP.json` pins the first cumulative review candidate's
inherited science blobs without assigning scientific acceptance.

The owner has deferred formal audit until a solid TOE is ready.
Focused independent checks and reviewed science integration continue. A
planning refresh must not launch an audit or promote scientific standing.

```bash
git fetch origin ai/execution --quiet
git show origin/ai/execution:TOE_SCORECARD.md
git show origin/ai/execution:CAMPAIGN_STATUS.md
```

## Edit flow

```bash
git worktree add /tmp/ai-exec-wt ai/execution
# edit files in /tmp/ai-exec-wt
git -C /tmp/ai-exec-wt commit -am "chore(ai): <what moved> [skip ci]"
git -C /tmp/ai-exec-wt push origin ai/execution
git worktree remove /tmp/ai-exec-wt
```

The third reviewed source landing and its exact validation/provenance receipts
are in [backlog_evidence/wave3](backlog_evidence/wave3). Shared statuses keep
landed source, pending review and applied audit standing separate.
