# Ordered signed holes give a mobile variational lowering

This is a scratch candidate for independent review. It uses the supplied full-carrier dictionary and low-charge RK model of the canonical stability draft, not a new native primitive. The static parent already supplies nonempty D=2 support and ring-zero states. No novelty is claimed for standard particle-hole or variational mathematics.

## Why arbitrary two-component overlap is insufficient by itself

For fixed charge positions Q and ring components C,C', a permitted edge hop has a fixed fermion sign in the dictionary representation. Between normalized uniform component states its modulus is N_e(C,C')/sqrt(|C||C'|). It is positive if some configuration of C hops into C', but without component-size control this alone gives only a potentially tiny bound. Instead use the entire finite D=2 configuration set, which is a union of ring components and charge-position sectors. No ergodicity or component-size equality is required.

## Exact ordered-hole frame

Let |F> be the fully occupied fermion state. In a low-charge D=2 configuration z there is exactly one positive charge at x and one negative charge at y, with x!=y. The dictionary's fermion occupations are one everywhere except these two holes. Choose its fermion basis vector

 |eta(x,y)>=c_x c_y |F>,

where the order is by signed charge, not by vertex index. This differs from the usual occupation basis only by a position-dependent unit-modulus sign. Tensor it with the electric-link basis |z>. All these vectors are orthonormal because their link labels are distinct, and satisfy the exact Z2 Gauss constraints.

Put h_i^dagger=c_i, h_i=c_i^dagger. For i!=j, electron hopping c_i^dagger c_j=-h_j^dagger h_i. Acting on h_x^dagger h_y^dagger|F>, moving the positive hole x to a vacant target z gives -h_z^dagger h_y^dagger|F>. Moving the negative hole y to z gives -h_x^dagger h_z^dagger|F>; the two anticommutations in that calculation leave the same minus sign. Low-charge hopping preserves signed species and never targets the other hole. Thus every allowed native hop, after the exact W dictionary and this frame choice, has matrix element -1, with its accompanying link flip. There is no assertion about sectors with two holes of the same signed species.

Every ring keeps x,y fixed and maps to a positive link flip in this frame. Let Omega be the equal-amplitude normalized sum of all low-charge D2 link configurations in this ordered-hole frame. Each ring term annihilates Omega: configurations occur in flip pairs with equal amplitudes, including every ring component. Thus its ring energy is zero and its penalty is2U.

Each charged vertex has four eligible edge bits. At most one reaches the other charged vertex on the simple graph. Hence each configuration has at least6 and at most8 allowed undirected hops. Different edges give different configurations. Consequently

 <Omega,T_low Omega>=- average_z degree(z) <= -6.

For t>=0 this yields E_D2<=2U-6t. For t<0 multiply each configuration amplitude by epsilon_x epsilon_y. Every hop moves one charge across a bipartite edge, reversing this sign; rings preserve it. The hopping expectation changes sign while the ring energy stays zero. Therefore

 E_D2 <= 2U-6|t|.

The exact trial value is2U-|t| average degree, with average taken uniformly over the entire finite D2 configuration set. No count of that set is required for the inequality. Nonuniform nonnegative ring coefficients do not change annihilation.

Combining the earlier lower bound gives2U-8|t| <= E_D2 <=2U-6|t|. This is an absolute sector-energy interval. In the earlier stable regime U>=4|t| the neutral zero state is a ground state, so it is also the stated energy-above-ground interval. If U<3|t|, the upper trial is strictly negative, proving that neutral zero states are not global ground states in this supplied finite model. This does not classify the actual ground sector, settle the intermediate threshold3<=U/|t|<4, prove a band, transport dynamics, deconfined particles or a thermodynamic phase.

All winding sectors and all ring components are included. A separately fixed flux/winding sector or fixed magnetic-cycle code may invalidate support or the trial invariance. The phase-correct superposition is a variational vector, not an implemented preparation. Couplings, low-charge projector and RK Hamiltonian remain supplied.
