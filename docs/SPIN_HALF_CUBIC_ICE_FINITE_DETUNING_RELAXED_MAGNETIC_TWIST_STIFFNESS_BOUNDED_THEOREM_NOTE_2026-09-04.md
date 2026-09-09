# Occupation-sign response, corrected sample bounds and historical magnetic data

**Date:** 2026-09-04; source correction 2026-09-09.

**Claim type:** bounded_theorem

**Runner:** [scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py](../scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py)

**Current diagnostic receipt:** [logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt](../logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt)

**Premise boundary:** [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md). The Hamiltonian, state/readout, Born weighting and imaginary-time sampling protocol used here are supplied model choices. They are not derived primitives or a physical Record formation law. Formal audit is deferred by the owner; this source applies no audit status.

## Source convention and finite algebra

The existing matrix family attaches a phase exp(i theta s_p) to a plaquette transition, where s_p is its occupation sign. For E_i(r)=epsilon(r)(n_i(r)-1/2), the same flip changes the electric field by -epsilon(r)s_p times the oriented plaquette boundary. Consequently a uniform Cartesian source has the additional epsilon(r) factor. Opposite root parities in the actual finite geometry distinguish these two sources. The occupation-sign family is retained under its actual definition; it is not renamed a uniform Maxwell stiffness.

The [current Cartesian-source note](SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md) gives the finite source distinction and the separate full-background-flux boundary. For a finite Hermitian analytic family with a simple eigenvalue, a local second derivative is well defined. An analytic continuation may evaluate that local response within its own spectral domain. Neither a local curvature nor its continuation proves a constrained flux-sector energy or a finite-flux endpoint formula. Those require an additional model and control of the branch/remainder.

## Corrected sample and covariance definitions

With b burn sweeps, n requested sample sweeps and M steps per sweep, samples are taken at (b+1)M,...,(b+n)M. The old bM endpoint produced n+1 writes when b>0. The current compiled core enforces a strictly post-burn boundary, a pre-write array bound and exact returned count. Tiny zero/positive-burn calls are current evidence; the old multi-volume population run is not silently repeated or certified by them.

For continued estimates K_i=-2(E_i-E_0)/(eta_i^2 L^3), their full covariance is 4[Cov(E_i,E_j)-Cov(E_i,E_0)-Cov(E_0,E_j)+Var(E_0)]/(eta_i^2 eta_j^2 L^6). The shared-zero helper explicitly assumes mutually independent continued-energy runs, each independent of the common zero-source run. Under that assumption its off-diagonal term is 4 Var(E_0)/(eta_i^2 eta_j^2 L^6), and the supplied diagonal errors already include their own zero-source contribution. The combination routine now requires the actual covariance and performs generalized least squares. A diagonal-error average cannot stand in for this matrix.

## Preserved data and held identification

The old 13/0 artifact prints occupation-sign responses .075561 and .076589 for the two detunings. Its reported response errors omitted the shared-zero covariance and the producer had the buffer defect. These are historical payloads, not validated current production or uniform K estimates. Multiplying .162638 by .075561 remains exact arithmetic on two printed numbers, with no available physical UK uncertainty. The .015345 charge-fit error belongs to U_charge=.160609, not U_flux=.162638.

A new controlled uniform-source response, a relaxed full-sector energy, long-production health/convergence and physical Maxwell matching remain held. The current checks establish finite source algebra, covariance arithmetic and corrected tiny sampling only.

## Recovery and evidence status

The [complete original note](../.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md) and [complete original receipt](../.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt) are immutable dated history. All original program bodies, seeds, budgets, checks, tables and failures are retained in the same archive and authenticated by the [historical receipt index](../data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json). Earlier claims are not current authority. Current successful checks certify only the explicitly bounded diagnostics above. Historical production remains unvalidated under the corrected source; unavailable long-run evidence is held rather than restamped.
