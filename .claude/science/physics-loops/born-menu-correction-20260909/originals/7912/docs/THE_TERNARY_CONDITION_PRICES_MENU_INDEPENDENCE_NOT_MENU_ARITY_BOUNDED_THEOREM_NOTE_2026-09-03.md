---
claim_id: ternary_condition_prices_menu_independence_not_arity
claim_type: bounded_theorem
claim_scope: "Exact finite algebra at one site. Among gradings whose value depends on the effect alone, normalization on the declared ternary scaled-projector menus removes every exhibited nonlinear candidate with exact rational witnesses, and an exact rational rank certificate at polynomial degree five leaves nullity three, spanned by the linear Born modes, with and without the binary oddness restriction. Among gradings whose value may depend on the menu, the uniform law and the amplitude-power laws are normalized on every declared menu of arity two and three on both a qubit and a qutrit carrier, and are separated from the Born form only by effect functionality and by the merge rule. The five Cycle-984 laws are per-atom counting weights on a declared world table with no projector or state argument. No axiom is changed, no axiom-side Born forcing is claimed, and the dimension-three frame-function theorem is named as context, not recomputed."
upstream_dependencies:
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
  - born_compatibility_z3_adjacency_cycle984_note_2026-08-11
runner: scripts/ternary_condition_prices_menu_independence_check_2026_09_03.py
---

