---
claim_id: the_superlattice_role_pattern_is_a_next_nearest_neighbour_support_rule_over_roles_and_roles_are_not_record_values_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Conditional finite classification on the five named tori, using a supplied five-symbol role alphabet and a separately supplied binary recorded alphabet. The NN local pair table is the rotation closure of the template pairs; its global admissible set is larger than the sector family. NN plus the second axial orbit pins the sectors on the three tested commensurate tori as a set equality and has no configurations on the two tested incommensurate tori. The binary window censuses, template-domain decoder and NN profile-orbit census have the domains stated below. No physical law, formation process, quantum alphabet reduction, general record-rule translation or Hamiltonian is selected."
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

**Audit:** unset; formal audit is deferred by the current owner directive.

**Status:** conditional source under independent review; no audit status is assigned.

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
claim_type_reason: "Integer finite censuses and set comparisons, complete 4x2x2 binary enumeration and required CaDiCaL decisions on 4x4x4. Decoder composition supplies conditional upper radius bounds, not a global equivalence or minimality theorem."
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

The **superlattice role pattern** is a declared template family on `Z^3`. A site's coordinate parity names a corner, coarse edge, face or cube centre. Along a chosen axis the corner value alternates with period `(4,2,2)`; faces are `0`, cube centres `1`, and coarse edge bits are free. There are 16 translates for each of three orientations, giving 48 templates when the torus supports them.
The pattern, five-symbol alphabet and binary recorded alphabet are supplied mathematical choices. Here "readout" means a complete static catalog of allowed configurations or its declared partial restrictions. It supplies neither occurrence probabilities nor reachable histories nor a way to infer absence from finite observations. Record permanence does not supply those missing rules.
Historical #7834 and #7934 motivated the question. Their broader fermion, separation and arbitrary-readout claims are not premises of this note; the finite definitions and proofs used here are redeclared. The question is which windows constrain this declared template family.

## Supplied surface (quoted)

Lattice, Qubit and Admissibility, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`), with reading note (3) fixing
the sense of "admissible":

> "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."

> "Each site has a domain of local possibilities. The full one-site possibility domain has algebraic presentation `M_2(C)`."

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus, exactly the possibilities of nonzero probability."

The binary recorded alphabet `{0,1}` is separately supplied. `M_2(C)` is not a two-element domain: for example, the five distinct density matrices `diag(j/4,1-j/4)`, `j=0,...,4`, belong to it. Distinct matrices are not thereby perfectly distinguishable classical messages.

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

The first two lines express a local-pair covariance identity: closing one orientation's realised pairs gives exactly the union over the three orientations. This does not identify the global admissible set with the 48 sectors; T2 gives 2,048 NN-admissible configurations on `4x4x4`. The `17` rows are one corner row, `12` edge rows (four corner-pin pairs on each of three axes), three face
rows and one cube-centre row.

Two things this encoding does, both load-bearing below. It **refines** the record value -- separating a corner showing `0`
from a face showing `0`, which no record does -- and it **forgets** the free edge bits entirely: every edge site is `E`
whatever its qubit says, and any separate quantum encoding on the free edge bits is outside this role-table result.

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
closes at `NN` already, so the frustration PR #7834 reports at `5x5x5` is a property of the `(2,2,2)` skeleton and already appears at the nearest-neighbour range in this model.

## T3 -- the minimal pinning neighbourhood is next-nearest-neighbour (exact)

Among rotation orbits of offsets inside the `5x5x5` window the only ones of size `6` are `{+-e_d}` and `{+-2 e_d}`, so the
only extension of `NN` by a nonempty orbit with at most `12` total offsets inside that window is `NN` together with
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
CaDiCaL over `64` value variables and `3,072` template indicators, and is required for a complete run. Only the `5x5x5` window
pins among this ladder on these two tori, independently of the historical parent's separation criterion. The `12`-offset role rule of T3 does **not**
transfer: the same offsets over binary values admit configurations outside every cylinder. What buys it its economy is the
alphabet, not the geometry.

Two further record-level facts complete the picture.

```text
binary 7-site star patterns realised over all 48 sectors and all free edge bits = 128 of 128
the centre role is a function of the window's record values:  star no   NN with {+-2 e} no
                                                              L1<=2 no   3x3x3 no   5x5x5 yes
