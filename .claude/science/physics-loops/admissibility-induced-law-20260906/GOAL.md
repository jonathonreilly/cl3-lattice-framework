# Goal — the formation law of a nearest-neighbor rule versus its static law on finite windows (block 01, 2026-09-06; contract v2 after the panel)

## Why this block (the owner's sequencing gate)

The owner's standing rule (2026-08-26): identify the framework-level object
that the Admissibility rule induces on the lattice BEFORE any statistical
bridge is considered; the gravity lane's finite quadratic forms are measuring
instruments, not that object. The archived Opus-direct packet (result R136,
floating point, never refereed) answered "the rule's form is forced to a
neighbor product" by reading the Admissibility conditional as the full
conditional of one static joint law over complete configurations. The Record
axiom describes permanent records forming one site at a time, and its Open
Gates list leaves "at which site" outside axiom content. So two objects can be
built from one rule on a finite window: the static law (one joint law whose
full conditionals are the rule) and the formation law (the chain of the rule's
conditionals along a formation order, conditioning on records only). This
block defines both exactly, proves exactly when they coincide, and shows they
never coincide on a window containing a plaquette. It does NOT identify the
infinite-lattice object and says so; it does not fire wake condition 1 of
`docs/repo/DEFERRED_DECISIONS.md` entry 1.

Panel record (four lenses, 2026-09-06; synthesis in `REVIEW_HISTORY.md`):
the product-level lemma was missing from the first contract and is now proved
(the single-site variation lemma below); the static half is a landed binary
theorem and is cited, not re-proved; the records-only extension is one of
three named readings, not "the natural reading"; the headline is a positive
classification, not a negative; the Gaussian remark is rewritten with its
hypotheses; the infinite-lattice non-claim is explicit.

## Exact target contract

**Declared objects.**

- Menu `M`: the six Bloch-axis pure-state projectors
  `P(±e_a) = (I ± σ_a)/2`, `a ∈ {x,y,z}`, inside the one-site domain
  `M_2(C)`. The 24 proper cubic rotations act on `M` by signed axis
  permutations (spinor conjugation induces exactly that action; checked
  exactly for two generators). Ordered pairs fall into three orbits: parallel
  (6), antiparallel (6), orthogonal (24), labelled by `Tr(PP') ∈ {1, 0, 1/2}`.
  The menu is transitive under the rotations.
- Windows: finite graphs with nearest-neighbor edges — the three-site path,
  the four-site star, the four-cycle (one plaquette of `Z^3`), the open
  `2×2×2` cube (8 sites, 12 edges); open boundary by default, plus one
  declared exterior record assignment on the four-cycle and the cube for the
  boundary-conditioned static law.
- A nearest-neighbor rule `r`: for a site `x` and an assignment `η` of menu
  values to a SUBSET `A ⊆ N(x)` of its neighbors (the recorded ones), a
  probability vector `r(· | η)` on `M`. Covariant: `r` depends on `η` only
  through rotation-orbit data. Positive: every entry strictly positive.
  - (P) product rules `r(s | η) ∝ ψ(s) Π_{y ∈ A} φ(s, η_y)`, `φ` symmetric,
    isotropic, positive with orbit values `(p, q, r)` on `M`; `ψ` covariant,
    hence constant on the transitive menu (executed: the covariance equations'
    solution space for `ψ` is one-dimensional).
  - (S) the sum rule `r(s | η) ∝ 1 + λ Σ_{y ∈ A} ⟨s, η_y⟩`,
    `⟨P, P'⟩ = 2 Tr(PP') − 1 ∈ {1, −1, 0}`, at rational `λ` with `|λ| < 1/6`
    (positive on every shell) and symbolically.
- **Three readings of the rule at a partially recorded neighborhood** (all
  named; none is axiom content; the Admissibility sentence says "conditions",
  the Record sentences say only records are readable and an unrecorded site
  cannot be read):
  - R-only (records-only extension): an unrecorded neighbor contributes no
    factor and is not a condition — equivalently a constant absence factor;
  - absence-as-condition: an unrecorded neighbor in lattice direction `d`
    contributes a covariant factor `φ_abs(s, d)` with orbit values
    `(a, b, c)` by the orbit of (forming value, absent direction);
  - marginal reading: the conditional at `x` given the recorded set `A` is
    the static law's own conditional `μ(v_x | v_A)`.
