# Refuting-checker findings — block 01, admissibility-induced-law-20260906

Seat: independent refuting checker (Opus 5). Branch
`physics-loop/admissibility-induced-law-static-vs-formation-20260906`, commit
`fc13903829`, worktree
`/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/sync-science-task-0c8fac`.
Read-only on tracked files; no git state changed; all arithmetic exact
(`fractions.Fraction`, Python ints, `sympy`); no float, no numpy.

Disjointness: I did not import the runner. My menu index order is
`(+x, +y, +z, −x, −y, −z)` (the runner's is `(+x, −x, +y, −y, +z, −z)`);
configurations are enumerated by base-6 integer codes; ranks are taken by
modular Gaussian elimination at two primes and by `sympy` nullspace (the
runner uses Bareiss); `det Φ` is obtained by eigen-decomposition of
`Φ = rJ + (p−r)I + (q−r)K`; the `f_j` are re-derived from an orbit count I
wrote myself; my cube configuration sample and my Brook cycle are my own.

## (1) VERDICT

**PASS-NO-BLOCKER.**

Nothing in the note or the runner is refuted. Every numeral I could reach
reproduced exactly on independent machinery, including both facts the
supervisor flagged. The five items in section (3) are editorial/wording only
(one is a redundancy in a proof, none changes a claim's truth value).

## (2) CK-01 … CK-12

| item | verdict | exact numbers I computed |
|---|---|---|
| CK-01 menu, orbits, rotations, spinors | CONFIRM | Six sympy projectors: Hermitian, idempotent, trace 1. `Tr(PP')` census `{1: 6, 0: 6, 1/2: 24}`; dot-product orbit census `{par 6, anti 6, orth 24}`; `⟨P,P'⟩ = 2Tr(PP')−1 ∈ {1,−1,0}` on all 36 pairs. 24 signed axis permutations with det `+1`; single menu orbit of size 6 (transitive); pair orbit rotation-invariant; **ordered**-pair orbits under the diagonal action have sizes (par 6, orth 24, anti 6). `U_z = diag(e^{−iπ/4}, e^{iπ/4})` induces `+x→+y, +y→−x, ±z` fixed — a proper signed permutation. `U_3 = (I − i(σx+σy+σz))/2` induces `+x→+y→+z→+x` — proper. Extra fact (stronger than the note): the two induced permutations **generate all 24**. |
| CK-02 static full conditionals = rule | CONFIRM | Mismatches 0 of 3888 (path3), 0/31104 each (P4, star4, cycle4, cycle4+exterior), at both triples. Cube8 on my own 549-configuration sample (all ≤1 site off reference, plus 500 draws of my own RNG, seed 424242): 0/26352 open and 0/26352 with exterior, at both triples. |
| CK-03 Brook / sum rule | CONFIRM | (P) path3 (3,1,2): 648×216 system, modular rank 215 mod 1000003 **and** mod 999983, exact sympy rank 215, nullspace dim 1, nullvector = static weight × 1/9, all entries same sign. (S) path3: modular ranks (216, 216) at λ=1/4 and λ=−1/8, exact rank 216, nullity 0. (S) single edge: rank 35, nullity 1, `(1+λ⟨s,t⟩)/36` has residual exactly 0 and sums to 1 at both couplings. Note's Brook cycle: `R(λ) = −(λ−1)²(2λ+1)/((λ+1)²(2λ−1)) = (−2λ³+3λ²−1)/(2λ³+3λ²−1)`; `R(1/4) = 27/25`; `R(−1/8) = 243/245`; `R−1 = −4λ³/((λ+1)²(2λ−1))`. My own cycle `(e1,e1,e1)→(e2,e1,e1)→(e2,e2,e1)→(e1,e2,e1)`: `R(λ) = (1+2λ)/(1+λ)²`, `R(1/4) = 24/25` — matches the spec's expected value. Both cycles for (P) with symbolic `(p,q,r)`: exactly 1. |
| CK-04 identity B1, `Σ μ_σ = 1` | CONFIRM | `μ_σ(v)·Π_k Z_k = μ(v)·Z_W` for every order and every configuration of path3 (Z_W 864 / 3174), P4 (10368 / 73002), star4 (10368 / 73002), cycle4 (20784 / 280086) at (3,1,2)/(5,2,4); every `Σ_v μ_σ = 1`. Cube8, six declared orders × my own 409-configuration sample: 0 mismatches of 2694 pairs at each triple, `Z_W = 6982520832` (3,1,2) and `17002040556294` (5,2,4). |
| CK-05 classification + censuses | CONFIRM | Equal-order sets and `max_k|A_k| ≤ 1` sets are **identical** on every window and both triples. path3 4/6 — exactly `(0,1,2),(1,0,2),(1,2,0),(2,1,0)`; P4 8/24; star4 12/24, all with the centre first or second; cycle4 0/24. Distinct laws 2 (sizes 4,2), 3 (8,8,8), 5 (12,6,2,2,2), 4 (8,8,4,4); `μ` present in the first three, absent for cycle4. Cube8: `max_k|A_k|` distribution over all 40,320 orders `{3: 40320}`; 0 orders with `max ≤ 1`; the last-formed site always has all 3 neighbours recorded. |
| CK-06 single-site variation lemma | CONFIRM | Re-derived `f_j` from my own orbit count for `j = 1..5`: all three formulas match the note exactly; `f_j(par) − f_j(anti) = (p−q)(p^j−q^j)` factors as `(p−q)²·Σ`; `f_j(anti) − f_j(orth) = (p−r)(q^j−r^j) + (q−r)(p^j−r^j)`; at `p=q` it is `2(p−r)²·Σ`. Cube instance, identity order at (3,1,2): `m = 3`, `y = 1`, j-multiset `{1,1}`, `Π_k Z_k` on (par, anti, orth) = **(10933678080, 7828254720, 9316270080)** — identical to the note. Three more orders of my own choosing: `(0,1,3,2,4,5,7,6)` → m=2, y=0, js={1}, (10933678080, 9251573760, 10092625920); `(0,4,2,6,1,5,3,7)` → m=6, y=2, js={1,1}, same three values as identity; `(7,6,5,4,3,2,1,0)` → m=4, y=5, js={1,1}, same; `(0,7,1,6,2,5,3,4)` (declared_b) → m=2, y=0, js={1,2}, (12615782400, 7828254720, 10092625920). Exactly three distinct values in every case. Proof text: see finding F1. |
| CK-07 normalizers and ranks | CONFIRM | `Σ_s φ(s,t) = p+q+4r` for every one of the six `t` (symbolic). `Z_2` orbit values `p²+q²+4r²`, `2pq+4r²`, `2pr+2qr+2r²`; differences `(p−q)²`, `p²−2pr+q²−2qr+2r²`, `2(p−r)(q−r)`. `det Φ = (p−q)³(p+q−2r)²(p+q+4r)`, obtained independently from the eigenvalues `p+q+4r` (×1), `p+q−2r` (×2), `p−q` (×3) — matches the note. rank Φ = rank `Z_2` = **4** at (3,1,2) (det 0), **6** at (5,2,4) (det Φ 621, det Z_2 385641), 1 at (2,2,2), 6 at (2,3,5). Both stated `2×2` minors verified symbolically. The homogeneous system "`Z_2(b,c)` constant" in the six `ψ(s)`: rank **6**, nullspace dim **0**, at both declared triples. |
| CK-08 menu-restriction witness | CONFIRM | `f(1) = f(−1) = f(0) = 1`, `f(1/2) = 19/16`, `f = 5/4` at `x² = 1/2`. At `(p,q,r) = (1,1,1)`: `μ` is uniform `1/6⁴` on cycle4 and `μ_σ = μ` for all 24 orders; same at `(2,2,2)`. |
| CK-09 the three readings / routes | CONFIRM | Route 3: the covariance system on `φ_abs(s)` has rank 5, solution space dimension **1** (same system as for `ψ`). Route 4b: cycle4 static site-0 marginal is exactly uniform `1/6` at both triples; the first-formed site's absence marginal is `(ac, bc, ac, bc, c², c²)` in the runner's menu order, uniform iff `a = b = c`. Route 5: `max_v|avg_σ μ_σ − μ|` = **899/2341664** (3,1,2), **3478458125/23066700436908** (5,2,4), **1585133/10007780364** (2,3,5) — all three identical to the note. Route 6a: path3 one-neighbour conditional equals the rule for every `v_1`; cycle4 at `v_1 = P(e_x)` gives **(219/866, 71/866, 72/433, 72/433, 72/433, 72/433)** against the rule's **(1/4, 1/12, 1/6, 1/6, 1/6, 1/6)**. Route 6b: chain rule given **all earlier records** 24/24 orders; given **recorded neighbours only** 0/24. (Extra, unclaimed by the note: on path3 the neighbours-only version reproduces `μ` for 4 of 6 orders — exactly the forest orders.) Route 4a: see finding F5 — I confirmed its conclusion by an independent rank argument rather than by Gröbner. |
| CK-10 numerals, quotes, fences, scope | CONFIRM | Every numeral listed above matches. All six axiom sentences quoted in the note are **verbatim** in `docs/MINIMAL_AXIOMS_2026-06-29.md` (whitespace-normalised substring test). The four fence sentences are present verbatim. Forbidden-word scan on the note for "certified", "closed", "complete", "global", "the natural reading", "any extension", "any reading", "the physical rule", "distinct orders give distinct", "witnesses the variation": **zero hits**. `claim_scope` names exactly the five windows, the two objects, Theorem B with its hypothesis "not all equal on the declared menu", the plaquette corollary and the path3 sum-rule failure — all executed or proved; it is neither wider nor narrower than the runner + proof. |
| CK-11 runner validity | CONFIRM | Fresh `python3 <runner>` → `TOTAL: PASS=53 FAIL=0`, exit 0. Its stdout is **byte-identical** to the pinned cache's stdout block (blank lines stripped). `--list-mutations` prints 41 entries. Twelve mutations run (table in section 4): 12/12 fail in exactly the declared family and in no other. Source scan for `d.d` / exponent float literals, `float(`, `numpy`, `nsimplify`, `.evalf`, `Decimal`: **zero hits**; imports are `re, sys, fractions, itertools, pathlib, sympy` only. `AUDIT_TIMEOUT_SEC = 600` and `AUDIT_INPUT_PATHS = (…)` are pure literals. Cache `runner_sha256` `48272bc7…065b61` equals my `shasum -a 256` of the runner file. `input_fingerprint_sha256` `e65ebc4c…24e68` reproduces exactly under the v1 rule in `scripts/runner_cache.py` (`b"runner-cache-input-fingerprint-v1\0"` + length-prefixed path/body per declared input). |
| CK-12 hidden-wall / overclaim scan | CONFIRM | Every occurrence of "infinite" in the note is inside a non-claim, a `next_trace_action`, an open-obligation row, or a fence. "Born", "gravity", "bridge" appear only in the `next_trace_action` field, the Gaussian-analogy remark (which states its hypotheses and calls itself cross-carrier) and the fences. No sentence says the order is physical, that distinct orders give distinct laws, or that the menu witnesses the axiom's variation clause. The records-only reading is called "a named premise" and never "the natural reading". N7's steelman explicitly declines the broader claims. |

## Supervisor's two flagged facts

**(a) The `6×6` determinant and ranks — CONFIRMED, with one wording note.**
The note writes `det Φ = (p+q+4r)(p+q−2r)²(p−q)³`, i.e. the determinant of the
**pair-weight matrix `Φ`**, not of the two-neighbour normalizer matrix
`Z_2 = Φ²`. That is correct as written (`det Z_2 = (det Φ)²`; at (5,2,4) I get
`det Φ = 621` and `det Z_2 = 385641 = 621²`). I re-derived the factorization
independently from the eigen-decomposition of `Φ = rJ + (p−r)I + (q−r)K`:
eigenvalues `p+q+4r` (multiplicity 1, all-ones), `p+q−2r` (multiplicity 2,
antipode-symmetric, zero-sum), `p−q` (multiplicity 3, antipode-antisymmetric).
At (3,1,2): `12, 0, 0, 2, 2, 2` → rank 4. At (5,2,4): `23, −1, −1, 3, 3, 3` →
rank 6. `rank Z_2 = rank Φ² = rank Φ` because `Φ` is real symmetric; the note
infers the `Z_2` rank from `det Φ` without saying so (finding F2, editorial).
The route's actual requirement — rank ≠ 1 — holds for all not-all-equal
positive triples by the two symbolic minors: `(p−q)²(p²+2pq+q²+8r²)` vanishes
only at `p=q`, and `((p−r)²+(q−r)²)(p²+2pr+q²+2qr+6r²)` vanishes only at
`p=q=r`, so at least one is nonzero. Confirmed symbolically.

**(b) The marginal reading's chain rule — the note's wording matches the
runner exactly. CONFIRMED.**
Runner `chain_product(order, v, condition_on_all_records, break_last)` builds
`Π_k μ(v_{E∪{x_k}})/μ(v_E)` with `E` = **all** earlier-formed sites when the
flag is true, and `E` = **earlier-formed neighbours of `x_k`** when it is
false. `chain_all` requires equality with `μ` for all 24 orders and all 1296
configurations (true); `orders_nbr_only` counts orders passing the second
version (0). The note's sentence — "makes `μ_σ = μ` for every order by the
chain rule when the conditional at the forming site is the static law's
conditional given all existing records … given only the recorded neighbors it
does so for 0 of 24 orders" — is exactly that, and the note's definition (iii)
of the marginal reading ("given all existing records … `μ(v_x | v_E)`, `E` the
recorded sites") is consistent with it. My independent computation reproduces
24/24 and 0/24. The block GOAL's own definition (iii) reads `μ(v_x | v_A)` with
`A ⊆ N(x)`; the note's Review record and `RESULTS.md` defect 2 both disclose
that this contract wording was corrected, so the divergence is declared, not
hidden.

## (3) Findings

All editorial / wording. None blocks.

**F1 — note lines 288–291 (B2 ⇒, the single-site variation lemma).**
"every factor is positive, so their product takes the same value on the three
orbits iff each factor does, iff `p = q = r`." As a standalone sentence this is
false for positive factors in general (they can compensate). It is *sound here*
only because the two displayed inequalities are sign-definite in the same
direction for every `j`: `f_j(par) ≥ f_j(anti)` always, so `Π f_j(par) ≥
Π f_j(anti)` with equality iff `p=q`; and when `p=q`, `f_j(anti) ≥ f_j(orth)`
always, so the anti/orth products separate unless `p=r`. The correct statement
is the case split "if `p ≠ q` use par vs anti; if `p = q ≠ r` use anti vs
orth". Note that `f_j(anti) − f_j(orth)` is **not** sign-definite off `p = q`:
at `(p,q,r) = (5,1,3)`, `j = 1`, I get `f_1(anti) − f_1(orth) = 46 − 54 = −8`.
The note does not claim general nonnegativity (it writes "at `p = q`:"), so
this is a compression, not an error. Severity: wording.

**F2 — note lines ~400–404 (route 4, E4c).** "the `6 × 6` matrix
`Z_2(b, c) = (Φ²)(b, c)` to have rank 1. Its rank is 4 at `(3,1,2)` and 6 at
`(5,2,4)`: `det Φ = …`". The colon presents `det Φ` as the reason for the
`Z_2` rank; that step uses `rank Φ² = rank Φ`, which needs `Φ` symmetric (it
is). One clause would close it. Both stated ranks are exactly right (I get 4
and 6 for both `Φ` and `Z_2`). Severity: editorial.

**F3 — note lines ~228–233 ("Symmetry of the pair weight on `Z^3` windows",
runner B9).** The derivation is valid, but it is redundant on this menu:
the 24 proper rotations act on **ordered** menu pairs with exactly three
orbits, of sizes 6 / 24 / 6, and each orbit is closed under swapping the pair
(I computed the orbit sizes). So isotropy alone — `φ` a function of the
ordered-pair orbit — already forces `φ(a,b) = φ(b,a)`; the edge-flip element
`t_{e_1} ∘ R_{e_2,π}` is not needed for menu-symmetry (it is needed for the
different statement that a lattice edge carries the same weight in both
orientations). Severity: editorial (a redundancy, not a defect).

**F4 — note line ~118 ("The axiom sentences used, verbatim:").** The first two
bullets are quoted and are verbatim in the axioms file (I checked all six
sentences). The third bullet — "Lattice: sites are the points of `Z^3` … Qubit:
the full one-site domain is `M_2(C)`" — is a paraphrase carrying no quotation
marks under a heading that says "verbatim". The axioms file reads "The full
one-site possibility domain has algebraic presentation `M_2(C)`", so the
content is faithful. Severity: editorial.

**F5 — route 4 on path3, order `(0,2,1)` (note lines ~382–392): a shorter exact
proof exists, which independently confirms the Gröbner result.** With order
`(0,2,1)` the last site's normalizer is `Z_2(v_0, v_2)` and both earlier sites
carry only absence factors, so `μ_σ = μ` on all configurations is *equivalent*
to `Z_2(v_0, v_2) = const · g(v_0) g'(v_2)`, i.e. to `Z_2` having rank 1. Rank 1
forces both stated minors to vanish, hence `p = q` and `p = q = r` in the
positive domain, and then `Z_2` is constant so `a = b = c`. This reaches the
note's solution set `{a=b=c, p=q=r}` with no Gröbner basis and no `sympy.solve`
— I did not reproduce the Gröbner basis elements `(a−1)u, (b−1)u, (p−q)²u,
(q−1)³u` themselves (CANNOT-REACH within budget), but the conclusion they
support is confirmed by this route. Severity: editorial (an available
simplification; the note is not wrong).

**F6 — observation, no change required.** E6b's positive half ("given all
earlier records, `μ_σ = μ` for every order") is a telescoping identity true for
*any* joint law and any order, not a property of this static law. The note does
not overclaim it (it says "by the chain rule" and immediately says the reading
is not one fixed nearest-neighbour rule), so the informative content of route 6
is the 0/24 half plus E6a's `219/866` vs `1/4`. Severity: none; recorded so the
supervisor knows the check's strength.

## (4) Mutation runs performed

Twelve mutations across all five families; each failed in exactly the declared
family and nothing else, exit code 1 in every case.

| mutation | expected | observed | TOTAL | exit | failing checks |
|---|---|---|---|---|---|
| `menu_drop_projector` | B | B | PASS=51 FAIL=2 | 1 | B2, B4 |
| `positivity_zero_entry_passes` | B | B | PASS=52 FAIL=1 | 1 | B10 |
| `sum_rule_pretends_consistent` | C | C | PASS=52 FAIL=1 | 1 | C6 |
| `compat_rank_off_by_one` | C | C | PASS=52 FAIL=1 | 1 | C5 |
| `formation_equals_static_on_cycle` | D | D | PASS=49 FAIL=4 | 1 | D1, D3, D4, D5 |
| `fj_j4_wrong` | D | D | PASS=52 FAIL=1 | 1 | D6 |
| `p4_census_wrong` | D | D | PASS=51 FAIL=2 | 1 | D4, D5 |
| `z2_rank_one` | E | E | PASS=52 FAIL=1 | 1 | E4c |
| `marginal_chain_rule_broken` | E | E | PASS=52 FAIL=1 | 1 | E6b |
| `order_mixture_equals_static` | E | E | PASS=52 FAIL=1 | 1 | E5 |
| `claim_order_physical` | F | F | PASS=52 FAIL=1 | 1 | F2 |
| `claim_infinite_volume` | F | F | PASS=52 FAIL=1 | 1 | F2 |

All twelve rows agree with the corresponding rows of the primary's
`RESULTS.md` mutation census, including the multi-check counts.

## (5) My scripts, and my own failures

Scratch directory `S = /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/checker`.

- `S/ck_a.py` — CK-01: sympy projectors, `Tr(PP')` census, 24 rotations,
  transitivity, ordered-pair orbits, `U_z`/`U_3` conjugation and the group they
  generate.
- `S/ck_b.py` — CK-06/07/08 symbolic: one- and two-neighbour normalizers,
  `Z_2` orbit values and differences, minors, `det Φ` and its eigenvalues,
  ranks at four triples, the `ψ` rank-6 system, `f_j` for `j = 1..5`, the
  menu-restriction witness.
- `S/ck_c.py` — CK-02/04/05 on path3, P4, star4, cycle4 (+ exterior) and a
  549-configuration cube sample: full conditionals, identity B1, `Σ μ_σ = 1`,
  classification and law censuses.
- `S/ck_d.py` — CK-05 cube plaquette lemma over all 40,320 orders; CK-06 cube
  single-site-variation instances.
- `S/ck_e.py` — CK-03: compatibility systems by modular rank at 1000003 and
  999983 plus exact sympy rank and nullspace; single-edge sum rule; both Brook
  cycles symbolically.
- `S/ck_f.py` — CK-09 routes 3, 4b, 5, 6a, 6b; CK-08 coincidence at (1,1,1).
- `S/ck_g.py` — CK-04 identity B1 on cube8 with exact `Z_W` over all `6⁸`
  configurations, six declared orders × my own 409-configuration sample.
- `S/run_main.txt`, `S/cache_stdout.txt`, `S/fresh_stdout.txt`, `S/muts.txt` —
  raw runner output, the cache's stdout block, and the mutation listing.

My own failures during this pass, recorded:

1. `ck_a.py` first run crashed (`TypeError: unsupported operand type(s) for +:
   'int' and 'MutableDenseMatrix'`) — I had summed sympy matrices with the
   builtin `sum`. Fixed with an explicit accumulator; no result depended on the
   broken version.
2. `ck_e.py` exceeded the 120 s foreground limit because `sympy.Matrix.rank()`
   on the 648×216 system is slow; I let it finish in the background (~3 min) and
   read the result. The modular ranks at both primes had already agreed at 215.
3. CANNOT-REACH within budget: I did not independently recompute the E4a lex
   Gröbner basis elements `(a−1)u, (b−1)u, (p−q)²u, (q−1)³u`, nor the raw
   `sympy.solve` the primary recorded as a could-not. I confirmed the
   *conclusion* of E4a by the independent rank-1 argument in finding F5.
4. CANNOT-REACH: I did not re-verify the runner's E1/E2/E4a/D3/C3-family code
   line by line; I verified their stated outputs against my own computations
   where I could construct them (E2's `ψ` rank, E3's dimension, E4c, E5, E6a,
   E6b, D-family) and read the source for E4a/E4b.
5. I ran 12 of the 41 mutations, not all 41 (budget). The 29 I did not run are
   covered only by the primary's own census.

## (6) Worktree observation (not a finding about the note)

`git status --porcelain` in the worktree shows one uncommitted modification:
`docs/audit/data/citation_graph_manifest.json` (edge_count 11859 → 11861,
node_count 4760 → 4761, adding the node
`admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06`
with `out_degree 2`). Its mtime is 2026-09-06 14:22:44, inside my working
window (my first runner execution was 14:16). I ran no command that writes to
the repository — only reads, the runner and twelve mutation runs (the runner
opens files read-only), my own scripts under `S`, `shasum`, and read-only git
commands. So either the manifest was already dirty when I started (the initial
`git status` snapshot handed to me was truncated before this path) or another
process is writing in this worktree concurrently. Flagging it for the
supervisor to resolve before the freeze; the change itself is consistent with
registering this block's note in the citation graph.
