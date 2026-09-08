---
claim_id: admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_bounded_theorem_note_2026-08-11
claim_type: bounded_theorem
claim_scope: "For the supplied flat four-dimensional Kuhn/Coxeter Regge edge action S_alpha=sum_h A_h(epsilon_h+alpha epsilon_h^2) at alpha=1/1024, a coefficient-two static tick-edge row is a positive unit h_tt source and exactly annihilates all four vertex-displacement Ward columns. After fixing only the homogeneous metric mode, complete fifteen-edge pseudoinversion on every nonzero static momentum of the L=33,49,65,81,97 odd spatial tori gives 9 negative, 2 positive, and 4 Ward-zero eigenvalues; removes the fifth nonmetric flat zero; closes 1,872,320 solves; retains a normalized nonzero quotient gap above 0.058; and reconstructs a real mean-zero field whose offset-free radius-eight coefficient converges monotonically to the residue-derived 1/(2 pi), reaching relative error below 4.3e-4 at L=97. The finite-volume source is one localized positive unit source plus a disclosed uniform fixed-average compensation of density L^-3. A full-rank ten-metric congruence has a false Brillouin-edge near-pole at L=65 that is absent from the complete edge operator. This is a bounded finite-sequence linear Ward/Green result, not a selected action, an all-L or full-Z3 theorem, a semibounded Euclidean phase, a Lorentzian causal update, a nonlinear gravity theory, or an axiom amendment."
upstream_dependencies:
  - minimal_axioms
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
  - admissibility_centered_tick_edge_defect_improvement_exact_static_regge_source_boundary_bounded_theorem_note_2026-08-10
  - admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_bounded_theorem_note_2026-08-10
  - admissibility_flat_regge_curvature_squared_branch_lift_boundary_bounded_theorem_note_2026-08-10
  - admissibility_periodic_flat_ec_connection_negative_mode_axiom_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py
---

# Fixed-Average Positive Tick Source: Repaired Regge Ward Identity And Increasing-Torus Green Boundary

**Date:** 2026-08-11

**Type:** bounded theorem

**Role:** test whether an already supplied action-native Regge repair can join an exact displacement Ward identity, a positive local static source, and an increasing-region inverse-square-law response before investing in a Lorentzian constraint construction.

**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:** [admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py](../scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py)

## Result Up Front

One important part of the gravity route works on its declared linear finite scope. The supplied flat Kuhn/Coxeter Regge action with the action-native curvature-square repair is

~~~text
S_alpha = sum_h A_h [epsilon_h + alpha epsilon_h^2],
alpha   = 1/1024.                                             (1)
~~~

It supports a positive static unit h_tt source, an exact lattice displacement Ward identity, and a controlled increasing-torus Green response when the **complete fifteen-edge equations** are solved.

Let t=(0,0,0,1) denote the unit tick edge. Since the edge-length variation induced by a diagonal metric perturbation is

~~~text
delta ell_t = (1/2) h_tt,                                    (2)
~~~

the coefficient-two edge row

~~~text
s = 2 e_t                                                     (3)
~~~

is one positive unit h_tt source. For every static momentum k=(k_1,k_2,k_3,0), the tick component of each vertex-displacement gauge column is proportional to exp(i k_t)-1=0. Therefore

~~~text
s Gamma(k) = 0                                                (4)
~~~

exactly, without projecting or balancing the local source against another localized source.

On odd spatial tori with

~~~text
L in {33,49,65,81,97},                                       (5)
~~~

only the homogeneous metric mode is fixed. Equivalently, the periodic source is one localized positive unit source plus a uniform compensation of density L^-3. This compensation is the fixed-average convention, not a localized negative matter source, and its density falls to

~~~text
1/97^3 = 1.0956826815e-6.                                    (6)
~~~

For all 1,872,320 nonzero static momenta in (5), the complete repaired edge symbol has inertia

~~~text
(negative, positive, zero) = (9,2,4),                        (7)
~~~

where the four zeros are precisely the vertex-displacement Ward directions. The fifth nonmetric zero of bare flat Regge is absent. The nonzero quotient gap divided by

