---
claim_id: the_partial_configuration_readout_is_injective_on_the_3_torus_every_law_is_visible_to_records_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "The covariant label-equivariant support tables number 3^24. A partial configuration assigns open, 0 or 1 to the sites of an L^3 torus and is admissible under a table when every recorded site's value lies in the support the table names for that site's ternary neighbour profile; this reduces exactly to a 48-bit demand mask, and mask(c) contained in a bit set S is a local condition on 7-site stars, encoded here as CNF with one-hot ternary site variables and forbidden profile codes as clauses, the demanding site pinned at the origin by a verified translation x 24-rotation x flip reduction. On the 3^3 torus the digit-confined question is decided completely for all 24 flip-pairs and all 3 targets: 50 satisfiable with witness masks re-verified by two independent code paths, and 22 unsatisfiable, each decided by a complete backtracking enumeration carrying no solver and, where a solver is present, by three solvers with DRUP refutations. Pairs 11, 16 and 17 admit no digit-confined mask there; pair 23 does, by a complete 27-record configuration; the per-digit reading is 17 exact, 4 to a binary choice, 3 blind, per-digit fibre 432 = 3^3 x 2^4. A sufficiency criterion for injectivity, proved in full in the note, is closed against a declared pool of 3117 masks each re-verified from its explicit witness configuration: 96 requirements decided twice, so the readout separates all 3^24 = 282,429,536,481 tables on the 3^3 torus and every fibre is a singleton. On the 4^3 and 5^3 tori all 24 digits are read by isolated digit-confined masks, established from 72 declared witness configurations at each size. No physical law is selected."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/partial_configuration_readout_injective_torus_3_check_2026_09_04.py
registry_id: partial_configuration_readout_injective_torus_3_every_law_visible
---

# The partial-configuration readout is injective on the 3-torus: every law is visible to records

**Date:** 2026-09-04

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/partial_configuration_readout_injective_torus_3_check_2026_09_04.py`](../scripts/partial_configuration_readout_injective_torus_3_check_2026_09_04.py)

**Runner cache:**
[`logs/runner-cache/partial_configuration_readout_injective_torus_3_check_2026_09_04.txt`](../logs/runner-cache/partial_configuration_readout_injective_torus_3_check_2026_09_04.txt)

**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
[`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md),
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md),
[`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The digit-confined question on the 3^3 torus is decided completely for all 72 targets, the 22 unsatisfiable ones by a complete backtracking enumeration carrying no solver as well as by three solvers with DRUP refutations; the injectivity criterion is proved in the note and closed against a declared pool of 3117 masks, each re-verified from its explicit witness configuration, by 96 requirement checks decided twice. The 4^3 and 5^3 results rest on declared witness configurations re-verified exactly. No physical law is selected and no lattice beyond the 3^3, 4^3 and 5^3 tori is claimed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Decide the readout on 6^3 and on non-cubic regions; lift the statement from supports to the distribution-valued rule; then ask which record-level object the framework should declare readable."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

PR #7918 asked how much of the law records can tell apart, for one record-level object: a region every site of
which carries a record. That object realises only the 64 fully recorded neighbour profiles, depends on 4 of the
24 ternary digits, and on the 3^3 torus distinguishes exactly 81 tables, every fibre exactly 3^20.

The companion note *Partially recorded regions make most of the law visible without reading the order of
formation* took the object the Record clauses actually license -- a region in which some sites carry records and
some do not, the unrecorded sites reading as open -- and found 17 of the 24 digits read exactly and 3 more to a
binary choice: at least 1,033,121,304 tables told apart, fibre at most 648. It left four digit-pairs
unseparated, claimed no impossibility and no injectivity for them, and named an exact decision procedure for "is
this demand mask realisable" as the next step. This note runs that procedure. Are the remaining digits visible
at all, and is the readout injective? Records register; the lattice is physical; a site carrying no record reads
as open.

## Supplied surface (quoted)

Admissibility and Record, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`), with reading note (3)
fixing the sense of "admissible" below:

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

