# Independent mathematical source review — native Wilson #8007

This is a source review of the three exact conditional mathematical claims on the frozen candidate in FROZEN_SOURCE.json. It is not an audit, retained-grade application, physical identification, or global TOE result. All three canonical notes and all five canonical runners were read in full; the entire 64-file historical packet was read, with identical duplicate proof/log bodies reused only after explicit diff comparison. The two actual parent proof notes were read in full. Computational runtime closure is only the five self-contained modules and their standard/third-party libraries.

## Native normalization and multiplier coefficient

The six-neighbor step set divided by six is invariant under the two Weyl reflections in dominant-weight coordinates. Killing nonpositive shifted coordinates agrees with omitting negative unshifted labels. An independently written exact integer walk/reflection calculation compared 1,053 entries (steps 0–12 and 81 endpoint labels at each step). This checks the finite combinatorial identity, not an infinite asymptotic estimate. The read recurrence parent separately supplies the representation-ring origin and the reflection parent derives the Fourier identity. No physical group-convolution normalization is imported: its representation-dimension division is a different object.

For a=k²−kl+l² and Δ=(2k−l)(k−2l)(k+l), the Gaussian transform of exp(−a/3) is sqrt(3)/(2π) exp(−Q). Direct differentiation gives the numerator transform D0 W with D0=27sqrt(3)/π. An independent Wick recursion with covariance [[2,1],[1,2]] gives EΔ²=324, the Δ²-weighted moments E a=12 and E a²=180. Therefore the denominator's first correction is 180/36−12/2=−1. This explicitly retains the factor six and the numerator orientation; it does not infer normalization from agreement between implementations sharing a formula.

Multiplication by a transforms to −3L. Consequently the first numerator correction is (L²+3L)W/4. Combining it with the denominator correction gives W2=(3−7Q/4+Q²/4)W. The independently differentiated expression agrees exactly. In particular the diagnostic alternative W2−W is the unnormalized-numerator coefficient, not an equally valid convention for v.

## Remainder and global extension

The canonical proof uses a≤β/2 inside the scaled torus, a stable cosine deficit and sinc alternant. The quartic identity and alternating Taylor bounds yield 0≤a/3−βψ≤a²/(36β), sixth-order error bounded by a³/(810β²), and Gaussian damping 23/72. The sinc product's quadratic correction is −a/(4β); its squared product has correction −a/(2β). The stated product remainder estimates supply the displayed numerator and denominator polynomial bounds. I checked their combination, Gaussian moment powers, rational coefficients and the stricter low-cut constants against the exact scalar checks, not merely their printed labels.

On the complement a>β/2, dropping the third cosine term and using the coordinate torus bounds yields βψ≥a/24. The incomplete-gamma tails reduce to finite polynomials times exp(−β/48); β≥2048 exceeds the maximum monotonicity threshold 5·48. The proof's positive Taylor lower bounds for exp(128/3) and exp(512/3) justify the chosen exact rational ceilings without fitted values. The approximation tail also includes the part outside the scaled torus. Summing gives CN<171 and CD<2618.

The algebraic identity Q³−27H²=(x−y)²(x+2y)²(2x+y)²/4 is exact. Its global consequence bounds W, QW, Q²W and W2 as stated. The denominator is uniformly positive for β≥2048, and subtracting D[W+W2/β] gives the exact residual cancellation used in the note. The final conservative ratio coefficient 76675625/2685312 is less than 29.

The global endpoint extension is justified: endpoint dependence disappears through |exp(−iz·x)|=1 in the numerator error, and the remaining multiplier bounds hold everywhere in the positive chamber. No compact-window hypothesis remains in that argument. This supports every actual shifted dominant label for all real β≥2048; it supplies no relative-error estimate when W is tiny and no theorem at the numerical witnesses' lower β values.

## Exact heat sandwich and topology of the limit

