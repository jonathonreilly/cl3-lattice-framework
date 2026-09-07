---
name: review-loop
description: Use when an LLM agent needs to run `/review-loop`, review branch changes, run parallel physics-specific reviewers, identify overclaims/imported values/support-only material, apply narrow honest fixes, verify audit-system compatibility without applying audit verdicts, and re-review only files changed by those fixes.
---

# Review Loop

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Run a local review/fix/re-review loop for this physics repo. This is not a
generic software review. Its job is to protect the live claim boundary:
retained/Nature-grade claims must have artifact support, imported values must
be explicit, and support-only results must not be promoted by prose.

## Model And Tool Boundary

Review-loop is a text/code/math review path. Run it with the user's configured
highest-tier Codex reviewer model and maximum available reasoning for this
repo. Resolve the current model from the active configuration; dated model
names in process prose are not configuration. Respect an explicit owner
choice of model or reasoning tier for the episode. Do not switch to lower-reasoning models for convenience, and
do not use image-generation, image-editing, presentation, document-rendering,
or visual-generation tools unless the user explicitly asks for a separate
visual artifact task.

If a run surfaces an image-generation model/tool error such as a stale
`gpt-image-*` tool configuration, treat it as a local Codex tooling/config
problem, not as part of review-loop. Do not retry the review by invoking
imagegen, changing the science-review model, or routing science review through
visual tooling.

This skill is **review only**. It may make branch/package hygiene changes that
allow the independent audit system to parse and queue claims, but it must not
apply audit verdicts, write `audited_clean`, or run the audit worker.
Audit results have a strict provenance boundary: review-loop must never land
PR-submitted audit verdicts, audit-status promotions/demotions, effective-status
changes, auditor transcripts, or `apply_audit.py` outputs as authority. Audits
come only from the independent post-landing audit loop. PRs may land source
repairs, runners, controlled-data dispatch sidecars, and explicit audit or
re-audit targeting metadata when those are review-clean; they may not carry the
answer to the audit they request.
It must not create or open pull requests. When reviewing an existing PR or
branch, review-loop either fixes/narrows that existing landing path and lands it
when requested, or rejects/closes it with a clear reason. Salvage, dependency
chain repair, audit queue regeneration, and parent re-audit gates are part of
that same landing path, not follow-up PRs.
Delete a closed PR's head branch **only when durable content actually landed** --
its reviewed content was salvaged to `main`, or it was merged. Immediately
before closing, refetch the PR head and require the frozen head SHA. If it moved,
leave the PR open and the branch intact for a fresh review of the new head. For
an unchanged same-repository head, delete only with an exact lease, for example
`git push --force-with-lease=refs/heads/<head>:<frozen-head-sha> origin
:refs/heads/<head>`, and close the PR only after that deletion succeeds. A fork
head that cannot be lease-deleted from `origin` may be closed but must be left
intact. **Do NOT delete the head branch when a PR is closed without landing its
content** -- rejected as non-landable with nothing salvaged, or with salvage
deferred to a later pass: keep that branch as the working handle on the
un-landed work. Never delete a head that still backs another open PR, nor `main`
or a protected branch. (Closed PRs retain their commits either way; the live
branch matters as the recovery handle precisely when the content did not land.)
It auto-corrects status vocabulary and terminology so a PR follows repo
conventions by running `scripts/vocab_lint.py --fix` on all
branch-modified files before any landing gate. Vocabulary is canonical
in
[`docs/repo/controlled_vocabulary.yaml`](../../../repo/controlled_vocabulary.yaml)
(design in
[`VOCABULARY_HYGIENE_DESIGN.md`](../../../repo/VOCABULARY_HYGIENE_DESIGN.md)).
Routine local drift that has a non-link-aware rewrite rule, such as legacy
aliases and deprecated wording, is rewritten mechanically as part of the
same review commit; this is never a science blocker. Link-aware filename
suffix migrations and F-letter finding-label migrations are reported but
deferred to Cleanup-2 tooling. Genuinely new terms, pending link-aware
renames, or pending F-letter migrations that `vocab_lint` cannot
mechanically rewrite are recorded as
`prose_status: needs_human_vocab_decision` for the periodic
vocab-extension review; they do not block the landing. Review-loop
must not introduce new repo-wide axioms, new theory
language, new retained-surface claims, framework primitives, or new
foundational premises without explicit user approval. Imports are allowed for
bounded theorem surfaces when they are scoped, labelled, and
dependency-checked; repo-wide axiom additions and primitive additions are not
review-loop fixes.

## Premise Authority

<!-- BEGIN GENERATED: axiom-baseline (generate_skill_axiom_baselines.py) -->
Review-loop must enforce the two supplied premise types. Repo-wide axioms and
explicitly approved framework primitives are registered in
`docs/audit/data/axiom_premise_nodes.json` and chain-satisfy dependencies
without making downstream rows `retained_bounded`. No admission class exists;
`docs/audit/data/premise_decision_history.json` is provenance only and never
chain-satisfies. Do not infer a registered node's current grant or boundary
from a summary in this skill. Before naming a changed dependency as a premise,
import, wall, or bounded-status source, perform the mandatory authority reads
below; the registered current source files control. New axioms and new
primitives both require explicit owner approval and a reviewed registry/policy
update before review-loop may treat them as accepted premises.

Generated by `docs/audit/scripts/generate_skill_axiom_baselines.py`.
**Mandatory authority read:** before any premise, import, wall, or dependency
judgment, read the current axiom memo, primitive registry check, registry data,
and every relevant primitive source listed below. This roster is a freshness
router, not a content substitute; the cited source grant and boundary control.
Do not hand-edit inside the markers.

