---
claim_id: admissibility_regge_full_conserved_source_multimode_metric_completion_ward_refinement_boundary_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "For the repository's actual four-dimensional Kuhn/Coxeter Regge-plus-deficit-square action at alpha=1/1024 and the skew momentum ray n=(1,2,3,0), complete six-dimensional transverse symmetric-source bases are constructed and solved at k and 2k. The exact quadratic action-gradient tensor is evaluated on all 21 symmetric equal-mode source pairs with output 2k and all 36 unequal-harmonic k-plus-2k source pairs with output 3k. On periods L=145,193,257, after the fixed square-root metric completion, the equal-mode full-tensor force and Ward powers are 1.9872 and 3.0148; the unequal-harmonic powers are 1.9592 and 3.0189. The completion/raw fractions fall to 0.0199 and 0.0521, and the completion reaction is Ward-null below 2e-12. Frobenius tensor norms bound unit coefficient combinations in the orthonormal metric-response basis; the invertible transformed physical-source map has condition number below 1.86 and singular values proportional to momentum squared, so this is not stated as a fixed-unit-physical-source norm bound. This closes the special-polarization and equal-input loopholes on one generic collinear ray. It is not a uniform angular theorem, noncollinear multimode theorem, all-L/refinement bound, observable-decoupling theorem, nonlinear solved-branch theorem, full-Z3 construction, selected source/action law, nonlinear Lorentzian stability theorem, axiom amendment, audit verdict, or TOE percentage movement."
upstream_dependencies:
  - minimal_axioms
  - admissibility_regge_nonlinear_metric_completion_skew_momentum_ward_refinement_boundary_bounded_theorem_note_2026-08-12
  - admissibility_regge_nonaxial_momentum_ward_k3_factorization_refinement_boundary_bounded_theorem_note_2026-08-12
  - admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12.py
---

# Full Conserved-Source And Multimode Metric-Completed Regge Ward Boundary

**Date:** 2026-08-12

**Type:** `bounded_theorem`

**Role:** test whether Block 61's metric-completed cubic Ward law was an
artifact of two selected polarizations or of equal-input single-mode forcing.

**Audit-status authority:** independent audit lane only. This source authors
no audit verdict and predicts none.

**Primary runner:**
[admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12.py](../scripts/admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12.py)

**Repository dependencies:** the current
[minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md), the
[Block-61 nonlinear metric completion](ADMISSIBILITY_REGGE_NONLINEAR_METRIC_COMPLETION_SKEW_MOMENTUM_WARD_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md), the
[Block-60 nonaxial Ward mechanism](ADMISSIBILITY_REGGE_NONAXIAL_MOMENTUM_WARD_K3_FACTORIZATION_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md), and the
[Block-53 causal two-TT update](ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md).

## Result Up Front

Use the less-symmetric ray

```text
n=(1,2,3,0),                 k=(2 pi/L)n.           (1)
```

At any nonzero `k`, a conserved symmetric source obeys

```text
k_mu T_(mu nu)=0.                                      (2)
```

The transverse vector space has dimension three, so its symmetric square has
dimension six. The runner constructs a Frobenius-orthonormal tensor basis for
that complete space, maps it to all fifteen edge sources, solves the complete
eleven-dimensional nongauge response, and changes basis so the six metric
responses are orthonormal. It repeats the construction at `2k` and retains
the transformed physical-source basis rather than identifying the two norms.

Thus this block executes the full six-dimensional transverse source class at
both input harmonics. Source Ward residuals, response residuals, and basis
orthonormality errors remain below `1.4e-14` on the retained tail. The
transformed physical-source map has condition number below `1.86`; after
division by the corresponding input momentum squared, all singular values
lie between `0.49` and `0.94`. No source direction becomes singular beyond
the expected inverse-response `k^2` scale.

Let `B_(k1,k2)` be the symmetric quadratic action-gradient force. There are
two complete tensors:

```text
equal input:       B_(k,k),       Sym^2(R^6), 21 components, output 2k;
unequal input:     B_(k,2k),      R^6 x R^6,  36 components, output 3k. (3)
```

No source pair is selected after seeing its result. The runner evaluates all
21 and all 36 components, then reports the Frobenius norm of each complete
edge-force and Ward tensor. These norms bound every unit coefficient
combination in the orthonormal metric-response basis. They are not promoted
to a fixed-unit-physical-source Frobenius bound; the explicit source singular
values convert between those normalizations.

For unequal inputs the stored convention is

```text
B_(k,2k)(a,b) = (1/2)[F(a_k+b_(2k))]_(3k).          (4)
```

The self terms have output `2k` and `4k`, so only the two ordered cross terms
enter `3k`; division by two stores the symmetric bilinear coefficient.

