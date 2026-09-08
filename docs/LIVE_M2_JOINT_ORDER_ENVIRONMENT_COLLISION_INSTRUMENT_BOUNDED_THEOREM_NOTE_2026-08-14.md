---
claim_id: live_m2_joint_order_environment_collision_instrument_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "For the exact Block90 ready write-disjoint semantic-overlap witness left:B=right:R at (-1,-1,0), the two isolated ideal event words differ by sqrt(2), but a single supplied joint transaction is normalized by retaining physical order in an equal two-valued environment. The instrument has refusal, no-event, and two order labels times sixteen joint event labels, for 34 outcomes total. On the rank-256 joint-ready subspace of the fifteen-site semantic carrier, both order-specific branch families separately normalize to one and the complete instrument closes to residual 4.44e-16. All 32 nonzero event maps preserve the six arbitrary archive-target qubits against an external reference with rank 64 and maximum normalized Gram residual 5.33e-15, while producing six exact branch locks. Order is load-bearing: the two conditional distributions have total-variation distance 0.190900887 for matter (0,0) and 0.076360355 for matter (0,1). Both order words compile to 374 nearest-neighbor primitives on the same guarded 52-site corridor, exactly matching all 512 tested ready order/basis rows with zero routed-background disturbance. A complete ledger writes six Records, spends two event packets and one supplied order coin, archives both events, adds two conserved source edges, releases the corridor, refuses replay and occupied corridors with state identity, and permits no-event retry. Across the full Block89 finite census, both dilation orders normalize on all 921 ready write-disjoint semantic-overlap placements; 447 have disjoint archive supports, and 445 of those pass all 9,834 present cross-semantic path checks except for two exact trapped paths. The remaining physical walls are two trapped route geometries, 474 archive-overlap placements, 175 write-overlap placements, a selected global Record-aware corridor/route law, NN outcome-environment compilation, actual outcome, hazard derivation, resource genesis/renewal, cadence, source/action typing, gravity, audit retention, obligation retirement, and TOE percentage movement."
upstream_dependencies:
  - minimal_axioms
  - live_m2_pair_aware_swapback_collision_repair_bounded_theorem_note_2026-08-14
runner: scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py
---

# Live-M2 Joint Order-Environment Collision Instrument

**Date:** 2026-08-14

**Type:** `bounded_theorem`

**Audit authority:** independent audit only

**Constitutional effect:** none. This note is not an approved primitive and
does not edit an axiom, premise registry, audit ledger, or effective-status
surface.

**Primary runner:**
[`scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py`](../scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py)

**Selected parent (original receipt retained as history):**
[`LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md`](LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md),
receipt `161a6ed1f9`.

**Current constitutional authority:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Block90 ended at a genuine semantic collision. For the ready pair

```text
R = diag(-1,-1,1),  t = (1,-2,1),
left:B = right:R = (-1,-1,0),
```

the two isolated ideal event orders differ by `sqrt(2)`. No route restoration
can make noncommuting semantic operators commute.

The positive repair is to stop asking two isolated updates to be confluent.
Make them one joint transaction and retain which dilation order occurred in a
finite environment. Both coherent dilations act before either archive. Their
outcomes are projected jointly, and the two archives are then applied on
disjoint six-site archive supports.

The resulting instrument has

```text
1 refusal + 1 no-event + 2 orders x 16 joint event labels = 34 outcomes.
```

It is normalized on the exact fifteen-site semantic carrier. All 32 nonzero
event maps preserve six arbitrary archive-target qubits against an external
reference, write six exact locks, and have rank 64. The order environment is
not decorative: its two branch distributions differ with total-variation
distance `0.190900887...` for matter `(0,0)` and `0.076360355...` for
matter `(0,1)`.

The two ordered coherent words also have exact finite NN implementations:

| quantity | left-then-right | right-then-left |
|---|---:|---:|
| physical primitives | 374 | 374 |
| logical routes | 46 | 46 |
| touched / guarded sites | 52 | 52 |
| unrecorded route-background sites | 37 | 37 |
| ready semantic/archive basis rows | 256 | 256 |
| maximum semantic residual | 0 | 0 |
| background changes | 0 | 0 |

