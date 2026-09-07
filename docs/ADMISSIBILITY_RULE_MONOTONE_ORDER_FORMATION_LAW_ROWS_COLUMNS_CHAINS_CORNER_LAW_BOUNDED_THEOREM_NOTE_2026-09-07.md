---
claim_id: admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule at the declared exact weight triples (3, 1, 2) and (5, 2, 4), under the records-only reading, on the rectangles S_{W,n}, the infinite strip and the quadrant: every linear extension of the product partial order (every monotone order) gives one formation law mu_P, for every nearest-neighbor rule (P1, proved; executed on the 5, 42, 462 extensions of 2x3, 3x3, 3x4 and counted at 24024 on 4x4); its two-neighbor factor is the bridge of a two-step K-chain (P2, from block 02's E1); mu_P is transpose-symmetric (P3); every row and every column of mu_P is the path chain p_0, on finite rectangles by the row transfer and on the infinite strip and the quadrant by block 02's limit arguments (P4); every 2x2 block carries the corner law pi(c, b, a, d) = (1/6) K(c,a) K(c,b) K(a,d) K(d,b) / K^2(a,b), in which a and b are independent given the top-left corner c (P5, proved by the partial sums of block 02's E3 with the n-row reduction; executed at every block position of 3x3 and 3x4); no right/down staircase with a turn is a first-order Markov chain in its site values at any positive triple with p, q, r not all equal (P6, proved from P5; the minimal staircase's conditional 227/858 against 1/4; all six staircases of 3x3 executed); the corner classes: opposite corners give identical laws on every finite rectangle (proved from the edge/plaquette product); at each declared nonconstant triple the four actual corner orders on 2x3 give exactly two distinct laws (the mirror differs from mu_P on 32616 of 46656 configurations), and the snake keeps p_0 rows and (1/6) K vertical pairs but on 3x3 only column 0 is a chain and on 4x3 no column is (P7, executed). No order is selected as physical; nothing about the static law beyond blocks 01-02; outside the top-left class only the finite opposite-corner identity and declared distinctness/snake witnesses; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py
---

# The formation law of every monotone order is one law whose rows and columns are path chains: the corner law and finite boundary witnesses

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py`](../scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.txt`](../logs/runner-cache/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.txt)

## Result up front

Take the same fixed rule as before, the one that gives the odds for a new
record from the records its neighbours already carry, and lay records down on
a rectangular patch of lattice in any order you like, provided each site waits
for the site above it and the site to its left before it forms. Every such
order gives exactly the same pattern law. In that law every row and every
column, taken by itself, looks exactly like a single chain of records; any
two-by-two square has one explicit law, in which the two sites next to a
top-left corner are independent of each other once that corner is known.
For positive nonconstant orbit weights, a path made only of right/down steps
that turns is not a first-order Markov chain in its site values. A path
through the same square in the order bottom-left → top-left → top-right is
a chain, so the direction restriction matters. Orders that do not wait for
the site above — the snake, which runs the rows back and forth — keep the
rows as chains and can lose column-chain structure; one column survives on
the executed three-by-three square. Nothing here says which order is the physical
one, and nothing is said about the static pattern law beyond what the earlier
notes already separated.

