---
claim_id: the_seas_cancellation_zeros_are_a_determinant_criterion_closed_stars_only_on_flat_bands_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite supplied free Slater/Born and encoded-readout model. T1/T2 retain cube/slab determinant and many-body censuses. T3 retains all 48 slab inclusion-minimal sets of size at most N. T4 retains the exact determinant/support criterion and flat-band spectral reduction, with c>0; stars are sufficient examples, not all minimal supports. T5 retains the antiperiodic 4^3 minimum cardinality seven and its 64 minimizing stars, with complete executed connected-set keys; an exact eleven-site inclusion-minimal nonstar disproves the former whole-family claim. T6 preserves every determinant and the original 1e-12 cutoff, which flags 36/56 BALLS20 sets. A separately declared post-review smallest-eigenvalue diagnostic supports numerical positive margins with reported residuals, not an exact nonsingularity or infinite-volume theorem. No parent campaign or physical locality/formation supplier is accepted."
upstream_dependencies: []
runner: scripts/sea_cancellation_zeros_determinant_criterion_check_2026_09_03.py
---

# The sea's cancellation zeros: determinant criterion, finite minimum supports and numerical limits

**Date:** 2026-09-03
**Type:** bounded_theorem
**Conditions:** one supplied law, one supplied vacuum and one restated conditional update clause
**Audit:** unset; formal audit is deferred until a solid TOE.
**Status:** current conditional source, awaiting independent correction confirmation. No applied audit status is changed.
**Primary runner:**
[`scripts/sea_cancellation_zeros_determinant_criterion_check_2026_09_03.py`](../scripts/sea_cancellation_zeros_determinant_criterion_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/sea_cancellation_zeros_determinant_criterion_check_2026_09_03.txt`](../logs/runner-cache/sea_cancellation_zeros_determinant_criterion_check_2026_09_03.txt)
**Premises:** the mathematical model is redeclared below. The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) constrain its interpretation; no unselected parent theorem is accepted through a historical quotation.

A result in this lane, open at PR #7883, found that the sea's set of records carries a determinantal law with the sea's own one-particle projector `P` as its kernel, and counted its exact zeros: `8` of `70` corner patterns on the open `2x2x2` cube and `120` of `924` on the open `2x2x3` block. A second, open at PR #7895, identified the cube's `8` as **exactly the closed corner stars** `{v} u N(v)`, and a third, open at PR #7902, showed that the corner property behind them is a flat-band condition, `h^2 = 3I`. What none of them settled is the question this note asks: do those cancellation zeros exist at all beyond the cube, and what is their exact rule? The answer is that the rule is a **determinant criterion on the sea's own correlations** -- a corner set has zero odds for the all-occupied pattern exactly when the empty band carries a state living entirely inside that set -- and that flat bands supply closed-star examples but do not classify all inclusion-minimal supports. The zeros generalise as a criterion but not as a family: one cube taller they are a different family, on the antiperiodic `4^3` torus the minimum-cardinality examples are closed stars, and the larger-torus scan needs the distinct determinant-cutoff and eigenvalue-margin qualifications below.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster statements plus finite floating-point computations and two complete enumerations, every one conditional on one named supplied law, one named supplied vacuum and one update clause stipulated upstream and on nothing else. The combinatorial statements, the set equalities, the coset structure and the integer identities h^2 = 3I and h^2 = 6I are exact at zero tolerance; the Born census, the determinants and the spectral scans are finite floating-point computations on integer data, each reporting its residual against a tolerance declared before the run; the 6^3 and 8^3 statement is a bounded scan and is written as old cutoff and separate numerical-margin diagnostics."
trace_class: frontier_discovery
target_claim_id: the_seas_cancellation_zeros_are_a_determinant_criterion_closed_stars_only_on_flat_bands_bounded_theorem_note_2026-09-03
target_blocker_text: "The finite supplied model does not derive its physical law, state, readout or formation dynamics."
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Confirm the corrected conditional source independently; formal audit is deferred until a solid TOE. Physical suppliers and limiting questions remain open."
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`: `T1` (`A`) the cube control; `T2` (`B`) the `2x2x3` slab's full `2^20` census; `T3` (`C`) the failure of the closed-star description one cube taller; `T4` (`D`) the criterion, its mechanism, and its flat-band collapse; `T5` (`E`) the antiperiodic `4^3` torus and the complete enumeration that makes the closed stars the minimum-cardinality family there; `T6` (`F`) the `6^3` and `8^3` tori, where all closed-star minors exceed the old cutoff and only the separately qualified numerical diagnostics are asserted. Each carries its own tag: `[exact]` where the arithmetic is integer, combinatorial or a set equality, and `[numerical]` with a stated tolerance where it is floating point.

## Imports and authority

Historical quotations and PR references below refer to the original dated sources identified in `.claude/science/sea-corner-corrections-20260908/CORRECTION_HISTORY.md`; they do not assert that a branch is still open or that its current source is accepted. The finite definitions used in the proofs are restated here. The current minimal-axiom memo is a live interpretation boundary, distinct from those quotations.

Imported scientific authority: none load-bearing. Determinantal point processes, the fact that a free-fermion ground state's occupation law is one, compact localized states on flat bands, the Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering and the twist convention on a finite torus are standard methodology; every object is redeclared here and the runner recomputes every statement from the hopping signs up, importing nothing from this repository. The many-body census is built in the encoded record sector by sparse Lanczos and never from a Slater form, so the agreement with the determinant is a result and not a definition. The one supplied law, the one supplied vacuum and the update clause stipulated upstream are declared and quoted in "Setting"; they are conditions of the result, not graded dependencies, and this note cites no grade of any of them and consumes no row. Non-load-bearing context pointers, plain file names carrying no grade and no dependency weight: `MINIMAL_AXIOMS_2026-06-29.md`, from which the Record axiom and Admissibility's reading note (3) in "Setting" are quoted verbatim; `RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7883), whose determinantal law and zero counts this note recomputes independently; `A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7895), whose closed-corner-star identification this note reproduces and then bounds; `THE_CORNER_EIGENVECTOR_PROPERTY_IS_A_TWO_MODE_SPECTRAL_CONDITION_EXACT_ON_FLAT_BANDS_NOT_GENERAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7902), the flat-band mechanism whose `h^2 = 3I` is the same identity that drives Theorem 4; `JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_UNDER_THE_UNITARY_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7900), which counts zeros kept and lost; `A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7890), the source of the twist convention; and `EMERGENT_DICTIONARY_SELECTION_RULE_ZEROS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7842), quoted verbatim in "Setting" as the reading this note narrows.

