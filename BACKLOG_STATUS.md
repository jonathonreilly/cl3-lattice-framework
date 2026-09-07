# Backlog review and landing — active

Owner instructions, 2026-09-07: manage review, fixes and landing of the open
backlog on main. Inspect all draft PRs and either mark them ready or close
them with a concrete disposition. Formal audit is deferred until a solid TOE.
The coordinator owns GitHub changes and landing; reviewers return evidence.

The original 13:57 UTC routing refresh had 254 open PRs: 217 non-draft and 37 draft.
The verified post-triage refresh has 233 open PRs and 0 drafts.
All 37 drafts are explicitly in triage scope. Marking ready means reviewable,
not scientifically accepted. A still-draft PR does not land. The standing
reservations #6379, #6858 and #6859 are all non-draft and remain in force.

| Work | Frozen source / owner | Status |
|---|---|---|
| First cumulative science unit | #8001 at `707d7a9c7f929c1c2c16078dfed76acb786e5f3b`, carrying #7983/#7996; Astra xhigh independent reviewer | Independent source review PASS after one confirmed preparation-memo correction: all 97 paths classified, seven runners passed, 19 semantic mutations rejected. Mechanical landing checks pending. |
| All draft PRs | 37 frozen heads in OPEN_PR_INVENTORY.json; separate Astra xhigh reviewer | All 37 source/delta dispositions reviewed: 21 close, 16 ready. All 37 actions verified: 21 closed, 16 marked ready; exact-head checks before and after every action. |
| Faster review contract | `process/coherent-backlog-review-20260907`, base `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`; separate Astra xhigh author | Seven-file candidate complete; 133 focused tests passed. Fresh Astra xhigh adversarial review in progress before use. |

No backlog science has yet landed. All 37 draft actions are verified in
[DRAFT_DISPOSITIONS.json](DRAFT_DISPOSITIONS.json); all 37 reviewed dispositions
and exact heads are recorded there. The coordinator independently checked 396
source blobs across 17 duplicate drafts against their frozen successors. Two
additional old drafts are semantically covered by stronger current-main Cycles
979/983. An empty status reversal and an unexecuted plan complete the 21 planned
closures. Preserve all branches; duplicate closure does not mean source landed.

The 16 ready decisions open reviewable archive/science packets, with source
repair obligations carried forward. In particular #7870, #7871, #7836 and
#7966 have material findings. Queue readiness grants no scientific PASS.
Review findings hold the affected claim or unit, not unrelated checked work.

## Preservation and routing

The repository has shallow history. The inventory's 144 visible ancestry
edges and 110 connected groups are routing over available Git history, not a
proof that every ancestry relation is known. A failed merge-base is unknown;
it must never be interpreted as an empty delta or already-landed source.
Recover necessary ancestry or compare explicitly frozen source trees before
integration. Do not force a stale branch over current main.

Close unlanded work only with a recorded reason and preserved branch/recovery
path. A cumulative successor's presence alone is insufficient to assert its
parents' claims survived. Verify accepted source on main before closing a
covered parent as landed. No auditor verdict or generated status is carried
from a PR as authority. Shared planning and candidate checks grant no grade.
