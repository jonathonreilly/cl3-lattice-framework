---
claim_id: admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "For the repository's actual four-dimensional Kuhn/Coxeter Regge-plus-deficit-square action at alpha=1/1024, odd transversely homogeneous periods L=3,5,7,9,11 retain all 15L edge variables, fix only the ten average metric moduli, and split the remaining directions exactly into 11L-6 nongauge and 4L-4 real displacement coordinates. For both the static Euclidean density source and the conditionally Lorentzian null Record source, the full nonlinear nongauge equations have positive-length metric-dominated solutions at fixed fundamental metric amplitude 1e-4. The period-three Ward obstruction is the aliased quadratic harmonic 2k=-k; for every larger executed period the residual is concentrated at the distinct 2k harmonic. Its norm divided by metric amplitude squared decreases from 3.033635 to 0.066601 for the static source and from 1.043652 to 0.075184 for the null source. An independent weak-amplitude evaluation on L=19,25,33,49 fits k exponents 2.9786 and 2.9743, with tail ratios W/(eta^2 k^3) reaching 0.3733 and 0.4388. Fourfold amplitude controls preserve those normalized coefficients. An independent Schur companion finds enlarged full-harmonic gauge blocks mixed-sign and finite-spacing lifted, while their maximum absolute eigenvalue divided by eta falls from 0.176688 to 0.140878 and from 0.139431 to 0.105053 between L=3 and L=5. This is controlled increasing-period evidence that the fixed action's nonlinear Ward and pseudo-constraint defects soften in the infrared, not an all-L theorem, exact continuum constraint theorem, observable-decoupling theorem, full-Z3 construction, selected source/action law, nonlinear Lorentzian stability theorem, axiom amendment, audit verdict, or TOE percentage movement."
upstream_dependencies:
  - minimal_axioms
  - admissibility_nonuniform_conserved_source_regge_second_order_ward_pseudoconstraint_gate_bounded_theorem_note_2026-08-12
  - admissibility_flat_regge_curvature_squared_branch_lift_boundary_bounded_theorem_note_2026-08-10
  - admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py
companion_runner: scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_schur_companion_2026_08_12.py
---

# Nonuniform Conserved-Source Regge Increasing-Period Pseudo-Constraint Scaling

**Date:** 2026-08-12

**Type:** `bounded_theorem`

**Role:** decide whether Block 58 found a persistent nonlinear gravity wall or
a finite-spacing pseudo-constraint that becomes irrelevant in the infrared,
and change campaign priority only on the basis of the resulting order law.

**Audit-status authority:** independent audit lane only. This source authors
no audit verdict and predicts none.

**Primary runner:**
[admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py](../scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py)

**Independent Schur companion:**
[admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_schur_companion_2026_08_12.py](../scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_schur_companion_2026_08_12.py)

**Repository dependencies:** the current
[minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md), the
[Block-58 genuine nonuniform source test](ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md), the
[flat curvature-square repair](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md), and the
[two-TT causal split-step update](ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md).

## Result Up Front

Block 58 remains correct about microscopic exactness: on its period-three
source branches, the fixed Regge-plus-deficit-square action has a nonzero
quadratic Ward force and eight lifted displacement directions. That rejects
the action with an external source as an exact finite-spacing first-class
law.

It did not answer the more important alternative question: does the defect
remain at the same physical order under refinement, or is it a soft lattice
artifact? Period three is especially dangerous because the quadratic
harmonic aliases:

```text
k=2 pi/3,
2k=4 pi/3=-2 pi/3=-k  (mod 2 pi).                    (1)
```

Thus the Block-58 residual could not be separated from its source harmonic.
This block removes that alias and retains every generated harmonic.

For odd period `L`, all `15L` edge lengths are retained. Only the ten average
metric moduli are fixed. The remaining real directions split exactly as

```text
nongauge:    5+22(L-1)/2 = 11L-6,
displacement: 8(L-1)/2   = 4L-4,
total:       (11L-6)+(4L-4)+10 = 15L.                (2)
```

