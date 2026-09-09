# Gate B: Evolving Network Dynamics — Current Status

**Date:** 2026-04-04
**Status:** bounded generated-geometry source index; not a physical-gravity or
primitive-to-readout bridge
**Claim type:** open_gate
**Audit-scope narrow:** 2026-06-08

## 2026-06-16 weak-field source/action interface split

The post-audit source/action repair
[`GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md`](GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md)
splits `GB-S1` into two pieces:

| ID | Piece | Current status |
|---|---|---|
| `GB-S1a` | linear weak-field test-action form `S = L (1 - phi)` | bounded-support interface from the retained-bounded weak-field source-response bridge |
| `GB-S1b` | runner scalar `phi_GB(x)=strength/(r(x,mass)+0.1)`, finite-core regulator, and normalization | still supplied Gate-B runner data |

This narrows the earlier black-box boundary without closing Gate B. The parent
Gate B row remains an open gate: it still does not derive a Gate B dynamics
theorem, the `GB-S1b-b` physical scalar source/boundary/regulator/normalization,
`GB-S2b` physical-readout semantics, or the `GB-S3b` physical-growth selector
from retained framework primitives. These splits add no new axiom, Tier-A
admission, or audit-status change.

## 2026-06-18 finite path-sum propagation split

The source-side bridge
[`GATE_B_FINITE_PATH_SUM_PROPAGATION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md`](GATE_B_FINITE_PATH_SUM_PROPAGATION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md)
splits `GB-S2` into two pieces:

| ID | Piece | Current status |
|---|---|---|
| `GB-S2a` | finite complex-amplitude propagation on the supplied layered DAG | bounded-support source bridge: the runner recursion is exactly the finite path-sum transfer over unblocked directed paths, with a finite linear transfer operator and normalized terminal detector distribution once a detector set is supplied |
| `GB-S2b` | physical detector-window mass-gain, `TOWARD`, and `F~M` readout semantics | still supplied Gate-B runner data |

This removes a bookkeeping ambiguity in the propagation packet: the update rule
is not an opaque numerical procedure. It is the exact finite path expansion of
the declared edge kernel on the declared finite DAG. The physical interpretation
of the detector window, `TOWARD` sign, and `F~M` slope remains open. This
update does not derive `GB-S1b`, `GB-S3`, a physical gravity readout, or a full
Gate B dynamics theorem.

## 2026-06-18 local stencil connectivity split

The source-side bridge
[`GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md`](GATE_B_LOCAL_STENCIL_CONNECTIVITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md)
splits `GB-S3` into two pieces:

| ID | Piece | Current status |
|---|---|---|
| `GB-S3a` | label/offset-preserving forward stencil on the finite `Z^3` slab | bounded-support source bridge: the stencil is a finite-range local lattice relation, translation-covariant in the interior, boundary-clipped on the finite slab, and exactly matches the adjacency used by `scripts/gate_b_connectivity_tolerance.py` |
| `GB-S3b` | physical selection or dynamical generation of that stencil as the Gate B growth rule | still open Gate-B dynamics data |

This removes one avoidable ambiguity in the generated-connectivity packet: the
runner's positive label/offset family is not an arbitrary KNN or nonlocal graph
choice. It is the finite-slab restriction of a fixed local stencil on the
framework lattice. The stronger physical-growth claim remains open. This update
does not derive `GB-S1b`, `GB-S2`, a physical gravity readout, or a full Gate B
dynamics theorem.

## 2026-06-18 finite radial scalar split

The source-side bridge
[`GATE_B_FINITE_RADIAL_SCALAR_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md`](GATE_B_FINITE_RADIAL_SCALAR_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-18.md)
splits `GB-S1b` into two pieces:

| ID | Piece | Current status |
|---|---|---|
| `GB-S1b-a` | finite runner scalar `phi_GB(x)=strength/(r(x,mass)+0.1)` on the supplied coordinate slab | bounded-support source bridge: the scalar is positive, finite, radially monotone in the supplied Euclidean coordinate distance, exactly matches the runner helper, and is linear in the source-strength normalization |
| `GB-S1b-b` | physical Poisson/source equation, boundary condition, regulator selection, and absolute normalization | still open Gate-B runner/physics data |

