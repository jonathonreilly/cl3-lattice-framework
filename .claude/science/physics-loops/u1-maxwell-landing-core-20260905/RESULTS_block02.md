# RESULTS — block 02: the #7917 dynamics class against the four axioms

**Runner:** `scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py` (exact integer, rational and symbolic arithmetic; no
float is evidence). **Cache:** `logs/runner-cache/u1_dynamics_class_axiom_adjudication_2026_09_05.txt` (status ok, exit 0,
`TOTAL: PASS=100 FAIL=0`; timeout 900 s declared; one declared input, the axiom memo). **Note:**
`docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md`.

## Verdict table (from the note's section 9)

| item | verdict |
|---|---|
| 1 payload (one real E per edge, one real B per face) | GENUINE SUPPLY (Qubit bounds a linear one-site payload to eight real components) |
| 2 real linear first-order continuous time | GENUINE SUPPLY; memoryless clause DERIVED-CONDITIONAL-ON(SI) |
| 3 nearest-neighbor locality | DERIVED-CONDITIONAL-ON(IP-B), a target-equivalent premise |
| 4 translation + proper-cubic covariance | DERIVED-CONDITIONAL-ON(items 1,3,5,6,7) with orientation only through item 5's own d0/d2 (covariance exhibited for the oriented representation); also DERIVED-CONDITIONAL-ON(LR) |
| 5 gauge + magnetic-Gauss compatibility | DERIVED-CONDITIONAL-ON(items 1,3,4,7 and OL, the vector-type law in the compilation's sign basis); the conclusion is also representation-free through the nullspace theorem |
| 6 positive diagonal energy conserved | GENUINE SUPPLY |
| 7 no vertex/cube/coin/hidden-time payload | GENUINE SUPPLY |

## Review and fix pass (2026-09-05)

Supervisor line-by-line review (hand verification of the stabilizer stencil map, the blockwise conservation equations, the
leapfrog invariant, the momentum-census multiplicities, the cube-connectivity argument): no defects beyond the checker's.
Opus 5 refuting checker (`CHECKER_block02_findings.md`; disjoint machinery: own d0 sign, Levi-Civita curl signs, Fourier
block-diagonalization, brute-force representation enumeration; eighty independent checks; three planted mutations all caught):
verdict FIX FIRST, no verdict in the seven-row table refuted. Findings CK-01..CK-08 were each verified by the supervisor
against the primary surfaces and applied: two PR quotations replaced by the PRs' own sentences (CK-01, CK-02); the sixteen-law
classification scoped to the compilation's sign basis, the sign-relabelled law exhibited as an executed check, and the item-5
conclusion stated as representation-free through the nullspace theorem (CK-03); five executed witness checks added — tick
covariance and per-shear locality, the nonlinear law's locality/gauge/covariance, the complex law's assembled real generator
(CK-04); "no orientation premise" qualified wherever it occurs (CK-05); R1's reversibility sentence narrowed to the
single-site statement, marked not executed (CK-06); the capacity check computed from a real basis and the constructed
generators rather than declared (CK-07); the side-6 gauge-plus-chain nullspace solved in full generality, 324 unknowns
(CK-08). Runner: 95 -> 100 checks (five added, the section-M check rewritten); cache re-pinned on the final runner.

## Mutation checks

Primary's twelve (scratch copies of the 95-check runner inside scripts/, removed afterwards; each detected by the targeted
check family):

| mutation | result |
|---|---|
| axiom sentence altered ("Records form." -> "Records do not form.") | PASS=94 FAIL=1: memo integrity read |
| one curl sign flipped | PASS=65 FAIL=30: chain identities and everything downstream |
| face d-wave character factor dropped | PASS=91 FAIL=4: global-character check, stabilizer, classification |
| metric-skew defect zeroed | PASS=92 FAIL=3: the three item-6 witnesses |
| Gauss-Seidel update sign flipped | PASS=94 FAIL=1: energy decrease |
| modified-energy coefficient h^2/8 -> h^2/4 | PASS=94 FAIL=1: tick conservation |
| quartic energy term dropped | PASS=94 FAIL=1: nonlinear conservation |
| chain constraint disabled in the side-4 nullspace | PASS=94 FAIL=1: nullspace dimension |
| one multiplicity altered | PASS=94 FAIL=1: exact multiplicities |
| stabilizer face sign fixed to +1 | PASS=91 FAIL=4: stabilizer dimensions and stencils |
| support-radius test disabled | PASS=94 FAIL=1: improved-curl radius |
| covariance test disabled | PASS=93 FAIL=2: anisotropic and site-privileging witnesses |