- axiom authority: `docs/MINIMAL_AXIOMS_2026-06-29.md`
- primitive classification procedure:
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
- primitive registry: `docs/audit/data/axiom_premise_nodes.json`
- `scale_reference_primitive`: `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
- `kinetic_isotropy_primitive`:
`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`
- `realized_state_primitive`:
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
<!-- END GENERATED -->

## Claim Boundary

Do not land new science under bare letter-number names such as `A1`, `A2`,
`G1`, or `R3`; those labels are overloaded with axioms, assumptions, Lie
types, lane stages, route codes, and branch blocks. Use the explicit
scientific name on live science surfaces; archival aliases belong
only in clearly historical work-history/archive material. Review-loop must
not treat the framework baseline as a
new axiom, new supplied premise, regulator interpretation, or optional
theory language. Correcting a PR back to this repo language is allowed. This
does not promote downstream science by itself: physical-species
identifications, `C_3`-breaking selectors, kinetic-branch selectors,
readout/scale/unit bridges, and empirical matches remain separate
bounded/open inputs unless they have their own retained-grade derivation and
independent audit closure.

Review must remove preventable source and packaging defects. The later
fresh-context audit independently tests the claim and may disagree; agreement
is not its objective. Do not pass branches that
leave the audit lane to discover basic claim-boundary, dependency-graph,
status-vocabulary, or runner-validity defects. Do not lose durable science
when a PR fails that bar: before closing or rejecting a branch, run the
salvage pass below and preserve any narrow, runner-backed lemma that can be
made canonical without changing the science.
Review-loop is still not the audit loop: it must never apply verdicts or
describe its review as an audit. Its job is to decide whether source/tooling
math, claim boundaries, and repo language are honest enough to land and be
sent to the independent auditor afterward.
Non-science PRs require the same discipline: do not reject generated
audit/status or hygiene-only work just because it is not theorem science.
First decide whether it exposes a real audit-graph, cache, queue,
normalization, dependency-chain, or audit-readiness defect. If it does,
salvage the value into durable source, tooling, pipeline, or controlled-data
repairs and regenerate the generated surfaces from that repair.
Audit-dispatch manifests are a special non-science case. If a PR lands a
source note whose purpose is to request future re-audit, retagging, cascade
repair, or batch audit selection, review-loop is not done when the source note
lands. It must also make the request machine-visible by adding or updating a
supported dispatcher sidecar under `docs/audit/data/`, rerunning the audit
pipeline, and verifying the target appears in `docs/audit/AUDIT_DISPATCH_QUEUE.md`
or `docs/audit/data/audit_dispatch_queue.json`. The dispatch manifest is
target-selection metadata only; it must not be passed to auditors as evidence
and must not apply audit verdicts.

## Default Entry: Parallel PR Review, Any Orchestrator (owner-directed 2026-07-17)

An UNSPECIFIED invocation — no named branch or PR — IS the parallel
backlog drain, as is invoking against a SET of open PRs ("review the open
PRs", "drain the PR backlog"): enumerate the backlog, review in parallel, and
land confirmed components through the double-buffered trains below — no
topology decisions required from the invoker. Free-text
focus without a named target (e.g. "imports") is the drain with that
emphasis applied in every slot. Reviewing one branch or one PR is the
special case that requires naming the target, and ANY flag without a named
target is invalid — stop and ask for a target (see Arguments; the
review-only flags contradict the drain's land-end-to-end contract).

1. **Enumerate targets**: open, non-draft PRs in scope (drafts stay out of
   scope per the draft rule below). Detect stacks and cumulative-tower
   branches first; stacked PRs review and land bottom-up as deltas, never in
   parallel with each other.

   Before allocating a reviewer wave, run
   `python3 scripts/review_loop_backlog_inventory.py` (use `--json` for the
   complete machine-readable snapshot). It amortizes the GitHub enumeration
   into one read-only `gh pr list` invocation and reports declared-base stack
   order, unresolved bases, registered worktrees and unregistered `rev-*`
   recovery candidates, external findings files, disk and observed worker-CLI
   headroom, and capacity-bounded candidate slots. Re-run it before each wave
   because PRs, worktrees, disk, and the shared process pool move independently.

   The helper's `ready` label means only `baseRefName == main` with no detected
   existing checkout or PR-scoped recovery artifact. It never launches a worker and grants no review,
   science, merge, audit, or landing readiness. Its topology is limited to
   declared GitHub base edges: still perform the cumulative-history,
   merge-base, and independent delta checks here, and still run every lens and
   gate below. Inspect every reported existing worktree/findings path for
   ownership and recovery before creating a duplicate; the helper never
   prunes, removes, or modifies one.
2. **One isolated worktree per PR.** Parallel reviews never share a
   worktree or a checkout; shared worktrees race and have destroyed findings
   in this repo's history.

   **Worktree lifecycle (disk discipline — mandatory).** Concurrent reviews
   plus abandoned per-cycle confirm trees have repeatedly exhausted the host
   disk. Guard on free space and remove each verified-clean worktree on exit:

   ```bash
   # POSIX df reports 1 KiB blocks here; check the filesystem that will hold WT.
   REPO_ROOT=$(git rev-parse --show-toplevel)
   REVIEW_TMP_ROOT=${TMPDIR:-/tmp}
   git -C "$REPO_ROOT" worktree prune
   avail_kb=$(df -Pk "$REVIEW_TMP_ROOT" | awk 'NR == 2 {print $4}')
   case "$avail_kb" in
     ''|*[!0-9]*) echo "ENOSPC guard: cannot read free space for $REVIEW_TMP_ROOT" >&2; exit 1 ;;
   esac
   [ "$avail_kb" -ge 5242880 ] || {
     echo "ENOSPC guard: less than 5 GiB free on $REVIEW_TMP_ROOT — not spawning" >&2
     exit 1
   }

   WT=$(mktemp -d "$REVIEW_TMP_ROOT/rev-<N>.XXXXXX")
   cleanup_review_wt() {
     [ -e "$WT" ] || return
     python3 - "$REPO_ROOT" "$WT" <<'PY_REVIEW_CLEAN'
   from pathlib import Path
   import sys
   sys.path.insert(0, str(Path(sys.argv[1]) / "scripts"))
   from science_fix_loop import cleanup_worktree
   removed, reason = cleanup_worktree(Path(sys.argv[2]))
   if not removed:
       print(f"cleanup retained worktree for recovery: {sys.argv[2]}: {reason}", file=sys.stderr)
   PY_REVIEW_CLEAN
     git -C "$REPO_ROOT" worktree prune
   }
   trap cleanup_review_wt EXIT
   trap 'exit 130' INT
   trap 'exit 143' TERM

   git -C "$REPO_ROOT" worktree add -q "$WT" <branch-or-ref>
   ```

   Apples-to-apples measurement from the same object store on 2026-08-14 was
   343.6 MiB for a fresh full worktree and 326.3 MiB for the proposed sparse
   baseline, only about 5% less. Review and pipeline inputs span every root,
   so a sparse default adds omission risk without a material disk benefit.
   Use a normal full worktree; the operational gain comes from prompt cleanup,
   not from counting the shared Git object store as part of every checkout.

   The `trap` is not optional: it removes a verified-clean worktree on normal
   exit and catchable INT/TERM termination. The shared cleanup helper preserves
   dirty work, valuable ignored artifacts, unverifiable trees, and any HEAD not
   yet preserved on main. It prints the recovery path and never force-removes a
   worktree. This review trap does not delete local branches. `git worktree prune` at the start of a drain clears
   stale metadata whose directories are already gone. Neither mechanism can
   catch `SIGKILL` or remove an abandoned directory that still exists, so
   inventory such directories separately instead of claiming that the trap
   handles every crash mode.
3. **One reviewer process per PR at a time**, applicable lenses combined
   into a single pass (two for large diffs), findings written incrementally
   to `FINDINGS=$(mktemp "$REVIEW_TMP_ROOT/review-findings-pr<N>.XXXXXX")`
   outside the disposable worktree, verdict line last. Freeze the PR's
   original changed-file snapshot before creating that file. Remove it only
   after its findings and verdict are recorded in the PR provenance comment;
   if the worker fails, report its recovery path. The findings file and any
   reviewer scratch artifacts are named scope exclusions — they never enter
   `files_to_review`, the changed-file set, or any commit. This is
   the budget-adapted default of the Reviewer Fanout section below: under
   the shared-pool budget, cross-PR parallelism replaces per-lens
   parallelism; full per-lens fanout inside one PR remains available in a
   quiet pool, and every applicable lens must be explicitly covered either
   way.
4. **Concurrency budget (shared codex pool).** Reviewer processes share one
   pool with the audit lane's auditor seats and judicial panels. Keep the
   TOTAL concurrent codex processes across every lane at or under ~8-10
   (measured 2026-07-17: ~18 concurrent processes collapsed audit-lane
   throughput from 6-11 landed verdicts/hour to ~1 every 3 hours). When the
   audit drain is running at 4+ seats, run at most 2-3 concurrent PR
   reviewers; scale up only in a quiet pool.
5. **Land confirmed PRs in continuously collected trains of at most eight.**
   Review, fixes, and focused confirmation remain per PR and stay in that PR's
   worker. Batching starts only after a component is independently ready to
   land; it never combines science review, shares reviewer context between
   PRs, or turns one PR's PASS into authority for another.

   A component may enter the collecting train only when all of the following
   are frozen together: PR number, original PR-head SHA, exact reviewed commit
   list, resulting tree SHA, confirmation-base SHA, changed-file set, head
   repository and branch, findings file SHA-256, reviewer thread/session
   identity, and that same session's explicit `FINAL VERDICT: PASS`. Focused
   confirmation MUST resume the reviewer thread/session that issued the
   findings. That same reviewer thread/session must confirm fixes;
   do not launch a new reviewer process to confirm fixes.
   Give that reviewer the fixed files, prior findings, and necessary interacting
   context. Record any newly necessary source inspection or edit as a scope
   expansion; a new edit needs confirmation before the component is frozen again.
   If the session cannot be
   recovered, the PR head moved, any frozen value no longer matches, or the
   reviewer did not explicitly pass the final state, fail closed and do not land
   that component; do not enroll it.

   The train scheduler is a double buffer:

   - the first eligible component entering an empty collecting train starts
     its collection clock;
   - eight eligible components close it immediately;
   - otherwise the normal departure boundary is 60 minutes after the first
     component. With a nonempty backlog, the operating target is a full
     eight-component train, not an intentionally small timed batch;
   - at that 60-minute boundary, extend collection only when at least one
     additional PR had already started focused confirmation on a recorded
     head SHA in a recorded reviewer session before the boundary. Only that
     same head/session may use the extension. Close at eight components or at
     the absolute 75-minute boundary, whichever comes first;
   - atomically freeze the departing membership and open the next empty
     collecting train immediately, before the frozen train is integrated. Its
     clock starts when its first eligible component enters. Reviews and
     confirmations that finish during integration therefore feed the next
     train instead of waiting for the landing to finish;
   - stacked PRs never share a train, and independent PRs with overlapping
     non-generated paths do not share a train. Keep the lower stack member or
     earlier-ready component in the current train and route the other to the
     next one after current-main re-review. The citation-graph manifest is the
     sole generated-path overlap handled inside integration.

   In this skill, a **flush** means only “stop collecting and freeze the
   current membership.” It never skips review, confirmation, integration, or
   validation. Automatic flushes are the full-train and time-boundary
   departures above. An operator-requested early flush is useful for an urgent
   ready change or orderly shutdown, but normally hurts throughput by sending
   an underfilled train; do not use it as a routine polling action.
   A named focused-mode target is a requested completion boundary: once it is
   confirmed, flush its one-component train unless the operator explicitly put
   it into an ongoing backlog drain.

   One coordinator owns one clean, disposable integration worktree for the
   frozen train. This is an integration function, not a second reviewer or a
   new source-editing lane. Fetch the latest `origin/main`, verify every frozen
   component again, and cherry-pick the components in deterministic ready-time
   order. Run the Stale PR Integration Guard before each component. A source
   conflict, PR-head change, missing confirmation, or provenance mismatch
   ejects only that component to its original worker for same-session focused
   re-review against current main; rebuild and validate the candidate without
   it. The coordinator may resolve only the generated manifest case below.

   Every component still passes the existing per-PR full pipeline, strict lint,
   changed-evidence gate, all three `diff --check` scopes below, and every
   applicable reviewer lens before enrollment. The combined gate is mechanical;
   it does not replace or routinely repeat the component-scoped semantic
   reviewers. Before running it, compare the components' interacting-file sets
   and dependency edges. If integration changes any reviewed source bytes or
   exposes a cross-component semantic interaction, eject the affected
   components for confirmation by their original reviewer sessions on the
   integrated files. Otherwise their frozen per-component verdicts remain the
   semantic authority.

   On the frozen integrated candidate, run this combined validation pass:

   ```bash
   TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate
   bash docs/audit/scripts/run_pipeline.sh
   python3 docs/audit/scripts/audit_lint.py --strict
   python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main
   ```

   Restore generated audit outputs under the Audit-System Compatibility Gate,
   regenerate the citation-graph manifest when required, and then run the final
   clean-state checks:

   ```bash
   TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate
   review_base=$(git merge-base origin/main HEAD)
   git diff --check "$review_base"..HEAD
   git diff --check
   git diff --cached --check
   ```

   The efficiency gain is only at the redundant landing tail: one current-main
   integration, one combined revalidation, one manifest regeneration, one push,
   and one close pass instead of up to eight separate current-main races. No
   per-PR review or gate is removed, and no component is considered landed until
   the combined gate passes.

   After the combined gate passes, push the exact candidate once to `main`.
   `origin/main`'s fast-forward atomicity remains the serializer. If main moved
   after the train base was fetched, do not replay a stale PASS or force-push:
   fetch, rebuild the entire candidate on the new base, rerun the combined
   gate, and try the ordinary fast-forward push again. A
   conflict touching only `docs/audit/data/citation_graph_manifest.json`
   is resolved by regenerating it from the landed tree
   (`build_citation_graph.py` then `write_citation_graph_manifest.py`),
   never by hand-merge; a manifest regeneration touches only that generated
   acknowledgment surface, so it needs no new reviewer round — any OTHER
   conflict fails the landing closed and returns the PR to its worker for
   re-review on a rebased head. PROACTIVE rule, not just on conflict: when
   the commits being landed change citation-graph TOPOLOGY — adding or
   removing any graph node, or rewiring any dependency edge — the landing
   set must INCLUDE a
   refreshed `docs/audit/data/citation_graph_manifest.json`
   (`build_citation_graph.py` then `write_citation_graph_manifest.py`,
   staged into the landing) — otherwise the enforced stage-18 guard blocks
   every subsequent pipeline run on main until someone lands the
   acknowledgment for you. `build_citation_graph.py` registers every
   non-skipped `docs/**/*.md` file as a node before extracting any edge, so
   a newly added note with zero markdown links is a node addition and
   triggers this rule exactly like an edge rewire.
   After cherry-picking a frozen commit set that carries the manifest, rerun
   those generators on the integrated tree before EVERY push attempt, even
   when Git reports no conflict. Git can merge two independent topology
   additions without a textual conflict while coalescing their `node_count`
   increments; only current-tree regeneration detects that semantic stale
   manifest. Stage the regenerated manifest and amend the newest cherry-picked
   commit when its bytes changed. This generated-only integration repair needs
   no new reviewer round; every source conflict still returns to the reviewer.
   The landing loop refuses any tracked staged or unstaged residue at entry.
   Between retries it may restore only the generated manifest to the current
   `HEAD`, clearing a failed regeneration without discarding reviewed source.
   Generated-output restoration is a COMMIT-time rule (see the
   audit-compatibility gate), not a landing-time step: the component commits
   are already clean. The train's fail-closed landing loop is, exactly:
   ```bash
   # Record these immediately after the combined gate and generated-output
   # cleanup, before entering the push loop.
   VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>
   VALIDATED_TREE=<combined-candidate-tree-sha>
   # Exact reviewed commits from each frozen component, components in
   # ready-time order and each component's commits oldest first.
   COMMITS=(<pr-a-oldest> ... <pr-a-newest> <pr-b-oldest> ...)
   PR_NUMBERS=(<pr-a-number> <pr-b-number> ...)
   PR_HEADS=(<pr-a-frozen-head-sha> <pr-b-frozen-head-sha> ...)
   if [ "${#PR_NUMBERS[@]}" -ne "${#PR_HEADS[@]}" ]; then
     echo "FAILED: PR number/head inventory mismatch" >&2
     exit 1
   fi
   verify_frozen_pr_head() {
     local pr="$1" expected="$2" live_ref actual
     case "$pr" in
       ''|*[!0-9]*) return 1 ;;
     esac
     live_ref="refs/tmp/review-loop-train-pr-$pr"
     if ! git fetch -q origin "+pull/$pr/head:$live_ref"; then
       return 1
     fi
     actual="$(git rev-parse --verify "$live_ref")" || return 1
     [ "$actual" = "$expected" ]
   }
   verify_frozen_pr_heads() {
     local index
     for index in "${!PR_NUMBERS[@]}"; do
       if ! verify_frozen_pr_head \
            "${PR_NUMBERS[$index]}" "${PR_HEADS[$index]}"; then
         return 1
       fi
     done
   }
   refresh_manifest=""
   for commit in "${COMMITS[@]}"; do
     if git diff-tree --no-commit-id --name-only -r "$commit" -- \
          docs/audit/data/citation_graph_manifest.json \
          | grep -qx docs/audit/data/citation_graph_manifest.json; then
       refresh_manifest=1
       break
     fi
   done
   if ! git diff --quiet || ! git diff --cached --quiet; then
     echo "FAILED: landing worktree has tracked residue before integration" >&2
     exit 1
   fi
   landed=""
   for attempt in 1 2 3 4; do
     git cherry-pick --abort >/dev/null 2>&1 || true
     # A failed generator/write/add/amend may leave only the generated
     # manifest dirty after a completed cherry-pick. Restore exactly that path
     # to the current HEAD before retrying; never reset arbitrary reviewed work.
     if [ "$refresh_manifest" = 1 ] \
        && ! git restore --source=HEAD --staged --worktree -- \
             docs/audit/data/citation_graph_manifest.json; then
       echo "FAILED: could not clear generated manifest retry residue" >&2
       exit 1
     fi
     # Name the destination explicitly: isolated/partial repos may have no
     # remote.origin.fetch refspec, in which case a plain fetch leaves the
     # local origin/main stale and creates fake non-fast-forward "races".
     if ! { git fetch -q origin \
              +refs/heads/main:refs/remotes/origin/main \
            && git switch -q --detach origin/main; }; then
       sleep 3; continue
     fi
     if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then
       echo "FAILED: main moved; rebuild and rerun the combined gate" >&2
       exit 1
     fi
     if ! git cherry-pick "${COMMITS[@]}" >/dev/null 2>&1; then
       conflicts="$(git diff --name-only --diff-filter=U)"
       if [ "$conflicts" != "docs/audit/data/citation_graph_manifest.json" ]; then
         git cherry-pick --abort >/dev/null 2>&1 || true
         echo "FAILED: source conflict; return the PR to its worker" >&2
         exit 1
       fi
       if ! { python3 docs/audit/scripts/run_citation_graph_build.py >/dev/null \
              && python3 docs/audit/scripts/write_citation_graph_manifest.py >/dev/null \
              && git add docs/audit/data/citation_graph_manifest.json \
              && GIT_EDITOR=true git cherry-pick --continue >/dev/null; }; then
         sleep 3; continue
       fi
     fi
     # A conflict-free textual merge can still coalesce independent manifest
     # counts. If this landing carries the manifest, rebuild it from the
     # integrated tree on every retry and amend only generated bytes.
     if [ "$refresh_manifest" = 1 ]; then
       if ! { python3 docs/audit/scripts/run_citation_graph_build.py >/dev/null \
              && python3 docs/audit/scripts/write_citation_graph_manifest.py >/dev/null \
              && git add docs/audit/data/citation_graph_manifest.json; }; then
         sleep 3; continue
       fi
       if ! git diff --cached --quiet; then
         if ! GIT_EDITOR=true git commit --amend --no-edit >/dev/null; then
           sleep 3; continue
         fi
       fi
     fi
     if [ "$(git rev-parse 'HEAD^{tree}')" != "$VALIDATED_TREE" ]; then
       echo "FAILED: integrated tree differs from the validated candidate" >&2
       exit 1
     fi
     if ! verify_frozen_pr_heads; then
       echo "FAILED: PR head moved; dissolve the train without pushing" >&2
       exit 1
     fi
     if git push -q origin HEAD:main; then
       landed="$(git rev-parse HEAD)"
       break
     fi
     sleep 3
   done
   if [ -z "$landed" ]; then
     echo "FAILED: landing did not complete after 4 attempts" >&2
     exit 1
   fi
   if ! git fetch -q origin \
          +refs/heads/main:refs/remotes/origin/main; then
     echo "FAILED: could not refresh origin/main for containment verification" >&2
     exit 1
   fi
   if ! git merge-base --is-ancestor "$landed" origin/main; then
     echo "FAILED: $landed not contained in origin/main" >&2
     exit 1
   fi
   echo "LANDED $landed"
   # Build the close-ready set one PR at a time from a post-push head check.
   for index in "${!PR_NUMBERS[@]}"; do
     pr="${PR_NUMBERS[$index]}"
     expected="${PR_HEADS[$index]}"
     if verify_frozen_pr_head "$pr" "$expected"; then
       printf 'CLOSE_READY %s %s\n' "$pr" "$expected"
     else
       echo "LEAVE_OPEN $pr: PR head moved after landing" >&2
     fi
   done
   ```
   Every step is conditioned; push success captures the landed sha; retry
   exhaustion and non-containment both exit nonzero — the loop can never
   report success without the landed sha verified inside `origin/main`.
   A `CLOSE_READY` line is not permission that survives another command. Refetch
   that PR head again immediately before its own close. If it differs from the
   frozen SHA, leave that PR open and its branch intact, and record that only the
   older reviewed head landed. For an unchanged same-repository head, use the
   lease-protected branch-deletion rule above; close only after its exact lease
   succeeds. Never let one moved head prevent unaffected train members from
   being checked and closed individually.

   If combined validation fails, preserve the failing command and log, do not
   push any part of the candidate, and dissolve the train. Rebuild its
   components as one-component trains in deterministic order on fresh current
   main, using the same landing loop and the same per-PR review and same-session
   confirmation requirements. Do not guess a culprit, auto-bisect scientific
   content, or quarantine a PR from a shared failure. This fallback spends more
   validation only on the exceptional failing train and keeps the common clean
   path fast.
6. **Who may kick it off: any orchestrator** — any Claude tier, a codex
   session, or a human. The orchestration is process: every finding and
   every PASS/FAIL verdict comes from the configured reviewer model's seats,
   the orchestrator fixes only per Fix Policy, and nothing lands without a
   reviewer PASS on its final state. The orchestrator never self-certifies.
   Substituting a different reviewer family for a round (for example a
   fresh-context reviewer when the codex lane is unavailable) requires
   explicit owner authorization for that episode and must be disclosed in
   the PR's provenance comment.

7. **Progress reports every 15 minutes.** While any slot is active, emit a
   summary block to the operator surface at least every 15 minutes — never
   silence for a long session: a per-PR table (PR number, phase — reviewing
   round N / fixing / confirmation / landing / landed / closed-with-reason —
   reviewer runtime, and the finding count so far read from that PR's
   incremental findings file), landings so far with their main SHAs, the
   remaining queue, and the current codex process count against the budget.
   A session that stops early still emits a final block with the same
   fields; the Final Report section below remains the full closing artifact.

The per-PR procedure in the rest of this skill, through final confirmation, is
the inner loop of each parallel slot; nothing below is weakened by running
slots concurrently. The train coordinator above is only the shared landing
tail after those independent inner loops pass.

## Author Pre-Flight (input hygiene)

Authors are expected to run [`PREFLIGHT.md`](PREFLIGHT.md) before requesting
review. The pre-flight is authoring discipline, not a gate: it grants no
standing, replaces no reviewer lens, and its absence blocks nothing by
itself — but a reviewer may cite a skipped pre-flight item as a finding when
the defect it would have caught is present. Whether such findings are fixed
in place or the branch is rejected follows the existing Fix Policy and
close-with-reason path; the checklist adds no new disposition.

`docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` is the pre-review
conformance bar the pre-flight serves: authors generate to it, and at review
entry the orchestrator pre-fixes a NARROW set of mechanical subchecks before
a reviewer seat is spent on the PR. The pre-fixable set is exactly:

- link resolution and repository portability (section 8's tracked-regular-file
  / web-URL requirement, and absolute or outside-repository link targets);
- field presence and enum validity in the machine-status and trace blocks
  (section 9), including a value drawn from the wrong enum family;
- removal of forbidden author-written audit outputs and regenerated audit
  surfaces (section 10);
- deterministic command and gate hygiene (section 12): running the linter,
  the pipeline, `py_compile`, the merge-base `git diff --check`, and
  restoring generated outputs so the staged set is exactly the intended one.

Everything else is scientific or dependency judgment and is NEVER pre-fixed
as mechanical: whether an added, removed, or rewired dependency edge is
INTENDED (section 8); which inputs are underivable, their provenance and role,
and which lane owns an open bridge (section 9); claim scope and the honest
boundary reading of section 3; proof content (section 5); runner logic and
validity (section 6); and sections 1, 2, 4, 7, and 11 entire. Those stay with
the reviewer, who is the only seat that may decide them.

Pre-fix is orchestrator repair of mechanical non-conformance under Fix Policy,
not a review: it confers no PASS, it does not shorten or replace any lens, and
nothing lands without a reviewer PASS on the final state.

## Arguments

Parse, in this order:

- `[target]`: optional named branch or PR (a PR number/URL, or a token that
  matches an existing branch). Resolve the target FIRST: a named target
  selects focused single-target mode; anything that is not a resolvable
  branch/PR is focus text, not a target.
- focus text: optional free-text review emphasis. With a target it scopes
  that review; without a target it scopes every slot of the backlog drain.
- `--max-iterations N`: optional iteration cap, default `5`.
- `--no-fix`: review only, do not edit.
- `--no-commit`: fix locally but do not create iteration commits.

ANY flag without a named target is an invalid invocation — flags configure
a focused single-target run and contradict or under-specify the drain
(`--no-fix`/`--no-commit` contradict its land-end-to-end contract) — stop
and ask for a target instead of guessing. Only the zero-argument and
focus-text-only forms select the backlog drain.

## Setup

1. Read the local review/governance surfaces before judging status:
   - `docs/repo/REVIEW_FEEDBACK_WORKFLOW.md`
   - `docs/repo/ACTIVE_REVIEW_QUEUE.md`
   - `docs/repo/CONTROLLED_VOCABULARY.md`
   - `docs/CANONICAL_HARNESS_INDEX.md`
   - `docs/audit/README.md`
   - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
   - `docs/audit/data/axiom_premise_nodes.json` and the source notes named by
     relevant primitive nodes
   - `docs/audit/data/premise_decision_history.json`
   - `docs/KEY_SCIENCE.md` as the current front-of-house router when
     front-facing science changed; it is an index and grants no status
   - the relevant sharded rows under `docs/audit/data/ledger/` when
     quantitative, imported-value, or status-bearing claims changed
2. Determine the base ref:
   - prefer `origin/main` if present;
   - otherwise use `main`;
   - if the current branch is the base branch, use `HEAD~1`.
3. Compute the review base with `git merge-base HEAD <base-ref>`.
4. Build the original changed-file set from committed, staged, unstaged, and
   untracked changes. This is the primary review scope. Read necessary unchanged
   dependencies, callers, schemas, and policy sources from the same snapshot to
   judge those changes; record each contextual path and why it is needed. Context
   inspection does not authorize unrelated edits. If a confirmed fix requires
   another file, record the bounded scope expansion and review its new delta.
5. Record whether the worktree was initially clean. If it was dirty, do not
   auto-commit without explicit user permission unless the slash-command
   invocation clearly requested commit-producing fixes.
6. If the task is to review open/non-landed PRs, include all non-merged,
   non-draft PRs in the requested scope except PRs the user explicitly
   excluded. Draft PRs are out of scope: ignore them entirely and do not land
   them unless the user explicitly asks to inspect a draft PR without landing
   it. Closed-but-unmerged PR heads can be inspected with `gh pr view` and
   `git fetch origin pull/<N>/head:refs/tmp/pr-<N>`.

Useful commands:

```bash
git diff --name-only <base>...HEAD
git diff --name-only --cached
git diff --name-only
git ls-files --others --exclude-standard
git diff <base>...HEAD -- <files>
git diff --cached -- <files>
git diff -- <files>
```

For untracked files, include their full content or a concise new-file summary
in reviewer prompts.

## Stale PR Integration Guard

When landing one or more PRs, protect already-landed science before applying
any branch content. A PR branch may be based before another PR just landed, so
checking out whole files from that stale PR head can erase current-main source
science in shared files.

For every PR before integration:

```bash
git fetch origin \
  +refs/heads/main:refs/remotes/origin/main \
  pull/<N>/head:refs/tmp/pr-<N>
