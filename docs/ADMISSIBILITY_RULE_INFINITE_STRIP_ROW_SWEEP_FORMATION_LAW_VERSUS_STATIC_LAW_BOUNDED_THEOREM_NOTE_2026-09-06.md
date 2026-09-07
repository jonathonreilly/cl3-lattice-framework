---
claim_id: admissibility_rule_infinite_strip_row_sweep_formation_law_versus_static_law_bounded_theorem_note_2026-09-06
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu with the covariant positive product rule at the declared exact weight triples (3, 1, 2) and (5, 2, 4): the specification consistency of the finite-window static laws with exterior records, executed on the open 2x2x2 cube and the plaquette (Theorem C1); existence of an infinite-volume static law on Z^3 for the finite menu by compactness and the finite-window conditional identity, with a translation-invariant limit (Theorem C2, proved, no uniqueness); the row sweep's exact solvability on strips of every width and length including the infinite strip (rows indexed by N) and the quadrant (the half-plane swept row by row from its left end) under the records-only reading (Theorem E: every row is the path static chain p_0; every horizontal and vertical nearest-neighbor pair has the single-edge law with pair-parallel probability p/(p+q+4r)), executed at widths 2, 3 and 4; the static law of the width-2 and width-3 strips: an exactly enclosed center-row pair-parallel probability s_inf as an algebraic number (Theorem F) and its separation from the formation value (F5). No uniqueness on Z^3, no static law of the plane, no three-recorded-neighbor sweep, no order selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py
---

# On an infinite strip the row-sweep formation law is the path chain on every row while the static law is not: the normalizer history does not wash out

**Date:** 2026-09-06
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py`](../scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.txt`](../logs/runner-cache/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.txt)

## Result up front

Take the same fixed rule as before, the one that gives the odds for a new
record from the records its neighbours already carry, and lay records down on
a long strip of lattice row by row, each row from left to right. Then each row
taken by itself looks exactly like a single chain of records, and every
neighbouring pair, sideways or upward, has the odds of an isolated pair. The
single static pattern law that the same rule defines for the whole strip gives
neighbouring pairs different odds, and the gap between the two stays fixed no
matter how long the strip grows. So the order in which records form leaves a
permanent trace on an infinite patch of lattice, and the rule alone still does
not fix the pattern. Nothing here says which order is the physical one, and
nothing is said about the full plane or about whether the whole lattice
carries one static pattern law or several.

Exactly: for the product rule with orbit weights `(p, q, r)` on the strips
`S_{W,n}` (rows of width `W`, `n` rows, nearest-neighbor edges, open boundary)
under the row sweep and the records-only reading, the formation law has the
row-to-row kernel `P` of (E2), the first row has the path static law
`p_0(ρ) = (1/6) Π_j K(ρ_{j−1} → ρ_j)` with `K = φ / (p + q + 4r)`, and
`p_0 P = p_0` by a telescoping identity (E3), so every row of every strip,
including the infinite strip and the half-plane, has the law `p_0` and every
horizontal or vertical nearest-neighbor pair has the single-edge law `(1/6) K`
with pair-parallel probability `p/(p + q + 4r)` (E4): `1/4` at `(3, 1, 2)`,
`5/23` at `(5, 2, 4)`. The static law of the same strip has a center-row
pair-parallel probability `s_∞` that is an algebraic number of degree 3 at
`(3, 1, 2)` and degree 8 at `(5, 2, 4)` for `W = 3`, enclosed in exact rational
intervals of width below `10^{-30}`, `s_∞ ∈ [0.2561109872857786908612, 0.2561109872857786908613]`
and `s_∞ ∈ [0.2199151616870197815075, 0.2199151616870197815076]` (decimal
endpoints rounded outward), which exclude `1/4` and `5/23` (Theorem F, F4–F5).
The finite-window static laws with exterior records form a specification
(Theorem C1, executed on the cube and the plaquette) and an infinite-volume
static law on `Z^3` exists for the finite menu (Theorem C2, proved; nothing
about uniqueness). Executed with exact arithmetic: 39 checks, 30 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 01's steelman obligation: 'an infinite-volume limit taken along growing windows could wash out the normalizer history'; and the owner's sequencing gate (2026-08-26): what the Admissibility rule induces on the infinite lattice is unidentified; the parked statistical-bridge decision wakes on 'the committed-action identification lands', which this note does not fire"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "next block: uniqueness of the infinite-volume static law on Z^3 (the contraction region of the one-site conditional's dependence on its six neighbors) and the static law of the plane; consumers: the parked statistical-bridge decision material (docs/repo/DEFERRED_DECISIONS.md entry 1, read-only), the record-matter lane's formation-order supply"
conditional_surface_status: "exact on the declared strips, windows, menu and triples; Theorem E's proof is for every width and length; Theorem C2 is an existence proof on Z^3 for the finite menu; conditional on the records-only reading and the declared sweep where stated; no uniqueness, no plane, no three-neighbor sweep"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorem C1 is executed exhaustively on the declared windows and C2 is a native compactness-and-consistency proof; Theorem E is proved by an exact telescoping identity for every strip and executed at widths 2, 3, 4; Theorem F is executed as an exact algebraic enclosure at widths 2 and 3 with the Perron-Frobenius step re-proved; the separation F5 is an exact statement on an infinite window; nothing about uniqueness, the plane, a physical order, the Born form or the bridge is claimed."
```

## Premises and declared objects

The only scientific dependencies are the four axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and the
upstream note
[`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)
(block 01; proposed, unaudited), whose definitions are restated here where
used. The axiom sentences used, verbatim (runner A2, A3):

- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and "For
  each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form." — "records are permanent" — "Only records are
  readable." — "A site with no record cannot be read."

**Menu, rotations, weights.** `M` = the six projectors `P(±e_a)`, indexed
`P(+e_x), P(−e_x), P(+e_y), P(−e_y), P(+e_z), P(−e_z)`; the 24 proper cubic
rotations act as signed axis permutations, transitively; ordered pairs fall
into the parallel, antiparallel and orthogonal orbits. The product rule (P):
`r(s | η) ∝ Π_{y∈A} φ(s, η_y)` over the recorded neighbors `A`, with `φ`
symmetric and isotropic with orbit values `(p, q, r)`, the site weight
constant on the transitive menu (block 01, B7). Declared triples `(3, 1, 2)`
and `(5, 2, 4)`; the constant triple `(2, 2, 2)` as the boundary.

**The one-edge kernel.** `Z_1 = Σ_s φ(s, a) = p + q + 4r` for every `a`
(transitivity), and `K(a → s) = φ(s, a)/Z_1`: symmetric because `φ` is, so
its rows and its columns sum to one; the uniform law is `K`-invariant
(runner B1, B3, symbolic in `p, q, r`).

