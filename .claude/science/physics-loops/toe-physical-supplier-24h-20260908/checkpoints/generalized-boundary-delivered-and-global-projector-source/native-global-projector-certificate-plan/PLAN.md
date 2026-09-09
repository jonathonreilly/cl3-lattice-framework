# One coherent prospective projector certificate

Status: analytic parameter plan only. No quadrature nodes, oracles, coefficients, native moments, matrices or scientific outputs evaluated. Original66-pole protocol and outcomes remain unchanged. High-tail proof independently reviewed here; low-tail independent review is pending. This combined design is not an execution contract or an achieved projector approximation.

## Candidate and conventions

Use one consistently signed spectral projector difference D=P_A,+-P0,+ (or negate every term for the negative convention). The candidate is the sum of: (i) p-node dyadic Gauss resolvent-difference quadrature on[h*2^-Jlo,16h]; (ii) the explicit zero-frequency finite-rank term +epsilon F0/pi for the positive convention, where epsilon=h*2^-Jlo and F0=R_A(0)-R0(0); (iii) the exact odd-power high-tail correction throughN terms from16h toinfinity. Low-tail source writes the negative convention, so its correction must be negated here. Real rephasing and particle-hole partner closure must preserve that sign.

Error components, dimensionless, are

 low <=(2/9)(5439/160)2^(-3Jlo/2)+(867/192)2^(-2Jlo),
 high <(1/8)(9/64)^N[1+18/(64(2N+3))],
 quadrature <=429(4/25)^p,
 numerical <=a separately certified budget.

The low formula holds for Jlo>=7. For integer-only planning, replace2^(-3Jlo/2) by2^(-Jlo-floor(Jlo/2)). The quadrature bound is the original operator-valued rho5/2 theorem summed over all dyadic panels, so it applies to the extended interval. Scalar rho5 does not transfer to this operator resolvent proof. Numerical error includes EVERY new root/weight/scalar/coefficient/finite correction/cross-Gram/rounding contribution required to assert an operator S1 approximation; a cache entry width alone is not that bound.

## Exact parameter table

Each component gets one quarter of the target. PARAMETERS.json contains exact rational component and total upper bounds, generated without scientific evaluations.

| target eta | Jlo | Jhi | Gauss p | high N | positive poles | common raw dimension upper | closed upper |
|---|---:|---:|---:|---:|---:|---:|---:|
|1e-6|17|4|12|7|252|1554|3108|
|1e-8|22|4|15|10|390|2400|4800|
|1e-10|26|4|17|12|510|3132|6264|
|1e-12|30|4|20|14|680|4164|8328|

At1e-12 the total is below the target with numerical allocation2.5e-13. This is a sufficient budget, not a prediction of actual error and not an actual lower error floor. Less conservative source-dependent bounds may use fewer columns, but need proofs/certificates.

## Support alignment and new data

For a single impurity, each positive pole contributes two local resolvent sources at both frequency signs, at most4 columns. For a common two-impurity orbit, use center and the two signed neighbor sums, three sources at both signs: at most6 columns per pole. The high correction of orderN is supported on their bare H0 Krylov powers0..2N-2, at most3(2N-1) common columns. The low correction uses their three zero-frequency inverse columns. Hence a safe common raw bound is6*p*(Jlo+4)+3+3(2N-1), before reference-Gamma doubling. Overlaps may reduce rank but are not assumed. Five orbit cases reuse literal geometry; this table does not assume their matrices are identical.

The existing66 poles generally do not coincide with the new Gauss roots. Their old source evidence can support imported inequalities but cannot be relabelled as new node values. New nonzero-s A/A'/B/B' certificates, mapped root/weight intervals, source separation and error propagation are required. Existing scalar catalogs might support those values with a new certified contraction; no such reuse is assumed automatically. The extra zero-frequency inverse-center Gram needs its own bound/value certificate. Bare high self-Grams require exact integer moments through2N-1 (27 at N14); these can be computed combinatorially but were NOT computed here. Rational/bare/inverse cross-Grams follow finite polynomial division and exact local resolvent identities with a separately audited sign/rounding ledger. Left reference-projector upper bounds can use contraction to avoid new higher half-moment suppliers, at a cost in sharpness.

No DATA column becomes part of the original24 trial span merely by appending it. The occupation raw-bank theorem uses this enlarged bank as a finite-rank supplier Chat; the original selected projection can remain24, with its finite complement term explicitly retained. If the trial span is enlarged later, that is another declared approximation.

## Cost and attainability boundary

At1e-12, the4164 raw upper triangle has8,671,530 pairs per common orbit. Storing G and J with two192-bit endpoints each requires at least96bytes/pair before indexing or Python objects:832,466,880bytes. Thus the straightforward full interval cache exceeds384MiB even for one orbit. No30/60/120-second execution ceiling can be claimed from the current much smaller cache timing. The fixed680-pole scalar family is over ten times the old66; its precision requirements are also different.

A feasible future design must stream structural blocks, compute only consumer-weighted trace/nuclear upper bounds, exploit exact displacement structure, or use a newly certified low-rank factor scheme. The present parameter table does not choose one or promise it fits. Potential scientific value is that Chat can bound occupation mass and residual objectives without natural-mode square-root continuity; computational benefit still requires actual structured implementation.

Even eta=1e-12 alone gives only the generic omitted-occupation Fock bound sqrt(43.5 eta), of order7e-6, before propagated residuals, CAR insertions, scalar Delta error and Laplace integration. It is not an alpha-error certificate. Root's targeted consumer budget must determine whether this eta is sufficient or excessive.

## Next discriminating source work

First finish independent low/high proof review and improve the operator quadrature envelope if a genuine bound exists. Then choose a consumer-specific finite factor objective and derive a streaming operation/memory count. Only after a full source/error/runtime review should any new nodes or scalar contractions be preregistered. Launching small disconnected refinements now would not certify the combined operator approximation.
