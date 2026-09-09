---
claim_id: native_sparse_first_action_frame_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied infinite native reference, fixed common midpoint family: three-source first-action DATA closure and conditional sparse pivot/action certificates."
upstream_dependencies:
  - native_gapfree_generator_propagation
  - native_finite_excitation_ward_note_2026-09-09
  - native_certified_local_green_scalars_note_2026-09-09
runner: scripts/native_sparse_first_action_frame_2026_09_09.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Sparse first-action frame for the supplied native model

**Status:** conditional-support. Constituent source reviews are preserved in the packet; final assembled review is separate. Formal audit is deferred. No native leakage, propagated state or alpha is computed by this milestone.

Use the [signed generator and gap-free propagation theorem](NATIVE_GAPFREE_GENERATOR_PROPAGATION_NOTE_2026-09-09.md), [finite-excitation Ward framework](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md) and [local Green scalar definitions](NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md). All supplied-model, infinite-reference and same-frame premises remain. Units below are h=1; general generator scales multiply by h.

The concrete advance is that first-action certification for an ideal frame obtained from at most four paired pivots requires at most24 DATA coordinates, not a dense804-coordinate contraction. Exactly three added bare sources suffice. This is an exact conditional algebraic closure; it supplies neither a well-conditioned pivot frame nor a small leakage estimate.

## Fixed mathematical family and executable scope

F is exactly the accepted family at rational midpoint poles s and rational midpoint balancing alpha. These rational numbers define F; outward conversion and sqrt(alpha) enclose its exact coefficients. They are not substitutions for unknown exact Gauss roots or pi in a different family. The analytic quadrature displacement reserve remains separate. Saved histories, DATA entries and action coefficients must refer to this identical F. An arbitrary shape-correct history or newer scalar schedule does not satisfy the hypothesis.

The ORIGINAL family has399 raw/798 real closed columns. DATA adds qA,qC,qD and their Gamma partners, giving402/804. The trial isometry V=FC stays in ORIGINAL F. No second action on the added q columns is asserted. Tuple coordinates(raw,Gamma-bit) decode old flattened indices with399 before any DATA402 re-encoding. The half seeds carry±1/2 coefficients, not the reconstruction weights2/1.

The following complete proof blocks preserve the constituent arguments, with their source provenance in verification/recovery. Historical source-only statements describe those constituent implementations; they do not negate the later bounded execution snapshots below or imply a new execution here.


## Three-source DATA closure


Source-only theorem in dimensionless h=1 units, with the supplied infinite native reference and conventions H0=iK, Gamma=i sign(H0). Import the reviewed Ward proof222f, augmented ledger0cfc, common five-orbit proofc61c, and canonical generator note with the corrected ORIGINAL-domain restriction (source5cecf). No native entries, scalar loader, integral, compression or propagation are evaluated here.

## 1. Domain versus workspace

The ORIGINAL raw carrier F has396 balanced pole columns z=√alpha y_sigma(v), v in {e0,dA,dC}, and x0=e0/2,xA=wA/2,xC=wC/2. Its covariance closure has798 real columns. Append ONLY qA=dA/2,qC=dC/2,qD=d_all/2 and their Gamma partners. The DATA carrier Z has402 raw/804 closed columns. Compression and an isometry V=FC remain in the ORIGINAL798-column domain; the DATA carrier is not a new compression domain. Its second action is not claimed closed.

The three bare columns are linearly independent for disjoint two-element A,C: their supports leave two neighbors outside A∪C, so the d_all coefficient in any dependence vanishes first, then the other two coefficients vanish. Thus three is the exact dimension of this bare source span. No assertion that all three remain independent modulo the nonlocal original F is needed, or made.

Ky_sigma(v)=sigma*s*y_sigma(v)-v, KwA=dA, KwC=dC, Ke0=d_all, and K commutes with Gamma. These identities prove K F lies in Z. DeltaK_A=2(e0 dA^T-dA e0^T) also maps F into Z. Same for C. Restoring h multiplies K action and DeltaK by h after dimensionless scaling; the following scalar formulas and ledger are explicitly h=1.

