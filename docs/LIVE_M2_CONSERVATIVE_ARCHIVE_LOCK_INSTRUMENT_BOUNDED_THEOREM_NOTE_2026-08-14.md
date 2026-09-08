---
claim_id: live_m2_conservative_archive_lock_instrument_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the declared finite live-M2 substrate domain, the exact Block73 refusal/no-event/four-event Kraus family, Block72 73-primitive nearest-neighbor coherent event core, and Block71 three-target archive/lock compose algebraically into one normalized six-outcome hybrid quantum/Record candidate instrument. A direct-sum guard preserves the complete quantum-plus-Record state on occupied or replayed support. The four event maps read the live matter factor without a host-selected matter bit or supplied realized branch, have weights q p(b|m) at q=1/3, preserve an arbitrary three-qubit target state and external reference branchwise, and append three Record memberships whose contents are the already-present target projectors. Completeness, Kraus rank six, an exact rank-two Gamma query, an exact 1536-by-256 six-outcome Stinespring isometry, four rank-eight branch isometries, a rank-32 combined archive, 2,048 coherent-core basis cases, 96 all-frame Record cases, complete-state refusal/replay, source-edge decoding, and an unarchived rank-4/32 hostile control are checked. The 73 primitives do not compile Gamma gating, outcome coupling, Record append, or the guard. Current fixed one-site nearest-neighbor Admissibility compatibility is not established: three identical blank prior Record neighborhoods have unequal conditional lock measures. This is a candidate under an amended or registered formation law, not authorization of live M2 as physical state, selection of the extensional law, clean-resource genesis/renewal, physical actuality, overlap confluence, time, gravity, audit retention, obligation retirement, or TOE percentage movement."
upstream_dependencies:
  - minimal_axioms
  - same_carrier_three_record_archive_packet_bounded_theorem_note_2026-08-13
  - nn_formation_selector_two_model_kill_bounded_note_2026-08-14
  - record_visible_integrated_formation_instrument_bounded_note_2026-08-14
runner: scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py
---

# A Conservative Live-M2 Archive-Lock Formation Instrument

**Date:** 2026-08-14
**Type:** bounded theorem
**Audit authority:** none. Independent audit alone may assign retention.
**Primary runner:**
[`scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py`](../scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py)

**Scientific parents:**

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md`](SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md)
- [`NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md`](NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md)
- [`RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md`](RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md)

## Result up front

The missing **algebraic** one-event composition left by Blocks 71--73 exists.

On five live qubit factors `P,M,B,R,A`, three arbitrary target factors, and
the exact clean-domain projector `Gamma`, define one refusal map, one no-event
map, and four event maps. The event maps apply the existing five-factor
dilation, select their own `(m,b)` output sector, mark the head, archive all
three target prestates, and leave the three exact projectors

```text
head = |-><-|,  root = |m><m|,  meta = |b><b|
```

already present at the sites that become Records. The classical half of the
same outcome atomically adds those three Record memberships. No target state
is reset, copied, traced out, or silently replaced.

The runner establishes all of the following on the declared finite domain:

- six Kraus outcomes have completeness residual `1.13e-15` and Kraus rank
  six;
- vertically stacking those maps gives an exact `1536 x 256` Stinespring
  isometry, but no nearest-neighbor gate compilation of that isometry is
  inferred;
- the exact rank-two `Gamma` pointer query is unitary on a one-qubit pointer,
  but it is not nearest-neighbor compiled;
- Block72's compiled rank-four query contains the coherent ready image but is
  not the `Gamma` query: the projector residual is `sqrt(2)`;
- all 64 clean matter/target basis probability rows and 45 coherent
  matter/target rows have the exact no-event and `q p(b|m)` values;
- none of the four event labels, the realized branch, or `m` is supplied by
  host control;
- each event branch is a rank-eight isometry on the arbitrary target space;
  the four labeled branches give rank `32/32` with Gram residual `3.8e-15`;
- target/reference information is therefore preserved for arbitrary
  superpositions and arbitrary external references;
- the three reduced target states match the lock projectors at residual below
  `8e-16` and factor with probability one;
- the ordered **coherent event core** has 73 one-/two-site nearest-neighbor
  primitives on 15 sites and agrees with the ideal core in all 2,048
  clean-domain basis states with arbitrary route/target backgrounds;
- all 96 frame/`m`/`b` classical Record executions normalize, preserve prior
  Records, and decode the signed source edge; 16 blank quantum rows and 32
  complete-state replays verify the direct-sum guard, including exact
  quantum-plus-Record refusal on occupied/replayed supports; and
- the hostile unarchived replacement has rank `4/32` and Gram residual
  `14.97`, so the archive is load-bearing for this conservative route.

This is significant positive local progress. It removes the earlier need to
hand the code a realized branch or a host-readable matter bit, and it joins
the live quantum outcome to the exact same-carrier Record locks in one
probability space. It does **not** make the object the framework's physical
law. The current axiom says that a state is a configuration of Records, that
only Records are readable, and that one fixed one-site distribution varies
with nearest-neighbor conditions. It neither authorizes an unrecorded
entangled live-M2 substrate as causal state nor supplies one-site measures
whose conditional marginals match this joint instrument. The live-M2 ontology
is conditional. The current fixed one-site NN Admissibility compatibility remains open.

No TOE score changes in this note. The effective retained-positive theory
count remains zero.

The candidate is not an approved primitive; overlap confluence is not executed.

## 1. Exact finite instrument

### 1.1 Input domain

Use the Block71 wire order

```text
(P,M,B,R,A) = (0,1,2,3,4).
```

The two-dimensional ready subspace is

```text
Gamma = |1><1|_P tensor I_M tensor |0><0|_B
        tensor |0><0|_R tensor |0><0|_A.
