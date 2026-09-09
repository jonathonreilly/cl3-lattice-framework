# Uniform local perturbative coefficient and the connected-return obstacle

This is a first-principles partial result for the supplied full carrier H(U)=H0+U(3N/2+V), V=(1/2)sum_j W_j. It does not remove the finite-volume window in PR8060. No physical computation, additional uniform fermion gap, Gaussian spectator preparation, or interacting phase assumption is used.

Sources read in full or relevant proof sections: canonical NATIVE_WEAK_ELECTRIC_JOINT_DEFECT_BOUNDS_NOTE_2026-09-09.md; its density parent, including exact 24/8 incidence counts; native-weak-electric-local-control-next/DERIVATION_BEFORE_FINITE_VOLUME_5260.md (the unproved compression premise); native-weak-electric-local-stability-design/DERIVATION.md; native-zero-penalty-pi-dispersion/DERIVATION.md (canonical seams, active frequencies and spectator multiplicity). The earlier conditional compression is not adopted as a theorem.

## 1. A uniform coefficient for a prescribed local defect

Assume H0 >= E0 + kappa K, with K the number of bad elementary faces and kappa>0 as supplied upstream. Let psi(U) be any normalized finite-volume analytic eigenvector branch issuing from the ground eigenspace and which is a ground branch for sufficiently small positive U. Finite-dimensional analytic perturbation supplies such branches after resolving degeneracy; no uniform radius is asserted. Write psi0=psi(0). Since K psi0=0, every W_j psi0 has exactly the defect set F_j, of size 6 or 8. On that sector H0-E0 is invertible with inverse norm at most 1/(kappa |F_j|). Projecting the derivative eigen-equation into any nonempty flux pattern therefore gives

 Q_C psi'(0) = -(1/2) sum_{j:C subset F_j} (H0-E0)^(-1) W_j psi0.

The derivative of the scalar energy and any ground-space basis rotation disappear under Q_C. Other zero-face winding sectors cause no problem with this sectorwise inverse.

Crucial orthogonality: distinct incident-edge pairs have distinct F_j. Otherwise their symmetric difference T, containing at most four edges, meets every elementary plaquette evenly. Pick e in T. The edge belongs to four different elementary plaquettes. Every other distinct edge shares at most one elementary plaquette with e on a simple periodic cubic torus of even extent >=4. Each of those four faces requires another edge of T, forcing at least five edges, contradiction. This argument uses actual elementary faces, including extent-four seams, and does not identify zero face flux with a connected component.

Thus the vectors in the sum are orthogonal by their exact bad-face eigenvalues, even if psi0 has coherent winding or spectator components. Consequently

 lim_{U->0+} p_C(U)/U^2 = ||Q_C psi'(0)||^2
 <= (1/(4 kappa^2)) sum_{j:C subset F_j} 1/|F_j|^2.

For a single prescribed face f, the 24 perpendicular and 8 opposite incident pairs yield

 lim p_f(U)/U^2 <= [24/36+8/64]/(4 kappa^2) = 19/(96 kappa^2).

For |C|>8 this quadratic coefficient vanishes. The bound holds uniformly over normalized initial ground vectors and finite-volume analytic branches. It is a coefficient statement only: the o(U^2) is not shown uniform in volume. It must not be promoted to p_f <= constant U^2 at a fixed volume-independent interval, or to a joint contour bound. The local selection already shows that the first leakage coefficient is not itself obstructed by the active gap closing as 1/L.

## 2. A genuine gapless bath integrability lemma

In the canonical minimizing pi background the active positive frequencies are omega(k)=4|t| sqrt(sum_a sin^2 k_a), with the seam/twist conventions of the dispersion source. Use a fixed finite magnetic unit cell, and let C_L(x,tau) be the positive-frequency Euclidean vacuum propagator for tau>=0. Parseval and spectral calculus give, up to the fixed choice of unit-cell normalization,

 integral_0^infinity d tau sum_x ||C_L(x,tau)||_F^2
 = (1/number_of_cells) sum_k Tr[P_+(k)/(2 omega(k))].

There is a volume-independent O(1/|t|) upper bound on this expression for the canonical antiperiodic cubic grids. To see this without a uniform gap, partition momentum space into fixed neighborhoods of the finitely many conical zeros and their complement. In a neighborhood, sin-distance is bounded below by a positive constant times distance to that zero. Shells of grid radius j contain at most constant*(j+1)^2 points; the closest shifted-grid distance is at least constant/L. The normalized sum of inverse distances is bounded by constant L^(-3) sum_{j=0}^{O(L)} (j+1)^2 L/(j+1), which is bounded. The complement is uniformly bounded away from zero. Constants depend on the fixed unit cell and dimension, not L. Zero-mode winding sectors are not included in this assertion.

Wick's rule for centered fixed-support ACTIVE bilinears expresses their connected vacuum two-point function as a finite sum of products of propagator entries. Cauchy-Schwarz and the preceding identity therefore bound the absolute spacetime sum/integral of these connected bilinear correlations uniformly in L. No exponential spatial clustering or fermion mass has been inserted. This proves an infrared-integrable two-point bath input, not convergence of a perturbation expansion. It does not apply directly to a single active fermion channel or arbitrary spectator correlations.

