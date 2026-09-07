---
claim_id: admissibility_rule_two_site_block_criterion_exact_and_silent_for_every_coupling_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule of orbit weights (p, q, r): the two-site block V = {x, y} of Z^3 with its ten boundary slots; the block law's x-marginal sensitivity rho to one outer slot and the y-marginal's second-order sensitivity rho', exactly, at (3,1,2), (5,2,4), (7,3,5), (2,1,2), (3,2,2), (5,4,4); the factorization of the block law under a change at an x-slot (Theorem O); the lower bound of the Hamming coupling distance by the marginal total variations for every coupling (Theorem N), hence the block sum B_V >= 10(rho + rho') > 2 = |V| at each of the three silent triples: the two-site block criterion is silent there for every coupling; the explicit sequential coupling and its upper bound 10 rho (1 + c_1); the block-scan contraction on a finite window (Theorem M) with its infinite-lattice implication left unproved; the scans along (t,1,1) and (t,t,1); nothing about one law or several at the silent triples; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py
---

# The two-site block criterion of the rule, exactly: silent at the silent triples for every coupling

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py`](../scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.txt`](../logs/runner-cache/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.txt)

## Result up front

The one-site test of the previous note adds up how much each of a site's six
neighbours can shift its odds, and decides "one static law" when the total is
under one. At three couplings the total is over one and the test says nothing.
The cheapest sharper test looks at a pair of adjacent sites together: it asks
how much each of the pair's ten outer neighbours can shift the pair's joint
odds, adds that up, and compares the total with the pair's size, two. We
computed the pair's sensitivities exactly. Averaging over one partner barely
helps: the pair's marginal is as sensitive to an outer neighbour as a lone site
is, and at one coupling slightly more. Every way of matching up the pair's two
laws must disagree at each site at least as often as that site's own marginal
does, so the pair total is at least ten times the marginal sensitivity, which is
above two at all three couplings. The pair test is silent there no matter how it
is run. Nothing is said about whether one law or several exist at those
couplings.

Exactly: for the pair block `V = {x, y}` with boundary `∂V` (five outer slots
of `x`, five of `y`), the sensitivity `ρ` of the block's `x`-marginal to one
outer `x`-slot is `2168397/7948400 ≈ 0.27281` at `(3, 1, 2)` (`c_1 = 270/989 ≈
0.27300`), `271059507090000/1298168979740633 ≈ 0.20880` at `(5, 2, 4)`,
`239957740750/1121635870169 ≈ 0.21394` at `(7, 3, 5)`; the ratios `ρ/c_1` are
`0.9992`, `0.9804`, `1.0024`. The second-order sensitivity `ρ'` of the
`y`-marginal to an `x`-slot is `1350/26077`, `1915425000/55627392667`,
`856455908/27833079009`. For every coupling of the two block laws the expected
Hamming distance is at least `TV(m_x) + TV(m_y)` (Theorem N), so the block sum
`B_V = Σ_{z ∈ ∂V} sup W_1 ≥ 10(ρ + ρ') = 3.2457…, 2.4323…, 2.4470…`, above the
block size `2`: the two-site block criterion is silent at the three silent
triples for every coupling. The explicit sequential coupling gives `B_V ≤ 10ρ(1
+ c_1) = 3.4728…, 2.5327…, 2.5959…`; at the region triples that upper bound is
`1.7517…, 1.4966…, 0.6676…`, below `2`. On a finite window the random block
scan contracts the total disagreement exactly when `B_V < 2` (Theorem M); its
infinite-lattice implication is not proved here and nothing on `Z^3` is claimed
from it. Along `(t, 1, 1)` and `(t, t, 1)` the sequential number `5ρ(1 + c_1)`
crosses `1` in the same scan cell as `6c_1`, and `ρ` exceeds `c_1` from `t =
39/20` and `t = 3/2`. Executed with exact arithmetic: 21 checks, 16 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 03's next question: the silent triples (3,1,2), (5,2,4), (7,3,5) under a sharper criterion, the two-site block condition first"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the two-site route is closed for every coupling; the remaining routes to the silent triples are larger planar blocks (not exactly computable at this menu), a transfer-matrix or expansion route, or an ordering argument on the other side; consumers: the campaign's queue and the parked statistical-bridge decision material (read-only)"
conditional_surface_status: "exact at the six triples and on the declared scans; Theorem N and Theorem O proved for the pair block; Theorem M proved on finite windows only; nothing at the silent triples about one law or several; no plane, no formation law, no bridge"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "the sensitivities are exact executed computations; Theorem N is a two-line coupling inequality executed on the declared family; Theorem O is an exact factorization executed on every instance at one triple; Theorem M is a finite-window contraction statement with its Z^3 implication explicitly left open; the silence at the silent triples is a finite exact statement for every coupling; nothing about several laws, a transition, a physical rule, the plane, the bridge, the Born form or gravity is claimed."
```

## Premises and declared objects

The scientific dependencies are the four axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and block 03
[`ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOU
NDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE
_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md) (proposed,
unaudited; its coefficient `c_1`, its region and its silent triples are used
as executed values, recomputed here). The axiom sentences used, verbatim
(runner A2): "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations." — "For each
site, the probability distribution over the possibilities is determined by,
and varies with, the nearest-neighbor conditions." — "Records form." — "Only
records are readable."

