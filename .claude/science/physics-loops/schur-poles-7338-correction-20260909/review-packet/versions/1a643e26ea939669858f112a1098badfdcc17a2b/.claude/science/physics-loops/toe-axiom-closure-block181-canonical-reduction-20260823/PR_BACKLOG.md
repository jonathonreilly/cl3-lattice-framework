# PR Backlog

Planned stacked PR:

- Base: `physics-loop/toe-axiom-closure-block180-gravity-observable-refinement-20260823`
- Head: `physics-loop/toe-axiom-closure-block181-canonical-reduction-20260823`
- Claim: bounded numerical support for the tested two-chart/raw-quotient
  boundary; gravity remains open.
- Required links: theorem note, primary runner, SHA-pinned cache,
  `TRACE_GATE.md`, `CLAIM_STATUS_CERTIFICATE.md`, `REVIEW_HISTORY.md`, and
  `HANDOFF.md`.
- Required checks: primary `8/8`, eight `7/1` mutations, independent math
  reconstruction, cache freshness, vocabulary lint, citation graph, strict
  audit lint, repository pipeline, and diff check. Every listed check except
  full pipeline completion passes locally; the pipeline reaches static-cache
  capture and then fails on the parent stack's stale policy-v2 dependency
  epoch. Latest `origin/main` contains the reviewed v3 repair at `39c74017b8`.
- Hard landing condition: parent PR #7335 and its transitive Block-74
  dependency land first, or the reviewed delta is explicitly widened; the
  parent stack must also incorporate the landed dependency-policy-v3 repair.
- No `review-loop` invocation and no audit verdict application in this block.
- Parallel overlap: PR #7335 has none; PRs #7333, #7336, and #7337 share only
  the deterministic citation manifest. Regenerate it after any of those land.
