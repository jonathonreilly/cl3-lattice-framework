# Review history — block 01

(conformance pass + quote-fidelity checker findings at close)

## 2026-09-04T21:45+00:00 — blind Opus supplied-input ledger: CHECKED (supervisor)
Deliverable: BLIND_supplied_input_ledger_opus.md (26 ranked rows, 16 narrowings/contradictions). Supervisor spot-verified 8/8 load-bearing quotes against inputs/ (PR #7959 "the link role is designed, not derived"; PR #7915 N3 "not a claim that permanent Records update unitarily"; PR #7963 the -3.849 sigma early-window RK coefficient; PR #7921 "would make a supplier choice look like axiom content"; PR #7959 "toward z = 2, not away from it"; PR #7886 line 237 "does not derive kappa_s>0 or kappa_s=kappa_t" and lines 60-62 "a temporal registration kernel by itself supplies only the electric/temporal quadratic block ... has no magnetic restoring block and is not Maxwell"; PR #7915 lines 62/569 attributing kappa to "the Record-overlap magnetic curvature"). All hold verbatim.
Findings carried into block 01: (F-B1) SCOPE CONTRADICTION #7915 vs #7886 on what the Record-overlap chain supplies (magnetic curvature vs temporal block only) — the landing core must state the magnetic restoring block as a supplied input, not Record-derived, at #7886's own scope. (F-B2) the two deepest supplies are the TIME RULE (conservative first-order flow; no axiom names time; Record permanence in tension with per-tick updates) and M5 (positive diagonal conserved energy; #7917's uniqueness evaporates without it) — block 02 candidates. (F-B3) c^2 = U K flips verdict four times across finite volumes (#7945 -> #7952 -> #7955 -> #7963); #7963's own early window carries a resolved -3.849 sigma RK coefficient where #7945 treats RK as a clean null — the landing core's photon item must carry this estimator boundary. Status of this seat's work: CHECKED, awaiting cross-merge with the Fable primary's ledger (disagreements = findings).

## 2026-09-04T22:17+00:00 — block 01 close: checker verdict, fix pass, conformance gate
Checker (Opus, refuting): FIX FIRST — CH-01 blocker (same-carrier attribution), CH-02..CH-05 material, CH-06..CH-14 minor; 203 attributions checked; passes on self-containment, status block, photon-open, terminal, no derivation voice; D3 confirmed for the primary. Supervisor verified CH-01..CH-05 against the note and inputs before applying. Fix pass commit baf24571d5 (all findings applied; none rejected). Deviation logged: that commit was staged with `git add -A` (owner directive forbids it); the staged set was exactly the three deliverables; explicit-path staging from here on.
Conformance gate (REVIEW_LOOP_PR_CONFORMANCE_SPEC sections 1-12):
1 self-containment — PASS (one markdown link, to the landed axiom memo; no unlanded note linked; eleven verbatim PR copies removed from the pack inputs, replaced by a SHA-256 provenance README).
2 cache/execution — NOT APPLICABLE (no runner; the note declares Runner: none and computes one declared product only).
3 claim-scope honesty — PASS (meta; status fields from their enums; "landing core" declared plain prose, not a tier; no bare letter-number names in title; full-surface consistency: title/headline/status block/closing agree on "open" and "meta").
4 N-gate — NOT TRIGGERED (no own-voice no-go; member negatives quoted at scope only; the "does not claim" section is non-claims, not walls) — verified by grep of the note outside quoted spans.
5 proof obligations — NOT APPLICABLE (no theorem claimed).
6 runner validity — NOT APPLICABLE (no runner).
7 packet completeness — NOT APPLICABLE (meta row; no helper runners).
8 links/graph — PASS pending manifest: the delta adds exactly one graph node (u1_maxwell_light_lane_landing_core_meta_note_2026-09-05), no edges rewired; manifest regenerated on the final tree and staged explicitly at commit.
9 note structure — PASS (15 machine-status fields with mandated values; Imports section; Review record section added at close; no `surface_status` field).
10 propose/ratify — PASS (no audit fields written; manifest is the only generated artifact).
11 sourced facts/counts — PASS (as-of stamp 2026-09-05 added; member/record counts recomputed by the primary from the pack inputs at HEAD).
12 pre-review gates — vocab_lint --fix then --report-only: 0; audit_lint --strict: PASS; git diff --check merge-base..HEAD: clean; py_compile: no Python in delta; check_changed_audit_evidence: meta rows exempt; run_pipeline.sh: exit code recorded below when the background run completes; generated outputs restored before commit; explicit-path staging; cold read of the diff by the supervisor.
Independence class disclosed: single family (Claude), cross-model (Fable primary / Opus checker + Opus blind ledger), supervisor hand-verification.

## 2026-09-04T22:30+00:00 — pipeline gate closed; PR opened
run_pipeline.sh, full run on the final tree (HEAD 7bcb2d6764): PIPELINE EXIT=0. The earlier run's exit 1 was caused by the supervisor pruning the eleven pack input copies while that run was in progress ("cannot read static input .../inputs/PR7884__..."), not by the science; the rerun on the final tree is the gate of record. Generated outputs restored before commit (`git restore --source=HEAD --staged --worktree -- docs/audit/data/ docs/audit/AUDIT_QUEUE.md docs/audit/MISSING_DERIVATION_PROMPTS.md docs/repo/FRONT_DOOR_STATUS.md; git clean -fdq -- docs/audit/`); the pipeline's front-door re-render (row counts 4914 -> 4476 from native retirement of the moved notes; publication section in deferred mode) is a nightly-owned surface and is not this block's science. Manifest check: build_citation_graph + write_citation_graph_manifest re-run on the final tree (4761 nodes, 11860 edges) leaves the committed manifest byte-identical — section 8 of the gate is PASS, no longer "pending manifest". Pack hygiene at close: specs/full_primary.log (the dead codex sol seat's raw 316 KB stream, committed in checkpoint 75b4ad0649) is removed from the branch tip — untrusted worker output with no review value; the salvage narration (specs/SALVAGE_sol_primary_narration.md, marked untrusted draft input) stays; the raw stream remains reachable in branch history at 75b4ad0649.

