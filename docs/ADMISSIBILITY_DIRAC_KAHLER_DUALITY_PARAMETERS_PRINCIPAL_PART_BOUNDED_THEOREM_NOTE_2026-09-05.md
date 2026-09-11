---
title: "Admissibility — Dirac-Kähler Duality Parameters and the Principal Part: Exact Parity Blocks, D07 Congruence, Run-Witness Union Loci, Generic W1 Factorization, Four W1 Slices, Selected Pencil Branches, and Two Formal Registration Slices — Conditional Finite Matrix Mathematics"
claim_id: admissibility_dirac_kahler_duality_parameters_principal_part_bounded_theorem_note_2026-09-05
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md
claim_type: bounded_theorem
claim_scope: "Exact finite matrix algebra for M = H0 D(kappa) + D(kappa)^T H0 on the supplied period-2 construction: the parity blocks and D07 congruence at symbolic moduli and parameters; the old det-B union locus at W1 and L+−/L−+; generic W1 factorization over the stated rational-function fields; two-quadric exclusion on four named W1 slices; all-parameter single-quadric exclusion at W1; on-plane persistence and one tested off-plane exclusion at L+−/L−+; selected pencil branches and the deformed flat control; and two separately fixed formal shear/volume slices. Unsampled special factorization and single-quadric loci remain open. No action, physical kernel, assembly selector, metric, propagation law, spacetime or dynamics is supplied."
upstream_dependencies: "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py (corrected Block 213 finite construction and witnesses); scripts/admissibility_dirac_kahler_weighted_kernel_released7981_7988_fixtures_2026_09_10.py (bounded extracted Block 201/209/211 definitions, source hashes recorded); scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py and its paired note (six AST-identical Block 105 assembly/Hodge helpers); docs/MINIMAL_AXIOMS_2026-06-29.md and docs/audit/data/axiom_premise_nodes.json (authority inputs only; no kernel/action premise); this paired note and runner"
runner: scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py
date: 2026-09-05
block: 214
series: toe-axiom-closure
status: bounded theorem note
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
historical_target_blocker_text: "The duality parameters are switched on. The graded-cone theorem was stated at the degree-diagonal representative; W1 with D16 = 1/4 supplied the original bounded off-representative probe."
source_of_blocker_text: recovered_original_handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the plane and overlap sum unselected; leave unsampled special factorization and single-quadric loci open; treat the two formal registration slices separately."
conditional_surface_status: "recovered conditional support pending fresh bounded execution and affected-source review; no audit verdict"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-dimensional linear algebra and bounded polynomial calculations over QQ, QQ(sqrt 6), and stated rational-function rings, with each locus claim restricted to the calculation actually performed"
audit_required_before_effective_retained: true
bare_retained_allowed: false
historical_parent_commit: 851aff9b3f950e5f08b0bd0878df2e1992bbe15b
correction_base: 1157173587fde42555d36659954e71c544e23312
current_main_at_note_edit: 2491ff70e921098fbb9130765458926c57c82364
registered: 0
adopted: 0
axiom_movement: none
---

# The Duality Parameters and the Principal Part — bounded exact calculations on the supplied finite construction

**One sentence.** With Block 211's four duality parameters kept symbolic, the
onsite folded `H0` stops preserving grade parity for **every** one of them —
each is a cross-parity entry of the cell — but the principal part
`M = H0 D + Dᵀ H0` treats them in two ways: `D07` (the empty–full corner pair,
grade 0–3) is removed from `M` by the exact unipotent congruence
`U = I − (D07/D3) E₇₀`, which acts on `H0` only as `D0 → D0 − D07²/D3`, so
`D07` leaves `det M` untouched; a simple 0-form branch rescaling follows on
the `D07`-only degree-diagonal/star line, while a mixed-parameter exact
counterexample rules out that stronger branch claim in general;
`D16, D25, D34` (the three grade 1–2 pairs) fill the odd–odd block of `M` with
the zero-diagonal `3 × 3` `[(D16 + D25) kt, (D34 − D16) kx, −(D25 + D34) ky]`
on the 1-forms. At the run witnesses the old `det B²` union locus is the plane
`D16 = D34 = −D25` onsite and `s = 0` overlap. At W1 the symbolic determinant
is generically one irreducible quartic squared, and four named W1 slices exclude
a product of two quadrics away from their origins; other specializations and
linear-times-cubic factors remain open. The single-quadric system is
inconsistent for every parameter at W1; at `L+−` and `L−+` it persists on the
plane and is excluded at the one tested off-plane point `D16 = 1/4`. The flat
cell with a parameter on is not the identity. Shear and volume registration
are measured on two distinct fixed formal slices.
**Scout-grade finite exact linear algebra on one cell form, not a spacetime and
not a dynamics** — Block 211's fence, inherited verbatim through Block 213.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Six imposed
objects, zero registered, zero adopted, zero axiom movement.

**FIVE WORDS ARE FENCED BEFORE THE FIRST NUMBER IS READ.**

- **NO GRAVITY IS SUPPLIED.** No lapse variable in an ADM phase space, no shift
  vector, no Hamiltonian constraint, no momentum constraint, no first-class
  constraint algebra, no Dirac closure, no Dirac observable, no gauge orbit and
  no diffeomorphism quotient. Nine structures, enumerated as a measured
  constant and gated (`B-2`).
- **`PARAMETER` NAMES A FREE COORDINATE OF ONE SOLVED LINEAR SYSTEM.** Block
  211's solve leaves exactly four unconstrained entries of the cell form; they
  are not couplings of anything physical, and **no value of any of them is
  selected here** (`B-3`, mutation `claim_parameter_value_selected`).
