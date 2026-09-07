---
name: physics-loop
description: Use when an LLM agent needs to plan, launch, resume, or package theoretical-physics discovery on a hard open lane/problem, with explicit premises, provisional dependency tracking, decisive checks, durable checkpoints, and review PRs at coherent science milestones.
---

# Physics Loop

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Run a stateful theoretical-physics loop that can make a major lane move:
retire a load-bearing import, close an exact support gate, prove a useful
no-go, add a decisive artifact, or isolate the remaining Nature-grade blocker.

This skill is not a bigger `/autopilot` and not a factory for easy audit
artifacts. It is a claim-state machine for hard physics. It must spend real
time on named hard residuals before a route can be declared blocked or the
campaign can end. Preserve useful work durably and prepare reviewable PRs at
coherent milestones; unfinished research does not need a forced PR.

When launched for a long unattended run, the default posture is a **campaign**:
keep working until the runtime or max-cycle budget is exhausted. If one route
or lane hits an honest stop, checkpoint it, select the next ranked science
opportunity from the repo, and continue. Do not stop the whole campaign merely
because the first target ends in a no-go, support-only boundary, or
human-judgment blocker.

For a request like "run for 12 hours unattended", treat the runtime as a work
budget, not a maximum that can be abandoned after the first clean stop. The
agent should spend the allotted time while a scientifically useful route remains.
The quality-exhaustion conditions in Stop Conditions also permit ending a
campaign; elapsed time, cycle counts, and PR counts are never evidence of
progress. Per-route blockers, review demotions, dirty PRs, missing retained
proof, unavailable optional literature, or failed
PR creation are not global stop conditions; they trigger demotion/backlog,
checkpoint, and pivot.

## Arguments

Parse:

- goal/problem text: required unless running `status` or `resume`;
- `--mode plan|run|resume|status|campaign`: optional, infer from the user
  request;
- `--runtime DURATION`: optional unattended runtime such as `45m`, `2h`, or
  `6h`;
- `--target retained|exact-support|bounded-support|no-go|best-honest-status`:
  optional, default `best-honest-status`;
- `--loop SLUG`: optional existing or new loop slug;
- `--workstream SLUG`: legacy alias for `--loop`;
- `--literature`: allow targeted physics/math literature review;
- `--max-cycles N`: optional cap on major execution cycles;
- `--checkpoint-interval DURATION`: optional, default `30m`;
- `--deep-block DURATION`: optional planning allocation for sustained work on
  a hard problem, default `90m`; evidence may justify an earlier route pivot;
- `--delivery milestone|block`: optional, default `milestone`; `block` preserves
  the earlier per-block delivery cadence when requested;
- `--no-pr`: do not open review PRs;
- `--no-review-loop`: skip optional author milestone review only if the user
  asked; this never waives independent review before landing;
- `--no-commit`: do not create commits.

If `--runtime` is absent and the user wants execution, ask how long to run
before launching unattended work. Do not assume a fixed default. If the user
only asks for planning, produce the plan without asking for runtime.

Infer `--mode campaign` when the user asks for an overnight, unattended,
long-running, or 12-hour run, even if the user says only `run`. A campaign
keeps selecting science blocks until the runtime/max-cycle budget or global
queue exhaustion condition is reached.

## Science Delivery And PR Policy

For science loops, work on an isolated coherent campaign branch. The default
`--delivery milestone` supports continuous discovery, selective independent
checks, and PRs/audits at meaningful milestones. `--delivery block` opens a PR
for each review-ready coherent block. Neither mode permits merging science PRs
or pushing science directly to `main` as part of the author run.

A milestone is an independently reviewable theorem or construction, a decisive
empirical result, a scoped negative theorem, a repaired source defect, or a
synthesis that closes a named obligation. Open its PR when the evidence and
conformance requirements are satisfied, at an explicit user handoff request,
or at the end of the authorized budget if the work is review-ready. An
incomplete block, routine checkpoint, or exhausted runtime does not force a PR.

- Start science execution from current `origin/main` after `git fetch origin`.
- Use a dedicated branch namespace such as `physics-loop/<slug>-YYYYMMDD`.
- If the current worktree is dirty or not disposable, create a clean worktree
  from `origin/main` instead of mixing loop output with other changes.
- Treat each coherent major cycle as a **science block**. In milestone mode,
  related blocks may compose on one campaign branch with a recorded dependency
  map. In block mode, prefer `physics-loop/<slug>-blockNN-YYYYMMDD`.
- If a block depends on prior unmerged block output, create a stacked PR whose
  base is the prior block branch. If independent, base it on `main`.
- Commit coherent science artifacts to the dedicated campaign/block branch and push it to
  `origin`.
- Before each commit, run `scripts/vocab_lint.py --fix` on the files
  being committed. The repo's process vocabulary is canonical in
  [`docs/repo/controlled_vocabulary.yaml`](../../../repo/controlled_vocabulary.yaml)
  (design in
  [`VOCABULARY_HYGIENE_DESIGN.md`](../../../repo/VOCABULARY_HYGIENE_DESIGN.md));
  routine local drift with non-link-aware rewrite rules is auto-rewritten as
  part of the commit. Link-aware filename suffix migrations and F-letter
  finding-label migrations are reported but deferred to Cleanup-2 tooling.
  Genuinely new terms that the lint cannot mechanically fix are recorded in the
  vocab-extension queue
  ([`docs/repo/vocab_extension_queue.json`](../../../repo/vocab_extension_queue.json))
  independent of audit rows; they do not block the physics block from
  landing. Vocabulary drift is never a stop condition for a physics loop.
- At a review-ready milestone (or each review-ready block in block mode), unless
  `--no-pr` was supplied, open the PR without waiting for campaign completion. Use
  `gh pr create` when authenticated; otherwise write `PR_BACKLOG.md` with
  exact commands and reasons PR creation failed.
- After opening a PR, verify it with `gh pr view` or `gh pr list`. If the PR is
  dirty against its intended base, update the branch or explicitly mark it as
  stacked in the PR body and `HANDOFF.md`.
- If PR creation or verification fails for network/auth reasons, write a
  complete `PR_BACKLOG.md` and continue the campaign if runtime remains.
  Missing GitHub access is a delivery degradation, not a science stop.
- PR titles must include `[physics-loop]`, the lane/block slug, the block's
  claim type, AND its honest status — two separate slots, each drawn from its
  own canonical enum. A claim type is not a status. The claim type is one of
  `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`, `decoration`,
  `meta` (the `target_claim_type` enum below); the status is one of `open`,
  `no-go`, `exact-support`, `bounded-support`, `conditional-support`,
  `demotion`, `candidate-retained-grade` (the `actual_current_surface_status`
  enum below). Never let one family stand in for the other: "exact theorem"
  and "bounded theorem" are claim-type phrasings, and a title that offers one
  of them where the status belongs states no status at all. A hybrid phrase
  spanning both families is the same defect (conformance spec section 3).
- PR bodies must link the block's `HANDOFF.md`, `TRACE_GATE.md`, notes,
  runners, verification commands/results, review findings, imports
  retired/exposed, trace reachability, and remaining blockers.
- Do not merge, push science to `main`, or update repo-wide authority surfaces
  as part of the science run.

### Provisional Composition And Selective Checks

Discovery may build on unmerged or unaudited lemmas. Record each premise's
exact source revision, hypotheses, proof gaps, author checks, independent check
state, and dependents in the campaign pack. Derived consequences inherit every
unresolved condition; a coherent branch, passing runner, or reviewer agreement
does not make them retained framework authority.

Before extensive downstream reuse of a load-bearing provisional result, obtain
a focused independent check of its contested step. Prioritize high-fanout
dependencies, physical-identification bridges, unexpected matches, and changes
whose failure would invalidate substantial work. If the check is unavailable,
checkpoint the dependency and continue independent work or a small explicitly
conditional probe. Do not deepen a large unverified dependency chain.

Formal review and audit are milestone activities, or targeted checks requested
for a critical dependency; formal audit of every leaf is not a prerequisite for
exploration. The independent audit lane alone ratifies status after landing.
When a premise changes or fails, mark its provisional descendants affected and
recheck them before carrying their conclusions forward.

