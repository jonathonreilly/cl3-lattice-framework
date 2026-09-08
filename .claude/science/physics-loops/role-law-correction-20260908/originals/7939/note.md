---
claim_id: the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Exact and finite, over the five tori 4x2x2, 4x4x4, 8x4x4, 5x4x4 and 7x4x4 only. The superlattice role pattern of PR #7834 is read as a symbol configuration over the 5-symbol role alphabet {C0, C1, E, F, Q}; the minimal covariant support rule realised by the pattern on a rotation-closed offset set is the rule whose menu at each realised profile is exactly the set of roles the pattern puts there and is empty elsewhere. Over that alphabet the pattern realises 18 (role, profile) pairs, 17 profiles of 5^6, 6 rotation orbits of 800, and the rotation closure of one axis orientation's realised set equals the union over the three orientations. The nearest-neighbour role rule admits 8 x 2^{#corners} configurations -- 32, 2,048 and 524,288 on the three commensurate tori against 48 sectors -- and 0 on the two incommensurate ones; NN together with {+-2 e_d}, 12 offsets of the 5x5x5 window's 124, admits exactly the 48 sectors on 4x4x4 and 8x4x4 as a set equality and 0 on the incommensurate tori, while NN with {+-3 e_d} and NN with {(+-1,+-1,0)} do not pin; the corner pin field is free under NN, laminar under NN with {(+-1,+-1,0)} (8 x 20 = 160 on 8x4x4) and striped under NN with {+-2 e_d} (8 x 6 = 48). Over the binary record alphabet a complete solver-free enumeration on the 4x2x2 torus and, where pysat is present, CaDiCaL on the 4x4x4 torus both place configurations outside every sector cylinder for the star, NN with {+-2 e}, L1<=2 and 3x3x3 windows and none for 5x5x5; all 128 binary star patterns are realised; the centre role is a function of the window's record values only at L-infinity radius 2. The pattern exercises 6 of 800 covariant nearest-neighbour role-table orbit entries completely and 61 of 2,226 partially. The separation counts of the parent's minimality criterion are not reproduced here and are excluded; nothing above rests on them. No physical law is selected."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
runner: scripts/role_pattern_next_nearest_neighbour_rule_roles_not_records_check_2026_09_04.py
registry_id: role_pattern_next_nearest_neighbour_rule_roles_not_record_values
---

# The superlattice role pattern is a next-nearest-neighbour support rule over roles, and roles are not record values

**Date:** 2026-09-04

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/role_pattern_next_nearest_neighbour_rule_roles_not_records_check_2026_09_04.py`](../scripts/role_pattern_next_nearest_neighbour_rule_roles_not_records_check_2026_09_04.py)

**Runner cache:**
[`logs/runner-cache/role_pattern_next_nearest_neighbour_rule_roles_not_records_check_2026_09_04.txt`](../logs/runner-cache/role_pattern_next_nearest_neighbour_rule_roles_not_records_check_2026_09_04.txt)

**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
[`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md),
[`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Every count is an exact enumeration over a named finite torus, with the sector comparisons carried out as set equalities rather than cardinalities. The record-level rows are decided completely and without a solver on the 4x2x2 torus and, where pysat is present, again by CaDiCaL on the 4x4x4 torus. The minimality statement is over rotation-closed offset sets containing the nearest neighbours and lying inside the 5x5x5 window. No physical law is selected and no lattice beyond the five named tori is claimed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Ask whether a record-native encoding of the role labels exists at one bit per site; then whether the sector choice can be posed as a past hypothesis rather than a supplied datum."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

PR #7834 puts a fermion on `Z^3` at one qubit per site by declaring a **superlattice role pattern**: a site's **role** is
its coordinate parity -- all coordinates even is a *corner*, one odd a coarse *edge* site, two odd a *face*, three odd a
*cube centre* -- and a repeating arrangement of pinned values with period `(4, 2, 2)` along a chosen axis pins a corner to
`(s[ax] / 2) mod 2`, a face to `0`, a cube centre to `1`, and leaves every edge site free as a live qubit: `16` translates
for each of `3` axis orientations, `48` **sectors**. Its Theorem 2 selects that pattern exactly, by a marker rule read on a
`5x5x5` window, and reports the window minimal; its Theorem 3 reports that a rule reading only the *values* in a seven-site
star is vacuous there. PR #7934 established, on the `3^3` torus, that the partial-configuration readout is injective on the
covariant support tables: which law holds is a matter of what the records show. This note bounds the reach of that result.
**Is the designed matter law a nearest-neighbour support rule, and is it readable from records?** Records register; the
lattice is physical; the pattern is an arrangement of pinned values on the plain cubic lattice, not a new lattice.

## Supplied surface (quoted)

Lattice, Qubit and Admissibility, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`), with reading note (3) fixing
the sense of "admissible":