- **`PARITY` NAMES THE EVEN/ODD GRADE SPLIT OF THE EIGHT CORNERS.** Whether the
  folded `H0` maps even to even is a statement about a matrix's zero pattern.
- **`CONE` NAMES THE ZERO SET OF `det M(κ)`**, a homogeneous polynomial of
  degree eight, read as a polynomial identity. It names no light cone.
- **`LOCUS` NAMES AN ALGEBRAIC SUBSET OF THE PARAMETER SPACE**, given by a lex
  Gröbner basis. `BRANCH` names an eigenvalue of an exact `8 × 8` matrix.

**AND THE ASSEMBLY IS A SUPPLIED FORK, NOT A RESULT.** Both of Block 105's
assemblies are run; they treat the parameters differently (four coordinates
versus their sum), and this block decides between them nowhere (`H-2`).

- **THE PLANE IS EXHIBITED AND NOT PREFERRED.** `D16 = D34 = −D25` is where
  the odd–odd block of `M` vanishes identically. No premise prefers it.
- **THE INSTANCE SCOPE IS ONE OF EVERYTHING.** One bench, one family, seven cone
  witnesses and the flat cell, four declared parameter points, two assemblies,
  two readings, the declared one-parameter slices. Six restrictions, gated.
- **THE READINGS ARE READINGS.** Six of them are enumerated below and none is
  licensed (`B-5`).

**EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER
METAPHYSICAL NECESSITY** — the cycle-913 caution, carried verbatim — and every
positive here is candidacy within this formalism and never a claim about nature.

---

## W1 — the wall, and the charter

### What was open

The supplied six-face linear system leaves four free entries of the `8 × 8`
cell form — `D07, D16, D25, D34`, each pairing a corner with its Hodge
complement. Its positive-definite parameter region is open and bounded. The
following separate inequalities are necessary bounds at W1:

> `a^2 < v0/v1 = 15/16, b^2 < v1/v0 = 16/15, c^2 < v1/v0 = 16/15, d^2 < v1/v0 = 16/15.`

(in the extracted finite construction, `D07^2 < v0/v1` and
`D16^2,D25^2,D34^2 < v1/v0`). They do not define a positive-definite box:
`D07=0`, `D16=D25=D34=3/4` obeys each separate bound, while the common
all-ones degree-1/degree-2 subspace has restriction
`[[1/2,3/4],[3/4,8/15]]` with determinant `−71/240`. Pencil claims below
therefore require actual positive definiteness. Block 213 then ran the weighted-kernel dispersion
at the degree-diagonal representative `D07 = D16 = D25 = D34 = 0` and proved
its graded-cone theorem there; the recovered original evidence exhibited `W1`
with one parameter switched on at `1/4` — on the variety, positive definite,
inside the bound — and found, by substitution:

| duality parameter on | `H0` preserves grade parity | `det M` factors (total degree, multiplicity) | cone = union of the two Hodge cones |
| --- | :---: | --- | :---: |
| none (degree-diagonal) | **yes** | `(2,2), (2,2)` | **yes** |
| `D07 = 1/4` | no | `(2,2), (2,2)` | yes |
| `D16 = 1/4` | no | **`(4,2)`** | **no** |
| `D25 = 1/4` | no | **`(4,2)`** | **no** |
| `D34 = 1/4` | no | **`(4,2)`** | **no** |

Block 213 recorded this as its `REOPEN` item 7 and claimed nothing off the
degree-diagonal slice. The original wall was therefore bounded: four points
of the open positive-definite region were probed; the mechanism and broader
parameter loci were unknown.

### The charter

Registry check first (`docs/audit/data/axiom_premise_nodes.json`, read in
full): the four axioms and the three approved primitives are the complete
supplied foundation; none is used as content here. Every object below is an
imposed measured object of the recovered finite construction.
Determine exactly, at symbolic parameters wherever the fraction-free machinery
reaches: (a) which parameters break the grade parity of the folded `H0` under
each assembly and the mechanism by which `D07` leaves the cone while
`D16, D25, D34` do not; (b) `det M(κ)` at symbolic parameters, its factorization
type at the stated generic point and slices; (c) the single-quadric question at
W1 and the bounded plane/off-point checks at `L+−`, `L−+`; (d) selected pencil
branches with a parameter on; (e) shear and volume registration on two
explicit formal slices. The flat cell with
a parameter on is the sharpest control: it is **not** the identity.

---

## N1 — THE CONSTRUCTION AND THE CONTROL

### The objects, read through their own runners

```text
cell form   D = Block 211's solve_pinned(at_zero=False): 8 x 8 over QQ (or QQ(sqrt 6)) with the
            four free names D07, D16, D25, D34 kept symbolic; at zero it EQUALS Block 213's
            solve_witness cell at every one of the eight cells (flat + seven cone witnesses).
carriers    exactly the eight antidiagonal entries (0,7),(1,6),(2,5),(3,4) and transposes, in
            Block 209's corner order 0=(0,0,0) 1=(0,0,1) 2=(0,1,0) 3=(0,1,1) 4=(1,0,0) 5=(1,0,1)
            6=(1,1,0) 7=(1,1,1): D07 pairs grade 0 with grade 3; D16, D25, D34 pair a unit corner
            (grade 1) with its complement (grade 2).
raising     D(kappa)[c, c + e_mu] = eta_mu(c) k_mu, Block 209's shadow: the twelve entries
            D[1,0]=ky D[2,0]=kx D[4,0]=kt D[3,1]=kx D[3,2]=-ky D[5,1]=kt D[5,4]=-ky D[6,2]=kt
            D[6,4]=-kx D[7,3]=kt D[7,5]=-kx D[7,6]=ky,  with D[0,:] = 0 and D[:,7] = 0.
assemblies  onsite: the folded H0 IS the cell (H0 = D exactly at the formal family);
            overlap: H0 = H0(0) + (s/4) P111, s = D07 + D16 + D25 + D34, P111 the Hodge-complement
            permutation c -> c + (1,1,1) -- all eight parameter entries have the SAME step mod 2.
principal   M = H0 D(kappa) + D(kappa)^T H0, symmetric, measured from the composed rules; in the
            even/odd order (0; 3,5,6 | 1,2,4; 7):  M = [[M_ee, B], [B^T, M_oo]],  B parameter-free.
```

