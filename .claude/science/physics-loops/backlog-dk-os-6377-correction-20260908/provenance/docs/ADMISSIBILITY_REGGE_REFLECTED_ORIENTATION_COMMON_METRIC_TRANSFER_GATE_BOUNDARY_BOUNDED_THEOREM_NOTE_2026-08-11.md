---
claim_id: admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the supplied repaired flat four-dimensional Kuhn/Coxeter Regge edge action at alpha=1/1024, direct identification of the sampled single-orientation conditional poles with one-step transfer eigenvalues lambda=exp(-omega) is incompatible with a positive self-adjoint transfer because the finite-lattice pole phases make lambda nonreal. The minimal local union of the fifteen-edge complex and its time reflection has twenty-two edge classes, an exact momentum-dependent reflection involution, four exact displacement Ward columns, and a thirteen-dimensional constant-metric flat fiber. Ten directions are one common metric; the exact three-direction excess is the relative forward/backward h_it sector. Each orientation-separable action annihilates that full fiber, so coefficient retuning cannot lift the excess, and the declared nonzero static-axis sample retains a fifth null beyond four gauge columns. Identifying the two orientation metrics before averaging their complete-edge stationary Schur operators gives an exactly reflection-covariant Ward operator with one real positive tensor pole per transverse parity sector at four declared momenta, a positive conditional decaying two-step spectral kernel, and the infrared static residue. The common-metric identification, a local cross-orientation action, the action-to-physical-transfer map, physical inner product, decaying-branch rule, and Record clock/update are not selected. This is a narrow direct-transfer and orientation-separable boundary with a viable conditional repair, not a gravity no-go, selected dynamics, axiom amendment, or TOE closure."
upstream_dependencies:
  - minimal_axioms
  - admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_bounded_theorem_note_2026-08-11
  - admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_axiom_boundary_bounded_theorem_note_2026-08-11
  - admissibility_joint_record_gravity_law_five_control_axiom_cut_gate_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py
---

# Reflected-Orientation Common-Metric Regge Transfer Gate

**Date:** 2026-08-11

**Type:** bounded theorem

**Role:** decide whether the Block-47 conjugate pole pair already defines a
positive physical transfer, and identify the smallest exact repair target when
it does not.

**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py](../scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py)

## Result Up Front

The direct single-orientation transfer reading fails, but gravity does not.

On the supplied Block-47 continuation, the two complete-edge tensor poles are
slightly complex away from the infrared. If one directly calls

~~~text
lambda_1(k) = exp[-omega(k)]                              (1)
~~~

the eigenvalues of a one-step transfer, at least one `lambda_1(k)` is nonreal
on the declared sample. A positive self-adjoint operator has real
nonnegative spectrum. Therefore this direct identification cannot be the
positive one-step physical transfer. Similarity transformation or a change of
positive inner product cannot alter that spectrum.

The smallest local time-reflection completion is also not yet the answer.
The original fifteen edge classes and their reflected labels glue on eight
classes and form a twenty-two-edge union. Its averaged Laurent symbol has an
exact time-reflection involution, exact two-sided displacement Ward identities,
and the coefficient pairing `Q_{-s}=Q_s^T`. Yet its constant flat fiber has
dimension thirteen, not ten. The excess is exactly the three relative
forward/backward mixed-time metric components `h_it^+ - h_it^-`. Each of the
two orientation-local actions separately annihilates this full fiber, so
retuning their two scalar coefficients cannot remove the extra directions.
At every one of eight declared nonzero static-axis momenta, the union has five
nulls: four gauge directions plus one extra branch.

There is a viable narrower repair candidate. Identify the two orientation
metrics as one metric before averaging the two complete-edge stationary Schur
operators. The resulting ten-component operator is exactly time-reflection
covariant, retains its Ward columns, has one real positive tensor pole in each
transverse parity sector at all four declared transfer momenta, and retains the
infrared static residue. Selecting the decaying roots gives the positive
diagonal two-mode spectral candidate

~~~text
T_2(k) = diag(exp[-2 omega_even(k)], exp[-2 omega_odd(k)]). (2)
~~~

Equation (2) is conditional spectral data. The current result does not derive
a local reflected action whose physical quotient is this operator, an
Osterwalder--Schrader half-space form, a physical inner product, or the Record
event that counts one or two transfer steps.

This is significant blocker localization and a mathematical repair candidate,
not TOE progress. The exact missing gravity-law content now includes a
**three-component orientation-shift intertwiner** together with the
action-to-physical-transfer and Record-clock identifications. This is **not a
gravity no-go**. No canonical axiom is edited. No TOE percentage moves.

