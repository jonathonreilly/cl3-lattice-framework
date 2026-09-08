# Vacuum/energy source correction — 2026-09-08

This dated record preserves prior wording and results verbatim. They are historical evidence, not active claims or audit status. The three current canonical notes are the authoritative source correction for F1–F13. The finite numerical protocol, all73 old check identities and all old numeric results are preserved; changed labels/operands and newly added controls are identified in the author handoff. No parent campaign, physical law, APS boundary or new primitive is adopted.

The first #7881 revision c7ca994c385cc7d282c9017a8df17e6fe6e70821 and live revision af1af53d28c8bf54a6e0440274ce01e5f0163eeb both remain exact Git recovery points. The live revision usefully corrected the action sign but retained a false point-force equality; the current source keeps the sign and corrects the operands.

## original-cutoff live — docs/MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md

SHA-256 `2ba36f82cc287562d46086ece1147ad2e93c422a0c9cd2a2257dc1092729a2f9`. Verbatim body follows.

````text
---
claim_id: matter_above_half_filled_sea_vacuum_question
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on the same two separately supplied surfaces the weak-field-source note is conditional on -- the designed fermion law of EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md, which that note declares a supplier model derived from no axiom, and the landed weak-field response surface of docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md -- plus one supplied datum, the filling, taken from HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md: on the named finite coarse tori and nowhere else, (T1) the half-filled staggered sea at its energy-minimising twist has E_sea = -78.383672, -258.857540 and -611.811768 on 4^3, 6^3 and 8^3, the first two being that note's own quoted values, with M^2 = 6 I an exact 64x64 integer identity at L = 4 so that E_sea/V = -sqrt6/2 exactly; the sea gaps are 2 sqrt6, 2 sqrt3 and 2 sqrt(6 - 3 sqrt2), each matching the reduced-zone Bloch form 2 sqrt(6 + 2 min_q sum_a cos q_a) to 1e-13, and the grid corner q = (pi, pi, pi) sends that gap to 0, a single Dirac point; V/2 is even at every L; and <n_v> = 1/2 at EVERY site, exactly, because the bipartite grading eps_v = (-1)^{v1+v2+v3} satisfies eps M eps = -M as a zero-residual integer identity, so P_vv + (eps P eps)_vv = 1 and P_vv = 1/2. (T2) On 8^3 the band-edge orbital pair has E_exc = 2.651309 and is delocalised, inverse participation ratios 171 and 176 of 512, while localised wavepackets at separations d = 1, 2, 3, 4 give sum_v rho = 0 to 1e-13 for rho = <n_v> - 1/2 with particle and hole rms radii 1.60 to 1.77; the local energy density eps_v = sum_{j~v} M_vj (P' - P)_vj has sum_v eps_v = E_exc to 1e-14, its negative part is exactly 0 for the orbital pair and on 4^3 and 0.2 to 0.3 per cent of E_exc for the wavepackets, and sum_v |rho| runs 1.12 to 1.94, under the 2 a disjoint unit particle and hole would give. (T3) Particle-hole conjugation P' -> eps (I - P') eps sends rho -> -rho and eps_v -> +eps_v exactly, residuals 6e-17 and 0: the number-density deviation is the ODD datum of a pair and the energy density the EVEN one; and eps flips all 1536 link signs of the 8^3 torus while leaving all 1536 face holonomies unchanged, difference 0, and every even-length Wilson line fixed, so a state and its conjugate lie in the same flux sector. (T4) With the source built on the physical 8^3 torus and zero-padded into response boxes Lb = 8, 16, 32, 64, read out centroid-centred and cubic-star-averaged, phi = G0 P0 rho gives: for rho = <n_v> - 1/2 a pure DIPOLE, total charge 1e-14, star-averaged monopole 4e-05 at r = 16, |p| = 3.206 at d = 4, log-log slope of the antisymmetric part -1.99 and 4 pi r^2 antisym_x phi / p_x = 1.0003, 1.0061, 0.9940 at r = 5, 8, 10; and for rho = eps_v/E_exc the landed MONOPOLE form, 4 pi r phi at r = Lb/4 equal to 0.2534, 0.3529, 0.3335, 0.3282 against the point control 0.4065, 0.3468, 0.3307, 0.3275, outside the window note's own 0.02 band about its stable 0.3266-0.3269 at Lb = 8 and 16 and inside it at Lb = 32 and 64, with Richardson 2 f_64 - f_32 giving 1.0096, 0.9941, 0.9741, 0.9427 at dd = 4, 6, 8, 10 against the like-for-like point control 1.0166, 0.9966, 0.9766, 0.9456; |rho| and rho_+ = max(rho, 0) reproduce the same monopole, 0.3283 and 0.3282 at Lb = 64. (T5) Against the bridge's five source-readout clauses above this vacuum: rho_v = <n_v> - 1/2 is the named diagonal operator -B_v/2, local on exactly six coarse edge sites, phase invariant and exactly covariant on the untwisted 6^3, gauge residual 0 and translation residual 6e-16, but its spectrum is {-1/2, +1/2} so it is NOT positive and its total is 0; eps_v is local, phase invariant and covariant off the twist cut, whose residual is 4.4e-02 on v_x in {0, 1, 7} of the twisted 8^3, but it is NOT diagonal, A_ij carrying an X, and is not guaranteed positive; |rho| and rho_+ are the expectation of no operator at all, being non-linear in the state, which the equal mixture of a pair and its conjugate exhibits at 0.1208. No linear-in-the-state candidate examined meets all five clauses. (T6) The signed sector is unchanged: rho and -rho enter both eta sectors with the same coefficient, the source vector stays [+1, +1], and least squares against the orientation-odd [+1, -1] leaves residual sqrt2 = 1.414214, the weak-field-source note's T7 value and the signed note's own 1.414e+00; the chirality grading maps the lowest empty orbital wholly into the occupied shell with its energy negated while fixing every holonomy and hence chi_eta, so the particle/hole sign is not the eta-sector orientation. WHICH STATE IS THE FRAMEWORK'S VACUUM IS NOT DECIDED HERE: it is named as a decision about the framework, for its owner, and the exact consequences of each choice are supplied. No mass, no M_phys, no G_Newton, no coupling and no test-body response law appears. Nothing is derived from any axiom, no axiom is amended, no status is set, and no registry entry is created."
upstream_dependencies: []
runner: scripts/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.py
---

# Matter above the half-filled sea: the odd density, the even density, and the vacuum question

**Date:** 2026-09-03
**Type:** bounded_theorem, explicitly conditional on two supplied surfaces and one supplied datum
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:** [`scripts/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.py`](../scripts/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.py)
**Runner cache:** [`logs/runner-cache/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.txt`](../logs/runner-cache/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.txt)
**Parents:** none in the dependency sense. The two conditioning surfaces and the one conditioning datum are quoted in "Setting" as conditions, not consumed as graded rows.

Two results in this lane are each internally clean and are about two different states. One takes the empty state as the vacuum, puts a named positive count on top of it, and finds that count meets every clause the weak-field bridge
asks of a source. The other finds that the staggered flux sector -- the one the framework's own kinetic clause names -- is selected by the hopping energy only when the coarse lattice is half full, and that at zero filling every
flux sector ties. This note computes what matter looks like above the half-filled state, and finds that the two landed results are consistent with each other and not with a single vacuum. Which state the framework means by its
vacuum is a question about the framework. It is named here for its owner, with the exact consequences of each answer, and it is not answered here.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-torus identities plus finite-dimensional numerical computations, every one conditional on two named supplied surfaces and one named supplied datum and on nothing else. Groups A2, A4, A5, C, E and F are integer matrix identities at zero tolerance, F2 bitmask structure of the encoding's generators, and an exact least-squares evaluation; groups A1, A3, B and D are finite floating-point computations each reporting its residual against a tolerance declared before the run, the response tolerance being the landed window note's own 0.02 band."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "The physical Newton residual is instead the source/test typing, mass-readout identification, and test-body response law. Current Record supplies none of the finite-additive scalar premise."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Route to its owner the one question this note names and does not decide: which state -- the empty one or the half-filled staggered sea -- the framework calls its vacuum. The consequences of each are supplied in the Corollary; the choice is not a residual to compute away."
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`: `T1` (`A`) the sea; `T2` (`B`) particle-hole pairs and the two densities; `T3` (`C`) conjugation and flux-sector invariance;
`T4` (`D`) the responses; `T5` (`E`) the clause check; `T6` (`F`) the signed sector. Each is established on named finite tori and carries its own tag: `[exact]` where the arithmetic is integer, `F2` or exact evaluation, and
`[numerical]` with a stated tolerance where it is floating point.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the tight-binding dispersion, the discrete Fourier inverse of the graph Laplacian, the multipole expansion and
Richardson extrapolation in `1/L` are standard methodology; every object is redeclared here and the runner recomputes every statement, including a validation of its own Green-function implementation against the landed window
note's published table before any new number is reported. The two surfaces and the one datum this note is conditional on are declared, quoted and named in "Setting"; they are conditions of the result, not graded dependencies,
and this note cites none of their grades and consumes no row. Non-load-bearing context pointers, plain file names with no grade and no dependency weight: `MINIMAL_AXIOMS_2026-06-29.md` (the four axioms quoted below);
`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`, the authority for the `1 / (4 pi |r|)` asymptotic; `POISSON_FINITE_VOLUME_WINDOW_AND_BIHARMONIC_OFFSET_BOUNDED_THEOREM_NOTE_2026-07-27.md`, whose band is
quoted before the run and used as the tolerance; `SIGNED_GRAVITY_APS_ACTION_ORIGIN_SUPERSELECTION_STABILITY_NOTE.md`; and `NEWTON_LAW_DERIVED_NOTE.md`, whose Non-Claims bound this whole exercise as they bound the parent lane.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."
**Qubit**: "Each site has a domain of local possibilities," whose "full one-site possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant
under lattice translations and proper cubic rotations." **Record**: "Records form. When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent. Only
records are readable. A readout value is determined by record content alone."

The record ontology is what makes the objects below densities at all. Neither `n_v` nor its deviation is a new primitive and neither is a site: each is a **readout of six records**. The six fine edge sites `2v +- e_a` around the
coarse corner `2v` each carry a record; `B_v` is the product of their six `Z` values, so `n_v = (1 - B_v)/2` returns `1` exactly when those six records register odd parity and `0` when they register even. Nothing is read that is
not a record, and the value is determined by record content alone, as Record requires.

**Supplied surface one -- the fermion law.** From `origin/physics-loop/emergent-3d-fermion-superlattice-existence:docs/EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md`,
verbatim: "The **encoding** is the Bravyi-Kitaev superfast encoding written on the coarse sublattice, with the code qubits exactly the coarse edge sites. The direction order at every coarse vertex is `-x < -y < -z < +x < +y <
+z`." and "`B_i = -1` marks the excitation; the **hop** across the coarse edge `(i, j)` is `T_ij = (i/2) A_ij (B_i - B_j)`." Its Proof boundary, verbatim and outranking every summary: "The law of Theorems 1 to 3 is a **designed
supplier model**: Admissibility fixes that there is one covariant nearest-neighbour rule and leaves its form to the supplier, and this note supplies one form and computes its consequences, deriving that form from no axiom and
claiming for it no privileged status." Everything below inherits that conditional.

**Supplied surface two -- the weak-field response, and its five clauses.** From `docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`, verbatim: the quadratic source action `A[phi; rho] = (1/2)
<phi, H phi> - <P0 rho, phi>` "has the unique stationary solution, modulo the constant zero mode, `phi = G0 P0 rho`." And the clause set this note tests, verbatim: "For a lattice amplitude `psi`, the only local, diagonal,
positive, phase-invariant quadratic density that is translation covariant and normalized by `sum_x rho_psi(x) = ||psi||^2` is `rho_psi(x) = |psi(x)|^2`. On finite periodic volumes the Poisson solve uses `P0 rho_psi`, i.e. the
zero-mode-subtracted density. The zero mode is the total-mass/background sector and is not part of the local force law." Five clauses -- local, diagonal, positive, phase invariant, translation covariant -- plus a normalisation.

**The supplied datum -- the filling.** From `origin/physics-loop/half-filling-selects-staggered-sector:docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md`, verbatim:
"Minimising each uniform sector over its eight twists gives `E_{V/2} = -78.383672` against `-67.882251` on `4^3`, `-116.809009` against `-99.882251` on `4x4x6` and `-258.857540` against `-218.564065` on `6^3`", and: "The all-`(-1)`
sector at its optimal twist satisfies `M^2 = 6 I` exactly, as a `64x64` integer matrix identity, so its spectrum is `+-sqrt6` with multiplicity `32` each and its half-filling energy attains the bound. It is therefore a **global
minimiser at half filling over all `2^192` link-sign fields on that torus**." And, verbatim, the filling dependence: "all `32` tie at `N = 0` and `N = 8`."

**The tension, named.** The weak-field-source note sources gravity on the empty state, `N = 0`, where `n_v >= 0` meets every clause of the bridge at once. The half-filling note selects the staggered sector -- the sector the
framework's own kinetic clause names -- only at `N = V/2`, and records that at `N = 0` every flux sector ties. Each result is clean about its own state. They are about different states.

**The window band, read before the run.** From `docs/POISSON_FINITE_VOLUME_WINDOW_AND_BIHARMONIC_OFFSET_BOUNDED_THEOREM_NOTE_2026-07-27.md`, verbatim: the scaling window `r = max(3, floor(N/16)), ..., floor(N/4)` "gives a stable
exponent near `1.66`; its outer-edge normalization is near `0.327`, not `1`", with `4 pi r G` at `r = N/4` equal to `0.3269`, `0.3267`, `0.3266` at `N = 96, 128, 192`, the last three exponents agreeing "within `0.02`", and "The
stable finite-volume number is not the continuum target `1`." That value and that `0.02` are read here **before** the run and used as the tolerance exactly as the weak-field-source note used them; the run chooses none of its own.

**The signed sector's demand.** From `docs/SIGNED_GRAVITY_APS_ACTION_ORIGIN_SUPERSELECTION_STABILITY_NOTE.md`, verbatim: the proposed `S_int = - chi_eta(Y) M_phys <rho, Phi>` needs a source vector over `(chi=+, chi=-)` of `[+1,
-1]`, with reported "least-squares residual=1.414e+00" against what the retained sources supply.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the strongest supported scope is precisely `P0`-`P6`. `P0`, declared here and conditional: the two supplied surfaces, the
supplied filling, the coarse lattice, the KS sign field, the twists and the response operator. `P1` (`A`): the sea, its energies, its gap and the exact half filling. `P2` (`B`): particle-hole pairs and the two densities. `P3`
(`C`): conjugation and flux-sector invariance. `P4` (`D`): the responses, validated against the landed table first. `P5` (`E`): the five-clause check. `P6` (`F`): the signed sector. `P5` uses `P1` and `P2` only for the states it
evaluates on; `P6` uses `P3`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`,
`eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`. A **twist** on axis `a` flips the bonds crossing the cut `v_a = L-1 -> 0`, changing one Wilson line and no face holonomy. `M` is the symmetric integer hopping matrix of the
chosen sign field on the coarse torus `L^3`; `P` is the orthogonal projector onto its `V/2` lowest eigenvectors, the **half-filled sea**, and `E_sea` is the sum of those `V/2` levels. A **particle-hole pair** above the sea is
`P' = P - |h><h| + |p><p|` with `p` in the empty span and `h` in the occupied one, and its energy is `E_exc = <p|M|p> - <h|M|h>`. The two candidate densities are

```text
rho_v   = <n_v> - 1/2 = P'_vv - 1/2 = -<B_v>/2        the number-density deviation
eps_v   = sum_{j ~ v} M_vj (P' - P)_vj                the local excitation energy density
```

with `sum_v eps_v = tr(M (P' - P)) = E_exc`. The **chirality grading** is `eps_v = (-1)^{v_1 + v_2 + v_3}`, the bipartite two-colouring of the coarse torus. The **response** is the landed one, unchanged: `H = -Delta_lat` with the
seven-point stencil, `G0 = H^{-1}` off the constant mode, `P0` the projection off that mode, `phi = G0 P0 rho`. Sources are built on the physical `8^3` coarse torus, unwrapped about the pair, re-centred on their own charge
centroid and zero-padded into a response box `Lb^3`; the far field is read **cubic-star-averaged**, `<phi>_star(r)`, which kills `l = 1` and `l = 3` exactly, and **`x`-antisymmetrised**, which kills `l = 0` and `l = 2`.

## Theorem 1 -- the half-filled staggered sea, and why every site holds exactly a half

**Conclusion.** On the coarse tori `4^3`, `6^3` and `8^3`, each at its energy-minimising twist:

1. `E_sea = -78.383672`, `-258.857540` and `-611.811768`. The first two are the supplied datum's own quoted values. At `L = 4` the optimal-twist field satisfies `M^2 = 6 I` as a `64x64` integer identity at zero residual, so
   every level is `+-sqrt6` and `E_sea / V = -sqrt6 / 2` exactly.
2. The sea gaps are `2 sqrt6`, `2 sqrt3` and `2 sqrt(6 - 3 sqrt2)`, each matching the reduced-zone Bloch form `2 sqrt(6 + 2 min_q sum_a cos q_a)` to `1e-13`. As `L` grows the momentum grid reaches the reduced-zone corner
   `q = (pi, pi, pi)`, where `sum_a cos q_a = -3` and the gap is `0`: a single Dirac point, and the energy-minimising twist is the one that keeps that point off the finite grid.
3. `V/2 = 32, 108, 256` is even at every `L`.
4. `<n_v> = 1/2` at **every** site of all three tori, to `8e-16`, and the reason is exact: the chirality grading satisfies `eps M eps = -M` as a zero-residual integer identity, so the spectrum is symmetric about `0`, the sea
   projector obeys `eps P eps = I - P`, and `P_vv + (eps P eps)_vv = 1` with `(eps P eps)_vv = eps_v^2 P_vv = P_vv`. Hence `P_vv = 1/2`.

**Proof.** Item 1's flatness certificate and item 4's chirality identity are integer matrix identities at zero tolerance; the energies and the gaps are `[numerical, 1e-13]` against tolerances declared before the run, the two
sea energies against the supplied datum's published values and the gaps against both the closed surd forms and the reduced-zone Bloch formula. Item 3 is arithmetic.

**Reading, not theorem.** Every site of this state holds exactly half a particle, and not approximately: the same two-colouring that makes the box bipartite pairs each level with its negative, and pairing levels that way forces
the half. The state is a closed shell with an even count, and on larger boxes the distance from the top of the sea to the bottom of the empty band shrinks toward zero at one corner of the reduced zone.

## Theorem 2 -- matter above the sea comes as a pair, and carries two densities

**Conclusion.** On the `8^3` torus above that sea:

1. The band-edge orbital pair has `E_exc = 2.651309`, exactly the sea gap, and is **delocalised**: inverse participation ratios `171` and `176` of the `512` coarse sites, rms radii `3.64` and `3.63`.
2. Localised wavepackets -- a particle drawn from the empty orbitals and a hole from the occupied ones, at separations `d = 1, 2, 3, 4` -- have `sum_v rho = 0` to `1e-13`, with particle and hole rms radii `1.60` to `1.77`.
3. `sum_v eps_v = E_exc` to `1e-14` over all five pairs, `E_exc` running `2.6513` to `4.5163`.
4. The negative part of `eps_v` is exactly `0` for the orbital pair and on the `4^3` torus, and `0.2` to `0.3` per cent of `E_exc` for the localised wavepackets.
5. `sum_v |rho|` runs `1.12` to `1.94`, strictly under the `2` a disjoint unit particle and unit hole would give.

**Proof.** All five items are `[numerical]` at the tolerances printed with them, computed from the one-body projector `P'` on the `512 x 512` sea; no many-body object is formed anywhere. The wavepackets are normalised Gaussians
projected into the empty and the occupied spans respectively, a placement choice declared in the Proof boundary.

**Reading, not theorem.** Nothing sits on this sea alone. A particle above it is a hole below it, and the two together carry no net count: the pluses and the minuses cancel exactly. What the pair does carry is an energy, and that
energy sits on the sites the pair occupies, positive nearly everywhere. Item 5 says the two clouds are not disjoint lumps but overlapping ones.

## Theorem 3 -- the odd datum and the even datum, and the flux sector both share

**Conclusion.**

1. Particle-hole conjugation `P' -> eps (I - P') eps` sends `rho -> -rho` exactly, residual `6e-17`, and `eps_v -> +eps_v` exactly, residual `0`, over all five pairs. The number-density deviation is the **odd** datum of a pair
   and the local energy density the **even** one.
2. `eps` is a diagonal `+-1` gauge map: it flips every one of the `1536` link signs of the `8^3` torus, yet all `1536` face holonomies are unchanged, difference `0`, and every even-length Wilson line is fixed.
3. Hence a state and its particle-hole conjugate lie in the **same** flux sector.

**Proof.** Item 1 is an exact conjugation of the one-body projector, its residuals reported at machine precision. Item 2 is exact integer bookkeeping over every face and every axis loop of the torus: the grading appears twice at
each corner of a four-link face and an even number of times around an even loop.

**Reading, not theorem.** Conjugate every particle to a hole and every hole to a particle. The count above the sea changes sign at every site; the energy at every site does not change at all. And the pattern of signs around every
small square, and around every way through the box, is exactly what it was. The conjugation is a relabelling inside one sector, not a passage between sectors.

## Theorem 4 -- the responses: a dipole from the count, a monopole from the energy

**Conclusion.** With `phi = G0 P0 rho`, the source built on the physical `8^3` torus at `d = 4` and zero-padded into `Lb = 8, 16, 32, 64`:

1. **Validation first.** The recomputed `4 pi r G(r)` at `r = 10` rounds to `0.190 / 0.432 / 0.568` at `N = 32 / 48 / 64`, the window note's own published row. The point-source control at `r = Lb/4` gives `0.4065 / 0.3468 /
   0.3307 / 0.3275`, the weak-field-source note's own values to `5e-05`.
2. **The count is a dipole.** For `rho = <n_v> - 1/2`: total charge `1e-14`, star-averaged monopole `4e-05` at `r = 16`, dipole `|p| = 3.206`, log-log slope of the antisymmetric part `-1.99` against the dipole's `-2`, and
   `4 pi r^2 antisym_x phi / p_x = 1.0003 / 1.0061 / 0.9940` at `r = 5 / 8 / 10`, within one per cent.
3. **The energy is a monopole.** For `rho = eps_v / E_exc`: `4 pi r phi` at `r = Lb/4` is `0.2534 / 0.3529 / 0.3335 / 0.3282` at `Lb = 8 / 16 / 32 / 64`, against the point control above -- outside the window note's `0.02` band
   about `0.3266`-`0.3269` at `Lb = 8` and `16`, inside it at `Lb = 32` and `64`.
4. **The coefficient.** Richardson `f_inf = 2 f_64 - f_32` gives `1.0096 / 0.9941 / 0.9741 / 0.9427` at `dd = 4 / 6 / 8 / 10`, against the **like-for-like** point-source control on the same two boxes, `1.0166 / 0.9966 / 0.9766 /
   0.9456`: the two agree to `0.01` at every `dd`, so the deficit from `1` is the box, not the source.
5. `|rho|` and `rho_+ = max(rho, 0)` reproduce the same monopole readout, `0.3283` and `0.3282` at `Lb = 64`.

**Proof.** `G0` is the discrete Fourier inverse of `lambda(k) = 6 - 2 sum_a cos k_a` with the zero mode set to zero, which is `P0` exactly rather than approximately; the response is one forward and one inverse transform. Every
readout is cubic-star-averaged or `x`-antisymmetrised, which removes the multipoles the readout is not about, and every source is re-centred on its own charge centroid before the far field is read. The window comparison uses the
landed note's own `0.02`, quoted before the run; the extrapolation is the standard `1/L` Richardson step at fixed `dd`, applied identically to the source and to the control, with no fitting window and no free parameter.

**Reading, not theorem.** A pair with no net count does not pull from far away in the way a lump of count does. Its field falls off one power faster and points along the line from the hole to the particle: at a distance it is a
dipole and nothing else. The energy of the pair is a different object. It is positive nearly everywhere, it adds up to the pair's whole energy, and at a distance its field carries exactly the shape a single point of count carries
-- the same number, box for box, as the point control.

## Theorem 5 -- the five clauses above this vacuum, and which one each candidate fails

**Conclusion.** Against the bridge's clause set -- local, diagonal, positive, phase invariant, `2Z^3`-covariant, plus the normalisation -- above the half-filled sea:

1. `rho_v = <n_v> - 1/2` is the **named diagonal operator** `-B_v/2`: diagonal, its `x`-mask being empty; local on exactly the six coarse edge sites at `2v`; phase invariant, trivially, being diagonal; and exactly covariant on
   the untwisted `6^3`, gauge residual `0` and translation residual `6e-16`. But its spectrum is `{-1/2, +1/2}`, so it is **not positive**, and its total is `0`, not `||psi||^2`.
2. `eps_v` is local, phase invariant, and covariant off the twist cut -- the twisted `8^3` cut plane leaves a translation residual `4.4e-02` supported on `v_x` in `{0, 1, 7}`, a finite-torus boundary artefact named rather than
   absorbed. But it is **not diagonal**: it is built from the supplied hop and `A_ij` carries an `X` on one code qubit with three trailing `Z`s. Nor is it guaranteed positive, though its negative part is small or zero here.
3. `|rho|` and `rho_+ = max(rho, 0)` are the expectation of **no operator at all**, being non-linear in the state: on the equal mixture of a pair and its conjugate the deviation vanishes, so `|rho|` reads `0` there where any
   linear functional reads the average of the two, `0.1208` apart.
4. So **no** linear-in-the-state candidate examined meets all five clauses above this vacuum.

**Proof.** Item 1's structural facts are exact `F2` bitmask statements about `B_v` in the declared encoding, its spectrum an exact enumeration over the six-qubit support; its covariance residuals are computed by gauge-corrected
translation of the state on the untwisted `6^3`. Item 2's `X`-support is the same bitmask statement about `A_ij`, and the cut residual is computed and localised rather than asserted. Item 3 is an exact evaluation on an explicit
mixture.

**Reading, not theorem.** On the empty state the count of matter is a number that is never negative, and the bridge asks for exactly that. On the half-filled sea the count above the sea is negative wherever there is a hole, and
positive wherever there is a particle, and it adds to nothing. Making it positive by hand -- taking its size, or keeping only its positive half -- gives a quantity no operator names. The two demands, positive everywhere and zero
in total, do not sit together for anything but the zero source.

## Theorem 6 -- the signed sector is untouched

**Conclusion.** `rho` and `-rho` enter both `eta` sectors with the same coefficient, so the source vector over `(chi = +, chi = -)` is still `[+1, +1]`, and least squares against the orientation-odd `[+1, -1]` leaves residual
`sqrt2 = 1.414214` -- the weak-field-source note's `T7` value and the signed note's own `1.414e+00`. And the chirality grading maps particles to holes: the lowest empty orbital's conjugate lies wholly in the occupied shell, norm
`1.000000000000`, with its energy exactly negated, residual `4e-16`, while every holonomy and hence `chi_eta` is fixed. The particle/hole sign is **not** the `eta`-sector orientation.

**Proof.** The residual is the same least-squares evaluation on the same two-sector basis the signed note reports. The orbital statement is an exact conjugation on the `8^3` sea; the holonomy invariance is Theorem 3 item 2.

**Reading, not theorem.** A sign on the count above the sea is not the sign the signed sector wants. That sign is a global label of the whole boundary; this one is a per-site charge inside one sector, and under the conjugation of every
particle to a hole the global label is exactly what it was.

## Corollary -- what moved, and the question that is named rather than answered

Within the setting declared above, conditional on the two supplied surfaces and the one supplied filling, and on the finite tori named:

1. **Above the half-filled staggered sea, matter comes as particle-hole pairs.** The number-density deviation is a named diagonal operator `-B_v/2`, exactly covariant, zero-total and particle-hole odd, and it sources a pure
   dipole. The excitation energy density is particle-hole even, is positive nearly everywhere, and reproduces the landed monopole form against a like-for-like control.
2. **The bridge's clause set, satisfiable on the empty vacuum, is met by no linear-in-the-state candidate examined on the half-filled vacuum.** Positivity and zero total do not hold together for a non-trivial signed source, and
   Theorem 5 names exactly which clause each candidate fails. This is a statement about the candidates examined above this vacuum; it closes nothing and it is not a no-go.
3. **The two landed results are consistent with each other and not with a single vacuum.** Which state is the framework's vacuum is a decision about the framework, named here for its owner, not a residual to compute away. The
   exact consequences of each choice are supplied. **If the vacuum is empty**: the positive number density `n_v` sources gravity and meets every clause; all flux sectors tie, so the kinetic clause's staggered field is a free
   choice; and there is no Dirac structure. **If the vacuum is the half-filled sea**: the staggered sector is selected by the hopping energy; the spectrum has a gapless point at the reduced-zone corner; matter comes in pairs;
   the energy density is the object that carries the monopole; and the number-density deviation carries a dipole and no monopole.
4. **The signed sector is untouched either way**, at residual `sqrt2` in both.

**Reading, not theorem.** If the vacuum is empty, the count of matter is the thing that pulls, and the sign on the squares does not matter. If the vacuum is the half-filled sea, matter comes as a particle together with a hole,
the count of matter above the sea pushes and pulls in equal measure and reaches only as far as a dipole, and it is the energy of the pair that pulls like a mass. The framework has not yet said which vacuum it means.

## What does not move

- No mass, no `M_phys`, no `G_Newton`, no coupling constant, and no absolute unit appears anywhere.
- No test-body response law. `F = -M_test grad(phi)` is exactly as unsupplied after this note as before it.
- No vacuum is chosen. Nothing below or above prefers one of the two states; both consequence lists are supplied and neither is adopted.
- Nothing at nonlinear order; this note stays strictly at the linear response the bridge supplies. The signed sector is untouched.
- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

- **The vacuum decision.** Whichever lane owns the framework's ground state should decide between the empty state and the half-filled sea. Corollary item 3 hands it two fully explicit consequence lists; it does not hand it an
  answer, and no part of this note is weakened or strengthened by either choice.
- **A positive diagonal density above the sea.** None linear in the state is found here. A lane that wants one should treat Theorem 5 as the statement it must get past, and the incompatibility of positivity with zero total as
  the shape of the obstacle, not as a bound on the search.
- **The twist cut's covariance residual.** The `4.4e-02` on `v_x` in `{0, 1, 7}` is a finite-torus artefact of the twisted sign field. A lane wanting exact covariance of `eps_v` on a twisted torus owns it.
- **Larger physical tori.** The source here is built on `8^3` and nowhere else.
- **The signed sector.** Theorem 6 says this construction's particle/hole sign is not the orientation that sector wants; that is a survey, not a bound.

## Remaining live routes

1. Physical tori beyond `8^3`, and response boxes beyond `64^3`.
2. Interactions. Everything here is free hopping on a one-body projector; nothing is claimed about what an interaction term would do to the sea or to a pair.
3. The mass readout and the test-body response law, both untouched here and both still the Newton lane's residuals.

## Executable claim block

The canonical machine-bound restatement of the six theorem conclusions.

```text
conditional_on: the supplied fermion law (declared supplier model, derived from no axiom), the landed weak-field response surface phi = G0 P0 rho, and the supplied half-filling datum
sea: E_sea = -78.383672 / -258.857540 / -611.811768 at optimal twist on 4^3 / 6^3 / 8^3, the first two the supplied datum's own; M^2 = 6 I exactly at L = 4 so E_sea/V = -sqrt6/2
gap: 2 sqrt6 / 2 sqrt3 / 2 sqrt(6 - 3 sqrt2), matching 2 sqrt(6 + 2 min_q sum_a cos q_a) to 1e-13; the grid corner q = (pi,pi,pi) sends the gap to 0, a single Dirac point
half_filling: V/2 = 32/108/256 even; <n_v> = 1/2 at EVERY site to 8e-16, exactly because eps M eps = -M is a zero-residual integer identity, so P_vv + (eps P eps)_vv = 1 and P_vv = 1/2
pairs: orbital pair E_exc = 2.651309 with IPR 171 and 176 of 512; wavepackets at d = 1/2/3/4 with sum_v rho = 0 to 1e-13 and rms 1.60 to 1.77
energy_density: sum_v eps_v = E_exc to 1e-14 over five pairs; negative part exactly 0 for the orbital pair and on 4^3, 0.2-0.3 per cent of E_exc for wavepackets; sum_v |rho| = 1.12 to 1.94 < 2
conjugation: P' -> eps (I - P') eps sends rho -> -rho (6e-17) and eps_v -> +eps_v (0); rho is the ODD datum, eps_v the EVEN one
flux_invariance: eps flips all 1536 link signs of 8^3, all 1536 face holonomies unchanged (difference 0), every even-length Wilson line fixed; a state and its conjugate share a flux sector
response_validation: 4 pi r G at r = 10 rounds to 0.190/0.432/0.568 at N = 32/48/64; point control 4 pi r G at r = Lb/4 = 0.4065/0.3468/0.3307/0.3275 at Lb = 8/16/32/64
dipole: rho = <n_v> - 1/2 gives total charge 1e-14, star monopole 4e-05 at r = 16, |p| = 3.206 at d = 4, log-log slope -1.99, 4 pi r^2 antisym_x phi / p_x = 1.0003/1.0061/0.9940 at r = 5/8/10
monopole: rho = eps_v/E_exc gives 4 pi r phi at r = Lb/4 = 0.2534/0.3529/0.3335/0.3282, outside the landed 0.02 band about 0.3266-0.3269 at Lb = 8, 16 and inside it at Lb = 32, 64
monopole_coefficient: Richardson 2 f_64 - f_32 gives 1.0096/0.9941/0.9741/0.9427 at dd = 4/6/8/10 against the like-for-like point control 1.0166/0.9966/0.9766/0.9456
positive_variants: |rho| and rho_+ = max(rho, 0) give 0.3283 and 0.3282 at Lb = 64
clause_check: (a) -B_v/2 diagonal, local on six coarse edge sites, phase invariant, exactly covariant on the untwisted 6^3 (0, 6e-16), spectrum {-1/2, +1/2} so NOT positive, total 0; (b) eps_v local, phase invariant, covariant off the twist cut (residual 4.4e-02 on v_x in {0,1,7}) but NOT diagonal, A_ij carrying an X, and not guaranteed positive; (c) |rho| and (d) rho_+ the expectation of no operator, non-linear in the state, exhibited at 0.1208
clause_verdict: no linear-in-the-state candidate examined meets all five clauses above the half-filled vacuum
signed_sector: source vector [+1, +1]; least squares against [+1, -1] leaves residual sqrt2 = 1.414214; the chirality grading maps particles to holes, fixing every holonomy and chi_eta
vacuum: NOT DECIDED HERE; named as an owner-level decision about the framework, with the exact consequences of each choice supplied
not_supplied: mass, M_phys, G_Newton, coupling, absolute unit, test-body response law, nonlinear order, interactions, a positive diagonal density above the sea, any choice of vacuum
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=24 FAIL=0
```

## Proof boundary

The fermion law is a **designed supplier model**, in that note's own words "deriving that form from no axiom and claiming for it no privileged status"; the weak-field response is likewise a supplied surface, bounded in its own
note; and the filling is a supplied datum taken from a third note and not derived here. Every statement above inherits all three: if any one is not the framework's, nothing above survives except as a statement about what was
supplied. Nothing here is derived from any axiom.

Every result is at **finite volume**. The sea is computed on `4^3`, `6^3` and `8^3` and nowhere else; the source is built on the `8^3` physical torus and zero-padded into response boxes `Lb = 8, 16, 32, 64` and nowhere else; the
Dirac point is a statement about where the momentum grid tends, established from the reduced-zone Bloch form and not from any infinite-volume theorem. The Richardson step of Theorem 4 item 4 is a `1/L` step between two of those
boxes, applied identically to the source and to the control, not an infinite-volume result; the small-box readouts of Theorem 4 item 3 are reported as outcomes precisely so the small-box deficit is not hidden inside the large-box
agreement.

The **wavepacket placement is a choice**. The particle and hole are normalised Gaussians of unit width centred at named sites and projected into the empty and occupied spans; `E_exc` varies by about four per cent across the
separations tested, and every pair-dependent number is reported per pair rather than averaged. The **twist cut's covariance residual** is named, localised and not absorbed: `4.4e-02` on `v_x` in `{0, 1, 7}` of the twisted `8^3`,
against `0` on the untwisted `6^3`.

**No vacuum is chosen.** The tension between the two landed results is stated, both consequence lists are supplied, and the decision is routed to the owner of the framework's ground state. Theorem 5 is scoped to the candidates
examined above the half-filled sea and is not a no-go about that vacuum or any other. No mass, no `M_phys`, no `G_Newton`, no coupling and no absolute unit appears; the mass-readout identification and the test-body response law
are untouched; nothing nonlinear is touched. No axiom is amended, no status is set, and no registry entry is created.

## Review record

An honest auditor should come away with: a conditional computation, not a derivation; six statements on named finite tori, several of them exact integer identities; one exact reason -- a bipartite chirality identity -- for the
half filling that everything else rests on; two densities cleanly separated by their behaviour under one exact involution, the odd one sourcing a dipole and the even one the landed monopole; a five-clause audit that says which
clause each candidate fails rather than that some clause must fail; and one question named as a decision about the framework rather than answered. Nothing here is a fitted number: the one tolerance in the response is quoted from
a landed note before the run, the implementation is validated against that note's own published table before any new value is reported, and every extrapolation is applied identically to the source and to a like-for-like point
control. The note is self-contained in the sense that matters for replay -- `upstream_dependencies` is empty, every object is declared in "Definitions", the runner imports nothing from the repository, and the two conditioning
surfaces and the one conditioning datum are quoted verbatim with paths rather than consumed as graded rows. Hard landing conditions are a fresh runner and cache pair closing at `PASS=24 FAIL=0` with runtime under the declared
timeout and stdout under `5500` characters, and passing repository pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
````

## original-cutoff live — logs/runner-cache/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.txt

SHA-256 `f2fa8687bfb5e89717e399e66a79c2d36a87b3e608855456200be5af018cc5b6`. Verbatim body follows.

````text
===== runner cache v1 =====
runner: scripts/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.py
runner_sha256: 6dd961e2a4ace198d7fc6d882a688477c6f875c96c9d654f6a35a8853ef73012
timeout_sec: 300
exit_code: 0
elapsed_sec: 0.31
status: ok
----- stdout -----
PASS A1 [numerical, 1e-6] the half-filled staggered sea at its optimal twist on 4^3/6^3/8^3 has E_sea = -78.383672/-258.857540/-611.811768, the first two being the supplied filling datum's own values
PASS A2 [exact] at L = 4 the optimal-twist field satisfies M^2 = 6 I as a 64x64 integer identity (residual 0), so every level is +-sqrt6 and E_sea/V is exactly -sqrt6/2 = -1.224744871 (residual 0e+00)
PASS A3 [numerical, 1e-13] the gaps are 2 sqrt6 / 2 sqrt3 / 2 sqrt(6 - 3 sqrt2) = 4.898979/3.464102/2.651309, matching the reduced-zone Bloch form 2 sqrt(6 + 2 min_q sum_a cos q_a) (8e-15); the grid reaches q = (pi,pi,pi), the gap -> 0: a Dirac point
PASS A4 [exact] V/2 = 32/108/256 is even at every L: the sea is a closed shell of pairs, the neutral sector the finite-torus P0 assumes
PASS A5 [exact/numerical, 1e-12] <n_v> = 1/2 at EVERY site of all three tori (8e-16), and its exact reason: the bipartite grading eps_v = (-1)^{v1+v2+v3} gives eps M eps = -M as an integer identity (0), so P_vv + (eps P eps)_vv = 1 (2e-15) and P_vv = 1/2
PASS B1 [numerical, 1e-12] the band-edge orbital pair on 8^3 has E_exc = 2.651309, the sea gap, and is DELOCALISED: IPR 171 and 176 of 512 sites, rms 3.64 and 3.63
PASS B2 [numerical, 1e-13] localised wavepackets on 8^3 -- particle from the empty orbitals, hole from the occupied ones, d = 1/2/3/4 -- have sum_v rho = 0 to 1e-14 for rho = <n_v> - 1/2, with rms 1.60 to 1.77
PASS B3 [numerical, 1e-14] the local energy density eps_v = sum_{j~v} M_vj (P' - P)_vj carries the whole excitation: sum_v eps_v = E_exc to 2e-15 over all five pairs, E_exc 2.6513 to 4.5163
PASS B4 [numerical, 1e-15] eps_v is essentially non-negative: its negative part is exactly 0 for the orbital pair (0e+00) and on 4^3 (0e+00), and 0.2% to 0.3% of E_exc for the wavepackets
PASS B5 [numerical] the clouds OVERLAP: sum_v |rho| runs 1.12 to 1.94, under the 2 a disjoint unit particle and hole would give
PASS C1 [exact] conjugation P' -> eps (I - P') eps sends rho -> -rho (6e-17) and eps_v -> +eps_v (0e+00) over all five pairs: the number-density deviation is the ODD datum, the energy density the EVEN one
PASS C2 [exact] eps is a diagonal +-1 gauge map: it flips all 1536 link signs, yet all 1536 faces of 8^3 keep their holonomy (0) and every even Wilson line is fixed (True) -- a state and its conjugate lie in the SAME flux sector
PASS D1 [numerical, 1e-3] validation before any new number: 4 pi r G(r) at r = 10 rounds to 0.190/0.432/0.568 at N = 32/48/64, the window note's published row
PASS D2 [numerical, 1e-4] the point control on the same boxes: 4 pi r G at r = Lb/4 is 0.4065/0.3468/0.3307/0.3275 at Lb = 8/16/32/64, the source note's own row (5e-05)
PASS D3 [numerical] candidate (a) rho = <n_v> - 1/2 is a pure DIPOLE: total charge 1e-14, star monopole 4e-05 at r = 16, |p| = 3.206 at d = 4, log-log slope of its antisymmetric part -1.99, 4 pi r^2 antisym_x phi / p_x = 1.0003/1.0061/0.9940 at r = 5/8/10
PASS D4 [numerical, band 0.02] candidate (b) rho = eps_v/E_exc reproduces the landed MONOPOLE form: 4 pi r phi at r = Lb/4 is 0.2534/0.3529/0.3335/0.3282 at Lb = 8/16/32/64, outside the window note's 0.02 band about 0.3266-0.3269 at Lb = 8, 16 and INSIDE it at Lb = 32, 64
PASS D5 [numerical] Richardson f_inf = 2 f_64 - f_32 gives candidate (b) the monopole coefficient 1.0096/0.9941/0.9741/0.9427 at dd = 4/6/8/10 against the like-for-like point control 1.0166/0.9966/0.9766/0.9456, agreeing to 0.01
PASS D6 [numerical, band 0.02] the two non-linear positive candidates do the same: (c) |rho| and (d) rho_+ = max(rho, 0) read 0.3283 and 0.3282 at Lb = 64, inside the band and beside the point control 0.3275
PASS E1 [exact] candidate (a) is the NAMED operator rho_v = <n_v> - 1/2 = -B_v/2: diagonal (x-mask 0), local on exactly 6 coarse edge sites, phase invariant, covariant on the untwisted 6^3 (0, 6e-16); spectrum {-0.5, +0.5}, so NOT positive; total 1e-14
PASS E2 [exact] candidate (b) eps_v is local, phase invariant and covariant off the twist cut, but NOT diagonal: it is built from the hop, and A_ij carries an X on 1 code qubit with 3 trailing Z's; nor is it positive. The twisted 8^3 cut leaves residual 4.4e-02 on v_x [0, 1, 7]
PASS E3 [exact] candidates (c) |rho| and (d) rho_+ are the expectation of NO operator, being non-linear in the state: on the equal mixture of a pair and its conjugate |rho| reads 0 where a linear functional reads the average, 0.1208 apart
PASS E4 [stated] so NEITHER linear-in-the-state candidate meets all five bridge clauses above this sea: (a) fails positivity, total zero; (b) fails diagonality; (c), (d) are positive with non-zero total but no operator expresses them
PASS F1 [exact] rho and -rho enter both eta sectors with the SAME coefficient, so the source vector stays [+1, +1]; least squares against the orientation-odd [+1, -1] leaves residual 1.414214 = sqrt2, the source note's T7 and the signed note's own 1.414e+00
PASS F2 [exact] the chirality grading maps particles to holes -- the lowest empty orbital's conjugate lies wholly in the occupied shell (1.000000000000), energy negated (4e-16) -- while fixing every holonomy and chi_eta: the particle/hole sign is NOT the sector orientation
SUMMARY: above the half-filled sea matter comes in pairs; the number-density deviation is the named operator -B_v/2, ODD and zero-total, sourcing a dipole, and the energy density is EVEN and gives the landed monopole form. Which state is the vacuum is not decided here.
TOTAL: PASS=24 FAIL=0

----- stderr -----

````

## original-cutoff live — docs/ENERGY_PRODUCT_AND_TEST_BODY_LAW_ABOVE_THE_HALF_FILLED_SEA_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md

SHA-256 `e3afef7d7608e275775a84e335f43d10ea488d6c0842c4a1b66eb07cdde950f1`. Verbatim body follows.

````text
---
claim_id: energy_product_test_body_law_half_filled_sea
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on three separately supplied things and on nothing else -- the designed fermion law of EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md, which that note declares a supplier model derived from no axiom; the landed weak-field response surface phi = G0 P0 rho of docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md; and the choice of the half-filled staggered sea as the vacuum, which MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md names as a decision about the framework and does not make -- on the named finite tori and nowhere else: (T1) two localised particle-hole pairs above the 8^3 half-filled staggered sea at its energy-minimising twist (E_sea = -611.811768, gap 2.651309, <n_v> = 1/2 to 8e-16) form a determinant state P'' = P - Q_h + Q_p that is a projector to 2e-15 with trace exactly 256 = V/2 at every centroid separation D = (2,0,0), (3,0,0), (4,0,0), (3,3,0) and both internal separations d_pair = 1, 2; the orbital overlaps fall <p1|p2> = 0.37, 0.15, 0.044, 0.014 and <h1|h2> = 0.38, 0.021, 0.0013, 0.0036; the energy is additive at relative defect -2.1e-02, -2.3e-03, -2.7e-04, -5.8e-05 and the additivity defect of the local energy density eps_v falls an order of magnitude per unit of D, 2.1e-01, 2.4e-02, 2.7e-03; and sum_v rho = 0 to 1e-14 for every single-pair and every joint state, so the count above this sea is identically zero. (T2) With the landed response validated first against the point control 4 pi r G at r = Lb/4 = 0.3307, 0.3275 at Lb = 32, 64, the interaction energy E_int = <eps_1, G0 P0 eps_2> equals the product form E_1 E_2 G0P0(D) at ratio 0.8517, 0.9043, 0.9650, 0.9540 at those four D on Lb = 64 with d_pair = 1, 0.8757 and 0.9188 at D = 3, 4 with d_pair = 2, and 0.9575 and 0.8997 on Lb = 32; E_int is exactly the cross term of the quadratic form, <eps_12, G eps_12> minus the two self terms equalling 2 E_int to 1e-15 over all sixteen rows; the leading multipole correction from each source's dipole and traceless quadrupole moves the point form to 0.9380, 0.9146, 0.9773, 0.9576, accounting for the deficit to 1-3 per cent at |D| >= 3; and on two RIGID copies of one eps profile in the Lb = 64 box, a statement about the kernel and the source shape and not about a joint 8^3 state, the ratio is 0.9462, 0.9736, 0.9938, 0.9986 at D = 3, 4, 8, 16. (T3) The force F = -grad_{x2} E_int, by central differences on pair 2's centroid under rigid translation in the response box, equals F_pred = -E_2 grad phi_1(x_2) with phi_1 = G0 P0 eps_1 at x-component ratio 0.8271 and 0.9719 at D = 3, 4 for d_pair = 1 and 0.8568 and 0.9209 for d_pair = 2, with angle residuals 5.7, 6.5, 1.9 and 0.1 degrees; rebuilding a pair one coarse site over from a fresh seed is faithful only when the seed is carried by the KS field's gauge sign, translation residual 3.96e-01 naive against 2.10e-03 gauge-corrected, a named gauge artefact of the sign field; and on rigid copies the x ratio is 0.8981, 0.9854, 0.9982, 0.9992, 0.9997, 1.0000 at D = 3, 4, 6, 8, 10, 16 with the angle falling 7.3 to 1.8 degrees and the inverse-square coefficient 4 pi D^2 F_x / (E_1 E_2) reading 0.9711, 1.0398, 1.0216, 1.0060, 0.9924, 0.9260 against the source note's own point-kernel control 1.0194, 1.0064, 1.0009, 0.9963 at d = 4, 6, 8, 10; and the INTERACTION ENERGY is the on-shell action U = A* = -(1/2) <P0 rho, G0 P0 rho>, whose cross term is -E_int, so that F_U = -grad_{x2} U = -F_num at 4e-16 points from pair 2 toward pair 1 at every one of those D with the magnitudes and ratios above unchanged -- the pull is ATTRACTIVE, and the test-body law reads F = -E_test grad Phi_N with the Newtonian Phi_N = -phi, equivalently F = +E_test grad phi. (T4) The pooled object differs by vacuum: an energy knob at fixed D = 4, band-filtering one Gaussian seed toward +-E0 at width 0.6, carries E_exc through 3.8766, 4.5998, 5.3655, 5.8591, 6.0461 and lifts E_int by 2.525 while E_1 E_2 lifts by 2.425, a ratio of ratios of 1.041; the same bilinear form on the EMPTY vacuum's A-string count source, I = 2 per pair, reads E_int^count = 0.0655525 in every one of those rows at spread 0e+00, literally constant; and above the half-filled sea the count product is identically 0 by T1. The source note's T6 sentence, that the object the pooled response carries is the count product I(S) I(T) and NOT a mass product, stands unchanged on the empty vacuum it was proved on. UNITS ARE STATED, NOT DERIVED: the hop is t = 1 so m = E_exc/t is a dimensionless lattice number, G0 P0 carries a^-1, and no G_Newton, no coupling, no M_phys and no absolute unit appears; the source note's declared factor-two coarse/fine unit carry applies unchanged and is not adjudicated. This note chooses no vacuum, repairs neither of the two bridge clauses eps_v fails, stays strictly at the supplied linear response, and derives nothing from any axiom. No axiom is amended, no status is set, and no registry entry is created."
upstream_dependencies: []
runner: scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py
---

# The energy product and the test-body law above the half-filled sea

**Date:** 2026-09-03
**Type:** bounded_theorem, explicitly conditional on two supplied surfaces and one supplied vacuum choice
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:** [`scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py`](../scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py)
**Runner cache:** [`logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt`](../logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt)
**Parents:** none in the dependency sense. The two conditioning surfaces and the one conditioning choice are quoted in "Setting" as conditions, not consumed as graded rows.

The Newton lane carries two residuals that no landed note supplies: an identification of what plays the part of a mass, and a law saying how a second body responds to the field of the first. A landed note on the empty vacuum found that the object its pooled response
carries is a product of two counts, and said in terms that the identification of a count with a mass is a separate premise. A second landed note put matter above the half-filled staggered sea instead, found that the count of matter there is identically zero and the
excitation energy carries the landed monopole form, and named the choice between the two vacua as a decision about the framework that it did not make. This note takes that second vacuum as given and asks what the same bilinear response carries above it. The answer is
the product of the two excitation energies, with the same kernel; and the pull on a second lump is that lump's energy times the slope of the first lump's field. Both are candidates handed to the Newton lane by a vacuum choice, not by an axiom.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-dimensional numerical computations on named finite tori, every one conditional on two named supplied surfaces and one named supplied vacuum choice and on nothing else. Group B4's cross-term identity, group H's on-shell evaluation of the supplied action, and the structural statements of group A are exact identities of the quadratic form and of the one-body projector at machine tolerance; every other group is a finite floating-point computation reporting its residual against a tolerance declared before the run, and the response implementation is validated against both parents' own published point-source control before any new number is reported. Group E is a statement about units and derives nothing."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "The physical Newton residual is instead the source/test typing, mass-readout identification, and test-body response law. Current Record supplies none of the finite-additive scalar premise."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Route the undecided vacuum question, already named for its owner by the matter-above-the-sea note, together with what this note adds to each branch: on the half-filled sea the mass-readout identification has the candidate m = E_exc in units of t and the test-body response law the candidate form F = -E_test grad Phi_N with the Newtonian Phi_N = -phi, attractive, both within the supplied linear response; on the empty vacuum the count product stands unchanged. The choice, and the two bridge clauses eps_v still fails, remain open."
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below plus one stated unit paragraph, exactly the runner's check groups `A`-`E` and `H`: `T1` (`A`) the two-pair state and additivity; `T2` (`B`) the energy product; `T3` (`C`) the test-body magnitudes; `T3b` (`H`) the
on-shell action, and with it the direction of the pull; `T4` (`D`) count versus energy; and `E` the units. Each is established on named finite tori and carries its own tag: `[exact]` where the statement is an identity of the quadratic form or of the projector, `[numerical]` with a stated tolerance where it is floating point, and `[stated]` where it
records a convention rather than a computation.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the discrete Fourier inverse of the graph Laplacian, the multipole expansion of a Coulomb kernel, and central finite differencing are standard
methodology; every object is redeclared here and the runner recomputes every statement, including a validation of its own Green-function implementation against both parents' published point-source control before any new number is reported. The two surfaces and the one
vacuum choice this note is conditional on are declared, quoted and named in "Setting"; they are conditions of the result, not graded dependencies, and this note cites none of their grades and consumes no row. Non-load-bearing context pointers, plain file names with no
grade and no dependency weight: `MINIMAL_AXIOMS_2026-06-29.md` (the four axioms quoted below); `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`, the authority for the `1 / (4 pi |r|)` asymptotic;
`POISSON_FINITE_VOLUME_WINDOW_AND_BIHARMONIC_OFFSET_BOUNDED_THEOREM_NOTE_2026-07-27.md`, whose finite-volume window explains the roll-off of the inverse-square coefficient at large `D`; and `NEWTON_LAW_DERIVED_NOTE.md` together with
`RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md`, whose two residuals this note addresses conditionally and whose Non-Claims bound this whole exercise as they bound the parent lane.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local
possibilities," whose "full one-site possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." **Record**: "Records form. When
present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent. Only records are readable. A readout value is determined by record content alone."

The record ontology is what makes the objects below densities at all. Neither `n_v` nor the energy density `eps_v` is a new primitive and neither is a site: each is a **readout of six records**. The six fine edge sites `2v +- e_a` around the coarse corner `2v` each
carry a record; `B_v` is the product of their six `Z` values, so `n_v = (1 - B_v)/2` returns `1` exactly when those six records register odd parity and `0` when they register even. Nothing is read that is not a record, and the value is determined by record content
alone, as Record requires.

**Condition one -- the fermion law.** From `origin/physics-loop/emergent-3d-fermion-superlattice-existence:docs/EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md`, verbatim: "The **encoding** is the
Bravyi-Kitaev superfast encoding written on the coarse sublattice, with the code qubits exactly the coarse edge sites. The direction order at every coarse vertex is `-x < -y < -z < +x < +y < +z`." and "`B_i = -1` marks the excitation; the **hop** across the coarse edge
`(i, j)` is `T_ij = (i/2) A_ij (B_i - B_j)`." Its Proof boundary, verbatim and outranking every summary: "The law of Theorems 1 to 3 is a **designed supplier model**: Admissibility fixes that there is one covariant nearest-neighbour rule and leaves its form to the
supplier, and this note supplies one form and computes its consequences, deriving that form from no axiom and claiming for it no privileged status." Everything below inherits that conditional.

**Condition two -- the landed response, quoted with its action and its own force convention.** From `docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`, verbatim: the quadratic source action `A[phi; rho] = (1/2) <phi, H phi> - <P0 rho,
phi>` "has the unique stationary solution, modulo the constant zero mode, `phi = G0 P0 rho`." And, verbatim, the scope of that solve: "On finite periodic volumes the Poisson solve uses `P0 rho_psi`, i.e. the zero-mode-subtracted density. The zero mode is the
total-mass/background sector and is not part of the local force law." And, verbatim, its force statement: `U_test(phi; x) = -m phi(x)` and `F_x = -grad_x U_test = +m grad_x phi(x)` "with the sign fixed by the attractive potential convention in which a positive source has
`phi(r) > 0` and `grad phi` points inward at large separation." That surface is used exactly as landed, at linear order and nowhere beyond it, and its action is the object Theorem 3b evaluates.

**Condition three -- the vacuum, quoted as the choice it names and does not decide.** From `origin/physics-loop/matter-above-the-half-filled-sea:docs/MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md`,
verbatim: "**The two landed results are consistent with each other and not with a single vacuum.** Which state is the framework's vacuum is a decision about the framework, named here for its owner, not a residual to compute away." And, verbatim, the branch this note
takes as its condition: "**If the vacuum is the half-filled sea**: the staggered sector is selected by the hopping energy; the spectrum has a gapless point at the reduced-zone corner; matter comes in pairs; the energy density is the object that carries the monopole;
and the number-density deviation carries a dipole and no monopole." That branch is assumed here. It is not chosen here, and nothing below argues for it.

**The Newton lane's two residuals, quoted verbatim from the landed notes.** From `docs/NEWTON_LAW_DERIVED_NOTE.md` on `origin/main`, verbatim: the conditional audit "found that the test-mass force/source coupling" `F = -M_test grad(phi)` "was neither retained nor
registered as an approved admission", so that what the row proves is "an inverse-square gradient of a supplied `1/r` scalar kernel. It is not yet a physical Newton force law." Its Non-Claims list, verbatim, includes "the test-mass force/source response rule `F = -M_test
grad(phi)`" and "the physical product law `M_source M_test`". From `docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md` on `origin/main`, verbatim: "The physical Newton residual is instead the source/test typing, mass-readout
identification, and test-body response law", and its `next_trace_action`, verbatim: "Derive source/test typing, mass-readout identification, and the test-body response law; do not seek the scalar product in a pooled union value." Its own residual table records, verbatim,
that a route which would "Compose source and test-response linearities", where "A derived response `F=-m_t grad(phi)` yields the product without pooled recovery", is "the live Newton route, not ruled out", and its wall list, verbatim, is "`W1`: a scalar mass/readout
functional, including its finite-additive form if that form is intended; `W2`: physical source/test typing with separate accessibility; `W3`: the test-body response law", with every pair of those three independent.

**The empty-vacuum statement this note contrasts with.** From `origin/physics-loop/fermion-number-density-weak-field-source:docs/EMERGENT_FERMION_NUMBER_DENSITY_AS_WEAK_FIELD_SOURCE_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-02.md`, Theorem 6, verbatim: "So the object this
route delivers is `I(S) I(T)`, the product of two **counts**. It is emphatically **not** `M_source M_test`: no mass appears anywhere in this note, and the identification of a count with a mass is a separate premise this note neither supplies nor assumes." That
statement is about the empty vacuum, and this note leaves it exactly where it stands. Its `T4` point-kernel control, `4 pi d G_inf(d) = 1.0194, 1.0064, 1.0009` and `0.9963` at `d = 4, 6, 8, 10`, is quoted here **before** the run and used as the like-for-like comparison
for Theorem 3 item 4; the run fits nothing.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the strongest supported scope is precisely `P0`-`P5`. `P0`, declared here and conditional: the two supplied surfaces, the supplied vacuum choice, the coarse lattice,
the KS sign field, the twist, and the response operator. `P1` (`A`): the sea recomputed, and two pairs above it. `P2` (`B`): the energy product, validated against the landed point control first. `P3` (`C`): the test-body law, which uses `P1` for its states and `P2` for
its kernel. `P4` (`D`): count versus energy, which uses `P1` item 6 and `P2`. `P5` (`E`): the units, which derive nothing and depend on nothing. `P6` (`H`): the on-shell action and the direction of the pull, which uses `P0`'s
action, `P1`'s sources and `P3`'s differences.

## Definitions

Every object here is the parent's, unchanged. The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`. The **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`; a **twist** on axis
`a` flips the bonds crossing the cut `v_a = L-1 -> 0`. `M` is the symmetric integer hopping matrix on the coarse torus `L^3`, `P` the orthogonal projector onto its `V/2` lowest eigenvectors -- the **half-filled sea** -- and `E_sea` the sum of those levels. A **single
pair** is `P' = P - |h><h| + |p><p|` with `p` a normalised Gaussian seed projected into the empty span and `h` one projected into the occupied span, and a **two-pair state** is

