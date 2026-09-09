# A polylogarithmic-rank approximation to the stationary impurity projector

New analytic refinement of TRACE_CLASS_IMPURITY_PROJECTOR, for independent review. No physical resolvent or quadrature was evaluated. This is a finite-rank existence/construction bound for the stationary projector, not a completed quench-state algorithm.

Write F(s)=(h_A-is)^-1-(h0-is)^-1 and P_A-P0=-(2pi)^-1 integral_0^infinity [F(s)+F(s)^dagger]ds. Each F(s) has rank at most two. The preceding lemma gives ||F(s)||_1<=C0 with C0<1071/(25h). Self-adjoint resolvent norms additionally give ||F(s)||_1<=2beta/s² for every s>0, without a Neumann assumption.

On a complex disk |z-c|<=c/2, the resolvent identity bounds each bare or perturbed local resolvent column by twice its value at c. Therefore F is analytic there with

 ||F(z)||_1<=M(c)=min(4C0,8beta/c²).

Use dyadic real intervals [s,2s], centered at c=3s/2. The Bernstein ellipse of parameter rho=5/2 has maximum distance (s/4)(rho+rho^-1)=29s/40<c/2 from the center. The standard Chebyshev contour bound follows directly from Cauchy's formula: the degree-(2p-1) polynomial tail is at most (10/3) M(c) rho^(-2p). Positive p-node Gauss-Legendre quadrature integrates that polynomial exactly and has weights summing to the interval length. Its error in trace norm is thus at most

 (20/3) s M(c) (4/25)^p.

This is an operator-valued polynomial approximation argument; no dimension factor or Fock expansion is used.

Choose intervals j=-Jlo,...,Jhi-1 with s=h*2^j. Summing s M(3s/2) over all integer j is less than

 4C0*h + (64/3) < 14452/75.

The first term bounds j<0 by a geometric sum; the second bounds j>=0 using beta<3h. Combining quadrature and both omitted tails, with pi>3, proves a Hermitian finite-rank Q approximating P_A-P0 with

 ||(P_A-P0)-Q||_1
 <= (357/25) 2^(-Jlo) + 2*2^(-Jhi) +429*(4/25)^p.       (1)

The rank of Q is at most 4p(Jlo+Jhi), because each quadrature node contributes F+F^dagger. All finite-rank columns can be represented through actual impurity/bare resolvent columns; their infinite-space Gram entries need their own certified local Green-function evaluation. Equation (1) does not provide those entries for free.

In particular this gives rank O(log²(1/epsilon)), rather than the algebraic rank tail from trace norm alone. The constants remain conservative. The companion exact arithmetic lists sufficient ranks for three fixed tolerances without computing any physical matrix.

A physical covariance can be recovered without assuming Q itself is a projector. Let A=P0+Q and round its spectrum at 1/2. The resulting projector Ptilde differs from the true P_A by at most twice the error in (1) in trace norm: spectral rounding minimizes trace-norm distance to the set of projections, and the triangle inequality applies. The change from P0 is confined to span(range Q, P0 range Q), of dimension at most twice rank Q. Particle-hole symmetry must be preserved in the represented quadrature and rounding. This observation is a finite excitation-carrier construction, not a license to ignore parity or the physical phase of a vacuum implementer.

For a long-time quench one must still transport this finite excitation representation, control state and phase errors, and compute all required Gram data. The stationary rank bound alone does not establish a uniform finite-time approximation or 384-MiB cost. It nevertheless replaces an unquantified compression hope by a checkable explicit rank/error relation.