This removes one avoidable black-box part of the source packet: the runner
scalar is now an explicit finite radial field with a checked regulator and
linear normalization dependence. The stronger physical claim remains open:
this update does not derive the Poisson PDE, the `0.1` finite-core regulator,
the source strength, `GB-S2` propagation/readout semantics, `GB-S3`
generated-connectivity rule, a physical gravity readout, or a full Gate B
dynamics theorem.

## 2026-06-17/18 context-independence no-go

The source-side no-go
[`GATE_B_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md`](GATE_B_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md)
proves that the remaining physical packet pieces are not hidden content of the
current Lattice + Quantum + Record axiom surface. Two completions can share the
same fixed `Z^3` nearest-neighbor patch while assigning different physical
scalar source/regulator/normalization choices, different detector/readout
windows, and different generated-growth rules.

This does not refute the finite Gate B numerics or the bounded-support split
notes above. It says the current axioms cannot derive `GB-S1b-b`, `GB-S2b`, or
`GB-S3b`. The row therefore stays an open-gate bounded generated-geometry
source index until a separate local-growth/dynamics/readout theorem lands.
This no-go adds no axiom, Tier-A admission, Gate B closure, or audit-status
change.

## 2026-06-12 audit firewall: source index, not dynamics closure

The audited missing bridges remain `GB-S1b-b`, `GB-S2b`, and `GB-S3b`: the Gate
B runner's physical scalar source/boundary/regulator/normalization remains
supplied, physical detector-window/TOWARD/`F~M` semantics remain supplied, and
physical selection/dynamical generation of that stencil remains supplied. The
primary connectivity replay and companion manifest verify finite
generated-geometry behavior inside that supplied packet only.

This row is therefore an **open-gate source index**. It does not derive a
Gate B dynamics theorem, physical gravity/readout bridge, or primitive local
growth rule from retained framework primitives, and it introduces no new
axiom, Tier-A admission, or audit-status change.

## 2026-06-08 Audit-Scope Narrow

This row is a source-side index over bounded generated-geometry numerical
companions. It is not itself a theorem deriving the primitive growth rule, the
physical gravity/readout bridge, or a full-family Gate B closure.

When older sections below say that a slice is "closed", read that only as:

```text
the named frozen runner-local far-field slice passed its tested sign/F~M gates
inside the supplied generated-geometry harness.
```

That wording does not promote a framework-native generated-geometry theorem.
The stronger science target remains open: derive the local growth/connectivity
rule and the physical gravity/readout semantics from retained framework
primitives.

## 2026-06-09 Row-Local Source-Packet Manifest

This manifest is the current re-audit target for the Gate B row. It does not
derive a clean Gate B dynamics theorem. It discloses the supplied ingredients
of the bounded generated-geometry packet so the row can be audited as a source
index rather than as an independent primitive-to-physical-gravity bridge.

**Manifest runner:**
[`scripts/gate_b_source_packet_manifest_2026_06_09.py`](../scripts/gate_b_source_packet_manifest_2026_06_09.py)
**Cached output:**
[`logs/runner-cache/gate_b_source_packet_manifest_2026_06_09.txt`](../logs/runner-cache/gate_b_source_packet_manifest_2026_06_09.txt)

| ID | Supplied ingredient | Row-local definition | Status boundary |
|---|---|---|---|
| `GB-S1` | valley-linear source/action rule | The runners use the scalar field `f(x) = strength/(r(x, mass)+0.1)` and the forward phase action `S = L(1 - f)` with the declared constants in the paired scripts. | Split by the 2026-06-16 interface note and 2026-06-18 scalar bridge: the linear `S=L(1-phi)` response form has bounded weak-field support (`GB-S1a`), and the finite radial runner scalar has bounded-support as checked algebra on the supplied coordinate slab (`GB-S1b-a`), but the physical Poisson/source equation, regulator choice, and absolute normalization remain supplied (`GB-S1b-b`). Not fully derived from retained primitives and not a new axiom. |
| `GB-S2` | propagation/readout semantics | The runners use forward-layer path propagation, a central blocked barrier, detector-window mass gain, `TOWARD` sign, and local `F~M` log-slope readouts. | Split by the 2026-06-18 finite path-sum bridge: the finite propagation recursion itself is exact path-sum algebra (`GB-S2a`), but the central barrier, detector-window mass gain, `TOWARD`, and `F~M` physical readout semantics remain supplied (`GB-S2b`). |
| `GB-S3` | generated-connectivity rule | The positive generated-geometry rows use label/offset-preserving forward connectivity with drift/restore companions; KNN and non-label candidates are recorded as controls or bounded negatives where their sign/`F~M` package weakens. | Split by the 2026-06-18 local-stencil bridge: the label/offset stencil itself has bounded-support as a finite-range `Z^3` local relation matching the runner adjacency (`GB-S3a`), but the physical selection/dynamical generation of that stencil remains supplied (`GB-S3b`). |

