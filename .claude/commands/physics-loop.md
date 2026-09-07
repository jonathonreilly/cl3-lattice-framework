# /physics-loop — Long-Running Physics Loop

Run the repo-native physics loop skill from:

`docs/ai_methodology/skills/physics-loop/SKILL.md`

## Invocation

```text
/physics-loop "<science goal>" [--mode plan|run|resume|status|campaign] [--runtime DURATION] [--delivery milestone|block] [--target STATUS] [--literature] [--max-cycles N] [--deep-block DURATION] [--no-pr]
```

Examples:

```text
/physics-loop "retire the DM/leptogenesis 16v support import" --mode plan
/physics-loop "close the Koide Q bridge or prove the next no-go" --mode run --literature --runtime 12h
/physics-loop "work the best open science opportunities" --mode campaign --runtime 12h --target best-honest-status
/physics-loop --mode resume --loop dm-leptogenesis-16v
```

Infer `--mode campaign` for overnight, unattended, long-running, or 12-hour
execution requests even when the user says only `run`.

## Required Behavior

1. Read the skill file above before acting.
2. If execution is requested and `--runtime` is absent, ask the user how long
   to run unattended before launching work.
3. Create or update a durable loop pack under
   `.claude/science/physics-loops/<slug>/`. Existing
   `.claude/science/frontier-workstreams/<slug>/` packs may be read as legacy
   resume surfaces.
4. Ground in current repo authority surfaces, retained work, no-go history,
   atlas/tool surfaces, approved primitive registry entries, and relevant
   publication tables before route selection.
5. For science execution, fetch `origin` and create a clean dedicated campaign
   branch from `origin/main`. Default to `--delivery milestone`: related blocks
   may compose on that branch with explicit provisional dependencies. Commit
   coherent artifacts and preserve incomplete work durably. Use block branches
   when `--delivery block` was requested.
6. Build an assumption/import ledger before new derivation work. Read
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and enumerate
   approved primitives from `docs/audit/data/axiom_premise_nodes.json` before
   naming imports, walls, or bounded-status sources.
7. Generate and score a route portfolio; for theorem or multi-step bridge
   targets, also write the exact target contract and maintain
   `APPROACH_REGISTRY.md` using the skill's proof-search governance reference.
   Execute only a route that can move claim state, retire an import, close a
   blocker, prove a no-go, create a decisive artifact, or make a recorded
   first-principles stretch attempt on a named hard residual.
8. Apply the skill's pre-PR gates in writing: V1-V5 for retained-positive
   proposals and frontier questions as scoped in the skill, and N1-N8 for
   negative claims covered by `no-go-discipline`. The N1-N8 record must land
   in the source note or a linked committed sidecar, with the required N5
   execution evidence in cached stdout. Branch-local certificates and PR text
   alone are not the binding packet. Record V1-V5 in the queue/review history.
9. Add a trace gate for each serious route in `TRACE_GATE.md`: name the exact
   claim/blocker/import the artifact is meant to move, or classify it as
   `frontier_discovery` when it is pure science with no known downstream
   blocker yet. Frontier discovery is valid output, but it must not be framed
   as closing, promoting, or retiring an existing lane.
10. For unattended runs longer than one major cycle, build
   `OPPORTUNITY_QUEUE.md` and rank unresolved obligations and decisive
   discriminators by expected evidence value for the user's objective. Continue
   until runtime/max cycles expires or the skill's documented quality/queue
   exhaustion conditions apply. Positive answers and PR counts are not progress
   criteria.
11. Write `CLAIM_STATUS_CERTIFICATE.md` for each science block. Do not use bare
   `retained` / `promoted` status language in branch-local source notes. Use
   `proposed_retained` / `proposed_promoted` only when the certificate supports
   a theorem-grade proposal and marks the later independent audit requirement;
   otherwise demote branch-local, conditional, same-surface,
   comparator-dependent, or Axiom* consequences to the narrowest honest status.
12. Checkpoint `STATE.yaml`, `TRACE_GATE.md`, and `HANDOFF.md` throughout
   unattended work.