```

Thus `M` is not supplied as a classical argument. It is a live quantum input.
The other four factors are fixed resources. Three further qubit factors
`T_head,T_root,T_meta` may be in an arbitrary joint state, including a state
entangled with an external reference.

Let `U` be Block71's exact 29-gate five-factor dilation. Let `Pi_mb` project
the output onto

```text
P=1, M=m, B=b,
```

while retaining `R,A`. Let `A` first apply `H` to `P` and then exchange

```text
P <-> T_head,
M <-> T_root,
B <-> T_meta.
```

Every operator below is tensored with the identity on the three target
inputs before `A` acts.

### 1.2 Six outcomes

At the declared witness hazard

```text
q = 1/3,
```

define

```text
K_ref       = I - Gamma,
K_no        = sqrt(1-q) Gamma,
K_mb        = sqrt(q) A (Pi_mb U Gamma tensor I_T),
              (m,b) in {0,1}^2.
```

These are six distinct outcome maps: refusal, no event, and four events. The
branch is an output label of the instrument, not a supplied realized branch.
The matter value is selected by `Pi_mb` from the live input, not passed by the
host.

The exact completeness identity is

```text
K_ref^dag K_ref + K_no^dag K_no
  + sum_(m,b) K_mb^dag K_mb = I.
```

The runner checks the `256 x 256` identity directly. It also checks the
Hilbert--Schmidt Gram rank of the six Kraus operators. The rank is six, so an
implementation that insists on unitary dilation rather than treating the
instrument as a primitive needs an outcome environment of dimension at least
six. Three binary qubits provide dimension eight; no such environment is
silently included here.

The runner also stacks the six maps vertically,

```text
V = sum_o |o> tensor K_o : C^256 -> C^6 tensor C^256,
```

and checks `V^dag V = I_256` plus exact recovery of every `256 x 256` outcome
block. This proves an abstract `1536 x 256` Stinespring isometry. It does not
compile `V`, the outcome pointer, or actualization into nearest-neighbor
operations.

The exact nondemolition pointer query for the rank-two input projector is

```text
Q_Gamma = [[I-Gamma, Gamma], [Gamma, I-Gamma]].
```

It is unitary and gives the correct pointer value on all 32 five-factor basis
states. It is also only an abstract certificate. Block72's compiled `78+3`
query is a different rank-four projector on the four dephased branch rays.
Its coherent rank-two subspace contains `U Gamma U^dag`, but the two projectors
differ by Frobenius norm `sqrt(2)`. It must not be credited as a compilation of
this `Gamma` query.

### 1.3 Exact weights without host-selected `m`

For a clean basis input `|1,m,0,0,0>` and every target basis state,

```text
Pr(refusal) = 0,
Pr(no event) = 2/3,
Pr(m',b) = delta_(m,m') (1/3) p(b|m),

p(.|0) = (1/2,1/2),
p(.|1) = (1/5,4/5).
```

For a coherent matter input

```text
alpha_0 |m=0> + alpha_1 |m=1>,
```

the event probability is

```text
Pr(m,b) = (1/3) |alpha_m|^2 p(b|m).
```

The runner uses three phase-distinct matter superpositions and three
target-state superpositions. This is a measurement instrument: coherence
between `m=0` and `m=1` becomes outcome information. The theorem does not
claim that the input matter phase survives after the branch is actualized.
The conservative statement concerns the arbitrary target/background and
external-reference information.

## 2. Exact archive and lock

### 2.1 Branchwise reference preservation

For fixed `(m,b)`, divide `K_mb` by the square root of its nonzero clean-input
probability and restrict it to the eight-dimensional target input. The result
has Gram matrix `I_8` and rank eight. Across all four labeled branches, the 32
columns have Gram matrix `I_32`.

Consequently, for every target/reference state

```text
|xi>_(T,E),
```

the normalized branch map has the form

```text
|1,m,b>_(PMB) |chi_mb>_(RA) |xi>_(T,E)
   ->
|xi>_(archive,E) |chi_mb>_(RA)
   |-,m,b>_(T_head,T_root,T_meta).
```

The identity Gram matrix proves the statement for arbitrary target
superpositions and arbitrary external reference dimension by linearity. No
finite reference sample is substituted for that proof.

### 2.2 Same-carrier locking

The event output already has the exact local reduced matrices

```text
P_minus, P_m, P_b
```

at the three target sites, jointly with probability one. The classical update
therefore adds Record membership without replacing the local M2 content. The
Record contents are not non-Hermitian parser tags; their geometry supplies
the role/frame data.

For a Record-free event support the event outcome appends all three memberships
atomically. Refusal and no-event leave the complete Record map unchanged. If
any Record already occupies the finite support, including an identical replay,
the hybrid law returns a unit-probability refusal and preserves the complete
map. An overwrite mutation fails this test.

More explicitly, the candidate is a direct-sum hybrid map on a quantum state
`rho` and complete Record map `R`:

```text
support intersects dom(R):
    {(guard_refusal, 1, rho, R)}

support disjoint from dom(R):
    {(o, Tr[K_o rho K_o^dag], normalized K_o rho K_o^dag,
      R union packet_o) : o is an event}
    union the unchanged-Record refusal/no-event outcomes.
