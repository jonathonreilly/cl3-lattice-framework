# Finite-region and finite-register approximation for local compact-gauge probes

This is a conditional theorem for the supplied compact cubic-link Hamiltonian. It is not a derivation of that Hamiltonian, a uniform estimate on arbitrary-energy inputs, or a hardware compiler. The initial root candidate for the incidence constant was disclosed in PREREGISTRATION.md before the geometry checks. I have not read root's parallel derivation. Here ell denotes spatial radius and r denotes Peter-Weyl cutoff; this only separates the two roles called R in the prospective route.

## 1. Model and statement

On an arbitrary finite cubic link set Lambda, include any elementary plaquettes whose four links are present, and put

 H_Lambda=sum_(e in Lambda) K_e+v sum_(p retained)(1-r_p),
 K_e=-(3/(2a))Delta_e, r_p=ReTr(U_p)/3, a>0, v>=0.

Each link space is full L2(SU3), not its central subspace. The bounded centered interaction Phi_p=-v r_p has norm at most v. Scalar deficits do not affect dynamics. Link distance joins two distinct links when they belong to one elementary plaquette of the ambient cubic lattice. A bounded observable A has nonempty finite link support X. Let B=B_ell(X) intersect Lambda, ell a nonnegative integer; include all original plaquettes wholly contained in B in H_B. Define N=|B|, F=number of those faces, and C=number of original faces crossing between B and Lambda minus B. Set M=2vF. The following upper bounds hold:

 N <=3|X|(2ell+1)^3, F<=N, C<=4N.                 (1)

For any initial state rho of Lambda, its reduction rho_B is sufficient for evolution under H_B, regardless of correlations with the exterior. Assume only its finite local form energy

 E=Tr(rho_B H_B)<infinity.                         (2)

At each link of B retain every matrix coefficient of every SU3 representation p+q<=r, r>=0. Let P be the tensor product of these projectors, p=Tr(P rho_B), and suppose p>0. Define rho_r=P rho_B P/p, H_r=P H_B P restricted to RanP, and A_r=PAP restricted there. Write

 m=r+1,
 g_r=[ceil(3m²/4)+3m]/a,
 alpha=sqrt(E/g_r),
 L_ell(T)=2|X| v C T exp(32 exp(1) v T-ell).       (3)

For all |t|<=T,

 |Tr(rho tau_t^Lambda(A))-Tr(rho_r exp(itH_r) A_r exp(-itH_r))|
 <= ||A|| min{2, L_ell(T)+2[(1+M T)alpha+1-sqrt(p)]}.
                                                               (4)

Moreover p>=1-E/g_r. If E<g_r this guarantees p>0, and the simpler upper bound is

 ||A|| min{2,L_ell(T)+2(2+M T)sqrt(E/g_r)}.         (5)

The trivial cap2 applies because both outputs are normalized states. The p-dependent statement also applies when E>=g_r if p is independently positive. It does not assert a positive projection probability from an uninformative energy lower bound.

The estimate is independent of the total volume and total energy. It uses only the finite ball energy and counts. For example an initial per-link bound Tr(rho_B K_e)<=e_loc gives E<=(e_loc+2v)N by(1), without any extensive global-energy premise. Choose ell first to make the polynomial-times-exponential L_ell small; for that finite region choose r to make the cutoff term small. No numerical optimization is used.

## 2. Strong-topology setting and explicit propagation constant

