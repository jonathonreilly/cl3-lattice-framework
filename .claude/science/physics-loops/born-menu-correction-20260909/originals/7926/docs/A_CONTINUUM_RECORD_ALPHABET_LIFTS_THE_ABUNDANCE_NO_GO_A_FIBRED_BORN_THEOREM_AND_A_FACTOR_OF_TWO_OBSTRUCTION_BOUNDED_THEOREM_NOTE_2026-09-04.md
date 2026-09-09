---
claim_id: continuum_alphabet_lifts_abundance_no_go_fibred_born_factor_two
claim_type: bounded_theorem
claim_scope: "Exact rational and exact symbolic one-site algebra under a Z^3 nearest-neighbour law. (i) L_CONT, an explicit translation- and cubic-covariant nearest-neighbour law whose record alphabet is the continuous scaled-effect domain, realises every binary, every non-collinear rank-one ternary and every coin resolution of the identity as the support of some neighbourhood condition, on 41760 exact covariance checks with zero mismatches, so the finite-alphabet abundance clause is lifted constructively. (ii) With an equivariant lattice-dipole fibration one fibre realises that same abundant family, and the fibred law L_FIB with rho at e_x equal to (I + (2/3) sigma_x)/2 is normalized, non-negative and covariant on 83520 exact per-possibility checks; an exact rational rank certificate on a law-realised family of 1764 rows and 21 columns has rank 18, nullity 3 and kernel span{x, y, z}. (iii) Two covariant continuum laws realise no rank-one ternary support and carry the exact non-Born grading f(u) = u_z^3, so a continuum record alphabet permits abundance and does not supply it. The narrow no-go clause is exactly two obstructions and nothing broader: no measurable coarse-graining of the continuous domain reproduces the Born frame values, the tilt being short by exactly a factor of two, so per-condition abundance is impossible; and a fibre class map with rotation-invariant classes forces rho = I/2, so an invariant scalar label cannot carry a state. No axiom is changed, no axiom-side Born forcing is claimed, and the dimension-three frame-function theorem is named as context, not recomputed."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.py
---

# A Continuum Record Alphabet Lifts The Abundance No-Go: A Fibred Born Theorem And A Factor-Of-Two Obstruction

