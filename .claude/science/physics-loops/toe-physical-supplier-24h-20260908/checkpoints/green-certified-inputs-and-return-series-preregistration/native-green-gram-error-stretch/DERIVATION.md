# Certified local Green-to-Gram error budget

Provisional algorithm design with exact analytical bounds; no integral, Gram or spectrum run. Inputs are the reviewed local Green identities (1)–(3) in native-star-local-green-gram-stretch/DERIVATION.md. Real positive spectral parameters only. Scalar errors below are midpoint radii, half the full interval widths. Poles and h are exact; uncertainty in them requires additional terms.

## Block error from scalar intervals

Use spectral matrix norm. The actual seven-site matrices have ||N||=2, ||O||=1, ||T||=sqrt(6). Define

 r(s)=2s+s^3/(6h^2)+sqrt(6)s^2/(6h),
 b(s)=2+s^2/(6h^2)+sqrt(6)s/(6h).

Scalar midpoint errors eps_A(s),eps_B(s) imply

 ||Rhat_sigma(s)-R_sigma(s)|| <= r(s) eps_A(s),
 ||Fhattilde_sigma(s)-Ftilde_sigma(s)|| <= [r(s)eps_A(s)+b(s)eps_B(s)]/2.

These bounds follow directly by differentiating the affine scalar formulas; constant D and mu terms introduce no uncertainty, and mu cancels before any interval evaluation. They are conservative matrix bounds, not entrywise heuristics.

For q=sigma*s+tau*t nonzero the ordinary Gram block error is at most [r(t)eps_A(t)+r(s)eps_A(s)]/|q|. The negative-band block error is at most [r(t)eps_A(t)+b(t)eps_B(t)+r(s)eps_A(s)+b(s)eps_B(s)]/(2|q|). Independent subtraction is safe but can be useless when tau=-sigma and t is close to s. Same signs have |q|=s+t and no coincidence instability.

## Derivative branch and a rigorous switching rule

Set

 a0(s)=2+s^2/(2h^2)+sqrt(6)s/(3h),
 a1(s)=r(s),
 b0(s)=s/(3h^2)+sqrt(6)/(6h),
 b1(s)=b(s).

The derivative errors are bounded by

 E_Rprime=a0 eps_A+a1 eps_Aprime,
 E_Fprime=[a0 eps_A+a1 eps_Aprime+b0 eps_B+b1 eps_Bprime]/2.

For opposite pole signs let alpha=tau=-sigma, d=|t-s|, m=(s+t)/2, a=min(s,t)>0. The block is the average of R_alpha'(u)/(i alpha), or Ftilde_alpha'(u)/(i alpha), over the interval between s and t. At exact coincidence use this derivative, with its indicated sign, not a divided difference. Projection P0 commutes with h0 and is a contraction, so the full resolvent gives ||F'''(u)||,||R'''(u)|| <=6/a^4. The local compression and cancellation of the constant mu term preserve this bound. Symmetric Taylor integration therefore gives

 ||average F'(u)-F'(m)|| <= d^2/(4a^4),

and the same for R. Thus a certified midpoint derivative enclosure gives a robust block error E_Fprime(m)+d^2/(4a^4), without division by d. This holds even though individual scalar B higher derivatives are not computed. The bound uses the actual resolvent operator, not a separately rounded derivative integrand. At d=0 the truncation term is exactly zero.

Given a desired block error eta, select the derivative branch only if its certified error plus d^2/(4a^4) is <=eta; for example reserve eta/2 to each term, requiring d<=a^2 sqrt(2eta). Otherwise refine scalar intervals for the ordinary branch or subdivide the derivative integral with rigorous error. “Near enough” without this bound is not a certificate. Endpoint A',B' intervals alone do not enclose the midpoint derivative; compute midpoint inputs or rigorously enclose their variation. A future cancellation-free two-parameter scalar integral can avoid this branch overhead, but is a new implementation requiring review.

## From blocks to a meaningful matrix target

For n pole labels, retaining all seven local columns per label, the full Gram has size7n. If each 7x7 block error is eta_ij, its operator error is bounded by the spectral norm of the n x n nonnegative matrix (eta_ij), and hence by the square root of its maximum row-sum times maximum column-sum. A symmetric error ledger reduces this to the maximum row sum. Uniform eta gives delta_G<=n*eta, not7n*eta. Apply the same bound to the projected Gram H. Enforce Hermitian output by symmetrization; this cannot increase an operator error to the exact Hermitian target.

If Woodbury columns equal bare columns times a fixed coefficient matrix C, errors grow by ||C||^2. Coefficient uncertainty must be propagated separately; a large ill-conditioned C cannot be ignored. Exact duplicate/dependent columns must be removed or treated on their range before whitening.

A concrete conditional accuracy target is: certify delta_G,delta_H<=epsilon_cov*gamma/4, where gamma is a certified lower eigenvalue of the retained exact G and0<epsilon_cov<=1 is the desired covariance error. To see the scaling without an arbitrary coordinate comparison, put E=G^-1/2(Ghat-G)G^-1/2 and Z=G^-1/2 H G^-1/2, with0<=Z<=I. In the exact-G coordinates, normalize using S=(I+E)^-1/2. For e=delta_G/gamma<1, ||S||<=(1-e)^-1/2 and ||S-I||<=(1-e)^-1/2-1. Hence ||SZS-Z||<=||S-I||(||S||+1)<=e/(1-e). The perturbed projected Gram adds at most delta_H/[gamma(1-e)]. Total covariance error is therefore

 (delta_H+delta_G)/(gamma-delta_G).

The proposed quarter allocation bounds this by2epsilon_cov/3<=epsilon_cov. This comparison uses an explicit compatible frame gauge; arbitrary independently whitened coordinates differ by a unitary and must be aligned for downstream insertions. A lower bound gamma can, for example, be obtained from a separately certified lower eigenvalue of Ghat minus delta_G; no eigensolver certification is silently assumed.

Accordingly an honest uniform bare-block allocation is eta<=epsilon_cov*gamma/(4n||C||^2) for both Grams when C is exact and gamma belongs to the retained transformed Gram. This is a usable target once n, C and a certified conditioning bound are specified. No numerical scalar width independent of these data certifies a useful many-column covariance. The current1/32 scalar widths give radii1/64; they can be inserted into the displayed formulas, but neither n nor gamma nor the required downstream epsilon_cov is supplied by that pilot.

## Scope and next design obligation

This derives a finite Gram error ledger, not a proof of conditioning. Closely spaced resolvent columns can be genuinely nearly linearly dependent even with perfect subtraction. The derivative branch cures evaluation cancellation; it cannot cure a small gamma. A stable implementation should use divided-difference/confluent columns or certified rank truncation with an explicit discarded-subspace error. An actual matrix target requires: fixed pole list, column coefficients, rank/conditioning certificate, downstream covariance tolerance, and separate orbital/phase errors. No final accuracy or cost is inferred from the completed four-job scalar pilot.
