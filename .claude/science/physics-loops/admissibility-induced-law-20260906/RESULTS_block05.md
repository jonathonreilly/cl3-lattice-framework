# RESULTS — block 05 (Fable primary seat; Opus contract lens before the build; Opus refuting checker pending), 2026-09-07

## Headline

Every linear extension of the product partial order on a rectangle — every order in which each site waits for its left and above neighbors — gives the same formation law `μ_P`, for every nearest-neighbor rule (P1: the recorded set of every site is `{left, above}`; the 5, 42, 462 extensions of `2×3`, `3×3`, `3×4` executed, 24024 counted on `4×4`). Under `μ_P` every row and every column is the path chain `p_0` (P4), every `2×2` block carries the corner law `π(c,b,a,d) = (1/6) K(c,a) K(c,b) K(a,d) K(d,b)/K^2(a,b)` with the two neighbors of a corner independent given it (P5, proved from block 02's telescoping partial sums with the `n`-row reduction; executed at all 4 block positions of `3×3` and all 6 of `3×4`), and no staircase with a turn is a Markov chain at any positive triple with `p, q, r` not all equal (P6, proved from P5 by a Cauchy–Schwarz step; the minimal staircase's conditional `227/858` against `1/4` at `(3,1,2)`; the six staircases of `3×3` executed with exact defects; `P(c|c,c) > K(c→c)` on all 210 non-constant triples of `{1..6}^3`). The boundary: the mirror class differs from `μ_P` on 32616 of 46656 configurations of `2×3`; the snake proper keeps `p_0` rows and `(1/6) K` vertical pairs but on `3×3` only column 0 is a chain (defects `0`, `3161/7227792`, `3583442207/7981260404832`) and on `4×3` no column is (P7, executed). No order is selected as physical.

## Run record

- Runner `scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py`: `TOTAL: PASS=38 FAIL=0`, 23 declared mutations (4 B, 4 C, 5 D, 6 E, 4 F), unmutated stdout 5,992 characters, baseline 40.5 s (integer numerators over common denominators in the row transfers; the `2×4`/`4×2` transpose check on 1,679,616 configurations is the largest single item).
- Cache: runner sha256 `73ae26a5dfaf71694fa299d8734cafbf74b7eebc8ce2e84a7e7d8daee10a1f22`, input fingerprint `1a49b041364505ca04c08d5a2ea09b76fe03b3eab5f4d3eb1fa17d6e6d8e51cf`, exit 0, elapsed 54.84 s (written by `execute_and_write_cache(<runner>, 900)` after the final note edit, while the census ran 4-wide; the uncontended baseline is 40.5 s).
- Note `docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md`: 578 lines; `vocab_lint --report-only` 0 violations; the literature name appears in the Prior art and Imports sections only (checked by the runner's F3 with the needle assembled from character codes, so the runner source carries no such label).
- Control reproduction before any theorem sentence (own code, scratch `control_repro.py`): bridge identity, the 5-extension law equality on `2×3`, the counts 5/42/462/24024, the `3×3` column chain, the corner law at two block positions, the RDRD staircase defect, `227/858` vs `1/4`, the snake `3×3` defects `0`, `3161/7227792`, `3583442207/7981260404832`, the mirror count 32616 of 46656, and the `4×3` snake with no column a chain — all equal to the supervisor's controls; 1.2 s.

## Defects fixed while executing

- The runner's own `N(` scan tripped on the block-01 fragment `A_k = N(x_k)`; replaced by the fragment `FORMATION law of a rule for a formation order` (present in block 01's note across a line break; the check normalizes whitespace).
- The diagonal-pair check first asserted `(1/6) K^2 ≠ (1/6) K` entrywise and failed at `(3,1,2)`: `K^2` and `K` agree on the orthogonal orbit exactly when `p + q = 2r`, which holds there (`2r(p+q+r) = r(p+q+4r)`). The check now states the inequality as a statement about laws and executes the orbit fact at both triples (D6); the note records it as a remark.
- Unmutated stdout was 6,524 characters; detail strings and the N5 lines were shortened to 5,992.
- The census helper's argument order was wrong on the first launch (the xargs form passed the directory as the mutation name); corrected, no runner change.
- P5's proof, first draft, summed the columns beyond `j` from the right end over the β's; the correct order sums the α's from the right end first (each `Σ_{α_l} K(α_{l−1}→α_l) K(α_l→β_l) = K^2(α_{l−1}, β_l)` cancels that column's denominator), then the β's; and the left partial sum's product index runs over `1 ≤ l ≤ j−1`. Corrected in the note (no runner change; the corner law was executed, not derived, by the runner).

