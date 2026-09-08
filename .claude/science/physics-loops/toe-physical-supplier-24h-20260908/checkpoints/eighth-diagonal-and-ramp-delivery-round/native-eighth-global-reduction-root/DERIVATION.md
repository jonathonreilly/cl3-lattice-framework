# Global eighth-order diagonal from abstract connected clusters

Research derivation, before receiving any numerical eighth-order table. Let N be the number of vertices, all degree six, and let each ice bitstring have exactly three occupied incident edges. Work on a simple bipartite cubic torus with even periods at least four. Let c_T(b) denote the connected order-eight diagonal coefficient for a fixed-exterior active tree T with active bits b, and c_C(b) the corresponding genuine four-cycle coefficient in canonical direct-rotation gauge. These symbols are arbitrary functions with the abstract motif's automorphism symmetries and global bit-complement symmetry; no values are assumed.

## Why abstract motif functions are permissible

Physical Z_e covariance makes a diagonal perturbation coefficient even in each individual edge coupling. At order eight it uses at most four active edges. Inclusion-exclusion over active subsets isolates the monomials supported on the entire subset. Vertex-disconnected subsets factor into independent Hamiltonians, and their low-energy diagonal has additive energy; connected subtraction removes their mixed contribution. For <=4 edges a connected simple bipartite graph is a tree or four-cycle.

On a fixed-exterior tree, leaf induction makes its ice subspace one dimensional. The diagonal is its unique low eigenvalue and is invariant under edge phase redefinitions. Native active A_e operators flip their own bit and have the same square I and incident-anticommutation relations under relabeling of an abstract motif. Their edge-hypercube hopping representations are related by diagonal gauge: every square holonomy is fixed by the pair commutation sign, and square faces generate all closed paths in the hypercube. The same exterior energy deviations depend only on the motif and initial active bits. Hence the coefficient cannot depend on an arbitrary global lexicographic edge ordering or frozen exterior Z signs. Global bit complement sends all degree deviations to their negatives and preserves their squares. Uniform coupling signs also disappear from these even diagonal monomials. This justifies motif automorphism and complement invariance. This argument does not assert that offdiagonal ring signs disappear.

## Tree embedding sums are scalar except for excluded closed walks

Every connected tree with at most three edges has a scalar embedding sum by local degree counts. A length-k nonbacktracking walk, k<=3, is simple: a shorter collision would be an immediate reversal or a triangle. For a prescribed bit word b_1,...,b_k its number is

    N * 3 * product_{j=1}^{k-1} a(b_j,b_{j+1}),
    a(b,c)=2 if b=c, and 3 otherwise.

At each new vertex, three incident edges have each bit value and the incoming edge excludes one of its own value. Reversing a path gives its other orientation, so the unoriented path sum is half the weighted bit-word sum. Three-star embeddings likewise depend only on binomial choices from three occupied and three unoccupied incident edges. The one-edge case counts each edge twice in oriented walks.

There are three abstract four-edge trees: four-star, degree-three/degree-two fork, and length-four path. Four-star has coefficient s(k) for k occupied leaves and contributes

    N * sum_{k=0}^4 binom(3,k) binom(3,4-k) s(k).

Invalid binomial coefficients are zero; the multiplicities are3,9,3 for k=1,2,3, totaling15N. This is scalar.

For the fork orient its unique internal edge from degree-three center a to degree-two center b. Let its bit be b0, the two leaves at a contain k occupied edges, and the extra leaf at b have bit d. The coefficient is t(b0,k,d). The total contribution is

    N * 3 * sum_{b0=0}^1 sum_{k=0}^2 sum_{d=0}^1
      binom(3-b0,k) binom(2+b0,2-k) a(b0,d) t(b0,k,d).

The leaf pair at a is unordered already. No hidden collision invalidates this product: an extra b-leaf coinciding with an a-leaf would produce a triangle, absent here. The edge a-b is explicitly excluded. The coefficients sum to300N when t=1, matching6N*binom(5,2)*5. Each fork is counted once because its degree-three and degree-two vertices are unique. This is scalar as well.

Let p(b1,b2,b3,b4) be the four-edge simple-path coefficient, invariant under reversal. Count ALL nonbacktracking four-step walks, allowing return to the initial vertex. The same transition formula holds even at the final step. The only nonsimple walks are closed four-cycles: immediate reversal is excluded and no triangle exists. Therefore the sum over actual unoriented simple paths is

    (3N/2) * sum_{b in {0,1}^4} [product_{j=1}^3 a(b_j,b_{j+1})] p(b)
    - (1/2) * sum_{unoriented four-cycles C}
                       sum_{eight directed rooted traversals r of C} p(b(r)).

Each simple path has exactly two orientations. A four-cycle has four roots and two directions. This subtraction uses the abstract PATH table evaluated on the four distinct edges of the closed walk; it is a combinatorial weight for subtracting forbidden path embeddings, not an assertion that the physical cycle is a tree. Reversal symmetry reduces the inner half-sum to the four cyclic rotations of either chosen direction.

## Exact form of the remaining cycle interaction

Combining all trees with the genuine cycle-connected term gives

    E8_diag(x) = N*C_tree + sum_{C unoriented simple four-cycle} W(b_C),
    W(b) = c_C(b) - sum_{r=0}^3 p(rotation_r b).

C_tree includes all smaller connected clusters, star and fork scalars and the unrestricted walk scalar. Four-cycle embeddings include straight winding cycles when an extent equals four. The coefficient table must include the rank-two alternating-cycle case; scalar nondegenerate recursion in that case is invalid. No value or constancy of W has been established here.

Under cycle rotations, reversal and complement there are four bit-pattern classes: all equal; one/three occupied; two adjacent occupied; alternating. Four W values may therefore be needed. Inferring a pure flippability potential from only an alternating/nonalternating difference is invalid unless the other three class values coincide, or additional global identities are established. In particular a finite fit on a few ice states is not a proof that those other observables cancel.

This derivation is a conditional reduction of a complete canonical cluster expansion. It neither establishes the actual H8 coefficients nor transfers them into a different local normal-form gauge. No ground-state, RK partner, phase or electromagnetic conclusion follows. Deterministic motif enumeration with symbolic placeholder weights can check the combinatorics independently of the physical coefficient extraction.
