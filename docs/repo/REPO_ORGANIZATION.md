# Repo Organization

**Claim type:** meta
**Purpose:** navigate current science, work in progress, process instructions,
and historical evidence without confusing their authority.

For term meanings, use [`KEY_TERMINOLOGY.md`](../KEY_TERMINOLOGY.md). For the
end-to-end working process, start with
[`SCIENCE_WORKFLOW.md`](../ai_methodology/SCIENCE_WORKFLOW.md).

## Current Entry Points

| Need | Surface | How to use it |
|---|---|---|
| Read the current scientific package | [`README.md`](../../README.md), then [`START_HERE.md`](../START_HERE.md) | Follow the current science entry points. |
| Verify a claim's standing | Shards under `docs/audit/data/ledger/` on `origin/main` | Check the exact scoped row and its current dependencies. |
| Orient across audited results | [`FRONT_DOOR_STATUS.md`](./FRONT_DOOR_STATUS.md), [`RETAINED_BACKBONE.md`](./RETAINED_BACKBONE.md) | Generated views; verify the relevant shard before relying on a grade. |
| Find source notes | [`KEY_SCIENCE.md`](../KEY_SCIENCE.md) | Navigation to claims and open obligations; the index does not confer standing. |
| Develop, review, audit, or repair work | [AI methodology](../ai_methodology/README.md) | Select the current skill and follow its freshness procedure. |
| Track current-main review defects | [`ACTIVE_REVIEW_QUEUE.md`](./ACTIVE_REVIEW_QUEUE.md) | Actionable findings and repair handoffs, not audit verdicts. |
| Plan the next research target | `AGENTS.md`, `README.md`, and `TOE_SCORECARD.md` on `origin/ai/execution` | Planning only; reverify scorecard evidence against current `origin/main`. |

The `ai/execution` branch never merges into `main`. Read it with `git show`;
keep planning files on that branch or in branch-local working space rather
than copying them into the live science tree.

## Layout And Ownership

- `docs/` contains source notes, scientific indexes, and policy documents.
  A file's presence here does not make its claim retained.
- `scripts/` contains runners and probes. Use each current claim's declared
  runner and evidence; filename prefixes and age do not establish authority.
- `docs/audit/` contains audit policy, tooling, controlled inputs, tracked
  claim shards, and generated views. Only the independent audit lane applies
  verdicts; regeneration alone does not perform a scientific audit.
- `docs/ai_methodology/` contains the workflow and canonical methodology
  skills. `.claude/commands/` provides command entry points into that process.
- `docs/repo/` contains navigation, active feedback, and governance surfaces.
- `docs/lanes/` and `docs/CANONICAL_HARNESS_INDEX.md` help locate lane history
  and runners. Verify their prose against the current scoped ledger before
  using it to select evidence or describe standing.
- `docs/work_history/` preserves earlier notes, reviews, lane boards, and
  backlogs. `archive/` is the record tier; its rules are in `archive/README.md`.
  The deferred publication package lives at `archive/publication/ci3_z3/`.
- `.claude/science/`, `outputs/`, and `logs/` hold branch-local working
  material or runtime output under the applicable skill's placement rules.
  Distill landable evidence into the source packet rather than treating a
  working log as science authority.

## Historical Navigation

The [Historical Lane Status Board](../work_history/repo/LANE_STATUS_BOARD.md)
and [`LANE_REGISTRY.yaml`](./LANE_REGISTRY.yaml) preserve the earlier lane
taxonomy. Their `primary-retained`, `retained-companion`, and related labels
are historical navigation labels, not current audit `effective_status`.
Do not update these snapshots as a required step for every new result.

The [retest playbook](./RETEST_PLAYBOOK.md) and old harness/lane manifests
can suggest reproductions for a historical bug. Select the actual rerun from
the affected current claim and source packet before executing it.
Legacy root `AUTOPILOT_*` protocols describe an earlier automation setup;
current work follows the lifecycle and refreshed skills above.

## Adding Or Correcting Work

1. State one scientific target, the supporting authorities, and the exact
   missing step the task will address. Keep campaign plans outside the live
   science tree.
2. Use clear lane-specific filenames for source notes and runners; preserve
   existing names unless a reviewed move is necessary. Record explicit
   dependencies, claim scope, and executable or other permitted evidence.
3. Prepare a focused PR and route it through review-loop before landing.
   Corrections to current-main science follow the same source-side path.
4. Update a live index only when navigation actually changed. Do not refresh
   dated historical syntheses or hand-author generated status summaries.
5. Hand landed claim/evidence changes to independent audit or re-audit.
   Update planning from the observed result and current status, keeping
   landed evidence distinct from audit-ratified standing.

[`REVIEW_FEEDBACK_WORKFLOW.md`](./REVIEW_FEEDBACK_WORKFLOW.md) describes
feedback placement and closure. [`ROOT_FILE_GUIDE.md`](./ROOT_FILE_GUIDE.md)
explains the remaining root files.
