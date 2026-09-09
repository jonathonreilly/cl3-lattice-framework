# Cycle 709 local-seam signed-Clifford physical-M2 compiler

**Date:** 2026-07-26

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Graph-code input:**
[`OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md`](OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md)

**Literal-placement input:**
[`LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md`](LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md)

**Endpoint regression input:**
[`PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md`](PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md)

**Mass/contact regression inputs:**
[`common_matter_field_coin_family_cycle219_2026_07_16.py`](../scripts/common_matter_field_coin_family_cycle219_2026_07_16.py)
and
[`spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py`](../scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py)

**Primary runner:**
[`scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py`](../scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py)

## Result

Cycle 709 replaces Cycle 706's dense free symplectic completion, on a declared
family of supplied-order open rectangular boxes, by a fixed local signed-
Clifford word and then compiles one complete overlapping-star instance to
literal nearest-neighbour M2 gates.

For every seam `e`, four transported Pauli transvections implement the exact
signed seam map.  A fixed six-colour seam schedule followed by a frozen
radius-one cleanup rule

```text
A_ef = 1 iff
  colour(e) < colour(f), lower(e) = upper(f),
  or the same statement with e and f exchanged
```

closes the complete signed tableau on five boxes without refitting.  In words,
the earlier-coloured seam exits the cell shared with the later-coloured seam.
The emitted word does not call the dense tableau constructor.  The runner does
retain that constructor as a verification oracle.

On the primary `3 x 2 x 2` box, the construction places the code and rails on
`276` literal M2 sites, compiles all `80` seam factors and `11` cleanup edges,
and emits a supplied serial Manhattan route-and-return word containing `22,635`
nearest-neighbour gates.  The two overlapping cube views agree on their shared
physical registers and obey

```text
180 + 180 - 84 = 276.
```

This is a positive bounded physical compiler on a supplied canonical
cell/path tuple.  It is not yet the campaign's translation-compatible,
order-gauge-free recurrent law: shuffled cell order changes coarse-face signs,
the full-box 24/576 semantic diagram has not been executed, and the physical
micro-schedule and code genesis remain supplied.

## Exact compiler relation

Let `T_B` be the signed Cycle-706 OpenReference-to-PatchGraph-plus-rail tableau
on a lawful box `B`.  Let `C_B` be the Cycle-709 word consisting of the four
signed seam transvections in the six frozen colour layers followed by the
`H-CZ-H` cleanup on the edges selected by `A_ef`.  Let `E_lit` be the
Cycle-707 repetition/placement isometry, and let `R_B` be the nearest-neighbour
route-and-return realization of `C_B`.

On all ambient Pauli generators of each tested box,

```text
C_B P C_B^dagger = T_B(P).
```

On the declared prepared repetition/code sector of the physical primary box,
the routed word therefore satisfies the code-space intertwiner

```text
E_lit C_B = R_B E_lit,
```

up to the physically irrelevant common state phase checked by the finite state
certificates.  Every route restores the intervening wire permutation.  This
identity is a finite gate/compiler identity, not a time-evolution law.

## Reference-seam factorization

For the supplied `+x` reference seam, `rank(S-I)=3`.  Exhaustive search over
all nonzero transvection axes in `im(S-I)` finds no word of depth one, two, or
three.  The constructed depth-four signed word has

```text
abstract weights   (13, 12, 1, 1)
Pauli phases       ( 0,  0, 0, 1)
rotation signs     ( +,  -, -, +)
```

and zero signed, symplectic, phase-only, or Hermiticity failures.  Deleting a
factor gives generator failures `(13,12,1,14)`.  This is a restricted-axis
depth certificate; it is not a proof that four is globally minimal over all
Pauli axes or over all Clifford syntheses.

Cycle 706's signed order-gauge transport sends the word through all `24`
proper-cubic frames.  The axis-dependent abstract weight families are

```text
x: (13,12,1,1)
y: ( 9, 8,1,1)
z: ( 5, 4,1,1).
```

