# HANDOFF — u1-maxwell-landing-core-20260905 (campaign start 2026-09-04T21:04+00:00)
State: block 01 launched (sol primary drafting the landing core + meta note + ledger). Supervisor: this session; independent sol checker for quote fidelity against inputs/. Next: review, checker, conformance gate, PR off main; then block 02 from the ledger ranking.

# DEGRADED WORKER MODE (2026-09-04T21:32+00:00): the gpt-5.6-sol seats died at the codex account usage limit (reset Sep 6 22:27); block continues on Fable worker seats (single-family) under the workhorse robustness conditions: refuting checker on disjoint machinery, mutation probes, supervisor hand-verification; independence class = cross-context; disclosed in the note/receipt/PR. Sol narration salvaged to specs/SALVAGE_sol_primary_narration.md as untrusted draft input.
# WORKER PROFILE UPDATE (owner 2026-09-05): Opus 5 seats permitted for physics work conditional on supervisor checking; profile = Fable primary + Opus blind/refuting seats (cross-model within family) + supervisor line-by-line.

## 2026-09-04T22:17+00:00 block 01 close
Deliverables: LANDING_CORE.md, docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md, SUPPLIED_INPUT_LEDGER.md (+ blind ledger, checker findings). Checker FIX FIRST -> fix pass applied -> disposition pass. PR opens after the pipeline gate and manifest; then block 02 (ledger row 1). Worker profile: Fable primary / Opus checker + blind seat (cross-model, single family).

## 2026-09-04T22:35+00:00 block 01 PR opened; block 02 in flight
PR #7976 — "[physics-loop] u1-maxwell-landing-core block01 — meta — open" — base main, head this branch (f4503630df + this checkpoint). Pipeline gate: full rerun on the final tree exit 0; manifest byte-identical on regeneration (4761 nodes / 11860 edges). The raw codex seat log was dropped from the branch tip at close (salvage narration kept; history retains the stream at 75b4ad0649).
Block 02: worktree .claude/worktrees/loop-u1-block02, branch physics-loop/u1-maxwell-landing-core-block02-dynamics-class-20260905 stacked on this branch at 7bcb2d6764 (one commit behind this tip: the close commit + this checkpoint — rebase onto this branch before the block-02 PR). Contract: GOAL_block02.md (be4fa51f32). Fable primary launched 2026-09-04T22:20+00:00; expected deliverables: scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py, docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md, RESULTS_block02.md, ROUTE_PORTFOLIO.md prior-art sweep. Then: Opus refuting checker, fold, V1-V5 (and N1-N8 if any family-level negative), conformance gate, PR stacked on #7976.
Resume rule for a fresh session: never merge #7976; review-loop is owner-operated. The lock (owner fable-supervisor) expires 2026-09-05T10:24+00:00; campaign budget ends 2026-09-05T09:04+00:00.

## 2026-09-05 block 02 (Fable primary) — deliverables written; awaiting supervisor/checker
Deliverables: scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py (95 exact checks; 12 mutations detected),
docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md (seven-row table; N1-N8 landed), RESULTS_block02.md,
ROUTE_PORTFOLIO.md sweep, REVIEW_HISTORY.md V1-V5 + conformance record. Findings: items 4 and 5 of the #7917 class are mutually
redundant (5 from 1,3,4,7+OL; 4 from 1,3,5,6,7); the sampling identification of the dynamics with Admissibility is dissipative;
the residual is payload+OL, time rule, locality (IP-B), conservation. Not pushed; PR to be opened by the supervisor stacked on
block 01 after the checker seat. Proposed weaving (later review): none.

Pipeline gate: pipeline exit=0 (2026-09-05, HEAD cb7e75702b); generated outputs restored. Block 02 complete on the worker side; not pushed.