pr_base=$(git merge-base origin/main refs/tmp/pr-<N>)
comm -12 \
  <(git diff --name-only "$pr_base"..origin/main | sort) \
  <(git diff --name-only "$pr_base"..refs/tmp/pr-<N> | sort)
```

If the overlap list is non-empty, or if earlier PRs have landed during the
same review-loop run, do **not** run `git checkout refs/tmp/pr-<N> -- <file>`
for those paths. Integrate the PR's delta against its merge base with a
three-way patch, rebase/merge, or cherry-pick source commits, then resolve any
conflicts by preserving both current-main science and the salvageable PR
science:

```bash
git diff --binary "$pr_base"..refs/tmp/pr-<N> -- <source paths> > /tmp/pr<N>.patch
git apply --3way /tmp/pr<N>.patch
```

Whole-file checkout from a PR head is allowed only when the file is new on the
PR or when `git diff --quiet "$pr_base"..origin/main -- <file>` proves current
`main` has not changed that path since the PR base. For every overlapped
source path, do a science-loss guard after integration: the current-main diff
from `pr_base` to `origin/main` must still be represented in the final file.
If that cannot be verified quickly, stop and treat it as a blocking integration
hazard rather than risking science loss.

Generated audit JSON/Markdown is a special case: do not hand-merge generated
files from stale PR heads. Resolve source files first, prefer the current
`origin/main` generated audit surface, then rerun the audit pipeline and strict
lint to regenerate it.

## Reviewer Fanout

On each iteration, set `files_to_review` to the files that changed since their
last clean review. On iteration 1, use all original changed files.

Run every applicable reviewer lens. Under the shared-pool concurrency
budget (Default Entry above), combine the lenses into one or two passes per
PR — full per-lens parallel fanout through the available agent/subagent
mechanism is the quiet-pool mode. If parallel agents are unavailable, run
the same reviewer passes locally and report that limitation. In every mode,
each applicable lens must be explicitly covered and named in the findings.

### Required Reviewers

- `CodeRunnerReviewer`
  Review changed Python/scripts/log-producing code. Check syntax, decisive
  assertions, hard-coded targets, stale fixtures, literal `True` checks,
  hidden observations, reproducibility, paired runner/output agreement, and
  whether the runner actually tests the note's load-bearing bridge. If a
  runner checks audit-ledger dependency status, it must use the current
  retained-grade set (`retained`, `retained_bounded`, `retained_no_go`) rather
  than hard-coding stale expectations such as exactly `retained`.
  For math-bearing runners, PASS output is not enough. Extract every
  load-bearing formula, sign, factor, normalization, matrix identity,
  optimizer objective, and expected numeric value from the changed code and
  note, then verify them by an independent route before landing: manual
  derivation against the note, symbolic simplification, small-case exhaustive
  enumeration, a second implementation that does not share the same expression,
  or invariant/limit/property checks. Treat self-confirming tests, expected
  values generated by the same implementation under review, missing factor/sign
  checks, or stale reopened bug reports as blocking until the formula is
  corrected or the claim is demoted to a narrower supported boundary.
  Run adversarial mutation tests that corrupt each decisive formula, threshold,
  expected value, or assertion and confirm the runner fails for the intended
  reason; a runner that survives a load-bearing mutation does not validate it.

- `PhysicsClaimReviewer`
  Attack theorem notes, claims tables, publication surfaces, and prose. Check
  semantic bridges, selector assumptions, status labels, exact/bounded/support
  boundaries, and code/prose drift.

- `ProofObligationReviewer`
  Trigger when changed content claims a theorem, proof, derivation, reduction,
  or closure through a nontrivial intermediate lemma. Apply
  [`docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md).
  Reconstruct the exact target contract and proof-obligation graph; check
  hypothesis preservation, admissibility of constructed objects, boundary and
  degenerate cases, circular use of equivalent statements, and whether the
  strongest unresolved lemma is weaker than, equivalent to, or stronger than
  the target. Output `CLOSED`, `CONDITIONAL`, `EQUIVALENT-GAP`, or `FAIL`.
  An elegant reduction ending in a target-equivalent lemma is not near
  closure and must not receive proof-complete framing.

