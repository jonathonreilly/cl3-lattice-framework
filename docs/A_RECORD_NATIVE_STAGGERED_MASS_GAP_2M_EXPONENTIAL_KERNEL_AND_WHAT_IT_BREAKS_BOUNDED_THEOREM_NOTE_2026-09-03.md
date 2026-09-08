---
claim_id: a_record_native_staggered_mass_gap_2m_exponential_kernel_and_what_it_breaks_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
historical_claim_id_alias: record_native_staggered_mass_gap_2m
claim_scope: "Supplied finite coarse KS/Pauli model with real mass m and optional Slater/Born occupation readout. T1: diagonal corner-parity form/constants and exact finite commutants; [Hm,T]=m(eps_j-eps_i)TBj, ad(Hm)^2T=4m^2T and oriented eigenoperators, not a real nonzero commutator eigenvalue for Hermitian T. T2: stated finite even/odd translations and24 rotations. T3: squaring identity and balanced-bipartite SVD sign pairing; node gap2|m| or finite gap2sqrt((gap0/2)^2+m^2), with all original spectra preserved. T4: chirality-odd flavor-singlet mass; two Dirac flavors, fourfold spin/flavor bands, flavor mixing not splitting. T5: finite sea/projector densities and declared quadrature comparisons. T6: finite kernel validation and mass={.2,.5,1} fits compared with branch-point xi; no all-m or infinite-distance/image bound. T7: only KS versus plain, five masses on4^3/6^3 with8twists each and six masses on200^3 quadrature; fourth moments do not prove universal ordering. T8: mass-sign conjugation and complementary fixed-label densities, not fixed-readout equivalence without relabeling. All28 original check IDs/numerical data are retained; physical encoding/Record/time formation and historical parent campaigns remain unproved."
upstream_dependencies: []
runner: scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py
---

# A supplied staggered mass: node gap `2|m|`, finite kernel fits, and its symmetry

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; formal audit is deferred by the owner until a solid TOE.
**Status:** bounded - bounded or caveated result note
**Status authority:** current conditional source awaiting independent correction confirmation; no applied audit grade or axiom change.
**Primary runner:**
[`scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py`](../scripts/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.txt`](../logs/runner-cache/a_record_native_staggered_mass_gap_2m_exponential_kernel_check_2026_09_03.txt)
**Proof setting:** the finite constructions and conditional readout below are supplied here. The linked current memo and historical gate are scoped context, not a physical derivation or acceptance of the gate campaign.

This note supplies a coarse-lattice KS hopping matrix, an abstract Pauli encoding and an alternating mass term. It tests their finite algebra and one-particle consequences. Diagonal corner parity is an available code observable; no physical permanent Record instrument, role-pattern formation or clock is derived. The mass coefficient and the filled sea are supplied.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional finite Pauli and balanced one-particle identities plus explicitly scoped numerical spectra, densities, two-sector comparisons and kernel fits; no physical Record or global minimization claim."
trace_class: frontier_discovery
target_claim_id: a_record_native_staggered_mass_gap_2m_exponential_kernel_and_what_it_breaks_bounded_theorem_note_2026-09-03
target_blocker_text: "Physical role/formation/readout/time bridge and all unproved limits remain outside this conditional unit."
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Original-session confirmation of the exact corrected source and composed manifest; owner manages landing. Formal audit remains deferred until a solid TOE."
conditional_surface_status: "supplied-model finite results; no physical bridge or parent-campaign acceptance"
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the eight statements below, exactly the runner's check groups `A`-`H`. Groups `A`, `B`, `G1` and `H1` are exact -- `F2` support and `Z4` phase
arithmetic on Pauli monomials, exhaustive sweeps, and zero-residual integer identities -- and the items tagged `[numerical]` are floating-point cross-checks at the stated
tolerance. The two decay lengths of `T6` are fits, labelled as such wherever they appear.

1. `T1` (`A`). The supplied code-parity form, locality, commutants and exact hop/double-commutator identities.
2. `T2` (`B`). What the term keeps and what it costs: the surviving translations and the full rotation group.
3. `T3` (`C`). The spectrum theorem `(M + m Eps)^2 = M^2 + m^2`, balanced SVD sign pairing, and node gap `2|m|`.
4. `T4` (`D`). The classification: chirality-odd and taste-singlet.
5. `T5` (`E`). The massive sea, its densities, its condensate and its finite-torus gaps.
6. `T6` (`F`). Finite kernel samples and fits, compared with the branch-point scale `2/arccosh(1 + m^2/2)`.
7. `T7` (`G`). KS versus plain at the listed finite masses/twists/quadrature; no universal minimization inference.
8. `T8` (`H`). Conjugation exchanges `+m` and `-m`.

## Imports and authority

The mathematical model is supplied, not derived from the framework. No whole parent campaign is accepted. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the Dirac-Kahler spin-taste basis and the Ornstein-Zernike
form of a massive correlation function are standard methodology; every object is redeclared here and the runner checks the finite statements and controls at the explicitly stated coverage; it does not prove continuum limits or physical interpretation. No observational value is imported; numerical fits remain finite evidence rather than proofs of limits. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): the cell algebra, the intertwiner `U`, and `epsilon = Z_1
  Z_2 Z_3` with its image `I (x) (+- T B_1 B_2 B_3)`. Pointer only; the encoding, the cell and the intertwiner are redeclared below.
- `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7874): the sector selection at `m = 0`.
- `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7879): the half-filled sea, `eps M
  eps = -M`, and `<n_v> = 1/2` at every site.
- `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the superlattice role pattern and the coarse
  sublattice `2Z^3`.
