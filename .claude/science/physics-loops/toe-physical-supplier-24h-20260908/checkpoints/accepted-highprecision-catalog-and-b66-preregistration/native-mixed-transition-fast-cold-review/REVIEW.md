# Independent cold review of fast mixed-transition certificates

Disposition: PASS for the prospective mathematical certificate method. Reviewed complete DERIVATION7e631e53, check.py3482e799, protocol, pre-run hash, result and timing, and all8 pins in freeze3cfb9ed8c7e391d4fe8a910c8ecc81dea7cb5153567808b1775f9f76ff66a2c5. Every pin matches. This reviewer authored the imported mixed-overlap/CAR theorem; that theorem is reused openly. The doubling/LU/log construction and its source are independently reviewed here, not authored by this reviewer. No B66 source was changed and no native computation occurred.

## Algebra and inverse certificate

The simultaneous recurrence S2n=Sn+PnSn,P2n=Pn² is correct without normality. After11 doublings the sum contains2048 terms and the stated exact tail is below1e-15. There are22 products, or21 if the final unused power is omitted. The fresh residual identity M^-1-Shat=M^-1(I-MShat) proves the claimed bound with g=1-q. Input-matrix error contributes eta||Shat|| by the triangle inequality. In implementation the displayed sum is the certified residual upper bound to use; no arbitrarily smaller rho is justified. The optional forward bounds correctly include both cross-error and quadratic terms. No vendor product accuracy is asserted.

## Real LU and scalar logarithms

For eta<g, M+tDelta remains invertible by the singular-value perturbation bound. Its real determinant therefore has constant positive sign. Row-permutation parity and all non-unit diagonal factors must be included exactly. The determinant differential and inverse bound integrate to -N log(1-eta/g); the alternative tau/(g-eta) and rational2Neta/g bounds follow. The finite dimension factor is explicit and cannot be carried to the infinite determinant without the separately imported HS input control.

The positive-dyadic logarithm decomposition is correct, including negative powers of2. The atanh-series remainder bounds all omitted positive terms using the first omitted denominator and a geometric sum. Combining the signed integer powers before applying the log2 interval avoids redundant cancellation error. This remains a proof/design: the author helper does not implement a production LU or interval residual engine, and the note does not claim it does.

For approximate anchors, the universally valid upper norm is1+||Zhat||²; the shorthand1+r² is available only when that same norm bound is certified. This is non-load-bearing for the anchor log certificate, which uses the valid lower singular bound1. Approximate product norms and both actual/approximate q_* are otherwise explicitly handled. Native-frame legitimacy, ghost modes, real structure, HS tails and positive unnormalized evolution scalars remain separate obligations.

## Independent exact challenges

I did not rerun the author's unchanged16 controls. A separately frozen literal rational test uses a different nonnormal2x2 matrix, a seven-term candidate and fresh inverse residual, then deliberately forces an odd row permutation in an exact LU. It verifies that ignoring permutation gives the wrong determinant sign, and that falsely declaring the nonzero candidate residual zero is rejected. Exact signed-exponent log intervals, including small dyadics, satisfy inversion consistency and the LU perturbation envelope. All14 predicates pass in0.00226 seconds. These are synthetic algebraic controls, not physical matrix runs or a runtime benchmark. The author's recorded16 controls ran in0.01 seconds with14,876,672-byte maximum RSS; this is author evidence, not my measured memory.

No material blocker. A future numerical implementation still needs actual dyadic/interval residual code, source/runtime freezing, saved candidate matrices and pivots, error allocations and a resource contract. This review does not authorize such a run or infer a sign for an inserted kernel or alpha.
