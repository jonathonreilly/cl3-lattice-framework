# Analytic negative Perron correction certificate

This proof was found after the separately frozen Nyström diagnostic runs. Those floating values motivated continued analysis but supply NO inequality or premise below. The numerical meshes/domain are unchanged and their raw outputs remain preserved. All constants in this certificate follow from explicit trial-function identities, a positive-operator trace bound and elementary scalar inequalities.

## Objects and exact reduction

On the Dirichlet chamber C=(0,infinity)², let L=(partialxx-partialxy+partialyy)/3, S=exp(L/2), W=H exp(-Q), H=xy(x+y)/2 and Q=x²+xy+y². Put T0=S M_W S and let its normalized Perron eigenvector be phi0 with eigenvalue mu0>0. Define B=M_sqrtW exp(L) M_sqrtW. The normalized Perron vector of B is u=sqrt(W)Sphi0/sqrt(mu0), since T0=A* A and B=A A* for A=M_sqrtW S. Therefore
 r:=d0/mu0=integral_C R(Q)|u|²,
 R(q)=q(q-7)/4.
This is the SAME normalization as the previously derived Wilson insertion, not a physical group-convolution eigenvalue.

## Positive-operator bound, not a trial-state sign inference

B is positive trace class, hence B>=mu0 |u><u|. Let g(q)=(R(q)+1)_+. Since R<=-1+g,
 r<=-1+integral_C g(Q)|u|².
For bounded truncations of g, multiply the operator inequality by its square root and take traces; then use monotone convergence. The weighted heat-kernel trace is finite by the Gaussian envelope below. Consequently
 r<=-1+J/mu0,
 J:=Tr(M_sqrtg B M_sqrtg)=integral_C g(Q)W(x)s_1^C(x,x)dx. (1)
This controls the ACTUAL Perron distribution; a trial function will be used only to lower-bound mu0, never substituted for u.

## Exact radial integrals

In metric-polar coordinates Q=rho², the chamber is an angle-pi/3 wedge, dxdy=(2/sqrt3)rho d rho d theta, and H=rho³ sin(3theta)/(3sqrt3), with theta measured from a wall. Direct integration gives
 integral_C H f(Q)dxdy=(2/27) integral_0^infinity q^(3/2)f(q)dq,
 integral_C H exp(-aQ)dxdy=sqrt(pi)/(18 a^(5/2)),
 integral_C H² exp(-aQ)dxdy=pi/(27sqrt3 a^4). (2)
The full-plane time-one heat diagonal is sqrt3/(2pi). Killing only reduces it, so from (1) and (2),
 J<=[sqrt3/(27pi)] integral_0^infinity g(q)q^(3/2)e^-q dq. (3)
The chamber angular factor is retained; replacing it by a plane integral would lose this useful bound.

## Scalar tail certificate

For all q>=0,
 g(q)<= (1-3q/2)_+ + [q(q-6)/4] 1_(q>=6). (4)
For0<=q<=2/3, R+1<=1-3q/2 because q<=1. On[2/3,6], the convex polynomial R+1 is negative at both endpoints and hence throughout. For q>=6, R+1<=q(q-6)/4 because q>=4. This proves (4) without locating irrational roots.

The low integral obeys
 integral_0^(2/3) q^(3/2)(1-3q/2)e^-q dq
 <=(4/35)(2/3)^(5/2)<1/24.
The last comparison is exact after squaring:294912<297675.

For the high integral, substitute q=6+s and use concavity
 sqrt(6+s)<=sqrt6(1+s/12).
Then
 (1/4) integral_6^infinity q^(5/2)(q-6)e^-q dq
 <=(sqrt6 e^-6/4) integral_0^infinity s(6+s)²(1+s/12)e^-s ds
 =20sqrt6 e^-6<1/8.
The polynomial moment is exactly80. The strict last inequality uses sqrt6<5/2 and e^6>400; the latter is certified by a finite positive Taylor sum, with no fitted exponential approximation.

Thus the integral in (3) is below1/6. Since sqrt3<7/4 and pi>3,
 J<7/1944. (5)

## Rigorous Perron eigenvalue lower bound

Take the legitimate Rayleigh trial v=sqrt(W)/||sqrt(W)||. The Dirichlet heat equation has the exact solution
 exp(tL)[H exp(-Q)]=(1+t)^-4 H exp[-Q/(1+t)]. (6)
This follows by direct differentiation, LH=0 and homogeneity3; H vanishes on both chamber walls, so the displayed solution has the required Dirichlet boundary data. It can equivalently be obtained by odd Weyl extension and full-plane Gaussian heat evolution. No eigenfunction ansatz is made.

Using (2) at t=1 in (6),
 mu0>=<v,Bv>
 =[integral W exp(L)W]/[integral W]
 =2sqrt(pi)/(243sqrt3)>2/243, (7)
where only pi>3 is used for the strict final bound.

Combining (1), (5) and (7) gives the exact sign certificate
 r< -1+(7/1944)/(2/243)=-9/16<0. (8)
Also R(q)>=-49/16, and equality occurs only on the measure-zero ellipse Q=7/2, so normalization in L² gives
 -49/16 < d0/mu0 < -9/16.
In particular d0< -1/216 follows from (7) and (8). These are deliberately conservative analytic bounds. The precise value is not certified by this argument.

## Consequence and limits

The already derived top-to-top asymptotic comparison against the EXACT beta-dependent sampled shifted saddle has a negative coefficient d0/mu0. Hence the native normalized top eigenvalue is eventually smaller than that saddle top eigenvalue, provided the previously proved operator-difference/Perron-limit hypotheses are used. This proof gives no explicit finite-beta onset for that eventual comparison, no full fixed-heat expansion, no excited-eigenvalue or ground/excited log-ratio sign, and no physical mass-gap conclusion.

Frozen floating diagnostics gave r approximately-2.59269814, consistent with (8), but this number is NOT a certified value. The analytic certificate does not use any Nyström eigenvalue, eigenvector, fitted cutoff, spectral gap estimate or grid agreement.