- [Historical kinetic gate](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md): the kinetic-form clause quoted below.
- [Current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): the four framework axioms quoted in "Setting". No grade of theirs is cited and no hypothesis is adopted.

**On the mass term in the landed gate note.** `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` declares no mass term for the staggered operator and fixes no mass
coefficient. Its only uses of the word are exclusions: "**SM phenomenology.** Nothing here derives generation masses, Yukawa couplings, mixing angles, or any PDG number", and
"not a phenomenology claim (no masses, no mixing, no PDG numbers)". The term here is a **declared** addition to the locally supplied model, with supplied coefficient. Neither that historical gate campaign nor a framework derivation of this model is accepted here.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations,
and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has algebraic presentation
`M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations", and "For each site, the
probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a record locks exactly one
admissible local possibility", "records are permanent", "Only records are readable."

The historical gate text is quoted below with line wrapping normalized; its forcing claim is not proved or adopted here:

> **Kinetic-form clause.** Within the declared kinetic class (the naive-Dirac kinetic form on nearest-neighbor `Z^3` links, made
> compatible with the matter-statistics clause by site-local spin diagonalization), the kinetic operator is the staggered operator
> `D = (1/2) Σ_{x,μ} η_μ(x) (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})` with the Kawamoto-Smit phases `η_1 = 1, η_2(x) = (−1)^{x_1},
> η_3(x) = (−1)^{x_1+x_2}`, unique as a local Z2 gauge class.

Everything below supplies that sign field on `2Z^3`, an edge-qubit Pauli algebra and a one-particle hopping matrix. The physical role pattern is not imported. Ordinary qubit composition does not alone establish an encoded CAR representation, a constrained code/readout equivalence or permanent Records. The BKS-named operators are explicitly defined and their stated Pauli identities checked; broader encoding/formation claims remain outside this unit. Occupation probabilities below additionally supply a Slater state and Born occupation readout; they are not a consequence of the current Record axiom.

The runner's Hermitian hopping has unit coefficient. The quoted antihermitian `D` has coefficient `1/2`; on a compatible periodic torus a site phase gives `G(-iD)G^dag=M/2`. Mass and time units are supplied, and no physical scale follows. All other listed parent claims are historical, unverified and unaccepted here; only local redeclarations and the exact quoted contextual text are used.

For the optional occupation interpretation, let `V` have orthonormal occupied columns and set `P=VV^dag`. Supply the Slater/Born law `Pr(S)=|det V_S|^2` on subsets of size `rank(P)`. Cauchy-Binet gives its generating polynomial `sum_S Pr(S) prod_{i in S} z_i = det(V^dag diag(z) V)`. Differentiating at all `z_i=1` gives `E[n_i]=P_ii` and, for `i != j`, `E[n_i n_j]=P_ii P_jj-|P_ij|^2`; repeated indices use `n_i^2=n_i`. This proves the conditional identities without deriving that joint law from a one-site marginal or the Record axiom.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the KS sign field on it, the
superfast encoding, the encoded hop, the face stabilizers, the grading `eps_v`, and the mass term `H_m` with its supplied coefficient. `P1` (`A`) is the supplied code-parity form and
the hop commutator; `P2` (`B`) the symmetry content; `P3` (`C`) the squaring identity and the spectra; `P4` (`D`) the taste classification; `P5` (`E`) the massive sea; `P6` (`F`)
the kernel decay; `P7` (`G`) the sector comparison; `P8` (`H`) the conjugation. `P3` uses `{M, Eps} = 0` and balanced bipartite block SVD for sign multiplicities, `P5` and `P6` use `P3`, and `P7` and `P8` use `P3` and the
bipartite structure. The strongest supported scope is precisely `P0`-`P8`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **KS sign** of
the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`; the **plain sign** is `+1` on every bond. The **encoding** is the
Bravyi-Kitaev superfast encoding on the coarse lattice, code qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`.

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_i  = product of the Z's on the six edges incident to i,   S_f = the ordered product of the four A's around a coarse face f
n_v  = (1 - B_v)/2                     the occupation of coarse vertex v; B_v = -1 marks the excitation
T_ij = (i/2) A_ij (B_i - B_j)          the encoded hop across (i, j)
eps_v = (-1)^{v_1+v_2+v_3},  Eps = diag(eps_v),  M = the one-particle KS hopping matrix on the coarse torus
H_m  = m sum_v eps_v n_v               THE DECLARED MASS TERM; m is supplied and is fixed by nothing quoted here
c(m) = [(M^2 + m^2)^{-1/2}]_vv,   C(m) = (1/V) sum_v eps_v <n_v>      the coefficient and the condensate
```