Exactly: for the product rule with orbit weights `(p, q, r)` on the rectangle
`S_{W,n}` (rows `i = 0..n−1`, columns `j = 0..W−1`, nearest-neighbor edges,
open boundary) under the records-only reading, every linear extension of the
product order `(i', j') ≤ (i, j) iff i' ≤ i and j' ≤ j` has the same recorded
sets `A_{(i,j)} = {(i, j−1), (i−1, j)} ∩ S_{W,n}`, hence the same formation law
`μ_P` for every rule (Theorem P1; the `5`, `42`, `462` extensions of `2×3`,
`3×3`, `3×4` executed, `24024` counted on `4×4`). With
`K(a → s) = φ(s, a)/Z_1` and `Z_2 = Z_1^2 K^2` (block 02, E1), the two-neighbor
factor is the bridge `β(s | a, b) = K(a → s) K(s → b)/(K^2)(a, b)` (P2), so
`μ_P(v) = (1/6) Π_{j≥1} K(v_{0,j−1} → v_{0,j}) Π_{i≥1} K(v_{i−1,0} → v_{i,0}) Π_{i,j≥1} β(v_{ij} | v_{i,j−1}, v_{i−1,j})`,
which is symmetric under transposition (P3; `2×3` against `3×2` and `2×4`
against `4×2` executed on every configuration). Every row and every column of
`μ_P` is the path chain `p_0` (P4; every column of `3×3` and `3×4` executed as
a three-site joint), every `2×2` block has the corner law
`π(c, b, a, d) = (1/6) K(c → a) K(c → b) K(a → d) K(d → b)/(K^2)(a, b)` with
`P(a, b | c) = K(c → a) K(c → b)` (P5; all `4` block positions of `3×3` and all
`6` of `3×4`), and along the minimal staircase `(0,0)(0,1)(1,1)` the
conditional `P(d | c, b) = Σ_a K(c → a) K(a → d) K(d → b)/(K^2)(a, b)` is
`227/858` against `K(b → d) = 1/4` at `(3, 1, 2)`, `c = b = d = P(e_x)`, so no
staircase with a turn is a Markov chain at any positive triple with `p, q, r`
not all equal (P6; all six staircases of `3×3` executed with exact defects).
The mirror class differs from `μ_P` on `32616` of `46656` configurations of
`2×3`; the snake proper (row 0 left to right, row 1 right to left, …) has rows
`p_0` and vertical pairs `(1/6) K`, but on `3×3` its columns have total
variation defects `0`, `3161/7227792`, `3583442207/7981260404832` from the
`K`-chain and on `4×3` no column is a chain (P7). Executed with exact
arithmetic: 39 focused checks. The original 23-mutation census is historical;
the review correction adds and executes a corner-order reversal control.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 02's refresh, item 2: rows and columns as path chains; the column statement from the corner-pair condition; the monotone-order class. The owner's sequencing gate (2026-08-26): what the Admissibility rule induces on the infinite lattice is unidentified; the parked statistical-bridge decision wakes on 'the committed-action identification lands', which this note does not fire"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "next block: the static law of the plane and uniqueness on Z^3 (blocks 03-04's contraction lanes); consumers: the record-matter lane's formation-order supply (the class of orders with one law), the parked statistical-bridge decision material (docs/repo/DEFERRED_DECISIONS.md entry 1, read-only)"
conditional_surface_status: "exact on the declared rectangles, menu and triples; P1 is proved for every rectangle and every rule; P2, P4 and P5 are proved for every rectangle with symmetric positive phi having common row sum Z1, including the declared isotropic orbit rule; P3 holds for arbitrary positive phi with locally normalized boundary factors; these claims are executed on 2x3, 2x4, 3x3, 3x4; P6 is proved for right/down staircases in site values under the declared positive product-rule monotone law when p, q, r are not all equal; P7 proves opposite-corner equality on finite rectangles and executes distinctness only on the declared 2x3 witnesses, with finite snake witnesses; conditional on the records-only reading; no static-law statement, no plane, no order selected as physical"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "P1 is a two-line proof about recorded sets executed on 509 linear extensions; P2-P5 are proved from block 02's E1-E4 by the same telescoping partial sums and executed exactly on the declared rectangles; P6 is proved from P5 by an elementary inequality and executed on the six staircases of 3x3 and on 210 non-constant triples; P7 combines the finite-rectangle opposite-corner identity with executed distinctness and snake witnesses; nothing infinite-volume beyond block 02's limit arguments, nothing about the static law, the plane, a physical order, the Born form or the bridge is claimed."
```

## Premises and declared objects

The only scientific dependencies are the four axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and the two
upstream notes
[`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)
(block 01) and
[`ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md)
(block 02), both proposed and unaudited, whose definitions are restated here
where used. Nothing new is adopted. The axiom sentences used, verbatim (runner
A2):

- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and "For
  each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form." — "records are permanent" — "Only records are
  readable." — "A site with no record cannot be read."

**Menu, rule, kernel (blocks 01–02, restated).** `M` = the six projectors
`P(±e_a)`, indexed `P(+e_x), P(−e_x), P(+e_y), P(−e_y), P(+e_z), P(−e_z)`; the
24 proper cubic rotations act transitively as signed axis permutations;
ordered pairs fall into the parallel, antiparallel and orthogonal orbits. The
product rule: `r(s | η) ∝ Π_{y∈A} φ(s, η_y)` over the recorded neighbors `A`,
with `φ` symmetric, isotropic and positive with orbit values `(p, q, r)`;
`r(s | ∅) = 1/6`. Declared triples `(3, 1, 2)` and `(5, 2, 4)`; the constant
triple `(2, 2, 2)` as the boundary (the variation clause: `p, q, r` not all
equal, the extensional reading restricted to the declared menu, block 01 B4).
`Z_1 = p + q + 4r`, `K(a → s) = φ(s, a)/Z_1` (symmetric, doubly stochastic),
`Z_2(a, b) = Σ_s φ(s, a) φ(s, b) = Z_1^2 (K^2)(a, b)` (block 02, E1). The
records-only reading (i) of block 01: an unrecorded neighbor contributes no
factor and is not a condition. The FORMATION law of an order
`σ = (x_1, …, x_N)` is block 01's `μ_σ(v) = Π_k r(v_{x_k} | v restricted to A_k)`
with `A_k = N(x_k) ∩ {x_1, …, x_{k−1}}` the neighbors recorded when `x_k`
forms. The axioms supply no order; no order is selected as physical.

**Rectangles.** `S_{W,n}` is the `n × W` grid, rows `i = 0..n−1` (downward),
columns `j = 0..W−1` (rightward), nearest-neighbor edges, open boundary (as a
window of `Z^3` the out-of-plane and out-of-rectangle neighbors carry no
records and contribute nothing under the records-only reading); the infinite
strip `S_W` has rows indexed by `N`; the quadrant has rows and columns indexed
by `N` (block 02, Theorem E). Row states `ρ ∈ M^W`; the path chain
`p_0(ρ) = (1/6) Π_{j≥1} K(ρ_{j−1} → ρ_j)`; the row-to-row kernel of the row
sweep `P(β → α) = K(β_0 → α_0) Π_{j=1}^{W−1} K(α_{j−1} → α_j) K(α_j → β_j)/(K^2)(α_{j−1}, β_j)`
(block 02, E2), with `p_0 P = p_0` (E3) and the pair laws (E4): every vertical
and horizontal nearest-neighbor pair `(1/6) K`, the diagonal pair
`(α_{j−1}, β_j)` the law `(1/6) K^2`.

**The product partial order and the monotone class.** On the sites of
`S_{W,n}`: `(i', j') ≤ (i, j)` iff `i' ≤ i` and `j' ≤ j`. A **monotone order**
is a linear extension of it: a total order in which every site follows its
left neighbor and its above neighbor. Members named here: the row sweep (rows
in order, each left to right), the column sweep (columns in order, each
downward), and the sweep by increasing `i + j` (any order within a level). The
sweeps by increasing `i − j` or `j − i` are NOT linear extensions (a site can
precede its left or its above neighbor: on `3×3` the `i − j` sweep forms
`(0, 1)` before `(0, 0)`, runner B5). The boustrophedon (**snake**: rows in
order, row 0 left to right, row 1 right to left, and so on) is not one either
(on `2×3` site `(1, 1)` forms after `(1, 2)` and before `(1, 0)`, runner B6).
`μ_P` is the formation law of any monotone order (P1: one law). The four
**corner classes** are the linear extensions of the product order with the
origin at each corner of the rectangle (the reflections of the monotone
class); the **mirror class** is the one with the origin at the top-right
(every site follows its right and above neighbors).

**The bridge and the corner law.** `β(s | a, b) = K(a → s) K(s → b)/(K^2)(a, b)`,
the conditional law of the middle point of a two-step `K`-chain given its
ends. On a `2×2` block with top-left `c`, top-right `b`, bottom-left `a`,
bottom-right `d`:
`π(c, b, a, d) = (1/6) K(c → a) K(c → b) K(a → d) K(d → b)/(K^2)(a, b)`.
A **staircase** is a path of right and down steps starting at any site of
the rectangle (the six staircases executed on `3×3` start at the top-left
site); a **turn** is a right step followed by a down step or a down step
followed by a right step; the **minimal staircase** is `(0,0)(0,1)(1,1)`
(sites `c, b, d`).
"Is a `K`-chain" for a list of sites means its joint law is
`(1/6) Π K(v_t → v_{t+1})` along the list; "is a Markov chain" means the
sequence of values along the list is Markov in that order with some kernel.

## Prior art and what is new

Block 01 (linked above) defines the formation law and proves the identity
and the classification; block 02 solves the row sweep on strips (E1–E4: the
two-neighbor normalizer `Z_2 = Z_1^2 K^2`, the row kernel `P`, the telescoping
invariance `p_0 P = p_0`, the pair laws) and names in its refresh, item 2,
the objects of this note: rows and columns as path chains, the column
statement from the corner-pair condition, the monotone-order class. The
classical reference is the unilateral Markov field of the lattice literature
(Pickard, 1977–1980, and the Markov-mesh constructions that followed): a
stationary field on the plane in which rows and columns are Markov chains,
any `2×2` square has a product-form law and the two neighbors of a corner are
conditionally independent given it. It is referenced once, here, by its
author's name, and nothing is taken from it: every statement below is proved
at the scope used from block 02's telescoping partial sums, with the
framework's own kernel `K` and its own two-neighbor factor, and the executed
numbers are the framework's. The contract lens's survey of this structure
(the refuter lens on block 05's contract, recorded in the pack's
`GOAL_block05.md` addendum) is the origin of the corrected snake statement
(A1), the theorem form of P6 (A2), the transposition-free route to the
infinite strip (A3), the `n`-row reduction in P5 (A4), the diagonal-sweep
definitions (A5) and the strengthenings of P1 and P3 (A7). No landed note
states any of P1–P7.

New here: the class statement P1 (one law for every linear extension, for
every rule); the bridge form of the two-neighbor factor (P2); the transpose
symmetry (P3); the column theorem (P4); the corner law with its conditional
independence (P5) and its `n`-row proof; the staircase theorem (P6) with an
elementary proof for every non-constant positive triple; the class boundary
witnesses (P7) with exact defects.

## Exact target and obligation graph

**Target.** On `S_{W,n}` for the declared isotropic positive orbit product
rule (so `φ` is symmetric with common row sum `Z_1`) under the records-only
reading: every monotone order has the one formation
law `μ_P` of the displayed product formula; every row and every column of
`μ_P` is the path chain `p_0`; every `2×2` block has the corner law `π`; and
no staircase with a turn is a Markov chain when `p, q, r` are not all equal.

| obligation | disposition |
|---|---|
| the recorded set of every site in every linear extension is `{left, above} ∩ S_{W,n}` (P1) | proved here (two lines); executed on the 509 extensions of `2×3`, `3×3`, `3×4` (B1, B2) and on the laws of `2×3` for three rules (B3, B4) |
| `Z_2 = Z_1^2 K^2` (block 02, E1); the bridge form of the two-neighbor factor (P2) | cited and re-executed on all 216 triples at both triples (C1) |
| the product formula equals block 01's definition (P2) | proved here; executed entrywise on `2×3` (C4) |
| the transpose symmetry (P3) | proved here from the product form; executed `2×3`/`3×2` and `2×4`/`4×2` (C3, C5) |
| the row kernel `P`, `p_0 P = p_0`, the pair laws (block 02, E2–E4) | cited; `P` re-executed against the definition (D1); rows of `3×3`, `3×4` re-executed (D3) |
| the column theorem on finite rectangles (P4) | proved here from P3 and E3; executed on every column of `3×3`, `3×4`, `2×3` (D2, D3) |
| the column theorem on the infinite strip and the quadrant (P4) | proved here by block 02's projective-limit and restriction arguments applied to finite rectangles, without transposing an infinite object |
| the corner law and its `n`-row reduction (P5) | proved here from E3's partial sums; executed at all 4 block positions of `3×3` and all 6 of `3×4` (D4–D6) |
| the two transfer schemes agree | executed (D7) |
| the minimal staircase's conditional from `π`; the inequality `P(c | c, c) > K(c → c)` for `p, q, r` not all equal (P6) | proved here (elementary); executed at `(3, 1, 2)` and on the 216 triples of `{1..6}^3` (E1, E10); the six staircases of `3×3` (E2, E3) |
| opposite corners give identical laws; the two reflection laws differ at the declared `2×3` triples; the snake's rows and columns (P7) | opposite-corner identity proved from the edge/plaquette product; all four actual corner laws compared as complete dictionaries (E11); finite defects (E4–E9) |
| the static law of the plane; uniqueness on `Z^3`; characterization of orders outside the corner classes beyond the snake witnesses | open; not this note |

The strongest missing lemma is a characterization of the orders outside the
monotone class whose columns are chains. Class membership is sufficient for
rows and columns by P4, but need not be necessary for row chains: the snake
is outside the class. Having row chains alone does not force column chains.
The missing characterization is not used by the target.

## Theorem P1 — the monotone-order class is one law

**Statement.** Let `σ` be any linear extension of the product order on
`S_{W,n}`. Then for every site `(i, j)` the recorded set is
`A_{(i,j)} = {(i, j−1) if j > 0} ∪ {(i−1, j) if i > 0}`. Hence every linear
extension gives the same formation law `μ_P(v) = Π_{(i,j)} r(v_{ij} | v on A_{(i,j)})`,
for every nearest-neighbor rule `r(· | η)` (block 01's definition uses only
the recorded sets and the rule).

*Proof.* The neighbors of `(i, j)` are `(i, j−1)`, `(i−1, j)` (below it in
the product order, so before it in every linear extension) and `(i, j+1)`,
`(i+1, j)` (above it, so after it). ∎ Executed: the `5`, `42`, `462` linear
extensions of `2×3`, `3×3`, `3×4` enumerated by recursion and `24024` counted
on `4×4` by memoized recursion — the standard Young tableaux of the
rectangle (B1); the recorded set of every site of every extension is
`{left, above} ∩ S_{W,n}` (B2); the full formation laws of the `5` extensions
of `2×3` on all `6^6` configurations coincide at both triples (B3), and also
for the sum rule `r(s | η) ∝ Σ_y φ(s, η_y)` and for block 02's asymmetric
`φ(a, b) = φ_{(3,1,2)}(a, b) + [a < b]` (B4: P1 uses nothing about the rule);
the `i + j` sweep is a member and the `i − j`, `j − i` sweeps are not (B5); the
snake is not (B6).

## Theorem P2 — the two-neighbor factor is the bridge

**Statement.** For symmetric positive `φ` with common row sum `Z_1`
(in particular the declared isotropic orbit rule), and two recorded
neighbors `a, b`:
`r(s | a, b) = φ(s, a) φ(s, b)/Z_2(a, b) = K(a → s) K(s → b)/(K^2)(a, b) = β(s | a, b)`.
Hence
`μ_P(v) = (1/6) Π_{j≥1} K(v_{0,j−1} → v_{0,j}) Π_{i≥1} K(v_{i−1,0} → v_{i,0}) Π_{i,j≥1} β(v_{ij} | v_{i,j−1}, v_{i−1,j})`.

*Proof.* `φ(s, a) = Z_1 K(a → s)` and `φ(s, b) = Z_1 K(s → b)` by symmetry of
`φ`; `Z_2(a, b) = Z_1^2 (K^2)(a, b)` is block 02's E1. The site `(0, 0)` has
no recorded neighbor (`1/6`); the sites `(0, j)`, `j ≥ 1`, and `(i, 0)`,
`i ≥ 1`, have one (`φ/Z_1 = K`); every other site has its left and above
neighbors (P1). ∎ Executed on all `216` triples `(a, b, s)` at both declared
triples (C1) and entrywise against block 01's definition on `2×3` (C4).

## Theorem P3 — transpose symmetry

**Statement.** `μ_P^{(n×W)}(v) = μ_P^{(W×n)}(v^T)` with `(v^T)_{ji} = v_{ij}`.
It holds for every positive `φ`, symmetric or not.

*Proof.* For arbitrary positive `φ`, write the one-neighbor transition as
`L(a → s) = φ(s, a)/Σ_t φ(t, a)`, normalized separately for each parent `a`.
The first row is the `L`-chain from `(0, 0)` rightward with uniform start,
and the first column is the `L`-chain downward; every other site carries
the locally normalized product factor of its left and above neighbors.
Within P2's symmetric common-row-sum family, `L = K`; outside that family
no common `Z_1` or uniform later-site marginal is asserted. Transposition
exchanges the two boundary chains and, at an
interior site, exchanges the roles of the left and above neighbors. The
two-neighbor factor `r(s | a, b) = φ(s, a) φ(s, b)/Σ_t φ(t, a) φ(t, b)` is
symmetric in `(a, b)` by the product form alone, whatever `φ`; this, and not
the symmetry of `K`, is the reason. ∎ Executed: `r(s | a, b) = r(s | b, a)`
on `216` triples for the asymmetric `φ` (C2); `2×3` against `3×2` on every
configuration at both triples and for the asymmetric `φ`, from block 01's
definition (C3); `2×4` against `4×2` on all `1679616` configurations by the
row-kernel form of the product formula, integer numerators over one
denominator (C5).

## Theorem P4 — rows and columns are path chains

**Statement.** For the symmetric positive common-row-sum product rule of
P2, under `μ_P` on `S_{W,n}` every row and every column has the
law `p_0` (the `K`-chain from its first site with the uniform start). On the
infinite strip `S_W` every row is `p_0` and every finite initial segment of
every column is the `K`-chain of its length; on the quadrant the same holds
for every finite initial segment of every row and of every column.

*Proof.* Rows: `μ_P` is the row sweep's law (P1), whose every row is `p_0`
by block 02's E3. Columns on finite rectangles: by P3 the column `j` of
`μ_P^{(n×W)}` is the row `j` of `μ_P^{(W×n)}`, which is `p_0` by E3 applied
to the transposed rectangle. Infinite strip: no infinite object is
transposed. For every `n` the column of `S_{W,n}` is the `K`-chain of length
`n`; the law of `S_W` is the projective limit of the `S_{W,n}` laws (E3: the
law of the first `n` rows is `μ_P` on `S_{W,n}`, later rows not entering
earlier conditionals), and the finite-`n` column laws are consistent
`K`-chains, so the column of `S_W` is the `K`-chain. Quadrant: the same
through E3's restriction lemma (every site's recorded neighbors lie in its
own column or to its left, so the width-`W` law restricted to the first `W'`
columns is the width-`W'` law) applied to finite rectangles. ∎ Executed:
every column of `3×3` (both triples) and of `3×4` as a three-site joint by the
middle-row contraction of the row transfer (D2); rows `1`, `2` of `3×3`,
`3×4` by the transfer and every row and column of `2×3` from the definition
(D3).