**Menu and rule.** As in blocks 01–03: the six projectors `P(±e_a)`, the pair
orbits parallel/antiparallel/orthogonal with weights `φ ∈ {p, q, r}`, positive,
not all equal; the product rule `r_x(s | η) ∝ Π_y φ(s, η_y)`. Triples: the
silent triples `(3, 1, 2)`, `(5, 2, 4)`, `(7, 3, 5)` and the region triples
`(2, 1, 2)`, `(3, 2, 2)`, `(5, 4, 4)` of block 03. No formation order enters.

**The pair block.** `V = {x, y}`, `y = x + e`. Its boundary `∂V` has ten
slots: `∂x`, the five neighbors of `x` other than `y`, and `∂y`, the five
neighbors of `y` other than `x`; `Z^3` is bipartite, so no site is adjacent to
both. With exterior records `ω` on `∂V` the block law is
`μ_V^ω(s_x, s_y) ∝ φ(s_x, s_y) Π_{z ∈ ∂x} φ(s_x, ω_z) Π_{z ∈ ∂y} φ(s_y, ω_z)`,
with marginals `m_x^ω`, `m_y^ω` and the conditional `K^ω(s_y | s_x) ∝ φ(s_x,
s_y) Π_{z ∈ ∂y} φ(s_y, ω_z)`, which does not depend on `ω_{∂x}`. Block 01's
Theorem A applies to `V` as a window: `μ_V^ω` is the unique law whose full
conditionals are the rule.

**Sensitivities.** `ρ = sup TV(m_x^ω, m_x^{ω'})` over `ω, ω'` differing at one
slot of `∂x` (by the rotation and reflection symmetries of the block the same
number serves every slot of `∂x`, and `∂y` with `m_y`); `ρ' = sup TV(m_y^ω,
m_y^{ω'})` over the same pairs. Executed as suprema over the `252` multisets of
`∂y` values, the `126` multisets of the other four `∂x` values and the `15`
unordered pairs at the varied slot (the conditional is a symmetric function of
each shell). `c_1` is block 03's coefficient, recomputed (C1).

**Couplings and the block sum.** `d_H` is the Hamming distance on `M^V`;
`W_1(μ, ν) = min_π E_π d_H` over couplings `π` (a minimum: the couplings form
a compact polytope and `E_π d_H` is linear); `b_V(z) = sup_{ω ~ ω' at z} W_1(μ_V^ω,
μ_V^{ω'})`; `B_V = Σ_{z ∈ ∂V} b_V(z)`. `W_1` is not computed exactly; it is
bounded below (Theorem N) and above (the sequential coupling).

**The declared instance family.** `200` boundary instances from a fixed linear
congruential generator (seed `20260907`, multiplier `1103515245`, increment
`12345`, modulus `2^31`, eleven draws per instance, `(state >> 16) mod 6`, the
pair at the varied slot required distinct) plus the maximizing instance of `ρ`
at `(3, 1, 2)`.

## Prior art and what is new

