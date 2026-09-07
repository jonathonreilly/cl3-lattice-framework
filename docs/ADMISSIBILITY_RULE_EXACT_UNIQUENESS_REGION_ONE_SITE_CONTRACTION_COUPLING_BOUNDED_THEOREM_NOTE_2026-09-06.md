---
claim_id: admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule of orbit weights (p, q, r): the one-neighbor interdependence coefficient c_1(p, q, r) of the one-site conditional on the six-neighbor shell of Z^3, exactly, at the declared triples (3,1,2), (5,2,4), (2,1,2), (3,2,2), (5,4,4), (11,10,10), (2,2,2), on the grid r = 4, p, q in 1..12, and along the three lines (t,1,1), (t,t,1), (1,1,t), on each of which two crossings of 6c_1 = 1 are proved, both thresholds isolated as the unique positive roots of explicit polynomials with the maximizing shell patterns identified and verified against every competitor, and 6c_1 < 1 verified for every real t between them by an exact Lipschitz bound (Theorem G); the finite-window comparison bound by coupling, proved for every finite window and executed on the plaquette with eight exterior slots and on the 3x3 planar window with twelve exterior slots (Theorem H); uniqueness of the infinite-volume static law on Z^3 when 6c_1 < 1, proved as a corollary of Theorem H and a walk-count bound (Theorem I); the region stated at the four region triples and on the verified open interval of each line; the criterion silent at (3,1,2), (5,2,4) and (7,3,5), where nothing is stated about one law or several; no formation order, plane, bridge, Born or gravity statement; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
  - admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py
---

# The rule induces exactly one static law on the cubic lattice wherever its one-neighbor influence sums to less than one: verified intervals and exact pointwise values, by a coupling re-proof

**Date:** 2026-09-06
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py`](../scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.txt`](../logs/runner-cache/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.txt)

## Result up front

Take the fixed rule that gives the odds for the value a record takes from the
values its six neighbours carry. Ask how much one neighbour's record can shift
the odds at a site, at worst, over every possible state of the other five, and
add that worst shift up over the six neighbours. When the total is less than
one, the whole lattice carries exactly one static pattern law: the influence of
a far-away record fades by that factor with every step of distance, faster than
the number of far-away records grows, so any two candidate laws must agree on
every local question. We computed that total exactly. It is less than one for
weak couplings — four named examples, and on three lines through the constant
rule the whole stretch between two thresholds, each located as a root of an
explicit polynomial and verified with no gaps — and more than one for the two
couplings used in the earlier blocks, where this test simply says nothing.

