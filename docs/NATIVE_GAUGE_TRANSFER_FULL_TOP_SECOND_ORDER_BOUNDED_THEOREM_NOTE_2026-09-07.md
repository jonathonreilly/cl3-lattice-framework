---
claim_id: native_gauge_transfer_full_top_second_order_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional full first inverse-beta correction of the normalized native Wilson top eigenvalue, with relative coefficient at least7/16 and remainder o(beta^-1); no excited-branch or physical-gap claim."
upstream_dependencies:
  - native_gauge_transfer_wilson_discrete_heat_insertion_bounded_theorem_note_2026-09-07
  - native_gauge_transfer_killed_heat_second_order_kernel_bounded_theorem_note_2026-09-07
  - native_gauge_transfer_a2_reflection_uniform_half_line_gap_theorem_note_2026-09-02
runner: scripts/native_gauge_transfer_full_top_second_order_2026_09_07.py
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
next_trace_action: "Review the exact heat, quadrature and Perron assembly; no physical or excited-branch sign is inferred."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

# Full normalized native top-eigenvalue correction

On P=N0² use the exact native six-neighbor killed operator J and character coefficients c_p(beta) of the parent. Let

    T_beta=exp((beta/2)J) diag(c_p/c_0) exp((beta/2)J),
    A_beta=exp(-beta) beta^(-3/2) T_beta,
    h=beta^(-1/2), x_p=h(p+(1,1)).

On C=(0,infinity)² let L=(partialxx-partialxy+partialyy)/3 with its self-adjoint Dirichlet realization, S=exp(L/2), Q=x²+xy+y², H=xy(x+y)/2, W=H exp(-Q), and W2=(3-7Q/4+Q²/4)W. Let T0=S M_W S have normalized positive top eigenvector phi and eigenvalue mu>0. Put f=W2-3W and d0=<phi,S M_f Sphi>.

The result is

    lambda_top(A_beta)=mu+c_full/beta+o(beta^-1),
    c_full=d0+3mu+(mu/4)||Lphi||²,
    c_full/mu >=7/16.

It follows that the normalized native top is eventually above mu. No explicit onset, numerical coefficient value or O(beta^-2) eigenvalue remainder is claimed.

## Direct scientific inputs and normalizations

