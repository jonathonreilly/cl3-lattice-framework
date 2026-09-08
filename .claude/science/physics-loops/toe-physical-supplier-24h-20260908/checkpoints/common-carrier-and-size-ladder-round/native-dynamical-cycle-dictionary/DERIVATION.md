# Full native edge carrier as a constrained fermion–Z2-link space

## Exact statement and premises

For every finite connected simple graph with ordered vertices and ordered neighbor lists, the entire native edge-qubit Hilbert space is unitarily isomorphic to the Gauss-invariant subspace of one CAR mode per vertex and one Z2 qubit per edge. The unitary intertwines all native A, B and physical Z operators, not merely a chosen fixed-cycle sector. It maps native cycles to magnetic Z2 Wilson loops and native hopping to CAR hopping dressed by the corresponding link X.

This is a mathematical enlargement and constraint dictionary, not additional physical sites, a selected dynamics, or an axiom-level matter/gauge identification. The supplied native graph and operator conventions remain imports. Relaxing the original cycle code changes the allowed state space; the dictionary does not make that relaxation automatic.

The source read is the native matter/instrument note's Definitions, equations (1)–(4), and Theorem 1, in the campaign main checkout. It gives B_i=product_{e incident i} Z_e and, for i<j,

 A_ij = X_e product_{edges preceding e at i or j} Z_f,
 A_ji=−A_ij,
 T_ij=(i/2) A_ij(B_i−B_j),
 S_C=i^length(C) product_{oriented C} A_ij.

A's square to one, anticommute for distinct edges sharing a vertex, and commute otherwise. Each A flips only its own Z bit. Cycles are Hermitian central involutions of the A/B algebra. These exact signs are retained.

## Enlarged space and Gauss basis

Let F be the ordinary finite CAR Fock space on m labeled modes; put P_i^f=1−2 c_i†c_i and gamma_i=c_i+c_i†. On F tensor (C^2)^{tensor E}, define

 G_i=P_i^f product_{e incident i} Z_e^g,
 Atilde_ij=−i gamma_i gamma_j X_e^g,
 Btilde_i=P_i^f,
 Ztilde_e=Z_e^g.

G_i are commuting involutions. Work on their simultaneous +1 subspace H_G. In the link electric basis x in {0,1}^E, Gauss fixes the unique occupation vector

 n_i(x)=sum_{e incident i} x_e mod 2.

Thus |n(x)>_F tensor |x>_g is an orthonormal basis of H_G. Its dimension is 2^E, not 2^(E+m−1). All m Gauss equations are independent on the enlarged space: their product is total fermion parity, not the identity there. On H_G this product enforces even total fermion parity. No independent odd-parity sector is included.

Every Atilde commutes with all G_i: at either endpoint the Majorana and link X each supply one sign. P_i^f and Z_e^g commute with G. On H_G, Btilde_i=product incident Ztilde. Atilde has exactly the native A pairwise commutation relations and the native A–Z commutation relations.

## Explicit global phase construction

Fix the standard Fock basis |n>=product_i (c_i†)^(n_i)|vac>, with increasing labels. Applying gamma_j then gamma_i for i<j gives

 gamma_i gamma_j |n> = (−1)^(sum_{i<=v<j} n_v) |n xor e_i xor e_j>.

Let a_e(x) be the native A_ij amplitude from x to x xor e, and b_e(x) the Atilde amplitude in the Gauss basis. Then

 a_e(x)=(−1)^(w_e dot x),
 b_e(x)=−i (−1)^(ell_e dot x),

where w_e is the ordered-star mask in the native definition, and ell_e is the mod-two sum of incidence rows for vertices i through j−1. Put M_e=w_e xor ell_e. Its diagonal entry M_ee=1: e crosses that vertex interval once, and is omitted from its own ordered-star dressing. Its off-diagonal entries are symmetric. One direct proof of this symmetry is that a_e and b_e have identical square-commutation signs for every pair e,f; taking their ratio cancels that sign and gives M_ef=M_fe.

Define the explicit unit-modulus phase

 d(x)=(-i)^{|x|} (−1)^(sum_{e<f} M_ef x_e x_f).

Then d(x xor e)/d(x)=−i (−1)^(M_e dot x)=b_e(x)/a_e(x), including the x_e=1 reverse step. Therefore

 W|x> = d(x) |n(x)>_F tensor |x>_g

