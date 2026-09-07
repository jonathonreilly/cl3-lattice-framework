# Block 02 — REFUTING CHECKER findings (disjoint machinery)

Campaign `admissibility-induced-law-20260906`, block 02.
Target branch `physics-loop/admissibility-induced-law-block02-infinite-strip-sweep-20260906`, commit `d52844f1c8`.
Worktree treated as read-only; no git state changed; no tracked file edited.

Machinery built independently of both runners: menu = the six `±e_a` unit
vectors with the dot-product orbit (`+1 → p`, `−1 → q`, `0 → r`); row states
enumerated as base-6 tuples; the row kernel built from the definition
(product of the rule's conditionals with its own normalizer) before any
comparison with the note's closed formula; the 24 proper rotations generated
as signed axis permutations of determinant `+1`; the quotient built from my
own orbit reduction; the algebraic step done by elimination over the rational
function field `Q(λ)` plus exact rational interval evaluation and my own Sturm
bisection — **no resultant** (the runner's E7 uses one). All arithmetic exact
(`fractions.Fraction`, Python ints, `sympy` rationals/polynomials). No float
was used as evidence anywhere.

---

## 1. VERDICT

**FIX FIRST** — two items (F-1, F-3), plus four recommended (F-2, F-4, F-5, F-6).

Nothing in Theorems C1, C2, E, F, F5, in `claim_scope`, in the machine-status
block or in the runner was refuted. Every executed numeral in the note
reproduced exactly on my own machinery, including all four facts flagged for
special care. The two fix-first items are (a) a **false general sentence in
the No-Go gate's route-1 row** that over-closes a route, refuted by an exact
counter-computation below, and (b) a classical theorem used in the C2 proof
that is quoted, not proved, and not declared in `Imports`.

Required before landing:

- **F-1** — note line 479: "row sweeps with any per-row direction and **any row
  order** are covered by Theorem E (each row is still a path swept from an end
  with one recorded neighbor below…)". False for a non-monotone row order.
  Narrow to "any *monotone* row order (rows in increasing or decreasing index
  order)".
- **F-3** — note line 234: the Carathéodory extension theorem is used by name
  in C2 and is neither re-proved at scope nor listed in "Prior art" (line 152 ff)
  or "Imports" (line 617 ff), against the note's own stated discipline that
  classical facts are re-proved at the scope where they are used.

---

## 2. CK table (exact numbers, my computation)

| CK | object | verdict | my exact numbers |
|---|---|---|---|
| CK-01 | `φ` symmetric; `Z_1 = p+q+4r` for all 6 states; `K` symmetric, rows and columns sum to 1 | **CONFIRM** (symbolic in `p,q,r`) | 0 failures on 36 pairs / 6 states |
| CK-01 | `Z_2(a,b) = Z_1² (K²)(a,b)` | **CONFIRM** (symbolic) | 0 failures / 36 pairs |
| CK-01 | `K` spectrum cited in E4 | **CONFIRM** | `{1: 1, (p+q−2r)/Z_1: 2, (p−q)/Z_1: 3}` — matches the note verbatim |
| CK-01 | path static law = end-swept path formation law, `W = 2, 3` | **CONFIRM** | identical by construction and by execution, 0 deviations |
| CK-02 | plaquette edge `{0,1}` sub-window conditional | **CONFIRM** | 0/36 mismatching complements, both triples |
| CK-02 | plaquette site `{0}` | **CONFIRM** | 0/216, both triples |
| CK-02 | cube edge `{0,1}` | **CONFIRM** | 0/46656, both triples |
| CK-02 | cube face `{0,1,2,3}` | **CONFIRM** | 0/1296 complements × 1296 states, both triples |
| CK-02 | **undeclared** sub-window: two opposite cube corners `{0,7}` (positive extension) | **CONFIRM** — identity holds | 0/46656, both triples |
| CK-02 | finite-range class counts (C6) | **CONFIRM** | cube edge: adjacent-outside = `{2,3,4,5}` → 6⁴ = 1296 classes, 2 non-adjacent sites; cube site: `{1,2,4}` → 216 classes, 4 non-adjacent; plaquette site: `{1,3}` → 36 classes, 1 non-adjacent — all three match the note |
| CK-03 | C2 proof, step by step | **CONFIRM with two documentation defects** | see F-3, F-4, F-5 |
| CK-04 | row kernel from the definition vs the note's closed formula (E2), entrywise | **CONFIRM** | `W = 2`: 0/1296; `W = 3`: 0/46656 mismatches; both triples; every row of `P` sums to 1 |
| CK-04 | `p_0 P = p_0` | **CONFIRM** | `W=2` 0/36, `W=3` 0/216, **`W=4` 0/1296**, both triples (fact (d)) |
| CK-04 | vertical and horizontal pair laws `= (1/6)K` | **CONFIRM** | 0 deviations at every column, `W=3 n=2` and `W=2 n=3`, both triples |
| CK-04 | **diagonal pair `(α_{j−1}, β_j)` law `= (1/6)K²`** (fact (c)) | **CONFIRM** | 0/36 deviations at `j = 1` and `j = 2`, `W=3`; 0/36 at `W=2`; both triples |
| CK-04 | direct finite-strip formation law vs `p_0 P^{n−1}` | **CONFIRM** | `W=3,n=2` and `W=2,n=3`: row-marginal deviations 0; last-two-row joint 0/46656 and 0/1296; both triples |
| CK-04 | telescoping proof uses only `K` symmetric doubly stochastic + `Z_2 = Z_1²K²` | **CONFIRM** | verified line by line; the load-bearing inputs are exactly transitivity (`Z_1` constant) and symmetry of `φ` — both independently broken below |
| CK-04 | constant rule `(2,2,2)` boundary | **CONFIRM** | `K` uniform ⇒ `p_0` uniform ⇒ invariant, trivially |
| CK-04 | asymmetric-weight control | **CONFIRM** (runner D7; reproduced in kind by my non-transitive control) | |
| CK-04 | three-recorded-neighbour cube witness (D8) | **CONFIRM** | joint law of `(v_3,v_5,v_6)` under the 7-site chain at `(3,1,2)` is off proportionality to `Z_3` on **210/216** triples — exactly the note's number |
| CK-04 ATTACK | column sweep, `W=3, n=3` | **survives** | top-row marginal deviates from `p_0` on **0/216** states |
| CK-04 ATTACK | snake / boustrophedon (right-to-left rows) | **survives** | `p_0 P_rev = p_0`, 0/216 violations |
| CK-04 ATTACK | diagonal sweep, `W=3, n=3` | **survives** | rows 0, 1, 2 deviate on 0/216 each; horizontal and vertical pair-parallel probabilities both exactly `1/4` |
| CK-04 ATTACK | **non-monotone row order (0, 2, 1)**, `W=3, n=3` | **BREAKS** | row-1 marginal deviates on **216/216** states (see F-1) |
| CK-04 ATTACK | non-transitive 8-point menu (`Z_1` not constant) | **BREAKS**, as expected | `Z_1 = (18,18,18,18,18,18,22,22)`; `K` not symmetric; `p_0 P ≠ p_0` on 64/64 (`W=2`) and 512/512 (`W=3`) |
| CK-05 | row orbits under the 48 maps | **CONFIRM** | 8 at `W=3`, 3 at `W=2`, both triples |
| CK-05 | `T(gρ, gρ′) = T(ρ, ρ′)` | **CONFIRM** | 0 failures in 82944 checks at `W=3` (48 maps × 8 reps × 216 rows); 0/62208 exhaustively at `W=2` |
| CK-05 | **`T` has real spectrum** (fact (a)) | **CONFIRM, structurally** | `T = V·diag(A)` with `V` symmetric (0 failures on all 216² pairs) and `A > 0` on all 216 states, so `diag(A)^{1/2} T diag(A)^{−1/2} = diag(A)^{1/2} V diag(A)^{1/2}` is symmetric. Independently: charpoly(`Q`) divides charpoly(`T`) at `W=2` (exact remainder 0), and every root of charpoly(`Q`) is real by my own Sturm count in all four cases |
| CK-05 | `Q` well defined on every orbit member; entries positive | **CONFIRM** | exact, all orbits |
| CK-05 | charpoly at `(3,1,2)`, `W=3` | **CONFIRM** | `λ⁵(λ³ − 7312λ² + 2578432λ − 221134848)` — identical to the note |
| CK-05 | charpoly at `(5,2,4)`, `W=3` | **CONFIRM, irreducible** | `λ⁸ − 185171λ⁷ + 1095911038λ⁶ − 1772274674784λ⁵ + 469450026668192λ⁴ + 67550038108063488λ³ − 17237755848001351680λ² − 1439162188263618969600λ − 14640126202850181120000`, `is_irreducible = True` — identical to the note |
| CK-05 | charpoly at `W=2` | **CONFIRM** | `(3,1,2)`: `λ(λ² − 296λ + 2112)`; `(5,2,4)`: `λ³ − 2063λ² + 67814λ − 190440` |
| CK-05 | Perron root isolation | **CONFIRM** | `λ₁ = 6945.337824257111051299945…` at `(3,1,2)` and `179107.4288028301852413067…` at `(5,2,4)`, `W=3` (own bisection, width < 10⁻⁴⁰) — the note's truncations `6945.337824257111…` and `179107.428802830185…` are correct |
| CK-05 | Perron vector by elimination over `Q(λ)`; residual on **every** row incl. the dropped one | **CONFIRM** | numerator of `(Q − λI)x` divisible by the minimal polynomial on all 8 rows, all four cases; every entry strictly positive on the isolating interval by exact interval evaluation |
| CK-05 | left Perron vector `ℓ = A ρ₁` (derived myself, not read off) | **CONFIRM** | `ℓᵀQ = λ₁ℓᵀ` mod minpoly: 0/8 violations, both triples |
| CK-05 | limit-law formula `w ∝ A ρ₁²` | **CONFIRM** (corroborated by the finite-`n` sequence converging to the same enclosure) | |
| CK-05 | **`s_∞` enclosure at `W=3`** (fact (b)) | **CONFIRM** | `(3,1,2)`: `s_∞ = 0.25611098728577869086123064…` (own interval, width 4.9·10⁻⁴³) ⊂ note's `[0.2561109872857786908612, 0.2561109872857786908613]`. `(5,2,4)`: `s_∞ = 0.21991516168701978150758266…` (width 2.4·10⁻⁴⁴) ⊂ note's `[0.2199151616870197815075, 0.2199151616870197815076]`. Both endpoints correctly rounded outward |
| CK-05 | `s_∞` enclosure at `W=2` | **CONFIRM** | `(3,1,2)`: `0.25594308890161876620605…` ⊂ `[0.255943088901618766, …767]`; `(5,2,4)`: `0.21987417612409003162695…` ⊂ `[0.219874176124090031, …032]` |
| CK-05 | degree of `s_∞`: 3 and 8 at `W=3` (fact (b)) | **CONFIRM**, by conjugate separation, no resultant | the 3 (resp. 8) conjugate images `g(λ_i)` are pairwise disjoint exact intervals ⇒ `s_∞` generates `Q(λ₁)` ⇒ degree 3 and 8. `W=2` degrees 2 and 3 likewise |
| CK-05 | the note's claimed minpoly of `s_∞` at `(3,1,2)` | **CONFIRM** | `2647547323586176y³ − 2190008305118016y² + 544429860087294y − 40261879885473` is irreducible of degree 3 with exactly **1** root inside the note's enclosure (Sturm) and 3 real roots overall; with degree(`s_∞`) = 3 this identifies it |
| CK-05 | exclusion of the formation value | **CONFIRM** | `1/4 = 0.25` and `5/23 = 0.21739130434782608…` lie outside every one of the four enclosures |
| CK-05 | finite-`n` centre-row values `n = 3,5,7,9,11,13` | **CONFIRM, all 12 decimals** | `(3,1,2)`: 0.2559429133, 0.2561061627, 0.2561108435, 0.2561109828, 0.2561109871, 0.2561109872; `(5,2,4)`: 0.2198741514, 0.2199144959, 0.2199151505, 0.2199151614, 0.2199151616, 0.2199151616 — each is the exact 10-digit truncation of my exact rational. `n = 3` exact values `578647/2260844` and `3731173618465/16969587349457` both match |
| CK-05 | **second-eigenvalue bound** (fact (b)) | **CONFIRM**, by my own bisection isolation of every root | `(3,1,2)`, `W=3`: `m = 225.4139310693809…`, `|λ₂/λ₁| ≤ 0.0324554307902…` — the note's `225.413932` and `0.0324554308` are correct round-ups. `(5,2,4)`: `m = 3376.351457076775…`, ratio `≤ 0.0188509850186…` — note's `3376.351458` and `0.0188509851` correct. `W=2`: ratios `≤ 0.0253424358…` and `≤ 0.0149117889…` — note's `0.02534244` and `0.01491179` correct |
| CK-05 | all eigenvalues of `Q` real | **CONFIRM** | Sturm counts 8, 8, 3, 3 = matrix sizes, all four cases; consistent with the symmetrization above. The bound is by real-root isolation alone, as claimed |
| CK-05 | nonzero eigenvalues simple | **CONFIRM** | `(3,1,2)`: `λ⁵` × irreducible cubic ⇒ 3 distinct nonzero; `(5,2,4)`: irreducible octic with nonzero constant term ⇒ 8 distinct nonzero. Zero multiplicity 5 at `(3,1,2)` matches F3 |
| CK-05 | Wielandt re-proof of Perron–Frobenius (F2) | **CONFIRM** | every step checked as written: attainment of `max r(v)` on the compact set `T(simplex) ⊂ {v>0}`, `r(Tv) ≥ r(v)`, the contradiction giving `Tv* = λ₁v*`, `|μ| ≤ r(|z|) ≤ λ₁` with the equality case, geometric simplicity by the `v* − cw` argument, algebraic simplicity by pairing with the positive left vector. No gap; `T > 0` holds because `φ > 0` (verified: all 216² entries positive) |
| CK-06 | axiom sentences verbatim | **CONFIRM** | all six sentences present in both `MINIMAL_AXIOMS_2026-06-29.md` and the note under NFKC + whitespace normalization |
| CK-06 | four fence sentences present; forbidden phrases absent | **CONFIRM** | 4/4 present; 0 forbidden hits |
| CK-06 | every other numeral | **CONFIRM** | 37 checks, 28 mutations, orbit counts 3/8, `Q` 8×8 integer, `1296` width-4 row states, `210/216`, class counts `1296/216/36` — all reproduce |
| CK-06 | `claim_scope` neither wider nor narrower | **CONFIRM with one wording flag** | the two-sided-in-rows infinite strip `S_W` **is** defined (line 124: rows indexed by `N`, finite width) and its formation law **is** constructed (E3: projective limit of the consistent finite-strip laws, existing on `M^{S_W}` by the C2 cylinder-algebra argument), with row marginals `p_0` "without any limit". So the scope sentence is backed. See F-6 for the "half-plane" wording |
| CK-07 | runner runs; TOTAL line | **CONFIRM** | `TOTAL: PASS=37 FAIL=0`, exit 0, 27.2 s wall |
| CK-07 | `--list-mutations` | **CONFIRM** | 28 names, families B(3) C(3) D(8) E(9) F(5) |
| CK-07 | mutations (I ran **all 28**, not 8) | **CONFIRM** | 28/28 exit 1 with `mutation_family_observed == mutation_family_expected`; table in §4 |
| CK-07 | float self-scan | **CONFIRM** | runner F3 reports 0 hits on 953 lines; I confirmed no float literal, no `float(`, no `evalf(` outside the two marker lines |
| CK-07 | `AUDIT_TIMEOUT_SEC`, `AUDIT_INPUT_PATHS` literal | **CONFIRM** | `AUDIT_TIMEOUT_SEC = 900` (int literal, module level); `AUDIT_INPUT_PATHS` a literal 3-tuple of the three declared paths |
| CK-07 | cache sha + fingerprint + stdout | **CONFIRM** | `shasum -a 256` of the runner = `1cd8762aba6c5582332c6455ca4a70ba84946690849c871abe5b0bec3374817a` = the cache header; `scripts/cached_runner_output.py --check-only` reports `fresh` (so the declared-input fingerprint also reproduces); cache stdout is **byte-identical** to my live stdout |
| CK-08 | hidden-wall / overclaim scan | **CONFIRM with F-1, F-2, F-5, F-6** | no sentence asserts anything about the plane's static law, `Z^3` uniqueness, other orders beyond route 1, or a physical order. Positivity and transitivity are both used and both named (`W_pos`, and transitivity in "Menu, rotations, weights" / "The one-edge kernel"). No reading is treated as natural |

---

## 3. Findings

### F-1 (fix first, severity: moderate) — note line 479, N1 route 1: false for non-monotone row orders

The note writes: "row sweeps with any per-row direction and **any row order** are
covered by Theorem E (each row is still a path swept from an end with one
recorded neighbor below; `p_0` is reversal-invariant since `K` is symmetric)".

Counter-computation (mine, exact, `W = 3`, `n = 3`, triple `(3,1,2)`, row order
`0, 2, 1`, records-only reading, each row left to right):

- Row 2 forms while row 1 is unrecorded, so each site `(2,j)` has **no** recorded
  neighbour below — the parenthetical's premise fails immediately.
- Row 1 then forms with **three** recorded neighbours per site `(1,j)`:
  `(1,j−1)`, `(0,j)` and `(2,j)` — exactly the case the note's own Remark and D8
  witness say E does not cover.
- Result: the row-1 marginal deviates from `p_0` on **216 of 216** row states.
  Example: `ρ = (P(+e_x), P(+e_x), P(+e_x))` gets
  `5922478547/568465840800` where `p_0(ρ) = 1/96 = 5921519175/568465840800`
  (difference `959372/568465840800`). Total mass 1, so this is not a
  normalization artefact.

Correct statement: "row sweeps with any per-row direction and any **monotone**
row order (rows in increasing or decreasing index order) are covered by Theorem
E". Rows 0 and 2 in a non-monotone order are independent `p_0` chains and the
squeezed row is not `p_0`.

This is a false sentence inside the No-Go gate, and it over-closes route 1.
It does not touch `claim_scope`, any theorem statement, or the runner.

### F-2 (recommended, severity: low) — note line 479, same row: the diagonal sweep is misdescribed, and it in fact survives

The same row says uncovered orders are "diagonal or random sweeps in which some
site forms with two recorded neighbors **that have no common earlier neighbor**".
On a 2-D grid, a diagonal sweep's two recorded neighbours `(i−1,j)` and
`(i,j−1)` always **do** have a common earlier neighbour, `(i−1,j−1)`, so the
clause does not describe the diagonal sweep at all.

Positive extension I executed: the diagonal sweep (sites ordered by `i+j`, then
by `j`) at `W = 3`, `n = 3`, `(3,1,2)` gives **0/216** deviations from `p_0` on
every one of the three rows, and pair-parallel probability exactly `1/4` on both
the horizontal pair `(1,1)-(1,2)` and the vertical pair `(1,1)-(2,1)`. The
disposition "not executed" is safe; the reason given is wrong. Either drop the
clause or replace it with "sweeps in which some site forms with three or more
recorded neighbours".

### F-3 (fix first, severity: low-moderate) — note line 234: Carathéodory quoted, not proved, not declared

C2 says: "…and `m` is countably additive on the algebra; the **Carathéodory
extension** gives a probability measure `μ` on the product σ-algebra." The
Carathéodory extension theorem appears nowhere in the "Prior art and what is
new" list of classical facts re-proved at scope (lines 152–161: Perron–Frobenius,
and compactness of a countable product of finite sets plus the passage of
finite-window conditional identities to a limit) and nowhere in "Imports"
(lines 617–627). It is a general theorem quoted instead of proved, against the
note's own stated discipline ("Classical facts used here are re-proved at the
scope where they are used and never imported as authority"). Either add it to
Imports as a reference re-proved-or-cited at scope, or state that only finite
additivity on the cylinder algebra plus compactness is used and that the
extension is a named classical step.

