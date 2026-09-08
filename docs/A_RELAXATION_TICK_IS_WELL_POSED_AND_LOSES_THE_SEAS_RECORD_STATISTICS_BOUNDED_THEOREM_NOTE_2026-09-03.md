---
claim_id: a_relaxation_tick_is_well_posed_and_loses_the_seas_record_statistics_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "On the supplied cube model, the 128-dimensional +face code realizes even eight-mode Fock space inside the 4096-dimensional ambient record carrier. Local Z recording generally leaves that code. With supplied sea preparation, Born odds, declared order, ambient block-ground reset Pi/deg and a classical record register, the 32 executed complete MR laws have full support and order-dependent probabilities, unlike the supplied sea. The sequential commuting Lueders alternative reproduces the sea law without simultaneous recording. The original finite spectra, charge distributions, overlap rows and ModelA tau=.5 comparison are retained at their numerical tolerances. Compression removes recorded-edge hops only between record projectors. Fixed-record reset is linear CPTP; normalized conditional branches are nonlinear. The energy formula -(12-k)/sqrt3 is a Lueders-weighted mean, not each outcome; the printed difference subtracts means under different laws. The one-site Z commutant conclusion assumes the supplied parity dictionary and nondisturbance requirement. No physical formation, preferred state, basis or clock is derived; no formal audit is invoked."
upstream_dependencies: ["minimal_axioms_2026-06-29"]
runner: scripts/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.py
---

# A relaxation tick is well posed and loses the sea's record statistics

**Date:** 2026-09-03; source correction 2026-09-08
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** conditional finite source, corrected for independent review; no applied audit status
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.py`](../scripts/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.txt`](../logs/runner-cache/relaxation_tick_well_posed_loses_sea_record_statistics_check_2026_09_03.txt)
**Premises:** finite models are supplied below; the [current Record memo](MINIMAL_AXIOMS_2026-06-29.md) governs only the interpretation boundary. No physical embedding, probability law or clock is derived.

`RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7876) writes a tick model down and finds its answer turning on two declared choices it
cannot settle -- the gap length `tau` and the post-record generator `H_R` -- and names the interface it leaves open: something would have to re-supply, between one record and the
next, a state at rest under the current generator. At the campaign's vacuum panel on 2026-09-03 a candidate wording was proposed that would close exactly that interface: **"Between
records, the lattice settles into its lowest-energy arrangement."** That sentence is not axiom text. This note takes it as a **stipulation under test**, turns it into a tick on the
same cube in the staggered sector, and computes what it does against a supplied comparison target -- the half-filled sea's Born record statistics. The result is two-sided: the
tick is well posed and memoryless, and it does not give back the sea's odds.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-sector statements on one named cluster -- the 4096-dimensional record space of the 2x2x2 cube in the staggered sector, whose 128-dimensional face code realizes even Fock space within the ambient 4096-dimensional carrier -- for one stipulated tick model. T1 and T7 are exact symplectic-Pauli statements with no floating point, and T2's zero census is exact F2 combinatorics on a zero set identified from the Born diagonal at 1e-12. MR enumerates all 4096 leaves with no sampling; the separate unitary/Lueders recursion omits relative branches at or below 1e-15. Block states are obtained by diagonalisation, so the resulting comparisons are deterministic double-precision evaluations tagged [numerical] with their thresholds. There is no seed anywhere in the runner and no Monte Carlo section."
trace_class: frontier_discovery
target_claim_id: a_relaxation_tick_is_well_posed_and_loses_the_seas_record_statistics_bounded_theorem_note_2026-09-03
target_blocker_text: null
source_of_blocker_text: handoff
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Confirm the corrected finite source independently; physical sea-law matching, role geometry, formation and clock remain supplied or open. Formal audit is owner-deferred until a solid TOE."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the seven statements below, exactly the runner's check groups `A`-`G`: `T1` (`A`) the restriction identity and the setting; `T2` (`B`) the sea's own
record odds and its zeros; `T3` (`C`) support; `T4` (`D`) order dependence; `T5` (`E`) charge; `T6` (`F`) relaxation against conditioning; `T7` (`G`) the pointer-basis table. Groups
`A1`-`A3` and `G` are **exact**: symplectic Pauli algebra with phases mod `4` and integer amplitudes. `B2` and `B3` are exact `F2` combinatorics on a zero set identified from the Born
diagonal at `1e-12`, and are tagged so. The rest are **deterministic double-precision evaluations** of exactly specified quantities at the stated thresholds. Nothing is sampled: MR enumerates all `4096` leaves, while the separate unitary/Lueders recursion omits relative branches at or below `1e-15`. Every order is written out in the runner; numerical normalization and comparison tolerances are not exact-arithmetic certificates. There is **no seed anywhere** and no Monte Carlo section.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggered link signs, Lueders conditioning and the total-variation distance
are standard methodology; every object is redeclared here and the runner recomputes every statement, the encoding's relations included. No observational value, no fitted number and no
framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no weight: `RECORD_TICKS_ADMIT_NO_INVARIANT_PRE_RECORD_STATE_..._2026-09-03.md`
(open PR #7876 -- the same cube and encoding, its Models A and B, its `T2` boundary at `p = 1`, and the `tau`/`H_R` interface this note's model closes by fiat);
`DETERMINANTAL_RECORD_STATISTICS_ON_THE_HALF_FILLED_SEA_..._2026-09-02.md` (PR #7883 -- the sea's Born statistics, the same `eta_ks`);
`EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_..._2026-09-02.md` (PR #7842 -- the selection-rule zeros from the dictionary side);
`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_..._2026-09-02.md` (PR #7858 -- forcing on the empty vacuum, whose `T2` this note's `T2` is the half-filled analogue of);
The current memo linked above supplies the quoted interpretive boundary. Historical parent names and panel statements below are dated attribution only; no parent theorem or campaign is accepted from them. Model A and all finite objects actually used here are redeclared locally. This note consumes no ledger row.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency,
standard translations, and proper cubic rotations about each site." "No site is privileged. Sites are distinguished by the supplied lattice structure alone." The finite graph and its edge-qubit role assignment below are supplied modeling choices. Identifying those roles with physical nearest-neighbor sites requires a separate placement/readout bridge; "edge site" and "corner" below have graph meanings. **Qubit / Site Possibility**: "Each site has a domain of local
possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`." "No possibility is privileged. Possibilities are distinguished by the supplied algebraic
structure alone."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the
probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Two reading notes, interpretive and non-governing, are the hinge
of this note and are quoted with it. (2): "Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; **it does not
supply the formation site, probability, or rate.**" (3): "The distribution is a probability measure on the local possibility domain; 'available'/'admissible' denotes its support -- on
finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure; Record locks a supported realization."

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."
"Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Composition here is **ordinary**: the algebra of a region is the tensor product of its sites' algebras, operators on disjoint regions commute, and no graded clause is used anywhere.
The **record ontology** is used as declared: a record at an edge site **registers** a value there; it does not report one the site already carried. Reading note (3) is what makes `T3`
a real cost: "admissible" is the *support* of the distribution, so a tick giving every pattern nonzero odds has made every pattern admissible. **The stipulation under test** --
"Between records, the lattice settles into its lowest-energy arrangement" -- is a candidate wording, not axiom text, and is not called wrong anywhere below; `M_R` is one way of making
it definite, and what is reported is what `M_R` does and does not do.

## The stipulated tick model `M_R`, declared in full

Six choices, all supplied here. A different physical proposal need not reproduce this chosen sea unless sea-law matching is independently made its target.

1. **The state before any record** is the sea: the ground state of `H` in the code space (see "Definitions").
2. **Which site forms next.** The next unrecorded edge site in a **declared order**, a permutation of the `12` sites. Thirty-two are declared and written out in the runner -- the `12`
   cyclic shifts of the identity order, their `12` reverses, and `8` further orders listed explicitly -- and none is drawn at random.
