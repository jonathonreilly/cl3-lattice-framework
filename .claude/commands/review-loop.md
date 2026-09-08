# /review-loop — Physics Review Loop

Run the repo-native physics review loop from:

`docs/ai_methodology/skills/review-loop/SKILL.md`

## Invocation

`/review-loop [target] [focus] [--max-iterations N] [--no-fix] [--no-commit]`

Mode selection:
- **Zero arguments** (`/review-loop`): the parallel open-PR backlog drain
  per the skill's Default Entry — enumerate open non-draft, non-reserved PRs,
  form coherent frozen review units, and land independently confirmed units
  through the skill's continuously collected trains of at most eight.
- **Named `[target]`** (a branch or PR): focused mode — review only that
  target's changes against `origin/main` or `main`.
- **Free-text `[focus]` without a target** (e.g. `/review-loop imports`):
  the backlog drain with that review emphasis applied in every slot.
- **ANY flag without a named target is invalid** (including
  `--max-iterations`): flags configure a focused single-target run, and
  `--no-fix`/`--no-commit` contradict the drain's land-end-to-end
  contract; a bare flag form must stop and ask for a `[target]`.

## Required Behavior

1. Read the skill file above before acting.
2. Select the mode per the Invocation section above; focused mode only
   when a `[target]` is named.
3. Use one independent Astra-low (`gpt-6-astra`, `low`) reviewer per coherent
   unit. Apply the relevant physics lenses in one focused pass. Escalate only
   unresolved material mathematical/premise questions or reviewer disagreements
   to Astra xhigh. Completed valid reviews remain reusable. Follow the skill's
   focused-landing section: concise material findings and decisive evidence;
   exhaustive claim certification belongs to the deferred formal audit.
4. Fix only verified, narrow findings. Demote overclaims instead of patching
   missing science with prose. Use the skill's overlap-repairs guidance for
   authorized early finding handoffs against immutable originals, safe-boundary
   priority for same-session final confirmations, early publication/input checks,
   and reuse of verified mechanical facts. Early handoffs are provisional;
   complete final source review, independent mathematics and exact current-main
   integration remain required. Preserve owner-frozen backlog membership and
   actual execution/attempt limits; never restamp evidence after an input change.
5. Enforce audit-system compatibility without running the independent audit:
   no bare `retained` / `promoted` status lines. Run focused source/runner/
   premise checks per unit; perform one full `docs/audit/scripts/run_pipeline.sh`,
   `python3 docs/audit/scripts/audit_lint.py --strict`, and changed-evidence
   validation on the exact integrated current-main candidate. Reuse an identical
   successful base/tree receipt only under the skill's full provenance rule;
   do not require duplicate per-PR or per-unit full runs.
6. Treat review as the pre-landing source gate; the independent audit must
   judge the landed claim without an expectation of agreement. Block PASS when a changed claim has missing graph
   dependencies, author-prewritten audit verdicts, stale retained-status
   assumptions, or a runner that does not test the load-bearing bridge.
7. For math-bearing runner/proof changes, do not trust PASS output alone:
   independently cross-check load-bearing formulas, signs, factors,
   normalizations, expected values, and edge cases before landing.
   Reconstruct nontrivial proof-obligation graphs and reject proof-complete
   framing when the terminal missing lemma is target-equivalent or stronger.