The first source harmonic is `k=2 pi/L`. For each source and period, its
coupling is chosen only to hold the norm of the fundamental metric response
at

```text
eta=10^-4.                                             (3)
```

Every other nongauge harmonic is solved, not suppressed. Every displacement
harmonic is retained for the Ward and Schur tests.

The full nonlinear results are:

| source | `L` | `k` | `||Ward||/eta^2` | dominant Ward harmonic | nonmetric / metric |
|---|---:|---:|---:|---:|---:|
| static density | 3 | 2.094395 | 3.033635 | 1, because `2k=-k` | 0.357295 |
| static density | 5 | 1.256637 | 0.811713 | 2 | 0.161968 |
| static density | 7 | 0.897598 | 0.267442 | 2 | 0.087163 |
| static density | 9 | 0.698132 | 0.121836 | 2 | 0.053827 |
| static density | 11 | 0.571199 | 0.066601 | 2 | 0.036400 |
| Record/null | 3 | 2.094395 | 1.043652 | 1, because `2k=-k` | 0.093337 |
| Record/null | 5 | 1.256637 | 0.560584 | 2 | 0.032605 |
| Record/null | 7 | 0.897598 | 0.255345 | 2 | 0.016729 |
| Record/null | 9 | 0.698132 | 0.131314 | 2 | 0.010166 |
| Record/null | 11 | 0.571199 | 0.075184 | 2 | 0.006825 |

At every `L>3`, the `2k` Ward component is more than one hundred times every
other executed harmonic. The solved nonlinear Ward norm agrees within two
percent with an independently evaluated symmetric quadratic jet on the flat
first-order response. Changing `eta` from `5e-5` to `2e-4` leaves the
normalized coefficient unchanged within two percent. The effect is therefore
quadratic in field amplitude on the resolved surface, not a Newton tolerance
or one-amplitude artifact.

The weak-amplitude tail can be evaluated without assembling the full torus
Hessian because the first-order response is one Bloch mode. On
`L=19,25,33,49`, a log fit gives

| source | fitted power in `k` | fitted coefficient | maximum relative fit residual | `W/(eta^2 k^3)` at `L=49` |
|---|---:|---:|---:|---:|
| static density | 2.978573 | 0.357816 | 0.00199 | 0.373308 |
| Record/null | 2.974311 | 0.417185 | 0.00291 | 0.438785 |

The honest bounded statement is therefore

```text
||Ward_(2k)|| = eta^2 O(k^3)                         (4)
```

on the executed increasing-period family. The desired sourced graviton
equation begins at `O(eta k^2)`. At fixed small amplitude, (4) is suppressed
by one additional momentum power relative to that equation. This is evidence
for an infrared-irrelevant pseudo-constraint, not proof of an exact continuum
Noether identity.

The independent Schur companion tests the stronger relaxed-gauge Hessian.
Retaining all nonzero harmonics gives mixed-sign Schur blocks:

| source | `L` | dimension | inertia | `max |lambda_Schur| / eta` |
|---|---:|---:|---:|---:|
| static density | 3 | 8 | 5-/3+ | 0.176688 |
| static density | 5 | 16 | 10-/6+ | 0.140878 |
| Record/null | 3 | 8 | 5-/3+ | 0.139431 |
| Record/null | 5 | 16 | 10-/6+ | 0.105053 |

The constraints are still lifted at every executed finite spacing. Their
largest normalized lift decreases as the infrared is approached. No physical
ghost interpretation is made from a Euclidean Schur inertia.

## What Changed Scientifically

This is not merely another finite-size table. It changes the candidate
diagnosis and the campaign's optimal route.

Before this block, the only executed genuine curved branch was the resonant
`L=3` carrier. The leading alternatives were to endogenize the source and
cancel the finite-spacing defect exactly, or abandon fixed Regge for a
perfect/Pachner law.

After this block, there are two distinct gravity targets:

