# Reference scalar and log-anchor for an actual two-link defect

Prospective, unexecuted physical integration design. Supplied infinite canonical pi-flux reference, h=2|t_hop|. This is not an alpha calculation.

## Relative vacuum scalar

Use parent8067's relative Hamiltonian D_A=H_A-E0, with K0=[[0,B0],[-B0^T,0]], B0=U0 S and B_A=B0-2e0 b_A^T. Align the black Majoranas with U0 and set f=(a+ib)/2. Then the normally ordered reference operator is

 D_A=c_A+f† H f+(f† K f†+f K^T f)/2,
 H=(D+D^T)/2, K=-(D-D^T)/2, D=S-2u b_A^T, u=U0^T e0.

The finite relative constant is c_A=-Tr(D-S)/2=u^T b_A. No divergent extensive trace is subtracted numerically. Each of the six signed incident edge contributions to e0^T B0 U0^T e0=mu has the same expectation by the physical signed cubic symmetries. Hence two selected links give c_A=mu/3 for both perpendicular and opposite classes, where mu=<e0,|iK0|e0>=h E sqrt(X), X=6-2sum cos(theta), 0<=X<=12. This scalar is the REFERENCE expectation, not the impurity ground energy shift c from the diagonalized parent theorem.

## Log-anchor sign

Write exp(-t D_A)Omega0=exp(ell(t)) exp(f† Z(t) f†/2)Omega0, Z real skew, ell(0)=0. The bounded-chart construction supplies implementability; finite-rank K makes all traces below defined. Since <0|fi fj|Z>=-Zij, the scalar coefficient of the annihilation term is (1/2)Tr(K^T Z). Therefore

 ell'=-c_A-(1/2)Tr(K^T Z)=-c_A+(1/2)Tr(K Z).

Together with Z'=-K-HZ-ZH-ZKZ this is the actual unnormalized anchor equation. For K=kJ,Z=zJ, the even two-mode block has offdiagonal k and ell'=-c_A-kz. Initially ell'=-c_A and ell''=(1/2)Tr(K^T K)>=0, matching the vacuum variance. Normalized-state anchor instead subtracts log||psi||, equivalently one half log||psi||²; do not confuse the two.

## New integral using only accepted catalogue entries

In h1 units mu=(2/pi)int_0^infty Q(s)ds, Q(s)=E[X/(X+s²)]=1-s² A(s), by positive Tonelli. This is a NEW physical integral even though it uses no new scalar oracle.

Reuse exactly the accepted76350 Gauss12 rule, 31 dyadic panels j=-28..2, and its744 A endpoint records (exclude the two fixed-pole entries except for catalogue validation). At a node bracket [l,u], monotonicity gives A bracket [A(u).lo,A(l).hi]. Ordinary interval evaluation of 1-[l,u]^2 A contains the node value, including lost dependence.

Low tail [0,epsilon], epsilon=2^-28, because 0<=Q<=1. On |z-c|<=c/2, |X+z²|>=X and >=c²/4, so |Q(z)|<=min(1,24/c²), using EX=6. For the actual panels c=3a/2: sum a M(c)<=sum_{j=-28}^1 2^j+8/3<20/3. The previously proved Gauss/Chebyshev bound is (20/3) sum aM (4/25)^12, hence absolute middle radius R=(400/9)(4/25)^12. Add R on both sides before multiplying by 2/pi.

For T=8, expand16 terms:
 int_T^infinity Q=sum_{n=0}^{15} (-1)^n M_(n+1)/[(2n+1)T^(2n+1)]+r,
 0<=r<=12^17/(33 T^33).

Here M_n=EX^n=sum_{a+b+c=n} n!/(a!b!c!) comb(2a,a)comb(2b,b)comb(2c,c), since X=4sum sin²k. The even16 remainder is positive. The analytic final WIDTH is bounded by (2/3)[epsilon+2R+12^17/(33*8^33)]<1e-6. Actual success must include all input/weight/interval/pi widths and require final width<=1e-6; no assumed success.

Pi is enclosed independently by Machin pi=16atan(1/5)-4atan(1/239), using48 alternating terms and the next-term remainder. Fixed192-bit outward Fraction arithmetic prevents uncontrolled rational denominator growth. All saved input and partial output hashes must be retained.

## Contract still required before launch

Proposed one catalogue-only attempt: external30s/384MiB, internal29s, no retry, no oracle or physical matrix. Root must independently review source/proof, provide a source-bound authorization and external whole-tree monitor, and archive the final runtime contract before execution. Current worker source is a design candidate, not runtime-ready authorization. All31 panel partials and any final interval must be preserved before gate checks. No precision/node/target changes after data.
