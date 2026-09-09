---
claim_id: admissibility_nonuniform_conserved_source_regge_second_order_ward_pseudoconstraint_gate_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "On the repository's actual four-dimensional Kuhn/Coxeter Regge-plus-deficit-square action at alpha=1/1024, a period-three transversely homogeneous reduction retains all forty-five slice-edge variables. After fixing the ten average metric moduli and only the eight real nonzero-mode displacement coordinates, twenty-seven nongauge equations are solved for two exactly zero-mean, linearly conserved sources: a Euclidean static h_tt density mode and a metric-dominated t+x Record/null-bundle mode whose Lorentzian interpretation is conditional. At source strengths 1e-5 through 1e-3 both branches have projected residual below 3.3e-12, nonzero deficits, positive lengths, and metric response exceeding nonmetric response. Nevertheless, the inherited gauge residual is nonzero at order c^2: its small-c norm divided by c^2 tends approximately to 1.918 for the static source and 2.165 for the null bundle, while the leading eight-real-component Ward vectors have norms 11.514 and 12.988. The relaxed gauge Schur complement has rank eight and mixed signs at c=5e-4 and 1e-3 on both branches. A one-parameter interval-power source seagull leaves at least 92.9% and 63.5% of the respective leading residuals, and a fixed finite cubic-deficit term enters at order c^3 and therefore cannot cancel the order-c^2 obstruction. This rejects only the executed fixed Regge-plus-deficit-square action with these external source laws as an exact finite-curvature first-class completion. It is not a gravity no-go and does not exclude a dynamical Record/matter source, nonlinear generator/current, improved/perfect action, Pachner/tent evolution, or controlled refinement limit. No nonlinear Lorentzian theorem, full-Z3 result, selected law, axiom amendment, audit verdict, or TOE percentage movement is claimed."
upstream_dependencies:
  - minimal_axioms
  - admissibility_flat_regge_curvature_squared_branch_lift_boundary_bounded_theorem_note_2026-08-10
  - admissibility_curved_regge_pseudoconstraint_perfect_action_route_gate_bounded_theorem_note_2026-08-12
  - admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_nonuniform_conserved_source_regge_second_order_ward_pseudoconstraint_gate_2026_08_12.py
---

# Nonuniform Conserved-Source Regge Second-Order Ward / Pseudo-Constraint Gate

**Date:** 2026-08-12

**Type:** `bounded_theorem`

**Role:** replace the Block-19/21 affine nonmetric surrogate with a genuine
nonuniform full-edge metric-source response, test the first nonlinear Ward
obligation, and re-rank the gravity campaign without treating a route kill as
TOE closure.

**Audit-status authority:** independent audit lane only. This source note
authors no audit verdict and predicts none.

**Primary runner:**
[admissibility_nonuniform_conserved_source_regge_second_order_ward_pseudoconstraint_gate_2026_08_12.py](../scripts/admissibility_nonuniform_conserved_source_regge_second_order_ward_pseudoconstraint_gate_2026_08_12.py)