## Setting

The framework axioms are quoted, not amended; the three this note leans on are given in full. **Lattice / Physical Locality**, verbatim: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." The lattice in the memo is physical. The vertices and edge qubits below belong to a supplied coarse graph; its physical realization is not established here. **Record / Fixed Reality**, verbatim: "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read." **Admissibility / Local Constraint**, verbatim: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Its reading note (3), interpretive and non-governing, is exactly what a zero of the odds instantiates and is quoted with it: "(3) The distribution is a probability measure on the local possibility domain; "available"/"admissible" denotes its support -- on finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure; Record locks a supported realization."

**The record ontology, as used.** Nothing below is read that is not a record. A record at a coarse site **registers** occupancy there; it does not report a value the site already carried. In the encoded picture the occupancy at a coarse corner is a readout of the records on that corner's incident coarse edge sites, `n_v = parity(z & incident_edges(v))`, so a corner condition is a condition on those records and on nothing else. Every zero below is a zero of the support in the sense of reading note (3): a corner pattern with zero odds is a pattern the finished set of records never registers.

**Supplied condition one -- the fermion law.** From `origin/physics-loop/emergent-3d-fermion-superlattice-existence`, its Proof boundary verbatim and outranking every summary: "The law of Theorems 1 to 3 is a **designed supplier model**: Admissibility fixes that there is one covariant nearest-neighbour rule and leaves its form to the supplier, and this note supplies one form and computes its consequences, deriving that form from no axiom and claiming for it no privileged status." This is historical attribution, not acceptance of that supplier. Its immediately adjacent qualification says the marker rule directly depends on a `5x5x5` window, and an adjacent-sites-only replacement is open. The finite matrices below are redeclared here; no nearest-neighbour physical realization is inferred.

**Supplied condition two -- the vacuum, and the law of records on it.** From PR #7883, its `claim_scope` verbatim and unbackticked as it stands there: "the finished set of records carries a determinantal law with kernel P", with "sum over full patterns of det P_S = 1 with 8 of 70 and 120 of 924 exact zeros and no negative value", on "the open 2x2x2 cube (8 modes, N = 4) and the open 2x2x3 block (12 modes, N = 6)" and the tori "4^3, 6^3, 8^3 at twists (1,1,1), (0,0,0), (1,1,1)". That note's own conditioning clause is quoted as it stands: "**The update clause is stipulated, not derived.** When a record forms with a given value, this note conditions the state in the Lueders form". This note stipulates nothing further; it takes that clause, that vacuum and that law as given and asks only what the zeros are.

**The description this note bounds.** From PR #7895, Theorem 2, verbatim: "`[exact, 1e-12 zero read]` At `p = 1`, where every site registers before anything else happens, the finished set is the sea's Born diagonal: support `1984 = 62 x 32`, and `2112` zeros splitting as `1856` **charge zeros** (every pattern with `N != 4`) plus `256 = 8 x 32` **cancellation zeros**. The `8` corner-occupation patterns carrying the cancellation zeros are **exactly the `8` closed corner stars** `{v} u N(v)`, one per corner". Theorem 1 below reproduces that census exactly and independently.

**The mechanism this note extends.** From PR #7902, verbatim: "Flat bands are **sufficient**: `h^2 = c I` gives `h = sqrt(c)(P_+ - P_-)`"; "The pi-flux cube has `h^2 = 3 I` exactly -- each face's two 2-step paths cancel under flux `-1`"; and, from its Corollary, "**It is not general.** It fails at the eight degree-`3` corners of the `2x2x3` slab and at **every** corner of the periodic slab". Theorem 3 below finds the same eight corners failing, from the zeros rather than from the eigenvector condition, and Theorem 4 supplies the criterion of which both are instances.

