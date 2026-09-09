# Uniqueness of the supplied real homogeneous quadratic cubic gauge kernel

**Date:** 2026-09-04; source correction 2026-09-09.

**Claim type:** bounded_theorem

**Runner:** [scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py](../scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py)

**Current diagnostic receipt:** [logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt](../logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt)

**Premise boundary:** [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md). The Hamiltonian, state/readout, Born weighting and imaginary-time sampling protocol used here are supplied model choices. They are not derived primitives or a physical Record formation law. Formal audit is deferred by the owner; this source applies no audit status.

## Exact conditional theorem

Let K(q) be a real symmetric 3-by-3 matrix whose entries are homogeneous quadratic polynomials in a continuous three-vector q. Require covariance under the proper cubic rotations, K(Rq)=R K(q) R^T, and the polynomial gauge identity K(q)q=0 for every q. Then

    K(q)=B (|q|^2 I - q q^T).

The cubic half-turns and axis permutations reduce the diagonal entries to K_ii=A q_i^2+B sum_(j!=i)q_j^2 and the off-diagonal entries to K_ij=C q_i q_j. Substitution into K(q)q=0 gives A=0 and B+C=0. Thus the joint space is one-dimensional. Positivity would additionally require B>=0; it is not supplied by the covariance identity.

The runner independently constructs the 36-coefficient real symmetric homogeneous-quadratic ansatz. Its exact linear constraints give cubic dimension three, gauge-transverse dimension six, and joint dimension one; it checks every one of the 24 declared rotations and the explicit basis kernel. These are algebraic identities, not a finite grid extrapolation.

## Domain and physical boundary

Reality, symmetry, homogeneity of degree two, the continuous polynomial variable and cubic covariance are hypotheses. Nonlocal/nonanalytic terms, parity-odd or frequency-dependent terms, higher gradients and other supplied degrees of freedom are outside this theorem. The result does not prove that a spin-half Hamiltonian has this effective kernel, that B is positive, or that a physical time/readout yields Maxwell dynamics. Historical finite dispersion fits and magnetic occupation-sign response data supply no missing implication. The original 5/0 algebra is retained under this exact scope.

## Recovery and evidence status

The [complete original note](../.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md) and [complete original receipt](../.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt) are immutable dated history. All original program bodies, seeds, budgets, checks, tables and failures are retained in the same archive and authenticated by the [historical receipt index](../data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json). Earlier claims are not current authority. Current successful checks certify only the explicitly bounded diagnostics above. Historical production remains unvalidated under the corrected source; unavailable long-run evidence is held rather than restamped.
