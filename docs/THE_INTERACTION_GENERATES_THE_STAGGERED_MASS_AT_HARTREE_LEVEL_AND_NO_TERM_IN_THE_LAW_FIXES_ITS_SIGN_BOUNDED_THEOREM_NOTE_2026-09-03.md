---
claim_id: the_interaction_generates_the_staggered_mass_at_hartree_level_and_no_term_in_the_law_fixes_its_sign_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional supplied-Fock and Hartree model: T1 the staggered ansatz gives m=-zVO, finite antiperiodic response and separate bulk Brillouin-zone kernel; T2 the bulk conditional Hartree minimum has an analytically justified logarithmic onset, while all finite-grid samples and one-body length diagnostics retain their finite scope; T3 exact C sectors and Born occupation distributions on the degree3 cube and degree4 slab, with an opposite-parity first excitation at tested V, not a C-conjugate state or critical estimate; T4 an even functional, unsourced sign choice, and analytic fixed-cluster small-field response with limit zero, not spontaneous symmetry breaking or Record formation; T5 the open-slab C obstruction and periodic finite-torus zero modes. All original numerical rows remain diagnostics. The chosen Hamiltonian, ordinary Fock composition, state, ansatz, coefficients, labels and joint Born measurement are supplied; no encoded physical or permanent Record bridge is proved."
upstream_dependencies: [minimal_axioms]
runner: scripts/interaction_generates_staggered_mass_hartree_sign_registered_check_2026_09_03.py
---

# The interaction generates the staggered mass at Hartree level, and no term in the law fixes its sign

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; formal audit is deferred by owner directive until a solid TOE
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/interaction_generates_staggered_mass_hartree_sign_registered_check_2026_09_03.py`](../scripts/interaction_generates_staggered_mass_hartree_sign_registered_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/interaction_generates_staggered_mass_hartree_sign_registered_check_2026_09_03.txt`](../logs/runner-cache/interaction_generates_staggered_mass_hartree_sign_registered_check_2026_09_03.txt)
**Premises:** the conditional mathematical objects are declared below. The [current minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) governs the framework-scope boundary, not the Hamiltonian or readout.

A nearest-neighbour density interaction produces an alternating one-body coefficient under a supplied staggered Hartree ansatz. What does that calculation fix, and what is left to a choice of state or readout? The algebra fixes a self-consistency equation. Its even functional does not select one sign, and the finite interacting clusters do not establish spontaneous symmetry breaking or permanent Records.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional local Hartree algebra and bulk asymptotic proof, plus finite supplied-Fock spectra and joint Born readout. Bulk, finite antiperiodic and two differently coordinated cluster calculations are separate; no physical phase transition, encoding bridge or Record formation is inferred."
trace_class: frontier_discovery
target_claim_id: the_interaction_generates_the_staggered_mass_at_hartree_level_and_no_term_in_the_law_fixes_its_sign_bounded_theorem_note_2026-09-03
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Confirm the corrected conditional source independently; formal audit is deferred until a solid TOE. Physical suppliers and limits remain open."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target and provenance

The five theorem groups and all 23 original check IDs are retained. `T1` gives the conditional mass operator and distinct finite/bulk self-consistency equations. `T2` proves a logarithmic onset only for the explicitly defined bulk Hartree functional. `T3` reports two finite spectra and Born distributions. `T4` separates sign symmetry from selection and corrects the finite small-field limit. `T5` records two actual finite-boundary traps.

Historical source pointers are PR #7890 (mass/response/length), #7878 (density interaction), #7892 (charge conjugation), #7879 (half-filled sea), #7844/#7834 (coarse model). The selected note's original quotations, its raw source and its cache remain provenance in the external original packet; this does not claim that every parent campaign or its caches were copied. No parent campaign, code-space equivalence, status or physical interpretation is accepted by this note. The formulas used here are rederived below or directly constructed by the runner. The current memo linked above is the only off-note premise input; the mathematical model and joint Born measurement remain supplied.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has algebraic
presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations", and "For
each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a record locks
exactly one admissible local possibility", "records are permanent", "Only records are readable."

The framework lattice is physical; the following identification with a chosen Fock model is an additional conditional construction. Everything below reads the Kawamoto-Smit sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, on the superlattice role
pattern's sublattice. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

