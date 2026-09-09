# OpenReferenceGraph ↔ PatchGraph plus four-rail signed Clifford equivalence — Cycle 706

Date: 2026-07-26

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none.

Primary runner:
[`scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py`](../scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py).

Dependencies are the landed
[`RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md`](RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md)
and the
[`ENDPOINT_LOCALIZATION_THREE_ROUTE_DISCRIMINATOR_CYCLE705_NOTE_2026-07-26.md`](ENDPOINT_LOCALIZATION_THREE_ROUTE_DISCRIMINATOR_CYCLE705_NOTE_2026-07-26.md).
The runner directly reuses Pauli, GF(2), frame, and order-gauge helpers from
the Cycle-232
[`ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py`](../scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py)
and its [route note](work_history/repo/review_feedback/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_NOTE_2026-07-17.md).
The complete route packet, inventories, and N1--N8 boundary are in the
explanatory
[`CYCLE706_OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_EQUIVALENCE_NOTE_2026-07-26.md`](work_history/repo/review_feedback/CYCLE706_OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_EQUIVALENCE_NOTE_2026-07-26.md).

## Bounded result

The finite prepared `OpenReferenceGraph(2x2)` code on 80 abstract graph-edge
qubits is exactly signed-Clifford equivalent to the scheduled
`PatchGraph(2x2)` code on 76 graph-edge qubits tensor four prepared Z rails.
The map fixes all 24 logical X/Z pairs, maps 49 shared loop checks and three
independent local-D checks to their Patch counterparts, and maps four Open
bond-rectangle checks to four `Z_rail=+1` checks.

Both 80-row commuting W bases have rank 80.  The resulting 160 edge-generator
images have symplectic rank 160, exact inverse, and zero failures in all 25,600
ordered generator products including Pauli phases.  Deleting any image lowers
rank to 159; deleting any bond/rail basis row lowers W rank to 79.  The largest
image has weight 15 and cell-Manhattan diameter two.

This is an exact finite graph-code equivalence, not yet a uniformly bounded
recurrent circuit and not a literal one-M2-per-`Z^3`-site compiler.  The
general stabilizer-tableau/Clifford machinery is standard; see
[Dehaene--De Moor](https://doi.org/10.1103/PhysRevA.68.042318) and
[Aaronson--Gottesman](https://doi.org/10.1103/PhysRevA.70.052328).  The claimed
new content is only this fixture-specific signed map, its direct-map
falsifier, and the executed finite controls.

## Direct-map falsifier

The natural shared-edge relabeling plus four independent X/Y/Z rail checks is
not the signed equivalence.  All `3^4=81` axis assignments fail unsigned
rank/commutator invariants, so adding all ± characters (`6^4=1,296`) cannot
repair them.  The best uniform-Z case has target rank 56, union rank 60, ten
cross-commutator failures, 51 positive target stabilizers, one negative shared
cycle, and four rows outside the target group.

This falsifies only that natural tensor-rail map.  The constructed signed
Clifford map itself blocks any finite graph-inequivalence no-go.

## Covariance ceiling

For each of the 24 proper-cubic frames the graphs and signed equivalence are
rebuilt, and 104 semantic rows are compared: 24 logical Z, 24 logical X, and
56 source stabilizers.  All 2,496 individual-frame comparisons pass.  The 576
ordered products test direction composition, with 2,304 additional rail-label
composition checks.  They do not constitute a full 576-product semantic
tableau-diagram proof.

## Supplied / derived / open

Supplied:

- the two landed Cycle-703 graph definitions and pinned edge-list digests;
- Cycle-232 Pauli/GF(2)/frame/order-gauge helper conventions;
- the finite `2x2` path/chart, BKSF local edge order, positive loop/D/rail
  characters, and deterministic free-zero symplectic completion.

Derived:

- the 76 shared-edge bijection and four reference-bond rail labels;
- the signed Clifford Pauli map, inverse, multiplication and deletion
  certificates;
- the 1,296-choice direct-map falsifier;
- 24 individual-frame semantic diagrams and 576 direction/rail compositions.

Open:

- a bounded local Clifford circuit implementing the map without a global
  tableau solve;
- an all-volume constant-support family and held `3x3`/cube tests;
- composition with literal Z3/M2 placement, repetition, preparation, and
  nearest-neighbour control;
- autonomous rail-Z genesis/protection.

## No-go and TOE effect

N1--N8 leaves local bond-elimination, direct Patch preparation, and alternative
rail constraints open.  Therefore there is no general no-go, minimum rail
content, shared obstruction, or axiom pressure.

`C_local` improves finitely because the prior 80-versus-76 graph bifurcation is
no longer an algebraic code mismatch.  `C_ref` is sharpened to the prepared
rail-Z supply.  `C_num`, `C_wrap`, `C_int`, and `C_source` are unchanged.  No
tableau order is called time, no stabilizer sign energy, and no copied
auxiliary a Record.
