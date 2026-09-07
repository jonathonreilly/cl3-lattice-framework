# CHECKER — block 05 (monotone-order formation law: rows, columns, corner law, class boundary)

Independent refuting checker (Opus 5). Disjoint machinery, exact arithmetic only.
Worktree read-only; all artifacts under the scratch dir.

## 1. VERDICT

**FIX FIRST — one false sentence in P7(b); everything else reproduces exactly.**

- **F1 (must fix, note lines 413–416).** The P7(b) "executed pattern" sentence is **false**
  as a statement about recorded sets, and it is a mechanism sentence the GOAL addendum A1
  forbade beyond the executed one. The runner does not test it.
- Every theorem (P1–P7) and **every** numeral in the note reproduced on my own code:
  P1's counts and recorded sets, the bridge identity, the transpose symmetry, the column
  theorem, the corner law at every block position, the six staircase defects, the minimal
  staircase conditional row, `P(c|c,c) > K(c→c)` on all 210 non-constant triples, the mirror
  count and TV, the snake `3×3` and `4×3` defects at both triples. No numeral is wrong.
- The proofs of P5 (partial sums + `n`-row reduction) and P6 (Cauchy–Schwarz + orbit algebra)
  are **sound as written**; I re-derived both line by line and found no gap.
- P4's infinite-strip and quadrant sentences are sound; the restriction lemma they invoke is
  correct and I verified it numerically in both directions.
- Runner: `TOTAL: PASS=38 FAIL=0`, 60.2 s wall; stdout **byte-identical** to the pinned cache;
  `runner_sha256` matches; 12 mutations run, each failing exactly one check in exactly its
  declared family.
- Two low-severity wording items (F2, F3) below. Nothing else is refuted.

## 2. CK table

