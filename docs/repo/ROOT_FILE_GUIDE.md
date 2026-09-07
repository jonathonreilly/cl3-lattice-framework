# Root File Guide

**Claim type:** meta
**Purpose:** explain top-level entry points and distinguish current operating
instructions from legacy artifacts.

## Current Entry Points

- [`README.md`](../../README.md) introduces the scientific package and links
  to the current status, foundations, and science index.
- [`AGENTS.md`](../../AGENTS.md) routes automated executors to the canonical
  instructions on `origin/ai/execution`. Read that branch with `git show`;
  its files are planning material and never merge into `main`.
- [`CLAUDE.md`](../../CLAUDE.md) contains the repository model policy and
  points to the same planning branch.
- [`SCIENCE_WORKFLOW.md`](../ai_methodology/SCIENCE_WORKFLOW.md) explains the
  current author → PR → review → landing → independent audit → repair cycle.
- `LICENSE` states the license. `requirements.txt` declares development
  dependencies; `requirements-release.txt` records the release dependency
  pins. Follow the relevant environment setup instructions for a run.

## Legacy Root Artifacts

`toy_event_physics.py`, `ARCHITECTURE_OPTIONS.md`, `SCALING_BENCHMARK_TABLE.md`,
`SCALING_FAILURE_MECHANISMS.md`, and `SCALING_TARGETS.md` are legacy
implementation or architecture/scaling artifacts.

`AUTOPILOT_PROTOCOL.md`, `AUTOPILOT_JANITOR_PROTOCOL.md`,
`AUTOPILOT_SUMMARY_PROTOCOL.md`, and `AUTOPILOT_WORKLOG.md` document an earlier
automation setup and its history. They are not the entry point for starting
current science work or an authorization to bypass current review/audit
boundaries. Use the refreshed repo-native skills for current operations.

## Reading Rule

For physics state, follow [`START_HERE.md`](../START_HERE.md) and the current
scoped shards under `docs/audit/data/ledger/` on `origin/main`.
[`FRONT_DOOR_STATUS.md`](./FRONT_DOOR_STATUS.md) and
[`RETAINED_BACKBONE.md`](./RETAINED_BACKBONE.md) provide generated orientation.

For unresolved current-main review findings, use
[`ACTIVE_REVIEW_QUEUE.md`](./ACTIVE_REVIEW_QUEUE.md). For historical lane
context, consult `docs/work_history/repo/LANE_STATUS_BOARD.md`; its old labels
do not establish current scientific standing.