## Theorem P5 — the corner law and the corner independence

**Statement.** For the symmetric positive common-row-sum product rule of
P2, for every `2×2` block of `S_{W,n}` (rows `i−1, i`, columns
`j−1, j`, `i, j ≥ 1`) the marginal of `μ_P` is `π(c, b, a, d)`. Consequently
`P(c) = 1/6`, `P(a, b | c) = K(c → a) K(c → b)` (the two neighbors of the
corner are independent given it), `P(d | c, b, a) = β(d | a, b)`, and the
diagonal pair `(a, b)` has the law `(1/6) (K^2)(a, b)` (block 02's E4
recovered).

*Proof.* Three steps reduce the `n`-row rectangle to the two rows
`(i−1, i)`: (i) the law of row `i−1` is `p_0` for every `i` (E3, stationarity
above the block); (ii) the rows below `i` sum out to one, because each `P` is
row-stochastic; (iii) the joint law of rows `(i−1, i)` is `p_0(β) P(β → α)`,
because the row chain is Markov (row `i`'s conditional given all earlier rows
depends only on row `i−1`). Write `β` for row `i−1` and `α` for row `i`, with
`c = β_{j−1}`, `b = β_j`, `a = α_{j−1}`, `d = α_j`. The partial sums of E3's
telescoping proof (summing `β_0, …, β_{j−2}` in order; nothing to sum when
`j = 1`) leave the weight
`(1/6) Π_{1≤l≤j−1} K(α_{l−1} → α_l) · K(α_{j−1} → β_{j−1}) · K(β_{j−1} → β_j) · K(α_{j−1} → α_j) K(α_j → β_j)/(K^2)(α_{j−1}, β_j) · R`,
where `R` collects the factors of the columns `> j` (each `(K^2)(α_{l−2}, β_{l−1})`
produced by summing `β_{l−2}` cancels the column-`(l−1)` denominator).
Summing `α_0, …, α_{j−2}` — a `K`-chain with the uniform start; the columns
of `K` sum to one — leaves `(1/6) K(a → c)`, the vertical pair law of E4,
times the column-`j` factors `K(c → b)` (from `p_0(β)`) and
`β(d | a, b) = K(a → d) K(d → b)/(K^2)(a, b)` (from `P`), times `R`. The
factors of `R` depend on the columns `≤ j` only through `(α_j, β_j)`, and they
sum to one: summing `α_{W−1}, α_{W−2}, …, α_{j+1}` in that order, each
`Σ_{α_l} K(α_{l−1} → α_l) K(α_l → β_l) = (K^2)(α_{l−1}, β_l)` cancels the
column-`l` denominator (the conditional factors of the later-formed sites
sum to one), and then `Π_{l>j} K(β_{l−1} → β_l)` sums to one over
`β_{W−1}, …, β_{j+1}` (the rows of `K` sum to one). Hence the marginal on
`(c, b, a, d)` is `(1/6) K(c → a) K(c → b) K(a → d) K(d → b)/(K^2)(a, b) = π`. Summing `π`
over `d` gives `(1/6) K(c → a) K(c → b)` (the bridge sums to one), whence
`P(c) = 1/6` and the two conditionals; summing over `c` and `d` gives
`(1/6) (K^2)(a, b)`. ∎ Executed at all four block positions of `3×3` (both
triples, including the blocks in rows `(1, 2)`) and all six of `3×4` from
the computed block marginals, not from the formula (D4–D6). Remark (executed,
D6): `K^2` and `K` agree on the orthogonal orbit iff `p + q = 2r`, which
holds at `(3, 1, 2)` and not at `(5, 2, 4)`; the diagonal-pair law
`(1/6) K^2` differs from `(1/6) K` as a law at both triples.

