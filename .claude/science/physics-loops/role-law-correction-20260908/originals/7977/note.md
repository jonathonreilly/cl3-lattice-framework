---
claim_id: the_designed_matter_law_is_read_from_records_only_where_its_role_alphabet_realises_an_adjacency_the_role_table_is_blind_on_95_percent_of_partial_entries_while_every_two_and_three_site_record_pattern_is_exercised_bounded_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Exact and finite. The designed matter law of PR #7834 is read as PR #7939 reads it: the minimal covariant support table over the five-symbol role alphabet {C0, C1, E, F, Q}, whose menu at each profile the period-(4,2,2) superlattice role pattern realises is exactly the roles the pattern puts there and is empty elsewhere. Two offset sets are treated, the six nearest neighbours and the twelve of NN with {+-2 e_d}; the readout is the partial-configuration readout of PR #7928 and PR #7934 applied to roles, unrecorded sites reading as open. The role tori are 4x2x2, 4x4x2 and 4x4x4; the record tori are 4x4x4 and 8x4x4; the censuses and the star certificates are on Z^3. The nearest-neighbour table has 7 of 4,000 complete and 84 of 11,130 partial entries exercised, from 18 pairs, 17 profiles of 15,625 and 6 orbits of 800, and from 794 pairs, 655 profiles of 46,656 and 61 orbits of 2,226. On 4x4x4 all 2,048 nearest-neighbour-admissible role configurations exercise exactly those 18 pairs, the sub-configurations of the 48 sectors exactly those 794, and every excitation the parent notes define is an assignment of the free edge bits that reads back to the same role configuration and adds nothing. Under the partial readout on 4x4x4, 435 unexercised entries are read as absent, each with a re-verified witness, and 10,611 of 11,130 entries, 95.34 per cent, are blind; 9,919 of them are blind on every torus because their profile carries one of the 17 ordered role adjacencies of 25 that the pattern never realises. The certified fibre bounds are 2^1580 and 2^10599 on 4x4x4, and 2^478 under the complete readout; the blind set never shrinks with torus size or with admitted excitations. The 12-offset table is blind on 454,637,516 of its 454,664,880 partial entries, 99.994 per cent, with 16,333 self-adjacency entries left undecided. Over binary records the 48 template cylinders are disjoint on the 5x5x5 window, every 2-site and 3-site partial record pattern inside it is exercised, 496 of 496 and 61,008 of 61,008, and 97.04 per cent of the 4,961,984 four-record patterns are, with 50,968 undecided; a 39-offset rotation-closed window containing no nearest neighbour pins the cylinders on 4x4x4 and on 8x4x4, and no configuration outside every cylinder violates the 5x5x5 record rule at six or fewer sites. The 201 pinning and 17 minimal windows of the 512-window sweep are quoted from the source computation and are not recomputed by the runner. No physical law is selected."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/matter_law_readout_blind_where_role_alphabet_realises_no_adjacency_check_2026_09_04.py
registry_id: matter_law_readout_blind_where_role_alphabet_realises_no_adjacency_2026_09_04
---

# The designed matter law is readable on its exercised entries and blind on every entry that carries an adjacency it never realises: the fibre of the role readout is at least `2^1580`, and over records the small patterns are all exercised

**Date:** 2026-09-04

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.

**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/matter_law_readout_blind_where_role_alphabet_realises_no_adjacency_check_2026_09_04.py`](../scripts/matter_law_readout_blind_where_role_alphabet_realises_no_adjacency_check_2026_09_04.py)

**Runner cache:**
[`logs/runner-cache/matter_law_readout_blind_where_role_alphabet_realises_no_adjacency_check_2026_09_04.txt`](../logs/runner-cache/matter_law_readout_blind_where_role_alphabet_realises_no_adjacency_check_2026_09_04.txt)

**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), [`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md),
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Every count is an exact enumeration over a named finite torus or, for the censuses and the star certificates, over Z^3 with the orbit totals supplied by Burnside. Every unexercised entry of the nearest-neighbour role table is decided on the smallest torus without a solver -- the type-ii entries by the reciprocal obstruction, which is torus-independent, and the type-i and type-iii entries by a complete depth-first search -- and, where pysat is present, CaDiCaL re-decides them on all three role tori and agrees entry by entry. The visible entries carry witnesses re-verified by a scalar path. The fibre bounds are certified by an ordering argument and by explicit double stars, not estimated. The 201 pinning and 17 minimal windows of the 512-window sweep are quoted, not recomputed. No physical law is selected."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Decide the 16,333 self-adjacency entries of the 12-offset table and the 50,968 four-record patterns; then ask whether a role alphabet realising every adjacency can carry the same pattern."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

