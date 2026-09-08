# Flux-selection source correction — 2026-09-08

This dated record preserves the original #7874/#7878 notes and caches verbatim. Their historical claims, failures, labels and numbers are retained as provenance, not current authority. The current canonical notes supersede their interpretation at the explicitly stated finite/conditional scope. Original runners remain recoverable from Git heads f45ec1559862575657ce5e2e5ccc020ec9f99a81 and 1a1d50f308c703d2e39924b9ae5b0c5e61d0c104; both original bases are36fe57a7a784df31bc2178c4b94dfc7caaa5d094.

Corrections cover even-N edge-code versus full Fock domains; diagonal gauge equivalence; finite exact versus numerical and sampled scopes; total occupation versus permanent Record; the attractive N=2 branch; finite Neel averages; the exact cube fourth-order diagonal/tunnelling split; independent MBPT pair counting; interpolation/error boundaries; bibliography; and genuine current publication/premise input binding. The original2000 draws plus500-subset disclosure was already correct and remains. No original numerical protocol, sampling seed or check ID is discarded. The old g-independent ground claim at attractive coupling and scalar-face interpretation are superseded explicitly; the useful fixed-sector spectra, exact inequalities and finite data remain.

No formal audit verdict is assigned. Historical citations and cache bodies below are not runtime/proof inputs of the current claims. There are no new parent campaign registrations.

## Exact original body

Path: `docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md`

SHA256: `9bf684bc9e7dd0af1777d0787a9d0d96ffac169dea8209dd1c3c5d5ed4ac32cc`

<!-- BEGIN ORIGINAL docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md -->
---
claim_id: half_filling_kinetic_energy_selects_staggered_flux_sector
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3, carrying one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, with free nearest-neighbour hopping sum_ij eta_ij c_i^dag c_j and no other term, the flux sector of a face being the eigenvalue of that face's stabilizer S_f and E_N the sum of the N lowest one-particle levels, on the named finite blocks and tori only: (T1) the open 2x2x2 coarse cube has exactly 32 consistent flux sectors of the 64 face assignments -- six faces with one F2 relation, so an even number of -1 faces -- confirmed by enumerating all 2^12 link-sign fields, which realise exactly those 32 holonomy patterns with the one-particle spectrum constant on each; the all-(+1) sector has E_N = 0, -3, -4, -5, -6, -5, -4, -3, 0 and the all-(-1) sector E_N = -N sqrt3 for N <= 4 with its mirror, both exact over the integers; at N = 4 the all-(-1) sector is the unique minimiser of all 32, by 0.456067 to the next distinct value and by 4 sqrt3 - 6 to the plain sector, while the unique minimiser is the plain sector at N = 1, 7, the two-flux class at N = 2, 6 and the four-flux class at N = 3, 5, and all 32 tie at N = 0 and 8. (T2) On the coarse tori 4^3, 4x4x6, 6^3 and 8^3 and the open blocks 3^3 and 4^3, sign(E_N(-) - E_N(+)) is + below N*, - on the whole of [N*, V - N*] and + above -- one contiguous window, the difference symmetric under N -> V - N -- with N* = 23, 30, 71, 171, 10, 22 respectively; at L = 4 the spectra are fixed exactly by integer minimal-polynomial and power-trace witnesses, E_32(-) - E_32(+) = 36 - 24 sqrt2 - 8 sqrt3 < 0, E_16(-) - E_16(+) = 48 - 24 sqrt2 - 8 sqrt3 > 0, and the first sign change is at N* = 23 where the difference is 46 - 24 sqrt2 - 8 sqrt3. (T3) The S_f fix no torus Wilson line, so each sector is a family of eight link-sign fields; minimised over the eight twists the half-filling energies are -78.383672 against -67.882251 on 4^3, -116.809009 against -99.882251 on 4x4x6 and -258.857540 against -218.564065 on 6^3, and the all-(-1) sector at its worst twist still beats the all-(+1) sector at its best, by 3.92, 10.15 and 36.58; the twisted Bloch formulas +-sqrt(6 + 2 sum_a cos q_a) and 2 sum_a cos q_a reproduce all 48 twisted real-space spectra of those tori at 1e-9. (T4) The 4^3 coarse torus is bipartite with every degree 6, so for ANY link-sign field on it the integer matrix M has tr M^2 = 2|E| = 6V = 384 and D M D = -M for the colour involution D, hence a spectrum symmetric about 0; the V/2 lowest squared levels therefore sum to 3V = 192 and Cauchy-Schwarz gives E_{V/2} >= -sqrt((V/2)(3V)) = -V sqrt(3/2) = -32 sqrt6 = -78.383672, with equality exactly when every |lambda| = sqrt6; the all-(-1) sector at its optimal twist satisfies M^2 = 6 I exactly as a 64x64 integer identity, its spectrum is +-sqrt6 with multiplicity 32 each, and it attains the bound, so it is a global minimiser at half filling over all 2^192 link-sign fields on that torus; on 4x4x6, 6^3 and 8^3 the same bound is -117.5755, -264.5449 and -627.0694 and the all-(-1) sector misses it by 0.766, 5.687 and 15.26. (T5) At half filling on 4^3 and 4x4x6, 2000 random link-sign fields per torus as drawn and a 500-field subsample with each field minimised over its own eight twists give 0 of 2500 fields beating the all-(-1) sector on either torus; the structured sectors with flux only on the xy, xz or yz plaquettes, xy flux on alternating x planes, and flux on the xz and yz plaquettes together are consistent and all strictly above it, while flux on the even-parity faces, xz+yz on alternating planes and a single-face flip off the all-(-1) sector are inconsistent; greedy single-link descent from 24 random restarts per torus never beats the all-(-1) field at its optimal twist and on 4^3 returns exactly that field; that field is a strict local minimum, every single-link flip raising E_{V/2} by at least 0.426844 on 4^3 and 0.365352 on 4x4x6. (T6) From the exact Bloch formulas the per-site half-filling energies converge to e(+) = -1.00241973 and e(-) = -1.19380112, a difference of -0.19138139 |t| per coarse site, while at quarter filling the difference is +0.07909 at L = 96; the crossing filling n* = N*/V settles to 0.339659 with the window ending at the mirror 1 - n* = 0.660341. T3 and T5 are search results, not theorems. Nothing here is derived from any axiom, no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py
---

