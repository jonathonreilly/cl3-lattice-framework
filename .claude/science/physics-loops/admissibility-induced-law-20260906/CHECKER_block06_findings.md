# Block 06 — refuting checker findings (Opus 5, disjoint machinery), 2026-09-07

## 1. VERDICT

**PASS-NO-BLOCKER**, with **three wording corrections recommended before land** (F-01 is a false
sentence inside the S1 proof; F-02 is a false-as-printed factorization list; F-03 is lay-summary
softening). None of the three touches a number, an enclosure, a degree or a theorem's truth: I
rebuilt the whole object from block 02's definitions with my own code and **every quantitative claim
I could reach reproduced exactly** — orbit counts, self-adjointness on every pair, all four
`tr(Q^2)` integers, all four `λ_1` 18-digit labels, all eight `s` 22-digit enclosure labels, the
four ratio bounds, the four Krylov degrees (my own prime), the exact `m_1(Q)1 = 0` dependency on
every orbit at all four cases, irreducibility and root counts at `d = 8, 30, 16`, the two pairs of
minimal polynomials of the statistics, the `W = 2, 3` recomputation against block 02's literals, the
finite-`n` sequence at `(5; 3,1,2)`, and the 526-digit figure. The runner passes on the current
source (`PASS=34 FAIL=0`) and reproduces the pinned cache byte-for-byte; ten mutations each fail in
exactly their declared family. No forbidden phrase appears; no float literal appears in the runner.

One process hazard is reported separately (H-01): the note **and the runner source were being edited
by another seat while I checked**, and for part of my window the pinned cache did not reproduce a
live run.

## 2. CK table (exact numbers, my own machinery)