PR #7834 puts a fermion on `Z^3` at one qubit per site by declaring a **superlattice role pattern**: a site's role is its coordinate parity,
and a repeating arrangement of pinned values with period `(4, 2, 2)` along a chosen axis pins a corner to `(s[ax] / 2) mod 2`, a face to `0`,
a cube centre to `1`, and leaves every coarse edge site free as a live qubit -- `48` sectors. PR #7939 encodes that pattern over the
five-symbol role alphabet `{C0, C1, E, F, Q}` and reads the designed matter law as the **minimal covariant support table** `T0` on a
rotation-closed offset set: each realised profile gets exactly the roles the pattern puts at its centre, and every other profile gets the
empty menu. PR #7928 and PR #7934 established that the partial-configuration readout determines a covariant support table -- which law holds
is a matter of what the records show -- and PR #7939 reported that the pattern exercises `2.74 %` of the covariant partial table.

**So can the designed matter law be read from the records that exercise it?** This note answers that question exactly, on named tori, for the
role-level law and for the record-level one. Records register; the lattice is physical; the pattern is an arrangement of pinned values.

## Supplied surface (quoted)

Admissibility and Record, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`), with reading note (3) fixing "admissible":

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

> "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

From the campaign: PR #7939's role law and its census, taken as supplied -- `18` realised `(role, profile)` pairs, `6` orbits of `800`
complete and `61` of `2,226` partial, `2.74 %`. From PR #7928 and PR #7934: the partial-configuration readout `A_p`, and PR #7934's class --
covariant label-equivariant tables over a **binary** record alphabet with no empty menu, `3^24` of them, on which the readout is injective and
every fibre a singleton. From the excitation notes: every excitation named there lives on the coarse edge sites, which is exactly the part the
role alphabet drops.

## T1 -- the census, and the entries the census does not count

PR #7939's role census is reproduced with fresh code and extended to the table **entries**, which that note does not report. A covariant
support table is a bit per `(role, profile orbit)`, so the table space here is `2^{5 x orbits}`.

```text
complete readout   18 pairs   17 profiles of 5^6 = 15,625    6 orbits of   800     7 entries of  4,000
partial  readout  794 pairs  655 profiles of 6^6 = 46,656   61 orbits of 2,226 = 2.74 per cent   84 entries of 11,130
entries by role, complete / partial   C0 1 / 10   C1 1 / 10   E 3 / 36   F 1 / 18   Q 1 / 10
covariance: the rotation closure of one orientation equals the union over the three      true
12 offsets, NN with {+-2 e_d}:  22 pairs, 7 orbits of 10,229,375;  3,404 partial entries of 454,664,880
```

The orbit totals are Burnside counts over the `24` proper rotations. `7 of 4,000` and `84 of 11,130` are the numbers the readability question
is actually about: PR #7939's `2.74 %` counts profile orbits, and an orbit with a nonempty menu still leaves four of its five entries
unexercised.

## T2 -- the exercised set of the whole admissible set is the law itself

```text
torus      NN admits    12-offset admits    sectors    12-offset = sectors    NN-admissible exercises
4x2x2             32                  16         16    true                   14 pairs
4x4x2            128                  32         32    true                   16 pairs
4x4x4          2,048                  48         48    true                   18 pairs = T0
```

On `4x4x4` every one of the `2,048` configurations the nearest-neighbour role table admits -- including every non-striped corner pin field,
that is, every pin defect -- exercises exactly the `18` pairs of `T0`, and the sub-configurations of the `48` sectors exercise exactly the
`794` pairs of `T0^p`, `84` entries. **For a minimal support law the exercised set of its whole admissible set is the law**: every entry of
`T0` is realised by a sector, and admissible configurations realise nothing else by definition. The excitations add nothing, and not by a small
margin. Reading the role at every site from the records alone through the `5x5x5` window, torus-wrapped:

```text
all 1,024 = 16 x 2^6 cylinder record configurations on 4x2x2   unique role everywhere; 16 role configurations = the sectors
4x4x4: 8 coarse vertices, 24 edge sites, 48 x 2^24 = 805,306,368 cylinder record configurations
   the sea 1, single complements (hops) 24, double complements 276, one representative of each of the 128 vertex-parity
   classes -- every family reads to ONE role configuration and 12 raw pairs
   fillings by odd-corner number N:  131,072 / 3,670,016 / 9,175,040 / 3,670,016 / 131,072  =  2^24
