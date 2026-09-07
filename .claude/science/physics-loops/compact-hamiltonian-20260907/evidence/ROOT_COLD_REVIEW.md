# Cold review of independent root compact-Hamiltonian proof

Reviewed root DERIVATION.md SHA2984f2e9a4beff97083b47c55c2265eb6b67918103c830b32baefacb600de5a2 only after freezing my independent derivation ea14e01aa46f135f41b7b796c1df81fe3a18b9458e8cf068a00b8345be259cb0. Verdict PASS. The Hamiltonian graph-domain telescope is a sound sharpening and simplification of my independent H4-Dyson stability route. Prefer it for the canonical rate, while retaining explicit local-moment/Taylor justification and both frozen derivations.

## Coefficients and local consistency

Our independently derived models and coefficients agree: exact compact spatial V=v sum(1-ReTr/3), temporal normalized Wilson parameter a/h, scalar exp(-6hv)c0(a/h)^-12 relative to the full Wilson transfer, and H=-(3/(2a))Delta_tot+V. Trace-orthonormal fundamental Casimir8/3 gives kinetic4/a. Root correctly says the isolated colored coefficient is not a physical singlet excitation.

The unique identity minimum, even exponential action and Haar density give normalized covariance3/b withO(b^-2), vanishing odd chart moments and fourth momentO(b^-2). The product96-dimensional increment is used only for an L2 unitary translation Taylor remainder. Its group structure yields a finite directional-derivative bound on H4 without a Sobolev embedding. No weak-field assumption on the boundary vector enters. Complement probability is exponentially small and is used only to bound the omitted unitary convolution by2||f|| times that probability. This is appropriate here, unlike a kernel-HS estimate that would require amplitude tails.

The smooth multipliers preserve H4 and H2, and their small-h expansion is valid in these multiplier norms. The cross term K(M_h-I) uses H2 regularity and isO(h); after the exterior kinetic h it isO(h²). There is no commutation of K with V. Thus the stated H4-to-L2 one-step consistency is sound.

## Hamiltonian squared domain and graph equivalence

Write A0=-Delta_tot and kappa=3/(2a)>0. Spectral Sobolev H2 is D(A0), H4 is D(A0²); these labels are distinct from the operator square H². H=kappa A0+V is selfadjoint on H2 by bounded real perturbation and nonnegative because V>=0.

If f belongs to D(H²), then f lies in H2 and Hf lies in H2. Since multiplication by smooth V maps H2 to H2, kappa A0 f=Hf-Vf also lies in H2. Thus A0 f belongs to D(A0), hence f belongs to D(A0²)=H4. Conversely f in H4 has both A0f and Vf in H2, so Hf lies in D(H) and f belongs to D(H²). This proves equality of domains, not merely a formal expansion on smooth functions.

Both (D(H²),||f||+||H²f||) and (H4,||(I+A0)²f||) are complete graph spaces. The identity map has closed graph because convergence in either graph norm implies the same L2 limit; the closed graph theorem gives norm equivalence. The forward explicit bound also follows from H²=kappa²A0²+kappa(A0V+VA0)+V² on H4. Therefore the local consistency bound may legitimately be repriced by ||f||+||H²f|| with a fixed finite constant. No lower-order norm is silently dropped: ||f|| is retained in the graph norm.

## Semigroup, rate and spectral cutoff

For positive selfadjoint H, spectral calculus gives ||(e^-hH-I+hH)f||<=h²||H²f||/2 for f in D(H²). It also gives e^-sH D(H²) subsetD(H²), H²e^-sHf=e^-sH H²f and contraction in both graph components. Thus the exact telescope with right factors e^-jhH gives

 ||F(t/n)^n f-e^-tHf|| <= C t²/n (||f||+||H²f||)

for sufficiently small h=t/n. This replaces my larger exp(C_Vt) H4 bound and is fully valid. Density plus the contraction of both families yields strong convergence for every L2 vector, including after the commuting physical gauge projection.

For P_E=1_[0,E](H), every vector P_E f belongs to D(H²) and ||H²P_E f||<=E²||f||. Therefore

 ||(F(t/n)^n-e^-tH)P_E|| <= C t²(1+E²)/n.

This is a right-input energy-cutoff operator norm bound. It neither asserts that F preserves the cutoff nor inserts P_E between transfer steps. If E grows with n the E² price must remain; it is not a global uniform operator-norm rate. The source's statement is correct; the displayed right-projector formula is recommended in the canonical version.

## Physical and historical scope

The full gauge-invariant space is reducing for H and each F, so restriction retains the domain argument and actual layer gluing. No source map/reset is introduced. The spatial potential is the exact nonlinear compact plaquette function, not its Hessian. Selfadjoint H defines mathematical real-time unitaries, but Euclidean convergence supplies no physical clock/occurrence or continuum-space interpretation.

The literature statement is properly limited to historical provenance. Root records reading official APS abstracts only, not the paywalled full proofs, and imports no coefficient from them. Kogut–Susskind1975 and Creutz1977 must be credited rather than calling the generic Hamiltonian limit novel. The claimed repository bridge is the explicit supplied normalization, physical reducing space and quantitative graph/core estimate.

Canonical wording: consistently write H² for the Hamiltonian square, and mathsf H^2/mathsf H^4 or H_Sob^2/H_Sob^4 for Sobolev spaces. The present plaintext clarifying sentence prevents a mathematical ambiguity, but typography will make the domain proof auditable. No scientific correction or new fixture is required.
