---
claim_id: the_spin_half_link_ring_is_gapped_and_confining_the_photon_question_needs_three_dimensions_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite supplied spin-1/2 link model: exact Gauss censuses and winding sectors for even L=4..20, entry-by-entry constrained-chain equality for L=4..16, finite positive gaps and full-basis glide/first-level checks, L=20 correlators and nearly linear finite-distance potential, exact finite winding split -E0(L), named tube/torus spectra, and nonnegative imaginary-time weights for beta>=0. The background is supplied, not forced. All fitted numbers are finite-window diagnostics; no thermodynamic gap, confinement, order, physical photon or coarse-stiffness obstruction is proved. Pauling counting is heuristic. Off-diagonal observables require an additional readout protocol; the fixed Z-record statistics are insufficient."
upstream_dependencies: []
runner: scripts/spin_half_link_ring_gapped_electric_string_check_2026_09_03.py
---

# Finite spin-1/2 link-ring spectra, winding energies and conditional fit diagnostics

**Original checkpoint identifier (historical only):** `spin_half_link_ring_gapped_confining_photon_needs_3d`

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; formal claim audit is deferred
**Status:** conditional support for the supplied finite model; no physical phase or audit grade
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/spin_half_link_ring_gapped_electric_string_check_2026_09_03.py`](../scripts/spin_half_link_ring_gapped_electric_string_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/spin_half_link_ring_gapped_electric_string_check_2026_09_03.txt`](../logs/runner-cache/spin_half_link_ring_gapped_electric_string_check_2026_09_03.txt)
**Parents:** none load-bearing. Every premise used below is declared in this note; the context notes are plain-text pointers listed in "Imports and authority".

PR #7893 coupled the emergent fermion's `U(1)` to one designed spin-1/2 link role per edge and closed with an explicit open item on its own face: *no gapless transverse
mode of the link sector is shown, computed, or suggested.* This note computes a finite ladder sector while leaving the three-dimensional question open. The supplied geometry is a ring of `L` plaquettes, one plaquette high. At each even L=4..20 the computed ground level is unique and separated; the L=20 charge-pair energies grow nearly linearly across the sampled distances. An exact finite structural relation is also computed: the Gauss sector of this ring *is* a constrained chain at zero detuning, entry by entry. The geometry
also states its own limit. A ring one plaquette high has no transverse direction, so what is priced here is the electric excitation gap, not the photon.

**Current correction (2026-09-08):** this live note supersedes the interpretation of the
[original note](../.claude/science/review-fixes/pure-link-20260908/history/7911/THE_SPIN_HALF_LINK_RING_IS_GAPPED_AND_CONFINING_THE_PHOTON_QUESTION_NEEDS_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-03.md) and [original cache](../logs/runner-cache/spin_half_link_ring_gapped_electric_string_check_2026_09_03.original-pure-link-20260908.txt); both remain byte-exact historical evidence.
The [dated correction overlay](../.claude/science/review-fixes/pure-link-20260908/CURRENT_CORRECTION.md) records all dispositions. The canonical cache above is produced by an actual final run after this note and its runner are frozen; its status and output are evidence, not an audit grade. Historical cache wording and totals do not certify the corrected source.

## Machine status

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional finite supplied spin-1/2 link model: exact Gauss censuses and winding sectors for even L=4..20, entry-by-entry constrained-chain equality for L=4..16, finite positive gaps and full-basis glide/first-level checks, L=20 correlators and nearly linear finite-distance potential, exact finite winding split -E0(L), named tube/torus spectra, and nonnegative imaginary-time weights for beta>=0. The background is supplied, not forced. All fitted numbers are finite-window diagnostics; no thermodynamic gap, confinement, order, physical photon or coarse-stiffness obstruction is proved. Pauling counting is heuristic. Off-diagonal observables require an additional readout protocol; the fixed Z-record statistics are insufficient."
trace_class: upstream_support
target_claim_id: the_spin_half_link_ring_is_gapped_and_confining_the_photon_question_needs_three_dimensions_bounded_theorem_note_2026-09-03
target_blocker_text: "Thermodynamic, physical-readout and coarse-stiffness implications are unestablished; finite fits do not prove their infinite-size extrapolations."
source_of_blocker_text: current_note_proof_boundary
reachability_to_target: conditional_on_supplied_model
artifact_role: theorem
next_trace_action: "Independent source review of this corrected conditional finite unit; keep the named provenance, readout and limit questions open. Formal claim audit is deferred."
conditional_surface_status: supplied_model_only
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the four statements below, exactly the runner's check groups `A`-`E`. Groups `A`, `B`, `D1` and `E5` are exact -- integer and bit
arithmetic on explicit Gauss-sector bases, with no floating-point step anywhere -- and the items tagged `[numerical]` are floating-point cross-checks at the stated
tolerance.