# Review history — block 02 (the #7917 dynamics class against the axioms)

## 2026-09-05 — value gate V1-V5, answered in writing before any PR (Fable primary)
V1 (obstruction closed). No verdict-identified obstruction is closed: the members are unlanded open PRs with no audit row, so
there is no `verdict_rationale` to quote; the obstruction is the terminal's own boundary, quoted at scope from open PR #7917:
"The classification does not derive that dynamics class from the axioms, and exact finite local tick selection remains open."
and "The four axioms do not currently select that class. In particular, they do not state real linear first-order evolution,
energy conservation, minimal (E,B) payload, or continuous time." This block does not close it; it makes it item-exact
(trace_class upstream_support, consumer = the light lane's terminal): two of the seven items are shown mutually redundant
inside the class (compatibility from covariance under the vector-type payload law; covariance from compatibility plus
conservation with no orientation premise), one has a named axiom lever, and the other four are supplies with exact witnesses.
V2 (new content + the search). New: (i) the exact classification of every covariant nearest-neighbor real linear generator on
the one-component edge/face payload under all sixteen signed-permutation representations (four distinct couplings; only the curl
gauge/chain-compatible); (ii) the exact nullspace theorem that nearest-neighbor + gauge + magnetic-Gauss forces the curl with one
lattice-wide coefficient, hence item 4 from items 1,3,5,6,7; (iii) the parity theorem (edge-face couplings only at odd distance);
(iv) the sampling-identification dissipation (Gauss-Seidel decrease, radius two on the collapsed payload); (v) the item-6 versus
2026-08-13 analysis (three-part decomposition; the revision removed the first part for records, the axioms never had the other
two); (vi) ten exact witnesses; (vii) the two-speed extended conservative class with a vertex payload. Search: origin/main
e249016f759f224d9b429932cd0d1db4d452dc1a; the commands, thirty statement patterns, obligation/ledger greps and title greps, all
hits and their classification are in ROUTE_PORTFOLIO.md under "Block 02 prior-art sweep"; every matched hit is context,
method precedent, or a different object/mechanism; target state OPEN.
V3 (framework sentences needed). Yes: the Lattice axiom's "proper cubic rotations about each site" is what makes the face-site
stabilizer a supplied symmetry (the compilation's sector-preserving subgroup is computed from the parity roles, a supplied
structure the axioms permit but do not name); Lattice's "No site is privileged" sentence is the lever for item 4; Admissibility's
covariance and neighborhood sentences define IP-A/IP-B and the sampler; Record's one-record-per-site sentence is why a field
evolution is not a record sequence; the Qualification's one-answer sentence is the lever for the memoryless clause; the
2026-08-13 revision text decides the M5 kin question. Representation theory of D_4 and skew matrices alone would not produce
the adjudication, the identification premises, or the M5 analysis.
V4 (non-trivial). Yes: the redundancy of items 4 and 5 inside the declared class is a structural fact about the terminal that no
member states; the sixteen-representation classification and the cube-connectivity nullspace are constructions; the witnesses
are explicit laws checked exactly, several of which (unoriented, overdamped, vertex-scalar) are not in any member.
V5 (not a one-step variant). No. Closest landed: DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06 (class != selection, for
the Wilson class under record preservation — different class, different mechanism, no per-item adjudication);
ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_2026-08-13 (same witness METHOD on static conditional laws — different object);
DYNAMICS_FORM_FROM_RECORD_PRESERVATION_2026-06-05 (gauge invariance from record preservation of a supplied Hamiltonian under
bridges — different mechanism from the covariance stabilizer). Closest campaign cycle: block 01 (meta; catalogued the class
without adjudicating it). Closest member: #7917 (declares the class and uses gauge as a hypothesis; never states that covariance
forces the curl or that its covariance step is implied by its magnetic-Gauss clause); #7921 (uses gauge for the curl too).
Structural distinction: this block removes a hypothesis from the declared class and names the exact residual with witnesses.
Gate: PASS on V2-V5; V1 answered honestly as upstream support, not closure (the PR is a bounded_theorem, not a promotion).