The direction census is four per signed cubic direction.  All `576` ordered
frame products have zero group, cell-diagram, signed-factor, phase, and
Hermiticity failures.  This is one-seam factor covariance, not yet complete-
box schedule covariance.

## Fixed local cleanup and held boxes

The same six colours, factor template, and `A_ef` predicate are applied without
refit:

| box | qubits | seams | `rank(S-I)` | pre-clean failures | cleanup edges | collinear | max degree | final failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `2 x 2 x 2` | 168 | 12 | 36 | 9 | 6 | 0 | 2 | 0 |
| `3 x 2 x 2` | 256 | 20 | 60 | 16 | 11 | 0 | 2 | 0 |
| `4 x 2 x 2` | 344 | 28 | 84 | 25 | 20 | 4 | 3 | 0 |
| `3 x 3 x 2` | 390 | 33 | 99 | 28 | 20 | 0 | 2 | 0 |
| `3 x 3 x 3` | 594 | 54 | 162 | 48 | 36 | 0 | 2 | 0 |

An independent bond-row oracle reconstructs exactly the same cleanup graph.
The `4 x 2 x 2` box is a discriminator rather than a cosmetic held size: it
contains four collinear cleanup edges.  Deleting any one gives two generator
failures, while an orthogonal-only cleanup leaves eight exact and symplectic
failures.  All five cleanup graphs are bipartite and need two or three abstract
edge layers.  Same-colour abstract factor collisions are zero.

The primary compiler has an explicit exact inverse.  All eight colour-parity
translation residues close exactly when the supplied colour origin is carried
with the chart.

## Literal physical resources

The reference seam uses `39` literal M2 sites.  Its abstract and physical
factor weights are `(13,12,1,1)` and `(14,13,1,1)`.  The compiler uses `74`
primitive H/S/CNOT gates and expands to `1,558` nearest-neighbour gates,
including `1,484` route SWAPs.  Maximum operand distance is `24`.  The maximum
compiled-state residual up to global phase is
`1.5899293649329254e-15`.

Every primitive class is deletion-sensitive.  The deletion residuals for
`basis_H`, `basis_S`, `basis_Sdg`, `parity_CNOT`, `phase_S`, and `phase_Sdg`
are respectively approximately

```text
1.13224, 0.76537, 0.76521, 0.99049, 0.999995, 1.00678.
```

Deleting the first route SWAP is detected in all `50` routed macros that use
one.  One occupied spectator is traversed and returned.  Nearest-neighbour,
operand-order, route-return, placement, and repetition-stabilizer failures are
zero.  The local gate inverse residual is below `3.2e-16`, and the compiled
`H-CNOT-H` versus CZ residual is below `4.5e-16`.

The same physical compiler closes all three positive seam axes:

| axis | physical weights | primitive gates | routed gates | state residual |
| --- | --- | ---: | ---: | ---: |
| `x` | `(14,13,1,1)` | 74 | 1,558 | `1.59e-15` |
| `y` | `(10,9,1,1)` | 58 | 1,062 | `1.61e-15` |
| `z` | `(6,5,1,1)` | 42 | 566 | `1.63e-15` |

The complete primary `3 x 2 x 2` word contains:

| resource | exact count |
| --- | ---: |
| cells / seams | `12 / 20` |
| abstract graph/rail qubits | 256 |
| literal code/rail M2 | 276 |
| physical seam-factor rows | 80 |
| primitive gates | 1,265 |
| routed nearest-neighbour gates | 22,635 |
| route SWAPs | 21,370 |
| cleanup edge layers | 2 |
| maximum route distance | 24 |

All 723 routed macros with a first SWAP detect its deletion.  All 36 Cycle-708
endpoint rows regress exactly.  The two cube views have zero shared-address,
view-to-primary, or union failures.

The literal placement count obeys

```text
M2(B) = 18 N_cells + 3 N_seams <= 27 N_cells
```

