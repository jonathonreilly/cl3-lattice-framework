# Backlog review and landing — active

Owner instructions, 2026-09-07: manage review, fixes and landing of the open
backlog on main. Inspect all draft PRs and either mark them ready or close
them with a concrete disposition. Formal audit is deferred until a solid TOE.
The coordinator owns GitHub changes and landing; reviewers return evidence.

The original 13:57 UTC routing refresh had 254 open PRs: 217 non-draft and 37 draft.
The verified post-triage refresh has 230 open PRs and 0 drafts after the first three science closures.
All 37 drafts are explicitly in triage scope. Marking ready means reviewable,
not scientifically accepted. A still-draft PR does not land. The standing
reservations #6379, #6858 and #6859 are all non-draft and remain in force.

| Work | Frozen source / owner | Status |
|---|---|---|
| First cumulative science unit | #8001 at `707d7a9c7f929c1c2c16078dfed76acb786e5f3b`, carrying #7983/#7996; Astra xhigh independent reviewer | Independent source review PASS after one confirmed preparation-memo correction: all 97 paths classified, seven runners passed, 19 semantic mutations rejected. Integrated as source-only commit `bc116666469ed260ab53413898480d471c9c4d18`; all 97 reviewed hashes match. Landed on main `2d0f551dcd8bd444daee85b97811cda53da0661e`; all three constituent PRs closed with branches preserved. |
| Next science unit | #7998/#7999/#8000/#8002, frozen terminal `726bafb889a85efadc62dbd81d51efb66c2cdf90`; original #8001 reviewer, separate worktree | Full cumulative source review in progress; exact finite/static/strip/uniqueness/two-site claims and appended consumer probes. Initial proof findings awaiting final scoped fixes. |
| All draft PRs | 37 frozen heads in OPEN_PR_INVENTORY.json; separate Astra xhigh reviewer | All 37 source/delta dispositions reviewed: 21 close, 16 ready. All 37 actions verified: 21 closed, 16 marked ready; exact-head checks before and after every action. |
| Faster review contract | `process/coherent-backlog-review-20260907`, base `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`; separate Astra xhigh author | Seven-file candidate complete; 133 initial focused tests passed. Fresh Astra xhigh adversarial review found a successive-manifest-conflict retry bug. Author fix passes 70 contract tests and same-session adversarial confirmation, including 17 real shell/Git scenarios. Final seven-file patch SHA256 `104d16e39fbf5736bc5cad1f5475872160803d892ebab6a737d9b4229191853e`; committed and combined with the first science unit. |

The first three-PR science unit and seven-file review process have landed. All 37 draft actions are verified in
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

## First integration candidate — 2026-09-07 14:45 UTC

Landed commit `2d0f551dcd8bd444daee85b97811cda53da0661e` is based on unchanged
main `f6f861e8f0c7870b3a9a200a020ec5ca0b14be38`, with 104 reviewed paths
(97 science/provenance and seven process). Complete constituent maps cover
all 23 original #7983 paths, 21 original #7996 paths and 97 original #8001
paths; no original path is missing. The four updated runner caches replace
older evidence, two notes carry reviewed scope/provenance repairs, the
matter runner preserves the mathematics while reducing allocation, and one
preparation memo corrects its live-fuel count. All other original source
bytes survive unchanged, apart from the combined topology acknowledgment.

The full mechanical pipeline, strict lint and changed-evidence check passed
on that exact combined candidate: three evidence rows, zero failures/control
failures; strict lint zero errors. Same-session source reviewers confirmed all
104 integrated hashes, complete constituent maps and disjoint process/science
changes. The 1,438 generated ledger/queue/status paths were inspected, preserved
externally and restored to candidate HEAD; no non-generated byte changed.
One full pipeline ran, with zero integration retries. All 104 source blobs
were verified on remote main before #7983/#7996/#8001 were closed. Their
branches remain available. The installed review-loop skill is synchronized
with current main, with a backup of its previous bytes.

Frozen maps, gate results and verified landing/closure receipts are in
[backlog_evidence/wave1](backlog_evidence/wave1). No scientific audit or
verdict application occurred. Current ledger counts still describe the applied
main ledger; source readiness does not promote those counts or statuses.

The next review has found errors in the strip Perron proof normalization,
the pair-block supremum inequality and finite-window contraction scope, plus
unsupported larger-block and Gaussian-consumer claims. These are repair
obligations; the four-PR unit remains held until final source confirmation.

Read-only tower routing found that #7827 and #7813 both contain source from
all three owner-reserved PRs. Neither raw tower is a permissible whole landing
unit. Complete delta coverage is being mapped before splitting by source
dependencies. Shared history and exact copied files are not scientific PASS.

## Further consolidation and review assignments

[BACKLOG_CONSOLIDATIONS.json](BACKLOG_CONSOLIDATIONS.json) records 26 exact
duplicate-consolidation decisions awaiting coordinator actions: nine source/Eta
parents into open #7827 and 17 light-sector parents into open #7937. Root
independently checked every authored original delta and complete inherited
source (Eta) or whole parent tree (light), including file modes and blobs.
Every scientific and evidence obligation transfers to the open successor;
reserved source remains excluded, branches remain, and no science is accepted
or declared landed by these duplicate closures.

[NEXT_REVIEW_UNITS.json](NEXT_REVIEW_UNITS.json) freezes six proposed partitions
across 35 original open constituents. They are initial review scopes, not a
claim that all inherited tower content has been reviewed. The light germ /
finite-depth dynamics unit (47 source paths, 11 notes and 11 runners) is now
in independent Astra xhigh review against #7937's frozen head. Admissibility
repairs are assigned to a separate implementation worker; the original
reviewer owns confirmation. No author or reviewer has GitHub mutation authority.
