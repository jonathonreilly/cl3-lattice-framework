# Block 07 — independent refuting checker findings (Hermitian Gaussian instance, L†DL)

## 1. VERDICT

**FIX FIRST** — two fixes required before landing, three cosmetic.

1. **[MAJOR] `G3(b)`'s "only if" is FALSE as stated at the note's declared generality** (every Hermitian
   positive-definite nearest-neighbor precision on every finite graph). Refuted by three exact
   counterexamples, one of them **on the note's own 2×2 plaquette window**. The load-bearing wrong
   step is in G3's proof: *"the support of `F_σ` is exactly the set of pairs recorded together by
   some site"* (note line 265–266) — it is only **contained in** that set; a sum of fill-in terms
   can cancel. The forward direction, `G3(a)`, `G1`, `G2`, `G4` and every executed number are correct.
2. **[MINOR] "Each of the 18 declared mutations … fails in exactly one family" (note line 448–449) is
   false**: `monotone_class_split` fails B5, C5 **and** E2 (the runner's own output prints
   `mutation_family_expected: B`, `mutation_family_observed: BCE`).
3. Cosmetic: F3 (runner's forbidden list diverges from the GOAL's), F4 (Gershgorin modulus attributed
   to both instances), F5 (loose "pinned" framing of the three read-slice objects).

Not REFUTED: every executed statement of the note reproduces exactly under disjoint machinery, and the
note's own **Exact target** (line 183–187) already restricts the "every finite graph" promise to G1 and
G3(a) — so the fix is a scope correction, not a retraction.

## 2. CK table

