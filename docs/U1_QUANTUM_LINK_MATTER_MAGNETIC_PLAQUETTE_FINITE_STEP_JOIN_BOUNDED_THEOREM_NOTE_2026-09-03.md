# Quantum-Link Matter and Magnetic Plaquette Finite-Step Join

**Status:** proposed_retained
**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct backreaction parent:**
[`U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Finite-current parent:**
[`U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_FINITE_STEP_GAUGE_COVARIANT_MATTER_CURRENT_OPERATOR_WORK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Sourceful-photon parent:**
[`U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Reversible-photon parent:**
[`U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)

**Runner:**
[`scripts/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_2026_09_03.py`](../scripts/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_2026_09_03.txt`](../logs/runner-cache/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_2026_09_03.txt)

## Result up front

The exact finite-step matter/electric result survives its first contact with
magnetic curvature. On one square face, four spin-one quantum links and one
charged two-site hop form a `3^4 x 2 = 162` dimensional block in which:

- the electric-matter generator and Wilson magnetic generator separately
  commute with all four vertex Gauss operators;
- the matter layer retains the parent's exact equality among transported
  charge, electric-flux change, electric work, and opposite hopping work;
- the magnetic layer circulates equal signed flux around the face, changes no
  matter charge, and is divergence-free;
- the exact joint exponential is unitary, preserves Gauss, and conserves the
  complete matter-electric-magnetic Hamiltonian; and
- the complete flux change separates exactly into charged transport plus a
  divergence-free face circulation.

This is a positive local junction theorem. Adding the magnetic term produces
no local Gauss or work mismatch.

There is a resolved finite-step consequence. Split the complete generator as

```text
A = H_E + H_hop,              B = H_B,
U_S(h)=exp(-ihA/2) exp(-ihB) exp(-ihA/2).
```

The palindromic tick is exactly unitary, reversible, and Gauss-preserving. It
approaches the exact joint flow with `O(h^3)` one-step error and changes the
simple summed Hamiltonian by `O(h^3)` per step. Its principal Floquet
generator is exactly conserved on the tested branch and obeys

```text
H_F
 = A+B
   +(h^2/24) ([A,[A,B]]+2[B,[A,B]])
   +O(h^4).
```

The quadratic correction contains correlated matrix elements that move the
charge and the magnetic face together. Those entries are absent from `A+B`,
scale as `h^2`, and vanish when either charged hopping or magnetic curvature
is removed. Thus the finite-depth law does not break the matter-light join;
it supplies definite local interaction corrections that an extended law must
either keep as its Floquet energy or suppress by a different time schedule.

For a separate continuous U(1) phase comparison on the same square, replace
each hard-cutoff shift by the scalar `exp(i A_e)`. This supplies the potential

```text
V(A)=kappa[1-cos(A_0+A_1-A_2-A_3)].
```

Its flat-point Hessian is the positive rank-one curl form

```text
kappa b b^T,                 b=(1,1,-1,-1),
```

covariant under all eight square symmetries. This scalar comparison is the
local magnetic block of the parent Maxwell curl energy. It is not a derived
Hessian of the finite quantum-link Hamiltonian: its spin-one shift satisfies
`U^3=0` and has no unit-modulus phase eigenvalues. A state, symbol or limit
bridge from the finite operator to this phase model remains open, as does
the extended-lattice photon question.

## 1. The bounded block

Label the square vertices counterclockwise by `0,1,2,3`. Store the oriented
links as

```text
e_0: 0 -> 1,   e_1: 1 -> 2,   e_2: 3 -> 2,   e_3: 0 -> 3.
```

Every link has flux states `m=-1,0,+1`, with

```text
E|m>=m|m>,
U|m>=|m+1> for m<1,
U|1>=0.
```

The cutoff keeps `[E,U]=U` exactly but makes `U` nonunitary at its top-flux
boundary. This cost is tested rather than hidden.

The one-particle matter factor has states `|0>,|1>` on the bottom edge. With
supplied positive coefficients `g^2,t,kappa`, define

```text
H_E   =(g^2/2) sum_(e=0)^3 E_e^2,
H_hop=-t(U_0 tensor |1><0| + U_0^dag tensor |0><1|),
P     =U_0 U_1 U_2^dag U_3^dag,
H_B   =-(kappa/2)(P+P^dag),
H     =H_E+H_hop+H_B.
```

The hard cutoff is part of the declared model. No infinite rotor, continuum
limit, many-body matter sea, or physical coefficient is inferred.

## 2. One Gauss law covers transport and circulation

Let `n_0,n_1` be the two matter projectors. The four vertex generators are

```text
G_0=-E_0-E_3-n_0,
G_1=+E_0-E_1-n_1,
G_2=+E_1+E_2,
G_3=-E_2+E_3.
```

The runner verifies directly that

```text
[G_v,H_E+H_hop]=0,           [G_v,H_B]=0
```

for every `v`. The charged hop raises `E_0` when matter moves from `0` to
`1`, preserving `G_0,G_1`. The face shift raises `E_0,E_1` and lowers
`E_2,E_3`, preserving the divergence at every corner. Truncation deletes
some boundary moves but does not spoil either commutator.

Under a pure magnetic layer the four flux changes obey the operator identities

```text
Delta E_0=Delta E_1=-Delta E_2=-Delta E_3,
Delta n_0=Delta n_1=0.
```

Under the full exact flow, Gauss conservation gives a sharper decomposition.
If `Delta n_1` is the transported charge and

```text
Q_loop=Delta E_0-Delta n_1,
```

then

```text
Delta E_1=Q_loop,
Delta E_2=-Q_loop,
Delta E_3=-Q_loop.
```

So charge transport and magnetic circulation do not compete for two different
notions of current. They are the longitudinal endpoint-changing and closed
face components of the same Gauss-preserving flux change.

## 3. Exact work survives the magnetic join

During the operational `A=H_E+H_hop` layer, define

```text
E_0'=exp(+ihA) E_0 exp(-ihA),
Jbar=(E_0'-E_0)/h.
```

The runner confirms

```text
h Jbar=n_1'-n_1=-(n_0'-n_0)
```

and that the other three link fluxes are unchanged. The exact work identity is

```text
Delta H_E=(g^2 h/4){Jbar,E_0+E_0'},
Delta H_hop=-Delta H_E,
Delta(H_E+H_hop)=0.
```

This is the parent one-bond theorem embedded without alteration in a magnetic
face. The magnetic generator does not commute with `A`; it is therefore not
silently included in the one-layer work claim. Instead, the complete
Hamiltonian exponential is tested separately and conserves the complete `H`
to numerical diagonalization tolerance.

## 4. The reversible tick and its generated interaction

The local generators overlap, so `[A,B]` is nonzero. The palindromic product

```text
U_S(h)=exp(-ihA/2) exp(-ihB) exp(-ihA/2)
```

is nevertheless exactly unitary, exactly reversed by `h -> -h`, and exactly
Gauss-preserving because every factor has those properties.

On `h=0.16,0.08,0.04,0.02`, halving `h` reduces both the flow error and the
one-step change of the simple `H=A+B` by factors approaching `8`. The
principal logarithm stays far from an eigenphase crossing. Its Hermitian
generator `H_F` commutes with every `G_v`, is exactly invariant under the
tick, and differs from `H` by factors approaching `4` under each halving.

The resolved Baker-Campbell-Hausdorff correction above predicts `H_F` through
quadratic order: the residual falls by factors approaching `16`. More
physically, entries that change matter and at least one of `e_1,e_2,e_3` are
identically zero in the simple `H`, but their largest magnitudes in `H_F` are

```text
1.42330388e-3, 3.53553904e-4, 8.82470787e-5, 2.20529418e-5.
```

They therefore scale quadratically. Setting `t=0` removes them; setting
`kappa=0` makes the split product identical to the exact `A` flow. The effect
is specifically the finite-step interaction between charged hopping and
magnetic circulation, not a logarithm artefact already present in either
sector alone.

This correction remains supported on the one face plus its charged edge in
the tested block. No statement about the range of the exact logarithm after
many overlapping faces is made here.

## 5. Separate continuous-phase Maxwell comparison

Supply continuous link phases and replace the finite nilpotent shift
operators by `U_e -> exp(i A_e)`. This is a different carrier construction,
not a spectral substitution or a proved limit of the 162-state finite face.
Its scalar Wilson energy near the flat connection is

```text
kappa[1-cos(b dot A)]
  =(kappa/2)(b dot A)^2+O(||A||^4),
b=(1,1,-1,-1).
```

Its Hessian `kappa b b^T` has eigenvalues

```text
0,0,0,4 kappa.
```

The three null directions are phase changes that leave the face curl
unchanged; the one positive direction is the face curl. The runner constructs
the signed edge maps induced by all eight symmetries of the square and checks
that each preserves the Hessian. A direct refinement probe confirms the
quartic remainder.

The sourceful and reversible parents establish the extended noncompact curl
complex, transverse modes, Coulomb sector, and finite-speed wave tick in their
own scopes. The finite quantum-link matter junction accepts its operator
plaquette term without violating Gauss, work, or reversible finite stepping.
The separately supplied scalar phase model has the displayed curl Hessian.
No state/symbol/limit map connecting those two results is established here.

## 6. What this changes and what it does not

This removes the immediate local compatibility risk between the two positive
halves of the light campaign:

```text
finite charged current + exact electric backreaction
                         meets
finite magnetic plaquette + reversible local stepping.
```

The result is meaningful because a mismatch here would have forced a change
to the link carrier, current definition, or update architecture before any
extended photon test. No such change is required on the smallest joint block.

The remaining issues include the local operator-to-phase bridge and the
extended physical spectrum: does a finite-payload three-dimensional
quantum-link lattice have a low-energy
transverse branch that converges to the already-proved noncompact photon, and
how do the `O(h^2)` Floquet interactions alter that branch when charged matter
is active? A single face cannot answer that spectral question.

No axiom edit follows from this source. The Hamiltonian, link cutoff,
coefficients, one-particle sector, and palindromic schedule are supplied model
data. Admissibility has not yet been shown to select them, and Record
formation/readout is untouched.

## 7. Program and prior-art boundary

The Hamiltonian structure is the standard compact Hamiltonian lattice-gauge
construction; see J. Kogut and L. Susskind,
[“Hamiltonian formulation of Wilson's lattice gauge
theories”](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.395)
(1975). Symmetric product formulas and their double-commutator corrections are
also standard methodology.

The repo-specific contribution is the exact finite-step junction demanded by
the preceding source/current/backreaction chain: one operational current
simultaneously closes matter continuity and electric work while an overlapping
magnetic layer preserves the same Gauss law, followed by an explicit census
of the generated matter-face Floquet entries.

Open PR #7903 independently constructs compact-link matter, Gauss, electric,
and Wilson terms and studies finite-cluster statics. It is context only here:
no code, numerical result, or conclusion from that PR is an input. This source
instead tests real-time finite-step work, reversible composition, and its
generated interaction on a deliberately smaller block.

## 8. Executable evidence

The runner reports `TOTAL: PASS=24 FAIL=0`. It checks:

- hard-cutoff link algebra and boundary cost;
- Hermiticity and the noncommuting layer overlap;
- all eight layer/Gauss commutators;
- exact magnetic face circulation and unchanged matter;
- exact matter current, spectator links, electric work, opposite hopping
  work, and local energy;
- exact joint unitarity, all four Gauss operators, complete energy, and the
  transport/circulation decomposition;
- palindromic reversal and Gauss preservation;
- cubic one-step energy and flow errors;
- exact Floquet conservation, Gauss, quadratic deviation, and the explicit
  double-commutator expansion;
- correlated-transition scaling and both removal controls; and
- positive rank-one face curvature, all eight square symmetries, and the
  quartic weak-field remainder.

## No-Go Discipline Gate

This is a positive local theorem with a bounded schedule distinction and an
explicitly unexecuted extended-photon question. The gate prevents either from
being inflated into a no-go.

### N1 — Alternative route enumeration

| Honesty | Route family | Outcome |
|---|---|---|
| **ATTEMPTED** | exact unsplit matter-electric-magnetic exponential | **Positive:** unitary, Gauss-preserving, and exactly conserves the complete `H`. |
| **ATTEMPTED** | operational electric-matter layer plus magnetic layer | **Positive:** each preserves Gauss; matter work and face circulation close separately. |
| **ATTEMPTED** | palindromic finite-depth composition | **Positive with resolved cost:** reversible and Gauss-preserving; simple-`H` drift is `O(h^3)`. |
| **ATTEMPTED** | principal Floquet energy | **Positive exact invariant:** gains correlated matter-face terms at `O(h^2)`. |
| **ATTEMPTED** | remove charged hopping | The correlated matter-face entries vanish, identifying their matter dependence. |
| **ATTEMPTED** | remove magnetic curvature | The split tick becomes the exact electric-matter flow, identifying their magnetic dependence. |
| **ATTEMPTED** | separate continuous-phase face expansion | **Positive conditional lemma:** the supplied scalar cosine has the Maxwell curl Hessian; no finite-operator-to-phase bridge is proved. |
| **OPEN** | higher-order symmetric composition | Could move the generated terms to higher order; not tested and not ruled out. |
| **OPEN** | enlarged collision/clock carrier | Could make another simple local energy exact; not tested and not ruled out. |
| **OPEN** | extended quantum-link spectral calculation | Could establish or reject a photon branch; not executed here. |

### N2 — Wall-independence audit

The result leaves four distinct questions, not four asserted obstructions:

```text
W1 = convergence with increasing finite flux payload,
W2 = an extended three-dimensional transverse spectrum,
W3 = global range and interpretation of the exact Floquet generator,
W4 = Admissibility selection and Record realization of the supplied law.
```

The following motivations do not prove both directions of every pairwise
non-implication. Those logical relations remain unresolved; no independent
wall count or stronger exclusion follows. The positive constructions and
partial witnesses elsewhere in this note retain their stated domains.

| Pair | Implication proved? | Independence proved? |
|---|---:|---:|
| W1, W2 | unresolved | unresolved |
| W1, W3 | unresolved | unresolved |
| W1, W4 | unresolved | unresolved |
| W2, W3 | unresolved | unresolved |
| W2, W4 | unresolved | unresolved |
| W3, W4 | unresolved | unresolved |

No wall count or claim of impossibility is inferred from this list.

### N3 — Hidden-condition scan

The link cutoff, coefficients, one-particle matter sector, square geometry,
Hamiltonian, and schedule are declared. “Standard” appears only in the
non-load-bearing prior-art classification. “Background” is not used as a
premise. The framework is not said to provide the law. The parent Maxwell
results are cited only for the already-proved noncompact extended sector; they
do not supply the untested quantum-link spectrum.

### N4 — Residual matching

| Surface | Exact residual there | Match here |
|---|---|---|
| finite-current parent | current is supplied to the field | **closed locally:** the quantum link and matter produce one joint current |
| backreaction parent | magnetic plaquette not joined | **closed locally:** one magnetic face is included in the exact unitary |
| sourceful-photon parent | sources are conserved but external | **partial match:** dynamical charged transport now supplies a local source; the extended lattice is not joined |
| reversible-photon parent | free noncompact field tick | **separate phase-comparison curvature:** no finite-operator Hessian or finite-payload spectrum is imported |
| open PR #7903 | static compact-link matter/gauge block | **different residual:** context only, not evidence for finite-step work |

No prior negative is cited as evidence for a broader negative here.

### N5 — Rhetoric and resolution audit

“The junction closes” means only the tested face block. “Generated
interaction” means the resolved matrix entries of its principal small-step
Floquet logarithm. “Not an extended photon calculation” is a scope statement:
no extended quantum-link spectrum was executed, so no positive or negative
photon verdict is made.

The cached runner contains the required resolution certificate:

```text
per_element: finite electric shifts, charged hopping, and face circulation are checked
per_site: four vertex Gauss generators and exact matter continuity are checked
per_mode: weak-face curl curvature and Floquet refinement orders are resolved
per_block: the 162-state spin-one four-link face plus one charged edge is checked
lattice_wide: the local junction is compatible; photon survival on an extended quantum-link lattice is not claimed
```

### N6 — Partial-closure paths and primitive boundary

No new axiom is required or proposed. The next partial closure is ordinary
model science: first increase the flux payload on symmetry-reduced blocks,
then test the lowest transverse excitation on the smallest periodic
three-dimensional complex that can carry it. Higher-order schedules and an
explicit collision carrier remain alternative time architectures. The
approved kinetic-isotropy primitive supplies a normalization boundary, not
the dynamics, payload, or spectrum used here.

### N7 — Steelman

A hostile reviewer should argue that one plaquette is too small to contain a
photon and that a hard cutoff may qualitatively change the compact theory.
That objection is correct and is why the source makes no photon or convergence
claim. It does not overturn the local theorem: the full 162-state operator
norm checks show exact Gauss, work, and energy identities, including cutoff
boundary states. The actionable route is an extended symmetry-reduced
finite-payload spectrum followed by a payload-refinement ladder.

The reviewer should also argue that a higher-order product could reduce the
Floquet corrections. That route remains explicitly open. The only negative
statement retained is that this particular second-order palindromic product
does not conserve the simple `A+B` exactly on the tested block.

### N8 — Cross-cycle echo

The finite-current parent found that aggregating all colored currents in an
old-time frame expands support; the backreaction parent then kept currents
operational and found cross-bond Floquet entries. This cycle repeats neither
finding as a universal obstruction. It adds the magnetic face, resolves the
leading double commutator, and keeps exact unsplit evolution, higher-order
composition, collision carriers, and extended spectral tests visible as
positive routes. Open PR #7903 likewise shows why a supplied compact
Hamiltonian can exist without yet settling its photon spectrum.

**Gate result:** PASS. Seven distinct route families are executed, three are
left open, and no extended-lattice, finite-payload, or axiom no-go is shipped.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- a layer fails to commute with any displayed Gauss generator;
- the magnetic layer changes matter or fails the signed circulation identity;
- the matter layer's transported charge, flux, or opposite work disagree;
- the unsplit joint exponential is nonunitary or changes full energy;
- the full flux change does not separate into transport plus circulation;
- the palindromic tick is not reversible or Gauss-preserving;
- its flow and simple-energy errors fail the cubic ladder;
- the Floquet generator is not Hermitian, conserved, or Gauss-preserving;
- its deviation, BCH residual, or correlated entries fail their stated
  refinement orders;
- either removal control retains the correlated effect; or
- the separately supplied continuous-phase Hessian is not positive rank one
  and square-covariant.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_quantum_link_matter_magnetic_plaquette_finite_step_join_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=24 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected electromagnetic law, physical matter/field identification and Record preparation/readout remain open."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Review the corrected conditional source and establish the missing physical consumer before claiming framework closure."
conditional_surface_status: "Supplied spin-one hard-cutoff links, one-particle matter and one-face Hamiltonian with stated couplings and schedule; exact finite Gauss/work/Floquet statements, plus a separate continuous-phase scalar Hessian comparison with no operator-to-phase or extended-photon bridge."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The result is a conditional mathematical theorem on supplied laws and finite domains; author status and a green runner grant no audit retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original source and receipts remain recoverable at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. The finite hard-cutoff quantum
face and the separately supplied continuous-phase cosine/Hessian are
explicitly distinguished. No operator-to-phase limit bridge is supplied; the
exact finite Gauss/work/Floquet calculation is preserved. All runner timeouts
and final input-bound receipts describe this corrected source. The source
status and trace above state the supplied premises and open physical bridge.
Independent review confirmation and integration validation remain separate; no
audit verdict or effective retained status is asserted.
