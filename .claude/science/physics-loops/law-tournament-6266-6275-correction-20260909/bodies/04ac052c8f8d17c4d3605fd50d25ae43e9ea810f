# Cycle 707 literal PatchGraph Z3/M2 placement and projected-controller trace

**Date:** 2026-07-26

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Placement input:**
[`ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_NOTE_2026-07-17.md`](work_history/repo/review_feedback/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_NOTE_2026-07-17.md)

**Controller inputs:**
[`FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md`](FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md)
and
[`FULL128_TWO_RAIL_FIXED_LAW_COMPOSITIONAL_INDUCTION_BOUNDED_THEOREM_NOTE_2026-07-24.md`](FULL128_TWO_RAIL_FIXED_LAW_COMPOSITIONAL_INDUCTION_BOUNDED_THEOREM_NOTE_2026-07-24.md)

**Cycle-706 graph-code input:**
[`OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md`](OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md)

**Proper-cubic frame input:**
[`PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md`](work_history/repo/review_feedback/PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md)

**Primary runner:**
[`scripts/frontier_literal_patchgraph_z3_m2_placement_controller_cycle707_2026_07_26.py`](../scripts/frontier_literal_patchgraph_z3_m2_placement_controller_cycle707_2026_07_26.py)

## Result

The corrected open `2 x 2` PatchGraph can be placed literally on `Z3` with
one physical `M2` factor per occupied site. The graph has 76 abstract
graph-edge qubits: 72 onsite octahedral/spoke edges and four intercell matter-stream
edges. Cycle 232's stream repetition uses two sites for each stream edge, so
the literal carrier has exactly 80 occupied physical M2 sites.

The 76-edge target is therefore viable. The optional prepared graph adds one
edge-gauge `M2` at each of the four unused seam midpoints and has 84 occupied
physical M2 sites. There is no need to switch to that 80-abstract-edge graph
merely to obtain an injective site placement. This note does not claim that
the 76-edge code is locally prepared, or that the extra gauge bits solve the
held common-E problem studied elsewhere.

The runner independently rebuilds the graph and obtains:

- `28` graph vertices and `76` ordered graph edges;
- stream edge indices `72,73,74,75` in the corrected snake-cell order;
- the complete `112`-factor update inventory (`48` coin, `4` seam, `60`
  contact) in `27` collision-free colors;
- physical schedule SHA-256
  `f90bc5256e8c6e16863870c1445029fc793f3e259c7814687e55db6d221e8d22`;
- an exact two-site repetition intertwiner and an active deletion residual of
  `2` when the second physical `X` is removed; and
- zero carrier collisions.

This is a positive bounded placement and execution result on a supplied
chart. It is not an origin-free, order-free, or schedule-free derivation.

## Exact site/qubit resource map

Use the six signed directions

```text
D_0=+x, D_1=-x, D_2=+y, D_3=-y, D_4=+z, D_5=-z.
```

The four cell centers, relative to a supplied origin `O`, are

```text
O+(-8,-8,0), O+(8,-8,0), O+(8,8,0), O+(-8,8,0).
```

They are ordered by the snake

```text
(0,0,0), (1,0,0), (1,1,0), (0,1,0).
```

For a cell center `C`, place the onsite edge qubits at

```text
octahedral edge (a,b):    C + 2(D_a+D_b),  b != reverse(a),
reference spoke a:        C + 4 D_a.
```

For a positive-axis seam owned by `C`, place its repeated stream qubit at

```text
C + 7 D_axis,  C + 9 D_axis.
```

The repetition code is

```text
|0> -> |00>, |1> -> |11>,
logical X = X_7 X_9,
logical Z = Z_7,
Z_7 Z_9 = +1.
```

For the optional edge-gauge extension, place `q_e` at the blank midpoint
`C+8D_axis`. The executable runner prints the edge-index-to-site map for all
76 edges and the four optional gauge sites.

| resource | exact count |
| --- | ---: |
| abstract PatchGraph graph-edge qubits | 76 |
| onsite one-site carriers | 72 |
| repeated stream carriers | 8 |
| literal occupied physical M2 | 80 |
| optional midpoint edge-gauge M2 | 4 |
| optional prepared-graph occupied physical M2 | 84 |
| patch `L_infinity` radius about `O` | 12 |

The `2 x 2` physical carrier is contained in
`[-12,12] x [-12,12] x [-4,4]`. Distinct graph edges never share a site.
The pitch is 16 and the largest onsite offset is four, while the stream pair
sits at offsets seven and nine across the seam.

