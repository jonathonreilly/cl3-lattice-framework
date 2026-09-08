# Full native carrier with soft charge penalty

Independent result frozen before reading root's soft-penalty candidate. Let the physical carrier be ALL edge qubits of a finite simple even cubic torus with extents>=4. Qv=epsilon_v(deg_v−3), D=sumQv²; now Qv can range from−3 to3. Take H=UD+g sum lambda_e A_e, U>0, with actual native Hermitian edge generators and no low-domain sandwich. P is the full ice projector. Couplings and penalty remain supplied.

## Fourth order survives exactly

Every ice departure by one edge has D2. The canonical folded calculation gives H2=−sum lambda²/(2U) and H4=−PVRVRVRVP+(sum lambda²)²/(8U³), with R=(1−P)/(UD).

For incident edges of equal initial bits, the newly permitted two-edge state has D6. Its four irreducible words still have signs−,+,+,− and the same denominator2×6×2. They cancel. Opposite bits have D2 and the same cancellation. Disjoint pairs and single-edge folded terms are unchanged. Thus H4 diagonal remains [sum lambda⁴/8+sum_incident lambda_e²lambda_f²/4]/U³.

An alternating square has only D2 orD4 intermediate states in every ordering; no new state changes its24-order sum. Therefore the ring coefficient is still eta_C product lambda/(2U³) relative to cyclic native S_C. Extent-four winding cycles remain included. No flippability diagonal is generated at fourth order.

## Canonical sixth-order extraction

Fix the canonical direct-rotation effective Hamiltonian. Physical Z_e covariance makes each diagonal analytic coefficient even in each coupling. At degree6 its support has at most3 active edges. These form forests. With exterior ice bits fixed, leaf induction gives one ice state in each active block. Hence its exact scalar low eigenvalue supplies the canonical diagonal coefficient, including energy feedback/folded terms. Vertex-disconnected active sets factor and their inclusion-exclusion connected coefficient vanishes. This argument does not invoke a low-domain truncation.

Exact intermediate-normalization recursion is
E_n=<0|V psi_(n−1)>,
psi_n=−R Q[V psi_(n−1)−sum_(j=1)^(n−1)E_j psi_(n−j)].
All2^k active bit states are retained. For one edge, incident pair and star, anticommuting paths cancel before any nontrivial double excitation is reached from the bright vector. Their energies remain1−sqrt(1+k g²), giving connected sixth coefficients−1/16,−3/8,−3/8, respectively.

For a three-edge path, let d be the energy of the triple toggle. Unlike the hard model, that state is always present:
d=2+4*(number of equal adjacent bit pairs), so d=2,6,10.
Use |s>=|1>+|2>+|3> and |o>=|101> (the outer-edge double toggle). Then V|0>=|s>, V|s>=3|0>+2|o>, V|o>=|1>+|3>−|111>. Adjacent-double terms cancel, regardless of their energies. The recursion gives E2=−3/2, E4=7/8, psi3(111)=1/(4d), psi4(o)=−7/32+1/(16d), and
E6=−(35+2/d)/32.
Subtracting the three single-edge and two incident-pair contributions gives connected path coefficient−(5+2/d)/32. Thus d2,6,10 give respectively−3/16,−1/6,−13/80. High-charge excursions change the local coefficient; they have not been silently removed.

## Uniform sum is still scalar

For each middle edge, each endpoint has three other opposite-bit edges and two same-bit edges. Among25 paths, there are9 with d2,12 with d6 and4 with d10. These counts hold for every ice state. Cubic motif totals are3N edges,15N incident pairs,20N stars,75N paths, where N is vertex count. Hence

H6_diag=−[3N/16+45N/8+60N/8+3N*(9*3/16+12/6+4*13/80)]lambda^6/U^5
=−1053N lambda^6/(40U^5) P.

This differs from the hard-projected−207N/8 result by−9N/20. It remains constant for uniform magnitudes; arbitrary real edge signs drop out. Inhomogeneous weighted sums need not be constant. Sixth-order offdiagonal terms are not calculated.

## Finite fourth-order error remains valid

On the full carrier signed charges are integers with global sum zero. Any nonice state has D>=2, so the unperturbed Q-block gap remains2U. Every ambient A_e has norm1, hence ||gV||<=a=|g|sum|lambda|. Ice has fixed total occupied-edge parity, which eliminates all odd P-to-P V words. These are exactly the ingredients of the independently reviewed Schur remainder proof44bc39bb: for a<=U/4, every ice-descended eigenvalue has one-sided distance at most a^6/U^5 from the actual fourth-order Hermitian operator. Its Weyl isolation, nonzero P component, scalar second-order normalization and Neumann bounds apply unchanged. This is finite-volume norm control, not a thermodynamic assertion.

## Evidence and boundary

check.py is a new exact rational forest recurrence, retains all active states and compares its outputs to the derived table. It includes the newly allowed d6/10 values, an independent24-order ring sum, a bare-X adverse comparison and all200 local ice endpoint assignments. No root conjecture or implementation was read. The preserved HARD_REFERENCE.py is historical, not an executed input. No stochastic computation or whole-lattice enumeration is performed.

The hard low projection is removed from this conditional ring mechanism. This does not extend the two-species no-double U1 dictionary beyond its low carrier: additional high-charge states require another representation if one is sought. It does not select A couplings, penalty, initial state, a probability law or an RK potential. Original hard-domain theorems remain separate.