### F-4 (recommended, severity: low) — note line 230: sequential compactness ⇒ compactness needs metrizability

C2 argues "Each cylinder set is compact-open in the product topology of the
finite menu — the compactness of `M^{Z^3}` is the same diagonal argument applied
to a sequence of configurations". The diagonal argument delivers *sequential*
compactness. The step used next (a countable disjoint union of cylinders that
equals a cylinder is finite) needs *compactness*. The two coincide here because
a countable product of finite discrete spaces is metrizable/second countable —
true, but unstated. Add the half-sentence.

### F-5 (recommended, severity: low) — note line 180 vs line 227: "no choice principle" stronger in the table than in the body

The obligation table (line 180) disposes of C2 as "proved here (C2), **no choice
principle**", while the C2 body (line 227) is correctly hedged: "no choice
principle is used beyond countable selection along an explicit rule". Make the
table row match the body.

### F-6 (recommended, severity: low) — line 4 `claim_scope` vs line 124: "half-plane" means the quadrant

Line 124 declares "the half-plane is the quadrant with rows and columns both
indexed by `N`". `claim_scope` (line 4) then says "strips of every width and
length including the infinite strip and **the half-plane**" without the
redefinition, and the Result-up-front paragraph (line 43) does the same. On the
standard half-plane (rows indexed by `N`, columns by `Z`) a row is a two-sided
infinite path with no left end, so "each row from its left end" and E3's
"swept from an end with at most one recorded neighbour" are undefined and the
proof as written does not apply. A reader taking the ordinary meaning reads more
than is proved. Recommend writing "the quadrant" in `claim_scope` and line 43,
or repeating the declaration there.