union growth of the exercised set over all of these                                    zero
```

One sector's `12` raw pairs already cover all `7` complete entries, the gap to `18` being the rotation covariance. For the partial table, a
`4x4x4` configuration realises at most `64` pairs, so at least `2` configurations are needed and `84` star sub-configurations suffice. The
fermion lives in the free edge bits, which the role alphabet drops; the exercised set is a function of the pinned pattern alone.

## T3 -- the reading theorem, and the exact obstruction

Every pair of `T0` is realised by an admissible configuration, so every table `T'` with `A(T') = A(T0)` contains `T0`, and

```text
fibre(T0) = { T0 u S  :  S subset of the unexercised entries, jointly invisible }
```

Call an unexercised entry `e` **visible** if `A(T0 u {e}) != A(T0)`, **blind** otherwise, and let `B` be the blind set. A visible entry lies in
no such `S`; a blind entry `b` gives `T0 u {b}` in the fibre. Hence `1 + |B| <= |fibre| <= 2^|B|`, and **the fibre is a singleton exactly when
no unexercised entry is individually blind**: the readout reads every exercised entry as present, every visible entry as absent, and nothing at
all on `B`.

**The reciprocal obstruction.** If the profile of `(r, P)` shows a recorded symbol `s != r` at an offset at which the pattern never shows `s`
from `r`, then `(r, P)` is blind on every torus: any configuration realising it has, at that offset, a site of role `s` whose own profile shows
`r` at the reciprocal offset -- the same never-realised adjacency -- so that site's entry is unexercised too, and it cannot lie in the orbit of
`(r, P)`, its role being `s` and not `r`. Adjacency realisation is symmetric, and the pattern realises only `8` of the `25` ordered role
adjacencies: `17` are never realised. Classify an unexercised entry by the never-realised adjacencies its profile carries: **type i**, none;
**type ii**, one with a cross symbol `s != r`; **type iii**, only `r` itself.

```text
readout, torus     exercised   visible   blind    type i vis/blind   type ii vis/blind   type iii vis/blind
complete 4x2x2             7        12   3,981           4 /   59           0 /  3,673          8 /   249
complete 4x4x2             7        12   3,981           4 /   59           0 /  3,673          8 /   249
complete 4x4x4             7        18   3,975           5 /   58           0 /  3,673         13 /   244
partial  4x2x2            84       136  10,910          71 /  172           0 /  9,919         65 /   819
partial  4x4x2            84       286  10,760         160 /   83           0 /  9,919        126 /   758
partial  4x4x4            84       435  10,611         243 /    0           0 /  9,919        192 /   692
```

Type ii is blind on every torus, as the obstruction predicts, and on `4x4x4` type i is visible without exception, by an explicit all-else-open
star configuration; the type-i blindness on the smaller tori is the size-`2` direction identifying `+e` with `-e`. Each of the `435` visible
partial entries and each of the `18` visible complete entries on `4x4x4` carries a declared witness, re-verified by a scalar check: admissible
under `T0` with the entry's orbit added, not admissible under `T0`, and the entry used. The blind set shrinks as the torus grows -- no entry is
blind on `4x4x4` that is not blind on `4x2x2`, and `299` partial and `6` complete entries are blind only on `4x2x2` -- and it stops at the
type-ii core together with the geometrically obstructed self-adjacency entries. It cannot reach zero.

```text
partial readout on 4x4x4:  exercised 84,  read as absent 435,  blind 10,611 of 11,130 = 95.34 per cent
certified fibre bounds:    2^1580 <= |fibre| <= 2^10599      (complete readout: 2^478 <= |fibre| <= 2^3975)
the upper bound's structure: 6 double stars, 12 hubs, 1,337 leaves, all 1,343 edges realised explicitly
```

The lower bound is certified: order the roles, take the blind entries all of whose never-realised symbols are cross symbols above `r`, and no
admissible configuration can use one of them, so every subset of that family lies in the fibre. The bound does not shrink as the torus grows --
the type-ii core is torus-independent, and the certified family uses only cross adjacencies -- nor as the excitations and the pin defects are
admitted, since by T2 they exercise nothing new.

**The law that pins.** The `12`-offset table, the one that admits exactly the `48` sectors, has `454,664,880` partial entries, `3,404` of them
exercised. Counting by Burnside with the per-class alphabets, `454,560,782` -- `99.977 %` -- carry a cross never-realised adjacency and are
blind on every torus. The remaining `104,098` are enumerated: `3,404` exercised, `7,627` visible by the star certificate, `76,734` blind by a
forced-neighbour certificate, and `16,333` undecided, every one of them a self-adjacency entry. So the pinning law is blind on at least
`454,637,516` of its entries, `99.994 %`, and readable on at most `27,364`.

## T4 -- over records the picture inverts

The record-level law `R_W` demands that the binary pattern on a window `W` at every site agree with one of the `48` templates on that
template's pinned sites, the free edge bits wild.

```text
window                        star (7)   NN+AX2 (13)   L1<=2 (25)   3x3x3 (27)     5x5x5 (125)
exercised window patterns          128         1,638      391,233      101,626     2^57.05 of 2^125
4x2x2, outside every cylinder   64,512        13,981          186          154               0
```

On the `5x5x5` window the `48` template cylinders are pairwise disjoint -- `0` of `1,128` pairs consistent -- so the exercised patterns number
exactly `148,935,859,368,886,272`, a fraction `2^-68`, with `36`, `44`, `51` or `54` free sites per template. The record-level exercised
fraction is not a meaningful percentage; the role table is the compressed object.

**Where the record rule closes.** Over the `512` rotation-closed windows inside `5x5x5`, `201` pin the cylinders on `4x4x4` and `17` are minimal
by inclusion. The smallest has **`39` offsets -- the centre, the `8` body diagonals `(1,1,1)`, the `6` axial `(2,0,0)` and the `24` of orbit
`(2,1,0)` -- and contains no nearest neighbour at all**; it pins again on `8x4x4`, each of its maximal proper rotation-closed sub-windows fails
to pin, and pinning is monotone under inclusion. Of the ladder only `5x5x5` pins. On `8x4x4` no configuration outside every cylinder violates
the `5x5x5` rule at `6` or fewer sites, while the `3x3x3` rule is violated at a single site, so any table that enlarges the `5x5x5` record rule
and admits something new does so through at least `7` violated sites at once.

**The partial record readout has no small blind entries.**

```text
2-site partial record patterns inside the window     496 of 496 exercised
3-site patterns (centre and two offsets)          61,008 of 61,008 exercised
4-site patterns (centre and three offsets)     4,814,888 of 4,961,984 = 97.04 per cent exercised;
                                                  of the 147,096 unexercised, 96,128 visible and 50,968 undecided
