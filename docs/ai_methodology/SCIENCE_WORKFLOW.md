# Science workflow

This is the operating map for research, review, audit, and repair. It supplies
no physics premise and grants no scientific status. The objective is to build
and test a theory of everything; whether a proposed theory succeeds remains
an open scientific question. Optimize for resolved scientific obligations and
discriminating evidence, not favorable verdicts, paper volume, or PR counts.

## Read the task before choosing a procedure

For a process or prompt review, inspect the instructions for correctness before
using them. Do not launch a science campaign, drain PRs, apply audits, or change
premises merely because the request mentions those activities. A skill is a
maintained procedure, not evidence that its own rules are correct or permission
to expand the user's task. Preserve explicit user constraints and existing
authorization; explain actual conflicts instead of inventing an approval gate.

Read the current entry point and only the references needed for the selected
mode. Validate scientific statements against their actual source and tests.
Treat local memory, old commands, and previous model conclusions as retrieval
aids, never as proof. Use the user's configured model and actual available
tools; do not infer current model capabilities from a dated name in a prompt.

## Default research cadence

Owner-selected 2026-09-07: continuous discovery, selective independent checks,
and milestone PRs and audits. Keep a coherent candidate on a dedicated working
branch and checkpoint useful blocks there. Routine landing and full audit are
not prerequisites for the next exploratory step.

Check a provisional result independently before substantial downstream work
depends on it, especially a bridge that fixes an observable, dynamics, symmetry,
normalization, or a widely reused theorem. Keep its unresolved obligations
explicit. Such checks support a research decision; they do not confer formal
retention. A candidate TOE is a connected proposed derivation with named gaps;
completion as an established result still requires the full evidence chain.

Deliver a PR at a coherent scientific milestone or explicit handoff. Group
related lemmas when they form one reviewable argument; avoid indefinitely
growing branches or PRs that exceed reliable review. Audit the milestone and
critical landed dependencies when the campaign needs authoritative reuse, and
perform complete chain verification before claiming the TOE is established.
Explicit review/audit drains remain available; merely doing science does not
launch them. The old per-block delivery mode remains opt-in.

## Responsibilities and handoffs

| Stage | Work product | Completion evidence | Authority boundary |
|---|---|---|---|
| Select | Exact target, current gap, alternative routes, decisive test | Current source and dependency snapshot; novelty search | Planning does not establish a claim |
| Develop | Coherent source note and reproducible evidence on a branch | Proof obligations, honest scope, independent checks of load-bearing calculations | Author proposes; no audit verdict or direct science landing |
| Author check | Corrected packet and reproduction instructions | Applicable mechanical checks actually run; omissions named | Self-check is not independent review |
| Review | Findings and fixes on a frozen source revision | Independent reviewer confirms the final changed content; integration gates pass | Review decides source readiness and lands only within the requested scope |
| Audit | Verdict on the landed, restricted evidence packet | Fresh-context mathematical examination plus authenticated evidence | Only the independent audit application path writes verdicts |
| Repair | Source fix or justified re-audit request | Exact defect addressed; affected row is discoverably requeueable | Repair cannot prewrite the verdict it requests |
| Synthesize | Candidate assembly or account of established results | Candidate: explicit provisional dependency graph and gaps; established result: audited dependency closure | A summary cannot promote its sources |

The mechanical audit pipeline prepares and propagates data. A pipeline PASS,
runner PASS, reviewer PASS, and scientific audit verdict answer different
questions. None substitutes for the others. Audit must be free to disagree
with review; agreement is not its performance target.

Use `skills/physics-loop/SKILL.md` for sustained discovery,
`skills/exercise/SKILL.md` for bounded investigations,
`skills/workhorse/SKILL.md` for a scoped worker handoff,
`skills/review-loop/SKILL.md` for independent source review and authorized
landing, `skills/audit-loop/SKILL.md` for an independent audit operation, and
`skills/science-fix-loop/SKILL.md` for a repair campaign. Negative claims also
use `skills/no-go-discipline/SKILL.md`. The remaining reviewer, lane-building,
backpressure, and methodology-writing skills are supporting operations, not
additional mandatory stages for every change.

## Select work by what it could establish

