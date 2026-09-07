---
name: audit-loop
description: Run the cl3-lattice-framework audit lane as an adversarial Nature-grade claim auditor. Use when the user asks to audit scoped retained-grade science, process the audit backlog/queue, run an auditor loop, update audit results, apply audit verdicts, or push claim-audit outcomes directly to main.
---

# Audit Loop

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Use this skill to audit one claim at a time from the repository audit queue and land the audit result. The standard is hostile field review: the claim must survive an adversarial physicist looking for hidden imports, circular logic, definition-as-derivation, stale numerics, misidentified observables, and overstated closure.

## Scope and research cadence

An explicit audit request invokes this lane. Mentioning audit in a science,
planning, or process-review task does not. The default research cadence in
`docs/ai_methodology/SCIENCE_WORKFLOW.md` is continuous discovery with selective
checks and milestone audits. Formal audit of every provisional leaf is not a
prerequisite for further work on a candidate branch. An explicit backlog drain
retains the full drain behavior below.

Resolve the user's target scope before selecting an execution path. A named
claim, commit, PR, source set, milestone, lane, or candidate file is a bounded
request even when it contains no literal claim ID. Use the bounded path below;
prioritizing such targets inside a global drain does not respect that boundary.
Keep queues and checkpoints durable so discovery can continue independently of
audit throughput. Neither speed nor agreement with an earlier reviewer is a
verdict criterion. Do not claim an unexamined candidate is retained.

Use the standard invocation-bound runner/application path for automated
verdicts. Legacy/manual `apply_audit.py` calls do not universally enforce the
same transport provenance for ordinary rows; do not describe a manual apply as
authenticated runner evidence. A new automated workflow must use the standard
path rather than treating that compatibility route as a shortcut.

### Bounded audit requests

1. Pin the requested commit/PR/source revision and the canonical main snapshot
   used for selection. Verify Git containment and map the requested landed
   source paths to exact canonical ledger claim IDs. Record that allowlist and
   the source revisions in the session handoff. For a milestone or lane name,
   resolve its actual source set; a title match alone is not a claim mapping.
   PR metadata may locate sources but must not enter the restricted auditor
   packet as scientific evidence. Unlanded candidate work is a source-review
   handoff, not an applied main audit.
2. Include critical dependency IDs only when the request includes them, using
   the actual dependency graph and stated scientific obligation. Record why
   each dependency belongs. Do not silently expand a bounded request to every
   ancestor, descendant, queue row, or future milestone. If the source mapping
   or dependency boundary is ambiguous, ask for the missing scope and continue
   independent source mapping/readiness work or already-unambiguous authorized
   targets. An absent source or empty allowlist is a scoped blocker, never
   permission to fall back to a global queue.
3. Use supported invocation-bound commands with a nonempty explicit selector:
   - Eligible development-tier claims:
     `python3 docs/audit/scripts/orchestrate_audit_batch.py --claims 'id1,id2' --max-workers 4`.
   - Required judicial confirmation for selected claims:
     `python3 docs/audit/scripts/orchestrate_judicial_panel.py --claims 'id1,id2' --max-workers 4`.
     Pass only the in-scope disagreement/reseat IDs. Omission of `--claims`
     selects unrelated disagreements and is forbidden in this mode.
   - A selected forensic claim uses the authenticated single-claim runner:
     `python3 scripts/codex_audit_runner.py --claim-id 'id1' --push-mode per-verdict`.
     Preserve the forensic tier's packet, evidence, timeout and completion
     requirements. When the claim comes from dispatch or cascade selection,
     retain the matching `--from-dispatch` or `--from-reaudit-candidates`
     provenance selector. Do not force a forensic or unsupported claim type
     into the development batch, bypass eligibility, or use legacy/manual
     apply to evade a missing supported transport path.
4. Supervise the bounded batch/panel/resume sequence explicitly. Required
   independent second seats, judicial panels and reseats stay within the
   allowlist and retain all existing evidence, independence, application and
   transaction gates. A batch exit or skipped row does not establish audit
   completion. Revalidate the remaining selected IDs, source fingerprints and
   eligibility before each continuation; never substitute new queue members.
   If a requested exact source revision has changed on main, report the drift
   and resolve the requested version before judging different bytes.
5. Stop when the selected set is complete or its remaining rows need user,
   source, evidence or tooling action; report completed, pending and blocked
   IDs separately. A blocker outside the selected dependency set is a named
   follow-up, not authority to expand the audit. Continue useful work within
   scope while possible. If no available invocation-bound path can enforce
   the requested scope or support an eligible claim, report that concrete
   limitation and preserve the handoff.

`orchestrate_audit_loop.py` has no top-level claim-set selector. Its lane and
runtime options do not confine every dispatch, cascade, panel and forensic
phase to a milestone. Do not launch it for a bounded target request. All later
queue-fallthrough, retry, recovery and "continue unrelated rows" instructions
remain inside the frozen allowlist in bounded mode. Unrestricted-drain commands
and selection snippets below apply only to a truly unscoped invocation or an
explicit full-backlog request, subject to any additional user constraints.

## Non-Negotiables

- Audit; do not repair the science. If a claim fails, record a physicist-actionable failure handoff so someone else can fix it.
- Work one claim per commit. This keeps audit verdicts reversible and reviewable.
- Prefer a clean temporary worktree based on `origin/main`. Do not use a dirty shared checkout for audit commits.
- Push routine audit commits directly to `main`. This project has authorized direct-main audit operation for ordinary `apply_audit.py`-accepted verdicts; do not open PRs for routine clean, conditional, renaming, decoration, numerical-match, or non-controversial failed verdicts.
- Do not smuggle tooling or pipeline changes into a routine audit verdict. If an audit session produces non-generated code changes (for example an audit runner, dispatcher, queue generator, or helper-script edit), stop and route that change through review-loop as audit infrastructure before relying on it. Generated audit surfaces produced by the standard pipeline are expected; handwritten or worker-authored tooling changes are not verdicts.
- Do not read broad publication framing while judging the claim. Use the source note, one-hop cited authorities, runner, runner output, and the audit rubric.
- Preserve fresh-context integrity. Do not read prior audit rationales, previous audit entries, rendered `AUDIT_LEDGER.md` history, PR text, publication framing, or downstream summaries while judging a claim.
- Do not grant `audited_clean` unless the derivation closes without hidden premises, unsupported physical identifications, circular dependency, or tuned comparator matching.
- Treat every math-bearing claim as requiring an independent math audit before
  any verdict is applied. Check every load-bearing formula, sign, factor,
  normalization, matrix identity, optimizer objective, and expected numerical
  value against the source note and cited authorities. Use at least one route
  that does not share the runner's implementation path: manual derivation,
  symbolic/algebraic simplification, finite toy-case enumeration, independent
  recomputation, invariant/limit checks, or direct comparison to a cited
  theorem. Do not let PASS output, cached logs, or generated expected values
  substitute for this check.
- Displayed closed-form identities are part of the math audit even when they
  appear in characterization, fingerprint, signature, qualitative-support,
  or non-headline sections. Inventory every quantitative equation, table
  coefficient, ratio, projection, and prose/comment closed form of the source
  packet. A wrong displayed formula means the source is not clean as written;
  do not exempt it because the headline bound or theorem may not depend on it.
- When a coefficient multiplies a named basis object, recompute the coefficient
  in the stated normalization. This includes spherical harmonics, group
  characters, Casimirs, Gell-Mann/Pauli/projector bases, normalized
  eigenvectors, and similar named bases. Use a projection check such as
  `<f,B>/<B,B>` (or the exact algebraic equivalent) and flag convention-pairing
  errors where the coefficient and basis are individually valid only under
  different normalizations.
- Runner PASS covers only quantities the runner executes and asserts. Compare
  each displayed coefficient against actual executable checks, not comments or
  narrative in the runner. If a coefficient lives only in prose or code comments,
  or no runner assertion would fail if it were wrong, treat it as unverified
  unless the auditor independently recomputes it in the restricted packet.
- If the note and runner describe the same object with different conventions or
  normalizations, treat that as source-runner drift and do not grant
  `audited_clean` until the convention is reconciled. When a closed-form
  coefficient defect appears copied across a note family, finish the current
  verdict using only the restricted packet, then record exact sibling repair or
  re-audit targets in the handoff; do not use sibling rows as evidence for the
  target claim.
- When the independent math check fails, is incomplete, or exposes a
  runner/source mismatch, the verdict rationale must name the exact formula
  family and why the independent check does not close. Do not grant
  `audited_clean` until the expression is independently fixed and rechecked.
  If the runner is self-confirming, generates its own expected value, omits a
  sign/factor/normalization check, or a reopened issue says the runner math was
  wrong, treat the formula family as suspect and choose a non-clean verdict
  unless the restricted packet contains a valid independent repair.
- No admission class exists. `docs/audit/data/premise_decision_history.json`
  is non-authoritative history and must never satisfy or bound a dependency.
  Scientific content outside the axiom/approved-primitive foundation must be
  retained-derived or remain conditional/open.
- Apply the No-Go Discipline gate (`no-go-discipline` skill, checks N1-N8)
  before recording any verdict on a row with `claim_type: no_go`, a
  `bounded_theorem` whose source note names walls/open conditions, or an
  `audited_conditional` whose `verdict_rationale` would name walls. **Tier
  scope (owner-approved 2026-07-12):** the gate is always applied as auditor
  JUDGMENT, but the heavyweight evidence plumbing is tier-scoped -- see
  "Two-Tier Assurance" below. Every incoming audit still declares
  `negative_assertion_classes`; a non-empty declaration requires the
  structured N1-N8 packet on the same terms as the output trigger (clean
  verdicts, no-go rows, forensic runs), and an empty declaration never
  bypasses the mechanical source/output triggers.
  Forensic packets (manifest-backed containment, live runner-stdout citation,
  complete index dispositions) are mandatory for `claim_type: no_go` rows,
  source paths matching the no-go-name trigger (including obstruction,
  firewall, negative-boundary, no-uniform-sign, and stretch-attempt names),
  and `AUDIT_FORENSIC_MODE=1` certification runs. Development-tier rows supply
  the N1-N8 packet as structured judgment with quoted evidence when the packet
  is required or voluntarily included; otherwise non-clean verdicts record the
  judgment in rationale prose. Any supplied packet is validated structurally.
  Negative-claim overclaims foreclose investigation paths
  permanently and require the same scrutiny as positive-claim overclaims. If
  any N1-N8 check fails on the source note, choose the more conservative
  non-clean verdict whose `verdict_rationale` reflects the honest narrower
  claim scope; do not record `audited_clean`, and do not transcribe the source
  note's inflated wall list into the ledger.