| CK | verdict | what I computed independently |
|---|---|---|
| CK-01 S1/S2 | **CONFIRM** | Orbits under my own 48-map group (24 det = +1 signed axis permutations × row reversal; `len(ROT) = 24` checked): **3, 8, 38, 178** at `W = 2,3,4,5`; orbit sizes sum to `6^W` (1296, 7776). `A` orbit-constant: True at all four cases. `w_O Q_{OO'} = w_{O'} Q_{O'O}` on **all 38² and 178² pairs, both triples**: True. `tr(Q^2) = Σ_{O,O'} Q_{OO'}Q_{O'O}` = **28006524928 / 250087391159985 / 16238809878528 / 1948759036672266913** — all four match the note. Sector vs **full 1296-state** center-row statistics at `W = 4`, `n = 3, 5, 7`, both pairs, both triples: **12/12 exact equalities** (full state built through `V = φ^{⊗4}`, no quotient). |
| CK-02 S3 | **CONFIRM** | Re-derived and re-executed all four steps in my own code with `k = 40`. At every case `y > 0`, `0 < lo ≤ μ ≤ hi`, `δ = μ − λ_2bound > 0`, `lo > λ_2bound`. My `λ_1` outward labels: `[167095.549094439124072551, …552]`, `[15805546.058271708040967862, …863]`, `[4020095.963367139908549070, …071]`, `[1394779038.040295659739675096, …097]` — **identical to the note**. My eight `s` enclosures reproduce the note's 22-digit labels **exactly** (widths `5.550e-59`, `3.438e-69`, `2.273e-57`, `7.443e-68`, all `< 10^{-50}`). My `λ_2bound/lo` rounded up at 5 dp: **0.05538, 0.03301, 0.06932, 0.04150** — identical. My `r/δ`: `9.810e-60`, `6.077e-70`, `4.019e-58`, `1.3159e-68`, so the note's `sin θ ≤ 9.82e-60, 6.08e-70, 4.02e-58, 1.32e-68` are valid upper bounds. **Independent cross-check demanded by the spec:** I ran the *entire* enclosure route on the **full 1296-state transfer matrix** at `W = 4` (weights `A`, `T` is `A`-self-adjoint by the same symmetry, `tr(T^2)` by the tensor trick = 38822375424 and 310039677754398) and obtained the **same eight 22-digit endpoints** — the orbit quotient is not doing any load-bearing work in the numbers. |
| CK-02 attacks | **CONFIRM (no defect)** | (a) `δ = μ − λ_2bound` with negative eigenvalues: valid — the proof needs only `μ − λ_i ≥ δ` for `i ≥ 2`, and `λ_i ∈ [−λ_2bound, λ_2bound]` gives it; a negative `λ_i` widens the gap. `μ > λ_1` is never used and is not needed. (b) `w`-normalisation: `r = ‖Qy − μy‖_w/‖y‖_w = ‖Qŷ − μŷ‖_w`, `‖ŷ‖_w = ‖x‖_w = 1`, `a_1 = cos θ`, `Σa_i² = 1` — consistent; `2 − 2cos θ ≤ 2sin²θ` needs `cos θ ≥ 0`, supplied by `ŷ, x, w > 0`. (c) The rational square-root bound is rigorous: with `m = ⌊t·10^{160}⌋`, `s = ⌊√(m+1)⌋`, `(s+1)² > m+1 > t·10^{160}`, so `(s+1)/10^{80} > √t`. My own (slightly tighter) outward integer-sqrt gives the same 22-digit labels, so the note's interval is not narrower than a rigorous one. |
| CK-03 S4 | **CONFIRM** | Krylov rank by incremental echelon **mod `2^{127} − 1`** (a prime the runner does not use): **8, 30, 16, 111** — certifies `d ≥` those over `Q`. Taking the runner's printed `m_1` coefficients and evaluating `m_1(Q)1` with **my own `Q`** in exact integer arithmetic: **zero on all 38 / 38 / 178 / 178 orbits**, monic, at all four cases (`d = 111` in 1.2 s) — certifies `d ≤` those. So `d = 8, 30, 16, 111` exactly, on my matrix. `m_1` irreducible over `Q` at `d = 8, 30, 16` (sympy `factor_list`, < 0.1 s each); `d` **distinct** real roots at each (8/30/16, all distinct). **Attack "could another root of `m_1` lie in the CW interval":** I isolated **all** real roots — roots in `[lo, hi]` = **1**, roots above `hi` = **0**, at all three degrees. At `d = 111` I did not factor (as the note declines to). Minimal polynomials of the statistics: `(4; 3,1,2)` `s_edge` and `s_inner` degree **8**, `(5; 3,1,2)` degree **16**; each **irreducible**, with **exactly one** real root in the corresponding S3 enclosure (8/8/16/16 real roots total). `d = 111` coefficients: 111 non-leading coefficients, **max 526 digits** — matches. |
| CK-04 S5 | **CONFIRM** | `f = 3/12 = 1/4` and `5/23`. My lower-endpoint minus `f`: `0.0061162479…`, `0.0062841851…` (`W=4`, `(3,1,2)`); `0.0061164296…`, `0.0062896288…` (`W=5`); `0.0025245576…`, `0.0025654721…` (`W=4`, `(5,2,4)`); `0.0025245705…`, `0.0025661840…` (`W=5`) — all match the note's truncations and all `> 10^{-3}`. `W = 2, 3` by my S3 route: `[0.255943088901618766, …767]`, `[0.219874176124090031, …032]`, `[0.2561109872857786908612, …613]`, `[0.2199151616870197815075, …076]` — **block 02's F4 digits reproduced exactly**, and `s_inner = s_edge` there (the formula returns the edge pair), `s − f = 0.00594308, 0.00248287, 0.00611098, 0.00252385`. `s_inner(lo) − s_edge(hi)` = `1.6794e-4`, `4.0914e-5`, `1.7320e-4`, `4.1614e-5` → the note's rounded-down `1.67e-4, 4.09e-5, 1.73e-4, 4.16e-5` are correct. Width-4 vs width-5 differences at `(3,1,2)`: `s_inner` `5.44368e-6`, `s_edge` `1.81697e-7` → the note's outward interval labels `[5.4436, 5.4437]e-6` and `[1.8169, 1.8170]e-7` are correct. Finite-`n` at `(5; 3,1,2)`, `n = 3,5,9,17,33,65`: distances to the enclosure **strictly decreasing** (`1.876e-4, 6.113e-6, 7.870e-9, 1.868e-14, 1.484e-25, 1.066e-47` inner), and the `n = 33` inner value is `0.2562896288160817584176711…` — **the note's digits verbatim**, `1.484e-25 < 1.5e-25` and `1.066e-47 < 1.1e-47` as claimed. |
| CK-04 attack (plane / monotonicity) | **CONFIRM, with F-03** | No sentence claims a limit, a plane value or monotonicity. `Boundaries and non-claims`, `N7`, `N5 lattice_wide` and S5's closing sentence all restrict to the four widths. Only the lay line 23 ("a fixed step away") reads as more than is proved (see F-03); line 26 already says "of about the same size, at every width we computed". |
| CK-05 numerals / fences / phrases | **CONFIRM, with F-02** | My own scan of the 19 forbidden phrases over the note: **zero hits**. `Collatz–Wielandt`, `Davis–Kahan`, `Perron–Frobenius` occur only in `Prior art` and `Imports` (the theorem bodies use "the two-sided ratio bounds", "the trace bound", "the residual–gap bound"). `claim_scope` matches what is proved and executed — it claims irreducibility only at `8, 30, 16`, the identification only at `d ≤ 16`, and disclaims wider strips, the plane and monotonicity. Every numeral I could reach reproduced (above). The one printed literal that is false as written is the charpoly degree list (F-02). |
| CK-06 runner validity | **CONFIRM** | Baseline run on the current source: `TOTAL: PASS=34 FAIL=0`, `elapsed_s: 76`. `--exact` run: `PASS=34 FAIL=0`, 84 lines, prints the rational `λ_1`/`s` endpoints, the finite-`n` rationals, `m_1` at all four degrees and the two pairs of minimal polynomials — as the Verification section says. Pinned cache vs my run: **0 differing lines** (55 vs 55), `runner_sha256 = 9b05b6d8b81fdf529885ac1e0a31922557889e255260ac6e9f17e600c875d315` = live runner sha. `--list-mutations` lists 26. Ten mutations run (4 at a time): each gives `PASS=33 FAIL=1` with `mutation_family_observed` = `mutation_family_expected` and exactly one failing check (table in §4). Float scan: tokenising the runner source I find **zero float literals**, no `float(`, no `numpy`, no `math.`, no `round(`, no `%f`/`{:.` formatting; the only `decimal` hits are the integer-expansion helper and its comments. |
| CK-07 hidden wall / overclaim | **CONFIRM** | No "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical" outside the N3 section that names them. The spectral theorem is declared cited scaffolding; Gauss's lemma is explicitly non-load-bearing (the dependency is verified exactly, which I confirmed on my own `Q`); the Mersenne primality is explicitly non-load-bearing for the same reason — correct, since my modular ranks only ever *lower-bound* `d` and the upper bound comes from the exact integer identity. `next_trace_action`'s "(the orbit count is the only cost)" is a method aside, not a claim about physics. |