Checker's three (scratch copies with ROOT repointed at the worktree; the repo copy untouched):

| mutation | result |
|---|---|
| face_stencil sign flipped for the z-normal orientation only | PASS=65 FAIL=30: chain identities first, then the classification, Gauss rows and spectrum |
| is_covariant returning True for every translation | PASS=94 FAIL=1: the site-privileging witness (the only check that notices; fail-closed but thin) |
| modified-energy coefficient h^2/8 -> h^2/6 | PASS=94 FAIL=1: tick conservation |

All fifteen mutation counts are at the pre-fix-pass 95-check runner; the fix pass added five checks and rewrote one, and the
three properties the checker found unexecuted (CK-04) are now executed checks.

## What could not be established (honest list)

- No item was derived from the four axioms alone. Every DERIVED-CONDITIONAL verdict rests on a named premise (LR, IP-B, OL,
  SI) or on other items of the class; every GENUINE SUPPLY verdict is a negative at family level with an exact witness.
- Item 3's premise IP-B is target-equivalent (it restates the item for the dynamics); the block sharpens the residual, it does
  not derive locality.
- Item 4's axiom lever LR is a reading of scope ("No site is privileged" binding the dynamical law); it is not forced by the
  Qualification, which permits supplied further structure. Its covariance conclusion is relative to the oriented representation
  that item 5's d0/d2 select.
- Item 6 was not derived and no derivation route was closed as impossible: the reflection-positivity route (N7) is live and
  needs two supplied structures (a path-product transfer interpretation; an evolution axis). The block did not attempt it.
- The finite-size statements are exact on the compiled tori of sides 4, 6, 8; the size-free content is the one-face
  stabilizer argument and the cube-connectivity argument. No infinite-volume, continuum, thermodynamic or Lorentz statement.
- The sampling identification IP-A was executed on the collapsed harmonic edge law (Gauss-Seidel mean map); the exact finite
  auxiliary heat-bath chain of the compiled alphabet (with face auxiliaries) was not executed — the collapsed law is radius two,
  the compiled one is nearest-neighbor by the compilation's own construction. The single-site detailed-balance statement in
  route R1 is stated, not executed.
- No Record readout of E or B, no identification with electromagnetism, no selection among the time-selection fork's branches
  beyond stating which identification premise selects which branch.
- The sixteen-law classification is of signed-permutation representations in the compilation's sign basis; sign relabellings
  are equivalent laws (one is exhibited) and representations that do not act by site permutation were not classified.
- Independence class: single family (Claude), cross-model — Fable primary, Opus 5 refuting checker, supervisor line-by-line
  review with hand verification. Independent audit is still required.

## Full runner output (from the cache, stdout section)