- **Vocabulary is auto-corrected, not adjudicated.** The repo's process vocabulary is canonical in [`docs/repo/controlled_vocabulary.yaml`](../../../repo/controlled_vocabulary.yaml) (design in [`VOCABULARY_HYGIENE_DESIGN.md`](../../../repo/VOCABULARY_HYGIENE_DESIGN.md)). Before writing an audit verdict, run `scripts/vocab_lint.py --fix` on the source note under audit. Routine local drift that has a non-link-aware rewrite rule, such as legacy aliases and deprecated wording, is rewritten mechanically; link-aware filename suffix migrations and F-letter finding-label migrations are reported but deferred to Cleanup-2 tooling. This is a normal commit step, never a science verdict. Record what was rewritten in the ledger row's `prose_corrections` field and set `prose_status: auto_corrected`. When `vocab_lint --fix` changed the source note, include a `pre_audit_prose_fix` envelope on the audit blob carrying `{old_hash, new_hash, prose_status, prose_corrections}` so `apply_audit.py` atomically refreshes `note_hash` before the hash-drift check. If `vocab_lint` cannot mechanically rewrite a violation (genuinely new term, link-aware rename pending, or F-letter migration pending), set `prose_status: needs_human_vocab_decision` — but **do not** translate this into a non-clean `audit_status`. Physics and prose are separate verdicts. A clean derivation with vocabulary drift lands as `(audit_status: audited_clean, prose_status: auto_corrected)`; a clean derivation that introduces a genuinely new term lands as `(audit_status: audited_clean, prose_status: needs_human_vocab_decision)`. Never assign `audited_renaming` or `audited_conditional` on prose grounds alone.
- Repo-wide axioms and explicitly approved framework primitives are accepted
  premises only when already registered in
  `docs/audit/data/axiom_premise_nodes.json`; they satisfy dependency closure
  without making downstream rows `retained_bounded`.
  <!-- BEGIN GENERATED: axiom-baseline (generate_skill_axiom_baselines.py) -->
  Generated by `docs/audit/scripts/generate_skill_axiom_baselines.py`: every
  paragraph below is extracted verbatim from the source section named in
  italics above it (whitespace re-wrapped, inline links flattened). The cited
  source file is the authority; do not hand-edit inside the markers.

  **Axiom baseline** (source: `docs/MINIMAL_AXIOMS_2026-06-29.md`; axioms:
  Lattice, Qubit, Admissibility, and Record)

  *Lattice / Physical Locality*

  Physical sites are the points of the cubic lattice `Z^3`, with
  nearest-neighbor adjacency, standard translations, and proper cubic rotations
  about each site.

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

  There is one fixed nearest-neighbor admissibility rule, covariant under
  lattice translations and proper cubic rotations.

  For each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions.

  *Reading notes (interpretive, non-governing).* (1) The distribution is
  law-level: the general substrate is the weighted-branching realization, with
  deterministic substrates as boundary realizations -- the law supplies the
  odds; the realized state supplies the pick. (2) Read with Record, the
  distribution concerns which possibility a forming record locks, conditional
  on formation at that site; it does not supply the formation site,
  probability, or rate. (3) The distribution is a probability measure on the
  local possibility domain; "available"/"admissible" denotes its support -- on
  finite menus, exactly the possibilities of nonzero probability. On a
  continuous domain, a supported exact point may have zero singleton measure;
  Record locks a supported realization.

  *Record / Fixed Reality*

  Records form.

  When present, a record locks exactly one admissible local possibility. A site
  never carries more than one record; records are permanent.

  Only records are readable. A readout value is determined by record content
  alone. A site with no record cannot be read.

  *Qualification*

  These axioms state only their named primitive content. Further physical
  structure requires a retained derivation or bridge, or explicit
  approved-primitive registration, before use as a premise. A choice not fixed
  by the supplied structure remains a named conditional or open dependency.

  A state is a configuration of records.

  A law privileges no states. Its domain is a supplied condition, and at every
  state where the condition holds it gives exactly one answer.

  *Open Gates Outside The Axioms*

  The four axioms do not close, import, or rename the framework's downstream
  open gates. In particular, the following remain outside axiom content:

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

  **Approved primitives** (registry:
  `docs/audit/data/axiom_premise_nodes.json`)

  **`scale_reference_primitive`** (source:
  `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`)

  *What This Declares*

  The framework takes exactly one dimensionful reference: a scale that converts
  the framework's lattice-natural units to physical units. The chosen reference
  is the Planck mass scale, `a^{-1} = M_Pl`.

  This is a units conversion, not a physics axiom. It carries zero
  dimensionless content: no mass ratio, coupling, mixing angle, phase,
  selector, readout bridge, or empirical fit is supplied by it. A row whose
  only otherwise non-retained dependency is this scale-reference primitive
  should not become `retained_bounded` merely for using a ruler.

  *What This Does Not Do*

  - It does not add or amend an axiom. The minimal framework baseline is the
    four named axioms: Lattice, Qubit, Admissibility, and Record.
  - It does not assert `a/l_P = 1` as a derived theorem. The self-consistency
    question that the framework's natural unit equals the Planck length remains
    a separate open gravity derivation.
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

  This is a structural statement about the regulator geometry, the
  time-direction analogue of the `LATTICE` axiom's spatial **cubic adjacency**
  `a_x = a_y = a_z`. It carries no dimensionless dynamical content: no mass
  ratio, coupling, mixing angle, phase, selector, readout bridge, or empirical
  fit is supplied by it. It is not a fourth spatial dimension, not a new
  dynamics, and not a re-axiomatization of time: the framework's time remains
  emergent and derived (the single-clock codimension-1 evolution theorem); this
  primitive fixes only the one dimensionless graining ratio relating that
  emergent time to space.

  *What This Does Not Do*

  - It does not add or amend an axiom. The minimal framework baseline is the
    four named axioms in `MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit,
    Admissibility, and Record.
  - It does not re-axiomatize time. The emergent single-clock evolution remains
    derived; this primitive normalizes only the one graining ratio `c_t / c_s`.
  - It does not supply any dimensionless dynamical quantity. No mass ratio,
    coupling, mixing angle, phase, or selector is supplied; dimensionless
    physics must derive from retained-grade framework content or remain
    conditional/open.
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

  A row may evaluate an already-defined state functional at the supplied
  realized state. A value that would change under a different law-admissible
  realized state is registered data, not derivation output.

  *What This Does Not Do*

  - It does not add or amend an axiom. The minimal framework baseline remains
    the four named axioms: Lattice, Qubit, Admissibility, and Record.
  - It does not supply a state, state-selection rule, averaging over
    alternatives, measure, weighting, probability rule, typicality claim,
    genericity claim, preferred state, default state, boundary condition,
    normalization rule, or state-contingent value.
  - It does not assert any special boundary condition on the realized history.
    A low-record or low-entropy boundary remains a separate named input,
    anchored at
    `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`.
  - It does not change any audit verdict. Audit status remains set only by the
    independent audit lane.
  <!-- END GENERATED -->
  Do not recognize, add, or imply any new axiom or new primitive without
  explicit user approval and a reviewed registry/policy update.
- Before treating any premise as an import, missing dependency, no-go wall, or
  bounded-status source, perform
  `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. If the only
  otherwise non-retained dependency is the registered
  `scale_reference_primitive`, do not bound the row for using the Planck
  scale reference; if it is the registered `kinetic_isotropy_primitive`, do not
  bound the row for using `c_t = c_s` as structural kinetic-form isotropy; if it
  is the registered `realized_state_primitive`, do not bound the row for
  pointwise evaluation at the supplied realized state (bounding, where due,
  comes from the supplied state data actually quoted, not from the primitive).
  Audit only the extra content actually claimed.
- If the author family appears to be Codex and the current auditor is Codex, do not let the current context self-ratify a clean result. Restart the claim in a distinct restricted-input sub-agent when sub-agents are available, and record a clean result only as `independence: fresh_context` with a distinct `auditor` identity if `apply_audit.py` accepts it. If no sub-agent is available, skip clean application and report that a non-Codex, human, or fresh-context agent audit is required.
- Do not stop after producing an audit JSON unless the user explicitly asks for a dry run, no-apply, or JSON-only result. If the user asks to "return JSON" as part of an audit-loop task, treat that as the required verdict format and still apply, verify, commit, and push the audit result according to this skill.

## Two-Tier Assurance (owner-approved 2026-07-12)

The lane runs two tiers; know which one your row is in before building the
packet.

- **Development tier (default).** Verdicts bind to claim content (note,
  runner, premise hashes) and survive unrelated repository growth.
  Independent cross-family re-derivation at xhigh and two-pass
  cross-confirmation on critical rows are unchanged and remain the heart of
  the audit. When walls are named, answer N1-N8 in the structured packet when
  it is required or voluntarily included, and otherwise in rationale prose.
  A supplied packet is validated structurally (no manifest-containment scans,
  no live-stdout precondition, no full-universe dispositions, no transport
  envelope). The structured packet is MANDATORY
  for `audited_clean` verdicts that name walls (and always on no-go rows);
  for non-clean verdicts on non-no-go rows it is optional — state the
  wall-naming judgment in `verdict_rationale` prose instead, since those
  verdicts re-enter the repair queue and foreclose nothing. A supplied
  packet is validated in full either way.
- **Forensic tier.** Mandatory for `claim_type: no_go` rows and source paths
  matching the no-go-name trigger (including obstruction, firewall,
  negative-boundary, no-uniform-sign, and stretch-attempt names); forced
  lane-wide by `AUDIT_FORENSIC_MODE=1` (used for freeze/certification runs
  against a pinned commit). Requires the full
  heavyweight regime: orchestrator evidence transport
  (`CODEX_AUDIT_TRUSTED_EVIDENCE_MANIFEST` envelope: schema
  `codex_audit_trusted_manifest_v1`, matching `claim_id` and 32-hex
  `audit_invocation_id`, timezone-aware `issued_at` within 2 hours,
  `entries` = the rendered manifest), verbatim-contained N1 route evidence,
  ATTEMPTED routes citing a live entry whose `roles` include
  `"runner_stdout"`, complete
  N6/N8 dispositions against the capped indexes (bulk scan kinds carry
  authenticated omitted-tail summaries in `candidate_truncation`), and
  snapshot authentication. Dynamic-index growth after packet authentication
  is re-audit signal (`no_go_index_growth_targets.json`), never retroactive
  invalidation.

