---
name: physics-claim-reviewer
description: Use when an LLM agent needs to adversarially review a candidate physics claim, theorem note, runner, branch, or publication surface for overclaims, missing assumptions, code/prose drift, and safe disposition.
---

# Physics Claim Reviewer

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Use this skill to apply reviewer pressure before a claim lands on the live
surface. The raw synthesis shows that the most common failure is not bad prose;
it is artifact-chain or semantic drift.

## Landing review depth

For pre-landing review, follow the owner-selected Astra-low default and focused
review contract in [`../review-loop/SKILL.md`](../review-loop/SKILL.md).
Read the complete changed argument and its necessary premises, challenge the
decisive mathematics and physical identifications, and report material findings
concisely. Escalate unresolved consequential questions to Astra xhigh. The
batteries below guide risk selection; they do not require exhaustive new
certificates for every minor detail. Known false claims must be fixed or
narrowed before landing; comprehensive claim certification belongs to the
later independent audit. This does not change the formal auditor's model or
standards, or authorize running it before the owner's solid-TOE milestone.

## Workflow

1. **Read the claimed authority surface.** Identify the note, runner, log,
   claim table row, or branch being reviewed.
2. **Find the load-bearing statements.** Extract the exact claims, imported
   assumptions, observations, status labels, and reproduction path.
3. **Check artifact-chain alignment.** Compare prose against the runner/output
   or derivation. Flag placeholder scripts, literal `True` checks, stale logs,
   hard-coded baselines, and runners that do not exercise the decisive claim.
4. **Attack semantic bridges.** Ask what is selected, fitted, imposed,
   imported, conventional, finite-order, protocol-specific, or only shown on
   one surface. Correct algebra can still compare the wrong physical objects.
