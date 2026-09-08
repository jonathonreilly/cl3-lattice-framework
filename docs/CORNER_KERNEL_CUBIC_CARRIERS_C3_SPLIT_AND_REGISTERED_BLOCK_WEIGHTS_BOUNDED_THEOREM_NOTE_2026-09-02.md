---
claim_id: corner_kernel_cubic_carriers_c3_split_and_registered_block_weights_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "Six conditional finite claims T1-T6 on the redeclared corner representation: 2A1+2T1 with two grading-selected Hamming copies and a CP1 mixed-carrier family; invariant grading/intertwiner; C3 split; twelve operator restrictions and three-parameter surjectivity; finite invariance census; comparison of the two chosen copies. Ratio r only for a nonzero diagonal coefficient and phase only for a nonzero off-diagonal coefficient. Exact symbolic identities are distinguished from numerical cross-checks. No physical carrier, species, probability or Record formation law follows."
upstream_dependencies: [minimal_axioms_2026-06-29]
runner: scripts/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.py
---

# Corner-kernel cubic multiplicities, grading-selected carriers and supplied block coefficients

**Date:** 2026-09-02; source correction 2026-09-08.
**Claim type:** bounded_theorem
**Status:** bounded, conditional source; no scientific grade assigned.
**Primary runner:** [corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.py](../scripts/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.py)
**Runner cache:** [corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.txt](../logs/runner-cache/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.txt)
**Correction provenance:** [dated correction and four verbatim original bodies](../.claude/science/review-fixes/carriers-7869-7880-20260908/REVIEW_CORRECTION.md).
Historical checkpoint identifier: `corner_kernel_cubic_carriers_c3_split_registered_block_weights`. The actual claim ID is derived from this note's filename.

## Authority and supplied setting

