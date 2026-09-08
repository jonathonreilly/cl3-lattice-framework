# Constructive translation symmetry of the supplied mobile component

## Source and novelty scope

The source is the current supplied periodic binary-link ice model, not a primitive Record theorem. Read the actual initial_ice, vertex_degrees and electric_flux functions in spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py: n_a(r)=r_a mod2, degree3, and staggered electric plane flux. The geometric alternating-face rule and Fourier dictionary are the same source authority independently checked in the preceding energy-source review. Targeted main ICE-note searches found the known unique maximal L2 mobile component and full L2 enumeration, but no general-even-L translation construction. This limited search does not certify global novelty.

Let C_L be exactly the connected plaquette-flip component containing that seed on an even periodic L³ lattice. No claim that C_L contains every zero-flux configuration is needed.

## Explicit legal path and general lift

A face in plane(a,b) at root r has ordered bits on (r,a),(r+e_a,b),(r+e_b,a),(r,b); legality is0101 or1010. To translate the seed along direction0, use plane(0,1) roots, in order,

 (0,1,0), (0,1,1), (1,1,0), (1,1,1)

on the L2 torus. Direct substitution gives legal alternating bits at all four steps, and the endpoint toggles all direction0 links and no others. Paths for directions1 and2 are retained verbatim in RESULT.json; alternatively permuting coordinate names in this construction gives their existence because the seed is coordinate-permutation invariant.

For any even L, replace each root by the complete layer of roots with its three coordinate parities, retaining the same plane. Distinct roots in a layer differ by even coordinates; their unit plaquettes share no edge (including across the periodic seam). Therefore their flips commute and can be performed sequentially in any fixed order. A2-periodic configuration restricts on every such face to the same ordered four bits as the L2 configuration. Hence if the L2 step is legal, every layer face is legal before and throughout the layer. The layer endpoint is again2-periodic and is exactly the lifted L2 endpoint. Induction proves the entire path. It uses4(L/2)^3=L³/2 individual legal flips for each translated seed. This is a concrete polynomial-size path, not a general mixing estimate.

The executable independent coordinate checker verifies all three translations at L2,4,6, with4,32,108 moves respectively. It checks edge-disjoint layers, each actual binary flip, target equality, final degree3 and the actual staggered plane flux0. The first diagnostic computed total staggered flux; the final added plane test explicitly matches the source convention. Neither diagnostic was used to tune the path. L2 BFS found864 states; larger components were not enumerated.

## Component invariance and reflected seeds

A lattice translation sends legal flip paths to legal flip paths. Since every unit-translated seed lies in C_L, translation maps C_L onto itself: for x connected to seed, translate its connecting path and concatenate the constructed seed path. Inverses give equality. This is the missing component-level argument, rather than an inference from full-Hamiltonian symmetry alone.

Coordinate permutations fix the seed. Reflection of coordinate a sends an undirected a-link at r to the a-link at reflected r−e_a; its seed occupation toggles direction a, while other directions remain unchanged. Thus the reflected seed is the same reachable configuration as an a-translation. Reflections also conjugate legal faces to legal faces. These observations prove cubic reflection/permutation invariance of C_L as well, without asserting ergodicity among other components.

## Elastic Fourier mass

For O_ab(q)=L^(-3/2) sum_r epsilon(r)exp(i q r_a)(n_b(r)−1/2), take the state translation convention (tau_j n)_b(r)=n_b(r−e_j). For allowed torus momenta,

 O_ab(q,tau_j n)=−exp(i q delta_aj) O_ab(q,n).

Translation in ANY direction j!=a therefore changes its sign. This remains true at q=pi: longitudinal translation then has eigenvalue+1 and alone is insufficient, but a transverse translation still has eigenvalue−1. It also covers qmin=2pi/L and q0 with the explicit staggered definition.

The restricted H=V Nf−A+lambda sum|O|² commutes with these translations; the diagonal source is invariant since each O only acquires a phase. On the finite connected component its real positive ground vector is unique by irreducibility. Translation is a basis permutation, so it maps that normalized positive ground vector to itself. Consequently <O_ab>=−<O_ab>=0 exactly. The same holds for the uniform RK component state. Thus in THIS supplied component and symmetric source family, the raw Fourier second moments have no ground-state elastic contribution. At finite L the unique ground gives the only zero-energy spectral state relative to E0. A positive nonzero second moment therefore normalizes an inelastic measure, and its first moment gives an excitation-energy upper bound in the usual restricted observable sector.

This does not prove a pole, photon, a positive lower gap, convergence of finite-chain estimates, or uniqueness of the ground across all components. An explicitly translation-breaking source or preparation is outside the zero-mean conclusion. Finite stochastic samples may have nonzero sample means despite the exact stationary symmetry.
