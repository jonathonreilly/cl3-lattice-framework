---
claim_id: menu_independence_independent_insufficient_born_needs_abundance
claim_type: bounded_theorem
claim_scope: "Exact finite algebra plus one finite emergent model. (i) An explicit fixed nearest-neighbour rule on Z^3 with a seven-symbol cubic-covariant record alphabet carries four normalized covariant odds rules, one menu-independent and three menu-dependent, on the same law; menu-independence is therefore not a consequence of Lattice, Qubit, Admissibility and Record. (ii) With menu-independence in force, exact rational rank certificates at polynomial degree five show the Born form follows only when every binary and every non-collinear rank-one ternary resolution occurs as a support; singleton-only, binary-only, binary-plus-mixed-ternary and any finite menu family each leave an explicit normalized non-Born grading. The narrow no-go clause is exactly: a nearest-neighbour law with a finite record alphabet cannot supply menu abundance. (iii) On the emergent 2x2x2 cube the conditional record odds take five values on one binary menu at three prior records and are forced only from eight, so a single universal grading is false there. No axiom is changed, no axiom-side Born forcing is claimed, and the dimension-three frame-function theorem is named as context, not recomputed."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/menu_independence_independent_and_insufficient_check_2026_09_03.py
---

# Menu-Independence Is Independent Of The Axioms And Insufficient With Them: The Born Form Needs Menu Abundance