## Could-not list

- The `3×4` executions are at `(3,1,2)` only (both triples at `3×3`); a `4×4` law is counted (24024 extensions) but not executed.
- The three corner classes other than the row sweep and its mirror are not separately executed; their row/column statement is by reflection symmetry.
- P6 excludes first-order Markov chains in the site values along staircases; second-order chains or changes of state space are not addressed (steelman N7).
- No characterization of the orders outside the class whose columns are chains is attempted; the snake's `3×3`/`4×3` pattern is an executed description only.
- The refuting checker seat has not yet run.

## Modelling choices (declared, not physics)

- Menu order and orbit weights as in blocks 01–04; `K(a→s) = φ(s,a)/Z_1`; `K^2` as integer numerators `K2n` over `Z_1^2` (`26, 22, 24` at `(3,1,2)` for the parallel, antiparallel, orthogonal orbits; `93, 84, 88` over `529` at `(5,2,4)`), `L = lcm` of the three values, so that every bridge factor is `φφ (L/K2n)/L`.
- The row kernels `P` (left to right) and `P_rl` (right to left) as integer numerators over `Z_1 L^{W−1}`; `p_0` over `6 Z_1^{W−1}`.
- Marginals of three-row rectangles by the middle-row contraction (`U[s0][r1] = Σ_{r0 ∼ s0} p_0(r0) P(r0,r1)`, `V[s2][r1] = Σ_{r2 ∼ s2} P(r1,r2)`); of two- and four-row rectangles by the column-projected row transfer whose state is (carried values of the selected sites in earlier rows, the full current row); the two agree on column 1 of `3×3` (D7).
- Staircases of `3×3` labelled by their step words `RDRD, DRDR, RRDD, DDRR, RDDR, DRRD`; the snake convention: row 0 left to right, row 1 right to left, and so on; the `i+j` sweep with ties by `i`; the `i−j` and `j−i` sweeps with ties by `i`.
- The general-triple execution of P6 on the integer grid `{1..6}^3` (216 triples, 6 constant).

## Exact laws and defects (`--exact`)

- `K` at `(3,1,2)`: `1/4` parallel, `1/12` antiparallel, `1/6` orthogonal; at `(5,2,4)`: `5/23`, `2/23`, `4/23`.
- Minimal staircase at `(3,1,2)`, `c = b = P(e_x)`: `P(d | c, b) = 227/858, 197/2574, 212/1287, 212/1287, 212/1287, 212/1287` against `K(b→d) = 1/4, 1/12, 1/6, 1/6, 1/6, 1/6`.
- Staircase total-variation defects from the `K`-chain, `3×3` at `(3,1,2)`: `RDRD = DRDR = 1874214125027/58529242968768`; `RRDD = DDRR = 381233308277/21948466113288`; `RDDR = DRRD = 3021054877865/117058485937536`. At `(5,2,4)`: `603989722568508979/30035851924783781538`; `113047203771057118/10664903944307284749`; `1686264713485074893/105125481736743235383` (same pairing).
- Snake proper, `3×3` columns 0, 1, 2: at `(3,1,2)` `0`, `3161/7227792`, `3583442207/7981260404832`; at `(5,2,4)` `0`, `104792291/623922798807`, `45687143997705515/267592135329891871884`. `4×3` columns at `(3,1,2)`: `3583442207/7981260404832`, `23960429927/34827318130176`, `3583442207/7981260404832`; at `(5,2,4)` `45687143997705515/267592135329891871884`, `36156719468443362521/135401620476925287173304`, `45687143997705515/267592135329891871884`.
- Mirror class on `2×3` at `(3,1,2)`: differs on `32616` of `46656` configurations, total variation `2764753/79505712`.
- Constant rule `(2,2,2)`: every staircase and snake-column defect `0`; the mirror law equals `μ_P`.

