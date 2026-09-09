---
claim_id: admissibility_flat_regge_curvature_squared_branch_lift_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the actual four-dimensional Kuhn/Coxeter Regge edge action, the interval-certified homogeneous nonflat background of Block 19 does not by itself establish an invertible inhomogeneous linearization: under global-only affine constraints its complete double-precision Hessian numerically brackets a spatial soft mode on k=(x,x,0,0) at x=1.1694470624..., while the pointwise five-normal affine extension numerically brackets a distinct soft mode at x=2.4250409952.... This is a bounded numerical boundary of those two named extensions, not a gravity no-go or an interval root theorem. On the separate flat background, the local action family S_alpha=sum_h A_h(epsilon_h+alpha epsilon_h^2) has exact quadratic correction 2 alpha sum_h A_h d_h^dag d_h and exact extra-branch curvature 768+384 sqrt(2). Positive-semidefinite monotonicity plus endpoint spectra establish on every declared finite matrix that the complete coefficient interval 0<alpha<=1/128 preserves the four vertex-gauge zeros, lifts the fifth nonmetric Regge branch, leaves the ten constant-metric k=0 directions zero, repairs the named gauge-compatible body-edge source, and keeps the curvature-square metric correction at O(k^4) relative to the O(k^2) Einstein term. The interval statement is exhaustive only on all 25,308 nonzero modes of L=3,...,10 tori and is additionally tested on 7,183 declared Brillouin stress samples; it proves that these named Euclidean linear criteria do not select alpha=1/1024, but not that a continuous-zone, nonlinear, Lorentzian, coarse-grained, or realized law cannot select a coefficient. Interval root certification for the nonflat roots, a continuous-zone theorem, Lorentzian stability, nonlinear sourced completion, and physical geometry-law selection remain open."
upstream_dependencies:
  - minimal_axioms
  - admissibility_fixed_metric_nonlinear_regge_kkt_continuation_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
  - cubic_coxeter_regge_linearized_action_selection_eh_class_narrow_theorem_note_2026-06-10
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py
---

# Flat Regge Curvature-Squared Branch Lift, Coefficient Window, And Nonflat Mode Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** identify the first inhomogeneous failure of the Block-19 compact
background, exhibit an action-native repair of the flat carrier's extra
lattice branch, and determine whether the named linear repair criteria select
its dimensionless coefficient.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py](../scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py)

## Result Up Front

The Block-19 result is real progress, but it is not yet a gravity vacuum.
Block 19 proves that one explicitly constrained, homogeneous, nonflat
background closes its five normal equations at `k=0`. The missing test is the
complete inhomogeneous Hessian.

For the actual Regge action on that same uniform background, let `Q_*(k)` be
the `15x15` Bloch Hessian reconstructed from all 50 hinge classes and 240
dihedral incidences per cell. Along the purely spatial line

    k=(x,x,0,0),                                                       (1)

where the last coordinate is the record-tick direction, two natural
extensions exhibit double-precision-bracketed losses of invertibility at
different momenta:

1. If the ten affine constraints are global homogeneous constraints only,
   every `k!=0` edge mode remains in the complete operator. Its determinant
   changes sign on `[1.16,1.18]` and numerically isolates a soft mode at

       x_full = 1.1694470624... .                                     (2)

2. If the same five-dimensional normal surface is instead imposed at every
   cell, the pointwise projected operator `N^T Q_*(k) N` changes inertia on
   `[2.42,2.43]` and numerically isolates a soft mode at

       x_normal = 2.4250409952... .                                   (3)

Thus `k=0` nondegeneracy does not by itself establish inhomogeneous
invertibility. This is not a claim that gravity cannot work. It says that
neither of these two tested extensions has yet made the named Block-19
background a certified complete physical geometry law.

The same calculation exposes a constructive repair on a different, physically
better motivated weak-field branch. Return to the exactly flat background and
consider the local action family

    S_alpha = sum_h A_h [epsilon_h + alpha epsilon_h^2],
    alpha > 0.                                                          (4)

The original repair point is `alpha=1/1024`; it is now tested inside the
bounded rational window

    0 < alpha <= 1/128.                                                (4a)

Because every flat deficit is zero, its second variation is exactly

    Q_alpha(k) = Q_R(k)
                 + 2 alpha sum_h A_h d_h(k)^dag d_h(k),                 (5)

where `d_h(k)` is the linearized deficit row. Equation (5) is an actual local
curvature-squared action Hessian. It is not the rank-one projector used as a
counter-control in the earlier source note.

At `k=0`, the bare Regge inertia is

    4 negative, 0 positive, 11 zero.                                   (6)

The repaired inertia is

    4 negative, 1 positive, 10 zero.                                   (7)

The ten remaining zeros are exactly the constant-metric tangent directions.
The fifth nonmetric branch has the exact curvature-square quadratic form

    g^T delta^2 S_2 g = 768 + 384 sqrt(2)
                         = 1311.05800795... .                           (7a)