A **flux sector** is a choice of eigenvalue `+-1` for every `S_f` consistent with the `F2` relations among them; the **staggered sector** is the all-`(-1)` one and the **plain
sector** the all-`(+1)` one. A finite torus carries a **twist** `tw in {0,1}^3`, `tw_a = 1` negating the links crossing the `a`-boundary; the **energy-minimising twist**
minimises `E_{V/2} = -(1/2) tr sqrt(M^2 + m^2)`, and `gap_0` is the massless gap of a torus at that twist.

## Theorem 1 -- code corner parity and the correct hop commutator

**Conclusion.** (1) `H_m = -(m/2) sum_v eps_v B_v + (m/2)(sum_v eps_v) I` exactly, the constant being `0` on every even torus and `+m/2` on the open `3x3x3` coarse block. (2)
Every term is a pure `Z`-product on the six coarse-edge sites at one corner: `H_m` is diagonal in the code-qubit Z basis and star-local, the open block's boundary stars having supports
`3` to `6` and its interior star `6`. (3) `H_m` commutes with every face stabilizer -- all `972` term-face pairs of the open `3x3x3`, all `12288` of the torus `4^3` -- with every
`B_w` (`729` and `4096` pairs) and with all three non-contractible Wilson lines of the `4^3` torus. (4) On all `192` bonds of the `4^3` torus `[H_m, T_ij] = m (eps_j - eps_i)
T_ij B_j` exactly, nonzero for `m != 0` on these bonds. `T_ij B_i = -T_ij B_j` does not make the Hermitian hop an eigenoperator with real nonzero commutator eigenvalue. Instead `ad(H_m)^2 T_ij = 4m^2 T_ij`, and the oriented operators `T_ij(I+b B_j)/2`, `b=+-1`, have eigenvalue `m(eps_j-eps_i)b`. The original nonzero anticommutator at `m=1` is retained; `m=0` is separately checked.