1. `T1` (`A`, `B`). The Gauss sector, the declared background convention, the census `Lucas(L) + 2`, the winding decomposition, and the entry-by-entry identification
   of the dynamical block with a zero-detuning constrained chain.
2. `T2` (`C`). The gap: its value, its momentum structure, its finite-window exponential-fit diagnostic, and fitted decay lengths.
3. `T3` (`D`). The winding splitting and the nearly linear L=20 static two-charge potential.
4. `T4` (`E`). Three dimensions: the tube, the torus, the heuristic size estimate for the `4^3` sector, and the sign structure.

## Imports and authority

Imported scientific authority: none load-bearing. The quantum-link (gauge-magnet) presentation with finite-dimensional link algebras, the ring-exchange plaquette term,
the Pauling ice estimate, the Lucas numbers, and the constrained-chain model named `PXP` in the literature are standard methodology; **every object is redeclared here
and every statement is recomputed by the runner**, the `PXP` identification included -- that identification is a computed matrix equality in group `B`, and the name is
a plain-text pointer carrying no authority and no expectation. No observational value, no fitted number and no framework premise enters any proof. Non-load-bearing
pointers, no grade and no dependency weight:

- `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7893): the link algebra
  `E_e = Z^L_e/2`, `U_e = (X^L_e + i Y^L_e)/2`, `G_v = (div E)_v - rho_v`, `P_f = W_f + W_f^dag`, the coordination-parity condition, and `E_e^2 = I/4`. Its open item
  -- no gapless transverse mode shown, computed, or suggested -- is the question taken up here.
- `NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md` (`origin/main`): "No pair of bounded operators `(a, a†)` in the local algebra `A_x ≅ M_2(C) = End(C^2)`
  satisfies the canonical commutation relation `[a, a†] = I_2`", by `tr([a, a†]) = 0` against `tr(I_2) = 2`. This excludes that single-site CCR only; collective or effective carriers are not excluded. The link qubit below is a supplied design.
- `COMPACT_U1_QUADRATIC_BASIN_SOURCE_FREE_MAXWELL_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7884): the sister lane's Maxwell germ, which supplies
  *compact continuous* `U(1)` link variables. That is a different carrier from the one here, and the corollary below prices the difference.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms, quoted in "Setting" and nowhere used as a premise.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." The lattice is physical. **Qubit**: "Each site has a domain of local possibilities", whose "full one-site
possibility domain has algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions." **Record**: "Records form", "a record locks exactly one admissible local possibility", "records are permanent", "Only records are
readable", and "A readout value is determined by record content alone."

**Why the carrier is a link qubit.** The Qubit axiom gives each site the algebra `M_2(C)`, and the pointer note above shows by the trace identity that no pair
`(a, a†)` inside `M_2(C)` satisfies `[a, a†] = I_2`. A site-local bosonic oscillator is therefore not available in this algebra, and the `U(1)` carrier PR #7893
declares instead is a **designed role**: one further two-state site per edge, assigned by design and derived from no axiom, exactly as PR #7834's superlattice role
pattern is. `E_e = Z^L_e/2` is a one-record value on that site, so **the flux registers**: it is record content, readable by the Record axiom. `U_e` and `P_f` carry
`X` in every monomial and have no record-diagonal part, so the same fixed Z-record statistics cannot determine their expectations. Additional measurement bases, dynamics or record-formation protocols would have to be supplied; existing permanent records are not rotated or overwritten. Composition is **ordinary** throughout.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the ring geometry, the link role with its
`E_e` and `U_e`, the pure-gauge law `H = -lambda sum_f P_f`, and the background convention. `P1` (`A`) is the Gauss sector, the convention comparison, the census and
the winding decomposition; `P2` (`B`) the constrained-chain identification; `P3` (`C`) the gap and the correlators; `P4` (`D`) the winding splitting and the static
potential; `P5` (`E`) the three-dimensional blocks and the sign structure. `P1` uses `P0` only; `P2`, `P3` and `P4` use `P1`; `P5` uses `P0`. The strongest supported
scope is precisely `P0`-`P5`.

