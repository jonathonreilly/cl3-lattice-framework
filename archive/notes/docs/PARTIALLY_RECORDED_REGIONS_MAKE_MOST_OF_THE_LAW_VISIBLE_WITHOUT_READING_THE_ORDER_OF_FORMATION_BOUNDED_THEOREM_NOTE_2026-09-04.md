---
claim_id: partially_recorded_regions_make_most_of_the_law_visible_without_reading_the_order_of_formation_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "The covariant label-equivariant support tables number 3^24. A partial configuration assigns open, 0 or 1 to the 27 sites of the 3^3 torus and is admissible under a table when every recorded site's value lies in the support the table names for that site's ternary neighbour profile; this reduces exactly to a 48-bit demand mask, invariant under lattice translation, proper cubic rotation and the global value flip. Complete sweeps of every partial configuration with at most 8 records, of the 3^12 distance-2 shell of each of the 48 demand bits, and of the 13 x 3^9 translation-symmetric family are run. A declared list of 44 witness configurations, each re-verified exactly by two independent code paths, determines 17 of the 24 ternary digits exactly and 3 more to within a binary choice, so the partial-configuration readout distinguishes at least 3^17 x 2^3 = 1,033,121,304 tables with every fibre at most 3^4 x 2^3 = 648. Four digit-pairs are not separated by any declared witness and no impossibility is claimed for them; injectivity is not claimed. Over all 305,659 partial configurations with at most 4 records and six declared tables, every admissible configuration is reachable by some formation order for five tables including both repository rules, and for one declared table 1,350 admissible configurations are reachable by no order. No physical law is selected."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/partially_recorded_regions_make_most_of_law_visible_check_2026_09_04.py
registry_id: partially_recorded_regions_make_most_of_law_visible_torus_3
---

# Partially recorded regions make most of the law visible without reading the order of formation

**Date:** 2026-09-04

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/partially_recorded_regions_make_most_of_law_visible_check_2026_09_04.py`](../scripts/partially_recorded_regions_make_most_of_law_visible_check_2026_09_04.py)

**Runner cache:**
[`logs/runner-cache/partially_recorded_regions_make_most_of_law_visible_check_2026_09_04.txt`](../logs/runner-cache/partially_recorded_regions_make_most_of_law_visible_check_2026_09_04.txt)

**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
[`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md),
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md),
[`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Complete finite sweeps on the 3^3 torus -- every partial configuration with at most 8 records, the 3^12 distance-2 shell of each of the 48 demand bits, the 13 x 3^9 translation-symmetric family, and every partial configuration with at most 4 records for six declared tables -- together with a declared witness list re-verified exactly by two independent code paths. No physical law is selected and no lattice beyond the 3^3 torus is claimed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Decide realisability of a demand mask exactly rather than by construction, settling the four unseparated digit-pairs either way; then exploit the 7,824 multi-digit masks already in hand; then repeat on larger tori."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

The 2026-07-13 deep probe counts the room the structural clauses leave: 3^24 =
282,429,536,481 covariant label-equivariant support tables. PR #7918 asked how many
records can tell apart, and answered it for one record-level object -- a region
every site of which carries a record. That object realises only the 64 fully
recorded neighbour profiles, so it depends on 4 of the 24 ternary digits; on the 3^3
torus it distinguishes exactly 81 tables, every fibre exactly 3^20 = 3,486,784,401.
It named the partial-configuration object as the follow-on it did not run.

This note runs it: records register, the lattice is physical, and the question is
what a region of it can register. The Record clauses say a site with no record
cannot be read and that only records are readable; they nowhere say a region may be
read only when every site carries one, and **a site need not carry a record** at
all. So the licensed object is a region in which some sites carry records and some
do not, the unrecorded sites **read as open**.

## Supplied surface (quoted)

Admissibility, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`):

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

Reading note (3) of the same section fixes the sense of "admissible" below:

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

Record, current landed wording:

> "Records form." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read." "A state is a configuration of records."

## T1 -- the readout, and its reduction to a 48-bit demand mask (exact)