> "Records form." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read." "A state is a configuration of records."

Nothing there requires that every site of a region carry a record before the region can be read, and **a site
need not carry a record** at all; nothing there refers to when a record was made, or in what order.

## T1 -- the encoding (exact)

A **support table** `T` assigns to each of the 729 ternary neighbour profiles a nonempty subset of `{0,1}`,
covariant under proper cubic rotations and label-equivariant. The 729 profiles fall into 57 proper-cubic orbits;
the global value flip fixes 9 and pairs the other 48 into 24 flip-pairs, each carrying one free ternary digit
`d_i`. Hence 3^24 = 282,429,536,481 tables. A **partial configuration** `c` is admissible under `T` as it stands
iff no recorded site asks for a value its orbit's menu forbids, and the asking is 48 bits: `c` is admissible iff
`mask(c) & block(T) == 0`, where `block(T)` sets bit `2i` iff `d_i = 0` and bit `2i+1` iff `d_i = 1`. Write
`A_p(T)` for the readout: the records present, each checked against what is actually beside it.

**The decision problem is local.** `mask(c)` contained in a bit set `S` says: every recorded site's demand bit
lies in `S` or is absent. A site's demand bit is a function of that site's value and its six neighbours'
conditions only, so the condition is a conjunction of constraints on 7-site stars -- a subshift of finite type
-- plus one existential per bit that must occur. That is what makes an exact solve possible, and the runner
checks it against the mask criterion directly. The CNF gives each site one one-hot ternary variable (`open`,
`record 0`, `record 1`) and forbids, for each site and value, every profile code whose demand bit falls outside
`S`, emitted through a prefix trie over the six ternary digits so a wholly forbidden subtree costs one short
clause; a bit required to occur is asserted by a Tseitin disjunction over all (site, profile) placements raising
it.

**The reduction is verified, not assumed.** `mask` is invariant under lattice translation, all 24 proper cubic
rotations acting as `c'(x) = c(Mx)`, and the global 0-1 flip; the runner checks all 27 translations, all 24
rotations and the flip on a declared configuration set, and checks that every profile in orbit A of a flip-pair
is rotatable onto that orbit's canonical representative and every profile in orbit B onto it after the flip. So
the demanding site is pinned at the origin, carrying the canonical representative, with no loss.

## T2 -- the digit-confined decision on the 3^3 torus (complete, exact)

For each pair `i` the three digit-confined targets are `{2i}`, `{2i+1}` and `{2i,2i+1}`; any two determine
`d_i`, any one splits `{0,1,2}` into 1+2. All 72 are decided.

```text
satisfiable                            50   masks re-verified by two paths
unsatisfiable                          22   zero targets realised
digits read exactly                    17
digits read to a binary choice          4   pairs 14, 18, 21, 23
digits no digit-confined mask reaches   3   pairs 11, 16, 17
per-digit fibre    3^3 x 2^4                =           432
per-digit classes  3^17 x 2^4               = 2,066,242,608
```

**The 22 unsatisfiable instances.** Each is decided by **a complete backtracking enumeration written from
scratch, carrying no solver**: a frontier search that branches only on sites adjacent to an existing record --
every other site may stay open without raising a demand -- and cuts a branch as soon as a recorded site has no
legal completion of its profile. Over the 22 it enumerated the whole space, found 55 legal configurations in
total, and **not one realises its target**. Where a solver is present the same 22 are decided again by CaDiCaL,
by Glucose with a DRUP refutation, and by MiniSat. So pairs 11, 16 and 17 admit no digit-confined mask on the
3^3 torus: the object is absent, not unfound.

**Pair 23 is realised**, by the complete configuration `101000110011010110001111100`, all 27 sites recorded,
demand mask exactly `{46, 47}`. The companion note's per-digit table is corrected here: it listed four pairs as
unseparated, and three of them are; the fourth is read to a binary choice. Its witness list holds 43 entries
where the exact count is **50**, the six additional ones all `{2i,2i+1}` targets.

