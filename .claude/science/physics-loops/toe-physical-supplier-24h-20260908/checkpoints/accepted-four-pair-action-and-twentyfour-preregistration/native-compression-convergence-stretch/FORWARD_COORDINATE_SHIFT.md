# Dense shift from saved forward coordinates — UNREVIEWED optional extension

This is a future candidate-selection route. It changes no frozen zero/diagonal plan and uses no actual saved C/history/Gram here. Same accepted rational-midpoint family F, exact ideal paired V=FC, Gamma-invariant projection P and authenticated saved rows are prerequisites.

## 1. Recover V*F_R without a new original Gram call

For saved pair a, V columns are b_a/sqrt(r_a), Gamma b_a/sqrt(r_a). The saved physical residual rows are g_ai=<b_a,f_i>, j_ai=<b_a,Gamma f_i>. Thus the forward coordinates of half seed f_i are

 (g_ai/sqrt(r_a), -j_ai/sqrt(r_a)).

For its Gamma partner the pair is (j_ai/sqrt(r_a),g_ai/sqrt(r_a)). The minus sign in the second coordinate of f_i is necessary. These are exactly the existing forward coordinate objects, not inverse coefficients beta/sqrt(r).

For a pole/source with chirality sign chi, f_eta=(z_plus-eta*chi*z_minus)/2. Hence

 z_plus=f_-+f_+,  z_minus=chi*(f_--f_+).

Apply these sums to every saved forward-coordinate pair. Original insertion x uses its own half label directly. Decode ORIGINAL raw399/Gamma coordinates before DATA402 offsets. The Gamma partner of any raw column with pair coordinates(a,b) has(-b,a). This determines A_R=V*F_R for all selected raw/Gamma support R, requiring O(ps) sums once authenticated coordinates are available, not old native entries. If only g,j,r are retained, positive-root interval normalization adds O(ps) divisions/roots and must retain its conditioning bounds.

For exact midpoint coordinates transformed without extra rounding, the old weighted coordinate error d² bounds the raw forward-coordinate Frobenius error: the plus/minus transform obeys the parallelogram identity, yielding precisely weight2 per half pair and weight1 per insertion. Adding Gamma partners duplicates that squared error, so the closed-family bound is≤2d²; restriction to R cannot increase it. Independently rounded transformations require an additional explicit rounding bound. One may simply retain transformed coordinate intervals instead of relying on this global estimate.

## 2. Exact ideal dense candidate and its limited optimality

Let Lambda be the free scalar diagonal from the previous decomposition. Define

 Z_free=A_R Lambda C=V*F_R Lambda C.

Then F_R(Lambda C-CZ_free)=(I-P)F_R Lambda C. It removes the exact in-frame component of the free scalar-diagonal term. It minimizes the physical Frobenius norm ||F_R Lambda C-VZ|| over all Z (orthogonal decomposition); operator norm is also minimized in the weak sense that projection is contractive and the residual attains the unavoidable projected lower bound. Operator minimizers need not be unique.

This does NOT prove that Z_free minimizes a weighted coefficient norm of Lambda C-CZ, or that its row-triangle certificate is smaller than Z=0. F_R may be ill-conditioned. The final certificate must compare the rigorous candidate bounds and may select the best valid one. The source Q term remains untouched and is still bounded via Q*(I-P)Q and Y_A. Z_free is generally NOT skew: Lambda is a coordinate diagonal, not by itself the physical K0 action. Do not apply a false skew-symmetry intersection to this matrix.

With exact paired coordinates, A_R J_R=J_p A_R, J_R C=CJ_p and Lambda J_R=J_R Lambda. Thus Z_free commutes with J_p. Its2×2 pair blocks have form[[a,-b],[b,a]]. This is a complex-linearity constraint, not skew-adjointness. The complete compressed free K additionally includes A_QY0, and then is real skew; full impurity compression need not commute with the reference Gamma. No such identity is needed merely to choose a candidate shift.

## 3. Avoid certifying the candidate-selection inverse

No least-squares solve is necessary. Use exact dyadic midpoints of saved forward intervals and candidate inverse-coordinate intervals C, the exact rational Lambda of the accepted family, and form

 Z_hat = round_dyadic(A_mid Lambda C_mid).

Once written, Z_hat is an arbitrary fixed rational matrix. The identity (I-P)F_R C Z_hat=0 holds exactly for the true C regardless of how inaccurate Z_hat is. Therefore candidate selection need not enclose Z_free or propagate its error as a new physical error. The final X=Lambda C-C Z_hat MUST still be evaluated outward using the full certified C and Lambda intervals, with Z_hat treated as that fixed rational. A poorly selected candidate enlarges the bound; it cannot falsify it. This prevents double-counting candidate uncertainty. Never replace true C by C_mid in the final residual expression.

Exact rational candidate products are simplest. A floating candidate is also mathematically just a finite dyadic choice after exact conversion, but any implementation would still need finite/overflow/resource guards and complete retention. This note specifies no floating kernel. It supplies no exemption from the coefficient positivity/width/l1 certificate.

## 4. Cost and falsifiable comparison

Form A_R from saved forward coordinates in O(ps). Dense candidate product costs p²s scalar products, and final outward CZ_hat another p²s. At k24, s≤96,p≤48, each is221184 summands per orbit; at k12 each is27648. Plus midpoint/rational rounding and retained p² candidate entries, this is small compared with479232000 direct-action summands across all cases. These are counts, not timing. There are zero new original Gram requests for A_R; the already proposed M_RQ/M_QQ requests for the Q residual certificate remain necessary.

A future fixed experiment can compare Z=0, paired diagonal shifts and this saved-forward dense candidate at identical physical input widths, C intervals and leakage target. Retain candidates and free/source upper contributions separately. The route is falsified as a practical improvement for that case if its certified bound is not smaller, or arithmetic/bit limits fail. That is not a theorem that no other candidate works. Do not retune physical targets or alter the already frozen fixed-candidate protocol retrospectively.
