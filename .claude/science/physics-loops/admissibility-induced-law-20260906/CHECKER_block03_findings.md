# REFUTING CHECKER — block 03 (admissibility-induced-law-20260906), independent seat, disjoint machinery

Seat: Opus 5, refuting checker. Worktree read-only; all computation in my own code
(`fractions.Fraction` / Python ints / `sympy` for polynomial algebra only). The runner was
never imported. Floats appear in my scripts only inside `print` as labelled diagnostics;
every decision compared exact rationals.

## 1. VERDICT

**PASS-NO-BLOCKER.**

Nothing in the note or the runner was refuted. Every literal I recomputed matched exactly —
the seven `c_1` values and their tie counts, the maximizing patterns, the fifteen-cell grid,
all six thresholds with their polynomials and isolating intervals, all six copy counts
(30, 288, 288, 60, 72, 72), the `c_1^{(4)}` literals, the `3×3` centre-site total variations
including the 21-over-23-digit rational at `(2,1,2)`, the three window bounds, the walk counts
and the `α^L/(1−α)` table. Every attack I mounted failed to produce a counterexample: no
rational `t` between the thresholds with `6c_1 ≥ 1` (1,344 points), none outside with
`6c_1 < 1` (1,110 points), no exterior flip or window observable violating the coupling bound
(1,080 site-checks plus a two-slot flip and a two-site observable). Twelve mutations each
failed in exactly their declared family.

Two **low-severity, presentational** items are recorded below (F1, F2). Neither changes a
number or a claim; both are places where the note's written justification is shorter than the
fact it asserts, and in both cases I verified the fact independently. Two informational
observations (F3, F4) round out the scan.

## 2. CK table (exact numbers)

