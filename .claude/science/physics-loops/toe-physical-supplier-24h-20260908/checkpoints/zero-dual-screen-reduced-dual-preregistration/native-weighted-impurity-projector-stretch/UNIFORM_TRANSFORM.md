# Shared-catalog uniform transform envelope

Set h=1. This sharpens the previous transform envelope; it does not evaluate new physical inputs. Use the reviewed A0<=17/60 and Cminus=E X^-1/2<7/15. The folded uniform theta convention is X=6-2 sum cos(theta_a), theta in[-pi,pi]^3, so X>=4|theta|²/pi².

For s>0,

    -A'(s)=2s E (X+s²)^-2
      <= [2s/(2pi)^3](pi/2)^3 integral_R3 (|p|²+s²)^-2 dp
      =pi²/32 <1/3.

The integral is pi²/s; enlarging the rescaled cube is allowed because the integrand is positive. The bound also controls the one-sided limit at zero. Separately A(s)<=17/60<1/3. Set E0(s)=2s E[X/(X+s²)^2]. Maximizing 2y/(1+y²)^2 gives9/(8sqrt(3)), hence E0<=9 Cminus/(8sqrt(3))<63/200<1/3. Also C0(s)=1-s²A(s)<=1.

For the B transform functions G_s(z)=E[X/((X+s²)(X+z²))] and H_s(z)=2s E[X/((X+s²)^2(X+z²))], on |z-c|<=c/2 the earlier factored-denominator estimate gives |X+z²|>=(X+c²)/4. The sharper near-zero estimate used by the reviewed transform proof is |G_s(z)|<=A(s), |H_s(z)|<=-A'(s) on its Bernstein ellipse (not on the entire disk if that estimate is unavailable). More directly on the actual Gauss Bernstein ellipse of parameter5/2 mapped to[a,2a], Re(z²)>0: its real semiaxis0.725a, imaginary semiaxis0.525a, center1.5a; minimizing x²-y² on the ellipse gives a positive minimum. Therefore |X+z²|>=X there, proving both near-zero bounds. The disk bound supplies the far bound. Thus on that ellipse

    M(c)=min(1/3,4/c²), c=3a/2.

For dyadic a, sum a M(3a/2)<= (1/3)sum_(a<=2)a + (16/9)sum_(a>=4)1/a =4/3+8/9=20/9.

The same reviewed Gauss estimate consequently gives total middle error <=(400/27)(4/25)^p before the factor2/pi. The omitted low interval[0,epsilon] contributes <=epsilon/3 for either function. With m tail moments and T large, the G high-tail remainder is <=12^m/((2m+1)T^(2m+1)), and H is <=one third of this, using E0<=1/3. These bounds are uniform in s and remove the old 1/s loss. They do not eliminate oracle endpoint errors or division conditioning near catalog nodes. Disjoint root brackets are a required implementation gate.

Scope: this proves a useful common analytic envelope, not adequacy of the accepted catalog's precision for the actual weighted matrix. No oracle or integral was called.
