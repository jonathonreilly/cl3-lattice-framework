# /pstack — Physics Science Stack Index

You are running PStack — the physics science stack for the qubit-lattice
axiom framework (four axioms: Lattice, Qubit, Admissibility, Record; see
`/framework-refresher`).

## Available Skills

### Orientation
| Skill | Role | What It Does |
|-------|------|-------------|
| `/framework-refresher` | Orientation | Load the current axioms, approved primitives, open obligations, vocabulary, and standing discipline before any physics work |
| `/ledger` | Status Lookup | Verify a claim's audit-ratified `effective_status` on `origin/main` before citing or building on it |

### Research Direction
| Skill | Role | What It Does |
|-------|------|-------------|
| `/hypothesis` | Research Director | Frame a falsifiable research question with a premise ledger and claim-type forecast |
| `/theory-review` | Theoretical Physicist | Check a hypothesis for axiom compliance, consistency, falsifiability, minimality, and claim-type fit |

### Experiment Design
| Skill | Role | What It Does |
|-------|------|-------------|
| `/design-experiment` | Experimental Physicist | Plan a runner around its decisive check, controls, and falsification observable |
| `/sweep` | Computational Physicist | Generate reproducible parameter sweep + collector scripts |

### Analysis & Validation
| Skill | Role | What It Does |
|-------|------|-------------|
| `/analyze` | Data Analyst | Analyze runner/sweep output against the hypothesis prediction |
| `/validate` | Reproducibility Officer | Robustness battery — independent-route math checks for exact runners; seeds/sensitivity/finite-size/cherry-pick for stochastic ones |
| `/sanity` | Senior Skeptic | Adversarial review: model consistency, scale, symmetry, limits, artifacts, bugs, hostile-reviewer semantic-bridge test |
| `/investigate-physics` | Detective Physicist | 4-phase anomaly investigation: characterize, hypothesize (bug/artifact/genuine), discriminate, resolve |

### Derivation & Negative Claims
| Skill | Role | What It Does |
|-------|------|-------------|
| `/first-principles` | First-Principles Theorist | Derive a target from axioms + approved primitives + retained theorems only |
| `/exercise` | Wall Breaker | Structured exercise suite against a stuck wall/blocker (repo-native skill) |
| `/no-go-gate` | Negative-Claim Gate | N1–N8 discipline before any no-go / walls-naming claim ships |

### Documentation & Strategy
| Skill | Role | What It Does |
|-------|------|-------------|
| `/write-up` | Scientific Writer | Archival summary of a completed investigation, in the repo voice |
| `/progress` | Research Manager | Periodic retrospective: claim-state movement, dead ends, pipeline health |
| `/frontier` | Research Strategist | Frontier map: lane census, blocker fanout, ranked highest-value gaps |
| `/autopilot` | Lab Operations | Status dashboard: locks, active loops, open PRs, audit backlog |

### Loops & Gates (repo-native skills)
| Skill | Role | What It Does |
|-------|------|-------------|
| `/physics-loop` | Physics Loop Lead | Continuous discovery with explicit provisional dependencies, selective critical checks, and milestone PRs; optional per-block delivery |
| `/review-loop` | Review Board | Pre-landing gate: parallel physics reviewers, narrow honest fixes, audit-system compatibility without applying verdicts |

## Science Pipeline

```
/framework-refresher
        |
/hypothesis --> /theory-review --> /design-experiment --> [build runner] --> [run]
                                          |
                                       /sweep (if parameter scan)
                                          v
                               /analyze --> /validate --> /sanity
                                          |
                       /first-principles (derive)   /investigate-physics (anomalies)
                       /no-go-gate (negative claims)
                                          v
                                      /write-up
                                          v
                    assemble a coherent milestone with source notes
                    and applicable proof/runner/cache evidence
                                          v
              science branch off origin/main --> PR --> /review-loop (gate)
                                          v
                 independent audit lane ratifies on main (not run from here)
```

Side channels (run anytime): `/frontier`, `/progress`, `/ledger`,
`/autopilot`, `/exercise`, `/physics-loop` for campaigns.

## Core Principles

1. **Design Discriminating Computation** — Choose the smallest scan that can
   answer the question within the resource budget. Record coverage, uncertainty,
   controls, and untested regions; use an exhaustive scan when the claim needs it.
2. **Import Discipline** — Derive from approved axioms and approved primitive
   registry entries when making framework claims; use known physics and
   literature only as disclosed comparators, targets, or external context that
   does not satisfy a framework dependency.
   Registered primitives, including the scale-reference and kinetic-isotropy
   primitives, are not bounded imports; unregistered primitives are not
   granted. The kinetic-isotropy primitive supplies only structural OS0
   kinetic-form isotropy `c_t = c_s`, not dynamics, Lorentz closure, scale,
   selector, or empirical content.
3. **Evidence Must Be Checked** — A runner is an implementation of a model,
   not ground truth about nature. Investigate discrepancies against the source
   mathematics, independent calculations, and relevant empirical comparisons;
   neither a passing runner nor prior theory is immune from error.
4. **The Ledger Is Authoritative** — the tracked claim shards under
   `docs/audit/data/ledger/` on `origin/main` are the only source of
   retained-grade status. Note headers, memory, and prose go stale.
5. **Propose, Never Ratify** — Author-side surfaces use `proposed_*` /
   `support` / `bounded` / `open` vocabulary. Audit verdicts come only from
   the independent audit lane; nothing in this stack runs it.
6. **Negative Claims Are Claims** — A no-go rules out its stated conclusion
   under its proved premises and domain. It does not permanently foreclose
   untested families or corrected formulations; apply the scoped `/no-go-gate`
   requirements before shipping.

Continuous discovery may compose provisional lemmas on a coherent campaign
branch with inherited gaps explicit. Independently check critical steps before
extensive reuse. Deliver review-ready milestones through PR and formal audit;
do not require either for each intermediate lemma. `--delivery block` remains
available when requested.

## Lock & Worktree Protocol

Prefer a dedicated git worktree on a science branch off `origin/main` for any
work that mutates files — concurrent sessions race a shared checkout. When
running compute or mutations in a shared checkout, use the cooperative lock:

```bash
python3 scripts/automation_lock.py acquire --owner pstack-{skill} --purpose "{description}" --ttl-hours N
python3 scripts/automation_lock.py release --owner pstack-{skill}
```

Read-and-think skills (hypothesis, theory-review, sanity, first-principles,
write-up, progress, frontier, ledger, pstack) need no lock.

## Output Directory

PStack working documents live in `.claude/science/` (branch-local; the audit
citation graph scans `docs/` only, so working notes here never pollute it):

```
.claude/science/
  hypotheses/        experiments/       analyses/
  validations/       sanity/            investigations/
  derivations/       write-ups/         progress/
  frontier/          theory-reviews/    exercises/
  physics-loops/     research-lanes/
```

Working documents do not land on `main`. Landable science is distilled to
the note + runner + cache shape and goes through a science-branch PR and
`/review-loop`.

Print this index when invoked. Ask the user which skill to run.

## Execution Mechanism

Use the current `docs/ai_methodology/skills/workhorse/SKILL.md` for worker
profiles, task boundaries, neutral checks, and handoff. This index does not
dispatch work or authorize a lane merely by listing it.
