---
claim_id: record_statistics_of_the_half_filled_sea_are_determinantal_conditional_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite Slater/Born and encoded-readout mathematics on the two named open blocks and three tori. T1 retains the exact determinant and inclusion laws. T2 distinguishes three selected N=2 character Slaters, the rank-four one-particle union, and the normalized rank-three N=2 ground-manifold mixture. T3 is positive-probability Schur conditioning with complete finite order coverage. T4 retains unconditioned one-record responses and finite Fourier-grid fit diagnostics only. T5 retains opposite-sublattice additivity, uniform-support sufficiency and actual finite conditional effects; arbitrary forcing means a conditional diagonal is zero or one, with exact counterexamples to both former row-cover implications. No physical law, vacuum selection, fine-site formation, continuum of finite-menu odds, uncapped reach or thermodynamic exponent is derived."
upstream_dependencies: []
runner: scripts/record_statistics_of_the_half_filled_sea_are_determinantal_check_2026_09_03.py
---

# Record statistics of the half-filled sea are determinantal

**Date:** 2026-09-03
**Type:** bounded_theorem
**Conditions:** one supplied law, one supplied vacuum and one stipulated update clause
**Audit:** unset; formal audit is deferred until a solid TOE.
**Status:** current conditional source, awaiting independent correction confirmation. No applied audit status is changed.
**Primary runner:**
[`scripts/record_statistics_of_the_half_filled_sea_are_determinantal_check_2026_09_03.py`](../scripts/record_statistics_of_the_half_filled_sea_are_determinantal_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/record_statistics_of_the_half_filled_sea_are_determinantal_check_2026_09_03.txt`](../logs/runner-cache/record_statistics_of_the_half_filled_sea_are_determinantal_check_2026_09_03.txt)
**Premises:** the model is redeclared below. The [current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) constrain its interpretation; the supplied law, vacuum, Born rule and update clause are not derived from them. Historical quotations supply attribution only.

The historical empty-vacuum and half-filled-sea calculations motivate this comparison of two supplied states in a parity encoding. The finite half-filled Slater law is determinantal, and positive-probability conditioning uses its Schur complement. The original one-observation kernel rules do not extend unchanged to arbitrary histories. Finite Fourier fits and conditional counterexamples below state precisely what was computed; they establish neither a physical law of Records nor an asymptotic decay exponent.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems plus finite floating-point computations, every one conditional on one named supplied law, one named supplied vacuum and one stipulated update clause and on nothing else. Group A's exact half, group B and the commutation clause of group C are integer matrices, `Fraction` arithmetic and exact arithmetic in Q(sqrt3) and Q(sqrt2) at zero tolerance; groups C, D, E and the Fock half of A are finite floating-point computations on integer data, each reporting its residual against a tolerance declared before the run, and the decay exponent is a fitted local slope on a finite momentum grid and is labelled as such."
trace_class: frontier_discovery
target_claim_id: record_statistics_of_the_half_filled_sea_are_determinantal_conditional_bounded_theorem_note_2026-09-03
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

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`: `T1` (`A`) the finished set of records is determinantal with kernel `P`; `T2` (`B`) the empty vacuum's forbidden pairs are
determinantal zeros in closed form; `T3` (`C`) conditioning is the Schur complement, with the joint formula, the edge-record push-forward and order independence; `T4` (`D`) the reach -- the one-record shift `2 P_vu^2`, the
unconditioned selection census, and finite Fourier fit; `T5` (`E`) opposite-sublattice additivity, corrected forcing boundaries, and finite influence beyond the star. Each carries its own tag: `[exact]` where the arithmetic is integer, rational or in a
quadratic field, and `[numerical]` with a stated tolerance where it is floating point.

## Imports and authority

Historical quotations and PR references below refer to the original dated sources identified in `.claude/science/sea-corner-corrections-20260908/CORRECTION_HISTORY.md`; they do not assert that a branch is still open or that its current source is accepted. The finite definitions used in the proofs are restated here. The current minimal-axiom memo is a live interpretation boundary, distinct from those quotations.

Imported scientific authority: none load-bearing. Determinantal point processes, the fact that a free-fermion ground state's occupation law is one, the Schur-complement form of its conditionals, the Bravyi-Kitaev superfast
encoding, the Kawamoto-Smit staggering and the Bloch reduction of a periodic hopping matrix are standard methodology; every object is redeclared here and the runner recomputes every statement from the hopping matrix up,
building the many-body ground state in the Fock sector rather than assuming a Slater form so that the determinantal identity is a result and not a definition. The one supplied law, the one supplied vacuum and the stipulated
update clause are declared and quoted in "Setting"; they are conditions of the result, not graded dependencies, and this note cites no grade of any of them and consumes no row. Non-load-bearing context pointers, plain file
names carrying no grade and no dependency weight: `MINIMAL_AXIOMS_2026-06-29.md`, from which the four axioms and two reading notes in "Setting" are quoted verbatim;
`RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7858), whose results are quoted below as the contrast this note is drawn against and whose cube, encoding and forbidden
pairs Theorem 2 recomputes; and `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md`, the source of the filling and of the `M^2 = 6I` identity Theorem 5 uses.

## Setting

The four framework axioms are quoted, not amended. **Lattice / Physical Locality**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations
about each site." **Qubit / Site Possibility**: "Each site has a domain of local possibilities," whose "full one-site possibility domain has algebraic presentation `M_2(C)`."

**Admissibility / Local Constraint.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the
possibilities is determined by, and varies with, the nearest-neighbor conditions." Two of its reading notes (interpretive, non-governing) are exactly what this note instantiates and are quoted with it: "(2) Read with Record,
the distribution concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate." "(3) The distribution is a probability measure on the
local possibility domain; "available"/"admissible" denotes its support -- on finite menus, exactly the possibilities of nonzero probability. On a continuous domain, a supported exact point may have zero singleton measure;
Record locks a supported realization."

**Record / Fixed Reality.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." "Only records are readable. A readout value
is determined by record content alone. A site with no record cannot be read."

**The record ontology, as used.** Nothing below is read that is not a record. A record at a coarse site registers occupancy there; it does not report a value the site already carried. In the encoded picture the occupancy at a
coarse vertex is a readout of the six records on that vertex's incident coarse edge sites, `n_v = (1 - B_v)/2` with `B_v` the product of their six `Z` values, so a vertex condition is a condition on six records and on nothing
else. The distributions below are supplied finite Born/conditioning laws. Identifying them with physical formation odds in reading note (2), or their coarse outcomes with permanent fine-site Records, requires an additional supplier. The finite mathematical support uses the measure-theoretic meaning in reading note (3).

**Supplied condition one -- the fermion law.** From
`origin/physics-loop/emergent-3d-fermion-superlattice-existence:docs/EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md`, its Proof boundary verbatim and outranking
every summary: "The law of Theorems 1 to 3 is a **designed supplier model**: Admissibility fixes that there is one covariant nearest-neighbour rule and leaves its form to the supplier, and this note supplies one form and
computes its consequences, deriving that form from no axiom and claiming for it no privileged status." Everything below inherits a conditional model, not acceptance of that supplier. The next sentence in the historical supplier explicitly says its marker rule directly depends on a `5x5x5` window and leaves an adjacent-sites-only replacement open. No physical nearest-neighbour realization is established here.

**Supplied condition two -- the vacuum.** From
`origin/physics-loop/matter-above-the-half-filled-sea:docs/MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7879), verbatim: "the
half-filled staggered sea at its energy-minimising twist has `E_sea = -78.383672`, `-258.857540` and `-611.811768` on `4^3`, `6^3` and `8^3`", and "`<n_v> = 1/2` at EVERY site, exactly, because the bipartite grading
`eps_v = (-1)^{v1+v2+v3}` satisfies `eps M eps = -M` as a zero-residual integer identity, so `P_vv + (eps P eps)_vv = 1` and `P_vv = 1/2`." And, verbatim, what that note leaves open: "WHICH STATE IS THE FRAMEWORK'S VACUUM IS
NOT DECIDED HERE: it is named as a decision about the framework, for its owner, and the exact consequences of each choice are supplied." This note supplies one more consequence and decides nothing.

