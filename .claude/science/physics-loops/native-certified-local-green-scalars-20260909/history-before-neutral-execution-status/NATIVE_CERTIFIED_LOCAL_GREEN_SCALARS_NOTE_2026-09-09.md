---
claim_id: native_certified_local_green_scalars_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied infinite native Gaussian dispersion: accepted certified local A/Aprime and B/Bprime scalar intervals at fixed poles, with explicit mathematical elliptic-identity import."
upstream_dependencies:
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
  - native_infinite_star_node_reduction_note_2026-09-09
runner: scripts/native_certified_local_green_scalars_2026_09_09.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
bare_retained_allowed: false
---

# Certified fixed local Green scalar inputs

**Status:** conditional-support; independent draft source review found no scientific scope defect and identified the now-recorded closure/schema repairs. See packet REVIEWS and REVIEWER_REPAIR.md. Canonical saved-certificate execution remains pending; formal audit is deferred. Existing physical scalar attempts were separately accepted; this package does not rerun them.

Use the [canonical dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md) and [infinite node conventions](NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md). In h1 units X=4sum sin²k, A(s)=E1/(X+s²), B(s)=E sqrtX/(X+s²). Dimensions restore as A_h=h^-2 A_1(s/h), A_h'=h^-3 A_1', B_h=h^-1 B_1(s/h), B_h'=h^-2 B_1'. The reference/model remains supplied.

Accepted fixed computations give A/Aprime at s0,1e-9,1/2,1,2 with widths<=1e-12; the s0 derivative is right-sided. Independent positive return series overlaps at1/2,1,2 check the elliptic convention. Accepted B/Bprime at1,2 have widths below1e-6 (actual widths about1.4–1.8e-8), including all analytic tails and quadrature arithmetic. Exact rational endpoints in the paired input files are authoritative. No rounded decimal is used as an input.

The elliptic identity is an explicit imported mathematical bridge, source-checked in Guttmann arXiv1004.1435 section1.2, which attributes it to Joyce1998. It is not rederived here and supplies no physical selection. The positive return method independently checks overlapping poles. Full methods and error allocations are recorded below; their original source snapshots, failures/review records and accepted receipts remain separate from the canonical runner.

The canonical runner only authenticates saved source-bound acceptance/interval certificates, exact widths, derivative signs and cross-method intersections. It neither calls an oracle nor reconstructs a physical integral. Such bookkeeping does not alone prove interval containment: that conclusion also depends on the included methods, reviewed arithmetic implementations and authenticated accepted execution records. No Gram compression, stationary projector, node alpha or phase conclusion is claimed.


## Preserved method derivation: native-green-return-series-stretch

# Positive exact return series for the local A function

In h1 units, X=4 sum sin²k=6-2 sum cos(2k). Put Y=2 sum cos(2k), q=s²+6>6. Uniform momenta give A(s)=E[1/(q-Y)]. Since |Y|<=6<q, the geometric expansion converges absolutely and uniformly. Odd moments vanish by translating all three folded angles by pi. The even moment counts length2n nearest-neighbor walks on Z³ returning to0:

 c_(2n)=(2n)! sum_(j+k+l=n)1/(j!²k!²l!²).

Group k of n paired steps in two coordinates. Vandermonde sum_j binom(k,j)²=binom(2k,k) reduces this to

 c_(2n)=binom(2n,n) sum_(k=0..n)binom(n,k)² binom(2k,k).

Every coefficient is a nonnegative integer and at most6^(2n), since returning walks are a subset of all six-choice walks. Thus

 A(s)=sum_(n>=0)c_(2n)/q^(2n+1),
 A'(s)=-2s sum_(n>=0)(2n+1)c_(2n)/q^(2n+2).