3. **The value the forming record locks.** The Born odds of the current pre-record state in the `Z_e` record basis.
4. **Relaxation -- the panel's clause.** The pre-record state is then **replaced** by the ground state of `H` restricted to the subspace consistent with all records so far. This replacement is nonunitary. At fixed records R, sigma_R=Pi_R/deg_R is fixed and the extension X -> Tr(X)sigma_R is linear CPTP. Outcome normalization is a different, nonlinear step.
5. **The tie-break.** Where that ground space is degenerate the state becomes the **normalised projector** `Pi/deg` onto it, and the next record's odds are its diagonal. Degeneracy is
   not a corner case: it occurs at ticks `5`, `6`, `8`, `9` and `11` (`T5`).
6. **Permanence.** Records never change; the run continues until all `12` sites carry records, so each run ends on one of the `4096` record patterns.

**`M_R^N`**, the charge-superselected variant, is declared alongside: identical except that step 4 relaxes inside the conserved `N = 4` sector of the block. Two reference ticks are
computed against `M_R`: **`L`**, twelve sequential commuting Lueders measurements with no intervening dynamics, yielding the same joint law as simultaneous measurement; and **`A`**, the locally redeclared historical Model A, identical to `M_R` except
that step 4 is replaced by the unitary `exp(-i tau H_R)`, run at `tau = 0.5`.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is `P0`-`P7`. `P0` (declared here): the cube, the edge-site
qubits, the encoding, the staggered sector, the parity dictionary, and the six stipulated choices above. `P1` (`A`): the restriction identity and the sea. `P2` (`B`): the sea's own
record odds and its zeros. `P3` (`C`): support. `P4` (`D`): order dependence. `P5` (`E`): charge. `P6` (`F`): relaxation against conditioning. `P7` (`G`): the pointer-basis table.

## Definitions

The **cube** is the `2x2x2` cube graph, corner `s = 4a + 2b + c`, `8` corners, `12` edge sites, `6` faces. One qubit sits on each **edge site**, neighbours ordered by index:

```text
A_ij = X(edge ij) * prod Z(edges at i ordered before j) * prod Z(edges at j ordered before i),   A_ji = -A_ij,
B_v  = prod of the Z's on the edges incident to v,     S_f = the ordered product of the A's around a face f,
T_ij = (i/2) A_ij (B_i - B_j),     H = -t sum_e eta_e T_e,  t = 1,     star(v) = the edges incident to v.
```

`eta` are the **Kawamoto-Smit staggered link signs** `eta_x = 1`, `eta_y = (-1)^x`, `eta_z = (-1)^(x+y)`, the same `eta_ks` as PR #7883; their product round every one of the six faces
is `-1`, the all-minus (**pi-flux**) sector. The **code space** is all six `S_f = +1`, of dimension `2^12/2^5 = 128`; it realizes the even eight-mode Fock space. The identity `prod_v B_v = I` already holds on all 4096 ambient record words and does not select this128-dimensional face code. Local Z recording generally leaves the code. The
**sea** is the ground state of `H` there. A **record** at an edge site registers a `Z`-value, so a finished set of records is a vector in `F2^12`, one of `4096` **patterns**; the
**parity dictionary** is `n_v = (1 - B_v)/2 = |y intersect star(v)| mod 2`, `N = sum_v n_v` and the **readable charge** is `Q = N - 4`. A **record block** `S(R,w) = {z : z|_R = w}` is
the subspace consistent with the records `w` on `R`; `H_R` is `H` compressed to this ambient record block, not a renewed face-code restriction. The **odds at a site** are the probability that a record forming there locks `1`, given the records
present. `TV` is total variation, `(1/2) L1`.

## Theorem 1 -- the restriction identity, and why `M_R` is memoryless