This does not yet compile the joint outcome projection or 34-valued
environment into NN primitives. It compiles the two order-conditioned unitary
words around that still-abstract outcome interface.

The full finite critical-pair census changes the route map materially:

| ready collision class | count | present result |
|---|---:|---|
| semantic supports disjoint | 1,134 | Block90 conditional swap-back repair |
| semantic overlap, archive supports disjoint, all paths found | 445 | joint order-environment law plus unitary NN compiler skeleton |
| semantic overlap, archive supports disjoint, path trapped | 2 | abstract joint instrument; present NN route fails |
| semantic overlap, archive supports overlap | 474 | joint dilation normalizes; conservative joint archive missing |
| Record writes overlap | 175 | Record capacity/merge disposition missing |
| total simultaneously ready | 2,230 | exact partition |

Thus the conditional finite compiler campaign grows from `1,134/2,230 =
50.852%` to `1,579/2,230 = 70.807%`. Those are **critical-pair coverage
fractions**, not TOE lane percentages and not retained closure.

## 1. Exact Joint Instrument

Let `Gamma` be the projector onto simultaneous readiness of the two events.
On the fifteen-site union it has rank 256: two matter bits and six arbitrary
archive-target bits remain free. Let

```text
D_0 = D_right D_left,
D_1 = D_left D_right
```

denote the two operator orders, with the rightmost factor acting first. For
joint branch label `alpha=(m_left,b_left,m_right,b_right)`, let `Q_alpha` be
the product of the two diagonal output projectors. On this witness the two
archive supports are disjoint, so

```text
A = A_left A_right = A_right A_left
```

is a well-defined unitary archive word.

The supplied hazard remains the Block86 value `h=1/3`. Introduce an equal
order coin `o in {0,1}` and define

```text
K_refusal       = I - Gamma,
K_no-event      = sqrt(2/3) Gamma,
K_(o,alpha)     = sqrt(1/6) A Q_alpha D_o Gamma.
```

For each order separately, the runner evaluates all 256 ready basis columns
and all sixteen joint projections:

```text
sum_alpha ||Q_alpha D_o |psi>||^2 = 1.
```

Consequently,

```text
K_refusal^* K_refusal
+ K_no-event^* K_no-event
+ sum_(o,alpha) K_(o,alpha)^* K_(o,alpha)
= I.
```

The maximum ready-subspace normalization residual is `4.44e-16`. The
complement is carried identically by the refusal projector. The conceptual
Naimark output has 34 orthogonal outcome sectors, and a padded binary
environment needs six qubits. No minimality claim is made: another Kraus
representation or coherent-order dilation may compress or reorganize that
environment.

## 2. Conservative Archive And Six Locks

The exact witness is especially useful because the two archive supports are
disjoint. After both dilations and the joint branch projection, each event
performs the Block86 archive operation:

```text
H on P,
P <-> head target,
M <-> root target,
B <-> meta target.
```

Every one of the 32 nonzero order/branch maps is exercised on all 64 basis
states of the six target qubits. For each map:

- exactly one two-bit matter input sector is nonzero;
- all 64 target columns survive;
- the normalized column Gram matrix is the identity to at most `5.33e-15`;
- the map has rank 64; and
- the six output target sites carry `K_minus`, `K_m`, and `K_b` for the two
  events with maximum lock residual `6.66e-16`.

The conditional branch weights range from

```text
0.0236396451679 to 0.64.
```

After the event hazard and equal order coin, the actual Kraus probabilities
range from `0.00393994086131` to `0.106666666667` on their supporting matter
sectors.

The rank/Gram result is the external-reference statement: each nonzero branch
is proportional to an isometry on the full six-qubit archive space. A hostile
control that erases one archived target drops the rank and fails this gate.

## 3. Why The Order Environment Is Load-Bearing

For a fixed matter input, normalize the sixteen event-branch probabilities
inside each order. The exact total-variation distances are:

| matter `(m_left,m_right)` | TV between order distributions |
|---|---:|
| `(0,0)` | `0.190900887080303` |
| `(0,1)` | `0.076360354832122` |
| `(1,0)` | `< 6e-16` |
| `(1,1)` | `< 2e-16` |

Therefore the construction cannot silently replace the two order-conditioned
families by either order alone. The equal mixture is supplied law content. The
orthogonal order sector keeps the two CP alternatives from interfering.
Tracing that sector would give the averaged channel, but it would not make the
order degree absent from the physical dilation.