The direct source packet is therefore:

```text
I_GateB = (GB-S1 weak-field action plus finite radial scalar
              with supplied physical source/boundary/regulator/normalization,
           GB-S2 finite propagation plus supplied physical readout semantics,
           GB-S3 local stencil plus supplied physical-growth selector,
           frozen seed/geometry rows recorded in the companion notes).
```

The load-bearing claim is only conditional on `I_GateB`: the named frozen
runners compute sign, local `F~M`, distance-law, and non-gravity companion
readouts for the declared rows. The row does not promote `I_GateB` to a
repo-wide accepted premise, retained theorem, physical gravity theorem, or
closed Gate B dynamics theorem.

**Re-audit target.** Audit this note as a bounded generated-geometry source
index/open gate with a fully visible supplied packet. Re-audit as a clean Gate B
dynamics theorem only after a separate theorem derives `GB-S1`, `GB-S2`, and
`GB-S3` from retained primitives.

## The question

Can we grow (rather than impose) geometry that gives Newtonian gravity?

## What was tested

Primary frozen replay for the current connectivity-vs-noise read:

- [scripts/gate_b_connectivity_tolerance.py](../scripts/gate_b_connectivity_tolerance.py)
- [logs/2026-04-04-gate-b-connectivity-tolerance.txt](../logs/2026-04-04-gate-b-connectivity-tolerance.txt)
- [docs/GATE_B_CONNECTIVITY_TOLERANCE_NOTE.md](GATE_B_CONNECTIVITY_TOLERANCE_NOTE.md)

Structured-connectivity follow-up:

- [scripts/evolving_network_prototype_v4.py](../scripts/evolving_network_prototype_v4.py)
- [logs/2026-04-04-evolving-network-prototype-v4.txt](../logs/2026-04-04-evolving-network-prototype-v4.txt)
- [docs/EVOLVING_NETWORK_PROTOTYPE_V4_NOTE.md](EVOLVING_NETWORK_PROTOTYPE_V4_NOTE.md)

Latest bounded follow-up:

- [scripts/evolving_network_prototype_v5.py](../scripts/evolving_network_prototype_v5.py)
- [logs/2026-04-04-evolving-network-prototype-v5.txt](../logs/2026-04-04-evolving-network-prototype-v5.txt)
- [docs/EVOLVING_NETWORK_PROTOTYPE_V5_NOTE.md](EVOLVING_NETWORK_PROTOTYPE_V5_NOTE.md)

The primary runner reports per-architecture TOWARD fractions and a local
`F~M` response-slope probe (mean over the six frozen seeds). These match the
retained companion [docs/GATE_B_CONNECTIVITY_TOLERANCE_NOTE.md](GATE_B_CONNECTIVITY_TOLERANCE_NOTE.md):

1. **Jittered NN lattice** (positions jittered, fixed connectivity):
   `75.0%` TOWARD at jitter `0.5`; across the jitter sweep `0.0-0.5` the
   TOWARD fraction stays in the `47.2%-75.0%` band with local `F~M` in the
   `0.47-0.75` band. Born stays at machine precision. The response degrades
   gradually rather than at a cliff; it does not collapse.

2. **Templated growth** (copy prev layer + jitter, NN offsets):
   `27.8%` TOWARD, local `F~M = 0.27`. Position drift accumulates across
   layers and the response becomes mixed.

3. **K-NN grown** (relaxed positions, 9-nearest connectivity):
   `55.6%` TOWARD, local `F~M = 0.55`. Asymmetric connectivity weakens
   coherence.

4. **Grid-snapped grown** (relaxed positions, snapped NN connectivity):
   `58.3%` TOWARD, local `F~M = 0.58`. Inconsistent grid assignment.