## 2026-09-05 — block 02 conformance gate (REVIEW_LOOP_PR_CONFORMANCE_SPEC sections 1-12), recorded before any PR
1 self-containment — PASS: one markdown link in the note (the landed axiom memo); no unlanded note linked; the runner declares one
  input (`docs/MINIMAL_AXIOMS_2026-06-29.md`, landed); PR numbers are evidence addresses in backticks; the compilation is rebuilt
  from the parity rule inside the runner, not imported from any member.
2 cache/execution — PASS: cache written through `runner_cache.execute_and_write_cache` (status ok, exit 0, `timeout_sec: 900`
  equal to the declared `AUDIT_TIMEOUT_SEC = 900`, no timestamps, input fingerprint bound); read inventory stated in the runner
  docstring and the note (one external input; no package-local integrity read); re-pinned after the last runner edit (the literal
  `AUDIT_INPUT_PATHS` declaration) — the note was edited after the cache but is not a pinned input.
3 claim-scope honesty — PASS: finite domain and parameters stated on every surface (note prose, title, runner docstring and
  banner, certificate lines, machine-status block); status fields from their enums (`bounded-support` / `bounded_theorem`); no
  "certified/closed/complete/global/the law" claims; no bare letter-number names in title or headings (the premise labels LR,
  IP-A, IP-B, OL, SI are defined in section 1 and used as parenthetical aliases of their spelled-out names); no coined tier word
  ("named premise", "supply", "witness" are plain prose).
4 negative claims / N-gate — TRIGGERED and PASSED at scope: N1-N8 landed as section 12 of the note (seven attempted/excluded
  routes, one live; pairwise wall table with collapse to five; hidden-wall scan; citation table with drops; five-resolution
  rhetoric audit; partial-closure and primitive scan; steelman naming the live route; cross-cycle echo); the N5 certificate
  lines are in the cached stdout (five lines, each > 40 chars, all "executed").
5 proof obligations — PASS: target claim stated in one sentence before the proof; every lemma marked proved-here (runner
  section named) or a named premise; hypotheses carried (each conditional verdict lists its premises); boundary cases stated
  (sizes 4/6/8 executed, two size-free arguments named); strongest missing lemma named per row (section 9); no circular
  reduction (the class is never a premise; items are used only as named hypotheses of conditional statements).
6 runner validity — PASS: twelve load-bearing mutations on scratch copies, one per check family, all detected (table in
  RESULTS_block02.md); independent-math checks: hand-derived one-face stencil, blockwise symbolic conservation equations,
  cube-connectivity argument, kick-drift-kick invariant derivation, momentum-census multiplicity predictions — all agree with the
  exhaustive runner.
