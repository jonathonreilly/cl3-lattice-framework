# 7315-D focused original source review

NEEDS_FIX for #7202/#7203/#7204 (Blocks171–173). This is the final three-scope unit, not acceptance of all #7315. No science producer, audit, or repository mutation was performed.

The full original deltas contain 15 occurrences: twelve added science bodies and three distinct historical manifest states, with no deletions. The twelve science bodies equal the frozen successor. All notes, mathematical runner implementations and claim/gate logic, measurement outputs, and ledgers were examined; repeated N5 text was checked for exact identity and read once. Manifest deltas were inspected structurally. Necessary parent definitions reuse the same-session A/B/C body coverage only at independently matching bytes; source equivalence is not inherited theorem acceptance. The 43-script closure and five existing corrected main inputs are bound separately. Current authority is main07f0e842d7e283213c8f480b1380a6addae36d2b.

## D01: 173 stationarity existence, uniqueness, normalization

For column-stochastic M and probability P0, M mu=P0 already implies sum(mu)=1. After replacing it by E mu=0, E=M-P0 1^T, normalization is essential. Existence means P0 lies in the affine hull of the columns; equivalently ker(E) contains a vector with nonzero sum. Invertibility of M is sufficient, not necessary. M=P0 1^T gives E=0 and every probability vector is stationary although M is singular. Thus a cofactor routine returning None at rank(E)<3 does not establish nonexistence. State uniqueness loss at sigma=0, keep the normalized-kernel formula conditional on a normalizable kernel, and keep the raw inverse formula conditional on invertibility.

## D02: 173 positivity domain and boundary claims

Coordinate scans in steps of 1/40 followed by Boolean bisection do not locate a certified nearest zero: a narrow negative interval can be skipped, and solver failure is not distinguished from a zero of a component. Axis sections do not prove a bounded box in all dials; disconnected sections do not imply disconnected full positivity region. Retain exact positive/negative points and opposite-sign endpoint brackets. Withdraw global box, nearest-boundary, and full-region topology claims unless supported by a separate exact argument.

## D03: 171/173 probability extension and one-shot fork

A finite list of trails and extensions does not define kernels for every history/time and therefore does not supply a half-infinite process. Any positive finite Gibbs joint J(a,b)=w_ab/sum(w) factors as J_A(a) J(b|a). Failure of the particular ratio sum(w_extended)/w_empty to equal one does not disprove this factorization or a normalized finite joint. Different slot-order profile constructions are not a proof that Kolmogorov marginal consistency fails for a fixed joint. Retain the finite normalized kernels and measured discrepancy between the two specified recipes; state infinite extension as conditional on kernels for every history. Correct the lingering same-slice order claim when the witness uses different levels.

## D04: 172 primitive defect and ladder interpretation

The conjunction defect is negative because the measured weights satisfy w(S)<sum_c w(c), not because normalization forces that inequality. Positive weights 3 versus 1+1 give the opposite sign with a common positive denominator. A reported bracket 1/(N+1) certifies 1/(N+1)<abs(delta)<=1/N, not delta=1/N. The primitive_is_alphabet_reciprocal test only checks the bracket integer. Likewise the base variation calculation compares bracket integers, not exact defect ratios; nonzero variation cannot support distance alone/nothing else. Keep exact bracket bounds and measured dependence; remove exact reciprocal and base-invariance claims.

## D05: 172 general density and complex phase construction

Hermitian positive diagonal does not imply a positive semidefinite density: [[1,2],[2,1]] is a counterexample. Require PSD and positive trace. With the implemented v_i=3/5 and v_j=4 phi/5, trace(rho vv†) has off-diagonal contribution (12/25)(phi rho_ij+conj(phi)rho_ji). Lines879–880 reverse the phases. phi=i and rho_ij=i/4 give true -6/25 versus the printed +6/25. Real phi=1 masks this seam. Correct the general formula or vector convention and retain the tested fixture separately.

## D06: 173 iteration and ladder laws