> "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."

> "Each site has a domain of local possibilities. The full one-site possibility domain has algebraic presentation `M_2(C)`."

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

`M_2(C)` names two local possibilities: **one bit of record per site**. That is the whole of the tension this note quantifies.

## T1 -- the role census (exact)

Encode the pattern over the `5`-symbol role alphabet `{C0, C1, E, F, Q}`: a corner showing `0` or `1`, an edge site whatever
its qubit says, a face, a cube centre. The **minimal covariant support rule** on a rotation-closed offset set `N` gives each
profile the pattern realises exactly the roles the pattern puts at its centre, and every other profile the empty menu -- the
strongest rule the pattern permits.

```text
realised (role, profile) pairs, one axis orientation closed under 24 rotations = 18
union over the three axis orientations of the raw realised pairs               = 18  (the same set)
distinct realised profiles                                                     = 17  of 5^6 = 15,625
rotation orbits realised                                                       =  6  of 800
```

The third line is the covariance statement: closing one orientation's realised set under the proper cubic rotations gives
**exactly** the union over the three orientations, so "one covariant rule" and "`48` sectors" are the same object, as PR
#7834 has them. The `17` rows are one corner row, `12` edge rows (four corner-pin pairs on each of three axes), three face
rows and one cube-centre row.

Two things this encoding does, both load-bearing below. It **refines** the record value -- separating a corner showing `0`
from a face showing `0`, which no record does -- and it **forgets** the free edge bits entirely: every edge site is `E`
whatever its qubit says, and the fermion lives in exactly the part the role alphabet drops.

## T2 -- the nearest-neighbour role table does not pin the pattern (exact counts)

```text
T(E E E E E E)      = {C0, C1}      every corner has this profile, so the menu holds both
T(C_a C_b F F F F)  = {E}           all four (a,b) in {0,1}^2, on each of three axes
T(E E Q Q E E)      = {F}           faces;    T(F F F F F F) = {Q}   cube centres
coarse (skeleton) pairs                                            = 8
refinements of a realised coarse pair that are NOT realised        = 0
```

Every corner carries the same profile `E E E E E E`, so the table must admit both `C0` and `C1` there; every edge site
realises all four corner-pin pairs on its axis; and no refinement of a realised coarse pair is unrealised. The
nearest-neighbour table therefore constrains the corner pin bit not at all. It pins the period-`(2,2,2)` **parity skeleton**
exactly -- `8` translates, nothing else -- and leaves the pin field free:

```text
torus      NN admits          = 8 x 2^{#corners}     sectors
4x2x2             32          = 8 x 2^2                   16
4x4x4          2,048          = 8 x 2^8                   48
8x4x4        524,288          = 8 x 2^16                  48
5x4x4              0                                       0
7x4x4              0                                       0
```

The `(4,2,2)` period is carried entirely by the corner pin field; the role structure itself is only `(2,2,2)`. A
nearest-neighbour window holds at most two corners, never two on two different axes -- precisely what a covariant rule would
need in order to say that the alternation runs along one axis and one axis only. On the incommensurate tori every branch
closes at `NN` already, so the frustration PR #7834 reports at `5x5x5` is a property of the `(2,2,2)` skeleton and needs no
range at all.

## T3 -- the minimal pinning neighbourhood is next-nearest-neighbour (exact)

Among rotation orbits of offsets inside the `5x5x5` window the only ones of size `6` are `{+-e_d}` and `{+-2 e_d}`, so the
only rotation-closed offset set containing `NN` with at most `12` offsets and lying inside that window is `NN` together with
`{+-2 e_d}`: **`12` offsets of the window's `124`**.