Block 03 (linked above) computed the one-site coefficient, proved the one-site
criterion by a random-scan coupling and named the two-site block condition as
the first sharper route. The block criterion re-proved on finite windows here
is classical: the constructive block condition of Dobrushin and Shlosman,
referenced by the authors' names once and re-proved at the scope used
(Theorem M); the Hamming coupling distance is the Vaserstein distance of the
same literature. No value, constant or theorem is imported. No landed note
computes the pair block's sensitivities for this rule or states the
obstruction; the prior-art sweep of block 03 (`ROUTE_PORTFOLIO.md`) covers the
criterion's in-repo uses, all on other carriers.

New here: the exact pair-block sensitivities and their ratio to the one-site
coefficient; the factorization theorem (O); the marginal lower bound for every
coupling (N) and its consequence, the silence of the two-site criterion at the
three silent triples independent of any proof of the criterion; the explicit
sequential coupling with its exact upper bound; the finite-window block-scan
contraction (M) with its implication left open; the scans along two lines.

## Exact target and obligation graph

**Target.** `B_V > |V| = 2` at each of `(3, 1, 2)`, `(5, 2, 4)`, `(7, 3, 5)`,
for every coupling of the two block laws — the two-site block criterion is
silent there — with the sensitivities and bounds exact.

| obligation | disposition |
|---|---|
| the block law with exterior records and its uniqueness among laws with those full conditionals (Theorem A) | cited (block 01 through block 03, unaudited) |
| the one-site coefficient `c_1` at the six triples | recomputed here (C1) |
| `TV(μ_V^ω, μ_V^{ω'}) = TV(m_x^ω, m_x^{ω'})` for a change at an `x`-slot (O) | proved; executed on all `476,280` instances at `(3, 1, 2)` (B1) |
| `P_π(η_x ≠ η'_x) ≥ TV(m_x, m'_x)` for every coupling (N) | proved; the sequential coupling executed on `201` instances (B2, B3) |
| the sequential coupling's upper bound `W_1 ≤ TV(m_x)(1 + c_1)` | proved; executed (B4) |
| `ρ`, `ρ'` exactly; `B_V ∈ [10(ρ + ρ'), 10ρ(1 + c_1)]`; `> 2` at the silent triples, `< 2` at the region triples | executed (C2–C6) |
| the finite-window block-scan contraction iff `B_V < 2` (M) | proved on the interior of a finite window; the `Z^3` implication open |
| the scans along `(t, 1, 1)`, `(t, t, 1)` | executed (D1, D2) |
| a criterion deciding the silent triples | open; not this note |

## Theorem O — the block law factors across the pair

**Statement.** For `z ∈ ∂x` and `ω, ω'` differing only at `z`,
`TV(μ_V^ω, μ_V^{ω'}) = TV(m_x^ω, m_x^{ω'})`.

*Proof.* `μ_V^ω(s_x, s_y) = m_x^ω(s_x) K^ω(s_y | s_x)` by the definition of the
conditional, and `K^ω = K^{ω'}` because `K^ω` involves `ω` only through
`ω_{∂y}`. For two laws of the form `a ⊗ K` and `b ⊗ K` with the same kernel,
`Σ_{s_x, s_y} |a(s_x) K(s_y | s_x) − b(s_x) K(s_y | s_x)| = Σ_{s_x} |a(s_x) −
b(s_x)| Σ_{s_y} K(s_y | s_x) = Σ_{s_x} |a(s_x) − b(s_x)|`. ∎ Executed on every
boundary instance and every pair at `(3, 1, 2)` (B1).

## Theorem N — the marginal lower bound holds for every coupling

**Statement.** Let `π` be any coupling of two laws `μ, ν` on `M^V`. Then
`P_π(η_x ≠ η'_x) ≥ TV(μ|_x, ν|_x)` for every `x ∈ V`, hence `E_π d_H ≥ Σ_{x ∈ V}
TV(μ|_x, ν|_x)` and `W_1(μ, ν) ≥ Σ_x TV(μ|_x, ν|_x)`. Consequently `b_V(z) ≥
ρ_z + ρ'_z` for each slot and `B_V ≥ 10(ρ + ρ')`.

