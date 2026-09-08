# Independent signed-hole variational review

PASS for DERIVATION.md c13a8d737ebd2cc11511e267f48dd36dc816ad5e1fa13e0d651ac8a64d77f6a8. Full author checker was read after independently implementing occupation-bit CAR actions; no author implementation was imported. The source-defined full W dictionary is a declared premise, not independently reconstructed again here.

With hole creation h†_i=c_i and hole vacuum the completely filled electron state, electron hopping is -h†_j h_i. On the signed order h†_x h†_y|F>, moving either first or second hole gives minus the same signed-order vector at its new position. For the second hole the annihilation crosses the first creation once and reinsertion crosses once, cancelling those two signs. The target cannot be the other hole. Independent bit-CAR controls check1512 such moves for3 through8 modes, including reversed vertex orders. Thus the assertion is not an unsigned occupation-basis assumption. W contributes the exact native phase; the additional signed frame is diagonal in charge positions. Rings preserve positions, so retain their positive flip amplitude. Uniformity over all D2 electric configurations pairs every flippable configuration with its partner, without any ergodicity assumption. Multiplying by epsilon_x epsilon_y reverses hopping but leaves ring terms unchanged for t<0.

The minimum degree6 follows because each of two charged sites has four eligible bits, and only their mutual edge can target a nonneutral vertex. The mean-degree trial therefore proves the original2U-6|t| bound. This is an all-D2 variational state, not an implemented preparation or a fixed-winding trial. It does not remove the model's supplied gates/couplings or imply mobile deconfinement.

## Separate strengthened counting lemma

The proposed36/5 improvement is valid on the stated simple even cubic tori with all extents>=4. Define A precisely as D2 configurations whose two charged vertices are adjacent AND whose mutual edge is eligible at either endpoint. Because their Q signs are opposite and epsilon signs opposite, their G signs agree. Eligibility is therefore simultaneous at both ends. These configurations have degree6; all others have degree8. Adjacent but ineligible configurations must not be called members of A.

A is in bijection with an ice configuration together with one undirected edge: toggle that edge. Conversely, toggling the unique mutual edge of an A configuration restores ice. Thus A is nonempty; no count of ice states is needed. Every A configuration has six allowed hops, all into configurations with nonadjacent charges, since the cubic graph is triangle-free. There are no A-to-A hops.

For a configuration outside A, a hop can enter A only by moving one charge onto a common neighbor of the two current positions. Two distinct vertices on a Cartesian product of cycles of lengths>=4 have at most two common neighbors: a length-two displacement in one coordinate has one intermediate vertex, or two for a length-four wrap; a displacement in two coordinates has two orders; all other displacements have none. Each common neighbor permits at most two candidate charge moves, so at most four incoming-to-A edges exist. Adjacent outside-A configurations have none. Distinct physical edge toggles give distinct configurations and the Hermitian support graph is undirected.

Double counting edges across A and its complement B gives6|A|<=4|B|. Hence |A|/(|A|+|B|)<=2/5 and mean degree=8-2|A|/(|A|+|B|)>=36/5. Therefore

    E_D2 <= 2U-(36/5)|t|.

Together with the existing lower bound:2U-8|t|<=E_D2<=2U-(36/5)|t|. In the stable region the global reference is E0=0. Separately U<(18/5)|t| makes the trial negative and excludes the neutral zero states as global grounds. No optimal threshold or ground-sector classification follows. The common-neighbor step is geometry-specific; this argument is not asserted for arbitrary bipartite graphs or other charge sectors.

Independent finite geometry controls checked triangle freedom and maximal common-neighbor count2 on4x4x4,4x4x6,6x6x6. These support the elementary general geometry proof, not a D2 census. All scope and resource outputs are in RESULT.json. No stochastic production, main edit or PR mutation occurred.