## 2. Every new entry, with signs and scales

Use seven-star order (0,+x,-x,+y,-y,+z,-z), signed d's, I, O joining opposite neighbors, N=I+O and T_(0,+a)=-1,T_(0,-a)=+1, T skew. For u∈{dA,dC,d_all}, put q=u/2. Let D_s=(1-s²A_s)/6. For an original balanced pole z=√alpha y_sigma(v),

 G(q,z)=(√alpha/2) u^T[ sigma*s*(A_s N-D_s O)+D_s T ]v,
 J(q,z)=(√alpha/2) u^T[ B_s N-(mu-s²B_s)O/6-sigma*s*B_s T/6 ]v.

Here J(a,b)=<a,Gamma b>. For original insertion columns,

 G(q,x0)=G(q,xA)=G(q,xC)=0,
 J(q,x0)=-(mu/24)u^T T e0,
 J(q,xA)=-(1/4)dA^T[c N-mu O/6]u,
 J(q,xC)=-(1/4)dC^T[c N-mu O/6]u.

In particular J(qD,x0)=-mu/4, while J(qA,x0)=J(qC,x0)=-mu/12. This minus sign follows from u^T T e0=6 or2; reversing it changes the generator normalization. The Ward cross minus sign follows from skew-adjoint Gamma, not from changing the source d.

New-new entries are G(q_u,q_v)=u^T v/4 and J=0. Thus the3×3 G block is [[1/2,0,1/2],[0,1/2,1/2],[1/2,1/2,3/2]]. J=0 because these sources share the neighbor sublattice. All cross blocks in the closed carrier follow from M=[[G,J],[-J,G]]. New raw sources have negative chirality, their Gamma partners positive; exact structural zero tests must respect this reversal relative to x0,xA,xC.

These formulas are direct restrictions of the reviewed local Green/ Ward identities. Nonzero-pole A,B, old derivatives A′,B′, a0,c and mu suffice. There is no A″, new zero-pole division, additional moment or distance-two covariance. The new entries do not involve a0 directly, but the retained original Ward block does. mu is essential and must be bound to its actual certificate; a file's existence is not acceptance.

## 3. Explicit signed action coefficient matrix

Let E embed the original closed columns in Z. Define D0 by the following column rules (and their Gamma copies):

 Kz=sigma*s*z-2√alpha*x0 or -2√alpha*qA or -2√alpha*qC, according to v;
 Kx0=qD, KxA=qA, KxC=qC.

For ALL original columns f, including Gamma copies, add

 DeltaK_A f=8[x0 <qA,f>-qA <x0,f>].

Hence D_A=D0+8[e_x0 (M_(qA,:)E)-e_qA(M_(x0,:)E)] satisfies K_A F=Z D_A exactly. D_C is analogous. In the Gamma columns only the free K part is obtained by commuting Gamma; DeltaK does NOT commute with Gamma and must use the displayed actual Gram rows. This avoids a false shortcut.

Therefore F*H_A F=i E^T M D_A and (H_A F)*(H_A F)=D_A^T M D_A. For an exact V=FC with C*E^T M E C=I, A_V=i C*E^T M D_A C and leakage-square equals C*D_A^T M D_A C-A_V². Complex C uses adjoints. These are exact identities; midpoint Gram and approximate coefficient matrices need rigorous interval propagation, including the dependence of D_A on M. Neither a small leakage nor stable C is implied. An enlarged-domain V using q columns would need additional action data and is excluded.

## 4. Sufficient physical-input ledger, separate from action conditioning

The original closed trace<531 increases by exactly2*(2+2+6)/4=5, so Tr M<536. No coefficient is added to the stationary impurity matrices: pad them by zero and their norm≤1 remains. The original scalar error bounds and geometry assumptions are imported unchanged:1/128≤s≤16,√alpha<4, eta_A,eta_A′,eta_a0≤1e-30, eta_B,eta_B′,eta_c≤1e-19. Require additionally eta_mu≤1e-19 (radii, not widths).