**Conformance gate — verify before the PR is opened, not after review says
so.** A block PR is not ready to request review until it has been checked,
section by section, against
`docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md`: 1 self-containment,
2 cache and execution discipline, 3 claim-scope honesty, 4 negative claims and
the N-gate, 5 proof obligations, 6 runner validity, 7 packet completeness,
8 links and citation graph, 9 note structure, 10 the propose/ratify boundary,
11 sourced facts and counts, 12 the pre-review gates. Every MUST in that
document is a generation-time requirement of this skill; failing one is a
defect to fix before the PR exists, not a finding to receive. Record the pass
in `REVIEW_HISTORY.md`, naming each section deliberately not applicable to the
block and why — an unrun section is not a passed section. That document
restates rules owned elsewhere and cites each owner: where it and a cited
skill, script, or vocabulary file disagree, the cited authority wins and the
disagreement is a defect in the spec, to be reported in `HANDOFF.md` rather
than followed.

Allowed science-branch output:

- theorem/support/no-go notes;
- scripts/runners and paired outputs needed to inspect the result;
- branch-local loop state under `.claude/science/physics-loops/`;
- review history and handoff notes for later integration.

Forbidden science-branch output (the audit lane is sole authority over
these; a framework PR that ships them overwrites ratified audit state at
merge):

- `docs/audit/data/` (any file, except the single citation-graph manifest
  carve-out stated below);
- `docs/audit/AUDIT_LEDGER.md`, `docs/audit/AUDIT_QUEUE.md`,
  `docs/audit/MISSING_DERIVATION_PROMPTS.md`;
- `docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md` and
  `docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md`.

`bash docs/audit/scripts/run_pipeline.sh` may be invoked for validation
(to confirm the source repair is ingested and the runner row queued or
re-queued as intended), but the regenerated outputs above must be dropped
before commit. Drop by restoring the branch's OWN committed state, never by
importing another ref: `git checkout origin/main -- <paths>` writes the index
as well as the working tree, so on a stale or stacked branch — the normal case
under the parallel landing contract — it silently STAGES current-`main`'s
deltas on those generated surfaces relative to your HEAD.

```bash
python3 - <<'PY_CLEAN'
from pathlib import Path
import sys
sys.path.insert(0, "scripts")
from science_fix_loop import publication_changed_paths, strip_generated_audit_outputs
root = Path.cwd()
strip_generated_audit_outputs(root, publication_changed_paths(root))
PY_CLEAN
```

The one carve-out is `docs/audit/data/citation_graph_manifest.json`, and it is
conditional, proactive, and commit-time. The trigger is graph TOPOLOGY, not
markdown links alone: `docs/audit/scripts/build_citation_graph.py` registers
every non-skipped `docs/**/*.md` file as a graph node BEFORE it extracts any
edge, so a new note carrying only backticked provenance references is still a
new node, and `docs/audit/scripts/write_citation_graph_manifest.py` requires
acknowledgment for every added, removed, or rewired node. When the block's own
commits add or remove any graph node — including a note with zero markdown
links — or rewire any dependency edge, a refreshed manifest MUST co-land with
the block, or the enforced stage-18 guard blocks every subsequent pipeline run
on `main` until someone else lands the acknowledgment. Regenerate it
deterministically on the proposed tree *after* the drop above, read the
stage-18 delta against the tracked manifest before staging, then stage that
one path: acknowledgment is assertion that every added, removed, or rewired
node and edge is intended. Never hand-merge or hand-edit it, and stage it only
when the block's commits actually change graph topology — when they change
none, the correct staged set contains no manifest at all
(`docs/ai_methodology/skills/review-loop/SKILL.md` landing rule; conformance
spec section 8).

```bash
# Only when the block's commits add/remove a graph node or rewire an edge:
python3 docs/audit/scripts/run_citation_graph_build.py
python3 docs/audit/scripts/write_citation_graph_manifest.py
git add docs/audit/data/citation_graph_manifest.json
# Second line of defense: the staged set must be exactly the intended source
# paths plus, at most, the one manifest path.
git status --porcelain
```

Do not weave science results through `README`, `docs/repo/LANE_REGISTRY.yaml`,
`docs/work_history/repo/LANE_STATUS_BOARD.md`, publication matrices,
canonical-harness indexes, active review queues, or methodology docs during the
science run unless the user's task is explicitly a skill/governance update.
Record proposed weaving in `HANDOFF.md` for the later review process.

## Loop Pack

Create or update a durable pack under:

```text
.claude/science/physics-loops/<slug>/
  STATE.yaml
  GOAL.md
  ASSUMPTIONS_AND_IMPORTS.md
  ROUTE_PORTFOLIO.md
  APPROACH_REGISTRY.md
  OPPORTUNITY_QUEUE.md
  NO_GO_LEDGER.md
  LITERATURE_BRIDGES.md
  ARTIFACT_PLAN.md
  TRACE_GATE.md
  CLAIM_STATUS_CERTIFICATE.md
  REVIEW_HISTORY.md
  HANDOFF.md
  PR_BACKLOG.md
```

Legacy packs under `.claude/science/frontier-workstreams/<slug>/` may be read
for resume/migration, but new loop state should use `physics-loops`.

Use `STATE.yaml` as the resume surface: current goal, delivery mode, next
milestone, provisional dependency/check state, target status, runtime,
cycle/block count, active route, approach-family coverage, strongest unresolved
proof obligation, hard residual being attacked, files touched, open imports,
no-go routes, trace-gate classification, review findings, PR status, next exact
action, and stop condition.

For theorem, multi-step bridge, or hard-reduction targets, write the exact
target contract in `GOAL.md` and maintain `APPROACH_REGISTRY.md` using
[`references/proof-search-governance.md`](references/proof-search-governance.md).
Keep mathematical approach families separate from artifact types recorded in
`ROUTE_PORTFOLIO.md`.

Use `OPPORTUNITY_QUEUE.md` in campaign mode. Rank candidate science targets by
the evidence they could add to the user's objective:

- the exact unresolved proof obligation, empirical discriminator, or reusable
  construction and its path to a named downstream physical target;
- expected reduction of uncertainty or retirement of a load-bearing import,
  including a counterexample or a properly scoped negative result;
- verified downstream obligations unlocked, prioritizing shared upstream
  bottlenecks over extra instances of already established results;
- the first decisive check, estimated work and review cost, and available
  computation;
- premise risk, invalidation blast radius, branch size, and overlap with work
  already active or awaiting review.

Use qualitative estimates with reasons, not invented success probabilities.
Distinguish scientific dependency edges from mere citations when estimating
downstream value. A high row count, easier retained label, positive answer, or
new filename does not by itself move the TOE objective. Preserve an exploratory
route when it offers a concrete discriminator even if its chance of closure is
uncertain. Re-rank after new evidence rather than forcing a positive outcome.

Use `CLAIM_STATUS_CERTIFICATE.md` for every science block. It must record the
actual current-surface status, any conditional/hypothetical status, dependency
classes, open imports, review-loop disposition, the intended audit
`claim_type`, trace-gate classification, and whether independent audit remains
required.

Use `TRACE_GATE.md` for every coherent science block. It answers the
reachability question: "If this artifact is true, what exact claim, blocker,
import, or frontier surface does it move?" This is not a demand that all
frontier work already have a downstream consumer; it is a demand not to pretend
that frontier-only work closes a known lane.

Required trace-gate fields:

```yaml
trace_class: direct_blocker_closure|upstream_support|negative_route_pruning|frontier_discovery|methodology
target_claim_id: null|...
target_blocker_text: null|"..."
source_of_blocker_text: null|audit_ledger|review_loop|handoff|user_goal|frontier_question
reachability_to_target: closes|partially_closes|supports|prunes|unknown_frontier|none
artifact_role: theorem|runner_certificate|literature_bridge|no_go|demotion|tooling|frontier_probe
next_trace_action: "..."
```

Trace rules:

- `direct_blocker_closure` requires an exact quoted blocker or import and a
  concrete statement of how the artifact retires it.
- `upstream_support` must name the downstream consumer that could use it, or
  explicitly say the consumer is not yet known.
- `negative_route_pruning` must state which route is pruned and why the no-go
  applies to that route rather than a broader family.
