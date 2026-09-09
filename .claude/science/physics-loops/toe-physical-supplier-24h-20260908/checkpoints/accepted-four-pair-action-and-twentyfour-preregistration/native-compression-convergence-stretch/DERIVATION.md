# Compression progress does not yet price propagation

Provisional analytic stretch; no native computation. Input hashes identify only the four- and twelve-pair root scalar summaries. Twelve-pair saved POST remains a separate acceptance obligation. Descriptive decimal values below are copied summaries, not newly certified exact endpoints. Existing targets and frozen12→24 protocol are unchanged.

## 1. What the actual metadata says

All five twelve-pair cases remain PAIR_CAP. Reported raw residuals are0.00131259–0.0138556, versus target r*=1/(1062*10^6), approximately9.4162e-10. Coordinate d² is at most7.379e-20, far below its fixed1/40000² gate. Last pivot relative widths are between2.62e-10 and2.54e-9. Thus the observed failure is residual size, not the current coordinate gate; this is not evidence that inverse pivot coefficients are well conditioned.

Across the eight added pairs the residual ratios are0.00467–0.01249. Purely descriptive geometric per-pair ratios are0.5113–0.5782. If, counterfactually, those average ratios persisted for twelve further steps, r24 would be4.19e-7–1.93e-5, still above the target in every orbit. This is neither a convergence theorem nor a fitted timing forecast. It gives a useful falsifiable expectation: reaching the target by24 would require materially faster decay than the observed eight-step average. It does not justify stopping the already selected fixed study or relaxing its target.

## 2. A rigorous but weak generic greedy bound

Let f_i be399 real half/insertion seeds, w_i=2 for396 halves and1 for3 insertions. For a Gamma-invariant projection P, let d_i=||(1-P)f_i||² and r=sum w_i d_i. Total W=sum w_i=795. Suppose each diagonal interval has width≤epsilon and encloses d_i. The algorithm selects the largest strictly positive lower bound. Whenever r/W>epsilon, some eligible lower bound is positive and selected d_j≥r/W-epsilon. Adding its exact normalized pair removes at least w_j d_j from r (its own residual becomes zero); other contributions cannot increase. Hence

 r_next≤(1-1/795)r+epsilon.

For exact arithmetic epsilon=0 this proves only a very slow worst-case decay, not the observed factor near1/2. If r/W≤epsilon the bound gives no positive-pivot guarantee. The statement is about exact residuals; recomputed outward upper bounds need not be monotone. It does not claim the code's scalar upper trajectory obeys this recurrence without tracking interval widths.

This bound exposes the missing ingredient for a fast a priori guarantee: a native spectral-width/low-rank property stronger than generic positivity. The finite rank ceiling399 paired directions is exact but not an affordable or well-conditioned algorithm.

## 3. Two independent obstacles to inferring leakage

Small approximation residual is not inverse-coordinate conditioning. In a finite real Hilbert space take seeds e1 and e1+epsilon e2, plus their Gamma partners. At full span the residual is zero; representing normalized e2 requires coefficient size1/epsilon. The normalized coordinates of the original seeds can nevertheless be evaluated exactly (coordinate-radius d=0). Thus d controls the forward representation, not the inverse C.

Even residual zero and well-conditioned C do not imply small generator leakage. Choose Gamma-paired modes e1,e2,e3, let F span the first two mode pairs, and let real skew K map mode2 to mode3 and mode3 to minus mode2, identically on both Gamma components. K commutes with Gamma; H=iK is self-adjoint with norm1. The exact isometry V for F has ||(1-P)HV||=1 although r=d=0 and an orthonormal F has coefficient condition1. This is an abstract counterexample to an inference, not a claim about the actual native H. The native added bare q sources contain precisely the extra first-action information needed to rule such behavior in or out.

## 4. A usable sufficient diagnostic connecting residual and action

Use the canonical closed ORIGINAL F and DATA Z, exact ideal V=FC, P=VV*. The weighted half residual satisfies ||(1-P)F||_HS²=2r: each pole half reconstruction preserves the stated2 weight, then Gamma closure duplicates the raw trace.

Write the first-action coefficient identity as K_A F=F Lambda+Q T_A. Lambda is diagonal sigma*s on pole raw coordinates and their partners, zero on insertions. Q contains x0,qA,qC,qD and their partners; T_A includes source coefficients and the actual rank-two Gram-row correction. Q may overlap F, which does not invalidate the identity or triangle bound. Therefore

 delta_A=||(1-P)K_A FC||
 ≤sqrt(2r)||Lambda C|| + beta_Q ||T_A C||,
 beta_Q=||(1-P)Q||.

The small matrix Q*(1-P)Q=Q*Q-(Q*FC)(C*F*Q) encloses beta_Q² from the same DATA principal block; no second action is required. This diagnostic is only useful with certified C and coefficients. A conservative l1/Frobenius bound may fail from cancellation although the exact leakage passes. The direct small leakage matrix L=B*MB+T² remains the sharper definitive test.

If a certified diagonal lower bound L_ii exceeds delta_target², the current subspace fails that sufficient leakage target regardless of basis rotation. If the row-sum upper bound passes, the existing propagation theorem applies with its additional particle/state premises. If neither occurs, the enclosure is indeterminate. Rotating within the same exact subspace cannot alter leakage operator norm, though an alternative coordinate representation can improve arithmetic conditioning.

## 5. Why doubling pairs can move the bottleneck

For k pairs, p=2k, R≤4k and U≤4k+8. The principal Gram request bound is U(U+1)/2 per orbit. The currently implemented direct contraction bound across five orbits/two impurities is

 10*(2k)^2*((4k)*(4k+8)+(4k+8)^2).

It equals614400 main summands at k4,33546240 at k12,479232000 at k24. These are arithmetic counts, not time forecasts; they exclude coefficients, correction terms, indexing and interval overhead. Thus a cheap continuation can create an expensive downstream action certificate. The four-pair action contract cannot be extrapolated to24 pairs merely because scalar compression is fast. Conditioning guards may become harder as pivots shrink.

The leverage is to retain one fixed candidate subspace and test the separate C/action bottleneck before authorizing blind further doubling. A source-only optimization may exploit block matrices, common coefficient support or a validated factorization, but it must preserve the exact ideal-isometry premise and interval correlations. A new Krylov domain containing q would need its own action data beyond this ORIGINAL-domain theorem; it is not a free alternative already certified here.

## 6. Falsifiable continuation decision, no weakened gates

The fixed12→24 study retains its original residual and coordinate gates and cap. At its terminal point classify separately:

1. Residual/coordinate pass: compression only. Require actual positive pivot intervals and inverse coefficient gates, then separately priced sparse action and leakage. No automatic propagation claim.
2. Residual fail with resolved pivots: record exact residual lower/upper trajectory and interval widths. Compare the observed contraction with the explicit descriptive expectation above; do not label a failed geometric extrapolation a physical no-go. Further continuation requires a newly bounded full pipeline cost, including action at the enlarged k.
3. Conditioning or precision failure: do not infer rank exhaustion. A new coordinate representation or higher arithmetic precision is a separate protocol, not an implicit retry.
4. Certified leakage lower bound above target: basis rotation alone cannot help; change subspace or source strategy under a new proof/data contract. Compression convergence alone is not the deciding signal.

This is a concrete go/no-go rule for scientific reuse, not a change to the current execution contract. The propagation theorem's one-particle sufficient delta≤h/10^6 at t≤100/h remains unchanged. The stronger398-particle example needs delta≤h/10^9 plus an independently established particle cutoff; small r alone establishes neither.
