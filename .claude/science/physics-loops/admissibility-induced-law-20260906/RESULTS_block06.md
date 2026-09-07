# RESULTS — block 06 (Fable primary seat; Opus contract lens before the build; Opus refuting checker pending), 2026-09-07

## Headline

On the open-boundary static strips of widths 4 and 5 (1296 and 7776 row states; 38 and 178 orbits under the row symmetry group of order 48), the deep-row pair-parallel probabilities of the edge pair and of the innermost pair are enclosed in exact rational intervals of width below `10^-50`, at both declared triples, by an elementary route that needs no algebraic field: the orbit quotient `Q` is self-adjoint for the weights `|O| A_O` (S2, proved from block 02's F1 and the symmetry of `φ`; executed on every orbit pair), so the two-sided ratio bounds enclose the Perron root, the trace bound `λ_2^2 ≤ tr(Q^2) − lo^2` controls every other eigenvalue, the residual–gap bound controls the angle between `Q^40 1` and the Perron vector, and one Cauchy–Schwarz step encloses the statistic (S3). Every enclosure excludes the formation value `f = p/(p+q+4r)` by more than `10^-3` (widths 2, 3, 4, 5; S5), and the innermost pair is strictly more often parallel than the edge pair at widths 4, 5. The Krylov dimension of `Q` on `1` is `8, 30, 16, 111`, with the integer dependency `m_1(Q) 1 = 0` verified exactly on every orbit at all four cases by the runner itself (the degree-111 polynomial with 526-digit coefficients in about ten seconds by a multi-modular search plus integer verification); `m_1` is irreducible at degrees 8, 30, 16, and at degrees 8 and 16 the statistics are identified as algebraic numbers by their minimal polynomials (S4). Nothing about wider strips, the plane, monotonicity in the width, or a physical order.

## Run record

- Runner `scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py`: 34 checks in families A (5), B (5), C (7), D (7), E (4), F (5), G (1); 26 declared mutations (4 B, 6 C, 9 D, 3 E, 4 F). Baseline about 60 s uncontended (the largest items: the width-5 quotient builds, the degree-111 modular solve, the `n = 33` full-state boundary check at width 5 through the tensor structure of `V`, the degree-30 Sturm counts).
- Control reproduction before any theorem sentence (own code, scratch `control_repro.py`, 23 s): orbit counts 38/178; Krylov dimensions 8/30/16/111 with the exact dependency verified on all orbits at every case; `λ_1` to 18 digits at all four cases; `tr(Q^2)` at all four; the 22-digit enclosures of `s_edge` and `s_inner` at all four; the ratio bounds `0.05538, 0.03301, 0.06932, 0.04150`; the innermost sector values at `W = 5`, `(3,1,2)`, `n = 3, 5, 9, 17, 33, 65` (`n = 33`: `0.2562896288160817584176711…`, `1.49 × 10^-25` from the enclosure). All equal to the supervisor's controls.
- Note `docs/ADMISSIBILITY_RULE_STATIC_STRIP_WIDTHS_4_5_RIGOROUS_ENCLOSURE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`: 634 lines; `vocab_lint --report-only` 0 violations; the classical names appear only in Prior art, Imports and the verbatim third fence in Boundaries (runner F4 strips that fence before scanning Boundaries).

## Defects fixed while executing

- First full run: the `--exact` printing of the field image crashed on Python's 4300-digit integer-to-string limit; the limit is lifted at import and the image is printed as 40-digit outward labels with the coefficient counts and digit sizes instead of the raw rationals.
- The E3 literal check first demanded `floor = 54437` for the width-4/width-5 difference of `s_inner`; the exact interval difference is `[5.4436…, 5.4437…] × 10^-6` (and `[1.8169…, 1.8170…] × 10^-7` for `s_edge`), so the contract's `5.4437`, `1.8170` are the upper (rounded-up) labels; the check and the note's S5 say so.
- The E4 detail string carried the four ratio labels as literals, which the runner's own F3 (float-literal scan) and F5 (every decimal from `dec()`) flagged; the labels are now produced by `dec(…, 5, up=True)` from the exact rationals. The F3 scan's own lines named the array library and matched themselves; the word is assembled from parts on marker lines.
- The note used "certificate" twice ("the rank certificate", "the resolution certificate"); the lane's forbidden scan is a substring match on the family of that word, so both were reworded.

## Could-not list

- The identification of the statistics as algebraic numbers is executed at Krylov degrees 8 and 16 only; at degree 30 (width 4, `(5,2,4)`) it was not attempted (the contract scopes it to `d ≤ 16`), and at degree 111 neither factorization nor root isolation is attempted; the S3 enclosure stands alone there.
- Irreducibility of `m_1` at degree 111 is not claimed; the polynomial is verified exactly and nothing else.
- `s_inner` is a distinct statistic at two widths only; the width-4/width-5 differences are two numbers, not a law.
- The boundary check with the single record `P(e_y)` on both end rows is executed on the full state through the tensor structure of `V` (not in the sector, where a single record is not `G`-invariant); the sector version uses the orbit-averaged record. Both are within `10^-6` of the enclosures at `n = 33`; the contract's "(sector)" wording is read as the latter.
- The refuting checker seat has not yet run.

## Modelling choices (declared, not physics)

- Menu order, orbit weights, `A`, `V`, `T` as in block 02; the group as the 24 signed axis permutations of determinant `+1` (computed by the Leibniz formula) times the row reversal; orbits by the images of each row.
- The power `k = 40`; the square-root scale `10^80` (integer square root plus one, over the scale) for `λ_2bound`, `r` and `√2`; enclosures `[s(y) − 2ε, s(y) + 2ε]` with `ε = √2 r/δ`.
- The Krylov dimension by an incremental reduced echelon form modulo `2^61 − 1` and `2^89 − 1` (both must agree at each step); the integer coefficients of `m_1` by a multi-modular Gauss–Jordan solve on `d` rows independent modulo `2^61 − 1` with primes of 512 bits (enough that their product exceeds `2 (1 + ⌈hi⌉)^d`), symmetric CRT, then the exact integer verification of `m_1(Q) 1 = 0` on every orbit — the verification is the proof, the search is not.
- The resultant `Res_λ(m_1, y D − N)` by exact evaluation at `y = 0, …, d` (univariate integer resultants) and Lagrange interpolation over `Q`; `N`, `D` scaled to integer coefficients by their common denominator (the ratio is unchanged).
- The full-state transfer as `T v = φ^{⊗W} (A ∘ v)` and `a T = A ∘ (φ^{⊗W} a)` (mode-by-mode application; checked against the explicit `T` at width 4 on three vectors).
- The finite-`n` sequence `n = 3, 5, 9, 17, 33, 65` in the sector; the end-record check at `n = 33`.