on all five boxes, with zero collisions and no refit.  This proves constant
site overhead for this open rectangular family.  It does not prove constant
circuit depth: the current serial route word grows with the supplied box.

## Order, covariance, and schedule boundary

The reference route geometry is transported through `24` proper-cubic frames,
all `576` frame products, and eight translation residues with zero
nearest-neighbour or site-diagram failures.  The supplied coframe acts by
transporting the chart word; a single textual coordinate word is not claimed
invariant.

The full-box semantic statement is narrower.  The compiler currently accepts
translated rectangular boxes only in a supplied canonical product cell/path
order.  Across twelve shuffled orders, the logical one-site, D, bond-to-rail,
and triangle sectors remain exact.  The coarse-face exact/phase/code failure
census is `(2,2,0,2,2,2,2,4,2,2,0,4)`, for `24` code-sector phase failures in
total and zero symplectic failures.  The full-generator mismatch census is
`(54,6,55,52,57,56,57,68,51,28,28,54)`, while the geometric cleanup-edge set
does not change.  The canonical guard therefore rejects a real signed
semantic mismatch, not merely an input-format difference.  Only one of 24
rotated raw cell tuples obeys that guard without first transporting the
supplied order/coframe.

Consequently, Cycle 709 does not satisfy the campaign's no-preferred-order
contract.  A local carried order gauge, a quotient that makes the face signs
unobservable, or an order-free sign repair remains a constructive target.

The physical word uses a supplied serial x-y-z Manhattan micro-schedule.  It
returns all traversed wires, but it does not yet supply a collision-safe
constant-depth parallel schedule, a translation-invariant autonomous
controller, or controller genesis.  No schedule counter or circuit ordinal is
called physical time.

## Supplied, derived, and open structure

Supplied:

- a translated rectangular open box in canonical product cell/path order;
- chart origin, proper-cubic coframe, colour origin, and fixed lexicographic
  six-layer order;
- the Cycle-706 OpenReference `+1` loop/D/bond source sector, natural
  PatchGraph edge map, one rail per seam, and four-factor reference template;
- prepared Cycle-707 repetition, PatchGraph, and rail sectors;
- the radius-one predicate `A_ef` and signed factor convention;
- a serial support order, x-y-z Manhattan route convention, blank route work,
  and deterministic numeric tolerances.

Derived and executed on the declared surface:

- the exact four-transvection signed seam word and active deletions;
- signed one-seam 24/576 transport;
- the six-colour plus local-cleanup compiler on five no-refit boxes;
- collinear-edge, colour-layer, cleanup-edge, rotation-sign, inverse,
  translation, and unlawful-domain controls;
- literal M2 placement with `18N+3M <= 27N` site overhead;
- explicit H/S/CNOT/SWAP realization on all three seam axes;
- the complete supplied-order `3 x 2 x 2` routed word and overlapping-cube
  register consistency; and
- primary-runner re-execution of the Cycle-219 one-particle mass fixture and
  Cycle-230 vacuum/one-particle and double-occupation contact controls, plus
  preservation of the Cycle-708 endpoint regression terminal.

Removed from the emitted compiler word, but not from verification:

- the host-sized lexicographic seam sweep;
- the global free-zero symplectic completion;
- the cube 30-row deletion choice on the code-space path; and
- a held-size fitted cleanup table.

Open and not claimed:

- an order-free or locally gauged full-box sign convention;
- complete-box 24/576 semantic covariance;
- collision-safe constant-depth physical routing and an autonomous recurrent
  controller;
- local genesis and enforcement of the OpenReference, PatchGraph, repetition,
  rail, coframe, colour-origin, controller-token, and route-work sectors;
- periodic/Wilson sectors, irregular or holed domains, and an all-volume proof;
- a physical predecessor/interval bank or Cycle-612 matter-caused endpoint
  bridge;
- occurrence/admission, Record permanence, Born/history actualization,
  source/gravity response, or an empirical prediction; and
- a route-independent no-go, minimum-resource theorem, shared obstruction, or
  axiom pressure.