- `frontier_discovery` is valid pure science output. It may have
  `target_claim_id: null`, `target_blocker_text: null`, and
  `reachability_to_target: unknown_frontier`, but the PR/body/handoff must not
  claim it closes, promotes, or retires any existing lane.
- Any retained-positive or promoted-positive proposal must have trace class
  `direct_blocker_closure` or a fully enumerated chain of trace entries whose
  last entry is `direct_blocker_closure`.

## Claim-Status Firewalls

The loop must separate actual current-surface status from conditional or
hypothetical status.

Every theorem/support/no-go note and every loop `STATE.yaml` checkpoint must
state the narrowest status using the controlled vocabulary. When a result
depends on a new axiom, unapproved primitive, same-surface family,
observational input, fitted selector, open derivation obligation, or
human judgment, the actual current surface status is **not** `retained`.

**No-new-axiom/no-new-primitive rule.** The repo does NOT accept extensions to
its axiom stack or primitive registry as part of physics-loop work. `A_min`
means the current minimum axiom set, Lattice + Qubit + Admissibility + Record,
NOT permission to enlarge it. A route or
counterfactual whose closure requires adopting a new axiom or new framework
primitive is `infeasible`, regardless of how productive its consequences would
be. The legitimate import-bearing shape is:

1. take an explicit import (theorem, value, convention) with a narrow
   non-derivation role;
2. produce a **bounded theorem/support** result — the import-bearing
   ceiling;
3. queue an import-retirement audit as the next work in the lane.

**`audited_conditional` from `dependency_not_retained` is normal.** When a
physics-loop PR ships a derivation that cites an upstream authority that is
itself still `unaudited` or `audited_conditional`, the downstream's first
verdict can correctly be `audited_conditional` with
`notes_for_re_audit_if_any: dependency_not_retained`. This is expected
dependency bookkeeping, not a defect in the downstream proof. Do not
over-engineer around that verdict when the only obstruction is upstream
retention still pending. The cascade-resolution mechanism in
[`docs/ai_methodology/skills/audit-loop/SKILL.md`](../audit-loop/SKILL.md)
checks `docs/audit/data/reaudit_candidates.json` before the regular queue
and re-audits these rows once upstream retention lands.

Any artifact that maps consequences of an unadopted axiom must be
labeled `hypothetical_axiom_status: ...` and its tables/runner summaries
must say "conditional on accepted new axiom; not retained on the actual
current surface." This labeling does not promote the axiom — only an
external repo-wide governance decision does that, and physics-loop
runs do NOT make such decisions.

Approved framework primitives are supplied foundation content alongside the
axioms, not bounded imports. They must already be recorded in
`docs/audit/data/axiom_premise_nodes.json`, where they chain-satisfy
dependencies without bounding downstream rows. No admission class exists;
decision history has zero premise weight.
<!-- BEGIN GENERATED: axiom-baseline (generate_skill_axiom_baselines.py) -->
Generated by `docs/audit/scripts/generate_skill_axiom_baselines.py`: every
paragraph below is extracted verbatim from the source section named in italics
above it (whitespace re-wrapped, inline links flattened). The cited source file
is the authority; do not hand-edit inside the markers.

**Axiom baseline** (source: `docs/MINIMAL_AXIOMS_2026-06-29.md`; axioms:
Lattice, Qubit, Admissibility, and Record)

*Lattice / Physical Locality*

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

No site is privileged. Sites are distinguished by the supplied lattice
structure alone.

*Qubit / Site Possibility*

Each site has a domain of local possibilities.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
adds no further primitive structure.

No possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone.

*Admissibility / Local Constraint*

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

*Reading notes (interpretive, non-governing).* (1) The distribution is
law-level: the general substrate is the weighted-branching realization, with
deterministic substrates as boundary realizations -- the law supplies the odds;
the realized state supplies the pick. (2) Read with Record, the distribution
concerns which possibility a forming record locks, conditional on formation at
that site; it does not supply the formation site, probability, or rate. (3) The
distribution is a probability measure on the local possibility domain;
"available"/"admissible" denotes its support -- on finite menus, exactly the
possibilities of nonzero probability. On a continuous domain, a supported exact
point may have zero singleton measure; Record locks a supported realization.

*Record / Fixed Reality*

Records form.

When present, a record locks exactly one admissible local possibility. A site
never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

*Qualification*

These axioms state only their named primitive content. Further physical
structure requires a retained derivation or bridge, or explicit
approved-primitive registration, before use as a premise. A choice not fixed by
the supplied structure remains a named conditional or open dependency.

A state is a configuration of records.

A law privileges no states. Its domain is a supplied condition, and at every
state where the condition holds it gives exactly one answer.

*Open Gates Outside The Axioms*

The four axioms do not close, import, or rename the framework's downstream open
gates. In particular, the following remain outside axiom content:

- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta gauge and mass-side derivation obligations;
- P2/modulus/phase-blindness and any log-det readout theorem;
- context selection, measurement basis selection, Born weight values,
  probability rules beyond the distribution clause, update laws, decoherence
  mechanisms, and the remaining formation rules (the distribution's form and
  values, at which site, and at what rate);
- arrow, record-production dynamics, physical persistence dynamics, time
  metric, and local observability of records;
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference primitive and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length.

**Approved primitives** (registry: `docs/audit/data/axiom_premise_nodes.json`)

**`scale_reference_primitive`** (source:
`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`)

*What This Declares*

The framework takes exactly one dimensionful reference: a scale that converts
the framework's lattice-natural units to physical units. The chosen reference
is the Planck mass scale, `a^{-1} = M_Pl`.

This is a units conversion, not a physics axiom. It carries zero dimensionless
content: no mass ratio, coupling, mixing angle, phase, selector, readout
bridge, or empirical fit is supplied by it. A row whose only otherwise
non-retained dependency is this scale-reference primitive should not become
`retained_bounded` merely for using a ruler.

*What This Does Not Do*

- It does not add or amend an axiom. The minimal framework baseline is the four
  named axioms: Lattice, Qubit, Admissibility, and Record.
- It does not assert `a/l_P = 1` as a derived theorem. The self-consistency
  question that the framework's natural unit equals the Planck length remains a
  separate open gravity derivation.
- It does not supply any dimensionless quantity. Dimensionless physics must
  derive from retained-grade framework content or remain conditional/open.
- It does not change any audit verdict. Audit status remains set only by the
  independent audit lane.

**`kinetic_isotropy_primitive`** (source:
`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`)

*What This Declares*

The framework takes one structural graining fact: the emergent evolution tick
is grained on the same footing as the spatial lattice edge. Concretely, the
matter kinetic normalization is space-time isotropic,

`c_t = c_s`,

equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are
computed is hypercubic-symmetric (the Osterwalder-Schrader OS0 kinetic
normalization). One tick is one edge in **form**, not only in spacing.

This is a structural statement about the regulator geometry, the time-direction
analogue of the `LATTICE` axiom's spatial **cubic adjacency** `a_x = a_y =
a_z`. It carries no dimensionless dynamical content: no mass ratio, coupling,
mixing angle, phase, selector, readout bridge, or empirical fit is supplied by
it. It is not a fourth spatial dimension, not a new dynamics, and not a
re-axiomatization of time: the framework's time remains emergent and derived
(the single-clock codimension-1 evolution theorem); this primitive fixes only
the one dimensionless graining ratio relating that emergent time to space.

*What This Does Not Do*

- It does not add or amend an axiom. The minimal framework baseline is the four
  named axioms in `MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit,
  Admissibility, and Record.
- It does not re-axiomatize time. The emergent single-clock evolution remains
  derived; this primitive normalizes only the one graining ratio `c_t / c_s`.
- It does not supply any dimensionless dynamical quantity. No mass ratio,
  coupling, mixing angle, phase, or selector is supplied; dimensionless physics
  must derive from retained-grade framework content or remain conditional/open.
- It does not supply the absolute scale (`scale_reference_primitive`) or the
  spacing ratio (derived from the no-diagonal clause); it supplies only the
  kinetic-form isotropy.
- It does not change any audit verdict. Audit status remains set only by the
  independent audit lane.