- The STATIC law of a rule on `W` with exterior records `ω` (empty for the
  open boundary): a probability law `μ` on `M^W` whose full conditionals equal
  the rule with all neighbors (interior and exterior) recorded. A rule is
  *consistent* on `W` iff such `μ` exists.
- The FORMATION law of a rule for a formation order `σ = (x_1, …, x_n)`
  under R-only: `μ_σ(v) = Π_k r(v_{x_k} | v restricted to A_k)`,
  `A_k = N(x_k) ∩ {x_1, …, x_{k−1}}`. The axioms supply no order; every
  statement quantifies over orders or names a declared order family.

**Theorem A (the static law of a product rule; the landed binary theorem
generalized and cited, not re-proved).** For every finite graph `W`, every
exterior assignment `ω`, and every (P): the law
`μ_W^ω(v) ∝ Π_x ψ(v_x) Π_{xy ∈ E(W)} φ(v_x, v_y) Π_{x ∈ W, y ∈ ∂W} φ(v_x, ω_y)`
has full conditionals equal to the rule (direct cancellation) and is the
unique law with those full conditionals (Brook's ratio lemma for a finite
menu, re-proved in two paragraphs). The landed note
`docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`
is the binary case (linked as upstream); the general converse (only
product-form rules are consistent on triangle-free graphs) is a reference
only, not used and not re-proved. The sum rule (S) is not consistent on the
three-site path: exact certificate (the compatibility system has full rank at
`λ ∈ {1/4, −1/8}`; the Brook cycle at sites 1–2 gives a rational function
`R(λ)` with `R(1/4) = 27/25` and `R(λ) − 1` carrying the factor `λ²`, no
other root in `|λ| < 1/6`).

**Theorem B (the formation law; the classification — the headline).** For
every finite graph `W`, every (P) with `(p, q, r)` not all equal, every order
`σ`, under R-only:
- (B1, identity) `μ_σ(v) · Π_k Z_k(v_{A_k}) = μ(v) · Z_W` for every `v`,
  with `Z_k(η) = Σ_s ψ(s) Π_{y ∈ A_k} φ(s, η_y)` the local normalizer at
  `x_k` and `Z_W` the static partition function. Hence `μ_σ = μ` iff
  `Π_k Z_k(v_{A_k})` is constant in `v`.
- (B2, classification) `μ_σ = μ` **iff every site forms with at most one
  recorded neighbor** (`|A_k| ≤ 1` for all `k`).
  (⇐) The one-neighbor normalizer `Σ_s ψ(s) φ(s, t) = ψ (p + q + 4r)` is
  independent of `t` (transitivity), and the zero-neighbor normalizer is
  constant, so the product is constant.
  (⇒, the single-site variation lemma) If `|A_m| ≥ 2` for some `m`, pick
  `y ∈ A_m` and fix every other site at a reference value `R`. Every factor
  `Z_k` with `y ∉ A_k` is then constant; every factor with `y ∈ A_k` and
  `|A_k| = 1` is constant; every factor with `y ∈ A_k` and `|A_k| ≥ 2`
  equals `f_j(orbit(v_y, R))` with `j = |A_k| − 1 ≥ 1`, where
  `f_j(par) = p^{j+1} + q^{j+1} + 4 r^{j+1}`,
  `f_j(anti) = p q^j + q p^j + 4 r^{j+1}`,
  `f_j(orth) = (p + q) r^j + r (p^j + q^j) + 2 r^{j+1}`, and
  `f_j(par) − f_j(anti) = (p − q)(p^j − q^j) ≥ 0` with equality iff `p = q`,
  while at `p = q`, `f_j(anti) − f_j(orth) = 2 (p − r)(p^j − r^j) ≥ 0` with
  equality iff `p = r`. The multiset of such factors is nonempty (it contains
  `k = m`), each factor is positive, so their product is constant across the
  three orbits iff `p = q = r`. As `v_y` ranges over the menu it meets all
  three orbits relative to `R`, so `Π_k Z_k` is not constant and `μ_σ ≠ μ`.