# Half filling selects the staggered flux sector

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py`](../scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt`](../logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

A separate construction puts one fermionic mode on each vertex of the coarse lattice `2Z^3` and shows that transport of one encoded excitation around a coarse face
equals that face's stabilizer `S_f`, so the framework's staggered kinetic sign field is the sector in which every `S_f` is `-1` and the plain field is the sector in
which every one is `+1`. That construction states its own limit: the law as written attaches no coefficient to any face term, so the sector is a free choice under
the law. This note refines that statement. The law's hopping term *is* supplied, and it is not indifferent: on the finite clusters named below the hopping energy of
a filled Fermi sea distinguishes the two sectors, strictly, and which one it prefers depends on how much matter is present.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems on the flux-sector dependence of the free coarse-lattice hopping energy: exhaustive enumeration on the open 2x2x2 cube, exact surd spectra on the 4^3 torus, and an integer Cauchy-Schwarz certificate making the staggered sector a global half-filling minimiser there. The sampling, structured-sector and descent items are declared search results, not theorems, and the thermodynamic items are converged quadrature."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: what fixes the coarse-lattice matter density."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`. Group `A`, the `L = 4` content of `B` and the whole of `D` are
exact -- exhaustive enumeration, `sympy` surds, integer matrix arithmetic at zero tolerance, `F2`/`Z4` symplectic bit arithmetic -- and the items tagged
`[numerical]` are floating-point statements at the stated tolerance. Groups `C` and `E` are search results and are labelled as such wherever they appear.

1. `T1` (`A`). The exhaustive `2x2x2` cube: 32 consistent sectors, their `E_N` ladders, and the filling-dependent minimiser.
2. `T2` (`B`). The two uniform sectors on four tori and two open blocks: one contiguous `pi`-flux window `[N*, V - N*]`, with exact surds at `L = 4`.
3. `T3` (`C`). The Wilson-line caveat: the `S_f` fix no torus Wilson line, and the ordering survives every twist.
4. `T4` (`D`). The Cauchy-Schwarz certificate: on the `4^3` torus the staggered sector at its optimal twist is a global half-filling minimiser over all link-sign
   fields, and the gap by which the bound is missed elsewhere.
5. `T5` (`E`). Random, structured and greedily optimised sectors, all at half filling. Search results.
6. `T6` (`F`). The thermodynamic per-site difference and the crossing filling, from the exact Bloch formulas.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering and the tight-binding dispersion are standard
methodology; every object is redeclared here and the runner recomputes every statement. Lieb's flux-phase theorem is named only as background -- it fixes the
optimal flux of half-filled bipartite *planar* lattices, is not proved for the cubic lattice, and nothing below uses it or claims a cubic analogue. No observational
value, no fitted number and no framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): face transport equals `S_f`, and the sentence
  quoted below. Pointer only; the encoding, the sign fields and the face stabilizers are redeclared here and recomputed by this runner.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`: the kinetic-form clause quoted below.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". This note cites none of their grades and adopts no hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has
algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**:
"Records form", "a record locks exactly one admissible local possibility", "records are permanent", "Only records are readable."

The landed kinetic clause whose sign field is under test reads, verbatim:

> **Kinetic-form clause.** Within the declared kinetic class (the naive-Dirac kinetic form on nearest-neighbor `Z^3` links, made
> compatible with the matter-statistics clause by site-local spin diagonalization), the kinetic operator is the staggered operator
> `D = (1/2) Σ_{x,μ} η_μ(x) (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})` with the Kawamoto-Smit phases `η_1 = 1, η_2(x) = (−1)^{x_1},
> η_3(x) = (−1)^{x_1+x_2}`, unique as a local Z2 gauge class.

and the sentence this note refines, from the face-transport note, reads:

> So the two sectors are a free choice under the law as written; a face term `-J sum_f S_f` with negative `J` would select the staggered
> sector, and no such term is supplied by anything quoted here.

Everything below reads those sign fields on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, with free nearest-neighbour hopping and nothing else.
Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the two uniform
sign fields on it, the superfast encoding, the face stabilizers, the flux sectors and the filling functional `E_N`. `P1` (`A`) is the exhaustive `2x2x2` cube; `P2`
(`B`) the uniform sectors on the named tori and blocks and the shape of the difference; `P3` (`C`) the Wilson-line freedom; `P4` (`D`) the Cauchy-Schwarz bound and
its equality case; `P5` (`E`) the searches; `P6` (`F`) the thermodynamic limit. `P4` uses nothing from `P3` but its numbers; `P5` and `P6` use nothing from each
other. The strongest supported scope is precisely `P0`-`P6`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The
**KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`, the clause's phases read in coarse
coordinates; the **plain sign** is `+1` on every bond. The **encoding** is the Bravyi-Kitaev superfast encoding on the coarse lattice, code qubits on the coarse
edges, direction order `-x < -y < -z < +x < +y < +z`, with

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_i  = product of the Z's on the edges incident to i,   S_f = the ordered product of the four A's around a coarse face f
```

A **flux sector** is a choice of eigenvalue `+-1` for every `S_f` consistent with the `F2` relations among them; a sector is realised as a link-sign field `eta` by
spanning-tree gauge fixing followed by fundamental-cycle transport, and the plaquette holonomy of that field reproduces the sector face by face. The **hopping
matrix** is `M_ij = eta_ij` on nearest-neighbour coarse bonds and `0` elsewhere; `E_N` is the sum of its `N` lowest eigenvalues, the ground-state kinetic energy of
`N` spinless fermions, and the **filling** is `n = N/V`. On a torus the three **Wilson lines** -- the products of `eta` around the three non-contractible loops --
are gauge-invariant data that no `S_f` fixes; a **twist** flips the signs on one cut plane and changes one Wilson line without changing any face.

## Theorem 1 -- the exhaustive 2x2x2 cube

**Conclusion.** On the open `2x2x2` coarse cube, 8 sites, 12 links, 6 faces with one `F2` relation:

1. Exactly `32` of the `64` face assignments are consistent flux sectors -- those with an even number of `-1` faces -- and enumerating all `2^12` link-sign fields
   gives exactly those `32` holonomy patterns, with the one-particle spectrum constant on each pattern.
2. `E_N` of the all-`(+1)` sector is `0, -3, -4, -5, -6, -5, -4, -3, 0` and of the all-`(-1)` sector is `-N sqrt3` for `N <= 4` with its mirror, both exact.
3. At half filling `N = 4` the all-`(-1)` sector is the **unique** minimiser of all `32`, by `0.456067` to the next distinct value and by `4 sqrt3 - 6` to the plain
   sector. The unique minimiser is the plain sector at `N = 1, 7`, the two-flux class at `N = 2, 6` and the four-flux class at `N = 3, 5`; all `32` tie at `N = 0`
   and `N = 8`.

**Proof.** Item 1 solves the `F2` relations among the six face generators, realises each consistent assignment as a sign field and checks its holonomy face by face,
then enumerates the `4096` sign fields directly, `[numerical, 1e-12]` for the constancy of the spectrum within a pattern and exact for the pattern count. Item 2
diagonalises the two exact integer `8x8` matrices in `sympy` and sums the surds. Item 3 compares the `32` exact ladders entry by entry, with the tie counts
`32, 1, 3, 12, 1, 12, 3, 1, 32` and the minimiser's flux count `all, 0, 2, 4, 6, 4, 2, 0, all` printed by the runner.

**Reading, not theorem.** Eight sites and a choice of sign on each of six squares. With no particles, or with all eight sites full, every choice costs the same.
With one particle the plain arrangement is cheapest; with four -- one particle for every two sites -- the arrangement with a minus on every square is cheapest, and
by a clear margin. In between, other arrangements win. The cheapest sign pattern is a function of how many particles there are.

## Theorem 2 -- the uniform sectors on tori and open blocks

**Conclusion.** For the two uniform sectors on the coarse tori `4^3`, `4x4x6`, `6^3` and `8^3` and the open blocks `3^3` and `4^3`:

1. `sign(E_N(-) - E_N(+))` over `N = 1..V-1` is `+` below `N*`, `-` on the whole of `[N*, V - N*]` and `+` above: one contiguous window, and the difference is
   symmetric under `N -> V - N`. The values are `N* = 23, 30, 71, 171, 10, 22` in that order.
2. At `L = 4` both spectra are fixed exactly by an integer minimal-polynomial witness and integer power traces: `0 x20, +-2 x15, +-4 x6, +-6 x1` for the plain
   sector and `0 x8, +-2 x12, +-2sqrt2 x12, +-2sqrt3 x4` for the staggered one. Hence `E_32(-) - E_32(+) = 36 - 24 sqrt2 - 8 sqrt3 < 0` at half filling,
   `E_16(-) - E_16(+) = 48 - 24 sqrt2 - 8 sqrt3 > 0` at quarter filling, and the first sign change is at `N* = 23`, where the difference is
   `46 - 24 sqrt2 - 8 sqrt3`.
3. Where the sector is small enough to be formed from the `S_f` directly, the field read off the all-`(-1)` sector has holonomy `-1` on every plaquette and the same
   one-particle spectrum as the KS field, so the two labels name the same object here.

**Proof.** Item 2 evaluates the claimed minimal polynomial at the exact integer matrix, which vanishes over `Z`, and checks `tr M^k` for `k = 1..8` against the
claimed multiset, which fixes the multiplicities; the ladders and their difference are then exact sums of surds. Item 1 is `[numerical, 1e-9]` away from `L = 4`,
with `E_N = E_{V-N}` from the symmetry of a bipartite spectrum; item 3 likewise, and the `8^3` torus is evaluated from the Bloch formula, not a matrix.

**Reading, not theorem.** The same picture holds on every block tested. Below about a third filling the plain arrangement is cheaper, above about two thirds it
is cheaper again, and in the whole band between the two the minus-on-every-square arrangement is. The band is a single stretch, symmetric about half filling.

## Theorem 3 -- the Wilson-line caveat

**Conclusion.** The face stabilizers fix none of the three torus Wilson lines, so each sector is a family of eight link-sign fields, related by twists that change no
face. Minimising each uniform sector over its eight twists gives `E_{V/2} = -78.383672` against `-67.882251` on `4^3`, `-116.809009` against `-99.882251` on
`4x4x6` and `-258.857540` against `-218.564065` on `6^3`. The staggered sector at its **worst** twist still beats the plain sector at its best, by `3.92`, `10.15`
and `36.58` respectively. The twisted Bloch formulas `+-sqrt(6 + 2 sum_a cos q_a)` and `2 sum_a cos q_a`, with a half-integer momentum shift on each twisted axis,
reproduce all 48 twisted real-space spectra of those three tori.

**Proof.** Both statements are `[numerical, 1e-9]`: the eight twisted fields are built explicitly per sector, diagonalised, and compared, and the Bloch spectra are
compared eigenvalue by eigenvalue against the real-space ones.

**Reading, not theorem.** A sign on each link is not the whole story on a ring: besides the sign around every small square there is a sign around each way through
the box, and the squares do not fix those. This is a real freedom, and it moves the numbers. It does not move the comparison: the worst way of running the
minus-on-every-square field around the box is still cheaper than the best way of running the plain one.

## Theorem 4 -- the Cauchy-Schwarz certificate on the 4^3 torus

**Conclusion.**

1. The `4^3` coarse torus is bipartite, coloured by `(-1)^{v_1+v_2+v_3}`, with every degree `6`. So for **any** link-sign field on it the integer hopping matrix
   satisfies `tr M^2 = 2|E| = 6V = 384` and `D M D = -M` for the colour involution `D`, hence has a spectrum symmetric about `0`.
2. The `V/2` lowest levels are therefore the negatives of the `V/2` highest, their squares sum to `(1/2) tr M^2 = 3V = 192`, and Cauchy-Schwarz gives
   `E_{V/2} = -sum |lambda| >= -sqrt((V/2)(3V)) = -V sqrt(3/2) = -32 sqrt6 = -78.383672`, with **equality exactly when every `|lambda| = sqrt6`**.
3. The all-`(-1)` sector at its optimal twist satisfies `M^2 = 6 I` exactly, as a `64x64` integer matrix identity, so its spectrum is `+-sqrt6` with multiplicity
   `32` each and its half-filling energy attains the bound. It is therefore a **global minimiser at half filling over all `2^192` link-sign fields on that torus**.
4. The same bound reads `-117.5755` on `4x4x6`, `-264.5449` on `6^3` and `-627.0694` on `8^3`, and there the all-`(-1)` sector misses it by `0.766`, `5.687` and
   `15.26`: its spectrum `+-sqrt(6 + 2 sum_a cos q_a)` is not flat on those tori. Global minimality is a theorem on `4^3` and a search result elsewhere.

**Proof.** Items 1 and 3 are zero-tolerance integer matrix identities, item 1 on 52 fields including both uniform ones and item 3 on the single field named. Item
2 applies Cauchy-Schwarz to the `V/2` numbers `|lambda|`, whose sum of squares item 1 pins. Item 4 evaluates the bound and the exact Bloch energies, `[1e-9]`.

**Reading, not theorem.** Two facts about the box fix a floor no arrangement of signs can go below: every site has six neighbours, so the levels have a fixed total
spread, and the box is two-colourable, so they come in plus-minus pairs. Spreading a fixed total spread over a fixed number of levels is cheapest when every level
has the same size. On the smallest box the minus-on-every-square field, run the right way around the box, does exactly that: every level is the same size. So it is
not merely better than everything tried -- it is as good as anything could be.

## Theorem 5 -- the searches

**Conclusion.** At half filling on the tori `4^3` and `4x4x6`, all `[numerical, 1e-9]` and all **search results, not theorems**:

1. `2000` random link-sign fields per torus, each realising a consistent sector as drawn, and a `500`-field subsample with each field minimised over its own eight
   twists: `0` of `2500` beats the all-`(-1)` sector on either torus.
2. The structured sectors with flux only on the `xy`, `xz` or `yz` plaquettes, `xy` flux on alternating `x` planes, and flux on the `xz` and `yz` plaquettes
   together are consistent and all strictly above the all-`(-1)` sector. Flux on the even-parity faces, `xz+yz` on alternating planes, and a single-face flip off
   the all-`(-1)` sector are **inconsistent**: every face lies in two cube relations, so no sector differs from another in one face alone.
3. Greedy single-link descent from `24` random restarts per torus never beats the all-`(-1)` field at its optimal twist. On `4^3` its best equals that field
   exactly, `3` of `24` restarts reaching it. On `4x4x6` its best stays above, at `-116.134` against `-116.809`.
4. That field is a strict local minimum: every one of the `192` and `288` single-link flips raises `E_{V/2}`, by at least `0.426844` and `0.365352`.

**Proof.** Direct evaluation of `E_{V/2}` for each field, with the consistency of a structured assignment decided by the `F2` relations among the `S_f` before any
diagonalisation. The negative statements are statements about the samples drawn and the descent runs made, at the seeds the runner fixes, and are not claims about
the whole space.

**Reading, not theorem.** Two thousand random arrangements, five patterned ones, and a descent free to change any single link: nothing beats the
minus-on-every-square arrangement, and on the smallest box the descent walks straight back to it. Away from that box this is evidence, not proof.

## Theorem 6 -- the thermodynamic limit and the crossing filling

**Conclusion.** From the exact Bloch formulas -- `E = +- sqrt(6 + 2 sum_a cos q_a)` for the all-`(-1)` sector, fourfold, and `2 sum_a cos q_a` for the all-`(+1)`
one -- evaluated at `L = 4, 8, 16, 32, 64, 96` and by converged Brillouin-zone quadrature:

1. At half filling `e(+) = -1.00241973` and `e(-) = -1.19380112`, a difference of `-0.19138139 |t|` per coarse site in favour of the staggered sector.
2. At quarter filling the difference is `+0.07909` per coarse site at `L = 96`, in favour of the plain sector.
3. The crossing filling `n* = N*/V` settles to `0.339659` along the sequence `0.3594, 0.3287, 0.3340, 0.3380, 0.3411, 0.3398, 0.3394, 0.3397, 0.3396, 0.3397` at
   `L = 4, 6, 8, 12, 16, 24, 32, 48, 64, 96`, and the window ends at the mirror `1 - n* = 0.660341`.

**Proof.** Item 1 is `[numerical]` at converged quadrature: the reduced-grid Brillouin-zone integrals at `M = 600, 1200, 2400` agree to `1e-8` in `e(-)` and settle
to the digits quoted in `e(+)`. Items 2 and 3 are `[numerical, 1e-9]` on the `L = 96` Bloch grid, `n*` read off it by linear interpolation of the difference.

**Reading, not theorem.** In a large box the two arrangements differ by a fixed amount per site, not a vanishing one. Fill a third of the sites or fewer and the
plain arrangement is cheaper; fill more, up to two thirds, and the other is cheaper, by about a fifth of a hopping unit per site at half filling.

## Corollary -- what this says about the framework's kinetic form

Within the setting declared above, and on the finite blocks and tori named:

1. The law's own hopping term selects the framework's staggered kinetic form at half filling. No face term is supplied, and none is needed: the term already in the
   law does the selecting, uniquely on the `2x2x2` cube, provably against all link-sign fields on the `4^3` torus, and by a fixed amount per site in the limit.
2. The selection is a property of the **matter density**. Below `n* ~ 0.3397` and above `1 - n*` the plain sector is cheaper; between them the staggered sector is.
   At `N = 0` -- the record vacuum, no matter present -- every sector ties exactly, and at `N = V` they tie again.
3. So the question "which sector" is answered by "how much matter", and the filling is a supplied datum, not something this note derives. What the face-transport
   note calls a free choice under the law as written is free only until a matter density is named; once one is, the hopping term already in the law fixes the sector.
4. The `-J sum_f S_f` term that note describes is not needed for the half-filled case and is not supplied here. Nothing below the level of the hopping term is
   added, and no coefficient, coupling, rate or unit appears anywhere in this note.

**Reading, not theorem.** With no matter present, the sign on the squares costs nothing either way. Put in enough matter, about a third of the sites or more, and
the arrangement with a minus on every square is the cheapest by a fixed amount per site. That arrangement is the framework's staggered kinetic form: it is not
chosen by the law's wording; it is chosen by the matter's own energy.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding, the sign fields and the filling are declared objects, and the theorems are about them.
- No update rule, formation site, formation rate, coupling, mass, absolute unit or dynamical clause appears. The filling is supplied, never derived.
- No claim is made that a Lieb-type flux-phase theorem holds on the cubic lattice. The certificate of Theorem 4 is a Cauchy-Schwarz bound on one named torus.

## Interfaces named for other lanes, not moved here

- **The filling as a supplied datum.** Every statement here is conditional on `N`. Which filling the coarse lattice actually carries is a science question a lane
  owning the matter density must answer; nothing here narrows it, and Corollary item 3 states exactly what such a lane would have to supply.
- **Interacting terms.** Only free nearest-neighbour hopping is compared. A four-fermion term, or any interaction, could order the sectors differently, and no such
  term is examined.
- **Global minimality beyond `4^3`.** Theorem 4 is a theorem on the `4^3` torus and on the `2x2x2` cube only. On `4x4x6`, `6^3` and `8^3` the bound is missed and
  the statement is the search result of Theorem 5. A lane wanting global minimality there must supply a different certificate.
- **The Wilson-line convention.** Theorem 3 makes the twist explicit; which twist a physical setting selects is not decided here.
- **The many-body energetics.** Only the one-particle ladder `E_N` is used, the ground state of the free problem; what an interacting ground state prefers is
  untouched.

## Remaining live routes

1. Larger blocks and other geometries. The four tori and two open blocks named are what is proved; nothing is claimed beyond them.
2. Other fillings on the cube. Theorem 1 names a minimiser for each `N` on the `2x2x2` cube; the corresponding statement on larger clusters is not made.
3. Finite temperature. Everything here is a ground-state energy at fixed particle number, and `N = 0` and `N = V` tie exactly across all sectors.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one mode per coarse vertex, BK superfast encoding on it, free nearest-neighbour hopping only; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
objects: KS eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}; plain +1; S_f the face stabilizer; flux sector = consistent choice of S_f eigenvalues; E_N = sum of the N lowest levels of M_ij = eta_ij
cube_2x2x2: 32 of 64 face assignments consistent (flux counts 0, 2, 4, 6), confirmed by all 2^12 link fields giving exactly 32 holonomy patterns; E_N(+1) = 0, -3, -4, -5, -6, -5, -4, -3, 0; E_N(-1) = -N sqrt3 for N <= 4 and mirror
cube_minimisers: N = 4 unique all-(-1), margin 0.456067 to the next distinct value and 4 sqrt3 - 6 to plain; ties 32, 1, 3, 12, 1, 12, 3, 1, 32 and minimiser flux counts all, 0, 2, 4, 6, 4, 2, 0, all
uniform_window: tori 4^3, 4x4x6, 6^3, 8^3 and open blocks 3^3, 4^3; sign(E_N(-) - E_N(+)) is + below N*, - on [N*, V - N*], + above, symmetric under N -> V - N; N* = 23, 30, 71, 171, 10, 22
exact_L4: E_32(-) - E_32(+) = 36 - 24 sqrt2 - 8 sqrt3; E_16(-) - E_16(+) = 48 - 24 sqrt2 - 8 sqrt3 > 0; first sign change N* = 23 at 46 - 24 sqrt2 - 8 sqrt3
wilson: S_f fix no torus Wilson line; twist-minimised E_{V/2} = -78.383672 vs -67.882251 (4^3), -116.809009 vs -99.882251 (4x4x6), -258.857540 vs -218.564065 (6^3); staggered at its worst twist beats plain at its best by 3.92, 10.15, 36.58
certificate: 4^3 bipartite, all degrees 6, so tr M^2 = 6V = 384 and D M D = -M for any link field; E_{V/2} >= -V sqrt(3/2) = -32 sqrt6 = -78.383672, equality iff every |lambda| = sqrt6; all-(-1) at its optimal twist has M^2 = 6 I exactly, spectrum +-sqrt6 x32 each, attains the bound: global minimiser over all 2^192 fields
certificate_gaps: bound -117.5755, -264.5449, -627.0694 on 4x4x6, 6^3, 8^3, missed by 0.766, 5.687, 15.26
searches: 2000 random fields per torus plus a 500-field Wilson-minimised subsample, 0 of 2500 beating all-(-1) on 4^3 or 4x4x6; five structured sectors consistent and all above; even-parity faces, alternating xz+yz and any one-face flip inconsistent; 24 greedy restarts per torus never beat it and on 4^3 return it; strict local minimum, smallest single-flip rise 0.426844 and 0.365352
thermodynamic: e(+) = -1.00241973, e(-) = -1.19380112 at half filling, difference -0.19138139 |t| per coarse site; +0.07909 at quarter filling at L = 96; n* -> 0.339659, mirror 0.660341
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=19 FAIL=0
```

## Proof boundary

The content is **free nearest-neighbour hopping only**, on **finite** clusters, at a **supplied** filling. No interaction, mass, coupling, rate, temperature or
absolute unit appears, and no dynamical clause is proposed. Nothing here is derived from the four axioms.

Global minimality over all link-sign fields is a **theorem on exactly two clusters**: the open `2x2x2` cube, by exhaustion of all `2^12` fields, and the `4^3`
coarse torus, by the Cauchy-Schwarz certificate whose equality case the all-`(-1)` sector meets. On `4x4x6`, `6^3` and `8^3` the bound is missed by the stated gaps
and the corresponding statement is a **search result** -- a statement about the samples drawn and the descent runs made at the runner's fixed seeds, not about the
whole space. Theorem 3 and Theorem 5 are search results throughout and are labelled so wherever they are used.

No Lieb-type flux-phase theorem is claimed for the cubic lattice. Lieb's theorem is planar; it is named as background only and no step below invokes it.

The three torus **Wilson lines** are gauge-invariant data that no face stabilizer fixes, so "the sector" alone does not name a link-sign field on a torus. Every
torus comparison here is either at the stated twist or minimised over all eight, and Theorem 3 records both. Theorem 5's `4x4x6` descent result is that the best
restart stays *above* the all-`(-1)` field, not that it reaches it; only the `4^3` descent returns that field exactly.

The identification of the all-`(-1)` sector with the staggered kinetic form is up to a **site relabelling**, and is verified spectrally here only on the clusters
small enough for the sector to be formed directly from the `S_f`; on the larger tori the KS field is used and its holonomy is `-1` on every face by construction.

## Review record

An honest auditor should come away with: one exhaustive finite-cluster theorem naming the staggered sector as the unique half-filling minimiser on the `2x2x2`
cube; one exact-surd statement of where the two uniform sectors cross on four tori and two open blocks, with a single contiguous window symmetric about half
filling; one genuine certificate -- a Cauchy-Schwarz bound whose equality case the staggered sector meets exactly on the `4^3` torus, making it a global minimiser
there over all `2^192` link-sign fields; a clearly labelled band of search results away from that torus; and one honest limit, that the whole statement is
conditional on a filling this note does not derive.

The three things most likely to be over-read are flagged in the proof boundary: global minimality holds as a theorem on two clusters only; the `4x4x6` descent does
not reach the staggered field, it merely fails to beat it; and no cubic-lattice flux-phase theorem is claimed. This note is self-contained:
`upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the three context notes in "Imports and authority" are
plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=19 FAIL=0`, runtime under the
declared `120` seconds, stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence
gates; independent audit remains a separate lane.
<!-- END ORIGINAL docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md -->

## Exact original body

Path: `docs/RECORD_CONSERVING_INTERACTION_KEEPS_THE_STAGGERED_SECTOR_AT_HALF_FILLING_BOUNDED_THEOREM_NOTE_2026-09-03.md`

SHA256: `e92cdc267608de4e5f89b3e84f87c86d8ff9a9cf74a2d1a6e79f6bdc8d95a9d9`

<!-- BEGIN ORIGINAL docs/RECORD_CONSERVING_INTERACTION_KEEPS_THE_STAGGERED_SECTOR_AT_HALF_FILLING_BOUNDED_THEOREM_NOTE_2026-09-03.md -->
---
claim_id: interaction_keeps_staggered_sector_half_filling
claim_type: bounded_theorem
claim_scope: "On the coarse cubic lattice 2Z^3, one fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding written on it, the flux sector of a face being the eigenvalue of that face's stabilizer S_f, and the law read on the record-conserving nearest-neighbour family H(t, V) = -t sum_bonds eta_ij (c_i^dag c_j + c_j^dag c_i) + V sum_bonds n_i n_j at t = 1 with the single ratio g = V/t, on the many-body ground state at fixed particle number N and on the named finite clusters only: (T1) on the open 2x2x2 coarse cube at half filling, N = 4, dimension 70, all 32 consistent flux sectors compared, the all-(-1) sector is the unique many-body minimiser at every g in {-2, -1, -0.5, 0, 0.5, 1, 2, 4, 8}, with margins to the next distinct sector 0.192, 0.344, 0.408, 0.456, 0.483, 0.485, 0.407, 0.158, 0.025; and exactly over Z at the twelve integer g in {-8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 32, 64}, where the 70x70 integer characteristic polynomials give minimal polynomials of E_0 over Z for both uniform sectors -- degrees 3, 3, 3, 4, 1, 4, 3, 3, 4, 4, 4, 4 for the plain sector and 5, 5, 5, 5, 2, 5, 5, 5, 5, 5, 5, 5 for the staggered one, the plain g = 2 polynomial being x^3 - 10x^2 - 16x + 48 and the staggered g = 0 polynomial x^2 - 48 -- and a CRootOf comparison gives E_0(-) < E_0(+) strictly at all twelve with no tie and no floating point. (T2) On the same cube away from half filling, N = 2 and N = 6, dimension 28, the interaction does reorder: the minimiser is the two-flux class, three tied sectors, at every g in that list and the all-(-1) sector is never it, sitting at rank 31, 31, 31, 31, 31, 31, 31, 30, 27 of 32; exactly, at N = 2 the staggered characteristic polynomial carries the g-free factor x^2 - 12, so E_0(-) = -2 sqrt3 at every g, while E_0(+) is the least root of x^3 - g x^2 - 16 x + 8 g, and the two are equal exactly at g_c = 2 sqrt3. (T3) On the open 2x2x3 coarse block at half filling, N = 6, dimension 924, 11 faces of F2 rank 9 and exactly 512 consistent sectors of 2048 face assignments, the all-(-1) sector is the unique minimiser of all 512 at every g in {0, 0.5, 1, 2, 4, 8, 16}, with margins 0.381, 0.401, 0.401, 0.311, 0.058, 0.0048, 0.00049, its ground state non-degenerate and the plain sector's 2-fold throughout, the plain sector ranking 500, 500, 509, 511, 511, 511, 511 of 512; on the attractive side it is still the unique minimiser at g = -1, -2 and -2.3 and is beaten at g = -2.4 by an 8-flux class of 8 tied sectors, so the flip window is -2.4 < g_c < -2.3, while the uniform pair itself never crosses on [-64, 64], E_0(-) - E_0(+) being at most -4.53e-05 over the 15 couplings scanned. (T4) First-order perturbation theory in V about the twist-minimised free half-filled sea on the coarse tori 4^3, 6^3, 8^3, 10^3 and 12^3, with A = sum_bonds (P_ii P_jj - P_ij^2) by Wick, gives A/V = 0.65625, 0.66427, 0.66505, 0.66541, 0.66592 for the plain sector against 0.62500, 0.63032, 0.63101, 0.63116, 0.63120 for the staggered one, so the first-order correction also favours the staggered sector at every L; on 4^3 the integer hopping matrices satisfy M^6 - 52 M^4 + 676 M^2 = 1152 I at the all-antiperiodic twist for the plain field and M^2 = 6 I for the staggered one, making both occupied projectors polynomials in M with rational squared entries, so A(+) = 42 = 21/32 per site and A(-) = 40 = 5/8 per site exactly, dE_free = 48 sqrt2 - 32 sqrt6, and the only first-order crossing is attractive, at g_c = 24 sqrt2 - 16 sqrt6 = -5.250710; by converged Brillouin-zone quadrature the limiting values are A/V = 0.666263 and 0.631237 and g_c = -5.4639. Second-order MBPT on 4^3 gives -10.50142 - 2.00000 g + 0.44685 g^2, whose positive root g = 7.577 is refuted by T1 and T3 and is recorded as a caution about the truncation, not a result. (T5) At large coupling on the cube both sectors freeze into the same Neel doublet: <n_i> = 1/2 on every site in both sectors to 5e-14 at g = 4, 8, 16, 32, the staggered moment m^2 rising to 0.24945 and 0.24944 against the Neel value 1/4 and the weight on the two Neel patterns to 0.99708 and 0.99704; the t^2/V exchange is sector-independent, g E_0 -> -6 in both sectors and g^2 (E_0(-) - E_0(+)) -> 0 along -0.4216, -0.2109, -0.1055 at g = 64, 128, 256; and the surviving difference is order t^4/V^3, g^3 (E_0(-) - E_0(+)) = -26.9815477888, -26.9953982475, -26.9988502688, -26.9997126114 at g = 64, 128, 256, 512 in 60-digit arithmetic with local exponent 2.99926, 2.99982, 2.99995 and Richardson limit -26.9999999999, that is E_0(-) - E_0(+) = -27 t^4/V^3 + O(V^-4), a plaquette ring exchange of 9/4 per face carrying the sign S_f; the same structure holds on the 2x2x3 block with its own coefficient, g^3 (E_0(-) - E_0(+)) settling near -11.8530 ~ -320/27. All statements are at fixed particle number, on the named clusters, for that one interaction family. Nothing here is derived from any axiom, no axiom is amended, no status is set, and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.py
---

# A record-conserving interaction keeps the staggered sector at half filling

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.py`](../scripts/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.txt`](../logs/runner-cache/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.txt)
**Parents:** none. Every premise used below is declared in this note.

A separate construction puts one fermionic mode on each vertex of the coarse lattice `2Z^3` and shows that transport of one encoded excitation around a coarse face equals that
face's stabilizer `S_f`, so the framework's staggered kinetic sign field is the sector in which every `S_f` is `-1` and the plain field is the sector in which every one is `+1`.
A second result shows that the *free* hopping energy of a half-filled sea prefers the staggered sector, strictly, and names its own limit: only free hopping was compared. This
note removes that limit for one declared interaction family, reading the comparison off the interacting many-body ground state at fixed particle number.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact and exhaustive finite-cluster theorems on the flux-sector ordering of one record-conserving interacting law: every consistent sector of the open 2x2x2 cube and of the open 2x2x3 block diagonalised at fixed particle number, the cube's half-filling ordering fixed over Z by minimal polynomials and a CRootOf comparison, the off-half-filling crossing fixed exactly at 2 sqrt3, and the 4^3 first-order coefficients fixed by integer matrix certificates. The torus items are first (and, once, second) order in V and are labelled so; the large-coupling ring-exchange coefficient is a high-precision numerical limit, and its sign, not its value, is what the note carries."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-cluster theorem, and route to its owner the science-level question this note does not decide: which interaction the coarse lattice actually carries."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. The integer-`g` content of `A`, the whole exact item of `B` and the `4^3`
item of `D` are exact -- `sympy` characteristic polynomials of integer matrices, symbolic `g`, surds, `CRootOf` comparison, integer matrix identities at zero tolerance, `F2`/`Z4`
symplectic bit arithmetic, exhaustive enumeration -- and items tagged `[numerical]` are floating-point at the stated tolerance.

1. `T1` (`A`). The exhaustive `2x2x2` cube at half filling, with the exact minimal-polynomial ordering.
2. `T2` (`B`). The same cube away from half filling, where the interaction does reorder, and the exact crossing `g_c = 2 sqrt3` for the uniform pair.
3. `T3` (`C`). The exhaustive `2x2x3` block at half filling, repulsive and attractive, with the attractive flip window.
4. `T4` (`D`). First-order perturbation theory in `V` on five coarse tori, exact on `4^3`, with the second-order truncation recorded only as a caution.
5. `T5` (`E`). The large-coupling structure: one Neel doublet, one sector-independent `t^2/V` exchange, and a plaquette ring exchange at order `t^4/V^3`.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, Wick's theorem for a Slater determinant and
Rayleigh-Schrodinger perturbation theory are standard methodology; every object is redeclared here and the runner recomputes every statement. Lieb's flux-phase theorem is named
only as background -- it is planar and free, is not proved for the cubic lattice, and nothing below uses it. No observational value, no fitted number and no framework premise
enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7874): the free-hopping selection at half filling and the interface
  sentence quoted below, which is the question this note answers.
- `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7833): the interaction family quoted below.
- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): face transport equals `S_f`.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". This note cites none of their grades and adopts no hypothesis.

