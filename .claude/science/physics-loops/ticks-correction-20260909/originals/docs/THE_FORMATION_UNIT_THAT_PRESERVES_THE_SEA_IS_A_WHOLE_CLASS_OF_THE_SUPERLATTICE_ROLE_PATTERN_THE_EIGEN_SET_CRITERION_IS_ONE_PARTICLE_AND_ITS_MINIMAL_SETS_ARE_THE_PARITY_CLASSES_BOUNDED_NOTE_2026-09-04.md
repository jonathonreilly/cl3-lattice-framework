---
claim_id: formation_unit_preserving_the_sea_is_a_whole_superlattice_class_2026_09_04
claim_type: bounded_theorem
claim_scope: "On finite subgraphs of the cubic lattice with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, in the staggered (pi-flux) Kawamoto-Smit sector H = -sum_e eta_e T_e, t = 1, at half filling -- the open boxes 2x2xL (L = 3..8), 2x3x3, 2x3x4, 2x3x5, 2x3x6, 3x3x3, 3x3x4, 4x4x4 and the periodic tori 4^3, 6^3, 4x4x6, 8^3 in their declared twist sectors -- for the STIPULATED tick of PR #7876 Model A (Lueders formation with the Born odds of the pre-record state; exp(-i tau H_R) between formations, H_R the hop terms on the unrecorded edges) and the DECLARED formation unit of a joint corner set: (T1) a vertex set S with closure S' is an eigen-set -- P_w|sea> an H_R eigenvector at every outcome -- iff the occupied space orthogonal to the occupied corners, restricted to the unrecorded corners, is h_R-invariant pattern by pattern; on the 2x2x2 cube the many-body residual, eigenvalue and outcome odds equal the one-particle Frobenius residual, trace and 2^-(|R|-|S'|) times the determinantal law over ALL 255 vertex sets and every outcome to 1.44e-14 / 1.51e-14 / 4.4e-16, and on a declared 107-set family of the 2x2x3 slab on its 2^20 record space to 2.93e-13 / 2.00e-12 / 3.4e-14; irregular sets, where the one-particle test is only sufficient, are many-body non-eigen wherever tested (6 of 255 on the cube at residual 0.7071, all 21 smallest ones on the slab at >= 0.827). (T2) With flux -1 on every face h^2 = D + T2 exactly, T2 the straight-two-step graph (residual 0.0 on every cluster below except the 4^3 ground sector, where h^2 = 6I); the single-sublattice eigen-sets are exactly the unions of T2 components -- the parity classes, the cosets of 2Z^3 -- the minimal ones are the classes, and the mixed eigen-sets are non-adjacent cross unions or closures of class unions (complete over all 4095 slab sets: 20 of 80 single-sublattice closures, 33 eigen closures, 132 adjacent class-union closures failing, nothing else). (T3) Complete enumeration of every union of up to three corner stars on thirteen clusters finds only class unions and non-adjacent cross unions and none at all on 2x2x8, the 4x4x4 open box, the 6^3 torus or the 8^3 torus; every class is an eigen-set to 1e-13 and every tested proper subset fails at 0.15-0.83, as do a plaquette of stars, a coarse cell, a coarse line, a coarse plane and a class minus one corner. (T4) The even (or the odd) classes partition the record sites, every proper prefix closure of every order is an eigen-set, and under the unitary tick with evolution the final record law is the sea's: 96 cube trees at TV <= 1.2e-15 with all 256 cancellation zeros kept and 48 slab trees at full-law TV <= 6.7e-16 on the sea's support 411648, while controls fail exactly where a prefix closure fails. (T5) Eigen-sets exist on the tori too -- the classes -- with the ground twist sectors as declared (4^3 flat in (1,1,1); 6^3 periodic and gapped at 3.464 with classes of 27; 4x4x6 in (1,1,0); 8^3 in (1,1,1) with classes of 64), and the periodic 4^3 and 8^3 sectors carry 8 zero modes and no sea. The tick and the formation unit are stipulated reconstructions supplied by no axiom; no rate, unit or tick is foreclosed. No seeds anywhere."
upstream_dependencies: []
runner: scripts/formation_unit_preserving_the_sea_is_a_whole_superlattice_class_check_2026_09_04.py
---

# The formation unit that preserves the sea is a whole class of the superlattice role pattern; the eigen-set criterion is one-particle and its minimal sets are the parity classes