8. Before classifying a dependency as an import, wall, conditional/open input,
   or bounded-status source, read
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`,
   `docs/audit/data/axiom_premise_nodes.json`, and any relevant primitive
   source note. The registered `scale_reference_primitive` grants the Planck
   scale reference as units conversion only; it is not a bounded Planck import.
   The registered `kinetic_isotropy_primitive` grants only structural OS0
   kinetic-form isotropy `c_t = c_s`; it is not a bounded import, Lorentz
   theorem, dynamics, scale, spacing-ratio theorem, selector, or empirical
   input. The registered `realized_state_primitive` grants only pointwise evaluation at a supplied law-admissible realized state; it does not supply a state, state-selection rule, measure, typicality or genericity assumption, weighting, probability rule, or any state-contingent value (quantities that vary across the law-admissible family remain registered data).
9. Focus re-review on files changed by the fix pass. Inspect necessary unchanged
   dependencies and callers when the fix affects a prior conclusion; record the
   path and reason. Record any newly necessary edit as a bounded scope expansion
   and review that delta before treating it as covered by PASS.
10. Before closing or rejecting a non-landable PR, run the skill's salvage pass:
   preserve any durable, runner-backed lemma in the same requested landing path
   with a canonical claim type, and explicitly reject only the pieces that
   cannot be salvaged without new science.
   Non-science audit/status or hygiene PRs still need a utility review:
   salvage durable audit-graph, cache, queue, normalization, dependency-chain,
   or audit-readiness repairs into source/tooling/pipeline changes and
   regenerate generated surfaces instead of rejecting them just because they
   are not theorem science.
11. Draft PRs are excluded by default. Explicit owner-directed draft triage
    permits review and a close-with-reason or mark-ready disposition after
    exact-head verification. Mark-ready is not PASS and still-draft PRs cannot
    land. Preserve owner-reserved exclusions, including inherited content.
12. End with a concise report covering imports/support status, retained/bounded
    disposition, salvage disposition, audit-readiness, commits, checks, and
    remaining manual science.
13. After final source confirmation, freeze each unit's complete constituent
    claim/content disposition map, PR heads, source/input hashes, reviewed
    commits/tree/base, findings hash, and original reviewer session. Enroll it
    in the skill's double-buffered landing train of at most eight units. Depart
    with a useful ready batch as soon as the coordinator is available; no fixed
    collection wait. The combined mechanical gate runs once in one clean
    integration worktree, verifies every frozen PR head
    immediately before push, pushes atomically, verifies containment, and
    rechecks each head immediately before its own close. The next empty train
    opens as soon as the old membership freezes. Source conflicts, moving heads,
    or changed semantic interactions hold the affected unit and its dependents
    for original-session confirmation. Verify accepted constituent source on
    current main before closing and preserve rejected/deferred recovery handles.
    A named focused target flushes as a one-component train once confirmed
    unless explicitly added to an ongoing backlog drain.

## Non-Negotiables

- Every imported or measured value must be identified.
- Support-only results must not be promoted to retained claims.
- Source-note `Status:` lines may not contain bare `retained` or `promoted`;
  use `proposed_retained`, `proposed_promoted`, `support`, `bounded`, or
  `open`. The audit lane alone grants effective retained status.
- Authors and review packets must not prefill audit verdicts such as
  `target_audit_status: audited_clean`, `audit_status = audited_clean`, or
  `effective_status = retained`; say that audit status is set only by the
  independent audit lane and effective status is pipeline-derived.
- Load-bearing dependencies in changed claim notes must be markdown links that
  seed the citation graph. After the audit pipeline, changed claim rows must
  show the intended deps in their tracked
  `docs/audit/data/ledger/<claim-id-prefix>/<claim-id>.json` shards.
- New landed science must use explicit repo naming from
  `docs/repo/CONTROLLED_VOCABULARY.md`. Do not approve bare overloaded labels
  such as `A1`, `A2`, `G1`, `R3`, `Route F`, or `Block 2` as theorem/lane
  names, table labels, claim scopes, runner headlines, or review findings.
  Use names such as `Qubit` / `site possibility` / `one-site possibility
  domain` (the local algebraic presentation fixed by
  `MINIMAL_AXIOMS_2026-06-29.md`, with `Cl(3,0)` as equivalent notation),
  `Lattice` / `Z^3 lattice`, `Admissibility` / `local constraint`,
  `Record` / fixed record readout,
  `Koide Frobenius-equipartition condition`, or `Lie type A_1`; the
  `M_2(ℂ)` / `Cl(3,0)` / qubit names are labels for the same one-site
  algebraic presentation. Keep shorthand only as a parenthetical legacy alias.
- `retained`, `retained_bounded`, and `retained_no_go` are the retained-grade
  dependency statuses. Reviewers must reject stale exact-status checks that
  require only `effective_status = retained` when bounded/no-go retained
  grades are valid.
- Approved primitives listed in `docs/audit/data/axiom_premise_nodes.json`
  chain-satisfy dependencies without making rows `retained_bounded`. Do not
  call the registered `scale_reference_primitive` a Planck import, missing
  premise, no-go wall, or bounded-status source. Do not
  grant it more than `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` declares. Do not
  call the registered `kinetic_isotropy_primitive` a missing
  premise, no-go wall, bounded-status source, Lorentz theorem, dynamics, scale,
  spacing-ratio theorem, selector, or empirical input; do not grant it more
  than `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` declares. Do not
  call the registered `realized_state_primitive` a missing
  premise, no-go wall, bounded-status source, state-selection rule, measure,
  typicality assumption, weighting, or value source; do not grant it more
  than `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` declares.
- `/review-loop` must not apply audit verdicts. It prepares
  audit-compatible review surfaces and reports which proposed claims require
  the independent audit worker.
- `/review-loop` is review, not audit. It may run the compatibility pipeline
  and strict lint, but it must not claim an audit verdict, apply auditor
  results, or describe its review as an audit.
- `/review-loop` must not create or open pull requests. If science is
  salvageable, land the source-only salvage and dependency-chain/audit-queue
  repairs as part of the current landing path; otherwise close or reject the
  existing PR with a clear reason.
- A PR whose purpose is repairing a stuck terminal ledger row
  (`audited_conditional` / `audited_renaming` / `audited_failed` /
  `audited_numerical_match`) must leave that row requeue-able: the row's own
  note or paired runner must change in the PR, or the PR must ship
  machine-readable re-audit targeting metadata (a dispatcher sidecar) naming
  the row. Dependent-side edits alone never reschedule the stuck row. When
  the audit-named repair is dependent-side only (for example, narrowing
  dependents' citing sentences), add a dated downstream-hygiene line to the
  stuck row's own note boundary as part of the landing — a source-side fact,
  no grade language. Verify with the validation pipeline that the row
  re-enters the queue, then restore generated audit outputs per the
  pipeline-output-stripped gate.
- `/review-loop` excludes drafts by default; explicit draft-triage authorization
  permits inspection and close/ready decisions, never still-draft landing or a
  shortcut from mark-ready to source PASS. Owner reservations remain in force.
- When integrating PRs, `/review-loop` must not checkout whole files from a
  stale PR head over current `main`. Compute the PR merge base, detect overlap
  between files changed on current `main` and files changed by the PR, and use
  three-way patch/rebase/merge/cherry-pick integration for overlapping paths.
  Whole-file checkout is allowed only for new paths or paths proven unchanged
  on current `main` since the PR base.
- The repo baseline is the four named axioms in
  `MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit, Admissibility, and Record.
  Name them explicitly; do not compress them to bare `A1` / `A2` / `A3` /
  `A4` labels. Do not classify that baseline as a new premise,
  regulator interpretation, or optional theory language. Do not let that
  baseline silently promote separate species identifications, selectors,
  probability or occurrence rules, K/CPT or central-sector structure,
  P2/modulus, log-det structure, source/action bridges, empirical matches, or
  parent theorem/status surfaces. The current baseline includes: no possibility
  is privileged; possibilities are distinguished by the supplied algebraic
  structure alone; no site is privileged; sites are distinguished by the
  supplied lattice structure alone; readout value is determined by record
  content alone; a state is a configuration of records; and a law privileges
  no states, has a supplied condition as its domain, and gives exactly one
  answer where that condition holds.
