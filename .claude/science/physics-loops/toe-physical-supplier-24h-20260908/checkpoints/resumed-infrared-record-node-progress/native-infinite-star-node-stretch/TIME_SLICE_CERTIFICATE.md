# A volume-free time-slice certificate for the node representation

This is an algorithmic error bound before a numerical pilot. It does not assert that its conservative constants make the eventual node sign inexpensive. The actual target is formula(B) in NODE_GAUSSIAN_REPRESENTATION.md.

Let W=||K||=4sqrt(3)|t_hop|, beta=||K_A-K||=4sqrt(2)|t_hop| for a two-edge star pair, and b=||(K_A-K)q||=beta. These are one-particle norms. The corresponding many-body local perturbation has norm beta/2. Put S=|s|, T=|t| and Ltime=S+T. The symbol Ltime below is a duration, not the torus size.

## Piecewise-constant interaction picture

Approximate each cocycle's interaction-picture generator by its left-endpoint value on intervals of length at most Delta. Exponentiate that fixed rank-two generator exactly in each step; every approximate factor is still a genuine unitary Gaussian spin operator. Use the same ordered factors to obtain its real orthogonal one-particle map. No polar repair or unverified normalization is part of this construction.

For the one-particle generator D_A(r)=L_H(-r)(K_A-K)L_H(r),

 ||D_A||<=beta, ||D_A'||<=2W beta,
 ||D_A q||=b, ||D_A' q||<=W b.

The last estimate uses Kq=0. For the many-body generator, differentiating the center/neighbor Majorana product bounds its derivative by W beta. Duhamel comparison of unitary evolutions therefore gives

 epsilon_G <= Delta W beta Ltime,
 epsilon_R <= 2 Delta W beta Ltime.

Here epsilon_G is the many-body operator error of the complete two-cocycle product and epsilon_R its one-particle operator error. Signs of the real times do not change these norm estimates.

The generalized-q error is controlled separately, without multiplying epsilon_R by ||q||. Write u=(R-I)q. Its inhomogeneous equation has skew homogeneous generator D and forcing Dq. Both the exact and approximate solutions satisfy ||u(r)||<=br. The generator difference applied to u is bounded by2W beta Delta br, while its action on q is at mostW b Delta. Integrating yields the safe composite bound

 epsilon_q(Ltime) <= Delta W b [Ltime+beta Ltime^2].

The same estimate applies to the inverse center segment needed for q dot l. A time-shifted free interaction picture preserves Kq=0 and every displayed norm, so composing the two segments does not introduce a volume factor.

## Pointwise overlap error

Write the integrand F=a<G>+(1/2)<gamma(l)gamma(d)G>. Exact and approximate orthogonal evolutions obey |a|<=1+bT, ||l||=1, ||d||<=bLtime. Applying the triangle inequality before taking the Gaussian expectation gives

 |F-F_Delta| <= epsilon_q(T)
 +(1+bT)epsilon_G
 +(1/2)[(2Delta W beta T)bLtime+epsilon_q(Ltime)+bLtime epsilon_G]
 <= Delta W[3 beta Ltime+5 beta^2 Ltime^2],

where the last line uses b=beta and rounds constants upward. This certificate bounds the physical overlap, independent of any potentially ill-conditioned Gaussian determinant formula. The Pfaffian arithmetic error must be added separately.

On the square |s|,|t|<=Tcut, a conservative complete90-word integrated discretization error is

 (90/8) M0^2 Delta W [6 beta Tcut+20 beta^2 Tcut^2].

Together with the preceding explicit filter-tail bound this provides prospective choices of Tcut and Delta for an absolute tolerance. It is not a measured quadrature convergence criterion.

## Remaining finite numerical steps

An explicit finite-smoothness polynomial inverse filter is sufficient for this computation: take an odd cutoff of -1/x with a polynomial beta-profile transition between delta/2 and delta, with at least twelve flat derivatives at each endpoint. It supplies enough weighted Fourier moments for the node extraction and its time tail. The resulting smooth coefficient has a unique node value by the opposite-ray argument, so it computes the same scalar as the parent infinitely smooth creator. Piecewise derivative integrals give rigorous filter tails. No such filter's constants have yet been optimized or evaluated here.

Every point evaluation then reduces to an ordered product of O(Tcut/Delta) rank-two Gaussian factors. Its branch-safe ordered Wick Pfaffian has order proportional to that number, not to lattice volume. Its contractions are integrals of the explicit free covariance and propagation. Interval contraction quadrature and rational/interval Pfaffian evaluation remain mandatory. Finite-size active eigenvectors and a bare square root of a determinant are not substitutes.

Real-time scalar quadrature is two-dimensional. On each time quadrant the filter and overlap are differentiable; the one possible Fourier jump at zero is handled by splitting the quadrants. Generator and generalized-q bounds give polynomial-in-Tcut derivative bounds, so elementary panel quadrature can be certified. A proposed implementation must record actual constants, point count and arithmetic precision before any physical evaluation. Polynomial matrix size does not mean the conservative error budget is already computationally practical.
