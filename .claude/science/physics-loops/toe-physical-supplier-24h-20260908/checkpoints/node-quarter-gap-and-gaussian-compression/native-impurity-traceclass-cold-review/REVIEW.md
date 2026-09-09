# Independent review: infinite native impurity projector

Disposition: PASS for TRACE_CLASS_IMPURITY_PROJECTOR.md SHA256 5654417a40c26abf8e634d79cdbe5d7cd63dfa2643677488813111678d4ef0c1. Read its complete proof, the companion normalized-time DERIVATION.md, and the actual pair determinant/Green identities in native-infinite-star-node-stretch/UNIFORM_PAIR_GAP.md. No physical computation was executed. This review does not certify a finite-time quench algorithm.

## Resolvent and integral checks

With R0=(h0-is)^-1, R0*R0=(h0²+s²)^-1. On the two support vectors the latter compression is diagonal by bipartite parity, with entries A,B<=a/h². Thus ||R0 U||op<=sqrt(a)/h, not merely the Hilbert–Schmidt bound sqrt(2a)/h. This justifies the stated compression estimate. The two outside factors in Woodbury have Hilbert–Schmidt norms at most sqrt(2a)/h; the adjoint spectral parameter on the second factor gives the same bound. Schatten Holder then gives exactly the author's C0.

The interpolation determinant has first term (1-4lambda h²D)². The native identity s²A+6h²D=1 implies 0<=D<=1/(6h²), so its square is at least 1/9 on the full lambda interval. The other term is nonnegative. For an invertible 2x2 matrix the largest singular value of its inverse equals its largest singular value divided by the modulus of its determinant; no Hermiticity of the Woodbury matrix is required. Hence the inverse bound is valid uniformly down to zero energy.

At s>=2beta the resolvent identity and Neumann expansion give trace norm at most rank2 times beta/s² times2 =4beta/s². For the projector difference, sign(h)=(1/pi) integral_0^infinity [R(is)+R(-is)] ds. Multiplication by -1/2 and equality of the two trace norms gives the prefactor 1/pi in the bound. Neither a factor2 nor an active-parity division is missing.

The explicit conservative arithmetic is C0<1071/(25h). Splitting at6h gives integral <6426/25+2=6476/25; division by pi>3 gives <6476/75<87. All scales cancel, as required for a projector norm.

## Zero modes, limit and uniformity

The reference Fourier symbol has only measure-zero Dirac zeros, hence no l2 kernel. For an impurity zero eigenvector, the equation h0 psi=-lambda U V U*psi determines psi uniquely almost everywhere by the Fourier inverse of that finite source. The two local inverse columns are l2 by finite A(0), so this is a legitimate vector. Its support amplitudes obey the limiting 2x2 Birman–Schwinger equation, whose determinant stays at least1/9. Therefore they vanish and psi=0. This closes the zero-mode step without an assumed spectral gap.

The near-zero bound controls the difference in trace norm even though the individual sign integrals are not trace-norm integrable. Away from zero the finite-rank resolvent formula is continuous in lambda; the common integrable envelope proves trace-norm continuity of the projector difference. There is no inferred volume-uniform AP estimate in this conclusion: the proof uses the infinite local Green bounds. No reference-overlap or Gaussian determinant branch is assumed.

## Precise consequences and limits

Write P=P_-(h_lambda), Q=P_-(h0). The proved trace-class difference is in particular Hilbert–Schmidt. Under the usual self-dual CAR realization for these real Majorana Hamiltonians, this is precisely the implementability condition for equivalence of their pure quasifree Fock representations. This statement uses the CAR implementability criterion as a separate representation-theoretic implication; the resolvent proof itself does not construct an implementer or fix its scalar phase. One can describe it concretely by the principal-angle decomposition: the squared sines are summable, so the infinite paired-rotation product defines a normalized Fock vacuum after treating the finite fully occupied directions separately. A fully occupied direction may make the overlap with the reference vacuum zero. Trace class alone cannot exclude it.

The expected number of reference quasiparticles in this stationary impurity vacuum is

 Tr((1-Q)P) = (1/2)||P-Q||HS² <87/2.

The equality uses particle-hole symmetry, which exchanges the two off-diagonal particle/hole traces; it is not a generic equality for arbitrary pairs of projections with nonzero index. Since |P-Q|<=1, its squared Hilbert–Schmidt norm is bounded by its trace norm. This supplies a coarse excitation-count bound, and Markov gives probability(N>n)<87/(2(n+1)). It is about the stationary impurity vacuum, not the normalized finite-time state in the companion note. It neither proves fast singular-value decay nor practical memory use.

For one-particle compression the stated tail ||D-D_r||HS<=||D||1/sqrt(r+1) follows by bounding the largest discarded singular value by ||D||1/(r+1). Applied to D=P-Q it is valid but coarse. Translating a truncated projector difference into a physical pure covariance requires a compatible principal-angle truncation, not an arbitrary matrix truncation. No useful fixed rank, nonzero overlap, alpha sign, or finite-time quench compression is established.
