# Block 05 — PRIMARY SEAT (Fable): the Pickard structure of the monotone-order formation law (hard budget 120 minutes)

Your complete science contract is `GOAL_block05.md` in this pack, INCLUDING its addendum after the contract lens (read all of it first). The supervisor's exact controls `specs/supervisor_control_block05_pickard.py` (~15 s) and `specs/supervisor_control_block05_snake.py` (~25 s) already confirm every number; read them, do not import them.

## Hard operating rules (seats have died on each of these)
- Work only inside the worktree `W = /Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/sync-science-task-0c8fac` (branch `physics-loop/admissibility-induced-law-block05-pickard-structure-monotone-class-20260907`, stacked on block 04's branch; blocks 01–04's notes and runners are in the tree) and the scratch directory `S = /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/primary05` (`mkdir -p`).
- NEVER: `rm -rf`, sandbox copies of the repo, any path outside W and S, `git stash`, `git checkout`, `git reset`, `git clean`, `git add -A`, `git push`, editing any tracked file you did not create; in the pack you may write only `RESULTS_block05.md` and append a section to `REVIEW_HISTORY.md`.
- OUTPUT DISCIPLINE: no single tool call may write more than 250 lines; commit after every coherent append with explicit paths and the prefix `ail05:`. Reads ≤ 250 lines per call. Every Bash call under 10 minutes; long runs in the background writing to S, polled.
- Budget 120 minutes; at 100 minutes stop adding and certify.
- Exact arithmetic only: `fractions.Fraction`, Python ints (`sympy` only if needed). No `float`, `numpy`, `nsimplify`, `evalf`, `N(`. The runner self-scans its source as blocks 01–04 do. Integer numerators over common denominators in the hot loops (the `3 × 3` row-transfer contractions with `216^3` terms take ~10 s with Fractions; keep the baseline under 300 s).
- The lane's forbidden-phrase scan is a SUBSTRING match: never write "certified"/"uncertified" (use "verified"), "phase transition", "several static laws", "the physical order", "washes out"; the name "Pickard" only inside the `## Prior art` and `## Imports` sections.

## Read caps
1. This pack: `GOAL_block05.md` (complete, with the addendum), this spec, the two controls.
2. Block 02's note (Premises; Theorem E complete) and block 01's note (Premises; the formation-law definition; Theorem B).
3. Block 04's runner `W/scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py` — the lane format only (check class, mutation gate, N5 lines, float scan, `dec()`); do NOT import it.
4. `W/docs/MINIMAL_AXIOMS_2026-06-29.md` — COMPLETE.
5. `W/docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` sections 3, 4, 5, 9.
6. `python3 scripts/vocab_lint.py --report-only <note>` before every note commit.

## Deliverables (exact paths; write incrementally; commit each)

### 1. The runner — `W/scripts/admissibility_rule_monotone_order_formation_law_pickard_rows_columns_corner_law_2026_09_07.py`
Lane format (`AUDIT_TIMEOUT_SEC = 900`; `AUDIT_INPUT_PATHS = (the block-05 note, "docs/MINIMAL_AXIOMS_2026-06-29.md", the block-01 note, the block-02 note)` as a pure literal tuple; check class; `--list-mutations`, `--mutation NAME`, `MUTATION_GATE`, expected/observed lines; N5 lines; unmutated stdout under 6,000 characters; baseline under 300 s; `--exact` prints the exact laws and defects).