| CK | verdict | exact numbers I obtained |
|---|---|---|
| CK-01 coefficient | **CONFIRM** | `c_1`: (3,1,2) `270/989`; (5,2,4) `8650000/40615109`; (2,1,2) `2/13`; (3,2,2) `2079/15566`; (5,4,4) `4000000/61385721`; (11,10,10) `98241110000/4544062780611`; (2,2,2) `0`; (7,3,5) `6391462/29948925`. My own extra triple `(4,7,6)`: `2494427712/20122619095`, `6c_1 = 14966566272/20122619095 < 1`. Tie counts over the 252×15 choices `12, 6, 60, 30, 30, 30, 24` — the note's list, in order. Lex-first maximizers reproduce the note exactly: `(+x,+x,+x,+y,−y)` pair `+x↔−x` at (3,1,2); five `+x`, pair `+x↔−x` at (5,2,4),(5,4,4),(11,10,10); `(+x,+x,−x,+y,−y)` pair `+z↔−z` at (2,1,2); `(+x,+x,+x,−x,−x)` pair `+x↔−x` at (3,2,2). Direction independence by **full ordered `6^5` enumeration at each of the six slot positions**: `270/989` six times. `c_1(p,q,r)=c_1(q,p,r)` on 7 triples. `c_1^{(4)}(2,5,3)=14250/59251 > c_1(2,5,3)=1629375/6780002` confirmed. `c_1(2,1,2)=c_1(4,2,4)=2/13` (degree-zero homogeneity). |
| CK-02a fold content | **CONFIRM** (2 presentational items) | Second crossings reproduced by brute force. `(t,1,1)`: numerator of `6TV−1` at `(+x,+x,−x,+y,−y)`/`+z↔−z` is `−(t²+10t−5)/(t²+4t+1)` — I derived it by hand and by sympy; root `√30−5`. `(t,t,1)`: five `+x`/`+y↔+z` gives `−(t⁵+7t−5)/(t⁵+t+1)`, 1 real root. `(1,1,t)`: same pattern gives `(5t⁵−7t⁴−1)/(1+t⁴+t⁵)`, 1 real root. Brute-force `6c_1−1` at the six isolating endpoints: signs `(−,+) (−,+) (+,−) (+,−) (+,−) (−,+)` — exactly the note's orientations, and reversed at rational points 10⁻⁶ outside on each side. Copies by **function-level** test (TV equal at 8 spread rationals incl. the interval midpoint): `30, 288, 288, 60, 72, 72` = the note's counts, and = the counts my own symmetry combinatorics predicts (`6·5`, `4·3·6·4`, `4·3·6·4`, `6·C(5,3)`, `3·6·4`, `3·6·4`). Lipschitz lemma re-derived: `t a_s' = a_s(k_s−k̄)`, `Σ_s|a_s'| ≤ (1/t)Σ_s a_s|k_s−k̄| ≤ 6/t` — constant correct; `TV` gets `6/u`, `6TV` gets `36/u`; using `max(f(a),f(b)) + L(b−a)` is a valid (conservative) over-estimate of `max_{[a,b]} f`. Numeric test at 6 rational pairs per line: worst `lhs/rhs` = 0.0766 / 0.0842 / 0.0841 — holds with wide margin. Reciprocity `c_1(t,t,1)=c_1(1,1,1/t)` exact at `t = 5/4, 3/2, 7/10, 11/8, 1/3, 9/4`; reciprocal-polynomial proportionality holds for both the degree-7 and the degree-5 pairs. |
| CK-02 grid and lines | **CONFIRM** | `r=4`, `p,q ∈ 1..12`: the `6c_1 < 1` set is exactly `{(2,4),(3,3),(3,4),(3,5),(4,2..6),(5,3..6),(6,4),(6,5)}`, 15 cells, set-equal to the note's diamond, no extras, no omissions; `p↔q` symmetric on all 144 points. Region attack: 448 rationals inside `(u,v)` on each line (400 evenly spaced plus 48 hugging the endpoints at `(v−u)/10^e`, `e ≤ 12`) — **0 violations**; scan sup `0.999999999998 / 0.999999999999 / 0.999999999998`. Outside attack: 94+238, 137+252, 134+255 rationals beyond the thresholds — **0 points with `6c_1 < 1`**. Sliver scan: 17 points across each of the six isolating intervals — exactly one sign change in each, `6c_1 < 1` throughout the region side. Contract-lens point `6c_1(1,1,2) = 96/49 = 1.9592` (note: "≈ 1.959"). All ten declared line points reproduce the note's truncated 4-digit labels. Real-root counts: 3 / 3 / 3 for the degree-7 polynomials (1 positive each), 2 / 1 / 1 for the second-crossing polynomials (1 positive each). |
| CK-03 Theorem H | **CONFIRM; no missing lemma** | Every step checked as written — details in §3. |
| CK-04 window numbers | **CONFIRM** | `c_1^{(4)}`: `1/8`, `1404/11431`, `10000/175641`, `918/3431` — the note's literals; row sums `4c` = `1/2`, `5616/11431`, `40000/175641` all `< 1`, and `3672/3431 > 1` at (3,1,2). `3×3` window rebuilt from the definition by my own integer row transfer over the 216 row states. Centre TV at (2,1,2) = `691410442136477999520/76730168638463067377251` — **exact match** with the note; bound `(D_Λ b)_c = 1/56`, `D_Λ(I−C_Λ)=I` and `D_Λ ≥ 0` exact. (3,2,2): TV `33371823530478793013606992/4514027923287489693489918949`, bound `1971216/114898033`. (5,4,4): TV `1731753640209702882755284603119966790400/1024620776654359492500695152066016873791443`, bound `100000000/30049760881`. Truncated decimal labels verified digit-for-digit: `0.009010933436→0.0090109`, `0.007392914731→0.0073929`, `0.001690141054→0.0016901`, `0.034675398608→0.0346753`. **Attack: 1,080 site-checks (2 triples × 12 exterior slots × 5 flipped values × 9 sites) — 0 violations**; worst `TV/(D_Λ b)_x` = 0.77134 at (2,1,2) and 0.80860 at (5,4,4). Two simultaneous flips with additive `b`: 0 violations. Window observable `f = 1[η_c = +x] + 1[η_{(0,0)} = +x]`: `|μ(f)−μ'(f)| = 13069625885097261928232/767445752878261848774747 ≤ 549/13888`. |
| CK-05 Theorem I | **CONFIRM** | `Σ_y N_n(0,y) = 6^n` for `n = 1..6` by my own walk enumeration (I extended past the runner's `n ≤ 4`). `α^L/(1−α) < 10^{-3}` first at `L = 119, 39, 8, 4` at (2,1,2),(3,2,2),(5,4,4),(11,10,10), with `L−1` failing in each case. Block 02's Theorem C2 does supply exactly the identity used (existence + the finite-window conditional identity; its claim_scope names "existence … by compactness and the finite-window conditional identity … no uniqueness"). No use of translation invariance anywhere in Theorem I. |
| CK-06 literals, quotes, scope | **CONFIRM** | Axiom sentences verbatim against `docs/MINIMAL_AXIOMS_2026-06-29.md` lines 57–58, 60–61, 77, 80, 82–83. All four fence sentences present verbatim (note lines 657, 659, 661, 663). Forbidden phrases: 0 hits; `certified` appears 0 times (the note uses "certificate"/"certificates"). Author name `Dobrushin`: note lines 191, 194, 196 (Prior art) and 681 (Imports) only — nowhere else, and not in the front matter. `sharp` occurs 6× and every occurrence is "sharper criterion". `221,616 + 2,000 = 223,616` plaquette pairs: `1296·(1+4·5+6·25) = 1296·171 = 221,616` — arithmetic correct. Mutation count 31, check count 41 — as the note states. |
| CK-07 runner validity | **CONFIRM** | Baseline `TOTAL: PASS=41 FAIL=0`, exit 0, **123.4 s** wall on this machine (cache records 86.38 s; limit 400 s). `--list-mutations` = 31 names. 12 mutations run, all `rc=1`, all failing in exactly the declared family (§4). Float scan `grep -nE '\b(float\|numpy\|np\.\|evalf\|nsimplify\|N\()'`: 7 hits, **all** inside the F4 self-scan machinery (lines 32, 865, 895–899) — no float literal, no conversion; a separate `[0-9]\.[0-9]` scan gives 0 hits. `AUDIT_TIMEOUT_SEC = 900`; `AUDIT_INPUT_PATHS` = the four declared files, printed at startup. Cache `runner_sha256` `953de23b…e06d5` equals my `shasum -a 256` of the runner. Cache `input_fingerprint_sha256` `19543425…d183` **reproduced independently** by re-implementing the v1 fingerprint (`sha256` over `b"runner-cache-input-fingerprint-v1\0"` then per path the 8-byte lengths and bytes of the relative path and file body). |
| CK-08 overclaim / hidden wall | **CONFIRM, with F3** | No sentence asserts several laws at the silent triples, a phase transition, a physical rule, or that the two-site criterion would fail. Sharpness is nowhere asserted in the body; N7 concedes in full that the criterion may be crude. Monotonicity of `c_1(t)` is explicitly disclaimed ("monotonicity of `c_1` is neither proved nor needed", note line 353–354) and the region on each line is carried by the Lipschitz-bisection certificate, not by monotonicity. Only wording item: the claim_id / headline phrase "the exact uniqueness region" is readable as sharpness (F3). |

## 3. Findings

### F1 — LOW (presentational). The C11 "copy" test certifies a weaker statement than the note's inference needs.
*Note line 341–344 (G6(i)): "or has, with its sign pattern at `a`, the same rational function as the displayed maximizer (a copy)"; runner `competitor_sweep`, lines 391–412.*

What the runner checks for a non-Lipschitz-certified choice is that the numerator of
`6·(½ Σ_s σ_s (a_s − b_s)) − 1`, with `σ` the choice's **sign pattern at the left endpoint `a`**,
is proportional to the displayed polynomial. For any fixed `σ`,
`TV(t) = ½Σ_s|a_s−b_s| ≥ ½Σ_s σ_s(a_s−b_s)`, with equality only where that sign pattern holds.
So the check certifies `TV_choice ≥ f` on `[a,b]`, not `TV_choice = f`. A choice whose sign
pattern flipped and flipped back strictly inside `[a,b]` would pass the check while its actual
`TV` exceeded the displayed function there, and the inference "6c_1 − 1 crosses zero on `[a,b]`
exactly where the displayed function does" would not follow.

**No such choice exists** — I closed this independently, two ways. (a) A *function-level* copy
test (TV equal at `t = 1/3, 1/2, 3/4, 9/8, 5/4, 3/2, 7/3` and the midpoint of the isolating
interval) gives exactly `30, 288, 288, 60, 72, 72` — the note's counts, so every "identical"
choice is a genuine function identity, not a sign-pattern artefact. (b) The counts are forced
by symmetry: on `(t,1,1)` the rule is 6-state Potts (`φ = t` iff equal), so the conditional
depends only on the value-count vector — `6·5 = 30` at the first threshold and
`6·C(5,3) = 60` at the second; on `(t,t,1)`/`(1,1,t)` the conditional depends only on the
axis-count vector — `4·3·6·4 = 288` and `3·6·4 = 72`. Additionally the displayed pattern
attains the full `7776×15` supremum not only at both endpoints but also at the **midpoint** of
all six isolating intervals (my check).

**Correct statement.** The copies are choices whose two conditional vectors are literally the
displayed pattern's up to a menu relabeling (Potts value counts on `(t,1,1)`; axis counts on
`(t,t,1)`/`(1,1,t)`), hence whose `TV` is identically the displayed `TV` on the whole line. The
note should say that, rather than "with its sign pattern at `a`, the same rational function".
The runner would then check function identity (e.g. equality of the sorted conditional
vectors, or of `TV` at more than `deg` points) rather than signed-sum proportionality.

### F2 — LOW (presentational). G6(ii)'s certificate covers `[u,v]`, which is strictly inside the stated open interval.
*Note lines 348–353.*

`region_certificate` is called with `u` = the **upper** endpoint of the lower threshold's
isolating interval and `v` = the **lower** endpoint of the upper one (runner lines 557–563).
`[u,v]` therefore omits two slivers, `(t_2, u)` and `(v, t*)`, each of width `< 10^{-20}`, that
lie inside the stated open interval `(t_2, t*)`. The note's conclusion — "the set
`{t > 0 : 6c_1 < 1}` on each line contains the open interval between its two thresholds" — is
reached only by combining (ii) with (i): on each isolating interval every non-copy choice is
below one and the copies equal the displayed function, so on the region side of the displayed
root `6c_1 < 1` there too. The note does not spell out that combination sentence.

**The fact is true.** I sampled 17 points across each of the six isolating intervals: exactly
one sign change in each, and `6c_1 − 1 < 0` at every sampled point on the region side
(`A first: --------------+++`, `B first: ------+++++++++++`, `C first: +++++++----------`,
`A second: ++++++++---------`, `B second: +++++++----------`, `C second: ------------+++++`).
**Correct statement.** Add one sentence to G6 deriving the two slivers from (i). No number changes.

### F3 — INFO. "The exact uniqueness region" is readable as a sharpness claim.
*claim_id, the note's title line 12, and Result-up-front line 33.*
The criterion is sufficient only. No body sentence asserts sharpness; the Boundaries fence
("states uniqueness only where the one-neighbor influence sum is less than one") and N7
(conceding the criterion is crude) rule it out. Reading "the exact region" as "the region
computed exactly" is the only consistent reading and it is supported by the surrounding text.
Recorded, not a defect.

### F4 — INFO. H3's stationarity cites block 01 rather than re-proving it.
*Note lines 438–441.* The middle equality — the full conditional of `μ_Λ^ω` at `x` is the rule
with every neighbor recorded — is cited from block 01's Theorem A, where it **is** proved
(block-01 note, "Direct cancellation": every factor not containing `x` cancels in the ratio).
The obligation table declares it "cited (block 01, unaudited)". In scope and honestly declared.
Note that block 01's Theorem A carries a site weight `ψ`, dropped here on block 01's B7
(constant site weight on the transitive menu) — stated at note line 129–130.

### Theorem H, step by step (no missing lemma found)
- **Step 0.** The maximal coupling is constructed and `P(S≠S') = 1−m = TV` proved, including
  the disjoint-support argument on the second branch and the optimality
  `P(S=S') ≤ Σ_s min(a_s,b_s)`. Correct.
- **Step 1 (H1).** The single-slot telescope is valid with several interior neighbors **and** a
  differing exterior simultaneously: `TV` is half the `ℓ¹` distance hence a metric, each
  consecutive pair differs at exactly one slot, and `C_{xy}` is by definition the sup over such
  pairs. `b_x = Σ_{z∈∂(x)} C_{xz}[ω_z ≠ ω'_z]` is exactly the exterior half of the split.
  Correct. On both executed windows every site has exactly four slots (I verified: corners
  2 interior + 2 exterior, edges 3+1, centre 4+0), so one number `c_1^{(4)}` covers every slot.
- **Step 2.** `X` is drawn independently of `(η^t, η'^t)`, so
  `u^{t+1}_x = (1−1/n)u^t_x + (1/n)E[TV(…)]` is exact, and the Step-1 bound is applied
  **pointwise in the joint state** before the expectation — the note says "by Step 1 and
  linearity of expectation", which is that order. Correct.
- **Step 3 (H2).** `‖A‖_∞ ≤ 1 − (1−α_Λ)/n < 1`, contraction, unique fixed point `u* = D_Λ b ≥ 0`.
  The monotone **decrease** of `Φ^t(1)` is correctly gated on `C_Λ 1 + b ≤ 1`; the theorem's
  conclusion does not need that gate (only `u^0 ≤ 1` and monotonicity of `Φ`). Substochasticity
  is checked, and where it fails the note refrains: at `(3,1,2)` the `3×3` centre row sum is
  `4c_1^{(4)} = 3672/3431 > 1` and the note says the bound "is not asserted", recording the
  exact `TV ≈ 0.0346753` only (note lines 481–483; runner D8). I reproduced `3672/3431` and the
  recorded TV.
- **Step 4 (H3).** `μP_x = μ` from the full-conditional identity (F4 above). Correct.
- **Step 5.** A subsequence **is** needed (`π_t` need not converge); the marginals are `μ` and
  `μ'` at every `t` by Step 4; `1[η_x ≠ η'_x]` is a finite sum so its limit passes. Correct.
- **Step 6.** Telescoping over `Λ` with `δ_x(f)` the oscillation. Correct.

### Theorem I (the finite-window-to-lattice passage)
The sentence is: *"Therefore `|μ(f) − ν(f)| ≤ 6c_1 (Σ_x δ_x(f)) α^{L−ℓ}/(1−α)`, which tends to
zero as `L → ∞` because `α < 1`."* (note lines 510–511). It is **complete** given Theorem H
(proved here, for every finite window with row sums below one) and block 02's C2 (cited). I
checked each supporting step: the identity is applied to each law separately and the difference
written as `Σ_{b,b'} μ(b)ν(b')(μ^b(f) − μ^{b'}(f))` using `Σ_b μ(b) = Σ_{b'} ν(b') = 1`, so the
random exterior is handled by a convex combination and dominated by `sup_{b,b'}` — uniform over
both laws. `b_y ≤ 6c_1·1[y ∈ ∂_in Λ_L]` is a conservative over-bound (a box site has at most 3
exterior neighbors). `|x−y|_1 ≥ |x−y|_∞ ≥ L−ℓ` for `x ∈ Δ_ℓ`, `y ∈ ∂_in Λ_L` justifies killing
`k < L−ℓ`. Translation invariance is used **nowhere**. The last step (cylinder algebra is a
π-system generating the product σ-algebra) is cited under Imports, as declared.

## 4. Mutation runs (all in a read-only pass over the tracked runner; 4 at a time)

Baseline: `TOTAL: PASS=41 FAIL=0`, exit 0, **123.4 s**.

| mutation | family declared | family observed | rc | elapsed | failing checks |
|---|---|---|---|---|---|
| coefficient_direction_dependent | B | B | 1 | 135.1 s | B1 |
| region_certificate_forged | C | C | 1 | 43.6 s | C12 (subintervals `[-1,-1,-1]`) |
| second_crossing_wrong_root | C | C | 1 | 77.3 s | C10, C11 (copies `[30,288,288,0,0,72]`), C12 |
| c4_c1_inversion_denied | C | C | 1 | 135.4 s | C14 |
| competitor_identity_forged | C | C | 1 | 151.6 s | (family C) |
| reciprocity_broken | C | C | 1 | 151.9 s | (family C) |
| endpoint_sup_pattern_forged | C | C | 1 | 152.3 s | (family C) |
| one_step_inequality_drops_b | D | D | 1 | 139.3 s | D1 |
| D_matrix_wrong_inverse | D | D | 1 | 142.5 s | D4, D5, D6, D7 |
| path_count_wrong | E | E | 1 | 142.3 s | E1 |
| claim_unique_at_silent | F | F | 1 | 143.0 s | F2 (hit `unique at (3,1,2)`) |
| claim_phase_transition | F | F | 1 | 151.3 s | (family F) |

12 of 31 mutations run, across families B, C (5), D (2), E and F (2) — the spec's "at least
eight, at least two from D" is met. Every run printed
`mutation_family_expected: X` / `mutation_family_observed: X` with `X` equal, and no run failed
a check outside its family.

## 5. My scripts, and my own failures

Scripts (all under `S = /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/checker03/`):
- `S/ck_core.py` — menu as `0..5 = ±e_x,±e_y,±e_z` with `anti(s) = s^1`, `axis(s) = s>>1`;
  `φ` by the three orbits; unnormalised integer weights; `TV` by the cross-multiplied integer
  form `Σ_s|W_a(s)Z_b − W_b(s)Z_a| / (2 Z_a Z_b)`; `c_1^{(d)}` by the 252 (resp. 56) multisets ×
  15 pairs, and by full ordered `6^{d−1}` enumeration per slot position.
- `S/ck01.py` — CK-01 (values, tie counts, maximizers, direction independence, `p↔q`, `(2,5,3)` inversion, homogeneity).
- `S/ck02.py` — grid `r=4` and brute-force `6c_1−1` at the six isolating endpoints and outside.
- `S/ck02a.py` — CK-02a: pattern rational functions vs the displayed polynomials (sympy),
  root counts, endpoint and **midpoint** suprema, function-level copy counts, reciprocity,
  reciprocal polynomials, Lipschitz numeric test.
- `S/ck_region.py` — the region attack (inside/outside scans, `(1,1,2)`, the ten declared line points).
- `S/ck04.py` — my own `3×3` integer **row transfer** over the 216 row states, exact
  Gauss-Jordan `(I−C)^{-1}` over `Fraction`, the bound attacks, and CK-05 (walk counts, tail table).
- `S/ck_sliver.py` — 17-point sign scan across each isolating interval.
- `S/mut/` — the 12 mutation stdout/stderr and `SUMMARY.txt`; `S/baseline.out` the baseline.

My own failures and coverage gaps, stated plainly:
1. I did **not** independently re-execute the plaquette family (D1, D2: 223,616 pairs × 4 sites
   × 4 triples, and the 5,184 maximal-coupling instances). I verified the pair-count arithmetic
   (`1296·171 = 221,616`, `+2,000 = 223,616`), proved Step 1 and Step 0 on paper, and relied on
   the runner for that execution. That is the largest hole in my check.
2. I did not re-derive block 01's linear congruential generator draws, so the 2,000 LCG pairs
   are unchecked by me.
3. My copy test (F1(a)) is equality of `TV` at 8 rational points, not a symbolic proof of
   identity for all `t`. Combined with the independent symmetry count (F1(b)) I regard the
   conclusion as settled, but it is not a formal proof.
4. My sliver check (F2) samples 17 points per interval; it does not certify the two slivers for
   every real `t`. The note's own argument does cover them once F2's missing sentence is added.
5. First command attempt used `timeout`, which does not exist on this macOS shell — harmless,
   re-run without it.
6. I read the runner's C-family and F-family source directly to know what its checks assert
   (needed for F1); all *numbers* I report are from my own code, never from the runner.
