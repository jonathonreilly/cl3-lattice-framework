# Full Ward channel identity and a positive native direct term

Source-only analytical result. No actual Gaussian kernels, moments, spectra, accepted scalar values or orbit data evaluated. Keep the original vacuum and every Ward boundary source. The full alpha remains undetermined.

## Three exact channels for the complete scalar

Index the15 pairs by two-subsets A of six star legs. Let T_CA=1 when A,C are disjoint. In the Hilbert direct sum of15 copies of the original GNS space define

 x_A=R_A Omega,
 v_A=R_A J_A R_A Omega=(R_A W_A-W_A R_A)Omega,
 p_A=gamma0 v_A.

Here R_A=-D_A^-1 is Hermitian, J_A is anti-Hermitian, W_A is Hermitian, [W_A,D_A]=-J_A and {W_A,gamma0}=4. These are the bounded identities already proved from the actual native inverse source. In particular (R_A J_A R_A)*=-R_A J_A R_A. Substituting into the complete reviewed soft formula gives

 8 alpha=<x,T x>-Re<x,T p>.                                      (1)

The first correction in that formula is minus the conjugate of the second after A,C reversal. This sign is essential. No claim that W_A Omega vanishes occurs.

Let B_Ai=1_(i in A)-1/3. Then B*B=4I-(2/3)11*, and the orthogonal pair-space projections are E0=11*/15, E1=BB*/4, E2=I-E0-E1. Direct counting gives T=6E0-3E1+E2, with ranks1,5,9. Put y=x-p/2. Equation(1) becomes

 8 alpha=sum_l lambda_l (||E_l y||²-||E_l p||²/4), lambda=(6,-3,1). (2)

Thus six nonnegative norm quantities give an exact real scalar certificate. For example a rigorous lower bound is6L_y0+L_y2+(3/4)L_p1-3U_y1-(3/2)U_p0-(1/4)U_p2. This is a sufficient sign criterion only; none of its six actual quantities has been computed here. Squared-norm positivity alone does not settle their signed combination.

Cubic covariance implies that scalar vacuum components <Omega,x_A> and <Omega,p_A> depend only on whether A is opposite or perpendicular. Each leg belongs to one opposite and four perpendicular pairs. Consequently E1 annihilates these scalar components. It does NOT annihilate E1x or E1p as Hilbert-valued vectors: their negative channel may contain reference excitations.

## A strictly positive direct90-pair overlap, without scalar acquisition

Use h=1 and the independently proved infinite pair gap D_A>=1/4. Write D_A=H0+B_A with H0 Omega=0. The actual rank-two pair perturbation is B_A=i gamma0 gamma(d_A), where ||d_A||²=2 and d_A is orthogonal to the center. Hence B_A²=2I. Its reference expectation is c=<B_A>=mu/3 for both classes. The scalar law mu=E sqrt(X), EX=6 gives c<=sqrt(6)/3<49/60. Positivity also gives c>=1/4.

The bounded one-particle free generator has norm<=6. A quadratic local B_A applied to its Gaussian vacuum has only vacuum and two-particle components, whose free energies lie in[0,12]. Therefore B_A Omega is in Dom(H0^n) for every fixed n and

 <D_A>=c, <D_A²>=2,
 <D_A³>=<B_A Omega,H0 B_A Omega>+2c<=24+2c<26.                  (3)

The stronger vacuum-subtracted bound12(2-c²)+2c is available but unnecessary. These are spectral-support arguments, not evaluated native moments. B_A bounded and the finite-particle energy support justify all displayed domains; no finite-volume gap is assumed.

Let m_A=<D_A^-1>. Cauchy applied to D_A^-1/2 Omega and D_A^1/2(a+bD_A)Omega gives, for every real a,b,

 m_A >= (a+bc)²/(c a²+4ab+<D_A³>b²).

Replacing the third moment by26 enlarges the positive denominator. The2x2 matrix [[c,2],[2,26]] is positive definite for c>=1/4. Optimizing this two-dimensional quadratic form yields

 m_A >= f(c)=(26-4c+c³)/(26c-4).

The derivative numerator is52c³-12c²-660<0 on[1/4,49/60], so

 m_A>=m0=5028049/3722400>4/3.                                 (4)

This bound is for the actual reference inverse expectation, not the impurity ground energy. It imports no observed scalar values.

For completeness the direct overlap positivity does not require the stronger cubic annihilation fact above. Put u_A=D_A^-1 Omega and split u_A=m_A Omega+u_A^perp. Since T>=-3I and D_A^-2<=4D_A^-1,

 Q=sum_disjoint<R_C R_A>
   >=m* T m-3 sum_A(||u_A||²-m_A²)
   >=m*(T+3I)m-12 sum_A m_A.

Write m=m0 1+t, t_A>=0. T+3I is positive semidefinite with row sum9. The remaining terms are (18m0-12)sum t+t*(T+3I)t>=0. Thus

 Q>=135m0²-180m0=326063949601/102638976000>3.                   (5)

Restoring units gives Q>3/h². This is a native quantitative positivity theorem for the direct term only. The full Ward correction in(1) is not removed, and the available tail norm bounds are too coarse to place its negative part below3/h². In particular (5) does not prove alpha nonzero or positive.

## Matching identity for the next attempt

The90 ordered disjoint pairs partition into15 perfect matchings, each containing three disjoint two-sets and six ordered words. For one matching A,C,D, the exact inverse-source relation gives w_A+w_C+w_D=e0, hence W_A+W_C+W_D=6gamma0. Let V_A=W_A-2gamma0. Then V_A+V_C+V_D=0 and {V_A,gamma0}=0. Each V_A is supported on the white sublattice with zero center coefficient, so it commutes with every quadratic pair perturbation B_C (the CAR signs cancel). Accordingly [V_A,D_C]=[V_A,H0] is independent of C.

These identities permit centering the boundary sources before norm bounds, but they do not by themselves cancel their products with noncommuting R_A. The matching-summed correction is still retained. A next proof must exploit these actual cross commutators or bound their correlations; replacing the ordered products by commuting scalar inverses is not allowed.
