# Review Feedback Workflow

**Claim type:** meta
**Purpose:** route review findings from a candidate PR through correction,
reviewed landing, and independent audit.

The current lifecycle and division of responsibility are in
[`SCIENCE_WORKFLOW.md`](../ai_methodology/SCIENCE_WORKFLOW.md). The detailed
review procedure is the repo-native
[`review-loop` skill](../ai_methodology/skills/review-loop/SKILL.md).

## Before Landing

1. Develop the candidate on a branch based on current `origin/main`. Pair the
   source note with its evidence, explicit dependencies, and remaining gaps.
2. The author prepares the PR and runs the
   [author preflight](../ai_methodology/skills/review-loop/PREFLIGHT.md).
3. Review-loop checks the candidate before landing. It records exact findings,
   fixes or narrows verified defects in the existing PR path, and re-reviews
   those changes. Missing science stays explicit; wording cannot discharge it.
4. Land only the reviewed candidate after the current review-loop confirmation
   and mechanical gates pass. Preserve current-main changes and the evidence
   tying the review to the landed revision.
5. Hand the landed claim IDs and source/evidence changes to the independent
   audit lane. Review PASS and landing are not audit verdicts or retained status.

PR-local findings remain with that PR until resolved or handed off. Findings
that affect current `main`, survive a PR's closure, or need another source-side
repair belong in [`ACTIVE_REVIEW_QUEUE.md`](./ACTIVE_REVIEW_QUEUE.md). This
queue records actionable feedback; it does not replace the generated audit
queue or the science-fix backlog.

## Findings On Current Main

Record a short, actionable entry in the active review queue with the affected
claim/file, observed defect, evidence or reproduction command, intended
disposition, and next action. Link a detailed packet under
`docs/work_history/repo/review_feedback/` when needed; the active queue remains
the routing surface.

Use the narrowest honest disposition:

- **Source or tooling repair:** fix wording, packaging, reproducible code
  defects, or dependency declarations on a repair branch and submit it for
  review before landing.
- **Claim narrowing:** make the supported scope explicit in source prose and
  request re-audit when the audited claim or evidence changed. Reviewers do
  not hand-edit audit grades or effective status.
- **Science needed:** state the missing theorem, selector, or physical bridge
  and send it to a science task. Keep the unresolved claim explicit.
- **Reject or historical only:** explain why the candidate cannot land or why
  the issue no longer affects the live evidence chain, preserving useful
  evidence and the unresolved branch where required by review-loop.

Audit findings enter the source-repair path through
[`science-fix-loop`](../ai_methodology/skills/science-fix-loop/SKILL.md).
Auditors judge the restricted claim packet independently; source repairs
return through PR review and fresh re-audit.

## Closing Feedback

Close an item only when its stated action is complete. Record the disposition,
landed revision or rejection reason, and any separate re-audit target in the
queue history or linked packet before removing it from the open list. A
source fix may complete its review item while the claim still awaits audit;
report those states separately.

Keep detailed or resolved packets in
[`review_feedback/`](../work_history/repo/review_feedback/README.md) and old
planning material in [`backlog/`](../work_history/repo/backlog/README.md).
Do not create another live feedback queue or use a branch-local memo as the
long-term routing surface for an unresolved current-main defect.
