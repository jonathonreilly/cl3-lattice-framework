---
claim_id: admissibility_d4_h1_aci_component_summary_terminal_confluence_boundary_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "The exact five-atom OR semilattice passes ACI and joins the translated Block-229 overlap, but the literal coverage-only terminal compiler has 51 reachable states and 19 terminal normals on the four-site center-writer typed Y; this is a finite counterexample to that frozen compiler only, while neighbor readiness, leaf writers, distributed incidence, labelled lift, CP absorption, Record probability, axioms, and TOE closure remain open."
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: admissibility_d4_h1_cleanup_front_coalescence_radius_boundary_bounded_theorem_note_2026-08-28
target_blocker_text: "replace the Block-229 diameter-dependent cleanup join by a finite locally readable schedule-independent component summary and physical Record instrument"
source_of_blocker_text: user_goal
reachability_to_target: exact_frozen_terminal_rule_counterexample_with_local_guard_reopen
artifact_role: theorem
runner: scripts/admissibility_d4_h1_aci_component_summary_terminal_gate_2026_08_28.py
next_trace_action: "preregister the all-neighbor readiness guard on typed Steiner-hull trees, prove arbitrary-tree confluence/contact safety, then attempt the explicit rank-128 labelled isometry and Lindblad absorption"
conditional_surface_status: "ACI algebra and translated overlap positive; frozen E-only terminal compiler negative on one complete finite Y; guarded arbitrary-tree and physical stages open"
hypothetical_axiom_status: none
admitted_observation_status: none
claim_type_reason: "an exhaustive finite counterexample and exact local repair control narrow one preregistered compiler but do not prove a broad no-go"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_commit: c6ab3c9094
preregistration_commit: da9935977d
no_go_discipline_status: pass_exact_finite_claim_fail_broad_no_go
axiom_amendment: none
obligation_retirement: 0
toe_percentage_movement: 0
---

# ACI component summaries pass, but the frozen coverage-only terminal rule is nonconfluent

Type: bounded_theorem

Primary runner: `scripts/admissibility_d4_h1_aci_component_summary_terminal_gate_2026_08_28.py`

## Claim status

**Decision:** `scoped-summary-rank-or-confluence-failure` for the literal
Block-230 compiler, demoted to
`partial-attempt-with-named-untested-routes` against any broader claim.

This note proves one finite statement.  On an allowed four-site typed Y with
the seam/writer at the degree-three center, the frozen Boolean-union merge rule
and coverage-only terminal rule have 19 distinct reachable terminal normal
forms.  It does **not** rule out ACI gossip, finite summary compilers, a stronger
local terminal guard, a leaf writer, distributed incidence, coherent
arbitration, or the associative Haar route.

The committed [Block-230 preregistration](../.claude/science/physics-loops/aci-confluence-7781-correction-20260909/originals/.claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/PREREGISTRATION.md)
is historical contract context. The current finite theorem uses the explicit
rules below, with coverage treated as the complete enabling condition; a
necessary-only phrase does not specify that rule. Supporting scope discussion
is in the linked
[N1--N8 sidecar](../.claude/science/physics-loops/aci-confluence-7781-correction-20260909/SUPPORT_NO_GO.md).

## Stage A0 result

The supplied summaries are subsets of five atoms, encoded as bits
`rho=1, alpha=2, lambda=4, chi=8, phi=16`; `Sigma={0,...,31}`.
The product is bitwise union with bottom zero. Set union proves associativity,
commutativity and idempotence directly. An enabled unequal-neighbor merge
replaces both summaries by their union. Terminalization replaces the center
by `CLEAN=64`, after which incident merges are disabled. These finite
mathematical rules supply no physical Record or generator.

The 32-element product has the following exact checks:

- all 1,024 ordered products reproduce
  `5e7bfc1cb5c5d43ec8df382bfe491c4e12ce7cb1e6d6929d8358148812be5c18`;
- all 32,768 associativity triples, 1,024 commutativity pairs, 32
  idempotence diagonals, and 32 bottom cases pass;
- for every translation `n=10..16`, the Block-229 `CF_A/CF_T` successors
  enter a common six-site quotient diagram; their two reachable sets have
  20 and 87 states and 15 common states, including the all-`alpha|phi`
  normal;
- the old 46-row table has seven source-summary factorization collisions.
  That comparator failure is nonfatal because Block 230 proposed a new
  compiler rather than a relabeling of the old grammar.

For these supplied comparator branches, the ACI multiplication gives the
common six-site quotient diagram for each tested translation. This does not
establish an arbitrary-translation or full old-compiler confluence theorem.  The new failure is later and different: Record terminalization can
destroy the very summary carrier that still has to broadcast the union.

## Exact Stage A1 counterexample

