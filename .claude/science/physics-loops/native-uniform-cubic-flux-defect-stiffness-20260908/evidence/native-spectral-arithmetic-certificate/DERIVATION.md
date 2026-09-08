# Gap-free a posteriori arithmetic certificate for D16

Prospective arithmetic strategy; no physical spectral scan. The exact Clifford identity supplies PSD D(k) of dimension16 and e_aux(k)=-Tr sqrt(D)/32. This proof does not establish that identity; it uses its separately reviewed source. Computed eigenvectors/eigenvalues are arbitrary candidate numbers, not trusted accurate results from eigvalsh.

## Polar residual bound

Let Q be the square complex candidate vector matrix, Lambda the real diagonal candidate eigenvalues, A the exact Hermitian matrix represented by the supplied rounded matrix entries, and ||D-A||_2<=b_input. Certify eta>=||Q*Q-I||_2<=1/2 and r>=||AQ-Q Lambda||_2. Write Q=W P, P=(Q*Q)^(1/2). Then W is unitary and

A-W Lambda W* = R Q^(-1) + W(P Lambda P^(-1)-Lambda)W*.

Since ||P^(-1)||<=1/sqrt(1-eta) and ||P-I||<=eta/(1+sqrt(1-eta)),

||A-W Lambda W*|| <= r/sqrt(1-eta) + 2 L eta/[(1+sqrt(1-eta))*sqrt(1-eta)] <= 2r+4L eta,

where L=max|Lambda_j|. Thus delta=b_input+2r+4L eta is a deliberately conservative Weyl radius. Sorting Lambda, each exact sorted PSD eigenvalue mu_j lies between max(0,Lambda_j-delta) and max(0,Lambda_j+delta). If any upper endpoint is negative before clipping, reject the certificate rather than hide the contradiction. No spectral gap or nonzero eigenvalue assumption is used.

Tr sqrt(D) is enclosed by sums of square roots of these endpoints, with outward square-root and summation rounding. The density interval reverses endpoints and divides by32. Each individual trace interval width is <=sqrt(2delta); total width<=16sqrt(2delta). For delta=1e-12, density width<=7.1e-7, much smaller than a .01 quadrature-scale target. This is a scale illustration, not a measured physical residual.

## Explicit residual evaluation contract

Do not assert arbitrary installed BLAS is rigorously accurate merely because a residual is small. Two acceptable implementations:

1. Compute Gram and residual with an explicitly controlled scalar binary64 certificate kernel (ordinary IEEE nearest operations, no reassociation/fast-math, no overflow). Eigensolver/BLAS may generate Q,Lambda, but the certificate kernel does not trust their arithmetic. Use real/imaginary component loops. For a length d complex dot product evaluated with four products and real additions per term, a conservative absolute error per real component is gamma_(8d+16) times a component-magnitude sum bound. gamma_m=m*u/(1-m*u), u=2^-53. Bound that sum by 2d*amax*bmax, where maxima are over absolute real and imaginary components. This is intentionally coarse. Include subtraction/product terms for R: dot bound plus u*(|computed dot component|+|Qcomponent*lambda|) and product error u*|Qcomponent*lambda|, each itself evaluated outward. Gram diagonal subtraction similarly includes its absolute rounding term. Alternatively enlarge a single magnitude bound to include these final terms with the same conservative gamma_(8d+16). All input and error-bound arithmetic must itself be outward, using nextafter around each nonnegative operation or exact dyadic rational arithmetic. Reject nonfinite entries. Underflow must be included by an absolute per-operation allowance or avoided by a declared normal-range check; it cannot be silently dropped.

2. For fastest practical batch certification, a fixed-order compiled scalar kernel can compute those same16x16 products; inspect its generated operation contract and compiler flags. A general BLAS residual is conditionally usable only with an explicit verified IEEE dot-product error model for that implementation; binding the library bytes alone is not a proof of this model. A few exact rational replay controls validate implementation but do not replace the operation-level argument.

Once entry intervals are available, bound eta by the maximum row sum of absolute real+imaginary Gram-error entries (Hermitian exact Gram). Bound r by sqrt(rowmax*columnmax) for the residual, or more simply max(rowmax,columnmax), since ||R||2<=sqrt(||R||1||R||infinity). These scalar upper bounds avoid expensive certified matrix decompositions. eta<=1/2 is a hard guard. The large margin to1/2 makes orthogonality certification inexpensive.

An especially transparent standard-library implementation uses Fraction.from_float for exact dyadic dot products on a bounded subset or all matrices. It removes residual-roundoff assumptions entirely but has unmeasured grid runtime and should not be advertised as practical at32^3 grids without a cost-only profile. No such profile is run here.

## Input trigonometry and final roots

D16 uses q_a=2sin(k_a/2); those are not exact binary64 inputs. Supply certified sine intervals and propagate q uncertainty linearly: b_input<=sum_a |Delta q_a| ||A_a tensor sigma_a||. Here each signed cube-edge A_a is an involution, so each norm is1. C^2+3I is integer-exact. Library sin accuracy must not be assumed without a stated bound. Rational argument reduction plus Taylor remainder is a simple independent interval option; precompute the n one-dimensional q intervals once and reuse across all grids/classes. Certified pi input is required if angles are represented through pi. A finite Taylor bound and rational pi enclosure are sufficient; this is a separate small source routine to freeze before execution.

Final square-root endpoints can use math.sqrt only as arbitrary candidates: convert the candidate to an exact dyadic rational, compare its square against the rational endpoint, and move by nextafter until the lower/upper rational-square inequalities hold. This certifies roots without assuming library correct rounding. Sum endpoints as exact rational numbers or directed binary64 sums. No negative eigenvalue clipping without delta, unverified BLAS stability, interval-narrowing from expected positivity, or assumed finite gap is allowed.

## Scope and recommendation

Prefer D16 with a residual certificate over64-dimensional direct h: square-root sensitivity still leaves ample expected scale separation while product count is64 times smaller. It requires actual controlled residual code and sine input enclosures before a physical grid launch. This derivation supplies a valid enclosure strategy, not a completed runtime forecast, density sign, spectral scan or quadrature proof. A failed residual/Gram/input guard must report failure, not request more favorable eigenpairs automatically.

### Concrete coarse scalar-loop envelope

For clarity, a fixed scalar implementation can avoid any uncertainty in the phrase “magnitude sum”: let a and q bound every real/imaginary component of A and Q, and L bound |lambda|. Compute each complex dot by separately accumulating its real and imaginary components in a fixed order. Use N=8d+16 and gamma_N=N*u/(1-N*u). For each real or imaginary residual component, M_R=2d*a*q+q*L bounds the sum of absolute exact terms. For each Gram-minus-identity component use M_G=2d*q*q+1. Then |computed-exact|<=gamma_N*M+2N*sigma, sigma=2^-1074, under IEEE nearest basic operations with gradual underflow and no overflow. N deliberately exceeds the longest dependency path; each underflow error is at most sigma and subsequent roundings amplify the total by less than2 for this dimension. Treat M,gamma and the bound with outward arithmetic. This gives a complete conservative per-component error rule for that specified scalar kernel; it is not asserted for an arbitrary vendor complex BLAS routine. Final row/column absolute sums must include these error radii and their own outward accumulation.
