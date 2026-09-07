# Independent root map to a uniform electric-dominated lattice gap

This is an explicit application of an established mathematical stability theorem to a supplied compact SU3 Hamiltonian family. It does not reproduce that theorem from framework axioms or select the action/couplings. Root wrote the mapping after reading the primary paper's hypotheses and Theorems1–3, before reading native34's final proof. The native padding observation was received during derivation and is attributed below.

## Imported mathematical statement (not a new theorem here)

Yarotsky, math-ph/0411042, Theorems1–3, pp2–4, allows possibly infinite-dimensional site spaces and nonnegative possibly unbounded onsite operators with unique vacuum and gap at least1. For a fixed finite interaction shape and bounded selfadjoint translated local terms of supremum norm s, there are positive constants c1,c2 depending only on that shape. If s<c1, every finite empty-boundary restriction has a simple ground and its centered gap is at least1-c2*s. The infinite-volume ground-state limit and its GNS Hamiltonian exist with the same gap bound. Constants are existential, not numerical data supplied by this work. The paper identifies these statements as earlier results and sketches their proofs in section2; they remain load-bearing mathematical imports.

Primary source: https://arxiv.org/pdf/math-ph/0411042 . Only this imported statement is needed; no quasi-particle or scattering conclusion is used.

## Exact cell and interaction map

At each x in Z³ place the three positively directed links (x,i), i=1,2,3, with cell Hilbert space L²(SU3³). No link is duplicated. The onsite kinetic sum K_x is the sum of the three link operators -(3/(2a))Delta_(x,i). With Tr(T_A T_B)=delta_AB, a link representation(p,q) has energy [p²+pq+q²+3p+3q]/a. It is zero only for the trivial block and at least4/a otherwise. Thus h_x=(a/4)K_x has unique normalized constant vacuum and gap1, on an infinite-dimensional Hilbert space with compact-resolvent onsite Laplacian.

For i<j define the actual plaquette holonomy
U_(x,i) U_(x+e_i,j) U_(x+e_j,i)^(-1) U_(x,j)^(-1).
Its normalized real trace r_(x,ij) satisfies |r|<=1, and it acts only on cells{x,x+e_i,x+e_j}. Group the three pairs at anchor x. Every group fits the fixed four-cell shape Lambda0={0,e1,e2,e3}. Write
phi_x=-(av/4) sum_(i<j) r_(x,ij).
It is bounded selfadjoint with norm at most s=3av/4, regardless of volume. The physical magnetic deficits v sum(1-r) differ from these rescaled centered terms only by a scalar, which shifts the ground energy and leaves gaps unchanged. No global perturbation norm is substituted for s: the global norm generally grows with volume.

For a finite cell set Lambda, take all three outgoing link registers at each cell and include a whole plaquette group exactly when x+Lambda0 is contained in Lambda. This is precisely the fixed-interaction empty-boundary family in the imported theorem. Its outgoing links can end outside the cell set; their endpoint gauge transformations remain included. All included plaquettes close through actual links. This family may omit an individual boundary plaquette whose three cells are present but whose unused fourth common-shape cell is absent. It must not be identified with every conventional open-box truncation.

Let s<min(c1,1/(2c2)). Subtracting the scalar vacuum shift, applying the imported theorem and undoing the a/4 energy rescaling yields
 gap(H_Lambda)>= (4/a)(1-c2*3av/4) >= 2/a,
uniformly in the size of Lambda. The same estimate holds for the GNS Hamiltonian of the fixed infinite family. This is a nonempty sufficiently-small-av regime with an unspecified threshold. Here a is the supplied temporal scaling/kinetic parameter of the compact Hamiltonian; it is not identified with a measured spatial lattice spacing.

## Physical gauge restriction

Each gauge transformation at a vertex multiplies incident oriented link variables on the appropriate left/right side. It acts on finitely many cells. The bi-invariant kinetic Laplacian and the closed plaquette real trace commute with it, including at finite boundaries. In finite volume the ground can be chosen strictly positive: the compact product heat kernel is strictly positive and bounded real potential preserves positivity improvement. Uniqueness then fixes the positive normalized ground under every gauge transformation. Alternatively, no nontrivial one-dimensional representation of a finite product of SU3 can supply a ground phase. Thus the ground belongs to the full local Gauss-invariant sector, and restricting a reducing subspace containing it cannot decrease the gap.

The infinite ground state is invariant under each finite-support gauge transformation by the finite-volume limit. Its GNS representation therefore has unitaries U_g defined by U_g pi(A)Omega=pi(alpha_g(A))Omega, fixing Omega. For fixed local A,B and g, finite-volume covariance and the imported weak resolvent limit give U_g(H_infty-z)^(-1)=(H_infty-z)^(-1)U_g. Hence the closed joint fixed space intersection_g ker(U_g-I) reduces H_infty, contains Omega and the vectors pi(A)Omega for gauge-invariant local A, and inherits the gap. This statement does not need an unproved identification with another quotient Hilbert space or an infinite product Haar projection.

An optional stronger regularity argument is available: resetting one cell to its onsite vacuum in a finite ground-state density matrix preserves all other onsite expectations. Variational minimality gives <h_x><=2 sum_(y:x in y+Lambda0)||phi_y||<=8s. Compact onsite resolvent then gives tightness of local reduced densities and normality of the limiting local state. This can justify continuous local gauge averaging, but the fixed-space gap assertion above does not require the stronger identification and does not use it as an unstated premise.

## Conventional finite open graphs: separately attributed padding lemma

Native independently proposed this useful repair during root's derivation. For any finite subset of cubic links with its included elementary faces, place the links into full three-link cells, add enough cells so every nonzero anchor's whole common shape fits, and use only the desired graph's faces in each anchor group. The perturbation can be inhomogeneous; its norm is still <=3av/4 and the imported finite-volume constants depend only on the same shape. Every added link appears only in its onsite kinetic term. The enlarged Hamiltonian is exactly H_graph plus independent free electric factors. Its gap is the minimum of the graph gap and4/a (when extra factors exist), so the uniform >=2/a bound implies the same graph gap bound. This invokes Theorem1 separately for each inhomogeneous finite model; it does not apply the infinite-limit theorem to volume-dependent interactions.

## Movement and remaining imports

This advances a supplied compact Hamiltonian from a finite cube to a uniform lattice gap in an electric-dominated regime, including a properly defined infinite-volume physical sector. It does not prove a gap for arbitrary av, approach a spatial continuum/scaling limit, derive physical beta6 or QCD parameters, produce an area law, or select Wilson dynamics from Record axioms. The existing fixed-lattice scope note's absence of a framework-native gap remains true. The imported mathematical stability theorem is explicit and must survive independent applicability review before this becomes a review publication.