## T3 -- the readout is injective on the 3^3 torus (exact)

The digit-confined framing is not the readout: a mask may constrain several digits at once, and such masks
separate tables the digit-confined ones cannot.

**The criterion.** Write `B = block(T)`; `d` maps to `B` injectively. Since `A_p(T) = { c : mask(c) & B == 0 }`,
`A_p(T) = A_p(T')` exactly when no realisable mask avoids one block set and meets the other. Define, for `b` not
in `B`,

```text
VIS(B, b) :=  some realisable mask m has  b in m  and  m & B == 0
A_v(j)    :=  VIS(B, 2j+v) for every legal B with d_j = 2
C_v(j)    :=  for every legal block set Bd on the 23 digits other than j, some
              realisable m has  m & {2j, 2j+1} = {2j+v}  and  m & Bd == 0
```

**Claim.** If `A_0(j) and A_1(j) and (C_0(j) or C_1(j))` holds for every `j`, then `T -> A_p(T)` is injective.

**Proof.** Take `T` distinct from `T'`, so `B` is distinct from `B'`; without loss some bit `b` lies in `B'` and
not in `B`; let `j = b div 2`. *(i)* If `d_j(T) = 2`, then `A_{b mod 2}(j)` applied at `B` supplies a realisable
`m` with `m & B == 0` and `b` in `m`; since `b` is in `B'`, that `m` lies in `A_p(T)` and not in `A_p(T')`.
*(ii)* Otherwise `d_j(T)` is 0 or 1, so `B` contains the partner bit of `b`, and the two tables differ at `j` as
`{0}` against `{1}`. If `C_{b mod 2}(j)` holds, apply it at `Bd = B` restricted to the digits other than `j`: it
gives a realisable `m` with `m & {2j,2j+1} = {b}` meeting neither `Bd` nor the pair-`j` bits of `B`, hence
`m & B == 0`, while `b` lies in `m` and in `B'`. If the other one holds instead, apply it at `Bd = B'`
restricted to the digits other than `j`; then `T` and `T'` exchange roles and the separating mask lies in
`A_p(T')` and not in `A_p(T)`. Either way `A_p(T)` is distinct from `A_p(T')`. ∎

**Antitonicity.** `VIS(B, b)` is antitone in `B`: enlarging the block set can only lose masks. So `C_v(j)` needs
checking only at **maximal** `Bd` -- every other digit 0 or 1, a fully deterministic law except at pair `j` --
which turns 3^23 candidate laws into 2^23 and puts the search on the hard end. In that form each usable mask
serves exactly a subcube of the deterministic laws, and the requirement is that the subcubes cover the cube.
Counterexample-guided refinement grew a pool of realisable masks until no block set defeated it: **3117 masks,
every one carried with the configuration that realises it and re-verified from that configuration** by both the
vectorised and the scalar path. The 96 requirements -- 48 of type `A`, 48 of type `C` -- are decided twice: by a
from-scratch subcube-cover procedure carrying no solver, and, where a solver is present, by CaDiCaL and Glucose
forced to agree.

```text
pairs 0..21, 23 :  A0=Y A1=Y C0=Y C1=Y
pair 22         :  A0=Y A1=Y C0=N C1=Y     (the criterion needs one of the two)
96 requirements : 95 met, C_0(22) the only one not; injectivity established
fibre 1; all 3^24 = 282,429,536,481 tables separated
```

**The blind digits are read jointly.** The 5-record configuration `101...0...........0........` has demand mask
`{0, 2, 22}`: admissible exactly when `d_0` is not 0, `d_1` is not 0 and `d_11` is not 0. Digits 0 and 1 are
read exactly by isolated masks of 2 and 3 records, so this configuration reads `d_11`. Six such witnesses, of 5
or 6 records, cover pairs 11, 16 and 17 in both directions: the digits were never beyond reach, only beyond the
reach of a single-digit witness.

## T4 -- the 4^3 and 5^3 tori (verified witnesses)

