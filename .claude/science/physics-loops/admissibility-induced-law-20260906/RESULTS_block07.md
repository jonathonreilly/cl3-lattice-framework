# RESULTS — block 07 (supervisor-authored, Fable; Opus refuting checker), 2026-09-07/08

## Headline

On a self-made Hermitian positive-definite nearest-neighbor precision `P` (Gaussian rationals; `P_xx = 3`, horizontal `(1 + 2i)/4`, vertical `(2 − i)/4`; and a real instance with `1/2` on every edge), the records-only formation law along any order is the complex Gaussian with precision `P_σ = L_σ† D L_σ` and normalizer `Π P_kk` (G1); `P_σ` depends on the order only through the recorded sets, so the monotone class gives one law (G2: 24 plaquette orders in 14 classes, the 5 monotone orders of `2×3` one law, the snake and mirror different); `P_σ = P + diag(c) + F_σ` with corrections `c_x = Σ |P_kx|²/P_kk` and fill-in on pairs recorded together, so `P_σ ≠ P` on every window with an edge (G3(a), a theorem for every finite graph); at most one recorded neighbor per site implies `P`'s support is kept (G3(b) forward, a theorem), the converse holding on the declared grid instances and failing in general (the checker's witnesses, executed); `det P_σ = Π P_kk > det P` unless `P` is diagonal (G4, Hadamard); the static marginal, pinned-static conditional and formation read-slice covariances of the `2×3` bottom row are pairwise different (G5).

## Run record

- Runner `scripts/admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_2026_09_07.py`: `TOTAL: PASS=25 FAIL=0`, 19 declared mutations, unmutated stdout 4,025 characters, baseline 1.8 s (sympy exact arithmetic over `Q(i)`).
- Cache: runner sha256 `19254f5f535645be9a30944aaf3a3b3241174e8dc95cb8420ee102f5e3074c5f`, input fingerprint `8375780418b4b24a55a0fe066514883452b8ef4c8699154ca850a8150fe1f2d3`, exit 0, elapsed 1.78 s.
- Note `docs/ADMISSIBILITY_RULE_HERMITIAN_GAUSSIAN_INSTANCE_FORMATION_PRECISION_LDL_BOUNDED_THEOREM_NOTE_2026-09-07.md`: 430 lines; `vocab_lint --report-only` 0 violations.
- Seat profile: the supervisor's control `specs/supervisor_control_block07_gaussian.py` (with output) computed every number before the contract; note and runner supervisor-authored; the Opus refuting checker the independent seat.

## Defects fixed while executing

- The runner's term-by-term quadratic form had a stray transpose (caught by B2 against `L† D L`).
- Two forbidden tokens collided with the note's own words ("the bridge" inside "no bridge statement is claimed"; "certif" inside "resolution certificate"); tokens tightened to "the Bridge weights", "the Bridge conjecture", "certified".
- The mutation `monotone_class_split` leaked into families C and E through the shared report object (census 17/18); localized to B5 (census 19/19).

## Could-not list

