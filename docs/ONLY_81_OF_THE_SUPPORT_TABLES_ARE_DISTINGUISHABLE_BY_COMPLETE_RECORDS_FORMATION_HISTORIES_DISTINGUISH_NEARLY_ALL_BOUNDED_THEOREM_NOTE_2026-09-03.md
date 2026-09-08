---
claim_id: only_81_of_the_support_tables_are_distinguishable_by_complete_records_formation_histories_distinguish_nearly_all_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite support-table results. The static complete-configuration map A(T) depends on four of 24 digits and has exactly 81 classes of size 3^20 on the 3-torus. Under a supplied deterministic order and uniform lift, the complete endpoint law P_T has exact fibre 3^(24-|R(T)|); censored queried sets give upper bounds. The original TV-one pair is separated by a final endpoint event, without reading history. Physical preparation, ensemble access and a membership oracle are not derived; no physical law is selected."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/support_table_fibres_complete_records_81_classes_check_2026_09_03.py
registry_id: support_table_fibres_complete_records_81_classes_torus_3
---

# Static admissibility has 81 classes; fixed-order endpoint laws distinguish more

**Date:** 2026-09-03

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** conditional source; no retained or audited status applied

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
claim_type_reason: "Finite static census and a supplied fixed-order endpoint theorem. Three orders have geometric profile checks; 35 original frontier calls use lex order, with 11 censored family rows. No physical access protocol is derived."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "The joint September-8 correction records the companion partial-mask and injectivity results. Physical preparation/readout access and arbitrary-size refinement remain separate obligations."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Setting

How much of a finite support table is fixed by a static admissibility set, and
how much by a supplied endpoint probability law? These are different maps.
The deep probe supplies a finite family of 3^24 = 282,429,536,481 support
tables, of which 282,429,536,480 vary with the shell. The full distribution-valued
law on M2(C) is a larger object. The corrected Q8 law pair is nonselection
context only; its broader process claims are not used here.

Records register supported values, but reading actual Records does not supply
arbitrary preparations, a static membership oracle or a complete endpoint
ensemble. This note classifies the declared mathematical maps, leaving those
physical access conditions open.

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

The memo names that records form; it does not supply a site order, preparation
protocol or ensemble. A formal open symbol records the supplied domain of a
configuration; it is not a physical readout of an absent site. Records remain
permanent when later additions change their neighbors. The history-index note
is context for a sequence convention only, not a physical clock supplier.

## Definitions

A **support table** `T` assigns to each ternary neighbour profile -- each of
the six neighbours open, 0, or 1 -- a nonempty subset of `{0,1}`, subject to
covariance under proper cubic rotations and to label-equivariance
`T(flip p) = flip T(p)`. This is the deep probe's finite witness family under
the canonical uniform lift, not the full distribution-valued rule space.
**(A), the static complete-configuration map.** `A(T)` is the set of complete
configurations -- every site carrying a record -- whose every site value lies
in the support `T` names for that site's fully recorded shell.

**(B), the supplied fixed-order endpoint law.** Fix an order of the sites. From no
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

## T2 -- the profiles used by static complete configurations (exact)

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
`A(T)` depends on `T` through at most 4 of the 24 digits; the other 20 concern
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
than re-deriving them. They lie in different static classes; this is a statement about `A(T)`. Both counts are recomputed by a second complete 2^27 sweep using
only neighbour sums -- no orbit machinery, no plane factorisation, no mask.

## T4 -- supplied fixed-order endpoint laws

The three declared orders are `s = 9x+3y+z`, its reverse, and `s = 9z+3y+x`.
Their geometric checks each find 343 profiles and all 24 pairs. The 35 original
frontier calls are **all lex order**: majority, copy, the modified-majority
partner and 32 arithmetic tables. The all-support result below uses a geometric
argument, not an uncapped 2^27 frontier run.

Let `R(T)` contain every digit queried at a positive-probability prefix under
the supplied order and uniform lift. If `T'` agrees with `T` on `R(T)`, induction
over the order gives identical prefixes and conditional menus, hence the same
complete endpoint law. Conversely `P_T = P_T'` gives the same prefix marginals.
At each positive prefix, dividing the next-value joint probability by that
prefix probability recovers its menu. The prefix fixes the shell and flip
orientation, so every queried digit agrees. Thus, in the full declared family,
**the endpoint fibre is exactly `3^(24-|R(T)|)`**.