7 packet completeness — PASS: single primary runner; no helper runner; no registry edit.
8 links/graph — PASS: manifest regenerated on the final tree (`run_citation_graph_build.py` then
  `write_citation_graph_manifest.py`): delta = +1 node (this note), +1 edge (its link to the axiom memo), 4761->4762 nodes,
  11860->11861 edges, no rewired edge; staged alone (commit 77dc5ace14); no other generated surface dirty after the build.
9 note structure — PASS: frontmatter (claim_id, claim_type, claim_scope, upstream_dependencies, runner); machine-status block
  with every mandated field and trace fields; Imports section with role/provenance/open-bridge separated; Review record (worker
  provenance, independence class, mutations, no hard landing conditions).
10 propose/ratify — PASS: no audit field written; the manifest is the only generated artifact staged; generated audit surfaces
  restored before each commit.
11 sourced facts/counts — PASS: every count in the note is recomputed by the runner at HEAD (censuses, multiplicities,
  dimensions) or quoted from the memo; PR quotes are from the extracted texts of 2026-09-05 (as-of stamp in the note).
12 pre-review gates — vocab_lint --fix then --report-only: 0; audit_lint --strict: OK, no errors; py_compile: ok;
  `git diff --check e249016f75..HEAD`: clean; check_changed_audit_evidence --base origin/main: checked=0 failures=0 (no ledger row
  exists yet for the new note; the pipeline seeds it); stacked delta be4fa51f32..HEAD = 13 files (independently recounted);
  explicit-path staging throughout; cold read of the complete note done (one wording fix, commit 2f53ea6751); run_pipeline.sh:
  launched after these commits — exit code recorded below when it completes.
Independence class disclosed: single family (Fable primary), cross-context (hand derivations against the exhaustive runner);
refuting checker seat not yet run — disposition `pending` in CLAIM_STATUS_CERTIFICATE.md.

## 2026-09-05 — block 02 pipeline gate
`bash docs/audit/scripts/run_pipeline.sh` on the committed tree (HEAD cb7e75702b): pipeline exit=0; the new row `u1_dynamics_class_axiom_adjudication_bounded_note_2026-09-05` is seeded by the pipeline; generated audit surfaces restored to HEAD before this commit (tree clean).