- `ImportSupportReviewer`
  Inventory every measured, fitted, literature, PDG, cosmological,
  normalization, boundary-condition, or convention input. Classify each as
  `zero-input structural`, `framework-derived`, `one computed lattice input`,
  `explicit normalization/boundary condition`, `standard/literature
  correction`, `observational comparator`, `support-only`, `insensitive
  nuisance`, or `unjustified import`. For a Nature-grade retention claim, every
  import must be derived, disclosed as a non-satisfying condition with a narrow role, quantitatively
  insensitive, or the claim must be demoted.

- `NatureRetentionReviewer`
  Apply the hostile external-review bar. Ask whether the result can honestly
  be called retained/Nature-grade: no hidden unit identification, no structural
  redefinition, no imported selector, no unsupported first-principles claim,
  no unmatched observed target, and clear falsifiers/open gates. Output
  `RETAINED`, `RETAINED SUPPORT`, `BOUNDED`, `OPEN`, `NO-GO`, or `REJECT`.

- `NoGoDisciplineReviewer`
  Scrutinize negative claims with the same rigor as positive ones. Trigger
  this reviewer whenever changed content includes a `no_go`, `stretch_attempt`,
  `bounded_with_named_walls`, or derived-no-go-boundary artifact, or when any
  other reviewer in this fanout outputs `NO-GO` / `BOUNDED` / `OVERCLAIM` on
  a negative claim. The reviewer must invoke the `no-go-discipline` skill
  and walk N1-N8 against the branch content (see
  [`docs/ai_methodology/skills/no-go-discipline/SKILL.md`](../no-go-discipline/SKILL.md)):
  N1 alternative-route enumeration (≥5 distinct routes), N2
  wall-independence audit, N3 hidden-wall scan, N4 residual matching,
  N5 rhetoric audit (per-element / per-mode / per-block / lattice-wide
  resolutions), N6 partial-closure path scan (convention-reframe vs new
  axiom), N7 steelman, N8 cross-cycle echo. Output `PASS` (negative claim
  honestly scoped) or `FAIL` with the failing checklist items named and the
  narrowest demoted claim proposed (`partial-attempt-with-named-untested-routes`,
  `partial-narrowing`, `bounded-with-corrected-wall-count`, or
  `stretch-attempt-with-honest-residual`). The reviewer must not approve a
  no-go that has not been stress-tested against the framework's full
  authority surface — under-tested negative claims are at least as harmful
  as overclaimed positive ones because they foreclose investigation paths
  permanently.