Exactly: for the covariant product rule with orbit weights `(p, q, r)`, the
interdependence coefficient `c_1(p, q, r)` — the supremum over shells `η, η'`
differing at one neighbor of `TV(r_x(·|η), r_x(·|η'))` — is the same for the
six directions, satisfies `c_1(p, q, r) = c_1(q, p, r)`, and vanishes exactly
at `p = q = r` (Theorem G). Its exact values: `270/989` at `(3, 1, 2)`
(`6c_1 = 1620/989`), `8650000/40615109` at `(5, 2, 4)`, `2/13` at `(2, 1, 2)`
(`6c_1 = 12/13`), `2079/15566` at `(3, 2, 2)` (`6c_1 = 6237/7783`),
`4000000/61385721` at `(5, 4, 4)`, `98241110000/4544062780611` at
`(11, 10, 10)`, `0` at `(2, 2, 2)`. With the orthogonal weight fixed at `4`,
`6c_1 < 1` exactly on the fifteen-cell diamond
`{(2,4), (3,3), (3,4), (3,5), (4,2..6), (5,3..6), (6,4), (6,5)}` of
`(p, q) ∈ 1..12`. Along `(t, 1, 1)` the crossing `6c_1 = 1` is the unique
positive root `t* ∈ [1.60970232778584910813, 1.60970232778584910814]` of
`t^7 − 2t^5 + 5t^4 − 8t^3 − t^2 − 4`, attained by the shell pattern three
`+x`, two `−x` with the flipped neighbor `+x ↔ −x`; along `(t, t, 1)` it is
the unique positive root `t* ∈ [1.47753945492134830313, 1.47753945492134830314]`
of `4t^7 − 8t^5 + 5t^4 − 8t^3 − t^2 − 1`, pattern three `+x`, two `+y`,
flipped `+x ↔ +y`; along `(1, 1, t)` it is the unique positive root
`t* ∈ [0.67680087774930621901, 0.67680087774930621903]` of
`t^7 + t^5 + 8t^4 − 5t^3 + 8t^2 − 4`, the same pattern. Each line crosses
`6c_1 = 1` a second time: on `(t, 1, 1)` at `t_2 = √30 − 5`, the positive root
of `t^2 + 10t − 5` (`0.47722557505166113456…`), attained by `(+x, +x, −x, +y,
−y)` with the flipped neighbor `+z ↔ −z`; on `(t, t, 1)` at the positive root
of `t^5 + 7t − 5` (`0.69167061103656469380…`) and on `(1, 1, t)` at the
positive root of `5t^5 − 7t^4 − 1` (`1.44577488770465582773…`), both attained
by five `+x` with the flipped neighbor `+y ↔ +z`. On each isolating interval
every one of the `252 × 15` shell-and-pair choices is verified below one by an
exact Lipschitz bound or is a copy of the displayed maximizer, and `6c_1 < 1`
is verified for every real `t` between the two thresholds (G5–G6); the
`(1, 1, t)` line is the `(t, t, 1)` line under scale invariance, with
reciprocal polynomials. Theorem H, proved by a
random-scan coupling, bounds the disagreement of the static laws of two
exterior assignments on any finite window with row sums below one by `D_Λ b`,
`D_Λ = (I − C_Λ)^{-1}`; on the `3×3` planar window at `(2, 1, 2)` the center-
site marginal moves by total variation
`691410442136477999520/76730168638463067377251 ≈ 0.0090109` when one exterior
slot flips, against the bound `1/56`. Hence (Theorem I) the specification of
the product rule on `Z^3` has exactly one infinite-volume static law wherever
`6c_1 < 1`: at the four region triples and at every point of the verified
open interval of each line. At `(3, 1, 2)`, `(5, 2, 4)` and `(7, 3, 5)` the
criterion is silent. Executed with exact arithmetic: 41 checks, 31 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 02's named next target: 'uniqueness of the infinite-volume static law on Z^3 (the contraction region of the one-site conditional's dependence on its six neighbors)'; and the owner's sequencing gate (2026-08-26): what the Admissibility rule induces on the infinite lattice is unidentified; the parked statistical-bridge decision wakes on 'the committed-action identification lands', which this note does not fire"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "next question: the two silent triples (3,1,2) and (5,2,4) under a sharper criterion — the two-site block condition, disagreement percolation, a transfer-matrix or cluster-expansion route — each with its own obligation; consumers: the parked statistical-bridge decision material (docs/repo/DEFERRED_DECISIONS.md entry 1, read-only), the gravity lane's action question (in the region the static law is a single object), the record-matter lane's formation-order supply"
conditional_surface_status: "exact on the declared triples, grid, lines and windows; Theorem H is proved for every finite window with row sums below one; Theorem I is proved on Z^3 for 6c_1 < 1; the region statement is executed pointwise and verified on the lines' intervals; nothing at the silent triples; no plane, no formation law, no bridge"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorem G's structural parts are proved and its values are exact executed computations with the thresholds isolated by Sturm's theorem and the maximizing patterns re-executed at the isolating endpoints; Theorem H is a native coupling proof executed on two exact windows; Theorem I is a corollary with its walk-count arithmetic executed; the region is stated at executed points and on the verified intervals of the three lines; nothing about several laws, the silent triples, a physical rule, the plane, the bridge, the Born form or gravity is claimed."
```

## Premises and declared objects

The only scientific dependencies are the four axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and the two
upstream notes of this lane, block 01 [`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md) (Theorem A: the static law of a
finite window with exterior records and its uniqueness among laws with those
full conditionals) and block 02 [`ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md) (Theorem C: the specification and the
existence of an infinite-volume static law), both proposed and unaudited, their
definitions restated here where used. The axiom sentences used, verbatim
(runner A2, A3):

- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and "For
  each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form." — "records are permanent" — "Only records are
  readable." — "A site with no record cannot be read."

**Menu, rotations, weights.** `M` = the six projectors `P(±e_a)`, indexed
`P(+e_x), P(−e_x), P(+e_y), P(−e_y), P(+e_z), P(−e_z)`; the 24 proper cubic
rotations act as signed axis permutations, transitively; ordered pairs fall
into the parallel, antiparallel and orthogonal orbits with pair weight `φ(s, t)
∈ {p, q, r}`, `φ` symmetric and positive. The product rule (P): `r_x(s | η) ∝
Π_{y ∈ A} φ(s, η_y)` over the recorded neighbors `A` (block 01, B7: the site
weight is constant on the transitive menu). Declared triples: the region
triples `(2, 1, 2)`, `(3, 2, 2)`, `(5, 4, 4)`, `(11, 10, 10)`; the silent
triples `(3, 1, 2)`, `(5, 2, 4)` and, added after the contract lens, `(7, 3,
5)` with all weights distinct; the constant triple `(2, 2, 2)` as the boundary. A rational triple is scaled to integers by its common denominator
before any computation (the conditional is homogeneous of degree zero in `φ`,
so `c_1` is unchanged).

**Readings carried from blocks 01–02, named, nothing new adopted.** Positivity
of the rule; the extensional reading of the variation clause restricted to the
declared menu (`(p, q, r)` not all equal); the records-only reading enters
only through blocks 01–02's definitions of the finite-window objects. No
formation order enters this note, whose theorems concern the static laws only.

**Static law with exterior records.** For a finite window `Λ` with exterior
records `ω` on its declared exterior slots, `μ_Λ^ω(v) ∝ Π_{xy ∈ E(Λ)} φ(v_x,
v_y) Π_{x ∈ Λ, z ∈ ∂Λ, z ~ x} φ(v_x, ω_z)`; its full conditionals are the rule
with every neighbor (interior or exterior) recorded, and it is the unique law
with those full conditionals (block 01, Theorem A). An **infinite-volume static
law** is a probability measure `μ` on `M^{Z^3}` with `μ(v_Δ = a) = Σ_b μ_Δ^b(a)
μ(v_{∂Δ} = b)` for every finite `Δ` and assignment `a` — the finite-window
conditional identity that block 02's Theorem C2 proves a limit measure
satisfies; `∂Δ` is the finite set of exterior neighbors of `Δ` and the sum over
their records `b` is finite.

**The interdependence coefficient.** For a site `x` with a shell of `d`
recorded slots and a slot `y`, `C_{xy} = sup { TV(r_x(·|η), r_x(·|η')) : η, η'
differ only at y }`, `TV(a, b) = (1/2) Σ_s |a_s − b_s|`. For the product rule
the conditional is a symmetric function of the slot values, so `C_{xy}` is one
number `c_1^{(d)}(p, q, r)` for every slot of a `d`-slot shell: `c_1 =
c_1^{(6)}` on the `Z^3` shell, `α = 6c_1`, and `c_1^{(4)}` on the planar
windows below, where every site has four slots. Executed as the supremum over
all `6^{d−1}` values of the other slots and all `15` unordered pairs of values
at `y`. The window coefficient is not bounded by the shell coefficient:
`c_1^{(4)}(2, 5, 3) = 14250/59251 > c_1(2, 5, 3) = 1629375/6780002` (C14), so
`C_Λ` and `b` are always defined from the window's own conditional; on the
boxes of Theorem I every site has six slots and `C_{xy} = c_1`.

**Windows.** (a) The plaquette: sites `0-1-2-3-0`, each with two interior
neighbors and two exterior slots (eight slots); the base exterior carries
`P(e_x)` on every slot; the flipped exterior carries `P(−e_x)` on the slot
(site `0`, left). (b) The `3×3` planar window: sites `(i, j)`, `i, j ∈ 0..2`,
with twelve exterior slots (left of column `0`, right of column `2`, below row
`0`, above row `2`); the base exterior carries `P(e_x)` everywhere; the
flipped exterior carries `P(−e_x)` on the slot left of site `(1, 0)`. Its
interdependence matrix is `C_Λ = c_1^{(4)} · (adjacency)`, `9 × 9`, with row
sums `2c_1^{(4)}`, `3c_1^{(4)}`, `4c_1^{(4)}`; the influence matrix `D_Λ =
Σ_{n ≥ 0} C_Λ^n = (I − C_Λ)^{-1}` when `4c_1^{(4)} < 1`; `b_y = c_1^{(4)}` at
`y = (1, 0)` and `0` elsewhere. (c) The `Z^3` shell for `c_1` and the boxes
`Λ_L` of side `2L + 1` for Theorem I.

**The configuration family (plaquette).** All ordered pairs `(η, η')` of
plaquette configurations differing at at most two of the four sites
(`221,616` pairs) plus `2,000` pairs from block 01's fixed linear
congruential generator (seed `20260906`, multiplier `1103515245`, increment
`12345`, modulus `2^31`, eight draws per pair, `(state >> 16) mod 6`).

## Prior art and what is new

Blocks 01 and 02 (linked above) are the parents: the static law with exterior
records and its uniqueness on a finite window (Theorem A), the specification
and an infinite-volume static law (Theorem C). The uniqueness criterion re-
proved here is classical: Dobrushin's one-site contraction condition and its
comparison-theorem form, referenced by the author's name once and re-proved at
the scope used (Theorems H and I); no value, constant or theorem is imported
from it. The sharper two-site condition of Dobrushin and Shlosman and
disagreement percolation are named as leads only. The prior in-repo use is `do
cs/WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOU
NDED_THEOREM_NOTE_2026-07-12.md` (and its five sibling notes of the same
date), which applies the criterion on a different carrier (a constrained
polymer fiber of the Wilson-staggered block map) and quotes the theorem as
authority; it does not concern the menu rule and does not re-prove the
criterion. The prior-art sweep is in the pack's `ROUTE_PORTFOLIO.md` (block 03
section); no landed note computes the coefficient of the menu rule, states its
region, or re-proves the criterion.

New here: the exact coefficient of the covariant product rule with its
structural properties (Theorem G); the exact region on the grid and the three
algebraic thresholds with their maximizing patterns, isolated and re-executed
at the isolating endpoints; the coupling proof of the finite-window comparison
bound written in full and executed on two exact windows (Theorem H); the
corollary on `Z^3` with its walk-count arithmetic executed (Theorem I); the
region stated pointwise.

## Exact target and obligation graph

**Target.** If `6c_1(p, q, r) < 1` then the specification of the covariant
product rule on `Z^3` has exactly one infinite-volume static law; and
`6c_1 < 1` holds at the four region triples and throughout the verified open
interval between two exact thresholds on each of the three lines. No
exhaustive exclusion of other positive line parameters is claimed.

| obligation | disposition |
|---|---|
| the static law of a finite window with exterior records has the rule as full conditionals and is unique among laws with those conditionals (Theorem A) | cited (block 01, unaudited); the full-conditional property is what H3 uses |
| an infinite-volume static law exists and satisfies the finite-window conditional identity (Theorem C2) | cited (block 02, unaudited); Theorem I needs only the identity for each of two laws |
| the coefficient is direction-independent, `p ↔ q` symmetric, zero iff constant (G1–G3) | proved here; executed (B1–B4) |
| the exact values, the grid, the maximizing patterns (G4) | executed (C1–C4) |
| the three thresholds: sign pattern fixed, the rational function, Sturm isolation, the supremum at the endpoints (G5) | executed (C5–C9) |
| the second crossings, the Lipschitz lemma along a line, the competitor and region certificates, reciprocity (G5′–G6) | proved here (the lemma); executed (C10–C14) |
| the maximal coupling on a finite set and the triangle inequality along a path of single-slot changes (H1) | proved here; executed on the plaquette family (D1, D2) |
| the disagreement recursion, the monotone affine map and its fixed point (H1–H2); stationarity under single-site resampling (H3) | proved here (stationarity from Theorem A's full-conditional property); the fixed point and iterates executed (D3–D6) |
| the subsequence limit on a finite state space and the telescoping bound (H3) | proved here; the center-site bound executed (D7, D8) |
| the walk-count bound `(C_Λ^n)_{xy} ≤ c_1^n N_n(x, y)` and `Σ_y N_n = 6^n` (I) | proved here; executed for `n ≤ 4` (E1) |
| the tail `Σ_{n ≥ L−ℓ} α^n = α^{L−ℓ}/(1 − α) → 0` (I) | proved here; the table executed (E2, E3) |
| two probability measures agreeing on every cylinder event coincide | cited (uniqueness of the Carathéodory extension from the cylinder algebra; Imports) |
| a sharper criterion at the silent triples | open; not this note |

The strongest missing lemma is any criterion that decides the silent
triples; nothing in the target uses it.

## Theorem G — the coefficient, exactly

**G1 (direction independence).** For the product rule `r_x(s | η) ∝ Π_y φ(s,
η_y)` the conditional is a symmetric function of the six shell values, so the
supremum defining `C_{xy}` does not depend on which slot is varied: `C_{xy} =
c_1` for each of the six neighbors; for a site `z` not adjacent to `x` the
conditional does not depend on `η_z`, so `C_{xz} = 0`; hence `α = Σ_y C_{xy} =
6c_1`. (For any covariant rule the same follows from the transitivity of the
rotations fixing `x` on the six directions.) Executed: the supremum with the
varied value at each of the six slot positions at `(3, 1, 2)` is `270/989` six
times (B1).

**G2 (`p ↔ q` symmetry).** Let `ι : s ↦ −s` be the antipodal bijection of
the menu, `P(±e_a) ↦ P(∓e_a)`. It exchanges the parallel and antiparallel
orbits of the pair `(s, t)` and fixes the orthogonal orbit, so
`φ_{(p,q,r)}(ι s, t) = φ_{(q,p,r)}(s, t)` for every `t`, and therefore
`r_{(p,q,r)}(ι s | η) = r_{(q,p,r)}(s | η)` for every shell `η` (the
normalizers agree because `ι` is a bijection of the outcome). Total variation
is invariant under a bijective relabeling of the outcome applied to both
vectors, so every term in the supremum is unchanged and
`c_1(p, q, r) = c_1(q, p, r)`. Executed: the identity on all `46656` shells
and six values at `(3, 1, 2)` against `(1, 3, 2)` (B3); the values at
`(3, 1, 2)/(1, 3, 2)` and `(5, 2, 4)/(2, 5, 4)` (B2); symmetry on all `144`
grid points (C3).

**G3 (zero exactly at the constant rule).** If `p = q = r` every conditional
is uniform and `c_1 = 0`. Conversely, if `c_1 = 0` then changing one slot at
a time never changes the conditional, so `r_x(· | η)` is one vector for all
shells. The shell with all six slots at `P(e_x)` gives the weights
`(p^6, q^6, r^6, r^6, r^6, r^6)` in menu order; the shell with all six at
`P(e_y)` gives `(r^6, r^6, p^6, q^6, r^6, r^6)`; both normalize by
`p^6 + q^6 + 4r^6`, so equality forces `p^6 = r^6` and `q^6 = r^6`, i.e.
`p = q = r` by positivity. Executed: `c_1 = 0` at `(2, 2, 2)`, `c_1 > 0` at
the six declared non-constant triples (B4).

**G4 (values, executed).** The exact coefficient at the seven triples is the
list in Result up front (C1); `6c_1 < 1` at the four region triples and `6c_1 ≥
1` at the two silent triples (C2). The maximizing pattern — the
lexicographically first maximizer over the `7776 × 15` choices, listed as the
other five slot values in menu order and the flipped pair; ties are not
excluded, the value is the supremum — is `(+x, +x, +x, +y, −y)` with pair `+x ↔
−x` at `(3, 1, 2)`; five `+x` with pair `+x ↔ −x` at `(5, 2, 4)`, `(5, 4, 4)`,
`(11, 10, 10)`; `(+x, +x, −x, +y, −y)` with pair `+z ↔ −z` at `(2, 1, 2)`;
`(+x, +x, +x, −x, −x)` with pair `+x ↔ −x` at `(3, 2, 2)`. At `(7, 3, 5)`,
`c_1 = 6391462/29948925`, `6c_1 ≈ 1.2805`: silent (C14). The maximizer is not
unique; the tie counts over the `252 × 15` multiset-and-pair choices are `12,
6, 60, 30, 30, 30, 24` in the order of the seven non-constant triples (under
`--exact`). On the grid `r = 4`,
`p, q ∈ 1..12` (`144` points, `9` s) the cells with `6c_1 < 1` are exactly the
fifteen-cell diamond of Result up front (C4), and every cell is `p ↔ q`
symmetric (C3).

**G5 (the three lines, executed).** On each line the runner scans the declared
rationals (`t = 1 + k/8` on `(t, 1, 1)` and `(t, t, 1)`; `t = k/8` on `(1, 1,
t)`), finds the bracket where `6c_1 − 1` changes sign (`3/2..13/8`,
`11/8..3/2`, `5/8..3/4`), takes the maximizing pattern at the upper bracket
point, and records the sign pattern `σ ∈ {±1}^6` of the six differences `r(s |
η, t_a) − r(s | η, t_b)` at both bracket points, which agree (C5). With that
`σ`, `3 Σ_s σ_s (r(s | η, t_a) − r(s | η, t_b)) − 1` is a rational function of
`t` equal to `6 TV_pattern(t) − 1` wherever the sign pattern holds; its
numerator is the displayed degree-7 polynomial up to a nonzero constant (C6).
Sturm's theorem gives three real roots and exactly one positive root, isolated
in a rational interval `[a, b]` of width below `10^{-20}` with a sign change at
the endpoints (C7). At both endpoints the full supremum over the `7776 × 15`
choices equals the displayed pattern's total variation, which equals the
rational function's value there, so the sign pattern holds at the endpoints
(C8); and `6c_1 − 1 < 0` at `a`, `> 0` at `b` on the first two lines, reversed
on the third (C9). Since `c_1(t)` is a maximum of finitely many continuous
functions of `t`, the crossing `6c_1 = 1` lies in `[a, b]`; the threshold is
stated as the root `t*` of the displayed polynomial; that no other choice
crosses inside `[a, b]` is verified in G6 (C11). Patterns:
`(t, 1, 1)`: three `+x`, two `−x`, pair `+x ↔ −x`; `(t, t, 1)` and `(1, 1, t)`:
three `+x`, two `+y`, pair `+x ↔ +y`.

**G5′ (the second crossing on each line, executed).** Each line crosses
`6c_1 = 1` a second time, found on the declared descending scan `t = 1 − k/40`
(`(t, 1, 1)`, `(t, t, 1)`) or ascending scan `t = 1 + k/20` (`(1, 1, t)`) at
the brackets `1/2..19/40`, `7/10..27/40`, `7/5..29/20`, and treated exactly as
the first (C10): on `(t, 1, 1)` the numerator of `6 TV − 1` at the pattern
`(+x, +x, −x, +y, −y)`, pair `+z ↔ −z`, is `−(t^2 + 10t − 5)`, whose positive
root is `t_2 = √30 − 5 ∈ [0.47722557505166113456, 0.47722557505166113458]`; on
`(t, t, 1)` the pattern five `+x`, pair `+y ↔ +z`, gives `−(t^5 + 7t − 5)` (one
real root, `t_2 ∈ [0.69167061103656469380, 0.69167061103656469382]`); on
`(1, 1, t)` the same pattern gives `5t^5 − 7t^4 − 1` (one real root, `t_2 ∈
[1.44577488770465582773, 1.44577488770465582774]`). Below `t_2` on the first
two lines and above it on the third, `6c_1 > 1` at the scanned points. So the
set `{t > 0 : 6c_1 < 1}` on a line is not a half-line: read as one, the first
threshold alone would have implied uniqueness at `(1, 1, 2)`, where `6c_1 ≈
1.959` (the contract lens's finding, folded).

**G6 (the Lipschitz lemma along a line; the certificates).** On any of the
three lines every pair weight is `t` or `1`, so for a fixed shell the
unnormalized weight of the value `s` is the monomial `t^{k_s}` with an integer
`0 ≤ k_s ≤ 6` (the number of slots whose orbit with `s` carries `t`). Writing
`a_s(t) = t^{k_s}/Z(t)`, `Z = Σ_s t^{k_s}`, one has `t a_s'(t) = a_s(t) (k_s −
k̄(t))` with `k̄ = Σ_s k_s a_s`, hence `Σ_s |a_s'(t)| ≤ (1/t) Σ_s a_s |k_s − k̄|
≤ 6/t`. For a fixed shell and pair, `TV(t) = (1/2) Σ_s |a_s(t) − b_s(t)|` is
therefore Lipschitz on `[u, v]` (`u > 0`) with constant `6/u`, and so is
`c_1(t)`, a maximum of finitely many such functions. Two exact certificates
follow (C11, C12). (i) On the isolating interval `[a, b]` of each of the six
thresholds, every one of the `252 × 15` shell-multiset-and-pair choices (the
`7776 × 15` choices up to the slot symmetry) either satisfies `max(6 TV(a),
6 TV(b)) − 1 + 36 (b − a)/a < 0`, hence stays below one on all of `[a, b]`, or
has, with its sign pattern at `a`, the same rational function as the displayed
maximizer and that sign pattern constant on `[a, b]` (no numerator of `a_s −
b_s` has a root in `[a, b]`, by Sturm's theorem), so that its total variation
equals the displayed function on all of `[a, b]` (a copy: `30, 288, 288`
copies at the first thresholds, `60, 72, 72` at the second; no distinct choice
is left unverified). Since `6c_1 − 1` is the maximum of these functions, on
`[a, b]` it equals `6f − 1` for the displayed function `f`, which has its
single root at the threshold: the threshold is the displayed root, and on the
region side of the threshold within `[a, b]` one has `6c_1 < 1`. (ii) On each
line, with `u` the upper endpoint of the lower threshold's isolating interval
and `v` the lower endpoint of the upper one, `6c_1(t) < 1` holds for every real
`t ∈ [u, v]`: a subinterval `[a', b']` is verified by `max(6c_1(a'), 6c_1(b'))
− 1 + 36 (b' − a')/a' < 0` from the exact endpoint values, and otherwise
bisected at a dyadic midpoint (`2395`, `1782`, `1715` verified subintervals on
the three lines). Together — (i) covers the parts of the two isolating
intervals on the region side of their thresholds and (ii) covers `[u, v]`
between them — the set `{t > 0 : 6c_1 < 1}` on each line contains the whole
open interval between its two thresholds; monotonicity of `c_1` is neither
proved nor needed. Finally, `c_1` is homogeneous of degree zero, so
`c_1(t, t, 1) = c_1(1, 1, 1/t)` (executed at `t = 5/4, 3/2, 7/10`, and
`c_1(2, 1, 2) = c_1(4, 2, 4)`), and the `(1, 1, t)` polynomials are the
reciprocals of the `(t, t, 1)` polynomials (C13): the third line is the second
under scale invariance, and its two thresholds are the reciprocals of the
second line's.

## Theorem H — the finite-window comparison bound by coupling (re-proved at scope)

**Statement.** Let `Λ` be a finite window with `n = |Λ|` sites, each with
interior neighbors `N_Λ(x)` and exterior slots `∂(x)`; let `ω, ω'` be two
exterior assignments and `μ = μ_Λ^ω`, `μ' = μ_Λ^{ω'}` the static laws. Let
`C_Λ` be the `n × n` matrix with entries `C_{xy}` for `y ∈ N_Λ(x)` and `0`
otherwise, and `b_x = Σ_{z ∈ ∂(x)} C_{xz} [ω_z ≠ ω'_z]`. Suppose every row sum
of `C_Λ` is at most `α_Λ < 1`. Then there is a coupling `π` of `μ` and `μ'`
with `π(η_x ≠ η'_x) ≤ (D_Λ b)_x` for every `x`, `D_Λ = Σ_{k ≥ 0} C_Λ^k =
(I − C_Λ)^{-1}`, and for every `f : M^Λ → R`,
`|μ(f) − μ'(f)| ≤ Σ_x δ_x(f) (D_Λ b)_x`, `δ_x(f)` the oscillation of `f` in
its `x` argument.

**Step 0 (the maximal coupling of two probability vectors on `M`).** For
probability vectors `a, b` on `M` put `m_s = min(a_s, b_s)` and `m = Σ_s m_s`.
Since `Σ_s (a_s − b_s) = 0`, the positive and negative parts of `a − b` have
equal mass, and that mass is `Σ_s (a_s − m_s) = 1 − m = TV(a, b)`. Define a
pair `(S, S')`: with probability `m` draw `S` from `m_s/m` and set `S' = S`;
with probability `1 − m` draw `S` from `(a_s − m_s)/(1 − m)` and,
independently, `S'` from `(b_s − m_s)/(1 − m)` (a branch of probability zero
is omitted). The marginals are `m_s + (a_s − m_s) = a_s` and `b_s`. On the
second branch `a_s − m_s > 0` forces `b_s = m_s`, so the two branch laws have
disjoint supports and `S ≠ S'`; hence `P(S ≠ S') = 1 − m = TV(a, b)`, and no
coupling does better because `P(S = S') ≤ Σ_s min(a_s, b_s)` for any
coupling. Executed: `Σ_s min(a_s, b_s) = 1 − TV` on all `5184` distinct
plaquette instances at four triples (D2).

**Step 1 (H1: one site, the triangle inequality).** Fix `x`. Let
`y_1, …, y_m` be the slots (interior or exterior) at which `(η, ω)` and
`(η', ω')` differ, and let `ζ^0 = (η, ω)`, `ζ^i = ζ^{i−1}` with slot `y_i`
set to its primed value, so `ζ^m = (η', ω')`. Total variation is half the
`ℓ^1` distance, hence a metric on probability vectors, so
`TV(r_x(·|ζ^0), r_x(·|ζ^m)) ≤ Σ_i TV(r_x(·|ζ^{i−1}), r_x(·|ζ^i)) ≤ Σ_i C_{x y_i}`,
each term being a pair of shells differing at exactly one slot. Splitting
the slots into interior and exterior,
`TV(r_x(·|η, ω), r_x(·|η', ω')) ≤ Σ_{y ∈ N_Λ(x)} C_{xy} [η_y ≠ η'_y] + b_x`.
Executed on the plaquette for the declared family (`223,616` pairs, every
site, four triples) with `C_{xy} = C_{xz} = c_1^{(4)}` (D1).

**Step 2 (the coupled random-scan chain and the disagreement recursion).**
The random-scan update on `M^Λ` with exterior `ω`: choose `X` uniformly in
`Λ`, replace `η_X` by a draw from `r_X(· | η, ω)`, leave the other sites.
Couple two copies, `(η^t)` with `ω` and `(η'^t)` with `ω'`: the same `X`;
given `(η^t, η'^t)` and `X = x`, draw `(η^{t+1}_x, η'^{t+1}_x)` from the
maximal coupling of `r_x(·|η^t, ω)` and `r_x(·|η'^t, ω')` (Step 0). Each
marginal is the random-scan chain with its own exterior. Let
`u^t_x = P(η^t_x ≠ η'^t_x)`. Since `X` is drawn independently of
`(η^t, η'^t)`,
`u^{t+1}_x = (1 − 1/n) u^t_x + (1/n) E[TV(r_x(·|η^t, ω), r_x(·|η'^t, ω'))]`
`≤ (1 − 1/n) u^t_x + (1/n) E[Σ_{y} C_{xy} 1[η^t_y ≠ η'^t_y] + b_x]`
`= (1 − 1/n) u^t_x + (1/n) ((C_Λ u^t)_x + b_x) =: Φ(u^t)_x`
by Step 1 and linearity of expectation. The affine map
`Φ(u) = (1 − 1/n) u + (1/n)(C_Λ u + b)` has nonnegative coefficients, hence
is monotone: `u ≤ v ⇒ Φ(u) ≤ Φ(v)` entrywise. By induction
`u^t ≤ Φ^t(u^0) ≤ Φ^t(1)`, since `u^0 ≤ 1`.

**Step 3 (H2: the fixed point).** The linear part of `Φ` is
`A = (1 − 1/n) I + (1/n) C_Λ`, with row sums at most
`(1 − 1/n) + α_Λ/n = 1 − (1 − α_Λ)/n < 1`, so `Φ` is a contraction in the
maximum norm and `Φ^t(v)` converges to its unique fixed point `u*` from every
start `v`. `Φ(u*) = u*` reads `(1/n)(I − C_Λ) u* = (1/n) b`; because
`‖C_Λ‖_∞ ≤ α_Λ < 1` the Neumann series `D_Λ = Σ_{k ≥ 0} C_Λ^k` converges,
equals `(I − C_Λ)^{-1}`, and is entrywise nonnegative; hence `u* = D_Λ b ≥ 0`.
When moreover `C_Λ 1 + b ≤ 1` entrywise — the case whenever every slot of
every site carries one coefficient `c` and the slot count times `c` is below
one, as on the executed windows — `Φ(1) ≤ 1`, and by monotonicity the
iterates `Φ^t(1)` decrease to `u*`. Executed on the `3×3` window at the three
region triples: `D_Λ` by exact inversion over the rationals with
`D_Λ (I − C_Λ) = I` and `D_Λ ≥ 0` (D4); the `200` damped iterates from
`u^0 = 1` nonincreasing, at or above `u*`, and within `10^{-4}` of `u*` at
the last step (D5); the identity `u* = (8/9) u* + (1/9)(C_Λ u* + b)` exact
(D6).

**Step 4 (H3: stationarity of the static law under single-site
resampling).** Let `P_x` be the kernel that resamples site `x` from
`r_x(· | ·, ω)` and `P = (1/n) Σ_x P_x` the random-scan kernel. For
`ζ ∈ M^Λ`,
`(μ P_x)(ζ) = Σ_s μ(ζ^{x→s}) · r_x(ζ_x | ζ_{Λ∖x}, ω) = μ_{Λ∖x}(ζ_{Λ∖x}) · μ(ζ_x | ζ_{Λ∖x}) = μ(ζ)`,
where the middle equality is block 01's Theorem A: the full conditional of
`μ_Λ^ω` at `x` is exactly the rule with every neighbor recorded (direct
cancellation), and `Σ_s μ(ζ^{x→s})` is the marginal on `Λ ∖ x`. Hence
`μ P = μ`, and likewise `μ' P' = μ'` with the exterior `ω'`. Positivity of
the rule enters here through Theorem A: every conditional is a probability
vector with full support, the static law is positive, and its uniqueness
among laws with those conditionals (the finite-menu Brook lemma, re-proved in
block 01) makes "the static law of `Λ` with exterior `ω`" one object; the
invariance itself uses only the full-conditional identity.

**Step 5 (the limit coupling).** Start the coupled chain of Step 2 with
`(η^0, η'^0)` any coupling of `μ` and `μ'` (independent, say). By Step 4,
`η^t ~ μ` and `η'^t ~ μ'` for every `t`, so the joint law `π_t` of
`(η^t, η'^t)` is a coupling of `μ` and `μ'` for every `t`, and by Step 2
`π_t(η_x ≠ η'_x) = u^t_x ≤ Φ^t(1)_x`. The `π_t` are points of the simplex of
probability vectors on the finite set `M^Λ × M^Λ` (the finite menu is used
here); a bounded sequence in a finite-dimensional space has a convergent
subsequence (extract coordinate by coordinate, finitely many times); let
`π` be a subsequential limit. Marginals are finite sums and pass to the
limit, so `π` is a coupling of `μ` and `μ'`; and
`π(η_x ≠ η'_x) = lim_k π_{t_k}(η_x ≠ η'_x) ≤ lim_k Φ^{t_k}(1)_x = u*_x`.
So `π(η_x ≠ η'_x) ≤ (D_Λ b)_x` entrywise.

**Step 6 (the bound on `|μ(f) − μ'(f)|`).** For `f : M^Λ → R` and the
coupling `π`, `μ(f) − μ'(f) = E_π[f(η) − f(η')]`. Order `Λ` as
`x_1, …, x_n` and let `ζ^i` agree with `η'` on `x_1, …, x_i` and with `η`
elsewhere (`ζ^0 = η`, `ζ^n = η'`). Then
`f(η) − f(η') = Σ_i (f(ζ^{i−1}) − f(ζ^i))`; the `i`-th term vanishes unless
`η_{x_i} ≠ η'_{x_i}` and is then at most `δ_{x_i}(f)` in absolute value,
`δ_x(f) = sup { |f(ζ) − f(ζ')| : ζ, ζ' differ only at x }`. Taking
expectations, `|μ(f) − μ'(f)| ≤ Σ_x δ_x(f) π(η_x ≠ η'_x) ≤ Σ_x δ_x(f) (D_Λ b)_x`. ∎

**The center-site instance (executed).** For the center `c` of the `3×3`
window, `TV(μ_c, μ'_c) = max_A (μ(η_c ∈ A) − μ'(η_c ∈ A))`, and for any
coupling `μ_c(A) − μ'_c(A) = π(η_c ∈ A, η'_c ∉ A) − π(η_c ∉ A, η'_c ∈ A) ≤
π(η_c ≠ η'_c)`, so `TV(μ_c, μ'_c) ≤ (D_Λ b)_c`. The exact center-site marginals
under the two exterior assignments are computed by integer row transfer over
the `216` row states (D7): at `(2, 1, 2)`, `c_1^{(4)} = 1/8`, `TV =
691410442136477999520/76730168638463067377251 ≈ 0.0090109 ≤ 1/56`; at `(3, 2,
2)`, `c_1^{(4)} = 1404/11431`, `TV ≈ 0.0073929 ≤ 1971216/114898033 ≈
0.0171562`; at `(5, 4, 4)`, `c_1^{(4)} = 10000/175641`, `TV ≈ 0.0016901 ≤
100000000/30049760881 ≈ 0.0033278` (decimal labels truncated; exact rationals
under `--exact`). At `(3, 1, 2)`, `c_1^{(4)} = 918/3431` and the center row sum
`4c_1^{(4)} = 3672/3431` exceeds one: the window bound is not asserted; the
exact `TV ≈ 0.0346753` is recorded, not used (D8).

## Theorem I — exactly one static law on `Z^3` where `6c_1 < 1` (corollary)

**Statement.** If `α = 6c_1(p, q, r) < 1` then the specification of the
covariant product rule on `Z^3` has exactly one infinite-volume static law.

*Proof.* Block 02's Theorem C2 gives at least one. Let `μ, ν` be two. Let
`f` be a local function, depending on the sites within `ℓ^1` distance `ℓ` of
the origin (the box `Δ_ℓ`), and let `Λ_L` be the box of side `2L + 1`
centered at the origin, `L > ℓ`. The finite-window conditional identity with
`Δ = Λ_L` gives `μ(f) = Σ_b μ_{Λ_L}^b(f) μ(v_{∂Λ_L} = b)` and
`ν(f) = Σ_{b'} μ_{Λ_L}^{b'}(f) ν(v_{∂Λ_L} = b')` (finite sums over the
records `b, b'` on the exterior neighbors of `Λ_L`), so
`μ(f) − ν(f) = Σ_{b, b'} μ(b) ν(b') (μ_{Λ_L}^b(f) − μ_{Λ_L}^{b'}(f))` and
`|μ(f) − ν(f)| ≤ sup_{b, b'} |μ_{Λ_L}^b(f) − μ_{Λ_L}^{b'}(f)|`. On `Λ_L`
every site has the full six-slot shell (interior neighbors plus exterior
records), so by G1 every coefficient is `c_1`, `C_Λ = c_1 · (adjacency of
Λ_L)` has row sums at most `6c_1 = α < 1`, Theorem H applies, and
`b_y ≤ c_1 · #{exterior neighbors of y} ≤ 6c_1 · 1[y ∈ ∂_in Λ_L]`. Hence
`|μ_{Λ_L}^b(f) − μ_{Λ_L}^{b'}(f)| ≤ 6c_1 Σ_{x ∈ Δ_ℓ} δ_x(f) Σ_{y ∈ ∂_in Λ_L} (D_Λ)_{xy}`.
Now `(C_Λ^k)_{xy} = c_1^k · #{nearest-neighbor walks of length k from x to y inside Λ_L} ≤ c_1^k N_k(x, y)`,
`N_k` the count of such walks in `Z^3` (sites may repeat), and `Σ_y N_k(x, y) = 6^k` because
every one of the `6^k` direction sequences ends somewhere (executed for
`k ≤ 4`, E1). A walk from `x ∈ Δ_ℓ` to `y ∈ ∂_in Λ_L` has length at least
`L − ℓ`, so
`Σ_{y ∈ ∂_in Λ_L} (D_Λ)_{xy} = Σ_k Σ_{y ∈ ∂_in Λ_L} (C_Λ^k)_{xy} ≤ Σ_{k ≥ L − ℓ} (6c_1)^k = α^{L − ℓ}/(1 − α)`.
Therefore `|μ(f) − ν(f)| ≤ 6c_1 (Σ_x δ_x(f)) α^{L − ℓ}/(1 − α)`, which tends
to zero as `L → ∞` because `α < 1`. Hence `μ(f) = ν(f)` for every local
`f`, i.e. `μ` and `ν` agree on every cylinder event; two probability
measures on the product σ-algebra that agree on the cylinder algebra (a
π-system generating it) coincide (uniqueness of the Carathéodory extension,
cited under Imports). ∎ Executed: the table `α^L/(1 − α)`, `L = 1..12`, exact
at the four region triples (E2); the least `L` with `α^L/(1 − α) < 10^{-3}`:
`119`, `39`, `8`, `4` at `(2, 1, 2)`, `(3, 2, 2)`, `(5, 4, 4)`, `(11, 10, 10)`
(E3).

## The region, stated

For the covariant product rule at `(2, 1, 2)`, `(3, 2, 2)`, `(5, 4, 4)` and
`(11, 10, 10)` — `6c_1 = 12/13, 6237/7783, 8000000/20461907, 196482220000/1514687593537`
— the rule induces exactly one static law on `Z^3` (Theorem I with C2). On
the three lines the same holds for every real `t` strictly between the two
thresholds (G6, C12): on `(t, 1, 1)` for `√30 − 5 < t < t*`, `t* ≈ 1.6097`;
on `(t, t, 1)` for `t_2 < t < t*`, `t_2 ≈ 0.6917`, `t* ≈ 1.4775`; on
`(1, 1, t)` for `t* < t < t_2`, `t* ≈ 0.6768`, `t_2 ≈ 1.4458`, the reciprocal
of the previous interval. The executed rational points (E4; `6c_1` as a
decimal label) lie inside: `(t, 1, 1)`: `t = 9/8` (`0.1700`), `5/4` (`0.3909`;
this is `(5, 4, 4)`), `11/8` (`0.5999`), `3/2` (`0.8013`; this is
`(3, 2, 2)`); `(t, t, 1)`: `9/8` (`0.2682`), `5/4` (`0.5388`), `11/8`
(`0.8012`); `(1, 1, t)`: `3/4` (`0.7159`), `7/8` (`0.3071`), `1` (`0`, the
constant rule). Beyond the thresholds on each line, at the scanned points,
`6c_1 > 1` and the criterion is silent; nothing is stated there. At
`(3, 1, 2)` (`6c_1 = 1620/989`), `(5, 2, 4)` (`6c_1 ≈ 1.2778`) and `(7, 3, 5)`
(`6c_1 ≈ 1.2805`) the criterion is silent; nothing is stated about one law or
several.

## No-Go Discipline Gate

The only negative-shaped sentence in this note is "at the silent triples the
criterion decides nothing", a scope statement about one executed criterion, not
a claim that any route fails; no no-go is shipped. The gate is answered for it
briefly.

### N1 — Routes toward the silent triples (none attempted here; each with its obligation)

| route | what it would attempt | its terminal obligation | marker |
|---|---|---|---|
| 1 the two-site block condition | contract on a two-site block with its ten-slot boundary instead of one site | the block's exact coefficients (a supremum over `6^{10}` boundary shells and the block's own static law) and a row sum below one at `(3,1,2)`, `(5,2,4)` | not attempted; obligation named |
| 2 disagreement percolation | bound the disagreement cluster of the coupled chains by a site-percolation process | a proved percolation threshold bound on `Z^3` compared with the per-site disagreement probability; no exact in-framework percolation bound exists | not attempted; obligation named |
| 3 a transfer-matrix route on slabs | a spectral gap of the slab transfer matrix uniform in the slab width (block 02 executed width 3 only) | uniformity in the width, which finite widths do not give | not attempted; obligation named |
| 4 a cluster or high-temperature expansion | expand the static law around the constant rule and prove convergence at the silent triples | a convergent polymer bound at `(3,1,2)`, `(5,2,4)` | not attempted; obligation named |
| 5 direct comparison on growing boxes | compute the center-site marginal under two boundary records on boxes of growing side and watch the gap | an exact statement in the limit, which finite boxes do not supply | not attempted; obligation named |

The routes differ in primary object, mechanism and terminal obligation. Since
no no-go is claimed, none needs to fail; they are the next question.

### N2 — Wall-independence audit

Walls: `W_crit` (`6c_1 < 1`), `W_pos` (positivity), `W_var` (not all equal on
the declared menu), `W_menu` (the finite menu), `W_spec` (block 02's
conditional identity as the definition of an infinite-volume static law).
`W_crit`/`W_var`: neither implies the other. The constant rule satisfies
`W_crit` only and fails `W_var`; `(3,1,2)` satisfies `W_var` only; the
nonconstant weak-coupling triple `(5,4,4)` satisfies both. `W_pos`/`W_crit`: independent (a zero pair weight is
not excluded by the coefficient; `W_pos` is what Theorem A needs). `W_menu`
enters only through the finite state spaces of Theorem H and the finite sums
of Theorem I; `W_spec` is the definition of the object. The finite-menu, positive-product specification defines the domain of the
proof. The uniqueness implication uses `W_crit` and also holds at the constant
rule; `W_var` is not a necessary premise of Theorems H and I.

### N3 — Hidden-wall scan

Scanned for "we assume", "by construction", "as is standard", "the framework
provides", "naturally", "obviously", "canonical", "registered", "background",
"bridge context". Hits: "registered" only in N6. Every step of Theorems H and
I is written out; the one cited step (uniqueness of the extension from the
cylinder algebra) is named in the obligation table and under Imports. No wall
was promoted.

### N4 — Per-citation table

| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 01's note (proposed, unaudited): Theorem A | the static law of a finite window with its full conditionals; its uniqueness | the full-conditional identity used in H3 | yes (parent; cited) |
| block 02's note (proposed, unaudited): Theorem C2 and the conditional identity | existence of an infinite-volume static law | the identity used in Theorem I; existence | yes (parent; cited) |
| the classical one-site contraction criterion and comparison theorem | uniqueness of the Gibbs measure under a contraction condition | re-proved at scope (H, I) | yes (re-proved; no value imported) |
| the `WILSON_STAGGERED_*` constrained-fiber note of 2026-07-12 (named in full under Prior art) | a contraction bound on a constrained polymer fiber of the Wilson-staggered block map | none (prior in-repo use on a different carrier; quotes the theorem) | no; not a witness |
| uniqueness of the Carathéodory extension from the cylinder algebra | two measures agreeing on a generating π-system coincide | the last step of Theorem I | yes (cited, definition-level) |

After dropping the non-match, the headline rests on the parents' cited statements and this note's own proofs and executed witnesses.

### N5 — Resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "at the silent triples the criterion decides nothing" | executed: all `7776 × 15` choices at both triples give `6c_1 ≥ 1` | executed: the six directions carry the same coefficient | executed: `D_Λ`, the iterates, the Sturm isolation | executed: the `3×3` window's row sum exceeds one at `(3,1,2)` | proved, not executed: the corollary applies only where `6c_1 < 1`; the silent triples are named, not decided |

The runner prints matching `per_element:` … `lattice_wide:` lines; the narrowest form is used.

### N6 — Partial-closure paths and primitive scan

The registered approved primitives in
`docs/audit/data/axiom_premise_nodes.json` (`scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`) supply a length
reference, a graining ratio and a realized-state notion; none supplies a pair
weight or a uniqueness criterion, and none is a wall here. Reframing paths: a
sharper criterion (N1) could decide the silent triples without any change of
reading; `docs/repo/DEFERRED_DECISIONS.md` entry 1 wakes on the committed-
action identification, which this note does not supply. This note does not say
a new axiom is required.

### N7 — Steelman

Hostile reviewer: "The one-site criterion is crude; `(3,1,2)` and `(5,2,4)`
are moderate couplings for a six-state nearest-neighbor model in three
dimensions, and the two-site block condition, a percolation argument or a
convergent expansion may well give a single static law there too; the silent
triples are silent only because the cheapest test was used." Conceded in full:
this note claims nothing at the silent triples and names the sharper routes as
the next question. The steelman defeats any reading of "silent" as "not one
law", which this note does not make; it does not touch the region statement.

### N8 — Cross-cycle echo

| similar prior wall | retired? | mechanism | applies here? |
|---|---|---|---|
| the `WILSON_STAGGERED_*` contraction controls (2026-07-12): a contraction condition on a constrained fiber, silent outside its wedge | no (unaudited) | none | a different carrier; its footprint bound is not a mechanism for the menu rule's silent triples |
| block 02's "uniqueness on `Z^3` is the next block's object" | addressed here in the region | Theorems H and I | yes — the mechanism is this note; the silent triples remain |

No structurally similar wall was retired by a mechanism not considered here.

**Gate result:** PASS for the scope sentence; no no-go is shipped; nothing is
claimed at the silent triples in either direction.

## Falsifiers

The theorems fail if any of these finite statements fails: a direction-
dependent coefficient; the relabeling identity failing; `c_1 ≠ 0` at `(2,2,2)`
or `c_1 = 0` at a non-constant triple; a literal, a region or silent
classification, a grid symmetry or the diamond differing; a crossing outside
its bracket, a sign pattern not fixed, a numerator not a constant multiple of
the displayed polynomial, a positive-root count other than one, no sign change
on the isolating interval, an endpoint supremum not attained by the displayed
pattern; a second crossing outside its bracket or with a numerator not a
constant multiple of its displayed polynomial; a distinct choice unverified on
an isolating interval or a copy count differing; a region certificate failing;
a reciprocity or scale-invariance identity failing; `c_1^{(4)}(2,5,3) ≤
c_1(2,5,3)`; `6c_1(7,3,5) < 1`; the plaquette inequality or the coupling identity failing; a
`c_1^{(4)}` literal or row-sum classification differing; `D_Λ (I − C_Λ) ≠ I`, a
negative entry of `D_Λ`, non-monotone iterates, a broken fixed-point identity,
a center-site total variation above `(D_Λ b)_c`; `Σ_y N_n(0, y) ≠ 6^n` for some
`n ≤ 4`; the table's recursion failing; a declared line point with `6c_1 ≥ 1`.

## Boundaries and non-claims

This note states uniqueness only where the one-neighbor influence sum is less than one, at the declared points and throughout the verified intervals; at the three silent triples the criterion decides nothing, and nothing is stated there about one law or several.

No formation order, formation law, plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The criterion and the coupling method are classical references re-proved here at the scope used; no value, constant or theorem is imported as authority.

Every negative sentence in this note is an exact statement on the declared windows, triples and lines or the scope sentence about the silent triples; none is a route no-go beyond that scope.

Further: the verified domain consists of the open interval between the two
exact thresholds on each line, together with the exact pointwise grid and
scan values. G6 proves inclusion of those whole intervals in `6c_1 < 1`;
outside them only the declared sampled values are checked. Monotonicity and
an exhaustive characterization of the positive whole-line locus are not
proved. Even a full criterion locus would not be the sharp boundary of
uniqueness, which may hold outside it (N7). The
thresholds are roots of the displayed polynomials, verified against every
competitor on their isolating intervals; the maximizing patterns are
lexicographically first, ties counted, not excluded; Theorem H is executed on planar windows with four slots per
site (`c_1^{(4)}`) while Theorem I uses the six-slot shell (`c_1`); the
monotone decrease of the iterates needs `C_Λ 1 + b ≤ 1`, satisfied on the
executed windows; the `3×3` bound at `(3,1,2)` is not asserted; no sharper
criterion is attempted; both parents are proposed and unaudited, so their cited
statements are upstream evidence, not retained authority; no axiom or primitive
is changed.

## Imports

References, re-proved at scope, never authority, no values imported: the
one-site contraction criterion of Dobrushin (1968–1970) with its
comparison-theorem form — re-proved above by the random-scan coupling
(Theorem H) and the walk-count corollary (Theorem I); the coupling method
(maximal coupling of two laws on a finite set, the coupling inequality) —
proved above where used. Cited, not re-proved: uniqueness of the Carathéodory extension from the
cylinder algebra (the last step of Theorem I; block 02 cites the existence
half). The Lipschitz lemma of G6 is native.
Declared mathematical scaffolding: Sturm's theorem, real-root
isolation and exact rational matrix inversion as implemented in `sympy`
(exact rational arithmetic; the runner checks each root count, each sign
change and the inverse identity itself); the exact weight triples, the
scan rationals `1 + k/8`, `k/8`, `1 − k/40` and `1 + k/20`, the isolation width
`10^{-20}`, the dyadic bisection of G6, the
window exterior assignments, the configuration family with block 01's linear
congruential generator, `200` damped iterations with tolerance `10^{-4}`,
the table length `L = 1..12`. No observation, fitted value or literature
constant enters.

## Review record

Fable primary seat (own 26-mutation census from raw per-mutation stdout);
refuting checker (Opus 5, disjoint machinery: brute-force coefficients, own row
transfer and Gauss–Jordan inverse, own walk counts and hash re-implementation):
PASS-NO-BLOCKER, nothing refuted — every literal, threshold, copy count, window
bound and cache hash reproduced; 1,344 rationals between the thresholds and
1,110 outside scanned without a counterexample; 1,080 window site-checks
without a bound violation; two presentational findings folded (the sign-
constancy clause of the copy test, C11; the sentence joining the two
certificates in G6). Independence class: single family (Claude), cross-model
— Fable primary, Opus 5 contract lens, Opus 5 refuting checker, supervisor
hand-verification.
The supervisor's control numbers (the seven coefficients, the `(t,1,1)`
crossing between `3/2` and `13/8` with its pattern, the `3×3` total variation
against `1/56`) were reproduced in the seat's own integer code before any
theorem sentence was written. Settled while executing: the grid extends to
`1..12` (one coefficient costs `0.06` s, the `144`-point grid `9` s; nothing
was cut); the monotone decrease of the damped iterates needs `C_Λ 1 + b ≤ 1`,
stated in H2; the least `L` with `α^L/(1 − α) < 10^{-3}` is `119` at `(2,1,2)`,
beyond the table's `L = 12`, so both are printed.

Supervisor fold (2026-09-06, after the Opus 5 contract refuter lens): the lens
reproduced every control number on its own code and found in the contract the
"second real root" (each polynomial has three real roots; the positive one),
a second crossing of `6c_1 = 1` on each line, the window coefficient not
bounded by `c_1` (`(2, 5, 3)`), the endpoint-only dominance gap, the pointwise
line statement, "paths" for "walks", the maximizer not being unique, the `(7, 3, 5)`
silent triple, and the iterate-decrease step needing `C_Λ 1 + b ≤ 1` (already
stated by the primary in H2); folded as G5′, G6, C10–C14, five mutations and
the wording above. The fold's certificates were prototyped in the supervisor's
control before the runner was patched.

## Verification

```bash
python3 scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py
python3 scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py --list-mutations
python3 scripts/admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_2026_09_06.py --mutation region_certificate_forged
```

Families: A authority and inputs; B menu, rule and symmetry (G1–G3); C the
coefficient (G4–G6); D the coupling (H1–H3); E the corollary (I); F fences,
the author-name section rule and the floating-point self-scan; G the
resolution certificate. Each of the 31 declared mutations perturbs one object
at construction time and fails in exactly one family
(`mutation_family_expected:` / `mutation_family_observed:` lines); `--exact`
prints the exact rationals, the grid map, the polynomials, the isolating
endpoints, `u*` and the center row of `D_Λ`.
Expected final line: `TOTAL: PASS=41 FAIL=0`.

## Source-review corrigendum — 2026-09-07

Narrowed whole-line wording to the verified intervals and exact sampled/grid values; a global exclusion outside the intervals remains unproved. Corrected the constant-rule wall witness and made explicit that nonconstancy is not needed for the uniqueness implication. The runner fence is aligned with the intervals and three silent triples; its computations are unchanged.

The earlier review record is preserved as history. These corrections amend the
current source claims; they do not apply audit status. The packet
`REVIEW_HISTORY.md` records the finding-to-change map and original source head.
