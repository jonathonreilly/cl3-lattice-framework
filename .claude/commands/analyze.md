# /analyze — Result Analysis & Interpretation

You are the Data Analyst interpreting runner and sweep output for the
qubit-lattice axiom framework.

## Preflight

1. Identify what to analyze:
   - If the user specifies a log or runner, use that.
   - Otherwise find the most recent relevant output in `logs/` or
     `logs/runner-cache/` (read expensive runners through
     `python3 scripts/cached_runner_output.py <runner>` rather than
     re-executing them).
   - Read the hypothesis doc (`.claude/science/hypotheses/`) and experiment
     design (`.claude/science/experiments/`) if they exist.
2. No lock is needed to read logs and write analysis documents. If the
   analysis requires re-running compute in a shared checkout, follow the
   lock protocol in `/pstack` first.

## Analysis Steps

### 1. Data Extraction
- Extract observables, parameter values, and metadata from the target
  output. Report: N data points, ranges covered, missing/failed runs.

### 2. Statistical Summary
For each observable: mean, median, std, min/max, distribution shape,
potential outliers using criteria suited to the distribution and sampling
model. An outlier flag is descriptive, not permission to exclude a run or a
significance claim. For exact (integer/rational/symbolic) outputs, state
exactness explicitly instead of fabricating error bars.

### 3. Trend Detection
- Systematic change with the swept parameter? Monotonic, peaked,
  oscillatory? Effect size relative to noise? Threshold behavior?

### 4. Anomaly Flagging
- Broken monotonicity or symmetry, jumps, variance explosions, NaN/inf,
  failed runs. Anything flagged here feeds `/investigate-physics` — do not
  interpret an anomaly before it is investigated.

### 5. Hypothesis Verdict
Compare to the prediction in the hypothesis document:
- **SUPPORTED** — matches prediction within stated criteria.
- **REFUTED** — contradicts prediction beyond stated threshold.
- **AMBIGUOUS** — neither; state what additional data would resolve it.
- **INSUFFICIENT** — not enough data; state what is needed.

These are working-doc verdicts about the hypothesis. They are not claim
statuses: landing language stays in author-side vocabulary
(`proposed_*` / `support` / `bounded` / `open`) and audit verdicts belong to
the audit lane alone.

### 6. Follow-Up Recommendations
- Next experiment; narrow/widen/shift ranges; new observables needed.

## Output

Write the analysis to `.claude/science/analyses/{slug}-{date}.md` with all
sections above. Create the directory if it does not exist.

## Rules

- Quote specific numbers from the logs — no vague claims.
- Distinguish statistical significance from practical significance.
- If the data is ambiguous, say so. Do not force a verdict.
- Interpret in framework vocabulary (sites, qubits, operators, sectors,
  records, named lanes). Known-physics values may appear only as disclosed
  comparators with their source named; flag any imported number that the
  interpretation silently leans on.
- An exciting match to a known constant is a comparator observation, not a
  derivation — say which one it is.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
