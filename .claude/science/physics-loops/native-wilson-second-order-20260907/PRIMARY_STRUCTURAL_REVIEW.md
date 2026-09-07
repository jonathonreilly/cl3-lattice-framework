# Cold review of structural appendix and assembled source

PASS. This separate review covers STRUCTURAL_APPENDIX.md and the appended part of DRAFT_SOURCE.md, beyond the earlier operator-extension review. No source edits. No new numerical spectral value is used.

## Dense range, indefinite insertion and domains

For the self-adjoint nonpositive Dirichlet generator L, bounded spectral calculus defines S=exp(L/2) on all L². If Su=0, the integral of strictly positive exp(lambda) against u's spectral measure is zero, so u=0. There is no spectral point at minus infinity. Thus kerS=0 and RanS is dense, even though its inverse is unbounded and its range need not be closed. The proof never applies L or S inverse to arbitrary vectors; no unjustified domain step appears.

The continuous bounded insertion f has strict opposite signs on nonempty interior regions. Compactly supported L² test functions give strict positive/negative multiplier forms. Approximating them by Su_n transfers those signs by boundedness of M_f. The norms of u_n need not be bounded; existence of one nonzero vector of each sign suffices. D is already self-adjoint trace class from the previous sandwich proof, so the compact spectral theorem implies at least one positive and one negative eigenvalue.

For D=cT0, self-adjointness and T0 nonzero force c real. The sesquilinear identity on RanS extends to all pairs by density and boundedness of M_(f-cW), forcing its multiplier to vanish almost everywhere. Since f/W=Q(Q-7)/4 is continuous and nonconstant in the chamber (values-3 and15 at the listed points), this is impossible. No bounded inverse of S is invoked. The appendix correctly does not infer a sign for d0 from indefiniteness or from positivity of the Perron vector.

## Uniform gap and first difference

I read the actual parent September2 Section5 passage establishing that T0 is nonzero compact positive semidefinite with strictly positive interior kernel and a simple top eigenvalue. It supplies a positive top spectral separation g; no numerical gap value or excited-branch simplicity is imported.

Norm convergence Bhat_beta→T0 isolates a rank-one top spectral projection for large beta, with gap at least g/2 and an eigenvector converging after phase choice. Let epsilon=||E_beta|| and b be the Bhat top gap. Weyl gives lambda_top(Bhat+E)>=lambda_top(Bhat)-epsilon, while the perpendicular compression Q(Bhat+E)Q has top at most lambda_top(Bhat)-b+epsilon. Thus the reduced resolvent has norm at most1/(b-2epsilon)<=2/b when epsilon<b/4. This explicitly verifies the appendix's reduced-resolvent constant for the PERTURBED perpendicular block, not merely QBhatQ.

The eigenvector's top component a is nonzero, and its perpendicular equation gives ||z||/|a|<=2epsilon/b. The top scalar equation then bounds the first-order remainder by2epsilon²/b exactly as stated. This estimate uses only bounded compact self-adjoint operators and an eventual spectral gap, with no unbounded-generator domain or differentiability assumption.

Because E_beta=beta^-1 Dhat_beta+O(beta^-2), Dhat_beta→D in norm and the top vectors converge, multiplying by beta yields the stated top DIFFERENCE coefficient d0=<phi0,Dphi0>. The quadratic remainder tends to zero after that multiplication. Isometric embeddings add zero eigenvalues but preserve the positive nonzero top branches. Since the saddle top tends to mu0>0, the ratio and logarithmic comparisons have coefficient d0/mu0. No rate for Bhat_beta→T0 is necessary for these difference statements.

## Scope check of assembled draft

The draft retains the distinction between trace-norm insertion convergence and operator-norm convergence of the complete normalized difference. It does not claim an expansion relative to a fixed continuum heat saddle, an individual excited-eigenvalue coefficient, a ground/excited ratio sign, or a physical mass-gap result. A first-difference top coefficient relative to the exact beta-dependent saddle is narrower than a full absolute spectral expansion and is justified here. d0 and its sign remain undetermined.

No actionable gap found. This verdict covers the specific appendix and assembled source hashes below, not later spectral or heat-side extensions.

STRUCTURAL_APPENDIX.md SHA d8fca7c058b1fafc4d7b3d1ead1f5a9cec6da6c6dbc6443e88f9efd99d8902b0.

DRAFT_SOURCE.md SHA 41d81f79b5a7de82fa87038d61f9f8db2e16d805269136c8d9fe9de47f34067b.