```text
4^3 : 72 / 72 digit-confined targets satisfiable, k = 2 .. 64 records
5^3 : 72 / 72 digit-confined targets satisfiable, k = 2 .. 64 records
```

All 24 digits are read exactly by isolated digit-confined masks at both sizes, so the per-digit fibre is 1 there
too, and each of the 22 targets the 3^3 torus does not reach becomes individually visible at L = 4. The note
carries the 144 witness configurations and re-verifies each mask against its target by both paths; the
satisfiability search that produced them is not re-run, and that is the one place where these rows rest on
declared data rather than a decision in the runner.

## T5 -- the structural explanation (exact)

**The 3-cycle mirror lemma.** On the `L^3` torus the two `d`-neighbours of a site `x` are `x+d` and `x-d`. For
`L = 3`, `x-d = x+2d`, so the three sites of any axis line are mutually `d`-adjacent; for `L >= 4` they are not,
and the runner checks both directions at L = 3, 4, 5. Two consequences: if all three sites of a line are
recorded, no site of that line can see open on that axis; and if exactly one is open, both recorded sites see
(open, the other record) -- a mixed axis at one site forces a mirrored one at its partner, carrying that
partner's value. That single missing degree of freedom is the whole difference between 3 and 4. Re-solving each
3^3-unsatisfiable target with every record confined to a wrap-free block centred on the demanding site then
separates the causes exactly:

```text
3x3x3 block  : only pair 4's {2i} becomes satisfiable, k = 14
4x4x4 block  : 18 of the 22, including all three targets of 11, 16 and 17
the 4^3 torus: all 22
```

1. **Pure wrap -- pair 4.** A 14-record witness fits inside a wrap-free 3x3x3 block, but that block cannot be
   laid on the 3-torus: the identification glues its opposite faces, and by the mirror lemma the open end the
   profile requires becomes a recorded far side. There is room; no room that stays open.
2. **Diameter 4 -- pairs 11, 16, 17, and the missing targets of 6, 18, 19, 22, 23 and 14.** Their witnesses need
   a recorded cluster of extent 4 along some axis, and the 3-torus has no wrap-free 4-run in any direction. This
   is the companion note's hold-out set: its search was not weak, it was looking for an object that is not
   there.
3. **Genuinely periodic -- `14:{2i}`, `20:{2i,2i+1}`, `21:{2i+1}`, `21:{2i,2i+1}`.** These four have no witness
   even in a 4x4x4 block; on the 4^3 torus they are realised only by densely recorded, wrap-using configurations
   of 52 to 64 records. Their profiles are the densest of the 24, so every witness site draws its whole
   neighbourhood into the record and the record has no boundary to terminate on: it must close on itself through
   the torus.

## Corollary

1. **Reading partially recorded regions, exactly as the Record axiom licenses, separates every one of the 3^24
   covariant laws on the 3^3 torus.** The partial-configuration readout is injective; every fibre is a
   singleton.
2. **Three digits are beyond the reach of any single-digit witness on the 3-torus, for an exact geometric
   reason, and are read jointly.** On 4^3 and 5^3 every digit is read individually.
3. **The companion note's bound stands and its headline understates.** Its floor of 1,033,121,304 tables and its
   ceiling of 648 on the fibre are both correct; the truth is not most of the law but all of it.
4. **No reading of the order of formation is needed**: the readout uses only the records present and what is
   beside them.
5. **Hence, under the axioms as written, which law holds is entirely a matter of what the records show**: the
   underdetermination of the law by the axioms is not a hidden choice.

## Reading, not theorem

Read a region as it is, empty sites empty, and every one of the possible laws leaves a different fingerprint,
even on the smallest torus: three of its settings cannot be read one at a time there, for a reason of the
torus's geometry, but they can be read together, and one size up they can be read one at a time. So the law is
not hidden from the records at all. Whatever the lattice's law is, the records say which.

## Interfaces

- **Larger alphabets.** Everything here is a two-valued site with a ternary profile; a larger local alphabet
  enlarges both the profile census and the digit space, and whether the covering argument survives is untouched.