## Theorem P6 — rows and columns, not staircases

**Statement.** Let `p, q, r > 0` be not all equal. Under `μ_P` on any
rectangle containing it, no right/down staircase with a turn is a first-order
Markov chain in its site values (in particular none is a `K`-chain). Among
right/down paths, the straight row and column paths are chains by P4 and
every path with a turn is covered by this negative. Non-monotone turning paths are outside this negative: summing P5
over `d` gives `(1/6) K(c → a) K(c → b)`, which by symmetry of `K` is
exactly the chain law `(1/6) K(a → c) K(c → b)` along `a → c → b`.

*Proof.* Along any staircase every consecutive pair is a horizontal or a
vertical nearest-neighbor pair, with the law `(1/6) K` and uniform site
marginals (E4). If the values along the staircase formed a Markov chain, its
kernel would be `K`, so at a turn `x_{k−1}, x_k, x_{k+1}` the conditional
`P(x_{k+1} | x_{k−1}, x_k)` would equal `K(x_k → x_{k+1})`. The three sites of
a turn are three sites of one `2×2` block, whose law is `π` (P5). For the
turn right-then-down (`c, b, d` in the block's labels),
`P(d | c, b) = Σ_a π(c, b, a, d)/((1/6) K(c → b)) = Σ_a K(c → a) K(a → d) K(d → b)/(K^2)(a, b)`;
for down-then-right (`c, a, d`) the same expression with `a` and `b`
exchanged (P3). At `c = b = d`:
`P(c | c, c) = K(c → c) Σ_a K(c → a)^2/(K^2)(a, c) ≥ K(c → c) (Σ_a K(c → a))^2/Σ_a (K^2)(a, c) = K(c → c)`
by the Cauchy–Schwarz inequality in the form `Σ x_a^2/y_a ≥ (Σ x_a)^2/Σ y_a`
(`y_a > 0`), with equality iff `K(c → a)/(K^2)(a, c)` is constant in `a`,
i.e. (both sum to one) iff `K(c → ·) = (K^2)(c → ·)`. On the three orbits
with `Z_1 = p + q + 4r`: `(K^2)(orth) = 2r(p + q + r)/Z_1^2` equals
`K(orth) = r/Z_1` iff `p + q = 2r`; `(K^2)(par) = (p^2 + q^2 + 4r^2)/Z_1^2`
equals `K(par) = p/Z_1` iff `q(q − p) + 4r(r − p) = 0`, which at
`r = (p + q)/2` reads `(q − p)(p + 2q) = 0`, i.e. `p = q`, hence `r = p`. So
equality forces `p = q = r`, and for `p, q, r` not all equal
`P(c | c, c) > K(c → c)`: the conditional at the turn is not `K`, and the
staircase is not Markov. ∎ Executed: `P(d | c, b)` from the corner law equals
the direct marginal on all `216` triples `(c, b, d)`, and at `(3, 1, 2)`,
`c = b = d = P(e_x)`, it is `227/858` against `K = 1/4` (E1); the full row
`P(d | c, b)` there is `227/858, 197/2574, 212/1287, 212/1287, 212/1287, 212/1287`
against `1/4, 1/12, 1/6, 1/6, 1/6, 1/6`; `P(c | c, c) > K(c → c)` at all `210`
non-constant triples of `{1..6}^3` and `=` at the six constant ones (E10);
all six staircases of `3×3` fail as five-site laws with exact total-variation
defects from the `K`-chain — at `(3, 1, 2)`: `RDRD` and `DRDR`
`1874214125027/58529242968768`, `RRDD` and `DDRR` `381233308277/21948466113288`,
`RDDR` and `DRRD` `3021054877865/117058485937536` (the transpose pairs equal, P3) —
and at `(5, 2, 4)` (E2, `--exact`); along every staircase every consecutive
pair is `(1/6) K` and every site marginal uniform (E3).

## Theorem P7 — opposite-corner identity and finite boundary witnesses

**(a) The corner classes.** There are four order classes, the reflections
of the top-left class, each with rows and columns `p_0`-chains by P4.
Opposite corners give the same law: `μ_TL = μ_BR` and `μ_TR = μ_BL` on every
finite rectangle for P2's symmetric positive common-row-sum rule.

*Proof.* Regroup P2's factors as
`μ_TL(v) = (1/6) [Π_{grid edges xy} K(v_x → v_y)] / [Π_{plaquettes} (K^2)(v_bottom-left, v_top-right)]`.
Edges in the first row or first column enter through their boundary chains;
each remaining edge enters through its later endpoint's bridge. Thus every
horizontal and vertical edge
appears exactly once. Symmetry makes its orientation irrelevant. Rotating
the rectangle by 180 degrees permutes the edges and plaquettes, swaps the
two entries of each anti-diagonal denominator, and leaves the product
unchanged because `K^2` is symmetric. The reflected top-left order is a
bottom-right order, proving `μ_TL = μ_BR`. Applying left-right reflection
proves `μ_TR = μ_BL`. ∎

Distinctness is asserted only at the executed witnesses. Complete direct
formation dictionaries for all four actual corner orders on `2×3`, at both
`(3, 1, 2)` and `(5, 2, 4)`, give exactly the equality classes `{TL, BR}`
and `{TR, BL}` (E11). At either triple the reflection pair differs on
`32616` of `46656` configurations. Their total variations are respectively
`2764753/79505712` and `27302976973/1247845597614`. The first mirror's rows
are `p_0` and its two-site columns `(1/6) K` (E4). Reflection changes the
anti-diagonal denominator to the other diagonal; opposite-corner reversal
does not. At a constant triple every order gives the independent uniform
law (the `(2, 2, 2)` mirror control is E9). Width-one or height-one rectangles
also have only one corner law, since reversal of the symmetric `K`-chain
with uniform start leaves it invariant. No plane law or distinctness on
other parameters or dimensions is inferred.

**(b) The snake.** Convention declared: row `0` left to right, row `1` right
to left, row `2` left to right, and so on. The row formed right to left has
the kernel
`P_rl(β → α) = K(β_{W−1} → α_{W−1}) Π_{j=W−2}^{0} K(α_{j+1} → α_j) K(α_j → β_j)/(K^2)(α_{j+1}, β_j)`,
row-stochastic with `p_0 P_rl = p_0` on all `216` row states at both triples
(E5, the mirror image of E3's telescoping), and the snake's law on `2×3` from
block 01's definition equals `p_0(row 0) P_rl(row 0 → row 1)` entrywise (E6).
Hence the snake's rows are `p_0` and all its vertical pairs `(1/6) K` (E4 for
each row pair). Its columns: on `3×3` at `(3, 1, 2)` the three-site column
laws have total-variation defects `0`, `3161/7227792`, `3583442207/7981260404832`
from the `K`-chain (column `0` is the chain, columns `1` and `2` are not; at
`(5, 2, 4)`: `0`, `104792291/623922798807`, `45687143997705515/267592135329891871884`)
(E7); on `4×3` no column is a chain — at `(3, 1, 2)` the defects are
`3583442207/7981260404832`, `23960429927/34827318130176`, `3583442207/7981260404832`
(E8), computed by the column-projected row transfer whose state carries the
full current row and the column values recorded so far. Nothing beyond
these executions is claimed about the snake. The other corner classes have
the separately proved P7(a) identity; remaining orders are not characterized.
No snake mechanism is stated (the refuting checker found the first draft's
mechanism sentence false: site `(1, 0)` of the `3×3` snake records two
neighbors, `(0, 0)` and `(1, 1)`). At `(2, 2, 2)` every snake-column defect is zero
(E9).

## No-Go Discipline Gate

The negative sentences of this note are Theorem P6 (a proved finite-
dimensional statement about right/down staircases in site values under
`μ_P`, for positive `p, q, r` not all equal) and the executed distinctness
and snake witnesses of P7 (finite statements with exact defects). Neither is a route no-go; the gate is answered for P6.

### N1 — Routes by which a staircase with a turn could still be a chain
1. A kernel other than `K` along the staircase — RULED OUT BY PRIOR: the pair
   laws and uniform marginals (block 02, E4) fix the kernel; ATTEMPTED here
   (E3). 2. Equality `P(d | c, b) = K(b → d)` at every triple — ATTEMPTED:
   fails at `c = b = d` for every non-constant positive triple (proof above;
   E1, E10). 3. A rectangle in which the block law is not `π` — ATTEMPTED:
   `π` at every block position of `3×3` and `3×4` (D4). 4. A turn whose three
   sites are not in one block — impossible by definition of a turn.
   5. The constant rule — ATTEMPTED: there every defect vanishes (E9); it is
   excluded by the variation clause, named in the premises.

### N2 — Wall-independence audit
Within the already declared positive isotropic product rule, its monotone
formation law `μ_P`, and first-order chains in the values along right/down
paths, P6 separates the nonconstant triples from the constant rule. These
carrier, rule, positivity, order and path restrictions remain hypotheses;
variation is not the theorem's sole hypothesis. No independence or minimality
claim is made about this list. The non-monotone chain `a → c → b` and the
constant-rule chains are explicit escapes outside the scoped negative.

### N3 — Hidden-wall scan
"By symmetry of `φ`" (P2, P4): a named premise of the product rule, cited.
"By E3/E4" (P4, P5, P6): block 02's theorems, cited with their proofs
restated where used. "Stationarity above the block" (P5): E3's induction,
cited. No "as is standard", "the framework provides" or "canonical".

### N4 — Per-citation table
| citation | residual attacked | residual claimed closed | match |
|---|---|---|---|
| block 02 E1 (`Z_2 = Z_1^2 K^2`) | the bridge form of the factor | P2 | y |
| block 02 E2–E3 (`P`, `p_0 P = p_0`) | rows and the row chain's Markov step | P4, P5 (i)–(iii) | y |
| block 02 E4 (pair laws) | the kernel along a staircase | P6 | y |
| block 01 Theorem B (the definition) | the recorded sets | P1 | y |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "no staircase with a turn is a Markov chain" | executed: every configuration of `2×3` and `2×4`, every `(c, b, d)` triple | executed: every site of 509 extensions; every site marginal along every staircase | executed: every column, row and block position of `3×3`, `3×4`; the six staircases; the snake columns | executed: the row kernels entrywise; the invariances on all row states; the `4×3` snake | not claimed: the inequality is proved for every rectangle, but nothing about the static law, the plane, or orders outside the class beyond the witnesses |

The runner prints matching `per_element:` … `lattice_wide:` lines. The
narrowest form is used: "first-order chains in site values on right/down
staircases under the declared positive product-rule `μ_P`, with nonconstant
orbit weights".

### N6 — Partial-closure paths and primitive scan
No new axiom or primitive is proposed or needed; the theorems use the four
axioms, block 01's definition and block 02's E1–E4 only. The registry scan
finds no primitive naming a formation order; none is used.

### N7 — Steelman
A hostile reviewer: "The staircase theorem is a fact about one conditional
at `c = b = d`; a chain with memory two (a second-order Markov chain) along
the staircase is not excluded, and the row-column structure may still admit a
Markov description along staircases after a change of state space." Correct
and outside the claim: P6 excludes first-order Markov chains along the
staircase in the site values, nothing else, and the note says so.

### N8 — Cross-cycle echo
Block 02's remark on three-recorded-neighbor sweeps (a witness, not a
theorem) has the same shape: an executed failure of a chain property. It was
not retired; P6 is the first of the lane's negative statements to carry a
proof for every non-constant triple, and its mechanism (a conditional
compared with the pair kernel) does not apply to the three-neighbor case,
where no pair-law premise holds.

