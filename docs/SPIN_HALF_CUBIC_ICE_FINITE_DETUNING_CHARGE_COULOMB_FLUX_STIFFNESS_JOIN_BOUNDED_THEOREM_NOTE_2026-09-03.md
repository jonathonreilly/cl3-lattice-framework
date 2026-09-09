# Finite charge geometry and historical Coulomb-fit diagnostics

**Date:** 2026-09-03; source correction 2026-09-09.

**Claim type:** bounded_theorem

**Runner:** [scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py](../scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py)

**Current diagnostic receipt:** [logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt](../logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt)

**Premise boundary:** [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md). The Hamiltonian, state/readout, Born weighting and imaginary-time sampling protocol used here are supplied model choices. They are not derived primitives or a physical Record formation law. Formal audit is deferred by the owner; this source applies no audit status.

## Surviving finite statement

The supplied occupation model uses E_i(r)=epsilon(r)(n_i(r)-1/2), with epsilon(r)=(-1)^(r_x+r_y+r_z). Reversing the occupations on a directed path changes the discrete divergence only at its two endpoints. This follows by cancellation of the entering and leaving link contributions at each interior vertex; the endpoint contributions are opposite. The current runner constructs three declared paths and evaluates the actual divergence of their states.

A separate real-field quadratic model minimizes (U/2) sum E_l^2 at fixed divergence and harmonic flux. Fourier inversion of the nonzero periodic Laplacian gives the pair energy U[G(0)-G(d)]; the specified harmonic displacement contributes U|d|^2/(2L^3). This formula assumes U>0 and the allowed real-field space. It is a conditional model coordinate for a fit, not an exact ground-energy identity for the discrete spin-half Hamiltonian or every topological component. The runner retains permutation/inversion controls for its finite coordinate.

For a finite connected component with nonpositive off-diagonal H, a strictly positive lowest eigenvector gives the mixed-estimator identity sum_x (H psi)_x / sum_x psi_x = E_0. The current check reconstructs the declared 508-state charged component and checks this identity. Neither its size nor this identity proves that all charged configurations lie in that component or that its energy is the minimum over other components.

## Historical evidence and current limits

The preserved original receipt reports 15/0. At V=.95 and .90 it prints charge-fit U_charge=.160609 +/- .015345 and .301440 +/- .026769. The distinct flux values are .162638 and .321114, without corresponding flux standard errors. A charge-fit error must not be attached to a flux central value. The new diagnostic explicitly keeps those estimator/value pairs separate.

The original health aggregate preceded later off-axis/path/charge controls, so its green header does not certify those later runs. The current finite health reducer checks all records actually passed to it and rejects an added late violation, but this is not a reconstructed health record for the historical production. A new complete population run, global component comparison, estimator convergence and thermodynamic Coulomb limit remain held. The source does not derive physical electric stiffness from the approved axioms.

## Recovery and evidence status

The [complete original note](../.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md) and [complete original receipt](../.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt) are immutable dated history. All original program bodies, seeds, budgets, checks, tables and failures are retained in the same archive and authenticated by the [historical receipt index](../data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json). Earlier claims are not current authority. Current successful checks certify only the explicitly bounded diagnostics above. Historical production remains unvalidated under the corrected source; unavailable long-run evidence is held rather than restamped.
