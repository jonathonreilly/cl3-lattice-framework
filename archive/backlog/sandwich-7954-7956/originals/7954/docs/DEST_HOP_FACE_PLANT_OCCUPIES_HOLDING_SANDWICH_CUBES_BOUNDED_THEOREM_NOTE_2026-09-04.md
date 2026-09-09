---
claim_id: dest_hop_face_plant_occupies_holding_sandwich_cubes_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "On Z^3 with the L2 ball B_r = {p : p·p <= r^2}, a unit cube is named by its min-corner. The geometric y=0 sandwich in B_r is the set of unit cubes whose eight vertices lie in B_r and whose min-corner has y=0. Curl grow is first-arrival BFS with dest update L' = L × s when that product is a signed axis. Inherit+perp grow is first-arrival BFS with dest copied along perpendicular steps. For r in {4,6,8}, with grow radius r+4: (A) curl grow from seeds {(0,0,0): +e1, (0,1,0): +e2} occupies exactly the geometric y=0 sandwich cubes; (B) inherit+perp grow from the four HOLDING seeds occupies exactly those same cubes; (C) curl grow from {(0,0,0): +e1, (0,-1,0): -e2} occupies exactly the geometric y=-1 sandwich; (D) those two sandwiches are disjoint and curl grow from both face plants occupies their union; (E) curl grow from {(0,0,0): +e1, (1,0,0): +e2} occupies exactly the geometric x=0 slab. At r=6 the dest=hop and HOLDING occupancy *sets* differ; every y=0 sandwich vertex is occupied in both; dests agree on exactly 26 of 218 of those vertices; 1-seed curl and dest=copy plant +e2 occupy no 8/8 cube in B_6. The seeds, dest rules, ball, and cube predicate are declared finite constructions. Nothing is claimed about formation, uniqueness, Standard Model content, or a=ℓ_P."
upstream_dependencies: []
runner: scripts/dest_hop_face_plant_occupies_holding_sandwich_cubes_check_2026_09_04.py
---

# Dest=hop face plant occupies the HOLDING sandwich 3-cells

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** independent audit required
**Status:** proposed_retained
**Status authority:** effective status is pipeline-derived after independent audit ratification and dependency closure.
**Primary runner:**
`scripts/dest_hop_face_plant_occupies_holding_sandwich_cubes_check_2026_09_04.py`
**Runner cache:**
`logs/runner-cache/dest_hop_face_plant_occupies_holding_sandwich_cubes_check_2026_09_04.txt`
**Parents:** none. The finite lattice constructions used by the claim are declared here.

Two displayed occupancy members fill the same 8-vertex cubes in a finite ball,
while occupying different vertex sets and writing different dests on the shared
cube vertices. The identity is a finite integer check. It is not a derivation
of a formation law, not a Standard Model claim, and not a TOE.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite occupancy identities on named L2 balls: occupied 8-vertex cubes of two declared grows equal a geometric sandwich, with an exact dest-agreement count on the shared vertices."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Submit the finite occupancy identity to the independent audit lane. Do not treat sandwich 3-cells as SM+gravity or as a forced seed."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

On `Z^3`, write `B_r = {p : p·p <= r^2}`. A unit cube is named by its
min-corner `(i,j,k)` and has vertices `{i,i+1} × {j,j+1} × {k,k+1}`.
The geometric `y=0` sandwich in `B_r` is the set of unit cubes whose eight
vertices all lie in `B_r` and whose min-corner has `y=0`. Analogous slabs
are defined for min-corner `y=-1` and min-corner `x=0`.

Curl grow is first-arrival BFS: from an occupied site `p` with dest `L`,
a nearest-neighbour step `s` is allowed when `L × s` is a signed axis, and
the new dest is `L × s`. Inherit+perp grow is first-arrival BFS: a step `s`
is allowed when `L · s = 0`, and the new dest is `L`.

HOLDING seeds are the four sites

```text
(0,0,0): +e1
(0,1,0): -e1
(0,0,1): +e2
(0,1,1): -e2
```

