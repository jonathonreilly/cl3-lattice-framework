---
claim_id: mirror_asymmetric_rule_registers_its_own_texture_movers_t_blind_2026_09_05
claim_type: bounded_theorem
claim_scope: "Complete integer enumerations over the ternary nearest-neighbour profile alphabet, plus one-particle and determinantal record numerics on declared finite geometries. SUPPLIED, none of it read out of any axiom: the covariant support-table census and its label-equivariant readable class (PR #7934), the wider readable class without label equivariance (PR #7982), the superlattice role pattern and its 48 sectors (PR #7939/#7982), the Kawamoto-Smit sign field and the half-filled sea (PR #7883), the star tick with the rotated kernel (PR #7986), the body-diagonal second mass M2 with its winding phase (PR #7949), and this note's own chiral support rules, chiral odds table, formation orders, regions and tolerances. (T1) The 729 ternary neighbour profiles fall into 57 proper orbits and 56 full orbits, so exactly one chiral orbit pair exists, Burnside-cross-checked; it needs four recorded neighbours and two open ends, no fully recorded profile is chiral (10 orbits, 0 chiral), the label-equivariant class of 3^24 = 282429536481 tables contains 0 mirror-asymmetric tables because all 24 digits are inversion-fixed, and the wider class of 3^57 tables is mirror-asymmetric in exactly two thirds, organised as 3^56 chiral pairs differing from their mirrors on that one profile pair alone. (T2) The 48 sectors, the nearest-neighbour and 12-offset role rules and the 5x5x5 record table with its parity completion are preserved by all 48 elements of O_h (the inversion relabelling the sectors with 24 fixed and 12 two-cycles), the mirror image of the Kawamoto-Smit field is a Z2 gauge copy at residual 0.0e+00 with the record law invariant to 9.2e-16, and the medium h_KS + m2 M2 is preserved by the 24 elements of T_h, the inversion included, and sent to -m2 by the other 24, so its gauge-invariant four-cycle products change by 0.800 under the proper rotations as well as the improper ones. (T3) Every parity-odd record correlator vanishes on the sea of the cube, the slab and the 4^3 torus (|chi_k| <= 3.5e-16, helix Ursell 7.0e-19); a single star-tick order is chiral, max |chi_4| = 0.088127 over all 40320 cube orders with 29376 nonzero, its mirror order carrying -chi_4 and the uniform average 3.1e-19; and TV(law of K, law of K*) = 0.0e+00 exactly. (T4) On the cube no corner can realise the chiral profile and every table gives one law; on the slab the chiral tables give partner-odds asymmetries from -1.32e-02 to +0.273 with chi_3(sea) to -0.439 against controls at 0.0e+00; under the star tick the rule acts only in mirror-closed order families that expose the four-record shape at formation (Delta = +4.33e-03 and +5.28e-03 at 8448 events) and not at all in families that do not; on torus regions Delta falls from +1.10e-02 to +6.62e-03 while the rule's own texture grows, and a fully recorded L^3 block is chiral-capable only on its 12(L-2) edge lines; and for the string of PR #7949 rebuilt on 12x12x24 the anti-string is conj(H) exactly, the core right-mover and the anti-string's core left-mover have identical record laws on every column under every table (TV = 0.0e+00), so Delta = 0 identically. (T5) An m2-sign wall binds a gapped two-dimensional band at |E| = m1 = 0.49497 with <M2> = 0, the same on wall, anti-wall and open ends; a rule/mirror-rule wall in the records gives total parity-odd correlators at 6.1e-16, partners under the wall-plane mirror Delta = 1.1e-16 and partners under a perpendicular mirror up to -7.58e-02. The chiral rules and odds tables are this note's own supplied objects. Interactions, many-body dynamics, wider windows, larger alphabets and geometries other than those named are out of scope. No axiom is changed, no status is set, no hypothesis is adopted, and no registry entry is created."
upstream_dependencies: []
runner: scripts/mirror_asymmetric_rule_registers_own_texture_movers_t_blind_check_2026_09_05.py
---

# A mirror-asymmetric nearest-neighbour rule has one profile to live on and the records read it only where records are missing: no chiral table in the readable label-equivariant class, one chiral profile pair in the wider class, a registered parity-odd texture that never distinguishes a mover from its time-reversed partner

