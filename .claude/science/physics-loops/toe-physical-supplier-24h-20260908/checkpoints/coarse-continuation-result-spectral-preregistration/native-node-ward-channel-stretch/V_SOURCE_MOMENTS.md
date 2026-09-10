# Exact one-body boundary moments and what their bounds do not close

New source-only continuation of the full Ward formula. Native kernels and accepted scalar values are not evaluated. Work first at h=1. Write B_A=i gamma0 gamma(d_A), ||d_A||²=2, and d_all=sum over a matching d_A, ||d_all||²=6. This d convention is half the d in the earlier expression B=(i/2)gamma0 gamma(d).

Let V_A=W_A-2gamma0 and L_A=[H0,V_A]. The bounded cross-commutator identities imply

 L_A=3J_A-J_all=i gamma(6d_A-2d_all),
 ||L_A||²=48,
 [V_A,B_C]=0 for every pair C.

In particular H0 V_A Omega=L_A Omega is a one-particle vector. Its energy support is within[0,6], without a spatial cutoff on V_A. Put n_A=||V_A||² and e_A=<V_A Omega,H0 V_A Omega>. Then the exact moments in the V_A vacuum vector are

 M0=n_A,
 M1=<V_A Omega,D_A V_A Omega>=e_A+n_A c,
 M2=<V_A Omega,D_A² V_A Omega>=48+2n_A+2c e_A.                 (1)

Here c=mu/3 is the reference scalar, not the impurity ground shift.

To verify the cross term in M2, write L=i gamma(ell), ell=6d_A-2d_all. Equal incident-edge expectations give <i gamma0 gamma(ell)>=6c-2mu=0. Also V is a real white-sublattice vector with zero center coefficient, so its real scalar product with gamma0 vanishes. The reference Gaussian Wick rule therefore gives <B_A V_A L_A>=c e_A: the second contraction vanishes by white parity and the third by the preceding center-ell identity. Since L*=-L and {V,L}=0, Re<L Omega,B V Omega>=Re<V L B>=c e. Together with B²=2I and ||L Omega||²=48 this proves(1). No impurity-vacuum replacement is used.

The existing local Green identities express these quantities as

 n_P=72 A(0)-4, n_O=8,
 e_P=72 cminus-4mu, e_O=8mu.

For general h, n_P=72h²A(0)-4, e_P=72h²cminus-4mu, e_O=8mu, M2=48h²+2h²n+2ce. The cross <w,|h0|e0>=mu/3 and inverse-neighbor even/odd scalar identities give these expressions. They are identities in the declared covariance convention, not numerical evaluations.

## A useful upper inverse moment from only M0,M1,M2

For any D>=delta and vector b, with Mj=<b,D^j b>, Cauchy in the nonnegative measure weighted by x-delta gives

 <b,D^-1 b> <= M0/delta - (M1-delta M0)²/[delta(M2-delta M1)]. (2)

Indeed1/x=1/delta-(x-delta)/(delta x) and E[(x-delta)/x]>=E[x-delta]²/E[x(x-delta)]. If the denominator is zero, the spectral measure is concentrated at delta and the inverse moment is M0/delta; do not divide by zero. A valid numerical enclosure must retain the nonnegative moment-matrix premise rather than clipping inconsistent data.

Equations(1)-(2) improve the bound on ||R_A V_A Omega||² via D^-2<=D^-1/delta, using only A0,cminus,mu and delta. They supply a concrete scalar-only bound instead of a whole Gaussian propagator. They do not determine the mixed inner product in ||[R_A,V_A]Omega||².

For that commutator, the universal spectral-diameter estimate is already

 ||[R_A,V_A]|| <=sqrt(n_A)/delta,

because R_A lies in[-1/delta,0]; subtract its interval midpoint before applying the commutator triangle inequality. This is a factor two better than bounding its two products separately. With delta=1/4, n_O=8,n_P<=82/5, sum_A n_A<=1104/5 and sum_A||R_A Omega||²<=240, the signed90-pair centerless correction satisfies

 |Re<x,T p_V>| <=6 sqrt(240*16*(1104/5)) <5525,
 p_V,A=gamma0[R_A,V_A]Omega.                                  (3)

This valid upper bound is far larger than the direct-term lower bound3. It cannot close the full sign. The improved inverse moments(2) can be inserted into a state-dependent commutator triangle or covariance bound, but no source-only argument here proves them sufficiently small. Accurate scalar moments are not themselves a bound on the required signed cross-correlations.

The center boundary vector also has exact inexpensive moments. Conjugating by gamma0 turns D_A into its four-link complement D_comp, still >=delta. In the original vacuum its perturbation has square4h²I and mean2c. Thus for b=gamma0 Omega, M0=1,M1=2c,M2=4h², and(2) yields

 <gamma0 Omega,D_A^-1 gamma0 Omega> <=1/delta-(2c-delta)²/[delta(4h²-2c delta)].

This bounds the center-source inverse norm, but not its signed cross products with R_C Omega. It keeps the complementary four-link Hamiltonian explicit; it does not replace its boundary state by an impurity ground vacuum.

## Matching cancellation was tested, not assumed

The exact three-pair identity Wsum=6gamma0 does not cancel the full correction. A one-active-channel Clifford toy happened to have zero centerless-tail sum; an attempted assertion of a nonzero tail failed and is preserved. A separately fixed two-active-channel/six-Majorana rational Gaussian toy obeys Wsum, Vsum=0, [V_A,B_C]=0, [W_A,D_A]=-J_A, positive D_A and Dsum=2D0+gamma0D0gamma0, but its centerless-tail sum is390290501015242800/72607265548152554879, not zero. These are not native six-neighbor baths and do not refute native positivity. They refute obtaining exact cancellation from only those displayed identities. Both toy full Ward sums were positive.

The remaining native possibility is a stronger inequality coupling the signed boundary cross terms to the positive direct term, or an additional spatial/bath identity absent from these toys. No generic CAR positivity, determinant-overlap positivity, scalar sign extrapolation, or law-selection conclusion is inferred.
