# Root uniform static-source energy bounds via equivariant ground dressing

This hard block38 was prospectively contracted before proof work. Native/root discussed the source, covariance route and finite source-dimension amplification before independently writing completed proofs. Root has not opened native's completed proof. The result concerns a supplied compact SU3 Hamiltonian and additional supplied static probe representations; it does not derive these from the axioms. It is an application of an imported many-body perturbation construction, not a claim to a new general confinement mechanism.

## Statement and conventions

Let G be a finite connected subgraph of the infinite cubic lattice with any subset of its actual elementary faces. Pick distinct vertices x,y in the same component and let d=d_G(x,y). On full link Haar L2 take

 H_G=K_G+v sum_f(1-J_f), K_e=-3Delta_e/(2a), J_f=ReTr(U_f)/3, a>0,v>=0.

There are no endpoint rest-energy or kinetic terms. The neutral energy E_vac is the full-link ground energy, equal to the ground energy in the Gauss-invariant sector. The charged carrier consists of matrix-valued functions Psi with Psi(U^g)=g_x Psi(U)g_y^dagger and inner product integral Tr(Psi^dagger Psi)/3; its Hamiltonian acts on link arguments only. This specifies the source convention and is equivalent to adjoining conjugate endpoint representations, of total dimension9, and imposing Gauss invariance. Let E_xy be its lowest energy.

There exist positive constants delta_* and c depending only on fixed cubic interaction geometry such that, with delta=3av/4 and kappa=3c delta, if delta<delta_* and kappa<1 then

 (4/a)(1-kappa)d <= E_xy-E_vac <= 4d/a.                 (1)

In particular delta<min(delta_*,1/(6c)) suffices for2d/a<=E_xy-E_vac<=4d/a. The upper bound and nonnegativity hold for everyv>=0. Constants and coupling window are existential; no numerical physical scale is selected. The bounds are uniform in G and in d. We do not assert existence of a unique infinite-volume static potential from these inequalities alone.

## Imported coordinate estimate

The load-bearing primary source is Yarotsky, arXiv:math-ph/0411042, Section2, equations8–15: https://arxiv.org/pdf/math-ph/0411042 . For sufficiently small fixed-range bounded perturbations of onsite product-vacuum operators with gap1, it constructs an invertible ground dressing S=exp(sum_I vhat_I). In its excitation coordinates, the vacuum-energy-subtracted Hamiltonian is H0+F, with a column estimate sum_J||(F u_I)_J||<=c delta |I| ||u_I||. Its constants are independent of finite volume and it permits infinite-dimensional onsite carriers and inhomogeneous bounded interactions. We use this actual coordinate estimate, not merely the theorem's global spectral inclusion. The new steps below are symmetry restriction, finite source amplification, boundary-vacuum restriction and the exact charged trial upper bound.

## Complete-cell embedding and charged free threshold

Complete the finite graph into a finite family of cells, each carrying its three outgoing link spaces. Include enough cells that every original face group's range fits. All newly added links are called ghosts; their electric terms are present, but no plaquette containing a ghost is retained. Set h_z=(a/4)K_cell,z. Its constant vacuum is unique and its gap is1: the full all-label electric spectrum is [p²+pq+q²+3p+3q]/a, with minimum4/a on nontrivial irreps. Group the actual retained plaquettes by base vertex, phi_z=-(av/4)sum_(retained i<j)J_(z,ij). Their support lies in {0,e1,e2,e3}+z and norm is at mostdelta=3av/4. Missing terms are zero, allowed by the inhomogeneous theorem. The centered scaled enlarged Hamiltonian is (a/4)(H_G+K_ghost)-avF/4. Its vacuum energy is (a/4)E_vac-avF/4, because ghosts decouple with zero ground energy. Scalar subtraction therefore leaves exactly (a/4)(H_G-E_vac+K_ghost).

Impose Gauss at every vertex of this enlarged link graph, including dangling head vertices outside the cell index set. Every gauge transformation nevertheless factorizes over cells: it acts by left/right group translations on their outgoing links. It fixes each cell's constant vacuum and commutes with each h_z and each excitation projection. To recover the actual graph, ALSO restrict every ghost link to its constant vacuum. This restriction prevents any artificial screening or shortcut through the completion.

In the joint charged/ghost-vacuum sector the free scaled operator H0=(a/4)(K_G+K_ghost) has thresholdd. Proof: in any nonzero spin-network representation assignment, the occupied component containing x must also contain y. Applying one center element simultaneously at all vertices of an occupied component cancels its internal link phases; a lone fundamental endpoint has nonzero triality and is impossible. Thus there is a path of at leastd occupied original links, each costing at least1 in scaled units. A shortest fundamental path realizes equality. This argument admits all SU3 representations and baryonic branching; branches cannot evade the component constraint. It also works on each excitation-coordinate block after projection onto the charged sector, since unused cells are vacuum and the same Gauss equations apply.

## Equivariance of the nonunitary dressing

In a finite volume the full link ground state is unique, gauge invariant and has nonzero overlap with the product vacuum. Positivity of the elliptic heat kernel gives these properties for the present smooth compact model; the imported theorem also ensures the small-perturbation construction. Normalize that overlap to1. The product vacuum, cell excitation projectors and ground vector are all fixed by every gauge transformation U_g. Uniqueness of the creation-log expansion in the source's equation8 implies U_g v_I=v_I for each coefficient. Consequently each vhat_I=|v_I><Omega_I|, tensored with identity outside I, commutes with U_g, and so do S and S^-1. No claim that S is unitary is made.

