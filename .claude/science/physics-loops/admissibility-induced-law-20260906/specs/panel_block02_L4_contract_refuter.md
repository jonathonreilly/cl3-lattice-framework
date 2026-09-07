# L4 — hostile refuter on the block-02 contract (Theorems C, E, F)

Scope: `GOAL_block02.md`, the block-01 note (Premises, Theorem A, Theorem B) and
`docs/MINIMAL_AXIOMS_2026-06-29.md`, all read in full. Every number below is my own
exact computation (Fractions / sympy over `Q` and over `Q(λ1)`), from the raw rule
definition, not from the contract's formulas. Scripts:
`panel2/s1_rowsweep.py`, `s2_orders.py`, `s4b_theoremF.py`, `s5_ve_orders.py`,
`s6_final.py`, `s7` inline. Read-only on the worktree; no git state touched.

## VERDICT

**Build with changes.** Theorems E and F are true as mathematics at the executed
scope and every declared control number reproduces exactly. The defects are in
what the sentences quantify over, not in the arithmetic: two of them (D1, D3) make
stated claims false as written, and one (D8) makes a value-gate justification
false. All are cheap to fix before the build; none forces the block to be dropped.

## CONFIRMED (my own exact numbers)

C1. `Φ` symmetric, row sums all `p+q+4r` (symbolic); `Φ` eigenvalues
`p+q+4r` (×1), `p+q−2r` (×2), `p−q` (×3). Hence `K` symmetric **and** doubly
stochastic. E1 (`Z_2 = Z_1^2 K^2`) holds — but it is one line from those two
properties, not a discovery (see D8).

C2. `p_0 P = p_0` **exactly**, `max|dev| = 0`, with `P` rebuilt from the rule
(`φ`, `Z_2`) rather than from the E2 formula: at `W = 2` and `W = 3`, for
`(3,1,2)`, `(5,2,4)` and my third triple `(7,3,5)`. Also `p_0 P^2 = p_0`.

C3. Every horizontal and every vertical nearest-neighbor pair law equals `(1/6)K`
exactly at `W = 2, 3` for all three triples; pair-parallel `1/4`, `5/23`, `7/30`
= `p/(p+q+4r)`. E4's joint formula for `(α_0,…,α_{j−1}, β_j)` verified at
`j = 1, 2`, `W = 3`.

C4. Controls break E3 as the contract predicts. Asymmetric `φ` (`φ[0][2] = 5`):
`max|p_0P − p_0| = 5971/411840` (`W=2`), `1500013/256988160` (`W=3`).
Non-transitive menu with non-constant `Z_1` (3 values, `Z_1 = (6,5,6)`):
`79/3600` (`W=2`), `58013/3168000` (`W=3`). In both the vertical pair in column 0
still carries `(1/6)K` and every later column does not.

C5. Theorem F at `W = 3`: **8 orbits**, sizes `[6,12,48,6,48,24,24,48]` (sum 216);
`Q` well defined on every orbit (checked against every representative);
`diag(A)·T` is symmetric as an integer matrix — this is the exact reason the left
Perron vector is `A·ρ_1`, and it needs no limit argument; `T` strictly positive.
charpoly(Q) at `(3,1,2)` = `λ^5 (λ^3 − 7312 λ^2 + 2578432 λ − 221134848)`, the
cubic irreducible — the contract's expectation reproduces exactly. Perron root
label `6945.3378242571`; other roots `225.41393106938`, `141.24824467351`.

