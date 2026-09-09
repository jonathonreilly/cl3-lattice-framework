# Uniform reference Riccati disk for the actual native pair defects

Status: conditional-support, source review pending. This is a new mathematical construction on the supplied infinite native Gaussian model, not an executed time evolution or a node-alpha computation. The finite-energy offset and Gaussian domain are the independently reviewed prerequisites of PR8067; the weighted accretivity bounds come from PR8068. No new axiom or observed value enters.

## Reference-frame Hamiltonian and signs

Use the real bipartite reference polar frame, with D=U0^T B_A. In the convention f=(a+ib)/2, the one-particle quadratic term i a^T D b/2 equals, apart from its finite relative scalar,

 f^dagger H f + (f^dagger K f^dagger + f K^T f)/2,
 H=(D+D^T)/2, K=-(D-D^T)/2.

Here the bilinear notation includes the two indices. H is real symmetric and K real skew. The pair-creation sign is fixed by expanding i(a)(b)/2; reversing the Majorana convention changes K and the pairing coordinates together. For one two-mode block H=mu I,K=kappa J,Z=zJ, the even Hamiltonian has offdiagonal kappa, giving z'=-kappa-2mu z+kappa z^2.

For the reference-normalized Gaussian exponential exp(f^dagger Z f^dagger/2), imaginary-time Schrodinger evolution therefore gives the operator Riccati equation

 Z'=-K-HZ-ZH+Z K^T Z = -K-HZ-ZH-ZKZ, Z(0)=0.       (1)

The scalar normalization is separate. The actual relative vacuum scalar is supplied by the parent energy theorem, not obtained by subtracting extensive vacuum energies here.

## Actual weighted accretivity and skew control

The pair-chart proof writes D=S-2u b^T with S=|B0| positive, injective, bounded and gapless. Put a=S^-1/2 u,d=S^-1/2 b. Its actual native estimates are

 a^T d=1/3, 2||a||||d||<=33/25,
 H>=S/150>=0.                                          (2)

All inverse powers here act only on the already justified local vectors. The bounded normalized skew form for K has norm

 ||a d^T-d a^T||<=||a||||d||<=33/50.

The first inequality follows by restricting this real skew rank-two map to span(a,d): its nonzero singular values are sqrt(||a||^2||d||^2-(a^T d)^2), at most ||a||||d||. Thus for all real vectors v,w,

 |v^T K w|<=99 sqrt(v^T H v) sqrt(w^T H w).             (3)

This is a form inequality, not an assertion that H has a bounded inverse or a positive spectral gap. It extends by continuity from the local normalized factorization. The same estimates hold throughout the defect path by the uniform parent bounds.

## Invariant disk without a spectral gap

Fix r=99/100. The exact rational inequality

 99(1-r^2)<=2r                                         (4)

holds strictly. For an arbitrary real skew Z define M=r^2 I+Z^2=r^2 I-Z^T Z and A=H+ZK. Direct differentiation of(1) gives

 M'=F-A M-M A^T,
 F=2r^2 H-2ZHZ-(1-r^2)(KZ+ZK).                        (5)

For any real v write a0=v^T H v,b0=(Zv)^T H(Zv). Both are nonnegative. Equation(3) gives

 v^T F v >=2r^2 a0+2b0-2*99(1-r^2)sqrt(a0 b0)
            >=(4r-2*99(1-r^2))sqrt(a0 b0)>=0.          (6)

Crucially this proves F>=0 for every real skew Z; it does not assume the desired disk bound. With T'=-A T, the variation-of-constants expression for(5) is a sum of positive congruences. Since M(0)=r^2 I, M(t)>=0 throughout the local solution. Hence ||Z(t)||<=99/100. H and K are bounded operators, so the norm bound prevents finite-time blowup of the locally Lipschitz Riccati ODE and extends the solution to every finite t>=0.

This argument works in the infinite Hilbert space with bounded H,K; it does not use a finite-dimensional minimum eigenvalue or a compactness argument on the unit sphere. Congruence evolution is boundedly invertible on finite intervals. In particular M(t) is strictly positive there; the displayed uniform closed-disk bound suffices for subsequent estimates.

K is finite rank (the reference contribution S is symmetric). Starting at Z0=0, the same equation is locally Lipschitz in the trace ideal S1 and its linear growth estimate on the bounded operator-norm disk gives finite S1 norm at every finite time. Thus the Gaussian exponential is implementable. Finite-rank approximants, the same uniform disk estimate and the established positive reference chart identify this solution with the normalized actual quadratic evolution. A fully quantitative approximation theorem must separately account for the approximation of H,K and the S1/HS tail; no convergence rate is claimed solely from implementability.

## What this changes, and what it does not

The actual reference pairing chart stays in a uniform ball strictly inside radius one at all nonnegative imaginary times. This is much sharper than the previous exponential reference-anchor-only bound. It may permit a direct low-rank Riccati construction in the reference frame, avoiding the need to evaluate an exponential on a slightly contaminated negative-energy band. It does not imply positive cross-impurity kernels, determine their phases by a square root, or compute alpha.

Equation(1) uses the actual bounded reference H and finite-rank K; a finite matrix compression still needs certified moment/Gram residuals, common CAR conventions, scalar normalization and approximation-error propagation. A naive Euclidean Lipschitz estimate can grow exponentially with time. This proof does not establish practical numerical stability, cost or target precision by itself. The separate positive-band contraction method remains available.

The uniform bound also implies ||(I+Z^T Z)^-1||<=1 and det/pairing factors have singular values bounded in [1,1+r^2]; total determinants still depend on a certified trace bound. No dimension-free lower vacuum overlap follows from operator norm alone.