```

The runner checks 32 complete post-event replays and three unrelated occupied
states: both `rho` and `R` are preserved exactly. By contrast, applying the
unguarded six-Kraus quantum map to an explicit post-event witness changes its
density matrix by `1/3`. The guard is therefore load-bearing and is not
nearest-neighbor compiled here.

The decoded root-to-head edge gives the exact incidence bookkeeping

```text
Delta J = delta_head - delta_root,
B_edge  = delta_root - delta_head,
Delta J + B_edge = 0.
```

This remains a signed source *syntax*. No stress-energy tensor, energy value,
source normalization, cadence, or gravity coupling is inferred.

## 3. Ordered nearest-neighbor coherent core

Block72 established the primitive count and token layout macro by macro. This
runner adds an ordered end-to-end test of the coherent `U+archive` core.

The physical sequence is

```text
15 relocation SWAPs
+ 53 routed dilation primitives
+ 1 head-marker H
+ 4 compact archive SWAPs
= 73 primitives.
```

All two-site primitives are nearest neighbor. The support contains 15 sites.
The four fixed inputs and live `M` occupy the five original role sites; the
other ten sites are treated as arbitrary basis backgrounds. The runner tests
both matter values and all `2^10` background assignments, for 2,048 complete
basis cases. Each physical output equals the corresponding ideal long-range
word with zero residual. Basis equality plus linearity covers arbitrary
background superpositions and external references.

This `73`-primitive word does **not** implement the rank-two `Gamma` query, the
`q=1/3` refusal/no-event coupling, the four `Pi_mb` outcome sectors, the
six-outcome environment, the direct-sum occupied-support guard, or Record
membership append. Calling it a nearest-neighbor implementation of the full
instrument would be an overclaim.

Every one of the 24 proper-cubic rotations preserves the edge lengths and the
packet decoder. This is spatial covariance with Block71's declared trivial
internal action candidate. It is not a derivation selecting the trivial
internal action over other compatible internal actions.

## 4. Resource ledger

| resource | exact debit in this candidate | generated here? |
|---|---:|---|
| fixed live inputs | `P=1`, `B=0`, `R=0`, `A=0` | no |
| live matter input | one qubit, arbitrary/coherent | no |
| target quantum factors | three arbitrary qubits; all information archived | no reset required |
| Record capacity | three Record-free target sites inside a Record-free 15-site support | no |
| coherent event core | 73 one-/two-site NN primitives | compiled, not physically authorized |
| exact `Gamma` query | rank-two `64 x 64` pointer unitary | exact algebraically; not NN-compiled |
| Block72 query | rank-four projector; `78` routed primitives plus three onsite tests | compiled, but not the `Gamma` query (`sqrt(2)` mismatch) |
| outcome coupling and sectors | hazard plus refusal/no-event/four event maps | exact algebraically; not NN-compiled |
| full outcome isometry | `1536 x 256`; environment dimension at least six | exact algebraically; not NN-compiled or supplied |
| Record append and occupied/replay guard | direct-sum hybrid map | exact on tested finite domain; not NN-compiled or authorized |
| extra clean route bank | zero | background factors are arbitrary and restored/archived |
| hazard | `q=1/3` | declared witness, not selected |
| output actuality | one of six mathematical outcomes | no physical draw/actualization law supplied |
| renewal | the ready packet and blank capacity are consumed by an event | no genesis or renewal supplied |

The archive closes information disposition for the three target factors. It
does not create the four fixed inputs, regenerate them after an event, create
blank Record capacity, or authorize the readiness measurement and stochastic
outcome. A primitive stochastic instrument can take the six outcomes as
fundamental; a conservative unitary implementation instead owes the explicit
six-dimensional outcome environment. These are different theories and are
not silently identified.

## 5. Constitutional and axiom decision

### 5.1 What current authority says

The current axiom memo says all of the following:

- each site has the full one-site possibility presentation `M_2(C)`;
- the Admissibility distribution is a fixed covariant nearest-neighbor rule;
- Records form and permanently lock one supported possibility;
- only Records are readable;
- a state is a configuration of Records; and
- Admissibility is not a dynamics axiom, while update, formation, source, and
  physical-observable rules remain downstream.

Those statements permit the matrices used here as members of the one-site
possibility domain. That is weaker than proving they lie in the support of the
fixed distribution for the actual nearest-neighbor conditions, and weaker
again than matching this joint instrument's conditional one-site measures.
The statements also do not make a consistent entangled state on finite tensor
products of unrecorded M2 factors part of physical state, allow that substrate
to control formation, or authorize local CP instruments acting on it.
Therefore this theorem is a finite candidate under an amended or registered
formation law, not a compatibility qualification relative to the current four
axioms and not an approved primitive.

The narrow current-authority verdict is:

> The conservative live-M2 candidate is mathematically complete for one
> finite event, but it cannot be load-bearing physical law while “state” is
> Record-only, no live-substrate/instrument bridge is registered, and its
> three lock marginals are not matched to the fixed one-site NN law.

This is not a universal impossibility theorem. A Record-only fundamental
stochastic append/nonunitary law remains live, as does another live-substrate
law.

### 5.2 Exact current-Admissibility gap

Before the event, all three target sites are Record-free. On the current
state-as-Records interface their six-neighbor Record conditions are identical:
all six entries are absent. For the clean `m=0` input, however, conditioning
this candidate on formation gives three distinct one-site lock measures:

```text
head: delta_(P_minus)
root: delta_(P_0)
meta: (1/2) delta_(P_0) + (1/2) delta_(P_1).
```

Their pairwise total-variation distances are respectively `1`, `1`, and
`1/2`. A fixed covariant one-site rule cannot assign different measures to
identical supplied NN conditions. This does not prove that the joint
instrument is impossible: a registered formation context could add packet
role/live-substrate data, a sequential law could change intermediate
conditions, or a different instrument could have matching marginals. None of
those bridges is current axiom content or supplied here. Thus current fixed
one-site NN Admissibility compatibility remains open; mere membership in
`M_2(C)` is not a support or marginal certificate.

### 5.3 One sufficient state repair if the live route is intended

One sufficient type-level repair is to distinguish readable state from causal
prestate. No minimality claim is made. Candidate wording, **not adopted here**,
is:

> A readable state is a configuration of permanent Records. A physical
> prestate may additionally contain a consistent state on the quasi-local
> tensor-product algebra generated by the unrecorded site `M_2(C)` factors.
> Only Record content is readable, but a registered covariant local formation
> instrument may condition on the live substrate. When it forms Records, each
> locked content must equal the supported local possibility present in the
> corresponding event outcome, and prior Records may not be overwritten.

This wording preserves Record-only readability while changing the present
Record-only state ontology. It is a material axiom choice, not a clarification
that can be inferred from “site possibility.” It does not by itself repair the
one-site NN marginal gap or select an instrument.

### 5.4 One sufficient live-route payload (not a sufficient TOE payload)

Choosing the state type alone does not select this instrument. One sufficient
live-route payload, spread across axiom text, retained bridges, or explicit
approved primitives, has seven modules:

1. **State domain.** Adopt the readable-state/causal-prestate distinction and
   the consistent quasi-local live-M2 substrate, including how Records and
   live factors coexist.
2. **NN-Admissibility bridge.** Give the exact covariant one-site probability
   measure for every supplied six-neighbor condition, prove support for every
   lock, and state how its one-site marginals relate to the joint formation
   instrument. If packet role or live substrate enters the condition, register
   that enlarged condition explicitly.
3. **Exact local instrument and action.** Register one finite-range covariant
   total instrument, including `Gamma`, query/operation authority, the actual
   extensional branch weights, refusal, supported no-event, archive,
   same-carrier atomic lock, chosen hazard, and selected internal proper-cubic
   action. This note supplies one candidate at `q=1/3` with a trivial internal
   action; it does not select either.
4. **Resource provenance.** State where the four fixed inputs, three blank
   Record targets, and any six-dimensional outcome environment come from, and
   whether/how capacity renews.
5. **Actuality and atomicity.** Specify how one outcome becomes actual and why
   the three memberships form as one event without readable intermediates.
6. **Global process and time.** Supply translated-occurrence recognition,
   overlap arbitration or confluence, a process on arbitrary configurations,
   and the physical time/rate represented by the hazard.
7. **Source and gravity typing.** Map the decoded event/output state to a
   normalized physical source and establish the conservation/Ward/connection
   identities used by gravity.

These seven items need not all be literal sentences in the minimal axiom memo.
Some may be retained derivations, initial-condition/resource laws, or approved
primitive registrations. They cannot be omitted while claiming an end-to-end
live formation-to-source route. It is a sufficient live-route payload and
modular residual set, not owner approval and not a sufficient payload for the
rest of the TOE (including independent matter/chirality obligations).

### 5.5 The surviving Record-only alternative

If the intended ontology is strictly Record-only, the live-M2 construction is
implementation scaffolding rather than physical state. A fundamental
stochastic append law may form Records directly and may dispose of unrecorded
implementation variables nonunitarily. On that theory the rank-`4/32`
unarchived control is not by itself a contradiction, because preservation of
unrecorded target information is not a constitutional obligation.

That alternative still owes the exact fixed one-site NN measure/support,
formation-law values, site/rate, overlap arbitration, time, and a physical
source map. It also gives up the conservative live-M2 explanation unless a
separate resource/environment law restores it. The Record-only nonunitary route remains live;
this note does not select between the two ontologies.

## 6. Gravity and TOE status

This result improves the route to gravity without moving the gravity score.
It supplies an algebraically branch-complete candidate, accounts for the
minimum outcome-environment dimension, and gives an exact signed edge output.
It does not compile the full event, qualify its lock marginals under current
NN Admissibility, type the edge as energy-momentum, fix its normalization,
provide cadence, or establish the nonlinear Ward/connection identity. More TT
response calculations before choosing the state/formation/source law would
remain conditional on the same missing input.

The TOE map is unchanged:

| TOE lane | repository map | physical bridge | autonomous law | current ceiling |
|---|---:|---:|---:|---:|
| operational / Records | 95% | 92% | 50% | 99% |
| causal / time | 76% | 72% | 41% | 99% |
| inertia / matter | 95% | 96% | 75% | 99% |
| gravity / source / resources | 70% | 45% | 29% | 94% |
| Born / history | 84% | 63% | 34% | 99% |

Actual movement requires adoption/retention of a state ontology and exact law,
then a global process and typed gravity source. Local route confidence is not
obligation retirement. This note records zero TOE percentage movement.

## 7. Exact falsifiers

The bounded positive claim fails if any of the following occurs:

- the six Kraus operators fail completeness or positivity;
- a basis or coherent input probability differs from `q p(b|m)`;
- the event construction requires a host-provided `m` or branch;
- any branch map has rank below eight on the arbitrary target input;
- the combined archive has rank below 32 or nonidentity Gram matrix;
- a target Record content differs from the already-present target projector;
- the exact `Gamma` query is nonunitary or misidentifies a five-factor basis
  state;
- Block72's rank-four query is credited as the rank-two `Gamma` query;
- the stacked six-outcome map fails to be an isometry;
- any physical two-site primitive is non-nearest-neighbor;
- the 73-primitive coherent core differs from the ideal core on any tested
  clean-domain/background basis state;
- an occupied/replayed event changes either the quantum state or a prior
  Record;
- the packet decoder fails in any proper-cubic frame; or
- the note promotes the candidate to current NN-Admissibility compatibility,
  law, axiom, gravity source, retention, or score movement.

The runner contains independent mutations for stale authority, broken
completeness, host-selected `m`, target erasure, a non-NN edge, overwrite,
omitted resource debit, and law overclaim. Each mutation makes its named gate
fail.

## 8. No-Go Discipline gate

The only negative claims shipped are narrow:

1. the unarchived fixed-output control is not conservative on the declared
   arbitrary-target domain; and
2. current Record-only state authority does not approve this live-M2
   instrument as physical law.

Neither says that Record formation, live quantum dynamics, or TOE closure is
impossible. The full N1--N8 gate follows.

### N1 — Alternative-route enumeration and normalization

| route | normalized target / mechanism / terminal obligation | result | marker |
|---|---|---|---|
| R1 Block70 output-root/adjacent parsers | two-Record parser / replace or tag targets / executable Record law | exact local parsers exist, but target/environment disposition is not conservative | **RULED OUT BY PRIOR — CLOSED** only for the conservative live-M2 target; remains live as a nonunitary Record-only theory |
| R2 Block71 supplied-branch archive | three-target factor archive / preserve arbitrary targets / same-carrier locks | rank `32/32` archive and exact locks pass; realized branch and occurrence were supplied | **ATTEMPTED — PARTIAL** |
| R3 Block72 visible local star | exact atomic endpoint coupling / expose `m` through current state / one probability law | the two `p(b|m)` rows collide on identical Record neighborhoods when `m` is unrecorded | **ATTEMPTED — CLOSED negatively** for a Record-only controller that nevertheless reads live `m` |
| R4 Block73 pre-Recorded controller | make `m` readable first / normalized no-event+append kernel / total finite candidate | succeeds only after changing the task; pair scan has 928 original aliases and sequential order dependence | **ATTEMPTED — PARTIAL** |
| R5 live Kraus plus archive-lock | six-outcome CP instrument / project live `m,b`, archive targets, lock present projectors / one complete finite algebraic event | executed here: completeness, weights, reference preservation, coherent NN core, guarded Record update, and abstract Stinespring isometry pass | **ATTEMPTED — CLOSED POSITIVELY** only on the declared algebraic one-event domain; current NN-law qualification remains open |
| R6 unitary-only realization | Stinespring outcome carrier / preserve all information including outcome / conservative physical implementation | exact `1536 x 256` isometry exists and Kraus rank is six, but its local compilation, environment provenance, and actuality are absent | **ATTEMPTED — PARTIAL at representation; OPEN at resource/authority** |
| R7 direct current-axiom selection | read exact values/process from four axioms / no new primitive / physical law | current memo explicitly leaves dynamics, values, site/rate, update, and source downstream | **RULED OUT BY PRIOR — CLOSED** as a direct-text route |
| R8 Record-only primitive append | fundamental stochastic/nonunitary map / no live substrate obligation / physical law | compatible and not falsified; still needs exact values, process, resources, time, and source | **ATTEMPTED — OPEN** |
| R9 asynchronous/full-Z3 lift | translated local occurrences / critical-pair or stochastic-process construction / autonomous global law | premature raw overlap work was already shown aliasing/order-dependent in Block73; the new guarded algebraic candidate has not been tested globally | **ATTEMPTED — OPEN** |
| R10 current one-site NN qualification | exact covariant measures on supplied six-neighbor conditions / supported locks and matching event marginals / axiom-facing formation rule | three identical blank prior Record conditions give unequal head/root/meta lock measures here; an enlarged context, sequential law, or different instrument remains possible | **ATTEMPTED — OPEN** |

The route family is normalized by terminal obligation. A representation theorem,
one-event instrument, global process, and gravity source are not counted as the
same task. R5 retires the one-event algebraic composition only; it does not
retire NN-Admissibility matching, constitutional adoption, or TOE obligations.

### N2 — Wall-independence audit

Let

```text
W1 = live-M2 state/controller authority
W2 = fixed one-site NN measure/support and joint-marginal compatibility
W3 = exact joint instrument/hazard selection plus operation/query authority
W4 = clean-input, blank-capacity, and outcome-environment provenance
W5 = physical actuality plus atomic Record locking
W6 = global overlap process, scheduler, and physical clock
W7 = source normalization and gravity/Ward typing
W8 = internal proper-cubic action selection
```

The directional pair audit is:

| pair | left implies right? | right implies left? | exact reason |
|---|---|---|---|
| W1/W2 | no | no | a live substrate does not fix the one-site NN measures; one-site measures can be stated on a Record-only domain |
| W1/W3 | no | no | a live substrate permits many joint instruments; an abstract instrument can be written without physical state authority |
| W1/W4 | no | no | state type creates no clean packets/capacity; resources can be postulated for a Record-only law |
| W1/W5 | no | no | causal live state does not make an outcome actual; a primitive Record append need not use live M2 |
| W1/W6 | no | no | ontology supplies no overlap/time law; a scheduler can order Record-only events |
| W1/W7 | no | no | live state is not a stress tensor; a Record-derived source can be defined without live state |
| W1/W8 | no | no | tensor-product state does not choose the internal action; an action can act on possibility labels without making them causal state |
| W2/W3 | no | no | one-site marginals/support do not select joint correlations, hazard, or operations; a joint instrument can fail to match the fixed NN law |
| W2/W4 | no | no | supported measures generate no clean factors or capacity; resources do not define the one-site law |
| W2/W5 | no | no | a mathematical marginal does not make a realization actual; atomic locking does not fix the marginal measure |
| W2/W6 | no | no | a local conditional measure can be globally nonconfluent; a scheduler can host inequivalent local measures |
| W2/W7 | no | no | one-site odds/support do not type energy; a source law does not determine admissibility measures |
| W2/W8 | no | no | covariance of a measure does not select an internal representation; an action alone supplies no measure values |
| W3/W4 | no | no | normalized joint maps do not generate their inputs; resources do not select `q`, queries, or Kraus maps |
| W3/W5 | no | no | a CP instrument is mathematical without actuality/locking authority; atomic locking does not select probabilities or operations |
| W3/W6 | no | no | one joint event can be nonconfluent; a scheduler can host many inequivalent joint laws |
| W3/W7 | no | no | event odds and operations do not type energy; a source law does not determine the event instrument |
| W3/W8 | no | no | this candidate supplies a trivial action; action choice does not select hazard, queries, or instrument values |
| W4/W5 | no | no | capacity may remain unused; a primitive append may consume unspecified resources |
| W4/W6 | no | no | resources do not choose event ordering/time; a global process can run with a different resource model |
| W4/W7 | no | no | resource counting is not source normalization; a typed source need not regenerate clean inputs |
| W4/W8 | no | no | clean factors do not choose an internal representation; action choice does not create capacity |
| W5/W6 | no | no | atomic one-event locking can still be order-dependent; a scheduler does not prove same-carrier locking |
| W5/W7 | no | no | Record formation alone supplies no stress/energy value; a gravity source need not be a Record event |
| W5/W8 | no | no | atomicity does not choose action; action covariance does not make membership actual |
| W6/W7 | no | no | cadence/order does not fix source magnitude; a conserved source does not supply a stochastic process |
| W6/W8 | no | no | a scheduler does not select internal action; action selection does not produce confluence/time |
| W7/W8 | no | no | source typing can be scalar/Record-based; an internal action alone supplies no gravity normalization |

No wall is being hidden inside another. R5 closes the finite algebraic part of
W3 and the target-disposition part of W4. The exact blank-neighborhood
collision exposes rather than closes W2; the physical selections in W1--W8
remain independent.

### N3 — Hidden-wall scan

| phrase family | checked meaning in this note |
|---|---|
| `state`, `prestate`, `live`, `substrate` | live-M2 ontology is conditional; current state authority remains Record-only |
| `measure`, `project`, `Kraus`, `instrument` | mathematical CP outcomes; no physical measurement/actuality authority is inferred |
| `branch`, `select`, `realized`, `pick`, `sample` | no supplied realized branch; Kraus labels are outcomes, while physical actualization remains open |
| `m`, `matter`, `controller`, `read` | no host-selected matter bit; the instrument projects live `M`, which current Record-only authority cannot read |
| `Admissibility`, `condition`, `support`, `marginal` | possibility-domain membership is not support; the fixed one-site NN measure and its relation to the joint event remain open |
| `clean`, `zero`, `ready`, `Gamma` | four fixed input factors are explicit resources; the readiness projector does not create them |
| `blank`, `empty`, `capacity` | blank means absence from the Record map, not a clean quantum ket; three targets and the support must be Record-free |
| `archive`, `preserve`, `reference` | branch isometry preserves arbitrary target/reference information; it does not claim matter-phase preservation across outcomes |
| `reset`, `erase`, `discard`, `trace` | the executed event does none to target data; the rank-4 hostile reset is only a bounded control |
| `atomic`, `lock`, `form` | one candidate hybrid update appends three memberships at once; physical atomicity is not derived |
| `probability`, `hazard`, `rate` | `q=1/3` is a witness value and not selected or converted to physical time |
| `unitary`, `environment`, `conservative` | the event word is unitary on its branch, while full six-outcome unitarization owes a six-dimensional environment |
| `covariant`, `rotation`, `action` | spatial proper-cubic covariance is executed; internal action selection remains supplied |
| `source`, `current`, `gravity`, `Ward` | only an incidence edge is decoded; no physical source or gravity identity is promoted |
| `complete`, `closed`, `law`, `theory` | complete means the declared finite one-event instrument only; no global or adopted law is claimed |

### N4 — Residual matching

| exact source surface | inherited result | use here | unmatched residual after this note | direct execution? |
|---|---|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:47,60-61,77-83,92,116-124,183-187` | site M2 possibility, conditional distribution, Record formation/readability, Record-only state, dynamics/source exclusions | constitutional type and open-law boundary | live tensor-product state, instrument, resources, time, source | text checked from current `origin/main` |
| `scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py:444-524` | rank-32 target archive and exact same-carrier target projectors | branchwise information return and lock content | occurrence, controller, law selection | recomputed through Block72 parent certificate |
| `scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py:581-727` | packet decoder and finite-map refusal | Record/source parser and no-overwrite behavior | global parser/provenance | extended to one hybrid outcome map |
| `scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py:362-420` | 73-primitive/15-site candidate compiler | ordered coherent `U+archive` core | `Gamma`, outcome, guard, append, and physical operation authority | executed on 2,048 full basis backgrounds here |
| `scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py:437-455,629-640` | four fixed inputs and live-m/Record controller collision | explicit resource and ontology debit | genesis/renewal/state bridge | checked, not inferred away |
| `scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py:1027-1103` | six-Kraus live-M2 comparator | normalized refusal/no-event/event seed | archive and locking were absent there | composed and executed here |
| `scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py:835-925` | two-event alias/scheduler machinery | reason raw overlap was not repeated | confluence of the new guarded candidate after law selection | not executed here |
| `scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py:213-326` | six full extended Kraus maps and probability rows | closes branch/controller composition | physical actualization/selection | yes |
| `scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py:329-379` | four rank-eight archive maps and exact target locks | closes target/reference disposition | resource renewal | yes |
| `scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py:382-444` | exact six-outcome Stinespring isometry, exact rank-two `Gamma` query, and Block72 rank-four mismatch | separates algebraic realizability from compilation | NN implementation and operation authority | yes |
| `scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py:509-547` | ordered physical compiler | closes coherent-core route equality | full-instrument compilation/authority | yes |
| `scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py:601-834` | complete-state direct-sum hybrid update | closes local no-event/refusal/append/replay including quantum identity | global overlap process and guard compilation | yes |
| `scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py:837-943` | resource, blank-neighborhood marginal, and ontology certificates | exact owner decision surface | NN-law bridge, adoption, and downstream physics | yes for text/counts, not owner action |

