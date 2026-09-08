---
claim_id: admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "A self-made Hermitian positive-definite nearest-neighbor precision P over the Gaussian rationals (the declared instance P_xx = 3, P_xy = (1 + 2i)/4 horizontal, (2 - i)/4 vertical; and a real instance with 1/2 on every edge) on the path 1x3, the plaquette 2x2 and the rectangle 2x3, with complex record variables; the static law the complex Gaussian with precision P and the formation law along an order the product of the rule's conditionals given the recorded neighbors only (block 01's definition): the formation law is the complex Gaussian with precision P_sigma = L^H D L and normalizer prod P_kk (G1, proved; executed on every order of the path and plaquette and on declared orders of 2x3); P_sigma depends on the order only through the recorded sets, so the monotone class of the rectangle gives one law (G2, proved; executed); P_sigma = P + diag(c) + F with the corrections c >= 0 and the fill-in F between pairs recorded together, so P_sigma is never P on a window with an edge (proved for every finite graph); if every site records at most one neighbor then P_sigma keeps P's support (proved), the converse holding on the declared grid instances as an executed fact and failing in general (the refuting checker's exact witnesses, executed: a plaquette precision whose fill-in cancels, a triangle whose fill-in lands on an edge or cancels an edge entry); on the grid the fill-in sits on the anti-diagonal pairs of the plaquettes (G3); det P_sigma = prod P_kk > det P with equality only for a diagonal P (G4, Hadamard, re-proved; executed); on 2x3 the static marginal, the pinned-static conditional and the formation read-slice covariances of the read row are pairwise different (G5, executed), and herm(Q^-1) != (herm Q)^-1 for a non-Hermitian witness. The instance is declared, not derived; nothing is claimed about any external fixture, committed action or bridge; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07
runner: scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py
---

# The Hermitian Gaussian instance: the formation law is a Gaussian whose precision is never the static one on a window with an edge

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py`](../scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.txt`](../logs/runner-cache/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.txt)

## Result up front

The earlier notes compared two ways of getting a pattern law from one rule
on a six-valued menu: the single static law the rule defines all at once, and
the law built by laying records down in an order, each record drawn from the
rule with only the records already present counted. This note asks the same
question for the simplest continuous case, where each site carries a complex
number and the rule is the conditional of a Gaussian: given the neighbours'
values, a site's value is Gaussian with a mean that is a fixed linear
combination of them and a fixed spread. The answer is sharper than in the
discrete case. Laying records down in any order gives a Gaussian law too, with
an explicit formula, but never the static one as soon as two sites are joined:
every recorded neighbour tightens the recorded site's spread a little, and a
site that records two neighbours at once couples them to each other even
though they are not joined. Orders that wait for the site above and the site to
the left all give the same law. On a row read after the row above it is fixed,
the three natural covariances one can write down, the static one, the static
one conditioned on the fixed row, and the order-built one, are three different
matrices. The instance is our own; nothing here is a statement about any
other project's object.

