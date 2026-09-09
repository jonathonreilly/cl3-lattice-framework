---
claim_id: born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
claim_type: bounded_theorem
claim_scope: "Conditional one-site finite-dimensional theorem. A menu-independent grading on the scaled rank-one and scalar-identity effects in M_2(C), normalized on every binary and ternary nonzero resolution of the identity, has a unique density-matrix trace form on that scaled domain. The proof lifts the rank-one grading to a nonnegative normalized frame function on C^3 and applies the standard dimension-three frame-function theorem. The grading, eligible-menu family, physical registration, and selected density matrix remain explicit inputs or outputs of a supplied law; no canonical axiom is changed."
upstream_dependencies:
  - minimal_axioms
  - gleason_on_qubit_lattice_projection_lattice_narrow_theorem_note_2026-05-20
runner: scripts/born_form_binary_ternary_scaled_projector_frame_lift_2026_08_09.py
---

# Born Form From Binary And Ternary Scaled-Projector Menus By A One-Ancilla Frame Lift

**Date:** 2026-08-09
**Type:** bounded_theorem
**Scope:** conditional one-site mathematics on an explicitly supplied grading
and eligible-menu family.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/born_form_binary_ternary_scaled_projector_frame_lift_2026_08_09.py`](../scripts/born_form_binary_ternary_scaled_projector_frame_lift_2026_08_09.py)
**Runner cache:**
[`logs/runner-cache/born_form_binary_ternary_scaled_projector_frame_lift_2026_08_09.txt`](../logs/runner-cache/born_form_binary_ternary_scaled_projector_frame_lift_2026_08_09.txt)

## Result Up Front

At one `M_2(C)` site, normalization on every binary and ternary
scaled-projector menu is sufficient to force the Born trace form on the
scaled-projector domain. Menus with four or more outcomes are not used.

The proof is a one-ancilla reduction. Compress every orthonormal basis of
`C^3=C^2 direct_sum C` onto its first two coordinates. The three compressed
rank-one projections are scaled rank-one qubit effects summing to `I_2`.
Either all three are nonzero, giving a ternary menu, or exactly one is zero,
giving a binary menu. The supplied grading therefore becomes a nonnegative
normalized frame function on `C^3`. The standard dimension-three
frame-function theorem makes that function quadratic. Its value on the pure
ancilla direction is zero, so positivity deletes the ancilla row and column
and leaves a unique qubit density matrix.

This resolves the positive mathematical question recorded in
`docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md` as "prove ternary
scaled-projector sufficiency or find a rogue," when "ternary" means the
maximum-arity surface containing binary and ternary menus. It does not prove
that the current framework physically registers that menu family or grading.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: born_form_scaled_projector_arity_three_threshold
target_blocker_text: "prove ternary scaled-projector sufficiency or find a rogue"
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Derive or physically register the distribution-to-effect-grade identification/functionality and the eligible binary-and-ternary menu family."
conditional_surface_status: "exact theorem conditional on a supplied menu-independent grading, binary-and-ternary menu eligibility, and the standard dimension-three frame-function theorem"
hypothetical_axiom_status: "candidate consequence map only; no canonical axiom edit"
admitted_observation_status: null
claim_type_reason: "The finite-dimensional implication is exact, but its grading and physical menu-registration premises are not supplied by the four axioms and the named frame theorem remains an explicit mathematical input."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Inputs

Work at one site, with `H=C^2`. For each unit vector `n in R^3`, write

`P(n)=(I+n dot sigma)/2`.

Define the scaled domain

`S={cP(n): 0<=c<=1, |n|=1} union {cI:0<=c<=1}`.

A menu is a finite family of nonzero members of `S` summing to `I`. The
conditional inputs are:

1. **Effect functionality.** A function `w:S->[0,1]` has `w(0)=0` and
   `w(I)=1`; its value depends on the effect, not on a menu containing it.
2. **Low-arity eligibility.** Every two- or three-member menu is normalized:
   `sum_j w(E_j)=1`.
3. **Standard frame theorem.** Every nonnegative weight-one frame function on
   a complex Hilbert space of dimension at least three is represented by a
   unique density operator. The theorem statement and its present repository
   application surface are recorded in
   [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md).

The exact claim proved here is:

> There is a unique density matrix `rho in M_2(C)` such that
> `w(E)=Tr(rho E)` for every `E in S`.

The standard frame theorem is named rather than hidden. The new mathematical
content is the exact compression from the restricted qubit menu family to its
dimension-three hypotheses and the ancilla-block elimination. Relative to the
campaign's stricter no-literature-import contract, this is an advance rather
than a self-contained completion.

## Proof-Obligation Graph

| Obligation | Role | Disposition |
|---|---|---|
| scalar coins have value `w(cI)=c` | identity branch | proved below from binary and ternary coin menus |
| every lifted basis compresses to an eligible menu after zero removal | frame construction | proved below by the top-block completeness identity |
| the lifted function is nonnegative and normalized on every basis | frame hypothesis | proved below from the range and low-arity inputs |
| the lifted frame function is quadratic | representation | named standard dimension-three frame theorem; explicit mathematical input |
| zero ancilla value removes cross terms | descent to `M_2(C)` | proved below from positivity |
| the resulting qubit operator is a unique density matrix | conclusion | proved below from positivity, trace one, and rank-one separation |

The named frame theorem is stronger than the restricted qubit target and is
consumed openly as an upstream standard theorem. Accordingly, this artifact is
a bounded downstream theorem rather than a self-contained proof of the
campaign's stricter native target. The nontrivial new reduction proves that the
much smaller qubit binary-and-ternary scaled family supplies exactly the frame
hypotheses; no near-closure claim is based on merely renaming the stronger
theorem.

## Coin Linearity

Set `f(c)=w(cI)`. Binary coin menus give

`f(c)+f(1-c)=1`.

For positive `a,b` with `a+b<1`, compare the ternary coin menu
`{aI,bI,(1-a-b)I}` with the binary coin menu
`{(a+b)I,(1-a-b)I}`. Their common remainder cancels:

`f(a)+f(b)=f(a+b)`.

The endpoint and zero cases follow from `f(0)=0`, `f(1)=1`, and the binary
identity. Nonnegativity makes `f` monotone. Rational iteration and a rational
squeeze therefore give

`w(cI)=f(c)=c` for every real `c in [0,1]`.

## One-Ancilla Frame Lift

Let `pi:C^3->C^2` be projection onto the first two coordinates. For a unit
vector `u in C^3`, define

`E_u=|pi u><pi u|`, and `F(u)=w(E_u)`.

If `pi u` is nonzero, then

`E_u=cP` with `c=||pi u||^2 in (0,1]`;

if `pi u=0`, then `E_u=0`. Thus `F` is defined everywhere, lies in `[0,1]`,
and depends only on the ray of `u`.

Let `{u_1,u_2,u_3}` be any orthonormal basis of `C^3`. Completeness gives

`sum_i E_{u_i}=pi (sum_i |u_i><u_i|) pi^dagger=pi I_3 pi^dagger=I_2`.

The kernel of `pi` is one-dimensional, so at most one `E_{u_i}` is zero.

- If none is zero, the three effects form an eligible ternary menu.
- If one is zero, the two remaining nonzero effects form an eligible binary
  menu, and the removed value is `F(u_i)=w(0)=0`.

Consequently

`sum_i F(u_i)=1`

for every orthonormal basis. `F` is a nonnegative normalized frame function on
`C^3` with no continuity, measurability, differentiability, or countable
additivity premise added.

## Quadratic Representation And Ancilla Elimination

By the named dimension-three frame theorem, there is a unique positive
operator `R on C^3` with `Tr(R)=1` and

`F(u)=<u|R|u>`.

Let `e_3=(0,0,1)`. Since `pi e_3=0`,

`0=w(0)=F(e_3)=<e_3|R|e_3>`.

Write `R=B^dagger B`. Then the last expression is `||B e_3||^2`; hence
`B e_3=0` and therefore `R e_3=0`. Hermiticity removes the corresponding row
as well, so

`R=rho direct_sum 0`

for a positive `rho on C^2` with `Tr(rho)=1`.

For any unit qubit vector `psi` and `c in [0,1]`, choose

`u=(sqrt(c) psi, sqrt(1-c))`.

Then `E_u=c|psi><psi|` and

`w(c|psi><psi|)=F(u)=<u|(rho direct_sum 0)|u>
                  =c<psi|rho|psi>
                  =Tr(rho c|psi><psi|)`.

Together with coin linearity, this proves the trace formula on all of `S`.
Rank-one qubit projectors span the Hermitian matrices, so two density matrices
with these values agree; `rho` is unique.

## Boundary And Degenerate Cases

- **Binary menus are load-bearing.** A lifted basis containing the pure
  ancilla vector compresses to a binary qubit menu plus zero. The theorem is
  about maximum arity three, not exactly-three-nonzero normalization alone.
- **Zero effects are not menu members.** Zero is used only as the fixed endpoint
  `w(0)=0` after compression. The original menus retain the landed nonzero
  convention.
- **Repeated outcomes and collinear ternaries are included.** The proof uses
  only the operator sum and does not require distinct rays.
- **Complex phases are included.** `E_u` is unchanged by the global phase of
  `u` or by the relative phase of its ancilla coordinate.
- **No four-outcome schema is used.** In particular, the same-ray split menu
  used by the all-finite scaled-family proof is absent.
- **The domain remains `S`.** No value is claimed for a qubit effect having two
  distinct nonzero eigenvalues.

## Independent Adversarial Checks

The runner verifies exact rational or symbolic instances of the compression,
the zero-to-binary edge, a Fourier trine, and the ancilla deletion. It also
checks an exact hostile control: the prior smooth cubic binary grading gives
`5/4`, rather than `1`, on the trine with Bloch directions

`e_z`, `(sqrt(3)/2,0,-1/2)`, and `(-sqrt(3)/2,0,-1/2)`

and coefficient `2/3` on each effect.

A separate exact modular-rank check takes the isosceles menu with coefficients
`(3/4,5/8,5/8)`, rotates it through 1,000 deterministic rational rotations,
and tests every odd sphere-polynomial section through total degree nine at its
two radii. The constraint matrix has 110 columns, exact rank 107 modulo the
prime 1,000,003. The runner separately verifies that the three independent
radius-weighted linear Born vectors lie in the rational kernel. Those vectors
give rational rank at most 107, while the nonzero modular minor gives rational
rank at least 107; hence the rational nullity is exactly three and the
surviving modes are exactly the linear Born modes. This finite polynomial
certificate is an adversarial diagnostic, not the no-regularity proof; the
named frame theorem supplies the general step.

## Relation To The Current Axioms

[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
one-site algebraic possibility presentation `M_2(C)`. Its August 5
Admissibility sentence says that a probability distribution over local
possibilities is determined by, and varies with, nearest-neighbor conditions.
The theorem above instead begins with an explicitly typed effect grading and
an eligible family of effect menus. Those are declared conditional inputs in
this note. No inference of impossibility is made: a later operational theorem
could still derive them from Record dynamics or other landed structure.

If the owner elects an axiom-side closure rather than a derivation-side
closure, the narrow sufficient candidate is:

> For each site and nearest-neighbor condition, the Admissibility distribution
> extends to a menu-independent grading `w` on the one-site scaled-projector
> domain. Every binary and ternary nonzero scaled-projector resolution of the
> identity is an eligible local menu and its grades sum to one.

This is hypothetical wording, not an edit, recommendation, or adopted
primitive. Under it, the theorem derives a unique local density matrix
`rho(neighbors)` and the Born form `w(E)=Tr(rho E)` on `S`. The existing
nearest-neighbor determination then determines `rho` by uniqueness. The
candidate still does not supply physical occurrence, record-formation site or
rate, an actual member, frequency typicality, arbitrary-effect merging, or the
functional dependence of `rho` on neighbor data.

The candidate contains two scientifically distinct theorem clauses that
should not be hidden inside the word "distribution":

1. the Admissibility distribution is extended to a grade on registered scaled
   effects, and equal scaled effects receive equal grades across local
   registrations;
2. every binary and ternary scaled resolution is eligible and normalized.

Whether either piece can be derived is the next constructive science target.

## No-Go Discipline Gate For The Axiom Boundary

This gate is included because the note names conditional premises and maps a
hypothetical axiom consequence. The theorem is positive. The gate does not
turn a scope boundary into a non-derivability claim.

### N1 — materially distinct closure routes

| Route | What was attempted | Exact result and authority | Marker |
|---|---|---|---|
| Direct Admissibility reading | Identify the canonical possibility distribution itself with `w` on effects. | The current text names an `M_2(C)` possibility domain and a probability measure over possibilities, but it does not type registered outcomes as effects or quantify over effect resolutions; compare [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), Qubit and Admissibility. This is a textual premise mismatch, not a theorem that no derivation exists. | **ATTEMPTED** |
| Record-additivity lift | Use scalar additivity over disjoint records to generate all binary and ternary effect-frame equations. | Record additivity quantifies over finite collections of pairwise-disjoint records. The prior frame-extension analysis keeps the all-frame extension constructive and open; see [`READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md`](READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md), the conditional frame-extension and gap sections. | **ATTEMPTED** |
| Physical ternary dilation | Use an actual one-site contact instrument to supply the full menu family. | The physical-contact construction supplies one trine and a larger bounded compiler, while preserving effect functionality, eligibility, and normalized grading as explicit premises; see [`work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md`](work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md), the conditional Born statement. This is strong partial closure, not a universal registration theorem. | **ATTEMPTED** |
| Composite projective frame | Move to a neighboring composite and apply projective Gleason before restricting back to one site. | The composite route closes mathematically after a full frame-function extension is supplied, but the extension remains its named conditional input; see the linked readout-frame note. It therefore changes the carrier without deriving the registration premise. | **ATTEMPTED** |
| Barycenter/evaluation map | Average local matrix possibilities and evaluate effects against the average. | Writing `w(E)=integral Tr(sigma E) dmu(sigma)` already chooses density-matrix possibilities and the trace evaluation kernel. It is a valid consequence once those structures are supplied, but it inserts the representation being sought rather than deriving the effect grade from the present words. The type distinction is explicit in [Exact Target And Inputs](#exact-target-and-inputs). | **ATTEMPTED** |

The five routes differ in primary object and terminal obligation: axiom text,
record scalar functional, physical dilation, composite projection frame, and
state/effect duality. None supports a broad no-go. The physical-dilation and
Record routes remain constructive successors.

### N2 — wall independence and collapse

For the narrow axiom-consequence map, the candidate contains two walls:

- **effect-grade identification/functionality:** the Admissibility distribution
  induces a grade on registered scaled effects, with one grade attached to the
  same effect across registrations;
- **low-arity eligibility:** every binary and ternary scaled resolution is a
  normalized menu.

| Pair | First closes second? | Second closes first? | Collapsed disposition |
|---|---:|---:|---|
| effect-grade identification/functionality / low-arity eligibility | no: a grade can exist without declaring any counterfactual menu eligible | no: menus can be available while their outcomes lack a distribution-derived, context-independent effect grade | two independent conditional clauses |

The density operator is not a third wall; the theorem derives it after these
two clauses and the standard frame theorem. Occurrence, formation, frequency,
and arbitrary-effect merging are outside the target rather than extra walls
inside it.

### N3 — hidden-condition scan

| Phrase or construction | Classification |
|---|---|
| "standard frame theorem" | explicit named mathematical input, linked and listed in the obligation graph |
| "scaled-projector domain" | explicit conditional domain, defined before the theorem |
| "menu-independent" and "eligible" | the two exposed conditional clauses; neither is attributed to Record or Admissibility |
| top-block projection `pi` | constructed finite-dimensional map, with its completeness identity proved |
| positivity of `R` | conclusion of the named nonnegative frame theorem, used explicitly for ancilla deletion |
| "current axioms" | exact text comparison to the linked canonical file, not session memory |
| candidate axiom wording | hypothetical governance option; no adoption, necessity, or effective status asserted |

No observation, fitted value, continuity assumption, countable extension,
physical measurement context, or selected density matrix is hidden.

### N4 — citation-to-residual matching

| Citation | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:43-73` | exact one-site possibility and probability-distribution wording | only the textual baseline, not an effect-grade derivation | yes |
| `docs/GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md:123-155` | nonnegative normalized frame representation in dimension three | the lifted mathematical representation step | yes |
| `docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md:282-301,397-414` | binary scaled control and the explicit ternary-scaled frontier question | provenance and exact target only | yes |
| `docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md:89-110,422-448` | physical effect/dilation construction | partial physicalization only; functionality and eligibility remain premises | yes |
| `docs/READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md:157-185` | Record-to-all-frame route | conditional composite representation and an open constructive successor | yes |