`P0` supplies the coarse lattice, KS signs, Fock Hamiltonian, half filling, grading, joint Born occupation readout and Hartree ansatz. `P1/T1` derives the local decoupling and finite/bulk response. `P2/T2` uses the separately declared bulk kernel and proves its conditional onset. `P3/T3` is an independent finite-cluster computation; `P4/T4` uses the even functional and finite symmetry. `P5/T5` fixes the finite boundary conditions. None of these arrows supplies a physical time evolution or a permanent Record mechanism.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`. The **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`,
`eta_3(v) = (-1)^{v_1 + v_2}`; every elementary face of both clusters used here carries flux `-1`.

```text
H(t,V) = -t sum_bonds eta_ij (c_i^dag c_j + c_j^dag c_i) + V sum_bonds n_i n_j     THE SUPPLIED FOCK HAMILTONIAN, read at t = 1
eps_v  = (-1)^{v_1+v_2+v_3},   Eps = diag(eps_v),   M = the one-particle KS hopping matrix
H_m    = m sum_v eps_v n_v        the companion note's declared mass term; its m is supplied
O      = (1/N) sum_v eps_v (n_v - 1/2),   N = number of coarse vertices,   so H_m = m N O on every even block
Q      = sum_v (n_v - 1/2)        the total occupation charge; identically 0 in the half-filling sector
c_L(m) = (1/N) sum_k (E_k^2 + m^2)^{-1/2}   finite antiperiodic torus
c_inf(m) = <(6+2 sum_a cos(q_a)+m^2)^(-1/2)>_BZ   separate normalized bulk integral
m*     = -z V O,  z = 6           the SELF-CONSISTENT Hartree coefficient
S      = <O^2>,   chi = -d<O>/dh at h = 1e-4 t, with the field term h sum_v eps_v n_v = h N O
Delta_C = the gap to the lowest state of the opposite C sector
```

`C` is the explicitly constructed unitary charge conjugation, `c_v -> eps_v c_v^dag`, realised here in the one-mode-per-vertex Fock space with Jordan-Wigner signs. `C` is exact on a
cluster exactly when the conjugate interaction `V sum (1-n_i)(1-n_j)` differs from `V sum n_i n_j` by a constant at fixed particle number, which needs **uniform coordination**.
The two clusters that satisfy it are the **cube** `2x2x2` open (`z_i = 3`, 12 bonds, `N = 4` particles, dimension `C(8,4) = 70`) and the **slab** `2x2x4`, open in `x, y` and
**periodic in `z`** (`z_i = 4`, 32 bonds, `N = 8`, dimension `C(16,8) = 12870`).

The **Bravyi-Kitaev superfast encoding is not carried here**. Equality of the single free cube energy `-4 sqrt3=-6.928203` with a historical encoded value is a numerical comparison, not an intertwiner or a proof of a six-edge readout. Occupation probabilities below use an explicitly supplied joint Born measurement on a Fock state; they are not the framework's permanent physical Records.

The density interaction commutes with every `n_i`. Hopping generally does not, so the full Hamiltonian is not a law preserving each fixed occupation record. A Hartree collection of one-site means does not supply the joint law either: with four sites and alternating labels, the equiprobable two-particle configurations `(1100,0011)` and `(1010,0101)` both give means `1/2` but staggered second moments `0` and `1/4`. This is a finite probability counterexample, not an all-axiom independence theorem.

## Theorem 1 -- the supplied Hartree ansatz generates that mass operator

**Conclusion.** (1) With `<n_i> = 1/2 + eps_i O` and uniform `z = 6`, every neighbour of a site lies on the opposite sublattice, so `sum_{j in nn(i)} <n_j> = z(1/2 - eps_i O)` at
residual `0.0e+00`, and the decoupling `n_i n_j -> <n_i> n_j + n_i <n_j> - <n_i><n_j>` gives, exactly,

```text
V sum_<ij> n_i n_j  ->  (zV/2) Nhat  -  z V O sum_i eps_i n_i  +  const,     H_MF = H_0 + m* sum_v eps_v n_v + const,   m* = -z V O.
```