## 3. Findings

**F-01 — a false sentence inside the S1 proof (severity: moderate; fix before land).**
Note lines **203–206**: "The pair indicator `[ρ_a = ρ_b]` is `G`-invariant for the edge pair and for
the innermost pair (a rotation preserves equality of entries; the reversal maps `(0, 1)` to `(W−1,
W−2)`, whose indicator has the same orbit sums since the reversal is in `G`, **and maps the
innermost pair to itself**)".

- The indicator is **not** `G`-invariant pointwise. I checked directly: at `W = 5`, `[ρ_0 = ρ_1]` is
  not invariant under the 48 maps (**False**), and `[ρ_1 = ρ_2]` is not invariant either
  (**False**). (At `W = 4` the innermost indicator *is* invariant — reversal fixes `(1,2)` there:
  **True**.)
- "maps the innermost pair to itself" is **false at `W = 5`**: reversal `j ↦ 4 − j` sends the
  declared innermost pair `(1, 2)` to `(3, 2)`, i.e. the pair `(2, 3)`.
- **The result is nonetheless correct**, and nothing downstream changes: what is used is only that
  `n_O = #{ρ ∈ O : ρ_a = ρ_b}` is a well-defined orbit count, and reversal being a bijection of each
  orbit makes it insensitive to which reflected copy of the pair one counts. I verified this
  exhaustively at `W = 5`: **0 of 178 orbits** have `#{ρ_1 = ρ_2} ≠ #{ρ_2 = ρ_3}`, and **0 of 178**
  have `#{ρ_0 = ρ_1} ≠ #{ρ_3 = ρ_4}`.