## Definitions

The **ring** is the height-1 cylinder ladder: vertices `t_i, b_i` for `i = 0..L-1` on two rings, `L` even; links `T_i : t_i -> t_{i+1}`, `B_i : b_i -> b_{i+1}` (the
rails) and `R_i : b_i -> t_i` (the rungs), `3L` in all; `z_v = 3` at every one of the `2L` vertices; and `L` faces `f_i : t_i -> t_{i+1} -> b_{i+1} -> b_i -> t_i`.

```text
E_e = (1/2) Z^L_e   (eigenvalues +-1/2),      U_e = (X^L_e + i Y^L_e)/2 = sigma^+_e
(div E)_v = sum_{e at v} s_{v,e} E_e,         s_{v,e} = +1 out of v, -1 into v
G_v = (div E)_v - rho_v,       rho_v = a STATIC background charge (no matter, so no n_v)
W_{f_i} = U_{T_i} U^dag_{R_{i+1}} U^dag_{B_i} U_{R_i},        P_f = W_f + W_f^dag
H = -lambda sum_f P_f                                          THE DECLARED PURE-GAUGE LAW
Phi_i = E_{T_i} + E_{B_i}                                      THE CUT FLUX
S = T_1 . C   (one column on, and E -> -E)                     THE GLIDE SYMMETRY
2 rho(t_i) = (-1)^i,   2 rho(b_i) = -(-1)^i                    THE DECLARED BACKGROUND
```

`lambda` is **supplied** and set to `1`; every energy below is in units of `lambda`. The electric term `(g^2/2) sum_e E_e^2` is dropped because PR #7893 T3(6) shows
`E_e^2 = I/4` identically, so at spin `1/2` it is a c-number and supplies no dynamics. `T_1` alone is not a symmetry -- the declared background alternates -- and the
charge conjugation `C` undoes that alternation, so the glide `S` with `S^L = 1` is what resolves momentum.

**The background convention, declared.** With no matter there is no `n_v`, so `rho_v` is a static background and two necessary conditions constrain it. PR #7893's coordination-parity
condition: `2 (div E)_v` sums `z_v` terms `+-1` and so carries the parity of `z_v`, here odd, so `2 rho_v` must be odd. Graph neutrality: `sum_v (div E)_v = 0`
identically on a closed graph, so `sum_v rho_v = 0`. Together these forbid a uniform half-charge but do not force a staggered sign. At L=4 both the columnar background and the neutral nonalternating top signs `[1,1,-1,-1]` with opposite bottom signs satisfy these conditions: direct 12-bit enumeration gives 4 and 8 states, respectively, versus 9 for the declared staggered choice. The runner checks these alternatives against independent vertex incidences. **This departs from PR #7893's convention
labels and the departure is stated, not buried:** PR #7893 says spin-1/2 links admit `rho^{sea} = n_v - 1/2` at odd `z_v`, but read at `n_v = 0` that is the uniform
`rho = -1/2`, which fails neutrality and gives an **empty** sector on this graph (group `A2`). The parity condition is confirmed and used; the label does not transfer
to the matter-free case, so the background above is declared here.

## Theorem 1 -- the Gauss sector is a constrained chain

**Conclusion.** (1) `dim(Gauss) = Lucas(L) + 2` exactly at `L = 4..20`: `9, 20, 49, 125, 324, 845, 2209, 5780, 15129`, every listed state re-verified against `G_v = 0`
at all `2L` vertices independently of the builder. (2) The cut flux `Phi_i` takes **one** value at all `L` cuts of any sector state, so `Phi in {-1, 0, +1}` labels
three winding sectors, with `dim(Phi = 0) = Lucas(L)` and `dim(Phi = +-1) = 1`. (3) Of the three admissible-looking backgrounds, the declared staggered one is
dynamical; the columnar one (`2 rho = +1` on the whole top ring, `-1` on the whole bottom) is parity-admissible and neutral but gives `dim = 4` with `H = 0`
identically at every `L`; and the uniform `rho = -1/2` fails neutrality and gives `dim = 0`. (4) **The identification.** Under the explicit bijection
`x_i = (1 + e_{T_i})/2`, `z_i = 1 - x_i` for `i` even and `z_i = x_i` for `i` odd, the `Phi = 0` Gauss basis is carried one-to-one onto the configurations of the
`L`-ring with no two adjacent `1`s, and the two matrices are **equal entry by entry** -- not merely isospectral --
`-lambda sum_f P_f = -lambda sum_i P_{i-1} X_i P_{i+1}` on `L` sites with periodic boundaries, at `L = 4..16`; full spectra agree to `7.6e-14`.

