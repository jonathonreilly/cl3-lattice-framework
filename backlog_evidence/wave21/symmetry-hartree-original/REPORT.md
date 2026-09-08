# Original #7894/#7897 independent source review

Verdict: **CHANGES REQUIRED** — 11 P2 groups and one P3 label correction. The useful finite conditional constructions remain reviewable; this is not a rejection of them or a claim-audit verdict.

Frozen review base `d81f3c22117522411c20fb6c38eef5874c4765ae`; exact selected six-path tree `6de15dc67588dd65deb6df2ec293395f847fe792`. Both source heads, modes and SHA-256s are in SOURCE_SELECTION.json. Both actual parents are `36fe57a7a784df31bc2178c4b94dfc7caaa5d094`. Read-only live captures match both open/non-draft frozen heads. #7897's later live base is metadata, not its authored parent. Current-main merge-base searches return 1 (unknown visible ancestry), never an empty-delta inference. Actual parent-to-head deltas are three additions each, no deletion.

I read the full original two notes, two runners and two caches, complete selected PR bodies, exact planning target scope, current minimal memo/registry context, and all locally used computational definitions. No local helper/imported science code exists in either runtime. The finite objects are redeclared locally; historical parent realization, Born/readout and continuum claims are not accepted through their names. No reserved science is imported or required to establish the bounded controls.

The 30,088-row full map binds both raw heads, actual parent, current main and selected tree. All 28,796 current-main leaves remain exact; 1,286 raw-only inherited paths are excluded. Original paths/blobs and historical caches remain recoverable from frozen heads and exact external copies. No original science path was edited. Wave20 was not silently imported into this frozen d81 review.

## Actual execution and independent evidence

Each original runner executed once through actual runner_cache with pre/post source identity and external cache/live destinations: #7894 **33/0 in 1.912 s**, cap 90 s; #7897 **23/0 in 9.151 s**, cap 120 s. Wrapper elapsed 2.173/9.299 s; observed peak RSS 102,736/395,136 KiB, BLAS1, six-GiB watchdog, no timeout/error/stderr. These are original-code baseline successes, not proof of the overclaims. Original caches remain verbatim. All 56 original IDs are preserved in ORIGINAL_CHECK_IDS.json.

Independent controls include full 70-dimensional occupation Hamiltonian reconstruction; actual slab below-gap response and eigen-residuals; actual zero/nonzero-m antiunitary domains and many-body CP; fixed-Z measurement counterexamples; complete 2,048-case dense CZ comparison; actual missing-CZ-phase and missing-JW-sign mutants; one full-run false-extra-scalar mutant that incorrectly still passes 33/0; and actual note/memo/source cache drifts. Twelve first control groups, eleven additional groups, and a supplemental exact-rational joint-law counterexample are recorded, with scripts/stdout/receipts. Positive controls establish finite math, not physical registration or a limit theorem.

Only review artifacts were changed after the baselines. All preparation failures are preserved: executable-mode assertion during first extraction, one external context receipt script's wrong forensic-tool path, and a receipt writer's syntax error before execution. No source/scientific run was retried for either.

## Findings

### F1 — P2: Separate massless spectral BDI and kernel CPT from fixed-m many-body symmetry

Exact anchors: N7894:184; N7894:238; R7894:959; R7894:1063. Full paths and line hashes are in FINDINGS.json.

The note assigns C=Eps K and S=Eps beside the massive h(m), although Eps h(m) Eps = -h(-m), so these are spectral particle-hole/chiral symmetries of h0, not of fixed nonzero m. At m=0.7 the claimed particle-hole anticommutator residual is 1.4. D6 checks only squares, not the required Hamiltonian relation. The eight-dimensional product of two antiunitary one-particle maps is linear +I; the many-body table uses a unitary C and antiunitary T, and its C/CPT columns send H(m) to H(-m). The phrase vector-like, none broken and the unqualified CPT reading erase that distinction.

**Narrow repair:** State the specified internal spectral BDI relations at m=0 only; test their commutation/anticommutation against actual h at zero and nonzero m. Distinguish the declared one-particle spectral C, its kernel product, and the many-body C/table; retain the latter exact mass-flip entries. No physical CPT or fixed-m C/CPT invariance follows from the +I kernel product. Preserve exact P-corner and T invariance at all real t,m; qualify gap as 2|m| (original D1 samples positive masses).