**Date:** 2026-09-03
**Type:** bounded_theorem, carrying one narrow no-go clause
**Audit:** unset; independent audit remains a separate lane
**Status authority:** independent audit only. This note authors no audit
verdict and changes no axiom, primitive, registry, queue, or policy.
**Primary runner:**
[`scripts/menu_independence_independent_and_insufficient_check_2026_09_03.py`](../scripts/menu_independence_independent_and_insufficient_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/menu_independence_independent_and_insufficient_check_2026_09_03.txt`](../logs/runner-cache/menu_independence_independent_and_insufficient_check_2026_09_03.txt)
**Parent:**
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md).
The immediate predecessor is the sibling branch note *The Ternary Condition Prices
Menu-Independence, Not Menu Arity* (PR #7912), whose closing claim this note
corrects; the cube reading here corrects PR #7895.

## Result Up Front

The 2026-08-09 note derives the Born trace form at one site from two conditional
clauses its own N2 table calls "two independent conditional clauses" — **effect
functionality**, that a possibility's odds depend on the effect and not on the menu
containing it, and **low-arity eligibility**, that every binary and ternary scaled
resolution is a normalized menu — plus the named dimension-three frame theorem. PR
#7912 closed by placing the whole readout price in the first: "once a record's odds
depend on the effect alone and not on the menu it sits in, the Born form follows,
and that clause is what the axioms do not supply." Is menu-independence implied by
the axioms, and is it that one clause?

Half of that is confirmed and half corrected. Menu-independence is genuinely
independent of the four axioms: an explicit fixed nearest-neighbour rule on `Z^3`,
covariant over all 117649 neighbourhood patterns and all 24 proper cubic rotations,
carries the Born odds rule and three menu-dependent odds rules side by side, all
normalized on all 166 menus it realises. But it is not the one clause. With it in
force the Born form still needs **menu abundance** — every binary and every
non-collinear rank-one ternary resolution occurring as the support of some condition
— and the narrow no-go clause proved here is exactly that **a nearest-neighbour law
with a finite record alphabet cannot supply menu abundance**. The emergent cube then
removes the option of reading clause (i) as one universal grading: its conditional
record odds take five distinct values on one and the same binary menu.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "The finite algebra is exact at the stated degrees and on the declared menus, and the narrow no-go clause is a counting statement about finite-alphabet nearest-neighbour laws. The positive Born direction still rests on a supplied grading clause, a supplied menu family, and the named dimension-three frame-function theorem."
trace_class: upstream_support
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Attack menu abundance directly: derive, or physically register, a condition family whose supports include the non-collinear rank-one ternary resolutions, which a finite record alphabet on six neighbours cannot enumerate."
conditional_surface_status: "exact finite algebra conditional on a supplied grading family, declared menus, and stated polynomial degree; one finite emergent model at float64 precision"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

Work at one site of the physical lattice, with `H = C^2`. For a unit vector `n in
R^3` write `P(n) = (I + n dot sigma)/2`, and take the 2026-08-09 scaled domain `S =
{c P(n) : 0 <= c <= 1, |n| = 1} union {c I : 0 <= c <= 1}`. A
**menu** is a finite family of nonzero members of `S` summing to `I`.
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
objects: Admissibility gives one fixed nearest-neighbour rule, covariant under
lattice translations and proper cubic rotations, under which for each site "the
probability distribution over the possibilities is determined by, and varies with,
the nearest-neighbor conditions", and its reading note (3) says that distribution is
a probability measure on the local possibility domain whose support is what
`"available"/"admissible"` denotes — so the menu of a condition `n` is exactly `M(n)
= supp p_n`. Record says that when present "a record locks exactly one admissible
local possibility" and that "only records are readable". Records register; the
needles are the record contents on the six nearest neighbours. A **law** is the map
`n |-> p_n`, and **menu-independence** is the property that for all conditions `n,
n'` and every `v` in `M(n) intersect M(n')`, `p_n(v) = p_{n'}(v)`. The runner
classifies the menus on `S` exactly: `c P(u) + a I = I` forces `c u = 0`, so binary
rank-one menus are antipodal pairs at `c = 1`, rank-one ternary menus are trines
with `sum_k c_k = 2` and `sum_k c_k n_k = 0`, coin menus are the scalar-identity
families, and a fourth family the 2026-08-09 classification does not list appears
below: the **mixed ternary** `{c P(u), c P(-u), (1 - c) I}`.

## T1 — Menu-Independence Is Independent Of The Four Axioms

**The witness law `L_MENU`.** The record alphabet is finite and cubic-covariant:
blank, or `P(m)` with `m` one of the six `+-e_x, +-e_y, +-e_z` — seven symbols per
neighbour, so `7^6 = 117649` conditions. Write `V(n)` for the sum of the recorded
neighbour Bloch directions and `k(n)` for the number of records: `k = 0` gives
`{I}`; `V != 0` with `k` odd gives the binary rank-one `{P(u), P(-u)}` at `u =
V/|V|`; `V != 0` with `k` even gives the mixed ternary `{(2/3) P(u), (2/3) P(-u),
(1/3) I}`; and `V = 0` with `k >= 1` gives the coin `{(1/3) I, (2/3) I}`. `V` is
equivariant and `k` invariant, so the menu map is covariant; it reads only the six
neighbour symbols, so it is nearest-neighbour determined; and every realised menu
resolves `I` exactly. The runner checks `M(g.n) = g.M(n)` over **all `7^6` patterns
times all 24 proper cubic rotations — 2823576 pairs, zero mismatches** — and again
as an exact family of possibilities on 48000 deterministic pattern-rotation pairs.
On a `3^3` torus with 400 deterministic record configurations, translation
covariance holds over 291600 checks and rotation covariance about the origin over
259200, both with zero mismatches.

**Four odds rules on the same law.** `BORN` with `w(E) = tr(E)/2` (the state
`I/2`, the unique cubic-invariant one), `UNIFORM` with `p(E) = 1/|M(n)|`, and `POWER
q` with `p(E) = tr(E)^q / sum_j tr(E_j)^q` at `q = 2, 3`. All four are exactly
normalized on all **166** menus the law realises, and all four are covariant. Each
is a legitimate model of the four axioms: one fixed covariant nearest-neighbour rule
with a per-site distribution determined by and varying with the neighbour records,
out of whose support a record locks one possibility.

**The discriminator.** Of the 331 possibilities the law realises, exactly one
sits in more than one menu: `(1/3) I`. Take `n1` with `P(+e_z)` recorded at both
`+e_x` and `-e_x` (`k = 2`, `V = (0,0,2)`, menu `{(2/3) P(e_z), (2/3) P(-e_z), (1/3)
I}`), against `n2` with `P(+e_z)` at `+e_x` and `P(-e_z)` at `-e_x` (`k = 2`, `V =
0`, menu `{(1/3) I, (2/3) I}`).

On that pair `(1/3) I` gets `1/3` against `1/3` under `BORN` — menu-independent —
and `1/3` against `1/2` under `UNIFORM`, `1/3` against `1/5` under `POWER q=2` and
`1/3` against `1/9` under `POWER q=3`, all menu-dependent. So `L_MENU` with
`UNIFORM` is a model of the four axioms in which menu-independence is false, and
with `BORN` one in which it is true. **Menu-independence is independent of the four
axioms** — an added clause, not a theorem. That much of PR #7912's reading stands,
now at the level of a lattice law.

## T2 — With The Clause, The Born Form Still Needs Menu Abundance

Take the polynomial sector `w(c P(u)) = c(1 + f(u))/2` with `f` in the normal form
`A(x,y) + z B(x,y)` of degree at most five: 36 coefficients, of which the binary
condition `f(u) + f(-u) = 0` retains 21. Ranks below are exact rational
eliminations; the largest matrix is 96 by 36.

| supports supplied | menu-independent | Born form | exact witness |
|---|---|---|---|
| singletons only | yes, trivially | **no** | normalization gives `w(v) = 1`; `tr(rho P(n)) = 1` forces `r = n`, and `r = e_z` with `r = e_x` is infeasible |
| binary only | yes | **no** | `f(u) = u_z^3` is odd, so it passes every binary rank-one and coin menu; it is not a trace form, `f(3/5,0,4/5) = 64/125` against `4/5` |
| binary plus mixed ternary | yes | **no** | the mixed ternary normalizes to `(c/2)(f(u) + f(-u))`, **exactly the binary condition**; all 72 mixed-ternary rows vanish identically, nullity **21**, not 3 |
| one cubic orbit of a rank-one ternary | yes | **no** | 24 rows, 21 columns, rank 6, nullity **15**, with the explicit survivor below |
| the full family | yes | **yes** | 96 rows, rank 18 on 21 columns and rank 33 on 36 columns, nullity **exactly 3**, kernel `span{x, y, z}` |

**The explicit survivor.** For the isosceles trine
`{(3/4) P(e_x), (5/8) P(-3/5, 4/5, 0), (5/8) P(-3/5, -4/5, 0)}` and all 24 of its
proper-cubic images, `f = -34/59 y^3 + 25/59 y^5` has residual exactly `0`, is odd,
and has coefficients of absolute sum exactly `1`, so `|f| <= 1` on the sphere and
`w` has range in `[0,1]`: a menu-independent, normalized, **non-Born** grading. The
full-family row independently confirms the 2026-08-09 modular certificate, the three
linear modes annihilating every row so the kernel is exactly `w(c P(u)) = Tr(rho, c
P(u))`; unlike the parent's mod-`p` certificate it is a rational elimination end to
end.

**The narrow no-go clause.** What the frame lift consumes is not ternary *arity*:
the mixed ternary carries no more information than its binary shadow. It is menu
**abundance** — every binary and every non-collinear rank-one ternary resolution
occurring as a support. A covariant nearest-neighbour law reading an alphabet of `a`
symbols has at most `a^6` conditions and so at most `a^6` menus, a finite family,
while the non-collinear rank-one ternary resolutions form an infinite one: the runner
exhibits 200 pairwise distinct exact rational members from one Pythagorean
parametrisation, every one a legitimate menu. `L_MENU` is such a law: it realises 166
menus, **none** a non-collinear rank-one ternary, and `f(u) = u_z^3` is exactly
normalized on all of them. The clause proved here is exactly this, nothing broader:

> A nearest-neighbour law with a finite record alphabet cannot supply menu
> abundance.

## T3 — The Cube's Own Record Odds Are Not A Universal Grading

The runner rebuilds the emergent model from scratch inside the file: the `2x2x2`
cube, 12 edge qubits in the superfast encoding, the Kawamoto-Smit staggered link
signs giving flux `-1` on all six faces, the 128-dimensional code space, and its
non-degenerate half-filled sea at `E = -4 sqrt(3)` with gap `2 sqrt(3)`. That sea
has exactly 2112 exact zeros among the 4096 computational labels — the selection
rule zeros that make forcing possible at all. A record at edge `q` registers bit `q`
of the label; the menu is the support of the conditional distribution.

| prior records `k` | nonzero record blocks | distinct `p(Z = 0)` at a free edge | menus |
|---|---|---|---|
| 0 | 1 | `1/2` | `{0,1}` |
| 1 | 24 | `1/2` | `{0,1}` |
| 2 | 264 | `1/2` | `{0,1}` |
| **3** | **1760** | **`5/18, 1/3, 1/2, 2/3, 13/18`** | `{0,1}` |

Complete over every record subset and every value, no menu is a singleton at `k = 4,
5, 6, 7`; forcing first appears at `k = 8`, where the eight zero records on edges
`0..6` and `8` lock edge `9` — the corner pair `(4,6)` — to the value one, against
odds `1/2` for that same possibility in the empty neighbourhood. Both readings the
campaign carried are corrected. The odds are **not** "flat `1/2` or forced": that
holds only for `k <= 2`. And at `k = 3` the menu is the same binary `{0,1}` in every
block while the same possibility receives five different odds, which a single
universal grading forbids outright. **The cube's record odds are Born odds `Tr(rho_n
E)` of a state that varies with the records — which is what a nearest-neighbour law
is for — and that is exactly what one global grading `w` cannot be.**

The cube also supplies **no discriminator** for the clause. Under the relaxation
tick `M_R` and under the sea, on the sampled neighbourhoods, every menu is the same
binary `{0,1}`: `M_R` removes the selection-rule zeros, so nothing is forced there.
Both depart from `1/2` at exactly the same place — records `(0,1,2,3) = (0,0,0,0)`,
edge `4`, where the tick gives `1/5` and the sea `1/3` — and uniform gives `1/2` on
every binary menu here. A menu-independence test cannot separate the three laws on
this carrier, which realises one menu shape; that needs a site whose *menu* varies,
and so the scaled contents `c P(n)`, `c I` that a 12-qubit edge-record model lacks.

## T4 — The Vacuity Lemma And The Two Usable Sentences

**Vacuity lemma.** Under Admissibility the menu is a *function* of the condition:
`M(n) = supp p_n`. A clause that already permits the odds to depend on the
neighbourhood's records therefore cannot forbid dependence on which other
possibilities are admissible, because the admissible set is itself a function of the
condition. In particular the candidate sentence

> *"the odds depend on the possibility and its neighbourhood's records, not on
> which other possibilities are admissible"*

is satisfied verbatim by `L_MENU` with `UNIFORM`, which is menu-dependent at `1/3`
against `1/2` on the shared possibility. It places no constraint, and **it is not
offered here.** Any non-vacuous clause must compare *different* conditions. Two
candidates survive that test.

- **S1 — the 2026-08-09 clause stated honestly.** *The odds a forming record
  registers for a possibility are fixed by that possibility alone; the
  nearest-neighbour conditions fix only which possibilities are admissible.*
  Non-vacuous, and with abundance it yields one density matrix for the whole
  lattice. It is **false** in the emergent cube (T3).
- **S2 — the fibred clause.** *Conditions sort into fixed classes; within a class the
  odds are fixed by the possibility alone, and every two-fold and three-fold resolution
  of the site's possibilities is admissible under some condition of the class.*
  Consistent with the cube's form, since `rho` may vary across classes — but it carries
  the class structure, the grading inside a class, and abundance inside a class. Either
  way the readout price is **three** items and not one: a fibred menu-independence
  clause, abundance, and the frame import.

## Corollary

1. Menu-independence is **not implied** by Lattice, Qubit, Admissibility and
   Record. The witness is an exact covariant nearest-neighbour law carrying both
   a menu-independent and a menu-dependent normalized odds rule.
2. With menu-independence in force the Born form **still** needs menu abundance,
   and a nearest-neighbour law with a finite record alphabet cannot supply it;
   on such laws the Born form is not forced by the supports and a menu clause.
3. The emergent model's own record odds are Born odds of a conditioned state, not
   a universal grading, so any usable clause must be fibred over conditions.
4. The readout price is therefore three items — a fibred menu-independence
   clause, abundance, and the frame import — not one. **The Root A
   closure-by-decision proposed in PR #7912 is withdrawn to that statement.**
5. The candidate sentence quoted in T4 is vacuous under Admissibility, and is
   not offered.

## Reading, Not Theorem

The hope was that one plain sentence would turn the Born rule into a theorem. It
does not. The rule that a record's odds must not depend on the list of alternatives
is genuinely something the axioms leave open, but adding it is not enough: the
derivation also needs the lattice to offer, somewhere, every possible two-way and
three-way choice, and a neighbourhood rule with finitely many record values never
does. And the emergent model's own odds are not a fixed grading anyway; they depend
on what the neighbours have registered. So the price of the Born rule is three
things, and the first honest sentence for it has yet to be written.

## Interfaces

**Infinite record alphabets**: the narrow clause is about finite alphabets, and a
law whose record contents range over `S` itself is not covered here. **Abundance
from a larger neighbourhood**: it might be recovered by a compiler building the
missing ternary supports across several sites rather than at one. **The frame
import**: the dimension-three frame-function theorem is named in the parent note and
used the same way here, as context, and is not re-proved.

## Proof Boundary

Proved: the covariance of `L_MENU` over all `7^6` patterns and 24 rotations and on a
`3^3` torus; the exact normalization and covariance of four odds rules on its 166
realised menus; the single shared possibility and its four odds pairs; the
mixed-ternary reduction to the binary condition; the four nullity rows at degree
five with their explicit non-Born survivors; the infinite abundance family; and on
the cube, the block counts, the five odds values at three prior records, the absence
of forcing through seven and its appearance at eight, and the single menu shape
under the tick and the sea.

Not proved: any axiom-side derivation of the Born form; any value of `rho`; the
dimension-three frame-function theorem, named and not recomputed; any formation
site, probability or rate; menu arities above three; the minimal sufficient menu
family, shown necessary and not characterised; polynomial degree above five. T1 and
T2 are exact rational or exact symbolic throughout; T3 inherits float64 eigenvectors
of the cube and its conclusions depend only on the odds being distinct, with gaps of
order `10^-1`. The witness law is **one** law, not a classification of laws. The
no-go clause is exactly "a nearest-neighbour law with a finite record alphabet
cannot supply menu abundance" and nothing broader: no claim is made that the Born
form is underivable, that no other route reaches it, or that any route has been
ruled out.

Corollaries 1 and 4 are statements about the canonical wording and about what the
exhibited models satisfy, not non-derivability claims.
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) gives the one-site
`M_2(C)` presentation, a nearest-neighbour-determined and neighbour-varying
probability distribution whose support is the menu, and a readout value determined
by record content alone. It does not state that a registered effect carries one
grade across the menus it can sit in, nor that every low-arity resolution occurs as
a support. Whether Record dynamics, an operational-equivalence theorem, or a
physical registration construction supplies either remains open, and that is the
constructive successor this note points at; no axiom-side Born forcing is claimed
and no canonical axiom edit is proposed here.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| scaled domain `S` and its menus | declared family | 2026-08-09 parent note | physical eligibility remains open |
| the witness law `L_MENU` | theorem construction | explicit in this note and its runner | one law, not a classification |
| dimension-three frame-function theorem | context pointer | named in the parent note | not recomputed here |
| the `2x2x2` cube and its sea | finite emergent model | rebuilt inside the runner | float64 eigenvectors only |
| observations, fits, target probabilities | none | not used | not applicable |

## Review Record

This note confirms one half of the sibling branch's closing claim, corrects the other
half, and corrects the cube reading carried since PR #7895. It does not advance
current-surface physical Born closure. The minimal sufficient menu family, arities
above three, degree above five, the neighbour-to-density law, and record-formation
site, weight and rate are not classified. Independent audit remains required first.
