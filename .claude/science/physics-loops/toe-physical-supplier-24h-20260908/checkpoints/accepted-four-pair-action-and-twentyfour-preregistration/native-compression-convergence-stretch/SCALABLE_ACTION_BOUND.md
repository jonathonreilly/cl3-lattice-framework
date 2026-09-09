# Cancellation-aware sparse residual certificate — UNREVIEWED

Source-only extension of52502. No saved C, Gram, native entry, solve or runtime was evaluated. This proposes a cheaper sufficient certificate, not a claim it passes. All vectors use the SAME exact rational-midpoint family and authenticated ideal paired C. Gamma closure and physical interval premises are unchanged.

## Exact decomposition with eight source columns

Write F_R for original closed columns on selected support R, s=|R|≤4k; C is s×p, p=2k, and V=F_R C is the exact ideal isometry. Let Q contain x0,qA,qC,qD and their Gamma partners (eight columns). Overlap between R and Q is harmless. The first action has

 K_A V=F_R Lambda C+Q Y_A.

Lambda is sigma*s on pole coordinates and zero on insertion coordinates. For the free source part of Y, each pole coordinate contributes−2sqrt(alpha) to its corresponding x0,qA,qC source with the SAME Gamma bit, and each x0,xA,xC coordinate contributes to qD,qA,qC with the same bit. These operations are linear sums of C rows. For the impurity add8 e_x0 (qA*V)−8 e_qA (x0*V); for C replace qA by qC. Only the untransformed Q rows occur in this correction. There is no assumption that DeltaK commutes with Gamma.

Let A=V*Q=C* M_RQ and G_Q=Q*Q−A*A. Then G_Q=Q*(I-P)Q≥0 exactly. Its computation needs only M_RQ and M_QQ, not M_RR. C is not certified by a midpoint inverse: the ideal-isometry premise is supplied by the authenticated exact paired recurrence.

## Exact null-direction cancellation

For ANY p×p matrix Z, (I-P)F_R C Z=0. Therefore, putting X=Lambda C−CZ,

 (I-P)K_A V=(I-P)F_R X+(I-P)QY_A.

Z is a freely chosen numerical candidate, not a physical input. It may be rounded dyadic, selected from midpoint coefficients or approximate least squares; no assertion that it is the exact minimizer is necessary. Evaluate the final X with outward arithmetic. A dense Z costs O(sp²); diagonal column shifts cost O(sp). Choosing Z=0 recovers the prior bound, so take the minimum of separately valid upper bounds. A bad choice is inefficient, not invalid. It is essential to subtract CZ before taking entrywise norms; replacing it by a triangle of Lambda C and CZ throws away the exact cancellation.

## Recover needed residual diagonals without new native entries

The accepted checkpoint has diagonal residuals for chiral HALF seeds. For each source/pole, z_plus=f_-+f_+ and z_minus=chi(f_--f_+) up to the exact sign convention. Since the ideal paired projection commutes with the physical chirality grading, the two residual halves are orthogonal. Hence the residual squared norm of either raw pole column is the SUM of its two half diagonal residuals. Its Gamma partner has the same norm. Original appended x diagonal is already supplied and Gamma duplicates it. Upper bounds u_i on ||(I-P)F_i||² therefore follow by additions of saved upper endpoints, without old Gram calls. This uses exact chirality and the paired projection; it is not valid for arbitrary unpaired C.

## Two inexpensive free-term bounds

Let X_i denote row i. The triangle and rank-one norm inequalities give

 a_1 = sum_i sqrt(u_i) ||X_i||_2 >= ||(I-P)F_R X||.

All roots can be bracketed by integer isqrt on exact rational/dyadic upper quantities; no floating eigensolver is needed. Complexity is O(sp) once X is formed. Alternatively for arbitrary positive rational weights w_i,

 a_2² = (sum_i u_i/w_i) ||diag(sqrt(w_i)) X||_op².

This follows by factoring RF_R diag(1/sqrt(w)) and bounding its operator norm by Frobenius norm. Its second factor may be bounded by Frobenius norm at O(sp), or by the maximum absolute row sum of X* diag(w) X at O(sp²). Any chosen rational weights are valid. Frobenius-optimal weights formally yield a_1; finite candidate weights avoid division by zero and are checked positive. The operator bound can exploit cross-column cancellation that the row triangle misses.

Choose Z and weights from cheap candidates, then certify the best VALID upper bound. The cost of selecting candidates must be explicitly budgeted; it is not free proof optimization. Severe C growth may still make both bounds useless.

## Source term and final leakage inequality

Keep cancellation among the eight sources by forming the small PSD residual Gram G_Q. Rather than beta_Q||Y||, use

 b_A² = Tr(Y_A* G_Q Y_A) >= ||(I-P)QY_A||_op².

This is a Frobenius bound and costs O(8²p), not a dense action Gram. Compute a rigorous nonnegative upper bound on the trace with outward arithmetic; repeated C/M appearances remain correlated exact inputs and interval over-enclosure remains valid. Proved Hermitian symmetry and nonnegative diagonal intersections may tighten bounds but must reject empty intersections. The true trace is nonnegative; an upper endpoint below zero means inconsistent premises, not successful clipping.

Then delta_A <= min(a_1,a_2,...)+sqrt(b_A²), and similarly C. The bound deliberately drops cross cancellation between the free and source residual terms; failure is inconclusive. It cannot certify a lower leakage bound. If it fails, the direct small L method may still pass, but that is a separate cost decision.

## Quantified source-only work ceiling

M_RQ/M_QQ requires at most8s+36 callback requests per orbit before removing duplicates:164 at k4,420 at k12,804 at k24. These are physical-inflated DATA requests, not underlying disk reads; indexes and hashes remain extra. It needs no full s×s Gram. For k24, s96,p48:

- A=C* M_RQ:36864 triple-product terms.
- G_Q=M_QQ−A*A:3072 terms.
- source Frobenius trace per impurity:3072 terms.
- dense candidate shift CZ:221184 products (diagonal shift only4608).
- optional X*diag(w)X bound:221184 triple terms.

Across five orbits these are a few million bounded interval terms even with dense shifts, versus479232000 for the earlier full direct action contraction ceiling. These counts exclude coefficient formation, Y sums, integer roots, callback inflation and serialization. They justify designing a separately measured cost fixture, not declaring the job fits120 seconds. No physical calls are authorized here and the frozen continuation forecast is unchanged.

## Concrete next certificate experiment

After authenticated saved C exists, a prospective cheap contract can fix Z=0 and a diagonal-shift candidate, one rational weight rule, both impurities and all five orbits. Retain all u_i, exact candidate Z/weights, interval A/G_Q/Y/X and final a,b upper bounds. Preserve the current physical thresholds delta≤h/10^6 (one-particle example) or the separately applicable stronger condition. If no upper bound passes, report INDETERMINATE; do not alter targets, assume source projection small, or infer a native no-go. An independent replay can check the small retained contractions without rerunning pivots.