Evidence: INDEPENDENT_CONTROLS.json: C domain controls, original-execution/7894/RECEIPT.json: D6 and E table.

### F2 — P2: Classify CP/PT before invoking Kramers and the m=0 restriction

Exact anchors: N7894:186; N7894:243; R7894:968. Full paths and line hashes are in FINDINGS.json.

The half-shift squares do not depend on m. Actual one-particle CP=Eps U_mirror K has square -I and anticommutes with h(m) even at m=0.7; PT at the cube centre commutes only at m=0. A spectral antisymmetry pairs E with -E and is not a commuting Kramers symmetry at general energy. In the actual many-body representation, unitary C times the odd-shift mirror preserves both hopping and mass at fixed m, contrary to the shared statement that both send m to -m.

**Narrow repair:** Give separate square, unitary/antiunitary type, and commuting/anticommuting relations for each product at the actual source level. Restrict any Kramers inference to a commuting antiunitary on the specified eigenspace (or explicitly the zero-energy subspace). Remove the claim that the square itself occurs only at m=0 and avoid inferring physical spin from it. Add actual nonzero-m controls.

Evidence: INDEPENDENT_CONTROLS.json: CP/PT at m=0,0.7 and actual many-body CP.

### F3 — P2: Make D7 test all listed improper CPT alternatives

Exact anchors: N7894:185; R7894:957; R7894:965. Full paths and line hashes are in FINDINGS.json.

D7 tests only the corner product and never checks the other improper products for scalar action. A full-source mutation replacing the x=0 reflection representation with the corner representation after D4 adds a second scalar CPT product while the complete runner still reports 33/0.

**Narrow repair:** Check every explicitly tested improper representation and its antiunitary flag against a scalar-identity condition, then assert the intended complete count/list. Preserve the corner result and scope uniqueness to that tested list; the mutation must fail the actual final runner.

Evidence: symmetry_second_scalar_mutant.py, symmetry_second_scalar_mutant.stdout, INDEPENDENT_CONTROLS.json, ADDITIONAL_CONTROLS.json.

### F4 — P2: Zero record diagonal does not establish correlation readout or history covariance

Exact anchors: N7894:116; N7894:223; N7894:245; N7894:279; R7894:1081. Full paths and line hashes are in FINDINGS.json.

The exact zero-diagonal test only excludes direct fixed-Z readout. Even the entire joint distribution of Z strings cannot distinguish |+> and |->, although their X expectations are +1 and -1. Thus register only through correlations does not follow for the offdiagonal operators. A Hamiltonian/Pauli covariance does not supply a record-formation rule or a covariant probability law for permanent histories.

**Narrow repair:** Retain pure-Z versus zero-Z-diagonal facts. State that offdiagonal readout would require a separately supplied instrument/context/dynamics and is not derived, rather than asserting correlation recovery. Narrow P/T record statements to covariance of the declared fixed readout functions under the supplied map; leave history/formation covariance open. Keep the counterexample as an actual control.

Evidence: INDEPENDENT_CONTROLS.json: identical complete Z law, context/docs/MINIMAL_AXIOMS_2026-06-29.md.

### F5 — P2: Remove the false finite-volume singular zero-field limit

Exact anchors: N7897:200; N7897:201; R7897:558. Full paths and line hashes are in FINDINGS.json.

The finite slab has an isolated positive gap 9.544487e-5 at V=8 and a C-even ground state. Therefore its zero-field ground expectation is continuous and tends to zero, not -1/2. Actual unchanged gstate gives O=-0.4217863 at h=1e-5, -0.00814690 at 1e-7 and -8.14801e-5 at 1e-9; residuals are below 7e-14. The reported saturation at h=0.001 is real but does not prove the limit.

**Narrow repair:** Preserve the original ±0.001 rows and finite susceptibility protocol. Remove singularly and the false fixed-volume limit everywhere, including D3/stdout. State the finite analytic response and the separate, unproved order of infinite-volume and h→0 limits. Add the actual below-gap field controls; do not run a larger-volume campaign.

Evidence: INDEPENDENT_CONTROLS.json: slab fields and finite gap, independent_controls.py.

### F6 — P2: Use opposite C parity, not a C-conjugate excited partner or an exact two-string cat

Exact anchors: N7897:178; N7897:199; R7897:445; R7897:552. Full paths and line hashes are in FINDINGS.json.