**Proof.** Item 1 substitutes `n_v = (1 - B_v)/2` term by term. Items 2 and 3 are `F2` support arithmetic: a `Z`-product commutes with a monomial exactly when their symplectic
form vanishes, and each corner star meets every face and every Wilson line evenly. Item 4 expands both sides as Pauli monomials with `Z4` phases and compares key by key. All
exact. Since `H_m` commutes with `B_j` and `B_j^2=I`, commuting once more yields `m^2(eps_j-eps_i)^2 T=4m^2T`; right projection onto `B_j=b` gives the oriented result. The actual Pauli source directly tests the double commutator at `m=1`, the oriented identity at `m=-1/2,0,1`, and rejects both putative real eigenvalues for Hermitian `T` at `m=1`.

**Instrument boundary.** The six-edge parity commutes with the face stabilizers, but an individual edge `Z` can anticommute with a face (the runner supplies an actual witness). A diagonal code observable is therefore not a proof that all its individual edge outcomes are readable permanent Records or that their measurement preserves the constrained space. Such an instrument is extra data. The algebraic hop changes the staggered occupation energy by the oriented `+-2m`.

## Theorem 2 -- what the term keeps and what it costs

**Conclusion.** On the `4^3` coarse torus: (1) all `32` coarse translations of even coordinate sum leave `H_m` invariant, forming an index-`2` sublattice generated by the `e_a +
e_b`, strictly larger than `2Z^3`; (2) all `32` of odd coordinate sum send `H_m -> -H_m`, equivalently `Eps -> -Eps` and `m -> -m`; (3) all `24` proper cubic rotations about a
coarse corner leave `H_m` invariant.

**Proof.** Each coarse-vertex map sending edges to edges induces a permutation of the code qubits, and the induced action on a diagonal `Z`-product is the corresponding
permutation of its support. A translation by `d` multiplies every `eps_v` by `(-1)^{sum d}`; a signed coordinate permutation preserves `v_1 + v_2 + v_3 mod 2` while permuting the
six edges at each corner. Exact, by exhaustion over the `64` translations and the `24` rotations.

**Reading, not theorem.** The kinetic term alone does not care which colour is which: shift everything by one corner and, after a relabelling of signs, it is the same operator.
The price does care, because the shift interchanges the two colours; the one symmetry it costs is the freedom to move by an odd number of corners, and even that returns as the statement
that shifting reverses the sign of the price.

## Theorem 3 -- balanced spectrum and node gap `2|m|`

**Conclusion.** (1) `{M, Eps} = 0` as a zero-residual identity on `4^3`, `6^3` and `8^3`, periodic and antiperiodic. (2) Hence `(M + m Eps)^2 = M^2 + m^2`, and the spectrum is
exactly the pairs `+-sqrt(E_0^2 + m^2)`, half positive and half negative, at `m = 0.25, 0.5, 1, 2`. (3) `E(q)^2 = 6 + 2 sum_a cos q_a + m^2` with `q_a = 2pi(2n_a+1)/L`, each
eigenvalue fourfold, on `L = 4, 6, 8` antiperiodic at `m = 0` and `0.7`. (4) `M^2 = 6 I` exactly on the antiperiodic `4^3`, so the whole massive spectrum there is the flat pair
`+-sqrt(6 + m^2)`, `32`-fold each. (5) The periodic `8^3` carries the Dirac point `q = (pi, pi, pi)` on its momentum grid, with `8` exact zero modes, and the mass gaps it to
exactly `2|m|` (the original positive-mass checks are retained).