## No-Go Discipline Gate

**Gate result: FAIL for a broad negative.  Disposition:
`partial-attempt-with-named-untested-routes`.  Retain the positive bounded
compiler theorem and exact shuffled-order falsifier only.**

### N1 — normalized approach families

| family | object / mechanism / terminal obligation | status |
| --- | --- | --- |
| global signed tableau | full symplectic completion; finite semantic equivalence | attempted; finite oracle succeeds in Cycle 706 |
| local seam plus cleanup | signed transvections; six colours and `A_ef`; local physical realization | attempted; succeeds boundedly here |
| direct local bond elimination | stabilizer Gaussian elimination; graph-local pivot rule; order-free all-volume proof | untested |
| direct PatchGraph preparation/update | bypass OpenReference conjugation; prepare and update target code directly | untested |
| direct physical OpenReference | keep source bonds on literal M2; avoid rail elimination | untested |
| local order-gauge carrier | finite gauge state transports face signs; full-box 24/576 closure | untested |
| larger plaquette/face gauge | non-diagonal face constraints repair the shuffled-order cocycle | untested beyond narrower Cycle-705 ansatz |
| autonomous cellular controller | bounded colouring/routing/genesis rule; recurrent all-volume trace | untested |

These are distinct in primary object, mechanism, and terminal obligation.  The
live routes make any route-independent negative premature.

### N2 — collapsed obligation audit

The candidate obligations are:

- `W_A`: all-volume identity on the declared open-box family;
- `W_C`: order/coframe handling and complete-box covariance;
- `W_P`: collision-safe parallel nearest-neighbour execution;
- `W_G`: code, rail, gauge, work, and controller genesis/enforcement;
- `W_R`: autonomous repeated scheduling and cleanup; and
- `W_T`: periodic/Wilson and non-box topology.

The downstream phrase “end-to-end compiler” is not counted as a seventh wall.
For all 15 unordered pairs, closing either member does not logically close the
other on current evidence:

```text
A/C A/P A/G A/R A/T C/P C/G C/R C/T P/G P/R P/T G/R G/T R/T
= no/no in both directions.
```

This is a dependency classification, not a theorem that the physical
substrate makes the obligations independent.

### N3 — hidden-input scan

The supplied inventory exposes every use of “canonical” and “by
construction”: canonical means a supplied product tuple, not an intrinsic
global order; construction means the deterministic finite compiler, not an
autonomous law.  The positive source characters, chart, origin, coframe,
colour origin, six-layer order, factor signs, cleanup predicate, repetition-Z
side, rail characters, route axis/support order, blank work, and verification
oracle are explicit.  No “standard QFT,” background fermionization, physical
clock, or host parity service is imported silently.

### N4 — exact residual matching

| witness | witness residual | Cycle-709 residual | match? |
| --- | --- | --- | --- |
| Cycle 706, lines 85-92 | bounded local Clifford, all-volume family, literal placement, rail genesis open | local signed Clifford plus bounded literal execution | yes for locality/placement; genesis remains open |
| Cycle 707, lines 145-147 | one segment does not imply overlapping recurrent update | complete overlapping `3 x 2 x 2` supplied-order word | partial; recurrence still open |
| Cycle 707, lines 167-177 | blank-bypass controller incompatible with H basis and schedule supplied | autonomous controller/genesis | yes; not closed here |
| Cycle 708, lines 81-83 | dense tableau not physically executed | local signed tableau compiler | exact match; advanced here |
| Cycle 708, lines 101-112 | deletion/coframe basis gauge | order/coframe full-box signs | related but not identical; not counted as closure |
| Cycle 708, lines 148-164 | FSWAP static endpoint fails outside opcode domain | local tableau compiler | no; dropped as a witness for this wall |

The current shuffled-order residual is the measured `24` coarse-face phase
failures.  It is not identified with the earlier endpoint-domain residual or
with source/gravity, time, Record, or Born gaps.

