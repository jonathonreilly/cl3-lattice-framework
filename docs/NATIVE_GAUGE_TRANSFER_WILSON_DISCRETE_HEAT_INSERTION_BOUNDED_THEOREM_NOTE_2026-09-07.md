---
claim_id: native_gauge_transfer_wilson_discrete_heat_insertion_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional same-lattice exact discrete-heat Wilson insertion, qualitative common-space limit, indefinite nonproportional correction and top-Perron comparison with undetermined sign."
upstream_dependencies:
  - native_gauge_transfer_wilson_second_order_multiplier_bounded_theorem_note_2026-09-07
  - native_gauge_transfer_a2_reflection_uniform_half_line_gap_theorem_note_2026-09-02
runner: scripts/native_gauge_transfer_wilson_discrete_heat_insertion_2026_09_07.py
---

**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is conditional-support; independent audit is unset.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
target_claim_type: bounded_theorem
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review the exact native multiplier and insertion proof; no spectral sign is inferred."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

# Separately derived global multiplier and exact discrete-heat operator consequence

This is an analytic extension of the reviewed refined Wilson proof, not a revision of its frozen Omega preregistration. The original compact-window claim/source and receipts remain unchanged. The multiplier estimate imports the exact native recurrence/reflection/Fourier identity. The common-space insertion and Perron comparison additionally use the parent section4 local heat-kernel limit and compact sandwich proof, and section5 simplicity of the leading eigenvalue. These are explicit load-bearing mathematical imports. No physical convolution or additional heat expansion is assumed.

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

# Separately derived structural consequences and top-Perron comparison

Use the notation and proved domains above. Let S=S_(1/2) on the Dirichlet chamber C, T0=S M_W S, f=Q(Q-7)W/4, and D=S M_f S. These consequences do not revise the original Omega preregistration and do not assert a full heat-side expansion.

## Indefiniteness and nonproportionality

The self-adjoint Dirichlet generator L has spectrum in(-infinity,0]. Spectral calculus gives S=exp(L/2) self-adjoint and injective, since exp(lambda/2)>0 at every finite spectral value. Consequently Ran(S) is dense: its orthogonal complement is ker(S*)=0. Boundedness, not invertibility with a bounded inverse, is used below.

W is strictly positive in the chamber. The continuous bounded f is strictly negative on the nonempty open set0<Q<7 and strictly positive on Q>7. Choose nonzero compactly supported test functions g_- and g_+ inside these regions. Their multiplier quadratic forms have strict opposite signs. Approximate each g by S u_n in L² using dense range. Since M_f is bounded, <S u_n,M_f S u_n> converges to <g,M_f g>. Thus <u_n,D u_n> is negative for some n and positive for some n. D is an indefinite self-adjoint trace-class operator. In particular it has at least one positive and one negative eigenvalue, by the compact self-adjoint spectral theorem.

If D=cT0, self-adjointness and T0 nonzero make c real. Then S M_(f-cW) S=0. Its sesquilinear form vanishes on Ran(S)xRan(S); boundedness and density extend this to all L² pairs. Hence f=cW almost everywhere. Since W>0 inside C, this would require Q(Q-7)/4 to be constant, which it is not: at(x,y)=(1,1) it is-3, while at(2,2) it is15. Therefore D cannot be any scalar multiple of T0. Indefiniteness already rules out real scalar proportionality, but the dense-range proof also identifies the exact multiplier obstruction.

Neither result determines <phi0,D phi0>, nor an excited/ground ratio coefficient. Positivity of phi0 or Sphi0 does not remove the sign-changing weight f from its integral.

## Uniform-gap top-eigenvalue comparison

Write Ahat_beta=U_beta A_beta U_beta*, Bhat_beta=U_beta B_beta U_beta*, and Dhat_beta=U_beta P_beta M_(f(x_p))P_beta U_beta*. The already proved statements are
 Bhat_beta ->T0 in operator norm,
 Dhat_beta ->D in trace norm, hence operator norm,
 Ahat_beta-Bhat_beta=beta^-1 Dhat_beta+Rhat_beta,
 ||Rhat_beta||<30/beta².
The first convergence follows from the parent's compact saddle sandwich proof and exp(3/beta)->1. The parent September2 section5 explicitly proves that T0 is nonzero compact positive semidefinite with strictly positive interior kernel, and hence has a simple top eigenvalue mu0>mu1. In particular mu0>0 and its spectral gap g=mu0-mu1 is positive. This is a displayed parent hypothesis/proof, not a numerically fitted eigenvalue assumption.

Operator-norm convergence gives, for sufficiently large beta, a top gap of Bhat_beta at least g/2. Its normalized top eigenvector phi_beta can be chosen to converge to phi0, by convergence of the isolated rank-one spectral projections. Let E_beta=Ahat_beta-Bhat_beta, so ||E_beta||=O(beta^-1). For large beta it is smaller than one quarter of the Bhat_beta gap.

An elementary block argument gives the uniform first-order perturbation estimate. Decompose a normalized top eigenvector of Bhat_beta+E_beta as a phi_beta+z with z perpendicular to phi_beta. Weyl's eigenvalue bound and the spectral gap make the reduced resolvent on the perpendicular space bounded by2/gap(Bhat_beta). Thus ||z||/|a|<=2||E_beta||/gap(Bhat_beta). The phi_beta component of the eigenvalue equation then implies
 |lambda0(Ahat_beta)-lambda0(Bhat_beta)-<phi_beta,E_beta phi_beta>|
 <=2||E_beta||²/gap(Bhat_beta).
All constants are uniform in sufficiently large beta; no derivative or rate for Bhat_beta itself is needed.

Multiplying by beta, using beta Rhat_beta->0, Dhat_beta->D and phi_beta->phi0, yields
 beta[lambda0(A_beta)-lambda0(B_beta)] -> d0:=<phi0,D phi0>.
The isometric embeddings preserve the nonzero top eigenvalues, so this statement is also on the original discrete spaces. Since lambda0(B_beta)->mu0>0,
 beta[lambda0(A_beta)/lambda0(B_beta)-1] ->d0/mu0.
The equivalent top-to-top logarithmic comparison has the same coefficient, if desired, because both top branches are positive. The number d0 and its sign remain undetermined by this argument.

This compares the exact native normalized packet with its exact beta-dependent sampled shifted saddle. It is not an expansion lambda0(A_beta)=mu0+d0/beta+O(beta^-2): the saddle's own convergence correction has not been computed. It also supplies no excited-eigenvalue coefficient without a separately established isolated simple branch, no ground/excited log-ratio sign, and no physical mass-gap statement.

The [global multiplier theorem](NATIVE_GAUGE_TRANSFER_WILSON_SECOND_ORDER_MULTIPLIER_BOUNDED_THEOREM_NOTE_2026-09-07.md) and [Dirichlet reflection parent](NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md) carry the exact scientific assumptions. The certificate checks nine rational statements; no eigenfunction or eigenvalue is computed.

The [N1–N8 discipline checklist](../.claude/science/physics-loops/native-wilson-second-order-20260907/NO_GO_DISCIPLINE_CHECKLIST.md) preserves the conditional imports and heavy negative-packet NOT PASS.