**Proof.** Item 1 is `eps_v eps_w = -1` on every bond of a bipartite graph, an integer identity at residual `0.0e+00`. Item 2 follows because the cross terms `M Eps + Eps M`
cancel and `Eps^2 = I`. Squaring fixes absolute values, not sign multiplicities by itself. On the even tori the two sublattices have equal size: order them so `M=[[0,A],[A^dag,0]]` and `Eps=diag(I,-I)`. An SVD `A=U S V^dag` reduces `H(m)` to independent `[[m,s_j],[s_j,-m]]` blocks. Each has eigenvalues `+-sqrt(s_j^2+m^2)`; zero singular values contribute the paired `+-m` (zero at `m=0`). Thus signs pair on this balanced domain. An unbalanced open graph can have unmatched `+m` or `-m` modes, and the open block in Theorem 1 is not part of this half-sign claim. The actual intertwiner is `Eps H(m) Eps=-H(-m)`, not `-H(m)`. Items 3 to 5 evaluate the block result at allowed momenta. The added control checks signed spectra at `m=-.7,0,.7`, the correct intertwiner and an unbalanced three-site counterexample. Original numerical checks retain tolerances `[1e-11]`, `[1e-13]`, `[1e-12]`, `[1e-11]`.

A grid containing the massless node has gap `2|m|`; a grid with positive massless gap has `2sqrt((gap_0/2)^2+m^2)`. No half-positive count is asserted at a zero eigenvalue.

**Reading, not theorem.** In this balanced model the squared mass and singular values add. The node gap and finite-grid gap are different cases of the same formula, with no implication of fixed-mass chiral symmetry.

## Theorem 4 -- chirality-odd and taste-singlet

**Conclusion.** In the cell basis `spin (x) chirality (x) flavor` fixed by the intertwiner of the spin-taste split: (1) `U Eps U^dag = -+ I_spin (x) Y_A (x) I_B` on both sign
branches, the identity on the flavour factor; (2) `Eps` anticommutes with all three kinetic Dirac generators `gamma_a = sigma_a (x) Z_A (x) I_B`, a chirality-odd Dirac mass and
not a chemical potential; (3) `Eps` commutes with all three flavour generators `F_b = I (x) I (x) sigma_b`, a taste singlet; (4) the `gamma_a` commute with the `F_b`, while only
the `O(p^2)` kinetic artefacts `W_a = I (x) X_A (x) sigma_a` fail to; (5) `Eps` anticommutes with the `W_a` too, hence with all six Clifford generators -- which is `(M + m Eps)^2
= M^2 + m^2` read inside one cell.

**Proof.** The intertwiner is built by Clifford averaging over the `64` words of the cell algebra, normalised, and applied to `Eps`; every statement is then a matrix identity in
`8` dimensions, all at residual `0.0e+00` except the artefact-flavour commutator, which is `2.0` and so is not zero. `[numerical, 1e-12]` throughout. The historical `gamma_5 (x) xi_5` label for an antihermitian convention is retained only as unverified naming context. The result proved here is precisely the displayed matrix classification in the Hermitian model, without an imported equivalence theorem.

**Reading, not theorem.** The eight states factor as spin `2` times chirality `2` times flavor `2`: two Dirac flavors/tastes. Each positive or negative band is fourfold from spin times flavor. The `W_a` mix a chosen flavor basis but do not split these energies, because the complete Bloch square including mass is scalar. The runner checks that square and the fourfold bands at an off-node momentum; no kinetic energy taste splitting is inferred.

## Theorem 5 -- the massive sea and its condensate

**Conclusion.** (1) `<n_v> = 1/2 - (m/2) eps_v c(m)` with `c(m) = [(M^2 + m^2)^{-1/2}]_vv`, on `4^3`, `6^3` and `8^3` at `m = 0.1` to `2`, because `M f(M^2)` has zero diagonal on
a bipartite graph; hence `C(m) = -m c(m)/2`. (2) On the antiperiodic `4^3`, in closed form, `<n_v> = 1/2 -+ m/(2 sqrt(6 + m^2))` uniform on each sublattice and `C(m) = -m/(2
sqrt(6 + m^2))`. (3) `C(0) = 0`; the finite quadrature estimate for the slope magnitude is `chi = c(0)/2 = 0.227671` against `0.227506` at `m = 0.05`; the large-mass numerical comparison is `-1/2 + 3/(2
m^2)`, reaching `-0.499850` at `m = 100`. (4) The finite-torus gap is exactly `2 sqrt((gap_0/2)^2 + m^2)`, with `gap_0 = 2.651309` the massless gap of the `8^3` torus at its
energy-minimising twist. The runner prints the table at `m = 0, 0.1, 0.25, 0.5, 1, 2, 4`.

