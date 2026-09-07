# Perron correction sign exploration, frozen before numerical values

Target r=d0/mu0=integral Q(Q-7)u²/4 for normalized Perron eigenfunction of B=M_sqrtW S_1 M_sqrtW on C=(0,infinity)². Exact heat kernel is the six-image Dirichlet reflection kernel for L=(partialxx-partialxy+partialyy)/3. No sign conclusion will be inferred from a trial function, a floating matrix or agreement between grids alone.

First numerical discriminator: tensor Gauss-Legendre Nyström on square[0,5]² with n=12,20,28 nodes per coordinate, all fixed before values. Use the full six reflected images and exact covariance normalization sqrt3/(2pi)exp(-Q). Diagonalize symmetric weighted kernel, take normalized largest eigenvector and report top eigenvalue, gap estimate, correction moment, mass beyond Q7, and eigenvalue positivity. These are diagnostic only. One BLAS thread,180seconds/180MiB.

After these frozen runs, investigate a certified route: operator-norm enclosure for heat-kernel quadrature/domain tails, isolated-Perron projection perturbation, and weighted correction expectation bounds. Any enlarged grid/domain is separately motivated and preregistered. Preserve failures; absent a rigorous analytic bound or computable enclosure with actual certified margins, report sign unresolved despite numerical evidence. No repository changes or physical spectrum claims.