## Executed two-cell update segment

The runner selects corrected schedule factor `("stream",3,0)`, the upper
horizontal seam. Its two stabilizer-descended Pauli summands have abstract and
physical weights `11` and `7`; their union occupies 14 physical sites. They
commute. For angle `0.37`, the runner executes

```text
U_seam = exp(-i 0.37 P_2/2) exp(-i 0.37 P_1/2)
```

on four independent state vectors in the full `2^14` union Hilbert space.
Each Pauli rotation is compiled by local basis changes, a parity-CNOT ladder,
one `RZ`, and exact uncomputation. The compiled-state residual is below the
runner tolerance. Deleting both load-bearing `RZ` factors produces a nonzero
state residual.

The abstract segment has 54 one-/two-M2 factors. Cycle 655's fixed Manhattan
route-and-return convention expands it to 910 nearest-neighbor factors on
178 touched sites. The longest operand distance is 24. Every routed macro
preserves operand order and returns all intervening wires. Deleting the first
route SWAP is detected by a failed wire-return permutation.

This execution establishes one nontrivial two-cell segment. It does not infer
the exponentially large full-patch unitary matrix, a recurrent update on
overlapping patches, or physical time from the circuit index.

## Cycle-655 controller composition

The same 910-factor routed word is inserted into the landed Cycle-655
one-hot controller grammar. A radius-15 cube contains the data, a 910-site
serpentine program counter, one relay, and two bypass-work factors.

| Cycle-655 resource | exact count |
| --- | ---: |
| fixed cube radius | 15 |
| physical M2 in fixed cube | 29,791 |
| PatchGraph occupied code sites | 80 |
| one-hot clock sites | 910 |
| relay plus bypass work | 3 |
| remaining routing/schedule sites | 28,798 |

The trace selects factors `0,...,909` in order and returns the token. The
imported Toffoli and Fredkin words are exact within tolerance, and deleting
the first clock-shift edge changes the selected word. However, the unmodified
Cycle-655 blank-bypass gadget is not a direct controller for this word. The
Pauli compiler contains basis `H` gates, and `H|0>` is not blank. The runner
obtains bypass action residual `1.0823922002923938` and work leakage `1`.
This is an active incompatibility control, not a missing test.

Thus Cycle 655 supplies the exact routing and selection geometry, but its
blank-fixed opcode domain does not by itself execute this Pauli-basis word.
Its microscopic macro substep schedule also remains supplied. The substep
index is not interpreted as time or a rate. Cycle 656 supplies an abstract
PacketTrace comparator and resource projection below; its literal selector
blueprint remains open.

## Cycle-656 abstract trace and projected resource census

The Cycle-656 `SelectorLaw`, `RailShiftLaw`, `AutoLaw`, and `run_orbit`
objects are instantiated on an abstract `PacketTrace` with 178 data lanes and
one live-token lane. Because 910 is even, no identity padding is needed. The
abstract trace has 910 A stations and 910 B stations. Separately, applying the
Cycle-656 column-width formulas to this larger word projects a square rail of
side 456. The projected custom selector is **not** constructed or executed:
the landed literal primitive iterator is specialized to Cycle 656's original
116-lane/33-program-bit instance and cannot certify this 178-lane instance.
Exact controlled-one-M2 and two-M2 blank-bypass matrices below are opcode
checks, not an executed ROM-match circuit.

| Cycle-656 abstract/projected resource | count |
| --- | ---: |
| packet data/live-token lanes | `178 / 1` |
| program bits per A station | 31 |
| match scratch per A station | 30 |
| selector flag / bypass work per A | `1 / 2` |
| projected A-column / B-column M2 | `243 / 179` |
| projected complete footprint M2 | 384,020 |
| projected NN rail edges per shift layer | 162,890 |
| projected maximum A-column route distance | 242 |

The abstract finite trace selects all 910 factor indices and returns the unique packet to A
station zero. An origin-one token gives the cyclically shifted factor history.
Deleting ROM block 17 omits factor 17. Exact controlled-one-M2 residual,
controlled-one unitarity residual, two-M2 bypass action residual, and two-M2
work leakage are all zero within tolerance. These test the abstract trace and
individual opcode matrices; they do not execute a custom literal selector.

