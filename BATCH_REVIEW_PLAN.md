# Faster review and integration of open science

Landed review procedure, 2026-09-07; first combined validation passed. The owner wants the open science integrated
more efficiently and defers formal audit until a solid TOE.
Independent examination of surviving source claims still precedes landing.

## Actual backlog

Current refresh: 173 open PRs, zero drafts. There have been 21 draft closures,
eight science landings with PR closure, and 57 duplicate consolidations;
16 drafts became ready. The original 254 PRs gained five new successors
(#8003/#8004/#8005/#8006/#8007); #8003 is included in the eight landed closures.
The ancestry counts below describe the original snapshot, not this refresh.

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
unchanged in current main `e6a50983b4d4b40ff4faf63a6d5edb0545a769ac`.

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

The third combined landing is the 47-path conditional light-germ source unit
at `16c2d6860e168ec8e5e8f66296410265e5d7226d`. Its eleven constituent PRs were already
closed as duplicates; the successor remains open for the remaining science.
Four complete mechanical runs have served four source batches, with zero
integration retries and no formal audit.

The fourth landing at `e6a50983b4d4b40ff4faf63a6d5edb0545a769ac` integrates
corrected #8003. Parent proof context and complete independent source coverage
were reused only after actual input and current-main preservation checks; the
coordinator inspected correction and integration changes. No duplicate full
review or second pipeline was added to the confirmed unit.