~~~text
khat^2 = 4 sum_i sin^2(k_i/2)                                (8)
~~~

stays above 0.058 on every declared grid. The complete pseudoinverse solve

~~~text
delta ell(k) = -Q_alpha(k)^+ s^dagger,
h_tt(k)      = 2 delta ell_t(k)                              (9)
~~~

closes with maximum residual below 9e-12.

The long-wave response is not fitted. Direct evaluation along an axial momentum gives

~~~text
lim_(q->0) q^2 h_tt(q,0,0,0) = 2,                           (10)
~~~

which fixes the three-dimensional Green coefficient to

~~~text
C_* = 1/(2 pi) = 0.159154943091895... .                     (11)
~~~

For the reconstructed mean-zero field H_L, the additive periodic offset is removed by the radius-eight difference

~~~text
C_L(8) = 16 [H_L(8 e_1)-H_L(16 e_1)].                       (12)
~~~

The five values increase monotonically toward (11), while their absolute errors decrease monotonically:

| L | nonzero modes | C_L(8) | relative error from C_* |
|---:|---:|---:|---:|
| 33 | 35,936 | 0.117852344 | 0.2595 |
| 49 | 117,648 | 0.149781612 | 0.0589 |
| 65 | 274,624 | 0.156112318 | 0.0191 |
| 81 | 531,440 | 0.158199084 | 0.00600 |
| 97 | 912,672 | 0.159087619 | 0.000423 |

This closes a real discriminator: Ward compatibility and an increasing-region positive-source Newtonian sector do not fail merely because the fifth bare Regge lattice branch exists. The supplied curvature-square term removes that branch while leaving the infrared residue intact.

It also exposes the next wall. Equation (7) remains indefinite after quotient by the four gauge directions. This is **not a semibounded Euclidean** phase theorem. No overall sign converts nine negative and two positive physical directions into a semibounded quadratic form. A Euclidean Gibbs interpretation of this unreduced edge Hessian is therefore not supplied.

That boundary is **not a gravity no-go**. Lorentzian lapse/shift constraints, a canonical or transfer-law reduction to two transverse-traceless modes, a conformal contour, a stable nonflat phase, or a different selected Record law can evade the unreduced Euclidean-signature obstruction. These are live routes, not rhetorical caveats.

No canonical axiom is edited, and no locked TOE percentage moves in this block. The result instead changes the priority stack: the highest-leverage next test is a Record-native Lorentzian/constraint update that preserves (4), (10), and the increasing-region source response while leaving exactly two positive-energy physical tensor modes.

## Inputs And Non-Imports

