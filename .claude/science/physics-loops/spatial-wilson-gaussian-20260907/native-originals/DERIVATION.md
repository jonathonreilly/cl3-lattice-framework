# Actual nonlinear SU3 slab saddle and dilated central-kernel limit

This is an analytical result for the SAME supplied finite bare-Haar Wilson cube slab, not a Gaussian replacement of its action. Original preregistration fixed a finite-dimensional limit; the separate OPERATOR_EXTENSION_PREREGISTRATION froze the stronger kernel target before the argument below. The independent primary cycle calculation supplies exact constants only after the structural proof; none is fitted.

## 1. Exact gauge coordinates and unique minimum

Restore the8temporal links, obtaining the open tesseract with32edges,16vertices and22weightedfaces. Spatial weights are1/2, temporal weights1; both marked xy z0 faces are absent. Normalized Haar gauge changes were proved in the spatial-mixing parent. Fix ANY15edge spanningtree toI by recursive vertex gauge transformations with root gaugeI. For fixed tree variables, each remaining link undergoes left/right Haar translation. Integrating the15tree variables gives1, leaving EXACTLY product Haar on17SU3chords. No determinant, gauge-volume division or residual constraint appears.

Let E be the weighted sum of1−ReTr(U_f)/3. Every term is nonnegative. E=0 implies each weighted faceI. The two missing faces areI by the exact five-face disk identity. Thus all24faces are flat. On a hypercube, monotone paths between vertices differ by adjacent coordinate swaps, each bounded by a square face. Flatness identifies their transports. Cancelling backtracks then gives a vertex potential for every edge. In the spanningtree gauge that potential is constant, so ALL17chords areI. The gauged minimum is unique. Before gaugefixing the flat set is a gauge orbit; it is not claimed to be an isolated point in32link coordinates.

Choose an ADAPTED tree containing three edges of each of the two disjoint markedsourcefaces. Their union is a forest and extends to a spanningtree. The fourth edge of each sourceface is then a chord, and each marked holonomy is exactly that chord or its inverse. Orient these two group coordinates to equal the marked holonomies. The remaining15chords are nuisance variables. This exact global product-coordinate fact, not merely a linear submersion, is essential for the marginal-kernel proof.

## 2. Positive quadratic form and Haar chart

Use Hermitian traceless coordinates X_e=Σ_(a=1)^8 x_(e,a)T_a, Tr(T_aT_b)=delta_ab, U_e=exp(iX_e). Let B be the22face by17chord signed linear incidence matrix, W the diagonal positive face weights, and H=B*WB. Expanding the finite holonomy words and ReTr gives

E(X)= (1/6)Σ_a x_a*H x_a + O(||X||³).

H is positive definite without needing a numerical determinant. If Bx=0, the linearized missing-face disk relations give zero circulation on the two missingfaces. Thus all24face circulations vanish. The same coordinate-swap argument gives an exact vertex-gradient cochain; zero tree edges force that gradient constant and allchords zero. Therefore H>0.

The exponential map is an analytic local chart. Write normalized single-group Haar measure as j(X)dX, with j smooth, positive, Ad-invariant and j(0)=j0>0. Inversion invariance gives j(-X)=j(X), hence j(X)=j0+O(||X||²). One can also obtain this from the determinant of the left-translated differential of exp; no numerical Haar density is assumed. Taylor's theorem on a fixed small chart bounds the BCH/action remainder uniformly by C||X||³. Positive H allows the chart to be shrunk so E(X)≥c||X||² there. On the compact complement of any neighborhood of the unique minimum, E has a strictly positive gap.

## 3. Actual normalized saddle, not a proxy

Let Z_beta=∫exp(-beta E)dHaar on the17chords. In the local chart set X=x/sqrtbeta. Pointwise, beta E(x/sqrtbeta) tends to (1/6)Σ_a x_a*H x_a. The local lower bound supplies an integrable Gaussian dominator; the compact complement contributes at most exp(-beta gap). Dominated convergence, with the136dimensional Jacobian beta^-68, proves

Z_beta ~ j0^17 (2pi)^68 det(H/3)^(-4) beta^-68.

The normalized rescaled17chord coordinate density converges in L1 (equivalently probability total variation) to the136dimensional Gaussian with independent color components, each covariance3H^-1. The exponentially small outside-chart mass may be assigned a cemetery value. Gaussian domination also gives convergence of every fixed polynomial moment; this is not an assertion about unscaled or growing-degree tests.

For the two oriented source cycles with linear row matrix S, the leading Lie-log pair has covariance Sigma⊗I8, Sigma=3 S H^-1 S*. S has rank2: a linear combination of the two disjoint source cycles supported only on treeedges would be a cycle in a forest, hencezero; the two original cycles are independent. Thus the16dimensional Gaussian is nondegenerate. Nonlinear holonomy logarithms equal Sx+O(||x||²/sqrtbeta) on the scaling window; weak convergence follows already here. The stronger density statement next does not rely on this weak convergence alone.

## 4. Uniform marginal bounds and L2 convergence

Use the adapted tree, so the two sourceholonomies are group coordinates U,V globally. Let

k_beta(U,V)=Z_beta^-1∫_(SU3)^15 exp[-beta E(U,V,Z)]dZ.