- The converse of G3(b) and G3(c) are grid/instance statements, not theorems for every graph (the checker's witnesses mark the boundary).
- G5 is an executed instance on `2×3` only.
- The instance's off-diagonal entries are one value per edge direction; G1–G4 are stated for general Hermitian positive-definite nearest-neighbor `P`, executed on the two instances.
- Nothing about any external fixture, committed action or bridge.

## Modelling choices (declared, not physics)

- Complex record variables; the complex Gaussian density `(a/π) exp(−a|z − m|²)`; the rule's mean `−(1/P_xx) Σ_{y∼x} P_xy z_y` and variance `1/P_xx`; the records-only reading restricts the sum to the recorded neighbors.
- Windows: the path `1×3`, the plaquette `2×2`, the rectangle `2×3`; orders: all 6 and 24 for the path and plaquette; the 5 monotone orders, the snake and the mirror of `2×3` (two orders for G1).
- The read slice: row 1 of `2×3` with row 0 pinned for the pinned-static object.

## Exact values

- Correction per recording neighbor at the declared instance: `|P_kx|²/P_kk = (5/16)/3 = 5/48`; `2×3` monotone corrections `[5/24, 5/24, 5/48, 5/48, 5/48, 0]`; fill-in on `((0,1),(1,0))`, `((0,2),(1,1))`; path end-to-end corrections `[5/48, 5/48, 0]`.
- `det P`: `201/8`, `279/4`, `2285299/4096` (declared) and `51/2`, `72`, `37835/64` (real), against `Π P_kk = 27, 81, 729`.
- Formation row-1 precision block diagonal `149/48, 149/48, 3` against `3, 3, 3`; the three read-slice covariances printed under `--exact`.
- The checker's witnesses (C6): plaquette with `P_cd = −1/2`, order `(a, d, b, c)`: `P_σ = P + diag(1/6, 0, 0, 1/6)`; `K_3` with `1/2` on every edge: fill-in on an edge; the triangle `[[3, 1/4, 1/2], [1/4, 3, −3/2], [1/2, −3/2, 3]]`: the `(0,1)` entry of `P_σ` vanishes.

## Refuting checker and the fold (2026-09-08)

- Checker (Opus 5, disjoint machinery; `CHECKER_block07_findings.md`): FIX FIRST on one theorem — G3(b)'s "only if" false in general (three exact witnesses, one on the note's own plaquette window); a mutation leak; three cosmetic items. Everything else confirmed: the conditional densities integrated in real coordinates, the 14 classes and 62 cases, the Schur pivots `[3, 139/48, 402/139, 18601/6432, 51558/18601, 2285299/824928]`, the three covariances by its own elimination, and the pinned-static conditional precision derived as `P_11` (the attack on G5(ii) failed).
- Fold: G3(b) restated as a sufficient condition with the converse executed on the declared grid instances; G3(c) as a bipartite statement; the witnesses executed (C6) with the mutation `cancellation_witness_denied`; the scope lines, the Gershgorin sentence and the G5 heading corrected; `GOAL_block07.md` carries the addendum.
- Final certificate: `TOTAL: PASS=25 FAIL=0`; runner sha `19254f5f…`; 19 mutations, census 19/19 in family at that sha (table below).

## Final census (19 mutations, one invocation each; expected/observed read from raw stdout at the final runner sha 19254f5f…)

| mutation | expected | observed | FAIL count | failing checks | exit | in-family |
|---|---|---|---|---|---|---|
| `pd_certificate_forged` | B | B | 1 | B1 bot | 1 | yes |
| `quadratic_form_mismatch` | B | B | 1 | B2 G1: | 1 | yes |
| `normalizer_wrong` | B | B | 1 | B3 G1: | 1 | yes |
| `class_equality_broken` | B | B | 1 | B4 G2: | 1 | yes |
| `monotone_class_split` | B | B | 1 | B5 G2: | 1 | yes |
| `separation_formula_wrong` | C | C | 1 | C1 G3: | 1 | yes |
| `support_condition_forged` | C | C | 1 | C3 G3( | 1 | yes |
| `fillin_pairs_wrong` | C | C | 1 | C5 G3( | 1 | yes |
| `correction_literal_off` | C | C | 1 | C4 G3: | 1 | yes |
| `equality_with_static_claimed` | C | C | 1 | C2 G3( | 1 | yes |
| `cancellation_witness_denied` | C | C | 1 | C6 the | 1 | yes |
| `hadamard_reversed` | D | D | 1 | D1 G4: | 1 | yes |
| `hadamard_equality_case_wrong` | D | D | 1 | D2 G4: | 1 | yes |
| `read_slices_equal_claimed` | E | E | 1 | E1 G5: | 1 | yes |
| `conditional_block_equal_claimed` | E | E | 1 | E2 G5: | 1 | yes |
| `herm_inverse_commutes_claimed` | E | E | 1 | E3 G5 | 1 | yes |
| `claim_lane_fixture` | F | F | 1 | F2 the | 1 | yes |
| `claim_formation_equals_static` | F | F | 1 | F2 the | 1 | yes |
| `claim_bridge` | F | F | 1 | F2 the | 1 | yes |
in-family: 19/19

Gates on the final tree: pipeline PASS (`graph_delta=acknowledged`), changed-evidence `checked=7 failures=0`, audit_lint strict OK, diff --check clean, manifest 4767 nodes, 11873 edges (+1 node).
