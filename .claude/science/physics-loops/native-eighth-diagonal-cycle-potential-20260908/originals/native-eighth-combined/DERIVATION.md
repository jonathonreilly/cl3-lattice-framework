# Combined full-carrier eighth diagonal: exact coefficients and remaining identities

This combines the frozen local table af417f5c with the independently frozen root motif argument751543dd. The root global argument was read before this coefficient calculation; this is independent arithmetic and formula inspection, not a blind discovery of its combinatorial mechanism. No canonical files changed.

## Tree scalar

Use the parent's motif formulas, retaining the local helper's fork order: edges0,1 are leaves at the degree-three vertex, edge2 is the internal edge, edge3 is the final leaf. This order matters when reading the nonconstant fork table.

The contributions per vertex are

|Support|Coefficient|
|---|---:|
|one edge|15/128|
|two-edge path|525/64|
|three-star|225/8|
|three-path|6479/150|
|four-star|225/16|
|fork|10091/120|
|unrestricted four-step path count|191387/4000|

Their sum is C_tree=3610233/16000. Binomial counts suppress locally unextendible four-star patterns. Fork counting excludes the internal edge at each endpoint; a would-be leaf collision would require a triangle, absent here. Nonbacktracking paths of length<=3 are simple; length4 can only fail simplicity by closure into a four-cycle. Reversal divides path counts by two. Thus the actual path correction per unoriented cycle is the sum of its four rotated path weights, not eight.

With uniform magnitudes, in the canonical direct-rotation convention, the complete diagonal coefficient supplied by this cluster reduction is

E8_diag(x)=N*(3610233/16000)+sum_C W(b_C).

Restore the common eighth coupling power and U^-7. C includes all simple four-cycles, including straight winding cycles in directions of extent four. This statement concerns the diagonal only and does not compute the full eighth-order effective operator.

## Cycle weights and exact decomposition

The four rotation/reflection/complement classes have W values

|Class|W|
|---|---:|
|all equal|−99/1600|
|one or three occupied|−10019/108000|
|two adjacent occupied|−11/144|
|alternating|5/32|

All sixteen inputs were checked under four rotations, reflection and complement. Define d_C as the number of adjacent unequal bit pairs around the cycle, P_C=product_(e in C)(1−2b_e), and F_C as its alternating indicator. Exact linear elimination gives

W=−7567/108000 −(209/28800)d_C +(1769/216000)P_C +(3559/14400)F_C.

The helper verifies this equality for all16 patterns. Unequal nonalternating weights do not alone prove that the global sum cannot simplify to a scalar plus flippability.

## A global domain-wall identity

At any degree-six ice vertex, three incident edges are occupied and three are empty, so exactly nine unordered incident edge pairs have unequal bits. Each perpendicular incident pair belongs to exactly one elementary plaquette. A collinear opposite pair belongs to a simple four-cycle precisely when that coordinate extent is four; that cycle is the straight winding cycle. No other four-cycle passes through that pair on these simple cubic tori.

Therefore, with all simple four-cycles counted,

sum_C d_C=9N−sum_v sum_(axes a with L_a>4) 1[b_(v,a,+) != b_(v,a,−)].

For the all-L4 torus this is exactly9N. For all extents>=6 the last term contains all three collinear pairs at every vertex and is not eliminated by degree-three counting alone. Mixed extents obey the same formula with the indicated subset.

Even on L4 the sum of P_C remains in the decomposition. Multiplicative cube/Bianchi constraints on P_C do not by themselves make its additive sum constant or a known affine function of total F. This note does not assert irreducibility, since that needs a further analytical identity or explicit globally admissible separating witnesses. Root is checking deterministic full ice backgrounds separately. The exact formula above is already usable without resolving that question.

## Evidence scope

112 exact arithmetic predicates confirm table symmetries and the four-invariant decomposition. The scalar was assembled from exact binomial/path counts and the frozen table, not fitted to global configurations. The general global formula relies on the stated canonical cluster support and linked additivity argument, not on these112 finite predicates. No RK-point selection, phase, physical coupling or dynamical conclusion follows.
