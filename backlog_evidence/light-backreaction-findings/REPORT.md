# Light-backreaction independent source review

**Source verdict: HOLD for seven narrow corrections.** The six conditional theorem families contain useful coherent mathematics. Preserve all eighteen original source paths and correct the claims and evidence below; no closure, axiom addition, audit verdict or whole-unit restart is warranted.

Reviewed source: exactly the eighteen `light_backreaction` paths in `SOURCE_PREPARATION.json`, extracted from frozen #7937 head `2814c6768e4d7b38048f70ad7883b4951cb12da3`. The isolated worktree is `/Users/jonreilly/Projects/Physics-worktrees/review-backlog-light-backreaction-20260907`, detached at corrected light parent commit `16c2d6860e168ec8e5e8f66296410265e5d7226d`, with only those eighteen untracked source additions. No raw uncorrected parent, generated audit output, ice remainder, reserved PR science or other raw branch source was imported. This reviewer read every line of all six notes, six runners and six caches. The eight actually imported parent helpers are bound to the already reviewed corrected parent; all 47 parent hashes match that session's PASS. The current-main workflow and relevant premise sources match the prior full authority reads; applicability was checked before reuse.

All six complete original base-to-head deltas were independently checked by Git mode/blob/path data: each consists of its three source additions plus the historical generated manifest. Their complete nongenerated union is exactly eighteen paths, each original blob identical at raw #7937. No deletion or inherited source is omitted. Live metadata now reports all six constituents (#7922/#7923/#7924/#7927/#7930/#7932) CLOSED with unchanged heads, while #7937 remains OPEN, ready and unchanged. These are original provenance packets carried by #7937, not six asserted live landing PRs. The first metadata assertion expected open constituents and therefore failed; the recorded complete rerun preserves their actual states. No changed head was hidden. Review base remains explicit; root owns current-main integration checks.

## Findings

### F1 — P1: Make the finite-clock charged Gauss convention and sector match the claimed additive law

`docs/U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:213` states `X=exp(+i dA E)`. Together with its displayed matter factors `omega^n` and Gauss generators (lines 180–195), this gives `G_v=exp[i dA(div E+rho)_v]`. It does not give the result claimed at line 82, `div E=rho`, or the upstream convention `div E-rho`.

An independent K=9 Fourier-basis example has no wrap: the displayed forward hop `Z tensor |head><tail|` sends electric mode 0 to -1 while the head number rises from 0 to 1. Thus `Delta E=-1`, `Delta n_head=+1`. The earlier source and hard-cutoff interface require equal signs. The runner's no-wrap test (lines 618–650) checks only charge-free integer divergence modulo 32 and cannot detect this mismatch.

Minimal repair: adopt and consistently derive an oriented electric convention, for example `X=exp(-i dA E)`, which leaves the cosine Hamiltonian and exact Weyl generators intact and restores the parent's current orientation. State the Gauss-sector eigenvalues/background explicitly: on a one-charge closed face, the product of the displayed generators is `omega I`, so all generators cannot simultaneously have eigenvalue 1. Distinguish conservation of a chosen sector from imposing the neutral constraint. Express the charged no-wrap bound on the full constraint residual including matter and sector/background labels, and add an actual nonzero-charge Fourier-basis transition/sector control with the corrected sign. Do not assign a globally additive current across a modular wrap.

Evidence: `INDEPENDENT_CHECKS.json`, `clock_charged_sign_counterexample`. This correction reopens the clock's charged/additive bridge and dependent rhetoric, not the already valid Weyl commutators or bond energy identities.

### F2 — P1: Fixed-coupling clock refinement does not converge to the exact harmonic photon gap

The clock note at lines 102–104 and 311–317, and its runner's check 22 at lines 751–767, claim the exact reduced gaps converge to `sqrt(lambda)` as K increases with fixed `g=0.06`. The K→infinity model at fixed g is instead the periodic cosine rotor

`H_rotor=-(g^2/2)d^2/dA^2 + lambda/g^2 (1-cos A)`.

Its anharmonicity survives K refinement. Independent Fourier tridiagonal solves, checked at electric cutoffs 100/200/300, give limiting gaps 0.764916599742, 0.389730123464 and 0.195583241400 for L=8,16,32. Their discrepancies from the respective harmonic frequencies are 0.05882996%, 0.11546461% and 0.23008183%. Independent finite-K Fourier windows reproduce the author's K=1024 gaps and approach these rotor values through K=8192. They do not approach the asserted harmonic target. The perturbative mechanism is explicit: the quartic potential shifts the first gap by `-g^2/8` to leading order.

