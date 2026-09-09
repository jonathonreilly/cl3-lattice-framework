---
claim_id: dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Finite fresh-initialization census for first-arrival FIFO curl grow on Z^3 with ordered seeds and steps. For scored radii 4,6,8 and grow radii 8,10,12, each fresh two-seed dictionary {origin:+e1,+e2:d} is grown independently for each signed-axis d. Only d=+e2 or -e2 fills exactly the geometric y=0 sandwich cubes; the other four choices fill no complete cube. The two successful candidates have equal occupancy sets and occupy +e1 with destinations -e1 and +e1 respectively. A separate one-seed baseline occupies +e2 with destination +e3 and leaves +e1 vacant. These are alternative initializations, not overwrite-and-continuation or physical Record intervention."
upstream_dependencies: []
runner: scripts/dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_check_2026_09_04.py
---

# Fresh two-seed curl grows: only the ±hop destinations fill the sandwich

**Original date:** 2026-09-04. **Correction date:** 2026-09-09.
**Author scope:** exact finite integer constructions; no retained grade.
**Audit:** formal audit deferred by the owner; landing review grants no audit verdict.
**Primary runner:** `scripts/dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_check_2026_09_04.py`.
**Evidence:** `logs/runner-cache/dest_overwrite_at_perp_nn_sandwich_selects_hop_axis_check_2026_09_04.txt`.

The six cases start independently from two seeds. They do not overwrite the
completed one-seed grow. The successful cases also occupy the site +e1,
which is vacant only in the separate one-seed baseline. These distinctions
correct the old temporal interpretation and its false vacancy statement.

## Finite definitions

Sites are integer triples. Signed-axis destinations are ±e1,±e2,±e3.
The L2 ball is `B_r={p:dot(p,p)<=r²}`. A cube has the eight vertices
`{i,i+1} x {j,j+1} x {k,k+1}`; its label is minimum corner `(i,j,k)`.
The geometric y=0 sandwich consists of cubes with j=0 and all vertices in B_r.

Curl grow initializes `formed=dict(seeds)` and a FIFO queue from the seed keys
in insertion order. For each popped site p with destination L, steps are
visited in the fixed order `+e1,-e1,+e2,-e2,+e3,-e3`. A step s is allowed
when `L cross s` is a signed axis and p+s lies in the grow ball. An unoccupied
site is assigned that destination and appended. Existing assignments are never
changed or erased by the grow rule. The origin seed precedes the +e2 seed.
The rule, seeds, ordering, grow margin and scoring predicate are supplied.
No uniqueness among bilinear rules or universal order independence is proved.

## What the finite census establishes

For each scored r in {4,6,8}, grow in B_(r+4):

1. A separate baseline `grow_curl({origin:+e1},r+4)` occupies +e2 with
   destination +e3 and does not occupy +e1.
2. Each of the six candidates is a **fresh**
   `grow_curl({origin:+e1,+e2:d},r+4)`. For d=+e2 and d=-e2, the complete
   cubes equal the geometric y=0 sandwich: 32,88,164 cubes at r=4,6,8.
3. The other four initial destinations, ±e1 and ±e3, yield no complete cube.
4. The successful ±e2 candidates have equal occupancy sets. This finite
   predicate selects neither sign.
5. Both successful candidates occupy +e1. The +e2 candidate assigns -e1 there;
   the -e2 candidate assigns +e1. The runner checks the actual candidate
   dictionaries, separately from the baseline's vacancy.
6. The site +e2 belongs to the baseline and both candidates. This fact concerns
   only that particular site's membership across separate runs. At r=6, grow=10,
   **each successful candidate omits 413 sites** of the completed baseline.
   The runner checks the actual set differences. Since grow never erases a
   previously formed site, a fresh candidate cannot be a retained-state
   continuation of that completed baseline.

A local path explains the positive candidate's +e1 assignment: start at +e2
with L=+e2, step +e1 to (1,1,0) with L=-e3, then step -e2 to +e1 with L=-e1.
For L=-e2 at the initial second seed, the two destination signs reverse.
The full candidate checks establish these assignments under the stated
first-arrival convention, rather than assuming the local path arrives first.

The old phrase 'overwrite at an already-occupied site' conflated separate
counterfactual initializations. No temporal protocol is established. An actual
intervention would need its own time, retained state, queue and assignment
rules. In particular, this construction licenses no overwrite of a permanent
physical Record. No physical formation rule or seed selection follows.

## Inputs, limits and next use

All geometry, functions and fixtures are defined here and in the standalone
integer runner. No repository scientific helper, data or graded supplier is
consumed. Each runner declares and verifies its own exact note as input;
its current cache binds that note and the actual runner. The preserved original
review independently reproduced the finite census with signed-axis orientation
lookup and a farthest-corner ball criterion; the corrected primary retains all
original predicates and adds the candidate-membership and set-loss controls.

The scope is these radii, finite balls, six destination choices, seeds and queue
conventions. No global-radius theorem, unique-rule classification, physical
Record intervention, Standard Model content, species or absolute scale is
claimed. Use the finite census as conditional exploration; a physical growth
law remains open. Formal audit waits for the owner's later TOE milestone.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: reuse the finite fresh-seed census with explicit queue conventions; physical formation and seed selection remain open
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The [historical recovery inventory](../archive/backlog/sandwich-7954-7956/HISTORY.md)
preserves the exact original six science bodies. Historical manifest deltas
remain external recovery and do not replace current main. The active path and
claim identifier retain the old wording solely for provenance; this corrected
body supplies the current author scope.