## Verified stdout (final runner, unmutated)

`TOTAL: PASS=38 FAIL=0`; families A1–A5, B1–B6, C1–C5, D1–D7, E1–E10, F1–F4, G1 all PASS; the five N5 lines printed (`per_element`, `per_site`, `per_mode`, `per_block` executed; `lattice_wide` not claimed).

## Mutation census (23 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha 73ae26a5…)

| mutation | expected | observed | PASS | FAIL | failing checks |
|---|---|---|---|---|---|
| `extension_count_wrong` | B | B | 37 | 1 | B1 |
| `recorded_set_forged` | B | B | 37 | 1 | B2 |
| `nonmonotone_order_accepted` | B | B | 37 | 1 | B6 |
| `antidiagonal_sweep_accepted` | B | B | 37 | 1 | B5 |
| `bridge_identity_broken` | C | C | 37 | 1 | C1 |
| `transpose_symmetry_broken` | C | C | 37 | 1 | C3 |
| `product_formula_mismatch` | C | C | 37 | 1 | C4 |
| `asymmetric_bridge_symmetry_forged` | C | C | 37 | 1 | C2 |
| `column_chain_forged` | D | D | 37 | 1 | D2 |
| `corner_law_wrong_denominator` | D | D | 37 | 1 | D4 |
| `corner_independence_forged` | D | D | 37 | 1 | D5 |
| `diagonal_pair_law_wrong` | D | D | 37 | 1 | D6 |
| `row_kernel_wrong` | D | D | 37 | 1 | D1 |
| `staircase_claimed_chain` | E | E | 37 | 1 | E2 |
| `mirror_law_equal_claimed` | E | E | 37 | 1 | E4 |
| `snake_column_claimed_chain` | E | E | 37 | 1 | E7 |
| `snake_row_kernel_not_invariant` | E | E | 37 | 1 | E5 |
| `minimal_staircase_conditional_off` | E | E | 37 | 1 | E1 |
| `constant_rule_defect_claimed` | E | E | 37 | 1 | E9 |
| `claim_static_equals_formation` | F | F | 37 | 1 | F2 |
| `claim_all_orders_same_law` | F | F | 37 | 1 | F2 |
| `claim_staircases_chains` | F | F | 37 | 1 | F2 |
| `claim_unilateral-field_in_theorem` | F | F | 37 | 1 | F3 |

23 of 23 mutations fail in exactly their expected family.

Every mutation exits 1 and fails exactly one check in its declared family; the three F-family claim injections are caught by the forbidden-phrase scan (F2) and the name injection by the section scan (F3). Raw per-mutation stdout in the seat's scratch directory (`census/<mutation>.txt`).

## Supervisor fold (2026-09-07) — final certificate before the checker

- Line-by-line review of the runner (901 lines) and the note (578 lines): the P6 algebra re-derived (`P(c | c, c) = K(c → c) Σ_a K(c → a)^2/(K^2)(a, c) ≥ K(c → c)` by Cauchy–Schwarz, equality iff `K(c → ·) = (K^2)(c → ·)`, which forces `p = q = r` through the orthogonal and parallel orbit equalities); the P5 partial sums checked in the corrected order; the runner's surname needle assembled from character codes (no label in the runner); F3 verified.
- Fold: the certified stdout was 6,031 characters (31 over the cap) — the `lattice_wide` N5 line and the scope line shortened to 5,989; the mutation `claim_unilateral-field_in_theorem` renamed `claim_author_in_theorem`. Cache re-pinned: runner sha256 `5104a93e01aa413390030eeb8193040e203a0646910461de9b0af00d7400407e`, input fingerprint `1a49b041364505ca04c08d5a2ea09b76fe03b3eab5f4d3eb1fa17d6e6d8e51cf`, exit 0, elapsed 40.55 s, `TOTAL: PASS=38 FAIL=0`.
- Gates on the final tree: vocab lint 0; pipeline PASS (`graph_delta=acknowledged`, two passes: the first rebuilds the citation graph and rewrites the manifest, the second acknowledges it); changed-evidence `checked=5 failures=0`; audit_lint strict OK; `git diff --check` clean; manifest 4765 nodes, 11868 edges (+1 node).