**Date:** 2026-09-04
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/formation_unit_preserving_the_sea_is_a_whole_superlattice_class_check_2026_09_04.py`](../scripts/formation_unit_preserving_the_sea_is_a_whole_superlattice_class_check_2026_09_04.py)
**Runner cache:**
[`logs/runner-cache/formation_unit_preserving_the_sea_is_a_whole_superlattice_class_check_2026_09_04.txt`](../logs/runner-cache/formation_unit_preserving_the_sea_is_a_whole_superlattice_class_check_2026_09_04.txt)
**Parents:** none. Every premise used below is declared in this note.

`NO_SITE_WISE_FORMATION_RULE_PRESERVES_THE_SEA_..._2026-09-03.md` (open PR #7947) found that the rule which preserves the sea's registration under a tick with evolution is set-wise, not
site-wise, and left one question open: which unions of corner stars are eigen-sets on a general cluster, and whether every corner belongs to one. This note answers both. The criterion is a
one-particle statement, exact rather than approximate, and its minimal solutions are the parity classes of the corner lattice -- the cosets of `2Z^3`, the classes of the superlattice role
pattern of PR #7939. One joint-formation rule preserves the sea's registration on every cluster computed: *form together all records incident to a whole class.* That rule is not local. On
any box with all sides at least `3` a class is about an eighth of all corners, on the `6^3` torus `27` corners and `162` records, on the `8^3` torus `64` corners and `384` records, and on
the lattice itself an infinite set. Local units survive only where the one-particle spectrum is flat -- the `2x2x2` cube, and the `4^3` torus in its ground twist sector through an `L = 4`
cancellation.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on thirteen open boxes and four periodic tori in the staggered sector at half filling, for the stipulated tick of PR #7876 Model A and for a formation unit declared in full here. The one-particle criterion is V x V linear algebra with 2^|S'| patterns per set and is evaluated completely where declared; the many-body certification is a complete enumeration of the 2x2x2 cube's 255 vertex sets on its whole 2^12 record space and a declared 107-set family of the 2x2x3 slab on the 2^20 record space held on its half-filling index set, |J| = 473088. Every tree is a complete exact enumeration in the unnormalised-branch form, so the final laws, per-node residuals and per-node diagonal displacements are deterministic double-precision evaluations of exactly specified quantities; the propagator is a Chebyshev series under the rigorous bound ||H_R|| <= number of free edges. The setting checks are exact symplectic Pauli and F2 arithmetic. Nothing is sampled, there is no seed anywhere in the runner, every cluster, set, pattern, order and schedule is enumerated or written out, and no dense object above 4096 x 4096 is formed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Carry the class unit into the Born lane as the object to compute: the menus a class-wise tick presents, and whether the outcome odds of a whole class -- the determinantal law of its corner occupations dressed by the uniform gauge factor 2^-(|R|-|S'|) -- meet the abundance condition of PRs #7919 and #7926 that a Born form requires. Report the full record law, never the leaf statistics."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five theorems and the corollary below, exactly the runner's check groups: the cube's setting (`A1`), Theorem 1 on the cube (`A2`), Theorem 2 on the cube
(`A3`), Theorem 4 on the cube (`A4`-`A5`), the slab's setting with Theorem 1 (`B1`), Theorem 2 complete on the slab (`B2`), Theorem 4 on the slab (`B3`), Theorem 3 on the open boxes
(`C1`-`C3`), Theorem 4's coverage and order independence (`C4`), Theorem 5 on the tori (`D1`-`D4`) and the timing (`E1`). `A1` and `B1` carry **exact** content: the encoding relations
`R0`-`R4` in symplectic Pauli arithmetic with phases mod `4`, the face group, the flux sector and the cluster combinatorics. Everything else is a **deterministic double-precision
evaluation** of an exactly specified quantity at the stated threshold. Nothing is sampled: the Lanczos start on the slab is the fixed vector `cos(0.7 i + 0.3) + i cos(1.3 i + 1.1)` projected
into the code space, written out in the runner, and every cluster, set, pattern and order is written out there too. There is **no seed anywhere**.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggered signs, Lueders conditioning, Slater determinants and their quadratic
Hamiltonians, determinantal point processes, Lanczos, the Jacobi-Anger expansion of the propagator and the total-variation distance are standard methodology; every object is redeclared here
and the runner recomputes every statement, the encoding's relations included. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers,
carrying no grade and no weight, with each one's state at the time of writing: `NO_SITE_WISE_FORMATION_RULE_PRESERVES_THE_SEA_UNDER_TICK_EVOLUTION_..._2026-09-03.md` (**open PR #7947, not on
main** -- the per-step set-wise condition and the question this note answers); `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7876** -- the
tick, Model A, its representative `tau = 0.5`); `JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_UNDER_THE_UNITARY_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7900** --
the corner-set unit, and the one non-star unit on record, a face, which fails);
`THE_CORNER_EIGENVECTOR_PROPERTY_IS_A_TWO_MODE_SPECTRAL_CONDITION_EXACT_ON_FLAT_BANDS_NOT_GENERAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7902** -- the single-corner two-mode
condition that Theorem 1 generalises); `A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7895** -- the restriction
identity `P_S H P_S = H_R`, and a different between-event model, not run here);
`THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md` (**open PR #7939** -- the superlattice
role pattern whose classes turn out to be the minimal units here); `RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (**open PR #7883**
-- the determinantal record statistics that reappear as the outcome odds); and `MINIMAL_AXIOMS_2026-06-29.md` (on main), from which the axiom text in "Setting" is quoted verbatim.
This note cites no grade of any and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. Lattice / Physical Locality and Qubit / Site Possibility are used only through the graph structure of the clusters and the `M_2(C)` site
algebra. **Record / Fixed Reality**, verbatim: *"Records form."* *"When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records
are permanent."* *"Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."* **Admissibility / Local Constraint** reading note
(2), interpretive and non-governing, is quoted with it because it is what makes the unit below a free choice: *"Read with Record, the distribution concerns which possibility a forming record
locks, conditional on formation at that site; it does not supply the formation site, probability, or rate."* The axioms therefore supply no formation **unit** either; every unit below is
declared, and nothing below follows from an axiom.

Composition is **ordinary**: the algebra of a region is the tensor product of its sites' algebras and operators on disjoint regions commute. A record at an edge site **registers** a
`Z`-value there; it does not report one the site already carried. The **tick** is PR #7876's Model A, adopted unchanged: a forming record locks its value by Lueders conditioning with the
Born odds of the current pre-record state, and between formations the pre-record state runs by `exp(-i tau H_R)`, `H_R` the sum of the hop terms on the unrecorded edges, which is exactly
`P_S H P_S` on the record sector because every hop's Pauli `X`-part is one edge qubit.

**Reading, not theorem.** The cluster, the encoding, the staggered sector, half filling, the tick and the formation unit are stipulated reconstructions of what would be registered. Nothing
here is presented as following from an axiom, and no unit is foreclosed; this note reports which units keep the sea's registration and which do not.

## Definitions