Event-label exchange acts exactly by

```text
(o, alpha_left, alpha_right)
  -> (1-o, alpha_right, alpha_left).
```

The runner checks 128 order/branch rows under this relabeling with zero
residual. This is covariance under exchange of the two event labels. It is not
yet a selected spatially covariant atlas for arbitrary event sets.

## 4. Full Semantic-Overlap Census

Block90 partitioned the 2,230 simultaneously ready routed-core overlaps into
1,134 semantic-disjoint, 921 write-disjoint semantic-overlap, and 175
write-overlap placements. This block exhausts the middle class.

For every one of the 921 placements, and for both dilation orders, the runner
checks every basis state allowed by the joint readiness constraints. Both
output `P` factors remain in the branch-projector support. There are 1,842
order checks and zero normalization failures. Thus order mixing is not a
one-witness normalization trick.

The archive-support overlap histogram is exact:

| archive-support overlap sites | placements |
|---:|---:|
| 0 | 447 |
| 1 | 432 |
| 2 | 40 |
| 3 | 1 |
| 4 | 1 |

For the 447 zero-overlap cases, the two archive unitaries have disjoint
supports. The same 34-outcome formula therefore supplies an abstract
normalized six-lock joint instrument, subject to each pair's readiness domain
and any reduced freedom caused by cross-role site identifications. The full
six-arbitrary-target rank theorem is claimed only for the displayed witness.

The current pair-aware route search then asks for 22 logical endpoint paths
per placement:

```text
447 pairs x 2 events x 11 distinct endpoint pairs = 9,834 path checks.
```

Exactly two paths fail, in two distinct placements. Hence 445 placements have
all present compiler paths. The failures are:

```text
R=((0,-1,0),(0,0,-1),(1,0,0)), t=(0,0,1),
right: (-1,-1,-1) -> (-1,0,0),

R=((0,0,1),(-1,0,0),(0,-1,0)), t=(-1,0,0),
left: (-2,1,1) -> (-1,1,0).
```

The finite semantic obstacle set traps the selected endpoint under the current
rule that forbids every other semantic site as route interior. These are not
numerical search timeouts. The two trapped route geometries remain open: a
joint semantic permutation, added local port, or different compiler may still
repair them.

The 474 archive-overlap cases need more than another order coin. Sequentially
applying the two parent archive swaps can move or disturb a lock just written
by the other event, duplicate a shared classical source, or demand two
different contents at one intermediate semantic site. A conservative joint
archive/capacity law must resolve those demands explicitly.

## 5. Exact NN Compiler And Corridor Scope

For the displayed witness, every two-qubit logical gate is compiled by moving
one endpoint along a nearest-neighbor path, applying the gate, and reversing
the route immediately. Both dilations are completed in the order selected by
the order environment. Only then are the two disjoint archive words compiled
by interior-restoring endpoint transpositions.

Each order uses:

```text
58 logical dilation gates,
46 nontrivial endpoint routes,
374 NN primitives,
52 touched sites,
37 route-only background sites.
```

Every route macro is checked on its full path basis. The complete physical
word is then compared with the ideal fifteen-site word on all 256 ready
matter/archive basis inputs and a nonuniform assignment of the 37 route-only
factors. Both orders have exact observed residual zero and zero background
changes.

As in Block90, “arbitrary background” means arbitrary **unrecorded live
factors**. The selected 52-site physical corridor must be checked against the
complete permanent Record map and reserved as one joint transaction.

The same exact ambient witness remains load-bearing. A `K1` Record at
`(-2,-1,0)` lies outside the semantic support but inside the corridor.
Zero-based primitive 34 is

```text
SWAP((-1,-1,0),(-2,-1,0)),
```

and changes the recorded site's marginal from `{0:0,1:1}` to
`{0:1/2,1:1/2}` before swap-back restores it at macro end. The physical
ledger therefore refuses this occupied corridor with exact state identity.
Final restoration is not primitive-step Record permanence.

The global Record-aware corridor protocol remains open. The finite word does
not derive corridor availability, reservation acquisition, deadlock freedom,
or a covariant route atlas.

## 6. Complete Ledger, Resource Debit, And Depth Two