```text
P'' = P - Q_h + Q_p          Q_h, Q_p the orthogonal projectors onto span{h1, h2} and span{p1, p2}
eps_v = sum_{j ~ v} M_vj (P'' - P)_vj        sum_v eps_v = tr(M (P'' - P)) = E_exc
rho_v = <n_v> - 1/2 = P''_vv - 1/2 = -<B_v>/2
```

The **internal separation** `d_pair` is the offset of a pair's hole from its particle, along `z`; the **centroid separation** `D` is the offset between the two pairs. The **response** is the landed one: `H = -Delta_lat` with the seven-point stencil, `G0 = H^{-1}` off
the constant mode, `P0` the projection off that mode, `phi = G0 P0 rho`. Each `eps_i` is unwrapped about its own pair midpoint, recentred on its rounded charge centroid -- the same integer shift for both copies, so their centroid separation is exactly `D` -- and
zero-padded into a response box `Lb^3`. The **positive bilinear form** is `E_int = <eps_1, G0 P0 eps_2>` and the **product form** is `E_1 E_2 G0P0(D)`, with `G0P0(D)` the same box's point-source kernel at the same offset. `E_int` is the object Theorem 2 measures against
that product; it is a bilinear form and carries no sign convention of its own.

The **interaction energy** is the quoted action at its own stationary point, `U = A* = A[G0 P0 rho; rho] = -(1/2) <P0 rho, G0 P0 rho>`, whose two-source cross term is `-<eps_1, G0 P0 eps_2> = -E_int`. The **Newtonian potential** is `Phi_N = -phi = -G0 P0 eps`, negative
near a positive source and increasing outward to zero. Where Theorem 2 writes `E_int` it means the positive bilinear form, whose on-shell counterpart is `-E_int`; the direction of every force is taken from `U`, never from `E_int`. A **rigid copy** is one `eps` profile
placed twice in the response box at separation `D`; it is a statement about the kernel and the source shape, and not a joint state on the `8^3` torus.

## Theorem 1 -- two pairs above the sea, and what is additive

**Conclusion.** On the `8^3` coarse torus at its energy-minimising twist `(1,1,1)`:

1. The vacuum is the parent's: `E_sea = -611.811768` to `3.5e-07` of that note's own quoted value, gap `2.651309 = 2 sqrt(6 - 3 sqrt2)` to `5.3e-15`, and `<n_v> = 1/2` at all `512` sites to `7.8e-16`. The single pairs are the parent's too: the band-edge orbital pair at
   `E_exc = 2.651309`, the localised wavepackets from `4.3614` to `4.5163` over `d = 1, 2, 3, 4`, and `sum_v eps_v = E_exc` at residual `0`.
2. Two such pairs at centroid separations `D = (2,0,0), (3,0,0), (4,0,0), (3,3,0)` and internal separations `d_pair = 1, 2` give a determinant state `P''` that is a projector, `max|P''^2 - P''| = 2e-15` over all eight states, with trace exactly `256 = V/2`.
3. The pairs decouple with `D`: `<p1|p2> = 0.37, 0.15, 0.044, 0.014` and `<h1|h2> = 0.38, 0.021, 0.0013, 0.0036`.
4. The energy is additive to the same order: `(E_12 - E_1 - E_2)/(E_1 + E_2) = -2.1e-02, -2.3e-03, -2.7e-04, -5.8e-05`, and the additivity defect of `eps_v` itself falls an order of magnitude per unit of `D`, `2.1e-01, 2.4e-02, 2.7e-03`.
5. `sum_v rho = 0` to `1e-14` for every single-pair state **and** for every joint state: the count above this sea is identically zero, not merely small.

**Proof.** Item 1 recomputes the parent's own table before anything new is built. Item 2 is an algebraic property of the projector, `Q_p` and `Q_h` being orthonormal bases of two-dimensional spans lying wholly inside the empty and the occupied shells; the trace is
integer arithmetic. Items 3 to 5 are `[numerical]` at the tolerances printed with them, all from the `512 x 512` one-body projector; no many-body object is formed anywhere.

**Reading, not theorem.** Two lumps of matter above this sea sit in one state that is still a closed shell, and the closer they are the more their clouds overlap. Far enough apart, the energy of the two together is the sum of the energies of each alone, and the energy
at each site is likewise the sum, to an accuracy that improves tenfold for every extra unit of distance. What the two lumps together carry no more of than one lump does is count: it is zero for one pair, zero for two, and zero exactly.

## Theorem 2 -- the energy product

**Conclusion.** With `phi = G0 P0 rho` the landed response, validated first: the point control `4 pi r G` at `r = Lb/4` gives `0.3307` and `0.3275` at `Lb = 32, 64`, both parents' own row, to `5e-06`. Then:

1. `E_int = <eps_1, G0 P0 eps_2>` against `E_1 E_2 G0P0(D)` has ratio `0.8517, 0.9043, 0.9650, 0.9540` at the four `D` on `Lb = 64` with `d_pair = 1`.
2. Neither the internal separation nor the box is doing the work: `d_pair = 2` on `Lb = 64` gives `0.8757` and `0.9188` at `D = 3, 4`, and `Lb = 32` gives `0.9575` and `0.8997` at `D = 4` for the two `d_pair`.
3. `E_int` is exactly the cross term: `<eps_12, G eps_12> - <eps_1, G eps_1> - <eps_2, G eps_2> = 2 E_int` to `1e-15` over all sixteen box-and-separation rows.
4. The deficit from `1` is the sources' shape. Adding each source's dipole and traceless quadrupole to the point form gives `0.9380, 0.9146, 0.9773, 0.9576`, closing the gap to `1`-`3` per cent at `|D| >= 3`.
5. On two rigid copies of one `eps` profile in the `Lb = 64` box the ratio is `0.9462, 0.9736, 0.9938, 0.9986` at `D = 3, 4, 8, 16`.

**Proof.** `G0` is the discrete Fourier inverse of `lambda(k) = 6 - 2 sum_a cos k_a` with the zero mode set to zero, which is `P0` exactly rather than approximately; each pairing is one forward transform per source and one spectral sum. Item 3 is an exact identity of the
quadratic form, `<a+b, G (a+b)> = <a, G a> + <b, G b> + 2<a, G b>` for symmetric `G`, evaluated rather than asserted. Item 4 uses the standard continuum expansion of `1/(4 pi |R - (u - v)|)` to dipole and traceless-quadrupole order in each source's own moments, with no
fitted coefficient and no window. Item 5 places one profile twice in the box by a phase factor; the moments are the same profile's, so the deficit there is the shape's and the box's alone.

**Reading, not theorem.** Put two lumps of matter above this sea a distance apart, and the energy the field carries between them is the energy of the first times the energy of the second times the same kernel the landed field equation already had. The shortfall from
that product at close range is not a different law but the fact that a lump is not a point: it has a width, a dipole and a quadrupole, and adding those two moments accounts for nearly all of the shortfall. Far apart, the shortfall goes away.

## Theorem 3 -- the test-body law, and the gauge-sign rebuild lemma

**Conclusion.** On `Lb = 64`, with `F_num = -grad_{x2} E_int` by central differences on pair 2's centroid under rigid translation in the response box, against `F_pred = -E_2 grad phi_1(x_2)` and `phi_1 = G0 P0 eps_1`. Both are built from the positive bilinear form
`E_int`, so what this theorem fixes is the magnitudes and the agreement of those two vectors with each other; the direction of the pull relative to the sources is Theorem 3b's:

1. The `x`-component ratio is `0.8271` and `0.9719` at `D = 3, 4` for `d_pair = 1`, and `0.8568` and `0.9209` for `d_pair = 2`.
2. The two vectors point the same way: the angle between `F_num` and `F_pred` is `5.7, 6.5, 1.9` and `0.1` degrees on those same four rows.
3. **The gauge-sign rebuild lemma.** Rebuilding pair 2 one coarse site over on the `8^3` torus from a fresh positive seed is **not** faithful: the translation residual `max|eps - shift(eps)|` is `3.96e-01`. Carrying the seed by the KS field's gauge sign first gives
   `2.10e-03`. The KS sign field is not translation invariant, only gauge equivalent, and the naive rebuild's discrepancy is that gauge artefact and not a property of the pair.
4. The law tightens with separation. On rigid copies at `D = 3, 4, 6, 8, 10, 16` the `x` ratio is `0.8981, 0.9854, 0.9982, 0.9992, 0.9997, 1.0000` and the angle falls from `7.3` to `1.8` degrees; the inverse-square coefficient `4 pi D^2 |F| / (E_1 E_2)` reads
   `0.9711, 1.0398, 1.0216, 1.0060, 0.9924, 0.9260` against the source note's own point-kernel control `1.0194, 1.0064, 1.0009, 0.9963` at `d = 4, 6, 8, 10`, the same finite-box roll-off in both.
5. **The law, with its sign.** The test-body law is `F = -E_test grad Phi_N` with the Newtonian `Phi_N = -phi_1`, equivalently `F = +E_test grad phi_1`, and it is attractive: on the rows of item 4 it is `-F_pred`, of the same magnitude at every `D` and directed from
   pair 2 toward pair 1. The earlier wording of this note, `F = -E_test grad phi` with `phi = G0 P0 eps_1 > 0`, is the like-charge sign convention -- `phi` is largest at the source, so that expression points away from it -- and is corrected here. It is also the
   convention the bridge itself quotes against, its own statement being `F_x = -grad_x U_test = +m grad_x phi(x)`. Every ratio, angle and coefficient in items 1, 2 and 4 is a magnitude and is unchanged by the correction; Theorem 3b establishes the direction.

**Proof.** Every derivative is the same central difference over one lattice unit, taken on the numerical energy and on the predicted potential alike, so no differencing scheme separates them. The rigid translation is exact in the response box, a phase factor on the
source transform, which is precisely the bridge's own linear response and introduces no rebuild of the state. Item 3 is a controlled comparison: the same pair, the same site, one seed carried by the gauge sign and one not, with the translation residual reported for
both. Item 4's coefficient is compared against the landed control quoted before the run, on the same boxes and with the same readout; the roll-off at `D = 16` is the finite-volume window's, present in the control as it is here. Item 5's sign is not read off items 1 to 4,
which compare two vectors built from the same positive bilinear form and so agree with each other whichever way both point; it is Theorem 3b's, taken from the on-shell value of the supplied action, and items 1, 2 and 4 are quoted there unchanged.

**Reading, not theorem.** The pull on the second lump is the second lump's energy times the slope of the first lump's field, and the two agree in direction to within a few degrees. The agreement is not exact at close range for the same reason the product was not exact
at close range -- a lump has a width -- and it goes to one as the lumps separate. Which way that pull points, against the lumps themselves, is settled in the next theorem and not here. One thing needs care: the sign field that carries the hop is not the same at a shifted site, so a lump rebuilt one site over from scratch is not the same lump translated.
Carrying the seed by the field's own sign restores it, and that difference is a property of the sign field, named here rather than absorbed.

## Theorem 3b -- the interaction energy is the on-shell action, and the pull is attractive

**Conclusion.** With `U = A*` the quoted action evaluated at its own stationary point, on `Lb = 64` and the same sources:

1. Evaluating `A[phi; rho] = (1/2) <phi, H phi> - <P0 rho, phi>` at `phi = G0 P0 rho`, with `H` the same seven-point stencil applied in the box, gives `A* = -(1/2) <P0 rho, G0 P0 rho>` at relative residual `5e-15`, on the two-pair source at all four `D`.
2. Its two-source cross term is `A*_12 - A*_1 - A*_2 = -E_int`, reading `-0.522027` at `D = (4,0,0)` against Theorem 2's `E_int` to `6e-15`: the negative of the positive bilinear form.
3. `F_U = -grad_{x2} U` by the same central differences is `-F_num` to `4e-16` and of the same magnitude to `4e-16`, and its `x`-component is negative at every `D` of Theorem 3 item 4, `-2.808e-01` at `D = 3` through `-9.413e-03` at `D = 16`, with pair 2 at `+x`:
   the second lump is pulled toward the first.
4. That force is `F_U = -E_2 grad Phi_N` with `Phi_N = -phi_1`, to `0e+00`; equivalently `F_U = +E_2 grad phi_1`, which is the convention the bridge states for itself.

**Proof.** Item 1 evaluates both sides from their definitions rather than asserting the identity: the stencil is applied in the box for `<phi, H phi>` and the spectral solve supplies `phi`. The algebra it checks is that `<phi*, H phi*> = <P0 rho, phi*>` at the stationary
point, so `A* = (1/2) <P0 rho, phi*> - <P0 rho, phi*> = -(1/2) <P0 rho, G0 P0 rho>`. Item 2 is item 1's sign applied to the bilinear expansion already evaluated in Theorem 2 item 3: `A*` is `-(1/2)` of the quadratic form, so its cross term is `-<eps_1, G0 P0 eps_2>`.
Item 3 differences `U` itself, self terms included, at the shifted positions, so the cancellation of the position-independent self terms is carried out numerically rather than assumed. Item 4 builds `Phi_N` as an array and differences it exactly as Theorem 3 differences
`phi_1`.

**Reading, not theorem.** The energy the field holds when two lumps sit a distance apart is the value of the action at the field they produce, and that value falls as the lumps approach. A force points down an energy, so the pull is toward the other lump. The size of it
is the same number as before and every ratio in Theorem 3 stands; what changes is which way it points, and which potential's slope gives it -- the negative one, deepest at the lump and rising to nothing far away.

## Theorem 4 -- count versus energy: the pooled object differs by vacuum

**Conclusion.**

1. An energy knob at fixed `D = 4` -- one Gaussian seed band-filtered toward `+-E0` at width `0.6` -- carries `E_exc` through `3.8766, 4.5998, 5.3655, 5.8591, 6.0461`. Across those rows `E_int` lifts by a factor `2.525` while `E_1 E_2` lifts by `2.425`: a ratio of
   ratios of `1.041`.
2. The **same** bilinear form on the empty vacuum's count source -- two `A`-string pairs, `<n_v> = 1` at each string's two endpoints, `I = 2` per pair -- reads `E_int^count = 0.0655525` in every one of those rows, at spread `0e+00`. It is literally constant while the
   excitation's energy quadruples.
3. Above the half-filled sea the count product is identically `0`: `sum_v rho = 0` to `1e-14` by Theorem 1 item 5, so `I_1 I_2 = 0` there, while `E_1 E_2 = 32.25` for the same two pairs.
4. So the source note's Theorem 6 sentence stands unchanged where it was proved -- the object the pooled response carries is the count product `I(S) I(T)` and **not** a mass product, on the **empty** vacuum -- and above the half-filled sea the same form carries the
   **energy** product instead. The difference between the two is the vacuum and nothing else in this computation: same encoding, same hop, same kernel, same bilinear form.

**Proof.** Item 1's knob changes only the band filter applied to a fixed Gaussian seed, so the source stays localised and the only thing that moves is the excitation's energy; the ratio of ratios is reported rather than fitted. Item 2's count source is placed at the
same two centroids in the same box, so the kernel and the geometry are identical to item 1's and the only difference is which readout is used as `rho`; its constancy is a consequence of the count being an integer property of the string endpoints. Item 3 is Theorem 1
item 5 restated as a product. Item 4 is an implication of items 1 to 3 together with the quoted sentence, not a new computation.

**Reading, not theorem.** Turn up the energy of a lump without changing how many things are in it, and the pull between two such lumps grows in the same proportion as the product of their energies. The count reading does not move at all: it is the same number in every
row. Above the half-filled sea the count reading is not merely constant but zero, so nothing can be built from it. Which of the two objects the response carries is settled by which state is called the vacuum, and by nothing else here.

## Corollary -- what the vacuum choice supplies to the Newton lane

Within the setting declared above, conditional on the two supplied surfaces and on the supplied vacuum choice, and on the finite tori named:

1. **The bilinear response carries the energy product.** Conditional on the half-filled sea and on the energy density as the source, `E_int` equals `E_1 E_2 G0P0(D)` with the landed kernel, at a ratio that the sources' own dipole and quadrupole account for at short
   range and that goes to `1` as the sources separate, `0.9986` at `D = 16` on rigid copies.
2. **The test-body law holds within the bridge's linear response, and it is attractive.** `F = -E_test grad Phi_N` with the Newtonian `Phi_N = -phi`, equivalently `F = +E_test grad phi`, reproduces `-grad_{x2} U` at `x`-ratio `1.0000` and angle `1.8` degrees by
   `D = 16`, with the landed inverse-square coefficient and the landed finite-box roll-off, and points from the second lump toward the first at every `D`. The earlier wording here, `F = -E_test grad phi`, was the like-charge sign convention and is corrected.
3. **So the Newton lane's two residuals have candidates, supplied by a vacuum choice rather than by an axiom.** The mass-readout identification has the candidate `m = E_exc`, in units of the hop `t`; the test-body response law has the candidate form `F = -E_test grad
   Phi_N` with `Phi_N = -phi`, attractive. Both are conditional on the half-filled sea being the framework's vacuum, which is not decided here or anywhere yet, and neither is derived from any axiom.
4. **On the empty vacuum nothing changes.** The source note's count product `I(S) I(T)` stands exactly as proved, and this note supplies no reason to prefer either branch.
5. **What is not repaired.** `eps_v` still fails two of the bridge's five source clauses -- it is not diagonal, the hop's `A_ij` carrying an `X`, and it is not guaranteed positive -- exactly as the parent's Theorem 5 records. This note uses `eps_v` as the parent's
   supplied even datum and repairs neither clause.

**Reading, not theorem.** Above the half-filled sea a lump of matter pulls on another lump in proportion to the product of their energies, with the same fall-off the landed field equation already had; the pull on the second lump is its energy times the slope of the first
lump's field, and it draws the second lump toward the first. Whether that is the framework's gravity turns on whether the half-filled sea is the framework's vacuum, which is not yet decided.

## What does not move

- No vacuum is chosen. The half-filled sea is taken as a **condition**, quoted from the note that names it as an undecided choice, and nothing here argues for or against either branch.
- No mass, no `M_phys`, no `G_Newton`, no coupling constant, and no absolute unit appears anywhere. `m = E_exc/t` is a dimensionless lattice number and is offered as a candidate identification, not as a mass.
- The bridge's five source clauses are not repaired. `eps_v` fails two of them above this vacuum and still does.
- Nothing at nonlinear order, no back-reaction, no self-consistency between the field and the state that sources it. Everything here is the supplied linear response.
- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

- **The vacuum decision.** Still the parent's, still open, still for its owner. What this note adds is one more consequence on the half-filled branch: on that branch the mass readout and the test-body law both have candidate forms, and on the empty branch the count
  product stands. The decision is not made easier or harder by that; it is made more explicit.
- **The two failed clauses of `eps_v`.** A lane wanting a source above this sea that meets all five clauses owns them. Theorem 4 uses `eps_v` because the parent found it carries the monopole, not because it passes.
- **`G_Newton` and the unit carry.** Nothing here fixes a scale. The source note's declared factor-two coarse/fine carry -- reading (i) `1/(4 pi d_coarse) = 1/(2 pi |r_fine|)` against reading (ii) `1/(4 pi |r_fine|)` -- applies unchanged and is not adjudicated.
- **Back-reaction and self-consistency.** The field here is sourced by a fixed state and does not act back on it. A lane wanting a self-consistent pair owns that.
- **Larger physical tori.** Joint two-pair states exist here only to `|D| <= 4`, the `8^3` torus's own limit. Everything beyond that separation is rigid copies in the response box, labelled as such.

## Remaining live routes

1. Physical tori beyond `8^3`, where joint states at larger `D` would replace the rigid copies of Theorem 2 item 5 and Theorem 3 item 4.
2. A source above this sea meeting all five bridge clauses, which would remove the parent's Theorem 5 caveat from everything here.
3. Nonlinear order and back-reaction, both untouched.
4. The vacuum decision itself, which is not a computation.

## Executable claim block

The canonical machine-bound restatement of the four theorem conclusions and the unit statement.

```text
conditional_on: the supplied fermion law (declared supplier model, derived from no axiom); the landed weak-field response phi = G0 P0 rho at linear order; and the CHOICE of the half-filled staggered sea as the vacuum, quoted from the note that names it undecided
vacuum: 8^3 coarse torus, twist (1,1,1), E_sea = -611.811768 (3.5e-07 of the parent's own value), gap 2.651309 = 2 sqrt(6 - 3 sqrt2) (5.3e-15), <n_v> = 1/2 at all 512 sites (7.8e-16)
two_pair_state: P'' = P - Q_h + Q_p is a projector to 2e-15 with trace exactly 256 = V/2, at D = (2,0,0)/(3,0,0)/(4,0,0)/(3,3,0) and d_pair = 1, 2
decoupling: <p1|p2> = 0.37/0.15/0.044/0.014 and <h1|h2> = 0.38/0.021/0.0013/0.0036 at those four D
additivity: (E_12 - E_1 - E_2)/(E_1 + E_2) = -2.1e-02/-2.3e-03/-2.7e-04/-5.8e-05; the eps_v additivity defect falls an order of magnitude per unit of D, 2.1e-01/2.4e-02/2.7e-03
count_above_the_sea: sum_v rho = 0 to 1e-14 for every single-pair AND every joint state; the count product is identically 0 there
response_validation: point control 4 pi r G at r = Lb/4 = 0.3307/0.3275 at Lb = 32/64, both parents' own row, to 5e-06
energy_product: E_int/(E_1 E_2 G0P0(D)) = 0.8517/0.9043/0.9650/0.9540 at Lb = 64, d_pair = 1; 0.8757/0.9188 at D = 3, 4 with d_pair = 2; 0.9575/0.8997 at Lb = 32, D = 4
cross_term_identity: <eps_12, G eps_12> - <eps_1, G eps_1> - <eps_2, G eps_2> = 2 E_int to 1e-15 over all sixteen rows
multipole_accounting: point form corrected by each source's dipole and traceless quadrupole gives 0.9380/0.9146/0.9773/0.9576, closing the deficit to 1-3 per cent at |D| >= 3
large_separation: two RIGID copies of one eps profile on Lb = 64 (kernel and source shape, NOT a joint 8^3 state) give 0.9462/0.9736/0.9938/0.9986 at D = 3/4/8/16
test_body_magnitudes: F_x(-grad E_int)/F_x(-E_2 grad phi_1) = 0.8271/0.9719 at D = 3, 4 with d_pair = 1 and 0.8568/0.9209 with d_pair = 2; angles 5.7/6.5/1.9/0.1 degrees
gauge_rebuild_lemma: rebuilding a pair one coarse site over from a fresh seed gives translation residual 3.96e-01; carrying the seed by the KS gauge sign gives 2.10e-03 -- a sign-field artefact, named
force_scaling: rigid copies at D = 3/4/6/8/10/16 give x-magnitude ratio 0.8981/0.9854/0.9982/0.9992/0.9997/1.0000, angle 7.3 -> 1.8 degrees
inverse_square: 4 pi D^2 |F|/(E_1 E_2) = 0.9711/1.0398/1.0216/1.0060/0.9924/0.9260 against the source note's point control 1.0194/1.0064/1.0009/0.9963 at d = 4/6/8/10
on_shell_action: A[phi; rho] = (1/2)<phi, H phi> - <P0 rho, phi> at phi = G0 P0 rho is A* = -(1/2) <P0 rho, G0 P0 rho> to 5e-15 relative on the two-pair source at all four D; its two-source cross term is -E_int, -0.522027 at D = (4,0,0), to 6e-15
attraction: with U = A* the interaction energy, F_U = -grad_{x2} U = -F_num to 4e-16 at magnitude unchanged to 4e-16, x-component NEGATIVE at every D = 3/4/6/8/10/16 (-2.808e-01 through -9.413e-03) with pair 2 at +x: the second lump is pulled TOWARD the first
test_body_sign: F = -E_test grad Phi_N with the Newtonian Phi_N = -phi, equivalently F = +E_test grad phi, to 0e+00 -- attractive, and the bridge's own quoted convention. The earlier F = -E_test grad phi was the like-charge sign convention and is corrected; every magnitude above is unchanged
energy_knob: E_exc = 3.8766/4.5998/5.3655/5.8591/6.0461 at fixed D = 4; E_int lifts by 2.525 while E_1 E_2 lifts by 2.425, ratio of ratios 1.041
count_knob: the same bilinear form on the EMPTY vacuum's A-string count source (I = 2 per pair) reads E_int^count = 0.0655525 in EVERY row, spread 0e+00 -- literally constant
pooled_object: the count product I(S) I(T) on the empty vacuum, unchanged from the source note's T6; the energy product E_1 E_2 above the half-filled sea; the difference is the VACUUM and nothing else here
units: hop t = 1 so m = E_exc/t is a dimensionless lattice number; G0 P0 carries a^{-1} so E_int is in t^2/a; the source note's factor-2 coarse/fine carry applies unchanged and is not adjudicated
not_supplied: any choice of vacuum, G_Newton, a coupling, M_phys, an absolute unit, a repair of the two bridge clauses eps_v fails, anything nonlinear, back-reaction, joint states beyond |D| = 4
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=25 FAIL=0
```

## Proof boundary

The fermion law is a **designed supplier model**, in that note's own words "deriving that form from no axiom and claiming for it no privileged status"; the weak-field response is likewise a supplied surface, bounded in its own note; and the vacuum is a **choice**, quoted
from the note that names it as undecided and takes no side. Every statement above inherits all three: if any one is not the framework's, nothing above survives except as a statement about what was supplied. Nothing here is derived from any axiom.

Everything is at **linear order** in the supplied response, and at **finite volume**. The source is built on the `8^3` physical coarse torus and nowhere else, so joint two-pair determinant states exist here only to `|D| <= 4`; every separation beyond that is two rigid
copies of one profile in the response box, which is a statement about the kernel and the source shape and not about a joint state, and is labelled as such at every occurrence. Response boxes are `Lb = 32` and `64` and nowhere else. The finite-box roll-off of the
inverse-square coefficient at `D = 16` is the landed window's and is present in the like-for-like control too; it is reported rather than extrapolated away.

The **wavepacket placement is a choice**, as it was in the parent: the particle and hole are normalised Gaussians of unit width centred at named sites and projected into the empty and the occupied spans, and the energy knob of Theorem 4 is a band filter on that same
seed. `E_exc` varies by a few per cent across placements and every number is reported per configuration rather than averaged. The **twist cut** is named: with the pairs based at `x = 2` the `D = 3` translations stay off the cut, while a `+x` translation at `D = 4` lands
on it, which is why the reported force rows are the rigid ones -- exact translations in the response box -- and the rebuilt rows appear only in the gauge lemma of Theorem 3 item 3.

**No vacuum is chosen and no mass is claimed.** `m = E_exc/t` is a dimensionless lattice number offered as a candidate identification on one branch of an undecided question; it is not a mass, and no `G_Newton`, coupling or absolute unit appears. The two bridge clauses
`eps_v` fails above this vacuum are not repaired. Nothing nonlinear and no back-reaction is touched. No axiom is amended, no status is set, and no registry entry is created.

## Review record

An honest auditor should come away with: a conditional computation, not a derivation; four statements on named finite tori, one of them an exact identity of the quadratic form; a clean separation between what is a joint state on the physical torus and what is two rigid
copies in a response box, marked at every occurrence rather than left to the reader; a deficit from the ideal product form that is explained by the sources' own two leading moments rather than absorbed into a tolerance; one gauge artefact of the sign field found,
isolated by a controlled comparison, and named rather than corrected quietly; one sign convention corrected on review, the interaction energy being the on-shell value of the supplied action rather than the positive bilinear form, so that the pull is attractive and the
test-body law reads `F = -E_test grad Phi_N` -- every magnitude, ratio and coefficient in the note is unchanged by that correction; and a contrast between two vacua in which the earlier landed statement about the empty one is quoted verbatim and left exactly where it
stands. Nothing here is a fitted number: the response
implementation is validated against both parents' own published control before any new value is reported, the inverse-square comparison uses a control quoted before the run, and every finite difference is taken identically on the computed and the predicted quantity.
The note is self-contained in the sense that matters for replay -- `upstream_dependencies` is empty, every object is declared in "Definitions", the runner imports nothing from the repository, and the two conditioning surfaces and the one conditioning choice are quoted
verbatim with paths rather than consumed as graded rows. The one thing an auditor should press hardest on is the conditional itself: the whole result is about a vacuum nobody has chosen, and the note says so in its scope, its corollary and its boundary. Hard landing
conditions are a fresh runner and cache pair closing at `PASS=25 FAIL=0` with runtime under the declared timeout and stdout under `5500` characters, and passing repository pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
````

## original-cutoff live — logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt

SHA-256 `b5c2284b57a4fc4bddb28bf71bf239fa0724e45fc2b82fd281e88df271db33b4`. Verbatim body follows.

````text
===== runner cache v1 =====
runner: scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py
runner_sha256: b7d36311c3ae65187b5e4a27f8eb5f7b9a18462fccf0c4d12389b2a63d679374
timeout_sec: 300
exit_code: 0
elapsed_sec: 1.07
status: ok
----- stdout -----
PASS A1 [numerical, 1e-6] the conditioning vacuum: the half-filled staggered sea on 8^3 at twist (1,1,1), E_sea = -611.811768 (the matter note's, 3.5e-07), gap 2.651309 = 2 sqrt(6 - 3 sqrt2) (5.3e-15), <n_v> = 1/2 at all 512 (7.8e-16)
PASS A2 [numerical, 1e-13] single pairs: band-edge orbital E_exc = 2.651309, localised wavepackets 4.3614 to 4.5163 over d = 1..4, sum_v eps_v = E_exc to 0e+00 -- the matter note's 2.651309, 2.6513-4.5163
PASS A3 [numerical, 1e-14] TWO pairs at D = (2,0,0)/(3,0,0)/(4,0,0)/(3,3,0): P'' = P - Q_h + Q_p is a projector to 2e-15 over eight states, trace exactly 256 = V/2
PASS A4 [numerical] the pairs decouple with D: <p1|p2> = 0.37/0.15/0.044/0.014, <h1|h2> = 0.38/0.021/0.0013/0.0036 at those D
PASS A5 [numerical] the joint energy is additive: (E_12 - E_1 - E_2)/(E_1 + E_2) = -2.1e-02/-2.3e-03/-2.7e-04/-5.8e-05 at d_pair = 1, -2.3e-03/-2.7e-04 at d_pair = 2; the eps_v defect falls an order per unit of D, 2.1e-01/2.4e-02/2.7e-03
PASS A6 [numerical, 1e-13] the COUNT above this sea is identically zero: sum_v (<n_v> - 1/2) = 0 to 1e-14 for every single-pair AND every joint state, so a count product is exactly 0
PASS B1 [numerical, 1e-4] validation before any new number: the landed G0, Fourier inverse of lambda(k) off the constant mode; point control 4 pi r G at r = Lb/4 = 0.3307 and 0.3275 at Lb = 32, 64, both parents' own row (5e-06)
PASS B2 [numerical, 1e-9] THE ENERGY PRODUCT. E_int = <eps_1, G0 P0 eps_2> against E_1 E_2 G0P0(D), Lb = 64, d_pair = 1: ratio 0.8517/0.9043/0.9650/0.9540 at those four D -- the ENERGY product
PASS B3 [numerical, 1e-9] neither the internal separation nor the box does the work: d_pair = 2 on Lb = 64 gives 0.8757/0.9188 at D = 3, 4; Lb = 32 gives 0.9575 (d_pair 1) and 0.8997 (d_pair 2) at D = 4
PASS B4 [numerical, 1e-14] E_int is exactly the cross term: <eps_12, G eps_12> - <eps_1, G eps_1> - <eps_2, G eps_2> = 2 E_int to 1e-15 over all sixteen rows
PASS B5 [numerical] the deficit from 1 is the sources' SHAPE: each source's dipole and traceless quadrupole added to the point form give 0.9380/0.9146/0.9773/0.9576 against B2's, closing it to 1-3 per cent at |D| >= 3
PASS B6 [numerical] the ratio goes to 1 with separation: two RIGID copies of one eps profile in the Lb = 64 box -- kernel and source shape, NOT a joint 8^3 state -- give 0.9462/0.9736/0.9938/0.9986 at D = 3/4/8/16
PASS C1 [numerical, 1e-9] TEST-BODY MAGNITUDES, sign in H. F_num = -grad_{x2} E_int by central differences on pair 2's centroid against F_pred = -E_2 grad phi_1: x ratio 0.8271/0.9719 at D = 3, 4 for d_pair = 1, 0.8568/0.9209 for d_pair = 2, Lb = 64
PASS C2 [numerical] and they point the same way: the angle between F_num and F_pred is 5.7/6.5/1.9/0.1 degrees on those four rows
PASS C3 [numerical] the GAUGE-SIGN REBUILD LEMMA: pair 2 rebuilt one coarse site over from a fresh seed is NOT faithful, translation residual 3.96e-01 against 2.10e-03 when the seed is carried by the KS gauge sign -- a sign-field artefact
PASS C4 [numerical] it tightens with separation: on rigid copies at D = 3/4/6/8/10/16 the x ratio is 0.8981/0.9854/0.9982/0.9992/0.9997/1.0000, the angle falls 7.3 -> 1.8 degrees
PASS C5 [numerical] inverse-square with the landed coefficient: 4 pi D^2 |F|/(E_1 E_2) = 0.9711/1.0398/1.0216/1.0060/0.9924/0.9260 against the source note's control 1.0194/1.0064/1.0009/0.9963
PASS D1 [numerical] COUNT VERSUS ENERGY. An energy knob -- a Gaussian seed band-filtered toward +-E0, width 0.6 -- moves E_exc through 3.8766/4.5998/5.3655/5.8591/6.0461 at D = 4: E_int rises to 2.525, E_1 E_2 to 2.425, ratio of ratios 1.041
PASS D2 [numerical, 1e-12] the SAME form on the empty vacuum's count source -- two A-string pairs, I = 2 per pair -- reads E_int^count = 0.0655525 in EVERY row, spread 0e+00: constant while the excitation's energy quadruples
PASS D3 [numerical, 1e-13] and above this sea that count source does not exist: sum_v rho = 0 to 1e-14 for every pair and every joint state, so I_1 I_2 = 0 while E_1 E_2 = 32.25 for the same pairs. The pooled object differs BY VACUUM
PASS D4 [stated] so the source note's T6 stands where it was proved -- 'the count product I(S) I(T) and NOT a mass product', on the EMPTY vacuum -- while above this sea the same form carries the ENERGY product
PASS E1 [stated] units: hop t = 1, so E_exc is in t and m = E_exc/t is a dimensionless lattice number; G0 P0 carries a^{-1}, so E_int is in t^2/a. No G_Newton, coupling or M_phys appears; the source note's factor-2 carry is not adjudicated
PASS H1 [numerical, 1e-14] THE ON-SHELL ACTION. A[phi; rho] = (1/2)<phi, H phi> - <P0 rho, phi> at phi = G0 P0 rho is A* = -(1/2)<P0 rho, G0 P0 rho> to 5e-15; its cross term -0.522027 at D = 4 is exactly -E_int to 6e-15
PASS H2 [numerical, 1e-14] SO THE PULL IS ATTRACTIVE. F_U = -grad_{x2} A*, same central differences, is -F_num to 4e-16 at unchanged magnitude (4e-16); F_U,x = -2.808e-01 to -9.413e-03 is NEGATIVE at every D = 3/4/6/8/10/16 -- pair 2 pulled TOWARD pair 1
PASS H3 [numerical, 1e-14] the test-body law: F_U = -E_2 grad Phi_N with the Newtonian Phi_N = -phi_1, to 0e+00, i.e. F_U = +E_2 grad phi_1; C1-C5's ratios, angles and coefficient are unchanged
SUMMARY: on the half-filled sea as the vacuum, the bridge's response carries the product of the two excitation energies with the landed kernel, ratio -> 1 with separation, and the pull is ATTRACTIVE: F = -E_test grad Phi_N, Phi_N = -phi. From that choice, not an axiom.
TOTAL: PASS=25 FAIL=0

----- stderr -----

````

## original-cutoff live — docs/THE_VACUUM_QUESTION_IS_ONE_COEFFICIENT_OF_THE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md

SHA-256 `14077ae9413537077600e83d8bd380ecbefe41687a23063a31a092ca9256c3d1`. Verbatim body follows.

````text
---
claim_id: vacuum_question_one_coefficient_occupancy_cost
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3 carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with free nearest-neighbour hopping of strength t = 1 and the encoding's own site operator B_i given a coefficient -- the occupancy term -J_B sum_i B_i, declared here and not derived -- on the named finite blocks and tori only: (T1) sum_i B_i commutes with every encoded hop T_ij = (i/2) A_ij (B_i - B_j), exactly, over all 16029 (hop, site) Pauli-string sign pairs on the open 2x2x2 and 3x3x3 blocks and the tori 3^3 and 4^3, by the identity [sum_k B_k, T_ij] = -i (B_i^2 - B_j^2) A_ij = 0, while a single B_i does not, ||[B_i, T_ij]|| = 2 against ||[sum_k B_k, T_ij]|| = 0 on a dense 16-dimensional block; and (V I - sum_i B_i)/2 is the record-number operator there, so -J_B sum_i B_i = -J_B V + 2 J_B N is a pure chemical potential of 2 J_B per fermion and adds no dynamics. (T2) At J_B = 0 the global minimum over record numbers and flux sectors is the half-filled staggered sea: every cluster here is bipartite with all degrees 6, so its spectrum is symmetric about 0 to 3.4e-14 and min_N E_N = E_{V/2} for every link-sign field, attained on the tie range [#neg, #neg + #zero] (plain 4^3 untwisted: 20 zero modes, ties N in [22, 42]); on the open 2x2x2 cube all 32 consistent sectors at all N give -4 sqrt3 uniquely at the all-(-1) sector and N = 4, by a margin of 0.456067; on the 4^3 torus the minimum is -32 sqrt6, the Cauchy-Schwarz floor over ALL link-sign fields, checked against 8 twists times 2 uniform sectors, 5 structured sectors and 1000 random fields; elsewhere the same sector wins as a search result, -258.857540 on 6^3 (8 twists times 2 plus 300 random, best random -230.81), -611.811768 on 8^3, and -26.040600 against -21.213203 on the open 3x3x3. (T3) With W(J_B) = sum over levels below -2 J_B of (eps + 2 J_B), twist-minimised at each J_B, the ground state moves continuously from the half-filled staggered sea to the empty lattice, and the optimal Wilson twist changes with J_B. (T4) The plain sector overtakes the staggered one at J_B* = sqrt3/2 exactly on the 4^3 torus -- the staggered KS twist has W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J against the plain (0,1,1) twist's W = -24 - 24 sqrt2 + 40 J, difference 16 J - 8 sqrt3 -- at 0.849332 on 6^3, 0.867676 on 8^3 and 0.8654003 +- 3e-6 in the thermodynamic limit, where the fillings there are 0.4417 and 0.2521; the emptying thresholds J_B >= |eps_min|/2 are 3 exactly for the plain sector, band bottom -6 at (pi, pi, pi), and sqrt3 for the staggered one, on all three tori and in the limit; 3 sqrt2/2 and sqrt6/2 on the open 3x3x3; 3/2 on the cube, where all 32 sectors tie at W = 0; and on the cube the all-(-1) sector loses to the 2-flux class at sqrt3 - (1 + sqrt2)/2 = 0.524944. (T5) For ANY link-sign field on a bipartite degree-6 cluster, tr M^2 = 6V and D M D = -M give W(J) >= min_m [-sqrt(3 V m) + 2 J m] = -V sqrt(3/2) + J V for J <= sqrt(3/8) = 0.612372 and -3V/(8J) above; the 4^3 flat-twist staggered sea has W = 64 J - 32 sqrt6 and attains that floor with slack at most 7e-15 at every J_B <= sqrt(3/8), so it is a global minimiser over all link-sign fields AND all record numbers on that interval. (T6) Exactly half filling survives for J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = 0.823267 twist-minimised on 4^3 and for J_B < sqrt6/2 within the half-filling twist, for J_B < 2 sqrt3 - 3 = 0.464102 on 6^3 and J_B < 0.306846 on 8^3; in the thermodynamic limit the staggered band is gapless at q = (pi, pi, pi), so exactly half filling survives only at J_B = 0, with 1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3. T2 away from the cube and the 4^3 torus is a search result, not a theorem. The occupancy term and its coefficient are declared by this note, not derived from any axiom; no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py
---

# The vacuum question is one coefficient of the law

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py`](../scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.txt`](../logs/runner-cache/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

Three notes sit next to each other. One says that on the coarse lattice the half-filled staggered sea is what the hopping term prefers, and that the filling which selects it is a supplied datum. The other says that the empty state and the
half-filled sea have different and incompatible consequences, and asks which of them the framework calls its vacuum. A third says that the encoding's site operator `B_i` is a term type of the declared law and that no coefficient is attached to it
anywhere. Put those three together and the vacuum question has a shape: give `B_i` the coefficient the law leaves blank, and the answer is a number. This note computes what that number does.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems on the ground state of free coarse-lattice hopping plus an occupancy term -J_B sum_i B_i: exact Pauli-string commutation making the term a pure chemical potential, exhaustive enumeration on the open 2x2x2 cube, exact surd crossings on the 4^3 torus, and an extended Cauchy-Schwarz certificate valid at every J_B <= sqrt(3/8). The sampling items are declared search results, not theorems, and the thermodynamic items are converged Bloch quadrature. The occupancy term and its coefficient are declared, not derived."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: what value the dimensionless coefficient J_B/t takes."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`. Group `A` is exact Pauli-string and dense matrix arithmetic at zero tolerance; the surd statements of `B`, `C`, `D` and `E` are exact in `sympy`;
and the items tagged `[numerical]` are floating-point statements at the stated tolerance. Global minimality is a theorem on the cube and on the `4^3` torus and a **search result** elsewhere, labelled so wherever it appears.

The six are `T1` (`A`), the occupancy term as a pure chemical potential of `2 J_B` per fermion; `T2` (`B`), the half-filled staggered sea as the global ground state at `J_B = 0` over all record numbers and all sectors; `T3` (`C`), the ground state as
a function of `J_B`, twist-minimised at each `J_B`; `T4` (`C`), the crossover `J_B*` and the emptying thresholds; `T5` (`D`), the extended certificate on the `4^3` torus for `J_B <= sqrt(3/8)`; and `T6` (`E`, `F`), the half-filling persistence
windows and the gapless thermodynamic limit.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering and the tight-binding dispersion are standard methodology; every object is redeclared here and the runner recomputes every statement.
No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the declared law and its term census, quoted below. Pointer only; the encoding, `B_i` and the hop are redeclared here
  and recomputed by this runner.
- `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7874): the supplied-filling sentence quoted below.
- `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7879): the vacuum question as that note names it, quoted below.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". This note cites none of their grades and adopts no hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." **Qubit**: "Each site has
a domain of local possibilities", whose "full one-site possibility domain has algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a record locks exactly one admissible local possibility", "records
are permanent", "Only records are readable."

