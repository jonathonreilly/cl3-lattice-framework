# Separately derived global multiplier and exact discrete-heat operator consequence

This is an analytic extension of the reviewed refined Wilson proof, not a revision of its frozen Omega preregistration. The original compact-window claim/source and receipts remain unchanged. Its sole load-bearing scientific import is the same exact native recurrence/reflection/Fourier identity. No physical convolution or additional heat expansion is assumed.

## Global endpoint extension

Every refined numerator remainder estimate removes the endpoint only through |exp(-iz.x)|=1. Thus CN=171 applies uniformly to every real endpoint x, including every dominant grid label x_p=(p+rho)/sqrt(beta). The denominator estimate CD=2618 has no endpoint. The only endpoint-dependent bounds used in the FINAL ratio calculation are W<1/12, QW<1/6, Q²W<1/2 and |W2|<2/3; all were proved globally on the positive chamber from Q³>=27H². No use of Omega remains in the proof after this refinement.

Consequently the IDENTICAL constant and threshold prove the separately stated extension
 sup_(p,q>=0) |v_beta(p,q)-W(x_p)-W2(x_p)/beta| <=29/beta²,
 for EVERY REAL beta>=2048,
 where v_beta=beta^-3/2 c_(p,q)(beta)/c_(0,0)(beta), x_p=((p+1),(q+1))/sqrtbeta,
 W=H exp(-Q), W2=(3-7Q/4+Q²/4)W.
No additional assumption, endpoint cutoff, quadrature or tail fitting is required. The extension does not make a statement at beta=0 or below2048.

## Same-lattice exact discrete-heat sandwich

On ell²(P), P=N0², keep the native self-adjoint six-neighbor J and define the EXACT contraction P_beta=exp[(beta/2)(J-I)]. The Schur bound ||J||<=1 implies J-I<=0 and ||P_beta||<=1. Since scalar identity commutes with J,
 A_beta:=e^-beta beta^-3/2 T_beta=P_beta M_(v_beta) P_beta
 exactly. This verifies all exponential and beta normalizations; it is not the differently normalized physical group-convolution operator.

Let w_beta(p)=W(x_p) and w2_beta(p)=W2(x_p). The global diagonal operator norm is the supremum of its entries, so
 ||A_beta-P_beta M_(w_beta+w2_beta/beta) P_beta|| <=29/beta². (1)
Both heat factors retain their full beta-dependent discrete operator. This is a genuine operator-norm second-order remainder on the SAME ell² lattice, with no comparison of bare heat operators in norm and no replacement by a fixed continuum heat semigroup.

## Difference from the exact sampled shifted saddle

The parent identity d_(p,q)=H(p+rho) and Q(p+rho)=3C2(p,q)+3 gives the exact saddle multiplier
 beta^-3/2 d_(p,q) exp[-3C2(p,q)/beta]=e^(3/beta)w_beta(p).
Define B_beta=e^(3/beta) P_beta M_(w_beta)P_beta and
 F(x)=W2(x)-3W(x)=Q(x)(Q(x)-7)W(x)/4.
For u=3/beta<1, exp(u)-1-u<=u²/[2(1-u)]. Using supW<1/12 and beta>=2048 yields
 beta² supW |exp(3/beta)-1-3/beta| <=3/[8(1-3/2048)]=768/2045.
Subtracting B_beta from (1) consequently gives
 ||A_beta-B_beta-beta^-1 P_beta M_(F(x_p))P_beta||
 <=(29+768/2045)/beta² <30/beta². (2)
Also |F|<[(1/2)+7(1/6)]/4=5/12, so (2) implies the explicit weaker comparison
 ||A_beta-B_beta|| <=5/(12beta)+(29+768/2045)/beta².
The inserted function changes sign at Q=7. No sign for an eigenvalue or spectral-gap correction follows from this fact or from the multiplier inequality.

## Qualitative common-space insertion limit, with the actual parent proof

Use exactly the parent September2 section4 embedding: h=beta^-1/2, cells C_p=(hp1,h(p1+1)]x(hp2,h(p2+1)], U_beta e_p=h^-1 1_(C_p), and F_beta=U_beta P_beta U_beta*. To avoid confusing notation, call the scalar insertion f=Q(Q-7)W/4 in this paragraph. Its positive and negative parts f_+,f_- are continuous, nonnegative, integrable, and have polynomial-times-Gaussian envelopes. Their square roots are continuous; no differentiability across Q=7 is needed.

For either g=f_+ or f_-, define g_beta^pc by sampling g(x_p) on C_p and B_beta,g=M_(sqrt(g_beta^pc))F_beta. The parent reflection local CLT applies unchanged to its kernel, since it is a statement about the heat factor, independent of the multiplier. Exactly,
 ||B_beta,g||_HS²=h² sum_p g(x_p)[beta K_beta(p,p)].
The uniform return-kernel bound from the parent, together with a Gaussian-polynomial envelope for g, controls all Riemann-sum tails uniformly as h→0. The local CLT then gives convergence of this norm to integral_C g(x)s_1^C(x,x)dx. On compactly supported continuous rank-one test kernels the same CLT gives weak Hilbert-Schmidt convergence to M_(sqrt g)S_(1/2). Uniform HS boundedness extends weak convergence to all HS tests; norm convergence upgrades it to strong HS convergence, precisely as in the parent's equations18–20.

Taking B*B gives trace-norm convergence of F_beta M_(g_beta^pc) F_beta to S_(1/2)M_g S_(1/2). Subtract the two nonnegative parts to conclude
 ||U_beta P_beta M_(f(x_p))P_beta U_beta* - S_(1/2)M_f S_(1/2)||_1 ->0. (3)
The same argument also applies to W2 via its positive/negative parts. This is a rigorous reuse of the compact weighted-sandwich proof, not a claim of bare heat operator-norm convergence.

Combining (2) with (3) gives the strongest immediate normalized-difference consequence
 beta U_beta(A_beta-B_beta)U_beta* -> S_(1/2)M_f S_(1/2)
 in OPERATOR NORM. The error term in (2) is controlled only in operator norm, so this final convergence is NOT asserted in trace norm. Similarly beta times(A_beta-P_beta M_w P_beta), embedded on the common space, converges in operator norm to S_(1/2)M_W2 S_(1/2).

These are qualitative insertion limits relative to the EXACT beta-dependent discrete-heat saddle. They do not imply A_beta=T_infty+beta^-1 T2+O(beta^-2), because the convergence rate and boundary/heat corrections of the saddle itself have not been expanded. No full spectral coefficient, sign, continuum-domain perturbation theorem, physical Wilson-environment identification, confinement or mass-gap conclusion is asserted.