The generated one-body term, less its `eps`-even mean, is `m* eps_v` at residual `0.0e+00`: it is the companion note's `H_m` character for character, not a new operator. The
subtracted constant is `(z N/2)(1/4 - O^2)` exactly, hence even in `O`. (2) The companion note's `T5` response `O(m) = -(m/2) c(m)` is re-verified on the antiperiodic `8^3`
torus at `m = 0.3` and `m = 1.0`, giving `-0.066175285` and `-0.200251524` against the prediction to `5.6e-17`. (3) Substituting it into `m* = -zVO` closes the self-consistency:

```text
SELF-CONSISTENCY: m*[1 - (z V / 2)c(m*)] = 0, z = 6
NONZERO BRANCH: 1 = (z V / 2)c(m*)       V_c^MF = 2/(z c(0))
Use c_L and V_c,L for each finite torus; c_inf and V_c,inf for the bulk functional.
```

(4) The separate bulk kernel `c_inf(m)` has the closed 1-D form `c(m) = (1/sqrt(pi)) int_0^inf ds s^{-1/2} e^{-s m^2} (e^{-2s} I_0(2s))^3`, whose kernel identity `<e^{-s(6 + 2 sum_a cos q_a)}>_BZ = (e^{-2s}
I_0(2s))^3` agrees with a `64^3` midpoint grid to `3.3e-16`. It gives bulk `c_inf(0) = 0.455344052`, so `chi = c(0)/2 = 0.227672` against the companion note's `0.227671`, and

```text
V_c,inf^MF = 2 / (6 * 0.455344052) = 0.732047 t      [BULK HARTREE]
```

The separate finite antiperiodic thresholds are larger in the three sampled cases: `0.747072` at `L = 8`, `0.738124` at `L = 12`, `0.735366` at `L = 16`.

**Proof.** Item 1 is bond-by-bond arithmetic on the `4^3` coarse torus over every site and dyadic `O`, at residual `0.0e+00`; the bipartite structure is what reduces every
neighbour sum to `z(1/2 - eps_i O)`. Item 2 diagonalises `M + m Eps` densely and reads the diagonal of the half-filled projector; item 3 is substitution; item 4 evaluates the
proper-time representation of `(M^2 + m^2)^{-1/2}` and factorises the zone average over the three directions. Item 1 exact; 2 `[numerical, 1e-9]`; 4 `[numerical, 1e-12]`.

**Conditional reading.** The alternating operator is the same one-body matrix one could add by hand. Within the supplied Hartree ansatz its coefficient instead satisfies a self-consistency equation. The zero solution remains an algebraic solution for every `V`; selecting a nonzero minimizing branch uses the bulk functional and positive coupling conditions in Theorem 2.

## Theorem 2 -- a conditional bulk logarithm and finite diagnostics

**Bulk conclusion.** Set `t=1`, `z=6`, `V>0`, and define the normalized zone integral in Definitions independently of a finite grid. The conditional bulk Hartree functional per site is

```text
F_V(m) = -1/2 <sqrt(E(q)^2+m^2)>_BZ + m^2/(2zV) + const,
E(q)^2 = 6+2 sum_a cos(q_a),   V_c=2/(z c_inf(0)).
F'_V(m) = m[1/(zV)-c_inf(m)/2].
```

`c_inf(m)` is continuous, positive and strictly decreasing for `m>0`, tends to zero, and has finite `c_inf(0)`. Therefore `m=0` is the unique minimum for `0<V<=V_c`; for `V>V_c` the two nonzero roots `+-m*` are degenerate minima and zero remains a stationary point. This is a conditional variational statement about this functional, not the finite interacting Hamiltonian or a physical transition.

As `m` tends to zero through positive values,

```text
c_inf(0)-c_inf(m) = [m^2/(4 pi^2)] log(1/m) + O(m^2).
```

Consequently the positive minimum obeys `m*^2 log(1/m*) ~ [4 pi^2 c_inf(0)/V_c](V-V_c)` and `m*` is proportional to `sqrt((V-V_c)/log(1/(V-V_c)))` to leading order. This is the claimed one-half exponent with a logarithm, restricted to the bulk Hartree functional.