This is before multiplication by `alpha`, while the correction
annihilates the complete ten-dimensional metric map to numerical error below
`6e-13`.

At every one of the 25,308 nonzero Fourier modes on the `L=3,...,10`
four-tori, every coefficient in (4a) has repaired inertia

    9 negative, 2 positive, 4 zero,                                    (8)

and the four zeros are the exact vertex-displacement gauge directions. This
is an interval statement on each declared matrix, not an inference from five
isolated coefficients. The curvature-square Hessian is positive semidefinite,
so every ordered eigenvalue of `Q_alpha` is nondecreasing in `alpha`. The bare
operator has inertia `9-/1+/5-zero`; its quotient curvature-square form is
positive on the extra branch; and the endpoint `alpha=1/128` still has
inertia (8). Therefore no negative mode crosses zero anywhere in (4a), while
the extra mode is positive for every `alpha>0`.

Five dyadic witnesses spanning the window give zero failures in `126,540`
mode-coefficient evaluations. The smallest nonzero absolute eigenvalue over
those evaluations is greater than `0.0323`. Direct generalized-pencil
diagonalization places the earliest negative-mode crossing in the complete
finite-torus inventory at

    alpha_cross = 0.0098646245597... > 1/128.                          (8a)

A separate set of 7,183 random, corner, and high-symmetry samples has the
same interval inertia by the same monotonic endpoint argument. Its five
dyadic controls give zero failures in `35,915` sample-coefficient
evaluations. On that declared sample set, the curvature-square form on the
extra branch is at least `527.529...` before multiplication by `alpha`.

This repairs a concrete prior obstruction. The full body-diagonal edge source
at `k=(0.3,0.2,-0.1,-0.4)` obeys the four-gauge Ward identity. The bare
operator rejects it with solve residual approximately `2`. Throughout (4a),
the repaired kernel on that momentum is exactly the four-gauge kernel, so the
Ward-compatible source lies in the range. Five spanning coefficients reduce
the direct unprojected solve residual below `1.2e-13` while preserving the
gauge kernel.

Finally, on metric perturbations the new term is `O(k^4)`. The retained Regge
term remains `O(k^2)` and keeps its leading Einstein comparator and `1/k^2`
weak-field pole. Halving `|k|` quarters the measured correction-to-leading
ratio at both ends of the declared dyadic control range. Even at `alpha=1/128`
the displayed correction-to-leading ratio at `|k|=10^-2` is below `3.84e-6`.
The repair therefore targets the lattice branch without replacing the
infrared graviton scaling.

Consequently the named Euclidean linear criteria do not select
`alpha=1/1024`: an uncountable interval of coefficients has the same declared
gauge, inertia, source-range, and infrared-order properties. This conclusion
is deliberately narrower than “the framework cannot select alpha.” A
continuous-zone extremum, nonlinear completion, Lorentzian transfer law,
coarse-graining fixed point, different background, or realized source law
could still impose a coefficient.

The result is still conditional. Nothing in the current axioms selects (4),
fixes `alpha` inside (4a), selects the flat background as the realized vacuum, proves a
continuous Brillouin-zone gap, derives a Lorentzian evolution law, or proves
nonlinear sourced stability. Those are now the exact gravity obligations.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact flat-background second-variation and coefficient-monotonicity identities plus exhaustive finite-torus coefficient-window spectra, deterministic Brillouin stress samples, two robust nonflat soft-mode brackets, and independent periodic-action reconstructions on supplied geometry fixtures."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "select or derive the realized geometry/history action, background, constraint localization, dimensionless higher-curvature coefficient, Lorentzian continuation and stability rule; then prove the gauge-quotient spectrum over the complete realized momentum support"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "test whether a continuous-zone, nonlinear, Lorentzian, coarse-grained, background, or source law selects alpha; replace the finite Brillouin scan by a continuous gauge-quotient theorem; and test nonlinear Lorentzian sourced evolution on the flat repaired branch"
conditional_surface_status: "The named Block-19 nonflat background has numerically bracketed finite-spatial-momentum soft-mode crossings under both tested constraint localizations; on the separate flat Regge-plus-curvature-square family every coefficient in 0<alpha<=1/128 removes the fifth branch on every declared finite mode while preserving gauge, the named source range, and infrared order, so those bounded Euclidean linear criteria do not select alpha=1/1024."
hypothetical_axiom_status: "A downstream geometry-law clause must select the action, background, constraint localization, and stability obligation. Candidate wording below is unadopted and sufficient rather than necessary or minimal; no canonical axiom is edited."
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target Contract And Obligation Graph