The abstract composition and projected census are conditional: the
packet-lane ordering, square rail orientation, fixed ROM,
selector-before-shift order, station-zero token, vacuum B packets, and clean
selector work are supplied. A collision-free nearest-neighbor layout and
executed ROM-match circuit for the projected 384,020-M2 footprint are open.
The construction does not turn those inputs into framework Records or a
dynamical preparation law.

## Locality, translations, and proper-cubic behavior

The finite locality statements are:

- the literal PatchGraph carrier has `L_infinity` radius 12;
- the selected two-cell Pauli factor has physical support union 14 and a
  maximum routed operand distance 24;
- every routed elementary gate is nearest-neighbor;
- the Cycle-655 selection/bypass audit fits in radius 15; and
- the Cycle-656 abstract rail graph has radius-one shift edges; `242` is only
  the projected A-column route distance, not a certified literal route.

The site rule is covariant as a family. For any lattice translation `t`, use
origin `O+t`. For any proper-cubic frame `R`, transform the cell centers,
direction vectors, repeated seam pair, midpoint gauge sites, and gate-word
coordinates by `R`. The runner checks four translations, all 24 frames, and
all 576 ordered frame products for frame closure, signed-direction action,
carrier and optional-gauge placement, and routed-word diagrams. Every
transformed two-site gate remains nearest-neighbor.

The canonical frozen `2 x 2` site set is not itself invariant under every
proper rotation, because many rotations move its square into another plane.
Nor is it invariant under a unit translation while `O` is held fixed. The
same is true of the selected routed word and the two-rail cassette. What is
covariant is the supplied-origin/supplied-coframe family. A single canonical
off-code word invariant under every translation and proper rotation is not
claimed.

## Held-size and deletion controls

The same formulas are applied without refit to larger open squares.

| square | split | abstract edges | literal physical M2 | plus midpoint gauges |
| ---: | --- | ---: | ---: | ---: |
| 2 | direct | 76 | 80 | 84 |
| 3 | held-no-refit | 174 | 186 | 198 |
| 4 | held-no-refit | 312 | 336 | 360 |

Every row has zero collisions and the expected `2n(n-1)` seams. These are
held placement controls only. They do not claim held common-E target closure
or a size-independent controller footprint.

Active deletions are:

1. delete the second stream-repetition `X`: intertwining residual `2`;
2. delete both two-cell `RZ` factors: nonzero executed-state residual;
3. delete the first route SWAP: wire return fails;
4. delete the first Cycle-655 clock-shift edge: selected order changes;
5. delete Cycle-656 ROM block 17: index 17 is absent from the abstract
   PacketTrace history.

## Does routing need supplied origin, order, or schedule?

Yes, in the constructions executed here. The supplied order and supplied
schedule are load-bearing inputs of these finite controllers.

- A supplied origin chooses the spacing-16 residue class and locates the
  patch or cassette.
- A supplied coframe identifies the six signed directions and transports the
  square, seam ownership, and rotated word.
- The snake cell order and local incident-edge order define the BKSF chart;
  local port-order gauge repairs covariance but does not erase the chart.
- The owner-side logical-Z choice fixes which member of a stream repetition
  pair carries `Z`.
- Cycle-655 routing uses a supplied Manhattan axis order, factor order,
  one-hot program, and microscopic macro schedule.
- Cycle-656 uses a supplied lexicographic lane order, station orientation,
  ROM, selector-before-shift layer order, and station-zero clean genesis.

This is an inventory of the present construction, not a theorem that every
possible compiler must contain those inputs.

## Supplied and derived structure

Supplied:

- patch origin and proper-cubic coframe;
- snake cell order, local incidence order, and repetition logical-Z side;
- the corrected coin/seam/contact factor order and angle `0.37` for the
  executed segment;
- fixed Manhattan axis order and route-and-return convention;
- Cycle-655 one-hot token, program, blank work, and macro substep schedule;
- Cycle-656 coordinate-to-lane order, cassette orientation, fixed ROM,
  selector-before-shift order, station-zero token, clean work, and vacuum
  inactive packets; and
- numerical tolerance and deterministic execution vectors.

Derived and executed on that surface:

- the 76-to-80 injective physical map and optional 84-site extension;
- edge, factor, color, placement, locality, and held-size censuses;
- repetition intertwining and active deletion;
- one two-cell Pauli-rotation segment on `2^14` states;
- the 910-factor nearest-neighbor route-and-return word;
- the Cycle-655 per-opcode selection/bypass incompatibility controls;
- the Cycle-656 abstract PacketTrace, individual opcode controls, projected
  resource census, and ROM/origin deletions; and
