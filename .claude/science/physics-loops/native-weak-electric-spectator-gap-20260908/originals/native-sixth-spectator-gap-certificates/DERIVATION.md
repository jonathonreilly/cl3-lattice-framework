# Exact rational prefix-gap certificates

This supplies a frame-independent ground-distance lower certificate for a specified intermediate edge-toggle mask. It does not solve any coefficient or scan all prefixes. The actual L4 canonical uniform endpoint and its unique minimizing orbit are retained premises.

Order the vertices by bipartite parity. At |t|=1, write K=2[[0,B],[-B^T,0]] up to the fixed sign convention, where B is a32x32 integer signed adjacency. Its singular values sigma_j give positive active frequencies2sigma_j. Thus the full active ground energy is -sum sigma_j=-Tr sqrt(A), A=BB^T. At the base flux A=6I, so E0=-32sqrt6. This uses the full32-mode Gram matrix and automatically includes the unaffected complement-vacuum energy. It does not need the checker's20-dimensional frame or any numerical orthogonalization.

For every x>=0 and rational c>0 define y1=(c+x/c)/2 and y2=(y1+x/y1)/2. AM-GM gives y1>=sqrt(x); the identity y2-sqrt(x)=(y1-sqrt(x))²/(2y1) gives y2>=sqrt(x), also at x=0. Therefore functional calculus gives the exact trace upper bound

Tr sqrt(A) <= U2(A,c)
 = [Tr A+32c²]/(4c)+c[32-c² Tr(A+c²I)^(-1)].

A+c²I is strictly positive, so rational Gaussian elimination is valid. The implemented inverse trace is exact Fraction arithmetic; its positive pivots are explicitly checked. No rounded eigenvalues or SVD enter. Set c=5/2, and ell=2449489742783178/10^15; ell²<6 is checked exactly. Then

Delta_F >= |t| [32ell-U2(A_F,5/2)].

Whenever the bracket is positive, it lower-bounds every energy in this flux representative above E0, including the reduced512-dimensional parity block. Hence its reciprocal bounds the inverse norm. It is conservative; a negative certificate is inconclusive, not evidence of a negative physical gap. Higher Newton iterates could tighten it but were not needed for these fixtures.

For a singleton-cut prefix the unrestricted active ground remains E0, so this formula must not claim a positive gap. Instead the unreduced initial-parity block excludes the gauge-transformed vacuum and has exact distance sqrt24|t|. The separate rational lower bound2ell|t| is valid there. Classifying that case requires the exact cut and active-parity argument, not a numerically small singular value. The implementation explicitly checks that the unrestricted star certificate is negative, preventing accidental misuse of the wrong-space bound.

## Bounded actual results

The independent canonical edge construction agrees exactly with the checker's exported coordinate/edge order at PREFIXES.json7a154126. Four non-star prefixes of one internal-bridge sequence have certified lower bound

999997540876869429/1446265625000000000 |t| >0.6914342176 |t|.

Its order-three singleton prefix has the separate parity bound2ell|t|>4.8989794855|t|. The first prospectively selected order-three prefix in each of the five external bridge families has rational lower bound approximately1.5029004255,1.5029004255,1.0206489524,1.5029004255,1.3828701355, all times|t|. Decimal values are displays of exact lower rational certificates, not floating estimates. Full numerators/denominators and masks are in RESULT and EXPORT_RESULT.

The first run executes180 exact predicates. The external supplement declares its fixed selection before reading numerical bounds, verifies the complete geometry binding, and applies the same exact certificate to five masks. There is no whole-prefix cost forecast or all-prefix validation yet. An implementation interface needs only the full canonical edge-toggle integer and, for same-orbit returns, its exact cut parity classification. Matrix frames and DP vectors are not shared inputs.

These stronger denominator bounds can enter the previously derived residual recursion state by state. They do not certify the DP solution, its metric, its closing spectator sign or a nonzero coefficient by themselves. No large active-space solve or random profile was performed.