**The twist convention.** From PR #7890, Definitions, verbatim: "A finite torus carries a **twist** `tw in {0,1}^3`, `tw_a = 1` negating the links crossing the `a`-boundary; the **energy-minimising twist** minimises `E_{V/2} = -(1/2) tr sqrt(M^2 + m^2)`", and its Theorem 3 item (4), verbatim: "`M^2 = 6 I` exactly on the antiperiodic `4^3`". Theorem 5 recomputes that identity at zero residual and reads its consequence for the zeros.

**The reading this note narrows.** From PR #7842, its title verbatim: "The emergent dictionary reproduces the three-dimensional selection-rule zeros, from single-vertex neighbourhood conditions alone". Its Corollary item 1, verbatim: "The zero sets that `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7833) identifies as the readable shadow of a cross-site sign -- `12` of `70` on the cube, `8` of `84` on the `3x3` grid, same value multisets -- are reproduced here on an **ordinary-composition** edge-site lattice, the plain tensor product throughout with no graded clause anywhere." And its Proof boundary, verbatim: "This note supplies a **dictionary, not a derivation of the exclusion law**. ... The exclusion is imported from the structure of the encoding, not deduced from any axiom." Two facts about that note are recorded here because they bound what follows: the phrase "selection rule" occurs in it only in its title, its `claim_id` and its runner and log filenames, never in a body sentence; and the zero sets it reproduces are the composition discriminator's `12` of `70`, not the sea's `8` of `70`. The bridge between the two is PR #7895's own cross-link, verbatim, whose subject there is the lattice: "never registers eight of the corner patterns at all -- the forbidden patterns PR #7842 and PR #7883 exhibit from the dictionary side." It is that bridged reading -- that the cube's forbidden patterns are the lattice registering a known rule of three-dimensional physics -- which the Corollary narrows.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P6`. `P0`, declared here and conditional: the supplied law, the supplied vacuum, the Kawamoto-Smit sign field, the twists, the two open clusters, the three tori, the update clause stipulated upstream, and the original thresholds and the separately declared post-review margin diagnostic. `P1` (`A`): the cube control. `P2` (`B`): the slab's `2^20` census. `P3` (`C`): the failure of the closed-star description on the slab. `P4` (`D`): the criterion, its mechanism and its flat-band collapse. `P5` (`E`): the antiperiodic `4^3` torus. `P6` (`F`): `6^3` and `8^3`. `P3` uses `P2`'s zero list; `P4` uses `P1` and `P2` for the many-body side of the determinant law; `P5` and `P6` use `P4`'s criterion only, at one-particle cost.

## Definitions

