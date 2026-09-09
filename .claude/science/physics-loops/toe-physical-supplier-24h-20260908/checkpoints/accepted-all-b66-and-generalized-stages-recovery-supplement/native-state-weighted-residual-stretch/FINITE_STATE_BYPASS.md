# Avoiding an unnecessary infinite square-root-density approximation

This is a provisional continuation, not a claim that the native finite principal-angle modes have been constructed. Let the supplied finite-excitation theorem provide a normalized finite-mode state Φhat with ||Φ−Φhat||<=δΦ in the correct impurity Fock representation. For contractions T,U,

 ||(ΓT−ΓU)Φ|| <=2δΦ+||(ΓT−ΓU)Φhat||,
 ||ΓT Φ−ΓU Φhat|| <=δΦ+||(ΓT−ΓU)Φhat||.

Both are immediate from the triangle inequality and second-quantization contractivity. This changes which input supplier is needed: Qhat=sqrt(Nhat) is a finite positive matrix in the actually embedded finite-mode space. Its trace and weighted Gram can be computed with a finite certified square root. There is no need first to establish trace-norm continuity of sqrt(N) for arbitrary approximate infinite densities. In particular, do not infer ||sqrt(N)−sqrt(Nhat)||1 from ||N−Nhat||1 by a dimension-independent Lipschitz claim. The ordinary square-root Holder estimate in a different Schatten norm does not supply that assertion.

Let the finite-mode embedding be Y:C^d→H_+ with Y*Y=I, and let Q_d=sqrt(Nhat) in its natural one-body representation (any unitary coordinate basis is valid). Then

 Qhat=Y Q_d Y*,  M=Tr Q_d,
 M_Q=(S'*Y) Q_d (Y*S'),
 τ=Tr Q_d−Tr[H^-1(S'*Y)Q_d(Y*S')].

Therefore only a finite weighted cross-Gram S'*Y and the finite occupation matrix are needed, plus a certified initial-state errorδΦ. The prior majorant objective yields an absolute Fock propagation error bounded by

 δΦ + sqrt(M)[sqrt(τ)+E(t;x,ρ)]

for the target-versus-approximate-state comparison; use2δΦ for comparing the two propagators on the same original state. Input representation uncertainty, nonorthogonality of approximate Y, and scalar energy factors must be added separately. If Y is only approximately isometric, it must be corrected within an actual physical subspace or bounded by a separate embedding error; it cannot be treated as exact because a midpoint Gram is nearI.

For fixed CAR boundary insertions, use the separately proved creation/annihilation input errors and the corresponding finite occupied-mode factor, or form the finite excited state explicitly. No arbitrary high-degree estimate or determinant continuity follows merely from finite d. The mixed-Gaussian note's common-frame and HS/error assumptions remain necessary for its alternative pairing-based consumer.

This makes the missing native construction precise:8067 proves existence of exact principal-angle truncations but explicitly says quadrature columns do not yet compute those modes. A certified finite physical approximant and its overlap cross-Grams would close this interface. Existing stationary projector quadrature/Gram machinery is a candidate way to supply it; neither the completed24-mode leakage result nor this proof establishes that it does. This is a new sufficient route, not a weakening of the failed uniform leakage tolerance.