## 2026-09-05 — supervisor line-by-line review of block 02 (Fable supervisor)
Read in full: GOAL_block02.md, the note (770 lines), the runner (1,149 lines), RESULTS_block02.md, the receipt, the pack deltas. Hand-verified the load-bearing mathematics: the D_4 face-stabilizer map (a,b,c,d) -> (-d,a,-b,c) under the 90-degree rotation about the normal with vector transport, whose only invariant stencil is (1,1,-1,-1) (scalar law: (d,a,b,c), invariant (1,1,1,1)); the blockwise skew equations M G + G^T M = 0 => 2 w_E u = 0, 2 w_B v = 0, w_E r + w_B q = 0; the kick-drift-kick map as velocity Verlet with x = E, v = -C B, omega^2 = C^T C, shadow energy |B|^2/2 + |E|^2/2 - (h^2/8)|C E|^2 positive iff spec(C^T C) < 4/h^2 (9 < 16 at h = 1/2); the side-6 multiplicities from the coarse-side-3 momentum census (26 nonzero momenta, 4 sin^2(k/2) = 3 per nonzero component: 6/12/8 momenta -> eigenvalues 3/6/9 with transverse doubling 12/24/16, zero modes 26 + 3 = 29; Hodge 18/36/24 with 3 zero modes); the cube-connectivity nullspace argument (each cube edge lies in exactly two of the cube's faces with opposite signs, forcing equal q_f); the per-mode overdamped slow root -s^2 - s^4/gamma; the trace argument for "no positive form of any kind". Also checked: runner sha256 = receipt; `upstream_dependencies: - minimal_axioms` is the landed convention with a live ledger row; the six N4-cited notes exist on origin/main in docs/. Supervisor findings: none beyond the checker's (the gloss "agree on the in-plane 180-degree flip" was independently confirmed to mean alpha_E = alpha_B at a boundary edge fixed by the flip).

## 2026-09-05 — refuting checker (Opus 5) verdict and the fix pass
Checker deliverable: CHECKER_block02_findings.md (disjoint machinery: own d0 sign, Levi-Civita curl signs, Fourier block-diagonalization, brute-force representation enumeration; eighty independent checks; three planted mutations all caught). Verdict FIX FIRST; no verdict in the seven-row table refuted. Every finding was verified by the supervisor against the primary surfaces before it was applied:
- CK-01 (material) VERIFIED: "The classification does not derive that dynamics class from the axioms" is not in PR #7917 (body grep: absent; the string is the campaign's own science-record précis, inputs/light_lane_science_records.json). Fix: the PR body's sentence "This is a bounded conditional classification, not an axiom derivation or TOE-status change." is quoted instead; target_blocker_text is #7917's verbatim "The four axioms do not currently select that class ..." with source_of_blocker_text: handoff. The same précis-as-quote sat in block 01's meta note and LANDING_CORE (PR #7976): fixed on the block-01 branch in the same pass and recorded in that note's Review record.
- CK-02 (material) VERIFIED with a refinement: the PR #7913 body reads "Valid even-torus role fields are exactly eight translated sectors." — "translated" is the PR's own word (the checker searched only its head-branch note) — but the note's quote was not verbatim. Fix: the body sentence quoted verbatim.
- CK-03 (material) VERIFIED: the sixteen tensor-transport laws classify the signed-permutation representations up to a diagonal sign relabelling; the relabelled law (payload negated at every z-normal face) has covariant coupling D C with D C d0 = 0 and d2 D C != 0. Fix: section 3 and claim_scope say "in the compilation's sign basis"; the item-5 conclusion is stated as representation-free through section 4's nullspace theorem; the runner exhibits the relabelled law as an executed check; the falsifier bullet is scoped accordingly.
- CK-04 (material) VERIFIED against the runner's predicates (complex law: conservation only; nonlinear: non-homogeneity only; tick: neither covariance nor locality). Fix: executed checks added — tick covariance and per-shear locality by perturbation; nonlinear locality, gauge invariance and covariance by perturbation and rotation; the complex law's assembled real generator (antisymmetric, radius 1, covariant under the doubled representation, edge-to-face blocks exactly C); the onsite-phase coupling replaces the constant conjunct.
- CK-05 (material) VERIFIED: covariance is representation-relative; the derived generator is covariant under the vector/vector law and its global twist only. Fix: "with no orientation premise" qualified wherever it occurs (results table, section 4, section 9) to "beyond the oriented d0/d2 that item 5 itself names; covariance exhibited for the oriented representation".
- CK-06 (minor) VERIFIED: section G tests no reversibility, and the systematic sweep is not reversible. Fix: R1 reworded to the single-site detailed-balance statement, marked not executed.
- CK-07 (minor) VERIFIED: the capacity check was a tautology on literals. Fix: dim_R M_2(C) computed as the rank of the real coordinate basis; component counts read off the constructed generators.
- CK-08 (minor) VERIFIED and adopted: the side-6 gauge-plus-chain nullspace is now solved in full generality (324 unknowns) in the runner; section 4 states sides 4 and 6 in full generality.
Fix-pass runner: TOTAL: PASS=100 FAIL=0 (95 + 5 executed checks; the section-M check rewritten, not added); cache re-pinned on the final runner. The note's Review record now discloses the independence class as cross-model (Fable primary / Opus 5 refuting checker / supervisor hand verification) and records the checker's mutations. Disposition: pass after the fix pass.

# Review history — block 03 (the Gauss rows as support forcing on the extended payload class)

## block 03 — V1-V5 (primary)
V1 (obstruction closed). No verdict-identified obstruction is closed: the members are unlanded open PRs with no audit row, so there
is no `verdict_rationale` to quote; the obstruction attacked is block 02's residual wall W_P (the payload, item 7 of the declared
class), quoted verbatim from block 02's note: "The exact residual supply of the terminal relative to the four axioms is therefore:
payload and its transformation law, deterministic real linear continuous time, nearest-neighbor locality (unless the
identification premise IP-B is granted), and positive diagonal energy conservation." This block tests whether the class's own
supplied Gauss rows (item 5) buy the vertex/cube half of item 7 — they do, DERIVED-CONDITIONAL-ON(SF-all, EC, CONS): frozen and
decoupled payloads, in every charge sector — and whether they buy the coin/hidden-time half — they do not (six-parameter
conservative coin family cut to four, never to zero; two exact witnesses each). Trace class upstream_support, consumer = the
light lane's terminal via block 02's residual; the payload wall is split, not closed.
V2 (new content + the search). New: (i) the exact ten-dimensional covariant nearest-neighbor class on the four-role payload with
the cube payload (56 patterns; sides 4 and 6) and its three-speed conservative cut; (ii) the Gauss rates as exact linear
functionals coefficient by coefficient (the coupling blocks d0^T C^T and d2 C vanish identically); (iii) the collapse theorem
with its exact iff (a2 = 0 and u_E rho_V = 0; b = 0 and u_B rho_C = 0) and the frozen-payload corollary under conservation;
(iv) the exact maximal invariant subspace of a non-preserving member (connectedness lever: phi, psi constant) and the sector
branch count (52 = 2 x 26 transverse; longitudinal 26 = 6 + 12 + 8 absent); (v) the emptiness of every invariant subset of a
charged surface under a vertex-coupled conservative member; (vi) the odd-shift self-duality (d0, C, d2) -> (-d2^T, C^T, -d0^T);
(vii) the sixteen-dimensional coin class, its six-parameter cut and the rows' cut to four; (viii) the kernel-dimension
certificate (0 against 116) that the complex law is not decoupled by any real change of basis, and the finding that it preserves
the rows at zero charge only; (ix) the second-order hidden-time identity. Search: origin/main
e249016f759f224d9b429932cd0d1db4d452dc1a; the commands, the twenty-six statement patterns, the title sweep, all hits and their
classification are in ROUTE_PORTFOLIO.md under "Block 03 prior-art sweep"; every matched hit is context or a method precedent
on a different object; target state OPEN.
V3 (framework sentences needed). Yes: Admissibility's support reading note ("'available'/'admissible' denotes its support")
is what makes a Gauss row a constraint on the admissible set rather than a dynamics, and the memo's "Admissibility is not a
dynamics axiom" is why "preserves" has to be defined as invariance of that set under a separately supplied flow; Lattice's
nearest-neighbor adjacency and standard translations give the connectedness lever (ker of the Laplacians = constants) and the
odd-shift duality (a standard translation that changes the sector); Lattice's rotations define the class; the Qualification's
"Further physical structure requires a retained derivation or bridge" is why the rows' content and charges stay supplied;
Record's "locks exactly one admissible local possibility" with Qubit's M_2(C) decide the coin steelman (one record is one point
of an eight-real-dimensional domain, not one real number). Linear algebra alone would produce the class and the multiplicities
but not the two readings of support forcing, the adjudication, or the coin disposition.
V4 (non-trivial). Yes: an exact class with the cube payload; a constraint-dynamics computation (rate functionals, invariant
subspaces, affine consistency) that no member performs; the charged-surface emptiness and the coin cut are structural facts about
the terminal's payload item that no member states; witnesses are explicit laws checked exactly.
V5 (not a one-step variant). No. Closest landed: TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE (Record-side operator invariance
under Gauss generators — different object); SIGNED_GRAVITY_CONTINUUM_GRADED_EINSTEIN_LOCALIZATION (a constraint surface preserved
under formal jet transport — same notion, different object and mechanism); AXIOM_FIRST_REEH_SCHLIEDER (a maximal invariant
subspace of a commutant — same tool, different object). Closest campaign cycle: block 02 (the vertex witness with its Hodge
multiplicities and two speeds; no constraint analysis, no cube payload, no coin class, the complex law's row preservation asserted
in the contract but not executed). Closest member: #7917 (item 5 and item 7 declared side by side; never composed); #7893
(the row as a support condition among records on a different carrier; no field dynamics). Structural distinction: this block
composes the class with its own constraint, splits item 7 into a conditional half and a supplied half, and finds that a
background charge makes a vertex coupling inconsistent with the row rather than merely invisible.
Gate: PASS on V2-V5; V1 answered honestly as upstream support (the PR is a bounded_theorem, not a promotion).