The eight cells, their free names and their reconciliation with Block 213's
degree-diagonal cells are gated at `C-1`/`C-2`; the two folded structures at
`C-3`.

---

## N2 — THE PARITY LEMMA AND THE D07 CONGRUENCE, at symbolic moduli and symbolic parameters

### The mechanism, measured on the formal family

`M = H0 D + Dᵀ H0` with `H0 = [[H_e, H_eo], [H_eoᵀ, H_o]]` and
`D = [[0, D_eo], [D_oe, 0]]` (the raising part maps grade `g` to `g + 1`, so
even to odd and odd to even) gives, as an identity of block matrices,

```text
M_eo = H_e D_eo + D_oe^T H_o          (parameter-free: Block 213's B, unchanged),
M_ee = H_eo D_oe + (H_eo D_oe)^T,     M_oo = H_eo^T D_eo + (H_eo^T D_eo)^T.
```

The parameters live **only** in `H_eo`, so they enter `M` only through the two
diagonal blocks. Under the onsite assembly `H_eo` is the antidiagonal
`[[0,0,0,D07],[0,0,D34,0],[0,D25,0,0],[D16,0,0,0]]` (rows `0,3,5,6`, columns
`1,2,4,7`), and the measured blocks at the formal family — symbolic
`(v0, g0, v1, g1)`, symbolic parameters, all-plus signs — are

```text
M_ee  =  [[0, u^T], [u, 0_3]],   u = ( (D07 + D34) kt,  (D25 - D07) kx,  (D07 + D16) ky )   on corners (3, 5, 6),
M_oo  =  [[N, 0], [0, 0]],       N = [[0, (D16 + D25) kt, (D34 - D16) kx],
                                      [(D16 + D25) kt, 0, -(D25 + D34) ky],
                                      [(D34 - D16) kx, -(D25 + D34) ky, 0]]        on corners (1, 2, 4), corner 7 empty.
```

**Why `D07` is different.** Each parameter `p` on the pair `(e, o)` contributes
`p (E_o D[e, :] + E_e D[o, :] + transposes)`: two borderings, of corner `o` by
row `e` of `D` and of corner `e` by row `o` of `D`. For `(0, 7)` the first
bordering vanishes because **row 0 of `D` is zero** — nothing is raised *into*
the empty corner, the 0-form being the bottom of the grading (column 0, the
raising out of it, is not zero) — so `M_oo` gets nothing from `D07`; and the
second bordering
is `D07 · (row 7 of D)`, which is already present in `M` as row and column 7
scaled by `D3` (`M[7, ·] = D3 D[7, ·]`, `M[0, 7] = M[7, 7] = 0`). For the three
grade 1–2 pairs both borderings are nonzero (`D[1,·], D[2,·], D[4,·]` and
`D[3,·], D[5,·], D[6,·]` are all nonzero), so `M_oo` fills. Gate `F-1`.

### The `D07` congruence — exact, at symbolic everything

With `U = I − (D07/D3) E₇₀` (unipotent, `det U = 1`):

```text
U^T M U   =  M |_{D07 = 0}                                        (exact, symbolic moduli),
U^T H0 U  =  H0 |_{D07 = 0}  with  D0  ->  D0 - D07^2 / D3  =  v0 - D07^2 v1,   nothing else moved.
```

Thus `det M` and the inertia of `M` are independent of `D07`, and the pencil
`(M,H0)` is simultaneously congruent to the zero-`D07` pair with the 0-form
block shifted by `−D07²/D3`. The shift is the Schur complement of the
`{0,7}` form block `[[v0,D07],[D07,1/v1]]`. On the **D07-only
degree-diagonal/star line**, where `D16=D25=D34=0`, this isolates the familiar
0-form branch and replaces `kᵀ(D1/D0)k` by
`kᵀD1k/(D0−D07²/D3)`.

That isolated-branch conclusion does not hold with other duality entries on.
For the exact positive-definite example
`H=I8+(E07+E70)/4+(E16+E61)/3`, `k=(1,2,3)`, the same congruences hold, but the
candidate `224/15` has residual
`det((H⁻¹M)²−(224/15)I)=528724036/455625`. The characteristic polynomial is
`(8λ²−238λ+1719)²(15λ²−434λ+3056)²/14400`. Gate `F-2`, mutation
`break_d07_congruence`.

### Overlap: the sum, and nothing else

All eight parameter entries have the same step `(1, 1, 1)` modulo 2, so the
folded overlap `H0` is `H0(0) + (s/4) P₁₁₁` with `s = D07 + D16 + D25 + D34`
and `P₁₁₁` the Hodge-complement permutation: grade parity is preserved **iff
`s = 0`**, and `M` depends on the four parameters only through `s` (moving the
whole value from one parameter to another leaves `M` unchanged: measured at the
formal family). Gates `C-3`, `F-3`.

