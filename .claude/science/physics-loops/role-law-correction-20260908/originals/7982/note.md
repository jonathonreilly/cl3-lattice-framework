---
claim_id: a_readable_matter_law_exists_on_the_5x5x5_window_the_designed_laws_record_table_completed_by_a_covariant_parity_rule_has_every_menu_nonempty_is_read_from_partial_blocks_and_keeps_the_fermion_bounded_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "Exact and finite. The object is the designed matter law of PR #7834 written over binary records: the minimal covariant support table T_min on a rotation-closed window, whose menu at each profile is the set of values the 48 template cylinders realise there and is empty at every never-realised profile. Six covariant completions of the never-realised profiles are treated -- constant 0, constant 1, the parity of the window's recorded values, its complement, a corrected parity that gives the all-0 profile 1 and the all-1 profile 0, and the permissive one -- on the windows NN (6 offsets), NN with the second axial orbit (12), L1<=2 (24), 3x3x3 (26), the 39-offset closing window of PR #7977 (38 offsets and the centre), 5x5x5 (124) and 7x7x7 (342) as a control. The tori are 4x2x2, 4x4x2 and 4x4x4 for the tabulated windows and 4x4x4 and 8x4x4 for the wide ones; the tables, the star readout and the censuses are on Z^3. On the 5x5x5 window the corrected parity completion has every menu nonempty, every complete entry read by one partially recorded 5x5x5 block, the 48 cylinders as its complete admissible set on 4x4x4, and the cylinders with 16 isolated weight-24 configurations on 8x4x4; the parity completion adds the all-0 configuration on each. Every extra is isolated under single flips, so the hop Hamiltonian of PR #7889 restricted to the admissible set is the direct sum of the 48 untouched cylinder blocks and a zero operator. No nearest-neighbour or radius-1 table containing the cylinders is both readable and pinning. The completeness of the two 8x4x4 extra lists is quoted from the source computation's output lines and re-verified member by member, not re-enumerated. Capped enumerations are reported as bounds and never as counts. No physical law is selected."
upstream_dependencies:
  - minimal_axioms
  - extensional_nearest_neighbor_rule_deep_probe_2026-07-13
  - finite_bksf_sign_and_superlattice_marker_census_bounded_theorem_note_2026-09-02
runner: scripts/readable_matter_law_on_5x5x5_window_parity_completion_check_2026_09_04.py
registry_id: readable_matter_law_on_5x5x5_window_parity_completion_2026_09_04
---

# A readable matter law exists on the `5x5x5` window: the designed law's record table completed by a covariant parity rule has every menu nonempty, is read entry by entry from partially recorded `5x5x5` blocks, admits exactly the 48 sectors on `4x4x4` and 16 further isolated configurations on `8x4x4`, and leaves the emergent fermion's hop Hamiltonian block-diagonal; no nearest-neighbour or radius-1 table containing the sectors does so

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/readable_matter_law_on_5x5x5_window_parity_completion_check_2026_09_04.py`](../scripts/readable_matter_law_on_5x5x5_window_parity_completion_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/readable_matter_law_on_5x5x5_window_parity_completion_check_2026_09_04.txt`](../logs/runner-cache/readable_matter_law_on_5x5x5_window_parity_completion_check_2026_09_04.txt)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
[`EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md`](EXTENSIONAL_NEAREST_NEIGHBOR_RULE_DEEP_PROBE_2026-07-13.md),
[`FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-02.md`](FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-02.md)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Every count is an exact enumeration over a named finite torus or, for the tables, the star readout and the censuses, over Z^3 with the orbit totals supplied by Burnside. The complete admissible sets on the smallest torus are computed without a solver for all seven rules and agree with CaDiCaL as sets on the four rules re-run there. The star lemma is verified completely on the tabulated windows by an exact recount of the completions of every overlap pattern, and on the wide windows by a counting certificate with a margin of 16,625,822 at the worst offset. The two 8x4x4 extra lists are quoted for completeness and re-verified member by member. Capped enumerations are reported as bounds. No physical law is selected."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Decide the minimum of the extras over the space of completions rather than the six declared rules, and the extra count on a torus all of whose sides are at least 5."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Setting

