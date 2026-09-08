# Exact charge-position reachability, and a separate configuration-connectivity gap

Premises are the supplied low-charge full-edge-carrier model on a periodic cubic graph whose three extents are even and at least4. The initial configuration has exactly one positive and one negative Q. No fixed winding constraint is imposed. Native hopping preserves these signed charges and follows the electric orientation as previously derived. This proof concerns nonzero matrix-element support, not quantum transport speed or preparation.

## Six-edge cut lemma

For a nonempty proper vertex set B, let b_a be the number of cut edges parallel to coordinate a. Every periodic coordinate fiber crosses the cut an even number of times; a mixed fiber contributes at least2. If all three b_a are positive, the cut has at least6 edges. Otherwise b_a=0 for some directiona, so membership in B is constant along every a-fiber. Any cut edge in another direction therefore repeats along all L_a>=4 translated copies, giving at least4 such edges; parity within each perpendicular fiber gives at least2L_a>=8 altogether. Some direction must have a cut edge because the Cartesian graph is connected. Hence every nontrivial cut has at least6 edges. A singleton attains6. This is a direct fiber argument, not an imported connectivity theorem.

## Positive charge can avoid the fixed negative charge

Orient an edge out of v when epsilon_v(2n_e-1)=+1. Its outdegree is3+Q_v:4 at the positive chargep,2 at the negativem,3 elsewhere. Let R be vertices reachable from p in this directed graph after removing m. Suppose B consists of some remaining vertices outsideR. There is no directed edge R->B. All B vertices are neutral, so total outgoing-minus-incoming flow across its edge cut is zero. Its incoming edges can come only from m, which has outdegree2. Therefore its total cut has at most4 edges, contradicting the six-edge lemma. Thus R contains every vertex exceptm.

Choose a directed simple path from p to any target other thanm. Sequentially flip its edges. Each step moves Q=+1 to the next neutral vertex. Earlier path edges have been reversed, but simplicity means the next edge has not been changed. Every prefix stays in D2 and leaves m fixed. These are actual permitted nonzero native hopping entries; phases do not affect support. Reversing all arrows and interchanging the charge signs proves the same statement for moving the negative charge while holding the positive fixed. Each simple path has at mostV-2 edges.

Any desired ordered pair of distinct final positions is therefore reachable. If the desired positive site equals the current negative site, first move the negative to a spare vertex different from the positive and its target; then move the positive, then move the negative to its requested target. Otherwise two moves suffice. This gives at most three simple-path operations, not a mixing or shortest-path claim.

## A constructive subset of configuration changes

At fixed charge positions, the difference between two link orientations with the same Q decomposes into directed cycle reversals in the first orientation: each vertex has equally many changed incoming and outgoing edges. This decomposition alone does not make each cycle a legal native plaquette sequence.

A directed simple cycle avoiding the negative charge can be reversed by positive-charge hopping while restoring its original position. Find a directed path from the positive to the cycle, stopping at its first cycle vertex; it avoids the negative by the reachability theorem and is internally disjoint from the cycle. Move the positive along this path, once around the directed cycle, and back along the now-reversed access path. The cycle edges were untouched by the access path and the return path is disjoint from the cycle. Net change is precisely the cycle reversal. If the positive already lies on the cycle, the access path is empty. The negative analogue handles cycles avoiding the positive charge.

This establishes more than position reachability, but it does not complete all-D2 configuration connectivity. A difference cycle can contain both charges. Neither preceding cycle traversal can pass through the other charge. Temporarily moving that charge can change edges of the desired cycle or its restoration path, so simply asserting conjugation is insufficient. No general decomposition into cycles avoiding at least one charge is proved here, and no full-connectivity claim is made. Plaquette ring moves may help, but their legal alternating conditions must be respected rather than replacing them by freely allowed cycle flips.

The open obligation is therefore precise: construct a legal D2 sequence reversing an arbitrary directed difference cycle containing both charges, or find an invariant separating configurations despite the proved position mobility. Equal signed-position support and staticzero ring energy are not substitutes for this argument.
