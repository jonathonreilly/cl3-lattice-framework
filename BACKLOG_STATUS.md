# Backlog review and landing — active

Owner instructions, 2026-09-07: manage review, fixes and landing of the open
backlog on main. Inspect all draft PRs and either mark them ready or close
them with a concrete disposition. Formal audit is deferred until a solid TOE.
The coordinator owns GitHub changes and landing; reviewers return evidence.

The 13:57 UTC routing refresh has 254 open PRs: 217 non-draft and 37 draft.
All 37 drafts are explicitly in triage scope. Marking ready means reviewable,
not scientifically accepted. A still-draft PR does not land. The standing
reservations #6379, #6858 and #6859 are all non-draft and remain in force.

| Work | Frozen source / owner | Status |
|---|---|---|
| First cumulative science unit | #8001 at `707d7a9c7f929c1c2c16078dfed76acb786e5f3b`, carrying #7983/#7996; Astra xhigh independent reviewer | Full source, inherited claims, runners and supporting-tool delta under review. No final acceptance yet. |
| All draft PRs | 37 frozen heads in OPEN_PR_INVENTORY.json; separate Astra xhigh reviewer | Actual source/delta triage underway; ready-or-close recommendations need coordinator verification and current-head checks before action. |
| Faster review contract | `process/coherent-backlog-review-20260907`, base `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`; separate Astra xhigh author | Candidate implementation/testing in progress. Fresh adversarial review required before use. |

No backlog PR has yet been landed or closed by this campaign. Completed
actions and their exact main commits/PR heads will replace this statement.
Review findings hold the affected claim or unit, not unrelated checked work.

The first 19 draft dispositions are recorded in
[DRAFT_DISPOSITIONS.json](DRAFT_DISPOSITIONS.json), pending current-head
verification/action. The coordinator independently compared all 337
non-generated changed files of 14 duplicate source/Eta drafts with the frozen
non-draft #7827 successor: every blob matches. Closing those review duplicates
preserves their original branches and does not mean their source landed.
The other decisions close one empty status reversal and one unexecuted plan,
and mark three useful archive/science packets ready with explicit repair
obligations. Drafts #7870 and #7871 have material scope/stale-source hazards
to fix during full review; their queue readiness is not a scientific PASS.

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