For reference, the ordered-lattice baseline is `66.7%` TOWARD with local
`F~M = 0.66` on the same frozen seeds.

## Key insight

**Position noise is tolerated. Connectivity structure is critical.**

The valley-linear action gives TOWARD gravity on any graph with:
- Forward-only edges (layer l → layer l+1)
- NN-like connectivity (fixed offsets, not distance-based neighbors)
- Approximately uniform node spacing (within 0.5h tolerance)

The growth rule must produce **structured connectivity**, not just
regular spacing. K-nearest-neighbor connectivity on relaxed positions
does NOT suffice — the resulting edge structure is too asymmetric.

## What the local `F~M` probe tells us

On this connectivity-tolerance primary replay, the local `F~M`
response-slope probe stays in a bounded band (`0.27-0.75` across the tested
architectures and jitter levels) rather than collapsing — it does not show
a cliff even where the TOWARD fraction is mixed (e.g. templated growth at
`27.8%` TOWARD keeps `F~M = 0.27`). The mass-side response is therefore more
stable under connectivity changes than the gravity sign, but the local
`F~M` values on this near-field harness are **not** universal constants and
should not be read as a promoted `F∝M = 1.00` law. The clean retained
`F∝M = 1.00` mass-scaling result lives on the far-field harness
([docs/GATE_B_FARFIELD_NOTE.md](GATE_B_FARFIELD_NOTE.md)),
not on this connectivity-tolerance replay.

## Path forward

The remaining gap is a growth rule that produces structured connectivity.
Options:

1. **Crystal-like templating with restoring force**: copy previous layer,
   add jitter, but pull toward grid positions. Prevents cumulative drift.