PR #7834 puts a fermion on `Z^3` at one qubit per site by declaring a **superlattice role pattern**: a site's role is its coordinate parity, and a repeating arrangement of pinned values with period
`(4, 2, 2)` along a chosen axis pins a corner to `(s[ax] / 2) mod 2`, a face to `0`, a cube centre to `1`, and leaves every coarse edge site free as a live qubit -- `48` sectors, each a cylinder of
record configurations. PR #7977 read that pattern as a law over the five-symbol role alphabet and found it blind: the role table has an empty menu at every profile carrying one of the `17` ordered
role adjacencies of `25` the pattern never realises, and the partial readout cannot see those entries at all. Over binary records, its control showed, every small partial pattern inside the `5x5x5`
window is exercised instead.

**The question here is the next one.** Is there a matter law of the readable kind -- PR #7934's class, binary records, every menu nonempty -- that still carries the emergent fermion: admits every
cylinder, has the cylinders as its whole complete admissible set up to a declared finite set of separated configurations, and leaves the hop Hamiltonian of PR #7889 supported inside them? The answer
is yes on the `5x5x5` window and no on any nearest-neighbour or radius-1 window tried. Records register; the lattice is physical; the pattern is an arrangement of pinned values.

## Supplied surface (quoted)

Admissibility and Record, current landed wording (`docs/MINIMAL_AXIOMS_2026-06-29.md`), with reading note (3) fixing "admissible":

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."

> "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on finite menus,
> exactly the possibilities of nonzero probability."