**The contrast, quoted.** From `origin/physics-loop/record-formation-emergent-vacuum:docs/RECORD_FORMATION_ON_THE_EMERGENT_VACUUM_PARITY_FORCED_ODDS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7858), on the **empty**
vacuum of the same encoding, verbatim: its allowed set "is uniform on a LINEAR subspace of `F2^E` of dimension `E - V + 1` -- `32` of `4096` at `p = 1/32` on the cube"; "The odds that a forming record locks the value `1` at a
site, given the records already present in its neighbourhood, are `1/2` or forced to `0` or `1` and never anything between"; "over all `66` cube site pairs x `4` values the odds elsewhere change in exactly the `96` cases where
the two records close a vertex star and never in the other `168`"; "Forcing is the cocircuit structure of the graph"; "The finished set of records carries the same odds whatever order the records formed in"; and, for the
coherent state, "the Slater ground state at `E = -4` has support `512 = 16` cosets uniform at `1/512` with `384` cancellation zeros = `12` cosets, exactly the corner pairs on one `x`-face". Those six statements are the
baseline every theorem below is set against.

**The update clause is stipulated, not derived.** When a record forms with a given value, this note conditions the state in the Lueders form: restrict to the eigenspace of that value at that site and renormalize. That is a
choice declared here, of a shape the record axiom permits, and it is the same clause PR #7858 stipulated, so the two notes are compared on equal terms. Nothing below claims it is taken from an axiom, and nothing below supplies
a formation site, probability or rate.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the supported scope is precisely `P0`-`P5`. `P0`, declared here and conditional: the supplied law, the supplied vacuum,
the KS sign field, the twists, the two open clusters, the three tori and the stipulated Lueders update clause. `P1` (`A`): the determinantal law and its kernel. `P2` (`B`): the empty vacuum's forbidden pairs as determinantal
zeros. `P3` (`C`): conditioning as the Schur complement, the edge push-forward, order independence. `P4` (`D`): the reach. `P5` (`E`): additivity, forcing, and the influence beyond the star. `P4` and `P5` use `P1` for the
kernel and `P3` for the conditional form; `P2` uses `P1`'s closed form only.

## Definitions

A **cluster** is either of two finite open blocks with Kawamoto-Smit signs and no wrap -- `cube`, the `2x2x2` block (`8` modes, `N = 4`, `70` patterns), and `block`, the `2x2x3` block (`12`, `6`, `924`) -- or one of the three
tori `4^3`, `6^3`, `8^3` with those signs and the energy-minimising twist. The **KS sign** of the bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`; a **twist** on axis `a` flips the
bonds crossing `v_a = L-1 -> 0`. `M` is the symmetric integer hopping matrix, `N = V/2`, and