**`realized_state_primitive`** (source:
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`)

*What This Declares*

The framework takes one realized-state reference: a law-admissible state
supplied by the physical history.

This is pointwise evaluation, not a state-selection rule. It carries zero
state-contingent content: no state, averaging over alternatives, measure,
weighting, probability rule, typicality claim, genericity claim, preferred
state, default state, boundary condition, normalization rule, or value is
supplied by it.

A row may evaluate an already-defined state functional at the supplied realized
state. A value that would change under a different law-admissible realized
state is registered data, not derivation output.

*What This Does Not Do*

- It does not add or amend an axiom. The minimal framework baseline remains the
  four named axioms: Lattice, Qubit, Admissibility, and Record.
- It does not supply a state, state-selection rule, averaging over
  alternatives, measure, weighting, probability rule, typicality claim,
  genericity claim, preferred state, default state, boundary condition,
  normalization rule, or state-contingent value.
- It does not assert any special boundary condition on the realized history. A
  low-record or low-entropy boundary remains a separate named input, anchored
  at
  `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`.
- It does not change any audit verdict. Audit status remains set only by the
  independent audit lane.
<!-- END GENERATED -->
Before writing a wall/import/dependency statement in `STATE.yaml`,
`ASSUMPTIONS_AND_IMPORTS.md`, `TRACE_GATE.md`, `CLAIM_STATUS_CERTIFICATE.md`,
`HANDOFF.md`, or a source note, perform
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. If the only issue is
use of the registered `scale_reference_primitive`, record it as an approved
units primitive. If the only issue is use of the registered
`kinetic_isotropy_primitive`, record it as approved structural kinetic-form
isotropy. If the only issue is use of the registered
`realized_state_primitive`, record it as approved pointwise specialization to
the supplied realized state. Keep the actual status judgment focused on any additional
dimensionless dynamical quantity, selector, readout, normalization,
specific probability-distribution value, dynamics, closure theorem, or
empirical content.

Required status fields for major artifacts:

```yaml
actual_current_surface_status: open|no-go|exact-support|bounded-support|conditional-support|demotion|candidate-retained-grade
target_claim_type: positive_theorem|bounded_theorem|no_go|open_gate|decoration|meta|null
trace_class: direct_blocker_closure|upstream_support|negative_route_pruning|frontier_discovery|methodology
reachability_to_target: closes|partially_closes|supports|prunes|unknown_frontier|none
conditional_surface_status: null|...
hypothetical_axiom_status: null|...
admitted_observation_status: null|...
claim_type_reason: "..."
audit_required_before_effective_retained: true|false
bare_retained_allowed: false
```

Hard wording bans in branch-local physics-loop artifacts:

- bare `retained` / `promoted` in source-note `Status:` lines;
- using source-note status prose as an audit authority;
- `retained branch-local`
- `would become retained`
- `promote to retained`
- `retained on the actual surface` when a required premise is conditional,
  hypothetical, conditional, fitted, or human-judgment-only.

Use `Type:` / `Claim type:` metadata for the intended audit classification.
Source-note status prose must never be presented as audit-ratified retained
status.

Allowed replacements include `exact negative boundary`, `exact support`,
`bounded support`, `conditional / support`, `open`, `demotion`, and
`hypothetical consequence map`. If the artifact maps what would follow from an
unadopted axiom, every table and runner summary must say "conditional on
accepted new axiom; not retained on the actual current surface."

## Claim-Type Certificate

Bare `retained` / `promoted` is an audit-ratified effective status, not a
branch-local author status. `target_claim_type` describes the intended source
claim even while it is open, conditional, or awaiting review. It must not be
withheld or replaced by a status enum because retention is unproved. In
particular, a `bounded_theorem` names its hypotheses and does not claim their
framework derivation. Type, author support status, independent review, and audit
ratification are separate fields.

Before claiming `candidate-retained-grade` support for an unconditional
framework target, verify all of these:

1. `CLAIM_STATUS_CERTIFICATE.md` names the intended `target_claim_type`.
2. No open imports remain for the claimed target.
3. No observed target values, fitted selectors, conditional unit conventions, or
   literature values are load-bearing proof inputs.
4. Every dependency is retained, a retained corollary, or explicitly allowed
   exact support on the current authority surface.
5. A runner or proof artifact checks dependency classes, not only numerical
   output.
6. `TRACE_GATE.md` gives a direct blocker/import closure path for the proposed
   target; frontier-discovery/support-only trace classes cannot certify
   retained-grade proposal language by themselves.
7. Author artifact checks are complete with no unresolved blocker to that
   proposal. Record independent review as pending until a fresh review-loop
   actually completes; an author `pass` is not its receipt.
8. The PR body and handoff explicitly say independent audit is still required
   before the repo may treat the claim as retained-grade.

If any item fails, keep the intended claim type and use `open`, `exact-support`,
`bounded-support`, `conditional-support`, `no-go`, or `demotion` for the honest
support status instead. A correctly scoped bounded result remains eligible for
review under its explicit hypotheses; it does not pass as unconditional closure.

## Campaign Continuation Policy

Long unattended runs must continue through local stops.

Nonfatal events that must **not** end a campaign while runtime remains:

- a route produces a no-go, exact negative boundary, demotion, or blocker;
- review-loop returns `demote` or `block` for the current artifact;
- retained-proposal certification fails;
- a PR is dirty, stacked, or cannot be opened because of GitHub/network auth;
- a lane reaches a human-judgment premise;
- optional literature access is unavailable for one route;
- the repo automation lock is unavailable but a branch-local supervisor lock
  can still prevent duplicate work.

Required response to a nonfatal event:

1. demote or archive the current artifact honestly;
2. checkpoint `STATE.yaml`, `HANDOFF.md`, `REVIEW_HISTORY.md`,
   `TRACE_GATE.md`, and `CLAIM_STATUS_CERTIFICATE.md`;
3. preserve coherent work in the campaign branch; open a PR only when the
   selected delivery cadence and review-readiness conditions are met, or record
   an actionable delivery failure in `PR_BACKLOG.md`;
4. refresh `OPPORTUNITY_QUEUE.md`;
5. choose the next highest-ranked science opportunity by expected evidence
   value and continue.

Global stop is allowed only when:

- runtime or max cycles is exhausted;
- the worktree/repo changes externally in a way that makes safe continuation
  impossible;
- required core tooling for all viable routes is unavailable;
- a lock conflict means another active worker owns the same repo/task and no
  clean independent worktree can be created;
- the refreshed opportunity queue proves every viable target is blocked and no
  independent useful candidate remains;
- the documented corollary/value-gate exhaustion conditions in Stop Conditions
  are met after the required substantive search.

## Required Grounding

Before proposing or executing routes, read the relevant current repo surfaces:

- `docs/repo/REPO_ORGANIZATION.md`
- `docs/repo/CONTROLLED_VOCABULARY.md`
- `docs/repo/ACTIVE_REVIEW_QUEUE.md`
- `docs/repo/REVIEW_FEEDBACK_WORKFLOW.md`
- `docs/CANONICAL_HARNESS_INDEX.md`
- `docs/repo/LANE_REGISTRY.yaml`
- `docs/work_history/repo/LANE_STATUS_BOARD.md`
- relevant notes, runners, retained logs, publication tables, no-go notes, and
  atlas/tool surfaces for the requested lane.

For publication-facing or quantitative work, also inspect
`docs/publication/ci3_z3/` and
`docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md`.

## Workflow

1. **Preflight.** Check worktree state. If running unattended or modifying
   files, use the repo lock protocol and plan lock refreshes at checkpoints.
2. **Ground, then sweep for prior art.** Build the current lane map from repo
   authority surfaces rather than memory.

   **Include relevant open PR science.** Main owns adopted premises and status;
   open proposals may contain newer results, counterexamples or stronger versions
   of the target. Use the PR inventory to locate relevant proposals, then read
   their bodies, changed primary science, evidence, substantive review findings
   and actual dependencies before claiming novelty or reusing a result. Record
   the exact revisions and what was actually read, including limits. Reuse
   matching coverage and inspect affected changes; a title or matching receipt
   alone establishes no scientific conclusion. Do not make complete reading of
   every unrelated open PR a prerequisite for a bounded research block.

   Respect the owner's intake scope. A fixed backlog cutoff does not authorize
   a global capture or review of new arrivals. Keep the frozen inventory and its
   outstanding obligations; refresh only the authorized proposals as needed.

   When a complete new intake is authorized, the optional helper
   `python3 scripts/open_pr_science_coverage.py capture --repo OWNER/REPO --output current.json`
   checks the total open count, binds head/base commits and proposal metadata,
   recovers paginated changed-file lists, and rejects observed capture drift.
   Preserve that snapshot. After an actual read, use
   `python3 scripts/open_pr_science_coverage.py receipt --reviewed current.json --number N --read-coverage 'Surfaces read and limits'`
   to emit its JSONL receipt. The offline
   `python3 scripts/open_pr_science_coverage.py check --current current.json --reviewed reviewed.json --receipts reads.jsonl`
   compares declared coverage with both saved inventories. It does not fetch
   new proposals. These commands accept this helper's versioned inventory
   schema; another planning inventory is not interchangeable merely because it
   lists the same PRs.

   Exit 0 means matching declared coverage, 1 means missing/stale receipts, and
   2 means invalid inputs. The helper cannot verify reading or understanding;
   partial declared coverage remains partial even if it matches. Its result is
   an optional planning aid, not a universal research gate, scientific grade,
   proof review or landing permission. `updatedAt` is a conservative metadata
   signal, not a stored review-discussion transcript; inspect relevant discussion
   when refreshing. Proposed results remain provisional under their actual
   premises and review state.

   **Then search the repo for the result you are about to produce, before you
   produce it.** This is a hard prerequisite, not a courtesy. The failure mode
   was observed on 2026-07-25: a cycle derived that a finite-dimensional
   complex `C*`-algebra generated by two commuting faithful unital
   star-embeddings of `M_2(C)` is isomorphic to `M_2(C) (x) M_2(C)`, opened a
   PR, and had that claimed-new algebraic component rejected as non-novel
   because `docs/GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md`
   already proved the statement for `n` sites — strictly more general, landed
   twelve days earlier. The loop had searched hard for claims that would
   *contradict* the result and never once searched for the *result itself*.

   Refresh the landed ref immediately before each sweep and record the commit
   searched. A long campaign must not rely on the `origin/main` value fetched
   at startup:

   ```bash
   git fetch origin main:refs/remotes/origin/main
   git rev-parse origin/main
   ```

   Search on the **statement**, not on the lane name and not on your framing.
   Use multiple distinctive nouns, their reverse order, notation variants, and
   synonyms; no result from one ordered regular expression is not evidence of
   absence:

   ```bash
   # distinctive nouns of the theorem, over landed source notes
   git grep -n -iE "(<noun1>.*<noun2>|<noun2>.*<noun1>)" origin/main -- 'docs/*.md'
   git grep -n -i "<notation-or-synonym>" origin/main -- 'docs/*.md'
   # titles encode results in this repo -- read the file list before the files
   git ls-tree -r --name-only origin/main -- docs/ | grep -iE "<key-noun>"
   # obligation and sharded claim/no-go rows that name the same object
   git grep -n -i "<object>" origin/main -- \
     docs/audit/data/derivation_obligations.json \
     'docs/audit/data/ledger/*.json'
   ```

   Read each hit's exact statement, hypotheses, proof or decisive artifact,
   current audit/effective status, and any active review finding. First mark
   nonmatching or context-only hits as such; they are search evidence but not
   prior results. Then classify the **target state** into one of three outcomes
   and record the searched commit, commands, hits, and classification in
   `ROUTE_PORTFOLIO.md`:

   - **Already proven on matching premises.** Stop. Cite it and pick a
     different target. A more general landed version outranks your special case
     even when your proof is cleaner. If its proof is broken or an active
     finding disputes the matching statement, target that repair instead of
     silently duplicating it.
   - **Already refuted at matching scope.** If the proof leaves compatible
     escapes, do not stop — see step 4. If it leaves none, stop and pick a
     different target.
   - **Open after the matched-hit review.** Proceed, and quote the search you
     ran in `V2` so the reviewer can check the novelty claim instead of taking
     it on trust.

   A landed headline or audit label is not proof of correctness. Conversely,
   an unaudited or non-clean package can still contain prior art that defeats a
   novelty claim; record its state and review the matching content directly.

   Understanding repo state is the point of this step. A campaign that does not
   know what is already landed cannot price its own novelty, and the Promotion
   Value Gate's `V2` and `V5` answers are worthless without it.
3. **Audit assumptions/imports + counterfactual pass.** Create or
   refresh `ASSUMPTIONS_AND_IMPORTS.md` with the import ledger AND
   the counterfactual pass over implicit framework choices (geometry,
   boundary conditions, observable definitions, irrep truncations,
   traversal conventions, sector choices, normalization conventions).
   The counterfactual pass surfaces hidden routes by asking, for each
   assumption, "what if this is wrong, and what direction does the
   alternative open?" — bounded by the no-new-axiom rule below. See
   [`references/assumption-import-audit.md`](references/assumption-import-audit.md).
4. **Update no-go memory — by reading the proofs, not the headlines.** Extract
   prior no-go routes and reviewer objections into `NO_GO_LEDGER.md` so the loop
   does not re-explore dead routes.

   **Do not treat a no-go title, verdict, or summary as the finding.** Open the
   note and read what was actually proved, at what scope, under which supplied
   premises. In this repo a no-go is a map, not a wall: notes routinely carry a
   `Remaining Live Routes`, `Escape conditions`, or `What Does Not Move` section
   that names precisely what would still close the target. That section is
   usually the most valuable text in the lane, and it is invisible from the
   title.

   Record for each no-go, in `NO_GO_LEDGER.md`:

   - the **exact quantified scope** — what it ruled out, over which family, on
     which surface. Broad-sounding titles frequently cover narrow claims;
   - the **supplied premises** the refutation leans on, since a route can reopen
     when one of them is retired;
   - the note's current **claim type, audit/effective status, and active review
     findings**. An unaudited or non-clean no-go is prior-art evidence, not
     authority that a route is dead;
   - every **named live route**, verbatim, with its own status;
   - whether the escape is derivation, a new governance decision, or approval
     and registry of a new primitive — the last two are not available to a
     physics-loop run. An already registered approved primitive remains
     available within its declared boundary; run the primitive-registry check
     before classifying the route.

   Two failure modes this prevents, both observed:

   - **Believing the headline and stopping.**
     `docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md`
     listed four remaining live routes; a run that read only the verdict would
     have written the whole target off.
   - **Believing the headline and duplicating.** The different
     `docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md`
     had already shown that the homogeneous Record-additive, `C3`-covariant
     ansatz leaves a free one-parameter coefficient family, including the
     distinct witnesses `alpha` in `{0, 1/9, 1/3, 1, 2/27}`; only
     `alpha = 2/27` is the target member. A run that skipped the proof could
     repeat that failed symmetry-only pin. The separately named inhomogeneous
     readout theorem remains live.

   Prior-art hits classified as "already refuted, with escapes" in step 2 land
   here, and the surviving escapes — not the refutation — are what feed the
   route portfolio in step 5.
5. **Generate route portfolio.** Produce several independent routes and score
   them by likely claim-state movement. See
   [`references/route-patterns.md`](references/route-patterns.md).
   For theorem, multi-step bridge, or hard-reduction targets, also apply
   [`references/proof-search-governance.md`](references/proof-search-governance.md):
   freeze the exact target contract, normalize routes into mathematical
   approach families, preserve early-round independence, and classify every
   terminal missing lemma by strength relative to the target.
   When a route will produce a new source note and companion runner,
   use the abstract-algebraic core extraction reference to separate the
   provable algebraic core from imports, numerical checks, and parent
   ambitions before engineering the artifact. See
   [`references/abstract-algebraic-core-extraction.md`](references/abstract-algebraic-core-extraction.md).
6. **Draft the trace gate.** For each serious route, write the expected
   trace class before execution. If the route is pure frontier work, mark it
   `frontier_discovery` rather than inventing a downstream blocker. If the
   route is intended to move a known lane, quote the exact blocker/import it
   is supposed to retire.
7. **Build the opportunity queue.** In campaign mode or unattended runs longer
   than one major cycle, create `OPPORTUNITY_QUEUE.md` and keep at least three
   ranked science opportunities unless the repo has fewer viable open targets.
   Prefer unresolved upstream obligations or decisive discriminators over more
   audit churn after one or two no-go/support-only cycles. Evaluate the
   information gained without requiring an affirmative result.
8. **Apply the dramatic-step gate.** Execute only routes that can change the
   lane state: import retired, exact support added, no-go proven, major blocker
   isolated, or novel structure introduced with a falsifier. Apply the
   **corollary-churn check** alongside the gate: if the proposed cycle's output
   would be a one-step algebraic corollary of an already-landed cycle in this
   campaign — same load-bearing premises, same retained surface, just a
   relabeling or specialization — reject it as churn even when the arithmetic
   is correct. A cycle must introduce a new load-bearing premise, close a
   named residual not yet closed in this campaign, attempt a stretch on an
   unattempted hard residual, or synthesize prior cycles with a new structural
   insight. "Plug already-derived hypercharges into the photon-charge formula
   for hadron X" is the canonical churn shape; do not produce it.

   **PROMOTION VALUE GATE (mandatory pre-PR self-review).** If the campaign goal
   includes "promote bounded → retained" or any retained-positive movement, the
   agent MUST answer the following questions IN WRITING in a value-gate section
   of `OPPORTUNITY_QUEUE.md` or `REVIEW_HISTORY.md` before opening any PR. This
   value-gate record is not an audit certificate and must not state or predict
   an audit verdict. Failing any single question forbids the PR — discard the
   cycle and pivot, do NOT downgrade to a lower-value pattern just because work
   has already been done.

   | # | Question | Required answer to allow PR |
   |---|---|---|
   | V1 | What exact unresolved obligation or discriminating question does this PR address? | State the target and cite its current source: a primary note, derivation obligation, validated science-fix handoff, review finding, or explicit user goal. For a repair, reproduce the defect on current main. An existing audit verdict is not required for new science. Mere upstream non-ratification is an audit scheduling issue unless an actual missing upstream derivation is supplied. |
   | V2 | What evidence does this PR add beyond the existing repo, and **what repo search established that** (step 2)? | Describe the new proof, construction, counterexample, decisive computation, or repair. Record the searched commit, commands, matching hits, and scope comparison. Re-checking an already supported identity does not become a new derivation; independent verification is legitimate when it resolves a named reproducibility or correctness concern and is described as such. |
   | V3 | Does the artifact actually discharge the named obligation using justified premises, or provide the declared decisive discriminator? | "Yes" with the exact proof step or evidence path and every remaining gap. Standard mathematical tools are valid when their hypotheses are checked and their import role is explicit. Do not reject a missing derivation because an auditor could in principle carry it out; the author must supply that derivation. A proof is not new merely because it uses unusual machinery. |
   | V4 | Is there a concrete scientific or evidential gain beyond restating a definition or established consequence? | "Yes" with the before/after obligation or uncertainty. A short proof can close a hard gap; length and apparent sophistication are not acceptance criteria. Pure arithmetic or renaming without a new obligation discharged fails this question. |
   | V5 | Is this a one-step variant of an already-landed cycle in this campaign, **or of anything already on `origin/main`**? | "No" — name the closest prior cycle and explain the structural distinction. "Same matrix structure, different physical interpretation" is NOT a structural distinction; it's relabeling. Refresh and check `origin/main`, not only the campaign's own cycles, and record the searched commit — a landed note you did not know about still counts, and a more general landed version outranks your special case. |

   A `frontier_discovery` route answers V1 with its explicit open question and
   V3 with its declared discriminator or construction. It need not invent an
   existing audit obstruction, but it must add new evidence and must not be sold
   as closure. Source-repair authors may use validated applied-audit feedback;
   never pass prior verdict rationales or expected outcomes to a restricted
   independent audit seat.

   Review-loop triage of the 2026-05-02 audit-backlog campaign found too many
   branches whose marginal repo value was review-prep rather than new science.
   Do not repeat that failure mode.

   **NO-GO DISCIPLINE GATE (mandatory pre-PR self-review for negative claims).**
   The V1-V5 Promotion Value Gate above prevents overclaiming POSITIVE results.
   The symmetric counterpart, the N1-N8 No-Go Discipline Gate, prevents
   overclaiming NEGATIVE results. Run the `no-go-discipline` skill BEFORE
   shipping any cycle artifact, PR body, source note, runner, or review verdict
   that asserts a `no_go`, `stretch_attempt_negative`, `bounded_with_named_walls`,
   or derived-no-go-boundary result. Answer N1-N8 IN WRITING, and LAND the
   answers in the PR as a committed artifact the audit lane can bind: a
   `## No-Go Discipline Gate` section in the source note itself, or a
   committed `NO_GO_DISCIPLINE_CHECKLIST.md` that the note links. The PR body
   is not a landing surface, and neither is the branch-local
   `CLAIM_STATUS_CERTIFICATE.md` — keep the cycle's copy there as loop state
   and copy it into the PR body as a courtesy, but review-loop's salvage pass
   strips claim-status certificates, handoffs, and campaign state out of a
   salvage slice, so only the source note or its linked sidecar survives as
   the record. The second required landing artifact is the
   N5 execution certificate in the primary runner's cached stdout, one
   substantive line each for `per_element:`, `per_site:`, `per_mode:`,
   `per_block:`, and `lattice_wide:`. A packet that existed at review time and
   did not land is this repo's largest audit-invalidation class
   (`docs/ai_methodology/skills/no-go-discipline/SKILL.md` Output section;
   conformance spec section 4).

   | # | Check | Failure condition |
   |---|---|---|
   | N1 | Alternative route enumeration: name ≥5 distinct attack routes against the no-go, each with what it would attempt, why it fails (with retained-authority citation), and `ATTEMPTED` vs `RULED OUT BY PRIOR` marker. | Fewer than 5 distinct routes named — packet PASS is unavailable under the current schema; this count does not decide theorem validity. |
   | N2 | Wall-independence audit: pairwise table for all named walls/open conditions; collapse any wall that follows from another. | Source-note presents walls as independent when one follows from another. |
   | N3 | Hidden-wall scan: grep the proof for "we assume", "by construction", "bridge context", "naturally", "standard QFT", "registered", "canonical"; classify each hit as cited authority, hidden condition, or non-load-bearing context. | Any hidden condition found that should have been promoted to an explicit wall. |
   | N4 | Residual matching: for every prior no-go/wall/campaign cited as a witness, verify the residual matches exactly. Drop non-matching citations. | Witness count after dropping non-matches falls below what the claim needs. |
   | N5 | Rhetoric audit: phrases of the form "X is not a Y-fact" must be checked at per-element / per-site / per-mode / per-block / lattice-wide resolutions; narrow the phrase to the resolutions actually tested. | Over-broad phrase not verified at every named resolution. |
   | N6 | Partial-closure path scan: per `feedback_no_new_axioms.md`, a labeling-convention ratification or definition refactor is NOT a new axiom — it is the import-retirement path. Scan for existing reframings, meta-notes, controlled-vocabulary entries, or in-flight PRs that close the wall via convention. | Partial-closure path found but the no-go calls it "new axiom required." |
   | N7 | Steelman: write the strongest possible one-paragraph argument AGAINST your own no-go, in hostile-reviewer voice, citing the strongest counter-authority. | A convincing steelman can be written — the no-go is premature; demote and ship the steelman as next cycle's target. |
   | N8 | Cross-cycle echo: search `NO_GO_LEDGER.md` and `docs/` for structurally similar prior walls; check if any have since been retired and by what mechanism. | A structurally similar prior wall was retired by a mechanism not considered for the current wall. |

   If any failure condition is hit, demote to one of: `partial-attempt-with-named-untested-routes`,
   `partial-narrowing`, `bounded-with-corrected-wall-count`, or
   `stretch-attempt-with-honest-residual`. Record the failing checklist items
   in `NO_GO_LEDGER.md`. Do not weaken the gate by lowering the failure
   thresholds or fabricate coverage. Narrowing can repair the scientific scope
   while the packet remains incomplete; report those facts separately.

   See [`docs/ai_methodology/skills/no-go-discipline/SKILL.md`](../no-go-discipline/SKILL.md)
   for the full skill plus archetypal failure-mode case studies from the
   2026-05-10 v-scale-planck-convention campaign (three out of four cycles
   overclaimed; the case studies are the canonical examples N1-N8 is designed
   to catch).

   **Source-note hygiene as a separate, lower-volume lane.** Pattern C
   tightenings (correcting `proposed_retained` / `DERIVED` / `EXACT` author-side
   labels that conflict with the audit-lane verdict) are real housekeeping the
   audit lane wants done — but they are NOT bounded → retained promotion work.
   When invoked under `--mode source-note-hygiene`, these are allowed at a
   max of 5 per session and must NOT be conflated with retained-promotion
   campaigns. When invoked under any other mode, treat Pattern-C-shaped output
   the same as any other PR: it must pass the V1-V5 gate.
9. **Execute one major cycle.** Produce a theorem note, runner/log pair,
   import-retirement audit, literature bridge, no-go packet, or demotion
   packet. Keep edits scoped to the chosen route.
10. **Reassess search depth when stuck.** Repeated audit/no-go/blocker-isolation
   outputs trigger a check for an underexplored hard residual and a concrete
   mechanism to try. Prefer a substantive stretch attempt when one exists;
   otherwise record the search limits and pivot. See **Deep Work Rules** below.
11. **Certify status and trace.** Before committing a block, write or update
    `CLAIM_STATUS_CERTIFICATE.md` and `TRACE_GATE.md`. Demote any title,
    status line, table row, runner printout, or handoff sentence that fails
    the claim-type certificate or overstates trace reachability.
12. **Checkpoint.** Update `STATE.yaml`, `TRACE_GATE.md`, and `HANDOFF.md`
   at least every checkpoint interval, before long scripts, after long
   scripts, and before any authorized campaign stop.
13. **Check artifacts at milestones.** Apply the relevant `physics-claim-reviewer`
   checks and review-loop conformance requirements to the author artifact.
   `--no-review-loop` may skip this optional milestone pass; required pre-PR
   conformance and later independent review still apply.
   Record findings in branch-local `REVIEW_HISTORY.md` and `HANDOFF.md`; do not
   update live review queues, land, or run the independent audit. A local
   `pass`, `demote`, or `block` is an author check, never an independent review
   receipt. Fix, narrow, or checkpoint incomplete work before requesting review.
   The later fresh review-loop owns the PR's review and any authorized landing.
14. **Close the cycle honestly.** Use the narrowest honest status inside the
    branch artifacts: candidate retained-grade only when the certificate names
    an audit-ready `claim_type`; otherwise exact support, bounded support,
    open, no-go, reject, or historical. Do not patch a missing
    theorem step with prose. Put
    any proposed repo-wide weaving in `HANDOFF.md` for later review and
    backpressure integration.
15. **Deliver coherent milestones.** At a milestone (or review-ready block in
    block mode), run the conformance gate in Science Delivery And PR Policy against
    `docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` and fix what it
    catches, then open or prepare the coherent PR unless `--no-pr` was supplied.
    Record failed delivery in `PR_BACKLOG.md`. Between milestones, commit useful
    coherent work and checkpoint incomplete work without forcing a PR; continue
    discovery while a useful route and authorized budget remain.
16. **Continue the campaign or stop.** After PR/backlog handling, if runtime
    remains and the current lane is blocked or closed, pick the next
    `OPPORTUNITY_QUEUE.md` item and continue. Stop the whole campaign only
    when runtime/max cycles expires, the target status is genuinely achieved
    and no further campaign target was requested, or the queue has been freshly
    scanned and every viable opportunity is blocked by human judgment/tooling.
    In campaign mode, even successful retained-grade proposal of one target is
    a checkpoint, not a stop, unless no further target was requested or no
    viable next opportunity exists.

## Deep Work Rules

The loop must not stop merely because audit-grade routes are easy and hard
routes are risky.

- **Search-depth checkpoint:** two consecutive cycles dominated by no-go,
  demotion, dependency firewall, or blocker isolation are a planning signal to
  reassess useful hard routes. They are not a quota requiring a nominal stretch
  attempt or an affirmative result. Try a concrete new mechanism when available;
  otherwise record why it is exhausted and pivot to useful independent work.
- **Evidence-value pivot:** after a stretch attempt and one no-go/support
  cycle on the same lane, campaign mode must check the opportunity queue and
  prefer a different unresolved target unless the current lane has a concrete
  next route with higher expected evidential value for the user's objective.
- **Stretch attempt:** choose one blocker from `STATE.yaml` or `HANDOFF.md` and
  allocate a `--deep-block` interval for sustained work from the allowed premises.
  Continue while the next step can add evidence; a decisive result or exhausted
  mechanism may justify an earlier checkpoint and pivot. A valid output may be partial structure,
  a sharper obstruction, a falsified premise, or a worked failed derivation
  with the exact load-bearing wall named.
- **First-principles reset:** before the stretch attempt, write the minimal
  allowed premise set (`A_min`: Lattice, Qubit, Admissibility, Record), the approved
  primitive set from `docs/audit/data/axiom_premise_nodes.json`, and
  forbidden imports. The attempt must not
  rely on observed target values, fitted selectors, or literature as hidden
  proof inputs. `A_min` is the minimum axiom set, NOT a license to add
  axioms or framework primitives — extending either governance surface is
  forbidden in physics-loop work; see the no-new-axiom/no-new-primitive rule
  above. Counterfactual-pass output (see
  references/assumption-import-audit.md) is a useful stretch input
  here.
- **Stuck fan-out:** before declaring "no route passes the gate", search for
  materially distinct attack frames; 3-5 is a planning target when that many
  useful routes exist, not a required count. Do not invent families or repeat
  equivalent attempts to fill it. If the active tool policy and user
  authorization allow parallel agents, run them in parallel; otherwise emulate
  the fan-out sequentially in separate notes/sections. Give early passes
  neutral route-local briefs without the favored approach or other passes'
  conclusions. Require concrete lemmas, constructions, equations, falsifiers,
  or exact missing obligations; synthesize only after the independent passes
  expose their real strengths and gaps.
- **Equivalent-obligation block:** when a route terminates at a missing lemma
  equivalent to or stronger than the target, mark its approach family
  `blocked-equivalent` in `APPROACH_REGISTRY.md`. Do not keep assigning work to
  that family until a new invariant, construction, decomposition, premise, or
  proof mechanism changes the obligation map.
- **Longer cadence:** checkpoint every `--checkpoint-interval`, but do not turn
  every checkpoint into a polished artifact. Protect sustained reasoning from
  unnecessary packaging; use the next scientific decision rather than elapsed
  minutes to decide when a route needs to change.
- **No shallow stop:** inspect live alternatives and underexplored mechanisms
  before declaring a route exhausted. Record the attempted work, decisive
  evidence, and search limits. Honor an explicit runtime budget by pivoting to
  useful independent work; do not busy-wait or manufacture attempts merely to
  satisfy a duration or route count. Global quality-exhaustion conditions still
  apply when no useful candidate remains.
- **No all-lane stop without queue evidence:** do not create a global stop
  marker such as `STOP_ALL_LANES_REQUESTED` unless `OPPORTUNITY_QUEUE.md` was
  refreshed in the same checkpoint and records why each viable next target is
  blocked.
- **No-churn exception:** an honest first-principles attempt with named
  obstructions is valid progress even without closure. This exception does not
  allow vague prose, unverified algebra, or unsupported status promotion.
- **Corollary-churn guard (late campaign):** the `--max-cycles` cap is a
  ceiling, not a target. After ~5 substantive cycles in a campaign, before
  launching each new cycle, name the new load-bearing premise, named
  residual, stretch target, or synthesis insight that this cycle introduces
  beyond what already-landed campaign cycles imply. If the answer is "none —
  it's a corollary of cycle N applied to a different label," do not
  launch the cycle. Pivot to a fresh lane, attempt a stretch on a hard
  residual not yet attempted, or stop the campaign. A passing runner that
  verifies arithmetic Python already implies (e.g. `2/3 + 2/3 - 1/3 = 1`) is
  not a derivation; it is repackaging. PRs at this density are blocked by
  Content Integrity policy and will be closed as churn even if individually
  technically correct.

## Cluster-Cap Evaluator

The cluster-cap rule (see Stop Conditions) is JUDGMENT-BASED, not a hard
ceiling. After 2 PRs are open in a single parent-row family within one
campaign, the loop must run a cluster-cap evaluation BEFORE opening PR
#N for any N >= 3 in that cluster. Use a separate evaluator agent only
when the active tool policy and user authorization allow it; otherwise
the loop agent applies the same evaluator brief locally and records the
judgment in `HANDOFF.md` or `PR_BACKLOG.md`. The evaluator's verdict
gates only the PR opening — science work continues regardless.

### Evaluator brief

The evaluator is either a separate research agent, when available, or
the current loop agent running an isolated local pass with this brief:

> You are a cluster-cap evaluator for a physics-loop campaign. The
> campaign has already opened {N-1} PRs in the parent-row family
> `{family_pattern}`. The campaign now proposes opening PR #{N} for
> {block_summary}. Your job: decide if this proposed PR represents
> genuinely new content warranting audit-lane review, OR is corollary
> churn / review-burden inflation that should be backlogged.
>
> Read the proposed PR's deliverable note + paired runner output (if
> any). Apply the project's **content-integrity criteria**:
>
> 1. **New load-bearing premise.** Does the proposed PR introduce a
>    structural premise (theorem, derivation chain, no-go, named
>    obstruction, numerical artifact) NOT present in the prior {N-1}
>    PRs of this cluster?
> 2. **Distinct claim type.** Is the proposed PR a different *kind* of
>    artifact (positive theorem vs no-go vs exploration vs numerical
>    comparator) than the prior cluster PRs, or just another instance
>    of the same kind?
> 3. **Independent reviewability.** Can the audit lane review this PR
>    on its own merits, or does its content essentially restate what
>    a single combined PR for the cluster would already cover?
> 4. **Marginal review value.** Is the per-PR review effort justified
>    by the per-PR content delta, or would the audit lane be better
>    served by a single combined PR (or commits-only into a future
>    campaign)?
>
> Output a one-line verdict: `OPEN` (proposed PR is genuinely new and
> should be opened) or `BACKLOG` (content is real but should go to
> `PR_BACKLOG.md` for a future campaign or combined PR). Justify in
> ~200-400 words. Do NOT consider the audit verdict — only the PR
> opening decision. The evaluator does NOT decide audit outcomes.