```

The first establishes locally, without accepting PR #7834's wider theorem: the minimal covariant nearest-neighbour table over records is the
all-permissive one. The second says a role is uniquely recovered on the union of template-compatible `5x5x5` windows, with the failures
explicit -- at the star and at `NN` with `{+-2 e}` a corner is mistakable for an edge site, at `L1<=2` an edge site for a
cube centre, at `3x3x3` a corner for a face.

**The cost of the alphabet.** Encoding five role labels as fixed-length classical binary strings takes three bits; the supplied record alphabet takes one. This is no reduction of the Qubit domain.
The decoder is a partial function defined only where a window matches a template. Composing it with a NN role rule inspects records within radius at most `1+2=3`; composing it with the twelve-offset rule inspects radius at most `2+2=4`, provided every decoder window used is in its domain. Outside that domain no extension is chosen here. Neither upper bound proves global equivalence, an exact radius, or minimality. Both exceed the direct radius-2 marker window. The latter is a different directly defined support rule.

## T5 -- readability, and what the designed law is made of (exact)

Count the NN profiles in the declared template family and its partial restrictions, with absent slots represented by `open`:

```text
NN rotation-orbit profiles the complete pattern exercises      =  6 of 800
(role, profile) pairs realisable from sub-configurations         = 794
partial profiles realised                                        = 655 of 6^6 = 46,656
partial NN rotation-orbit profiles realised                    = 61 of 2,226 = 2.74 %
```

These are **profile-orbit** counts for the six-offset NN table, not central-role entry counts and not the twelve-offset pinning table's census. The corresponding complete and partial central-role entries are `7/4000` and `84/11130` (recomputed in #7977). The displayed 61/2226 is approximately `2.74 %`.
The template catalog certifies present entries where it supplies witnesses. Its unexercised profiles alone do not decide whether an absent entry can be inferred from a larger static admissible-set catalog; that distinct question is studied in #7977. No quantum ground state, physically accessible preparation ensemble or absence-detection protocol is constructed here.

| part | declared object | scope of the calculation |
|---|---|---|
| **role support rule** | NN local table versus the twelve-offset sector-pinning table | The former supplies the `6/800` and `61/2,226` profile census; the latter supplies the finite sector set equality. Both are role tables. |
| **sector choice** | one of the 48 templates on the two larger commensurate tori | Choice is supplied, and no selection dynamics or ground-state degeneracy calculation is made. |
| `S_f`, `B_v`, `T_ij` | separately proposed quantum operators | Their coefficients, physical encoding and dynamics are not supplied by this support catalog. |

Treating a static support-table identification as determination of Hamiltonian terms is a category error. The formal expression `T_ij=(i/2) A_ij(B_i-B_j)` concerns a separately supplied operator; no such operator is selected by the census.

## Corollary

1. On the named finite tori the twelve-offset role rule pins the specified sectors; NN alone allows the reported extra pin fields.
2. The supplied five-symbol roles and binary record values are distinct alphabets. The template-domain decoder gives conditional radius bounds `3/4` for NN/twelve-offset compositions, not a global translation theorem.
3. The NN profile census `61/2,226` is different from an entry census, a twelve-offset census and any physical readability claim.
4. Sector choice, quantum operator coefficients, preparation, actual occurrence and permanent-record formation remain separate supplied or open content. No physical law is selected.

## Reading, not theorem

The same templates produce different local constraints when read as role labels or binary values. A compact role rule does not by itself give an equally compact binary rule, and neither static catalog identifies a physical Hamiltonian or formation process.

## Interfaces

- **A record-native role encoding.** Whether the four role classes can be carried at one bit per site, by a
  construction that does not smuggle in a second bit, is untouched here.
- **The sector choice as a past hypothesis.** Whether a globally fixed choice among the templates is a
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
role_bits_against_supplied_binary_alphabet_bits: 3 / 1; full M_2(C) domain unrestricted
conditional_decoder_composition_radius_upper_bounds_nn_and_twelve: 3 / 4
nn_profile_catalog_complete_and_partial_orbits: 6 of 800 / 61 of 2226
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
  they require CaDiCaL; missing or indeterminate solver results fail the complete run.
- **Minimality, stated in its class.** `12` is minimal among rotation-closed offset sets that contain the nearest
  neighbours and lie inside the `5x5x5` window. It is not a claim about arbitrary local rules, nor about offset sets
  reaching outside that window -- `NN` with `{+-3 e_d}` is the exhibited failure just outside it.
- **The parent's separation criterion is excluded.** A reconstruction of PR #7834's unseparated-pair counts at the
  star and `3x3x3` windows does not reproduce its `29` and `2`; those rows are **not reproduced here and are
  excluded** from every statement above, and nothing here rests on them. The tested ladder is decided
  instead by T4 enumeration and SAT. This is not a minimum among arbitrary windows. The radius-`2`
  role recovery is a function only on template-compatible windows.
- **Supports, not distributions.** Every statement is about supports, in the sense reading note (3) fixes. The
  distribution-valued lift is untouched. No sampling, no seed and no random number generator is used anywhere; no
  premise is edited, no axiom is added, and **no physical law is selected**.

## Honest-auditor read

The load-bearing objects are, in order: the set equality of T3 -- that `NN` with `{+-2 e_d}` admits the sector set itself, not merely
`48` things; the `0` unrealised refinements of T2, the single line that makes the nearest-neighbour table blind to the corner pin
bit; and the `5x5x5` `UNSAT` of T4. Attack them in that order. The first two are complete enumerations with small witnesses and the
easiest to re-run. The third has the strongest support here, decided twice by different methods on different boxes -- a complete
solver-free enumeration on `4x2x2` and CaDiCaL on `4x4x4` -- without using any historical parent claim as acceptance. The weakest
rows are T3's minimality, which holds only in the class named above, and the `4x4x4` SAT rows, which need the solver. The claim most
likely to be over-read is T5's: `2.74 %` says what one arrangement exercises, not what any record configuration could.

## Review record

The 2026-09-08 correction preserves the original note and cache byte-for-byte in
`.claude/science/physics-loops/role-law-correction-20260908/originals/7939/`. The dated correction record there separates historical claims from the present scope.
The original once-only review run is preserved externally. Final evidence must bind these corrected source/input bytes and include all required solver rows.
Source review and the coordinator's combined mechanical validation precede any authorized landing. Formal audit remains deferred; no physical law is selected.