---

## N3 — THE UNION LOCUS AND THE FACTORIZATION TYPE

### `det M = det B²` exactly on a plane

For `n × n` blocks,
`det [[0,B],[Bᵀ,C]]=(-1)^n det(B)²` (and likewise when `C=0`). Here `n=4`, so
the sign is positive. Onsite, `M_oo ≡ 0` iff
`D16 + D25 = D34 − D16 = D25 + D34 = 0`, i.e. on the plane `D16 = D34 = −D25`
(for every `D07`). That the plane is also **necessary** is measured: at `W1`
and at the two locus witnesses the ideal generated by the `κ`-coefficients of
`det M − det B²` has a raw lex Gröbner basis whose radical is certified as the
declared linear ideal by two direct checks: every raw generator lies in that
linear ideal, and bounded powers of every declared linear generator reduce to
zero modulo the raw basis. At `W1` the raw onsite basis is
`{(D16−D34)²,(D16−D34)(D25+D34),(D25+D34)²}`, certifying
`rad=(D16−D34,D25+D34)`. The overlap target is `(s)`. This is a certificate
for these measured ideals, not a general factor-splitting radical algorithm.
Gate `F-4`, mutation `break_union_locus`.

> **THE DEGREE-DIAGONAL BLOCK-SQUARE IDENTITY `det M = det B²` IS RESTORED
> EXACTLY ON `D16 = D34 = −D25` ONSITE (ANY `D07`) AND ON `s = 0` OVERLAP,
> AT `W1` AND THE TWO LOCUS WITNESSES, AND NOWHERE ELSE THERE. ONSITE, `det B`
> IS THE PRODUCT OF THE TWO HODGE-READING QUADRICS; OVERLAP, IT IS BLOCK 213'S
> DISTINCT NON-HODGE PAIR.**

### Generic W1 factorization and four named W1 slices

At symbolic parameters, under both assemblies at `W1`,
`det M` is proportional to `Q²`, with `Q` a single irreducible factor over `QQ(parameters)`, of total degree 4 in `κ` and of
degree **exactly 2 and even** in the parameters: `Q = Q0 + Q2`, `Q0 = ±` the
degree-diagonal product of the two Hodge quadrics (at `W1` that is `±(45/8) det B`;
the rational content sits in front, `det M = (8/45)² Q²`), `Q2` a quadratic form in
`(D16, D25, D34)` (in `s` under overlap) with quartic coefficients. At `W1`,
`D16` alone: `Q = Q0 + D16² (6 kt² ky² − 3 kt kx ky² + 6 kx² ky²)`, the
original W1 quartic recovered. Gate `F-5`.

**Four slice tests.** One exact factor test sets `Q=q1q2` with two general
quadrics (normalised by the nonzero `kt⁴` coefficient). On the four declared
slices through `W1` (onsite) — `D16` alone, `D25` alone, `D34` alone,
`D16 = D25 = D34 = s` — the two-quadric eliminant is **`s²`**. Thus no product
of two quadrics occurs away from the origin on each of those four slices. This
does not classify other parameter directions. Gate `F-8`, mutation
`break_factorization_type`. The linear-times-cubic test (a line factor), the
slices at the other four rational witnesses, and the full three-parameter
two-quadric eliminant off the slices (the thirteen-unknown lex basis did not
finish within the budget) are **not computed** — recorded as could-nots, not
paraphrased into a theorem.

---

## N4 — THE FATE OF THE COINCIDENCE LOCUS, THE BRANCHES, AND THE DEFORMED FLAT CELL

### Single-quadric results at W1 and two bounded locus checks

`det M = (kᵀ G k)⁴` for some symmetric `G` — one metric's cone — is a
polynomial system in the six entries of `G` and the parameters. Its lex
Gröbner basis is `(1)` — **inconsistent over the algebraic closure for every
parameter value** — at `W1` under both assemblies (`F-6`, mutation
`claim_single_metric_cone_restored`). At the two locus witnesses `L+−` and
`L−+` (onsite; `√6` carried as `r` with `r² − 6` adjoined where a Gröbner
basis is taken): along the whole plane `(D16, D25, D34) = (s, −s, s)`, symbolic
`s`, `det M` is `(kᵀ G1 k)⁴` times a constant — the union locus makes this an
identity, and on the locus the two Hodge quadrics coincide — while at the
declared off-plane point `D16 = 1/4` the single-quadric system in `G` is
inconsistent. Therefore the old single-quadric zero set persists on the plane
for every `D07`, and a single quadric is excluded at the declared off-plane
point (`F-7`, mutation `break_coincidence_fate`). The rest of the off-plane
single-quadric locus at `L+−` and `L−+` is not computed. Failure of equality
with the old `det B²` away from the plane does not by itself exclude a
different single quadric.

### The branches with a parameter on

| point | pencil `(H0⁻¹ M)²` charpoly in `λ` | form `M²` |
| --- | --- | --- |
| `W1`, zero | Block 213's: `kᵀ(D1/D0)k`, `D3 kᵀ E D2⁻¹ E k`, transverse pair — each doubled | — |
| `W1`, `D07 = 1/4` | 0-form branch `kᵀ D1 k/(D0 − D07²/D3)` = `(4/7)(2kt² − …)` (was `8/15`), top-form `(3/8)(3kt² − …)` unchanged, transverse pair unchanged | irreducible of degree 8 (was a quartic squared) |
| `W1`, `D16 = 1/4` | no polynomial quadratic-form branch over the stated field: one irreducible quartic in `λ`, squared | irreducible of degree 8 |
| `W1`, plane `(1/4, −1/4, 1/4)` | the cone is Block 213's; only the 0-form branch `kᵀ(D1/D0)k` survives as a quadratic form, the top-form and transverse branches merge into an irreducible cubic, squared | irreducible of degree 8 |
| `L+−`, `D07 = 1/4` | constants `{128/119, 32/27, 4/3, 4/3} · kᵀ G1 k` — the 0-form constant `1 → 128/119` | — |
| `L+−`, `D16 = 1/4` | no polynomial quadratic-form branch over the stated field: one irreducible quartic, squared | — |

