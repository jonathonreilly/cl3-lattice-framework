# L1 — MRF / Gibbs-specification rigor review of the proposed block

Lens: mathematical statistics + statistical mechanics (MRF, Gibbs specifications,
Hammersley–Clifford, Brook's lemma, Besag consistency, DLR).
Read: the complete `docs/MINIMAL_AXIOMS_2026-06-29.md`, the dossier, and the
archived R136 packet (`archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md`,
lines ~10450–10580).

All computations below were run in the scratchpad
(`scratchpad/panel/l1/l1_checks*.py`, sympy exact + `fractions.Fraction`); the
exact numbers are quoted where they matter.

---

## 1. VERDICT

**Build with changes.** T2 is the real content and it is correct: I verified the
formation-law identity, the constancy of the one-neighbour normaliser, the exact
`Z(b,c)` lemma, and the partition-function identity, all in exact arithmetic. The
distinction it states — a sequential formation law versus a static DLR/Gibbs law —
is a genuine and well-known gap in the R136 chain, and the repository has never
stated it. But T1 as written is *not* a correct theorem statement (four missing
hypotheses: the window boundary condition, the rule's domain on partial
neighbourhoods, symmetry/uniformity of `φ`, and the site-weight gauge), and T2(b)'s
general-window sentence has a real logical gap (non-constancy of one factor does
not give non-constancy of a product of factors) that I can close only when every
site forms with at most two recorded neighbours — which is *not* the generic case
on `Z^3`, degree 6. Fix those and the block is worth landing; land it as stated and
it ships an unproved general-window negative.

---

## 2. STRONGEST ARGUMENT FROM MY LENS

R136's step (ii) is the classical conflation of a **specification** with a
**process**. In DLR language: a rule `r` is a candidate *specification*
`γ = (γ_Λ)`; a static law is a measure in `G(γ)`; a formation law is a
non-stationary sequential (Markov-chain-like) construction that exists for any
`r` whatsoever, needs no consistency, and lands outside `G(γ)` unless the
normaliser history is degenerate. Everything in Hammersley–Clifford applies to the
first object. The Record axiom, read literally — records *form*, one at a time,
permanently, and "a site with no record cannot be read" — describes the second.
The framework supplies no reason to prefer the first. So the R136 conclusion "the
FORM of the admissibility rule is forced" is conditional on a reading, and the
block is right to make that conditionality a theorem rather than a comment.

The strongest *technical* support is that the correction is exact and small:

- **Formation identity** `μ_σ(v) = μ(v) · Z_W / Π_k Z_k(v_{A_k})` — I re-derived
  it. Each edge `{x_j,x_k}` (`j<k`) is picked up exactly once, at step `k`; that
  is the whole proof, and it is where symmetry of `φ` is load-bearing (§5, D2).
- **Two-neighbour normaliser, six-state menu**, `ψ` constant, `φ ∈ {p,q,r}`
  (parallel / antiparallel / orthogonal), `Z(b,c) = Σ_s φ(s,b)φ(s,c)`:

  | `⟨b,c⟩` | `Z(b,c)` |
  |---|---|
  | `+1` | `p² + q² + 4r²` |
  | `−1` | `2pq + 4r²` |
  | `0`  | `2r(p+q+r)` |

  Differences (sympy `factor`):
  `Z(+1) − Z(−1) = (p−q)²`,
  `Z(+1) − Z(0) = (p−r)² + (q−r)²`,
  `Z(−1) − Z(0) = 2(p−r)(q−r)`.
  Two of the three are **sums of squares**, so `Z` constant ⟺ `p=q=r` over the
  **reals** — positivity is not even needed for this lemma, and the R136
  "rank(FᵀF)=1 ⇒ p=q=r" route is unnecessary. `sp.solve` confirms the only
  solution is `{p:r, q:r}`. This is the cleanest native proof and it should
  replace the rank argument.
- **One-neighbour normaliser** `Z₁(b) = Σ_s φ(s,b) = p + q + 4r`, verified
  constant over all six `b` (one line in general: transitivity of the proper
  cubic group on `{±e_a}` plus invariance of `φ` ⟹ `Z₁(Rb)=Z₁(b)`).
- **Exact Brook certificate for the sum rule** (this is the block's best object
  and it replaces R136's floating-point nullspace table). 3-path `1−2−3`, sum
  rule `u(s|η) = 1 + λ Σ_{y∈η} ⟨s, η_y⟩`, pin `v₃ = e₁`, and walk the closed
  single-site loop
  `(e₁,e₁,e₁) → (e₂,e₁,e₁) → (e₂,e₂,e₁) → (e₁,e₂,e₁) → (e₁,e₁,e₁)`.
  Product of the four full-conditional ratios (sympy, exact in `λ`):

  > **`(1 + 2λ) / (1 + λ)²`,  so the Brook defect is `1 − Π = λ²/(1+λ)² ≠ 0` for `λ ≠ 0`.**

  Brook's lemma forces this product to be 1 for any joint law; hence **no static
  law exists at any `λ ≠ 0`** (positivity holds for `|λ| < 1/2` on degree 2,
  `|λ| < 1/d` in general). This is exact, rational, half a line, and it
  reproduces R136's measured `O(λ²)` scaling as an identity rather than a fit.
  A brute-force search over all `(a,a',b,b',c)` found other certificates too,
  e.g. `−(λ−1)²(2λ+1)/((λ+1)²(2λ−1))` with defect `4λ³/((λ+1)²(2λ−1))`.
  **Note also**: on a single *edge* the sum rule *is* a product rule and a static
  law exists; the obstruction needs a site of degree ≥ 2. That is exactly why the
  linear analysis missed it, and it is worth one sentence in the note.
- **Partition-function identity (T2d)** verified exactly on the 4-cycle,
  `(p,q,r) = (5,2,3)`: `E_{μ_σ}[Π_k Z_k] = 130566 = Z_W` for orders `(0,1,2,3)`
  and `(0,2,1,3)`. The dual form `E_μ[(Π_k Z_k)^{-1}] = Z_W^{-1}` follows from
  `Σ_v μ_σ = 1` and is the more useful one; it is the Jarzynski /
  annealed-importance identity, and re-proving it natively in one line is fine
  under the reference-not-borrow policy.
- **Order dependence (T2c)**, 4-cycle, `(p,q,r) = (5,2,3)`, exact rationals:
  `TV(μ_σ, μ) = 110760/7855721 ≈ 0.014099` for `σ = (0,1,2,3)` and `(0,1,3,2)`;
  `= 3589/130566 ≈ 0.027488` for `σ = (0,2,1,3)`;
  `TV(μ_{(0,1,2,3)}, μ_{(0,2,1,3)}) = 29/2166 ≈ 0.013389`.

There is also a sharper physical statement the block is not making and should:
`log Z_k(v_{A_k})` with `|A_k| = 2` is a function of two sites at graph distance 2
(the plaquette diagonal), and it is **not** additively decomposable (that is
exactly the `Z(b,c)` lemma). So **the formation law is not a nearest-neighbour
Markov field at all — the normaliser history generates a genuine range-2
interaction absent from the static action.** That is a second, independent proof
that `μ_σ ≠ μ` and it is much more informative than "the two measures differ".

---

## 3. STEELMAN AGAINST MY VERDICT

Three real ones.

1. **The block proves a negative that may be uninteresting.** Even granting
   `μ_σ ≠ μ`, the axioms supply no formation order, so `μ_σ` is not a single
   object either — it is a family indexed by an unsupplied `σ`. A theorem saying
   "the unsupplied object differs from the supplied one" arguably just restates
   that the order is unsupplied. The owner's actual question ("what action does
   the rule induce") is answered by T1, and T1 is the part with defects.
2. **The static reading may be forced anyway, by permanence.** Records are
   permanent and one-per-site, so the *final* configuration of a fully-recorded
   window is a definite random field, and if one additionally requires the family
   `{μ_σ}` to be order-independent (a plausible "no site privileged / no order
   privileged" reading of the Lattice axiom's homogeneity), then T2's own
   machinery says the rule must satisfy `Π_k Z_k = const`, hence `p=q=r`, hence
   *no rule at all* satisfies both order-independence and the variation clause.
   That is a much stronger and more interesting statement than T2 as written, and
   the block should chase it rather than the weaker `μ_σ ≠ μ`.
3. **T1's defects are all repairable in an afternoon.** If so, "build with
   changes" collapses into "build".

---

## 4. WHAT EVIDENCE WOULD CHANGE MY MIND

- A proof (or exact finite counterexample) for the **no-cancellation lemma** at
  `|A_k| ≥ 3` (§5, D7). If cancellation *is* possible, T2(b)'s general statement
  is false as written and the block must be re-scoped to windows/orders with
  `max_k |A_k| ≤ 2`.
- An exact demonstration that some **absence-dependent extension** `φ_abs` makes
  two orders coincide on the plaquette. The dossier lists this as an attempted
  route; it is the one route with a free function in it, and if it succeeds the
  headline "for every order" is wrong.
- A statement of the **boundary condition** under which T1 is claimed. If the
  intended window is a torus (periodic) the covariance and gauge issues largely
  evaporate; if it is free-boundary, T1 needs T2's records-only premise as well
  and the two theorems are not independent.
- Anything showing the framework *does* supply a formation order (it does not, on
  my reading of the Record axiom and the "Open Gates" list, which explicitly
  parks "at which site, and at what rate").

---

## 5. CONCRETE DEFECTS

**D1 — T1's "static law on a finite window W" is not well-defined.** For a
boundary site `x ∈ W`, `N(x) ⊄ W`, so "μ(v_x = s | v_{W\x}) = r(s | v_{N(x)})"
has no meaning until you fix one of: (i) free boundary (`N(x) ∩ W`, which
requires the rule to be defined on *partial* neighbourhoods), (ii) a frozen
boundary condition on `∂W`, (iii) periodic (torus). These give **different**
static laws and different `S_W`. Under (i), T1 already needs the very
"records-only extension" premise that T2 names — so the two theorems share a
premise the dossier attributes only to T2. All four declared model graphs
(3-path, 4-star, 4-cycle, open 2×2×2 cube) are non-regular or non-`Z³`, so this
is not academic. **Fix:** name the boundary convention in the theorem statement.

**D2 — "product form with a symmetric pair weight" is not what the ⇒ direction
delivers.** Hammersley–Clifford on a triangle-free graph gives
`μ = Z⁻¹ Π_x ψ_x(v_x) Π_{xy∈E} φ_{xy}(v_x,v_y)` with **site-indexed** `ψ_x`,
**edge-indexed** `φ_{xy}`, and `φ_{xy}` an ordered-pair function — nothing yet
forces one `φ` on every edge, and nothing forces `φ(a,b) = φ(b,a)`. What supplies
each:
 - same `φ` on all edges of one direction ⟸ translation covariance;
 - direction-independence ⟸ proper cubic rotations;
 - **symmetry** ⟸ the edge-flip element. This must be exhibited: with
   `R` the proper (det = +1) 180° rotation about `e₂` and `t_{e₁}` the unit
   translation, `g = t_{e₁} ∘ R` satisfies `g(0) = e₁` and
   `g(e₁) = e₁ + R e₁ = e₁ − e₁ = 0`, so `g` lies in the group generated by the
   axioms' translations and proper rotations *about sites* and swaps the endpoints
   of the edge `{0, e₁}`. Covariance then gives
   `φ(a,b) = φ(ρ(R)b, ρ(R)a)`, and with isotropy (`φ = f(⟨a,b⟩)`) symmetry
   follows. **This lemma is missing and is one line; state it.**
 - On the *abstract* model graphs (3-path, 4-star, 4-cycle) there is no lattice
   group at all, so uniformity and symmetry of `φ` there are **class-(P)
   hypotheses**, not consequences. The note must say so.
 - **Tie to T2:** symmetry of `φ` is exactly what makes the formation identity
   hold. The sequential product always orients each edge *later ← earlier*; the
   static product orients it once, arbitrarily. With `φ` asymmetric, `μ_σ` is
   `Π_edges φ(v_later, v_earlier) / Π Z_k`, which is not a reweighting of any
   single `μ`, and the identity `μ_σ = μ Z_W/Π Z_k` **fails**. Say this
   explicitly; it is the cleanest answer to "what ties symmetric `φ` to undirected
   edges".

**D3 — the site-weight gauge is unnamed, and the canonical fix violates an
axiom.** `μ` is invariant under `φ(a,b) → φ(a,b) g(a) g(b)`,
`ψ_x(s) → ψ_x(s) g(s)^{−deg(x)}`, and under global rescalings. So
`S_W = −Σ log ψ − Σ log φ` is a **gauge class, not a function**, and "the object
the rule induces statically" is ill-defined until fixed. The canonical
(Möbius/Besag) potential fixes it by choosing a reference possibility `0` — which
**privileges a possibility**, contrary to the Qubit axiom's "No possibility is
privileged". The covariant fix works and should be stated as a lemma: `g` must be
rotation-invariant on the menu, and the proper cubic group acts transitively on
`{±e_a}`, so `g ≡ const`; the gauge group collapses to two global scalars and
`S_W` is canonical **up to an additive constant**. Note this is a *consequence of
transitivity*, so it fails on a non-transitive menu — another hypothesis to name.

**D4 — "positive rule" is undefined, and positivity is the one hypothesis the
axioms decline to make.** The Admissibility reading note says availability is the
*support*: "on finite menus, exactly the possibilities of nonzero probability".
So the axioms explicitly contemplate zeros. Two consequences:
 - The block must declare positivity as an **added premise** and say that it is
   the added premise, not derive it.
 - For a non-positive rule T1's "iff" **cannot even be stated**: `r(·|η)` is
   arbitrary off the support of any candidate law, so neither existence nor
   uniqueness of "the static law of `r`" is well-posed. Positivity is not a
   convenience; it is what makes the theorem's subject exist.
 - The right definition is `r(s|η) > 0` for every `s ∈ M` and every **partial**
   assignment `η` (needed for both T1-on-a-window and T2). For a product rule this
   is equivalent to `ψ > 0` and `φ > 0` on the menu.
 - Small true lemma worth adding: a positive rule forces the static law to be
   positive (the support is closed under single-site changes, and the Hamming
   flip graph on `M^W` is connected), which is what licenses Brook.

**D5 — the positivity-necessity witness is correct but proves a weaker statement
than claimed.** I checked the classical 4-cycle example: sites `0-1-2-3-0`,
binary, uniform on the 8 configurations that are prefixes-of-1s or suffixes-of-1s
(`0000,1000,1100,1110,1111,0111,0011,0001`).
 - Local Markov property holds wherever the conditioning event has positive
   probability: **verified, no failures**.
 - Every one of the four edges realises **all four** pair values in the support:
   **verified**. So the dossier's finite argument is valid: any nonnegative
   factorisation would have all `ψ`, `φ` factors strictly positive, hence `μ > 0`
   everywhere, contradicting the **8 zeros**.
 - But: this object is a **law, not a rule** — its conditionals are undefined off
   the support — and it lives on a binary menu on an abstract 4-cycle, not on the
   covariant six-state menu on `Z³`. So it establishes "Markov ⇏ factorisation",
   which is what is needed, and **not** "a non-positive covariant rule on the
   six-state menu has a non-product static law", which is a separate and untested
   claim. Do not let the note blur those.

**D6 — T2(a)/(b) state the wrong graph condition.** The sharp statement is not
"tree swept from a root" / "contains a 4-cycle" but:

> There exists an order with `max_k |A_k| ≤ 1` **iff the window graph is a
> forest.**

Proof, two lines, cleaner than the dossier's: `Σ_k |A_k| = |E|` exactly (each edge
is counted once, at its later endpoint), and the first site of each component has
`|A_k| = 0`; so `max |A_k| ≤ 1` ⟹ `|E| ≤ n − c` ⟹ forest; conversely a BFS/DFS
sweep from a root in each component achieves it. The converse direction of (b) is
then "the window contains **any** cycle", and the proof is one line: the
latest-formed vertex of a cycle has both its cycle-neighbours already recorded.
The 4-cycle is a special case, not the hypothesis. Also, (a) needs `ψ` constant —
which needs transitivity + covariance (D3) — and needs `Z₀ = Σ_s ψ(s)` constant
too (trivially). Then `Π_k Z_k` is a constant, both `μ_σ` and `μ` are probability
measures, so the constant is `Z_W` and `μ_σ = μ`. Correct as far as it goes.

**D7 — the real gap: T2(b) infers non-constancy of a product from non-constancy of
one factor.** `μ_σ = μ` ⟺ `Π_k Z_k(v_{A_k})` is constant in `v`. Non-constancy of
`Z₂` does **not** immediately give non-constancy of the product; factors could
cancel. What I can prove and what I cannot:

 - **Closed, when `max_k |A_k| ≤ 2`.** By transitivity of the menu group and
   invariance of `Z_d`, the ANOVA main effects of `log Z_d` vanish, so
   `log Z₂(b,c) = const + g₂(b,c)` with `g₂` a pure 2-body term with zero
   marginals. In `Σ_k log Z_k`, the component on a site pair `{y,z}` is
   `m_{yz} · g₂` with `m_{yz} ∈ Z_{≥0}` the number of sites forming with both
   `y,z` recorded. Distinct pairs do not mix. Hence the sum is constant iff
   `g₂ ≡ 0` iff `Z₂` constant iff `p=q=r`. **This covers the 3-path, the 4-star
   and the 4-cycle** — i.e. every exhibit the dossier actually names — and it is
   the missing lemma for those. It should be written into the note.
 - **Open, when some site forms with `|A_k| ≥ 3`** — which is the *generic* case
   on `Z³` (degree 6) and already occurs on the declared open 2×2×2 cube. The
   condition becomes `Σ_d n_d(y,z) · g_d ≡ 0` for every pair, with `g_d` the
   2-body ANOVA component of `log Z_d` and `n_d ≥ 0` integers. Cancellation needs
   `g₂` and `g₃` (…, `g₆`) to point in opposite directions. I computed `g₂` and
   `g₃` exactly on the six-state menu (25-digit evaluation of exact symbolic
   expressions), in the basis `(⟨b,c⟩ = +1, −1, 0)`:

   | `(p,q,r)` | `g₂` | `g₃` | `g₃/g₂` componentwise | proportional? |
   |---|---|---|---|---|
   | `(5,2,3)` | `(0.078201, −0.070835, −0.0018416)` | `(0.076083, −0.069066, −0.0017544)` | `0.97292, 0.97503, 0.95265` | no (cross ≈ −1.2e−4) |
   | `(1,1,2)` | `(0.078522, 0.078522, −0.039261)` | `(0.077401, 0.077401, −0.038701)` | `0.98573` (all) | yes, ratio > 0 |
   | `(7/3,1,5/4)` | `(0.093444, −0.057430, −0.0090034)` | `(0.090450, −0.055643, −0.0087017)` | `0.96796, 0.96889, 0.96648` | no (cross ≈ −5.0e−5) |

   At every point tested `g₃` has the **same sign pattern** as `g₂` with ratio
   ≈ 0.95–0.99 > 0, so with nonnegative integer counts no cancellation is
   possible. That is a check at points, **not a theorem**. Missing lemma, stated
   sharply: *for positive `(p,q,r)` not all equal, the 2-body ANOVA components
   `g_d` of `log Z_d`, `d = 2..6`, all lie in one open half-space; equivalently
   `Σ_d n_d g_d = 0` with `n_d ≥ 0` forces every `g_d = 0`.*
 - Spot check on the declared cube: 8 vertices, 12 edges, 3-regular; order
   `(3,6,1,5,7,0,4,2)` with `|A_k|` profile `(0,0,1,1,3,1,3,3)`. The difference of
   `Π_k Z_k` between two configurations is the nonzero polynomial
   `108 r⁴ (p−q)² (p+q) (p+q+4r)³ (p²+2pq+2pr+q²+2qr+4r²)`,
   whose only positive-orthant zeros are at `p = q`. So that single configuration
   pair does **not** cover the sub-case `p = q ≠ r`; a second pair is needed and I
   did not run it. **As stated, T2(b) is unproved for `|A_k| ≥ 3`.**

**D8 — T2(d) is correct** (verified exactly, §2). Add its dual
`E_μ[(Π_k Z_k)^{-1}] = Z_W^{-1}`, which is the more usable identity and follows
from the same line plus `Σ_v μ_σ = 1`.

**D9 — T3's Gaussian remark conflates conditioning with marginalising.** For a
Gaussian with precision `Q`: the **conditional** law of a block `A` given the rest
has covariance `(Q_{AA})^{-1}` — the inverse of the *submatrix*; the **marginal**
has covariance `(Q^{-1})_{AA}` — the *submatrix of the inverse*. These differ by
a Schur complement. `W9 = herm(Q^{-1})` is a marginal (covariance) object; the
phrase "pinned-record conditional marginals are `herm(Q_sub^{-1})`" reads as the
other one. Fix the wording, or the remark is wrong. (For a Gaussian menu the
positivity hypothesis is free — Gaussian densities are positive on `R^n` — and
Hammersley–Clifford is just the sparsity pattern of `Q`; worth saying, since it
shows the T1 machinery is trivial in that fixture and therefore carries no
independent evidence there.)

**D10 — a free, honest strengthening the block declines.** The dossier fences off
DLR entirely. But on `Z³` with a *finite* menu the configuration space is compact
and a positive covariant NN specification is quasilocal, so **at least one Gibbs
measure exists**, and by averaging over translations at least one
translation-invariant one. **Uniqueness is not free** — a phase transition would
mean the rule induces several static laws while inducing exactly one action (up to
D3's gauge). One sentence: *the rule induces an action, not a law.* That is a
direct and correct answer to the owner's sequencing question, it strengthens T1's
reading rather than weakening it, and it costs nothing while keeping the no-claim
fence on existence/uniqueness *values*.

**D11 — the cleanest native proof of T1(⇒) does not need Hammersley–Clifford at
all, and the note should say so.** For a positive rule on a finite product space:
a static law exists **iff** the log-conditional-ratio 1-form is closed on the
Hamming flip graph, and it suffices to check **elementary two-site squares** (the
cycle space is generated by within-site 3-cycles, which are automatic because the
ratios come from one conditional distribution, and cross-site 4-cycles). This
gives existence *and* uniqueness in one stroke (Brook's lemma is the telescoping
line integral), and it is the same object as the sum-rule certificate — so the
note gets its positive and negative results from one lemma. Factorisation is then
Besag's Möbius inversion in three lines: `Q(v) = log(μ(v)/μ(0))`,
`Q_A(v_A) = Σ_{B⊆A} (−1)^{|A\B|} Q(v_B 0_{Aᶜ})`, and `Q_A ≡ 0` unless `A` is a
clique; triangle-freeness of `Z³` NN adjacency then leaves vertices and edges.
Presenting it this way (a) discharges the reference-not-borrow policy honestly,
(b) makes the reference-state gauge of D3 visible instead of hidden, and (c)
removes the need to cite an external theorem in the load-bearing step.

---

## 6. NEXT TEST — the single most decisive exact computation

**Close D7 on the declared open 2×2×2 cube, exactly, over `Q[p,q,r]`.** For each
of the 8! orders (or a covering set: one order per `|A_k|` profile that contains a
site with `|A_k| = 3`), form `Π_k Z_k(v_{A_k})` as a polynomial in `p,q,r` and
compute the ideal generated by the differences `Π_k Z_k(v) − Π_k Z_k(v')` over a
spanning set of configuration pairs (single-site changes suffice). **Claim to
test:** the common zero locus of that ideal inside `{p,q,r > 0}` is exactly the
line `p = q = r`. My one-pair spot check already returns the nonzero polynomial
`108 r⁴(p−q)²(p+q)(p+q+4r)³(p²+2pq+2pr+q²+2qr+4r²)`; the sub-case `p = q ≠ r` is
the one still open, and a single further configuration pair should settle it.

This is decisive because it is the *only* place T2(b)'s headline sentence
("for every rule obeying the variation clause and every order, `μ_σ ≠ μ`") is
currently unproved, it is finite and exact, and the `|A_k| = 3` case it probes is
the generic one on `Z³`. Pair it with the `max|A_k| ≤ 2` ANOVA lemma (D7, which I
can prove) and the general-window statement is fully closed for the declared
windows. If instead cancellation *is* found, the block must be re-scoped and the
finding is more interesting than the theorem it replaces.

---

## 7. RANKING AGAINST THE ALTERNATIVES

1. **The proposed block, with the §5 fixes** — highest. It converts a reading
   into a theorem, it is exact and finite, it is the only item that touches the
   owner's stated sequencing question ("identify the framework-level action
   BEFORE any statistical bridge"), and it retires a never-refereed floating-point
   claim (R136) with rational certificates.
2. **(d) a verbatim exact re-proof of R136 under the static reading** — second,
   but it is not a separate item: it *is* T1 done properly, and doing it alone
   would ship the same reading R136 shipped, unlabelled. Fold it in as T1; do not
   run it standalone.
3. **(e) my own alternative: the order-independence theorem.** Ask not "does
   `μ_σ = μ`?" but "is `μ_σ` independent of `σ`?" — the natural homogeneity
   reading of "no site is privileged". Same machinery, same normalisers, and the
   answer (on the evidence above) is that order-independence plus the variation
   clause is contradictory on the plaquette. That is a stronger, non-relative
   statement about the rule itself, it does not depend on privileging the static
   law, and it needs no new objects. I rank it **above** T2(b) as currently
   stated; run it inside the same block.
4. **(c) record-matter: derive a formation/renewal law from the carrier** —
   fourth. It is the item the block's own conclusion demands next (the block says
   the order is physical and unsupplied; this lane tries to supply it), but it is
   a harder, open-ended derivation, not a bounded exact theorem.
5. **(b) U(1)/Maxwell time-selection fork at the linear level** — fifth. Live,
   well-posed, but orthogonal to the action-identification question.
6. **(a) continue the gravity mainline queue** — last. Incremental, and the owner
   stopped the campaign after block 219 yesterday; restarting it needs an owner
   decision, not a panel recommendation.
