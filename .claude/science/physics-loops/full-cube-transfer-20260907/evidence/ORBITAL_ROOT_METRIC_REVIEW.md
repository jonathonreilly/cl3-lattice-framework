# Root full geometry/Haar review after independent native-review freeze

Reviewed root full-cube-transfer/DERIVATION.md SHA83f22a03157b1b12bfa88dd031f1360df08e344352f2ab87cf1454454b5a2b43 only after freezing NATIVE_COLD_REVIEW.md SHA44eab4c84f7ef00f78d729aaf26337b9043a69178322b2fc8350d080fb680f2f. Verdict PASS. Hilbert-space identification, gluing, Hessian, octahedral modes and global-singlet count agree with my separately frozen geometry proof; no independent-per-loop conjugation is imported.

The absolute metric factor has the stated direction. For z=M^(1/2)x in five spatial modes and eight colors, dz=J_M dx with J_M=(det M)^4. If g_x is the normalized joint density relative to dx dy, then g_x=J_M² g_z. The one-boundary unitary is f(x)->J_M^-1/2 f(M^-1/2 z), so its kernel transformation divides by J_M. Consequently g_x/j0^5 transforms to J_M g_z/j0^5, NOT its reciprocal and not J_M². This factor cancels only after operator-norm normalization.

For a one-color normalized two-variable Gaussian of plus/minus variances sigma_plus,sigma_minus, the top kernel eigenvalue is 1/[sqrt(pi)(sqrt(sigma_plus)+sqrt(sigma_minus))]. Eight colors give pi^-4 times that sum to power-8. Using the previously derived normalized SU3 Haar density j0=1/(16sqrt3*pi5), the five-mode absolute top eigenvalue is exactly

 (det M)^4 product_j 16sqrt3*pi/(sqrt(sigma_plus,j)+sqrt(sigma_minus,j))^8.

My frozen independent cycle matrix gives det M=1/384 exactly, hence J_M=1/21743271936. The constant is positive and k-independent. The covariance plus eigenvalues stay fixed positive and minus eigenvalues decrease with k, proving the uniform positive lower and finite upper norm bounds used by the normalized uniform theorem.

This check does not promote the earlier one-chord Haar scaling or beta^-4 amplitude into the full model: boundary dimension40 and amplitude beta^-20 are separately verified. Root's absolute constant is sound, while the actual simultaneous transfer proof remains the separately reviewed native estimate. No finite-beta onset, physical time selection or infinite-volume consequence follows.
