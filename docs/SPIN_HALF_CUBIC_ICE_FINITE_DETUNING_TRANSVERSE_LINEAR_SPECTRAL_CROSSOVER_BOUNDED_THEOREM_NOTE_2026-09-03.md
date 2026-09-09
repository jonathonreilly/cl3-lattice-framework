# Finite transverse Green functions and historical fit diagnostics

**Date:** 2026-09-03; source correction 2026-09-09.

**Claim type:** bounded_theorem

**Runner:** [scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py](../scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py)

**Current diagnostic receipt:** [logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt](../logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt)

**Premise boundary:** [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md). The Hamiltonian, state/readout, Born weighting and imaginary-time sampling protocol used here are supplied model choices. They are not derived primitives or a physical Record formation law. Formal audit is deferred by the owner; this source applies no audit status.

## Conditional finite construction

The program supplies a finite occupation Hamiltonian H=V F-A, a positive Green matrix G=I-H/M on its declared component, and a staggered/link-centred transverse readout. Nonnegativity and a strictly dominant Perron eigenvalue are hypotheses of the projection interpretation; a component, observable and state are additional inputs. If H psi_j=E_j psi_j, then G has eigenvalues g_j=1-E_j/M. In a normalized ground-state correlation the finite spectral expansion weights (g_j/g_0)^n by squared observable matrix elements. It need not contain only one nonzero excited term.

For a single isolated contributing eigenvalue, with tau=n/M, the logarithmic slope a is M log(g_j/g_0), and the finite-step conversion is E_j-E_0=(M-E_0)(1-exp(a/M)). A multi-term finite-window fit is an effective diagnostic; imaginary projection time is not physical Record formation time. The current exact-component control retains C(0)=1 for the supplied normalization. A sampled decay is not a proof of the lowest global gap, an asymptotic photon pole, or a thermodynamic dispersion relation.

## Historical fits with corrected uncertainty

The archived 16/0 receipt contains fourteen gap estimates over its declared couplings and volumes. The current analysis retains every one. The RK-subtracted squared-gap fit and the unsubtracted pure-q or pure-q-squared fits use different response vectors and parameter counts. Their losses are printed as separate diagnostics; comparing those numbers does not select a physical model.

In a joint detuning regression the same RK gap at a given L appears in multiple observations. The delta-method covariance therefore contains the off-diagonal product of the two RK-reference derivatives times its variance. The current fit uses that full shared-reference covariance. The uncertainty remains a finite fitted-estimator approximation, not a calibration theorem.

The old .2598 magnetic comparison is a trial response. It is neither the relaxed response later sampled by the occupation-sign source nor a derived uniform physical K. No physical c-squared=UK follows from these fits. The actual control API now returns health records with its gap, allowing a caller to aggregate the later controls. The historical receipt does not contain that complete late-control health record. New long production, population/forward-length/volume limits and a physical clock/readout supplier remain held.

## Recovery and evidence status

The [complete original note](../.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md) and [complete original receipt](../.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt) are immutable dated history. All original program bodies, seeds, budgets, checks, tables and failures are retained in the same archive and authenticated by the [historical receipt index](../data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json). Earlier claims are not current authority. Current successful checks certify only the explicitly bounded diagnostics above. Historical production remains unvalidated under the corrected source; unavailable long-run evidence is held rather than restamped.