### N5 — resolution and rhetoric audit

The tested resolutions are one seam, five canonical finite boxes, one complete
literal `3 x 2 x 2` routed word, one finite inverse, eight parity translations,
and one-seam 24/576 transport.  Arbitrary box size, irregular domains,
arbitrary cell orders, full-box frame diagrams, periodic topology, autonomous
genesis, parallel recurrence, and prediction bridges are untested.

Therefore “order-independent compiler fails” is too broad.  The retained
negative is only: twelve tested shuffles of the current canonical-product word
produce 24 coarse-face phase failures.  “Four is minimum” is narrowed to the
explicit `im(S-I)` depth-three search.

### N6 — partial-closure paths and primitive boundary

The lattice supplies three-dimensional integer-lattice nearest-neighbour
adjacency and M2 sites; using them is not a new axiom.  Cycle 709 retires the
finite local-circuit and literal-
routing imports without deriving their autonomous selection as the physical
law.  Plaquette redundancy, carried finite order gauge, direct target-code
preparation, and cellular controller construction are all import-retirement
paths under the existing substrate.  Nothing here requires a new axiom.

The Record and realized-state primitives do not prepare the code, select the
cell order, generate the controller, or turn a copied rail/pointer into a
Record or a Born event.  Cycle 709 makes none of those identifications.

### N7 — steelman against a broad negative

A hostile constructive reviewer can plausibly close the remaining compiler
contract without changing the axioms: carry the coarse-face sign as a bounded
local gauge attached to each oriented cell, update that gauge with the same
endpoint-incidence cocycle that transports the four seam factors, edge-colour
the bounded-degree cleanup graph, and replace serial Manhattan routing by a
fixed returned-spectator routing tile.  Compose the tile with a local
preparation/check cycle for the repetition and rail sectors.  The decisive
artifact is an order-free graph-generated word that never invokes the global
tableau oracle, closes complete-box 24/576 diagrams, and repeats
prepare-update-cleanup on growing boxes with all work returned.  This mechanism
and terminal test are concrete and unclosed, so the broad no-go fails.

### N8 — cross-cycle echo

Cycle 703's finite fitted-sign problem was bypassed by changing to a local-
Gauss/stabilizer representation.  Cycle 706's 1,296-choice natural relabeling
failed, but the signed tableau route succeeded.  Cycle 707's one-segment
physical realization was extended here to a complete overlapping-box word.
Cycle 708's dense-tableau locality wall is partially retired here while its
genesis and endpoint-bank walls remain.  Within Cycle 709, the initial
orthogonal-only cleanup was repaired by the `4 x 2 x 2` collinear control.

These are direct examples of similar finite walls being retired by a new
representation or sharper local gauge.  They forbid promoting the current
order residual to constitutional evidence.

## TOE dependency effect

Cycle 709 materially narrows `C_local`: bounded support, constant site
overhead, overlapping register consistency, and an explicit complete finite
nearest-neighbour word are no longer generic mysteries on the supplied-order
open-box domain.  The remaining `C_local` content is order-gauge/full-box
covariance, parallel recurrence, and autonomous genesis/enforcement.

`C_ref` is unchanged but sharpened to the listed source characters, chart,
coframe, colour origin, rail/repetition sector, and controller/work genesis.
`C_num` is unchanged: this Clifford map does not derive a physical number
reference or superselection law.  `C_wrap` is unchanged: gate indices and
colour layers are not time.  `C_int` is regression-preserved but not advanced.
`C_source` is unchanged.

This is an implementation/import-retirement result, not shared substrate
obstruction or axiom pressure.

## Reproduction

Run:

```bash
python3 -u scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py
```

Expected terminal:

```text
SUMMARY_JSON ... "pass": 22, "fail": 0 ...
CYCLE709_LOCAL_SEAM_PHYSICAL_M2_BOUNDED_COMPILER_PASS
```

Authority remains `none`; audit remains `unset`.  Only the independent audit
lane may apply a verdict.
