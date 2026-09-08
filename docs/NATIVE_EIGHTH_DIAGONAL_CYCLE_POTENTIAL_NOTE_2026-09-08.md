---
claim_id: native_eighth_diagonal_cycle_potential_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Full-carrier supplied native pair perturbation: canonical eighth-order ice diagonal equals an explicit tree scalar plus four-cycle pattern potential. Exact same-component L6 witnesses exclude scalar plus total flippability in this convention; no full H8 offdiagonal or phase claim."
upstream_dependencies:
  - native_virtual_pair_ring_mechanism_note_2026-09-08
runner: scripts/native_eighth_diagonal_cycle_potential_2026_09_08.py
---

# Eighth-order native ice diagonal and its cycle potential

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

For the supplied full-carrier native Hamiltonian, the eighth-order canonical ice diagonal has an explicit local cycle potential. It is not a scalar plus total cycle flippability: three ice states connected by legal plaquette flips on the same L6 torus give an exact affine obstruction. This concerns a specified effective-Hamiltonian convention, not a phase or a basis-independent obstruction to other physical models.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite-order full-carrier canonical diagonal and global witness."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Model and result

Use the [full-carrier mechanism](NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md), its [native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) and [instrument algebra](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). On finite periodic cubic graphs with even extents at least four, retain the full edge carrier, relaxed cycle constraint and no fixed winding sector. There is no hard low-charge projection. Let

\[
H=UD+g\sum_e\lambda_e A_e,\qquad D=\sum_vQ_v^2,\quad
Q_v=(-1)^{v_1+v_2+v_3}\left(\sum_{e\ni v}(1-Z_e)/2-3\right),\qquad U>0.
\]

Use the canonical direct rotation for the finite low-energy spectral cluster. The result is its perturbative coefficient at zero coupling, not a volume-uniform convergence-radius claim. For uniform $|\lambda_e|=\lambda$, put $N=|V|$. On any ice bitstring $x$,

\[
\langle x|H^{(8)}_{\rm eff}|x\rangle
=\frac{g^8\lambda^8}{U^7}\left[\frac{3610233}{16000}N+
\sum_{C\in\mathcal C_4}W(x|_C)\right].
\]

Here $\mathcal C_4$ includes every unoriented simple four-cycle, including straight winding cycles along extent-four directions. The four pattern weights are

|Pattern|$W$|
|---|---:|
|all equal|$-99/1600$|
|one or three occupied|$-10019/108000$|
|two adjacent occupied|$-11/144$|
|alternating|$5/32$|

Equivalently, with cycle domain-wall count $d_C$, product $P_C=\prod_{e\in C}(1-2x_e)$ and alternating indicator $F_C$,

\[
W=-\frac{7567}{108000}-\frac{209}{28800}d_C+
\frac{1769}{216000}P_C+\frac{3559}{14400}F_C.
\]

The proof below specifies the active-cluster gauge, rank-two trace, subtraction and embedding counts. No eighth-order offdiagonal operator is computed, and this diagonal is not transferred into an arbitrary local-normal-form gauge.

## Finite cluster identification

Fix an exterior ice bitstring and activate at most four edges. In relative toggle coordinates z, the energy is

D(z)=sum_v [sum_{e incident v} z_e(1−2b_e)]².

The native flips square to one, anticommute exactly for incident edges, and commute otherwise. In a local edge ordering they are represented by X_e times Z on earlier incident active edges. Fixed exterior factors only change individual edge signs, removable by conjugating Z_e. Different edge orderings give diagonal quadratic phase conjugations. These changes preserve diagonal energies and canonical effective diagonal entries. Thus this finite representation retains the native algebra; it is not replacement by bare X.

For a forest, leaf induction gives a unique zero-energy toggle configuration z=0. The exact analytic eigenvalue recurrence, with intermediate normalization psi_n(0)=0 for n>0, is

E_n=(V psi_(n−1))(0),
psi_n(z)=[−(V psi_(n−1))(z)+sum_(j=1)^(n−1) E_j psi_(n−j)(z)]/D(z).

All energy-feedback terms are retained. This is the canonical diagonal because the fixed-exterior ice space is rank one.

## Independent contour extraction

Let R0(z)=(z−D)^−1. The sum of eigenvalues in the low-energy Riesz cluster is the contour integral of z Tr(z−H)^−1. The resolvent trace is the z derivative of log det(z−H). Expanding

log det(z−D−gV)=log det(z−D)−sum_(k>=1) g^k Tr[(R0V)^k]/k

and integrating z times the derivative gives

E_k,total=(1/k) Res_(z=0) Tr[(R0(z)V)^k].

This is a finite-dimensional analytic contour identity, not a scalar rank-one assumption. Each closed k-step walk contributes its native phase times k denominator factors at its visited states. With q zero-energy denominators, the residue is the coefficient of z^(q−1) in the product of the remaining factors. Each nonzero factor expands as −sum_(a>=0)z^a/D^(a+1). The implementation retains those coefficients exactly with Fraction arithmetic. Rank-one agreement through eighth order was checked independently against the feedback recurrence on all one-edge, pair and three-star bit inputs. The one-edge eighth coefficient is 5/128, as also follows from 1−sqrt(1+g²).

## Alternating cycle and canonical diagonal

Only alternating four-cycle inputs have two zero-energy states. The product S of its four native A operators commutes with every active A: each edge has two incident anticommuting neighbors. It toggles all four bits. Alternation makes the fixed exterior degree two at each cycle vertex, so the full toggle negates every degree deviation and preserves D on all sixteen states. S therefore commutes with H and exchanges the two ice basis vectors up to phases.

