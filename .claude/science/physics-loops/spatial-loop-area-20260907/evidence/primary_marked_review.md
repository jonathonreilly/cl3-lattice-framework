# Independent cold review: complex marked expansion and spatial area suppression

Verdict: PASS for the two frozen derivations in their stated supplied-Hamiltonian, sufficiently small coupling, periodic-volume/selected-limit scope. This review checks applicability and the additional counting/normalization argument; it does not claim to reprove the imported general polymer construction or KP theorem. No integration files were edited and no finite checker was rerun.

Bound files:

- Native `/private/tmp/toe-autonomous-native-ladder-20260907/spatial-loop-area/DERIVATION.md`, SHA256721889e76b351390a016374434ae3708c9d16e3d9bfe097333381bd1c08c070e.
- Root `/private/tmp/toe-campaign-20260907/spatial-area-suppression/ROOT_DERIVATION.md`, SHA2563d2d869494e39a844d904e664aaf20605c2420bab3d562d3b7f57a8ded7ee031.

My independent charge-selection proof was frozen before I read these marked-expansion proofs. Initial route suggestions and the root's later periodic qualification were shared and remain disclosed. Thus this is an independent critical review, not a blind-discovery claim.

## Primary source checks

I directly inspected [Yarotsky0412040](https://arxiv.org/pdf/math-ph/0412040), hypotheses/Theorem1 and Section2, including Lemmas1–4, support definition(13), printed page10 ordinary count and page11 marked insertion/analyticity. The paper allows infinite local spaces and unbounded classical local operators, but requires a unique vacuum on the entire common-range block. Its inclusion–exclusion terms have sectorial complex-parameter norm estimates. Ordinary activities admit epsilon-to-support-size bounds and exponential support counting; the marked insertion loses the marked-support power. These are actual statements of the construction, not deductions from weak-star analyticity alone. It uses periodic translation-invariant volumes. The proofs accurately restrict their applicability.

I also directly inspected [Fernandez–Procacci0605041](https://arxiv.org/pdf/math-ph/0605041), equations2.7 and2.12–2.15. The alternative KP inequality implies the absolute pinned sum bound exp(a); self-incompatibility is included. Both papers are explicit load-bearing mathematical imports. No numerical threshold is supplied by their invocation here.

## Four-cell vacuum map

A tail cell carries three full outgoing-link L2 spaces. Its normalized electric k_x has unique vacuum and gap1 by the all-label Casimir result. The common-range term must be sum of the four neighboring k_y, not k_x tensored with unused identity factors. The former has unique vacuum on the whole four-cell block, as required. Summing it periodically gives4 sum k=aK. Thus the perturbation is -u times the three normalized face traces, with norm<=3|u|, and the total is aH minus its scalar face count. The block34 normalization3u/4 must not be substituted here. Both reviewed proofs make this distinction correctly.

For bounded perturbations, one can fix an arbitrarily small positive relative-bound parameter and then shrink the disk's bounded remainder. Choose the time step large first; subsequently choose these perturbation constants small enough to meet the activity target. This is consistent with Lemma1's exponential factor and Lemma3's excitation suppression. There is no requirement to bound the onsite upper spectrum, and no local-dimension factor is introduced.

## Marked counting and weighted KP calculation

The marked perimeter set is all perimeter vertices regarded as tail cells, with the unused corner padded by identity. It is connected and has m=P sites. This avoids a disconnected-source animal-count problem. On a fixed finite-range space-time graph, the expanded local support pieces have bounded diameter and bounded-degree connectivity. A connected marked support of n points containing one prescribed mark has at most exponential-in-n encodings by a spanning-tree walk. The binary insertion/excitation sets have only exponentially many decorations for a fixed support. Requiring the remainder of the fixed connected S only reduces the count. Hilbert-space excitation indices are never enumerated: the construction uses projectors and operator norms. Hence one constant c independent of m, volume and time length is sufficient for the stated marked count. The connection to the actual paper's support expansion, rather than just nearest-neighbor raw insertions, is essential and valid after enlarging the fixed graph constant.

I recomputed both choices of convergence reserve. Native takes ordinary majorant epsilon^n exp(n/2), a=n/2, and q=ce epsilon<=1/4. Per-point sum<=1/3, so a root of size n0 sees at most n0/3<=n0/2. Its pinned factor is exp(n0/2). Including the marked root's reserve exp(n0/2) produces the sum epsilon^(-m) sum_(n0>=m)q^n0 <=(2ce)^m. Root instead takes reserve exp(n), a=n and q=ce²epsilon<=1/4, giving (2ce²)^m. Both are safe; their different C0 values are not conflicting physical constants.

A distinguished root need not have positive ordinary activity. For rigor one may append that single root with arbitrarily small positive auxiliary activity. The strict slack in the ordinary inequalities permits this for each fixed finite root; the root inequality has slack too. Apply KP, differentiate once and send its auxiliary activity to zero. Equivalently use the pinned tree bound directly. This supplies precisely one marked root, with its actual possibly-large weight outside the KP majorants. It does not assume a small marked observable or treat multiple independent marks as an unconstrained gas.

The reserves weight total polymer sizes with multiplicity, which dominate the spatial/time span of a connected cluster on the fixed graph. Thus clusters reaching a distant endpoint or wrapping a growing torus have exponentially small tails. For fixed local S this establishes the needed uniform-in-volume/time normal convergence, not merely pointwise finite-volume analyticity. The constants may grow exponentially with |S|, exactly as priced.

## Complex quotient, limit and holomorphy

The two finite-time semigroups must use the same complex parameter. Both proofs do this. Analytic inclusion–exclusion weights inherit uniform norm majorants from bounded complex perturbations; the classical free factors remain unchanged. For each finite space-time gas, its partition function equals the exponential of the normally convergent connected-cluster logarithm. This proves nonvanishing on the common disk; dividing is not justified solely by positivity on the real axis. Introducing I+lambda A and differentiating at lambda0 cancels the unmarked clusters and leaves one marked root. The activity sum is genuinely finite-volume exact before limits.

The weighted tail then gives the centered-time limit and, for a fixed interaction, the periodic thermodynamic limit locally uniformly on a smaller closed complex disk. On real small coupling, ground filtering with nonzero vacuum overlap identifies the limit with the normalized ground expectation. Near zero in any fixed finite volume, its time-limit function agrees with the analytic Riesz expectation; continuation concerns that limit function, not an equality between a finite-time sandwich and a ground projection. Read in this sense, the root paragraph is correct. No uniform complex spectral isolation of all excited levels is needed.

## Selection and conclusion

The separate edge-center argument supplies vanishing order at least area in open geometry and on projected tori under the half-area/nonwrapping condition. Finite-time Dyson selection or multivariate Riesz covariance are both legitimate; neither requires trace-class free resolvents. Uniform holomorphic convergence passes derivatives to the limit. The denominator has nonzero constant coefficient, so division cannot lower the numerator's vanishing order.

Applying higher-order Schwarz to the bounded normalized holomorphic function gives C0^P(|u|/u0)^A without an extra geometric-series factor. Since P<=4A, the stronger smallness condition stated by native indeed yields a pure exponentially decreasing area bound. Root's real-part loop and native's oriented complex loop are distinct stated observables, but the same center selection and norm argument apply to both. The periodic complement counterexample must remain: no unrestricted projected-torus area count is justified.

No blocking gap was found. The conclusion is a sufficiently-small-coupling upper bound for supplied spatial loops, with existential constants and a perimeter cost. It is not an arbitrary-coupling statement, positive lower bound, numerical string tension, temporal static-charge potential, spatial continuum theorem, physical confinement identification or axiom derivation. The explicit imported marked expansion is indispensable; finite Taylor selection alone would not establish this conclusion.
