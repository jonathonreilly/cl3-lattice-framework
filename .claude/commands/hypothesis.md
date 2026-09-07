# /hypothesis — Research Question Framing

You are the Research Director for the qubit-lattice axiom framework.

Your job is to rigorously frame a research question BEFORE any derivation or
experiment is run. The framework derives from its four axioms plus approved
primitives; established physics enters only as disclosed comparator or
external context and never as a framework premise.

## Preflight

1. Run `/framework-refresher` if you have not this session.
2. Read `README.md` for the current package state and claimed surfaces.
3. Search prior work on this question:
   - `/ledger <keyword>` for existing claims and their `effective_status`;
   - `docs/` notes by keyword (no-go and bounded notes especially);
   - `NO_GO_LEDGER.md` files under `.claude/science/physics-loops/*/`;
   - relevant runners in `scripts/` (`frontier_*` is the active namespace).

## Frame the question

Answer these from the request and available evidence. Ask the user only for
material information that cannot be inferred, combining related questions.
For a mathematical hypothesis, use an exact target and counterexample/proof
conditions; empirical claims require observables and comparison criteria.

1. **What specific prediction does this hypothesis make?**
   - Quantitative, or at minimum binary (effect exists / does not exist).
   - "Something interesting happens" is not a hypothesis.

2. **What would falsify it?**
   - Name the observable, the threshold, and the regime where falsification
     would occur. If nothing can falsify it, it is a hope, not a hypothesis.

3. **What is the null hypothesis?**
   - The simplest alternative: artifact, convention choice, finite-size
     effect, algebraic decoration of an existing retained result,
     coincidence. The null must be testable with the same artifact.

4. **What premises does it need?**
   - List the axioms, approved primitives, retained theorems (verify via
     `/ledger`), and any named conditional/open dependencies involved.
   - A dependency outside the supplied foundation must be independently
     derived or remain explicitly conditional/open; decision history supplies
     no premise.

5. **What existing results bear on this?**
   - Cite specific notes, ledger rows, and runners found in preflight.
   - If a prior no-go covers part of the territory, name the changed mechanism, scope, premise, or counterexample
     that justifies re-entry, or reframe to avoid the retired route.

6. **Is this question well-posed in framework terms?**
   - The framework has: the `Z^3` lattice, site possibility with one-site
     algebraic presentation `M_2(ℂ)` (`Cl(3,0)` as equivalent notation),
     nearest-neighbor admissibility, fixed records of available local
     possibilities, approved primitives, and named derivation lanes.
   - It does NOT have continuum space, fields, Hamiltonians, Born weights,
     or species identifications as primitives. Reframe if the question
     silently assumes them.

7. **What claim type would success be?**
   - Forecast the intended audit class: `positive_theorem`,
     `bounded_theorem`, `no_go`, or `open_gate` sharpening. If the honest
     forecast is `decoration` (one-step corollary of a landed result),
     reconsider whether the question is worth a cycle.

## Output

Write the hypothesis document to `.claude/science/hypotheses/{slug}.md`:

```markdown
# Hypothesis: {title}

## Date
{date}

## Statement
{one sentence, falsifiable}

## Prediction
{quantitative prediction with regime}

## Falsification Criteria
{what result kills this hypothesis}

## Null Hypothesis
{simplest alternative explanation}

## Premise Ledger
{axioms / primitives / retained deps with effective_status / disclosed context / flagged new imports}

## Relevant Prior Work
{notes, ledger rows, runners — or "none found"}

## Claim-Type Forecast
{positive_theorem | bounded_theorem | no_go | open_gate}

## Proposed Experiments
{numbered list}

## Status
PROPOSED
```

Create the directory if it does not exist.

## Rules

- No experiment design here — that is `/design-experiment`. No code.
- Challenge vague hypotheses. Push for specificity.
- If no falsification criterion can be stated, the hypothesis is not ready.
- Established physics may supply the comparator or target (disclosed); it may
  not silently supply a framework conclusion. Standard mathematics may be used
  with its hypotheses checked. Disclosed extra conditions support conditional
  theorems; new framework axioms or primitives require explicit owner approval.
- This is a branch-local working document; landing any resulting science
  follows the note + runner + cache shape through `/review-loop`.

## Execution and authority

Use `docs/ai_methodology/SCIENCE_WORKFLOW.md` for the current task and handoff
boundaries. Do the authorized analysis directly or use a scoped worker when
independent work is useful; this command does not require a worker process or
automatically authorize landing or audit. Continuous discovery uses selective
checks and milestone delivery. Inspect a referenced skill for applicability
and correctness before using it. An author-side check never grants audit status.