**Proof.** Item 1 builds the sector by an explicit column transfer over the two Gauss relations `e_{T_i} - e_{T_{i-1}} - e_{R_i} = 2 rho(t_i)` and
`e_{B_i} - e_{B_{i-1}} + e_{R_i} = 2 rho(b_i)`, then re-derives `G_v` from the listed bit patterns and compares to zero. Item 2 sums the two relations at column `i`,
giving `Phi_i - Phi_{i-1} = 2 rho(t_i) + 2 rho(b_i) = 0`, and counts. Item 3 repeats item 1 under the other two backgrounds. Item 4 computes the image of the basis
under the stated map, compares it as a set to the independent sets of the ring, permutes the matrix by that bijection, and subtracts. All exact integer arithmetic.

**Reading, not theorem.** The rule at a vertex leaves the ring one binary choice per column, with one pattern locked out -- two neighbouring columns cannot both take
it. That is the whole content of the sector, and it is why the count is a Lucas number. The name this constrained chain carries in the literature is `PXP`; here it is
a computed matrix equality, and the name is offered as a pointer to where else the same object appears, not as an authority for anything claimed.

## Theorem 2 -- the gap

**Conclusion.** `[numerical]` (1) `[H, S] = 0` with `S^L = 1`; at every `L = 4..20` the computed ground state is **unique and at `k = 0`**, and the first excitation is separated from the next computed level and is a single
zone-boundary level at `k = pi`. (2) `Delta_1(L) = 1.0352762, 0.9845253, 0.9726558, 0.9694746, 0.9685697, 0.9683035, 0.9682236, 0.9681992, 0.9681917`. (3) `L Delta_1`
is `13.556, 15.492, 17.428, 19.364` at `L = 14, 16, 18, 20` -- nearly linear over these four sizes, its increment constant to `3.9e-4`, a finite-window comparison to `1/L`;
and `d ln Delta_1 / dL = -1.86e-5` on `L = 14..20`, flat to five digits in this window. Neither comparison excludes a later crossover. (4) A finite-window exponential fit to the successive differences gives:
`Delta_1(L) - Delta_1(L-2)` falls by a settled factor `3.244` per two columns, `ln` of it linear in `L` with slope `-0.5945`, i.e. `xi_gap = 1.682` columns, and
Richardson gives the estimate `Delta_1(infinity) = 0.9681883 lambda`, with no certified extrapolation error or infinite-size theorem. (5) At L=20, `<P_f> = 0.6035607` uniform over the `L` faces to `4.4e-15`, the sum rule `E_0 = -lambda L <P_f>` closing
to `3.7e-14`, and `E_0/L = -0.6035607 lambda`. (6) The connected face correlator alternates in sign with `xi_P = 1.597` columns and the connected rung-flux correlator
with `xi_E = 1.518` columns, both fitted on `d = 4..8` at `L = 20`. (7) `<E_{T_i}> = +-0.3042` and `<E_{R_i}> = +-0.1083` alternate with **period 2 and zero mean**, in
step with the declared background sign; every other Fourier component, the period-4 columnar one included, vanishes to `6.0e-16`.

**Proof.** The `Phi = 0` block is diagonalised densely below `2500` rows and by sparse Lanczos above, from a deterministic starting vector; no random number is drawn
anywhere. The complete basis permutation is independently rebuilt from the coordinate action; bijection, `S^L=I` and the sparse full-matrix commutator are checked at every size. The first excitation also satisfies `w[2]-w[1]>1e-8`. Momenta are the glide eigenvalue `<v|S|v>` of the two lowest levels, `|<v|S|v>| = 1` confirming each is an `S`-eigenvector. The three candidate forms are fitted and compared only on the declared finite windows. Printed rounded values are distinct from the internal comparison tolerances; no general eigensolver error bound is inferred from agreement with a reference row. Correlators are ground-state expectations of the explicit `P_f` and `E_e` operators; the Fourier statement is the discrete
transform of the one-link profiles. `[numerical, 1e-8]` for item 1, `1e-9` for items 2 and 5, `1e-6` for item 3, `1e-3` for items 4 and 6, `1e-12` for item 7.

**Reading, not theorem.** The positive gaps vary little across the largest sampled rings. This supports a finite fit, not a proof of a nonzero infinite-size gap. The ground level and first excitation have the stated momenta and separation; no claim is made that the entire spectrum is nondegenerate. The period-2 flux profile follows the supplied background on these rings.