## Final census (23 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha 5104a93e…)

| mutation | expected | observed | FAIL count | failing checks | exit | in-family |
|---|---|---|---|---|---|---|
| `extension_count_wrong` | B | B | 1 | B1 lin | 1 | yes |
| `recorded_set_forged` | B | B | 1 | B2 eve | 1 | yes |
| `nonmonotone_order_accepted` | B | B | 1 | B6 the | 1 | yes |
| `antidiagonal_sweep_accepted` | B | B | 1 | B5 the | 1 | yes |
| `bridge_identity_broken` | C | C | 1 | C1 P2: | 1 | yes |
| `transpose_symmetry_broken` | C | C | 1 | C3 P3: | 1 | yes |
| `product_formula_mismatch` | C | C | 1 | C4 P2: | 1 | yes |
| `asymmetric_bridge_symmetry_forged` | C | C | 1 | C2 r(s | 1 | yes |
| `column_chain_forged` | D | D | 1 | D2 P4: | 1 | yes |
| `corner_law_wrong_denominator` | D | D | 1 | D4 P5: | 1 | yes |
| `corner_independence_forged` | D | D | 1 | D5 P5: | 1 | yes |
| `diagonal_pair_law_wrong` | D | D | 1 | D6 E4 | 1 | yes |
| `row_kernel_wrong` | D | D | 1 | D1 the | 1 | yes |
| `staircase_claimed_chain` | E | E | 1 | E2 P6 | 1 | yes |
| `mirror_law_equal_claimed` | E | E | 1 | E4 P7( | 1 | yes |
| `snake_column_claimed_chain` | E | E | 1 | E7 P7( | 1 | yes |
| `snake_row_kernel_not_invariant` | E | E | 1 | E5 P7( | 1 | yes |
| `minimal_staircase_conditional_off` | E | E | 1 | E1 P6: | 1 | yes |
| `constant_rule_defect_claimed` | E | E | 1 | E9 the | 1 | yes |
| `claim_static_equals_formation` | F | F | 1 | F2 the | 1 | yes |
| `claim_all_orders_same_law` | F | F | 1 | F2 the | 1 | yes |
| `claim_staircases_chains` | F | F | 1 | F2 the | 1 | yes |
| `claim_author_in_theorem` | F | F | 1 | F3 the | 1 | yes |
in-family: 23/23

## Refuting checker and the second fold (2026-09-07) — final certificate

- Checker (Opus 5; `CHECKER_block05_findings.md`): FIX FIRST on one sentence — the P7(b) mechanism sentence, forbidden by the contract's addendum A1 and false (site `(1,0)` of the `3×3` snake records two neighbors); two wording items (staircase definition; P4's infinite-strip wording). Everything else confirmed on direct summations (all four block positions of `3×3` by full `6^9` summation; every literal verbatim; the P5 and P6 proofs re-derived; 12 mutations in family).
- Fold: the sentence deleted; staircases defined from any site; P4 stated for finite initial segments; the Review record carries the checker's verdict and the independence class. Cache re-pinned: runner sha256 `5104a93e01aa413390030eeb8193040e203a0646910461de9b0af00d7400407e` (unchanged), input fingerprint `515e1b01a3b5cc9da4b062b9f60c431fc0b288d673df09c474254f8ce9c467ee`, exit 0, elapsed 41.86 s, `TOTAL: PASS=38 FAIL=0`; note 591 lines, vocab lint 0; the census (23/23) stands at the unchanged runner sha. Gates re-run on the final tree: pipeline PASS, changed-evidence `checked=5 failures=0`, audit_lint strict OK, diff --check clean.
