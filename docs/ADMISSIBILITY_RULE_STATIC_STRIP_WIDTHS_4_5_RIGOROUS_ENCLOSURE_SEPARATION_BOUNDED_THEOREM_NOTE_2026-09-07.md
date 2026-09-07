---
claim_id: admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule at the declared exact weight triples (3, 1, 2) and (5, 2, 4): the open-boundary static strips of widths 4 and 5 (1296 and 7776 row states; 38 and 178 orbits under the row symmetry group of order 48). The orbit sector carries the center-row law and the pair statistics (S1, executed against the full state at widths 4 and 5). The orbit quotient Q is self-adjoint for the weights |O| A_O, so its spectrum is real and the sum of its squared eigenvalues is tr(Q^2) (S2, proved; executed on every orbit pair). The deep-row pair-parallel statistics of the edge pair and of the innermost pair are enclosed in exact rational intervals of width below 10^-50 by the two-sided ratio bounds, the trace bound, the residual-gap bound and a Cauchy-Schwarz step (S3, proved and executed); every enclosure excludes the formation value p/(p+q+4r). The Krylov dimension of Q on the all-ones vector is 8, 30, 16, 111 with the integer dependency verified exactly on every orbit; the relative minimal polynomial is irreducible at degrees 8, 30, 16 (executed) and nothing is claimed at degree 111; where the degree is at most 16 the statistics are identified as algebraic numbers by their minimal polynomials (S4). The separation s - f > 10^-3 is executed at widths 2, 3, 4, 5 and s_inner > s_edge at widths 4, 5 (S5). Nothing about wider strips, the plane, monotonicity in the width, or a physical order; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py
---

# The static strip at widths four and five, rigorously enclosed: the separation from the formation law at every executed width

**Date:** 2026-09-07 **Type:** bounded_theorem **Status:** proposed_retained **Audit:** unset; the
independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py`](../scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.txt`](../logs/runner-cache/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.txt)

## Result up front

On strips four and five sites wide, the single static pattern law gives neighbouring pairs odds of
matching that sit a step away from the odds the order-built law gives them, a step of about the same
size at every width, both at the edge
of the strip and one step in. We pinned those odds down with rigorous bounds far tighter than the
question needs, and where the algebra is small enough we identified them as exact algebraic numbers.
The step is present, and of about the same size, at every width we computed: two, three, four and five.
Nothing is said here about wider strips or about the infinite plane.

Exactly: on the open-boundary strip `S_{W,n}` of width `W = 4` or `5`, the static law's center-row
law as `n` grows is `w ∝ A ρ_1^2` (block 02, F3), and its pair-parallel probability on the edge pair
`(0, 1)` and on the innermost pair `(⌊W/2⌋−1, ⌊W/2⌋)` lies in an exact rational interval of width
below `10^{-50}`:

| `W` | triple | `s_edge ∈` | `s_inner ∈` | `f` |
|---|---|---|---|---|
| 4 | (3,1,2) | `[0.2561162479042062541091, 0.2561162479042062541092]` | `[0.2562841851395883553318, 0.2562841851395883553319]` | `1/4` |
| 4 | (5,2,4) | `[0.2199158620242067557423, 0.2199158620242067557424]` | `[0.2199567765176185248607, 0.2199567765176185248608]` | `5/23` |
| 5 | (3,1,2) | `[0.2561164296010283514028, 0.2561164296010283514029]` | `[0.2562896288160817584176, 0.2562896288160817584177]` | `1/4` |
| 5 | (5,2,4) | `[0.2199158748550207694373, 0.2199158748550207694374]` | `[0.2199574883712355711334, 0.2199574883712355711335]` | `5/23` |

(decimals are exact integer-arithmetic expansions of the rational endpoints,
rounded outward; the endpoints are printed by the runner under `--exact`). Every interval excludes
the formation value `f = p/(p + q + 4r)` of the row-sweep formation law (block 02, E4, the same on
every pair of every width), by more than `10^{-3}`: `s_edge − f = 0.00611624…`, `s_inner − f =
0.00628418…` at `W = 4` and `0.00611642…`, `0.00628962…` at `W = 5` for `(3,1,2)`; `0.00252455…`,
`0.00256547…` and `0.00252457…`, `0.00256618…` for `(5,2,4)`. The innermost pair is strictly more
often parallel than the edge pair at both widths and both triples. The route is elementary and needs
no algebraic field: the orbit quotient `Q` is self-adjoint for the weights `w_O = |O| A_O`, so the
two-sided ratio bounds enclose the Perron root, the trace bound `λ_2^2 ≤ tr(Q^2) − lo^2` controls
every other eigenvalue, the residual–gap bound controls the angle between the power vector `Q^{40}
1` and the Perron vector, and one Cauchy–Schwarz step turns that angle into the enclosure of the
statistic. The Krylov dimension of `Q` on the all-ones vector is `8, 30, 16, 111` in the order of
the table (the integer dependency verified exactly on every orbit at all four cases); the relative
minimal polynomial is irreducible at degrees `8, 30, 16`, so the Perron root has those degrees over
`Q` there, and at degrees `8` and `16` the statistics are identified by their minimal polynomials
(degree `8` and `16`). At degree `111` the polynomial is verified and nothing else is claimed.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 02's refresh item 3: the width-W enclosures for W = 4, 5, the static pair statistic versus the width-independent formation value; the owner's sequencing gate (2026-08-26): what the Admissibility rule induces on the infinite lattice is unidentified; the parked statistical-bridge decision wakes on 'the committed-action identification lands', which this note does not fire"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the static law of wider strips by the same self-adjoint route (the orbit count is the only cost), and the plane's static law by a route not yet chosen; consumers: the parked statistical-bridge decision material (docs/repo/DEFERRED_DECISIONS.md entry 1, read-only), the record-matter lane's formation-order supply"
conditional_surface_status: "exact on the declared strips of widths 2 to 5, the menu and the two triples; S2 and S3 are proved for every width; S4's identification is executed where the Krylov degree is at most 16; conditional on the records-only reading where the formation value enters; no wider strip, no plane, no monotonicity in the width"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "S1 and S2 are proved from block 02's F1 and the product rule's symmetry and executed exhaustively on the orbit sector; S3 is a proved chain of four elementary inequalities executed with exact rational arithmetic to enclosures below 10^-50; S4 is a proved Krylov lemma with the degrees executed by modular ranks and an exact integer dependency; S5 is executed at four widths; nothing about wider strips, the plane, a physical order, the Born form or the bridge is claimed."
```

## Premises and declared objects

The only scientific dependencies are the four axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and block 02's
note
[`ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md)
(proposed, unaudited), whose definitions are restated here where used; blocks
03 to 05 are not inputs. The axiom sentences used, verbatim (runner A2):

- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and "For
  each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form." — "records are permanent" — "Only records are
  readable." — "A site with no record cannot be read."

**Menu, rule, strips (block 02, restated).** `M` = the six projectors `P(±e_a)`, indexed `P(+e_x),
P(−e_x), P(+e_y), P(−e_y), P(+e_z), P(−e_z)`; the 24 proper cubic rotations act on `M` as signed
axis permutations of determinant `+1`, transitively; the product rule has the symmetric isotropic
pair weight `φ` with orbit values `(p, q, r)` on the parallel, antiparallel and orthogonal pairs, at
the declared triples `(3, 1, 2)` and `(5, 2, 4)`. The strip `S_{W,n}` is the `W × n` grid with
nearest-neighbor edges and open boundary; its static law is `μ(v) ∝ Π_{xy∈E} φ(v_x, v_y)`. Row
states `ρ ∈ M^W`; `A(ρ) = Π_{j<W−1} φ(ρ_j, ρ_{j+1})` (row-internal edges), `V(ρ, ρ') = Π_j φ(ρ_j,
ρ'_j)` (vertical edges), the row transfer `T(ρ, ρ') = V(ρ, ρ') A(ρ')`, so the `n`-row static weight
is `A(ρ^0) Π_{i≥1} T(ρ^{i−1}, ρ^i)`. The row symmetry group `G` (order 48) is the 24 rotations
acting entrywise times the row reversal.

**Readings carried from blocks 01–02, named, nothing new adopted.** The records-only reading (an
unrecorded neighbor contributes no factor) and the declared row sweep enter only through the
formation value `f` of E4; the positivity of the rule; the variation clause restricted to the menu
(`(p, q, r)` not all equal); no order is selected as physical.

**Named results of block 02 used.** F1: `A(gρ) = A(ρ)`, `V(gρ, gρ') = V(ρ, ρ')`, hence `T(gρ, gρ') =
T(ρ, ρ')`; the Perron vector `ρ_1` of `T` is constant on `G`-orbits and `T` acts on orbit-constant
vectors as the quotient `Q_{OO'} = Σ_{ρ'∈O'} T(ρ_O, ρ')`. F2: the positive-matrix spectral theorem,
re-proved there (the Perron root `λ_1 > 0` is simple, its eigenvector is positive, every other
eigenvalue has modulus below `λ_1`, and `r(v) = min_i (Tv)_i/v_i ≤ λ_1` for `v ≥ 0`, `v ≠ 0`). F3:
the center-row law of the `n`-row strip, as `n` grows, is `w(ρ) ∝ A(ρ) ρ_1(ρ)^2`, independent of the
records on the two end rows. E4: the row-sweep formation law gives every nearest-neighbor pair of
every width the pair-parallel probability `f = p/(p + q + 4r)`: `1/4` at `(3, 1, 2)`, `5/23` at `(5,
2, 4)`.

**Declared objects of this note.** Widths `W = 4` (1296 row states, 38 orbits) and `W = 5` (7776 row
states, 178 orbits); widths `2, 3` (3 and 8 orbits) as controls on the method. Orbit sizes `|O|`;
`A_O` (orbit-constant by F1); the quotient `Q` and the row-vector quotient `R` with `R_{OO'} |O'| =
|O| Q_{OO'}`; the weights `w_O = |O| A_O > 0` and the inner product `⟨u, v⟩_w = Σ_O w_O u_O v_O`
with norm `‖·‖_w`. The pair statistics: `s_edge` for the pair `(0, 1)` and `s_inner` for the
innermost pair `(⌊W/2⌋−1, ⌊W/2⌋)` — `(1, 2)` at both widths `4` and `5` (at `W = 5` one step from
the boundary); at `W = 2, 3` the formula returns the edge pair, so `s_inner` is a distinct statistic
only at `W = 4, 5`, two data points. With `n_O` the number of the orbit's states whose pair is
parallel and `c_O = n_O/|O| ∈ [0, 1]`, the statistic of a `w`-unit sector vector `v` is `s(v) = Σ_O
w_O v_O^2 c_O`. The exact power vector `y = Q^{40} 1 > 0`, its `w`-normalization `ŷ`, the Rayleigh
quotient `μ = ⟨y, Qy⟩_w/⟨y, y⟩_w`, the residual `r = ‖Qy − μy‖_w/‖y‖_w`, the two-sided ratio bounds
`lo = min_O (Qy)_O/y_O` and `hi = max_O (Qy)_O/y_O`. The Krylov sequence `1, Q1, Q^2 1, …` and the
relative minimal polynomial `m_1` of `Q` on `1`
(monic, of least degree `d`, `m_1(Q) 1 = 0`).

## Prior art and what is new

