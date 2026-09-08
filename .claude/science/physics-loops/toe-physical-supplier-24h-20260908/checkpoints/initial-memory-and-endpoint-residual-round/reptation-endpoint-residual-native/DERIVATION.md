# Finite-projector endpoint residual identities

Let H=V N-A be a real symmetric finite matrix, A nonnegative off diagonal with row sum N, and G=I-H/M symmetric nonnegative. Let n=2k, psi=G^k 1, Z=psi^T psi>0. The path probability is Z^-1 product_{j=0}^{n-1} G(x_j,x_{j+1}) with uniform unnormalized trial endpoints. All expectations below refer to this finite path measure; they do not require stationarity in projector length or ground-state preparation. Define h(x)=(H1)(x)=(V-1)N(x).

Summing paths with an endpoint insertion replaces the endpoint vector1 by h=H1. Since H commutes with G,

 E[h_L]=E[h_R]=psi^T H psi/Z=:E,
 E[h_L h_R]=psi^T H² psi/Z.

For a real diagonal midpoint X,

 E[X_mid (h_L+h_R)/2]=psi^T X H psi/Z.

Each endpoint individually has this same expectation by reflection and real symmetry. It is not generally E[X_mid h_mid]. In particular Var_psi(H)=E[h_Lh_R]-E², not the midpoint variance of h or the variance of one endpoint's h. Midpoint marginals are exactly psi²/Z.

For any collection of complex diagonal observables O_j set X=sum_j |O_j|² and S=<X>_psi>0. Expanding each symmetric off-diagonal pair gives

 sum_j <O_j psi,(H-E)O_j psi>/Z
 = (1/(2Z)) sum_{xy} A_xy psi_x psi_y sum_j |O_j(x)-O_j(y)|²
   + <XH>_psi-<X>_psi E.

The imaginary antisymmetric contributions cancel between x,y. Thus R=D+C/S, where D is the positive Dirichlet numerator divided by S, and C=Cov_path(X_mid,(h_L+h_R)/2). This holds even when O has a nonzero mean, but then it is not an inelastic ground-state spectral ratio without the corresponding subtraction. At finite psi, H-E need not be positive and R is a quadratic-form ratio, not a positive spectral moment about E0.

Operator Cauchy–Schwarz on (X-S)psi and (H-E)psi yields

 |C| <= sqrt(Var_psi(X) Var_psi(H)),
 |R-D| <= sqrt(Var_psi(X) Var_psi(H))/S.

Var_psi(X) is a midpoint fourth-observable moment; Var_psi(H) uses the endpoint cross product. This bound is exact but not necessarily statistically efficient. Correlated path samples require covariance-aware estimation; subtracting squared empirical means and taking ratios is not finite-sample unbiased. Negative noisy variance estimates must not be silently clipped into a claimed bound.

## Actual ice normalization and harmonic qualification

The supplied ice source uses O(q,b)=Volume^-1/2 sum_r exp(iq.r)(-1)^sum(r)(n_b(r)-1/2). The previously reviewed signed local identity in ice-spectral-moments/DERIVATION.md and its KINETIC_SUM_RULE_ADDENDUM.md gives |Delta O|²=qhat_a²/Volume for an ab-plane flip, zero for other planes. Therefore a SINGLE mode has Dirichlet numerator qhat_a² <A_ab>/(2Volume). For the six ordered transverse modes at one fixed harmonic h, every plane occurs twice, so their summed numerator is qhat_h² <A>/Volume. Since <A>=V<N>-E, the six-mode ratio is

 D_h=qhat_h² (V<N>-E)/(Volume <X_h>).

If X sums BOTH six-mode harmonics, the numerator is (qhat_1²+qhat_2²)(V<N>-E)/Volume, not one unspecified q² times that quantity. More general unequal directional momenta retain the separate plane-weighted kinetic expectations. A single mode cannot replace <A_ab> by the full <A> without an additional proved symmetry relation. These are inherited local-operator identities, not independently re-enumerated ice matrices in this probe.

The endpoint residual measures the failure of psi to be an eigenvector through observables accessible to the same finite path law. Small energy variance alone does not certify proximity to the ground rather than an excited state without further spectral/overlap input. None of these identities proves equilibration of a reptation chain, a low-variance estimator, a photon pole or a physical instrument selection.