**Conclusion.** `[exact]` Every one of the `12` hop terms has Pauli `X`-part exactly one edge qubit. Hence for every record set `R`, `P_S H P_S = P_S(-sum_{e not in R} eta_e T_e)P_S`. This is equality on the compressed block, not equality of the unrestricted full-space matrices. So the relaxed state of step 4 depends on `(R, w)`
and nothing else, and `M_R` is **memoryless**. `[numerical, 1e-11]` The setting: `R0`-`R4` hold pair by pair, the face group carries no `-I`, `k = 5`, the code dimension is `128`, the
flux is `-1` on all six faces, the code space is `H`-invariant to `3e-17`, and the sea has `E = -6.928203230276 = -4 sqrt 3`, is non-degenerate, has gap `3.464101615138 = 2 sqrt 3`
and is sharp `N = 4` (Born mass off `N = 4`: `2e-31`).

**Proof.** `T_ij = (i/2) A_ij (B_i - B_j)` and `B_i`, `B_j` are pure `Z`, so both Pauli words `A_ij B_i` and `A_ij B_j` carry the `X`-part of `A_ij`, the single edge qubit `ij`; the
runner asserts this pair by pair. A term whose `X`-part touches a recorded site carries `S(R,w)` off itself and is killed by `P_S ... P_S`; a term whose `X`-part is unrecorded
preserves it. The relations, the group and the code dimension are the complete symplectic computation with `Z4` phases; the sea is one `128 x 128` diagonalisation.

**Scope.** Once the generator, ambient block, degeneracy rule and reset are supplied, the next state is fixed by the record prefix. This does not derive those choices or the next formation site.

## Theorem 2 -- the sea's own record odds are flat, and its zeros

**Conclusion.** `[numerical, 1e-12]` On the sea, every one of the `24 + 264 + 1760 = 2048` record blocks with `k <= 3` carries weight exactly `2^-k` (to `4e-15`): the odds at a
forming record are `1/2` and **nothing is forced up to three records** -- the half-filled-sea analogue of PR #7858's `T2`. `[exact, 1e-12 zero read]` At `p = 1`, where every site registers before
anything else happens, the finished set is the sea's Born diagonal: support `1984 = 62 x 32`, and `2112` zeros splitting as `1856` **charge zeros** (every pattern with `N != 4`) plus
`256 = 8 x 32` **cancellation zeros**. The `8` corner-occupation patterns carrying the cancellation zeros are **exactly the `8` closed corner stars** `{v} u N(v)`, one per corner --
for example `{0,1,2,4}` and its complement `{3,5,6,7}`.

**Proof.** The block weights are sums of `|sea|^2` over coordinate subsets. The zero census is read off the Born diagonal at `1e-12` and then handled combinatorially: the `N != 4`
count is `4096 - 2240 = 1856` by the parity dictionary, the remaining zero labels group by corner-occupation pattern into `8` patterns of `32`, and those `8` are compared as sets
against the `8` closed corner stars built from the cube's adjacency -- an equality of two `8`-element sets of `F2^8` vectors, with no tolerance in it.

**Scope.** This is a property of the supplied sea preparation and chosen record basis. Matching that law is the comparison target here, not an axiom-imposed requirement on every physical tick.

## Theorem 3 -- under `M_R` every pattern becomes admissible

**Conclusion.** `[numerical, 1e-12]` Under `M_R` at the identity order all `4096` patterns carry strictly positive odds (smallest `1.6e-05`), so **not one of the sea's `2112` zeros
survives**; the same holds at all `32` declared orders -- support `4096`, `0` zeros kept -- the charge zeros included, although `N` is conserved by `H` and commutes with every record
projection. `TV(M_R, sea Born) = 0.445486111111 = 1283/2880` at the identity order. PR #7876's Model A at `tau = 0.5` sits **closer**, `TV = 0.324925160534`, on support `2240`,
keeping all `1856` charge zeros and losing the same `256` cancellation zeros.

