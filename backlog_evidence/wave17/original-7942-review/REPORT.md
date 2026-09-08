# Independent original review of #7942

**FINAL VERDICT: FINDINGS — narrow correction required; no complete source PASS.**

Reviewed original head `4886ac719d2dda0325134fac87f4e790713346ee`, actual base/merge-base `a950a1aacfb33c10699dc88ac2f441d7024ad109`, over current main `eed3c68fffdd8f912a6a4b4bc2e0098184fb3b2b`. The complete original delta is three additions, with no deletions: one 321-line note, one 1,250-line standalone Python/embedded-C runner and one 35-line historical cache. All three bodies were read in full. They remain byte-exact in the isolated review worktree. This is independent source review, not a formal claim audit or a new physical grade.

The useful core survives: independent meet-in-the-middle enumeration gives all 9,600 Gauss states; independent directed transitions give 937 components with the original complete size multiset; independent cycle reduction gives rank10; all 9,600 eigenvalues computed through the complete 937 block decomposition reproduce the quoted full and internal gaps. A replayed odd-parity closed walk confirms the restricted pair update's obstruction. The source's current wider conclusions and passing checks need the repairs below.

## Findings and narrow repair targets

`N` and `R` refer to the canonical original note and runner, whose complete paths/hashes appear in `ORIGINAL_SOURCE_MAP.json`. Anchors are original one-based source lines. `FINDINGS.json` contains machine-readable locations.

### F1 — P2: Required compiler/engine failures become successful full-unit evidence

R1023–1028,1074–1090,1112–1114,1169–1172,1211–1212,1249–1250; N289,300,321. Actual `CC=/usr/bin/false` and a separate real embedded-C `return29` mutant both produce **16 PASS,0 FAIL,5 SKIP, exit0**, with actual `runner_cache` status **fresh**. These are failed required witness executions, not complete validation of T3/T4. `FAILURE_CONTROLS.json` binds full outputs, commands and cache identities.

Keep the original21 IDs and mathematical results, but required compiler absence, compilation failure, engine failure, missing/malformed diagnostics and timeout must leave a nonzero runner exit and unusable successful-evidence cache. A partial exact-only run may be reported separately. Preserve these original failure receipts.

### F2 — P2: Claimed complete Gauss and run-wide invariant checks are incomplete

R775–784 checks roughly400 strided states plus64, while N124,132–135 and A1 claim every state. Mutating untested state65 by one link bit yields actual Gauss residual2 and the **actual original A1 still PASSes**. The original unmutated basis is correct: the independent full residual sweep verifies it.

The C engine never evaluates Gauss equations; R313–314 prints warmup errors but R353 resets them, and R1052–1057 consumes only the final line. A wrong-Gauss initial geometry with residual2 returns `closure_err=0`, `illegal=0`, `GE0=.25`; actual D4 accepts it. A real source mutant reports warmup `illegal=1`, then terminal `illegal=0`, which the real API accepts. See `INDEPENDENT_CONTROLS.json`, `ENGINE_CONTROLS.json`, `engine-control-raw/`.

Check all basis states/vertices, and check actual initialized, updated/rotated/replayed and terminal C states against the declared torus/ladder equations at a stated bounded cadence, with positive state/equation counts independent of dump flags. Keep cumulative errors across equilibration and production, and make the API fail on an actual violation. Do not present closure alone as a Gauss or full-code certificate.

### F3 — P2: Equal-time normalization does not certify the imaginary-time map

N174–181,238–241,300; R417–432,1159–1167. `GE(0)=1/4` follows from squaring the stored ±1 spin whenever sampled; it does not test the time spacing or positive-lag indexing. A real C mutant changes only `double v=u+taus[i]` to `double v=u`; it collapses every lag to zero, but original D4 still PASSes with .25 and zero error counters.

Retain the equal-time identity as that identity. Either add a genuine independent positive-lag/order-statistic reference that rejects this mutant, or narrow the claim to the finite equal-time check and describe the unvalidated map explicitly. The Dirichlet-spacing construction itself has a standard elementary derivation; its software implementation needs a discriminating control before code-correctness language.

### F4 — P2: Winding classes, connected components and observable gaps are different objects

N title/122–130,185–198,208–210,258–259; R2–3,819–825,853–860,1013–1016,1214–1222. There are **125 winding classes**, not937: zero winding alone contains the864-state component plus16 frozen singletons. Original component projection does not itself establish winding. Independent explicit cut-flux labels do confirm that the six full first-excitation components have winding `(±2,0,0)` and permutations, so retain that useful conclusion with its actual check.