## 2026-09-05 — supervisor line-by-line review of block 03 (Fable supervisor)
Read in full: GOAL_block03.md, the note (806 lines), the runner (1,301 lines, sections A-M), RESULTS_block03.md, the receipt (sha 119500b2..., 89/0). Hand-verified: the rate identity d/dt(d0^T E) = d0^T(a2 d0 phi + u_E E + r C^T B) = a2 (d0^T d0) phi + u_E (d0^T E) + r (C d0)^T B, the last term zero by the chain identity; the unobservable-subspace chain P G x = a2 L phi, P G^2 x = a a2 L (d0^T E), P G^3 x = a a2^2 L^2 phi (u = 0), whose common kernel inside the zero-charge surface is {phi constant, d0^T E = 0} because ker L = constants on a connected torus; the sector dimensions from the counts: side 6, ker d0^T has dimension 81 - 26 = 55, so the electric-only invariant subspace is 55 + 1 + 81 + 27 = 164 and the two-row sector 55 + 1 + 55 + 1 = 112 (side 4: 17 + 1 + 24 + 8 = 50 and 36); the charged-surface impossibility (a zero-sum nonzero charge is not constant, so L rho_V != 0 and the charge moves); the coin cut from the blockwise skew equations (diagonal onsite entries vanish, one skew mixing per role, K free: 6) and the rows' action on it ((Theta_E (x) d0^T) E, cutting theta_E only: 6 -> 4); the hidden-time identity from z = z1 + i z2, z' = G z + i theta z: z2 = (G z1 - z1')/theta and z1'' = 2 G z1' - (G^2 + theta^2) z1; the -G^2 blocks of the three-speed member (E-block 4 d0 d0^T + C^T C with longitudinal eigenvalues 4 x {3, 6, 9} at counts 6/12/8, sum 81) and the sector multiplicities {0:3, 3:12, 6:24, 9:16} summing to 55. Quote fidelity re-verified against the live PR bodies: #7893's "record-diagonal relation at each corner" and "G_v = (div E)_v - rho_v is pure Z ..." sentences, #7917's "Split-step and enlarged-state exact ticks remain live." and its head-branch item-7 line — all verbatim. Supervisor findings: (F-B3-1, upstream) the primary's quote-fidelity flag is confirmed — block 01's ledger row 4 presented a précis as #7893's words; corrected on the block-01 branch and pushed to #7976 (post-open correction 2 in the meta note's Review record); the block-03 contract carried the same phrase and now carries a correction header. (F-B3-2, minor) the runner's section-I check that "the sector spectrum does not depend on the vertex and cube speeds" tests 4 d0 d0^T C^T = 0, i.e. vanishing on im C^T only, while the statement is about ker d0^T (on which d0 d0^T vanishes by definition); the statement is immediate, the executed test is narrower than its label — to be tightened in the fold if the checker concurs. No defect in the collapse theorem, the coin residual or the witnesses.

## 2026-09-05 — block 03 refuting checker (Opus 5) verdict and the fix pass
CHECKER_block03_findings.md (commit 6d64a13872): FIX FIRST, no verdict refuted; disjoint machinery (lexicographic layout, flipped signs, Levi-Civita curl, signed orbit counting, rate functionals solved, two-prime ranks); 74 independent checks; the collapse theorem and the coin residual reproduced; 15 axiom quotations and 5 PR quotations verbatim; 7/7 N4 ledger statuses; receipt pin re-verified. Every finding verified by the supervisor before applying:
- CK-01 (medium) VERIFIED against #7917's item 5 as quoted in block 02 ("the edge-to-face map is invariant under A -> A+d_0 lambda and preserves the magnetic Gauss row"): only the magnetic row is a class item. Fix: section 1, the consequence bullet, next_trace_action and the Imports row attribute the electric row to the lane's supply (#7893/#7903; used by #7917's section-6 mode count, not declared among its seven items); the verdict rows were already stated on the electric row explicitly.
- CK-02 (medium) VERIFIED by the runner's own construction (even translations via translation4's assertion; rotations about the origin vertex). Fix: claim_scope, the EC premise, the section-3 theorem and the first falsifier state the group as the even (sector-preserving) translations and the 24 proper rotations about a vertex-role site; the checker's five-dimensional self-dual class under the odd shift is recorded.
- CK-03 (medium) VERIFIED by grep (no capacity computation in the 89 checks). Fix: dim_R M_2(C) = 8 executed in runner section J; R7 marked ATTEMPTED (executed here); section 11 and N7 reworded.
- CK-04 (low-medium) VERIFIED (the doubled law is a stipulation). Fix: OL-coin named in the EC premise with the checker's twelve-dimensional alternative recorded; section 7 says stipulation, not finding; a falsifier bullet added.
- CK-05 (low) VERIFIED algebraically (K = U Sigma V^T decouples K (x) C into Sigma (x) C copies). Fix: executed as an exact SVD over QQ(sqrt 5) for the witness (runner section J); section 7 and the result table say the SF-all residue is decoupled copies and a coupled coin survives only the zero-charge reading.
- CK-06 (low) VERIFIED (invariance of the zero-charge surface alone cuts a2 but not u_E). Fix: SF-zero named in section 1; section 7 reworded.
- CK-07 (low) VERIFIED. Fix: the branch sentence and the runner label reworded ("a further branch").
- F-B3-2 (supervisor, minor): the sector-independence test now runs on a basis of ker d0^T and ker d2.
Fix-pass runner: TOTAL: PASS=91 FAIL=0 (89 + 2 executed checks, one tightened); cache re-pinned (sha aeabf99a...). The note's Review record carries the checker's verdict, its mutations and the independence class (cross-model). Disposition: pass after the fix pass.