1. **Microscopic exact gravity.** If every finite lattice must carry exact
   first-class constraints, fixed Regge still fails and a dynamical source,
   improved/perfect action, or Pachner/tent formulation remains necessary.
2. **Emergent infrared gravity.** If the physical claim is a continuum
   Einstein regime, the measured defect is at a higher derivative order than
   the target equation. The next high-value task is an analytic `k^3` bound,
   Schur/observable decoupling theorem, and compatibility with the Record
   source and two-TT causal update. Exact cancellation at the cutoff is then
   optional rather than automatically prior.

The second route is now ranked first because it uses the observed order
separation directly and can save an unnecessary perfect-action construction.
More period scans are stopped; the next work must prove the order law or break
it on a genuinely different momentum/source family.

## Construction And Normalization

Let `B_L` contain the five homogeneous nonmetric directions and the real and
imaginary parts of the eleven-dimensional gauge complement at every positive
Fourier representative. Let `Gamma_L` contain the real and imaginary parts
of all four vertex-displacement columns at those modes. Equation (2) and the
ten average metric columns give a complete rank-`15L` basis.

For either source `J`, the solved equations are

```text
B_L^T [grad S_Regge+R2(ell)-c J] = 0.                (5)
```

The source has zero average and annihilates the flat displacement columns.
The solve holds the average metric moduli and displacement coordinates fixed,
but no nonzero nongauge Fourier mode is fixed. Newton steps use the exact flat
Bloch Hessian as a preconditioner; the nonlinear action gradient rebuilds all
fifty hinge classes and all 240 simplex-hinge incidences per longitudinal
site. Projected residuals are below `2e-12`, all edge lengths exceed `0.9999`,
and both branches become progressively more metric-dominated.

The Ward field is evaluated mode by mode as

```text
W_m=Gamma(m)^dagger [grad S(ell)-cJ]_m.              (6)
```

The independent quadratic comparison uses the symmetric second response at
the flat first-order solution. It therefore does not reuse the nonlinear
branch residual.

For the Schur test, the complete raw length Hessian is rebuilt by complex-step
differentiation of the analytic action gradient, then transformed to
orthonormal bases for `B_L` and `Gamma_L` before the nongauge block is
eliminated. This avoids coordinate-normalization comparisons between periods.

## Exact Axiom And Law Consequence

No axiom is amended. The current axioms neither select the Regge action nor
say whether physical gravity must be exact at the cutoff or only in a
controlled infrared equivalence class.

The new axiom issue is narrower than “add covariance.” An exact attached law
object must choose one of these extensional acceptance contracts:

> **Exact microscopic contract.** The joint Record, source, constraint, and
> geometry action has an exact finite-region Noether identity and exact
> first-class constraint propagation on its declared carrier.

or

> **Controlled emergent contract.** The joint law supplies a directed
> refinement/coarse-graining family, identifies its physical observables and
> states, and proves uniform bounds under which every gauge-breaking Ward,
> pseudo-constraint, and source error vanishes relative to the retained
> `O(k^2)` Einstein operator while the causal Record update and physical
> amplitudes converge.

Adjectives such as “approximately covariant” or “continuum-like” do not meet
the second contract. It needs a norm, a refinement map, a source class, a
state/observable quotient, and a convergence rate. The present data supply a
candidate rate for one source family; they do not supply that contract.

## TOE Consequence And Priority Reset

| lane | actual advance | condition still required for percentage movement |
|---|---|---|
| gravity / source / resources | the first genuine curved-source obstruction is dealiased and shown to soften as `eta^2 k^3` on an increasing-period family; fixed Regge returns as a viable infrared candidate | analytic/all-period control, pseudo-constraint observable decoupling, selected joint source/action, and nonlinear Lorentzian regime |
| inertia / matter | the conserved Record/null source has improving metric purity and the same infrared Ward order | physical matter/source selection, general source class, dressed inertia, and stable state |
| causal time | the defect is now compared at the order relevant to the existing two-TT `k^2` update | bind the nonlinear corrections to one selected causal Record update |
| operational quantum / Records | the named null source remains a valid explicit Record carrier | physical source decoder and joint-law selection |
| Born probability / realized history | no direct closure | selected realized-history law and probabilities |

