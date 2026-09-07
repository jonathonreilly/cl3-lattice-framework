# Conserved Vertex Charge and Edge Current Join Coulomb to the Local Photon Tick

**Status:** proposed_retained
**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct dynamics parent:**
[`U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Minimal-radius decision boundary:**
[`U1_RADIUS_ONE_ONSITE_UNITARY_MINIMAL_MAXWELL_TICK_BOUNDED_NO_GO_NOTE_2026-09-03.md`](U1_RADIUS_ONE_ONSITE_UNITARY_MINIMAL_MAXWELL_TICK_BOUNDED_NO_GO_NOTE_2026-09-03.md)

**Physical role compiler:**
[`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)

**Runner:**
[`scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py`](../scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/u1_conserved_source_coulomb_photon_bridge_2026_09_03.txt`](../logs/runner-cache/u1_conserved_source_coulomb_photon_bridge_2026_09_03.txt)

## Result up front

The source-free parent carried two local transverse photon branches, but did
not show how charge and current join that field. There is a direct positive
extension on the same vertex-edge-face-cube incidence complex.

Put charge `rho` on vertex roles, current `J` on edge roles, electric field
`E` on edge roles, and magnetic field `B` on face roles. Let `d0` be the
vertex-to-edge incidence and `C` the edge-to-face curl. For a supplied step
`h`, use

```text
B^(1)   = B^n     + (h/2) C E^n,
E^(n+1) = E^n     - h C^T B^(1) + h J^n,
B^(n+1) = B^(1)   + (h/2) C E^(n+1),
rho^(n+1) = rho^n + h d0^T J^n.
```

The current sign is an incidence convention: positive current on an oriented
edge transfers positive charge from its tail vertex to its head vertex.
With the electric Gauss condition

```text
d0^T E^n = rho^n,
```

the sourced tick gives

```text
d0^T E^(n+1) = rho^(n+1)
```

exactly. Magnetic Gauss is preserved during each magnetic half-step. Total
charge is conserved on a periodic lattice. A one-edge current pulse moves one
unit of charge to the neighboring vertex with no bookkeeping repair.

The same construction supplies the static and propagating pieces of weak-field
electromagnetism in one lattice language.

- At fixed neutral charge, minimizing `||E||^2/2` gives
  `E=d0 phi` and the cubic-lattice Poisson equation
  `d0^T d0 phi=rho`.
- Its periodic Green function is axis-cubic and approaches
  `1/(4 pi r)`. Fit errors decrease across the named `L=48,64,96,128` ladder; the `L=128`
  fitted coefficient is within `0.9%` of `1/(4 pi)`.
- Gradient currents occupy the longitudinal Coulomb sector. Co-curl currents
  are divergence-free and occupy the transverse photon sector. The two are
  orthogonal by `C d0=0`.
- At every generic nonzero Fourier symbol, the curl-coupled source projector
  has rank two, matching the two photon polarizations proved by the parent.
- A local edge-current impulse has a strict finite support cone under the
  three-layer update, and the sourced law covaries under all 48 cubic signed
  permutations.

This is a meaningful positive bridge: the previously source-free light
candidate now has exact local continuity, Gauss coupling, the Coulomb sector,
and the transverse photon sector in one executable law.

It is not yet a derivation of electromagnetism from the four axioms. The
current is supplied rather than derived from the matter construction; the
charge unit and electromagnetic coupling are not selected; the fields remain
real, linear, and weak; accelerated-source radiation and Record readout are
not established here; and no compact interacting qubit circuit is claimed.

## 1. Exact cochain identities

The physical-role compiler realizes the doubled cubic incidence chain

```text
vertices --d0--> edges --C--> faces --d2--> cubes
```

with

```text
C d0 = 0,                  d2 C = 0.
```

Every `d0` row joins two neighboring vertex roles through one edge role.
Every `C` row reads the four edge roles around a face role. In the doubled
physical lattice those incidence partners are one physical nearest-neighbor
step apart.

Define the electric charge represented by a field configuration as

```text
rho_E=d0^T E.
```

Only the electric shear and its onsite source change `E`. Therefore

```text
d0^T E^(n+1)
 = d0^T E^n - h d0^T C^T B^(1) + h d0^T J^n
 = rho_E^n + h d0^T J^n,
```

because `d0^T C^T=(C d0)^T=0`. Updating registered charge by the same
incidence continuity equation keeps electric Gauss exact.

For magnetic Gauss,

```text
d2 B^(1)=d2 B^n+(h/2)d2 C E^n=d2 B^n,
d2 B^(n+1)=d2 B^(1)+(h/2)d2 C E^(n+1)=d2 B^(1).
```

On a periodic lattice the all-ones vertex vector is in the kernel of `d0`.
Thus

```text
sum rho^(n+1)-sum rho^n
 =h 1^T d0^T J
 =h (d0 1)^T J
 =0.
```

The runner verifies these identities over integers at `h=1/2` on the full
`L=3` incidence block, not by comparing rounded trajectories.

## 2. A local charge-transfer event

Take an oriented edge `e=(tail -> head)` and set

```text
J_e=1/h,                   J_other=0.
```

Then

```text
h d0^T J = -delta_tail + delta_head.
```

One tick removes one unit from the tail and places it at the neighboring
head. A distant opposite spectator charge keeps the periodic block neutral.
The executable checks the complete vertex vector exactly.

This is a kinematic source event. It does not yet show that a fermion hop
produces this `J`, nor that Record selects the hop with a derived rate. Those
are now sharply stated join obligations rather than missing definitions of
charge or current.

## 3. Static energy selects the lattice Coulomb field

For a neutral vertex charge `rho`, minimize

```text
H_E(E)=(1/2) E^T E
```

subject to

```text
d0^T E=rho.
```

Introducing a vertex multiplier `phi` gives

```text
E=d0 phi,
(d0^T d0) phi=rho.
```

The constant mode of `phi` is gauge and is fixed to zero mean. The runner
solves this equation on the complete `L=3` block and reconstructs the input
neutral charge to numerical tolerance.

Any constraint-preserving variation `z` obeys `d0^T z=0`, including co-curl
variations `z=C^T a` and the torus harmonic sector. Then

```text
(d0 phi)^T z=phi^T d0^T z=0.
```

So

```text
H_E(E+delta E)=H_E(E)+(1/2)||delta E||^2.
```

The Poisson field is therefore the unique minimum-energy field in its Gauss
sector; adding a nonzero harmonic field also raises the energy. The executable
checks the orthogonality with a nonzero deterministic curl variation, while
the displayed identity covers the complete constraint kernel.

For a unit source neutralized by the periodic background, the scalar Green
function satisfies

```text
L G = delta_0 - 1/L^3,
L=d0^T d0.
```

Its Fourier denominator is

```text
lambda(k)=4 sum_i sin^2(k_i/2).
```

The code constructs all `L^3` Fourier entries, removes only the constant
mode, and inverse-transforms. For each of `L=48,64,96,128` it checks the
Poisson residual and zero mean. It also verifies equality on the three
coordinate axes. Fitting the on-axis window to

```text
G(r)=a/r+b+c/r^3
```

gives a coefficient `a` whose relative errors against `1/(4 pi)` decrease
strictly across the four sizes and reach less than `0.009` at `L=128`.

This establishes the lattice-to-infrared Coulomb shape and normalization in
the runner's dimensionless field units. It does not determine the physical
charge quantum, fine-structure constant, dielectric normalization, or meter
conversion. The Green-function inverse characterizes or initializes the
static solution; it is not an operation performed by the local time-update
law.

## 4. Longitudinal Coulomb and transverse photon sectors

Two exact source families expose the split:

```text
J_L=d0 f,                  J_T=C^T a.
```

They obey

```text
C J_L=0,
d0^T J_T=0,
J_L^T J_T=f^T d0^T C^T a=0.
```

Thus `J_L` changes the vertex charge and populates the longitudinal electric
field, while `J_T` changes no charge and directly excites the curl sector.
The torus also has harmonic currents; they are not mislabeled as either local
exact or local coexact sources.

At a generic nonzero lattice symbol `s`, define

```text
P_L=s s^T/|s|^2,           P_T=I-P_L.
```

Then `rank(P_T)=2`, `C(s)P_L=0`, and `C(s)P_T=C(s)`. The runner checks these
identities at generic and axial symbols. Together with the direct parent's
phase calculation, this means a general conserved source decomposes into a
nonpropagating Coulomb constraint sector and exactly two propagating
curl-coupled photon sectors.

This is a field-level Hodge decomposition. “Photon” still names the two
transverse normal-mode branches of the supplied linear tick; quantized photon
number, Fock structure, and detector clicks are not proved by this note.

## 5. Locality, covariance, and reversibility boundary

The source insertion `h J` is onsite on the same edge role as `E`. Charge
continuity is a vertex-star sum of its incident edge currents. The two
magnetic half-steps and one electric full-step retain the parent's physical
nearest-neighbor layer structure.

Starting from zero field and one edge-current impulse, the first complete
cycle has support at periodic physical Manhattan distance at most one from
the source edge. One subsequent source-free cycle reaches distance at most
four. The exact number reflects the half/full/half layer schedule; the key
claim is a finite causal cone, not continuum Lorentz invariance at the cutoff.

Under a signed permutation `R`, use

```text
s -> R s,
E -> R E,
J -> R J,
B -> det(R) R B.
```

The sourced Fourier tick covaries for all 48 signed permutations, including
reflections. Current and electric field are polar; magnetic field is axial.

For prescribed `J`, the update is affine. The homogeneous field map remains
the exactly reversible parent tick, but an externally fixed source history is
not itself a closed reversible dynamical system. Reversibility of a joint
matter-field update requires the matter variables that generate `J`; it is
not inferred from this forced-field calculation.

## 6. What was and was not selected

The construction uses no new axiom. It supplies a candidate law inside the
freedom that the minimal-axioms document leaves open. Specifically:

- incidence and the role geometry supply the chain identities;
- the source-free parent supplies the finite-depth Maxwell tick;
- positive electric energy supplies the static Poisson minimizer; and
- a conserved edge current supplies the source insertion.

None of those steps makes the source current emerge from Admissibility or
Record. The kinetic primitive fixes a spacetime normalization form; it does
not select this field payload, coupling, or leapfrog schedule.

The shortest high-value continuation is therefore a matter-current join:
given a local charged matter hop, construct the same edge `J`, prove the joint
matter-field Gauss generator is preserved, and test energy exchange and
reversibility. A driven-radiation check is useful next evidence, but cannot by
itself retire the supplied-current wall.

## 7. Prior-art boundary

The finite-difference curl staggering and leapfrog idea are standard and are
not claimed as new numerical electrodynamics; see K. S. Yee,
[“Numerical solution of initial boundary value problems involving Maxwell's
equations in isotropic media”](https://doi.org/10.1109/TAP.1966.1138693)
(1966). Local cellular-automaton constructions with Maxwell sectors also
exist, including [*Quantum Cellular Automaton Theory of
Light*](https://arxiv.org/abs/1407.6928) and the Maxwell discussion in
[*Free Quantum Field Theory from Quantum Cellular
Automata*](https://arxiv.org/abs/1601.04832).

The repo-specific result is the exact composition of four previously separate
obligations on its role-compiled one-qubit-site geometry: local sourced tick,
incidence continuity, Gauss preservation, and the Coulomb/transverse split.
It is an existence and integration theorem for this program, not a claim to
have discovered Maxwell's equations.

## 8. Executable evidence

The runner reports `TOTAL: PASS=19 FAIL=0`. It checks:

- the full vertex-edge-face-cube incidence complex;
- exact integer electric continuity and both magnetic half-step constraints;
- total charge conservation and the source-free parent reduction;
- exact one-edge transfer of one unit of charge;
- the finite-block Poisson solve and minimum-energy orthogonality;
- periodic Green functions at `L=48,64,96,128`, including cubic axes and the
  infrared `1/(4 pi r)` coefficient;
- exact longitudinal/co-curl source separation;
- rank two of the nonzero transverse Fourier projector;
- the finite impulse support cone; and
- all 48 cubic transformations with the correct polar/axial assignments.

## No-Go Discipline Gate

This is a positive theorem, but it names several walls. The gate keeps those
unclosed joins from being rhetorically promoted into impossibility claims.

### N1 — Alternative route enumeration

| Honesty | Route | Outcome |
|---|---|---|
| **ATTEMPTED** | vertex charge plus edge-incidence current | **Positive:** exact integer continuity and both Gauss rows, actual nonzero-current full-field numerators, and the actual one-edge coefficient/doubling control. |
| **ATTEMPTED** | static energy minimization and Poisson field | **Positive:** the written whole-kernel minimizer proof, finite neutral solve, and named FFT Green/axis/coefficient checks. |
| **ATTEMPTED** | longitudinal/co-curl Hodge split | **Positive:** exact orthogonality and the named longitudinal, co-curl and transverse-projector checks. |
| **ATTEMPTED** | finite-depth impulse propagation | **Positive:** the actual sourced impulse has the named one-cycle and two-cycle causal support bounds. |
| **ATTEMPTED** | cubic source transformation | **Positive:** actual sourced symbols covary under all 48 polar/axial cubic transformations. |
| **OPEN** | derive `J` from a local charged matter hop | Highest-value joint matter-field obligation; no result is imported from an open matter PR. |
| **OPEN** | compact group-valued source update | Needed beyond the real weak-field branch. |
| **OPEN** | enlarged local unitary with E/B as observables | Possible route around the raw-field unitary boundary; source/readout compiler absent. |
| **OPEN** | driven retarded radiation and flux | Same field law can be tested, but it would not derive the matter source. |

### N2 — Wall-independence audit

Use

```text
W1 = matter derivation of the edge current,
W2 = compact nonlinear gauge interaction,
W3 = onsite finite-payload unitary compiler,
W4 = Record preparation and detector readout,
W5 = physical coupling and unit normalization.
```

The following motivations do not prove both directions of every pairwise
non-implication. Those logical relations remain unresolved; no independent
wall count or stronger exclusion follows. The positive constructions and
partial witnesses elsewhere in this note retain their stated domains.

| Pair | Relation established? | Existing motivation, not an independence proof |
|---|---:|---|
| W1, W2 | unresolved | a conserved matter current can exist in a linear field theory; compactness does not identify its carrier |
| W1, W3 | unresolved | current conservation does not construct a unitary field payload |
| W1, W4 | unresolved | a kinematic current does not select or register an outcome |
| W1, W5 | unresolved | current shape does not fix its charge quantum or coupling |
| W2, W3 | unresolved | a compact classical update need not be an onsite qubit circuit |
| W2, W4 | unresolved | nonlinear gauge closure does not supply records |
| W2, W5 | unresolved | compactness does not determine alpha |
| W3, W4 | unresolved | unitary dynamics and registered outcomes are distinct obligations |
| W3, W5 | unresolved | a compiler does not select physical units |
| W4, W5 | unresolved | measurement/readout does not fix the interaction strength |

### N3 — Hidden-wall scan

The lattice is periodic. Charges are neutral in finite volume. Fields and
sources are real and linear. The step is supplied and set to `h=1/2` in the
finite-block checks. Coulomb convergence is numerical at four named sizes;
the incidence identities are exact. The source history is external. The
torus harmonic sector is present. The theorem does not assume that a fermion
construction already supplies the required current.

### N4 — Residual matching

| Surface | Its residual | Match here |
|---|---|---|
| local photon-tick parent | charged sources and electromagnetic dictionary absent | **positive partial closure:** conserved source, Gauss, Coulomb, and transverse join |
| radius-one raw-unitary boundary | minimal raw E/B complete map cannot transport | **unchanged:** finite-depth field tick used; no raw onsite-unitary claim |
| physical role compiler | spatial edge/face law but no dynamics or source | **exact reuse:** current is onsite on edge roles and constraints use its incidence |
| minimal axioms | no supplied transition law | **unchanged:** sourced tick remains downstream candidate physics |
| kinetic primitive | spacetime normalization but no dynamics selector | **unchanged:** no source coefficient or coupling derived from it |

### N5 — Rhetoric and resolution audit

“Exact” applies to incidence, integer continuity, finite-block charge transfer,
and algebraic projector identities. “Coulomb” applies to the stated periodic
Green function and its measured infrared coefficient. “Photon” imports only
the parent's two transverse field-mode branches. “Local” applies per update
layer and to the finite support cone. No sentence says the four axioms derive
Maxwell, matter, electric charge, alpha, quantization, or Record outcomes.

The cached output carries all five resolution lines:

```text
per_element: every incidence sign, one-edge charge transfer, and source coefficient is checked
per_site: vertex charge, edge current, edge electric field, and face magnetic updates are local
per_mode: longitudinal and rank-two transverse source projectors are checked at generic momenta
per_block: exact continuity, Hodge separation, Poisson minimization, cubic covariance, and causal support are checked
lattice_wide: full incidence blocks and L=48,64,96,128 Green functions recover the three-dimensional Coulomb coefficient
```

### N6 — Partial-closure paths and primitive check

The approved kinetic primitive was read directly. It neither blocks nor
proves this source bridge. The shortest partial closures are:

1. connect one reversible charged matter hop to one oriented edge current;
2. show the field energy change is the negative of matter work in the same
   joint tick;
3. drive a transverse localized source and recover retarded radiation and
   lattice Poynting flux; and
4. compile the resulting observables into finite local possibility payloads
   and Record events.

No axiom update is justified merely by the existence of these open compiler
steps.

### N7 — Steelman

A hostile reviewer should say that this is standard sourced lattice Maxwell,
not a fundamental derivation. That is correct. The scientific value is not a
new Maxwell equation; it is eliminating a program-specific compatibility
doubt. The exact source-free photon tick, the role-compiled one-site geometry,
the charge continuity law, and the static Coulomb field can coexist without a
new axiom or a nonlocal projection.

The reviewer can also object that a supplied classical current smuggles in
the matter law. That objection survives and sets the next terminal
obligation. The note therefore stops at “source bridge” and does not claim an
end-to-end electromagnetic sector.

### N8 — Cross-cycle echo

The immediately preceding cycles first found a source-free Maxwell generator,
then replaced its nonlocal exact exponential with a finite-depth local tick,
then bounded one overly strict raw-unitary implementation. This cycle follows
the positive escape retained by those results rather than treating the strict
radius-one block as a general obstruction. It also avoids the recurring error
of treating a constraint identity as a derived interaction: `C d0=0` protects
Gauss, while the source coefficient and matter current remain supplied.

**Gate result:** PASS for the scoped positive bridge. Five distinct proof/control route
families are executed, four enlarged routes remain open, and no named wall is
promoted into a general no-go.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- `C d0` or `d2 C` is nonzero on the physical incidence block;
- sourced electric Gauss disagrees with the vertex continuity update;
- a magnetic half-step changes magnetic Gauss;
- an oriented unit current fails to transfer one charge tail-to-head;
- the Poisson field is not the minimum-energy field in its neutral Gauss
  sector;
- the periodic Green function fails its Poisson equation or its cubic-axis
  equality;
- the fitted infrared coefficient does not approach `1/(4 pi)` on the named
  size ladder;
- longitudinal and co-curl currents fail to be orthogonal;
- a generic nonzero curl-coupled projector does not have rank two;
- the current impulse outruns the stated finite layer cone; or
- the sourced symbol fails polar/axial covariance under a cubic transform.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=19 FAIL=0
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
conditional_surface_status: "Supplied normalized linear sourced Yee tick on the periodic role incidence complex with real fields, external edge current, neutral charge and chosen time step; finite Coulomb coefficient fits are numerical comparisons, not a derived coupling or asymptotic proof."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The result is a conditional mathematical theorem on supplied laws and finite domains; author status and a green runner grant no audit retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original source and receipts remain recoverable at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. The actual nonzero-current tick is
now compared with independent rational full-field numerators and a charged
one-edge coefficient control. Finite-size fit rhetoric and the
route/implication evidence map are narrowed. All runner timeouts and final
input-bound receipts describe this corrected source. The source status and
trace above state the supplied premises and open physical bridge. Independent
review confirmation and integration validation remain separate; no audit
verdict or effective retained status is asserted.