## Inputs And Non-Imports

| input | used here | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | the current law, update, and physical-selection boundary | a Hamiltonian, transfer operator, action, physical norm, reflection, or Record clock |
| [full-edge finite-frequency parent](ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the repaired `alpha=1/1024` Laurent kernel, exact Ward columns, parity quotient, and conditional poles | a physical transfer, inner product, or interpretation of pole phase |
| [infrared Einstein/TT parent](ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the complete-edge stationary metric Schur operator and static residue | action selection, nonlinear constraints, or Lorentzian evolution |
| [joint-law cut gate](ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the exact immutable `L*` target and separation of Record, clock, constraint, and source controls | extensional values for that law or an axiom amendment |
| [free staggered two-step precedent](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md) | the distinction between conditional spectral positivity and an action-to-physical map | a fermionic CAR construction for gravity or a gravity positivity theorem |

The flat coframe, Kuhn/Coxeter orientation, coefficient `alpha=1/1024`, time
reflection, analytic continuation, and Euclidean coordinate diagnostics are
declared features of this bounded surface. They are not promoted into the
foundation.

The approved [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies only the Euclidean OS0 form `c_t=c_s`; it does not supply the
reflection completion or physical transfer. The
[scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) supplies units
only. The [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
supplies pointwise evaluation only. None selects the objects tested below.

## Direct One-Step Positive-Transfer Obstruction

For a positive self-adjoint transfer operator `T` on a positive Hilbert space,

~~~text
spec(T) subset [0,infinity).                               (3)
~~~

The Block-47 pole equation is instead a conditional analytic equation for the
complete edge symbol at

~~~text
q = (k,0,0,-i omega).                                      (4)
~~~

At `k=0.4` and `k=pi/2`, the runner recomputes both transverse parity roots
from the raw Laurent symbol. The maximum pole phase on those four roots
exceeds `6e-4`, and the maximum imaginary part of `exp(-omega)` exceeds
`1e-4`. Thus (1) violates (3).

This conclusion is deliberately narrow. It rejects only the literal
single-orientation, one-pole/one-eigenvalue, positive self-adjoint one-step
identification. It does not reject a reflected two-step composition, a
common-metric carrier, a unitary dilation, an indefinite auxiliary edge
space, or an OS reconstruction with a different physical quotient.

## Minimal Local Time-Reflection Union

Let

~~~text
D_+ = {d in {0,1}^4 : d != 0},
R_t = diag(1,1,1,-1).                                     (5)
~~~

The seven purely spatial classes are fixed by `R_t`. The pure negative-time
edge is the reverse of the positive-time class after a base-cell shift. Those
eight classes are shared. The seven mixed-time diagonals of `D_+` and their
seven reflected partners are distinct, giving

~~~text
15 + 15 - 8 = 22                                          (6)
~~~

union edge classes.

For each real-space coefficient `Q_s^+`, reflection maps the endpoints as
well as the displacement. If reflected edge labels require base offsets
`b_a,b_b`, its exact transformed shift is

~~~text
s^- = R_t s + b_b - b_a.                                  (7)
~~~

The runner applies (7) coefficient by coefficient and forms

~~~text
Q_union(q) = (Q_+(q) + Q_-(q))/2.                         (8)
~~~

There are `133` shifts, with maximum transpose-pairing error below `5e-15`.
The momentum-dependent label/base-shift matrix `Theta(q)` obeys

~~~text
Theta(R_t q) Theta(q) = I,
Q_union(q) = Theta(-q)^T Q_union(R_t q) Theta(q).           (9)
~~~

The maximum tested covariance error is below `5e-14`, and the involution error
is below `1e-14`. At real and complex declared momenta, all four displacement
columns have rank four and the two-sided Ward residual is below `5e-13`.

These are exact local reflection and gauge facts for (8). They do not yet make
(8) a physical transfer.

## Exact Thirteen-Versus-Ten Fiber

Let `M_+` and `M_-` be the constant edge-length maps from the ten symmetric
metric components for the two orientations. Equality on the eight shared
edge classes gives an `8`-by-`20` constraint matrix `C`. Exact radical
arithmetic for the maps and numerical rank reconstruction agree that

~~~text
rank(C) = 7,
dim ker(C) = 20 - 7 = 13.                                 (10)
~~~

The seven independent shared data are the six spatial metric components and
`h_tt`. One common four-metric has ten components. Consequently

~~~text
ker(C) = common metric (dimension 10)
         plus relative (h_xt,h_yt,h_zt) (dimension 3).     (11)
~~~

The three relative columns are independent, have zero shared-edge residual,
and together with the common-metric columns span the full thirteen-dimensional
fiber. The zero-momentum union symbol has inertia

~~~text
(negative, positive, zero) = (7,2,13)                     (12)
~~~

and annihilates all thirteen columns.

More strongly, both orientation components in (8) separately annihilate the
full fiber. Hence every orientation-separable retuning

~~~text
a Q_+ + b Q_-                                              (13)
~~~

does so too. Lifting the relative `h_it` directions requires a cross-
orientation term, identification, or quotient. It cannot come from choosing
different values of `a` and `b`.

At the eight declared static momenta

~~~text
k in {0.05,0.10,0.20,0.40,0.80,pi/2,2.40,pi},             (14)
~~~

the union inertia is `(14,3,5)`. Its nullity is five, and adjoining the four
gauge columns to the computed null basis still has rank five. Thus one exact
gauge-invariant static branch remains on this sample. The next singular gap
stays above `4e-4`.

Equations (10)--(14) are the precise orientation-separable boundary. They are
not a claim that every reflected Regge construction has an extra physical
mode.

## Common-Metric Repair Candidate

Let `E_+(q)` be the Block-47 ten-component stationary Schur operator obtained
only after eliminating the full five-dimensional nonmetric complement of the
fifteen-edge symbol. Let `R_h` flip the three `h_it` components and fix the
other seven metric components. The common-metric candidate is

~~~text
E_com(q) = [E_+(q) + R_h E_+(R_t q) R_h]/2.               (15)
~~~

This is not a metric-only projection of the original edge Hessian: each term
first includes the stationary complete-edge nonmetric dressing. It then makes
one additional identification—the two orientations describe the same metric.

The runner verifies

~~~text
E_com(q) = R_h E_com(R_t q) R_h                           (16)
~~~

and its two-sided metric Ward identities at real and complex declared
momenta. Reflection error is below `5e-14`; the absolute Ward residual is
below `5e-12`.

After exact transverse-parity gauge bordering, the sampled pole inventory is:

| `k` | even / cross `omega` | odd / plus `omega` |
|---:|---:|---:|
| `0.10` | `0.099918904223` | `0.099919621616` |
| `0.40` | `0.394911593176` | `0.394947166453` |
| `pi/2` | `1.326661840743` | `1.323950908830` |
| `pi` | `1.797380948536` | `1.784483004734` |

All eight roots are real to the runner tolerance, positive, isolated from the
next bordered singular direction, and retain the Ward quotient. The table is
a declared finite sample, not an all-momentum or stability theorem.

Choosing the decaying roots makes every diagonal entry in (2) lie strictly
between zero and one. On the static source probes `k=0.025,0.05,0.10,0.20`,
the computed values of `k^2 h_tt` converge to `2`, with the lowest-momentum
error below `1e-4` and maximum declared deviation below `0.02`. Thus the
reflection repair does not discard the parent infrared source residue.

Positivity of the two numbers in (2) is not positivity of an action-derived
physical Hilbert transfer. The missing theorem must construct the carrier,
inner product or OS form, and action-to-physical-transfer intertwiner, then
show that its spectrum is (2) while preserving the constraints and source
response.

## Exact Joint-Law And Axiom Consequence

Block 46 identified the sufficient constitutional target as one exact joint
law `L*` binding Record extension, event precedence, clock continuation,
constraint transport, and source decoding. The present calculation makes one
part of that target more concrete.

For this Regge route, an extensional candidate must now specify at least:

1. whether successive local updates alternate the two orientations or first
   identify a common metric;
2. the three-component orientation-shift intertwiner that removes, constrains,
   or dynamically couples the relative `h_it` sector;
3. a local action or update whose physical quotient yields the decaying tensor
   channel with a positive physical inner product;
4. which Record event is one physical step, including whether (2) is one event
   or two; and
5. preservation of the four displacement constraints and the same static
   source residue under that update.

The current axioms permit structural kinetic isotropy but do not extensionally
choose these values. Conversely, (15) shows that the supplied gravity evidence
does not justify declaring them impossible. The correct next task is to derive
this piece of `L*` from the Record/Admissibility law or present the smallest
explicit owner-facing amendment after competing constructions are tested.

No axiom edit is ready merely because a choice has been localized. In
particular, importing “use the common metric and decaying two-step branch”
would rename the target rather than derive it. No canonical axiom is edited.
No TOE percentage moves.

## Portfolio Decision

This block ends the current finite-frequency regulator-repair sequence. The
following work does not clear the value gate unless a new mechanism changes
the obligation graph:

- denser samples of the same single-orientation poles;
- more coefficients in the separable combination (13);
- more static source fixtures on the same quadratic symbol; or
- a common-metric pole grid without a local physical carrier.

The highest-value next seam is binary: construct a Record-faithful local
orientation/metric transfer realizing (15), or prove that the exact current
Record/Admissibility form cannot select its required intertwiner and step map.
Only the first closes a physical gravity obligation; the second justifies a
precise axiom-candidate request. Nonlinear constraint propagation, a stable
nonflat phase, and full-`Z^3` control remain downstream rather than substitutes
for this interface.

## No-Go Discipline Gate

The only negatives shipped here are:

- the literal single-orientation `lambda=exp(-omega)` spectrum is not a
  positive self-adjoint one-step transfer on the declared sample; and
- scalar retuning of the two orientation-separable constant-metric actions
  cannot lift their exact three-direction relative-shift fiber.

No broader gravity, reflection, transfer, or axiom no-go is asserted.

### N1 — Alternative Route Enumeration

The route families are normalized by mathematical object, mechanism, and
terminal obligation.

| family | attack and terminal obligation | result against the narrow negatives | marker |
|---|---|---|---|
| direct one-orientation edge transfer | Use the complete fifteen-edge pole as one one-step eigenmode and prove positive self-adjointness. | Recomputed nonreal `exp(-omega)` violates the necessary real-spectrum condition; this is the first narrow negative. | `ATTEMPTED` |
| locally reflected separable edge action | Glue the reflected edge complex locally and retune the two orientation weights until only one metric remains. | Exact rank `(13 versus 10)` and separate annihilation by both actions show scalar retuning cannot lift the three relative shifts; this is the second narrow negative. | `ATTEMPTED` |
| alternating-orientation monodromy | Pair conjugate forward/backward pole factors over two steps so their product is positive. | The spectral product `exp(-2 Re omega)` succeeds conditionally and therefore defeats any broad no-go, but it changes the one-step object and still lacks a local physical intertwiner. | `ATTEMPTED` |
| metric-first carrier | Identify both orientation metrics before averaging the complete-edge stationary operators, then prove the physical quotient. | Equation (15) passes reflection, Ward, sampled real-pole, and residue gates. It is a live repair, not a counterexample to either narrow statement because it adds the missing identification. | `ATTEMPTED` |
| unitary dilation | Embed the contractive complex one-step channel in a larger unitary evolution and recover the tensor mode by compression. | The spectral-level dilation route remains open and is not a positive self-adjoint transfer on the original edge carrier; locality, constraints, and Record recovery are its terminal obligations. | `ATTEMPTED` |
| OS half-space reconstruction | Derive a reflection-positive half-space form directly from the twenty-two-edge Euclidean action. | The exact reflection involution is supplied, but the extra static branch and absent boundary form prevent completion in this block. It remains open and is not claimed ruled out. | `ATTEMPTED` |

At least three materially different live routes remain. That is why this note
ships a partial narrowing rather than a gravity or transfer no-go.

### N2 — Wall-Independence Audit

After collapsing downstream consequences, the current repair has three open
conditions:

- `W_G`: derive the common-carrier or cross-orientation shift intertwiner;
- `W_H`: derive a positive physical transfer/inner product from the action;
- `W_R`: identify the physical step with a Record-faithful event update.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `W_G`, `W_H` | no | no | yes |
| `W_G`, `W_R` | no | no | yes |
| `W_H`, `W_R` | no | no | yes |

A common carrier need not be positive; a positive spectral kernel need not
come from the Regge action; and either can exist without a Record occurrence
law. Nonlinear propagation and full-`Z^3` control are downstream obligations,
not inflated into this wall count.

### N3 — Hidden-Wall Scan

The proof was scanned for “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.” No load-bearing
choice is hidden behind those phrases.

- The flat coframe, orientation, coefficient, reflection, and continuation
  are disclosed bounded-surface inputs above.
- “Canonical” occurs only in the statement that no canonical axiom is edited;
  it grants no premise.
- The approved primitive registrations are cited from their actual source
  notes and are used only for their declared narrow content.
- The common-metric identification, decaying branch, and transfer-step reading
  are explicit open conditions `W_G`, `W_H`, and `W_R`.

### N4 — Residual Matching

| cited witness | witness residual | present residual | match? |
|---|---|---|---:|
| [Block 47, lines 90--96](ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | complete-edge poles lack a physical transfer, inner product, and Record clock | `W_H` and `W_R` | yes |
| [Block 46, lines 234--290](ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md) | exact `L*` and physical inner-product controls remain extensional | the sharpened `W_G`, `W_H`, `W_R` portion of `L*` | yes, as refinement rather than proof |
| [free two-step note, lines 14--15 and 369--391](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md) | action-to-physical-CAR/OS identification is open for a free fermion recurrence | gravity action-to-physical transfer | no; analogy only, dropped as a proof witness |
| [count/rate note, lines 60--70](MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06.md) | Record counts do not by themselves provide a clock-rate denominator | `W_R` physical transfer-step identification | partial analogy only, dropped as proof witness |

Only the Block-47 residual is used as a prior negative witness. Block 46 is a
target decomposition. The other two sources motivate routes but do not prove
the gravity residual.

### N5 — Rhetoric Audit

| resolution | actually checked | narrow conclusion licensed |
|---|---:|---|
| per element | yes | every reflected label and Laurent coefficient obeys the declared map and pairing |
| per site | yes | one local original-plus-reflected unit-cell union has the exact involution |
| per mode | yes, finite declared samples | direct complex transfer factors, the fifth static branch, and common-metric poles only on those samples |
| per block | yes | exact `13 versus 10` constant fiber, separable annihilation, and conditional two-mode spectrum |
| lattice-wide | no | no alternating full-`Z^3` law, half-space OS form, nonlinear phase, or Record update is inferred |

Accordingly, the source does not say that reflection cannot repair gravity or
that a physical transfer does not exist. The primary runner prints and caches
the matching five-resolution execution certificate.

### N6 — Partial-Closure Path Scan

Three partial closures are kept separate from new physics:

1. Treating the two lattice orientations as regulators of one metric is a
   carrier identification candidate. It closes the three-coordinate doubling
   at the linear level only if derived or explicitly ratified; equation (15)
   shows what it would close.
2. Separating transfer-step **count** from clock **rate**, as in the
   [count/rate source](MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06.md),
   could let an alternating two-step count be established before a physical
   rate. It does not by itself close `W_R`.
3. The approved scale-reference, kinetic-isotropy, and realized-state
   primitives chain-satisfy only units, OS0 form, and pointwise evaluation.
   None closes `W_G`, `W_H`, or `W_R`.

No statement that a new axiom is required is made. If the common-metric
identification is only a convention, an explicit interpretation/registration
could close `W_G`; the physical transfer and Record update would still require
derivation. A proposed primitive absent from the registry has zero premise
weight until owner approval.

### N7 — Steelman

A hostile reviewer can make a strong concrete case that the apparent problem
is regulator bookkeeping: the physical field is one metric, while the forward
and reflected Kuhn complexes are two coordinate realizations of it. On that
reading the thirteen-dimensional edge-union fiber is never the physical
carrier; the correct map is the diagonal ten-dimensional metric embedding.
Equation (15) then supplies the obvious linear candidate, and its exact
reflection covariance, Ward identities, real tensor roots, positive decaying
two-step spectrum, and static residue show that the physics may already be
consistent. The actionable terminal obligation is to construct a local
twenty-two-edge cross-orientation quadratic or OS boundary form whose Schur
quotient is (15), then tie one alternating pair to a Record event. Until that
construction is tried, any broad no-go is premature. The present claim is
therefore demoted to the two narrow negatives stated above; common-metric
identification is **not proved necessary** globally.

### N8 — Cross-Cycle Echo

- The [free staggered two-step note](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  found positive conditional two-step spectral/Fock data while leaving the
  action-to-physical map open. That residual has not been retired and warns
  against calling (2) a physical transfer.
- The [count/rate note](MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06.md)
  retired an overbroad clock obstruction by separating step count from rate.
  The same mechanism is applied here: an alternating-orientation two-step
  count remains live even though its Record rate/meaning is open.
- The [gravity reflection-sign note](GRAVITY_SIGN_FROM_REFLECTION_POSITIVITY_UNITARITY_REDUCES_TO_EMERGENT_DIFFEOMORPHISM_NARROW_THEOREM_NOTE_2026-06-08.md)
  made the sign conditional on reflection-positive physical mode selection.
  The present note supplies a reflection-completed candidate but does not
  silently import that physical selection.
- Block 47 showed momentum-reversal conjugacy rather than a same-sign growth
  rate. The reflected and common-metric routes explicitly use that opening.

The analogous partial-closure mechanisms have therefore been considered; none
licenses a broader negative.

**Status: PASS.** The two negatives are exact and narrowly quantified, at
least five distinct attack families are recorded, the three residuals remain
separate, the viable common-metric and alternating-orientation routes remain
open, and the N5 certificate lands in the runner cache.

## Reproduction

~~~bash
python3 scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py
python3 scripts/cached_runner_output.py --refresh \
  scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py
~~~

Expected final line:

~~~text
TOTAL: PASS=14 FAIL=0
~~~