No source is credited with a stronger terminal lemma than it proves. The new
runner composes the parents rather than importing their open conclusions as
premises.

### N5 — Rhetoric and granularity audit

The runner emits these exact resolution lines:

```text
per_element: checked six Kraus operators, all clean matter/target basis rows, coherent matter/target rows, four branch isometries, exact target projectors, and the unarchived reset control
per_site: checked five live roles, three arbitrary targets, every one of 15 coherent-core support sites, all 73 ordered core primitives, prior Records, occupancy, replay, and exact source edge
per_mode: checked both live matter basis values, three coherent matter states, four (m,b) outcomes, eight target bases, 24 proper-cubic frames, no-event, and refusal
per_block: checked Block71 archive/lock, Block72 ordered NN coherent core and rank-four query mismatch, Block73 Kraus family, the exact rank-two Gamma query, six-outcome Naimark isometry, hybrid Record update, blank-neighborhood marginal mismatch, and seven-item sufficient live-route payload
lattice_wide: checked and not executed — this is one finite candidate instrument; no homogeneous full-Z3 process, overlap confluence, capacity renewal, physical clock, or gravity coupling is claimed
```

The lattice-wide line is deliberately “checked and not executed.” Translation
reuse of a local formula is not an infinite process, and a finite event does
not prove confluence. “Conservative” is limited to arbitrary target/background
information on the declared event branch; it is not a global energy theorem.

