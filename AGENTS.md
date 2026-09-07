# AGENTS.md — pointer

Agent instructions for this repository live on the standing `ai/execution`
branch (an orphan branch that never merges into `main`), alongside the other
AI planning surfaces. Read them from any checkout without touching your
working tree:

```bash
git fetch origin ai/execution --quiet
git show origin/ai/execution:AGENTS.md
```

`origin/main` remains the sole authority for science content and audit
status; the `ai/execution` branch holds planning and instruction material
only. Do not check its files out into a `main` working tree.

For the active science/process lifecycle, read
`docs/ai_methodology/SCIENCE_WORKFLOW.md`. A request to review prompts or
procedures does not invoke the workflows under review.