- Correct statement: *the orbit sum of a `G`-invariant weight against the pair indicator is
  `weight_O · n_O = weight_O · |O| c_O`, because every `g ∈ G` maps `O` bijectively to `O` and
  carries the pair `(a, b)` to a pair whose indicator has the same orbit count (a rotation preserves
  equality of entries; the reversal carries `(a, b)` to `(W−1−b, W−1−a)`).* No claim of pointwise
  invariance is needed or true.

**F-02 — the width-4 charpoly degree list is false as printed (severity: minor; fix before land).**
Note lines **361–362** (and runner check **C5**): "the characteristic polynomial of `Q` factors with
degrees `[1, 1, 2, 8]` and `[1, 1, 1, 5, 30]`". `Q` is `38 × 38`, so its characteristic polynomial
has degree 38, but `1 + 1 + 2 + 8 = 12`. I factored my own `Q` exactly: at `(4; 3,1,2)` the
irreducible factors are of degree **1 (multiplicity 1), 1 (multiplicity 27), 2 (multiplicity 1), 8
(multiplicity 1)** — `1 + 27 + 2 + 8 = 38`. At `(4; 5,2,4)` the list is `1, 1, 1, 5, 30`, all
multiplicity 1, summing to 38, so only the first case is affected. The load-bearing part of the
sentence ("`m_1` is its factor of degree `d`") is true. Correct statement: *"factors into
irreducibles of degrees `1, 1, 2, 8` with multiplicities `1, 27, 1, 1` and `1, 1, 1, 5, 30` with
multiplicity 1"* — or print the multiplicities in C5.

**F-03 — one lay-summary phrase reads as more than is proved (severity: cosmetic).**
Note line **23**: "odds of matching that sit **a fixed step** away from the odds the order-built law
gives them". The step is not fixed across the computed widths: at `(3,1,2)` it is `0.0059431`,
`0.0061110`, `0.0061162`, `0.0061164` for `W = 2, 3, 4, 5` (edge), and the inner step at `W = 4, 5`
is `0.0062842`, `0.0062896`. Line 26 already says "of about the same size, at every width we
computed"; line 23 should match it ("a step away", or "a step of about the same size at the widths
we computed"). Nothing else in the note asserts width-independence.

**H-01 — hazard: the note and the runner were being edited by another seat during this check
(severity: process; not a defect of the science).**
My first baseline run (17:58) printed `PASS: F4 classical names only in Prior art, Imports and the
verbatim fence`, whereas the current runner (and the pinned cache) print `PASS: F4 classical names
only in Prior art and Imports`; at that moment the pinned cache did **not** reproduce a live run
(1 differing line). The note's line 359 also changed under me ("the contract lens's independent
exact construction" → "the supervisor's independent exact construction …, 795 s"), and line 26 was
softened to "of about the same size". After the edits settled I re-ran the current runner: cache and
run now agree on **0 of 55 lines**. Anyone re-verifying should pin: note sha256
`2506cec2d27304762fc5d800860526fb188e02d3e20f468067ca2e4592f38f3a`, runner sha256
`9b05b6d8b81fdf529885ac1e0a31922557889e255260ac6e9f17e600c875d315`. My §2 findings on the note text
are against that note hash. (The cited pack
`specs/supervisor_control_block06_krylov_d111_exact.out.txt` exists and states 795 s and 526 digits,
matching the note.)

**Nothing refuted.** In particular I could not break: the self-adjointness identity or any of its
three hypotheses (all three are genuinely used and genuinely supplied); the upper ratio bound's
left-Perron-vector argument; the trace bound's use of `λ_1 ≥ lo > 0`; the residual–gap bound's `δ`
and `cos θ ≥ 0` conditions; the `2ε` Cauchy–Schwarz step; the Krylov separation lemma; or any
printed digit.

## 4. Mutation runs (all in `S/mut/`, four at a time)