Exactly: let `P` be a Hermitian positive-definite precision supported on the
diagonal and the edges of a finite nearest-neighbor graph, with entries in the
Gaussian rationals, and let the rule at `x` be the complex Gaussian with mean
`−(1/P_xx) Σ_{y∼x} P_xy z_y` and variance `1/P_xx` — the one-site conditional
of the static law `∝ exp(−z† P z)`. Under block 01's definition the formation
law along an order `σ` draws site `x_k` from the rule with the sum over its
recorded neighbors `A_k` only. Then (G1) `μ_σ` is the complex Gaussian with
precision `P_σ = L_σ† D L_σ`, `L_σ` unit lower triangular in the order with
`(L_σ)_{ky} = P_ky/P_kk` for `y ∈ A_k`, `D = diag(P_kk)`, and normalizer
`Π_k P_kk`; (G2) `P_σ` depends on `σ` only through the recorded sets, so every
monotone order of a rectangle gives one law (block 05, P1); (G3)
`P_σ = P + diag(c) + F_σ` with `c_x = Σ_{k: x∈A_k} |P_kx|^2/P_kk ≥ 0` and
`(F_σ)_{xy} = Σ_{k: x,y∈A_k} P_xk P_ky/P_kk`, so `P_σ = P` only when no site records a neighbor; if every site records at most one neighbor, `P_σ` keeps `P`'s support, and on the declared instances a site recording two neighbors couples them (in general the fill-in, a sum, can cancel — the checker's witnesses); (G4)
`det P_σ = Π_k P_kk > det P` unless `P` is diagonal; (G5) on `2×3` with the
top row pinned, the three read-slice covariances of the bottom row are
pairwise different. Executed on the declared instance (`P_xx = 3`, horizontal
`(1 + 2i)/4`, vertical `(2 − i)/4`) and a real instance (`1/2` on every edge):
the correction per recording neighbor is `5/48`; on the `2×3` monotone class
the corrections are `[5/24, 5/24, 5/48, 5/48, 5/48, 0]` and the fill-in sits on
the anti-diagonal pairs `((0,1),(1,0))`, `((0,2),(1,1))`; the formation
precision's bottom-row block has diagonal `149/48, 149/48, 3` against `P`'s
`3, 3, 3`. Exact arithmetic: 25 checks, 19 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the campaign's probe record PROBES_gravity_consumer_20260907.md: the queue item 'the Gaussian instance on the gravity lane's fixture' re-scoped to a self-made Hermitian instance; the owner's sequencing gate (2026-08-26): what the Admissibility rule induces on the infinite lattice is unidentified; the parked statistical-bridge decision wakes on 'the committed-action identification lands', which this note does not fire"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "consumer: the gravity/source lane's chain-rule-versus-one-shot-joint sentence (block 171 on its branch), which this note states exactly for a Hermitian precision the day the lane's chain is on main; next in the campaign: formation-law uniqueness on Z^3 for the monotone class; width 6"
conditional_surface_status: "exact on the declared instance and windows; G1, G2, G3(a), G4 and the forward half of G3(b) are proved for every Hermitian positive-definite nearest-neighbor precision on every finite graph; the converse of G3(b) and G3(c) are executed on the declared grid instances and fail in general (executed witnesses); G5 is an executed instance; no external fixture, no bridge, no order selected"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "G1-G4 are elementary identities of Gaussian conditionals and triangular factorizations, proved in full and executed exactly on the declared windows and orders; G5 is an exact executed comparison; nothing about any external object, the plane, a physical order, the Born form or the bridge is claimed."
```

## Premises and declared objects

The scientific dependencies are the four axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), block 01's
note [`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)
(the definition of a formation law along an order and its Theorem B
condition) and block 05's note
[`ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md`](ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md)
(P1: every linear extension of the product order records exactly `{left,
above}`, for every rule), both proposed and unaudited. The axiom sentences
used, verbatim (runner A2): "There is one fixed nearest-neighbor
admissibility rule, covariant under lattice translations and proper cubic
rotations." — "For each site, the probability distribution over the
possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable."

**Why a Gaussian instance, and whose it is.** The campaign's probe record
(`PROBES_gravity_consumer_20260907.md` in the pack) found that the queue item
"the Gaussian instance on the gravity lane's fixture" cannot be built as
stated: that lane's object is complex and not Hermitian, and its artifacts are
not on the main branch. This note builds the instance on a **self-made**
Hermitian positive-definite precision, declared below, so that the
static/formation distinction of blocks 01–02 is stated exactly for the object
class in which a Hermitian precision lives. Nothing here concerns that lane's
object.

**The graph and the instance.** A finite nearest-neighbor graph: the path
`1×3` (sites `(0,0), (0,1), (0,2)`), the plaquette `2×2`, the rectangle `2×3`
(sites `(i, j)`, edges between horizontal and vertical neighbors). Complex
record variables `z_x`. The **declared instance**: `P_xx = 3`; on a
horizontal edge with `x` left of `y`, `P_xy = (1 + 2i)/4` and `P_yx` its
conjugate; on a vertical edge with `x` above `y`, `P_xy = (2 − i)/4`; all
other entries `0`. The **real instance**: `P_xx = 3`, `P_xy = 1/2` on every
edge. Both are Hermitian; positive definiteness follows from Gershgorin (each site has at most three neighbors, each off-diagonal entry of modulus `√5/4` for the declared instance and `1/2` for the real one, both below `1`, so `3 > 3 · √5/4`) and is executed by the leading principal minors (B1).

**The static law and the rule.** The complex Gaussian with density
`(det P/π^N) exp(−z† P z)`. Its one-site conditional given all the neighbors'
values is the complex Gaussian with mean `m_x = −(1/P_xx) Σ_{y∼x} P_xy z_y`
and variance `1/P_xx` (complete the square in `z_x`: `z† P z = P_xx |z_x −
m_x|^2 + (terms without z_x)`): this is the instance's **rule**, a
probability law at each site determined by, and varying with, the neighbors'
values.

