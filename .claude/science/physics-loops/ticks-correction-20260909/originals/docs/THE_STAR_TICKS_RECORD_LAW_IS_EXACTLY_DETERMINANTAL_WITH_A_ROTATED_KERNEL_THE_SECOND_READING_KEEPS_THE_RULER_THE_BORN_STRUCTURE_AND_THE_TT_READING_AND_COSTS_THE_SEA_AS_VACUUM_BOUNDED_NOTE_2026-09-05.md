---
claim_id: star_tick_record_law_determinantal_rotated_kernel_second_reading_priced_2026_09_05
claim_type: bounded_theorem
claim_scope: "On finite subgraphs of the cubic lattice with qubits on the EDGE sites, ordinary composition, the superfast encoding and the corner parity dictionary n_v = (1 - B_v)/2, in the staggered (pi-flux) Kawamoto-Smit sector H = -sum_e eta_e T_e, t = 1, at half filling -- the 2x2x2 cube, the 2x2x3 slab and the periodic tori 4^3 (twist (1,1,1)) and 6^3 (twist (0,0,0)) -- for the STIPULATED tick of PR #7876 Model A and the STIPULATED star tick of PR #7974's sum sharing rule S1, with the corner-order families and the null-event convention DECLARED here and tau in {0.1, 0.5, 2.0} with declared scans: (T1) for any Model-A schedule the final record law is |<w| U_{k-1} ... U_1 |sea>|^2 -- every formation projector commutes with every later restricted propagator, so the formations are invisible to the level vector -- hence the law of every fixed schedule is EXACTLY determinantal, P(w) = 2^-g p_K(Aw) with the rotated projection kernel K = G P G^+, G = prod exp(-i tau h_R), and the sea's own gauge factor; certified many-body against one-particle to 1.04e-17 on the cube's whole 2^12 record space and 3.9e-18 on the slab's 2^20 space held on |J| = 473088, with PR #7947's A4 figures reproduced to nine digits and its B2 figures reproduced. (T2) Complete over all 8! = 40320 cube corner orders at three tau: 1440 are exact (576 even-first, 576 odd-first, 288 more), the rest reach TV 0.342 at tau = 0.5, the uniform-order average sits at TV 0.009854703 / 0.145430031 / 0.237998278 with support 2240 and none of the 256 cancellation zeros, a fixed order keeps 8, 4, 2 or 0 of them with histogram [25536, 0, 9792, 0, 2976, 0, 0, 0, 2016], TV = c tau^2 as tau -> 0 and there is no large-tau limit (quasi-periodic, Cesaro TV 0.199223). (T3) On the slab no star-tick order is exact (prefix residual 0.2071 at the first degree-3 corner); 28 declared orders span 0.032625-0.486099 at tau = 0.5, family average 0.345484. (T4) Per fixed order every one of 521-2953 formation events has Born odds equal to the diagonal of ONE conditioned pre-record state of the sea's kind, the rotated Slater state, to 4.4e-16, so PR #7969's one-frame, fibred-identity and refuted-global-clause structure transfers verbatim, with a three-outcome menu now realised; for the order-averaged law the odds are those of a conditioned MIXED state and the best single Slater state sits at TV 0.068765 (tau = 0.5) / 0.090499 (tau = 2.0) where the same search fits a single order exactly. (T5) Per order the law is exactly determinantal with the zero criterion intact and the sea's zeros gone; the disturbed state is not an h-eigenstate (residual 2.81) and the two-mode and class structure do not transfer; no formation unit holds the disturbed law still (a second class round displaces it by 0.30); order-averaged it is a mixture of determinantal laws and no single one within a 64-parameter search. (T6) On the tori the site statistic is exactly 1/2 with identically zero response for every order, polarisation, momentum and shift, so the sublattice cancellation and the rate ruler stand; the TT rank pattern survives exactly while the calibration does not (amplitudes halve on 4^3, 0.016586 vs 0.034722; the sea's endpoint-mean silences break; the face-diagonal statistics come alive at 7.1e-3 on 4^3 and 8.7e-3 on 6^3 while the shear columns stay exactly zero); the tick keeps 0.2423 / 0.2346 of the sea's binding energy at kernel distance 0.8705 / 0.8724; rotation covariance of the mixture needs the full 48-element cubic group. The tick, the star tick, the formation unit, the order families, the null-event convention and tau are stipulated or declared and are supplied by no axiom. No seeds anywhere."
upstream_dependencies: []
runner: scripts/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.py
---

# The record law of any Model-A schedule is the determinantal law of a rotated projector, `G P G^+`; under the star tick the physical law is a mixture of such laws, and on it the rate ruler, the sublattice cancellation and the TT rank criterion survive exactly while the sea's zeros, its two-mode and class structure and the propagating sector's calibration do not (bounded, cube and slab many-body, `4^3` and `6^3` one-particle)