For first-order edge modes `d_1,d_2`, the square-root metric embedding fixes
the symmetric bilinear completion

```text
C(d_1,d_2)_e = -d_(1,e)d_(2,e)/(2 ell_e).            (5)
```

For distinct input modes the full mixed coefficient before the one-half
bilinear convention in (4) is `2C`, as required by polarization. The stored
reaction therefore uses `C`. This coefficient is fixed by the
metric-to-length map before the action force is evaluated; it is not fit to
any source component.

On `L=145,193,257`, the complete tensor norms give:

| tensor | completed-force power | maximum fit residual | spread of `||F||/|k|^2` | Ward power | spread of `||W||/|k|^3` |
|---|---:|---:|---:|---:|---:|
| all 21 equal-mode pairs | 1.987246 | 0.00068 | 1.00733 | 3.014849 | 1.00854 |
| all 36 unequal-harmonic pairs | 1.959182 | 0.00213 | 1.02364 | 3.018894 | 1.01088 |

The normalized tail values are:

| `L` | equal `F/k^2` | equal `W/k^3` | equal completed/raw | unequal `F/k^2` | unequal `W/k^3` | unequal completed/raw |
|---:|---:|---:|---:|---:|---:|---:|
| 145 | 28.270417 | 4.491407 | 0.062231 | 72.736229 | 14.998618 | 0.160324 |
| 193 | 28.402393 | 4.466619 | 0.035195 | 73.825501 | 14.891942 | 0.091786 |
| 257 | 28.477555 | 4.453394 | 0.019865 | 74.455596 | 14.837289 | 0.052079 |

The completion reaction is

```text
R(k_1+k_2)=Q(k_1+k_2)C(k_1,k_2).                    (6)
```

The exact flat Hessian annihilates every displacement column, hence

```text
Gamma(k_1+k_2)^dagger R(k_1+k_2)=0.                (7)
```

The maximum executed reaction Ward norm is below `1e-15`. The completion
removes the nonmetric coordinate reaction but does not tune away the measured
Ward tensor.

Together, (1)--(7) establish on the executed ray and complete source bases:

```text
metric-completed bilinear force:        O(|k|^2),
displacement Ward tensor:               O(|k|^3),
equal-mode source pairs retained:       21/21,
unequal-harmonic source pairs retained: 36/36.       (8)
```

This closes the two most immediate source-side objections to Block 61:
neither the two selected polarizations nor equal-input forcing generated the
observed order.

## What Changed Scientifically

Block 61 proved the exact constant-metric second-jet identity and tested two
sources on one skew ray. This block promotes that source test from two vectors
to a complete finite-dimensional bilinear tensor. The response-normalized
Frobenius bounds and explicit invertible source map mean there is no untested
polarization inside the six-dimensional transverse source space at `k` or
`2k` for the retained ray. They do not erase the physical inverse-response
scale.

It also supplies the first unequal-input nonlinear resonance test in this
route. Every one of the 36 `k+2k -> 3k` coefficients has entered the aggregate
tensor. The same metric completion leaves a quadratic force and cubic Ward
tail.

This is significant mechanism progress. It is not scored TOE progress: one
collinear ray does not provide angular uniformity, and a soft Ward tensor does
not by itself prove that pseudo-modes decouple from physical observables.

## Refinement And Observable Boundary

The remaining emergent-gravity contract is narrower:

1. extend (8) uniformly over momentum angle and noncollinear input pairs in a
   named neighborhood of zero;
2. provide a refinement map and norm with a quantitative convergence rate;
3. project the completed response onto the retained two-TT observables,
   conserved Record decoder, and physical state quotient; and
4. prove compatible nonlinear Lorentzian constraint propagation on
   increasing regions.

Observable decoupling remains unproved. The next highest-value calculation is
the two-TT/Record quotient unless a local analytic coefficient calculation can
close angular uniformity without another period scan.

## Axiom Issue

No axiom is amended. Any attached emergent gravity law still needs to state
the nonlinear metric embedding, refinement map, norm, full source and mode
class, observable quotient, rate, and Lorentzian propagation theorem. An exact
microscopic alternative still needs a joint source-geometry Noether identity
or a different local action/update.

The current axioms select neither contract. The present calculation removes
two candidate loopholes; it does not supply adoption authority or establish
necessity or minimality of a new axiom.

## No-Go Discipline Packet

The only negative shipped here is bounded:

> Complete source and collinear unequal-harmonic control on one skew ray does
> not establish angular-uniform refinement or physical observable closure.

### N1 -- Alternative Route Enumeration

