---
name: no-go-discipline
description: Use when an LLM agent is about to ship a no-go, stretch-attempt-negative, or bounded-with-named-walls claim. Forces structured stress-testing (N1-N8) — alternative route enumeration, wall-independence audit, hidden-wall scan, residual matching, rhetoric audit, partial-closure path scan, steelman, cross-cycle echo — before the negative claim can ship.
---

# No-Go Discipline

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

A structured gate for negative claims. The symmetric counterpart of the V1-V5
Promotion Value Gate in `physics-loop` — V1-V5 prevents overclaiming positives;
N1-N8 prevents overclaiming negatives.

Agents are good at finding one route that fails. They are bad at proving all
routes fail. This skill makes that gap explicit and gates negative-claim output
on a structured stress-test before the claim can ship.

## When to invoke

Invoke this skill **before shipping** any cycle artifact, PR body, source note,
runner, or review verdict that asserts:

- a `no_go` result ("structurally closed," "no route exists," "no retained
  primitive supplies this");
- a `stretch_attempt_negative` outcome ("the attempted route does not close");
- a `bounded_with_named_walls` result ("conditional on N open conditions/walls");
- a derived no-go boundary inside a positive theorem ("the per-element
  identity does not lift");
- an audit-conditional verdict rationale that names a residual wall.

Skills that must invoke this gate before approving negative-claim output:

- `physics-loop` — before any cycle classified `no_go` / `stretch_negative` /
  `bounded_with_walls` can ship to a PR;
- `review-loop` — when any reviewer reports an OVERCLAIM on a negative claim,
  or before a `NO-GO` / `BOUNDED` recommendation is finalized;
- `audit-loop` — before issuing `audited_clean` for a `claim_type: no_go`
  row, or any verdict whose rationale names walls (independent audit
  authority; this gate prevents the audit lane from inheriting the
  source-note's overclaim);
- any future skill that produces negative-claim output.

## The N1-N8 checklist

Each item must be answered IN WRITING before the negative claim can ship, and
the answers must LAND as a committed artifact the audit lane can bind: a
`## No-Go Discipline Gate` section in the source note itself, or a committed
`NO_GO_DISCIPLINE_CHECKLIST.md` that the note links (see Output below). The
cycle's branch-local `CLAIM_STATUS_CERTIFICATE.md` is loop state, not a
landing surface — review-loop's salvage pass strips claim-status certificates
out of a salvage slice — so keep the working copy there if it helps, but the
source note or its linked sidecar is the record. Copying the checklist into
the PR body or a review verdict is a courtesy, never the record.

### N1 — Alternative route enumeration

Name at least **5 distinct attack routes** against the claim being declared
closed. For each route, give:

- one-sentence statement of what the route would attempt;
- one-sentence statement of why the route fails (with retained-authority
  citation);
- honesty marker: `ATTEMPTED` (tested in this cycle) or `RULED OUT BY PRIOR`
  (closed by an existing retained authority — cite it).

Normalize route families using
[`../physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md).
Two routes count as distinct only when they materially differ in primary
object/formulation, load-bearing mechanism or invariant, or terminal proof
obligation. Different agents, notation, or artifact types do not make distinct
routes.

**Packet failure condition:** fewer than 5 distinct routes cannot receive
packet PASS under the current schema. List the real routes and distinguish
the submission limitation from the theorem's mathematical validity. Never
manufacture route families or describe the count itself as disproof.

This five-family minimum is the current packet validator's procedural rule,
not a proof of exhaustiveness. Do not manufacture families or infer that a
mathematical theorem is false because its packet cannot meet the quota. Report
the packet limitation separately; do not claim PASS. The rule must be changed
in the validator and auditor schema before using a different packet contract.

**Why 5:** small enough to be achievable in one cycle, large enough to force
agents off the "I tried one obvious route" failure mode that produced three
out of four overclaims in the v-scale-planck-convention campaign (see
[`references/case-studies.md`](references/case-studies.md)).

### N2 — Wall-independence audit

If claiming multiple walls / open conditions / load-bearing conditionals, produce
a pairwise table. For each pair `(W_i, W_j)`:

- does closing `W_i` automatically close `W_j`? (yes / no);
- does closing `W_j` automatically close `W_i`? (yes / no);
- independent? Only assert this when both non-implications are justified;
  absence of a known implication is not proof of independence. Record
  unknown relations as unresolved, without inventing a wall count.

Collapse all pairs where one wall follows from another. The claim must use
the **collapsed** wall set, not the inflated raw set.

**Failure condition:** if the pairwise table shows any wall follows from
another but the source-note still presents them as independent, the
claim is overstated and must be narrowed.

### N3 — Hidden-wall scan

Re-read your own proof. Search for these phrases and any close variants:

- "we assume";
- "by construction";
- "as is standard";
- "the framework provides";
- "bridge context";
- "background";
- "naturally";
- "obviously";
- "standard QFT";
- "registered" / "canonical".

For each hit, classify:

- cited retained authority (with link) — keep as-is;
- hidden condition — **promote to explicit wall** and re-run N2;
- genuine non-load-bearing context — annotate that it is non-load-bearing.

**Failure condition:** any hidden condition promoted to a wall means the
wall count was wrong; revise the claim.

### N4 — Residual matching

For every prior no-go / wall / campaign cited as a witness against the
current claim, verify the **residual matches exactly**. Build a per-citation
table:

- cited witness (file path, line);
- residual the witness attacks (named explicitly);
- residual you are claiming closed (named explicitly);
- match? (yes / no).

Drop every citation where the residuals differ. Recount your witness
support after dropping non-matches.

**Failure condition:** if dropping non-matching citations reduces the witness
count below what the claim needs, the claim is unsupported.

### N5 — Rhetoric audit

Any phrase of the form "X is not a Y-fact" must be checked at multiple
resolutions. Specifically, for each such phrase, list:

- per-element / per-site / per-mode / per-block / lattice-wide versions;
- which resolutions you actually tested;
- whether the negative result holds at the resolutions you did NOT test.

If "X is not a per-element Y-fact" was proven but "X is not a per-mode
Y-fact" was not tested, the broader phrase is over-broad and must be narrowed.

**Failure condition:** any over-broad phrase that has not been verified at
every named resolution must be replaced with the narrowest accurate phrase.

### N6 — Partial-closure path scan

Per `feedback_no_new_axioms.md`, the legitimate import-bearing shape is
(1) take an explicit import; (2) bound-theorem; (3) retire-import audit. A
labeling convention, meta-ratification, or definition refactor that closes
the wall WITHOUT new physics is NOT a new axiom — it is the import-retirement
path.

Also separate approved framework primitives from walls. A primitive already
registered in `docs/audit/data/axiom_premise_nodes.json`, such as the
scale-reference or kinetic-isotropy primitive, chain-satisfies dependencies
without making the claim bounded. The kinetic-isotropy primitive supplies only
structural OS0 kinetic-form isotropy `c_t = c_s`, not dynamics or a
Lorentz-closure theorem. A proposed but unapproved primitive has zero premise
weight until explicit approval; it is not an automatic no-go wall.
Run `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` before writing
"no retained primitive supplies this" or any equivalent wall language.

Before declaring "this requires a new axiom," scan for:

- existing reframings that move the wall from "physics" to "convention";
- existing meta-notes / interpretation-stance notes;
- existing controlled-vocabulary entries that name the residual as
  labeling-only;
- existing PRs in flight that propose convention ratification.

For each candidate path found, report: file path, status, what it would close.

**Failure condition:** if you found a partial-closure path that closes the
wall via convention/reframe (not new physics) but the no-go still calls
this "new axiom required," the no-go is misclassified.

### N7 — Steelman

Write the **strongest possible one-paragraph argument AGAINST your own
no-go.** Use a hostile reviewer voice. Name the specific route or framing
that might break the claim. Cite the strongest authority that supports the
counter-argument.

The steelman must identify a concrete unclosed mechanism and terminal
obligation. Persuasive rhetoric without a mathematically actionable route is
not by itself evidence that the no-go is premature.

If you can write a convincing steelman, the no-go is premature: there is
at least one route you have not closed. Demote to partial-attempt and ship
the steelman as the next cycle's target.

Failure to find a counterargument supplies no evidence of impossibility.
The scoped negative theorem still requires a valid proof or a certificate
that exhausts its stated domain. Report an unresolved search as unresolved.

**Failure condition:** an admissible counter-route inside the claimed domain
remains unclosed, or the negative conclusion rests on inability to think of
an alternative. An out-of-domain escape narrows the conclusion; it does not
refute an otherwise proved theorem inside its stated domain.

### N8 — Cross-cycle echo

Search the repo for prior cycles, notes, or campaigns that named **similar**
walls (not necessarily identical — similar shape).

- `grep -rln "structurally undecidable\|no retained primitive\|requires new axiom\|cannot be derived from A_min" docs/`;
- walks of `NO_GO_LEDGER.md` files under `.claude/science/physics-loops/`.

For each prior wall:

- has it since been retired? (via reframe / ratification / convention /
  new authority);
- if yes: by what mechanism? Could the same mechanism apply to YOUR wall?

**Failure condition:** if a structurally similar prior wall was retired
by a mechanism that you have not considered applying to your current wall,
the no-go is premature.

## Output

A `## No-Go Discipline Gate` section in the source note itself, or a committed
`NO_GO_DISCIPLINE_CHECKLIST.md` that the note links, recording the answers to
N1-N8 verbatim. Not the branch-local `CLAIM_STATUS_CERTIFICATE.md`, and not
the PR body or the review verdict.

**The packet must LAND with the PR — a PR body is not a landing surface.**
The single largest audit-invalidation class in this repo's history is the
no-go-discipline packet family (1,560 voided verdicts, 799 of them in one
day for `no_go_discipline_packet_missing`): packets that existed at review
time but did not land as evidence the audit could bind. Two artifacts are
therefore required to land IN the PR, not merely appear in its body:

1. **The N1-N8 checklist as a committed artifact** — a `## No-Go Discipline
   Gate` section in the source note itself, or a committed sidecar
   `NO_GO_DISCIPLINE_CHECKLIST.md` the note links. Copying it into the PR
   body as well is fine, but the PR body copy is a courtesy, not the record.
2. **The N5 execution certificate in the primary runner's cached stdout** —
   one line per resolution class (`per_element:`, `per_site:`, `per_mode:`,
   `per_block:`, `lattice_wide:`), each an honest, substantive (>= 40 char)
   statement of what the runner actually resolves at that granularity,
   using the form "checked and not executed — <reason>" where a class is
   genuinely not exercised. `docs/audit/scripts/forensic_evidence_readiness.py`
   is the validator; `docs/audit/scripts/check_changed_audit_evidence.py`
   checks it at review time against the staged changes.

A negative-claim PR whose packet artifacts are not landing with it fails
this gate even when the checklist is complete and correct.

Status: `PASS` if all 8 checks have answers and no failure conditions are
hit. `FAIL` if any failure condition is hit.

## Stop conditions

If the gate produces `FAIL`:

1. Do not ship the negative claim as currently framed.
2. Demote to one of: `partial-attempt-with-named-untested-routes`,
   `partial-narrowing`, `bounded-with-corrected-wall-count`, or
   `stretch-attempt-with-honest-residual`.
3. Record the failing checklist items in `NO_GO_LEDGER.md`.
4. Either (a) attempt the missed routes in the same cycle if budget allows,
   or (b) ship the narrowed claim and queue the missed routes for the next
   cycle.

If the gate produces `PASS`:

- ship the negative claim with both Output artifacts LANDING in the same PR:
  the N1-N8 checklist as a committed artifact, and the N5 execution
  certificate in the primary runner's cached stdout. A PR-body-only copy
  does not satisfy this;
- the independent audit lane and other reviewers can then see exactly what
  was tested and what alternative routes were closed.

## Case studies

Three archetypal failure modes drawn from the 2026-05-10 v-scale-planck-convention
campaign are recorded in
[`references/case-studies.md`](references/case-studies.md). Each is a real
example of a negative claim that shipped without this discipline and was
later caught by a stress-test review.

The cases illustrate:

- **F1 — Untested alternative route** (cycle 4 / G4 γ-norm overclaim):
  per-element identity tested, per-mode route via Matsubara product
  structure not tested, but the conclusion was phrased as universal.
- **F2 — Independent walls that are not independent, plus hidden walls**
  (cycle 3 / T1 three-wall decomposition): one wall was downstream of
  another; a fourth wall was buried as "bridge context."
- **F3 — Conflated residuals plus dismissed partial-closure path**
  (cycle 1 / substep-4 ratchet): BAE 30-probe synthesis cited as witness
  against species-identification AC_φλ when the residuals differ;
  existing meta-conventions ratification path dismissed as "new axiom."

## Relationship to other skills

- `physics-loop` V1-V5 Promotion Value Gate prevents overclaiming POSITIVE
  results. N1-N8 prevents overclaiming NEGATIVE results. They are
  symmetric and independently mandatory.
- `physics-loop` `NO_GO_LEDGER.md` is where failed routes are recorded for
  future campaigns. N1-N8 output gets appended there when a cycle ships a
  negative claim.
- `physics-loop` Deep Work Rules' stretch-attempt valid-output language
  ("a valid output may be partial structure, a sharper obstruction, a
  falsified premise, or a worked failed derivation with the exact
  load-bearing wall named") aligns with the demotion options here.
- `review-loop` adds a `NoGoDisciplineReviewer` that invokes N1-N8 when
  reviewing changes that ship negative claims.
- `audit-loop` should invoke N1-N8 before issuing `audited_conditional`
  verdicts that name walls.

## Non-Negotiables

- N1 requires 5 normalized approach families, not 5 phrasings, agents, or
  artifact types for the same mathematical route.
- N7 steelman must be the strongest counter-argument, not a token paragraph.
- N6 "convention reframe vs new axiom" distinction must respect
  `feedback_no_new_axioms.md` — bounded condition with named import-retirement
  audit is the legitimate path, approved primitives are not bounded walls, and
  proposed new primitives require explicit approval rather than
  silent use or automatic foreclosure.
- Do not weaken the gate by lowering the failure thresholds. If a cycle
  cannot pass N1-N8, the negative claim is not yet ready to ship; that is
  the gate working correctly.
- This gate checks scope and packet completeness. Narrowing an overclaim may
  repair its science, but does not automatically satisfy the five-route schema.
  Report any remaining packet limitation separately and do not claim PASS.
- This gate is also not a substitute for honest physics work. Passing N1-N8
  on a real no-go just records the discipline; the no-go itself stands or
  falls on its science content.