A censored frontier observes only `R_seen` contained in `R(T)`. Its interval is
`1 <= fibre <= 3^(24-|R_seen|)`; equality with the upper endpoint follows only
when the query set is complete. This also applies to a finite prefix law when
its queried set and endpoint are defined for that shorter fixed order.

```text
majority rule       |R| = 9    endpoint fibre = 3^15 = 14,348,907
copy-neighbour      |R| = 9    endpoint fibre = 3^15
all-supports table  |R| = 24   endpoint fibre = 1 (geometric argument)
```

The majority endpoint law has two constant configurations, at 1/2 each. The
first site has the all-open pinned menu; every later site takes the majority
of already formed neighbors. These two atoms belong to its static set of
9,038 configurations, but the endpoint law puts no mass on the other members.
For all supports, every binary prefix has positive probability, so all 24
geometrically accessible digits are genuinely queried.

**Total-variation-one witness.** Change, in the majority table, the single
digit carried by the orbit of `(0, open, open, open, open, open)`. It is one of
the 20 invisible digits, so the pair shares all four visible digits and
therefore one admissible set. Under the changed table the second site in the
order takes the value opposite to the first, so no formed configuration is
constant, while under the majority table every one is. The supports are disjoint
and the total variation is exactly 1: `(B)`-separation inside one `(A)`-class.
The event that all final bits are equal separates the laws; it reads no history.

**A declared family with censoring.** The 32 arithmetic codes are the base-3
expansions of `j * floor(3^24 / 32)`, `j = 0..31`. Their observed counts range
from 6 to 24, with the complete original histogram and eleven censor flags
retained. Twelve rows observe at least 23 digits and therefore have fibre at
most three; the ten observing all 24 have singleton fibres. These are upper
bounds within this declared finite set, not a generic-table claim. The runner
adds the actual cap-one all-support control: nine observed digits give an upper
bound of 14,348,907 while the true fibre is one.

## Corollary

1. The static map `A(T)` ignores twenty digits on every lattice of the declared
   profile type. On the 3^3 torus it has exactly 81 classes of size 3^20.
2. Under the supplied fixed order and uniform lift, endpoint statistics can
   distinguish tables inside an `A(T)` class. The TV-one event uses only final
   bits; access to the event ordering is unnecessary.
3. This finite classification does not identify the unrestricted probability
   law, derive formation or provide physical preparation/ensemble access.

## Reading and interfaces

Static support sets and endpoint probability laws answer different questions.
Seeing one actual configuration is not querying membership of every possible
configuration, and it is not knowing the full endpoint distribution. A supplied
readout/preparation protocol is still required to use either mathematical map
as a physical experiment. No physical law is selected.

- **Partial configurations.** Static membership `A_p(T)` and sequentially
  reachable prefixes `R_p(T)` differ. Neither is a definition of the other.
  Later neighbors do not erase an earlier permanent Record.
- **Larger tori.** The complete-profile upper bound of 81 is structural.
  Arbitrary `L` to `L+1` refinement is not proved: periodic domains are not
  nested profile-preserving lattices. A finite witness can be padded only when
  each recorded site's shell, including its open-neighbor buffer, is preserved.
- **Other lifts.** The endpoint proof here uses the stipulated uniform lift.
  It does not classify all measures on M2(C) or infer a physical rate.

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
geometry_orders: 3
original_lex_frontier_calls_and_distinct_tables: 35 / 35
original_censored_family_rows: 11 / 32
majority_endpoint_atoms_and_exact_fibre: 2 / 14348907
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
- **`(B)` on a declared finite set:** original lex-order atoms and censored
  frontiers are preserved. Their exact/upper-bound status follows from the
  endpoint proof; the other two orders have only geometric profile checks.
  No random number generator is used. The added small controls do not supply
  the missing physical process or readout bridge.

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
T4's exact fibre theorem distinguishes complete queried sets from censored
observations. The cap-one control rejects the old lower-bound inference.
The endpoint-TV example and original finite histogram are retained.

## Review record

The September-8 joint correction preserves the original note/cache under
`archive/notes` and all original numeric evidence. The companion partial-mask
and injectivity studies now have their own conditional results; they do not
retroactively prove a physical oracle or arbitrary-size extension here.
This source applies no scientific grade or audit status. Formal audit remains
deferred by the owner; source review and repository checks are separate.