| CK | verdict | exact numbers reproduced by my own machinery |
|---|---|---|
| CK-01 G1 | **CONFIRM** | Completing the square on 2×2 declared: `z†Pz − P_xx|z_x − m_x|²` is free of `z_x` with `m_x = −(1+2i)z_{(0,1)}/12 − (2−i)z_{(1,0)}/12`. Convention: `∫exp(−a\|w\|²)d²w = π/a`, so `(a/π)exp(−a\|w−m\|²)` is normalized and `E\|w−m\|² = 1/a` — the note's `(det P/π^N)`, `π^{−N}Π P_kk` and "variance `1/P_xx`" are mutually consistent. Product-of-densities exponent (built in **real coordinates**, never from `L†DL`) `=` `z†(L†DL)z` on **60** (instance, order) cases (path 6 + plaquette 24, ×2 instances) plus 2×3 row-major and snake. `det P_σ = Π P_kk` = 27 / 81 / 729 on 1×3 / 2×2 / 2×3, both instances. |
| CK-02 G2 | **CONFIRM** | 24 plaquette orders → **14** recorded-set classes; `P_σ` constant on each (site-indexed); the 14 classes also give **14 distinct** `P_σ`. 2×3 has **5** monotone orders, all with recorded sets `{left, above}` and one common `P_σ`; snake and mirror both differ. Order-within-class does **not** matter: `P_σ = Σ_k P_kk · conj(v_k) v_kᵀ` with `v_k` determined by `(k, A_k)` alone — a one-line proof of G2 that the note's "simultaneous permutation" argument reaches indirectly. |
| CK-03 G3 formula/literals | **CONFIRM** | `P_σ = P + diag(c) + F_σ` on **62** cases (6+24+1 orders × 3 windows × 2 instances) — matches the runner's 62. `|P_kx|²/P_kk = (5/16)/3 = 5/48` for both edge directions. Path end-to-end corrections `[5/48, 5/48, 0]`, support kept; middle-out fills in the end pair. 2×3 monotone corrections `[5/24, 5/24, 5/48, 5/48, 5/48, 0]`; fill-in exactly on `((0,1),(1,0))` and `((0,2),(1,1))`. Plaquette: **0** orders keep `P`'s support and **0** have `P_σ = P` (structural reason: `Σ_k|A_k| = #edges = 4 > 3 ≥` max achievable with all `|A_k| ≤ 1`, since the first site records nothing). |
| CK-03 G3(b) general | **REFUTED** | See finding F1 — three counterexamples with exact matrices. |
| CK-04 G4 | **CONFIRM** | `det P` / `Π P_kk`: declared — 1×3 `201/8`/27, 2×2 `279/4`/81, 2×3 `2285299/4096`/729; real — 1×3 `51/2`/27, 2×2 `72`/81, 2×3 `37835/64`/729. All `det P` real, positive, strictly below `Π P_kk`. Diagonal `P = 3I₃`: `det = 27 = Π P_kk` (equality case). Schur-pivot re-proof executed on 2×3 declared: pivots `[3, 139/48, 402/139, 18601/6432, 51558/18601, 2285299/824928]`, product `= det P`, each `≤ P_kk = 3`. |
| CK-05 G5 | **CONFIRM** | By my own Gauss-Jordan: static marginal `[[824928/2285299, −556/16441 − 1112i/16441, −21456/2285299 + 28608i/2285299], …]`; pinned-static `(P₁₁)⁻¹ = [[139/402, −2/67 − 4i/67, −1/134 + 2i/201], …]`; formation `[[149/432, −77/2592 − 77i/1296, −53/6912 + 53i/5184], …]` — pairwise different. Formation row-1 precision diagonal `[149/48, 149/48, 3]` vs `[3, 3, 3]`. **The `(P₁₁)⁻¹` attack fails**: I derived it symbolically — `z†Pz − (z₁ + P₁₁⁻¹P₁₀z₀)† P₁₁ (z₁ + P₁₁⁻¹P₁₀z₀)` is free of `z₁` on 2×3, so the conditional of row 1 given row 0 has precision **exactly** `P₁₁`; the note's (ii) is right. Witness: `herm(Q⁻¹) = diag(1/2,1/2) ≠ I = (herm Q)⁻¹`. |
| CK-06 numerals/fences/scope | **CONFIRM with F1, F3–F5** | Every numeral checks: `3`, `(1+2i)/4`, `(2−i)/4`, `5/16`, `5/48`, `5/24`, `149/48`, `14`, `24`, `5`, `62`, `6`, "24 checks, 18 mutations", max degree 3 on 2×3 (2 on the path and plaquette), `3·√5/4 < 3`. Fences present verbatim; no GOAL-forbidden phrase asserted. |
| CK-07 runner | **CONFIRM with F2** | `TOTAL: PASS=24 FAIL=0` in 1.71 s. 18 mutations listed and all 18 detected; 17 fail in exactly their declared family, one does not (F2). Independent float scan of the runner source: no float literal, no `float(` / `.evalf` / `sp.N(` / `nsimplify(`. Cache reproduces: `runner_sha256 d842c8025bddbece5fb92a325333d3912ec5fd1379d320a7e4e2a05c896b0824` matches the live file, and the fresh stdout is **byte-identical** to the cache body. All four `AUDIT_INPUT_PATHS` exist; the four axiom sentences are verbatim in `docs/MINIMAL_AXIOMS_2026-06-29.md`. |
| CK-08 hidden wall / overclaim | **CONFIRM (clean) with one observation** | No "we assume / by construction / as is standard / the framework provides / naturally / obviously / clearly / it is easy to see / standard result" outside the N3 section itself. One provenance observation below. |

## 3. Findings

### F1 — [MAJOR, scope] `G3(b)` "only if" is false for a general Hermitian PD nearest-neighbor precision

