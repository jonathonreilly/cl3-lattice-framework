# Autonomy Ledger, Reclassified

## Scope and counting convention

This D6 ledger uses only the five authorized campaign receipts. A citation of the form `C753 boundary.fixed_supplies` means Cycle 753 and that exact JSON field. Each table row is one ledger item. Semicolon-delimited or separately named supplies are split where the receipt makes the split visible. The four inherited-package bundles are not expanded or counted in a D6 class because their inventories are not visible in the authorized receipts.

`DERIVED` below means established only at the receipt's bounded-theorem scope. It does not mean axiom-level, global, or audit-ratified.

## 1. Items DERIVED this campaign

| Item | Reclassified result | Evidence |
|---|---|---|
| Mechanism-level write-once locking | **DERIVED.** The same eight-gate reversible word accepts a first write and cleanly refuses overwrites; the claim stops short of axiom-level Record permanence. | `C745 boundary.mechanism_level_write_once_derived`; `C745 boundary.positive_scope`; `C745 result.write_word_gates`; `C745 result.refusal_censuses` |
| Minimality of genesis length | **DERIVED.** The minimum lawful length is exactly 27, with zero lawful words at lengths 0–26. This derives the length, not the selection of one rank at that length. | `C753 boundary.minimal_length`; `C753 boundary.minimality_derived`; `C753 result.lawful_words_below_27`; `C753 result.minimal_length` |
| The \(b=1\) program's content/order | **DERIVED.** Two anchored candidates reduce to exactly one lawful class. | `C755 boundary.b1_program_unique`; `C755 boundary.positive_scope`; `C755 result.b1` |
| Passive program closure | **DERIVED.** All 894 of 894 tested translations are lawful-to-lawful. | `C755 boundary.passive_closure`; `C755 boundary.positive_scope`; `C755 result.passive_closure` |
| Response-comparison criteria and verdict instrument | **DERIVED as an instrument only.** The frozen criteria are exact recoil \((-2d,+d,+d)\), zero flux balance, and reciprocal transfer at held \(L=6\); the ACCEPT/REJECT/DRIFT machinery generalizes to the checker's fourth candidate. No response law is thereby derived. | `C749 boundary.positive_scope`; `C749 boundary.harness_is_instrument_only`; `C749 result.criteria`; `C749 result.checker_fourth_candidate` |
| Derived occurrence census/comparison | **DERIVED at the 38-epoch sample ceiling.** The census is \((13,13,12)\), with simplex \((13/38,13/38,6/19)\); this is data under a supplied outcome mapping and supplied comparison weights, not Born content or convergence. | `C757 boundary.first_derived_occurrence_comparison`; `C757 boundary.positive_scope`; `C757 boundary.sample_size_bound`; `C757 result.derived_census`; `C757 result.simplex` |

## 2. COUNTED-RESIDUAL items

| Residual supplied choice | Exact count exposed by the receipts | Evidence and limit |
|---|---|---|
| The one base-28 Pruefer rank | **1 choice among 42,277,452,950,578,284,263,485,622,772,148,731,904 minimal classes.** The landed rank is **31,766,083,475,554,533,889,333,676,095,260,538,518**, with outcome `B`. The pre-quotient raw length-27 orbit contains **1,304,242,256,990,794,732,881,944,806,061,811,799,701,848,064,000,000,000,000** words. | `C753 boundary.fixed_supplies`; `C753 boundary.residual_selection`; `C753 boundary.not_derived`; `C753 result.minimal_classes`; `C753 result.landed_word_rank`; `C753 result.outcome`; `C753 result.raw_orbit_length_27` |
| The residual \(b=2\) program class | **1 choice among exactly 81 lawful classes**, obtained from **1,814,400 anchored candidates**. | `C755 boundary.fixed_supplies`; `C755 boundary.b2_residual_classes`; `C755 boundary.not_derived`; `C755 result.b2` |
| The outcome-class mapping convention | The visible convention assigns **38 occurrences to 3 mapped outcome bins**, with exact census **(13,13,12)**; the reversal control has census **(12,13,13)**. **TODO-supervisor: supply the number and identities of admissible alternative mapping conventions.** The authorized receipts do not state that residual cardinality, and the three bin counts are not a substitute for it. | `C757 boundary.fixed_supplies`; `C757 boundary.mapping_convention_supplied`; `C757 boundary.not_derived`; `C757 boundary.positive_scope`; `C757 result.derived_census` |

The Cycle-753 statement that “no landed structure distinguishing one minimal class was identified at this scope” is a precise failed distinction, but this receipt alone does not show accumulated independent-failure evidence. The Pruefer item therefore remains **COUNTED-RESIDUAL**, not **SUSPECTED-INDEPENDENT**. (`C753 boundary.not_derived`)

## 3. Still-supplied items: class and named route

Where a receipt names only an unresolved target rather than an executable route, the target is quoted verbatim and the missing route is marked `TODO-supervisor`. No route is invented.