**Proof.** Item 1 is the projector `P = (I - H (H^2)^{-1/2})/2` with `H^2 = M^2 + m^2`, whose `M`-part has zero diagonal because odd powers of a bipartite adjacency matrix do
(`1.2e-15`). Item 2 substitutes `M^2 = 6 I`; items 3 and 4 use `200^3` Bloch quadrature and the finite-torus levels. `[numerical, 1e-12]`, `[numerical]` and `[numerical, 1e-11]`.

**Reading, not theorem.** With no price the two colours of corner are equally occupied, one half each. Turn the price on and the sea tilts: the cheap colour fills, the dear
colour empties, by an amount proportional to the price at first and then more slowly, until at a very large price one colour is full and the other empty. The tilt is the
condensate.

## Theorem 6 -- finite kernel samples and exponential fits

**Conclusion.** Along the axis `(n,0,0)`, the massless noncontact same-sublattice term vanishes; contact is `P_vv=1/2`. The odd branch has finite log-log slope `-3.0228` over `41 <= n <= 119`. On the fixed `192^2 x 2048` quadrature the mass values `.2,.5,1` give far-window fitted lengths respectively `10.038/10.117`, `4.053/4.086`, `2.095/2.117`, within2 percent of the branch-point comparisons `10.0166`, `4.0410`, `2.0781`. The fitted power exponents span `1.56` to `1.95`. Original near/far windows and every numerical value are retained.

The original validation is precisely128 selected entries of one periodic `8^3` source column and7 antiperiodic axis magnitudes at `m=.5`, with original residuals `1.7e-16` and `1.0e-16`. The correction additionally computes all8 cell components and checks all512 periodic complex entries and all512 antiperiodic magnitudes of that source column, including off-axis/contact/zero components. This is a complete declared-column comparison, not all entries of the matrix.

**Method and boundary.** Inverting the Bloch column by FFT gives the stated finite quadrature. Fits use `A exp(-r/xi) r^{-b}` in the original log least-squares windows. The analytic branch point satisfies `cosh kappa=1+m^2/2`; the corresponding comparison scale is `xi=2/kappa`, with small-positive-m expansion `xi approximately 2/m`. This identifies a branch-point scale, not a proved lattice asymptotic with a remainder bound. No rigorous bound on quadrature error, periodic images, all-positive-m decay or the fitted power is supplied. Exponential decay is not exact disappearance at finite range.

**Readout boundary.** These are projector amplitudes. Under an additionally supplied Slater/Born occupation law, distinct-site connected covariance is `-|P_uv|^2`: an amplitude comparison `exp(-r/xi)` corresponds to covariance length `xi/2` and a massless amplitude `r^-3` to covariance `r^-6`. No law of permanent Record correlations follows.

## Theorem 7 -- finite KS-versus-plain comparisons

**Conclusion.** Both supplied one-particle matrices are balanced bipartite, so the half-filled sea energy is `-(1/2)tr sqrt(M^2+m^2)`. Among only these two uniform sectors, each minimized over its8 twists, KS is lower at every tested mass `{0,.5,1,2,4}` on `4^3` and `6^3`; the smallest per-site margin is `0.023607`. The separate finite `200^3` quadrature gives KS-minus-plain differences `-0.191380,-0.164354,-0.126890,-0.070552,-0.004698,-0.000023847` at `{0,.5,1,2,8,50}`. The printed `-3/m^3` column is a numerical large-mass comparison, not a proved uniform asymptotic. Moments retain `<E_0^2>=6` in both cases and `<E_0^4>=42` versus`90`.