A C-even ground vector obeys Cg=g; its first excited state cannot be Cg. The complete independent 70-dimensional cube control at V=8 gives ||Cg-g||=5.85e-16 and first-state overlap with Cg=2.22e-16, while the gap is 0.07816297. The same ground vector has only 0.945750949 total probability on the two extreme checkerboards, so it is not exclusively their even combination at finite V.

**Narrow repair:** Retain opposite-C-parity lowest excitation and actual gap comparison on the sampled V list, with the convention for C explicit. Describe the finite even state as containing the full set of configurations, with the measured extreme-string weights. Preserve C-invariance and bimodality; add actual C-action, orthogonality and non-two-string controls.

Evidence: INDEPENDENT_CONTROLS.json: complete cube/C action/checkerboard weight.

### F7 — P2: Separate bulk Hartree integrals, finite tori, and an asymptotic proof

Exact anchors: N7897:139; N7897:159; N7897:166; N7897:220; N7897:255; R7897:414. Full paths and line hashes are in FINDINGS.json.

c_inf is a continuous Brillouin-zone integral, not a finite antiperiodic-torus number: the runner itself finds distinct thresholds 0.747072,0.738124,0.735366 at L=8,12,16 versus bulk 0.732047. Yet the theorem/method captions say antiperiodic is used throughout and no thermodynamic limit is taken. The correct-looking m² log(1/m) law and limiting exponent are asserted from three ratios/nine finite slopes; those finite computations do not prove the asymptotic claim even within Hartree.

**Narrow repair:** Label c_infinity, its bulk Hartree critical value and bulk roots separately from finite antiperiodic response/energy comparisons. Retain all numbers. Either supply the short local-zone asymptotic estimate with a controlled remainder and derive the conditional Hartree scaling, or narrow to sampled numerical evidence without asserting a proved limit. Preserve the useful logarithmic candidate, not a physical transition claim. The undivided self-consistency also has m=0; identify nonzero branch selection explicitly.

Evidence: original-execution/7897/RECEIPT.json: A4/B1/B2/table/E2, PROOF_REVIEW.md: bulk integral and local asymptotic derivation.

### F8 — P2: Replace exact classical/checkerboard and exclusive Dirac-window claims with scale comparisons

Exact anchors: N7897:162; N7897:170; N7897:241; N7897:326; R7897:400; R7897:408. Full paths and line hashes are in FINDINGS.json.

At V=2, the reported O=-0.457388 is not the classical ±1/2 value, and finite hopping remains. Ratios 0.915,0.979,0.991 approach a limit; they do not establish an exact classical state at these finite couplings. Comparing 2m with the free bandwidth and a one-body branch-point length with one spacing does not prove an exclusive physical Dirac-mass window or an interacting correlation length. No approximation-error threshold defines V≈1.

**Narrow repair:** Retain m, gap, ratios, bandwidth and length values as explicitly specified Hartree/one-body scale diagnostics. State approach toward the strong-coupling checkerboard limit, and call the small-m window illustrative rather than necessary/exhaustive. Identify xi as the supplied/rederived one-body amplitude branch-point comparison, with coarse-unit normalization and no interacting/physical correlation-length theorem.

Evidence: original-execution/7897/RECEIPT.json: B3/B4, PROOF_REVIEW.md: finite Hartree state and branch-point scope.

### F9 — P2: Do not grade a true critical coupling from a two-shape crossing

Exact anchors: N7897:183; N7897:184; N7897:325; R7897:524. Full paths and line hashes are in FINDINGS.json.

The cube and slab differ in coordination (3 versus 4), boundary condition and shape, and neither is the z=6 bulk model used for Vc_Hartree. Their two-curve crossing at 1.76598 is a valid finite diagnostic, but mean field low by 2.41 and the disordered/ordered assignments treat it as a controlled interacting critical estimate. The separate no-transition disclaimer does not justify that comparison.

**Narrow repair:** Keep both complete curves, the two-size crossing and arithmetic ratio as comparisons of specified models. Remove the error/underestimate/phase labels and any suggestion that a third size alone would certify extrapolation; no larger simulation is needed.

Evidence: original-execution/7897/RECEIPT.json: C7, SOURCE_SELECTION.json: full N97.

### F10 — P2: State the supplied probability/readout and finite-Fock bridge separately from sign symmetry

Exact anchors: N7897:23; N7897:201; N7897:211; N7897:237; R7897:8; R7897:570; R7897:585. Full paths and line hashes are in FINDINGS.json.

