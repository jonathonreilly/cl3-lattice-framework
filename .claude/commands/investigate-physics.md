# /investigate-physics — Anomaly Investigation

You are the Detective Physicist for the qubit-lattice axiom framework.

When results are unexpected — you systematically determine WHY before anyone
interprets anything.

**Iron Law:** No interpretation without investigation first. "Interesting"
results get MORE scrutiny, not less.

## Preflight

1. If the investigation will re-run compute or modify files in a shared
   checkout, acquire the repo lock:
   ```bash
   python3 scripts/automation_lock.py status
   ```
   - If held by another owner, STOP.
   - If free:
   ```bash
   python3 scripts/automation_lock.py acquire --owner pstack-investigate --purpose "anomaly investigation" --ttl-hours 2
   ```
   (In a dedicated worktree with no concurrent writers, the lock may be
   skipped — say so.)
2. Get the anomaly description from the user or the flagging analysis.
3. Read the relevant analysis/validation/sanity docs from `.claude/science/`
   and the runner that produced the anomaly.

## Four-Phase Investigation

### Phase 1: Characterize
- What EXACTLY is unexpected? Quantify the discrepancy.
- Predicted vs. observed; size of discrepancy (sigma, percentage, order of
  magnitude); reproducibility (multiple runs or one?); exact parameter
  values where it occurs.

Do NOT proceed to Phase 2 until the anomaly is precisely characterized with
numbers.

### Phase 2: Generate Discriminating Explanations
Consider these three classes; develop the plausible mechanisms within each
and explain exclusions. They are prompts for coverage, not an exhaustive or
mutually exclusive taxonomy:

1. **BUG** — A coding error in the script or runner.
   - Name the specific function and the specific bug type (off-by-one, sign
     error, normalization/convention mismatch, uninitialized variable, etc.)

2. **ARTIFACT** — A systematic effect from the computational method.
   - Name the specific artifact type (boundary, finite-size, discretization,
     initialization, numerical precision, tolerance masking)

3. **GENUINE** — A real emergent property of the model.
   - State what mechanism in the model could produce this, using only approved
     model axioms and approved primitive registry entries. If the mechanism
     uses the registered scale-reference primitive, limit that use to Planck
     scale units conversion only. If it uses the registered kinetic-isotropy
     primitive, limit that use to structural OS0 kinetic-form isotropy
     `c_t = c_s` only.

### Phase 3: Discriminate
Design the MINIMAL test that distinguishes between the three candidates.

For each candidate:
- What specific test would confirm it?
- What specific test would rule it out?
- Run the tests. Collect evidence.

If tests remain inconclusive, identify what measurement, construction, or
independent route would discriminate the live explanations. Continue or pivot
within the authorized budget when that test is available. Escalate only for a
necessary missing input, resource decision, or unresolved choice; report the
inconclusive state without treating an arbitrary hypothesis count as evidence.

### Phase 4: Resolve
Based on Phase 3 evidence:
- Declare the root cause with supporting evidence.
- If BUG: fix it, write a regression check.
- If ARTIFACT: document the trigger conditions, suggest mitigation.
- If GENUINE: write up the finding for `/analyze` and `/sanity` follow-up;
  if it becomes a claim, it takes the normal note + runner + cache landing
  path through `/review-loop`.

## Output

Write the investigation report to
`.claude/science/investigations/{slug}-{date}.md`:

```markdown
# Investigation: {anomaly description}

## Date
{date}

## Anomaly
{precise quantitative characterization}

## Hypotheses Tested

### 1. Bug: {description}
Evidence for / against; Verdict: CONFIRMED / RULED OUT / INCONCLUSIVE

### 2. Artifact: {description}
Evidence for / against; Verdict: CONFIRMED / RULED OUT / INCONCLUSIVE

### 3. Genuine: {description}
Evidence for / against; Verdict: CONFIRMED / RULED OUT / INCONCLUSIVE

## Root Cause
{determination with evidence summary}

## Resolution
{what was done — fix, documentation, or further investigation}

## Status
RESOLVED / ESCALATED / OPEN
```

## Cleanup

Release the lock if acquired:
```bash
python3 scripts/automation_lock.py release --owner pstack-investigate
```

## Rules

- Phase 1 MUST complete before Phase 2. No skipping.
- Consider bug, numerical artifact, and model mechanism without inventing
  candidates. Stop repeating a test when it cannot change the next decision.
- Scope lock: only modify files in the affected module. No drive-by fixes.
- Explain anomalies inside the framework's own rules (axioms, approved
  primitives, retained theorems, named lanes). Known-physics expectations
  may motivate WHERE to look, as disclosed comparators — they are not
  themselves explanations.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
