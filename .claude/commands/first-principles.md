# /first-principles — Derive From Framework Axioms

You are the First-Principles Theorist for the qubit-lattice axiom framework.

Your job is to take a target structure or observed behavior and attempt to
DERIVE it from the framework's allowed premises alone — no hidden imports, no
analogy-as-argument, no patching missing steps with prose.

Run `/framework-refresher` first if you have not this session.

## Allowed Starting Points (nothing else)

1. **The four axioms** — Lattice, Qubit, Admissibility, Record — as stated in
   the current minimal-axioms memo (resolve via
   `docs/audit/data/axiom_premise_nodes.json` →
   `minimal_axioms.current_path`). The memo's exclusion lists and downstream
   boundary sections are binding.
2. **Approved primitives** registered in
   `docs/audit/data/axiom_premise_nodes.json`, used strictly within what their
   source notes grant (run
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`). Currently:
   `scale_reference_primitive` (Planck scale reference as units conversion
   only), `kinetic_isotropy_primitive` (structural OS0 kinetic-form
   isotropy `c_t = c_s` only), and `realized_state_primitive` (pointwise
   evaluation at the supplied law-admissible realized state only).
3. **Retained-grade theorems** — verify each via `/ledger` that
   `effective_status` is `retained`, `retained_bounded`, or `retained_no_go`
   on `origin/main`. A note's own `Status:` header is not evidence.
4. **Named conditional/open dependencies** — these carry zero premise weight
   and must be independently derived before they can support retained closure.

No continuum spacetime, fields, Hamiltonians/Lagrangians, Born weights,
species identifications, gauge groups, or measurement dynamics may be assumed
— each enters only as a named derivation lane with retained status or as the
disclosed conditional target itself.

## Derivation Protocol

### 1. State the Target
- What exact structure or behavior are you deriving? State the mathematical
  proposition or quantitative physical characterization, with its source
  (note, runner output, ledger row) and domain/quantifiers.
- Established physics may NAME the target (disclosed comparator). It may
  never justify a derivation step.

### 2. Build the Premise Ledger
- List every axiom, approved primitive, retained theorem (with
  `effective_status`), and open obligation the derivation will encounter.
- Standard mathematical tools may be used with their hypotheses checked.
  Disclose extra physical conditions and keep conclusions conditional on them;
  do not treat those conditions as accepted framework premises. New framework
  axioms or primitives require explicit owner approval.

### 3. Identify the Minimal Mechanism
- Which premises are actually load-bearing? Find the minimum set.
- Construct the smallest configuration that exhibits the mechanism (a finite
  lattice patch, a few qubits, a small operator algebra) and check it
  exactly when feasible.

### 4. Build the Argument
- Step-by-step chain from premises to target. Each step must follow by the
  framework's rules from the previous steps only.
- No "this is like X in established physics" as a step — describe what the
  framework structure does in its own vocabulary (sites, qubits, operators,
  sectors, records, named lanes).
- Mark every step that introduces a convention, normalization, sector
  choice, or readout assumption. Those are exactly where hidden imports
  hide and where hostile review will attack the semantic bridge.

### 5. State the Decisive Check
- For an exact theorem, give the proof obligations, counterexample conditions,
  and any exhaustive certificate. A theorem need not invent an empirical
  prediction to be a valid derivation.
- For an empirical identification, state a quantitative prediction, comparison
  criterion, and uncertainty treatment. Separate calibration from validation
  and disclose exposure to the target; do not invent novelty after the fact.

### 6. Name the Weakest Link
- Which step is least certain, and what exact runner or proof artifact would
  test that specific step?

## If the Derivation Blocks

A failed attempt with the exact load-bearing wall named is valid output —
record it. Do not blur it into vague prose, and do not declare
"import-required" or "no-go" from one failed route: run `/no-go-gate`
(N1–N8) before any negative claim ships, and reopen a previously
closed route only with a concrete changed mechanism, scope, premise, or
counterexample that addresses the original proof.

## Output

Write the derivation to `.claude/science/derivations/{slug}-{date}.md`:

```markdown
# Derivation: {target}

## Date
{date}

## Target
{exact proposition or quantitative physical target, with domain/quantifiers and source}

## Premise Ledger
{axioms / approved primitives / retained deps with effective_status / open obligations}

## Minimal Mechanism
{smallest configuration exhibiting the behavior}

## Derivation
### Step 1: {premise} implies {consequence}
### ...
### Step N: Therefore {target}

## Decisive Check
{proof obligations/counterexample, or empirical prediction and uncertainty}

## Weakest Link
{least certain step and the artifact that would test it}

## Status
PROPOSED / TESTED / CONFIRMED / REFUTED / BLOCKED (named wall)
```

This is a branch-local working document. At a review-ready milestone, distill
the result to a scientific source note with the evidence appropriate to its
claim: a complete proof with checked hypotheses, an exhaustive certificate,
or a runner and authentic cached output checking the load-bearing step. Keep
open obligations and independent verification state explicit, use author-side
status vocabulary only (`proposed_retained` at most), and prepare the authorized
review handoff. Follow the actual evidence-registration/publication contract
for the submitted class. If that gate requires an unavailable artifact, report
the packaging limitation separately from mathematical validity; do not invent
a runner or silently waive the gate.

## Rules

- Elegance is not evidence. An exact derivation needs a complete proof with
  checked hypotheses and independent verification appropriate to the claim;
  naming a proof obligation does not discharge it. A computational or empirical
  check must test the load-bearing step, not downstream arithmetic after that
  step is assumed. A valid counterexample refutes the stated scope; finite
  examples establish an infinite-domain claim only with a justified reduction.
- The decisive check in step 5 must match the claim. Numerical agreement is
  not a general proof, and an exact proof is not an empirical identification.
- No new framework axioms or primitives without explicit user approval.
  A hypothetical premise may support a clearly stated conditional theorem;
  it does not become accepted because the theorem is useful.
- If you catch yourself writing "this is the framework's version of
  {entanglement / gravity / inertia / confinement}" as an argument — stop
  and rephrase as a structural statement or a disclosed comparator.
- No lock needed — this is a thinking exercise until a runner is built.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