Termwise differentiation is justified uniformly on any compact s interval bounded away from0 by the weighted geometric majorant. With r=36/q² and the first m terms retained, explicit tails are

 0<=A-A_m<=r^m/[q(1-r)],
 0<=(-A')-D_m<=(2s/q²)r^m[(2m+1)/(1-r)+2r/(1-r)²].

All quantities are exact rational for rational s. These are bounds on the actual infinite native integral, not asymptotic estimates. There is no cancellation in either positive partial sum. The derivative enclosure is[-D_m-tail,-D_m]. No numerical integration or transcendental arithmetic is necessary.

The prospective six cases are s1,2,1/2, each at target widths1e-6 and1e-12. The smallest m with both tail bounds<=target is fixed from the formulas before evaluating any coefficients. Coefficients can be shared across cases, but the initial implementation computes them per case for simple complete timing; no outcome-selected truncation occurs. Work per case is O(m²) binomial operations with growing integers; root must measure real cost before any stronger forecast. The s approaching0 regime has m growing roughly s^-2 log(1/target), so this is not a uniform small-s solution for every projector quadrature node.

Dimensions restore as A_h(s)=h^-2 A_1(s/h), A_h'(s)=h^-3 A_1'(s/h). This proposal supersedes no prior data and leaves the frozen Gauss route unlaunched.


## Preserved method derivation: native-small-s-green-acceleration-stretch

# Uniform small-s acceleration through a checked mathematical bridge

## Imported identity and normalization

Read Guttmann, arXiv1004.1435, section1.2 page5, simple-cubic formula and its defining integral; reference33 identifies Joyce1998 J.Phys.A31,5105–5115. Source: https://arxiv.org/pdf/1004.1435 . This is an explicitly imported lattice-Green-function identity, not a new native physics derivation. With P(z)=E[1-z(sum cos k)/3]^-1, the paper gives

 P(z)=((1-9xi^4)/((1-xi)^3(1+3xi))) [2K(k)/pi]^2,
 k²=16xi³/((1-xi)^3(1+3xi)),
 xi=sqrt(1-sqrt(1-z²/9))/sqrt(1+sqrt(1-z²)).

Use positive roots for0<=z<=1. K is the complete elliptic integral with modulus k; below m=k² is the series parameter. The source formula is the load-bearing mathematical bridge. No numerical value from the paper is imported.

## Native substitution and stable algebra (derived here)

The actual scalar oracle has q=s²+6 and z=6/q, so A(s)=P(z)/q. This follows directly by folding the actual dispersion X=6-2sum cos(2k). For s>=0 rewrite the radical parameter as

 xi²=4/[(q+sqrt(q²-4))(q+s sqrt(s²+12))].        (1)

This rationalization removes cancellation in1-sqrt(1-z²/9) and in1-z² near the node. The second radical is s sqrt(s²+12), not an independently subtracted near-equal number. At s0 equation(1) is finite; the positive one-sided branch is explicit.

For every s>=0, xi²<=1-sqrt(8/9)<1/16. The latter strict inequality is the exact rational comparison8/9>(15/16)². Therefore0<=xi<1/4, d=(1-xi)^3(1+3xi)>=27/64, and

 0<=m=16xi³/d<16/27<1.

The normalized elliptic factor has a positive binomial series derived by integrating the binomial expansion of(1-m sin²theta)^-1/2:

 C(m)=2K(sqrt m)/pi=sum_(n>=0)[binom(2n,n)/4^n]^2 m^n.

Every coefficient is at most1, so retaining N terms has remainder at most m^N/(1-m), uniformly at most(16/27)^N/(1-16/27). All operations are rational interval arithmetic and integer square roots; pi cancels from the normalized series entirely. N depends logarithmically on accuracy and does NOT grow as s approaches0.

If C lies in[S,S+r], square it monotonically. The prefactor (1-9xi^4)/d is positive and at most64/27, and1/q<=1/6. Thus the series-tail contribution to A is at most(32/81)(2S r+r²). Parameter/radical errors must be added by actual interval evaluation; this is not a full floating error certificate. It gives an explicit uniform alternative to the return series whose ratio approaches1 at smalls.

## A0 subtraction, derivatives and B

A0 need not be separately subtracted: equation(1) and the uniformly convergent C series evaluate A(s) directly at arbitrarily small positive s and at0. Computing A0-A(s) by subtracting separate enclosures may still lose relative accuracy. A joint derivative/Taylor enclosure in s, using (1), avoids this: all denominators in (1) stay positive, sqrt(s²+12) stays away from0, and the right-hand expression is one-sided analytic near0. It reflects the physical linear cusp under even extension in s, rather than incorrectly assuming an analytic function of s² there.

Derivatives of C have explicit tails, e.g. sum_(n>=N)n m^(n-1)<=N m^(N-1)/(1-m)+m^N/(1-m)². Chain-rule interval evaluation can therefore certify A' jointly. For the B-transform divided difference, use a shared expression or interval derivative for zA(sqrt z) near coincident parameters; independent high-precision A evaluations alone are not a relative-error guarantee.

## Certification and scope

Next implement the rationalized formula and positive C series with outward roots; independently check the imported modulus/parameter convention against exact return-series coefficients or overlapping certified A intervals before any downstream physical use. A rigorous source-based implementation must bind this mathematical import and independently validate its transcription; the present work does not reprove Joyce's identity. No physical evaluation or new pilot has occurred. Existing A0<=17/60 remains the campaign's established bound until a new certified calculation is reviewed. The model/reference are still supplied, and no alpha sign or value follows from an efficient A oracle.


## Preserved method derivation: native-elliptic-b-transform-stretch

# Fixed B/B' positive-transform pilot design

UNLAUNCHED. Actual native h1, s1 and2, target width1e-6 for both B and B'. This is a prospective implementation contract, not a timing or target-pass claim. It uses the reviewed positive transform and an independently validated elliptic A/A' oracle. The latter's physical pilot is still pending at preparation time.

Let G_s(t)=E[X/((X+s²)(X+t²))] and H_s(t)=2s E[X/((X+s²)²(X+t²))]. Then B=(2/pi)int G and B'=-(2/pi)int H. Both integrands are positive. Write a=A(s), da=A'(s), b=A(t), d=t²-s². For d!=0,

 G=(t² b-s² a)/d,
 H=[(2s a+s² da)d-2s(t² b-s² a)]/d².

These formulas retain shared interval values and do not take differences of separately rounded midpoint answers. Both apparent singularities are removable analytically. The pilot places s at dyadic panel endpoints; even Gauss nodes avoid coincidence. An interval denominator that nevertheless contains zero fails the entire case; it is not shifted or clipped.

## Fixed error allocation and schedule

Low cutoff epsilon=2^-28, upper cutoff T8. Middle panels[2^j,2^(j+1)], j=-28,...,2:31panels. Use12-node Gauss on each,372nodes shared between s1 and2. Reuse node/weight enclosures from the exact Legendre implementation, preserving its source snapshot. No outcomes select nodes or change p.

Low tails satisfy int_0^epsilon G<=epsilon A(s)<=epsilon/s² and int_0^epsilon H<=epsilon(-A'(s))<=2epsilon/s³. Thus2/pi times either low tail is below4epsilon/3 for these s.

On |z-c|<=c/2, |X+z²|>=X and >=c²/4. Therefore

 |G_s(z)|<=min(1/s²,4/c²),
 |H_s(z)|<=min(2/s³,2/(s c²)).

A common envelope for s1,2 is min(2,4/c²). Summing a M(3a/2) over all dyadic a is bounded by2+32/9=50/9. The rho5/2 ellipse argument yields a total middle integral error at most(1000/27)(4/25)^12 for either integrand. Multiplying by2/pi<2/3 gives(2000/81)(4/25)^12. This is an absolute error; add it on BOTH sides of a computed quadrature enclosure. The low-tail interval is one-sided, not symmetric.

High tail: use16terms. Cn=E[X^(n+1)/(X+s²)], C0=1-s²a, Cn=Mn-s²C_(n-1). Let En=-dCn/ds, so E0=2s a+s²da and En=2s C_(n-1)-s²E_(n-1). These are actual positive coefficients; interval recurrence may be wider and must not be clamped without justification.

 int_T^infinity G=sum_(n<16)(-1)^n Cn/[(2n+1)T^(2n+1)] +positive remainder,
 int_T^infinity H=sum_(n<16)(-1)^n En/[(2n+1)T^(2n+1)] +positive remainder.

The G remainder is bounded by12^16/[33 T^33]. The H remainder is at most1/(2s) times that bound, using X/(X+s²)²<=1/(4s²). Moments Mn are exact native multinomial integers. At T8 the expansion ratio is12/64. The sign is positive because16 is even. Add the remainder as[0,bound].

## Arithmetic implementation requirements

Make a new explicit oracle version with192-bit dyadic interval operations and160elliptic terms; leave the original96term physical-pilot source immutable. Each actual A/A' enclosure used must have width<=1e-30 or the case fails. This width is a checked gate, not inferred from the term count. Enclose A(t) at a Gauss-node interval by monotonicity using oracle endpoints; that requires up to744 endpoint oracle calls shared across both s cases. Fixed As/As' need two further calls. A tighter derivative-based node enclosure is a later optimization, not silently assumed here.

Use outward Gauss weights and nodes; sum signed G/H interval expressions with full interval arithmetic. Include node widths, coefficient-input widths, moment recurrence widths, pi enclosure and every outward rounding. Final interval adds low/middle/high budgets as above, then applies2/pi; negate for B'. Target achievement is based on FINAL WIDTH, not just analytic truncation bounds. Midpoint values are not certificates. Save partial interval sums by panel and both final rows, including every input oracle interval or its lossless bound receipt.

## Cost and remaining readiness

The important prospective cost is746 higher-precision oracle calls plus exact Gauss rule/moments/interval accumulation. This may exceed a30-second whole-tree384MiB attempt; no feasible timing is asserted before the pending elliptic pilot. Forecast using its measured maximum per-oracle time with an explicit precision/method headroom, then decide a new frozen cost contract. If that forecast is not credible, first cost a fixed subset under a new preregistration rather than launch the whole target opportunistically. This document does not authorize any oracle or integral calls.

A source-level implementation must also preserve progress before comparisons/failures, bind the oracle and Gauss versions, and pass tiny synthetic spectral-measure identities for G/H and both tail recurrences. No actual B value, Gram spectrum, alpha or final precision certificate exists yet.


## Execution chronology and live scope

The preserved method texts contain prospective wording from before their once-only attempts. They are provenance, not the current execution status. Return and elliptic/B results and root acceptance files are now present. Their source-specific independent reviews are preserved. Canonical review is pending. No provisional higher-order Gauss, uniform batch, Krylov or future compression extension is part of this live claim.
