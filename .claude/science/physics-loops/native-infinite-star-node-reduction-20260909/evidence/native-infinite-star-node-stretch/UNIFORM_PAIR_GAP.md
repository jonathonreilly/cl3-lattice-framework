# A sharper infinite-volume gap for the actual two-link impurities

Provisional first-principles proof for independent review. No physical spectrum or numerical integral was computed. This sharpens a denominator used in the node representation; it does not determine the node scalar. Use h=2|t_hop|>0. The reference is the infinite canonical pi Gaussian state obtained from cubic AP tori. Energies are always relative to the same canonical E0.

## 1. Exact finite determinant reduction

Orient the two chosen star neighbors with signs so that u is their normalized signed sum and K_vu=-sqrt(2)h. Reversing their links changes the real skew matrix by

 Delta K=beta(v u^T-u v^T), beta=2sqrt(2)h,

with v the center basis vector and v perpendicular to u. The sign is opposite the original center coupling. For s>0 let

 A_L(s)=<v,(s^2-K^2)^(-1)v>,
 D_L(s)=A_L(s)-G_{2,L}(s),

where G_2 is the same-axis two-step Green entry in the centered gauge. K^2 is diagonal in cell parity and symmetric among axes. The resolvent identity and the six equal hopping magnitudes give exactly

 s^2 A_L+6h^2 D_L=1.

The projected real resolvent (s-K)^(-1) on(v,u) has entries

 [[s A_L, -sqrt(2)h D_L], [sqrt(2)h D_L, s B_L]],

where B_L=A_L for a perpendicular pair and B_L=D_L for an opposite pair. The cross term vanishes for different cell parities in the first case; the signed opposite pair subtracts G_2 in the second. The matrix determinant lemma therefore gives

 d_F,L(s)=det(s-K_F)/det(s-K)
         =(1-4h^2D_L)^2+8h^2s^2 A_L B_L.

With z=s^2A_L this becomes

 d_O=1-(8/9)(1-z)^2,
 d_P=(1+2z)^2/9+8h^2s^2 A_L^2.              (1)

Both are at least1/9 because0<=z<=1. These identities include the full unchanged bath; no active parity or spectator multiplicity is used to divide an energy again.

The finite full-active ground-energy difference is

 Delta E_F,L=-(1/(2pi)) integral_0^infinity log d_F,L(s) ds.    (2)

Indeed det(s-K)=product_positive_modes(s^2+omega_j^2), integral log[(s^2+a^2)/(s^2+b^2)]ds=pi(a-b), and the active ground energy is -sum_positive omega_j/2. This fixes the factor in(2).

## 2. The infinite scalar Green function and a rational bound

The AP Riemann limit is

 A(s)=average_k [s^2+4h^2 sum_a sin^2 k_a]^(-1).

At s=0, folding2k gives

 6h^2 A(0)=sum_{n>=0} p_(2n),
 p_(2n)=6^(-2n) sum_{a+b+c=n} (2n)!/(a!^2 b!^2 c!^2).

These are simple-cubic return probabilities. The expansion is legitimate by symmetry of phi=(cos x+cos y+cos z)/3 and monotone expansion of1/(1-phi^2). For n>=1,

 p_(2n) <= [3sqrt(3)pi^(3/2)/32] n^(-3/2) < n^(-3/2).

To derive it, split phi>=0 and phi<=0; the latter is the translated former. On the first region1-phi>=2|x|^2/(3pi^2) for x in[-pi,pi]^3, and phi^(2n)<=exp[-2n(1-phi)]. Extending the resulting Gaussian integral to R^3 gives the displayed constant. Its square is27pi^3/1024<1, using pi<22/7.

The exact rational partial sum through n=100 is less than3/2. The remaining sum is at most integral_100^infinity x^(-3/2)dx=1/5. Hence

 A(0)<=17/(60h^2).                            (3)

The companion control computes only the explicit rational factorial sum and compares exact fractions; it does not sample momentum or evaluate a physical spectrum.

Let X=4h^2 sum sin^2 k. Its moments are EX=6h^2, EX^2=42h^4. Cauchy-Schwarz applied to sqrt[X/(s^2+X)] and sqrt[X(s^2+X)] gives

 1-z=E[X/(s^2+X)] >= 6h^2/(s^2+7h^2).        (4)

## 3. Both determinant integrands have the needed sign

For opposite pairs, (1) directly gives d_O<=1 and

 Delta E_O >= (1/(2pi)) integral (8/9)[6h^2/(s^2+7h^2)]^2 ds
            =4h/(7sqrt(7)) > h/5.

For perpendicular pairs set u=s^2/h^2. Equation(4) gives z<=(u+1)/(u+7). Since d_P is increasing in A,

 d_P <=1-(24-8/u)/(u+7)^2 <=1  for u>=1/3.

For0<=u<=1/3, (3) instead gives d_P<=P(s/h), where, with a=17/60,

 P(y)=1/9+(4a/9+8a^2)y^2+(4a^2/9)y^4.

P is increasing for y>=0, and P(1)<1, so the small-u range also has d_P<=1. Thus omitting the rest of the positive -log integral in the next bound is valid, rather than silently discarding a possibly negative contribution.

For0<=y<=1, define w(y)=1-P(y)>0. The elementary series gives

 -log d_P(hy)>=sum_{n=1}^{12} w(y)^n/n.

The polynomial integral is rational. Using1/(2pi)>7/44, the exact control proves

 Delta E_P/h >=(7/44)sum_{n=1}^{12}(1/n)integral_0^1 w(y)^n dy
             >1/6.

The computed rational lower bound is approximately0.186999628; the theorem uses only the exact comparison with1/6. No fitted coefficient is introduced.

## 4. Passing the energy lower bound to the Gaussian GNS space

For each fixed s>0, finite AP A_L(s) converges to A(s). The parent shifted-grid inverse-square estimate bounds A_L(0) uniformly, so the logarithms in(2) are uniformly bounded near zero, using d_F,L>=1/9 and the explicit determinant expressions. At large s, the exact shared second moment of K and K_F, or direct expansion of(1) with the uniform bounded dispersion, gives log d_F,L=O(s^-4) uniformly. Dominated convergence thus identifies the limit of the finite energy differences with(2) using A(s).

For any fixed local polynomial X, finite lower bounds H_L+B_A-E0,L>=Delta E_A,L pass to the GNS quadratic form as in the thermodynamic parent. The local-polynomial core and bounded B_A extend the inequality to its full self-adjoint domain. Therefore, for the actual infinite two-link impurities,

 H+B_A >= (h/6) I.                            (5)

This is an infinite-volume denominator bound relative to the original vacuum energy. It is not a uniform active gap, a statement about a nonminimizing reference, or a claimed explicit finite-L threshold. No assertion of a defect vacuum vector's existence in this representation is required for the lower bound.

## Consequence for the proposed node integration

After independent review, (5) permits delta=h/6 in the exact imaginary-time tail. With beta<3h, T=160/h already gives complete90-word tail below10^-6/h^2, verified by rational lower Taylor bounds for the exponential. This reduces the earlier1024/h conservative cutoff, but does not certify pointwise Gaussian arithmetic or make the node sign known. A cost-only fixed kernel pilot remains separate and unlaunched.
