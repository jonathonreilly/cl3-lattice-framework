# Uniform absolute-error quench compression without an overlap denominator

## Initial approximation in the stationary impurity Fock space

Use the explicit principal-angle construction from FOCK_AND_QUENCH_EXTENSION.md, now expressing the original vacuum Omega in the impurity-vacuum representation. Projection symmetry gives the same trace bound L=87 in either direction. Retain every fully occupied exceptional mode (there are fewer than L), and order the remaining paired angles by decreasing s_j=sin(theta_j). Their doubled projection trace contributions are4s_j, so in particular sum s_j<=L is a conservative bound independent of conventions about counting pairs.

Let Omega_r retain the first r paired creation factors and all fully occupied exceptional modes, replacing every other paired factor by its empty factor. It is normalized and finite-excitation, with at most2r+L occupied-mode capacity. Fix its phase through the explicit ordered paired product, so

 <Omega_r,Omega>=product_(j>r) sqrt(1-s_j²)>=0.

This is an overlap with the APPROXIMATED ORIGINAL STATE, not a presumed nonzero overlap between the two vacua. All angle-pi/2 exceptions have been retained, so none are discarded in this product. The omitted paired factors have even parity and therefore the truncation preserves relative parity.

From descending order, s_(r+1)<=L/(r+1), and

 sum_(j>r) s_j² <= L²/(r+1).

Using product sqrt(1-x_j)>=1-sum x_j whenever the latter is positive (otherwise use the trivial nonnegative bound) gives

 ||Omega-Omega_r||²=2[1-product_(j>r)sqrt(1-s_j²)]
 <=2 sum_(j>r)s_j² <=2L²/(r+1).                 (1)

Thus r+1>=2L²/epsilon² guarantees initial Fock error at most epsilon. This is constructive mathematically, but the coarse constant makes it unsuitable as a claim of affordable rank. The actual singular tail could improve it only after certification. No root determinant branch is chosen numerically in this argument; phase is fixed by the paired-product construction or an equivalent continuous lift.

## Uniform unnormalized propagation

In the impurity representation the actual quadratic Hamiltonian has

 D_A=Delta E_A+dGamma(omega_A), omega_A>=0,

with its scalar impurity ground-energy difference retained. Its implemented constant must be the actual normal-ordering energy, not an arbitrary scalar from one-particle diagonalization. The reviewed positive impurity energy bound gives Delta E_A>=delta. Therefore

 ||exp(-tau D_A)(Omega-Omega_r)|| <=exp(-delta tau) epsilon. (2)

There is no conditioning factor and no division by a reference overlap or evolved norm. Finite excitation number is preserved: each occupied orbital is propagated by the one-particle contraction exp(-tau omega_A), and a k-particle wedge is propagated by its k-fold exterior power. The vectors need not remain orthonormal. Their wedge/product representation and Gram determinants can be retained without normalization. Orthogonalizing them is an implementation choice whose errors must be certified, not a condition for the mathematical bound.

For the overlap kernel with normalized initial approximants independently constructed for A and C,

 |<E_C(t)Omega,E_A(s)Omega>-<E_C(t)Omega_rC,E_A(s)Omega_rA>|
 <=exp[-delta(t+s)](epsilon_C+epsilon_A).        (3)

The two impurity representations must be compared through their physical common CAR/Fock representation, including relative lift phases. Formula (3) does not compute that comparison for free. It isolates an overlap-free error budget. Analogous bounded-insertion estimates cost the insertion norm when the approximated vectors are directly on its two sides. The complete node's internal insertion integrals still require the corresponding source-state approximation/propagation, and are not automatically covered by merely evaluating (3).

## Why normalization cannot have the same bound

A two-level even-sector counterexample is sufficient. Let D=diag(delta,delta+g), g>0, and psi_epsilon=epsilon|0>+sqrt(1-epsilon²)|2>, while phi=|2>. Their initial distance tends to zero with epsilon. At large time the normalized evolution of psi_epsilon tends to |0>, but that of phi remains |2>; their distance tends to sqrt2. Absolute unnormalized evolution obeys (2) throughout. Thus an error bound for normalized states independent of their surviving norm is false, even for a positive gapped quadratic two-mode model. This does not obstruct the unnormalized kernel route.

## Concrete remaining inputs

The route genuinely eliminates the earlier need to isolate an invariant exceptional subspace or bound a normalized moving-chart Gram matrix. It needs certified impurity principal-angle tails and their orbitals, a phase-consistent map into the common representation, the scalar Delta E_A, and a certified one-particle contraction on the retained finite orbital set. The stationary projector trace bound proves existence but its universal rank estimate is very large: L87 gives r+1>=15138/epsilon². No physical computation, affordable-rank claim, or alpha-sign inference is made. A controlled low-rank approximation to the actual stationary projector and its energy is now a precise alternative to finite-time normalized chart compression.