## Falsifiers

The theorems fail if any of these finite statements fails: a linear
extension of `2×3`, `3×3` or `3×4` with a recorded set other than
`{left, above}`; extension counts other than `5, 42, 462, 24024`; two
extensions of `2×3` with different laws for any of the three rules; the
`i − j` sweep found to be an extension; `r(s | a, b) ≠ K(a → s) K(s → b)/(K^2)(a, b)`
for some triple; the product formula differing from the definition on `2×3`;
`μ_P^{(2×3)}(v) ≠ μ_P^{(3×2)}(v^T)` or `μ_P^{(2×4)}(v) ≠ μ_P^{(4×2)}(v^T)` for
some `v`; a column or row of `3×3`, `3×4` or `2×3` not the `K`-chain; a block
marginal not `π`; `P(a, b | c) ≠ K(c → a) K(c → b)`; a diagonal pair not
`(1/6) K^2`; the two transfer schemes disagreeing; `P(c | c, c) ≤ K(c → c)`
at some non-constant triple of `{1..6}^3`; a staircase of `3×3` with zero
defect at a declared triple; either opposite-corner dictionary differing
from its partner, or the mirror law equal to `μ_P` or differing on other
than `32616` configurations at a declared `2×3` triple; `p_0 P_rl ≠ p_0`; the snake's `3×3` column
defects other than the three literals; a `4×3` snake column with zero defect;
a nonzero defect at `(2, 2, 2)`; a fence sentence missing; a forbidden
phrase present; a floating-point literal in the runner.

