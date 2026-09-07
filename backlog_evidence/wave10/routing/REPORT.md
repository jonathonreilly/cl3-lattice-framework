# Routing-only consolidation review: #6282 / #6285 / #6287 into #6377

**Decision: safe for source-preserving routing transfer only**, after root verifies these exact bindings and records the complete obligation transfer. This does not approve or land any science. In particular, it does not establish that proofs written against the old Record memo remain valid, and it does not accept the appended ledger claims.

The open target is #6377, “physics: bind Dirac-Kahler action to staggered OS”, frozen head `7fe07db6c03fad1191893c942f708c5cb9a54c43`. All four participating PRs were freshly confirmed OPEN and non-draft at their recorded heads and bases. No head moved from the prior routing inventory. Preserve all original branches and the target branch; a closure changes the location of outstanding review, not the claim's status.

| Original | Frozen head | Actual direct base | Raw authored delta | Source records | Complete original source paths |
|---|---|---|---:|---:|---:|
| #6282 | `058a5c6f88d277a03fe80592f3168a588daf45f7` | `86be489b2e9a400f78380cd9efaf8bdbe077ff20` | 4 | 3 | 19,086 |
| #6285 | `59664313a23fe5c9354d892a4bf00acef4e1d889` | `34e1fa8a8f6c2ad0dc6d5dd652616c86eac56869` | 5 | 4 | 19,092 |
| #6287 | `d7d4d6ecb55ce5c0f6948eba14984b2b93c4730a` | `f978fccc8c42f3ab087a7a60d9d73625bc380423` | 6 | 5 | 19,098 |

The target's own direct base is `99cee0a6c962b382a3ca1a8497d589ffa280dfe8`; its original delta has five paths (four source plus manifest). The three originals contribute 12 authored source records over 11 unique paths: three note/runner/cache trios, one shared ledger and one axiom memo. All nine trio files are exact in the target; the memo and ledger cases are explicitly disposed below. No authored deletion exists.

## Complete preservation, including inherited source

I recomputed all seven original deltas, including the three reserved PRs used only for exclusion, from actual available direct-parent commits and trees. Each declared base is both the actual merge-base and an explicit parent in the head commit. All delta counts and paths match the prior inventory and fresh live metadata. The repository is shallow; I rely on positive visible ancestry and actual objects only, never a negative ancestry inference. Each of the three original heads is visibly ancestral to the target, but ancestry alone is not the preservation evidence.

The three `*-complete-source-map.tsv` files each enumerate the entire 23,145-path original/base/target union. Every row records its classification, authored/inherited/addition disposition and full original-base/original-head/target/current-main mode/type/blob identities. Generated files are retained in the raw maps, not silently discarded. The current-main source-versus-generated classifier was fully inspected for these categories and hash-bound; controlled data remains source. All 30,548 referenced leaf objects across original/base/target/current-main/reserved trees are available locally. Existing local and remote-tracking recovery refs and fresh remote head identities are in RECOVERY_REFS.json. No fetch or shallow-file change was necessary.

For #6282, 23,083 of 23,086 original raw paths are exact in the target; the three differences are the shared ledger, old axiom memo and generated manifest. For #6285 the same pattern is 23,089 of 23,092. For #6287, 23,096 of 23,098 are exact; only the shared ledger and generated manifest differ, since its memo already has the current wording. All 3,999 non-manifest generated paths are exact too; their historical labels are not current scientific authority. The target adds respectively 59, 53 and 47 source paths, all explicitly enumerated. Those successor additions retain their own outstanding science review obligations. There is no source deletion, mode loss, unidentified non-exact source or omitted inherited path.

## The two non-exact source cases

**Shared no-go ledger.** The complete original ledger is a strict byte prefix of the target in all three cases, with unchanged mode. The target adds 113, 101 and 72 lines respectively. I read the complete longest append (Blocks77–83), which contains the shorter appended suffixes; byte comparisons establish this overlap. The additions record historical partial-positive constructions, finite countergates, alternative routes, reopen conditions and caveats about source typing, formation, clocks, recoil, nonlinear completion, state ontology and physical stress. The ledger sometimes describes a seam as constructively closed or partially retired, while also preserving retention and broader obligations. Those assertions are all unaccepted historical source requiring review. Prefix preservation supports lossless transfer, not their truth or current status.

