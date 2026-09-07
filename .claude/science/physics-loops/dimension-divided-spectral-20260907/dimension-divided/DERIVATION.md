# Global wall-uniform dimension-divided Wilson expansion

The elementary divided-alternant route succeeds. Conditional on the exact parent SU(3) recurrence/reflection/Fourier identity, for EVERY real beta>=2048 and EVERY p=(p1,p2) in N0², set x=(p+rho)/sqrtbeta,rho=(1,1). Then

    |c_p/(d_p c0)-exp(-Q(x))[1+P2(Q(x))/beta]| <1710/beta²,
    P2(q)=3-7q/4+q²/4, d_p=H(p+rho).

The constant is conservative and chosen by analytic rational ceilings, not a fitted multiplier. This includes wall/origin-scaled labels. It is not obtained by dividing the old29/beta² error by H.

## An elementary divided alternant bound

Let A_x(z)=sum_(w inWeyl)det(w)exp[-iz·wx]. As a function F(x,y)=A_(x,y)(z), it vanishes on x=0,y=0 and x+y=0, the fixed lines of the three reflections. It is smooth on the whole real plane. Twice applying the fundamental theorem of calculus gives

    F(x,y)=xy B(x,y),
    B(x,y)=integral_0^1 integral_0^1 F_xy(tx,sy)dt ds.

On y=-x, B(x,-x)=0 for x!=0 and also at0 by continuity. Therefore

    B(x,y)=(x+y)integral_0^1 B_y(x,-x+u(x+y))du,
    |B_y|<=[integral_0^1 integral_0^1 s dt ds] sup|F_xyy|
           =(1/2)sup|F_xyy|.

For x,y>0 this proves |A_x(z)|<=H(x) sup|F_xyy|, H=xy(x+y)/2. No group integral or assumed positivity formula is used.

Write a(z)=z1²-z1z2+z2². Each dual Weyl transform alpha=w^Tz preserves a and obeys alpha_i²<=4a/3. Differentiating each of the six phases gives magnitude |alpha1 alpha2²|. Hence

    |A_x(z)|/H(x) <=6(4a/3)^(3/2)
                    =(16/sqrt3)a^(3/2)<10a^(3/2).       (1)

This bound is uniform in the entire positive endpoint chamber, including its limiting walls, and in all real z. It is deliberately looser than possible sharp alternant bounds but suffices.

## Exact averaging, including the torus issue

Use parent scaled integrals N_beta,D_beta, with N/D=beta^-3/2 c_p/c0, Delta=(2z1-z2)(z1-2z2)(z1+z2), and B_beta the three sinc factors. The exact numerator integrand contains exp(-iz·x)iDelta B_beta. Average it over the six dual Weyl transformations to obtain

    N_beta/H(x)=[6(2pi)²]^-1 integral_Tbeta
      exp[-beta psi(z/sqrtbeta)] iDelta(z)B_beta(z)
      [A_x(z)/H(x)] dz.                              (2)

This averaging is legitimate for the ACTUAL shifted labels: x=(p+rho)/sqrtbeta makes every phase periodic on the scaled Fourier torus. The dual Weyl maps are integral torus automorphisms. The product iDelta B_beta is the scaled exact alternant, so it transforms with the required sign. An arbitrary real endpoint extension need not be periodic and is not asserted to satisfy(2).

The low ellipse a<=beta/2 is preserved by the dual Weyl group and lies strictly inside the chosen square: each z_i²<=2beta/3<pi²beta. Its images therefore do not wrap. Both its exact integral and its torus complement can be averaged. The Gaussian comparison integrals over R² can be averaged directly by linear changes of variables. This justifies using(1) for the low remainders AND both exact/Gaussian tails; no nonperiodic remainder is silently moved around a torus.

As x=epsilon rho, A_x=-i epsilon³ Delta+O(epsilon5), while H(x)=epsilon³. Thus the small-endpoint divided numerator integrand in(2) tends to Delta²/6, exactly matching the denominator's leading normalization. The certificate verifies this sign and factor from the six actual matrices.

## Explicit divided numerator remainder

The already reviewed low factor remainder on a<=beta/2 is

    beta^-2 exp[-alpha a] PN(a),
    alpha=23/72,
    PN=a²/20+(23/2592)a³+a4/2592.

It is the error after expanding the exact exponential times B_beta to first order. Here the endpoint is already averaged, so multiplication by(1) preserves a factor H instead of losing it. Since |Delta|<=3a^(3/2), (1) and the1/6 average give |Delta A_x/H|/6<=5a³. The radial Fourier prefactor is1/(2pi sqrt3)<1/10. Consequently the low divided-numerator error constant is bounded by

    CN_low=(1/2)[(1/20)5!alpha^-6
             +(23/2592)6!alpha^-7+(1/2592)7!alpha^-8]
           =1660205766279168/78310985281 <21201.

The exact high tail uses exp(-a/24), and a>=beta/2. Multiplying by beta² bounds it by

    (beta²/2)24^4 3!exp(-t)(1+t+t²/2+t³/6), t=beta/48.

Its terms decrease for beta>=2048. The positive exponential-series certificate exp(128/3)>10^18 bounds its endpoint coefficient by less than3/50. For the Gaussian approximation tail, beta<=2a gives

    (1/2)integral_1024∞[(9/2)a5+a6/18]exp(-a/3)da.

Splitting the exponential and using exp(512/3)>10^60 bounds it by less than1/1000. Exact rational addition of the actual low value and both tail bounds gives a TOTAL constant below21201; the separate low inequality alone is not used to absorb tails without checking their margin.

The Gaussian transforms retain the previously proved coefficient, so with E=exp(-Q),

    |N_beta/H-D0[E+(P2-1)E/beta]|<=21201/beta².       (3)

D0=27sqrt3/pi. This proof does not replace the native numerator by a Gaussian or divide a previously endpoint-independent error by a vanishing H.

## Denominator and final ratio

The same reviewed denominator estimate remains

    |D_beta-D0(1-1/beta)|<=2618/beta²,
    D_beta/D0>999/1000, D0>14, beta>=2048.

Globally E<=1. The elementary maxima q exp(-q)<=1/e and q²exp(-q)<=4/e², together with e>8/3, give

    |P2 E|<=3+7/(4e)+1/e² <243/64<4.

Subtracting D_beta[E+P2E/beta] from (3)'s expansion produces exactly rN+D0P2E/beta²-rD[E+P2E/beta]. Hence its ratio error coefficient is at most

    (1000/999)[21201/14+4+(2618/14)(1+4/2048)]<1710.

Finally d_p=beta^(3/2)H(x), so (N/H)/D is exactly c_p/(d_p c0). This proves the announced global shifted-label bound.

## Scope and preserved failed route

Directly dividing the old absolute29/beta² estimate by H would give as weak as29/sqrtbeta at p=0. That route is not used. The new load-bearing ingredient is the elementary three-wall divided-alternant estimate plus correct torus averaging at integral shifted labels.

The physical normalization c_p/(d_p c0) is the supplied one-link central convolution normalization already established by Schur orthogonality. This result is a uniform conditional one-link multiplier theorem, not a new derivation of that normalization. It neither identifies a spatial multi-link compression with a diagonal character convolution nor transfers the native H-weighted Perron corrections to that different operator. Haar/Wilson action typing, multilink environment, continuum and physical gap obligations remain separate.