### Default behavior

If the deliverable note, paired runner output, or local review context is
unavailable enough that the evaluator cannot make the judgment, default
to `BACKLOG` for PRs N >= 3 — fail-closed on the cap rather than
fail-open. The science work still continues; the commit lands on the
loop branch and is recorded in `PR_BACKLOG.md`.

### Anti-patterns (evaluator should reject)

- "Apply theorem X (just landed in PR N-1) to label Y" — relabeling
- "Same matrix structure, different physical interpretation" —
  reframing not deriving
- "Sympy-exact verification of the existing primary runner's identities"
  when the runner already exists
- "Pattern A narrow rescope of the algebraic core" — creates audit
  row but no closer derivation

### Patterns the evaluator should approve

- A no-go theorem that retires a route the prior PRs assumed
- A numerical artifact (NEW computation) under a different action /
  geometry / coupling
- A structural finding orthogonal to the prior cluster PRs (e.g.
  gauge-group exploration when prior PRs were action-form)
- An exact closed-form derivation when prior PRs derived only inputs

### When the evaluator is moot

If the campaign has runtime and queue-budget but the evaluator says
`BACKLOG` for every remaining queued candidate, that is a stop signal
(corollary exhaustion). Update `HANDOFF.md` accordingly.

## Literature

Use literature only when the user passes `--literature` or the route requires a
known theorem/experimental comparator. Prefer primary sources and stable math
references. Any literature value, theorem, or convention must be entered in the
assumption/import ledger with its role: bridge, comparator, explicit convention,
or non-derivation context. See
[`references/literature-bridge-protocol.md`](references/literature-bridge-protocol.md).

