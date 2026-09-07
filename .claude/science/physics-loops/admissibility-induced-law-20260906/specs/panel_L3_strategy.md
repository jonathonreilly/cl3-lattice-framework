# L3 (research-program strategy) — verdict on "What the nearest-neighbor rule induces on a finite window"

Read: full axioms file `docs/MINIMAL_AXIOMS_2026-06-29.md` (complete, not truncated);
`docs/ai_methodology/skills/physics-loop/SKILL.md` lines 846-851 (V1-V5);
`docs/repo/DEFERRED_DECISIONS.md` lines 21-49 (parked bridge + wake conditions);
`docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md` (complete).

## 1. VERDICT

**Build with changes — and the changes are large: cut T1, keep T2.** T1 is not new.
The repository already carries, front-of-house on `main`, the static half of T1 for the
binary alphabet: `docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`
proves compatible-positive-joint-law ⟺ zero square curl (that is Brook's ratio
consistency, unnamed), uniqueness, path reconstruction, the nearest-neighbour reduction
to adjacent pairs, the cubic count classification, and the derived finite-volume
nearest-neighbour action `S_Λ`. T1 is that theorem with `{0,1}` replaced by a six-value
menu and square-curl replaced by Hammersley–Clifford — a textbook route to a result the
repo already has. T2 is the only part that is genuinely new and the only part that
changes a claim state: it names, as an exact finite theorem, the distinction the
supervisor identified in R136 step (ii). The block should be **one note whose subject is
T2**, with T1 demoted to a half-page corollary that cites the 2026-08-10 note as the
binary case and states only the menu generalization, and with T3's gravity remark either
deleted or given an explicit Hermiticity premise (defect D5 below). The note must not be
sold as moving the parked statistical-bridge decision; it does not.

## 2. STRONGEST ARGUMENT (from the program-strategy lens)