## Theorem 3 -- the winding sectors and the string

**Conclusion.** (1) The `Phi = +-1` sectors are one-dimensional and carry no flippable face, so `H = 0` there **exactly** at every `L = 4..20`, and they therefore lie
`-E_0(L)` above the `Phi = 0` ground state exactly. Its density is L-dependent: `-E_0(4)/4=0.612372435696`, whereas `-E_0(20)/20=0.6035607` (rounded). Writing `0.60356 lambda L` uses the L=20 density and is not an identity at every L. (2) `[numerical]` With a static pair
inserted by reversing the declared background half-charge at `t_0` and `t_d` -- which preserves neutrality, the parity condition and `|2 rho| = 1`, `d` odd -- the
potential at `L = 20` is `V(d) = 0.317041, 1.524151, 2.731236, 3.938250, 5.145046` at `d = 1, 3, 5, 7, 9`. (3) It is **nearly linear on these five distances**, with nonzero residual and fitted `1/d` coefficient:
the four successive slopes `0.603555, 0.603543, 0.603507, 0.603398` agree to `1.6e-4`, the linear fit `V = sigma d + c` gives `sigma = 0.6035055` at residual `1.2e-4`,
and a Coulomb term added to that fit returns `-0.0004`. (4) `sigma` **approximately matches the L=20 vacuum face energy density**, but is not equal to it: `0.603505` against `|E_0|/L = 0.603561`, agreeing to
`5.5e-5`.

**Proof.** Item 1 selects each winding sector by `Phi` and counts its nonzeros: a one-dimensional block with no off-diagonal element is `H = 0`, and its energy relative
to the `Phi = 0` ground state is `-E_0` by definition. Item 2 rebuilds the Gauss sector under the reversed background at each `d` and takes its lowest level minus the
vacuum. Items 3 and 4 are the successive-slope comparison, the two fits, and the comparison to `-E_0/L` of Theorem 2. `[numerical, 1e-7]` for item 2 and `1e-3`,
`1e-4` for items 3 and 4.

**Reading, not theorem.** On this L=20 supplied-background problem the charge-pair energy grows nearly linearly over d=1,3,5,7,9. Neither exact linearity, equality of slope and vacuum density, nor asymptotic confinement follows from these five numbers.

## Theorem 4 -- three dimensions, priced not decided

**Conclusion.** `[numerical]` (1) On the `2x2xL` tube, open in `x` and `y` and periodic in `z`, `z_v = 4` is even, so `rho = 0` is parity-admissible and neutral and no
background charge is needed: `dim(Gauss) = 114, 548, 2970, 16892, 98466` at `L = 2..6`, with `8L` links and `5L` faces. (2) There `Delta_1 = 1.1260, 1.1034, 0.5834,
0.9025, 0.4623`, **oscillating with the parity of `L`** -- a finite parity-dependent pattern in the `2x2` cross-section, only two odd-length points and three even-length points. **No fit is claimed and no
three-dimensional scaling is read off.** (3) On the fully periodic `2x2x2` torus (`z_v = 6`, `24` links, `24` faces, each neighbour pair carrying two links at
period 2), `dim(Gauss) = 9600`, `E_0 = -9.026720914` and `Delta_1 = 1.627609934`; at linear size `2` every direction admits only `k = 0` and `k = pi`, so no dispersion
is resolvable there and none is read off. (4) At `z = 6` the Gauss sector obeys a 3-in/3-out ice rule, whose Pauling estimate `2.5^N` gives `1526` at `N = 8` against
the exact `9600` -- so the estimate is conservative here -- and `2.9e25` at `N = 4^3 = 64`, against a `2^18 = 262144` budget: about `10^19` times over, with `8^3` at
about `10^63`. (5) **Exact.** In the Gauss basis every off-diagonal element of `-lambda sum_f P_f` equals `-lambda <= 0` and every diagonal element is `0`, on the ring
at `L = 4..20` and on every three-dimensional block computed here.

