# A Finite-Depth Local Reversible Yee Tick Carries the Maxwell Photon

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source changes no audit
verdict, TOE score, axiom, or approved primitive.
**Direct parent:**
[`U1_MINIMAL_PHYSICAL_NEIGHBOR_CONSERVATIVE_GAUGE_DYNAMICS_UNIQUELY_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_MINIMAL_PHYSICAL_NEIGHBOR_CONSERVATIVE_GAUGE_DYNAMICS_UNIQUELY_MAXWELL_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Physical role compiler:**
[`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
**Runner:**
[`scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py`](../scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_local_reversible_yee_leapfrog_tick_2026_09_03.txt`](../logs/runner-cache/u1_local_reversible_yee_leapfrog_tick_2026_09_03.txt)

## Result up front

The direct parent classified the continuous weak-field generator

```text
dot E = -C^T B,
dot B =  C E
```

inside a declared minimal conservative class, but left an exact local finite
tick open. There is a positive discrete-time construction on the same
role-compiled physical edge/face lattice. For a supplied step `h`, perform

```text
B^(1)   = B^n     + (h/2) C E^n,
E^(n+1) = E^n     - h C^T B^(1),
B^(n+1) = B^(1)   + (h/2) C E^(n+1).
```

This is the staggered Yee/leapfrog update written as three local shears. It
has the following exact properties.

- Every shear reads one site's own field and four opposite-role physical
  nearest neighbors. No global inverse, Fourier transform, projection, or
  hidden coin is used.
- The complete map obeys `U(-h)=U(h)^-1`. With `B -> -B`, it has exact time
  reversal.
- The electric and magnetic Gauss rows are preserved by each shear
  separately, not merely by the product.
- All 48 cubic transformations covary when `E` is polar and `B` is axial
  under reflections.
- For `0<h<1/sqrt(3)`, the map conserves the positive local quadratic form

  ```text
  H_h(E,B)
    = (1/2)||B||^2
      +(1/2)||E||^2
      -(h^2/8)||C E||^2.
  ```

- At lattice momentum `k`, with

  ```text
  s_i=2 sin(k_i/2),
  theta_h(k)=2 asin(h |s|/2),
  ```

  at nonzero momentum the physical spectrum has two positive and two negative
  transverse phases
  `+/-theta_h`, plus two longitudinal directions removed by the Gauss
  constraints. At zero momentum the tick is the identity and the constant
  harmonic fields survive Gauss. The only zero-phase momentum
  in the tested Brillouin zones is `k=0`, and `theta_h/h -> |k|` in the
  infrared.

Within the narrower three-layer schedule `B(a h)-E(b h)-B(c h)`, first-order
agreement with the classified generator requires `b=1` and `a+c=1`.
Palindromic time symmetry then gives the unique coefficients
`(a,b,c)=(1/2,1,1/2)`. The dual `E/2-B-E/2` schedule has the same spectrum and
is the time-staggered sibling.

This is meaningful positive closure of one dynamics question: a discrete,
finite-depth, physically local, reversible gauge evolution with photon modes
exists. Continuous time is not required for the candidate light law.

It does not yet produce a one-layer radius-one qubit unitary. The three local
layers compose to radius three in the old-time data, and `H_h` is a local
field-energy metric rather than the raw onsite Euclidean norm. The step,
schedule, field payload, Record bridge, and relation between this finite-depth
cycle and the approved one-edge kinetic tick remain supplier or derivation
questions.

## 1. The three local shears

Let `C` be the exact oriented edge-to-face incidence matrix supplied by the
physical role compiler. Every row and every column has four nonzero entries,
and every such entry joins an edge-role site to a face-role site one physical
lattice step away.

In `(E,B)` ordering define

```text
S_B(t) = [[I, 0], [t C, I]],
S_E(t) = [[I, -t C^T], [0, I]].
```

The candidate tick is

```text
U_h = S_B(h/2) S_E(h) S_B(h/2).
```

Matrix products act right to left, so the rightmost magnetic half-step is
performed first. Each layer has at most five nonzero entries per output row:
the old value and the four physical incidence neighbors.

The complete old-to-new matrix contains paths of length zero through three.
On the side-six physical torus its nonzero entries have exactly the periodic
Manhattan distances `{0,1,2,3}`. “Finite-depth local” here means three
nearest-neighbor shear layers. It does not mean that the composed map has
radius one.

## 2. Exact inverse, time reversal, and Gauss preservation

Each shear is triangular with unit diagonal:

```text
S_B(t)^-1=S_B(-t),
S_E(t)^-1=S_E(-t).
```

Because the schedule is palindromic,

```text
U_h^-1
  =S_B(-h/2) S_E(-h) S_B(-h/2)
  =U_-h.
```

At `h=1/2`, the runner represents the two layer types with integer
numerators over denominators four and two. It multiplies the full
`162 x 162` tick and its reverse exactly and obtains `32^2 I` before division.

Let the two Gauss rows be

```text
Q_E=d_0^T,                 Q_B=d_2.
```

The incidence identities

```text
C d_0=0,                   d_2 C=0
```

give

```text
Q S_B(t)=Q,                Q S_E(t)=Q,
Q=diag(Q_E,Q_B).
```

Thus a valid Gauss sector cannot leak during an intermediate layer. This is
stronger than a cancellation that occurs only after the three-layer cycle.

For physical time reversal use

```text
T(E,B)=(E,-B).
```

Then `T U_h T=U_-h=U_h^-1` exactly.

## 3. Why half-full-half is selected inside the schedule class

Consider the general alternating three-shear family

```text
U(a,b,c;h)=S_B(c h) S_E(b h) S_B(a h).
```

Its first-order tangent is

```text
I+h [[0,-b C^T],[(a+c)C,0]]+O(h^2).
```

Agreement with the parent's classified Maxwell generator requires

```text
b=1,                       a+c=1.
```

A self-adjoint three-layer schedule must read the same forward and backward,
so its outside coefficients agree: `a=c`. Hence

```text
a=c=1/2,                   b=1.
```

The runner enumerates the exact one-eighth rational grid from `-1` through
`2`; half-full-half is the sole member satisfying all three equations. A
quarter-full-three-quarter control retains the correct tangent but fails
`U(-h)U(h)=I` when the same ordered schedule is used backward.

This is a bounded schedule classification. It does not classify longer
palindromic products, implicit steps, quantum walks, or nonlinear ticks.

## 4. A positive local conserved field energy

The raw Euclidean field norm is not exactly preserved at finite `h`. The
palindromic tick instead preserves

```text
M_h=diag(I-(h^2/4)C^T C,I),
U_h^T M_h U_h=M_h.
```

The associated quadratic form is

```text
H_h=(1/2)E^T(I-(h^2/4)C^T C)E+(1/2)B^T B
   =(1/2)(||E||^2+||B||^2)-(h^2/8)||C E||^2.
```

Although the Hessian contains `C^T C`, its density is local: `||C E||^2` is
a sum of squared four-edge face curls.

The largest singular value of the cubic curl is `2 sqrt(3)`. Therefore

```text
lambda_min(M_h) >= 1-3h^2,
```

and the invariant is positive for

```text
0<h<1/sqrt(3).
```

The executable uses `h=1/2`, for which the infinite-lattice lower bound is
`1/4`. It checks the exact integer identity

```text
U_num^T M_num U_num=32^2 M_num
```

on the full physical block. A control with `h=2/3` crosses the positivity
boundary and develops an explicit Brillouin-corner instability.

Preserving `H_h` makes the finite map orthogonal in a positive local field
metric. It does not by itself construct a finite-depth qubit circuit in the
tensor-product onsite inner product. A local Hilbert-space implementation of
this metric is a separate compiler question.

## 5. Exact discrete photon spectrum

For each nonzero singular value `|s|` of `C(k)`, the transverse update is a
two-dimensional determinant-one block with trace

```text
2-h^2 |s|^2.
```

Inside the stability interval its eigenvalues are

```text
exp(+/- i theta_h),
cos(theta_h)=1-(h^2/2)|s|^2,
theta_h=2 asin(h|s|/2).
```

The curl has two equal nonzero singular values and one zero singular value at
every nonzero momentum. The tick therefore carries two equal positive-phase
transverse modes and their negative-phase partners. The two longitudinal
unit eigenvalues lie outside the Gauss-constrained physical subspace rather
than representing propagating modes.

At `h=1/2`, `h|s|/2` is at most `sqrt(3)/2`, so the phase remains strictly
between zero and pi for every nonzero momentum. The executable checks all
momenta on `L=3,4,5,7` and finds no additional zero-phase point. It also
checks five infrared refinements through `L=256`:

```text
theta_h(k)/h -> |k|.
```

Comparison with the exact continuous exponential shows cubic one-step error:
halving `h` reduces the operator error by a factor approaching eight. The
finite map and the continuous exponential differ away from the infrared;
choosing this tick is physical discretization input, not a notation change.

## 6. Cubic symmetry, parity, and the dual schedule

For any signed permutation matrix `R`,

```text
C(Rs)=det(R) R C(s) R^T.
```

Electric fields transform as polar vectors and magnetic fields as axial
vectors. With

```text
D_R=diag(R,det(R)R),
```

each shear and the full tick satisfy

```text
U_h(Rs)=D_R U_h(s) D_R^T.
```

The runner executes all 48 signed permutations, including the 24 improper
ones. This adds the reflection check not required by the proper-cubic parent.

The sibling schedule

```text
S_E(h/2) S_B(h) S_E(h/2)
```

has the same phase spectrum. It corresponds to the other electric/magnetic
time staggering. The result therefore does not use the arbitrary choice of
which field occupies the integer time slice as a prediction.

## 7. Program significance and exact remaining choice

Before this construction, the light stack had a local continuous generator
and evidence that its exact exponential is spatially nonlocal. The new result
shows that this did not block discrete local photon dynamics. Locality,
reversibility, Gauss preservation, positive energy, cubic symmetry, and two
transverse branches coexist in one explicit finite-depth update.

The remaining questions are narrower:

1. Is a three-layer nearest-neighbor cycle an admissible realization of the
   framework's emergent tick, or must the complete old-to-new map itself have
   one-edge radius?
2. Is a positive local field-energy metric sufficient, or must the raw
   edge/face coordinates be implemented by an onsite-norm unitary circuit?
3. Can the step and schedule be selected from Admissibility, Record order, or
   a smaller reversibility principle rather than supplied?
4. Can the finite real field update be compiled into the one-site `M2(C)`
   possibility system without importing an unbounded payload?
5. Does the construction survive compact nonlinear gauge interactions,
   charged matter, Record formation, and the electromagnetic dictionary?

No axiom edit follows automatically. The four axioms explicitly do not
select a Hamiltonian, transfer map, persistence law, or transition rule. The
construction supplies positive evidence for a narrow candidate-law route and
identifies the exact additional decision instead of treating “discrete time”
as an undifferentiated blocker.

## 8. Executable evidence

The runner reports `TOTAL: PASS=27 FAIL=0`. It checks:

- the exact physical incidence complex and every incidence distance;
- five-entry support for each of the three local layers;
- the full rational inverse and both Gauss rows over integers;
- radius three for the composed old-to-new map;
- the exact three-shear coefficient classification and Maxwell tangent;
- the exact modified-energy identity and positivity bound;
- raw Euclidean-norm, asymmetric-schedule, and unstable-step controls;
- every momentum on `L=3,4,5,7`, including branch count and no extra
  zero-phase point;
- five infrared refinements and the cubic local error ratio;
- all 48 cubic transformations with polar/axial parity; and
- the spectrum of the dual time staggering.

## No-Go Discipline Gate

The positive construction sits beside bounded negative statements about raw
Euclidean norm, radius, and the unstable step. This gate prevents those
controls from being generalized into a no-go for local unitary dynamics.

### N1 — Alternative routes and same-cycle evidence

These attempts were checked analytically or by the paired runners in this
47-path review unit. Positive and partial constructions remain positive or
partial; none is recast as a failed route to satisfy a count. Named check
labels, rather than old ordinal numbers, identify the evidence. Cross-note
comparisons below are scope tests, not extra premises of this note.

| Route | Actual attempt and evidence | Result within the stated scope |
|---|---|---|
| Palindromic local shears | **ATTEMPTED:** Multiply the half/full/half maps and test exact inverse, Gauss rows and the modified metric (§§2–5). | This supplies the positive finite-depth tick. |
| Nonpalindromic schedule | **ATTEMPTED:** Use the quarter/full/three-quarter control with the same tangent (time-reversal mutation check). | The displayed schedule loses self-adjoint time reversal; other schedules remain open. |
| Implicit Cayley transform | **ATTEMPTED:** Use the minimal-generator note’s executed full-block inverse. | Raw norm is preserved but the tested map is spatially dense. |
| Local pair rotation | **ATTEMPTED:** Use the radius-one sibling’s explicit Givens/Gauss counterexample. | One norm-preserving pair gate leaks from Gauss; gauge-preserving products remain open. |
| Enlarged directed streams | **ATTEMPTED:** Use the radius-one sibling’s six-stream unitary transport exhibit. | Strict radius-one unitary transport exists with extra payload; a Maxwell sector still needs proof. |
| Static Gaussian dynamics | **ATTEMPTED:** Use the role-compiled sibling’s projected OU construction and relaxation checks. | A reversible static sampler is a different time law with quadratic infrared rate. |

Longer palindromic schemes, gauge-preserving pair circuits and compact
group-valued updates remain live. Positive sibling comparisons are not
claimed as failures or as proofs of a general unitary-tick obstruction.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: acceptance or derivation of the three-layer tick schedule.
- W2: one-edge-radius versus finite-depth tick interpretation.
- W3: onsite-norm qubit-unitary compiler.
- W4: finite one-site payload compiler.
- W5: Record formation/readout bridge.
- W6: compact interactions and charged-matter stability.

| Pair | First closure implies second? | Second closure implies first? | Independence established? |
|---|---|---|---|
| W1, W2 | unresolved | unresolved | no |
| W1, W3 | unresolved | unresolved | no |
| W1, W4 | unresolved | unresolved | no |
| W1, W5 | unresolved | unresolved | no |
| W1, W6 | unresolved | unresolved | no |
| W2, W3 | unresolved | unresolved | no |
| W2, W4 | unresolved | unresolved | no |
| W2, W5 | unresolved | unresolved | no |
| W2, W6 | unresolved | unresolved | no |
| W3, W4 | unresolved | unresolved | no |
| W3, W5 | unresolved | unresolved | no |
| W3, W6 | unresolved | unresolved | no |
| W4, W5 | unresolved | unresolved | no |
| W4, W6 | unresolved | unresolved | no |
| W5, W6 | unresolved | unresolved | no |

The examples elsewhere in this note establish only their displayed positive
or negative cases. In particular, the leapfrog example changes both complete
map radius and energy metric; that single example does not establish those
restrictions’ independence. The strict radius-one sibling retains its own
explicit domain-relaxation table.

### N3 — Hidden-wall scan

The fields are real and weak. The law is linear. The step is supplied. The
locality claim is per shear, while the complete map is explicitly radius
three. Positivity uses `h<1/sqrt(3)`. The executable uses `h=1/2`. “No
doubler” means no additional zero-phase momentum on the named periodic grids,
not a classification of every possible nonlinear or enlarged-payload tick.

### N4 — Residual matching

| Surface | Residual | Match here |
|---|---|---|
| generator-classification parent | exact local finite tick absent | **positive partial closure:** finite-depth reversible tick constructed |
| physical role compiler | only spatial conditionals | **exact reuse:** every shear follows its edge-face nearest-neighbor incidence |
| minimal axioms | no transition or persistence law | **no import:** the tick remains supplied downstream physics |
| kinetic-isotropy primitive | one tick parallel in form to one edge | **open interpretation:** three layers and supplied `h` require matching |
| raw onsite qubit norm | no local unitary implementation | **not closed:** only the positive local field-energy metric is conserved |
| interacting light/matter | weak-field free branch only | **not closed:** compact and charged sectors remain untested |

### N5 — Rhetoric and resolution audit

“Exact” refers to the algebraic inverse, constraints, metric identity, and
finite matrices stated. “Local” refers to each physical-neighbor shear;
“radius three” describes the composed map. “Unique” appears only for the
three-layer palindromic coefficient choice. The unstable control is one
explicit step beyond the stated bound, not a universal instability theorem.

The cached output carries:

```text
per_element: every integer incidence coefficient and each half/full shear coefficient is checked
per_site: every shear reads one physical four-neighbor star; the three-layer tick has radius three
per_mode: all momenta on L=3,4,5,7 carry exactly two stable photon-phase branches
per_block: exact inverse, Gauss preservation, modified energy, time reversal, cubic covariance, and controls are checked
lattice_wide: the full 162-variable rational tick is multiplied exactly and compared with its local energy metric
```

### N6 — Partial-closure paths and primitive check

The shortest positive route is to decide whether finite-depth local update
cycles are acceptable realizations of the kinetic tick. If yes, this source
supplies an explicit candidate and the next work is payload/Record/interaction
compilation. If no, the next discriminator is a radius-one paraunitary search
with exact Gauss preservation. Either answer is more precise than reopening
the already solved finite-depth existence question.

### N7 — Steelman

A hostile reviewer can say leapfrog Maxwell is standard numerical analysis
and therefore not a derivation from the framework. Correct: the update is a
candidate supplier law. Its value here is compositional. It runs on the exact
role-compiled physical lattice, preserves the framework candidate's two Gauss
rows at every substep, and removes a concrete existence blocker without
changing the axiom boundary.

The reviewer can also reject `H_h` as a Hilbert norm because its density
couples a face star. That objection survives. The theorem claims positive
local field-energy conservation, not an onsite tensor-product circuit.

### N8 — Cross-cycle echo

The direct parent contrasted local Euler with nonlocal Cayley and left
split-step evolution live. This source realizes that live route. The minimal
axiom source independently says Admissibility does not choose a transfer map,
and the kinetic primitive says its normalization is not a new dynamics. Both
warnings remain unchanged.

**Gate result:** PASS for the scoped positive construction and bounded
controls. The attempted routes remain separated; pairwise implications among
the named open tasks remain unresolved,
and no universal radius-one or unitary no-go is asserted.

## Falsifiers

The bounded result fails if any of the following occurs:

- an update layer reads a non-neighbor field or more than four opposite-role
  neighbors;
- `U(-h)` is not the exact inverse of `U(h)`;
- either Gauss row changes during any one of the three shears;
- half-full-half is not the sole palindromic three-shear schedule with the
  classified first-order tangent;
- `U_h^T M_h U_h` differs from `M_h`;
- `M_h` is not positive for a step strictly below `1/sqrt(3)`;
- an allowed nonzero tested momentum lacks exactly two positive phases;
- an additional tested momentum has zero photon phase;
- the tick violates polar/axial covariance under a cubic transformation; or
- the finite tick fails to approach the continuous Maxwell generator with
  second-order global accuracy.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=27 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected framework-derived electromagnetic law and physical field/readout bridge remain open; the eventual physical consumer is not yet established."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Use the conditional result with its stated inputs; establish the missing physical consumer and selection bridge before claiming framework closure."
conditional_surface_status: "Supplied normalized weak-field Yee generator and palindromic three-shear tick with strict CFL bound; complete-map radius three and local modified metric."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The written derivation establishes only the declared conditional mathematical claim; finite checks and source review grant no retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original September 2–3 source and receipts are preserved at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. This revision supplies current
source status, explicit timeout/input-bound evidence and written boundary
checks. The conditional scope is stated in the status record above.
Independent source confirmation and current-main integration validation are
separate; no audit verdict or effective retained status is asserted.