| CK | verdict | exact numbers |
|---|---|---|
| CK-01 P1 | CONFIRM | linear extensions enumerated by my own recursion: `2×3` **5**, `3×3` **42**, `3×4` **462**; memoized count `4×4` **24024**. Recorded set `= {left, above} ∩ S` for **every site of all 509** extensions, **0 violations**. Direct summation over all `6^6 = 46656` configurations of `2×3`: all 5 extension laws **identical**, sum `= 1`, at `(3,1,2)` and `(5,2,4)`. ATTACK (Young shape `{(0,0),(0,1),(0,2),(1,0),(1,1)}`): 5 extensions, all give the **same** law — P1's mechanism extends to any down-set shape; the note claims only rectangles (narrower, not wrong). ATTACK (site before its ABOVE neighbour, after its LEFT: order `(0,0)(1,0)(1,1)(0,1)(0,2)(1,2)`): law **differs** from `μ_P` on **23328 / 46656**, TV `691/30888` — the class boundary is real, and the note claims nothing there. |
| CK-02 P2/P3 | CONFIRM | `Z_2(a,b) = Z_1^2 (K^2)(a,b)` on all 36 pairs; `r(s|a,b) = K(a→s)K(s→b)/(K^2)(a,b)` on all **216** triples, **0 mismatches**, both triples. P2's product formula vs block-01's definition entrywise on `2×3`: **0/46656** mismatches, both triples. Transpose `2×3` vs `3×2`: **0/46656**, both triples. Transpose `2×4` vs `4×2` by direct summation over all **1679616** configurations at `(3,1,2)`: **0** mismatches, sum `= 1`. Boundary conventions in the product formula match block 01's definition exactly (`(0,0) → 1/6`, first row/column `→ K`, interior `→ β`). |
| CK-03 P4 | CONFIRM | All three columns AND all three rows of `3×3` at both triples: TV from the `K`-chain `= 0`; column joints cross-checked between my `6^9` direct summation and my variable-elimination scheme — **identical dictionaries**. All four columns of `3×4` at `(3,1,2)`: TV `= 0`. Column-restriction lemma verified numerically (`2×3→2×2`, `3×3→3×2`, `2×4→2×3`, `2×4→2×2`, `3×3→3×1`: all exact) and row-restriction/projective consistency (`3×3→2×3`, `2×3→1×3`, `3×2→2×2`: all exact). The **transposed** restriction lemma is used only on finite rectangles (P4 proof line 288–290), which is legitimate; the infinite-strip route (lines 290–296) transposes nothing and is sound. |
| CK-04 P5 | CONFIRM | Corner law `π` at **all 4** block positions of `3×3` computed by **direct summation over all `6^9 = 10077696` configurations** (integer numerators over one denominator): **0/1296 mismatches at each position, including both blocks in rows (1,2)** — the "lower rows" step is genuinely exercised, and each block marginal sums to exactly `1`. All **3** block positions of `2×4` by direct summation over `6^8`: **0/1296** each. All **6** blocks of `3×4`: **0/1296** each. `P(c) = 1/6` for all `c`; `P(a,b|c) = K(c→a)K(c→b)` on all 216 `(c,a,b)`. `K` and `K^2` are both doubly stochastic (all row and column sums `= 1`), which is what the two summation steps of the proof need. |
| CK-05 P6/P7 | CONFIRM | `P(d\|c=+x, b=+x)` at `(3,1,2)` `= 227/858, 197/2574, 212/1287, 212/1287, 212/1287, 212/1287` against `K = 1/4, 1/12, 1/6, 1/6, 1/6, 1/6` — matches the note verbatim; the corner-law conditional equals the direct `3×3` block marginal on all **216** `(c,b,d)`. Staircase five-site TV defects from the `K`-chain, **from the `6^9` direct sum** at `(3,1,2)`: `RRDD`/`DDRR` `381233308277/21948466113288`, `RDRD`/`DRDR` `1874214125027/58529242968768`, `RDDR`/`DRRD` `3021054877865/117058485937536` — all three literals match. At `(5,2,4)`: `113047203771057118/10664903944307284749`, `603989722568508979/30035851924783781538`, `1686264713485074893/105125481736743235383` (nonzero). `P(c\|c,c) > K(c→c)`: **210 strict, 6 equal** on `{1..6}^3`, equality exactly at the six constant triples; 400 random non-constant **rational** triples: **0 violations** (so the inequality is not an integer-grid artefact). Mirror on `2×3` at `(3,1,2)`: differs on **32616/46656**, TV `2764753/79505712`; at `(2,2,2)` identical (0 differences). Mirror rows and columns on `2×3` and `3×3` are exact `K`-chains. Snake `3×3` column TVs `0`, `3161/7227792`, `3583442207/7981260404832` at `(3,1,2)` and `0`, `104792291/623922798807`, `45687143997705515/267592135329891871884` at `(5,2,4)`; snake `4×3` (4 rows, 3 columns) `3583442207/7981260404832`, `23960429927/34827318130176`, `3583442207/7981260404832` at `(3,1,2)` and `45687143997705515/267592135329891871884`, `36156719468443362521/135401620476925287173304`, `45687143997705515/267592135329891871884` at `(5,2,4)` — **every literal matches**. Snake rows are `p_0` and all vertical pairs `(1/6)K` on `2×3`, `3×3`, `4×3`. `p_0 P_rl = p_0` on all 216 row states, `P_rl` row sums all `1`. **REFUTED: the P7(b) mechanism sentence** — see F1. |
| CK-06 numerals/fences | CONFIRM (with F1, F2, F3) | Every numeral ≥ 4 digits in the note is in my verified set. Forbidden phrases: **none present**. "Pickard" appears exactly twice, line 173 (Prior art, section starts 164) and line 527 (Imports, section starts 524) — correct. No floating-point literal in the note or the runner. `claim_scope` matches the theorem statements; wording items F2/F3 below. |
| CK-07 runner | CONFIRM (fingerprint CANNOT-REACH) | `TOTAL: PASS=38 FAIL=0`, 38 PASS lines, 0 FAIL lines, 60.22 s user time. `--list-mutations` prints **23** mutations across families B–F. Stdout lines 1–52 are **byte-identical** to cache lines 10–61. `shasum -a 256` of the runner `= 5104a93e01aa413390030eeb8193040e203a0646910461de9b0af00d7400407e`, matching `runner_sha256` in the cache. **CANNOT-REACH:** `input_fingerprint_sha256: 1a49b041...` — the hashing scheme is not defined in the runner (it is written by the audit harness); I tried concat-of-bytes, path+bytes and path:sha-line forms over both the 2- and 4-path lists and none reproduces it. Not a note defect; flagged only as unreproduced by me. |
| CK-08 hidden wall / overclaim | CONFIRM (with F2, F3) | No "as is standard" / "the framework provides" / "canonical". No "the physical order"; "physical" appears only in explicit non-selection sentences. "unique" appears only in `next_trace_action` (about a future block) and the obligation table's "open; not this note". N1–N8 gate present and each entry checks out against my executions. |