```text
P     = the orthogonal projector onto the N lowest eigenvectors of M          the half-filled sea's kernel
P_S   = the |S| x |S| principal submatrix of P on the mode set S
n_v   = (1 - B_v)/2, B_v the product of the Z's on the six edge sites at v    the parity dictionary
```

A **record** at a mode registers occupancy there, so a full set of records is an occupation pattern `S`. The **odds at a site** are the probability that a record forming there locks the value `1`, given the records already
present. A law on patterns is **determinantal with kernel `K`** when `P(all of T occupied) = det K_T` for every set `T`. The **Schur complement** of `K` on a set `R` is `K_{rest} - K_{rest,R} (K_R)^{-1} K_{R,rest}`; conditioning
on `O` occupied uses it on `P`, and on `E` empty uses it on the hole kernel `I - P` and returns `I` minus the result. The **support of the kernel's row at `v`** is the set of `u != v` with `P_vu != 0`. A record set **forces**
the value at `v` when the conditional odds there are `0` or `1`. The **BKSF encoding** is the one PR #7858 declares, with qubits on the edge sites, `A_ij = X(edge ij)` times the `Z`'s ordered before it at both endpoints,
`B_v` the product of the `Z`'s incident to `v`, and the face loops as stabilizers; a **fibre** is one coset of its cycle space.

## Theorem 1 -- the finished set of records carries a determinantal law with kernel P

**Conclusion.** On the open `2x2x2` cube and the open `2x2x3` block:

1. `[numerical, 1e-15]` The many-body ground state built in the Jordan-Wigner Fock sector -- assembled from `H = sum_ij M_ij c^dag_i c_j` and diagonalized there, **not** from a Slater form -- is non-degenerate and satisfies
   `|<S|psi>|^2 = |det phi_i(s_j)|^2 = det P_S` on all `70` and all `924` patterns, and every `1`-, `2`- and `3`-point marginal `P(T occupied)` equals `det P_T`.
2. `[exact]` Over `Q(sqrt3)`, where `M^2 = 3I` is an integer identity and hence `P = (I - M/sqrt3)/2`, and over `Q(sqrt2)`, where the spectrum `{+-2, +-sqrt2}` gives `P` by spectral idempotents: `P = P^2 = P^T`, `tr P = N`,
   and `P_vv = 1/2` at **every** site.
3. `[exact]` The sum of `det P_S` over full patterns is exactly `1`, no value is negative, and the marginal identity `sum_{S contains T} det P_S = det P_T` holds on every `1`-, `2`- and `3`-subset (`8 + 28 + 56` and
   `12 + 66 + 220`) with `0` mismatches. So the law is a genuine probability law and it is the determinantal one.
4. `[exact]` The cube's value multiset is `{1/144 x30, 1/48 x24, 0 x8, 1/36 x6, 1/16 x2}`; the exact zeros are `8` of `70` and `120` of `924`. No **pair** minor vanishes on either cluster: a forbidden pair needs
   `|P_uv| = 1/2` and the largest off-diagonal entry is `0.2887` and `0.3018`.

**Proof.** The hopping matrices are integer, so `M` is exact; the Fock sector is built combinatorially with Jordan-Wigner signs and diagonalized, and its ground vector's squared amplitudes are compared entrywise against the
Slater determinant and against `det P_S`. The exact half rebuilds `P` in a quadratic field -- on the cube from the verified identity `M^2 = 3I`, on the block from the four spectral idempotents -- and every determinant, sum
and marginal is a Gaussian elimination over `Q(sqrt d)` with `Fraction` coefficients, with no floating point anywhere in items 2 to 4.

**Reading, not theorem.** On this vacuum the finished set of records has a law with a single object behind it: the sea's own projector. Which patterns of records the law allows, and with what weight, is read off from
determinants of that one matrix, and the sites are no longer independent of each other in the way a parity subspace makes them.

## Theorem 2 -- the empty vacuum's forbidden pairs are determinantal zeros, in closed form

**Conclusion.** For the plain-adjacency `2x2x2` cube of PR #7858 in its `N = 2` sector, whose many-body ground energy is `-4` with degeneracy `3` over the `28` cosets:

1. `[exact]` Each of the three **declared character-basis** `E = -4` Slater states has a rank-`2` kernel whose pair minors take exactly two values, `det P_uv = 0` on `12` pairs and `1/16` on `16`, in the closed form `det P_uv = P_uu P_vv - P_uv^2`. For
   the `(chi_111, chi_011)` state the `12` vanishing pairs are exactly the corner pairs sharing an `x`-face -- PR #7858's own list.
2. `[exact]` Pushed through the parity dictionary, whose `128` cosets are a bijection onto the even-parity vertex patterns and each of which is a fibre of `32` edge-record patterns, the `16` nonvanishing vertex patterns give
   support `512` uniform at `1/512` and the `12` vanishing ones give `384` cancellation zeros: PR #7858's census, recovered from `P` alone.
3. `[exact]` The original rank-`4` **one-particle union** projector onto `(chi_111, chi_011, chi_101, chi_110)` has `0` vanishing pair inclusion minors of `28`, the smallest being `3/16`; their sum is `6`. Filling that subspace is an `N=4`, `E=-6` Slater. It is not the `N=2`, `E=-4` ground-manifold projector.
4. `[exact, correction]` The latter many-body eigenspace has rank `3`. Its normalized projector has full-pair weights `1/48, 1/24, 1/16`, summing to `1`, with no zero. A normalized ground Slater using second orbital `(chi_011+2 chi_101+4 chi_110)/sqrt(21)` also has no forbidden pair: twelve zeros is not a claim about every ground Slater. The current runner constructs these quantities explicitly while retaining the old union minors.