### N6 — Partial-closure path scan

| prior or current mechanism | partial closure now available | why it does not finish TOE | reuse next? |
|---|---|---|---|
| Block71 three-target archive | exact same-carrier target/reference preservation and parser | supplied branch, no state authority/global law | yes; retained as event output layer |
| Block72 NN compiler/query | exact finite coherent `U+archive` route; separate rank-four query | rank-four query is not `Gamma`; full instrument operations and clean-resource genesis absent | yes, but only with the corrected scopes |
| Block73 Record controller | normalized finite Record-only candidate | changes live-input task; aliases and order dependence | hostile alternative/control |
| Block73 live Kraus comparator | exact normalized live-`m` outcomes | no archive/locking composition | closed by this note on one event |
| this six-outcome archive-lock instrument | one total local probability space with exact locks and direct-sum guard | current NN marginal mismatch, conditional ontology, uncompiled operations, selected values, resources, actuality, global process, time, gravity | yes; in this tested live-conservative stack it is the next overlap subject after law adoption/compilation |
| signed incidence edge | exact `Delta J + B=0` bookkeeping | not energy/stress, no normalization/cadence | later source typing |
| unarchived reset | simple Record-only implementation | fails conservative target task; may be legal under Record-only ontology | keep as ontology discriminator |

The missing algebraic composition itself is now closed; no minimality claim is
made. The next leverage is owner/type and NN-law selection, then operation
compilation and global process—not another local parser.

