# Analytic parameter selection for the quadratic inverse-norm majorant

Source-only derivation of the parent's proposed optimization. No actual rho, scalar, native moment or saved scientific value is read. No existing spectral implementation is modified. The target remains the inverse norm of the specified residual, with the same p and q; this selects an error bound, not a physical trial or nominal observable.

Let the supplied self-adjoint channel H>=delta>0 and r in Dom(H) have moments rho0=||r||², rho1=<r,Hr>, rho2=||Hr||². The imported majorant proof uses tau>delta. In fact its exact factorization is valid for every tau>0:

Q_tau(lambda)-lambda^-2 = (lambda-delta)(lambda-tau)²[(tau+2delta)lambda+delta*tau]/(delta²*tau³*lambda²)>=0.

Write z=1/tau. Direct expansion yields

U(z)=<r,Q_tau(H)r>=rho0/delta²+Bz+Cz²+Dz³,
B=2rho0/delta-2rho1/delta²,
C=3rho0-4rho1/delta+rho2/delta²,
D=2rho2/delta-2rho1.

The letters B,C,D here are scalar polynomial coefficients; D is not the channel operator. All three proposed coefficients are correct.

For the spectral measure dmu_r(lambda),
 B=-(2/delta²) integral(lambda-delta)dmu <=0,
 D=(2/delta) integral lambda(lambda-delta)dmu >=0.
Finite rho2 suffices for these statements. If B=0 or D=0, positivity and lambda>=delta imply that the measure is supported at delta (including the zero vector). Then both vanish, C=0, and every tau has exactly U=rho0/delta²=||H^-1r||². Thus exact physical moments have no case B=0,D>0 or B<0,D=0. These cases can occur for arbitrary midpoint boxes and must not be treated as exact spectral facts.

In the nondegenerate case B<0 and D>0, U'(z)=B+2Cz+3Dz² has precisely one positive root, because its two roots have negative product. It is negative before that root and positive afterwards. The unique minimum over z>0 is

 z_*=(sqrt(C²-3DB)-C)/(3D),
 tau_*=(sqrt(C²-3DB)+C)/(-B)=3D/(sqrt(C²-3DB)-C).

The first z formula in the parent request is correct. The radical strictly exceeds |C|. To avoid cancellation, use tau=(sqrt(S)+C)/(-B) when C>=0, and tau=3D/(sqrt(S)-C) when C<0. The alternative z form is z=-B/(sqrt(S)+C); choose its branch with the same care if z rather than tau is wanted.

The optimum is admissible under the original restriction tau>delta, not merely the extended tau>0 theorem:

 U'(1/delta)=(8/delta³) integral(lambda-delta)² dmu >0

in the nondegenerate case. Since U'(0)<0 and there is exactly one positive root, 0<z_*<1/delta and tau_*>delta. Equality at the endpoint is possible only in the degenerate case already handled. The exact optimizer is global; C need not be nonnegative. For a point mass at lambda=L>delta, tau_*=L and the majorant is exact. A point mass at L=1/2 with delta=1/4 explicitly supplies an optimizer below the old fixed family's minimum1. These are synthetic examples, not native residuals.

## Deterministic bounded proposal from interval midpoints

Exact optimality is not an interval certification rule. A new implementation may propose tau from midpoint moments, then certify at the exact rational proposed tau using the ORIGINAL moment intervals and signed majorant evaluation. Midpoints need not satisfy spectral inequalities. The proof works for any positive proposed tau, so a poor or clipped proposal only loses sharpness.

The accompanying inert proposal.py fixes delta=1/4, uses midpoint moments, and computes B,C,D. If B>=0 or D<=0 it returns tau=1; it makes no spectral inference from that fallback. Otherwise it forms S=C²-3DB>0 and a rational upper square-root approximation on a2^-256 grid. It evaluates the cancellation-avoiding branch above, clamps its dimensionless ratio tau/delta to[1+2^-32,2^24], then rounds UP to the2^-32 ratio grid. Thus the proposed tau is an exact positive dyadic, strictly above delta and no larger than2^22. Rounding or clamping does not establish optimality. No data-dependent search or repeated scientific evaluation occurs.

The frozen prospective candidate family is the old{1,2,4,8,16} plus this one proposal, deduplicated. The old rho0 upper/delta² bound is also retained. Every candidate is evaluated outward with the original rho intervals: the coefficient of rho1 in Q is negative, so its LOWER endpoint is used in an upper bound. If an apparent upper bound is negative, refuse the inconsistent certificate; do not silently square-root it. Taking the minimum over valid upper bounds cannot worsen the old certified result. Identical logic applies separately to first and inner residual moments, without changing their coefficients or nominal Ward value.

## Cost, domain and scientific scope

This adds no spectral moment: rho0..rho2 (or xi0..xi2) are already required. First degree-one residuals still need m0..m6; inner constant-q residuals need s0..s4, with the imported six-vector c,nu,omega5 closure. The remaining full operator factor ||H^-1J||<=||J||/delta is unchanged.

The proposal takes a constant number of rational operations, one integer square root, and one additional quadratic-moment upper evaluation per residual/channel. The source caps parsed rational numerator/denominator lengths at4096bits and explicitly checked returned intermediates at65536bits. A one-operation multiply/add transient can be bounded by262144bits under those guards; the radical uses an additional512-bit shift. These are prospective refusal limits, not claims about actual native moment sizes or a measured runtime. A future integration may separately justify a different bound before its freeze; it must not silently alter this one. The standalone tests use finite synthetic spectral measures and inconsistent midpoint examples only. The proposal source is not an execution-ready native runtime or authorization to read moments.
