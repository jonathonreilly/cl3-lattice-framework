# Review-loop PR conformance spec

**Authority and use.** The requirements below were distilled from the 2026-08
review-loop drain, over its first nineteen landed reviews. They are banked in-repo by
owner directive (2026-08-09) so that PRs are authored to the spec rather than corrected
against it across review cycles. The `physics-loop` skill treats this document as
a **generation-time checklist**: a PR is not ready to request review until every MUST
below is satisfied. The wiring is in place — `physics-loop` runs the section-by-section
check in its Science Delivery And PR Policy before a block PR is opened,
`science-fix-loop` runs it before a repair PR exists, and `review-loop` uses it as the
pre-review conformance bar for pre-fix and as shared cure text in its Fix Policy.

**This document is a restatement, not an authority.** Every rule below either
cites the file that owns it, or says explicitly that the owner directive of
2026-08-09 is its authority — those are the only two provenances a MUST here
may have, and a MUST with neither is a defect to report rather than follow.
Where this document and a cited file disagree, the cited file
wins, and the disagreement is a defect in this document. An owner-directive
rule is genuinely new operational authority: it binds because the owner said
so, not because it restates a skill. Items are MUST unless
marked otherwise. Exemplars: PRs #6015, #5921, #5925, #5930, #5979 (iterations),
#5931 (salvage); landed packet exemplar
`docs/LOCAL_CLOCK_RELATION_CYCLE869_BOUNDED_THEOREM_NOTE_2026-07-28.md`.
References here are provenance-only and deliberately non-linking, per the
citation-edge rule in section 8.

## 1. Self-containment (the top rejection driver)

- A declared input (`AUDIT_INPUT_PATHS` or any equivalent closure) must be a file
  that either has landed on `origin/main` **or** is included and reviewed in this
  PR's own landing delta. The cache and the readiness checker bind the input's
  bytes in the proposed tree and reject drift; they do not require pre-existence
  on `origin/main` (`scripts/runner_cache.py` header;
  `docs/audit/scripts/forensic_evidence_readiness.py` `_runner_source_issue`).
- Forbidden regardless: pins of artifacts from a rejected branch, receipts from a
  rejected run, and pins of anything that is neither on `origin/main` nor in this
  delta. If an ancestor result did not land and is not carried here, it cannot be
  used: either re-establish it inside this PR's own computation or drop the claim
  that needs it.
- A dependency may be brought in as a self-contained derivation and reviewed in
  the same branch; that is the sanctioned repair route
  (`docs/ai_methodology/skills/review-loop/SKILL.md:737-738`). Copying in an
  unreviewed sibling's conclusion is not.
- No hard requirement on gitignored artifacts (e.g. the symlinked
  `docs/audit/data/audit_ledger.json`). Runners must be fresh-worktree
  reproducible: clone at `origin/main`, apply the delta, run.
- Stacked PRs: the delta may rely on the base branch's content only if that
  content has landed by the time this PR is reviewed, or is itself inside the
  reviewed delta; otherwise the same rules apply.

## 2. Cache and execution discipline

- Every cached runner output goes through
  `scripts/runner_cache.py` `execute_and_write_cache(runner, timeout_sec)`.
  Raw stdout files are not caches.
- Timeouts, as an AUTHORING requirement on new and changed runners: every new
  or changed runner declares `AUDIT_TIMEOUT_SEC = N` as a top-level
  assignment, and its cache header's `timeout_sec` carries that declared
  number — not an ad-hoc value chosen at call time. This is a rule about what
  a new runner must declare, not a claim about resolver behaviour. The
  resolver has three tiers: declared value, then a legacy substring override,
  then the 120-second default (`scripts/runner_cache.py` `runner_timeout_for`,
  reading `declared_timeout_for`); `scripts/precompute_audit_runners.py` and
  `scripts/codex_audit_runner.py` both consume it. So an existing runner that
  declares nothing still reproduces at its override or default value — the
  point of the authoring rule is that new work must not rely on that fallback,
  and that a header number matching neither the declaration nor the resolver's
  fallback for that runner will not reproduce under independent audit. The
  explicit-declaration requirement itself is the owner directive of
  2026-08-09; the resolver is unchanged.