This is significant candidate and route progress. It does not yet retire the
controlled-infrared obligation, so **no TOE percentage moves**. The fixed map
remains `95/92/50`, `76/72/41`, `95/96/75`, `70/45/29`, and `84/63/34` in
the campaign's evidence/integration/closure notation.

The revised priority stack is:

1. derive a local analytic small-`k` expansion or uniform bound proving (4)
   and the normalized Schur softening, including a non-axial momentum control;
2. prove that the pseudo-constraint directions decouple from the retained
   two-TT observables and bind that quotient to the conserved Record source;
3. construct the selected nonlinear Lorentzian update and increasing-region
   state only after the infrared quotient survives;
4. return to exact dynamical-source cancellation or perfect/Pachner dynamics
   if the analytic/refinement test fails or microscopic exactness is adopted
   as a requirement.

## No-Go Discipline Gate

The only bounded negative retained is:

> The fixed action is not exactly first class on any executed nonzero-period
> sourced branch; its displacement Schur block is nonzero at finite spacing.

The positive result is increasing-period evidence for infrared suppression.
Neither statement is a universal gravity theorem.

### N1 -- Alternative Route Enumeration

| route | executed outcome | status |
|---|---|---|
| persistent finite-spacing obstruction | contradicted as the only interpretation: normalized Ward force falls by factors 45.5 and 13.9 through `L=11` | `ATTEMPTED`; persistent-order reading retired on this family |
| aliased quadratic harmonic | `L=3` has `2k=-k`; every `L>3` localizes the defect at distinct `2k` | `ATTEMPTED`; alias identified |
| controlled infrared fixed-Regge route | tail fits `k^(2.98)` with stable amplitude normalization | `ATTEMPTED`; strongest live route, theorem still open |
| exact dynamical Record/matter completion | may cancel the finite-spacing Ward term through a joint identity | live if microscopic exactness is required |
| improved/perfect action | may cancel lattice artifacts at every spacing | live, now conditional on the infrared route failing or exactness being selected |
| Pachner/tent dynamics | may replace fixed-carrier pseudo-constraints | live |
| alternate source or generic momentum | may change the measured exponent or activate other harmonics | live and required hostile control |
| observable quotient despite nonzero Schur block | can make the soft constraint sector physically irrelevant | live and required for emergent closure |

### N2 -- Wall-Independence Audit

Four independent walls remain:

- `W_rate`: promote the sampled `k^3` behavior to an analytic or uniform bound;
- `W_obs`: show that the soft constraint sector decouples from physical
  observables and state norms;
- `W_source`: select and generalize the Record/matter source law; and
- `W_time`: construct nonlinear Lorentzian causal evolution and a realized
  increasing-region history.

An order fit does not prove observable decoupling. A source decoder does not
prove a refinement bound. A Lorentzian update does not select the source or
physical state. These walls are not collapsed into one percentage.

### N3 -- Hidden-Wall Scan

The nonlinear carriers are odd one-dimensional periods embedded
transversely homogeneously in the four-dimensional complex. Average metric
moduli are fixed. The source has one axial Fourier momentum. The calculation
is Euclidean, `alpha=1/1024` is supplied, the metric amplitude is small, and
the source coupling changes with `L` to hold that response fixed. “Every
harmonic” means every harmonic on these reduced tori, not generic four-vector
momenta. “Increasing period” is not an infinite-volume theorem.

### N4 -- Residual Matching

The target is exactly Block 58's omitted displacement equation, now evaluated
after solving every nongauge harmonic. The `L=3` number reproduces the same
finite-spacing mechanism in a metric-amplitude normalization. The `L>3`
calculation separates its quadratic harmonic rather than replacing it with a
linear or projected proxy. Schur softening tests the Hessian consequence of
the same mechanism. Full `Z^3`, state, and Lorentzian residuals are carried
forward, not declared solved.