## 2026-09-05T03:25+00:00 block 02 PR opened; block 03 launched
PR #7980 — "[physics-loop] u1-maxwell-landing-core block02 — bounded_theorem — bounded-support" — base = the block-01 branch (PR #7976), head = the block-02 branch at 11fdd471a5. Verification chain in REVIEW_HISTORY.md (supervisor review, Opus checker verdict, fix pass) and RESULTS_block02.md. Never merge; review-loop is owner-operated.
Block 03: worktree .claude/worktrees/loop-u1-block03, branch physics-loop/u1-maxwell-landing-core-block03-gauss-support-20260905 stacked on block 02; contract GOAL_block03.md; Fable primary launched 2026-09-05T03:25+00:00; expected deliverables scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py, docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md, RESULTS_block03.md, V1-V5 in REVIEW_HISTORY.md. Then: Opus refuting checker, fold, conformance gate, PR stacked on #7980.
Resume rule for a fresh session: three open PRs #7976 -> #7980 -> (block 03), each stacked on the previous; rebase a stacked branch onto its parent's tip before opening its PR; never merge any of them.

## 2026-09-05 block 03 (Fable primary) — deliverables written; awaiting supervisor/checker
Deliverables (commit 13accb8c03 on the block-03 branch, not pushed): scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py (89 exact
checks; fourteen mutations caught), docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md (four-row
obligation table; N1-N8 landed; one markdown link), the cached receipt, RESULTS_block03.md, ROUTE_PORTFOLIO.md sweep (zero matching
hits on origin/main e249016f75), REVIEW_HISTORY.md V1-V5. Findings: on the ten-dimensional covariant class (phi, E, B, psi) the
electric surface is invariant iff a2 = 0 and u_E rho_V = 0 (magnetic: b = 0, u_B rho_C = 0); with conservation the invariant members
are exactly the one-speed law with frozen, decoupled vertex and cube payloads in every charge sector; a vertex-coupled conservative
member has no invariant subset of any charged surface and, at zero charge, a Gauss sector with phi, psi constant on which it equals
the one-speed law (52 = 2 x 26 transverse modes; the longitudinal branch is inadmissible, not killed); the coin class is
sixteen-dimensional, conservation leaves six parameters, the rows cut only the two onsite mixings (never the second component);
block 02's complex law preserves the rows at zero charge only (a charged two-component charge rotates). Item 7 of #7917 splits:
vertex/cube half DERIVED-CONDITIONAL-ON(SF-all, EC, CONS); coin/hidden-time half GENUINE SUPPLY. Quote-fidelity finding for the
supervisor: the ledger row-4 / GOAL_block03 phrase attributed to PR #7893 is a précis (not in the live body or head note).
Next: supervisor review, Opus refuting checker, fold, conformance gate, manifest, PR stacked on #7980. Proposed weaving (later
review): SUPPLIED_INPUT_LEDGER row 4's derivability estimate ("partial, shape only") is now item-exact for the payload; a later
block could update the ledger row rather than this note.

## 2026-09-05T04:50+00:00 block 03 PR opened; lane campaign stop
PR #7984 — "[physics-loop] u1-maxwell-landing-core block03 — bounded_theorem — bounded-support" — base = the block-02 branch (#7980), head = the block-03 branch at 2cd0b6d546. The three PRs stack #7976 -> #7980 -> #7984; each carries its own verification chain (REVIEW_HISTORY.md, RESULTS_block0N.md, CHECKER_block0N_findings.md); never merge any of them — review-loop is owner-operated.
What the lane established this campaign, at scope: the landing core and supplied-input ledger (block 01, meta); the #7917 dynamics class adjudicated item by item — items 4/5 mutually redundant, the residual supply item-exact: payload with its transformation law, time rule, locality, conservation (block 02); the payload wall split — the vertex/cube half of item 7 folds into the supplied Gauss rows read as support forcing plus the class's items and conservation, while the coin and hidden time remain supplied, with the SF-all coin residue shown to be decoupled copies (block 03).
Next targets, for a fresh campaign (none launched tonight; reasons in STATE.yaml and OPPORTUNITY_QUEUE.md): (1) conservation — reflection positivity of a supplied transfer interpretation along a declared axis, carried to the payload level (does the reconstructed generator act on the edge/face payload or an enlarged one); (2) the one-component clause — the readout bridge from recorded values to one real coordinate per site (block 02's SI, #7915's W4); (3) the 3D photon origin — a sampler computation outside this format; (4) the time-selection fork (G2) at the linear level.
Resume rule: rebase a stacked branch onto its parent's tip before touching it; the lock (owner fable-supervisor) expires 2026-09-05T10:24+00:00.