- (B3, corollaries) An order with `|A_k| ≤ 1` for all `k` exists iff `W` is
  a forest (every edge is charged to its later endpoint), and then such orders
  are exactly the root-outward sweeps of each component; on every window
  containing a cycle — every plaquette of `Z^3` — no order gives `μ_σ = μ`.
  Executed: path3 exactly 4 of 6 orders; star4 exactly 12 of 24; cycle4 0 of
  24 (all laws computed); cube8: all 40,320 orders have some `|A_k| ≥ 2`
  (combinatorial), the identity (B1) and the inequality on a declared order
  family and configuration family; the `f_j` formulas and their factorizations
  symbolic for `j = 1, 2, 3`; the single-site variation instances on the cube.
- (B4, the constant rule) At `p = q = r` the rule's output is the uniform
  measure under every condition (executed) and `μ_σ = μ` for every order.
  Under the extensional reading of the Admissibility sentence "determined by,
  and varies with, the nearest-neighbor conditions" — a named reading — the
  constant rule is excluded, so B2's "not all equal" hypothesis is the
  variation clause.
- (B5, order dependence) `μ_σ` depends on `σ`: the number of distinct
  formation laws over all orders (path3 2, star4 5, cycle4 4 at the declared
  weights; the classes reported; an invariant stated only if proved).

**The six readings and routes by which the two laws could still coincide
(executed; they answer N1–N8 for the corollary "never on a plaquette").**
(1) the constant rule (coincides; excluded by the named reading of the
variation clause); (2) a non-constant site weight (breaks covariance on the
transitive menu; executed); (3) a direction-blind absence factor
`φ_abs(s)` (covariance forces it constant, so R-only is without loss of
generality inside that subfamily; executed as a solution-space dimension);
(4) a direction-dependent covariant absence factor `(a, b, c)`: on the
four-cycle with order `(0,1,2,3)` and on the path with order `(0,2,1)`, the
equations `μ_σ = μ` on a declared configuration set force `a = b = c` and
`p = q = r` (sympy solve; then verified on every configuration at the found
solutions); (5) the uniform mixture of `μ_σ` over all 24 orders of the
four-cycle differs from `μ` (exact maximum difference reported); (6) the
marginal reading makes `μ_σ = μ` for every order by the chain rule, but it is
not one fixed nearest-neighbor rule: the one-neighbor conditional it assigns
on the path equals the rule's, while on the four-cycle it does not (exact:
`219/866` against `1/4` at `(3,1,2)`) — the same recorded condition receives
different odds on different windows.

**Named objects (remarks; no computation beyond the above).** The static
action `S_W^ω = −Σ log ψ − Σ log φ` (unique up to the gauge
`φ → φ h(s) h(t)`, `ψ → ψ h^{−deg}`, and a constant); the formation action
`S_W + Σ_k log Z_k(v_{A_k})`; the family `{μ_W^ω}` over windows and exterior
assignments is a specification — its infinite-volume existence or uniqueness
is not claimed (next block). Gaussian analogy, three sentences with stated
hypotheses: for a REAL SYMMETRIC POSITIVE-DEFINITE quadratic pair form the
static law is Gaussian with that precision; pinning records fixes a
sub-block of the precision, and the read-slice block of its inverse is the
read-slice marginal covariance under the pinned law — a static,
conditional-then-marginal object, not a formation-order conditional; the
parked bridge text's weights are the normalized diagonal of such a block on a
different carrier, so this is a cross-carrier analogy, and the 2026-08-26
gate measurement is a float measurement on one fixture, cited by path, on
which this note has no bearing.