2. **Edge structure rule**: instead of computing NN from positions, define
   edges by a LOCAL rule (each node connects to the node "opposite" it
   in the previous layer's neighborhood). This is connectivity-first growth.

3. **Accept the lattice**: the lattice IS the continuum limit. The
   dynamics question becomes "what produces regular structure at large
   scale?" rather than "can we grow a specific graph that works?"

## Honest status for reviewers

The model can produce TOWARD gravity on grown geometry IF the connectivity
is approximately grid-structured. A fixed connectivity backbone tolerates
substantial position noise (the jitter sweep degrades gradually across
`0.0-0.5` rather than at a cliff). The remaining challenge is producing the
grid-like connectivity from a local rule. The clean `F∝M = 1.00`
mass-scaling closure is the separate far-field harness result, not this
near-field connectivity-tolerance replay.

This is a genuine partial result, not a failure: the position-noise
tolerance is quantified on this replay, the local mass-side response stays
in a bounded band rather than collapsing, and the connectivity requirement
is identified.

The newest v4 crystal-like growth rule is the first explicit
structured-connectivity prototype guided by that lesson. It remains mixed and
does not close Gate B, but it is a cleaner next-step prototype than the older
pure KNN or pruning-only lanes.

The newer v5 cross-growth follow-up is the current best bounded Gate B row:

- it improves the TOWARD rate over the matched KNN control on the same grown
  positions
- it also improves the local `F~M` slope over that control
- it does **not** cleanly beat the KNN control on mean delta

So the current safe Gate B read is:

- connectivity-first growth is better than generic recomputed KNN
- the advantage is now visible in a frozen artifact chain
- but the result is still mixed enough that Gate B remains open

## Update: frozen h=0.5 structured-growth replay

The newer h=0.5 structured-growth lane is now frozen on disk:

- [scripts/evolving_network_prototype_v6.py](../scripts/evolving_network_prototype_v6.py)
- [logs/2026-04-04-evolving-network-prototype-v6.txt](../logs/2026-04-04-evolving-network-prototype-v6.txt)
- [docs/EVOLVING_NETWORK_PROTOTYPE_V6_NOTE.md](EVOLVING_NETWORK_PROTOTYPE_V6_NOTE.md)

It does **not** reproduce the branch headline of `100%` TOWARD across the full
tested matrix. The frozen rows are:

- `drift=0.3, restore=0.5`: `33/36` TOWARD, `mean_delta=+0.000021`, `F~M=1.00`
- `drift=0.2, restore=0.7`: `24/36` TOWARD, `mean_delta=+0.000010`, `F~M=1.00`
- `drift=0.1, restore=0.9`: `24/36` TOWARD, `mean_delta=+0.000008`, `F~M=0.99`
- `drift=0.0, restore=1.0`: `24/36` TOWARD, `mean_delta=+0.000007`, `F~M=0.99`

So the safe Gate B read is now:

- the h=0.5 structured-growth lane is genuinely TOWARD and near-linear
- the best tested row is stronger than the older bounded prototypes
- the full tested matrix is still mixed enough that Gate B remains open

## Diagnosis: v6 mixed result is a near-field effect (2026-04-04)

The v6 frozen replay uses near-slit mass positions (y=1.0, 1.5) and
varied field strengths (0.75-1.25x). These are near-field parameters
where even the FIXED lattice gives noisy gravity.

Controlled comparison at z≥2 with standard strength:
| Size | drift=0.3 | drift=0.2 | exact grid |
|------|-----------|-----------|------------|
| HALF=5 (v6) | 88% | 100% | 100% |
| HALF=12 | 96% | 100% | 100% |

The growth rule itself is not the bottleneck — the near-field
parameter choice in the v6 replay is what creates the mixed signal.

**Honest status:** Gate B is strong in the far field (z≥2) but
noisy in the near field (z≤1.5). This is a lattice-size effect,
not a growth-rule failure. The v6 mixed result is an honest
characterization of the near-field regime.

## Frozen far-field harness (2026-04-05)

Dedicated far-field artifact chain:

- [`scripts/gate_b_farfield_harness.py`](../scripts/gate_b_farfield_harness.py)
- [`logs/2026-04-05-gate-b-farfield-harness.txt`](../logs/2026-04-05-gate-b-farfield-harness.txt)
- [`docs/GATE_B_FARFIELD_NOTE.md`](GATE_B_FARFIELD_NOTE.md)

Results at h=0.5, 12 seeds × z=[3,4,5] = 36 tests per row:

| drift | restore | TOWARD | F∝M |
|-------|---------|--------|-----|
| 0.3 | 0.5 | 36/36 (100%) | 1.00 |
| 0.2 | 0.7 | 36/36 (100%) | 1.00 |
| 0.1 | 0.9 | 36/36 (100%) | 1.00 |
| 0.0 | 1.0 | 36/36 (100%) | 1.00 |

**Gate B far-field bounded slice:** the frozen runner-local generated-geometry
harness gives 100% TOWARD with F∝M=1.00 at all drift/restore levels in the far
field (z≥3).

The near-field (z≤2) remains mixed on both grown and fixed lattices.
This is a beam-optics effect, not a growth-rule or physics failure.

## Frozen v6 near-field comparator (2026-04-05)

Dedicated exact-vs-grown control:

- [`scripts/gate_b_v6_nearfield_comparator.py`](../scripts/gate_b_v6_nearfield_comparator.py)
- [`logs/2026-04-05-gate-b-v6-nearfield-comparator.txt`](../logs/2026-04-05-gate-b-v6-nearfield-comparator.txt)
- [`docs/GATE_B_V6_NEARFIELD_COMPARATOR_NOTE.md`](GATE_B_V6_NEARFIELD_COMPARATOR_NOTE.md)

Frozen bucket summary for the retained `drift = 0.3`, `restore = 0.5` row:

| `y_mass` | exact control | grown row |
| --- | --- | --- |
| `1.0` | `0/3` `TOWARD`, mean `-0.000019` | `9/12` `TOWARD`, mean `+0.000006` |
| `1.5` | `3/3` `TOWARD`, mean `+0.000011` | `12/12` `TOWARD`, mean `+0.000023` |
| `2.0` | `3/3` `TOWARD`, mean `+0.000030` | `12/12` `TOWARD`, mean `+0.000035` |

This sharpens the near-field diagnosis:

- the mixed v6 signal is confined to the closest near-field bucket
- the ordered-lattice control is already worse on that bucket
- only one of the four retained grown seeds flips all three closest-bucket
  strengths

So the safe read is stronger than “near-field mixed” alone:

- the v6 misses are not evidence that the structured-growth rule collapses
  relative to the exact grid
- the mixed bucket is best read as a bounded near-field optics issue

## Generated-geometry companion package (2026-04-05)

The far-field Gate B lane now has dedicated companion replays for the retained
moderate-drift row:

- [`scripts/gate_b_grown_distance_law.py`](../scripts/gate_b_grown_distance_law.py)
- [`logs/2026-04-05-gate-b-grown-distance-law.txt`](../logs/2026-04-05-gate-b-grown-distance-law.txt)
- [`docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
- [`scripts/gate_b_grown_joint_package.py`](../scripts/gate_b_grown_joint_package.py)
- [`logs/2026-04-05-gate-b-grown-joint-package.txt`](../logs/2026-04-05-gate-b-grown-joint-package.txt)
- [`docs/GATE_B_GROWN_JOINT_PACKAGE_NOTE.md`](GATE_B_GROWN_JOINT_PACKAGE_NOTE.md)

These companions sharpen the safe Gate B read:

- retained far-field sign / `F~M` closure remains the main result
- the retained moderate-drift grown row also keeps a positive declining
  distance-law fit close to the exact-grid row on the tested `z = 3..7` window
- the same retained grown row keeps Born at machine precision and leaves the
  joint `d_TV` / `MI` / decoherence read nearly unchanged from the exact grid

So the honest status is now:

- far-field generated geometry is a real bounded positive with companion
  support for distance and joint non-gravity observables
- the mixed near-field region is now localized to the closest tested bucket,
  where the exact control is already worse than the retained grown row
- full-family Gate B closure remains open

## Non-label connectivity candidate (2026-04-05)

The degree-balanced non-label forward candidate is now frozen too:

- [`scripts/gate_b_nonlabel_connectivity_v3.py`](../scripts/gate_b_nonlabel_connectivity_v3.py)
- [`logs/2026-04-05-gate-b-nonlabel-connectivity-v3.txt`](../logs/2026-04-05-gate-b-nonlabel-connectivity-v3.txt)
- [`docs/GATE_B_NONLABEL_CONNECTIVITY_V3_NOTE.md`](GATE_B_NONLABEL_CONNECTIVITY_V3_NOTE.md)

Its bounded read is:

- exact grid: `12/12` TOWARD, `F~M = 1.00`
- no-restore label-NN control: `12/12` TOWARD, `F~M = 1.00`
- no-restore degree-balanced matching candidate: `10/12` TOWARD, `F~M = 0.75`

So the non-label candidate preserves most far-field sign rows, but it does
not retain the clean `F~M = 1.00` class on this family.

That makes it a bounded negative for the current non-label forward-connectivity
idea, not a replacement for the label-based far-field rule.

## One-step h=0.25 scaling companion (2026-04-05)

The same moderate-drift generated-geometry family now also has bounded
`h = 0.25` refinement companions:

- [`scripts/gate_b_h025_farfield.py`](../scripts/gate_b_h025_farfield.py)
- [`logs/2026-04-05-gate-b-h025-farfield.txt`](../logs/2026-04-05-gate-b-h025-farfield.txt)
- [`docs/GATE_B_H025_FARFIELD_NOTE.md`](GATE_B_H025_FARFIELD_NOTE.md)
- [`scripts/gate_b_h025_distance_law.py`](../scripts/gate_b_h025_distance_law.py)
- [`logs/2026-04-05-gate-b-h025-distance-law.txt`](../logs/2026-04-05-gate-b-h025-distance-law.txt)
- [`docs/GATE_B_H025_DISTANCE_LAW_NOTE.md`](GATE_B_H025_DISTANCE_LAW_NOTE.md)
- [`scripts/gate_b_h025_joint_package.py`](../scripts/gate_b_h025_joint_package.py)
- [`logs/2026-04-05-gate-b-h025-joint-package.txt`](../logs/2026-04-05-gate-b-h025-joint-package.txt)
- [`docs/GATE_B_H025_JOINT_PACKAGE_NOTE.md`](GATE_B_H025_JOINT_PACKAGE_NOTE.md)

Their bounded read is:

- far-field sign / `F~M` stay clean on the compact `h = 0.25` family:
  exact grid `12/12` TOWARD, grown `drift = 0.2` `12/12` TOWARD, both with
  `F~M = 1.00`
- the compact distance-law companion stays positive and declining:
  exact grid `b^(-0.42)`, grown `b^(-0.54)`
- the compact joint-package companion stays in the same qualitative Born /
  interference / decoherence regime as the exact grid

So the safe Gate B read is now:

- the retained moderate-drift generated-geometry lane is no longer just a
  coarse `h = 0.5` positive
- it now has one bounded `h = 0.25` refinement companion on the same family
- near-field and broader generated-geometry closure remain open

## Weak-connectivity boundary (2026-04-05)

The no-restore weak-connectivity lane is now frozen separately:

- [`scripts/gate_b_weak_connectivity_harness.py`](../scripts/gate_b_weak_connectivity_harness.py)
- [`logs/2026-04-05-gate-b-weak-connectivity-harness.txt`](../logs/2026-04-05-gate-b-weak-connectivity-harness.txt)
- [`docs/GATE_B_WEAK_CONNECTIVITY_NOTE.md`](GATE_B_WEAK_CONNECTIVITY_NOTE.md)

Its bounded read is:

- no-restore label-NN control still gives `12/12` TOWARD and `F~M = 1.00`
- the weaker no-restore KNN+floor candidate collapses to `0/12` TOWARD and
  `F~M = 0.00`

So the restoring force is not the whole story. The connectivity rule is the
critical piece, and the weaker position-based candidate does **not** carry the
far-field package on this retained family.

## Non-label forward-cone candidate (2026-04-05)

The no-restore grown-geometry lane now has a second bounded non-label
candidate:

- [`scripts/gate_b_nonlabel_connectivity_v2.py`](../scripts/gate_b_nonlabel_connectivity_v2.py)
- [`logs/2026-04-05-gate-b-nonlabel-connectivity-v2.txt`](../logs/2026-04-05-gate-b-nonlabel-connectivity-v2.txt)
- [`docs/GATE_B_NONLABEL_CONNECTIVITY_V2_NOTE.md`](GATE_B_NONLABEL_CONNECTIVITY_V2_NOTE.md)

Its bounded read is:

- no-restore label-NN control still gives `12/12` TOWARD and `F~M = 1.00`
- the no-restore forward-cone candidate gets only `8/12` TOWARD and `F~M = 0.50`

So the forward-cone rule is a bounded negative: it preserves some far-field
sign rows, but it does **not** keep the Newtonian mass-scaling class cleanly.

## No-restore hierarchy (2026-04-05)

The no-restore lane is now bounded more sharply too:

- [`scripts/gate_b_no_restore_farfield.py`](../scripts/gate_b_no_restore_farfield.py)
- [`logs/2026-04-05-gate-b-no-restore-farfield.txt`](../logs/2026-04-05-gate-b-no-restore-farfield.txt)
- [`docs/GATE_B_NO_RESTORE_FARFIELD_NOTE.md`](GATE_B_NO_RESTORE_FARFIELD_NOTE.md)
- [`scripts/gate_b_no_restore_joint_package.py`](../scripts/gate_b_no_restore_joint_package.py)
- [`logs/2026-04-05-gate-b-no-restore-joint-package.txt`](../logs/2026-04-05-gate-b-no-restore-joint-package.txt)
- [`docs/GATE_B_NO_RESTORE_JOINT_PACKAGE_NOTE.md`](GATE_B_NO_RESTORE_JOINT_PACKAGE_NOTE.md)

Their bounded read is:

- far-field gravity is surprisingly robust without restore on the label-based
  family:
  - `drift = 0.0` through `0.3`: `6/6` TOWARD, `F~M = 1.00`
  - `drift = 0.5`: `5/6` TOWARD, `F~M = 1.00`
- the non-gravity joint package is not comparably robust:
  - `drift = 0.0` still matches the exact-grid row
  - once drift is turned on, `d_TV`, `MI`, and decoherence become sharply
    drift-sensitive on the frozen one-seed replay

So the clean hierarchy is now:

- restore is **not** required for the basic far-field sign / mass-law slice on
  the label-connectivity family
- restore still matters if the goal is to preserve the broader lattice-like
  interference / decoherence package

## 2026-06-15 audit-unlock residual certificate

This source update re-opens the row as a dynamics-harness packet, not a Gate-B
foundation theorem. The runner's graph-family propagation and
connectivity-tolerance checks remain useful diagnostics.

The live blocker is the three-part `I_GateB` input set: the valley-linear
source/action rule, propagation and readout semantics, and genericity or
exhaustiveness of the tested family. Until those are derived or approved,
the harness cannot establish Gate-B dynamics as framework-native. This repair
adds no Gate-B axiom, family-genericity assumption, or audit status.