Number the writer/seam center by `0` and its typed root, child-0, and child-1
leaves by `1,2,3`.  The edges and initial summaries are

```text
edges   = {(0,1),(0,2),(0,3)}
initial = (alpha,rho,lambda,chi) = (2,1,4,8)
E       = rho|alpha|lambda|chi   = 15
```

Three legal merges reach

```text
(2,1,4,8)
 -> (3,3,4,8)
 -> (7,3,7,8)
 -> (15,3,7,15).
```

At the last state, terminalization and another incident merge are both
enabled.  Terminalization replaces the writer summary ray and immediately
parks at

```text
(CLEAN,3,7,15).
```

The other order can reach

```text
(15,3,7,15)
 -> (15,15,7,15)
 -> (15,15,15,15)
 -> (CLEAN,15,15,15).
```

The first state is already normal because every remaining gossip edge was
incident to the replaced center ray.  The two branches have no common
descendant.  Both finite histories are fair: after the first terminal jump no
transition remains enabled.

Full exhaustive reachability gives

```text
reachable states        51
directed transitions    70
terminal normal forms   19
correct normal forms     1
rank non-decreases       0
```

The rank is `sum_(live summary sites)(5-popcount(s)) + live_writer`.
Each unequal merge strictly increases at least one summary without decreasing
any other; terminalization removes the writer term and its nonnegative
missing-bit term. The rank therefore strictly decreases and proves termination
for this finite graph, but does not prove unique termination.  A
positive Lindblad rate cannot repair a dark normal state for which the frozen
compiler supplies no enabled jump.

## Strongest immediate repair

The locally readable repair is to require, at the unique writer `w`,

```text
E subset summary(w)
and summary(v) = summary(w) for every v adjacent to w.
```

This has support at most four because the tree degree is at most three.  The
same Y then has 33 states, 52 transitions, and the unique normal
`(CLEAN,15,15,15)`.  More generally, if the writer holds the global union
`U`, every component of the tree after removing the writer begins with its
boundary neighbor already holding `U`; ordinary OR gossip can therefore
finish independently in every component.  Incident writer merges are already
identity rows, neighboring merges preserve `U`, and disjoint rows commute.

That is a concrete route, not a completed Block-230 rescue.  The preregistration
called the terminal guard frozen, so the neighbor-ready rule must be tested in
a new preregistered block.  The next block must also say explicitly that the
tree is the Steiner hull of its typed endpoints (equivalently, every graph
leaf is typed); otherwise an untyped pendant can retain an unseen live contact
and produce a false clean.

## Physical scope

The supplied dimension count fits 64 parity-summary rays,
four terminal rays, and a rank-60 complement in rank 128.  That is only a
dimension/character count, not an explicit physical representation.  Proper
cubic isometries, dart transport, complement exchange, QND Record-code
orthogonality, exact participant cylinders, and the Lindblad/absorption proof
remain downstream.

No axiom or retained obligation moves.  No edit to the minimal axioms is
justified: this is an exact compiler-rule defect with an explicit local repair.
No TOE-completion or independent retention result is claimed.

## Current packaging and historical evidence

The comparator now uses a supplied explicit 46-row table and only the original
word-transition functions needed for the translated witness. Its rows and all
seven used source/two-branch configurations were checked against the exact
historical runtime modules. Their complete bodies are archived; their larger
campaigns, absent note inputs and physical conclusions are not imported.
The independent checker remains separately implemented and imports neither
the primary nor the comparator. The primary uses its independent Y graph,
so both real helper-discovery APIs include it through an actual static import.

The old twelve-behavioral-mutation claim is corrected to **nine behavioral
variants (six algebra, three graph) plus three bookkeeping comparisons**.
The remaining forty originally listed downstream cases were not executed.
No new scientific credit is assigned to list-length, digest-only or
`len(range(64))` checks. The optional self-test reports this split explicitly;
the original plan and original caches are preserved unchanged.

The [recovery history](../.claude/science/physics-loops/aci-confluence-7781-correction-20260909/HISTORY.md) maps all fifteen original
endpoints, including the historical generated manifest, and four earlier
bodies. Current main's generated manifest remains authoritative and unchanged.
Current inputs bind this note, the supporting sidecar and the actual loaded
helper union. Dated planning claims are historical custody. Formal audit is
deferred; this author revision awaits the original reviewer's confirmation.

## Reproduction

Run:

```bash
python3 -B scripts/admissibility_d4_h1_aci_component_summary_terminal_gate_2026_08_28.py
python3 -B scripts/admissibility_d4_h1_aci_component_summary_terminal_gate_2026_08_28.py --self-test
python3 -B scripts/independent_admissibility_d4_h1_aci_component_summary_terminal_gate_2026_08_28.py
```
