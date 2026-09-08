---
claim_id: only_81_of_the_support_tables_are_distinguishable_by_complete_records_formation_histories_distinguish_nearly_all_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "The covariant label-equivariant support tables number 3^24. A complete record configuration realises only the 64 fully-recorded neighbour profiles, which form 10 proper-cubic orbits, 2 self-flip and 4 flip-pairs, so 4 ternary digits are visible to complete records and 20 are invisible on any lattice. Complete enumeration of all 2^27 complete configurations of the 3^3 torus gives exactly 81 distinct globally admissible sets, one per reduced table, every fibre exactly 3^20 and the fibres summing to 3^24. On a declared finite set of formation orders and tables under the uniform lift the sequential-formation law queries up to all 24 digits, and a declared pair of tables sharing one admissible set is separated in total variation by 1. No physical law is selected."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/support_table_fibres_complete_records_81_classes_check_2026_09_03.py
registry_id: support_table_fibres_complete_records_81_classes_torus_3
---

# Only 81 of the support tables are distinguishable by complete records

**Date:** 2026-09-03

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/support_table_fibres_complete_records_81_classes_check_2026_09_03.py`](../scripts/support_table_fibres_complete_records_81_classes_check_2026_09_03.py)

**Runner cache:**
[`logs/runner-cache/support_table_fibres_complete_records_81_classes_check_2026_09_03.txt`](../logs/runner-cache/support_table_fibres_complete_records_81_classes_check_2026_09_03.txt)

**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
[`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md),
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md),
[`TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md`](TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Complete finite enumeration of the 2^27 complete configurations of the 3^3 torus, an exact orbit census of the 3^24 support tables, and exact formation-atom weights on a declared finite set of orders and tables. No physical law is selected and no lattice beyond the 3^3 torus is claimed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Repeat the fibre count for partially recorded configurations, the 48-bit object over all 24 pairs, and for larger tori."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Setting

Admissibility names one fixed nearest-neighbour rule but does not display it.
The 2026-07-13 deep probe counts the room the structural clauses leave:
282,429,536,480 covariant label-equivariant tables vary with the shell, out of
3^24 = 282,429,536,481. The 2026-08-13 covariant law pair exhibits two rules
that both satisfy the current Admissibility contract and differ in internal
symmetry, selecting neither as the framework's physical law. The axioms leave
the law underdetermined by a large finite factor.
This note asks a different question about the same space. Only records are
readable; records register, and a state is a configuration of records. If two
tables are different laws but no record content ever comes apart under them,
the difference is not a difference in what the lattice is like. So: how many of
the 3^24 tables can records tell apart? The answer depends on which
record-level object is readable, and the two candidates point opposite ways.

## Supplied surface (quoted)

Admissibility, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`):

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

Reading note (3) of the same section fixes the sense of "admissible" used
below:

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

Record, current landed wording:

> "Only records are readable. A readout value is determined by record content alone."

> "A state is a configuration of records."

> "Records form."

The memo names that records form; it does not name an order of formation, nor
say the order is part of record content. That silence is what this note
isolates.

## Definitions

A **support table** `T` assigns to each ternary neighbour profile -- each of
the six neighbours open, 0, or 1 -- a nonempty subset of `{0,1}`, subject to
covariance under proper cubic rotations and to label-equivariance
`T(flip p) = flip T(p)`. This is the deep probe's finite witness family under
the canonical uniform lift, not the full distribution-valued rule space.
**(A), the complete-record object.** `A(T)` is the set of complete
configurations -- every site carrying a record -- whose every site value lies
in the support `T` names for that site's fully recorded shell.

**(B), the formation-history object.** Fix an order of the sites. From no
records, at step `k` the site's support is `T` applied to the current ternary
profile, with `open` in the slots of sites not yet carrying a record, and the
value is uniform on that support; `P_T` is the resulting distribution on
complete configurations. The uniform lift is the deep probe's own canonical
lift, stipulated here.

## T1 -- the table space (exact)

The 3^6 = 729 ternary profiles fall into 57 proper-cubic orbits. Global value
flip fixes 9 of them and pairs the other 48 into 24 flip-pairs. A self-flip
orbit admits only the flip-invariant menu `{0,1}` and is pinned; each of the 24
flip-pairs carries one free ternary choice, the partner forced. Hence 3^24 =
282,429,536,481 tables, reproducing the deep probe's census exactly, including
its 3^24 - 1 = 282,429,536,480 neighbour-varying count. The 24 counts
flip-*pairs*, not orbits, and the profiles are ternary.

## T2 -- what complete records can realise (exact, structural)

A complete configuration has no open slot, so it realises only the 64 fully
recorded profiles. Those fall into 10 proper-cubic orbits: 2 self-flip and 4
flip-pairs.

| class | representative `(+x,-x,+y,-y,+z,-z)` | orbit size | menu |
|---|---|---|---|
| self-flip a | `000111` | 12 | pinned to `{0,1}` |
| self-flip b | `010101` | 8 | pinned to `{0,1}` |
| pair 0 | `000000` and `111111` | 1 + 1 | one free digit |
| pair 1 | `000001` and `011111` | 6 + 6 | one free digit |
| pair 2 | `000011` and `001111` | 3 + 3 | one free digit |
| pair 3 | `000101` and `010111` | 12 + 12 | one free digit |

The sizes sum to 64. Both self-flip orbits are the three-three shells, so the
tie is never a free choice: covariance with label-equivariance already forces
both values into the support there, for every table in the space. Therefore
`A(T)` depends on `T` through exactly 4 of the 24 digits; the other 20 concern
profiles containing an open slot, and no complete configuration ever presents
one. This holds on any lattice, not only on the torus below: **every fibre of
`T -> A(T)` contains at least 3^20 = 3,486,784,401 tables.**

## T3 -- the 3^3 torus (complete enumeration)

The runner enumerates all 2^27 = 134,217,728 complete configurations of the 3^3
torus; nothing is sampled. A configuration reduces to an 8-bit mask of the
one-sided menu choices it forbids; the sweep runs in 512 plane chunks with no
dense array above 512 x 512, and a site-by-site computation on a declared
configuration set reproduces the masks.
```text
distinct realised masks                       182 of 256
reduced tables / distinct sets A(T)           81 = 3^4  /  81
fibre of every class, sum of fibres           3^20 = 3,486,784,401 -> 3^24
tables inducing the empty set                 0
tables inducing all 2^27 configurations       1  (menu code 2222)
tables with 0 < |A(T)| < 27, singletons       0, 0
smallest class                                2,918 configurations (0100)
distinct values of |A(T)|                     81 of 81
```

Menu code: one digit per pair 0..3, `0` for `{0}` on the side-A representative,
`1` for `{1}`, `2` for `{0,1}`; the partner is forced.
**The fibre structure is exactly uniform.** Each class is the image of exactly
one reduced table, and each reduced table lifts to exactly 3^20 full tables;
there is no fibre-size distribution to report. All 81 cardinalities happen to
be distinct here, so `|A(T)|` is a complete invariant on this torus -- a
coincidence of the torus, not a theorem. Two rows are repository objects: the
repository's own `majority_availability` is menu code `0000` with
`|A| = 9,038`, and `copy_neighbor_availability` on the binary domain is menu
code `0222` with `|A| = 89,286,536`. The runner imports both from
`scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py` rather
than re-deriving them. They land in different classes, so complete records do
separate them. Both counts are recomputed by a second complete 2^27 sweep using
only neighbour sums -- no orbit machinery, no plane factorisation, no mask.

## T4 -- formation histories (exact, on a declared finite set)

The declared order set is three orders of the 27 sites: `s = 9x+3y+z`, its
reverse, and `s = 9z+3y+x`. Each reaches 343 of the 729 profiles and touches all
24 flip-pairs, so no digit is hidden from `(B)` by the order alone. Let `R(T)`
be the set of digits queried at some positive-probability partial configuration.
Digits outside `R(T)` are never queried, so changing them leaves the process
identical step by step: **`P_T` is unchanged, and the `(B)`-fibre
of `T` contains at least 3^(24-|R(T)|) tables.** Conversely, at the first step
where a reachable partial configuration meets a profile whose support differs,
the two laws differ on that step's joint distribution, the earlier steps being
identical. So `R(T)` is exactly the set of digits that change the law singly.

```text
majority rule       |R| = 9    (B)-fibre >= 3^15 = 14,348,907
copy-neighbour      |R| = 9    (B)-fibre >= 3^15
all-supports table  |R| = 24   (B)-fibre >= 3^0  = 1
```

The majority rule's formation law has exactly **two** atoms, the two constant
configurations, at 1/2 each: the first site meets an all-open profile, a
self-flip orbit pinned to `{0,1}`, and every later site takes the majority of
the neighbours already recorded. Both atoms lie in `A(majority)`, but the law
puts all its mass on 2 of that class's 9,038 members, so `(A)` and `(B)` are
not the same object even in support. For the all-supports table every step
branches, so every order-reachable profile carries positive probability and
`R = 24`: each of the 24 digits individually changes the formation law,
against the 4 that can ever change the admissible set.

**Total-variation-one witness.** Change, in the majority table, the single
digit carried by the orbit of `(0, open, open, open, open, open)`. It is one of
the 20 invisible digits, so the pair shares all four visible digits and
therefore one admissible set. Under the changed table the second site in the
order takes the value opposite to the first, so no formed configuration is
constant, while under the majority table every one is. The supports are disjoint
and the total variation is exactly 1: `(B)`-separation inside one `(A)`-class.

**A declared family, exact lower bounds.** The 32 tables whose 24-digit codes
are the base-3 expansions of `j * floor(3^24 / 32)`, `j = 0..31`, give queried
counts from 6 to 24, with 12 of the 32 at 23 or 24 and a second cluster at 9.
Each stated fibre is an exact lower bound over the declared finite set; where
the frontier cap is reached, `|R(T)|` is itself a lower bound. Near injectivity
is therefore common in this family but not its typical case, and the sharp
statement is the digit count above, not a claim about generic tables.

## Corollary

1. **At the level of complete records the law is almost entirely invisible.**
   20 of its 24 digits concern partially recorded neighbourhoods and are
   invisible on any lattice; on the 3^3 torus the remaining 4 are fully
   separated, so complete records distinguish exactly 81 classes, fibres 3^20.
2. **At the level of formation histories the law is nearly fully visible.**
   All 24 digits are individually visible for the all-supports table, and a pair
   sharing one admissible set is separated in total variation by 1.
3. **Whether the law is underdetermined "physically" is therefore decided by
   which record-level object is readable:** the final configuration, or the
   history of formation. The Record axiom names record content as readable and
   is silent on the order of formation; the history-index result on main makes
   the history index the record-monotone direction. That is an axiom-level
   decision. This note names that decision; it does not make it.
4. **The two repository rules sit in different complete-record classes**, so
   records do separate them; the reduction to 81 erases no distinction anyone
   has drawn.

## Reading, not theorem

Look only at a region once every site has its record, and almost nothing of the
law shows: on this small torus just 81 different laws could ever be told apart,
and most of what a law says is about sites whose neighbours are not yet all
recorded. Watch the records form instead, and nearly every law shows. So whether
the lattice's law is a hidden choice or a visible one depends on whether the
order in which records formed can be read, and that the axioms do not answer.

## Interfaces

- **Partial configurations.** The object matching the append-only ontology is
  the admissible set of *partially* recorded configurations, a 48-bit mask over
  all 24 pairs rather than an 8-bit mask over 4. That is the named follow-on and
  is not run here.
- **Larger tori.** 81 is a ceiling fixed by the 4 visible digits, so it bounds
  the complete-record count on every lattice; larger tori can only refine
  `A(T)`, never coarsen it. Torus-specific is the *attainment*.
- **Non-uniform lifts.** Every `(B)` number depends on it; a non-uniform lift
  separates at least as much, never less.

## Executable claim block

```text
registry_id: support_table_fibres_complete_records_81_classes_torus_3
ternary_profiles_orbits_selfflip_pairs: 729 / 57 / 9 / 24
support_tables: 282429536481
fully_recorded_profiles_orbits: 64 / 10
visible_and_invisible_digits: 4 / 20
torus_complete_configurations: 134217728
realised_masks: 182
distinct_admissible_sets: 81
fibre_of_every_class: 3486784401
smallest_class: 2918
majority_menu_code_and_count: 0000 / 9038
copy_neighbour_menu_code_and_count: 0222 / 89286536
formation_orders_and_tables_declared: 3 / 35
majority_formation_atoms_and_fibre_bound: 2 / 14348907
witness_total_variation: 1
no_physical_law_selected: true
```

## Proof boundary

The theorem is the finite classification above and nothing wider.
- Attainment is proved on **one torus** only: the count 81 and the uniform 3^20
  fibre come from complete enumeration on the 3^3 torus. T2's 20-digit
  invisibility is structural and holds on any lattice.
- **Support tables, not the full rule space.** After the 2026-08-05 revision the
  rule is distribution-valued and the unrestricted space is continuous. The 3^24
  support tables are the deep probe's own finite lower-bound witness under the
  canonical uniform lift, and that lift is a stipulation here.
- **`(B)` on a declared finite set:** three orders and 35 tables, all named by
  declared arithmetic; every `(B)` number is an exact atom weight or an exact
  lower bound over that set. No sampling and no random number generator is used
  anywhere in the runner. Beyond that: no physical law is selected, no premise
  is edited, no axiom is added, and nothing is claimed about which record-level
  object the framework should declare readable.
- **PR #7833 is not a control** for this note. Its family is Hermitian bond
  operators parameterised by a coupling ratio, a different object from a support
  table; its structural lesson was borrowed, no check was run against it, and
  the source computation says plainly that it is not a control.

## Honest-auditor read

The load-bearing objects are the 2^27 complete enumeration and the two
independent complete recounts; attack them in that order. The mask reduction is
the one place where an indexing error would be silent, which is why the runner
recomputes the masks site by site on a declared configuration set and recounts
two named classes by neighbour sums alone. That all 81 `|A(T)|` are distinct is a
coincidence of this torus; classes are decided on the admissible sets, not on
cardinality. T2 is the strongest claim here, structural and lattice-independent,
and the shortest to check: an orbit count on 64 profiles.
T4's fibre numbers are lower bounds by construction; the only two-sided `(B)`
fact asserted is the total-variation-one witness, which follows from disjoint
supports, not an estimate. The declared-family row came out weaker than
anticipated and does not support the corollary.

## Review record

This note counts fibres; it narrows nothing and proposes no law. Its two numbers
point opposite ways on purpose, and the corollary is a statement about the
axioms' silence on the order of formation, not about the lattice. Hard landing
conditions are a fresh exact-boundary runner and cache pair, a current
citation-manifest entry, and passing repository pipeline, strict-lint, and
changed-evidence gates; independent audit remains a separate lane.
