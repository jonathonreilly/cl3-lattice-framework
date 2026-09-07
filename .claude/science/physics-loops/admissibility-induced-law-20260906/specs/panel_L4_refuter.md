# L4 — hostile refuter

All numbers below come from exact rational / symbolic computation. Scripts:
`/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-sync-science-task-0c8fac/3a5217b4-5b36-4906-8abe-d27fc3312603/scratchpad/panel/l4_scratch/`
(`a_menu_static_formation.py` symbolic, killed as too slow; `b_fast.py`,
`c_symbolic.py`, `d_sumrule.py`, `e_extra.py`, `f_final.py` all ran to
completion). Product-rule witnesses: (p,q,r)=(2,3,5) and (7,11,13), plus full
symbolic (p,q,r) where feasible. Menu = the six Bloch-axis projectors, encoded
as ±e_a with ⟨P,P'⟩ = 2Tr(PP') − 1 = the dot product of the axis vectors.

I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (231 lines).

---

## 1. VERDICT

**Build with changes.** The mathematical core survives every attack I ran: the
product-rule static law's full conditionals are exactly the rule (0 mismatches
in 66 096 exact identity checks); the formation-law identity
μ_σ = μ·Z_W/Π_k Z_k is exact (0 violations over all orders × all configs on the
3-path and the 4-cycle); "Z(b,c) constant iff p=q=r" is a true symbolic
identity; the one-neighbour normaliser is constant; the sum rule really has an
empty compatibility nullspace on every graph with a degree-2 site and I have an
explicit rational Brook cycle. But **three sentences of the block as written are
false or unproved**, and two of them are load-bearing for the headline claim:
(i) T2(b)'s bridge from the axiom's variation clause to the menu-restricted
rule is a non-sequitur, and I have an explicit positive isotropic rule that
varies on M_2(C), reduces to p=q=r on the six-axis menu, and makes μ_σ = μ for
every order on every window; (ii) T2(b) needs "Π_k Z_k is non-constant", not
"some Z_k is non-constant", and the block only argues the latter; (iii) T2(c)'s
natural reading "distinct orders give distinct laws" is false — 24 orders give
4 laws on the plaquette. Fix those three and the block is sound and worth
building.

## 2. STRONGEST ARGUMENT FROM MY LENS

The block's real content is the *iff*: μ_σ = μ **exactly iff** Π_k Z_k(v_{A_k})
is constant on the support. This follows from the identity plus normalisation
(both μ and μ_σ sum to 1, so a constant ratio must be 1), and it is the only
statement I could not break. Everything else in T2 is a corollary that either
holds or fails according to whether that product is constant — and the block
never proves the product is non-constant, only that one factor is. I verified
non-constancy exhaustively where I could rather than assuming it.

The second-strongest point is a **scope** one, and it is why I do not vote
"build as specified": T2(b) is stated as "for every rule obeying the variation
clause and every order, μ_σ ≠ μ". That sentence quantifies over rules on the
*axiom's* possibility domain (`M_2(C)`, Qubit axiom) while the theorem lives on
a *declared finite menu*. The gap is real and I exhibit it below.

## 3. STEELMAN AGAINST MY VERDICT

Two directions.

*Against "build with changes", for "build as specified":* every defect I found
is in the prose bridging the theorem to the axiom, not in the theorem. If T2(b)
is restated as "for every product rule with (p,q,r) not all equal on the
declared menu, and every order on a window containing a 4-cycle, μ_σ ≠ μ", then
on all four windows I tested it is exactly true, and the block would need no
mathematical change at all — only a sharper hypothesis line.

*Against "build", for "do not build":* the theorem may be true and still not do
the job the dossier wants. The dossier's target is R136's step (ii) — the claim
that Admissibility's conditional *is* a static full conditional. T2 shows the
two objects differ *once you have already granted the product form*. It does not
show which of the two the axiom names, and the axiom explicitly disclaims the
formation site and rate, so the formation order σ is not axiom content either.
The block therefore replaces one un-derived reading (static) with a second
un-derived reading (records-only sequential, a "NAMED premise" by the block's
own admission) and proves they differ. That is a fact about two readings, not
a framework-level action identification. The owner's sequencing rule asks for
"what the Admissibility rule induces on the infinite lattice"; T1/T2 are finite
and give two candidate answers rather than one. And the numbers say the
difference is small: on the plaquette the order-averaged formation law and the
static law are at total-variation distance 29761/1306260 ≈ 2.28e-2, and the
worst single-configuration gap is 1585133/10007780364 ≈ 1.58e-4.