The `D07` rescaling is exact: at `L+−`, `v1/v0 = 9/8`, so
`1/(1 − D07² v1/v0) = 128/119` at `D07 = 1/4`; `D07² = (v0/v1)(1 − 1/μ) = 5/36`
(inside the bound `v0/v1 = 8/9`) would tie the 0-form constant to the
top-form constant `μ = 32/27`, but the transverse pair `4/3` does not move —
**this D07-only locus pencil is not scalar for any `D07`** (`F-10`). Under
`D16=1/4` at W1 the four pencil branches become the algebraic roots of one
irreducible quartic, doubled; none is a polynomial quadratic form over the
stated coefficient field.

### The deformed flat cell — the sharpest control

At `(c, v) = (0, 1)` the degree blocks are the identity, so with a parameter
on the cell is `I + (parameter entries)`, **not** the identity: `H ≠ I` on the
bench (measured), and

```text
det M_flat = Q_flat^2,   Q_flat = -|k|^4 + Q2_flat,   D07 absent,   Q2_flat = 0 exactly on the plane D16 = D34 = -D25,
Q2_flat = D16^2 ky^2 (kt^2 + kx^2) + D25^2 kx^2 (kt^2 + ky^2) + D34^2 kt^2 (kx^2 + ky^2)
          + 2 D16 D25 kx^2 ky^2 - 2 D16 D34 kt^2 ky^2 + 2 D25 D34 kt^2 kx^2;
bench multisets on (4,2,2), pencil reading, D16 = 1/4 or D07 = 1/4: {0 x8, 1 x6, 16/15 x2}  (form: irrational roots),
Bloch union = direct bench at each (D-3).
```

R5's control is reproduced at zero parameters only (`D-1`); with a parameter
on, the "flat" symbol is a deformed one, and its exact deformation is `Q2_flat`
(`D-2`, mutation `break_flat_deformation`).

---

## N4c — REGISTRATION UNDER THE PARAMETERS, and the #7970 record

Two different formal slices are measured; their quantifiers must not be
combined:

```text
shear:   at fixed (v0,v1)=(15/16,1), d(det M)/dg0 != 0 and d(det M)/dg1 != 0
         with (D16,D25,D34) symbolic; the ideal of
         kappa- and moduli-coefficients of each derivative in (D16, D25, D34) is (1):
         NO parameter point cancels either shear's registration.
volume:  at fixed (g0,g1)=(1/4,1/4), det M is proportional to its unit-volume value at zero
         parameters and NOT with symbolic D16,D25,D34 on: the volumes enter the cone THROUGH the
         parameters -- the parameter entries carry no volume while the degree blocks do, so the
         relative scale is no longer a pure factor.
```

On those respective formal slices the supplied kernel matrix registers the
shears and, through the parameters, the diagonal moduli. The historical matter-side
comparison (PR #7970, at its own
conditional scope) responds to the diagonal metric and to no shear. The
tension recorded by Block 213 is therefore **modified, not resolved**: with a
parameter on, both sides see the diagonal, and only the kernel side sees the
shear. Recorded here; no bridge is supplied (`G-1`, `G-2`).

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | gate |
| :---: | --- | --- | :---: |
| 1 | free names, carriers, reconciliation at zero | `D07, D16, D25, D34`; eight antidiagonal entries; equal to Block 213's cells | `C` |
| 2 | onsite `H0 = D`; overlap `H0 = H0(0) + (s/4) P111` | identities at the formal family | `C` |
| 3 | flat control at zero parameters | `H = I`, `{0×8, 1×8}`, `Q = |k|⁴` | `D` |
| 4 | deformed flat cell | `Q = −|k|⁴ + Q2_flat`, `D07` absent, plane restores | `D` |
| 5 | Bloch union = direct bench at `W1 + D16`, `W1 + D07` | both assemblies, both readings | `E` |
| 6 | `M_ee`, `M_oo` | `u`, `N` as displayed | `F-1` |
| 7 | `D07` congruence | `Uᵀ M U = M|₀`, `D0 → D0 − D07²/D3` | `F-2` |
| 8 | overlap sees the sum | `M(s)` only | `F-3` |
| 9 | union locus | plane / `s = 0`, `W1` and the two locus witnesses | `F-4` |
| 10 | generic W1 type under both assemblies | one irreducible quartic squared, `Q2` even quadratic | `F-5` |
| 11 | W1 single-quadric system, all parameters | inconsistent (basis `(1)`) under both assemblies | `F-6` |
| 12 | `L+−`, `L−+` bounded single-quadric checks | persists on plane; excluded at `D16=1/4`; remaining off-plane locus open | `F-7` |
| 13 | slices at `W1` | eliminant `s²` | `F-8` |
| 14 | branches; `128/119`; `5/36` | as displayed | `F-9`, `F-10` |
| 15 | registration | shear identity at `(v0,v1)=(15/16,1)`; volume comparison at `(g0,g1)=(1/4,1/4)` | `G` |

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

- **PARAMETER** names a free coordinate of Block 211's solved linear system.
  Not a coupling, not a field, not chosen.