### N7 — Steelman and strongest surviving escape route

The hostile steelman has two strong forms.

First, the current framework may intentionally be Record-only. In that case
unrecorded M2 factors are possibilities used to describe a stochastic law, not
ontic quantum data requiring conservation. A direct nonunitary Record append
can be lawful, and demanding a rank-32 archive imports an extra conservation
principle. This criticism is correct. The rank-`4/32` control rules out only
the conservative live-target obligation, not Record formation generally.

Second, even on a live-M2 ontology this candidate may be the wrong law. The
hazard `1/3`, clean domain, trivial internal action, five-factor circuit,
readiness measurement, and atomic lock are witness choices. Other CPTP
instruments and continuous-time processes remain possible. Completeness proves
existence, not selection.

The strongest surviving positive route is therefore:

1. choose live-M2 or Record-only state ontology explicitly;
2. if live-M2, adopt or retain a quasi-local state/CP-instrument bridge;
3. supply the fixed one-site NN measures and prove support/marginal consistency
   with the chosen joint formation law, enlarging the condition explicitly if
   necessary;
4. select one exact instrument, internal action, and resource model, using this candidate as a
   tested witness rather than as authority;
5. compile `Gamma`, outcome coupling, the guard, membership append, and
   actual outcome/atomicity, including the dimension-six environment
   if unitary conservation is required;