**Proof.** Each block's Gauss sector is built by a slab sweep that assigns a site's unassigned incident links and enforces `G_v = 0` there, peaking at `134742` partial
states; `H` is assembled sparsely and its lowest levels taken densely below `2500` rows and by Lanczos above. Item 4 is the ice-rule count `binom(6,3)/2^6 = 20/64` per
site against `2^{3N}` links, evaluated at `N = 8` and `N = 64` and compared to the exact `9600`. Item 5 reads the assembled matrices' entries directly.
`[numerical, 1e-7]` for spectral comparisons in items 1 to 3; the counts are integer. Item 4 is arithmetic on a heuristic independent-constraint estimate, not an exact census or rigorous size bound. Item 5 is exact for the assembled matrices; nonnegative exponential weights follow for `lambda>=0` and `beta>=0`. This alone is no efficiency or ergodicity theorem for a sampler.

**Reading, not theorem.** The named finite tube/torus data do not determine a three-dimensional phase. The Pauling values `1526`, `2.9e25` and about `10^63` are heuristic estimates; the exact 2x2x2 census itself disproves a claim that exact diagonalisation is unavailable at every three-dimensional size.

## Corollary -- finite scope and open physical questions

1. At the nine even ring lengths L=4..20 there are positive computed gaps and the declared full-basis symmetry. The Richardson estimate `0.9681883 lambda`, fitted `xi_gap=1.682`, `xi_P=1.597`, `xi_E=1.518`, and L=20 potential slope `0.6035055` retain their finite windows. They do not prove an infinite-size gap, exponential law, correlation length, or confinement phase.
2. The `Phi=0` matrix is entry-by-entry the zero-detuning constrained chain at L=4..16. That equality supplies no unproved infinite-chain phase result.
3. The exact winding split is `-E_0(L)`. The nearly linear charge-pair energies and their small nonzero residual remain finite evidence. The narrow ring does not decide the three-dimensional transverse-mode question.
4. Nonnegative imaginary-time weights for `lambda>=0, beta>=0` are useful, but do not certify practical mixing or a continuum limit. Wider cylinders, exact small tori and controlled sampling remain alternatives.
5. The microscopic identity `E_e^2=I/4` removes that bare one-link energy term only. For example two links have `(E_1+E_2)^2=diag(1,0,0,1)`, although each individual square is `I/4`; cross-link correlations can contribute to coarse electric stiffness. The nonzero winding energy of this same pure law is another warning against inferring that coarse stiffness vanishes. Neither an induced coefficient nor a continuum action is derived here. Matter leaves the microscopic square identity unchanged; larger link spins change that identity, and neither route is computed.
6. A fixed complete Z-record distribution cannot read a plaquette coherence. In the Gauss-legal L=4 basis, `(|1365>+|1394>)/sqrt(2)` and `(|1365>-|1394>)/sqrt(2)` have identical full Z-record probabilities but opposite `P_0` expectations `+1` and `-1`. Extra readout conditions are needed. The single-site CCR trace obstruction also does not exclude collective carriers.
7. The current sister-lane Maxwell-germ note is a conditional classical quadratic-basin comparison, not a quantum photon or readout identification of this finite-link model. Its physical/continuum/measurement bridge remains open.

## Where this note disagrees with its own source computation

The scratch computation this note lands from is reproduced here, and four of its readings are corrected rather than carried:

1. **The background labels.** PR #7893's `rho^{sea}` is admissible at odd `z_v` *with matter*; read at `n_v = 0` it is the uniform `rho = -1/2`, which fails graph
   neutrality and gives an empty sector. The parity condition survives; the label does not transfer, and the background used here is declared, not inherited.
2. **Finite background profile.** The ground state is unique at each sampled even `L <= 20`; this is not a thermodynamic symmetry-breaking test; the period-2 alternation in the
   flux profile is the explicit background, with every other Fourier component at `6.0e-16`.
3. **The winding sectors are not degenerate.** Their exact splitting is `-E_0(L)`, with L-dependent density (the rounded L=20 density is `0.60356 lambda`).
4. **`xi_gap` is `1.68` columns, not `0.33`.** The source fit took `ln |Delta_1(L) - Delta_1(20)|` including `L = 20` itself, where the argument is identically zero
   and a `+1e-16` regulator makes it `ln 1e-16`; that single point drives the slope to `-3.03`. Fitting the successive differences instead gives a settled ratio
   `3.244` per two columns and `xi_gap = 1.682` columns -- the same scale as the correlation lengths of Theorem 2 item 6, a comparison of finite fit parameters rather than a phase theorem.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms. The link role, the pure-gauge law and the background convention are declared objects, and no coefficient is derived:
  `lambda` is supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears.
