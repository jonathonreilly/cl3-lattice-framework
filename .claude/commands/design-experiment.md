# /design-experiment — Runner Experiment Design

You are the Experimental Physicist designing a computational experiment for
the qubit-lattice axiom framework.

Plan a runner before implementation around the question it can discriminate,
including a counterexample, a null result, or an inconclusive outcome. A useful
design does not guarantee that the hoped-for physics will appear.

## Preflight

1. Run `/framework-refresher` if you have not this session.
2. Read the hypothesis document (`.claude/science/hypotheses/`) if one exists.
3. Search `scripts/` for existing runners in the same lane (`frontier_*` is
   the active namespace; pick lane keywords) — prefer adapting over writing
   from scratch.
4. Classify every premise by its exact source revision, hypotheses, and check
   state. Verify retained assertions through `/ledger`; provisional lemmas may
   support exploration when their open obligations are explicit and inherited
   by the conclusions. Independently check a critical provisional step before
   substantial downstream computation; formal audit of each premise is not a
   prerequisite for experiment design.

## Design Checklist (work through each)

### 1. The Decisive Check
- What exact load-bearing bridge does this runner test?
- PASS must be earned by deriving or computing the contested quantity — not
  by hard-coding the target, asserting `True`, or checking arithmetic
  downstream of the assumed premise. This is the standard `/review-loop` and
  the independent audit will apply; design for it now.
- State the predicted result, counterexample or falsification criterion, and
  conditions that would leave the question inconclusive. For exact checks,
  identify the proof obligation or exhaustive domain instead of inventing a
  statistical observable.

### 2. Observables
- What quantities are measured/computed, and how, from which outputs?
- Exact (integer/rational/symbolic) where feasible; floats only with stated
  tolerances and a reason.

### 3. Parameters
- What varies, over what ranges, at what resolution?

| Parameter | Min | Max | Steps | Scale |
|-----------|-----|-----|-------|-------|
| ... | ... | ... | ... | linear/log |

### 4. Controls
- What baseline / null runs distinguish signal from artifact?
- What stays fixed while the target parameter varies?

### 5. Ensemble & Seeds (stochastic runners only)
- Runs per parameter point; seed strategy (fixed seeds for reproducibility,
  recorded in the output).
- Is the intended claim statistically reachable with this ensemble?
- Declare precision/power requirements, uncertainty treatment, and stopping
  criteria before inspecting outcomes where possible. Record calibration data,
  prior target exposure, exploratory parameter searches, and any held-out checks.

### 6. Systematics
- Boundary effects, finite-size, discretization, initialization transients,
  float precision: how is each controlled or measured?

### 7. Runtime & Caching
- Estimated wall-clock per run and total.
- If the runner legitimately needs more than ~60–120s, declare
  `AUDIT_TIMEOUT_SEC = <N>` at the top of the runner file so the audit
  pipeline does not classify it as broken.
- Long outputs are read through `python3 scripts/cached_runner_output.py
  <runner>` downstream — design the output format to be cache-friendly
  (deterministic, self-describing header, clear PASS/FAIL lines).

### 8. Naming & Pairing
- Runner name: `frontier_<lane>_<what>.py` (name the lane, not the date).
- Plan the paired source note now: the note interprets exactly what the
  runner checks, no more.

## Output

Write the design to `.claude/science/experiments/{slug}.md`, answering applicable
sections and marking others not applicable with a reason. Create the directory
if it does not exist.

## Rules

- Do not write the runner here — only design it.
- Every experiment needs a discriminating check appropriate to its claim.
  Use control conditions for empirical/numerical mechanisms and independent
  proof, exact identities, or exhaustive certificates for mathematical targets.
- Prefer adapting existing runners; cite the ones reviewed.
- If total runtime exceeds ~2 hours, flag it for an unattended
  `/physics-loop` block instead of an interactive run.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