A **support table** `T` assigns to each of the 729 ternary neighbour profiles -- six
neighbours, each open, 0, or 1 -- a nonempty subset of `{0,1}`, covariant under
proper cubic rotations and label-equivariant, `T(flip p) = flip T(p)`: the deep
probe's finite witness family under the canonical uniform lift, not the full
distribution-valued rule space. A **partial configuration** `c` assigns `open`, `0`
or `1` to each of the 27 sites of the 3^3 torus, and is **admissible under `T`, as
it stands** iff every recorded site's value lies in `T`'s support for that site's
ternary profile in `c`; unrecorded sites ask nothing and unrecorded neighbours read
as open. Write `A_p(T)`: the readout the Record clauses license, the records present
each checked against what is actually beside it. `c` is **reachable under `T`**,
written `R_p(T)`, iff some order `s_1..s_k` of its recorded sites has `c(s_j)` in
`T`'s support for the profile of `s_j` against the records `{s_1..s_{j-1}}` at every
step, records being permanent and never re-checked.

The 729 profiles fall into 57 proper-cubic orbits. The global value flip fixes 9 and
pairs the other 48 into 24 flip-pairs. A flip-fixed orbit admits only the
flip-invariant menu `{0,1}` and is pinned for every table; each flip-pair carries
one free ternary digit `d_i in {0,1,2}` -- `0` for `{0}`, `1` for `{1}`, `2` for
`{0,1}` on the side-A representative, the partner forced. Hence 3^24 tables,
reproducing the deep probe's census. Admissibility then factorises -- `c` is
admissible under `T` iff no recorded site of `c` asks for a value its orbit's menu
forbids -- and the asking is 48 bits:

```text
bit 2i    set  <=>  c realises (A_i,1) or (B_i,0) at a recorded site  -> forbids d_i = 0
bit 2i+1  set  <=>  c realises (A_i,0) or (B_i,1) at a recorded site  -> forbids d_i = 1
flip-fixed orbits raise no bit: their menu is {0,1} for every table
c in A_p(T)   <=>   mask(c) & block(T) == 0
```

`block(T)` sets bit `2i` iff `d_i = 0` and bit `2i+1` iff `d_i = 1`; digit `2`
blocks nothing. So `A_p(T)` is fixed by which masks survive `T`. The runner checks
the criterion against a direct site-by-site menu test on a declared configuration
set against 24 declared tables, and checks that `mask(c)` is unchanged by all 27
lattice translations, all 24 proper cubic rotations and the global value flip -- the
invariance that makes the sweeps below complete after fixing site 0 recorded at 0.

## T2 -- what the torus realises (complete sweeps)

All 729 ternary profiles are realised at a recorded site of the 3^3 torus: on a
3-torus `+d` and `-d` land on distinct sites, so a site's six neighbours are six
distinct sites, and each profile is realised by recording the site and the
neighbours it names and leaving the rest unrecorded. But realising a profile also
records its neighbours, and those sites raise their own bits; the sharper question
is which demands can be raised alone. A bit no family below isolates is not thereby
shown to be unrealisable.

```text
family (each complete as stated)                    configurations   bits isolated
record-count sweep, k <= 8, site 0 fixed at 0         101,299,433         17 of 48
   84,198,400 of them at k = 8; 7,824 distinct demand masks realised
distance-2 shell, 3^12 = 531,441 per demand bit    48 x   531,441         20 of 48
translation-symmetric, 13 subgroups x 3^9              13 x 19,683        27 of 48
union of the three families                                               30 of 48
```

## T3 -- the visibility table (exact, declared witnesses)

If the single-bit mask `{b}` is realisable then `A_p(T)` reveals whether `T` blocks
`b`, unconditionally on the other 23 digits; a mask confined to one flip-pair does
the same for that pair, `{2i}` separating `d_i = 0` from `{1,2}`, `{2i+1}`
separating `d_i = 1` from `{0,2}`, `{2i,2i+1}` separating `d_i = 2` from `{0,1}`,
and any two of the three determining `d_i`. Isolation is possible at all because of
the 9 pinned orbits: two adjacent sites both recorded `0` raise the same single bit,
and the origin recorded `1` among six neighbours recorded `0` leaves every neighbour
on a pinned orbit, which asks nothing of any table, so the origin alone raises a
bit.

The note carries a **declared witness** list: 44 partial configurations, written out
in full in the runner with their stated demand masks. The runner recomputes each
mask twice -- by the vectorised path, and by a scalar path that rebuilds every
profile tuple and re-canonicalises it -- and checks that each is confined to a
single flip-pair. How the list was assembled is not part of any claim.

