# A source-only global projector quadrature budget

This is a new candidate, not an evaluation or refinement of the completed 66-node calculation. Work at h=1; rescale s by h otherwise. Import the supplied-model local trace-class estimate for F(s)=(h_A-is)^-1-(h_0-is)^-1,

 ||F(c)||_1 <= min(C0,V1/c^2), C0<1071/25, V1<6.

The positive projector difference is +(2pi)^-1 integral(F+F*) ds; the negative projector has the opposite sign. No zero atom and the trace-class integral premises are inherited from the reviewed projector proof.

## Complex ellipse and positive Gauss rule

For z with Re z>0 the resolvent identity gives

 F(z)=[I+i(z-c)R_A(z)] F(c) [I+i(z-c)R_0(z)].

Each factor has norm at most 1+|z-c|/Re z. On the Bernstein ellipse of parameter rho for [a,ba], center c=(b+1)a/2 and semimajor d=(b-1)a(rho+rho^-1)/4, assume d<c. Then

 M(a)= [c/(c-d)]^2 min(C0,V1/c^2)

bounds the nuclear norm throughout the ellipse. Holomorphy is in nuclear norm because the middle F(c) is trace class and the two analytic factors are bounded.

Truncating the Banach-valued Chebyshev series at degree 2p-1 has uniform remainder at most 2rho M(a) rho^(-2p)/(rho-1). The p-node Gauss-Legendre rule is exact on that polynomial, its weights are positive and sum to (b-1)a. Integration plus quadrature therefore has error at most

 4rho (b-1)a M(a) rho^(-2p)/(rho-1).

Taking the Hermitian part and the projector prefactor gives an overall factor 1/pi, not 1/(2pi), on the sum of these F errors. All these statements apply to operator quadrature, not merely scalar Green integration.

## Ratio-four panels

Take b=4,rho=5/2. Then c=5a/2,d=87a/40,c-d=13a/40 and c/(c-d)=100/13. For a=4^j, summing over all integer j is a conservative bound on any finite set of panels. Use the C0 bound for j<0 and the V1/c^2 bound for j>=0:

 sum_j a min(C0,V1/c^2) < (1071/25)/3 + (24/25)(4/3) =389/25.

Thus sum a M(a)<155600/169. With pi>3,

 epsilon_quad < (3112000/507)(4/25)^p <6139(4/25)^p.

The panel length is 3a. Omitting that factor would incorrectly give a constant three times smaller. An earlier informal message had that omission; the present displayed bound supersedes it.

## Concrete analytic budget

Take 18 panels [4^j,4^(j+1)], j=-16,...,1, hence interval [2^-32,16], with p=21 on every panel. This has 378 positive quadrature nodes, all NEW. Append the reviewed rank-two zero-endpoint correction at epsilon=2^-32. Its trace error is bounded by

 E_low=(2/9)(5439/160)2^-48+(1/6)(867/32)2^-64.

Append the reviewed N=15 high-frequency polynomial correction at S=16. Its error is bounded by

 E_high=(1/8)(9/64)^15 [1+18/(64*33)].

Then E_low+E_high+6139(4/25)^21 <2*10^-13.

Consequently a NEW finite operator approximation whose coefficient, Gram, arithmetic and any node-displacement errors total at most 8*10^-13 in nuclear norm would have error <10^-12. The latter budget is an explicit unsatisfied supplier condition. It cannot be inferred from a nominal scalar oracle width. No quadrature nodes, oracle values, native moments or matrices were evaluated here.

Each quadrature term F(s)+F(s)* has rank at most four. The zero correction has rank at most two and the high correction at most 58. The rank bound is therefore 1572 per pair geometry, before linear dependencies. The high correction uses bare Krylov powers through degree 28 and integer moments through 29. A naive square dense matrix at this dimension still carries material storage and arithmetic cost. The bound is not a numerical rank prediction or a runtime forecast.

## Existing nodes and sensitivity boundary

The old p=6 rule is immutable. Its positive analytic error bound is not an observed error floor, but this proof does not certify a 10^-12 approximation from its 66 nodes. Replacing the error estimate alone is insufficient. Subtraction of additional analytic operator terms could yield another method, but requires a new remainder bound and the relevant finite factors.

At low poles, independent enclosures for quantities such as (c-B(s))/s^2 lose information: interval radii divide by s^2 even when the exact numerator vanishes quadratically. A correlated identity, the exact identity cminus-B(s)=s^2 E[1/(sqrt(X)(X+s^2))], written as a positive integral before division, must be certified directly if it is used. The present operator quadrature budget does not solve that scalar input problem. For an assembled factor Z K Z*, perturbations must be charged at operator level; ||Z||^2||delta K||_1 plus the two factor perturbations is a valid sufficient bound. Per-entry scalar widths without factor norms and weights are not such a bound.

No physical computation, new result, occupation-tail success or kernel/alpha accuracy is claimed. The finite factorization is a proposed supplier for the separately proved state-weighted interface.