**Date:** 2026-09-05
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.py`](../scripts/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.py)
**Runner cache:**
[`logs/runner-cache/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.txt`](../logs/runner-cache/star_tick_record_law_rotated_kernel_second_reading_priced_check_2026_09_05.txt)
**Parents:** none. Every premise used below is declared in this note.

`THE_FORMATION_UNIT_THAT_PRESERVES_THE_SEA_IS_A_WHOLE_CLASS_..._2026-09-04.md` (open PR #7968) left the tick's open content split into two readings and chose neither: either formation is non-local at the level of the
vacuum -- the unit in which the sea's records lock is an extensive corner set -- or the sea is not what survives local formation, in which case the physical record statistics are the ones a local unit actually
produces. This note computes the second reading and prices it. The object is the star tick of PR #7974 under its sum sharing rule `S1`, the one local formation process whose rate is the ruler's rate exactly; its
record law is computed on the cube complete over every corner order, on the slab over a declared family, and on two tori, and every lane built on the sea -- gravity's static and propagating halves, the Born line, the
determinantal structure -- is evaluated on it. The first thing the computation returns is that there is nothing exotic about the disturbed law: it is the determinantal law of a rotated projector, and the tick lane's
own trees have been computing it all along.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on the 2x2x2 cube, the 2x2x3 slab and the 4^3 and 6^3 tori in the staggered sector at half filling, for the stipulated tick of PR #7876 Model A, the stipulated star tick of PR #7974's sum sharing rule S1, and corner-order families declared in full here. The cube census is complete over all 8! = 40320 corner orders at three tau values; the many-body certification walks the cube's whole 2^12 record space and the slab's 2^20 space held on its half-filling index set, |J| = 473088; the Born trees are complete enumerations in the unnormalised-branch form; the propagator is a Chebyshev series under the rigorous bound ||H_R|| <= the number of free edges. The setting checks are exact symplectic Pauli and F2 arithmetic. The torus response is exact linear response, the sea's dP by projector perturbation theory and the tick's dG by the divided-difference Frechet derivative of every exp(-i tau h_R). Nothing is sampled, there is no seed anywhere in the runner, every cluster, order, pattern and schedule is enumerated or written out, and no dense object above 4096 x 4096 is formed."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Price the two horns against a physical criterion the computation does not supply: whether the propagating sector's calibration, which under the second reading becomes a property of the formation process rather than of the vacuum, is fixed by anything already declared, or whether it is a second free parameter alongside the rate. Report the full record law, never the leaf statistics."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six theorems and the corollary below, exactly the runner's check groups: Theorem 1 on the cube (`A1`), Theorem 2 complete over `8!` orders (`B1`) with its `tau` dependence and the
null-event convention (`B2`), Theorem 3 on the slab (`B3`), Theorem 4's Born structure per order (`C1`) and its Markov and single-site menu statements (`C2`), Theorem 5 per order (`D1`) and on the order-averaged law
(`D2`), Theorem 6 on the `4^3` torus (`E1`), on the `6^3` torus (`E2`) and on the vacuum's own energy (`E3`), and the timing (`F1`). `A1` and `B3` carry **exact** content: the encoding relations `R0`-`R4` in
symplectic Pauli arithmetic with phases mod `4`, the face group, the flux sector, the cluster combinatorics and the `F2` rank that fixes the gauge factor. Everything else is a **deterministic double-precision
evaluation** of an exactly specified quantity at the stated threshold. Nothing is sampled: the slab's Lanczos start is the fixed vector `cos(0.7 i + 0.3) + i cos(1.3 i + 1.1)` projected into the code space, written
out in the runner, and every cluster, order, pattern, momentum and schedule is written out there too. There is **no seed anywhere**.

## Imports and authority

Imported scientific authority: none load-bearing. The superfast encoding, the Kawamoto-Smit staggered signs, Lueders conditioning, Slater determinants and their quadratic Hamiltonians, determinantal point processes,
Lanczos, the Jacobi-Anger expansion of the propagator, the divided-difference Frechet derivative of a matrix exponential, the transverse-traceless decomposition and the total-variation distance are standard
methodology; every object is redeclared here and the runner recomputes every statement. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade
and no weight, with each one's state at the time of writing: `NO_SITE_WISE_FORMATION_RULE_PRESERVES_THE_SEA_..._2026-09-03.md` (**open PR #7947** -- the site-wise distances and the trees reproduced here);
`THE_FORMATION_UNIT_THAT_PRESERVES_THE_SEA_IS_A_WHOLE_CLASS_..._2026-09-04.md` (**open PR #7968** -- the class unit and the two readings this note prices);
`THE_RULERS_PER_SITE_FORMATION_RATE_IS_THE_STAR_TICKS_RATE_..._2026-09-04.md` (**open PR #7974** -- the star tick, the sum sharing rule `S1`, and the class tick's missing potential);
`THE_TWO_TT_GRAVITON_POLARISATIONS_ARE_READ_BY_THE_AXIS_BOND_PAIR_RECORD_STATISTICS_..._2026-09-04.md` (**open PR #7951** -- the dressing, the edge rule, the pair-statistic reading and the TT conventions);
`THE_MATTER_LAWS_OWN_TICKS_REALISE_MENUS_IN_ONE_FRAME_ONLY_..._2026-09-04.md` (**open PR #7969** -- menu, grading, the fibred and global clauses, the abundance item);
`RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_..._2026-09-03.md` (**closed PR #7876** -- Model A, adopted unchanged as the tick); `RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_..._2026-09-03.md`
(**open PR #7883** -- the sea's determinantal record statistics that reappear here with a rotated kernel); `THE_VACUUM_QUESTION_IS_ONE_COEFFICIENT_OF_THE_LAW_..._2026-09-03.md` (**open PR #7885**); the ruler chain's
three notes (**open PRs #7916, #7925 and #7940** -- the record-density ruler, the formation-rate ruler that evades the cancellation, and the static Regge edge lengths); and `MINIMAL_AXIOMS_2026-06-29.md` (on main),
from which the axiom text in "Setting" is quoted verbatim. This note cites no grade of any and consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. Lattice / Physical Locality and Qubit / Site Possibility are used only through the graph structure of the clusters and the `M_2(C)` site algebra. **Record / Fixed
Reality**, verbatim: *"Records form."* *"When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."* *"Only records are readable. A
readout value is determined by record content alone. A site with no record cannot be read."* **Admissibility / Local Constraint** reading note (2), interpretive and non-governing, verbatim, because it is what leaves
both horns of the corollary open: *"Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or
rate."* The axioms supply no formation **unit** either. Everything in the next paragraph is supplied by the parents or declared here; nothing below follows from an axiom.

**Supplied, exactly as the parents supply it.** The designed fermion law (superfast encoding on the edge sites, Kawamoto-Smit staggered signs `eta_x = 1`, `eta_y = (-1)^x`, `eta_z = (-1)^(x+y)`, flux `-1` on every
face, `H = -sum_e eta_e T_e`, `t = 1`, one-particle matrix `h_ij = -eta_ij`); the half-filled sea as the code-space ground state; PR #7876's Model A as the **tick** -- a forming record locks its value by Lueders
conditioning with the Born odds of the current pre-record state, and between formations the pre-record state runs by `exp(-i tau H_R)`, `H_R` the hops on the unrecorded edges, which is `P_S H P_S` on the record
sector; `tau in {0.1, 0.5, 2.0}`; and PR #7974's **star tick** under its sum sharing rule `S1` -- every corner's star ticks, a ticking star registers jointly all of its still-unrecorded edge sites, so a record site
forms at the first tick of either of its two stars. The second tick of a site finds it recorded, and since `H_R` commutes with `Z_e` for every recorded `e` a re-registration returns the same value with probability
one, so `S1` and one-record-per-site agree exactly on the record law. **Declared here, by no parent:** (i) the corner order in which the stars tick -- the physical object is the **uniform-order average**, complete
over all `8!` orders on the cube, a declared 28-order family on the slab where `12!` is out of reach, and declared symmetric families on the tori; single orders are reported as its members; (ii) a star tick whose
edges are all already recorded is a **null event** -- it forms nothing and no evolution follows it -- with the alternative reported as a quantified sensitivity.

**Reading, not theorem.** The cluster, the encoding, the staggered sector, half filling, the tick, the star tick, the order families and the null-event convention are stipulated reconstructions of what would be
registered. Nothing here is presented as following from an axiom, and no unit or rate is foreclosed.

## Definitions

A **cluster** is a finite subgraph `G = (V, E)` of the cubic lattice, corner `(x, y, z)` indexed `(x L_y + y) L_z + z`, one qubit per edge site. For a schedule with formation steps `i = 1..k` recording edge sets
`U_i`, write `R_i = U_1 u ... u U_i` and `U_i = exp(-i tau H_{R_i})` for the evolution after step `i`. `P_w` is the projector on the full record pattern `w`; `A` is the corner-edge incidence over `F2`, so `n_v` is
the parity of `w` on `star(v)`; `g = |E| - rank_F2 A` is the **gauge dimension** (`5` on the cube, `9` on the slab). `W` is the span of the `N = V/2` lowest `h`-modes and `P = W W^+` the sea's one-particle projector.
`h_R` is `h` with the recorded edges' entries zeroed, `G = prod_i exp(-i tau h_R_i)` with later factors on the left, and `K = G P G^+` the **rotated kernel**. A law is **determinantal** with kernel `K` when `p_K(n) =
det(diag(n) K + diag(1-n)(I - K))`. **TV** is total variation; the **full law** is the distribution on all `2^|E|` record patterns after every edge has formed. The cube's zeros are `2112`: `1856` **charge zeros**
(patterns with `N != 4`) and `256` **cancellation zeros** (the eight closed corner stars times `32`). **Superlattice role pattern** means the eight-class partition of the corners by `(x, y, z) mod 2`. The gravity
lane's **statistics** are the per-corner site occupation, the three axis-bond pair statistics `-|K_{v,v+e_a}|^2` and the six face-diagonal pair statistics; its **response** is exact first-order linear response to the
dressing `t_e = t(1 - h_e)` under PR #7951's endpoint-mean rule, assembled as a matrix of (statistic, half-reciprocal shift) rows against six polarisation columns, whose **TT rank** is the rank of its projection on
the two transverse-traceless polarisations.

## Theorem 1 -- the record law of every Model-A schedule is the determinantal law of a rotated projector

**Conclusion.** `[exact]` For any Model-A schedule -- site-wise, star-wise, class-wise, in any order -- the final record law is `P(w) = || P_w U_{k-1} ... U_1 |sea> ||^2`: each `P_{w_j}` is a function of `Z_e`, `e in
R_j`, and `H_{R_i}` commutes with every such `Z_e` for `i >= j`, because each hop's Pauli `X`-part sits on one unrecorded edge; so in `P_{w_k} U_{k-1} P_{w_{k-1}} ... U_1 P_{w_1}|sea>` every projector commutes past
the propagators to the left and their product is `P_w`. **The formations are invisible to the level vector; only the sequence of restricted evolutions acts.** Since `H_{R_i}` is the encoded quadratic Hamiltonian of
the graph with the recorded edges deleted and preserves the code space, `U_{k-1}...U_1|sea> = Slater(G W)`, so **the record law of every fixed schedule is exactly determinantal**, `P(w) = 2^-g p_K(A w)` with `K = G P
G^+` a rank-`N` projector and the **same** uniform gauge factor `2^-g` as the sea's. What changes is the kernel, not the form: the disturbance is a unitary rotation of the sea's projector by the tick's own restricted
propagators. Two corollaries follow from the bipartite grading `eps h eps = -h`, which survives every edge deletion: (a) `eps K eps = (I - K)^*`, so `K_vv = 1/2` exactly for every schedule and every `tau`; (b)
same-sublattice entries of `K` are purely imaginary and cross-sublattice entries real, so `Re(K_uv K_vw K_wu) = 0` for every triple and the 3-point marginals of every law in this family, mixtures included, are fixed
by the 1- and 2-point ones.

**Certification.** `[numerical, 1e-15]` On the cube's whole `2^12` record space the one-particle law equals the many-body `|sea|^2` to `4.34e-18`; PR #7947's A4 figures for its `24` declared edge orders at `tau =
0.5` reproduce to nine digits by **both** routes (identity `0.324925161`, reverse `0.289380397`, min/max/mean `0.289380397 / 0.456208220 / 0.379401338`, average law `0.239288631`) with `max|law_mb - law_1p| =
1.04e-17` over `24 x 4096` patterns; five declared star-tick orders under **both** null-event conventions agree to `5.0e-18`; and for the identity order `K^2 = K` to `2.2e-16`, `tr K = 4.000000000000`, `max|K_vv
- 1/2| = 4.4e-16`, the corner law equals `det(K)` to `1.18e-16` and the fibre is uniform to `4.3e-18`. `[numerical, 1e-12]` On the slab's `2^20` record space held on `|J| = 473088` the same agreement is `4.1e-18` for
  the sea and `3.9e-18` over four declared star orders and PR #7947's rule-C six-record law (`2.7e-18`).

**Reading, not theorem.** The tick lane's trees were computing `|<w| U_{k-1} ... U_1 |sea>|^2` all along. Nothing about the disturbed law is a new kind of object.

## Theorem 2 -- the star tick on the cube, complete over all `40320` corner orders

**Conclusion.** `[numerical, 1e-12]` Complete over all `8! = 40320` corner orders at `tau = 0.1 / 0.5 / 2.0`. TV to the sea runs `0` to `0.056408783 / 0.342363972 / 0.452076976` with mean `0.020698 / 0.227752 /
0.321057`. Exactly **`1440` orders are exact at every `tau`** -- `576` even-first, `576` odd-first and `288` others in which every prefix closure is an eigen-set, exactly PR #7968's criterion, now counted. Support
takes the values `{1984, 2112, 2176, 2240}`: a fixed order keeps `8`, `4`, `2` or `0` of the eight closed-star zeros, with histogram `[25536, 0, 9792, 0, 2976, 0, 0, 0, 2016]` over `j = 0..8`. The **uniform-order
average** -- the physical object -- sits at TV `0.009854703 / 0.145430031 / 0.237998278` with support `2240` and **none** of the `256` cancellation zeros at any `tau`. TV is invariant under the `48` cube symmetries
to `3.1e-16`. `tau -> 0`: `TV = c tau^2`, local exponent `2.00` for the identity order (`3.444e-06` at `1e-3`), for the antipodal order (`2.250e-06`) and for the uniform average (`1.0077e-04` at `0.01`, `9.0531e-04`
at `0.03`); the support is already `2240` at `tau = 1e-3`, so the cancellation zeros go at any `tau > 0` and only their weight is small. `tau -> infinity`: **no limit** -- over the declared grid `tau = 0.5 + 0.25 j`,
`j < 400`, the identity order's TV ranges `0.0009 - 0.3362` with mean `0.2246` and last-100 spread `0.3326`, quasi-periodic because each `exp(-i tau h_R)` carries an incommensurate finite spectrum; its `tau`-averaged
(Cesaro) law sits at TV `0.199223` on support `1984`, the antipodal order's at `0.214374`. **Null-event sensitivity:** "evolve after every tick" displaces a single order's TV by at most `0.13` and the uniform average
from `0.145430` to `0.154022`; a null event before full coverage occurs in `10368` of the `40320` orders. No verdict below depends on the convention.

## Theorem 3 -- on the slab no star-tick order is exact

**Conclusion.** `[exact; numerical, 1e-12]` On the `2x2x3` slab (`12` corners, `20` edges, `g = 9`, sea `E = -10.828427124746 = -(8 + 2 sqrt 2)`, support `411648`, `61440` cancellation zeros) **no star-tick order is
exact at any declared `tau`**, `0` of `28` at each. Every order's first event is a single star, the only single-corner eigen-sets are the two degree-`4` corners, and the third event is a degree-`3` corner whose
prefix closure fails: the identity order's prefix residuals are `0.2071, 0.5003, 0.7071, ...` and the deg4-first order's `0.0000, 0.0000, 0.2071, 0.2143, ...`. At `tau = 0.5` the `28` declared orders span TV
`0.032625` (even-first, odd-first, deg4-first and classes-in-order, all on support `411648` with every one of the `61440` cancellation zeros kept) to `0.486099` (rshift3), with declared-family average `0.345484` on
support `473088` and no zeros kept; at `tau = 0.1` the span is `0.001457 - 0.160932` with average `0.081326`, at `tau = 2.0` it is `0.151098 - 0.612645` with average `0.408083`. Many-body against one-particle on `|J|
= 473088` agrees to `3.9e-18` over four star orders (TV `0.468995964` identity, `0.032625043` even-first, by both routes), and PR #7947's B2 figures reproduce: `0.1148 / 0.3156` at `tau = 0.5` and `0.0268 / 0.3472`
at `tau = 2.0`. The `12!` uniform average is out of reach; the 28-order family is the declared stand-in and is stated as such.

## Theorem 4 -- the Born structure of PR #7969 transfers per order, and the physical law's odds are a mixed state's

**Conclusion.** `[numerical, 1e-15]` Cube, many-body, `tau = 0.5`, every branch of the tree walked. At every one of the `2793` (identity), `2889` (antipodal), `521` (even-first) and `2953` (closed-star-first)
formation events the Born odds of the branch state -- Model A's own definition -- **equal the record-basis diagonal of the one conditioned final level vector** `Psi_pi = U_{k-1}...U_1|sea> = Slater(G_pi W)`, to
`4.4e-16 / 3.3e-16 / 1.1e-16 / 4.4e-16`. So PR #7969's structure transfers verbatim with the sea replaced by the order's rotated Slater state, a state of the same kind: odds are the diagonal of a conditioned
pre-record state and the menus sit in one frame. The menu census gives `7` menus of sizes `{1,2,4,8}` for the identity order, `9` of sizes `{1,2,3,4,8}` for the antipodal order -- including a **three-outcome menu**
on a 2-edge unit, absent on the sea's star, because a lost cancellation zero re-opens a pattern while a charge zero still closes one -- `37` of sizes `{4,5,6,8}` for the even-first (class) order and `8` of sizes
`{1,2,6,8}` for closed-star-first. The **global clause stays refuted by the supports**, `rank(A|1) = rank(A) + 1`, at every unit size with more than one menu in every order, while the fibred clause holds as the same
identity. `[numerical, 1e-15]` Records on the four edges sharing a corner with a site never displace its odds off `1/2` (`2.8e-16` on the sea, `3.3e-16` on both disturbed laws), and over **all** conditions with `k <=
9` prior records the single-site menus are the same three, `{P0,P1}`, `{P0}`, `{P1}`, with the first forced record at `k = 8` on the sea and on the identity-order law and at `k = 9` on the antipodal-order law. The
abundance item stays unpaid: every menu is still a subset of the record frame. `[numerical, 1e-13]` For the **uniform-order mixture** the odds are the diagonal of the conditioned mixed state, an identity, and no
single state of the sea's kind reproduces them: the best rank-`4` projector sits at TV `0.068765` from the `tau = 0.5` mixture and `0.090499` from the `tau = 2.0` mixture, where the same search recovers a single
order's law exactly (TV `0.000000`, minors `3.9e-16`).

## Theorem 5 -- exact determinantal structure per order; a mixture of such laws on average

**Conclusion.** `[numerical, 1e-13]` Cube, `tau = 0.5`. Every fixed order's law is exactly the determinantal law of the rank-`4` projector `K = G_pi P G_pi^+`: over seven declared orders `max|K^2 - K| = 3.3e-16`, `tr
K = 4` to `0.0e+00`, rank `4`. The **determinant criterion for zeros survives as a criterion** -- a pattern has probability zero iff its minor vanishes -- while the sea's own zeros do not: the identity order keeps
all eight closed-star zeros at TV `0.246607` (support `62/70`), shift1 keeps `{0,7}` and shift3 keeps `{3,4}` (`68/70`), shift2 and the antipodal order keep none (`70/70`, TV `0.307152 / 0.286110`), and even-first is
exact. The disturbed state is **not** an `h`-eigenstate: `<h> = -3.878820 / -4.652201` against the sea's `-6.928203`, with one-particle eigen-residual `2.8140 / 2.4781` where the sea's is `0`. PR
#7968's eigen-set criterion evaluated on `W_pi = G_pi W` gives single corner `2.2336 / 1.7477`, adjacent pair `1.9636 / 1.5137`, antipodal pair `1.4070 / 1.2838`, closed star `1.1048 / 0.8615` against the sea's
`0, 0.5000, 0, 0`; its zero on the even class is the cube accident that the class records every edge, so `H_R = 0`. **No formation unit holds the disturbed law still:** a second round -- the even pairs `{0,3}` then
`{5,6}` with evolution between -- displaces it by TV `0.295792 / 0.340817` where the same schedule leaves the sea at `2.3e-16`. `[numerical, 1e-13]` The **physical order-averaged law** has 1-point marginals `1/2` to
`2.7e-14`, its 2-point-derived `sum |K_uv|^2` is `4.000000` for any rank-`4` projector so that test cannot discriminate, and its 3-point marginals are fixed by symmetry (Theorem 1(b), phase ratio `<= 6.7e-07` with
`0` violations of `56`); the discriminating content is at four points and beyond. The best single Slater state, a 64-parameter search over `G = expm(iA)` from five declared starts, reaches TV `0.068765` (`tau = 0.5`)
and `0.090499` (`tau = 2.0`) with 2-/3-/4-point minors off the mixture's marginals by `1.8e-2 / 1.4e-2 / 1.0e-2`, against TV `0.145430` and `0.237998` from the sea; the control, a single order's law, is fitted to TV
`0.000000` and minors `3.9e-16`, and the 16-order cyclic mixture to `0.047305`. Since the mixture has `N = 4` exactly, a determinantal law for it would need a projection kernel, so "determinantal", "Gaussian" and
"Pfaffian" coincide here and the fit tests all three. **The exact structure of the physical law is a mixture of determinantal laws over the formation orders, and no single determinantal law reproduces it within the
search** -- an upper bound on the best fit, not a lower-bound certificate.

## Theorem 6 -- gravity on the disturbed law: the static half stands, the propagating half keeps its reading and loses its calibration

**Conclusion.** `[numerical, 1e-14]` The `4^3` torus in its ground twist sector `(1,1,1)` (`E_sea = -78.383672`, gap `4.898979`, flat, `h^2 = 6I`) with the declared `O_h x T` family of `3072` orders, and the `6^3`
torus in `(0,0,0)` (`E_sea = -258.857540`, gap `3.464102`, the non-flat check) with the declared 27-even-translation family; `tau = 0.5`.

*The static half is intact and stronger than on the sea.* The **site statistic is `1/2`** to `1.7e-16` on `4^3` and `3.8e-15` on `6^3` for the mixture, and **its response to every metric polarisation is zero at every
momentum and every shift**, `<= 2.2e-16` and `<= 3.3e-15` against the sea's `8.1e-18` and `7.6e-18`. This is Theorem 1(a): the bipartite grading survives every edge deletion, so `K_vv = 1/2` for any dressing of the
hop magnitudes and the sublattice cancellation is exact **order by order**, where PR #7951 found it on the sea only in the uniform part. The reading of the disturbed law's site statistic stays where it was, so PR
#7974's identification of the star rate with the ruler's rate is untouched and the rate ruler is still the carrier of the scalar.

*The propagating half keeps its rank criterion and loses its map.* The **TT rank pattern survives exactly** -- rank `1` on every coordinate-plane momentum, rank `2` off them, `[1,1,2,2,2]` on `4^3` at `n =
(1,0,0)/(1,1,0)/(1,1,1)/(1,1,2)/(1,2,3)` and `[1,1,1,2,2,2]` on `6^3` -- because it is set by the coupling and by covariance, not by the law. The **magnitudes halve**: TT singular values `0.016586 / 0.009521 /
0.003867 / 0.004437 / 0.003329` on `4^3` against the sea's `0.034722 / 0.020833 / 0.008505 / 0.008019 / 0.005952`, and `0.019545 / 0.016647 / 0.013441 / 0.009104 / 0.003763 / 0.003910` on `6^3` against `0.030359 /
0.023311 / 0.020249 / 0.013664 / 0.015679 / 0.009180`. The **sea's endpoint-mean silences at `k_a = pi` break**: at `(1,1,2)` and `(1,2,3)` on `4^3` the sea is exactly silent in the second TT direction and the
disturbed law responds at `2.6e-04` and `3.0e-04`. **Shear columns are exactly `0.0e+00`** on every law, so the shear sector stays unread by a length-dressed hop for PR #7951's coupling reason and the period-2
coupling that would read it remains supplied; but the **face-diagonal pair statistics, identically zero on the pi-flux sea** (`8.6e-32`, `9.6e-32`), **come alive** at `7.1e-3` on `4^3` and `8.7e-3` on `6^3` and
respond at `2.7e-3` and `4.2e-3`. **Rotation covariance of the mixture needs the full 48-element cubic group:** at the body diagonal `s_min/s_max` is `1.0000` for `O_h` and `0.9292` for the `24` proper rotations
alone; PR #7951's group `O` suffices for the sea only because the sea's kernel is real. The rotation-averaged `6^3` family (`1296` orders) is above this runner's budget and is quoted, not recomputed: TT rank `2` with
singular values `0.004079 / 0.001423` and `s_min/s_max = 0.3488` at `(1,1,2)` against the sea's `0.015679 / 0.004882` and `0.3114` -- amplitudes down by `3.8 / 3.4` with the conditioning at its kinematic value.

*How disturbed the vacuum is.* `[numerical, 1e-12]` On `4^3` every order of the declared family gives `tr(h K_pi) = -18.990137` against `-78.383672`, so the tick keeps `0.2423` of the sea's binding energy at kernel
distance `||K_pi - P||_F / ||P||_F = 0.8705`; on `6^3`, `-60.727366` against `-258.857540`, `0.2346` kept at distance `0.8724`. The face-diagonal `|K|^2`, exactly zero on the sea, reaches `3.43e-02` and `3.92e-03`
per order. For scale the cube's `40320` orders keep `0.7645` of its binding energy. On the tori the tick is an order-one rotation of the vacuum's kernel, not a perturbation of it.

## Corollary -- the two horns, priced; the computation cannot choose between them

Within the setting declared above, on the clusters and sectors named in the proof boundary:

**Horn A -- non-local formation plus two rates.** Formation locks whole classes of the superlattice role pattern, about `V/8` corners -- `27` corners and `162` records on the `6^3` torus, `64` and `384` on `8^3`, an
infinite set on the lattice (PR #7968). The sea and every one of its exact record features survive. The price: one non-local unit at the level of the vacuum, and a class rate that carries no Newtonian potential (PR
#7974), so gravity needs a **second**, star-level rate, and the two cannot be one object.

**Horn B -- local formation, one rate, a disturbed vacuum.** The star tick under `S1` is the one formation process, its rate is the ruler's rate exactly, and the physical record law is the order-averaged law computed
here. The price, with the numbers. (1) The vacuum's record law sits at TV `0.145430` (`tau = 0.5`) and `0.237998` (`tau = 2.0`) from the sea on the cube and keeps `0` of its `256` cancellation zeros; on the tori the
record state keeps `24 %` of the sea's binding energy at kernel distance `0.87`. (2) The law depends on `tau` (as `tau^2` near zero, with no large-`tau` limit) and on the order statistics of the tick, so it is a
property of the **formation process**, not of the vacuum alone. (3) The sea's exact features lost: **all** the cancellation zeros, the two-mode condition, the class structure, the identically-zero face-diagonal
statistics, and -- for the physical order-averaged law -- the determinantal form itself, which becomes a mixture of determinantal laws with best single-state fit TV `0.069`. (4) Gravity's propagating half keeps its
readability pattern and loses its **calibration**: a ruler that inverts the sea's response matrix on the disturbed records mis-reads the amplitude by a factor about `2` and the polarisation mixture by the ratio of
the two conditioning numbers, and the calibration then depends on `tau` and on the order statistics -- it becomes a property of the formation process. (5) The Born structure keeps its form per order, but the physical
law's odds are those of a conditioned mixed state.

**What Horn B keeps intact, exactly:** the charge zeros; `<n_v> = 1/2` at every corner for every order; the sublattice cancellation, with identically zero response, stronger than on the sea; the rate ruler; the TT
rank criterion; the coupling zero of the shear sector; the one-frame menu structure of PR #7969 and its fibred identity.

**The computation cannot choose.** Admissibility's reading note (2) is quoted above in full: the distribution *"does not supply the formation site, probability, or rate"*, and the axioms supply no formation unit
either. What this note fixes is what each horn costs, and it removes one apparent asymmetry: under Horn B the "disturbance" is not noise on the sea. It is a different determinantal law per order with a computable
kernel `G_pi P G_pi^+`, and the physical law is the mixture of those.

## Disagreements with the expectation this probe was run under, stated plainly

1. The disturbed law is **not** a new kind of law: for every fixed schedule it is exactly determinantal with a rotated projection kernel, and the tick line's trees were computing `|<w| U_{k-1} ... U_1 |sea>|^2` all
   along. The "disturbance" is a unitary rotation of the sea's kernel by the tick's own restricted propagators.
2. The star tick on the cube is **not** always disturbing: `1440` of `40320` orders -- all even-first, all odd-first and `288` more -- reproduce the sea exactly, and the identity order keeps every cancellation zero
   at TV `0.2466`. On the slab, by contrast, no order is exact.
3. The sublattice cancellation is **stronger** on the disturbed law than PR #7951 found it on the sea: the site statistic is `1/2` with identically zero response for every order, every polarisation, every momentum
   and every shift.
4. The sea's endpoint-mean silences at `k_a = pi` are **broken** by the disturbed law (a second TT singular value about `3e-4` appears), and its face-diagonal vacuum zero is lost, while the coupling zero of the shear
   sector is not.
5. Rotation covariance of the mixture requires the **full** `48`-element cubic group; the `24` proper rotations leave a `7 %` asymmetry at the body diagonal. PR #7951's group `O` suffices for the sea only because the
   sea's kernel is real.
6. The best single Slater state is **closer** to the mixture (TV `0.069`) than the sea is (`0.145`): the physical law is nearer to *some* determinantal law than to the sea's, just not to any one of them.
7. Large `tau` has **no limit**; `tau -> infinity` is a quasi-periodic function with a Cesaro mean about `0.2`.

## Reading, not theorem -- the whole thing in plain words

Ask what the vacuum's own record statistics look like if records lock around one corner at a time instead of around a whole interleaved sub-lattice at once. The answer is not a smeared or noisy version of the sea. It
is a clean object of exactly the same shape: for each order in which the corners take their turn, the statistics are those of a Slater determinant whose one-particle space has been turned by the very propagators the
tick runs between one locking and the next, and the whole family of such objects, averaged over the order, is the physical law. That law is about a seventh of the way across the space of distributions from the sea at
the representative `tau`, and about a quarter of the way on the tori measured by binding energy. What it costs is specific. Every one of the sea's exact cancellations -- the patterns the vacuum forbids outright -- is
gone, and gone at any `tau` however small, though with small weight. The neat spectral conditions that told you which corner sets keep the vacuum still no longer apply, and nothing keeps the new law still either. And
the physical law, being an average over orders, is no longer of the single-determinant kind at all, though the closest one is nearer to it than the sea is.

What it does not cost is the part of gravity that was carrying the ruler. The per-corner occupation is exactly one half on the disturbed law, for every order, with exactly zero response to any metric dressing -- more
exactly than on the sea, where a piece of that cancellation held only in the uniform part. So the rate that reads out as a length still reads out as a length. The two transverse polarisations are still readable, and
still by the same criterion of rank; what is lost is the dial, the number that converts a measured pair statistic into an amplitude, and that number becomes a property of how formation happens rather than of what the
vacuum is. Either formation is non-local at the level of the vacuum and gravity needs two rates, or formation is local and this is the vacuum, at these prices. The axioms say nothing about which.

## Interfaces named for other lanes, not settled here

- **PR #7947 (the site-wise parent).** Its A4 and B2 distances are reproduced to nine digits and explained: they are the distances of a rotated Slater state.
- **PR #7968 (the class unit).** Its prefix criterion is what selects the `1440` exact cube orders, now counted; its class criterion is the condition `G_pi = ` a phase on every branch. The two readings it left open
  are the two horns priced above.
- **PR #7974 (the star tick and the ruler's rate).** The star tick under `S1` is adopted unchanged and is the object computed. Its identification of the star rate with the ruler's rate is untouched by the law's
  disturbance, because the site statistic the ruler reads is still `1/2` with zero response.
- **PR #7951 (the TT reading).** Its rank criterion and its shear coupling zero survive exactly; its calibration and its endpoint-mean silences do not, and its `24`-element rotation group must be enlarged to the full
  `48` for the mixture.
- **PR #7969 (the Born line).** Its one-frame structure, fibred identity and refuted global clause transfer verbatim per order; on the physical order-averaged law the odds are a mixed state's, and the abundance item
  stays unpaid. Whether a three-outcome menu changes anything for that item is not computed here.
- **PR #7876 (the tick).** Model A is adopted unchanged; Model B is not touched.
- **PR #7883 (the determinantal record statistics).** They reappear here with the kernel rotated, and with the same gauge factor.
- **The ruler chain (PRs #7916, #7925, #7940).** Its static input is the per-site formation rate, not the record law, so it is untouched; what this note adds is that the reading of the site statistic it relies on
  survives the disturbance exactly.

## Executable claim block

The canonical machine-bound restatement of the six theorem conclusions and the corollary.

```text
setting: qubits on the EDGE sites of the 2x2x2 cube, the 2x2x3 slab and the periodic tori 4^3 (twist (1,1,1)) and 6^3 (twist (0,0,0)); ordinary composition; Record and Admissibility reading note (2) quoted verbatim from MINIMAL_AXIOMS_2026-06-29.md
law: BKSF superfast encoding; eta = Kawamoto-Smit staggered signs, flux -1 on every face including the tori's wrap-around faces; H = -sum_e eta_e T_e, t = 1; sea = the code-space ground state at half filling; H_R = the hops on the UNRECORDED edges = P_S H P_S
tick_model: STIPULATED, PR #7876 Model A; star tick STIPULATED, PR #7974 sum sharing rule S1; corner-order families and the null-event convention DECLARED here; tau in {0.1, 0.5, 2.0} with declared scans; no seed
T1_identity [exact; numerical, 1e-15]: P(w) = ||P_w U_{k-1}...U_1|sea>||^2 for every Model-A schedule; law = 2^-g p_K(Aw), K = G P G^+ rank N, g = 5 cube / 9 slab; K_vv = 1/2 and Re(K_uv K_vw K_wu) = 0 for every schedule and tau. Cube whole 2^12 space: sea 4.34e-18, 24 edge orders 1.04e-17 with #7947's A4 at nine digits (0.324925161, 0.289380397, 0.289380397/0.456208220/0.379401338, 0.239288631), five star orders both null conventions 5.0e-18, K^2-K 2.2e-16, tr K 4.000000000000, K_vv-1/2 4.4e-16, det gap 1.18e-16, fibre 4.3e-18. Slab 2^20 on |J| = 473088: sea 4.1e-18, four star orders 3.9e-18, rule-C six records 2.7e-18, #7947's B2 0.1148/0.3156 and 0.0268/0.3472
T2_cube [numerical, 1e-12]: COMPLETE over all 40320 corner orders at tau = 0.1/0.5/2.0. TV max 0.056408783/0.342363972/0.452076976, mean 0.020698/0.227752/0.321057, exact orders 1440 at every tau = 576 even-first + 576 odd-first + 288 others; supports {1984, 2112, 2176, 2240}; zero-survival histogram [25536, 0, 9792, 0, 2976, 0, 0, 0, 2016]; UNIFORM AVERAGE TV 0.009854703/0.145430031/0.237998278, support 2240, 0 of 256 zeros; 48-symmetry invariance 3.1e-16; tau^2 exponents 2.00 (identity, antipodal, uniform average 1.0077e-04 at 0.01 and 9.0531e-04 at 0.03); no large-tau limit, grid 0.0009-0.3362, Cesaro 0.199223 / 0.214374; null-event sensitivity 0.13 per order, 0.145430 -> 0.154022 on the average, 10368 orders
T3_slab [exact; numerical, 1e-12]: 28 declared orders, 0 exact at every tau; prefix residuals identity 0.2071/0.5003/0.7071, deg4-first 0.0000/0.0000/0.2071/0.2143; tau=0.5 span 0.032625-0.486099, family average 0.345484 (support 473088, 0 of 61440 zeros); tau=0.1 0.001457-0.160932 average 0.081326; tau=2.0 0.151098-0.612645 average 0.408083
T4_born [numerical, 1e-15]: 2793/2889/521/2953 events, odds = diagonal of the conditioned Slater(G_pi W) to 4.4e-16/3.3e-16/1.1e-16/4.4e-16; menus 7/9/37/8 of sizes {1,2,4,8}/{1,2,3,4,8}/{4,5,6,8}/{1,2,6,8} with a three-outcome menu on a 2-edge unit; global clause refuted (rank(A|1) = rank(A)+1) at every unit size with more than one menu in every order; nearest-neighbour records leave odds at 1/2 to 2.8e-16/3.3e-16/3.3e-16; single-site menus the same three with first forcing k = 8/8/9; mixture odds = a conditioned mixed state's, best single Slater TV 0.068765 (tau=0.5) / 0.090499 (tau=2.0), control 0.000000
T5_structure [numerical, 1e-13]: per order K^2-K 3.3e-16, tr K 4, rank 4, zero criterion intact; zeros kept identity 8, shift1 {0,7}, shift3 {3,4}, shift2 and antipodal none, even-first exact; <h> -3.878820/-4.652201 vs -6.928203, eigen-residual 2.8140/2.4781; eigen-set criterion on W_pi 2.2336/1.9636/1.4070/1.1048 and 1.7477/1.5137/1.2838/0.8615 vs the sea's 0/0.5000/0/0; second round displaces by 0.295792/0.340817 (sea 2.3e-16); mixture 1-point 1/2 to 2.7e-14, sum|K_uv|^2 4.000000, 3-point phase ratio 6.7e-07 with 0 of 56 violations, best Slater 0.068765/0.090499, control 0.000000 with minors 3.9e-16, 16-order mixture 0.047305
T6_gravity [numerical, 1e-14]: 4^3 O_h x T family of 3072 orders (48 rotations + the exact 64-translation average, certified against all 64 explicitly: G != 0 rows 1.5e-16, G = 0 rows 1.3e-15) -- site 1/2 to 1.7e-16, site response <= 2.2e-16 (sea 8.1e-18), TT rank [1,1,2,2,2] vs the sea's [1,1,2,1,1], TT sv 0.016586/0.009521/0.003867/0.004437/0.003329 vs 0.034722/0.020833/0.008505/0.008019/0.005952, endpoint-mean silences break at 2.6e-04/3.0e-04, shear columns 0.0e+00, face-diagonal 7.1e-03 responding at 2.7e-03 (sea 8.6e-32), body-diagonal s_min/s_max 1.0000 for O_h and 0.9292 for O. 6^3 27-even-translation family (reduction R2, certified to 2.5e-15) -- sea baseline = the TT note, TT rank [1,1,1,2,2,2] and sv 0.030359/0.023311/0.020249/0.013664/0.015679/0.009180; disturbed site 1/2 to 3.8e-15, response <= 3.3e-15, TT rank unchanged, sv 0.019545/0.016647/0.013441/0.009104/0.003763/0.003910, axis pair -0.001009/-0.001594/-0.031317 (mean -0.011307), face-diagonal 8.7e-03, shear 0.0e+00, G != 0 axis response 1.2e-03-5.4e-03. Energies: 4^3 -18.990137 of -78.383672 (0.2423 kept, distance 0.8705), 6^3 -60.727366 of -258.857540 (0.2346, 0.8724), cube 0.7645. QUOTED not recomputed: the 1296-order rotation-averaged 6^3 family at (1,1,2), TT sv 0.004079/0.001423, s_min/s_max 0.3488
corollary: Horn A costs one non-local unit of about V/8 corners plus two rates that cannot be one object; Horn B costs the sea as vacuum (TV 0.145/0.238 on the cube, 24 % of the binding energy on the tori, all 256 cancellation zeros, the two-mode and class structure, the determinantal form of the physical law) and the calibration of the propagating sector, which becomes a property of the formation process; Horn B keeps the charge zeros, <n_v> = 1/2, the sublattice cancellation, the rate ruler, the TT rank criterion, the shear coupling zero and the one-frame Born structure. The computation chooses neither: the axioms supply no unit and no rate
boundary: the clusters and twist sectors listed; half filling; tau in {0.1, 0.5, 2.0} with declared scans; Model A only; the star tick under S1 with the declared null-event convention; the uniform-order average complete on the cube only, declared families elsewhere; linear response only, static perturbations, continuum TT vector; the best-Slater residuals are upper bounds from a 64-parameter search with five declared starts, not lower-bound certificates; nothing derived from any axiom; no rate, unit or tick foreclosed
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=12 FAIL=0
```

## Proof boundary

Every statement above is proved on the **`2x2x2` cube** (complete over all `8!` corner orders at three `tau`, many-body certified on its whole `2^12` record space), the **`2x2x3` slab** (`28` declared corner orders,
four of them many-body certified on the `2^20` record space held on `|J| = 473088`), the **`4^3` torus** in its ground twist sector `(1,1,1)` (the declared `O_h x T` family of `3072` orders, evaluated through the
exact translation reduction certified in the runner) and the **`6^3` torus** in `(0,0,0)` (the declared 27-even-translation family; the `1296`-order rotation-averaged family at one momentum is **quoted, not
recomputed**, and is named as such wherever it is used). One flux sector, the Kawamoto-Smit staggered signs, at **half filling** only, `t = 1`, one between-event model -- PR #7876's Model A -- at `tau in {0.1, 0.5,
2.0}` with the declared small-`tau` and large-`tau` scans, and one formation process, PR #7974's star tick under `S1`, with the null-event convention declared in "Setting" (sensitivity `<= 0.13` per order and
`0.0086` on the average). No mass term, no relaxation tick, no interacting law. The **uniform-order average is exact on the cube only**; on the slab and the tori declared families stand in and are named where they
are used, and the `6^3` translation family's directional spread is the reduced family's period-2 content, not anisotropy of the physics. Linear response only, static perturbations, continuum TT vector. The
one-particle gravity rows are on the tori; the many-body certification is on the cube and the slab. **Not covered:** other clusters, other flux sectors, other fillings, interacting laws, Model B, formation units that
are not unions of whole stars, and any statement about the infinite lattice. The law is **designed**, not derived.

**The tick, the star tick, the order families and the null-event convention are stipulated reconstructions**, adopted or declared here and supplied by no axiom; reading note (2) says the axioms supply no formation
site, probability or rate, and they supply no unit either. This note supplies none as axiom content, adds none, and amends none. Every line not tagged `[exact]` is a deterministic double-precision evaluation at the
stated threshold; the `2^20` object is touched by sparse Pauli strings, Lanczos and a Chebyshev propagator only, no dense object above `4096 x 4096` is formed, peak memory stays under `1 GB`, and there is **no seed
anywhere**. No absolute unit appears, no axiom text is amended, extended, reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

**Honest-auditor read.** An honest auditor should come away with one structural simplification and one bill. The simplification: the record law of a Model-A schedule is not a new kind of object at all, it is the
determinantal law of a rotated projector, and that makes the whole second reading computable exactly rather than approximately -- complete over every corner order of the cube, certified many-body on two clusters, and
evaluated for gravity and for the Born line on the same footing as the sea. The bill: under that reading the sea is no longer the vacuum. Every exact record feature that came from the sea's nearest-neighbour
projector is gone -- all `256` cancellation zeros at any `tau > 0`, the two-mode condition, the class structure, the identically-zero face-diagonal statistics, and the determinantal form of the physical
order-averaged law itself -- and the propagating sector's calibration goes with them. What does not go is the half of the gravity chain that was carrying the ruler, and it comes through more exactly than it did on
the sea. The tick, the star tick, the order families and the null-event convention are declared as stipulations in the front matter, the setting, the claim block and the proof boundary alike; nothing is presented as
following from an axiom; no rate, unit or tick is foreclosed, and the note does not decide between the horns.

**Departures from the scratch computation this note lands, stated here.** Every figure quoted above reproduces the scratch exactly at the printed digits, including the `1440` exact orders, the zero-survival
histogram, the three uniform-average distances, the `28`-order slab spans, the `2793 / 2889 / 521 / 2953` event counts, the menu censuses, the best-fit distances `0.068765 / 0.090499 / 0.000000 / 0.047305`, the `4^3`
and `6^3` TT tables and the torus energies. Two differences of record. (i) The runner computes the `4^3` `O_h x T` family of `3072` orders and the `6^3` 27-translation family through the exact translation reductions
described in the runner's header, rather than by running every member: the family average of the response matrix is unchanged (certified against all `64` translations of the base order on `4^3`, agreeing to `1.5e-16`
on the annihilated rows and `1.3e-15` on the surviving ones, and against two declared translated orders on `6^3` to `2.5e-15`), and the resulting site-response bound on `4^3` is `2.2e-16` where the scratch's
`3072`-order sum gave `6.1e-17` -- the same exact zero with a different floating-point accumulation. (ii) The scratch's per-condition Born statements are recomputed here as exact marginal reductions -- one `bincount`
per record subset instead of a boolean mask per condition -- which changes the arithmetic path and not the values: the same three single-site menus, the same first forcing at `k = 8 / 8 / 9`, and the
nearest-neighbour bound `2.8e-16` on the sea against the scratch's `2.8e-16`. One numbering correction: the determinantal record statistics quoted throughout are PR **#7883**, not #7885, which is the vacuum-question
note; both are cited above.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the "Imports and authority" pointers are plain text carrying no grade and no
weight, each with its PR state at the time of writing. Hard landing conditions are a fresh runner and cache pair at `PASS=12 FAIL=0`, runtime under the declared `AUDIT_TIMEOUT_SEC = 300` seconds (`104` s measured),
and passing strict-lint, minimal-axioms and changed-evidence gates. The runner prints `12095` characters over `13` lines, above the `5500`-character target, because every certified figure is printed on its own
check's line and the two torus lines carry a full singular-value table each. Audit remains a separate lane, and the ledger has been fully unaudited since 2026-08-07.