**Where.** Note line 57–58 (Result up front: *"`support(P_σ) = support(P)` exactly when every site records
at most one neighbor"*, stated after *"let `P` be a Hermitian positive-definite precision … of a finite
nearest-neighbor graph"*); line 245–248 (Theorem G3 statement (b) and (c)); line 264–267 (the proof step);
line 81 (`conditional_surface_status`: *"G1-G4 are proved for every Hermitian positive-definite
nearest-neighbor precision on every finite graph"*); line 279–284 (the "Reading" paragraph); line 388–390
(Falsifiers, which state the support falsifier without an instance restriction); runner docstring line 11.

**Counterexample A — on the note's own plaquette window (grid, fill-in terms cancel).**
Sites `a=(0,0), b=(0,1), c=(1,0), d=(1,1)`; `P_kk = 3`; `P_ab = P_ac = P_bd = 1/2`, `P_cd = −1/2`
(Hermitian, nearest-neighbor, positive definite: leading minors `3, 35/4, 51/2, 289/4`).
Order `σ = ((0,0), (1,1), (0,1), (1,0))` — a legitimate order; `A_b = A_c = {a, d}`, so **two** sites each
record **two** neighbors. The two fill-in contributions to the (non-adjacent) pair `(a,d)` cancel:

    F_ad = P_ab P_bd / P_bb + P_ac P_cd / P_cc = (1/2)(1/2)/3 + (1/2)(−1/2)/3 = 0

giving `P_σ = P + diag(1/6, 0, 0, 1/6)` exactly, i.e.
`[[19/6, 1/2, 1/2, 0], [1/2, 3, 0, 1/2], [1/2, 0, 3, −1/2], [0, 1/2, −1/2, 19/6]]`, with
`support(P_σ) = support(P)` while `max_k |A_k| = 2`. The separation formula itself still holds here
(verified), so only the biconditional (b) breaks.

**Counterexample B — triangle (fill-in lands on an existing edge).** `K₃`, `P_kk = 3`, all off-diagonals
`1/2` (PD: minors `3, 35/4, 25`). Order `(1,2,3)`: `A_3 = {1,2}`, `F_12 = (1/2)(1/2)/3 = 1/12` lands on the
**adjacent** pair `(1,2)`; `P_σ = [[19/6, 7/12, 1/2], [7/12, 37/12, 1/2], [1/2, 1/2, 3]]`, support unchanged.
This is the case the note's parenthetical *"two neighbors of one site are at distance two on the grid"*
excludes for (c) but **not** for (b).

**Counterexample C — the sharper one: fill-in can cancel an existing edge entry, so the support can
SHRINK.** `K₃` with `P = [[3, 1/4, 1/2], [1/4, 3, −3/2], [1/2, −3/2, 3]]` (PD: minors `3, 143/16, 303/16`).
Order `(1,2,3)`: `P_σ[0][1] = 1/4 + (1/2)(−3/2)/3 = 0`, so
`P_σ = [[149/48, 0, 1/2], [0, 15/4, −3/2], [1/2, −3/2, 3]]` and `support(P_σ) ⊊ support(P)`. This answers
CK-03's attack (a) directly: **yes**, an off-diagonal fill-in can cancel an existing edge entry.

**The wrong step.** Note line 265–266: *"the support of `F_σ` is exactly the set of pairs recorded together
by some site"*. Only `support(F_σ) ⊆ {pairs recorded together}` is justified; `F_xy = Σ_{k: x,y∈A_k}
P_xk P_ky/P_kk` is a **sum**, and A shows it can vanish. Line 266–267 then adds *"a pair recorded together
is two neighbors of one site, hence non-adjacent on the grid"* — correct, but it silently imports the grid
hypothesis into a statement (b) that carries none, and even with it, A survives.

**Correct statement.** Forward direction is general and unaffected: if every `|A_k| ≤ 1` then `F_σ = 0`
(empty sum) and `P_σ = P + diag(c)`, so `support(P_σ) = support(P)`. The converse needs **two** extra
hypotheses: (i) no two neighbors of a site are adjacent (triangle-free — true on the grid, which is
bipartite), and (ii) no cancellation in the fill-in sums. Suggested rewrite of (b):

> (b) if every `|A_k| ≤ 1` then `F_σ = 0` and `P_σ = P + diag(c)`, so `support(P_σ) = support(P)`; the
> converse holds whenever no two neighbors of a site are adjacent **and** no fill-in sum cancels — in
> particular it holds on the declared instance and windows (executed), but not for every Hermitian
> positive-definite nearest-neighbor precision: on the plaquette with `P_kk = 3`, `P_ab = P_ac = P_bd =
> 1/2`, `P_cd = −1/2` and the order `(a, d, b, c)`, two sites record two neighbors each and the support
> is still `P`'s.

and (c) likewise ("couples them" → "couples them **unless the contributions cancel**").
`conditional_surface_status` should read *"G1, G2, G3(a) and G4 are proved for every Hermitian
positive-definite nearest-neighbor precision on every finite graph; G3(b)'s converse and G3(c) are proved
on the grid for the declared instance"*, which is what the note's own **Exact target** (line 183–187)
already says.

**Scope of the damage.** Nothing executed changes. I checked that the *declared* instance does not
cancel: on the 3×3 grid under the monotone order there are 4 pairs recorded together and none cancels
(the two contributions to `((0,1),(1,0))` are both `−5i/48`, they add). All 62 executed cases stand.

### F2 — [MINOR] the "exactly one family" claim about the mutations is false

Note line 448–449: *"Each of the 18 declared mutations perturbs one object or injects one claim and fails
in exactly one family."* `--mutation monotone_class_split` fails **B5, C5 and E2**
(`mutation_family_expected: B`, `mutation_family_observed: BCE`, `TOTAL: PASS=21 FAIL=3`). Cause: the
mutation overwrites `Pm[0]` at runner line 288, and runner line 291 then stores that mutated matrix in
`report["P23"]`, which families C (C5) and E (E2) consume. Fix: either mutate a copy that is not exported,
or state the leakage. The runner already prints the discrepancy but does not gate on it.

### F3 — [MINOR] the runner's forbidden list diverges from the GOAL contract's

`GOAL_block07.md` line 27 forbids the literal `"the Bridge"`; the runner's `FORBIDDEN` (line 407–411)
replaces it with `"the Bridge weights"` and `"the Bridge conjecture"`. The note **does** contain `the
bridge` — line 86, `claim_type_reason`: *"nothing about any external object, the plane, a physical order,
the Born form or the bridge is claimed"* — and the runner's comparison is case-insensitive, so the
contract's list as written would fail the note. Substantively harmless (the occurrence is a negation, a
fence, not a claim), but F2 does not enforce the contract as written. Either narrow the GOAL's string or
say in the note that the forbidden list bars assertions, not fences. (Similarly `"fires wake condition"`
in the runner can never match the note's `"does not fire wake condition 1"` — deliberate, since that
sentence is a required fence, but worth a word.)

### F4 — [COSMETIC] Gershgorin sentence over-applies one modulus

Note line 122–124: *"Both are Hermitian; positive definiteness follows from Gershgorin (each site has at
most three neighbors, each entry of modulus `√5/4 < 1`, so `3 > 3 · √5/4`)"*. The **real** instance's
off-diagonal modulus is `1/2`, not `√5/4`. The conclusion is unaffected (`1/2 < √5/4 < 1`) and the leading
minors are executed (B1), but the sentence as written asserts the wrong modulus for one of the two
instances.

### F5 — [COSMETIC] "with row 0 the pinned records" heads a list where two of three objects do not condition

Note line 146–151 and line 304–306: of the three read-slice objects only (ii) conditions on row 0;
(i) and (iii) are **marginals** of row 1. Each item is individually labelled correctly ("static marginal",
"pinned-static conditional", "formation covariance"), so no false statement is made, but the framing
sentence invites a misreading, and the genuinely matched conditional comparison is the separate E2
(precision blocks `[149/48, 149/48, 3]` vs `[3, 3, 3]`).

### Observation (not a finding)

Note lines 105–113 assert that the external lane's object *"is complex and not Hermitian, and its artifacts
are not on the main branch"*. This is a factual claim about an external object, in tension with the fence
*"nothing is claimed about any external fixture"* — but it is provenance, it is sourced verbatim to
`PROBES_gravity_consumer_20260907.md` lines 7–8 (which itself cites the block-171 note by branch and line
numbers), and nothing in G1–G5 rests on it. I could not verify it from `main` (the branch is not here),
and the note says as much. No action needed beyond awareness.

Also noted: the note's G2 proof reaches the right conclusion by an indirect route (invariance of `L†DL`
under a simultaneous permutation). The direct identity `P_σ = Σ_k P_kk · conj(v_k) v_kᵀ`, with
`v_k` the site-indexed vector determined by `(k, A_k)` alone, gives G2 immediately and makes the
site-indexing explicit. Optional improvement.

## 4. Mutation runs

Runner clean: `TOTAL: PASS=24 FAIL=0` (1.71 s wall). All 18 declared mutations run:

| mutation | declared family | observed | TOTAL | checks failed |
|---|---|---|---|---|
| pd_certificate_forged | B | B | 23/1 | B1 |
| quadratic_form_mismatch | B | B | 23/1 | B2 |
| normalizer_wrong | B | B | 23/1 | B3 |
| class_equality_broken | B | B | 23/1 | B4 |
| **monotone_class_split** | **B** | **BCE** | **21/3** | **B5, C5, E2** |
| separation_formula_wrong | C | C | 23/1 | C1 |
| support_condition_forged | C | C | 23/1 | C3 |
| fillin_pairs_wrong | C | C | 23/1 | C5 |
| correction_literal_off | C | C | 23/1 | C4 |
| equality_with_static_claimed | C | C | 23/1 | C2 |
| hadamard_reversed | D | D | 23/1 | D1 |
| hadamard_equality_case_wrong | D | D | 23/1 | D2 |
| read_slices_equal_claimed | E | E | 23/1 | E1 |
| conditional_block_equal_claimed | E | E | 23/1 | E2 |
| herm_inverse_commutes_claimed | E | E | 23/1 | E3 |
| claim_lane_fixture | F | F | 23/1 | F2 |
| claim_formation_equals_static | F | F | 23/1 | F2 |
| claim_bridge | F | F | 23/1 | F2 |

17/18 fail in exactly their declared family; `monotone_class_split` does not (finding F2). Every mutation
is detected — no mutation passes silently. Cache: fresh stdout byte-identical to the cache body;
`runner_sha256` matches.

## 5. My scripts, and my own failures

**Scripts** (scratch, disjoint machinery — the runner is never imported):
- `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/checker07/ck_own.py`
  — my own `gdet`/`ginv` (Gaussian elimination / Gauss-Jordan), the formation exponent built from the
  Gaussian conditional **densities** in real coordinates `z = a + ib` (never from `L†DL`), my own
  recorded-set enumeration, my own `P + diag(c) + F` assembly, and the counterexamples.
- `.../checker07/ck_misc.py` — order censuses, Gershgorin numerals, 3×3 no-cancellation check.
- `.../checker07/mutations.txt`, `.../checker07/fresh.txt` — mutation sweep and fresh runner stdout.

**My own failures and limits:**
- My `ginv` calls `sp.nsimplify` on its inputs to normalize types. On exact `Rational`/`I` entries this is
  the identity and no float entered (every output above is an exact rational or Gaussian rational), but
  under the runner's own float-scan discipline that call would have been banned; disclosed rather than
  hidden.
- My first pass at the GOAL forbidden-phrase scan used `grep -c` and returned an ambiguous count of 1; I
  needed a second pass to localize it to line 86. No conclusion was drawn from the ambiguous pass.
- I did **not** re-derive block 01's Theorem B or block 05's P1. Per the spec they are cited premises; I
  verified only that the cited fragments exist verbatim (`"at most one recorded neighbor"` in block 01,
  `"for every nearest-neighbor rule"` in block 05) and that block 01's claim_scope states Theorem B "for
  every finite graph". If block 01's Theorem B is itself scope-defective, G3's "Reading" paragraph inherits
  it; that is block 01's audit, not mine.
- My "the declared instance never cancels" check covers the three declared windows plus the 3×3 grid under
  the **monotone order only**. I have **not** proved that the declared instance can never produce a
  cancelling fill-in on an arbitrary grid and arbitrary order; the recommended rewrite of (b) therefore
  says "executed on the declared instance and windows", not "provable for the declared instance".
- I attacked G1's conventions, the term-by-term expansion, the `P_σ = P` iff, the Hadamard proof and the
  `(P₁₁)⁻¹` identification and found **nothing wrong** with any of them; the only break is F1.
