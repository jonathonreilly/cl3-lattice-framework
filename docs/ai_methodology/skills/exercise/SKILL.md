---
name: exercise
description: "Use when an LLM agent hits a hard wall in repo physics work and needs a structured first-principles exercise to open new attack vectors: assumption table from axioms upward, Elon-style simplification/reduction, literature proof search, broad mathematics sector search, and reframing synthesis. Trigger on requests for 'exercise', 'assumptions exercise', 'Elon exercise', 'math sector search', 'reframing exercise', or help getting unstuck on a physics blocker without immediately adding new theory."
---

# Exercise

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Run this skill when a physics lane is stuck and the goal is to discover new
routes, not to defend the current framework story. This is a thought-heavy
wall-breaking protocol. It may produce candidate routes, proof plans, runner
ideas, or literature bridges, but it must not apply audit verdicts, promote
claims, add axioms/primitives, or treat existing repo content as unquestionable.

## Model And Tool Boundary

Use the strongest available reasoning model/profile. If subagents are used for
any exercise, each subagent must be a maximum-reasoning physics reviewer class
agent, not a lightweight summarizer. Every main agent and subagent must perform
the Framework Refresher Read below before starting its assigned exercise slice.
Do not use image-generation or visual artifact tools for this skill.

For theorem, proof, or multi-step bridge exercises, read
[`../physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md)
before fan-out. Give early agents neutral route-local briefs without the
favored approach or other agents' conclusions, require concrete mathematical
returns, and delay cross-pollination until independent passes expose their
actual gaps.

For literature search, browse current scholarly sources when network access is
available. Cite papers or source pages precisely. Literature can suggest proof
templates, but it is never imported as authority: any external proof must be
translated into the repo's framework, implemented as a runner or proof artifact
when appropriate, then reviewed and audited like native theory.

## Framework Refresher Read

Before Exercise Zero, perform a short framework refresher read. If a current
repo-native `framework-refresher` skill or command exists, read/use that first;
otherwise read the surfaces below directly. When using subagents, include this
requirement in each subagent prompt and require each subagent to state the
refresher surfaces it read before giving conclusions.

Minimum refresher surfaces:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` for the current Lattice, Qubit,
  Admissibility, and Record baseline;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` for how approved
  primitives enter assumption, import, wall, and bounded-status judgments;
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` for the approved scale-reference
  primitive boundary;
- `docs/audit/data/axiom_premise_nodes.json` for the complete supplied
  foundation, and `docs/audit/data/premise_decision_history.json` only when
  historical provenance is relevant;
- `docs/ai_methodology/skills/review-loop/SKILL.md` for current review/audit
  boundaries, especially the axiom/approved-primitive distinction and Record
  guardrails;
- `docs/repo/CONTROLLED_VOCABULARY.md` when proposing names, statuses, or new
  surfaces.

Use the refresher to avoid stale framework language. Do not use it to
short-circuit the exercise: the assumptions table must still mark framework
premises as assumptions for purposes of the wall-breaking exercise, and it may
still identify overbroad, hidden, or misframed uses of existing repo content.

## Arguments

Parse:

- problem/wall text: required unless resuming a named exercise packet;
- `--artifact`: write a durable packet under `.claude/science/exercises/<slug>/`;
- `--slug SLUG`: optional packet slug;
- `--literature`: force literature search even if the user asks only for the
  first-principles parts;
- `--subagents N`: optional independent exercise fan-out, normally `4` or `5`;
- `--no-web`: skip live literature search and mark that limitation explicitly.

If no durable artifact is requested, return the structured exercise in the
conversation. If `--artifact` is requested, write:

```text
.claude/science/exercises/<slug>/
  EXERCISE.md
  ASSUMPTIONS_TABLE.md
  ATTACK_VECTORS.md
  APPROACH_REGISTRY.md
  LITERATURE_SEARCH.md
  MATH_SECTOR_SEARCH.md
  REFRAMING.md
  SUMMARY.md
```

## Exercise Zero: State The Wall

Begin by making the blocker precise:

- the target claim, theorem, import, selector, no-go, or bridge;
- its quantifiers/domain, allowed premises, and forbidden weakenings;
- required boundary or degenerate cases and outcomes that do not count as
  closure;
- what currently fails;
- what would count as progress;
- what would count as a decisive closure, demotion, or no-go;
- which observations, fitted values, conventions, imported theorems, and
  repo-retained surfaces are currently being leaned on.

Keep this statement neutral. Do not smuggle the desired answer into the wall
statement.

## Exercise One: Assumptions From Axioms Up

Build a complete assumption ledger from first principles to the local blocker.
Start with only approved repo axioms and approved primitives when the task is
repo-native, but mark even those as assumptions for purposes of the exercise.
Enumerate approved primitives from `docs/audit/data/axiom_premise_nodes.json`
and read their source notes. The scale-reference primitive, including the
Planck scale reference, is already granted as units conversion only; do not
treat it as a bounded wall, and do not grant it dimensionless content. The
kinetic-isotropy primitive grants only structural OS0 kinetic-form isotropy
`c_t = c_s`; do not let it supply dynamics, a Lorentz-closure theorem, an
absolute scale, a spacing-ratio theorem, a selector, or empirical content.
Then climb layer by layer:

1. axioms and primitives;
2. definitions and equivalence choices;
3. representation, algebra, topology, finiteness, smoothness, symmetry, and
   regularity assumptions;
4. readout, record, probability, measure, normalization, scale, time, dynamics,
   and selector assumptions;
5. retained or bounded repo surfaces being reused;
6. runner/model assumptions, numerical choices, and boundary conditions;
7. problem-local hypotheses and implicit "obvious" steps.

Create a table with at least these columns:

```text
ID | Layer | Assumption | Explicit/Implicit | Current source/evidence |
Why it is needed | What if wrong? | Failure mode opened |
New attack vector | Test/artifact to check | Confidence
```

Rules:

- Include implicit assumptions even when they feel embarrassing or basic.
- Treat existing framework content as useful evidence, not as immune from
  challenge. A retained row can still reveal a hidden premise or a route that
  should be attacked differently.
- Separate axioms/primitives, open obligations, bounded dependencies, empirical
  comparators, conventions, and mere prose habits.
- For each assumption, write a real "what if wrong?" entry. If no consequence is
  visible, say what would have to be inspected to know.

After the table, cluster the "what if wrong?" entries into possible routes:

```text
Route | Assumptions challenged | Why this might open the wall |
Expected artifact | Risk | First test
```

## Exercise Two: Elon-Style First-Principles Reduction

Use this as an engineering-reduction exercise, not as an appeal to a person.
Reason upward from the minimum physical and mathematical requirements.

Ask:

- What is the exact requirement? Is it stated too strongly?
- Which requirement is inherited, conventional, or optimized for a stale route?
- What can be deleted without losing the target?
- What is the smallest object, carrier, algebra, graph, sector, or toy model
  where the issue still exists?
- Can the problem be decomposed into two independent bits or dials?
- Are we solving a selector problem, a readout problem, a dynamics problem, a
  normalization problem, or a representation problem?
- What is the fastest falsifying test or smallest runner?
- If the target cannot be derived, can we prove the exact missing input instead
  of writing more prose around it?

Use the reduction order:

1. make requirements less wrong;
2. delete unnecessary parts or premises;
3. simplify the remaining mechanism;
4. accelerate the feedback loop with a small runner or finite example;
5. automate only after the route is conceptually clean.

## Exercise Three: Literature Proof Search

Search the relevant physics and mathematics literature for proof patterns,
obstructions, dual formulations, canonical examples, and known no-go results.
Prefer primary sources: arXiv, journal papers, books/lecture notes by domain
experts, and official bibliographic pages.

For each useful source, record:

```text
Source | Problem it solves | Premises | Proof skeleton |
What maps to the repo | What does not map | Runner/proof translation |
Import risk | Citation to preserve
```

Do not import a literature theorem as a repo result. The acceptable pattern is:

1. extract the proof skeleton;
2. rewrite it in repo-native objects and assumptions;
3. implement the finite or symbolic check when possible;
4. prepare the resulting evidence for independent review at the requested
   milestone; this exercise does not automatically invoke review or landing;
5. cite the external paper as inspiration or precedent, not as the proof
   authority unless the row is explicitly an imported bounded theorem.

## Exercise Four: Mathematics Sector Search

Run a broad math search as if a single reviewer were fluent across many fields.
The goal is to find an unexpected formal lens, not to name-drop fields.

At minimum scan:

- finite group and representation theory;
- operator algebras, C*-algebras, and noncommutative geometry;
- category theory, adjunctions, and universal properties;
- algebraic topology, cohomology, K-theory, and index theory;
- spectral graph theory and combinatorics;
- convexity, optimization, semidefinite programming, and variational methods;
- probability, information theory, entropy, and large deviations;
- dynamical systems, ergodic theory, and stability theory;
- PDE, functional analysis, and distribution theory when continuum limits are
  relevant;
- number theory, modular forms, lattices, and arithmetic constraints when
  discrete spectra or exact constants appear;
- logic/model theory/proof theory when independence or hidden axioms are
  suspected.

For each sector, write:

```text
Sector | Reframe | Candidate theorem/tool | Minimal toy example |
How it could attack the wall | What would falsify it | First artifact
```

Reject vague "maybe use topology" entries. A sector entry must name the object
that changes, the invariant or theorem type that might bite, and the first
concrete artifact to try.

## Exercise Five: Reframing

Use the previous four exercises to generate alternate frames. Good reframes
often move one of these boundaries:

- pre-record vs recorded;
- object vs readout;
- selector vs admissible dial;
- dynamics vs kinematics;
- finite carrier vs limiting family;
- exact theorem vs bounded theorem vs no-go;
- value derivation vs value availability;
- central sector vs within-sector data;
- representation choice vs physical observable;
- obstruction vs missing input.

For each reframe, state:

```text
Reframe | What moves | What becomes simpler | What becomes harder |
New route opened | First decisive test
```

## Synthesis

End with a compact route portfolio:

```text
Rank | Approach family | Route | Source exercise(s) | Premise challenged |
Terminal obligation | Strength vs target | Expected status if successful |
First concrete artifact | Stop/reopen condition
```

For theorem-heavy exercises, normalize families and strength relations using
the proof-search governance reference. A route ending at a target-equivalent or
stronger missing lemma is `blocked-equivalent`, not near closure. Reopen it only
after naming a materially new mechanism.

Also include:

- assumptions most likely to be wrong;
- assumptions most expensive to be wrong;
- routes worth a physics-loop PR;
- routes that should be added to a no-go or opportunity ledger;
- literature proofs worth translating;
- math-sector tools worth trying;
- what not to do next.

Do not claim the wall is solved unless the exercise produced an actual proof,
runner, or decisive no-go artifact. The normal output is a better attack map.