```text
neighbourhood                4x2x2     4x4x4      8x4x4    5x4x4   7x4x4   pins?
NN (6)                          32     2,048    524,288        0       0   no
NN with {+-3 e_d} (12)          32     2,048      2,048        0       0   no
NN with {(+-1,+-1,0)} (18)      32        64        160        0       0   no
NN with {+-2 e_d} (12)          16        48         48        0       0   YES
NN with {(+-1,+-1,+-1)} (14)    16        48         48        0       0   yes
L1<=2 (24) / 3x3x3 (26) / 5x5x5 (124)   as the sectors on all three commensurate tori
```

Every `YES`/`yes` row was compared with the sector set **as a set**, not by cardinality. `NN` with `{+-2 e_d}` therefore
admits exactly the `48` sectors on `4x4x4` and on `8x4x4`, exactly the `16` the `4x2x2` torus holds, and nothing at all on
`5x4x4` and `7x4x4`.

**What the extra configurations are.** On `8x4x4` the corner sublattice is a `4x2x2` grid carrying a binary pin field, and
the ladder is a clean three-step chain:

```text
all binary pin fields                                        2^16 = 65,536   NN admits every one   (8 x 65,536 = 524,288)
laminar: constant on the planes normal to one coarse axis            20      NN with {(+-1,+-1,0)} admits exactly these (8 x 20 = 160)
striped: alternating with period 2 along one axis                     6      NN with {+-2 e_d}     admits exactly these (8 x  6 =  48)
```

Nearest neighbours are load-bearing for the skeleton and the `+-2` offsets for the pin field; neither alone suffices, the
`+-2` offsets lying inside `2Z^3`, whose constraint graph has eight parity components.

## T4 -- over the record alphabet (complete on 4x2x2; SAT on 4x4x4)

A role is not a record value. Building the minimal covariant support rule for a window `W` over **binary records** -- a
site's value pattern on `W` must match one of the `48` templates, the free edge bits wild -- and asking for a configuration
admissible under it and outside every sector cylinder:

```text
window                  star (7)   NN with {+-2 e} (13)   L1<=2 (25)   3x3x3 (27)   5x5x5 (125)
4x2x2, complete count   64,512     13,981                 186          154          0
   of admissible configurations lying outside every sector cylinder; at 5x5x5 all 1,024 = 16 x 2^6 lie inside one
4x4x4, CaDiCaL          SAT        SAT                    SAT          SAT          UNSAT
```

The `4x2x2` row is a complete enumeration over all `2^16` binary configurations carrying no solver; the `4x4x4` row is
CaDiCaL over `64` value variables and `3,072` template indicators, and runs where pysat is present. Only the `5x5x5` window
pins, confirming PR #7834's Theorem 2 by a method that note does not use. The `12`-offset role rule of T3 does **not**
transfer: the same offsets over binary values admit configurations outside every cylinder. What buys it its economy is the
alphabet, not the geometry.

Two further record-level facts complete the picture.

```text
binary 7-site star patterns realised over all 48 sectors and all free edge bits = 128 of 128
the centre role is a function of the window's record values:  star no   NN with {+-2 e} no
                                                              L1<=2 no   3x3x3 no   5x5x5 yes
```

The first reproduces PR #7834's Theorem 3 item 2: the minimal covariant nearest-neighbour table over records is the
all-permissive one. The second says a role is recovered from records only at `L`-infinity radius `2`, with the failures
explicit -- at the star and at `NN` with `{+-2 e}` a corner is mistakable for an edge site, at `L1<=2` an edge site for a
cube centre, at `3x3x3` a corner for a face.

**The cost of the alphabet.** Five role symbols is three bits per site; the Qubit axiom's `M_2(C)` gives one. So a
nearest-neighbour rule *over roles* is a **radius-3** rule *over records* and the `12`-offset rule a radius-4 one: both
wider than a nearest-neighbour rule, the first still narrower than the radius-2 marker window whose minimality over records
is confirmed independently above. Roles are a *derived* label, a radius-2 function of the records.

## T5 -- readability, and what the designed law is made of (exact)

Applying the partial-configuration readout of PR #7934 to the role rule, with unrecorded sites reading as open:

```text
rotation-orbit table entries the complete pattern exercises      =  6 of 800
(role, profile) pairs realisable from sub-configurations         = 794
partial profiles realised                                        = 655 of 6^6 = 46,656
partial rotation-orbit table entries realised                    = 61 of 2,226 = 2.74 %
```

For each such entry the records show only that the menu *contains* the realised role, never that it excludes anything. The
other `2,165` entries are unexercised: the pattern never puts a site in that profile. This is a categorically weaker readout
than PR #7934's, and the difference is the crux. There the reader may place records anywhere; here the record configuration
is not free -- it is the pattern, up to `48` sectors and the free edge bits. **A law whose ground state is a single rigid
arrangement makes almost all of itself unreadable by that arrangement.** The `48`-fold degeneracy does not help: the sectors
are rotations and translates of one another, exercising the same entries.

The designed matter law is three things, and only the first is a support rule at all.

| part | what it is | how the readability result reaches it |
|---|---|---|
| the **role support rule** | a covariant support rule whose admissible set is exactly the `48` sectors: `12` offsets over roles, `L`-infinity radius `2` over records. Not nearest-neighbour in either alphabet. | Through its exercised part only -- `6` of `800` entries completely, `61` of `2,226` partially. |
| the **sector choice** | which of the `48` the record background is: four bits of phase together with one of three axis orientations, fixed once, globally. Past-hypothesis-shaped. | Not at all. The rule cannot pick it; the `48` are exactly degenerate. |
| `S_f`, `B_v`, `T_ij` | the encoding's face stabilizers, corner parities and hops -- the fermion itself, acting on the free edge qubits the role alphabet drops. | Not at all, and not by degree: these are Hamiltonian terms, not a support table. |

**The third row is a category error, and it should be written down as one.** PR #7934 established that the
partial-configuration readout determines a covariant nearest-neighbour *support table*: a predicate on records, saying which
local value is admissible given the neighbours. `T_ij = (i/2) A_ij (B_i - B_j)` is not such a predicate; it partitions
nothing into admissible and inadmissible. Applying "records determine the law" to the Hamiltonian terms is not a weak
inference, it is an inference about the wrong kind of object.

## Corollary

1. **The superlattice role pattern is pinned by a next-nearest-neighbour support rule over roles**, `12` offsets,
   and by no nearest-neighbour rule: the nearest-neighbour role table admits `8 x 2^{#corners}` configurations --
   `524,288` on `8x4x4` where `48` were wanted.
2. **Roles are not record values.** A role needs three bits where the Qubit axiom gives one, and is recovered from
   records only at radius `2`; so over records the rule has radius `3`, wider than a nearest-neighbour rule and
   narrower than the `5x5x5` marker window, whose minimality over records is confirmed here independently.
3. **The designed law is three things**: a next-nearest-neighbour role rule -- Admissibility's kind, but not
   nearest-neighbour -- a supplied four-bit sector choice, and a supplied Hamiltonian, to which the readability
   result does not apply.
4. **The role law is almost entirely unexercised by the arrangement it produces**: `2.74 %` of the covariant table,
   so it cannot be read off its own ground state.
5. Hence **"records determine the law" reaches the designed matter law only through its support-rule part, and only
   where the records exercise it.**

## Reading, not theorem

The arrangement that makes the particle is held in place by a rule that looks two sites away, not one, and the labels it
uses cost three bits where the lattice gives one. So the particle's law is not a neighbour rule of the kind the axioms name,
and most of it is never exercised by the arrangement itself, so records cannot read it from the vacuum. What the readability
result reaches is the rule's support part; the particle's dynamics is a different kind of object, and the campaign's result
says nothing about it.

## Interfaces

- **A record-native role encoding.** Whether the four role classes can be carried at one bit per site, by a
  construction that does not smuggle in a second bit, is untouched here.
- **The sector choice as a past hypothesis.** Whether a globally fixed choice among exactly degenerate sectors is a
  boundary condition, a symmetry-breaking event or an initial record is decided by nothing computed here.
- **The marker window's reduction.** The `12`-offset role rule shows the `5x5x5` marker rule doing two separable
  jobs, a nearest-neighbour one and a `+-2` one; a matching record-level factorisation is open.

## Executable claim block

