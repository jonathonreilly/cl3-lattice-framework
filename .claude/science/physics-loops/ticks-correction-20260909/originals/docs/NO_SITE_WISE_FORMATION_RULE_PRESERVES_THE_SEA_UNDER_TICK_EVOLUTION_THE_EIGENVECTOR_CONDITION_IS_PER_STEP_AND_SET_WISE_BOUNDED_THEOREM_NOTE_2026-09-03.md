---
claim_id: no_site_wise_formation_rule_preserves_the_sea_2026_09_03
claim_type: bounded_theorem
claim_scope: "On two finite subgraphs of the cubic lattice with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, in the staggered (pi-flux) Kawamoto-Smit sector H = -sum_e eta_e T_e, t = 1, at half filling -- the 2x2x2 cube (8 corners, 12 edge sites, record space 2^12, sea E = -4 sqrt 3) and the 2x2x3 slab open in z (12 corners, 20 edge sites, record space 2^20 held on the half-filled sector J, |J| = 473088, sea E = -(8 + 2 sqrt 2)) -- for the STIPULATED tick of PR #7876 Model A (Lueders formation with the Born odds of the pre-record state; exp(-i tau H_R) between formations, H_R the hop terms on the unrecorded edges) and for the DECLARED formation rules A1/A1v (energy above the sea, edge and corner form), A2/A2v (energy scale), B (least entangled first), E (eigenvector first), the 24 declared orders C and the corner-set rule D, each walked as a complete exact tree (greedy paths for the stochastic rules, the odds along the path quantified): (T1) at tau = 0 every rule reproduces the sea's registration exactly (TV <= 8.2e-17), so rate selection in the instantaneous limit says nothing about rates; (T2) at tau = 0.5 every site-wise rule and every one of the 24 orders ends at TV 0.289-0.456 from the sea's law with all 256 cancellation zeros lost (support 2240), the average of the 24 orders is closer (0.239) with the same support, the same holds at tau = 0.1 and 2.0, and D keeps all 2112 zeros at TV <= 1.2e-15; (T3) on the slab, exact sparse trees to six records at tau = 0.5 give full-law TV 0.115-0.139 after one record and 0.212-0.409 after six for every rule, while the leaf-TV on the formed sites is <= 7.2e-14 at three records for every rule and through six for A2/A2v; (T4) the energy-above-sea rule is exactly uniform in the instantaneous limit and at finite tau orders formation along the evolution's own energy spread -- the four parallel z-edges, a matching -- with the greedy site carrying 0.50-1.00 (cube) and 0.44-0.61 (slab) of the odds at steps 2-4, its record odds exact for three records and off by 0.189 at the fourth; the corner energy-scale form follows the degree-4 corners' edges and is the worst rule by the full law (0.409); (T5) the SUFFICIENT condition is per step and set-wise: if the conditioned state is an H_R eigenvector after each formation the registration is exact for every tau, which holds when each formed set is a union of whole corner stars satisfying the two-mode condition, and the necessary diagonal-invariance (dephasing) condition is met by no non-eigenvector node in any of 12 scanned trees (0 of 27848; smallest displacement 7.1e-05) and by no single edge site at any step (best-site residual >= 0.496 for seven steps on the cube, 0.5638-0.7354 on the slab); (T6) the column pair of degree-3 stars star(0) u star(2) on the slab restores the exact eigenvector property as a six-record joint tick (residual 2.1e-15 at all 64 outcomes, full-law TV 3.6e-16 after the tick) although each star alone leaves 0.207107 = (sqrt 2 - 1)/2 and the same six sites formed one at a time with tau = 0.5 ticks end at TV 0.316. The tick, the rules and the orders are stipulated reconstructions supplied by no axiom; no rate, unit or tick is foreclosed; the dephasing condition is shown unmet numerically, not proved impossible. No seeds anywhere."
upstream_dependencies: []
runner: scripts/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.py
---