For each of the 32 event outcomes, the classical transaction checks the full
52-site corridor and its exact reservation before executing. A successful
event branch:

```text
writes six permanent Records,
spends the left and right event packets,
spends one supplied order coin,
archives both event targets,
adds two oriented source edges,
stores one order/branch environment label,
releases the 52-site reservation.
```

Both decoded three-Record packets are recovered, and each source edge obeys

```text
Delta J + boundary = 0.
```

An event replay is an exact guard refusal. No-event is identity and leaves all
three resources and the reservation available, so a later retry succeeds. A
pre-existing Record at either a write site or any route-only corridor site
forces exact refusal with state identity. Mutations that permit overwrite or
ignore an ambient route Record fail the ledger gate.

The supplied branch label is still not a physical actual-outcome mechanism.
The 34-sector Naimark environment is an exact mathematical interface; its
query, pointer, actual draw, and NN circuit remain uncompiled.

## 7. Authority And Axiom Decision

The current premise registry still contains only `minimal_axioms`,
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive`. Their live sources contain no joint
order-environment collision law, equal order coin, joint Record-aware corridor
protocol, or clean coin renewal law.

This construction is therefore not derivable from current authority. It is
an extensional formation/update candidate. Adopting its route would require a
primitive or amendment that states at least:

1. how simultaneously ready events are grouped into one joint transaction;
2. the joint readiness projector and the two order-conditioned dilation maps;
3. why the order coin is equal and why the event hazard is `1/3`, or a
   derivation replacing those supplied values;
4. the joint output/archive rule for every overlap class;
5. the complete Record-map corridor guard, reservation, and covariant route
   protocol;
6. the physical outcome environment and actual branch interface;
7. event-packet and order-coin genesis, debit, renewal, and cadence; and
8. the source-to-action/energy identification required before gravity.

No axiom edit is justified yet from one exact full witness plus finite-class
coverage. The 474 archive overlaps, two trapped paths, and 175 write overlaps
must either receive one coherent law or be excluded by an explicit lawful
formation domain. Dense Records may also block corridor liveness.

- the selected global joint law remains open;
- the global Record-aware corridor protocol remains open;
- clean-resource genesis and renewal remain open;
- source/action typing and gravity remain open.

## 8. Strict TOE Accounting

There is no TOE percentage movement. No retained obligation is retired, and
the retained-positive end-to-end theory count remains zero.

| lane | operational | physical | autonomous | ceiling |
|---|---:|---:|---:|---:|
| operational / Records | 95% | 92% | 50% | 99% |
| causal / time | 76% | 72% | 41% | 99% |
| inertia / matter | 95% | 96% | 75% | 99% |
| gravity / source / resources | 70% | 45% | 29% | 94% |
| Born / history | 84% | 63% | 34% | 99% |

The scientific progress is significant but pre-retention:

- the exact `sqrt(2)` semantic collision now has a normalized positive joint
  instrument rather than only a localized obstruction;
- all 32 event branches conserve six arbitrary archive qubits on the witness;
- order dependence is quantified and carried by a finite physical
  environment instead of hidden in scheduler choice;
- both order words have exact 374-primitive NN implementations on a guarded
  corridor;
- the 921 semantic-overlap class is partitioned into 445 present routed
  candidates, two route traps, and 474 archive collisions; and
- conditional ready-pair compiler coverage rises from 50.852% to 70.807%.

The priority stack is now:

1. construct one conservative joint archive/capacity map for the 474
   archive-overlap cases, testing whether it also handles the 175 write
   overlaps;
2. attack the two trapped paths with a joint semantic permutation or prove the
   exact added-port requirement;
3. compile the 34-outcome query/environment and Record pointer into NN
   primitives with exact corridor guards;
4. derive rather than supply event packets, the order coin, renewal, hazard,
   and physical cadence; and
5. attach action/energy meaning to the two conserved source edges, then test
   nonlinear Ward/connection and gravity closure.

Another isolated-order commutator census is now lower leverage.

## 9. No-Go Discipline Record

The remaining-boundary claims were subjected to the current N1--N8
discipline. “Closed” means closed only on the exact stated fixture or finite
class.

### N1 — Alternative-route enumeration and normalization

| route | attack | result | disposition |
|---|---|---|---|
| R1 | execute the two isolated semantic instruments sequentially | exact order residual `sqrt(2)` | **attempted / insufficient** |
| R2 | choose one order deterministically | supplies a selector and retains order-dependent output statistics | **viable only as added law** |
| R3 | equal stochastic order environment with orthogonal order sectors | 34 outcomes normalize; both events execute | **positive / constructed** |
| R4 | coherent quantum switch or compressed Kraus environment | may reorganize the order degree | **open alternate positive route** |
| R5 | refuse every semantic overlap | safe but deadlocks all 921 cases | **normalized / liveness-negative** |
| R6 | apply both dilations before either archive | both orders normalize on all 921 placements | **positive core theorem** |
| R7 | use the two parent archives when their supports are disjoint | 447 placements; exact six-target witness proved | **positive / scoped** |
| R8 | sequential parent archives on overlapping supports | can disturb locks or misroute shared contents | **attempted / insufficient for 474** |
| R9 | pair-aware cross-semantic swap-back routes | all paths exist on 445 archive-disjoint placements | **positive / conditional compiler** |
| R10 | forbid every other semantic site on the two trapped geometries | two exact endpoint paths fail | **attempted / insufficient** |
| R11 | joint semantic permutation or added local port for trapped paths | not constructed | **open positive route** |
| R12 | merged conservative archive/capacity network | could address 474 archive and 175 write overlaps together | **highest open positive route** |
| R13 | simultaneous incompatible writes without disposition | violates permanent Record capacity | **rejected** |
| R14 | Record-only nonunitary formation law | remains an alternate theory without the live-M2 compiler | **open alternate route** |

R3 is not a proof that the equal coin is selected. R6 is normalization of the
dilation/projector core, not conservative archive closure of all 921 cases.

### N2 — Wall-independence audit

Define:

```text
W1 live-M2 and joint-transaction authorization
W2 selected order/hazard collision law
W3 conservative archive/write-capacity disposition
W4 global Record-aware corridor, reservation, and route atlas
W5 outcome query, pointer, and actual branch
W6 packet/coin genesis, renewal, and physical cadence
W7 conserved-source to action/energy typing
W8 nonlinear Ward/connection and gravity law
```

| pair | independent? | exact reason |
|---|---|---|
| W1/W2 | yes | authorizing live factors does not select an equal order coin or hazard; an abstract CP law can be stated on a supplied carrier |
| W1/W3 | yes | ontology does not resolve overlapping archives or writes; a Record-only theory faces the same capacity problem |
| W1/W4 | yes | live authorization does not supply a blank corridor, reservation protocol, or route atlas |
| W1/W5 | yes | a carrier supplies no actual pointer or draw |
| W1/W6 | yes | state authorization does not create or renew packets, coins, or a clock |
| W1/W7 | yes | source edges are not an energy/action identification |
| W1/W8 | yes | ontology supplies no nonlinear connection response |
| W2/W3 | yes | a normalized order mixture can still overwrite an archive; a capacity map can be stated for another collision law |
| W2/W4 | yes | semantic normalization does not route around Records; a route atlas does not choose outcome statistics |
| W2/W5 | yes | a CPTP instrument can exist without an actual branch interface |
| W2/W6 | yes | a one-shot supplied coin does not renew itself or set a rate |
| W2/W7 | yes | order statistics do not type source action |
| W2/W8 | yes | a local joint channel does not select gravity |
| W3/W4 | yes | a conservative archive map may be nonlocal; a corridor can exist for incompatible writes |
| W3/W5 | yes | exact archive unitary does not make an outcome actual |
| W3/W6 | yes | information preservation does not renew resources |
| W3/W7 | yes | archived content is not automatically energy |
| W3/W8 | yes | Record capacity supplies no connection law |
| W4/W5 | yes | a routed circuit may lack a pointer; an abstract pointer may lack a route |
| W4/W6 | yes | finite routes do not generate clean ancillas or cadence |
| W4/W7 | yes | geometry of a route does not normalize source action |
| W4/W8 | yes | an atlas is not a gravitational response law |
| W5/W6 | yes | an outcome can be realized once with a consumed, unrenewed environment |
| W5/W7 | yes | actuality does not identify stress/energy |
| W5/W8 | yes | a Born interface is not gravity |
| W6/W7 | yes | cadence and renewable tokens still need physical action units |
| W6/W8 | yes | a clock alone does not generate a metric response |
| W7/W8 | yes | a typed conserved source still requires a selected nonlinear field law |

One integrated joint archive/resource/source cell could couple W3--W7. That is
why it outranks another carrier or commutator count.

### N3 — Hidden-wall scan

| trigger family | checked surface | result |
|---|---|---|
| current authority | live axiom, registry, and four premise sources | no joint collision, equal coin, corridor law, or renewal registration |
| parent drift | exact Block90 runner/note hashes and receipt | frozen parent reproduced |
| normalization | 34 outcomes on rank-256 ready plus rank-32,512 refusal complement | complete to `4.44e-16` |
| zero branches | all two orders times sixteen labels | 32 maps nonzero somewhere; each exact matter support named |
| archive erasure | all six target qubits and external reference | rank 64 and Gram identity; erase-target control fails |
| lock content | six output Record targets on every nonzero map | `K_minus,K_m,K_b` residual below `7e-16` |
| hidden order choice | two conditional distributions and equal coin | nonzero TV exposes the order degree; equality is supplied, not derived |
| covariance rhetoric | event-label exchange versus spatial atlas | 128 relabel rows pass; arbitrary-set spatial covariance remains open |
| archive overlap | all 921 placements | exact 447/474 support partition; no six-lock claim for the 474 |
| path coverage | 9,834 cross-semantic paths | 2 exact failures; no Record-aware global atlas inferred |
| ambient Records | exact route-only `K1` witness | primitive disturbance; full 52-site guard gives identity refusal |
| outcome actuality | 34-sector mathematical environment | query/pointer/draw and NN compilation absent |
| resources | two packets and one order coin | debit explicit; genesis, renewal, and cadence absent |
| source/gravity | two incidence-conserved edges | energy/action and connection response absent |
| globality | finite two-event relative placements | arbitrary event sets and infinite histories excluded |

### N4 — Residual matching

| claim | exact matched evidence | rejected nonmatch |
|---|---|---|
| C1 semantic collision has a positive joint resolution | normalized 34-outcome instrument on the exact `sqrt(2)` witness | averaging prose without a complete CP family is not credited |
| C2 order is physical in this construction | TV `0.1909` and `0.07636`, orthogonal order sectors | scheduler order is not hidden or called irrelevant |
| C3 archive information is conserved on the witness | 32 rank-64 maps, six-target Gram identity, six locks | completeness alone is not called conservative archive closure |
| C4 finite-class reach is 445 routed candidates | exact 921 split, 447 archive-disjoint, 9,834 paths with two failures | 445 is not relabeled a selected law or full instrument circuit |
| C5 474 cases remain a joint archive wall | direct archive-support overlaps of sizes 1--4 | semantic normalization is not called six-lock compatibility |
| C6 gravity remains open | source ledger has no action, energy, cadence, connection, or field response | critical-pair coverage is not gravity progress |

The principal next residual is W3: a conservative joint archive/capacity law.

### N5 — Rhetoric and granularity audit

| claim | per element | per site | per mode | per block | lattice-wide resolution |
|---|---|---|---|---|---|
| C1 joint instrument | 34 outcomes, 32 nonzero event maps | 15 semantic sites | refusal, no-event, two orders, 16 branches/order | completeness plus Naimark dimensions | exact witness; selected law not claimed |
| C2 archive/reference | 64 target columns/map | six target and six lock sites | all nonzero branches | rank, Gram, density locks, erase control | exact witness only |
| C3 order environment | two labels and four matter rows | shared `B/R` factor | both orders and relabeling | distributions plus branch maps | equal coin supplied, not universal |
| C4 finite coverage | 921 pairs, 9,834 paths | overlap histogram 0--4 | normalized, archive-disjoint, trapped, archive-overlap | census plus BFS | finite relative-placement census only |
| C5 NN compiler | 374 primitives and 46 routes/order | 52 guarded, 37 unrecorded backgrounds | both order words | macro plus full ready word | 445 path-existence candidates; outcome projector uncompiled |
| C6 ledger/resources | six Records, two packets, one coin, two edges | write and corridor guards | event, no-event, retry, replay, occupied | quantum/environment/classical ledger | no arbitrary histories, renewal, time, energy, or gravity |
| C7 TOE boundary | four premises | Record, live, route, source separated | authority, actuality, cadence, gravity | parent, runner, note, cache | no retention, obligation retirement, or score movement |

The runner emits corresponding `N5_RESOLUTION` lines into its canonical cache.

### N6 — Partial-closure path scan

The exact semantic collision now has a positive normalized joint instrument,
not merely a no-go. The finite census also shows that the same order-mixture
core normalizes across all 921 semantic overlaps. Conservative disjoint
archives reduce the immediate routed candidate class to 445.

The shortest positive path is:

1. express the 474 archive overlaps as finite source/destination graphs;
2. search for one reversible joint permutation plus environment that preserves
   every displaced prestate and writes compatible locks;
3. include the 175 write-overlap cases by adding an explicit merged-content or
   capacity outcome rather than overwrite;
4. solve the two trapped path geometries with the same joint permutation or
   name the minimal added local port;
5. compile the order/outcome environment and pointer into the guarded NN word;
6. close packet/coin renewal and cadence on depth-two histories; and
7. type the conserved source as action/energy before gravity testing.

A separate global atlas for already routable cases is secondary unless it is
integrated with the archive/resource construction.

### N7 — Steelman and strongest surviving escape route

The strongest steelman is one reversible collision network on the entire
overlap component. It reads the complete ready cluster and Record map, uses a
finite order/outcome environment, treats shared semantic and archive sites as
one permutation/isometry problem, archives every displaced prestate, emits
either six compatible Records or an explicitly merged capacity Record,
reserves its complete transient corridor, returns or renews its collision
tokens, and assigns its conserved boundary current an action/energy unit.

Such a cell could close the 474 archive overlaps, 175 write overlaps, two
route traps, pointer, renewal, cadence, and gravity handoff in one law. Nothing
here rules it out. The current result supplies its normalized order core and
one fully conservative witness.

### N8 — Cross-cycle echo audit

| earlier echo | present relation | disposition |
|---|---|---|
| Block71 conservative archive | supplies exact target-preserving locks | doubled on disjoint archive supports; overlap not inferred |
| Block72 NN gate compiler | supplies SWAP-conjugated two-site gates | reused with immediate swap-back paths |
| Block73 overlap scheduler | warned that write-disjointness is insufficient | realized here as semantic, archive, and route distinctions |
| Block86 six-outcome instrument | supplies `h=1/3`, readiness, branches, archive | promoted to a supplied 34-outcome two-event candidate, not authority |
| Block89 semantic/physical support census | supplies 2,230 critical pairs and `sqrt(2)` witness | middle 921 class exhausted directly |
| Block90 guarded corridors | supplies cross-semantic paths and ambient-Record counterexample | guard expanded from 32 to 52 sites and retained exactly |
| earlier all-conflicts-refuse scheduler | safe but deadlocking | dominated on the 445 positive routed class |
| historical source/Green candidates | suggest field response | not imported as action, energy, cadence, or gravity authority |

Lifecycle disposition:

- Blocks 89 and 90 remain valid on their exact compiler/support scopes.
- This note resolves the displayed semantic witness by changing the law from
  two isolated events to one order-environment transaction.
- It does not supersede the parent, because the parent covers the
  semantic-disjoint class with a smaller environment.
- No source is promoted, retained, or registered here.
- The next cycle should attack the joint archive/capacity graph, not repeat
  the isolated-order obstruction.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py
```

The baseline must end with `TOTAL: PASS=9 FAIL=0`. Mutation runs must reject
stale authority, a missed census row, broken completeness, target erasure,
collapsed order, missing swap-back, Record overwrite, an ignored ambient
Record, erased source, invented renewal, and false TOE progress.

## 2026-09-08 provenance correction

The original commit/parent hashes remain immutable historical identities.
They do not require the extracted current-main candidate to retain the raw
branch ancestry. Gate A separately verifies the selected current parent and
all declared proof/runtime inputs, including the current constitutional
files. Corrected parent source is pinned bottom-up; historical receipts are
not substituted for current source or scientific acceptance. The supplied
finite construction and its physical-law boundaries above are unchanged.