- **PARITY** names the even/odd grade pattern of a folded `8 × 8` matrix.
- **CONE** names the zero set of `det M(κ)` as a polynomial identity. Not a
  light cone.
- **LOCUS** and **PLANE** name algebraic subsets of the parameter space given
  by lex Gröbner bases. Not preferred by anything here.
- **BRANCH** names an eigenvalue of `(H0⁻¹ M)²` or `M²`, an exact `8 × 8`
  matrix. Not a propagator, not a continuum limit.
- **REGISTRATION** names an exact nonzero derivative of a polynomial with
  respect to a rational parameter. Not a response of anything physical.
- **FLAT** names `(c, v) = (0, 1)` — the cell whose degree blocks are the
  identity; with a parameter on it is **not** the identity matrix.

### The six scope qualifications, carried as content — each a gated constant, a fence and a mutation

1. **ALL OF IT IS SCOUT-GRADE FINITE EXACT LINEAR ALGEBRA ON ONE CELL FORM,
   NOT A SPACETIME AND NOT A DYNAMICS** — Block 211's fence, inherited verbatim
   through Block 213. Gate `H-1`, mutation `break_scout_grade_fence`.
2. **THE ASSEMBLY IS A SUPPLIED FORK, NOT A RESULT**, and no Hodge reading is
   selected. Gate `H-2`, mutation `claim_assembly_decided`.
3. **NO PARAMETER VALUE IS SELECTED.** The four declared points (`W1` and
   `L+−` with `D16 = 1/4`, with `D07 = 1/4`, and the plane point
   `(D16, D25, D34) = (1/4, −1/4, 1/4)`) are probes. Gate `B-3`, mutation
   `claim_parameter_value_selected`.
4. **THE INSTANCE SCOPE, ENUMERATED.** One bench; one family, seven cone
   witnesses and the flat cell; two assemblies, two readings; the construction
   reconciled at all seven witnesses, with parameterized cone calculations at
   W1 and `L±`; symbolic moduli only for the mechanism and registration;
   generic factorization only at W1, with four named W1 slice eliminants and
   bounded `L±` checks; `m = 0` and
   periodic closure. Gate `H-3`, mutation `break_instance_scope`.
5. **THE VOLUME REGISTRATION IS A STATEMENT ON THE FORMAL BLOCK FAMILY** in
   which volumes, shears and parameters are independent; on Block 211's family
   the volumes are tied to the shears. The #7970 tension is carried, not
   resolved. Gate `G-2`.
6. **THE READINGS ARE READINGS**, six of them, none licensed. Gate `B-5`,
   mutation `claim_readings_licensed`.

### The narrowest true statement, written out so it cannot be paraphrased upward

> On the `(4,2,2)` bench, with Block 213's weighted kernel completed by Block
> 211's cell form with `D07, D16, D25, D34` symbolic: under the onsite assembly
> `M_eo = B` is parameter-free, `M_ee` is the bordering of corner 0 by
> `u = ((D07 + D34) kt, (D25 − D07) kx, (D07 + D16) ky)` and `M_oo` the
> zero-diagonal `[(D16 + D25) kt, (D34 − D16) kx, −(D25 + D34) ky]` on the
> 1-forms; `U = I − (D07/D3) E₇₀` gives `Uᵀ M U = M|₀` and `Uᵀ H0 U = H0|₀`
> with `D0 → D0 − D07²/D3`; `det M` carries no `D07`; `det M = det B²`
> identically in `κ` iff `D16 = D34 = −D25` at `W1` and at the two locus
> witnesses; at generic symbolic W1 parameters `det M` is proportional to
> `Q²`, with `Q = Q0 + Q2` irreducible and `Q2` quadratic in the three
> parameters; the two-quadric
> eliminant is `s²` on the four declared slices at `W1`; the single-quadric system is inconsistent at `W1` under both
> assemblies, and at `L+−`, `L−+` (onsite) `det M` is proportional to
> `(kᵀ G1 k)⁴` along the whole plane, with respective factors `(8/9)²` and
> `(3/4)²`, while the system is inconsistent at `D16 = 1/4`;
> under overlap `H0 = H0(0) + (s/4) P₁₁₁` and `M` depends on `s` alone, with
> the union at `s = 0` only; the flat cell with a parameter on has `H ≠ I`, its
> `det M` is `Q²` with `Q = −|k|⁴ + Q2_flat`, `D07` absent, `Q = −|k|⁴` restored on
> the plane; the pencil branches at the four declared points are the recorded
> literals; on the D07-only degree-diagonal/star line the 0-form branch has the
> displayed rescaling, while the mixed `D07=1/4,D16=1/3` example disproves a
> general isolated-branch inference; at fixed `(v0,v1)=(15/16,1)` neither
> shear derivative is the zero polynomial for any fixed
> `(D16,D25,D34)` (coefficient ideal `(1)`); and at the distinct slice
> `(g0,g1)=(1/4,1/4)` `det M` is proportional to its unit-volume value at zero
> parameters and not with symbolic `D16,D25,D34` on.

### What IS established, stated positively so the fence is not mistaken for a retreat

**The parity lemma and the `D07` congruence are symbolic in all four moduli and
all four parameters.** **The old-union locus is exhaustive at the run witnesses**
by raw-basis containment and power-membership certificates, with the
sufficiency half (`M_oo ≡ 0` on the plane) an identity at symbolic moduli.
**The single-quadric system is closed at W1 for all parameters.** At `L+−` and
`L−+`, only the plane and the declared `D16=1/4` off-point are classified.

---

## Actual runtime and citation closure