## Long-Running Execution

For unattended runs, follow
[`references/long-running-execution.md`](references/long-running-execution.md).
In short:

- ask for runtime if absent;
- avoid mid-run questions;
- checkpoint enough state that another agent can resume;
- refresh the lock before it expires;
- continue to the next ranked opportunity when one lane blocks and runtime
  remains;
- stop cleanly only when runtime, max cycles, global queue exhaustion, or a
  global safety/tooling condition dictates;
- push only dedicated science campaign/block branches;
- open or prepare PRs at review-ready milestones, or at review-ready block
  closures when `--delivery block` was requested;
- never push science work to `main`.

## Stop Conditions

Stop and write a clear `HANDOFF.md` when:

- runtime or max cycles is reached;
- no route in the refreshed opportunity queue or active approach-family
  registry passes the dramatic-step gate **after** the Deep Work Rules and any
  applicable theorem-strength gap tests have been satisfied for the target;
- **corollary exhaustion**: every remaining ranked opportunity would produce
  only a one-step algebraic corollary of an already-landed campaign cycle
  with no new load-bearing premise. This is a real stop condition, not a
  reason to fill the cycle cap with thin restatements. The campaign's
  substantive ground is covered when the highest-value remaining moves are
  "apply cycle N's exact-support theorem to a different label";