The program's scarcest resource is **claim states that actually move**, and the only
mechanism in this block that moves one is T2. R136 is an archived, never-refereed
positive result whose headline ("Record consistency fixes the FORM of the admissibility
rule") is currently load-free but is the kind of sentence that gets cited later as if it
were retained. T2 converts the supervisor's prose objection into an exact object: the
formation law `μ_σ` exists for any rule, is computable, and is provably different from
the static law `μ` on the smallest window that occurs in `Z^3` (the plaquette). That
retires R136's step (ii) from "reading" to "false under the records-only premise", and
it does so with arithmetic small enough to certify exhaustively in one session. Cost is
one note; the payoff is that a future adoption argument cannot silently import the static
reading. Nothing else on the alternatives list produces a comparable premise-level
correction for the same cost.

The second-order strategic point: T2 makes **formation order a physical variable**, which
is the supply-side question the record-matter lane (alternative (c)) is already meant to
answer. Landing T2 first gives (c) a target it does not currently have — it turns "derive
a formation/renewal law" from an open-ended request into "supply the object `σ` that T2
proves the answer depends on."

## 3. STEELMAN AGAINST MY VERDICT

The honest case for "do not build": the entire block is standard statistical mechanics
wearing repo clothing. T1 is Brook (1964) + Hammersley–Clifford (1971) + Besag (1974).
T2's central identity `μ_σ(v) = μ(v) · Z_W / Π_k Z_k(v_{A_k})` is one line of chain-rule
bookkeeping — the same algebra that defines pseudo-likelihood — and T2(d)
(`Z_W = E_{μ_σ}[Π_k Z_k]`) is that identity summed against `μ_σ`, i.e. a restatement, not
a result. The observation "a sequential/chain-rule construction is not the Gibbs measure"
is textbook. On that reading the block spends a session to write down that a Gibbs
sampler run once in a fixed order does not sample its own equilibrium law, and dresses it
as a framework theorem. Under V4 that is exactly the failure mode the gate exists to
catch. The counter is narrow but real: the *specific* statement — for the declared
covariant menu, **every** order on **any** window containing a 4-cycle gives `μ_σ ≠ μ`,
and the exceptional orders are exactly the forest sweeps — is a classification, not an
identity, and I could not find it in any textbook framing or in this repo. But the block
must be written so that this classification, not the identity, is the headline; if it is
written as proposed (three theorems, T1 first), the steelman wins.

## 4. WHAT EVIDENCE WOULD CHANGE MY MIND

- A landed or archived note that already compares an order-dependent formation law with a
  static law on a declared window. I searched and found none (receipts in §5, D0). One
  hit would collapse the block to zero.
- A proof or exhaustive certificate that some records-only-compatible extension (an
  absence factor `φ_abs`, or marginalizing over unrecorded neighbours rather than dropping
  the factor) makes `μ_σ = μ` for some order on the plaquette. That would make T2's
  headline premise-dependent and reduce it to "under one reading of *only records are
  readable*", which is the same category of defect T2 accuses R136 of.
- A counterexample window+order where `Π_k Z_k` is constant while individual `Z_k` are
  not. That would falsify T2(b)'s general-window statement (see D2) and force it back to
  the declared windows.
- Owner statement that the R136 static reading is not going to be cited by any live lane.
  Then T2's consumer disappears and (b) or (c) outrank it.

## 5. CONCRETE DEFECTS

**D0 — the dossier's duplication claim is half wrong; T1 is duplicated.**
Read-only greps under `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/sync-science-task-0c8fac/docs`:

| term | hits | disposition |
|---|---|---|
| `Brook` | 0 | absent |
| `Hammersley` | 0 | absent |
| `sequential law` | 0 | absent |
| `Markov random field`, `Besag`, `pseudo-likelihood`, `conditional specification`, `pair potential`, `sliding frontier`, `normaliser history` | 0 each | absent |
| `formation order` | 1 | `docs/work_history/repo/review_feedback/LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md:505` — counting cut transcripts, not a law. Not prior art. |
| `growth law` | 4 | `docs/PHYSICAL_AMBIENT_DOMAIN_SYMMETRY_SPLIT_CYCLE720_NOTE_2026-08-02.md`, ledger rows `adaptive_coevolving_geometry_no_go`, `growing_graph_frontier_expansion_proxy_note` (`claim_type: bounded_theorem`, `audit_status: unaudited`, `claim_scope: null`), `record_conditional_law_period_scaling_l3_to_l4_...`. None compares a formation-ordered law to a static law. Not prior art. |
| `Gibbs` | 410 | Gibbs states / KMS / Tomita / Wilson-staggered contexts. Sampled the nearest-looking (`OBSERVABLE_PRINCIPLE_P1_BRIDGE_TOMITA_GIBBS_MODULAR_...`); none is the conditional-specification theorem. Not prior art for T2. |

So T2 is clean. **T1 is not.** `grep -l "full conditional"` returned
`docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`,
`claim_id: admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_bounded_theorem_note_2026-08-10`,
`claim_type: bounded_theorem`, ledger `audit_status: unaudited` / `effective_status_reason: awaiting_audit`,
`load_bearing_score: 4.085`. Its `claim_scope` front matter reads, verbatim in part:
"a positive joint law exists exactly when the conditional-odds one-form has zero
multiplicative curl on every two-site configuration square; the joint law is then unique
and recovered by path integration ... equivalent to geometric odds, hence an affine logit
and a finite-volume nearest-neighbor Ising-type action." That is T1's `(⇒)` criterion,
uniqueness, and induced action. The dossier's sentence "no front-of-house note mentions
formation order, Brook's lemma, or a growth/sequential law" is literally true about the
*names* and false about the *mathematics*. Also adjacent and worth citing rather than
re-deriving: `docs/EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md` (an
append-only cellular relation with an exhaustive 3^8 = 6561 witness — the closest existing
object to a formation process) and
`docs/ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md`
(partial configurations, extension cones, "one-record append schedule").

**D1 — T2(b)'s inference is invalid as written. This is the load-bearing defect.**
The block argues: the two-neighbour normaliser `Z(b,c)` is non-constant ⟹ `μ_σ ≠ μ`.
That does not follow. From the block's own identity, `μ_σ = μ` iff
`Π_k Z_k(v_{A_k})` is constant in `v` — a condition on the **product**, not on each
factor. Cancellation between the normalisers of different sites is not excluded by a
two-neighbour computation. Writing `Σ_k log Z_k` and taking its Möbius/ANOVA expansion,
the coefficient on a pair `{b,c}` collects one contribution from **every** `k` with
`{b,c} ⊆ A_k`, and those contributions differ when the `A_k` differ; their sum vanishing
is not a priori impossible. The missing lemma is exactly: *`Π_k Z_k` constant ⟹ every
`|A_k| ≤ 1`.* Until it is proved, T2(b)'s general-window sentence is a conjecture with
exhaustive support on the declared windows.

*What I ran* — two independent passes, six-projector menu, `ψ ≡ 1`: **(i) symbolic**
(`sympy`, `p,q,r` free positive symbols) and **(ii) exact rational**
(`fractions.Fraction`, fixture `p = 5/7, q = 2/3, r = 1/4`). Both passes agree on every
shared quantity.
- `Z_0 = 6`; one-neighbour `Z_1 = p + q + 4r` (`= 50/21`), constant in the neighbour's
  value — **T2(a) confirmed symbolically**.
- `Z_par = p² + q² + 4r²`, `Z_anti = 2pq + 4r²`, `Z_orth = 2r(p+q) + 2r²`
  (`= 2125/1764, 101/84, 137/168`). Symbolically
  `Z_par − Z_anti = (p−q)²` and `Z_par − Z_orth = (p−r)² + (q−r)²`, so over the whole
  parameter space `Z(b,c)` is constant ⟺ `p = q = r`. **T2(b)'s normaliser computation
  confirmed** on this menu with constant `ψ` — not merely at a fixture.
- Exhaustive over all orders, checking whether `Π_k Z_k` is constant over all `6^{|W|}`
  configurations: **3-path 4 of 6 orders constant; 4-star 12 of 24; 4-cycle 0 of 24**
  (3-path and 4-cycle counts reproduced identically in the symbolic pass); open 2×2×2 cube
  (8 sites, 12 edges) **0 of 40320 orders** (constancy refuted on 6 random exact
  configurations per order, early exit).
- Direct law comparison on the 4-cycle: orders `(0,1,2,3)` and `(0,2,1,3)` give laws
  differing on **1296 of 1296** configurations (e.g. all-parallel: `27/4250` vs `36/7225`);
  `μ_σ` vs static `μ` differ on **1296 of 1296**. **T2(c) confirmed on the plaquette.**
- Pattern across all four windows: `Π_k Z_k` is constant exactly when **every site forms
  with at most one already-recorded neighbour** — i.e. the formation order's
  recorded-predecessor graph is a forest. This is a cleaner and *positive* statement of
  T2(a)+(b) and should replace them as the headline (see §6).

**D2 — T2(b)'s "which Admissibility forbids" is a reading step, of the same kind the
block criticizes in R136.** The chain `Z` constant ⟹ `p = q = r` ⟹ "the rule does not
vary with its neighbours" ⟹ forbidden, uses an extensional reading of the axiom sentence
"the probability distribution over the possibilities is determined by, and varies with,
the nearest-neighbor conditions." Whether `p = q = r` violates *varies with* is a question
about the axiom text, not a theorem. The note must quote the sentence and declare the
extensional reading as a named premise, or the block repeats R136's error while
diagnosing it. Also note that `p = q = r` is a statement about the pair weight, not
directly about the rule: within class (P) with constant `ψ`, `p = q = r` does make the
conditional uniform, but that identification is the declared-menu computation, not a
general fact — state it as such.

**D3 — the records-only premise is under-enumerated.** "An unrecorded neighbour
contributes no factor" is one of at least three readings of *only records are readable*.
The block lists absence-dependent factors `φ_abs` as an attempted route but omits the most
natural competitor: **conditioning on the pattern of absence while marginalizing the
unrecorded neighbour's later value**. Under Record the unrecorded site *has no value*, so
marginalization is arguably illegitimate — but that argument must be written, not assumed.
Add it to the N1 enumeration; five routes is the floor, not the target.

**D4 — T3's gravity remark is probably wrong as stated, and it is the only place the
block touches the parked bridge.** "A quadratic pair weight is a Gaussian Markov field
whose precision is `Q` and whose pinned-record conditional marginals are
`herm(Q_sub^{-1})`" conflates two objects. For a Gaussian field with precision `Q`, the
conditional covariance of a set `A` given the rest is `(Q_AA)^{-1}` — the inverse of a
principal **submatrix of the precision** — not a submatrix of `Q^{-1}`, and `herm(·)` is
meaningful only if `Q` is not Hermitian, in which case "Gaussian field with precision `Q`"
is undefined. The repo's `W9 = herm(Q^{-1})` (per the gravity lane's generator-kernel
result) is a different object. Either delete this remark or state Hermiticity of the
gravity lane's `Q` as an explicit premise and check it. As written it invites exactly the
mis-citation the parked decision is parked to avoid.

