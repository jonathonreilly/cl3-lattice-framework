# RESULTS — block 05 (Fable primary seat; Opus contract lens before the build; Opus refuting checker pending), 2026-09-07

## Headline

Every linear extension of the product partial order on a rectangle — every order in which each site waits for its left and above neighbors — gives the same formation law `μ_P`, for every nearest-neighbor rule (P1: the recorded set of every site is `{left, above}`; the 5, 42, 462 extensions of `2×3`, `3×3`, `3×4` executed, 24024 counted on `4×4`). Under `μ_P` every row and every column is the path chain `p_0` (P4), every `2×2` block carries the corner law `π(c,b,a,d) = (1/6) K(c,a) K(c,b) K(a,d) K(d,b)/K^2(a,b)` with the two neighbors of a corner independent given it (P5, proved from block 02's telescoping partial sums with the `n`-row reduction; executed at all 4 block positions of `3×3` and all 6 of `3×4`), and no staircase with a turn is a Markov chain at any positive triple with `p, q, r` not all equal (P6, proved from P5 by a Cauchy–Schwarz step; the minimal staircase's conditional `227/858` against `1/4` at `(3,1,2)`; the six staircases of `3×3` executed with exact defects; `P(c|c,c) > K(c→c)` on all 210 non-constant triples of `{1..6}^3`). The boundary: the mirror class differs from `μ_P` on 32616 of 46656 configurations of `2×3`; the snake proper keeps `p_0` rows and `(1/6) K` vertical pairs but on `3×3` only column 0 is a chain (defects `0`, `3161/7227792`, `3583442207/7981260404832`) and on `4×3` no column is (P7, executed). No order is selected as physical.

## Run record

- Runner `scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py`: `TOTAL: PASS=38 FAIL=0`, 23 declared mutations (4 B, 4 C, 5 D, 6 E, 4 F), unmutated stdout 5,992 characters, baseline 40.5 s (integer numerators over common denominators in the row transfers; the `2×4`/`4×2` transpose check on 1,679,616 configurations is the largest single item).
- Cache: runner sha256 `73ae26a5dfaf71694fa299d8734cafbf74b7eebc8ce2e84a7e7d8daee10a1f22`, input fingerprint `39ea974b711e25e87a9afeeb0507749f8db1ac34e398c7fc3fc285de793f503d`, exit 0, elapsed 40.48 s, written by `execute_and_write_cache(<runner>, 900)` after the final edit.
- Note `docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md`: 572 lines; `vocab_lint --report-only` 0 violations; the literature name appears in the Prior art and Imports sections only (checked by the runner's F3 with the needle assembled from character codes, so the runner source carries no such label).
- Control reproduction before any theorem sentence (own code, scratch `control_repro.py`): bridge identity, the 5-extension law equality on `2×3`, the counts 5/42/462/24024, the `3×3` column chain, the corner law at two block positions, the RDRD staircase defect, `227/858` vs `1/4`, the snake `3×3` defects `0`, `3161/7227792`, `3583442207/7981260404832`, the mirror count 32616 of 46656, and the `4×3` snake with no column a chain — all equal to the supervisor's controls; 1.2 s.

## Defects fixed while executing

- The runner's own `N(` scan tripped on the block-01 fragment `A_k = N(x_k)`; replaced by the fragment `FORMATION law of a rule for a formation order` (present in block 01's note across a line break; the check normalizes whitespace).
- The diagonal-pair check first asserted `(1/6) K^2 ≠ (1/6) K` entrywise and failed at `(3,1,2)`: `K^2` and `K` agree on the orthogonal orbit exactly when `p + q = 2r`, which holds there (`2r(p+q+r) = r(p+q+4r)`). The check now states the inequality as a statement about laws and executes the orbit fact at both triples (D6); the note records it as a remark.
- Unmutated stdout was 6,524 characters; detail strings and the N5 lines were shortened to 5,992.
- The census helper's argument order was wrong on the first launch (the xargs form passed the directory as the mutation name); corrected, no runner change.

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