- **value-gate exhaustion**: every remaining ranked opportunity would fail
  V1-V5 of the Promotion Value Gate (workflow step 8). If the only PRs the
  campaign can produce are textbook re-verifications, near-tautological
  rescopes, or one-step variants of landed cycles, the campaign must stop
  rather than fill the cycle cap;
- **(no volume cap)**: there is NO fixed PR-count cap per campaign or per
  day (owner decision 2026-06-11; the former 5-PRs-per-24-hour volume cap
  is removed). PR volume is gated by CONTENT, not by a counter: every PR
  must pass the V1-V5 Promotion Value Gate, negative claims must pass
  N1-N8, and the judgment-based cluster-cap evaluator applies from the
  3rd PR in a parent-row family. A campaign stops on quality-gate
  exhaustion (the two conditions above), never on a PR count;
- **cluster cap evaluator triggered**: at the 3rd and every subsequent
  PR in a single parent-row family (`koide_*`, `dm_neutrino_*`,
  `gauge_vacuum_plaquette_*`, `ckm_*_2026-04-25`, `bridge_gap_*`, etc.)
  per campaign, BEFORE opening that PR, the loop must run the
  cluster-cap evaluation described above to decide whether the proposed
  PR is genuinely new content warranting audit-lane review, OR is
  corollary churn / review-burden inflation that should be backlogged.
  Use a separate evaluator agent only when the active tool policy and
  user authorization allow it; otherwise run the same evaluator brief
  locally. The cap is JUDGMENT-BASED, not a hard 2-PR ceiling. The
  evaluator's verdict gates only the PR opening — science work
  continues either way (commits-only into the loop branch, recorded in
  `PR_BACKLOG.md` if the evaluator says "backlog"). Past N=2 in a
  cluster the burden is on the proposed PR to demonstrate non-churn
  content, not on the cap to be lifted;