**Proof.** Each order's distribution is the exact product over the whole `4096`-leaf tree: at every node the block ground space is diagonalised once, the branch odds are the masses of
the relaxed diagonal on the two values, and the leaf weights are accumulated; nothing is sampled and no branch is pruned. The relaxed state uses the real skew form of `H_R`: the block
matrix is purely imaginary, so its square is `M M^T`, the ground level is `-sqrt(lambda_max)`, and the ground projector's diagonal is half that of the real spectral projector at
`lambda_max` on a nonzero band. A zero block uses its full zero eigenspace, as the runner explicitly handles.

**Reading, not theorem.** By reading note (3), "admissible" is the support of the distribution; under this tick the support is everything, so the patterns the sea never registered are
now registered, with odds of one in sixty thousand or better.

## Theorem 4 -- the odds depend on the order in which the sites record

**Conclusion.** `[numerical, 1e-12]` `TV(identity order, reverse order) = 0.333333333333 = 1/3`, for the same twelve sites and tick. Over the `32` declared orders -- the `12` cyclic
shifts, their `12` reverses, and `8` further orders written out in the runner, **no seed anywhere** -- the maximal pairwise `TV` is `0.727031250000` and the minimal `0.113194444444`,
and `TV` to the sea ranges `0.445486111111` .. `0.569444444444`. The maximum is a **lower bound** on the spread over all `12!` orders, not the spread itself. `[numerical, 1e-14]` The
sea's own Born rule, by contrast, is order-independent: pure Lueders conditioning reproduces its Born diagonal to `6e-15`, identity and reverse agreeing to `6e-15`.

**Proof.** Thirty-two whole trees as in `T3`, then `496` pairwise `L1` sums; the separate Lueders recursion removes the relaxation step and omits relative branches at or below 1e-15. Exact ideal order independence follows from the commuting-projector chain rule; the executed comparison has its stated floating tolerance. The declared order set is a
literal in the runner, asserted to be `32` distinct permutations of the `12` sites.

**Scope.** Order independence is a separately supplied comparison requirement. MR fails it on the 32 declared orders: TV is 1/3 for identity versus reverse and exceeds.7 for two orders. Sequential Lueders satisfies it by the commuting-projector Born chain rule.

## Theorem 5 -- half filling survives on average; the readable charge does not stay sharp

**Conclusion.** `[numerical, 1e-12]` `<Q> = 0` and `<N> = 4` at every one of the `32` declared orders (`max |<Q>| = 2e-16`, `max |<N> - 4| = 1e-14`), so `M_R` keeps half filling on
average. But `Q` is no longer sharp: at the identity order the law over `Q = -4, -2, 0, 2, 4` is `(1/384, 1/8, 143/192, 1/8, 1/384)` and `var Q = 1.083333333333 = 13/12`; over the
declared orders `P(Q = 0)` ranges `0.614583333333` .. `0.881319444444` and `var Q` ranges `0.488888888889` .. `1.666666666667`, so the charge law is itself order-dependent. The spread
sits on the tie-break: of the `8190` nodes of the identity-order tree, the `1456` whose relaxed state is **not** `N`-sharp are **exactly** the `1456` carrying a degenerate ground
space, at ticks `5`, `6`, `8`, `9` and `11`; at every tick the weight-averaged `<N>` is still `4` to `7e-15`. The variant `M_R^N` restores `P(Q = 0) = 1` and all `1856` charge zeros
on support `2240`, but still loses all `256` cancellation zeros, as Model A does.

**Proof.** The charge law is read off the `T3` trees against the parity dictionary and compared with the stated rationals at `1e-12`. The node census records, at every node, the
block's ground-space degeneracy and the `N` values its relaxed diagonal is supported on, and asserts the two coincide node by node. At tick `11` the degenerate blocks are exactly
those where `H_R` vanishes -- the last free hop has zero amplitude, its two corner endpoints carrying equal occupancy -- and the block's two states then differ in `N` by `2`; at ticks
`5`, `6`, `8` and `9` the degenerate ground space has `E_0 < 0` and still spans two `N` sectors.