# No site-wise formation rule preserves the sea's registration under tick evolution; the eigenvector condition is per step and set-wise

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.py`](../scripts/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.txt`](../logs/runner-cache/no_site_wise_formation_rule_preserves_the_sea_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

`RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_..._2026-09-03.md` (open PR #7876) found that on the `2x2x2` cube no pre-record state is invariant under all the post-record
Hamiltonians, so a tick in which records form one site at a time with unitary evolution between them does not reproduce the sea's registration. `JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_...`
(open PR #7900) and `THE_CORNER_EIGENVECTOR_PROPERTY_IS_A_TWO_MODE_SPECTRAL_CONDITION_...` (open PR #7902) found the one unit that does: a corner's whole record set forming together, at
corners whose site vector lives in exactly two one-particle modes. The question those results leave open, asked with the formation-rate ruler of PRs #7916 and #7925 in view, is whether
a **site-wise rule that chooses where the next record forms** -- a rate keyed to the local energy above the sea, or any other function of the pre-record state -- could restore the sea's
registration where the plain tick loses it. This note answers it on the cube and on the `2x2x3` slab, by complete exact trees: **no.** The site rule is invisible without evolution,
changes the distance to the sea by at most a factor `1.6` with it, and never recovers the sea's zeros. The preserving rule lives in the **set** a tick forms, per step, and that set-wise
rule extends one step beyond the flat-band corners -- as a six-record joint tick on a pair of degree-`3` stars, never site-wise.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on two named clusters -- the 2^12 record space of the 2x2x2 cube and the 2^20 record space of the 2x2x3 slab, in the staggered sector at half filling -- for the stipulated tick of PR #7876 Model A and for formation rules declared in full in this note. Every tree is a complete exact enumeration in the unnormalised-branch form (one vector per level, one node label per basis state), so the final laws, the per-node residuals and the per-node diagonal displacements are deterministic double-precision evaluations of exactly specified quantities at the stated thresholds; the propagator is a Chebyshev series under the rigorous bound ||H_R|| <= number of free edges, checked against expm_multiply to 1e-16. The setting checks are exact symplectic Pauli and F2 arithmetic. Nothing is sampled, there is no seed anywhere in the runner, every order and set is written out, and no dense object above 4096 x 4096 is formed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Carry the set-wise criterion into the tick lane as the object to compute: which unions of corner stars are eigen-sets on a given cluster, by the invariance of the occupied one-particle space restricted to the deleted vertex set -- the multi-site form of PR #7902's two-mode condition -- and whether every corner of a larger open slab belongs to some eigen-set; report the full record law, never the leaf statistics."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six theorems below, exactly the runner's check groups: the cube's setting (`A1`), `T1` (`A2`), `T2` (`A3`-`A5`), `T4` on the cube (`A6`), `T5`
(`A7`-`A8`), the slab's setting (`B1`), `T3` (`B2`-`B4`), `T4` on the slab (`B5`), `T6` (`B6`-`B7`) and the timing (`B8`). `A1` and `B1` carry **exact** content: the encoding
relations `R0`-`R4` in symplectic Pauli arithmetic with phases mod `4`, the face group, the flux sector, and the cluster combinatorics. Everything else is a **deterministic
double-precision evaluation** of an exactly specified quantity at the stated threshold. Nothing is sampled: the Lanczos start vector on the slab is the fixed vector
`cos(0.7 i + 0.3) + i cos(1.3 i + 1.1)` projected into the code space, written out in the runner, and every rule, order and set is written out there too. There is **no seed anywhere**.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggered signs, Lueders conditioning, Lanczos, the Jacobi-Anger
expansion of the propagator and the total-variation distance are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's
relations included. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight, with each one's
state at the time of writing: `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7876, not on main** -- the tick, Model A, its
representative `tau = 0.5`); `A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7895, not on main** -- the
relaxation tick `M_R`, a different model already excluded there, and the restriction identity `P_S H P_S = H_R`);
`JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_UNDER_THE_UNITARY_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7900, not on main** -- the corner-set unit, rule
`D` here); `THE_CORNER_EIGENVECTOR_PROPERTY_IS_A_TWO_MODE_SPECTRAL_CONDITION_EXACT_ON_FLAT_BANDS_NOT_GENERAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7902, not on main** -- the
two-mode condition, the slab's failing degree-`3` corners, and the blindness of marginal tests);
`THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7916, not on main** -- the ruler
whose rate form the energy-above-sea rule `A1` reproduces) and `A_FORMATION_RATE_RULER_EVADES_THE_SEAS_SUBLATTICE_CANCELLATION_..._2026-09-04.md` (**open PR #7925, not on main** --
the corner form of that rate, `A1v` here); and `MINIMAL_AXIOMS_2026-06-29.md` (on main), from which the axiom text in "Setting" is quoted verbatim. This note cites no grade of any
and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. Lattice / Physical Locality and Qubit / Site Possibility are used only through the graph structure of the two clusters and the
`M_2(C)` site algebra. **Admissibility / Local Constraint**, verbatim: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Reading note (2), interpretive and
non-governing, is quoted with it because it is what makes every rule below a free choice: "Read with Record, the distribution concerns which possibility a forming record locks,
conditional on formation at that site; it does not supply the formation site, probability, or rate." **Record / Fixed Reality**, verbatim: "Records form." "When present, a record locks
exactly one admissible local possibility. A site never carries more than one record; records are permanent." "Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read."

Composition is **ordinary**: the algebra of a region is the tensor product of its sites' algebras and operators on disjoint regions commute. A record at an edge site **registers** a
`Z`-value there; it does not report one the site already carried. The **tick** is PR #7876's Model A, adopted unchanged: a forming record locks its value by Lueders conditioning with
the Born odds of the current pre-record state, and between formations the pre-record state runs by `exp(-i tau H_R)`, `H_R` the sum of the hop terms on the unrecorded edges, which is
exactly `P_S H P_S` on the record sector because every hop's Pauli `X`-part is one edge qubit. `tau = 0` is the boundary in which records form faster than the state can run.

**The rules, declared in full.** A rule is a map (current state `psi`, record set `R`) to the next site. Greedy means the deterministic argmax, ties broken by the lowest edge index
after rounding to `1e-9`. `A1`, energy above the sea: `r_q = max(eps_q(psi) - eps_q(sea), 0)`, `eps_q = <psi|h_q|psi>` with `h_q = -eta_q T_q` the hop term of edge `q`; its stochastic
odds are `r_q / sum r` (uniform when all vanish), and along the greedy path the runner reports their **contrast** (largest odds times the number of free sites, `1` = uniform) and the
odds of the greedy site. `A1v`, the corner form: `eps_v = (1/2) sum_{e in star(v)} eps_e`, `r_e = max((excess_i + excess_j)/2, 0)` for `e = (i, j)`. `A2`, energy scale: `r_q =
|eps_q(psi)|`; `A2v` its corner form. `B`, least entangled first: argmax of the purity `Tr rho_q^2` of the one-site reduced state, `rho_q = [[p0, c], [c*, p1]]`. `C`, declared orders:
the identity `0..11` and its `11` cyclic shifts, the reverse and its `11` cyclic shifts (`24` orders on the cube); the identity `0..5` on the slab. `D`, corner sets: joint formation of
whole corner stars on the even sublattice -- cube `star(0), star(3), star(5), star(6)`, a partition of the `12` edges; slab `star(4), star(7)` (degree `4`) -- evolving after each star.
`E`, eigenvector first: argmin over free `q` of the Born-weighted `H_{R+q}` eigenvector residual of the two conditioned states; the rule **exists** at a step iff that minimum is `0`.

**Reading, not theorem.** The tick, Lueders formation with Born odds, the rate rules and the declared orders are stipulated reconstructions of what would be registered -- they are
not axiom content, and nothing here is presented as following from an axiom. Reading note (2) is explicit that Admissibility supplies no formation site, probability or rate; the axioms
supply no formation unit either. Every rule above is a candidate for what the axioms leave open, and the theorems say what each candidate does to the sea's registration.

## Definitions

The **cube** is the `2x2x2` cube graph: `8` corners, `12` edge sites, `6` faces, every corner of degree `3`, record space `2^12 = 4096`. The **slab** is the `2x2x3` lattice open
in `z`: `12` corners, `20` edge sites, `11` faces, degree `4` at the four middle corners `1, 4, 7, 10` and `3` at the other eight; vertices indexed `(x*Ly + y)*Lz + z`; its record
space `2^20` is held on the half-filled sector `J` (`N = 6`, `|J| = 473088`). The encoding, the staggered signs `eta_x = 1`, `eta_y = (-1)^x`, `eta_z = (-1)^(x+y)` (flux `-1` on
every face of both clusters), `H = -sum_e eta_e T_e` with `T_ij = (i/2) A_ij (B_i - B_j)`, the code space (all `S_f = +1`, dimension `128` and `2048`) and the **sea** (the ground
state of `H` there at half filling) are PR #7902's. A **tree** is the complete branching of the tick under a rule: a node is a record set `R` with values `w` and the branch state
`psi_{R,w}`; the **law** after every edge has formed is the distribution on the `2^12` patterns (cube), and the **full law** at `k` records on the slab is the `20`-edge law obtained by
registering every remaining edge at once from the propagated branches. `TV` is total variation, `(1/2) L1`, against the sea's Born law. The sea's **zeros** on the cube are `2112`:
`1856` **charge zeros** (patterns with `N != 4`) and `256` **cancellation zeros** (the `8` closed corner stars times `32`), both exact. The **residual** of a branch state under `H_R`
is `||H_R psi - <H_R> psi||`; the **diagonal displacement** of a tick is the `TV` by which `exp(-i tau H_R)` changes the branch state's `Z`-diagonal; **margerr** is the difference
between the next record's odds and the sea's own conditional `P_sea(z_q = b | z_R = w)`; the **leaf-TV** at `k` records is `(1/2) sum_leaves |p_rule - p_sea|` on the formed sites.

## Theorem 1 -- with no evolution every rule is exact, so the instantaneous limit says nothing about rates

**Conclusion.** `[numerical, 1e-12]` At `tau = 0` every rule -- `A1`, `A1v`, `A2`, `A2v`, `B`, `E`, `D`, each of the `24` declared orders and their average -- ends at `TV <= 8.2e-17`
from the sea's law, with support `1984` and all `1856` charge and `256` cancellation zeros kept; the next record's odds equal the sea's own conditional at every node
(`margerr <= 4.1e-17`). The energy-above-sea odds are **exactly uniform** at steps `1`-`5` (contrast `1.0000` at each). `[numerical, 1e-12]` The conditioned sea is an `H_R`
eigenvector after a single edge forms at none of the `12` edges (residual `0.577350 = 1/sqrt 3` at every one) and exactly when a corner star is completed (`1.4e-14` at `star(0)`);
rule `E` on the un-evolved sea finds this by itself, `0.577 / 0.577 / 0.000` at its first three records.

**Proof.** Sequential Lueders conditioning of a fixed state is order-independent and the products of the conditional odds telescope to the state's own Born law, so with no evolution
every tree returns the sea's law identically; the runner walks each tree anyway and reports the distance. Uniformity of `A1`: Lueders conditioning deposits the excess energy on the
recorded edge alone (`<h_e>` goes from `-0.5774` to `0`) and leaves every unrecorded edge's local energy untouched until the record set contains a whole star, and on the flat-band cube
even then only at the star's neighbours.

**Reading, not theorem.** The rule is invisible without evolution. Rate selection in the instantaneous limit is exact for every rule and therefore tests none.

## Theorem 2 -- on the cube every site-wise rule loses all 256 cancellation zeros, at every declared tick

**Conclusion.** `[numerical, 1e-12]` At `tau = 0.5`, the final `4096`-pattern law sits at `TV` `0.337565692` (`A1`), `0.320717027` (`A1v`), `0.422413255` (`A2`), `0.449953329`
(`A2v`), `0.453896665` (`B`), `0.362827766` (`E`) from the sea's, with support `2240` -- all of `N = 4` -- so every one of the `256` cancellation zeros is lost while the `1856` charge
zeros are kept by everything (`N` is conserved and diagonal in the record basis). The `24` declared orders give `0.289380397` (the reverse order, the best) to `0.456208220`, mean
`0.379401338`, identity `0.324925161`, each with support `2240`; the **average** of the `24` laws is closer, `TV 0.239288631`, and has support `2240` as well, so no mixture of site-wise
trees reaches the sea. Rule `D` keeps all `2112` zeros at `TV 6.8e-16`, its branch states eigenvectors at every node (residual `<= 1.4e-14`, diagonal displacement `<= 1.1e-15`).
`[numerical, 1e-12]` At `tau = 0.1`: `A1 0.2603`, `A1v 0.1298`, `A2 0.0704`, `A2v 0.2679`, `B 0.1527`, `E 0.1203`, orders `0.0459`-`0.2990`; at `tau = 2.0`: `0.4691`, `0.3604`,
`0.4662`, `0.3263`, `0.3698`, `0.4149`, orders `0.3272`-`0.5243`; every site-wise law has support `2240` and `0` of `256` cancellation zeros at both, the rules cross each other
(`A2` best at `0.1`, among the worst at `0.5` and `2.0`), and `D` is exact at both (`3.2e-16`, `1.2e-15`).

**Proof.** Complete exact trees: `124` of them on the `4096`-dimensional record space, each level one vector, each node's odds a bincount, each evolution the Chebyshev series of
`exp(-i tau H_lev)` with `H_lev` the sparse `H` with every node's own recorded hops masked out. The census counts the patterns of the final law below `1e-14` against the sea's exact
zero set.

**Reading, not theorem.** Whatever site the rule prefers, the first tick after the first record already leaks weight into the patterns the sea forbids, and no later choice takes
it back. Choosing the order changes the distance by a factor of at most `1.6`; it never changes the support.

## Theorem 3 -- on the slab the full law leaks from the first record and the leaf statistics cannot see it

**Conclusion.** `[numerical, 1e-10]` Exact sparse trees to six records at `tau = 0.5`, full `20`-edge law against the sea's, for `A1 / A1v / A2 / A2v / B / E / C`: after one record
`0.1148 / 0.1148 / 0.1259 / 0.1387 / 0.1259 / 0.1259 / 0.1148`, the propagated object already off the sea's support `411648` (supports `436224`-`458752`); after six
`0.3727 / 0.2116 / 0.3895 / 0.4089 / 0.3431 / 0.3167 / 0.3156`. The sites formed, in order: `A1` `(0,1)(3,4)(6,7)(9,10)(5,11)(2,8)`; `A1v` `(0,1)(0,3)(0,6)(6,7)(6,9)(3,9)`; `A2`
`(0,3)(0,6)(3,9)(0,1)(5,11)(6,9)`; `A2v` `(1,4)(7,10)(1,7)(0,3)(5,11)(2,8)`; `B` `(0,6)(0,3)(0,1)(2,8)(2,5)(1,2)`; `E` `(0,3)(0,6)(6,9)(1,7)(0,1)(6,7)`. At `tau = 2.0` (`A1`, `C`):
`0.0268 / 0.0268` after one record, `0.353 / 0.347` after six -- same picture, different numbers. `[numerical, 1e-10]` The **leaf-TV** on the formed sites is `<= 7.2e-14` at three
records for every rule, while the full law is already `0.207`-`0.314` away; `A2` and `A2v` stay at `2.6e-14 / 2.1e-14` through six records with full-law `TV 0.389 / 0.409`; `A1`
breaks at the fourth record (`0.152`, and stays there), `A1v` at the fifth (`0.118`), `B`, `E`, `C` only at the sixth (`0.079 / 0.146 / 0.023`). `[numerical, 1e-9]` Rule `E` does not
exist on the slab: the minimum over free sites of the conditioned-state residual is `0.5638 / 0.6358 / 0.6389 / 0.6943 / 0.6829 / 0.7354` at records `1`-`6`, identical across every
branch of a level (spread `<= 1.3e-15`), never `0`, and ending above where it began. Along every rule's path the branch residual is `0.50`-`1.37` and the tick displaces the diagonal by
`0.078`-`0.291`.

**Proof.** The `2^20` record space is touched only on `J` by sparse Pauli strings; the sea comes from Lanczos at the declared start, projected into the code space and polished by
`20` shifted power steps, with `E = -(8 + 2 sqrt 2)` to `0.0e+00` and residual `2.5e-15` when the Rayleigh quotient is reduced exactly (a sequential reduction over `473088` terms is
off by `3.8e-12`, the cancellation trap PR #7902 named; every residual near zero reported here uses an exact or pairwise reduction). The leaf-TV and the full law are two bincounts of the
same propagated vector.

**Reading, not theorem.** A lane that checks a site-wise tick by comparing the records it formed with the sea's odds on those sites will see agreement to `1e-13` for three
records, and for `A2` and `A2v` for all six, while the full record law is a third of the way to somewhere else. Only the full law discriminates.

## Theorem 4 -- what the energy-rate rule does: uniform at the instant, then a matching along the evolution's own spread

**Conclusion.** `[numerical, 1e-12]` On the cube at `tau = 0.5`, `A1` forms `(0,1)(2,3)(4,5)(6,7)` -- the four `z`-edges, a perfect matching, no star -- with contrast
`1.00 / 5.50 / 6.85 / 9.00` and the greedy site carrying `0.083 / 0.500 / 0.685 / 1.000` of the odds at steps `1`-`4`: uniform at step `1` exactly, and the greedy path the process's
dominant path from step `2`. The odds of the first three records are still the sea's own (`margerr 0 / 6e-15 / 1e-15`) and break at the fourth (`0.189`); the branch state is never an
eigenvector (residual `0.58 / 0.85 / 0.84 / 0.45`) and the tick displaces its diagonal by `0.125 / 0.140 / 0.129 / 0.056`. The corner form `A1v` completes `star(0)` and then
`star(4)` site-wise within five records, and its third record -- the one that completes `star(0)` -- leaves residual `0.671`, not `0`, because the two earlier ticks already took the
state off the conditioned sea. `[numerical]` On the slab, `A1` is uniform at step `1` (contrast `1.000000`), then contrast `8.4 / 8.4 / 10.4 / 5.0 / 8.7` with the greedy site at
`0.440 / 0.466 / 0.611 / 0.311 / 0.579` at steps `2`-`6`, forming the four parallel `z`-edges between the two stacked cubes first. The corner energy-scale form `A2v` forms the middle
edges `(1,4)(7,10)(1,7)` first -- the edges of exactly the degree-`4` corners where PR #7902's two-mode condition holds -- and is the **worst** rule by the full law at six records
(`0.4089`, the maximum of `0.373 / 0.212 / 0.389 / 0.409 / 0.343 / 0.317 / 0.316`).

**Proof.** The rates are the declared functions of the branch state, evaluated per node by bincounts of the same products that give the local energies; the stochastic odds are read
off the same rates along the greedy path. Which site the rate selects at `tau = 2.0` differs from the `tau = 0.5` choice (the slab path becomes `(0,1)(4,5)(8,11)(2,5) ...`), so the
order a rate selects is itself a function of `tau`.

**Reading, not theorem.** At the instant the rate sees nothing: the excess energy of a record sits on the recorded edge. With evolution the hop dynamics spreads that excess to the
edge across the pi-flux face and the rate follows it, forming parallel edges rather than stars. Its corner form does complete stars, but one edge at a time, after the state has
already left the sea. The one rate that follows the flat-band corners is the worst of all by the full law: the flat-band structure belongs to the whole star, not to its edges.

## Theorem 5 -- the condition is per step and set-wise; the site-wise dephasing condition is met nowhere computed

**Conclusion.** `[numerical, 1e-12]` **Sufficient condition, proved.** If at every node the conditioned state `P_w|sea>` is an eigenvector of `H_R`, then `exp(-i tau H_R)` is a
phase on it, the branch state stays `P_w|sea>` for every `tau`, and the rule reproduces the sea's registration exactly for every completion. This holds when each formed set is a union
of whole corner stars satisfying the two-mode condition: `P_w = 2^-d sum_T eps_T Z_T` with every `Z_T` commuting with `H_R`, so `P_w|sea>` is an `H_R` eigenvector iff the fermionic
projection is (PR #7902). Rule `D` on the cube is the instance: `TV 6.8e-16 / 3.2e-16 / 1.2e-15` at `tau = 0.5 / 0.1 / 2.0`. `[numerical, 1e-9]` **Set-wise, not site-wise.** The
residual of the sea conditioned on two edges of one star is `0.577350`, on two parallel `z`-edges `1.000000`, on two far edges `0.816497 = sqrt(2/3)`, on a whole star `1.4e-14`, on
three edges not a star `1.290994`, on `A1`'s four-edge matching `1.323435`: for a partial star the logical content of `P_w` is `I` alone and the criterion is never met. Rule `E`'s
best-site residual along its own path at `tau = 0.5` is `0.577 / 0.685 / 0.671 / 0.643 / 0.552 / 0.512 / 0.496` at steps `1`-`7`, and the first branch in which some site leaves an
eigenvector appears at step `9`, with four free edges left, long after the law has left the sea (`E`'s final `TV 0.362828`, `0` of `256` cancellation zeros). `[numerical]` **Necessary
condition, tested.** A branch state that is not an `H_R` eigenvector has an invariant `Z`-diagonal for all `tau` iff the dephasing condition `sum_{k,l : E_k - E_l = Delta} c_k c_l^*
<z|k><l|z> = 0` holds for every `z` and every `Delta != 0`. Over `12` trees (`A1`, the identity order, `A1v`, `B` at `tau = 0.5, 0.1, 2.0`; `5246`-`5822` nodes each) every node with
residual `> 1e-6` has diagonal displacement `> 7.1e-05` (`0` invariant of `27848`; the smallest displacement `7.1e-05` at `tau = 0.1`, `8.2e-04` at `0.5`, `3.6e-03` at `2.0`) and
every node with residual `<= 1e-6` has displacement `< 1e-9` (`0` displaced of `40672`).

**Proof.** The sufficient half is two lines: a phase on the branch state leaves its `Z`-diagonal and therefore every later conditional untouched. The set-wise statement is PR #7902's
factorisation, reproduced by the declared-set residuals. The scan reads each node's residual before its tick and its displacement after it from the same level vectors.

**Reading, not theorem.** A tick preserves the sea's registration when the state it leaves behind after each formation is one the remaining law holds still. No single edge ever
leaves such a state on either object; only a set that is a whole star -- or a union of stars with the right spectral property -- does. That is what a site-wise rule cannot buy: it can
choose the order, and the order is not the issue.

## Theorem 6 -- the positive result: a pair of degree-3 stars is an eigen-set, as a six-record joint tick

**Conclusion.** `[numerical, 1e-11]` With no evolution, rule `E` run on the sea of the slab forms `(0,3)(0,6)(0,1)` and then `(1,2)(2,5)(2,8)` -- `star(0)` and then `star(2)`, the
two degree-`3` stars flanking the degree-`4` corner `1` along `z` -- with best residuals `0.5638 / 0.5210 / 0.2071 / 0.5210 / 0.5638 / 0.0000`. Each star alone leaves
`0.207107 = (sqrt 2 - 1)/2` at all `8` outcomes (PR #7902's failing value), and the **column pair `star(0) u star(2)` restores the exact eigenvector property**: residual `<= 2.1e-15`
at all `64` outcomes. As a **six-record joint tick** at `tau = 0.5` the pair keeps the sea: residual `2.1e-15`, diagonal displacement `<= 4.0e-16`, full-law `TV 3.6e-16` on the
sea's own support `411648`. The **same six sites formed one at a time** with `tau = 0.5` ticks between them (rule `C`, the identity order, is exactly this sequence) leak from the
first record and end at full-law `TV 0.3156`. The degree-`4` sets `D` (`star(4)` then `star(7)`, joint, evolving between) give full-law `TV 2.4e-16 / 3.3e-16` at `4 / 8` records,
residual `<= 3.9e-15`, support `411648`.

**Proof.** One joint formation of the six edges is one relabelling of the level vector into `64` sectors; the residual of each sector's normalised state under `H_R`, the tick, its
displacement and the full law follow as in every other tree. The single-star controls are the same computation on three edges.

**Reading, not theorem.** PR #7902 found that a degree-`3` corner of the slab fails the two-mode condition and nothing at that corner restores it. The pair of degree-`3` stars
stacked along `z` does restore it -- but only as one formation event of six records. The eigenvector condition is about the set formed in one tick, not about which sites are
eventually recorded.

## Corollary -- where the preserving rule lives, and where the next lane is

Within the setting declared above, on the two named clusters, in the staggered sector at half filling, for PR #7876's Model A tick and the rules declared in full here:

1. **No site-wise formation rule preserves the sea's registration under evolution between formations** -- energy-rate, purity, uniform, the declared orders, or the eigenvector-seeking
   rule itself -- on the cube (`TV 0.29`-`0.46`, all `256` cancellation zeros lost, at every declared `tau > 0`) or on the slab (full-law `TV 0.11`-`0.14` after one record, `0.21`-`0.41`
   after six). What a site rule can do is choose an order; the order changes the distance by a factor `1.6` at most and never the support (`T2`, `T3`).
2. **The formation rate is not the missing supplier of the sea's registration; the formation unit is.** The energy-rate rule in the ruler's form is uniform at the instant and, at finite
   `tau`, follows the evolution's own energy spread into a matching -- neither the flat-band order nor a preserving one; its corner form completes stars only after the state has left the
   sea; the one form that follows the flat-band corners is the worst by the full law (`T4`).
3. **The exact condition is per step and set-wise**: the conditioned state must be an `H_R` eigenvector after each formation -- the sufficient condition proved -- which holds when each
   formed set is a union of whole corner stars satisfying the two-mode condition; no single edge site meets it at any step, and the necessary dephasing condition is met by no
   non-eigenvector node in any tree computed (`T5`).
4. **The rule that does preserve the sea therefore exists exactly where PRs #7900 and #7902 said** -- whole corner stars and their eigen-set unions, formed jointly -- **and nowhere a
   site-wise rate can extend it.** It does extend set-wise one step beyond the flat-band corners: the column pair of degree-`3` stars is an eigen-set as a six-record joint tick (`T6`).
5. **The natural next lane** is which unions of stars are eigen-sets on a general cluster. The criterion is the invariance of the occupied one-particle space restricted to the deleted
   vertex set -- the multi-site form of PR #7902's two-mode condition -- and the question is whether every corner of a larger open slab belongs to some eigen-set.

## Reading, not theorem -- the whole thing in plain words

The tick lane hoped that if records picked their own moment -- forming first where the energy sits above the sea -- the sea's own statistics might survive the evolution between
them. They do not. With no evolution every way of picking sites is perfect, so picking sites proves nothing there; with evolution every way of picking sites leaks into the patterns
the sea forbids, from the first tick, and the energy rule just follows the disturbance it is supposed to avoid. What survives is a statement not about which site forms next but about
how many form at once: a whole corner's records forming together leave the sea a state its remaining law holds still, and so, one cube taller, do two stacked corners' records forming
together as one event of six; one record at a time never does.

## Interfaces named for other lanes, not settled here

- **PR #7876 (the tick).** Its no-invariant-state result is reproduced at its representative `tau = 0.5` and extended: no site rule fixes it. Model B is not touched.
- **PR #7895 (the relaxation tick).** `M_R` is a different between-event model, already excluded there; no relaxation tick is run here.
- **PRs #7900 and #7902 (the corner-set condition).** Rule `D` is their unit; `T6` adds one eigen-set on the same cluster and names the multi-site criterion, computed nowhere else.
- **PRs #7916 and #7925 (the rate ruler form).** `A1` and `A1v` are the ruler's rate in edge and corner form on the pre-record state; a rate on the record configuration is not computed.

## Executable claim block

The canonical machine-bound restatement of the six theorem conclusions.

```text
setting: qubits on the EDGE sites of the 2x2x2 cube (12 edges, record space 2^12) and the 2x2x3 slab open in z (20 edges, record space 2^20 on the half-filled sector J, |J| = 473088); ordinary composition; Admissibility and Record quoted verbatim from MINIMAL_AXIOMS_2026-06-29.md with Admissibility reading note (2)
law: eta = Kawamoto-Smit staggered signs, flux -1 on every face; H = -sum_e eta_e T_e, t = 1; sea = the code-space ground state at half filling, E = -4 sqrt 3 (cube, residual 5.4e-15) and -(8 + 2 sqrt 2) (slab, to 0.0e+00, residual 2.5e-15 with an exact reduction); H_R = the hops on the UNRECORDED edges = P_S H P_S
tick_model: STIPULATED, PR #7876 Model A adopted unchanged -- Lueders formation with the Born odds of the pre-record state; exp(-i tau H_R) between formations; tau in {0, 0.1, 0.5, 2.0} (cube) and {0, 0.5, 2.0} (slab)
rules: DECLARED IN FULL -- A1 energy above the sea, A1v its corner form, A2 energy scale, A2v its corner form, B least entangled first, E eigenvector first (greedy paths, odds along the path quantified), C the 24 declared orders (cube) and the identity (slab), D joint corner stars; every tree a complete exact enumeration; no seed
T1_instantaneous [numerical, 1e-12]: tau = 0 -- every rule, D, each of the 24 orders and their average at TV <= 8.2e-17, support 1984, 1856/1856 charge and 256/256 cancellation zeros kept, margerr <= 4.1e-17; A1 exactly uniform at steps 1-5; one edge leaves residual 0.577350 = 1/sqrt 3 at all 12 edges, a whole star 1.4e-14
T2_cube [numerical, 1e-12]: tau = 0.5 -- TV A1 0.337565692 A1v 0.320717027 A2 0.422413255 A2v 0.449953329 B 0.453896665 E 0.362827766, 24 orders 0.289380397 (reverse) to 0.456208220 mean 0.379401338, their average 0.239288631; every site-wise law support 2240 with 0/256 cancellation zeros; D 6.8e-16 with 256/256, node residual <= 1.4e-14. tau = 0.1 -- 0.2603/0.1298/0.0704/0.2679/0.1527/0.1203, orders 0.0459-0.2990, D 3.2e-16; tau = 2.0 -- 0.4691/0.3604/0.4662/0.3263/0.3698/0.4149, orders 0.3272-0.5243, D 1.2e-15; 0/256 cancellation zeros for every site-wise law at both
T3_slab [numerical, 1e-10]: tau = 0.5, six records, full-law TV after one 0.1148/0.1148/0.1259/0.1387/0.1259/0.1259/0.1148 (A1/A1v/A2/A2v/B/E/C, supports 436224-458752 > 411648), after six 0.3727/0.2116/0.3895/0.4089/0.3431/0.3167/0.3156; tau = 2.0 A1/C 0.0268/0.0268 then 0.353/0.347; leaf-TV <= 7.2e-14 at three records for every rule, A2/A2v <= 2.6e-14 through six; rule E's best-site residual 0.5638/0.6358/0.6389/0.6943/0.6829/0.7354, never 0
T4_rate_rule [numerical]: cube A1 forms the z-matching (0,1)(2,3)(4,5)(6,7), contrast 1.00/5.50/6.85/9.00, greedy odds 0.083/0.500/0.685/1.000, margerr <= 6e-15 for three records then 0.189, residual 0.58/0.85/0.84/0.45; A1v completes star(0) then star(4) within five records, its third record leaving 0.671; slab A1 uniform at step 1 then greedy odds 0.440/0.466/0.611 at steps 2-4 on the parallel z-edges (0,1)(3,4)(6,7)(9,10); A2v forms (1,4)(7,10)(1,7) first and is worst at six records, 0.4089
T5_condition [numerical, 1e-9]: sufficient -- an H_R eigenvector after each formation gives exact registration for every tau (D); set-wise -- two edges of one star 0.577350, parallel 1.000000, far 0.816497, star 1.4e-14, three not a star 1.290994, the matching 1.323435; E's best site 0.577/0.685/0.671/0.643/0.552/0.512/0.496 at steps 1-7 with no eigenvector site before step 9; necessary (dephasing), tested -- 12 trees, 5246-5822 nodes: 0 of 27848 non-eigenvector nodes with an invariant diagonal (smallest displacement 7.1e-05 / 8.2e-04 / 3.6e-03 at tau 0.1 / 0.5 / 2.0), 0 of 40672 eigenvector nodes displaced
T6_column_pair [numerical, 1e-11]: at tau = 0 rule E forms star(0) then star(2) with residuals 0.5638/0.5210/0.2071/0.5210/0.5638/0.0000; each star alone 0.207107 = (sqrt 2 - 1)/2; star(0) u star(2) as one six-record tick at tau = 0.5: residual <= 2.1e-15 at 64/64 outcomes, displacement <= 4.0e-16, full-law TV 3.6e-16 on support 411648; the same six sites one at a time with tau = 0.5 ticks: 0.3156; D star(4) then star(7): 2.4e-16 / 3.3e-16 at 4 / 8 records
boundary: greedy paths of the stochastic rules with the exact mixture bounded below by the support argument; 24 declared orders standing in for the uniform-order average; the sufficient condition proved, the dephasing condition shown unmet numerically and not proved impossible; nothing derived from any axiom; no rate, unit or tick foreclosed
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=16 FAIL=0
```

## Proof boundary

Every statement above is proved on **two finite clusters** -- the `2x2x2` cube graph and the `2x2x3` slab open in `z` -- in **one flux sector** (all-minus, the Kawamoto-Smit
staggered signs) at **half filling only**, with `t = 1`, and for **one between-event model**, PR #7876's Model A, at `tau in {0, 0.1, 0.5, 2.0}` on the cube and
`{0, 0.5, 2.0}` on the slab, the slab trees to **six records** (deeper is outside this session's runtime stipulation; the depth is stated wherever a slab figure appears). Nothing is
claimed for other clusters, other sectors, other particle numbers, infinite lattices, or any law family other than the one in "Definitions". The law is **designed**, not derived.

**The stochastic rate rules are walked along their greedy (max-rate) paths**, with the stochastic odds along the path quantified: uniform at step `1` exactly, the greedy site
carrying `0.50`-`1.00` (cube) and `0.44`-`0.61` (slab) of the odds at steps `2`-`4`. The exact stochastic mixture is bounded below by the **support argument**: every tree computed has
support `2240` on the cube, mixing only enlarges support, and the sea's is `1984`. The **24 declared orders stand in for the uniform-order average**; their average is the closest
object found and is not the sea. **Not covered:** rates that depend on the record configuration rather than on the pre-record state; joint formation of sets other than corner stars
and the one star pair of `T6`; any interacting or non-flat `H`; the relaxation tick of PR #7895.

**What is proved and what is tested.** The eigenvector condition per step is the **sufficient** condition, proved. The **necessary** half -- the dephasing condition on a
non-eigenvector branch state -- is shown numerically never to be met off the eigenvector case on these two objects (`0` of `27848` nodes) and is **not proved impossible**. `T6` is a
value on one declared set of one cluster; the multi-site criterion is named and not computed elsewhere.

**The tick, the formation, the rates and the orders are stipulated reconstructions**, adopted or declared here and supplied by no axiom; reading note (2) says the axioms supply no
formation site, probability or rate, and they supply no unit either. This note supplies none, adds none, and amends none. Every line not tagged `[exact]` is a deterministic
double-precision evaluation at the stated threshold; the `2^20` object is touched by sparse Pauli strings, Lanczos and a Chebyshev propagator only, no dense object above `4096 x 4096`
is formed, peak memory stays under `1 GB`, and there is **no seed anywhere**. The one floating-point trap met -- a sequential Rayleigh quotient over `473088` terms carrying a `3.8e-12`
floor, its variance form negative -- is named in `T3` and avoided by exact and pairwise reductions wherever a residual near zero is reported. No absolute unit appears anywhere, no
axiom text is amended, extended, reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

**Honest-auditor read.** An honest auditor should come away with a bounded negative and one bounded positive, both on declared finite sets: no site-wise formation rule -- rate,
purity, uniform, declared order, or the eigenvector-seeking rule itself -- reproduces the sea's registration under Model A evolution on either cluster, while the set-wise rule of PRs
#7900 and #7902 does, and extends by exactly one further eigen-set found here. The tick, the rules and the orders are declared as stipulations in the front matter, the setting, the
claim block and the proof boundary alike; nothing is presented as following from an axiom; no rate, unit or tick is foreclosed. The disagreements with the expectation this probe was
run under are stated plainly: rate selection at `tau -> 0` is exact for every rule and so says nothing about rates; the rule that "forms first where the two-mode condition holds"
exists (`A2v`) and is the worst of all by the full law; the leaf statistics on the formed sites are blind for three to six records; the closest object on the cube is the average over
orders, not any rate rule; and against PR #7902's reading that nothing restores the property at a failing degree-`3` corner, the column pair of degree-`3` stars does -- as a six-record
joint tick, never site-wise.

Departures from the scratch computation this note lands, stated here. The scratch sea on the slab carried a residual of `6.0e-12`, its conditioned eigen-sets `1.4e-13` and its `D`
figures `8e-14`; those were the floors of sequential reductions over `473088` terms, and with exact and pairwise reductions the same vectors give `2.5e-15`, `2.1e-15` and `3.9e-15`
-- the numbers reported here, and the reason `T3` names the trap. The propagator is a Chebyshev series under a rigorous norm bound rather than the scratch's dense eigendecomposition
(cube) and `expm_multiply` (slab); it agrees with `expm_multiply` to `1e-16` and every cube distance agrees with the scratch to nine digits, every slab distance to four. The scratch's
statement that rule `E`'s best-site residual on the cube is "never `0`" is refined: it is `>= 0.496` for seven steps and an eigenvector site first appears at step `9`, with four free
edges left; the scratch's "greedy site carrying `44`-`100 %` of the odds" is separated by object, `0.50`-`1.00` on the cube and `0.44`-`0.61` on the slab at steps `2`-`4`. Node
counts in the `T5` scan differ from the scratch's by the pruning convention (`5246`-`5822` against `5263`-`5863`); the verdict, `0` invariant non-eigenvector nodes and `0` displaced
eigenvector nodes, is the same.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority" pointers are plain
text carrying no grade and no weight, each with its PR state at the time of writing (all five parents are open PRs, none on main). Hard landing conditions are a fresh runner and cache
pair at `PASS=16 FAIL=0`, runtime under the declared `180` seconds, and passing pipeline, strict-lint and changed-evidence gates; audit remains a separate lane, and the ledger has
been unaudited since 2026-08-07.
