# Static source electric minimum and the first geodesic plaquette operator

This is finite-volume perturbation theory for an explicitly supplied static-source sector of the compact cubic Hamiltonian. It does not derive external charges, their preparation, a physical clock or confinement from the axioms. Root disclosed the shortest-path adjacency hypothesis but no coefficient before my calculation. The coefficient1/18 was independently derived and prospectively frozen before exact checks. General fluctuating-string/fermion formulations are prior art: [Kogut, Sinclair, Pearson, Richardson and Shigemitsu, Phys.Rev.D23,2945(1981)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.23.2945) explicitly studies Hamiltonian string dynamics and a fermion formulation. The publication abstract was inspected; no claimed access to the paywalled full paper or novelty of the general string construction is made.

## 1. Supplied sector and conventions

Take a finite open rectangular cubic box containing distinct vertices s,t and all links of their coordinate bounding box. Its link Hamiltonian is

 H=K+v sum_f(1-r_f), K=-(3/(2a))sum_e Delta_e,
 r_f=ReTr(U_f)/3, a>0, v>=0.

The external source space is3 at s and bar3 at t, with zero external Hamiltonian by convention. Represent a state by a3by3 matrix-valued function F(U), with norm squared integral Tr(F†F). Under a vertex gauge transformation define the combined action

 (G_g F)(U)=g_s F(g^(-1)·U)g_t†.

The physical source sector is its invariant subspace. If W_P is the ordered link product along a path s→t (inverse matrices when traversed backward), then

 F_P(U)=W_P(U)/sqrt3                              (1)

belongs to this sector and is normalized: Tr(W_P†W_P)/3=1 pointwise. This fixes endpoint/source normalization rather than importing a color-averaging factor later.

## 2. All-representation electric lower bound and complete equality space

Peter-Weyl decomposes every link into full irreducible matrix blocks. A label(p,q) carries kinetic energy

 e(p,q)=[p²+pq+q²+3p+3q]/a.

For a nonzero label this is at least4/a, with equality only for3 or bar3. Indeed its increments in p and q are2p+q+4 and p+2q+4, strictly positive on nonnegative labels. This covers all representations, including triality-zero ones.

Fix a representation assignment with a nonzero physical intertwiner and call its nontrivial-edge support G. The connected component of G containing s must also contain t. Otherwise perform the same center transformation zetaI at every vertex of that component. Internal link endpoint phases cancel, links leaving the component have trivial labels, and the lone external fundamental source contributes zeta. An invariant vector cannot have this phase. This argument uses all nontrivial edges, not just fundamental triality-carrying edges, so it does not miss a possible adjoint/baryonic route.

Consequently G contains an s-t path. Its number of nontrivial edges is at least the graph distance, which is the Manhattan distance d=|t-s|_1 for the stipulated box. The total electric energy therefore obeys

 E>=4|G|/a>=4d/a.                                (2)

Equality forces exactly d nontrivial edges and energy4/a on every one. The support is exactly one simple shortest path: a connecting path already uses at least d edges, so there is no remaining edge for a branch, cycle, disconnected excitation or baryonic junction. Every internal path vertex has degree2. Schur's lemma fixes the compatible fundamental/antifundamental continuation and its one-dimensional intertwiner. The source representations fix its orientation at the endpoints, with a unique invariant contraction there. Thus each shortest path contributes precisely one state(1), not an extra9-fold endpoint degeneracy.

Distinct shortest paths are orthogonal. There is an edge used by one and not the other, and its Haar integral in the overlap is linear in a fundamental matrix coefficient and hence zero. Conversely each path state has d fundamental link factors and exact kinetic energy4d/a. The full minimum eigenspace is therefore exactly the orthonormal span of all shortest paths. The argument applies to every Peter-Weyl assignment, so it excludes a cheaper branched/baryonic state rather than assuming it absent. For a connected non-box open subgraph, replace d by its actual graph distance; the stated Manhattan formula requires that a Manhattan path is present.

## 3. Exact first-order projected magnetic term

Let P_min project onto that entire eigenspace and let N_f be the number of included plaquettes. Diagonal matrix elements of r_f vanish because the path norm is pointwise1 and the Haar mean of r_f is zero.