*Proof.* For any set `A ⊂ M`, `μ|_x(A) − ν|_x(A) = P_π(η_x ∈ A) − P_π(η'_x ∈ A)
= P_π(η_x ∈ A, η'_x ∉ A) − P_π(η_x ∉ A, η'_x ∈ A) ≤ P_π(η_x ≠ η'_x)`; taking `A`
the set where `μ|_x ≥ ν|_x` gives `TV`. Summing over `x` and taking the minimum
over `π` gives the `W_1` bound; the supremum over pairs at a slot gives `b_V(z)
≥ ρ_z + ρ'_z`, and the slot symmetry gives the sum. ∎

**Consequence (the silence).** `10(ρ + ρ') = 3.2457…, 2.4323…, 2.4470…` at
`(3, 1, 2)`, `(5, 2, 4)`, `(7, 3, 5)` (C5), all above `2 = |V|`. Whatever
coupling a proof of the block criterion may use, and whatever the criterion's
infinite-lattice consequence, the two-site block sum exceeds the block size at
each silent triple: the two-site block criterion decides nothing there. This is
a finite exact statement, not a route no-go beyond the two-site block.

**The sequential coupling (the upper bound).** Given `ω ~ ω'` at `z ∈ ∂x`,
draw `(s_x, s'_x)` from the maximal coupling of `m_x^ω, m_x^{ω'}` (block 03,
Step 0), then `(s_y, s'_y)` from the maximal coupling of `K(· | s_x)` and
`K(· | s'_x)` (the same kernel, by Theorem O). Both marginals are the block
laws; `P(s_x ≠ s'_x) = TV(m_x^ω, m_x^{ω'})`; when `s_x = s'_x` the two `y`-laws
coincide and `s_y = s'_y`; when `s_x ≠ s'_x`, `P(s_y ≠ s'_y) = TV(K(· | s_x),
K(· | s'_x)) ≤ sup_{s ≠ s'} TV(K(· | s), K(· | s')) ≤ c_1`, since `K(· | s)` is
the six-slot conditional of `y` with the `x`-slot at `s` and the other five
slots fixed, and `c_1` is the supremum over one-slot changes. Hence `E d_H ≤
TV(m_x)(1 + c_1)`, `b_V(z) ≤ ρ(1 + c_1)`, `B_V ≤ 10ρ(1 + c_1)`. Executed: the
coupling built as an exact `36 × 36` table on the `201` declared instances,
both marginals exact and all entries nonnegative (B2); `E d_H ≥ TV(m_x) +
TV(m_y)` (B3) and `E d_H ≤ TV(m_x)(1 + c_1)` (B4) on every instance.

## Theorem M — the block scan contracts the total disagreement iff `B_V < 2` (finite windows)

**Statement.** Let `Λ ⊂ Z^3` be a finite window with exterior records and
`n = |Λ|`. The random block scan picks `a ∈ Λ` uniformly and resamples
`(V + a) ∩ Λ` from its conditional law given the rest (the single site `a` when
`a + e ∉ Λ`). Couple two copies with the same exterior by a Hamming-optimal
coupling at each step (a minimizer exists by compactness). Then, with
`u_x = P(η_x ≠ η'_x)` and `U = Σ_x u_x`,
`E[U'] ≤ U − (1/n) Σ_x κ_x u_x + (1/n) Σ_z β_z u_z`,
where `κ_x` is the number of updates covering `x` and `β_z` the sum over the
updates in which `z` is a boundary slot of their `W_1` sensitivities to `z`.
For sites `x` with `x ± e ∈ Λ`, `κ_x = 2`; for sites `z` whose neighbors and
their `e`-translates lie in `Λ`, `β_z = B_V` (the ten translates of `V`
adjacent to `z`, by translation covariance). On such an interior the
coefficient of `u_z` is `1 − (2 − B_V)/n`: the scan contracts the interior
total disagreement exactly when `B_V < 2`.