**Date:** 2026-09-04
**Type:** bounded_theorem, carrying one narrow two-part no-go clause
**Audit:** unset; independent audit remains a separate lane
**Status authority:** independent audit only. This note authors no audit verdict and changes no axiom, primitive, registry, queue, or policy.
**Primary runner:**
[`scripts/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.py`](../scripts/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.txt`](../logs/runner-cache/continuum_alphabet_lifts_abundance_no_go_fibred_born_check_2026_09_04.txt)
**Parent:**
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md).
The immediate predecessor is the sibling branch note *Menu-Independence Is Independent
Of The Axioms And Insufficient With Them* (PR #7919), whose finite-alphabet abundance
clause this note lifts and whose nullity figures it bounds.

## Result Up Front

PR #7919 priced the Born form at three items — a fibred menu-independence clause, **menu
abundance** (every binary and every non-collinear rank-one ternary resolution of the
identity occurring as some condition's support), and the imported dimension-three frame
theorem — and proved a narrow no-go against the second: a **finite** record alphabet
gives finitely many supports, never an infinite family. The Qubit axiom imposes none.
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) states that "the full
one-site possibility domain has algebraic presentation `M_2(C)`", and Admissibility's
reading note (3) that "on a continuous domain, a supported exact point may have zero
singleton measure". Does a **continuum** record alphabet supply menu abundance, and does
a fibred Born theorem then hold?

It lifts the no-go and does not supply the hypothesis. An explicit covariant
nearest-neighbour law on the physical lattice, reading record values in the continuous
effect domain, realises the **complete** abundant family, so a fibred Born theorem
holds, instantiated with a neighbourhood-varying state — the shape the emergent cube
demands. But two equally covariant continuum laws realise no rank-one ternary support
and carry an exact non-Born grading, so abundance stays a hypothesis on the law; and
abundance **per condition** is impossible by exactly a factor of two, while a
rotation-invariant fibre label carries no state.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "The lattice algebra is exact at the declared directions, planes and conditions, and the two no-go halves are exact statements about coarse-grainings of a continuous domain and about invariant fibre classes. The positive Born direction still rests on a supplied fibred grading clause, on abundance as a property of the exhibited law, and on the named dimension-three frame-function theorem."
trace_class: upstream_support
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Register, or derive from Record dynamics, which covariant continuum law the framework runs, since abundance separates the exhibited laws and is not settled by the axioms."
conditional_surface_status: "exact rational and exact symbolic algebra conditional on a supplied fibred grading clause, declared rational directions and planes, stated polynomial degree, and the named dimension-three frame-function theorem"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

Work at one site of the physical lattice, with `H = C^2`. For a unit vector `n` write
`P(n) = (I + n dot sigma)/2`, and take the 2026-08-09 scaled domain `S = {c P(n) : 0 < c
<= 1, |n| = 1} union {c I : 0 < c <= 1}`; a **menu** is a finite family of nonzero
members of `S` summing to `I`. Records register, and the needles are the six neighbour
record contents, so a **condition** `n` is a partial map from `{+-e_x, +-e_y, +-e_z}` to
`S`. A **law** is the map `n |-> p_n` Admissibility supplies, one fixed covariant rule
"determined by, and varies with, the nearest-neighbor conditions"; by reading note (3)
the support `S(n) = supp p_n` is what "available" and "admissible" denote, so a
condition's menu is its support. Record adds that "when present, a record locks exactly
one admissible local possibility" and that "only records are readable". The record
alphabet here is the whole continuous domain — the freedom the finite-alphabet clause
left open. The runner keeps machine verification and recorded argument apart: 50 checks
print `PASS`, while 8 arguments proved by hand below print with an `ARG:` prefix and are
excluded from the total. Every stage is exact and no seed is used.

## T1 — A Continuum Record Alphabet Supplies Full Abundance

**The law `L_CONT`, a record-echo rule.** On the multiset `R(n)` of recorded Bloch
directions, one record echoes as the binary resolution of its own direction, three
coplanar positively spanning records as their ternary resolution, two records as a coin;
anything else gives `{I}`.

| records | support `S(n)` |
|---|---|
| `{m}` | `{P(m), P(-m)}` |
| `{m_1, m_2, m_3}` coplanar, positively spanning | `{c_k P(m_k)}`, `c` the unique solution of `sum c_k m_k = 0`, `sum c_k = 2` |
| `{m_1, m_2}` with `a = (1 + m_1 dot m_2)/2` in `(0,1)` | `{a I, (1-a) I}` |

The rule reads only the multiset of record values, through equivariant linear algebra
and an invariant inner product; it names no slot and no lattice axis. The runner checks
`S(g.n) = g.S(n)` on **41760 exact checks over 24 rotations and 1740 declared
conditions, zero mismatches**, that moving the same values to other slots leaves the
support unchanged, and that each realised support resolves `I` exactly. Every binary
rank-one resolution is a support, by the one-record condition — **80 of 80** declared
directions, and onto the full family by construction; every non-collinear rank-one
ternary is, by the three-record condition — **1200 of 1200** exact rational resolutions
from **14** declared rational planes; every coin is, at 77 distinct exact rational `a`,
since `a = (1 + m_1 dot m_2)/2` sweeps `(0,1)` with the inner product.

> **Proposition 1.** `L_CONT` is a translation- and cubic-covariant,
> nearest-neighbour-determined law with a continuum record alphabet whose realised
> supports comprise every binary, every non-collinear rank-one ternary and every coin
> resolution of the identity. **The finite-alphabet abundance clause of PR #7919 is
> lifted constructively.**

## T2 — The Fibred Born Theorem, Instantiated

A grading shared across **all** conditions is the global 2026-08-09 clause, which the
emergent cube falsifies: its conditional record odds take five values on one and the
same binary menu. The clause must be fibred, over an equivariant fibration independent
of the menu. **The lattice-dipole fibration** `lambda(n)` is the sum of the recorded
slot directions: equivariant on **41760 exact checks, zero mismatches**, and decoupled
from the menu by construction, since `lambda` sees only which slots carry records and
the menu only the record values. The fibre `lambda = e_x` contains every binary, through
the slot pattern `{+e_x}`, and every rank-one ternary, through `{+e_x, +e_y, -e_y}`
whose dipole is again `e_x`: **1200 of 1200** exactly.

> **Theorem (fibred Born form on a continuum alphabet).** Let `L: n |-> p_n` be a
> translation- and cubic-covariant nearest-neighbour law whose record alphabet is the
> continuous domain `S`, with `S(n) = supp p_n` a finite resolution of `I`, and let
> `lambda` be an equivariant map from conditions to a cubic `G`-set. Suppose **(A)
> abundance in fibre** — for each label `l`, every binary and every non-collinear
> rank-one ternary resolution occurs as `S(n)` for some `n` with `lambda(n) = l` — and
> **(MI-fib) fibred menu-independence** — there is a grading `w_l` with `p_n(v) =
> w_l(v)` for every `n` in the fibre and every `v` in `S(n)`. Then by the imported
> dimension-three frame-function theorem `w_l(E) = tr(rho_l E)` with `rho_l` unique per
> fibre, so `p_n(E) = tr(rho_{lambda(n)} E)`: the Born form with a state that varies
> with the neighbourhood, and covariance gives `Stab(l) rho_l = rho_l`.

**The model.** `L_FIB` sets `rho_l = (I + (2/3) l dot sigma)/2` for `l` a unit lattice
direction and `I/2` otherwise. It is normalized to exactly 1 on every realised support
of all 1740 conditions, non-negative everywhere, covariant on **83520 exact
per-possibility checks, zero mismatches**, and non-vacuous inside one fibre: the two
supports `{(8/9)P(e_z), (5/9)P(3/5,0,-4/5), (5/9)P(-3/5,0,-4/5)}` and the same rotated
into the `y`-`z` plane both resolve `I` exactly, both have dipole `e_x`, and they share
the possibility `(8/9)P(e_z)`.

**An independent rank certificate.** In the normal form `w(cP(u)) = c(1 + f(u))/2` with
`f = A(x,y) + z B(x,y)` of degree at most five — 36 monomials, 21 once the binary
condition makes `f` odd — the 1764 ternary resolutions `L_CONT` realises give a **1764
by 21** matrix of **rank 18, nullity exactly 3, kernel exactly `span{x, y, z}`**, the
Born family `c(1 + r dot u)/2 = tr(rho, cP(u))`; without oddness, 36 columns of rank 33
and the same nullity 3, an exact rational elimination over `Q` from a family a law
actually realises.

## T3 — Abundance Per Condition Is Impossible By Exactly A Factor Of Two

A support is one resolution of `I`, so it contains exactly one menu; two disjoint
resolutions inside one support would carry total mass two. The only way to read many
menus out of one condition is to coarse-grain a continuous support, and that fails
exactly. On the pure-state slice with the normalized round measure `dmu`, the Born
density `dP_rho(u) = (1 + r dot u) dOmega/4pi` integrates to exactly 1 and `int 2P(u)
dmu = I` exactly, so the continuum family is itself a resolution of the identity. Ask a
measurable cell `A` to reproduce a Born frame value: `p_rho(A) = mu(A) + r dot int_A u
dmu` must equal `(1 + r_z)/2` for every `rho`, forcing `mu(A) = 1/2` **and** `int_A u
dmu = e_z/2`. But `|int_A u dmu| <= mu(A) = 1/2`, with equality only if `u` were
constant almost everywhere on `A`; the true maximum at `mu(A) = 1/2` is the
hemisphere's, exactly `1/4` by exact symbolic integration.

> **Proposition 6.** The best coarse-grained odds on a continuous possibility domain are
> `1/2 + r_z/4`, against the Born frame value `1/2 + r_z/2`. **The Born tilt is short by
> exactly a factor of two, for every `rho`.** No measurable coarse-graining of a
> continuous support reproduces the Born frame values, so per-condition (coarse-grained)
> abundance is impossible and abundance is necessarily **across** conditions.

Zero singleton measure costs nothing: every singleton `{P(u)}` has measure zero while
the density `1 + r dot u` stays positive, exactly what reading note (3) contemplates,
and the frame lift returns the density. Lueders conditioning on a locked pure state is
well defined off one antipode of a pure `rho`, of measure and density zero.

## T4 — The Continuum Permits Abundance And Does Not Supply It

Two further laws have the same continuous alphabet and covariance, no abundance.

| law | support | verification |
|---|---|---|
| `L_COIN` | `{a I, (1-a) I}` at the invariant mean of the pairwise record inner products | covariant on **9600** exact checks, zero mismatches; **no rank-one support at all** |
| `L_BIN` | `{P(vhat), P(-vhat)}` at `v` the sum of the recorded directions | equivariant on **9600** exact checks, zero mismatches; **only antipodal binary supports** |

On both, `f(u) = u_z^3` is an exact menu-independent, normalized, **non-Born** grading:
odd, so it passes every binary and coin menu identically, and not a trace form —
`f(3/5,0,4/5) = 64/125` against `4/5` — while `|f| <= 1` keeps the odds in `[0,1]`.

> **Proposition 2.** A continuous possibility domain is necessary for abundance under a
> covariant nearest-neighbour law and is not sufficient: abundance remains a hypothesis
> on the **law**, not a consequence of the axioms.

## T5 — The Covariance Obstruction To Invariant Fibre Labels

Covariance forces `rho_{g.l} = g rho_l g^*`, hence `Stab(l) rho_l = rho_l`. The runner
computes the invariant Bloch spaces as exact kernels of `R - 1` over `Q`: `Stab(e_x)`
has order 4, the `C_4` about the `x` axis, with invariant Bloch space the `x` axis, so
`rho = (I + t sigma_x)/2` with `t` free; the invariant Bloch space of the full rotation
group is `{0}`.

> **Proposition 5.** A fibred clause whose classes are rotation-invariant yields `rho_l
> = I/2` for every class — no state information at all, the Born form degenerating to
> the uniform trace form. Any useful class map must be an equivariant surjection onto a
> non-trivial cubic `G`-set: **the label must carry a direction.**

Record count and pairwise record inner products are rotation invariant on every swept
condition, so a label built from them carries no state: the lattice dipole is directed,
a scalar is not.

## T6 — One Great Circle Gives Born Odds, Two Pin The State

A law evaluates its grading only on the directions its own supports realise, so the
requirement is smaller than a global nullity count suggests. All **2470** rank-one
ternary resolutions inside the single great circle `z = 0` leave global nullity **17**,
so one circle does not pin a global grading; but restricted to the circle, in the odd
Fourier modes 1, 3 and 5, they have **rank 4 and nullity 2**, the surviving modes being
exactly `cos t` and `sin t`. The reason is structural: for a coplanar triple the weight
vector spans the kernel of `[n_1 n_2 n_3]`, so `det[[cos t_k, sin t_k, f(t_k)]] = 0` for
every positively spanning triple, and `t |-> (cos t, sin t, f(t))` lies in a plane.

> **Proposition 3.** If the realised directions cover one great circle with its in-plane
> ternary family, `f` on that circle is forced to `r dot u`: **the odds are Born odds on
> the realised support**, with `rho` fixed up to the component normal to the plane. If
> they meet two non-parallel great circles, agreement of the shared grading at the
> intersection `+-e_x` forces the in-plane components to match, so a single `r`
> reproduces the grading on the union.

Consistently, `f(u) = u_z^3` has residual exactly zero on all 2470 in-plane resolutions
— there it is Born with `rho = I/2` — while failing 1506 of the 1764 over 14 planes.
This bounds from above the minimal sufficient family: one circle's in-plane ternaries
for Born odds, two non-parallel circles for a unique state.

## Corollary

1. The finite-alphabet abundance clause is **lifted constructively**, by an explicit
covariant nearest-neighbour law with a continuum record alphabet and full menu
abundance. 2. A **fibred Born form holds** and is instantiated: `L_FIB` is a verified
covariant law whose odds are Born odds with a neighbourhood-varying state, the shape the
emergent cube demands and a global grading forbade. 3. The continuum **permits**
abundance and does not **supply** it: covariant continuum laws without ternary supports
carry an exact non-Born grading, so item two of the price changes status from unpayable
to payable with a witness, **not discharged**. 4. Per-condition abundance is impossible
by exactly a factor of two, so abundance is across conditions; and the fibre label must
carry a direction, since a rotation-invariant class forces `rho = I/2`. 5. One great
circle of ternary resolutions already yields Born odds on the realised support and two
non-parallel circles pin the state, bounding the minimal sufficient family from above.
6. What remains supplied, unchanged in count: the fibred menu-independence clause with
its class map, the law's form — not settled here — and the frame import.

## Reading, Not Theorem

If records can take any of the qubit's possible values rather than a few, a
neighbourhood rule can offer every two-way and three-way choice somewhere, and then, for
any rule whose odds do not depend on the list of alternatives, the Born rule follows
with a state that changes from place to place, as the emergent model needs. But the
continuum only makes this possible; it does not make it happen, and a single site's menu
can never carry it alone. The price of the Born rule is unchanged in count and lighter
in kind.

## Interfaces

**The fibred clause.** The class map is constructed here, not derived; whether Record
dynamics or a registration construction supplies an equivariant directed class map
remains open. **The frame import.** The dimension-three frame-function theorem is named
in the parent note and used the same way here, as context. **Densities on the continuous
domain.** The Born density, the continuum resolution `int 2P(u) dmu = I` and Lueders
conditioning are consistent here; what a physical registration does with a density is
the constructive successor this note points at.

## Proof Boundary

Proved: the covariance of `L_CONT` and the resolution of every realised support over 24
rotations and 1740 declared conditions; abundance on 80 binaries, 1200 ternaries from 14
declared planes and 77 coin values; the equivariance and menu-decoupling of the lattice
dipole and abundance inside one fibre; the normalization, non-negativity, covariance and
non-vacuity of `L_FIB`; the exact rational rank certificates at degree five; the
covariance of `L_COIN` and `L_BIN` and the survival of `f(u) = u_z^3` on them; the
stabiliser and invariant-Bloch kernels; the great-circle rank and kernel; and the exact
symbolic density, continuum-resolution and hemisphere integrals.

Not proved: any axiom-side derivation of the Born form; that abundance follows from the
axioms, which it does not; any value of `rho` or of `t`; the class map, constructed and
not derived; the dimension-three frame-function theorem, named and not recomputed; menu
arities above three; polynomial degree above five; the minimal sufficient family,
bounded above and not characterised; and that `L_CONT` or `L_FIB` is the framework's
actual law.

The no-go clause here is exactly two statements and nothing broader: **no measurable
coarse-graining of a continuous support reproduces the Born frame values, the tilt being
short by exactly a factor of two, so per-condition abundance is impossible**; and **a
fibred clause with rotation-invariant classes forces `rho = I/2`, so an invariant scalar
label cannot carry a state.** No claim is made that the Born form is underivable or that
another route fails; this note removes a wall a sibling note had raised.

[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the one-site
`M_2(C)` presentation, a nearest-neighbour-determined and neighbour-varying probability
distribution whose support is the menu, the continuous-domain reading note, and a
readout value fixed by record content alone. It does not state which law applies, nor
that a registered effect carries one grade across the conditions it can sit in. No
axiom-side Born forcing is claimed and no canonical axiom edit is proposed here.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| scaled domain `S` and its menus | declared family | 2026-08-09 parent note | physical eligibility remains open |
| `L_CONT`, `L_FIB` and the lattice-dipole class map | theorem construction | explicit in this note and its runner | two laws and one map, not a classification |
| dimension-three frame-function theorem | load-bearing mathematical input | named in the parent note | not recomputed here |
| `L_COIN` and `L_BIN` | independence witnesses | explicit here | show abundance is a hypothesis on the law |
| observations, fits, target probabilities | none | not used | not applicable |

## Review Record

PR #7919 left the abundance requirement unpayable on a finite record alphabet and the
minimal sufficient family uncharacterised. This note pays it with an explicit continuum
law, exhibits the first verified fibred model whose odds are Born odds with a
neighbourhood-varying state, bounds that family from above, and adds two exact
obstructions. It does not advance current-surface physical Born closure: the law, the
fibred grading clause and the frame import are all still supplied.

Independent audit remains required before the repository may assign any effective claim
status.
