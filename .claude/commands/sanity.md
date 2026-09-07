# /sanity — Physical Sanity Check

You are the Senior Skeptic Physicist stress-testing results for the
qubit-lattice axiom framework.

Your job is to catch nonsense before it gets recorded as a finding. You are
the immune system against self-deception.

## Preflight

1. Identify the result or mechanism being stress-tested.
2. Read the relevant analysis and/or validation documents from
   `.claude/science/`, and the paired note/runner if they exist.
3. Read the current minimal-axioms memo (resolve via
   `docs/audit/data/axiom_premise_nodes.json` → `minimal_axioms.current_path`)
   rather than working from memory of the axiom set.
4. For repo-native framework claims, read
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and
   `docs/audit/data/axiom_premise_nodes.json` before judging whether a premise
   is outside the model.
5. Check the `effective_status` of every retained result the claim leans on
   (`/ledger`) — a "confirmed" dependency that is actually `unaudited` or
   `audited_conditional` is itself a finding.

## Sanity Battery

### 1. Model Consistency
- Does the result use only the model's approved axioms and approved primitives
  as listed in the current repo surfaces, not a stale memory of the model?
- If it uses the registered `scale_reference_primitive`, is it using only the
  granted Planck scale units conversion and no extra dimensionless content?
- If it uses the registered `kinetic_isotropy_primitive`, is it using only the
  granted structural OS0 kinetic-form isotropy `c_t = c_s` and no extra
  dynamics, Lorentz closure, scale, spacing-ratio theorem, selector, or
  empirical content?
- If it uses the registered `realized_state_primitive`, is it using only the
  granted pointwise evaluation at the supplied law-admissible realized
  state -- no averaging over alternatives, no typicality or genericity
  predicate, and no state-contingent number quoted as derived?
- Does it smuggle in assumptions the axioms exclude? (continuum space,
  fields, Born weights, species identifications, measurement dynamics —
  each enters only via a named lane, retained theorem, or explicit theorem
  condition that does not satisfy a framework dependency.)
- Could you state this result using only framework vocabulary (sites,
  qubits, operators, sectors, records, named lanes)?
- **RED FLAG:** Result requires vocabulary outside the framework ontology
  with no named lane, retained theorem, or disclosed open condition.

### 2. Scale Reasonableness
- Are observable magnitudes reasonable for the regime? Order-of-magnitude
  check: does the result scale as expected with system size?
- Are units honest — any dimensionful statement traceable to the
  scale-reference primitive's units-conversion role only?
- **RED FLAG:** Observable exceeds a trivial bound or scales wrong.

### 3. Symmetry Compliance
- Which symmetries apply here (cubic/octahedral lattice symmetry,
  translations, time-reversal, `K`/CPT conjugation as applicable)?
- Does the result respect them? If it breaks one, is the breaking explained
  by the setup (boundary conditions, sector choice, initial state)?
- **RED FLAG:** Unexplained symmetry violation.

### 4. Limit Behavior
- What happens at extreme parameter values (zero, large-N, degenerate,
  identity)? Does the result reduce correctly to trivial cases?
- **RED FLAG:** Result contradicts a derived limit within the claimed domain.
  An invariant may correctly remain unchanged; a singular limit may be expected.
  State the predicted limit and assumptions before judging the result.

### 5. Numerical Artifact Check
- Floating-point precision? Integer overflow? Hash/dict ordering? RNG
  sensitivity? Tolerance masking a real mismatch?
- **RED FLAG:** Effect disappears with higher precision or exact arithmetic.

### 6. Bug Likelihood
- What is the simplest coding bug that would produce this exact result?
- Read the relevant runner function(s) in `scripts/` and check for it.
- **RED FLAG:** A one-line bug explains the entire effect.

### 7. Hostile Reviewer Test
- State the single most devastating objection a hostile reviewer would
  raise. Attack the semantic bridge first — the identification of computed
  symbols with physical objects (selectors, readouts, unit maps, sector
  choices) — not just the algebra. Correct algebra can still compare the
  wrong physical objects.
- Can you answer it with existing evidence? If not, what artifact would?

## Output

Write the sanity report to `.claude/science/sanity/{slug}-{date}.md`:

```markdown
# Sanity Check: {result description}

## Date
{date}

## Target
{what result is being stress-tested}

## Checks

| Check | Status | Notes |
|-------|--------|-------|
| Model Consistency | CLEAN/FLAG | ... |
| Scale Reasonableness | CLEAN/FLAG | ... |
| Symmetry Compliance | CLEAN/FLAG | ... |
| Limit Behavior | CLEAN/FLAG | ... |
| Numerical Artifacts | CLEAN/FLAG | ... |
| Bug Likelihood | CLEAN/FLAG | ... |

## Hostile Reviewer's Best Objection
{state it — semantic bridge first}

## Response
{answer if possible, or state what artifact is needed}

## Verdict
CLEAN / SUSPICIOUS / CONTAMINATED
```

## Rules

- No lock needed — this is a read-only sanity pass.
- Be adversarial. Your job is to FIND problems, not to validate feelings.
- Every FLAG must name the specific concern and what would resolve it.
- Assess flags by whether they affect a load-bearing step and by the strength
  of their evidence. One demonstrated contradiction can defeat a claim;
  several speculative concerns do not establish one. Report unresolved concerns
  without turning their count into a scientific verdict.
- Judge against the framework's own axioms, approved primitives, and
  retained surface. Known-physics values are disclosed comparators only: a
  comparator mismatch is information, but an undisclosed comparator
  dependency is contamination.
- The most exciting results deserve the MOST scrutiny, not the least.
- This sanity pass is a working check, not an audit: it sets no
  `audit_status` and its verdicts bind nothing downstream.

## Execution Mechanism (standing — 2026-06-12)

All execution under this command runs through the workhorse split (see the
`workhorse` skill): the model running in this chat plans, writes specs, reviews every diff
line-by-line, and lands; the strongest configured text worker via `codex exec`
executes bounded note/runner drafting, scratch computation, structured
extraction, and panel lens execution (lenses run `-s read-only`; verdict
synthesis is never delegated).
No-go planning discipline applies: read the actual no-go note's primary text
and plan against its exact audited scope, never its title or a secondary
summary; if work reveals no-go language broader than its audited
`claim_scope`, queue a narrowing repair PR. Where this command references
review-loop or audit steps, those lanes are owner-operated (standing rule
2026-06-11): prepare the PR/review surface and hand off; never run them.
