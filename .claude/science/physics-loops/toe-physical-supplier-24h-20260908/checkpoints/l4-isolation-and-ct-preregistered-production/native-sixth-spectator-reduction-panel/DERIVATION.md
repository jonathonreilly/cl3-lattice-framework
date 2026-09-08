# Independent sixth-order spectator reduction panel

The supplied actual uniform L4 endpoint and its proved full-space gap delta=|t|/432 are imports. Read the complete new DESIGN before controls, without author implementation reuse. This is a reduction/error-analysis result, not a sixth-order coefficient calculation.

## Common active subspace

Let J=K0/(sqrt24 |t|), so J²=-I. For S consisting of the adjacent centers and all their neighbors, W=span(E_S,J E_S) is invariant under J, hence has even dimension. Its orthogonal complement is invariant as well. Every changed hopping matrix differs from K0 by sums of antisymmetric rank-two operators supported at endpoints in S. Such differences annihilate W-perp and have image in W. This proves simultaneous invariance for every prefix, not merely the final support. Independent rational rank computation gives dim W=20 for centers0,16, so m=10. The complement remains in its32-10=22-mode vacuum and contributes -11 omega. Thus the reduced denominator is precisely -5 omega-H_F,W; dropping the complement energy would be wrong.

A once-chosen oriented Clifford frame factors the vacuum and fixes all closing signs. In the unreduced link-X representation the insertions are matter identity and all intermediate Hamiltonians are even. The initial active parity is therefore preserved. Only its512-dimensional block is needed, though constructing W still requires both real halves of each complex mode. Re-gauging after each prefix is possible but then the intertwining gauge parity operators must be retained; projecting every re-gauged state onto the original even active sector would be incorrect.

## Complete bridge supports and denominator invertibility

Independent literal L4 construction confirms ten boundary edges, twelve vertices and exactly six possible repeated bridge edges. One is the internal bond, four are opposite edges of elementary squares through it, and one is the opposite edge of its length-four winding. A repeated boundary edge cannot connect the two odd incidence classes. No repeated outside edge whose endpoint fails to meet both classes can fix their odd counts. Thus this list is complete for the adjacent-cut monomial at six insertions.

A dynamic traversal with boundary usage0/1 and bridge usage0/1/2, allowing only distinct incident edge pairs, counts all ordered words independently:162000 for the internal bridge and6480 for each of five others, total194400. It checks every reachable proper prefix has nonempty toggle and, whenever that toggle is a cut, its vertex subset has odd cardinality. This agrees with the arbitrary-subset cut theorem; the finite traversal does not replace that theorem.

For a proper prefix in a different flux orbit, the full-H0 isolation theorem bounds every denominator away from zero by delta. For a prefix gauge-equivalent to the starting orbit, the cut is odd. Its gauge transformation changes active parity, so the gauge-transformed active vacuum is in the opposite block. The retained parity block has no ground pole (indeed its distance is at least omega). Thus ordinary inverses on this fixed block equal the required reduced resolvent for these particular monomials. This does not authorize ordinary inverses in a general electric word: empty-toggle or even-cut returns would need Q.

## Canonical terms

Write A=P Pi P and C=P(H-E0)Pi P. Their coefficients through five are scalar on the full spectator ground space. Since C0=0, multiplying A^(-1/2) C A^(-1/2) changes its nonscalar sixth coefficient only by products of lower scalar coefficients. Intermediate P pieces in the contour expansion split the six insertions into shorter returning words, each scalar under the proved selection theorem, including higher resolvent powers. Therefore the nonscalar adjacent-cut sixth coefficient can be obtained from the irreducible six-insertion chain. This argument concerns the full coefficient sum; it would not justify deleting folded pieces while computing its scalar part.

The constant3N/2 in D can be subtracted exactly as a scalar energy shift. The remaining pair terms each carry1/2, so six insertions give1/64. In the unreduced gauge every insertion is identity on the active vector, but changes which K_F enters the next inverse. Sum predecessor vectors first and apply that state's inverse once. The final state has no resolvent: it is closed with the fixed Gauss operator P_v P_w. With bar-gamma=i(c†-c) and P_v=-i gamma_v bar-gamma_v,

P_v P_w=gamma_v gamma_w bar-gamma_v bar-gamma_w
       =-(i gamma_v gamma_w)(i bar-gamma_v bar-gamma_w).

Consequently a coefficient quoted relative to i bar-gamma_v bar-gamma_w must retain this minus sign and the active i gamma_v gamma_w matrix element. A scalar overlap without the active closing bilinear is not the desired coefficient. Orientation of v,w must be fixed once. This is a particularly useful independent normalization check before a large solve.

## Certified solve and DP error route

Every relevant inverse has operator norm at most1/delta. If a computed vector xhat solves A_s x=b with residual r=b-A_s xhat, then ||x-xhat||<=||r||/delta. This uses the actual physical Hilbert norm, not an unweighted coordinate norm in a nonorthogonal basis. For predecessor errors e_j and insertion coefficient1/2, a safe propagated bound is

e_s <= delta^(-1)[ (1/2) sum_j e_j + ||r_s|| ].

If the matrix is approximated, add ||A_s-Ahat_s|| ||xhat_s|| inside brackets, and include any RHS representation error. Final contraction has norm one and propagates the weighted predecessor errors without another inverse. The triangle sum over six bridge families is conservative but valid. A resulting interval separated from zero would certify a nonzero coefficient; an interval containing zero would not certify cancellation. Conditioning may make this too costly, which should be measured rather than assumed away.

A proof-friendly basis alternative avoids uncertified numerical orthogonalization. The positive-frequency projector of J has entries in Q(i,sqrt6). Select ten independent projected endpoint vectors exactly; their positive Hermitian Gram matrix and exterior-power Gram determinants specify a nonorthogonal Fock basis over that field. CAR contraction uses the inverse Gram matrix. The corresponding matrix representation can be exact algebraic; numerical solves, if used, must certify its metric and residuals. This is a proposed implementation route, not an already implemented512-dimensional solver.

No missing canonical nonscalar term is identified in the author's design under its stated premises. The remaining genuine task is to evaluate and certify the full six-bridge sum with actual closure signs. The194400-word count alone supplies neither a coefficient nor cancellation. No large solve, random fixture or performance profile was run here.