6. enumerate only the reachable overlaps of that selected, compiled event and demand
   confluence or a locally state-derived collision rule;
7. construct the infinite/local stochastic process and physical clock; and
8. type and normalize the event output as a gravity source, then execute the
   nonlinear Ward/connection test.

If the owner instead chooses Record-only fundamental append, the live-state
and conservative-environment pieces change, but the one-site measure, exact
law, process, actuality, and source obligations remain. They require
an explicit nonunitary primitive/resource statement rather than a live quantum
implementation. Either route is viable in principle. Neither can be inferred
from the current four axioms.

### N8 — Cross-cycle echo audit

| echo | repeated issue | relation to this result | imported authority? |
|---|---|---|---|
| `RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md` | pointer nondemolition and instrument resources | same-carrier lock avoids target replacement but still needs actuality/operation authority | no; conceptual echo only |
| `RECURRENT_ENCODE_UPDATE_DECODE_SANDWICH_CYCLE883_BOUNDED_THEOREM_NOTE_2026-08-03.md` | recurrent carrier return and clean-domain reinvocation | one event does not prove the ready packet renews for depth two | no; renewal remains open |
| `docs/work_history/repo/review_feedback/CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md` | state, context, atomic law, continuation, availability, concurrency, Record, actuality, statistics | this note fills a finite atomic-law/statistics cell but not continuation/concurrency/global actuality | no; checklist echo |
| `docs/work_history/repo/review_feedback/COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md` | same interface supports inequivalent sampled laws | existence cannot select `q` or ontology | no; underdetermination echo |
| `docs/work_history/repo/review_feedback/EXACT_LAW_CONSTITUTIONAL_PLACEMENT_SCHEMA_PROBE_NOTE_2026-07-14.md` | exact law needs a constitutional referent | the candidate still needs primitive registration or retained derivation | no; placement echo |
| Block73 pair scan in the direct parent | local writes can alias and sequential recomputation differs from frozen update | raw confluence work is deferred until a selected, compiled guarded event is the subject | yes, exact parent result |
| Block71 archive control | fixed-output replacement loses arbitrary target information | reproduced here as rank `4/32`, Gram `14.97` | yes, exact parent mechanism |