*Proof.* Condition on the current pair and the chosen `a`. The sites outside
the update keep their disagreement; for the update `W = (V + a) ∩ Λ`, the
Hamming-optimal coupling gives `E[Σ_{x ∈ W} 1[η_x ≠ η'_x] | current] =
W_1(μ_W^{η}, μ_W^{η'})`, where `η, η'` are the current configurations outside
`W`; `W_1` is a metric on laws (the minimum over couplings of a metric cost is
a metric), so the triangle inequality along the single-slot changes of the
boundary gives `W_1 ≤ Σ_{z ∈ ∂W} b_W(z) 1[η_z ≠ η'_z]`, with `b_W(z) = b_V(z −
a)` for a full block and the one-site sensitivity for a single-site update.
Averaging over `a` uniformly and over the current pair, and collecting the
coefficient of each `u_z`, gives the displayed inequality. The interior counts
follow by translation covariance of the rule: the translates of `V` adjacent
to `z` are the ten `V + a` with `z ∈ ∂(V + a)`, and their sensitivities to `z`
are the ten `b_V(z')`, `z' ∈ ∂V`. ∎

**What Theorem M does not give.** The one-site corollary of block 03 needed a
per-site decay (the matrix `D_Λ` and the walk-count bound). The block scan
bounds the sum over the block, not each site, so the passage to `Z^3` needs a
block-level version of that decay; it is not proved here, and this note claims
nothing on `Z^3` from Theorem M. The silence of Theorem N does not depend on
it: at the silent triples the interior coefficient `1 − (2 − B_V)/n` is at
least `1` for every coupling.

## The sensitivities, exactly (executed)

| triple | `c_1` | `ρ` | `ρ/c_1` | `ρ'` | `B_V` lower `10(ρ + ρ')` | `B_V` upper `10ρ(1 + c_1)` |
|---|---|---|---|---|---|---|
| `(3, 1, 2)` | `270/989` | `2168397/7948400` | `0.9992` | `1350/26077` | `3.2457…` | `3.4728…` |
| `(5, 2, 4)` | `8650000/40615109` | `271059507090000/1298168979740633` | `0.9804` | `1915425000/55627392667` | `2.4323…` | `2.5327…` |
| `(7, 3, 5)` | `6391462/29948925` | `239957740750/1121635870169` | `1.0024` | `856455908/27833079009` | `2.4470…` | `2.5959…` |
| `(2, 1, 2)` | `2/13` | `67715/446034` | `0.9868` | — | — | `1.7517…` |
| `(3, 2, 2)` | `2079/15566` | `1471549788/11145302999` | `0.9885` | — | — | `1.4966…` |
| `(5, 4, 4)` | `4000000/61385721` | `81847628000000/1305850357630907` | `0.9618` | — | — | `0.6676…` |

The maximizing instances (lexicographically first over multisets, the `∂y`
multiset, the other four `∂x` values and the pair, under `--exact`): at
`(3, 1, 2)` the `∂y` slots `(+x, +x, +x, +y, +y)`, the `∂x` slots `(+x, +x, +x,
−y)`, the pair `+x ↔ −x`; at `(5, 2, 4)` and `(5, 4, 4)` all ten slots `+x` with
the pair `+x ↔ −x`. Why averaging over the partner barely helps: the
`x`-marginal is the one-site conditional with the `y`-slot's factor `φ(s_x,
η_y)` replaced by the effective factor `h(s_x) = Σ_{s_y} φ(s_x, s_y) w_y(s_y)`,
and at the maximizing `∂y` shells `h` is as steep across the menu as a single
`φ` factor; at `(7, 3, 5)` and at strong couplings on the lines it is steeper
(`ρ > c_1`, C3, D2).

**The lines (D1, D2).** On the scan `t = 21/20, …, 39/20` along `(t, 1, 1)`,
`6c_1` and `5ρ(1 + c_1)` both cross `1` in `(8/5, 33/20)`, and `ρ/c_1 > 1`
from `t = 39/20`; along `(t, t, 1)` both cross in `(29/20, 3/2)` and `ρ/c_1 >
1` from `t = 3/2`. The sequential number is below `6c_1` on the region side of
the crossing (`0.9366` against `0.9828` at `t = 8/5`) and above it beyond
(`1.6123` against `1.5343` at `t = 39/20`): the pair block gains a little near
the threshold and loses at strong couplings. No threshold of the two-site
number is isolated here, and no uniqueness statement is attached to it.

## No-Go Discipline Gate

The negative-shaped sentence of this note is "the two-site block criterion is
silent at the three silent triples for every coupling" — an exact finite
statement about one block and one criterion, proved by Theorem N. It is a
route closure at the scope of the two-site block, so the gate is answered.

### N1 — Routes toward the silent triples (each with its obligation)

| route | what it would attempt | its terminal obligation | marker |
|---|---|---|---|
| 1 the two-site block (this note) | `B_V < 2` | exact `ρ, ρ'`; the `W_1` lower bound | executed: `B_V ≥ 2.43` at every silent triple; closed for every coupling |
| 2 larger blocks (a planar `k × k` window) | per-site boundary influence below one, volume beating surface | exact block sensitivities for `6^{|∂V|}` boundary shells — not exactly computable beyond a plaquette at this menu; and the block-level decay of Theorem M's open implication | not attempted; obligation named |
| 3 a transfer-matrix route on slabs | a spectral gap uniform in the slab width | uniformity in the width | not attempted |
| 4 a convergent expansion around the constant rule | convergence at `(3,1,2)` etc. | a convergent polymer bound at couplings far from constant | not attempted |
| 5 the other side: an ordering argument | more than one static law at strong coupling | a contour (Peierls-type) bound at the given weights | not attempted; named because silence of every criterion is consistent with it |