**Quantifiers / domain.** Theorem B's proof is for every finite graph; every
executed instance is on the declared windows and menu. No infinite-volume
existence or uniqueness; no selection of the physical rule, order or
reading; no formation site, probability or rate; no Born, bridge or readout
statement; no axiom or primitive change; the note does not fire wake
condition 1 of `docs/repo/DEFERRED_DECISIONS.md` entry 1.

**Allowed premises.** The four axioms (quoted verbatim where used); the
declared menu and windows; exact integer, rational and symbolic arithmetic;
R-only as a named reading with its two alternatives named and computed.
Brook's ratio lemma re-proved at the finite-menu scope; the landed binary
note linked; Hammersley–Clifford referenced only.

**Forbidden.** Floating point anywhere in the runner; any sentence selecting
a rule, a `λ`, an order, or a reading; any infinite-lattice statement beyond
naming the specification and the open question; any claim that this block
derives, explains, bears on or decides the parked bridge, the Born form, or
the gravity lane's action; "the order is physical" as a claim (the honest
sentence: the pattern of records depends on the order, so the rule alone does
not fix the pattern, and whatever fixes the order is physics the axioms leave
open); the words "certified", "closed", "complete", "global", "the law"
outside their exact finite meaning.

**Completion witness.** A note with the definitions, Theorem A (cited and
generalized), Theorem B with the native proof and obligation graph, the six
executed readings/routes under N1–N8, the named objects, falsifiers, fences;
an exact runner (TOTAL line, N5 certificate, declared mutations each flipping
exactly one check family); the pinned cache; the pack's block records; a PR
off `main`.

**What does not count.** Floating-point evidence; a re-proof of
Hammersley–Clifford; the positivity counterexample (a scope illustration, not
needed); any claim about `Z^3` beyond the plaquette corollary; a static-
reading-only restatement of R136.

## Value gate answers (V1–V5), in advance (supervisor; the primary answers its own)

- V1: no `verdict_rationale` names this; the obstruction is the owner's
  sequencing gate and the scorecard's Root-A live attack ("uniqueness of the
  FORM from NN-determination + Record consistency, as native new theorems").
  This block is a falsifier and a hard-premise test at that gate, stated as
  `upstream_support` with the consumers named; it closes nothing.
- V2: new — the formation law as an object; the identity B1; the
  classification B2 with its proof; the plaquette corollary; the six
  executed readings/routes including the window-dependence of the marginal
  reading. Sweep recorded in `ROUTE_PORTFOLIO.md`; the binary note is cited
  as the static half.
- V3: the static half is standard machinery (cited); the classification
  needs the covariant menu's orbit structure and the `f_j` lemma, which the
  audit lane does not have.
- V4: non-trivial — B2 is a classification, not an identity; B1 alone would
  fail V4 and is presented as the tool, not the result; the partition
  identity `Z_W = E_{μ_σ}[Π Z_k]` is a runner consistency line, not a
  theorem.
- V5: no landed or archived note compares a formation-ordered law with a
  static law; the closest objects are the binary compatibility note (static
  only) and R136 (static reading, floats).

## Amendments after the rigor and refuter lenses (contract v2.1; these override the text above where they differ)

1. **Hypothesis on the menu, with its boundary witness.** Theorem B's
   hypothesis is "`(p, q, r)` not all equal ON THE DECLARED MENU". The axiom's
   variation clause is about the full one-site domain `M_2(C)` and does not
   imply variation on a finite menu: the isotropic pair weight
   `φ(s, t) = f(2 Tr(PP') − 1)` with `f(x) = 1 + x²(1 − x²)` gives
   `f(1) = f(−1) = f(0) = 1` (so `p = q = r = 1` on the six-axis menu and
   `μ_σ = μ` for every order on every window) while `f(1/2) = 19/16` and
   `f(1/√2) = 5/4` (executed as exact rationals). So the reading used is "the
   variation clause restricted to the declared menu", named as such; no
   sentence bridges from the axiom's clause to the menu without that name.
2. **Positivity is a named premise.** The axioms allow zero-probability
   possibilities (admissibility is the support). A positive rule means
   `r(s | η) > 0` for every `s ∈ M` and every partial assignment `η`; for
   (P) this is `ψ > 0`, `φ > 0` on the menu. Lemma (stated, one paragraph):
   a positive rule's static law is positive on every configuration (the
   single-site-change graph on `M^W` is connected), which is what licenses
   Brook's ratio lemma.