Literal signed geometry gives for neighbor v∈{dA,dC}: |u^T N v|≤2, |u^T O v|≤2, u^T T v=0. For v=e0 only T survives and |u^T T e0|≤6. Consequently the new balanced pole entries have conservative sensitivities: A≤2800, B≤176, mu≤1. New insertion entries have c≤1/2 and mu≤1/4, and new self entries are exact. Taking a loose maximum over804 entries per row, the newly supported matrix error is bounded by

 epsilon_new ≤804*(2800 eta_A+176 eta_B+eta_c+eta_mu).

Add this to the OLD embedded block bound; do not charge the old block a second time as an append. For the B/c/mu group, epsilon≤48985020*1e-19+804*178*1e-19=49128132*1e-19<5e-12. For A/a0 use old2^40*1e-30 plus804*2800*1e-30<2^41*1e-30.

The equivariant factor bound is now E(epsilon)=2√(536*1608*epsilon)+1608epsilon for each norm≤1 stationary coefficient matrix. E(5e-12)<.00416; E((2^40+804*2800)*1e-30)<.000002; a separate FINAL total arithmetic spectral radius≤2^-60 contributes<.000002. Signed coefficient radius≤2^-40 contributes<1e-9. With the imported1e-6 pole/weight/pi reserve the total is<.0042<.005. The arithmetic gate must cover the COMPLETE804 matrix, e.g.old bound plus new append row-sum; it is not a fresh2^-60 allowance on each block. Physical scalar input uncertainty and midpoint arithmetic are separate.

These bounds certify proximity for stationary weighted operators under the common-factor theorem, NOT a generator/leakage error of.005. D_A contains source scales and M entries, and C may be ill-conditioned: their interval errors must be propagated through the exact formulas in§3. The existing first-action operator bound ||H_A||≤6h controls a separately certified nearby-frame action error by6h times frame error. It cannot replace the missing C or leakage certificate.

Compression remains on ORIGINAL F. Its original trace/residual and Ward insertion estimates remain valid without inflating their domain to402 columns. The DATA trace536 is used here only for a common factor/error bound. A future action append runtime must bind accepted mu and existing scalars, preserve all rows on failure, and certify arithmetic gates. No actual append or claim of attained conditioning is made.


## Exact pivot coordinates


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


## Sparse support and action


Status: conditional-support, source-only. The supplied native carrier, exact paired pivot recurrence and first-action formulas are provisional reviewed inputs. This note computes no native pivot, entry, coefficient or leakage. The physical law and alpha remain open.

Let F have the original399 raw columns and their Gamma partners, and let Z add the three bare qA,qC,qD sources and partners, for804 DATA columns. V=F C is the exact ideal isometry formed from k accepted paired pivots, as in the coefficient recurrence0639bb7f. A pole half-column seed has exactly two raw coefficients; an appended insertion seed has one. Take S to be the union of raw coordinates appearing in the selected seeds, and R=S union Gamma(S). The coordinate-space Gamma is a signed permutation. Thus |S|<=2k and |R|<=4k.

The recurrence beta_h=s_h-sum beta_a*g_ai/r_a+sum Jc beta_a*j_ai/r_a proves inductively that beta_h, Jc beta_h and all normalized C columns have support in R. This is an exact structural zero statement independent of rounding. Fixed outward interval implementations can keep absent coordinates identically zero. This is stronger than treating C as a dense798-row array and then discovering small entries.

Let Q={x0,qA,qC,qD,Gamma x0,Gamma qA,Gamma qC,Gamma qD}. The free K action on a selected pole coordinate is its scalar multiple plus a source in Q. On x0,xA,xC it gives qD,qA,qC; their Gamma copies follow by commutation with free K. The impurity correction maps every vector to span{x0,qA} for A, or span{x0,qC} for C. In particular this correction is not assumed to commute with Gamma. Consequently H_A V and H_C V lie in span Z_U, where U=R union Q and |U|<=4k+8, also <=804.