- translated, 24-frame, and 576-product covariance diagrams for the carrier,
  optional gauges, and routed-word family.

Not claimed:

- derivation of an origin, coframe, cell/port/lane order, program, schedule,
  coupling, or controller genesis from the minimal axioms;
- constant-depth local preparation or dynamical enforcement of the BKSF,
  repetition, optional gauge, clock, or ROM sectors;
- a literal custom Cycle-656 selector blueprint, collision/NN certificate, or
  execution of the projected 384,020-M2 resource census;
- one overlap-safe recurrent lattice compiler or full-neighborhood update;
- one canonical off-code coordinate word invariant under every translation
  and proper rotation;
- physical time, rate, energy, source, Record, occurrence, or probability
  meaning; or
- a route-independent no-go. There is no route-independent no-go in this
  note.

## No-Go Discipline Gate

**Gate result: FAIL for a broad negative. Demotion:
`partial-attempt-with-named-untested-routes`. Keep the positive bounded
construction and the exact route-specific controls only.**

### N1 — alternative routes

1. **Cycle-232 repeated 76-edge placement — ATTEMPTED.** It closes with 80
   occupied sites and supplies the main construction.
2. **Midpoint-gauge 80-edge placement — ATTEMPTED.** It closes geometrically
   with 84 occupied sites but does not remove chart or controller inputs.
3. **Cycle-655 fixed one-hot controller — ATTEMPTED.** Its selection geometry
   returns the 910-factor word, but the blank-bypass domain rejects the basis
   `H` opcodes with nonzero residual and leakage.
4. **Cycle-656 two-rail law — ATTEMPTED.** It closes the abstract finite
   factor-index PacketTrace and separately checks individual opcode matrices,
   conditional on packet placement, station-zero token, ROM, orientation, and
   clean work. The custom literal selector circuit is unbuilt.
5. **One frozen origin/frame/word as a bare invariant — ATTEMPTED.** Unit
   translations and non-preserving proper frames change the frozen coordinate
   set or word. The supplied transformed family remains exact.
6. **Translation-invariant recurrent overlap-safe local controller and local
   preparation law — UNTESTED AND OPEN.** It is the steelman route below.

The open sixth route forbids a route-independent negative conclusion.

### N2 — wall-independence audit

The initial wall list is grouped into four candidate sub-obligations. Their
mutual independence is not established:

| candidate | exact content | provisional separation question |
| --- | --- | --- |
| `W_chart` | origin, coframe, cell/port chart, repetition-Z side | controller genesis and recurrence |
| `W_order` | Manhattan, factor, lane, ROM, and layer order | coordinate origin and clean inputs |
| `W_genesis` | one token, fixed program, blank/clean work and packets | routing geometry and recurrence proof |
| `W_recurrence` | overlap-safe recurrent tiling conditional on the declared chart/order/genesis | one finite cassette succeeding |

Origin and bare-frame covariance are not double-counted; they are one chart
wall. Factor order, Manhattan order, and selector layer order are one order
wall. Clean work and station-zero placement are one genesis wall. None of
these finite walls proves the recurrence wall.

The required six unordered wall pairs are explicitly inventoried below. The
two directional columns state the missing intervention, not a passed result.

| pair | change first while holding second | change second while holding first |
| --- | --- | --- |
| chart/order | no origin-free chart intervention | no order-free routed word |
| chart/genesis | no chart change with identical prepared token/work | no genesis change on a fixed chart that still closes |
| chart/recurrence | no alternative chart with a recurrent trace | no recurrent trace on the present chart |
| order/genesis | no alternative order at fixed genesis that preserves action | no genesis intervention at fixed order that closes |
| order/recurrence | no order intervention inside a recurrent law | no recurrent law at fixed finite order |
| genesis/recurrence | no genesis intervention inside a recurrent law | no recurrent law at fixed supplied genesis |

Therefore N2 has `6/6` pair rows but `0/12` bidirectional constructive
interventions. It is incomplete. This is sufficient to block a shared-wall
negative, not to prove that the four labels are substrate-independent.

### N3 — hidden-wall scan

