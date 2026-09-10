---
claim_id: admissibility_d4_record_flag_collision_safe_controller_boundary_bounded_theorem_note_2026-08-29
claim_type: bounded_theorem
claim_scope: "For the frozen Block-12 outcome-typed five-cell relay, test an oracle-free finite controller whose eligibility stage reads only nearby permanent-Record flags and whose post-formation stage reads only the five destination Record flags. The all-or-none guard is exactly collision-safe in all 37,632 six-front, predecessor, outcome, and obstacle cases, including a normalized STOP branch. However, two collinear untyped Record flags select both ends of every tested finite unmarked straight trail, so they do not orient the history arrow. The result is CONDITIONAL-HALO: static single-tip obstacle safety is constructed, while an orientation-bearing Record readout or other asymmetric local datum, microscopic control, interacting-front arbitration, occurrence rate, time, gravity, axiom amendment, audit retention, obligation retirement, and TOE movement remain open."
parent_commit: 1a42db99a3f8a388625ebc620ade12dac8caf4dd
block12_result_commit: 4db65374c6b04b52045fc46e4b312864dc9c5f08
preregistration_commit: 8d08827b404628b3444d40226894aa8b3f5e2c89
origin_main: 3cc632921c36aa90266c5c62e56816577ce59a0a
minimal_axioms_blob: bc23300becfe4e4db57153c0e94cfcdf2338da71
verdict: CONDITIONAL-HALO
static_obstacle_controller: true
flag_only_finite_line_arrow: false
microscopic_controller: false
interacting_fronts: false
formation_rate: false
gravity: false
axiom_amendment: false
obligation_retirement: 0
toe_percentage_movement: 0
---

# Record-Flag Collision-Safe Controller Boundary

**Date:** 2026-08-29

**Campaign block:** Source/Eta 13

**Type:** `bounded_theorem`

**Standing:** author-side bounded result; independent replication and audit
retention are separate gates

Primary runner:
[`admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py`](../scripts/admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py).

Independent checker:
[`independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py`](../scripts/independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py).

Frozen parent result:
[`ADMISSIBILITY_D4_OUTCOME_TYPED_GENERATED_FRONT_PREFIX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md`](ADMISSIBILITY_D4_OUTCOME_TYPED_GENERATED_FRONT_PREFIX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md).

Frozen framework boundary:
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

No-Go Discipline packet:
[`NO_GO_DISCIPLINE_CHECKLIST.md`](../.claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/NO_GO_DISCIPLINE_CHECKLIST.md).

## 1. Result up front

The registered terminal is **`CONDITIONAL-HALO`**.

The positive result is exact: the **all-or-none controller is collision-safe**
for the frozen five-cell Block-12 relay.  Once one formation site and its
forward direction have been identified, the controller inspects the five
Record flags at the proposed destinations.  If all five are clear, it performs
all five nearest-neighbor SWAPs.  If any one is occupied by a permanent Record,
it performs none of them.  Thus it never moves an existing Record, never moves
only part of the packet, never clones a source, and never grows the packet.
The blocked event terminates with a STOP branch carrying the entire normalized
outcome mass.

The negative result is equally exact and deliberately narrow: **flag-only geometry selects both ends** of a finite unmarked straight Record trail.  Two
collinear predecessor flags distinguish the line axis and reject every lateral
candidate, but they do not distinguish past-to-future from future-to-past.  A
finite line has one eligible candidate beyond each endpoint.  Therefore this
flag-only rule cannot autonomously choose the history arrow.

This is not a no-go for local orientation.  The Block-12 Record contents encode
the signed front, and the framework already permits Record readout determined
by content.  **Record content readout remains the shortest orientation escape**
at the effective framework level.  What remains open is whether that readout
has a satisfactory microscopic quantum realization, since the 84 displayed
one-qubit density operators are full-rank and nonorthogonal.

Accounting is unchanged: **obligation retirement: 0** and **TOE percentage movement: 0**.  No axiom amendment is proposed.

## 2. Frozen typed local state

Each lattice site has two logically distinct fields:

1. a permanent Record flag `R(z)` in `{0,1}`;
2. an `M2(C)` content `c(z)`.

The Record flag is what the collision guard uses.  Its action is independent
of the quantum content at a destination.  This preserves the axiom-level
distinction between the fact that a Record exists and what its locked content
means.  The 84-state Block-12 code, rank-nine hybrid carrier, and normalized
fourteen-outcome source law are not changed.

The runtime is not handed a target name, site ID, role, epoch, global clock,
predecessor outcome, future outcome, host front, or codebook.  The realized
outcome appears only after the probability distribution has been formed.

## 3. The flag-only eligibility rule

For a no-Record candidate site `x`, the registered rule searches the six
nearest directions.  It accepts only if there is exactly one nearest Record,
at `x-f`, and a second collinear Record at `x-2f`.  The other five nearest
neighbors must have no Record.  If accepted, it infers the proposed front `f`
from the displacement of the unique nearest predecessor.

This rule is useful.  Exact enumeration over all six signed coordinate axes
and trail lengths two through nine shows that no lateral branch is eligible.
It therefore identifies the axis and excludes side growth without reading
Record content.

But it cannot orient that axis.  For a finite trail

```text
0, f, 2f, ..., (L-1)f,
```