**Local proof.** The unique zero of `E(q)^2` on the Brillouin torus is `q=(pi,pi,pi)`. In local coordinates of radius `r`, `E^2=r^2+O(r^4)` and is comparable to `r^2`. Off a fixed ball about the zero the integrand difference is `O(m^2)`. Inside it replace `E^2` by `r^2`. For `f_m(s)=s^(-1/2)-(s+m^2)^(-1/2)`, `|f'_m(s)|` is bounded by a constant times `min(s^(-3/2),m^2 s^(-5/2))`. The `O(r^4)` change in its argument and the radial measure give integrated errors bounded by `O(m^4)` for `r<=m` and `O(m^2)` for `m<r<delta`. The remaining integral is

```text
(1/(2 pi^2)) int_0^delta [r-r^2/sqrt(r^2+m^2)] dr
 = (m^2/(4 pi^2)) log(1/m) + O(m^2).
```

Here the prefactor is `4pi/(2pi)^3`; the antiderivative of the second term is `[r sqrt(r^2+m^2)-m^2 asinh(r/m)]/2`. Subtracting `2/(zV)` from `c_inf(0)=2/(zV_c)` gives the stated onset. A fixed gapped antiperiodic sum instead has an ordinary Taylor expansion in `m^2` and no such leading logarithm. No finite-grid-to-bulk or physical thermodynamic convergence theorem is asserted.

**Original numerical diagnostics retained.** The ratio `(c_inf(0)-c_inf(m))/(m^2 log(1/m))` is `0.0399,0.0444,0.0501` at `m=0.02,0.05,0.1`. These finite values alone did not prove the asymptotic; the local proof does. The eight adjacent finite-difference exponents from nine `V-V_c` values drift `0.5991 -> 0.5378` as the interval moves from `1e-1` toward `1e-5`.

At `V=2,4,6`, `m*/(3V)=0.915,0.979,0.991`, `2m*=10.98,23.50,35.67` exceed the free bandwidth `2sqrt12=6.928`, and the one-body amplitude branch-point length `xi=2/acosh(1+m^2/2)` is `0.58,0.40,0.35` coarse-site units. These are strongly staggered Hartree states approaching the classical checkerboard; at any finite listed coupling they are not the exact occupation-product state. For example at `V=2`, `O=-0.457388`, not `-1/2`.

The illustrative smaller-mass samples `V=0.75,0.8,0.9,1.0` give `m*=0.365,0.802,1.397,1.877` and `xi=5.51,2.56,1.54,1.19`. They define no exclusive Dirac-mass window or phase boundary. The length follows from the one-body complex zero `q=pi+i kappa`, `cosh(kappa)=1+m^2/2`, with two coarse sites per cell. It is not an interacting correlation length. Every original row is retained in the runner; no continuum or critical point is inferred from these diagnostics.

## Theorem 3 -- what the two exact clusters carry

**Conclusion.** On the cube (uniform degree `3`, dimension `70`, exact) and the slab (uniform degree `4`, dimension `12870`, sparse Lanczos in each `C` sector), every
elementary face carrying flux `-1`: (1) `C^2 = I`, `[C, H_0] = 0` and `d(~b) - d(b) = 0` on every basis state, all at `0.0e+00`, and the free cube energy is `-6.928203 = -4
sqrt3`. (2) At every `V` tested the ground state is `C`-even and the **lowest excitation at the tested couplings has opposite C parity**: `gap = Delta_C` to `1.2e-14`, and `Delta_C` falls from
`2 sqrt3 = 3.464102` (cube) and `2 sqrt2 = 2.828427` (slab) at `V = 0` to `7.8163e-02` and `9.5445e-05` at `V = 8 t`. (3) At `V = 0` both clusters give `S = 1/(2N)` exactly and
the odds over `O` are `Binomial(N/2, 1/2)` exactly: the free half-filled sea's staggered fluctuation is shot noise. (4) The odds over `O` go bimodal: the cube at `V = 8 t` holds
`0.472875 + 0.472875` on `O = -1/2` and `O = +1/2` against `0.004317` on `O = 0`, the two staggered patterns carrying `0.945751` of the weight. (5) `chi` is size-flat at `V = 0`, `0.28868 ->
0.27884`, then explodes with size: `6.52 -> 717.3` at `V = 4 t` and `48.64 -> 4920.8` at `V = 8 t` from cube to slab; the `V = 8` slab value is saturation of the finite difference, not a
slope. (6) The `S`-doubling crossover **falls** with size, `2.03411 t -> 1.14065 t`. (7) The two computed curves have a crossing; neither their ordering nor this comparison identifies phases. The crossing is `V_x = 1.76598 t`, against `V_c^MF = 0.732047 t` -- the numerical ratio is `2.41`, not a mean-field error factor.