```text
registry_id: role_pattern_next_nearest_neighbour_rule_roles_not_record_values
role_alphabet_and_realised_pairs_profiles_orbits: 5 / 18 / 17 / 6 of 800
covariance_closure_equals_three_orientation_union: true
nn_admissible_4x2x2_4x4x4_8x4x4: 32 / 2048 / 524288
nn_admissible_incommensurate_5x4x4_7x4x4: 0 / 0
sectors_4x2x2_4x4x4_8x4x4: 16 / 48 / 48
minimal_pinning_offsets_and_window: 12 of 124
nn_ax2_admissible_4x4x4_8x4x4_set_equality: 48 / 48 / true
failing_siblings_ax3_and_diag2_on_8x4x4: 2048 / 160
pin_field_families_all_laminar_striped: 65536 / 20 / 6
record_windows_outside_cylinders_4x2x2: 64512 / 13981 / 186 / 154 / 0
record_windows_4x4x4_cadical: SAT / SAT / SAT / SAT / UNSAT
binary_star_patterns_realised: 128 of 128
role_determined_by_records_at_radius: 2
role_bits_against_qubit_axiom_bits: 3 / 1
nn_role_rule_record_radius: 3
readability_complete_and_partial_orbits: 6 of 800 / 61 of 2226
readability_fraction: 2.74 per cent
separation_counts_of_the_parent_criterion: not reproduced here and excluded
no_physical_law_is_selected: true
```

## Proof boundary

The theorem is the finite classification above and nothing wider.

- **Five named tori, periodic, no open blocks.** `4x2x2`, `4x4x4`, `8x4x4`, `5x4x4`, `7x4x4`. The `4x2x2` torus is
  degenerate -- `+d` and `-d` are the same site in the size-`2` directions -- and carries weight only as the box on
  which the record-level enumeration is complete. The commensurate comparisons are set equalities on PR #7834's own
  two boxes.
- **The record-level rows.** Complete and solver-free on `4x2x2`, over all `2^16` binary configurations. On `4x4x4`
  they are decided by CaDiCaL where pysat is present, and are not run otherwise; the runner prints which path ran.
- **Minimality, stated in its class.** `12` is minimal among rotation-closed offset sets that contain the nearest
  neighbours and lie inside the `5x5x5` window. It is not a claim about arbitrary local rules, nor about offset sets
  reaching outside that window -- `NN` with `{+-3 e_d}` is the exhibited failure just outside it.
- **The parent's separation criterion is excluded.** A reconstruction of PR #7834's unseparated-pair counts at the
  star and `3x3x3` windows does not reproduce its `29` and `2`; those rows are **not reproduced here and are
  excluded** from every statement above, and nothing here rests on them. The `5x5x5` minimality is established
  instead by the record-level enumeration and SAT of T4, which use no separation criterion, and T4's radius-`2`
  role recovery is a directly computed functional determination.
- **Supports, not distributions.** Every statement is about supports, in the sense reading note (3) fixes. The
  distribution-valued lift is untouched. No sampling, no seed and no random number generator is used anywhere; no
  premise is edited, no axiom is added, and **no physical law is selected**.

## Honest-auditor read

The load-bearing objects are, in order: the set equality of T3 -- that `NN` with `{+-2 e_d}` admits the sector set itself, not merely
`48` things; the `0` unrealised refinements of T2, the single line that makes the nearest-neighbour table blind to the corner pin
bit; and the `5x5x5` `UNSAT` of T4. Attack them in that order. The first two are complete enumerations with small witnesses and the
easiest to re-run. The third has the strongest support here, decided twice by different methods on different boxes -- a complete
solver-free enumeration on `4x2x2` and CaDiCaL on `4x4x4` -- and agreeing with a parent result reached by a third method. The weakest
rows are T3's minimality, which holds only in the class named above, and the `4x4x4` SAT rows, which need the solver. The claim most
likely to be over-read is T5's: `2.74 %` says what one arrangement exercises, not what any record configuration could.

## Review record

This note bounds the reach of an earlier readability result on one designed law and proposes no law of its own. Hard landing
conditions are a fresh runner and cache pair, a current citation-manifest entry, and passing pipeline, strict-lint and
changed-evidence gates; independent audit remains a separate lane.
