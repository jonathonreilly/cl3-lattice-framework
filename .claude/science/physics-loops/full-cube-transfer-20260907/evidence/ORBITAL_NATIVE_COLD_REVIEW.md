# Independent cold review of the full-cube uniform/operator proof

Reviewed native full-cube-uniform-limit/DERIVATION.md SHA6058464c1123745735e462fbc3b61dd7f786fde8aad4464d922aaf0e60cc1b68. This review is frozen before reading root full-cube-transfer/DERIVATION.md. The exact modal geometry is independently supplied by this reviewer's previously frozen28-check calculation and proof541ec391d4a51b2a6996a5f9b9db2677eb40332f5db9df47b29574a2cc78df58. Verdict: PASS for the conditional full24-face finite transfer and stated polynomial simultaneous limit. No numerical onset or physical action selection is obtained.

## Exact physical operator and dimension

Independent tree analysis agrees: the whole invariant boundary is L2(SU3^5)^single simultaneous Ad, an onto Haar isometry after a7edge tree. T=Msp C Msp preserves it exactly because both factors commute with the vertex gauge action. Restriction powers are therefore genuine T powers; intermediate slices carry full spatial weights, not an I I* spectator reset. Restoring temporal links and choosing7+7+1tree edges leaves literal5left+5right+7temporal chord groups. Global-Ad projection uses one conjugation per whole boundary.

There are136 full,80 joint boundary and56 nuisance real logarithm coordinates. Gaussian full partition has beta^-68, nuisance beta^-28; each boundary measure beta^-20 and chart isometry amplitude beta^-10. Conjugating a group kernel by both chart maps contributes beta^-20, and a further beta^-20 operator scaling converts its normalized beta^40 marginal peak to the finite Gaussian kernel. The total Haar denominator tends to j0^5, not a Cartan-rank or generic-orbit-volume power. These dimension factors are correct.

## Uniform geometry and determinant

On fixed nested product charts, E_k>=E_1 for k>=1 yields a k-independent positive quadratic lower bound and complementary gap. Every fixed-order derivative of the finite plaquette action grows at most Ck. The temporal linear constraints first kill7time-tree variations and then identify5left/right variations, giving rank12. Spatial curl is positive on their five-dimensional kernel, by the independent full spatial geometry. Thus H1 is positive definite.

Factoring H1, the determinant is detH1 product_(12)(1+(k-1)nu_j), with fixed positive nu_j. This rigorously gives detH_k comparable to k^12 and Z0(k) comparable to k^-48 in eight colors. No k-dependent gauge measure is introduced. The source covariance's plus eigenvalues are fixed positive and minus eigenvalues scale k^-1. Its80-dimensional determinant is comparable to k^-40, so ||g_k||2 is comparable to k^10. Polynomial-weighted L2 norms obey the same upper power: g_k² normalized has covariance Sigma_k/2 with uniformly bounded largest eigenvalue.

## Taylor and tail estimates independently reconstructed

Let F(epsilon,z)=chi(epsilon z) j_full(epsilon z) exp[-E_k(epsilon z)/epsilon²]. Extend at epsilon0 by its Gaussian value. On the compact chart, integral Taylor formulas bound the first derivative by Ck P3(z) exp(-c|z|²), including the cutoff/Haar terms in a larger fixed polynomial. Second derivatives are bounded by C(k+k²)P6(z) exp(-c|z|²). For a derivative along0 toepsilon, points remain inside the star-shaped charts where the uniform lower action applies. Cutoff derivative terms are supported away from the origin and satisfy the same polynomial/Gaussian bounds. No requirement that epsilon k|z|³ be pointwise small is being used to expand an uncontrolled exponential.

At epsilon0 the full first derivative is a cubic odd function times an even centered Gaussian; Haar and cutoff contribute no linear term there. Therefore partition error is Ck² epsilon². Integrating nuisance variables in the first derivative bound yields a Gaussian-polynomial function of80source coordinates with L2 norm Ck. This proves unnormalized marginal error Ck epsilon. Conditional cubic cancellation is correctly NOT claimed: ten fixed Lie vectors can span more than two dimensions.