No cited artifact is used to claim more than the row states.

### N5 — rhetoric and resolution audit

The risky sentence family is "the current axioms do not supply X." This note
uses the narrower form "the canonical text does not state the typed
effect-grade identification/functionality and low-arity menu clauses," then
leaves derivation from other structure open.

| Resolution | Tested here? | Honest statement |
|---|---:|---|
| per element | yes | the theorem grades each element of the declared scaled domain; the axiom text does not name that effect typing |
| per site | yes | the theorem is one-site and the axiom supplies a per-site possibility distribution, without the two typed clauses |
| per mode | finite hostile diagnostic only | odd polynomial modes through degree nine are checked; general modes are handled by the named frame theorem |
| per block | one theorem block only | no claim about every record/dynamics block |
| lattice-wide | no | no lattice-wide registration or impossibility statement is made |

The primary runner cache emits the required substantive `per_element`,
`per_site`, `per_mode`, `per_block`, and `lattice_wide` execution lines.

### N6 — partial closure and primitive scan

The approved primitive registry was checked before the axiom-pressure wording.
The scale-reference primitive concerns units, kinetic isotropy concerns the
structural kinetic form, and the realized-state primitive permits pointwise
specialization. None is counted as a wall, and none is repurposed as a
probability-form selector.

Live partial-closure routes are:

