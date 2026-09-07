---
claim_id: native_gauge_transfer_killed_heat_second_order_kernel_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional native killed-heat second-order shifted-kernel remainder18/beta² for beta>=2048 and t in[1/2,1], with two-sided weighted same-grid Hilbert-Schmidt control; no bare-heat norm expansion."
upstream_dependencies:
  - native_gauge_transfer_a2_reflection_uniform_half_line_gap_theorem_note_2026-09-02
runner: scripts/native_gauge_transfer_killed_heat_second_order_kernel_2026_09_07.py
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
next_trace_action: "Review the exact native Fourier/reflection kernel remainder and same-grid weighted consequence."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

# Native killed-heat second-order kernel with a uniform remainder

The source theorem is conditional on the [September2 exact native reflection parent](NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md), sections1–4: the six-neighbor recurrence, shifted chamber reflection identity(1), Fourier normalization and Dirichlet generator convention. No physical convolution interpretation is imported. The target was preregistered before calculation, and two independent cold reviews plus root review passed; these reviews do not set an audit verdict. This proof refines the parent's ordinary heat CLT(16)–(17), separately from its Wilson numerator alternant.

Let h=beta^-1/2, x_p=h(p+rho), rho=(1,1), and K_(beta t)=exp[beta t(J-I)]. For every beta>=2048, t in[1/2,1], and p,q in N0², the following bound holds:

|h^-2 K_(beta t)(p,q) - s_t^C(x_p,x_q) - (t h²/4)L_x²s_t^C(x_p,x_q)| < 18h^4. (A)

In particular t=1/2 gives the requested coefficient1/8; t=1 gives1/4. The estimate is uniform up to the shifted boundary and in arbitrarily large endpoints. It does not replace cell integration by point evaluation.

## Full-walk Fourier calculation

Write a=z1²-z1z2+z2² and psi(k)=1-[cos k1+cos k2+cos(k1-k2)]/3. Fourier inversion after k=hz yields

h^-2 q_(beta t)(n)=(2pi)^-2 integral_(scaled torus) exp[-t beta psi(hz)] exp[-iz.(hn)] dz.

The Gaussian Fourier symbol is exp(-ta/3). Since L has symbol -a/3, the proposed correction symbol is (t h² a²/36) exp(-ta/3), precisely (t h²/4)L² applied to the Gaussian kernel. All subsequent errors discard the endpoint phase only by its modulus1.

The polynomial identities sum(z1,z2,z1-z2)^4=2a² and max(z1²,z2²,(z1-z2)²)<=4a/3 imply sum sixth powers<=8a³/3. The global Taylor remainder for cosine therefore gives

|beta psi(hz) - a/3 + a²/(36beta)| <= a³/(810beta²).

Also 0<=a/3-beta psi(hz)<=a²/(36beta), by the global quadratic/quartic cosine inequalities. On the low ellipse a<=beta/2 put b=t[a/3-beta psi(hz)] and u=t a²/(36beta). Then 0<=b<=u and |b-u|<=t a³/(810beta²). The elementary exp remainder yields

|exp[-t beta psi(hz)]-exp(-ta/3)(1+u)|
<= beta^-2 exp[-(23t/72)a] [t a³/810+t²a^4/2592]. (B)

Here u<=ta/72, so ta/3-u>=(23t/72)a. The low ellipse lies inside the scaled torus: z_i²<=4a/3<=2beta/3<pi²beta.

For radial a, dz=(2pi/sqrt3)da after angular integration. Thus the Fourier prefactor for a radial integral is1/(2pi sqrt3)<1/10 (pi>3 and sqrt3>5/3). Integrating (B) over the entire plane gives coefficient bounded by

(1/10)[6t/(810alpha^4)+24t²/(2592alpha^5)], alpha=23t/72.

Both terms scale as t^-3, so the maximum on[1/2,1] is at1/2. The value there is (1/10)(899776512/32181715)<14/5. (C)

## Explicit high-frequency tails

For k in[-pi,pi]², retain just the first two nonnegative terms in psi. The inequality1-cos k_i>=2k_i²/pi² and k1²+k2²>=2a(k)/3 give
psi(k)>=4a(k)/(9pi²)>a(k)/24,
where pi<22/7 implies pi²<32/3. Hence on a>beta/2, for all t>=1/2 the exact scaled-torus integral is bounded by the full-plane radial tail

(1/10) integral_(beta/2)^infinity exp(-a/48) da
=(48/10)exp(-beta/96).

Multiplying by beta², this decreases for beta>=2048. At2048, exp(64/3)>10^9 by the finite positive Taylor sum through degree80, so the coefficient is below21/1000. This comparison uses exact rational arithmetic, not a floating exponential.

For the Gaussian approximation on the complement of the low ellipse, use t>=1/2 in the exponent and t<=1 in the polynomial. Its radial tail is at most

(1/10) integral_(beta/2)^infinity exp(-a/6)[1+a²/(36beta)] da
=(6/10)[7/6+beta/144+2/beta]exp(-beta/12).