# The Ternary Condition Prices Menu-Independence, Not Menu Arity

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status authority:** independent audit only. This note authors no audit
verdict and changes no axiom, primitive, registry, queue, or policy.
**Primary runner:**
[`scripts/ternary_condition_prices_menu_independence_check_2026_09_03.py`](../scripts/ternary_condition_prices_menu_independence_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/ternary_condition_prices_menu_independence_check_2026_09_03.txt`](../logs/runner-cache/ternary_condition_prices_menu_independence_check_2026_09_03.txt)
**Parents:**
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
and [`BORN_COMPATIBILITY_Z3_ADJACENCY_CYCLE984_NOTE_2026-08-11.md`](BORN_COMPATIBILITY_Z3_ADJACENCY_CYCLE984_NOTE_2026-08-11.md).

## Result Up Front

The 2026-08-09 note derives the Born trace form at one site from two
conditional clauses that it presents as symmetric: effect functionality
(menu-independence) and low-arity eligibility (normalization on every binary
and ternary scaled resolution). This note narrows that pair. The two clauses
are not of equal discriminating cost.

Among gradings that already depend on the effect alone, the ternary condition is
decisive: four independent candidates that pass every declared binary menu fail a
ternary menu at exactly `5/4`, `21/16`, `13/8` and `29/32`, and an exact rational
rank certificate at degree five leaves nullity exactly three, spanned by the
linear Born modes.

Among gradings whose value may depend on the menu, the ternary condition removes
nothing. The uniform law and the amplitude-power family are normalized on every
declared menu of arity two and three, on a qubit and on a qutrit carrier, and are
separated from the Born form only by effect functionality and the merge rule.

The five Cycle-984 weighting survivors sit on the second side of that split
only degenerately: they are per-atom counting weights on a world table, with no
projector and no state argument, and their test family has no menu arity.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "The finite algebra is exact at the stated degrees and menus, but the discriminating statements are about a supplied grading family and a supplied menu family; neither is derived from the four axioms here, and the dimension-three frame-function theorem is named as context."
trace_class: upstream_support
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Attack effect functionality directly: derive, from Record and Admissibility, that a registered outcome carries one grade independent of the menu it sits in."
conditional_surface_status: "exact finite algebra conditional on a supplied grading family, a supplied menu family, and stated polynomial degree"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

Work at one site of the physical lattice, with `H = C^2`. For a unit vector
`n in R^3`, write `P(n) = (I + n dot sigma)/2`, and take the 2026-08-09 scaled
domain

`S = {c P(n) : 0 <= c <= 1, |n| = 1} union {c I : 0 <= c <= 1}`.

A menu is a finite family of nonzero members of `S` summing to `I`. A **grading**
assigns each member of a menu a value in `[0,1]`; it is **menu-independent** when
that value depends on the effect alone, and **menu-dependent** when the same
effect may take different values in different menus. Records register: only
records are readable, and the canonical Record axiom fixes that "a readout value
is determined by record content alone."

The runner checks the declared menu structure symbolically:
`c P(n) + a I = I` holds exactly when `c n = 0` and `c + 2a = 2`. Hence the
declared binary rank-one menus are antipodal pairs at `c = 1`, the declared
ternary rank-one menus are trines with `sum_k c_k = 2` and
`sum_k c_k n_k = 0`, and the coin menus are the scalar-identity families. The
declared menus are `BIN_z`, `BIN_x`, `BIN_tilt`, the Fourier trine
`TER_fourier` at coefficient `2/3`, the planar isosceles trine `TER_isosceles`
at `(3/4, 5/8, 5/8)`, its exact rational rotation `TER_iso_rotated`, the
collinear `TER_degenerate = {P(e_z), (1/2)P(-e_z), (1/2)P(-e_z)}`, and coins at
`1/3`, `1/2`, `{1/4,1/4,1/2}` and `{1/6,1/3,1/2}`.

## The 2026-08-09 Note's Two Clauses

That note states three inputs: **effect functionality** (the value depends on the
effect, not on a menu containing it), **low-arity eligibility** (every two- and
three-member menu is normalized), and the **standard frame theorem** in dimension
three, named as an explicit import. From these it derives a unique density matrix
with `w(E) = Tr(rho E)` on all of `S`. Its own N2 table records the first two as
"two independent conditional clauses" — independent, with no cost distinction
drawn between them. That is the reading this note narrows.

## The Cycle-984 Survivors, And Why The Briefed Retest Does Not Apply

The Cycle-984 note carries five weighting survivors. Their declared numerators
in world `w` are `1`, `D/N_w`, `o(w) D/N_w`, `(180225 - f(w)) D/N_w` when
formed, and `f(w) D/N_w` when formed, with `N_w` the event count of the world,
`D = 1,073,280`, `o(w)` the clean-dwell occupation and `f(w)` the formation
moment. Every argument is a world-level substrate variable. There is no
argument of type projector and none of type state, so none of the five has a
value on a menu of effects.

The Cycle-984 conditional test is likewise arity-free. It compares a
factorized joint `p_i(e) mu_p(x) q(n) 1{y = L_g(x,n)}` against an event
marginal, and the note states its own verdict directly:

> "This factorization is exactly why survival is nondiscrimination rather than
> Born compatibility: every nonnegative normalized `p_i` would pass the event-
> marginal step, regardless of its detailed event weights."

So the briefed retest — enlarge the menu family from binary to ternary and see
whether the survivors are discriminated — does not apply to that family. The
family has no menus, and enlarging a menu condition cannot change a test that
is satisfied by every normalized event law. The question that does typecheck is
the substituted one: on the 2026-08-09 domain, does the ternary condition
discriminate non-Born *gradings*? The answer splits by which of the two clauses
is in force, and that split is T3 against T4.

## T1 — The Parent Reproduces, And Its Clauses Are Symmetric As Written

The 2026-08-09 runner re-executes on its repository inputs and prints
`TOTAL: PASS=16 FAIL=0`. Its three assumptions and its derived form are read
back out of the parent note verbatim. This runner independently regrades the
parent's own hostile control — the smooth binary cubic grading on the Fourier
trine — and also gets exactly `5/4`.

## T2 — The Cycle-984 Laws Are Counting Measures On Event Atoms

The five numerator formulas are recomputed as typed laws on a declared exact
world table. Two worlds are declared to agree in every event-level datum and to
differ only in `o(w)` and `f(w)`.

- `M1` gives every atom the same weight; `M2` is constant within each world and
  gives every world the same total. Neither separates the two worlds. Read on a
  single menu, each supports the uniform law `w(E_k) = 1/|menu|`, which is
  menu-dependent; no menu-independent reading of either is exhibited here.
- `M3`, `M4` and `M5` do separate those two worlds. A function of the effect
  alone cannot reproduce a weight that separates atoms agreeing in every
  event-level datum, so these three admit no effect-side lift at all.
- The declared product joint marginalizes to `p(e)` identically for a generic
  nonnegative normalized event law. The test is vacuous by the note's own
  sentence, at every arity, because it has none.

This is a typed reconstruction of the declared formulas: it does not reload the
748-world receipt of the Cycle-984 note or bear on its own certificates.

## T3 — Among Menu-Independent Gradings, Ternary Discriminates

Every candidate here has range in `[0,1]`, sends `0` to `0` and `I` to `1`, and
depends on the effect alone.

| grading | rank-one branch | binary | first ternary witness |
|---|---|---|---|
| `W_BORN[r=0]`, `W_BORN[r=(3/5,0,4/5)]` | `c(1 + r.n)/2` | pass | normalized on all |
| `W_CUBIC` | `c(1 + n_z^3)/2` | pass | `TER_fourier = 5/4` |
| `W_QUINTIC` | `c(1 + n_z^5)/2` | pass | `TER_fourier = 21/16` |
| `W_HARM3` | `c(1 + P_3(n_z))/2` | pass | `TER_fourier = 13/8` |
| `W_COINWOBBLE` | `c/2`; coin `c + c(1-c)(c-1/2)` | pass | `COIN_ter_1/4 = 29/32` |
| `W_CSQUARE` | `c^2/2` | fails `COIN_bin_1/2 = 1/2` | — |

`W_COINWOBBLE` is normalized on every rank-one menu, binary and ternary, and on
every binary coin menu; it fails ternary coins at `29/32` and `11/12`, so the
coin branch of the ternary condition carries weight no rank-one menu carries.
`W_CSQUARE` is the converse control: a binary coin menu already removes it.

The rank certificate makes the survivor set exact. Take
`w(c P(n)) = c(1 + f(n))/2` with `f` a sphere polynomial in normal form
`f = A(x,y) + z B(x,y)`. The ternary condition on a menu `{(c_k, n_k)}` reduces
to `sum_k c_k f(n_k) = 0`. Rotating the `(3/4, 5/8, 5/8)` menu by exact
rational quaternion rotations gives, by exact rational elimination:

| ansatz | columns | rows | rank | nullity | kernel |
|---|---:|---:|---:|---:|---|
| `A` odd, `B` even, degree `<= 5` (binary imposed) | 21 | 45 | 18 | 3 | `x`, `y`, `z` |
| `A`, `B` unrestricted, degree `<= 5` | 36 | 120 | 33 | 3 | `x`, `y`, `z` |

In both cases the nullity is exactly three and the three linear modes annihilate
every ternary row, so the kernel is exactly their span: the surviving gradings
are `f(n) = r.n`, that is `w(c P(n)) = Tr(rho, c P(n))`. The second row is the
sharper one — through degree five, on this orbit, the ternary constraints alone
already leave the Born modes and nothing else, without the binary oddness
restriction. Binary stays load-bearing for the parent's frame lift, where a
lifted basis containing the pure ancilla vector compresses to a binary menu,
and for the coin branch.

On a genuine qutrit the same condition has a plain name. The menu-independent
quartic deformation `Tr(rho P) + lambda (Tr(Delta(P)^2) - Tr(P)/3)` at
`lambda = 1/10` gives `6/5`, `46/45` and `3462/3125` on three of the four
declared bases. The condition violated there is the `d = 3` frame-function
condition: a nonnegative function on rank-one projectors of `C^3` summing to
one on every orthonormal basis. That is a pointer to the standard theorem the
parent note already imports, and this note imports it the same way, as context
rather than authority. Nothing here re-proves it.

## T4 — Menu-Dependent Gradings Are Untouched By Arity

Let `W_UNIFORM(E_k; menu) = 1/|menu|` — the effect-side reading of `M1` and `M2`
from T2 — and let `W_POWER[p](E_k; menu, rho) = Tr(rho E_k)^{p/2} / sum_j
Tr(rho E_j)^{p/2}`.

Both are normalized on every declared qubit menu, binary and ternary, and on all
four qutrit bases and all four rank-two-plus-rank-one qutrit menus. Normalization
holds at every arity by construction for any renormalized law, so no menu
condition of any arity separates them from the Born form.

Two conditions do, with exact witnesses. **Effect functionality:** the same
effect `P(e_z)` sits in `BIN_z` and in `TER_degenerate`, and is graded `1/2`
then `1/3` by the uniform law, and `16/17` then `32/33` by `W_POWER[p=4]` at
Bloch `(0,0,3/5)`. The Born grading gives `4/5` in both. **The merge rule
`w(E_1 + E_2) = w(E_1) + w(E_2)`:** on the qubit merge the uniform law gives
`1/2` against `2/3` and the power law `1/17` against `1/33`, while Born gives
`1/5` on both sides; on the qutrit merge with `rho = diag(1/2, 1/3, 1/6)` the
uniform law gives `1/2` against `2/3` and the power law `25/26` against
`13/14`, while Born gives `5/6` on both sides.

## T5 — A Planar Ternary Menu Is Blind

`TER_isosceles` has all three Bloch directions in one plane, and grades
`W_CUBIC`, `W_QUINTIC` and `W_HARM3` at exactly `1` — it sees none of them. One
exact rational rotation out of that plane restores discrimination, giving
`221/225`, `50209/50625` and `43/45`. The qutrit side shows the same effect:
the quartic deformation of T3 is exactly `1` on the Fourier basis.

## Corollary

1. The survivors of the earlier cycle are not effect gradings, and their test
   family had no menus, so no menu condition can discriminate them. That row
   carries no evidence about the Born form either way.
2. Among menu-independent gradings, the ternary condition leaves exactly the
   Born linear modes at the stated degree, on the stated orbit, with exact
   rational witnesses for every candidate removed.
3. Menu-dependent gradings are untouched by arity. They die only under
   menu-independence and the merge rule.
4. Therefore the readout price sits in the menu-independence clause: once a
   record's odds depend on the effect alone and not on the menu it sits in,
   the Born form follows, and that clause is what the axioms do not supply.
   The parent's two clauses are not symmetric in cost.
5. A practical warning for any successor runner: a ternary menu whose
   directions lie in a plane is blind. Ternary menus must be rotated.

## Reading, Not Theorem

The rule that a record's odds must add up over any three-way choice does cut
down the candidates, but only among rules that already give an outcome the
same odds whatever else was on offer. Rules that let the odds depend on the
list of alternatives pass every such test and fall only to the requirement
that they must not. So the thing the framework has not yet supplied is that
requirement itself: that what a record registers depends on the outcome and
not on the menu.

## Interfaces

- **Menu eligibility under Admissibility.** Whether the fixed nearest-neighbor
  admissibility rule registers ternary scaled resolutions as local menus is a
  separate open question, untouched here.
- **Degree above five.** This certificate is exact rational at degree five on
  one radius profile; the parent runner's modular certificate reaches degree
  nine at two radii. Neither reaches all modes, and the general step is the
  named frame theorem.
- **The formation rate.** The canonical Admissibility reading note says the
  distribution "does not supply the formation site, probability, or rate", and
  nothing here bears on record-formation site, weight, or rate.

## Proof Boundary

What is proved is exact finite algebra at the stated degrees and on the declared
menus: the parent reproduction, the typed reconstruction of the five Cycle-984
numerators on a declared world table, the binary-versus-ternary tables with
exact rational witnesses, the two rank certificates at degree five, the
normalization of the menu-dependent laws on every declared menu, the
functionality and merge witnesses, and the planar-menu blindness.

What is not proved: any axiom-side Born forcing; the dimension-three
frame-function theorem, named as context and not recomputed; menu eligibility
under Admissibility; `c`-linearity of the grading independently of the parent's
frame lift, which the rank ansatz assumes and the coin menus test only on the
scalar branch; polynomial degree above five; any recomputation of the Cycle-984
748-world receipt; and anything about record-formation site, weight, or rate.

The candidate families are declared, not complete: no claim is made about
menu-independent gradings outside the stated polynomial degree, nor that the
two conditions named in T4 are the only separators of the menu-dependent laws.

## Axiom-Text Boundary

Corollary 4 is a statement about the canonical wording, not a non-derivability
claim. [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) gives the
one-site `M_2(C)` presentation, a nearest-neighbor-determined probability
distribution over local possibilities, and a readout value determined by record
content alone. It does not state that a registered effect carries one grade
across the different menus it can sit in. Whether Record dynamics, an
operational-equivalence theorem, or a physical registration construction derives
that clause remains open, and is the constructive successor this note points at.
No no-go is asserted, no derivation route is ruled out, and
no canonical axiom edit is proposed here.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| `M_2(C)` one-site presentation | carrier context | Qubit axiom | supplied algebraic presentation |
| scaled domain `S` and its menus | declared family | 2026-08-09 parent note | physical eligibility remains open |
| declared grading families | theorem premise | explicit in this note | not derived from the axioms |
| dimension-three frame-function theorem | context pointer | named in the parent note | not recomputed here |
| Cycle-984 numerators and test | quoted source | Cycle-984 note, verbatim | typed reconstruction only |
| observations, fits, target probabilities | none | not used | not applicable |

## Review Record

This note narrows the parent's symmetric presentation of its two clauses into an
asymmetry with exact witnesses on both sides, and reclassifies the Cycle-984 row
as a type mismatch rather than a discrimination failure. It does not advance
current-surface physical Born closure. The exactly-three-only surface, menu
occurrence, degree above five, the neighbor-to-density law, and record-formation
site, weight and rate are not classified. Independent audit remains required
before the repository may assign any effective claim status.