The echoes reinforce the boundary; they are not stacked as hidden premises.

**Gate verdict:** PASS for the bounded positive one-event theorem and the two
narrow negative controls. No universal no-go, forced axiom amendment, physical
law selection, gravity closure, or score movement is shipped.

## 9. Reproduction

```bash
python3 scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py
```

Expected final line:

```text
TOTAL: PASS=10 FAIL=0
```

Mutation controls:

```bash
for mutation in \
  stale_axiom break_completeness host_select_m erase_targets \
  non_nn overwrite omit_resource law_claim
do
  python3 scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py \
    --mutation "$mutation"
done
```

Each mutation must produce at least one `FAIL` and a nonzero final failure
count.

## 10. Boundary

Established here:

- one normalized six-outcome live-M2 CP instrument;
- no supplied realized branch and no host-selected matter bit;
- exact clean-basis and coherent-input branch probabilities;
- branchwise arbitrary target/reference preservation;
- same-carrier three-projector atomic Record locks;
- exact rank-two `Gamma` query and exact six-outcome Stinespring isometry,
  both explicitly uncompiled;
- the exact mismatch between Block72's rank-four query and this rank-two
  `Gamma` query;
- ordered 73-primitive NN coherent-core implementation on arbitrary finite
  backgrounds;
- complete-state direct-sum refusal on occupied/replayed supports;
- local refusal, no-event, replay, permanence, covariance, packet decode, and
  signed-edge bookkeeping; and
- the exact identical-blank-neighborhood/unequal-lock-marginal gap; and
- exact resource, ontology, and seven-module live-route localization.

Not established here:

- live M2 as approved physical state or readable controller;
- compatibility with the current fixed one-site NN Admissibility law;
- selection of this instrument, its hazard, clean domain, or internal action;
- nearest-neighbor implementation of `Gamma`, outcome coupling, Stinespring
  environment, direct-sum guard, or Record membership append;
- clean resource/capacity genesis or renewal;
- physical outcome actuality or atomicity;
- a homogeneous full-`Z^3` law, overlap confluence, or infinite process;
- physical time, rate, stress-energy, source normalization, nonlinear Ward or
  connection identity, or gravity;
- an axiom edit or approved-primitive registry entry;
- audit retention, obligation retirement, or TOE percentage movement.

## 2026-09-08 provenance correction

The original commit/parent hashes remain immutable historical identities.
They do not require the extracted current-main candidate to retain the raw
branch ancestry. Gate A separately verifies the selected current parent and
all declared proof/runtime inputs, including the current constitutional
files. Corrected parent source is pinned bottom-up; historical receipts are
not substituted for current source or scientific acceptance. The supplied
finite construction and its physical-law boundaries above are unchanged.
