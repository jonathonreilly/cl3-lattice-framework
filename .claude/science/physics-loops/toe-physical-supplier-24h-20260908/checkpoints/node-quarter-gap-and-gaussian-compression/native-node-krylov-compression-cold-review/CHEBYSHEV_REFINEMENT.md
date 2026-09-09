# Chebyshev refinement and structured covariance route

New independent derivation from root's proposed ellipse estimate. No physical action, moment matrix, or spectrum was evaluated. Earlier Taylor bounds remain preserved.

## Improved seed approximation

The unitary integral Taylor remainder removes exp(WL): for bounded skew K,

 ||exp(tK)-sum_(n<m)(tK)^n/n!|| <=(W|t|)^m/m!.

The integral remainder has unitary exp(sK), so its norm is bounded before integration. Since the two polynomials match on the seed span, the seed difference is at most twice this quantity. This improves the previous Taylor estimate but Chebyshev is better near the natural degree scale.

Apply polynomial approximation to the self-adjoint operator iK/W. On the Bernstein ellipse rho=exp(eta), the maximum of exp(-i tau z) is exp(tau sinh eta), tau=W|t|. Its Chebyshev coefficients have absolute values <=2 exp(tau sinh eta)rho^-n. Summing the tail and applying the same polynomial to both generators gives the seed error

 E_m(tau)<=4 exp(tau sinh eta)rho^-m/(1-rho^-1).

No dimension factor appears; polynomial equality holds on the entire seven-seed span. For rho=3/2 this is12 exp(5tau/12)(2/3)^m. The spectral scaling i does not require doubling the original real cyclic carrier: the real-time exponentials remain real, and this is merely a complex polynomial norm proof.

## Explicit full-node budget with infinite delta=h/4

Use h=1 units, beta<3, W<4, T=448, R=256. With sqrt(T)<22 and the elementary1/sqrt(2e)<=1 bound, the complete inverse approximation error is <=173160 exp(-28)<1.3e-7. The complete time truncation error is <=2039400 exp(-256/7)<3e-10. These use the actual soft-functional estimate, not vacuum norm alone.

For m=2304 and tau<=2048,

 E_m<=12 exp(2560/3)(2/3)^2304.

The lower bound log(3/2)>=2[1/5+(1/5)^3/3]=152/375 gives E_m<=12 exp(-30208/375). Insert this in the already derived full compression coefficient

 Ccomp=(90/8)[4beta M0M1+beta²(M0M2+M1²)].

Use M0<=44, M1=448, M2<=78848/3. The resulting compression error is far below10^-6. The covariance coefficient remains

 Ccov=(90/8)[6beta M0M1+(3/2)beta²(M0M2+M1²)].

Taking covariance operator error epsilon<=10^-6/(4Ccov) reserves2.5e-7 for covariance, leaving over half the total10^-6 budget for frame and kernel arithmetic. Exact constants and rational exponential comparisons are recorded separately. This still assumes exact cyclic compression and evaluation of explicit local-J insertions, not a compressed zero-mode identity or fictitious stationary compressed vacuum.

The real dimension bound is16128. One full binary64 real matrix requires2,080,899,072bytes, already exceeding384MiB. The improvement therefore does not by itself authorize a dense calculation.

## A genuine low-displacement-rank covariance structure

Let P=P_m, Q=I-P, Gamma commute with K, and write Gamma_m=P Gamma P and K_m=P K P. Then exactly

 [Gamma_m,K_m]=P K Q Gamma P-P Gamma Q K P.       (1)

Since K V_m is contained in V_(m+1), Q K P has rank at most7. Equation(1) therefore has rank at most14. This holds even though Gamma_m is mixed and generally does NOT commute with K_m. It does not imply that Gamma_m itself or its purity defect has low rank.

In an eigenbasis of iK_m, offdiagonal entries of Gamma_m are determined by the low-rank displacement generators divided by eigenvalue differences, with separate diagonal/degenerate-block data. Thus a Cauchy-like representation could store O(14d) generator entries instead of d² covariance entries. At d=16128 this is only a few megabytes of raw binary64 data. The unresolved obligations are a certified construction of those generators and the diagonal/degenerate blocks, stable treatment of clustered eigenvalues, and kernel operations exploiting that representation without materializing dense transforms. No conditioning guarantee follows merely from rank14.

Likewise a rank-two instantaneous perturbation does not imply rank-two R(t)-I. Only the trace bound ||R-I||1<=2beta|t| is automatic. Replacing its time integral by a finite-rank quadrature creates a time-channel determinant representation, but needs its own quadrature and phase/conditioning certificate. This is an algorithmic possibility, not an attained storage or runtime bound.

The low-displacement identity is a concrete structured-storage supplier missing from the earlier huge-box route. It avoids asserting a false low-rank covariance approximation. Practical evaluation remains open until the indicated structured operations and error bounds are supplied.