**Rolling lane certification.** `docs/audit/data/lane_certification.json`
(pipeline step 7b) reports, per flagship lane, whether the root claim's full
transitive dependency closure is chain-satisfying at the current state:
retained-grade rows, retained-parent decorations, registered accepted
premises, and permitted metadata context satisfy the marker. Treat a lane's
`blocking` list as a high-value targeting input alongside the dispatch and
cascade queues: draining those rows moves a flagship lane toward
certification.

## Default Entry: Do The Right Thing, In Parallel (owner-directed 2026-07-17)

A bare, argument-less audit-loop invocation retains the standing full-backlog
drain contract. The same path serves an explicit full-backlog request. Any
named commit, PR, source set, milestone, lane or other target constraint instead
uses the bounded audit path above, even without literal claim IDs. Mentioning
this skill during a process review invokes neither path. For a truly unscoped
or explicitly full-backlog audit, the default session is:

1. Setup per "Setup For Each Session" below (fetch, clean worktree,
   pipeline, strict lint).
2. Launch the panel-aware top-level drainer:

   ```bash
   python3 docs/audit/scripts/orchestrate_audit_loop.py --max-workers 4
   ```

   The canonical command has no wall-clock limit and keeps draining until its
   governed fixed point or a verified resource/integrity blocker. When the
   operator explicitly requests a runtime-limited full-backlog campaign, add
   `--max-runtime-hours 12` (or the requested duration). The limit is checked
   only between completed batch/panel/canary phases, so it never interrupts a
   claim transaction, pipeline, lint, or push. The bound must be finite and
   non-negative. If a batch crosses the deadline, its mandatory post-batch
   panel sweep still runs once before the bounded stop. A hard result remains
   hard, and a typed temporary-service result from batch, panel, or forensic
   canary preserves that status when the bound prevents its next retry.

   This command owns the complete control loop: drain authenticated targeted
   dispatch and cascade re-audit sources, finish pending judicial work, drain
   configured development lanes in order, drain every other eligible
   development row, immediately panel every fresh cross-seat disagreement,
   resume after the panel lands, then advance the forensic source one
   validated row at a time. Every landed forensic result returns through the
   development phases because it may unblock dependencies. Raise toward 6
   workers only in a quiet pool per the budget below. The drainer generates a
   unique session id when `AUDIT_WORKER_ID` / `--worker-id` is omitted. The id
   is only an ordering hint: it disperses independent clones across the queue
   without assigning an exclusive shard. The supervisor holds the clone-wide
   audit lock for the complete campaign and hands that lock to its batch/panel
   children. It runs the panel sweep after every batch termination before
   propagating any unrelated hard batch failure, so a mixed result cannot
   strand a valid judicial handoff.
   Keep the printed campaign artifact directory. It is the durable operational
   record for schema, compute, blocked-reentry, and safely rolled-back
   transaction exclusions; it does not carry scientific authority.
   A bounded JSON/schema rejection from a forensic row is also claim-local:
   the supervisor preserves the complete `forensic-canary-*.jsonl` run log,
   appends a strict `schema_invalid_quarantined` record, reports that the row
   did not land, and advances to the next non-excluded forensic row. Unknown
   execution failures and apply,
   propagation, or push failures still fail closed.
3. The full-backlog orchestrator iterates lanes from
   `docs/audit/data/lane_certification_config.json`,
   selecting entries whose generated `lane_certification.json` record still
   has blocking rows. Its `--lane` option controls configured lane phases,
   not the membership of every other phase; a lane-only request uses the
   bounded path above.

When multiple employees or Codex accounts participate, read and follow
[`references/distributed-drain.md`](references/distributed-drain.md). Every
employee runs the same command from a separate clean clone. There is no leader,
helper role, global lease, campaign ref, or terminal completion record.
Independent workers may duplicate computation; immediately before apply, the
existing current-main provenance check discards stale deliveries, and only a
fast-forward transaction may land. Each zero-work exit is a worker-local
observation, never a global certification. Confirm the backlog from a fresh
canonical status/pipeline read after all visible workers have quiesced.

Do not detach `orchestrate_audit_batch.py` as the whole unrestricted `/audit-loop`
campaign. A batch is one inner development-tier step and intentionally yields
when cross-seat disagreement appears. Only `orchestrate_audit_loop.py` owns
the automatic panel-and-resume edge; treating `judicial_panel_required` as a
terminal campaign failure is an orchestration defect.

The bounded path above supervises targeted rows without launching the global
drainer. The later single-claim judgment and application requirements still
apply; they do not authorize a legacy/manual transport shortcut.

## Progress Reports (every 15 minutes)

While a session is running, the operator surface gets a summary block at
least every 15 minutes — never silence for a long run.