A **cluster** is a finite subgraph `G = (V, E)` of the cubic lattice: corners `V`, edge sites `E`, one qubit per edge site, corner `(x, y, z)` indexed `(x L_y + y) L_z + z`. The encoding is
Bravyi-Kitaev superfast: `A_ij`, `B_v = ` the product of `Z` over `star(v)`, face stabilisers `S_f`, corner parity dictionary `n_v = (1 - B_v)/2`. The signs are Kawamoto-Smit staggered,
`eta_x = 1`, `eta_y = (-1)^x`, `eta_z = (-1)^(x+y)`, giving **flux `-1` on every face** of every cluster here, the wrap-around faces of the tori included; `H = -sum_e eta_e T_e` with `t = 1`
and one-particle matrix `h_ij = -eta_ij`. The **sea** is the code-space ground state at half filling, the Slater determinant of the `N` lowest `h`-modes with `W` their span, `N = V/2`
rounded up to the even value the code space allows when `V` is odd. For a corner set `S`, **`R(S)`** is the union of the stars of its corners -- the records formed jointly -- and **`H_R`**
is the hopping Hamiltonian of `G[V \ S]`. The **closure** `S' = {u : star(u) subset R(S)}` is the set of corners whose occupation the outcome on `R(S)` fixes. A set is **regular** when the
`Z`-strings inside `R(S)` that commute with every face stabiliser have `F2` rank `|S'|` (`|S'| - 1` when `S' = V`), equivalently when the unrecorded graph `G[V \ S']` is connected. `S` is an
**eigen-set** iff `P_w|sea>` is an `H_R` eigenvector for every outcome `w` of nonzero odds. **`T2`** is the **straight-two-step graph** `u ~ u +- 2 e_a` on the corners; **superlattice role
pattern** means the eight-class partition of the corners by `(x, y, z) mod 2`, the cosets of `2Z^3`, and a **class** is one of those cosets. The **residual** of a vector under `M` is `||M
psi - <M> psi|| / ||psi||`; **TV** is total variation; the **full law** is the distribution on all `2^|E|` record patterns after every edge has formed. The cube's **zeros** are `2112`:
`1856` charge zeros (patterns with `N != 4`) and `256` cancellation zeros (the eight closed corner stars times `32`).

## Theorem 1 -- the eigen-set criterion is one-particle, and it is exact

**Conclusion.** Let `S` have closure `S'` and let `S' = S1 u S0` be a corner-occupation pattern (`S1` occupied, `S0` empty). Put `U_{S1} = R_{V \ S'}( W ∩ e_{S1}^perp )` and `h_R = h[V \ S',
V \ S']`. Then for a **regular** set, `P_w|sea>` is an `H_R` eigenvector at every outcome iff `h_R U_{S1}` lies in `U_{S1}` for every pattern of nonzero odds; a pattern has nonzero odds iff
`dim U_{S1} = N - |S1|`; the many-body eigen-residual of the outcome is **exactly** `||(I - P_U) h_R U||_F` for an orthonormal basis `U`, its `<H_R>` is `Tr(U^+ h_R U)`, and its odds are
`2^-(|R| - |S'|) p(n_{S'})` with `p` the determinantal law `p(n) = det( diag(n) K_{S'S'} + diag(1 - n)(I - K_{S'S'}) )`, `K = P_W`. `[numerical, 1e-13]` On the `2x2x2` cube this is certified
over **all `255` vertex sets and every outcome of each**: on the `249` regular sets the many-body residual, eigenvalue and odds agree with the one-particle Frobenius residual, trace and
dressed determinantal law to `1.44e-14`, `1.51e-14` and `4.4e-16`; there are `75` eigen-sets. `[numerical, 1e-12]` On the `2x2x3` slab, whose `2^20` record space is held on the half-filling
index set `|J| = 473088` (sea `E = -10.828427124746 = -(8 + 2 sqrt 2)`, residual `2.5e-15`, support `411648`), the same agreement holds on a declared `107`-set family -- all `12` singletons,
all `66` pairs, all `21` irregular sets of size `4`, and eight declared larger sets -- to `2.93e-13`, `2.00e-12` and `3.4e-14`, each worst case attained at `|S'| <= 8` and sitting at the
double-precision floor of a `473088`-term reduction.

**Proof sketch.** Two steps. *Records.* `P_w = 2^-|R| sum_{T subset R} eps_T Z_T`; a `Z_T` commutes with every face stabiliser exactly when `|T ∩ f|` is even for every face, and for a
regular set those `T` form the group generated by the `B_v = Z_{star(v)}`, `v in S'`. Grouping the `2^|R|` subsets into the `2^(|R| - |S'|)` cosets of that group and using `eps_{T Δ star(A)}
= eps_T prod_{v in A} b_v` gives `P_w|sea> = 2^-(|R| - |S'|) [ sum over coset representatives T0 of eps_{T0} Z_{T0} ] Pi_{n_{S'}}|sea>` with `Pi_{n_{S'}} = prod_{v in S'} (1 + b_v B_v)/2`.
The coset terms sit in mutually orthogonal syndrome sectors, every `Z_T` with `T subset R` commutes with `H_R` (its `X`-parts are unrecorded edges) and is unitary; so `P_w|sea>` is an
eigenvector iff `Pi_{n_{S'}}|sea>` is, with the same eigenvalue and residual, and `2^-(|R| - |S'|)` is the uniform gauge factor in the odds. *Fermions.* Projecting a Slater determinant of
`W` onto "`S1` occupied" leaves, on the remaining modes, the Slater determinant of `W ∩ e_{S1}^perp`, and onto "`S0` empty" the restriction to `V \ S'`; so `Pi_{n_{S'}}|sea> = |n_{S'}> (x)
Slater(U_{S1})`, nonzero iff `dim U_{S1} = N - |S1|`, with squared norm the determinantal law. For a quadratic Hamiltonian, `H_R Slater(U) = Tr(U^+ h_R U) Slater(U) + sum_k |U with u_k -> (I - P_U)
h_R u_k>` and the correction terms are mutually orthogonal, so `Slater(U)` is an eigenvector iff `h_R U` lies in `U`, with residual `||(I - P_U) h_R U||_F`. On an **irregular** set
the outcome also fixes the particle parity of each unrecorded component; those parity projectors commute with `H_R`, so the one-particle test is **sufficient** there and not necessary.

