---
name: reviewer-backpressure-integrator
description: Use when an LLM agent needs to turn adversarial review feedback into narrow honest repo changes, selective landing decisions, demotions, active review queue updates, or historical archiving.
---

# Reviewer Backpressure Integrator

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Use this skill after review has found pressure points. Its job is not to defend
the original branch. Its job is to make the repo state honest.

For any paper-facing rewrite, read `docs/WRITING_VOICE_GUIDE_2026-04-25.md`
and keep the prose plain: what was claimed, what failed, what survived, and
what remains open.

## Workflow

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for task and authority boundaries.
This skill applies evidenced review feedback; it does not itself authorize
landing, a review/audit drain, or changes to audit status. Source-only work ends
with a reviewable handoff and completed author checks. Only an authorized
review/landing operation integrates source; the independent audit path alone
applies verdicts and derives retention. Preserve provisional assembly and
milestone delivery when this is part of ongoing discovery.

1. **Group findings by disposition.** Use `fix on main`,
   `support-only demotion`, `science-needed`, `reject`, and `historical only`.
2. **Apply the narrowest honest fix.**
   - wording or stale packaging: fix the live surface;
   - missing theorem step: mark open, demote, or leave off-main;
   - useful but non-live material: archive in work history;
   - false or misleading route: reject or convert to no-go.
3. **Align evidence chain and status.** If the note, runner, log, README, and
   claim table disagree, weaken the strongest surface or add the missing
   artifact before promotion.
4. **Prepare selective landing.** Identify the honest subset of a branch and
   hand it to the authorized fresh review/landing lane. If landing is already
   in scope, integrate only its reviewed final revision.
   Keep branch-local review packets and raw traces out of the public front door
   unless they belong in a raw annex.
5. **Update scoped source and handoff surfaces.** If the author claim boundary
   changes, fix source prose and the relevant active review/handoff entry within
   the task. Route authoritative package/status updates to their owning lane;
   never hand-write generated effective status or audit verdicts. Do not revive
   historical lane boards as live status surfaces.
6. **Preserve provenance.** Record why a branch was narrowed, demoted, or
   rejected. Link detailed packets from the active queue or archive.
7. **Close the loop.** Remove active review items only after the repo-facing
   state is correct.

## Backpressure Rules

- If a reviewer is right, change the claim boundary.
- If a reviewer found a real missing derivation, do not patch it with prose.
- If only part of a branch is supported, propose only that part for authorized
  landing; preserve the rest with its unresolved conditions.
- If a result is negative but meaningful, keep it as a no-go or boundary note.
- If a lane is historical, route it to work history rather than live authority.
- If raw evidence is useful but messy, land it under a raw annex with a curated
  front door rather than making it public authority.

## Output

Produce:

- disposition summary;
- exact repo-facing changes needed;
- honest author scope/disposition and independent review/audit state, with any
  existing ratified status quoted from its exact current source revision;
- files/surfaces that must be updated together;
- active queue or archive placement;
- remaining science question, if any.
