# Three-source first-action DATA augmentation

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