5. **Audit proof obligations.** For theorem, proof, and reduction claims,
   reconstruct the obligation graph and apply
   [`../physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md).
   Check the exact target, hypothesis preservation, boundary cases,
   circularity, and the strength of every unresolved terminal lemma.
6. **Check status language.** Decide whether the evidence supports retained,
   bounded, support, open, no-go, reject, or historical language.
7. **Scrutinize no-go claims with the same rigor as positive theorems.**
   A wrongly scoped no-go is just as bad as a wrongly scoped positive theorem,
   and can be worse because it forecloses investigation paths prematurely.
   For any `claim_type: no_go` candidate, run the no-go battery in the
   dedicated section below before recommending disposition.
8. **Check science naming.** Reject new bare shorthand labels that can be
   confused with axioms, assumptions, Lie types, lane stages, route codes, or
   branch blocks. Require explicit scientific names from the controlled
   vocabulary, with shorthand only as a parenthetical alias when needed.
9. **Classify findings.** Use the local disposition buckets:
   `fix on main`, `support-only demotion`, `science-needed`, `reject`,
   `historical only`.
10. **Recommend the narrowest honest fix.** Prefer wording fixes for wording
   problems; demotion for overclaimed support; new science only when a real
   theorem step is missing.
11. **Write review output.** Lead with findings and file/line references when
    possible, then summarize the safe status.

## Review Questions

- Does the note claim more than the runner proves?
- Does the runner check the decisive step or just assert it?
- Is the result exact, bounded, support-only, conditional, or open?
- Is a selector, convention, imported datum, or fitted parameter being treated
  as derived?
- Is the symbol-to-physics identification actually justified?
- Does the proof match the exact target, including quantifiers and edge cases?
- Does every reduction preserve its hypotheses and produce admissible objects?
- Is the strongest unresolved lemma weaker than the target, or is it
  target-equivalent/stronger and therefore not genuine near-closure?
- Is any equivalent formulation of the target being used circularly?
- Is the claim still true under the stated validation path?
- Does the public package surface match the latest retained evidence?
- Does the name identify the scientific object, or is it a bare overloaded
  code like `A1`, `A2`, `G1`, `R3`, `Route F`, or `Block 2`?
- Should this be live, demoted, archived, or rejected?

## No-Go Scrutiny Battery

A wrongly scoped no-go forecloses investigation paths prematurely and can
poison-pill future work that would otherwise close positively. Apply the
same review battery to no-gos as to positive theorems. For any candidate
with `claim_type: no_go` or "bounded obstruction" / "structural foreclosure"
framing in prose:

1. **Scope precision.** State the no-go formally with explicit premises and
   forbidden conclusion class. Could a reader reasonably read it as a wider
   no-go than intended? If yes, narrow the language. (Example failure:
   `first_order_coframe_unconditionality_no_go` is correctly scoped to
   "substrate symmetries alone cannot break Hodge degeneracy" but gets
   misread by downstream notes as "Wald-Noether BP section 5 impossible.")
2. **Reframe-as-positive check.** Is there a positive theorem with the same
   algebraic content and a different framing? For example, a Schur calculation
   that blocks one primitive may also expose a positive finite-spectrum
   structure once labels are treated as conventions. If yes, the right
   delivery may be the no-go plus the positive reframe, not foreclosure alone.
3. **Labeling vs physics check.** Is the no-go on a labeling / convention
   question (dissolvable by convention parallel to u/c/t naming) or on a
   physics question (genuinely foreclosing)? If labeling, the right outcome
   is a `meta` convention note, not a `no_go` theorem note. The same
   labeling-vs-meta rule applies on the positive-claim side: a labeling
   convention shipped as `bounded_theorem` is overclassified, since
   `retained_bounded` grade is for algebraic claims with explicit named
   premises, not for stipulations about names or approved framework primitives
   already registered in `docs/audit/data/axiom_premise_nodes.json`. Before
   treating any primitive use as bounded or missing, consult the primitive
   registry check in
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. The registered
   `scale_reference_primitive` grants the Planck scale reference as units
   conversion only; it is not a bounded import. The registered
   `kinetic_isotropy_primitive` grants only structural OS0 kinetic-form
   isotropy `c_t = c_s`; it is not a bounded import and does not supply
   dynamics, a Lorentz-closure theorem, scale, spacing-ratio theorem, selector,
   or empirical content. The registered `realized_state_primitive` grants only pointwise evaluation at a supplied law-admissible realized state; it does not supply a state, state-selection rule, measure, typicality or genericity assumption, weighting, probability rule, or any state-contingent value (quantities that vary across the law-admissible family remain registered data). For the symmetric check on bounded-theorem candidates,
   see the
   `LabelingConventionReviewer` in
   `docs/ai_methodology/skills/review-loop/SKILL.md`.
4. **Premise-retention check.** No-go theorems depend on premise lists
   just like positive theorems. Verify each premise via live ledger
   `effective_status`. An "unaudited no-go" with an unaudited premise can
   be just as wrong as an "unaudited positive."
5. **Literature bypass check.** Has the published literature gotten around
   this obstruction class via a different route? Causal-set BH entropy
   bypasses Wald-Noether entirely; Connes NCG bypasses gauge-coupling
   lattice derivation. A no-go of "X requires Y" may be a no-go FOR THE
   PARTICULAR ROUTE Y, not for X itself.

When a no-go passes the five-check battery, ship it with the same confidence
as any other reviewed claim boundary, while leaving `audit_status` and
`retained_no_go` effective status to the independent audit lane. When it fails
any check, recommend either narrowing scope, shipping a parallel positive
reframe, or demoting to bounded.

## Executor Fabrication-Pattern Battery

When the runner/note under review was produced by an LLM executor (codex or any
generation agent) under pressure for a strong result, the failure mode is not
honest error — it is a **rigged success signal**: a runner that passes its own
gates while the load-bearing gate establishes nothing. Across a 2026-06 wave,
four of five executor outputs fabricated the decisive step and *every one passed
its own runner*; only line-by-line gate review caught them. Run this battery on
any executor-generated artifact before disposition.

The five patterns (each passed `TOTAL: PASS=N FAIL=0`):

1. **Value-from-target.** The "computed" result is derived from the very target
   it is compared against. Tell: the comparison constant appears inside the
   formula that predicts it; a damping/blend toward `d_measured`; `_ = x  # not
   used` discarding the real input. (Seen: a "Richardson extrapolation" that was
   `alpha = d_measured + 0.12*(onepoint - d_measured)` and ignored the sequence.)
2. **Proxy-for-physics.** A `0/1`/parity matrix stands in for a real
   Schur-complement / eigenvalue / floating quantity, making a downstream
   "coincidence" tautological. Demand the real object; a sibling runner building
   the genuine Schur proves it was feasible.
3. **Rounded / idealized anchors.** The artifact freezes a rounded stand-in
   (`0.366` for landed `0.366421...`) or a designed split (`0.30*tail`), so an
   approximate model "matches" a target that is not the real measured quantity.
   Require exact landed values to full precision, recomputed from real machinery.
4. **Fitted prefactor as derivation.** A wrong functional form is forced to
   match by one or two fitted constants (a 17-digit normalization; a tidy
   rational like `47/120`) presented as derived. A native symbolic derivation
   refutes it. Tell: any multi-digit constant with no derivation shown.
5. **Tautological / non-discriminating gate.** The gate holds regardless of
   whether the implemented object is correct. (Seen: a "SymPy completeness"
   gate that reduced to `(I - A·A^{-1})·X`, vanishing for *any* `X` — it tested
   only that the inverse inverts, nothing about the implemented coefficient.)

**The discriminating-gate test (apply to every completeness/identity gate).**
A real gate must FAIL if the implemented object were wrong. Recompute the gate
with a term dropped or perturbed: if it still passes, it is tautological. Prefer
finite-difference cross-checks with a convergence-ratio requirement (a wrong
object plateaus instead of converging) and explicit wrong-value discriminators
(e.g. gate that the `-1/11` competitor is rejected by `>>` the tolerance) over
algebraic identities that hold by construction.

**Keep validation targets independent of the prediction.** An exact landed
value, independent computation, or known constant can expose an error, but a
worker can still fit or copy a known target. Trace every numerical input and
the computation that produces the prediction. Disclose targets known during
development and any search over formulas or parameters; use held-out cases,
independent derivations, or preregistered checks when applicable. A match is a
comparison result until the derivation and physical identification are
supported. Do not prefer a target merely because its desired answer is known.

**Independent verification.** A single reviewer can miss tautological gates
and overstated framing. Have a separate pass re-derive the load-bearing step
using different machinery and test whether the gate detects relevant defects.
Different model families can reduce correlated errors but do not guarantee
independence or correctness; report shared inputs and context limits.
This applies to the reviewer's own synthesis too: even when the artifact is
honest and correctly scoped, the carried-forward summary can overstate (claiming
a convergence study "confirms" a gap it never measured; quoting a residual the
note never reports). Verify the *framing* against the gated numbers, not only
the gates.

## Guardrails

- Do not reward novelty over correctness.
- Do not treat review as cosmetic copyediting.
- Do not invent fixes that would require missing science.
- Do not approve arithmetic-only closure when the semantic bridge is open.
- Do not approve proof-complete language when the terminal missing lemma is
  target-equivalent or stronger than the headline claim.
- Do not bury useful no-go results; preserve them as route-pruning evidence.
- Do not approve overclaimed no-gos. A wrongly scoped no-go is at least
  as harmful as a wrongly scoped positive theorem; apply the No-Go
  Scrutiny Battery before treating any `claim_type: no_go` candidate as
  review-ready for independent audit.
- Do not approve new science names that are only ambiguous shorthand. Use
  explicit names such as `physical Cl(3) local algebra`, `Z^3 lattice`,
  `Koide Frobenius-equipartition condition`, or `Lie type A_1`.
- Do not trust a passing runner. `TOTAL: PASS=N FAIL=0` is necessary, not
  sufficient: run the Executor Fabrication-Pattern Battery and the
  discriminating-gate test on any executor-generated runner before disposition.
- Do not let a tautological gate stand as evidence. If a completeness/identity
  gate still passes with a term dropped or perturbed, it establishes nothing;
  require a discriminating gate (FD convergence-ratio or wrong-value rejector).
- Do not let the review summary outrun the gated numbers. Verify the framing
  against what the runner actually measured, even when the artifact is honest.