| Obligation | Evidence | Disposition |
|---|---|---|
| test the complete Block-19 inhomogeneous Hessian | real-space kernel from all hinge and simplex incidences | closed for the uniform background |
| distinguish global from pointwise affine constraints | full `Q_*(k)` versus `N^T Q_*(k)N` | closed numerically; distinct double-precision brackets (2)--(3) |
| reject a floating-kernel artifact | independent periodic `L=3` action second difference | closed numerically |
| replace the flat fifth branch by a local action | equation (4), not a projector | closed conditionally |
| preserve all four gauge modes | `Q_alpha(k) Gamma(k)=0` on every declared mode | closed on the declared inventory |
| retain the infrared Einstein order | curvature square `O(k^4)` versus Regge `O(k^2)` | closed numerically on the declared long-wave sequence |
| cover a finite lattice family exhaustively | every nonzero mode of `L=3,...,10` | closed, 25,308/25,308 |
| test coefficient uniqueness under the named linear criteria | positive-semidefinite monotonicity, endpoint inertia, five dyadic controls, and the first finite generalized crossing | closed negatively on the declared matrices; all `0<alpha<=1/128` pass |
| prove the continuous Brillouin-zone quotient spectrum | interval or analytic all-`k` theorem | open; samples are not a theorem |
| derive `alpha`, action, background, and constraint localization | current foundation or retained bridge | open; the bounded linear repair criteria now provably leave an interval |
| establish Lorentzian nonlinear sourced stability | selected evolution and stability theorem | open |
| edit or adopt an axiom | owner governance | not attempted and not authorized |

The first positive result is equation (5): a local curvature action realizes
the previously hypothetical fifth-branch lift without spoiling the leading
metric sector. The coefficient-window result is a selection boundary: the
same named criteria admit every coefficient in (4a), so uniqueness must come
from stronger physics. The strongest missing lemma remains to derive the
realized geometry law and prove its complete gauge-quotient Lorentzian
spectrum and nonlinear sourced evolution.

## 1. Nonflat Background: What Breaks

Let the Block-19 stationary background be

    ell_* = ell_flat + a_* r + u_* g,                                  (9)

with

    a_* = 0.0176289114528026416711...,
    u_* = 0.1522365512153477903341... .                                (10)

Its hinge deficits range from approximately `-0.70860918` to `1.22024523`.
It is therefore not the flat weak-field vacuum. The complete real-space
Hessian has 29 translation shifts and is Hermitian after Bloch transformation.
At `k=0`, its projection into the exact basis
`N=[r,v_0,v_1,v_2,g]` agrees with the independent automatic-differentiation
Hessian of the [Block-19 note](ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md).

The global-only and pointwise-affine interpretations are not equivalent:

- A global homogeneous constraint removes only `k=0` metric variations. Its
  tangent restriction does nothing to `k!=0`; the physical test is the full
  `15x15` matrix.
- A pointwise affine constraint freezes ten tangent coordinates in every
  cell. Its `k!=0` operator is the five-dimensional congruence
  `N^T Q_*(k)N`. This is mathematically definite but is not supplied by the
  current axioms and would freeze local metric gravity if interpreted
  literally.

Both numerically isolate a soft mode, but at different spatial momenta. The
double-precision determinant signs change at both brackets by large displayed
margins, and the runner reconstructs one commensurate finite-momentum
quadratic form directly from the original periodic action. No outward-rounded
interval bound is applied to the roots, so these are bounded numerical mode
brackets, not interval root certificates and not an all-background
instability theorem.

## 2. Flat Action-Native Repair