The routes differ in primary object, mechanism and terminal obligation; route
1 fails by an exact obstruction independent of any proof of the criterion.

### N2 — Wall-independence audit

Walls: `W_two` (`B_V < 2`), `W_one` (`6c_1 < 1`), `W_pos` (positivity),
`W_var` (not all equal), `W_menu` (the finite menu). `W_two` and `W_one` are
independent as conditions (the sequential number is below `6c_1` near the
threshold and above it far from it; D1, D2); `W_pos`, `W_var`, `W_menu` enter
as in block 03. No wall collapses into another.

### N3 — Hidden-wall scan

Scanned for "we assume", "by construction", "as is standard", "the framework
provides", "naturally", "obviously", "canonical", "registered", "background",
"bridge context". Hits: "registered" only in N6. Every step of Theorems N, O
and M is written; the open implication of M is named as open, not assumed.

### N4 — Per-citation table

| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 03's note (proposed, unaudited): `c_1`, the region, the silent triples, Step 0 (the maximal coupling) | uniqueness where `6c_1 < 1`; silence elsewhere | the silent triples as the target; `c_1` recomputed | yes (parent; cited) |
| blocks 01–02 through block 03: Theorem A on the pair window | the block law's full conditionals and uniqueness | the block law as one object | yes (cited) |
| the classical block condition and the Hamming coupling distance | uniqueness under a block condition | re-proved at scope (M on finite windows); the `Z^3` step not re-proved and not claimed | yes (re-proved where used; nothing imported) |

### N5 — Resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "the two-site block criterion is silent at the three silent triples for every coupling" | executed: every boundary instance for `ρ`, `ρ'`; the factorization on every instance at `(3,1,2)` | executed: `x`- and `y`-marginal sensitivities separately; the coupling's `x` and `y` disagreements | executed: the sequential coupling built explicitly on `201` instances | executed: the pair block with its ten slots; the bounds at six triples; two line scans | not claimed: the block contraction's `Z^3` implication is not proved; the silence is a finite exact statement |

The runner prints matching `per_element:` … `lattice_wide:` lines.

### N6 — Partial-closure paths and primitive scan

The registered approved primitives in `docs/audit/data/axiom_premise_nodes.json`
(`scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`) supply no block sensitivity and are not walls here.
Reframing paths: routes 2–5 of N1; `docs/repo/DEFERRED_DECISIONS.md` entry 1
is not touched. No new axiom is said to be required.

### N7 — Steelman