The universal claim that any winding-conserving sampler reads2.2257853859 is false. In the same864-state component, a local `E_e` does couple to that first level, but `E_y(k=(pi,0,0))` has weight below3e-30 there and first couples at **2.5172790443**. A conserved/constant observable need not give a decay gap at all. See `SPECTRAL_CONTROLS.json`, `ALL_COMPONENT_SPECTRA.json`, `CONTEXT_CONTROLS.json`.

Use “plaquette-flip connected components” for937. Define and check winding separately. Carry reached component/ensemble, observable overlap, projection/temperature and estimator assumptions with any inferred rate. Keep the two exact finite spectral gaps; do not assign one universally to every sampler or observable.

### F5 — P2: Algebraic parity index is not thermal mass or an exclusive diagnosis of bias

N25–27,150–162,211–213,220–223,238–241,300,314–319; R932–939,1135–1156. Rank10/index1024 is correct. It does not give the Gibbs-weight fraction of omitted histories, prove that “almost everything” is lost, prove complete mixing in the remaining subset or exclude implementation/equilibration error. A C-scan at one seed and zero closure/illegal counters cannot supply those missing results.

The unchanged finite graph has rank10 at all beta, but at beta=.0001 positivity and `||H||<=24` imply the even-parity thermal mass is at least `exp(-24 beta)=.9976028777`, already near1. Thus algebraic index cannot be read as a1/1024 weighted fraction or a general dominance claim. The original beta8 discrepancy remains an actual, reproducible witness; it is not disproved.

Retain the exact obstruction and the original stochastic numbers/standardized bin residuals. Narrow the causal/weighted/mixing wording unless a separately bound weighted-ensemble or detailed-balance/ergodicity analysis actually establishes it. Do not imply the40 bins, common seed or C agreement calibrate all uncertainties, finite-M error, autocorrelation or equilibration.

### F6 — P2: The geometric cube factor and short timing do not prove sampler necessity or phase cost

N187–202,214–218,255–257,285; R1185–1196,1204–1209,1246. `(lambda/C)^6 N_s/binom(N_p,6)` is a geometric selection factor times a putative matrix-element ratio, not the asserted state-independent acceptance probability: all720 orderings of the first actual cube's six faces are illegal from the analytic ice state. The XOR relation alone says nothing about the intermediate flippability constraints. The actual state trace of a different **four-face** odd-parity closed walk is also preserved (`ADDITIONAL_CONTROLS.json`).

A loop/cluster/worm is a possible correction to this closed-string representation, not a theorem about all correct three-dimensional sampling. The current corrected #7959 free-end formulation is a concrete representation alternative; this review does not reapprove its complete campaign. The short4^3 sweep measurement reports operation cost for this restricted sampler, not mixing time, error-controlled phase resolution or the performance of an unwritten algorithm. Fixed `beta~L` assumes a spectral scale that this note does not establish; slower gaps can require different growth.

Preserve both geometric numbers and measured timing under their correct definitions. Mark proposed alternatives and unmeasured costs as open. Remove “would be right,” “needs exactly,” “compute is not the obstacle,” “day or two” and phase-settling forecasts unless independently supported. No new production campaign or new physics is needed for that correction.

### F7 — P2: Fixed records do not supply off-diagonal readout through correlations

N85–89,296–298. Supplied link Z content can define E within the designed readout; this does not establish a physical role placement or derive quantum equilibrium sampling from Record. More specifically, fixed-Z record correlations do not determine `U` or `P` expectations. The actual legal configurations166 and2196 connected by plaquette5 yield normalized ± superpositions with identical full Z-record probability distributions and `P_5` expectations±1. (`INDEPENDENT_CONTROLS.json`, `ADDITIONAL_CONTROLS.json`.)

Retain the finite supplied quantum-link model and the diagonal readout identification as conditional. State that off-diagonal expectations need an additional supplied measurement/readout protocol; imaginary-time updates are an auxiliary mathematical sampler, not rewriting permanent records. The current axiom quotation is accurate and unchanged; there is no premise-epoch replacement to request.

### F8 — P2: The historical L20 value is promoted to a thermodynamic limit

