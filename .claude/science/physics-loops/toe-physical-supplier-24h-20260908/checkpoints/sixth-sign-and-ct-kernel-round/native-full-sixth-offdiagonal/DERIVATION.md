# Full-carrier sixth-order offdiagonal mechanism

## Scope and convention

Use the supplied full H=UD+g sum_e lambda_e A_e on a simple bipartite degree-six cubic torus of even extents at least four. There is no low-charge projection. The global formula below assumes uniform coupling magnitude, with individual real signs retained in the native product. All effective coefficients use the canonical direct rotation; this is not a transfer to an arbitrary local normal form.

For an unoriented simple even cycle C, choose a traversal e0,...,e_(k−1), and define B_C to act as the alternating-cycle indicator times the sequential product A_(k−1)...A_0, with any chosen actual canonical edge signs included. Its reversal has the same product for even k: reversal contributes (−1)^k from the k incident anticommuting pairs. A cyclic shift likewise crosses two incident neighbors and changes no sign. Thus B_C is well-defined independently of traversal start/direction, is Hermitian, and toggles the cycle only on alternating inputs. This is an explicit native-product convention; converting to the parent's oriented S_C requires retaining its orientation and i^k factor. No universal sign is inferred after discarding that conversion.

For all positive coefficients in this canonical-A convention, the sixth offdiagonal coefficient is

(g^6/U^5)[−(43/6) sum_(C4) B_C4 −(3/8) sum_(C6) B_C6].

For uniform magnitudes lambda and arbitrary signs, include lambda^6 times the product of the signs on the toggled cycle in each B_C. Repeated-edge signs square to one. The result concerns only offdiagonal entries between ice strings. It combines with the parent's sixth scalar only in this same canonical convention. No phase or thermodynamic conclusion follows.

## Completeness of transition support

Between two ice configurations the toggled edges have balanced occupied and empty incidences at each vertex. Their nonempty support is therefore an alternating Eulerian subgraph. At order six its size is even and at most six. A simple bipartite graph has no two-cycle or triangle; the minimum nonempty support is a four-cycle. A six-edge Eulerian support must be a simple six-cycle: any decomposition into more than one cycle would require at least eight edges. This argument also excludes repeated-vertex figure-eight transitions at this order.

Consequently, six distinct flips give a simple six-cycle. Four-cycle transitions have the four changed edges used oddly and exactly two additional uses: either one cycle edge is used three times, or an extra edge is used twice. All six-cycle geometries have the same abstract active cycle algebra and energy function. This includes planar rectangle perimeters, nonplanar hexagons, periodic winding examples and any other simple six-cycle; a geometrical list is unnecessary once all simple cycles are included. Inactive chords do not alter the fixed-exterior degree deviations or active-edge commutation signs.

An extra edge for a four-cycle is either incident to one cycle vertex or vertex-disjoint. It cannot connect two cycle vertices: adjacent endpoints would duplicate an existing edge, while opposite endpoints lie in the same bipartition. Each cycle vertex has four external incident edges, giving sixteen distinct spokes. On an alternating ice cycle exactly one occupied and one empty cycle edge meet each vertex; the four external edges comprise two occupied and two empty. The local spoke coefficient below is identical for either bit, so its embedding sum is uniform.

## Canonical two-dimensional recursion

For an alternating C4, with or without one spoke, let P project onto the two fixed-exterior ice states, Q=I−P and D_Q>0. Let chi: P→Q be the graph wave operator, with Omega=P+chi and P Omega=P. Invariance H Omega=Omega H_B gives, since PVP=0,

D_Q chi+g QVP+g QVQ chi−g chi PVQ chi=0,
H_B=g PVQ chi.

At coefficient n,

chi_n=−D_Q^-1[delta_(n1) QVP+QVQ chi_(n−1)−sum_(a+b=n−1;a,b>=1) chi_a PVQ chi_b].

The first term involving chi0 is omitted. This exact triangular recurrence includes the folded feedback terms. The isometry Omega M^-1/2 with M=I+chi†chi has positive P overlap, hence is the canonical direct-rotation column. Its effective Hamiltonian is

H_eff=M^1/2 H_B M^-1/2.

This direction follows directly from Omega†Omega=M and H Omega=Omega H_B; it is not guessed from Hermiticity. Exact binomial series through sixth order suffice. The finite helper separately checks the graph equation, inverse metric product and Hermiticity at every retained degree. At this order M2 is scalar, so these particular fixtures cannot discriminate the inverse similarity direction merely by their final sixth matrix; the algebraic isometry derivation supplies that obligation.

For an isolated alternating C4 the canonical matrices are H2=−2I, H4 with diagonal3/2 and offdiagonal1/2, and H6 with diagonal−5/2 and offdiagonal−3/2. With one spoke, either initial spoke bit gives H6 diagonal−97/24 and offdiagonal−89/48. Subtracting the isolated C4 result leaves the connected spoke correction −17/48. Other proper subsets cannot realize the same C4 transition, so no further offdiagonal inclusion-exclusion terms occur.

A vertex-disjoint edge factorizes from the cycle. The low isometry is the tensor product of the two positive-overlap canonical isometries, and its effective Hamiltonian is the sum of the factors. Thus mixed disconnected offdiagonal coefficients vanish, rather than producing an extensive correction to a local ring. Sixteen spokes then give −3/2+16(−17/48)=−43/6.

## Leading six-cycle coefficient

Any nonempty proper subset of a simple alternating cycle has an endpoint of degree one in the toggled support, and hence nonzero D. A six-distinct-edge history therefore never returns to P before its last step. Folded terms cannot contribute to this monomial. The amplitude is the sum over all720 permutations of the native product matrix element divided by the five negative full-D intermediate energies. The exact sum is −3/8 times the sequential cycle product. All proper-subset energies and phases are retained; no bare-X substitution is made.

The abstract cycle calculation applies to every actual simple six-cycle by diagonal gauge equivalence of the active flip hypercube: pairwise square holonomies are precisely the native incident anticommutation signs, while fixed exterior factors are edge-sign gauges. Ratios to the sequential product are invariant under that gauge. This proves geometry independence of the coefficient without replacing native phases by a bosonic model.

## Evidence and limitations

The exact Fraction helper has3653 predicates, including the32-state spoke matrices, metric/graph identities and all720 six-cycle histories. It ran in0.020 seconds and used16.3MiB. This is not a full Hilbert-space simulation. The finite calculations support the closed-form recurrence and complete support argument; independent review is still required before downstream reuse. The source has no actual subprocess mutation claim. H8 canonical bytes were not changed.