```text
U(1) dynamics class against the four axioms: per-item adjudication (exact)
============================================================================

A. Axiom memo integrity read (the only external input)
------------------------------------------------------
  [PASS] memo carries verbatim: lattice sites
  [PASS] memo carries verbatim: no site privileged
  [PASS] memo carries verbatim: qubit domain
  [PASS] memo carries verbatim: no possibility privileged
  [PASS] memo carries verbatim: one fixed covariant rule
  [PASS] memo carries verbatim: distribution sentence
  [PASS] memo carries verbatim: records form
  [PASS] memo carries verbatim: one record, permanent
  [PASS] memo carries verbatim: readout
  [PASS] memo carries verbatim: law sentence
  [PASS] memo carries verbatim: not a dynamics axiom
  [PASS] memo carries verbatim: no Hamiltonian / time metric
  [PASS] memo carries verbatim: open gates: time
  [PASS] memo carries verbatim: 2026-08-13 removal

B. The supplied compilation: parity roles, doubled incidence (sides 4, 6)
-------------------------------------------------------------------------
  [PASS] side 4: role census vertices/edges/faces/cubes = 8/24/24/8
  [PASS] side 4: edge shell = 2 vertices + 4 faces; face shell = 4 edges + 2 cubes; vertex/cube shells
  [PASS] side 4: no same-role nearest-neighbor pair exists (compilation fact)
  [PASS] side 4: edge-face torus distances are all odd; same-role distances all even (parity theorem)
  [PASS] side 6: role census vertices/edges/faces/cubes = 27/81/81/27
  [PASS] side 6: edge shell = 2 vertices + 4 faces; face shell = 4 edges + 2 cubes; vertex/cube shells
  [PASS] side 6: no same-role nearest-neighbor pair exists (compilation fact)
  [PASS] side 6: edge-face torus distances are all odd; same-role distances all even (parity theorem)
  [PASS] all eight parity translates satisfy the neighbor bit-flip rule (translation permutes sectors)
  [PASS] every proper rotation about every role type maps the role field onto one of the eight sectors
  [PASS] rotations about a vertex or cube site fix the sector (24 each); about an edge or face site exactly 8 do  ({'vertex': 24, 'edge_x': 8, 'face_xy': 8, 'cube': 24})

C. Incidence of the compilation: exact chain identities and covariance
----------------------------------------------------------------------
  [PASS] side 4: C d0 = 0 and d2 C = 0 over the integers
  [PASS] side 4: every face row and every edge column of the oriented curl has entries (+1,+1,-1,-1)
  [PASS] side 4: every curl entry couples a face to a physical nearest-neighbor edge
  [PASS] side 6: C d0 = 0 and d2 C = 0 over the integers
  [PASS] side 6: every face row and every edge column of the oriented curl has entries (+1,+1,-1,-1)
  [PASS] side 6: every curl entry couples a face to a physical nearest-neighbor edge
  [PASS] side 8: C d0 = 0 and d2 C = 0 over the integers
  [PASS] side 8: every face row and every edge column of the oriented curl has entries (+1,+1,-1,-1)
  [PASS] side 8: every curl entry couples a face to a physical nearest-neighbor edge
  [PASS] oriented curl is covariant under all 24 proper rotations about a vertex (vector E, vector B)
  [PASS] unsigned incidence is covariant under all 24 proper rotations (scalar E, scalar B)
  [PASS] oriented gradient d0 is covariant under all 24 proper rotations (scalar vertex payload)
  [PASS] all 16 signed-permutation payload representations are genuine group representations (composition law on 24 x 24 pairs)
  [PASS] the second character factor is one global sign character of the rotation group (parity of the axis permutation), the same for every edge and face
  [PASS] oriented curl is covariant under all eight even translations of the side-4 torus

D. One-face stabilizer: the 90-degree rotation about a face-role site
---------------------------------------------------------------------
  [PASS] the sector-preserving stabilizer of a face-role site has exactly eight proper rotations (D_4), all named by the Lattice axiom
  [PASS] one-face stabilizer: a covariant boundary stencil exists (and is unique up to scale) exactly when the edge and face characters agree on the in-plane 180-degree flip (8 of 16)  ({((0, 0), (0, 0)): 1, ((0, 0), (0, 1)): 1, ((0, 0), (1, 0)): 0, ((0, 0), (1, 1)): 0, ((0, 1), (0, 0)): 1, ((0, 1), (0, 1)): 1, ((0, 1), (1, 0)): 0, ((0, 1), (1, 1)): 0, ((1, 0), (0, 0)): 0, ((1, 0), (0, 1)): 0, ((1, 0), (1, 0)): 1, ((1, 0), (1, 1)): 1, ((1, 1), (0, 0)): 0, ((1, 1), (0, 1)): 0, ((1, 1), (1, 0)): 1, ((1, 1), (1, 1)): 1})
  [PASS] one-face stabilizer: characters ((1, 0), (1, 0)) force the stencil (1, 1, -1, -1) up to scale  (['-1', '-1', '1', '1'])
  [PASS] one-face stabilizer: characters ((0, 0), (0, 0)) force the stencil (1, 1, 1, 1) up to scale  (['1', '1', '1', '1'])
  [PASS] gauge invariance on one face star (own row reduction): the invariant stencils are exactly the curl multiples (1,1,-1,-1)
  [PASS] the eight compatible character pairs give exactly four distinct one-face stencils (each shared by a pair related by the global sign twist)  ({('1', '1', '1', '1'): [((0, 0), (0, 0)), ((0, 1), (0, 1))], ('1', '-1', '1', '-1'): [((0, 0), (0, 1)), ((0, 1), (0, 0))], ('1', '1', '-1', '-1'): [((1, 0), (1, 0)), ((1, 1), (1, 1))], ('1', '-1', '-1', '1'): [((1, 0), (1, 1)), ((1, 1), (1, 0))]})
  [PASS] exactly the vector/vector pair and its global sign twist give the gauge-invariant curl stencil; the other three stencils fail gauge invariance

E. Exact covariant classification of nearest-neighbor real linear generators (side 4)
-------------------------------------------------------------------------------------
  [PASS] scalar/scalar characters: covariant generators = span{onsite E, onsite B, unsigned incidence, its transpose} exactly
  [PASS] vector/vector characters: covariant generators = span{onsite E, onsite B, curl, curl^T} exactly
  [PASS] all 16 payload representations: rotated patterns stay in the 30-pattern span; onsite terms always covariant; one coupling direction iff the flip characters agree
  [PASS] covariant nearest-neighbor generator space has dimension 4 for the 8 compatible character pairs and 2 for the 8 incompatible pairs  ({((0, 0), (0, 0)): 4, ((0, 0), (0, 1)): 4, ((0, 0), (1, 0)): 2, ((0, 0), (1, 1)): 2, ((0, 1), (0, 0)): 4, ((0, 1), (0, 1)): 4, ((0, 1), (1, 0)): 2, ((0, 1), (1, 1)): 2, ((1, 0), (0, 0)): 2, ((1, 0), (0, 1)): 2, ((1, 0), (1, 0)): 4, ((1, 0), (1, 1)): 4, ((1, 1), (0, 0)): 2, ((1, 1), (0, 1)): 2, ((1, 1), (1, 0)): 4, ((1, 1), (1, 1)): 4})
  [PASS] the 8 compatible pairs carry exactly 4 distinct couplings (up to sign): the curl, the unsigned incidence, and their two sign-twisted partners
  [PASS] exactly the curl is gauge- and chain-compatible (X d0 = 0, d2 X = 0): the vector/vector pair and its global sign twist; the other three couplings are not
  [PASS] with a scalar vertex payload: covariant nearest-neighbor generators = span{onsite x3, curl, curl^T, d0, d0^T} (dim 7)  (dim=7)

F. Item 6 inside the covariant family: conservation is a two-condition cut (side 6)
-----------------------------------------------------------------------------------
  [PASS] symbolic: positive diagonal conservation <=> u = 0, v = 0, w_E r + w_B q = 0 (blockwise metric-skew equations)
  [PASS] Maxwell member (u=v=0, r=-q): exact metric-skew defect zero; dH/dt = 0 on a random rational field
  [PASS] per-site energy (1/2)E_e^2 is NOT conserved by the Maxwell member while the lattice-wide sum is
  [PASS] both Gauss rows are exactly preserved by the Maxwell member (d0^T dE/dt = 0, d2 dB/dt = 0)
  [PASS] side 6: the edge operator C^T C satisfies Q(Q-3)(Q-6)(Q-9) = 0 exactly (spectrum in {0,3,6,9})
  [PASS] side 6: exact multiplicities of C^T C are {0:29, 3:12, 6:24, 9:16} = two transverse branches per nonzero momentum  ({0: 29, 3: 12, 6: 24, 9: 16})
  [PASS] side 6: C C^T has the same nonzero multiplicities (frequency^2 spectrum of the conservative law)  ({0: 29, 3: 12, 6: 24, 9: 16})
  [PASS] side 6: 52 = 2 x 26 nonzero momenta transverse modes; the 29 zero modes are 26 gradients + 3 harmonic
  [PASS] witness damped (u=v=-1/3): nearest-neighbor, covariant, edge-to-face block gauge-compatible, minimal payload
  [PASS] witness damped (u=v=-1/3): violates item 6 (no positive diagonal conserved energy; dH/dt or trace nonzero)  (dH/dt=-766661/1200, trace=-54)
  [PASS] witness overdamped (u=0, v=-2, q=2, r=-1): nearest-neighbor, covariant, edge-to-face block gauge-compatible, minimal payload
  [PASS] witness overdamped (u=0, v=-2, q=2, r=-1): violates item 6 (no positive diagonal conserved energy; dH/dt or trace nonzero)  (dH/dt=-321641/200, trace=-162)
  [PASS] witness same-sign (r=+q): nearest-neighbor, covariant, edge-to-face block gauge-compatible, minimal payload
  [PASS] witness same-sign (r=+q): violates item 6 (no positive diagonal conserved energy; dH/dt or trace nonzero)  (dH/dt=-18529/900, trace=0)
  [PASS] same-sign witness: G^2 = diag(C^T C, C C^T) has eigenvalue 9 > 0, so G has real eigenvalues (no conserved positive form)
  [PASS] overdamped witness per mode: characteristic polynomial lambda^2 + gamma lambda + gamma s^2; slow root = -s^2 - s^4/gamma + ... (diffusive)
  [PASS] Maxwell per mode: eigenvalues +/- i s (propagating at unit speed), not diffusive

G. The sampling identification of the dynamics lands on dissipation (side 6)
----------------------------------------------------------------------------
  [PASS] Gauss-Seidel sweep of single-site conditional means of the harmonic static law strictly decreases (1/2) A^T C^T C A  (5541407/3600 -> 355337281288581238828593429634585659772720318473928807/2630702947195625252766632698889309435380678577356800)
  [PASS] the conditional-mean map on the edge field alone reads edges at physical distance 2 (collapsed payload is not nearest-neighbor)

H. Item 5 witness: the unoriented covariant law (side 6)
--------------------------------------------------------
  [PASS] unoriented law: nearest-neighbor, covariant (unoriented representation), conserves (1/2)(|E|^2+|B|^2), minimal payload
  [PASS] unoriented law violates item 5: S d0 != 0 and d2 S != 0 over the integers
  [PASS] unoriented law has no soft mode at zero momentum: S maps the three constant edge fields to independent faces (rank 3), while the curl kills them
  [PASS] sign-relabelled oriented law (payload negated at every z-normal face): a signed-permutation representation with the same site action, distinct from all sixteen tensor-transport laws; the generator it makes covariant has edge-to-face block D C with D C d0 = 0 but d2 D C != 0 — OL's convention clause (the compilation's own sign basis) is load-bearing

I. Item 4 witnesses (side 6)
----------------------------
  [PASS] anisotropic law (orientation coefficients 1,2,3): nearest-neighbor, conservative, gauge-invariant (L d0 = 0), NOT covariant, and NOT magnetic-Gauss preserving (d2 L != 0)
  [PASS] side 4: nearest-neighbor face rows with L d0 = 0 and d2 L = 0 form exactly the one-dimensional space spanned by the oriented curl (no covariance assumed)
  [PASS] side 6 in full generality (324 free boundary-edge coefficients, no per-face reduction): the gauge-plus-chain nullspace is one-dimensional and spanned by the oriented curl
  [PASS] side 6: with each face row a multiple q_f of its curl, d2 L = 0 forces q_f constant over all 81 faces (nullspace dimension 1, the all-ones vector)
  [PASS] consequence: items 1,3,5,6,7 force the generator to c[[0,-C^T],[C,0]] after normalization, which is covariant; item 4 is implied by the other items
  [PASS] site-privileging law (one face row doubled): conservative, nearest-neighbor, gauge-compatible, but NOT translation covariant

J. Item 3 witness: improved curl of physical radius three (side 8)
------------------------------------------------------------------
  [PASS] improved-curl law L = C(1 + eps C^T C): conservative, gauge-compatible (L d0 = 0, d2 L = 0), covariant, minimal payload
  [PASS] improved-curl law violates item 3: its support radius on the side-8 torus is exactly 3 (edge-face couplings occur only at odd distance)

K. Item 7 witness: a scalar vertex payload (side 6)
---------------------------------------------------
  [PASS] vertex-scalar law: dH/dt = 0 for H = (1/2)(|phi|^2+|E|^2+|B|^2); nearest-neighbor (a vertex reads its six edges); covariant
  [PASS] vertex-scalar law spectrum: -G^2 on edges is the Hodge Laplacian with multiplicities {0:3, 3:18, 6:36, 9:24} = three branches per nonzero momentum  ({0: 3, 3: 18, 6: 36, 9: 24})
  [PASS] with a vertex payload the conservative covariant class has two independent speeds (a=-2,a2=2 also conserves H): uniqueness up to one speed needs item 7
  [PASS] symbolic: the extended conservative family has two free ratios (a2 = -w_V a / w_E, r = -w_B q / w_E), i.e. two speeds

L. Item 2 witnesses: finite tick, nonlinear constitutive law; item 1 witness: complex payload (side 6)
------------------------------------------------------------------------------------------------------
  [PASS] finite tick h=1/2: exactly reversible (U(-h) U(h) = identity on a random rational field)
  [PASS] finite tick: each shear preserves its Gauss row exactly (d2 B after the half shears; d0^T E after the full shear)
  [PASS] finite tick: conserves the modified energy H_h = |B|^2/2 + |E|^2/2 - (h^2/8)|C E|^2 exactly; H_h > 0 since spec(C^T C) <= 9 < 4/h^2 = 16
  [PASS] finite tick: not a continuous-time law (the one-tick map differs from exp(h G) at order h^3: E-block of U(h) has a nonzero h^2 C^T C term)
  [PASS] finite tick: covariant under all 24 proper rotations (oriented representation); each shear reads one site and its four opposite-role nearest neighbors only (one edge moves exactly its four faces, one face exactly its four edges, all at physical distance 1)
  [PASS] nonlinear constitutive law dE/dt = -C^T(B + eps B^3), dB/dt = C E: conserves the positive energy |E|^2/2 + |B|^2/2 + (eps/4)|B|^4 exactly
  [PASS] nonlinear constitutive law: violates linearity (rate not homogeneous of degree one)
  [PASS] nonlinear constitutive law: nearest-neighbor (one face moves exactly its four boundary edges' rates, one edge exactly its four faces', all at distance 1), gauge-compatible (dB/dt invariant under E -> E + d0 lambda), covariant under all 24 proper rotations
  [PASS] complex two-component law with onsite phase theta: conserves sum |E|^2 + |B|^2 exactly; the onsite phase couples the two real components of every site (violates item 1: two real components per site)
  [PASS] complex law: real generator exactly antisymmetric, support radius 1, covariant under the doubled oriented representation, and its edge-to-face blocks are exactly C (gauge- and chain-compatible)

M. Qubit capacity bound on linear one-site coordinates
------------------------------------------------------
  [PASS] dim_R M_2(C) = 8 (rank of the real coordinate basis): every witness payload fits, with components per site read off the constructed generators (1, 1, 2, 1); a nine-component linear payload cannot  ({'Maxwell member': 1, 'vertex-scalar law': 1, 'complex law': 2, 'finite tick / nonlinear law': 1})

N. Resolution certificate
-------------------------
per_element: executed — every coefficient of the 30-pattern (43 with vertex payload) translation-covariant nearest-neighbor generator basis is classified exactly under all 24 proper rotations for each orientation law
per_site: executed — every site of the side-4, side-6 and side-8 compiled tori is role-censused, and per-site field energy is shown not conserved by the conservative law while the lattice-wide sum is
per_mode: executed — exact eigenvalue multiplicities of the edge, face and Hodge Laplacians on the side-6 torus certify two transverse branches per nonzero momentum and a third branch for the vertex-scalar witness; symbolic per-mode roots for the overdamped witness
per_block: executed — the edge, face and vertex blocks of every witness generator are checked separately for skewness, Gauss rows, chain identities and orientation covariance
lattice_wide: executed — every witness law is assembled as a full generator on the side-6 or side-8 torus where its conservation, covariance, support radius and gauge compatibility are decided exactly; no infinite-volume or continuum statement is executed

TOTAL: PASS=100 FAIL=0
```