NONEXACT_CONTENT_DISPOSITION.json records the seven block-level content dispositions. Every old row and every alternative/reopen route remains readable in #6377. None of the append's numerical counts, proof claims, N1–N8 labels or apparent retirement language reduces the review burden. The source review for #6377 must resolve contradictory or stale claims against the actual current premises before relying on them.

**Record memo epoch.** #6282 and #6285 contain old blob `2f5fdd26898f62c17fcabc846761f7785c2eadb1`, SHA-256 `53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39`. #6287, #6377 and current main `b0f7089ea5dd6e26e0d58a8a36a77d36c50a8e7a` contain exact blob `bc23300becfe4e4db57153c0e94cfcdf2338da71`, SHA-256 `93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753`. I read the complete old memo and the full old-to-new diff. The owner-approved August13 revision removes the scalar collection functional I, finite Record additivity and I(empty)=0 from axiom content. It instead states that a site without a Record cannot be read and explicitly requires renewed review for consumers of the removed structure.

This is a semantic premise change. It is not byte equivalence or an editorial correction. The old memo is absent from the target's current file bytes, but its exact bytes remain in the preserved ancestral commits, the original branches and this external recovery packet. All old-memo proof, runner, evidence and dependency obligations must therefore transfer to #6377 with an explicit premise-epoch reconciliation requirement. The target must identify affected direct and transitive consumers and determine what survives under the current foundation, what needs an independently supported supplier, and what must remain explicitly conditional or open. Neither the old memo nor an old cache/status may silently supply the removed axiom structure. I did not perform that scientific review or decide which old proofs survive.

Recover the old memo with:

```sh
git show 058a5c6f88d277a03fe80592f3168a588daf45f7:docs/MINIMAL_AXIOMS_2026-06-29.md
git show 59664313a23fe5c9354d892a4bf00acef4e1d889:docs/MINIMAL_AXIOMS_2026-06-29.md
```

Exact external copies are `recovery/6282-MINIMAL_AXIOMS_2026-06-29.md` and `recovery/6285-MINIMAL_AXIOMS_2026-06-29.md`. RECOVERED_HISTORICAL_BLOBS.json also binds complete original/target ledger snapshots and all recovery commit:path specifications. This recovery is historical provenance only; do not restore the old memo over current main.

**Generated manifest.** I read the complete longest manifest diff and verified every old node record is unchanged in each comparison. The target adds historical topology (17 nodes/75 edges relative to #6282). This is not a generated science verdict, a current-main graph acknowledgment or a claim of valid dependencies. All three complete manifest diffs and their dispositions are retained. No generated status is applied or imported.

## Reservations and remaining review

Fresh reserved heads are #6379 `d06066c2b908aaca0779625d831dfb10620cf34d`, #6858 `503cf8dabdfca5d6adc962cdc047846d1d417a77`, and #6859 `275f1bd78201b0d9f440099536d3f602106caf29`. The twelve reserved authored source paths are absent from all four participating trees; their new source blobs are absent under every other path too. Only their common generated manifest path is shared, which supplies no reserved source. #6377 precedes #6379 in the actual visible chain. This does not waive a reservation, authorize future reserved imports, or judge those reserved claims.

I read the original three claim headers and minimal-axiom dependency declarations to identify the obligation-transfer context, not to issue a scientific verdict. Their full proofs, runners and inherited closure were preserved by exact content mapping; I did not claim to reread tens of thousands of unchanged source files or execute their science. The complete source review, actual input/dependency closure, current-premise checks, decisive adverse controls, proof standards, no-go scrutiny and any eventual authorized validation remain work at #6377. Target additions and any additional downstream consumers remain included in that review burden.

The proposed routing disposition is safe only with the exact frozen heads, preservation of branches/recovery content, and the explicit complete obligation transfer above. If the target closes, moves, drops content, or refuses the old-premise reconciliation obligation before action, hold and recompute. This is not raw-tower landing authorization; current-main scientific/process source must not be replaced by this historical branch. Root must perform its own exact check before any PR closure. No audit, pipeline, source edit, PR/GitHub mutation, branch deletion, commit, push or planning write occurred in this review.