Minimal repair: retain the actual finite-K discrepancy ladder, but label it as improvement toward the fixed-g cosine-rotor gap, with a remaining anharmonic discrepancy from the harmonic comparison. Either leave exact harmonic convergence open or state and substantiate a separate small-g/joint limit. At fixed positive lambda, angular tameness requires `g^2/sqrt(lambda)` small, while angular-grid resolution requires `2pi/K << g/lambda^(1/4)`; K alone does not supply both limits. Add a fixed-g rotor-floor control and, if claimed, a distinct small-g control. Also state that the reduced oscillator is a supplied comparison model, not an exact invariant Fourier sector or derived spectral reduction of the interacting many-link clock. The existing many-link-phase caveat should remain.

Evidence: `INDEPENDENT_CHECKS.json`, `fixed_g_clock_gap_counterexample` and `analytic_anharmonic_gap_shift`. This does not reject the formal quadratic Maxwell kernel, finite-clock Hamiltonian or useful sub-percent comparison.

### F3 — P2: Test the actual nonzero-current update, not only a separate continuity calculation

`scripts/u1_conserved_source_coulomb_photon_bridge_2026_09_03.py:60` implements the live source insertion. Replacing `+ step * current` by `+ 2.0 * step * current` still produces byte-identical `TOTAL: PASS=17 FAIL=0` output. Its integer continuity calculation is separate from the actual function; its actual source-free reduction uses J=0, and support/covariance tests do not determine the source amplitude.

For the one-edge unit transfer, the mutated function gives electric divergence (-2,+2) while the charge update is (-1,+1), a maximum Gauss residual of 1. The claimed source coefficient and live charged Gauss law therefore lack direct runner coverage.

Minimal repair: execute the actual sourced tick with nonzero field/current and compare it to independently constructed rational full-field numerators, the actual charge continuity update, both magnetic constraints and the one-edge coefficient. Include an adverse source-coefficient control. Preserve the algebraic proof; do not merely assert the implementation's own output as its expected value.

Evidence: `MUTATIONS.json`, case `source_coefficient`; `SOURCE_COEFFICIENT_COUNTEREXAMPLE.json`; actual stdout logs in `mutants/source_coefficient/`.

### F4 — P2: Pin all actual transitive helper inputs and refresh affected receipts

The source runner's declaration at line 30 omits a direct imported helper as well as downstream imports. The radiation declaration at line 39 and finite-current declaration at line 26 omit further actual transitive helpers. `INPUT_CLOSURE.json` records the exact missing sets (seven, six and six respectively). The three other new runners have no actual local imports; their declared explanatory contexts must still be preserved honestly.

Using the actual unchanged current-main `runner_cache.py`, SHA-256 `1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2`, I wrote a cache for a fresh successful source run in scratch, then changed its omitted `curl_symbol` helper to `C+I`. The cache remained `fresh` with identical runner/input identities, while the live runner exited 1 with failed source-projector and cubic-covariance checks. This is actual cache behavior, not a token-based warning.

Minimal repair: pin the complete actual local import closure for every new runner, retaining any additional declared premise/context dependencies needed for source provenance. Refresh caches on the final corrected-parent context and reject a changed helper with `input_mismatch`. A conservative declaration closure is acceptable; it must not replace the independent actual-input inspection or smuggle unreviewed science. Four original caches already report `input_mismatch` on the corrected parent; the two standalone quantum caches report `fresh`. No old cache result grants a final corrected-source receipt.

Evidence: `INPUT_CLOSURE.json`, `CACHE_COUNTEREXAMPLE.json`, `ORIGINAL_CACHE_STATES.json`, `cache-counterexample/`.

### F5 — P2: Supply the current author-source records and timeout declarations

All six notes begin with a `Status authority` disclaimer at line 7 but omit the required enum-valid author source status and structured premise/trace record. A disclaimer about independent audit authority is not that record. All six runners omit `AUDIT_TIMEOUT_SEC`, although every cache specifies 120 seconds. The mathematical predicates are supplied conditional models, not current audited statuses.

Minimal repair: add honest current author source status, full conditional trace/import/parent-boundary records, and the source timeout on all six runners. Preserve the supplied Hamiltonians, coefficients, one-particle sectors, weak-field restrictions, finite block/schedule domains, compiler gaps and empirical non-identifications. Do not write or imply an applied audit verdict. Update final receipts after the source declarations change.

### F6 — P2: Correct the N1 evidence maps and unsupported N2 independence assertions