**Where the sufficient-only direction could bite, it does not.** `[numerical, 1e-9]` All `6` irregular sets of the cube are many-body non-eigen at residual `0.7071`, and all `21` smallest
irregular sets of the slab (the size-`4` ones; `547` of the slab's `4095` sets are irregular) are many-body non-eigen at `>= 0.827`. No verdict below rests on the sufficient direction.

**Reading, not theorem.** PR #7902's single-corner two-mode condition was reported as an agreement to three digits. With the closure and the regularity condition respected and the gauge
factor written out, the same computation is exact to the sea's own residual, outcome by outcome, on every set of a whole cluster.

## Theorem 2 -- `h^2 = D + T2` splits the corners into classes, and the eigen-sets are unions of them

**Conclusion.** `[exact]` With flux `-1` on every face the two two-step paths to a diagonal neighbour cancel and a straight two-step has a single path of product `+1`, so `h^2 = D + T2` with
`T2` the straight-two-step adjacency: on every cluster below except the `4^3` ground sector, `h^2 - D - T2 = 0.0e+00` exactly, `T2` equals the geometric straight-two-step graph and all its
entries are `+1`. On a side of length `4` with an antiperiodic twist the two straight two-steps `u -> u +- 2 e_a` reach the same corner with opposite signs and cancel, so that direction
leaves `T2`; on the `4^3` torus in its ground sector all three do and `h^2 = 6I` exactly. `[numerical, 1e-13]` For `S'` inside one sublattice the Krylov space `E + hE` closes at `2|S'|` iff
no `T2` edge leaves `S'` iff `S'` is a union of `T2` components, and then every mixed pattern follows with a pattern-independent eigenvalue. So the **single-sublattice eigen-sets are exactly
the unions of parity classes and the minimal ones are the classes**. Complete over all `4095` vertex sets of the slab (`2375` distinct closures, `33` of them eigen): of the `80`
single-sublattice closures exactly `20` are eigen-sets and exactly the same `20` are class unions -- eigen if and only if a class union, set by set -- and the minimal eigen-sets are the
eight `T2` components `{0,2}, {1}, {3,5}, {4}, {6,8}, {7}, {9,11}, {10}`. Every one of the `33` eigen closures has its even part and its odd part a class union; the `13` mixed ones are `4`
non-adjacent cross unions and `9` closures of a class union, with none of any other shape, and the `132` class-union closures that are **not** eigen-sets are all adjacent. On the cube, which
is flat, all `30` single-sublattice sets are eigen-sets, `45` of the `225` mixed sets are, the size-`2` mixed eigen-sets are exactly the four antipodal pairs with all twelve adjacent pairs
failing, and the size-`4` ones are exactly the eight closed corner stars.

**Reading, not theorem.** The obstruction has a name. A corner's site vector lives in `dim Krylov_h(e_v)` one-particle modes; that number is `2` -- PR #7902's condition -- only where the
corner's class is a singleton, and it grows with the class. What fails when a smaller unit is tried is always the same thing: a straight two-step leaves the set, so the Krylov space exceeds
`2|S|` and the empty or the full pattern is not an eigenvector. Adding stars repairs it only when the union closes under `T2`, that is, only when it is a whole class.

## Theorem 3 -- on growing clusters the eigen-sets are class unions, and below a class there is nothing

**Conclusion.** `[numerical, 1e-13]` Complete enumeration of **every union of up to three corner stars** (closure, then the Krylov screen `rank[e_S, h e_S, h^2 e_S] <= 2|S|`, then the full
per-pattern criterion on every set that passes). On `2x2xL`, `L = 3..8`: of `298 / 696 / 1350 / 2324 / 3682 / 5488` sets, `22 / 8 / 8 / 8 / 4 / 0` are eigen-sets -- `22` on `2x2x3` (eighteen
class unions and four non-adjacent cross unions), then exactly the `z`-columns, and **none at all** on `2x2x8`. On `2x3x3`, `2x3x4`, `2x3x5`, `2x3x6`, `3x3x3` and `3x3x4`: of `987 / 2324 /
4525 / 7806 / 3303 / 7806` sets, `10 / 4 / 4 / 4 / 4 / 2`, each one a class union or a non-adjacent cross union and none of any other shape. On the `4x4x4` open box, whose classes are
`2x2x2` coarse cubes of eight corners, **not one** of the `43744` sets is an eigen-set and none even passes the screen. On every one of these thirteen clusters each of the eight classes
**is** an eigen-set over all its patterns (`<= 1.0e-14`), and every proper subset of every class of size `<= 8` fails: smallest residual `0.178` on `2x2xL`, `0.152` on the `2x3xL` and
`3x3xL` boxes, `0.275` on `4x4x4`, and on the `4x4x4` box every corner sees `8` modes at residual `0.27`-`0.36`. The declared larger units fail on `4x4x4` -- plaquette of four stars `0.996`,
coarse cell of eight `1.430`, coarse line `0.388`, coarse plane `0.366`, class minus one corner `0.358` -- while two whole classes are exact at `1.3e-14`.

**Reading, not theorem.** The minimal eigen-set containing a corner is its whole class: on `2x2x8` a column of four corners, on `3x3x3` the eight outer corners together, on the `4x4x4` box a
coarse cube of eight. Three stars never suffice past the short columns of `2x2xL` and `2x3x3`.

## Theorem 4 -- the classes cover the record sites, in any order, and the tick then keeps the sea's law

**Conclusion.** `[numerical, 1e-12]` On every one of the thirteen open boxes the even classes -- and equally the odd -- partition the record sites: every edge site lies in exactly one
class's star-union and every corner in exactly one class. Every proper prefix closure of all `24` orders of the four even classes is itself an eigen-set (`182` distinct prefix closures of
sizes `1` to `32` over the thirteen boxes, max residual `2.0e-13`), so the classes may form in any order. `[numerical, 1e-13]` With the tick and its evolution, on the cube: `96` trees -- all
`24` orders of the four even classes and of the four odd, at `tau = 0.5` and `tau = 2.0` -- end at `TV <= 1.2e-15` from the sea's law, on the sea's own support `1984`, with all `256`
cancellation zeros and all `1856` charge zeros kept, node residual `<= 1.6e-14` and diagonal displacement `<= 1.8e-15`; the two six-record pair schedules are exact at `<= 5.7e-16`. On the
slab, all `48` orders of the four even and of the four odd classes at `tau = 0.5` end at full-law `TV <= 6.7e-16` on the sea's support `411648`, node residual `<= 4.4e-14`, displacement `<=
2.4e-15`, and the identity order at `tau = 2.0` at `<= 6.7e-16`. `[numerical]` Controls fail exactly at the levels whose prefix closure fails the criterion. Cube: antipodal pairs `TV 0.106 /
0.299` -- the first pair is an eigen-set at `1e-15` but the prefix union `{0,1,6,7}` is irregular and not one, `0.707`; adjacent pairs `0.229 / 0.319` (first prefix `0.500`); the two faces
`0.102 / 0.024` (`0.662`); one corner at a time `0.247 / 0.324`; while the closed star `{0,1,2,4}` then its antipode `{7}`, a sequence of eigen-sets, is exact at `2.8e-16 / 4.2e-16`. Slab,
at `tau = 0.5`: a degree-`3` star alone then the rest `0.0203` on support `428032`, its own residual `0.2071`; the `z = 0` plaquette of stars `0.139`; the coarse cell `0.081`; the adjacent
pair `{0,1}` `0.299` on support `455680` -- prefix residuals `0.21`-`0.75` -- while all six even corners in one tick give `0.0`.

## Theorem 5 -- on the tori the classes are still the units, and the flat case is an `L = 4` accident

**Conclusion.** `[numerical, 1e-9]` All eight twist sectors of each torus, `N = V/2`, flux `-1` on every face including the wrap-around ones. The `4^3` ground sector is `(1,1,1)`, `E =
-78.384 = -32 sqrt 6`, gap `4.899`; its periodic sector has gap `0` with `8` zero modes and no sea. The `6^3` ground sector is the **periodic** one `(0,0,0)`, `E = -258.858`, gap `3.464`, no
zero modes; its all-antiperiodic sector has `8` zero modes. The `4x4x6` ground sector is `(1,1,0)`, gap `4.472`. The `8^3` ground sector is `(1,1,1)`, gap `2.651`; its periodic sector has
`8` zero modes and no sea. `[numerical, 1e-13]` **`4^3`, ground sector:** `h^2 = 6I` and `T2 = 0` exactly, so every corner is its own class; over the complete enumeration of all `2080`
unions of one or two stars, all `64` single corners are eigen-sets and, of the `2016` pairs, exactly the `992` same-sublattice and the `832` non-adjacent cross ones are, with all `192`
adjacent pairs failing; the coarse line, plane, whole class, class minus one corner and two classes are all eigen-sets (`<= 1.8e-14`) while the adjacent plaquette and coarse cell fail at
`1.33` and `2.07`. **`6^3`, ground sector:** `T2` is the straight-two-step graph (`648` edges) and its components are the `8` classes of `27` corners, `162` records each; of the `179804`
unions of up to three stars -- every such set modulo the `27` even translations -- **not one** passes the screen, while the classes are eigen-sets at `<= 5.1e-14` over `114` declared
patterns and the declared proper subsets fail at `>= 0.357`; a corner sees `8` modes at residual `0.3572`; plaquette `1.302`, coarse cell `1.903`, coarse line `0.507`, coarse plane `0.622`,
class minus one `0.357`, two whole classes exact at `4.0e-14`. **`8^3`, ground sector:** `T2` is the straight-two-step graph (`1536` edges) with `8` classes of `64` corners, `384` records
each; the class of corner `0` is an eigen-set at `1.1e-13` over a declared eight-pattern family, its declared proper subsets fail at `>= 0.380`, and of the `512` single corners not one
passes the screen (corner `0`: `8` modes, residual `0.3798`). **`4x4x6`, ground sector:** the two `L = 4` directions are antiperiodic so their straight two-steps cancel and `T2` keeps only
the `z` edges -- `32` components, the `z`-columns of three corners, `18` records each -- and of all `147536` unions of up to three stars exactly `32` are eigen-sets, exactly those columns
(`<= 2.8e-14`); the whole class of `12` is an eigen-set at `2.5e-14` over all `4096` patterns and the class minus one corner fails at `0.1975`; plaquette `1.390`, coarse cell `2.119`, coarse
line `0.279`, coarse plane `0.395`.

**Reading, not theorem.** On a torus with no boundary and no flat band the eigen-sets are whole classes -- an eighth of all the corners at once. The `4^3` case where single corners suffice
is a length accident: on `L = 4`, `u + 2 e_a` and `u - 2 e_a` are the same corner, and with that direction antiperiodic the two paths cancel. It is not a property of the lattice.

## Corollary -- one joint-formation rule preserves the sea's registration everywhere, and it is not local

Within the setting declared above, on the clusters and sectors named in the proof boundary, for PR #7876's Model A tick:

**The rule.** *Form together all records incident to a whole class of the superlattice role pattern -- one coset of `2Z^3` in the corner lattice -- in any order, with the Born odds of the
pre-record state at each formation.* The even classes (or, equally, the odd) partition the record sites, so the rule is a cover: every record site lies in exactly one unit and every corner
in exactly one class. Under it the conditioned state is an `H_R` eigenvector after every formation, `exp(-i tau H_R)` is a phase on it for every `tau`, and the final record law is the sea's
Born law, with each formation's outcome odds the determinantal law of that class's corner occupations dressed by the uniform factor `2^-(|R| - |S'|)`.

**It is not local.** A class is about `V/8` corners on any box with all sides at least `3`; `27` corners and `162` records on the `6^3` torus, `64` corners and `384` records on the `8^3`
torus, and an infinite set on the lattice itself. A single-corner unit works only where `h^2` is a multiple of the identity: the `2x2x2` cube, and the `4^3` torus in its ground twist sector
-- and the latter through the `L = 4` cancellation `+2 = -2 mod 4`, not through any property of the lattice. On every other cluster computed, three stars, a plaquette of stars, a coarse
cell, a coarse line, a coarse plane and a class minus one corner all fail.

**So the tick's open content splits into two readings**, and this note does not choose between them. Either formation is non-local at the level of the vacuum -- the unit in which the sea's
records lock is an extensive set of sites, whatever that would mean for a nearest-neighbour reading of Admissibility -- or the sea is not what survives local formation, in which case the
physical record statistics are the ones a local unit actually produces, and PR #7947's distances (`TV 0.29`-`0.46` on the cube, `0.11`-`0.41` on the slab) are those statistics rather than an
error to be repaired. The axioms decide neither: reading note (2) supplies no formation site, probability or rate, and Admissibility supplies no formation unit.

## Reading, not theorem -- the whole thing in plain words

Ask which records have to lock at the same instant for the vacuum's own statistics to survive the time between one locking and the next. The answer is not "the records around one corner",
except on two small objects where the hopping problem happens to be degenerate. It is "all the records around one of the eight interleaved sub-lattices of corners" -- every other corner in
every direction, all at once, everywhere in the cluster at the same instant. That set is a whole class of the same eight-fold pattern of roles that showed up in the law lane, and there is
nothing smaller inside it: take one corner away and the sea is disturbed by about a fifth. The disturbance always has the same cause, and it is visible one particle at a time: hop twice in a
straight line from a corner of the set and you land outside it, and the state the remaining law would have to hold still is not held still. Two hops in a straight line reach a corner two
steps away, so the unit is forced to be spaced two steps apart in every direction, and a set spaced two apart in a finite box is an eighth of the box. Whether that says formation is
non-local, or says the vacuum is not what a local formation rule produces, is exactly what the axioms leave open.

## Interfaces named for other lanes, not settled here

- **PR #7947 (T1, the parent question).** Its set-wise per-step condition is reproduced and made exact and complete: the criterion is one-particle, its minimal solutions
  are the parity classes, and its column pair of degree-`3` stars on the slab is the class `{0,2}`.
- **PRs #7900 and #7902 (the corner-set and two-mode conditions).** The two-mode condition is the `|S'| = 1` case of Theorem 1, and it holds exactly where the corner's
  class is a singleton. PR #7900's face, the one non-star unit on record, remains the one non-star unit tested, and it fails.
- **PR #7876 (the tick).** Its no-invariant-state result concerns site-wise ticks. For the class-wise tick the pre-record state is invariant at every step; the invariant
  unit is not local. Model B is not touched.
- **PR #7895 (the relaxation tick).** A different between-event model; no relaxation tick is run here.
- **PR #7939 (the superlattice role pattern).** Its eight classes are exactly the minimal formation units found here, arrived at from the sea's spectrum rather than from a
  support rule over roles.
- **PR #7883 (the determinantal record statistics).** The outcome odds of a class are that determinantal law on the class's corner occupations, times `2^-(|R| - |S'|)`.
- **PRs #7919, #7926 and #7950 (the Born line).** The class tick presents a menu of `2^|S'|` joint outcomes per formation event rather than a two-outcome menu per site;
  whether those menus meet the abundance condition a Born form needs is the next question, and it is not computed here.

## Executable claim block

The canonical machine-bound restatement of the five theorem conclusions and the corollary.

```text
setting: qubits on the EDGE sites of finite subgraphs of the cubic lattice -- open boxes 2x2xL (L = 3..8), 2x3x3, 2x3x4, 2x3x5, 2x3x6, 3x3x3, 3x3x4, 4x4x4 and periodic tori 4^3, 6^3, 4x4x6, 8^3; ordinary composition; Record and Admissibility reading note (2) quoted verbatim from MINIMAL_AXIOMS_2026-06-29.md
law: BKSF superfast encoding; eta = Kawamoto-Smit staggered signs, flux -1 on every face including the tori's wrap-around faces; H = -sum_e eta_e T_e, t = 1; sea = the code-space ground state at half filling (N even); H_R = the hops on the UNRECORDED edges = P_S H P_S
tick_model: STIPULATED, PR #7876 Model A -- Lueders formation with the Born odds of the pre-record state; exp(-i tau H_R) between formations; tau in {0.5, 2.0}
unit: DECLARED -- a whole corner set formed jointly; R(S) = union of the stars of S; every set, pattern, order and schedule enumerated or written out; no seed
T1_criterion [numerical, 1e-13]: for a regular S with closure S', P_w|sea> is an H_R eigenvector at every live outcome iff h_R U_{S1} subset U_{S1} for every pattern, U_{S1} = R_{V\S'}(W ∩ e_{S1}^perp); residual = ||(I - P_U) h_R U||_F, eigenvalue Tr(U^+ h_R U), odds 2^-(|R|-|S'|) p_det; liveness = dim U_{S1} = N - |S1|. Cube, ALL 255 sets, every outcome, 249 regular: max|resid_mb - resid_1p| 1.435e-14, max|<H_R>_mb - Tr| 1.510e-14, max odds gap 4.4e-16, 75 eigen-sets, 6 irregular sets non-eigen at 0.7071. Slab 2^20 on |J| = 473088 (sea E = -(8+2sqrt2), residual 2.5e-15, support 411648), declared 107-set family, 86 regular: 2.926e-13 / 2.002e-12 / 3.4e-14; all 21 smallest irregular sets non-eigen at >= 0.827
T2_structure [exact; numerical, 1e-13]: h^2 - D - T2 = 0.0e+00 with T2 the straight-two-step graph, entries +1, on every cluster except the 4^3 ground sector where h^2 = 6I and T2 = 0. Slab, ALL 4095 sets (2375 distinct closures, 33 eigen): 80 single-sublattice closures, 20 eigen = 20 class unions, eigen <=> class union set by set; minimal eigen-sets = the 8 T2 components {0,2},{1},{3,5},{4},{6,8},{7},{9,11},{10}; all 33 eigen closures have both parts class unions; 13 mixed = 4 non-adjacent + 9 closures of a class union, 0 unexplained; 132 non-eigen class-union closures all adjacent; 547 irregular. Cube: 30/30 single-sublattice eigen, 45 of 225 mixed, size-2 mixed = 4 antipodal, 12 adjacent fail, size-4 = the 8 closed stars
T3_classification [numerical, 1e-13]: complete over every union of up to three stars -- 2x2xL sets 298/696/1350/2324/3682/5488 eigen 22/8/8/8/4/0; 2x3x3, 2x3x4, 2x3x5, 2x3x6, 3x3x3, 3x3x4 sets 987/2324/4525/7806/3303/7806 eigen 10/4/4/4/4/2; 4x4x4 open 43744 sets, 0 eigen, 0 pass the screen. Every class an eigen-set <= 1.0e-14; every proper subset of a class of size <= 8 fails, smallest 0.178 / 0.152 / 0.275; 4x4x4 corners see 8 modes at 0.27-0.36; plaquette 0.996, cell 1.430, line 0.388, plane 0.366, class minus one 0.358, two classes 1.3e-14
T4_cover [numerical, 1e-12]: even (equally odd) classes partition the record sites on all 13 boxes; every proper prefix closure of all 24 orders is an eigen-set, 182 distinct closures of sizes 1-32, max residual 2.0e-13. Cube 96 trees (24 orders x 2 parities x tau in {0.5,2.0}): TV <= 1.2e-15, support 1984, 256/256 cancellation and 1856/1856 charge zeros kept, node residual <= 1.6e-14, displacement <= 1.8e-15; pair schedules <= 5.7e-16. Slab 48 orders at tau = 0.5: full-law TV <= 6.7e-16 on support 411648, node residual <= 4.4e-14, displacement <= 2.4e-15; identity order at tau = 2.0 <= 6.7e-16. Controls: cube antipodal 0.106/0.299 (prefix 0.707), adjacent 0.229/0.319 (0.500), faces 0.102/0.024 (0.662), one at a time 0.247/0.324, closed star then antipode 2.8e-16/4.2e-16; slab degree-3 star alone 0.0203 (support 428032, residual 0.2071), plaquette 0.139, coarse cell 0.081, adjacent pair 0.299 (support 455680), six even corners in one tick 0.0
T5_tori [numerical, 1e-12]: ground sectors 4^3 (1,1,1) E -78.384 = -32sqrt6 gap 4.899; 6^3 (0,0,0) E -258.858 gap 3.464, no zero modes; 4x4x6 (1,1,0) gap 4.472; 8^3 (1,1,1) gap 2.651; periodic 4^3 and 8^3 carry 8 zero modes and no sea. 4^3: h^2 = 6I, 64 singleton classes, of 2080 unions of <= 2 stars the 64 singles, 992 same-sublattice and 832 non-adjacent cross pairs are eigen-sets, 192 adjacent fail; line/plane/class/class-minus-one/two classes <= 1.8e-14, plaquette 1.33, cell 2.07. 6^3: T2 648 edges, 8 classes of 27 (162 records), 0 of 179804 unions of <= 3 stars pass the screen, classes eigen <= 5.1e-14 over 114 patterns, declared subsets >= 0.357, corner 8 modes 0.3572, plaquette 1.302, cell 1.903, line 0.507, plane 0.622. 8^3: T2 1536 edges, 8 classes of 64 (384 records), class of corner 0 eigen at 1.1e-13 over 8 declared patterns, declared subsets >= 0.380, 0 of 512 single corners pass, corner 0 sees 8 modes at 0.3798. 4x4x6: T2 z-only, 32 columns of 3 (18 records), exactly 32 of 147536 unions of <= 3 stars eigen <= 2.8e-14, class of 12 eigen 2.5e-14 over 4096 patterns, class minus one 0.1975
corollary: the joint rule "form together all records incident to a whole class of the superlattice role pattern, in any order, with Born odds" preserves the sea's registration on every cluster computed; the unit is ~V/8 corners on any box with all sides >= 3, 27 corners / 162 records on 6^3, 64 corners / 384 records on 8^3, infinite on the lattice; single-corner units survive only where h^2 is a multiple of the identity (the 2x2x2 cube; the 4^3 torus in its ground sector, an L = 4 cancellation)
boundary: the clusters and twist sectors listed; N even; the unitary tick at tau in {0.5, 2.0}; many-body certification on the cube (complete) and the 2x2x3 slab (declared family) only; unions of up to three stars enumerated completely (the 6^3 torus modulo its 27 even translations, the 8^3 torus single corners only); larger sets by the class structure; subsets as declared; nothing derived from any axiom; no rate, unit or tick foreclosed
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=17 FAIL=0
```

## Proof boundary

Every statement above is proved on the **open boxes** `2x2xL` (`L = 3..8`), `2x3x3`, `2x3x4`, `2x3x5`, `2x3x6`, `3x3x3`, `3x3x4` and `4x4x4`, and on the **periodic tori** `4^3`, `6^3`,
`4x4x6` (all eight twist sectors scanned, the classification run in the ground sector) and `8^3` (single corners and declared units only), in **one flux sector** (all-minus, the
Kawamoto-Smit staggered signs) at **half filling only** with `N` even (the `3x3x3` sea carries its one zero mode, `N = 14`), `t = 1`, and for **one between-event model**, PR #7876's Model A,
at `tau in {0.5, 2.0}`. **Many-body certification is on the `2x2x2` cube and the `2x2x3` slab only** -- complete over the cube's `255` vertex sets and every outcome, and over a declared
`107`-set family of the slab; everywhere else the criterion is evaluated one-particle. **Unions of up to three stars are enumerated completely** on every cluster where that is stated (on the
`6^3` torus modulo its `27` even translations, which act freely and exactly); larger sets are treated through the class structure, with all proper subsets of every class of size `<= 8` and
declared subsets above that, and declared pattern families where `2^|S'|` is out of reach (`114` patterns on a `6^3` class, `8` on an `8^3` class, all `2^|S'|` otherwise). **Not covered:**
interacting or non-flux-`-1` laws, other fillings, irregular sets beyond the cube and the slab (where the one-particle test is only sufficient), formation units that are not unions of whole
stars -- PR #7900's face is the one non-star unit on record, and it fails -- and the relaxation tick of PR #7895. Nothing is claimed for other clusters, other sectors, other particle numbers
or infinite lattices. The law is **designed**, not derived.

**The liveness caveat.** A corner-occupation pattern counts as having nonzero odds by the **orbital-dimension test** `dim U_{S1} = N - |S1|`, never by the determinantal odds themselves:
those underflow below `1e-13` for sets above about `43` corners (`2^-64` on an `8^3` class), which would make the class tests on the large tori vacuous. Every statement here about a set
above `43` corners uses the dimension test.

**The tick and the unit are stipulated reconstructions**, adopted or declared here and supplied by no axiom; reading note (2) says the axioms supply no formation site, probability or rate,
and they supply no unit either. This note supplies none as axiom content, adds none, and amends none. Every line not tagged `[exact]` is a deterministic double-precision evaluation at the
stated threshold; the `2^20` object is touched by sparse Pauli strings, Lanczos and a Chebyshev propagator only, no dense object above `4096 x 4096` is formed, peak memory stays under `0.7
GB`, and there is **no seed anywhere**. No absolute unit appears, no axiom text is amended, extended, reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no
registry or manifest node is created or edited.

## Review record

**Honest-auditor read.** An honest auditor should come away with one positive and one price, both on declared finite sets. The positive: there **is** a single joint-formation rule that keeps
the sea's registration on every cluster computed, the criterion that decides it is a one-particle test that is exact rather than approximate, and the rule's units are forced -- they are the
classes of the superlattice role pattern and there is nothing smaller inside one. The price: that unit is extensive. It is an eighth of the corners of any box with all sides at least `3` and
an infinite set on the lattice, and every local candidate tried -- one star, three stars, a plaquette of stars, a coarse cell, a coarse line, a coarse plane, a class minus one corner --
fails by `0.15` to `2.1`. The tick, the unit and the orders are declared as stipulations in the front matter, the setting, the claim block and the proof boundary alike; nothing is presented
as following from an axiom; no rate, unit or tick is foreclosed.

**Disagreements with the expectation this probe was run under, stated plainly.** (i) The expectation that some *local* union of stars covers every corner is wrong on every cluster whose
one-particle spectrum is not flat: the minimal eigen-set containing a degree-`3` corner of `2x2x8` is its whole column of four, of a `3x3x3` corner the eight outer corners together, of a
`6^3` corner its class of `27`; three stars never suffice past the short columns. (ii) The `4^3` torus, where single corners do work, is a length accident and not evidence for a local rule:
`+2 = -2 mod 4` makes the two straight two-steps cancel in an antiperiodic direction, and its periodic sector has eight zero modes and no sea at all. (iii) The one-particle criterion is not
an agreement to three digits, as PR #7902's single-corner form reported: once the closure and the regularity condition are respected and the `2^-(|R| - |S'|)` gauge factor is written out it
is exact to the sea's own residual, outcome by outcome, over every vertex set of the cube. (iv) Mixed-sublattice eigen-sets do exist beyond flat bands -- `{0,2,10}` on the slab is one -- but
they too are unions of classes; on no cluster does an eigen-set have a sublattice part that is not a class union.

**Departures from the scratch computation this note lands, stated here.** The scratch reported the slab's many-body-versus-one-particle agreement as `2.435e-13` (residual), `1.403e-12`
(eigenvalue) and `1.1e-14` (odds) over all `2711` regular sets with `|S'| <= 8`; the runner rebuilds the slab's sea by its own Lanczos-plus-polish path (residual `2.5e-15` against the
scratch's `1.38e-12`) and gets `2.926e-13`, `2.002e-12` and `3.4e-14` over its declared `107`-set family, each worst case attained at `|S'| <= 8`. These are the same order of magnitude and
sit at the floating-point floor of a `473088`-term reduction; the runner's values are the ones certified here, and the slab's complete `4095`-set scan is carried out one-particle rather than
many-body for the runtime budget. Likewise the cube's agreement is `1.435e-14 / 1.510e-14 / 4.4e-16` here against the scratch's `1.526e-14 / 1.599e-14 / 4.4e-16`, and the cube's class trees
reach `TV <= 1.2e-15` against the scratch's `2.7e-15`, the slab's `<= 6.7e-16` against `1.87e-15`, both because the propagator is a Chebyshev series under a rigorous norm bound rather than
`expm_multiply`. Every structural count -- `75` and `229`/`33` eigen objects, `6` and `547` irregular sets, `22 / 8 / 8 / 8 / 4 / 0` and `10 / 4 / 4 / 4 / 4 / 2` eigen-sets among the unions
of up to three stars, `0` of `43744`, `0` of `179804`, `32` of `147536`, `992 + 832 + 64` on the `4^3` torus -- reproduces the scratch exactly, as do the control distances (`0.0203`,
`0.139`, `0.081`, `0.299`) and every declared repair-unit residual. The `8^3` class test uses an eight-pattern declared family rather than the scratch's `188`; the scratch's `1.16e-13` and
this note's `1.1e-13` agree.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority" pointers are plain text
carrying no grade and no weight, each with its PR state at the time of writing (all seven parents are open PRs, none on main). Hard landing conditions are a fresh runner and cache pair at
`PASS=17 FAIL=0`, runtime under the declared `AUDIT_TIMEOUT_SEC = 300` seconds (`92` s measured), and passing pipeline, strict-lint and changed-evidence gates. The runner prints `8575`
characters over `18` lines, above the `5500`-character target, because every certified figure is printed on its own check's line. Audit remains a separate lane, and the ledger has been
unaudited since 2026-08-07.