The parent [actual Regge second-variation note](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
finds five zeros at every generic nonzero momentum: four vertex-displacement
gauge modes plus one nonmetric lattice branch. For the added local functional

    S_2 = sum_h A_h epsilon_h^2,                                      (11)

the flat-background gradient vanishes. Two derivatives give

    delta^2 S_2 = 2 sum_h A_h |delta epsilon_h|^2.                    (12)

Terms involving `delta A_h`, `delta^2 A_h`, or `delta^2 epsilon_h` carry at
least one background deficit and therefore vanish at the flat anchor. This is
why (5) is exact rather than a finite-difference ansatz.

Every vertex displacement has `delta epsilon_h=0`, so (12) preserves the four
gauge directions. Every constant metric deformation also preserves flatness,
so the ten `k=0` metric directions remain zero. The extra branch has a
nonzero deficit variation and is lifted.

The closest prior result is the
[linearized action-selection note](CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md).
It already exhibits this deficit-squared form as a local, gauge-annihilating,
nonzero `O(k^4)` freedom. That prior result is load-bearing provenance, not
the new conclusion: it does not evaluate the fifth branch, derive (7a), solve
the body source, construct the Block-19 nonflat kernel, or inventory the
repaired modes. This block tests exactly those previously open consequences.

The coefficient `alpha=1/1024` was a supplied dyadic control. The extended
runner does not fit a replacement to data. Instead it evaluates the family at
`1/16384`, `1/4096`, `1/1024`, `1/256`, and `1/128`, while using the exact
positive-semidefinite order

    Q_alpha_2 - Q_alpha_1 =
        2 (alpha_2-alpha_1) sum_h A_h d_h^dag d_h >= 0               (13)

for `alpha_2>=alpha_1`. On each declared gauge quotient the correction is
positive on the bare extra branch. Since the upper endpoint retains the same
negative count as the right-hand limit at zero, eigenvalue monotonicity rules
out an intervening negative-mode crossing. This proves the full interval
(4a) on the finite inventory and separately on every declared stress matrix.

A physical completion must therefore derive a coefficient from stronger
content, select it through an approved law, or replace (4) by a different
selected action with the same terminal spectral obligations. The finite
window is not evidence that `1/128` is preferred; it is a safe rational
endpoint chosen below the observed finite crossing (8a).

## 3. Source Repair And Infrared Gravity

The earlier [closed-history source note](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
used a rank-one projector only as a counter-control. Equation (4) supplies the
missing mechanism at action level.

For the body-edge source in the runner, the four Ward overlaps vanish before
solving. The bare residual is entirely in the fifth nonmetric zero branch.
The curvature-square Hessian lifts that branch for every coefficient in
(4a), so the same unprojected source is in the repaired range throughout the
declared window. No source projection or compensating signed source is
introduced. The displayed solves at five coefficients are numerical controls;
the interval range statement follows from the four-gauge kernel and the Ward
identity on the named matrix.

On the metric image, a linearized deficit is `O(k^2)`. Hence (12) is `O(k^4)`,
while the parent Regge quadratic form is `O(k^2)` and matches the Euclidean
Einstein pairing at leading order. The correction is therefore irrelevant in
the strict infrared in the technical scaling sense used here. This does not
derive a physical Newton constant, action sign, Lorentzian pole prescription,
or matter coupling. Scaling order also cannot select a finite coefficient:
every fixed `alpha` in (4a) remains `O(k^4)`.

## 4. Candidate Geometry-Law Wording

The current [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) correctly says
that Admissibility is not a dynamics axiom and explicitly leaves
source/action identification outside axiom content. The approved
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies only equal-form OS0 graining; the
[scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) supplies only
units; the [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
supplies only a pointwise evaluation slot. None selects (4) or `alpha`.

The immediate defect is therefore not best repaired by silently enlarging
Admissibility. It requires a downstream retained geometry/history law or an
explicitly owner-approved new premise.

### Candidate geometry-law wording

> A realized geometry/history law selects a local lattice-covariant geometry
> action, its dimensionless coefficients, a law-admissible background or
> boundary sector, and the localization of every constraint. About each
> selected background, the gauge-quotient linearization has no unintended
> zero modes on the realized momentum support, preserves the intended
> infrared gravitational pole and source Ward identities, and admits a stable
> Lorentzian nonlinear evolution for the selected source family.

This wording is a sufficient target, not a claimed minimal axiom. It is also
close to the terminal theorem being sought, so adopting it as an axiom would
buy closure rather than explain it. The preferred path is to derive the action,
coefficient, background, and spectrum from the existing framework. If that
derivation fails, owner governance can decide whether a narrower action-
selection primitive is scientifically justified.

No canonical axiom or primitive file is edited in this block.

## 5. TOE Lane Consequence

This is significant gravity-lane progress:

- it identifies exactly why the Block-19 nonflat root is not yet a gravity
  vacuum;
- it turns the earlier algebraic fifth-branch projector control into a local
  action mechanism;
- it proves that the named linear repair conditions admit the full interval
  `0 < alpha <= 1/128`, rather than selecting the original dyadic point;
- it restores full gauge-compatible source solvability on a large exact finite
  inventory; and
- it preserves the leading weak-field Einstein order.

It does not move the campaign's fixed TOE percentages. The campaign rule
requires a retained selector or approved premise registration before physical
or autonomous closure percentages move. Action selection, stronger-physics
coefficient selection, continuous mode control, Lorentzian dynamics, and
realized history remain open.

The next highest-value gravity work is:

1. replace the 7,183-point continuous-zone stress scan by an analytic or
   interval proof on the gauge quotient and test whether its extremal gap
   narrows the coefficient window;
2. test coefficient selection in nonlinear, Lorentzian, coarse-grained,
   background, and realized-source laws; the bounded Euclidean linear criteria
   are now eliminated as a unique selector;
3. construct the Lorentzian transfer/update operator and test its physical
   poles rather than Euclidean Hessian signs; and
4. solve the nonlinear localized source equation on the selected flat/open
   background.

## 6. No-Go Discipline Gate

**Status:** `PASS` for the narrow numerical claims in (2)--(3) and for the
statement that the declared Euclidean linear repair criteria do not select a
unique coefficient inside (4a). The broad statements “gravity fails” and
“the framework cannot select alpha” are explicitly rejected. The successful
flat family and the live stronger-physics selectors are counter-routes inside
this artifact.

### N1 — Alternative route enumeration

The route families are normalized by primary operator, mechanism, and terminal
obligation.

| Family | Object / mechanism | Terminal obligation | Result | Marker |
|---|---|---|---|---|
| complete global-only operator | full `Q_*(k)`; homogeneous constraints remove no `k!=0` edge direction | prove invertibility of the complete nonzero-momentum operator on the named background | the determinant changes sign on `[1.16,1.18]`; this establishes the numerical boundary (2) rather than evading it | `ATTEMPTED` |
| pointwise affine localization | congruence `N^T Q_*(k)N`; freeze the ten metric tangents in every cell | prove invertibility of the five-normal pointwise operator | its determinant changes sign on `[2.42,2.43]`; this establishes the separate numerical boundary (3) | `ATTEMPTED` |
| action orientation and coordinate chart | `Q_* -> -Q_*` or nonsingular congruence; determinant-zero and Sylvester invariance | remove the bracketed zero without changing the action, background, or constraint surface | a sign flip and nonsingular congruence preserve determinant zeros; the numerical roots remain singular points | `ATTEMPTED` |
| alternate background | exactly flat Regge branch; replace the nonflat root rather than its coordinates | exhibit a viable gravity branch and thereby defeat a background-universal no-go | this defeats any broad gravity no-go but does not falsify the fixed-background statements (2)--(3) | `ATTEMPTED` |
| local higher-curvature action | `S_R+alpha S_2`; positive deficit-gradient form | lift the extra mode without violating gauge or leading infrared order | on the flat branch it succeeds, yielding (5)--(8); action changes remain live and force the negative scope to stay narrow | `ATTEMPTED` |
| bounded Euclidean coefficient family | the Hermitian pencil `Q_R+alpha Q_2`; positive-semidefinite Loewner order | test whether gauge, inertia, the named source range, and infrared order uniquely select `1/1024` | every `0<alpha<=1/128` passes on the declared matrices, so these criteria do not select a point | `ATTEMPTED` |
| continuous-zone extremal selector | minimize the first quotient crossing over the complete Brillouin zone | determine whether an all-momentum gap condition narrows or selects the coefficient | 7,183 samples are insufficient for an all-zone extremum; the route remains live | `BLOCKED-EQUIVALENT` |
| nonlinear action selector | finite-amplitude sourced equations and background stability | select `alpha` from nonlinear existence, uniqueness, or stability | current axioms supply no realized geometry action/background; Block 18 proves nonlinearity matters | `BLOCKED-EQUIVALENT` |
| Lorentzian or coarse-grained selector | transfer spectrum, reflection/causal condition, or renormalization fixed point | select a coefficient by dynamics rather than Euclidean inertia | kinetic isotropy supplies no transfer law or flow; no negative conclusion follows | `BLOCKED-EQUIVALENT` |
| realized background/source selector | law-selected boundary sector, source family, and coupling | determine `alpha` only after physical realization | neither the background nor source law is selected, so this independent route remains live | `BLOCKED-EQUIVALENT` |

Ten materially distinct mechanisms were tested or reduced. Two locate the
nonflat boundary, two execute the flat repair and coefficient-family test, one
checks invariance, and five preserve alternate background or stronger-physics
routes. Those live routes prevent promotion of finite-window nonselection into
a universal coefficient no-go.

### N2 — Wall-independence audit

The coefficient window shows that action form and coefficient choice must not
be collapsed. The remaining open conditions are:

- `W1`: select or derive the geometry action functional;
- `W2`: select its dimensionless coefficient;
- `W3`: select the background, constraint localization, and boundary ensemble;
- `W4`: replace finite samples by a complete continuous momentum-support
  theorem;
- `W5`: derive Lorentzian nonlinear stability, causal evolution, or a
  coarse-graining flow;
- `W6`: select the conserved matter/history source law and coupling.

| Pair | Does first close second? | Does second close first? | Independent? |
|---|---|---|---|
| `W1,W2` | no; choosing the deficit-square family leaves the interval (4a) | no; one coefficient does not derive the action family | yes |
| `W1,W3` | no; an action does not choose background or constraints | no; a background does not derive the action | yes |
| `W1,W4` | no; a selected action still needs an all-mode proof | no; a spectral theorem does not select its operator | yes |
| `W1,W5` | no; a Euclidean action does not supply dynamics or flow | no; dynamics does not alone derive the action functional | yes |
| `W1,W6` | no; geometry selection does not select matter coupling | no; a source law does not select geometry | yes |
| `W2,W3` | no; a coefficient does not choose its background | no; background selection leaves coefficient freedom | yes |
| `W2,W4` | no; a coefficient does not prove its full spectrum | no; a spectrum can bound without uniquely selecting a coefficient | yes |
| `W2,W5` | no; Euclidean window membership does not prove Lorentzian stability | no; a stability law may constrain but need not derive the coefficient | yes |
| `W2,W6` | no; the coefficient does not identify physical matter | no; a source law need not select the coefficient | yes |
| `W3,W4` | no; localization defines the operator but does not prove its spectrum | no; a spectrum does not select the physical localization | yes |
| `W3,W5` | no; a boundary choice does not derive causal evolution | no; evolution does not choose the compact/open constraint rule | yes |
| `W3,W6` | no; constraints do not select a source history | no; a history does not fix geometry constraints | yes |
| `W4,W5` | no; Euclidean all-mode invertibility is not Lorentzian stability | no; Lorentzian stability does not itself prove the Euclidean inventory | yes |
| `W4,W6` | no; a spectral gap does not identify physical matter | no; matter selection does not prove a quotient gap | yes |
| `W5,W6` | no; stable dynamics does not select its source | no; a source law does not prove stability | yes |

No listed wall follows automatically from another.

### N3 — Hidden-condition scan

| Phrase or premise | Classification |
|---|---|
| “background” | explicit supplied condition: either the Block-19 nonflat root or the exactly flat Regge anchor |
| “by construction” | avoided as proof language; equations (5) and (12) are derived by differentiating the local action |
| “the framework provides” | not used; current axioms and registered primitives are read directly and their non-supply is explicit |
| “standard QFT,” “naturally,” “obviously” | absent from the load-bearing derivation |
| “canonical” or “registered” | refers only to the machine-readable premise registry and the unchanged canonical memo, not to a physics selector |
| finite Brillouin scan | explicit bounded condition; never promoted to an all-`k` theorem |
| `1/128` endpoint | a deliberately safe rational boundary below the observed finite crossing, not a fitted or selected value |
| `alpha>0` | explicit condition needed to lift the extra branch; the singular limit `alpha=0` is excluded rather than hidden |
| eigenvalue monotonicity | exact consequence of the positive-semidefinite difference (13); endpoint inertias remain numerical on declared matrices |
| Euclidean signature | explicit supplied surface; no Lorentzian inference |

No hidden condition was promoted after the wall count.

### N4 — Residual matching

| Cited source | Source residual | Current residual | Match? |
|---|---|---|---|
| [Block 19](ADMISSIBILITY_FIXED_METRIC_NONLINEAR_REGGE_KKT_CONTINUATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | homogeneous five-normal existence and nondegeneracy at `k=0` | finite-momentum invertibility of the same background | no; used as the exact background source, not as a negative witness |
| [actual Regge second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) | flat fifth zero branch and leading Einstein comparator | action-native lift of that same fifth branch while retaining the comparator order | yes |
| [linearized action selection](CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md) | deficit-squared form is local, gauge-annihilating, nonzero, and `O(k^4)` but higher-order freedom remains | exact extra-branch curvature, unprojected body-source repair, full declared mode inventories, and a nonunique coefficient window | partial premise match only; cited as provenance, not counted as the new interval result |
| [closed-history source note](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | gauge-compatible body source rejected only by the fifth branch; projector as counter-control | same source repaired by the local action (4) | yes |

The nonmatching Block-19 residual is not counted as witness support. The new
finite-momentum computation carries claims (2)--(3) directly. For coefficient
selection, the prior higher-order-freedom residual matches the direction but
does not supply the present interval, endpoint, generalized crossing, or
source family; those are computed here.

### N5 — Rhetoric audit

The negative statements are bounded: the named background under each named
constraint extension exhibits a numerically bracketed loss of invertibility,
and the declared finite Euclidean linear repair criteria admit the entire
coefficient interval (4a). The first does not imply a gravity no-go; the
second does not imply that stronger physics cannot select a coefficient.

| Resolution | Executed? | Authorized statement |
|---|---|---|
| per element | yes | all 15 edge classes enter the local Hessian; no single-edge universal no-go is claimed |
| per site | yes | all 50 hinge classes and 240 incidences enter each uniform-cell kernel |
| per mode | yes | two spatial brackets give bounded numerical evidence for two soft-mode crossings; the coefficient interval is exhaustive only on the named finite matrices and samples |
| per block | yes | the nonflat and flat backgrounds are kept separate; failure or coefficient freedom in one is not transferred to the other |
| lattice wide | finite only | `L=3,...,10` and all five coefficient witnesses are exhaustive for the declared inventory; the continuous Brillouin zone remains explicitly open |

The primary runner's cached stdout contains the required substantive
`per_element`, `per_site`, `per_mode`, `per_block`, and `lattice_wide`
execution lines.

### N6 — Partial-closure paths

The primitive registry was checked directly:

- `minimal_axioms` leaves source/action and dynamics outside axiom content;
- `kinetic_isotropy_primitive` supplies only equal-form OS0 graining, not an
  action or Lorentz theorem;
- `scale_reference_primitive` supplies units only, not `alpha`;
- `realized_state_primitive` permits pointwise evaluation but selects no
  background or state.

Existing partial-closure paths remain live: derive the action and coefficient
from a continuous-zone extremum, nonlinear or Lorentzian stability,
coarse-graining, background/source realization, or another downstream law;
register a narrowly approved action-selection primitive by owner decision; or
replace the action family. A retained convention is permitted only for
genuine labeling content, not physical coefficient selection. This note
therefore does not say “a new axiom is required.” It records the exact
derivation-or-governance fork after eliminating only the bounded linear tests.

### N7 — Steelman

The strongest hostile response is decisive against a broad no-go: the
Block-19 root was never proposed as the unique physical vacuum, and discrete
gravity is expected to be tested after action improvement and background
selection. A local deficit-square term is precisely an available improvement;
on the flat branch it preserves gauge symmetry and the leading Einstein term
while lifting the extra mode. Therefore neither finite-momentum root licenses
“Regge gravity fails,” much less “gravity fails.” The actionable obligation is
to derive the improved action and prove its complete Lorentzian quotient
spectrum. The strongest response to coefficient nonselection is equally
decisive: gauge preservation, source solvability, and infrared order are
consistency conditions, not principles expected to determine a Wilson
coefficient. A nonlinear, Lorentzian, coarse-grained, or realized-law
criterion may still select it. This note accepts both steelmen, narrows the
negative results to the named extensions and criteria, and makes the stronger
selector the positive next route.

### N8 — Cross-cycle echo

Earlier cycles repeatedly retired carrier obstructions by changing the local
representative, ensemble, or nonlinear equation:

- the closed-history note's rank-one fifth-branch lift showed the residual was
  operator-dependent but supplied no action mechanism;
- Block 18 showed that the bare Regge extra branch is lifted cubically by the
  full nonlinear action;
- Blocks 13--16 retired several bare source residuals with conserved histories,
  neutralization, or reaction constraints rather than universal no-go claims.

Equation (4) applies the same repair discipline and advances it: the lift now
comes from a local action. Those precedents forbid promoting the two nonflat
roots into a universal conclusion. They also warn against converting one
successful dyadic control into a selected constant: earlier action-selection
work already exposed higher-order freedom. The interval (4a) quantifies that
echo for the actual branch/source criteria without closing the stronger
selector routes. No similar retired route has been omitted.

## 7. Promotion Value And Cluster-Cap Gate

| Gate | Required answer and evidence |
|---|---|
| V1 — specific obstruction | The Block-14 source note says: “A lifted action, alternate triangulation, or balanced multi-edge junction is a concrete unclosed mechanism.” Block 19 separately leaves “Lorentzian plus inhomogeneous stability” as the strongest next gravity obligation. Equation (4) closes the lifted-action mechanism for the named body source; equations (2)--(3) execute, rather than close, the inhomogeneous test. No audit verdict is claimed because these stacked parents remain audit-pending. |
| V2 — new derivation and search | At `origin/main@39c74017b870c27c804e3992f2a11e90336476b2`, the searches below find the June-10 deficit-squared higher-order witness as the only matching Regge hit. It establishes local/gauge/`O(k^4)` provenance but none of (2), (3), (7a), the body solve, or the mode inventories. Those are the new derivations. |
| V3 — already completable by generic machinery? | No. Generic Schur complements or curvature formulas do not supply the repository's 50-hinge Kuhn/Coxeter kernel, its isolated fifth branch, the Block-19 nonflat background, the exact source residual, or the finite spectra. Each is computed from framework-specific retained carrier data. |
| V4 — marginal content nontrivial? | Yes. The result combines an exact number-field coefficient, two independently reconstructed nonflat kernels, 25,308 exhaustive finite modes, 7,183 disclosed samples, and a source-range reversal under an actual local action. It is not a definition or textbook identity. |
| V5 — one-step variant? | No. The closest origin-main row only exhibits deficit-square freedom and its infrared order. The closest campaign row uses an inserted rank-one projector. This block instead derives the action Hessian, executes the extra branch and source, and computes the previously absent nonflat spectrum. |

The refreshed prior-art commands were:

```text
git grep -n -iE '(curvature[- ]squared.*Regge|Regge.*curvature[- ]squared|deficit[- ]squared|R\^2.*Regge|Regge.*R\^2)' origin/main -- 'docs/*.md' 'docs/**/*.md' 'scripts/*.py'
git grep -n -iE '(fifth branch.*lift|extra branch.*lift|nonmetric.*branch.*lift|rank.one.*lift)' origin/main -- 'docs/*.md' 'docs/**/*.md' 'scripts/*.py'
git grep -n -iE '(inhomogeneous.*Regge.*stability|Regge.*inhomogeneous.*stability|finite.momentum.*Regge.*background|nonflat.*Regge.*Hessian|Regge.*soft.mode)' origin/main -- 'docs/*.md' 'docs/**/*.md' 'scripts/*.py'
git ls-tree -r --name-only origin/main -- docs scripts | rg -i '(regge|curvature.*square|higher.*derivative)'
```

**Cluster-cap evaluator verdict: `OPEN`.** This is the twentieth campaign
block and another gravity-family PR, so the local four-question evaluator is
mandatory. First, content integrity is genuinely new: earlier blocks derived
the flat carrier, sources, an algebraic projector control, nonlinear
homogeneous lift, and one constrained root; none constructed the nonflat
Bloch Hessian or evaluated a local curvature-square repair against the fifth
branch and body source. Second, the claim has a standalone identity. Its
review object is one action modification plus one explicitly separated
nonflat diagnostic, not another source label or Fourier census under an
unchanged operator. Third, it stands on its own merits: the exact flat
identity, exact coefficient (7a), periodic-action controls, source reversal,
and mode inventories can each be reviewed and falsified independently. The
parents supply inputs but do not imply those outputs. Fourth, the marginal
review value justifies a separate PR because the result changes the repair
mechanism from an inserted projector to a local action and converts an
unspecified inhomogeneous obligation into two computed boundaries. Combining
it silently with Block 19 would conflate a nonflat diagnosis with a distinct
flat repair and obscure their different premises. The claim remains one
bounded cluster; it does not split scans or candidate wording into extra
headline claims. This evaluator decides PR opening only, not audit outcome.

### Coefficient-window extension value and cluster decision

| Gate | Extension-specific evidence |
|---|---|
| V1 — specific obstruction | Block 20 left coefficient selection as its first action-law obligation. The interval result directly tests whether the already named gauge, source, inertia, and infrared conditions select the supplied `1/1024`. |
| V2 — new derivation and search | Searches of `origin/main`, the June action-selection packet, and the complete stacked branch find higher-order freedom and the single supplied repair point, but no `0<alpha<=1/128` theorem, finite generalized crossing, or coefficient-family source solve. |
| V3 — generic machinery | Loewner monotonicity is generic, but the quotient positivity, endpoint inertia, first crossing, source kernel, and margins are properties of the actual 50-hinge/15-edge operator and must be computed. |
| V4 — marginal content | `126,540` exhaustive mode-coefficient evaluations, `35,915` stress-coefficient evaluations, exact monotonicity, and the `0.0098646245597...` crossing turn “alpha is supplied” into a concrete nonuniqueness interval. |
| V5 — one-step variant | The computation materially changes the selector conclusion, but it uses the same action/operator and is a direct extension of the open Block-20 packet rather than an independently reviewable carrier. |

**Extension cluster-cap verdict: `FOLD`.** The coefficient window is valuable
science, but opening a twenty-first gravity-family PR would split one local
action claim across adjacent reviews. It is therefore folded into the existing
Block-20 PR #6091. This verdict limits packaging, not the scientific claim or
its independent-audit requirement.

## 8. Verification

Run:

```bash
python3 scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py
```

The runner independently checks:

1. current-axiom and approved-primitive non-supply boundaries;
2. exact reconstruction of the retained flat Regge Bloch kernel;
3. reduction of the nonflat kernel to the Block-19 `k=0` Hessian;
4. a periodic `L=3` finite-momentum second difference on the nonflat action;
5. both soft-mode determinant brackets;
6. the exact flat curvature-square Hessian identity, `k=0` coefficient window,
   and first negative-mode crossing;
7. a periodic `L=3` second difference of the extended action;
8. direct repair of the gauge-compatible body-edge source across five dyadic
   coefficients;
9. positive-semidefinite monotonicity, `126,540` coefficient evaluations, and
   the first generalized crossing on all 25,308 nonzero modes of
   `L=3,...,10` tori;
10. `35,915` coefficient evaluations on 7,183 deterministic Brillouin stress
    samples; and
11. `O(k^4)` versus `O(k^2)` infrared scaling at both ends of the dyadic
    control range.

The canonical axiom memo and the campaign's fixed percentages are unchanged.
No `review-loop` is used.

## Boundary Verdict

The urgent gravity diagnosis is now sharper than “the nonlinear route may be
unstable.” The Block-19 nonflat homogeneous root has double-precision-
bracketed finite-spatial-momentum soft-mode crossings under both tested
constraint localizations, so neither named extension yet supplies a globally
invertible gravity background. An interval root certificate remains open.

Gravity is not thereby lost. On the flat weak-field branch, a local
curvature-square action lifts the spurious fifth lattice mode, preserves the
four gauge modes and ten constant-metric zeros, repairs a previously rejected
source, and leaves the infrared Einstein order intact over every declared
test. The same criteria admit every `0<alpha<=1/128`, so they cannot select
the original `1/1024`. The immediate science priority is no longer guessing
whether a repair exists or whether its bounded linear tests select a point;
it is testing continuous-zone, nonlinear, Lorentzian, coarse-grained, and
realized-law selectors while constructing the nonlinear source evolution.