> "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Supplied from the campaign: the pattern and its `48` templates (PR #7834); the record rule `R_W` on a rotation-closed window and the readable class of PR #7934 -- covariant tables over a binary record
alphabet with no empty menu -- with two stipulations, no label-equivariance (the designed law is not flip-symmetric: faces `0`, centres `1`) and the ternary profiles not free law content; the hop
Hamiltonian `T_e = (i/2) A_ij (B_i - B_j)`, the BKSF encoding, the KS sign field and the twist convention (PR #7889, PR #7885 and the landed BKSF and superlattice census); the six completion rules --
constant `0`, constant `1`, the parity of the window's recorded values, its complement, a corrected parity that gives the all-0 profile `1` and the all-1 profile `0`, and the permissive one -- the
tori; the caps.

**Stipulation R, the marginal reading of an unrecorded neighbour.** For a partial profile the menu is the union, over the completions of the open offsets, of the complete table's menus, and a partial
configuration is admissible when every recorded site's value lies in that union. This is the partial-configuration readout of PR #7928 and PR #7934 with the ternary table derived from the complete
one, and on the exercised part it reproduces PR #7977's projection reading exactly: `496` of `496` one-offset, `61,008` of `61,008` two-offset and `4,814,888` of `4,961,984` three-offset patterns.

**The designed law over records** is `T_min^W`: the menu at a profile is the set of values the cylinders realise there, empty at every never-realised profile. Every entry of `T_min` is exercised by a
cylinder, so the readable laws carrying the cylinders are exactly the completions of `T_min^W`, one or two values at every never-realised profile orbit.

## T1 -- the censuses, and the entries a completion must add

The parent censuses reproduce with fresh code.

```text
torus                4x2x2        4x4x2         4x4x4              8x4x4
cylinders               16           32            48                 48
free edge bits           6           12            24                 48
record configurations 1,024      131,072   805,306,368         48 x 2^48
role table T0: 18 (role, profile) pairs, 17 profiles of 5^6, 6 rotation orbits; 8 of 25 ordered
role adjacencies realised, 17 never; the nearest-neighbour role rule admits 32 / 128 / 2,048 and
the 12-offset rule admits 16 / 32 / 48, equal to the sector sets as sets
window                    NN      NN+AX2       L1<=2         3x3x3           5x5x5
offsets                    6          12          24            26             124
exercised entries        128       1,638     391,233       101,626    2^57.05 of 2^125
profiles with both        64         640     193,600         3,089               0
profile orbits            10         240     703,360     2,802,752               -
NEVER-REALISED orbits      0         157     694,711     2,798,417               -
4x2x2, outside every cylinder under T_min: 64,512 / 13,981 / 186 / 154 / 0
```

The never-realised orbit counts are the entries a readable completion must add: `0` at nearest neighbour, `157` at twelve offsets, `694,711` at `L1<=2`, `2,798,417` at `3x3x3`. On `5x5x5` the `48`
template cylinders are pairwise inconsistent, `0` of `1,128` pairs, with `36`, `44`, `51` or `54` free sites per template, so the exercised entries number exactly `148,935,859,368,886,272`; on the
39-offset window `159` of `1,128` pairs are consistent and the free sites number `0`, `7` or `24`. The odd-corner census of one sector on `4x4x4` is intact: `131,072 / 3,670,016 / 9,175,040 /
3,670,016 / 131,072` over the `2^24` edge assignments. **At nearest neighbour the only table containing the cylinders is the all-permissive one:** all `128` of `128` star entries are exercised and all
`64` profiles carry both values, so the minimal law is already permissive, admits every configuration, and excludes nothing.

## T2 -- the tabulated windows: readable, and not pinning

On `4x2x2` the complete admissible set of each of the seven rules is enumerated without a solver, and CaDiCaL agrees with it as a set for the minimal, constant-0, parity and corrected rules on all
three windows.

```text
4x2x2, configurations outside every cylinder          4x4x4, admissible pinned flips of 1,920
window     T_min      c0      c1     par    apar    corr    permissive     T_min     par     corr
NN+AX2    13,981  13,981  64,512  40,349  23,056  40,349        64,512     1,920       -       -
L1<=2        186     833     699     725     607     636        64,512         0     384      384
3x3x3        154     175     883     187     887     210        20,714         0     768      768
```

The minimal law already admits thousands of configurations outside every cylinder at each of these windows, and where it does not, the parity completions open single flips out of the cylinders.
**Readability, on the other hand, is cheap.** The star flexibility -- for every offset, neighbour value and recorded overlap pattern, does some completion of the open offsets keep that value available
-- is decided completely: `144` triples at twelve offsets, `74,496` at `L1<=2` and `1,624,064` at `3x3x3`, of which `0` have no completion under the parity, anti-parity, corrected and permissive rules
at every window; the minimal law fails `55,848` and `1,587,236` of them.

```text
Z^3 star readout, complete entries
window   law                  in T*        read        not in T*       read        blind
NN+AX2   T_min                1,638       1,638            6,554      6,554            0
L1<=2    T_min              391,233     391,233       33,163,199      4,132   33,159,067
L1<=2    c0              16,970,816     414,296       16,583,616     45,170   33,094,966
L1<=2    par/apar/corr   16,970,816         all       16,583,616        all            0
3x3x3    T_min              101,626     101,626      134,116,102      7,486  134,108,616
3x3x3    c0              67,111,953     127,281       67,105,775  1,024,996  133,065,451
3x3x3    c1              67,111,953     109,097       67,105,775    124,785  133,983,846
3x3x3    par/apar/corr   67,111,953         all       67,105,775        all            0
```

Three readings. **The designed law over records is blind on any window wide enough to matter** -- `134,108,616` of `134,217,728` entries on `3x3x3`, `99.92` per cent -- and what causes it is the empty
menus, not the role alphabet. **Nonempty menus alone do not buy readability:** the constant completions are in the readable class and are almost as blind. **A flexible completion reads everything**,
in or out of the law.

## T3 -- the pinning windows: `5x5x5` is where the completion costs nothing

**Pinned-flip lemma.** If no template agrees with a template `tau` on `tau`'s non-centre pins inside `W` while pinning the centre to the other value, then a cylinder configuration with one pinned site
flipped is inadmissible at that site under *every* completion, because its profile is realised and a completion never touches a realised menu. The count of such template pairs is `0` on the 39-offset
window, on `5x5x5` and on `7x7x7`, and on the tori no pinned flip is admissible under any rule, `0` of `1,920` and `0` of `3,840`. Each cylinder is therefore a component of the admissible set under
single flips, whatever the completion.

```text
configurations outside every cylinder
torus / window            T_min       c0        c1      par     apar     corr
4x4x4, W39 (39 offsets)       0    3,457   >= 5,000   3,457  >= 5,000  >= 5,000
4x4x4, 5x5x5                  0        1          1        1        1        0
8x4x4, 5x5x5                  0  >= 5,000         1       17  >= 5,000       16
```

On `4x4x4` the wrapped `5x5x5` window reaches every site and the parity rule reduces to the linear system `c_s = sum of the odd-multiplicity neighbours`, whose matrix has full rank `64` over `F2`
(rank `128` of `128` on `8x4x4`): the all-0 configuration is the only extra of the parity rule, all-1 the only one of the anti-parity rule, and the corrected rule, which assigns `1` to the all-0
profile and `0` to the all-1 profile, has none. The 39-offset window, which does pin the minimal law on both tori, admits `3,457` extras under the parity and constant-0 rules on `4x4x4` and thousands
more on `8x4x4`, because it does not separate the templates locally: `159` of its `1,128` template pairs are consistent on the window.

**The completion is invisible to complete records on a torus.** On `4x4x4` the parity and constant-0 rules have the same admissible set, the anti-parity and constant-1 rules likewise, and the
corrected rule the same set as the minimal law. A torus every site of which carries a record cannot tell these laws apart; a `5x5x5` block of records with open surroundings reads every entry of each.
The Z^3 census of exercised complete entries on `5x5x5`: the sea of one sector exercises `48` in `9` rotation orbits, adding every single hop within reach gives `2,298` in `114` orbits, adding every
double complement `54,642` in `2,421` orbits, and the whole cylinder set exercises `T_min` itself.

## T4 -- the physics survives

The record-level Hamiltonian is PR #7889's, taken as supplied: qubits on the free edge sites of a sector, and a hop on edge site `e` is the map `y -> y XOR e` on record patterns. Restricting it to the
admissible set keeps the matrix elements between admissible configurations.

```text
4x4x4, 5x5x5, par and corr: 10,296 hop transitions from the declared families, 0 leaving
8x4x4, 5x5x5, par and corr: 18,096 hop transitions from the declared families, 0 leaving
4x4x4, corr: nothing outside the cylinders; two-copy SAT for an admissible pair at Hamming
             distance 1 with one member outside every cylinder: UNSAT
8x4x4, corr: 16 extras, each of weight 24, each with exactly 32 template-consistent sites of 128,
             each 16 pinned-site flips from the nearest cylinder, none a corner pin-field defect;
             0 admissible neighbours in 2,048 direct solves (2,176 under par, which adds all-0)
coarse graph  corners  bonds   E_sea          twist      gap        best even filling
4x4x4               8     24   -8 sqrt 3      (0,0,0)    6.928203   N = 4
8x4x4              16     48   -8 sqrt 10     (1,0,0)    6.324555   N = 8
flux classes on 4x4x4: 131,072 bond-sign classes, 146 distinct half-filled energies, the minimum
             -13.856406 attained by exactly one class, the KS / pi-flux class
8x4x4 odd-corner census: parity-map rank 15 = corners - 1, fibre 2^33, C(16, N) 2^33 for even N
```

Every extra is isolated under single flips and no cylinder configuration has an admissible pinned flip, so `H` restricted to the admissible set is the direct sum of the `48` untouched cylinder blocks
and a zero operator on the extras. `H` is off-diagonal in the record basis, so an isolated configuration is an exact eigenvector of eigenvalue `0`: the extras sit `13.856406` and `25.298221` above the
sea on the two tori, degenerate with mid-spectrum states of the blocks and connected to nothing.

## The star lemma

Let `T` be a covariant support table on `W` and `T^loc` its marginal extension. For a complete entry `(v, P)` let its **star** be the partial configuration with the centre recorded `v`, the offsets of
`W` recorded as `P`, and every other site open.

1. `(v, P)` is exercised by the partial readout on `Z^3` exactly when its star is admissible, that is when `v` lies in `T(P)` and every neighbour's recorded value lies in `T^loc` of its ternary
   profile. Any partial configuration realising `(v, P)` at a site refines the star, and `T^loc` is antitone under refinement, so the star is the easiest witness.
2. Call `T` **flexible** when every neighbour of every star is in that sense available. Then `T' = T` for every support table `T'` on `W` with the same partial readout: for `v` in `T(P)` the star lies
   in the readout of `T`, hence in that of `T'`, so `T` is contained in `T'`; then `T'^loc` contains `T^loc`, the neighbours stay available under `T'`, and for `v` outside `T(P)` the star is absent
   from the shared readout only because `v` is outside `T'(P)`. **The fibre of a flexible law under the partial readout is a singleton** -- in the class of all covariant support tables on the window,
   not only the nonempty-menu ones -- and every complete entry, present or absent, is read by one `5x5x5` block of records with everything else open.

Flexibility is verified completely on the tabulated windows (`0` of `144`, `0` of `74,496`, `0` of `1,624,064` triples without a completion for the parity, anti-parity and corrected rules) and
certified on the wide windows by counting: a neighbour at offset `d` has `n_d` open offsets and the template-consistent completions number at most `sum_tau 2^{e_tau}`, so never-realised non-uniform
completions of either parity number at least `2^{n_d - 1} - sum_tau 2^{e_tau} - 2`, which is `16,625,822` at the worst offset of `5x5x5` and `255,065,528` on the 39-offset window.

## Corollary

**The answer is yes, conditionally, on the `5x5x5` window -- radius 2 over records -- and on no nearest-neighbour or radius-1 window tried.** Take `T_min` on `5x5x5` and give every never-realised
profile the value the corrected parity rule names. Every menu is nonempty; every complete entry is read by one partially recorded `5x5x5` block; the complete admissible set is exactly the `48`
cylinders on `4x4x4` and the cylinders with `16` isolated configurations on `8x4x4`; the hop Hamiltonian is block-diagonal with the sea still the ground state of each block. The plain parity rule does
the same with one further configuration on each torus.

**The price, itemised.**

1. **The window.** Radius 2 over records, `124` offsets, against "one fixed nearest-neighbor admissibility rule". PR #7939 priced the role rule at radius 3 over records; this law is radius 2 and needs
   no role alphabet at all.
2. **The completion is supplied.** The axioms and the cylinders say nothing about never-realised profiles, and complete records on a torus cannot read the choice: the parity and constant-0 completions
   have the same admissible set on `4x4x4`. Only partially recorded regions distinguish them, which is what the Record axiom permits -- a site with no record is not read, and the region around a
   recorded block may be unrecorded. The parity rule is one covariant choice among many, preferred here because it is flexible and has the fewest extras of the six.
3. **The extras.** None on `4x4x4` under the corrected rule, `16` of weight `24` on `8x4x4`, isolated and at energy `0`. Their number on larger commensurate tori, `8x8x4` and `8x8x8`, is not computed.
4. **Stipulation R**, the marginal reading of an unrecorded neighbour. Under the projection reading the completion entries are exercised only by the extras and readability becomes a different,
   undecided question.

**Disagreements with the expectation, stated plainly.**

- The expected trade-off "readability forces the wider window" is not what the computation shows: readability by partially recorded stars is available at twelve offsets and even for the minimal law.
  **What forces the wider window is pinning** -- having the cylinders as the whole complete admissible set -- not readability.
- PR #7977's 39-offset closing window is the wrong window for a readable law. It pins the minimal law on both tori, but every completion of it admits thousands of configurations outside the cylinders,
  because `159` of its template pairs agree on the window. The `5x5x5` window, which separates all `48`, is where the completion costs `0` on `4x4x4`.
- The blindness PR #7977 measured is not the role alphabet's alone: the designed law over records is `99.92` per cent blind on `3x3x3` under the partial readout, and what removes the blindness is the
  completion, not the alphabet.
- The completion is invisible to complete records on a torus, so "records determine the law" holds for it only through partially recorded regions.
- The extras depend on the torus: none on `4x4x4`, `16` on `8x4x4` for the corrected rule. A window-independent statement needs a torus all of whose sides are at least `5`, which is outside this run.

## Reading, not theorem

A law with empty menus cannot be read where it is silent, and the designed law over records is silent almost everywhere: nearly every arrangement of `26` neighbouring records is one the pattern never
builds, and about such an arrangement the law says nothing that any record can confirm or deny. Completing those silences with a coin the neighbours themselves determine -- the parity of what is recorded
around the site -- costs nothing that complete records can see and buys everything the partial ones need: each silence now has an answer, and each answer shows up in some block of records that is
surrounded by open sites. The surprise is which half of the job needs the wide window. Reading the law is easy and was available six offsets out; what needs `124` offsets is telling the pattern apart
from everything else, and once the window is wide enough to do that, the filling costs one configuration on the smaller torus and sixteen on the larger, all of them frozen, all of them at zero energy,
none of them reachable by a hop.

## Interfaces

- **PR #7977**, the readout-blindness note, is the parent this note answers: its role-level blindness, its record-level control and its 39-offset closing window are all reproduced here, and its
  blindness is shown to be removable at the record level by the completion. **PR #7939**, the role-pattern note, supplies the role rule priced at radius 3 and the 12-offset table whose admissible set
  is the sectors.
- **PR #7928** and **PR #7934**, the readability notes, supply the partial-configuration readout and the class in which every menu is nonempty; this note runs their readout against a completed minimal
  table and gives the exact condition, flexibility, under which the fibre is a singleton.
- **PR #7889** and **PR #7891**, the shifting-record notes, supply the hop and the single- and double-complement families, shown here to stay inside the cylinders; **PR #7885**, the determinantal
  statistics note, supplies the reading of a full set of records at the coarse modes, used here to name the excitation families. The landed BKSF and superlattice census supplies the encoding and the
  sign field on the coarse graph.

## Executable claim block

```text
registry_id: readable_matter_law_on_5x5x5_window_parity_completion_2026_09_04
censuses_pairs_profiles_orbits_and_adjacencies: 18 / 17 of 15,625 / 6 and 8 of 25
role_admissible_sets_nn_and_twelve_offset: 32 / 128 / 2,048 and 16 / 32 / 48 = the sectors
record_tables_exercised_entries: 128 / 1,638 / 391,233 / 101,626 and 2^57.05 of 2^125
free_sites_per_template_on_5x5x5_and_pairs_consistent: 36 / 44 / 51 / 54 and 0 of 1,128
never_realised_profile_orbits: 0 / 157 / 694,711 / 2,798,417
ladder_4x2x2_outside_every_cylinder: 64,512 / 13,981 / 186 / 154
star_flexibility_triples_and_failures_par_apar_corr: 144 / 74,496 / 1,624,064 and 0
minimal_law_star_failures_and_blind_entries_on_3x3x3: 1,587,236 and 134,108,616 of 134,217,728
completed_table_entries_read_on_3x3x3: 67,111,953 in and 67,105,775 out, blind 0
pinned_flip_lemma_pairs_w39_5x5x5_7x7x7_and_counting_margin: 0 / 0 / 0 and 16,625,822
extras_4x4x4_5x5x5_min_c0_c1_par_apar_corr: 0 / 1 / 1 / 1 / 1 / 0
extras_8x4x4_5x5x5_min_c1_par_corr: 0 / 1 / 17 / 16 (par and corr quoted, s3A.030 and s3B.005)
extras_4x4x4_w39_par_and_c0: 3,457 each, weights 0, 4, 8; 159 consistent template pairs
f2_rank_of_the_wrapped_parity_system: 64 of 64 and 128 of 128
z3_entry_census_and_partial_patterns: 48 / 2,298 / 54,642 and 496 / 61,008 / 4,814,888
hop_transitions_and_departures: 10,296 and 18,096, 0 leaving
extras_isolated_direct_solves: 0 of 2,048 and 0 of 2,176; two-copy SAT on 4x4x4 UNSAT
sea_energies_and_gaps: -8 sqrt 3 with gap 6.928203 and -8 sqrt 10 with gap 6.324555
flux_class_minimum_and_multiplicity: -13.856406 over 131,072 classes, attained once, 146 energies
odd_corner_census_4x4x4_and_8x4x4_rank: 131,072 / 3,670,016 / 9,175,040 and rank 15, fibre 2^33
no_physical_law_is_selected: true
runner_result_required: zero failed checks
```

## Proof boundary

The theorem is the finite classification above and nothing wider.

- **Named tori, periodic, no open blocks.** `4x2x2`, `4x4x2` and `4x4x4` for the tabulated windows; `4x4x4` and `8x4x4` for the 39-offset, `5x5x5` and `7x7x7` windows; `Z^3` for the tables, the star
  readout and the censuses.
- **Capped enumerations are reported as bounds and never as counts.** Where a row reads `>= 5,000` or `>= 20,000` the enumeration stopped at the cap, and no such row is used as a count anywhere above.
  Six completion rules are treated, not the space of completions: the minimum of the extras over all completions is not computed, its lower bound on a pinning window being the cylinder count, attained
  on `4x4x4` by the corrected rule.
- **What is quoted, not recomputed.** The completeness of the two `8x4x4` extra lists on the `5x5x5` window -- `17` under the parity rule and `16` under the corrected rule -- is quoted from the source
  computation's output lines s3A.030 and s3B.005, each of which cost about a thousand seconds; the runner re-verifies all `16` configurations member by member as admissible, outside every cylinder, of
  weight `24`, with `32` template-consistent sites, `16` pinned-site flips from the nearest cylinder, and isolated. The capped `8x4x4` rows for the constant-0 and anti-parity rules are likewise quoted
  as bounds. The corrected rule's list was closed once more away from the runner, by a single call with all `16` blocked that returned unsatisfiable
  after about `2,000` seconds, so there is no seventeenth configuration; that call is outside the runner's budget and the runner does not repeat it.
- **Undecided rows, named.** The single-flip adjacency question for the 39-offset window's extras on `8x4x4` is not decided; the `8x4x4` `7x7x7` corrected-rule row was not run; the extra count on a
  torus all of whose sides are at least `5` is not computed; and the readability claim under the projection reading rather than Stipulation R is not decided.
- **Supplied and stipulated.** The pattern and its templates, the record rule and the windows, the readable class with its two stipulations, Stipulation R, the six completion rules, the tori, the
  caps, and the whole of the physics -- the hop Hamiltonian, the BKSF encoding, the KS sign field and the twist convention. The flux-class scan is a free-fermion statement per bond-sign class; the
  identification of the classes with encoding sectors is the parents' supplied content, and no dynamics is derived here.
- **The axiom-level observation is a tension, not a derivation:** the law found is radius 2 where Admissibility says nearest-neighbour, and its never-realised menus are readable only through regions
  the Record axiom permits to be partly unrecorded. No axiom is edited, no physical law is selected, and nothing is derived from the axioms about which law holds. No sampling, no seed and no random
  number generator is used anywhere.

## Honest-auditor read

The load-bearing objects are, in order: the pinned-flip lemma, a two-line argument that makes every cylinder a component of the admissible set under every completion and carries the whole
block-diagonality claim; the `0 / 1 / 1 / 1 / 1 / 0` extras row on `4x4x4`, which is what makes the corrected rule's admissible set exactly the sectors and is a complete CaDiCaL enumeration with an
UNSAT proof at the end; and the star lemma, whose flexibility hypothesis is decided completely at `3x3x3` and by a counting certificate above it. Attack them in that order; the first two need only a
solver and the third only arithmetic. The weakest rows are the two `8x4x4` extra totals, quoted rather than re-enumerated, and the capped rows beside them. The claim most likely to be over-read is the
headline: the completion is a supplied choice that complete records cannot see, so "readable" here means readable through partially recorded regions under Stipulation R, and the `16` extras on `8x4x4`
say the sector structure is not yet torus-independent.

## Review record

This note answers a readability question about one designed law, prices the answer, and proposes no law of its own. Hard landing conditions are a fresh runner and cache pair, a current
citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane.