The runner/note expose: pitch 16; the signed direction convention; the snake
cell order; local incidence order; positive-bond ownership; repetition
logical-X and logical-Z representatives; optional midpoint gauge placement;
the chosen seam and angle; deterministic localization basis order; color
order; Manhattan axis order; parity-ladder pivot order; coordinate-to-lane
sort; opcode equivalence by exact matrix digest; one-hot token origin; clean
relay/bypass/match work; fixed ROM; selector-before-shift order; and the rule
that circuit indices are not physical time.

### N4 — exact residual matching

| target | executable witness | exact outcome | disposition |
| --- | --- | --- | --- |
| 76-edge literal site injection | Cycle-707 primary runner | `76 -> 80`, zero collision | closed |
| optional midpoint gauges | Cycle-707 primary runner | `4` gauges, `84` total sites, zero collision | closed geometrically |
| corrected full factor inventory | Cycle-707 primary runner | `112` factors, `27` colors | closed |
| one two-cell gate segment | Cycle-707 primary runner | `2^14` execution, `1.0903676167168099e-15` maximum residual | closed |
| nearest-neighbor routing | Cycle-707 primary runner + Cycle-655 core | 910 factors, zero NN/order/return failures | closed |
| Cycle-655 direct blank bypass | Cycle-707 primary runner + Cycle-655 core | basis-`H` residual `1.0823922002923938`, leakage `1`; `RZ` residual nonzero | rejected for this word |
| Cycle-656 abstract trace/opcodes | Cycle-707 primary runner + Cycle-656 core | zero selected-index/order/return failures; opcode residuals below tolerance | abstract closure only |
| transformed-family covariance | Cycle-707 primary runner + Cycle-210 frames | zero diagram failures at 24 frames, 576 products, four translations | closed for supplied family |
| origin/order/schedule derivation | no executable witness | not supplied | open, not a negative theorem |
| recurrent held common-E/preparation | no executable witness | not tested | open |

N4 matches every positive or route-specific failed witness used by this note.
It does not supply a residual for the unexecuted recurrent steelman, so an
N4-complete shared negative is unavailable.

### N5 — resolution and rhetoric audit

The positive state execution is at 14 physical support sites. Routing is
checked factor by factor on 178 touched sites. Controller selection is checked
at 910 steps. Placement is held at `3 x 3` and `4 x 4`. Covariance is
checked at 24/576 frames/products. No observation at one of these resolutions
is promoted to an asymptotic lower bound, minimum-resource result, or global
compiler no-go. Words such as “must” and “cannot” apply only to the declared
finite grammar and exact failed deletion/control.

### N6 — partial-closure path scan

The useful partial closure is substantial: literal edge-to-site placement,
stream repetition, one executed two-cell segment, nearest-neighbor routing,
one rejected blank-bypass controller, one abstract PacketTrace plus projected
resource census, transformed-family covariance, deletions, and held placement
all close at their stated levels. These results remain valid without deciding
the open literal selector and recurrent preparation routes.

### N7 — steelman

An adversary can replace the supplied finite chart/cassette with a
translation-invariant local cellular controller. A bounded local rule could
carry coframe and phase-gauge labels, prepare repetition/gauge constraints,
schedule commuting colors through recurrent local tokens, update overlapping
patches consistently, and return every work field. If it works on growing
held volumes with no distinguished residue class or station-zero genesis, it
would remove or relocate the present chart, order, genesis, and recurrence
walls. The cheapest decisive artifact is an explicit two-neighbor-cell local
rule plus a no-refit `3 x 3 x 3` trace showing preparation, one update,
cleanup, and transformed-family covariance.

This steelman is live. Therefore the broad negative fails.

### N8 — cross-cycle echo

Cycle 232 already named its spacing-16 placement, repetition side, blank
routing, gate schedule, local port-order gauge, and nonlocal state-preparation
boundary. Cycle 655 internalized finite data-program selection but kept the
microscopic controller macro schedule supplied. Cycle 656 internalized the
factor-order trace into a fixed law while keeping packet placement, ROM,
orientation, layer order, and clean station-zero genesis supplied. The present
result does not relabel those same admissions as derivations. It composes them
with the corrected PatchGraph and records exactly what closes.

## Reproduction

Run:

```bash
python3 scripts/frontier_literal_patchgraph_z3_m2_placement_controller_cycle707_2026_07_26.py
```

The expected terminal marker is:

```text
LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_CONTROLLER_CERTIFICATE
```

Authority remains `none`; audit remains `unset`. Only an independent audit
lane may apply a verdict.