## 3. Findings

### F1 — REFUTED: the P7(b) "executed pattern" sentence is false (note lines 413–416). Severity: **MEDIUM — fix before landing.**

The note says:

> The executed pattern: on `3×3` column `0` is a chain and it is the column where row `2`
> starts, so that each of its sites below the first has the site above as its sole recorded
> neighbor; on `4×3` no column has that property in every row.

**Counter-computation (exact, recorded sets of the declared snake).** Snake on `3×3`
(row 0 left→right, row 1 right→left, row 2 left→right) has order
`(0,0)(0,1)(0,2)(1,2)(1,1)(1,0)(2,0)(2,1)(2,2)` and column-0 recorded sets

- `(0,0) → {}`
- `(1,0) → {(0,0), (1,1)}`   ← **two** recorded neighbours
- `(2,0) → {(1,0)}`

Site `(1,0)` is a site of column 0 below the first, and the site above it is **not** its sole
recorded neighbour: `(1,0)` is the last site of the right-to-left row 1, so its left-hand
partner `(1,1)` is already recorded. The named property therefore fails for column 0 of the
`3×3` snake, the very column the sentence explains. The property holds only for `(2,0)`.

Worse, the same property fails identically on `4×3` for the same reason, so it does not
separate the two executions: `4×3` column 0 recorded sets are
`(0,0) → {}`, `(1,0) → {(0,0),(1,1)}`, `(2,0) → {(1,0)}`, `(3,0) → {(2,0),(3,1)}`. What the
sentence names as the distinguishing property is present in `4×3` column 0 in exactly one of
its three non-initial rows, and in `3×3` column 0 in exactly one of its two — the counts do
not distinguish the chain case from the non-chain case at all.

The GOAL addendum A1 is explicit: "State P7(b) with the convention declared, the `3×3` and
`4×3` executions, and **no mechanism sentence beyond the executed one**." This sentence is a
mechanism sentence, it is beyond the executions, and it is false.

**Correct statement.** Delete the sentence, or replace it with the executed facts only:
"On `3×3` the snake's column `0` is the `K`-chain and columns `1` and `2` are not; on `4×3`
no column is. No mechanism is claimed." (The measured defects `0`, `3161/7227792`,
`3583442207/7981260404832` and the three `4×3` defects are all correct and stay.)

The runner has no check for this sentence (E7/E8 test the defects only), so the falsifier list
and the 38 checks do not catch it.

### F2 — the staircase definition is narrower than P6's proof and than P6's own scope sentence (note line 157 vs line 349). Severity: **LOW.**

Line 157 defines "A **staircase** is a path of right and down steps **from the top-left site**".
Line 349 then says "every other monotone path is covered by this theorem exactly when it
turns". A right/down path that does not start at `(0,0)` is not a staircase under the line-157
definition, so the line-349 sentence asserts coverage the definition does not grant. The proof
itself does cover it (the block law `π` holds at **every** block position `i, j ≥ 1`, which I
confirmed by direct summation at all four positions of `3×3` including rows `(1,2)`), so the
theorem is true at the wider scope. Fix: drop "from the top-left site" from line 157, or
restrict line 349 to paths from the top-left site.