**The formation law (block 01's definition, records-only reading).** For an
order `σ = (x_1, …, x_N)` and `A_k = N(x_k) ∩ {x_1, …, x_{k−1}}`, site `x_k`
draws from the rule with the sum restricted to `A_k`: mean `−(1/P_kk)
Σ_{y∈A_k} P_ky z_y`, variance `1/P_kk`; an unrecorded neighbor contributes
nothing. `μ_σ` is the product of these conditional densities in the order.

**The factors.** `L_σ`: the unit lower-triangular matrix (in the order) with
`(L_σ)_{ky} = P_ky/P_kk` for `y ∈ A_k` and `0` off the recorded pairs;
`D = diag(P_kk)`; `P_σ = L_σ† D L_σ`. The **corrections** `c_x = Σ_{k: x∈A_k}
|P_kx|^2/P_kk` and the **fill-in** `(F_σ)_{xy} = Σ_{k: x,y∈A_k} P_xk P_ky/P_kk`
(`x ≠ y`).

**The three read-slice objects.** On `2×3` with row `0` the pinned records and
row `1` the read slice: (i) the static marginal covariance, the row-`1` block
of `P^{-1}`; (ii) the pinned-static conditional covariance `(P_{11})^{-1}`,
the inverse of the row-`1` diagonal block of `P` (the static law conditioned
on row `0`); (iii) the formation covariance, the row-`1` block of `P_σ^{-1}`
for the monotone class.

**Readings, named.** Block 01's records-only reading, block 05's class
statement; the variation reading is satisfied by both instances (the rule's
mean varies with the neighbors' values since the off-diagonal entries are
nonzero). No order is selected as physical.

## Prior art and what is new

Blocks 01 and 02 stated and executed the static/formation distinction for the
six-projector product rule: equal exactly when every site records at most one
neighbor, separated by an exact gap on every window with a plaquette and on
the infinite strip. Block 05 showed that the class of orders in which every
site waits for its left and above neighbors gives one law, for every rule.
Block 01's Gaussian sentences (its Boundaries, three lines) named the static
Gaussian object — the precision, the pinned sub-block, the read-slice block of
its inverse as a conditional-then-marginal object — and fenced it. The
campaign's probe record re-scoped the Gaussian instance to a self-made
Hermitian precision. The Gaussian conditional formulas, the `L† D L`
factorization of a product of Gaussian conditionals and Hadamard's inequality
are elementary linear algebra, re-proved here where used.

New here: G1 (the formation law's precision as an explicit triangular
factorization), G2 (the class statement for the Gaussian rule), G3 (the exact separation with its two parts — diagonal corrections and fill-in — and the reading of block 01's one-recorded-neighbor condition as a sparsity condition, sufficient in general and necessary on the declared grid instances), G4 (the normalizer twin of block 02's normalizer history by
Hadamard's inequality), G5 (the three read-slice covariances told apart on an
instance).

## Exact target and obligation graph

**Target.** For every Hermitian positive-definite nearest-neighbor precision
on every finite graph and every order: `μ_σ` is the complex Gaussian with
precision `L_σ† D L_σ`, equal to `P` if and only if no site records a
neighbor; and on the declared instance and windows the executed statements of
G2–G5.

| obligation | disposition |
|---|---|
| the formation law as a product of the rule's conditionals given the recorded neighbors (block 01) | cited (proposed, unaudited); restated |
| the recorded sets of a monotone order are `{left, above}` (block 05, P1) | cited (proposed, unaudited); the class statement G2 rests on it |
| the one-site conditional of a Gaussian (completing the square) | proved here |
| `μ_σ` is Gaussian with precision `L_σ† D L_σ` and normalizer `Π P_kk` (G1) | proved here; executed on every order of the path and plaquette, two orders of `2×3`, both instances (B2, B3) |
| `P_σ` depends only on the recorded sets (G2) | proved here; executed on the 24 orders of the plaquette and the monotone class of `2×3` (B4, B5) |
| `P_σ = P + diag(c) + F_σ`; never `P`; the support condition; the fill-in (G3) | proved here; executed on 62 cases (C1–C5) |
| `det P_σ = Π P_kk > det P` unless diagonal (G4) | proved here (Hadamard); executed (D1, D2) |
| the three read-slice covariances (G5) | executed (E1–E3) |
| anything about an external fixture, larger windows or the plane | not this note |

## Theorem G1 — the formation law is Gaussian with precision `L_σ† D L_σ`

**Statement.** `μ_σ(z) = π^{−N} (Π_k P_kk) exp(−z† L_σ† D L_σ z)`; hence
`μ_σ` is the complex Gaussian with precision `P_σ = L_σ† D L_σ`, which is
Hermitian positive definite, and its normalizer is `Π_k P_kk`, the same for
every order, while the static normalizer is `det P`.

*Proof.* The complex Gaussian with mean `m` and variance `1/a` on `C` has
density `(a/π) exp(−a |z − m|^2)`. Site `x_k`'s conditional in the formation
law has `a = P_kk` and `m_k = −Σ_{y∈A_k} (P_ky/P_kk) z_y`, so
`|z_k − m_k|^2 = |Σ_y (L_σ)_{ky} z_y|^2` with the row `k` of `L_σ` (its
diagonal entry `1`, its entries `P_ky/P_kk` on `A_k`); the product over `k`
of `(P_kk/π) exp(−P_kk |(L_σ z)_k|^2)` is `π^{−N} (Π P_kk) exp(−Σ_k P_kk
|(L_σ z)_k|^2) = π^{−N} (Π P_kk) exp(−z† L_σ† D L_σ z)`. The matrix
`L_σ† D L_σ` is Hermitian and positive definite because `D > 0` and `L_σ` is
invertible (unit triangular); its determinant is `det D = Π P_kk` since
`det L_σ = 1`, which is the normalizer of a complex Gaussian with that
precision — consistent with the product form. ∎ Executed: the quadratic form
assembled term by term from the conditional means and variances equals
`L_σ† D L_σ` on every order of the path (6) and the plaquette (24) and on
two orders of `2×3`, both instances, and is Hermitian (B2); `det L_σ = 1` and
`det P_σ = Π P_kk` (B3).

## Theorem G2 — the recorded-set class

**Statement.** `P_σ` depends on `σ` only through the recorded sets `{A_k}`.
Consequently two orders with the same recorded sets give the same Gaussian
law, and every monotone order of a rectangle (block 05, P1: the recorded set
of every site is `{left, above}`) gives one law.

*Proof.* `L_σ` is determined by the recorded sets (its nonzero off-diagonal
entries are `P_ky/P_kk` at `(k, y)` with `y ∈ A_k`, and the order of the rows
and columns is a simultaneous permutation of the sites, under which
`L_σ† D L_σ` is invariant as a matrix indexed by sites); `D` does not depend
on the order at all. ∎ Executed: the 24 orders of the plaquette fall into 14
recorded-set classes, and `P_σ` is constant on each (B4); the 5 monotone
orders of `2×3` give one `P_σ`, and the snake (rows alternating) and the
mirror (rows right to left) give different ones (B5).

## Theorem G3 — the separation, explicit

**Statement.** `P_σ = P + diag(c) + F_σ` with `c_x = Σ_{k: x∈A_k}
|P_kx|^2/P_kk ≥ 0` and `(F_σ)_{xy} = Σ_{k: x,y∈A_k} P_xk P_ky/P_kk` for
`x ≠ y`. Hence: (a) `P_σ = P` if and only if every `A_k` is empty — on a connected graph with at least two sites, never; (b) if every `|A_k| ≤ 1` then `F_σ = 0`, `P_σ = P + diag(c)` and `support(P_σ) = support(P)`; on the grid with the declared instances the converse also holds (executed: every order with a site recording two neighbors has nonzero fill-in), but it is not a theorem — `(F_σ)_{xy}` is a sum over the sites recording both `x` and `y` and can vanish, and off the grid it can land on an edge or cancel an edge entry (the refuting checker's exact witnesses, executed in C6); (c) on the grid (bipartite) two neighbors of one site are at distance two, so a nonzero fill-in entry lies off `P`'s support: a site recording two neighbors couples a non-adjacent pair.

*Proof.* Expand `(L_σ† D L_σ)_{xy} = Σ_k P_kk (L_σ)̄_{kx} (L_σ)_{ky}`. The
terms: `k = x = y` gives `P_xx`; `k = y ≠ x` gives `P_yy · (P̄_yx/P_yy) · 1 =
P_xy` when `x ∈ A_y` (and `0` otherwise); `k = x ≠ y` gives `P_xy` when
`y ∈ A_x`; since for an adjacent pair exactly one of `x ∈ A_y`, `y ∈ A_x`
holds (the earlier one is recorded by the later one), these two cases
together reproduce `P_xy` on every edge and `0` on every non-edge; the terms
with `k ≠ x, y` and both `x, y ∈ A_k` give `P_kk (P̄_kx/P_kk)(P_ky/P_kk) =
P_xk P_ky/P_kk` (Hermitian `P`), the fill-in; and on the diagonal the terms
`k ≠ x` with `x ∈ A_k` give `P_kk |P_kx/P_kk|^2 = |P_kx|^2/P_kk`, the
corrections. (a): `c_x > 0` whenever `x ∈ A_k` for some `k`, because
`P_kx ≠ 0` on an edge and `P_kk > 0`; if some `A_k` is nonempty then `P_σ ≠
P`; and on a connected graph with two or more sites the second site of any
order records the first when they are adjacent, or some later site records an
earlier neighbor — in every case some `A_k ≠ ∅` (executed: every order of
every window has a nonempty recorded set). (b): if every `|A_k| ≤ 1` no pair is recorded together, `F_σ = 0`, and `diag(c)` touches the diagonal only. The support of `F_σ` is contained in the set of pairs recorded together by some site, and each entry is a sum that can vanish, so the converse is an instance statement: on the declared grid instances no cancellation occurs (C3), while a plaquette precision with `P_cd = −1/2` under the order `(a, d, b, c)` keeps `P`'s support although two sites record two neighbors, the triangle `K_3` with `1/2` on every edge puts its fill-in on an edge, and a triangle precision `[[3, 1/4, 1/2], [1/4, 3, −3/2], [1/2, −3/2, 3]]` loses its `(0,1)` entry (C6). (c): on a bipartite graph two neighbors of one site are non-adjacent. ∎ Executed: the formula on 62
(instance, window, order) cases (C1); `P_σ ≠ P` on every one (C2); the support condition on every one (C3) and its boundary (C6); the path: the end-to-end order keeps
`P`'s support with corrections `[5/48, 5/48, 0]` (each recording neighbor
contributes `|P_kx|^2/P_kk = (5/16)/3 = 5/48` at the declared instance), the
middle-out order records two neighbors at the middle site and fills in the
end pair (C4); on `2×3` the monotone class has corrections `[5/24, 5/24,
5/48, 5/48, 5/48, 0]` in site order and fill-in exactly on `((0,1),(1,0))`
and `((0,2),(1,1))`, the anti-diagonal pairs of the two plaquettes, recorded
together by `(1,1)` and `(1,2)` (C5) — the pairs on which block 05's corner
law carries its `K^2` denominator.

**Reading.** Block 01's condition "every site records at most one neighbor"
is, for the discrete product rule, the condition for equality of the two
laws; here it is a sufficient condition for the two precisions to have the same support (and on the declared grid instances the necessary one), while equality fails already at one recorded neighbor: the discrete
rule's normalizer `Z_1` is constant, which hides the diagonal correction that
the Gaussian rule's fixed variance `1/P_kk` exposes.

## Theorem G4 — the normalizers (Hadamard)

**Statement.** `det P_σ = Π_k P_kk ≥ det P`, with equality if and only if `P`
is diagonal.

*Proof.* `det P_σ = Π P_kk` by G1. For Hermitian positive-definite `P`,
eliminate in the site order: the pivot at step `k` is the Schur complement
`p_k = P_kk − r_k† (P_{<k})^{-1} r_k` with `r_k` the column of `P` above the
diagonal, and `det P = Π_k p_k`; since `(P_{<k})^{-1}` is positive definite,
`r_k† (P_{<k})^{-1} r_k ≥ 0` with equality iff `r_k = 0`; so `det P ≤ Π P_kk`
with equality iff every `r_k = 0`, i.e. `P` diagonal. ∎ Executed: `det P` is
real, positive and below `Π P_kk` on the three windows, both instances (D1);
equality for a diagonal `P` (D2). This is the Gaussian twin of block 02's
normalizer history: the order-built law's normalizer `Π P_kk` and the static
normalizer `det P` differ on every window with an edge.

## G5 — the three read-slice covariances (executed)

On `2×3`, with row `0` the pinned row for object (ii) and row `1` the read slice: the static marginal covariance of row `1` (the
block of `P^{-1}`), the pinned-static conditional covariance `(P_{11})^{-1}`
and the formation covariance (the block of `P_σ^{-1}` for the monotone class)
are pairwise different exact matrices (E1; printed under `--exact`). The
formation precision's row-`1` block differs from `P_{11}`: its diagonal is
`149/48, 149/48, 3` against `3, 3, 3` (E2) — the formation law conditioned on
the pinned row is not the static law conditioned on it. Remark, the lane's
own point recorded in the probe record and executed here: for a non-Hermitian
`Q`, `|exp(−z† Q z)| = exp(−z† herm(Q) z)` (the anti-Hermitian part
contributes a phase), and `herm(Q^{-1}) ≠ (herm Q)^{-1}` — witness
`Q = [[1, 1], [−1, 1]]` (E3).

## No-Go Discipline Gate

The negative sentences of this note are G3(a) ("`P_σ` is never `P` on a
window with an edge") and G5's "pairwise different" — exact finite
statements, the first a theorem for every Hermitian positive-definite
nearest-neighbor precision, the second an executed instance. Neither is a
route no-go. The gate is answered for G3(a).

### N1 — Routes by which the formation law could still be the static law
1. An order in which no site records a neighbor — impossible on a connected
   graph with two or more sites (proof of G3(a); ATTEMPTED on every order of
   every window). 2. A precision with zero off-diagonal entries — the
   disconnected case, excluded by the instance's nonzero edges (the variation
   reading). 3. A different reading of "recorded neighbors" (e.g. the pinned
   reading, in which unrecorded sites are integrated out rather than dropped)
   — a different construction, not the formation law of block 01; its object
   is the static conditional, G5(ii), and it too differs from the formation
   covariance (E1). 4. A different variance rule (e.g. the conditional
   variance given the recorded set under the static law, a Schur complement)
   — not the rule of the instance, which fixes `1/P_xx`; named, not built.

### N2 — Wall-independence audit
Walls: `W_R` (records-only reading), `W_H` (Hermitian positive definite),
`W_NN` (nearest-neighbor support), `W_var` (nonzero edges). `W_H` is needed
for the static law to be a probability law; `W_NN` for the rule to be a
nearest-neighbor rule; `W_var` for G3(a); `W_R` for the formation law. No
wall implies another.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework
provides", "naturally", "obviously", "canonical", "registered", "background",
"bridge context": hits only in this section. Every step is written.

### N4 — Per-citation table
| citation | residual attacked | residual claimed closed | match |
|---|---|---|---|
| block 01 (the formation-law definition; Theorem B's condition) | the discrete distinction | the Gaussian instance's G1, G3 | yes (definition cited; the condition reread) |
| block 05 P1 (recorded sets of monotone orders) | the class | G2 | yes |
| the probe record (`PROBES_gravity_consumer_20260907.md`) | the re-scoping | the instance's provenance | yes (a pack record, not authority) |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "`P_σ` is never `P` on a window with an edge" | executed: every order of the path and plaquette, the declared orders of `2×3`, both instances | executed: every site's recorded set, correction and fill-in | executed: the quadratic forms, determinants, minors, the three covariances | executed: the row-1 blocks on `2×3` | not claimed: three finite windows of a declared instance |

The runner prints matching `per_element:` … `lattice_wide:` lines.

### N6 — Partial-closure paths and primitive scan
No axiom, primitive or convention is proposed or changed; the instance is a
declared fixture of this note, imposed and measured, never registered.

### N7 — Steelman
"The Gaussian rule should be defined with the static conditional variance
given the recorded set (a Schur complement), not the fixed `1/P_xx`; with that
rule the path's formation law would be the static law." Correct as a
statement about a different rule: block 01's formation law uses the rule's
conditional with the unrecorded factors dropped, and the instance's rule has
the fixed variance; the alternative rule is named in N1 and not built here.

### N8 — Cross-cycle echo
Block 01's Gaussian sentences fenced the static object; block 02's normalizer
history is echoed by G4. Neither is retired; this note supplies the missing
formation side for a Hermitian precision.

## Falsifiers

The theorems fail if any of these finite statements fails: a leading
principal minor not positive, or `P ≠ P†`; a conditional-product quadratic
form not equal to `L_σ† D L_σ`, or not Hermitian; `det L_σ ≠ 1` or
`det P_σ ≠ Π P_kk`; two orders with the same recorded sets and different
`P_σ`; a plaquette class count other than 14; two monotone orders of `2×3`
with different `P_σ`, or the snake or mirror equal to the class; a case where
`P_σ ≠ P + diag(c) + F_σ`; an order with `P_σ = P`; a support difference with every site recording at most one, or, on the declared grid instances, a support equality with a site recording two; a witness of C6 failing (the plaquette cancellation, the triangle's edge fill-in, the triangle's lost entry); path corrections other than `[5/48, 5/48, 0]`; `2×3`
corrections or fill-in pairs other than the literals; `det P ≥ Π P_kk` on a
window with an edge; two of the three read-slice covariances equal; the
formation row-`1` block diagonal other than `149/48, 149/48, 3`;
`herm(Q^{-1}) = (herm Q)^{-1}` for the witness.

## Boundaries and non-claims

This note states the static/formation distinction for a self-made Hermitian positive-definite nearest-neighbor precision on three small windows; the instance is declared, not derived, and nothing is claimed about any external fixture or committed action.

No order is selected as physical; no plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.

Hadamard's inequality and the Gaussian conditional formulas are elementary results re-proved here at the scope used; no value, constant or theorem is imported as authority.

Further: the instance's off-diagonal entries are one value per edge
direction, not a general nearest-neighbor precision, though G1–G4 are proved
for every Hermitian positive-definite nearest-neighbor `P`; the executed
orders of `2×3` are the monotone class, the snake and the mirror (and two
orders for G1); G5 is an executed instance, not a theorem; the converse of G3(b) and G3(c) are statements about the grid and the declared instances, not theorems for every graph (the executed witnesses show the boundary); the complex record
variable is a modelling choice of the instance (the real instance shows the
same structure); no formation site, probability or rate is supplied; no
axiom or primitive is changed.

## Imports

References, re-proved at scope, never authority, no values imported: the
one-site conditional of a complex Gaussian (completing the square); the
`L† D L` form of a product of Gaussian conditionals (G1); Hadamard's
inequality for a Hermitian positive-definite matrix (G4, by Schur-complement
pivots). Declared mathematical scaffolding: exact arithmetic in the Gaussian
rationals as implemented in `sympy` (`Rational`, `I`; determinants, inverses
and minors by exact elimination); the declared instance's entries; the three
windows; the orders named. No observation, fitted value or literature
constant enters.

## Review record

Supervisor-authored (Fable) from the supervisor's control
`specs/supervisor_control_block07_gaussian.py` (with its output), which
computed every number here before the contract `GOAL_block07.md` was written;
Refuting checker (Opus 5, disjoint machinery; `CHECKER_block07_findings.md`): FIX FIRST on one theorem — the first draft's G3(b) claimed the support condition as an equivalence for every finite graph; the checker showed by exact witnesses (a plaquette precision whose fill-in cancels, a triangle whose fill-in lands on an edge, a triangle that loses an edge entry) that only the forward direction is a theorem; folded: G3(b), (c) restated, the witnesses executed (C6), the scope lines corrected; also a mutation that leaked across families (localized), the Gershgorin sentence and the G5 heading. Everything else confirmed on its own machinery — the conditional densities integrated in real coordinates, the 14 classes, the 62 cases, the Schur pivots, the three covariances by its own elimination, and the pinned-static conditional precision derived as `P_{11}`. Independence class: single family (Claude), cross-model — Fable supervisor-author, Opus 5 refuting checker. Settled while executing: the runner's term-by-term quadratic form
had a stray transpose in its first draft (caught by B2 against `L† D L`);
the plaquette's 24 orders give 14 recorded-set classes (not 24 laws), the
executed content of G2.

## Verification

```bash
python3 scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py
python3 scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py --list-mutations
python3 scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py --mutation separation_formula_wrong
python3 scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py --exact
```

Families: A authority and inputs; B the formation law's precision and the
class (G1, G2); C the separation (G3); D the normalizers (G4); E the read
slices (G5); F fences, forbidden phrases and the floating-point self-scan; G
the resolution certificate. Each of the 19 declared mutations perturbs one object or injects one claim and fails in exactly one family; `--exact` prints
`P`, `P_σ` and the three read-slice covariances of `2×3`. Expected final line: `TOTAL: PASS=25 FAIL=0`.
