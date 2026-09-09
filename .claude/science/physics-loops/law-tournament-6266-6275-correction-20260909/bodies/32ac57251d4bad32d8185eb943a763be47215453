# Cycle 712 joint two-cell full-update physical-M2 compiler

**Date:** 2026-07-26

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Direct compiler inputs:**
[`LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md`](LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md)
and
[`FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md`](FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md)

**Primary runner:**
[`scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py`](../scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py)

**Independent checker:**
[`scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py`](../scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py)

**Receipt:**
[`outputs/joint_two_cell_full_update_physical_m2_compiler_cycle712_receipt_2026_07_26.json`](../outputs/joint_two_cell_full_update_physical_m2_compiler_cycle712_receipt_2026_07_26.json)

**Canonical runner cache:**
[`logs/runner-cache/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.txt`](../logs/runner-cache/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.txt)

## Result

On one adjacent two-cell block, the landed OpenReference/PatchGraph-plus-rail
grammar admits a direct joint state isometry and a literal physical word for
the complete supplied Cycle-230 free, reverse-stream, internal-seam, and
onsite-contact update.  With 12 matter modes, 38 abstract edge/rail qubits,
26 independent auxiliary stabilizers, and one literal repetition site,

```text
E = Rep U_target (I_4096 tensor |0>^26)
G_physical = E G_coarse E^dagger                 on Im(E)
E G_coarse = G_physical E.
```

The stabilizer rank is 26, so the code dimension is exactly
`2^(38-26) = 4096 = M64 tensor M64`.  The literal carrier has 39 assigned M2
sites.  The graph count generalizes algebraically to a connected finite cell
domain with `C` cells and `B` internal bonds as

```text
n = 18 C + 2 B,   s = 12 C + 2 B,   k = n-s = 6 C.
```

Thus the landed rail completion has zero logical-dimension deficit.  This
does not mean that the previous Cycle-655 seven-live-mode block can simply be
tensored cellwise: it retains one independent live seam-port bit per cell.
For two cells that naive construction has 14 live bits instead of 12 and a
dimension ratio of four.  The direct global PatchGraph encoder removes that
semantic overcount rather than hiding it in a fixed rail.

## Combined update certificate

The decoded fixed program contains 67 gates:

| factor | count |
| --- | ---: |
| coin Givens rotations | 20 |
| coin phases | 2 |
| reverse adjacent FSWAPs | 6 |
| one internal seam as adjacent FSWAPs | 9 |
| onsite contact phases | 30 |

The dense vacuum/one/two-particle comparator has dimension 79 and gives

```text
|| E G_coarse - G_physical E || = 6.251918067842639e-15
decoded unitarity residual       = 8.421015252503785e-15
encoded number commutator        = 0
one-particle mass residual       = 5.551115123125783e-17.
```

The full 4096-column domain is certified factorwise rather than by storing a
dense `4096 x 4096` comparator.  Every free primitive agrees with the second
quantization of its one-particle restriction to
`8.673527957121405e-19`; the contact product agrees on all 4096 occupation
basis states to `2.2256874016713148e-15`; and 33 active columns spanning all
13 number sectors have maximum residual `2.526252967680787e-15`.  The compiled
one-particle residual is `1.7920088139491047e-15`.  These checks use the exact
homomorphism of second quantization and the diagonal occupied-pair form of the
supplied contact.  They are a sector-complete algebraic certificate, not a
misreported dense full-matrix calculation.

The Cycle-230 comparison is independent at the declared boundary: coin
residual `1.952777839357751e-16`, mass residual zero, FSWAP residual zero,
64-state onsite-contact residual `2.149937642474629e-15`, and internal
depth-two stream residual zero.

An independently written checker reconstructs a fresh lexicographic BFS
tree, its 24 fundamental cycles, the signed-tableau code columns, and the
coarse update through a creator-wedge calculation.  Its fundamental-cycle
space has rank 24 and union rank 24 with the landed shared-cycle rows; the
literal 39-site constraint rank is 27, while the complete commuting physical
W basis has rank 39.  Exhaustive comparison of all 4096 decoded-update
columns gives maximum residual `5.566705740848049e-16`, norm residual
`9.992007221626409e-16`, zero number leakage, zero contact residual, and zero
lawful-seam residual.  Its update digest is
`c2778e0cda9eefd0a417724c702fbf704a2b38af5ae58dffd312301f7f6aa612`.
This independently checks the full decoded update and the physical code
tableau; it does not expand the 39-M2 encoded amplitudes.  It is not a
restatement of the primary factor proof.