**Proof/evidence.** The energy formula follows from balanced block SVD, not from an all-sector minimization theorem. The tori enumerate exactly8 boundary twists per sector. The quadrature and moments use the stated200-point midpoint grid on each axis. No arbitrary flux patterns are enumerated, no all-mass ordering is proved and no thermodynamic error bound is provided.

**Failed inference and preserved alternative.** Concavity plus equal first and ordered second moments does not order `E sqrt(X+m^2)`. At `m=1/4`, take `X_A={0,2}` with weights`1/2,1/2` and `X_B={1/2,5}` with weights`8/9,1/9`. Both means are1; their second moments are2 and3, but `E sqrt(X_A+m^2)=(1+sqrt33)/8 <11/12=E sqrt(X_B+m^2)`. The runner tests these actual distributions. This rejects the original variance argument while leaving the displayed KS/plain comparisons intact. Ordering at other masses, other sectors and in a controlled limit remains open.

## Theorem 8 -- conjugation exchanges `+m` and `-m`

**Conclusion.** `eps (M + m Eps) eps = -(M - m Eps)` as a zero-residual identity, so `P -> eps (I - P) eps` carries the mass-`m` sea exactly onto the mass-`(-m)` sea, to
`1.4e-15` on the `8^3` torus at `m = 0.25, 0.5, 1`, with identical spectra, `<n_v>(-m) = 1 - <n_v>(m)` and `C(-m) = -C(m)`.

**Proof.** Conjugation by the diagonal grading negates `M` and fixes `Eps`, so it sends `M + m Eps` to `-(M - m Eps)`; the sea projector of a negated operator is the complement
of the sea projector, and conjugation carries the complement across. Exact for the operator identity, `[numerical, 1e-11]` for the projectors.

**Fixed labels versus relabeling.** At fixed labeled sites and readout, the opposite masses are distinguishable: their means complement, and the actual4^3 antiperiodic `m=.7` control has a difference greater than`.25` despite equal spectra. Calling the sign a convention is legitimate only if the sublattice naming and observable/state identification are transformed simultaneously. No unconditional "nothing measurable" claim remains.

## Corollary -- conditional consequences of the supplied term

1. The term is a diagonal corner-parity observable in the declared edge-qubit algebra. Physical readable Records, encoding realization and formation are additional unresolved interfaces.
2. Balanced spectra follow SVD sign pairs; a node has gap`2|m|`, while finite nonzero massless gaps follow Theorem5. Two flavors give fourfold bands; no kinetic taste energy splitting is inferred.
3. The named kernel fits and KS/plain finite comparisons are preserved at their specified parameters. No all-sector, all-mass, infinite-distance or finite-range disappearance theorem is asserted.
4. The listed odd coarse shifts reverse the term, and even shifts/proper rotations preserve it. Other theories and symmetry completions remain outside this conditional model.
5. Magnitude and sign of`m` are supplied. Fixed-label mass signs give different occupation means; transformed labels/readouts can identify them as stated in Theorem8.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No applied science/audit status is set. Current source metadata and explicit contextual citations are corrected; owner integration generates the manifest.
- Nothing here is derived from the axioms; the coarse lattice, the encoding, the sign field and the mass term are declared objects, and no coefficient is derived: `m` is
  supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears.
- No interaction term is added, no second species appears, and no corner of the taste cube is identified with any named species.

## Interfaces named for other lanes, not moved here

- **The value and the sign of `m`.** Supplied. Nothing quoted here fixes either, and the gate note declares no mass term at all. What would fix them is a question for the lane
  that owns the dynamical clause.