3. **Symmetry of the pair weight on `Z^3` windows.** For windows of `Z^3`,
   the element `g = t_{e_1} ∘ R_{e_2, π}` (unit translation after the proper
   half-turn about `e_2`, both in the axioms' group) sends `0 ↦ e_1` and
   `e_1 ↦ 0`, so covariance forces `φ(a, b) = φ(ρ(R) b, ρ(R) a)`, and with
   isotropy `φ(a, b) = φ(b, a)` (executed as a signed-permutation check). On
   the abstract model graphs (path, star, cycle) uniformity and symmetry of
   `φ` are class-(P) hypotheses, not consequences. Symmetry is what makes the
   formation identity hold: with an asymmetric pair weight the sequential
   product orients every edge later-after-earlier and is not a reweighting of
   any single static law (stated; one executed instance on the three-site
   path).
4. **The sum rule's obstruction is degree-dependent.** On a single edge the
   sum rule IS consistent (`μ(s, t) = (1 + λ⟨s, t⟩)/36`, executed); the
   obstruction needs a site of degree at least two. Positivity of the sum rule
   holds for `|λ| < 1/deg`; the declared couplings are `λ = 1/4` on the path
   (degree 2) and `λ = −1/8` on every declared window and on the `Z^3` shell
   (degree 6 needs `|λ| < 1/6`).
5. **The product-level lemma is the single-site variation lemma** (Theorem B,
   B2 ⇒), proved for every arity; the `f_j` formulas are executed for
   `j = 1, …, 5` (the `Z^3` shell has at most five recorded neighbors before
   the last). The `f_j(par) − f_j(anti) = (p − q)(p^j − q^j)` identity is
   elementary for every `j`; the `f_j(anti) − f_j(orth)` identity is derived
   in the note by counting the six `s` by their orbit relative to `(v_y, R)`.
6. **Order dependence, stated honestly.** Distinct orders need not give
   distinct laws: the census is path3 6 orders → 2 laws (4 equal to `μ`),
   four-site path 24 → 3 laws (8 equal to `μ`), star4 24 → 5 (12), cycle4
   24 → 4 (0). The four-site path is added as a fifth declared window. No
   sentence says "distinct orders give distinct laws".
7. **Two routes closed by rank, without covariance.** (2) The site weight:
   "`Z_2(b, c)` constant" as a homogeneous linear system in the six values
   `ψ(s)` has rank 6 at the declared triples (no signed site weight makes the
   two-neighbor normalizer constant). (4) Any factorized absence weight: on
   the path with order `(0, 2, 1)` the middle site's normalizer must factor as
   `χ(v_0) χ(v_2)`, i.e. the `6 × 6` matrix `Z_2(b, c)` must have rank 1; it
   has rank 6 (executed; two `2 × 2` minors `(p − q)²(p² + 2pq + q² + 8r²)` and
   `((p − r)² + (q − r)²)(p² + 2pr + q² + 2qr + 6r²)` stated). The same rank
   fact says the normalizer history couples sites at graph distance two
   non-multiplicatively: the formation law is not a nearest-neighbor field of
   the static kind (remark, executed through the rank).
8. **What the rule induces, said precisely.** The finite-window static laws
   with exterior records form a specification, i.e. the rule induces a static
   ACTION (a gauge class, canonical up to a constant on the transitive menu)
   rather than a single law; whether the infinite lattice carries one static
   law or several is the phase question and is not claimed. The formation
   reading adds the order-dependent normalizer history. Both sentences are
   remarks; nothing infinite-volume is executed or claimed.
9. **Wording bans, extended.** Never write that the declared menu witnesses
   the axiom's variation clause; never write "distinct orders give distinct
   laws"; the Gaussian analogy stays at three sentences with its hypotheses
   (real symmetric positive-definite form; conditional-then-marginal block;
   cross-carrier).
