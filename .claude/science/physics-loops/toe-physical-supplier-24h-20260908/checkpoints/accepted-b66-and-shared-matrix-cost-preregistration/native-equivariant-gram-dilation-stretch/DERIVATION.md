# A legitimate native embedding for a shifted common Gram approximation

Status: conditional-support proof draft. This is a proposed repair to the missing native interpretation of numerical Gram shifts. No actual Gram, embedding, projector, state, propagation or alpha is computed. Finite matrix arithmetic alone does not supply the physical inputs or observable embeddings below.

Let H_R be the actual infinite real one-particle Hilbert space, with orthogonal complex structure Gamma_0 (Gamma_0^2=-I), and let E=R^n carry the exact orthogonal complex structure J. Suppose the actual finite column map F:E->H_R satisfies Gamma_0 F=F J. Its exact Gram M=F^T F is real positive semidefinite and commutes with J. The coefficient domain must be even-dimensional. The complex Hilbert dimension of H_R orthogonal to ran F is infinite, so it can contain an equivariant copy of ker M.

## Equivariant extension, including an exact singular Gram

The polar partial isometry V_0 of F obeys F=V_0 sqrt(M), and Gamma_0 V_0=V_0 J on ran M. This follows from M commuting with J and the polar identity, first on positive eigenspaces. The kernel and range of M are J invariant. Choose any orthonormal complex basis of ker M and the same finite number of orthonormal complex vectors in (ran F)^perp. Their realification extends V_0 to an isometry V:E->H_R satisfying V^T V=I and Gamma_0 V=V J. Thus F=V sqrt(M) on all E. The extension is not uniquely selected, and no unknown physical law is introduced: it is a mathematical coordinate/approximation choice in the already supplied one-particle space.

Suppose a real symmetric numerical midpoint Gram Mhat commutes EXACTLY with J and ||Mhat-M||<=epsilon has been proved, with epsilon>=0. Let Mplus=Mhat+epsilon I. Then Mplus>=0, it commutes with J, and ||Mplus-M||<=2epsilon. Define the actual-space approximate columns Ftilde=V sqrt(Mplus). Positive-square-root Holder continuity gives

 ||sqrt(Mplus)-sqrt(M)||<=sqrt(2epsilon),
 d=||Ftilde-F||_HS<=sqrt(2 n epsilon).

This standard inequality must be supplied with a proof or explicit mathematical bridge in a final package. A short proof uses operator monotonicity of square root: Mplus<=M+delta I implies sqrt(Mplus)<=sqrt(M+delta I)<=sqrt(M)+sqrt(delta)I, and the reverse inequality follows by interchanging M and Mplus, with delta=||Mplus-M||. The commuting scalar inequality is used only for sqrt(M+delta I), not to assume the two Grams commute.

For any coefficient C on E with ||C||<=c, trace-ideal Cauchy-Schwarz gives

 ||Ftilde C Ftilde^T-F C F^T||_1
 <= c(2 sqrt(Tr M) d+d^2)
 <= c[2 sqrt(2 n epsilon Tr M)+2 n epsilon].             (1)

This recovers the existing single-impurity ledger's1056epsilon when n=528, without claiming that Mplus equals the native Gram. It is uniform over the arbitrary equivariant kernel extension. The exact midpoint coefficient approximation Ctilde has an additional charge ||Ftilde||_HS^2 ||Ctilde-C|| <= (Tr M+2n epsilon)||Ctilde-C||. Physical quadrature/input error is added separately. No inverse of M or positive lower eigenvalue is assumed.

## When spectral rounding produces an actual native pure approximation

Let P_0=(I+i Gamma_0)/2 on the complexification. Suppose C=iR with R real antisymmetric (hence C Hermitian), and the actual unrounded model P_0+F C F^T approximates the actual impurity projection P_A in trace norm by eta_quad. Construct

 Xtilde=P_0+Ftilde Ctilde Ftilde^T,

where Ctilde is also exactly imaginary antisymmetric. It is self-adjoint and its conjugate is I-Xtilde. Combining (1), coefficient error and eta_quad gives ||Xtilde-P_A||_1<=eta. If eta<1/2, the spectrum avoids1/2, and Ptilde=1_(1/2,infinity)(Xtilde) is an actual orthogonal projection on the native complexified H_R obeying conjugate(Ptilde)=I-Ptilde. A radius1/2 contour around1 gives

 ||Ptilde-P_A||_1 <= eta/(1/2-eta).

Indeed the exact P_A resolvent on that circle has norm<=2; the perturbed resolvent has norm<=1/(1/2-eta); the contour length divided by2pi equals1/2. This is a sufficient conservative bound. The perturbation and rounded difference are finite rank relative to P_0 because ran V is Gamma_0 invariant; outside ran V, Xtilde=P_0. Hence it defines a finite-excitation quasifree pure-state approximation in the supplied reference Fock representation. Trace-distance/state-error conversion remains a separate established bound; no small alpha error is inferred just from eta<1/2.

On the abstract finite E frame, P_0 restricts to (I+iJ)/2 and Xtilde is represented by (I+iJ)/2+sqrt(Mplus) Ctilde sqrt(Mplus). Its numeric spectrum therefore has a legitimate native-space interpretation once the hypotheses above are certified. Arbitrary extra coordinates are not silently declared physical modes: the explicit equivariant isometric extension is what proves the representation exists. The output still approximates the supplied native object, and does not equal it.

## Common-frame and observable obligations

For two impurities use ONE actual common F and ONE V before forming both approximate projections. Separate arbitrary extensions do not determine their relative overlaps. The common enlarged-frame errors must be budgeted with its actual n and Tr M; single-impurity constants do not automatically transfer.

An inserted local vector w must have its relation to this frame proved. If w=F a for a known exact coefficient a, define wtilde=Ftilde a; then ||wtilde-w||<=sqrt(2epsilon)||a||, with any physical input error added separately. More generally append w and Gamma_0 w as columns before constructing the common Gram, preserving the exact intertwining structure, and certify every new cross entry. If w is not included and its projected/remainder data are unknown, finite-matrix Gaussian formulas do not yet compute its native insertion. The same warning applies to one-particle generators: frame compressions, leakage and Duhamel/time errors require separate certification.

Thus this theorem would remove the logical objection to a shifted Gram representation, under a proved common Gram and exact symmetry structure. It does not remove the absent observable/generator contracts or provide a unique native embedding from scalar data alone.
