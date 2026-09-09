# Independent equivariant native Gram-dilation proof review

PASS as a conditional exact mathematical construction, source DERIVATION d39d65ded04483fa725e5e6b569ea2835db44aeee1adff097981040d5b19ecdf, freeze3c1bb11632aedefa4819fbc66fade165c196758f8b88e181c6ee2ec1b9f37248. Complete proof read. No physical calculation or numerical feasibility conclusion. No required repair found; parity detail and the operator-monotonicity bridge are expanded below.

## Actual intertwining extension

From Gamma F=FJ and orthogonality, J^T M J=M, hence MJ=JM. Both kerM and its orthogonal complement are finite J-invariant real spaces. On suppM, V0=F(M|suppM)^-1/2 is an isometry intertwining J and Gamma. No unbounded inverse is applied on the kernel. ranF is closed (finite dimensional) and Gamma-invariant, so its orthogonal complement is also invariant and has infinite complex dimension. Any complex-linear isometry from kerM into that complement extends V0 as claimed. Realification preserves the exact complex-structure sign. This construction proves existence, not numerical recovery of an unknown physical embedding.

## Noncommuting square-root estimate

The Loewner argument is correct. For positive bounded A<=B, monotonicity of sqrt follows directly from sqrt(A)=pi^-1 integral_0^infinity t^-1/2 A(A+tI)^-1 dt and reversal of positive inverses: A(A+tI)^-1=I-t(A+tI)^-1. The integral converges in operator norm at both ends for bounded positive operators, including noninvertible ones. Thus if||A-B||<=delta, sqrt(A)<=sqrt(B+delta I)<=sqrt(B)+sqrt(delta)I, and the reverse inequality follows identically. The second inequality uses commuting functional calculus of B only. Consequently the self-adjoint difference has norm<=sqrt(delta), without asserting A and B commute. Finite dimension then gives HS<=sqrt(n delta).

Mplus is positive because Mhat>=M-epsilonI>=-epsilonI. Delta<=2epsilon. A common isometry V preserves HS norms, giving d<=sqrt(2n epsilon), uniformly over all admissible kernel extensions. Expanding (F+D)C(F+D)^T-FCF^T into three terms and using HS×HS→S1 gives c(2||F||HS d+d²). The separate coefficient error uses||Ftilde||HS²=TrMplus<=TrM+2n epsilon. Complexifying the real matrices leaves these finite-dimensional singular values unchanged; no extra factor two is needed.

## Projection and Fock meaning

With Gamma real skew, iGamma is self-adjoint and P0=(I+iGamma)/2 has conjugateI-P0. Exactly imaginary antisymmetric Ctilde gives self-adjoint Xtilde and the same complement identity. Trace-norm proximity eta implies operator proximity eta. For eta<1/2, its two spectral clusters lie inside the corresponding disjoint neighborhoods of0 and1. The radius1/2 circle about1 has PA resolvent norm2 and Xtilde norm at most1/(1/2-eta). The resolvent identity and contour length factor1/2 therefore give exactly eta/(1/2-eta), as stated. No equality of trace and operator errors is presumed.

ranV reduces Gamma and P0; Ftilde has range there. Its complement is unchanged by both Xtilde and its rounded projection. Thus the approximation is a genuine PH-symmetric finite-rank modification of the native reference polarization. The finite real CAR subspace has an actual Fock factor, and its pure quasifree covariance gives a normalized vector there, tensored with the unchanged reference vacuum. This is finite-mode/finite-excitation implementability, not localization in physical sites or a computed signed Gaussian kernel.

Parity is not asserted in the draft's conclusion. If needed for the native even branch, the PH-symmetric path PA+t(Xtilde-PA),0<=t<=1, also avoids1/2 because its distance fromPA is at mostt eta. Spectral rounding yields a norm-continuous restricted-polarization path, so relative parity is preserved from the parent PA. Finite-rank relative toP0 alone does not ensure even parity: flipping one occupied complex mode is a counterexample. The parent even-parity premise or this path must be cited before making an even-state claim. There is no such overclaim in the current text.

## What this repairs and leaves open

A single commonF and commonV make the abstract finite representation simultaneously native for both impurities. The approximation error is extension-independent, but individual overlaps/insertions are not determined by two unrelated extensions. The known-coefficient w=Fa estimate is correct since||V(sqrtMplus-sqrtM)a||<=sqrt(2epsilon)||a||. Appending w,Gammaw is legitimate only with all new Gram cross data and the exact expanded intertwiner. Generator/leakage/time bounds are genuinely separate.

The theorem therefore repairs the existence-level ghost-coordinate objection under a certified common Gram and exact symmetries. It does not show that today's midpoint data satisfy those hypotheses, give a unique canonical embedding, make unbound insertions meaningful, or transfer the single-impurity528 constants to an enlarged common carrier. These limitations are explicit and adequate.