## Boundaries and non-claims

This note describes the formation law of the monotone-order class on finite rectangles, the infinite strip and the quadrant; it states nothing about the static law beyond block 01's and block 02's separation. Outside the top-left class it proves the finite-rectangle opposite-corner identity and gives only the declared finite distinctness and snake witnesses.

No order is selected as physical; no plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The unilateral Markov field of the literature is a reference re-proved here at the scope used; no value, constant or theorem is imported as authority.

Further: the class is defined by the product order with the origin at the
top-left; the other three corner classes are its reflections (P7a), with
opposite corners giving identical laws on finite rectangles. All four actual
corner-order laws are executed on `2×3` at both declared nonconstant
triples, where exactly two distinct laws occur; no universal two-law count
is asserted. P6 concerns first-order Markov chains in site values along
right/down staircases within the declared positive product-rule monotone
law; it additionally requires nonconstant orbit weights. P7's distinctness
and snake claims are finite witnesses on `2×3`, `3×3` and `4×3`, and the
pattern sentence in P7(b) describes the executions only; the infinite-strip and quadrant statements of P4 rest on block 02's
projective-limit and restriction arguments and transpose no infinite object;
the `3×4` executions are at `(3, 1, 2)` only; no formation site, probability
or rate is supplied; no axiom or primitive is changed.