**Proof.** The kernels are `Phi Phi^T` for hypercube characters `chi_S/sqrt8`, so every entry is a rational with denominator `8` and every minor is computed with `Fraction`; the closed form is checked against the direct
`2 x 2` determinant on all `28` pairs of all three states; the fibre size and the bijection are read from the encoding's stabilizer group by exhaustion. All exact.

**Reading, not theorem.** PR #7858 found that a record pattern can fail to form for two different reasons, one belonging to the model and one to the state, and that its second kind of zero belonged to the state. Here the
second kind has a formula: a pair is forbidden exactly when the `2 x 2` determinant of the state's kernel on that pair vanishes. The two vacua share the mechanism and differ in whether it fires.

## Theorem 3 -- conditioning is the Schur complement

**Conclusion.** Under the stipulated Lueders clause:

1. `[numerical, actual 1e-12 odds / 1e-10 determinant checks]` For records at an occupied set `O` and an empty set `E`, the conditional odds at every remaining site equal the diagonal of the Schur complement -- of `P` for the occupied records, of `I - P` for the
   empty ones. Against explicit Lueders conditioning of the exact state: `16` and `112` conditions on the cube (`112` and `672` odds compared, ranges `[1/3, 2/3]` and `[1/6, 5/6]`), `24` and `264` on the block (ranges
   `[0.3179, 0.6821]` and `[0.1357, 0.8643]`), `0` mismatches.
2. `[numerical, actual 1e-12 odds / 1e-10 determinant checks]` On every one of those cases the joint law is `P(A occ, B empty) = (-1)^|B| det (P - 1_B)_{A u B}`, the odds are the determinant ratio `P(A + v, B) / P(A, B)`, and each conditional kernel is itself an
   exact projector of rank `N - |O|`: conditioning preserves the Slater class on the remaining modes, of rank `N-|O|`; an empty observation removes no particle.
3. `[numerical, 1e-16 fibre / 1e-14 odds]` The same law at the edge sites. On the BKSF cube the encoded state is uniform **within** each of the `128` fibres with fibre total `det P_S`; one edge record (`24` cases) leaves mass exactly
   `1/2` and two (`264` cases) mass exactly `1/4`, and in both the odds at every vertex stay at `1/2`; a full vertex **star** of edge records (`64` assignments, all reachable) induces exactly the determinantal conditional on
   `n_v = parity(star)` and nothing beyond it.
4. `[exact + numerical, 1e-14]` All `12` `Z_e` commute pairwise in the symplectic representation, and sequential Schur conditioning on all `448` three-record conditions (56 site triples times 8 value assignments) in all `6` orders gives `2240` comparisons with `0`
   mismatches: the finished set of records carries the same odds whatever order the records formed in.

**Proof.** The exact state is held explicitly, restricted to each record pattern and renormalized, and its site marginals are compared entrywise against the Schur-complement diagonal and against the determinant ratio; the
joint identity is evaluated as a signed determinant on the union; idempotency and trace of each conditional kernel are checked directly. The edge-level statements build the encoded state on all `4096` patterns from the
encoding's own coset structure with a fixed pseudorandom phase per coset, and condition on edge records by restriction. The commutation is exact in the symplectic representation; the order census walks each order explicitly.

**Reading, not theorem.** A record joins what the site can see, and the way it enters is fixed: the kernel is reduced by a Schur complement. Two records taken in either order leave the same odds, and a set of edge records
smaller than a full star around a corner leaves the odds at that corner exactly where they were.

## Theorem 4 -- unconditioned one-record responses and finite kernel fits

**Conclusion.** On the tori `4^3`, `6^3`, `8^3` at their optimal twists `(1,1,1)`, `(0,0,0)`, `(1,1,1)`, with `E_sea = -78.383672`, `-258.857540`, `-611.811768` and `P_vv = 1/2` everywhere:

1. `[numerical, 1e-15]` One record in the **unconditioned sea** shifts each other site’s odds by exactly `2 P_vu^2`: `odds(v occ | u occ) = 1/2 - 2 P_vu^2` and `odds(v occ | u empty) = 1/2 + 2 P_vu^2`, against the Schur complement on `126`,
   `430` and `1022` cases.