Block 02 (Theorem F) enclosed the same statistic at widths 2 and 3 by the algebraic route: the
characteristic polynomial of the quotient, Sturm isolation of the Perron root, the Perron vector by
elimination in the number field, and the minimal polynomial of the statistic by a resultant. At
widths 4 and 5 the characteristic polynomial has degree 38 and 178 and the Perron root has degree 30
and 111 over `Q` at `(5, 2, 4)`, where the field route does not fit a runner budget. What is new
here is the elementary route that needs no field: the observation that the quotient is self-adjoint
for the orbit weights (S2), which makes every eigenvalue real and gives the trace identity `Σ λ_i^2
= tr(Q^2)`; on that footing three classical inequalities, each re-proved at scope in S3, enclose the
statistic rigorously from a single exact power vector. Their classical names, given once here and in
Imports and not used in the theorem statements: the two-sided ratio bounds on the Perron root are
the Collatz–Wielandt bounds; the residual–gap bound on the angle between a trial vector and an
eigenvector is the Davis–Kahan sin-θ theorem in its one-dimensional self-adjoint form; the
positive-matrix spectral theorem is Perron–Frobenius, re-proved in block 02 (F2) and cited from
there. The Krylov route to the degree of the Perron root over `Q` (S4) is the standard relative
minimal polynomial of a matrix on a vector; the modular-rank step that makes it cheap is elementary
linear algebra over finite fields. Also new is the innermost-pair statistic, which at widths 2 and 3
coincides with the edge statistic and is a distinct object only from width 4.

## Exact target and obligation graph

**Target claim.** On the open-boundary static strips of widths 4 and 5 at the declared triples, the
deep-row pair-parallel probabilities of the edge pair and of the innermost pair lie in the exact
rational intervals of the table, each of width below `10^{-50}` and each excluding the formation
value `f = p/(p + q + 4r)`; and where the Krylov degree of the quotient on the all-ones vector is at
most 16 the two probabilities are the algebraic numbers whose minimal polynomials the runner prints.

| lemma | status |
|---|---|
| F1 (symmetry reduction), F2 (positive-matrix spectral theorem), F3 (the deep-row law `w ∝ A ρ_1^2`, end-record independence), E4 (the formation value) | cited from block 02 (proposed, unaudited); the parts used are restated in Premises; F1 is re-executed here (B2) |
| S1: the sector carries the center-row law and the statistics | proved here from F1/F3; executed against the full state (B5) |
| S2: `w_O Q_{OO'} = w_{O'} Q_{O'O}`; real spectrum; `w`-orthonormal eigenbasis; `Σ λ_i^2 = tr(Q^2)` | proved here; the spectral theorem for self-adjoint operators on a finite-dimensional inner-product space is cited scaffolding; executed on every orbit pair (C1, C2) |
| S3(a) the two-sided ratio bounds | proved here from F2 and the positive left Perron vector; executed (C3) |
| S3(b) the trace bound | proved here from S2; executed (D1) |
| S3(c) the residual–gap bound | proved here in the eigenbasis; executed (D1) |
| S3(d) the `2ε` bound on the statistic | proved here from F3 and Cauchy–Schwarz; executed (D2, D3) |
| S4(i)–(iii) the Krylov lemma | proved here; (iv) the degrees executed (C4–C7); (v) the identification executed where `d ≤ 16` (D7) |
| S5 the separation at widths 2 to 5 | executed (E1–E4); widths 2, 3 recomputed by the S3 route and matched to F4 (D6) |
| the finite-`n` sequences and the boundary check | executed facts (D4, D5), not theorems |

No hypothesis is dropped between the lemmas and the target: S2 uses the `G`-invariance of `V` and of
`A` and the symmetry of `V`, all three supplied by F1 and the product rule and each necessary (block
02's `W = 2` quotient loses self-adjointness when any one is removed, as the contract lens showed by
counterexample); S3(b) uses `λ_1 ≥ lo > 0`; S3(c) uses `δ > 0`, which is executed, and the
positivity of `ŷ`, `x`, `w`; S3(d) uses `c_O ∈ [0, 1]`. The boundary cases: `W = 2, 3`, where the
innermost pair is the edge pair, are covered by the same code path. The strongest missing lemma is
not part of the target: any statement about widths above 5 or about the plane.

## Theorem S1 — the orbit sector

**S1.** The vectors `A` and `1` are `G`-invariant; `T` maps `G`-invariant column vectors to
`G`-invariant column vectors, acting on them as `Q`, and `G`-invariant row vectors to `G`-invariant
row vectors, acting as `R`; hence the center-row law of the `n`-row strip, `(A T^c)(ρ) (T^{n−1−c}
1)(ρ)` with `c = ⌊n/2⌋`, is `G`-invariant, equal to `left_{O(ρ)} right_{O(ρ)}` with `left = A R^c`,
`right = Q^{n−1−c} 1` in the sector, and its pair-parallel probability is `Σ_O |O| left_O right_O
c_O / Σ_O |O| left_O right_O`. The deep-row law `w ∝ A ρ_1^2` (F3) is `G`-invariant as well, and its
statistic is `s(x)` for the `w`-unit Perron vector `x` of `Q` (S3(d)).

