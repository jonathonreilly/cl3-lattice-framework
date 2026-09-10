# Degree-(1,1): a six-vector Wick closure with one new scalar moment

SOURCE ONLY, unreviewed. No native scalar, moment, covariance, catalog or history was read/evaluated. This is a prospective successor to the independently reviewed degree-(1,0) proof28b1; existing protocols and source files remain unchanged. Work in h=1. The only new scalar proposed below is omega5=<e0,|h0|^5 e0>=E X^(5/2), not presently supplied by this derivation.

## Six vectors suffice for each source residual

For one pair set a=e0, d=d_A, k=K a, v=K d, z=K² a, w=K² d. Write the first polynomial p(D)=u+p1 D, and V=4p1. Its inner source is b=u J Omega+V g Omega. Using D O Omega=([H0,O]+B O)Omega gives

 b=(2iu gamma(d)+V gamma(a))Omega,
 Db=[u(-2gamma(v)-4gamma(a))+iV(gamma(k)-gamma(d))]Omega,
 D²b={iu[-2gamma(w)-2gamma(a)gamma(d)gamma(v)-4gamma(k)+4gamma(d)]
       +V[-gamma(z)-gamma(a)gamma(d)gamma(k)+gamma(v)+2gamma(a)]}Omega. (1)

Products in(1) have the displayed order and are NOT exterior products; contractions from nonorthogonal vectors remain. In particular B gamma(v) is cubic in general. Equation(1) follows directly from B=i gamma(a)gamma(d), ||d||²=2 and [H0,gamma(f)]=i gamma(Kf).

Thus the source moments sj=<b,D^j b>, j=0..4 are obtained from

 s0=<b,b>, s1=<b,Db>, s2=<Db,Db>, s3=<Db,D²b>, s4=<D²b,D²b>.     (2)

Wick words have length at most6. There is no unbounded Fock-space matrix in this computation.

## Explicit dot/covariance table

White vectors are(a,v,z); black vectors are(d,k,w). Their real dot Gram matrices are

 white: [[1,-2,-6],[-2,L2,14],[-6,14,42]],
 black: [[2,2,-L2],[2,6,-14],[-L2,-14,L4]],

where L2=12(P),14(O), L4=84(P),108(O). Cross-color dot products vanish. The integer324=EX³ gives108=EX³/3; it is an exact walk/dispersion identity, not a measured moment. Same-color antisymmetric covariance vanishes. With <gamma(x)gamma(y)>=x·y+i kappa(x,y), the white-to-black kappa table is

              d          k          w
 a           -c         -3c         nu/3
 v           ed          nu/3      -ed3
 z            nu/3       nu        -omega5/3

where ed=6c(P),nu/3(O), ed3=2nu(P),omega5/3(O). Reverse entries change sign. This uses kappa=K/|h0| and the native center/pair spectral measures. For example kappa(v,w)=-<d,|h0|³d>, while kappa(z,w)=a^T K|h0|³d=-omega5/3. The signs must not be inferred merely from positive scalar moments.

All entries therefore reduce to c,nu,omega5 and integer even moments. Pfaffian expansion of at most six fields in(2) closes these moments on that scalar family. This table is a proposed source identity requiring independent review; it is not a completed scalar certificate.

## Fixed second polynomial and residual

A residual-optimal second polynomial q(D)=q0+q1D solves

 [[s2,s3],[s3,s4]] q=[s1,s2],

provided positivity and nonsingularity are certified. Any chosen rational q remains valid after enclosing

 t²=s0-2q0 s1-2q1 s2+q0²s2+2q0q1s3+q1²s4.                    (3)

The same rigorous full-Ward error e858 applies, with unchanged first-polynomial residual r. Coefficient optimizer accuracy is not a physical premise. In particular an interval matrix can select a rational candidate and the original residual can certify it afterward. No midpoint isometry is claimed.

## Signed five-orbit nominal

For disjoint A,C let e_CA=<d_C,|h0|d_A>. The signed nearest-neighbor vectors have nonzero |h0| cross entries only when they are opposite neighbors on the same axis: |h0| preserves each coordinate parity, since K² is the sum of two-step translations. Consequently

 e_CA=ell*(nu/6-3c),

where ell is the number of opposite neighbor pairs split across C,A. It is0 for OO,OP,PO;1 or2 for the two PP orbits. Let u_A=p0A, v_A=p1A, V_A=4v_A. (Here v_A is a coefficient, NOT the earlier vector Kd.) The degree-(1,0) nominal per ordered edge, with q0 replacing q, is

 uC uA+c(uC vA+vC uA)
 +q0A[2c uC uA+4uC vA+4c vC vA].

The new q1 contribution is exactly

 q1A[2c V_A uC+vC(2uA e_CA-4uA c+2V_A)].                     (4)

To verify(4), multiply (uC+vC BC) g Db_A, retaining the overall sign from xhat=-(u+p1B). Use <g gamma(Kd_A)>=-2, <BC g gamma(Kd_A)>=-e_CA, and <d_C,k-d_A>=2. These are original-vacuum brackets. Summing over the fixed90 ordered edges gives the nominal in the same full-alpha error gate; no negative channel or boundary is deleted.

## Source cost, scope and next gate

A direct literal Wick evaluator of(2) uses at most a few dozen pairs of terms and at most15 matchings per six-field word. Two classes, two fixed first-polynomial choices, and a2x2 second solve give a small scalar arithmetic certificate, once omega5 and all interval errors are supplied. There is no need at this degree for a new spatial covariance matrix. This is an algebraic operation count, not an executed native profile or a promise that the error bound will decide the sign.

A possible NEW omega5 supplier uses the existing A(t) oracle family but requires its own proof/contract:

 omega5=(2/pi) integral_0^infinity [42-6t²+t^4-t^6 A(t)] dt
       =(2/pi) integral E[X³/(X+t²)] dt.

This is positive pointwise in its spectral representation. On the reviewed rho5 ellipse its analytic envelope is(5/4)EX²=105/2; the whole Gauss ledger must still be carried through. Forty high-tail terms use moments M3..M42 and a positive remainder bounded by M43/(81 T^81); the low polynomial is42epsilon-2epsilon³+epsilon^5/5 with subtraction integral t^6 A(t), bounded using A0. Input radii are amplified by t^6 rather than t^4: old nu precision cannot simply be copied. No required omega5 precision is asserted before examining the actual degree10 outcome and a conditional sensitivity ledger. No integral or old protocol has been run here.