The spectral projection and canonical direct rotation are covariant under this symmetry; their effective two-by-two Hamiltonian consequently has equal diagonal entries. Each diagonal is one half of the low-band trace. We use the contour identity divided by two, not a nondegenerate recurrence on one member. The actual sixteen-state commutation and energy symmetry are explicitly checked. Nonalternating cycles have rank-one ice and use the feedback recurrence.

## Support extraction and complete local output

Inclusion-exclusion over all nonempty edge subsets isolates the terms containing every active edge. At total degree eight four-edge supported diagonal terms use each edge twice, because physical Z conjugation makes each diagonal even in each coupling. For smaller subsets the table retains the sum of all their degree-eight monomials at unit magnitude. Vertex-disconnected supports factor, and the disconnected two-edge inclusion-exclusion control vanishes.

RESULT.json contains every bit pattern for one edge, pair, three-star, three-path, four-star, four-path, fork and cycle, together with all lower even coefficients and the connected eighth coefficient. Some locally listed patterns (for example four equal bits at a degree-three ice vertex) cannot have an exterior ice completion. They are explicitly a superset of physical inputs; no such row may be assigned a global embedding without an admissibility filter.

Selected connected coefficients are: one edge 5/128; pair 35/64; three-star 45/32; four-star 15/16. Paths and forks are nonconstant. Four-cycle classes are all-equal 1759/4800, one-or-three occupied 2827/7200, two adjacent 167/432, alternating 25/32. All cycle orientations, complements and rotations are present in the raw table.


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

C_tree includes all smaller connected clusters, star and fork scalars and the unrestricted walk scalar. Four-cycle embeddings include straight winding cycles when an extent equals four. The coefficient table must include the rank-two alternating-cycle case; scalar nondegenerate recursion in that case is invalid. The symbolic reduction is evaluated by the exact table below.


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

The helper verifies this equality for all 16 patterns. Unequal nonalternating weights do not alone prove that the global sum cannot simplify to a scalar plus flippability.

## A global domain-wall identity

At any degree-six ice vertex, three incident edges are occupied and three are empty, so exactly nine unordered incident edge pairs have unequal bits. Each perpendicular incident pair belongs to exactly one elementary plaquette. A collinear opposite pair belongs to a simple four-cycle precisely when that coordinate extent is four; that cycle is the straight winding cycle. No other four-cycle passes through that pair on these simple cubic tori.

Therefore, with all simple four-cycles counted,

sum_C d_C=9N−sum_v sum_(axes a with L_a>4) 1[b_(v,a,+) != b_(v,a,−)].

For the all-L4 torus this is exactly9N. For all extents>=6 the last term contains all three collinear pairs at every vertex and is not eliminated by degree-three counting alone. Mixed extents obey the same formula with the indicated subset.

The domain-wall identity alone does not remove the product term. The following delivered-state witness establishes the precise failure of a scalar-plus-flippability identity, without assuming irreducibility from unequal local weights.


## Narrow obstruction

Write the proven diagonal as a scalar plus

Q(x)+(3559/14400) F(x),
Q=−209 d(x)/28800+1769 P(x)/216000,

where d is total cycle domain walls, P the sum of four-edge sigma products, and F total cycle flippability. A scalar+aF representation would force Q to be affine in F on every ice state, even if the scalar and a were allowed to depend on volume.

On L4, counting all simple four-cycles including winding cycles, the three exact feature triples (F,P,d) are

(144,240,576), (136,208,576), (130,192,576).

The affine determinant (F1−F0)(Q2−Q0)−(F2−F0)(Q1−Q0) is −1769/3375, nonzero. The two successive legal flips are winding cycles with edge IDs[0,48,96,144] and[1,13,25,37] in the declared coordinate edge order.

On L6, where every simple four-cycle is an elementary plaquette, the triples are

(324,648,1296), (320,624,1304), (317,612,1310).

The determinant is −1769/9000, again nonzero. The successive legal plaquette flips have edge IDs[0,125,15,17] and[1,558,541,540]. Some cross a periodic coordinate seam; they are ordinary elementary plaquettes, not length-four winding cycles. Translation can place each such plaquette away from a coordinate seam, which is only a coordinate convention.

All three states in each witness are connected by legal alternating cycle flips. The obstruction therefore persists even on that particular ring-connected component, not merely across disconnected ice sectors.


## Scope, evidence and provenance

The Hamiltonian, penalty, edge coefficients and ice carrier are supplied. This result supplies neither an RK tuning nor a selected action, phase, ground state, electromagnetic interpretation or thermodynamic bound. The exact affine obstruction is confined to scalar plus total flippability in the stated canonical convention. Different supplied interactions and other representations are outside that claim.

The primary runner executes fresh local tables, independent symbolic graph counts, combination arithmetic and full-state witness reconstruction in that order. Original counts are 591+541533+112+21=542257 explicit predicates. Seven canonical absolute-value bindings give 542264 actual predicates; these independently reviewed constants prevent shared-dataflow mutations from passing self-consistently. Finite controls support the general proof and are not an exhaustive lattice census. Original direct alternative calculations remain described as direct controls; new isolated subprocess mutations are separately logged. Complete original proofs, outputs, source-bound reviews and the reviewer's corrected assert-under-OO history are preserved in the [packet](../.claude/science/physics-loops/native-eighth-diagonal-cycle-potential-20260908/REVIEW_HISTORY.md).

Resolvent perturbation, canonical rotations and linked-cluster bookkeeping are standard mathematics; no historical novelty is claimed. This block extends the exact supplied-model mechanism of its parent. No third-party PDF or text is copied. Author verification is not an audit verdict, and the final canonical source requires independent review.