## 2026-09-05 — block 03 conformance gate (REVIEW_LOOP_PR_CONFORMANCE_SPEC sections 1-12), recorded before the PR
1 self-containment — PASS: one markdown link (the landed axiom memo); the runner declares one input (the memo); PR numbers are evidence addresses; block 02 is quoted at scope as an evidence address, and the one fact previously leaned on from it (the capacity bound) is now executed here.
2 cache/execution — PASS: receipt pinned to runner sha aeabf99a... (timeout 900 declared and pinned; status ok, exit 0, 53 s); read inventory stated; re-pinned after the last runner edit.
3 claim-scope honesty — PASS after CK-01/CK-02: the symmetry group is stated exactly (even translations, rotations about a vertex); the electric row is attributed to the lane's supply, not to item 5; the three readings of support forcing are named; status fields from their enums (bounded-support / bounded_theorem); no coined tier word.
4 N-gate — TRIGGERED and PASSED at scope: N1-N8 in section 12; route R7 executed here (CK-03); the negatives scoped to the supplied rows under the named readings; the N5 certificate lines in the cached stdout.
5 proof obligations — PASS: the collapse theorem carries its hypotheses (the rate identity, d0^T d0 != 0, connectedness, conservation); the coin residual is a supply with two executed witnesses and the decoupling statement (CK-05) executed; no circular reduction (block 02's verdicts and #7917's class are never premises; EC and CONS are restated).
6 runner validity — PASS: fourteen primary mutations at the pre-fold sha, the checker's three plus one fidelity probe, all caught; supervisor independent-math checks (rate identity, unobservable-subspace chain and dimensions, coin cut, hidden-time identity, sector multiplicities from the momentum census).
7 packet completeness — PASS: single primary runner; no helper runner; no registry edit.
8 links/graph — PASS: manifest regenerated on the final tree and staged: +1 node (this note), +1 edge (to the axiom memo), 4762 -> 4763 nodes, 11861 -> 11862 edges, stable on a second regeneration; repo_invariants_check --check --enforce-links PASS with the manifest staged.
9 note structure — PASS: frontmatter, machine-status block with every mandated field, Imports, N1-N8, falsifiers, Review record with the independence class and the checker's mutations.
10 propose/ratify — PASS: no audit field written; the manifest is the only generated artifact staged; generated audit outputs not touched (no pipeline run in this block: the note seeds through the manifest and the nightly).
11 sourced facts/counts — PASS: every count measured by the runner at HEAD; the PR quotations re-verified against the live bodies by the primary, the checker and the supervisor; the pack's own précis (ledger row 4, contract) corrected upstream and annotated.
12 pre-review gates — vocab_lint --fix then --report-only: 0; audit_lint --strict: OK; git diff --check: clean; py_compile: ok; explicit-path staging; cold read of the complete note and runner by the supervisor.
Independence class disclosed: single family (Claude), cross-model — Fable primary, Opus 5 refuting checker on disjoint machinery, supervisor hand-verification.