The law whose coefficient is in question is the one PR #7834 declares. Its term census reads, verbatim:

> 1. Of the `16` quantum term types (three `A_ij`, six hop components, three hop totals, `B_i`, three face stabilizers) and the `49` marker term types (the `48`
>    templates and the no-role penalty), `4` are star-local -- `A_x`, the `A B_i` component along `x` and along `z`, and `B_i` -- `61` are through with an
>    explicitly constructed `6`-connected hub chain, and `0` are across.

and that note states what it does not supply, verbatim:

> - It supplies no update rule, no formation site, no formation rate, and no values. No coupling, no absolute unit, and no dynamical clause appears anywhere.

So `B_i` is a term type of the law with no coefficient attached to it. The question this note asks is what happens when it has one. The question it is asking about is the one PR #7879 names, whose Corollary item 3 reads, verbatim:

> 3. **The two landed results are consistent with each other and not with a single vacuum.** Which state is the framework's vacuum is a decision about the framework,
>    named here for its owner, not a residual to compute away. The exact consequences of each choice are supplied. **If the vacuum is empty**: the positive number
>    density `n_v` sources gravity and meets every clause; all flux sectors tie, so the kinetic clause's staggered field is a free choice; and there is no Dirac
>    structure. **If the vacuum is the half-filled sea**: the staggered sector is selected by the hopping energy; the spectrum has a gapless point at the reduced-zone
>    corner; matter comes in pairs; the energy density is the object that carries the monopole; and the number-density deviation carries a dipole and no monopole.

and the sentence from PR #7874 that this note sharpens reads, verbatim:

> So the question "which sector" is answered by "how much matter", and the filling is a supplied datum, not something this note derives.

The object declared here, and derived from nothing, is the **occupancy term**

```text
H = - t sum_<ij> eta_ij c_i^dag c_j  -  J_B sum_i B_i,      t = 1,
```