13. Repeated audit/no-go/blocker cycles trigger a search-depth checkpoint.
   Attempt an underexplored mechanism when useful; 3-5 independent attack
   frames and `--deep-block` are planning allocations, not output or time quotas.
   Use neutral briefs, concrete returns, and delayed cross-pollination. Never
   invent frames or prolong an exhausted route; pivot to useful work within the
   authorized budget. Mark target-equivalent missing lemmas `blocked-equivalent`
   until a materially new mechanism appears.
14. Perform the skill's author milestone checks after each major artifact.
   Label these as author checks and hand the PR to a fresh `review-loop` for
   independent review; no author check grants review PASS or audit status.
   Treat local demotions/blockers as block-level demotion/pivot events.
15. Open a PR at a review-ready scientific milestone, an explicit handoff
    request, or budget-end handoff when coherent and ready; `--delivery block`
    retains per-block PRs. Do not force incomplete work or a routine checkpoint
    into a PR. Before extensive reuse of a load-bearing provisional lemma, obtain
    a focused independent check; formal leaf-by-leaf audit is not required for
    discovery. Propagate every unresolved condition to downstream conclusions.
16. Keep science runs science-only. Record proposed repo weaving in
   `HANDOFF.md`; do not update repo-wide authority surfaces until later review
   and backpressure integration.

## Campaign Rule

If the user asks for a 12-hour unattended run, do not exit early just because a
lane hits a no-go, support-only boundary, human-judgment blocker, failed
retained-proposal certificate, dirty PR, or missing GitHub auth. Checkpoint/demote or
backlog the current block, refresh the opportunity queue, and continue on the
next science target. The skill's Stop Conditions govern early completion,
including documented value-gate/corollary exhaustion and global queue or tooling
exhaustion; do not fill the remaining budget with already implied results.

## Non-Negotiables

- No hidden fitted values, selectors, observations, normalizations, or
  literature imports.
- Approved primitives are not hidden imports. The registered
  `scale_reference_primitive` grants the Planck scale reference as units
  conversion only and does not bound a row by itself. The registered
  `kinetic_isotropy_primitive` grants only structural OS0 kinetic-form isotropy
  `c_t = c_s` and does not supply dynamics, a Lorentz-closure theorem, scale,
  spacing-ratio theorem, selector, or empirical content. The registered `realized_state_primitive` grants only pointwise evaluation at a supplied law-admissible realized state; it does not supply a state, state-selection rule, measure, typicality or genericity assumption, weighting, probability rule, or any state-contingent value (quantities that vary across the law-admissible family remain registered data). Proposed primitives not
  in `docs/audit/data/axiom_premise_nodes.json` remain unapproved.
- No Nature-grade or retained-grade proposal language without decisive artifact
  support, a passing retained-proposal certificate, review-loop backpressure,
  and explicit independent-audit handoff.
- Reopen a prior no-go route only with a material reason: a new compatible
  mechanism, changed obligation map, scope correction, counterexample, or
  justified premise change. Verify the original quantified proof first;
  another label or worker does not reopen it.
- Do not run low-value churn: more prose, nearby scripts, or repeated wording
  passes are not major loop progress.
- Do not write bare `retained` / `promoted`, `retained branch-local`, or
  hypothetical/Axiom* consequences as retained on the actual current surface.
  `proposed_retained` / `proposed_promoted` are allowed only as audit-ready
  author proposals, never as audit-ratified retained status.
- Push only dedicated science campaign/block branches. Do not push science work to
  `main`, merge PRs, or open PRs without enough review surface for
  `review-loop`.

## Execution Mechanism

Use the current `docs/ai_methodology/skills/workhorse/SKILL.md` for worker
profiles, neutral dispatch, independent checking, and owned-worker recovery.
The science run prepares source artifacts and author checks. It does not land
its own science or apply audit verdicts; later authorized review and audit lanes
own those actions. Plan against the no-go's primary proof and exact scope,
including live escape routes, rather than its title or a secondary summary.