## 3. Why this does not close the interacting joint bound

Actual W_j changes the flux background. A time history contains evolutions exp[-tau(H_F-E0)] with different F between electric insertions, rather than only the stationary pi propagator appearing in section 2. Histories with nonempty F have the useful exponential penalty exp(-tau kappa |F|). Histories returning to F=empty have arbitrarily soft active excitations and an exponentially large spectator ground space. The two-point lemma is not a bound on their connected multipoint kernels.

Three distinct missing steps must not be conflated:

1. A linked expansion must subtract disconnected exterior energy contributions. A bound on the unnormalized resolvent series still produces volume factors and does not establish the PR8060 compression relative to the true E_U.
2. One needs an operator-valued bound uniform in the spectator ground state, rather than Wick factorization of a chosen spectator state. The native reference ground space permits correlated spectators. Active Wick integrability by itself imposes no spectator clustering.
3. A summable connected-polymer majorant must hold to every order with controlled combinatorial growth and changing-flux Gaussian kernels. Pairwise integrability alone provides no such majorant and does not justify exchanging infinite-volume and small-U limits.

A precise next lemma would bound connected, vacuum-normalized, time-integrated electric histories touching a fixed face by A (B U/kappa)^n, with A,B independent of volume, retaining their spectator operator norm and subtracting disconnected vacuum pieces. Its flux intervals should use stiffness; its zero-flux returns should use the gapless active covariance. Establishing this lemma, or a local constrained-energy analogue, would be new load-bearing work. It is not supplied by the known dispersion, stiffness, or density inequalities.

The positive result obtained here is the exact uniform local quadratic coefficient and the square-integrable Euclidean active propagator. The fixed-U local ground-state joint-defect theorem remains open. In particular no mean-density inference, assumed positivity of diagram weights, or hidden active-gap replacement is made.


## 4. The actual dangerous return is odd-active, not an active bilinear

The preceding two-point lemma is insufficient even at the level of selecting the appropriate correlator. Three incident electric pairs can toggle the six edges of a full star. The native Gauss identification returns this flux to the reference orbit with an odd active insertion accompanied by an odd spectator insertion. Their product is physical and even. This is the same three-insertion vertex studied in the native third-star analysis; it is not an added interaction. At separated stars the zero-flux propagation therefore contains an odd-active transition correlator, with spectator factors retained as operators.

Let chi_v be the vacuum transition vector of that return and P1 its active one-particle projection. The exact one-particle contribution to the propagation between two such vertices is

 G_vw(tau)=<P1 chi_v, exp[-tau(Hactive-Eactive)] P1 chi_w>,
 integral_0^infinity G_vw(tau) d tau=<P1 chi_v,(Hactive-Eactive)^(-1)P1 chi_w>.

This is a single propagator. It cannot be replaced by a product of two propagators merely because the complete active-spectator operator is even. Arbitrary spectator states cannot be Wick-factorized to manufacture a second active decay factor. Multiparticle pieces add separate spectral contributions; their existence does not remove the one-particle channel by definition.

Here is a precise conditional obstruction to the simplest absolute connected-history bound. In a translation/magnetic-cell covariant one-particle description, suppose the vertex has form factor a(k). Its positive zero-frequency one-particle kernel has multiplier a(k)^* P_+(k) a(k)/omega(k) (or the corresponding matrix in the cell indices). If its positive numerator stays bounded below along momenta approaching a conical node, then the multiplier is unbounded as the grid approaches that node, of order L on the nearest antiperiodic momenta. For the finite convolution kernel T_L, the triangle inequality gives

 sup_k ||T_L(k)|| <= sum_x ||T_L(x)||.

Consequently no volume-independent absolute spatial summability bound is possible for this channel under that nonvanishing premise. This proof does not require a claimed pointwise Fourier asymptotic. It is a conditional algebraic obstruction to this particular majorant, not an assertion that the native form factor has a nonzero limit or that the interacting ground state is unstable.

The decisive native quantity is thus the one-particle star form factor near the Dirac nodes, not just the integrated active-bilinear susceptibility. A zero of a(k) at least linear removes the displayed inverse-frequency divergence, but boundedness of the multiplier alone still does not prove absolute summability; regularity estimates must be supplied. Alternatively one could retain and resum the induced spectator dynamics instead of expanding it in absolute histories. Such a resummation requires control of its gapless coupled reference and of the remaining defect insertions. The exact L4 vacuum identity, where all active frequencies coincide, cannot decide a node-vanishing condition on general tori.

The fixed-volume coefficient statement in section 1 has the order of limits sup_L limsup_(U->0+) kappa^2 p_f(U)/U^2 <=19/96. It is not limsup_(U->0+) sup_L. At each finite volume there are finitely many analytic Rellich branches. Taking the maximum of their uniform coefficient bounds also covers arbitrary ground-state mixtures, even with U-dependent mixing weights, for that fixed-volume limit. No uniform remainder follows.