**Repository dependencies:** the current
[minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md), the
[flat Regge curvature-square repair](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
the corrected
[Block-54 affine-surrogate gate](ADMISSIBILITY_CURVED_REGGE_PSEUDOCONSTRAINT_PERFECT_ACTION_ROUTE_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md),
and the
[Block-53 linear causal update](ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md).

## Result Up Front

The prior sourced-curvature route was not a physical gravity branch. Its ten
affine conditions fixed all ten uniform metric tangents and left only five
nonmetric edge modes. The source was linear and the reactions were affine, so
their length-length Hessians were exactly zero. At generic momentum the affine
constraint matrix has rank four on the four displacement columns, and its
bordered KKT matrix is full rank twenty-five. The Block-54 finite rank census
was numerically real but physically a gauge-fixed ensemble diagnostic.

This block changes the branch rather than extending that surrogate. It uses
the actual period-three four-dimensional Kuhn complex with all `3 * 15 = 45`
edge lengths, fixes the ten average metric moduli, and resolves:

- five uniform nonmetric coordinates;
- eleven complex nonzero-mode nongauge coordinates, represented by twenty-two
  real coordinates; and
- eight real displacement coordinates, retained for the Ward and Schur tests
  but gauge-fixed during the twenty-seven-coordinate solve.

Two source modes are used at `k=2 pi / 3`:

1. a static Euclidean `h_tt` density modulation; and
2. a `t+x` rank-one Record/null-bundle source with transverse modulation.

Both sources have zero mean and annihilate the flat displacement columns to
machine precision. The second source is carried by the Euclidean calculation;
calling it null is a conditional Lorentzian interpretation of its target
tensor, not a nonlinear Lorentzian evolution theorem.

At coupling `c=10^-3`, the solved branches are:

| source | `||B^T E||` | max `|epsilon_h|` | metric response | nonmetric response | min length |
|---|---:|---:|---:|---:|---:|
| static density | `3.30e-13` | `0.00380245` | `7.929e-4` | `2.816e-4` | `0.999325` |
| Record/null bundle | `3.76e-13` | `0.00534496` | `1.438e-3` | `1.342e-4` | `0.999328` |

These are genuine metric-dominated nonuniform solutions of every nongauge
equation on the declared slice. They are not the five-nonmetric-mode affine
continuation.

The omitted gauge equations do not vanish. For the four smallest couplings,

| source | `||Gamma^dagger E_k|| / c^2` at `c=10^-5` | at `c=10^-4` |
|---|---:|---:|
| static density | `1.918285` | `1.911864` |
| Record/null bundle | `2.164783` | `2.164180` |

The stable, nonzero limits show an order-`c^2` obstruction. A symmetric
second derivative at the flat first-order response gives the leading real
Ward vectors

~~~text
static: (approximately 0,0,0,0,-3.21255, 5.66547, 5.66547, 7.61904)
        norm = 11.513700

null:   (approximately 0,0,0,0,-0.44400,-12.96849,0.35148,-0.44401)
        norm = 12.988440
~~~

The first four components are below `4e-6` and are numerically zero on this
symmetry-reduced slice; the last four supply the nonzero obstruction.

The relaxed gauge Schur complement lifts all eight real displacement
directions. At `c=5e-4` and `10^-3` its rank is eight for both sources, with
negative and positive eigenvalues. The largest absolute eigenvalue grows
approximately linearly with `c`. These are soft pseudo-constraint directions.
Because the calculation is Euclidean, their mixed signs are not called a
Lorentzian instability.

This is the first campaign result that rejects the current fixed
Regge-plus-deficit-square action on a genuine nonuniform, metric-dominated,
conserved-source branch. It rejects that candidate as an *exact finite-spacing
first-class law*. It is not a gravity no-go.

## Independent Construction Checks

The runner does not validate the reduction only against itself. For a
deterministic nonuniform period-three field, it compares the reduced action to
the original independent periodic `L=3` box action, including the independently
assembled curvature-square term, divided by the transverse volume `27`. The
relative discrepancies are below `4.4e-9`. Central differences independently
check the analytic gradient, and a symmetric directional derivative checks the
Bloch-assembled flat Hessian. The reduced cell contains all fifty hinge classes
and 240 simplex-hinge incidences per slice.

The reduction is therefore a faster evaluation of the repository action, not
a replacement toy kernel.

## Repair-Family Tests

### Scalar interval-power source seagull

The external source gradient was generalized to

~~~text
J_e(l) = J_e (l_e / l_e,flat)^(p-1).
~~~

The linear source is `p=1`; the squared-interval source is `p=2`. Optimizing an
arbitrary scalar along the single direction between their leading Ward
vectors leaves these residual fractions:

| source | best remaining fraction |
|---|---:|
| static density | `0.929341` |
| Record/null bundle | `0.635485` |

Thus neither `p=2` nor any one-scalar member of this local power family closes
both Ward vectors. This does not exclude a dynamical matter action with its own
fields, mixed Hessian blocks, and transformed current.

### Cubic-deficit hinge term

For a fixed finite coefficient `beta`, consider

~~~text
Delta S_beta = beta sum_h A_h epsilon_h^3.
~~~

At flatness `D epsilon Gamma = 0`. Along a first-order perturbation,
`epsilon^2 = O(c^2)` while the displaced deficit derivative is `O(c)`; the
projected cubic contribution is therefore `O(c^3)`. The runner measures its
norm divided by `c^2` at `c=(10^-3,5*10^-4,2.5*10^-4)`:

| source | three values |
|---|---|
| static density | `1.499673, 0.750197, 0.375189` |
| Record/null bundle | `0.381879, 0.192482, 0.096629` |

Each halving of `c` halves the ratio. A fixed finite `beta` is one order too
late to cancel the nonzero order-`c^2` Ward vector. A coupling-dependent
`beta ~ 1/c` would not define the fixed local action being tested. No broader
local-counterterm no-go is claimed.

## Route Decision And TOE Score Gate

Three branches are now retired as gravity workhorses:

- the Block-19/21 affine continuation, because it freezes all metric tangents;
- further coefficient grids on that surrogate; and
- a fixed cubic-deficit coefficient or one-scalar interval-power seagull as a
  repair of the leading Ward obstruction.

The live priority stack is:

1. **Dynamical Record/matter source completion.** Endogenize the source field,
   transform the current and displacement generator jointly, and calculate the
   mixed source--geometry second variation. This is highest leverage because a
   same-order source block can directly cancel the measured Ward vector while
   binding gravity to Records, realized history, and causal update.
2. **Improved/perfect or Pachner/tent gravity law.** Integrate refinement data
   or vary the triangulation so the exact discrete Noether identity is a law of
   the carrier rather than an inherited flat null. This is the next route if a
   dynamical source cannot close the identity on the fixed action.
3. **Controlled pseudo-constraint refinement.** If exact finite-spacing
   symmetry is not available, prove the eight soft modes vanish under
   refinement and remain irrelevant to physical observables. This is a weaker
   emergent route, not the preferred exact closure.

The strategic checkpoint is intentionally strict: blocker localization,
runner count, and finite-rank tables do not move a TOE lane. The next block
must either construct a same-order source/refinement term and close the Ward
vector, or sharply rule out one normalized completion family. Repeating the
same fixed-action diagnostic at more couplings or momenta is low leverage.

The established TOE map remains unchanged, so this block earns **zero TOE
percentage points**:

| lane | evidence | integration | foundational closure |
|---|---:|---:|---:|
| operational quantum / Records | `95%` | `92%` | `50%` |
| causal time | `76%` | `72%` | `41%` |
| inertia / matter | `95%` | `96%` | `75%` |
| gravity / source / resources | `70%` | `45%` | `29%` |
| Born probability / realized history | `84%` | `63%` | `34%` |

Significant progress here means a wrong branch was corrected and one physical
candidate was decisively rejected. TOE progress would require the replacement
joint law, exact nonlinear constraint propagation, and then increasing-region
or full-`Z^3` control.

## Axiom Boundary

No axiom is amended. The current foundation permits law construction but does
not select this fixed Regge action, either external source, a nonlinear
generator, a perfect-action refinement, or a Pachner sequence. This block does
not claim that no retained primitive can participate in a completion and does
not infer that a new primitive is required.

The minimal law content exposed by the calculation is extensional rather than
adjectival: a candidate must supply a dynamical conserved Record/matter source,
its transformation under the nonlinear displacement generator, the mixed
source--geometry Hessian or canonical equivalent, and an exact joint Noether
identity. If this cannot be derived, an owner amendment would need to attach
that exact law object; saying only “gravity is covariant” would not close the
measured residual.

## No-Go Discipline Gate

The narrow negative is only:

> On the executed period-three transversely homogeneous slice, the fixed
> Regge-plus-deficit-square action with either named external conserved source
> has a nonzero order-`c^2` Ward residual and eight lifted gauge directions.

It is not “gravity fails,” “Regge calculus cannot work,” “no source completion
exists,” or “the TOE is impossible.”

### N1 -- Alternative Route Enumeration

| normalized route | attack and result | marker |
|---|---|---|
| full-edge fixed action plus external linear source | solved both conserved metric-dominated branches; nonzero order-`c^2` Ward vectors and rank-eight pseudo-constraint Schur blocks | `ATTEMPTED`; narrow candidate rejected |
| scalar interval-power source seagull | optimized the full one-scalar direction between `p=1` and `p=2`; at least `92.9%` and `63.5%` remain | `ATTEMPTED`; narrow family rejected |
| fixed cubic-deficit hinge term | analytic order count and three-coupling execution show `O(c^3)`, one order too late | `ATTEMPTED`; narrow term rejected |
| dynamical Record/matter source | include source equations, mixed Hessian blocks, and transformed current at the same order | `UNTRIED`; live and preferred |
| improved/perfect refinement action | integrate fine data into an exactly symmetric coarse action | `UNTRIED` here; live |
| variable-triangulation Pachner/tent law | encode the constraint identity in consistent local canonical moves | `UNTRIED` here; live |
| controlled pseudo-constraint infrared limit | prove the eight lifted modes vanish and decouple under refinement | `UNTRIED`; live but weaker |
| independent connection/tetrad system | use the prior connection carriers to realize a different exact constraint algebra | `RULED OUT BY PRIOR` only as already complete; construction route remains live |

Multiple concrete escape routes survive. A universal gravity no-go fails.

### N2 -- Wall-Independence Audit

After collapsing dependent tasks, three walls remain:

- `W_G`: construct an exact nonlinear geometry constraint identity;
- `W_S`: endogenize the Record/matter source and bind its current to that
  identity; and
- `W_H`: construct the positive physical state and realized causal history.

`W_G` and `W_S` interact but neither closes the other: a perfect vacuum action
does not select matter, while a conserved source does not create an exact
geometry algebra. `W_H` remains independent of both. The eight Schur
eigenvalues are consequences of `W_G`, not eight extra walls.

### N3 -- Hidden-Wall Scan

The carrier is period three in one coordinate and homogeneous in the other
three. Average metric moduli are fixed. The static source and Record/null source
are named explicitly. The signature is Euclidean; the null label is
conditional. The action coefficient is `alpha=1/1024`; source strengths are
finite and small; arithmetic is double precision. Neither continuous momentum,
larger periods, nonlinear Lorentzian causality, dynamical source equations, nor
refinement is hidden inside “full edge” or “conserved.”

### N4 -- Residual Matching

The Block-54 residual did not match a physical curved-source residual because
its affine constraints froze all ten metric tangents. This block retires that
wall by changing the branch. The present residual is evaluated after solving
all twenty-seven nongauge full-edge equations, and its response is
metric-dominated. It therefore matches the nonlinear Ward obligation left by
the Block-53 linear TT update. The scalar-seagull and cubic-term residuals are
matched only to their exact one-parameter families, not to general matter or
perfect-action completions.

### N5 -- Rhetoric And Resolution Audit

The primary cached stdout prints one substantive execution line for
`per_element`, `per_site`, `per_mode`, `per_block`, and `lattice_wide`. It
checks forty-five edge lengths, fifty hinge classes and 240 incidences per
slice, both named momentum/source modes, the affine-to-full-edge handoff, and
the explicit boundary against full-`Z^3`. Accordingly the claim says “on the
executed slice,” “order `c^2`,” and “fixed external-source candidate,” never
“all lattices,” “all sources,” or “gravity is impossible.”

### N6 -- Partial-Closure And Primitive Scan

Block 53 supplies a local causal linear two-TT update; the repaired flat action
supplies four exact displacement nulls; the Record campaign supplies event,
clock, and source carriers; and the connection/refinement lines supply live
construction mechanisms. These are substantial partial-closure paths. This
note makes no “no retained primitive” claim, does not require a registry-absence
argument, and does not say a new axiom is required. Derivation, a provisional
import with retirement criteria, and later owner adoption all remain valid.

### N7 -- Steelman

The strongest objection is that an external source held fixed under a lattice
displacement should not satisfy the complete nonlinear Noether identity. A
dynamical matter/Record field contributes its own equation of motion, current
transformation, mixed Hessian, and generator derivative; these can cancel the
measured order-`c^2` vector. A perfect or Pachner law can instead change the
geometry action itself. This objection succeeds. It prevents promotion of the
result to a gravity no-go and makes the dynamical-source completion the next
construction, not an afterthought.

### N8 -- Cross-Cycle Echo

Blocks 19--21 used affine constraints and only five nonmetric coordinates.
Block 54 mistook their full-rank length block for evidence of omitted affine
connection terms; the correction records that all affine/source Hessians are
zero and changes the branch. Blocks 42--53 previously escaped flat projection
walls by changing the quotient and update. The same discipline applies here:
endogenize the source or change the discrete action/move family rather than
repeating coefficient scans on a failed carrier.

**N1--N8 status: `PASS` for the narrow executed fixed-action/external-source
claim.** The universal gravity no-go fails N1 and N7 and is not shipped.

## Reproduction

From the repository root:

~~~bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
python3 scripts/admissibility_nonuniform_conserved_source_regge_second_order_ward_pseudoconstraint_gate_2026_08_12.py
~~~

Expected final line:

~~~text
TOTAL: PASS=9 FAIL=0
~~~

## Conclusion

The campaign was stuck in the scientifically relevant sense: the TOE map had
not moved, and the prior “curved source” branch did not contain curved metric
directions. That is now corrected. On the first genuine nonuniform,
metric-dominated conserved-source branch, the present fixed action develops a
second-order Ward obstruction and eight pseudo-constraints. Two simple repair
families are also retired.

This is significant route progress and zero TOE score progress. The optimal
next investment is a dynamical Record/matter source completion with the mixed
source--geometry identity calculated explicitly. If that cannot cancel the
displayed vector, move directly to improved/perfect or Pachner/tent dynamics;
do not spend another cycle expanding the same fixed-action coefficient grid.
