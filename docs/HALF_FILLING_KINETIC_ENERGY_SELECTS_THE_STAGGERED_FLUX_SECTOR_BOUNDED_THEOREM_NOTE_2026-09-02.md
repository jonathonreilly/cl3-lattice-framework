---
claim_id: half_filling_kinetic_energy_selects_the_staggered_flux_sector_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "Conditional finite signed-hopping comparisons: exact uniform cube ladders, exact half-filled cube uniqueness and 4-cubed global Cauchy-Schwarz certificate; explicitly numerical finite ladders, eight-twist enumerations, searches, Riemann-integral estimates and L=96 interpolation. Abstract odd-N Fock comparisons are outside the even-parity edge carrier; no physical sector selection is derived."
upstream_dependencies: [minimal_axioms_2026-06-29]
runner: scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py
---

# Finite half-filled signed-hopping energy comparisons

**Date:** 2026-09-02; source correction 2026-09-08.
**Type:** bounded_theorem
**Status:** bounded mathematical source proposal; formal audit deferred and no audit grade assigned here.
**Primary runner:** [half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py](../scripts/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.py)
**Runner cache:** [half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt](../logs/runner-cache/half_filling_kinetic_energy_selects_the_staggered_flux_sector_check_2026_09_02.txt)
**Correction and original evidence:** [dated record](../.claude/science/review-fixes/flux-selection-7874-7878-20260908/REVIEW_CORRECTION.md). It preserves both original notes and both historical caches verbatim. The current cache must bind this final note, current governing memo and declared attribution context before use.

## Declared objects, domains, and authority

These are conditional finite matrix comparisons. The coarse graph, Hamiltonian, hopping scale, filling, and choice of a lowest-energy state are supplied mathematical inputs. An energy ordering neither moves a conserved flux sector nor derives a formation rule, physical clock, Born law, occupation-to-record dictionary, or a mechanism choosing that ground state. Hopping conserves total occupation, but does not commute with every local occupation operator. Permanent readable records are not identified with movable occupation labels here.