**Date:** 2026-09-05
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/mirror_asymmetric_rule_registers_own_texture_movers_t_blind_check_2026_09_05.py`](../scripts/mirror_asymmetric_rule_registers_own_texture_movers_t_blind_check_2026_09_05.py)
**Runner cache:**
[`logs/runner-cache/mirror_asymmetric_rule_registers_own_texture_movers_t_blind_check_2026_09_05.txt`](../logs/runner-cache/mirror_asymmetric_rule_registers_own_texture_movers_t_blind_check_2026_09_05.txt)
**Parents:** none load-bearing. Every object used below is declared in this note and rebuilt from scratch by the runner; the notes named in "Imports and authority" are plain-text pointers carrying no grade and no dependency weight.

The question this note answers is the owner's: *could chirality be obtained by mirrored valid neighbourhoods, mirrored admissibility or neighbourhood maps?* The Lattice axiom demands covariance under proper rotations only, so a nearest-neighbour rule is allowed to differ from its mirror image, and the question is what the records then see. Three answers were on offer -- a handed medium, a handed registration, or nothing -- and the computation gives a different verdict to each. The designed law is mirror-symmetric throughout, so the medium is not handed. A chiral rule does register handedness, but of a narrow and self-referential kind: it has exactly one four-record profile pair to live on, the readable label-equivariant class contains no chiral table at all, and what a chiral table registers is a parity-odd texture of the records themselves, on partially recorded shapes. And for the object the handedness line actually wants -- the emergent fermion's right-mover against its partner left-mover -- a chiral rule registers exactly nothing, because the two are time-reversal images and the record law is real.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "T1 is a complete integer enumeration over 729 profiles and the two table classes, cross-checked by Burnside counting; T2's stabilisers, role tables, 5x5x5 entries and point-group censuses are complete enumerations at zero or 1e-9 residual; T3's correlator vanishing, the 40320-order census and the T-blindness identity are exact or machine-precision statements on named finite clusters; T4's and T5's registration odds, textures and band energies are floating-point statements on the declared regions, orders and tables at the stated tolerance. The chiral rules and odds tables are supplied by this note. No statement here is a proof about the infinite lattice, and none is read out of any axiom."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-size result, and route to the record-time lane the one object this note prices but does not rebuild: whether the winding reversal n -> -n of the record-time vortex (PR #7935) is a complex conjugation in a record basis, in which case T3's T-blindness lemma applies to it unchanged."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. The complete-enumeration and zero-residual items are exact; the items tagged `[numerical]` are floating-point statements on the named finite geometries at the stated tolerance.

1. `T1` (`A`). The chirality census of the covariant nearest-neighbour support tables: one chiral profile pair, none in the readable label-equivariant class, two thirds of the wider class.
2. `T2` (`B`). The designed matter law -- sectors, role rules, readable record table, sign field, sea -- is mirror-symmetric; the one parity-odd term on the table is not mirror-odd and is not covariant under the axiom's proper rotations.
3. `T3` (`C`). The sea's record statistics are parity-even to machine precision; a single formation order is chiral and the mirror-closed average is not; the record law is exactly time-reversal-blind.
4. `T4` (`D`). A chiral rule registers a parity-odd texture of its own and a partner-fidelity asymmetry on partially recorded shapes, and registers nothing that separates the string's right-mover from the anti-string's left-mover.
5. `T5` (`E`). An `m2`-sign wall binds no handed interface mode, and a rule/mirror-rule wall registers handedness only for movers parallel to it.

## Imports and authority

Imported scientific authority: none load-bearing. Kawamoto-Smit staggered signs, Burnside's counting lemma, determinantal point processes and the Jackiw-Rossi vortex mode are standard methodology and appear below only as **plain-text pointers carrying no authority**; every object is redeclared here and the runner recomputes every statement from scratch. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight: `THE_TASTE_SINGLET_SECOND_MASS_IS_A_BODY_DIAGONAL_IMAGINARY_HOP_AND_ITS_VORTEX_STRINGS_CARRY_2N_CO_MOVING_MODES_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7949, the second mass and the string); `A_VORTEX_IN_A_TWO_DIMENSIONAL_RECORD_TIME_CARRIES_A_SINGLE_WEYL_MODE_IN_THE_INTERIOR_AND_A_REAL_MASS_CARRIES_NONE_BOUNDED_THEOREM_NOTE_2026-09-04.md` (PR #7935); `THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7909); `THE_PARTIAL_CONFIGURATION_READOUT_IS_INJECTIVE_ON_THE_3_TORUS_EVERY_LAW_IS_VISIBLE_TO_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-04.md` (PR #7934) and `A_READABLE_MATTER_LAW_EXISTS_ON_THE_5X5X5_WINDOW_..._BOUNDED_NOTE_2026-09-04.md` (PR #7982), the two readable classes; `THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md` (PR #7939); `NO_SITE_WISE_FORMATION_RULE_PRESERVES_THE_SEA_UNDER_TICK_EVOLUTION_..._NOTE_2026-09-03.md` (PR #7947), `THE_FORMATION_UNIT_THAT_PRESERVES_THE_SEA_IS_A_WHOLE_CLASS_OF_THE_SUPERLATTICE_ROLE_PATTERN_..._BOUNDED_NOTE_2026-09-04.md` (PR #7968) and `THE_STAR_TICKS_RECORD_LAW_IS_EXACTLY_DETERMINANTAL_WITH_A_ROTATED_KERNEL_..._BOUNDED_NOTE_2026-09-05.md` (PR #7986), the tick line; `RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (PR #7883). None is linked and none is on the main line. [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the three clauses quoted in "Setting"; no grade of it is cited and no hypothesis is adopted.

## Setting

The framework axioms are quoted, not amended. **Lattice / Physical Locality**, verbatim:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

**Admissibility / Local Constraint**, verbatim:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.
>
> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

**Record / Fixed Reality**, verbatim:

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

Covariance is demanded under the 24 **proper** rotations only. A covariant rule may therefore differ from its mirror image, and `T1` computes exactly how much room that leaves. The map decision "Mirrors in the Lattice axiom", cited by the parent brief as saying that the emergent matter would be parity-symmetric if the inversion were a lattice symmetry, **is a paraphrase and was not found on `origin/main`** (`git grep -i "mirrors in the lattice"` returns nothing there); it is used here only as the parent's paraphrase and nothing below rests on it.

Supplied by the open branches and taken as they stand: the covariant support-table census and its label-equivariant readable class (PR #7934); the wider readable class without label equivariance (PR #7982); the superlattice role pattern with its 48 sectors and the readable `5x5x5` record table with the corrected-parity completion (PR #7939, PR #7982); the Kawamoto-Smit sign field and the half-filled sea whose record law is determinantal (PR #7883); the star tick with the rotated kernel `K = G P G^+` (PR #7986); the body-diagonal second mass `M2` with the winding phase (PR #7949). Supplied by this note and by no parent: the chiral support rules, the chiral odds table, the formation orders, the regions, the tolerances.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the profile alphabet with its group action, the clusters with their sign fields and seas, the tick, the two readings and the chiral rules. `P1` (`A`) is the profile-orbit census and the two table counts. `P2` (`B`) is the mirror behaviour of the designed law, which uses `P0` only. `P3` (`C`) is the sea's record statistics and the T-blindness lemma, which uses `P0` and `P2`'s gauge result. `P4` (`D`) is the registration battery, which uses `P1`'s chiral orbit, `P3`'s lemma and the clusters of `P0`. `P5` (`E`) is the wall control, which uses `P2`'s `m2` census and `P4`'s battery. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

```text
profile       ternary map from the six offsets (+x,-x,+y,-y,+z,-z) to
              {open, 0, 1}: the nearest-neighbour condition a corner reads
orbit A       (+x:0, -x:1, +y:0, -y:open, +z:1, -z:open) and its 24 proper
              rotations; orbit B its inversion image, which also contains
              (+x:0, -x:1, +y:0, -y:open, +z:open, -z:1)
class A       covariant tables assigning a nonempty menu in {0,1} to each of the
              57 proper orbits WITH label equivariance menu(F p) = F menu(p):
              3^24 tables                                            SUPPLIED
class B       the same without label equivariance: 3^57 tables       SUPPLIED
mirror-sym.   menu(sigma p) = menu(p) for the inversion sigma = -I
chiral rules  A -> {0}; A -> {1}; max = (A -> {0}, B -> {1}); and the
              mirror-symmetric control A, B -> {0}                   THIS NOTE
chiral odds   f(a | p) = exp(lam s (2a-1)), s = +1 on A, -1 on B, 0 elsewhere,
              multiplying the Born odds; control s = +1 on both      THIS NOTE
finished rd.  the rule read on the completed configuration, absent or
              unrecorded neighbours reading open
tick reading  PR #7986 Model A with the star tick: corners determined in the
              order pi, the Born conditional of the rotated determinantal law
              tilted at each formation by f on the forming corner's profile,
              undetermined corners reading open; tau = 0.5
partners      psi_R the E>0 one-particle mode of maximal current along a
              declared axis; psi_L = D sigma psi_R its mirror image
Delta         O_R - O_L with S_R = {n : P_R(n) > P_L(n)} under the untilted
              laws, S_L = sigma S_R, O_R = P_chi,R(S_R), O_L = P_chi,L(S_L)
chi_k(law)    sum over chiral orbit pairs of k-subsets of corners of
              [P(S occupied) over the orbit] - [same over the mirror orbit]
h_KS          eta_x = 1, eta_y = (-1)^x, eta_z = (-1)^{x+y}, h = -eta SUPPLIED
M2            body-diagonal hop M2[bbar, b] = i(-1)^{b_2} on every 2x2x2 cell
              with even corner, m2 its strength                      SUPPLIED
string        m_1 + i m_2 = M_0 tanh(rho/xi) e^{i n phi} about the core, M_0 =
              0.7, xi = 2, on 12x12x24, open plane, periodic axis    SUPPLIED
wall          an m2-sign wall at uniform m1 on a 48-site x-chain, transverse
              cell bits by Bloch (q_y, q_z), theta = pi/4
```

Sizes: the open `2x2x2` cube, the open `2x2x3` slab, the `4x4x4` open block, the `4^3` torus at twist `(1,1,1)`, the `6^3` torus at twist `(0,0,0)` with `2x2xL` column regions, the `12x12x24` string cluster in its 12 cell-momentum sectors of dimension `288`, and the 48-site wall chain. **There is no random number and no seed anywhere in the runner**: every enumeration is complete or a declared sub-family, every formation order and family is declared, and every eigenproblem is a deterministic LAPACK call. The largest dense matrix built anywhere is `288 x 288`; the `3456`-site string is carried sparse. Declared reductions, with the probe output lines that carry the rest, are listed in "Proof boundary".

## Theorem 1 -- one chiral profile pair, none of it usable by the readable class

**Conclusion.** The 729 ternary profiles fall into **57** orbits under the 24 proper rotations and **56** under the full group of 48, so exactly **one chiral orbit pair** exists: 55 orbits are inversion-fixed and 2 are exchanged, and all 24 improper elements induce the same pairing. Burnside counting gives 57 and 56 independently. The pair is orbit `A` above and its inversion image `B`; its shape class is `(4 records, 3 axes touched, 1 full axis)` -- one axis with both neighbours recorded carrying `(0,1)`, one recorded end on each other axis, **two open ends** -- and among the 64 fully recorded profiles there are 10 orbits and **0** chiral ones (Burnside on the binary alphabet: 10 and 10). In PR #7934's readable class of `3^24 = 282429536481` label-equivariant tables, the number of mirror-asymmetric tables is **0**: all 24 digits are inversion-fixed, so label equivariance forces both chiral orbits to the menu `{0,1}` and every table is its own mirror image. In PR #7982's wider class of `3^57` tables, `3^56` are mirror-symmetric and `2 * 3^56 = 1046695266054721074427023042` are not -- exactly two thirds, organised as `3^56` chiral pairs `{T, T^sigma}`. The all-permissive table has **4** nearest chiral neighbours in class B and **0** in class A.

**Reading.** Handedness is available as law content, and it is available in exactly one place: a chiral covariant nearest-neighbour rule over a binary alphabet differs from its mirror image on that one four-record profile pair and nowhere else.

## Theorem 2 -- the designed matter law is mirror-symmetric, and its one parity-odd term is not mirror-odd

**Conclusion.** The 48 sectors of the superlattice role pattern are mapped onto themselves by all 48 elements of `O_h`, the inversion relabelling them with **24 fixed sectors and 12 two-cycles** and keeping every axis family. The realised `(role, profile)` sets -- 18 pairs at nearest neighbour, 22 on the 12-offset window `NN + {+-2 e_d}` -- are preserved by all 48, with **0** failures, and so is the record-level table on the `5x5x5` window: 30 wild-marked exercised entries at pinned centres, **0** failures, with 24 free edge centres of 64 carrying both values and the parity completion a permutation-invariant function of the window. The mirror image of the Kawamoto-Smit field is `D eta D` for a real `Z2` gauge at residual `0.0e+00` on the cube, the slab and the `4x4x4` block, the sea's kernel goes to `D P D`, and the corner record law is mirror-invariant pattern by pattern to `9.2e-16` (cube) and `8.6e-16` (slab). **So the readable record law of PR #7982 is exactly mirror-symmetric.** The exception is PR #7949's second mass: `M2` has 64 purely imaginary entries on the `4x4x4` block, the medium's 348 four-cycles (240 through a body diagonal) have gauge-invariant products that change by up to `0.800 = 2 m_2` under the improper box symmetries **and by the same `0.800` under the proper ones**, while `h_KS` alone is invariant at `0.0e+00`. On the `4^3` torus the medium `h_KS + m2 M2` is preserved by exactly **24** elements -- 12 proper and 12 improper, the pyritohedral group `T_h`, the inversion included -- and the other 24, the 90-degree axis rotations and the diagonal mirrors, send it to `-m2`; `eps M2 eps = -M2` at `0.0e+00`.

**Reading.** PR #7949's "P-odd" is `eps`-conjugation, not a geometric mirror: under the point group the sign of `m_2` is a tetrahedral label reversed by a proper 90-degree rotation, the geometric inversion preserves the medium, and the medium is therefore **not covariant under the axiom's proper rotations**. That is a disagreement with PR #7949, stated plainly, and it is a statement about the supplied operator, not about the axiom.

## Theorem 3 -- the sea is parity-even, the formation order is the chiral object, and the record law is time-reversal-blind

**Conclusion.** On the cube, the slab and the `4^3` torus at twist `(1,1,1)` (48, 16 and 48 symmetries; gaps `3.4641`, `2.8284`, `4.8990`) every improper element sends the sign field to a `Z2` gauge copy at residual `0.0e+00` and the sea's kernel to `D P D` at `8.9e-16`, and the corner record law to itself at `4.6e-16` and `9.2e-16`. The cube carries one chiral pair of 4-subsets and none at `k = 2, 3, 5, 6`; the slab carries `2, 9, 23, 39, 46` pairs at `k = 2..6`. On the sea **every parity-odd correlator vanishes**: `|chi_k| <= 1.4e-17` (cube) and `3.5e-16` (slab), and on the `4^3` torus the helix's translation-averaged parity-odd 4-point Ursell function is `7.0e-19` against a same-shape magnitude sum of `2.7e-18` (the cumulant formula itself checked against the cube's exact law to `1.4e-16`). Under the star tick at `tau = 0.5`, over **all 40320** corner orders of the cube, the single-order law has `max |chi_4| = 0.088127` and mean `0.014096` with `29376` orders nonzero, while the uniform-order average has `chi_4 = 3.1e-19`; over all orders against all 48 symmetries a mirrored order carries `-chi_4` (`2.2e-16`) and a rotated order `+chi_4` (`2.5e-16`). Finally `TV(law of K, law of K*) = 0.0e+00` over the declared cube and slab orders: `p_K(n) = det(diag(n) K + diag(1-n)(I-K))` is real, so **the record law is exactly blind to complex conjugation of the pre-record kernel**. With complete records the cube has 0 chiral-capable corners, the `4^3` torus 0 and the slab 4; some slab corner realises the chiral orbit with probability `0.539063` and the expected number is exactly `1.000000`; an open `L^3` block is capable only on its `12(L-2)` edge lines (12, 24, 36, 48, 72 at `L = 3, 4, 5, 6, 8`), and under a uniformly random formation order a bulk site is capable at its own formation with probability `4/35`.

## Theorem 4 -- what a chiral rule registers, and what it cannot

**Conclusion.** *Cube:* its `E>0` modes carry no current (`+3.2e-16`) and no corner can realise the chiral profile, so all eight tables give one finished law with `Delta = 1.1e-16` and `chi_3 = chi_4 = 0`; the single formation orders are handed with no rule at all (identity `Delta = +2.761e-02`, closed-star-first `+0.154`). *Slab, finished reading* (12 corners, 4096 patterns): the right-mover has `<J> = +0.541196`, the untilted laws are exact mirror images (`4.7e-16`) with `P_R(S_R) = 0.253160`, and the chiral tables give `Delta = -1.32e-02` (`A -> {0}`), `+6.56e-02` (`A -> {1}`), `-4.00e-02` (max), `+0.113` and `+0.273` (the chiral odds at `lam = 0.5, 1.0`), with `chi_3(sea)` down to `-0.439`, against controls at `0.0e+00` and `5.6e-17`; the chiral orbit is exercised with probability `0.5391`. *Slab, tick reading:* averaged over the mirror-closed family of 16 images of an order, the identity family exposes the four-record shape at **0** formation events and every table -- chiral or control -- gives `Delta = 2.2e-16` and `chi_3(sea) = 2.2e-16`, while the even-first family exposes it at **8448** events and the rules act: `Delta = +4.33e-03` (`A -> {0}`), `+5.28e-03` (max), `-1.51e-03` (chiral odds), `chi_3(sea) = -0.139` and `-0.027`, the control still exactly `0.0e+00`. *Torus regions:* the fully recorded `2x2x2` block gives `Delta = 1.7e-16` for every table; the `2x2x3` and `2x2x4` columns give `+1.10e-02` and `+6.62e-03` -- **falling as the region grows** -- while `chi_3(sea)` grows with the number of capable sites (`-0.150` on 4, `-0.573` on 8). *The string:* built as PR #7949 declares it on `12x12x24`, the anti-string is `conj(H_string)` at `0.0e+00`, `H` commutes with the cell translation at `0.0e+00`, and of the 16 elements of `O_h` about the core exactly **2** send the string to a gauge copy of itself (one of them improper: the `x`-mirror), 2 send it to the anti-string, and 12 to neither. In its 12 cell-momentum sectors of dimension 288 the core carries a doublet at `p = +pi/6` with `E = +0.51019` (velocity `0.9744`) and `<J_z> = -1.861`, and `conj(psi_R)` are eigenmodes of the anti-string at the same energies with `<J_z> = +1.861`. On the `2x2xL` core columns for `L = 2, 3, 4` the anti-string's sea kernel is `conj(P)` at `2.2e-16` and **the two record laws are identical**, `TV(P_R, P_L) = 0.0e+00` untilted and under every chiral rule and odds table, although the chiral orbit is exercised there with probability `0.594` and `0.825`. So `S_R = S_L` is empty and `Delta = 0` identically.

**Reading.** A chiral rule registers two things: a parity-odd texture of the sea's own records, of order `1e-1` in `chi_3`, and a partner-fidelity asymmetry `Delta` of order `1e-3` to `1e-1` that does not grow with the region. Both live only where records are missing -- on the edge lines of a recorded region, or at formation events that expose the four-record shape. Neither can separate the string's right-mover from the anti-string's left-mover, because those two pre-record states are complex conjugates in the record basis and every record probability is real.

## Theorem 5 -- the mirror wall binds no handed mode

**Conclusion.** With `(m_1, m_2) = (0.4950, 0.4950)` and node gap `0.700000`, one `m2`-sign wall on an open 48-site chain binds **8** in-gap states at the node; the state nearest zero sits at `E = -0.49497`, exactly `-|m_1|`, with `<M2> = 0.000`, and the band disperses to `0.6298` at `dq_y = 0.4`. The wall-plus-anti-wall geometry carries the same band on the anti-wall (`-0.49499`) and the open ends with no wall at all carry it too (`+0.49497`), all with `<M2> = 0`: a **gapped, massive two-dimensional band with mass `m_1` and no handedness**, identical on wall, anti-wall and boundary. In the records, a wall between the chiral odds table and its mirror image on the two halves of the slab (wall plane `x = 1/2`) leaves the total parity-odd correlators at `6.1e-16` for all four tables; the partners under the mirror **through** the wall plane have `Delta = 1.1e-16`, while the partners under a mirror **perpendicular** to it have `Delta = +1.46e-02`, `+1.76e-03` and `-7.28e-02`. Carrying the rule and its mirror on the two sublattices instead gives `Delta = 2.2e-16` for both mover types; on the `6^3` torus a `2x2x4` column with a wall in `z` gives through-plane partners `2.2e-16` and perpendicular partners `+2.28e-02`, `+2.89e-02` and `-7.58e-02`.

## Corollary -- handedness as law content, and what it is worth

Handedness **can** be law content: the axioms demand covariance under proper rotations only, and `T1` shows a chiral covariant rule exists. But the room is one chiral profile pair of the nearest-neighbour alphabet. PR #7934's readable label-equivariant class cannot use it at all -- every table there is its own mirror image -- and PR #7982's wider class uses it on that pair alone, so every mirror-asymmetric covariant rule over a binary alphabet is a rule that differs from its mirror on one four-record neighbourhood shape with two open ends, and agrees everywhere else.

Such a rule does register handedness, in a narrow and honest sense: it puts a parity-odd texture into the record statistics (`chi_3(sea)` to `-0.439` on the slab, `-0.139` under the formation orders that expose the shape) and it registers one partner's pattern more faithfully than the other's (`Delta` from `-1.32e-02` to `+0.273` on the slab, `+4.33e-03` under the even-first family). That texture is the **rule's own**: the partner-dependent part of it is the same size as the untilted mode signature, and the asymmetry does not grow with the region, while the texture is extensive in the chiral-capable sites, which in a fully recorded block are only the `12(L-2)` edge lines.

For the emergent fermion's movers it is identically zero. The string's core right-mover and the anti-string's core left-mover are **time-reversal images** -- the anti-string is the conjugate Hamiltonian at `0.0e+00` -- and the record law is exactly time-reversal-blind, so no covariant rule, chiral or not, and no real odds table changes any registered quantity that distinguishes them. Alongside that: the designed law, its role rules, its readable completion and the sea's statistics are all mirror-symmetric, and a wall between a rule and its mirror rule binds no handed interface mode, only a massive band at `|E| = m_1` that is the same on wall, anti-wall and boundary.

What this buys toward Root B, the weak sector's chiral coupling: **a place for handedness in the law, not a handed fermion**. The weak sector needs a coupling that acts on left-handed movers only -- handedness-dependent dynamics, time-reversal-even and parity-odd. A chiral admissibility rule buys a parity-odd static texture in the record statistics and a fidelity asymmetry between mirror-partner modes on partially recorded shapes; it buys no chiral dispersion and no separation of a right-mover from its time-reversed partner. The handedness Root B needs would have to enter through the supplied hop structure, which the axioms do not supply and which a support or odds rule does not substitute for. What does move: the Lattice axiom's silence about mirrors is not what keeps the emergent matter parity-symmetric, since the readable rule class is mirror-symmetric on its own and the tick's records are mirror-symmetric on the physical average.

**Reading, not theorem (this register).** Ask whether the world could be left-handed because the rule for what may sit next to what is left-handed, and the arithmetic answers in a way that is easy to say in plain words. There is exactly one neighbourhood picture that is not the same as its own reflection: a corner with both neighbours along one axis recorded, one neighbour recorded on each of the other two, and two directions still blank. Everything else looks the same in a mirror. So a handed rule is a rule about that one half-finished picture, and it can only ever act where the records are unfinished -- along the edges of a recorded region, or at the moment a record forms next to blanks. Fill the block in completely and the rule has nothing to say. Worse, for the thing one actually wants handed, the rule is not merely weak but blind: the mover and its partner are related by running time backwards, and what the records give back is a determinant of a real quantity, which cannot tell a thing from its time-reverse. So a handed rule paints a handed pattern of its own onto the unfinished parts of the record, and the fermion it is supposed to sort walks straight past it.

**Disagreements with the expectation, stated plainly.** (1) "A covariant rule may differ from its mirror image, so handedness can be law content" is true in the wider class and false in the readable label-equivariant class, where the rule is never handed. (2) The chirality of such a rule is confined to one four-record profile pair with two open ends, so "handedness as law content" is content about partially recorded neighbourhoods. (3) PR #7949's second mass is **not** mirror-odd: the geometric inversion preserves the medium, proper 90-degree rotations reverse it, the medium is only tetrahedrally covariant, and it therefore **fails the Lattice axiom's proper-rotation covariance**, which that note does not state. (4) The expected "registration odds" between a mover and its partner are not small but identically zero, by T-blindness. (5) A single formation order produces registered parity-odd correlators (`max |chi_4| = 0.088127`) with no chiral rule at all, and the mirror-closed average removes them: chirality in the records can come from the order, not only from the rule. (6) The `m2`-sign wall binds no handed mode, so PR #7909's counting question does not arise for it. (7) The probe's own `+6` for the net `<J_z>` of the string's in-gap ring states is a sign-of-zero artefact: 8 of the 16 in-gap states carry a current, netting `-4` on the core against `+4` on the ring, and the other 8 sit at `p = 0` with `<J_z> = 0` to `1.2e-14`, whose sign is not determined; this note uses `+4`.

## The framework reading -- supplied item by item

**Supplied.** The two table classes and the readable completion (PR #7934, PR #7982); the superlattice role pattern and its 48 sectors (PR #7939); the Kawamoto-Smit sign field and the half-filled sea (PR #7883); the star tick and the rotated kernel with `tau = 0.5` (PR #7986); the second mass `M2`, the winding phase, the profile `M_0 tanh(rho/xi)` and the core position (PR #7949); and, from this note, the chiral support rules, the chiral odds table with `lam in {0.5, 1.0}`, the formation orders and their mirror-closed families, the regions, the wall geometry and every tolerance. **Derived, given those:** the orbit and table counts of `T1`; the stabilisers, role-table and record-table invariances, the gauge results and the `T_h` census of `T2`; the correlator vanishing, the order census and the T-blindness lemma of `T3`; every registration number of `T4`; and the band and wall results of `T5`. Nothing here is read out of an axiom; the axiom text is quoted only to fix what covariance demands.

## What is not changed

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. The Lattice axiom is quoted, not weakened.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited. The ledger is fully unaudited since 2026-08-07, and no status word here describes any current audit standing.
- Nothing here is read out of the axioms: the rules, the tables, the odds, the orders, the regions and the geometries are declared objects, and no coefficient is derived.
- Nothing here is framed as foreclosing anything. `T1` bounds what a *nearest-neighbour ternary support table over a binary alphabet* contains; it says nothing about wider windows, larger alphabets or constructions outside the declared setting.

## Interfaces named for other lanes, not taken up here

- **PR #7949** (the second mass and its `2n` string): its `M2` medium is `T_h`-covariant and not covariant under the axiom's proper rotations, and its string's handedness reverses under time reversal, not under a mirror. Both belong to that lane.
- **PR #7935** (the record-time vortex): **not rebuilt here.** Whether its winding reversal `n -> -n` is a complex conjugation in a record basis, so that `T3`'s T-blindness lemma applies unchanged, is the first thing a follow-up should compute.
- **PR #7909** (the single-wall counting rule): `T5` finds a gapped band and no handed interface mode at an `m2`-sign wall, so that rule's counting question does not arise for this wall.
- **PR #7934 and PR #7982** (the two readable classes): `T1` prices the chirality available in each. Whether a wider window or a larger alphabet reopens it belongs to those lanes.
- **PR #7939** (the role law) and **PR #7986 / #7947 / #7968** (the tick line): the role rule and the star tick are used as declared; the finding that a single order is chiral while the mirror-closed average is not is offered to the tick lane.
- **PR #7883** (the determinantal record statistics): the T-blindness lemma is a property of that law and is stated here in the form the registration argument needs.

## Remaining live routes

1. The record-time vortex of PR #7935, rebuilt, with the conjugation question above settled.
2. Wider admissibility windows and larger alphabets, where the chiral orbit count is not one; nothing here computes them.
3. The many-body statements. Everything here is one particle plus a determinantal record law: no interaction, no dynamics for the phase, no anomaly matching.

## Executable claim block

```text
setting: ternary nearest-neighbour profiles over a binary record alphabet with the 24 proper and 24 improper cubic elements; open 2x2x2, 2x2x3 and 4x4x4 blocks, 4^3 torus at twist (1,1,1), 6^3 torus with 2x2xL regions, 12x12x24 string in 12 sectors of dimension 288, 48-site wall chain; SUPPLIED: the two table classes, the role pattern, the KS field and half-filled sea, the star tick at tau = 0.5, M2 with M_0 = 0.7 and xi = 2, and this note's chiral rules, chiral odds (lam = 0.5, 1.0), orders, regions and tolerances; axiom clauses quoted from MINIMAL_AXIOMS_2026-06-29.md
T1 census [exact]: 729 profiles -> 57 proper orbits, 56 full orbits, 55 achiral + 1 chiral pair, all 24 improper elements inducing the same pairing; Burnside 57/56 and 10/10 binary; chiral shape (4 records, 3 axes, 1 full axis), 2 open ends; fully recorded profiles 10 orbits, 0 chiral; class A 3^24 = 282429536481 tables, 0 mirror-asymmetric, 24 'fixed-same' digits, 0 nearest chiral neighbours; class B 3^57 tables, 3^56 symmetric, 2*3^56 = 1046695266054721074427023042 asymmetric = 2/3 exactly, 4 nearest chiral neighbours
T2 designed law [exact / 1e-9]: template-set stabiliser 48 (24 improper), inversion relabelling 24 fixed + 12 two-cycles, axis families kept; role tables 18 and 22 realised pairs, 0 failures; T_min^W 30 entries at pinned centres, 0 failures, 24 free edge centres, parity completion permutation-invariant on 50 x 48 patterns; KS mirror gauge residual 0.0e+00, record law invariant to 9.2e-16 (cube) and 8.6e-16 (slab); M2 64 purely imaginary entries, 348 four-cycles (240 body-diagonal), products change 0.800 under improper AND 0.800 under proper rotations while h_KS gives 0.0e+00; on the 4^3 torus 24 elements preserve the medium (12 proper + 12 improper = T_h with the inversion), 24 send m2 -> -m2, 0 neither; eps M2 eps = -M2 at 0.0e+00
T3 sea statistics [1e-15]: cube/slab/torus 48/16/48 symmetries, gaps 3.4641/2.8284/4.8990, gauge residual 0.0e+00, kernel 8.9e-16, record law TV 4.6e-16 and 9.2e-16; chiral k-subset pairs cube [0,0,1,0,0], slab [2,9,23,39,46], all chi_k <= 1.4e-17 and 3.5e-16 on the sea; helix P-odd Ursell 7.0e-19 against 2.7e-18, cumulant check 1.4e-16; all 40320 cube orders at tau = 0.5: max |chi_4| = 0.088127, mean 0.014096, 29376 nonzero, uniform average 3.1e-19, mirrored order -chi_4 at 2.2e-16, rotated +chi_4 at 2.5e-16, minors vs exact law 2.8e-17; TV(law K, law K*) = 0.0e+00; capable corners cube 0, torus 0, slab 4, exercise probability 0.539063 with expected number 1.000000; blocks 12(L-2); bulk formation rate 4/35
T4 registration [numerical]: cube <J> 3.2e-16, Delta 1.1e-16 for all eight tables, single orders +2.761e-02 and +0.154; slab <J> +0.541196, mirror TV 4.7e-16, P_R(S_R) 0.253160, Delta -1.32e-02/+6.56e-02/-4.00e-02/+0.113/+0.273, chi_3(sea) to -0.439, controls 0.0e+00 and 5.6e-17, exercise 0.5391; tick identity family 16 images, 0 events, Delta 2.2e-16, chi_3(sea) 2.2e-16; even-first family 8448 events, Delta +4.33e-03/+5.28e-03/-1.51e-03, chi_3(sea) -0.139/-0.027, control 0.0e+00; torus 2x2x2 Delta 1.7e-16, 2x2x3 +1.10e-02 (chi_3 -0.150, 4 sites), 2x2x4 +6.62e-03 (chi_3 -0.573, 8 sites); string anti = conj(H) 0.0e+00, [H,T^2] 0.0e+00, 16 elements -> 2 string (1 improper x-mirror), 2 anti-string, 12 neither; core doublet E +0.51019, velocity 0.9744, <J_z> -1.861, anti-string partner +1.861 at residual 4.6e-15; core columns L = 2,3,4 exercise 0.000/0.594/0.825, anti kernel conj(P) 2.2e-16, TV(P_R, P_L) = 0.0e+00 for every table -> Delta = 0
T5 wall [1e-4]: (m1, m2) = (0.4950, 0.4950), node gap 0.700000, one wall 8 in-gap states at the node, nearest E -0.49497 = -|m1|, <M2> 0.000, dispersing to 0.6298 at dq_y = 0.4; anti-wall -0.49499 and open ends +0.49497, <M2> = 0; slab x-wall |chi| <= 6.1e-16, wall-plane partners 1.1e-16, perpendicular +1.46e-02/+1.76e-03/-7.28e-02; sublattice 2.2e-16 both types; 6^3 col4 z-wall |chi| <= 1.1e-15, through-plane 2.2e-16, perpendicular +2.28e-02/+2.89e-02/-7.58e-02
supplied: the chiral rules and odds table; the two table classes; the role pattern; the KS field and sea; the star tick and tau; M2, the winding phase, the profile and the core; the orders, regions, geometries and tolerances
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=27 FAIL=0
```

## Proof boundary

**Alphabet and rules.** Nearest-neighbour ternary support tables over a binary record alphabet -- the `3^24` label-equivariant class and the `3^57` class. Wider windows and larger alphabets are not treated. The chiral rules and odds tables act on the corner occupations `n_v`, **a derived quantity of the edge records** (PR #7883 / PR #7986), and on the fine lattice would be rules on the 12-offset window over same-type edge sites; this note does not lift them there.

**Geometries.** The open `2x2x2` cube, the open `2x2x3` slab, the `4x4x4` open block, the `4^3` torus at twist `(1,1,1)`, the `6^3` torus at twist `(0,0,0)` with regions of at most 16 corners for the tilted laws, the whole cube and slab for the tick reading (`tau = 0.5`, all 40320 cube orders for `chi_4`, 16-image families of the declared slab orders), the string on `12x12x24` with the declared `M_0`, `xi`, core and momenta, and the wall on a 48-site chain at `theta = pi/4`. Nothing is claimed at other sizes, other profiles or other boundary conditions.

**Declared reductions this runner makes,** with the probe output lines that carry the rest. (1) The string is solved in its 12 cell-momentum sectors rather than by one dense `3456 x 3456` eigh; the sector decomposition is certified by `[H, T^2] = 0.0e+00`, orthonormality `2.2e-16` and eigen-residual `4.8e-15`. Its parity-odd occupation-minor density map over the whole plane is **quoted, not recomputed** (`h4_string.py -> out_string.txt:13`, ST3.2d: whole-plane sum `-2.4e-17`, `max |rho| = 3.96e-04`, every shell sum `<= 2.2e-16`; the Ursell version `6.1e-18` at line 14), as is the `2x2x5` core column (`out_string.txt:39-44`, ST4.col5: `TV = 0.0` at exercise probability `0.914`). (2) The slab's tick reading recomputes the identity and even-first families; the deg4-first and rshift3 families are quoted (`out_tickfamily.txt:17-32`: deg4-first `Delta = +2.27e-03` and `+1.86e-03` at the same 8448 events, rshift3 identical to the identity family). (3) The `6^3` torus recomputes the `2x2x2`, `2x2x3` and `2x2x4` regions; the `2x2x5` column (`out_registration.txt:102-110`: `Delta = +5.05e-04`, `chi_3(sea) = -1.25`) and the `3x3xL` rods (`out_registration_rod.txt:2-20`: `3x3x1` `Delta = -2.2e-16`, `3x3x2` `Delta = -2.01e-03` with `chi_3(sea) = +1.11`) are quoted. (4) The wall spectrum is scanned at the declared points `(dq_y, dq_z) = (0,0)` and `dq_y in {0.1, 0.2, 0.3, 0.4}` at `dq_z = 0`, not over the full `13 x 13` grid.

**Estimates, named as such.** The roughly 3 % bulk formation-event rate quoted in the corollary is an **estimate**: `4/35 = 0.1143` is exact for the shape under a uniformly random order, and the conditional `1/4` for the chiral values is the slab's exact finished-reading value per capable corner, but their product is not computed as a bulk rate on any cluster here.

**Not claimed.** That any chiral rule is the framework's rule -- none is landed, and the chiral rules and odds tables are this note's own supplied objects. Any derivation of `M2`, the winding phase, the profile, the core position, the formation order, `tau`, or the tilt. The record-time vortex of PR #7935, which is not rebuilt. Anything about the infinite lattice. **Nothing here is read out of the axioms**; the axiom text is quoted only to fix what covariance demands.

## Review record

**Honest-auditor read.** An auditor should come away with three exact results and two numerical censuses, in that order. First, the **census**: one chiral orbit pair among 57, zero chiral tables in the readable label-equivariant class, two thirds of the wider class chiral but differing from their mirrors on that single four-record profile pair -- complete integer enumeration, Burnside-cross-checked. Second, the **designed law is mirror-symmetric**: sectors, role rules, `5x5x5` record table, sign field and sea, at residual `0.0e+00` and `9.2e-16`, with the one parity-odd term on the table turning out to be `eps`-odd rather than mirror-odd and, more sharply, not covariant under the axiom's proper rotations. Third, **T-blindness**: `TV(law of K, law of K*) = 0.0e+00`, from which the string's right-mover and the anti-string's left-mover have identical record laws under every real odds table, `TV = 0.0e+00` on every column. Then the censuses: the registration numbers on the slab, the tick families and the torus regions, and the wall band at `|E| = m_1` with `<M2> = 0`.

The auditor should also come away with five caveats. The registration numbers are **floating-point statements on small finite regions** with at most 16 corners for the tilted laws, and the `Delta` values are of the same size as the untilted mode signature, so the reading "the registered handedness is dominantly the rule's" rests on that comparison and not on a limit. The **chiral rules and odds tables are supplied by this note**, so what is bounded is what the declared construction gives, not what the axioms give. The string statement is exact where it matters (`conj` at `0.0e+00`, `TV` at `0.0e+00`) but the **record-time vortex is not rebuilt**, and whether the same lemma applies there is open. The bulk formation-event rate is an **estimate**, named as one in the boundary. And the probe's `+6` ring current count is corrected here to `+4` with 8 zero-current states at `p = 0`, a sign-of-zero artefact rather than a physical difference.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the pointers in "Imports and authority" carry no grade and no weight. The ledger is fully unaudited since 2026-08-07, and no status word in this note describes any current audit standing. Hard landing conditions are a fresh runner and cache pair closing at `PASS=27 FAIL=0`, runtime under the declared `AUDIT_TIMEOUT_SEC = 200` seconds, and passing pipeline and strict-lint gates; independent audit remains a separate lane.

## Validation

Run:

```bash
python3 scripts/mirror_asymmetric_rule_registers_own_texture_movers_t_blind_check_2026_09_05.py
```

Expected terminal summary:

```text
TOTAL: PASS=27 FAIL=0
```