is unitary from the native edge space ONTO H_G, and W A_ij=Atilde_ij W. Since W is diagonal in link labels it also intertwines every Z_e and B_i.

Equivalently, integrate the phase ratio along any path in the E-dimensional bit hypercube. Involution cancels backtracking and matching A commutators make every square flat; these moves generate all path equivalences. There is no residual Jordan–Wigner or global-cycle phase obstruction. The explicit quadratic formula exhibits that flatness without relying on a chosen graph spanning tree. W is not claimed to be a local physical circuit; the enlarged Fock representation and this basis change are mathematical coordinates.

## Hopping, cycles, and completeness

The source CAR identity, or direct expansion in c and c†, gives

 W T_ij W† = (c_i†c_j+c_j†c_i) X_e^g restricted to H_G.

For a simple oriented cycle C=(v0,v1,...,vr=v0), the Majorana product telescopes in the displayed order:

 i^r product_C (−i gamma_vi gamma_v(i+1) X_e^g)
 = i^r (−i)^r product_C X_e^g
 = product_C X_e^g.

The intermediate gamma pairs cancel without reordering, so this also covers odd cycles and the i^6=−1 native convention. Thus W S_C W† is the usual Z2 magnetic Wilson product. A fixed S_C=+1 native code corresponds to the zero-Wilson-flux restriction; retaining the full edge carrier retains all those flux sectors. Electric Z can change flux and does not commute with a loop containing that edge. Calling the sectors dynamical still requires a Hamiltonian containing terms which actually mix them: pure native T alone commutes every S_C.

This is a whole operator-algebra dictionary. Products of Z project onto individual link strings, and the A's connect every pair of strings by single-edge toggles with nonzero amplitudes. These products generate every matrix unit, hence the full native End(H_edge). Their images generate End(H_G). No untested extra relation among physical observables is being assumed from Hilbert dimension alone.

A literal Record projector (I+z Z_e)/2 maps to the electric-link projector with the same sign. Therefore existing supplied Kraus expressions built from native A/B/Z inherit the same algebraic dictionary. This supplies no occurrence law or new permission to update permanent recorded sites.

## Consequence for the charged-cycle construction

The earlier charged-cycle construction used n_e=(1−Z_e)/2, G_v=sum incident n_e−3, Q_v=epsilon_v G_v and |G_v|<=1 on the six-valent bipartite carrier. Those electric-bit functions and their projectors are unchanged by W. F_p S_p maps exactly to F_p product_{e in p} X_e^g; its alternating gate makes it the usual partial ring toggle, with no residual native phase. The low-charge hopping maps exactly to the low-charge projection of the CAR–Z2-link hop above.

Here c_i†c_i=(1−B_i)/2=1−Q_i^2 on the low-charge subspace. The mobile defects are holes relative to the filled fermion background. The hole parity obeys a background-minus Gauss convention, while the original fermion parity obeys G_i=+1. The positive and negative signed Q values are not two independent on-site CAR species: their sign also depends on the electric configuration. The integer divergence constraint is an additional link-state restriction, stronger than the Z2 Gauss equation. Consequently the result supplies an exact constrained Z2 matter/link dictionary and the previously proved hopping sign algebra, but not an independent U1 matter–link factorization, electromagnetism, deconfinement, photon or relativistic statistics theorem.

The new low-charge and alternating gates, relaxed cycle code, couplings and choice to use a Hamiltonian remain explicit supplied premises. Neither this isomorphism nor its dimension count selects those premises from Record/Admissibility.

## Prior overlap and finite evidence

The main September3 note `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS` was read completely. It explicitly adds a second designed spin-half link role per coarse edge and supplies a U1 Gauss kernel and Hamiltonian. That is a different enlarged physical carrier. This result uses the full existing native edge space and represents it as a constrained redundant Z2 space; it is not a proof that the earlier U1 role is unnecessary for that model. The targeted main search and this complete source comparison do not establish exhaustive literature/repository novelty; fermion–gauge encoding ideas are standard context.

The independently constructed finite checks cover triangle, square, square with diagonal (both sorted and reversed neighbor orders), and hexagon. Every electric-basis column is tested for phase-correct A, independent creation/annihilation T, B/Gauss and oriented Wilson cycles. The quadratic phase is checked against independently integrated edge-toggle phases. The omitted basis phase, omitted cycle i^length on odd/six cycles, and omitted link X all fail their intended identities. These are finite supporting controls for the proof, not numerical evidence for a phase of matter. No large Hilbert space or fitted input was used.
