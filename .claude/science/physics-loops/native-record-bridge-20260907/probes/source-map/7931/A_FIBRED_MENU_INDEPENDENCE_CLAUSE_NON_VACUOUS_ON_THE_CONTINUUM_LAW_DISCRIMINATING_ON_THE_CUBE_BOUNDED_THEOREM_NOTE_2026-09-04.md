---
claim_id: fibred_menu_independence_clause_non_vacuous_discriminating
claim_type: bounded_theorem
claim_scope: "Exact rational one-site algebra together with an complete float64 sweep of the emergent 2x2x2 cube. (i) The fibred menu-independence clause MI-fib', stated in comparison form over an equivariant menu-blind map sigma from neighbourhood conditions to states on the site's own possibility domain, escapes the vacuity lemma and is strongly non-vacuous on the continuum law L_CONT: two overlapping ternary supports lie in the single dipole fibre lambda = e_x and share the possibility (8/9) P(e_z), where the Born grading gives 4/9 under both while an adversary law meeting Lattice, Qubit, Admissibility and Record gives 20/27 and 28/135; inside that same fibre a mixed ternary and a coin menu share (1/3) I, which the uniform law grades 1/3 and 1/2 while every state grades 1/3, so the clause separates the Born form from the uniform form exactly. (ii) On the cube the conditioned-sea odds equal tr(rho_q(n) P_b) on 164232 checks over all 9969 conditions with at most four records, largest deviation 2.7e-15, and this is an identity and not a test, the cube offering the single frame {P_0, P_1}; on that same complete family no fibre contains two menus, so strong non-vacuity is impossible on the cube for any law and any state-valued fibre map. (iii) The cube nevertheless discriminates the record-conditioned relaxation tick in the weak form: 56 of 172 multi-element fibres carry unequal tick odds, largest difference 0.126777, with an exact witness of two four-record sets conditioning edge 10 to diag(2/3, 1/3) with sea odds 2/3 under both and tick odds 4/5 and (6 + sqrt 2)/8, both tick ground states non-degenerate; the uniform law is not discriminable there, structurally. (iv) The odds map is exactly equivariant under all 24 proper cubic rotations on 450144 triples, largest deviation 7.2e-16, while no site unitary makes the conditioned-sea state map equivariant, the exact diagonal invariance forcing U_g diagonal and so preserving |rho_01|, which differs by 0.289. (v) With the clause in force the Born form is a theorem for L_CONT under exactly four named conditions and is not one for the cube. No axiom is changed, no axiom-side Born forcing is claimed, the dimension-three frame-function theorem is named and not recomputed, abundance is named as a property of the law and not supplied by the sentence, and the two drafted sentences are offered as candidate wordings and not as axiom text."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/fibred_menu_independence_clause_non_vacuous_discriminating_check_2026_09_04.py
---

# A Fibred Menu-Independence Clause: Non-Vacuous On The Continuum Law, Discriminating On The Cube