- **Interactions.** Only free hopping plus one declared diagonal term is treated; a four-fermion term could shift the sector comparison of Theorem 7, and is not touched.
- **The chiral sector.** Absent. The mass here is taste-singlet on a vector-like pair, so no chiral projection is defined and none is claimed.
- **The fine-lattice pattern.** Everything is on the coarse lattice. How the alternating sign reads on the fine lattice `Z^3`, and whether it is a function of the superlattice
  role pattern, is not shown here.

## Remaining live routes

1. Larger blocks and other geometries. The open `3x3x3` block and the tori `4^3`, `6^3`, `8^3` are what is proved; nothing is claimed beyond them.
2. The many-body statements. Theorems 1 and 2 are many-body and exact; Theorems 3 to 8 are one-particle and free, and their many-body probabilistic interpretation requires the supplied Slater/Born state/readout. Physical Record formation is untouched.
3. The decay lengths at larger `m`. The fits stop at `m = 1`, where the branch-point comparison is about two coarse sites. Larger masses and controlled limits are not checked.
4. Other staggered mass terms. Only `eps_v` is examined; the remaining entries of the staggered mass classification are not.

## Executable claim block

```text
setting: supplied coarse KS/Pauli construction, unit hopping, real mass m, optional Slater/Born occupation law
T1: exact corner parity/constants and972/12288 term-face,729/4096 term-B pairs,3lines;192bond commutators; ad^2 T=4m^2T and oriented T(I+bBj)/2; m=0 separate
T2:32even and32odd translations,24rotations
T3: balanced SVD sign pairing; all original4^3/6^3/8^3 spectra; node2|m| versus finite-gap formula
T4: spin2 x chirality2 x flavor2; mass flavor singlet, artifact mixing, fourfold bands
T5: conditional projector densities/condensate; original quadrature tables and chi/saturation comparisons retained
T6: finite massless slope-3.0228; m=.2,.5,1 fits and branch-point comparison; original selected entries plus complete512-entry columns, no full matrix/limit claim
T7: KS versus plain only;5finite masses and8twists per4^3/6^3 sector;6masses on200^3; moments6/6,42/90 do not prove ordering
T8: mass-sign conjugation with complementary fixed-label means; simultaneous readout/state relabeling needed for equivalence
original_evidence: PASS=28 FAIL=0 is historical; corrected totals appear only in the genuinely fresh source/input-bound cache
```

## Proof boundary

Exact algebra applies on its declared finite Pauli or balanced bipartite domain; numerical evidence is limited to the named open`3^3`, tori`4^3,6^3,8^3` and fixed quadratures/windows. The open Pauli block is not an extension of equal positive/negative one-particle multiplicities to unbalanced graphs. No physical field theory, fine-lattice role pattern or parent campaign is accepted.

The coefficient is supplied in unit hopping/time conventions. The mass is chirality-odd and flavor singlet in the explicitly rebuilt basis; classification names for other antihermitian operators are historical context, not a separate equivalence theorem. Fits are finite descriptors, not exact decay theorems or image bounds. Other mass terms, nonuniform flux sectors, interactions, zero-mode fillings, instruments and physical completions remain alternatives; this packet supplies no global no-go or independent-wall count.

A Slater/Born occupation law is a conditional interpretation of the projector. Diagonal code parity alone does not provide a permanent Record instrument, nor does it prove full BKS/Fock equivalence on every sector. Actual single-edge/face anticommutation is retained as the boundary witness. Fixed-label mass signs are distinguishable even though their spectra agree.

## Review record

The 2026-09-08 correction preserves all28 original check IDs, finite grids, masses, fit windows and numerical targets. The hop predicate is strengthened; new actual controls cover oriented hops, balanced spectra, flavor degeneracy, full declared kernel columns, the invalid moment inference and fixed-label readout. Original source/caches and the genuine18/0 and28/0 original review baselines remain historical evidence. The current filename-derived ID replaces the old alias preserved above. Final own-note/current-memo/quoted-gate inputs are pinned before execution; no scientific helper or arbitrary parent campaign is registered. Independent same-session correction confirmation and owner integration remain pending. Formal audit is deferred until a solid TOE; a runner's success is not a science or audit verdict.
