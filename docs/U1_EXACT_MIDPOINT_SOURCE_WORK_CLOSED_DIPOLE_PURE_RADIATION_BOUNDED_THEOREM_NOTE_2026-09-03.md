# Exact Midpoint Source Work and a Closed-Dipole Pure Radiation Packet

**Status:** proposed_retained
**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct source parent:**
[`U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Photon-tick parent:**
[`U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Physical role compiler:**
[`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)

**Runner:**
[`scripts/u1_exact_source_work_closed_dipole_radiation_2026_09_03.py`](../scripts/u1_exact_source_work_closed_dipole_radiation_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/u1_exact_source_work_closed_dipole_radiation_2026_09_03.txt`](../logs/runner-cache/u1_exact_source_work_closed_dipole_radiation_2026_09_03.txt)

## Result up front

The sourced local photon tick has an exact finite-step work law. Write its
positive modified field energy as

```text
H_h(E,B)
  =(1/2)(||E||^2+||B||^2)
   -(h^2/8)||C E||^2.
```

For one sourced update

```text
B^(1) =B +(h/2) C E,
E'    =E -h C^T B^(1)+h J,
B'    =B^(1)+(h/2) C E',
```

the energy change is exactly

```text
H_h(E',B')-H_h(E,B)
  =h J^T (E+E')/2.
```

This is not a small-step approximation. At `h=1/2`, the runner proves the
cross and quadratic parts as integer matrix identities on the complete
`162`-field block. The equality also holds in deterministic full-field
trials and reduces to the parent's exact conservation law when `J=0`.

The work identity gives a direct radiation experiment. Start from no charge
and no field. Apply one edge current `J` for one tick, then apply `-J` on the
same edge for the next tick. With `J_e=1/h`, the first tick creates a unit
positive/negative nearest-neighbor charge pair and the second returns every
vertex charge to zero. The field does not return to zero. It is

```text
E_2=-h^3 C^T C J,
B_2= h^2 C J -(h^4/2) C C^T C J.
```

Therefore `E_2` is co-curl, `B_2` is curl, both Gauss laws hold, and neither
field has a constant harmonic component. The source has made a temporary
electric dipole, closed it, and left only a nonzero transverse field packet.
By the photon-tick parent's spectrum, that packet is a superposition of its
two propagating photon branches rather than a residual Coulomb field.

For `h=1/2` and the unit nearest-neighbor dipole, the residual modified field
energy is exactly `1/2`, equal to the accumulated midpoint source work. On an
`L=20` sparse role lattice, eight subsequent source-free cycles keep that
energy fixed to `2e-13`, advance the exact nonzero-support radius through
`3,5,...,19`, move the squared-field centroid monotonically from the source,
and leave less than `0.2%` of squared field amplitude inside radius three.

This closes a second source-level electromagnetic question: the conserved
current does not merely satisfy Gauss and make a static Coulomb field. A
closed, charge-conserving local history emits an energy-carrying transverse
wave packet under the same finite-depth law.

It still does not derive a matter current, quantize the field, construct a
detector Record, fix the electric charge or fine-structure constant, or prove
a compact finite-payload matter-field unitary. The exact work equation now
states what a successful joint matter-field compiler must satisfy:

```text
Delta H_matter = -h J^T (E+E')/2
```

for a closed isolated tick, with the same orientation and staggering.

## 1. Algebra of the exact work identity

Let

```text
a=h/2,
M_E=I-a^2 C^T C,
M=diag(M_E,I),
H_h(x)=(1/2)x^T M x,
x=(E,B).
```

The source-free tick is `x_0'=U_h x` and obeys

```text
U_h^T M U_h=M.
```

Adding `J` in the electric full-step changes the final state by

```text
R_h J=(h J,a h C J).
```

Thus

```text
x'=U_h x+R_h J.
```

The energy change has one cross term and one quadratic source term:

```text
Delta H
 =x^T U_h^T M R_h J
  +(1/2)J^T R_h^T M R_h J.
```

Using the last magnetic half-step gives

```text
M_E E_0'+a C^T B_0'
 =E_0'+a C^T B^(1),
```

and the electric update gives

```text
(E+E')/2
 =E_0'+a C^T B^(1)+(h/2)J.
```

Meanwhile

```text
R_h^T M R_h=h^2 I.
```

Combining the cross and quadratic pieces yields

```text
Delta H=h J^T(E+E')/2.
```

At `h=1/2`, the runner removes all denominators:

```text
U=U_num/32,
M=M_num/16,
R=R_num/8,
R_num=(4I,C)^T.
```

It verifies the two independent integer identities

```text
U_num^T M_num R_num
 =32(32 P_E^T+U_num^T P_E^T),

R_num^T M_num R_num=256 I,
```

where `P_E` selects the electric coordinates. These are the coefficientwise
statement of the work theorem for every old field and every current on the
named block.

The sign is the source parent's incidence convention. Positive `J` increases
the field by `+hJ`; an isolated matter supplier must lose the same work. No
claim is made that a separately stipulated source conserves total energy.

## 2. A charge excursion that ends with no charge

Start with

```text
rho_0=0,                    E_0=0,                    B_0=0.
```

Use the source history

```text
J_0=J,                      J_1=-J.
```

The exact continuity rule gives

```text
rho_1=h d0^T J,
rho_2=rho_1-h d0^T J=0.
```

For one oriented edge with `J_e=1/h`, `rho_1` is `-1` at the tail and `+1`
at the head. The runner checks the complete vertex vector, not only total
charge.

The first field update is

```text
E_1=hJ,
B_1=(h^2/2) C J.
```

At the start of the second electric step,

```text
B^(1)_second=h^2 C J.
```

The reverse current cancels the direct electric insertion, but it cannot
cancel the curl field that evolved during the intervening tick. Direct
substitution produces

```text
E_2=-h^3 C^T C J,
B_2=h^2 C J-(h^4/2)C C^T C J.
```

The runner evaluates both the two-step trajectory and this formula and finds
them componentwise identical at `h=1/2`.

Applying `J` and `-J` simultaneously is the zero-source control and leaves
zero field. Reversing the pulse orientation reverses every field component
and preserves the energy. The residual packet is therefore caused by the
one-tick time separation, not a static source, floating offset, or hidden
background.

## 3. Why the residual field is radiation in this model

The incidence identities give

```text
d0^T E_2=-h^3 d0^T C^T C J=0,
d2 B_2=0.
```

More strongly,

```text
E_2 in image(C^T),          B_2 in image(C).
```

The longitudinal electric sector is `image(d0)`, and

```text
image(d0) perpendicular image(C^T)
```

because `C d0=0`. The three torus-constant electric and magnetic modes are
also absent: the executable groups fields by their actual edge orientation
and face normal and obtains zero sum in all six groups over integers.

The residual state therefore has no charge, no longitudinal Coulomb field,
and no harmonic zero mode. Every surviving component lies in the nonzero
curl sector. The direct photon parent proves that this sector has exactly two
positive and two negative finite-tick phases at every nonzero lattice
momentum, corresponding to two real transverse polarizations.

“Pure radiation packet” is used in that precise linear-field sense. The note
does not infer photon-number eigenstates, a quantum vacuum, spontaneous
emission rates, or detector clicks.

## 4. Exact energy left by the unit dipole

For the tested `h=1/2` and `J_e=2`, write the final state over denominator
`32`:

```text
E_num=-4 C^T C J,
B_num= 8 C J-C C^T C J.
```

With `M=M_num/16`, the runner computes over integers

```text
x_num^T M_num x_num=16384.
```

Since

```text
H=(1/2)(x_num/32)^T(M_num/16)(x_num/32),
```

the energy is exactly

```text
H_2=16384/32768=1/2.
```

The two midpoint work terms sum to the same `1/2`. This is useful beyond the
particular source: it makes energy exchange a coefficient-level join
criterion. A proposed matter update that supplies the same edge current but
does not lose this amount is not yet a closed matter-field dynamics.

## 5. Local propagation after the source closes

The executable independently builds a sparse `L=20` physical curl with
`24,000` edge and `24,000` face variables and `96,000` signed incidence
entries. At `L=3` its site ordering and dense matrix are exactly identical to
the role compiler, preventing a second discretization from silently entering
the large-volume control.

After the two source ticks, eight source-free cycles give

```text
support radius: 3,5,7,9,11,13,15,17,19.
```

All are before the radius-20 wrap boundary. The modified energy remains
`1/2` to `2e-13` throughout. As a separate location diagnostic, the runner
weights each edge and face by its squared raw field amplitude. That centroid
moves outward strictly at every sampled cycle, and the fraction within
physical Manhattan radius three falls from `1` to less than `0.002`.

Squared raw amplitude is not labeled an exactly conserved local energy
density; the exact conserved scalar is `H_h`, whose curl correction is local
but can redistribute density conventions. The propagation claim is the
combination of exact support, exact global energy, and the explicitly named
amplitude-location diagnostic.

## 6. Reversal and cubic covariance

For a prescribed current, one sourced step is inverted by using `-h` with
the same current:

```text
U_{-h,J} U_{h,J}=I
```

when the magnetic half-steps and source insertion are reversed in their
palindromic order. Starting from the final packet, the runner reverses the
two source values in time order with `-h` and returns every field component
to exact zero.

For every signed permutation `R`, transform

```text
s -> R s,
E -> R E,
J -> R J,
B -> det(R) R B.
```

The runner checks all 48 transforms at generic and axial symbols. Both the
driven field and the scalar midpoint work covary. Thus neither the radiation
mechanism nor its energy exchange selects a preferred cubic axis.

## 7. Program significance and the next join

The light stack now has, at source level:

1. a role-compiled local gauge measure;
2. the minimal conservative Maxwell generator;
3. a finite-depth reversible photon tick;
4. conserved vertex charge and edge current;
5. the static lattice Coulomb field;
6. an exact field/source work law; and
7. a closed charge history that leaves a causal transverse radiation packet.

This is substantial classical weak-field closure. It is still a supplied-law
chain rather than an axiom derivation, and its official audit status is
unchanged.

Open PR #7892 reports a local conserved current for the emergent fermion, and
open PR #7903 reports a compact-link gauge coupling. Those are context-only
pincer surfaces here: their code and conclusions are not imported as
authority. Once available on one common source base, the high-value test is
not merely to identify both symbols as `J`. It is to show, in one reversible
joint update, all three equations

```text
Delta rho=d0^T(hJ),
Delta H_field=h J^T(E+E')/2,
Delta H_matter=-Delta H_field.
```

Passing those with the same local hop would close charge, Gauss, and energy
exchange at once. Failure would identify the exact staggering or coupling
coefficient that needs revision.

## 8. Prior-art boundary

Finite-difference Maxwell radiation is standard, beginning with K. S. Yee,
[“Numerical solution of initial boundary value problems involving Maxwell's
equations in isotropic media”](https://doi.org/10.1109/TAP.1966.1138693)
(1966). The source parent names additional local cellular-automaton Maxwell
precedents.

This note does not claim a new radiation law. Its repo-specific theorem is
that the exact modified-energy invariant of this particular finite-depth
role-compiled tick has the midpoint work law, and that its exact incidence
source can execute a closed Record-sized dipole history leaving only the
already classified photon sector.

## 9. Executable evidence

The runner reports `TOTAL: PASS=22 FAIL=0`. It checks:

- the exact incidence complex;
- the two integer matrix identities constituting the source-work theorem;
- deterministic full-field work controls and the zero-source limit;
- unit dipole creation and exact charge return;
- the componentwise closed-pulse formula;
- both final Gauss laws, transverse images, and absence of harmonic fields;
- exact rational packet energy and equality to accumulated work;
- exact reversed-history recovery and orientation reversal;
- sparse/dense compiler identity;
- eight-cycle large-volume energy conservation, support, centroid, and
  near-source departure;
- all 48 cubic transformations; and
- simultaneous-current cancellation as the temporal-separation control.

## No-Go Discipline Gate

This is a positive theorem with named unclosed joins. The gate prevents those
joins from turning into unsupported impossibility claims.

### N1 — Alternative route enumeration

| Honesty | Route | Outcome |
|---|---|---|
| **ATTEMPTED** | exact metric expansion | **Positive:** integer cross/quadratic identities and actual full-field trials give midpoint work, including the source-free reduction. |
| **ATTEMPTED** | closed one-edge dipole history | **Positive:** charge closure, exact curl/co-curl residual, no harmonic field and exact half-unit work/energy checks. |
| **ATTEMPTED** | reversed and simultaneous source histories | **Positive controls:** the reverse-time history returns to vacuum; simultaneous opposite pulses cancel rather than radiate. |
| **ATTEMPTED** | large sparse propagation | **Positive:** sparse incidence comparison and the eight-cycle energy, support-radius, centroid and near-source amplitude checks. |
| **ATTEMPTED** | cubic work covariance | **Positive:** the actual driven field and midpoint work agree under all 48 cubic transformations. |
| **OPEN** | local matter hop supplies `J` and loses opposite work | Direct end-to-end pincer target; not assumed from another open PR. |
| **OPEN** | local Poynting-density convention | Global work is exact; no unique local energy-density/flux split is selected here. |
| **OPEN** | compact finite-payload quantum implementation | Needed beyond the real weak-field field coordinates. |
| **OPEN** | Record preparation and detector absorption | Emission field exists; outcome statistics and clicks are not compiled. |

### N2 — Wall-independence audit

Use

```text
W1 = reversible matter-current energy join,
W2 = compact finite-payload quantum compiler,
W3 = local energy-density and flux convention,
W4 = Record source preparation and detector readout,
W5 = coupling and unit normalization.
```

The following motivations do not prove both directions of every pairwise
non-implication. Those logical relations remain unresolved; no independent
wall count or stronger exclusion follows. The positive constructions and
partial witnesses elsewhere in this note retain their stated domains.

| Pair | Relation established? | Existing motivation, not an independence proof |
|---|---:|---|
| W1, W2 | unresolved | a classical joint symplectic law could balance work without a finite qubit payload |
| W1, W3 | unresolved | global matter/field energy balance does not select one local flux density |
| W1, W4 | unresolved | a conserved reversible current does not select a registered event |
| W1, W5 | unresolved | work balance fixes matching coefficients, not their physical value |
| W2, W3 | unresolved | a quantum compiler need not choose a classical density convention |
| W2, W4 | unresolved | unitary payload and Record formation remain distinct |
| W2, W5 | unresolved | finite payload does not determine electric charge |
| W3, W4 | unresolved | local flux bookkeeping does not create a detector outcome |
| W3, W5 | unresolved | a Poynting convention does not set alpha |
| W4, W5 | unresolved | readout does not normalize the coupling |

### N3 — Hidden-wall scan

The theorem uses real linear fields, periodic blocks, supplied `h=1/2`, an
external current history, and the parent's positive local metric. The exact
work algebra is finite-block but coefficientwise. The propagation diagnostic
uses an `L=20` torus before radius-20 wrap, and squared amplitude is not called
the exact local energy. “Radiation” means the source-free nonzero curl sector
of the proved tick, not a quantized photon count or experimental detector
signal.

### N4 — Residual matching

| Surface | Residual | Match here |
|---|---|---|
| conserved-source parent | accelerated source, radiation, and energy exchange open | **positive partial closure:** closed dipole radiates and field work is exact |
| photon-tick parent | source-free positive metric | **exact reuse:** same metric and homogeneous evolution |
| radius-one raw-unitary boundary | no minimal raw-coordinate unitary transport | **unchanged:** finite-depth field map used |
| matter-current PR context | current exists on another open source branch | **not imported:** joint energy loss remains to be executed |
| minimal axioms | no dynamics or Hamiltonian selector | **unchanged:** supplied downstream law |

### N5 — Rhetoric and resolution audit

“Exact” refers to the displayed finite matrices, continuity, field formula,
Gauss laws, rational energy, and reversal. “Pure radiation” refers to absence
of charge, longitudinal field, and harmonic field inside the parent's linear
mode classification. “Outward” refers to the named squared-amplitude centroid
on `L=20`. No claim extends to photon quantization, spontaneous emission,
continuum Lorentz symmetry at the cutoff, detector records, compact dynamics,
or an axiom derivation.

The cache contains all five resolution lines:

```text
per_element: each source coefficient, incidence sign, and exact work numerator is checked
per_site: one edge pulse creates and erases charges only on its two neighboring vertices
per_mode: the residual field lies in curl/co-curl images with no longitudinal or harmonic component
per_block: exact work, Gauss laws, reversal, cubic covariance, and dipole controls are checked
lattice_wide: an L=20 sparse block conserves energy and carries the packet from support radius 3 through 19
```

### N6 — Partial-closure paths and primitive check

The approved kinetic primitive supplies no current or work coefficient. The
shortest positive continuation is to put the matter current and this field
tick on one source base and prove opposite work in the matter sector. A
secondary path derives a local Poynting balance for a declared density split.
A third compiles source preparation and absorption into Record events. None
requires an axiom edit before these explicit joins are attempted.

### N7 — Steelman

A hostile reviewer should say that a prescribed two-tick classical current is
an antenna input, not matter. Correct. It proves that the field law has a
coherent radiation response and a sharp work ledger; it does not prove the
framework creates that source. The reviewer should demand the actual fermion
hop, the same edge orientation, opposite matter work, and a joint reversible
map. Those demands define the next test rather than invalidate this bounded
field theorem.

The reviewer can also reject squared-amplitude motion as Poynting flux. The
note agrees: it uses that quantity only as a location diagnostic and does not
claim a unique local flux law.

### N8 — Cross-cycle echo

The previous light cycles progressively removed false blockers: a nonlocal
exact exponential did not prevent a local split tick, and failure of a strict
raw-unitary block did not prevent positive field dynamics. This cycle follows
the positive source route and keeps the same distinction. It also avoids a
repeated program error in which matching a current symbol is treated as a
joint theory: the new midpoint identity makes opposite matter work an
independent terminal obligation.

**Gate result:** PASS for the scoped positive work and radiation theorem.
Five distinct proof/control route families are executed, four enlarged joins remain open, and no
remaining wall is stated as a no-go.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- either exact integer source-work matrix identity is nonzero;
- a sourced full-field trial violates midpoint work;
- the first pulse does not create only the neighboring unit dipole;
- the reverse pulse leaves any vertex charge;
- the two-step field differs from the displayed curl/co-curl formula;
- either final Gauss law fails or a harmonic component remains;
- the residual packet is zero or its exact energy differs from `1/2`;
- accumulated work differs from residual field energy;
- reverse-time source history fails to return the field to zero;
- the sparse curl differs from the role compiler;
- source-free packet energy drifts beyond the stated tolerance;
- the support or centroid fails the named `L=20` ladder; or
- source work changes under a cubic signed permutation.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_exact_source_work_closed_dipole_radiation_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=22 FAIL=0
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
conditional_surface_status: "Supplied real linear sourced Yee tick and its modified field metric; exact work algebra, with positive photon energy on the parent CFL domain, and the declared two-pulse history and finite sparse propagation trials; no matter loss law or detector Record is constructed."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The result is a conditional mathematical theorem on supplied laws and finite domains; author status and a green runner grant no audit retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original source and receipts remain recoverable at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. The route evidence map now
includes the actual cubic work-covariance check and identifies exact check
names. Unproved pairwise implications among open tasks are left unresolved.
All runner timeouts and final input-bound receipts describe this corrected
source. The source status and trace above state the supplied premises and open
physical bridge. Independent review confirmation and integration validation
remain separate; no audit verdict or effective retained status is asserted.