| route | mechanism | disposition |
|---|---|---|
| local analytic angular theorem | build the continuous-momentum local force tensor and bound its Taylor remainder on the direction sphere | open and ranked |
| noncollinear multimode test | evaluate `k_1+k_2` with unequal directions using a local stencil | open |
| two-TT/Record observable quotient | prove the soft/nonmetric response has a vanishing physical readout with rate | open and required |
| nonlinear Lorentzian refinement | bind the quotient to the finite-depth causal update and prove constraint propagation | open and required |
| dynamical-source exact identity | include source equations and transformed currents at the same order | open exact fallback |
| improved/perfect or Pachner/tent law | replace the fixed action if the emergent route fails | open exact fallback |
| connection carrier | realize an exact local-frame Ward law on the retained Record carrier | open fallback |

No open route is relabeled closed.

### N2 -- Wall-Independence Audit

Source-polarization completeness, equal-versus-unequal mode mixing, angular
uniformity, observable decoupling, refinement convergence, and nonlinear
Lorentzian propagation are separate walls. This block closes the first two on
one ray and leaves the latter four open.

### N3 -- Hidden-Wall Scan

The inputs are weak jets at harmonics `k` and `2k` on one collinear ray. Three
finite periods are retained. Noncollinear momenta, incommensurate modes,
uniform angular bounds, nonlinear solved multimode branches, boundaries,
full `Z^3`, physical norms, Record readout, and law selection are not
executed.

### N4 -- Residual Matching

The source bases are constructed from the conservation equation before the
nonlinear force is evaluated. Their response-normalizing transform, physical
source singular values, and condition number are all reported. The metric
completion is fixed by the exact square-root map. No coefficient is fit per
source or per mode. The Ward-null reaction and half-amplitude control
independently separate coordinate completion from numerical cancellation.

### N5 -- Resolution And Rhetoric Audit

- `per_element`: all fifteen edge classes enter every force and reaction;
- `per_site`: all fifty hinges and 240 simplex-hinge incidences enter each
  cyclic phase site;
- `per_mode`: `k`, `2k`, equal-output `2k`, and cross-output `3k` are kept
  separate;
- `per_block`: both six-source bases, all 21 symmetric pairs, all 36 cross
  pairs, three tail periods, amplitude control, and Ward-null reactions are
  executed; and
- `lattice_wide`: explicitly not executed.

No one-ray tensor is called a uniform continuum, observable, Lorentzian, or
TOE theorem.

### N6 -- Partial-Closure Paths

The complete source tensor remains useful if angular control later fails: it
localizes the failure to direction or noncollinear composition rather than
source polarization. Observable decoupling can be tested independently. A
counterexample in either remaining seam would retire the emergent route and
promote the exact-action alternatives without erasing this bounded result.

### N7 -- Steelman

The strongest objection is that collinear harmonics share a phase quotient
and may miss noncollinear resonances or angular zeros. The calculation does
not answer that objection. A second objection is that a cubic Ward tensor may
still contaminate the physical TT/Record state after inversion. That also
survives and is now the highest closure risk.

The opposing steelman is that locality, the exact nonlinear metric chart,
and complete transverse-source control make the observed orders structural,
not accidental. The 57-component bilinear execution materially strengthens
that case, but only an angular/local coefficient bound and observable theorem
can convert it into refinement closure.

### N8 -- Cross-Cycle Echo

Block 58 corrected a nonmetric affine surrogate. Block 59 corrected harmonic
aliasing. Block 60 corrected directional overreach. Block 61 corrected the
linear edge chart. This block corrects selected-source and equal-input scope.
The recurring discipline is to expose every carrier, polarization, and mode
class before interpreting a soft residual as physical closure.

**N1--N8 status: `PASS`** for the full one-ray source tensors, unequal-harmonic
control, and stated refinement boundary. A uniform Regge success/no-go,
observable theorem, axiom necessity, or TOE closure claim would fail this gate
and is not shipped.

## Reproduction

From repository root:

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
python3 scripts/admissibility_regge_full_conserved_source_multimode_metric_completion_ward_boundary_2026_08_12.py
```

Expected final line:

```text
TOTAL: PASS=7 FAIL=0
```

The runner supports `TOE_MUTATION=batch_gradient`,
`TOE_MUTATION=source_basis`, `TOE_MUTATION=equal_tensor`,
`TOE_MUTATION=multimode_tensor`, `TOE_MUTATION=amplitude_control`, and
`TOE_MUTATION=note_boundary`; each mutation must fail its named gate.

## Conclusion

The metric-completed cubic Ward order survives the complete six-dimensional
transverse source class and all 36 unequal-harmonic bilinear pairs on the
tested skew ray. This is the first full source-and-mode tensor result in the
current nonlinear gravity route.

The next work must be a local angular/noncollinear coefficient theorem or the
physical two-TT/Record observable quotient. No additional period, selected
source, coupling, coefficient, or precision scan qualifies.

No TOE percentage moves.