**Proof.** Both clusters are built over the whole half-filling occupation basis with Jordan-Wigner signs; `C` is a signed permutation of that basis, and item 1 is integer
arithmetic over the whole basis. Item 2 projects `H` into the two `C` sectors and takes the two lowest levels of each. Items 3 to 7 read the ground vector: the odds over `O` are
its weight in each `k`-block, `S` its second moment, the quoted `chi` a central difference at `h = 1e-4 t`, the crossings bisections. Item 1 exact; 3 `[numerical, 1e-12]`; 2, 4-7 `[numerical]`.

**Finite reading.** Cube and slab differ in size, shape, boundary conditions and coordination (`z=3` versus `4`), while the bulk functional uses `z=6`. The crossing `1.76598` and ratio `2.41` are arithmetic comparisons, not critical estimates, error factors or controlled finite-size scaling. A third size alone would not certify an extrapolation. The quoted susceptibilities are finite differences at `h=1e-4`; the slab V=8 value is already saturated and is not the derivative at zero.

## Theorem 4 -- sign symmetry does not supply selection or registration

1. The Hartree functional is even. At `V=2,4,6` on the antiperiodic `8^3` torus the original energy differences are `4.5e-13,0,0`, and `O(+m*)=-O(-m*)`. The finite roots here use `c_L`, separately from the bulk roots of Theorem 2.
2. For the sampled finite-cluster states, `<O>=0` at `h=0` to `1e-9`, while `<O^2>` ranges from `0.1235` to `0.2439`. The ground state is C-even, so `Cg=g`; its first excited state has opposite parity and is orthogonal to `Cg`, not equal to it. At cube `V=8`, the two extreme checkerboards have total weight `0.945751<1`, not an exact two-configuration cat. The runner checks the actual C action, orthogonality and nonzero intermediate weight.
3. The original slab `V=8` values at `h=-0.005,-0.001,+0.001,+0.005` remain `+0.492983,+0.492970,-0.492970,-0.492983`. This is finite-field near-saturation. The isolated finite ground state has gap `9.5445e-5`; for `H(h)=H(0)+hNO`, the perturbation norm is at most `N|h|/2`. Standard finite-matrix perturbation about this isolated eigenvalue makes its projector analytic in a sufficiently small neighbourhood of zero. Since C conjugates `H(h)` to `H(-h)` and makes O odd, its expectation is odd and tends to zero as `h->0`, not to `-1/2`. Actual below-gap fields `1e-7` and `1e-9`, with eigenpair residual checks and the opposite field, discriminate this boundary. No limit exchanging volume and field is taken.
4. `O=(1/N)sum eps_v(n_v-1/2)` is diagonal in a supplied joint occupation measurement, takes five and nine values on the two clusters, and is C-odd entry by entry. `Q` is identically zero in these half-filling sectors. No six-edge code readout has been implemented here, and no physical permanent Record is formed by this calculation.
5. At `V=1,3` on both regular clusters, `CH(t,V)C^-1=H(t,V)` exactly and `CH_mC^-1=-H_m`. This means the Hamiltonian alone distinguishes neither sign. It does not choose a state, a draw, an ansatz branch or a readout context. Those remain supplied. Within the conditional Hartree minimization, a nonzero magnitude is fixed only when its positive-coupling threshold condition holds.

**Proof.** The even functional follows from Theorem 1 and spectral symmetry. The original exact full-basis C identities and numerical finite expectations are retained; the added controls use the actual cube eigenvectors and actual slab matrix at small fields. The analytic fixed-size limit follows from the isolated projector and symmetry as stated. The original large finite-field data were never a proof of a singular limit.

## Theorem 5 -- two traps, recorded