### F-7 (informational, no action required) — the `FORBIDDEN` list does not cover the phrase the note actually uses

`FORBIDDEN` (runner line 866) contains `"washes out"`, but the note's headline
and F5 both use `"wash out"` ("does not wash out"), which the gate never tests.
The note's usage is legitimate at strip scope, so this is not a note defect —
but the F2 gate is weaker than it reads for that entry.

### Non-findings worth recording

- The two-sided-in-rows **infinite strip's formation law is defined** in the note
  (E3: the projective limit of the consistent finite-strip laws, existing on the
  countable product by C2's cylinder-algebra argument, with row marginals `p_0`
  "without any limit"), so the spec's flagged risk on `claim_scope` does not fire.
- Positivity and transitivity are both used and both declared. I broke each
  independently and E3 fails as it should: a non-transitive 8-point menu
  (`Z_1 = (18,…,18,22,22)`) gives `p_0 P ≠ p_0` on 64/64 and 512/512 row states.
- The column sweep and the boustrophedon sweep both preserve `p_0` at `W = 3`
  (0/216 deviations each); the note does not claim them, so nothing is overstated.

---

## 4. Mutation runs (all 28 executed, not the 8 required)

Every mutation exited 1 and failed in exactly its declared family; no mutation
leaked into another family (`mutation_family_observed` is a single letter equal
to `mutation_family_expected` in all 28 runs).

