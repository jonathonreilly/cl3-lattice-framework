# Repository agent entry point

Read `AGENTS.md` and `docs/ai_methodology/SCIENCE_WORKFLOW.md`. The current
research cadence is continuous discovery, selective independent checks, and
milestone PRs/audits. A process-review request examines instructions before
applying them; it does not automatically launch a review or audit drain.

Use the user's configured model and explicit reasoning choices. Proof-critical
review needs the strongest available suitable reasoning; old model names in
command prose are not current configuration. Report actual provenance rather
than inferring independence from a role name.

AI planning and dispatcher instructions live on the separate `ai/execution`
branch, which never merges into `main`:
`git fetch origin ai/execution --quiet` then
`git show origin/ai/execution:AGENTS.md`. Planning supplies no science status.