1. Admissibility already supplies existence, nearest-neighbor determination,
   and variation of a local probability distribution.
2. The physical-contact construction already supplies genuine effects and a
   bounded forcing-complete dilation basis on a supplied physical code.
3. An event/effect registration plus operational-equivalence theorem could
   derive the distribution-to-grade map and same-effect functionality across
   programs.
4. A recurrent local compiler plus a lawful occurrence/Record interface could
   derive menu eligibility rather than register it.
5. An owner decision could adopt the displayed sufficient clause directly;
   this is a governance route, not evidence that it is necessary.

### N7 — hostile steelman

> The axiom proposal may be premature. Admissibility now already contains a
> neighbor-determined, neighbor-varying probability measure; Qubit supplies
> `M_2(C)`; Record supplies content-determined scalar readout; and the physical
> contact work already constructs a forcing-complete finite dilation basis.
> A successful event/effect registration and operational-equivalence theorem
> could turn the Admissibility distribution into a grade and identify equal
> effects across those programs, while a recurrent Record compiler could make
> the relevant menus eligible. That constructive route would derive both
> clauses without changing the axioms. The present theorem should therefore
> advertise the candidate only as a sufficient fallback and make that
> registration/equivalence bridge the next terminal obligation.

This steelman is accepted. No "new axiom required" conclusion is shipped.