After multiplication by beta², every polynomial-times-exponential term decreases for beta>=2048. At2048, beta/12>32 and exp32>10^12 by the positive Taylor sum through degree80. The resulting coefficient is below1/1000. This tail also includes the part outside the scaled torus, so no Fourier-domain omission remains.

Combining(C) and the two tails yields a full-walk scaled-kernel error <[14/5+21/1000+1/1000]beta^-2<3beta^-2. The ten rational assertions in the linked exact rational runner check these arithmetic comparisons only; the source argument supplies the Fourier bounds.

## Exact boundary images

The native identity is K_(beta t)(p,q)=sum_w det(w)q_(beta t)((q+rho)-w(p+rho)). The same six images define the killed Gaussian kernel. The Weyl matrices preserve the diffusion quadratic form, so L_x² applied to each reflected Gaussian equals its radial Fourier correction above. Applying the full-walk estimate to each of the six exact images yields(A) with constant18. This does not need a separate boundary asymptotic or lose the rho shift. At a continuum wall the Gaussian terms cancel exactly; the bound itself remains an absolute bound and does not assert a relative estimate near a wall.

## Discrete two-sided weighted sandwich consequence

This is a direct norm estimate on the original lattice, not a common-space cell-expansion claim. For any sampled weights a_p,b_p with h²sum|a_p|² and h²sum|b_p|² finite, define lattice matrices
G_h(p,q)=h² s_t^C(x_p,x_q),
C_h(p,q)=h²(t/4)L_x²s_t^C(x_p,x_q).
Then(A) implies

||M_a[K_(beta t)-G_h-h²C_h]M_b||HS
<=18h^4 (h²sum|a_p|²)^(1/2)(h²sum|b_p|²)^(1/2). (D)

The nonstrict form includes the case where either weight is identically zero. Thus (D) also bounds the operator norm. It requires two-sided summable weights; an unweighted or one-sided estimate does not follow from(A).

For the actual W=xy(x+y)e^-Q/2, use Q>=x²+y² and (x+y)^3<=4(x³+y³) to obtain
W(x,y)<=0.5(x³+y³)exp(-x²-y²).
For h<=1/4, the right Riemann sum of exp(-x²) is below its integral sqrt(pi)/2<1. For f=x³exp(-x²), the integral is1/2 and its total variation is2max f<2; consequently h sum_(n>=1) f(nh)<=1/2+2h<=1. (The maximum is below1 since its square is(27/8)e^-3<1.) Therefore h²sum_p W(x_p)<1. Since beta>=2048 ensures h<1/4, (D) with a=b=sqrtW gives

||sqrtW[K_beta-G_h-h²C_h]sqrtW||HS<18h^4, t=1. (E)

This is the needed same-grid weighted heat correction for the spectrum-equivalent carrier sqrtW exp[beta(J-I)]sqrtW. The external scalar exp(3h²) in the shifted saddle can be handled separately. No square-root expansion of the native Wilson multiplier was used.

## Preserved obstruction and unfinished obligation

The stepfunction embedding U_h generally has an O(h) cell-projection error. Neither(A) nor(E) implies U_h A_h U_h*=A0+h²A2+o(h²) in continuum operator norm. A separate Nyström/eigenvalue quadrature argument, including boundary orders and tails, is still required before a full heat-side eigenvalue coefficient can be claimed. That spectral/quadrature argument is outside this theorem. This derivation supplies no physical spectrum, mass gap, excited ratio, or finite-beta sign onset.


## Executable coverage

The [exact rational runner](../scripts/native_gauge_transfer_killed_heat_second_order_kernel_2026_09_07.py) performs the original ten exact comparisons: the pi ceiling, low-integral ceiling, two positive exponential Taylor lower bounds, two high-tail ceilings, total full-walk ceiling, six-image multiplier, low-cut containment and monotonicity threshold. It does not numerically sample heat kernels or prove the continuum Fourier, reflection, Riemann-sum or Hilbert-Schmidt arguments by execution. Its source SHA and180-second/180-MiB/one-BLAS-thread contract are reported; there are no runtime scientific input files. The body above carries those mathematical arguments. The source makes no individual spectral or physical gap claim.

## Independent native recurrence diagnostic

The [two-endpoint helper](../scripts/native_gauge_transfer_killed_heat_second_order_native_recurrence_check_2026_09_07.py) directly evolves the same six-shift killed generator in frozen finite boxes, using nonorigin shifted sources and both wall and interior endpoints. It preserves all36signed leading/corrected residuals at beta128/512/2048 and t=1/2,1. Its119actual assertions include the beta2048 theorem-domain diagnostic. The box-exit Chernoff inequality is analytic, but its floating asinh/cosh/exp evaluation is not an interval-certified enclosure; the floating matrix exponential is also uncertified. These computations are independent falsifiers, not premises of the explicit Fourier theorem. Both initial memory failures and the identical-generator allocation repair remain preserved; limits stay180seconds/180MiB.

The [N1–N8 discipline checklist](../.claude/science/physics-loops/native-heat-spectral-20260907/NO_GO_DISCIPLINE_CHECKLIST.md) records exact scope, physical imports and the preserved failed formulation.
