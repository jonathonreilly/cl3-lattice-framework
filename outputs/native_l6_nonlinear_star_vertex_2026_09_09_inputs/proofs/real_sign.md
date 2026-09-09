# Real-only one-star representation: PASS as an exact algebraic reduction

This is a separate prospective kernel design. No frozen physical candidate is modified and no physical-size action or solve is performed. Use the exact adapted frame: normalized r_j are white, q_j=Kr_j/sqrt(lambda_j) black. Define annihilators f_j=[gamma(r_j)-i gamma(q_j)]/2. Therefore

A_j=gamma(r_j)=f_j+f_j†,
B_j=gamma(q_j)=i(f_j-f_j†)=i B_j(real).

On an occupation column n, A_j scatters with sign(-1)^(lower occupied bits), while B_j(real) scatters with that sign times(2n_j-1). Thus A_j²=I, B_j(real)²=-I and B_j(real) is real antisymmetric. The physical B_j is Hermitian. This is exactly the negative-Y convention; switching to positive Y without changing H0 would reverse the diagonal energy.

In this basis K has paired block[[0,-omega],[omega,0]], so H0,j=-i omega A_j B_j/2=omega(n_j-1/2). The denominator H0-E0 is sum_j sqrt(lambda_j)n_j, with all21 frequencies and the correct bath offset. No L4 flat-frequency formula is used.

The center endpoint has only black support: gamma0=i B0(real), a real linear combination of four B_j(real), the A1g mode in each spectral sector. Each neighbor gamma_v is a real linear combination of A_j. All six star edges have sorted endpoint0 first. The changed-edge term is therefore

-i K_0v gamma0 gamma_v = +K_0v B0(real) A_v.

The rightmost neighbor action is performed first. Anticommutation implies B0(real) A_v is symmetric, since its transpose is -A_v B0(real)=B0(real) A_v. Hence every pair denominator is real symmetric in both parity spaces. The sign is plusK, not minusK. Exact three-mode CAR controls compare the literal complex expression with this real product and reject the opposite sign.

With a real vacuum source, first positive-denominator inverses x_A are real. Applying gamma0 to their real sum gives i times a real odd source. Real odd solves yield y_C=i y_C(real); the vertex is chi=i chi(real). Particle weights and residual norms can be computed from the real arrays, with the global i restored explicitly for comparison to the complex convention. Vacuum-fixed magnetic transports in the adapted frame are real, so they preserve this representation. The opposite sign of a physical t changes K and the compatible frame together; this claim uses the frozen canonical t=+1 frame and scales |t| as previously declared, rather than silently reusing it for negative t.

Exact endpoint coefficients from ADAPTED.json have center support modes0,6,12,18. The ±x and ±y neighbors each have15 nonzero mode coefficients; ±z each have11 in this particular Eg basis. These unequal counts are a basis fact, not broken physical cubic symmetry. Exact zeros may be skipped without floating threshold selection. Two independent neighbor-then-center chains therefore use2*(15+4)=38 coefficient/scatter terms in the worst pair, rather than84 for four dense21-mode actions. The shared-center factor also permits B0(real)[K_0v A_v+K_0w A_w] exactly, but coefficient combination and its error envelope would be a distinct implementation amendment; no extra cost reduction is assumed here.

A real candidate uses half the array bytes of a complex candidate. Its roundoff proof can replace complex products by real products and remove exact imaginary swaps, but it still needs outward coefficient bounds, finite-intermediate/FP-environment assumptions, subnormal terms, exact dyadic norm scans and residual propagation. The existing9e489 envelope remains a conservative route if applied consistently; this algebra does not itself certify a floating implementation. For a real m-term signed-permutation sum, the standard gamma_m*sum|c_j| relative envelope plus explicit underflow injections is available, with m=4,11 or15 from the exact coefficient support. No new arithmetic constant is claimed without its implementation-specific proof.

The support count and toy controls are bounded exact calculations only. No spectral, physical resolvent, fullvector action, Gaussian evaluation or cost profile was run.
