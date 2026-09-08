---
claim_id: partially_recorded_regions_make_most_of_the_law_visible_without_reading_the_order_of_formation_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Conditional finite static-admissibility map for the supplied 3^24 support tables on the 3-torus. The exact 48-bit mask criterion, declared symmetry-normalized sweeps and all 44 digit-confined witnesses give at least 1,033,121,304 static classes and fibres at most 648. The original six-table, 305,659-configuration append-process comparison is retained: static membership and reachability differ in both directions. No membership oracle, empty-site readout, preparation ensemble or physical law is derived; arbitrary-torus refinement is unproved."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/partially_recorded_regions_make_most_of_law_visible_check_2026_09_04.py
registry_id: partially_recorded_regions_make_most_of_law_visible_torus_3
---

# Static partial-configuration masks distinguish more finite support tables

**Date:** 2026-09-04

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** conditional source; no retained or audited status applied

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
claim_type_reason: "Exact declared static mask and witness results. The at-most-eight-record sweep fixes site 0 recorded at 0 and covers masks by translation/flip symmetry; it is not a count of unique global orbits. The finite append process is supplied separately; physical oracle access remains open."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "The joint September-8 correction distinguishes this original 44-witness result from the later 50-witness and full-pool certificates. Physical preparation/access and arbitrary-size extension remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

How many finite support tables can a static set of partial configurations
distinguish? The declared family has 3^24 = 282,429,536,481 tables. Its static
complete-configuration map `A(T)` uses only four digits and, on the 3-torus,
has exactly 81 classes with fibres 3^20 = 3,486,784,401. That earlier result
does not restrict every statistic of complete records: a supplied fixed-order
endpoint law can distinguish tables in one such static class without history.

Here records register supported values and `open` is a formal domain label.
We ask a static membership question for supplied configurations, not whether
an absent site can be read. Actual preparation, knowledge of the recorded
domain, membership queries and an ensemble are additional conditions. They
are not supplied by the Record clauses.

## Supplied surface (quoted)

Admissibility, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`):

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

Reading note (3) of the same section fixes the sense of "admissible" below:

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

Record, current landed wording:

> "Records form." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read." "A state is a configuration of records."

## T1 -- static membership and the 48-bit demand mask (exact)

A **support table** `T` assigns to each of the 729 ternary neighbour profiles -- six
neighbours, each open, 0, or 1 -- a nonempty subset of `{0,1}`, covariant under
proper cubic rotations and label-equivariant, `T(flip p) = flip T(p)`: the deep
probe's finite witness family under the canonical uniform lift, not the full
distribution-valued rule space. A **partial configuration** `c` assigns `open`, `0`
or `1` to each of the 27 sites of the 3^3 torus, and is **admissible under `T`, as
it stands** iff every recorded site's value lies in `T`'s support for that site's
ternary profile in `c`; unrecorded sites impose no demand and unrecorded neighbors
are represented by the supplied open symbol. Write `A_p(T)` for this static set.
It is not a Record-licensed membership oracle or a physical formation test. `c` is **reachable under `T`**,
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
static complete-configuration fibre, for comparison  3^20       =  3,486,784,401
reduction in the fibre, at least  3^20 / 648      =      5,380,840
```

Pairs 11, 16, 17 and 23 are the 4-, 5- and 6-recorded-neighbour profiles: such a
site draws four to six neighbours into the record, each of which must land on a
pinned orbit or repeat the same demand. This list leaves their separation open; nothing here shows they cannot be. The
current joint correction distinguishes that original limitation from the later
conditional full-pool certificate; this runner does not execute that certificate.

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
exceptions over the 305,659 configurations. This is finite containment for five
supplied tables and the stated append model, not a general formation theorem.

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
a record. A lawful permanent Record is not erased by this later shell change.
Thus the supplied append process need not satisfy this simultaneous static test.

**4d -- finite reachable-set sensitivity.** For the separately defined reachable
set at the stated depth, only 5 of the
48 single-digit restrictions change it at k <= 4, so it sees 3 of the 24 digits (2
at k <= 3): only the demands no order can avoid survive. A supplied fixed-order endpoint law and the bare reachable set are different
objects; the former does not require reading an event history.

## T5 -- physical access remains a separate condition

The algebraic map `T -> A_p(T)` can be considered through a hypothetical static
membership oracle. Reading actual Records does not provide that oracle for all
counterfactual configurations, nor arbitrary preparations or a complete ensemble.
A site with no record cannot be read. Knowledge of a configuration's open domain
is a supplied mathematical input, not a value read from an absent site.

The six finite process comparisons exhibit both `A_p` outside `R_p` and `R_p`
outside `A_p`. They block identification of static membership with formation.
No physical law is selected. The full distribution-valued local law, its weights,
formation schedule, realized draws and physical readout bridge remain unsupplied.

## Corollary and interpretation

1. The declared 44 static witnesses determine seventeen digits exactly and three
   to a binary choice. Their class lower bound is 1,033,121,304 and fibre upper
   bound 648, a reduction of at least 5,380,840 relative to the static complete
   map. These are statements about the finite support family and membership map.
2. This witness list leaves four pairs unseparated and proves no impossibility.
   Injectivity is not claimed by this runner; later joint work has a separate
   sufficient certificate and does not alter the original witness payload.
3. No event order occurs in the static definition. That fact does not establish
   a physical experiment or tell which hypothetical configurations can be formed.

## Interfaces

- The 7,824 sweep masks and 44 listed witnesses are preserved. A finite list's
  failure to separate a digit is not a failure of all realizable masks.
- Arbitrary `L` to `L+1` torus refinement is unproved. The complete-profile
  upper bound of 81 is structural, but the attained partial-map bound is finite.
  Padding a witness is valid only if every recorded site's shell, including its
  open-neighbor buffer, is preserved by the embedding.
- The criterion uses supports. It does not identify different probability
  measures on the same support or determine the full M2(C) law.

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
static_complete_configuration_fibre_and_reduction: 3486784401 / 5380840
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
- **Complete exactly as scoped.** The at-most-eight-record sweep fixes site 0
  recorded at 0; translation and flip preserve masks, but its count is not a count
  of unique configuration orbits; the shell family within the 3^12 distance-2 shell of each demand bit; the
  translation family over the 13 x 3^9 configurations; the growth results over the
  305,659 configurations with at most 4 records and the six declared tables.
- **Declared witnesses, not a classification of witnesses.** The 44 witnesses are
  declared and re-verified exactly. A mask not on the list is not shown to be
  unrealisable, the four unseparated pairs carry no impossibility claim, injectivity
  is not claimed, and this list alone bounds the class count between 1,033,121,304 and 3^24.
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
unseparated pairs. 4b is the explicit finite formation counterexample; the sensitivity in 4d is
only the tested depth, with no strict-growth claim. That computation reported 43 witnesses where the merged list holds
44: the extra one is the third mask of pair 4, and no bound changes.

## Review record

The September-8 correction preserves the original note/cache in `archive/notes`
and all 44 witnesses, six process rows and original numeric checks. The original
open question is a historical frontier, not a claim that joint work has not
occurred. Current physical access and extension obligations remain explicit.
Formal audit remains deferred by the owner; no grade or audit status is applied.