The enlarged ground factorizes into the original ground and all ghost vacua. Its excitation coefficients therefore have ghost vacuum in every ghost factor. Whenever a cell includes ghosts, both ket and bra of its creation operator have ghost vacuum, so vhat_I commutes with each ghost-vacuum projector. Thus S preserves the ghost-vacuum restriction as well. Extend S by identity on the finite source space D of dimension9. It commutes with the combined link/source Gauss action. Hence it maps the joint physical charged and ghost-vacuum sector bijectively onto the same sector in free excitation coordinates.

The source's energy-weighted coefficient estimate puts each v_I in Dom H_I,0. For a finite number of cells there are finitely many I, and [H0,vhat_I]=widehat(H_I,0 v_I) is bounded. Therefore S and S^-1 preserve Dom H0, by the bounded commutator identity for their finite exponential. The similarity on that domain is legitimate even for unbounded onsite electric operators. Its norm and inverse norm may grow with volume; spectral equality in each fixed finite volume requires only bounded invertibility, not a uniform condition number.

## Fixed source multiplicity and coordinate norm

The excitation decomposition is an orthogonal direct sum over cell subsets I before dressing. After adjoining D, write u_I in H'_I tensor D and define ||u||_1=sum_I||u_I||, where each block uses its Hilbert norm. For each fixed finite volume this is equivalent to the ordinary Hilbert norm; there are only finitely many subsets I, even though each block may be infinite dimensional. Gauge averaging is a contraction in this norm because each gauge transformation acts blockwise unitarily. The joint ghost projector is likewise blockwise contractive. Thus the charged/ghost-vacuum sector is a closed complemented subspace of these coordinates.

The scalar column estimate does not automatically tensor with constant1. Choose an orthonormal basis e_alpha of D and write u_I=sum_(alpha=1)^9 u_I,alpha tensor e_alpha. The triangle inequality, the scalar estimate and Cauchy–Schwarz give

 sum_J||(F tensor I_D u_I)_J||
 <= sum_alpha sum_J||(F u_I,alpha)_J||
 <= c delta |I| sum_alpha||u_I,alpha||
 <= 3c delta |I| ||u_I||.

Summing I and using H_I,0>=|I| yields

 ||F_D u||_1 <= kappa ||H0 u||_1, kappa=3c delta.        (2)

This fixed factor3 is independent of lattice volume and source separation. It avoids assuming complete boundedness of a Banach-space estimate. F_D preserves the charged/ghost-vacuum sector because the full dressed Hamiltonian and H0 do.

## Restricted resolvent and linear lower bound

On the joint sector every nonzero excitation block has selfadjoint H_I,0 spectrum in[d,infinity). For real0<=z<d, functional calculus in each block gives

 ||H0(H0-z)^-1||_(1->1) <= d/(d-z).

For z<0 the corresponding bound is at most1. Combined with(2), if0<=z<(1-kappa)d the Neumann factor F_D(H0-z)^-1 has norm less than1. For z<0 the same is true whenkappa<1. Thus H0+F_D-z is invertible on the joint sector for all realz<(1-kappa)d, with inverse (H0-z)^-1 sum_n[-F_D(H0-z)^-1]^n. Its domain and closure are those justified above. Similarity carries this resolvent back to the selfadjoint vacuum-subtracted charged Hamiltonian. Therefore its spectrum lies in[(1-kappa)d,infinity), giving the lower inequality(1) after multiplication by4/a.

This is a sector-specific resolvent argument. A global spectral inclusion alone would allow eigenvalues from low-energy neutral sectors and would not prove a distance-dependent charge cost. The construction's covariance and sectorwise free threshold are essential.

## Exact all-coupling upper bound

Let Omega(U) be the normalized full-link ground state of H_G, and choose a shortest simple oriented path P from x to y. The matrix-valued Psi(U)=U_P Omega(U) belongs to the charged carrier and has norm1 pointwise after taking Tr/3. Multiplication by the smooth bounded holonomy preserves the form domain. Potential energy is unchanged because the potential is scalar multiplication and U_P is unitary.

For a link e on the simple path and an orthonormal SU3 generator basis T_A with Tr(T_A T_B)=delta_AB, the derivative of U_P inserts iT_A, conjugated by path factors, with either orientation. Thus Tr(U_P^dagger partial_(e,A) U_P)=0. The kinetic cross term between derivatives of Omega and U_P vanishes pointwise after the normalized source trace. Summing generators gives sum_A T_A²=(8/3)I, so

 (3/(2a)) sum_A Tr[(partial_(e,A) U_P)^dagger(partial_(e,A) U_P)]/3=4/a.

Links outside P give no additional term. Consequently the full quadratic form identity is

 <Psi,H_G Psi>=E_vac+4d/a.

Variational minimization gives the upper inequality(1) for allv>=0. Also E_xy>=E_vac because the charged space is a subspace of the full-link Hamiltonian tensored with D. No unknown extensive vacuum energy remains in either estimate.

## What is and is not established

The result bounds the energy needed to separate the explicitly supplied static fundamental probes between two linear functions of graph distance, uniformly over finite graphs, at sufficiently smallav. It includes actual nonlinear plaquette interactions and all electric representations. It does not establish convergence of finite-volume static energy differences, uniqueness of a charged infinite-volume state, a temporal Wilson-loop formula, a continuum limit or a physical numerical string tension. The static source species and their normalization are extra inputs; no new dynamical matter or axiom-selected QCD has been derived. The external dressed-ground perturbation theorem is indispensable and must remain named in any claim certificate.