*Proof.* `A(gρ) = A(ρ)` and `V(gρ, gρ') = V(ρ, ρ')` are F1 (isotropy of `φ`
under the rotations; the reversal reverses both rows and both products). For a `G`-invariant column
vector `v`, `(Tv)(gρ) = Σ_{ρ'} T(gρ, ρ') v(ρ') = Σ_{ρ'} T(gρ, gρ') v(gρ') = Σ_{ρ'} T(ρ, ρ') v(ρ') =
(Tv)(ρ)`, and grouping `ρ'` by orbits gives `(Tv)_O = Σ_{O'} Q_{OO'} v_{O'}` with `Q_{OO'} =
Σ_{ρ'∈O'} T(ρ_O, ρ')` independent of the representative (`O'` is `G`-stable and `T` is
`G`-invariant). For a row vector `a` the same computation gives `(aT)_{O'} = Σ_O a_O R_{OO'}` with
`R_{OO'} = A_{O'} Σ_{ρ∈O} V(ρ, ρ_{O'})`, and the transitivity of `G` on `O` and `O'` gives `Σ_{ρ∈O,
ρ'∈O'} V(ρ, ρ') = |O| Σ_{ρ'∈O'} V(ρ_O, ρ') =
|O'| Σ_{ρ∈O} V(ρ, ρ_{O'})`, i.e. `R_{OO'} |O'| = |O| Q_{OO'}`. The pair
indicator `[ρ_a = ρ_b]` is not itself `G`-invariant, but its orbit sums are: a rotation preserves
equality of entries, and the reversal maps the pair `(a, b)` to `(W−1−b, W−1−a)` — `(0, 1)` to
`(W−2, W−1)` and the innermost pair `(1, 2)` of width 5 to `(2, 3)` — whose indicator has the same
sum over every orbit because the reversal is in `G`; so `n_O = #{ρ ∈ O : ρ_a = ρ_b}` is the same for
a pair and its mirror image, and the sum over an orbit of a `G`-invariant weight times the indicator
is `|O| c_O` times the weight (the refuting checker verified that the two counts agree on every orbit at widths 4 and 5; the runner's B3 checks the pair counts against `6^{W−1}`). ∎

*Executed.* Orbit counts `3, 8, 38, 178` at widths `2, 3, 4, 5`, the same at
both triples (B1). `T(gρ, gρ') = T(ρ, ρ')` for all 48 maps, every orbit representative against all
1296 rows at width 4 and two representatives against all 7776 rows at width 5, both triples (B2).
`Q` rebuilt from a second representative of every orbit, `R_{OO'} |O'| = |O| Q_{OO'}` on every pair,
the orbit sizes summing to `6^W` and the parallel counts to `6^{W−1}`
(B3). The full-state transfer, computed through the tensor structure
`V = φ ⊗ … ⊗ φ` (`W` factors), equals the explicit `T` on three vectors
(B4), and the sector's center-row statistics equal the full-state ones at
width 4 for `n = 3, 5, 7` and at width 5 for `n = 3, 5`, both pairs, both triples: twenty exact
equalities (B5).

## Theorem S2 — self-adjointness and the real spectrum

**S2.** `w_O Q_{OO'} = w_{O'} Q_{O'O}` for all orbits `O, O'`, with `w_O = |O| A_O > 0`. Hence `Q`
is self-adjoint for `⟨·,·⟩_w`: every eigenvalue of `Q` is real, `Q` has a `w`-orthonormal eigenbasis
`v_1, …, v_N` (`N` the number of orbits), and `Σ_i λ_i^2 = tr(Q^2)`.

*Proof.* By S1's transitivity identity,
`|O| Σ_{ρ'∈O'} V(ρ_O, ρ') = |O'| Σ_{ρ∈O} V(ρ, ρ_{O'})`. The right side equals `|O'| Σ_{ρ∈O}
V(ρ_{O'}, ρ)` by the symmetry of `V` (inherited from the symmetry of `φ`). Multiplying both sides by
`A_O A_{O'}` (orbit-constant by the `G`-invariance of `A`) gives `|O| A_O · A_{O'} Σ_{ρ'∈O'} V(ρ_O,
ρ') = |O'| A_{O'} · A_O Σ_{ρ∈O} V(ρ_{O'}, ρ)`, i.e. `w_O Q_{OO'} = w_{O'} Q_{O'O}`. Three hypotheses
were used and each is needed: the `G`-invariance of `V` (for the transitivity identity), the
`G`-invariance of `A` (to pull `A_O`, `A_{O'}` through the sums) and the symmetry of `V`; all three
are supplied by F1 and the product rule. The identity says `⟨u, Qv⟩_w = Σ_{O,O'} w_O u_O Q_{OO'}
v_{O'} = Σ_{O,O'} w_{O'} Q_{O'O} u_O v_{O'} = ⟨Qu, v⟩_w`. The spectral theorem for a self-adjoint
operator on a finite-dimensional real inner-product space (cited scaffolding) gives the real
spectrum and the `w`-orthonormal eigenbasis; in that basis `Q` is diagonal, and the trace of `Q^2` —
a similarity invariant — is `Σ_i λ_i^2`. ∎

*Executed.* The identity on all `38^2` and `178^2` orbit pairs at both
triples (C1); `tr(Q^2) = 28006524928, 250087391159985, 16238809878528, 1948759036672266913` at `(4;
3,1,2)`, `(4; 5,2,4)`, `(5; 3,1,2)`, `(5; 5,2,4)`
(C2). `Σ_i λ_i^2 = tr(Q^2)` is a theorem here, not an executed identity.

## Theorem S3 — rigorous enclosures without a field

Throughout, `x` is the `w`-unit Perron vector of `Q` (positive, F2), `y = Q^{40} 1`, `ŷ = y/‖y‖_w`,
`μ`, `r`, `lo`, `hi` as declared.

**S3(a) (the two-sided ratio bounds).** For every `y > 0`, `0 < lo ≤ λ_1 ≤ hi`.

*Proof.* `lo = r(y) ≤ λ_1` is F2's inequality for the positive matrix `Q`
(`Qy ≥ lo · y` entrywise, so the maximum of `r` over nonnegative nonzero
vectors, which F2 shows to be `λ_1`, is at least `lo`); `lo > 0` because `Qy > 0`. For the upper
bound let `u > 0` be the left Perron vector, `u^T Q = λ_1 u^T`; by S2 one may take `u_O = w_O x_O`,
positive since `w > 0` and `x > 0` (indeed `(u^T Q)_{O'} = Σ_O w_O x_O Q_{OO'} = Σ_O w_{O'} Q_{O'O}
x_O = w_{O'} λ_1 x_{O'}`). Then `λ_1 u^T y = u^T Q y ≤ hi · u^T y` since `(Qy)_O ≤ hi · y_O`
entrywise and `u > 0`; dividing by `u^T y > 0` gives `λ_1 ≤ hi`. ∎

**S3(b) (the trace bound).** Let `λ_2` be the largest modulus among the non-Perron eigenvalues. Then
`λ_2^2 ≤ tr(Q^2) − lo^2 ≤ λ_2bound^2`, where `λ_2bound` is the rational upper bound of `sqrt(tr(Q^2)
− lo^2)` computed by an integer square root at scale `10^{80}`, rounded up.

*Proof.* All eigenvalues are real (S2), so `λ_2^2 ≤ Σ_{i≥2} λ_i^2 = tr(Q^2) − λ_1^2`
by the trace identity of S2, and `λ_1^2 ≥ lo^2` because `λ_1 ≥ lo > 0`
(S3(a)); the square-root step is `sqrt(t) ≤ (⌊sqrt(⌊t·10^{160}⌋ + 1)⌋ + 1)/10^{80}`,
an inequality between integers, executed. ∎

**S3(c) (the residual–gap bound).** Put `δ = μ − λ_2bound`. If `δ > 0`
(executed at every case), then with `θ` the `w`-angle between `ŷ` and `x`,
`sin θ ≤ r/δ` and `‖ŷ − x‖_w ≤ √2 · r/δ =: ε`.

*Proof.* Expand `ŷ = Σ_i a_i v_i` in the `w`-orthonormal eigenbasis with
`v_1 = x` (S2); then `Qŷ − μŷ = Σ_i a_i (λ_i − μ) v_i` and `r^2 = ‖Qŷ − μŷ‖_w^2 = Σ_i a_i^2 (λ_i −
μ)^2`. Every non-Perron eigenvalue lies in `[−λ_2bound, λ_2bound]` (S3(b)), so `μ − λ_i ≥ μ −
λ_2bound = δ > 0` for `i ≥ 2` — a negative `λ_i` only widens the gap — and `(λ_i − μ)^2 ≥ δ^2`.
Dropping the `i = 1` term, `r^2 ≥ δ^2 Σ_{i≥2} a_i^2 = δ^2 sin^2 θ`, since `Σ_i a_i^2 = 1` and `a_1 =
cos θ`. The inequality `μ ≤ λ_1` is not used. Next, `‖ŷ − x‖_w^2 = 2 − 2 cos θ`, and `cos θ = ⟨ŷ,
x⟩_w > 0` because `ŷ`, `x` and `w` are all positive, so `2 − 2 cos θ ≤ 2(1 − cos^2 θ) = 2 sin^2 θ`
(for `0 < cos θ ≤ 1`, `1 − cos θ ≤ 1 − cos^2 θ`). Hence `‖ŷ − x‖_w ≤ √2 sin θ ≤ √2 · r/δ`. ∎

**S3(d) (the statistic).** The deep-row pair-parallel probability of a pair whose orbit fractions
are `c_O` equals `s(x) = Σ_O w_O x_O^2 c_O`, and `|s(x) − s(ŷ)| ≤ 2ε`. Hence `s(x) ∈ [s(ŷ) − 2ε,
s(ŷ) + 2ε]`, an interval with exact rational endpoints.

*Proof.* By F3 the deep-row law is `w(ρ) ∝ A(ρ) ρ_1(ρ)^2` with
`ρ_1(ρ) = x_{O(ρ)}` and `A(ρ) = A_{O(ρ)}` (S1), so the pair-parallel probability is `Σ_O A_O x_O^2
n_O / Σ_O A_O x_O^2 |O| = Σ_O w_O x_O^2 c_O / Σ_O w_O x_O^2 = s(x)`, the denominator being `‖x‖_w^2
= 1`. For the bound, `s(x) − s(ŷ) = Σ_O w_O (x_O − ŷ_O)(x_O + ŷ_O) c_O`, and with `0 ≤ c_O ≤ 1` and
`w_O > 0`, `|s(x) − s(ŷ)| ≤ Σ_O w_O |x_O − ŷ_O| |x_O + ŷ_O| ≤ ‖x − ŷ‖_w ‖x + ŷ‖_w` by Cauchy–Schwarz
in `⟨·,·⟩_w`; finally `‖x + ŷ‖_w ≤ ‖x‖_w + ‖ŷ‖_w = 2` and `‖x − ŷ‖_w ≤ ε` (S3(c)). ∎

*Executed (`k = 40`; every decimal an exact outward-rounded expansion).*

| `W` | triple | `λ_1 ∈` | `λ_2bound/lo ≤` | `sin θ ≤` |
|---|---|---|---|---|
| 4 | (3,1,2) | `[167095.549094439124072551, 167095.549094439124072552]` | `0.05538` | `9.82 × 10^{-60}` |
| 4 | (5,2,4) | `[15805546.058271708040967862, 15805546.058271708040967863]` | `0.03301` | `6.08 × 10^{-70}` |
| 5 | (3,1,2) | `[4020095.963367139908549070, 4020095.963367139908549071]` | `0.06932` | `4.02 × 10^{-58}` |
| 5 | (5,2,4) | `[1394779038.040295659739675096, 1394779038.040295659739675097]` | `0.04150` | `1.32 × 10^{-68}` |

The enclosures of `s_edge` and `s_inner` are the table in Result up front; each has width below
`10^{-50}` and excludes `f` (D2, D3). At every case `y > 0`, `lo ≤ μ ≤ hi`, `δ > 0`, `lo >
λ_2bound`, and the square-root bounds are verified as upper bounds by squaring (D1). The ratio
column bounds the executed `λ_2bound/lo`, not the true `λ_2/λ_1`, which is smaller. The sector's
finite-`n` center-row statistics at `n = 3, 5, 9, 17, 33, 65` have strictly decreasing distances to
the enclosures for both pairs at all four cases (an executed fact for these `n`, D4); at `W = 5`,
`(3,1,2)`, the innermost value at `n = 33` is `0.2562896288160817584176711…`, within `1.5 ×
10^{-25}` of the enclosure, and at `n = 65` within `1.1 × 10^{-47}`. End-record independence (F3)
executed at `n = 33`: with `P(e_y)` recorded on every site of both end rows, computed on the full
state through the tensor structure of `V` (no sector), and with the orbit-averaged end record in the
sector, all four cases and both pairs lie within `10^{-6}` of the enclosures
(D5). Widths 2 and 3, recomputed by this route, carry block 02's F4 digits
(`0.255943088901618766…`, `0.219874176124090031…`, `0.2561109872857786908612…`,
`0.2199151616870197815075…`) and exclude `f` (D6): the two routes agree.

## Theorem S4 — the Krylov degrees and the identification where the degree allows

**S4.** Let `m_1` be the relative minimal polynomial of `Q` on `1` (monic, of least degree `d`,
`m_1(Q) 1 = 0`). (i) `λ_1` is the largest root of `m_1`.
(ii) `m_1` has `d` distinct real roots. (iii) Exactly one root of `m_1` lies
in `[lo, hi]`, namely `λ_1`. (iv) Executed: `d = 8, 30, 16, 111` at the four cases; `m_1` is
irreducible at `d = 8, 30, 16`, so the degree of `λ_1` over `Q` is `8, 30, 16` there; at `d = 111`
factorization is not attempted and nothing about irreducibility is claimed. (v) Where `d ≤ 16`: the
Perron vector is `x = p(Q) 1` with `p = m_1/(λ − λ_1)`, and each statistic is the algebraic number
`s = N(λ_1)/D(λ_1)` whose minimal polynomial is the irreducible factor of `Res_λ(m_1, y D − N)` with
exactly one root in the S3 enclosure.

*Proof.* (i) Write `1 = Σ_i a_i v_i` in the eigenbasis of S2. Then
`m_1(Q) 1 = Σ_i a_i m_1(λ_i) v_i = 0` forces `m_1(λ_i) = 0` whenever `a_i ≠ 0`; so every root of
`m_1` is an eigenvalue (`m_1` being the least such polynomial, its roots are exactly the eigenvalues
with `a_i ≠ 0`, each once). The Perron coefficient is `a_1 = ⟨1, x⟩_w = Σ_O w_O x_O > 0`
(`w > 0`, `x > 0`), so `λ_1` is a root; and `λ_1 = max spec(Q)` (F2, and all
eigenvalues are real), so it is the largest. (ii) `m_1` divides the minimal polynomial of `Q`, which
is squarefree with real roots because `Q` is diagonalizable with real spectrum (S2); so `m_1` is
squarefree with `d` distinct real roots, at every `d` including `111`, without executing.
(iii) Every non-Perron root of `m_1` is a non-Perron eigenvalue, of modulus
`≤ λ_2bound < lo` (S3(b), executed), while `λ_1 ∈ [lo, hi]` (S3(a)); so exactly one root lies in
`[lo, hi]`. This is a consistency check on the executed root counts, not the identification. (iv)
Executed below.
(v) Synthetic division of `m_1` by `λ − t` in `Q[t]/(m_1)` gives
`p(λ) = Σ_k p_k(t) λ^k` with `p_{d−1} = 1`, `p_{k−1} = m_{1,k} + t p_k`
(Horner; no field inversion), and `x = p(Q) 1 = Σ_k p_k(t) Q^k 1` is a
combination of the Krylov vectors with field coefficients. Since `p(λ_i) = 0` for every root `λ_i ≠
λ_1` of `m_1` and `p(λ_1) = m_1'(λ_1) ≠ 0`
(squarefree), `x = a_1 m_1'(λ_1) v_1` is a nonzero multiple of the Perron
vector; `(Q − t) x = m_1(Q) 1 = 0`. The statistic is scale-free, so `s = N(t)/D(t)` with `N = Σ_O
w_O x_O^2 c_O`, `D = Σ_O w_O x_O^2 ∈ Q[t]` and `D(λ_1) > 0`. With `m_1` monic and irreducible,
`Res_λ(m_1, y D − N) = Π_{m_1(λ_i)=0} (y D(λ_i) − N(λ_i))` vanishes at `y = s`, so the minimal
polynomial of `s` is an irreducible factor of the resultant; `s` lies in the S3 enclosure, and when
exactly one irreducible factor has a root there, and exactly one, that factor is the minimal
polynomial. ∎

*Executed.* The Krylov dimension by the incremental echelon form of
`1, Q1, …` modulo `2^{61} − 1` and `2^{89} − 1` (independence modulo a prime implies independence
over `Q`; the two primes agree at every step): `d = 8` at `(4; 3,1,2)`, `30` at `(4; 5,2,4)`, `16`
at `(5; 3,1,2)`, `111` at `(5; 5,2,4)`. The integer coefficients of `m_1` are found by a
multi-modular solve on `d` rows independent modulo `2^{61} − 1` (a search step, no authority) and
the dependency `m_1(Q) 1 = 0` is then verified exactly in integer arithmetic on every orbit at all
four cases — at `d = 111` with coefficients of up to 526 digits, in about ten seconds (C4); the
supervisor's independent exact construction of the same degree-111 polynomial (pack
`specs/supervisor_control_block06_krylov_d111_exact.out.txt`, 795 s), and the contract lens's
earlier one, are recorded controls, not inputs. At width 4 the characteristic polynomial of `Q` has distinct irreducible factors of degrees
`1, 1, 2, 8` (the linear factor `λ` with multiplicity `27`, the others simple; `27 + 1 + 2 + 8 = 38`)
at `(3,1,2)` and `1, 1, 1, 5, 30` (all simple) at `(5,2,4)`, and `m_1` is its factor of degree `d`
(C5). `m_1` is
irreducible at `d = 8, 30, 16`
(sympy `factor_list`, C6); by Sturm counts exactly one real root lies in
`[lo, hi]` and none above `hi` at those degrees (C7). At `d = 8` and `16`: `Q x = λ_1 x` holds
modulo `m_1` on every orbit, `x` is one-signed on `[lo, hi]` by rigorous interval evaluation, the
resultant (computed by exact evaluation at `d + 1` integers and Lagrange interpolation) factors, and
exactly one irreducible factor has exactly one root in the S3 enclosure, for `s_inner` and for
`s_edge`: the minimal polynomials have degree `8` at `(4; 3,1,2)` and `16` at `(5; 3,1,2)`, printed
under `--exact`; the interval image of `N/D` on a refined isolating interval of `λ_1` meets the S3
enclosure (D7): the two routes agree where both run. At `d = 30, 111` the identification is not
attempted and the S3 enclosure stands alone.

