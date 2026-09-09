# Faster review and integration of open science

Landed review procedure, 2026-09-07; first combined validation passed. The owner wants the open science integrated
more efficiently and defers formal audit until a solid TOE.
Independent examination of surviving source claims still precedes landing.

## Actual backlog

Current counts, assignments and landing evidence are in [BACKLOG_STATUS.md](BACKLOG_STATUS.md). The following ancestry counts describe the archived original snapshot.

The snapshot contains 254 PRs. 129 name another open branch as their GitHub
base. Actual Git history yields 144 nearest-open-head ancestry edges and
110 connected groups; the largest contain 97, 19, 11 and 7 PRs. These are
routing facts over the available local history, not scientific equivalence
or an exhaustive ancestry proof: the object store is shallow. Unknown
merge-bases need recovery, not an empty-delta assumption. The 97-member group must be split
by coherent arguments and includes owner-reserved material.

The previous review-loop batched only the landing tail. It required
per-PR review, per-PR full pipelines, and another full pipeline on the batch;
it excludes stacked PRs from sharing a batch. Eight components could therefore
require nine full pipeline runs before retries, despite repeated context.

## Proposed review unit

Review a coherent argument at its final source state, which may combine
multiple dependent PRs. Require:

1. Frozen PR heads, starting main and source provenance.
2. A mapping of every constituent claim to final source, or an explicit
   narrowing, supersession, rejection or deferral. Do not silently drop science.
3. An integrated source delta preserving current-main content, excluding
   branch-authored generated audit/status outputs.
4. Independent examination of every surviving claim and interacting premise.
   Reuse earlier checks only when their source and hypotheses match exactly.
5. Changed-runner reproductions and focused premise/evidence/source checks;
   findings fixed and confirmed on final source.
6. One full mechanical validation on the frozen integrated landing batch,
   followed by source/hash verification and generated-output cleanup.
   This validation does not invoke a scientific auditor or assign a verdict.

This changes the review unit and placement of repeated mechanical work, not
which scientific claims require scrutiny. The executable seven-file contract has now passed independent adversarial
review and same-session confirmation after a successive-manifest-conflict
repair. It landed at `2d0f551dcd8bd444daee85b97811cda53da0661e` and remains
in the current source workflow.

## Integration

Review independent units in parallel within actual resource limits. A
conflict, moving head or unproved identification holds only the affected
unit. Integrate compatible confirmed units and check their interactions;
changed source returns for focused confirmation. Run full validation on that
exact tree. If main moves, preserve current science and refresh the affected
integration evidence. Close a constituent PR only after its accepted science
is verified on main and its disposition recorded.

Do not make one giant batch of the whole backlog. Avoid arbitrary waiting once a useful
checked batch is ready. No batch operation promotes audit status.

## Initial groups

Immediate consolidation candidate: #8001 is already based on main and carries
the #7983/#7996 source packets. Direct blob comparison finds all six parent
science paths present: three unchanged and three updated. Reviewing #8001's
complete final packet can cover those inherited claims without treating the
older parent verdicts as current. Verify the content/disposition map before
closing covered parents. This existing cumulative-submission route does not
require waiting for the broader review-contract proposal to be implemented.
The exact six-path comparison is in
[BATTERY_PR_SOURCE_MAP.json](BATTERY_PR_SOURCE_MAP.json); its initial six-path comparison is superseded for landing by the complete
23/21/97-path maps and confirmations in `backlog_evidence/wave1`.

| Group | PRs | Why together / required check |
|---|---|---|
| Admissibility/static/formation | #7998, #7999, #8000, #8002 | Shared six-state rule. Keep formation, static existence, sufficient contraction criteria and physical law selection distinct. |
| Native Record energy apparatus | #7983, #7996, #8001 | Final proposal carries both parent packets. Verify CAR/instrument hypotheses, dwell convention, energy/coherence cost and shared memory. |
| Finite-spin field response | #7941, #7943, #7945, #7946, #7952, #7953, #7955; later #7963/#7966 | Shared Hamiltonian and observables. Verify physical source conventions before response joins; preserve convergence failures. |
| Curved-cell/source-action | Split the 97-member group | Separate old premise epochs, conditional kernels, action identification and reserved components; do not bulk approve history. |