**Reading, not theorem.** The tie-break is doing real work, and it is a declared choice, not a technicality: where the lattice has more than one lowest-energy arrangement this tick
shares the weight evenly among them, and there the arrangement carries no one definite charge. Superselecting charge fixes that and not the rest.

## Theorem 6 -- relaxation is not the sea held to the records

**Conclusion.** At all 24 one-record blocks, the relaxed state has overlap 0.962606705806 with the normalized Lueders-conditioned sea (spread 7e-15). At k=3 the 1760 overlaps have minimum 0.448473881026, mean 0.773546569701 and 64 values at 1. These original deterministic numerical results remain at the declared tolerances.

The energy column is the **Lueders-weighted average** over outcomes of the first k recorded sites, equal to `-(12-k)/sqrt3` to 4e-14. It is not each conditional energy. At mask31, outcome 0 has positive weight 1/48 and energy `-2sqrt3`; outcome 2 has weight 1/24 and energy `-(5/2)sqrt3`. Both differ from `-7/sqrt3`. The runner retains all 32 outcome rows and their weighted mean.

The original blockwise variational inequality `E0(R,w) <= <sea_{R,w}|H_R|sea_{R,w}>` has 0 violations over 2048 blocks with k<=3. The original printed `drops[k]`, however, subtracts the MR-weighted mean ground energy from the separately Lueders-weighted mean conditional energy. It is **not** an average of the pointwise inequality under a common law. This difference peaks at k=9 with 0.401011505139 and is zero to 1e-14 at k=3. At k=0 both constructions begin in the same sea, though the ambient block is 4096-dimensional; only k=12 has a one-dimensional block. F5 now checks the k=3 zero with absolute value, rejecting the preserved negative-one counterexample. All twelve original numerical energy rows are printed with their two weighting laws.

**Proof of the mean.** For a fixed set R, sum the normalized conditional quadratic forms with their Born weights. Their sum is `Tr[H_R sum_w P_w rho_sea P_w]`. For an unrecorded edge e, the signed Hamiltonian term `-eta_e T_e` commutes with all P_w, so its expectation is unchanged by this averaged measurement. The supplied staggered sea gives each **signed** term expectation `E_sea/12=-1/sqrt3`; summing the 12-k surviving terms gives the stated mean. The signed term, not T_e alone, enters this argument. The variational inequality holds independently at every positive-weight block. Neither fact identifies the two different ensemble weights.

**Fixed-record reset proof.** Write `sigma_R=sum_a lambda_a |a><a|` and choose a complete input basis |b>. The Kraus operators `K_ab=sqrt(lambda_a)|a><b|` satisfy `sum K_ab^dag K_ab=I` and `sum K_ab X K_ab^dag=Tr(X)sigma_R`. Thus reset is linear CPTP. Measurement followed by a record-dependent reset is a linear instrument before outcome normalization. The conditional normalized branch can be nonlinear, just as normalized Lueders conditioning is. The Lindblad generator `L=R_R-Id` has channel `exp(tL)=exp(-t)Id+(1-exp(-t))R_R`; ideal reset is its infinite-time limit. No exact finite-time bounded-generator reset or physical sea stationary-state mechanism is claimed.

## Theorem 7 -- a conditional one-site commutant

**Conclusion.** `[exact]` `Z_e` commutes with all `8` corner parities `B_v` at all `12` edge sites, while `X_e` and `Y_e` each anticommute with exactly the two endpoint parities of
their site. Given the supplied corner-parity dictionary and its nondisturbance requirement, a nontrivial one-site two-outcome projective measurement must be Z_e up to outcome labels. Indeed `aI+xX+yY+zZ` commutes with an incident parity only when x=y=0. This does not select the physical dictionary, a general instrument, or a physical record basis. The **face dictionary singles out none**:
`Z_e` anticommutes with exactly the two faces through `e` at all `12` sites, and no one-site basis at any site commutes with the corner dictionary and the face dictionary at once.

