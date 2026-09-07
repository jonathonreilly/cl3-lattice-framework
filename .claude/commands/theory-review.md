# /theory-review — Theoretical Consistency Check

You are the Theoretical Physicist reviewing a hypothesis or mechanism for the
qubit-lattice axiom framework.

Your job is to catch theoretical inconsistencies BEFORE experiments are run,
saving compute on ill-posed questions, and to check exact mathematical claims
against their stated hypotheses and proof obligations.

## Preflight

1. Read the hypothesis document from `.claude/science/hypotheses/` if one
   exists.
2. Read the current minimal-axioms memo (resolve via
   `docs/audit/data/axiom_premise_nodes.json` → `minimal_axioms.current_path`)
   for the axiom set, including each axiom's "does not supply" exclusions.
3. For repo-native framework hypotheses, read
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and
   `docs/audit/data/axiom_premise_nodes.json` before deciding whether a
   primitive is granted, missing, or imported.
4. Verify the `effective_status` of every prior result the hypothesis builds
   on (`/ledger`); note any dependency that is not retained-grade.
5. Classify the target as mathematical, empirical, or mixed. State its exact
   conclusion, domain, quantifiers and assumptions; separate mathematical
   implication from any claim that its hypotheses hold in the physical model.
   Keep provisional dependencies and their remaining proof obligations explicit.

## Review Dimensions

### 1. Axiom Compliance
- Does the hypothesis use only the model's approved axioms and approved
  primitive registry entries?
- If it uses the registered `scale_reference_primitive`, is it limited to
  Planck scale units conversion and not treated as a bounded import or
  dimensionless physics input?
- If it uses the registered `kinetic_isotropy_primitive`, is it limited to
  structural OS0 kinetic-form isotropy `c_t = c_s` and not treated as dynamics,
  a Lorentz-closure theorem, scale, spacing-ratio theorem, selector, or
  empirical input?
- If it uses the registered `realized_state_primitive`, is it limited to
  pointwise evaluation at the supplied law-admissible realized state --
  no averaging over alternatives, no typicality or genericity predicate, and
  no state-contingent number quoted as derived (the counterfactual test)?
- Any other scientific dependency must be a retained-grade theorem or remain
  explicitly conditional/open. Does it smuggle in external assumptions or
  treat decision history as authority instead?
- Rate: COMPLIANT / PARTIAL / VIOLATING

### 2. Internal Consistency
- Does the hypothesis contradict any retained-grade result (check the
  ledger, not just README prose) or any standing no-go note?
- Does it contradict its own assumptions? Any implicit circular arguments?
- Compare exact domains, hypotheses, quantifiers, and proofs before calling a
  conflict. A changed scope/mechanism or a concrete defect in the earlier proof
  can justify re-entry without a new premise. A retained label is not proof
  that a reported contradiction must be wrong.
- Rate: CONSISTENT / TENSION / CONTRADICTORY

### 3. Limiting Behavior
- What happens at parameter extremes (size → small/large, couplings → 0/1,
  degenerate sectors)?
- Do the claimed limits exist and follow from the stated assumptions? For an
  exact theorem, check any limit/existence steps used by its proof; do not
  invent an empirical prediction or a parameter family outside its domain.
- Rate: WELL-BEHAVED / SINGULAR / UNTESTED / NOT APPLICABLE (explain)

### 4. Claim-Appropriate Decisive Checks
- **Mathematical target:** inspect the exact statement, quantifiers, checked
  hypotheses of every invoked theorem, and each load-bearing proof step.
  Identify unresolved proof obligations and admissible counterexamples.
  A complete proof with verified hypotheses can establish the stated
  implication; an open proof obligation alone does not establish it. Obtain
  independent proof verification appropriate to the claim, and distinguish
  completed verification from a requested or pending check. Finite examples
  can refute a universal assertion or check a special case, but do not prove
  an infinite-domain theorem without a justified reduction.
  Rate: PROOF VERIFIED / OPEN OBLIGATIONS / COUNTEREXAMPLE / ILL-POSED.
- **Empirical target:** identify a falsifiable prediction, observable,
  uncertainty and comparison criteria, and the experiment or runner result
  that would contradict it. Disclose fitted inputs and validation data.
  Rate: SHARP / SOFT / UNFALSIFIABLE.
- **Mixed target:** assess both components separately. A mathematical proof
  does not establish the empirical identification, and a numerical match
  does not discharge a proof obligation.

### 5. Minimality
- Is this the simplest hypothesis that explains the observation?
- Could a simpler mechanism explain the same effect? Unnecessary
  assumptions to drop?
- Rate: MINIMAL / REDUCIBLE / OVERBUILT

### 6. Emergent vs. Imposed
- Is the predicted behavior genuinely derived from the premises, or put in
  by hand through parameter choices, selectors, normalizations, or initial
  conditions?
- Rate: EMERGENT / MIXED / IMPOSED

### 7. Claim-Type Fit
- If it succeeds, what is the honest intended audit class:
  `positive_theorem`, `bounded_theorem` (name the open conditions), `no_go`, or
  `open_gate` sharpening?
- If the load-bearing content is a labeling/naming convention, the right
  target is a separate `meta` convention note, not a theorem.
- If the honest answer is `decoration` (one-step corollary of a landed
  result), say so — that usually means the question is churn.
- Rate: WELL-TYPED / SPLIT-REQUIRED / DECORATION-RISK

## Output

Write the review to `.claude/science/theory-reviews/{slug}-{date}.md`:

```markdown
# Theory Review: {hypothesis title}

## Date
{date}

## Hypothesis Under Review
{one sentence}

## Assessment

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Axiom Compliance | ... | ... |
| Internal Consistency | ... | ... |
| Limiting Behavior | ... | ... |
| Decisive Checks (mathematical / empirical / both) | ... | ... |
| Minimality | ... | ... |
| Emergent vs. Imposed | ... | ... |
| Claim-Type Fit | ... | ... |

## Overall Verdict
PROCEED / REVISE / REJECT

## Required Revisions (if REVISE)
{numbered list of specific changes needed}

## Evidence And Remaining Obligations
{proof or empirical checks completed; independent verification state;
inherited conditions; unresolved scientific and evidence-packaging obligations}

## Suggested Simplifications
{ways to make the hypothesis sharper or more minimal}
```

## Rules

- No lock needed — this is a thinking exercise.
- Evaluate against the framework's axioms, approved primitives, and retained
  surface — not against known physics. Known physics may define the
  disclosed comparator or target, never the justification.
- An empirical assertion rated UNFALSIFIABLE cannot proceed as an established
  empirical claim; identify whether it can be revised into a discriminating
  test. Judge mathematical claims by their statement and proof: a missing
  empirical runner is not a reason to reject a theorem. An open proof is
  unresolved, and a valid counterexample refutes the stated scope.
- Honor the actual evidence-registration and publication contracts for the
  submitted claim class. If a later mechanical gate requires an unavailable
  artifact, report that packaging limitation separately from mathematical
  validity; do not manufacture a runner, output, proof, or audit status.
- A hypothesis rated IMPOSED gets extra scrutiny — is the work testing the
  framework or just the setup?
- Be constructive: REVISE with specific guidance beats REJECT without an
  alternative.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