Record this compact contract in the existing goal/handoff file; do not create
another packet just to repeat it:

```text
Target and quantified domain:
Current main revision and source/claim identifiers:
Accepted premises and separately supplied conditions:
Closest existing result and exact missing obligation:
New construction, proof mechanism, or discriminating test:
Success witness / counterexample / inconclusive outcome:
Downstream question this would resolve, or frontier-discovery value:
Next decision and condition for reopening an exhausted route:
```

Prioritize load-bearing gaps with plausible decisive tests. Keep exploration
of materially different routes available; graph fanout is a prioritization
signal, not a measure of truth or scientific importance. Do not keep generating
small variants because they are easier to package. Conversely, a short proof
using standard mathematics is valuable when it closes an actual missing
obligation. Proof difficulty is not a validity test.

Report progress as concrete changes: a proved lemma, discharged hypothesis,
new falsifier, eliminated counterexample class, validated observable map, or
remaining terminal obligation. Separate proposed progress from audited closure.
Do not give a percentage of TOE completion from counts of notes or retained
rows. A valid conditional theorem proves an implication; it does not establish
that the physical world satisfies its hypotheses.

For empirical claims, distinguish predictions from calibration, fitted inputs,
and post hoc matches. Declare comparison criteria and uncertainty treatment
before inspecting the comparison result when possible; disclose prior exposure
when it is not. For exact mathematical claims, state the domain, quantifiers,
edge cases, and proof or exhaustive certificate. Numerical agreement alone
does not prove a general theorem.

## Negative results and independent checks

A failed search reports what was attempted. An obstruction theorem rules out
an explicitly quantified family by proof. Underdetermination requires witnesses
or a proof under matching premises. These are different conclusions. Neither a
fixed number of failed approaches nor inability to imagine a counterargument
establishes impossibility. Computational resource exhaustion is operational
evidence, not evidence that a physical claim is false.

Use the existing N1-N8 packet contract honestly where required. Its current
five-route minimum is a mechanical submission requirement, not a theorem about
search completeness. Never invent route families to satisfy it; a packet that
cannot meet the schema remains pending, with the actual mathematical result
and the tooling limitation distinguished. Changes to that schema require
coordinated validator, fixture, and auditor-prompt validation.

Independent checking means a different derivation or implementation path for
the load-bearing step. A new agent repeating the same calculation or comparing
two outputs derived from the same expected constant is not independent evidence.
Adversarial checks should challenge premises, domains, normalization, and the
claimed physical identification, not merely the prose. Record uncertainty and
disagreement instead of resolving them by majority rhetoric.

## Where material belongs

- `origin/main`: scientific source, controlled premise registries, audit
  application tooling, and audit-derived status. Verify the relevant current
  source before relying on an old description of a premise.
- `ai/execution`: planning and dispatcher instructions. This orphan branch
  never merges into `main`; its scorecard is an as-of planning aid.
- Science branches: source proposals, evidence, and coherent handoffs. Draft
  PRs remain outside ordinary review/landing unless explicitly in scope.
- `docs/ai_methodology/skills/` and `.claude/commands/`: current procedure
  sources and command adapters. Check freshness of referenced files too.
- `docs/work_history/`, `archive/`, and dated campaign packs: history and
  recovery evidence. Do not update an archived board as the live work queue.

Keep changes reviewable: isolate work, stage intended paths, preserve unpushed
work on failure, and regenerate derived files using their owning tools. Never
restore generated files from moving `origin/main` into a stale branch's index.
Restore only identified generated residue to that branch's own `HEAD`, keeping
reviewed source, control data, and dispatcher sidecars intact.

## Changing this process

Treat editable agent prompts, skill bodies, command adapters, and embedded
worker/auditor prompts as one interface. For each proposed rule change, identify
the actual defect, affected callers, expected decisions, and a realistic
counterexample. Change code and prompt contracts together when behavior is
mechanically enforced. Run applicable tests and independent scenario review;
word matching and a skill-format validator alone do not establish correctness.

Platform-supplied system/developer instructions are outside the repository's
editable prompt surface. Review their behavioral implications and report
conflicts, but do not claim to have rewritten them. Local overrides must remain
within their scope and cannot change platform policy.