The [current governing memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the framework boundary only. No axiom is amended or inferred to select this model. The current composition discriminator, `COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md`, is attribution context: it declares a hopping-plus-density subfamily, not a complete global law. A locally allowed number term sums to `sum_i degree(i)n_i` and need not be constant on an irregular open graph. With nonzero hopping on a bipartite graph a sign gauge and positive rescaling give `t=1`, `g=V/abs(t)`; the diagonal limit `t=0` is excluded from that normalization. All needed matrices are defined here; no parent campaign is imported. The old face-transport and Dirac-gate quotations are preserved in the correction history as quotations, not as premises establishing a physical kinetic law.

The abstract calculation uses ordered spinless Jordan-Wigner Fock modes on the coarse vertices, with ordinary tensor composition. The auxiliary edge encoding has qubits on coarse edges, stars `B_i=prod_(e incident i) Z_e`, and signed Pauli edge operators in direction order `-x,-y,-z,+x,+y,+z`. For the edge i→j, start with X on that edge and multiply Z on edges ordered before it at each endpoint; write the Hermitian Pauli as `i^(x dot z mod 2)X^xZ^z`, with an additional minus for a negative-axis orientation. Thus `A_ij=-A_ji`. With `Q=i^k X^x Z^z`, multiplication includes `(-1)^(z dot x')`. The loop operator is `S_C=i^len(C) prod A` in cyclic order. Face and, on a torus, noncontractible loop eigenvalues determine a link-sign gauge class by spanning-tree recovery, exactly as constructed in the runner.

Every edge occurs twice in `prod_i B_i`, so this product is identity: identifying `B_i=1-2n_i` restricts this carrier to **even total occupation**. On the cube, one fixed loop sector has `2^(12-5)=128` states, matching the even subspace of the 256-state eight-mode Fock space. Odd-N Fock comparisons below remain valid abstract matrix comparisons; they are not encoded states of this edge carrier. A legal hopping loop can be considered with another spectator occupation when even parity is needed. No unpaired single-particle code state is asserted.

For connected graphs, a local sign gauge `G=diag(g_i)` sends `M` to `GMG`; fields with identical complete cycle holonomies are related this way. This is diagonal gauge conjugacy, not merely a site permutation. On an even cubic torus the face data leave three independent Wilson signs, hence eight gauge classes. Each class contains `2^(V-1)` raw sign fields. The eight representatives alone are not all raw fields.

The coarse coordinate is `v` at fine position `2v`. Define `eta_1=1`, `eta_2(v)=(-1)^v_1`, `eta_3(v)=(-1)^(v_1+v_2)` and the plain field `eta=1`. Their face holonomies are minus and plus, respectively. Link strength is normalized to one. `M_ij=eta_ij` on bonds and zero otherwise; `H(g)=-sum eta_ij(c_i^dag c_j+c_j^dag c_i)+g sum n_i n_j` in the ordered fixed-N occupation basis. For the free case `g=0`, bipartition conjugates `M` to `-M`, so `E_N` is the sum of either one-particle ladder's N lowest levels; `E_0(g)` denotes the lowest many-body eigenvalue at fixed N. In filling expressions V is the vertex count; the V in the traditional interaction notation g=V/abs(t) is the separately supplied density coupling. The supplied half-filled determinant, and the interacting lowest eigenspace where used, are state selectors for the calculation.

Lieb's background article, [The Flux-Phase of the Half-Filled Band](https://arxiv.org/abs/cond-mat/9410025), *Physical Review Letters* **73** (1994), 2158–2161, DOI `10.1103/PhysRevLett.73.2158`, discusses interactions and higher-dimensional periodic settings including cubic flux. Its hypotheses are not verified or used to certify these particular spinless finite calculations. The former blanket planar/free/no-cubic description is withdrawn.

## Theorem 1 -- the exhaustive 2x2x2 cube

**Conclusion.** On the open `2x2x2` coarse cube, 8 sites, 12 links, 6 faces with one `F2` relation:

1. Exactly `32` of the `64` face assignments are consistent flux sectors -- those with an even number of `-1` faces -- and enumerating all `2^12` link-sign fields
   gives exactly those `32` holonomy patterns, with the one-particle spectrum constant on each pattern.
2. `E_N` of the all-`(+1)` sector is `0, -3, -4, -5, -6, -5, -4, -3, 0` and of the all-`(-1)` sector is `-N sqrt3` for `N <= 4` with its mirror, both exact.
3. At half filling `N = 4` the all-`(-1)` sector is the **unique** minimiser of all `32`, by `0.456067` to the next distinct value and by `4 sqrt3 - 6` to the plain
   sector. The plain sector alone minimises at `N = 1, 7`; **three** sectors in the two-flux class tie at `N = 2, 6`, and **twelve** in the four-flux class tie at `N = 3, 5`; all `32` tie at `N = 0`
   and `N = 8`.

**Proof.** At half filling the cube has `tr M^2=24` and paired eigenvalues. Cauchy-Schwarz gives `E_4 >= -4sqrt3`, with equality iff `M^2=3I`. The two length-two paths across every face diagonal cancel precisely when that face holonomy is minus. Thus the all-minus gauge class is the unique equality class. The nonzero margin to the next class remains a numerical comparison. Item 1 solves the `F2` relations among the six face generators, realises each consistent assignment as a sign field and checks its holonomy face by face,
then enumerates the `4096` sign fields directly, `[numerical, 1e-12]` for the constancy of the spectrum within a pattern and exact for the pattern count. Item 2
diagonalises the two exact integer `8x8` matrices in `sympy` and sums the surds. Item 3 compares the `32` floating-point ladders entry by entry with the actual `1e-9` tie rule, with the tie counts
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
   one-particle spectrum as the KS field, so this is a spectral check consistent with the diagonal gauge equivalence proved above; it does not by itself prove a physical identification.

On the odd `3^3` open block no integer half filling exists: the table evaluates `floor(V/2)=13` with its `14`-particle mirror, and `floor(V/4)=6` with mirror `21`. The separate `floor(3V/4)=20` entry is not the mirror of 6. Odd-N entries are abstract Fock comparisons.

**Proof.** Item 2 evaluates the claimed minimal polynomial at the exact integer matrix, which vanishes over `Z`, and checks `tr M^k` for `k = 1..8` against the
claimed multiset, which fixes the multiplicities; the ladders and their difference are then exact sums of surds. Item 1 is `[numerical, 1e-9]` away from `L = 4`,
with `E_N = E_{V-N}` from the symmetry of a bipartite spectrum; item 3 likewise, and the `8^3` torus is evaluated from the Bloch formula, not a matrix.

**Reading, not theorem.** The same picture holds on every block tested. Below about a third filling the plain arrangement is cheaper, above about two thirds it
is cheaper again, and in the whole band between the two the minus-on-every-square arrangement is. The band is a single stretch, symmetric about half filling.

## Theorem 3 -- the Wilson-line caveat

**Conclusion.** The face stabilizers fix none of the three torus Wilson lines, so each fixed face assignment leaves eight Wilson-sign gauge classes, each containing `2^(V-1)` raw fields, related by twists that change no
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
   `15.26`: its spectrum `+-sqrt(6 + 2 sum_a cos q_a)` is not flat on those tori. Global minimality is a theorem on `4^3`; elsewhere only the stated finite searches are available.

**Proof.** The general identities in item 1 follow analytically because each edge contributes two squared unit entries and joins opposite colours; the 52 exact field checks are witnesses of that argument. Item 3 is a zero-tolerance matrix certificate for the named field. Item
2 applies Cauchy-Schwarz to the `V/2` numbers `|lambda|`, whose sum of squares item 1 pins. Item 4 evaluates the bound and the exact Bloch energies, `[1e-9]`.

**Reading, not theorem.** Two facts about the box fix a floor no arrangement of signs can go below: every site has six neighbours, so the levels have a fixed total
spread, and the box is two-colourable, so they come in plus-minus pairs. Spreading a fixed total spread over a fixed number of levels is cheapest when every level
has the same size. On the smallest box the minus-on-every-square field, run the right way around the box, does exactly that: every level is the same size. So it is
not merely better than everything tried -- it is as good as anything could be.

## Theorem 5 -- the searches

**Conclusion.** At half filling on the tori `4^3` and `4x4x6`, all `[numerical, 1e-9]` and all **search results, not theorems**:

1. `2000` random link-sign fields per torus, each realising a consistent sector as drawn, and a `500`-field subsample with each field minimised over its own eight
   twists: `0` of `2500` evaluations (`2000` draws plus `500` reevaluations of a subset, not `2500` distinct draws) beats the all-`(-1)` sector on either torus.
2. The structured sectors with flux only on the `xy`, `xz` or `yz` plaquettes, `xy` flux on alternating `x` planes, and flux on the `xz` and `yz` plaquettes
   together are consistent and all strictly above the all-`(-1)` sector. Flux on the even-parity faces, `xz+yz` on alternating planes, and a single-face flip off
   the all-`(-1)` sector are **inconsistent**: every face lies in two cube relations, so no sector differs from another in one face alone.
3. Greedy single-link descent from `24` random restarts per torus never beats the all-`(-1)` field at its optimal twist. On `4^3` its best energy equals that field's energy within the stated numerical tolerance, `3` of `24` restarts reaching that energy. On `4x4x6` its best stays above, at `-116.134` against `-116.809`.
4. That field is a strict local minimum: every one of the `192` and `288` single-link flips raises `E_{V/2}`, by at least `0.426844` and `0.365352`.

**Proof.** Direct evaluation of `E_{V/2}` for each field, with the consistency of a structured assignment decided by the `F2` relations among the `S_f` before any
diagonalisation. The negative statements are statements about the samples drawn and the descent runs made, at the seeds the runner fixes, and are not claims about
the whole space.

**Reading, not theorem.** Two thousand random arrangements, five patterned ones, and a descent free to change any single link: nothing beats the
minus-on-every-square arrangement, and on the smallest box the descent walks straight back to it. Away from that box this is evidence, not proof.

## Theorem 6 -- Bloch integrals and a finite-grid crossing diagnostic

**Conclusion.** From the exact Bloch formulas -- `E = +- sqrt(6 + 2 sum_a cos q_a)` for the all-`(-1)` sector, fourfold, and `2 sum_a cos q_a` for the all-`(+1)`
one -- evaluated at `L = 4, 8, 16, 32, 64, 96` and by the stated finite Brillouin-zone quadrature grids:

1. The limiting half-filling energies are the continuous bounded Bloch integrals, so the uniform Riemann sums converge. The numerical estimates are `e(+) approximately -1.00241973` and `e(-) approximately -1.19380112`, a difference approximately `-0.19138139 |t|` per coarse site in favour of the staggered sector.
2. At quarter filling the difference is `+0.07909` per coarse site at `L = 96`, in favour of the plain sector.
3. The **L=96 linearly interpolated finite-grid** crossing is approximately `0.339659`. The discrete first-negative occupations `N*/V` are the sequence `0.3594, 0.3287, 0.3340, 0.3380, 0.3411, 0.3398, 0.3394, 0.3397, 0.3396, 0.3397` at
   `L = 4, 6, 8, 12, 16, 24, 32, 48, 64, 96`. The interpolated L=96 mirror is approximately `0.660341`. Neither these digits nor a unique limiting crossing are certified.

**Proof.** Item 1 has an analytic Riemann-integral existence argument and a separate `[numerical]` estimate: the reduced-grid Brillouin-zone integrals at `M = 600, 1200, 2400` agree to `1e-8` in `e(-)` and settle
to the digits quoted in `e(+)`. Item 2 is a finite-grid numerical value. In item 3, let `d_j=E_j(-)-E_j(+)` and let `j` be the first index below the stated `-1e-9` search threshold. The displayed interpolation solves `d_(j-1)+(n*L^3-(j-1))(d_j-d_(j-1))=0`. The runner now tests this equation against the actual displayed value. This identity does not give a `1e-9` thermodynamic error bound. Agreement of quadrature grids is not a certified remainder.

**Reading, not theorem.** The finite grids and integral estimates favour the minus field at half filling. They do not establish an exact one-third threshold, uniqueness of a limiting crossing, or a mechanism selecting a physical state.

## Claim and evidence boundary

The six original groups A–F and their 19 check IDs remain. Exactness applies to the stated bit/integer/surd identities and the analytic inequalities, not to every eigenvalue comparison. The named finite twist enumeration is complete for its eight representatives; random searches and descent retain their original protocols and are not exhaustive. No new lattice size or random sample is added. Ground-energy minimization and actual dynamical sector selection remain distinct. The quoted larger-framework kinetic and face-transport claims remain historical context only.

The runner additionally checks the actual edge-parity identity, diagonal gauge recovery, and the finite interpolation equation. It binds its own publication note, the current governing memo and the current composition note used only for attribution. Both dependency consumers must derive the primary from this real filename, with zero local helpers. A fresh cache with zero failures supports precisely these source-bound checks; an independent source review and later formal audit remain separate tasks.