The [September2 reflection theorem](NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md) supplies the exact recurrence/reflection identity, the shifted chamber, the Dirichlet heat convention, the common-space compact-sandwich limit and the simple positive Perron eigenvalue. The [exact discrete-heat insertion theorem](NATIVE_GAUGE_TRANSFER_WILSON_DISCRETE_HEAT_INSERTION_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the native-versus-discrete-saddle top difference d0/beta+o(beta^-1), including the global multiplier coefficient W2 and its normalization. The [second-order killed-heat theorem](NATIVE_GAUGE_TRANSFER_KILLED_HEAT_SECOND_ORDER_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the uniform reflected heat remainder and the two-sided weighted Hilbert–Schmidt bound used below. These are load-bearing conditional mathematical inputs, not a physical Wilson environment or group-convolution identification.

Write P_beta=exp[(beta/2)(J-I)]. Exactly A_beta=P_beta M_v P_beta, v=beta^-3/2 c_p/c_0. The shifted saddle is B_beta=exp(3h²)P_beta M_(W(x_p))P_beta. Its nonzero spectrum equals that of exp(3h²)M_sqrtW exp[beta(J-I)]M_sqrtW, by the XX*/X*X identity. This moves the two weights around the time-one heat without expanding sqrt(v).

## Exact continuum sampled kernel and its Perron vector

Use B=M_sqrtW e^L M_sqrtW, with normalized Perron vector u=sqrtW psi/sqrtmu, psi=Sphi. Let k(x,y)=sqrtW(x)s_1^C(x,y)sqrtW(y). At right-endpoint nodes x_p=h(p+1), define the positive trace-class sampled matrix

    (B_h)_(p,q)=h² k(x_p,x_q),
    (u_h)_p=h u(x_p).

The kernel is positive definite, so B_h is positive; its finite trace follows from the heat diagonal bound and the summability of W. This is the sampled CONTINUUM kernel, not yet the discrete recurrence heat kernel.

The finite-reflection heat formula gives uniform bounds on every fixed-order spatial derivative of psi=Sphi: apply Cauchy–Schwarz to derivatives of each free Gaussian kernel, whose L² norms are uniform in the endpoint. It also gives smooth extension to the chamber walls and zero boundary values for psi and s_1^C(x,·). Thus

    k(x,y)u(y)
      =sqrtW(x)s_1^C(x,y)W(y)psi(y)/sqrtmu

is smooth as a function of y on the CLOSED quadrant despite sqrtW itself having fractional wall regularity. At either wall each of the three factors s_1^C, W and psi vanishes, so the product vanishes at least cubically. Its first normal derivative is zero. Every y derivative needed through order4 is bounded by sqrtW(x) times a fixed polynomial-Gaussian envelope in y, uniformly in x: heat-kernel derivatives and psi derivatives are uniformly bounded, while W and all its derivatives decay Gaussianly. No derivative of sqrtW(x) is needed for this estimate.

Similarly u(y)²=W(y)|psi(y)|²/mu is smooth, has cubic wall vanishing and derivative envelopes. Corners introduce no singularity; the underlying factors are smooth and all boundary conditions remain valid there.

## Euler–Maclaurin with a uniform residual

For a smooth half-line f with f(0)=f'(0)=0, vanishing derivatives at infinity and f^(4) integrable, right-endpoint Euler–Maclaurin gives

    |h sum_(n>=1)f(nh)-integral_0∞f|
      <=C h4 integral_0∞|f^(4)|.

One may take C=1/360 by bounding the B4 remainder and using |f'''(0)|<=integral|f4|. Only the order is needed. Apply this first in one coordinate and then the other. The error in the second application is sampled in the first coordinate, but its polynomial-Gaussian envelope has uniformly bounded Riemann sums for0<h<=1. The boundary zero/first-derivative conditions persist after integration in the other coordinate. Therefore

    |h² sum_q k(x,x_q)u(x_q)-mu u(x)|
       <=C h4 sqrtW(x),
    ||u_h||²=1+O(h4).

Since h²sum_p W(x_p) stays bounded, this gives the genuine quadrature-norm residual

    ||B_h u_h-mu u_h||_ell²=O(h4).

The cell-embedded sampled B_h converges to B in Hilbert-Schmidt norm by pointwise kernel convergence plus a two-sided polynomial-Gaussian domination. This is qualitative convergence, not a second-order embedded operator expansion. Its simple positive top eigenvalue is therefore eventually isolated near mu. The normalized residual identifies that branch and proves

    lambda_top(B_h)=mu+O(h4).

Thus the continuum-kernel sampling contributes NO h² top-eigenvalue term.

## Proof through the positive weighted heat carrier

The exact shifted saddle has the same nonzero spectrum as

    e^(3h²) M_sqrtW exp[beta(J-I)] M_sqrtW.

On the lattice, let B_h sample the continuum kernel sqrtW(x)s_1^C(x,y)sqrtW(y) with the usual h² matrix-entry factor. Let C_h sample sqrtW(x)L_x²s_1^C(x,y)sqrtW(y)/4. The reviewed uniform18h4 reflected heat error and h²sumW<1 yield

    M_sqrtW exp[beta(J-I)]M_sqrtW=B_h+h²C_h+R_h,
    ||R_h||<=||R_h||HS<18h4.

The quadrature lemma above proves lambda_top(B_h)=mu+O(h4). Its proof applies Euler–Maclaurin to the smooth cubic-wall products, not to the nonsmooth bare vector sqrtW psi. It also establishes qualitative HS convergence of B_h to B=M_sqrtW e^L M_sqrtW, while C_h converges qualitatively in HS to C=M_sqrtW L²e^L M_sqrtW/4. The top branch remains uniformly isolated. Consequently the bounded simple-gap perturbation estimate gives

    lambda_top(B_h+h²C_h+R_h)
       =mu+h²<u,Cu>+o(h²),

where u=sqrtW Sphi/sqrtmu. The domain/smoothing calculation below gives <u,Cu>=mu||Lphi||²/4. Expanding only the scalar e^(3h²) adds3mu to the coefficient.

Independently, the already proved exact-native versus exact-discrete-saddle comparison gives their top-eigenvalue difference h²d0+o(h²). Adding the two differences proves the displayed c_full. This argument does not require a square-root expansion of the native multiplier or a convergence rate for the sampled correction C_h.

## Domains and the complete dilation identity

Set psi=Sphi and dnu=W|psi|²dx/mu, a probability measure. Every Q moment below is finite because Q^jW is bounded and psi is L². The equation phi=mu^-1S(Wpsi) and boundedness of L^nS imply phi lies in Dom(L^n) for every finite n. Define kappa=-<phi,Lphi>>0. Positivity follows from the Dirichlet form, which vanishes only on a zero L² function. No domain for the unbounded dilation generator is assumed.

### Norm-differentiable cone dilation

For a>0 define the unitary cone dilation (U_a u)(x)=a u(ax). The Dirichlet form and cone domain scale exactly, giving U_a* L U_a=a²L. Multiplication transforms as U_a* M_W U_a=M_(W(x/a)). Hence

    T(a)=U_a* T0 U_a
        =exp(a²L/2) M_(W(x/a)) exp(a²L/2).

The family is differentiable in OPERATOR NORM near a=1. Indeed the heat times stay away from zero, so L exp(tL) is uniformly bounded; the differentiated multiplier is a bounded polynomial times a Gaussian, uniformly in a on a compact interval. No assertion that phi lies in the domain of the dilation generator is needed.

Use r=log a. At r=0, derivative of a heat factor is L S and derivative of W(x/a) is(2Q-3)W. Since T(a) has the same top eigenvalue mu for every a and <phi,T(a)phi><=mu with equality at a=1, its scalar derivative vanishes. The eigenvector equation, not a formal commutator with an unbounded dilation generator, then gives

    0=2mu<phi,Lphi>+<psi,(2Q-3)Wpsi>.

Therefore

    E_nu Q = 3/2+kappa >3/2.                       (1)

This is a rigorous virial identity for the actual ground equation.

### Full coefficient and its sign

The weighted correction C=M_sqrtW L²exp(L)M_sqrtW/4 is bounded and compact by its derivative-Gaussian kernel with two integrable weights. With u=sqrtW psi/sqrtmu and phi=mu^-1S(Wpsi),

    <u,Cu>=<Wpsi,L²exp(L)Wpsi>/(4mu)
            =mu||Lphi||²/4.

Equivalently define the bounded quadratic-form representative

    T2=S M_W2 S+(L²T0+T0L²)/8.

Here L²T0 is bounded because L²S is bounded, and T0L² has the adjoint bounded extension. Since phi belongs to DomL², <phi,T2phi>=c_full. This is a coefficient identity, not an asserted norm expansion of the step-embedded discrete operators.

From f=Q(Q-7)W/4 and the virial identity,

    d0/mu=[Var_nu(Q)+(kappa+3/2)(kappa-11/2)]/4,
    c_full/mu=[Var_nu(Q)+kappa²-4kappa+15/4+||Lphi||²]/4
      =7/16+[Var_nu(Q)+(||Lphi||²-kappa²)+2(kappa-1)²]/4
      >=7/16.

Cauchy–Schwarz supplies ||Lphi||²>=kappa². No trial vector is identified with phi. The negative native-versus-discrete-saddle correction d0 is compatible with this positive full coefficient because the exact saddle has its own heat/scalar correction; the separate negative-sign theorem is not a premise of this lower bound.

## Why the original embedded operator expansion fails

Let Pi_h be cell-average projection onto the parent piecewise-constant embedding. Every embedded discrete operator has range in RanPi_h. For a nonconstant smooth Gaussian-decaying function v,

    ||(I-Pi_h)v||²/h² -> (1/12) integral(|dxv|²+|dyv|²).

This follows by cell Taylor expansion and the variance h²/12 of each coordinate; dominated summation is valid for such v. The Perron vector phi is smooth with Gaussian decay, since phi=mu^-1S(Wpsi), psi=Sphi is bounded and W has a Gaussian envelope. It is nonconstant and nonzero. Hence any Ahat_h with that cell range obeys

    ||Ahat_h-T0|| >= mu||(I-Pi_h)phi|| = Omega(h).

Consequently Ahat_h=T0+h²T2+o(h²) in operator norm cannot hold under this embedding. This is a failed formulation, not an obstruction to eigenvalue asymptotics. No embedding is silently changed below.

## Executable scope and retained limits

The standalone certificate performs22 actual named exact symbolic/rational checks. It differentiates the actual six-step symbol, harmonic Gaussian heat solution and dilated multiplier; verifies the coefficient decomposition and its adverse variants; and checks Bernoulli, wall-jet and cell-variance identities. It does not compute a Perron vector or prove functional analysis by finite samples. The general domain, derivative-envelope, quadrature, spectral-isolation and assembly arguments are given above. The certificate uses no saved numerical eigenvalue or file dependency and retains180second/180MiB limits.

The theorem has remainder o(beta^-1), not a quantified O(beta^-2) spectral remainder. Qualitative convergence of the sampled correction and Perron projections is sufficient for this result and does not provide an explicit finite-beta onset. No bare heat-operator norm expansion, individual excited-eigenvalue coefficient, ground/excited ratio sign, physical Wilson environment, confinement or mass-gap statement follows. The conditional native recurrence and mathematical input audits remain load-bearing.

The [N1–N8 discipline checklist](../.claude/science/physics-loops/native-heat-spectral-20260907/NO_GO_DISCIPLINE_CHECKLIST.md) records exact scope, physical imports and the preserved failed formulation.
