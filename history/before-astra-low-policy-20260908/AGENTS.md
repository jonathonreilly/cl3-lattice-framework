# Agent instructions — planning branch

These instructions govern repository work and scoped dispatches. They are
maintained procedures, not scientific premises. Read the user's task before
choosing a workflow; a process or prompt review must examine the instructions
for correctness before applying them. Higher-priority platform instructions
and explicit user constraints control. Report a concrete conflict rather than
turning inherited wording into a new approval requirement.

`origin/main` is the authority for scientific source and applied audit status.
This orphan `ai/execution` branch contains planning only and never merges into
main. For the current lifecycle, read
`git show origin/main:docs/ai_methodology/SCIENCE_WORKFLOW.md`.

## Scientific work

- Treat TOE completion as a hypothesis to establish, not an outcome a worker
  must produce. A proof, counterexample, falsified premise, or precise open
  obligation can all be useful results. Never manufacture progress to satisfy
  a runtime, cycle count, positive-result quota, or reviewer expectation.
- State the exact target, quantifiers/domain, premises, and success witness.
  Distinguish framework premises, mathematical tools with checked hypotheses,
  provisional lemmas, extra conditions, and empirical inputs. New framework
  axioms/primitives require explicit owner approval; conditional exploration
  does not silently grant them.
- Derive the contested value. An expected test constant is legitimate only
  when justified independently of the implementation tested. Record actual
  commands, failures, uncertainties, and unrun checks. Never fabricate a log,
  numeric result, or PASS line or tune a prefactor to a comparison target.
- Inspect exact prior statements and proofs. A retained label is not immunity
  from a counterexample. A failed search is not an impossibility proof; neither
  an arbitrary number of routes nor inability to imagine alternatives closes
  a quantified theorem.

## Cadence — owner-selected 2026-09-07

Use continuous discovery, selective independent checks, and milestone PRs.
The owner has deferred formal audits until a solid TOE is ready.
Develop coherent blocks on an isolated candidate branch and
checkpoint them without forcing one PR per small result. Combine provisional
lemmas only with their open obligations and source revisions explicit.
Independently check critical steps before substantial downstream reuse.

Deliver a reviewable milestone when it establishes a coherent argument,
resolves a useful target, or the user requests handoff. Independent review
checks the final source revision before authorized landing. Formal audit uses
a separate restricted context on landed evidence; audit status remains unset
until that path applies a verdict. Review/audit throughput does not limit
unrelated discovery. A fully established TOE requires complete dependency and
empirical validation; a candidate assembly is not that certification.

## Dispatch and review

The orchestrator owns goal selection, integration, and honest reporting.
Delegate concrete independent work when useful and permitted, using available
capacity rather than a fixed worker quota. A worker may explore alternatives
inside its assigned target; it should challenge an infeasible spec instead of
forcing the requested answer. Estimate total memory and compute across workers;
choose sparse or reduced representations where needed, not a fixed site-count
rule divorced from representation size.

Every dispatch names its target, source revision, allowed paths, output,
verification, and external-action permissions. An analysis dispatch is read-only
except for explicitly assigned output paths and has no implicit commit, push,
or network authorization. Explicitly authorized implementation workers may
edit their assigned files. Independent reviewers receive raw artifacts and a
neutral task, not the author's desired conclusion. Independent reviewers read the complete final source of each frozen unit,
with explicit path, claim, premise, transitive input and applicable-lens
coverage, and confirm corrections in the same reviewer session. Only their
source-bound final PASS supplies reusable review coverage. Authors still read
their complete cold diff before requesting review.

Before landing, the coordinator independently verifies the complete original
constituent and current-main path/claim disposition map, including deleted and
inherited content, actual transitive helper/premise closure and source hashes.
Hashes alone do not prove that inventory complete. The coordinator reads all
author correction diffs, all finding dispositions and proof-critical context,
and every additional integration change relative to the frozen reviewed
sources. It checks the effective current-main delta for science loss and
cross-unit semantic interactions, including interactions across disjoint files.
An unchanged source body with verified complete independent review coverage
need not receive a second identical line-by-line read by the coordinator.
A summary, PASS label, ancestry relation, cache-freshness result or file count
alone is not coverage.