## Campaign finding that changes the field group

An independent reconstruction of frozen #7946 and its electric/spectral
parents confirms a source mismatch. With their physical electric map
`E_i(r)=(-1)^sum(r)(n_i(r)-1/2)`, the old plaquette phase probes a checkerboard
source. A uniform Cartesian source needs the root-parity factor. Exact L2
fourth-trace polynomials distinguish the resulting matrix families.

The held scope is the identification of the original response with uniform
magnetic K and the downstream UK interpretations. Preserve the original
matrix response, electric data, spectral data, conditional kernel theorems,
and their separate estimator limitations. Do not rerun every inherited
calculation or delay unrelated groups. The final packaged correction passed
focused independent confirmation on the campaign branch, bound by the source
hashes in its field review receipt. It has not yet repaired the original PRs.

A second exact source identity equates the fully relaxed spectrum at a whole
background flux quantum with the zero-source spectrum. This leaves a separate
branch/sector definition and limit obligation before identifying infinitesimal
source curvature with magnetic-flux-sector stiffness. It is not evidence that
the physical phase has been ruled out.

PRs #6379, #6858 and #6859 remain reserved under the standing defaults in
main's docs/repo/DEFERRED_DECISIONS.md. This proposal does not change that.
Other unresolved-base or historical branches need content/landing comparison.

## Measure the improvement

Record reviewer time, distinct source reviewed, runner time, full pipeline
count, integration retries and scientific findings per unit. Compare the first
small group with former per-PR execution. A reduction in mechanical runs alone
does not establish a whole-campaign speedup.

## Coordinator efficiency clarification — 2026-09-07

The current-main review contract already makes the coordinator an integration
function, while independent reviewers inspect the complete frozen source unit.
The shared `AGENTS.md` now makes that division explicit: preserve author cold
diff reading, full independent source/lens coverage and same-session correction
confirmation; verify complete original/final claim and content maps and actual
input closure; read every correction and additional integration change; check
current-main science preservation and all semantic interactions. Verified,
unchanged source bodies need no second identical coordinator reading.

A missing helper pin, omitted inherited/deleted content, a changed premise, a
moved head or new interaction holds the affected conclusions and dependents.
The one combined exact-base/tree mechanical gate remains mandatory. This is an
interpretation of the existing landed contract, independently challenged by
two Astra xhigh agents; it does not replace full review with summaries or
mechanical PASS tokens and introduces no new scientific status.

## Publication ordering and shared status

Complete note corrections and provenance links before an expensive input-bound
run. Record the actual attempt and its limits; leave the final cache to identify
its own exact outcome. A changed input requires fresh evidence, never a relabeled
old receipt. Reuse unaffected computations only under exact source/input binding.

When corrected source is frozen, compose its current-main source and generated
manifest before asking for final affected-scope confirmation. The original
reviewer can then check repairs and integration in one pass. Preserve complete
source/proof coverage, exact-input controls and the combined landing gate; avoid
a separate later handoff for an otherwise unchanged manifest.

BACKLOG_STATUS.md owns current counts and assignments. Preserve earlier snapshots
under history and bind detailed evidence by hashes. New submissions remain outside this cleanup inventory under the owner cutoff. Follow the established
continuous-discovery, selective-check, milestone-PR cadence; a research block or
passing runner alone is not a publication milestone.

## Owner cutoff — original backlog only

The cleanup includes only the original 254 PR identities and original scientific
scopes captured at 13:10:39 UTC on 2026-09-07. `BACKLOG_CUTOFF.json` pins membership,
original heads and the source snapshot. New-arrival PRs are excluded from review,
draft triage, repairs and landing for this task. Preserve their partial work with
an owner-cutoff deferral and no new verdict. Do not treat a post-cutoff successor
as permission to expand the cleanup's scientific scope.

Prioritize bounded units that complete an original PR's scientific disposition.
Keep full science landings, partial source extractions and draft/preservation
closures separate in throughput reports. `OPEN_PR_INVENTORY.json` now contains
only the still-open members of the fixed original set. Refresh their actual heads
and necessary source maps; do not ingest new arrivals. Existing source and
reservation standards remain in force, and formal audit stays deferred.