| family | mutations (failing-check count) |
|---|---|
| B (3) | `kernel_not_doubly_stochastic` (3), `z2_identity_wrong_power` (1), `path_law_not_formation` (1) |
| C (3) | `spec_conditional_ignores_exterior` (6), `spec_conditional_two_hop` (6), `spec_face_wrong_subwindow` (1) |
| D (8) | `row_kernel_formula_wrong_denominator` (1), `row_kernel_drops_left_neighbor` (4), `invariance_forced_true` (1), `pair_law_wrong_column` (1), `direct_strip_law_mismatch` (1), `asymmetric_control_passes` (1), `constant_rule_not_uniform` (1), `three_neighbor_witness_forced` (1) |
| E (9) | `orbit_count_wrong` (1), `quotient_not_commuting` (1), `charpoly_coefficient_off` (1), `perron_interval_wrong_root` (3), `eigvec_residual_nonzero` (2), `limit_law_uses_rho_not_squared` (1), `s_inf_enclosure_contains_formation_value` (3), `finite_n_sequence_shuffled` (1), `second_eigenvalue_bound_too_small` (1) |
| F (5) | `claim_order_selected` (1), `claim_plane_static` (1), `claim_z3_uniqueness` (1), `claim_washout` (1), `claim_gate_fired` (1) |

