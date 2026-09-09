# Sparse first-action contraction for a paired pivot frame

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
