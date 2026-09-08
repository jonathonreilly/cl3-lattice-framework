# Source-bound ice-physics target and bounded discriminant

## Recommendation

Prioritize a calibrated transverse spectral-measure calculation in the declared zero-flux mobile component, with pole weight and contamination bounds, before another UK fit or larger forward population. This addresses a named unresolved inference: a stable fitted decay need not be a photon pole with controlled weight. It does not derive the supplied spin Hamiltonian from Admissibility. No finite collection of volumes alone proves a 3D Coulomb phase.

Authority: current campaign main2b42ebe4b6b4ee76b0fa1b8e668ad7775e946307. Live PR7966 remains OPEN at369f785003f19c1ec5e8c4a6f1155c2827a7986b (live metadata saved). Complete corrected main source note SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07 and SOURCE_RECEIPT_DIAGNOSTIC note read. Complete PR7966 recovery note read. Replay measurement/run/summary code through line365 read; subsequent replay driver not fully reviewed. Transverse producer's propagation, coefficients, measurement, exact-small and effective-gap functions read; its large production driver was only partly displayed. Join searched/partly read, not full review. Stiffness helper fetched but not reviewed. Thus this is target selection, not producer certification or closure of its transitive imports.

## Fixed physical and estimator domain

Three spin-half occupation links per cubic vertex, three-of-six constraint; E_i(r)=(-1)^sum(r)(n_i(r)-1/2); elementary alternating ring flips, H=V N_f-A with geometric move multiplicities and J1. Fix even periodic volumes and explicitly the component reached from n_i(r)=r_i mod2. A claim about the full zero-flux ground requires proving this component wins among all components, not only preserving flux. Main's topological-stiffness note already explains this selection issue and exhausts L2 components. No extra source mismatch discovery is claimed here.

The actual projector is G=I-H/M, M=3L³, not exp(-H). A sweep uses M steps. Its exact single-level decay conversion is (M-E0)(1-exp(slope/M)), which the producer implements. Keep it; replacing it by minus slope changes the Hamiltonian estimator.

For stationary right ground amplitude psi, let R=G/(1-E0/M), O the transverse diagonal observable, and l_F=R^(MF)1. The infinite-population finite-forward normalized functional is

C_F(tau) = [l_F* O* R^(M tau) O psi] / [l_F* |O|² psi].

Here * denotes conjugate transpose; in the real tested mode all objects are real. This follows by summing the weighted transition paths and suffix descendants; the right-population normalization cancels. F→infinity gives <Opsi,R^(M tau)Opsi>/||Opsi||². It does not remove finite-population bias, finite burn-in, nonlinear ratio bias or correlations between the four origins. RK l_F is constant, so its exact F-independence is an identity control, not a detuned convergence guarantee.

## Executed bounded test

PREREGISTRATION.md was written before probe.py execution. Imported ONLY current source's finite geometry/component construction; independently built dense H, full eigenbasis, transverse O and spectral/finite-forward functionals. No stochastic producer was imported or run. All fixed curves and residuals remain in RESULT.json. Direct one-sweep matrix propagation agrees with spectral construction; RK all-F identity passes. One BLAS thread, under one second measured,128.79MiB,180second/180MiB bound. Floating eigensystem arithmetic is not interval-certified.

On864 states/6912 directed moves:

- RK V1: lowest observable-supported gap1.16086551317, level weight .704202846395, spectral energy variance .64. Pure fits2–6/8–14 give1.16581386640/1.16086647561.
- V.95: supported gap1.22445432926, weight .713684802046, variance .651863377433. Pure fits give1.22881906482/1.22445492059.
- V.95 maximum absolute curve error over tau0..16 versus pure: F0=.000611697535,F1=.000103139843,F2=.000011095367,F6=1.48e-9,F12=2.31e-15,F20<7e-18.

The lower full-component gap1.03054009191 quoted by corrected main is distinct from the transverse-supported1.22445432926. This is compatible with source repair's warning that a sampled Ritz separation missed a lower sector; an observable sees only its spectral support. The present full spectral calculation identifies that distinction, not an inconsistency.

The decisive finite lesson is limited: the declared L2 transverse operator has substantial higher-level weight even when late-time gaps and forward suffixes look stable. This is not a counterexample to an infrared photon; L2 is not infrared. It provides an exact calibration target which is stricter and different from the old producer's through-tau4 absolute tolerance .06.

## Prospective next experiment, not launched

First calibrate an independent estimator against the entire above C_F curve and spectral moments, with matched F and stationary/burn-in conventions. Predeclare independent replicas, population doubling, burn-in doubling, both fit windows and raw unnormalized numerator/denominator; never average only normalized blocks without exposing that choice. Use <=180seconds small jobs initially. A failure must be classified as finite-F, finite-population, burn-in, normalization, or observable error before scaling.

Then measure a positive pure spectral measure rather than infer it from one logarithmic slope. For each fixed momentum/polarization, report C(t), zeroth weight, first two energy moments and bounds on spectral mass outside a predeclared low-energy interval, using polynomial/moment positivity or independently validated imaginary-time inversion bounds. Variance alone bounds concentration about the mean by Chebyshev; it does not prove an isolated eigenvalue or a thermodynamic pole. Finite forward curves need not have positive spectral coefficients, so positivity bounds require genuine pure-estimator control first. The current experiment retains any negative coefficients rather than silently applying pure-measure inequalities.

For a later volume experiment, freeze L and harmonic pairs that share physical lattice momentum (e.g. L,h versus2L,2h) alongside lowest-harmonic points. This tests volume contamination separately from q-dependence. Compare supported weight and spectral interval against the RK z2 control, candidate z1 detuned response, and a possible gapped interval; do not select the winner by flexible q4/q6 nuisance fits alone. A finite positive residue bound at sampled volumes remains finite evidence. A phase theorem needs uniform-in-volume control, component selection and a limit argument absent here.

Do not launch L4 full Hilbert enumeration:192 links makes exhaustive enumeration infeasible. The old L16/18 replay already cost20807seconds and failed a genealogy floor. An independent large-volume design needs measured small-job scaling and a resource ceiling before authorization by the coordinator; no plausible numeric budget for new production is asserted here.

## Alternatives and overlap

Winding energy differences would test electric stiffness and avoid magnetic-source identification, but the existing exact L2 component derivatives and finite detuning projector ladder already target them. The new obligation would be a certified full-sector minimum plus ground-energy difference error substantially smaller than O(1/L), uniformly controlled in detuning. A selected component or borrowed U_charge error cannot supply it. Repeating that calculation without a new error method has lower value.

Uniform magnetic curvature is now correctly defined on main, but a whole-flux endpoint is unitarily equivalent to zero. It cannot by itself identify a followed magnetic branch or establish UK. Repeating source calibration is not the proposed task.

A rigorous photon lower/upper dispersion bound on this interacting finite-spin model would be stronger, but no source-grounded uniform estimate is currently available in the inspected material. The feasible immediate target retires part of estimator-to-pole inference, not the native action/observable supplier or full thermodynamic phase obligation.