`BACKLOG_CLOSURE_RECONCILIATION.json` tracks scientific content separately from
GitHub actions. Later reviewed extractions must update each original constituent's
scientific disposition even if its PR was already closed. A consolidation retains
every unresolved proof, premise and evidence obligation at its named open
successor. Closing that successor requires explicit dispositions or another
fully preserved transfer; reducing visible PR count alone cannot retire the work.

## Measured throughput adjustment — 2026-09-08

The owner requested further acceleration with 100 original PRs remaining.
The latest batch took 78.14 elapsed minutes from its original review seal to
landing; its combined validation took 4.00 minutes. Seven recent combined
gates have a 3.93-minute median. These are stage-boundary wall times, including
science, waiting and a nightly-main recomposition, not an active-time profile
or a measured estimate of avoidable delay. The exact observations and source
bindings are in [the timing evidence](backlog_evidence/throughput-review-20260908/COORDINATOR_TIMING_EVIDENCE.json).
An independent Astra xhigh reviewer examined the proposed changes and their
failure cases in [the process review](backlog_evidence/throughput-review-20260908/REVIEW.md).

Apply these scheduling clarifications within the existing landed contract:

- Hand evidenced, bounded findings to a separate author before the original
  review report is fully packaged, after freezing original source/heads and
  identifying the affected dependency boundary. The reviewer continues on
  immutable originals and records later findings or contrary evidence.
  Early drafting grants no completeness claim or approval; final fixes and
  executions must incorporate the completed original review.
- Prioritize a ready correction's same-session final confirmation over new
  original reviews or long legacy repair work. Checkpoint other work at safe
  boundaries; preserve active bounded runs and their evidence.
- Send reviewable draft correction diffs and publication/input placement to
  the coordinator early, so its source and interaction checks overlap the
  author's remaining work. Complete the cold diff, prose and input freeze
  before genuine final caches; never restamp prior output.
- Keep units with a bounded actual dependency closure moving alongside
  explicitly resourced legacy restoration. Small nominal diffs alone do not
  establish bounded closure. Do not starve, discard or count legacy
  obligations as landed. Combine compatible ready units without a collection
  wait or a requirement to finish unrelated work.

Tooling work proposed next, not yet implemented or a source of acceptance:

- One tested mechanical utility for complete original/current tree and path
  accounting, modes, moves/deletions, immutable artifact bindings and exact
  input/tool/log checks. Cache independently verified immutable Git facts by
  object identity; new endpoints, changed heads and semantic interactions
  still require their applicable checks. Existing reading-coverage tooling
  does not provide this verifier or certify science.
- One canonical per-unit evidence record with generated status and handoff
  views. Preserve full scientific explanations, raw outputs, real failures,
  historical revisions and explicit claim dispositions. Keep initial findings,
  failed attempts, provisional results and final acceptance distinct.

Measure original review, repair, final confirmation, coordinator handling and
mechanical validation separately over the next three batches. Record overlap
and blocking events; report a speedup only after comparison. No throughput
quota grants a scientific result. Complete independent final-unit/lens review,
independent mathematics, constituent content preservation, same-session final
confirmation, current-main science-loss/interaction checks, one combined gate,
transitive reservations and the original cutoff remain unchanged. Formal audit
continues to wait for a solid TOE. No automatic science retry is authorized.


## Wave50 packaging preflight placement

Before the shared graph/pipeline run, check the complete source diff, including exact historical recovery artifacts, and use the actual note-discovery, claim-type, helper and cached-readiness consumers. A legacy NOGO filename can select a different assurance path than corrected bounded prose. Correct inaccurate source naming and bindings through the original author/reviewer; never fabricate resolution certificates. Preserve original archive bytes, using narrowly scoped Git whitespace attributes when needed. Every active source remains checked. W50 retained its actual filename evidence failure and later historical-whitespace clean-state failure; moving these existing checks earlier prevents the same wasted full-run cost. This planning note changes no scientific acceptance or audit boundary.