the candidate `Lf` sees predecessors `(L-1)f,(L-2)f` and infers `+f`, while
the candidate `-f` sees predecessors `0,f` and infers `-f`.  Both candidates
satisfy exactly the same local flag predicate.  The primary enumeration checks
48 front/length combinations and finds exactly two eligible endpoints in every
one.  This is a reflection-symmetry ambiguity, not a numerical failure.

The conclusion is only:

> An unmarked finite straight line of identical Record flags does not itself
> carry a directed arrow.

It does not say that Record contents, a seed cap, a formation-order tag, a
larger block, or another permitted local asymmetric datum cannot carry one.

## 4. Collision-safe all-or-none transport

After a Record forms at `x`, the frozen Block-12 relay proposes five edges:

```text
x+f       -> x+2f
x+e1      -> x+f+e1
x-e1      -> x+f-e1
x+e2      -> x+f+e2
x-e2      -> x+f-e2
```

where `e1,e2` span the coordinate plane perpendicular to `f`.  These edges are
pairwise disjoint and nearest-neighbor for all six fronts.  Let

```text
C = product over the five destinations of (1 - R(destination)).
```

If `C=1`, all five SWAPs execute.  If `C=0`, the identity executes on all ten
source/destination cells.  This is a finite local guard over Record flags; it
does not decode destination quantum contents and it does not depend on which
of the fourteen outcomes was realized.

The primary runner exhausts

```text
6 fronts x 14 predecessor labels x 14 outcomes x 32 obstacle patterns
= 37,632 cases.
```

The single clear pattern contributes 1,176 exact successor cases.  All five
source contents move to the correct successor shell and the arbitrary prior
destination contents move backward.  The other 31 patterns contribute 36,456
blocked cases.  Every source and destination content is unchanged, every
occupied Record remains fixed, and no partial packet is emitted.  Packet size
stays five and growth is zero.

This closes the specific radius-two collision flaw found in Block 12 for one
already selected active tip.  It does not resolve two simultaneously eligible
or overlapping fronts; those require a compatible distributed arbitration or
a proof that the local instruments commute on every overlap.

## 5. Probability at a blocked site

Formation first computes the unchanged fourteen-way Block-09 distribution.
The collision guard is independent of the outcome.  Consequently the event
can be represented as

```text
clear:   P(continue with outcome b) = P(b)
blocked: P(STOP with terminal label b) = P(b).
```

In either case the total mass is one.  The runner checks 2,688 combinations of
front, predecessor label, and obstacle pattern.  No same-event outcome feeds
back into its own probability and no probability disappears when a collision
is encountered.

STOP here means only that this effective front does not advance through the
occupied layer.  It is not a derived lifetime distribution, physical decay
rate, or global absorbing state.

## 6. Why the result remains conditional

The controller has solved a real subproblem: safe behavior in an occupied
static background no longer needs an unbounded empty corridor.  The result is
still not an autonomous history law because the flag-only eligibility rule
offers two reflected tips on a finite trail.  Choosing one of them externally
would simply reintroduce a scheduler oracle.

At framework level the narrowest repair is to read the signed front already
encoded in the newest Record content.  That is consistent with the current
Record axiom, which makes readout content-determined, and does not by itself
require an axiom update.  It must be registered and tested as a changed target
rather than silently imported into this flag-only block.

At microscopic level, exact dictionary inversion of nonorthogonal one-qubit
states is not an ordinary perfect POVM.  Plausible routes include an orthogonal
pointer extension, a coarser direction-only pointer, an asymmetric seed/cap,
or explicit formation-order memory.  The next experiment must separate the
effective Record-semantic question from the microscopic measurement question.

## 7. Exact claim boundary

Established author-side:

1. the unchanged 84-state code and fourteen-way source law;
2. a geometry-only predicate that selects the line axis and rejects lateral
   branches;
3. an exact two-endpoint counterexample to flag-only arrow orientation on all
   registered finite trails;
4. a five-destination all-or-none Record guard;
5. exact continuation in all 1,176 clear cases;
6. exact identity and Record permanence in all 36,456 blocked cases;
7. normalized continuation-or-STOP mass in all 2,688 guard distributions.

Not established:

1. a flag-only directed tip on an unmarked finite line;
2. a microscopic perfect readout or controller;
3. compatible simultaneous or overlapping-front dynamics;
4. site selection from a general lattice state, a formation hazard, physical
   rate, or clock;
5. seed production, gravity coupling, continuum dynamics, or phenomenology;
6. an axiom amendment, independent audit retention, obligation retirement, or
   TOE completion.

The result therefore remains **`CONDITIONAL-HALO`**: static collision safety is
positive, arrow selection is the named local gap, and no broad no-member claim
is licensed.

## 8. Portfolio decision

The newest connection-dynamics result computes an exact finite `r=3,q=2`
cubic response, but it still imports temporal multipliers, an outer response
coefficient, crossing/projector data, and a finite carrier.  It does not derive
time or gravity.  That makes the next Record-content orientation discriminator
higher leverage than another isolated response coordinate: it directly tests
whether an existing axiom-level primitive closes the current history bridge or
whether a genuinely new physical readout primitive must be named.

The next block should therefore allow only the coarsest content-determined
Record readout needed to obtain signed `f`, retain the all-or-none guard, and
then retest arbitrary finite prefixes and reflected endpoints.  It must keep
the microscopic-POVM, rate/clock, interacting-front, and gravity obligations
explicitly open.
