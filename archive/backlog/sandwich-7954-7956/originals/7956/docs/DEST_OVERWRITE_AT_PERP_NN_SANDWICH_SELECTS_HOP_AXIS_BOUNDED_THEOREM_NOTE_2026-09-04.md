---
claim_id: dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "On Z^3, curl grow is first-arrival BFS with dest L' = L × s when that product is a signed axis. One-seed curl from {(0,0,0): +e1} occupies +e2 with dest +e3 = e1 × e2 and does not occupy +e1. Overwrite dest at +e2 to each of the six signed axes, then continue curl grow. For r in {4,6,8} with grow radius r+4: overwrite dest = ±e2 occupies exactly the geometric y=0 sandwich cubes in B_r (unit cubes with min-corner y=0 and all eight vertices in B_r); overwrite dest = ±e1 or ±e3 occupies no 8/8 cube; +e2 and -e2 overwrite occupancy sets are equal; +e2 is already occupied in the one-seed grow (dest overwrite, not occupancy-extra). The grows, seeds, ball, and cube predicate are declared. The overwrite itself is supplied. Sign ± is not selected. Nothing is claimed about formation from the four axioms, Standard Model content, or a=ℓ_P."
upstream_dependencies: []
runner: scripts/dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_check_2026_09_04.py
---

# Sandwich 3-cells select dest ±hop at the already-occupied perp neighbour

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** independent audit required
**Status:** proposed_retained
**Status authority:** effective status is pipeline-derived after independent audit ratification and dependency closure.
**Primary runner:**
`scripts/dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_check_2026_09_04.py`
**Runner cache:**
`logs/runner-cache/dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_check_2026_09_04.txt`
**Parents:** none. Finite constructions are declared here.

One-seed curl already occupies the hop-neighbour of the seed. Filling the
geometric sandwich 3-cells is a dest overwrite at that site, not a new
occupied vertex. Among the six signed-axis dests, only dest parallel to the
hop fills those cubes.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite census: six dest overwrites at an already-occupied perp NN; only ±hop occupies the geometric y=0 sandwich cubes in named L2 balls."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "The overwrite dest=±hop is still supplied. Next is whether Record or Admissibility forces that overwrite, or the sign, without a new axiom."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

Curl grow: first-arrival BFS; dest updates as `L' = L × s` when that product
is a signed axis. One-seed: `{(0,0,0): +e1}`.

The runner proves, for `r ∈ {4,6,8}`:

1. One-seed occupies `+e2` with dest `+e3 = e1 × e2`, and does not occupy `+e1`.
2. Overwrite dest at `+e2` to `+e2` or to `-e2`, then curl-grow: occupied 8-vertex
   cubes in `B_r` are exactly the geometric `y=0` sandwich (`32`, `88`, `164` cubes).
3. Overwrite dest at `+e2` to `±e1` or to `±e3`: no 8/8 cube in `B_r`.
4. Occupancy *sets* of the `+e2` and `-e2` overwrites are equal. Sign is not
   selected by 3-cell occupancy.
5. `+e2` is not occupancy-extra versus one-seed. The sandwich identity is dest
   overwrite at a site the unique bilinear 1-seed already occupies.

So: if curl grow after a dest at `+e2` is to occupy the sandwich 3-cells, that
dest must be parallel to the hop. Copy dest and curl dest are ruled out among
the six axes. The overwrite remains a supplied change of dest, not a Record or
Admissibility derivation. The sign `±` remains free.

## Imports, declared inputs, and authority

- **Declared geometry:** `Z^3`, 6-NN, L2 ball, unit cubes. Role: scoring set.
- **Declared grow:** curl first-arrival `L × s`. Role: the member class.
- **Declared overwrite:** dest at `+e2` set to each signed axis before grow.
  Role: the census. Not derived from the four axioms.
- **Standard methodology:** integer BFS and set equality. Role: proof method.
- **Observational inputs:** none.

## What this does not show

- It does not force dest overwrite from Record or Admissibility.
- It does not select the sign `+e2` versus `-e2`.
- It does not occupy `+e1` (along the seed dest) from this overwrite.
- It does not yield SM content or `a=ℓ_P`.
- It does not make sandwich cubes a TOE.

## Runner

`scripts/dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_check_2026_09_04.py`

```text
TOTAL: PASS=34 FAIL=0
```
