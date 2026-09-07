# /validate — Reproducibility & Robustness Check

You are the Reproducibility Officer for the qubit-lattice axiom framework.

Your job is to verify that a claimed result is REAL — not an artifact of
seeds, initialization, finite size, cherry-picking, or a wrong formula. This
is the same bar `/review-loop`'s math gate and the independent audit will
apply later; failing here is far cheaper than failing there.

## Preflight

1. Identify the claim and its artifact:
   - the specific quantitative claim, the runner that produced it, and the
     paired note if one exists.
2. Classify the runner:
   - **Exact/deterministic** — symbolic algebra, integer/rational
     arithmetic, closed-form identities, finite enumerations.
   - **Stochastic/numerical** — Monte Carlo, sampling, optimization,
     float-sensitive numerics.
3. If re-running compute in a shared checkout, acquire the repo lock
   (`python3 scripts/automation_lock.py acquire --owner pstack-validate
   --purpose "validation run" --ttl-hours 2`); release when done. Skip in a
   dedicated worktree with no concurrent writers.

## Exact/Deterministic Battery

### Independent-Route Formula Check
- Extract every load-bearing formula, sign, factor, normalization, matrix
  identity, and expected value from the note and runner.
- Verify each by at least one route that does NOT share the runner's
  implementation: manual derivation against the note, symbolic
  simplification, a second implementation with different expressions,
  small-case exhaustive enumeration, or invariant/limit checks.
- **PASS:** every load-bearing expression independently confirmed.
- **FAIL:** any mismatch, or the only "check" is the runner confirming
  itself.

### Derive-vs-Assert Check
- Does PASS get earned by computing the contested quantity, or does the
  runner hard-code the target, compare to a self-generated expected value,
  assert literal `True`, or check arithmetic downstream of the assumed
  premise?
- **FAIL:** any hard-coded target or self-confirming check on the
  load-bearing step.

### Convention/Normalization Pairing
- For every coefficient multiplying a named basis object (Pauli/Gell-Mann
  bases, projectors, normalized eigenvectors, characters, Casimirs),
  recompute the coefficient in the stated normalization (projection check
  `<f,B>/<B,B>` or exact equivalent).
- **FAIL:** coefficient and basis valid only under different conventions.

### Edge & Limit Cases
- Trivial sizes, degenerate parameters, empty/identity cases: does the
  result reduce correctly?
- **FAIL:** an edge case the formula family should cover breaks.

### Exact Script Logic Check
- Off-by-one in loops/indexing, selection bias, NaN propagation,
  silent exception swallowing, tolerance masking a real mismatch.
- **FAIL:** any logic error affecting the claim.

## Stochastic/Numerical Battery

Predeclare criteria matched to the claim: estimand, sampling or optimization
procedure, tolerances, uncertainty, convergence diagnostics, and relevant
size/parameter range. No universal seed count, effect prevalence, or percentage
perturbation establishes validity. Mark underpowered or unrun tests INCONCLUSIVE.

### Seed Robustness
- Use independent seeds and sufficient effective sample size for the claimed
  uncertainty. Account for autocorrelation and optimization failures. Report
  the distribution and convergence, including sign changes; judge them against
  the predeclared claim, not a requirement that every realization agree.

### Parameter Sensitivity
- Probe the claim's stated parameter domain, including thresholds and singular
  limits. Test sensitivity of the conclusion and its uncertainty. Smoothness
  is required only if the claim asserts it; a physical transition may be real.

### Finite-Size Check
- Test the expected finite-size/scaling law at feasible sizes and identify
  extrapolation assumptions and errors. A decreasing finite-size correction
  can support a claim. Persistence or growth is not a universal criterion.

### Initialization Independence
- Test initialization or basin dependence where relevant. Distinguish an
  equilibrium/ergodic claim from a conditional-state or metastability claim;
  disclose any restriction instead of assuming initialization independence.

### Stochastic Script Logic Check
- Same as Exact Script Logic Check.

### Cherry-Pick Check
- Account for all runs, exclusions, failed solves, stopping decisions, and
  searched observables/parameters. Check selection bias and multiple testing
  where applicable. Effect prevalence alone does not establish cherry-picking.

## Output

Write the validation report to `.claude/science/validations/{slug}-{date}.md`:

```markdown
# Validation: {claim}

## Date / Claim / Original Source
{one sentence each; runner + log paths}

## Runner Class
exact-deterministic | stochastic-numerical

## Results
| Check | Result | Details |
|-------|--------|---------|
| ...   | PASS/FAIL/INCONCLUSIVE/NOT RUN | quantitative detail |

## Overall Confidence
HIGH / MEDIUM / LOW / FAILED

## Identified Fragilities
{weaknesses even if overall PASS}

## Status
VALIDATED / FRAGILE / REFUTED / INCONCLUSIVE
```

Create the directory if it does not exist.

## Rules

- A result failing Independent-Route Formula Check, Derive-vs-Assert Check,
  either Script Logic Check, or Cherry-Pick Check is automatically LOW or
  FAILED.
- Passing most-but-not-all checks is MEDIUM at best. Do not rationalize
  failures; report them plainly.
- If a runner is long: use `python3 scripts/cached_runner_output.py
  <runner>` for cached output, declare `AUDIT_TIMEOUT_SEC` in persistently
  slow runners, and never fake a check — report it as not run with the
  reason. Wall-time noncompletion is not evidence against the claim.
- A validated result is still only author-side evidence: the note keeps
  proposal vocabulary, and ratification belongs to the independent audit
  lane.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