- `LabelingConventionReviewer`
  Detect labeling/naming/convention content masquerading as a bounded
  theorem. Trigger whenever changed content includes a `bounded_theorem`
  candidate whose load-bearing claim is a labeling/naming/convention
  statement (parallel to the u/c/t mass-ordering convention or the
  e/μ/τ charged-lepton naming) rather than an algebraic claim with
  explicit named conditions. A labeling convention has no propositional
  premise content, so `retained_bounded` grade does not apply — the
  grade is for algebraic claims with explicit named premises, not for
  stipulations about names.

  The right outcome is to split:
  (i) the algebraic core (if any) ships as a narrow `positive_theorem`
      or `bounded_theorem` with the algebraic premises explicit;
  (ii) the labeling content ships as a separate `meta` convention note,
       parallel to the No-Go Discipline Battery's labeling-vs-physics
       check in
       `docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md`
       ("If labeling, the right outcome is a `meta` convention note").

  Output `PASS` if the candidate is genuinely algebraic with named
  conditions, `SPLIT-REQUIRED` if labeling content is bundled with
  algebraic content (ship the algebraic theorem narrow + the convention
  as a separate `meta` note), or `DEMOTE-TO-META` if the candidate is
  purely convention with no derivation. The reviewer must not approve a
  `bounded_theorem` whose load-bearing content is a labeling stipulation
  — conflating conventions with bounded theorems hides which premises
  are actually load-bearing and prevents downstream rows from cleanly
  identifying their dependency status. Downstream costs of the
  conflation: the bundled convention becomes an undischargeable
  "premise" that blocks the row from reaching retained-unbounded;
  downstream rows that cite the bundled bounded_theorem inherit an
  unstated convention dependency; the audit lane cannot cleanly verify
  "all premises retained" because the convention is not propositional
  content; and future agents may waste cycles trying to "prove" the
  convention as if it were derivable.

- `RepoGovernanceReviewer`
  Check placement and authority surfaces. Ensure live findings route through
  `docs/repo/ACTIVE_REVIEW_QUEUE.md`, long packets go under
  `docs/work_history/repo/review_feedback/`, front-of-house edits update
  `docs/KEY_SCIENCE.md` without treating that index as status authority, status
  wording follows `docs/repo/CONTROLLED_VOCABULARY.md`, and changed claim notes
  are compatible with the audit lane's propose/ratify split. The deferred paper
  package under `archive/publication/ci3_z3/` is record-only; reject any stale PR
  that recreates its former live tree unless the owner explicitly authorizes an
  archive-promotion lane. Also verify that load-bearing dependencies are real
  markdown links that seed the citation graph, not just code-formatted file
  names in prose. Block ambiguous new science names such
  as bare `A1`, `A2`, `G1`, `R3`, `Route F`, or `Block 2` when they appear as
  titles, primary table labels, claim scopes, runner headlines, or review
  findings without an explicit scientific noun phrase. Block repo-wide axiom
  additions, nonstandard theory vocabulary, or new foundational claims unless
  the user explicitly approved that change; vocabulary corrections back to
  repo conventions are allowed.
  Block branch-local or draft-PR language from landing on repo-facing surfaces.
  Long-lived draft wording, PR-specific labels, campaign names, and branch-only
  framings must be translated into native repo vocabulary before merge
  (including language leaked from PR230 or any similar draft branch). If a
  scientific claim is otherwise salvageable, fix the vocabulary in the landing
  commit instead of rejecting the science.

### Optional Reviewer

Run `MethodologySkillReviewer` when files under `docs/ai_methodology/skills/`,
`docs/ai_methodology/`, or `.claude/commands/` changed. Check that the skill is
concise, triggerable from its frontmatter/command name, aligned with the AI
methodology lane, and not claiming physics authority.

## Reviewer Prompt

Use this prompt shape for each reviewer, filtered to only that reviewer's file
scope:

````text
Review the following physics-repo changes.

Files to review:
<files>

Diff/content:
```diff
<diff for only those files; include untracked file content separately>
```

Focus:
<focus text or "None specified">

Context:
- Base ref: <base-ref>
- Iteration: <N> of <max>
- Already reviewed and unchanged: <reviewed_files>
- Repo review surfaces: REVIEW_FEEDBACK_WORKFLOW, ACTIVE_REVIEW_QUEUE,
  CONTROLLED_VOCABULARY, CANONICAL_HARNESS_INDEX, docs/audit/README.md

Rules:
- Findings must cite file/line when possible.
- Separate bugs, overclaims, support-only demotions, imported-value problems,
  repo-governance problems, and nits.
- Do not require new science for wording problems.
- Do not approve retained/Nature-grade language if an import or bridge remains
  hidden.
- Do not apply audit verdicts. Review only whether the branch is ready for the
  independent audit worker.
- Do not approve new bare letter-number science names. Require explicit names
  from CONTROLLED_VOCABULARY, with shorthand only as a parenthetical alias.
- Do not approve a `NO-GO` or `BOUNDED with named walls` recommendation
  without running `no-go-discipline` N1-N8 against the branch content. An
  unscrutinized negative claim forecloses investigation paths permanently and
  is at least as harmful as an overclaimed positive.
- Do not approve proof-complete framing until the ProofObligationReviewer has
  reconstructed the obligation graph and ruled out target-equivalent missing
  lemmas, circular reductions, and uncovered edge cases.
````

## Consolidate Findings

Present one iteration summary:

```text
## Review Results (Iteration N)

### Code / Runner: PASS | RISK | FAIL
### Physics Claim Boundary: RETAINED | SUPPORT | BOUNDED | OPEN | REJECT
### Proof Obligations: CLOSED | CONDITIONAL | EQUIVALENT-GAP | FAIL | NOT APPLICABLE
### Imports / Support: CLEAN | DISCLOSED | DEMOTE | FAIL
### Nature Retention: RETAINED | RETAINED SUPPORT | BOUNDED | OPEN | NO-GO | REJECT
### No-Go Discipline: PASS | FAIL | NOT APPLICABLE
### Labeling Convention: PASS | SPLIT-REQUIRED | DEMOTE-TO-META | NOT APPLICABLE
### Repo Governance: PASS | FIX | QUEUE | ARCHIVE
### Audit Compatibility: PASS | FIX | BLOCKED | NOT APPLICABLE
### Methodology Skill: PASS | FIX | SKIPPED
```

Classify every finding:

- `BUG`
- `OVERCLAIM`
- `NO_GO_OVERCLAIM`
- `IMPORTED_VALUE`
- `SUPPORT_ONLY_DEMOTION`
- `MISSING_ARTIFACT`
- `PROOF_OBLIGATION`
- `EQUIVALENT_STRENGTH_GAP`
- `SEMANTIC_BRIDGE`
- `REPO_GOVERNANCE`
- `AUDIT_COMPATIBILITY`
- `NIT`
- `SALVAGE_CANDIDATE`
- `SALVAGE_REJECT`

Stop immediately when all applicable reviewers are clean.

## Salvage Pass

Run this pass before closing a PR, marking it non-landable, or discarding a
stretch/campaign packet. The goal is to preserve meaningful science without
lowering the review bar.