- NO hand-added metadata in runner-emitted files (caches, receipts). The cache
  format is fixed and machine-written — header keys, `----- stdout -----` and
  `----- stderr -----` sections, no timestamps anywhere
  (`scripts/runner_cache.py` module docstring). Review records live in the
  note, not in machine-emitted artifacts. Owner directive of 2026-08-09 for
  the prohibition as stated here.
- Exit-code honesty: a nonzero exit that is by design is recorded as
  `nonzero_exit` — the status the envelope itself writes for a nonzero exit
  (`scripts/runner_cache.py` `execute_and_write_cache`) — with the design
  reason stated in the note; never rewrap or launder it into `ok`. Owner
  directive of 2026-08-09 for the note-side design-reason requirement.
- After ANY edit to a pinned file, rerun the affected runners through the
  envelope and re-pin (checker pins of primary sha/blob, receipt pins of final
  bytes). A pin against pre-edit bytes is a defect: the cache binds the
  runner's content SHA-256 and a fingerprint of its declared
  `AUDIT_INPUT_PATHS`, and consumption rejects input drift
  (`scripts/runner_cache.py` module docstring), while the review-time
  readiness gate blocks PASS on a stale or failed SHA/input-bound compute
  result (`docs/ai_methodology/skills/review-loop/SKILL.md` "Changed-science
  evidence-readiness PASS gate").
- A runner-emitted read inventory must separate two kinds of read: external or
  ancestral scientific inputs (data the result depends on) and package-local
  integrity reads (the runner's own source for a self-hash, a paired source and
  receipt it verifies). An absolute sentence such as "this runner performs zero
  repository reads" is a defect whenever integrity reads exist; state the honest
  form — no external scientific input is read, and name the integrity reads that
  are. This is the full-surface consistency rule of section 3 applied to the
  runner's own self-description. Owner directive of 2026-08-09 for the
  two-kinds separation as an authoring rule.

## 3. Claim-scope honesty

- State exactly what the runner computed: finite domain, declared parameters,
  bounded scope. Words that claim more than the computation —
  "certified", "closed", "complete", "global", "maximal", "the law" — are
  demotion targets unless the computation actually establishes them
  (`docs/ai_methodology/skills/review-loop/SKILL.md` Fix Policy step 2:
  "Demote overclaimed status when the artifact supports only support/bounded
  language").
- Full-surface consistency: the claim scope must match on EVERY surface —
  note prose, title/headline, runner docstrings, emitted certificate strings,
  machine-status block, receipts, closing verdict line. Demoting the note while
  a docstring still overclaims is a confirmation failure (seen twice). The
  surface enumeration is the Native-language PASS gate's: changed headings,
  metadata, runner banners, claim scopes, table labels, and review comments
  (`docs/ai_methodology/skills/review-loop/SKILL.md` "Native-language PASS
  gate").
- Structured status fields carry only values from their own enum. A claim class
  (`positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`, `decoration`,
  `meta`) is not a status and must never appear in a status field, and no field
  may carry a hybrid phrase spanning two families
  (`docs/repo/CONTROLLED_VOCABULARY.md` "Audit Lane Field Vocabulary";
  `docs/ai_methodology/skills/review-loop/PREFLIGHT.md:33-43`). Source-note
  `Status:` lines carry exactly `proposed_retained` or `proposed_promoted`.
- Domain-explicit naming; no `near/far`-style frame-relative names where a fixed
  designation exists. No campaign/block/lane-opening language in scientific
  headlines. No unregistered labels or block/campaign fields in machine records.
  Campaign names, PR-specific labels, and branch-local/draft framings are owned
  by `RepoGovernanceReviewer` and the Native-language PASS gate
  (`docs/ai_methodology/skills/review-loop/SKILL.md`); the frame-relative
  naming rule is the owner directive of 2026-08-09.
- No bare letter-number names for new science. `A1`, `A2`, `G1`, `R3`,
  `Route F`, `Block 2` and their kin are overloaded across axioms, assumptions,
  Lie types, lane stages, route codes, and branch blocks; they must not be used
  as titles, claim scopes, runner banners or headlines, primary table labels, or
  review findings. Use an explicit scientific noun phrase; a shorthand may
  follow only as a parenthetical alias, and archival aliases belong only in
  clearly historical work-history or archive material
  (`docs/ai_methodology/skills/review-loop/SKILL.md:147-152,594-605`).
- Any noun phrase the PR introduces to categorize claims, lanes, or tiers must
  already exist in `docs/repo/CONTROLLED_VOCABULARY.md` or be plain descriptive
  prose. Coining a class word is a defect even when the concept is real; say the
  process fact instead, or defer it explicitly through the review loop's
  vocabulary path — never land it silently
  (`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:44-55`).

## 4. Negative claims: the N-gate

The trigger set is the canonical one and is NOT limited to explicit no-go
headlines. A PR MUST answer all of N1-N8 in writing when any cycle artifact,
PR body, source note, runner, or review verdict it ships asserts:

- a `no_go` result ("structurally closed", "no route exists", "no retained
  primitive supplies this");
- a `stretch_attempt_negative` outcome ("the attempted route does not close");
- a `bounded_with_named_walls` result ("conditional on N open
  conditions/walls");
- a derived no-go boundary inside a POSITIVE theorem ("the per-element
  identity does not lift");
- an audit-conditional verdict rationale that names a residual wall.

Authority for the trigger set and the checklist:
`docs/ai_methodology/skills/no-go-discipline/SKILL.md:23-46` (when to invoke)
and `:48-260` (N1-N8 and the binding Output artifacts); the same trigger is
wired at `docs/ai_methodology/skills/physics-loop/SKILL.md` "NO-GO DISCIPLINE
GATE". The checked-in gate binds every N1-N8 statement to evidence in the
restricted audit packet (`docs/audit/scripts/no_go_discipline_gate.py`).

- N1: at least **five materially distinct** attack routes, each with a
  one-sentence statement of what the route would attempt, a one-sentence
  statement of why it fails with its authority cited, and exactly one honesty
  marker — `ATTEMPTED` (tested this cycle) or `RULED OUT BY PRIOR`, which
  requires an existing **retained** authority, cited, not merely a pinned prior.
  Two routes are distinct only when they materially differ in primary
  object/formulation, load-bearing mechanism or invariant, or terminal proof
  obligation; different agents, notation, or artifact types do not make distinct
  routes. Fewer than five distinct routes means the no-go is premature: list
  what you have and stop.
- N2: the full pairwise independence table of the walls, WITH collapse applied —
  dependent walls collapse and the headline claim uses the collapsed set.
- N3: hidden-wall scan. Re-read your own proof for "we assume", "by
  construction", "as is standard", "the framework provides", "bridge context",
  "background", "naturally", "obviously", "standard QFT", "registered",
  "canonical", and close variants. Classify every hit as cited retained
  authority, hidden condition (promote to an explicit wall and re-run N2), or
  annotated non-load-bearing context.
- N4: a per-citation table: path:line, residual the witness attacks, residual
  claimed closed, match y/n. Drop every non-matching citation and recount the
  witness support; if the recount falls below what the claim needs, the claim is
  unsupported.
- N5: rhetoric audit. For every phrase of the form "X is not a Y-fact", list the
  per-element, per-site, per-mode, per-block, and lattice-wide versions, which
  resolutions were actually tested, and whether the negative holds at the
  untested ones; replace any over-broad phrase with the narrowest accurate one.
- N6: partial-closure and primitive scan. Before writing "this requires a new
  axiom", scan for reframings that move the wall from physics to convention,
  existing interpretation-stance notes, controlled-vocabulary entries naming the
  residual as labeling-only, and in-flight convention-ratification PRs; report
  path, status, and what each would close. Separate approved framework
  primitives (registered in `docs/audit/data/axiom_premise_nodes.json`) from
  walls — a registered primitive chain-satisfies its dependency without making
  the claim bounded, and a proposed but unapproved primitive has zero premise
  weight. Run `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` before
  writing "no retained primitive supplies this" or any equivalent wall language.
- N7: steelman. Write the strongest one-paragraph argument against your own
  no-go in a hostile reviewer voice, naming a concrete unclosed mechanism and
  terminal obligation with its strongest supporting authority. If the steelman
  is convincing, the no-go is premature: demote and ship the steelman as the
  next cycle's target.
- N8: cross-cycle echo. Search for prior cycles, notes, or campaigns that named
  similarly shaped walls. For each, record whether it has since been retired and
  by what mechanism, and whether that mechanism could apply here. A similar wall
  retired by a mechanism you have not considered means the no-go is premature.

Two artifacts must LAND with the PR; a PR body is not a landing surface, and the
packet family that existed at review time but did not land is this repo's largest
audit-invalidation class:

1. the complete N1-N8 answers as a committed artifact — a `## No-Go Discipline
   Gate` section in the source note itself, or a committed
   `NO_GO_DISCIPLINE_CHECKLIST.md` that the note links;
2. the N5 execution certificate in the primary runner's cached stdout — one line
   each for `per_element:`, `per_site:`, `per_mode:`, `per_block:`,
   `lattice_wide:`, each a substantive (>= 40 character) statement of what the
   runner actually resolves at that granularity, using "checked and not
   executed — <reason>" where a class is genuinely not exercised. The validator
   is `docs/audit/scripts/forensic_evidence_readiness.py`;
   `docs/audit/scripts/check_changed_audit_evidence.py` checks it at review time.

Withdrawing the negative claim to a bounded positive observation removes the
N-gate obligation — but then NO residual sentence may still function as a no-go.
Counterexamples are existence witnesses, not refutation theorems: publish the
witness (the observed firing, the constructed configuration) and scope the
positive claim to its declared domain. Any sentence quantifying over "any
generalization/extension/broader reading" is itself a derived no-go boundary and
owes the full N-gate. This must hold on EVERY surface (see claim-scope section),
including checker-emitted strings and receipts.

## 5. Proof obligations

Authority: `docs/ai_methodology/skills/review-loop/SKILL.md:1131-1137`. Any PR
claiming a theorem, proof, derivation, reduction, or closure through intermediate
lemmas MUST, in the note:

- state the exact target claim being proved, in one sentence, before the proof;
- reconstruct the obligation graph: every lemma the argument leans on, and for
  each, whether it is proved here, cited to a retained authority, or open;
- preserve hypotheses through every step — a hypothesis silently dropped between
  lemma and theorem is a defect, not a simplification;
- state the boundary and degenerate cases the argument covers and those it does
  not;
- name the strongest missing lemma explicitly.

Two shapes are non-conformance and must be fixed or demoted before review, not
argued about during it:

- **circular reduction** — the reduction's terminal lemma is the target itself,
  or follows from the target as readily as the target follows from it;
- **target-equivalent or stronger terminal lemma** — the reduction ends at a
  lemma at least as strong as the target. This forbids "proof-complete" or
  "near-closure" framing outright and requires demotion to `open_gate`, to
  support, or to the strongest independently proved lemma.

Stating the honest boundary requires no new science.

## 6. Runner validity: fail-closed and independent math

- Every new or changed runner check is mutation-checked: one load-bearing
  mutation per check family, applied on a scratch copy or reverted immediately,
  and the check MUST fail under it. Record the mutations you ran in the PR body
  (`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:85-90`). A check that
  asserts the formula it is supposed to test confirms nothing.
- Forced-green predicates, hard-coded or self-supplied targets, pass-through
  gates, tamper gates that cannot detect tampering, and category-error checks
  (a check that tests a different object than the claim) are the recurring
  defect family this rule exists to catch. Cache freshness is not runner
  validity.
- Every changed runner, proof script, numeric constant, matrix construction,
  optimizer, expected value, or note formula additionally needs at least one
  check that does NOT share the changed runner's implementation path: manual
  formula derivation, symbolic or algebraic reduction, finite toy-case
  enumeration, independent recomputation, or invariant/limit tests. Record which
  one was used (`docs/ai_methodology/skills/review-loop/SKILL.md:1119-1129`). A
  runner that computes its own target and prints PASS proves nothing about the
  formula.

## 7. Packet completeness (audit reachability)

- Every runner whose output the note's claims rely on must be inside the claim's
  restricted audit packet: either imported by the primary runner or declared as
  `packet_helper_runner:` in the note's machine-status block.
- A declared helper needs the claim-scoped mapping (claim id to runner paths) in
  `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
  `docs/audit/scripts/build_citation_graph.py`. Record that mapping verbatim as
  a reviewed **hard landing condition** in the note's own Review record, so it is
  a durable reviewed artifact rather than PR-body text — see the landed exemplar
  `docs/LOCAL_CLOCK_RELATION_CYCLE869_BOUNDED_THEOREM_NOTE_2026-07-28.md`
  ("Outstanding at landing ... as hard landing conditions").
- The registry edit is subject to the dependency-policy impact gate: a branch
  that changes citation/dependency extraction policy must inspect the pipeline's
  resulting invalidation set before PASS, with a fresh scientific audit for every
  mismatching fingerprint as the safe default; narrowing that blast radius takes
  a separate, reviewed machine-readable equivalence/impact record, and
  `docs/audit/data/legacy_science_epoch_baseline.json` is never refreshed to make
  a policy change pass (`docs/ai_methodology/skills/review-loop/SKILL.md:865-878`).
- Open policy debt, and how to stay correct across its repair: the helper
  registry is currently recorded as unresolved dependency-policy epoch debt on
  `origin/main`, because refreshing the epoch mass-invalidates roughly 860-891
  legacy audits; the disposition is owner-governed
  (`docs/repo/ACTIVE_REVIEW_QUEUE.md`, item
  `2026-08-08-dependency-policy-epoch-debt-helper-registry`). An owner-approved
  amendment scoping the claim-scoped helper registry out of the governed
  dependency-policy bytes is in review on branch `epoch-policy-pass-20260809`.
  The rule that holds either way: declare the mapping as a reviewed hard landing
  condition, do not edit the registry on the PR branch on your own authority, and
  confirm against
  `docs/audit/scripts/audit_science_fingerprint.py` `DEPENDENCY_POLICY_SOURCES`
  at your HEAD whether the registry is still governed. If it is, the impact gate
  applies and the mapping waits on the queue item's owner decision; once the
  amendment lands and the registry is out of the governed set, the mapping is an
  ordinary reviewed landing condition with no epoch consequence.
- Verification: on a disposable tree at `origin/main` + this delta + the mapping,
  `python3 docs/audit/scripts/check_changed_audit_evidence.py --base
  origin/main --include-worktree --json` must show the row forensic-ready with all load-bearing
  runners in `changed_surfaces` and `helper_runner_paths` populated.

## 8. Links, citation graph, and generated artifacts

- Load-bearing dependencies are markdown links; backticks seed no citation-graph
  edge. Provenance-only and decorative references stay in backticks and must not
  link. Every markdown link the delta adds or changes must dereference to one
  git-tracked regular file or a web URL — directory targets, untracked targets,
  absolute paths, and paths outside the repository are all violations
  (`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:56-64`).
- Run the pipeline and read the citation-graph delta gate (stage 18 against the
  tracked manifest at stage 1b). For every node your change adds, removes, or
  rewires, confirm the edge identity is intended — read your source diff against
  the manifest diff — BEFORE acknowledging it. Acknowledgment is staging the
  refreshed manifest, so an unintended edge acknowledged is an unintended
  dependency landed (`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:65-74`).
- Manifest co-landing is proactive and commit-time, and the trigger is graph
  TOPOLOGY, not markdown links alone. When the landing adds or removes ANY
  graph node, or rewires any dependency edge, the landing set MUST INCLUDE a
  refreshed `docs/audit/data/citation_graph_manifest.json`, generated on the
  proposed landing tree with the serialized
  `docs/audit/scripts/run_citation_graph_build.py` launcher then
  `docs/audit/scripts/write_citation_graph_manifest.py` and staged before
  commit and push. A new note is a new node whether or not it carries a single
  markdown link: `build_citation_graph.py` registers every non-skipped
  `docs/**/*.md` file as a node before extracting any edge, and
  `write_citation_graph_manifest.py` requires acknowledgment for every added,
  removed, or rewired node. A zero-edge note addition therefore changes
  `node_count` and needs the manifest exactly like an edge rewire. Omitting it
  blocks the enforced stage-18 guard on every subsequent pipeline run on `main`
  (`docs/ai_methodology/skills/review-loop/SKILL.md` proactive manifest rule in
  the landing loop; `docs/ai_methodology/skills/physics-loop/SKILL.md`
  citation-graph carve-out).
- Regeneration DURING landing is a narrow generated-artifact exception. After
  cherry-picking any frozen commit set that carries
  `citation_graph_manifest.json`, regenerate it from the integrated tree before
  every push attempt, even when Git reports no conflict, and amend the newest
  cherry-picked commit only when the generated bytes changed. Two independent
  topology additions can merge textually while coalescing their `node_count`
  increments, leaving a semantic mismatch that current-tree regeneration must
  catch. The landing worktree must have no tracked residue at entry; between
  retries only the generated manifest may be restored to the current `HEAD`,
  never arbitrary reviewed source. A manifest-only cherry-pick conflict is
  resolved by the same
  regeneration, never by hand-merge, and needs no new reviewer round. Any other
  conflict fails the landing closed and returns the PR to its worker for
  re-review on a rebased head
  (`docs/ai_methodology/skills/review-loop/SKILL.md` fail-closed landing loop).
- `docs/repo/ACTIVE_REVIEW_QUEUE.md` and `docs/CANONICAL_HARNESS_INDEX.md` are
  not append-only. The queue's own rule is that a resolved item is removed from
  the open list and recorded in the queue history or the linked packet
  (`docs/repo/ACTIVE_REVIEW_QUEUE.md:7-16`), and the harness index is an index,
  not a queue. Write entries so that an overlap at landing resolves by keeping
  both the current-`main` entry and this PR's entry, each in its correct place;
  a union of two appended blocks is one landing technique, not the update
  contract for either file.
- Receipts live in `outputs/`, caches in `logs/runner-cache/`; nothing else
  writes outside the delta's declared file set. `outputs/` and `logs/` are the
  repository's run-artifact and transient-output buckets
  (`docs/repo/REPO_ORGANIZATION.md`), and the canonical cache path
  `logs/runner-cache/<runner-stem>.txt` is fixed by
  `scripts/runner_cache.py` (module docstring). Never stage with `git add -A`:
  stage explicit paths only
  (`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:99-107`); the
  `git add -A` prohibition itself is the owner directive of 2026-08-09.

## 9. Note structure

- Machine-status block: complete, and consistent with the receipts and every
  other surface. Use the real field names from
  `docs/ai_methodology/skills/physics-loop/SKILL.md`. The status contract
  (`:399-412`) requires `actual_current_surface_status`, whose value is one of
  `open`, `no-go`, `exact-support`, `bounded-support`, `conditional-support`,
  `demotion`, `candidate-retained-grade`, together with `target_claim_type`,
  `trace_class`, `reachability_to_target`, `conditional_surface_status`,
  `hypothetical_axiom_status`, `admitted_observation_status`,
  `claim_type_reason`, `audit_required_before_effective_retained`, and
  `bare_retained_allowed: false`. There is no `surface_status` field.
- The trace contract (`:278-288`) additionally requires `trace_class`
  (`direct_blocker_closure`, `upstream_support`, `negative_route_pruning`,
  `frontier_discovery`, `methodology`), `target_claim_id`,
  `target_blocker_text`, `source_of_blocker_text` (`null`, `audit_ledger`,
  `review_loop`, `handoff`, `user_goal`, `frontier_question`),
  `reachability_to_target`, `artifact_role`, and `next_trace_action`. A support
  note declares `trace_class: upstream_support` and names its downstream
  consumer, or says explicitly that the consumer is not yet known — the relation
  is a `trace_class` value, not a free-form attachment.
- `packet_helper_runner:` where section 7 applies.
- Imports section: every underivable input named in plain language, with its
  provenance stated or stated to be unavailable, and with role, provenance, and
  open-bridge status kept in separate fields. For example: "comparator
  convention imported from the source cited below; provenance for its
  normalization is not available in-repo". Do not coin a status token for this;
  imported physics, textbook machinery, observations, fitted values, and
  conventions are labelled in prose
  (`docs/ai_methodology/skills/review-loop/SKILL.md:725-738`). Open bridges are
  declared open and owned by the correct lane.
- A Review record section when the PR replaces or narrows earlier content: what
  was dropped or refuted, where the retained scope ends, and any hard landing
  conditions (section 7). Owner directive of 2026-08-09 for this requirement;
  its shape follows the landed exemplar
  `docs/LOCAL_CLOCK_RELATION_CYCLE869_BOUNDED_THEOREM_NOTE_2026-07-28.md`
  ("Outstanding at landing ... as hard landing conditions").

## 10. Propose/ratify boundary

The author lane proposes; the independent audit lane ratifies. An author PR MUST
NOT write, pre-state, or recommend `audit_status`, `effective_status`, an audit
verdict or its rationale, an auditor transcript, a `previous_audits` entry, or a
generated ledger, queue, prompt, or publication effective-status output. Audit
fields are auditor-owned and `effective_status` is derived by the pipeline
(`docs/repo/CONTROLLED_VOCABULARY.md` "Audit Lane Field Vocabulary"); the
independent audit lane is the sole channel that refreshes the hash and
re-ratifies (`docs/ai_methodology/skills/review-loop/SKILL.md:1179-1192`).

- Do not run `docs/audit/scripts/apply_audit.py` from an author branch.
- Validation runs generate audit surfaces. Restore them before committing and
  stage explicit paths only; shipping them is a defect, and a source repair's
  hash drift on a previously audited row is resolved by re-audit, never by
  committing ledger churn.
- The one allowed generated artifact in a landing set is
  `docs/audit/data/citation_graph_manifest.json`, and only when the landing
  changes citation-graph topology (section 8).
- If the branch introduces retained-grade `claim_type` rows, say so plainly in
  the PR body as work for the independent audit worker — that is a referral, not
  a verdict.

## 11. Sourced facts, counts, and generators

Distinct from scientific imports: this is provenance for the PR's own factual
statements. Authority:
`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:14-31`.

- Every sentence characterizing a claim, a note, or a status is written with the
  authority open — the note's own claim/boundary section, the ledger shard, or
  the registered policy doc — and asserts nothing stronger than that source's
  own wording. Session memory, PR titles, and campaign shorthand name targets;
  they are never quotable claim text. If you did not just read it, do not write
  it.
- Every count, total, aggregate, or date is recomputed at your current HEAD from
  its authority, not carried forward from an earlier session or summed across
  overlapping sets (double-counted totals were a repeat repair). Values that move
  with the nightly carry an as-of stamp naming the state they quote, and one
  document must not carry two incompatible as-of dates.
- A generator that accompanies a volatile number must genuinely derive the whole
  output from its authority and fail closed when the derivation disagrees with
  its pin. A generator that re-states author-supplied values reproduces nothing;
  the alternative is an honest dated stamp, not a decorative script.

## 12. Pre-review gates

Run from a worktree with no untracked pipeline residue (clean generated caches
first). Authority:
`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:92-107`.

- `python3 scripts/vocab_lint.py --fix` on the changed files, then
  `python3 scripts/vocab_lint.py --report-only <delta files>` reports zero
  findings.
- `bash docs/audit/scripts/run_pipeline.sh` exits 0.
- `python3 docs/audit/scripts/audit_lint.py --strict` exits 0 with no errors
  (pre-existing warnings and notices may remain).
- `python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main --include-worktree`
  names no missing runner, missing declared input, missing current compute
  result, or incomplete N5 certificate for any affected non-meta, non-open,
  non-decoration row. Include staged, unstaged, and untracked author/review
  changes before committing; the CLI default sees committed changes only.
  This is preflight only: the independent audit reruns the
  runner live and inherits no author verdict.
- Restore generated validation outputs, stage explicit paths only, and confirm
  `git status` shows exactly the intended files.
- `git diff --check <merge-base>..HEAD` is clean. Plain `git diff --check`
  inspects only the working tree and reports clean on a committed PR whose delta
  carries whitespace errors, so it does not satisfy this gate. The
  `git diff --check` requirement is owned by
  `docs/ai_methodology/skills/review-loop/SKILL.md` (the post-fix pipeline
  block); the merge-base strengthening is the owner directive of 2026-08-09.
- `python3 -m py_compile` on every added or modified Python file
  (`docs/ai_methodology/skills/review-loop/SKILL.md` Smoketest).
- Prep sanity for stacked PRs: the reviewed delta must equal
  `merge-base(base-branch, head)..head`, and its file count must match an
  independently computed delta before any reviewer is launched. The
  merge-base review base is owned by
  `docs/ai_methodology/skills/review-loop/SKILL.md` (Setup step 3) and the
  stale/stacked overlap check by its Stale PR Integration Guard; the
  independent file-count cross-check is the owner directive of 2026-08-09.
- Read the complete diff once, cold, as the reviewer would
  (`docs/ai_methodology/skills/review-loop/PREFLIGHT.md:109-112`). Every hunk
  you cannot justify in one sentence from a source you just read is a hunk
  the reviewer will bounce.
