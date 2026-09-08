---
claim_id: emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
historical_claim_id_alias: emergent_lorentz_invariance_dirac_point_taste_census
claim_scope: "Conditional unit-hop KS model on the coarse cubic lattice. T1: exact 2x2x1 cell square/trace and node condition, finite60^3 scan, and numerical folding to one8-mode2x2x2 node. T2: local Clifford census8=spin2 x chirality2 x flavor2, N_f=2, and4^3/6^3/8^3 zero counts. T3: exact cell-phase dispersion and Taylor coefficients-1/12,+1/360, isotropic leading phase velocity in supplied units, finite anisotropy/mixing checks; no band taste splitting or physical clock. T4: exact off-contact selection rule and finite288^3 FFT samples compared with continuum4/pi^2, with no infinite-distance remainder or historical0.21 equivalence. T5: projector identities and distinct-site pair covariance only under a supplied Slater/Born occupation law, plus explicit alternative joint law and optional zero-mode filling. Original finite values and all18 check IDs are preserved; added controls do not establish a permanent Record instrument, full negative association, parent campaigns, or physical Lorentz covariance."
upstream_dependencies: []
runner: scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py
---

# Emergent Lorentz invariance at the Dirac point, and the taste census

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; formal audit is deferred by the owner until a solid TOE.
**Status:** bounded - bounded or caveated result note
**Status authority:** current conditional source awaiting independent correction confirmation; no applied audit grade or axiom change.
**Primary runner:**
[`scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py`](../scripts/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.txt`](../logs/runner-cache/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_check_2026_09_03.txt)
**Proof setting:** the finite constructions and conditional readout below are supplied here. The linked current memo and historical gate are scoped context, not a physical derivation or acceptance of the gate campaign.

A staggered sign field on the coarse lattice `2Z^3` has a gapless point. What sits at that point is the question here, and it has three parts: how
many touchings the sign field really has and how many modes each carries; whether the modes disperse at one speed in every direction; and whether the
equal-time correlations they produce carry the coefficient a free massless Dirac field would carry. The algebra and named finite checks are reported separately; kernel asymptotics and physical readout remain unproved.
Along the way one reading of the eight-mode cell is corrected -- the locally redeclared factor names; the rest of that historical parent is unverified by this unit.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact algebra and explicitly bounded numerical checks for a supplied free hopping model; finite kernel comparisons and conditional Slater/Born readout, without asymptotic or physical Record claims."
trace_class: frontier_discovery
target_claim_id: emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_bounded_theorem_note_2026-09-03
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

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. Groups `A`-`C` are exact where tagged --
symbolic identities in `sympy`, integer and `Z[i]` matrix arithmetic at zero tolerance, exhaustive scan -- and the items tagged `[numerical]` are
floating-point evaluations, at the stated tolerance, on the grids and tori named.

1. `T1` (`A`). The magnetic cell of the sign field and the two nodes it carries, and their folding onto one 8-fold touching.
2. `T2` (`B`). The chirality census of the zero modes, and the relabelling of the eight-mode cell that follows from it.
3. `T3` (`C`). The exact dispersion at the node, the `-1/12`, the leading isotropic phase velocity in cell units and the `|p|^2/36` spread.
4. `T4` (`D`). The equal-time propagator: an off-contact selection identity and finite samples compared with a continuum coefficient.
5. `T5` (`E`). The projector sum rule and pairwise covariance under an explicitly supplied Slater/Born occupation law.

## Imports and authority

The mathematical model is supplied, not derived from the framework. No whole parent campaign is accepted. The Kawamoto-Smit staggering, the Dirac-Kahler spin-taste basis, the Nielsen-Ninomiya counting and
the free massless Dirac equal-time propagator are standard methodology; every object is redeclared here and the runner checks the finite statements and controls at the explicitly stated coverage; it does not prove continuum limits or physical interpretation. No observational value is imported; numerical fits remain finite evidence rather than proofs of limits. Non-load-bearing pointers, carrying no grade and no dependency
weight:

- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): the coarse lattice, the `Cl(6)`
  cell algebra, the intertwiner `U` with `T = diag(1,1,-1,-1)`, and the `2 A1 + 2 T1` content of its Theorem 4. Pointer only; the cell algebra and `U`
  are redeclared below and rebuilt by this runner from scratch.
- [Historical kinetic gate](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md): the kinetic-form clause and the corner-structure clause quoted below.
- [Current minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): the four axioms quoted in "Setting". No grade of theirs is cited and no hypothesis is adopted.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full
one-site possibility domain has algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule,
covariant under lattice translations and proper cubic rotations", and "For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a record locks exactly one admissible local
possibility", "records are permanent", "Only records are readable."

The historical gate text is quoted below with line wrapping normalized; its forcing and corner-representation claims are not proved or adopted here:

> **Kinetic-form clause.** Within the declared kinetic class (the naive-Dirac kinetic form on nearest-neighbor `Z^3` links, made
> compatible with the matter-statistics clause by site-local spin diagonalization), the kinetic operator is the staggered operator
> `D = (1/2) Σ_{x,μ} η_μ(x) (χ̄_{x+μ̂} χ_x − χ̄_x χ_{x+μ̂})` with the Kawamoto-Smit phases `η_1 = 1, η_2(x) = (−1)^{x_1},
> η_3(x) = (−1)^{x_1+x_2}`, unique as a local Z2 gauge class.

and its corner-structure clause reads:

> **Corner-structure clause.** The free staggered operator has the
> 8-element BZ-corner (taste-cube) doubler set, decomposing uniquely
> by Hamming weight as `1 + 3 + 3 + 1`; the hw=1 triplet carries an
> exact irreducible `M_3(C)` algebra (translations + `C_3[111]`)
> with no proper exact quotient.

Everything below reads that sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, free nearest-neighbour hopping only.
The one-particle matrix and its projectors are supplied mathematical objects. A many-body occupation interpretation additionally supplies a fermionic Slater state, an occupation measurement and the Born rule. Representing these in an ordinary qubit tensor product requires an encoding with its strings/constraints; ordinary composition alone does not supply fermionic statistics, a physical role pattern, or permanent Records. No such bridge is proved here.

Normalization is explicit: the runner's Hermitian `M` has unit bond coefficient. The quoted antihermitian gate `D` has coefficient `1/2`; on a compatible periodic torus the site phase `G_vv=i^{sum v}` gives `G(-iD)G^dag=M/2`. For the `2x2x2` cell, `p=2k` where `k` is coarse-site momentum. Limiting speed is `1` per cell, `2` per coarse site in supplied hopping/time units; no physical clock follows.

For the optional occupation interpretation, let `V` have orthonormal occupied columns and set `P=VV^dag`. Supply the Slater/Born law `Pr(S)=|det V_S|^2` on subsets of size `rank(P)`. Cauchy-Binet gives its generating polynomial `sum_S Pr(S) prod_{i in S} z_i = det(V^dag diag(z) V)`. Differentiating at all `z_i=1` gives `E[n_i]=P_ii` and, for `i != j`, `E[n_i n_j]=P_ii P_jj-|P_ij|^2`; repeated indices use `n_i^2=n_i`. This proves the conditional identities without deriving that joint law from a one-site marginal or the Record axiom.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the
KS sign field on it, the magnetic cells, the cell algebra and the intertwiner. `P1` (`A`) is the magnetic cell and its two nodes; `P2` (`B`) the
chirality census; `P3` (`C`) the exact dispersion and the velocity; `P4` (`D`) the equal-time projector, its selection identity and its coefficient;
`P5` (`E`) the projector sum rule and supplied-law distinct-site covariance. `P3`, `P4` use `P1`'s node; `P2`, `P3` share `P0`'s intertwiner. Scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; the **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`,
`eta_3(v) = (-1)^{v_1+v_2}`, the clause's phases read in coarse coordinates. The hopping matrix is `H_{wv} = eta_a(v)` on each coarse bond and zero otherwise,
hermitian, no on-site term.

A **magnetic cell** is a block of coarse vertices on which the sign field is periodic, so that Bloch's theorem applies with that block as unit cell;
`H(Q)` denotes the corresponding block matrix and `E(Q)` its positive eigenvalue branch. A **node** is a `Q` with `E(Q) = 0`. The **velocity
matrices** at a node are `M_a = dH/dp_a` there; the **speeds** are `v_a = sqrt((M_a M_a)_{11})`, the **chirality operator** is `X = -i m_1 m_2 m_3`
with `m_a = M_a / v_a`, and a zero mode is **right-handed** when `X = +1` and **left-handed** when `X = -1`. On a `2x2x2` cell the algebra is

```text
Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3),  Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3),  T = diag(1,1,-1,-1),  B = (XX, XY, XZ)
H(q) = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a],   U Gamma_a U^dag = -sigma_a (x) T,   U Xi_a U^dag = I (x) B_a
```

with `U` rebuilt here by Clifford averaging over the `64` words of the generated group. The **equal-time projector** of the half-filled sea is
`P = proj(E < 0)`, whose Bloch form is `P(q) = (1/2)(I - H(q)/E(q))`; `P_vu` is its coarse-real-space matrix element and `r = v - u`, `nhat = r/|r|`.

## Theorem 1 -- the magnetic cell has two nodes, and they fold onto one

**Conclusion.** For the KS sign field on `2Z^3`:

1. The minimal magnetic cell is `2x2x1`, four coarse sites, and there `H4(Q)^2 = (6 + 2 cos Q_1 + 2 cos Q_2 + 2 cos 2Q_3) I` with `tr H4 = 0`: two
   doubly degenerate bands `+- E4`.
2. Direction `3` carries one coarse site per cell, so its hop is diagonal and enters squared, `4 cos^2 Q_3 = 2 + 2 cos 2Q_3`. Hence `Q = (pi, pi, pi)`
   is **not** a node of the `4x4`: its spectrum there is `(-2, -2, 2, 2)`.
3. `E4 = 0` exactly when `cos Q_1 = cos Q_2 = cos 2Q_3 = -1`, so there are exactly two nodes in the magnetic BZ, `Q = (pi, pi, pi/2)` and
   `Q = (pi, pi, 3pi/2)`, each a 4-fold touching. An exhaustive `60^3` scan finds these and no others.
4. Taking a `2x2x2` cell instead folds both onto the single point `q = (pi, pi, pi)`: the `8x8` spectrum at `(Q_1, Q_2, 2Q_3)` is the union of the
   `2x2x1` spectra at `Q_3` and `Q_3 + pi`, and the folded point is one 8-fold touching.

**Proof.** Items 1 and 2 are symbolic identities in the three cell momenta, the `4x4` square and trace expanded term by term against the hopping rules
and the double-angle identity checked in closed form. Item 3 is the observation that each of the three terms is bounded below by `-2`, so the sum
vanishes only when all three saturate, together with an exhaustive scan of a `60^3` grid over the magnetic BZ and an eigenvalue count at each hit.
Item 4 evaluates both cells at matched momenta over `60` random points, `[numerical, 1e-11]`, and counts the kernel dimension at the folded point.
Items 1-3 exact.

**Reading, not theorem.** The alternating signs repeat over a block of four sites, not eight, and that block has two places where the spectrum closes
rather than one. Writing the same field on the larger block puts both places on top of each other. The larger block is convenient but it is not where
the touchings are; the count of modes is the same either way.

## Theorem 2 -- the chirality census, and what the eight modes are

**Conclusion.**

1. At `q = (pi, pi, pi)` on the `2x2x2` cell the velocity matrices are `M_a = -Gamma_a` **exactly**, all three speeds are `1`, and the chirality
   operator has spectrum `+1` fourfold and `-1` fourfold. The eight zero modes are two right-handed and two left-handed Weyl fermions of two
   components each: `N_f = 2` four-component Dirac fields, net chirality `0`, as Nielsen-Ninomiya requires.
2. Each `2x2x1` node separately carries `1R + 1L`, with speeds `(1, 1, 2)` in that cell's coordinates. The two nodes together are `2R + 2L`, the same
   vector-like `N_f = 2`.
3. In the intertwiner branch `U Gamma_a U^dag = -sigma_a (x) T` the transported velocity matrices are exactly `sigma_a (x) T`, so `X = I (x) T`
   **exactly** and `H(pi + p) = sum_a p_a (sigma_a (x) T) + O(p^2)`. `T = +1` is the two right-handed Weyl (`det v = +1`) and `T = -1` the two
   left-handed (`det v = -1`); the other branch exchanges the two labels and nothing else, so the relative assignment is branch-independent.
4. The coarse tori `L = 4, 6, 8` carry `8, 0, 8` zero modes, exactly the count from `q_a = 4 pi m / L` reaching the node value `pi` precisely when
   `4 | L`.

**Conclusion, local census.** The historical PR #7844 phrase "a two-component spin and a four-component taste label" is an attributed reading, not authority. Here the explicitly rebuilt matrices factor `8 = 2` (spin/Weyl components) `x 2` (chiralities) `x 2` (flavors), hence two four-component Dirac flavors. The historical parent's `2 A1 + 2 T1`, full representation content, physical encoding and other spectra are unverified and unaccepted by this unit; no inference about them follows from this local census.

**Proof.** Item 1's `M_a = -Gamma_a` is a symbolic differentiation of the `8x8` Bloch matrix followed by an exact comparison over `Z[i]` at
`q = (pi, pi, pi)`; the speeds and the spectrum of `X` follow from the `Cl(6)` relations and are evaluated exactly. Item 2 builds each `2x2x1` node's
velocity matrices by the same differentiation and reads the census, `[numerical, 1e-12]`. Item 3 rebuilds `U` on both branches by Clifford averaging,
verifies both intertwining relations and the transported `M_a` at zero tolerance, and reads `X = I (x) T` as an exact matrix identity; the handedness
is the sign of the determinant of the `3x3` velocity matrix on each two-dimensional spin block. Item 4 diagonalises the three tori directly, `[numerical, 1e-9]`, against the momentum-grid
count. The relabelling is item 3 read back: nothing is recomputed for it.

**Reading, not theorem.** The eight states at the closing point split into two mirror-image halves, one turning one way and one the other, and each
half is itself doubled. Counting the halves as a single four-way label hides the mirror. Counted properly there are two copies of one particle, each
copy carrying its own left and right halves, and the two copies are otherwise identical. The arithmetic that produced the four was right; the four was
a chirality pair times a genuine pair, not four of one thing.

## Theorem 3 -- one velocity, and where isotropy first fails

**Conclusion.**

1. `E(pi + p)^2 = sum_a (2 - 2 cos p_a)` exactly, with expansion `|p|^2 - (1/12) sum_a p_a^4 + (1/360) sum_a p_a^6 + O(p^8)`. The `O(p^2)` term is
   exactly isotropic and the leading anisotropy is the quartic `sum p_a^4` with coefficient exactly `-1/12` for this hop. Cubic quartics span `sum p_a^4` and `|p|^4`; only the anisotropic class modulo the isotropic quartic is unique.
2. Hence `v(nhat, |p|) = E/|p| = 1 - (|p|^2/24) sum_a nhat_a^4 + O(p^4)`: one leading phase velocity `v -> 1` in every direction, for every taste and both
   chiralities, in the supplied cell/hopping/time units. Along an axis the group velocity is `dE/dp = 1-p^2/8+O(p^4)`, distinct from the phase correction `-p^2/24`.
3. The `[100]`/`[111]` phase-velocity spread is `|p|^2/36 + O(p^4)`, tabulated at `|p| = 0.8, 0.4, 0.1, 0.05, 0.0125`, with log-log anisotropy exponent
   `1.998` against the exact value `2`.
4. `U H(pi + p) U^dag = sum_a sin p_a (sigma_a (x) T) + sum_a (1 - cos p_a)(I (x) B_a)` to `4e-16`. The taste-mixing second sum is `O(p^2)` and
   commutes with every spin generator -- a spin singlet -- so it does not enter the velocity at leading order. Mixing of the chosen flavor generators does not imply energy splitting: the full Bloch square remains scalar and each nonzero band is fourfold (spin times flavor).

**Proof.** Items 1 and 2 are `sympy` identities: the closed form of `E^2` at the shifted momentum, its series in a scale parameter along a fixed
direction, and the resulting series for `E/|p|` on the unit sphere, each residual reported as exactly zero. Item 3 evaluates the exact dispersion
along three directions and fits the spread, `[numerical]`. Item 4 compares the transported Bloch matrix against the closed form over random momenta at
three scales, `[numerical, 4e-16]`, and checks the commutator of each `I (x) B_a` with each spin generator at zero tolerance.

**Reading, not theorem.** The supplied hopping has the same leading dispersion in every direction. The first axis/diagonal phase-velocity difference is `|p|^2/36`; this does not supply a physical clock or boost-covariant interacting dynamics.

## Theorem 4 -- exact kernel selection and finite continuum comparisons

**Conclusion.**

1. Every entry of `Xi_a` and `Gamma_a` whose row and column differ in other than exactly one bit vanishes, and their diagonals vanish. Hence
   `P(q)_{ss'} = delta_{ss'}/2 - H(q)_{ss'}/(2E(q))` has zero off-diagonal entries off the one-odd-component set, and `P_{ss} = 1/2`. So `P_vu = 0` **exactly**
   for `r != 0` whenever `r = v - u` has zero or two or three odd components, with the separate contact `P_vv=1/2`: an identity of the projector at every momentum, not an asymptotic statement.
2. On the surviving set, with `a` the unique odd component, the continuum comparison is `(4/pi^2) |nhat_a| = 0.405285 |nhat_a|`. On a finite `288^3` cell-momentum grid
   the axis ratios `|P| n^3 pi^2/4` along `(n,0,0)` are `1.0049`, `1.0024`, `1.0019` at `n = 41, 61, 81`.
3. Stride-subsampled shell means of `|P_vu| |r|^3` are `0.21145`, `0.20353`, `0.20213` over `6 <= |r| <= 24`, `30 <= |r| <= 50` and `60 <= |r| <= 90`,
   against same-sample means of the prediction `(4/pi^2)|nhat_a|` of `0.21018`, `0.20340`, `0.20202`. The finite sequence is compared with the sphere average
   `2/pi^2 = 0.202642`. The historical parent's `0.21` remains an unverified historical report, not an established value of this finite computation or a proved common asymptotic law.

**Proof.** Item 1 is an entrywise check of the six generators over all `64` index pairs at zero tolerance, together with the definition of `P(q)`.
Items 2 and 3 evaluate `P` per momentum on a half-shifted `288^3` grid of cell momenta -- a grid that misses the node exactly -- by one inverse FFT
per surviving cell-index pair, so no `V x V` object is ever formed; the shells are enumerated with the strides `1`, `2`, `3` recorded in the runner.
`[numerical]` throughout, on the grid named.

**Continuum comparison, not a lattice-limit proof.** Fourier transformation of the homogeneous continuum symbol `p_a/|p|` gives the angular `r^-3` kernel. With cell separation `R`, `F^{-1}(1/|p|)=1/(2 pi^2 |R|^2)` away from contact; differentiation, the projector factor `1/2`, and `r approximately 2R` give `4/pi^2`. This comparison does not bound the discrete lattice remainder, finite-grid images or the infinite-distance limit. The listed samples are the evidence. Under the supplied Slater/Born law of Theorem 5, an amplitude `r^-3` would correspond to connected occupation covariance `r^-6`, not `r^-3`.

## Theorem 5 -- projector sum rule and conditional occupation covariance

**Conclusion.** On the `8^3` coarse torus with one antiperiodic direction, which lifts the eight zero modes and leaves an exact half-filled projector,
and on the `6^3` periodic torus:

1. `P_vv = 1/2` at every site and `sum_{u != v} P_vu^2 = P_vv - P_vv^2 = 1/4` exactly, at `1e-15`. Under the supplied Slater/Born occupation law the total number variance is zero, since the particle count equals the projector rank.
2. For distinct sites `u != v`, the supplied Slater/Born occupation law has `E[n_u n_v]=P_uu P_vv-|P_uv|^2` and `Cov(n_u,n_v)=-|P_uv|^2 <= 0`. The original `262144` ordered-entry determinant diagnostic has maximum excess `0`; its diagonal entries are not joint occupation probabilities because `n_v^2=n_v`. The strengthened check also requires Hermiticity/idempotence and valid distinct-pair probabilities. This is pairwise covariance, not a proof of full negative association of arbitrary events or of a physical Record law.
3. On the `8^3` **periodic** torus the eight zero modes make half filling ambiguous: `proj(E < 0)` has rank `252` and `P_vv = 252/512` uniformly, so
   the sum rule closes at `0.2499390` rather than `1/4` while the projector identity itself still holds at `4.4e-16`. That torus is reported here and
   is not used for the `1/4`.

**Proof.** Direct diagonalisation of each torus hopping matrix, projection onto the negative-energy subspace, and evaluation of the identities
entrywise. `[numerical, 1e-15]` for items 1 and 2, `[numerical]` for item 3's rank and value. The largest object formed is `512 x 512`.

**Conditional proof and decisive alternatives.** Supply orthonormal occupied orbitals `V` and their Slater determinant with joint occupation probabilities `Pr(S)=|det V_S|^2` for subsets of size `rank(P)`, `P=VV^dag`. Cauchy-Binet gives normalization. Expanding a two-orbital minor gives the distinct-site identity above (or contracting the corresponding minors for higher rank); a repeated site uses `n_v^2=n_v`. The runner explicitly enumerates all six two-particle outcomes for a four-site Slater state, checks their means/joints and rejects a nonprojector. The alternative law assigning probability `1/2` to each configuration `{0,1}` and `{2,3}` has the same single-site means `1/2` and positive `Cov(n_0,n_1)=1/4`; it does not have the same pure one-body density matrix. Thus the joint law is additional information, not an implication of those means or the Record axiom.

Zero modes do not prevent uniform half filling. On periodic `4^3`, eight sublattice-supported `q=pi` null modes form `Z`; filling four Walsh combinations plus the strict-negative modes gives a rank-32 projector with every diagonal `1/2`. The same cell construction extends to `8^3`. The original strict-negative rank-252 `8^3` result is preserved; that convention does not itself choose the extra zero-mode occupations.

## Corollary -- what the staggered sector's low-energy content is

Within the setting declared above, on the grids and tori named, and for free hopping only:

1. The low-energy content of the coarse-lattice staggered sector is **two tastes of one four-component Dirac field**, with a single leading isotropic phase velocity
   in supplied cell units and finite kernel samples compared with the continuum Dirac coefficient; no physical or lattice-limit equivalence is asserted.
2. The content is **vector-like**: net chirality `0` at every node and in total, as Nielsen-Ninomiya requires on a lattice.
3. The locally rebuilt eight-dimensional cell has two Dirac flavors. Historical parent multiplicities and representation claims are not accepted by this correction.

**What this is not.** No chiral sector: the content is vector-like and nothing here produces a chiral one. No generations from tastes: `N_f = 2` is two
identical copies of one field, with no distinguishing quantum number, no mass splitting and no label attached here. Not a proof of Lorentz symmetry of
correlators: what is shown is the isotropy of the one-particle dispersion and one equal-time kernel, with no physical clock supplied, and boost covariance of
interacting correlators is untouched. Coarse lattice only: the fine `(4,2,2)` pattern's tetragonal anisotropy is not examined here.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- No applied science/audit status is set. Current source metadata and explicit contextual citations are corrected; owner integration generates the manifest.
- Nothing here is derived from the axioms. The coarse lattice and the sign field are declared objects and the theorems are about them.
- No update rule, formation site, rate, coupling, mass, or absolute unit appears, and no dynamical clause is supplied.
- No corner of the taste cube is identified with any named species; the relabelling names none either.

## Interfaces named for other lanes, not moved here

- **The fine-lattice anisotropy.** The velocity statement is proved for the coarse hopping. The fine `(4,2,2)` role pattern is tetragonal, and what
  its encoded hopping does to the `|p|^2/36` spread is not examined here. A lane wanting isotropy on the fine lattice must supply it.
- **Interactions.** Only free hopping is compared; a four-fermion term could move the velocity and either coefficient, and nothing here bounds that.
- **A mass term.** The spectrum is exactly gapless at the node and no clause quoted here supplies a mass; that is the next lane's question.
- **The chiral sector.** Absent, by corollary item 2; a lane wanting chiral matter must break the pairing, and nothing here says how.

## Remaining live routes

1. Larger grids and other tori. The `288^3` momentum grid and the tori `4^3`, `6^3`, `8^3` are what is used; nothing is claimed beyond.
2. Subleading structure. Only the declared finite kernel samples are compared with the continuum `|r|^-3` coefficient; a lattice-limit remainder remains open.
3. The `8^3` periodic torus. Its zero modes leave half filling ambiguous; a lane wanting the `1/4` there must fix the filling.

## Executable claim block

```text
setting: supplied unit-hop KS matrix, cell Clifford algebra and optional Slater/Born occupation readout; current axioms/context quoted, not used to derive these
T1: exact magnetic-cell square/trace/node condition;60^3 node scan;60-point folding comparison
T2: 8=spin2 x chirality2 x flavor2, N_f=2; periodic L=4,6,8 zero counts8,0,8
T3: E^2=sum(2-2cos p); Taylor coefficients-1/12,+1/360; phase spread |p|^2/36; p=2k and supplied units; no energy taste splitting
T4: exact off-contact selection;288^3 finite FFT axis ratios1.0049,1.0024,1.0019 and declared stride shells; continuum4/pi^2 comparison only
T5: projector identities; supplied-law distinct-site Cov=-|P_uv|^2; same-marginal positive-covariance alternative; original periodic8^3 strict-negative rank252 retained
added_controls: actual joint Slater outcomes/nonprojector, explicit periodic4^3 zero-mode filling, phase/group and D-to-M normalization
original_evidence: PASS=18 FAIL=0 is historical; final corrected totals are in the fresh source/input-bound cache
```

## Proof boundary

The exact cell identities and their algebraic domain are stated above; numerical evidence uses only the `60^3` scan, `288^3` half-shifted FFT, stride shells `1,2,3`, and named `4^3,6^3,8^3` tori. No infinite-lattice kernel remainder, interacting boost symmetry or fine `(4,2,2)` role-pattern result is proved. The coefficient `-1/12` belongs to this unit-hop dispersion; `4/pi^2` is a continuum comparison, not a proven lattice asymptotic. Units, sea filling and Slater/Born readout are supplied. Physical time, encoded roles, permanent Records and their instrument remain unresolved.

Only the relative handedness is independent of the intertwiner branch. No whole historical parent proof or `2 A1+2 T1` representation is accepted. Periodic zero modes do not uniquely select half filling; the original strict-negative convention and the optional filled-zero-mode witness are distinct. Interactions, other fillings, instruments, mass terms and chiral projections are outside this model, not ruled out by a global no-go theorem.

## Review record

The 2026-09-08 correction preserves all original finite grids, numerical targets and 18 check IDs; the historical E2 predicate and the implicated labels are superseded where applicable by the corrected source, with actual additional controls. Both final own-note and quoted-context identities are declared inputs. The filename-derived claim ID is current; the old alias is retained above. Independent correction confirmation and owner integration remain pending; a successful runner is bounded computational evidence at this conditional scope, not a science or audit verdict. Formal audit is deferred until a solid TOE. The outside-docs correction history records the original source/cache hashes and finding dispositions.