**D5 — T1's positivity witness sits outside T1's own hypothesis.** The 4-cycle
eight-configuration Markov law is the classical Hammersley–Clifford positivity
counterexample; T1 is stated for *positive* rules, so this witness illustrates the scope
fence rather than proving a step. Fine to include, label it as a scope illustration.

**D6 — the block cannot claim to move the parked bridge, and should say so.**
`docs/repo/DEFERRED_DECISIONS.md` §1 wake condition 1 is "The committed-action
identification lands (the owner's standing action-ID-before-Bridge sequencing rule)."
The owner's rule asks for what the rule induces **on the infinite lattice**; T1 delivers a
finite-window action for a rule class that is declared, not selected, and the block
explicitly disclaims DLR existence and rule selection. Wake condition 4 ("a lane produces
science it cannot state conditionally") is likewise not fired — everything here is
conditional on a declared rule class and a named records-only premise. Expected movement
on the parked decision: **zero**. Write that in the note; a claimed wake would be an
overclaim the audit lane will catch.

## V1-V5, in writing

- **V1 (which verdict-identified obstruction does this close?) — FAILS as a closure route,
  passes as `frontier_discovery`.** V1 demands the exact obstruction text quoted from a
  parent row's `verdict_rationale`. The block's declared consumers are a *parked owner
  decision's wake condition* and an *archived campaign's* claim; neither is a
  `verdict_rationale`. The nearest parent row
  (`admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_...`)
  is `unaudited`, so no `verdict_rationale` exists to quote. The skill's own escape applies:
  "A `frontier_discovery` route satisfies this gate only if it introduces a genuinely new
  structure, falsifier, or hard-premise test; it must not be sold as closure." T2 is a
  falsifier (it falsifies R136 step (ii) under a named premise) and a hard-premise test
  (records-only). T1 is neither. So: declare `trace_class: frontier_discovery`, claim
  falsifier, claim no closure.
- **V2 (new derivation + the search that establishes it) — T1 FAILS, T2 PASSES.** T1's
  content is on `main` in binary form since 2026-08-10 (D0). T2 passes with the grep table
  above quoted verbatim into the note, including the negative-hit list and the classified
  near-misses.
- **V3 (could the audit lane already do this from retained primitives + standard
  machinery?) — T1: yes, so it must not be opened.** Brook + Hammersley–Clifford on a
  triangle-free graph is standard machinery in the gate's own sense. T2: the identity is
  also standard machinery; the *classification* (which orders reproduce the static law) is
  not, because it needs the covariant menu's three-orbit structure and the missing lemma
  D1. The note must be built around the part that answers "no" here, i.e. the
  classification, and must not pad with the part that answers "yes".
- **V4 (marginal content non-trivial, not a textbook identity) — MIXED, and one sub-item
  fails outright.** T1: **FAIL** — textbook identity, and additionally restated in-repo.
  T2(d) `Z_W = E_{μ_σ}[Π_k Z_k]`: **FAIL** — it is the defining identity summed against
  `μ_σ` (`Σ_v μ_σ Π Z_k = Σ_v μ Z_W = Z_W`), one line, in the gate's "scaling by mu
  preserves slope" class. Delete it or demote it to a remark. T2(a),(b),(c) and the forest
  classification: **PASS** — the three-orbit normaliser computation and the every-order
  statement are not identities and were not obtainable without the declared menu. Blunt
  summary: roughly half the proposed block is a textbook restatement, and the note must be
  cut to the half that is not.
- **V5 (one-step variant of anything landed, on `origin/main` included) — T1 FAILS, T2
  PASSES.** T1 is a one-step alphabet generalization of the landed 2026-08-10 binary note;
  the gate's own language — "a more general landed version outranks your special case" —
  cuts here in the mirrored form: the landed version is the special case, and going from
  `{0,1}` to six menu values on a triangle-free graph is the same proof with a bigger
  index set. "Same structure, different alphabet" is relabeling. T2 has no closest prior
  cycle: nothing landed compares a formation-ordered law with a static law, and the
  structural distinction (two distinct measures on the same configuration space induced by
  the same rule) is not a relabeling of anything on `main`.

**Net gate reading:** as proposed, the block **fails V2/V3/V4/V5 on T1** and passes on T2.
A T2-only note with T1 cited rather than re-proved passes all five, with V1 answered as
`frontier_discovery`/falsifier and never as closure.

## 6. NEXT TEST (single most decisive exact computation)

**Decide the D1 lemma by exhaustive search, and reframe the result as a positive
classification.** Concretely: over every connected triangle-free graph on ≤ 6 vertices
(and the two named 3-D windows) and every formation order, compute `Π_k Z_k` exactly on
the six-projector menu and test whether *`Π_k Z_k` constant ⟺ every `|A_k| ≤ 1`*. My runs
already give one direction and four data points for the other (3-path 4/6, 4-star 12/24,
4-cycle 0/24, 2×2×2 cube 0/40320, all matching the forest criterion). If no cross-site
cancellation exists anywhere in that class, the note lands the theorem

> `μ_σ = μ` **iff** every site forms with at most one already-recorded neighbour — i.e.
> iff the order's recorded-predecessor graph is a forest — hence never on any window
> containing a 4-cycle, hence never on any window of `Z^3` containing a plaquette,

which is a positive classification rather than a negative claim, does not have to pass the
N1-N8 no-go gate at all, and is strictly stronger than T2(a)+(b)+(c) combined. If a
cancellation *is* found, T2(b) is false in general and the block must narrow to the
declared windows — either way this is the computation that decides whether there is a
theorem. Second priority, and the falsifier the note must run: the plaquette test for an
absence-dependent extension `φ_abs` (and the marginalization reading of D3) that makes
some order coincide with the static law.

## 7. RANKING against alternatives (a)-(e)

1. **(e)-as-modified: the T2-only note with the forest classification as its headline** —
   the only item that changes a claim state (retires R136 step (ii)), one session of exact
   arithmetic, no duplication, passes V1-V5 as `frontier_discovery`.
2. **The block as proposed (T1+T2+T3)** — same payload, but T1 duplicates a landed note and
   fails V2/V4/V5, and T3's gravity remark is likely wrong (D4); build only if cut.
3. **(c) record-matter: derive a formation/renewal law from the carrier** — attacks the
   same gap from the supply side and is what T2 makes necessary; higher long-run value,
   but it is not a one-session exact-arithmetic item and has no bounded target until T2
   lands.
4. **(b) U(1)/Maxwell time-selection fork at the linear level** — live, concrete, exact,
   independent of this argument; the right fallback if the panel rejects T2.
5. **(a) gravity mainline queue** — the owner stopped that campaign after block 219
   yesterday; incremental certification work with no claim-state movement.
6. **(d) verbatim exact re-proof of R136 under the static reading** — **do not build.** It
   re-derives what `docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`
   already carries and re-lands the exact reading the panel convened to expose. Fails V2,
   V4 and V5 outright.

## Uncertainties I could not close in the time budget

- I did not prove the D1 lemma; my evidence is exhaustive on four small windows only, and
  the 2×2×2 cube pass used 6 random exact configurations per order rather than all `6^8`.
  The 4-star and cube passes were run at the rational fixture only, not symbolically, so a
  measure-zero coincidence in `(p,q,r)` is not excluded for those two windows (it is
  excluded for the 3-path and 4-cycle, which ran symbolically).
- I sampled, not read, the 410 `Gibbs` hits; a conditional-specification theorem hiding in
  one of them would strengthen D0 further against T1 but I found none in the nearest ten.
- I did not verify whether the gravity lane's `Q` is Hermitian; D4 is stated as a defect in
  the remark's *derivation*, which holds regardless, not as a claim that `Q` is non-Hermitian.
- Scratch scripts used for the exact runs are at
  `…/scratchpad/t2fast.py` and `…/scratchpad/cube.py`; no repository file was modified.