**Date:** 2026-09-04
**Type:** bounded_theorem, carrying two exact finite negative statements
**Audit:** unset; independent audit remains a separate lane
**Status authority:** independent audit only. This note authors no audit verdict and changes no axiom, primitive, registry, queue, or policy.
**Primary runner:**
[`scripts/fibred_menu_independence_clause_non_vacuous_discriminating_check_2026_09_04.py`](../scripts/fibred_menu_independence_clause_non_vacuous_discriminating_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/fibred_menu_independence_clause_non_vacuous_discriminating_check_2026_09_04.txt`](../logs/runner-cache/fibred_menu_independence_clause_non_vacuous_discriminating_check_2026_09_04.txt)
**Parent:**
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md).
Two sibling-branch notes are its immediate predecessors: *Menu-Independence Is Independent Of The
Axioms And Insufficient With Them* (PR #7919), whose vacuity lemma this note works around and whose
reading of the cube it corrects, and *A Continuum Record Alphabet Lifts The Abundance No-Go*, which
supplies the continuum law `L_CONT`, the lattice-dipole fibration and the fibred Born theorem whose
covariance hypothesis is tested here.

## Result Up Front

PR #7919 priced the Born form at three items and proved a **vacuity lemma**: under Admissibility
the menu is a function of the condition, so a clause saying that the odds of a possibility do not
depend on what else is admissible **at a fixed condition** places no constraint at all. The sibling
continuum note then proved a fibred Born theorem whose fibred menu-independence hypothesis was
supplied, not derived. The question here is narrow and exact: **can that clause be written as
one sentence in the axiom's register which is non-vacuous, satisfied by the emergent sea, and
sufficient with abundance?**

It can be written, and written that way it has content — but the three predicates do not hold in
one place. The escape from the vacuity lemma is to **compare two conditions** through a menu-blind,
equivariant map from neighbourhoods to states on the site's own possibility domain. So written, the
clause separates the Born form from the uniform form exactly, inside a single fibre of the
continuum law. The emergent cube satisfies it as an **identity** and cannot test it, since there
every neighbourhood offers the same menu; yet it does discriminate, in the weak form, against the
record-conditioned relaxation tick, correcting PR #7919's reading. And its state map is equivariant
in the odds and **not** equivariant under any site unitary.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "The one-site algebra is exact rational at the declared directions, conditions and fibres, and the cube sweeps are complete enumerations whose reported equalities hold to 1e-12 and whose reported differences are of order 1e-1. The positive Born direction still rests on abundance as a property of the exhibited law, on the named dimension-three frame-function theorem, and on the law's form, none of which the sentence supplies."
trace_class: upstream_support
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Build the gauge-corrected symmetry operator on the cube, so that the covariance hypothesis of the fibred theorem can be tested there rather than left unverified."
conditional_surface_status: "exact rational one-site algebra and complete cube enumerations, conditional on a supplied fibred grading clause, on abundance as a property of the law, and on the named dimension-three frame-function theorem"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

Work at one site, with the site's possibility domain presented as `M_2(C)`. For a unit vector `u`
write `P(u) = (I + u dot sigma)/2` and take the 2026-08-09 scaled domain `S = {c P(u) : 0 < c <= 1}
union {c I : 0 < c <= 1}`; a **menu** is a finite family in `S` summing to `I`. Records register,
and the needles are the six neighbour record contents, so a **neighbourhood condition** `n` is the
record content on the six nearest neighbours. A **law** is the map `n |-> p_n` that Admissibility
supplies, one fixed rule "determined by, and varies with, the nearest-neighbor conditions",
covariant under translations and the 24 proper cubic rotations. By reading note (3) the support of
`p_n` is what "admissible" denotes, so the condition's menu is `M(n) = supp p_n`.

The lattice is physical; the cube stages are computations on the framework's own emergent model,
the 2x2x2 cube with 12 edge qubits in the superfast encoding, staggered link signs giving flux `-1`
on all six faces, and the non-degenerate half-filled sea at `-4 sqrt(3)` with gap `2 sqrt(3)` and
2112 exact zeros among the 4096 record labels. `M_R` is the record-conditioned relaxation tick, the
ground-space diagonal of the conditioned Hamiltonian and the campaign's standing adversary to the
sea. The runner keeps machine verification and recorded argument apart, arguments proved by hand
printing with an `ARG:` prefix and excluded from the total; every condition family is a complete
enumeration by declared index arithmetic and no seed is used.

## T1 — The Clause, And What It Costs To Make It Bite

> **(MI-fib')** There is an equivariant, menu-blind map `sigma` from neighbourhood conditions to
> states on the site's own possibility domain, and if `sigma(n) = sigma(n')` then `p_n(v) =
> p_n'(v)` for every possibility `v` admissible under both.

Equivalently `p_n(v) = w(v; sigma(n))`, one grading per state. It does not say `w(v; sigma) =
tr(sigma v)`, which would import the Born form as a premise, and it does not name `sigma`, which is
part of the law's data exactly as the menu is.

**Why it escapes the vacuity lemma.** The lemma bites only at a fixed condition. `MI-fib'` compares
**two** conditions, and the map is required to be menu-blind — without that requirement `sigma(n)
:= p_n` satisfies the sentence verbatim and the lemma applies again. On the continuum law the
lattice dipole `lambda(n)`, the sum of the recorded slot directions, is menu-blind by construction:
it reads only which slots carry records, the menu only the values.

**Strong non-vacuity, exact.** In the fibre `lambda = e_x`, reached by the slot pattern `{+e_x,
+e_y, -e_y}`, the two ternary supports `S_A = {(8/9) P(e_z), (5/9) P(3/5, 0, -4/5), (5/9) P(-3/5,
0, -4/5)}` and the first's rotation into the `y`-`z` plane, `S_B = {(8/9) P(e_z), (5/9) P(0, 3/5, -4/5),
(5/9) P(0, -3/5, -4/5)}`, both resolve `I_2` exactly and share exactly one possibility, `(8/9)
P(e_z)`. The Born grading `rho at e_x = (I + (2/3) sigma_x)/2` sums to exactly `1` on both and
gives the shared possibility `4/9` under both. An adversary law `L_ADV`, whose state reads the
record value on the dipole slot — equivariant, nearest-neighbour determined, normalised on every
resolution of `I_2` automatically — gives that same possibility **`20/27` under one condition and
`28/135` under the other**. `L_ADV` meets Lattice, Qubit, Admissibility and Record and fails
`MI-fib'`: the clause has content.

**It separates Born from uniform inside one fibre.** That same fibre contains the mixed ternary
`{(2/3) P(u), (2/3) P(-u), (1/3) I}` and the coin menu `{(1/3) I, (2/3) I}`, sharing the
possibility `(1/3) I`. The uniform law grades it `1/3` in the first and `1/2` in the second — a
violation inside one fibre — while **every** state grades it `1/3` in both, since `tr(rho (1/3) I)
= 1/3` for all `rho`. Finally, the only Bloch vector invariant under all 24 rotations is `0`, and
`Stab(e_x)` has order 4 with invariant Bloch space `span{e_x}`: a rotation-invariant label carries
no state, so the fibre label must carry a direction.

## T2 — On The Cube The Clause Is An Identity, And Cannot Be Strongly Tested

Take `sigma(n) := rho_q(n)`, the reduced record-conditioned sea state at the free edge `q`. Over
the complete family of **9969** conditions — every record subset of size at most four with every
value — and every free edge:

> `p_n(P_b) = tr(rho_q(n) P_b)` on **164232 checks**, largest deviation **2.7e-15**.

**This is an identity, not a test.** `rho_q(n)` *is* the reduced conditioned sea, whose
record-basis diagonal *is* the odds. The cube offers the single frame `{P_0, P_1}`, so it can never
test the Born *form*; it can only test the clause. With three records the odds take exactly the
five values `5/18, 1/3, 1/2, 2/3, 13/18` on one binary menu, which refutes a rotation-invariant
fibre label on the framework's own model.

**Strong non-vacuity is impossible there.** Over the same complete family, **no fibre of the
conditioned state contains two different menus** — zero violations over 82116 condition-edge pairs.
The reason is one line and holds for **any** law and **any** state-valued fibre map: the cube's
records register a bit in one fixed frame, so every menu is a subset of `{P_0, P_1}` and `M(n) =
{P_b : tr(sigma(n) P_b) > 0}` is a function of the state. With menus in a single frame the state
determines the menu, and the clause's "whatever else is admissible in each" has nothing to grip.
Weak non-vacuity, on the other hand, holds abundantly: all **172** fibres carry more than one
condition, the largest **6083**.

## T3 — But The Cube Does Discriminate The Relaxation Tick, In The Weak Form

On the same complete family, with the fibre keyed by the unitary invariants `(rho_00, rho_11,
|rho_01|)` at each site:

| law | multi-element fibres with unequal odds | largest difference |
|---|---|---|
| the record-conditioned sea | **0 of 172** | – |
| the relaxation tick `M_R` | **56 of 172** | **0.126777** |
| the uniform law | **0 of 172** | – |

**The exact witness.** Two four-record sets condition edge 10 to the same state:

```
n  : edge 2 = 1, edge 4 = 0, edge 8 = 1, edge 9 = 0      site q = 10
n' : edge 2 = 1, edge 3 = 1, edge 4 = 1, edge 9 = 1      site q = 10

sigma(n) = sigma(n') = diag(2/3, 1/3), coherence at most 2.0e-18; menu {P_0, P_1} under both
sea odds : 2/3 and 2/3                            -- MI-fib' satisfied
M_R odds : 4/5 and (6 + sqrt 2)/8 = 0.926776695   -- MI-fib' violated
uniform  : 1/2 and 1/2                            -- satisfied
```

Both tick ground states are non-degenerate, `E_0 = -4.809734345` and `E_0 = -5.226251860` each of
degeneracy one, so the difference is no artefact of a degenerate ground space.

**This corrects PR #7919's reading.** That note reported the cube as furnishing no discriminator,
which is right of the **global** clause and not of the **fibred** one: `M_R` reads the whole record
set through the conditioned ground space, and two record sets conditioning the sea to the same site
state need not relax to the same site state. **The uniform law, by contrast, is not discriminable
there, structurally:** its odds are a function of the menu, and on the cube the menu is a function
of the state (T2). Separating uniform needs the mixed-ternary and coin overlap of T1, which the
12-qubit edge-record model does not have.

## T4 — The Odds Are Equivariant; The State Map Is Not

The 24 proper cubic rotations induce 24 distinct permutations of the 12 edge qubits, all leaving
the sea probabilities invariant. Over every condition with at most three records:

> `p_(g.n)(P_b at g(q)) = p_n(P_b at q)` on **450144** condition-rotation-edge triples, largest
> deviation **7.2e-16**.

The odds map is exactly equivariant. The **state** map is not:

> **The cube's state map is not equivariant under any site unitary.** *Proof.* Conjugation by `U_g`
> preserves the record-basis diagonal for every condition, which the sweep above verifies to
> `7.2e-16`; hence `U_g` is diagonal or antidiagonal. An antidiagonal `U_g` exchanges `rho_00` and
> `rho_11`, contradicted by conditions with `rho_00 = 2/3`. A diagonal `U_g` preserves `|rho_01|`,
> contradicted by a difference of `0.289` (with `rho_01` itself moving by up to `0.577`). So no
> site unitary satisfies `rho_(g(q))(g.n) = U_g rho_q(n) U_g^dag` for the bare edge-permutation
> action. QED.

This is an exact finite statement about the bare permutation action on this carrier and nothing
broader. The staggered link signs fix a gauge, so a cubic rotation is a symmetry of the Hamiltonian
only up to a gauge transformation and the operator the site carries is not the bare edge
permutation; constructing the gauge-corrected one is an **open item**, and until it is built the
cube's status against the fibred theorem's covariance hypothesis is *unverified*, not settled
either way. The continuum law verifies that hypothesis directly, its dipole being equivariant on
exact checks.

## T5 — What The Sentence Buys, And The Two Candidate Wordings

With `MI-fib'` in force, the Born form `p_n(E) = tr(rho_(lambda(n)) E)` is a theorem for the
continuum law `L_CONT` under **exactly four conditions**:

1. the law's supports are finite resolutions of `I_2` in the scaled domain `S`;
2. **abundance in fibre** — every binary and every non-collinear rank-one ternary resolution occurs
   inside each fibre: a property of `L_CONT`, verified on the sibling branch, **not supplied by the
   sentence**;
3. the dimension-three **frame-function theorem**, imported;
4. the fibre map equivariant onto a non-trivial cubic `G`-set — the sentence's third clause, which
   a scalar label never meets (T1).

It is **not** a theorem for the emergent cube: the cube meets condition 2 in no fibre — every one
of its 82116 condition-edge menus lies in the single frame `{P_0, P_1}` and none carries a ternary
resolution — and condition 4 is unverified there (T4). The two wordings below are **candidate
wordings, not axiom text**, offered for review; nothing here ratifies either.

> **Layman.** Two neighbourhoods whose records leave a site in the same state give every
> possibility that site could register the same odds, whatever else remains possible there.

> **Precise, in the axiom's register.** The neighbourhood's records fix a state of the site. The
> odds the law assigns to a possibility depend on that possibility and on that state, and on
> nothing else: where two neighbourhoods fix the same state, every possibility admissible under
> both is given the same odds, whatever else is admissible in each. The state fixed by the records
> varies with the nearest-neighbour conditions and transforms with them under the lattice
> symmetries.

Register audit, machine-checked: neither wording uses a word outside the axiom's register, and both
use only *records*, *state*, *the odds*, *possibility*, *admissible*, *neighbourhood*,
*nearest-neighbour conditions* and *lattice symmetries*. The third sentence of the precise wording
is not decoration: without it the label may be taken rotation-invariant, and then every fibre state
is forced to `I/2` (T1).

## Corollary

1. The clause must compare **two conditions** through a menu-blind, equivariant state map, and so
   written it has content: it separates the Born form from the uniform form inside one fibre of the
   continuum law, exactly, and an adversary law meeting all four axioms violates it.
2. The emergent cube satisfies it as an **identity** and cannot test it, since there every
   neighbourhood offers the same menu, and strong non-vacuity is impossible on that carrier for any
   law and any state-valued fibre map. Yet the cube **does** discriminate the relaxation tick in
   the weak form, 56 of 172 fibres with an exact witness, correcting PR #7919's reading that the
   cube furnishes no discriminator.
3. The cube's conditioned-state map is **not** equivariant under any site unitary for the bare
   permutation action, so the fibred theorem's covariance hypothesis is not verified there and the
   gauge-corrected symmetry operator is an open item.
4. With abundance and the frame import the Born form is a theorem for the continuum law under four
   named conditions and the sentence supplies one of them; abundance and the frame theorem remain
   named prices, unchanged in count.
5. The two drafted sentences are offered as candidate wordings and not as axiom text.

## Reading, Not Theorem

The sentence that would make the Born rule follow has to say: two neighbourhoods that leave a site
in the same state give each possibility the same odds, whatever else is on offer. Said that way it
is not empty, it tells a Born rule from a uniform one inside a single situation, and the emergent
sea obeys it. On the small cube it cannot be tested, because there every situation has the same
menu; on a lattice whose records take continuous values it can, and there, with enough menus on
offer, the Born rule follows. What the sentence does not do is supply the menus, or the symmetry
the rule needs, and those are named.

## Interfaces

**The gauge-corrected symmetry operator.** The bare edge permutation is not the operator the site
carries, and building the gauge-corrected one would decide the cube's status against the covariance
hypothesis. Open. **Abundance.** Named as a property of the law: the continuum law pays it, no
finite record alphabet can, the sentence does not supply it. **The frame import.** The
dimension-three frame-function theorem is named in the 2026-08-09 parent and used the same way here
as context, not recomputed.

## Proof Boundary

Proved: on the continuum law, the exact rational non-vacuity of `MI-fib'` — the two overlapping
ternary supports and their shared possibility, the Born grading's normalisation and agreement, the
adversary's `20/27` against `28/135`, the in-fibre separation of Born from uniform, the invariant
Bloch kernels and the stabiliser at `e_x`; and on the cube, the Born identity over the complete
family with at most four records, the five odds at three records on one menu, the absence of any
fibre with two menus, the fibre census with its 56 tick violations and their largest difference,
the exact witness with its non-degenerate ground states, the 24 induced edge permutations and their
invariance of the sea probabilities, the exact equivariance of the odds map, and the failure of
`|rho_01|` invariance. Not proved: any axiom-side derivation of the Born form; any value of `rho`
or of the fibre parameter; the fibre map, constructed and not derived; abundance, a separate
clause; the dimension-three frame-function theorem, named and not recomputed; the gauge-corrected
symmetry operator, open; menu arities above three; anything about conditions with more than four
records on the cube; and which law the framework runs.

The two negative statements here are exactly these and nothing broader: **strong non-vacuity is
impossible on the cube, because with menus in a single frame the state determines the menu**; and
**the cube's conditioned-state map is not equivariant under any site unitary for the bare
edge-permutation action**. No claim is made that the Born form is underivable or that any route
fails; the second statement leaves the gauge-corrected operator open and says nothing about the
physical symmetry. [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the one-site `M_2(C)`
presentation, a nearest-neighbour-determined and neighbour-varying probability distribution whose
support is the menu, and a readout value fixed by record content alone. It does not state which law
applies, nor that a registered possibility carries one grade across the conditions it can sit in;
no axiom-side Born forcing is claimed and no canonical axiom edit is proposed.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| scaled domain `S` and its menus | declared family | 2026-08-09 parent note | physical eligibility remains open |
| the continuum law and the lattice-dipole fibration | theorem construction | sibling branch note, re-derived here at the declared witness | one law and one map, not a classification |
| dimension-three frame-function theorem | load-bearing mathematical input | named in the parent note | not recomputed here |
| the 2x2x2 cube, its sea and the relaxation tick | emergent carrier | rebuilt inside the runner | one finite carrier, no lattice-wide claim |
| observations, fits, target probabilities | none | not used | n/a |

## Review Record

PR #7919 left the readout price at three items and read the cube as furnishing no discriminator for
a menu-independence clause. This note writes the clause in the form that escapes the vacuity lemma,
shows it has content on the continuum law and separates Born from uniform inside one fibre, and
corrects the cube reading, with an exact witness, while recording that strong non-vacuity is
impossible there. It adds one exact negative statement about the cube's state map, leaving the
fibred theorem's covariance hypothesis unverified on that carrier. It does not advance
current-surface physical Born closure: the law, abundance and the frame import are all still
supplied. An honest-auditor read of the three predicates originally hoped for is that only the
first holds unqualified, the second as an identity rather than a test, and the third under four
conditions rather than two.

Independent audit remains required before the repository may assign any effective claim status.