| Still-supplied item | D6 class | Named route or receipt-exact unresolved target | Evidence |
|---|---|---|---|
| Declared gate alphabet | **FORCING-REQUIRED** | **TODO-supervisor:** no retirement route is named. | `C753 boundary.fixed_supplies` |
| Register layout | **FORCING-REQUIRED** | **TODO-supervisor:** no retirement route is named. | `C753 boundary.fixed_supplies` |
| Explanation of the unique-\(b=1\), counted-\(b=2\) pattern | **FORCING-REQUIRED** | “a structural explanation of the unique-then-counted pattern” | `C755 boundary.not_derived` |
| \(b\geq3\) program counts | **MECHANICALLY-RETIRABLE** | “b >= 3 censuses” | `C755 boundary.not_derived` |
| Frozen Cycle-748 tolerance ladder | **FORCING-REQUIRED** | **TODO-supervisor:** no derivation or retirement route is named. | `C757 boundary.fixed_supplies` |
| Weight or Born content | **FORCING-REQUIRED** | Unresolved target: “any weight or Born content”; **TODO-supervisor:** no forcing route is named. | `C757 boundary.not_derived`; `C757 boundary.weight_claim_made` |
| Convergence beyond the bounded sample | **FORCING-REQUIRED** | Unresolved target: “convergence (small-sample ceiling stated loudly)”; **TODO-supervisor:** no convergence route is named. | `C757 boundary.not_derived`; `C757 boundary.sample_size_bound` |
| Seven-rail encoding | **FORCING-REQUIRED** | **TODO-supervisor:** no retirement route is named. | `C745 boundary.fixed_supplies`; `C745 result.rails` |
| Initial clean sector | **FORCING-REQUIRED** | **TODO-supervisor:** no retirement route is named. | `C745 boundary.fixed_supplies` |
| Macro domain / declared alphabet | **FORCING-REQUIRED** | **TODO-supervisor:** no route deriving the domain is named. | `C745 boundary.fixed_supplies`; `C745 boundary.alphabet_scope` |
| Operations beyond that alphabet | **FORCING-REQUIRED** | Unresolved scope: “out-of-alphabet operations”; **TODO-supervisor:** no finite execution route is named. | `C745 boundary.not_derived` |
| `C_source` firewall | **FORCING-REQUIRED** | **TODO-supervisor:** no retirement route is named. | `C745 boundary.fixed_supplies` |
| Readout conventions | **FORCING-REQUIRED** | **TODO-supervisor:** no retirement route is named. | `C745 boundary.fixed_supplies` |
| Axiom-level Record permanence | **FORCING-REQUIRED** | Unresolved target: “axiom-level Record permanence”; **TODO-supervisor:** no forcing route is named. | `C745 boundary.not_derived`; `C745 boundary.record_permanence_claimed` |
| W5 junction full closure | **MECHANICALLY-RETIRABLE** | “the W5 junction's full closure (multi-cell archive integration is the named next cycle)” | `C745 boundary.not_derived` |
| Candidate kernel schema | **FORCING-REQUIRED** | **TODO-supervisor:** no route deriving the schema is named. | `C749 boundary.fixed_supplies` |
| Built-in demonstration kernels | **FORCING-REQUIRED** | **TODO-supervisor:** the receipt labels them “data” and names no derivation route. | `C749 boundary.fixed_supplies` |
| Response law or gravity content | **FORCING-REQUIRED** | “field/metric response law”; the unresolved boundary is “any response law or gravity content (C_source verbatim)”. | `C749 boundary.remaining_w7_components`; `C749 boundary.not_derived`; `C749 boundary.response_law_selected` |
| No-refit prediction attachment | **MECHANICALLY-RETIRABLE** | “no-refit prediction attachment” | `C749 boundary.not_derived`; `C749 boundary.remaining_w7_components` |

The three counted residual choices in Section 2 also remain supplied; their D6 class is already recorded there and they are not double-counted in this table.

### TODO-supervisor: unreadable inherited inventories

The following fixed-supply bundles are visible only as bundle references. Their contents, item counts, D6 classes, and routes cannot be recovered from the authorized receipts:

- “everything the Cycle-317/744/750 packages declare” (`C757 boundary.fixed_supplies`)
- “everything the Cycle-732 lineage declares” (`C753 boundary.fixed_supplies`)
- “everything the Cycle-719 package declares” (`C755 boundary.fixed_supplies`)
- “everything the landed Cycle-320/322 surfaces declare” (`C749 boundary.fixed_supplies`)

No visible item qualifies as **SUSPECTED-INDEPENDENT**: the receipts do not accumulate the repeated, precise forcing-attempt failures required for that promotion. The one visible failed distinction is retained with the Pruefer residual in Section 2.

## 4. Movement rules

1. A supplied item moves to **DERIVED** only after an executed attempt produces a scoped theorem result. Naming a route, freezing a convention, or passing an instrument check is not enough.
2. **MECHANICALLY-RETIRABLE** means an executable route is named but has not yet been run to retirement. Once run, its result must be reclassified from the resulting evidence; it does not promote automatically.
3. **COUNTED-RESIDUAL** records a supplied choice whose remaining space has been explicitly enumerated. An observed census does not establish the cardinality of a convention space.
4. **FORCING-REQUIRED** remains supplied until a named forcing argument is executed. Where these receipts name only the target, the missing route stays a supervisor TODO.
5. **SUSPECTED-INDEPENDENT** requires accumulated, precise failures of executed forcing attempts. A single scoped failure to distinguish a class is insufficient.
6. Nothing in this ledger is audit-ratified. All five receipts state `audit: "unset"` and `authority: "none"`.

## Class counts in this bounded ledger

- **DERIVED:** 6
- **MECHANICALLY-RETIRABLE:** 3
- **COUNTED-RESIDUAL:** 3
- **FORCING-REQUIRED:** 16
- **SUSPECTED-INDEPENDENT:** 0
- **TODO-supervisor, unclassifiable inherited bundles:** 4, plus the unstated cardinality of alternative outcome mappings and the route gaps marked above
