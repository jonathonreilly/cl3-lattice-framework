# Signed-SVD direct candidate, unlaunched

This implements the generic d753 Gaussian design and reads the c17 eight-mode blueprint as future scope only. No actual native matrix, SVD or physical Fock vector was evaluated. It is a new candidate algorithm, not a retry of the closed CG attempt. The small dense comparisons are not a native residual certificate.

For H=cI−(1/2)Σ Mij BiAj, oriented SVD gives M=U diag(sigma)V^T with U,V inSO(n); flipping their last columns transfers determinant signs to the last signed sigma. Delta=c−sum(sigma)/2. Never replace signed sigma by absolute values. The input constant is supplied explicitly; for the native model it would be sum(omega)/2. Incorrect offsets change the inverse.

Left Givens elimination Lk...L1 O=I implies O=L1^T...Lk^T. Apply vector planes in reversed elimination order. For each L^T=Rplus(theta), AA uses−theta and BB uses+theta. Combining U's BB and V's AA planes gives W; inverse acts with reverse order and negative angles. The implementation copies RHS, applies W^T, divides by delta+sum sigma*n in the declared full parity sector, and applies W. Source RHS is unchanged even on denominator failure. No active/spectator projection is implemented here; laterJ8 integration must preserve spectator energies and fermionic ordering.

Finite reconstructed small-matrix error and positive finite denominator guards are candidate checks, not certified accuracy. Any nonpositive/below-floor denominator or overflow fails, with no clipping, regularization or retry. Future acceptance requires fresh residual against the actual original operator and its independent arithmetic/gap bound.

Memory retains the source and one working real vector plus the already documented bounded plane scratch; small n-by-n SVD/rotation metadata is also retained. This does not yet meet a full-process memory budget and has no physical cost contract. n<=21 API is prospective only; tests use2..6. Plane code is an exact copy of2d8.

Thirty tiny dense CAR solve comparisons cover both parities, unequal diagonal H0, arbitrary nonsymmetric real M, and determinant-negative cases. All reconstruct the dense Hamiltonian independently from annihilation matrices, compare dense solve and fresh dense residual, and check source immutability. Zero and negative denominators reject. No floating spectral result is promoted to a science claim.
