# Independent review of the infinite h/4 refinement

**PASS**, bound to DERIVATION.md6d661ed665bca2dee06dab7f977d7fc6b6ec39deaf265e74c9bb48c37387ecab, check.pyf023a3e10caa88d2cdec55a91ed2394fb6aa52d6370f0581b1ca54dbec87630f and RESULT.json35ef7f1c5124d023a487de78e087f488c4d4e88ff437427bcc97df4be5dd6ab8. Read all three completely. Reuse explicitly my complete prior determinant/Green/finite-to-GNS review17d56392; the only new mathematics is retaining additional positive logarithmic contributions and changing the tail parameter.

For opposite pairs, g>=[32/(s²+7)²] and -log(1-g)>=g+g²/2. Multiplication by the full-active1/(2pi) gives4/(7sqrt7) from the first term and40/(343sqrt7) from the second. The second coefficient is512*(1/(2pi))*5pi/(32*7^(7/2)); no extra parity or spectator factor belongs here. Since sqrt7<8/3, the claimed rational lower bound is177/686>1/4.

For perpendicular pairs, the earlier proof establishes nonnegative -log d on the entire half-line and the lower function g_P on s>=1. Its numerator24-8/s² increases, its positive denominator(s²+7)² increases. Bounding the former from below at a and the latter from above at b is valid on each interval regardless of whether the ratio is monotone. There are exactly304 disjoint intervals from1 to20. The prefactor7/44 is a lower bound on1/(2pi), and every rectangle is positive. The omitted tail beyond20 is nonnegative by the original proof. Hence adding these rectangles to the old [0,1] contribution is legitimate.

My independent exact calculation simplifies each rectangle to7168(24j²-2048)/[11j²((j+1)²+1792)²], then sums those fractions. It agrees exactly with the supplied large rational tail. Combined with the already independently checked old low-frequency fraction, it gives approximately0.2655410478>1/4. Decimals are descriptive only; comparisons are exact.

The finite-to-GNS passage is unchanged: the actual finite energy differences converge, then their lower limit passes on local polynomial vectors. The result is the infinite operator inequality D_A>=h/4 in the same Gaussian reference. There is still no explicit finite-L h/4 threshold, impurity vacuum-existence assertion, or active bulk gap.

For delta=h/4, beta<3h and T=100/h, the bracket in the full90-word tail is(32+4800+384)/h². Its exact degree160 exponential lower sum at25 yields an upper error approximately8.14944546e-7/h², strictly below10^-6/h². This budgets only the time tail, leaving relatively little of a10^-6 total budget for other errors; it is not a claim that the complete computation has that total error.

One tiny independent exact control ran once:0.02s,15,990,784bytes maximum RSS, no physical run. Its five predicate groups cover rectangle equality, perpendicular comparison, opposite comparison, integral normalization and tail. An initially mislabeled counter field was corrected without rerunning arithmetic; predecessor source and raw output are retained explicitly. The author's research checker uses assert, so a future canonical-OO port must replace these with active predicates; this does not affect the mathematical verdict or its ordinary exact result.

The refinement can replace h/6 by h/4 and160/h by100/h in the corresponding infinite-gap and tail statements, preserving the old proof/source. It leaves alpha and all spatial/covariance/quadrature/phase claims unchanged.