**Readings carried from block 01, named, nothing new adopted.** (i) The
records-only reading: an unrecorded neighbor contributes no factor and is not
a condition. (ii) Positivity of the rule. (iii) The extensional reading of the
variation clause restricted to the declared menu: `(p, q, r)` not all equal.
(iv) The formation order is an unsupplied input; here the row sweep is a
declared order, and no order is selected as physical.

**Static law with exterior records.** For a finite window `Λ` with exterior
records `ω` on `∂Λ`, `μ_Λ^ω(v) ∝ Π_{xy∈E(Λ)} φ(v_x, v_y) Π_{x∈Λ, y∈∂Λ, x∼y} φ(v_x, ω_y)`;
its full conditionals are the rule with every neighbor recorded (block 01,
Theorem A). Windows used: the open `2×2×2` cube with block 01's exterior
assignment (the exterior neighbor along axis `a` carries `P(e_a)`; site
`i = x + 2y + 4z`), and the plaquette with block 01's exterior
`(P(e_x), P(−e_y))` at every site.

**Strips and the sweep.** `S_{W,n}` is the `W × n` grid (rows `i = 0..n−1`,
columns `j = 0..W−1`, nearest-neighbor edges, open boundary: as a window of
`Z^3` every strip site also has out-of-plane and out-of-strip neighbors, and
they carry no records on either side of the comparison — under the
records-only reading they contribute nothing to the formation law, and the
static law is the open-boundary one); `S_W` is the infinite strip (rows
indexed by `N`; a two-sided strip is not needed, see F5); the half-plane is the quadrant with
rows and columns both indexed by `N`, swept row by row, each row from its
left end (Theorem E treats it through its finite-width marginals). The row sweep
`σ_row`: rows in order, each row left to right; under the records-only
reading site `(i, j)` forms with the recorded neighbors `(i, j−1)` (if
`j > 0`) and `(i−1, j)` (if `i > 0`). The FORMATION law is block 01's
`μ_σ(v) = Π_k r(v_{x_k} | v restricted to A_k)`.

**Row objects.** Row states `ρ ∈ M^W`; the path static law
`p_0(ρ) = (1/6) Π_{j≥1} K(ρ_{j−1} → ρ_j)`, the formation law of the path
swept from an end (block 01, Theorem B; runner B4 re-executes it for
`W = 2, 3`); the row-to-row formation kernel `P(β → α)` (row `β` recorded,
row `α` forming); the row transfer matrix `T(ρ, ρ') = V(ρ, ρ') A(ρ')` with
`A(ρ) = Π_j φ(ρ_j, ρ_{j+1})` (row-internal edges) and
`V(ρ, ρ') = Π_j φ(ρ_j, ρ'_j)` (vertical edges), so the static weight of the
`n`-row strip is `A(ρ^0) Π_{i≥1} T(ρ^{i−1}, ρ^i)`; the row symmetry group
`G` = the 24 rotations acting diagonally on the entries, times the strip
reflection `ρ ↦ ρ^{rev}` (the runner uses all 48 pairs).

## Prior art and what is new