Hostile reviewer: "The Hamming coupling distance is the wrong metric for a
block criterion; with a weighted or non-Hamming cost, or with the marginal
sensitivities alone, the block sum at `(5, 2, 4)` might fall below two." Reply
at scope: any coupling of the two block laws disagrees at `x` with probability
at least `TV(m_x)` (Theorem N), so any criterion of the form "the sum over
boundary slots of a per-slot coupling cost, counted per site, is below the block
size" inherits the lower bound `10(ρ + ρ')/2 = 1.22, 1.22, 1.62 > 1`
per site at the silent triples; a criterion using marginal sensitivities alone
with a different normalization is a different theorem, whose proof is not
available here — named as route 2's obligation. Conceded: nothing here says the
silent triples are not unique.

### N8 — Cross-cycle echo

| similar prior wall | retired? | mechanism | applies here? |
|---|---|---|---|
| block 03: "the one-site criterion is silent at `(3,1,2)`, `(5,2,4)`" | no (this note closes the first sharper route) | the two-site block | yes — the same silence, now for the pair block and every coupling |
| the `WILSON_STAGGERED_*` contraction controls (2026-07-12): silent outside a wedge on another carrier | no (unaudited) | none | a different carrier |

**Gate result:** PASS for the scope sentence; the route closure is exact and
finite; nothing is claimed at the silent triples in either direction.

## Falsifiers

The theorems fail if any of these finite statements fails: a boundary
instance at `(3, 1, 2)` where `TV(μ_V) ≠ TV(m_x)` under a change at an `x`-slot;
a sequential coupling with a wrong marginal or a negative entry; an instance
with `E d_H < TV(m_x) + TV(m_y)` or `E d_H > TV(m_x)(1 + c_1)`; a `c_1`, `ρ` or
`ρ'` literal differing from the recomputation; a ratio `ρ/c_1` at `(7, 3, 5)`
at most `1` or a ratio above `1` at the other five triples; `10(ρ + ρ') ≤ 2` at
a silent triple; `10ρ(1 + c_1) ≥ 2` at a region triple; a crossing of `5ρ(1 +
c_1)` or `6c_1` outside the declared scan cells; `ρ/c_1 ≤ 1` at or beyond the
declared points on the scans.

## Boundaries and non-claims

This note states that the two-site block criterion is silent at the three silent triples for every coupling of the block laws; it states nothing about one law or several there, and nothing about uniqueness on the cubic lattice from the block contraction, whose infinite-lattice implication is not proved here.

No formation order, formation law, plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The block criterion and the Hamming coupling distance are classical references re-proved here at the scope used; no value, constant or theorem is imported as authority.

Further: `W_1` is bounded, not computed; the sequential coupling is one
coupling, not the optimal one; Theorem M holds on the interior of a finite
window and its boundary terms are not analyzed; the scans on the lines are at
the declared rational points only and no threshold of the two-site number is
isolated; the maximizing instances are lexicographically first among ties; the
parent is proposed and unaudited; no axiom or primitive is changed.

## Imports

References, re-proved at scope, never authority, no values imported: the
constructive block condition of Dobrushin and Shlosman (1985) — its
finite-window contraction re-proved as Theorem M, its infinite-lattice step
neither re-proved nor used; the Hamming (Vaserstein) coupling distance —
defined and bounded above and below where used. Declared mathematical
scaffolding: exact rational arithmetic; the linear congruential generator and
its seed; the scan rationals `k/20`. No observation, fitted value or literature
constant enters.

## Review record

Supervisor-authored (Fable) from the supervisor's controls
`specs/supervisor_control_block04_two_site.py` and
`specs/supervisor_control_block04_lines.py`, which computed every number here
before the contract `GOAL_block04.md` was written; refuting checker: pending;
independence class: to be filled after the checker. Settled while executing:
the block is small because the controls showed `ρ/c_1 ≈ 1` at every silent
triple, so the contract was written for the obstruction, not for a decision.

## Verification

```bash
python3 scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py
python3 scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py --list-mutations
python3 scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py --mutation lower_bound_lemma_forged
```

Families: A authority and inputs; B the factorization, the sequential coupling
and the two bounds (O, N); C the sensitivities, ratios and block-sum bounds; D
the line scans; E fences, the author-name section rule and the floating-point
self-scan; F the resolution certificate. Each of the 16 declared mutations
perturbs one object at construction time and fails in exactly one family;
`--exact` prints the maximizing instances and the scans. Expected final line:
`TOTAL: PASS=21 FAIL=0`.