- The finite construction and witness facts are cited through the
  [corrected Block 213 paired primary note](ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md),
  and its assembly definitions through the
  [current Block 105 paired primary note](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
  The authority boundary is the
  [minimal axioms note](MINIMAL_AXIOMS_2026-06-29.md). These edges supply no
  action, physical kernel, metric, propagation law, or assembly selector.
- The Block 214 runner imports only the corrected Block 213 runner. The latter
  imports the bounded fixture helper and current Block 105 helper source.
- The fixture helper extracts only the needed Block 201 lane/raising,
  Block 209 corner/exterior, and Block 211 linear-system/triangle/witness
  definitions. It records the original source hashes; the complete original
  bodies and every PR7981/7988 path version remain in the dedicated recovery
  archive.
- The six used Block 105 assembly/Hodge definitions are AST-identical to the
  original source. The current runner and paired note are fixed inputs.
- `docs/MINIMAL_AXIOMS_2026-06-29.md` and
  `docs/audit/data/axiom_premise_nodes.json` are authority inputs only. They
  supply no action, kernel identification, Hodge choice, physical metric,
  propagation law, or assembly selector.
- Both paired notes and both corrected runners are literal cache inputs. The
  runners bind fixed inputs by SHA-256 from actual bytes at source freeze.
- PR #7970 is historical comparison text at its own conditional scope; it is
  not a runtime import or a premise.

---

## No-Go Discipline Gate (N1–N8, at family level)

Every negative below is non-supply within this formalism, never necessity.

### Gate N1 — Alternative routes

The old `det B²` union could survive away from the declared plane/sum at the
run witnesses; raw-basis certificates exclude that route. A different single
quadric is excluded for every parameter at W1 and at the declared L± off-point,
while the remaining L± off-plane locus stays open. `D07` could move `det M`;
the general congruence excludes that route, while its effect on individual
pencil branches is kept separate.

### Gate N2 — Wall independence

The wall is Block 213's `REOPEN` item 7, quoted verbatim in the front matter;
the answers use Block 211's solve with the parameters free and Block 213's
machinery unchanged. No number of Block 213 is reused as a premise for a
parameter-on statement: each is re-derived at the parameter point.

### Gate N3 — Hidden-wall scan

A tolerance would turn the nonzero `Q2` into zero and manufacture the union
everywhere: gate `I-2` counts zero `nsimplify`, zero float literals, zero float
calls. A wrong normalisation in the two-quadric system would hide a
factorization: the `kt⁴` coefficient is checked nonzero before the split.

### Gate N4 — Residual matching (citation table)

| claim | gate | mutation |
| --- | :---: | --- |
| parity mechanism (`M_ee`, `M_oo`) | `F-1` | `break_parity_mechanism` |
| `D07` congruence and `D0` shift | `F-2` | `break_d07_congruence` |
| union locus = the plane / `s = 0` | `F-4` | `break_union_locus` |
| generic W1 quartic squared; four W1 slice eliminants | `F-5`/`F-8` | `break_factorization_type` |
| W1 single-quadric exclusion for all parameters | `F-6` | `claim_single_metric_cone_restored` |
| L± plane persistence and declared off-point exclusion | `F-7` | `break_coincidence_fate` |
| selected branches; D07-only rescaling | `F-9`/`F-10` | `break_pencil_branches` |
| two fixed registration slices | `G-1`/`G-2` | `break_shear_registration`, `claim_volume_blind_under_parameters` |

### Gate N5 — Rhetoric audit at the five resolutions

The fence below is byte-gated (`I-1`, mutation `drop_n5_fence`).

### Gate N6 — Partial-closure paths and the primitive scan

No primitive supplies a parameter value, an assembly or a reading; the plane
and the sum are exhibited, not preferred. Registry check performed before the
wall sentence.

### Gate N7 — Steelman

*"On the plane the cone is parameter-free, so the plane is the natural gauge
slice and the parameters are gauge."* Nothing here establishes a gauge
symmetry: the pencil branches and the form branches **do** move on the plane
(the parameters enter `H0`), and only `det M` is invariant. Reading `R1`.

### Gate N8 — Cross-cycle echo

The old coincidence locus and the **necessary** `D07²<v0/v1` bound reappear:
the old zero set persists on the plane, and the shifted 0-form block
`D0−D07²/D3` changes sign at that D07 boundary. The other separate pairwise
bounds do not characterize the full positive-definite region.

---

## READINGS — six of them, and each is a reading

`READINGS_LICENSED_CLAIMED = False` is a declared constant with a gate (`B-5`).

- **R1** — the parameters are a gauge-like freedom of the cell form. Not
  established: the branches move on the plane; only `det M` is invariant.
- **R2** — the plane `D16 = D34 = −D25` is preferred. Not established: no
  premise here selects it.
- **R3** — `D07` is a 0-form normalisation. A congruence fact, not a physical
  reading: it says what `D07` does to one pencil, and nothing about nature.
- **R4** — the deformed flat cell is a physical vacuum deformation. Not
  established: no dynamics, no vacuum.
- **R5** — the irreducible quartic is a birefringence. Not established: the
  cone is a polynomial identity and names no propagation.
- **R6** — the volume registration through the parameters resolves the #7970
  tension. Not established: it is a formal-family statement and the tension is
  carried, not resolved.

---

## N5 — the fence

```text
N5: NOTHING HERE IS REGISTERED OR ADOPTED. PARAMETER names a free coordinate of the supplied finite cell system; CONE is a determinant zero set; BRANCH is an exact matrix eigenvalue. The open positive-definite duality region is contained in, but is not equal to, the separate pairwise-bound box; pencil statements require actual positive definiteness. The general D07 unipotent congruence preserves det M and inertia and shifts D0 by -D07^2/D3. Its simple zero-form branch rescaling is established only on the D07-only degree-diagonal/star line: the positive-definite mixed D07=1/4,D16=1/3 example has candidate 224/15 residual 528724036/455625. For the actual n=4 block, det[[0,B],[B^T,0]]=det(B)^2; the general sign is (-1)^n. Raw coefficient-ideal bases certify the old det-B union locus at W1 and L+-/L-+ by containment and power membership, without generic factor splitting. The generic W1 determinant is an irreducible quartic squared over the stated rational-function fields; four named W1 slices exclude a product of two quadrics away from their origin, while linear-times-cubic and other specializations remain open. At L+- and L-+ the old single-quadric zero set persists on the declared plane and is excluded only at the tested off-plane D16=1/4 point; the remaining off-plane locus is open. Shear registration fixes (v0,v1)=(15/16,1); volume registration separately fixes (g0,g1)=(1/4,1/4). No action, parameter selector, assembly, physical metric, propagation law, continuum, spacetime cone, dynamics, or gravity is selected or supplied.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **Selecting a parameter value, the plane or the sum.** Stopped: a selector
   is a principle, not a measurement; the plane and `s = 0` are exhibited.
2. **Selecting the assembly or the reading.** Stopped, as in Block 213.
3. **The full three-parameter reducibility locus off the declared slices.**
   Stopped: the thirteen-unknown lex basis did not finish within the budget;
   what is proved is the union locus (exact) and the slices (exact); the
   line-factor test is not run.
4. **Interpreting the branch tables.** Stopped: they are exhibited, not read.
5. **Resolving the #7970 tension.** Stopped: the volume registration through
   the parameters is a formal-family statement; no bridge to the matter side
   is supplied.
6. **Any physical reading.** Stopped: `R1` through `R6` are readings.

### REOPEN IF

1. A framework principle prefers the plane `D16 = D34 = −D25` (onsite) or
   `s = 0` (overlap). The old union identity would then hold on the selected
   positive-definite portion. At `L+−` and `L−+`, the old single-quadric zero
   set also persists on that plane.
2. A framework principle prefers a point off the plane. At generic W1
   parameters the determinant is one irreducible quartic squared; special
   parameter loci beyond the four named slices remain to be classified.
3. A rational witness is found at which the two-quadric eliminant on a
   declared slice is not `s²`. That would contradict `F-8` and would mean an
   arithmetic error here. A line factor off the plane would be new content.
4. The full three-parameter eliminant is computed and finds a component off
   the plane. It would sharpen `N3` without touching the union locus.
5. A principle ties the parameters to the moduli (as the ties fix the volumes
   to the shears). The formal-family registration statements would then have
   to be re-run on the tied family.
6. A bench, closure or mass value is found at which the zero-parameter flat
   control fails. Every result above sits on that control.

---

## N7 — RECOVERY AND CORRECTION RECORD

### Original sources preserved

The complete PR7981 and PR7988 source deltas are recovery inputs, not current
proof authority. All 34 path occurrences, representing 28 unique paths and both
versions of the six shared packet paths, are preserved in
`.claude/science/physics-loops/released7981-7988-recovery-20260910/` as
hash-checked gzip/base64 JSON. The archive also preserves the historical Block
201, 209, 211, and old Block 105 helper bodies. Its verifier checks every
decoded path and aggregate hash.

The original Block 214 cache, scratch, results, checker report, and review prose
remain historical support. Prior `PASS`, `CONFIRM`, or landed-status language is
not a present review or audit verdict and does not validate corrected sources.

### Corrections applied to this recovered note and runner

- The open positive-definite parameter region is contained in the separate
  pairwise-bound box; the exact `-71/240` counterexample prevents identifying
  them.
- The general D07 congruence is retained. Simple 0-form branch rescaling is
  restricted to the D07-only degree-diagonal/star line, and the exact mixed
  counterexample is recorded.
- The block determinant sign is `(-1)^n`; the actual `n=4` result is positive.
- Raw union-ideal bases are retained and certified by containment and power
  membership. No generic factor-splitting radical rule is used.
- Generic W1 factorization, four W1 slice eliminants, W1 all-parameter
  single-quadric exclusion, and the two L± plane/off-point checks are stated as
  distinct results. Other special factorization and L± single-quadric loci stay
  open. Quartic roots are algebraic; the excluded branch is a polynomial
  quadratic-form branch over the stated field.
- Registration uses two distinct formal slices:
  `(v0,v1)=(15/16,1)` for shear and `(g0,g1)=(1/4,1/4)` for volume.

Block 213 is also corrected in this recovery unit: its finite non-scalar witness
scan is retained, its universal curved-overlap claim is removed in light of the
exact positive-definite scalar counterexample, and the L± determinant
proportionality factors `8/9` and `3/4` are restored.

### Runtime binding

The live runner imports the corrected Block 213 runner, which imports the
bounded fixture helper and the current Block 105 source. Both paired notes,
both runners, the fixture helper, current Block 105 runner and note, minimal
axioms, and registry are literal declared inputs. Fixed SHA-256 guards are taken
from actual source bytes at the final source freeze. Fresh bounded producer
evidence is required for these corrected files; the historical caches are not
reused.

```text
python3 scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py
python3 scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py --list-mutations
python3 scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py --mutation break_union_locus
```

This note remains conditional finite matrix mathematics. It registers or adopts
no premise and supplies no action, physical kernel, metric, propagation law,
assembly selector, continuum, spacetime, dynamics, or gravity.
