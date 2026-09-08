# Exact zero-penalty endpoint of the full native Hamiltonian

## Supplied model

Set U=0 in the SAME supplied full native H=UD+g sum_(i<j) lambda_ij A_ij, with real coefficients. Retain the full edge carrier, no hard charge or fixed native-cycle restriction. Use the exact8038 dictionary A_ij=−i gamma_i gamma_j X^g_ij on the all-positive Gauss space, G_i=P_i^f product_(e incident i) Z_e^g. This endpoint statement does not identify a physical coupling or phase, nor a limit of the low-charge two-species model.

Let the finite graph be connected, simple and loopless with v>=2 vertices and e edges. The cubic lane has even v; the argument also covers odd v in the parent dictionary domain. Choose a spanning tree. The link-X values xi_e=±1 label the redundant link basis. Local gauge transformations flip xi on their incident stars and act on matter by P_i^f.

## Gauge quotient and exact dimensions

Connectedness implies that the action on link-X configurations has kernel consisting only of the identity and the product of all vertex gauge transformations. Thus each link orbit has2^(v−1) elements, and there are2^(e−v+1) orbits. Products of xi along cycles label those orbits; a tree gauge sets every tree xi to+1, leaving the chord fluxes as independent signs.

The stabilizing product of all Gauss transformations acts on matter as total fermion parity. Invariance therefore requires EVEN matter parity. For any even Fock vector psi and chosen tree-gauge representative xi, the normalized sum over the2^(v−1) distinct gauge transforms of psi tensor|xi> is a Gauss-invariant vector. Its summands have orthogonal link states, so this is an isometry. Conversely, any Gauss-invariant vector on the orbit is determined by its coefficient at one representative, which must have even parity. This proves surjectivity and does not replace Gauss constraints by an informal gauge choice.

Every flux sector is therefore exactly an even-v-mode Fock space of dimension2^(v−1). Multiplying by2^(e−v+1) gives2^e, the whole native edge dimension. All sectors occur; neither an odd-matter sector nor an extra global gauge qubit is present.

The gauge-invariant Hamiltonian acts under this isometry as

H_xi=−ig sum_(i<j) lambda_ij xi_ij gamma_i gamma_j
     =(i/4) sum_ij gamma_i K_ij gamma_j,
K_ij=−2g lambda_ij xi_ij for i<j, K_ji=−K_ij.

The factor2 follows because the double sum has two equal contributions per unordered edge. Link fluxes are constants of motion at U=0. This fixed-flux decomposition is exact, not a mean-field treatment of a fluctuating link field.

## Energies and residual degeneracies

A real orthogonal transformation brings the real antisymmetric v-by-v K into r nonzero2-by-2 blocks [[0,omega_a],[-omega_a,0]], omega_a>0, and v−2r zeros. The transformed active Majoranas obey the same Clifford algebra. For each nonzero pair define d_a=(eta_(2a−1)+i eta_(2a))/2. Then

H_xi=sum_(a=1)^r omega_a(d_a†d_a−1/2).

An orientation change of an individual pair exchanges d with d†; the full energy multiset is unaffected. The frequencies are the positive eigenvalues of iK (equivalently the nonzero singular values of K, one per pair). A single edge with coupling g lambda has omega=2|g lambda| and energies±|g lambda|, fixing the convention.

There are v original spectator Majoranas bar_gamma_i=i(c_i†−c_i), none appearing in H. Along with the v−2r active zero modes they leave2(v−r) zero Majoranas, or v−r zero-energy fermionic degrees of freedom. Since r<=floor(v/2), at least one zero fermion remains. For every fixed occupation pattern of the r active modes, imposing even TOTAL matter parity removes exactly half the2^(v−r) zero-mode states. Hence each active occupation pattern has multiplicity

2^(v−r−1).

This is a precise pattern multiplicity. If different active patterns yield the same numerical energy, their multiplicities add. At generic full active rank with even v, r=v/2 and this becomes2^(v/2−1). If active zero modes occur it increases; at K=0 it becomes2^(v−1), as required. For odd v at maximal rank r=(v−1)/2 it is2^((v−1)/2). No claim that the individual spectator Majoranas are physical observables is required: a single spectator changes parity, while the dimension count concerns allowed even combinations and the residual Clifford module.

In each flux sector the bottom energy is −(1/2)sum_a omega_a with exactly the residual multiplicity above (unless additional active frequencies vanish, already included by reducing r). The global bottom is the minimum over all2^(e−v+1) flux sectors. The derivation gives a finite exact optimization problem; it does not solve that optimization on a cubic lattice or import a flux-phase theorem in three dimensions.

## Relation to finite coupling and interpretation

The zero-penalty endpoint has exact static flux sectors and extensive spectator degeneracy. A nonzero UD term need not preserve this decomposition and is not covered by the free endpoint solution. No continuity of a phase, protection of a photon, thermal preparation or realization of free propagating physical particles is inferred. The supplied native Hamiltonian remains the physical premise. The exact diagonalization and gauge quotient are standard finite Clifford mathematics, not a novelty claim for free-Majorana theory.

## Exact finite controls

The independent finite implementation constructs native Pauli A matrices and the oriented native cycle S directly, and constructs CAR Majoranas separately in the full vertex occupation basis before restricting to even parity. For each triangle/square flux it compares all spectral moments through the sector dimension, then independently checks the predicted frequency/multiplicity spectrum. Fifty-four exact predicates pass. The triangle is only a control in the broader dictionary domain, not a nonbipartite extension of the cubic physical lane.

At g=lambda=1 the triangle has one frequency2sqrt3 and energies±sqrt3 with multiplicity2 per flux. The square's flux− sector has frequency4 plus active zero modes and energies±2 with multiplicity4. Its flux+ sector has two frequencies2sqrt2 and energies−2sqrt2,0,+2sqrt2 with multiplicities2,4,2. These examples test both generic and zero-mode counting and the factor2 in K. They do not suggest a three-dimensional optimal flux.