Dest=hop plant `+e2` is the two-seed curl grow from `{(0,0,0): +e1, (0,1,0): +e2}`.

For each `r ∈ {4,6,8}`, occupancy is grown in `B_{r+4}` and cubes are scored
in `B_r`. The runner proves:

1. Dest=hop plant `+e2` occupies exactly the geometric `y=0` sandwich cubes
   (`32`, `88`, `164` cubes at `r=4,6,8`).
2. HOLDING inherit+perp occupies exactly those same cubes.
3. Dest=hop plant `-e2` occupies exactly the geometric `y=-1` sandwich.
4. The two sandwiches are disjoint. Curl grow from both face plants occupies
   their union (`64`, `176`, `328` cubes).
5. Dest=`⊥L` plant `+e1` dest=`+e2` occupies exactly the geometric `x=0` slab
   (same counts as the `y=0` sandwich, by cubic symmetry of `B_r`).

At `r=6` the runner additionally proves:

6. The dest=hop and HOLDING occupancy *sets* differ.
7. All `218` vertices of the `y=0` sandwich cubes are occupied in both grows.
8. Dests on those vertices agree at exactly `26` sites and disagree at `192`.
9. One-seed curl from `{(0,0,0): +e1}` occupies no 8/8 cube in `B_6`.
10. Dest=copy plant `{(0,0,0): +e1, (0,1,0): +e1}` occupies no 8/8 cube in `B_6`.

So the sandwich 3-cells are not inherit-only: a two-seed dest=hop face plant
on the curl grow fills the same cubes. The face dest at the plant is supplied.
The 4-seed HOLDING inherit grow is a different dest field on the same 3-cells.

## Imports, declared inputs, and authority

- **Declared lattice objects:** `Z^3`, 6-NN steps, the L2 ball, and the unit-cube
  predicate are this note's finite geometry. Their role is to define the scored
  cubes. Infinite-volume, other norms, and other cell shapes remain outside.
- **Declared grows:** curl `L' = L × s` on axis-valued dests, inherit+perp dest
  copy on perpendicular steps, first-arrival BFS, grow radius `r+4`, and the
  named seeds are supplied constructions. Their provenance is this note. The
  four axioms do not select these dest rules or these seeds.
- **HOLDING seed tuple:** the four sites and dests are a declared 4-seed. They
  are not derived from Admissibility or Record.
- **Face plant:** dest=`+e2` at `(0,1,0)` (and the minus and `⊥L` plants) are
  supplied extra seeds. The 1-seed curl control occupies no 8/8 cube, so the
  plant is load-bearing for the sandwich identity.
- **Standard methodology:** integer arithmetic on a finite ball, set equality
  of cube min-corners, and first-arrival BFS are proof methods. The runner
  checks the identities; their role is methodology.
- **Observational inputs:** none. No `⟨P⟩`, hop-cost, `L_phys`, Born weights,
  Gleason, Einstein, or Standard Model data enter the checks.

## What this does not show

- It does not derive dest=hop or HOLDING inherit from the four axioms.
- It does not force the face plant. Without it, 1-seed curl has `n8=0` in `B_6`.
- It does not identify dests: on the shared `218` vertices dests agree at `26`
  sites only.
- It does not produce a `(4,2,2)` fermion marker, chirality, colour, or
  `a=ℓ_P`.
- It does not occupy `Z^3`. Sandwich cubes at `r=6` all have min-corner `y=0`.
- Cauchy `A/4 = C` language is not used as a selector; the cube counts are
  the geometric sandwich enumerations in `B_r`.

## Runner

`scripts/dest_hop_face_plant_occupies_holding_sandwich_cubes_check_2026_09_04.py`

Exact integer checks, `AUDIT_TIMEOUT_SEC = 60`.

```text
TOTAL: PASS=25 FAIL=0
```

Cache: `logs/runner-cache/dest_hop_face_plant_occupies_holding_sandwich_cubes_check_2026_09_04.txt`.