### N5 -- Resolution And Rhetoric Audit

- `per_element`: every `15L` edge variable participates;
- `per_site`: all fifty hinges and 240 simplex-hinge incidences participate at
  each longitudinal site;
- `per_mode`: all nonzero Fourier harmonics are represented on every
  nonlinear torus;
- `per_block`: both sources, five nonlinear periods, the long leading-jet
  tail, amplitude controls, and four Schur-companion blocks are checked; and
- `lattice_wide`: explicitly not executed beyond this increasing-period
  reduction.

The rhetoric says “evidence,” “fit,” “softening,” and “candidate,” never
“continuum GR proved” or “gravity closed.”

### N6 -- Partial-Closure And Primitive Scan

The flat action already has the correct Einstein/TT `O(k^2)` operator and
four exact displacement nulls. Block 53 supplies a local causal linear two-TT
update. Block 58 supplies the genuine conserved nonlinear source branch. This
block adds the missing order comparison. None selects the source, state,
nonlinear update, or refinement law. No approved primitive is enlarged and no
new primitive is smuggled in.

### N7 -- Steelman

The strongest objection is that exact finite-spacing gauge symmetry may be a
category error for an emergent-gravity lattice theory: irrelevant operators
are expected and only the continuum observable algebra must recover the
constraint. The data support that objection. It succeeds in changing route
priority, but not in closing gravity, because a finite axial fit does not prove
uniform convergence, state positivity, constraint propagation, or observable
decoupling.

The opposing steelman also survives: without exact microscopic constraints,
pseudo-modes may contaminate the physical state or nonlinear evolution even
when one Ward norm is `O(k^3)`. That is why the Schur/observable theorem is the
next gate.

### N8 -- Cross-Cycle Echo

Earlier gravity blocks repeatedly overread reduced or aliased carriers: the
five-normal affine continuation froze metric tangents, the inherited flat
quotient hid source connections, and finite momentum inventories missed
infrared chambers. Block 58 corrected the first error by using genuine metric
branches. This block corrects the second-order resolution error by separating
`k` from `2k` and holding physical response rather than source coupling fixed.
The lesson is to derive scaling order before replacing a carrier.

**N1--N8 status: `PASS`** for the finite-spacing nonexactness, harmonic
dealiasing, and executed increasing-period scaling claim. A universal
fixed-Regge success/no-go, all-period bound, continuum constraint theorem,
axiom necessity, or TOE closure claim would fail this gate and is not shipped.

## Reproduction

From repository root:

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
python3 scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_scaling_2026_08_12.py

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
python3 scripts/admissibility_nonuniform_conserved_source_regge_increasing_period_pseudoconstraint_schur_companion_2026_08_12.py
```

Expected final line:

```text
TOTAL: PASS=8 FAIL=0
TOTAL: PASS=4 FAIL=0
```

The primary runner supports `TOE_MUTATION=harmonic_alias`,
`TOE_MUTATION=infrared_power`, and `TOE_MUTATION=note_boundary`. The Schur
companion supports `TOE_MUTATION=schur_softening`. Each mutation must fail its
named gate.

## Conclusion

Block 58 found a real finite-spacing failure, but period-three aliasing made
it look more terminal than the resolved infrared sequence supports. On both
genuine conserved-source branches the nonlinear Ward defect moves to `2k`,
is quadratic in metric amplitude, and scales approximately as `k^3`, while
the enlarged pseudo-constraint Schur extrema also soften.

Fixed Regge is therefore back in contention as an **emergent infrared gravity
candidate**, though it remains rejected as an **exact microscopic first-class
law**. The next decisive work is an analytic/refinement and physical-observable
theorem, not more size scans and not an automatic action replacement.

No axiom is amended. No TOE percentage moves.