Check families:
- **A authority/inputs.** The four declared inputs exist; the two Admissibility sentences and the Record sentences verbatim; block 01's and block 02's claim ids with a fragment each (block 02: `p_0 P = p_0`); this note's claim id.
- **B the class (P1).** Enumerate the linear extensions of `2×3` (`5`), `3×3` (`42`), `3×4` (`462`) by your own recursion; count `4×4` (`24024`) by memoized recursion; for every extension and every site the recorded set equals `{left, above} ∩ rectangle`; the full formation laws (block 01's definition, all `6^6` configurations) of the `5` extensions of `2×3` coincide; a NON-monotone order (the snake) has a different recorded set at a declared site.
- **C the bridge and the transpose (P2, P3).** `r(s | a, b) = K(a→s)K(s→b)/(K^2)(a,b)` on all `216` triples at both declared triples; `β(s|a,b) = β(s|b,a)`; `μ_P^{2×3}(v) = μ_P^{3×2}(v^T)` on every configuration; the product formula of P2 equals block 01's definition on `2×3` entrywise.
- **D rows, columns, the corner law (P4, P5).** By the row transfer (`p_0`, `P` from block 02's E2, rebuilt): every column of `3×3` is the `K`-chain (three-site joint); every column of `2×3` and every row; the `2×2` corner law `π` at every block position of `3×3` (four positions; the addendum's instruction if the lens found that lower rows need care) and at all three positions of the two-row joint at `W = 4`; the corner conditional independence `P(a, b | c) = K(c→a)K(c→b)` and the bridge conditional of `d`; the diagonal pair `(a, b)` law `(1/6)K^2` (E4) recovered from `π`.
- **E the boundary of the structure (P6, P7).** The two staircases of `3×3` are not `K`-chains: the exact total-variation defect from the `K`-chain printed as a decimal label; whether each is a Markov chain with some kernel (report, executed: the conditional of the last site given the previous two varies with the earlier one or not); the mirror class's law differs from `μ_P` on `2×3` (exact TV); the snake's rows are `p_0` and its vertical pairs `(1/6)K` (with `P_rl`, `p_0 P_rl = p_0` executed on all `216` row states of `W = 3`), and its columns `0` and `1` of `3×3` are not `K`-chains while column `2` is (exact defects).
- **F fences/forbidden.** The note's fence sentences verbatim; forbidden phrases absent; "Pickard" only in Prior art/Imports (split on `## ` headings); float self-scan; mutations `claim_static_equals_formation`, `claim_all_orders_same_law`, `claim_staircases_chains`, `claim_pickard_in_theorem`.
- **G certificate.** N5 lines and the total.

Declared mutations (≥ 20, each in exactly one family): e.g. `extension_count_wrong`, `recorded_set_forged`, `nonmonotone_order_accepted` (B); `bridge_identity_broken`, `transpose_symmetry_broken`, `product_formula_mismatch` (C); `column_chain_forged`, `corner_law_wrong_denominator`, `corner_independence_forged`, `diagonal_pair_law_wrong`, `row_kernel_wrong` (D); `staircase_claimed_chain`, `mirror_law_equal_claimed`, `snake_column_claimed_chain`, `snake_row_kernel_not_invariant` (E); the four F mutations. Census: one helper invocation per mutation, 4 in parallel, table from raw stdout into `RESULTS_block05.md`.

### 2. The note — `W/docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_PICKARD_ROWS_COLUMNS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md` (≤ 600 lines)
Front matter as blocks 01–04 (`claim_id: admissibility_rule_monotone_order_formation_law_pickard_rows_columns_corner_law_bounded_theorem_note_2026-09-07`, `claim_type: bounded_theorem`, `claim_scope` covering P1–P7 at scope, `upstream_dependencies: [minimal_axioms, block 01's claim id, block 02's claim id]`, `runner`). Title: `# The formation law of every monotone order is one law whose rows and columns are path chains: the corner law, the class, and its boundary`. Sections in the lane's order: Result up front (the layman's paragraph FIRST and symbol-free: lay records down in any order where each site waits for the one above and the one to its left; every such order gives the same pattern law; in it every row and every column looks exactly like a single chain of records, any 2×2 square has one explicit law in which the two sites next to a corner are independent given the corner, but a zigzag path is not a chain; orders that don't wait — the snake — keep the rows but break the columns; then the exact paragraph; machine status; Premises (restate; the partial order; the class); Prior art (blocks 01–02; the classical unilateral Markov field literature referenced by its author's name once in Prior art and re-proved at scope; the contract lens's survey as the origin); Exact target and obligation graph; Theorems P1–P7 with proofs (P1 two lines; P2 from E1; P3 the product formula's symmetry with the boundary conventions written; P4 via E3 on the transpose plus the infinite-strip and quadrant sentences; P5 the full partial-sum proof with the lower-rows step; P6, P7 as executed witnesses with exact defects and the reason for the turning column); No-Go Discipline Gate (the only negative sentences are the executed witnesses P6/P7, finite statements: answer N1–N8 briefly); Falsifiers; Boundaries with the fences; Imports; Review record ("Fable primary seat; contract lens: folded (list); refuting checker: pending"); Verification.

Note fences (verbatim; in Boundaries):
- `This note describes the formation law of the monotone-order class on finite rectangles, the infinite strip and the quadrant; it states nothing about the static law beyond block 01's and block 02's separation, and nothing about orders outside the class beyond the executed snake and mirror witnesses.`
- `No order is selected as physical; no plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.`
- `The unilateral Markov field of the literature is a reference re-proved here at the scope used; no value, constant or theorem is imported as authority.`

### 3. Cache — via `execute_and_write_cache(<runner>, 900)`; re-run after any edit.
### 4. `RESULTS_block05.md`: headline; run record; defects fixed; could-not list; modelling choices; exact laws and defects (from `--exact`); certified stdout; mutation table.
### 5. `REVIEW_HISTORY.md`: append `## block 05 — V1-V5 (primary)`.

## Science discipline
- Control first: reproduce the bridge identity, the `5`-extension law equality on `2×3`, the `3×3` column chain, the corner law at one block, and the staircase defect in your own code before any theorem sentence; if any differs, stop and report.
- Every theorem sentence carries its proof or its executed witness; P6/P7 are witnesses, never generalized.
- Raw final report (≤ 30 lines): headline in three sentences, certified totals and elapsed time, mutation census summary, the exact defects, could-not list, commit shas.
