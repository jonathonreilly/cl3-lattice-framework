# Older #7315-chain source consolidation

**Recommendation: close all 21 screened parents into the still-open #7315 as source/obligation consolidation.** The original source is preserved with a small, explicitly mapped arithmetic correction and append-only history. This is not scientific acceptance, main coverage, or a finding that the parents' open proof and claim-review obligations have been completed.

Target #7315 is frozen at `3c4d52bdb9d3d2e1211799db7232b91b561bf0e1`, with declared base `e7078f7ada6a45008b397ba8ebfb3f3243174093`. All 21 exact parent heads and their valid original merge bases are in `dispositions.json` and `MAPS.json`. The latest captured live check at 2026-09-07 17:10:35 UTC confirms all 22 heads are unchanged, open and ready. Recheck the head and state immediately before an action and retain every original branch/head for recovery.

The parents are #7204, #7203, #7202, #7146, #7136, #7106, #7104, #7083, #7071, #7056, #7052, #7051, #7046, #7042, #7032, #7029, #7028, #7021, #7016, #7015 and #7011. All are actual ancestors of the target in the available object graph, and all original authored merge bases resolve. No missing or shallow merge base was treated as an empty delta. **No fetch was performed.**

## Complete preservation map

I compared actual Git modes/blobs/paths, including complete original base-to-head deltas and each parent’s entire inherited source tree. `MAPS.json` records 86 authored source changes across 85 unique paths, plus generated-manifest changes. The authored changes contain no source deletions. Each `maps/<PR>-to-7315.tsv.gz` is a complete parent source-tree map, with 19,341–19,422 rows, not just a GitHub file list. It records the original and target modes/blobs for every path. Every original source path remains present in the target; the only differences are the four versions below. The map files' hashes, row counts and full difference lists were independently checked again in `VERIFICATION.json`.

The classifier was the actual `generated_audit_output` function and constants from main, with the citation manifest separately identified as generated topology. Controlled data, runner caches, claim-bearing documents and historical provenance were included as source. The classifier logic remains byte/AST equivalent on newer main `12d9c77c0605276b82eb9fcb8cf05cdaf3e40f56`. This report makes no assertion that any of the parents' science is on main.

Nineteen parents have every original authored source postcondition byte-exact in #7315. The two authored exceptions are:

- **#7032:** its 98-line campaign handoff is retained as an exact verbatim prefix, followed by 56 lines of later history. No original text is removed or rearranged.
- **#7029:** the quotient runner retains all notes, assertions, result strings, gates, imports, pins and conditional limitations. Only the two identified exact-arithmetic expression sites change; the original runner blob is preserved in the evidence and branch.

Across all inherited parent trees, there are only four distinct differing source versions. The complete old/new files and raw diffs are preserved in `sources/` and `differences/`.

| Path | Original blob → target blob | Assessed change |
| --- | --- | --- |
| `scripts/admissibility_dirac_kahler_adm_seam_two_history_gram_2026_08_15.py` | `1c156cb2970417dae67a69686a4cb07d4fac0998` → `76fe4963b15c966bdef1fa076bad905a8313c2ea` | Line 861: use the exact determinant directly for the pinned rational Hermitian Sylvester minors, removing numerical recognition. The dressing certificate and positivity predicates remain. |
| `scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py` | `3d82fcff03d550bf56459cef038c61ee7e6c82f1` → `b6b8595f5284dbeaea9ebdb90a8ca8c5f16b26be` | Line 511: retain the exact characteristic-polynomial coefficients directly. No diagnostic coefficient or gate is removed. |
| `scripts/admissibility_dirac_kahler_quotient_gate_2026_08_20.py` | `adf6ed7d16253926e38b7508f5fd737f2e6ac4e5` → `8ec127a0755d1e084c7b4435a1d074e2f61d9a73` | Lines 633 and 1621: construct exact rational squared principal cosines and exact rational tau numerator/denominator substitutions. The old sorting key already required rational cosines; no generic irrational principal-angle API is removed. |
| `.claude/science/physics-loops/CAMPAIGN_20260820_48H_HANDOFF.md` | `a9f44d174bf333b715d285064a6a0e5118825da2` → `3e76bd31a06b6c467e5ce0483002654e9d652a0b` | Strict append. The added inertia-convention, T=4 wrap, nsimplify, causal-time and loci-atlas obligations remain review work. The addendum's scientific and “superseded” assertions are historical claims, not independently accepted results of this routing review. |

## Bounded semantic examination

I read all four raw diffs and the complete old handoff plus addendum. For the three runners I examined the affected functions, their callers and the exact-input construction relevant to the changed expressions. A precise textual transformation reconstructs the complete target versions, proving that no other bytes changed; AST inspection confirms all string literals and docstrings are identical. Original notes, cached result records, no-go ledgers and claim fences survive byte-exact except for the append-only handoff. All original scientific predicates are retained.

Small isolated expression controls, without full runner imports or heavy science, verified the named quotient geometry gives `(1, 3/4)` in both versions; both old and new functions reject the tested irrational squared cosine (the old rational sorting key already does so); three small exact/symbolic characteristic polynomials match; the actual rational tau examples preserve substitutions; and direct rational Sylvester minors give exact positive values. These controls establish the narrow preservation rationale. They do not establish arbitrary-input equivalence or that every large original gate passes after the cleanup: `nsimplify` need not preserve every large exact rational. If direct exact arithmetic changes or rejects a previously recognized value, the original scientific assertion remains explicitly present and must be reviewed on the successor.

The target still has `nsimplify` at quotient lines 1218 and 1764 and shear line 577 (two calls on that line). I make no claim that the chain is globally free of this operation. The target PR body reports broader successful gates; that is an author claim, not my independent validation. `SEMANTIC_CHECKS.json` records the exact tests and limits.

## Required successor review obligations

Closing these parents is honest only as consolidation into a continuing review surface. #7315's nominal three-file hygiene diff is **not** the complete scientific review scope. Its inherited 85 authored source paths from these parents, the earlier inherited differing runners, their actual premise/input closure, original claim/result/limitation records and historical unresolved findings remain attributable and reviewable. A future source review must map all surviving claims and dependencies on the chosen current-main integration, then apply the applicable proof, import, independent-math, no-go, label and governance lenses before any scientific acceptance or landing. This routing review does not discharge those obligations.

The added handoff labels do not authorize deleting original open obligations or importing its claimed exclusions into a future proof. In particular, the inertia tuple-order issue, periodic-wrap exposure, remaining arithmetic-recognition sites, causal-time comparison and loci-atlas bookkeeping need explicit dispositions if load-bearing in a future candidate. Reserved #6379/#6858/#6859 receive no action. Any inherited reference or science from those reservations remains excluded from acceptance/landing; its presence in a preserved ancestry tree grants no review or authorization.

Unread scope is explicit: this was a bounded semantic-preservation review, not a line-by-line scientific review of all 19,000 inherited files or all 85 authored source paths. I did not rerun heavy stages, full pipelines or audit machinery, validate every proof, or convert author-reported results into independent evidence. Original PR bodies are captured for recovery, but were not all scientifically re-reviewed. The source preservation is strong enough for review-queue consolidation; scientific validity and current-main landability remain open.

No repository source edit, commit, push, PR mutation, shared planning edit or audit/status application was performed.
