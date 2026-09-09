# Positive exact return series for the local A function

In h1 units, X=4 sum sin²k=6-2 sum cos(2k). Put Y=2 sum cos(2k), q=s²+6>6. Uniform momenta give A(s)=E[1/(q-Y)]. Since |Y|<=6<q, the geometric expansion converges absolutely and uniformly. Odd moments vanish by translating all three folded angles by pi. The even moment counts length2n nearest-neighbor walks on Z³ returning to0:

 c_(2n)=(2n)! sum_(j+k+l=n)1/(j!²k!²l!²).

Group k of n paired steps in two coordinates. Vandermonde sum_j binom(k,j)²=binom(2k,k) reduces this to

 c_(2n)=binom(2n,n) sum_(k=0..n)binom(n,k)² binom(2k,k).

Every coefficient is a nonnegative integer and at most6^(2n), since returning walks are a subset of all six-choice walks. Thus

 A(s)=sum_(n>=0)c_(2n)/q^(2n+1),
 A'(s)=-2s sum_(n>=0)(2n+1)c_(2n)/q^(2n+2).

Termwise differentiation is justified uniformly on any compact s interval bounded away from0 by the weighted geometric majorant. With r=36/q² and the first m terms retained, explicit tails are

 0<=A-A_m<=r^m/[q(1-r)],
 0<=(-A')-D_m<=(2s/q²)r^m[(2m+1)/(1-r)+2r/(1-r)²].

All quantities are exact rational for rational s. These are bounds on the actual infinite native integral, not asymptotic estimates. There is no cancellation in either positive partial sum. The derivative enclosure is[-D_m-tail,-D_m]. No numerical integration or transcendental arithmetic is necessary.

The prospective six cases are s1,2,1/2, each at target widths1e-6 and1e-12. The smallest m with both tail bounds<=target is fixed from the formulas before evaluating any coefficients. Coefficients can be shared across cases, but the initial implementation computes them per case for simple complete timing; no outcome-selected truncation occurs. Work per case is O(m²) binomial operations with growing integers; root must measure real cost before any stronger forecast. The s approaching0 regime has m growing roughly s^-2 log(1/target), so this is not a uniform small-s solution for every projector quadrature node.

Dimensions restore as A_h(s)=h^-2 A_1(s/h), A_h'(s)=h^-3 A_1'(s/h). This proposal supersedes no prior data and leaves the frozen Gauss route unlaunched.