1. Inventory the branch into these buckets:
   - canonical source candidates: theorem/no-go/open-gate notes and paired
     runners;
   - useful negative results: failed routes that name a durable obstruction and
     have a runner or exact calculation;
   - support-only calculations: exact algebra or bookkeeping that may be useful
     as bounded support but not as retained/Nature-grade science;
   - audit/process hygiene: dependency-graph repairs, audit queue unlocks,
     stale runner-cache detection, generated-data normalization, cycle-break
     hygiene, and pipeline/tooling fixes that make audit results more reliable;
   - non-source material: claim-status certificates, handoffs, campaign state,
     generated audit files, expected audit verdicts, and branch-local logs.
2. For each source candidate, decide whether it can be salvaged with only
   review-level edits:
   - the claim can be narrowed to a canonical `claim_type`:
     `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`,
     `decoration`, or `meta`;
   - all imported physics, textbook machinery, observations, fitted values,
     and conventions are explicitly labelled;
   - the runner tests the actual load-bearing bridge, not just downstream
     arithmetic after the premise is assumed;
   - load-bearing dependencies can be represented as markdown links and
     non-load-bearing siblings can be kept out of the citation graph;
   - the salvage does not rely on a closed, unlanded, unaudited, or rejected
     sibling PR unless the dependency is copied in as a self-contained
     derivation and reviewed in the same salvage branch.
3. Do not salvage by papering over missing science. If the durable part is
   only an obstruction or failed route, salvage it as a narrow `open_gate` or
   `no_go` only when the runner directly supports that negative boundary.
4. Strip all non-source material from salvage branches:
   claim-status certificates, handoffs, campaign state, expected audit
   verdicts, `target_effective_status_*`, `audit_status = ...`, generated audit
   verdict payloads, and branch-local logs.
5. Prefer small salvage slices grouped by coherent topic. Split unrelated
   lemmas rather than bundling them only because they came from the same failed
   PR, but do not open follow-up PRs for those slices. Land them through the
   current requested landing path or report that the work cannot be landed yet.
6. Run the normal audit-system compatibility gate on every salvage slice.
   The resulting rows must remain `unaudited`; the independent audit lane owns
   all verdicts.
7. For audit/process hygiene, preserve the durable repair rather than the
   generated symptom. Land source/tooling/pipeline/controlled-data changes when
   they strengthen the repo or unblock auditing without changing science.
   Regenerate audit JSON/Markdown from the pipeline afterward only from the
   reviewed source repair on current `main`. Do not land PR-authored
   `effective_status`, `intrinsic_status`, `audit_status`, auditor-output,
   previous-audit, or expected-verdict edits as the authority for the change.
   Source repairs may intentionally invalidate a prior row hash and make a row
   visible for re-audit; that is allowed. The independent audit loop must still
   produce the verdict after landing.
8. If no salvage is possible, leave a concise PR comment or review summary
   saying why, for example: "runner only rechecks assumed premise",
   "claim depends on closed sibling", "noncanonical stretch packet with no
   theorem-grade boundary", or "overbroad theorem not supported by runner".

Salvageable examples:

- a parity/counting/no-go lemma with a decisive finite algebra runner;
- a conditional textbook lemma that is useful only when explicitly marked as
  bounded support;
- a negative route that conclusively rules out one proposed mechanism and
  narrows the remaining open gate;
- an audit-hygiene PR whose generated status change reveals a real durable
  graph/tooling/pipeline defect, salvaged as the underlying repair plus
  regenerated audit outputs.

Not salvageable without a new research task:

- branch-local certificates and handoffs with no source theorem;
- broad "closing derivations" whose runner assumes the missing bridge;
- expected audit verdicts or status-elevation packages;
- stretch-attempt notes that document research direction but do not define a
  canonical theorem/no-go/open-gate boundary.

## Fix Policy

If `--no-fix` was passed, do not edit.

Otherwise apply the narrowest honest fix:

1. Fix verified code bugs, broken reproduction commands, stale runner names,
   false PASS checks, and code/prose mismatches.
2. Demote overclaimed status when the artifact supports only support/bounded
   language.
3. If a claimed proof or reduction terminates at a target-equivalent or
   stronger missing lemma, demote the headline to `open_gate`, exact support,
   or the strongest independently proved narrow lemma. Do not describe the
   reduction as near closure unless it contains a genuinely new mechanism for
   the terminal obligation.
4. Mark imported values explicitly; distinguish derived, conditional, fitted,
   measured, literature, boundary-condition, and insensitive nuisance inputs.
5. Add or repair paired runner/note references only when the artifact exists.
6. Make audit-system hygiene fixes only when they do not change the science:
   status-line tier labels, machine-local path removal, stale runner transcript
   refreshes, generated audit queue/ledger seeding, and discoverability wiring.
7. Rename ambiguous science shorthand to explicit repo vocabulary without
   changing the claim boundary. Examples: write `one-qubit operator algebra`
   (or equivalently `M_2(ℂ) ≅ Cl(3,0)`, `physical Cl(3) local algebra` as
   the real-algebra reading — all co-equal labels for the same retained
   algebra-isomorphism class), `Z^3 lattice`,
   `Koide Frobenius-equipartition condition`, or `Lie type A_1` instead of
   bare `A1` / `A2`.
8. Update `docs/repo/ACTIVE_REVIEW_QUEUE.md` for live unresolved findings.
9. Route detailed resolved packets to
   `docs/work_history/repo/review_feedback/` only when a long packet is needed.
10. When a PR is non-landable but salvageable, preserve only the durable
   note/runner content, make the claim boundary canonical, and land that source
   salvage through the current requested landing path. If the rejected branch
   contains substantial non-source packet material, use a clean temporary
   worktree for integration, but do not create or open a follow-up PR.

For any finding it covers, apply the cure stated in
`docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md`, so the same defect
is cured the same way in every slot instead of being renegotiated per PR.
Reviewer prompts and findings may cite its sections by number as shorthand
for the requirement — "conformance spec section 5, target-equivalent terminal
lemma" — but the authority is the skill, script, or vocabulary file that
section cites, and a finding must be justifiable from that authority. Where
the spec and its cited authority disagree, the cited authority wins and the
spec carries a defect: fix the PR to the authority and report the drift.

Skip:

- nits;
- suspected findings without evidence;
- ambiguous science gaps that need new derivation;
- attempts to paper over missing theorem steps with confident prose;
- repo-wide axiom additions, new theory terminology, or new foundational
  premises that lack explicit user approval;
- broad refactors unrelated to the finding.

## Audit-System Compatibility Gate

This gate is mandatory when a branch adds or edits source notes, runners,
claim tables, lane stubs, or publication/control-plane files.

The review loop must enforce the audit lane's propose/ratify split without
performing the independent audit:

**Audit-hash churn guard.** Non-semantic hygiene sweeps on audited source notes
can be scientifically harmless while still invalidating large parts of the
audit ledger, because note hashes are source-content hashes. Before landing any
branch that touches many existing claim-note files for formatting, link-target,
path, vocabulary, or other non-science cleanup, run the pipeline in validation
mode and inspect the `seed_audit_ledger.py` / `invalidate_stale_audits.py`
counts. If the change would reset or requeue already-audited rows solely due to
non-semantic churn, do not land the broad source sweep. Either narrow the PR to
non-ledger/non-claim surfaces, land a reviewed hash/canonicalization tooling
repair first, or ask for explicit user approval to spend the audit capacity.
Never trade a clean audit graph for cosmetic source-note churn without making
that cost explicit.

**Dependency/axiom impact guard.** `science_fingerprint_v2` binds the complete
framework-premise epoch and dependency-policy epoch. A branch that changes an
axiom/approved primitive, premise membership or classification, document
authority/admission registry, citation/dependency extraction policy,
chain-sufficiency policy, or the fresh-look dependency standard must inspect
the pipeline's resulting invalidation set before PASS. The safe default is a
fresh scientific audit for every mismatching fingerprint, including
transitive consumers. Narrowing that blast radius requires a separate,
reviewed machine-readable equivalence/impact record; neither the PR author nor
review-loop may silently declare existing scientific judgments unaffected.
`docs/audit/data/legacy_science_epoch_baseline.json` is an immutable
deployment anchor, not a rolling manifest: never refresh it to make a policy
change pass. A mismatch must invalidate remaining pre-v2 judgments or be
resolved by a separately reviewed, row-specific provenance migration.

0. Before applying a PR, inventory any audit-status surface it touches:

```bash
git diff --name-only <pr-base>..refs/tmp/pr-<N> -- \
  docs/audit docs/KEY_SCIENCE.md \
  docs/repo/FRONT_DOOR_STATUS.md docs/repo/RETAINED_BACKBONE.md
git diff <pr-base>..refs/tmp/pr-<N> -- \
  docs/audit docs/KEY_SCIENCE.md \
  docs/repo/FRONT_DOOR_STATUS.md docs/repo/RETAINED_BACKBONE.md \
  | grep -E 'audit_status|effective_status|audited_clean|audited_conditional|audited_failed|audited_renaming|audited_decoration|audited_numerical_match|previous_audits|audit_result|verdict'
```

Treat this output as a provenance review, not as a merge recipe. Strip
PR-submitted generated ledgers, queues, effective-status tables, auditor
transcripts, and audit verdict payloads before landing. The only acceptable
audit-lane changes from a PR are reviewed source/tooling repairs and
machine-readable audit/re-audit targeting metadata, such as dispatcher
sidecars, that do not assert a verdict. After applying the source repair, run
the local pipeline to verify the row is queued or re-queued as intended, then
restore only generated audit residue to the branch's own `HEAD` before
committing; preserve reviewed source, controlled data, and dispatcher sidecars.
Importing moving `origin/main` into the index of a stale branch stages unrelated
audit changes. Pipeline
regeneration of `docs/audit/data/`, the generated audit queue/dispatch Markdown,
and `docs/repo/FRONT_DOOR_STATUS.md` / `docs/repo/RETAINED_BACKBONE.md` is a
VALIDATION step only; framework PRs must never ship these files because the
merge would overwrite the audit lane's ratified state. The audit-loop run on
`main` (nightly cron plus `audit:` commits) is the sole channel for landing
those outputs.

