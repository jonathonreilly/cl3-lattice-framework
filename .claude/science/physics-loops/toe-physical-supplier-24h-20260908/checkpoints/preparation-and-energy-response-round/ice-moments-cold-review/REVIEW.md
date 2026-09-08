# Independent local ice moment review

Mathematical disposition: PASS for the moment, variance and variational conclusions, with one required signed-source notation clarification before final source-hash PASS. Reviewed main DERIVATION f4bda3038bb17aa44d9645e7d54231307e30b1b6aa0fd587d252fed9096de447, complete preregistrations, check.py, curl_check.py, second_moment_variance.py, mutations.py, raw outputs and SECOND_MOMENT/KINETIC_SUM_RULE addenda. Historical variance and syntax failures are preserved. Complete original producer corpus is not re-audited. Earlier ice-physics spectrum is my own calculation, not an independent review of my own authority. New independent controls below reuse only main's geometry construction and use Python-integer graph sums rather than author moment matrices.

## Required local sign clarification

For orientation(a,b), the actual source dictionary gives Delta O=epsilon(r)*s_p(n)*exp(iq.r)*(1-exp(iq_a))/sqrt(volume), where s_p(n)=2n_a(r)-1. Reverse moves reverse this sign. The displayed epsilon_p is undefined; if it means root parity alone, the signed identity is false. Define it as epsilon(r)s_p(n), or display both factors. Current curl_check verifies only absolute squares and cannot detect this omission. My signed finite check finds1152 xy directed arcs failing the root-parity-only adverse. All squared changes, moment identities and reported values survive the correction unchanged.

## Independent arithmetic and operator checks

Independent check.py passes6 grouped exact controls: all signed L2 updates; missing-state-sign adverse; all moments0..8 using arbitrary-precision Python integers; exact numerator variances; denominator-correlated ratio influence; second-moment variance/influence. It obtains single-face ratio influence47744/1875, local4048/625 and second9232/625. Thus the printed decimal variance comparisons are correct. This is exact finite enumeration, not independent sampled configurations or an autocorrelation estimate.

Every geometric arc contributes to the graph Dirichlet form with factor1/2 because both directions are counted. The O_integer rescaling sqrt32 implies numerator variances divide by1024, not32. The author's normalization handles both factors correctly. On RK the uniform vector is ground state of the connected-component graph Laplacian, so the configuration measure is uniform and pure. The complex-mode identity uses absolute squared differences; the displayed nested commutator is correctly restricted to real/Hermitian O. No continuum curl approximation is used.

The variance reduction is conditional expectation over the uniformly proposed face at fixed configuration. It is valid for numerator variance at equal iid configuration count, and with the same random denominator the ratio influence also conditionally averages. It does not establish equal CPU cost, unbiased finite ratio estimates, or ordering of arbitrary correlated-chain asymptotic variances. The source explicitly preserves all three limitations. The repaired rational variance is sound; its former integer cast was a reporting defect and is honestly archived.

## Spectral interpretation

S and B are the Gram and energy forms on the same Krylov space. Positive-definite finite S gives the usual Rayleigh quotient minimum, an upper bound on the lowest supported energy. Nested subspaces give decreasing upper bounds; they provide no lower gap bound or residue. A finite Ritz quadrature matches moments through2k−1, not the complete spectral measure. The held-out discrepancies and nonclosure expose exactly this distinction. The full eigensystem's numerical support threshold identifies a finite observed support; it is not an interval-certified exclusion of arbitrarily tiny weights. The moment upper-bound theorem itself does not require that threshold or full-spectrum computation.

The support envelope B=2 maximum graph degree is valid for the Laplacian. With variance v, mean mu and interval radius r, bounding squared deviation by r² inside and max(mu²,(B−mu)²) outside gives the displayed lower bound on outside mass. It is weak but correctly directed. It excludes a single exact spectral energy, not an infrared pole plus continuum.

## Detuning and kinetic-source addendum

For psi>0, (H−E0)(Opsi)/psi has the weighted-difference form because the ground equation cancels diagonal terms. Its reversible measure is psi², not psi. The resulting local first and second moments have the stated weights. Uniform flippability and mixed-amplitude sampling are not substitutes. The finite detuned comparisons are useful negative controls.

KINETIC_SUM_RULE_ADDENDUM is correct: at this transverse momentum geometry, constant squared change on ab arcs gives mu1=qhat²<A_ab>/(2 volume S). At RK coherence equals mean flippability, but not generally off RK. For H(t)=H−(t−1)A_ab, finite simple-ground Hellmann–Feynman gives E0'(1)=−<A_ab>. This avoids an overbroad claim that every measurement method needs pointwise amplitude ratios. It still requires the actual pure ground state or a validated equivalent response estimator. No new source selection follows.

## Legitimate next larger-L RK probe

Freeze even L4,6,8 and harmonics1,2 on the same prescribed mobile component, before execution; do not enumerate the Hilbert space. Track orientation flippability counts and staggered S(q) with independent seeded chains, block/autocorrelation diagnostics, and multiple legal starts. Use the same observations for numerator/denominator covariance. Measure cost per independent estimate before choosing a total budget. No claim that local updates mix across disconnected components is allowed. These are prospective choices, not a launched job or a guaranteed runtime.

The sharp discriminator is whether S(q) stays nonvanishing while mean orientation flippability per volume stays finite, yielding mu1<=C qhat² on those sampled components. In a proven uniform version, positivity gives Markov's bound: spectral weight above K C qhat² is <=1/K. Thus a first-moment upper bound plus a structure-factor lower bound can locate substantial LOW-energy spectral weight without a late-time fit. This is stronger than merely bounding one invisible low eigenvalue, but still does not prove a narrow pole, lower dispersion law or positive photon velocity. Finite samples cannot establish those uniform premises.

At RK a q² energy scale is a z2 control, not evidence for a detuned z1 photon. The detuned extension needs kinetic coherence/pure S and a new validated estimator. A larger RK run may test scalability and the relevant structure-factor premise; it cannot by itself settle the detuned Coulomb phase or physical electromagnetic identification. Sampling uncertainty/mixing remains the next hard obligation, not another flexible fit to1/L.
