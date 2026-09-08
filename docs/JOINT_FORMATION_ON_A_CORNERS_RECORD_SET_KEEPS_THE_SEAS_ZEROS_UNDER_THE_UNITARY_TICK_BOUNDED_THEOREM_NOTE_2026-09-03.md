---
claim_id: joint_formation_on_a_corners_record_set_keeps_the_seas_zeros_under_the_unitary_tick_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite cube encoding/Born calculation for five explicitly supplied formation units, the 17 declared schedules, three between-event rules, 40 lexicographic orders per U2/U3/U4 and four declared dwell times. Original T1-T5 tables remain finite numerical observations. U2 preserves all 256 cancellation zeros in THREE of FOUR declared orders, not all. Two named schedules match the sea at tested times; all-time equality requires exact eigenvector behavior at every reachable node. Relaxation and order-dependence conclusions concern the named finite menus only. Relative-probability branches <=1e-12 are pruned with actual discarded mass reported. No physical tick or formation unit is derived."
upstream_dependencies: []
runner: scripts/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.py
---

# Joint corner formation: finite schedules that preserve or lose the sea's zeros

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; formal audit is deferred until a solid TOE.
**Status:** current conditional source, awaiting independent correction confirmation. No applied audit status is changed.
**Primary runner:**
[`scripts/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.py`](../scripts/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.txt`](../logs/runner-cache/joint_formation_corner_record_set_keeps_sea_zeros_check_2026_09_03.txt)
**Premises:** the mathematical model is redeclared below. The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) constrain its interpretation; the supplied Born, Fock, encoding and formation choices are not derived from them.

`A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_..._2026-09-03.md` (open PR #7895) lets **one edge site at a time** register, and finds that the sea's own
forbidden patterns do not survive. On 2026-09-03 the owner put a different reading of the same clause: **"the whole neighbourhood generally has to move together because it is its own
shared condition"**. Records are permanent, so at the level of formation that sentence is a statement about the **unit** in which records form: a formation event registers a whole
neighbourhood's worth of records **together**, as one event. This note takes that as a stipulation under test. It declares five units of formation on the same cube in the same sector, runs them against the same three between-event rules, and reports what follows. The answer turns on the **shape** of the unit, not its size.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on one named cluster -- the 4096-dimensional record space of the 2x2x2 cube in the staggered sector, whose 128-dimensional code space is the even-N space -- for five stipulated units of record formation and three stipulated between-event rules. The unit and order combinatorics of B1-B2 are exact integer and F2 statements; the sea's zero census is exact F2 combinatorics on a zero set identified from the Born diagonal at 1e-12. The formation trees are deterministic and not sampled, but relative branches <=1e-12 are omitted and their total weighted mass is reported. Each node's relaxed state or evolution comes from a diagonalisation, so those lines are deterministic double-precision evaluations of exactly specified quantities and are tagged [numerical] with their thresholds. There is no seed anywhere in the runner and no Monte Carlo section."
trace_class: frontier_discovery
target_claim_id: joint_formation_on_a_corners_record_set_keeps_the_seas_zeros_under_the_unitary_tick_bounded_theorem_note_2026-09-03
target_blocker_text: "The finite supplied model does not derive its physical law, state, readout or formation dynamics."
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Confirm the corrected conditional source independently; formal audit is deferred until a solid TOE. Physical suppliers and limiting questions remain open."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below plus the open item, exactly the runner's check groups `A`-`G`: the setting and the sea's zeros (`A`); the stipulated units and
orders (`B`); `T1` (`C`) the control; `T2` (`D`) the unitary tick; `T3` (`E1`-`E3`) the mechanism, with the open item recorded at `E4`; `T4` (`F`) relaxation; `T5` (`G`) order
dependence. Groups `A1`, `A2`, `B1` and `B2` are **exact**: symplectic Pauli algebra with phases mod `4`, and integer combinatorics on the cube's own adjacency. `A4` is exact `F2`
combinatorics on a zero set identified from the Born diagonal at `1e-12`. The rest are **deterministic double-precision evaluations** of exactly specified quantities at the stated
thresholds. Nothing is sampled: each distribution is a floating-point product over retained tree branches, with omitted probability accounted, every order is written out in the runner, and there is **no seed anywhere** and no Monte Carlo section.

## Imports and authority

Historical quotations and PR references below refer to the original dated sources identified in `.claude/science/sea-corner-corrections-20260908/CORRECTION_HISTORY.md`; they do not assert that a branch is still open or that its current source is accepted. The finite definitions used in the proofs are restated here. The current minimal-axiom memo is a live interpretation boundary, distinct from those quotations.

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggered link signs, Lueders conditioning and the total-variation distance
are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's relations included. No observational value, no fitted number and no
framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight: `A_RELAXATION_TICK_IS_WELL_POSED_..._2026-09-03.md` (open PR #7895 -- the site-wise
result this note extends, and the source of the `M_R` rule, the `Pi/deg` tie-break, and the zero census reproduced at `A4`); `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_..._2026-09-03.md`
(open PR #7876 -- Model A and `H_R`); `DETERMINANTAL_RECORD_STATISTICS_ON_THE_HALF_FILLED_SEA_..._2026-09-02.md` (PR #7883 -- the sea's Born statistics, the same `eta_ks`);
`EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_..._2026-09-02.md` (PR #7842 -- the selection-rule zeros from the dictionary side);
`SUPPORT_CONDITIONS_CONFINE_RECORD_GROUPS_..._2026-09-03.md` (PR #7891 -- the owner's neighbourhood mechanism);
`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_..._2026-09-02.md` (PR #7858 -- the same cube and encoding); and `MINIMAL_AXIOMS_2026-06-29.md`, from which the axioms in
"Setting" are quoted verbatim. This note cites no grade of any and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." "No site is privileged." The memo names a physical lattice; the cube below is a supplied graph,
so "edge site" and "corner" have their graph meanings. **Qubit / Site Possibility**: "Each site has a domain of local possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the
probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Two reading notes, interpretive and non-governing, are the hinge of
this note and are quoted with it. (2): "Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; **it does not
supply the formation site, probability, or rate.**" (3): "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure; Record locks a supported realization."

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."
"Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded clause is used anywhere.
The **record ontology** is used as declared: a record at an edge site **registers** a value there; it does not report one the site already carried. Reading note (2) is what makes this
note's subject a free choice: the axioms supply no formation site and no rate, so **the unit in which records form is not given** -- this note stipulates five of them and reports what each does. Reading note (3) is what makes a lost zero a real cost: "admissible" is the *support* of the odds, so a rule giving a pattern nonzero odds has made that pattern admissible.

**Reading, not theorem.** Records are permanent, so "the whole neighbourhood together" cannot be about anything happening to records already present. Read at the level of formation it
says: the records of one neighbourhood **form together**, in one event, because the neighbourhood is one shared condition. That is the reading tested below, and it is a stipulation.

## The stipulated formation model, declared in full

Seven choices, all made here, none derived. A lane proposing a different unit or a different between-event rule inherits the obligations of `T1`-`T5` and none of these choices.

1. **The object before any record** is the sea: the ground state of `H` in the code space (see "Definitions"). 2. **The unit of formation.** Five **unit types** are declared, each a set of edge sites whose records form together as one event:

   | type | what it is | count | size |
   |---|---|---|---|
   | `U1` | a single edge site | `12` | `1` |
   | `U2` | the three edges at one corner `v` -- **a corner's own record set** `star(v)` | `8` | `3` |
   | `U3` | the four edges of one face | `6` | `4` |
   | `U4` | the **closed corner star** of `v`: every edge incident to `{v} u N(v)`, which on this cube is `E \ star(7 - v)` | `8` | `9` |
   | `U5` | all twelve edge sites | `1` | `12` |

3. **Which unit forms next.** The next unit in a **declared order**, a permutation of that type's unit list. **Sixteen** are declared for `U1`-`U4`, four per type, written out in the
   runner, plus `U5`'s single order; a further declared **lexicographic sweep** of the first `40` permutations of the unit list is run for `U2`, `U3` and `U4`. None is drawn at random.
4. **What forms.** Only the **not-yet-recorded** sites of that unit, and they form **together**: one event registers all `m` of them, with the odds of the current pre-record object on
   the `2^m` joint outcome patterns.
5. **Between formation events**, one of three **declared rules** runs:
   * **(a) `M_R`** -- the object is replaced by the ground state of `H` restricted to the record-consistent subspace, with the normalised projector `Pi/deg` where that ground space is
     degenerate. This is PR #7895's tick, one way of making the vacuum panel's candidate wording -- "Between records, the lattice settles into its lowest-energy arrangement" --
     definite. That wording is a candidate, not axiom text, and is not called wrong here; what is reported is what `M_R` does.
   * **(b) `A`** -- the unitary `exp(-i tau H_R)`, `tau = 0.5`, PR #7876's Model A: the lattice's law simply runs on.
   * **(c) `L`** -- nothing at all, pure sequential Born. This is the control.
6. **Conventions.** A unit with no unrecorded sites is **skipped**: no formation event and no between-event rule. The between-event rule after the **last** event is not applied; it
   cannot change the final odds.
7. **Permanence.** Records never change; the run continues until all `12` sites carry records, so each run ends on one of the `4096` record patterns.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is `P0`-`P5`. `P0` (declared here): the cube, the edge-site
qubits, the encoding, the staggered sector, the parity dictionary, and the seven stipulated choices above, together with the setting and zero census of `A` and the unit/order
combinatorics of `B`. `P1` (`C`): the control. `P2` (`D`): the unitary tick. `P3` (`E`): the mechanism, and the open item. `P4` (`F`): relaxation. `P5` (`G`): order dependence.

## Definitions

The **cube** is the `2x2x2` cube graph, corner `s = 4a + 2b + c`, `8` corners, `12` edge sites, `6` faces. One qubit sits on each **edge site**, neighbours ordered by index:

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_v  = prod of the Z's on the edges incident to v,     S_f = the ordered product of the A's around a face f,
T_ij = (i/2) A_ij (B_i - B_j),     H = -t sum_e eta_e T_e,  t = 1,     star(v) = the edges incident to v.
```

`eta` are the **Kawamoto-Smit staggered link signs** `eta_x = 1`, `eta_y = (-1)^x`, `eta_z = (-1)^(x+y)`, the same `eta_ks` as PR #7883; their product round every one of the six faces
is `-1`, the all-minus (**pi-flux**) sector. The **code space** is all six `S_f = +1`, of dimension `2^12/2^5 = 128`; it encodes the even-`N` Fock space. The full 4096 edge-record carrier has additional loop sectors; it is not this code space, and the
**sea** is the ground state of `H` there. A **record** at an edge site registers a `Z`-value, so a finished set of records is a vector in `F2^12`, one of `4096` **patterns**; the
**parity dictionary** is `n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2`, `N = sum_v n_v` and the **readable charge** is `Q = N - 4`. `H_R` is `H` restricted to the subspace
consistent with the records so far, which is the sum of hops on **unrecorded** sites: every hop flips precisely its own edge bit, so compression kills exactly the recorded-edge terms. `TV` is total variation, `(1/2) L1`. A
**cancellation coset** is one of the eight `32`-label sets of the sea's non-charge zeros, indexed by the closed corner star carrying it.

## The setting and the sea's zeros, reproduced

`[exact]` The superfast relations `R0`-`R4` hold pair by pair, the face group carries no `-I`, `k = 5`, the code dimension is `128`, the flux is `-1` on all six faces, and every hop
term has Pauli `X`-part exactly one edge qubit, so `P_S H P_S` is the sum of the hops on unrecorded sites. `[numerical, 1e-11]` The code space is `H`-invariant to `2.8e-17`; the sea
has `E = -6.928203230276 = -4 sqrt 3`, is non-degenerate, has gap `3.464101615138 = 2 sqrt 3` and is sharp `N = 4` (mass off `N = 4`: `2.0e-31`). `[exact, 1e-12 zero read]` The
**target** every rule below is checked against is the sea's own registration: support `1984 = 62 x 32`, and `2112` zeros `= 1856` **charge zeros** (`N != 4`) `+ 256` **cancellation
zeros**, whose eight corner-occupation patterns are **exactly** the eight closed corner stars `{v} u N(v)`, `32` labels each; the smallest nonzero sea probability is `2.17e-04`.
`[exact]` The five unit types have counts `12, 8, 6, 8, 1` and sizes `1, 3, 4, 9, 12`, and `cstar(v) = E \ star(7 - v)`: **a closed corner star's complement is the antipode's own
record set.** The sixteen declared orders plus `U5`'s cover all twelve sites, with formation events `U1 [12,12,12,12]`, `U2 [7,7,4,6]`, `U3 [4,4,5,5]`, `U4 [3,3,2,3]`, `U5 [1]` --
means `12`, `6.00`, `4.50`, `2.75`, `1`. `[numerical, 1e-12]` What **one unit's own joint odds** already forbid: `0` charge and `0` cancellation zeros at **every** `U1`, `U2` and `U3`
unit, while every `U4` closed star forbids `448` charge and `64` cancellation zeros, and `U5` forbids all `1856 + 256`.

## Theorem 1 -- the control: with nothing between events, the unit and the order do not matter

**Conclusion.** `[numerical, 1e-15]` Under rule (c) all `17` declared schedules give support `1984` and **are** the sea's registration: `TV` to the sea at most `7.4e-16`. Between the
four declared orders of each proper unit type the maximal pairwise `TV` is `4e-16` (`U1`), `4e-16` (`U2`), `2e-16` (`U3`), `8e-17` (`U4`). `[numerical, 1e-12]` And `U1` reproduces PR
#7895 exactly: under rule (b) at `tau = 0.5` its support is `2240`, all `1856` charge zeros are kept, `0` of the `256` cancellation zeros are, and `TV` to the sea is
`0.324925160534` at the identity order, at all four declared orders alike.

**Proof.** Seventeen deterministic trees under rule (c) and four more under rule (b), keeping branches with relative probability greater than `1e-12`. The current runner records weighted discarded mass at every skipped branch, and checks retained plus discarded mass against one to `1e-10` for every actual run. This is probability accounting, not an exact-arithmetic whole-tree claim. Joint conditioning in the `Z` basis commutes with itself, so the control's order independence is expected and is checked rather than assumed.

**Reading, not theorem.** This is the control the rest of the note needs: with the lattice's law switched off between events, forming records one at a time and forming them a whole
neighbourhood at a time give the same odds, and give the sea's odds. So every difference below is caused by what runs **between** formation events, not by the joint formation itself.

## Theorem 2 -- under the unitary tick, a corner's record set keeps the sea's forbidden patterns

**Conclusion.** `[numerical, 1e-12]` Under rule (b) at `tau = 0.5`, cancellation zeros kept over the four declared orders are `U1 [0,0,0,0]`, `U2 [256,256,256,0]`, `U3 [0,0,0,0]`,
`U4 [128,128,256,128]`, `U5 [256]`: **all `256` at three of the four corner orders, none at any face order**, with all `1856` charge zeros kept everywhere. In the declared
lexicographic sweep of the first `40` permutations, `4` of `40` `U2` orders keep all `256`, `U3` keeps `0` throughout and `U4` `128` throughout. Two schedules reproduce the sea
**to the reported numerical tolerances**: `U2 evenfirst` -- the four **disjoint** corner record sets `star(0), star(3), star(5), star(6)` -- at `TV = 1.11e-15`, and `U4 antipodal` -- `cstar(0)` then `star(7)` --
at `TV = 7.02e-16`, both on the sea's own support `1984`. Both do it at every `tau` tested, `0.1`, `0.5`, `1.234567`, `2.0`, while `U1 identity` and `U3 identity` keep `0` of the `256`
at every one of them.

**Proof.** Retained-branch formation trees as in `T1`, one per (unit type, order, rule) and four more per schedule for the `tau` sweep; the zero census of each final distribution is read at
`1e-12` against the sea's zero set and split by cancellation coset. The `40`-permutation sweep is `itertools.permutations` on the sorted unit list, a literal enumeration with no seed.

**Reading, not theorem.** Letting the three records at one corner form together, with the lattice's law simply running on in between, keeps all 256 forbidden patterns at **three of the four declared U2 orders**, while the fourth loses them and site-wise formation loses them -- and for the right sequence of corners the records come out exactly as the sea itself would register them, at the four declared gap lengths. The four edges of a face are a
**larger** unit and keep none of them.

## Theorem 3 -- the mechanism: a jointly formed corner set leaves the sea at rest under what remains of the law

**Conclusion.** `[numerical, 1e-9]` After a corner's record set forms jointly, the Born-conditioned sea already lies in the restricted ground space (`G = <psi|Pi_0|psi> =
1.000000000`, `deg = 1`) and passes the **`H_R` eigenvector residual test** at `8` of `8` outcomes, with `TV(|psi|^2, Pi/deg) = 0`: relaxation is the **identity** there and the unitary is a
global phase. The closed corner star has the same property at `448` of `448` outcomes (`G = 1.000000000`), but its ground space is `2`-fold degenerate, so the `Pi/deg` tie-break gives
a rank-`2` mixture (`F = 0.636894534`, `Fq = 0.500`). A single edge (`G = 0.962606706`, `0/2`) and a **face** (`G = 0.890431430`, `0/16`) are eigenvectors at no outcome at all, though
the face is the larger unit. `[numerical, 1e-9]` Along both exact-sea schedules the conditioned state is an `H_R` eigenvector at **every** node a between-event step follows --
eigen-weight `1.000/1.000/1.000` (`U2 evenfirst`) and `1.000` (`U4 antipodal`) -- against `0.000` at each of the first seven levels for `U1 identity` and `0.000/0.079/0.142` for
`U3 identity`.

**Proof.** For each first-unit outcome the conditioned sea is formed, `H_R psi` is computed directly from the block's real skew form `H = i M` without any diagonalisation, and
`psi` is called an eigenvector when `max |H_R psi - lambda psi| < 1e-9` with `lambda = Re<psi|H_R|psi>`. `G` is `deg` times `<psi|Pi_0/deg|psi>` from the block ground projector, `F` is
the classical fidelity `(sum sqrt(p q))^2` between `|psi|^2` and `diag(Pi_0)/deg`, and every figure is weighted by the outcome's own odds. The stagewise profile repeats the test at
each node of the rule-(b) tree, weighted the same way.

**Reading, not theorem.** This is why the corner works and the face does not. Once a corner's own records are all present, what is left of the law is a Hamiltonian for which the
conditioned sea is already at rest: running it forward changes nothing, and settling it to the lowest arrangement changes nothing either, because it is already there. The face leaves
the conditioned sea off its own ground state, and the lattice's law then carries odds into patterns the sea never registers. Shape, not size.

## Theorem 4 -- the declared proper-unit relaxation menus lose zeros

**Conclusion.** `[numerical, 1e-12]` Under rule (a) the cancellation zeros kept over the sixteen declared orders are `U1 [0,0,0,0]`, `U2 [0,0,64,0]`, `U3 [0,0,0,0]`, `U4 [64,64,64,64]`,
and over the declared sweep at most `64`; only `U5` -- all twelve sites at once -- keeps all `2112` zeros. The `64` that do survive under `U4` are **exactly the first-formed star's
coset and its antipode's**, at all four declared orders: `cstar(v)`'s nine edges fix the corner parities on `{v} u N(v)`, and in the sharp-`N = 4` sea both all-occupied and all-empty
are forced to zero, so a `U4` unit's own joint odds already vanish there. Later stars' cosets go to the intervening relaxation. The same "formed first, therefore kept" reading does
**not** transfer to the corner unit: under `U2 evenfirst`, whose first unit is `corner0`, the surviving cosets are `1` and `6`, **not** `0` -- consistent with a `3`-site unit's own
joint odds vanishing on none of the sea's zeros. And the readable charge stays smeared: `P(Q = 0)` never reaches `1` below `U5` -- best `0.841145833` at `U3`, the four-site face,
against `U4`'s `0.666666667 .. 0.750000000` -- while `U5` gives exactly `1.000000000`.

**Proof.** Retained-branch trees again, one per (unit type, order) under rule (a) plus the `40`-permutation sweep for `U2`, `U3`, `U4`; the surviving cancellation zeros are broken out per
cancellation coset and compared, coset by coset, with the antipodal pair of the schedule's first unit. The charge law is read off each tree against the parity dictionary.

**Reading, not theorem.** Settling to the lowest-energy arrangement between formation events does something definite, and what it does here is not repaired by forming records
together: in every tested proper-unit schedule it leaves at least three quarters of the sea's forbidden patterns admissible, and it leaves the readable charge spread out. The
panel's candidate wording and the corner unit are two separate choices, and on this cluster they do not combine.

## Theorem 5 -- positive order dependence in the declared proper-unit menus

**Conclusion.** `[numerical, 1e-12]` Max pairwise `TV` over the four declared orders, rules (a)/(b): `U1 0.602777777778 / 0.619386368116`, `U2 0.461024273 / 0.286110110`,
`U3 0.562500000 / 0.506673787`, `U4 0.250000000000 / 0.076616282355`, against exactly `0` for the control. Each is a **lower bound** on the spread over all orders of that unit list.
The spread is smaller at `U4` than `U1` and positive in each declared proper-unit menu; it is **not monotone**: the four-site face `U3` is more order-dependent than the three-site corner record
set `U2` under both rules. Formation events per unit type average `12`, `6.00`, `4.50`, `2.75`, `1`.

**Proof.** Six pairwise `L1` sums per unit type and rule over the trees of `T2` and `T4`; the event counts are the schedule lengths, which are deterministic because which unit
registers which sites does not depend on the outcomes.

**Reading, not theorem.** Every declared run finishes on the same twelve sites, but the probabilities depend on the schedule within each tested proper-unit menu. A larger unit does not monotonically reduce that dependence. No axiom here requires schedule-independent probabilities under intervening dynamics.

## Open, not claimed

Under rule (b), `U2 identity` and `U2 reverse` finish with all `256` cancellation zeros although the propagated state **visits** `192` cancellation-coset labels at intermediate nodes
(the union of the state's `Z`-support over every node of the tree is `2176`, against the sea's `1984`). The union never leaves the `N = 4` sector for any schedule, and for the two
exact-sea schedules it never leaves the sea's `1984` labels at all. Why the visited amplitude never reaches a leaf with a matching record prefix is **not** explained here: the
eigenvector mechanism of `T3` covers the two exact-sea schedules and no more. This is recorded as an observation, and anyone landing on it should either derive it or keep it stated.

## Corollary -- finite schedules and an exact conditional mechanism

1. U2 keeps all 256 cancellation zeros in the identity, reverse and evenfirst schedules; U2 antipodal keeps zero. The face schedules tested keep zero. These are schedule-dependent results, not a theorem for every corner ordering.
2. The two named exact-sea schedules agree numerically at `tau=0.1,0.5,1.234567,2.0`. If the conditioned vector is exactly an `H_R` eigenvector at every reachable node, any dwell time changes it only by a phase; induction with the commuting Born projectors then gives all-time equality. The numerical residual tests support this mechanism on the named cube schedules; finite tolerance and pruned branches alone are not an exact certificate for all nodes.
3. The relaxation failures and nonzero order spreads concern only the declared unit/order menus, the stated tie-break and time choices. They are not a no-go for all proper units or all intervening rules.
4. The actual lexicographic keys are bound to the first 40 distinct permutations for each of U2/U3/U4 under both A/MR. A one-permutation run cannot stand in for the 240 executed cases. The original 4/40 U2 preservation count and U4 value 128 are asserted, not inferred from a positive hit.
5. The suggested formation sentence in the historical packet remains a proposal. Neither the unit, Born law nor Hamiltonian evolution is supplied by the current Record axiom. The parent campaigns remain outside this source confirmation.

## Reading, not theorem -- the whole thing in plain words

On this supplied cube model, both the shape of a jointly measured set and the chosen ordering matter. Three of four corner orders preserve the zeros and one does not. Two named schedules agree with the sea at the tested dwell times, with an eigenvector mechanism explaining what an exact all-time proof would require. The calculation does not establish a physical formation rule.

## Interfaces named for other lanes, not settled here

- **Larger clusters.** Whether a corner's record set keeps this property on the `3x3x3` cube, on periodic boundaries, or in the thermodynamic limit is outside this note; the sea's
  degeneracy and the corner-star census both depend on the cluster.
- **The fine lattice.** The cube here is a supplied coarse graph; its embedding as a physical emergent cluster is not established; nothing is said about the unit of formation on the physical sites themselves.
- **The formation rate.** How often a unit forms, and which one forms next, is stipulated here as an order and is not derived; reading note (2) says the axioms supply neither.
- **The open mechanism.** The non-disjoint corner schedules of `T2` that keep all `256` zeros are not covered by `T3`.
- **The exact-sea schedules on tori.** Whether a minimum vertex cover of the cluster graph plays the role `U2 evenfirst` plays here, on other graphs and on periodic boundaries, is
  named and not computed.

## Remaining live routes

1. Whether some between-event rule other than the three declared here -- a partial relaxation, or a dissipative generator with the sea as its stationary object -- keeps the zeros at a
   unit smaller than the whole cluster. Only the three ends are computed here.
2. Whether an exact eigenvector condition at all reachable nodes characterises schedules preserving the full sea law, or whether other mechanisms preserve only its zeros. First-unit stationarity alone is not a criterion for an entire schedule.

## Executable claim block

The canonical machine-bound restatement of the five theorem conclusions and the open item.

```text
setting: qubits on the 12 EDGE sites of the 2x2x2 cube graph (8 corners, 6 faces); ordinary (commuting) composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading notes (2) and (3)
encoding: A_ij = X(edge ij) * Z's ordered before it at both endpoints; A_ji = -A_ij; B_v the Z's incident to v; S_f the ordered four-A face loop; T_ij = (i/2) A_ij (B_i - B_j)
law: eta = Kawamoto-Smit staggered signs, flux -1 on all six faces; H = -sum_e eta_e T_e, t = 1; code space all six S_f = +1, dim 128 = the even-N space; the sea = its ground state, E = -4 sqrt 3, non-degenerate, gap 2 sqrt 3, sharp N = 4, Born support 1984 and 2112 zeros = 1856 charge + 256 cancellation on the 8 closed corner stars x 32
dictionary: n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2; N = sum_v n_v; readable charge Q = N - 4
formation_model: STIPULATED, seven declared choices -- (i) start from the sea; (ii) five UNITS U1 edge / U2 star(v) / U3 face / U4 closed corner star (9 edges, = E \ star(7-v)) / U5 all twelve; (iii) the next unit in a DECLARED order, 16 declared for U1-U4 plus U5's, plus a declared 40-permutation lexicographic sweep for U2, U3, U4; (iv) only the unrecorded sites of that unit register, and they register JOINTLY with the odds of the current pre-record object on the 2^m patterns; (v) between events one of three DECLARED rules -- (a) M_R relaxation with the Pi/deg tie-break, (b) A = exp(-i tau H_R) at tau = 0.5, (c) L nothing; (vi) a unit with no unrecorded sites is SKIPPED and the rule after the last event is not applied; (vii) records permanent, run to 12. No seed anywhere; every order written out in the runner
setting_and_zeros [exact; 1e-12 zero read]: R0-R4 pair by pair, no -I in the face group, k = 5, code dim 128, flux -1 on all six faces, every hop term has X-part exactly one edge qubit; E_sea = -6.928203230276 = -4 sqrt 3, deg 1, gap 3.464101615138, mass off N = 4 is 2.0e-31; sea support 1984 = 62 x 32, 2112 zeros = 1856 charge + 256 cancellation = the 8 closed corner stars x 32; unit counts 12/8/6/8/1 and sizes 1/3/4/9/12; cstar(v) = E \ star(7-v); events per order U1 [12,12,12,12], U2 [7,7,4,6], U3 [4,4,5,5], U4 [3,3,2,3], U5 [1]; one unit's own joint odds forbid 0 + 0 at every U1, U2, U3 unit, 448 + 64 at every U4 star, 1856 + 256 at U5
T1_control [numerical, 1e-15]: rule (c) gives support 1984 and TV <= 7.4e-16 to the sea at all 17 declared schedules, with max pairwise TV 4e-16 (U1), 4e-16 (U2), 2e-16 (U3), 8e-17 (U4); [numerical, 1e-12] U1 under rule (b) reproduces PR #7895 -- support 2240, 1856 charge zeros kept, 0 of 256 cancellation kept, TV 0.324925160534
T2_unitary [numerical, stated tolerances; declared schedules only]: cancellation zeros kept, rule (b), four declared orders: U1 [0,0,0,0], U2 [256,256,256,0], U3 [0,0,0,0], U4 [128,128,256,128], U5 [256], all 1856 charge zeros kept everywhere; lexicographic-40 sweep 4/40 for U2, 0 for U3, 128 constant for U4; U2 evenfirst TV 1.11e-15 and U4 antipodal TV 7.02e-16, both on support 1984, at every tau in {0.1, 0.5, 1.234567, 2.0}, while U1 identity and U3 identity keep 0 of 256 at every tau
T3_mechanism [numerical, 1e-9]: after star(0), G = 1.000000000, deg 1, H_R eigenvector residual test passed at 8/8 outcomes, TV(|psi|^2, Pi/deg) = 0; after cstar(0), G = 1.000000000 at 448/448, deg 2, F = 0.636894534, Fq = 0.500; after one edge G = 0.962606706 at 0/2; after one FACE G = 0.890431430 at 0/16; eigen-weight 1.000 at every node a between-event step follows for U2 evenfirst and U4 antipodal, 0.000 at the first seven levels for U1 identity, 0.000/0.079/0.142 for U3 identity
T4_relaxation [numerical, stated tolerances; declared schedules only]: cancellation zeros kept, rule (a): U1 [0,0,0,0], U2 [0,0,64,0], U3 [0,0,0,0], U4 [64,64,64,64], sweep at most 64, U5 all 2112 zeros; the 64 under U4 are exactly the first-formed star's coset and its antipode's at all four declared orders; under U2 evenfirst the survivors are cosets 1 and 6, NOT the first-formed corner0's coset 0; P(Q = 0) best 0.841145833 (U3), U4 0.666666667 .. 0.750000000, U5 exactly 1
T5_order [numerical, 1e-12]: max pairwise TV over the four declared orders, rules (a)/(b): U1 0.602777777778/0.619386368116, U2 0.461024273/0.286110110, U3 0.562500000/0.506673787, U4 0.250000000000/0.076616282355, control numerically 0; a LOWER BOUND over all orders of each unit list; not monotone -- U3 > U2 under both rules; mean events 12, 6.00, 4.50, 2.75, 1
OPEN_not_claimed [numerical, 1e-11]: under rule (b) the node-support union never leaves N = 4, and is 1984 for both exact-sea schedules, but U2 identity visits 192 cancellation-coset labels at intermediate nodes (union 2176) and still finishes with all 256 zeros; not explained here
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
historical_runner_result: PASS=24 FAIL=0
```

## Proof boundary

Every exact identity or finite numerical observation above concerns **one finite cluster**, the `2x2x2` cube graph, in **one flux sector** (all-minus, the Kawamoto-Smit staggered signs) at **one filling** (the
half-filled sea, `N = 4`). Nothing is claimed for larger clusters, periodic boundaries, infinite lattices, other sectors, other fillings, or any law family other than the one in
"Definitions". The law is **designed**, not derived: the encoding is chosen so that the Majorana relations `R0`-`R4` hold, the face constraints make that consistent, and the parity
dictionary is one readout map among many, with no uniqueness claimed for either.

**The formation model is stipulated in full and derived from nothing.** The five unit types, the sixteen declared orders and `U5`'s, the declared `40`-permutation lexicographic sweep,
the three between-event rules, the `Pi/deg` tie-break, the skip-an-already-recorded-unit convention, `tau in {0.1, 0.5, 1.234567, 2.0}`, and the joint-odds formation step itself are
all declared here, not taken from any axiom. Reading note (2) is explicit that the axioms supply no formation site, probability or rate; they supply no unit of formation either, and
this note supplies five alternatives for conditional calculation, with no framework adoption. The owner's statement is quoted as the **question** this note answers on one cluster, read at the level of formation because records
are permanent; it is not treated as axiom text and nothing here settles it. The vacuum panel's candidate wording is likewise a candidate, is not called wrong anywhere above, and
`M_R` is reported as one way of making it definite: what is stated is what each declared rule does.

**Nothing here says what the framework's tick is**, and nothing here forecloses any unit, rule or rate. The order-dependence figures of `T5` and the `4/40` and `0/40` counts of `T2`
and `T4` are maxima and counts over **declared finite sets** -- sixteen orders and forty permutations, all written out in the runner -- and are lower bounds on the spread over all
orders of each unit list, labelled so everywhere they appear. Every line not tagged `[exact]` is a **deterministic double-precision evaluation** of an exactly specified quantity at
the stated threshold: the retained branches are enumerated with no sampling, and omitted probability is accounted, but each node's relaxed object or evolution comes from a diagonalisation, against which no exact
rational value stands. There is **no seed anywhere** in this note or its runner and no Monte Carlo section. No absolute unit appears anywhere, no axiom text is amended, extended,
reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

This is a corrected conditional source, not an applied audit verdict. The original 2026-09-03 notes, runner bodies, caches and all 108 original check identities are preserved by the dated correction record outside active documentation discovery. Its original Git heads recover the unchanged historical bodies. Numerical tables above retain their historical values unless a correction is expressly identified. The current cache records a genuine run of the final source; a zero exit or fresh fingerprint is not a proof of its scientific claims.

Each primary is standalone and declares its own note and the current minimal-axiom memo as mutable inputs. The memo is an interpretation boundary, not a derivation of the supplied Hamiltonian, state, Born rule, coarse-to-fine map or permanent Record formation. Historical parent titles and quotations are attribution only; their science has not been accepted here. No parent campaign is imported. Independent source confirmation and the coordinator's current-main mechanical gates remain separate; formal audit is deferred until a solid TOE.

The actual omitted-mass receipts in the final cache qualify every numerical tree row. In particular, `H=iM` with real skew `M` implies `H^2=MM^T`; the former negative sign in three docstrings was a label error, while the implemented matrix was already correct.