### F3 — P4's statement says "every row and every column **of finite length**" for the infinite strip and the quadrant (note lines 280–283). Severity: **LOW (wording).**

On `S_W` the columns are infinite and on the quadrant both rows and columns are; no row or
column of either object has finite length, so the sentence as written asserts nothing about
them. The proof (lines 290–299) proves the intended thing — every finite segment is the
`K`-chain, hence the infinite column's law is the `K`-chain by consistency. Fix: "every row and
every column, and every finite segment of one, has the law `p_0` (the `K`-chain)". I verified
the consistency the argument needs: the column-restriction lemma (`μ_P` on `n×W` restricted to
the first `W'` columns equals `μ_P` on `n×W'`) and the row-restriction/projective-limit
consistency both hold exactly on every case I tested.

### Attacks that did NOT break anything (reported for completeness)

- **P5's proof, step by step.** I re-derived the telescoping: summing `β_0` gives
  `Σ_{β_0} K(β_0→α_0)K(β_0→β_1) = (K^2)(α_0, β_1)`, which cancels the column-1 denominator;
  induction to `β_{j−2}` reproduces the note's displayed weight **exactly**. Summing
  `α_0 … α_{j−2}` uses the **column** sums of `K` — `K` is doubly stochastic (verified: all row
  and column sums `= 1`), so the note's parenthetical "the columns of `K` sum to one" is right.
  `R` sums to one in the order `α_{W−1} … α_{j+1}` then `β_{W−1} … β_{j+1}` exactly as written.
  The `j = 1` edge case ("nothing to sum when `j = 1`") is consistent. The three-step `n`-row
  reduction (A4) is stated and each step is correct. **No gap.**
- **P6's Cauchy–Schwarz step.** `Σ_a x_a^2/y_a ≥ (Σ x_a)^2/Σ y_a` with `x_a = K(c→a)`,
  `y_a = (K^2)(a,c)`; `Σ_a x_a = 1` (rows of `K`), `Σ_a y_a = 1` (columns of `K^2`), so the
  bound is `K(c→c)`. Equality iff `x_a/y_a` constant, hence `= 1`, hence `K(c→·) = (K^2)(·,c)`.
  **Orbit algebra re-derived independently:** `(K^2)(orth) = 2r(p+q+r)/Z_1^2 = r/Z_1 ⟺ p+q = 2r`;
  `(K^2)(par) = (p^2+q^2+4r^2)/Z_1^2 = p/Z_1 ⟺ q(q−p) + 4r(r−p) = 0`, which at `r = (p+q)/2`
  factors as `(q−p)(p+2q) = 0`, forcing `p = q` and then `r = p`. **Identical to the note.**
  (The note uses only the orthogonal and parallel constraints; the antiparallel one,
  `q^2 + 4qr − pq − 4r^2 = 0`, is a further necessary condition it does not need — using a
  subset of necessary conditions is valid here.) The "kernel would be `K`" step is correct:
  Markov + pair law `(1/6)K` + uniform marginals forces `T = K` at every step.
- **P3 for asymmetric `φ`.** The stated reason — `r(s|a,b) = φ(s,a)φ(s,b)/Σ_t φ(t,a)φ(t,b)` is
  symmetric in `(a,b)` by the product form alone — is correct and does not use symmetry of `K`.
- **P5's `K^2` vs `K` remark (D6).** `K(orth) = K^2(orth) = 1/6` at `(3,1,2)` (`p+q = 2r`) and
  `4/23` vs `88/529` at `(5,2,4)`; `K ≠ K^2` as matrices at both triples, so the note's
  "as a law, not entries" phrasing is the right one.

## 4. Mutation runs (12, four at a time, background)

