---
claim_id: taste_singlet_second_mass_body_diagonal_hop_vortex_strings_2n_modes_2026_09_03
claim_type: bounded_theorem
claim_scope: "For supplied cell Pauli matrices: the four-dimensional anticommutant, unique taste-singlet direction, length-three cell support, algebraic conjugation signs, uniform-node gap and uniform-cell square identity. Actual nonuniform profiles generally fail first/second mass anticommutation. Dense-counted finite spectral windows give the stated core/ring velocity census, approximate projected labels and finite splitting data, not a universal index or asymptotic theorem. A uniform staggered mass on bipartite Hermitian hopping has spectral gap at least its magnitude. Physical spatial parity, gauge charge, phase formation and effective-range derivation remain open."
upstream_dependencies: []
runner: scripts/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.py
---

# Taste-singlet cell mass algebra and finite vortex-string census

**Date:** 2026-09-03; corrected 2026-09-09
**Type:** bounded_theorem
**Status:** bounded - bounded or caveated result note
**Audit:** unset; formal audit is deferred until a solid TOE is ready.
**Primary runner:** [scripts/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.py](../scripts/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.py)
**Current cache:** [logs/runner-cache/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.txt](../logs/runner-cache/taste_singlet_second_mass_body_diagonal_hop_vortex_strings_check_2026_09_03.txt)

