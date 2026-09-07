# Finite-Step Gauge-Covariant Matter Current and Operator Work Interface

**Status:** proposed_retained
**Date:** 2026-09-03

**Claim type:** bounded_theorem

**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.

**Direct field-work parent:**
[`U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_EXACT_MIDPOINT_SOURCE_WORK_CLOSED_DIPOLE_PURE_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Conserved-source parent:**
[`U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Photon-tick parent:**
[`U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md)

**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)

**Runner:**
[`scripts/u1_finite_step_matter_current_operator_work_interface_2026_09_03.py`](../scripts/u1_finite_step_matter_current_operator_work_interface_2026_09_03.py)

**Cached receipt:**
[`logs/runner-cache/u1_finite_step_matter_current_operator_work_interface_2026_09_03.txt`](../logs/runner-cache/u1_finite_step_matter_current_operator_work_interface_2026_09_03.txt)

## Result up front

A finite local matter hop supplies exactly the kind of edge current required
by the sourced photon tick, but it is not generally the instantaneous current
`i[H,n]` evaluated at the start of the tick.

For an oriented two-site charged hop with link phase `A`, hopping coefficient
`t`, tail/head number projectors `n_t,n_h`, and

```text
H_b(A)=-t(cos(A) X+sin(A) Y),
V_h(A)=exp(-i h H_b(A)),
```

define the finite-step oriented current by the actual transported charge:

```text
Jbar_h(A)=(V_h^dagger n_h V_h-n_h)/h.
```

Then, as operator identities,

```text
V_h^dagger n_t V_h-n_t=-h Jbar_h,
V_h^dagger n_h V_h-n_h=+h Jbar_h.
```

The current is Hermitian, local to the bond, gauge covariant, reverses sign
with bond orientation, and has the closed form

```text
Jbar_h(A)
 = [sin(2th)/(2h)] [cos(A)Y-sin(A)X]
   +[(1-cos(2th))/(2h)] Z.
```

Its first term tends to the familiar instantaneous current

```text
J_0=i[H_b,n_h]=t[cos(A)Y-sin(A)X],
```

while the `Z` term is the finite transported-charge correction. On a
refinement ladder, `Jbar_h` differs from the current evolved to the temporal
midpoint by `O(h^2)`, but differs from the initial instantaneous current by
`O(h)`. At a resolved tick the correction is large and cannot be silently
dropped.

The construction composes locally. A three-site two-layer hop satisfies exact
continuity at every site. On an `L=4` cubic torus, all `192` positive-axis
bonds split into six matchings by axis and tail parity; every operational
current remains on its two-site bond, the six layers form a unitary tick, and
all `64` vertex continuity equations hold to `3e-14`.

There is also a required operator-ordering correction to the field-work
parent. If `J`, `E`, and `B` are noncommuting Hermitian operators, the exact
field energy change is

```text
Delta H_field
  =(h/4) sum_e {J_e,E_e+E'_e},
```

where `{A,B}=AB+BA`. The unsymmetrized classical product is generally
non-Hermitian and fails the energy identity. When current and field commute,
the anticommutator reduces exactly to the parent's classical midpoint work.

This is a positive matter-light interface result. It removes two hidden join
errors before the branches meet:

1. use the integrated current of each finite matter layer, not an endpoint
   current; and
2. use symmetrized operator work when the current contains noncommuting link
   operators.

It does not yet construct a closed backreacting matter-field tick. The link
phase is supplied during each matter hop, and this note proves the field work
gained but not the equal matter energy lost. The exact remaining target is

```text
Delta H_matter
  =-(h/4) sum_e {Jbar_e,E_e+E'_e}
```

inside one layerwise local, reversible, gauge-preserving update.

## 1. The exact finite-step current

Use the one-particle bond basis

```text
|tail>, |head>.
```

The endpoint projectors are

```text
n_t=(I+Z)/2,               n_h=(I-Z)/2.
```

The oriented link transporter appears through

```text
H_b(A)=-t(cos(A)X+sin(A)Y).
```

Since the Pauli direction squares to identity,

```text
V_h(A)
 =cos(th)I+i sin(th)(cos(A)X+sin(A)Y).
```

Total number is exactly conserved because

```text
n_t+n_h=I.
```

Rather than approximating the transported charge, define the current from
the endpoint difference:

```text
Jbar_h=(n_h'-n_h)/h.
```

The two continuity equations then follow without truncation. Direct Pauli
reduction gives

```text
Jbar_h
 =[sin(2th)/(2h)](cos(A)Y-sin(A)X)
  +[(1-cos(2th))/(2h)]Z.
```

The runner checks the definition, formula, Hermiticity, tracelessness,
unitarity, and both endpoint equations over `5 x 3 x 3=45` phase, hopping,
and step combinations.

The formula is not merely notation. Expanding at small `h` gives

```text
Jbar_h
 =J_0+t^2 h Z+O(h^2).
```

Thus an initial-time insertion of `J_0` misses an order-`h` polarization term
in the current, producing an order-`h^2` charge error per tick. Evaluating the
instantaneous current at the temporal midpoint absorbs the odd correction,
so its current error is `O(h^2)`. The executable observes refinement ratios
of two for the endpoint error and four for the midpoint error.

This is the smallest correction required to connect a continuous Hamiltonian
current to an exact finite-tick Gauss law.

## 2. Gauge covariance and orientation

Let endpoint gauge phases be `alpha_t,alpha_h`. The matter basis transforms by

```text
G=diag(exp(i alpha_t),exp(i alpha_h)),
```

and the link phase by

```text
A' = A+alpha_h-alpha_t.
```

Then

```text
H_b(A')=G H_b(A) G^dagger,
V_h(A')=G V_h(A) G^dagger,
Jbar_h(A')=G Jbar_h(A) G^dagger.
```

The runner checks three nontrivial phase triples. Swapping tail and head and
sending `A -> -A` gives

```text
X Jbar_h(A) X=-Jbar_h(-A).
```

Thus the current has the same oriented-edge transformation required by the
incidence source. Setting `t=0` returns the exact zero operator.

This is a gauge-covariant bond interface. It does not derive which phase or
hopping coefficient the framework selects.

## 3. Layerwise continuity on overlapping hops

For one bond unitary, locality is immediate. On a lattice, adjacent bond
Hamiltonians overlap and cannot all occupy one disjoint circuit layer. The
correct finite-depth construction uses edge colors.

The runner first uses an open chain

```text
0 -- 1 -- 2
```

with the `0->1` hop followed by the `1->2` hop. Let `V_1,V_2` be the two
unitaries. The first current is represented in the initial frame. The second
is local on sites `1,2` when it is executed; if both increments are written
in the initial Heisenberg frame, it is pulled back through `V_1`:

```text
J_12^(initial)=V_1^dagger J_12^(operational) V_1.
```

The exact final changes are

```text
Delta n_0=-h J_01,
Delta n_1= h J_01-h J_12^(initial),
Delta n_2= h J_12^(initial).
```

All three matrices agree with direct conjugation by `V_2 V_1`. Updating the
two electric link operators by the same layer currents preserves

```text
d0^T E-n
```

at every vertex.

There is an important locality distinction. `J_12^(operational)` has support
only on sites `1,2`; its initial-frame representative has nonzero `0,2`
matrix element after the first hop. Therefore an implementation that first
aggregates every current in the old-time frame expands support. The positive
local construction updates the corresponding field source after each colored
matter layer.

For an even periodic cubic lattice, color every positive-axis edge by

```text
(axis, tail-coordinate parity).
```

There are six colors. On `L=4`, each color contains `32` disjoint edges and
covers all `64` vertices exactly once; the colors cover all `192` oriented
bonds. The runner assigns nonuniform deterministic phases and hopping
coefficients, builds all six block-diagonal unitaries, transports each
operational current through its actual prefix, and checks continuity at all
`64` vertices.

This is an explicit lattice-wide finite-depth compiler for exact charge
transport. It is not yet the complete matter-plus-photon circuit because the
field shear and matter energy backreaction still need to be interleaved.

## 4. Operator-valued field work

The field-work parent used commuting real coordinates. A gauge-invariant
matter current can contain link operators and therefore need not commute with
the electric field. The ordering cannot be guessed by copying the classical
formula.

Write the field energy with its symmetric numeric coefficient matrix:

```text
H_h=(1/2) x^T M x.
```

This expression is Hermitian even for noncommuting Hermitian components
because `M` is real symmetric. The sourced update remains a numeric linear
map

```text
x'=U x+R J.
```

Expanding without commuting `x` through `J` gives

```text
Delta H
 =(1/2) sum_ij M_ij[(Ux)_i(RJ)_j+(RJ)_i(Ux)_j]
  +(1/2)(RJ)^T M(RJ).
```

The same coefficient identities proved by the classical parent reduce this
to

```text
Delta H
 =(h/4) sum_e [J_e(E_e+E'_e)+(E_e+E'_e)J_e]
 =(h/4) sum_e {J_e,E_e+E'_e}.
```

The runner instantiates all three electric and magnetic components with
noncommuting Pauli combinations and puts an actual integrated bond current in
the source vector. The operator residual is below `3e-15`. The result is
Hermitian.

As an adversarial control it evaluates the left-ordered classical expression

```text
(h/2) sum_e J_e(E_e+E'_e).
```

That operator differs from the true energy change by more than `0.04` and
from its own adjoint by more than `0.08`. The missing anticommutator is a
physical operator-ordering error, not cosmetic notation.

When every field and current is a scalar multiple of identity, the runner
recovers the classical midpoint law exactly. It also evaluates the operator
identity in a nontrivial complex matter state and obtains equal expectation
values.

## 5. What this does to the matter-light pincer

Open PR #7892 reports an instantaneous conserved current for the emergent
fermion. Open PR #7903 reports a compact-link matter/gauge coupling. They are
context-only pointers in this source: neither branch is imported as proof
authority.

The present theorem states the finite-tick interface those sources must meet.
For each local colored hop:

1. compute or realize the integrated current from the actual unitary charge
   transfer;
2. apply that current to the corresponding oriented electric link in the same
   operational layer;
3. preserve `d0^T E-rho` exactly; and
4. make the matter sector lose the anticommutator work gained by the field.

Items 1-3 are positive here for a generic gauge-covariant charged hop. Item 4
is the remaining energy-backreaction join. This is narrower and more useful
than the prior statement “matter current must couple to Maxwell.” It exposes
the temporal averaging, layer schedule, and operator ordering that determine
whether the join is actually valid.

## 6. Program and axiom boundary

No axiom update is implied. The minimal axioms leave the transition law,
hopping coefficient, link phase, and Hamiltonian supplier open. The approved
kinetic primitive normalizes spacetime form but does not select the bond
unitary or its field coupling.

The result is nevertheless positive TOE-directed science. At source level,
the following pieces now share one exact interface language:

- local gauge-covariant matter transfer;
- finite-step conserved charge/current;
- layerwise electric Gauss preservation;
- sourced transverse photon dynamics; and
- Hermitian operator field work.

What remains is not “find a current.” It is construct one joint reversible
matter-field layer whose matter energy changes by the negative operator work,
then compile its finite field payload and Record observables.

## 7. Executable evidence

The runner reports `TOTAL: PASS=24 FAIL=0`. It checks:

- `45` bond phase/hopping/step combinations for unitarity, conservation,
  endpoint continuity, Hermiticity, and the analytic current formula;
- endpoint-versus-midpoint refinement orders and a resolved finite-step
  correction;
- endpoint gauge covariance, orientation reversal, and the zero-hop control;
- a two-layer overlapping three-site schedule;
- exact Gauss-residual preservation with integrated link currents;
- operational versus initial-frame current support;
- all six matchings and all `192` bonds on an `L=4` cubic torus;
- continuity at all `64` torus vertices;
- noncommuting anticommutator field work;
- failure and non-Hermiticity of the unsymmetrized product;
- the commuting classical limit; and
- a nontrivial state expectation value.

## No-Go Discipline Gate

The positive interface includes a negative control on endpoint current and
unsymmetrized work. This gate keeps those failures inside their exact scope.

### N1 — Alternative route enumeration

| Honesty | Route | Outcome |
|---|---|---|
| **ATTEMPTED** | current from exact endpoint charge difference | **Positive:** exact finite-step continuity and analytic local current; checks 1-5. |
| **ATTEMPTED** | initial instantaneous current | First-order current error on the refinement ladder; useful only as an infrared approximation; checks 6-8. |
| **ATTEMPTED** | temporal-midpoint instantaneous current | Positive second-order approximation, but not the exact finite current; check 6. |
| **ATTEMPTED** | layerwise edge coloring | **Positive:** local six-layer cubic tick with exact vertex continuity; checks 12-19. |
| **ATTEMPTED** | aggregate all currents in the old-time frame | Continuity survives algebraically but support spreads across prior layers; check 17. |
| **ATTEMPTED** | anticommutator operator work | **Positive:** exact Hermitian field-energy change; checks 20-21 and 24. |
| **ATTEMPTED** | left-ordered classical work | Fails and is non-Hermitian for noncommuting fields; check 22. |
| **OPEN** | joint gauge-link backreaction layer | Must make matter lose the exact anticommutator work while retaining locality and reversibility. |

### N2 — Wall-independence audit

Use

```text
W1 = exact matter energy backreaction,
W2 = compact finite field payload,
W3 = interleaved matter/field layer schedule,
W4 = Record preparation and readout,
W5 = coupling normalization and charge selection.
```

The following motivations do not prove both directions of every pairwise
non-implication. Those logical relations remain unresolved; no independent
wall count or stronger exclusion follows. The positive constructions and
partial witnesses elsewhere in this note retain their stated domains.

| Pair | Relation established? | Existing motivation, not an independence proof |
|---|---:|---|
| W1, W2 | unresolved | an unbounded rotor can exchange exact energy without a finite compiler |
| W1, W3 | unresolved | a global energy-preserving map need not have a local layer schedule |
| W1, W4 | unresolved | energy balance does not form a Record |
| W1, W5 | unresolved | opposite work fixes matching, not the physical coupling value |
| W2, W3 | unresolved | finite payload does not itself supply a collision schedule |
| W2, W4 | unresolved | a finite Hilbert carrier and outcome readout are distinct |
| W2, W5 | unresolved | payload dimension does not set electric charge |
| W3, W4 | unresolved | local scheduling does not select registered outcomes |
| W3, W5 | unresolved | edge coloring does not normalize the coupling |
| W4, W5 | unresolved | readout does not fix interaction strength |

### N3 — Hidden-wall scan

The matter calculation is the one-particle sector of a supplied two-site
hopping Hamiltonian. The link phase is external. The `L=4` torus is even so
the six parity matchings exist. Numerical tolerances test analytic operator
identities. Currents are operationally local layer by layer; their aggregated
initial-frame representatives are explicitly not called local. The field
work theorem uses the parent's linear weak-field metric. No actual emergent
fermion code, compact-link PR, Record event, or finite field payload is
silently imported.

### N4 — Residual matching

| Surface | Residual | Match here |
|---|---|---|
| exact-work parent | matter current and opposite matter work absent | **positive partial closure:** finite matter current and operator field work; opposite matter work remains |
| conserved-source parent | current supplied as a c-number | **positive extension:** current now comes from exact unitary charge transfer |
| matter current context | continuous instantaneous current | **interface correction:** integrated current required at finite step |
| compact gauge context | link operator may not commute with E | **interface correction:** anticommutator work required |
| minimal axioms | transition law not selected | **unchanged:** bond hop remains supplied physics |

### N5 — Rhetoric and resolution audit

“Exact” refers to the unitary definition, endpoint differences, continuity,
Gauss residual, and operator algebra. “Lattice-wide” refers to the explicit
`L=4`, 64-vertex, 192-bond colored schedule and the general even-cubic coloring
construction. “Local” refers to the operational layer, not every current
pulled back to the initial Heisenberg frame. The endpoint and ordered-product
failures are not generalized into no-go statements about other integrators or
joint Hamiltonians.

The cache contains all five resolution lines:

```text
per_element: the oriented bond phase, finite current, and operator anticommutator coefficients are checked
per_site: exact tail/head continuity and each operational two-site current support are checked
per_mode: instantaneous, midpoint, and integrated current orders are separated on a refinement ladder
per_block: one-bond gauge covariance, three-site colored continuity, Gauss preservation, and operator work are checked
lattice_wide: the layerwise construction generalizes by finite edge coloring; no global solve or all-at-once current is used
```

### N6 — Partial-closure paths and primitive check

The approved kinetic primitive supplies no matter current or ordering rule.
The shortest positive route is a local backreaction layer on one bond, tested
first in the joint charge-one sector: make its matter Hamiltonian change by
the negative anticommutator work, then compose it with the six-color schedule.
An exact continuous-time local Hamiltonian is a second route but would reopen
the already identified finite-tick locality distinction. A discrete-gradient
or collision-model layer is a third route. None demands an axiom edit before
construction is attempted.

### N7 — Steelman

A hostile reviewer should object that defining current from transported charge
makes continuity tautological. It does. The nontrivial content is the explicit
local formula, its gauge/orientation behavior, its finite-step difference from
`i[H,n]`, and its successful composition across overlapping lattice layers.
Those are exactly the points a matter-to-field compiler can get wrong.

The reviewer should also object that the link phase is external and total
energy is not yet conserved. That objection survives. This is an interface
theorem, not a completed coupled theory. The next test must dynamize the link
and close opposite matter work.

### N8 — Cross-cycle echo

Earlier source cycles correctly matched classical continuity but could have
invited an invalid direct substitution of a continuous current operator into
a finite tick. This cycle catches that mismatch before integration. It also
extends the exact classical work identity rather than assuming commuting
matter/link operators. The explicit left-ordered failure prevents a symbolic
name match from being mistaken for a quantum energy theorem.

**Gate result:** PASS for the bounded finite-step current and operator-work
interface. Seven route variants are executed, the strongest positive compiler
is explicit, and the one remaining energy-backreaction route stays open.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- the bond unitary is not unitary or fails total charge conservation;
- the integrated current fails either endpoint continuity equation;
- the analytic current formula, gauge covariance, or orientation rule fails;
- endpoint and midpoint refinement orders do not separate as stated;
- an operational colored-layer current has off-bond support;
- any of the three-site or 64-site continuity equations fails;
- the integrated current fails to preserve the electric Gauss residual;
- anticommutator work differs from the operator field-energy change;
- the anticommutator work is non-Hermitian;
- the left-ordered control accidentally satisfies the noncommuting identity;
  or
- the commuting operator limit fails to recover classical midpoint work.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_finite_step_matter_current_operator_work_interface_2026_09_03.py
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
conditional_surface_status: "Supplied one-particle two-site hopping Hamiltonian with external link phase, fixed step, even periodic coloring and layerwise prefix pullbacks; anticommutator work uses the supplied linear field metric and does not construct joint quantum field backreaction."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The result is a conditional mathematical theorem on supplied laws and finite domains; author status and a green runner grant no audit retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original source and receipts remain recoverable at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. The full imported helper closure
is declared. The finite current, prefix-support boundary and operator-work
identity are preserved; the wall table no longer claims unproved independence.
All runner timeouts and final input-bound receipts describe this corrected
source. The source status and trace above state the supplied premises and open
physical bridge. Independent review confirmation and integration validation
remain separate; no audit verdict or effective retained status is asserted.