2. `[numerical, 1e-13]` The largest `|P_vu|` at separation `1, 3, 5, 7` is `0.204124` then `0` on `4^3`, `0.199736, 0.037805, 0.008097, 0.002368` on `6^3`, and `0.199157, 0.023936, 0.007268, 0.003154` on `8^3`; and
   `sum_{u != v} P_vu^2 = 1/4` exactly on every torus, which is idempotency at `v` written out.
3. `[numerical, 1e-12]` **Selection rule.** `P_vu` is nonzero exactly when the separation has one odd component and no even component equal to `L/2`: `6` of `63`, `81` of `215`, `108` of `511`, with `0` mismatches.
4. `[numerical, fitted local slope]` From an `8 x 8` Bloch block at each of `48^3` cell momenta, equivalent to a torus of physical extent `96^3` -- no `V x V` object is formed -- validated against the exact `8^3` torus to `6e-16` on the spectrum and on every kernel entry:
   the last reported local slope `d log|P| / d log n` is `-3.02` on this finite grid, and a fit over `10 <= |r| <= 30` gives `|P| ~ |r|^-3.04` with `mean |P| |r|^3 = 0.21`. These are finite diagnostics over the stated range, with no error-controlled infinite-volume or infinite-distance exponent. Squaring an unconditioned kernel entry doubles a fitted exponent only in that diagnostic; it does not describe arbitrary conditional responses.

**Proof.** Each torus is built with the KS signs, its optimal twist found by minimising the half-filling energy over all eight twists, and `P` taken as the projector onto the lower half of the spectrum. Item 1 compares the
closed form against a Schur complement site by site; item 2 sums a row of `P` squared; item 3 is an exhaustive census against the stated predicate at a threshold declared before the run; item 4 diagonalizes the `8`-site-cell
Bloch matrix on a momentum grid, inverse-Fourier-transforms it, and validates the whole construction against the exact torus before any exponent is read.

**Reading, not theorem.** A single observation changes the remaining odds through the original kernel. Its zero entries are meaningful for that first observation. After further conditioning the relevant matrix is the updated Schur kernel, and the original parity zeros need not remain zeros.

## Theorem 5 -- additive opposite-sublattice observations and the corrected forcing boundary

**Conclusion.**

1. `[numerical, 1e-15]` The six neighbours of a site all lie on the other sublattice, so `P` restricted to them is exactly `I/2` and the Schur complement is **additive**: over all `64` six-neighbour record patterns on all
   three tori the odds are `1/2 - 2 sum_occ P_vu^2 + 2 sum_empty P_vu^2`.
2. `[numerical, 1e-12]` The range over those `64` is `[0, 1]` on `4^3` with `2` patterns forcing, `[0.021268, 0.978732]` on `6^3` and `[0.024036, 0.975964]` on `8^3` with none. The smallest torus forces because there
   `M^2 = 6I` is an exact integer identity, so the kernel row's support **is** the star.
3. `[numerical, preserved special case]` The support sum of `P_vu^2` is `1/4`. Recording the whole off-diagonal row support **uniformly occupied** is sufficient to force zero, and uniformly empty is sufficient to force one. The original tested support sizes `6`, `81`, `108`, and odds `8.3e-02`, `1.1e-05`, `2.0e-05` after dropping the weakest occupied site, are retained. They do not prove either direction of a general row-cover criterion.
4. `[numerical, stated finite bounds]` **Beyond the star.** On `8^3` with the six neighbours occupied (odds `0.024036`), one further record at separation `2` to `7` still shifts the odds by up to `4.5e-03`, `1.1e-03`, `3.6e-05`, `1.1e-04`,
   `2.6e-06`, `2.0e-05`, and by exactly `0` at separation `8` and beyond. With alternating neighbours a separation-`2` record reaches `5.9e-02` **although `P_vu` is exactly `0` there**: that influence arrives through the
   Schur complement alone. The whole separation-`2` shell empty gives `0.9704`.

**Proof.** Item 1 checks `P` on the six-neighbour block against `I/2` and compares the additive closed form against the Schur complement on every one of `64 x 3` patterns. Item 2 reads the range and the forcing count off
those same patterns and recomputes `M^2 - 6I` as an integer residual. Item 3 collects the row's support at a threshold declared before the run, sums its squared entries, and conditions on the whole support and on the support
minus its single weakest site. Item 4 conditions on the star plus one further record at every remaining site of the torus, exhaustively rather than by sampling, and reports the largest shift per distance shell.