**Conclusion.** (1) The **open** `2x2x4` slab has degrees `3` and `4`. Its `d(~b) - d(b)` is therefore not constant -- it takes `9` values -- and `V` itself breaks `C` on it,
`C H C^-1 - H = 4.0` at `V = 1 t`: no `C`-odd gap is definable there. Periodic `z` restores uniform degree `4`, keeps every face flux at `-1`, and is what Theorem 3 uses. The
result of Theorem 3 is boundary-condition-dependent at this size. (2) The **periodic** `8^3` torus carries `8` exact zero modes -- the companion note's `T3` says so -- so `c(0)`
diverges there and the gap equation returns `V_c^MF = 0`, a pure finite-size artefact. The **antiperiodic** sector, `min|E| = 1.325654` at `L = 8`, is used for the finite one-body response and finite energy comparisons. The bulk integral and its roots are separate, with no antiperiodic grid imposed.

**Proof.** Item 1 counts degrees, sweeps `d(~b) - d(b)` over the whole basis of the open cluster, and evaluates `C H C^-1 - H` directly. Item 2 diagonalises the periodic
one-particle matrix and counts eigenvalues below `1e-10`. Item 1 exact; item 2 `[numerical, 1e-10]`.

**Reading, not theorem.** Two ways of getting this wrong, written down so nobody repeats them. Leave the slab open and the repulsion is no longer blind to the exchange of
matter and its absence, because the corners no longer all have the same number of neighbours, and the quantity being tracked stops existing; put the torus on the periodic grid
and the massless energies include exact zeros, which make the threshold read as zero, an artefact of the grid and not a property of the lattice.

## Corollary -- a conditional mass coefficient with an unresolved physical bridge

Within the supplied staggered Hartree ansatz a density repulsion gives the mass matrix with `m=-zVO`. The bulk functional has the conditional minima and logarithm in Theorem 2; the two finite interacting clusters retain their spectra and Born distributions. The even functional does not select a sign. None of this trades a physical primitive for a registered bit: the Hamiltonian, Fock carrier, label, state/branch and joint readout remain supplied. A physical encoding, dynamical formation mechanism and permanent Record interpretation remain open.

The original finite classical/window, C-conjugate/cat, singular-field and critical-estimate readings have been corrected, not silently dropped. Their raw note, runner, cache and once-executed baseline are preserved as history. Their supported replacements are the finite and conditional claims above.

## Boundaries and remaining routes

Fluctuations, the exchange/Fock channel of the interaction, actual infinite interacting states and a critical point are not computed. No result about fine-lattice locality, time, Record production or many-body correlation length is established. Larger clusters could test finite trends but would need controlled geometry and convergence before an extrapolation. A physical supplier for `V`, a readout protocol and an encoded intertwiner remain unresolved; this is not an independence proof or a completed N1–N8 campaign. No wall quota or new primitive is invented.

## Executable claim block

```text
supplied: coarse Fock carrier, KS signs, t=1, V, eps labels, half-filled state, staggered Hartree ansatz, joint Born occupation measurement
T1: exact m=-zVO; undivided m[1-zVc(m)/2]=0; zero remains stationary; finite c_L and bulk c_inf are distinct
T2: local proof c_inf(0)-c_inf(m)=m^2 log(1/m)/(4pi^2)+O(m^2); conditional bulk minimizing branch only; original finite rows retained
T3: cube70 and slab12870; tested lowest excitation has opposite C parity, not Cg; bimodality/finite differences/two-shape crossing are finite diagnostics
T4: even functional; Cg=g; nonzero intermediate occupation weight; fixed-cluster h->0 gives zero; actual joint Born readout, no physical permanent Records
T5: open-slab nonuniform coordination breaks C; periodic8^3 has8zero modes; finite antiperiodic tests separate from bulk integral
checks: all23 original IDs and numerical expressions retained; additional discriminating controls; actual final totals and complete data in cache
```

## Proof boundary and review record

The mathematical closure is local: explicitly supplied objects, the finite matrices in the runner, and the short bulk integral argument above. The current minimal memo fixes scope quotations only. Historical parent pointers are neither proof authorities nor an accepted physical bridge. In particular no six-edge code/Fock equivalence is inferred from a shared energy constant, and no off-note runtime helper is used.

The 2026-09-08 correction preserves the original 23 check IDs and all numerical protocols, with separate bounded controls for the repaired distinctions. The note and current memo are actual declared, hash-checked inputs. The genuinely refreshed cache records final source/input identity, actual exit status and full stdout under the original 120-second cap. Original results and all adverse evidence remain preserved in the external packets. Formal audit is deferred until a solid TOE; this author correction does not grant acceptance.