The program computes a chosen Fock Hamiltonian and Born occupation weights, not a formation law selecting a permanent physical record or a six-edge BKSF readout intertwiner. Matching one free cube energy to -4sqrt3 cannot prove the encoding/state/observable bridge. C-evenness forbids a unique C-odd expectation in a C-invariant finite state, but does not cause spontaneous realization of one classical bit. The interaction is diagonal; the hopping term does not conserve individual occupation records. Self-consistency determines a nonzero Hartree branch only after the ansatz/branch (or minimization criterion) is supplied.

**Narrow repair:** Preserve conditional Hartree mass identity, even functional, chosen Fock spectra and explicit occupation-projector probabilities. Name Born joint occupation measurement, role labels, Hamiltonian, state/branch choice and any proposed physical readout as supplied conditional structure. Do not call the entire law record-conserving. Keep the six-bit encoding comparison as unaccepted context unless an actual bounded intertwiner is supplied; do not import its parent tower. State only sign degeneracy/nonselection from symmetry, leaving registration dynamics and physical SSB open.

Evidence: INDEPENDENT_CONTROLS.json: same marginals/joint-law limitation, context/docs/MINIMAL_AXIOMS_2026-06-29.md, PROOF_REVIEW.md: model and readout boundary.

### F11 — P2: Bind each actual note, premise and canonical identity before refreshing evidence

Exact anchors: N7894:2; N7894:5; R7894:16; N7897:2; N7897:5. Full paths and line hashes are in FINDINGS.json.

Both units have short frontmatter aliases that differ from the filename-derived graph IDs. The actual primary extraction works and both helper APIs correctly return zero helpers, but declared_input_paths is None for both runners; both original caches report fresh after actual own-note or quoted-memo drift. Actual citation extraction is empty despite the axiom interpretation being used. This permits unsupported current-note reuse of old evidence.

**Narrow repair:** For BOTH notes use actual filename-derived IDs consistently in metadata/trace; declare and validate the own note plus the precise used current premise/context inputs, without fabricated helpers. Add actual Markdown premise links (YAML alone is insufficient); leave unaccepted parent prose explicitly contextual. Make absent/drifted inputs reject actual live source/cache readiness. Freeze final prose/inputs first, then one genuine final run each using real cache pre/post guards; preserve both original caches and this baseline externally/historically as needed. Keep audit deferred.

Evidence: CLOSURE.json: both actual consumers, ADDITIONAL_CONTROLS.json: four omitted edges and two source drifts, SOURCE_CONTEXT_BINDING.json: current memo equals raw parent.

### F12 — P3: Keep the explanatory taste count consistent with the eight-dimensional census

Exact anchors: N7894:193; R7894:881. Full paths and line hashes are in FINDINGS.json.

The narrative says two doublets, one of each handedness, but D3 and the theorem correctly have chirality multiplicities +1×4 and -1×4: two right-handed and two left-handed two-dimensional doublets.

**Narrow repair:** Correct that sentence to two doublets per handedness (four Weyl doublets/two Dirac tastes in this specified linearized representation), retaining the finite eight-dimensional classification and its physical/continuum limitations.

Evidence: original-execution/7894/RECEIPT.json: D3.

## Scope, preservation and handoff

CLAIM_PATH_DISPOSITIONS.json maps all ten theorem blocks and both corollaries, including propagation through long frontmatter/reading/trace/stdout replicas. PROOF_REVIEW.md records the positive derivations and exact interpretation boundaries. All selected original science is retained for correction; none is dropped because premises are supplied. No raw parent campaign or reserved science is silently accepted.

Use a separate author worktree. Preserve all six original bodies and both new original-source executions before correcting. Keep existing seeds, model parameters, finite diagnostic tables and 56 original check IDs; add only decisive bounded controls and honest domain labels. No larger cluster/production campaign is required. Freeze final note/premise inputs before genuine final caches; use the actual note-derived graph/packet consumers and Markdown citation extraction. Follow-up interpretation context from reviewed wave20 #7888/#7890, after root verifies its landing, must be explicitly bound, rather than copied from stale raw parents. Root owns current-main composition, manifest, gates and any publication; this reviewer remains available for original-session affected-source confirmation.

No audit, pipeline, PR mutation, source fix, commit, push, axiom amendment or independent approval of supplied physical mechanisms occurred.
