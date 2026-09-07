# Independent event-epoch checker preparation

This is a derivation and checker plan, not an executed experiment. Set gamma=1, t>=0. The waiting times are independent Exp(3), then Exp(2) variables, conditional on a path whose degree sequence is (3,2,2,2). The initial head/path census remains a separate prerequisite.

## Density check

For T_k=sum_{j=1}^k W_j, convolution gives f_1(t)=3 exp(-3t) and

f_k(t)=2 exp(-2t) integral_0^t exp(2s) f_{k-1}(s) ds.

Thus all four root expressions are correct:

f_1=3 exp(-3t),
f_2=6[exp(-2t)-exp(-3t)],
f_3=12[(t-1)exp(-2t)+exp(-3t)],
f_4=12[(t^2-2t+2)exp(-2t)-2exp(-3t)].

Positivity follows directly from convolution. More constructively f_k(t)=3*2^(k-1) exp(-2t)/(k-2)! integral_0^t exp(-s)(t-s)^(k-2) ds for k>=2, which is manifestly nonnegative. Every density integrates to one, since the integrals are products of normalized exponential densities.

The Laplace transform is F_k(s)=3/(3+s)[2/(2+s)]^(k-1), Re(s)>-2 for k>=2 (Re(s)>-3 for k=1). In particular F_k(i omega) is the exact matrix-element averaging factor for exp(-i omega T_k).

Mean and variance, respectively:

k=1: 1/3, 1/9.
k=2: 5/6, 13/36.
k=3: 4/3, 11/18.
k=4: 11/6, 31/36.

They follow by adding exponential means and variances, independently of expanded densities. Alternatively -F'_k(0) and F''_k(0)-F'_k(0)^2 give the same values.

Exact survival tails Q_k(T)=P(T_k>T):

Q_1=exp(-3T),
Q_2=3 exp(-2T)-2 exp(-3T),
Q_3=(6T-3)exp(-2T)+4 exp(-3T),
Q_4=(6T^2-6T+9)exp(-2T)-8 exp(-3T).

Check Q_k(0)=1, -Q'_k=f_k and Q_k(infinity)=0. These supply a rigorous truncation bound: for any matrix element of a one-body density of a normalized Slater mixture, the omitted integral has absolute magnitude <=Q_k(T); for a bounded one-body observable o, use its actual many-body observable norm, or the safe N||o|| bound, times Q_k(T). For example Q_4(20) is approximately 9.73e-15. The exact formula, rather than this rounded value, should set the cutoff criterion.

## Stable time integration independent of rational Laplace contraction

Use the 8-by-8 one-particle Hamiltonian h_R. For a supplied 8-by-4 occupied-orbital matrix X and an independently constructed zero-dwell retained-battery one-body density C_R, the free-dwell endpoint is C_R(t)=exp(-it h_R) C_R exp(it h_R). Integrate f_k(t) C_R(t) on [0,T] directly with adaptive Gauss-Kronrod or composite Gauss-Legendre quadrature. Do not reuse the rational gap multiplier in this checker. Diagonalizing only h_R for exponentials is acceptable and independent of the primary 70-dimensional many-body eigensystem.

The density expressions have severe cancellation near zero. Evaluate f_2=6 exp(-2t)[-expm1(-t)]. For f_3 use expm1(-t)+t; for f_4 use t^2-2t-2expm1(-t). Below a small switch such as 0.1, evaluate the alternating Taylor series for these remainders with a remainder bound, or evaluate their positive convolution integrals. The series start t^2/2-t^3/6 for the f_3 bracket and t^3/3-t^4/12 for the f_4 bracket. Avoid clipping negative floating-point densities as a purported positivity proof.

Report the analytic Q_k(T) truncation bound separately from numerical integration error. A straightforward honest numerical contract is tolerance and mesh convergence at successively tightened quadrature tolerances and doubled subinterval counts, plus agreement between two quadrature families. These are numerical convergence evidence, not rigorous roundoff certification. Integrate scalar 1,t,t^2 first to recover normalization and moments with the same implementation. Check density Hermiticity, trace N and eigenvalues within [0,1]. For current observables, use the supplied sign convention and bond matrices explicitly.

The retained-battery C_R can itself be built as the Fourier mixture integral C_R=integral |beta_hat(tau)|^2 U_tau X X^* U_tau^* d tau, U_tau=exp(-i tau h_R)exp(i tau h_0), with unitary Fourier normalization. This is a mixture of Slater states, generally not a single Gaussian state. Calling the reduced matter state Gaussian would be wrong; one-body observables nevertheless depend only on C_R. Use an explicit Fourier tail bound or independent convergence study for this additional integral. Time quadrature alone does not certify the battery mixture integration.

## Independent direct battery first moment from 8-mode spectral data

A direct energy-domain construction is available without defining battery energy as a balancing scalar. It requires a number-conserving quadratic Hamiltonian, a pure Slater input X (the inherited Slater ground state followed by a one-body phase pulse qualifies), and the common nonbridge CAR gauge. Let V_0,V_R be 8-by-8 orbital eigenvector matrices; for each four-element subset I or J let epsilon_I^0 and epsilon_J^R be sums of four one-particle eigenvalues. Define

A_I=det(V_{0,I}^* X),
D_JI=det(V_{R,J}^* V_{0,I}),
u_JI=epsilon_I^0-epsilon_J^R+k Delta,
g_J(E)=sum_I D_JI A_I beta(E-u_JI).

The exact retained battery energy probability density is p_B(E)=sum_J |g_J(E)|^2. Therefore

<E_B>=integral_0^97 E sum_J |sum_I D_JI A_I beta(E-u_JI)|^2 dE.

Normalization is the same integral without E. This directly contracts the battery state and is independent of the energy-ledger definition. It uses 70 occupation subsets but only 8-mode orbital diagonalization and determinant overlaps, not a dense 70-dimensional Hamiltonian construction. This should be described accurately as an orbital/determinant checker, rather than implying it avoids all many-body combinatorics.

The post-event free dwell contributes exp(-i epsilon_J^R t) to g_J, which cancels from |g_J|^2. Hence the battery energy density and mean are independent of elapsed free-dwell time at a fixed final path/mask. Event-epoch time averaging is needed for currents and density, not this battery marginal. Fuel is represented by the explicit k Delta shift; the initial battery packet is the newly declared [48,49] sine packet.

For robust deterministic energy integration, partition the cap interval at every translated packet endpoint 48+u_JI and 49+u_JI lying in the cap. Within each open cell g_J is a fixed finite trigonometric sum, hence smooth; Gaussian quadrature with refinement supplies transparent convergence. Better, integrate its products analytically on each cell using sine-product antiderivatives, including E weighting. This is a genuinely independent energy-domain route and does not need the primary overlap-kernel formula. Summation should retain complex determinant phases and input-energy coherences. Degenerate orbital eigenbases may differ arbitrarily; the final p_B must be invariant under unitary changes within degenerate eigenspaces.

A mixed input can be handled by an explicitly supplied ensemble and linear averaging, but a general correlated input is not encoded by a single X or its one-body density. Bridge/parity projections also need an enlarged representation; the Slater endpoint simplification is asserted here only for the verified nonbridge four-event domain. No locality, closed-unitary realization, entropy-cost derivation or autonomous reservoir construction follows from these formulas.