This is a conditional finite matrix construction. Every operator, graph,
profile, coefficient, embedding, cutoff and boundary condition below is supplied.
The mathematical results do not derive a physical Hamiltonian, state-selection
rule, species realization, Record-production process or gauge coupling.
The [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the framework
boundary: permanent single records and nearest-neighbour physical adjacency
supply neither these operators nor their physical interpretation. No approved
primitive is invoked by the dimensionless calculations.

The exact original note, runner and cache are preserved in
`archive/backlog/vortex-7935-7949/originals/7949/` at their original PR head.
Those historical bodies include superseded claims; they are recovery evidence,
not current scientific authority. Current source and actual declared input
identities are checked before execution and bound into the cache. The runner
imports no local scientific helper or external data.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact conditional finite algebra with explicitly finite numerical diagnostics. No general index or physical species theorem."
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: "Resolve the stated physical realization and generalization obligations; formal audit remains deferred."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Definitions and exact cell algebra

All generators and the coarse-cell encoding are declared, not inferred from
physical nearest-neighbour adjacency. The original notation below calls the
mass “record-native”; this means the specified diagonal term, without a
physical Record formation derivation. The [current mass note](A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md)
and [current Dirac-cell note](EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md)
provide corrected contextual boundaries; the present definitions are supplied
and rebuilt without calling those runners.

```text
cell          2x2x2 coarse cell; bits (b_1,b_2,b_3) = (x,y,z) mod 2;
              Pauli-string index 4 b_1 + 2 b_2 + b_3
KS signs      eta_1 = 1, eta_2 = (-1)^x, eta_3 = (-1)^{x+y}                 SUPPLIED
Gamma_a       (Y1, Z1Y2, Z1Z2Y3)          Dirac-point velocities are -Gamma_a
Xi_a          (X1, Z1X2, Z1Z2X3)          the Wilson-like (1 + cos q_a) terms
eps           Z1Z2Z3                      the record-native staggered mass   SUPPLIED
H(q)          sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a];  Dirac point (pi,pi,pi)
X             i Gamma_1 Gamma_2 Gamma_3 = -Y1X2Y3     the 3+1D chirality
M2            X1Y2X3 = i Xi_1 Xi_2 Xi_3   the taste-singlet second mass      SUPPLIED
s_b           (Y2X3, Y1Z2X3, Y1X2) = (i Xi2Xi3, -i Xi3Xi1, i Xi1Xi2)  taste Paulis
Xi_b          = M2 (s_1, -s_2, s_3)_b     the taste-triplet second masses
m_1 + i m_2   M(rho) e^{i n phi}, M(rho) = M_0 tanh(rho/xi)                  SUPPLIED
              m_1 on sites times eps_v = (-1)^{x+y+b_3}; m_2 on cell centres
              (2X + 1/2, 2Y + 1/2) multiplying M2 on that cell
plane         open N_x x N_y transverse (x,y); z carried by bit b_3 and Bloch q_z
p             q_z - pi;   V_z = dH/dq_z, taken exactly
core / ring   rho < R_c about a declared core; within 2.5 of the plane edge
alpha_v       a proposed U(1)-valued coefficient; gauge charge unspecified  SUPPLIED
```

Sizes: `M_0 = 0.7`, `xi = 2`, in-gap window `|E| < 0.686`, `R_c = 5`; `N = 16, 24, 32` for the single vortex; `40 x 24` for the string/anti-string pair; `24 x 24` for the link-field control; an `8 x 8` plane for the real-space anticommutator. Cores sit at
`((N-1)/2, (N-1)/2)`, a cell corner, so no site sits at the core. Every transverse eigenproblem is solved by sparse shift-invert about `E = 0` from a fixed deterministic start vector -- **there is no randomness and no seed anywhere in the runner** -- followed
by a Rayleigh-Ritz re-diagonalisation on the returned span, and every window is checked against a full dense count: the `k`-th eigenvalue nearest zero lies outside it, and the count inside it equals a dense LAPACK count. The largest dense matrix is `2048 x 2048`.

## Cell anticommutant -- the anticommutant of the Dirac-point Clifford set is exactly four Pauli strings

**Conclusion.** A second mass must anticommute with the three Dirac-point velocity matrices `Gamma_a` and with the first mass `eps`. A **complete enumeration** of all 64 Pauli strings on the `2x2x2` cell finds exactly four that do: `XII = Xi_1`, `ZXI = Xi_2`,
`ZZX = Xi_3` and `XYX = i Xi_1 Xi_2 Xi_3 =: M2`. The count is confirmed independently by a rank computation -- the nullity of the linear map `M |-> ({M,Gamma_1}, {M,Gamma_2}, {M,Gamma_3}, {M,eps})` on the 64-dimensional real Pauli space is exactly `4` -- so no
linear combination outside the four is missed. Their bit-flip counts are `1, 3, 1, 1`. The three single-flip elements are the single-bond dimerizations and form a **taste triplet**: `Xi_b = M2 (s_1, -s_2, s_3)_b` at residual `0.0e+00`, the singlet times a
taste Pauli. `M2` is the one element of the four that commutes with all three taste Paulis, and is therefore the **taste singlet**.

`M2` is Hermitian, squares to `1`, and equals `i Xi_1 Xi_2 Xi_3`, all at `0.0e+00`; it anticommutes with `eps` and with each `Gamma_a` and **commutes** with each `Xi_a`, all at `0.0e+00`. The 3+1-dimensional chirality `X = i Gamma_1 Gamma_2 Gamma_3 = -Y1X2Y3`
commutes with the `Gamma_a` and anticommutes with both `eps` and `M2` at `0.0e+00`, and

```text
X M2 = i eps        residual 0.0e+00        so  (X, M2, eps) = (tau_3, tau_1, tau_2)
```

on the Dirac-point subspace: `m_1 eps + m_2 M2` is a two-component mass algebra `m_1 + i m_2` against the declared kinetic term. The spectrum at the node is exactly `+-sqrt(m_1^2 + m_2^2)`, fourfold each, for `(m_1, m_2) = (0.3, 0.4), (0.7, 0), (0, 0.7), (0.5, -0.5)`, at
maximum deviation `4.4e-16`. The `Cl(6)` relations, the anticommutation of `eps` with all six generators, and the agreement of the real-space cell hopping rules with the landed `H(q)` at three momenta are all `0.0e+00`.

## Support, conjugation and the nonuniform-mass counterexample

The singlet M2 has eight nonzero entries connecting each cell corner to its
bit complement, amplitude `i(-1)^b2`, so every hop has Manhattan length three.
Even bit-flip Pauli strings commute with eps; odd ones anticommute. The
anticommutant directions with fewer than three flips are exactly XII,ZXI,ZZX.
Thus no operator confined to nearest-neighbour or face-diagonal cell support
realizes this singlet. This is a support statement in the declared encoding;
it does not prohibit an effective longer-range operator generated from more
fundamental nearest-neighbour data, or classify other encodings/blocks.

`M2*=-M2` and `eps M2 eps=-M2` are exact algebraic signs. They do not by
themselves implement physical time reversal or spatial inversion of sites,
cells and background fields. In particular, at p=(.4,.2,-.3),
`max|eps H(pi+p) eps-H(pi-p)|=.157878011994`: eps reverses the Wilson-like
Xi terms as well as Gamma. A continuum/internal scalar-pseudoscalar convention
would require its own specified transformation law. No physical parity
violation or charged scalar is derived. A U(1)-valued coefficient has no
specified gauge charge until a gauge action is supplied.

For arbitrary cell weights, `{diag(eps),weighted M2}=0` because every
M2 hop reverses parity. For a varying real first mass the actual identity is

```text
{diag(m1 eps), weighted M2}_ij
    = eps_i (m1_i-m1_j) (weighted M2)_ij.
```

Consequently it vanishes precisely when m1 is equal along every nonzero
weighted M2-connected pair. Constant m1 is sufficient; arbitrary profiles
are not. The supplied 8x8 vortex profile has maximum anticommutator
.140173976408, despite its unweighted staggered-sign anticommutator being zero.
The runner evaluates this actual operator and the entry formula. The face-
diagonal hop still commutes with the staggered sign. These facts keep the
uniform-cell square separate from the inhomogeneous plane calculation.

## Uniform-cell square and small-momentum energy

For spatially uniform m1,m2, anticommutation of eps with the bare symbol and
M2, and commutation of M2 with Xi, give exactly

```text
H(pi+p)^2 = [sum_a(2-2cos p_a)+m1²+m2²] I
           +2 m2 sum_a(1-cos p_a) M2 Xi_a,
M2 Xi_a = (s1,-s2,s3)_a.
```

The taste matrices anticommute pairwise, so the exact squared energies are
the scalar term plus or minus `2 m2 sqrt(sum_a(1-cos p_a)^2)` (the sign
labels may exchange when m2 changes sign). Expanding gives
`E²=m1²+m2²+|p|² ± m2 sqrt(sum_a p_a^4)+O(|p|^4)` for fixed masses.
This is an anisotropic quadratic-energy splitting, not a proof of physical
Lorentz symmetry or a gapless group velocity. Original controls at three
momenta and two mass pairs have residual below 1e-14. At the node the
eigenvalues are ±sqrt(m1²+m2²), four of each when the gap is nonzero.

## Declared finite census and approximate labels

Every reported window uses deterministic sparse shift-invert, QR and
Rayleigh-Ritz orthonormalization, finite-value/orthogonality checks, full
operator residuals, and an independent dense LAPACK count/eigenvalue comparison.
An exterior returned Ritz value alone would not prove completeness; the dense
count and residual/eigenvalue comparison provide the additional coverage.
All 26 original windows remain tested. The energy window is .686, radius-five
core weight >.6 selects a core, and otherwise edge-distance<2.5 weight >.6
selects a ring; other states are mixed. Velocities are actual dH/dq_z
expectations. Classification and counts depend on this declared convention.

| N24 winding at p=.1 | Core count | Core energies | Core velocity | Core/ring signed velocity census |
|---|---:|---|---|---|
| +1 | 2 | .09990,.09990 | .994,.994 | +2 / -2 |
| -1 | 2 | -.09990,-.09990 | -.994,-.994 | -2 / +2 |
| +2 | 4 | .10020,.10020,.10022,.10022 | at least .991 | +4 / -4 |

The +1 window contains 16 states, core weights >=.845 and ring weights <=.013;
its projected taste eigenvalues are ±.961,±.985,±.946. Negative winding gives
opposite velocity and projected s3≈±.946. The +2 core weights are >=.712,
with projected s3≈-.951,-.950,.950,.951. These are approximate opposite taste
labels within a selected energy subspace, not simultaneous conserved taste
quantum numbers. The integer count is `2|n|` for these fixtures and signed
velocity net is `2n`; no arbitrary-winding formula or doubling theorem follows.

For N=16,24,32, the finite secant `(E(+.1)-E(-.1))/.2` is
1.0379,.9990,.9983 and the p=0 minimum absolute energies are
.02834,.003682,.0004706. The latter decrease by factors 7.7 and 7.8 in these
three sizes. Positive p=0 splitting excludes exactly linear dispersion through
zero; a finite trend does not prove exponential decoupling or a limiting velocity.

For n=±1, the original individual X expectations are near zero. The corrected
control diagonalizes X compressed onto the complete +1 core pair and finds
all its eigenvalues within 1e-12 of zero, making that conclusion basis
independent in the selected pair. By contrast, the compressed -Gamma3
eigenvalues are about .999307255508 with residual to a +1 eigenstate
.037222157154. They are approximately polarized, not sharp eigenvectors.
The n=+2 projected X values near ±.338 have trace about -4.1e-4, approximately
zero rather than exactly traceless. The observed velocity signs agree with
-Gamma3 polarization in these fixtures; this is not a Jackiw-Rossi index proof
or a physical chirality identification.

## Triplet comparison, mixed masses and pair geometry

Replacing M2 by Xi3 in the same N24,+1 fixture gives two core states
`(E,V,s3)=(-.13082,-.759,-.718),(.13082,.759,.718)`, projected s3≈±.941,
and signed core census zero. At p=0 the gap is 2×.08455. These are results
for this one triplet orientation and profile, not all nearest-neighbour models.
The identity Xi3=M2 s3 supports the uniform taste-sector comparison; finite
lattice terms do not conserve all taste labels.

For mixed `a M2+b Xi3`, the three tested (a,b) values (1,.5),(.5,1),(.8,.8)
give core counts 2,2,1 and signed nets +2,0,+1. These match the comparator
`n[sgn(a+b)+sgn(a-b)]` in these three fixtures. At a=b one taste’s second
mass vanishes, so a general protected gapped-index formula or universal
transition is not established by this comparison.

On the 40x24 pair with cores (9.5,11.5,+1),(29.5,11.5,-1), at p=.15 the
core energies are ±.14948, velocities ±.988, two states per core, and 16 ring
states have signed net zero. At p=-.15 the core nets remain +2/-2 and ring
net zero; the finite secant is .997. These finite local compensations are
not a general theorem of no net handedness for every plane or Hamiltonian.
The n=2 pair is not computed; no claim about why it must fail is supplied.

## Flux control and uniform bipartite mass gap

The N24 Gaussian Peierls-flux fixtures have width 2, target flux 2pi or 4pi,
and actual plaquette sums 1.0002 or 2.0004 in units 2pi. With uniform m=.7,
there are no states in |E|<.686 at p=-.1,0,.1; nearest energies are .702 or
.700. The massless first-flux control at p=.1 gives 12 states in |E|<.3,
nearest pair ±.1155 with velocities ±.864 and signed census zero. This
finite control does not say that link fields in all models give nothing.

There is also an exact conditional gap argument: any finite Hermitian hopping
T connecting only opposite eps sectors obeys `{T,eps}=0`, eps²=I. For a
uniform real m, `(T+m eps)²=T²+m² I`, hence |E|>=|m|. Arbitrary complex
bipartite link phases preserve this identity. A separate deterministic complex
six-site fixture checks it. Variable masses, same-parity hopping and other
couplings require separate analysis.

## Physical suppliers and open routes

The coarse encoding, KS signs, Hamiltonian coefficients, cell singlet term,
profile, phase values, core positions, boundary and Bloch conventions are
supplied. A physical derivation of the effective singlet and a law producing
the phase remain open. A Wilson-line dressing or U(1)-valued site coefficient
alone does not specify the transformation or phase-formation law. No claim
that the framework cannot ever realize one, or exact minimal supplier count,
is made. Selecting a physical mover requires another bridge; the finite
census does not select one. The auxiliary-square construction is a different
supplied operator family, not an equivalent physical-history theorem.

Other windings, parameters, encodings, periodic boundaries, the uncomputed
n=2 pair, asymptotic limits, phase dynamics, many-body sectors, anomalies and
physical parity/gauge actions remain open. These are limitations of the
current results, not a no-go claim.

## Validation and recovery

All twenty original numerical predicates and all 26 window comparisons are
retained. Four focused scientific controls test the actual profiled mass,
full-symbol inversion counterexample, basis-independent core labels and
uniform bipartite gap. Source/input binding precedes science. The cache gives
the actual executed total and complete results; historical source/caches are
preserved separately. Neither a successful runner nor independent landing
review grants an audit verdict.
