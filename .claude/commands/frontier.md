# /frontier — Frontier Map & Gap Analysis

You are the Research Strategist mapping explored vs. unexplored territory for
the qubit-lattice axiom framework.

## Data Collection

1. Freeze `origin/main` after a best-effort fetch when allowed, and report its
   SHA and freshness. Read status counts from that exact committed snapshot,
   without materializing or mutating audit outputs in the candidate checkout:
   ```bash
   python3 - <<'PY'
   import collections, io, json, subprocess, tarfile
   revision = subprocess.check_output(
       ['git', 'rev-parse', '--verify', 'origin/main^{commit}'], text=True).strip()
   payload = subprocess.check_output(
       ['git', 'archive', revision, 'docs/audit/data/ledger'])
   eff, ct = collections.Counter(), collections.Counter()
   with tarfile.open(fileobj=io.BytesIO(payload)) as archive:
       for member in archive:
           if member.isfile() and member.name.endswith('.json'):
               with archive.extractfile(member) as source:
                   row = json.load(source)
               eff[row.get('effective_status')] += 1
               ct[row.get('claim_type')] += 1
   print('snapshot:', revision)
   print("effective_status:", dict(eff))
   print("claim_type:", dict(ct))
   PY
   ```
   If `origin/main` is unavailable or the archive cannot be read, report lookup
   failure; do not substitute candidate HEAD as main. A cached remote ref with
   failed fetch is usable only with its remote freshness explicitly unverified.
2. Audit-lane backlog: `docs/audit/AUDIT_QUEUE.md` depth and
   `docs/audit/data/reaudit_candidates.json` at the same printed snapshot SHA.
3. Lane surfaces: `docs/repo/LANE_REGISTRY.yaml`,
   `docs/work_history/repo/LANE_STATUS_BOARD.md`,
   `docs/repo/ACTIVE_REVIEW_QUEUE.md`.
4. Candidate loop state: `OPPORTUNITY_QUEUE.md`, `NO_GO_LEDGER.md`, and
   `HANDOFF.md` on relevant campaign branches. Identify branch/revision,
   uncommitted state, inherited hypotheses, completed critical checks, open
   obligations, and the next milestone. Candidate progress is separate from
   landed-main and audit-ratified state.
5. In-flight work: `gh pr list --state open` (science and physics-loop
   branches), plus recent landings:
   `git log <MAIN_SHA> --oneline --since="2 weeks ago" -- docs/ scripts/`.
   Never use unqualified current-branch history as evidence of landing.
6. `README.md` package state at the pinned main revision. Read the main lane
   surfaces in item 3 at that same revision, treating historical boards as
   history; candidate packs are planning evidence, not status authority.

## Analysis

### 1. Lane Census
- Group active work by lane/domain. For each: retained-grade results,
  bounded results with named conditions, open gates, standing no-gos.
- Present as a table: | Lane | Retained | Bounded | Open gates | No-gos | Status |

### 2. Blocker Fanout (the keystone view)
- Which open gates, unaudited rows, and `audited_conditional` blockers sit
  upstream of the most downstream work? Use the ledger `deps` graph (and
  load-bearing/descendant fields where present) to rank blockers by how much
  they could unblock. Verify that these are actual scientific dependencies;
  raw citation fanout is a planning signal, not automatic priority. Compare the
  exact physical obligation, first decisive check, uncertainty, and cost.

### 3. Premise Coverage
- Which named conditional inputs and imports are still load-bearing, and
  which lanes are queued to derive or eliminate them?
- Which named derivation lanes (dynamics, Born weights, readout bridges,
  species identification, ...) have no active work at all?

### 4. Confirmed vs. Unvalidated
- Landed-and-audited (retained-grade), landed-but-unaudited, and candidate
  working results are separate. Use Git containment for landing, the ledger
  for ratification, and campaign evidence for provisional checks. A retained
  label never supplies hypotheses beyond the exact audited scope.

### 5. Dead Ends
- Read standing no-go proofs and `NO_GO_LEDGER.md` routes at exact scope.
  Re-entry needs material evidence: a compatible new mechanism, changed
  obligation map, scope correction, counterexample, or justified premise
  change. A new label or worker alone does not reopen a route.

### 6. Highest-Value Gaps
Rank the top 5 unexplored or under-explored targets by:
- expected evidence value for a physical target (could it retire an import,
  discharge an obligation, discriminate alternatives, or prune a proved family?);
- feasibility with existing runners vs. new code;
- estimated effort (interactive / unattended block / multi-day campaign).

## Output

Write to `.claude/science/frontier/{date}-frontier-map.md`:

```markdown
# Frontier Map: {date}

## Coverage Summary
{ledger counts, queue depth, open PRs, active loops}

## Lane Census
{table}

## Blocker Fanout
{ranked blockers with what each unblocks}

## Premise Coverage
{load-bearing open obligations/imports and their derivation lanes}

## Top 5 Highest-Value Gaps
1. {gap} — {why it matters} — {effort}
...

## Scoped Obstructions And Reopen Conditions
- {route} — {proved scope or attempted-search limit} — {material evidence needed to reopen}
```

## Rules

- No lock needed — read-only analysis.
- Do not fabricate coverage. If a lane has no artifacts, say so.
- Distinguish unexamined routes, bounded searches with unresolved alternatives,
  and proved obstructions at stated scope. A no-go title or lack of a successful
  attempt does not establish global exhaustion.
- The gap ranking is the most important output — spend the most thought
  there. This skill pairs naturally with `/progress`.
- Mapping only: this skill proposes targets, it does not move claim states.
  Execution belongs to `/physics-loop` or an interactive science session.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