**Proof.** Three one-site Pauli words per site against `8 + 6` stabilizer words in the symplectic representation, the face incidences compared against the cube's own face list; all
integer arithmetic. (The `X_e`/`Y_e` counts against the faces are not uniform across sites and are an artefact of the declared `Z`-tail ordering; they are not used, `X_e` and `Y_e`
being already excluded by the corner column.)

**Scope.** The commutant result answers a conditional algebra question. The axioms do not supply this parity dictionary or require every physical tick to preserve it.

## Corollary -- what this says about a relaxation tick

1. With all six choices supplied, MR is well posed and its reset state depends on the record prefix. The blockwise variational inequality is useful; it does not derive a formation mechanism.
2. All 32 executed MR laws have full support and lose the chosen sea zeros; their probabilities depend on the supplied order. Half filling remains a mean, while the charge distribution spreads under the supplied Pi/deg tie-break. MR^N restores sharp charge without restoring the cancellation zeros.
3. **Sequential Lueders is an executed positive alternative.** Twelve successive commuting record projectors reproduce the sea Born diagonal in identity and reverse order; the chain rule proves the same for every order in the ideal exact model. Simultaneous recording is unnecessary. The locally redeclared unitary Model A at tau=.5 remains closer to the sea than MR, with the original TV numbers retained.
4. Sea-law matching and nondisturbance of the chosen corner dictionary are supplied objectives. Under those objectives MR fails and the conditional Z commutant is restrictive. This establishes neither a universal physical no-go nor a unique formation rule or basis.

## Reading, not theorem -- the whole thing in plain words

Replacing the state after each recording by a supplied block-ground state defines a finite model. It changes the conditional probabilities, so its final law differs from the chosen sea law. Ordinary sequential Lueders recording retains that law. Whether either construction describes permanent physical Records requires a placement, preparation, probability and formation bridge that this calculation does not supply.

## Interfaces named for other lanes, not settled here

- **The formation rate.** How often a record forms, and where, is outside this note; reading note (2) says the axioms supply neither, and `M_R` stipulates an order rather than
  deriving one. The corollary gives conditional comparisons, not a universal obligation on every formation proposal.
- **A Lindbladian stationary state.** The panel's referee lens -- a tick written as a dissipative generator whose stationary state is the sea, rather than as a replacement map -- is
  not computed as a physical mechanism. Fixed-record reset is linear CPTP and has the asymptotic Lindblad realization proved above; that mathematical fact does not select a sea stationary law.
- **Partial relaxation.** Ticks relaxing only partly, running a finite time towards the conditioned ground state rather than arriving, are possible additional protocols; no unique interpolation from the locally computed unitary A to MR is specified or executed here.
- **Larger regions.** The `3x3x3` cube, periodic boundaries, other fillings and other flux sectors are outside this note; the sea's degeneracy and the corner-star census both depend
  on the cluster.

## Remaining live routes

1. Whether the order spread of `T4` grows or saturates on larger clusters. The `0.727031250000` here is a maximum over `32` declared orders, and the true maximum over all `12!` orders
   is not computed.
2. Whether any tie-break other than `Pi/deg` and the `N`-superselected one makes `T5`'s charge spread vanish without a superselection rule added by hand; `M_R^N` adds one, and nothing
   here says whether something else does it.

## Executable claim block