Block 01 (linked above) is the parent: it defines the two laws, proves the
identity `μ_σ Π_k Z_k = μ Z_W` and the classification "the formation law
equals its static law exactly when every record forms with at most one
recorded neighbor", and leaves in its steelman the obligation quoted in the
status block. Classical facts used here are re-proved at the scope where they
are used and never imported as authority: Perron–Frobenius for a matrix with
positive entries (Wielandt's maximin argument, Theorem F2); compactness of a
countable product of finite sets by a diagonal argument and the passage of
finite-window conditional identities to a limit (Theorem C2). One classical
observation is referenced only, as `classical: certain sequential lattice
processes have product-form or Markov-chain invariant row measures — the
Pickard / Markov-mesh construction`; no author claim is made and nothing is
taken from it — Theorem E is proved here
from the symmetry of `φ` and the constancy of `Z_1` (on this menu a consequence
of transitivity; a symmetric pair weight with constant row sums on a
non-transitive menu satisfies the same two hypotheses), through `Z_2 = Z_1^2 K^2`. The prior-art sweep is recorded in
the pack's `ROUTE_PORTFOLIO.md` (block 02 section); no landed note states any
of the objects below.

New here: the specification consistency executed with exterior records (C1);
the existence proof on `Z^3` for the finite menu (C2); the exactly solvable
sweep (E1–E4) with the telescoping proof and its execution at widths 2, 3, 4;
the exact algebraic enclosure of the static infinite strip's center-row pair
statistic at widths 2 and 3 (F4); and the separation on an infinite window
(F5).

## Exact target and obligation graph

**Target.** On the infinite strip `S_3` (and `S_2`), for the product rule at
each declared triple under the records-only reading: the row-sweep formation
law's row marginal is `p_0` with nearest-neighbor pair-parallel probability
exactly `p/(p + q + 4r)`, and the static law's center-row pair-parallel
probability `s_∞` lies in an exact rational interval that excludes it.

| obligation | disposition |
|---|---|
| the static law's full conditionals are the rule with all neighbors recorded (Theorem A of block 01) | cited; C1 re-executes the cancellation with exterior records |
| specification consistency C1 on the cube (face, edge, site) and the plaquette (edge, site) | executed (C1–C5); finite range by grouping (C6) |
| compactness of `M^{Z^3}`, the cylinder-limit measure, the limit identity, a translation-invariant limit | proved here (C2) with dependent choice only; the Carathéodory extension cited |
| `Z_1` constant; `Z_2 = Z_1^2 K^2` (E1); the row kernel formula (E2) | proved here; executed symbolically (B1, B2) and entrywise (D1) |
| `p_0 P = p_0` (E3) by telescoping; the pair laws (E4); the width restriction lemma | proved here for every `W`; executed `W = 2, 3, 4` (D2, D5), (D3) and (D9) |
| the finite-strip formation law is `p_0 P^{n−1}` on rows and row pairs | executed from block 01's definition (D4) |
| `T` commutes with `G`; the Perron vector is `G`-invariant; the quotient (F1) | proved here; executed (E1, E2, E5, E6) |
| Perron–Frobenius for positive matrices (F2) | re-proved here (Wielandt) |
| the center-row law formula, its limit and its boundary independence (F3) | proved here; executed for `n ≤ 13` (E9) and with end records (E11) |
| the exact enclosure of `s_∞` and the second-eigenvalue bound (F4) | executed (E3–E10) |
| uniqueness of the infinite-volume static law; the static law of the plane; a three-neighbor sweep | open; not this note |

The strongest missing lemmas are uniqueness of the infinite-volume static law
on `Z^3` and any statement about the plane's static law; neither is used by
the target, which is a statement about strips.

## Theorem C — the specification and an infinite-volume static law

**C1 (consistency, executed).** Let `Λ` be a finite window with exterior
records `ω`, `Δ ⊂ Λ` a sub-window, and fix the records on `Λ ∖ Δ`. The
conditional law of `v_Δ` under `μ_Λ^ω` equals `μ_Δ^{ω'}`, where `ω'` gives
each site of `Δ` its exterior records from `ω` and the records on the sites
of `Λ ∖ Δ` adjacent to it. *Proof.* In the ratio
`μ_Λ^ω(v_Δ, v_{Λ∖Δ}) / Σ_{u} μ_Λ^ω(u, v_{Λ∖Δ})` every factor not containing a
site of `Δ` is common to numerator and denominator and cancels; what remains
is `Π_{xy∈E(Δ)} φ(v_x, v_y) Π_{x∈Δ} Π_{y adjacent to x, y∉Δ} φ(v_x, ω'_y)`
normalized over `v_Δ` — the sub-window law with the adjacent records as
exterior. ∎ Executed on the cube for `Δ` = one face (sites `0..3`, all
`6^4` complements against all `6^4` face states), one edge (sites `0, 1`,
all `6^6` complements) and one site (all `6^7` complements), and on the
plaquette for one edge (all `36` complements) and one site (all `216`), both
triples, by integer cross-multiplication of the two normalized vectors
(C1–C5). The finite-range statement — the conditional depends only on the
adjacent records — is executed by grouping: the cube edge has `1296` classes
of adjacent records with `2` non-adjacent complement sites, the cube site
`216` classes with `4`, the plaquette site `36` classes with `1`, and the
conditional is constant on each class (C6).

**C2 (existence, proved; nothing about uniqueness).** The family
`{μ_Λ^ω}` over finite windows and exterior assignments is a specification of
range one: C1 is exactly the consistency condition, and the conditional
kernel of `Δ` depends on the outside only through `∂Δ`. Let `Λ_n` be any
exhausting sequence of finite windows (`Λ_n ⊂ Λ_{n+1}`, every site in some
`Λ_n`) with any boundary records `ω_n`, and extend `μ_n = μ_{Λ_n}^{ω_n}` to
`M^{Z^3}` by placing `ω_n` (or any fixed value) outside `Λ_n`. The cylinder
events (a finite set of sites and an assignment on it) are countable; list
them `C_1, C_2, …`. Since `μ_n(C_1) ∈ [0, 1]`, a subsequence converges; from
it a further subsequence converges on `C_2`; and so on; the diagonal
subsequence converges on every `C_k` (bounded sequences of rationals in
`[0, 1]` have convergent subsequences by bisection; the countable diagonal
extraction uses only dependent choice along an explicit rule, never the full
axiom of choice). The limits
`m(C)` are finitely additive on the algebra generated by cylinders and
`m(M^{Z^3}) = 1`. Each cylinder set is compact-open in the product topology
of the finite menu — the compactness of `M^{Z^3}` is the same diagonal
argument applied to a sequence of configurations, and a countable product of
finite sets is metrizable, so sequential compactness is compactness — so a
countable disjoint
union of cylinders that equals a cylinder is a finite union, and `m` is
countably additive on the algebra; the Carathéodory extension theorem (cited,
not re-proved: the definition-level step from a countably additive set
function on the cylinder algebra to a measure on the product σ-algebra; listed
under Imports) gives a probability measure `μ` on the product σ-algebra. For a finite `Δ` take `n`
with `Δ ∪ ∂Δ ⊂ Λ_n` and any cylinder event `B` determined by finitely many
sites outside `Δ`. By C1 applied inside `Λ_n`,
`μ_n(v_Δ = a, B) = Σ_b μ_Δ^{b}(a) μ_n(v_{∂Δ} = b, B)`, a finite identity
between cylinder probabilities; both sides converge along the subsequence,
so `μ(v_Δ = a, B) = Σ_b μ_Δ^b(a) μ(v_{∂Δ} = b, B)`: the limit satisfies the
finite-window conditional identity for every finite `Δ`. Translation
invariance: for the box `B_L = {0, …, L−1}^3` let
`μ̄_L = |B_L|^{-1} Σ_{t∈B_L} μ ∘ τ_t^{-1}`; each `μ ∘ τ_t^{-1}` satisfies the
identity (the specification is translation covariant), so `μ̄_L` does; for a
unit shift `e` and any cylinder `C`, `|μ̄_L(τ_e C) − μ̄_L(C)| ≤ 2 L^2 / L^3`
(the two boxes `B_L` and `B_L + e` differ in `2 L^2` sites); a diagonal
subsequence in `L` converges on every cylinder to a measure `μ̄` that is
translation invariant and satisfies the identity by the same passage to the
limit (the identity is preserved under convex combinations and under
cylinder-wise limits, and the boxes `B_L` have boundary-to-volume ratio
`2L^2/L^3 → 0`). ∎ Nothing is claimed about whether different exhaustions or boundary
records give the same limit.

## Theorem E — the row sweep is exactly solvable

Throughout: the product rule with symmetric isotropic positive `φ`, the
strip `S_{W,n}` with `W ≥ 1` and `n ≥ 1`, the row sweep and the records-only
reading. Rows are `β` (recorded) and `α` (forming).

**E1 (the two-neighbor normalizer is the two-step kernel).**
`Z_2(a, b) = Σ_s φ(s, a) φ(s, b) = Z_1^2 Σ_s K(a → s) K(s → b) = Z_1^2 (K^2)(a, b)`,
because `K(a → s) = φ(s, a)/Z_1` and `K(s → b) = φ(b, s)/Z_1 = φ(s, b)/Z_1`
by symmetry of `φ`. Executed symbolically in `(p, q, r)` for all 36 pairs
(B2).

**E2 (the row-to-row kernel).** Site `(i, 0)` forms with the single recorded
neighbor `β_0`, so its factor is `φ(α_0, β_0)/Z_1 = K(β_0 → α_0)`; site
`(i, j)`, `j ≥ 1`, forms with the two recorded neighbors `α_{j−1}` and
`β_j`, so its factor is `φ(α_j, α_{j−1}) φ(α_j, β_j) / Z_2(α_{j−1}, β_j)`,
which by E1 is `K(α_{j−1} → α_j) K(α_j → β_j) / (K^2)(α_{j−1}, β_j)`. Hence
`P(β → α) = K(β_0 → α_0) Π_{j=1}^{W−1} K(α_{j−1} → α_j) K(α_j → β_j) / (K^2)(α_{j−1}, β_j)`,
and the first row, swept from its left end with at most one recorded
neighbor per site, has the law `p_0` (block 01, Theorem B; runner B4).
Executed: the formula and the definition `Π_j r(α_j | recorded neighbors)`
agree entrywise on all `6^W × 6^W` entries for `W = 2, 3` at both triples,
and every row of `P` sums to one (D1).

**E3 (invariance: `p_0 P = p_0`).** *Proof.* Write
`p_0(β) P(β → α) = (1/6) K(β_0 → β_1) K(β_1 → β_2) ⋯ K(β_{W−2} → β_{W−1}) · K(β_0 → α_0) Π_{j≥1} K(α_{j−1} → α_j) K(α_j → β_j) / (K^2)(α_{j−1}, β_j)`.
Sum over `β_0`: the only factors containing `β_0` are `K(β_0 → β_1)` and
`K(β_0 → α_0)`, and by symmetry of `K`,
`Σ_{β_0} K(α_0 → β_0) K(β_0 → β_1) = (K^2)(α_0, β_1)`, which cancels the
`j = 1` denominator and leaves the factor `K(α_1 → β_1)` from the numerator
of `j = 1` as the only remaining factor in `β_1` besides `K(β_1 → β_2)`. Sum
over `β_1`: `Σ_{β_1} K(α_1 → β_1) K(β_1 → β_2) = (K^2)(α_1, β_2)`, which
cancels the `j = 2` denominator and leaves `K(α_2 → β_2)`. Continue: after
summing `β_{j−1}` the remaining factors in `β_j` are `K(α_j → β_j)` and
`K(β_j → β_{j+1})`, whose sum over `β_j` is `(K^2)(α_j, β_{j+1})`,
cancelling the `j + 1` denominator. The last sum,
`Σ_{β_{W−1}} K(α_{W−1} → β_{W−1}) = 1` (rows of `K` sum to one). What
remains is `(1/6) K(α_0 → α_1) ⋯ K(α_{W−2} → α_{W−1}) = p_0(α)`. ∎ The
induction over rows: row `0` has law `p_0`; if row `i − 1` has law `p_0`
then row `i` has law `p_0 P = p_0`, since under the sweep the conditional
law of row `i` given all earlier rows depends only on row `i − 1`. Hence
every row of every finite strip has law `p_0`; on the infinite strip `S_W`
the formation law is the projective limit of the consistent finite-strip
laws (the law of the first `n` rows is `μ_{σ_row}` on `S_{W,n}`, since later
rows do not enter earlier conditionals), which exists on the countable
product `M^{S_W}` by the cylinder-algebra argument of C2; its row marginals
are `p_0` without any limit. On the quadrant (the half-plane swept row by row
from the left end), the restriction lemma holds: every site's recorded
neighbors lie in its own column or to its left, so the formation law of width
`W` restricted to the first `W'` columns is the width-`W'` formation law
(executed at `3 → 2` on the two-row joint, D9), the finite-width marginals are
consistent, and the Kolmogorov extension on the countable product gives the
quadrant's law, whose every finite-width row marginal is the path chain. ∎
Executed: `p_0 P = p_0` on all `6^W` row states for `W = 2, 3` at both
triples (D2) and for `W = 4` (`1296` row states; integer numerators over a
common denominator; both triples; 0.5 s) (D5).

**E4 (nearest-neighbor pairs).** The partial sums of the proof give the
joint law of `(α_0, …, α_{j−1}, β_j)`:
`(1/6) Π_{l<j} K(α_{l−1} → α_l) · (K^2)(α_{j−1}, β_j)`, and continuing the
sum over `β_j` gives `(1/6) Π_{l≤j} K(α_{l−1} → α_l) K(α_j → β_j)` for
`(α_0, …, α_j, β_j)`. Marginalizing: every vertical pair `(β_j, α_j)` has
the law `(1/6) K(β_j → α_j)`; every horizontal pair `(α_{j−1}, α_j)` has
the law `(1/6) K(α_{j−1} → α_j)` (the row law is `p_0`); the diagonal pair
`(α_{j−1}, β_j)` has the law `(1/6) (K^2)(α_{j−1}, β_j)`, which is not
`(1/6) K` since `K` is not idempotent (its eigenvalues are `1`,
`(p + q − 2r)/Z_1` twice and `(p − q)/Z_1` three times, block 01 E4c). The
pair-parallel probability of a `(1/6) K` pair is `Σ_a (1/6) K(a → a) = p/(p + q + 4r)`:
`1/4` at `(3, 1, 2)`, `5/23` at `(5, 2, 4)`, for every row `i ≥ 0` and every
column. Executed: all vertical pairs at every column, all horizontal pairs,
and the diagonal `(K^2)` pair, `W = 2, 3`, both triples (D3).

**Executed instances beyond the kernel.** The finite-strip formation law
computed directly from block 01's definition on all `6^{Wn}` configurations
(`W = 2`: `n = 2, 3`; `W = 3`: `n = 2`) equals `p_0 P^{n−1}` on every row
marginal and on the joint law of the last two rows (D4). The constant rule
`(2, 2, 2)`: `K` uniform, `p_0` uniform on `6^W` states, trivially invariant
(D6). An asymmetric-weight control (`φ(a, b) = φ_{(3,1,2)}(a, b) + [a < b]`,
with `K(a → s) = φ(s, a)/Σ_t φ(t, a)`): `p_0 P ≠ p_0` on all `36` of `36`
row states at `W = 2` and all `216` of `216` at `W = 3` — the symmetry of
`φ` is load-bearing in E1 and E3 (D7).

**Remark (three recorded neighbors; a witness, not a theorem).** The
telescoping needs, at each site, that the normalizer of its two recorded
neighbors be the kernel that summing the common earlier neighbor produces
(`Z_2/Z_1^2 = K^2`). For a sweep in which a site forms with three recorded
neighbors the normalizer is `Z_3(a, b, c) = Σ_s φ(s, a) φ(s, b) φ(s, c)`,
which is not a product of two-step kernels, and the joint law of the three
recorded neighbors under the chain formed so far need not be proportional to
it. Executed on the cube with the index order `0..7` at `(3, 1, 2)`: the
last site `7 = (1, 1, 1)` forms with the recorded neighbors `3, 5, 6`; the
joint law of `(v_3, v_5, v_6)` under the seven-site formation chain is not
proportional to `Z_3` (the proportionality fails for `210` of the `216`
triples, D8). Nothing is claimed about any three-neighbor sweep beyond this
witness; on the strip the corresponding premise holds exactly (the diagonal
pair law `(1/6) K^2`, D3).

## Theorem F — the static infinite strip, exactly enclosed

**F1 (symmetry reduction).** For `g ∈ G`, `A(gρ) = A(ρ)` and
`V(gρ, gρ') = V(ρ, ρ')` (isotropy of `φ` for rotations; the reflection
reverses both rows and both products), so `T(gρ, gρ') = T(ρ, ρ')`. Executed:
all `48` maps on all `36 × 36` pairs at `W = 2` and on the `8` orbit
representatives against all `216` rows at `W = 3`, both triples (E2). If
`ρ_1` is the Perron vector of `T` (F2), then `g ρ_1` (entries permuted) is a
positive eigenvector for the same eigenvalue, hence a positive multiple of
`ρ_1`, and the multiple is one because a permutation preserves the entry
sum: `ρ_1` is constant on `G`-orbits. On orbit-constant vectors `T` acts as
the quotient `Q_{O,O'} = Σ_{ρ'∈O'} T(ρ, ρ')` for any `ρ ∈ O` (well defined,
since `O'` is `G`-stable and `T` is `G`-invariant). `Q` has positive entries.
Its Perron vector `x` lifts to `ρ_1(ρ) = x_{orbit(ρ)}`, a positive
eigenvector of `T` with `Q`'s Perron root, which is therefore `T`'s (a
positive eigenvector belongs to the Perron root: pair it with the positive
left Perron vector). Row orbits: `3` at `W = 2` and `8` at `W = 3`, both
triples (E1); `Q` is `8 × 8` with integer entries at `W = 3`.

**F2 (Perron–Frobenius for a positive matrix, re-proved).** Let `T` be a
square matrix with all entries positive. For `v ≥ 0`, `v ≠ 0`, put
`r(v) = min_{i: v_i>0} (Tv)_i / v_i`. Since `Tv > 0` for every such `v`,
`r` restricted to the compact set `T(simplex) ⊂ {v > 0}` is continuous and
attains its maximum `λ_1` at some `v* > 0`; and `λ_1 ≥ r(v)` for every
`v ≥ 0`, `v ≠ 0`, because `Tv ≥ r(v) v` entrywise gives `T(Tv) ≥ r(v) Tv`,
i.e. `r(Tv) ≥ r(v)`. The vector `Tv/Σv = T(v/Σv)` lies in
`T(simplex)`, and homogeneity gives `r(Tv/Σv) = r(Tv)`. If
`Tv* ≠ λ_1 v*` then `Tv* − λ_1 v* ≥ 0` is nonzero, so `T(Tv* − λ_1 v*) > 0`,
i.e. `r(Tv*) > λ_1`, a contradiction; hence `Tv* = λ_1 v*` with `v* > 0` and
`λ_1 > 0`. For any eigenvalue `μ` with eigenvector `z`,
`|μ| |z| = |Tz| ≤ T|z|` entrywise, so `|μ| ≤ r(|z|) ≤ λ_1`; if `|μ| = λ_1`
the same argument makes `|z|` an eigenvector and forces equality in the
triangle inequality in every row, so all `z_j` have a common argument and
`μ = λ_1`. The eigenspace of `λ_1` is one-dimensional: otherwise choose a real
eigenvector `w` not proportional to `v*` (the matrix is real, so real and
imaginary parts suffice), and replace its sign if needed so some `w_i > 0`.
Then `v* − c w`, with `c = min_{w_i>0} v*_i/w_i`, is nonnegative, has a zero
entry, and is nonzero because `w` is not proportional to `v*`. Its image
`T(v* − cw) = λ_1 (v* − cw)` would have a zero entry although `T` maps
nonnegative nonzero vectors to positive ones.
Algebraic simplicity: a generalized eigenvector `w` with `(T − λ_1) w = v*`
would give, with the positive left Perron vector `u` (the same argument for
`T^T`), `0 = u^T (T − λ_1) w = u^T v* > 0`. ∎ The transfer matrix `T` has
positive entries because `φ > 0`.

**F3 (the limit law).** The `n`-row static weight is
`A(ρ^0) Π_{i≥1} T(ρ^{i−1}, ρ^i)`, so the center row `c = ⌊n/2⌋` has the
marginal `∝ (A T^c)(ρ) · (T^{n−1−c} 1)(ρ)`. The row vector `A` and the column
vector `1` are `G`-invariant. Orbit-constant columns evolve by `Q`.
For a row vector with per-entry orbit values `a_O`, let
`D = diag(|O|)` and record its orbit masses as the row `a D`. Counting all
entries in each target orbit gives `(a D)' = (a D) Q`; equivalently the
per-entry row values evolve by `D Q D^{-1}`. Thus both free-end factors
evolve in the orbit sector, with the same spectrum as `Q`, provided the row
coordinates include these orbit sizes. The left Perron vector of `T` is `A · ρ_1`:
`Σ_ρ A(ρ) ρ_1(ρ) T(ρ, ρ') = A(ρ') Σ_ρ V(ρ', ρ) A(ρ) ρ_1(ρ) = A(ρ') (Tρ_1)(ρ') = λ_1 A(ρ') ρ_1(ρ')`
by symmetry of `V` (executed exactly in `Q(λ_1)`, E6). In the orbit sector
write `Q^k = λ_1^k Π_Q + R_k^Q`, with `Π_Q` its Perron projection. At both
triples all nonzero eigenvalues of `Q` are simple (the characteristic
polynomial's nonzero roots are distinct, E10), and its zero eigenvalue
(multiplicity 5 at `(3, 1, 2)`) contributes nothing after five steps. Thus,
for `k ≥ 5`, `‖R_k^Q‖ / λ_1^k ≤ C |λ_2/λ_1|^k`, with `λ_2` drawn from
`Q`'s spectrum. This is a bound on the orbit-sector operator, not on the
full matrix `T` outside that sector. Applied to the two free-end factors,
with the row-coordinate conversion just given, it yields
`(A T^c)(ρ) (T^{n−1−c} 1)(ρ) / λ_1^{n−1} → const · A(ρ) ρ_1(ρ) · ρ_1(ρ)`.
The center-row law therefore converges to `w(ρ) ∝ A(ρ) ρ_1(ρ)^2`; its
free-end error is bounded by a constant times
`|λ_2/λ_1|^c + |λ_2/λ_1|^{n−1−c}`. The limit does not depend on
the records at the two ends of the strip: for any nonnegative nonzero boundary
vectors `b_L`, `b_R` (any exterior records on the first and last rows),
`b_L T^c / λ_1^c` and `T^{n−1−c} b_R / λ_1^{n−1−c}` converge in direction to
`A ρ_1` and `ρ_1` because their Perron components `b_L · ρ_1` and
`(A ρ_1) · b_R` are positive, so the deep-row law is `w` whatever the end
records. This arbitrary-boundary convergence uses the full positive matrix
`T` and F2, and asserts no rate from `Q`'s spectrum (executed with `P(e_y)`
records on both end rows at `n = 13`, E11). The same argument gives `w` as the law of row `i` of the one-sided strip
(rows indexed by `N`) as `i → ∞`, which is the object F5 compares with.

**F4 (exact enclosure, executed; `W = 3`, both triples; `W = 2` likewise).**
(a) The characteristic polynomial of `Q` at `(3, 1, 2)` is
`λ^5 (λ^3 − 7312 λ^2 + 2578432 λ − 221134848)` (E3, exact integers); at
`(5, 2, 4)` it is irreducible of degree 8:
`λ^8 − 185171 λ^7 + 1095911038 λ^6 − 1772274674784 λ^5 + 469450026668192 λ^4 + 67550038108063488 λ^3 − 17237755848001351680 λ^2 − 1439162188263618969600 λ − 14640126202850181120000`.
The Perron root's minimal polynomial is the cubic, respectively the octic;
an isolating interval from Sturm's theorem is bisected with exact rationals
to width below `10^{-30}`: `λ_1 = 6945.337824257111…` and
`λ_1 = 179107.428802830185…` (E4; the decimals are exact truncations of the
lower endpoints, labels only). (b) The Perron vector of `Q` is computed in
`Q(λ_1) = Q[λ]/(minimal polynomial)` by exact elimination with `x_0 = 1`;
`Q x = λ_1 x` holds on every row including the one dropped in the solve, and
every entry is positive on the isolating interval by rigorous interval
evaluation (E5). (c) The lift `ρ_1` satisfies `T ρ_1 = λ_1 ρ_1` and
`(Aρ_1)^T T = λ_1 (Aρ_1)^T` exactly in `Q(λ_1)` on all `216` rows (E6).
(d) `s_∞ = Σ_ρ A(ρ) ρ_1(ρ)^2 [ρ_0 = ρ_1] / Σ_ρ A(ρ) ρ_1(ρ)^2` is an element
of `Q(λ_1)`; its minimal polynomial is the irreducible factor of the
resultant `Res_λ(m(λ), y − g(λ))` (`s_∞ = g(λ_1)`) that has a root in the
enclosure; the enclosure is the rigorous interval image of the isolating
interval of `λ_1` under `g` (monotone powers, since `λ_1 > 0`), refined to
width below `10^{-30}`; exactly one real root of exactly one irreducible
factor lies in it (E7). At `(3, 1, 2)` the minimal polynomial of `s_∞` is
`2647547323586176 y^3 − 2190008305118016 y^2 + 544429860087294 y − 40261879885473`
and `s_∞ ∈ [0.2561109872857786908612, 0.2561109872857786908613]`; at
`(5, 2, 4)` it has degree 8 (coefficients of 120 digits, printed by the
runner's `--exact` flag) and `s_∞ ∈ [0.2199151616870197815075, 0.2199151616870197815076]`
(decimal endpoints rounded outward from the exact rationals). Neither
interval contains the formation value (`1/4`, `5/23`) (E8). At `W = 2`:
`s_∞ ∈ [0.255943088901618766, 0.255943088901618767]` (degree 2) and
`s_∞ ∈ [0.219874176124090031, 0.219874176124090032]` (degree 3), again
excluding `1/4` and `5/23`. (e) The finite-`n` center-row values (exact
rationals; decimals truncated): at `(3, 1, 2)`, `n = 3, 5, 7, 9, 11, 13`
give `0.2559429133, 0.2561061627, 0.2561108435, 0.2561109828, 0.2561109871, 0.2561109872`
(`n = 3` is `578647/2260844`); at `(5, 2, 4)`,
`0.2198741514, 0.2199144959, 0.2199151505, 0.2199151614, 0.2199151616, 0.2199151616`
(`n = 3` is `3731173618465/16969587349457`). Their distances to the
enclosure strictly decrease and the last is below `10^{-6}` (E9); this is an
executed fact for these `n`, not a theorem. (f) Second eigenvalue: every root of the characteristic polynomial
is real (Sturm count equals the degree of each irreducible factor); the
non-Perron roots are isolated to width `10^{-20}` and `m` is the largest
modulus of their interval endpoints; the count of roots in `[−m, m]` equals
the degree minus one, so every non-Perron eigenvalue has modulus at most the
rational `m < λ_1` (E10): `m ≤ 225.413932` and `|λ_2/λ_1| ≤ 0.0324554308`
at `(3, 1, 2)`; `m ≤ 3376.351458` and `|λ_2/λ_1| ≤ 0.0188509851` at
`(5, 2, 4)` (decimals rounded up from the exact rationals, which the runner
prints under `--exact`). At `W = 2`: `|λ_2/λ_1| ≤ 0.02534244` and
`≤ 0.01491179`. Nothing about the second eigenvalue remains numeric.

## The separation (F5)

On the infinite strip `S_3` (and `S_2`), at each declared triple and under
the records-only reading, the row-sweep formation law has row marginal `p_0`
on every row and nearest-neighbor pair-parallel probability exactly
`p/(p + q + 4r)` on every horizontal and vertical pair (Theorem E), while the
static law of the same strip has center-row law `w ∝ A ρ_1^2` with
pair-parallel probability `s_∞` in an exact rational interval that does not
contain `p/(p + q + 4r)` (Theorem F). The two laws differ on an infinite
window, and the difference is a fixed exact amount, not a finite-size
effect: along the sweep the normalizer history does not wash out. This is
the block's headline at infinite scope and it is a statement about the
declared strips only.

## No-Go Discipline Gate

The negative sentence "the normalizer history does not wash out along the
sweep on the infinite strip" (for the product rule at the declared triples,
under the records-only reading, on `S_2` and `S_3`) carries the gate. It is
an exact statement on the declared strips, a corollary of Theorems E and F at
their stated scope; it is not a route no-go beyond that scope.

### N1 — Routes by which the two laws could still agree on an infinite window

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a different order family on the strip | choose an order whose formation law has the static pair statistic | row sweeps with the rows formed in increasing or decreasing order, each row swept from either end, are covered by Theorem E (the strip reflection maps a right-to-left row onto a left-to-right one and `p_0` is reflection-invariant since `K` is symmetric), and column sweeps by the transposed argument; orders in which some site forms with recorded neighbors above and below, or with two recorded neighbors that have no common earlier neighbor, are not covered by E and are not executed here — the panel's exact grid survey (pack `REVIEW_HISTORY.md`) found the row law kept by diagonal sweeps and by the snake order and broken by a scrambled order and by the ends-inward path order; those are leads for the next block, not claims of this note | ATTEMPTED (row sweeps); not executed (diagonal, random) |
| 2 the static law of the plane | let the plane's static law, not the strip's, be the comparator | not computed; the formation side is width-independent (E4 for every `W`), so the comparison on the plane would need only the plane's pair statistic, which this note does not compute | not executed; obligation named |
| 3 a three-recorded-neighbor sweep | a sweep on a three-dimensional window whose normalizers telescope | Theorem E's premise (the two-neighbor normalizer is the two-step kernel of a common earlier neighbor) fails at three neighbors: the cube witness D8 (`210/216` triples off) | ATTEMPTED (witness only; no theorem) |
| 4 a different exhaustion for the infinite-volume limit | take the formation law along growing squares rather than strips | the formation side is exhaustion-independent: every row of every `W × n` strip has law `p_0` and every nearest-neighbor pair the single-edge law (E3, E4 for every `W`, `n`); the static side along squares is the plane (route 2) | ATTEMPTED (formation side); static side not computed |
| 5 the constant rule | `p = q = r` makes every normalizer constant | coincides trivially (D6) and is excluded by the named reading of the variation clause restricted to the menu (block 01, B4) | ATTEMPTED |
| 6 the marginal reading of block 01 | let the forming site use the static law's own conditional given all existing records | coincides by the chain rule but is window-dependent and non-local, so it is not one fixed nearest-neighbor rule (block 01, E6a/E6b, executed there; block 01 is unaudited, so this is upstream evidence, not retained authority) | ATTEMPTED (upstream block 01; not re-executed here) |

### N2 — Wall-independence audit

Walls: `W_R` (records-only reading), `W_var` (not all equal on the declared
menu), `W_pos` (positivity), `W_sym` (class (P): symmetric isotropic pair
weight, constant site weight), `W_ord` (the declared row sweep), `W_width`
(the static enclosure is executed at `W = 2, 3` only).

| pair | first closes second? | second closes first? | independent? | witnesses |
|---|---|---|---|---|
| `W_R`, `W_var` | no | no | yes | the constant rule under R-only coincides (D6); the `(3,1,2)` rule under the marginal reading coincides (block 01) |
| `W_sym`, any | no | no | yes | the asymmetric control breaks E3 on every row state (D7) while keeping the other walls |
| `W_ord`, `W_width` | no | no | yes | E holds for every width; F is executed at two widths |
| `W_pos`, `W_var` | no | no | yes | `(1,1,1)` is positive and constant; a zero pair weight makes `T` non-positive and F2 inapplicable |

No wall collapses into another; the headline uses all six as hypotheses.

### N3 — Hidden-wall scan

Scanned for "we assume", "by construction", "as is standard", "the framework
provides", "naturally", "obviously", "canonical", "registered", "background",
"bridge context". Hits: "registered" only in N6. The readings used are the
four named premises carried from block 01; the diagonal argument in C2 and
the compactness of cylinders are proved in the text; the convergence rate in
F3 uses the executed simplicity of the nonzero eigenvalues (E10). No wall was
promoted.

### N4 — Per-citation table

| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 01's note (proposed, unaudited) | finite windows: the formation law equals the static law iff every site forms with at most one recorded neighbor | the infinite strip; the definitions and Theorem B's path instance | yes (parent; re-executed where used: B4) |
| `classical: sequential lattice processes with Markov-chain invariant row measures` | product-form invariant measures for certain sequential updates | none (reference only; E is proved here) | no; not a witness |
| Perron–Frobenius (classical) | the dominant eigenvalue of a positive matrix | re-proved at scope (F2) | yes (re-proved) |
| compactness of a countable product of finite sets (classical) | existence of a limit measure | re-proved at scope (C2) | yes (re-proved) |

After dropping the non-match, the headline rests on this note's own exact
witnesses, Theorems E and F, which is what it needs.

### N5 — Resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "the normalizer history does not wash out along the sweep on the infinite strip" | executed: every row state at `W = 2, 3, 4`, every pair, both triples | executed: every column's vertical and horizontal pair; every sub-window site class of the cube and plaquette | executed: `Q`'s spectrum exactly (Perron root, vector, second-eigenvalue bound) | executed: the row kernel block by block; the finite-`n` center rows `n ≤ 13`; the cube witness | checked and not executed: strips only; the plane and `Z^3` uniqueness are named, not computed |

The runner prints matching `per_element:` … `lattice_wide:` lines. The
narrowest form is used: "on the declared strips at the declared triples".

### N6 — Partial-closure paths and primitive scan

The registered approved primitives in `docs/audit/data/axiom_premise_nodes.json`
(`scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`) supply a length reference, a graining ratio and a
realized-state notion; none supplies a formation order, a reading of a
partially recorded neighborhood or a pair weight, and none is a wall here.
Reframing paths: (i) the marginal reading (route 6) makes the two laws
coincide by convention at the price of a window-dependent non-local rule;
(ii) `docs/repo/DEFERRED_DECISIONS.md` entry 1 wakes on the committed-action
identification, which this note does not supply (strips, not the lattice).
No path removes the separation without changing the reading; this note does
not say a new axiom is required.

### N7 — Steelman

Hostile reviewer: "A strip is not the lattice. On `Z^3` any sweep reaching
the bulk forms sites with three recorded neighbors, where Theorem E does not
apply; the static specification there may have a unique infinite-volume law
that some physical process — not a total order, perhaps a continuous-time
process with the static law as its stationary measure — reproduces. The strip
separation is an artifact of a two-dimensional window and a declared order."
The gap in each: the three-neighbor case is exactly what this note does not
claim (the cube witness shows E's premise fails there, nothing more);
uniqueness on `Z^3` is the next block's object, asserted in neither direction;
a continuous-time process needs a rate supply the axioms do not give (block
01, N7). The steelman defeats any claim about the lattice, which this note
does not make; it does not defeat the exact separation on the declared
strips, a theorem about an infinite window of the lattice.

### N8 — Cross-cycle echo

| similar prior wall | retired? | mechanism | applies here? |
|---|---|---|---|
| block 01's finite-window separation (every plaquette) | no (proposed) | none | extended here to an infinite window; the finite fact is the induction base |
| block 01's N7 "the limit could wash out the normalizer history" | addressed here at strip scope | Theorem E (exact invariance) and Theorem F (exact enclosure) | yes — the mechanism is this note; the lattice version remains open |
| the `WILSON_STAGGERED_*` contraction controls (2026-07-12) | not walls of this lane | contraction-coefficient bounds on a different carrier | not here; relevant to the next block's uniqueness question only |

No structurally similar wall was retired by a mechanism not considered here.

**Gate result:** PASS for the strip separation as a corollary of Theorems E
and F at their scope; not shipped for any claim about the plane, about `Z^3`
uniqueness, about three-neighbor sweeps, or about which order is physical.

## Falsifiers

The theorems fail if any of these finite statements fails: `K` not symmetric
or not doubly stochastic; `Z_2 ≠ Z_1^2 K^2` for some pair; the path chain
differs from the end-swept path formation law; a sub-window conditional on
the cube or plaquette differs from the sub-window law with adjacent records;
the row kernel formula differs from the definition; `p_0 P ≠ p_0` at some
width in `{2, 3, 4}`; a nearest-neighbor pair without the law `(1/6) K`; the
direct finite-strip law differs from `p_0 P^{n−1}`; the constant rule not
uniform; the asymmetric control invariant; the cube witness proportional to
`Z_3`; orbit counts other than `3` and `8`; `T` not commuting with `G`; the
`(3, 1, 2)` characteristic polynomial other than the displayed one;
`Qx ≠ λ_1 x` or a non-positive entry of `x`; the lift not an eigenvector of
`T`; the enclosure of `s_∞` without exactly one root of the minimal
polynomial, or containing `p/(p + q + 4r)`; the finite-`n` sequence not
approaching the enclosure; a non-Perron root of modulus above `m`.

## Boundaries and non-claims

This note selects no physical formation order; the row sweep is a declared order whose exact solvability is a property of sweeps in which each site forms with one in-row predecessor and the site below it as its recorded neighbors, on two-dimensional windows with an unrecorded exterior.

No statement is made about the static law of the plane, about uniqueness of an infinite-volume static law on the cubic lattice, or about any three-recorded-neighbor sweep; this note does not fire wake condition 1 of the parked statistical-bridge decision.

This note does not derive, explain, bear on or decide the parked statistical bridge, the Born form, or the gravity lane's action.

Every negative sentence in this note is an exact statement on the declared strips and windows or a corollary of Theorems E and F at their stated scope; none is a route no-go beyond that scope.

Further: the infinite strip and the quadrant have rows indexed by `N` (a
first row exists; the formation law is defined without any limit); the
exactly solvable order class is the one in the first fence, not every order
with at most two recorded neighbors (the ends-inward path order of block 01
has two recorded neighbors at its last site and its formation law is not the
path chain); Theorem C2 is existence only, along a subsequence, for the finite
menu; whether different exhaustions or boundary records give the same limit
is undecided here; the static enclosure is executed at widths 2 and 3 only;
the finite-`n` monotonicity is an executed fact for `n ≤ 13`; the convergence
ratio is `Q`'s on the orbit sector; no formation site, probability or rate
is supplied; no axiom or primitive is changed.

## Imports

References, re-proved at scope, never authority, no values imported:
Perron–Frobenius for positive matrices (Wielandt's maximin argument, F2);
the Carathéodory extension theorem (cited, not re-proved; used in C2 only as
the definition-level passage from the cylinder algebra to the product
σ-algebra);
compactness of a countable product of finite sets and the passage of
finite-window conditional identities to the limit (C2); Sturm's theorem and
resultants as implemented in `sympy` (exact rational arithmetic; the runner
checks each root count and each residual itself); the classical observation
on sequential lattice processes, reference only. Declared mathematical
scaffolding: the exact weight triples, the exterior assignments of block 01,
the cube index order `0..7` for the witness, the strip widths and lengths.
No observation, fitted value or literature constant enters.

## Review record

Fable primary seat (own 28-mutation census, read from raw per-mutation
stdout; two checks and two mutations added by the supervisor at the fold, D9
and E11, census re-run at 30); a hostile refuter lens on the contract before
the build (Opus 5; exact order survey on finite grids; the fence's order class
and the transitivity sentence corrected on its findings); refuting checker
(Opus 5, disjoint machinery): FIX FIRST with nothing refuted — CK-01 to CK-08 all confirmed with the numbers reproduced independently (a different menu encoding, base-6 row codes, the kernel from the definition, its own orbit reduction, elimination over `Q(λ)` with exact interval evaluation instead of a resultant; all 28 mutations run, each in its family; an undeclared opposite-corner sub-window of the cube also consistent); its two required fixes (the route-1 order class, with its own counterexample: row order `0, 2, 1` at width 3 gives row 1 three recorded neighbors and a marginal off `p_0` on all 216 states; the Carathéodory extension named as a cited import) and its recommendations (metrizability; the obligation table's choice wording; the quadrant named in the claim scope) folded here; supervisor line-by-line review of
the runner and the note with three exact control scripts. Independence class:
single family (Claude), cross-model. Contract facts settled while executing: the second eigenvalue at
`(5, 2, 4)`, left numeric in the contract, is exact by Sturm isolation since
every root of the octic is real; the contract's `next_trace_action` named the
uniqueness region by a proper name the fence list forbids, so the region is
described instead; width 4 fits the budget (0.5 s per triple). The
supervisor's control numbers were reproduced in the seat's own code before
any theorem sentence was written.

## Verification

```bash
python3 scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py
python3 scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py --list-mutations
python3 scripts/admissibility_rule_infinite_strip_row_sweep_formation_versus_static_law_2026_09_06.py --mutation invariance_forced_true
```

Families: A authority and inputs; B the kernel; C the specification; D the
sweep; E the static infinite strip; F fences and the floating-point
self-scan; G the resolution certificate. Each of the 30 declared mutations
perturbs one object at construction time and fails in exactly one family
(`mutation_family_expected:` / `mutation_family_observed:` lines); `--exact`
prints the exact rational endpoints and polynomials. Expected final line:
`TOTAL: PASS=39 FAIL=0`.

## Source-review corrigendum — 2026-09-07

Corrected the compact-image normalization and independent-eigenvector step in F2. F3 now distinguishes orbit masses from per-entry row coordinates and restricts the quotient spectral rate to the orbit sector; arbitrary-boundary convergence uses the full positive transfer matrix without a quotient rate. The exterior product contains adjacent edges only. No algebraic value changed.

The earlier review record is preserved as history. These corrections amend the
current source claims; they do not apply audit status. The packet
`REVIEW_HISTORY.md` records the finding-to-change map and original source head.