C6. `s_∞` at `(3,1,2)`, `W=3`, exact in `Q(λ1)`:
`s_∞ = −88739138613 λ^2/169443028709515264 + 39489459544779 λ/10590189294344704 − 125610297286389/330943415448272`,
minimal polynomial
`2647547323586176 t^3 − 2190008305118016 t^2 + 544429860087294 t − 40261879885473`,
label `0.25611098728577869086` (matches the contract's control to all printed
digits). `s_∞ > 1/4` **exactly**: `s_∞ − 1/4` as a rational-coefficient quadratic
in `λ` is positive at both endpoints of a rational isolating interval of width
`5.6e−15` (its stationary point, `λ ≈ 3559.7`, lies far outside that interval, so
the endpoint signs decide); the two endpoint values are
`298452234159286609725224223115197231668597507 / 48838627901228876714621894096060416000000000000`
and
`74613058539821410511137042376315236832319443 / 12209656975307219178655473524015104000000000000`.
So the enclosure excludes `p/(p+q+4r)` — I reproduce that independently.
Note the simpler exact route: `s_∞` reduces to a **polynomial** in `λ1`, so the
sign test is an interval evaluation; no resultant is needed at `W=3`, `(3,1,2)`.

C7. Finite-`n` center-row pair-parallel, exact, `(3,1,2)`, `W=3`:
`n=3: 578647/2260844`; `n=5: 20456844081/79876422590`;
`n=7: 770944922609499/3010200239734244`;
`n=9: 60528391297616165323/236336570250352523934`
(labels `.255942913`, `.256106163`, `.256110844`, `.256110983`), increasing to
`s_∞` from below; `1/4` is below every one of them. At `(5,2,4)`, `W=3`:
charpoly(Q) irreducible of degree 8 with **all eight roots real**, dominant
`179107.42880283`; `s_∞` label `0.21991516168701978151`, and exactly
`s_∞ > 5/23` and `s_∞ < 1/4` (signs certified on the isolating interval);
`n=3,5,7` values `3731173618465/16969587349457`,
`119716037792791450503185/544375382349486764567177`,
`768087720257216734305488815630597/3492654863932433332945094107153565`.
At `W=2`, `(3,1,2)`: charpoly(Q) `= λ(λ^2 − 296λ + 2112)`,
`s_∞ = 31035/54428 − 237λ/217712`, min poly `217712 t^2 − 178128 t + 31329`,
label `0.25594308890161877`, again `> 1/4`.

C8. The center-row formula `∝ (A·T^c)(ρ)(T^{n−1−c}1)(ρ)` is right: it agrees with
the brute-force static law (explicit product weight over all `6^{Wn}` configurations)
at `(W,n) = (2,3), (2,4), (3,3)`.

C9. Width consistency (ancestral closure): the width-3 two-row formation joint
restricted to columns `{0,1}` equals the width-2 two-row joint, exactly. This is
the lemma the infinite-width claim needs and it is true — but it is not in the
contract (D2).

## DEFECTS

**D1 — E3/F5 name an object that does not exist. Severity: high (statement).**
Claim: "every row of the formation law has exactly the law `p_0` … on the infinite
strip and half-plane", with `S_W` declared as "rows indexed by `Z` or `N`".
With rows indexed by `Z` the row sweep is **not a well-order** — no site is first,
every site has infinitely many predecessors — so `μ_σ = Π_k r(v_{x_k} | v_{A_k})`
is undefined; there is no finite product and no first row carrying `p_0`. Only the
half-plane (rows indexed by `N`) supports the definition. Meanwhile Theorem F's
object *is* two-sided: `w` is the `n → ∞` limit of the **center** row. So F5, the
block's headline, compares a formation law on a half-plane with a static law on a
two-sided strip. Missing lemma / fix: define the formation object on `N`-indexed
rows only, and compare with the static half-plane's row-`i` marginal as `i → ∞`
(same limit `w`, by the same Perron argument), or prove the strip's Gibbs measure
is unique so the two carriers agree. Either fix is a paragraph; without it F5 is
a comparison of two laws on two different graphs.