The Schur bound on J makes Pβ=exp[(β/2)(J−I)] a contraction. Scalar factors commute, giving the exact normalization Aβ=Pβ Mv Pβ. The supremum entry bound therefore gives the same-space operator norm remainder. The sampled saddle multiplier is exactly exp(3/β)W because the dimension and Casimir shifts are retained. Its scalar Taylor remainder is bounded by 768/2045 after multiplication by sup W. Thus the insertion f=W2−3W=Q(Q−7)W/4 and the remainder less than 30/β² have the stated normalization.

I read the parent reflection/compact-sandwich proof, including its cell embedding, local central limit theorem, return-kernel bound and positive simple Perron branch. Applying the weighted Hilbert–Schmidt argument to f+ and f− is legitimate: they are continuous with integrable Gaussian-polynomial envelopes; differentiability at Q=7 is not required. The exact HS norm formula and uniformly controlled tails give weak HS convergence plus norm convergence, hence strong HS convergence. Taking B*B gives trace-norm convergence of the two positive insertions and their difference. The final normalized full operator difference is claimed only in operator norm, because its residual has only that control. The note does not promote this to a trace-norm claim or a fixed-continuum-saddle expansion.

Injectivity of the Dirichlet heat operator implies dense range; no bounded inverse is assumed. Strict positive and negative multiplier regions can be approximated from this range, proving indefiniteness. The dense-range sesquilinear argument also proves nonproportionality. Neither alone determines the Perron expectation, and the note states that limitation.

The isolated top-mode comparison uses the positive limiting spectral gap, norm convergence of the sampled saddle, convergence of its rank-one projection and a uniform reduced-resolvent estimate. The resulting coefficient is a difference relative to the exact β-dependent saddle. There is no need to know that saddle's own first correction, and the note does not claim it. Embedding adds zero modes but preserves the nonzero top eigenvalues. No excited branch or ground/excited ratio is supplied.

## Perron sign

The transfer from T0=A*A to B=AA* normalizes the actual Perron vector u=sqrt(W)Sφ0/sqrt(μ0). Thus d0/μ0 is the expectation of R(Q)=Q(Q−7)/4 in |u|². The positive operator inequality B≥μ0|u><u|, applied to bounded truncations of g=(R+1)+ and then monotone convergence, controls the actual Perron distribution by the weighted heat trace. A trial vector is used only for a lower bound on μ0, never substituted for u.

I independently derived the chamber metric-polar change of variables and both angular moments. They give the note's H and H² radial factors and retain the chamber angle π/3. The scalar upper envelope for g holds on each of the three declared intervals. The low integral and shifted high integral reduce to the exact expressions in the proof; the latter polynomial moment is 80. With exp(6)>400, this proves J<7/1944.

Direct independent differentiation verifies the exact Dirichlet heat solution (1+t)^−4 H exp[−Q/(1+t)], including both walls and initial data. Its Rayleigh quotient is 2sqrt(π)/(243sqrt(3))>2/243. Combining the two bounds proves d0/μ0<−9/16 and d0<−1/216. The pointwise lower minimum −49/16 occurs on a measure-zero ellipse, so normalized L² mass gives the strict lower inequality. The resulting eventual eigenvalue ordering has no explicit onset. Frozen Nyström values were inspected as historical diagnostic data only; they supply no proof premise and were not rerun.

## Boundaries and remaining findings

The mathematical obligations above are closed within the explicitly supplied native representation/reflection/Dirichlet setting; the overall physical claim remains CONDITIONAL. The actual source closure supplies no derivation of physical Wilson convolution, action selection, an environment, observation, continuum field theory, confinement or a physical mass gap. Those gaps are not treated as independent proved no-go walls. N1 honestly reports one constructive family, and the packet explicitly retains heavy negative-packet NOT PASS. N2 lists related supplied hypotheses without asserting independence; no additional five-family or independence result is fabricated here.

There is no additional actionable mathematical, N1/N2, parent-epoch, or reservation finding. The frozen findings are narrower: disagreement between two helper discovery consumers, numerical support PASS assertions that do not discriminate their named scientific targets, and canonical draft framing prohibited by the landing contract. These must be corrected before source acceptance; the analytic arguments are not invalidated by a surviving numerical mutation.