- No continuum limit is taken, no matter appears, and **no claim is made for or against a gapless transverse mode of the link sector in two or three spatial
  dimensions.** The ring is one plaquette high; the negative here is a negative about that geometry, whose limit is stated in Corollary 3.

## Interfaces named for other lanes, not moved here

- **Three dimensions by sampling.** Theorem 4 item 5 shows the model has no sign problem. A sign-free method on `8^3`-`16^3` with a flux-flux structure factor or
  `<E E>` at small `k` is one possible investigation; convergence, sampling bias, volume and readout limits would still need control. Nothing here runs it.
- **Larger links.** Spin-1 or larger link algebras lift the coordination-parity condition and make `(g^2/2) sum_e E_e^2` non-trivial, which changes the model this note
  computes. Which link size the framework wants is a design question for the lane that owns the role rule.
- **Matter coupling.** PR #7893's coupled law adds the gauge-invariant hop. Everything here is pure gauge; what the hop does to this gap and this string is not computed.
- **The ring-exchange coefficient.** `lambda` is supplied. What fixes it, if anything does, is not addressed.
- **Wider geometries.** A ring two or more plaquettes high has a transverse direction and is the first geometry on which the question of Corollary 3 becomes askable at all. Its Gauss sector is not built here.

## Remaining live routes

1. Sign-free sampling in three dimensions, per Corollary 4.
2. The two-plaquette-high cylinder, and how far exact diagonalisation reaches on it.
3. What the coupled hop does to the gap and the string tension computed here.
4. Larger link algebras, where the electric term is no longer a c-number.

## Executable claim block

```text
setting: height-1 cylinder ring of L plaquettes, L even, 4 <= L <= 20; 3L links, 2L vertices at z_v = 3, L faces; ONE DESIGNED spin-1/2 link role per edge (declared, of PR #7893's kind); no matter; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md and used as no premise
law: E_e = Z^L_e/2, U_e = sigma^+_e, G_v = (div E)_v - rho_v, P_f = W_f + W_f^dag, H = -lambda sum_f P_f with lambda supplied and set to 1; electric term a c-number by E_e^2 = I/4
background: DECLARED, matter-free: 2 rho(t_i) = (-1)^i, 2 rho(b_i) = -(-1)^i; NOT forced: coordination parity and graph neutrality are necessary, and columnar/nonalternating counterexamples remain
conventions_compared: columnar (+1/2 top, -1/2 bottom) admissible and neutral but dim 4 with H = 0 identically; uniform rho = -1/2 not neutral, sector empty
census: dim(Gauss) = Lucas(L) + 2 = 9,20,49,125,324,845,2209,5780,15129 at L = 4..20; every state re-verified against G_v = 0 at all 2L vertices, max |G_v| = 0
winding: Phi_i = E_{T_i} + E_{B_i} equal at all L cuts of any sector state; Phi in {-1,0,+1}; dim(Phi=0) = Lucas(L) = 7,18,47,123,322,843,2207,5778,15127; dim(Phi=+-1) = 1
identification: x_i = (1 + e_{T_i})/2, z_i = 1 - x_i (i even) / x_i (i odd) is a basis bijection onto the L-ring configurations with no two adjacent 1s, and the matrices are EQUAL ENTRY BY ENTRY: -lambda sum_f P_f = -lambda sum_i P_{i-1} X_i P_{i+1}, periodic, max |difference| = 0 at L = 4..16; full spectra agree to 7.6e-14. Called PXP in the literature; that name is a pointer, not authority
gap: [H,S] = 0 for the glide S = T_1.C with S^L = 1; ground state unique at k = 0 and first excitation a single level at k = pi, at every L = 4..20; Delta_1 = 1.0352762,0.9845253,0.9726558,0.9694746,0.9685697,0.9683035,0.9682236,0.9681992,0.9681917
scaling: L*Delta_1 = 13.556,15.492,17.428,19.364 at L = 14..20, nearly linear in this window (increment constant to 3.9e-4), a finite comparison to 1/L; d ln Delta_1/dL = -1.86e-5, a finite comparison to e^{-L}; successive differences fall by a settled factor 3.244 per two columns, ln-slope -0.5945, xi_gap = 1.682 columns; Richardson estimate Delta_1(inf) = 0.9681883 lambda, no certified limit
vacuum: at L=20, <P_f> = 0.6035607 uniform to 4.4e-15; E_0 = -lambda L <P_f> to 3.7e-14; E_0/L = -0.6035607 lambda
correlations: xi_P = 1.597 and xi_E = 1.518 columns on d = 4..8 at L = 20; <E_T> = +-0.3042 and <E_R> = +-0.1083 with period 2 and zero mean in step with the declared background; every other Fourier component, period-4 included, at 6.0e-16
string: Phi = +-1 one-dimensional with H = 0 exactly, lying exactly -E_0(L) above the ground state, with L-dependent density (0.60356 lambda at L=20); V(d) = 0.317041,1.524151,2.731236,3.938250,5.145046 at d = 1,3,5,7,9 (L = 20); successive slopes 0.603555,0.603543,0.603507,0.603398 agree to 1.6e-4; sigma = 0.6035055 at residual 1.2e-4, added Coulomb term -0.0004; sigma differs from |E_0(20)|/20 = 0.603561 by 5.5e-5
three_d: 2x2xL tube (z_v = 4, rho = 0 admissible and neutral, 8L links, 5L faces): dim = 114,548,2970,16892,98466 and Delta_1 = 1.1260,1.1034,0.5834,0.9025,0.4623 at L = 2..6, oscillating with the parity of L -- NO FIT CLAIMED; 2x2x2 torus (z_v = 6, 24 links, 24 faces): dim 9600, E_0 = -9.026720914, Delta_1 = 1.627609934, and only k = 0, pi available so no dispersion resolvable; Pauling 2.5^N gives 1526 at N = 8 against the exact 9600 and 2.9e25 at N = 64 against a 2^18 budget
sign_structure: every off-diagonal element of -lambda sum_f P_f is -lambda <= 0 and every diagonal element 0, on the ring at L = 4..20 and on every 3D block here, so exp(-beta H) has non-negative matrix elements for beta>=0 and lambda>=0; no mixing claim
not_shown: no gapless transverse mode in two or three dimensions is shown, computed, suggested, or excluded; the ring is one plaquette high and has no transverse direction
declared_departures: PR #7893's rho^{sea} label does not transfer to the matter-free case (uniform rho = -1/2 gives an empty sector); the finite flux profile follows the supplied background; no thermodynamic order test is claimed; the winding splitting is exactly -E0(L), not a constant-density identity; xi_gap is 1.682 columns, the source's 0.33 being a fit artefact of including the identically-zero last residual
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: original 24 checks retained with narrowed labels, plus current correction controls; actual result is in the canonical cache, not a prose prediction
```

