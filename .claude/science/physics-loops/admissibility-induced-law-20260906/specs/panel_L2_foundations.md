# L2 — foundations / quantum-measurement lens

Read: complete `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines: four axioms,
the three Admissibility reading notes, Qualification, Audit-Pipeline Treatment,
Relation-to-Dynamics, the older-parent and 2026-06-05 relations, Open Gates,
Historical Context/revision history). Also read `docs/repo/DEFERRED_DECISIONS.md`
entry 1 and `archive/campaigns/exercise-bridge-adoption-20260826/SIGNING_TEXT_FINAL.md`.
Exact computations run in scratchpad (`l2_checks.py`, `l2_alpha.py`); results quoted below.

---

## 1. VERDICT

**Build with changes.** The block's core object — the exact identity
μ_σ(v) = μ(v)·Z_W / Π_k Z_k(v_{A_k}) and the demonstration that the two laws
differ — is correct, is native, and does real foundational work: it converts the
axioms' own open gate "at which site" from a missing detail into a *load-bearing
input to any action identification*. But three of the dossier's framings are not
licensed by the axiom text and must be rewritten before the note is drafted:
(i) the records-only extension is **not** "the natural reading of 'only records
are readable'" — it is one named premise among at least three, and it is not the
value-free option; (ii) the layman line "the order is physical" asserts exactly
what the Open Gates list leaves open, and must go; (iii) T2(b)'s inference from
"one local normaliser is non-constant" to "μ_σ ≠ μ" is a non-sequitur as written
and needs a product-level lemma. Additionally the block does **not** address the
owner's infinite-lattice gate and must say so in its own scope fence in those
words, rather than implying the finite S_W is the induced action.

## 2. STRONGEST ARGUMENT FROM THIS LENS

Read literally, **both** objects are readings; the dossier is right that R136's
step (ii) smuggles, but wrong to treat the formation law as the axiom-faithful
counterpart. Count the supplied content:

*Static law* smuggles two things the axioms do not assert: (a) that a joint law
over **complete** record configurations of W exists at all, and (b) that the
Admissibility conditional equals its full conditional. Textual support for (a)
is real but partial — Qualification says "A state is a configuration of records"
and "A law privileges no states … at every state where the condition holds it
gives exactly one answer", which is precisely the shape of a full-conditional
specification. Nothing says a complete configuration is ever realised; Record
says records *form*, one per site, permanently, and there is no time metric in
which "all of W is recorded" is reached.

*Formation law* smuggles **more**: (a) a total order σ on W — the Open Gates list
names "the remaining formation rules (the distribution's form and values, at
which site, and at what rate)" as outside axiom content, so σ is supplied, not
derived; (b) the records-only conditioning rule; (c) that formation is a Markov
chain in σ with no memory beyond recorded neighbour values; (d) that every site
of W forms exactly once. On Z^3 it smuggles a fourth thing that is not merely
unsupplied but in tension with axiom text: a rooted sweep **privileges a site**,
and Lattice says "No site is privileged." A fixed σ on the infinite lattice is
therefore not an axiom-admissible object; only a translation-covariant law over
orders is.

So the honest content of the block is a **conditional dichotomy**, not an
identification of the physical law: *no order-free local action is induced by a
positive covariant nearest-neighbour rule unless a further premise (a complete-
configuration joint law, or order-independence) is supplied.* Stated that way it
is exactly on-axiom and it is the strongest thing anyone in this repo has said
about the action-ID gate. Stated the dossier's way ("the order is physical, and
the formed pattern is not the equilibrium pattern") it is an unlicensed physical
claim resting on the same class of move it convicts R136 of.

On charge (2) specifically. Admissibility's input word is **"conditions"**, not
"records" and not "readouts". Record's clause "Only records are readable … A
site with no record cannot be read" governs *readout*, not the rule's dependence;
Qubit gives *every* site a domain of local possibilities whether or not it
carries a record; and the Historical Context says the rule fixes the distribution
"from the nearest-neighbor conditions … **before** a record can lock one
available local possibility" — i.e. the conditions are logically prior to
locking. Nothing licenses "condition = record content". Three readings are
available and none is axiom content:

- **R-only** (the block's): an unrecorded neighbour contributes no factor. This
  is *not* the absence of a choice — it is the choice φ_abs(s) ≡ const. The
  2026-08-13 revision note says the axioms "do not assign a scalar value to
  absence"; a constant factor is a value. Under R-only the variation clause
  ("varies with the nearest-neighbor conditions") is silent at exactly the sites
  where formation begins: the first-formed site's distribution is ψ, which
  varies with nothing.
- **Absence-as-condition**: absence is itself a nearest-neighbour condition
  value, weight α(s,u) with u the absent neighbour's lattice direction (three
  orbit values under covariance). Keeps the variation clause contentful
  everywhere.
- **Mean-field / self-consistent**: an unrecorded neighbour's "condition" is its
  own admissibility distribution, not a locked value. This reading is closest to
  the literal wording (the neighbour *has* a condition; it just is not readable),
  and it is **not** covered by any of the block's five attempted routes — route 5
  ("non-product rules") misses it, because such a rule can still be product-form
  on complete configurations, so the static law exists and the comparison is live.

Effect on T2: I checked the first two exactly and they do **not** rescue the
result (see §5), which is good news for the block — but the theorem must be
stated premise-relative ("under R-only", "under any covariant absence extension"),
not as if R-only were free.

## 3. STEELMAN AGAINST MY VERDICT

The strongest case for building as specified: the reading notes are labelled
*interpretive, non-governing*, and note (2) says the distribution "concerns which
possibility a **forming** record locks, conditional on formation at that site".
That is the axiom set's own gloss and it is sequential in shape — a forming
record, at a site, conditional on formation there. If one takes note (2)
seriously, the formation law is the object the memo has in mind and the static
law is the outsider. Combined with Record's "Only records are readable", a reader
can fairly say that whatever a rule conditions on must at least be *available*,
and unrecorded neighbours are the paradigm of unavailable. On that reading
R-only is not a smuggled premise but a consequence of taking Record and reading
note (2) together, and my "conditions ≠ records" objection over-reads a word in a
sentence that predates the Record clause it is being read against.

I do not think this wins — "readable" is a readout predicate and note (2) is
explicitly non-governing, and note (2) also disclaims the formation *site*, which
is precisely σ — but it is close enough that the block must **name** the premise
rather than declare a natural reading, and that costs the block nothing.

## 4. WHAT WOULD CHANGE MY MIND

- An owner ruling (or an axiom revision) that fixes "nearest-neighbor conditions"
  to mean recorded neighbour content. That would make R-only governing and my
  §2 objection evaporates; T2 becomes unconditional.
- A proof that the mean-field reading collapses to R-only (i.e. that conditioning
  on an unrecorded neighbour's *distribution* rather than its value gives the
  same formation law up to normalisation). I expect this is false, but I have not
  computed it.
- A proof that the uniform (or any translation-covariant) order-average equals
  the static law on every finite window. That would kill the "order is
  load-bearing" headline, because on Z^3 the no-privileged-site clause forces the
  order-averaged object anyway. I checked this on the plaquette and it is false
  there (§5, exact defect), so this would have to come from a structural argument
  that overrides my computation — it will not.
- For the action-ID gate: a boundary-conditioned T1 plus a DLR existence argument
  would make the block genuinely gate-addressing; absent that, my §7 ranking of it
  as "upstream support, not gate closure" stands.

## 5. CONCRETE DEFECTS

**D1 (T2, the headline inference — real gap).** T2(b) argues: every order on a
window with a 4-cycle has a site forming with ≥2 recorded neighbours, the
two-neighbour normaliser is non-constant, "so μ_σ ≠ μ". That does not follow. By
the block's own master identity, μ_σ = μ **iff Π_k Z_k(v_{A_k}) is constant in v**
— non-constancy of one factor does not preclude cancellation across factors. The
missing lemma is a product-level statement. On the 4-cycle it is provable in two
lines (only the last-formed site's Z couples its two non-adjacent neighbours, so
constancy of the product forces that Z to be independent of one argument, and
symmetry then forces it constant, hence p=q=r); on a general window it is not
proved and the block should either prove it by induction on the last-formed site
or restrict the general claim to windows where the argument runs.

**D2 (T2, premise labelling).** "the records-only extension … a NAMED premise,
the natural reading of 'only records are readable'". Delete "the natural reading".
R-only is φ_abs ≡ const, a supplied value for absence that the axioms decline to
supply (see §2). State T2 as: *under R-only*, and separately *under any covariant
absence extension*.

**D3 (T3, the Gaussian remark — as worded it is wrong in two independent ways).**
The dossier writes: "a quadratic pair weight is a Gaussian Markov field whose
precision is Q and whose pinned-record conditional marginals are herm(Q_sub^{-1})
— the object the parked Bridge text calls W9".
- *precision vs. covariance vs. which submatrix.* For exp(−½ vᵀQv), Q is the
  precision and the Markov structure is read off the **zeros of Q**, not of Q^{-1}.
  Pinning a set A to 0 gives the free block precision Q_BB (submatrix of the
  precision) and conditional covariance (Q_BB)^{-1}; the **block of the inverse**
  (Q^{-1})_BB is the *marginal* covariance and is a different matrix. Exact
  witness computed: A = [[2,1,0],[1,2,1],[0,1,2]]; (A^{-1})_{23,23} =
  [[1,−1/2],[−1/2,3/4]] but (A_{23,23})^{-1} = [[2/3,−1/3],[−1/3,2/3]]. The
  signing text's W9 is *first* record-substituted (pinned), *then* inverted,
  *then* the read-slice **block** is taken — so it is "conditional on the pins,
  **marginal** over the remaining free levels". "Conditional marginals" without
  that spelled out is ambiguous and, read the other way, false.
- *herm(·) does not commute with inversion.* Exact witness computed:
  Q = [[1,1],[−1,1]] has herm(Q) = I so (herm Q)^{-1} = I, while
  herm(Q^{-1}) = ½I. The signing text only guarantees that the *Hermitian part*
  of the record-substituted action is positive definite; it does not say Q is
  Hermitian. A Gaussian field with kernel Q is only defined via herm(Q), whose
  covariance is (herm Q)^{-1} ≠ herm(Q^{-1}). So the sentence "a Gaussian field
  whose precision is Q and whose … marginals are herm(Q^{-1})" is true only under
  the extra hypothesis **Q Hermitian (real symmetric)**, which must be stated and
  checked against the fixture, not assumed.
- *third wording requirement.* The Bridge's W(S|config) is the normalised
  **diagonal** of that block (Σ_{a∈S}G[a,a] / Σ_b G[b,b], CM-SITE basis), i.e.
  normalised conditional-then-marginal variances — not the field's density and
  not a conditional law. And its carrier is the landed x-graded free-cell /
  CM-SITE alphabet, a different state space from T1/T2's finite Bloch menu, so
  the remark is a **cross-carrier analogy**, not an instance of T1 (which is
  proved for finite menus only). Required wording: *"On a real symmetric
  positive-definite quadratic fixture the same static/formation split has a
  Gaussian analogue: the pinned field's read-slice block of the inverse precision
  — the object the parked Bridge text calls W9 — is a static conditional-then-
  marginal covariance, not a formation-order conditional. Stated as an analogy on
  a different carrier; it neither explains nor bears on the 2026-08-26 measured
  gap, cited by path."* Also: the 5e-2..1.2e-1 sliding-frontier gap is a **float
  measurement on one fixture** and must be quoted as measured, never as evidence
  for T2.

**D4 (T1, the action is a gauge class, not a function).** μ ∝ Π_x ψ(v_x) Π_{xy}
φ(v_x,v_y) is invariant under φ(s,t) → φ(s,t)h(s)h(t), ψ(s) → ψ(s)h(s)^{−deg(x)}.
On a degree-regular graph (Z^3 is 6-regular) this is a genuine freedom with
site-independent ψ, so S_W = −Σlogψ − Σlogφ is unique only up to that gauge and an
additive constant; μ is unique, the *split* is not. Under covariance on a
transitive menu h is forced constant and only overall scale survives — but T1 is
stated for general positive rules, so the gauge clause belongs in the theorem.

**D5 (T2(a), silent hypotheses).** "on a transitive menu with isotropic φ the ONE-
neighbour normaliser is constant" needs ψ constant (true under covariance on a
transitive menu, but it is an added hypothesis) and needs W to be a **tree as an
induced subgraph** (otherwise no order with ≤1 recorded neighbour per site
exists). Both should be in the statement.

**Verified-correct steps** (I checked these; they are not defects):
- master identity μ_σ(v) = μ(v)Z_W/Π_kZ_k, and T2(d) Z_W = E_{μ_σ}[Π_kZ_k]:
  exact check on the plaquette, 6-Bloch menu, (p,q,r)=(2,3,5): Z_W = 391878 =
  E_{μ_σ}[Π Z_k] exactly.
- T2(b)'s normaliser lemma on the 6-Bloch menu: one-neighbour normaliser is the
  single value p+q+4r (constant, as claimed); two-neighbour normaliser takes
  exactly three values {p²+q²+4r², 2pq+4r², 2r(p+q+r)}, and sympy `solve` gives
  constancy **iff p=q=r**. Claim correct.
- T1's positivity witness: uniform law on the eight 4-cycle configurations
  {0000,1000,1100,1110,1111,0111,0011,0001} is Markov w.r.t. the 4-cycle (checked
  exhaustively on all configurations with positive denominator), and every edge
  value pair occurs in the support, so any edge factorisation would be strictly
  positive everywhere while the support has 8 of 16 configurations. The
  block's stated argument is sound.
- T2's headline on the plaquette: all 24 orders give μ_σ ≠ μ (exact rational
  arithmetic, defects between 2656/22141107 and 2354375/10007780364), and the 24
  orders realise exactly **4 distinct** formation laws — worth reporting, the
  order-dependence is coarser than the order set.

**Pre-run answers to two of the block's five attempted routes** (both come out in
the block's favour, and should be folded in as theorems rather than left as
"attempted"):
- *Absence-dependent extension φ_abs.* If the absence weight is direction-blind,
  φ_abs(s) is a function of s alone; covariance on the transitive 6-menu forces it
  constant, so it cancels in the normalised conditional and R-only is WLOG within
  that subfamily. If it is direction-dependent, α(s,u) with three orbit values
  (a,b,c): on the plaquette with order (1,2,3,4) the last-formed site has no
  absent W-neighbour, so its normaliser Z(v_1,v_3) carries no α, and constancy of
  μ_σ/μ forces Z(u,v) = λ·α₃(u)α₃(v). sympy `solve` over all 36 (u,v) pairs
  returns only **{a=b=c, p=r, q=r}** — i.e. the constant rule, forbidden by the
  variation clause. So no covariant absence extension rescues order-independence
  on the plaquette.
- *Averaging over all formation orders.* Uniform average over the 24 orders,
  exact rationals: max |avg_σ μ_σ − μ| = 1585133/10007780364 ≈ 1.58e-4, nonzero.
  The order-average is **not** the static law.

## 6. NEXT TEST — the single most decisive exact computation

**The covariant-order-average on the plaquette, promoted from "attempted route" to
a theorem, plus its no-privileged-site justification.** Reason: on Z^3 a fixed σ
is not an axiom-admissible object (Lattice: "No site is privileged"), so the only
formation law that survives literal reading is one averaged over a
translation-covariant law on orders. If that object equalled μ, the block's
headline would be an artifact of privileging a root and the whole result would
collapse to a statement about a supplied choice. It does not: I have already run
the uniform average exactly (defect 1585133/10007780364 ≠ 0 at (p,q,r)=(2,3,5)).
Include it as stated exact content, and extend it once — same computation with the
order drawn from i.i.d. site clocks (the natural translation-covariant order law,
which on a finite window with exchangeable clocks is again the uniform order
distribution, so the plaquette answer transfers) — so the note can say: *even the
order-averaged formation law differs from the static law*, which is the version
that survives the no-privileged-site clause and is the one the action-ID gate
actually needs.

## 7. RANKING vs. ALTERNATIVES (and the infinite-lattice gate)

On charge (4) first, since it drives the ranking: **the block does not address the
owner's gate.** The gate is "what the Admissibility rule induces on the infinite
lattice"; the block's own fence says finite windows only, no DLR claim. T1 gives a
free-boundary finite-window law, which is not the infinite-lattice object. To be
the action identification it would need, in order: (i) **T1 restated with boundary
conditions** — for every finite Λ and every ω on Λ^c, μ_Λ^ω ∝ Π_{x∈Λ}ψ · Π_{edges
meeting Λ}φ — which is what a specification is and is a small delta on the proof
already planned; (ii) the observation that a finite menu makes M^{Z^3} compact and
the specification quasilocal, so a DLR measure **exists**, while uniqueness fails
in general (phase transitions) — hence the induced infinite-lattice object is the
**specification / potential**, not a measure, and the honest action is the formal
H = −Σ_x logψ(v_x) − Σ_{⟨xy⟩}logφ(v_x,v_y) **up to the D4 gauge**; (iii) the T2
caveat carried into the infinite volume: on Z^3 no fixed order is admissible, and
the order-averaged formation object is not the Gibbs object, so this is the action
of the *static* reading only. Delivering (i)+(ii)+(iii) would make the block an
honest partial answer to the gate — an identification of the induced object
*conditional on the static reading*, with an explicit statement of what the
formation reading costs. Without them, its trace class `upstream_support` is right
and the note must not be read as firing wake condition 1 of DEFERRED_DECISIONS
entry 1 ("the committed-action identification lands"). I would say that in the
note in those words, citing the entry by path.

Ranking:
1. **This block, with the §5 changes and the §7 (i)-(iii) additions.** It is the
   only item on the list that touches the sequencing rule's gate, and it is the
   only place where the axioms' open "at which site" gate is shown to be
   load-bearing rather than cosmetic. Highest value even in its bounded form.
2. **(c) record-matter: derive a formation/renewal law from the carrier.** Direct
   complement — T2 says the order matters; (c) is the lane that would supply it.
   If (c) is near, do it in parallel; the two together are worth more than either.
3. **(b) U(1)/Maxwell time-selection fork at the linear level.** Concrete, live,
   and shares the "which schedule" structure with T2's σ; but it is downstream of
   a carrier the axioms do not supply.
4. **(a) gravity mainline queue.** Incremental, and the owner stopped the campaign
   after block 219 yesterday; measuring instruments, not the framework action.
5. **(d) verbatim exact re-proof of R136 as stated.** Low value on its own — it
   re-proves the static reading whose licensing is the very thing in dispute. It
   is worth including only as T1 *inside* this block, which is what the block
   already does.
6. **(e) my own alternative, ranked here for honesty:** a one-page axiom-reading
   note that fixes "nearest-neighbor conditions" — R-only vs. absence-as-condition
   vs. mean-field — as an owner question, with the three readings and their exact
   plaquette consequences (all computed above) as the decision material. It is
   cheaper than the block and it is *upstream* of it: T2's statement is
   premise-relative until it is answered. I would not rank it above the block,
   because the block can carry all three readings as named premises and still
   land — but if the owner wants one thing decided rather than one thing proved,
   this is it.

**Uncertainty declared.** I did not check the mean-field reading computationally;
I did not verify the general-window version of D1's missing lemma; and I have not
independently confirmed that the gravity fixture's Q is real symmetric (D3's
required hypothesis) — the signing text only asserts positive-definiteness of the
Hermitian part, which is weaker.
