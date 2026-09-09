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