```

Over records all four value pairs occur at every offset, so there is no reciprocal obstruction to have: the type-ii blindness of T3 is
manufactured by the role alphabet, not by the pattern and not by the torus.

## Corollary

1. **The designed matter law is conditionally readable, with an exact obstruction.** Its exercised part is read exactly, from one sector for
   the complete table and from between `2` and `84` sub-configurations for the partial one; a further `435` unexercised entries are read
   exactly as *absent*; and it is blind on `10,611` of `11,130` partial entries.
2. **The obstruction is the role alphabet, not the vacuum.** No configuration exercises more than the vacuum does, because for a minimal
   support law the exercised set of its entire admissible set is the law itself; PR #7939's `2.74 %` is the fraction of the partial table
   where the law's menu is nonempty, not a statement about the vacuum's reach.
3. **The role table is blind wherever an entry's profile carries one of the `17` ordered adjacencies the pattern never realises** -- `9,919`
   entries of the partial table, blind on every torus. The fibre is at least `2^1580` and at most `2^10599`, and it never shrinks: not with
   torus size, not with pin defects, not with any excitation the parent notes define.
4. **Over records the blindness is absent at small patterns:** every `2`-site and every `3`-site partial record pattern inside the `5x5x5`
   window is exercised, and `97.04 %` of the four-record ones.
5. **So "records determine the law" holds for PR #7934's class** -- binary alphabet, every menu nonempty -- **and, for a minimal support law
   with empty menus, exactly when every unexercised entry is individually visible**, which fails as soon as the admissible set omits one
   adjacency. This law omits `17` of `25`.

**Disagreements with the expectation, stated plainly.**

- The question "which record configurations exercise more" has the answer *none*: the union over the excitations, the pin defects and all
  admissible configurations is exactly `T0`, respectively `T0^p`.
- The role table is not `3^{entries}`: with five roles the support version is `2^{5 x orbits}`; `3^24` is the binary case.
- The blind set is not the unexercised remainder. `435` unexercised entries are read exactly, as absent; the readable part is `519` of
  `11,130`, `4.66 %`, and what puts the rest out of reach is the alphabet's never-realised adjacencies, not the torus size and not the
  vacuum's rigidity.
- The record-level law does not need the nearest-neighbour offsets in order to close: a `39`-offset window without them pins the cylinders on
  both record tori.
- No parent defines a flux string, a particle-hole pair or a domain wall as a record configuration on this lattice, so those rows are absent
  for want of a definition, not by omission.

## Reading, not theorem

A law that says almost nothing says it about almost everything. The role rule names five kinds of site and then permits only eight of the
twenty-five ways two kinds can sit next to each other; every entry that asks about one of the other seventeen describes an arrangement the
pattern has no way to build, so the records can neither confirm nor deny it. That is not a shortage of records and not a shortage of
excitations: the arrangement the law produces is the largest thing the law admits, and it already shows everything the law has to show. Where
the same pattern is written in plain record bits, both values occur at every offset, every small pattern of two or three records really happens
somewhere, and the blindness is gone. What cannot be read is what the labelling invented.

## Interfaces

- **PR #7939**, the role census and the next-nearest-neighbour pinning rule, is the object read here; its `2.74 %` is re-derived and given
  its entry-level counterpart.
- **PR #7928** and **PR #7934**, the readability notes, supply the readout and the class on which it is injective; this note gives the exact
  condition under which their claim reaches a support law with empty menus. The same day's PR #7929, on the vacuum response under the rate
  ruler, shares no object with this note.
- **PR #7885**, the determinantal statistics note, supplies the reading of a full set of records at the coarse modes as an occupation pattern,
  used here only to name the excitation families; **PR #7889** and **PR #7891**, the shifting-record notes, supply the hop and the single- and
  double-complement families, each an assignment of the free edge bits and each shown here to leave the exercised set unchanged.

## Executable claim block

```text
registry_id: matter_law_readout_blind_where_role_alphabet_realises_no_adjacency_2026_09_04
census_pairs_profiles_orbits_complete: 18 / 17 of 15,625 / 6 of 800
census_pairs_profiles_orbits_partial: 794 / 655 of 46,656 / 61 of 2,226
entries_exercised_complete_and_partial: 7 of 4,000 / 84 of 11,130
admissible_sets_nn_and_twelve_offset: 32 / 128 / 2,048 and 16 / 32 / 48 = the sectors
exercised_set_of_the_whole_admissible_set: T0 on 4x4x4, T0^p from the sectors
excitation_families_one_role_configuration_each_union_growth: true / zero
cylinder_record_configurations_4x4x4: 805,306,368
never_realised_ordered_role_adjacencies: 17 of 25
partial_readout_4x4x4_exercised_visible_blind: 84 / 435 / 10,611 = 95.34 per cent
type_ii_blind_on_every_torus_and_complete_readout_4x4x4: 9,919 and 18 / 3,975
witnesses_reverified: 435 partial and 18 complete
fibre_bounds_partial_and_complete: 2^1580 to 2^10599 and 2^478 to 2^3975
twelve_offset_partial_entries_blind_undecided: 454,664,880 / 454,637,516 = 99.994 per cent / 16,333
record_cylinders_disjoint_on_5x5x5_and_exercised: true and 2^57.05 of 2^125
smallest_closing_window_offsets_and_nearest_neighbours: 39 and none
window_sweep_pinning_and_minimal_quoted: 201 of 512 and 17
record_rule_minimal_defect_number_on_8x4x4: greater than 6
two_and_three_record_patterns_exercised: 496 of 496 and 61,008 of 61,008
four_record_patterns_exercised_visible_undecided: 4,814,888 / 96,128 / 50,968
no_physical_law_is_selected: true
```

## Proof boundary

The theorem is the finite classification above and nothing wider.

- **Named tori, periodic, no open blocks.** `4x2x2`, `4x4x2` and `4x4x4` for the role readouts -- both laws' admissible sets, the visibility
  of every entry of the nearest-neighbour table, the witnesses and the fibre bounds. `4x4x4` and `8x4x4` for the record-level window sweep and
  the minimal defect number. `Z^3` for the censuses, the star certificates and the `2`-, `3`- and `4`-record counts. The `4x2x2` torus is
  degenerate -- `+d` and `-d` are the same site in the size-`2` directions -- which is why the type-i entries are not all visible there.
- **What is decided without a solver.** The censuses, the depth-first admissible sets, the Burnside totals, the `4x2x2` record ladder, the star
  certificates, the fibre bounds, the `12`-offset counts, and the `2`-, `3`- and `4`-record counts. Every unexercised entry of the
  nearest-neighbour table is decided on `4x2x2` without a solver: the `13,592` type-ii entries by the reciprocal obstruction, which is
  torus-independent, and the `1,447` type-i and type-iii entries by a complete depth-first search. Where pysat is present, CaDiCaL re-decides
  those `1,447` on all three role tori and agrees entry by entry, decides a declared type-ii sub-family of `124` entries on `4x4x4` and finds
  them blind, supplies the witnesses for the `192` visible type-iii entries, and decides the record-level window and defect rows.
- **What is quoted, not recomputed.** The `201` pinning and `17` minimal windows of the `512`-window sweep are quoted from the source
  computation's output line; the runner recomputes the declared smallest closing window on both record tori, its maximal proper
  rotation-closed sub-windows, and the ladder row.
- **Not decided here.** The exact fibre, only the bounds `2^1580` and `2^10599`; the `16,333` self-adjacency entries of the `12`-offset table;
  the `50,968` four-record patterns; whether the at least seven violated sites of the record rule can all carry one orbit entry; the
  record-level partial readout beyond four records; anything for a side length beyond `8x4x4`. Every statement is about supports, in the sense
  reading note (3) fixes; the distribution-valued lift is untouched.
- **Supplied and stipulated.** The pattern, the role alphabet, the reading of "law" as a minimal covariant support table with empty menus, the
  readout, the excitation families as edge-bit assignments, and the tori; nothing is derived from the axioms about which law holds, no axiom
  is edited, and no physical law is selected. No sampling, no seed and no random number generator is used anywhere.

## Honest-auditor read

The load-bearing objects are, in order: the identity of T2 -- that the exercised set of the whole admissible set is the law, checked as a set
equality on `4x4x4` and not by cardinality; the reciprocal obstruction of T3, a two-line argument carrying `13,592` of the `15,039` unexercised
entries and the reason the fibre can never be a singleton; and the `243 / 0` type-i row on `4x4x4`, which is what makes the `435` read as absent
rather than blind. Attack them in that order. The first two are complete enumerations with small witnesses and the easiest to re-run; the third
rests on explicit star configurations, each re-verified by a scalar path, so it needs no solver either. The weakest rows are the `12`-offset
`16,333` and the four-record `50,968`, both left undecided and both counted, and the `201 / 17` sweep, which is quoted. The claim most likely to
be over-read is the headline percentage: `95.34 %` measures the role alphabet's never-realised adjacencies as much as it measures the law, and
the record-level rows of T4 are the control that shows it.

## Review record

This note answers a readability question about one designed law and proposes no law of its own. Hard landing conditions are a fresh runner and
cache pair, a current citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane.