| mutation | family expected | family observed | result |
|---|---|---|---|
| `extension_count_wrong` | B | B | PASS=37 FAIL=1 (B1) |
| `recorded_set_forged` | B | B | PASS=37 FAIL=1 (B2) |
| `bridge_identity_broken` | C | C | PASS=37 FAIL=1 (C1) |
| `transpose_symmetry_broken` | C | C | PASS=37 FAIL=1 (C3) |
| `column_chain_forged` | D | D | PASS=37 FAIL=1 (D2) |
| `corner_law_wrong_denominator` | D | D | PASS=37 FAIL=1 (D4) |
| `staircase_claimed_chain` | E | E | PASS=37 FAIL=1 (E2) |
| `snake_column_claimed_chain` | E | E | PASS=37 FAIL=1 (E7) |
| `mirror_law_equal_claimed` | E | E | PASS=37 FAIL=1 (E4) |
| `snake_row_kernel_not_invariant` | E | E | PASS=37 FAIL=1 (E5) |
| `claim_all_orders_same_law` | F | F | PASS=37 FAIL=1 (F2) |
| `claim_author_in_theorem` | F | F | PASS=37 FAIL=1 (F3) |

Every mutation failed **exactly one** check and in **exactly** its declared family; five of the
seven families (B, C, D, E, F) exercised. Clean run: `TOTAL: PASS=38 FAIL=0`.

## 5. My machinery, and my own failures

All under `.../scratchpad/checker05/`:

- `mylib.py` — orbits, `φ`, `K`, `K^2`, `Z_1`, `Z_2`; linear-extension enumeration and memoized
  counting; recorded sets for an arbitrary order; block 01's formation-law definition evaluated
  directly (`mu_direct`); `int_brute` (exact enumeration of all `6^{nW}` configurations with
  integer numerators over one denominator, built from the **definition**, not from P2's product
  formula); a generic exact variable-elimination marginalizer over the factor graph
  (`ve_marginal`); `tv`, `chain_law`.
- `ck1.py` (P1 + the two attacks), `ck2.py` (bridge, product formula, transposes, `2×4` corner
  law, mirror), `ck3_brute33.py` (**the `6^9` direct summation of `3×3`**, 50.7 s, total exactly
  `1`; columns, four block positions, six staircases), `ck5.py` (brute-vs-VE cross-check, blocks,
  216 triples), `ck4.py`/`ck6.py`/`ck8.py` (columns, staircases, snake `3×3`/`4×3`, `3×4`, `P_rl`,
  mirror, mechanism test), `ck7.py` (restriction lemmas, double stochasticity, D6 remark).
- Outputs: `run_main.txt`, `mut_*.txt`, `mut_exits.txt`, `ck3_out.txt`, `brute33_312.pkl`.

**Disjointness.** No runner import. Two independent schemes of my own: (a) full enumeration over
all configurations with integer numerators over a single common denominator
`6 · Z_1^{#one-neighbour} · L^{#two-neighbour}` (`L = lcm` of the three `Z_2` orbit values), built
from block 01's definition; (b) exact variable elimination over the factor graph, with `Fraction`
values and a column-major elimination order. They agree exactly on the `3×3` column joints, so
(b) is trustworthy where (a) is unaffordable (`3×4`, `4×3`). Neither is the note's row-transfer.

**My own failures / limits.**
1. I could not reproduce `input_fingerprint_sha256` (CK-07): the scheme lives in the audit
   harness, not the runner. `runner_sha256` and the whole stdout body do reproduce.
2. `3×4` (`6^12`) and `4×3` were **not** done by brute force — only by my variable elimination.
   For those the disjointness is at the level of my own independent elimination code, not a raw
   sum. Said here per the spec.
3. My first `ck4.py` invocation used `timeout`, which is absent on this Mac; re-run without it.
4. I did not attempt an independent proof that the note's P7(b) *executed defects* are the only
   possible ones for other snake sizes; I checked `2×3`, `3×3`, `3×4` and `4×3` only.