Five iteration steps do not prove geometric convergence to the Perron vector. Give a primitive/positive stochastic-matrix argument for the actual domain, or report only the finite iterates. The non-limit claim for mu* can instead follow from M mu*=P0 != mu*: a convergent iteration limit must be fixed. Changing characteristic-polynomial coefficients does not by itself rule out a geometric law for a particular scalar observable. The vector identity defect=E(mu-mu*) is valid, but not an equality of the corresponding maximum norms. Restrict the scalar-law claim to what exact observed ratios or bracket intervals exclude.

## D07: 172/173 unsupported symbolic and census scope

The preserved baseline caches run with --deep false. They do not certify the full merge census or the 8x4 all-shear symbolic leg. Block173 baseline evaluates the mass symbolic leg; the advertised sigma and g_re symbolic forms are not supplied by the corresponding code path, and denominator degrees are not established by numerator-degree checks. Equality at selected plus/minus 2/5 points does not prove a 12x4 parity law. Keep actual finite observations and label missing symbolic/count obligations explicitly. Mu* also uses all extension profiles as well as P0; being nonuniform when P0 is uniform is not information finer than its complete input.

## D08: 171 battery and inherited closure rhetoric

The finite ten-member battery, supplied carriers, and farthest tested record do not establish full history memory or a universal generator classification. The 12x4 deep set must not be silently applied to 8x4, where near and far supports coincide. Correct the W1 SCiii prose/cache discrepancy and distinguish the 1/5 stress probe from the declared alphabet trails. Prior Blocks167–170 remain subject to review-C findings; their quadruple-audited/closed route language cannot be adopted as authority. None of these finite tests seals every theorem-shaped door or forces an axiom route. Retain the conditional matrix construction and explicitly tested failures.

## D09: Missing executable input and incomplete evidence closure

Block172 executes .claude/science/physics-loops/generator-program-20260821/b171_profile_table_v2.py in banner_probe. It is absent at all three original heads and the frozen successor. The five declared inputs omit it, the necessary transitive code closure, and ledger; importing a parent does not execute or inherit its authority gate. Block173 audit_source_paths inspects at most itself plus171/172, not every code file in the 43-file import closure. Recover the exact table or replace it with an explicitly reviewed finite construction, bind actual inputs and current authorities, and obtain authorized fresh evidence only after static cost preflight. Preserve historical caches as historical rather than current acceptance.

## D10: Scope-key mutation evidence

The drop_n5/owner/caution mutations delete required scope keys. Gate H checks all remaining values without checking equality to the required key set, so deletion can leave H passing; the later mutation assertion fails because its expected rejection did not happen. That assertion is not the promised missing-text rejection. Check required-key completeness or mutate actual note input and verify the intended gate rejects it. Boolean claim mutations remain harness controls, not independent mathematical counterexamples.

## Retained construction and independent checks

The congruence identity H(Q^-1)=Q^-1 H(Q) Q^-† is valid; positive H(Q) makes Q invertible. Direct-sum functional closure is valid with record-independent coefficients and defined inverses. These give conditional finite matrix results, not a physical measure or an adopted carrier. A length-two four-letter frequency census necessarily has ten multisets and six doubled pairs; differing weights within such pairs demonstrate loss under the frequency map for those fixtures. Trace additivity over orthogonal projector sums is linearity and supplies no extra bridge premise.

The independent checks above were manual derivations and decisive counterexamples, not reruns of the parent code. They include the affine-hull/normalization calculation, the singular stochastic matrix example, Gibbs factorization, the complex-phase calculation, and the interval interpretation. These separate consequential mathematical errors from unreviewed inherited authority. No attempt was made to certify every parent's independent scientific claim.

## Disposition and remaining work

Preserve every original body, including all three manifest versions. Correct the affected note, primary, ledger, and repeated cache rhetoric together. Retain only finite or explicitly conditional results, withdraw the listed stronger quantifiers and physical/axiom conclusions, and regenerate current topology after correction. Historical baseline PASS totals do not discharge the missing input or deep obligations. A bounded replacement can retain the supplied finite construction without importing the absent historical theorem chain. Fresh evidence needs a separately approved cost/input plan; no full original runner is authorized by this review.

SOURCE_BINDINGS.json records every original head/base/path and both original and successor hashes; dispositions.json covers every occurrence. INPUT_CLOSURE_BINDINGS.json and AUTHORITY_BINDINGS.json preserve exact reused input identities. The earlier checkpoint remains historical and is superseded by this completed report.
