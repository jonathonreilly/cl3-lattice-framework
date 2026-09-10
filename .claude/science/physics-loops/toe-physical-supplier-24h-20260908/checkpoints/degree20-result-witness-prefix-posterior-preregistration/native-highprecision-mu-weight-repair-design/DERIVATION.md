# Explicit weight-width repair: high-precision mu, unlaunched

This is distinct from the completed coarse mu study; no old protocol or output changes. In h=1 units X=6−2Σcos(theta),0≤X≤12, E X=6. Tonelli gives mu=E sqrt(X)=(2/pi)∫_0^∞ Q(t)dt, Q(t)=E[X/(X+t²)]=1−t²A(t). General scaling is mu(h)=|h|mu(1). No new oracle is needed, but this is a NEW physical integral requiring its own review and preregistration.

On the same rho=5/2 ellipse over[a,2a], center3a/2, semiaxes29a/40,21a/40, u=Re z≥31a/40 and |v|≤21a/40. The exact resolvent identity in the c_minus proof gives |Q(z)|≤sec(arg z)E[X/(X+|z|²)], with sec²≤3200/2759<(27/25)². Also |Q(z)|≤6/(u|z|)≤9600/(961a²). These suffice, but a sharper simple bound is available: u²−v²>0 throughout this ellipse, so |X+z²|≥X and |Q(z)|≤1. No positivity of complex Q itself is asserted.

Thus use M(a)=min(1,9600/(961a²)). Split the dyadic sum at a=2: Σ_(a≤2)a≤4, Σ_(a≥4)1/a=1/2. Hence ΣaM≤4+4800/961. The same reviewed analytic Gauss theorem gives TOTAL middle quadrature radius

 R=(20/3)(4+4800/961)(4/25)^26.

The often suggested3.24 times c_minus bound does not follow just from the small-pole envelope; the large-pole X numerator increases its bound. We retain the explicit valid dyadic sum above.

Low tail[0,2^-64] lies in[0,2^-64]. For t≥8,26 exact terms are
 Q(t)=Σ_(n=0)^25 (-1)^n E[X^(n+1)]/t^(2n+2)
       +E[X^27/(t^52(t²+X))].
Therefore integrated high partial uses M1..M26 with denominator(2n+1)8^(2n+1), and the positive remainder is ≤12^27/(53*8^53). The original proposed indexing is correct. It is not M26 in the remainder. Moments use the exact central-binomial multinomial formula, not numerical quadrature.

## Endpoint/cancellation and prospective full-width budget

At each actual Gauss root, accepted monotone endpoint A bounds enclose A(t); multiply the full t interval squared by that interval and subtract from1 using192-bit outward arithmetic. Correlation loss is safe. Large-pole subtraction cannot erase the certificate because exact directed rational endpoints, not floating cancellation, are used.

Require every saved endpoint A width≤1e-30; each node t width≤2^-140 and weight width≤1e-38; 0<t≤8; sum upper weights≤9. The reviewed global |A'|<1/3 and A≤17/60 give the monotone combined A interval width≤2e-30+2^-140/3. The resulting Q interval width is less than2e-28. Positive weight multiplication/summation,1742 nodes, and192-bit outward roundoff then give a conservative middle interval full-width≤1e-25. The code must check this aggregate width before claiming target success. The scalar B-input catalog is not used.

With pi>157/50, analytic-plus-middle full-width bound is
 (100/157)(2R+12^27/(53*8^53)+2^-64+1e-25)+1e-35 <2e-19.
The1e-35 allowance covers the far smaller fixed Machin32/10 multiplier width times an integral bound10 and its outward rounding. All these are predata rational inequalities, not a measured mu interval. The valid bound is about1.918e-19, leaving a small but positive prospective margin. Actual saved geometry and middle width must pass; otherwise retain INDETERMINATE/failed gate with all data, never refine or rerun silently.

The source copies reviewed interval/pi routines; new loader and compute are explicit. All67 panels and the complete interval/tail/error ledger are retained. No integral, oracle or cost run has occurred. A proposed30-second/384MiB once-only contract requires separate runtime closure, independent review and root monitor before execution.

## Original failed attempt and revised premise

The original f9e4 attempt FAILED in the loader before compute:130 saved weights violate the unsupported2^-140 width assumption. No mu integral began and no result exists. The original source, root and failure remain immutable; this is a separate explicit repair requiring independent review and new preregistration.

Exact saved-only inventory of all1742 nodes establishes weight widths<2^-128<1e-38, positive ordered weights and sum upper weights<9; all3484 accepted endpoint bytes and1742 A interval orders were verified. The actual maximum width is approximately1.6476e-39. No new oracle is needed to validate this premise: the prior accepted catalog proof encloses the true Gauss weights, and the actual rational endpoints supply their widths. Root bracket precision alone had not justified the previous weight-width bound.

With Q interval width<2e-28 and |Q|≤2 for its tiny endpoint enclosure, total middle uncertainty is bounded by9*2e-28+1742*2*1e-38 plus192-bit rounding. This is below2e-27, hence still below the unchanged1e-25 aggregate gate. The t-width bound remains2^-140. Analytic radius, low/high tails, moments, pi formula, nodes and2e-19 target are unchanged. The old conditional proof was not false, but its applicability to the saved weights was; this separate proof closes precisely that premise. No achieved integral precision is asserted before execution.
