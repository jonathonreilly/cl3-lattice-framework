# Block 05 — the Pickard structure of the monotone-order formation law: rows and columns are path chains, the corner law, and the class boundary (2026-09-07)

Branch `physics-loop/admissibility-induced-law-block05-pickard-structure-monotone-class-20260907`, cut from block 04's tip `726bafb889` (PR #8002); stacked PR. Seat profile: supervisor controls (done: `specs/supervisor_control_block05_pickard.py`, `specs/supervisor_control_block05_snake.py`), Opus contract refuter lens BEFORE the primary, Fable primary, Opus refuting checker, supervisor fold. Queue origin: the block-02 refresh, item 2 ("rows AND columns are path chains; prove the column statement from the corner-pair condition; classify the monotone-order class").

## Named readings and premises (from blocks 01–03; nothing new adopted)
The six-projector menu, the covariant positive product rule with symmetric `φ` (orbit weights `(p, q, r)`, declared triples `(3, 1, 2)` and `(5, 2, 4)`), the records-only reading, block 01's formation law `μ_σ(v) = Π_k r(v_{x_k} | v restricted to A_k)` with `A_k` the neighbors recorded when `x_k` forms and `r(s | ∅) = 1/6`; block 02's strip `S_{W,n}` (rows `i = 0..n−1`, columns `j = 0..W−1`), `K(a → b) = φ(a, b)/Z_1`, `p_0`, `P`, Theorem E (E1: `Z_2 = Z_1^2 K^2`; E2; E3: `p_0 P = p_0`; E4: the pair laws and the partial sums). No order is selected as physical.

## Declared objects
- The product partial order on the sites of `S_{W,n}`: `(i', j') ≤ (i, j)` iff `i' ≤ i` and `j' ≤ j`. A **monotone order** is a linear extension of it (a total order in which every site follows its left and above neighbors). The row sweep, the column sweep, the diagonal and antidiagonal sweeps are monotone orders; the boustrophedon (snake) is not.
- `μ_P`: the formation law of any monotone order (Theorem P1 shows it is one law).
- The **bridge**: `β(s | a, b) = K(a → s) K(s → b) / (K^2)(a, b)` — the conditional law of the middle point of a two-step `K`-chain given its ends.
- The **corner law** on a `2 × 2` block with top-left `c`, top-right `b`, bottom-left `a`, bottom-right `d`: `π(c, b, a, d) = (1/6) K(c → a) K(c → b) K(a → d) K(d → b) / (K^2)(a, b)`.
- The four **corner classes**: the linear extensions of the product order with the origin at each corner of the rectangle (the reflections of the monotone class); the **snake**: rows in order, alternating direction.
- A **staircase**: a path of right and down steps from the top-left site.

## Theorems (every number is in the controls)
**P1 (the monotone-order class is one law).** In every linear extension of the product order, site `(i, j)` forms with exactly the recorded neighbors `(i, j−1)` (if `j > 0`) and `(i−1, j)` (if `i > 0`): the left and above neighbors precede it, the right and below neighbors follow it. Hence every monotone order gives the same formation law `μ_P`. Executed: all `5` linear extensions of `2 × 3` give the same law on all `6^6` configurations; the recorded-neighbor sets are `{left, above}` for all `42` extensions of `3 × 3` and all `462` of `3 × 4` (counts `5, 42, 462, 24024` for `2×3, 3×3, 3×4, 4×4`, the standard Young tableaux of the rectangle).

**P2 (the formation rule is the bridge).** For two recorded neighbors, `r(s | a, b) = φ(s, a) φ(s, b)/Z_2(a, b) = K(a → s) K(s → b)/(K^2)(a, b) = β(s | a, b)` by E1. So `μ_P(v) = (1/6) Π_{j≥1} K(v_{0,j−1} → v_{0,j}) Π_{i≥1} K(v_{i−1,0} → v_{i,0}) Π_{i,j≥1} β(v_{ij} | v_{i,j−1}, v_{i−1,j})`. Executed on all `216` triples at `(3,1,2)`.

**P3 (transpose symmetry).** `μ_P^{(n×W)}(v) = μ_P^{(W×n)}(v^T)`: the product formula of P2 is symmetric under `(i, j) ↔ (j, i)` because `β(s | a, b) = β(s | b, a)` (`K` and `K^2` symmetric) and the two boundary chains exchange. Executed: `2 × 3` against `3 × 2` on every configuration.

**P4 (columns are path chains).** Every column of `S_{W,n}` under `μ_P` has the law `p_0` (the `K`-chain from the top with the uniform start): apply E3 to the transposed strip (P3), whose rows are the original columns. On the infinite strip and the quadrant the column law is the `K`-chain by the projective-limit and restriction arguments of E3. Executed: every column of `3 × 3` (three-site chains, by the row transfer with projections) and of `2 × 3`.

**P5 (the corner law and the corner independence).** For every `2 × 2` block of `S_{W,n}` (rows `i−1, i`, columns `j−1, j`, `i, j ≥ 1`) the marginal of `μ_P` is `π(c, b, a, d)`; hence `a` and `b` are conditionally independent given the corner `c`, with `P(a, b | c) = K(c → a) K(c → b)`, and `d` given `(a, b)` is the bridge. Proof: by E4 the vertical pair `(c, a)` at column `j−1` has the law `(1/6) K(c → a)`; the factors of columns `≥ j` depend on columns `< j` only through `(c, a)`; the column-`j` factors are `K(c → b)` (row `i−1`) and `β(d | a, b)` (row `i`); the columns `> j` sum to one. Executed: both `2 × 2` blocks of `2 × 3` on all `1296` entries; all three blocks of the two-row joint at `W = 4` (`1296^2` entries).

**P6 (rows and columns, not staircases; executed).** The staircase `(0,0)(0,1)(1,1)(1,2)(2,2)` and the staircase `(0,0)(1,0)(1,1)(2,1)(2,2)` of `3 × 3` are NOT `K`-chains under `μ_P` (executed; the exact defect recorded). The Markov structure of `μ_P` is along rows and columns; nothing is claimed for other monotone paths beyond these witnesses.

**P7 (the class boundary).** (a) The four corner classes give four laws, the reflections of `μ_P`; `μ_P` differs from its left-right mirror (executed on `2 × 3`: the laws differ; the corner law's `K^2` denominator sits on the anti-diagonal pair `(a, b)` and is not carried to the other diagonal by the mirror); each corner class has rows and columns as `p_0`-chains (by symmetry). (b) The snake: its rows are `p_0`-chains and all vertical pairs carry `(1/6) K` (E3, E4 with the reversed row kernel `P_rl`, which also satisfies `p_0 P_rl = p_0`), but on `3 × 3` its columns `0` and `1` are not `K`-chains while the turning column `2` is (executed): the column theorem is a property of the monotone class, not of every row-by-row order.

## Forbidden
"the physical order", "washes out", "unique on the lattice", "Pickard" outside Prior art/Imports, "certified", "phase transition", "several static laws"; no claim that the formation law equals the static law (block 01–02 say it does not); no claim about non-monotone orders beyond the snake witness; no claim that staircases fail in general beyond the two witnesses.

## V1–V5 (advance)
V1: the block-02 refresh names it (item 2). V2: new — P1's class statement, P2–P5 as proved theorems with exact executions, P6/P7 as exact witnesses. V3: not an audit-lane object. V4: non-trivial — the column theorem and the corner law are the complete finite-dimensional description of `μ_P`'s row/column structure. V5: extends block 02's Theorem E (rows) to columns and blocks; not a variant.
