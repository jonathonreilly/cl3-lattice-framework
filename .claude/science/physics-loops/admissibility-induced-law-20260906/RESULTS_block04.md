# RESULTS — block 04 (supervisor-authored, Fable; Opus refuting checker), 2026-09-07

## Headline

The two-site block criterion is silent at the three silent triples for every coupling of the block laws. The pair block's `x`-marginal is essentially as sensitive to an outer slot as a lone site (`ρ/c_1 = 0.9992, 0.9804, 1.0024` at `(3,1,2)`, `(5,2,4)`, `(7,3,5)`), and any coupling disagrees at each site at least as often as that site's marginal total variation (Theorem N), so the block sum `B_V ≥ 10(ρ + ρ') = 3.2457…, 2.4323…, 2.4470… > 2 = |V|`. The block law factors across the pair under a change at an `x`-slot (Theorem O, executed on all 476,280 instances at `(3,1,2)`); the explicit sequential coupling gives `B_V ≤ 10ρ(1 + c_1)`; the finite-window block-scan contraction (Theorem M) is proved with its `Z^3` implication explicitly left open and nothing claimed from it. Along the lines the two-site number crosses 1 in the same scan cell as `6c_1`.

## Run record

- Runner `scripts/admissibility_rule_two_site_block_criterion_exact_silent_for_every_coupling_2026_09_07.py`: `TOTAL: PASS=21 FAIL=0`, 16 declared mutations, unmutated stdout 3,890 characters, baseline 39.2 s.
- Cache: runner sha256 `8609e76702f123cf75f5f59615303fcc898b8285c62a3496619e5b5edc212089`, input fingerprint `994dcebd50c5e9a429d6e093a7f1ac741a5cda2f632053f54dddab9dc5fb905f`, exit 0, elapsed 39.16 s.
- Note: 429 lines; `vocab_lint --report-only` 0 violations.
- Seat profile: the supervisor's controls (`specs/supervisor_control_block04_two_site.py`, `specs/supervisor_control_block04_lines.py`) computed every number before the contract; the note and runner were written by the supervisor; no primary seat and no contract lens (the mathematics is one page and the controls settled the block's size); the Opus refuting checker is the independent seat.

## Defects fixed while executing

- The lane's forbidden-phrase scan (E2) caught "several static laws" in the N1 route table and "phase transition" in the machine-status reason and in N8; reworded ("more than one static law", "a transition").

## Could-not list

- `W_1` is bounded above and below, not computed exactly (the checker computes it on instances).
- Theorem M's `Z^3` implication (a block-level per-site decay) is not proved; nothing on `Z^3` is claimed from the block contraction.
- No threshold of the two-site number is isolated on the lines; the scans are pointwise.
- The silent triples remain undecided in both directions.

## Modelling choices (declared, not physics)

- Menu order and orbit weights as in blocks 01–03; the pair block `V = {x, x + e}` with `∂x` (five slots) and `∂y` (five slots); the sensitivities as suprema over the `252 × 126` multisets and the `15` pairs at the varied slot.
- The declared instance family: 200 LCG instances (seed 20260907, multiplier 1103515245, increment 12345, modulus `2^31`, eleven draws, `(state >> 16) mod 6`, distinct pair required) plus the maximizing instance at `(3,1,2)`.
- The sequential coupling: `x` by the maximal coupling of the marginals, then `y` by the maximal coupling of the conditionals given the coupled `x` values.
- Line scans at `t = k/20`, `k = 21..39`.

## Exact values (runner stdout)

- `ρ`: `(3,1,2) 2168397/7948400`; `(5,2,4) 271059507090000/1298168979740633`; `(7,3,5) 239957740750/1121635870169`; `(2,1,2) 67715/446034`; `(3,2,2) 1471549788/11145302999`; `(5,4,4) 81847628000000/1305850357630907`.
- `ρ'`: `(3,1,2) 1350/26077`; `(5,2,4) 1915425000/55627392667`; `(7,3,5) 856455908/27833079009`.
- `B_V` bounds at the silent triples: `[3.2457, 3.4728]`, `[2.4323, 2.5327]`, `[2.4470, 2.5959]`; the sequential upper bound at the region triples: `1.7517`, `1.4966`, `0.6676`.
- Lines: both crossings in `(8/5, 33/20)` on `(t,1,1)` and in `(29/20, 3/2)` on `(t,t,1)`; `ρ/c_1 > 1` from `t = 39/20` and `t = 3/2`.

## Mutation census (16 mutations, one helper invocation each, 4 in parallel; expected/observed read from raw stdout at the final runner sha 8609e767…)

