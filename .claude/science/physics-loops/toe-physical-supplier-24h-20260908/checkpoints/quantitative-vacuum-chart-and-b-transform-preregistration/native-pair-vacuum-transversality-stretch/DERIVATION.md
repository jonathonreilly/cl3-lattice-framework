# An explicit native pair-vacuum chart and nonzero overlap

This bounded first-principles extension concerns the stationary active Gaussian vacuum of either actual infinite two-link star impurity, and its interpolation B_lambda=B0-2lambda e0 b_A^T,0<=lambda<=1. It assumes the supplied canonical pi-flux cubic reference, h=2|t_hop|>0, and the already reviewed local Green/trace-class statements. It does not evaluate a physical matrix, scalar oracle or impurity overlap. It does not establish a chart for every cross-impurity time-dependent overlap.

## 1. Domains and trace-class prerequisites

Use the real bipartite block K0=[[0,B0],[-B0^T,0]]. The bare symbol has no l2 zero mode. The local inverse-square bound and b_A^T B0^-1 e0=1/3 show that B_lambda and B_lambda^T have zero kernel for all lambda, as detailed in GENERIC_RANK_ONE.md. Therefore their polar factors are onto real orthogonal maps, despite the gapless essential spectrum. Write

 B0=U0 S, B_lambda=U_lambda T_lambda, R_lambda=U0^T U_lambda,
 D_lambda=U0^T B_lambda=S-2lambda u b_A^T=R_lambda T_lambda,
 u=U0^T e0.

S,T_lambda are bounded positive injective operators; their inverse operators need not be bounded. Every weighted inverse vector below is defined by its finite spectral quadratic form. The trace-class impurity proof5654417a gives ||P_lambda-P0||_1<87 and trace-norm continuity, uniformly along both actual pair interpolations. Thus R_lambda-I is compact and trace class. The qualitative rank-one/Fredholm determinant proof is preserved separately; the metric estimate below is stronger and does not need determinant parity to exclude -1.

## 2. A finite exact bound for the weighted local inverse

Define C0=<e0,|h0|^-1 e0>. Folding the Brillouin zone gives

 h C0=(1/sqrt6) sum_(n>=0) c_(2n) p_(2n),
 c_m=binom(2m,m)/4^m,
 p_(2n)=binom(2n,n) sum_(j=0)^n binom(n,j)^2 binom(2j,j)/6^(2n).

To justify the positive expansion, average the binomial series at phi and -phi for |phi|<1 and then use monotone convergence; the nodal set has measure zero. The earlier return-probability proof gives p_(2n)<n^(-3/2) for n>=1. Also c_m²(3m+1)<=1: multiplying the induction ratio reduces to

 (2m+1)²(3m+4)-(2m+2)²(3m+1)=-m<=0.

Consequently the tail after N is at most1/(6N). The fixed exact32-term sum, with sqrt6>2449/1000, proves

 h C0 <= (1000/2449) sum_(n=0)^32 c_(2n)p_(2n)+1/192 <7/15.       (1)

The accompanying control evaluates only finite integer/rational combinatorial expressions, not a physical integral or an elliptic oracle. Its exact partial sum and bound are retained in RESULT. This supplies a stronger weighted metric than Cauchy-Schwarz with the previous inverse-square bound.

## 3. Actual rank-one weighted form

Let a=S^-1/2 u and d=S^-1/2 b_A. Then

 ||a||²=C0, a^T d=1/3.

For a perpendicular selected pair, different cell parities make the offdiagonal even Green entry zero, so ||d||²=2h² C0. For an opposite pair, isotropy gives

 ||d||²=mu/3, mu=<e0,|h0|e0><=sqrt6 h<5h/2.

Indeed the signed opposite-neighbor difference has spectral factor2sin²(k_a), whose three-axis average is X/(6h²); multiplication by the squared source norm2h² gives mu/3.

Define gamma_A=2||a||||d||. Equation(1) implies, for perpendicular pairs,

 gamma_A<14sqrt2/15<33/25,

using sqrt2<99/70. For opposite pairs gamma_A²<14/9<(33/25)². Thus the common rational bound gamma_A<=33/25 is valid for both geometries.

For any complex vector x, weighted Cauchy-Schwarz gives

 |x* (D_lambda-S)x|<=lambda gamma_A <x,Sx>,
 |x* D_lambda x|<=(1+lambda gamma_A)<x,Sx>.              (2)

The symmetric rank-two form a d^T+d a^T has largest eigenvalue a^T d+||a||||d||. Therefore

 Re <x,D_lambda x> >=[1-lambda/3-lambda gamma_A/2]<x,Sx>
 >=(1/150)<x,Sx>.                                      (3)

