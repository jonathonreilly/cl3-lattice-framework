---
claim_id: admissibility_d4_record_ready_set_successor_state_typing_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "For a simple graph with occupied set O and all-neighbor readiness F(O)={x outside O:N(x) subset O}, ready vertices are pairwise nonadjacent and appending any x in F(O) gives F(O union {x})=F(O) minus {x}. On the cubic six-neighbor event surface, every nominal adjacent successor target is already occupied; the old eta, outcome and direction fix only one bit of a successor mask and leave five outer-shell bits, hence 32 compatible masks rather than a reachable successor event. This is a state-typing theorem, not a formation law or dynamics no-go."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py
independent_checker: scripts/independent_admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py
status: proposed_retained
actual_current_surface_status: bounded-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Ready-set deletion and successor-state typing

**Date:** 2026-08-29
**Corrected:** 2026-09-09
**Type:** `bounded_theorem`
**Standing:** author-side `proposed_retained`; no formal audit has run.

Primary runner:
[`admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py`](../scripts/admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py).
Independent checker:
[`independent_admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py`](../scripts/independent_admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py).

## General finite-graph lemma

Let `G=(V,E)` be a simple graph, `O subset V` its occupied vertices, and

```text
F(O)={x in V\O : N(x) subset O}.                      (1)
```

If distinct `x,y` were both ready and adjacent, readiness of `x` would put
`y` in `O`, contradicting `y in F(O)`. Thus `F(O)` is independent. If
`x in F(O)`, all neighbors of `x` already lie in `O`. Appending `x` cannot
complete the neighborhood of another unoccupied vertex: any such new vertex
would neighbor `x`, but every neighbor of ready `x` was already occupied.
Previously ready vertices other than `x` remain ready because none neighbors
`x`. Hence

```text
F(O union {x}) = F(O) \ {x}.                          (2)
```

The runners exhaust finite graphs as a control; (2) itself is the displayed
cardinality-independent proof.
Its physical terminology is limited to the conditional content/Record typing
in the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).

## Cubic successor boundary

At a cubic event `x`, all six sites `x+d` are occupied by the premise of
all-neighbor readiness. After a Record is appended at `x`, none of those six
sites can be the next fresh target. For a nominal target `x+d`, the new
Record at `x` fixes the `-d` bit of its six-bit neighborhood. The other five
outer-shell bits are not specified by `(eta_x,b,d)`, leaving `2^5=32`
compatible successor masks.

Across all 64 starting masks, two outcomes, and six directions there are 768
such occupied-target rows. Restricting to the supplied 24-mask active set
gives `24*2*6*32=9216` compatible completions. These are compatibility rows;
they are not reachable events at the already occupied target.

The conclusion is narrow. A front with live non-Record conditions, a target
outside the old shell, hidden state, or a separately supplied formation rule
can evade this boundary. The theorem neither builds nor excludes such a
process. It supplies no site selector, rate, clock, unbounded history, axiom
change, or TOE conclusion.

## Reproduction

```bash
python3 scripts/cached_runner_output.py --refresh scripts/admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py
python3 scripts/cached_runner_output.py --refresh scripts/independent_admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py
```
