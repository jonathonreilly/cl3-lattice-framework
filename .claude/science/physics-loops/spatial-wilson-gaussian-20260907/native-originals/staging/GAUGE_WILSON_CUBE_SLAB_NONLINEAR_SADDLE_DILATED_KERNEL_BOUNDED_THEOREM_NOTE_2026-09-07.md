---
claim_id: gauge_wilson_cube_slab_nonlinear_saddle_dilated_kernel_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
claim_scope: "For the supplied finite open SU(3) Wilson cube slab and bare-Haar central source map, the actual nonlinear normalized kernel under local Lie-coordinate dilation and beta^-4 amplitude scaling converges in Hilbert–Schmidt norm to an independently conjugation-averaged Gaussian kernel. The proof includes gauge fixing, unique flat minimum, positive cycle Hessian, Haar/BCH localization and uniform source-fiber tails; no thermodynamic or physical coupling identification is claimed."
---

# Actual SU3 slab: nonlinear saddle and dilated central kernel

The actual Wilson source operator, rather than a substituted Gaussian model, has a compact Gaussian limit after an explicitly defined local coordinate dilation and beta^-4 scaling. This proves its D00-normalized norm grows as a positive constant times beta4. The limiting operator acts on Ad-invariant Liealgebra functions and includes the necessary independent conjugation averages.

## Status and direct premises

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
bodyType: bounded_theorem
conditional_surface_status: "Conditional on the supplied finite open Wilson/Haar action and constant-spectator central source embedding; no physical action or coupling is selected."
hypothetical_axiom_status: null
```

Independent audit owns status authority.

- [Actual cube-slab source](GAUGE_WILSON_CUBE_SLAB_CHARACTER_MIXING_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the exact source compression, open gauge restoration and22weighted-face model.
- [Fixed-window weak-coupling parent](GAUGE_WILSON_CUBE_SLAB_WEAK_COUPLING_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-07.md) records the noncommutative five-face word and separates fixed-window limits from full-space norm growth. Its weak convergence is not substituted for the stronger estimates proved here.
- [Native compact-group convention](GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.md) supplies normalized Haar and representation conventions.

Exact support runner: [gauge_wilson_cube_slab_adapted_tree_saddle_check_2026_09_07.py](../scripts/gauge_wilson_cube_slab_adapted_tree_saddle_check_2026_09_07.py), reporting TOTAL24=geometry7+positive-LDL-pivots17. The independent adapted tree has literal separate source chords and determinant55/2. These are finite exact geometry checks; the nonlinear Haar localization and Hilbert–Schmidt proof below are not inferred from a finite Gaussian sample.

## 1. Exact gauge coordinates and unique minimum

Restore the8temporal links, obtaining the open tesseract with32edges,16vertices and22weightedfaces. Spatial weights are1/2, temporal weights1; both marked xy z0 faces are absent. Normalized Haar gauge changes were proved in the spatial-mixing parent. Fix ANY15edge spanningtree toI by recursive vertex gauge transformations with root gaugeI. For fixed tree variables, each remaining link undergoes left/right Haar translation. Integrating the15tree variables gives1, leaving EXACTLY product Haar on17SU3chords. No determinant, gauge-volume division or residual constraint appears.

Let E be the weighted sum of1−ReTr(U_f)/3. Every term is nonnegative. E=0 implies each weighted faceI. The two missing faces areI by the exact five-face disk identity. Thus all24faces are flat. On a hypercube, monotone paths between vertices differ by adjacent coordinate swaps, each bounded by a square face. Flatness identifies their transports. Cancelling backtracks then gives a vertex potential for every edge. In the spanningtree gauge that potential is constant, so ALL17chords areI. The gauged minimum is unique. Before gaugefixing the flat set is a gauge orbit; it is not claimed to be an isolated point in32link coordinates.

Choose an ADAPTED tree containing three edges of each of the two disjoint markedsourcefaces. Their union is a forest and extends to a spanningtree. The fourth edge of each sourceface is then a chord, and each marked holonomy is exactly that chord or its inverse. Orient these two group coordinates to equal the marked holonomies. The remaining15chords are nuisance variables. This exact global product-coordinate fact, not merely a linear submersion, is essential for the marginal-kernel proof.

## 2. Positive quadratic form and Haar chart

Use Hermitian traceless coordinates X_e=Σ_(a=1)^8 x_(e,a)T_a, Tr(T_aT_b)=delta_ab, U_e=exp(iX_e). Let B be the22face by17chord signed linear incidence matrix, W the diagonal positive face weights, and H=B*WB. Expanding the finite holonomy words and ReTr gives

E(X)= (1/6)Σ_a x_a*H x_a + O(||X||³).

H is positive definite without needing a numerical determinant. If Bx=0, the linearized missing-face disk relations give zero circulation on the two missingfaces. Thus all24face circulations vanish. The same coordinate-swap argument gives an exact vertex-gradient cochain; zero tree edges force that gradient constant and allchords zero. Therefore H>0.

The exponential map is an analytic local chart. Write normalized single-group Haar measure as j(X)dX, with j smooth, positive, Ad-invariant and j(0)=j0>0. Inversion invariance gives j(-X)=j(X), hence j(X)=j0+O(||X||²). One can also obtain this from the determinant of the left-translated differential of exp; no numerical Haar density is assumed. Choose nested Ad-invariant exponential balls whose smaller closed ball lies in the larger chart. All local density upper/lower bounds below are taken on that compact closure, and the energy gaps use complements of fixed smaller neighborhoods. Taylor's theorem on this fixed small chart bounds the BCH/action remainder uniformly by C||X||³. Positive H allows the chart to be shrunk so E(X)≥c||X||² there. On the compact complement of any neighborhood of the unique minimum, E has a strictly positive gap.

## 3. Actual normalized saddle, not a proxy

Let Z_beta=∫exp(-beta E)dHaar on the17chords. The actual unnormalized D00 is exp(17beta)Z_beta; this common factor cancels exactly in D/D00. Any common positive temporal normalization also cancels. No exponential action factor is omitted from an unnormalized asymptotic. In the local chart set X=x/sqrtbeta. Pointwise, beta E(x/sqrtbeta) tends to (1/6)Σ_a x_a*H x_a. The local lower bound supplies an integrable Gaussian dominator; the compact complement contributes at most exp(-beta gap). Dominated convergence, with the136dimensional Jacobian beta^-68, proves

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

## 6. Scope and exact-constant interface

This theorem defines Sigma=3 S H^-1 S* from the exact native face/chord geometry. It needs only its positivity and the actual finite matrix definition. An independent companion computes its entries, the normalized-Haar density j0 and the compact Gaussian invariant spectrum. Those numerical/algebraic evaluations are downstream consequences, not premises needed for the present nonlinear convergence proof; this avoids a circular import between the convergence and spectrum notes.

Neither the raw correlated Gaussian nor its tree-frame coordinates is the central source kernel without the independent Ad averages in(K). No physical beta, formation law, dressed embedding, thermodynamic limit or high-representation uniform expansion is selected. The finite action, Haar measure and bare source map remain supplied. The earlier paired-side-removal control would leave a nonflat gauged minimum; a nonspanning gaugeforest would leave gauge directions. Neither weakened fixture is used here.