## 4. WHAT WOULD CHANGE MY MIND

- To "do not build": a demonstration that the records-only extension premise
  ("an unrecorded neighbour contributes no factor") is *arbitrary* — e.g. an
  equally natural reading of "only records are readable" under which μ_σ = μ.
  I tried the obvious one (an absence-dependent factor) and it fails by a rank
  argument (§5.6), which pushed me *towards* building.
- To "build as specified": a proof of the missing lemma (§5.2) and a premise
  that makes the declared menu witness the axiom's variation clause (§5.1).
- Against the whole direction: any derivation showing the formation order is
  itself law-determined (so σ is not a free label), which would make T2(c)'s
  order-dependence a statement about an object that does not exist.

## 5. CONCRETE DEFECTS

Ordered by severity. First the things I could *not* break, briefly, so the
defects are read against a verified baseline.

**Verified (attacks failed):**
- Rotation group order 24; the six-axis menu is a single orbit; ordered pairs
  fall into exactly three orbits, sizes (6, ⟨⟩=+1), (6, ⟨⟩=−1), (24, ⟨⟩=0).
- **T1 full-conditional identity**: 0 mismatches. 3-path 3 888 identities;
  4-cycle 31 104; 4-star K_{1,3} 31 104; each at both witnesses.
  Z_W(3-path)=3750, Z_W(4-cycle)=391878, Z_W(4-star)=93750 at (2,3,5).
- **One-neighbour normaliser** Z_1(b) = p+q+4r for every b in the menu — constant,
  as claimed. (Claim (4) of my brief: TRUE, and it is forced by transitivity of
  the menu + isotropy of φ; ψ constant is needed and is itself forced.)
- **Two-neighbour normaliser**, symbolically:
  Z(par) = p²+q²+4r², Z(anti) = 2(pq+2r²), Z(orth) = 2r(p+q+r), with
  Z(par)−Z(anti) = (p−q)², Z(par)−Z(orth) = (p−r)²+(q−r)²,
  Z(anti)−Z(orth) = 2(p−r)(q−r). So **Z(b,c) is constant iff p=q=r**, over the
  reals — positivity is not even needed. (Claim (3): TRUE.)
- **The T2 identity μ_σ = μ·Z_W/Π_k Z_k is correct as written.** Checked
  pointwise: 0 violations over all 6 orders × 216 configs (3-path) and all
  24 orders × 1296 configs (4-cycle). The proof is one line: every edge is
  counted exactly once, by its later endpoint, so the numerator is
  Π_x ψ Π_{xy} φ = Z_W·μ(v).
- **T2(d)** Z_W = E_{μ_σ}[Π_k Z_k]: verified (3750, 391878, 93750, 24018960,
  2058000 all reproduced). It is a triviality — substitute the identity and sum.