| mutation | expected | observed | result | failing check |
|---|---|---|---|---|
| `orbit_count_wrong` | B | B | PASS=33 FAIL=1 | B1 |
| `sector_full_mismatch` | B | B | PASS=33 FAIL=1 | B5 |
| `self_adjointness_broken` | C | C | PASS=33 FAIL=1 | C1 |
| `krylov_dimension_off` | C | C | PASS=33 FAIL=1 | C4 |
| `trace_bound_forged` | D | D | PASS=33 FAIL=1 | D1 |
| `s_enclosure_contains_formation_value` | D | D | PASS=33 FAIL=1 | D3 |
| `separation_sign_flipped` | E | E | PASS=33 FAIL=1 | E1 |
| `ratio_bound_too_small` | E | E | PASS=33 FAIL=1 | E4 |
| `claim_plane_limit` | F | F | PASS=33 FAIL=1 | F2 |
| `claim_classical_name_in_theorem` | F | F | PASS=33 FAIL=1 | F4 |

Ten mutations across all five executable families; each fails exactly one check, in exactly its
declared family. Baseline `run_base.txt` / `run_base2.txt` and `run_exact.txt`: `PASS=34 FAIL=0`.

## 5. My scripts, and my own failures

All under
`/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/checker06/`:

- `ck_core.py` — my menu/`φ`/`A`/`V`/`T`, my own enumeration of the 24 proper rotations as signed
  axis permutations with `det = +1`, the 48 row maps, orbits by my own closure, the quotient `Q`,
  and the outward integer-square-root helper. No runner import anywhere.
- `ck_s3.py` — the S3 route (`k = 40`, `lo/hi/μ/r/λ_2bound/δ/ε`, both statistics) and the exact
  outward decimal expander (`dec_out`, integer arithmetic only). Output `ck_s3.out`.
- `ck_full.py` — the **full 1296-state** route through `V = φ^{⊗W}`: the `n = 3,5,7` center-row
  statistics for the S1 equality test, and the complete enclosure route with weights `A` and
  `tr(T^2)` by the tensor trick. Output `ck_full.out`.
- `ck_krylov.py` — Krylov echelon rank mod `2^{127} − 1`; exact `m_1(Q)1` on every orbit.
- `ck_alg.py` / `ck_alg2.py` — irreducibility, all-real-root isolation and interval counts for `m_1`
  and for the minimal polynomials of the statistics. Output `ck_alg.out`.
- `ck_w23_n33.py` — `W = 2, 3` by the same route against block 02's F4 literals, and the `(5; 3,1,2)`
  finite-`n` sequence at `n = 3, 5, 9, 17, 33, 65`.
- `ck_charpoly.py` — the width-4 characteristic polynomial and its factor multiplicities (F-02).
- `mut/*.txt`, `run_base.txt`, `run_base2.txt`, `run_exact.txt`, `note_snapshot.md`, `runmut.sh`.

**My own failures and gaps.**
1. Three scripting bugs cost about six minutes: an off-by-one in parsing the runner's `m_1`
   coefficient list (the leading monic `1` is omitted from the printed list), and two `KeyError`s
   from my own inconsistent dict keys (`o['edge']` vs `o['s_edge']`). None affected a result.
2. One background run was killed because I backgrounded a shell that itself backgrounded the runner;
   I re-ran it.
3. **CANNOT-REACH within the 60-minute budget** (I did not verify these independently and am
   relying on the runner's D4/D5/B5 checks for them): the `n = 33` end-record `P(e_y)` boundary check
   (D5) at any case; the finite-`n` monotone-distance sequence (D4) at the three cases other than
   `(5; 3,1,2)`; the sector-vs-full-state equalities at `W = 5`, `n = 3, 5` (I did all twelve at
   `W = 4`, not the eight at `W = 5`); and the claim that **no other** irreducible factor of the
   resultant has a root in the enclosure (I confirmed the *claimed* factor is irreducible, of the
   claimed degree, and has exactly one root there, which with D7 closes the identification).
4. My `m_1` verification uses the runner's printed coefficients evaluated on **my** matrix. The
   degree lower bound (`d ≥ 8, 30, 16, 111`) is fully mine, via my own prime; the upper bound comes
   from that exact evaluation. I did not independently *construct* the degree-111 polynomial.
5. I did not audit the runner's internal implementation line by line; my confidence in the numbers
   comes from rebuilding them, not from reading its code.
