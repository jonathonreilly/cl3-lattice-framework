# Cold review: global multiplier and exact discrete-heat extension

PASS, with the stated conditional parent identity and topology distinctions. No actionable logical gap found. I reviewed the native DERIVED_EXTENSION.md against the actual parent Section4/equations14–21 and the independently checked refined scalar proof. No source edits or coauthorship of this extension.

## Global labels and normalization

The refined numerator remainders are endpoint-independent L1 estimates: the only endpoint factor is a modulus-one Fourier phase. Denominator bounds are scalar. The final bounds for W,QW,Q²W,W2 hold on the whole positive chamber, not merely Omega. Therefore the same29/beta² bound genuinely extends to every dominant lattice label for beta>=2048. This is a new derived statement and is correctly distinguished from the frozen compact-window preregistration.

P_beta=exp[(beta/2)(J-I)] is a self-adjoint contraction: the killed six-neighbor J has Schur norm at most1. Exact scalar splitting gives e^-beta beta^-3/2 T_beta=P_beta M_v P_beta. The diagonal norm is the supremum over all labels, so the global scalar estimate supplies the claimed operator norm without a summation or volume factor. Neither heat factor has been replaced by a continuum operator.

The sampled shifted saddle is e^(3/beta)W, by the exact degree/Casimir identities. Subtracting it gives f=W2-3W=Q(Q-7)W/4, including its sign change. For u=3/beta, the exponential remainder u²/[2(1-u)] is valid. With supW<1/12, the beta² correction is at most768/2045, so29+768/2045<30. The bound |f|<5/12 is also valid. No positivity of f, sign of an eigenvalue shift, or spectral-gap coefficient is used.

## Common-space trace-class insertion

The parent isometry is exactly U_beta e_p=h^-1 1_Cp with cell area h² and h=beta^-1/2. F_beta=U_beta P_beta U_beta* is self-adjoint; F_beta²=U_beta exp[beta(J-I)]U_beta*. For a sampled nonnegative insertion g, the exact Hilbert-Schmidt identity is therefore

    ||M_sqrt(g_pc) F_beta||_HS²
       = sum_p g(x_p) K_beta(p,p)
       = h² sum_p g(x_p)[beta K_beta(p,p)].

No factor beta or square-root sampling factor is missing. The return-kernel domination in the parent is multiplier-independent. Both f+ and f- are continuous and integrable with polynomial-Gaussian envelopes; their cell-sampled tails are uniformly summable as h→0. For example Q>=3(x+y)²/4 gives an integrable polynomial times exp(-c|x|²), and h<=1 lets one bound cell samples by a slightly enlarged such envelope. Thus the parent's Riemann-sum norm convergence applies unchanged.

On compactly supported continuous product test kernels the parent endpoint-uniform reflection CLT and local uniform sampling convergence give weak HS convergence. Uniform HS bounds and density extend this to every HS test. Norm convergence then gives strong HS convergence. The ideal-product inequality converts this to trace-norm convergence of B*B. Applying it separately to f+ and f- and subtracting is sound; differentiability of sqrt(f±) at its zeros is unnecessary. The exact cell identity U P diag(f(x_p)) P U*=F_beta M_fpc F_beta follows because multiplication by the cell-constant f_pc preserves the cell subspace.

The same reasoning works for W2±. It establishes trace-norm convergence of the signed INSERTION sandwich, not of every remainder in the full model.

## Final topology and limitations

After multiplying the discrete expansion error by beta, its operator norm is O(1/beta). Adding the insertion convergence gives the claimed operator-norm limit of beta U(A_beta-B_beta)U*. The original remainder has no trace-norm estimate, so one cannot conclude trace-norm convergence of this full normalized difference; the memo correctly declines that conclusion. It also correctly avoids replacing the exact beta-dependent saddle by a fixed continuum leading term plus a second-order coefficient, since its heat/boundary convergence rate has not been expanded.

The consequence remains relative to the exact discrete-heat saddle and conditional native recurrence. No spectral coefficient, physical group-convolution normalization, mass-gap or continuum-domain perturbation claim has been added.

Reviewed extension SHA c935c8e6c75f97b80e48a3a2d9e9b55898b76823f4fcd38ac322caa08679c7e8; actual parent SHA 4164e2aed57ee0dc248575402daa21c51dd40090cdbefbbdca0a2d90562c9089.