The conserved-source note's N1/Gate result (lines 377–389 and 493) and radiation note's N1/Gate result (lines 439–450 and 550) explicitly supply only four attempted families, below the current five-family gate, while declaring PASS. Some cited check-number groupings also do not match the named controls. This is a submission defect, not a mathematical impossibility or a reason to discard the positive lemmas. Use actual distinct proof/control families with exact evidence; do not invent attempts to meet a count.

All six N2 tables (source line 390, radiation 452, finite-current 421, hard-cutoff 474, plaquette 360, clock 423) mark every pair independent. Their few illustrative one-way non-implications or empty yes/no tables do not establish both logical directions for every stated pair. The useful clock phase/tameness collapse may remain, but the remaining pair relations are not automatically proved independent.

Minimal repair: map the actual same-unit proof/runner families accurately and keep unproved implication relations explicitly unresolved. Do not infer independent wall counts or stronger exclusions. The positive unsplit, higher-order, Floquet, collision/clock and finite-payload alternatives should remain visible; none is disproved by a failed particular schedule.

### F7 — P2: Label the plaquette's continuous-phase Hessian as a separate comparison construction

`docs/U1_QUANTUM_LINK_MATTER_MAGNETIC_PLAQUETTE_FINITE_STEP_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md:80` says “the same face has Wilson potential,” followed at line 245 by a continuous-phase Taylor expansion. Its actual finite spin-one links are hard-cutoff nilpotent shifts (`U^3=0`), not unitary phase eigenvalues `exp(iA)`. The runner's final three checks construct `kappa b b^T` and `kappa(1-cos(b dot A))` separately; they do not derive that scalar potential or Hessian from the finite 162-state quantum-link Hamiltonian.

The classical Taylor identity is correct, and the source already correctly declines an extended quantum-link photon claim. The remaining local link between these distinct constructions must also be explicit.

Minimal repair: label the continuous U(1) phase/rotor face as a separately supplied comparison and specify the operator-to-phase replacement. Do not call its Hessian an established tangent of the finite hard-cutoff quantum face or say that the finite quantum calculation proved the local curvature match. Preserve the exact finite-face Gauss/work/Floquet result and the conditional scalar Hessian lemma separately, with the missing state/symbol/limit bridge open. No new spectral calculation is required for this narrowing.

## Optional precise coverage improvements

- Clock note line 313 reports final angle second moments below 0.01, while runner line 749 accepts values below 0.12 and does not print the actual moments. Match the assertion to the reported bound or report the actual moment values with an accurately labeled weaker check.
- The conserved-source coefficient fits are four named numerical samples. Keep the note's existing numerical qualification in N3 and make the runner's “converges monotonically” label say “errors decrease across the named ladder”; no asymptotic theorem follows from four fits alone. The exact Poisson and minimization arguments remain valid.

## Full-unit scientific coverage

| Packet | Independently checked surviving argument and its boundary |
|---|---|
| conserved source / #7922 | `C d0=d2 C=0` gives signed continuity and both Gauss constraints; unique neutral minimum follows by full-kernel orthogonality, including harmonics. Fourier inverse, finite-size fits, longitudinal/coexact/harmonic split, nonzero-momentum polarization, polar/axial cubic symmetry and finite-layer support read and freshly executed. Coulomb asymptotic interpretation stays numerically bounded unless separately proved. F3/F4/F5/F6 apply. |
| midpoint work / #7923 | The metric/source coefficient identities imply exact midpoint work for arbitrary old fields/current; the delayed opposite pulses give the displayed curl/co-curl residual, no charge or harmonic field, rational half-unit energy at the tested step, reversed-history recovery and bounded sparse propagation. Positivity and propagating interpretation inherit the parent's CFL domain; the exact algebra alone holds more generally. Raw-amplitude location is correctly distinguished from a local conserved energy density. F4/F5/F6 apply. |
| finite current / #7924 | Exact one-particle bond conjugation gives the stated finite current, endpoint/midpoint error orders, phase covariance and orientation. Prefix pullbacks account for overlapping-layer continuity; operational two-site support does not imply initial-frame support. Symmetric numeric metric algebra gives anticommutator work for noncommuting fields; no joint quantum field dynamics is inferred from merely adding source operators. F4/F5/F6 apply. |
| finite-link backreaction / #7927 | Hard-cutoff `[E,U]=U`, paired transfer sectors and two dark states support full finite-block Gauss and same-sign current. Conjugation and the operator difference-of-squares identity give exact active electric/hopping exchange. Adjacent terms preserve Gauss but need not preserve inactive/summed energy under splitting; disjoint control is valid. Principal Floquet energy is a finite-block branch statement, with no global locality or physical-energy selection. F5/F6 apply. |
| quantum face / #7930 | Charged transport and signed loop shifts preserve the same four Gauss generators. Their exact full-flow flux decomposition and active-layer work are sound; full H is conserved only by the unsplit flow. I independently derived the Strang BCH coefficient as a formal noncommutative series, confirming its sign and factor. Correlated entries and both removal controls were freshly executed. Scalar phase curvature needs F7's separate comparison boundary. F5/F6 also apply. |
| finite clock / #7932 | Exact Weyl/cyclic algebra, binary register action, modular Gauss commutators, component exchange, finite face exponential, scalar Taylor bounds and conditional quadratic kernel are useful. The complex forward-difference kernel has one gauge null vector and two positive eigenvalues; independent staggered phase maps verify full cubic covariance. The physical register compiler and full many-link tame phase remain open. F1/F2/F5/F6 apply. |

