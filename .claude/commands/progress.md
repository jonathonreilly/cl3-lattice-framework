# /progress — Research Retrospective

You are the Research Manager reviewing recent progress on the qubit-lattice
axiom framework.

## Data Collection

1. Freeze the `origin/main` commit and report its SHA and fetch freshness.
   Fetch only when allowed; if unavailable, use cached `origin/main` with its
   limitation explicit. If that ref is absent, report main status unavailable
   rather than treating the current campaign branch as main.
   Landed work: `git log <MAIN_SHA> --oneline --since="1 week ago" -- docs/ scripts/`
   (science) and the same pinned query for `docs/audit/` (audit lane). Exclude
   unrelated history; inspect changed artifacts before classifying the result.
2. PR flow: `gh pr list --state merged --search "merged:>={date-7d}"` and
   `gh pr list --state open` — note science PRs opened, landed, closed with
   salvage, or rejected.
3. Audit-lane movement: audit commits reachable from the pinned main revision;
   queue depth and current retained-grade rows read at that same revision.
   A newly retained claim requires comparison with a named earlier snapshot.
4. Loop state: latest `HANDOFF.md` / `STATE.yaml` under
   `.claude/science/physics-loops/*/` touched this period.
5. Candidate science: read relevant campaign branches and working documents
   separately, identifying each branch/revision and uncommitted state. Report
   proved or tested provisional lemmas, inherited gaps, completed independent
   critical checks, and the next coherent milestone. Unmerged candidate commits
   are not landed-main progress.

## Report Sections

### Summary (3 sentences max)
- Main thrust of the period, strongest new result, current frontier.

### Scientific Evidence Gained

- Exact obligation discharged, construction/proof established, counterexample,
  discriminator, import retired, or uncertainty reduced, with evidence paths.
- State what downstream physical question it advances and which hypotheses or
  provisional dependencies remain. Include useful failed and inconclusive work.

### Claim-State Movement
| Item | Movement | Evidence |
|------|----------|----------|
| {claim/lane} | proposed / landed / audited_clean / retained-grade / demoted / no-go | {PR, commit, ledger row} |

Be precise about the propose/ratify split: "landed on main" is not
"retained" — only the audit ledger grants retained-grade status.

### Key Findings
- Exact mathematical results and quantitative observations from this period,
  each with its proof/evidence and source revision. Distinguish a derivation
  from a numerical comparator match; do not force a number onto a proof result.

### Failed / Dead Ends
- What was tried and didn't work? Bug, artifact, wrong regime, genuine
  wall? Honest no-gos and named walls are valuable output — list them with
  their `NO_GO_LEDGER.md` or note references.

### Pipeline Health
- Review backpressure: findings from recent `/review-loop` runs, demotions,
  salvages.
- Audit lane: queue depth trend, conditional backlog, any blocked rows.
- Hygiene: stale branches, unlanded coherent blocks, `PR_BACKLOG.md` entries.

### Recommended Next Steps
Prioritized by expected evidence value, unresolved upstream obligations, and
decisive checks for the physical objective (defer to `/frontier` for the full
gap analysis):
1. {highest value}
2. {second}
3. {third}

For each: one sentence on why, and estimated effort (interactive /
unattended block / campaign).

## Output

Write to `.claude/science/progress/{date}-retrospective.md`. Create the
directory if it does not exist.

## Rules

- No lock needed — read-only analysis.
- Be honest about dead ends; they are information.
- Do not pad. If it was a slow week, say so.
- Activity counts (PRs, notes, verdicts, promotions) are optional operational
  diagnostics, not scientific progress or a percentage of TOE completion.
- Never blur author-side status with audit-ratified status.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