```text
declared witnesses                                             44
digits read exactly / to a binary choice / not separated       17 / 3 / 4 of 24
digit-pairs not separated by any declared witness              11, 16, 17, 23
classes distinguished, at least  3^17 x 2^3       =  1,033,121,304
fibre, at most                   3^4  x 2^3       =            648
complete-record fibre, for comparison  3^20       =  3,486,784,401
reduction in the fibre, at least  3^20 / 648      =      5,380,840
```

Pairs 11, 16, 17 and 23 are the 4-, 5- and 6-recorded-neighbour profiles: such a
site draws four to six neighbours into the record, each of which must land on a
pinned orbit or repeat the same demand. Whether they can be separated at all **is
open**; nothing here shows they cannot be.

## T4 -- growth compatibility (complete for k <= 4)

Complete enumeration of all 305,659 partial configurations with at most 4 records
(`1+54+1404+23400+280800`) against six declared tables: the two repository rules,
re-derived as 24-digit codes and checked against their own module; three declared
literal codes; and the declared arithmetic code `d_i = (2i+1) mod 3`.

```text
table                              |A_p|     |R_p|   admissible, no order   reachable, not admissible
majority (repository)            151,489   194,905                      0                      43,416
copy-neighbour (repository)      152,137   196,201                      0                      44,064
declared literal A               299,989   304,309                      0                       4,320
declared literal B               297,289   305,659                      0                       8,370
all menus {0,1}                  305,659   305,659                      0                           0
declared arithmetic              152,947   222,823                  1,350                      71,226
```

**4a.** For five of the six declared tables, including both repository rules, every
admissible partial configuration is reachable by some formation order, with zero
exceptions over the 305,659 configurations: there the static readout certifies no
stage the append-only ontology could not produce.

**4b -- the containment is not universal.** The sixth table has 1,350 admissible
configurations no order builds. The smallest carries 3 records: three sites of one
3-cycle, all recorded `0`, each reading its two partners and asking for menu `{0}`
on that profile, so the configuration stands; but whichever record is written second
reads exactly one recorded neighbour valued 0, whose menu under this table is `{1}`.
The runner tries every order of the three and finds none. So 4a is a statement about
the declared tables, not a theorem.

**4c -- the converse fails.** 43,416 configurations reachable under the majority
rule are not admissible as they stand -- 22% of its reachable set at k <= 4, with
3-record witnesses. A site written early reads open where a later record comes to
sit, so its value stood when written and does not stand once that neighbour carries
a record: append-only formation does not produce globally consistent configurations,
and nothing requires it to.