with `J_B >= 0` a single dimensionless coefficient. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the superfast encoding, the two uniform sign fields, the flux sectors, the occupancy term and the
functional `W(J_B)`. `P1` (`A`) is the commutation making the occupancy term a chemical potential; `P2` (`B`) the `J_B = 0` ground state; `P3` (`C`) the `J_B`-dependence, the crossover and the thresholds; `P4` (`D`) the extended certificate; `P5`
(`E`, `F`) the half-filling windows and the limit. `P3` uses `P1` to know that the term only shifts occupancies; `P4` uses nothing from `P3` but its numbers; `P5` uses `P2`'s bipartite lemma. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` at `2v + e_a`. The **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1
+ v_2}`; the **plain sign** is `+1` on every bond. The **encoding** is the Bravyi-Kitaev superfast encoding on the coarse lattice, code qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`, with

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_i  = product of the Z's on the edges incident to i,   T_ij = (i/2) A_ij (B_i - B_j),   S_f = the ordered product of the four A's around a coarse face f
```

A **flux sector** is a choice of eigenvalue `+-1` for every `S_f` consistent with the `F2` relations among them, realised as a link-sign field `eta` by spanning-tree gauge fixing followed by fundamental-cycle transport. The **hopping matrix** is
`M_ij = eta_ij` on nearest-neighbour coarse bonds and `0` elsewhere, `E_N` is the sum of its `N` lowest eigenvalues, and the **filling** is `n = N/V`. On a torus the three **Wilson lines** are gauge-invariant data that no `S_f` fixes; a **twist**
flips the signs on one cut plane and changes one Wilson line without changing any face. The **occupancy cost** functional, measured from the empty lattice, is

```text
W(J_B) = min_N [ E_N + 2 J_B N ] = sum over levels eps < -2 J_B of (eps + 2 J_B),
```

and `n(J_B) = N/V` at the minimising `N`. Every torus quantity below is minimised over the eight twists **at each `J_B` separately**.

## Theorem 1 -- the occupancy term is a pure chemical potential

**Conclusion.** On the open `2x2x2` and `3x3x3` coarse blocks and the coarse tori `3^3` and `4^3`:

1. Every `B_i` squares to the identity and any two of them commute, and `A_ij` anticommutes with exactly `B_i` and `B_j`: `0` wrong signs over all `16029` `(hop, site)` Pauli-string pairs.
2. Hence `[sum_k B_k, T_ij] = i (B_i + B_j) A_ij (B_i - B_j) = -i (B_i^2 - B_j^2) A_ij = 0` for every hop: `sum_i B_i` commutes with the whole hopping term.
3. A single `B_i` does not. On a dense `16`-dimensional block, `||[sum_k B_k, T_ij]|| = 0` and `||[B_i, T_ij]|| = 2` over every hop, with `T_ij` Hermitian.
4. `(V I - sum_i B_i)/2` is the record-number operator there, with integer spectrum in `[0, V]`. So `-J_B sum_i B_i = -J_B V + 2 J_B N`.

**Proof.** Items 1 and 2 are `F2`/`Z4` symplectic bit arithmetic at zero tolerance, the sign of a commutator of two Pauli strings read off the symplectic form. Item 3 builds the four-qubit block explicitly as complex matrices and takes the
commutators. Item 4 diagonalises `(V I - sum_i B_i)/2` on that block; its eigenvalues are integers, and `sum_i B_i` commuting with every hop makes them conserved.

**Reading, not theorem.** The extra term counts particles and does nothing else. It cannot move one, it cannot make one, and it cannot destroy one; adding it to the law changes no motion, only the price of standing still. One particle costs `2 J_B`,
and `N` of them cost `2 J_B N`. That is the whole content of the coefficient: a charge for occupancy.

## Theorem 2 -- at zero cost the ground state is the half-filled staggered sea

**Conclusion.** At `J_B = 0`:

1. Every cluster here is bipartite with all degrees `6`, so every link-sign field on it has a spectrum symmetric about `0` -- `max |eps + reverse eps| < 4e-14` over all `82` spectra -- and therefore `min_N E_N = E_{V/2}`, attained exactly on the tie
   range `[#neg, #neg + #zero]`. On the plain `4^3` field at the untwisted Wilson line there are `20` zero modes and the ties run over `N` in `[22, 42]`.
2. On the open `2x2x2` cube, exhaustively over all `32` consistent sectors and all `N`, the global minimum is `-4 sqrt3`, attained **only** by the all-`(-1)` sector at `N = 4`, by a margin of `0.456067` to the next distinct value.
3. On the `4^3` torus the global minimum over `8` twists times `2` uniform sectors, `5` structured sectors and `1000` random link-sign fields is `-32 sqrt6`, which is the Cauchy-Schwarz floor over **all** link-sign fields on that torus.
4. Elsewhere the same sector wins as a **search result**: `-258.857540` on `6^3` against a best random field of `-230.81`, `-611.811768` on `8^3`, and `-26.040600` against the plain sector's `-21.213203` on the open `3x3x3`.

**Proof.** Item 1 is `[numerical, 4e-14]` for the symmetry and exact in structure: a spectrum symmetric about `0` makes the partial sums of the sorted levels decrease exactly while the levels are negative and increase after, so the minimum sits at
the last negative level and ties across the zeros. Item 2 enumerates the `32` sectors from the `F2` relations among the `S_f`, realises each as a sign field, and compares the exact ladders. Item 3 evaluates the fields and compares against the bound
of Theorem 5 at `J = 0`. Item 4 is direct evaluation at the runner's fixed seed and is a statement about the fields drawn, not about the whole space.

**Reading, not theorem.** With nothing to pay for a particle, the lattice fills every level that costs less than nothing, and half the levels do, because the box is two-colourable and its levels come in plus-minus pairs. So the cheapest state is
exactly half full whatever the signs on the links, and among the sign patterns the cheapest is the one with a minus around every square. On the smallest box that is the cheapest arrangement there is; on the `4^3` box it is as cheap as anything could
be.

## Theorem 3 -- the ground state as a function of the cost

**Conclusion.** With `W(J_B)` twist-minimised at each `J_B`, on the `4^3` torus:

| `J_B` | `w` plain | `n` plain | twist | `w` stag | `n` stag | twist |
|---|---|---|---|---|---|---|
| `0` | `-1.060660` | `0.50000` | `111` | `-1.224745` | `0.50000` | `111` |
| `0.5` | `-0.593750` | `0.34375` | `000` | `-0.724745` | `0.50000` | `111` |
| `0.823267` | `-0.390788` | `0.31250` | `011` | `-0.401477` | `0.50000` | `111` |
| `sqrt3/2` | `-0.364064` | `0.31250` | `011` | `-0.364064` | `0.43750` | `000` |
| `sqrt6/2` | `-0.224144` | `0.12500` | `111` | `-0.134464` | `0.25000` | `000` |
| `sqrt3` | `-0.097317` | `0.12500` | `111` | `0` | `0` | `000` |
| `3` | `0` | `0` | `000` | `0` | `0` | `000` |

and in the thermodynamic limit, by Bloch quadrature at `L = 224`:

| `J_B` | `w` plain | `n` plain | `w` stag | `n` stag |
|---|---|---|---|---|
| `0` | `-1.0024184` | `0.500028` | `-1.1938011` | `0.500000` |
| `0.4` | `-0.6480922` | `0.385838` | `-0.7946948` | `0.495420` |
| `0.8654003` | `-0.3510864` | `0.252133` | `-0.3510874` | `0.441724` |
| `1.2` | `-0.2126531` | `0.167895` | `-0.1051182` | `0.267308` |
| `sqrt3` | `-0.0810372` | `0.085917` | `0` | `0` |
| `3` | `0` | `0` | `0` | `0` |

The optimal Wilson twist is not fixed: the staggered sector's minimising twist changes from `(1,1,1)` to `(0,0,0)` as `J_B` rises through the table, and the plain sector's takes three distinct values across it.

**Proof.** `[numerical, 1e-9]` throughout, with the occupancy set at each `J_B` read off the sorted spectrum and the eight twisted fields built explicitly. The Bloch formulas `2 sum_a cos q_a` and `+-sqrt(6 + 2 sum_a cos q_a)`, with a half-integer
momentum shift on each twisted axis, reproduce the real-space spectra at `L = 4, 6, 8` to `2.7e-14`.

**Reading, not theorem.** Raise the price and the sea drains. At no price the lattice is half full; at a middling price it is a third or a quarter full; past a certain price it is empty. Nothing else about the arrangement changes -- the same links,
the same signs, the same motion -- only how much of the lattice is in use.

## Theorem 4 -- the crossover and the emptying thresholds

**Conclusion.**

1. On the `4^3` torus the plain sector overtakes the staggered one at `J_B* = sqrt3/2` **exactly**: the staggered sector's KS twist has `W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J` and the plain sector's `(0,1,1)` twist has `W = -24 - 24 sqrt2 + 40 J`, both
   valid across `J = sqrt3/2`, with difference `16 J - 8 sqrt3`.
2. `J_B* = 0.849332` on `6^3`, `0.867676` on `8^3`, and `0.8654003 +- 3e-6` in the thermodynamic limit, where the fillings at the crossover are `0.4417` for the staggered sector and `0.2521` for the plain one.
3. A sector empties at `J_B >= |eps_min|/2`. That is `3` **exactly** for the plain sector -- band bottom `-6` at `q = (pi, pi, pi)` -- and `sqrt3` for the staggered one, on all three tori and in the limit; `3 sqrt2/2` and `sqrt6/2` on the open
   `3x3x3`; and `3/2` on the open `2x2x2` cube, where all `32` sectors tie at `W = 0` from there up.
4. On the cube the all-`(-1)` sector stops being the strict global minimiser at `sqrt3 - (1 + sqrt2)/2 = 0.524944`, where the two-flux class takes over.

**Proof.** Item 1 is exact: the `L = 4` spectra `0 x8, +-2 x12, +-2sqrt2 x12, +-2sqrt3 x4` and `0 x16, +-2 x8, +-2sqrt2 x8, +-(2 + 2sqrt2) x4, +-(2sqrt2 - 2) x4` are verified against the numeric ones to `1e-13`, the occupancy sets are constant across
`J = sqrt3/2`, and the difference is a `sympy` identity whose only root is `sqrt3/2`. Items 2 and 3 are `[numerical, 1e-9]` by bisection on the twist-minimised difference and by reading the band bottoms, with the surd values checked to `1e-9`. Item 4
bisects on the cube's exhaustive sector list.

**Reading, not theorem.** There is a price at which the two arrangements cost the same, and it is close to nine tenths of a hopping unit however large the box. Below it the minus-on-every-square arrangement is cheaper, above it the plain one is, and
the reason is simple: the staggered arrangement holds its levels in a narrow band and so gives them all up at once, while the plain one has a few very deep levels that survive a much higher price. The plain arrangement is the last to empty, and it
empties at three.

## Theorem 5 -- the extended certificate

**Conclusion.** On any bipartite cluster of `V` sites with every degree `6`, for **any** link-sign field:

1. `tr M^2 = 2|E| = 6V` and `D M D = -M` for the colour involution `D`, so the spectrum is symmetric about `0` and the squares of the negative levels sum to `3V`.
2. If `m` levels are occupied, Cauchy-Schwarz gives `sum_occ |eps| <= sqrt(3 V m)`, hence `W(J) >= min_{0 <= m <= V/2} [-sqrt(3 V m) + 2 J m]`, which equals `-V sqrt(3/2) + J V` for `J <= sqrt(3/8) = 0.612372` and `-3V/(8J)` above it.
3. On the `4^3` torus the staggered sector at its flat twist has `W = 64 J - 32 sqrt6` and **attains** that floor with slack at most `7e-15` at every `J_B <= sqrt(3/8)`. It is therefore a global minimiser over all link-sign fields **and** all record
   numbers on that whole interval, not only at `J_B = 0`.
4. All `1021` fields evaluated -- `16` twisted uniform, `5` structured, `1000` random -- respect the floor at `16` values of `J_B`: `0` violations.

**Proof.** Item 1 is a zero-tolerance integer matrix identity. Item 2 minimises a one-dimensional function of `m` with the interior stationary point `m = 3V/(16 J^2)`, which lies inside `[0, V/2]` exactly when `J >= sqrt(3/8)`. Item 3 is exact: the
flat-twist spectrum is `+-sqrt6` with multiplicity `32` each, so every occupied level has the same size, which is the equality case, and the occupancy stays at `32` for all `J < sqrt6/2`. Item 4 is `[numerical, 1e-9]` verification of the bound, not a
proof of it.

**Reading, not theorem.** Two facts about the box -- six neighbours per site and two colours -- fix a floor that no arrangement of signs and no number of particles can go below, at any price. On the `4^3` box, and for every price up to about `0.61`,
the half-filled minus-on-every-square sea sits exactly on that floor. It is not merely the best thing tried; nothing could be better.

## Theorem 6 -- how long exactly half filling survives

**Conclusion.**

1. Exactly half filling survives on the `4^3` torus for `J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = 0.823267` when the twist is chosen freely at each `J_B`, and for `J_B < sqrt6/2 = 1.224745` within the half-filling twist itself.
2. On `6^3` the twist-minimised window is `J_B < 2 sqrt3 - 3 = 0.464102`, and on `8^3` it is `J_B < 0.306846`. The window shrinks with the box.
3. In the thermodynamic limit it closes. The staggered band `-sqrt(6 + 2 sum_a cos q_a)` vanishes at `q = (pi, pi, pi)` and only there, and near that point `6 + 2 sum_a cos q_a = |k|^2 + O(|k|^4)`, so for every `J_B > 0` the emptied region `|k| < 2
   J_B` has positive measure: exactly half filling survives only at `J_B = 0`, with `1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3`. The measured ratio of `1/2 - n(J_B)` to that cubic is `0.9663, 1.0215, 1.0258` at `J_B = 0.15, 0.2, 0.3`.

**Proof.** Items 1 and 2 bisect on the twist-minimised occupancy and check the surds to `1e-8`. Item 3's series expansion is exact in `sympy`; the ratios are `[numerical]` on the `L = 224` Bloch grid. At `J_B = 0.001` that grid cannot resolve the
effect: the emptied ball has radius `0.002` against a grid spacing of `2 pi / 112`, so the grid reports `n = 0.4999996`, which is its own `n(0)`. The statement that the sea is doped at every positive `J_B` is the analytic one, not a grid reading.

**Reading, not theorem.** In a finite box exactly half filling is stable: it takes a real price to empty the topmost level, because the topmost level is a real distance below zero. In an unbounded lattice there is no such distance -- the band touches
zero -- so any price at all, however small, empties a little of the sea. The window in which the lattice is exactly half full closes as the box grows.

## Corollary -- the vacuum question is the value of one coefficient

Within the setting declared above, and on the finite blocks and tori named:

1. The law's `B_i` term type, given the coefficient the law leaves blank, is a **pure chemical potential**: `-J_B sum_i B_i = -J_B V + 2 J_B N`, a price of `2 J_B` per fermion and nothing else. It adds no motion, no interaction and no scale beyond
   the ratio `J_B/t`.
2. At `J_B = 0` the law's own ground state, over all record numbers and all flux sectors, is the **half-filled staggered sea** -- provably on the cube, provably against all link-sign fields on the `4^3` torus, and as a search result elsewhere.
3. At `J_B/t >= 3` the ground state is the **empty lattice**, on every cluster here and in the limit. The plain sector is the last to empty and it empties exactly at `3`.
4. Between the two the ground state is a partially filled sea whose filling falls continuously with `J_B`, and which changes flux sector at `J_B* ~ 0.865`: `sqrt3/2` exactly on `4^3`, `0.8654003` in the limit.
5. So the two branches PR #7879 names are the two ends of one interval, and the framework's vacuum question is the value of a single dimensionless coefficient `J_B/t` that the law as written does not fix. What PR #7874 calls a supplied datum
   sharpens: **`J_B/t` is the supplied datum, and the filling follows from it.** The owner's decision is therefore the size of the occupancy cost; nothing here chooses it and nothing here narrows it.

**Reading, not theorem.** Ask how much it costs to have a particle at a site. If the answer is nothing, the lattice fills itself halfway with a sea of matter and the minus-sign pattern comes with it. If the answer is more than three hopping units,
the lattice stays empty. In between it fills part way. The law as written does not say what the cost is; that one number is the vacuum question.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. No status value is set, predicted, or implied, and no premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding, the sign fields, the occupancy term and its coefficient are declared objects, and the theorems are about them.
- No vacuum is chosen and no value of `J_B/t` is preferred, proposed, estimated or bounded by anything physical. Both ends of the interval are supplied and neither is adopted.
- No mass, no absolute unit, no interaction, no temperature, no formation rate and no dynamical clause appears anywhere. `t = 1` is a choice of unit for the ratio `J_B/t`, not a value.

## Interfaces named for other lanes, not moved here

- **The value of `J_B/t`.** This is a science question, not a residual: which known physics the coarse lattice must reproduce is what would fix it. A lane owning the framework's ground state should decide it; Corollary items 2 to 4 hand that lane the
  full consequence map, and nothing here narrows the choice.
- **Interactions.** Only free hopping plus a diagonal occupancy term is compared. A four-fermion term, or any interaction, could move the crossover and the thresholds, and no such term is examined.
- **The gapless limit.** Theorem 6 item 3 is an infinite-volume subtlety and is named as one: in a finite box exactly half filling has a window, and in the limit the window is the single point `J_B = 0`. A lane wanting a half-filled sea at positive
  cost in infinite volume owns that tension.
- **Global minimality beyond `4^3` and the cube.** Theorem 5 is a theorem on the `4^3` torus for `J_B <= sqrt(3/8)` and Theorem 2 item 2 an exhaustion on the cube. Everywhere else the corresponding statement is a search result at the runner's fixed
  seeds.
- **The Wilson-line convention.** Every torus quantity is minimised over the eight twists at each `J_B`; which twist a physical setting selects is not decided here.
- **The many-body energetics.** Only the one-particle ladder is used, the ground state of the free problem at fixed `J_B`.

## Remaining live routes

1. The interval's interior. The crossover and the thresholds are computed; what a partially filled sea implies for the results conditioned on either vacuum is not.
2. Larger blocks and other geometries. Three tori, two open blocks and the Bloch limit are what is here.
3. Finite temperature. Everything is a ground-state energy at fixed coefficient, and every sector ties at `W = 0` once the lattice is empty.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one mode per coarse vertex, BK superfast encoding, free nearest-neighbour hopping t = 1 plus the declared occupancy term -J_B sum_i B_i; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
chemical_potential: [sum_k B_k, T_ij] = -i (B_i^2 - B_j^2) A_ij = 0 exactly; 0 wrong signs over 16029 (hop, site) Pauli pairs on open 2x2x2, open 3x3x3, torus 3^3, torus 4^3; dense 16-dim block ||[sum B, T]|| = 0 vs ||[B_i, T]|| = 2; (V I - sum B)/2 = N integer; -J_B sum_i B_i = -J_B V + 2 J_B N
bipartite: every cluster bipartite degree 6; spectra symmetric to 3.4e-14; min_N E_N = E_{V/2} with ties [#neg, #neg + #zero]; plain 4^3 untwisted 20 zero modes, ties N in [22, 42]
j0_cube: all 32 sectors x all N -> -4 sqrt3, unique at all-(-1), N = 4, margin 0.456067
j0_tori: 4^3 -32 sqrt6 = the Cauchy-Schwarz floor over ALL link-sign fields (16 twisted uniform + 5 structured + 1000 random); 6^3 -258.857540 (16 + 300 random, best random -230.81); 8^3 -611.811768; open 3x3x3 -26.040600 vs plain -21.213203
crossover: J_B* = sqrt3/2 exactly on 4^3 (stag KS W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J, plain (0,1,1) W = -24 - 24 sqrt2 + 40 J, difference 16 J - 8 sqrt3); 0.849332 on 6^3; 0.867676 on 8^3; 0.8654003 +- 3e-6 in the limit, fillings 0.4417 and 0.2521
thresholds: plain empties at J_B = 3 exactly (bottom -6 at (pi,pi,pi)), staggered at sqrt3, on 4^3, 6^3, 8^3 and in the limit; open 3x3x3 3 sqrt2/2 and sqrt6/2; cube 3/2 with all 32 tying at W = 0; cube all-(-1) loses to the 2-flux class at sqrt3 - (1 + sqrt2)/2 = 0.524944
certificate: any bipartite degree-6 field has tr M^2 = 6V and D M D = -M, so W(J) >= -V sqrt(3/2) + J V for J <= sqrt(3/8) = 0.612372 and -3V/(8J) above; the 4^3 flat-twist staggered sea has W = 64 J - 32 sqrt6 and attains it with slack <= 7e-15 at every J_B <= sqrt(3/8); 0 violations over 1021 fields at 16 values of J_B
half_filling_windows: 4^3 J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = 0.823267 twist-minimised and sqrt6/2 within the half-filling twist; 6^3 2 sqrt3 - 3 = 0.464102; 8^3 0.306846; limit only J_B = 0, gapless at (pi,pi,pi), 1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3, ratios 0.9663, 1.0215, 1.0258 at J_B = 0.15, 0.2, 0.3
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=24 FAIL=0
```

## Proof boundary

The content is **free nearest-neighbour hopping plus one declared diagonal term**, on **finite** clusters and a converged Bloch grid. The occupancy term `-J_B sum_i B_i` and its coefficient are **declared by this note**; no axiom supplies them, no
axiom forbids them, and nothing here derives either. `t = 1` fixes the unit in which `J_B` is read and is not a physical value.

Global minimality over all link-sign fields is a **theorem on exactly two clusters**: the open `2x2x2` cube, by exhaustion of its `32` sectors at every `N`, and the `4^3` coarse torus, by the extended Cauchy-Schwarz certificate, and there only for
`J_B <= sqrt(3/8)`. On `6^3`, on `8^3` and on `4^3` above `sqrt(3/8)` the corresponding statement is a **search result** -- a statement about the fields drawn at the runner's fixed seed, not about the whole space.

The crossover value is exact only on the `4^3` torus. `0.849332`, `0.867676` and `0.8654003` are numerical, the last from Bloch quadrature whose `L` sequence `128, 160, 192, 224` settles within `3e-6`. Nothing here claims a limit theorem; the limit
numbers are converged quadrature.

Theorem 6 item 3 is the one place a finite-cluster reading and an infinite-volume reading differ, and the difference is stated rather than smoothed: on every finite cluster exactly half filling survives a positive window of `J_B`, and in the limit it
survives only at `J_B = 0`. At `J_B = 0.001` the `L = 224` grid cannot see the doping at all, and the runner says so rather than reporting the grid's own `n(0)` as a physical value.

No claim is made that any value of `J_B/t` is right, likely, natural or excluded. The interval `[0, 3]` and its interior structure are what is computed; which point of it the framework means is not a residual this note leaves open by accident, but a
decision it hands over on purpose.

## Review record

An honest auditor should come away with: one exact commutation theorem showing that the law's uncoefficiented `B_i` term, given any coefficient, is a chemical potential and nothing more; one exhaustive statement that at zero coefficient the law's own
ground state is the half-filled staggered sea, with a genuine certificate making that a global statement over all link-sign fields on the `4^3` torus and, extended, over all fillings too for every `J_B` up to `sqrt(3/8)`; one exact crossover at
`sqrt3/2` on that torus with its thermodynamic value `0.8654003`; the exact emptying threshold `3`; a clearly labelled band of search results away from the two certified clusters; and the honest limit that the half-filling window closes as the box
grows because the staggered band is gapless.

The three things most likely to be over-read are flagged in the proof boundary: the occupancy term is declared and not derived, so nothing here says the framework *has* such a term; global minimality is a theorem on two clusters and, on `4^3`, only
below `sqrt(3/8)`; and the gapless limit means the *exactly* half-filled sea is not the ground state at any positive cost in infinite volume. This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no
hypothesis is adopted, and the four context notes in "Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=24 FAIL=0`, runtime under the declared
`120` seconds, stdout under `5500` characters, and passing pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
````

## original-cutoff live — logs/runner-cache/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.txt

SHA-256 `86b52092cb44d1e8cf0b966f1fd18dd2ba37e708a5cdc26d6a0ef45c8565f51a`. Verbatim body follows.

````text
===== runner cache v1 =====
runner: scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py
runner_sha256: e7555a77393e22ce41e8dfa119befd0db6c3603dd950fc6c33b8abc8de31335d
timeout_sec: 120
exit_code: 0
elapsed_sec: 4.52
status: ok
----- stdout -----
==============================================================
A  THE OCCUPANCY TERM IS A PURE CHEMICAL POTENTIAL [exact]
==============================================================
  clusters: open 2x2x2, open 3x3x3, torus 3^3, torus 4^3
PASS A1 B_i^2 = I and all B_i mutually commute on all four clusters
PASS A2 A_ij anticommutes with exactly B_i, B_j: 0 wrong of 16029 (hop, site) pairs
PASS A3 [sum_k B_k, T_ij] = -i (B_i^2 - B_j^2) A_ij = 0: 0 failures
  dense 16-dim block: ||[sum B, T]|| = 0.00e+00, ||[B_i, T]|| = 2.00e+00
PASS A4 sum_i B_i commutes with every hop; a single B_i does not (norm 2)
PASS A5 (V I - sum_i B_i)/2 = N, integer spectrum in [0, V]: 0,2,4
  so -J_B sum_i B_i = -J_B V + 2 J_B N: 2 J_B per fermion, nothing else

==============================================================
B  AT J_B = 0: THE HALF-FILLED STAGGERED SEA
==============================================================
PASS B1 [numerical, 4e-14] spectra symmetric about 0: max |eps + rev| = 3.4e-14
PASS B2 min_N E_N = E_{V/2}, ties [#neg, #neg+#zero]; plain 4^3 20 zero modes, ties N in [22, 42]
PASS B3 cube exhaustive: 32 sectors; min over (sector, N) at J_B = 0 is -6.928203 = -4 sqrt3, unique all-(-1) at N = 4, margin 0.456067
  4^3, 16 twisted uniform + 5 structured + 1000 random: -78.383671769 = -32 sqrt6
  6^3, 16 + 300 random (best random -230.81): -258.857540 ; 8^3: -611.811768
PASS B4 4^3 minimum at J_B = 0 is -32 sqrt6, the Cauchy-Schwarz floor over ALL link-sign fields
PASS B5 [search] 6^3 -258.857540, 8^3 -611.811768, open 3x3x3 -26.040600 stag vs -21.213203 plain

==============================================================
C  THE GROUND STATE AS A FUNCTION OF J_B (twist-minimised)
==============================================================
  4^3 (V=64), w = W/V per site, n = N/V:
      J_B  |  w plain    n plain  twist |   w stag     n stag  twist | lower
  0.000000 | -1.060660  0.50000  111 | -1.224745  0.50000  111 | stag
  0.500000 | -0.593750  0.34375  000 | -0.724745  0.50000  111 | stag
  0.823267 | -0.390788  0.31250  011 | -0.401477  0.50000  111 | stag
  0.866025 | -0.364064  0.31250  011 | -0.364064  0.43750  000 | tie
  1.224745 | -0.224144  0.12500  111 | -0.134464  0.25000  000 | plain
  1.732051 | -0.097317  0.12500  111 |  0.000000  0.00000  000 | plain
  3.000000 |  0.000000  0.00000  000 |  0.000000  0.00000  000 | tie
PASS C1 [numerical, 1e-9] the optimal twist changes with J_B: 2 distinct staggered twists in the 4^3 table
PASS C2 [exact] 4^3: stag KS W = -24 - 24 sqrt2 - 8 sqrt3 + 56 J vs plain (0,1,1) -24 - 24 sqrt2 + 40 J; difference 16*J - 8*sqrt(3)
PASS C3 [numerical, 1e-9] J_B* = sqrt3/2 = 0.866025404 (4^3), 0.849332 (6^3), 0.867676 (8^3)
  emptying thresholds J_B >= |eps_min|/2: plain 3, staggered sqrt3, all tori;
  open 3x3x3 2.121320 = 3 sqrt2/2 and 1.224745 = sqrt6/2; cube 1.5000, all 32 tie at W = 0
PASS C4 [exact where surds] plain empties at J_B = 3, staggered at sqrt3, all tori
PASS C5 [exact] on the cube all-(-1) loses to the 2-flux class at sqrt3 - (1 + sqrt2)/2 = 0.524944

==============================================================
D  THE EXTENDED CERTIFICATE ON 4^3, J_B <= sqrt(3/8) [exact]
==============================================================
  tr M^2 = 6V, D M D = -M for any field, so sum_occ eps^2 <= 3V and W(J) >=
  min_m [-sqrt(3 V m) + 2 J m] = -V sqrt(3/2) + J V for J <= sqrt(3/8) = 0.612372,
  and -3V/(8J) above it
PASS D1 [exact] bipartite degree-6 premises: tr M^2 = 384 and D M D = -M
PASS D2 [exact] the 4^3 flat-twist staggered sea has W = 64*J - 32*sqrt(6) and attains the floor at every J_B <= sqrt(3/8): slack <= 0.0e+00
PASS D3 [numerical, 1e-9] the floor holds for all 1021 fields at 16 values of J_B: 0 violations

==============================================================
E  HOW LONG EXACTLY HALF FILLING SURVIVES
==============================================================
PASS E1 [exact] 4^3 half filled for J_B < 4 sqrt6 - 3 - 3 sqrt2 - sqrt3 = 0.823267, and < sqrt6/2 = 1.224745 within its own twist
PASS E2 [numerical, 1e-8] 6^3 half filled for J_B < 2 sqrt3 - 3 = 0.464102, 8^3 for J_B < 0.306846

==============================================================
F  THE THERMODYNAMIC LIMIT [Bloch quadrature, L = 224]
==============================================================
PASS F1 [numerical, 1e-9] Bloch 2 sum cos q_a and +-sqrt(6 + 2 sum cos q_a) match real space at L = 4, 6, 8 to 2.7e-14
      J_B  |   w plain     n plain |    w stag      n stag | lower
  0.000000 | -1.0024184  0.500028 | -1.1938011  0.500000 | stag
  0.400000 | -0.6480922  0.385838 | -0.7946948  0.495420 | stag
  0.865400 | -0.3510864  0.252133 | -0.3510874  0.441724 | stag
  1.200000 | -0.2126531  0.167895 | -0.1051182  0.267308 | plain
  1.732051 | -0.0810372  0.085917 |  0.0000000  0.000000 | plain
  3.000000 |  0.0000000  0.000000 |  0.0000000  0.000000 | tie
PASS F2 [numerical] J_B* = 0.8654029 +- 3e-6 in the limit, fillings 0.4417 staggered and 0.2521 plain there
  (1/2 - n(J)) / ((2/(3 pi^2)) J^3) at J = 0.15, 0.2, 0.3: 0.9663, 1.0215, 1.0258
  at J = 0.001 the emptied ball |k| < 2J is finer than the grid: n = 0.4999996
PASS F3 [exact + numerical] gapless at (pi, pi, pi), so any J_B > 0 dopes the sea: 1/2 - n(J_B) -> (2/(3 pi^2)) J_B^3
PASS F4 [exact] in the limit plain empties at J_B = 3 (bottom -6), staggered at sqrt3 (bottom -2 sqrt3)

runtime 4.2 s (budget 120 s)
TOTAL: PASS=24 FAIL=0

----- stderr -----

````

## first #7881 revision — docs/ENERGY_PRODUCT_AND_TEST_BODY_LAW_ABOVE_THE_HALF_FILLED_SEA_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md

SHA-256 `6d9bea6e484ca27559f2d8b64b42e5759b77c2e6a8df2bff4704d69083253635`. Verbatim body follows.

````text
---
claim_id: energy_product_test_body_law_half_filled_sea
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on three separately supplied things and on nothing else -- the designed fermion law of EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md, which that note declares a supplier model derived from no axiom; the landed weak-field response surface phi = G0 P0 rho of docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md; and the choice of the half-filled staggered sea as the vacuum, which MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md names as a decision about the framework and does not make -- on the named finite tori and nowhere else: (T1) two localised particle-hole pairs above the 8^3 half-filled staggered sea at its energy-minimising twist (E_sea = -611.811768, gap 2.651309, <n_v> = 1/2 to 8e-16) form a determinant state P'' = P - Q_h + Q_p that is a projector to 2e-15 with trace exactly 256 = V/2 at every centroid separation D = (2,0,0), (3,0,0), (4,0,0), (3,3,0) and both internal separations d_pair = 1, 2; the orbital overlaps fall <p1|p2> = 0.37, 0.15, 0.044, 0.014 and <h1|h2> = 0.38, 0.021, 0.0013, 0.0036; the energy is additive at relative defect -2.1e-02, -2.3e-03, -2.7e-04, -5.8e-05 and the additivity defect of the local energy density eps_v falls an order of magnitude per unit of D, 2.1e-01, 2.4e-02, 2.7e-03; and sum_v rho = 0 to 1e-14 for every single-pair and every joint state, so the count above this sea is identically zero. (T2) With the landed response validated first against the point control 4 pi r G at r = Lb/4 = 0.3307, 0.3275 at Lb = 32, 64, the interaction energy E_int = <eps_1, G0 P0 eps_2> equals the product form E_1 E_2 G0P0(D) at ratio 0.8517, 0.9043, 0.9650, 0.9540 at those four D on Lb = 64 with d_pair = 1, 0.8757 and 0.9188 at D = 3, 4 with d_pair = 2, and 0.9575 and 0.8997 on Lb = 32; E_int is exactly the cross term of the quadratic form, <eps_12, G eps_12> minus the two self terms equalling 2 E_int to 1e-15 over all sixteen rows; the leading multipole correction from each source's dipole and traceless quadrupole moves the point form to 0.9380, 0.9146, 0.9773, 0.9576, accounting for the deficit to 1-3 per cent at |D| >= 3; and on two RIGID copies of one eps profile in the Lb = 64 box, a statement about the kernel and the source shape and not about a joint 8^3 state, the ratio is 0.9462, 0.9736, 0.9938, 0.9986 at D = 3, 4, 8, 16. (T3) The force F = -grad_{x2} E_int, by central differences on pair 2's centroid under rigid translation in the response box, equals F_pred = -E_2 grad phi_1(x_2) with phi_1 = G0 P0 eps_1 at x-component ratio 0.8271 and 0.9719 at D = 3, 4 for d_pair = 1 and 0.8568 and 0.9209 for d_pair = 2, with angle residuals 5.7, 6.5, 1.9 and 0.1 degrees; rebuilding a pair one coarse site over from a fresh seed is faithful only when the seed is carried by the KS field's gauge sign, translation residual 3.96e-01 naive against 2.10e-03 gauge-corrected, a named gauge artefact of the sign field; and on rigid copies the x ratio is 0.8981, 0.9854, 0.9982, 0.9992, 0.9997, 1.0000 at D = 3, 4, 6, 8, 10, 16 with the angle falling 7.3 to 1.8 degrees and the inverse-square coefficient 4 pi D^2 F_x / (E_1 E_2) reading 0.9711, 1.0398, 1.0216, 1.0060, 0.9924, 0.9260 against the source note's own point-kernel control 1.0194, 1.0064, 1.0009, 0.9963 at d = 4, 6, 8, 10. (T4) The pooled object differs by vacuum: an energy knob at fixed D = 4, band-filtering one Gaussian seed toward +-E0 at width 0.6, carries E_exc through 3.8766, 4.5998, 5.3655, 5.8591, 6.0461 and lifts E_int by 2.525 while E_1 E_2 lifts by 2.425, a ratio of ratios of 1.041; the same bilinear form on the EMPTY vacuum's A-string count source, I = 2 per pair, reads E_int^count = 0.0655525 in every one of those rows at spread 0e+00, literally constant; and above the half-filled sea the count product is identically 0 by T1. The source note's T6 sentence, that the object the pooled response carries is the count product I(S) I(T) and NOT a mass product, stands unchanged on the empty vacuum it was proved on. UNITS ARE STATED, NOT DERIVED: the hop is t = 1 so m = E_exc/t is a dimensionless lattice number, G0 P0 carries a^-1, and no G_Newton, no coupling, no M_phys and no absolute unit appears; the source note's declared factor-two coarse/fine unit carry applies unchanged and is not adjudicated. This note chooses no vacuum, repairs neither of the two bridge clauses eps_v fails, stays strictly at the supplied linear response, and derives nothing from any axiom. No axiom is amended, no status is set, and no registry entry is created."
upstream_dependencies: []
runner: scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py
---

# The energy product and the test-body law above the half-filled sea

**Date:** 2026-09-03
**Type:** bounded_theorem, explicitly conditional on two supplied surfaces and one supplied vacuum choice
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:** [`scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py`](../scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py)
**Runner cache:** [`logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt`](../logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt)
**Parents:** none in the dependency sense. The two conditioning surfaces and the one conditioning choice are quoted in "Setting" as conditions, not consumed as graded rows.

The Newton lane carries two residuals that no landed note supplies: an identification of what plays the part of a mass, and a law saying how a second body responds to the field of the first. A landed note on the empty vacuum found that the object its pooled response
carries is a product of two counts, and said in terms that the identification of a count with a mass is a separate premise. A second landed note put matter above the half-filled staggered sea instead, found that the count of matter there is identically zero and the
excitation energy carries the landed monopole form, and named the choice between the two vacua as a decision about the framework that it did not make. This note takes that second vacuum as given and asks what the same bilinear response carries above it. The answer is
the product of the two excitation energies, with the same kernel; and the pull on a second lump is that lump's energy times the slope of the first lump's field. Both are candidates handed to the Newton lane by a vacuum choice, not by an axiom.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite-dimensional numerical computations on named finite tori, every one conditional on two named supplied surfaces and one named supplied vacuum choice and on nothing else. Group B4's cross-term identity and the structural statements of group A are exact identities of the quadratic form and of the one-body projector at machine tolerance; every other group is a finite floating-point computation reporting its residual against a tolerance declared before the run, and the response implementation is validated against both parents' own published point-source control before any new number is reported. Group E is a statement about units and derives nothing."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "The physical Newton residual is instead the source/test typing, mass-readout identification, and test-body response law. Current Record supplies none of the finite-additive scalar premise."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Route the undecided vacuum question, already named for its owner by the matter-above-the-sea note, together with what this note adds to each branch: on the half-filled sea the mass-readout identification has the candidate m = E_exc in units of t and the test-body response law the candidate form F = -E_test grad phi, both within the supplied linear response; on the empty vacuum the count product stands unchanged. The choice, and the two bridge clauses eps_v still fails, remain open."
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the four statements below plus one stated unit paragraph, exactly the runner's check groups `A`-`E`: `T1` (`A`) the two-pair state and additivity; `T2` (`B`) the energy product; `T3` (`C`) the test-body law; `T4` (`D`) count versus energy;
and `E` the units. Each is established on named finite tori and carries its own tag: `[exact]` where the statement is an identity of the quadratic form or of the projector, `[numerical]` with a stated tolerance where it is floating point, and `[stated]` where it
records a convention rather than a computation.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the discrete Fourier inverse of the graph Laplacian, the multipole expansion of a Coulomb kernel, and central finite differencing are standard
methodology; every object is redeclared here and the runner recomputes every statement, including a validation of its own Green-function implementation against both parents' published point-source control before any new number is reported. The two surfaces and the one
vacuum choice this note is conditional on are declared, quoted and named in "Setting"; they are conditions of the result, not graded dependencies, and this note cites none of their grades and consumes no row. Non-load-bearing context pointers, plain file names with no
grade and no dependency weight: `MINIMAL_AXIOMS_2026-06-29.md` (the four axioms quoted below); `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`, the authority for the `1 / (4 pi |r|)` asymptotic;
`POISSON_FINITE_VOLUME_WINDOW_AND_BIHARMONIC_OFFSET_BOUNDED_THEOREM_NOTE_2026-07-27.md`, whose finite-volume window explains the roll-off of the inverse-square coefficient at large `D`; and `NEWTON_LAW_DERIVED_NOTE.md` together with
`RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md`, whose two residuals this note addresses conditionally and whose Non-Claims bound this whole exercise as they bound the parent lane.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local
possibilities," whose "full one-site possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." **Record**: "Records form. When
present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent. Only records are readable. A readout value is determined by record content alone."

The record ontology is what makes the objects below densities at all. Neither `n_v` nor the energy density `eps_v` is a new primitive and neither is a site: each is a **readout of six records**. The six fine edge sites `2v +- e_a` around the coarse corner `2v` each
carry a record; `B_v` is the product of their six `Z` values, so `n_v = (1 - B_v)/2` returns `1` exactly when those six records register odd parity and `0` when they register even. Nothing is read that is not a record, and the value is determined by record content
alone, as Record requires.

**Condition one -- the fermion law.** From `origin/physics-loop/emergent-3d-fermion-superlattice-existence:docs/EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md`, verbatim: "The **encoding** is the
Bravyi-Kitaev superfast encoding written on the coarse sublattice, with the code qubits exactly the coarse edge sites. The direction order at every coarse vertex is `-x < -y < -z < +x < +y < +z`." and "`B_i = -1` marks the excitation; the **hop** across the coarse edge
`(i, j)` is `T_ij = (i/2) A_ij (B_i - B_j)`." Its Proof boundary, verbatim and outranking every summary: "The law of Theorems 1 to 3 is a **designed supplier model**: Admissibility fixes that there is one covariant nearest-neighbour rule and leaves its form to the
supplier, and this note supplies one form and computes its consequences, deriving that form from no axiom and claiming for it no privileged status." Everything below inherits that conditional.

**Condition two -- the landed response.** From `docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`, verbatim: the quadratic source action `A[phi; rho] = (1/2) <phi, H phi> - <P0 rho, phi>` "has the unique stationary solution, modulo the
constant zero mode, `phi = G0 P0 rho`." And, verbatim, the scope of that solve: "On finite periodic volumes the Poisson solve uses `P0 rho_psi`, i.e. the zero-mode-subtracted density. The zero mode is the total-mass/background sector and is not part of the local force
law." That surface is used exactly as landed, at linear order and nowhere beyond it.

**Condition three -- the vacuum, quoted as the choice it names and does not decide.** From `origin/physics-loop/matter-above-the-half-filled-sea:docs/MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md`,
verbatim: "**The two landed results are consistent with each other and not with a single vacuum.** Which state is the framework's vacuum is a decision about the framework, named here for its owner, not a residual to compute away." And, verbatim, the branch this note
takes as its condition: "**If the vacuum is the half-filled sea**: the staggered sector is selected by the hopping energy; the spectrum has a gapless point at the reduced-zone corner; matter comes in pairs; the energy density is the object that carries the monopole;
and the number-density deviation carries a dipole and no monopole." That branch is assumed here. It is not chosen here, and nothing below argues for it.

**The Newton lane's two residuals, quoted verbatim from the landed notes.** From `docs/NEWTON_LAW_DERIVED_NOTE.md` on `origin/main`, verbatim: the conditional audit "found that the test-mass force/source coupling" `F = -M_test grad(phi)` "was neither retained nor
registered as an approved admission", so that what the row proves is "an inverse-square gradient of a supplied `1/r` scalar kernel. It is not yet a physical Newton force law." Its Non-Claims list, verbatim, includes "the test-mass force/source response rule `F = -M_test
grad(phi)`" and "the physical product law `M_source M_test`". From `docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md` on `origin/main`, verbatim: "The physical Newton residual is instead the source/test typing, mass-readout
identification, and test-body response law", and its `next_trace_action`, verbatim: "Derive source/test typing, mass-readout identification, and the test-body response law; do not seek the scalar product in a pooled union value." Its own residual table records, verbatim,
that a route which would "Compose source and test-response linearities", where "A derived response `F=-m_t grad(phi)` yields the product without pooled recovery", is "the live Newton route, not ruled out", and its wall list, verbatim, is "`W1`: a scalar mass/readout
functional, including its finite-additive form if that form is intended; `W2`: physical source/test typing with separate accessibility; `W3`: the test-body response law", with every pair of those three independent.

**The empty-vacuum statement this note contrasts with.** From `origin/physics-loop/fermion-number-density-weak-field-source:docs/EMERGENT_FERMION_NUMBER_DENSITY_AS_WEAK_FIELD_SOURCE_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-02.md`, Theorem 6, verbatim: "So the object this
route delivers is `I(S) I(T)`, the product of two **counts**. It is emphatically **not** `M_source M_test`: no mass appears anywhere in this note, and the identification of a count with a mass is a separate premise this note neither supplies nor assumes." That
statement is about the empty vacuum, and this note leaves it exactly where it stands. Its `T4` point-kernel control, `4 pi d G_inf(d) = 1.0194, 1.0064, 1.0009` and `0.9963` at `d = 4, 6, 8, 10`, is quoted here **before** the run and used as the like-for-like comparison
for Theorem 3 item 4; the run fits nothing.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the strongest supported scope is precisely `P0`-`P5`. `P0`, declared here and conditional: the two supplied surfaces, the supplied vacuum choice, the coarse lattice,
the KS sign field, the twist, and the response operator. `P1` (`A`): the sea recomputed, and two pairs above it. `P2` (`B`): the energy product, validated against the landed point control first. `P3` (`C`): the test-body law, which uses `P1` for its states and `P2` for
its kernel. `P4` (`D`): count versus energy, which uses `P1` item 6 and `P2`. `P5` (`E`): the units, which derive nothing and depend on nothing.

## Definitions

Every object here is the parent's, unchanged. The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`. The **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`; a **twist** on axis
`a` flips the bonds crossing the cut `v_a = L-1 -> 0`. `M` is the symmetric integer hopping matrix on the coarse torus `L^3`, `P` the orthogonal projector onto its `V/2` lowest eigenvectors -- the **half-filled sea** -- and `E_sea` the sum of those levels. A **single
pair** is `P' = P - |h><h| + |p><p|` with `p` a normalised Gaussian seed projected into the empty span and `h` one projected into the occupied span, and a **two-pair state** is

```text
P'' = P - Q_h + Q_p          Q_h, Q_p the orthogonal projectors onto span{h1, h2} and span{p1, p2}
eps_v = sum_{j ~ v} M_vj (P'' - P)_vj        sum_v eps_v = tr(M (P'' - P)) = E_exc
rho_v = <n_v> - 1/2 = P''_vv - 1/2 = -<B_v>/2
```

The **internal separation** `d_pair` is the offset of a pair's hole from its particle, along `z`; the **centroid separation** `D` is the offset between the two pairs. The **response** is the landed one: `H = -Delta_lat` with the seven-point stencil, `G0 = H^{-1}` off
the constant mode, `P0` the projection off that mode, `phi = G0 P0 rho`. Each `eps_i` is unwrapped about its own pair midpoint, recentred on its rounded charge centroid -- the same integer shift for both copies, so their centroid separation is exactly `D` -- and
zero-padded into a response box `Lb^3`. The **interaction energy** is `E_int = <eps_1, G0 P0 eps_2>` and the **product form** is `E_1 E_2 G0P0(D)`, with `G0P0(D)` the same box's point-source kernel at the same offset. A **rigid copy** is one `eps` profile placed twice
in the response box at separation `D`; it is a statement about the kernel and the source shape, and not a joint state on the `8^3` torus.

## Theorem 1 -- two pairs above the sea, and what is additive

**Conclusion.** On the `8^3` coarse torus at its energy-minimising twist `(1,1,1)`:

1. The vacuum is the parent's: `E_sea = -611.811768` to `3.5e-07` of that note's own quoted value, gap `2.651309 = 2 sqrt(6 - 3 sqrt2)` to `5.3e-15`, and `<n_v> = 1/2` at all `512` sites to `7.8e-16`. The single pairs are the parent's too: the band-edge orbital pair at
   `E_exc = 2.651309`, the localised wavepackets from `4.3614` to `4.5163` over `d = 1, 2, 3, 4`, and `sum_v eps_v = E_exc` at residual `0`.
2. Two such pairs at centroid separations `D = (2,0,0), (3,0,0), (4,0,0), (3,3,0)` and internal separations `d_pair = 1, 2` give a determinant state `P''` that is a projector, `max|P''^2 - P''| = 2e-15` over all eight states, with trace exactly `256 = V/2`.
3. The pairs decouple with `D`: `<p1|p2> = 0.37, 0.15, 0.044, 0.014` and `<h1|h2> = 0.38, 0.021, 0.0013, 0.0036`.
4. The energy is additive to the same order: `(E_12 - E_1 - E_2)/(E_1 + E_2) = -2.1e-02, -2.3e-03, -2.7e-04, -5.8e-05`, and the additivity defect of `eps_v` itself falls an order of magnitude per unit of `D`, `2.1e-01, 2.4e-02, 2.7e-03`.
5. `sum_v rho = 0` to `1e-14` for every single-pair state **and** for every joint state: the count above this sea is identically zero, not merely small.

**Proof.** Item 1 recomputes the parent's own table before anything new is built. Item 2 is an algebraic property of the projector, `Q_p` and `Q_h` being orthonormal bases of two-dimensional spans lying wholly inside the empty and the occupied shells; the trace is
integer arithmetic. Items 3 to 5 are `[numerical]` at the tolerances printed with them, all from the `512 x 512` one-body projector; no many-body object is formed anywhere.

**Reading, not theorem.** Two lumps of matter above this sea sit in one state that is still a closed shell, and the closer they are the more their clouds overlap. Far enough apart, the energy of the two together is the sum of the energies of each alone, and the energy
at each site is likewise the sum, to an accuracy that improves tenfold for every extra unit of distance. What the two lumps together carry no more of than one lump does is count: it is zero for one pair, zero for two, and zero exactly.

## Theorem 2 -- the energy product

**Conclusion.** With `phi = G0 P0 rho` the landed response, validated first: the point control `4 pi r G` at `r = Lb/4` gives `0.3307` and `0.3275` at `Lb = 32, 64`, both parents' own row, to `5e-06`. Then:

1. `E_int = <eps_1, G0 P0 eps_2>` against `E_1 E_2 G0P0(D)` has ratio `0.8517, 0.9043, 0.9650, 0.9540` at the four `D` on `Lb = 64` with `d_pair = 1`.
2. Neither the internal separation nor the box is doing the work: `d_pair = 2` on `Lb = 64` gives `0.8757` and `0.9188` at `D = 3, 4`, and `Lb = 32` gives `0.9575` and `0.8997` at `D = 4` for the two `d_pair`.
3. `E_int` is exactly the cross term: `<eps_12, G eps_12> - <eps_1, G eps_1> - <eps_2, G eps_2> = 2 E_int` to `1e-15` over all sixteen box-and-separation rows.
4. The deficit from `1` is the sources' shape. Adding each source's dipole and traceless quadrupole to the point form gives `0.9380, 0.9146, 0.9773, 0.9576`, closing the gap to `1`-`3` per cent at `|D| >= 3`.
5. On two rigid copies of one `eps` profile in the `Lb = 64` box the ratio is `0.9462, 0.9736, 0.9938, 0.9986` at `D = 3, 4, 8, 16`.

**Proof.** `G0` is the discrete Fourier inverse of `lambda(k) = 6 - 2 sum_a cos k_a` with the zero mode set to zero, which is `P0` exactly rather than approximately; each pairing is one forward transform per source and one spectral sum. Item 3 is an exact identity of the
quadratic form, `<a+b, G (a+b)> = <a, G a> + <b, G b> + 2<a, G b>` for symmetric `G`, evaluated rather than asserted. Item 4 uses the standard continuum expansion of `1/(4 pi |R - (u - v)|)` to dipole and traceless-quadrupole order in each source's own moments, with no
fitted coefficient and no window. Item 5 places one profile twice in the box by a phase factor; the moments are the same profile's, so the deficit there is the shape's and the box's alone.

**Reading, not theorem.** Put two lumps of matter above this sea a distance apart, and the energy the field carries between them is the energy of the first times the energy of the second times the same kernel the landed field equation already had. The shortfall from
that product at close range is not a different law but the fact that a lump is not a point: it has a width, a dipole and a quadrupole, and adding those two moments accounts for nearly all of the shortfall. Far apart, the shortfall goes away.

## Theorem 3 -- the test-body law, and the gauge-sign rebuild lemma

**Conclusion.** On `Lb = 64`, with `F = -grad_{x2} E_int` by central differences on pair 2's centroid under rigid translation in the response box, against `F_pred = -E_2 grad phi_1(x_2)` and `phi_1 = G0 P0 eps_1`:

1. The `x`-component ratio is `0.8271` and `0.9719` at `D = 3, 4` for `d_pair = 1`, and `0.8568` and `0.9209` for `d_pair = 2`.
2. The two vectors point the same way: the angle between `F_num` and `F_pred` is `5.7, 6.5, 1.9` and `0.1` degrees on those same four rows.
3. **The gauge-sign rebuild lemma.** Rebuilding pair 2 one coarse site over on the `8^3` torus from a fresh positive seed is **not** faithful: the translation residual `max|eps - shift(eps)|` is `3.96e-01`. Carrying the seed by the KS field's gauge sign first gives
   `2.10e-03`. The KS sign field is not translation invariant, only gauge equivalent, and the naive rebuild's discrepancy is that gauge artefact and not a property of the pair.
4. The law tightens with separation. On rigid copies at `D = 3, 4, 6, 8, 10, 16` the `x` ratio is `0.8981, 0.9854, 0.9982, 0.9992, 0.9997, 1.0000` and the angle falls from `7.3` to `1.8` degrees; the inverse-square coefficient `4 pi D^2 F_x / (E_1 E_2)` reads
   `0.9711, 1.0398, 1.0216, 1.0060, 0.9924, 0.9260` against the source note's own point-kernel control `1.0194, 1.0064, 1.0009, 0.9963` at `d = 4, 6, 8, 10`, the same finite-box roll-off in both.

**Proof.** Every derivative is the same central difference over one lattice unit, taken on the numerical energy and on the predicted potential alike, so no differencing scheme separates them. The rigid translation is exact in the response box, a phase factor on the
source transform, which is precisely the bridge's own linear response and introduces no rebuild of the state. Item 3 is a controlled comparison: the same pair, the same site, one seed carried by the gauge sign and one not, with the translation residual reported for
both. Item 4's coefficient is compared against the landed control quoted before the run, on the same boxes and with the same readout; the roll-off at `D = 16` is the finite-volume window's, present in the control as it is here.

**Reading, not theorem.** The pull on the second lump is the second lump's energy times the slope of the first lump's field, and the two point the same way to within a few degrees. The agreement is not exact at close range for the same reason the product was not exact
at close range -- a lump has a width -- and it goes to one as the lumps separate. One thing needs care: the sign field that carries the hop is not the same at a shifted site, so a lump rebuilt one site over from scratch is not the same lump translated.
Carrying the seed by the field's own sign restores it, and that difference is a property of the sign field, named here rather than absorbed.

## Theorem 4 -- count versus energy: the pooled object differs by vacuum

**Conclusion.**

1. An energy knob at fixed `D = 4` -- one Gaussian seed band-filtered toward `+-E0` at width `0.6` -- carries `E_exc` through `3.8766, 4.5998, 5.3655, 5.8591, 6.0461`. Across those rows `E_int` lifts by a factor `2.525` while `E_1 E_2` lifts by `2.425`: a ratio of
   ratios of `1.041`.
2. The **same** bilinear form on the empty vacuum's count source -- two `A`-string pairs, `<n_v> = 1` at each string's two endpoints, `I = 2` per pair -- reads `E_int^count = 0.0655525` in every one of those rows, at spread `0e+00`. It is literally constant while the
   excitation's energy quadruples.
3. Above the half-filled sea the count product is identically `0`: `sum_v rho = 0` to `1e-14` by Theorem 1 item 5, so `I_1 I_2 = 0` there, while `E_1 E_2 = 32.25` for the same two pairs.
4. So the source note's Theorem 6 sentence stands unchanged where it was proved -- the object the pooled response carries is the count product `I(S) I(T)` and **not** a mass product, on the **empty** vacuum -- and above the half-filled sea the same form carries the
   **energy** product instead. The difference between the two is the vacuum and nothing else in this computation: same encoding, same hop, same kernel, same bilinear form.

**Proof.** Item 1's knob changes only the band filter applied to a fixed Gaussian seed, so the source stays localised and the only thing that moves is the excitation's energy; the ratio of ratios is reported rather than fitted. Item 2's count source is placed at the
same two centroids in the same box, so the kernel and the geometry are identical to item 1's and the only difference is which readout is used as `rho`; its constancy is a consequence of the count being an integer property of the string endpoints. Item 3 is Theorem 1
item 5 restated as a product. Item 4 is an implication of items 1 to 3 together with the quoted sentence, not a new computation.

**Reading, not theorem.** Turn up the energy of a lump without changing how many things are in it, and the pull between two such lumps grows in the same proportion as the product of their energies. The count reading does not move at all: it is the same number in every
row. Above the half-filled sea the count reading is not merely constant but zero, so nothing can be built from it. Which of the two objects the response carries is settled by which state is called the vacuum, and by nothing else here.

## Corollary -- what the vacuum choice supplies to the Newton lane

Within the setting declared above, conditional on the two supplied surfaces and on the supplied vacuum choice, and on the finite tori named:

1. **The bilinear response carries the energy product.** Conditional on the half-filled sea and on the energy density as the source, `E_int` equals `E_1 E_2 G0P0(D)` with the landed kernel, at a ratio that the sources' own dipole and quadrupole account for at short
   range and that goes to `1` as the sources separate, `0.9986` at `D = 16` on rigid copies.
2. **The test-body law holds within the bridge's linear response.** `F = -E_test grad phi` reproduces `-grad_{x2} E_int` at `x`-ratio `1.0000` and angle `1.8` degrees by `D = 16`, with the landed inverse-square coefficient and the landed finite-box roll-off.
3. **So the Newton lane's two residuals have candidates, supplied by a vacuum choice rather than by an axiom.** The mass-readout identification has the candidate `m = E_exc`, in units of the hop `t`; the test-body response law has the candidate form `F = -E_test grad
   phi`. Both are conditional on the half-filled sea being the framework's vacuum, which is not decided here or anywhere yet, and neither is derived from any axiom.
4. **On the empty vacuum nothing changes.** The source note's count product `I(S) I(T)` stands exactly as proved, and this note supplies no reason to prefer either branch.
5. **What is not repaired.** `eps_v` still fails two of the bridge's five source clauses -- it is not diagonal, the hop's `A_ij` carrying an `X`, and it is not guaranteed positive -- exactly as the parent's Theorem 5 records. This note uses `eps_v` as the parent's
   supplied even datum and repairs neither clause.

**Reading, not theorem.** Above the half-filled sea a lump of matter pulls on another lump in proportion to the product of their energies, with the same fall-off the landed field equation already had, and the pull on the second lump is its energy times the slope of the
first lump's field. Whether that is the framework's gravity turns on whether the half-filled sea is the framework's vacuum, which is not yet decided.

## What does not move

- No vacuum is chosen. The half-filled sea is taken as a **condition**, quoted from the note that names it as an undecided choice, and nothing here argues for or against either branch.
- No mass, no `M_phys`, no `G_Newton`, no coupling constant, and no absolute unit appears anywhere. `m = E_exc/t` is a dimensionless lattice number and is offered as a candidate identification, not as a mass.
- The bridge's five source clauses are not repaired. `eps_v` fails two of them above this vacuum and still does.
- Nothing at nonlinear order, no back-reaction, no self-consistency between the field and the state that sources it. Everything here is the supplied linear response.
- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.

## Interfaces named for other lanes, not moved here

- **The vacuum decision.** Still the parent's, still open, still for its owner. What this note adds is one more consequence on the half-filled branch: on that branch the mass readout and the test-body law both have candidate forms, and on the empty branch the count
  product stands. The decision is not made easier or harder by that; it is made more explicit.
- **The two failed clauses of `eps_v`.** A lane wanting a source above this sea that meets all five clauses owns them. Theorem 4 uses `eps_v` because the parent found it carries the monopole, not because it passes.
- **`G_Newton` and the unit carry.** Nothing here fixes a scale. The source note's declared factor-two coarse/fine carry -- reading (i) `1/(4 pi d_coarse) = 1/(2 pi |r_fine|)` against reading (ii) `1/(4 pi |r_fine|)` -- applies unchanged and is not adjudicated.
- **Back-reaction and self-consistency.** The field here is sourced by a fixed state and does not act back on it. A lane wanting a self-consistent pair owns that.
- **Larger physical tori.** Joint two-pair states exist here only to `|D| <= 4`, the `8^3` torus's own limit. Everything beyond that separation is rigid copies in the response box, labelled as such.

## Remaining live routes

1. Physical tori beyond `8^3`, where joint states at larger `D` would replace the rigid copies of Theorem 2 item 5 and Theorem 3 item 4.
2. A source above this sea meeting all five bridge clauses, which would remove the parent's Theorem 5 caveat from everything here.
3. Nonlinear order and back-reaction, both untouched.
4. The vacuum decision itself, which is not a computation.

## Executable claim block

The canonical machine-bound restatement of the four theorem conclusions and the unit statement.

```text
conditional_on: the supplied fermion law (declared supplier model, derived from no axiom); the landed weak-field response phi = G0 P0 rho at linear order; and the CHOICE of the half-filled staggered sea as the vacuum, quoted from the note that names it undecided
vacuum: 8^3 coarse torus, twist (1,1,1), E_sea = -611.811768 (3.5e-07 of the parent's own value), gap 2.651309 = 2 sqrt(6 - 3 sqrt2) (5.3e-15), <n_v> = 1/2 at all 512 sites (7.8e-16)
two_pair_state: P'' = P - Q_h + Q_p is a projector to 2e-15 with trace exactly 256 = V/2, at D = (2,0,0)/(3,0,0)/(4,0,0)/(3,3,0) and d_pair = 1, 2
decoupling: <p1|p2> = 0.37/0.15/0.044/0.014 and <h1|h2> = 0.38/0.021/0.0013/0.0036 at those four D
additivity: (E_12 - E_1 - E_2)/(E_1 + E_2) = -2.1e-02/-2.3e-03/-2.7e-04/-5.8e-05; the eps_v additivity defect falls an order of magnitude per unit of D, 2.1e-01/2.4e-02/2.7e-03
count_above_the_sea: sum_v rho = 0 to 1e-14 for every single-pair AND every joint state; the count product is identically 0 there
response_validation: point control 4 pi r G at r = Lb/4 = 0.3307/0.3275 at Lb = 32/64, both parents' own row, to 5e-06
energy_product: E_int/(E_1 E_2 G0P0(D)) = 0.8517/0.9043/0.9650/0.9540 at Lb = 64, d_pair = 1; 0.8757/0.9188 at D = 3, 4 with d_pair = 2; 0.9575/0.8997 at Lb = 32, D = 4
cross_term_identity: <eps_12, G eps_12> - <eps_1, G eps_1> - <eps_2, G eps_2> = 2 E_int to 1e-15 over all sixteen rows
multipole_accounting: point form corrected by each source's dipole and traceless quadrupole gives 0.9380/0.9146/0.9773/0.9576, closing the deficit to 1-3 per cent at |D| >= 3
large_separation: two RIGID copies of one eps profile on Lb = 64 (kernel and source shape, NOT a joint 8^3 state) give 0.9462/0.9736/0.9938/0.9986 at D = 3/4/8/16
test_body_law: F_x(-grad E_int)/F_x(-E_2 grad phi_1) = 0.8271/0.9719 at D = 3, 4 with d_pair = 1 and 0.8568/0.9209 with d_pair = 2; angles 5.7/6.5/1.9/0.1 degrees
gauge_rebuild_lemma: rebuilding a pair one coarse site over from a fresh seed gives translation residual 3.96e-01; carrying the seed by the KS gauge sign gives 2.10e-03 -- a sign-field artefact, named
force_scaling: rigid copies at D = 3/4/6/8/10/16 give x ratio 0.8981/0.9854/0.9982/0.9992/0.9997/1.0000, angle 7.3 -> 1.8 degrees
inverse_square: 4 pi D^2 F_x/(E_1 E_2) = 0.9711/1.0398/1.0216/1.0060/0.9924/0.9260 against the source note's point control 1.0194/1.0064/1.0009/0.9963 at d = 4/6/8/10
energy_knob: E_exc = 3.8766/4.5998/5.3655/5.8591/6.0461 at fixed D = 4; E_int lifts by 2.525 while E_1 E_2 lifts by 2.425, ratio of ratios 1.041
count_knob: the same bilinear form on the EMPTY vacuum's A-string count source (I = 2 per pair) reads E_int^count = 0.0655525 in EVERY row, spread 0e+00 -- literally constant
pooled_object: the count product I(S) I(T) on the empty vacuum, unchanged from the source note's T6; the energy product E_1 E_2 above the half-filled sea; the difference is the VACUUM and nothing else here
units: hop t = 1 so m = E_exc/t is a dimensionless lattice number; G0 P0 carries a^{-1} so E_int is in t^2/a; the source note's factor-2 coarse/fine carry applies unchanged and is not adjudicated
not_supplied: any choice of vacuum, G_Newton, a coupling, M_phys, an absolute unit, a repair of the two bridge clauses eps_v fails, anything nonlinear, back-reaction, joint states beyond |D| = 4
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=22 FAIL=0
```

## Proof boundary

The fermion law is a **designed supplier model**, in that note's own words "deriving that form from no axiom and claiming for it no privileged status"; the weak-field response is likewise a supplied surface, bounded in its own note; and the vacuum is a **choice**, quoted
from the note that names it as undecided and takes no side. Every statement above inherits all three: if any one is not the framework's, nothing above survives except as a statement about what was supplied. Nothing here is derived from any axiom.

Everything is at **linear order** in the supplied response, and at **finite volume**. The source is built on the `8^3` physical coarse torus and nowhere else, so joint two-pair determinant states exist here only to `|D| <= 4`; every separation beyond that is two rigid
copies of one profile in the response box, which is a statement about the kernel and the source shape and not about a joint state, and is labelled as such at every occurrence. Response boxes are `Lb = 32` and `64` and nowhere else. The finite-box roll-off of the
inverse-square coefficient at `D = 16` is the landed window's and is present in the like-for-like control too; it is reported rather than extrapolated away.

The **wavepacket placement is a choice**, as it was in the parent: the particle and hole are normalised Gaussians of unit width centred at named sites and projected into the empty and the occupied spans, and the energy knob of Theorem 4 is a band filter on that same
seed. `E_exc` varies by a few per cent across placements and every number is reported per configuration rather than averaged. The **twist cut** is named: with the pairs based at `x = 2` the `D = 3` translations stay off the cut, while a `+x` translation at `D = 4` lands
on it, which is why the reported force rows are the rigid ones -- exact translations in the response box -- and the rebuilt rows appear only in the gauge lemma of Theorem 3 item 3.

**No vacuum is chosen and no mass is claimed.** `m = E_exc/t` is a dimensionless lattice number offered as a candidate identification on one branch of an undecided question; it is not a mass, and no `G_Newton`, coupling or absolute unit appears. The two bridge clauses
`eps_v` fails above this vacuum are not repaired. Nothing nonlinear and no back-reaction is touched. No axiom is amended, no status is set, and no registry entry is created.

## Review record

An honest auditor should come away with: a conditional computation, not a derivation; four statements on named finite tori, one of them an exact identity of the quadratic form; a clean separation between what is a joint state on the physical torus and what is two rigid
copies in a response box, marked at every occurrence rather than left to the reader; a deficit from the ideal product form that is explained by the sources' own two leading moments rather than absorbed into a tolerance; one gauge artefact of the sign field found,
isolated by a controlled comparison, and named rather than corrected quietly; and a contrast between two vacua in which the earlier landed statement about the empty one is quoted verbatim and left exactly where it stands. Nothing here is a fitted number: the response
implementation is validated against both parents' own published control before any new value is reported, the inverse-square comparison uses a control quoted before the run, and every finite difference is taken identically on the computed and the predicted quantity.
The note is self-contained in the sense that matters for replay -- `upstream_dependencies` is empty, every object is declared in "Definitions", the runner imports nothing from the repository, and the two conditioning surfaces and the one conditioning choice are quoted
verbatim with paths rather than consumed as graded rows. The one thing an auditor should press hardest on is the conditional itself: the whole result is about a vacuum nobody has chosen, and the note says so in its scope, its corollary and its boundary. Hard landing
conditions are a fresh runner and cache pair closing at `PASS=22 FAIL=0` with runtime under the declared timeout and stdout under `5500` characters, and passing repository pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
````

## first #7881 revision — logs/runner-cache/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.txt

SHA-256 `27d4962c13c35644cf6555601b6b4a72d4717a5862351dd94e93402b6e87cab7`. Verbatim body follows.

````text
===== runner cache v1 =====
runner: scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py
runner_sha256: 21a25e2d77b9a5b4d5eebf0fc5380d9adcc7c18124a06801a4fca925727dc3d4
timeout_sec: 300
exit_code: 0
elapsed_sec: 0.77
status: ok
----- stdout -----
PASS A1 [numerical, 1e-6] the conditioning vacuum: the half-filled staggered sea on 8^3 at twist (1,1,1) has E_sea = -611.811768, the matter note's own value (3.5e-07), gap 2.651309 = 2 sqrt(6 - 3 sqrt2) (5.3e-15), <n_v> = 1/2 at all 512 sites (7.8e-16)
PASS A2 [numerical, 1e-13] single pairs first: the band-edge orbital pair has E_exc = 2.651309 and the localised wavepackets 4.3614 to 4.5163 over d = 1..4, sum_v eps_v = E_exc to 0e+00 -- the matter note's 2.651309 and 2.6513-4.5163
PASS A3 [numerical, 1e-14] TWO pairs above it at D = (2,0,0)/(3,0,0)/(4,0,0)/(3,3,0): P'' = P - Q_h + Q_p is a projector, max|P''^2 - P''| = 2e-15 over eight states, trace exactly 256 = V/2
PASS A4 [numerical] the pairs decouple with D: the orbital overlaps fall <p1|p2> = 0.37/0.15/0.044/0.014 and <h1|h2> = 0.38/0.021/0.0013/0.0036 at those D
PASS A5 [numerical] the joint energy is additive to the same order: (E_12 - E_1 - E_2)/(E_1 + E_2) = -2.1e-02/-2.3e-03/-2.7e-04/-5.8e-05 at d_pair = 1 and -2.3e-03/-2.7e-04 at d_pair = 2; the eps_v defect falls an order per unit of D, 2.1e-01 -> 2.4e-02 -> 2.7e-03
PASS A6 [numerical, 1e-13] the COUNT above this sea is identically zero: sum_v (<n_v> - 1/2) = 0 to 1e-14 for every single-pair AND every joint state, so a count product here is exactly 0, not merely small
PASS B1 [numerical, 1e-4] validation before any new number: the response is the landed one, G0 the Fourier inverse of lambda(k) = 6 - 2 sum_a cos k_a off the constant mode, its point control 4 pi r G at r = Lb/4 giving 0.3307 and 0.3275 at Lb = 32, 64, both parents' own row (5e-06)
PASS B2 [numerical, 1e-9] THE ENERGY PRODUCT. E_int = <eps_1, G0 P0 eps_2> against E_1 E_2 G0P0(D), Lb = 64, d_pair = 1: ratio 0.8517/0.9043/0.9650/0.9540 at those four D -- the bilinear response carries the product of the two excitation ENERGIES
PASS B3 [numerical, 1e-9] neither the internal separation nor the box is doing the work: d_pair = 2 on Lb = 64 gives 0.8757/0.9188 at D = 3, 4, and Lb = 32 gives 0.9575 (d_pair 1) and 0.8997 (d_pair 2) at D = 4
PASS B4 [numerical, 1e-14] E_int is exactly the cross term, not a fitted object: <eps_12, G eps_12> - <eps_1, G eps_1> - <eps_2, G eps_2> = 2 E_int to 1e-15 over all sixteen rows
PASS B5 [numerical] the deficit from 1 is the sources' SHAPE: adding each source's dipole and traceless quadrupole to the point form gives 0.9380/0.9146/0.9773/0.9576 against the computed 0.8517/0.9043/0.9650/0.9540, closing it to 1-3 per cent at |D| >= 3
PASS B6 [numerical] the ratio goes to 1 with separation: on two RIGID copies of one eps profile in the Lb = 64 box -- the kernel and the source shape, NOT a joint 8^3 state -- it is 0.9462/0.9736/0.9938/0.9986 at D = 3/4/8/16
PASS C1 [numerical, 1e-9] THE TEST-BODY LAW. F = -grad_{x2} E_int by central differences on pair 2's centroid against F_pred = -E_2 grad phi_1(x_2), phi_1 = G0 P0 eps_1: the x ratio is 0.8271/0.9719 at D = 3, 4 for d_pair = 1 and 0.8568/0.9209 for d_pair = 2, Lb = 64
PASS C2 [numerical] and the two vectors point the same way: the angle between F_num and F_pred is 5.7/6.5/1.9/0.1 degrees on those same four rows
PASS C3 [numerical] the GAUGE-SIGN REBUILD LEMMA, named not absorbed: rebuilding pair 2 one coarse site over from a fresh seed is NOT faithful, translation residual 3.96e-01, against 2.10e-03 when the seed is carried by the KS field's gauge sign: a sign-field artefact
PASS C4 [numerical] the law tightens with separation: on rigid copies at D = 3/4/6/8/10/16 the x ratio is 0.8981/0.9854/0.9982/0.9992/0.9997/1.0000 and the angle falls 7.3 -> 1.8 degrees
PASS C5 [numerical] the pull is inverse-square with the landed coefficient: 4 pi D^2 F_x/(E_1 E_2) = 0.9711/1.0398/1.0216/1.0060/0.9924/0.9260 at those D against the source note's point control 1.0194/1.0064/1.0009/0.9963 at d = 4/6/8/10
PASS D1 [numerical] COUNT VERSUS ENERGY. An energy knob -- one Gaussian seed band-filtered toward +-E0, width 0.6 -- moves E_exc through 3.8766/4.5998/5.3655/5.8591/6.0461 at fixed D = 4: E_int rises 1.000 -> 2.525 while E_1 E_2 rises 1.000 -> 2.425, a ratio of ratios of 1.041
PASS D2 [numerical, 1e-12] the SAME form on the empty vacuum's count source -- two A-string pairs, <n_v> = 1 at each string's two endpoints, I = 2 per pair -- reads E_int^count = 0.0655525 in EVERY one of those rows, spread 0e+00: constant while the excitation's energy quadruples
PASS D3 [numerical, 1e-13] and above this sea that count source does not exist: sum_v rho = 0 to 1e-14 for every pair and every joint state, so I_1 I_2 = 0 identically while E_1 E_2 = 32.25 for the same two pairs. The pooled object differs BY VACUUM
PASS D4 [stated] so the source note's T6 sentence stands where it was proved -- 'the object the pooled response carries is the count product I(S) I(T) and NOT a mass product', on the EMPTY vacuum -- while above this sea the same form carries the ENERGY product
PASS E1 [stated] units: hop t = 1, so every E_exc is in units of t and m = E_exc/t is a dimensionless lattice number; G0 P0 carries a^{-1}, so E_int is in t^2/a. No G_Newton, no coupling and no M_phys appears; the source note's factor-2 unit carry applies unchanged and is not adjudicated
SUMMARY: conditional on the half-filled sea as the vacuum, the bridge's bilinear response carries the product of the two excitation energies with the landed kernel, ratio -> 1 with separation, and F = -E_test grad phi holds in its linear response. Both candidates come from that choice, not an axiom.
TOTAL: PASS=22 FAIL=0

----- stderr -----

````

## Original runner recovery

- `79e3271b01a574426b404beead10fecd74ab87f0:scripts/matter_above_the_half_filled_sea_odd_and_even_densities_check_2026_09_03.py`, SHA-256 `6dd961e2a4ace198d7fc6d882a688477c6f875c96c9d654f6a35a8853ef73012`.
- `af1af53d28c8bf54a6e0440274ce01e5f0163eeb:scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py`, SHA-256 `b7d36311c3ae65187b5e4a27f8eb5f7b9a18462fccf0c4d12389b2a63d679374`.
- `4b135de8046553cc93304a7f6ca1071fa62e5509:scripts/the_vacuum_question_is_one_coefficient_of_the_law_check_2026_09_03.py`, SHA-256 `e7555a77393e22ce41e8dfa119befd0db6c3603dd950fc6c33b8abc8de31335d`.
- `c7ca994c385cc7d282c9017a8df17e6fe6e70821:scripts/energy_product_and_test_body_law_above_the_half_filled_sea_check_2026_09_03.py`, first action-sign revision source preserved.
