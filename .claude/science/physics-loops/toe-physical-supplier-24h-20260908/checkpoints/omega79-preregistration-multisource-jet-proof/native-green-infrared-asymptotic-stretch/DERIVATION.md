# Direct native Green infrared asymptotics with explicit remainders

New analytical derivation, independent of an elliptic Green formula. No physical integral or series evaluation. Let expectation be normalized Lebesgue measure on one theta-torus[-pi,pi]^3, X=6-2 sum cos(theta_a), and, for s>0,

 A(s)=E[1/(X+s²)], B(s)=E[sqrt(X)/(X+s²)].

Define A0=E[1/X] and B0=E[1/sqrt(X)]; both are finite. All bounds below are for0<s<=1, in h=1 units.

## Exact coordinate reduction and multiplicity

Set x_a=2sin(theta_a/2). This is one-to-one in the interior of the chosen cube, X=|x|², and normalized measure becomes

 f(x) dx=(2pi)^-3 product_a(1-x_a²/4)^-1/2 dx, x in[-2,2]^3.

Boundary singularities are integrable, with total mass1. There is exactly one conical zero in this theta-torus. The original dispersion4sum sin²k has eight zeros in a2pi k-torus, but theta=2k is an eightfold covering with the compensating normalized Jacobian. It produces precisely this one-torus expectation, not an extra factor8.

Put f0=(2pi)^-3 and r=|x|. On r<=1,

 0<=f(x)-f0<=c f0 r², c=1/6.

Indeed product(1-x_a²/4)>=1-r²/4, and convexity on[0,1] gives(1-r²/4)^-1/2<=1+(2/sqrt3-1)r². The coefficient is <=1/6, since48<=49. Thus the following elementary estimates include all lattice corrections. On r>=1, each needed inverse-power kernel is bounded by1 and its f-integral by the total probability1. These statements also prove finiteness of A0,B0; at zero the radial integrands are respectively constant and proportional to r.

## A and its right derivative

The exact positive difference is

 A0-A(s)=s² integral f(x)/[r²(r²+s²)] dx.

The constant-density unit-ball contribution is

 4pi f0 s arctan(1/s)=s/(4pi)-s arctan(s)/(2pi²).

The ball correction is between0 and c s²/(2pi²), and the exterior contribution between0 and s². Consequently

 -[1+1/(12pi²)]s² <= A(s)-A0+s/(4pi) <= s²/(2pi²).       (A)

This proves A(s)=A0-s/(4pi)+O(s²), with explicit one-sided remainders. In particular the even extension in s has a cusp, not a regular even Taylor series at0.

Differentiation under the integral is justified for each positive s by a locally uniform positive denominator. The constant-density contribution to -A'(s) is

 [arctan(1/s)-s/(1+s²)]/(2pi²)
 =1/(4pi)-[arctan(s)+s/(1+s²)]/(2pi²).

The density correction is at most c s/pi², using r^4/(r²+s²)^2<=1; the exterior contribution is at most2s. Hence

 |A'(s)+1/(4pi)| <= [2+7/(6pi²)]s.                    (A')

The derivative limit follows directly, not by differentiating an unspecified O(s²) remainder. In particular A'(0+)=-1/(4pi).

## B and its derivative

The exact difference is

 B0-B(s)=s² integral f(x)/[r(r²+s²)] dx.

Its constant-density unit-ball term is

 s²/(2pi²) log(1/s)+s²/(4pi²) log(1+s²).

The extra density contributes at most c s²/(4pi²), since integral_0^1 r³/(r²+s²) dr<=1/2. The exterior contribution is at most s². The logarithmic correction is nonnegative and <=s^4/(4pi²). Therefore

 0 <= B0-B(s)-s²/(2pi²)log(1/s)
   <= [1+7/(24pi²)]s².                              (B)

Thus the stated nonanalytic coefficient is positive in B0-B, or negative in B-B0.

Direct differentiation gives -B'(s)=2s integral f(x)r/(r²+s²)^2 dx. The constant-density unit-ball term is

 s/pi² log(1/s)+s/(2pi²)[log(1+s²)+s²/(1+s²)-1].

For0<s<=1 the bracket lies between-1 and log2-1/2, hence has absolute value<=1. The density correction is at most c s/(2pi²), using integral_0^1 r^5/(r²+s²)^2 dr<=1/2. The exterior contribution is at most2s. It follows that

 |B'(s)+s/pi² log(1/s)| <= [2+7/(12pi²)]s.            (B')

Again this is a direct derivative estimate. B'(0+)=0, while the logarithmic term prevents treating the second derivative as uniformly bounded near0.

## Dimensions and use in future certificates

For actual X_h=h²X, A_h(s)=h^-2 A(s/h) and B_h(s)=h^-1 B(s/h). Thus

 A_h(s)=h^-2 A0-s/(4pi h³)+O(s²/h⁴),
 A_h'(s)=-1/(4pi h³)+O(s/h⁴),
 B_h(s)=h^-1 B0-s²/(2pi²h³)log(h/s)+O(s²/h³),
 B_h'(s)=-s/(pi²h³)log(h/s)+O(s/h³),

for0<s<=h, with exactly the constants in(A)–(B') after scaling. The additive dimensions of B_h and its remainder agree; its O(s²/h³) term is not O(s²/h⁴).

These give direct independent normalization/limit checks for a future elliptic evaluator and rigorous near-zero scalar enclosures conditional on certified A0/B0 intervals. In particular(A') encloses A' without knowing A0. They do not evaluate A0 or B0 and do not provide high relative precision for small differences by themselves. The constants are deliberately elementary; their coarse exterior bound can dominate at moderate s. No numerical cost, Gram conditioning, projector precision or alpha follows from this lemma alone.