**4d -- the bare reachable set is nearly blind.** If the readable object is which
partial configurations are reachable rather than which are admissible, only 5 of the
48 single-digit restrictions change it at k <= 4, so it sees 3 of the 24 digits (2
at k <= 3): only the demands no order can avoid survive. Formation statistics with a
declared order (PR #7918) and the reachable-set readout are different objects.

## T5 -- the decision brief (statement)

The Record clauses license reading the records present, unrecorded sites read as
open, each record checked against what is actually beside it. That is exactly `A_p`:
no order, no history, no probability lift, and no axiom is added. The 3^20 fibre of
PR #7918 followed from insisting that a region be read only once every site carries
a record, which the clauses never demanded.

## Corollary

1. **Partially recorded regions make most of the law visible.** 17 of the 24 digits
   are read exactly and 3 more to within a binary choice, so the fibre is at most
   648 against 3^20 on the 3^3 torus -- a reduction of at least 5,380,840 -- and at
   least 1,033,121,304 tables are told apart, against 81.
2. **Four digit-pairs were not separated by any declared witness**, and whether they
   can be is open. An exact realisability decision procedure is the named next step;
   **injectivity is not claimed**, and no impossibility is claimed either.
3. **No reading of the order of formation is needed:** the readout uses only the
   records present and what is beside them, which the clauses license.
4. **What makes the law visible is reading regions at intermediate stages, not the
   sequence:** the bare reachable set sees 3 of 24 digits at k <= 4, while every
   admissible partial configuration is reachable for five of the six declared
   tables.
5. **Hence the law is largely visible to records under the axioms as written**: the
   underdetermination of the law by the axioms is an underdetermination of what the
   records will show, not a hidden choice, and which law holds is on this reading an
   empirical question for the records.

## Reading, not theorem

The earlier count assumed a region is read only once every site has its record, and
then almost nothing of the law shows. But the axiom lets a region be read as it is,
with the empty sites empty, and then most of the law shows: seventeen of its
twenty-four settings can be read off exactly and three more to a coin's worth.
Nothing about the order in which records formed is needed. Four settings were not
pinned down here, and whether they can be is the next question.

## Interfaces

- **The four pairs, and the 7,824 multi-digit masks.** An exact decision procedure
  for mask realisability -- a constraint solve rather than a construction -- would
  settle 11, 16, 17 and 23 either way; and masks touching several digits can
  separate tables the digit-confined masks cannot, tightening the class bound.
  Neither is run here.
- **Larger tori and the lift.** A larger torus can only refine `A_p`, never coarsen
  it, so 1,033,121,304 is a floor that survives enlargement and 648 a ceiling that
  can only fall; attainment is torus-specific. Every statement here is about
  supports, and a non-uniform lift separates at least as much.

## Executable claim block

```text
registry_id: partially_recorded_regions_make_most_of_law_visible_torus_3
ternary_profiles_orbits_flipfixed_pairs: 729 / 57 / 9 / 24
support_tables_and_demand_word_bits: 282429536481 / 48
record_count_sweep_depth_configs_masks: 8 / 101299433 (84198400 at k=8) / 7824
bits_isolated_sweep_shell_translation_union: 17 / 20 / 27 / 30
declared_witnesses_digits_exact_binary_unseparated: 44 / 17 / 3 / 4
unseparated_pairs: 11 16 17 23
classes_at_least_fibre_at_most: 1033121304 / 648
complete_record_fibre_and_reduction: 3486784401 / 5380840
growth_configurations_and_tables: 305659 / 6
tables_with_zero_admissible_unreachable_and_the_exception: 5 / 1350
reachable_not_admissible_majority: 43416
reachable_stage_digits_k4_k3: 3 / 2
no_physical_law_is_selected: true
```

## Proof boundary

The theorem is the finite classification above and nothing wider.

- **Attainment on one torus.** Every attainment number is the 3^3 torus; nothing is
  claimed for any other lattice.
- **Complete exactly as scoped.** The record-count sweep is complete for at most 8
  records; the shell family within the 3^12 distance-2 shell of each demand bit; the
  translation family over the 13 x 3^9 configurations; the growth results over the
  305,659 configurations with at most 4 records and the six declared tables.
- **Declared witnesses, not a classification of witnesses.** The 44 witnesses are
  declared and re-verified exactly. A mask not on the list is not shown to be
  unrealisable, the four unseparated pairs carry no impossibility claim, injectivity
  is not claimed, and the true class count lies between 1,033,121,304 and 3^24.
- **Support tables, not the full rule space.** After the 2026-08-05 revision the
  rule is distribution-valued and the unrestricted space is continuous; the 3^24
  support tables are the deep probe's own finite lower-bound witness under the
  canonical uniform lift, a stipulation here. No sampling, no seed and no random
  number generator is used anywhere; no premise is edited, no axiom is added, and
  **no physical law is selected**; and nothing is claimed about which record-level
  object the framework should declare readable.

## Honest-auditor read

The load-bearing objects are T1's mask reduction and T3's declared witness list;
attack them in that order. The reduction is the one place where an indexing error
would be silent, which is why the runner checks the criterion against a direct
site-by-site menu test and checks mask invariance under all 27 translations, all 24
rotations and the flip; every witness is re-verified by a scalar path sharing no
array machinery with the vectorised sweeps. T3's bound is one-sided: the witnesses
prove a floor on the classes and a ceiling on the fibre, and nothing about the four
unseparated pairs. 4b is the correction the source computation did not have, and 4d
will grow with k. That computation reported 43 witnesses where the merged list holds
44: the extra one is the third mask of pair 4, and no bound changes.

## Review record

This note counts fibres for one record-level object and proposes no law. Hard
landing conditions are a fresh exact-boundary runner and cache pair, a current
citation-manifest entry, and passing pipeline, strict-lint and changed-evidence
gates; independent audit remains a separate lane.
