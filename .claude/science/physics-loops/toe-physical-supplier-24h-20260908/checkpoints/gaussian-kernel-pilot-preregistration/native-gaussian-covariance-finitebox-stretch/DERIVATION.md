# Explicit finite-AP covariance bound on a fixed local box

Conditional analytic bound, not an executed finite covariance or infinite-node certificate. Uses exactly the canonical pi gauge, pure Gaussian reference and centered local identification of8063, together with its conical Bloch dispersion. No wrong-flux gap or improved pair threshold is needed for this covariance comparison.

## Conventions and actual scalar integrands

Let the physical torus side be L=4M and n=L/2 be its number of doubled magnetic cells per axis. Reduced momentum has spacing h=2pi/n; antiperiodic momenta are the centers of the n³ cubes partitioning [-pi,pi]³. Since n is even, the origin is the common corner of eight grid cells, not a sampled point.

In the periodic eight-site cell gauge the normalized Hermitian hopping symbol is the conjugate of

 S0(k)=sum_a Gamma_a sin(k_a/2) / r(k),
 r(k)=sqrt(sum_a sin²(k_a/2)),

by the diagonal half-cell phase matrix. Gamma_a=(product_(b<a)Z_b)X_a. Thus an entry is zero unless the cell parities differ in exactly one bit a. For such a pair, the real-space Fourier coefficient is, up to a constant unit phase/sign,

 F(k)=exp(i xi dot k) sin(k_a/2)/r(k),

where xi is half the physical displacement of the two sites (a sign choice for xi does not affect the estimates). The half-integer phase in the differing coordinate cancels the sign change of sin(k_a/2) across the BZ boundary, so F is periodic. This statement is for the actual matrix entries, not a replacement of the matrix projector by a scalar dispersion.

Use the real Majorana covariance Gamma_xy=(i/2)omega([gamma_x,gamma_y]), of operator norm at most1. Its off-diagonal entries are these sign-symbol Fourier coefficients up to a unit phase; the identity part of omega(gamma_x gamma_y) cancels in the finite/infinite difference. The spectral projector P differs by a factor1/2, so its entry error is half the bound below. The bounds do not depend on the hopping magnitude or its sign, provided it is nonzero.

## A safe derivative estimate

Put a=|xi|2 and u(k)=s(k)/r(k), s_j=sin(k_j/2). For any real direction y,

 |Ds[y]| <= |y|/2,
 |D²s[y,y]| <= r |y|²/4.

The normalized-vector derivative is (I-u u^T)Ds/r. Differentiating again, using ||D(I-u u^T)[y]||<=2|Du[y]| and |Dr[y]|<=|Ds[y]|, gives

 |Du[y]| <= |y|/(2r),
 |D²u[y,y]| <= (1/4+3/(4r²)) |y|².

Consequently the directional Hessian of the complex scalar F obeys

 |D²F[y,y]| <= [a²+1/4+a/r+3/(4r²)] |y|².

On the BZ, sin(|k_j|/2)>=|k_j|/pi, so r>=rho/pi where rho=|k|2. This controls the only singularity at the origin.

## Composite midpoint estimate with explicit constants

Remove the eight cubes contained in [-h,h]³. Their total normalized contribution to the sum-minus-integral error is at most16/n³, because |F|<=1. Every other grid cube Q has distance d_Q from the origin at least h. For x in Q, |x|<=d_Q+sqrt3 h<=(1+sqrt3)d_Q, whence

 d_Q^(-s) <= (1+sqrt3)^s |x|^(-s), s=1,2.

Taylor expansion around the midpoint has zero averaged linear term. The mean squared displacement in a cube is h²/4, so its error is bounded by h²/8 times the supremum of the bracketed Hessian estimate. Averaging over all remaining cubes, and enlarging the BZ to the radius sqrt3*pi ball for the singular integrals, gives

 average rho^-1 <=3/4,
 average rho^-2 <=sqrt3/(2pi).

Here average means integral divided by (2pi)³; enlarging the domain is only used for the positive singular integrands. Therefore

 |Cov_L(x,y)-Cov_infinity(x,y)|
 <= pi²/(2n²) [a²+1/4+(3pi/4)(1+sqrt3)a
                         +(3pi sqrt3/8)(1+sqrt3)²] +16/n³.

The elementary upper bounds pi<22/7 and sqrt3<7/4 make the square bracket at most a²+7a+16. A convenient completely rational bound is

 epsilon_n(a)=5(a²+7a+16)/n²+16/n³.                 (1)

For a local Euclidean radius-R ball, any pair has a<=R. Thus epsilon_n(R) bounds all local covariance entries. Require n>=4 and that the centered physical ball fits without a seam identification collision, for example L>4R. The estimate is conservative; it does not assert sharp convergence rate. One may always replace any entry bound by its trivial upper bound2.

## Matrix norms and a non-factorial Pfaffian transfer bound

For m real Majorana sites in the local region, entrywise(1) implies

 ||Delta Gamma||_op <= m epsilon_n(R),
 ||Delta Gamma||_F <= m epsilon_n(R),
 ||Delta Gamma||_trace <= m^(3/2) epsilon_n(R).

These are covariance matrix norms, not a claim about the trace distance of the many-body states. The latter is not imported without a separate theorem.

There is nevertheless a direct useful expectation bound. Let gamma(u_1)...gamma(u_(2p)) be an ordered product of real unit-norm linear Majoranas supported in this region. Interpolate Gamma(t)=(1-t)Gamma_0+tGamma_1. Every interpolated real antisymmetric contraction is the covariance of a valid finite mixed quasifree state (extend an odd-dimensional local list by an unused Majorana if needed). Differentiate its Wick Pfaffian. Each differentiated contraction is bounded by ||Delta Gamma||_op, and each complementary Pfaffian is the expectation of the remaining ordered Majorana product in that same valid state, hence has modulus at most1. Thus

 |omega_1(product)-omega_0(product)|
 <= binom(2p,2) ||Delta Gamma||_op
 <= binom(2p,2) m epsilon_n(R).                    (2)

This avoids the factorial obtained by bounding every Wick pairing separately. For individual site Majoranas, the sharper binom(2p,2) epsilon_n(R) follows directly. For nonunit real vectors multiply the right side by their norms; scalar i factors do not change it. General complex coefficient vectors require the corresponding CAR operator-norm factors, not the real isometry. Arbitrary Gaussian exponentials are not covered for free: a controlled expansion/product representation and its coefficient/norm sum are still necessary.

## Practical consequence and limitations

This proves quantitative local-state convergence but is too pessimistic for a brute-force finite-grid certificate at high precision. As a concrete bound example, R=2, m<=125, and four real unit linear insertions give error <=750[170/n²+16/n³]. At n=360000 this is below10^-6 by rational arithmetic, but n³ exceeds4.6e16 grid points. Even four site insertions, without the factor m, need n about32000 under this estimate. No such grids are proposed or executed.

The price applies to a naive full AP sum, not a lower bound on all algorithms. Direct certified local Fourier cubature, cone subtraction, symmetry cancellation or an analytic heat-kernel/image representation could be much cheaper. A likely improvement exploits oddness and midpoint cancellation near the cone, but no stronger rate is established here. Likewise a Gaussian time-slice kernel needs its separate spatial truncation and approximation errors. Formula(2) is a bridge for its genuinely local polynomial/insertion constituents; it does not yet certify the full semigroup kernel or infinite alpha.

The useful next bounded step is to derive cone-subtracted coefficient quadrature with an explicit smooth remainder, before choosing any finite-size physical job. No finite-L h/6 gap, node value, Gaussian conditioning estimate or numerical precision outcome is inferred.
