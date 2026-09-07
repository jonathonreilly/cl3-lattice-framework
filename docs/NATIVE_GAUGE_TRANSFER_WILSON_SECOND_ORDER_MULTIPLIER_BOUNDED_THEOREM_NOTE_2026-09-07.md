---
claim_id: native_gauge_transfer_wilson_second_order_multiplier_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional exact native Wilson global second-order multiplier with C29 for beta at least2048; no spectral inference."
upstream_dependencies:
  - native_gauge_transfer_a2_reflection_uniform_half_line_gap_theorem_note_2026-09-02
runner: scripts/native_gauge_transfer_wilson_second_order_multiplier_2026_09_07.py
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

# Native Wilson second-order multiplier with a global remainder

Bounded theorem,2026-09-07. Independent reviews of the refined proof passed; audit status remains unset. Conditional scientific input: the exact native dominant-weight recurrence/Fourier reflection identity from NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md. The source does not identify this packet multiplier with physical group convolution, derive a Wilson action, or assert a spectral/gap consequence.

Let P=N0² and J be the six-neighbor recurrence divided by6, with negative-label neighbors omitted. For beta>0 define c_p(beta)=<p|exp(beta J)|0>, v_beta=beta^-3/2 c_p/c_0, rho=(1,1), and x_p=(p+rho)/sqrt(beta). On Omega=[1/4,2]², put Q=x²+xy+y², H=xy(x+y)/2, W=H exp(-Q), and

W2=(3-7Q/4+Q²/4)W.

For every real beta>=2048 and every p with x_p inOmega,

|v_beta(p)-W(x_p)-W2(x_p)/beta|<=29/beta².

This is an absolute multiplier estimate at the actual integer endpoints. No boundary differential-operator expansion, eigenvalue-ratio sign or full operator estimate is inferred. In particular the earlier finite skew-translation similarity cancellation is not silently transferred to the Dirichlet chamber.

## Exact native integral and normalization

The parent identity has psi(k)=1-[cos k1+cos k2+cos(k1-k2)]/3 and A_rho(k)=8i sin((2k1-k2)/2)sin((k1-2k2)/2)sin((k1+k2)/2). The numerator is e^-beta c_p=(2pi)^-2 integral_T e^-beta psi e^-ik(p+rho) A_rho dk. The positive denominator is e^-beta c_0=[6(2pi)^2]^-1 integral_T e^-beta psi |A_rho|² dk, T=[-pi,pi]². The orbit factor1/6 must be retained.

## Scaled integrals and coefficients

Put a=z1²−z1z2+z2², Delta=(2z1−z2)(z1−2z2)(z1+z2), and B_beta=product_j sinc(l_j/(2sqrt(beta))), where l=(2z1−z2,z1−2z2,z1+z2). On the scaled torus T_beta=[−pi sqrt(beta),pi sqrt(beta)]²,

N_beta(x)=(2pi)^-2 integral_Tbeta exp(−beta psi(z/sqrt(beta))) exp(−iz.x) iDelta B_beta dz,
D_beta=[6(2pi)^2]^-1 integral_Tbeta exp(−beta psi(z/sqrt(beta))) Delta² B_beta² dz.

Exactly v_beta=N_beta/D_beta. The beta powers are beta^(5/2)e^-beta c_p in N and beta^4 e^-beta c_0 in D. Fourier signs follow the parent exactly.

Let D0=27sqrt(3)/pi>1. Leading transforms give N0=D0 W. The order1/beta numerator factor is a²/36−a/4; denominator factor is a²/36−a/2. Since a Fourier multiplication corresponds to−3L,

N1=D0[(L²/4)+(3L/4)]W=D0(W2−W).

For the denominator, the radial density e^(-a/3)Delta² has a moments12 and180. Hence D1/D0=180/36−12/2=−1. The identities LW=(Q−4)W and L²W=(Q²−10Q+20)W establish the frozen W2. All four polynomial/differential identities used here were independently checked symbolically during intake; the estimates below do not use a fitted coefficient.

## Low frequencies

Use the low region a<=beta/2. Define u=a²/(36beta), b=a/3-beta psi(z/sqrt(beta)), and v=a/(4beta). It still lies inside the scaled torus, and squared sine arguments sum to3a/(2beta)<=3/4, so all factors used in the product comparison are positive. The elementary product estimates give:

|B−(1−a/(4beta))|<=a²/(20beta²),
|B²−(1−a/(2beta))|<=a²/(5beta²).

For the second, the enlarged cutoff gives coefficient1/16+1/10+1/80+1/1600<1/5. The identity sum fourth powers=2a², together with max squared form<=4a/3, bounds sum sixth powers by8a³/3. Taylor remainder divided by2160 therefore supplies the cosine estimate |b−u|<=a³/(810beta²), with0<=b<=u=a²/(36beta). Now u<=a/72, so damping is exp(−alpha a), alpha=23/72.

