---
name: physics-loop
description: Use when an LLM agent needs to plan, launch, resume, or package a long-running theoretical-physics loop on a major hard open lane/problem, with repo grounding, assumption/import audits, no-go memory, deep first-principles stretch attempts, stuck fan-out, unattended checkpoints, review-loop backpressure, and one review PR per science block.
---

# Physics Loop

## Skill Freshness

Before applying this skill, perform the repo skill freshness check described in
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`. If a newer version of
this `SKILL.md` exists on `origin/main`, follow that version for the current
task.

Run a stateful theoretical-physics loop that can make a major lane move:
retire a load-bearing import, close an exact support gate, prove a useful
no-go, add a decisive artifact, or isolate the remaining Nature-grade blocker.

This skill is not a bigger `/autopilot` and not a factory for easy audit
artifacts. It is a claim-state machine for hard physics. It must spend real
time on named hard residuals before a route can be declared blocked or the
campaign can end, and it must leave reviewable PRs for the backlog.

When launched for a long unattended run, the default posture is a **campaign**:
keep working until the runtime or max-cycle budget is exhausted. If one route
or lane hits an honest stop, checkpoint it, select the next ranked science
opportunity from the repo, and continue. Do not stop the whole campaign merely
because the first target ends in a no-go, support-only boundary, or
human-judgment blocker.

For a request like "run for 12 hours unattended", treat the runtime as a work
budget, not a maximum that can be abandoned after the first clean stop. The
agent should spend the allotted time unless a global safety/tooling condition
makes safe continuation impossible. Per-route blockers, review demotions,
dirty PRs, missing retained proof, unavailable optional literature, or failed
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
- `--deep-block DURATION`: optional sustained hard-problem block, default
  `90m`;
- `--no-pr`: do not open review PRs;
- `--no-review-loop`: skip milestone `/review-loop` only if the user asked;
- `--no-commit`: do not create commits.

If `--runtime` is absent and the user wants execution, ask how long to run
before launching unattended work. Do not assume a fixed default. If the user
only asks for planning, produce the plan without asking for runtime.

Infer `--mode campaign` when the user asks for an overnight, unattended,
long-running, or 12-hour run, even if the user says only `run`. A campaign
keeps selecting science blocks until the runtime/max-cycle budget or global
queue exhaustion condition is reached.

## Science Delivery And PR Policy

For science loops, execute on clean remote branches and open review PRs for
each coherent block. Do not merge those PRs and do not push science work
directly to `main`.
No supervisor prompt may override this by telling the worker not to open PRs
unless the user explicitly supplied `--no-pr`.

- Start science execution from current `origin/main` after `git fetch origin`.
- Use a dedicated branch namespace such as `physics-loop/<slug>-YYYYMMDD`.
- If the current worktree is dirty or not disposable, create a clean worktree
  from `origin/main` instead of mixing loop output with other changes.
- Treat each coherent major cycle as a **science block**. Prefer one branch per
  science block:
  `physics-loop/<slug>-blockNN-YYYYMMDD`.
- If a block depends on prior unmerged block output, create a stacked PR whose
  base is the prior block branch. If independent, base it on `main`.
- Commit coherent science artifacts to the block branch and push it to
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
- At each science-block closure, unless `--no-pr` was supplied, open one review
  PR for that block before pivoting to the next opportunity. Use
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
git restore --source=HEAD --staged --worktree -- \
    docs/audit/data/ \
    docs/audit/AUDIT_QUEUE.md \
    docs/audit/MISSING_DERIVATION_PROMPTS.md \
    'docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md' \
    docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md
git clean -fd -- docs/audit/data/
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

Use `STATE.yaml` as the resume surface: current goal, target status, runtime,
cycle/block count, active route, approach-family coverage, strongest unresolved
proof obligation, hard residual being attacked, files touched, open imports,
no-go routes, trace-gate classification, review findings, PR status, next exact
action, and stop condition.

For theorem, multi-step bridge, or hard-reduction targets, write the exact
target contract in `GOAL.md` and maintain `APPROACH_REGISTRY.md` using
[`references/proof-search-governance.md`](references/proof-search-governance.md).
Keep mathematical approach families separate from artifact types recorded in
`ROUTE_PORTFOLIO.md`.

Use `OPPORTUNITY_QUEUE.md` in campaign mode. It must rank candidate science
targets by:

- retained-positive probability;
- missing-import count;
- runner/test availability;
- review landability;
- blast radius and branch size;
- whether the target is independent of the just-blocked lane.

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
branch-local author status. A physics-loop PR, note, runner, or status line may
set `target_claim_type: positive_theorem`, `bounded_theorem`, or `no_go` only
after all of these are true:

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
7. Review-loop disposition is `pass`; `pending`, `passed_with_notes`,
   `demote`, or `block` cannot certify a retained-grade proposal.
8. The PR body and handoff explicitly say independent audit is still required
   before the repo may treat the claim as retained-grade.

If any item fails, use `open`, `exact-support`, `bounded-support`,
`conditional-support`, `no-go`, or `demotion` instead.

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
3. commit/push/open PR or write `PR_BACKLOG.md` for the coherent block;
4. refresh `OPPORTUNITY_QUEUE.md`;
5. choose the next highest-ranked retained-positive opportunity and continue.

Global stop is allowed only when:

- runtime or max cycles is exhausted;
- the worktree/repo changes externally in a way that makes safe continuation
  impossible;
- required core tooling for all viable routes is unavailable;
- a lock conflict means another active worker owns the same repo/task and no
  clean independent worktree can be created;
- the refreshed opportunity queue proves every viable target is blocked and no
  independent retained-positive candidate remains.

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
   Prefer retained-positive opportunities over more audit churn after one or
   two no-go/support-only cycles.
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
   | V1 | What SPECIFIC verdict-identified obstruction does this PR close? | Quote the exact obstruction text from the parent row's `verdict_rationale`. "The upstream is unratified" does NOT qualify — that's a dependency-chain issue, not a derivation gap. |
   | V2 | What NEW derivation does this PR contain that the audit lane doesn't already have, and **what repo search did you run to establish that** (step 2)? | One paragraph describing genuinely new content. "Sympy-exact verification of the existing primary runner's identities" is NOT new derivation. "Pattern A narrow rescope of the algebraic core" is NOT new derivation if the audit lane already understands the algebra; it just creates a new audit-pending row with no closer derivation. Quote the step-2 prior-art search commit, commands, hits, and matched-hit classifications; an unevidenced novelty claim fails this question. |
   | V3 | Could the audit lane already complete this derivation from existing retained primitives + standard math machinery (Schur complement, cube-root-of-unity arithmetic, Casimir formulas, Pauli matrix algebra, etc.)? | "No" — explain why the framework's retained primitives are necessary. If "yes", the cycle is performative and the PR must not be opened. |
   | V4 | Is the marginal content non-trivial (not a textbook identity, not a definition restated)? | "Yes" with one-sentence justification. Examples that fail: "real shifts don't change imaginary parts", "(1/sqrt(N)) * I has matrix elements 1/sqrt(N)", "scaling by mu preserves slope". |
   | V5 | Is this a one-step variant of an already-landed cycle in this campaign, **or of anything already on `origin/main`**? | "No" — name the closest prior cycle and explain the structural distinction. "Same matrix structure, different physical interpretation" is NOT a structural distinction; it's relabeling. Refresh and check `origin/main`, not only the campaign's own cycles, and record the searched commit — a landed note you did not know about still counts, and a more general landed version outranks your special case. |

   A `frontier_discovery` route satisfies this gate only if it introduces a
   genuinely new structure, falsifier, or hard-premise test; it must not be
   sold as closure.

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
   | N1 | Alternative route enumeration: name ≥5 distinct attack routes against the no-go, each with what it would attempt, why it fails (with retained-authority citation), and `ATTEMPTED` vs `RULED OUT BY PRIOR` marker. | Fewer than 5 distinct routes named — the no-go is premature. |
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
   thresholds — a correctly scoped narrow no-go passes N1-N8 by being narrow.

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
10. **Run deep-work pressure when stuck.** If the last two cycles were
   audit/no-go/blocker-isolation outputs, or if no easy route passes the gate,
   run a stretch-attempt cycle before declaring the active route blocked. See
   **Deep Work Rules** below.
11. **Certify status and trace.** Before committing a block, write or update
    `CLAIM_STATUS_CERTIFICATE.md` and `TRACE_GATE.md`. Demote any title,
    status line, table row, runner printout, or handoff sentence that fails
    the claim-type certificate or overstates trace reachability.
12. **Checkpoint.** Update `STATE.yaml`, `TRACE_GATE.md`, and `HANDOFF.md`
   at least every checkpoint interval, before long scripts, after long
   scripts, and before any authorized campaign stop.
13. **Review at milestones.** After each major artifact, run the `review-loop`
   skill unless disabled. In science-run mode, record findings in branch-local
   `REVIEW_HISTORY.md` and `HANDOFF.md`; do not update the live active review
   queue or other repo-wide authority surfaces before the later review and
   integration process. The local disposition must be one of `pass`, `demote`,
   or `block`; `self-review pending` is not enough to push a PR. Either fix
   locally, demote locally, archive locally, or select a new route.
14. **Close the cycle honestly.** Use the narrowest honest status inside the
    branch artifacts: candidate retained-grade only when the certificate names
    an audit-ready `claim_type`; otherwise exact support, bounded support,
    open, no-go, reject, or historical. Do not patch a missing
    theorem step with prose. Put
    any proposed repo-wide weaving in `HANDOFF.md` for later review and
    backpressure integration.
15. **Open review PRs.** At each block closure, run the conformance gate in
    Science Delivery And PR Policy against
    `docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` and fix what it
    catches, then open or prepare one PR for the coherent science block unless
    `--no-pr` was supplied. In campaign mode, a missing PR must become
    `PR_BACKLOG.md` and the campaign must continue if runtime remains.
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

- **Audit quota:** after two consecutive cycles whose main output is a no-go,
  demotion, dependency firewall, or blocker-isolation artifact, the next cycle
  must be a stretch attempt on a named hard residual.
- **Positive-retention pivot:** after a stretch attempt and one no-go/support
  cycle on the same lane, campaign mode must check the opportunity queue and
  prefer a different retained-positive candidate unless the current lane has a
  concrete next route with higher retained-positive probability.
- **Stretch attempt:** choose one blocker from `STATE.yaml` or `HANDOFF.md` and
  work it from minimal repo primitives for at least one `--deep-block`
  interval when runtime allows. A valid output may be partial structure,
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
- **Stuck fan-out:** before declaring "no route passes the gate", generate
  3-5 orthogonal premises/attack frames. If the active tool policy and user
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
  every checkpoint into a polished artifact. Sustained 90-120 minute hard
  attempts are preferred over several shallow audit cycles.
- **No shallow stop:** after the most recent blocker, do not stop until at
  least one stretch attempt and one stuck fan-out synthesis have been recorded,
  unless runtime is exhausted or required core tooling fails for every viable
  queued route.
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
- push only dedicated science block branches;
- open or prepare one review PR per science block at block closure;
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
- remote science branch;
- runtime used and cycles completed;
- claim-state movement achieved;
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