All identities extend from spectral-cutoff vectors by bounded forms. The fact that a,d exist in l2 is sufficient; no global bounded S^-1 is used.

## 4. Relative polar angles: the bound is eigenvector-specific

Since R_lambda-I is compact normal, every spectral value other than1 is an eigenvalue e^(i theta), with finite multiplicity. Choose a normalized complex eigenvector x. Orthogonality/unitarity gives x*R_lambda=e^(i theta)x*, and hence

 <x,D_lambda x>=e^(i theta)<x,T_lambda x>.

Both <S> and <T> are strictly positive. Combining the MODULUS estimate(2) for this vector with(3) yields

 cos theta >=(1/150)/(1+33/25)=1/348.                   (4)

The spectral value1 trivially satisfies this. Crucially, no operator inequality |S^(1/2) C S^(1/2)|<=||C||S, or T_lambda<=(1+gamma_A)S, is asserted. Such an inequality would be unjustified for noncommuting matrices. Only the expectation on a genuine polar eigenvector is used.

It follows that

 ||P_lambda-P0|| <=sqrt(347/696)<1/sqrt2,
 Z_lambda=(I-R_lambda^T)(I+R_lambda^T)^-1,
 ||Z_lambda||<=sqrt(347/349)<1.                        (5)

Z_lambda is real skew and trace class. This is an explicit, uniform-in-lambda and geometry bound on the reference-vacuum graph chart, in the infinite supplied model. It is not inferred from finite-volume determinant signs or from even parity alone.

## 5. Constructive vacuum and overlap

After aligning the two sublattices by U0, define reference annihilators f=(A+iB)/2. The impurity annihilators may be chosen as

 f_lambda=(R_lambda^T A+iB)/2
          =[(I+R_lambda^T)f+(R_lambda^T-I)f^dagger]/2.

Equation(5) solves this Gaussian vacuum as a pairing graph with matrix Z_lambda. The real orthogonal spectral decomposition of R_lambda consists of two-dimensional rotation planes with angles theta_j in(-pi,pi), plus its fixed subspace. On each plane, the normalized vacuum factor has reference amplitude cos(theta_j/2)>0 and pair amplitude of modulus |sin(theta_j/2)|. This can be verified directly with two complex CAR modes, or by rotating the A Majoranas alone by the real Spin lift.

Trace-class control implies sum_j |sin(theta_j/2)|<87/4. Therefore the finite products of normalized pair factors converge in the reference Fock space; their tails are Cauchy because the sum of squared pair amplitudes converges. Their covariance is the desired negative-band projector. This constructs the impurity quasifree vacuum with positive reference overlap without assuming an implementation theorem, a uniform active gap, or parity merely from a determinant sign.

Explicitly,

 |<Omega0,Omega_lambda>|=product_j cos(theta_j/2)>0.

The exponent for det((I+R_lambda)/2) is ONE HALF for the overlap amplitude: a single real rotation plane contributes cos²(theta/2) to that determinant and cos(theta/2) to the amplitude. Using a one-quarter exponent for this sublattice determinant would be incorrect.

Set c=1/348 and x_j=sin²(theta_j/2)<=(1-c)/2. Since -log(1-x)<=x/(1-x_max),

 log |<Omega0,Omega_lambda>| >=-sum_j x_j/(1+c)
 >-87/[4(1+c)]=-7569/349.                              (6)

Thus a deliberately coarse but explicit positive overlap lower bound is exp(-7569/349). No numerical overlap was calculated. The bound holds for each reference-to-impurity stationary vacuum. It neither guarantees that two different impurity vacua overlap nor prevents zeros of arbitrary mixed-reference time kernels.

## 6. Quantitative finite-mode tail in this chart

If an exactly invariant collection of rotation planes is retained and the discarded pairing weight is r=sum_discarded sin²(theta_j/2), the normalized finite product has squared vector error

 ||Omega_lambda-Omega_lambda,retained||²
 =2[1-product_discarded sqrt(1-x_j)]<=2r.               (7)

The inequality follows from product(1-x_j)>=1-sum x_j (or is trivial when r>=1). If instead the actual discarded trace-class projector tail is eta=4 sum_discarded |sin(theta_j/2)|, then r<=eta/4 and the error is at most sqrt(eta/2). A sharper HS-tail statement is r=||P_tail||_HS²/4. These are actual a posteriori spectral-tail certificates, not a claim that the current coarse Gram intervals have identified such planes. Approximating noninvariant subspaces and propagating interval basis errors remain separate computational obligations.

The graph chart removes the stationary reference-overlap obstruction. It does not settle alpha, finite-time excitation rank, mixed-impurity phase tracking, or a physical phase of the full electric Hamiltonian.