A **cluster** is either of two finite open blocks with Kawamoto-Smit signs and no wrap -- the `2x2x2` **cube** (`8` corners, `12` edge sites, `N = 4`, `70` corner patterns at `N`) and the `2x2x3` **slab**, open in `z` (`12`, `20`, `6`, `924`) -- or one of the tori `4^3`, `6^3`, `8^3` with those signs and a declared twist. The **KS sign** of the bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`; a **twist** `tw_a = 1` negates the bonds crossing the `a`-boundary. With `H = -t sum_e eta_e T_e` at `t = 1` the one-particle matrix is `h_ij = -eta_ij`, and

```text
N       = V/2                                                    the sea's mode count
P       = the orthogonal projector onto the N lowest eigenvectors of h
P_T     = the |T| x |T| principal submatrix of P on the corner set T
star(v) = {v} u N(v)                                             a set of VERTICES
incident_edges(v) = bit mask of the EDGES incident to v             a different carrier
n_v(z)  = parity(z & incident_edges(v))                            edge-bit readout
```

A **record** at an edge site registers a bit; a finished set of records is `z in {0,1}^E`, and its **corner-occupation pattern** is `n(z)`. The map `z -> n(z)` is `F_2`-linear onto the even-weight subspace with kernel the cycle space, so each realised corner pattern carries a **coset** of `2^{E-V+1}` records. **The odds** of a record set are its Born weight in the sea. A **charge zero** is a record set with `N(z) != N`; a **cancellation zero** is a record set at `N(z) = N` whose odds still vanish. A corner set `T` is **singular** when `det P_T = 0`. A band is **flat** when `h^2 = cI`. The historical `REL_TOL=1e-20` relative Born census and `DET_TOL=1e-12` absolute minor cutoff remain unchanged. The old runner also used `GEO_TOL=0.20` for geometric means, which is not the same singularity criterion. The correction reports both old diagnostics, including the actual BALLS20 cutoff failures. A **new post-review** `MARGIN_TOL=1e-8` diagnostic compares the smallest principal eigenvalue against that margin, reporting eigensystem, orthogonality, commutator and projector-idempotency residuals below `1e-10`. These ordinary floating-point checks are not directed-rounding certificates of exact nonsingularity.

## Theorem 1 -- the cube control, reproduced independently

**Conclusion.** On the open `2x2x2` cube, with the sea built by sparse Lanczos in the encoded record sector and never from a Slater form:

1. `[exact]` `V = 8` corners, `E = 12` edge sites, cycle-space dimension `E - V + 1 = 5`, so each corner pattern carries a coset of `32` records; all `6` face fluxes are `-1`; the record sector has `2240` states.
2. `[numerical, 1e-11]` `E_sea = -6.928203230276 = -4 sqrt 3`, matching the sum of the `4` lowest one-particle levels, `H`-residual `3.8e-14`, Fermi gap `3.464101615 = 2 sqrt 3`, so the sea is a unique Slater determinant; the vector is stabilised by all `5` generators at residual `0.000e+00`.
3. `[numerical, exact]` The odds are **exactly constant on cycle-space cosets**: the maximum relative spread within a coset is `0.000e+00`. Every zero is therefore a whole coset of `32` records.
4. `[numerical, 1e-20 relative]` The histogram of `p / p_max` over the `2240` strictly positive entries is **bimodal**: `256` below `1e-30`, `1984` at or above `1e-2`, and `0` in the `28` decades between. The declared threshold sits in an empty span with ten decades of clearance on each side.
5. `[numerical, 1e-20 relative]` Support `1984` of `4096`; charge zeros `1856`; cancellation zeros `256`.
6. `[exact]` Those `256` are `8` corner patterns `x 32` records, and the `8` are **exactly the `8` closed corner stars** `{v} u N(v)`, each labelled twice -- as `star(v)` all-occupied and as `star(v-bar)` all-empty. That double labelling is why `8` stars give `8` patterns and not `16`.

**Proof.** The encoding is rebuilt from the edge graph and audited (`R0`-`R4`, and an independent stabilizer generating set) before anything else runs; the record sector is enumerated exactly; the ground vector is obtained by sparse Lanczos from a **declared deterministic start vector**, `v0_j = cos(j) + i cos(0.7j + 1)`, code-projected -- there is no random draw anywhere in this note. The Born weights are read over all `2^12` records, binned into cosets by the corner readout, and compared against the `8` closed stars as an equality of two `8`-element sets of `F_2^8` vectors, with no tolerance in it.

**Reading, not theorem.** The small cube's forbidden patterns are real and they are exactly the corners-with-their-neighbours. Everything after this asks whether that description is the rule or a coincidence of this one box.

## Theorem 2 -- the slab's full `2^20` census

**Conclusion.** On the open `2x2x3` slab, open in `z`, at `N = 6`:

1. `[exact]` `V = 12` corners -- `8` of degree `3` at the two `z`-boundary layers, `4` of degree `4` in the middle layer -- `E = 20` edge sites, cycle-space dimension `9`, coset size `512`, record sector `473088`.
2. `[numerical, 1e-10]` `E_sea = -10.828427124746 = -(8 + 2 sqrt 2)`, matching the one-particle sum; spectrum `(-2)^4 (-sqrt2)^2 | (+sqrt2)^2 (+2)^4`; Fermi gap `2.828427125 = 2 sqrt 2`, so the sea is unique; stabilised by all `9` generators.
3. `[numerical, exact]` The odds are again exactly constant on cosets, relative spread `0.000e+00`.
4. `[numerical, 1e-20 relative]` Of the `473088` strictly positive entries, `61440` lie below `1e-30`, **nothing** lies in the `26` decades from `1e-30` to `1e-4`, `96256` lie in `[1e-4, 1e-2)` and `315392` at or above `1e-2`.
5. `[numerical, 1e-20 relative]` Support `411648` of `1048576`; charge zeros `575488`; cancellation zeros `61440`.
6. `[exact]` Those `61440` are `120` corner patterns `x 512` records. The `120` of the `C(12,6) = 924` patterns at `N = 6` reproduces PR #7883's "`120` of `924`" -- reached here from the many-body vector rather than from the determinant, so the two routes to that count are independent.

**Proof.** The same pipeline as Theorem 1 at `2^20`: the sparse Hamiltonian is built edge by edge on the `473088`-dimensional record sector with no dense object anywhere, the Lanczos start vector is the same declared deterministic vector, and the Born weights are binned by corner readout with the coset sizes checked to be equal before any zero is counted.

**Reading, not theorem.** The cancellation zeros are not a cube artefact. They are there one cube taller, in quantity. What changes is which patterns carry them.

## Theorem 3 -- the closed-star description fails one cube taller

**Conclusion.** On the same slab:

1. `[exact]` The closed-star rule -- a corner pattern vanishes when it holds some closed star all-occupied or all-empty -- predicts `324` patterns against the `120` that vanish: **`204` false positives and `0` false negatives**. It is a necessary condition here and over-predicts by a factor `2.7`.
2. `[numerical, 1e-12]` The eight **degree-3** closed stars are **not singular**: `det P_star = 1.340413e-03` at every one of them, well above the declared `1e-12` cutoff. The four **degree-4** stars are singular, `|det P_star| <= 6.9e-18`.
3. `[numerical, 1e-12]` No corner set of size `<= 4` is singular (`0` of `12`, `66`, `220`, `495`). Among sets of size `<= N=6`, the inclusion-minimal zero-carrying sets are `12` of size `5` and `36` of size `6`, `48` in all.
4. `[exact]` Each of the `12` minimal five-corner sets is **one full `z`-column together with the two in-plane neighbours of one of its three sites** -- `4` columns `x 3` heights. Only the `4` middle-height ones coincide with a closed star; the other `8` are stars of nothing.
5. `[exact]` Each of the `36` minimal six-corner sets meets exactly `3` of the `4` `z`-columns, and each of those `3` in exactly `2` of its `3` heights: `9` height signatures `x 4` column triples.
6. `[numerical, 1e-9]` Of the `48` minimal sets only `8` have a single-band kernel direction -- `4` pure `+2`, the closed stars of the degree-`4` corners, and `4` pure `+sqrt2` -- while `40` **mix the `+sqrt2` and `+2` bands**. The zeros here are a two-band, non-eigenvector phenomenon.

**Proof.** The `120` are taken from Theorem 2's many-body census, not from the determinant, so the comparison against the rule is between a computed zero set and a combinatorial prediction. The rule's `324` are enumerated over all `924` patterns; the minimal sets are found by testing every principal minor at every size up to `N` and discarding any set with a singular proper subset; the structural statements are set identities over the four `z`-columns; the band content of each kernel direction is read from its expansion in the eigenbasis of `h` at a threshold declared before the run.

**Reading, not theorem.** One cube taller, the corners-with-their-neighbours picture stops describing the zeros. Eight of the twelve closed stars are not forbidden at all, and most of what is forbidden is not a star of anything.

## Theorem 4 -- the exact rule is a determinant criterion, and the closed stars are its flat-band case

**Conclusion.**

1. `[numerical, 1e-13]` **The criterion.** A corner set `S` with `|S| = N` has zero odds for "`S` occupied, complement empty" iff `det P_S = 0`, equivalently iff `det (I-P)_{S^c} = 0`. Checked as `det P_S = det (I-P)_{S^c}` on all `70` cube and all `924` slab patterns, maximum difference `1.1e-16` and `3.1e-17`, with the singular patterns equal to the Born zeros of Theorems 1 and 2 **as sets**, with no tolerance slack.
2. `[exact + numerical, 1e-13]` **The mechanism.** For `|T| <= N`, `det P_T = det(W_T W_T^dag)` vanishes iff the rows of `W` indexed by `T` are dependent, i.e. iff some `c` supported on `T` has `P c = 0`: **`det P_T = 0` iff the empty band carries a nonzero state supported inside `T`**, and dually `det (I-P)_T = 0` iff the occupied band does. On all `56` minimal singular sets of the two clusters the kernel direction has support exactly `T` and `||P c|| <= 6.3e-16`.
3. `[exact]` **The cube is flat**: `||h^2 - 3I|| = 0.0e+00`, each face's two `2`-paths cancelling under flux `-1`.
4. `[exact]` **The slab is not.** `h^2` has diagonal `deg(v)` -- values `{3, 4}` -- and exactly **four unordered pairs (eight ordered off-diagonal entries)**, all `1`, at `(0,2)`, `(3,5)`, `(6,8)`, `(9,11)`: the two ends of each open `z`-column are joined by a **single uncancelled 2-path** through the middle site, with no partner path to cancel it against. `h^2` block-diagonalises over the four columns as `[[3,0,1],[0,4,0],[1,0,3]]`, eigenvalues `{4,4,2}`, giving `spec(h^2) = 2^4 4^8`. **That single uncancelled path is what removes the boundary stars.**
5. `[exact + numerical, 1e-9]` **The flat-band corollary.** If `h^2 = cI` with `c>0` the empty band is the `+sqrt c` eigenspace and the criterion collapses to `det P_T = 0` iff `lambda_max(h_T) = sqrt c`. Forward, restriction gives `h_T c_T = sqrt c c_T`; back, the top eigenvector of `h_T` padded by zeros has Rayleigh quotient `lambda_max(h)`, so it is a global maximiser and hence an eigenvector. The two sides agree on all `162` cube corner sets of size `<= N`, `0` mismatches. Because `lambda_max` of a disconnected set is the maximum over its components, **minimal singular sets are connected**.
6. `[numerical, 1e-13]` **Closed-star solutions are realised.** `(sqrt c + h) e_v` is an `h`-eigenvector at `+sqrt c` supported exactly on `star(v)`, since `h^2 e_v = c e_v`. On all `8` cube corners the relative residual is `<= 1.8e-16`, the support is the closed star every time, and `|det P_star| <= 2.2e-17`.

**Proof.** Item 1 evaluates both determinants on every pattern and compares the singular set against the Born zero set as sets. Item 2 is one line of linear algebra, confirmed on every minimal set by exhibiting the kernel direction and its support. Items 3 and 4 are integer residuals and an exact entry census of `h^2`. Item 5 is the two-line argument above, checked against the determinant on every cube subset of size `<= N`. Item 6 evaluates the closed form and its support directly.

**Reading, not theorem.** The forbidden patterns are a property of the vacuum's own correlations, not of the shape of a neighbourhood. A set of corners has zero odds of all being occupied exactly when the empty band has a state living entirely inside that set. On a flat band, that condition reduces to a purely combinatorial one, and it supplies closed-star solutions but not an exhaustive inclusion-minimal family.

## Theorem 5 -- the antiperiodic `4^3` torus: minimum cardinality seven, not all minimal supports

**Conclusion.** On the `4^3` torus with Kawamoto-Smit signs:

1. `[exact]` At twist `(1,1,1)` all `192` plaquette fluxes are `-1`, the Polyakov loops are `[-1,-1,-1]`, and `||h^2 - 6I|| = 0.0e+00`. The mechanism is the twist itself: at `L = 4` the vertices `v + 2e_a` and `v - 2e_a` are the **same** vertex, so the two length-`2` paths joining `v` to it multiply to the `a`-Polyakov loop, which the twist sets to `-1`; they cancel and `h^2` stays diagonal.
2. `[numerical, 1e-9]` The sector is gapped: spectrum `+-sqrt 6`, `32` each, Fermi gap `4.898979486 = 2 sqrt 6`, so the sea is a unique Slater determinant and the criterion has one `P`.
3. `[numerical, 1e-12]` All `64` closed corner stars, `7` corners each, are singular; `max |det P_star| = 3.759e-18`.
4. `[numerical, complete enumeration, 1e-9]` Over **all `1391280` connected corner sets of size `2` to `7`** -- `192`, `960`, `5360`, `31680`, `191104`, `1161984`, each generated exactly once -- `max lambda_max(h_T) = sqrt(k-1)` at every size `k`. So nothing of size `<= 6` attains `sqrt 6`, and the minimum singular support is `7`.
5. `[exact set equality]` At size `7` exactly `64` of the `1161984` connected sets attain `sqrt 6`, and they are **precisely the `64` closed corner stars**.
6. `[numerical, 1e-9]` The **periodic** `4^3` sector has no unique sea to ask the question of: Polyakov loops `[1,1,1]`, `8` exact zero modes at `q = (pi, pi, pi)`, Fermi gap `1.5e-16`, so there is no single `P`.

**Proof.** The torus is rebuilt from the sign field and the twist, and both the fluxes and the Polyakov loops are computed rather than assumed. The identity `h^2 = 6I` is an integer residual at zero tolerance. Actual executed keys are checked for unique vertices, connectivity and distinctness, alongside the original expected counts; the same generator is compared with independent brute force on all 150 connected cube subsets of sizes 2..6. The enumeration is an exclusive-neighbourhood walk that grows every connected set from its least element and offers a corner only if it is not already in the closed neighbourhood of the set, so each set is reached exactly once: at each step the ordered frontier assigns a connected extension to its earliest offered vertex, while the exclusion set prevents that vertex being reintroduced along a later branch. The counts and actual unique keys are reported and the top eigenvalue of each induced signed subgraph is computed in batches. Item 5 is an equality of two `64`-element sets of corner tuples.

**Exact correction beyond the enumerated sizes.** The minimum-cardinality statement is preserved. It does not classify all inclusion-minimal supports. On this same matrix,

`T={0,2,3,4,5,12,13,16,17,48,49}`

has `det P_T=0` and all eleven single-deletion minors positive. The actual signed matrix is integer, bipartite and obeys `h^2=6I`; split the set into parity blocks and evaluate `det P_T=2^(-|T|)det(I-BB^T/6)` with rational arithmetic. Positivity of all single-deletion minors and positive semidefiniteness prove inclusion-minimality. No closed star is contained in `T`. Thus the former all-minimal-star claim is false, while the `<=7` census and its minimum-cardinality conclusion stand. The nonflat slab's middle-layer stars also show flatness is sufficient, not necessary for a star solution.

## Theorem 6 -- `6^3` and `8^3`: retained cutoff failures and a separate margin diagnostic

**Conclusion.** On the `6^3` and `8^3` tori with the same sign field:

1. `[numerical, 1e-9]` The gapped sector is twist `(0,0,0)` at `6^3`, gap `3.464101615`, and `(1,1,1)` at `8^3`, gap `2.651308592`; the other twist carries `8` exact zero modes and gap `0` in each case. This is an independent reproduction of PR #7883's stated optimal twists `(1,1,1)`, `(0,0,0)`, `(1,1,1)` for `4^3`, `6^3`, `8^3`.
2. `[numerical, 1e-9]` Neither gapped sector is flat: `||offdiag(h^2)|| = 3.600e+01` on `6^3` and `5.543e+01` on `8^3`. For `L >= 6` the vertices `v + 2e_a` and `v - 2e_a` differ and each is reached by a single `2`-path, so nothing cancels -- the same failure as at the slab's open boundary, now on a torus.
3. `[numerical, 1e-12]` **No closed corner star falls below the original cutoff in either sector**: `det P_star` is uniformly `3.323e-04` across all `216` stars of `6^3` and `3.756e-04` across all `512` of `8^3`, well above the declared `1e-12` cutoff, and the flat-band state `(lambda_max + h) e_v` fails with relative residual `1.528` and `1.216`.
4. `[numerical, complete enumeration]` Every connected corner set of size `<= 5` on `6^3` (`648`, `3240`, `18576`, `115344` sets) and of size `<= 4` on `8^3` (`1536`, `7680`, `44032`) gives `min |det P_T| = 2.101e-01, 8.511e-02, 2.897e-02, 1.107e-02` and `2.103e-01, 8.534e-02, 2.913e-02`. The per-corner geometric mean `|det P_T|^(1/|T|)` never falls below `0.406`: the stated finite values, above the original cutoff in this size range.
5. `[numerical, declared fixed family]` Two **declared fixed families** of larger sets, one set per corner and no random draw anywhere -- `BALLS(m)`, the `m` corners nearest a corner in the order (`L1` distance on the torus, then index), for `m = 7, 10, 15, 20`; and `COLUMN+`, a whole `z`-column together with the two in-plane neighbours of one of its sites, the shape of the slab's minimal five-corner sets transplanted -- give a minimum `|det P_T|` per family of `3.32e-04`, `1.01e-05`, `3.34e-09`, `2.83e-13` for `BALLS(7, 10, 15, 20)` and `5.82e-04` for `COLUMN+` on `6^3`, and `3.76e-04`, `1.16e-05`, `4.71e-09`, `5.03e-13` and `9.54e-05` on `8^3`, with the per-corner geometric mean never below `0.236`. These are size-dependent diagnostic values; they do not establish a decay law or an exact zero exclusion.

**Correction to the old classification.** Under the original absolute `DET_TOL=1e-12`, BALLS20 flags `36/216` sets on `6^3` and `56/512` on `8^3`. The minima `2.83088e-13` and `5.02891e-13` were already printed in the old cache. Calling that entire scan clear of its declared cutoff was wrong. The geometric means above are preserved as diagnostic data, not substituted for the cutoff. Separately, the new minimum-principal-eigenvalue diagnostic is positive (about `1.24e-4` and `2.35e-4` for BALLS20) with the reported residual checks; it supports numerical positive margins only. Exact singularity, finite-precision uncertainty beyond these diagnostics and sets outside the scanned range remain distinct questions.

**Proof.** Both twists are built for both tori and the gapped one is identified from the spectrum rather than assumed. The star census evaluates every closed star's minor. The size-bounded scans use the same exclusive-neighbourhood enumeration as Theorem 5, with the counts reported. The two larger families are declared in the runner's own source and depend on no seed and no draw. The old geometric means are retained for comparison. A positive floating-point determinant or geometric mean alone cannot certify an exact zero exclusion. The new eigenvalue calculation reports its residual diagnostics without silently replacing the old cutoff.

**Reading, not theorem.** The larger-torus star minors are far above the old cutoff. Some larger-family minors are below it; the separate eigenvalue diagnostic explains why an absolute determinant cutoff can be misleading, but is not an exact-arithmetic theorem.

## Corollary -- the criterion and its limits

1. For any supplied projection Slater law, a set has zero all-occupied probability iff its principal minor vanishes, equivalently iff an empty-band vector is supported there. The dual uses `I-P`. The criterion is exact; its numerical evaluation has the explicitly stated limits.
2. The retained finite cube/slab censuses and slab minimal-set structure remain useful. The antiperiodic `4^3` minimum size is seven with 64 minimizing stars; the exact eleven-site nonstar rules out the stronger inclusion-minimal-family classification.
3. The historical PR #7842 dictionary quotation and PR #7895 physical reading are not accepted parent proofs here. Their comparisons are historical context only; the present finite calculations do not establish a known physical selection rule on any lattice, including the cube.
4. Other notes' original counts and prose must be assessed in their own domains. This correction endorses no blanket downstream claim. The corrected four-note unit retains its explicit finite calculations with the scope qualifications stated in each note.
5. The large-torus old cutoff and separate margin diagnostic are both reported. No exact nonsingularity or infinite-volume theorem is supplied by those diagnostics.

## Reading, not theorem -- the whole thing in plain words

A determinant criterion describes the supplied sea's zero probabilities. Closed stars give some solutions; they do not give all minimal solutions. The finite larger-torus calculations require their numerical qualifications, and the physical interpretation still needs a supplier that this note does not provide.

## Interfaces named for other lanes, not settled here

- **The infinite-volume statement.** Everything here is finite: two open clusters and three tori, the largest a `512`-corner box. Nothing is said about `L -> inf`, and PR #7883's own caveat is inherited unchanged: "Everything here is finite: three tori and two open clusters."
- **Other fillings and other sectors.** Every statement is at `N = V/2` with the Kawamoto-Smit sign field at the declared twists. The criterion itself needs only a gapped Fermi level and would be asked the same way elsewhere; nothing here checks it there.
- **Whether any exact zero exists on the large tori beyond the scanned range.** Theorem 6 is a bounded scan with a declared range. A lane that wants the stronger statement inherits the criterion and the enumeration machinery, not a conclusion.
- **Interactions.** Everything here is free hopping, inheriting PR #7883's own free-hopping caveat. Nothing says what survives when the law is not quadratic in the modes.
- **The vacuum, the formation clause and the update clause.** All three are stipulated upstream and untouched. This note supplies no formation site, probability or rate, and decides nothing about which state the framework's vacuum is.

## Remaining live routes

1. Whether the criterion has a closed-form answer on a large torus -- which corner sets, if any, can hold a state of the empty band -- or whether the answer there is genuinely empty. Theorem 6 narrows the question to a scan and does not answer it.
2. Whether any physical reading survives for the flat-band zeros themselves. They are exact, they are stable on the two flat geometries, and Theorem 4 says what they are; what they mean, if anything, is left where PR #7842 and PR #7895 left it.

## Executable claim block

```text
conditions: redeclared free hopping, chosen half-filled Slater sea, Born/Lueders interpretation and encoded readout; no parent or physical supplier acceptance
T1/T2: original cube/slab many-body and determinant censuses and numeric tables retained
T3: slab 48 inclusion-minimal supports of size<=N,12 size5 and36 size6; four middle-layer stars remain despite nonflat bands
T4: det P_T=0 iff a nonzero empty-band vector is supported in T; dual for I-P; c>0 flatness reduces criterion to lambda_max(h_T)=sqrt(c)
T5: 4^3 antiperiodic minimum cardinality7; exactly 64 minimizing stars from 1391280 complete connected keys; eleven-site exact nonstar disproves all-inclusion-minimal-star claim
T6: original 1e-12 cutoff flags 36/56 BALLS20 rows; geometric-mean tests preserved as different diagnostics; new 1e-8 principal-eigenvalue margin with residuals<1e-10 is numerical only
carriers: star(v) is a vertex set; incident_edges(v) is the edge bit mask used by n_v(z)
limits: finite selected matrices, menus and tolerances only; exact larger-torus singularity and physical/formation/thermodynamic claims remain open
```

## Proof boundary

The fermion law is a **designed supplier model**, in that note's own words "deriving that form from no axiom and claiming for it no privileged status"; the vacuum is **supplied**, taken from a note that explicitly declines to decide whether it is the framework's; and **Lueders conditioning is stipulated upstream** and untouched here. Every statement above inherits all three: if any one is not the framework's, nothing above survives except as a statement about what was supplied. Nothing here is derived from any axiom.

Every result is at **finite volume** and on **free hopping**: two open clusters and three tori, the largest `512` corners, at `N = V/2`, with the Kawamoto-Smit sign field and the declared twists. Nothing is claimed for larger boxes, other boundary conditions, other sign fields, other fillings, or any law that is not quadratic in the modes.

**The `6^3` and `8^3` statement is a bounded scan and is written as one.** The complete enumerations are of every connected corner set of size `<= 5` on `6^3` and `<= 4` on `8^3`; beyond those sizes the scan is two declared fixed families, `BALLS(m)` for `m = 7, 10, 15, 20` and `COLUMN+`, one set per corner. The old cutoff flags some BALLS20 sets; the separately declared positive eigenvalue margins are numerical diagnostics, not exact zero decisions. The criterion of Theorem 4 remains an exact mathematical identity.

**No route is foreclosed.** This note supplies an exact criterion and narrows one reading of one computed result to the cluster it was computed on. It does not say that a physical reading of the sea's zeros is unavailable, and it does not say that the search for one is over; it says what the zeros are on the clusters examined and what was and was not found where.

**There is no random draw anywhere.** Every scan is either a complete enumeration -- with the counts reported, each set generated exactly once by an exclusive-neighbourhood walk -- or a declared fixed family written out in the runner's own source. The Lanczos start vector is a declared deterministic vector, not a seeded draw, and the old thresholds and the new post-review margin criterion are labeled separately and printed with the quantities they judge.

The arithmetic split is stated on every line. The combinatorial statements, the set equalities of Theorems 1, 5 and the entry census of `h^2` in Theorem 4 are **exact** at zero tolerance -- integer matrices and equalities of finite sets, with no floating point in the conclusion. The Born censuses, the determinants, the spectral scans and the residuals are double precision on integer-derived data at `1e-9` to `1e-20`, each printing what it is judged against.

**Nothing about formation dynamics follows.** No formation site, probability or rate is supplied, and none is implied. No mass, no coupling, no absolute unit and no dynamical clause appears anywhere. No axiom text is amended, extended, reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is created or edited.

## Review record

This is a corrected conditional source, not an applied audit verdict. The original 2026-09-03 notes, runner bodies, caches and all 108 original check identities are preserved by the dated correction record outside active documentation discovery. Its original Git heads recover the unchanged historical bodies. Numerical tables above retain their historical values unless a correction is expressly identified. The current cache records a genuine run of the final source; a zero exit or fresh fingerprint is not a proof of its scientific claims.

Each primary is standalone and declares its own note and the current minimal-axiom memo as mutable inputs. The memo is an interpretation boundary, not a derivation of the supplied Hamiltonian, state, Born rule, coarse-to-fine map or permanent Record formation. Historical parent titles and quotations are attribution only; their science has not been accepted here. No parent campaign is imported. Independent source confirmation and the coordinator's current-main mechanical gates remain separate; formal audit is deferred until a solid TOE.