| mutation | expected | observed | FAIL count | failing checks | exit | in-family |
|---|---|---|---|---|---|---|
| `block_law_factorization_broken` | B | B | 1 | B1 The | 1 | yes |
| `coupling_marginals_broken` | B | B | 1 | B2 the | 1 | yes |
| `lower_bound_lemma_forged` | B | B | 1 | B3 The | 1 | yes |
| `sequential_upper_bound_forged` | B | B | 1 | B4 seq | 1 | yes |
| `rho_literal_off` | C | C | 1 | C2 rho | 1 | yes |
| `rho_prime_literal_off` | C | C | 1 | C4 rho | 1 | yes |
| `ratio_bounded_by_one_claimed` | C | C | 1 | C3 rho | 1 | yes |
| `silent_lower_bound_below_two` | C | C | 1 | C5 The | 1 | yes |
| `region_upper_bound_forged` | C | C | 1 | C6 the | 1 | yes |
| `c1_literal_off` | C | C | 1 | C1 c_1 | 1 | yes |
| `crossing_cell_wrong` | D | D | 1 | D1 the | 1 | yes |
| `ratio_beyond_one_denied` | D | D | 1 | D2 rho | 1 | yes |
| `claim_two_site_decides` | E | E | 1 | E2 the | 1 | yes |
| `claim_nonunique_at_silent` | E | E | 1 | E2 the | 1 | yes |
| `claim_phase_transition` | E | E | 1 | E2 the | 1 | yes |
| `claim_author_in_theorem` | E | E | 1 | E3 the | 1 | yes |
in-family: 16/16

## Refuting checker and the fold (2026-09-07) — final certificate

- Checker (Opus 5, disjoint machinery; `CHECKER_block04_findings.md`; spec `scratchpad/checker04/checker_spec_block04.md`): **FIX FIRST** — the conclusion held but the first draft's inequality `b_V(z) ≥ ρ + ρ'` was false: it added two separate suprema attained at different instances (the wrong direction), so the three headline numbers `3.2457, 2.4323, 2.4470` were false, and the draft's own sequential coupling already bounded `B_V` below them (`3.2456, 2.3034, 2.4449`). The checker proved, and verified on 5,406 exact min-cost-flow transport solves, that `W_1 = TV(m_x) + TV(m_y)` exactly for a change at an x-slot, giving the exact block sums `152203860/48008647 = 3.1703…`, `124859962305/55627392667 = 2.2445…`, `14627647143900/6157201570091 = 2.3756…` (all still `> 2`). Also found: the N7 per-site figures in the wrong order and built on the invalid quantity; Theorem M's "iff" one-sided. Everything else held: all `c_1`, `ρ`, `ρ'`, ratios, maximizers, Theorem O on all 476,280 instances, the ∂y-slot symmetry (checked by enumeration), both line scans, fences, forbidden phrases, author names; the runner 21/21 with 12 mutations in family; the cache sha reproduced. Runner blind spot named by the checker: C5 tested the note's stated number, not a `W_1` quantity.
- Supervisor control before the fold (`specs/supervisor_control_block04_after_checker.py`): the three exact block sums reproduced digit for digit; `σ` at the three region triples computed (`14803/90094`, `31495356/211495159`, `261542884000000/3917551072892721`); the disjoint-support coupling built and verified on 300 instances at `(5,2,4)` (exact marginals, `E d_H = TV(m_x) + TV(m_y)` on every one).
- Fold: runner — `sigma_of` (one supremum of the sum), `optimal_coupling` (the disjoint-support construction), checks B4 (equality on every instance, never above the sequential coupling) and C5/C6 (exact `B_V = 10σ` against the literals; `σ ≤ ρ + ρ'` and `≤ ρ(1 + c_1)`), mutations `block_sum_literal_off` and `optimal_coupling_not_optimal`; note — Theorem N's consequence corrected, Theorem N' added with its proof, the `σ` column and exact `B_V` throughout, the N7 figures `1.5852, 1.1223, 1.1878`, Theorem M reworded as sufficiency, Boundaries, Falsifiers, Review record; the contract `GOAL_block04.md` carries an addendum.
- Final certificate: `TOTAL: PASS=22 FAIL=0`; runner sha256 `50b47ce6041d0b4bfdfe798de577965f749b7c118ff567f144d6b406b13d7652`; input fingerprint `7ac6dc97ce219f64436a2e5ad46b7da83ff1a09f828f230e176bc8a5e83ecec6`; exit 0; elapsed 52.9 s; unmutated stdout 4,068 characters; note 483 lines, vocab lint 0; 17 mutations, census re-run at this sha (table below).