This is a nonnegative density relative to dHaar(U)dHaar(V). For central sourcefunctions its bilinear integral is exactly D_beta/D00, with conjugate on the output function. Gaugefixed matrixholonomies themselves are not claimed to be ungaugedobservables.

Take an Ad-invariant exponential ball ||X||<delta on each sourcegroup, and let P_delta be its group multiplication projector. Define the rescaled joint Lebesgue density inside this chart by

p_beta(x,y)=beta^-8 j(x/sqrtbeta)j(y/sqrtbeta)
              k_beta(exp(ix/sqrtbeta),exp(iy/sqrtbeta)),

extended byzero outside the scaled sourceball. For fixed x,y, integrate the15nuisance coordinates after scaling them bysqrtbeta. The local Gaussian bound and the compact-gap bound justify dominated convergence, giving p_beta(x,y)→p_Sigma(x,y), the normalized16dimensional Gaussian marginal.

The same decomposition proves the stronger UNIFORM envelope p_beta(x,y)≤C exp[-c'(|x|²+|y|²)] for all sufficiently large beta. In the full localchart, nuisance integration contributes beta^-60 times exp[-c(|x|²+|y|²)]. The prefactor beta^-8/Z_beta is O(beta60). On the nuisance complement the contribution is at most C beta60 exp(-gap beta). Because the sourcewindow has |x|²+|y|²≤2delta²beta, choose c'≤gap/(4delta²); the polynomial can be absorbed into exp(-gap beta/2), producing the same Gaussian envelope. Constants may depend on the fixed chart, not on beta. This proves L1 AND L2 convergence of p_beta by dominated convergence, not just weak convergence.

If either sourcegroup is outside its fixed chart, uniqueness of the gaugedminimum gives a uniform positive energy gap on that compact set, for ALL nuisance variables. Hence k_beta(U,V)≤C beta68 exp(-gap beta) there. This controls the discarded source region in Hilbert–Schmidt norm, not merely probability mass.

## 5. Actual central-operator Hilbert–Schmidt limit

Let A_beta=D_beta/D00 on central L²(SU3,Haar). For its kernel, average k_beta independently under conjugation of U andV. This does not change central matrix elements; it is essential because a fixed gauge aligns the two Liealgebra frames, while the source Hilbert space contains only classfunctions. Denote this average by a bar. The chart, its Haar density and the Gaussian envelope are Ad-invariant.

The local unitary dilation from the chart subspace to functions supported in ||x||<delta sqrtbeta is

(U_beta f)(x)=beta^-2 sqrt[j(x/sqrtbeta)] f(exp(ix/sqrtbeta)).

Extend byzero outside that ball. It maps central functions to Ad-invariant functions in L²(su3,dX). It is an isometry on the chart subspace, not on the discarded group complement. The transformed kernel of beta^-4 U_beta P_delta A_beta P_delta U_beta* is

bar p_beta(x,y) / sqrt[j(x/sqrtbeta)j(y/sqrtbeta)].

The denominator tends to j0 and is uniformly bounded away fromzero on the chart. The Gaussian envelope therefore proves Hilbert–Schmidt convergence to

K_infinity(x,y)= (1/j0)∫∫ p_Sigma(Ad_g x,Ad_h y)dg dh.  (K)

This kernel acts on the Ad-invariant Liealgebra subspace (and vanishes on its orthogonal complement if viewed on full L²). The outside-source bound proves beta^-4||A_beta−P_delta A_beta P_delta||HS→0 on the original central space. Thus the chart cut loses no rescaled norm or nonzero spectral information. The family of partialisometries is explicit; no fixed-group strong limit is asserted.

K_infinity is a nonzero compact positive operator: compactness follows from its Gaussian L2kernel, positivity from the Hilbert–Schmidt limit of positive central operators, and nonzero from the positive Gaussian kernel. Consequently

beta^-4 ||A_beta|| → ||K_infinity|| >0.

This establishes the beta4growth rate for the ACTUAL SU3 slab under D00normalization, rather than merely for a Gaussian proxy. Fixed nonzero eigenbranches also converge to those of(K) with multiplicity by compact selfadjoint perturbation; exact eigenvalue formulas or gaps require a separate analysis of this kernel. The earlier fixed-window outer-dimension limit and fixed-vacuum divergence are compatible with this rescaled result.

## 6. Independent exact constants and scope

Primary's separately frozen cycle calculation, with the same trace convention, finds

Hdet=55/2,
Sigma=[[192,138],[138,192]]/11,
detSigma=1620/11.

Thus its normalized Gaussian density is

p_Sigma(X,Y)=(2pi)^-8(11/1620)^4
 exp[-(8/135)(TrX²+TrY²)+(23/270)Tr(XY)].

The nonlinear proof above needs only the stated exact covariance identity; it does not assume the Gaussian is the original Wilson action. j0 remains the actual normalized-Haar localdensity until separately derived. Neither the raw correlatedGaussian nor its matrix-frame coordinates should be called the central sourcekernel without the independentAd averages in(K).

No physical beta, formationlaw, dressed sourceembedding, thermodynamiclimit or high-representation uniform expansion is selected. The finite action, Haar measure and bare sourcemap remain supplied. The topology would fail if weightedface deletion left a nonflat gaugedminimum; the older paired-side-removal control exhibits that failure. A nonspanning gaugeforest would also leave flat gauge directions and invalidate the isolated-saddle argument. No such weakened fixture is silently used here.