Baseline: `TOTAL: PASS=37 FAIL=0`, exit 0, 27.2 s. Cache stdout byte-identical
to the live stdout; `cached_runner_output.py --check-only` reports `fresh`.

---

## 5. My scripts, and my own failures

Scripts (all under
`/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/checker02/`):

- `chk_core.py` — symbolic `φ`, `Z_1`, `K`, `Z_2 = Z_1²K²`, `K` spectrum (CK-01)
- `chk_sweep.py` — row kernel from the definition vs the closed formula; `p_0 P = p_0` at `W = 2, 3, 4` (CK-04)
- `chk_attack.py` — row-sweep control, snake, non-monotone row order `0,2,1`, column sweep, diagonal at `n = 2` (CK-04 ATTACK)
- `chk_attack2.py` — diagonal sweep by diagonal enumeration at `W=3,n=3`; non-transitive 8-point menu (CK-04 ATTACK)
- `chk_static.py`, `s1.py` — rotation group, orbits, `T`, `G`-invariance, `Q`, characteristic polynomials (CK-05)
- `s3.py` / `s4.py` — Perron root by own Sturm bisection, Perron vector by elimination over `Q(λ)`, `s_∞` by exact rational interval evaluation, second-eigenvalue bound by own root isolation (CK-05)
- `s5.py` — specification consistency on the cube, the plaquette, and the undeclared opposite-corner sub-window (CK-02)
- `s6.py` — diagonal/vertical/horizontal pair laws, direct finite-strip law, finite-`n` centre rows, the claimed `s_∞` minimal polynomial (CK-04, CK-05)
- `s7.py` — exact 10-digit truncations of all twelve finite-`n` values (CK-05/CK-06)
- `s8.py` — cube three-neighbour witness `210/216`; degree of `s_∞` by conjugate-interval separation (CK-04, CK-05)
- `s9.py` — left Perron vector `ℓ = A ρ₁` derived and verified (CK-05)
- `mut/` — the 28 per-mutation stdouts; `run_base.txt`, `cache_stdout.txt`, `live_stdout.txt`