**D2 — the width limit is hidden inside "the induction over rows needs no limit".
Severity: medium.** E3's telescoping is a finite induction that *terminates* at the
right end: `Σ_{β_{W−1}} K(α_{W−1} → β_{W−1}) = 1`. For infinite width (the
half-plane read as `W = ∞`) that last step does not exist and the proof as written
does not close. The repair is the restriction lemma (each site's parents lie in
`{j' ≤ j}`, so the formation law of width `W` restricted to the first `W'` columns
is the width-`W'` formation law) plus Kolmogorov extension. I verified the
restriction lemma exactly (C9); the contract does not state it.

**D3 — F3's convergence rate is wrong under the natural reading. Severity:
medium.** F3 says "the convergence is geometric with ratio `|λ_2/λ_1|`", one line
after F2 introduces Perron–Frobenius **for `T`**. `T`'s subdominant eigenvalue is
not the rate. Exact counterexample, `W=2`, `(3,1,2)`: the full `36×36` transfer
matrix has
`charpoly(T) = λ^{20}(λ−56)^3(λ−40)^3(λ−8)^8(λ^2 − 296λ + 2112)`,
so `T`'s spectrum is `{288.684, 56, 40, 8, 7.316, 0}` and `|λ_2(T)/λ_1| = 56/288.684
= 0.19399`. The observed per-two-row convergence of the exact `s_n` sequence is
`0.025342 = 7.3160/288.684`, i.e. the ratio **inside the `G`-invariant block**
(`Q`'s spectrum) — the eigenvalues 56, 40, 8 never appear, because `A` and `1` are
both `G`-invariant. The supervisor control's `0.0325` and `0.0189` are likewise
`λ_2(Q)/λ_1`, not `λ_2(T)/λ_1`. Fix: state the rate as `|λ_2(Q)/λ_1|` and give the
one-line reason (the two vectors driving the center-row law lie in the invariant
subspace); F4's rational bound must then be advertised as a bound on the invariant
block only. The `W=2` factorization above is a ready-made executed witness.

**D4 — "The normalizer history does not wash out" is unscoped, and violates the
block's own Forbidden list. Severity: medium (overclaim).** It appears bare in
"Why this block" and as the last clause of F5. What is proved: on `S_2` and `S_3`,
under `σ_row`, at two triples, one statistic of one static-law object differs from
`p/(p+q+4r)`. That does not exclude that some other exhausting sequence of windows
or some other order has a limit agreeing with a static law — which is exactly the
N7 obligation being answered. The Forbidden section itself bans
"'the normalizer history washes out' or its negation beyond the strip's scope".
Fix: scope every occurrence to `S_W`, `W ∈ {2,3}`, `σ_row`, the declared triples.

**D5 — "the static law of the same strip" / "the static law's center-row law is
`w`". Severity: medium (definite article without uniqueness).** F4 computes the
`n → ∞` limit of finite open-boundary strip static laws. Uniqueness on the infinite
strip is not claimed anywhere, and the Forbidden list bans "the law" outside its
exact finite meaning. Cheap repair, and it should be a numbered item: for **any**
positive boundary vectors (including any exterior records at the two ends of the
strip) `b_L T^c` and `T^{n−1−c} b_R` converge in direction to the Perron vectors,
so the center-row limit is `w` regardless of boundary condition — that is what
licenses "the". One PF line; without it the claim is a limit of one boundary family.

**D6 — C2's compactness and translation-invariance sentences are inaccurate.
Severity: medium-low.** (i) "compact (a diagonal argument on a finite menu — no
choice principle)": the countable diagonal extraction uses dependent choice; what
is avoided is full AC / Tychonoff for arbitrary index sets. Say that, or drop the
parenthetical. (ii) "Averaging over translations of a finite box of shifts and
taking a further subsequence gives a translation-invariant limit" is false as
written — an average over one fixed finite box is not translation invariant. The
argument needs a Følner/van Hove sequence of boxes `B_n` with
`|∂B_n|/|B_n| → 0`, the Cesàro averages of translates, and a weak subsequential
limit; plus the two facts that make it work (each translate of a DLR measure is DLR
because the specification is translation-covariant, and the DLR set is convex and
closed under the limit).

**D7 — C2's "the conditional kernels are local, so they pass to the limit" is a
sketch. Severity: low.** What is needed and should be written: for a local `f`,
`γ_Δ f` is again a function of finitely many coordinates (`Δ ∪ ∂Δ`, range one,
finite menu), so cylinder-wise convergence commutes with `γ_Δ`; and
`Λ_n ⊇ Δ ∪ ∂Δ` eventually, which is where the exhausting sequence is used.
C1 itself I confirm is exactly cancellation: conditioning `μ_Λ^ω` on `v_{Λ∖Δ}`
kills every factor not touching `Δ`, and the survivors are precisely the `Δ`-window
weight with exterior records `(v_{Λ∖Δ} ∪ ω)|_{∂Δ}` — the same computation as
Theorem A, no positivity of the conditioning event needed beyond `W_pos`.

**D8 — V3's justification "Theorem E's solvability needs the menu's transitivity"
is false. Severity: medium (value gate rests on it).** Counterexample computed:
the symmetric positive 4-value menu
`Φ = [[1,2,3,4],[2,4,3,1],[3,3,2,2],[4,1,2,3]]` has constant row sums `10` and
diagonal `(1,4,2,3)` — the diagonal values are an isomorphism invariant, so no
automorphism group can be transitive on it — and yet `p_0 P = p_0` holds **exactly**
(`max|dev| = 0`) at `W = 2` and `W = 3`, with every vertical pair equal to
`(1/|M|)K`. What E3 actually needs is: `φ` symmetric **and** `Z_1(t)` independent
of `t`, i.e. `K` symmetric doubly stochastic. Transitivity is one sufficient route
to the second on the rotation menu. Restate the hypothesis as those two properties
(and keep the transitivity remark as the derivation on this menu). Corollary: E1 is
then a two-line identity, which weakens the V3 sentence "the product rule's
`Z_2 = Z_1^2 K^2` identity, which the audit lane does not have".

**D9 — prior art: this is a Pickard / unilateral (Markov-mesh) field construction.
Severity: medium for the value gate, none for correctness.** `Z_2 = Z_1^2K^2` with
`K` symmetric doubly stochastic is exactly the classical condition under which a
two-parent unilateral construction makes every row and every column a `K`-chain
(Pickard random fields; Abend–Harley–Kanal Markov meshes). `LITERATURE_BRIDGES.md`
lists only Brook (1964). Under the repo's external-sources policy the reference
must be named and the result re-proved in-framework (which the block does anyway).
V5's "not a variant of anything landed" is about the repo and survives; V3's
novelty framing does not, unless the reference is added.

**D10 — the strip's exterior is silently unrecorded on the static side. Severity:
low, but it is a smuggled reading.** The strips are declared as grids "of `Z^2`",
while the axioms' lattice is `Z^3`; Theorem C builds static laws **with** exterior
records `ω`, and Theorem F silently uses the open-boundary (no-exterior-record)
static law. As a window of `Z^3`, every strip site has four out-of-plane neighbors;
under R-only they contribute nothing to the formation law (so E is a genuine `Z^3`
statement), but any recorded out-of-plane exterior adds a site factor
`h(v_x) = Π_y φ(v_x, ω_y)` and changes `T`, hence changes `w` and `s_∞`. F5 must
say it is the strip with unrecorded exterior, on both sides of the comparison.

**D11 — E's "not claimed" list should also disclaim the order class. Severity:
low.** "Theorem E's exact solvability is a property of the two-recorded-neighbor
sweep on a two-dimensional window" is not accurate as a sufficient condition: the
path-3 order `(0, 2, 1)` (ends inward) has at most two recorded neighbors and
breaks the row law — `max|μ_σ − p_0| = 1/1248` at `(3,1,2)`, pair-parallel
`106/429` instead of `1/4` (block 01's own census, reproduced here). The property
is not "≤ 2 recorded neighbors" but "each site's recorded parents are one
in-row predecessor and the site above" (a monotone/staircase past).

## ORDER SURVEY

Exact, by variable elimination on full grids at `(3,1,2)` (and `(5,2,4)` where
noted); "rows = `p_0`" means every row marginal equals the width-`W` chain law,
"cols = `p_0`" the same for columns, "NN" means every nearest-neighbor pair law is
exactly `(1/6)K`.

| order | grid 3×3 | grid 4×3 | grid 3×4 | verdict |
|---|---|---|---|---|
| row sweep | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | invariant (E3) |
| column sweep | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | invariant (transpose of E3, and rows survive too) |
| diagonal sweep (by `i+j`) | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | invariant |
| antidiagonal sweep | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | rows ✓ cols ✓ NN ✓ | invariant |
| snake / boustrophedon | rows ✓, cols ✗ (cols 1,2) , NN ✓ | rows ✓, cols ✗ (all), NN ✓ | rows ✓, cols ✗ | **row law survives, column law does not** |
| scrambled order (max 3 recorded parents) | rows ✗ cols ✗ NN ✗ | rows ✗ cols ✗ NN ✗ | — | breaks everything |
| path-3 "ends inward" `(0,2,1)` (2 parents) | row law ✗, `max dev 1/1248` | — | — | breaks; refutes "two-recorded-neighbor ⇒ solvable" |

Also verified at `(5,2,4)` on 3×2 and 2×3 (same pattern), and: the snake's
row-law survival is not luck — `p_0` is reversal-invariant because `K` is
symmetric, so the right-to-left row kernel is the reflection of the left-to-right
one. The scrambled order produces three distinct NN pair-parallel values
(`6293/25740`, `106/429`, `39453497/157907178` on 3×3), i.e. the pair statistic is
not even column-independent.

Two consequences for the contract. (i) The row sweep is **not** distinguished:
the column, diagonal and antidiagonal sweeps give exactly the same row law, column
law and pair statistic on every grid I tested. The block should either scope E to
`σ_row` explicitly (and say the executed survey found other invariant orders), or
prove the monotone-order class. Claiming solvability as a property of "the
two-recorded-neighbor sweep" is refuted by the `(0,2,1)` witness. (ii) Under the
row sweep the **columns** are `p_0` as well (executed 3×3, 4×3, 3×4) — strictly
stronger than E4's vertical-pair statement, and the strongest form of the
separation in F5, since it says the formation law's chain statistic is `K` in both
directions while the static center row's is not.

## NEXT TEST

1. Re-run the `s_n` sequence at `W = 3` out to `n = 13` and fit the per-two-row
   ratio against `λ_2(Q)/λ_1 = 225.41393…/6945.33782…`; publish the exact Sturm
   bound on `λ_2(Q)` **and** the `W=2` full-`T` factorization
   `λ^{20}(λ−56)^3(λ−40)^3(λ−8)^8(λ^2−296λ+2112)` as the executed witness that the
   rate is the invariant block's, not `T`'s (D3).
2. Prove and execute the boundary-independence of `w` (any positive `b_L, b_R`,
   including exterior records at the strip ends) — this is what licenses "the
   static law" in F5 (D5), and it is three lines of Perron–Frobenius.
3. State and execute the restriction lemma in `W` (I have it exactly at
   `3 → 2`) and re-cast the infinite-strip statement on `N`-indexed rows only (D1, D2).
4. Add "rows and columns are both `K`-chains under `σ_row`" as a theorem (E5) with
   the width-4 execution, and cite Pickard/Markov-mesh as the external converging
   idea, re-proved (D9).
5. Replace V3's transitivity sentence with "symmetric `φ` and `t`-independent
   `Z_1`", carrying the non-transitive constant-row-sum witness
   `[[1,2,3,4],[2,4,3,1],[3,3,2,2],[4,1,2,3]]` as its boundary (D8).