## Imports

References, re-proved at scope, never authority, no values imported: the
unilateral Markov field (Pickard) and the Markov-mesh constructions, whose
row-column Markov property, product-form square law and corner conditional
independence are proved here for the framework's own `μ_P` from block 02's
partial sums (P4, P5); the Cauchy–Schwarz inequality in the form
`Σ x^2/y ≥ (Σ x)^2/Σ y` (elementary, stated with its equality case, P6);
the standard Young tableaux count of the rectangle, used only as the name of
the executed extension counts. Declared mathematical scaffolding: the exact
weight triples, the rectangle sizes `2×3`, `2×4`, `3×2`, `3×3`, `3×4`, `4×2`,
`4×3`, the snake convention, the six staircases of `3×3`, the integer grid
`{1..6}^3` of triples. No observation, fitted value or literature constant
enters.

## Review record

Fable primary seat (own 23-mutation census, read from raw per-mutation
stdout). Refuting checker (Opus 5, disjoint machinery; `CHECKER_block05_findings.md`):
FIX FIRST on one sentence — the first draft's P7(b) mechanism sentence ("each
site below the first has the site above as its sole recorded neighbor") was
false and had been forbidden by the contract's addendum A1; deleted. Two
wording items folded: staircases start at any site (P6 covers every turning
monotone path, since the corner law holds at every block position), and the
infinite-strip statement of P4 speaks of finite initial segments. Everything
else reproduced on the checker's own direct summations (all four block
positions of `3×3` by full `6^9` summation; every staircase, snake and mirror
literal; the P5 and P6 proofs re-derived character for character; 12
mutations in family). The contract refuter lens (Opus 5) BEFORE the build, folded: A1 the
snake convention corrected and the "turning column" explanation withdrawn
(P7b executes `3×3` and `4×3` with the convention declared); A2 P6 stated as
a theorem from P5 (here strengthened to every non-constant positive triple by
the Cauchy–Schwarz step, executed on `{1..6}^3`); A3 the infinite strip
reached without transposing an infinite object; A4 the `n`-row reduction in
P5 with its three steps; A5 the `i + j` sweep as the class's third member and
the `i − j` sweep outside it; A6 the labels (the literature name only in
Prior art and Imports); A7 P1 for every rule and P3 for asymmetric `φ`, with
the product-form reason; A8 the executed extras (the mirror count, `2×4`
against `4×2`, `3×4`). Independence class: single family (Claude), cross-model — Fable primary,
Opus 5 contract lens, Opus 5 refuting checker, supervisor hand-verification.
The supervisor's control numbers (the bridge identity, the five-extension law equality, the `3×3`
column chain, the corner law at two blocks, the staircase defect and the
snake defects) were reproduced in the seat's own code before any theorem
sentence was written. Facts settled while executing: at `(3, 1, 2)` the
orthogonal entries of `K` and `K^2` coincide (`p + q = 2r`), so the
diagonal-pair statement of P5 is made as a statement about laws, not
entries; the `3×3` staircase defects come in transpose pairs.