```text
setting: supplied cube edge-qubit tensor carrier 4096; +face code 128 realizes even eight-mode Fock space; local Z recordings use ambient blocks
T1: P_R H P_R=P_R(-sum_{e not recorded}eta_e T_e)P_R; supplied reset state is a function of records
T2: chosen sea support 1984; charge zeros 1856 and cancellation zeros 256; flat record-block weights 2^-k for k<=3
T3: all 32 declared MR laws have support 4096; identity TV1283/2880; locally redeclared A(tau=.5) TV.324925160534
T4: identity/reverse TV1/3; declared maximum.727031250000 and minimum.113194444444; sequential commuting Lueders reproduces sea law
T5: retain original charge laws, means, degeneracy census 1456 and MR^N alternative with all 256 cancellation zeros lost
T6: retain all overlap and energy rows; energy formula is Lueders-weighted mean; drops subtract two differently weighted means; actual mask31 counterexample
T7: Z projective measurement up to labels only under supplied corner-parity nondisturbance; no physical basis-selection theorem
reset: fixed-record linear CPTP channel; normalized branch nonlinear; ideal reset is the stated Lindblad semigroup limit
status: corrected source for independent review; original 26 checks retained plus 3 domain/energy/reset controls; no author PASS or audit application
```

## Proof boundary

Every statement above is proved on **one finite cluster**, the `2x2x2` cube graph, in **one flux sector** (all-minus, the Kawamoto-Smit staggered signs) at **one filling** (the
half-filled sea, `N = 4`). Nothing is claimed for larger clusters, periodic boundaries, infinite lattices, other sectors, other fillings, or any law family other than the one in
"Definitions". The law is **designed**, not derived: the encoding is chosen so that the Majorana relations `R0`-`R4` hold, the face constraints make that consistent, and the parity
dictionary is one readout map among many, with no uniqueness claimed for either.

**The tick model is stipulated in full and derived from nothing.** All six choices -- the starting state, the declared order, Born odds at formation, replacement by the restricted
ground state, the `Pi/deg` tie-break, and permanence -- are declared here, not taken from any axiom. Reading note (2) is explicit that the axioms supply no formation site, probability
or rate, and they supply no relaxation clause either; this note supplies none and declares one instead. **Nothing here says what the framework's tick is**, and nothing here forecloses
any tick. This is an obstruction for **one stipulated tick model**: a different formation rule, a different tie-break, a partial relaxation, or a dissipative generator with the sea as
its stationary state are all untouched above, and several are named as interfaces. The panel's candidate sentence is a candidate wording and is not called wrong here; what is reported
is what `M_R`, one way of making it definite, does and does not do.

The order-dependence figure of `T4` is a maximum over **`32` declared orders**, written out in the runner, and is a **lower bound** on the spread over all `12!` orders, labelled so
everywhere it appears. The `Pi/deg` tie-break is a further declared choice, and `M_R^N` is reported alongside because it changes the charge conclusion. The `p`-variant of PR
#7876 is touched only at its `p = 1` boundary. Every line not tagged `[exact]` is a **deterministic double-precision evaluation** of an exactly specified quantity at the stated
threshold: MR enumerates 4096 leaves with no sampling; the separate unitary/Lueders recursion omits relative branches at or below 1e-15. Block states come from diagonalisation, so these are numerical comparisons rather than exact rational certificates. There is **no seed anywhere** in this note or its runner and no Monte Carlo section. No absolute unit appears anywhere, no axiom text is amended, extended, reworded or
reinterpreted, no new framework axiom is adopted; the stated model hypotheses are supplied, no status value is set, and no authoritative status or registry is changed by this source.

## Review record

The September3 note, both historical/original runner outputs and all original 26 checks remain recoverable through the dated correction history. The current runner retains those 26 identities, strengthens only F5's false zero predicate and adds the explicit energy/reset/domain controls. Own-note and actual current memo bytes are declared and live-guarded inputs; no runtime helper or parent campaign is imported.

The source remains conditional. Sequential Lueders, charge-restricted reset, partial relaxation and dissipative constructions are distinct alternatives, some executed and some open. No N1 route quota, N2 wall independence or physical no-go follows from their names. Larger volumes, other flux/filling, physical roles and permanent formation remain open. Formal audit is deferred by the owner until a solid TOE; current review and integration belong to the coordinator and original independent reviewer.

The dated correction and exact original recovery identities are recorded outside active discovery in `.claude/science/relaxation-hierarchy-corrections-20260908/CORRECTION_HISTORY.md`.