My own failures and limitations, stated plainly:

1. My first attempt to background the runner used a trailing `&` inside the shell
   call; the process was reaped when the call returned and `run_base.txt` came
   back **empty**. I re-ran it properly. No conclusion was drawn from the empty file.
2. Two crashes on `AttributeError: 'Mul' object has no attribute 'eval_rational'`:
   `sympy.real_roots` returns radical `Mul` expressions for solvable factors, not
   `CRootOf`. I discarded that route entirely and wrote my own exact bisection
   isolation on top of `count_roots`, which is what the reported numbers use.
3. An early version (`s1.py`) computed a 36×36 symbolic determinant it did not
   need and ran 10 m 51 s. Its outputs (orbit counts, `G`-invariance, both `W=3`
   characteristic polynomials, and `charpoly(Q) | charpoly(T)` at `W=2`) are
   used; the waste was mine.
4. **Not exhaustively checked at `W = 4`:** the definition-vs-formula agreement of
   the row kernel (1296² entries × 4 site factors was out of budget). My `W = 4`
   invariance result `0/1296` uses the *formula* kernel; definition-vs-formula was
   verified exhaustively only at `W = 2, 3`. The runner's D5 also uses `W = 4`;
   I did not independently reproduce it from the definition.
5. I did **not** recompute the 120-digit coefficients of the `(5,2,4)` minimal
   polynomial of `s_∞`. I verified its **degree is 8** (by pairwise-disjoint exact
   conjugate intervals) and the enclosure; the coefficient list printed under
   `--exact` is unchecked by me.
6. `G`-invariance of `T` at `W = 3` was checked on the 8 orbit representatives
   against all 216 rows and all 48 maps (82944 checks) — the same declared sample
   the note uses, not the full 216 × 216 × 48. Exhaustive only at `W = 2`.
7. I did not re-derive block 01's Theorem A or Theorem B beyond the path instance
   used here, and I did not re-execute block 01's route-6 (marginal reading)
   evidence. Both are cited by the note as upstream, unaudited.
8. I did not attempt a random sweep order; the attacks were the four named orders
   plus the non-monotone row order.