## Literal M2 execution

The primary direct-target word has:

- 1,375 primitive gates and 17,709 routed nearest-neighbour gates;
- maximum route distance 24;
- 39 assigned code/repetition M2 and 458 blank route-work M2 touched;
- zero non-nearest-neighbour, operand-order, and route-return failures; and
- routed digest
  `81acd5209a78ae4afca4af9dcb9c399d8410c0657ca03d6431faa44e8f3eead8`.

An alternative word using the Cycle-709 source encoder flanked by the exact
signed seam-chart bridge also closes: 1,535 primitives, 20,837 routed gates,
maximum route distance 24, zero routing failures, and digest
`90a53c77a2cbc0908f23efaad8665e1b16e97b9a264226c1dd96fba3b32678bb`.
The extra blank route-work sites are a disclosed serial-routing resource; no
asymptotic constant-overhead or collision-free parallel-controller theorem is
claimed here.

The target decoder sends the 24 shared-cycle, one local-D, and one rail
stabilizers to untouched auxiliary Z wires.  Re-encoding restores them and
the outer repetition CNOT restores the literal pair.  Cycle, D, and rail row
deletions each double the code dimension; deleting the repetition encode
leaves a nonzero stabilizer mismatch.  Update deletions are also active:

| deletion | residual / failure |
| --- | ---: |
| coin phase | `0.023595018644519728` |
| coin Givens | `3.5899334801224168` |
| reverse FSWAP | `6.928203230275511` |
| seam FSWAP | `6.928203230275508` |
| contact | `0.3678930670560826` |
| first decode gate | 6 tableau failures |

## Seam falsifier and held domain

A single nonadjacent two-wire tensor FSWAP is not the CAR seam: its residual
is `5.656854249492381`.  The mismatch is isolated to the seam stage.  The
nine-adjacent-FSWAP word has zero seam-stage residual.  The independent
all-column checker finds the same shortcut wrong on 1,024 of 4,096 columns,
with maximum column residual 2.  This is a useful
falsification of a tempting shortcut, not a no-go for local seam compilation.

Without refitting the graph-basis synthesizer, six-mode coin/reverse/contact
compiler, or adjacent-CAR seam template, the held three-cell chain with two
overlapping internal seams gives:

- 18 modes, 58 abstract qubits, stabilizer rank 40, and code dimension
  `262144 = M64^3`;
- 60 literal M2, 2,115 primitives, and 38,651 routed gates;
- combined `N<=2` residual `9.46085985276513e-15`;
- sector-complete free/contact residual at most
  `3.4056894305085554e-15`;
- maximum route distance 40; and
- zero placement, routing, operand-order, or route-return failures.

This held result establishes compositional reuse across two overlapping
seams.  Two finite sizes do not prove an autonomous recurrent infinite-lattice
law.

## Proper-cubic charts

All 24 native chart encoders synthesize with zero tableau or dimension
failure, using 635--688 gates.  The decoded free update is covariant in all 24
frames; contact permutations have zero failures.  All 576 ordered frame-pair
mode compositions, W/V chart transforms, and W/V chart compositions are
exact, as are the landed Cycle-706 and Cycle-709 chart/seam product checks.

This is common-chart naturality.  Literal routed physical words for every
transported chart and independently stored neighboring coframes with a
coherent relation register remain open.  Cycle 711's passive chart erasure
does not by itself construct that active interface.

## Supplied, derived, and open inventory

Supplied:

- the connected `+x` two-cell geometry and semantic cell/mode order;
- Cycle-706 signed W/V bases and its rail-Z reference completion;
- Cycle-707 placement, stream repetition sector, and serial Manhattan router;
- the Cycle-709 four signed seam-chart factors;
- the Cycle-230/Cycle-655 `beta=-0.3` coin, reverse layer, `+x` seam
  attachment, `g=0.37` contact, and factor order;
- the `+1` stabilizer, rail, and repetition sectors; and
- blank route work and the offline serial program order.