N4,168,281; R991–996, original cache C2 (also N4). Current corrected #7911 states `.6035607` as the rounded **L20** value and treats all finite-window fits as diagnostics; it does not prove the limit. #7942 repeats it as an `L->infinity` value. Keep the `.6038698340` L8 value and `.6035607` historical comparison with its actual finite provenance. Correct the associated unit wording: energy density is `E0/L=-.6038698340 lambda`, while total energy is that value timesL.

### F9 — P2: The cache does not bind its note or quoted current premise

R70–78 has no `AUDIT_INPUT_PATHS`; original and fresh caches pin only the runner. Actual independent note and axiom-memo drift both leave `cache_status=fresh`. All runtime mathematical definitions are truly standalone, so no transitive science helper needs importing. Both actual note-derived consumers return the correct primary and no helpers; the source guard accepts the undeclared-input state. See `CONTEXT_CONTROLS.json`.

Before a corrected final cache run, bind the canonical note and any current quoted/reviewed premise used by the correction to literal input declarations and actual source checks as appropriate. Keep current context historical/non-load-bearing where that is the true role; do not enroll entire parents to obtain pins. Verify the filename-derived ID/primary with both consumers. Add real source/input drift rejection. Preserve the original historical cache separately rather than restamping it.

### F10 — P2: The negative-claim packet and trace need honest scope

The source publishes a bounded obstruction and stronger universal tooling negatives but has no N1–N8 gate or real N5 resolution certificate. R1230–1235 counts a literal `True` scope statement as an “exact” test. N41 directs an immediate formal audit, inconsistent with this campaign's current deferred-audit direction.

Provide an honest source-side N1–N8/resolution record for the narrowed pair-update obstruction, distinguish actually executed routes from proposals and source-context alternatives, and disclose any unmet mechanical five-family requirement instead of manufacturing routes. Do not label independent finite checks as independent physical walls. Treat E4 as a scope declaration, not a mathematical identity proved by `True`. Leave audit status unset and the formal audit deferred.

## Reproduction and preservation

The one unchanged baseline uses actual current-main `runner_cache.execute_and_write_cache` in an external exact snapshot,150-second total cap,165-second outer process-group watchdog and single-thread numerical libraries. It returned **21/0 in22.025224 seconds**, identity unchanged, statusok. `BASELINE_EXECUTION.json` and `baseline-output/IDENTITY.json` bind command, tools, runtime and source. The observer only records child subprocess results, copies files before original cleanup and saves already-computed arrays at process exit; it neither alters source, random draws, mathematical functions, seeds, sampling lengths nor thresholds. No baseline rerun.

All9 actual numeric bin tables, three geometries, generated C, binary, full child stderr/stdout, original cache and fresh baseline cache are preserved. `ADDITIONAL_CONTROLS.json` independently re-evaluates every bin table. The original beta8 energy/standard error reproduce `-8.11846/.0067029378366`; only measured timing and harmless floating details can depend on the environment. Preserve these artifacts for exact reuse when corrections leave their actual inputs/algorithm unchanged; a final cache still requires the genuine final source/input identity.

Focused controls include complete independent Gauss enumeration, graph and spectra; the actual missed-state gate; four tiny C/API experiments; actual compiler and engine failure paths; two input-drift paths; a true odd-parity state trace; equal-record/opposite-operator states; and observable-specific spectral projections. Tiny C commands were repeated only to retain full raw streams discarded by the original API, in a separate directory. No larger parent campaign or full gate ran.

Two independent-review expectations were rejected and preserved: the analytic ice state did not admit the initially presumed cube ordering (zero of720, now useful evidence); the local E_e did not have the transverse-mode gap (it couples to the internal first level, while the explicit transverse Fourier observable supplies the intended counterexample). A suspected ladder spatial-array path was disproved by reading the actual `pos=None` writer before any baseline. These are not source findings. See `PROOF_REVIEW.md` for limits and scope.

`FULL_SOURCE_MAP.json` has29,985 actual mode/blob/path rows. All28,696 current-main paths are unchanged; only the three original additions are present in the private worktree. All original branch inheritance is mapped and excluded from this standalone unit, not accepted or silently restored. The original local and remote tracking branch both point to4886ac719d2dda0325134fac87f4e790713346ee. No branch was overwritten. No formal audit, GitHub action, commit, push or shared-planning mutation occurred.

The same reviewer session remains available to confirm a narrow author correction on the final composed source/input/manifest scope. The original finite results, failed witnesses and conditional boundaries must all remain recoverable.