**Correction and exact counterexamples.** For observations on one opposite sublattice, `P_R=I/2`; hence the additive formula above applies, and forcing is decided by that **signed occupied/empty sum**. Covering the six neighbours of site `0` on antiperiodic `4^3` with three occupied and three empty has probability `1/64` and leaves odds `1/2`, so row cover does not suffice for arbitrary outcomes. Conversely set

`T = {0,2,3,4,5,12,13,16,17,48,49}`.

The actual integer hopping matrix has `h^2=6I`. Splitting `T` into its two parity blocks gives `det P_T = 2^(-|T|) det(I-B B^T/6)`, evaluated with rational arithmetic. It is zero; every single-deletion minor is positive. Thus `T` is inclusion-minimal (principal submatrices are positive semidefinite, so a singular proper subset would make a single-deletion superset singular). No closed star is contained in `T`. Observing all ten sites `T\{0}` occupied has probability `3125/7962624` and forces `n_0=0`, although row-support neighbour `1` is missing. The sign convention `h=-M` is related by the bipartite diagonal gauge, which preserves these minors. For arbitrary positive-probability observations, the correct criterion is simply that the resulting conditional Schur diagonal is `0` or `1`. Neither former universal row-cover implication survives.

**Reading, not theorem.** In the tested six-neighbour menus the two uniform outcomes force on `4^3`; the `6^3` and `8^3` menus do not force. This is a statement about those menus. A later observation can affect a site where the unconditioned kernel entry vanished, as the retained distance-two witness shows.

## Corollary -- conditional mathematics and its physical boundary

1. The supplied finite Slater/Born law has an explicit determinant and conditional Schur description. Opposite-sublattice blocks with `P_R=I/2` give the stated additive formula. A general history uses the updated kernel; no universal sixth-power or original-parity rule is claimed for it.
2. These finite menus give a finite set of probabilities. They establish neither a continuum of odds nor uncapped spatial reach. The finite Fourier fits leave the asymptotic question open.
3. The three selected character states, the different generic ground Slater, the normalized ground-manifold mixture and the half-filled sea illustrate state dependence within supplied models. They do not select a physical vacuum or provide an admissibility/formation law.
4. Sequential conditioning on commuting record projectors is order independent when no intervening dynamics changes the state. The runner binds all 2688 actually executed `(triple, values, order)` keys and all 2240 comparisons; a one-order run cannot pass that coverage check.

## Reading, not theorem -- the whole thing in plain words

The determinant law and its conditional updates are useful finite identities. Which observations force another value depends on both their locations and outcomes. The explicit counterexamples rule out the earlier row-cover slogan. The model still needs its Hamiltonian, state, readout and formation choices supplied; none becomes physical by calling a probability a Record.

## Interfaces named for other lanes, not settled here

- **The vacuum decision.** This note supplies one more exact consequence of the choice PR #7879 named -- the law of records itself -- and does not make the choice. A lane deciding it inherits the two explicit distributions
  above, not a preference between them.
- **Interactions.** The determinantal structure is a **free-hopping** fact. Nothing here says what survives when the law is not quadratic in the modes, and no interaction term appears anywhere above.
- **The formation clause.** The site at which a record forms, the probability that it forms there, and the rate are all outside this note, exactly as they were outside PR #7858. Theorems 3 and 4 are the behaviour a
  formation clause would have to reproduce on this vacuum; they do not supply one.
- **The infinite-volume statement.** Everything here is finite: three tori and two open clusters. The inverse-cube decay is read from a finite momentum grid as a fitted local slope, validated against one exact torus. An
  infinite-volume theorem about that exponent is not attempted.

## Remaining live routes

1. Whether the special opposite-sublattice additivity and uniform-support sufficient conditions survive away from half filling and away from the KS sign field. Both the additivity of the six neighbours and the `1/4` support sum lean on `P_vv = 1/2` and on the bipartite structure, and
   neither is checked at any other filling here.
2. Whether the two zero mechanisms stay distinct on this vacuum as they did on the empty one. Theorem 1 exhibits determinantal zeros and Theorem 2 identifies the empty vacuum's cancellation zeros with them; no state is
   offered whose zeros are of neither kind, and none is forbidden.