- **Plaquette lemma** ("every order on a graph containing a 4-cycle has a site
  with ≥2 recorded neighbours"): TRUE, and trivially so — the last cycle vertex
  in the order has both of its cycle-neighbours already recorded. No dependence
  on the cycle being induced.
- **T1's positivity witness** on the binary 4-cycle: the 8-configuration law is
  Markov (48 conditionals, all consistent with two-neighbour dependence), all
  four value pairs occur on each of the four edges in the support, and 8 of 16
  configurations have μ=0. The block's proposed re-proof argument is therefore
  sound on that witness.
- **Sum rule**, exact compatibility nullspace (unknowns = 6^|W|; equations
  μ(s,v_{−x})·w_t − μ(t,v_{−x})·w_s = 0):
  1-edge 36 unknowns rank 35 **nullity 1**; 3-path 216 rank 216 **nullity 0**;
  4-star 1296 rank 1296 **nullity 0**; 4-cycle 1296 rank 1296 **nullity 0**.
  At λ ∈ {1/10, 1/5, 1/4, 1/3, −1/4} the ≥2-neighbour results are all nullity 0;
  at λ=0 all are nullity 1 (sanity: the uniform law). Product-rule control gives
  nullity 1 on all four graphs. Nullity 0 is stronger than "no probability law":
  there is no *signed* solution either.
- **Brook cycle**, explicit and rational. On the 3-path, sites 1 and 2 flipped
  with v_3 held: a = −e_1, a' = −e_2, b = −e_1, b' = −e_3, c = −e_1 gives
  ratio product (1+2λ)/(1+λ)², i.e. numerator − denominator = −λ². At λ=1/4:
  (3/2)/(25/16) = **24/25 ≠ 1**. 1 848 of the 5 400 four-step cycles tested have
  product ≠ 1; the obstruction's lowest order in λ is 2, matching the archived
  "O(λ²)".

### 5.1 DEFECT (fatal to T2(b) as stated): the menu-restriction gap

T2(b) says Z(b,c) constant "iff p=q=r, i.e. iff the rule does not vary with its
neighbours — which Admissibility forbids". The axiom's variation clause is about
the one-site possibility domain, whose "full one-site possibility domain has
algebraic presentation M_2(C)". The menu M is a *declared finite subset*. A rule
can vary on M_2(C) and be constant on M.

Explicit counterexample: the isotropic pair weight φ(s,t) = f(⟨s,t⟩) with
f(x) = 1 + x²(1−x²). Then f(1) = f(−1) = f(0) = 1, so (p,q,r) = (1,1,1) on the
six-axis menu, while f(1/2) = 19/16 and f(1/√2) = 5/4 — the rule genuinely
varies with the nearest-neighbour conditions. For this rule every Z_k is
constant, so **μ_σ = μ for every order on every window**, including every
window containing a 4-cycle. The universally quantified sentence "for every rule
obeying the variation clause and every order, μ_σ ≠ μ" is therefore false as
literally written.

Fix: state the hypothesis on the declared object — "(p,q,r) not all equal" — and
either drop the axiom-level sentence or add an explicit richness premise
("the declared menu witnesses the variation clause"), which would itself need
proving and is menu-dependent.

### 5.2 DEFECT (unproved lemma, load-bearing): Π_k Z_k, not one Z_k

μ_σ = μ **iff** Π_k Z_k(v_{A_k}) is constant on the support. The block argues
that *one* factor (the site with ≥2 recorded neighbours) is non-constant. That
does not imply the product is non-constant: the factors are functions of
overlapping variable sets and could in principle cancel. The block gives no
lemma ruling this out, and on Z^3 (degree 6) the factors have arities 2 through
6, of which only the arity-2 table is computed.

I could not find a counterexample, and I looked hard:
- 4-cycle: Π_k Z_k non-constant for all 24 orders, exhaustively over all 1296
  configurations. Values {375000, 420000, 423750} (16 orders) and
  {360000, 451584, 459684} (8 orders), against Z_W = 391878.
- 3-path: constant for 4 orders, non-constant for 2, values {3600, 4032, 4068}
  against Z_W = 3750.
- 4-path P_4 and 4-star K_{1,3}: exhaustive, no anomaly.
- 2×2×2 open cube (8 sites, 12 edges, degree 3): all 40 320 orders, exact
  2-configuration certificates from a 402-configuration probe pool. **0 orders**
  had constant Π_k Z_k, and max|A_k| = 3 for all 40 320 orders.
So the lemma is very likely true but is currently *empirical*, not proved. The
general-window statement in T2(b) is unproved as the block stands.

Auxiliary datum for that lemma: the three-neighbour normaliser takes 5 distinct
values on the menu, indexed by the pairwise-overlap pattern of the three
recorded values: (1,1,1)→p³+q³+4r³; (−1,−1,1)→p²q+pq²+4r³;
(0,0,1)→r(p²+pr+q²+qr+2r²); (−1,0,0)→r(2pq+pr+qr+2r²); (0,0,0)→3r²(p+q).

### 5.3 DEFECT: "distinct orders give distinct laws" is FALSE

Exhaustive, both witnesses:

| window | orders | distinct formation laws | orders with μ_σ = μ |
|---|---|---|---|
| 3-path P_3 | 6 | **2** | 4 (123, 213, 231, 321) |
| 4-path P_4 | 24 | **3** | 8 |
| 4-star K_{1,3} | 24 | **5** | 12 |
| 4-cycle C_4 | 24 | **4** | **0** |

On the plaquette the 24 orders collapse to 4 laws (two classes of 8, two of 4);
the two 8-classes even share the same *multiset* of Π_k Z_k values
{375000, 420000, 423750} yet differ as functions of v. T2(c) as written ("μ_σ
depends on σ") is true; the stronger reading is false and must not be written.
The counts above are the honest statement and are worth reporting as the result.

### 5.4 DEFECT: the sum rule's inconsistency is graph-conditional

The block writes the sum rule's inconsistency without a degree hypothesis. On a
single edge the sum rule **is** consistent: nullity 1, and the joint law is
exactly μ(s,t) = (1 + λ⟨s,t⟩)/36 (verified to sum to 1). The inconsistency
requires a site of degree ≥ 2. Any runner statement must be scoped that way, or
it is false on the 1-edge window the block would naturally include.

### 5.5 DEFECT: sum-rule positivity is degree-dependent and λ=1/4 is illegal on Z^3

r(s|η) ∝ 1 + λ Σ_y ⟨s,η_y⟩ is positive only for |λ| < 1/deg. At λ = 1/4 the
rule is positive on the 3-path, 4-cycle and 4-star (degrees 2, 2, 3) but the
degree-6 sites of Z^3 need |λ| < 1/6, and λ=1/4 gives weight 1 − 6/4 = −1/2.
The block's "positive for |λ| small" needs the explicit bound, otherwise the
finite-window results do not transfer to the Z^3 window the block also declares.

### 5.6 Escape routes I tested — all closed, two more sharply than the block claims

- **Non-constant site weight ψ.** The block closes this by "breaks covariance on
  a transitive menu". Stronger exact result: treat "Z(b,c) constant" as a
  homogeneous *linear* system in the six values ψ(s), with no positivity and no
  covariance assumed. Rank = 6 for generic (p,q,r) and at (2,3,5), so the
  ψ-nullspace is **0-dimensional**: no site weight whatsoever, signed included,
  makes the two-neighbour normaliser constant. Use this instead — it does not
  lean on covariance.
- **Absence-dependent extension φ_abs.** On the 3-path with the order (1,3,2),
  the most general factorised absence weight contributes χ_1(v_1)·χ_3(v_3), so
  μ_σ = μ requires χ_1(b)χ_3(c) = k·Z(b,c) — i.e. Z as a 6×6 matrix must have
  rank 1. It has **rank 6** (symbolically, and at (2,3,5) the matrix is
  113 on the diagonal, 112 on the antipodal pairs, 100 elsewhere). Route closed
  by rank, exactly. Two 2×2 minors: (p−q)²(p²+2pq+q²+8r²) and
  ((p−r)²+(q−r)²)(p²+2pr+q²+2qr+6r²).
- **Averaging over all formation orders.** Uniform mixture over the 24 orders on
  the plaquette: sums to 1, but ≠ μ. Total variation distance
  29761/1306260 ≈ 0.022783; worst pointwise gap 1585133/10007780364 ≈ 1.5839e-4
  at v = (+e_1, +e_2, +e_1, +e_2), where μ = 625/391878 ≈ 1.59488e-3 and
  mixture = 1981/1379052 ≈ 1.43649e-3. Route closed with exact numbers.
- **Constant rule.** Closed on the menu, *not* closed against the axiom — that
  is defect §5.1.
- **Non-product rules.** Correct that there is no static law to compare with;
  nothing to check.

### 5.7 Minor: S_W's definedness

The pair (ψ, φ) reproducing a given μ is only unique up to the gauge
φ → φ(s,t)g(s)g(t), ψ → ψ(s)g(s)^{−deg(s)}, plus an overall scale. On the
declared menu covariance forces g constant, so S_W is unique up to an additive
constant — but that is a *consequence of the menu being a single orbit*, not
automatic. T3 calls S_W "the object the rule induces statically"; it should say
so with the gauge remark, or the claim is over-strong for any non-transitive
menu (and the block's own scope allows declared menus generally).

### 5.8 Nothing depends on the open boundary or on ψ

Checked: T1 and T2 hold identically on the 3-path (degrees 1,2,1), the 4-star
(degrees 1,1,1,3), the 4-cycle (regular, no boundary) and the 2×2×2 cube
(regular degree 3, all-boundary). ψ is forced constant on a transitive menu and
plays no role beyond the constant Z_0 = |M| = 6. No boundary dependence found.

## 6. NEXT TEST (single most decisive)

Prove or refute the missing lemma of §5.2: **for a covariant product rule with
(p,q,r) not all equal, on any finite window containing a 4-cycle, and any
formation order, Π_k Z_k(v_{A_k}) is non-constant.** The decisive exact
computation is a search for a counterexample: enumerate every connected
triangle-free graph on ≤ 6 vertices (and the 2×3 and 2×2×2 Z^3 windows), every
formation order, and test Π_k Z_k for constancy exactly with symbolic (p,q,r)
rather than a numeric witness — a numeric witness could hide an accidental
coincidence, and a symbolic constancy would be the counterexample. If nothing is
found, the proof to write is: log Π_k Z_k = Σ_k g_{|A_k|}(v_{A_k}) is a sum of
functions of the recorded-neighbour sets, and the arity-2..6 tables above are
strictly ordered (Z(par) > Z(anti) and Z(par) ≥ Z(orth) with the stated
differences), so no cancellation is possible. Without this, T2(b)'s
general-window claim is not a theorem, and it is the block's headline.

## 7. RANKING AGAINST THE ALTERNATIVES

1. **The proposed block, with the three changes in §5.1–§5.3.** It produces
   exact, checkable finite theorems, closes four named escape routes with exact
   certificates, and it is the only item on the list that touches the R136
   step (ii) reading directly.
2. **(d) verbatim exact re-proof of R136 (static reading only).** Cheaper and
   strictly needed anyway: my §5 shows the R136 pieces (sum-rule nullity, Brook
   obstruction O(λ²), Z-constant-forces-rank-1) all reproduce exactly in
   rationals. It is a subset of the proposed block and could be landed first as
   the low-risk half if the panel wants the block split.
3. **(c) record-matter lane: derive a formation/renewal law from the carrier.**
   Ranked above the gravity and Maxwell items because T2's whole payload is
   conditional on the formation order being a free label; if a formation law is
   derivable, T2(c) becomes a statement about a determined object rather than a
   free one, and the block's value goes up or down sharply.
4. **(b) U(1)/Maxwell time-selection fork at the linear level.** Concrete and
   live, but orthogonal to the axiom-level question this panel was convened for.
5. **(a) gravity mainline queue.** The owner stopped the campaign after block
   219 yesterday; resuming it needs a reason this panel does not supply.
6. **(e) my own alternative, ranked below the block but worth naming:** state
   and prove *only* the iff — "μ_σ = μ iff Π_k Z_k is constant on the support"
   — plus the exhaustive order/law tables of §5.3, and drop every
   negative-shaped universally quantified sentence. That is what actually
   survived my attacks, it needs no axiom-level bridging sentence, and it is
   about a third of the work.

## Honest failures

- I did not prove the §5.2 lemma; I only failed to find a counterexample over
  four exhaustive windows and 40 320 cube orders with sampled certificates.
- The cube scan (§5.2) used a 402-configuration probe pool, not all 6^8 =
  1 679 616 configurations. It gives exact *non-constancy* certificates (two
  configurations with different exact values), which is what is needed, but it
  could not have certified constancy had any order been constant.
- I did not test the 2×2×2 cube's compatibility nullspace for the sum rule
  (6^8 unknowns), nor any window with a degree-6 site.
- My first symbolic script (`a_menu_static_formation.py`) was too slow to
  finish and was killed; everything reported came from the exact-rational
  re-runs at two independent witnesses plus targeted symbolic work.