The exact low remainder factors, after multiplying by beta², are at most exp(−alpha a) times

PN=a²/20+(23/2592)a³+a^4/2592,
PD=a²/5+(29/1620)a³+a^4/2592.

To see this directly, |exp(b)-1-u|<=exp(u)[a^4/2592+a³/810]/beta². Write B=1-v+r, |r|<=a²/(20beta²), multiply and bound the cross term uv. For B² use its remainder a²/(5beta²). The resulting coefficients are: numerator cubic1/810+1/1440+1/144=23/2592; denominator1/810+1/360+1/72=29/1620.

Retain Fourier prefactors. For numerator use |Delta|<=3a^(3/2), polar Jacobian2pi/sqrt3, obtaining coefficient sqrt3/(2pi) times radial integrals. Gamma(n+1/2)=sqrt(pi)*(2n)!/(4^n n!). Since sqrt3/(2sqrt(pi))<1/2 and alpha^-1/2<2, a fully rational sufficient low constant is

CN_low <= sum_(c,n) c [(2n)!/(4^n n!)] alpha^-n <170,
(c,n)=(1/20,4),(23/2592,5),(1/2592,6).

For denominator use the EXACT angular identity

integral Delta² exp(−alpha a) dz=8pi sqrt3 alpha^-4.

Its m-th radial moment is that expression times(4)_m alpha^-m. With denominator prefactor1/(24pi²), sqrt3/(3pi)<1/5, hence

CD_low <=(1/5)[(1/5)*20 alpha^-6+(29/1620)*120 alpha^-7+(1/2592)*840 alpha^-8] <2617.

Both rational inequalities are checked exactly in the companion certificate; their approximate values169.2583 and2616.294 are not inputs.

## Exact high tail

For k in the torus,1-cos k_j>=2k_j²/pi². Discarding the third nonnegative term gives psi>=2(k1²+k2²)/(3pi²)>=4a(k)/(9pi²)>a(k)/24. Thus beta psi>=a/24 globally. On a>=beta/2>=1024, |Delta|<=3a^(3/2)<=3a². The numerator prefactor and polar Jacobian give sqrt3/(2pi)<1/3. The denominator's exact angular radial density gives sqrt3/(18pi)<1/30. Therefore beta² times the exact high tails are bounded by

(beta²/3)24³*2!*exp(−t)(1+t+t²/2),
(beta²/30)24^4*3!*exp(−t)(1+t+t²/2+t³/6),
t=beta/48.

Each summand is a positive constant times beta^j exp(−beta/48), with j<=5, and is decreasing for beta>=2048>240. At beta2048, t=128/3. The exact positive exponential-series lower bound exp(128/3)>10^18 gives respective bounds below0.000037 and0.003869. No pointwise oscillatory cancellation is needed for these tail estimates.

## Gaussian approximation high tails

Here beta<=2a. Retaining the leading+first coefficient and using |Delta|<=3a² gives beta² times the numerator approximation tail at most

(1/3) integral_1024^infinity [(9/2)a^4+a^5/18]exp(−a/3)da.

For the denominator it is at most

(1/30) integral_1024^infinity [5a^5+a^6/18]exp(−a/3)da.

Use exp(−a/3)<=exp(−1024/6)exp(−a/6), the exact series bound exp(512/3)>10^60, and full moments m!6^(m+1). Each resulting rational upper bound is less than1/1000. This includes Gaussian integration outside the scaled torus. Thus, after adding exact and approximation tails,

|N−D0[W+(W2−W)/beta]|<=171/beta²,
|D−D0(1−1/beta)|<=2618/beta².

## Global multiplier bounds and denominator

On the positive chamber,

Q³−27H²=(x−y)²(x+2y)²(2x+y)²/4>=0.

Consequently H<=Q^(3/2)/(3sqrt3). Maximizing q^r exp(−q) for q>=0 at q=r and checking positive exponential sums yields

W<1/12 from exp(3)>18,
QW<1/6 from exp(5)>36(5/2)^5/27,
Q²W<1/2 from exp(7)>4(7/2)^7/27.

Hence |W2|<=3W+(7/4)QW+(1/4)Q²W<2/3. These are global absolute bounds, so certainly apply on the preregistered Omega. D0=27sqrt3/pi>14 (use sqrt3>5/3 and pi<22/7). For beta>=2048,

D/D0 >=1−1/2048−2618/(14*2048²)>999/1000.

Writing N=D0[W+(W2-W)/beta]+rN and D=D0(1-1/beta)+rD, subtracting D[W+W2/beta] leaves rN+D0 W2/beta²-rD[W+W2/beta]. The bounds above give a sufficient coefficient

(1000/999)[171/14+2/3+(2618/14)(1/12+(2/3)/2048)]
 =76675625/2685312 <29.