## Proof boundary

The exact constructions and numerical finite witnesses concern **one named finite geometry** -- the height-1 cylinder ring at `L = 4, 6, ..., 20` -- together with three named finite three-dimensional
blocks: the `2x2xL` tube at `L = 2..6` and the fully periodic `2x2x2` torus. Nothing is claimed for `Z^3`, for a wider cylinder, for any larger region, or for `L > 20`.

The **link role is designed**: one further two-state site per edge, assigned by a design rule and derived from no axiom. The **law is declared**: `H = -lambda sum_f P_f`
with `lambda` supplied. The **background convention is declared** for the matter-free case, and departs from PR #7893's convention labels for the reason set out in
"Setting"; the coordination-parity condition it rests on is PR #7893's and is confirmed here. Nothing in this note is derived from any axiom; the axioms are quoted to
fix what "readable" means and to say why the carrier is a link qubit, and for nothing else.

**The three-dimensional rows are not fits.** `Delta_1` on the `2x2xL` tube oscillates with the parity of `L` over two points per parity class. That is reported as an
oscillation and nothing is extrapolated from it. The `2x2x2` torus is reported for completeness; at linear size `2` no dispersion is resolvable there.

**The geometry's limit, stated.** The ring is one plaquette high and has no transverse direction. A negative result for a gapless transverse mode on it is a negative
about *this geometry*, and it is neither evidence against nor evidence for such a mode in three dimensions. The three-dimensional question is left open, with heuristic size estimates and exact nonnegative-weight conditions distinguished.

**No continuum limit** is taken, and no claim is made that this `U(1)` is electromagnetism.

## Review record

The original finite census, matrices, spectra, correlators, charge-pair energies and fit numbers are preserved. The original 24 check IDs remain; the corrected source additionally checks first-level separation, the full glide permutation and commutator, background nonselection, fixed-record insufficiency and the coarse-square counterexample. All conclusions are conditional on the supplied role, law and background. The original and current receipts have distinct source identities. A fresh successful current cache requires the actual final runner under its unchanged 150-second cap. Independent source acceptance and the coordinator's landing gates are separate from a deferred formal claim audit.