### N8 — cross-cycle echo

| Earlier wall | Later movement | Could the mechanism apply here? |
|---|---|---|
| probability distribution existence was formerly outside the minimal wording | the 2026-08-05 owner revision put existence, neighbor determination, and variation into Admissibility | yes; an owner revision could add typed effect structure, but that is not the only route |
| full effect/scaled menu families were abstract conditional inputs | the physical-contact cycle constructed one actual trine and a bounded forcing-complete compiler | yes; physicalization has already narrowed the registration wall once |
| realized-record additivity did not provide a full composite frame | the frame-extension note kept operational derivation and registration as separate live routes | yes; the one-ancilla theorem lowers the mathematical family needed but does not retire that constructive program |

Cross-cycle history argues against a broad no-go: previously open interfaces
have narrowed by both owner wording and physical construction.

**Gate disposition:** PASS for the narrow factual claim that the displayed two
clauses are sufficient and are not literally stated in the present canonical
wording. FAIL / DO NOT SHIP for any claim that an axiom change is necessary,
that Record dynamics cannot derive the clauses, or that all physical Born
routes are exhausted.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| `M_2(C)` one-site possibility presentation | carrier context | current Qubit axiom linked above | supplied algebraic presentation |
| scaled-effect grading and functionality | theorem premise | explicit in this note | physical registration remains a constructive target |
| all binary and ternary scaled menus | theorem premise | explicit in this note | physical eligibility remains a constructive target |
| dimension-three frame theorem | load-bearing mathematical theorem | named local theorem record linked above | native re-proof is not attempted here |
| density matrix `rho` | theorem output | unique representer | its neighbor-data law is not computed |
| observations, fits, target probabilities | none | not used | not applicable |

The result is conditional support for the Born-form lane and direct closure of
the named mathematical frontier question. It is not current-surface physical
Born closure and does not change any axiom, foundation, primitive, registry,
policy, queue, or audit record.

## Review Record

The source question left scaled ternary sufficiency open. This note adds the
one-ancilla frame lift and preserves the exact boundary between mathematical
forcing and physical registration. The exactly-three-only surface, smaller
proper subsets of ternary menus, arbitrary qubit effects, menu occurrence, and
the local neighbor-to-density law are not classified.

Independent audit remains required before the repository may assign any
effective claim status.