The proof/import lens finds supplied laws throughout: no matter species, fermion statistics beyond the stated one-particle matrices, electromagnetic charge/coupling, unique schedule, common gauge/matter speed, many-body Coulomb phase or Record outcome follows from the four axioms. Reciprocal coefficients select the unit-speed example; the matter kinetic primitive does not select those coefficients. The scale primitive supplies a ruler and no dimensionless empirical identification. No open matter/ice PR is used as theorem authority; their references are contextual only. Full historical/raw #7937 science remains outside this unit.

## Actual execution and independent evidence

All six original runners freshly exit zero with empty stderr, totaling **133 passing checks** (17+22+23+24+23+24), from the external frozen source with corrected parent inputs. These are runner checks, not 133 independent proofs. All six sources compile. Vocabulary lint has zero violations. All three ordinary diff checks pass; because the candidate overlay is untracked, eighteen additional no-index checks inspect its actual added bytes with the repository's whitespace attributes and report no warnings. An initial absolute-path check from the wrong working directory failed to apply the cache whitespace attribute; the recorded relative-path checks use the correct repository context. No full pipeline was run.

`INDEPENDENT_CHECKS.json` records separate derivation paths: exact rational rectangular/noncommuting work algebra at h=2/7; generic closed-pulse algebra; whole-kernel Poisson minimization on a separately built square; eight bond-current expm comparisons including negative step; four explicit two-state flux-pair work calculations; a noncommutative word-series BCH derivation; all 48 staggered complex-symbol covariance maps; the charged clock sign counterexample; and independent Fourier-space fixed-g rotor/finite-K gap controls. The finite-K Fourier windows are independently truncated comparison solves with resolved cutoff checks, not claimed certified full finite-K diagonalizations. Their K=1024 gaps agree with the author's actual full K-state solves, and the analytic anharmonic term identifies the limiting error mechanism.

Six actual implementation mutations were executed in isolated scratch. Five are rejected by named failed checks: midpoint work coefficient, finite-current Z correction, hard-cutoff wrap, BCH sign and clock Weyl orientation. The source-coefficient mutation survives and is F3. The additional actual cache mutation is F4. `MUTATIONS.json`, `CACHE_COUNTEREXAMPLE.json`, `FRESH_RUNS.json` and corresponding complete stdout/stderr logs preserve the evidence.

The non-load-bearing prior-art references were checked against primary sources: [Radičević's gauge-theory paper](https://arxiv.org/html/2105.12751v2) explicitly conditions its tame construction and has d−1 harmonic modes in that restricted theory; this supplies no missing proof for the present fixed-g comparison or many-link phase. [Kogut–Susskind](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.395), [QCA Theory of Light](https://arxiv.org/abs/1407.6928) and [the QCA field-theory overview](https://arxiv.org/abs/1601.04832) support only the stated prior-art classification. Their abstracts and the relevant Radičević tame/mode sections were inspected; no complete reading of those long external papers is claimed or used as imported scientific authority.

## Repair and same-session confirmation

The original eighteen-path snapshot, corrected parent scope and findings are now frozen externally. It is safe for the assigned author to edit the isolated light-backreaction candidate. Keep repairs inside the eighteen paths plus narrowly necessary input declarations or correction witnesses, preserving the corrected parent bytes and all original conditional content. In particular, do not replace the entire raw branch or import ice/matter science to patch a local boundary.

Return an exact correction patch, complete original-to-final eighteen-path disposition/hash inventory, declared/actual input closure, fresh affected runner receipts and adverse controls to this same reviewer session. I will inspect every correction and its affected conclusion/dependent closure; unchanged reviewed arguments need not restart. Final source PASS remains withheld until those changes are confirmed. Root alone owns current-main compatibility, combined exact-base/tree validation, commit/landing and GitHub disposition. No audit or status application is authorized by this review.