The normalization calculation is explicit. Let deltaZ=O(k²/beta), deltan=O(k/sqrtbeta), Z0>=c k^-48. Once beta>=Ck^50, Ztilde>=Z0/2. Then

 ||p-g||2 <= C k^48 ||deltan||2 + C k^48 |deltaZ| ||g||2
           <= C(k^49/sqrtbeta+k^60/beta).

The second term/first is k^11/sqrtbeta, bounded under beta>=Ck^50. This checks both exponents49 and60 without substituting a probability bound for an amplitude norm.

The compact nuisance tail in the unnormalized scaled marginal is O(beta^28 exp(-g beta)); the80-dimensional scaled source window has volume O(beta^40), so its L2 contribution is O(beta^48 exp(-g beta)). The full scaled partition tail is O(beta^68 exp(-g beta)). Those rates are bounded by the respective Taylor rates uniformly for k>=1. For a source outside its chart, normalized group kernel is bounded by C beta^68 k^48 exp(-g beta); after beta^-20 amplitude scaling its HS norm is C beta^48 k^48 exp(-g beta). These bounds are strong enough and do not rely on merely small discarded probability.

The two boundary square-root Haar factors differ from their constants by O(beta^-1 times a fixed quadratic polynomial) on the chart. Applied to g_k this costs Ck^10/beta, lower order. Applying their bounded multiplier to p-g does not worsen its k power. Source Gaussian chart tails have a uniform quadratic exponent and polynomial k amplitude and are also absorbed. Global-Ad averaging contracts L2; no extra projection loss occurs.

## Norm normalization and actual powers

The Gaussian top eigenvalue is a fixed positive Haar/metric factor times product_j(sqrt(sigma_plus,j)+sqrt(sigma_minus,j))^-8. Because sigma_plus is fixed and sigma_minus is bounded for k>=1, this is bounded above and below away fromzero. The invariant ground is the unrestricted Gaussian ground; projection does not reduce its norm. Therefore an absolute operator error Ck^49/sqrtbeta stabilizes division by the actual norm when beta>=Ck^98 (increase the finite constant to make the relative error small). The omitted group-space chart operator is controlled by the same absolute error.

For clarity, write B=A/||A|| and P for the group chart projection. The full-space bound ||B-PBP||<=delta implies ||B^n-(PBP)^n||<=n delta, since both are contractions. The chart map U is an isometry from PHphys onto the supported invariant Lie-space subspace, so U(PBP)^n U*=(UPBP U*)^n for n>=1. Gaussian comparison adds another n delta. This explicitly bounds true physical powers rather than silently replacing them by repeated chart resetting.

For k_n=n²/t² and beta_n=n204, threshold k_n^98=O_t(n196) is eventually satisfied and n delta=O_t(n^-3). The Gaussian exponents have n t_k,j=t sqrt(lambda_j)+O_t(n^-2). For commuting number operators, ||exp(-aN)-exp(-bN)||<=|a-b|/[e min(a,b)] follows by mean-value differentiation and sup_(x>=0) x exp(-cx)=1/(ec). Summing five factor differences yields O_t(n^-2), also on the global singlet subspace. Combining both errors proves the stated norm convergence after chart and oscillator identifications.

The ground is unique and invariant. The unique adjoint color bilinear gives6symmetric pairings among three frequency2species; no one-quantum singlet exists and all other excitation combinations cost more than4. Thus the limiting first singlet excitation4 with multiplicity6 is correct. It is not a physical mass-gap identification.

## Nonblocking canonical wording clarification

The final phrase 'boundary Haar and oscillator unitaries' should keep the earlier chart qualification explicit: U is a partial isometry on the original entire group Hilbert space, while oscillator scaling is a genuine Lie-space unitary. A precise final statement is convergence of U_n P_n B_n^n P_n U_n* to exp(-tH_eff), together with ||B_n^n-P_n B_n^n P_n||=O_t(n^-3). Equivalently use the displayed B^n-(PBP)^n control. The proof already supplies these bounds, so this is not a missing estimate or a mathematical obstruction.

Constants and onset remain unspecified, k_n and beta_n are deliberately supplied mathematical scalings, and the full24-face model is distinct from the prior22-face source compression. No stronger physical or uniform high-representation claim is licensed.