- **The probability lift.** Every statement here is about supports. After the 2026-08-05 revision the rule is
  distribution-valued; a non-uniform lift separates at least as much, but the quantitative readout of a
  distribution is a different object and is not run.
- **The physical identification of the readable law.** Nothing here says which record-level object the framework
  should declare readable.

## Executable claim block

```text
registry_id: partial_configuration_readout_injective_torus_3_every_law_visible
ternary_profiles_orbits_flipfixed_pairs: 729 / 57 / 9 / 24
support_tables_and_demand_word_bits: 282429536481 / 48
digit_confined_targets_decided_torus_3: 72 (50 satisfiable / 22 not)
enumeration_legal_configurations_and_targets_realised: 55 / 0
pairs_with_no_digit_confined_mask: 11 16 17
pairs_read_to_a_binary_choice: 14 18 21 23
digits_exact_binary_blind_torus_3: 17 / 4 / 3
per_digit_fibre_and_classes: 432 / 2066242608
digit_confined_witnesses_torus_3: 50
declared_mask_pool_reverified: 3117
criterion_requirements_and_met: 96 / 95 (C_0 at pair 22 the only one not)
true_fibre_and_classes_torus_3: 1 / 282429536481
digit_confined_targets_torus_4_and_5: 72 / 72 at each size
obstruction_split_wrap_diameter_periodic: 1 / 17 / 4
periodic_witness_records_on_torus_4: 52 .. 64
no_physical_law_is_selected: true
```

## Proof boundary

The theorem is the finite classification above and nothing wider.

- **Complete exactly as scoped.** The 3^3 statements are complete: all 72 digit-confined targets decided, the 22
  negative ones by a complete backtracking enumeration carrying no solver, and the injectivity criterion closed
  by 96 requirement checks. The 4^3 and 5^3 rows rest on 144 declared witness configurations, each re-verified
  against its target; their satisfiability search is not re-run here. T5's block-confined split is decided when
  a solver is present and rests on 19 declared wrap-free witnesses otherwise; which path ran is printed by the
  runner.
- **A sufficient criterion, and a verified subset.** The criterion of T3 is sufficient, not necessary, and its
  two-case proof is the load-bearing item. The 3117-mask pool is a verified subset of the realisable masks,
  never a census: injectivity established with a subset is a fortiori true, and no impossibility follows from a
  mask's absence from it.
- **Three torus sizes, cubic, periodic.** Nothing is claimed for L >= 6 or for non-cubic regions. The lift is
  not monotone in either direction: a witness on `L^3` need not embed in `(L+1)^3`, and T5 exhibits witnesses
  that exist only because of the wrap; what does lift is a wrap-free witness, to any larger torus.
- **Support tables, not the full rule space.** The 3^24 support tables are the deep probe's finite lower-bound
  witness family under the canonical uniform lift, a stipulation here. No sampling, no seed and no random number
  generator is used anywhere; no premise is edited, no axiom is added, and **no physical law is selected**.

## Honest-auditor read

The load-bearing objects are, in order: the criterion of T3 and its two-case proof; the 3117-mask pool, every
mask in it re-verified from an explicit witness configuration rather than asserted; and the 22 negative verdicts
of T2. Attack them in that order. The criterion is sufficient only, so a reviewer who doubts it should check
case (ii), where the two tables differ at `j` as `{0}` against `{1}` and the argument turns on applying `C` at
one table's restriction or the other's. The negative verdicts have the strongest support here: a decision
procedure with no solver in it agrees with three solvers, and the enumeration's 55 legal configurations are a
positive count, not an absence. The weakest rows are 4^3 and 5^3, witness verification rather than decision, and
T5's split, whose negative half needs the solver. The correction to the companion note is one table row and one
count; that note's bound stands and its headline understates.

## Review record

This note decides a finite question about one record-level object and proposes no law. Hard landing conditions
are a fresh exact-boundary runner and cache pair, a current citation-manifest entry, and passing pipeline,
strict-lint and changed-evidence gates; independent audit remains a separate lane.