The coordinator directly inspects additional source whenever coverage,
provenance, a discrepancy or an interaction is uncertain. New source/input or
premise bytes, a moved PR head even with identical bytes, new semantic
interactions, incomplete provenance or missing same-session confirmation hold
the affected conclusions and dependents for the original reviewer. Reopen the
affected closure, not automatically every unrelated claim. The exact-current-
main science-loss check and combined base/tree validation gate remain
mandatory. This clarifies the current-main separation of review and integration;
it does not grant an automated coverage, receipt or scientific verdict.

Science authors do not apply audit verdicts. Review may regenerate audit data
for validation but does not grant status. Only the independent audit application
path writes verdicts; it is free to disagree with prior review. Prompt, tooling,
and governance changes receive adversarial behavioral review proportional to
their effect, not scientific ratification of the procedure itself.

## Evidence and recovery

Keep runner output concise but sufficient to inspect every claimed check.
Use `TOTAL: PASS=<n> FAIL=<n>` when the repo runner contract requires it; an
exit code or summary line alone does not prove the mathematics. Preserve fuller
reproduction evidence in the appropriate artifact rather than truncating a
load-bearing result to meet a display limit.

Use isolated worktrees. Preserve dirty and unpushed work on failure and report
recovery paths. Stage intended paths only. Do not import moving-main generated
audit state into a stale science branch. Planning summaries and local memories
are retrieval aids; confirm current source and status before citing them.

## Planning surfaces

Owner direction for the active campaign (2026-09-07): formal audit waits until
a solid TOE is ready. Continue focused independent checks and
reviewed source integration; do not start an audit drain from discovery or PR
review. Mechanical integration validation is distinct from invoking an auditor
or applying verdicts. No candidate or planning entry grants retained status.

Before assigning new science, read `TOE_SCORECARD.md`, `CAMPAIGN_STATUS.md`,
`BACKLOG_STATUS.md`, and the relevant entries in `OPEN_PR_INVENTORY.json`
from this branch. Search
actual open-PR science as well as main; verify changed heads before reuse.
The campaign coordinator maintains the shared status and assignments. Workers
return evidence in assigned artifacts rather than concurrently rewriting them.
`BATCH_REVIEW_PLAN.md` summarizes the reviewed batching process now landed
on main; follow current main for the executable contract. The plan and
`NEXT_REVIEW_UNITS.json` grant no scientific PASS. `BACKLOG_CONSOLIDATIONS.json`
records duplicate closures and transferred obligations, not landed science.

The owner explicitly authorized the coordinator to manage review, fixes and
landing of the backlog on main. All 37 draft PRs are included for actual
ready-or-close triage under the latest owner direction. Ready is a queue
state, not acceptance, and a still-draft PR does not land. Preserve the three
standing owner reservations. Reviewers do not perform GitHub mutations.

- `TOE_SCORECARD.md`: as-of target map; check its revision before relying on it.
- `CAMPAIGN_STATUS.md`: common campaign assignments and current evidence.
- `BACKLOG_STATUS.md`: current authorized landing/triage assignments and actions.
- `OPEN_PR_INVENTORY.json`: complete pinned open-PR routing snapshot, with
  actual Git ancestry and source-file coverage; no scientific authority.
- `BATCH_REVIEW_PLAN.md`: concrete backlog grouping and efficiency proposal.
- `README.md`: branch contract and edit flow.
- `prompt_profiles/CODEX_GLOBAL.md`: versioned local Codex prompt profile.
- `PROMPT_REVIEW_2026-09-07.md`: prompt-review scope and runtime boundaries.