## Executable claim block

```text
scope: conditional finite Slater/Born and encoded readout; no physical supplier derivation
T1: exact projection/DPP full-pattern and inclusion identities on cube/block; original zero/value censuses retained
T2: three specified character Slaters each have 12 forbidden pairs; generic ground Slater has none; normalized N2 rank3 projector differs from rank4 one-particle union (old pair minors sum 6)
T3: positive-probability Schur conditioning, rank N-|O|; all 448 triple/value conditions, 2688 executed order keys, 2240 comparisons
T4: original one-record response and parity census only before conditioning;48^3 cell momenta,96^3 physical extent; fit10<=r<=30 is a finite diagnostic
T5: additive formula when P_R=I/2; uniform row-cover is sufficient; both universal row-cover implications false; exact eleven-site witness and mixed-neighbour counterexample retained
numerics: original tables/predicates preserved except strengthened actual order coverage; new checks B5/B6/E6/E7 disclose corrected quantities
physical_status: law/state/Born/coarse-readout/fine-site formation and infinite limits remain supplied/open
```

## Proof boundary

The fermion law is a **designed supplier model**, in that note's own words "deriving that form from no axiom and claiming for it no privileged status"; the vacuum is **supplied**, taken from a note that explicitly declines to
decide whether it is the framework's; and **Lueders conditioning is stipulated** here as this note's update clause. Every statement above inherits all three: if any one is not the framework's, nothing above survives except as
a statement about what was supplied. Nothing here is derived from any axiom.

Every result is at **finite volume** and on **free hopping**. The clusters are the open `2x2x2` and `2x2x3` blocks and the tori `4^3`, `6^3`, `8^3`, and nothing is claimed for larger boxes, other boundary conditions, other
sign fields, other fillings, or any law that is not quadratic in the modes. The `E = -4` statements of Theorem 2 are on PR #7858's own plain-adjacency cube in its `N = 2` sector and are not statements about the sea.

The **decay exponent is a fitted local slope on a finite momentum grid**, not a proof. It is read from an `8 x 8` Bloch block at `48^3` cell momenta (physical extent `96^3`), after that construction is validated against the exact `8^3` torus
to `6e-16`; the local slope and the two fits are reported as outcomes, with the residual spread of a Euclidean fit over anisotropic separations reported rather than hidden. The unconditioned selection rule and special forcing examples are
finite censuses at thresholds declared before the run, not samples.

The arithmetic split is stated on every line. Theorem 1 items 2-4, the exact clauses of Theorem 2, the new rational counterexample in Theorem 5, and the commutation clause of Theorem 3 are **exact** -- integer matrices, `Fraction` arithmetic, and Gaussian elimination over `Q(sqrt3)`
and `Q(sqrt2)` with no floating point. Theorem 1 item 1 and the numerical clauses of Theorems 3, 4 and 5 are double precision on integer-derived data at `1e-12` to `1e-17`, each residual printed.

**Nothing about formation dynamics follows.** No formation site, probability or rate is supplied, and none is implied; every "odds" statement is a statement about the stipulated clause applied to the supplied state. No mass,
no coupling, no absolute unit and no dynamical clause appears anywhere. No axiom text is amended, extended, reworded or reinterpreted, no hypothesis is adopted, no status value is set, and no registry or manifest node is
created or edited.

## Review record

This is a corrected conditional source, not an applied audit verdict. The original 2026-09-03 notes, runner bodies, caches and all 108 original check identities are preserved by the dated correction record outside active documentation discovery. Its original Git heads recover the unchanged historical bodies. Numerical tables above retain their historical values unless a correction is expressly identified. The current cache records a genuine run of the final source; a zero exit or fresh fingerprint is not a proof of its scientific claims.

Each primary is standalone and declares its own note and the current minimal-axiom memo as mutable inputs. The memo is an interpretation boundary, not a derivation of the supplied Hamiltonian, state, Born rule, coarse-to-fine map or permanent Record formation. Historical parent titles and quotations are attribution only; their science has not been accepted here. No parent campaign is imported. Independent source confirmation and the coordinator's current-main mechanical gates remain separate; formal audit is deferred until a solid TOE.