All four are pointers only: the encoding, the sign fields, the face stabilizers, the sector machinery and the interaction family are redeclared below and every matrix is built
from scratch by this runner.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations,
and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has algebraic presentation
`M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations", and "For each site, the
probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a record locks exactly one
admissible local possibility", "records are permanent", "Only records are readable." The interface sentence this note answers reads, verbatim, from the half-filling note:

> **Interacting terms.** Only free nearest-neighbour hopping is compared. A four-fermion term, or any interaction, could order the sectors differently, and no such term is
> examined.

The interaction examined is not invented here. It is the one-parameter family already declared by the composition discriminator, quoted verbatim from that note:

> The **law family** is one expression read on either composition, `H(t, V) = -t sum_bonds (x_i^dag x_j + x_j^dag x_i) + V sum_bonds n_i n_j,   x = b or x = c,` with the same
> real `t` and `V` on every bond. **Cubic-covariant** means exactly that: one bond expression, identical on every bond, symmetric under reversing a bond, commuting with
> `sum_i n_i`.

and, from the same note, "So the record statistics depend on the single ratio `g = V/t`, taken at `t = 1`." Everything below reads that family on the graded composition `x = c`,
with the bond sign field `eta_ij` restored on the hopping term so the flux sector is still a free label. Composition is **ordinary**: a region's algebra is the tensor product of
its sites' algebras and no graded clause is used.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the two uniform sign fields on
it, the superfast encoding, the face stabilizers, the flux sectors, the record-number sector and the interacting Hamiltonian `H(g)`. `P1` (`A`) is the exhaustive cube at half
filling; `P2` (`B`) the same cube at `N = 2, 6`; `P3` (`C`) the exhaustive `2x2x3` block; `P4` (`D`) the first-order torus theory; `P5` (`E`) the large-`g` structure. `P2` and
`P3` use nothing from each other; `P4` uses nothing from `P1`-`P3` except in its own refutation clause, which cites their numbers only. The strongest supported scope is precisely
`P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v` and the coarse edge from `v` along `e_a` at `2v + e_a`. The **KS sign** of the coarse bond
`(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`; the **plain sign** is `+1` on every bond. The **encoding** is the Bravyi-Kitaev superfast
encoding on the coarse lattice, code qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`, with `A_ij` the encoded hop generator and `S_f` the ordered
product of the four `A`s around a coarse face. A **flux sector** is a choice of eigenvalue `+-1` for every `S_f` consistent with the `F2` relations among them, realised as a
link-sign field by spanning-tree gauge fixing then fundamental-cycle transport, its plaquette holonomy reproducing the sector face by face.

The **record-number sector** at particle number `N` is the span of the occupation patterns with `N` sites occupied, of dimension `C(V, N)`. On it the law reads

```text
H(g) = - sum_bonds eta_ij (c_i^dag c_j + c_j^dag c_i) + g sum_bonds n_i n_j,     g = V/t at t = 1,
```

with `c` the Jordan-Wigner ladders in the fixed site order, so the hopping carries the string sign and the interaction is diagonal. `E_0(g)` is the lowest eigenvalue of `H(g)` in
that sector, `E_0(-)` and `E_0(+)` its values in the all-`(-1)` and all-`(+1)` sectors, and **half filling** is `N = V/2`. On a torus the three **Wilson lines** are
gauge-invariant data no `S_f` fixes and a **twist** flips the signs on one cut plane; every torus statement is minimised over the eight twists. `P` is the occupied one-particle
projector of the free sea and `A = sum_bonds (P_ii P_jj - P_ij^2)` the Wick value of `sum_bonds n_i n_j` in that determinant, so the first-order energy in `V` is `E_free + g A`.

## Theorem 1 -- the exhaustive cube at half filling

**Conclusion.** On the open `2x2x2` coarse cube, `8` sites, `12` bonds, `6` faces of `F2` rank `5`, at half filling `N = 4`, the record-number sector having dimension `70`:

1. Exactly `32` of the `64` face assignments are consistent flux sectors, flux counts `0, 2, 4, 6`, each realised by a link-sign field of that holonomy.
2. Comparing all `32` at `g = -2, -1, -0.5, 0, 0.5, 1, 2, 4, 8`, the all-`(-1)` sector is the **unique** minimiser at every one, by
   `0.192, 0.344, 0.408, 0.456, 0.483, 0.485, 0.407, 0.158, 0.025` to the next distinct sector.
3. At the twelve integer `g = -8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 32, 64` the `70x70` integer characteristic polynomials give minimal polynomials of `E_0` over `Z` for both
   uniform sectors, of degrees `3, 3, 3, 4, 1, 4, 3, 3, 4, 4, 4, 4` (plain) and `5, 5, 5, 5, 2, 5, 5, 5, 5, 5, 5, 5` (staggered) -- for instance `x^3 - 10x^2 - 16x + 48` for the
   plain sector at `g = 2` and `x^2 - 48` for the staggered sector at `g = 0`. A `CRootOf` comparison of those algebraic numbers gives `E_0(-) < E_0(+)` strictly at all twelve,
   with no tie and no floating point anywhere.

**Proof.** Item 1 solves the `F2` relations among the six face generators, realises each consistent assignment as a sign field and checks its holonomy face by face, exactly. Item
2 builds the `70x70` real matrix of each sector at each `g` and compares lowest eigenvalues, `[numerical, 1e-10]`. Item 3 builds the matrix over `Z`, takes its characteristic
polynomial in `sympy`, extracts the least real root as a `CRootOf` with its minimal polynomial over `Z` (domain checked to be `ZZ`), and compares the two roots symbolically.

**Reading, not theorem.** Eight sites, four particles, a sign on each of six squares, and now a price for two particles sitting on the ends of the same bond. With that price
switched on -- at any of the strengths tried, and whether the price is a charge or a reward -- the arrangement with a minus on every square is still the cheapest of all
thirty-two, and at whole-number strengths the comparison is a comparison of exact numbers, not of decimals.

## Theorem 2 -- away from half filling the interaction does reorder

**Conclusion.** On the same cube at `N = 2` and `N = 6`, the record-number sector having dimension `28`:

1. At every `g` in the list of Theorem 1 the minimiser of all `32` sectors is the **two-flux class**, three tied sectors, and the all-`(-1)` sector is never it: it sits at rank
   `31, 31, 31, 31, 31, 31, 31, 30, 27` of `32`.
2. Exactly, with symbolic `g`: at `N = 2` the staggered sector's characteristic polynomial carries the `g`-free factor `x^2 - 12`, so `E_0(-) = -2 sqrt3` at **every** `g`, while
   `E_0(+)` is the least root of `x^3 - g x^2 - 16 x + 8 g`. The two are equal exactly at `g_c = 2 sqrt3`, the plain sector lower below it and the staggered sector lower above.

**Proof.** Item 1 diagonalises all `32` sectors at each `g` and `N`, `[numerical, 1e-10]`. Item 2 builds the `28x28` matrix over `Z[g]`, factors its characteristic polynomial in
`sympy` and reads off the two factors named; the crossing is `sympy`'s exact solution of the cubic evaluated at `x = -2 sqrt3`.

**Reading, not theorem.** With two particles instead of four the answer is different, and it was different before the price was switched on. Neither the plain arrangement nor the
one with a minus on every square is cheapest there; a third arrangement is. The one place where the price changes nothing is the one place the free comparison already singled
out. That is not a weakness of the statement -- it is what makes half filling the point worth naming.

## Theorem 3 -- the exhaustive 2x2x3 block

**Conclusion.** On the open `2x2x3` coarse block, `12` sites, `20` bonds, `11` faces of `F2` rank `9`, at half filling `N = 6`, the record-number sector having dimension `924`:

1. Exactly `512` of the `2048` face assignments are consistent flux sectors.
2. At `g = 0, 0.5, 1, 2, 4, 8, 16` the all-`(-1)` sector is the **unique** minimiser of all `512`, by `0.381, 0.401, 0.401, 0.311, 0.058, 0.0048, 0.00049` to the next distinct
   sector. Its ground state is non-degenerate at every one; the plain sector's is `2`-fold at every one, and the plain sector ranks `500, 500, 509, 511, 511, 511, 511` of `512`.
3. On the attractive side the all-`(-1)` sector is still the unique minimiser at `g = -1, -2, -2.3`, and at `g = -2.4` it is beaten by an `8`-flux class of `8` tied sectors,
   falling to rank `8`. The flip window is `-2.4 < g_c < -2.3`.
4. The uniform **pair** itself never crosses on `[-64, 64]`: `E_0(-) - E_0(+) < 0` at all `15` couplings scanned, the largest value being `-4.53e-05`. The attractive flip of item
   3 is a third sector overtaking both, not the pair reordering.

**Proof.** Item 1 is the `F2` relation count, exact. Items 2-4 assemble each sector's sparse `924x924` matrix from one precomputed hopping graph and take its lowest levels by
Lanczos at tolerance `1e-12`, `[numerical, 1e-9]`; the degeneracies are read from the three lowest levels.

**Reading, not theorem.** A second, longer box with a different number of squares, and the same answer: with the price switched on, the minus-on-every-square arrangement is the
single cheapest of all five hundred and twelve, and its cheapest state is unique while the plain one's is doubled. Turn the price into a reward and there is a strength --
somewhere between minus two point three and minus two point four -- past which a different arrangement wins instead.

## Theorem 4 -- first order in V on the coarse tori

**Conclusion.** For the twist-minimised free half-filled sea of each uniform sector on the coarse tori `4^3, 6^3, 8^3, 10^3, 12^3`, with `A = sum_bonds (P_ii P_jj - P_ij^2)` the
Wick value of the interaction in that determinant:

1. Every sea is closed-shell, gaps `2.83, 0.54, 0.63, 0.47, 0.14` (plain) and `4.90, 3.46, 2.65, 2.14, 1.79` (staggered), the small `12^3` plain gap reported as such; `A/V` is
   `0.65625, 0.66427, 0.66505, 0.66541, 0.66592` (plain) against `0.62500, 0.63032, 0.63101, 0.63116, 0.63120` (staggered), so `Delta A < 0` at every `L`.
2. On `4^3` at the all-antiperiodic twist the integer hopping matrices satisfy `M^6 - 52 M^4 + 676 M^2 = 1152 I` (plain) and `M^2 = 6 I` (staggered) exactly, so both occupied
   projectors are polynomials in `M` with rational squared entries and `A(+) = 42 = 21/32` per site and `A(-) = 40 = 5/8` per site are **exact**. With
   `dE_free = 48 sqrt2 - 32 sqrt6` the only first-order crossing is on the attractive side, at `g_c = 24 sqrt2 - 16 sqrt6 = -5.250710`, exactly.
3. By converged Brillouin-zone quadrature, using the closed forms `P_ij = <cos q_1>_occ` for the plain sea and `P_ij = +-(h(0) + h(2e_1))/2` with `h = (6 + W)^{-1/2}` for the
   staggered one, the limiting values are `A/V = 0.666263` and `0.631237` and the limiting first-order crossing is `g_c = -5.4639`.
4. Second-order many-body perturbation theory on `4^3` gives `dE(g) = -10.50142 - 2.00000 g + 0.44685 g^2`, whose positive root `g = 7.577` would predict a repulsive-side flip;
   it is contradicted by Theorem 1 at `g = 8, 16, 32, 64`, where the ordering is exact over `Z`, and by Theorem 3 at `g = 8, 16`. Recorded as a **caution about the truncation**.

**Proof.** Item 1 diagonalises each twisted real-space hopping matrix, forms `P` from the occupied columns and sums the bond terms, `[numerical, 1e-9]`. Item 2 verifies the two
integer identities at zero tolerance and evaluates `A` in exact rational arithmetic from the polynomial projectors. Item 3 is converged quadrature, `M = 400` and `M = 800`
agreeing to `1e-5`. Item 4 is a standard antisymmetrised second-order sum over the free orbitals.

**Reading, not theorem.** Perturbation theory in the price, on boxes far bigger than the ones that can be solved outright, agrees: the first correction is smaller for the
minus-on-every-square arrangement, so switching the price on widens the gap rather than closing it. One order further on the smallest box suggests a strength at which the order
would flip; the boxes that can be solved exactly say it does not.

## Theorem 5 -- the large-coupling structure

**Conclusion.** At strong repulsion on the cube at half filling:

1. `<n_i> = 1/2` on every site in **both** sectors, to `5e-14`, at `g = 4, 8, 16, 32`; the staggered moment `m^2` rises to `0.24945` (plain) and `0.24944` (staggered) against the
   Neel value `1/4` and the weight on the two Neel patterns to `0.99708` and `0.99704`, and the same rise holds on the `2x2x3` block, where the plain ground space is `2`-fold and
   the densities are degeneracy-averaged. The order parameter does not tell the sectors apart.
2. The `t^2/V` exchange is sector-**independent**: `g E_0 -> -6` in both sectors, and `g^2 (E_0(-) - E_0(+)) -> 0` along `-0.4216, -0.2109, -0.1055` at `g = 64, 128, 256`.
3. The whole surviving difference is order `t^4/V^3`. In `60`-digit arithmetic `g^3 (E_0(-) - E_0(+)) = -26.9815477888, -26.9953982475, -26.9988502688, -26.9997126114` at
   `g = 64, 128, 256, 512`, with local exponent `2.99926, 2.99982, 2.99995` and Richardson limit `-26.9999999999`. So `E_0(-) - E_0(+) = -27 t^4/V^3 + O(V^-4)`: a plaquette ring
   exchange of `9/4` per face entering with the sign `S_f`, hence `-9/4` per face in the staggered sector and `+9/4` in the plain one.
4. The same structure holds on the `2x2x3` block with its own coefficient, `g^3 (E_0(-) - E_0(+))` running `-12.126, -11.921, -11.869, -11.856, -11.853` at `g = 16, ..., 256`,
   settling near `-11.853 ~ -320/27`. The coefficient is a cluster number; the **sign** is what the two clusters share.

**Proof.** Items 1 and 2 are direct diagonalisation, `[numerical, 1e-9]` and converged in `1/g`. Item 3 diagonalises the exact `70x70` integer matrices in `mpmath` at `60`
digits, so the difference of two nearly equal energies is not a double-precision cancellation; the exponent comes from successive ratios and the limit from Richardson
extrapolation in `1/g^2`. Item 4 is the double-precision `924x924` computation, converged in `1/g`.

**Reading, not theorem.** Push the price up and the particles stop moving: they settle into a checkerboard, identically in both arrangements, so nothing about where they sit
distinguishes the arrangements any more. What is left is small residual motion, and a particle stepping onto its neighbour's site and back costs the same in both. The first thing
that does not is a particle going once around a square and returning, which picks up the sign on that square; and that trip is cheaper when the sign is minus.

## Corollary -- what this says about the framework's kinetic form

Within the setting declared above, and on the finite clusters named:

1. For the record-conserving family at half filling, the interaction does **not** reorder the sectors on any cluster or coupling tested on the repulsive side: the cube's ordering
   is exact over `Z` at twelve integer couplings, the block's all-`(-1)` sector is the unique minimiser of all `512` at seven, and five tori agree at first order.
2. The reason at large coupling is structural. The density profile, the Neel weight and the `t^2/V` exchange are all sector-independent, so the sign on a plaquette enters the
   energy only through the ring exchange around it -- and that prefers the staggered sign, `-27 t^4/V^3` on the cube and `~ -320/27` on the block.
3. So the staggered kinetic form remains the choice of the matter's own energy with the discriminator's interaction present; the free result did not need its absence.
4. Away from half filling (`T2`) and on the attractive side (`T3`) the ordering **is** cluster- and coupling-dependent, with an exact crossing at `g_c = 2 sqrt3` for the cube's
   uniform pair at `N = 2` and a flip window `-2.4 < g_c < -2.3` for the block. That sharpens the statement: half filling on the repulsive side is the robust point.
5. No coefficient, coupling, rate, mass or absolute unit is fixed anywhere. `g` is a ratio scanned over a declared list, and the filling is supplied.

**Reading, not theorem.** Adding the repulsion between neighbours does not change which sign pattern is cheapest when half the sites carry matter; at strong repulsion the matter
freezes into a checkerboard in either pattern, and the only thing that still tells the patterns apart is how the particles go once around a square, which still favours the minus
sign. With fewer particles, or with attraction, the answer can change.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, no hypothesis is adopted, no status value is set, predicted or implied, and no premise registry, citation
  manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The coarse lattice, the encoding, the sign fields, the filling and the interaction family are declared objects, and the family is not
  proposed, preferred, or fixed by this note: it is quoted from the composition discriminator's note and scanned in `g`.
- No update rule, formation site, formation rate, coupling, mass, absolute unit or dynamical clause appears, and no Lieb-type cubic flux-phase theorem is claimed or used.

## Interfaces named for other lanes, not moved here

- **Attraction and other fillings.** `T2` and `T3` show the ordering there is cluster- and coupling-dependent. Nothing here decides it, and no lane should read the half-filling
  repulsive statement across those boundaries.
- **Longer-range or spin-dependent interactions.** One nearest-neighbour density-density family is examined; a longer-range term, a bond-dependent `V`, or a spin-carrying term is
  untouched.
- **An interacting global-minimality certificate on tori.** The free case had one on `4^3`, a Cauchy-Schwarz bound met with equality; that bound is free-fermion only, there is no
  interacting analogue here, and the torus statements are first (once second) order in `V`, not exhaustive.
- **Exact derivation of the ring-exchange coefficient.** The `-27` is a high-precision numerical limit, not a degenerate-perturbation-theory derivation. A lane wanting the
  coefficient from the algebra must supply that derivation; the sign is what this note carries.
- **The filling as a supplied datum.** Every statement is conditional on `N`, exactly as in the free case. Which filling the coarse lattice carries is a science question a lane
  owning the matter density must answer.

## Remaining live routes

1. Larger exhaustive clusters. Two open blocks are enumerated in full here; `2x2x4` and beyond are not.
2. The interacting problem on a torus -- only first-order theory is done there, with the Wilson-line freedom handled by twist minimisation of the free sea -- and the interacting
   problem at fixed chemical potential, or at finite temperature, rather than at fixed `N`.

## Executable claim block

```text
setting: coarse lattice 2Z^3, one mode per coarse vertex, BK superfast encoding on it; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
law: H(g) = -sum_bonds eta_ij (c_i^dag c_j + c_j^dag c_i) + g sum_bonds n_i n_j at t = 1, g = V/t; family quoted from the composition discriminator's note
objects: KS eta_1 = 1, eta_2(v) = (-1)^{v_1}, eta_3(v) = (-1)^{v_1+v_2}; plain +1; S_f the face stabilizer; flux sector = consistent choice of S_f eigenvalues; E_0(g) = lowest eigenvalue in the N-particle record-number sector
cube_half_filling: 2x2x2, N = 4, dim 70, all 32 sectors; all-(-1) unique minimiser at g = -2, -1, -0.5, 0, 0.5, 1, 2, 4, 8; margins 0.192, 0.344, 0.408, 0.456, 0.483, 0.485, 0.407, 0.158, 0.025
cube_exact: integer g = -8, -4, -2, -1, 0, 1, 2, 4, 8, 16, 32, 64; min polys of E_0 over Z, degrees 3,3,3,4,1,4,3,3,4,4,4,4 (plain) and 5,5,5,5,2,5,5,5,5,5,5,5 (staggered); plain g=2 is x^3 - 10x^2 - 16x + 48, staggered g=0 is x^2 - 48; CRootOf gives E_0(-) < E_0(+) at all 12, 0 ties
cube_off_half_filling: N = 2 and N = 6, dim 28; minimiser is the two-flux class (3 tied) at every g, all-(-1) at rank 31,31,31,31,31,31,31,30,27 of 32
cube_off_exact: N = 2 staggered charpoly factor x^2 - 12, so E_0(-) = -2 sqrt3 for all g; plain E_0(+) least root of x^3 - g x^2 - 16 x + 8 g; equality exactly at g_c = 2 sqrt3
block: 2x2x3, N = 6, dim 924, 11 faces of F2 rank 9, exactly 512 of 2048 assignments consistent; all-(-1) unique minimiser at g = 0, 0.5, 1, 2, 4, 8, 16 with margins 0.381, 0.401, 0.401, 0.311, 0.058, 0.0048, 0.00049; deg(-) = 1 and deg(+) = 2 throughout; plain rank 500, 500, 509, 511, 511, 511, 511 of 512
block_attractive: all-(-1) unique at g = -1, -2, -2.3; beaten at g = -2.4 by an 8-flux class of 8 tied sectors, rank 8; flip window -2.4 < g_c < -2.3; uniform pair never crosses on [-64, 64], largest E_0(-) - E_0(+) = -4.53e-05
tori_first_order: 4^3, 6^3, 8^3, 10^3, 12^3, twist-minimised closed-shell seas, gaps 2.83/0.54/0.63/0.47/0.14 (plain) and 4.90/3.46/2.65/2.14/1.79 (staggered); A/V = 0.65625, 0.66427, 0.66505, 0.66541, 0.66592 (plain) vs 0.62500, 0.63032, 0.63101, 0.63116, 0.63120 (staggered); Delta A < 0 at every L
tori_exact_L4: M^6 - 52 M^4 + 676 M^2 = 1152 I (plain) and M^2 = 6 I (staggered) at the all-antiperiodic twist; A(+) = 42 = 21/32 per site, A(-) = 40 = 5/8 per site; dE_free = 48 sqrt2 - 32 sqrt6; g_c = 24 sqrt2 - 16 sqrt6 = -5.250710
tori_limit: converged BZ quadrature gives A/V = 0.666263 (plain) and 0.631237 (staggered), e/V = -1.00241976 and -1.19380112, g_c = -5.4639
mbpt2_caution: 4^3 second order gives -10.50142 - 2.00000 g + 0.44685 g^2, positive root 7.577, refuted by cube_exact at g = 8, 16, 32, 64 and by block at g = 8, 16
large_g: <n_i> = 1/2 in both sectors to 5e-14 at g = 4, 8, 16, 32; m^2 -> 0.24945 / 0.24944 and Neel weight -> 0.99708 / 0.99704; g E_0 -> -6 in both; g^2 dE -> 0 along -0.4216, -0.2109, -0.1055
ring_exchange: g^3 dE = -26.9815477888, -26.9953982475, -26.9988502688, -26.9997126114 at g = 64, 128, 256, 512 (mpmath, 60 digits), exponents 2.99926, 2.99982, 2.99995, Richardson -26.9999999999; E_0(-) - E_0(+) = -27 t^4/V^3 + O(V^-4), i.e. 9/4 per face carrying the sign S_f; on 2x2x3 the same quantity settles near -11.853 ~ -320/27
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=18 FAIL=0
```

## Proof boundary

The content is **one interaction family**, on **finite** clusters, at a **supplied** particle number. The family is not derived, preferred or fixed here: it is quoted from the
composition discriminator's note and scanned in `g` over declared lists. No mass, rate, temperature or absolute unit appears.

Exhaustive comparison over **all** consistent flux sectors is done on **exactly two clusters**: the open `2x2x2` cube, all `32`, and the open `2x2x3` block, all `512`. There is
no torus analogue; on the tori only first order in `V` is computed, and once, on `4^3`, second order recorded as a caution against itself. The free-case Cauchy-Schwarz
certificate does not extend -- it bounds a one-particle ladder, not an interacting ground state -- so **no global-minimality claim is made anywhere in this note**.

The half-filling statement is **repulsive-side and half-filling only**. Theorem 2 exhibits a filling at which the ordering is different at every `g` tested, with an exact
crossing at `2 sqrt3`; Theorem 3 exhibits an attractive coupling at which a third sector wins. Both are results of this note, not caveats bolted onto it, and neither may be read
as narrowing the half-filling repulsive claim beyond what is stated.

The `-27` and the `-320/27` are **cluster coefficients**, high-precision numerical limits and not a derived ring-exchange amplitude; what transfers between the two clusters is
the **sign**. The `12^3` plain sea's shell gap is `0.136`, the smallest in the table, and the first-order value there should be read with that in mind. The identification of the
all-`(-1)` sector with the framework's staggered kinetic form is up to a **site relabelling**, verified spectrally on clusters small enough for the sector to be formed directly
from the `S_f`; on the tori the KS field is used and its holonomy is `-1` on every face by construction.

## Review record

An honest auditor should come away with: two exhaustive interacting finite-cluster theorems naming the staggered sector as the unique many-body ground sector at half filling, one
exact over `Z` at twelve integer couplings by minimal polynomials and a `CRootOf` comparison; one exactly located reordering away from half filling at `g_c = 2 sqrt3` and one
attractive flip window on the larger block, both stated as results; a first-order torus computation pointing the same way, exact on `4^3` by two integer matrix identities; a
large-coupling structure in which only a plaquette ring exchange separates the sectors; and one honest limit, that nothing here is a global-minimality claim.

The four things most likely to be over-read are flagged in the proof boundary: exhaustive means two open clusters and no torus; the half-filling statement is repulsive-side only,
with `T2` and `T3` marking where it ends; the second-order torus root at `g = 7.58` is a truncation artefact and is reported as one; and the ring-exchange coefficients are
cluster numbers whose transferable content is their sign. This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis
is adopted, and the four context notes in "Imports and authority" are plain-text pointers carrying no grade and no weight. Hard landing conditions are a fresh runner and cache
pair closing at `PASS=18 FAIL=0`, runtime under the declared `180` seconds, stdout under `5500` characters, a current zero-dependency citation-manifest entry, and passing
pipeline, strict-lint and changed-evidence gates; independent audit remains a separate lane.
<!-- END ORIGINAL docs/RECORD_CONSERVING_INTERACTION_KEEPS_THE_STAGGERED_SECTOR_AT_HALF_FILLING_BOUNDED_THEOREM_NOTE_2026-09-03.md -->

## Exact original body

Path: `logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt`

SHA256: `2074ebd65426a38e99a66eed7a4cc39b6541e58194b6a22267e7ab786974794d`

<!-- BEGIN ORIGINAL logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt -->
===== runner cache v1 =====
runner: scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py
runner_sha256: 311a6a400423359d23bca50786976a0746e5ed45858b97a0347a5df54467eb8b
timeout_sec: 120
exit_code: 0
elapsed_sec: 19.32
status: ok
----- stdout -----
PASS A1 [exact] open 2x2x2 cube, 6 faces with one F2 relation: 32 of 64 face assignments are consistent sectors, flux counts [0, 2, 4, 6]; the 4096 link fields realise exactly those 32 patterns, spectrum constant on each (4e-15)
PASS A2 [exact, sympy] uniform sectors on the cube, exact integer 8x8 matrices: E_N(+1) = 0, -3, -4, -5, -6, -5, -4, -3, 0; E_N(-1) = -N sqrt3 for N <= 4 and its mirror
   N=0..8 min E_N: 0.000 -3.000 -4.828 -5.878 -6.928 -5.878 -4.828 -3.000 -0.000
   ties/flux     : 32/all 1/0 3/2 12/4 1/6 12/4 3/2 1/0 32/all
PASS A3 [exact] at N = 4 the all-(-1) sector UNIQUELY minimises all 32: margin 0.456067 to the next value, 4 sqrt3 - 6 = 0.928203 to plain. Minimiser: plain at N = 1, 7; two-flux at N = 2, 6; four-flux at N = 3, 5; all 32 tie at N = 0, 8
PASS B1 [exact, sympy] torus 4^3: integer minimal-polynomial and trace witnesses fix both spectra. E_32 = -60 (plain) and -24*sqrt(2) - 24 - 8*sqrt(3) (staggered); E_N(-) - E_N(+) = c - 24sqrt2 - 8sqrt3 with c = 48 at N = 16 (+0.2025), 36 at N = 32 (-11.7975), 46 at the first sign change N* = 23 (-1.7975)
   name     V |  E(+) V/4,V/2,3V/4 |  E(-) same        |  N*
   T4^3    64 |  -48.0  -60.0  -48.0 |  -47.8  -71.8  -47.8 |  23
   T4x4x6  96 |  -76.0  -96.0  -76.0 |  -69.4 -112.3  -69.4 |  30
   T6^3   216 | -168.0 -216.0 -168.0 | -149.5 -258.9 -149.5 |  71
   T8^3   512 | -400.5 -506.6 -400.5 | -357.4 -609.4 -357.4 | 171
   B3^3    27 |  -15.6  -21.2  -17.0 |  -13.8  -26.0  -15.8 |  10
   B4^3    64 |  -42.8  -56.0  -42.8 |  -39.7  -66.0  -39.7 |  22
PASS B2 [numerical, 1e-9] tori 4^3, 4x4x6, 6^3, 8^3 (Bloch) and open blocks 3^3, 4^3: staggered strictly lower at half filling on all six, higher at quarter and three-quarter; the sector read off S_f matches KS spectrally where formed
PASS B3 [numerical, 1e-9] sign(E_N(-) - E_N(+)) is + below N*, - on all of [N*, V - N*], + above -- one contiguous window, symmetric under N -> V - N -- with N* = (23, 30, 71, 171, 10, 22) in table order
PASS C1 [numerical, 1e-9] the S_f fix no Wilson line, so a sector is a family of 8 fields. Minimised over them: -78.384 vs -67.882 (4^3, staggered W=---), -116.809 vs -99.882 (4x4x6), -258.858 vs -218.564 (6^3); staggered at its WORST twist beats plain at its best by 3.92, 10.15, 36.58
PASS C2 [numerical, 1e-9] the Bloch formulas +-sqrt(6 + 2 sum cos q_a) and 2 sum cos q_a, with a half-integer shift per twisted axis, reproduce all 48 twisted real-space spectra of the three tori, max deviation 2.7e-14
PASS D1 [exact, integer] the 4^3 torus is bipartite (colour (-1)^{|v|}), every degree 6, so ANY link-sign field has tr M^2 = 2|E| = 6V = 384 and D M D = -M, a spectrum symmetric about 0 -- zero-tolerance integer identities on 52 fields
PASS D2 [exact] the V/2 lowest levels are minus the V/2 highest, so their squares sum to (1/2) tr M^2 = 3V = 192 and Cauchy-Schwarz gives E_{V/2} >= -V sqrt(3/2) = -32 sqrt6 = -78.383672 on 4^3, equality iff every |lambda| = sqrt6
PASS D3 [exact, integer] the all-(-1) sector at its optimal twist has M^2 = 6 I EXACTLY (64x64 integer identity), spectrum +-sqrt6 x32 each, so E_32 = -32 sqrt6 = -78.383672 attains the bound: a GLOBAL minimiser over all 2^192 link-sign fields
PASS D4 [numerical, 1e-9] elsewhere the spectrum is not flat and the bound is missed: -117.58 vs -116.81 on 4x4x6 (gap 0.766), -264.54 vs -258.86 on 6^3 (gap 5.687), -627.07 vs -611.81 on 8^3 (gap 15.26)
PASS E1 [numerical, 1e-9] 2000 random link fields per torus: E_{V/2} min/med/max as drawn -69.5/-67.6/-66.0 (4^3), -103.7/-101.4/-99.2 (4x4x6), and -69.5/-68.0/-66.7, -103.7/-101.8/-99.9 over 500-field Wilson-minimised subsamples; 0 of 2500 beats all-(-1)
PASS E2 [numerical, 1e-9] structured sectors -- flux only on xy, xz or yz plaquettes, xy on alternating x planes, xz+yz -- are consistent and all above all-(-1); even-parity-face flux, alternating xz+yz and a one-face flip are inconsistent
PASS E3 [numerical, 1e-9] greedy single-link descent, 24 random restarts per torus, never beats the Wilson-minimised all-(-1) field: best -78.384 on 4^3, exactly that field (3 of 24 reach it); best -116.134 on 4x4x6, above -116.809
PASS E4 [numerical, 1e-9] the all-(-1) field at its optimal twist is a strict local minimum of E_{V/2}: all 192 and all 288 single-link flips raise it, by at least 0.426844 (4^3) and 0.365352 (4x4x6)
   L=4..96 e(+)1/2: -0.93750 -0.98937 -1.00075 -1.00217 -1.00238 -1.00240
           e(-)1/2: -1.12184 -1.19015 -1.19359 -1.19379 -1.19380 -1.19380
PASS F1 [numerical, 1e-9] exact Bloch formulas at L = 4..96 (above): at half filling staggered is lower at every L, settling at e(-) = -1.19380096 vs e(+) = -1.00240220; at quarter filling higher at every L, by +0.07909 per site
PASS F2 [numerical, converged quadrature] the BZ integrals of |2 sum cos q| and sqrt(6 + 2 sum cos q) on reduced grids M = 600, 1200, 2400 converge to e(+) = -1.00241973, e(-) = -1.19380112 at half filling; difference -0.19138139 |t| per site
   n* by L: 4:0.3594 8:0.3340 32:0.3394 96:0.3397
PASS F3 [numerical, 1e-9] the crossing filling n* = N*/V settles to 0.339659 (above), the window ending at the mirror 1 - n* = 0.660341: plain is cheaper below about a third filling and above its mirror
SUMMARY: the law's hopping term is not indifferent to the sector -- at half filling the all-(-1) (staggered) sector wins on every block tested; below n* = 0.3397 the plain sector wins.
TOTAL: PASS=19 FAIL=0

----- stderr -----

<!-- END ORIGINAL logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt -->

## Exact original body

Path: `logs/runner-cache/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.txt`

SHA256: `d58e6e0e8dc57f0e3a8e4dbeb48e985aeb1187f72532fdf80fa316432ef5146a`

<!-- BEGIN ORIGINAL logs/runner-cache/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.txt -->
===== runner cache v1 =====
runner: scripts/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.py
runner_sha256: b9d666ae0ca2dace54609dc814cc440da0f8e2c347387798561a8c9677022eb4
timeout_sec: 180
exit_code: 0
elapsed_sec: 30.02
status: ok
----- stdout -----
PASS A1 [exact] open 2x2x2 cube, 6 faces of F2 rank 5: exactly 32 of 64 face assignments are consistent sectors, flux counts 0/2/4/6, each realised by a link field of that holonomy
   A2 cube N=4, g:margin of all-(-1) to the next sector -- -2:0.192 -1:0.344 -0.5:0.408 0:0.456 0.5:0.483 1:0.485 2:0.407 4:0.158 8:0.025
PASS A2 [numerical, 1e-10] cube N = 4 (70-dim), H(g) = -sum eta_ij (c^dag c + h.c.) + g sum n_i n_j: all-(-1) is the UNIQUE minimiser of all 32 at each g above
   A3 min poly of E_0 over Z, plain g=2: x**3 - 10*x**2 - 16*x + 48 ; staggered g=0: x**2 - 48
     deg +: 333414334444 deg -: 555525555555 at g = -8,-4,-2,-1,0,1,2,4,8,16,32,64
PASS A3 [exact, sympy over Z] the 70x70 integer characteristic polynomials at those twelve g give minimal polynomials of E_0 over Z for both uniform sectors, degrees above
PASS A4 [exact, CRootOf comparison, no floating point] E_0(-) < E_0(+) strictly at all 12, 0 ties: the ordering is exact over Z, not a tolerance
   B1 cube N=2, g:minimiser flux class/rank of all-(-1) of 32 -- -2:2/31 -1:2/31 -0.5:2/31 0:2/31 0.5:2/31 1:2/31 2:2/31 4:2/30 8:2/27
PASS B1 [numerical, 1e-10] the same cube off half filling, N = 2 and N = 6 (28-dim): the minimiser is the two-flux class (3 tied) at every g above, never all-(-1)
   B2 cube N=2 charpoly factors -- plain -g*x**2 + 8*g + x**3 - 16*x ; staggered x**2 - 12
PASS B2 [exact, sympy, symbolic g] cube N = 2: the staggered factor x^2 - 12 is g-free, so E_0(-) = -2 sqrt3 at EVERY g and the pair crosses exactly at g_c = 2 sqrt3
PASS C1 [exact] open 2x2x3 block, 12 sites, 20 bonds, 11 faces of F2 rank 9: exactly 512 of 2048 assignments are consistent sectors; the N = 6 sector has dimension 924
   C2 2x2x3 N=6, 512 sectors, g:margin/plain rank/degeneracies -- 0:0.381/500/1/2 0.5:0.401/500/1/2 1:0.401/509/1/2 2:0.311/511/1/2 4:0.0581/511/1/2 8:0.0048/511/1/2 16:0.000491/511/1/2
PASS C2 [numerical, 1e-9] 2x2x3, N = 6 (924-dim), all 512 sectors: all-(-1) is the UNIQUE minimiser at every g above, non-degenerate, the plain sector 2-fold throughout
   C3 attractive, g:tied minimisers/flux count/rank of all-(-1) -- -1:1/11/0 -2:1/11/0 -2.3:1/11/0 -2.4:8/8/8
PASS C3 [numerical, 1e-9] attractive side (above): all-(-1) is still unique at g = -1, -2, -2.3, but at -2.4 an 8-flux class of 8 tied sectors takes over -- flip window -2.4 < g_c < -2.3
PASS C4 [numerical, 1e-9] the uniform PAIR never crosses on [-64, 64]: E_0(-) - E_0(+) < 0 at all 15 couplings there, largest -4.53e-05 -- the -2.4 flip is a third sector passing both
   D1 tori L = 4, 6, 8, 10, 12; e_free/V: -1.0607/-1.2247 -1.0119/-1.1984 -1.0096/-1.1949 -1.0075/-1.1942 -1.0042/-1.1940
      gap: 2.83/4.90 0.54/3.46 0.63/2.65 0.47/2.14 0.14/1.79 ; A/V: 0.65625/0.62500 0.66427/0.63032 0.66505/0.63101 0.66541/0.63116 0.66592/0.63120
PASS D1 [numerical, 1e-9] first order in V about the twist-minimised free sea, tori 4^3 ... 12^3, A = sum_bonds (P_ii P_jj - P_ij^2) by Wick (above): A/V is SMALLER in the staggered sector at every L
   D2 4^3 exact: A(+) = 42 = 21/32/site, A(-) = 40 = 5/8/site, dE_free = -32*sqrt(6) + 48*sqrt(2), g_c = -16*sqrt(6) + 24*sqrt(2)
PASS D2 [exact, integer certificates + surds] on 4^3 at the optimal twist M^6 - 52 M^4 + 676 M^2 = 1152 I and M^2 = 6 I, so both projectors are polynomials in M with rational squared entries: the values above are exact
   D3 BZ quadrature M=800: e/V = -1.00241976, -1.19380112; A/V = 0.666263, 0.631237; g_c = -5.4639
PASS D3 [numerical, converged quadrature] the closed forms P_ij = <cos q_1>_occ and P_ij = +-(h(0) + h(2e_1))/2 with h = (6 + W)^(-1/2) give the limiting A/V above: one crossing, attractive
   D4 4^3 MBPT2 dE(g) = -10.50142 -2.00000 g +0.44685 g^2, roots -3.1015 and 7.5773
PASS D4 [numerical, caution only] the MBPT2 truncation above has a positive root g = 7.58 predicting a repulsive flip; REFUTED by the exact cube (A3, A4) and the 2x2x3 block (C2)
   E1 cube N=4, g: m^2 then Neel weight, (+,-) each, against 1/4 and 1 -- 4: 0.2181 0.1999 0.8347 0.7504 | 8: 0.2414 0.2396 0.9545 0.9458 | 16: 0.2478 0.2477 0.9884 0.9878 | 32: 0.2495 0.2494 0.9971 0.9970
PASS E1 [numerical, 1e-9] both sectors freeze into the SAME Neel doublet (above): <n_i> = 1/2 on every cube site in both to 5e-14, m^2 and the Neel weight rising together, here and on 2x2x3
   E2 cube, g: g E_0 (+,-) then g^2 dE -- 64: -5.9995 -6.0061 -0.4216 | 128: -5.9999 -6.0015 -0.2109 | 256: -6.0000 -6.0004 -0.1055
PASS E2 [numerical, converged in 1/g] the t^2/V exchange is sector-INDEPENDENT (above): g E_0 -> -6 in both sectors, g^2 (E_0(-) - E_0(+)) -> 0
   E3 cube g^3 dE: 64:-26.9815477888 128:-26.9953982475 256:-26.9988502688 512:-26.9997126114; exponents 2.99926 2.99982 2.99995; Richardson limit -26.9999999999
PASS E3 [numerical, mpmath 60 digits] the surviving difference is order t^4/V^3 (above): E_0(-) - E_0(+) = -27 t^4/V^3 on the cube -- a ring exchange of 9/4 a face carrying the sign S_f
   E4 2x2x3 g^3 dE: 16:-12.12629 32:-11.92143 64:-11.86931 128:-11.85622 256:-11.85294
PASS E4 [numerical, converged in 1/g] the same ring exchange on 2x2x3 with its own coefficient (above), near -11.8529 ~ -320/27: that number is cluster data, its SIGN is what is shared
SUMMARY: with this interaction present the staggered sector stays the unique many-body ground sector at half filling on both exhaustive clusters at every repulsive coupling tested, the last difference to survive being a ring exchange that prefers the minus sign.
TOTAL: PASS=18 FAIL=0

----- stderr -----

<!-- END ORIGINAL logs/runner-cache/record_conserving_interaction_keeps_the_staggered_sector_check_2026_09_03.txt -->