- Nature-grade retention requires axioms, approved primitives, or retained dependencies,
  decisive artifact support, clear falsifiers, and no hidden semantic bridge.
- Math-bearing runners require independent formula review: PASS lines do not
  establish that the runner's expression, sign, factor, normalization, or
  expected value is correct.
- Branch-local or draft-PR vocabulary, including language leaked from PR230 or
  similar long-lived drafts, must be translated to native repo language before
  landing.
- Closing a PR must not discard durable science. Salvage narrow
  theorem/no-go/open-gate lemmas into canonical source-only landing commits
  when the runner directly supports the narrowed claim and no audit
  verdict/status language is carried over.
- Closing a PR must not discard durable audit-process value either. A generated
  audit/status diff can be evidence of a real repo defect; land the underlying
  source/tooling/pipeline repair when it strengthens auditability, but never
  treat hand-authored generated status as the authority.
- Delete a closed PR's head branch **only if durable content actually landed**
  (salvaged to `main`, or merged), no deferred content still needs its recovery
  handle, and a just-fetched head still equals the
  frozen reviewed SHA. For a same-repository branch, require an exact
  `--force-with-lease=<ref>:<frozen-head-sha>` deletion and close only after it
  succeeds; leave fork heads intact. If the head moved, leave both PR and branch
  open for fresh review. **Do not delete the branch when a PR is closed without
  landing its content** (rejected / nothing salvaged / salvage deferred) --
  keep it as the handle on the un-landed work. Never delete a head that still
  backs another open PR, nor `main`.
- Live unresolved review findings belong in `docs/repo/ACTIVE_REVIEW_QUEUE.md`.
- Long historical packets belong in `docs/work_history/repo/review_feedback/`.
