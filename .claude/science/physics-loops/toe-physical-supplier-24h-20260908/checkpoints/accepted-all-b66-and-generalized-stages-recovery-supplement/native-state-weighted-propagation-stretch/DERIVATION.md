# State-weighted first-action propagation after uniform leakage exclusion

Status: source-only conditional support. No native matrices or saved event values are read or evaluated here. The first generalized24 action reports all ten squared uniform leakage lower bounds above0.53; its independent saved arithmetic is pending. That result motivates a different sufficient condition, not relaxation of the same uniform condition. It does not imply the initial physical insertions have equally large propagation errors.

Allowed premises: a self-adjoint one-body H on a complex Hilbert space; an isometry V:C^m→D(H), A=V*HV, R=HV−VA, and a specified finite input matrix X:C^k→C^m. The exact one-body physical H, finite Gram and first-action certificates remain supplied-model imports. No positive band, spectral gap, observed alpha or added physical axiom is assumed. The result below controls propagated vectors only; Gaussian vacuum/covariance and inserted determinant errors require their own explicit input representation.

For real u>=0, Duhamel gives

 e^(-iuH)VX − V e^(-iuA)X
 = -i integral_0^u e^(-i(u-s)H) R e^(-isA)X ds.

For either operator norm or Hilbert–Schmidt norm, define
 r_X^+(s)=||R e^(-isA)X||, r_X^-(s)=||R e^(+isA)X||.
Then ||difference at ±u|| <= integral_0^u r_X^±(s) ds; the elementary bound is also2||X||. No use of ||R|| is necessary in the first bound. The exact computable residual quadratic form is X*e^(isA)(R*R)e^(-isA)X: its largest eigenvalue gives operator norm squared and its trace gives Hilbert–Schmidt norm squared.

For t>0 the Poisson spectral identity e^(-t|H|)=integral_R [t/(pi(t²+u²))]e^(-iuH)du yields, for any S>0,

 ||e^(-t|H|)VX − V e^(-t|A|)X||
 <= (t/pi) integral_0^S [integral_0^u (r_X^+(s)+r_X^-(s)) ds]/(t²+u²) du
    +(4/pi)||X|| atan(t/S).

The integrable tail uses2||X|| at both signs; normalization of the Poisson kernel proves the stated coefficient. At t=0 the error is exactly zero. If rho bounds both r_X^± on[0,S], the first term reduces to (t rho/pi) log(1+(S/t)²), recovering the old uniform estimate only upon setting rho=||R|| ||X||. Pointwise weighted residuals can be much smaller. One may also use min(2||X||,integral_0^u r_X^±) inside the integral. All such improvements require an actual certificate; an instantaneous residual alone is insufficient because the reduced evolution may rotate into leaking directions.

In a nonorthogonal frame S0 with G=S0*S0>0 and skew-adjoint K=-iH (or the consistently chosen opposite sign), J=S0*KS0, D=(KS0)*(KS0), B=G^-1J and L=D+J G^-1J, the exact residual of the reduced real evolution is

 ||(1-P)K S0 exp(sB)c||² = c* exp(sB*) L exp(sB)c,
 P=S0 G^-1 S0*.

B is G-skew, B*G+GB=0; exp(sB) preserves the G norm. This expression is equivalent to the orthonormal theorem and does not require a narrow entrywise factor C. It still needs certified inverse/finite evolution errors. It preserves the original physical input frame and squared uniform leakage result; only the downstream sufficient condition changes to an explicitly named input X or c.

A complementary exact resolvent identity is available for Im(z)≠0:

 (H-z)^-1 VX − V(A-z)^-1 X
 = -(H-z)^-1 R(A-z)^-1 X,

hence the error is <= ||R(A-z)^-1 X||/|Im(z)|. The sign follows (H-z)V=V(A-z)+R. This may directly fit the existing rational source bank; the complex resolvent source and any transformation to |H| must be spelled out rather than inferred from a similarity of formulas.

Required next proof work: identify finite inputs that suffice for the actual Ward/Gaussian observable, include their initial projection errors, and find a finite certified bound on the weighted residual over the required times/frequencies. No claim that arbitrary many-body Gaussian states are determined by these finite vectors, or that a small initial-vector propagation error controls an unbounded determinant dimension. The trace-weighted covariance route is a separate candidate needing an explicit trace-class factorization.
