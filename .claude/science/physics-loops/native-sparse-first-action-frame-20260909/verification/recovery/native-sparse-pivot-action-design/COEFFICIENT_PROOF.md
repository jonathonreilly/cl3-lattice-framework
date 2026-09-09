# Exact ideal pivot coordinates and first-action contraction

Source-only continuation of reviewed fixed192 pivot arithmetic and three-source first-action DATA proof3d766. No saved history, native input, index or matrix is evaluated. Every interval below must enclose the SAME true physical Gram and same exact selected pivot sequence. Authenticating saved source/input/row identity is indispensable; an arbitrary shape-correct history is not evidence.

## Exact original-domain coefficients

Write F=[raw399,Gamma raw399], and let Jc=[[0,-I],[I,0]], so F Jc=Gamma F. The actual pivot seed is a chiral pole HALF column (z_plus-eta*chi*z_minus)/2 or an appended x column. Let s_i be its exact sparse coefficient in F. These s_i have entries±1/2 or1. The396 pole half labels plus3 append labels are not independently normalized modes; reconstructing their metric uses the existing weights2/1, but those weights do NOT multiply the coefficient s_i.

For selected index i_h define residual b_h=(I-Q_(h-1))F s_(i_h). Let g_hj=<b_h,F s_j>, j_hj=<b_h,Gamma F s_j>, r_h=||b_h||²>0. These are exactly the saved residual rows: prior orthogonal projection disappears in the second argument because b_h and Gamma b_h are orthogonal to every previous pair. Their interval versions are correlated enclosures, not independent true parameters.

Define coefficient vectors beta_h recursively by

 beta_h=s_(i_h)-sum_(a<h) [ beta_a*g_(a,i_h)/r_a - Jc beta_a*j_(a,i_h)/r_a ].

Then F beta_h=b_h. In particular the PLUS sign in front of Jc beta_a*j/r is required because <Gamma b_a,F s_i>=-j_ai. Set c_h=beta_h/sqrt(r_h), and c'_h=Jc c_h. The columns C=(c_1,c'_1,...,c_k,c'_k) give an EXACT ideal isometry V=F C. The proof is ordinary paired orthogonal projection: the two columns in each pair are unit and mutually orthogonal because Gamma is skew; the residual removes all prior pairs. No inversion of the full Gram or numerical rank determination occurs. Positive lower pivot intervals prove r_h>0 for each accepted step. Coefficients need not be unique if F has dependencies; this recursively chosen representation is legitimate and stays in the ORIGINAL798 domain.

## Validated finite coefficient construction

Use outward fixed192 interval add/multiply/divide for beta recursion and outward sqrt for c. All old saved r intervals must have strict positive lower endpoints; every actual g,j value lies in its saved interval. Interval induction encloses the exact beta and C even though the occurrences are dependent. Treating dependent occurrences separately may widen enclosures but cannot invalidate them. Applying Jc is an exact signed permutation. No coefficient is obtained by dividing by a rounded midpoint pivot.

A denominator-growth-free implementation is therefore possible: after each operation round outward to the fixed dyadic lattice. Integer magnitude is not automatically bounded: beta may be large when pivots are small or the original family nearly dependent. A finite byte/bit cap and explicit width gates must terminate honestly with INDETERMINATE if necessary. Existing reconstructed-coordinate d≤1/40000 does not bound beta or C: those coordinates describe F in the ideal basis, the inverse direction is ill-conditioned. A new coefficient certificate is required.

One optional a priori runtime bound is scalar interval recursion B_h≤||s_i||_1+sum B_a*(|g_ai|+|j_ai|)/r_a using upper absolute row endpoints and positive lower r. It bounds coefficient l1 magnitudes before allocating large arrays. It is not a promise of affordable widths. Only2k coefficient columns of length798 are needed (k≤4 for the current pilot), with sparse seeds; later continuation is a separate resource decision.

## Action and leakage without declaring a midpoint isometry

Let Z be the804 DATA family of the three-source proof, E the original embedding, M=Z^T Z, and D_A(M) the exact804×798 coefficient matrix satisfying K_A F=Z D_A. It includes the explicit free action and the LINEAR Gram-row rank-two correction8[e_x0 M_(qA,:)E-e_qA M_(x0,:)E]. For a fixed accepted pair of physical A/C supports there is no unknown moment beyond the accepted scalar inputs of the DATA proof.

Set B=D_A(M) C. Then H_A V=i Z B, and

 A_V=i C* E^T M B,
 G_action=B* M B,
 L=G_action-A_V²=(H_A V-V A_V)*(H_A V-V A_V) >=0.

All entries can be interval-contracted using enclosures of M and C, with D_A recomputed as an interval expression of M. Repeated appearances of M/C remain the same exact object; outward enclosure arithmetic is safe without pretending independence. Alternatively form T=i B-E C A_V, then L=T* M T. Both identities are exact and select the same true L. Either route may have cancellation/width problems; neither grants favorable conditioning.

A rigorous upper bound delta² is max_i sum_j sup|L_ij| after intersecting Hermitian-related entries and true nonnegative diagonal constraints if desired. Any intersection must use a proved property and retain the true entry. The operator norm is bounded by this Hermitian row sum, so sqrt(delta²) is an upper leakage bound. Failure to meet a predeclared sufficient target is an honest inconclusive result. This requires no certification that midpoint C* M C equals I: ideal isometry follows from exact pivot identities. It DOES require proof that each saved row encloses the physical exact recurrence and that the new DATA M refers to the same F, scalar normalization and phases.

Numerical midpoint C may separately provide a candidate frame, but is not V and cannot inherit these exact identities without an additional nearby-frame bound. The signed action proof covers ONLY original F; no second action on appended q columns is used: G_action is computed as the norm Gram of first-action images. Thus the 804 workspace does not silently enlarge the trial domain.

## Concrete implementation boundary

Required future inputs: authenticated complete pivot history/context; sparse canonical half-column map; accepted804 DATA enclosure with physical inflation and arithmetic provenance; exact alpha/pole coefficient enclosures for D0. Saved stationary396/399 midpoint entries alone do not supply the DATA extension or its mu dependence. Old full Gram need not be inverted, but all contractions used must be available via a bounded streaming reader. At most8×8 leakage matrix in the fixed four-pair pilot is small; the dominant work is accurate Gram contractions over804 coordinates and may not be small. No cost or successful leakage is inferred here.
