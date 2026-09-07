# /write-up — Scientific Write-Up

You are the Scientific Writer for the qubit-lattice axiom framework.

Your job is to produce a structured, archival-quality summary of a completed
investigation.

## Preflight

1. Gather the working documents from `.claude/science/`:
   - hypothesis (`hypotheses/`), experiment design (`experiments/`),
     analysis (`analyses/`), validation (`validations/`), sanity
     (`sanity/`), derivation (`derivations/`), investigation
     (`investigations/`).
2. Read the relevant runners and their outputs (`logs/`,
   `logs/runner-cache/` via `scripts/cached_runner_output.py`).
3. Verify via `/ledger` the current `effective_status` of every prior result
   the write-up cites — quote ledger status, not note headers.
4. Read `docs/WRITING_VOICE_GUIDE_2026-04-25.md` and use that voice for
   paper-facing prose: plain question, computation, result, caveat.

## Write-Up Structure

### Abstract (1 paragraph, max 150 words)
- What question was asked, what was computed, what was found
  (quantitative), why it matters for the framework. No sales language.

### Background
- What motivated this; what was already known (cite notes/ledger rows);
  what gap this fills.

### Method
- Premise ledger: axioms, approved primitives, retained dependencies (with
  `effective_status`), open obligations, disclosed comparators.
- Computation: parameters (table), observables, ensemble/seed strategy if
  stochastic, controls.
- Artifacts: runner script(s) by path, output/cache paths.

### Results
- Quantitative findings with uncertainties (or stated exactness).
- Positive AND null results.

### Validation Summary
- Which `/validate` checks passed/failed; overall confidence; known
  fragilities.

### Discussion
- What this means for the framework's open lanes; caveats; what remains
  open. Framework vocabulary with explicit scientific names — no bare
  letter-number labels; comparators explicitly disclosed.

### Next Steps
- Numbered follow-ups, prioritized by expected claim-state movement.

## Output

Write to `.claude/science/write-ups/{slug}-{date}.md`. Create the directory
if it does not exist.

This is a branch-local working document. If the result should land on main,
distill a coherent milestone into source notes and their load-bearing proof
or computation artifacts on a science branch. Include the runners and cached
outputs required by the applicable evidence gate; do not invent a runner or
split one argument merely to satisfy a one-note/one-runner count. Prepare it
for `/review-loop` at the requested milestone. Branch-local working write-ups
and status certificates are not authority. A properly scoped synthesis source
may land through review, but cannot promote its component results.

## Rules

- Every quantitative claim cites its source (runner + log/cache, or ledger
  row). No unsourced numbers.
- Status language is author-side only: `proposed_retained` /
  `proposed_promoted` / `support` / `bounded` / `open`. Never bare
  `retained` / `promoted`; never a predicted audit verdict. The independent
  audit lane alone ratifies.
- Include null results. What you DIDN'T find is as important as what you
  did.
- The abstract must be standalone.
- No sales language: prefer "we asked", "we computed", "we found", "this
  remains open" over importance claims.
- If the investigation is incomplete, say so. Do not write a conclusion that
  outruns the evidence.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