Derived and executed:

- a rank-38 Clifford state encoder for 12 logical occupations plus 26 fixed
  auxiliaries;
- exact equivalence of direct target encoding and the source encoder followed
  by the landed Cycle-709 chart bridge;
- the literal decode/free/seam/contact/re-encode physical word;
- the 79-column dense comparator and sector-complete 4096-column certificate;
- an independent BFS/tableau/creator-wedge exhaustive 4096-column checker;
- a no-refit held three-cell/two-seam compiler;
- all 24 native encoders and all 576 exact chart compositions; and
- stabilizer, leakage, routing, deletion, mass, contact, and seam controls.

Open and not claimed:

- autonomous physical preparation or local enforcement of the stabilizer,
  rail, repetition, and blank-work sectors;
- a collision-free autonomous recurrent controller and its genesis;
- exterior-boundary stream closure beyond the tested internal bonds;
- independently active neighboring coframes and their relation-tag controller;
- literal routed words for all transported charts;
- asymptotic constant route-work overhead; and
- physical time/rate, source/gravity, Record, Born/probability,
  realized-history, prediction, minimum-content, or axiom consequences.

The serial circuit ordinal is a supplied program schedule.  It is not called
time, and no static constraint is called physical energy.

## No-Go Discipline gate

No negative theorem ships.  N1--N8 gives:

- **N1 routes:** direct global PatchGraph encoding succeeds; source-chart
  bridging succeeds; punctured-local, borrow/uncompute, explicit port-copy,
  sparse scheduler, and owned-interface routes remain live.
- **N2 wall independence:** the state-isometry wall is closed on the declared
  two- and three-cell domains and is removed from the remaining set.  External
  streams, active coframes, scheduler recurrence, code genesis, and physical
  time are distinct remaining obligations.
- **N3 hidden inputs:** geometry, mode order, signed bases, rails, stabilizer
  eigenvalues, contact/coin constants, factor order, routing, and blank work
  are inventoried above.
- **N4 residual matching:** the `5.65685` falsifier diagnoses omitted CAR
  parity in one shortcut; it is not an end-to-end substrate residual.
- **N5 resolution:** two and three open chains are tested; periodic, holed,
  branched, and large many-star domains are not exhausted.
- **N6 partial closures:** the direct joint isometry, internal seam, contact,
  held overlap, and chart naturality are strict constructive closures.
- **N7 steelman:** stream the same bounded factors over a larger prepared graph
  and internalize the supplied program order with sparse local control.
- **N8 cross-cycle echo:** Cycle-655's live-port overcount and Cycle-711's
  schedule/coframe walls are separated rather than promoted to one obstruction.

Therefore the result supplies no minimum-content, impossibility,
shared-obstruction, or axiom-pressure claim.

## TOE dependency effect

`C_local` narrows materially: an actual joint state isometry and complete
free-plus-internal-seam-plus-contact physical update now close on two cells and
a held three-cell/two-seam domain.  `C_int` narrows at the bounded compiler
interface because the supplied mass and contact fixtures survive the same
joint `E`; selection, rate, protection, and source causation remain open.
`C_ref` is unchanged beyond the Cycle-711 passive-chart result.  `C_num`
retains named stabilizer/rail sector supplies but has no dimension deficit.
`C_wrap` retains the offline serial program order and is not reclassified as
time.  `C_source` is unchanged.

## Prior-art and novelty boundary

Graph-state/stabilizer encoders, Clifford synthesis, second quantization,
Givens decompositions, fermionic swaps, and nearest-neighbour routing are
standard finite methods.  No global priority claim is made.  The new bounded
result is their exact executable composition for this repository's specific
M64 intrinsic-CAR cell and landed PatchGraph/rail grammar, including a shared
internal seam, onsite contact, held overlapping seam, literal M2 routing, and
proper-cubic chart audit in one state-isometry certificate.

## Reproduction

```bash
PYTHONPATH=scripts python3 -u \
  scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py
```

Expected terminal:

```text
CYCLE712_TWO_CELL_JOINT_E_FREE_SEAM_CONTACT_PHYSICAL_M2_PASS
```

Authority remains `none`; audit remains `unset`.  Only the independent audit
lane may set an audit verdict or effective status.