| input | used | not imported |
|---|---|---|
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | the Z^3 carrier, translations, proper-cubic covariance, fixed local Admissibility law, and permanent Records | Regge geometry, action (1), a source/action dictionary, physical law selection, dynamics, Lorentzian signature, or gravity |
| [retained Regge second variation](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md) | the actual fifteen edge classes, hinge incidences, Bloch symbol, metric map, and vertex-displacement columns | a selected microscopic law, nonlinear phase, or causal update |
| [static source boundary](ADMISSIBILITY_CENTERED_TICK_EDGE_DEFECT_IMPROVEMENT_EXACT_STATIC_REGGE_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | the exact tick-edge/h_tt normalization and periodic-zero-mode boundary | permission to call a signed pair a positive isolated source |
| [closed-history source note](ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | the distinction between a Ward-neutral signed pair and a positive source | a positive-matter interpretation for the negative member of that pair |
| [curvature-square branch lift](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | the action-native epsilon-squared correction, alpha=1/1024, and lifting of the fifth branch | coefficient selection, all-zone proof, nonlinear stability, or Lorentzian positivity |
| [flat EC connection boundary](ADMISSIBILITY_PERIODIC_FLAT_EC_CONNECTION_NEGATIVE_MODE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md) | the fact that the unchanged Record/EC flat saddle has a physical negative connection mode | a no-go for relational repairs, Regge laws, nonflat phases, or Lorentzian laws |

All of (1), the source dictionary (2)-(3), the fixed-average convention, and the pseudoinverse prescription are downstream supplied assumptions. They are not promoted to axioms by this calculation.

## Complete Edge Symbol And Exact Ward Identity

Let Q_R(k) be the retained Regge edge Hessian and let d_h(k) be the linearized deficit row of hinge class h. Flat deficits vanish, so the quadratic symbol of (1) is exactly

~~~text
Q_alpha(k) = Q_R(k)
             + 2 alpha sum_h A_h d_h(k)^dagger d_h(k).       (13)
~~~

The correction is positive semidefinite as a matrix addition and exactly annihilates metric tangents at k=0. It is not an ad hoc rank-one source projector. The primary runner independently reconstructs the real-space kernel and checks it against the retained Bloch symbol at three momenta to below 8e-13.

For an edge vector v, the vertex-displacement column in direction mu is

~~~text
Gamma_(v,mu)(k)
  = [exp(i k dot v)-1] v_mu/|v|.                             (14)
~~~

Both the Regge term and the deficit-square term obey

~~~text
Q_alpha(k) Gamma(k) = 0.                                     (15)
~~~

on the flat background. At static k_t=0, equations (3) and (14) give (4). Thus the source is in the range of the Hermitian quotient operator whenever no additional physical zero is present. The finite inventory confirms exactly four zeros at every tested nonzero static momentum.

The tick edge itself is also static-gauge invariant:

~~~text
delta_Gamma ell_t = [exp(i k_t)-1] xi_t = 0.                 (16)
~~~

Consequently the reported h_tt=2 delta ell_t response is not a gauge-dependent coordinate chosen after the solve.

## Fixed-Average Positive Source Boundary

A periodic Poisson-type operator cannot invert a source with nonzero homogeneous component. This calculation removes only that zero mode. In real space the Fourier convention is equivalent to

~~~text
rho_L(x) = delta_(x,0) - 1/L^3.                              (17)
~~~

The first term is the localized positive unit source. The second is a uniform fixed-average compensator. It does not introduce a second localized negative body or claim that a finite periodic universe contains net positive charge. For every fixed bounded observation region away from the origin, the local magnitude of the second term goes to zero along (5).

This is a bounded increasing-region construction, not a theorem that (17) converges in every distributional topology, not an open or Dirichlet boundary solution, and not a full-Z3 inverse construction. Those boundary routes remain open.

## Exhaustive Declared-Grid Inventory

The runner enumerates every nonzero spatial momentum on each grid in (5), sets k_t=0, builds the full 15-by-15 Hermitian symbol (13), and performs a complete eigensolve before any response is extracted.

| property | declared result |
|---|---:|
| total nonzero modes | 1,872,320 |
| distinct inertia on every grid | (9,2,4) |
| maximum Ward residual | below 1.5e-13 |
| maximum source-Ward residual | below 1e-15 |
| maximum solve residual | below 9e-12 |
| minimum gap/khat^2 | above 0.058 |
| maximum reconstructed imaginary part | below 5e-17 |
| maximum reconstructed mean | below 4e-19 |

The maximum response on each grid occurs at one of the six lowest nonzero axial momenta, as expected for a single 1/khat^2 infrared pole. The quotient-gap test is finite-grid evidence only; it does not prove a continuous-zone or all-L lower bound.

## Residue-Forced Green Coefficient

The runner evaluates the complete edge response at q=0.1, 0.05, and 0.025 along a spatial axis. The errors in q^2 h_tt(q) relative to 2 decrease strictly as q is halved, and the final error is below 2e-4. Equation (10) therefore supplies the target used in (11); no numerical fit to the five finite-volume field values selects their amplitude.

The difference observable (12) is chosen because an additive constant drops out and, for H(r)=C/r,

~~~text
2r [H(r)-H(2r)] = C.                                        (18)
~~~

Radius eight is fixed before comparing the five grids. The result establishes convergence on this declared sequence and observable. It does not claim a uniform radial window, a fitted Newton constant, an observed physical mass, or an error theorem beyond the five resolved volumes.

## Metric-Only Congruence Produces A False Pole

An important control prevents an attractive but incorrect stronger claim. Let M(k) be the full-rank 15-by-10 map from metric components to edge-length variations. Restricting the indefinite full symbol by congruence gives

~~~text
Q_metric(k) = M(k)^dagger Q_alpha(k) M(k).                  (19)
~~~

At the L=65 grid momentum

~~~text
k = (3.0932604589191808,
     2.5132741228718345,
     2.6099385122130587,
     0),                                                     (20)
~~~

the metric map has least singular value above 0.09, yet (19) has a physical nonzero eigenvalue of magnitude below 7e-5 and a tick response above 4000. At precisely the same momentum, the complete edge quotient has smallest nonzero absolute eigenvalue above 0.68, tick response below 0.19, and solve residual below 1e-12.

There is no full-edge pole. The ten-metric image is not an invariant subspace of the indefinite edge operator; discarding its mixing with the five nonmetric directions creates a stationary direction of the congruence. This is the same class of warning raised by earlier normal-subspace controls: full-rank restriction is not enough to preserve the spectrum of an indefinite coupled operator.

For this reason, neither the apparent metric-only pole nor its large response is used in the Green conclusion. All positive results above come from the complete fifteen-edge solve.

## Euclidean Semiboundedness And The Lorentzian Priority

The curvature-square correction removes the unwanted fifth zero, but the complete gauge quotient still has nine negative and two positive eigenvalues at every declared static nonzero momentum. Multiplying the action by -1 only swaps those counts. Therefore the supplied unreduced Euclidean edge quadratic form is indefinite rather than semibounded.

This prevents the present result from being promoted to a normalizable Euclidean Gaussian geometry phase. It does not prevent a Lorentzian theory from treating lapse-like and shift-like components as constraints rather than propagating positive-norm variables. The decisive next calculation is:

1. specify an extensional Record-native causal or transfer update;
2. derive its discrete lapse/shift constraint rows and propagation identity;
3. quotient gauge and solve constraints without a metric-only truncation;
4. show that exactly two transverse-traceless modes remain;
5. establish positive physical energy or reflection-positive transfer data;
6. verify that the static constrained response retains (4), (10), and (12).

A failure there would be much more informative than another Euclidean restricted-subspace scan because it would localize whether the missing object is a viable law or a missing law-selection/dynamics premise.

## Axiom And TOE Consequence

The minimal axioms explicitly state that Admissibility is not a dynamics axiom. They do not select an action, source dictionary, Lorentzian signature, time update, or physical geometry law. Nothing in this note derives (1) from the fixed Admissibility distribution, and nothing identifies a permanent Record history whose extensional effect is necessarily (3).

Accordingly, no canonical axiom is edited. A downstream sufficient interface suggested by the present boundary would require a selected geometry/Record law to provide all of:

~~~text
exact displacement Ward covariance,
a causal constraint update with two physical tensor polarizations,
a stable increasing-region positive-source Green sector,
and an extensional Record-to-source/action identification.              (21)
~~~

Clause (21) is not proved necessary, minimal, or adopted. If repeated constructive routes cannot derive such a law from the existing axioms, the candidate axiom issue is not another fitted coefficient. It is the absence of an extensional physical dynamics/law selection principle connecting Records to geometry, sources, and causal update.

The locked TOE map remains unchanged because this is retained-grade candidate evidence pending independent audit and because the Lorentzian/nonlinear law is still absent. Strategically, however, the gravity lane is more sharply localized: the linear Ward/source/Green seam is constructive, while unreduced Euclidean semiboundedness and causal law selection are the active walls.

## Fresh No-Go Discipline Packet

This packet governs only the bounded negative statement that the supplied unreduced Euclidean repaired flat edge Hessian does not itself furnish a semibounded phase. It does not ship a broad gravity no-go.

### N1 — Alternative-Route Enumeration

| route | status in this block | discriminating result |
|---|---|---|
| complete repaired flat Regge edge law | attempted constructively | exact Ward, fifth-branch lift, positive-source Green response; Euclidean quotient indefinite |
| ten-metric restriction | attempted as a control | false Brillouin-edge pole; rejected because the image is not invariant |
| bare flat Regge action | inherited exact boundary | retains the fifth nonmetric zero |
| unchanged flat Record/EC law | inherited Block-42 boundary | physical uniform connection negative mode |
| fixed-average periodic positive source | attempted constructively | succeeds on five increasing odd tori with uniform L^-3 compensation |
| localized Ward-neutral signed pair | inherited alternative | linear response exists, but one localized member has the wrong positive-matter premise |
| open or Dirichlet boundary | live | could remove the periodic compensation and strengthen the source interpretation |
| direct infinite-region/full-Z3 inverse | live | could replace the finite sequence with an analytic limit theorem |
| stable nonflat phase | live | may change the signature and constraint structure |
| Lorentzian/canonical constraint reduction | live and highest priority | may reduce the indefinite unreduced operator to two positive-energy TT modes |
| conformal contour/reflection-positive transfer law | live | may supply a physical measure without Euclidean semiboundedness of all edge variables |
| alternate relational derivative Record law | live | could supply Ward covariance and stable physical selection directly |
| Record-to-action/source law selection | live | needed to derive rather than merely supply (1) and (3) |

The successful complete-edge route and the live Lorentzian route defeat any claim that the tested Euclidean sign boundary is a general gravity impossibility.

### N2 — Wall-Independence Audit

The named open walls are:

~~~text
W1 = physical law/action selection from Records,
W2 = Lorentzian constraint reduction or another physical positivity rule,
W3 = all-L, continuous-zone, and full-Z3 boundary control,
W4 = extensional physical source/history identification,
W5 = nonlinear phase existence and stability,
W6 = causal update and constraint propagation.              (22)
~~~

| pair | reason the walls are not silently identified |
|---|---|
| W1/W2 | selecting an action does not prove constrained physical energy; a positive constrained law need not be uniquely selected |
| W1/W3 | finite/infinite analytic control does not select the microscopic law, and selection does not prove a limit |
| W1/W4 | selecting a geometry law does not identify which Record histories are physical sources |
| W1/W5 | microscopic selection does not prove a nonlinear stable phase |
| W1/W6 | an action-selection rule need not specify causal update or constraint propagation |
| W2/W3 | physical-mode positivity is distinct from uniform-volume and continuous-zone estimates |
| W2/W4 | constraint reduction does not supply a Record/source dictionary |
| W2/W5 | linear reduced positivity does not prove nonlinear phase stability |
| W2/W6 | a positive reduced spectrum does not by itself prove causal constraint propagation |
| W3/W4 | an infinite-region inverse can exist without identifying a physical source |
| W3/W5 | a linear full-Z3 bound does not prove a nonlinear measure or phase |
| W3/W6 | boundary control does not construct an update law |
| W4/W5 | physical source identification does not prove nonlinear stability |
| W4/W6 | a source dictionary does not imply a causal evolution rule |
| W5/W6 | phase existence and causal constraint propagation require separate arguments |

No wall in (22) is counted as evidence for another.

### N3 — Hidden-Wall Scan

The result depends on the supplied action (1), the chosen rational alpha=1/1024, the flat background, static k_t=0, coefficient-two tick normalization, fixed homogeneous mode, five stated odd tori, complete Hermitian pseudoinversion, double-precision eigensolves, and the fixed radius-eight observable. It does not use observed gravitational data, fit a Newton constant, assume a physical mass scale, select a lattice spacing, or identify the tick with measured proper time.

The runner reads all retained parent notes and the premise registry. Its scope line discloses that all-L, continuous-zone, nonlinear, Lorentzian, physical-scale, and law-selection statements remain open.

### N4 — Residual Matching

The successful claim uses the complete fifteen-edge residual

~~~text
||Q_alpha delta ell + s^dagger||,                            (23)
~~~

not only projected metric equations. It also checks Q_alpha Gamma, s Gamma, inertia, quotient gap, field reality, and fixed mean. The metric-only near-pole is explicitly matched against (23) at the same momentum and rejected because the complete residual has a regular quotient response.

The increasing-region conclusion matches the residue-forced target through the offset-free real-space observable (12). It is not inferred from visual similarity of a profile or from a fitted power law.

### N5 — Five-Resolution Cache

| resolution | exhaustive content in the primary runner |
|---|---|
| per element | all fifteen Kuhn/Coxeter edge classes, the coefficient-two tick row, and the ten-component metric-control map |
| per site | one localized unit source and the explicitly disclosed uniform fixed-average compensation |
| per mode | every nonzero static momentum on L=33,49,65,81,97, plus three independent long-wave controls |
| per block | the complete repaired 15-by-15 edge symbol before any restriction, with a separate metric-congruence false-pole control |
| lattice wide | five full finite odd tori totaling 1,872,320 modes; no all-L, full-Z3, nonlinear, or Lorentzian theorem |

The generated runner cache repeats this certificate and ends in an explicit TOTAL: PASS=n FAIL=n line.

### N6 — Partial-Closure Paths

Several nonempty constructive paths remain even if unreduced Euclidean semiboundedness never holds:

1. retain the exact Ward/source/Green sector and perform a canonical constraint reduction;
2. prove an open-boundary or direct full-Z3 Green theorem for the same repaired edge law;
3. derive a Record history whose linearized source is (3);
4. search for a stable nonflat stationary phase while keeping complete edge/nonmetric mixing;
5. replace Euclidean Gibbs positivity by a reflection-positive causal transfer law;
6. use the result as an infrared acceptance test for any newly selected relational law.

The present block already closes a partial path: exact static Ward compatibility plus a positive local source and a converging finite-volume Green observable.

### N7 — Steelman

The strongest opposing case is that the nine-negative/two-positive count is expected for an unreduced Euclidean gravitational Hessian and is not the physical stability question. A Lorentzian canonical formulation can make lapse and shift into constraint multipliers, remove gauge and constrained directions, and leave exactly two transverse-traceless propagating modes with positive physical energy. If that construction also preserves the static Green residue, it completely defeats a broad no-go based on (7).

This steelman succeeds against the broad claim. Therefore the only negative claim retained here is the narrow one: the supplied **unreduced Euclidean** quadratic form is not itself a semibounded phase theorem. The Lorentzian construction is promoted to the top experimental seam.

### N8 — Cross-Cycle Echo

The conclusion is consistent with, but not substituted by, earlier cycles:

- the retained Regge derivation supplied exact vertex-displacement columns;
- the curvature-square cycle lifted the fifth flat branch but did not prove a semibounded phase;
- the signed-source cycle exposed the periodic zero-mode and positive-source distinction;
- earlier metric/normal restrictions warned that a chosen subspace can hide coupled nonmetric response;
- the flat EC cycle found a genuine physical connection negative mode in a different unchanged Record law.

This block adds new information rather than echoing those boundaries: it exhausts five much larger full static grids, reconstructs the real-space positive-source response, and demonstrates the metric-only false pole at the same momentum against the full edge operator.

**Status: PASS.** The bounded negative statement survives N1-N8; every broad gravity no-go is rejected, and the strongest live Lorentzian route is named as the next priority.

## Reproduction

Run from the repository root:

~~~bash
python3 scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py
~~~

Expected final line:

~~~text
TOTAL: PASS=13 FAIL=0
~~~

The runner is source-bound to this note, the minimal axioms, all five named parent notes, the premise registry, and the retained Regge/repair scripts. It prints the five inventory summaries, the N5 certificate, and an explicit scope boundary.

## Conclusion

The highest-value gravity discriminator did not end in a generic failure. With the action-native curvature-square repair, the complete flat Regge edge law has exact static Ward compatibility, no fifth nonmetric zero, and a positive-source Green response approaching the analytically fixed 1/(2 pi) coefficient on five increasing tori. A metric-only truncation would have reported a spurious large pole; complete edge/nonmetric mixing removes it.

The remaining immediate obstacle is sharper: the unreduced Euclidean quotient is indefinite and the existing axioms do not select a Lorentzian causal law or a Record-to-source/action map. The next TOE campaign should therefore attack constrained Lorentzian propagation and law selection, not accumulate more finite-grid evidence for the already resolved linear static seam.