The local Hilbert spaces are separable and K_e is self-adjoint. In finite volume, bounded interactions give self-adjoint H on the free operator domain. Arbitrary bounded A need not preserve that domain or have norm-continuous free evolution. We therefore do not differentiate [H,A] on arbitrary vectors. The appropriate strong-operator calculus is supplied explicitly by [Nachtergaele and Sims, arXiv:1410.8174](https://arxiv.org/pdf/1410.8174), Proposition2.1, Lemma2.2 and Theorem3.1 steps1–4. The paper corrects earlier insufficient domain arguments. Its support-adapted interaction picture includes all onsite terms and interactions internal to X, so free evolution preserves X. The remainder is bounded and strongly continuous; strong Dyson integrals and the norm inequality for weak integrals apply. Their commutator iteration, equations(71)–(73), is the only imported propagation argument. No numerical velocity or finite-dimensional assumption is imported.

For clarity the actual constant here follows from direct counting in that iteration. For disjoint X,Y, it bounds the commutator by

 2||A||||B_Y|| sum_(n>=1) (2|t|)^n a_n/n!,

where a_n sums products of interaction norms over chains of n faces, the first meeting X, consecutive faces meeting each other, and the last meeting Y. Restricting to boundary faces in the support-adapted argument only decreases this sum. Every link belongs to four plaquettes; thus there are at most4|X| choices of the first face and at most16 choices of each subsequent face. Each product is at most v^n. Consequently

 a_n <=4|X|16^(n-1)v^n.                          (6)

A chain of n faces gives a link path from X to Y of length at most n, since the links in one face form a clique. Therefore a_n=0 for n<d(X,Y). For d>=1,

 sum_(n>=d)(32vT)^n/n! <=exp(-d) exp(32 exp(1)vT).

Combining this with(6) actually gives prefactor |X|/2 in front of ||A||||B_Y||. We use the weaker common bound

 ||[tau_t(A),B_Y]||<=2|X|||A||||B_Y||
                       exp(32 exp(1)vT-d(X,Y)).   (7)

For d=0, the same bound follows from the trivial commutator bound. For v=0 and d>=1 the chain sum is exactly zero even though the relaxed right side need not be. The strong-integral iteration remainder vanishes by the same factorial bound in each finite volume. Formula(7) is uniform over volumes, subsets of plaquettes and onsite kinetic strengths. The unbounded onsite terms do not contribute to the incidence count.

## 3. Boundary comparison and polynomial geometry

Temporarily decouple B from its exterior by removing only the C crossing faces. Keep all exterior kinetic and internal exterior interactions. This decoupled Hamiltonian evolves A exactly by H_B. Its difference from the full Hamiltonian is a bounded sum of crossing Phi_p, with the same free domain. The support-adapted/onsite interaction-picture Duhamel identity, interpreted as strong integrals, bounds the norm difference of the evolved A by

 sum_(p crossing) integral_0^|t| ||[Phi_p,tau_s^B(A)]|| ds.       (8)

One can equivalently prove(8) first in the bounded interaction picture and conjugate back; no unbounded commutator of A is used. Exterior-only faces have zero commutator. Each crossing face contains a link outside the ambient radius-ell ball. Since any two of its links are adjacent, every link of this face has distance at least ell from X. Thus d(X,p)>=ell. Apply(7) under the decoupled dynamics, with B_Y=Phi_p and ||Phi_p||<=v. Integration gives

 ||tau_t^Lambda(A)-tau_t^B(A)||<=||A|| L_ell(T).    (9)

This also holds at ell=0 by the trivial-overlap part of(7). At v=0 or T=0 the right side is exactly zero.

For(1), neighboring links have tail coordinates differing by at most1 in each coordinate. A radius-ell path from a link in X therefore stays within the coordinate cube of side2ell+1 about its tail. There are at most three outgoing links at each tail; union over X gives N's bound. Counting face-link incidences gives4F<=4N and C<=4N. Consequently

 L_ell(T)<=24 |X|² vT (2ell+1)^3 exp(32 exp(1)vT-ell).          (10)

It is important not to replace the polynomial geometric bound by an exponential degree bound: that would erase this useful spatial convergence. For a fixed infinite retained-plaquette interaction and its nested finite-volume restrictions, finite-volume local observables are norm-Cauchy by the same boundary estimate as balls grow. No claim of norm continuity in time on the entire bounded onsite algebra is needed. A locally normal infinite-volume state satisfying(2) gives the same expectation conclusion by this norm limit.

## 4. Finite-carrier error with mixed states and exterior correlations

The exact full-representation cutoff commutes with K_B and all local gauge actions. Any omitted link has kinetic energy at least g_r, minimized on the balanced first omitted shell. All other link kinetic terms are nonnegative. Thus, on quadratic forms,

 H_B>=K_B>=g_r(I-P).                             (11)

The bounded positive potential has norm at most M=2vF. Choose any purification psi of rho_B on B plus a reference. Finite energy(2) means psi belongs to the form domain of H_B tensor I, even when it does not belong to its operator domain. Let psi(t)=exp(-itH_B)psi. Energy conservation and(11) give ||(I-P)psi(t)||<=alpha for every t. The projected equation has only bounded cross term PV_B(I-P), since P commutes with K_B. In the form-domain extension of block32 projected Duhamel,

 ||psi(t)-exp(-itH_r)Ppsi||<=(1+M|t|)alpha.        (12)

One may establish this for spectral-cutoff initial vectors in the operator domain and then pass in form norm; the bounded cross term and conserved form energy control the limit. The reference is inert, so every step is unchanged for a purification. Normalizing Ppsi adds exactly1-sqrt(p) in vector norm. The trace norm of the difference of the corresponding normalized pure-state density operators is at most twice their vector distance, and partial trace is contractive. This proves the cutoff contribution in(4). Since 1-sqrt(p)<=sqrt(1-p)<=alpha, it implies(5). The preparation event P has the actual success probability p; the theorem does not turn this conditioned preparation into a deterministic channel for all inputs.

Finally, Tr(rho tau_t^B(A))=Tr(rho_B tau_t^B(A)) exactly, not approximately. This identity is why exterior entanglement does not introduce an extra error or require a product initial state across the boundary. Combining it with(9) and(12) proves(4).

## 5. Registers and scope

Put n=r+2. The exact link carrier dimension is

 D_r=n²(n+1)²(n-1)(n+2)(3n²+3n+2)/2880.

The region uses N ceil(log2 D_r) storage qubits in an encoding, with D_0=1 requiring zero nontrivial storage qubits. The compressed plaquette acts on four link registers within the finite carrier. This is not a four-qubit interaction, a compilation guarantee, or a claim that a globally inert unused-code extension retains four-register support. For physical gauge-invariant initial states the local reduction, cutoff and truncated closed-plaquette Hamiltonian respect the induced gauge actions; no separate per-link singlet compression is taken. Invariance of the reduced density matrix under boundary gauge conjugations does not put its support in the boundary-singlet vector space: boundary flux sectors can be present. The theorem uses the full tensor carrier and does not project them away.

The bound is about local expectation values and a specified finite-energy preparation. It is not whole-volume state approximation, a diamond norm over all inputs, or a continuum/physical-time identification. It does not use the small-coupling stability theorem of block34 and is valid for supplied v>=0, with a propagation radius that grows with vT. Finite r and ell resources depend on the stated tolerance and local energy, not on total lattice volume.

## 6. Frozen diagnostics

The preregistered checker constructs actual cubic faces and link balls, rather than an arbitrary bounded-degree graph. It verifies incidence, boundary distance, polynomial counts, balanced omitted thresholds and scalar endpoint cases. These finite exact checks support constants and indexing; the analytical all-volume propagation and form-domain proofs remain load bearing. No failed physical run was hidden and no parameter was fitted. Raw results are in result.json.