Thus the proposed refined bound follows. Every numeric constant in this note is fixed by algebra, a monotone tail bound, a positive series inequality or a rational ceiling. Existing quadrature is only a separate falsifier and was not used to set these constants.

## Evidence, scope and preserved history

The standalone exact primary `scripts/native_gauge_transfer_wilson_second_order_multiplier_2026_09_07.py` executes four symbolic identities and22 exact rational assertions. These are actual check counts, not26 independent theorem claims. The symbolic identities are the quartic symbol, quadratic alternant factor, LW andL²W; the rational checks cover low constants, tail series/monotonicity thresholds, multiplier maxima and denominator/ratio bounds. The analytic implications are stated above rather than replaced by numerical checks.

The separate support runner `scripts/native_gauge_transfer_wilson_second_order_multiplier_quadrature_check_2026_09_07.py` directly integrates the full scaled torus at frozen beta128,256,512,1024 and fixed shifted integer endpoints, using GL256/384/512. It reports every real numerator, denominator, v, scaled correction and residual. For each mesh of the original converged GL384/512 pair, it now requires |[beta(v-W)-W2]/W|<1/4 and |[beta(v-W)-(W2-W)]/W|>3/4. These finite comparison regions distinguish coefficients separated by exactly W>0. It also checks |beta(D/D0-1)+1|<1/4 and binds both coordinates to the actual shifted integer endpoint within floating tolerance1e-12. These 28 added comparisons supplement the original finiteness, positivity, window and mesh checks. GL256 remains a reported coarse diagnostic: at beta1024 it fails the new coefficient criterion, so it is not included in coefficient acceptance. Their margins are diagnostic choices made after the original review, not fitted theorem constants, numerical enclosures or theorem inputs. These diagnostic beta values are below the proved threshold2048, and no theorem applicability at those values is asserted.

The separate killed-recurrence support runner `scripts/native_gauge_transfer_wilson_second_order_recurrence_check_2026_09_07.py` checks the same finite coefficient and denominator comparisons on its unchanged18 integer-grid rows at beta128/256/512. Its104 assertions include the original47 walk, entry-tail and resource checks plus57 coordinate/denominator/coefficient comparisons. Its analytic first-exit tail controls truncation only; the floating exponential is not interval-certified. Each numerical runner emits its full numerical payload in both default and --json output, including the new comparison errors. The [dated correction receipt](../.claude/science/physics-loops/native-wilson-second-order-20260907/SOURCE_CORRECTION_2026-09-07.md) distinguishes this evidence from the preserved original receipts.

All three multiplier runners are self-contained; none imports repository inputs or executes another runner. They truthfully emit dependencies{}, with no empty AUDIT_INPUT_PATHS declaration, enforce180seconds/180MiB and set one-thread BLAS. Source hashes bind the executable receipts. Their independence is limited: the primary was authored with this proof; the quadrature is a different computational formulation, while cold proof reviews provide independent derivation scrutiny.

The original preregistration, candidate W2, huge-constant proof C=4738711459316761536/beta0=272104869, its exact certificate, subsequent root refinement proposal, fixed analytic refinement preregistration and all raw receipts remain preserved in the scratch/history packet. No coefficient was changed in response to numerical results. The new constants use stronger Gaussian integration and tail estimates, not a fit. No parked bridge/primitive decision is reopened.

## Separately proved global endpoint extension



Every refined numerator remainder estimate removes the endpoint only through |exp(-iz.x)|=1. Thus CN=171 applies uniformly to every real endpoint x, including every dominant grid label x_p=(p+rho)/sqrt(beta). The denominator estimate CD=2618 has no endpoint. The only endpoint-dependent bounds used in the FINAL ratio calculation are W<1/12, QW<1/6, Q²W<1/2 and |W2|<2/3; all were proved globally on the positive chamber from Q³>=27H². No use of Omega remains in the proof after this refinement.

Consequently the IDENTICAL constant and threshold prove the separately stated extension
 sup_(p,q>=0) |v_beta(p,q)-W(x_p)-W2(x_p)/beta| <=29/beta²,
 for EVERY REAL beta>=2048,
 where v_beta=beta^-3/2 c_(p,q)(beta)/c_(0,0)(beta), x_p=((p+1),(q+1))/sqrtbeta,
 W=H exp(-Q), W2=(3-7Q/4+Q²/4)W.
No additional assumption, endpoint cutoff, quadrature or tail fitting is required. The extension does not make a statement at beta=0 or below2048.


The compact target and subsequent global proof are preserved in the [campaign preregistration](../.claude/science/physics-loops/native-wilson-second-order-20260907/PREREGISTRATION.md). The [exact reflection parent](NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md) supplies the stated native identity.

The [N1–N8 discipline checklist](../.claude/science/physics-loops/native-wilson-second-order-20260907/NO_GO_DISCIPLINE_CHECKLIST.md) preserves the conditional imports and heavy negative-packet NOT PASS.
