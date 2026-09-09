# Independent low-rank impurity-projector review

**PASS with explicit rounding bookkeeping below**, source943237a3cabc4346fd8c7d9191833e77ea14a4dda249195b632eb92f86aa062a. Read complete LOW_RANK_PROJECTOR_CERTIFICATE.md, TRACE_CLASS_IMPURITY_PROJECTOR.md, rank_controls.py and RANK_RESULT.json. Reuse the independently reviewed native Green/determinant bound and Primary's complete trace-class-premise review041748c1. No physical quadrature, spectrum or matrix was evaluated.

## Analytic and quadrature bounds

For |z-c|<=c/2, the resolvent parameter iz stays at distance >=c/2 from the real spectrum. The resolvent identity from ic bounds each local column (and each required row) by at most twice its value at c. Writing F=-R_A Delta h R_0 and using the same two-column Woodbury bound as the premise gives4C0, not a bound inferred merely from||F(c)||. Independently, ||R_A||,||R_0||<=2/c and||Delta h||1=2beta give8beta/c². These factorizations prove trace-class analyticity and the stated minimum M(c). No many-body gap is needed here.

For [s,2s] the scaled Bernstein ellipse has semimajor radius(s/4)(5/2+2/5)=29s/40, strictly less than c/2=3s/4. Cauchy's formula is valid for the nuclear-norm Banach-valued function. Coefficient bound2M rho^-n and summation from degree2p give(10/3)M rho^-2p. A positive Gauss rule and the integral each cost at most the interval length times this approximation error, hence(20/3)sM(4/25)^p. There is no dimension multiplier. For F+F*, the doubled error cancels the2 in the1/(2pi) projector factor, leaving1/pi.

The geometric sum is4C0h for j<0 and at most64/3 for j>=0, so it is below14452/75. Multiplication by20/9 is below429. The omitted low and high ranges give respectively(357/25)2^-Jlo and2*2^-Jhi. Units cancel correctly. The rank bound4p(Jlo+Jhi) counts both the rank-two F and its adjoint at every node.

The exact recorded choices are internally consistent: at epsilon10^-6, Jlo26,Jhi23,p12, rank(Q)<=2352 and raw trace error<=2287839703834313821/4000000000000000000000000, about5.72e-7. The labels are upper bounds, not measured numerical singular ranks.

## Physical rounding and support

Let V=range Q and W=V+P0V. W is P0-invariant, since P0(V+P0V)=P0V. It is also Q-invariant because Q maps everything into V, and W-perp lies in ker Q. Thus A=P0+Q reduces W and equals P0 on W-perp. Spectral rounding changes the reference only on W, whose dimension is at most2rank Q. Rounding only inside V would generally be invalid.

For a self-adjoint matrix, threshold rounding is a nearest projection in trace norm: the finite-dimensional eigenvalue variation inequality reduces the minimization to eigenvalues0/1. The same statement applies here by finite-rank approximation in the trace-class affine space. Triangle inequality therefore gives||Ptilde-P_A||1<=2||A-P_A||1. At the three stated tolerances, this also implies||A-P_A||op<1/2, so A has NO eigenvalue at the rounding threshold1/2. No tie-breaking assumption is needed for these parameter choices.

In the real Majorana convention conjugation sends h to-h, hence sends R(is) to-R(is), Q to-Q and P0 toI-P0. Real positive quadrature weights preserve this exactly. Thus conjugation sends A toI-A, and the tie-free threshold projector satisfies C Ptilde C=I-Ptilde. W is also conjugation-invariant: C V=V and C P0V=(I-P0)V lies in W. This supplies a physical finite excitation carrier if the numerical representation preserves these relations. Approximate Gram/column arithmetic must certify or explicitly restore them; ordinary floating rounding is not automatically licensed.

**Bookkeeping:**2352 is rank(Q), NOT the final carrier dimension or a post-round error certificate. The enlarged support dimension is at most4704, and the general rounding error bound is twice the raw bound. In the recorded epsilon10^-6 row, this is about1.14e-6, so a demanded final projector error<=10^-6 would need a tighter raw budget. The source states the factor2 correctly; downstream use must retain it. No parity or physical implementer phase is proved by this rank argument alone.

## Scope and feasibility

The construction depends on certified infinite resolvent-column Gram data, not on free access to those columns. The trace-class and rank bounds are stationary. They do not prove finite-time quench accuracy, nonzero overlap or384MiB feasibility. No scientific correction to the stated rank approximation is required; the above physical rounding qualifications make its intended use precise.