1. Source-note `Status:` prose is not an audit authority. New or touched claim
   notes should use `Type:` / `Claim type:` metadata for intended audit
   classification.
2. If a no-go/firewall is intended to be theorem-grade, use
   `claim_type = no_go`; do not rely on support-style prose and expect audit
   ratification.
3. Keep disclaimers such as "This is not charged-lepton mass closure" outside
   audit metadata fields.
4. Do not prefill or recommend a verdict in author/review surfaces. Wording
   such as `target_audit_status: audited_clean`, `audit_status =
   audited_clean`, `effective_status = retained`, or "can land audited_clean"
   is not review-loop compatible. Use wording like `audit_status_authority:
   independent audit lane only` and "effective status is pipeline-derived
   after audit ratification and dependency closure."
5. Changed claim notes that cite load-bearing authorities must use markdown
   links, for example
   ``[`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)``.
   Code-formatted names such as `` `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` `` do
   not seed graph dependencies and are not enough.
6. Run the audit pipeline after review fixes:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
review_base=$(git merge-base origin/main HEAD)
git diff --check "$review_base"..HEAD
git diff --check
git diff --cached --check
```

The known graph-cycle warning is acceptable. Any strict-lint error blocks a
review-loop PASS.

6a. **Changed-science evidence-readiness PASS gate (hard).** After the full
pipeline has executed or refreshed every changed runner, run:

```bash
python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main --include-worktree
```

This gate is mechanical preparation, not an audit. It must pass for every
changed row not classified as `meta`, `open_gate`, or `decoration`, including
every such row bound to a changed primary or helper runner. A missing runner,
invalid/unreadable declared input, stale or failed SHA/input-bound compute
result, or incomplete forensic N5 resolution certificate blocks review-loop
PASS. Intentionally incomplete work must be typed as an explicit `open_gate`
and remains outside this seat-readiness gate until promoted; do not let the
independent audit discover a deterministic compute omission after spending a
seat. The cache/result used here is non-authoritative review evidence only.
The audit lane must still execute the current runner live and authenticate its
invocation-bound stdout before applying a verdict.

`--include-worktree` covers the committed delta plus staged, unstaged, and
untracked candidate paths. Use it for author preflight and review fixes,
including `--no-commit` sessions; the default CLI scope covers committed
changes only and cannot establish evidence readiness for an uncommitted fix.
The gate reads working-copy bytes. A path with both staged and unstaged changes
blocks candidate PASS: stage its intended final bytes, or unstage that path for
working-copy review, then rerun. Never use a clean working copy to certify a
different staged version. Recheck after any later source edit or staging change
that changes the bytes proposed for landing.

**`note_hash` drift is a notice for non-retained rows, an error only for
retained-grade rows.** `note_hash` is a *source-content* hash, not an audit
verdict. When a review fix edits a claim note, its `note_hash` drifts from the
seeded value; `audit_lint.py` reports this drift as a non-blocking
`note_hash_drift_reaudit_pending` **notice** when the row is not retained-grade
(`unaudited` / `audited_conditional` / pending), because re-audit is simply
pending and the audit-lane re-seed refreshes the hash. Such a notice does **not**
block review-loop PASS and must **not** be "fixed" by committing audit-lane
ledger churn (that is the forbidden pipeline-output commit). A `note_hash`
mismatch on a **retained-grade** row (`retained` / `retained_bounded` /
`retained_no_go`) stays a hard **error**: an edited retained note laundered past
a stale ratification is a real integrity violation. Resolve it by re-auditing
(the audit lane re-seeds and archives the prior verdict) or by demoting the edit
per the audit-hash churn guard — never by refreshing the hash while keeping the
retained verdict.

**Stuck-row repair requeue gate.** Terminal non-clean rows
(`audited_conditional` / `audited_renaming` / `audited_failed` /
`audited_numerical_match`) re-enter the audit queue only through their own
note or paired-runner hash drift, an upstream `deps_changed` invalidation, or
a dispatcher-sidecar re-audit target. Dependent-side edits never reschedule
the stuck row. When a branch's stated purpose is repairing such a row (the PR
title/body names the row or quotes its audit repair target):

1. Verify the stuck row itself will requeue: its note or paired runner
   changes on the branch, or the branch ships dispatcher-sidecar targeting
   metadata naming the row.
2. If the audit-named repair is dependent-side only (for example, narrowing
   dependents' citing sentences to the audited scope), add a dated
   downstream-hygiene line to the stuck row's own note boundary as part of
   the landing: a one-line source-side record of what changed downstream
   (date + what was narrowed + PR number), with no grade or verdict
   language. The hash drift re-enters the row into the ordinary queue and
   the re-auditor (or second auditor) sees the recorded condition.
3. Run the validation pipeline and confirm the row is queued or re-queued as
   intended, then restore generated audit outputs per the
   pipeline-output-stripped gate below.
4. Repair-PR review checklist: the audit repair target is quoted verbatim
   (from `verdict_rationale` / `notes_for_re_audit_if_any`) in the PR body;
   a sibling-runner pin sweep was done before every note edit (grep
   `scripts/` for runners pinning the edited sentences); no authored grade
   language anywhere; no `docs/audit/data/` content beyond
   dispatcher-sidecar targeting metadata and the citation-graph manifest
   acknowledgment (`docs/audit/data/citation_graph_manifest.json`) when the
   landed commits change graph dependencies (see the landing loop's
   proactive rule).

7. **Pipeline-output-stripped PASS gate (hard).** After running the pipeline
   for validation, the framework PR must NOT land any pipeline-regenerated
   audit-lane or effective-status surface. The independent audit lane is the
   sole authority for these files; a framework PR that ships them creates a
   dual-source-of-truth and overwrites the audit lane's ratified state at
   merge. The following must hold for review-loop to issue PASS:

```bash
# Inventory data changes: distinguish forbidden generated authority from
# reviewed controlled sidecars and the intended topology acknowledgment.
git status --porcelain docs/audit/AUDIT_DISPATCH_QUEUE.md \
                       docs/audit/AUDIT_QUEUE.md \
                       docs/audit/MISSING_DERIVATION_PROMPTS.md \
                       docs/audit/data \
                       docs/repo/FRONT_DOOR_STATUS.md \
                       docs/repo/RETAINED_BACKBONE.md
```

Inspect every listed change. Generated verdict/ledger/queue/status changes
block PASS and must be stripped. Reviewed controlled data and dispatcher
sidecars are allowed when they assert no verdict; the topology manifest is
allowed when the source changes graph topology. Do not erase the entire data
directory or untracked files indiscriminately. The shared helper below
restores only identified generated residue to the branch's own `HEAD`, fails
on errors, and preserves source-side sidecars. Inspect the remaining diff and
regenerate the manifest from the final intended topology before staging.

```bash
python3 - <<'PY_CLEAN'
from pathlib import Path
import sys
sys.path.insert(0, "scripts")
from science_fix_loop import publication_changed_paths, strip_generated_audit_outputs
root = Path.cwd()
strip_generated_audit_outputs(root, publication_changed_paths(root))
PY_CLEAN
# Only when the landed commits add/remove a graph node or rewire an edge:
python3 docs/audit/scripts/run_citation_graph_build.py
python3 docs/audit/scripts/write_citation_graph_manifest.py
git add docs/audit/data/citation_graph_manifest.json
git status --porcelain   # second line of defense: exactly the intended paths
```

The pipeline is run for VALIDATION only — to confirm the source repair is
ingested and the runner row is queued or re-queued as intended. The
audit-loop pipeline run on `main` (nightly cron + `audit:` commits) is the
sole channel for landing the regenerated outputs. Framework PRs that ship
these files force a destructive overwrite of ratified audit state at merge
time and have been an active source of broken-row regressions.

8. **Repository-portable links PASS gate (hard).** Markdown link targets on
   branch-modified `.md` files must be repo-relative or web URLs. Absolute
   local paths such as `/Users/<name>/...`, `/home/<name>/...`,
   `/private/tmp/...`, `/tmp/...`, `/var/...`, `/opt/...`, or `file://...`
   inside a markdown link target are non-portable: they break for other
   developers, CI runners, fresh clones, and independent reviewers.

```bash
# Must produce no output. Scans branch-modified markdown for local absolute
# paths inside markdown link targets.
git diff --name-only origin/main...HEAD -- '*.md' \
  | xargs -I{} grep -nE '\]\((/Users/|/home/|/private/|/tmp/|/var/|/opt/|file://)' {} 2>/dev/null
```

If this command prints lines for files the branch is already modifying for
source, runner, methodology, or review reasons, rewrite the offending link
targets before PASS. The usual mechanical fix is to preserve the display text
and replace the target with a `../` chain relative to the source file's
directory, e.g. in `docs/SOURCE_RESOLVED_FOO_NOTE.md` rewrite
`(/Users/me/Projects/Physics/scripts/foo.py)` to `(../scripts/foo.py)`.

This gate prevents new non-portable links from landing; it is not a license for
large standalone cosmetic sweeps over audited claim notes. If the PR's only
purpose is to rewrite existing local-path links across many audited source
notes, apply the audit-hash churn guard above before landing any broad cleanup.

9. **No-Go Discipline PASS gate (hard).** Before issuing review-loop PASS,
   identify any artifact on the branch that ships a negative claim:

```bash
# Source notes whose claim_type is no_go, or whose Status / Type line
# names walls / open conditions / "conditional on" content
git diff --name-only origin/main...HEAD -- 'docs/*NO_GO*.md' 'docs/*BOUNDED*.md' \
                                           'docs/*STRETCH_ATTEMPT*.md' \
                                           'docs/*OBSTRUCTION*.md'
# Audit-data shards whose verdict_rationale or claim_type record walls
git diff origin/main...HEAD -- docs/audit/data/ledger docs/audit/data/ledger_meta.json \
  | grep -E '"claim_type": "no_go"|"verdict_rationale".*wall|"verdict_rationale".*condition'
# Any source note touched on this branch whose body contains negative-claim shape
git diff origin/main...HEAD -- 'docs/*.md' \
  | grep -E 'structurally undecidable|no retained primitive|requires new axiom|cannot be derived from A_min|conditional on .* walls?'
```

For every match, the NoGoDisciplineReviewer must output `PASS` (N1-N8 walk
complete and no failure condition hit) before review-loop issues PASS. A
`FAIL` from NoGoDisciplineReviewer blocks PASS regardless of how other
reviewers voted. An unscrutinized no-go that ships through review cements
the overclaim at audit time and can wrongly discourage later investigation. Retained no-go conclusions
remain revisable when a proof defect, changed domain, or new mechanism is shown.

If NoGoDisciplineReviewer outputs FAIL, apply the narrowest honest fix per
Fix Policy step 2 (demote to a narrower honest claim that passes N1-N8) and
re-review. Do not weaken the gate to PASS the branch.

This gate is independent of the Pipeline-clean PASS gate above; both must
pass for review-loop to issue PASS.

10. **Math-runner independent-check PASS gate (hard).** Before issuing
review-loop PASS for any branch that changes a runner, proof script, numeric
constant, matrix construction, optimizer, expected value, or note formula,
record the independent math check used by `CodeRunnerReviewer`. At least one
check must not share the same implementation path as the changed runner:
manual formula derivation, symbolic/algebraic reduction, finite toy-case
enumeration, independent recomputation, or invariant/limit tests. A runner
that merely computes its own target and prints PASS is not a proof that the
formula is correct. If an issue was reopened because the runner's math was
wrong, treat the whole formula family as suspect until the changed expression
and any reused helpers are cross-checked.

11. **Proof-obligation scope PASS gate (hard).** When changed content claims a
theorem, proof, derivation, reduction, or closure through intermediate lemmas,
run `ProofObligationReviewer`. `CLOSED` supports the stated proof boundary.
`CONDITIONAL` supports only a claim whose exact premise and narrower scope are
explicit. `EQUIVALENT-GAP` forbids proof-complete or near-closure framing and
requires demotion to `open_gate`, support, or the strongest independently
proved lemma. `FAIL` blocks PASS until the proof is repaired or narrowed.

12. **Native-language PASS gate (hard).** Changed repo-facing text must use
controlled, native repo vocabulary. Run `scripts/vocab_lint.py --fix` on all
branch-modified files before landing, then inspect changed headings, metadata,
runner banners, claim scopes, table labels, and review comments for
branch-local/draft language that the linter cannot know about. PR-specific
labels, draft-branch vocabulary, campaign names, and noncanonical theory
phrases must be rewritten into repo-native language or explicitly deferred in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`; do not land them silently.

13. **Landed-evidence PASS gate (hard).** Audit evidence must LAND with the
PR, not live in its body. For every branch-changed note or runner whose row
the audit lane will consume, run

```bash
python3 docs/audit/scripts/check_changed_audit_evidence.py --include-worktree
```

and treat any reported `forensic_evidence_ready: false` on an affected row as
a blocking finding. In particular, for negative-claim-shaped changes (notes
whose rhetoric trips the N5 scan phrases in
`docs/audit/scripts/no_go_discipline_gate.py`):

- the primary runner's cached stdout must carry the five-line N5 execution
  certificate (`per_element:`, `per_site:`, `per_mode:`, `per_block:`,
  `lattice_wide:` — each honest and substantive, using "checked and not
  executed — <reason>" where a class is genuinely not exercised); and
- the N1-N8 checklist required by the no-go-discipline gate must be a
  committed artifact (a `## No-Go Discipline Gate` section in the note or a
  committed sidecar), not only PR-body text.