## Theorem S5 — the separation at every executed width

**S5 (executed).** `s − f > 10^{-3}` at every width `W = 2, 3, 4, 5`, both pairs, both triples (E1):
the lower endpoint of each enclosure minus `f` is `0.00611624…` (edge) and `0.00628418…` (inner) at
`W = 4` and `0.00611642…`, `0.00628962…` at `W = 5` for `(3,1,2)`; `0.00252455…`, `0.00256547…` and
`0.00252457…`, `0.00256618…` for `(5,2,4)`; at `W = 2, 3` the (single) statistic minus `f` is
`0.00594…`, `0.00611…` at `(3,1,2)` and `0.00248…`, `0.00252…` at `(5,2,4)`. `s_inner > s_edge`
strictly at `W = 4, 5`, both triples: the lower endpoint of `s_inner` exceeds the upper endpoint of
`s_edge` by `1.67 × 10^{-4}`, `4.09 × 10^{-5}`, `1.73 × 10^{-4}`, `4.16 × 10^{-5}` (E2; labels
rounded down). The width-4 and width-5 values at `(3,1,2)` differ by `s_inner: [5.4436 × 10^{-6},
5.4437 × 10^{-6}]` and `s_edge: [1.8169 × 10^{-7}, 1.8170 × 10^{-7}]` (E3; outward labels of the
interval differences; the contract's `5.4437`, `1.8170` are the upper labels). The ratio bounds
`λ_2bound/lo ≤ 0.05538, 0.03301, 0.06932, 0.04150` (E4; rounded up). These are executed facts at the
four widths; `s_inner` has two data points; nothing is stated about any other width, about how the
values depend on the width, or about the plane.

## No-Go Discipline Gate

The only negative sentence of this note is "the enclosures exclude `f`" — an exact finite statement
about eight rational intervals at the declared widths and triples, a corollary of S3 and E4 at their
scope. It is not a route no-go. The gate is answered briefly for the statement "the separation
persists at widths 4 and 5".

### N1 — Routes by which the two laws could still agree at these widths

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a wrong enclosure | the true `s` lies outside the interval | S3 is a proved chain with exact rational arithmetic; the block-02 field route agrees at widths 2, 3 (D6) and at degrees 8, 16 (D7) | ATTEMPTED |
| 2 the sector misses part of the law | the center-row law has a component outside the `G`-invariant sector | S1 proves the law is `G`-invariant; the sector equals the full state at twenty finite-`n` values (B5) | ATTEMPTED |
| 3 the end records | the deep-row law depends on the end rows | F3 (block 02, cited) and the executed `P(e_y)` check at `n = 33` (D5) | ATTEMPTED |
| 4 a different pair | a pair on which the two laws agree | the edge pair and the innermost pair are both separated; other pairs of widths 4, 5 are not computed | ATTEMPTED (two pairs); others not executed |
| 5 the constant rule | `p = q = r` | excluded by the named variation reading (block 01, cited through block 02) | RULED OUT BY PRIOR (block 01, proposed, unaudited: upstream evidence) |
| 6 a different order or width | an order whose formation law has the static statistic, or a width at which they meet | not this note's object; the formation side is width- and row-independent (E4) and the static side is computed at four widths only | not executed; obligation named |

### N2 — Wall-independence audit

Walls: `W_R` (records-only reading, entering through `f`), `W_var`
(`(p, q, r)` not all equal), `W_pos` (positivity), `W_sym` (symmetric
isotropic `φ`, constant site weight), `W_width` (widths 2 to 5 only). No wall closes another: the
constant rule is positive and symmetric but not varying; an asymmetric `φ` keeps positivity and
variation but breaks S2 (the lens's `W = 2` counterexample); the width wall is independent of the
rule walls. The headline uses all five as hypotheses.

### N3 — Hidden-wall scan

Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally",
"obviously", "canonical", "registered", "background", "bridge context": no hits outside this
section. The spectral theorem for self-adjoint operators is named as cited scaffolding (S2); the
readings are the named premises of blocks 01–02.

### N4 — Per-citation table

| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 02 (proposed, unaudited): F1, F2, F3, E4 | the strip's static law and the formation value | the same objects at widths 4, 5 | yes (restated; F1 re-executed) |
| the spectral theorem for self-adjoint operators (classical) | real spectrum and orthonormal eigenbasis | S2's consequences | yes (scaffolding, cited) |
| the classical ratio, residual–gap and Krylov results | bounds on eigenvalues and eigenvectors | re-proved at scope in S3, S4 | yes (re-proved) |

### N5 — Resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "the enclosures exclude `f`" | executed: every row state of widths 2 to 5 | executed: the edge and innermost pairs of every row; every site of both end rows in the boundary check | executed: the Perron root, every other eigenvalue's modulus, the Perron vector's angle, the Krylov degree | executed: the finite-`n` center rows for `n ≤ 65` (sector) and `n ≤ 7` (full state); the width-4 characteristic polynomial | checked and not executed: strips of widths 2 to 5 only; the plane and wider strips are named, not computed |

The runner prints matching `per_element:` … `lattice_wide:` lines.

### N6 — Partial-closure paths and primitive scan

No axiom, primitive or convention is proposed or changed; the registered approved primitives are not
used. No wall language of the form "no retained primitive supplies this" appears.

### N7 — Steelman

"The separation at widths 4 and 5 is a boundary effect of a narrow strip: the edge pair touches the
open boundary and the innermost pair at width 5 is one step from it; a pair deep inside a wide strip
could carry the formation value exactly." This is not refuted here: the note has two pairs at two
widths and says nothing about wider strips. It is the next block's target, not a defect of this
note's claims, which are finite statements at the declared widths.

### N8 — Cross-cycle echo

Block 02's F5 named the same separation at widths 2, 3 by the field route; block 01's steelman named
the possibility that an infinite-volume limit taken along growing windows removes the normalizer
history. Neither has been retired; this note adds two widths by a different route and does not
decide the plane.

## Falsifiers

The theorems fail if any of these finite statements fails: orbit counts other than `3, 8, 38, 178`;
`T` not commuting with some map of `G`; `Q` depending on the representative; `R_{OO'} |O'| ≠ |O|
Q_{OO'}`; a sector value differing from the full-state value at some executed `n`; `w_O Q_{OO'} ≠
w_{O'} Q_{O'O}` for some pair; `tr(Q^2)` other than the four displayed integers; `μ` outside `[lo,
hi]`; `δ ≤ 0` or `lo ≤ λ_2bound`; a square-root bound below the true root; an enclosure of width `≥
10^{-50}`, or containing `f`; a finite-`n` distance not strictly decreasing; an end-record value
beyond `10^{-6}` of the enclosure; a width-2 or width-3 enclosure differing from block 02's digits;
a Krylov dimension other than `8, 30, 16, 111`; the dependency `m_1(Q) 1 = 0` failing on some orbit;
`m_1` reducible at `d = 8, 30, 16`; a Sturm count other than one root in `[lo, hi]` and none above;
`Q x ≠ λ_1 x` modulo `m_1`; an enclosure containing roots of two irreducible factors of the
resultant, or of none; `s − f ≤ 10^{-3}` at some width; `s_inner ≤ s_edge` at width 4 or 5; a ratio
bound below the executed rational; a decimal label in the runner's output not produced by its
integer-arithmetic expansion.

## Boundaries and non-claims

This note encloses the static strip's deep-row pair statistics exactly at widths four and five and compares them with the formation value; it states nothing about the plane's static law beyond these widths, and no monotonicity in the width is claimed.

No order is selected as physical; no plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The transfer-matrix and positive-matrix machinery is cited from block 02, and the two-sided ratio, trace, residual–gap and Krylov steps are proved here at the scope used; the spectral theorem for self-adjoint operators is cited scaffolding; no value, constant or theorem is imported as authority.

Further: the deep-row law is block 02's F3 object (the center-row law of the `n`-row strip as `n`
grows, end-record independent), cited, not re-proved; the finite-`n` sequences and the `n = 33`
end-record check are executed facts for those `n`, not theorems; `s_inner` is a distinct statistic
only at widths 4 and 5, two data points; the identification of the statistics as algebraic numbers
is executed at Krylov degrees 8 and 16 only; at degree 111 the polynomial is verified and neither
irreducibility nor its factorization is claimed; the ratio bounds bound `λ_2bound/lo`, not
`λ_2/λ_1`; the width-4 and width-5 differences are two numbers, not a law; no formation site,
probability or rate is supplied; no axiom or primitive is changed.

## Imports

References, re-proved at scope, never authority, no values imported: the Collatz–Wielandt bounds on
the Perron root (S3(a), from block 02's F2); the Davis–Kahan sin-θ bound in its one-dimensional
self-adjoint form (S3(c)); the relative minimal polynomial of a matrix on a vector and its roots
(S4); the Perron–Frobenius theorem for positive matrices, re-proved in block 02 (F2) and cited from
there. Cited scaffolding, not re-proved: the spectral theorem for self-adjoint operators on a
finite-dimensional real inner-product space
(S2); Gauss's lemma, used only to expect integer coefficients of `m_1` in the
search step (the verification does not depend on it); Sturm's theorem, resultants and factorization
over `Q` as implemented in `sympy` (exact rational arithmetic; the runner checks each root count and
each dependency itself); the primality of the two Mersenne moduli (the rank argument) — the CRT
moduli's primality is not load-bearing since the dependency is verified exactly. Declared
mathematical scaffolding: the exact weight triples, the power `k = 40`, the square-root scale
`10^{80}`, the widths and the row lengths, the end record `P(e_y)`. No observation, fitted value or
literature constant enters.

## Review record

Fable primary seat (own 26-mutation census, read from raw per-mutation stdout); a hostile refuter
lens on the contract before the build (Opus 5; its fifteen findings D1–D15 and a late result folded
into the contract: exact outward-rounded digits, S2's three hypotheses, the left-Perron-vector proof
of the upper ratio bound, the side conditions of S3(b), (c), S3(d) derived from F3, S4 reordered,
the classical names moved out of the theorem statements, block 05 dropped from the premises, the
exact degree-111 polynomial recorded as a control); refuting checker (Opus 5, disjoint machinery)
pending; supervisor fold pending. Contract facts settled while executing: the supervisor's control
printed the `sin θ` labels as `0.99 × 10^{-59}` and the like (mantissa below one); this note prints
the same bounds normalized
(`9.82 × 10^{-60}`); the boundary check is executed on the full state with
the single record `P(e_y)` on every site of both end rows through the tensor structure of `V` (the
contract said "sector"; a single record is not `G`-invariant, so the sector version uses the
orbit-averaged record and is executed as well); the degree-111 dependency, which the contract left
to the lens's and the supervisor's 13-minute controls, is verified exactly by the runner itself in about ten seconds by a
multi-modular search and an integer verification; the resultant is computed by exact evaluation and
interpolation rather than a bivariate call. The supervisor's control numbers (orbit counts, Krylov
dimensions, `λ_1` to eighteen digits at four cases, the innermost enclosure and the `n = 33` sector
value at width 5) were reproduced in the seat's own code before any theorem sentence was written.

## Verification

```bash
python3 scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py
python3 scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py --exact
python3 scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py --list-mutations
python3 scripts/admissibility_rule_static_strip_widths_4_5_rigorous_enclosure_separation_2026_09_07.py --mutation trace_bound_forged
```

Families: A authority and inputs; B the orbit sector; C self-adjointness, the Perron root and the
Krylov degrees; D the rigorous enclosures; E the separation at every executed width; F fences,
forbidden phrases, the floating-point self-scan, the placement of the classical names and the
decimal-label scan; G the resolution lines. Each of the 26 declared mutations perturbs one object or
one comparison and fails in exactly one family (`mutation_family_expected:` /
`mutation_family_observed:` lines); `--exact` prints the rational endpoints, the Krylov polynomials
and the minimal polynomials of the statistics. Expected final line: `TOTAL: PASS=34 FAIL=0`.