- the worktree changes externally in a way that affects the route;
- the requested target status is honestly achieved and the user did not ask for
  a continuing campaign;
- required core tooling for every viable queued route is unavailable.

Do not stop solely because review-loop finds a blocker, retained certification
fails, PR creation fails, or one lane needs human science judgment. Demote or
backlog that block and pivot.

When stopping for corollary exhaustion, name in `HANDOFF.md` the highest-blast-
radius unattempted hard residual so the next campaign can resume on fresh
ground rather than re-mining the already-covered surface.

## Final Report

Report:

- loop slug and target;
- delivery mode, milestones reached, and provisional dependencies awaiting
  focused independent checks or formal audit;
- remote science branch;
- runtime used and cycles completed;
- scientific evidence gained: strongest proved result, counterexample,
  discriminator, import retired, or uncertainty reduced, with exact paths;
- claim-state movement achieved, separating author proposals, landed work,
  independent review, and audit-ratified status;
- trace-gate classification and whether the artifact reaches a known blocker
  or is frontier-only;
- imports retired or newly exposed;
- mathematical approach families explored and underexplored;
- strongest rigorously proved lemma plus the exact remaining proof obligation
  and its strength relation to the target;
- artifacts created and checks run;
- review-loop findings and disposition;
- commits and PRs created, if any;
- PRs that could not be opened, with exact recovery commands;
- remaining Nature-grade blockers;
- exact next action from `HANDOFF.md`.

Do not claim Nature-grade closure unless the assumptions/import ledger,
decisive artifact, and review-loop disposition all support it.