For distinct shortest paths P,P', independent link-center phases force a matrix element of either oriented face character to vanish unless their oriented edge difference equals that face boundary modulo3. Along any shortest path, distance from s strictly increases, so a shared edge cannot be traversed in opposite directions by two shortest paths. Their difference therefore has coefficients only0,+1,-1 with a fixed possible orientation per edge. The modulo3 condition is then an exact signed equality on the four face edges, not an epsilon-tensor loophole. Their symmetric difference must be exactly that square.

Two equal-length simple paths differing on only one square must replace one two-edge corner arc by the other two-edge arc. A1versus3-edge replacement would change the length. Thus the only nonzero off-diagonal entries are elementary square flips that remain shortest paths. The two arcs use adjacent edges, not disconnected opposite sides. Let Adj be the unweighted adjacency matrix of this finite path-flip graph.

For one such flip, common path prefix/suffix cancel inside Tr(W_P'†W_P), leaving one oriented plaquette character chi_f or its conjugate. Therefore the actual matrix element is

 <F_P',r_f F_P>=(1/3)*(1/6) integral chi_f(chi_f+bar chi_f)
               =1/18,                           (3)

using integral chi_f bar chi_f=1 and integral chi_f²=0. Only one orientation contributes. The external source normalization1/3 is essential. No commuting-field approximation or fitted hopping amplitude appears.

It follows exactly that

 P_min V P_min=v[N_f I-Adj/18].                  (4)

The free cluster is isolated with finite multiplicity in each fixed finite box. Bounded perturbation theory gives its first-order eigenvalues

 E_j(v)=4d/a+v[N_f-lambda_j(Adj)/18]+O(a v²),      (5)

with constants and valid neighborhood depending on the fixed graph. No uniform remainder in d or volume is asserted. The vacuum-sector ground energy is N_f v+O(a v²), so the lowest source-minus-vacuum energy has expansion

 4d/a-v lambda_max(Adj)/18+O(a v²).              (6)

This is a supplied static-source energy difference near v0, not a temporal Wilson-loop derivation or a finite-coupling string-tension theorem.

## 4. Entire planar first-order spectrum

For planar displacement(R,S,0), R,S>=0 and R+S=L>0, every shortest path is a binary word of length L with R steps in one axis and S in the other. An elementary plaquette flip swaps neighboring unequal letters. Thus Adj is exactly hard-core nearest-neighbor hopping on an open chain of L sites with R particles.

To verify the fermionic identification rather than assume it, use ordered occupation basis |i1<...<iR>. The operator c_j†c_(j+1)+c_(j+1)†c_j moves a particle to an adjacent empty site. Removing and reinserting it does not cross another occupied site, so the two fermion signs cancel. Its matrix element is+1, exactly the square-flip adjacency. The one-particle chain eigenvectors sin(pi k j/(L+1)) have eigenvalues2cos(pi k/(L+1)), k1..L. Antisymmetric products diagonalize the fixed-R hopping space completely. Hence every first-order path eigenvalue, with multiplicity, is

 lambda_(k1,...,kR)=2 sum_(b=1)^R cos(pi k_b/(L+1)),
 1<=k1<...<kR<=L.                               (7)

For R,S>0 the largest is simple and takes k_b=b. The next-largest replaces R by R+1, so the first-order splitting above the lowest source branch is

 (v/9)[cos(pi R/(L+1))-cos(pi(R+1)/(L+1))].       (8)

For an axis-aligned source displacement there is one path and no internal geodesic splitting; formula(8) is not asserted. At small positive v in a fixed box, the coefficient in(8) is positive and isolates the lowest branch after including its finite perturbative remainder. No claim that the radius remains uniform as the source separation grows is made.

## 5. Exact checks and scope

The prospective runner checks all-label kinetic increments, the source and Haar normalization, and five actual planar shortest-path sets: (R,S)=(1,1),(1,2),(2,2),(1,3),(2,3). It enumerates their actual oriented link differences against face boundaries; the resulting projected matrix equals Adj/18. It compares full exact characteristic polynomials against the fermion subset spectrum, not only the largest eigenvalue. Omitting the endpoint normalization is an adverse coefficient control. The all-representation equality classification is analytical and is not inferred from these finite path enumerations.

The external source spaces, action, couplings and finite graph are supplied. The result classifies a free electric eigenspace and its actual first-order perturbation. It is neither a uniform all-order expansion, an arbitrary-coupling confinement claim, a continuum limit, nor a deduction of temporal confinement from spatial-loop area suppression.