Only the principal Gram M_U=Z_U^T Z_U is needed. Pad the coefficients C_R into U. Compute the free action coefficients on R and add the correction8[x0(qA^T M_U C_U)-qA(x0^T M_U C_U)] (and C analogue); call the result B_U. Then

 A_V=i C_U* M_U B_U,
 G_action=B_U* M_U B_U,
 L=G_action-A_V^2 >=0.

These are the same exact original-domain identities as the804 DATA formula. They use a principal restriction containing the entire original support and its first-action image; no discarded couplings enter either scalar product. No second action H_A Z_U is required, and no large inverse or full804-square contraction is required. To enclose L, every used M_U, source scale and pivot coefficient must refer to the same accepted physical inputs, with outward arithmetic and coefficient conditioning gates. Restricting support does not remove those uncertainties or prove small leakage.

For the four-pair pilot, |R|<=16, |U|<=24 and V has at most8 columns. At most24*25/2=300 upper-triangle real closed-Gram requests per orbit suffice for M_U, or1500 across five orbits. These are requests to a physical-inflated immutable reader, not a claim about distinct underlying cached raw reads or wall time. Symmetry reconstructs the other triangle. An absent pivot contributes no selected seed; an early stall only reduces the support. Keeping Q when k=0 is harmless but no action need be evaluated. General continuation uses the authenticated cumulative selected seed set and never recomputes completed pivot rows.

The bounds are worst-case support counts. Coincident coordinates, exact chiral zeros and common scalar data can reduce cost further; no reduction is assumed in these ceilings. The complete DATA append may still be generated once for easy validation and reuse, while downstream contractions request only this small submatrix. This is a concrete sparse implementation route, not an achieved computational or physical certificate.


## Adapter, arithmetic and remaining obligations

Raw pole ordering is6n+[minus three,plus three], whereas pilot half labels use6n+2source+eta. The adapter must query raw G/J, not the half Gram a second time. The closed Gram is[[G,J],[-J,G]]. New q sources have negative chirality; raw poles are not individually chiral eigenvectors. The rank-two impurity does not commute with Gamma. The free generator does.

Accepted midpoint intervals receive physical input inflation once: new-pole G2800etaA and J176etaB+etamu; new-to-Ward Gzero and Jeta_c/2+eta_mu/4; new self is exact rational geometry. Old block inflation remains as imported. Immutable source indexes require same-descriptor initial/row/final hashes and finally verification on both success and failure. These conditions are necessary input obligations, not consequences of a hash alone.

For at most eight columns, C support≤16 and action support≤24. T contractions cost at most64*16*24 summands per impurity; action Gram at most64*24². Across two impurities and five orbits this is614400 main summands, refining the earlier loose737280 ceiling. Coefficient, correction, T², indexing, hashing and I/O remain additional. Neither count is measured timing. The source candidate has320-bit endpoint, positive-denominator, l1 and width guards; failure is indeterminate. Its native entry point remains disabled until an authenticated runtime contract exists.

## Bounded execution history, not a leakage result

The fixed four-pair pilot completed all five orbits, each with status PAIR_CAP. It did not meet the compression target and supplies no leakage or propagation result. The three-q append completed6015 midpoint G/J entries in2010 rows; its combined DATA arithmetic gates passed and the exact extra closed trace is5. These are recorded bounded execution snapshots, not a portable rerun of their native arithmetic. The canonical runner does not replay those arrays or infer physical-input containment from receipt existence.

The packet preserves source/result hashes and root receipt snapshots. Durable campaign archive commit33f95bf79536021cf09f524c55acf8df5430dfae contains preregistered source and prior campaign evidence; new output archival and saved-post reconciliation are separately tracked by root. Raw arrays are not silently declared portable inputs here. Any twelve-pair extension, actual C certificate, actual DATA action and leakage remain outside this frozen milestone until separately accepted and reviewed.

## Supporting portable controls

The standard-library runner checks exact rational paired projection signs, Gamma-square, dense tiny rank-two action, sparse dimension/count identities and selected seven-site contractions. These are small supporting controls of the analytical identities, not finite-example proof of the infinite model or native numerical replay. It verifies all declared local proof/source recovery hashes. Failure outputs and source revisions are preserved; no retained audit status follows from PASS.