- The batch drainer emits its own `== drain summary` block on that cadence
  for the whole session — a background print-only ticker covers the long
  serialized apply/pipeline/lint/push phases too (elapsed time, outcome
  counts straight from the session report, live worker seats with per-seat
  runtimes, and the dep-ready count as of the current round's start). Relay
  these to the operator surface as they appear; do not re-derive or
  editorialize the numbers.
- During phases the drainer does not cover — judicial panels, reseats, the
  forensic canary, setup/pipeline waits — the orchestrator composes the
  same cadence manually: elapsed session time, verdicts landed this session
  by type, attempts and failures with the top failure reasons verbatim,
  panel/reseat/canary state, and the current ready-row count from the audit
  queue.
- Every session ends with a final forced summary; a session that reaches
  the round loop's natural end also prints the standard batch report, and
  one that stops early still reports what landed, what failed, and what
  remains through that forced summary.

## Drain Liveness And Generated-State Recovery

- A quiet worker is bounded by the configured stall timer, and every
  read-only ordinary-auditor or judicial-judge seat is also bounded by the
  absolute `--codex-timeout-sec` deadline propagated by the top-level
  drainer. Continuous log output does not extend that absolute deadline.
  File activity resets the inactivity timer, but both inactivity and absolute
  age are measured with a monotonic clock rather than wall-clock or file-mtime
  subtraction.
  Both inactivity and absolute-age expiry terminate the complete recorded seat
  process group, reap its leader within the bounded cleanup policy, and prove
  the group absent. Failure to reap or prove absence is a global integrity stop:
  launch no later seat or post-batch panel, let any already-owned serialized
  transaction reach its rollback or push-reconciliation boundary, and then
  abort. Expiry is operational only and supplies no scientific verdict. It
  does not interrupt the serialized apply/pipeline/lint/commit/push
  transaction.
  Every supervisor phase continues to emit the 15-minute progress summary.
  Do not leave a drain silently waiting past those bounds.
- One full pipeline invocation must reach a generated-state fixed point.
  In a full run, `compute_load_bearing.py` first refreshes topology
  `criticality` from the newly built graph before the ledger seeder consumes
  it. Because that seeder can discover rows absent from the pre-seed ledger,
  load-bearing runs again and a second idempotent seed pass consumes the
  refreshed criticality and records the producer receipt before the static
  checkpoint binds classifier inputs. The final load-bearing pass refreshes
  status-dependent ancestor metrics after the effective-status/invalidation/
  restore fixed point. Pipeline-produced ledger status-dependent metrics are
  derived outputs in the static checkpoint; topology `criticality` remains
  fingerprinted because the skipped ledger seeder consumes its prior value
  when deciding whether legacy terminal rows require claim-type re-audit.
  Their underlying notes, dependency edges, runners, and classifier inputs
  remain fingerprinted. Never accept a design that requires a second
  operator-run pipeline merely to stabilize the first.
- Tracked generated audit surfaces must be commit-invariant. Never embed the
  current `HEAD` commit in a tracked pipeline output: committing that output
  changes `HEAD` and guarantees fresh dirt at the next regeneration.
- Treat mechanically verified provenance-only drift on an explicitly
  allowlisted generated surface as recoverable coordination state, not as a
  terminal campaign failure. Carry that exact state through the clean sync
  boundary unchanged and continue the same supervisor; the next normal
  pipeline/commit removes the obsolete provenance field.
- The clean guard must only classify this state; it must not patch, restore,
  rewrite, chmod, replace, or otherwise mutate the generated file. If
  overlapping or non-provenance content appears, preserve it, fail the clean
  check, and stop that transaction.
- Require a writable, owner-matched canonical regular file with no flags and a
  single-link entry, then verify the same raw bytes and metadata again after
  the second status read. Refuse ACL-denied, immutable, special-mode,
  hardlinked, or concurrently changed entries so the downstream generator
  cannot mutate user-owned filesystem state.
- Keep that recovery fail-closed. It must reject staged changes, source or
  ledger content, verdict-bearing changes, untracked files, deletions, and
  any payload delta beyond the exact allowlisted provenance field. Preserve
  every in-flight claim transaction and user-authored change.
- If a supervisor exits after a transaction has committed and pushed, verify
  process absence and exact local/remote synchronization, repair only the
  mechanically verified generated-state condition, and resume exactly one
  supervisor for the original scope: the canonical top-level drainer for a
  full-backlog session, or the remaining allowlisted batch/panel/forensic path
  for a bounded session. Do not leave a recoverable sync condition as a parked
  audit campaign or expand the campaign during recovery.

## Campaign Failure Taxonomy And Persistence

The drainer separates claim-local operational failures from global integrity
failures. This boundary is fail-closed and does not weaken any audit gate.

- **Claim-local, campaign-quarantined:** exhausted schema delivery; an explicit
  `compute_required` skip; a post-verdict row that immediately re-enters
  selection; or an apply/pipeline/lint failure for one validated delivery only
  after rollback to the synchronized `origin/main` parent is verified clean.
  Record the exact cause, exclude only that claim for the current campaign,
  and continue every unrelated ready row.
- **Resumable control flow:** a banked valid critical seat awaiting its peer,
  or `judicial_panel_required`. Resume it through the canonical batch/panel
  edge; neither is a campaign failure.
- **Global retryable:** a transient fetch/push failure whose remote outcome can
  be reconciled exactly. Reconcile the intended commit OID before replay; never
  blindly repeat an uncertain push. If fetch or ancestry proof is unavailable,
  preserve the local intended commit and hard-stop with
  `push_reconciliation_required`; do not reset to a stale remote-tracking ref.
- **Auditor service retryable:** a nonzero auditor exit is retryable only when
  its bounded terminal worker-log diagnostic contains an allowlisted
  backend/transport outage signature (for example HTTP 502/503/504,
  service-unavailable circuit-open, or a reset upstream connection) and
  contains no credit, quota/rate-limit, authentication/authorization, billing,
  policy, or unknown-failure marker. Batch, judicial-panel, and
  forensic-canary seats propagate the same typed temporary-service exit. A
  panel is temporary only when every unresolved seat failure is typed
  transient; any transient/contract/hard mix remains hard. The forensic path
  inspects only a pre-authority Codex execution diagnostic, never verdict
  payload, apply, propagation, or push fields. The top-level orchestrator still
  finishes the mandatory panel sweep after a batch, then retries the affected
  canonical phase with capped exponential backoff. The failed seat mints no
  verdict and is not converted into a scientific or campaign quarantine
  result. Credit, quota/rate-limit, authentication/authorization, policy, and
  unknown worker exits remain hard stops.
- **Global hard stop:** dirty or divergent source state, failed rollback,
  repository invariant failure, unclassifiable generated diff, corrupted
  campaign state, failure to prove an expired seat process group absent,
  unavailable required audit model, authentication failure or authorization
  failure, or an applyability/policy defect that cannot be scoped to one row.
  Preserve artifacts, finish any already-owned transaction at its existing
  reconciliation boundary, and stop before launching another seat or minting
  authority.
- Treat the campaign exclusion JSONL as a closed operational schema. Reject
  blank records, duplicate JSON keys, unknown exclusion reasons, noncanonical
  claim ids, non-finite numbers, noncanonical UTC timestamps, missing or
  reason-incompatible failure evidence, unverified transaction rollback
  evidence, and unexpected fields at every nesting level. A damaged record
  must hard-stop the whole campaign rather than silently suppressing a claim.
- Transaction rollback proof is stricter than the normal main-checkout guard:
  after resetting to the captured `origin/main` OID, require literal empty
  `git status --porcelain` plus exact local/remote OID equality. The narrowly
  tolerated lane-certification provenance drift is not clean rollback proof.

If the product surface supports a persistent goal, use it as a watchdog around
the detached canonical drainer, not as a replacement for the drainer. The goal
is: keep one clean independent-main campaign running or canonically resumed;
preserve every Nature-grade gate; continue through claim-local quarantines; and
after a worker-local fixed point, refresh current `main` and run the same
command again whenever canonical status still exposes work. Stop only after a
fresh post-quiescence status confirms a genuine backlog fixed point, credit
exhaustion, or a verified global integrity/tooling blocker. A goal cannot
repair a nonzero pipeline or supervisor exit by itself.

## Scaling: Canonical Fan-Out And Optimistic Workers

There is exactly one sanctioned audit machinery: the repo-native batch
drainer, invoked directly for a scoped inner step or by the top-level
panel-aware orchestrator. Across independent employee clones, run the same
top-level command described in
[`references/distributed-drain.md`](references/distributed-drain.md). The
scoped inner batch remains available for diagnosis or a named claim/lane:

```bash
python3 docs/audit/scripts/orchestrate_audit_batch.py \
  --lane <lane-name>            # or --claims id1,id2,...
  --max-workers N
```

- **Who may kick it off: any orchestrator.** The invocation is pure process —
  a Claude session (any tier), a codex session, or a human may start it
  without ceremony, because every verdict originates from a fresh sol auditor
  seat inside the drainer. The orchestrator never authors, edits, or
  completes verdict JSON, packets, or rationales; an orchestrator that
  touches verdict content has left this skill.
- **Auditor model/effort is fixed**: the current best Codex GPT model at
  xhigh reasoning exactly — per seat, regardless of who orchestrates. Do not
  escalate seats to max; do not mix families inside one row's
  cross-confirmation without the owner's seating policy saying so.
- **Commits stay serialized** one claim at a time (apply every validated seat
  for that claim -> one pipeline -> one lint -> one commit -> one push inside
  the drainer). A simultaneous critical pair is one claim transaction, not two
  generated-surface transactions; push-race retry replays the whole pair from
  refreshed `origin/main`. Never add a second committer against the same
  checkout; parallelism lives in the auditor seats only.
- **Cross-clone seats are optimistic, not authority-racing.** A stable unique
  worker id rotates each criticality tier while retaining the complete target
  set, so workers start in different places without creating abandoned shards.
  The top-level drainer generates a unique id when none is supplied.
  Immediately before apply, the drainer refreshes `origin/main` and binds the
  delivery to the complete ledger provenance, exact packet evidence manifest,
  dependency note bytes, runner/helper declared inputs, computed
  role/independence/passes, and any dispatch/cascade entry that selected it.
  The cascade cache must exactly equal a pure recomputation from the current
  ledger and runner bytes. Remote movement supersedes the stale delivery
  without applying or quarantining it. Duplicate computation is acceptable;
  duplicate scientific state is not.
- **Live runners never repair a shared checkout.** Execute each primary/helper
  runner in a disposable isolated worktree and capture stdout/stderr. Bind the
  runner and every inherited child to an unguessable invocation token; on
  every completion, timeout, exception, or cancellation, repeatedly enumerate
  token-bearing processes, revalidate the token immediately before each
  signal, and fail closed unless none remain. Never retain or signal a bare PID
  after its identity can change. On macOS, also apply a kernel sandbox that
  denies writes to the canonical checkout. A containment or checkout-discard
  failure is a hard error; discard the isolated checkout on every exit path.
  Never infer ownership of a shared untracked/ignored delta and recursively
  delete it.
- **Concurrency budget (shared codex pool).** Auditor seats, review-loop
  reviewers, and judicial panels all draw on one pool. Keep the TOTAL
  concurrent codex processes across every lane at or under ~8-10, and
  coordinate before raising `--max-workers` while review campaigns run.
  The top-level ceiling applies to judicial work too: a five-judge panel
  still requires five distinct validator-clean votes, but schedules them in
  bounded waves when `--max-workers` is below five. No vote from an earlier
  wave enters the packet or context of a later wave.
  Focused packet-completion helpers and separately authorized
  `--dispatch-science-fixes` work are outside this primary-auditor/judge
  ceiling; repair dispatch is default-off. Reserve shared-pool capacity for
  those helpers and lower `--max-workers` before enabling dispatch. Do not
  describe `--max-workers` as a global process limit.
  Measured 2026-07-17: ~18 concurrent processes collapsed lane throughput
  from 6-11 landed verdicts/hour to ~1 every 3 hours; a 4-6 seat drain in a
  quiet pool is the sweet spot.
- **Development tier only.** The drainer already skips `no_go` rows,
  non-batch-auditable claim types, and forensic-shaped sources at selection;
  do not force them in via `--claims`.

**Forensic tier is serial inside each worker, optimistic across clones.** Each
top-level worker advances at most one forensic row at a time and records every
validator rejection verbatim (it is repair evidence for the packet/validator
path, not noise). Different clones may select the same row. The same
current-main delivery precondition and push-race reconciliation apply: one
current transaction can land, and a stale duplicate is discarded. Do not add
intra-clone forensic fan-out; duplicate cross-clone attempts cost compute but
do not weaken the N1-N8 packet or apply gates.

The canary gets exactly one independent scientific seat. If that prompt-bound
judgment has a complete top-level scientific core but its N1-N8 packet is
rejected on citation or authenticated-occurrence mechanics, it may receive at
most three focused packet-mechanics passes because distinct binding defects can
surface serially (for example, an evidence-locator mismatch followed by an
authenticated occurrence-tuple mismatch). Those passes may change only N1-N8
evidence path/locator fields and authenticated occurrence metadata. The
verdict, claim type/scope, chain judgment, rationale, negative declaration,
invocation, every other top-level value, and every substantive N1-N8 route,
wall, classification, residual match, resolution, closure, steelman, and echo
disposition remain canonically identical. The existing N1-N8 `required` and
`status` gate fields are immutable too, so completion cannot promote FAIL to
PASS. A nonzero legacy
fresh-schema retry budget is a hard configuration error. Coverage rejects
require one exact N3/N5 disposition for every authenticated
`full_phrase_groups` record on every applicable manifest path; records that
share a group id or digest are still distinct when their phrase/path tuple is
distinct. If that bounded budget still ends in malformed JSON or a validator
reject, quarantine only that row for the campaign and continue to the next
ready forensic row. Record the typed validator code, repair class, preserved
run-log location, scientific-seat count, and focused-completion attempt count.
That is not a landed canary, does
not authorize forensic fan-out, and must never be described as multiple
scientific audits.

**Seat-blocked judicial rows are reseated, never frozen and never retried
as recorded.** A disagreement whose recorded seats lack invocation-bound
full rationales can never finish through a panel. When the original seat
delivery envelopes still exist on disk, the gentler operator option is
envelope backfill (`backfill_cross_seat_rationales.py` with the delivery
directories) run before the panel session. The panel orchestrator's own
automatic behavior on any still-blocked row is RESEAT — archive the broken
seats into `previous_audits` with full provenance and the recorded reseat
reason, and reopen the row as `unaudited` for fresh two-seat
cross-confirmation under the rationale-preserving apply contract
(`--no-reseat` reports instead). The reseated row re-enters the normal
development-tier lane: fresh seats that agree land it there; a fresh
disagreement returns to judicial work on the NEXT panel pass with valid
rationales (the default entry loops panels-then-drainer until a pass lands
nothing new). No toggle, no memo, no standing freeze. Reseats persist
through the same per-claim gate ladder as verdicts (pipeline, strict lint,
serialized commit, race-retried push), mint nothing, and any reseat
failure exits nonzero.

**Parallel coexistence with review-loop.** The audit lane and review-loop
sessions may run at the same time by design; the rules that keep concurrent
landings cheap are: (1) exactly ONE audit-lane orchestrator per clone; every
independent clone may run the same top-level command. The drainer and panel
orchestrator enforce the per-clone boundary with a machine-local exclusive
lock keyed to the clone's git common directory, so every worktree of that
clone shares one lock and a second instance exits with guidance. Cross-clone
safety comes from target dispersion, remote-state supersession, serialized
claim transactions, and fast-forward push reconciliation—not from a global
lock or leader; (2) audit
commits are the expensive racers (they ship regenerated audit surfaces and
a push race replays the pipeline), review landings are cheap racers
(cherry-pick retries in seconds) — so the audit lane never waits for
review-loop, and review-loop retries rather than queues; (3) neither lane
hand-merges `docs/audit/data/citation_graph_manifest.json` — a conflict
touching only that file is resolved by regenerating it from the landed
tree.

**Apply-gate rejections are data.** When a finished audit is rejected at the
apply gate (decoration/claim-type mismatch or any compatibility error),
record the exact rejection with the row id in the run report. Recurring
rejection classes get selection-time filters in the drainer — burning a full
audit to discover an incompatibility twice is a defect.

**Schema-invalid delivery is not a science verdict.** It means an auditor
returned JSON that the audit contract cannot apply (for example malformed
JSON, an incomplete N1-N8 packet, or a field whose value contradicts the
schema). It does not show that the source claim is false or needs editing.

- Every restricted Codex seat (ordinary audit, focused packet mechanics, and
  judicial judge) must use CLI `--output-schema` with a transport-level JSON
  object schema. The canonical Python validators remain the only semantic
  schema authority; the CLI schema prevents fences/preambles/malformed JSON
  without duplicating the evolving audit policy.
- In the development tier, an invalid *optional* N1-N8 packet on a non-clean,
  non-no-go verdict is removed mechanically only when the unchanged validator
  accepts the same verdict, declaration, rationale, and every other field with
  `no_go_discipline=null`. Do this before launching completion. Never use this
  normalization for clean authority, a no-go source/type, or forensic work.
- Give parseable N1-N8 citation/occurrence-mechanics rejects bounded,
  error-specific correction attempts in the same restricted seat. Preserve
  every top-level scientific judgment and every substantive N1-N8 value; only
  repair authenticated evidence path/locator and occurrence-tuple metadata.
  Malformed JSON, missing packet content, and other contract rejects without a
  narrow judgment-preserving repair target go directly to the same
  exhausted-delivery path.
- Treat an incompatible verdict/type tuple as a schema-invalid delivery, not
  as a scientific seat. In particular, `audited_decoration` requires
  `claim_type=decoration` plus a decoration parent, while `audited_clean`
  cannot ratify `decoration` or `meta`. Quarantine or retry the invalid seat
  under the normal delivery rules. Launch a judicial panel only when two
  validator-clean, applyable seats disagree on their scientific tuples.
- If a valid critical clean seat survives beside an invalid peer, bank the
  valid seat and let the next top-level batch retry only the missing peer. If
  no valid delivery survives, record every exact validator error and
  quarantine the claim for the current top-level campaign. Continue draining
  other ready rows. Pass the campaign quarantine file to every inner batch so
  a new batch cycle cannot immediately burn the same row again.
- A new campaign-exclusion record is operational progress even when no Git
  commit landed. Run another bounded batch so quarantine-only rounds cannot be
  mistaken for a lane fixed point while later unrelated rows remain eligible.
- Do not apply a verdict, mutate the ledger, or launch a science-editing PR
  from malformed output. A source-repair PR requires a validated non-clean
  verdict with a concrete rationale and repair target.
- Only when the user explicitly requested source repair and the orchestrator
  was invoked with `--dispatch-science-fixes`, hand a newly landed validated
  `audited_failed`, `audited_renaming`, `audited_numerical_match`, or
  repair-actionable `audited_conditional` verdict to
  `scripts/science_fix_loop.py`. Run one detached science-fix process per
  completed audit batch; it may edit only an isolated worktree and may only
  open a PR. Review-loop and a later independent audit remain mandatory before
  any repair reaches retained state.
- `missing_dependency_edge` is a repair-actionable conditional class and maps
  to the `conditional_missing_dependency_edge` science-fix category; do not
  strand it merely because `missing_bridge_theorem` has a separate lane.

Reaching a development fixed point with schema quarantines means the
actionable queue drained except for the explicitly reported malformed
deliveries; never describe that state as a fully empty ready queue.

## Setup For Each Session

1. Fetch `origin/main`.
2. Create or reuse a clean worktree based on `origin/main`.
3. Run:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

The graph-cycle warning is currently expected. Treat any error as a blocker.

## Clean-Context Guards

- Do not run broad content searches over `docs/audit/data/audit_ledger.json`, `docs/audit/AUDIT_LEDGER.md`, or other audit-history files. Use exact `jq` field extraction for selected rows and dependencies.
- When reading `audit_ledger.json`, extract only operational metadata such as `claim_id`, `note_path`, `runner_path`, statuses, `criticality`, `deps`, `note_hash`, and graph-degree fields. Do not print or inspect `verdict_rationale`, `chain_closure_explanation`, `previous_audits`, `audit_history`, or prior auditor notes.
- File-name listing is allowed when needed, but do not search file contents in audit data/history to find alternate candidate sources or prior conclusions.
- The shadow dispatch layer carries ZERO evidentiary weight in either
  direction. In `docs/audit/data/audit_queue.json` this means the per-row
  `would_park` and `would_park_reason` fields and the summary keys
  `shadow_would_park_count`, `shadow_conditional_fail_open_count`, and
  `shadow_publication_lane_size`. Also excluded as evidence: the generated
  files `docs/audit/data/publication_gap.json`,
  `docs/audit/data/audit_publication_lane.json` (top-level `shadow_only`,
  per-entry `would_park`), and the tracked day-keyed churn state
  `docs/audit/data/dispatch_shadow_state.json`;
  the tracked manifest `docs/audit/data/publication_lane_manifest.json`; and
  the front door's "Dispatch Shadow Report" section. All of it is
  dispatch/reporting metadata only (target selection and owner cutover
  evidence per the dispatch-retarget design note). Never cite any of it in a
  verdict rationale; publication-lane membership, pending admission, or a
  would-park classification says nothing about whether a claim is true,
  honest, or well-scoped.
- If fresh-context contamination occurs before a verdict is applied, discard the current context's judgment for that claim and restart the claim in a distinct restricted-input sub-agent when sub-agents are available. Do not pass the contamination, prior conclusion, or audit-history text to the sub-agent. If no sub-agent is available, stop before applying any audit and report the contamination.

## Blocked-Row Loop Guard

- If applying a verdict and rerunning the pipeline immediately invalidates that same row, returns it to the dep-ready queue, or creates a dependency-status cycle that cannot be resolved by the audit verdict alone, do not keep retrying the row in the same audit campaign.
- The canonical top-level orchestrator must persist the claim id and exact invalidation reason in its campaign exclusion JSONL and pass that file to every later batch and lane. A batch-local skip set is insufficient because the next batch process would forget it.
- Treat an accepted verdict as a blocked-row reentry when the post-pipeline row is again `unaudited` and the canonical development-tier selector would immediately choose it. Exclude it for the rest of the campaign, report `blocked_row_reentry_quarantined`, and continue draining every other eligible row. Do not exclude `audit_in_progress` / `awaiting_second` rows; they must resume the missing clean seat normally.
- Do not stop the top-level drainer merely because a row was excluded this way. Reach the fixed point over all non-excluded rows, then report the blocked rows and their exact invalidation reasons separately from schema-invalid quarantines.
- Do not write an unsupported blocked verdict into the ledger unless `apply_audit.py` provides such a route. Report skipped blocked rows at the end of the loop and require upstream dependency/status repair before retrying them.

## Quarantine And Skip Repair

Quarantines and skips are routing state, never evidence about whether a claim
is true. Do not convert them into `audited_conditional`, `audited_failed`, or
any other ledger verdict. Inspect a completed campaign with:

```bash
python3 docs/audit/scripts/audit_campaign_repair.py \
  --campaign-workdir /tmp/audit_loop_campaign_<id>
```

The campaign workdir carries two fail-closed append-only surfaces:
`campaign-row-exclusions.jsonl` suppresses typed claim-local failures only for
that campaign, while `campaign-selector-skips.jsonl` records every canonical
selector disposition without suppressing it. The repair helper joins both to
the current ledger. A missing route is an operational defect; do not leave a
skip only in transient stdout.

Repair and re-entry are reason-specific:

| Operational result | Required repair | Re-entry |
| --- | --- | --- |
| `schema_invalid_quarantined` | Preserve the malformed response, exact validator errors, typed error code/class, scientific-seat count, and any `forensic-canary-*.jsonl` artifact; correct the CLI transport schema, prompt, or bounded packet-completion defect. A failed forensic row enters this route while the worker advances through the remaining non-excluded backlog. Never edit the scientific judgment into validity. | Do not immediately spend another full scientific seat. Repair the typed packet/evidence prerequisite first; use a fresh scientific seat only when the preserved judgment is absent, invalid, or cannot be proven current. Reusing the old workdir keeps the claim excluded. |
| `compute_required_quarantined` / `compute_required` | Produce a SHA-pinned runner cache with `cached_runner_output.py`, a sliced deterministic certificate, or an independent derivation; then run the full pipeline and strict lint. | Start a new campaign after the artifact is current. |
| `blocked_row_reentry_quarantined` | Repair the recorded classifier promotion, dependency/status cycle, note-hash drift, or other invalidation cause. Require one converged full pipeline. | Start a new campaign only after the row no longer immediately returns to the same dep-ready state. |
| `claim_transaction_quarantined` | Fix the recorded apply, pipeline, or lint defect and prove the clean full pipeline converges. The failed delivery minted no verdict. | Use a fresh seat in a new campaign unless canonical tooling verifies an exact preserved-envelope replay against the current source/seat fingerprint. |
| `dependencies are not retained-grade` | Audit or repair the named upstream dependency; do not force the downstream row. | Automatic when dependency closure becomes retained-grade and the pipeline refreshes the queue. |
| `no_go row` or `source shape requires forensic tier` | Run the required N1-N8 forensic path, one canary at a time. | Through the forensic selector, never by forcing the development batch. |
| `claim_type ... not batch-auditable` | Route `meta` or `decoration` only when explicitly requested and through their compatible apply contract. | Targeted audit, not default development selection. |
| `missing ledger row` | Restore or register the canonical row and pass the full pipeline, strict lint, and repository invariants. | New campaign after registry repair. |
| `judicial_panel_required` | No repair: this is the normal two-seat disagreement handoff. | Immediate five-judge panel, then resume the same lane. |

The exclusion JSONL is append-only incident provenance for one campaign. Do
not delete individual records to force retry and do not reuse the old campaign
workdir after repairing prerequisites. Start a new campaign workdir; the row is
then eligible under current queue and selector rules. A campaign fixed point
with exclusions means “all non-excluded actionable work drained,” not “the
entire audit backlog is empty.”

## Long-Running Runner / Timeout Guard

- A wall-time timeout, missing stdout, or noncompletion of a runner is not scientific evidence against the claim. Do not apply `audited_conditional`, `audited_failed`, or any other terminal non-clean verdict solely because the runner may need a long compute run.
- When analysis needs runner stdout, use `python3 scripts/cached_runner_output.py <runner_path>` instead of running the runner directly. This reuses a fresh SHA-pinned cache, or writes one if the cache is missing/stale, so later audits and non-audit analysis do not rerun the same expensive computation.
- If the load-bearing step cannot be judged without a long run and there is no completed log, cached certificate, sliced deterministic runner, or independent derivation in the restricted packet, record a session-local `compute_required` skip with the claim id, runner path, timeout/budget used, and the exact artifact needed; then continue with the next ready row.
- Apply a non-clean verdict only when there is a substantive audit reason beyond wall-time noncompletion, such as a completed output mismatch, stale number, unsupported dependency, import/API failure, hard-coded contested premise, or an over-broad claim not supported by completed finite evidence.
- If a prior audit row appears to have used timeout/noncompletion as the primary reason for a terminal verdict, do not treat that prior verdict as settled science. Queue it for policy repair or re-audit under this guard.
- Do not blanket-reset older rows just because the rationale mentions a timeout. If the same rationale contains an independent blocker, re-audit the blocker under restricted inputs; if timeout/noncompletion is the primary or only reason, leave the row pending for compute or policy repair instead of citing it as non-clean science.

## Compute-Limited Backlog Repair

`runner_breakage_inventory.json` lists runners that the audit triage timed out or that exited nonzero. The default pipeline timeout is 60-120s; some load-bearing runners (lattice MC, large eigenvalue, dense sweeps) legitimately need 300-1800s. Treat these as compute-limited, not science-failed (per the Long-Running Runner / Timeout Guard above), and repair them with the canonical batch helper:

```bash
# Refresh a curated list of broken runners with extended timeouts:
python3 scripts/precompute_audit_runners.py \
  --runners scripts/frontier_plaquette_self_consistency.py,scripts/frontier_color_projection_mc.py,...

# Or, for one runner with an ad-hoc longer budget:
python3 scripts/cached_runner_output.py scripts/<runner>.py
```

Per-runner declared timeout (preferred for runners that are persistently slow): add a top-level `AUDIT_TIMEOUT_SEC = <N>` assignment to the runner file. `scripts/runner_cache.runner_timeout_for()` reads this and overrides the default.

After bulk cache refresh, commit `logs/runner-cache/*.txt` and the mechanical sharded-ledger delta (`docs/audit/data/ledger/`) together; the monolithic `audit_ledger.json` is an untracked cache materialized by the pipeline. The full audit pipeline (`docs/audit/scripts/run_pipeline.sh`) will then regenerate `runner_classification.json`, `audit_queue.json`, `effective_status_summary.json`, and `AUDIT_QUEUE.md` against the new cache.

**Refresh propagation**: refreshed cache files land on `main` via PR. After merge:

- The `.github/workflows/audit.yml` nightly cron at `0 6 * * *` UTC automatically runs the pipeline against `main` and auto-commits any refresh deltas as `audit: nightly repair and pipeline refresh (automated) [skip ci]`. **No manual action required.**
- For immediate refresh (skipping the wait for the nightly run), trigger `workflow_dispatch`: `gh workflow run audit.yml` (or via Actions UI). The same auto-commit pattern runs.
- Audit verdicts are **never** auto-minted; the cron only updates classification + queue + load-bearing. Auditors still pick from the refreshed `AUDIT_QUEUE.md` and apply verdicts via `apply_audit.py`.

## Legacy Claim-Type Re-Audits

- `claim_type_backfill_reaudit` rows are migration cleanup under the PR291 regime. Audit the current scoped claim, not the old source-note status prose.
- For critical rows with already confirmed legacy clean cross-confirmation whose summaries predate `claim_type`, a restricted-input re-audit may own the scoped `claim_type` and `claim_scope`; missing `claim_type` in the old summaries is not by itself a cross-confirmation disagreement.
- If the new restricted-input audit changes the actual clean/non-clean verdict, or if `apply_audit.py` records a real cross-confirmation disagreement, follow the normal escalation path.

## Pick The Next Claim

For a bounded request, select only from the frozen allowlist established above.
All dispatch, cascade and queue fallthrough below is restricted to those IDs.
The unfiltered selection snippets are for full-backlog sessions only; never
run them as selectors for a bounded session. Missing or ineligible selected
rows remain explicitly unresolved rather than being replaced by other work.

If the user names a candidate file or other constrained selection source, that source is authoritative. After the pipeline, check the exact path exists. If it is absent, stop and report the missing file; do not search for substitutes or fall back to the default queue unless the user explicitly authorizes that fallback.

### Targeted Audit Dispatch Source

Before falling through to cascade re-audit or the regular queue, check
`docs/audit/data/audit_dispatch_queue.json`. This is the durable dispatch
stream for targeted fresh-context re-audits that the normal queue will not
surface, especially rows that are already terminal-clean / retained-bounded
but need a scoped retag or reclassification decision after a framework-rule
clarification.

Process dispatch entries before cascade candidates:

1. Read `docs/audit/data/audit_dispatch_queue.json`.
2. Pick the first entry in `live` with `ready = true`.
3. Use the entry only to select the target `claim_id` and audit question. Do
   **not** pass the dispatch manifest, PR text, prior assistant discussion,
   prior audit rationales, or publication-facing retained summaries into the
   auditor packet.
4. Build the restricted packet from the selected row's source note, one-hop
   dependencies, runner/helpers/cache, required audit docs, and the entry's
   `allowed_context_paths`.
5. Apply any verdict or retag through the normal audit lane (`apply_audit.py`),
   one claim per commit, then rerun the pipeline. A dispatch entry is resolved
   only when the generated dispatch queue no longer lists it as live.

Use this snippet when useful:

```bash
python3 - <<'PY'
import json
p=json.load(open("docs/audit/data/audit_dispatch_queue.json"))
for e in p.get("live", []):
    if e.get("ready"):
        print(e["claim_id"], e["note_path"], e.get("audit_question", ""))
        break
PY
```

If the snippet prints no ready entry, continue to cascade re-audit.

### Cascade Re-audit Source

Before falling through to the regular queue, check
`docs/audit/data/reaudit_candidates.json`. This is the cascade-resolution
stream for non-clean audited theorem/no-go/open-gate rows whose blocker may
have been repaired after the original audit. The main `candidates` stream
covers rows whose one-hop dependencies have since become retained-grade; the
secondary `runner_drift_candidates` stream covers runner-artifact rows whose
runner hash changed after the audit snapshot.

Process cascade candidates before fresh queue rows, with the same scoped
claim-type filter and the current session's blocked/skip set:

1. Read `docs/audit/data/reaudit_candidates.json`.
2. If `candidates` is non-empty, pick the highest-leverage entry with
   `claim_type` in `{positive_theorem, bounded_theorem, no_go, open_gate}`.
   The producer sorts by criticality, descendants, load-bearing score, and
   claim id.
3. If `candidates` is empty but `runner_drift_candidates` is non-empty, pick
   the highest-leverage entry there with the same `claim_type` filter.
4. Exclude any claim id recorded in the current session's blocked/skip set.
5. If no cascade candidate is eligible, fall through to
   `docs/audit/data/audit_queue.json` and use the default queue rules below.

Use this snippet when useful:

```bash
python3 - <<'PY'
import json
p=json.load(open("docs/audit/data/reaudit_candidates.json"))
for e in p.get("candidates", []) + p.get("runner_drift_candidates", []):
    if e.get("claim_type") in {"positive_theorem","bounded_theorem","no_go","open_gate"}:
        print(e["claim_id"], e["note_path"], e.get("runner_path") or "-")
        break
PY
```

If the snippet prints no candidate, fall through to the regular queue.

`audited_conditional` with `dependency_not_retained` is the expected state
when a downstream theorem lands before its upstream dependencies reach
retained-grade. The cascade-first ordering resolves these naturally as
upstream cleanup lands, instead of letting fresh `unaudited` queue rows starve
now-unblocked downstream conditionals.

### Default queue selection

Default fall-through selection is the highest-priority ready scoped claim:

1. Read `docs/audit/data/audit_queue.json`.
2. Pick the first row with `ready = true`, `audit_work_kind =
   fresh_scientific_audit`, `audit_status` in `{unaudited,
   audit_in_progress}`, and `claim_type` in `{positive_theorem,
   bounded_theorem, no_go, open_gate}`. `ready` is the conjunction of
   `dependency_ready` and `forensic_evidence_ready`; it is no longer a
   dependency-only flag.
3. If the user explicitly says strict queue order, take the top queue row even if `claim_type` is unset.
4. Exclude any claim id recorded in the current session's blocked/skip set by the Blocked-Row Loop Guard.
5. If only `meta` or `decoration` rows remain, process them only when the user explicitly asks for those classes.

### Empty-Queue Refresh

If step (2) finds no eligible row in the current `audit_queue.json` (queue exhausted, or every remaining row excluded by `ready=false` / session-blocked / wrong `claim_type` filters), **refresh the pipeline locally before stopping**. Newly landed runner caches or upstream audit results may have made fresh rows ready since the queue was last regenerated.

Refresh exactly once per session per empty-queue event, in this order:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

Then re-attempt selection (steps 1-5). If the refreshed fresh-science selector
is empty, inspect and report `by_work_kind`. The audit lane is genuinely
caught up only when there is no pending `fresh_scientific_audit`,
`legacy_packet_upgrade`, or `evidence_repair_required` work. The latter two
are mechanical preparation/certification lanes, never permission to spend a
fresh scientific seat. Missing or ambiguous v2 provenance is conservatively
routed to `fresh_scientific_audit`, so it cannot rest in an undrained
preparation category. Do not refresh repeatedly in one session and do not
invoke `gh workflow run audit.yml` from inside the audit loop (the CI workflow
runs its own pipeline and could race the local one).

The empty-queue refresh exists because runner caches and audit verdicts land continuously; the queue snapshot can lag behind by several commits when the session started. A single local refresh covers the common case where a recent PR (e.g. a compute-limited backlog repair) made dozens of rows newly auditable but the local queue hasn't yet caught up.

Use this snippet when useful:

```bash
python3 - <<'PY'
import json
q=json.load(open("docs/audit/data/audit_queue.json"))["queue"]
for e in q:
    if (e.get("ready")
            and e.get("audit_work_kind") == "fresh_scientific_audit"
            and e.get("claim_type") in {"positive_theorem","bounded_theorem","no_go","open_gate"}):
        print(e["claim_id"], e["note_path"], e.get("runner_path") or "-")
        break
PY
```

### Dispatch Queue

`docs/audit/data/audit_dispatch_queue.json` carries provenance and
promotion re-audit targets. The top-level drainer authenticates and
drains ready entries before cascade and regular development work. Every
top-level worker runs this same source ordering. A manual single-claim run
processes this source when explicitly selected by the user or surfaced by an
external dispatcher.

**Same-status confirmation rule:** if a fresh-context re-audit on a
dispatch target confirms the same `{claim_type, audit_status,
effective_status}` as the manifest guard, do not re-attempt. The
producer (`docs/audit/scripts/compute_audit_dispatch_queue.py`) auto-
retires such targets to `resolved_targets` with one of two resolution
reasons:

- `same_status_fresh_context_reaudit_after_manifest` (general provenance
  resolution: `audit_date ≥ manifest.generated_date` and `independence
  != weak`)
- `bounded_terminal_after_reaudit` (promotion dispatch where the post-
  manifest verdict confirms `bounded_theorem` — retain as bounded-terminal
  unless future source work changes the claim hash)

Re-auditing a row already in `resolved_targets` is wasted work; only
re-attempt if the source note's `note_hash` has changed or the user
explicitly requests a fresh independence pass.

For `ready=false` dispatch rows, check the `ready_blocker` field —
it names the blocking dep as `blocked_by_dependency:<claim_id>:<effective_status>`. Do not attempt the audit until that dep reaches
retained-grade.

## Context To Read

For the selected claim, read only:

- source note at `note_path`;
- one-hop dependency notes listed in `docs/audit/data/audit_ledger.json` under `deps`;
- the primary runner, if any;
- current runner output, if the runner can be executed safely;
- `docs/audit/README.md`, `FRESH_LOOK_REQUIREMENTS.md`, `AUDIT_AGENT_PROMPT_TEMPLATE.md`, and `ALGEBRAIC_DECORATION_POLICY.md`.

**Relationship context inside a restricted packet.** A note may declare
machine-readable `contradicts:` / `cross_reference:` lists (historic-intake
wrappers do). When it does, `scripts/codex_audit_runner.py`
`relationship_context_blocks` resolves each declared reference — the wrapper
file and its archived original — and `render_prompt` appends them under a
`RELATIONSHIP CONTEXT (contradiction/context evidence — not dependencies)`
heading, each block role-labelled `contradiction evidence — not dependencies`
or `context evidence — not dependencies` and stamped
`authority: none`. Delivery is atomic and fail-closed: an unreadable
reference raises `RelationshipContextError` and types the seat
`relationship_context_unready`, and a wrapper or archived original that
changes while the seat runs is caught by `relationship_context_fingerprint`
and typed `relationship_context_superseded` — never
`remote_state_superseded` (regression:
`docs/audit/scripts/tests/test_relationship_context_delivery.py`).
Treat these sections as EVIDENCE to adjudicate — the contradiction set and the
historical context around the source note — never as dependencies to satisfy,
never as cited authorities, and never as prior-verdict context. They carry no
effective status and no claim authority, and the fresh-context rules below
apply to them unchanged: a relationship block that quotes or implies an
earlier verdict does not license inheriting it.

When writing the verdict, also load `references/nature-grade-rubric.md` from this skill.
For theorem, proof, or nontrivial reduction claims, also load
[`../physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md)
as audit procedure.

Do not use `CLAIMS_TABLE.md`, `PUBLICATION_MATRIX.md`, `ARXIV_DRAFT.md`, or earlier review summaries to bias the verdict.

## Audit Questions

Answer these before choosing a verdict:

- What exact sentence/equation is load-bearing?
- Is the claimed observable the same observable being compared or derived?
- Does the result follow from cited inputs, or is a symbol identity being introduced?
- Are any physical carriers, unit maps, source laws, boundary conditions, sectors, normalizations, or readouts selected without a retained theorem?
- Are dependencies unaudited, open gates, retained-pending-chain, stale, or themselves conditional?
- Does the runner compute the hard bridge, or does it hard-code the contested premise and check consistency afterward?
- For every math-bearing step, what independent formula check was performed
  beyond rerunning the same code? Did it verify the sign, factor,
  normalization, dimensions/units, matrix ordering, boundary condition,
  optimizer objective, and expected numeric value?
- Would a minimal toy case, limiting case, symmetry/invariance check, or
  second implementation catch the class of error the runner could otherwise
  hide?
- Is this an independent theorem, or algebraic decoration of an upstream claim?
- Does the proof match the exact target statement, quantifiers, and required
  edge cases?
- Does the proof-obligation graph close without cycles, lost hypotheses, or
  inadmissible constructed objects?
- What is the strongest unresolved lemma, and is it weaker than,
  target-equivalent to, or stronger than the headline claim?
- Are numerical values current with the runner and the source note?
- Would a hostile specialist be able to reject the conclusion without making a mistake?
- If the claim is a `no_go`, a wall-naming `bounded_theorem`, or its rationale would cite walls: have at least 5 distinct attack routes against the no-go been considered (N1)? Are the named walls actually independent (N2)? Are any hidden in "bridge context" / "we assume" / "standard QFT" / "registered" prose (N3)? Do cited witness residuals match the claim's residual (N4)? Are "X is not a Y-fact" phrases verified at every named resolution (N5)? Is the "needs new axiom" framing actually a convention-reframe / labeling ratification (N6)? Can a steelman against the no-go be made convincing (N7)? Has a structurally similar prior wall been retired by a mechanism not considered here (N8)? See `no-go-discipline` skill.

## Law-Domain Audit Procedure

(Relocated from the AXIOM_MINIMALITY_POLICY section 6 reading notes,
2026-07-02, under the owner rule that process lives in procedural docs while
semantic content lives in axiom text or audited derivations. This section is
audit process only; it carries no premise or interpretive weight.)

When a claim's law domain (a supplied condition) is audited:

- **Certificate demand.** Ask for the condition's certificate: its
  retained derivation, bridge, or approved primitive registration.
  A condition with no certificate does not enter as load-bearing content.
- **Covariance transport.** Transport the condition under lattice motions and
  check the selected state sets move covariantly; a condition whose selected
  sets are not motion-covariant is flagged against the motion-closure theorem
  rather than silently accepted.
- **Decidability from record readouts.** The condition must be decidable from
  record readouts without running the law it gates.
- **Finite/local evaluability.** On the infinite lattice some conditions are
  refutable but not verifiable; finite/local evaluability is audit practice,
  not axiom content — audit at the finite ranges the runner exercises and say
  so.
- **Extensional judgment.** Judge a condition by the set of states it
  selects, never by its wording; co-extensional conditions receive one
  verdict (interface theorem in the final derivation note).

## Verdict Rules

Use the audit-lane verdict enum exactly:

- `audited_clean`: derivation closes from the cited inputs; no hidden physical identification; runner checks the load-bearing step or the proof is purely exact algebra over independent retained inputs; and every math-bearing formula/sign/factor/normalization/numeric target has been independently cross-checked outside the runner's implementation path. Effective status is derived from ledger `claim_type` plus dependency closure, not source-note status prose. `support` is not a claim class, and old support prose neither grants nor blocks retained status after a clean audit.
- `audited_conditional`: depends on an unaudited dependency, open gate, retained-pending-chain row, unratified physical bridge, or an explicit premise not closed by the cited authorities.
- `audited_renaming`: the load-bearing step defines/renames the target quantity or identifies two concepts without derivation.
- `audited_decoration`: exact algebraic corollary with no independent comparator, falsifiability, compression, or new physical content beyond an upstream parent.
- `audited_numerical_match`: result depends on tuned/calibrated input or chosen scale/value rather than a structural theorem.
- `audited_failed`: chain is wrong, stale relative to the runner, mismatches the observable, contradicts dependencies, or does not close on its own terms.

Math errors in a runner are scientific blockers, not mere infrastructure
noise, when the affected formula is load-bearing. Use `audited_failed` if the
current claim relies on the wrong expression; use `audited_conditional` with
`notes_for_re_audit_if_any: runner_artifact_issue` only when the source claim
may still be true but the artifact is not reliable enough to judge it.

When in doubt, choose the more conservative non-clean verdict.

If a proof or reduction terminates at a target-equivalent or stronger missing
lemma, do not grant `audited_clean`. Route the defect by the claim actually
made:

- use `audited_failed` when the source claims to discharge the target but the
  proof ends at an unproved, circular, or merely renamed terminal lemma;
- use `audited_conditional` only when the terminal lemma is disclosed as an
  explicit named premise or dependency on which the claim is honestly
  conditional;
- for that conditional case, use `scope_too_broad` when a clean narrow core is
  overextended, `other` for a pure mathematical proof obligation not covered
  by a more specific class, and `missing_bridge_theorem` only for the physical
  carrier/readout/unit/boundary/sector/normalization/observable bridge kinds
  defined below.

In every case name the exact terminal obligation and explain why its strength
is comparable to or greater than the headline target. If a clean narrow lemma
survives independently, state that narrow boundary in `claim_scope`.

For claims with `claim_type: no_go`, `bounded_theorem` whose source note names walls/open conditions, or any verdict that would record walls in `verdict_rationale`, apply the No-Go Discipline gate (`no-go-discipline` skill, N1-N8) before recording. Any FAIL forbids `audited_clean`; instead, choose the non-clean verdict whose `verdict_rationale` reflects the corrected narrower claim scope. Specifically:

- if N1 fails (fewer than 5 distinct attack routes considered against the no-go), record `audited_conditional` with `notes_for_re_audit_if_any: scope_too_broad — alternative attack routes not exhausted`;
- if N2/N3 fails (walls not independent, or hidden walls promoted), record `audited_conditional` with the collapsed/expanded honest wall list;
- if N4 fails (witness-residual mismatch in cited authorities), record `audited_conditional` with `notes_for_re_audit_if_any: missing_dependency_edge — cited witness residual does not match the claim residual`;
- if N5/N6 fails (over-broad phrasing, or convention-reframe misclassified as new axiom), record `audited_renaming` if the failure is purely scope/framing, or `audited_conditional` with a sharper wall list;
- if N7/N8 fails (convincing steelman exists, or prior-wall retirement mechanism not considered), record `audited_conditional` with `notes_for_re_audit_if_any: scope_too_broad — named alternative not foreclosed`.

See [`docs/ai_methodology/skills/no-go-discipline/SKILL.md`](../no-go-discipline/SKILL.md). The audit lane must not transcribe a source note's inflated no-go into the ledger as `audited_clean` — that cements the overclaim and forecloses investigation paths permanently.

## Required Failure Handoff

For any verdict other than `audited_clean`, make the ledger useful to the physicist who fixes the science. Put this structure inside `verdict_rationale` and keep `chain_closure_explanation` short but specific:

```text
Issue: <exact failed step, stale number, hidden premise, or observable mismatch>.
Why this blocks: <why the conclusion cannot be claimed from current inputs>.
Repair target: <specific theorem, derivation, runner computation, or dependency status needed>.
Claim boundary until fixed: <what may still be safely said>.
```

For `audited_clean`, still explain why the load-bearing step closes and what residual risk remains.

## Conditional Repair Surfacing

For every `audited_conditional` result, make the next repair lane sortable.
Prefix `notes_for_re_audit_if_any` with exactly one repair class:

- `missing_dependency_edge`: a needed source note or authority exists or is
  named, but is not wired as a direct dependency for the audited claim.
- `dependency_not_retained`: a direct dependency exists but is not retained
  grade.
- `missing_bridge_theorem`: the claim needs a new theorem for a physical
  carrier, readout, unit map, boundary condition, sector choice,
  normalization, or observable bridge.
- `scope_too_broad`: a clean bounded core exists, but the current claim scope
  includes an unclosed extension.
- `runner_artifact_issue`: a runner, log, classifier, threshold, import, or
  pass/fail accounting problem blocks closure despite otherwise local scope.
- `compute_required`: closure needs a completed long run, sliced runner,
  cached certificate, or independent derivation.
- `other`: use only when none of the above fits, and state why.

After the class, name the cheapest next repair action, such as adding an
explicit citation/dependency edge, auditing a named dependency first, creating
an open bridge theorem, splitting the clean bounded core from the conditional
extension, or repairing/slicing the runner. Do not repair during the audit
unless the user explicitly asks for repair work.

Only when the user explicitly requests source repair as part of the audit
episode, pass `--dispatch-science-fixes` to the audit orchestrator. Repair
dispatch is off by default. The dispatched handoff is accepted only after its
claim id, audit invocation, verdict, scope, rationale, load-bearing step, and
repair target match the current canonical sharded ledger row on `origin/main`;
the repair prompt is reconstructed from those verified fields.

## Apply The Audit

Create an audit JSON matching `docs/audit/scripts/apply_audit.py`. Returning this JSON to the user is not the end of the task unless they explicitly requested dry-run/no-apply behavior. Required metadata:

- `claim_type`: one of `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`, `decoration`, `meta`.
- `claim_scope`: a short citeable statement of exactly what was audited.
- `auditor`: use a stable string such as `codex-audit-loop`.
- `auditor_family`: use the actual family if known; otherwise use `codex-current`. Do not claim `codex-gpt-5.5` unless that is true for the session.
- `independence`: use `cross_family` for non-Codex-authored claims, `weak` for same-family audits, `strong` for independent human review, `external` for off-project review.

Apply it:

```bash
python3 docs/audit/scripts/apply_audit.py --file /tmp/audit-result.json
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

For critical claims, the first clean audit records `audit_in_progress` and awaits cross-confirmation. That is expected.

`apply_audit.py` is the gate. Critical claims receive two independent audit
passes through the cross-confirmation flow. If those two passes disagree, do
not resolve the disagreement with a single judicial third auditor. Run a
five-judge panel in the same loop using the restricted source packet plus the
full first-audit and second-audit arguments as explicit context. Each judge
must run at the required audit model/reasoning level with a distinct auditor
identity, vote on the full tuple `(sided_with, ratified_verdict,
ratified_claim_type, ratified_claim_scope, ratified_load_bearing_step_class,
ratified_decoration_parent_claim_id, negative_assertion_classes)`, and explain
errors in the other position. Treat whitespace-only scope differences and
assertion-class ordering as equivalent, but require substantive scope,
decoration-parent, and declaration agreement. A majority is at least three
matching full-tuple votes out of five.

A judge response whose fields violate the semantic vote contract carries no
scientific authority and does not count as a delivered vote. Preserve the exact
validator error and launch a fresh five-judge panel; after two consecutive
fresh-panel contract recoveries, a third contract-invalid panel is a hard
tooling blocker rather than a scientific disagreement or human-review stop.

After a panel majority, go with the majority only if the majority tuple is
applyable by the audit tooling and the normal gates pass. The apply gate accepts
the representative judicial JSON only through an invocation-bound
`judicial_panel_record_v1` that preserves five distinct validator-clean votes,
the current source/seat fingerprint, and the matching 3-of-5 full-tuple
majority. The legacy `third_audit` fields are only the stored projection of
that verified panel record. Once verified, rerun the pipeline, strict lint,
and `git diff --check`, then land it as the audit result.

No cross-confirmation disagreement should stop at "human review" merely because
a five-judge panel has no 3-of-5 majority, because the panel majority sides with
neither original audit, or because the panel selects a hybrid tuple. Treat that
case as authorization to run another five-judge panel in the same audit loop.
Give the new judges the restricted packet, the full first/second audit
arguments, and every prior panel vote/rationale breakdown. If a later panel
majority selects a third applyable tuple rather than either original tuple,
record it as `third_confirmed_hybrid`, then rerun the normal
apply/pipeline/lint/diff-check gates before landing.

Do not keep retrying individual judges after a completed five-judge panel.
Escalate by running a fresh five-judge panel with the prior panel outcomes in
context. Stop only for a hard tooling or policy blocker that prevents the next
panel or prevents applying/verifying an otherwise applyable majority; report the
blocker as a tooling/policy stop, not as a human-review stop.

If `apply_audit.py` accepts the JSON and `audit_lint.py --strict` passes after the pipeline refresh, land the audit by direct push to `main` for these routine cases:

| Verdict / state | Audit-loop action |
| --- | --- |
| First or second `audited_clean` in the cross-confirmation flow | Direct push to `main` |
| Cross-confirmation disagreement resolved by a five-judge panel majority that confirms an applyable first, second, or hybrid verdict | Direct push to `main` after applying the majority judicial JSON |
| `audited_conditional`, `audited_renaming`, `audited_decoration`, or `audited_numerical_match` | Direct push to `main` |
| `audited_failed` on a non-controversial claim | Direct push to `main` |

Do not open a human-review PR for ordinary panel disagreement. Continue with
fresh five-judge panels until an applyable majority lands or a hard tooling /
policy blocker prevents progress:

| Exception | Audit-loop action |
| --- | --- |
| Five-judge panel has no 3-of-5 majority, sides with neither original audit, or produces a hybrid / currently unapplyable tuple | Run another five-judge panel with all prior panel outcomes in context |
| Cross-confirmation disagreement exists but the five-judge panel cannot be run with the required context/model | Stop as a tooling availability blocker |
| A batch claim's apply/pipeline/lint transaction fails and rollback to synchronized `origin/main` is verified clean | Quarantine that claim for the campaign, preserve the validated delivery and exact error, and continue unrelated rows |
| `apply_audit.py` rejects a targeted/manual verdict JSON or a hard rule cannot be scoped to one cleanly rolled-back batch claim | Stop as an audit tooling blocker after preserving the rejected JSON and exact error |
| `audit_lint.py --strict` fails and rollback cannot be verified clean, or the same infrastructure failure repeats across unrelated claims | Stop as a global verification blocker |

## Commit And Push

Review the diff. It should normally touch only:

- `docs/audit/data/ledger/<claim-id-prefix>/<claim-id>.json`;
- `docs/audit/data/ledger_meta.json` when top-level statistics change;
- `docs/audit/data/effective_status_summary.json`;
- `docs/audit/AUDIT_QUEUE.md`;
- possibly other tracked load-bearing/runner summaries if the pipeline refreshed them.

The monolithic ledger, queue JSON, runner classification, citation graph,
rendered `AUDIT_LEDGER.md`, and the generated shadow dispatch files
(`publication_gap.json`, `audit_publication_lane.json`) are ignored
materialized caches; never force-add them. `dispatch_shadow_state.json` is
TRACKED day-keyed churn state that pipeline runs may legitimately update at
most once per UTC day — audit commits that stage `docs/audit/data` will
carry that update, which is expected and carries no evidentiary weight.
`publication_lane_manifest.json` is tracked controlled data owned by the
review lane — an audit commit must not modify it.

Commit:

```bash
git add docs/audit
git commit -m "audit: <claim-id> <verdict>"
```

Before pushing, fetch and confirm `origin/main` is still the validated parent:

```bash
git fetch origin main
git push origin HEAD:main
```

If the push is rejected, reconcile the exact intended commit OID first. If it
already landed, record success. If canonical source, dependency, packet,
selection, role, or independence state moved, discard the old seat and build a
fresh packet; never rebase an already-applied forensic verdict onto that new
authority state. A manual replay is permitted only after exact source
fingerprints still match and apply/pipeline/lint/diff-check are rerun from the
new parent.

## Loop Control

After each successful direct-main push:

1. Report the claim id, verdict, and one-sentence reason.
2. If time and user intent allow, fetch `origin/main`, refresh the queue, exclude any session-local blocked/skip rows, and start the next claim within the authorized scope. A bounded session stops at its selected set; it never continues into the global queue after completing or blocking those IDs.
3. Stop if there is an ambiguous independence issue, source-note hash drift that cannot be resolved mechanically, or an audit requiring domain expertise beyond the provided authorities.

For unresolved global hard tooling or policy blockers listed above, do not
push to `main`; preserve the rejected JSON, panel logs, campaign exclusion
records, and exact command output, then report the blocker. A verified
claim-local rollback is quarantined and does not stop the campaign. Do not stop
merely because a five-judge panel occurred or because a panel was unresolved;
continue with a fresh panel carrying the prior panel outcomes in context.