## Verification

```bash
python3 scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py
python3 scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py --list-mutations
python3 scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py --mutation corner_law_wrong_denominator
python3 scripts/admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_2026_09_07.py --exact
```

Families: A authority and inputs; B the class; C the bridge and the
transpose; D rows, columns and the corner law; E the boundary of the
structure; F fences, forbidden phrases and the floating-point self-scan; G
the resolution certificate. The original 23-mutation census remains a
historical receipt at its original source hash. The final source adds a
24th declared mutation, `corner_order_reversal_broken`, that changes actual
bottom-origin formation orders; its focused E-family control is rerun after
the correction. No rerun of the unchanged full historical census is claimed.
`mutation_family_expected:` / `mutation_family_observed:` identify the
family when a full mutation run is requested. `--exact`
prints the kernels, the staircase and snake defects, the mirror count and the
minimal staircase's conditional row. Expected final line:
`TOTAL: PASS=39 FAIL=0`.

## Review correction — 2026-09-07

The original #8003 source at `f911b0e73d97b40710477f8985e14c3bd94420cf`
received five P2 findings. F1 replaces the four-law count by the proved
opposite-corner identity and two distinct laws only at the executed `2×3`
witnesses. F2 restricts the turning-path negative to right/down paths and
first-order chains in site values, retaining `a → c → b` as a chain. F3
restores the common-row-sum premise to the bridge and chain arguments while
P3 retains locally normalized arbitrary-positive factors. F4 distinguishes
class sufficiency for rows and columns from the weaker row-only property.
F5 corrects the live review queue and preserves current-main parent
corrections. Historical worker/checker/spec/control/result captures remain
unchanged with their disposition in the packet's review history. The fresh
39-check cache binds the corrected current-main parents. Source correction
and author checks do not grant an independent review verdict or audit status.