The [current governing memo](MINIMAL_AXIOMS_2026-06-29.md) fixes the interpretation boundary.
All finite operators, states, tensor products, grading, pins and readout conventions below are explicitly supplied mathematical definitions.
They are not derived from the four axioms. A fixed local possibility does not supply a central-sector readout, probability weighting,
physical generation label, clock, state preparation, selection law or permanent Record-formation mechanism.
The old Record central-sector/K-CPT proposal and earlier parent campaigns are historical context only; their original quotations
remain in the dated history. No parent campaign, physical bridge or ancestor authority is accepted by this unit.
Only this note and the current memo are mutable semantic inputs; all matrices and constraints are redeclared locally, with no runtime helper.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: source_correction
artifact_role: conditional_finite_result
next_trace_action: "Independent source confirmation; physical suppliers remain unresolved; formal audit deferred until a solid TOE."
bare_retained_allowed: false
```

## Definitions and obligation boundary

Use the supplied coarse lattice `2 Z^3`, ordinary complex tensor composition, and the eight-dimensional `2x2x2` cell with
`Gamma=(Y1,Z1 Y2,Z1 Z2 Y3)`, `Xi=(X1,Z1 X2,Z1 Z2 X3)`, `epsilon=Z1 Z2 Z3`, and `T=i Gamma1 Gamma2 Gamma3`.
The finite Bloch matrix is `H(q)=sum_a [(1+cos q_a) Xi_a + sin q_a Gamma_a]`.
The runner has **fine/site-coordinate side 4 relative to the eight-site blocking**, hence 64 sites and **coarse-cell side 2**, with cell momenta `q in {0,pi}^3`. Its site-coordinate nearest bond is the declared bond of `2 Z^3`; no physical length unit or clock is derived.
A cubic carrier means an invariant irreducible three-dimensional subspace of the supplied corner representation.
All operator tables below restrict to the **additional Hamming/grading-eigenspace choice** `P=P_hw1` or `Q=P_hw2`.
For a C3-invariant Hermitian restriction, `M=a I+b U+conj(b) U^2`, with real `a`, complex `b`;
`r=|b|^2/a^2` only for `a!=0`, and `delta=arg(b)` only for `b!=0`.
The literal `--`/None entries of the original table mean undefined, not zero.

Symbolic Clifford, rational character/projector and circulant identities are exact. Integer-valued arrays are represented partly
through complex floating NumPy arrays, with Gaussian-integer rounding/validation. The original kernel eigencount, overlap and
exhibited commutant matrix-rank diagnostics are numerical. The character formula supplies the exact commutant dimensions.
No claim that every original check is zero-tolerance arithmetic is retained.

## Theorem 1 -- the isotypic decomposition and two grading-selected Hamming copies

**Conclusion.** (1) `H(pi, pi, pi) = 0`, so the whole eight-dimensional cell is the kernel at the corner; the side-4 site-coordinate torus (side-2 coarse-cell torus) kernel is eight-dimensional and is
spanned by the corner basis. (2) All 24 proper cubic rotations lift to signed permutations preserving the hopping, and all 576 products close on the nose as integer
matrices on that kernel: a genuine representation of `O`, not projective. (3) Its characters `(E, 8C3, 3C2, 6C4, 6C2') = (8, 2, 0, 4, 0)` decompose, in exact rational
arithmetic against a self-checked orthonormal character table, as `2 A1 + 2 T1`, and the isotypic projectors are in the corner basis exactly `P_A1 = diag(1,0,0,0,0,0,0,1) =
P_hw0 + P_hw3` and `P_T1 = diag(0,1,1,1,1,1,1,0) = P_hw1 + P_hw2`, with `P_A2 = P_E = P_T2 = 0`. (4) Each Hamming block is separately `O`-invariant, with characters
`(1,1,1,1,1)` on `hw = 0, 3` and `(3,0,-1,1,-1)` on `hw = 1, 2` -- one `A1` and one `T1` each.

**Proof and implementation boundary.** The symbolic identity gives the corner zero. The explicit corner basis has Gram `8 I` and is annihilated by the torus matrix. Completeness follows independently from `H(q)^2 = (6+2 sum cos q_a)I`: on the side-4 site-coordinate/side-2 coarse-cell torus, cell momenta are 0 or pi and the scalar vanishes only at the all-pi corner. The original A2 eigencount uses NumPy at tolerance 1e-9 and its overlap uses allclose; these are numerical cross-checks, not zero-tolerance proofs. Item 2 solves each lift's signs by breadth-first propagation and compares all 576 products as integer matrices, the kernel-basis matrices obtained by exact
division by `8`. Items 3 and 4 are `Fraction` arithmetic: the orthogonality relations and the projector formula `P_irr = (d/24) sum_R chi_irr(R) M_R`, block by block.

**Scope.** The representation is `2 A1 + 2 T1`. This does not uniquely split either multiplicity-two isotypic space. The Hamming eigengrading supplies two particular irreducible triplets; it is an additional restriction to discuss only them.

## Theorem 2 -- the grading is an eigen-grading, and the two grading-selected copies are exchanged

**Conclusion.** (1) `i sum_a Gamma_a Xi_a = Z_1 + Z_2 + Z_3` exactly; it commutes with all 24 lifts, and its corner spectrum is `3 - 2 hw`, so the `1 + 3 + 3 + 1` grading
is the eigen-grading of that one `O`-invariant `Cl(6)` bilinear. (2) The `T1` isotypic is `T1 (x) C^2`: the commutant of the 24 lifts has dimension `8` on the kernel and
`4` on the `T1` isotypic, by the exact rational formula `(1/24) sum |chi|^2`, and four independent commuting elements `P_hw1`, `P_hw2`, `P_hw2 T P_hw1`, `P_hw1 T P_hw2` are
exhibited -- the group alone does not split the six-dimensional isotypic. (3) `T = i Gamma_1 Gamma_2 Gamma_3` commutes with all 24 lifts, is unitary, carries `hw = 1` onto
`hw = 2` and back with rank `3`, and anticommutes with `epsilon = Z_1 Z_2 Z_3 = diag((-1)^hw)`; `T != epsilon`.

**Proof.** Item 1 is a `Z[i]` matrix identity and a diagonal read-off, with commutation checked against all 24 integer lifts at zero tolerance. Item 2 is the character
formula in `Fraction` arithmetic plus a commutation check and a rank computation for the four exhibited elements. Item 3 is `Z[i]` arithmetic: unitarity, the vanishing of
`P_hw1 T P_hw1` and `P_hw2 T P_hw2`, the rank of the off-diagonal blocks, and the anticommutator. The character formula gives exact dimensions; the original exhibited-matrix rank checks use NumPy matrix_rank, while the operator identities are checked on the stated exact-valued matrices.

**Scope.** The supplied grading distinguishes two particular irreducible copies. It is not the isotypic decomposition alone, and the continuous mixed-carrier family is not removed by O invariance. The C3 singlet/doublet statements below are restricted to these chosen copies and basis conventions.

## Theorem 3 -- the C3 restriction and its singlet

**Conclusion.** On each carrier, with `U = C|_{T1}`: (1) `tr U = 0`, `U^3 = I`, eigenvalues `{1, omega, omegabar}` -- each carrier is the regular representation of `Z/3`.
(2) The `C`-invariant vector has corner weights exactly `(1/3, 1/3, 1/3)` on both carriers; against the *fixed* democratic `W = (1,1,1)/sqrt3` the overlaps are `|<W|v>|^2 =
1` on one carrier and `1/9` on the other, and that difference is a corner-sign gauge artefact, removed by rephasing a single corner, which carries `U` to the plain 3-cycle
and `v` to `W`. (3) The singlet projectors `P_0 = |v><v|` have every entry of modulus `1/3` -- `P_0 = J/3` in the gauge that carries `v` to `W` -- are idempotent, and `P_0`
and `P_1 = I - P_0` both commute with `U`.

**Proof.** Item 1 is exact `3x3` arithmetic over `Z`: the trace, the cube, and the eigenvalues as exact cube roots of unity. Item 2 computes the nullspace of `U - I`
exactly and evaluates the weights and overlaps as exact rationals, the rephasing being the diagonal sign matrix read off the invariant vector. Item 3 is exact idempotence,
entrywise modulus and commutation.

## Theorem 4 -- the block weight of every stipulated bilinear, and the surjectivity

**Conclusion.** For the twelve stipulated bilinears:

1. Each restricts to an **exactly** circulant operator on each carrier -- residual exactly `0`, `c = conj(b)` throughout -- with the coefficients the runner tabulates:
   `sum_a Gamma_a`, `sum_a Xi_a` and `T` restrict to zero; `i sum_a Gamma_a Xi_a` gives `a = +1 / -1` and `epsilon` gives `a = -1 / +1`, both with `b = 0`; `(sum_a
   Gamma_a)^2 = (sum_a Xi_a)^2 = 3 I`; the `p_a^2` coefficient of `H(pi + p)^2` is the identity on both carriers; the two bivector sums `i(Gamma_x Gamma_y + Gamma_y Gamma_z
   + Gamma_z Gamma_x)` and its `Xi` counterpart give `a = 0`, `|b| = 1`; and the two `Gamma`-`Xi` cross terms give `a = 0`, `|b| = 1` with `delta` differing by `pi` between
   the carriers.
2. **The structural fact.** No listed operator has `a != 0` and `b != 0`. The six that commute with all 24 lifts have `b = 0` by Schur on an irreducible `T1`; the
   `O`-average of each of the other six is exactly `0`, and `a` depends on the `O`-average alone because the Hamming projectors are `O`-invariant, so `a = 0` there. Hence
   every nonzero scalar restriction (`a != 0, b = 0`) has `r = 0`; `r` is undefined when `a = 0`, including the zero operator.
3. **The surjectivity.** The restriction map from real `C_3`-invariant Hermitian quadratics onto the circulant algebra has real rank `3` on each carrier: the three-element
   family `alpha (sum_a Z_a) + beta i(sum_cyc Gamma_a Gamma_{a+1}) + gamma i(sum_a Gamma_a Xi_{a+1})` maps onto `(a, Re b, Im b)` with rank `3`, so every `(a, Re b, Im b)`, with `delta` defined only when `b != 0`,
   hence every `r` in `[0, inf)`, is realised by stipulated coefficients -- `(alpha, beta, gamma) = (2, 1, 1)` registering `r = 1/2` and `(2, 1, 0)` registering `r = 1/4`,
   exactly and on both carriers. **These are stipulated coefficient choices exhibited as registered patterns; neither is derived, and neither is "the" `r`.**

**Proof.** Item 1 builds each operator over `Z[i]` at zero tolerance, verifies hermiticity and Gaussian-integrality, restricts it and decomposes it exactly by `a = tr M /
3`, `b = tr(M U^2) / 3`, `c = tr(M U) / 3`, comparing the residual against the zero matrix as an exact symbolic identity; the `p_a^2` coefficient comes from symbolic
differentiation of `H(pi + p)^2`. Item 2 checks the 24 commutators, forms the exact integer sum `sum_R M_R O M_R^T` and compares it to `0` or to `24 O`. Item 3 is an exact
rank over the rationals and two exact evaluations.

**Scope.** These conclusions concern the twelve listed operators and the supplied three-parameter linear family. They do not exclude every operator constructible from the kinetic algebra. Values of `r` are coefficient ratios, not physical Record weights. Zero restrictions and nonzero off-diagonal restrictions have undefined `r`, not zero `r`.

## Theorem 5 -- the invariance census

**Conclusion.** For all twelve operators on both grading-selected copies, with `r` only when `a != 0` and phase `delta` only when `b != 0`: (1) all six relabellings of a carrier's basis leave `(a, |b|, r)` unchanged, with circulant residual `0`; (2)
all 24 cubic conjugations, `O -> g O g^{-1}` with `C -> g C g^{-1}`, which cover all eight `C_3` elements, leave `(a, |b|, r)` unchanged, with residual `0`; (3) naming
`C^2` rather than `C` the generator sends `b -> conj(b)`, that is `delta -> -delta`, and leaves `(a, |b|, r)` fixed.

**Proof.** Items 1 and 2 re-run the exact circulant decomposition on the relabelled or conjugated data and compare the coefficients as exact symbolic quantities; item 3
re-runs it against `U^2` in place of `U`. These decompositions are exact symbolic checks; Gaussian-integer construction and kernel overlap diagnostics are separately numerical where indicated.

## Theorem 6 -- which listed operators distinguish the grading-selected pair

**Conclusion.** Exactly four of the twelve distinguish the two carriers: `i sum_a Gamma_a Xi_a = sum_a Z_a` and `epsilon`, by the sign of `a` -- that is, through the sign
convention of the chirality grading -- and `i sum_a Gamma_a Xi_{a+1}` and `i sum_a Gamma_a Xi_{a+2}`, with equal `|b|` and `delta` differing by exactly `pi`. The remaining
eight restrict identically to both. No listed operator is `C_3`-invariant with `b != 0` on exactly one carrier.

**Proof.** A direct comparison of the exact table of Theorem 4 across the two carriers, with the phase difference evaluated as an exact symbolic identity.

**Reading, not theorem.** Nothing reported here depends on which member of a triplet is written first, or on which axis the reader calls the first; the one choice that
shows is the direction of the cycle, and it flips the sign of one angle and moves nothing else. As for the two triplets, the only things in this list that tell them apart
are the grading itself and terms mixing the two halves of the Clifford set, and even those give both the same magnitude, differing by a sign or a phase. Nothing here makes
one triplet the one that carries a weight while the other does not.

## Multiplicity countercontrol and domain controls

The commutant on `T1 tensor C^2` is `M2(C)`. Every complex line in the multiplicity space defines an invariant irreducible triplet:
a `CP^1` family, not just the two Hamming copies. With `C=Q T P`, the actual exact projector
`R=(9P+16Q+12(C+C†))/25` has rank 3, is idempotent, commutes with all 24 lifts, and has character norm 1.
It differs from `P` and `Q` and does not commute with `epsilon`. More generally the isometry
`u -> alpha u + beta T u`, `|alpha|^2+|beta|^2=1`, embeds the same irreducible representation.
The grading-eigenvector restriction selects the two coordinate lines. No physical process choosing such a line is provided.

The original twelve-by-two coefficient table is retained in the actual cache, including zero restrictions.
Additional exact controls contrast `(a,b)=(0,0),(1,0),(0,1)`: their ratios are respectively undefined, 0, undefined;
phase is defined only in the last case. The real-rank-three restriction map still realizes every finite nonnegative ratio by supplied coefficients.
All original A1–F2 check IDs and numeric table payloads are preserved; labels now distinguish their domains and arithmetic.

## Conditional conclusion and remaining suppliers

The useful results are the exact isotypic decomposition, a supplied invariant grading, an intertwiner, the C3 split,
the stipulated coefficient table and surjective linear family, and the full finite relabelling/conjugation census.
They do not select a unique physical carrier or a species label. Even after restricting to the Hamming pair,
choosing an epsilon sign and a monitored operator/readout remains supplied. The finer mixed-carrier locus remains possible.
The original flavor, PMNS, species-bridge and labeling discussions survive as historical quotations only, with no accepted parent proof.

## N1–N8 negative-scope record

- **N1, attempted routes.** Cubic work executes the representation/commutant, C3 restrictions and the stipulated operator/invariance probes. Role work executes binary-star orbits, three marker geometries and the stated finite quantum-pin families. These are the actual attempts; multiple cases within one family do not manufacture five independent mechanism families. The five-family procedural minimum remains unmet.
- **N2, implication relations.** Mixed-carrier freedom, coefficient freedom, binary unintended configurations, quantum local/global-span excess and physical supplier gaps are different predicates. Their pairwise logical independence under all other hypotheses is not established; no independent-wall count is claimed. The positive 1D exception and mixed carriers remain explicit.
- **N3, hidden premises.** Carrier grading, operator coefficients, torus, marker/pin family, tensor composition, measurement basis and static penalty are supplied. None constructs a physical clock, Born law, preparation or permanent Record process.
- **N4, residual matching.** The 1/2 and 1/4 coefficient examples are supplied choices. The role trace estimates use the unchanged four-probe finite protocol with unbounded projection bias. No measured target or physical value is fitted here.
- **N5, rhetoric.** Finite/specified-domain exclusions replace universal selection, unique-carrier, period-collapse and all-junk-entangled claims. Exact algebra and numerical support are separated throughout.
- **N6, partial paths.** Grading-selected computations, mixed-carrier alternatives, finite unwanted witnesses and 1D positive cases survive. Other coefficient families, pins, energetic terms, larger windows and spacings remain open.
- **N7, strongest alternatives.** The mixed invariant rank-three projector defeats uniqueness; intended uniform configurations defeat the old shortcut; product junk defeats an entanglement-only mechanism; the 1D exact positive case defeats a universal negative. The repaired controls exercise those alternatives.
- **N8, historical echoes.** Earlier flavor/Record and role-pattern claims are dated context, preserved verbatim with original identities. No historical status, unsupported theorem or broader campaign is promoted through a quotation. Formal audit is deferred; this packet assigns no grade.

