# Independent same-edge native/ice compatibility check

## Precisely retained hypothesis

Take a connected periodic cubic graph of even sideL>=4, one physical qubit per graph edge, and identify the ice occupation literally with n_e=(1−Z_e)/2 on those SAME qubits. Impose the complete native fixed-cycle BKSF code, with no deleted edges or extra unfixed cycle degrees. These are restrictive supplied identifications, not primitive axioms. Main native instrument note lines97–193 supplies B_v=product incidentZ, T_ij=iA_ij(B_i−B_j)/2, independent fundamental-cycle constraints and free/transitive cycle action on each incidence fiber. Targeted main ICE/BKSF phrase searches did not locate this specific overlap bound; this is not exhaustive repository/open-PR novelty certification.

## Exact intersection and frozen native hopping

Ice degree3 implies B_v=−1 at every vertex. Consequently (B_i−B_j)Pice=0 and every native hopping operator T_ij Pice=0, as an ambient operator identity. It is not a statement about the ring-flip ice Hamiltonian.

For connected graph, the Z-basis strings with fixed vertex parities form an affine binary cycle-space coset of dimensionE−V+1. Its all-odd constraint is consistent since V is even. Each fundamental-cycle check is a monomial Pauli operator whose X support is that cycle; fixing all independent checks leaves one vector in each allowed B fiber. Their free transitive permutation action forces equal coefficient moduli on the whole coset, regardless of stabilizer sign phases. This uses full cycle fixing, not merely local plaquette checks that omit winding cycles.

The seed n_a(r)=r_a mod2 is an ice string. Its xy plaquette rooted at0 has four empty edges. Flipping those four bits keeps every vertex incidence odd but raises the four touched degrees from3 to5, hence leaves ice. This is a cycle-space translation even though it is NOT a legal alternating ice move. A nonzero native vector in the all-Bminus fiber must include this nonice string with nonzero modulus. It therefore cannot lie entirely in the ice span. Since Pice selects only this B fiber, intersection(code,ice)=0. No claim that the projectors have zero overlap is made.

## Quantitative projector overlap

Let S contain vertices with all coordinates even; k=V/8. Their six-edge stars are pairwise edge-disjoint. The induced graph after removing S is connected. One proof: any remaining vertex has at least one odd coordinate. If x is odd it lies on an entire connected yz plane avoiding S; if x is even, keep an odd y or z while stepping to an odd x plane. Odd-x planes connect through intermediate even-x planes along a route with y odd. This also covers periodic seams for L>=4.

Assign an arbitrary odd six-bit pattern to each selected star:32choices/star. The remaining incidence equations on G\S are solvable iff the total residual parity is even. The prescribed odd degrees on V−k remaining vertices plus k odd star incidences have total parityV, hence even. Because G\S is connected, every such assignment has exactly2^[E−6k−(V−k)+1] completions. Therefore under the uniform all-odd fiber measure, selected star patterns are independent and uniform among32choices. Exactly binomial(6,3)=20 meet degree3. Ice requires this at every selected star, so

  probability(ice | all-odd fiber) <= (20/32)^k = (5/8)^(V/8).

The native projector commutes with allB projectors. Only its rank-one all-Bminus block contributes to Pice Pnative. Thus

  ||Pice Pnative||² = probability(ice | all-odd fiber)
                     <= (5/8)^(V/8).

For a native normalized state this bounds the probability of projection into literal ice. It is not a bound on all alternative encodings. For L4/6/8 the independent graph check verifies disjoint stars, complement connectivity, the empty-face nonice cycle translation and completion exponents89/298/705; no full Hilbert matrices or L2 census were run.

## Scope and escape routes

No counterexample to the scoped argument found. Missing full cycle constraints, a tree graph, different operator identification, deleted-edge/record sectors, distinct qubit roles or additional carriers alter the hypotheses and require their own analysis. The two supplied models can coexist on different carriers. This proves incompatibility of one literal simultaneous identification and exponentially small projection probability, not impossibility of native/gauge unification, an axiom-derived model choice or a universal no-go. Main midpoint placement is a separate physical-locality issue; the result assumes the proposed same abstract edge-role correspondence and does not silently identify graph adjacency with fine-site nearest neighbors.