Rationale: packets that existed at review time but did not land are the
largest audit-invalidation class in repo history (1,560 voided verdicts;
799 in one day for `no_go_discipline_packet_missing`). A PASS with
un-landed evidence recreates that failure mode. Repairing the evidence
(adding honest certificate lines, landing the checklist) is in scope for
the review; fabricating resolution coverage is not — a runner that
genuinely cannot certify a resolution class states so honestly, and if the
claim's rhetoric then over-reaches the certificate, the claim is narrowed,
not the certificate padded.

The review loop must not run `docs/audit/scripts/apply_audit.py` and must not
write `audit_status`, `audited_clean`, or other audit verdicts. If the branch
introduces retained-grade `claim_type` rows, report those claim IDs in the
final report as requiring the independent audit worker.
When a source repair changes a note or runner for a previously audited row,
the local result is `note_hash`/runner-hash drift plus queue/dispatch
visibility for independent re-audit. For a non-retained row this drift is a
benign `note_hash_drift_reaudit_pending` notice (see the Audit-System
Compatibility Gate) — it does not block strict lint and must not be repaired by
committing ledger churn. For a retained-grade row the drift is a strict error
that must be resolved by re-audit, not laundered. In all cases, do not preserve,
copy, or author a fresh `previous_audits` entry, `audit_status`, or verdict
rationale from the PR branch; the independent audit lane (nightly cron +
`audit:` commits) is the sole channel that refreshes the hash and re-ratifies.

After the pipeline, inspect the changed claim rows in
`docs/audit/data/audit_ledger.json`:

- `claim_type` must match the intended class (`positive_theorem`,
  `bounded_theorem`, `no_go`, `open_gate`, `decoration`, or `meta`).
- `audit_status` must remain `unaudited` unless the branch is only carrying
  already-audited history from `origin/main`.
- `effective_status` must be pipeline-derived, not hand-authored.
- New theorem/no-go/bounded rows with declared load-bearing authorities must
  have non-empty `deps` matching the markdown-linked authorities.
- Dependencies asserted as retained-grade must currently have
  `effective_status` in `{retained, retained_bounded, retained_no_go}`. Open
  gates, `unaudited`, `audit_in_progress`, `retained_pending_chain`, and
  terminal non-clean audit statuses are blockers for retained-grade claims.

Useful review-only inventory:

```bash
python3 - <<'PY'
import json, subprocess
changed = set()
for cmd in (
    ["git", "diff", "--name-only", "HEAD"],
    ["git", "diff", "--name-only", "--cached"],
):
    changed.update(subprocess.check_output(cmd, text=True).splitlines())
try:
    changed.update(subprocess.check_output(
        ["git", "diff", "--name-only", "origin/main...HEAD"], text=True
    ).splitlines())
except Exception:
    pass
rows=json.load(open("docs/audit/data/audit_ledger.json"))["rows"]
for cid,row in rows.items():
    if row.get("note_path") in changed:
        print(cid, row.get("claim_type"), row.get("audit_status"),
              row.get("effective_status"), row.get("deps"),
              row.get("note_path"))
PY
```

If generated audit files conflict while integrating current `origin/main`, do
not hand-merge generated JSON/Markdown. Resolve source files, prefer the
current remote generated audit files, then rerun `run_pipeline.sh` and strict
lint so the generated surface is rebuilt from source.

## Smoketest

After fixes, run the smallest relevant checks:

- `python3 -m py_compile <changed .py files>` for changed Python files;
- changed paired runners directly when they are expected to be short;
- for changed math-bearing runners, independently verify formulas/constants
  before trusting PASS output: compare note equations to code line by line,
  check signs/factors/normalizations, run a second implementation or symbolic
  simplification when practical, and add finite edge-case or invariant checks
  when they would have caught the suspected class of error;
- if many changed runners are part of the branch, execute all practical
  changed runners with a bounded timeout, then rerun any timeout once with a
  longer timeout before classifying it as slow rather than broken;
- any reproduction commands named in changed notes when practical;
- publication/control-plane consistency checks by reading changed tables and
  nearby authority surfaces.
- `bash docs/audit/scripts/run_pipeline.sh` and
  `python3 docs/audit/scripts/audit_lint.py --strict` when claim notes or
  governance/publication surfaces changed.

If a runner is long, stochastic, or requires unavailable data, do not fake the
check. Report it as not run with the reason.

## Re-Review Tracking

Do not routinely repeat clean reviews of unchanged files. Reopen a prior
conclusion when a fix changes its relevant assumptions or interactions.

After each fix pass:

1. Identify files modified by the fix pass.
2. If committing is allowed, create one iteration commit:
   `fix: address physics review findings (iteration N)`.
3. Set `files_to_review` to the files modified by the fix pass.
4. Inspect needed interacting files, including unchanged context, through
   imports, runner/note pairs, canonical harness rows, publication tables, and
   explicit cross-links. Record the affected prior conclusion and reason for
   reopening it. A newly necessary edit expands the recorded changed-file set
   and receives review; it is not covered by an earlier PASS.
5. Loop until clean, no files changed, or max iterations reached.

## Final Report

Report:

- iterations run;
- files reviewed;
- total findings, fixed findings, skipped findings;
- import/support inventory summary;
- final claim-strength disposition;
- audit-compatibility status and proposed claim IDs needing independent audit;
- commits created;
- train membership, departure reason, combined-gate result, landed main SHA,
  and any components returned to single-PR fallback;
- checks run and checks skipped;
- remaining issues with disposition;
- recommendation: `PASS`, `PASS WITH BOUNDED CLAIMS`, or `NEEDS MANUAL SCIENCE`.

Do not claim Nature readiness. Say whether the branch meets this repo's
Nature-grade retention bar or exactly what remains open.
