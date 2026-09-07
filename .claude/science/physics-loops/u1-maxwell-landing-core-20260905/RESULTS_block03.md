# RESULTS — block 03: the Gauss rows as support forcing on the extended (phi, E, B, psi) payload class

**Runner:** `scripts/u1_gauss_support_forcing_extended_class_2026_09_05.py` (exact integer, rational and symbolic arithmetic; no
float is evidence). **Cache:** `logs/runner-cache/u1_gauss_support_forcing_extended_class_2026_09_05.txt` (status ok, exit 0,
`TOTAL: PASS=89 FAIL=0`, elapsed 49.7 s; timeout 900 s declared; one declared input, the axiom memo; runner sha256
`119500b23fbe32ba50501594463254580d7f3943fb812d520dd770f2ce697080`). **Note:**
`docs/U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md`.

## Obligation table (from the note's result-up-front)

| obligation (item 7 of the declared class) | verdict |
|---|---|
| no vertex payload participates | DERIVED-CONDITIONAL-ON(SF-all on the electric row, EC, CONS): frozen and decoupled in every charge sector; decoupled-only under (SF-all, EC); sector-inert under (SF-0, EC), with no invariant subset of any charged surface |
| no cube payload participates | the same via the magnetic row, by the odd-shift self-duality and by independent execution |
| no extra coin participates | GENUINE SUPPLY: the sixteen-dimensional coin class has a six-parameter conservative cut; the rows cut it to four (the onsite mixings), never to zero; witnesses: the complex law (zero-charge rows preserved; kernel dimension 0 against 116) and the K (x) C law (every charged surface preserved) |
| no hidden time payload participates | GENUINE SUPPLY, coextensive with the coin at the linear level: z1'' = 2 G z1' - (G^2 + theta^2) z1 exactly; the auxiliary pair is the velocity; G^2 has radius 2 |

## The collapse theorem, exactly

For every member of the ten-parameter class: d/dt(d0^T E) = a2 (d0^T d0) phi + u_E (d0^T E) and d/dt(d2 B) = b (d2 d2^T) psi + u_B (d2 B)
(the coupling blocks d0^T C^T and d2 C vanish identically — the chain identities). The electric surface {d0^T E = rho_V} is
invariant iff a2 = 0 and u_E rho_V = 0 (phi is free on the surface and d0^T d0 != 0); the magnetic surface iff b = 0 and
u_B rho_C = 0. With positive-diagonal conservation, a2 = 0 iff a = 0 and b = 0 iff b2 = 0, so the invariant conservative members are
exactly the one-speed edge/face law with d phi/dt = d psi/dt = 0 identically. Executed on sides 4 and 6.

## Branch count on the Gauss sector (side 6)

Full space, three-speed member (a=-2, a2=2, q=1, r=-1, b=-3, b2=3): E-block of -G^2 = 4 d0 d0^T + C^T C with multiplicities
{0:3, 3:12, 6:24, 9:16, 12:6, 24:12, 36:8}; B-block {0:3, 3:12, 6:24, 9:16, 27:6, 54:12, 81:8}. Gauss sector: C^T C on ker d0^T
{0:3, 3:12, 6:24, 9:16} (sum 55) and C C^T on ker d2 the same: two transverse branches per nonzero momentum (52 = 2 x 26), the
longitudinal (26 = 6 + 12 + 8) and cube branches absent, 3 + 3 harmonic zero modes plus two frozen constants. Sector dimension
112 on side 6 (36 on side 4); electric-only maximal invariant subspace 164 (50).

## Mutation checks

Fourteen probes on scratch copies of the final runner (`/private/tmp/.../scratchpad/mut/`, `ROOT` repointed at the worktree; the
repo copy untouched); every probe exits 1; the check family targeted is in parentheses.

| mutation | result | first failing check |
|---|---|---|
| M01 axiom sentence altered ("locks exactly one" -> "two") (A) | PASS=88 FAIL=1 | memo carries verbatim: records lock one admissible possibility |
| M02 one curl sign flipped (E_j at x + e_i) (B) | PASS=49 FAIL=40 | side 4: chain identities C d0 = 0 and d2 C = 0 |
| M03 z-faces dropped from d2 (B) | PASS=59 FAIL=30 | side 4: chain identities |
| M04 face payload made scalar in the rotation law (C) | PASS=81 FAIL=8 | d0, C and d2 covariant under all 24 rotations |
| M05 classification under one rotation only (D) | PASS=86 FAIL=3 | side 4: covariant class = span{...} (dimension 10) |
| M06 conservation cut sign (w_V a - w_E a2) (E) | PASS=88 FAIL=1 | symbolic conservation cut |
| M07 metric-skew defect zeroed (E) | PASS=88 FAIL=1 | the broken member has nonzero defect |
| M08 electric rate computed with the unsigned divergence (F) | PASS=84 FAIL=5 | d/dt(d0^T E) coefficient-wise identity |
| M09 edge-from-vertex coupling a2 made inert (G) | PASS=76 FAIL=13 | three-speed member conserves (E), then the collapse checks |
| M10 observability stack stops early (H) | PASS=83 FAIL=6 | side 4: maximal invariant subspace dimension |
| M11 restricted-multiplicity sign (I) | PASS=87 FAIL=2 | Gauss sector E-part multiplicities |
| M12 coin phase theta = 0 (J) | FAIL at the kernel-dimension check, then ZeroDivisionError at the hidden-time reconstruction (exit 1) | ker G_theta = 0 against 116 |
| M13 second-order coefficient 2 -> 1 (K) | PASS=88 FAIL=1 | z1'' identity |
| M14 magnetic rate read off the edge rows (F/L) | PASS=83 FAIL=6 | d/dt(d0^T E) / d/dt(d2 B) identities, then section L |

Independent-math checks against the runner (by hand): the blockwise skew equations; the rate identity via (C d0)^T = 0; the
odd-shift conjugation signs on one face and one edge; the unobservable-subspace chain P G x = a2 L phi, P G^2 x = a a2 L d0^T E,
P G^3 x = a a2^2 L^2 phi; the side-6 multiplicities from the coarse momentum census; the coin cut 16 - 10 = 6; the second-order
identity by substitution.

## What could not be established (honest list)

- No Gauss row, no item of the declared class, and no clause of item 7 is derived from the four axioms alone. The vertex/cube
  verdict is conditional on the supplied rows read as support forcing (their shape is Admissibility's support clause; their
  content and background charges are supplied), on the class's other items (EC, with the orientation law OL) and on conservation.
- The reading of "support forcing" is a choice: SF-all (every charged surface invariant) gives a coefficient statement (a2 = 0,
  b = 0); SF-0 (a consistent restriction) gives a sector statement (phi, psi constant and inert). Both were executed; the note
  states both; neither is derived from the axioms.
- The coin clause was not derived and no derivation route was closed as impossible: the one-component clause's only axiom contact
  is Qubit's capacity bound (eight real components per site, block 02), and the readout bridge (N7) is the live route.
- The complex law "preserves both Gauss rows" only at zero charge; on a charged surface the two-component charge rotates. The
  pack's contract carried the unqualified statement; this block corrects it.
- The finite-size statements are exact on the compiled tori of sides 4 and 6; the size-free content is the chain identities, the
  odd-shift duality, connectedness of the even torus and the block structure of -G^2. The classification's constraint system is the
  same linear system at both executed sides; no other size was executed. No infinite-volume, continuum, thermodynamic or Lorentz
  statement.
- No Record readout of phi, E, B or psi; no identification with electromagnetism; no statement about the compact, interacting or
  spin-half carriers of the lane's other members.
- The refuting checker seat has not run; independence class to be filled by the supervisor. Independent audit is still required.
- Quote-fidelity finding (outside this block's file set): the ledger's row 4 and GOAL_block03.md attribute "order-independent
  site-level support forcing among corner records" to open PR #7893; the live body (2026-09-05) and the head-branch note do not
  contain it. Carried to the supervisor; this block quotes the body's own sentence.

## Full runner output (from the cache, stdout section)

```text
U(1) light lane: the Gauss rows as support forcing on the extended (phi, E, B, psi) payload class (exact)
============================================================================================================

A. Axiom memo integrity read (the only external input)
------------------------------------------------------
  [PASS] memo carries verbatim: lattice sites
  [PASS] memo carries verbatim: no site privileged
  [PASS] memo carries verbatim: qubit domain
  [PASS] memo carries verbatim: no possibility privileged
  [PASS] memo carries verbatim: one fixed covariant rule
  [PASS] memo carries verbatim: distribution sentence
  [PASS] memo carries verbatim: support reading note
  [PASS] memo carries verbatim: records lock one admissible possibility
  [PASS] memo carries verbatim: one record, permanent
  [PASS] memo carries verbatim: readout
  [PASS] memo carries verbatim: qualification: further structure
  [PASS] memo carries verbatim: law sentence
  [PASS] memo carries verbatim: not a dynamics axiom
  [PASS] memo carries verbatim: no Hamiltonian / time metric
  [PASS] memo carries verbatim: 2026-08-05 availability as support

B. The supplied compilation, rebuilt from the parity rule (sides 4 and 6)
-------------------------------------------------------------------------
  [PASS] side 4: role census vertices/edges/faces/cubes = 8/24/24/8; state dimension 64
  [PASS] side 4: shells -- vertex: 6 edges; edge: 2 vertices + 4 faces; face: 4 edges + 2 cubes; cube: 6 faces; no same-role neighbor
  [PASS] side 4: parity theorem -- torus distance is odd exactly between roles of opposite parity (vertex-edge, edge-face, face-cube, vertex-cube)
  [PASS] side 4: chain identities C d0 = 0 and d2 C = 0 over the integers
  [PASS] side 4: d0 rows (+1,-1), curl rows (+1,+1,-1,-1), d2 rows (three +1, three -1); every incidence entry at physical distance 1
  [PASS] side 4: connectedness lever -- ker(d0^T d0) and ker(d2 d2^T) are exactly the constants (dimension 1 each); rank d0 = 7, rank d2 = 7
  [PASS] side 4: sum rules d0 1 = 0 and d2^T 1 = 0 -- every electric charge d0^T E and every magnetic charge d2 B sums to zero
  [PASS] side 4: d0^T E = rho is solvable for a zero-sum dipole charge and unsolvable for a unit monopole (image of d0^T = zero-sum vectors, by connectedness)
  [PASS] side 4: odd-shift self-duality -- the translation by (1,1,1) maps roles V->C, E->F, F->E, C->V and conjugates (d0, C, d2) to (-d2^T, C^T, -d0^T) exactly
  [PASS] side 6: role census vertices/edges/faces/cubes = 27/81/81/27; state dimension 216
  [PASS] side 6: shells -- vertex: 6 edges; edge: 2 vertices + 4 faces; face: 4 edges + 2 cubes; cube: 6 faces; no same-role neighbor
  [PASS] side 6: parity theorem -- torus distance is odd exactly between roles of opposite parity (vertex-edge, edge-face, face-cube, vertex-cube)
  [PASS] side 6: chain identities C d0 = 0 and d2 C = 0 over the integers
  [PASS] side 6: d0 rows (+1,-1), curl rows (+1,+1,-1,-1), d2 rows (three +1, three -1); every incidence entry at physical distance 1
  [PASS] side 6: connectedness lever -- ker(d0^T d0) and ker(d2 d2^T) are exactly the constants (dimension 1 each); rank d0 = 26, rank d2 = 26
  [PASS] side 6: sum rules d0 1 = 0 and d2^T 1 = 0 -- every electric charge d0^T E and every magnetic charge d2 B sums to zero
  [PASS] side 6: d0^T E = rho is solvable for a zero-sum dipole charge and unsolvable for a unit monopole (image of d0^T = zero-sum vectors, by connectedness)
  [PASS] side 6: odd-shift self-duality -- the translation by (1,1,1) maps roles V->C, E->F, F->E, C->V and conjugates (d0, C, d2) to (-d2^T, C^T, -d0^T) exactly

C. Covariance of the compilation under the oriented four-role law (side 4)
--------------------------------------------------------------------------
  [PASS] d0, C and d2 are each covariant under all 24 proper rotations about a vertex (phi scalar, E vector-along-axis, B vector-along-normal, psi scalar)
  [PASS] the four-role oriented law is a genuine signed-permutation representation of the rotation group (composition law on all 24 x 24 pairs)
  [PASS] d0, C and d2 are covariant under all seven nontrivial even translations of the side-4 torus

D. Exact classification of covariant nearest-neighbor generators on the four-role payload (sides 4 and 6)
---------------------------------------------------------------------------------------------------------
  [PASS] side 4: the translation-covariant nearest-neighbor pattern basis has 56 patterns and every rotated pattern stays in its span  (patterns=56)
  [PASS] side 4: covariant class on (phi, E, B, psi) = span{onsite x4, d0, d0^T, C, C^T, d2, d2^T} exactly (nullspace dimension 10 under all 24 rotations; all ten expected members inside; their rank is 10)  (dim=10)
  [PASS] side 4: a generic member of the ten-parameter class is covariant under all 24 rotations and all 7 nontrivial even translations, and has support radius exactly 1
  [PASS] side 6: the translation-covariant nearest-neighbor pattern basis has 56 patterns and every rotated pattern stays in its span  (patterns=56)
  [PASS] side 6: covariant class on (phi, E, B, psi) = span{onsite x4, d0, d0^T, C, C^T, d2, d2^T} exactly (nullspace dimension 10 under all 24 rotations; all ten expected members inside; their rank is 10)  (dim=10)
  [PASS] side 6: a generic member of the ten-parameter class is covariant under all 24 rotations and all 26 nontrivial even translations, and has support radius exactly 1

E. Positive-diagonal conservation on the class: the symbolic cut (three free speeds)
------------------------------------------------------------------------------------
  [PASS] symbolic: positive diagonal conservation <=> u_V = u_E = u_B = u_C = 0, a2 = -w_V a / w_E, r = -w_B q / w_E, b2 = -w_B b / w_C (three free coupling scales a, q, b)
  [PASS] the block reduction is exact because d0^T, C^T and d2^T are nonzero matrices (a scalar multiple of one vanishes iff the scalar does)
  [PASS] side 6: the three-speed member (a=-2, a2=2; q=1, r=-1; b=-3, b2=3) has metric-skew defect zero and dH/dt = 0 exactly on a random rational state
  [PASS] side 6: a member violating one cut condition (w_V a + w_E a2 = -1 != 0) has nonzero defect and dH/dt != 0

F. The Gauss rates as exact linear functionals, coefficient by coefficient (side 6)
-----------------------------------------------------------------------------------
  [PASS] d/dt(d0^T E) = a2 (d0^T d0) phi + u_E (d0^T E) exactly: the contribution of r is d0^T C^T = 0, and a, u_V, q, u_B, b, b2, u_C contribute nothing (all ten unit members)
  [PASS] d/dt(d2 B) = b (d2 d2^T) psi + u_B (d2 B) exactly: the contribution of q is d2 C = 0, and the other coefficients contribute nothing (all ten unit members)
  [PASS] side 6: the vertex Laplacian d0^T d0 and the cube Laplacian d2 d2^T are nonzero (rank 26 each), so a2 (d0^T d0) = 0 iff a2 = 0 and b (d2 d2^T) = 0 iff b = 0

G. The collapse theorem: which members leave the Gauss surfaces invariant (sides 4 and 6)
-----------------------------------------------------------------------------------------
  [PASS] side 4: the three-speed member does NOT preserve the electric surface: a zero-charge state with phi = delta (E = B = psi = 0) has d/dt(d0^T E) = 2 (d0^T d0) delta != 0
  [PASS] side 4: nor the magnetic surface: psi = delta (phi = E = B = 0) has d/dt(d2 B) = -3 (d2 d2^T) delta != 0
  [PASS] side 4: the one-speed member (a = a2 = b = b2 = 0) has BOTH rate functionals identically zero (every state, every background charge): both surfaces invariant
  [PASS] side 4: under the one-speed member d phi/dt = 0 and d psi/dt = 0 identically -- the vertex and cube payloads are frozen at every state, on and off the surfaces
  [PASS] side 6: the three-speed member does NOT preserve the electric surface: a zero-charge state with phi = delta (E = B = psi = 0) has d/dt(d0^T E) = 2 (d0^T d0) delta != 0
  [PASS] side 6: nor the magnetic surface: psi = delta (phi = E = B = 0) has d/dt(d2 B) = -3 (d2 d2^T) delta != 0
  [PASS] side 6: the one-speed member (a = a2 = b = b2 = 0) has BOTH rate functionals identically zero (every state, every background charge): both surfaces invariant
  [PASS] side 6: under the one-speed member d phi/dt = 0 and d psi/dt = 0 identically -- the vertex and cube payloads are frozen at every state, on and off the surfaces
  [PASS] side 6: a member with a2 = 0, b = 0 and u_E = u_B = 0 but every other coefficient nonzero (a, q, r, b2, u_V, u_C) has both rate functionals identically zero -- invariance needs only a2 = 0 / b = 0 (plus u_E rho_V = 0 / u_B rho_C = 0)
  [PASS] symbolic: on the conservative subfamily a2 = -w_V a / w_E and b2 = -w_B b / w_C with positive weights, so a2 = 0 <=> a = 0 and b = 0 <=> b2 = 0: the invariant conservative members are exactly the one-speed edge/face law with frozen phi and psi
  [PASS] side 6, non-conservative member a2 = 0, a = 3/2 on a charged surface (dipole rho_V): d phi/dt = a rho_V exactly and d^2 phi/dt^2 = 0 -- the vertex payload drifts linearly in time by a multiple of the charge; in the zero-charge sector it is frozen
  [PASS] side 6: a member with u_E = -1/3 (a2 = 0) preserves the zero-charge electric surface but not a charged one: the rate on the dipole surface is u_E rho_V != 0 (the charge decays)

H. The Gauss sector of a non-preserving member: the maximal invariant subspace (sides 4 and 6)
----------------------------------------------------------------------------------------------
  [PASS] side 4: the maximal invariant subspace of the three-speed member inside the zero-charge electric surface is exactly {d0^T E = 0, phi constant} (dimension 50; stabilizes after 2 steps)  (dim=50)
  [PASS] side 4: with both rows, the Gauss sector of the three-speed member is exactly {d0^T E = 0, d2 B = 0, phi constant, psi constant} (dimension 36)  (dim=36)
  [PASS] side 4: the flow maps the Gauss sector into itself, the three-speed and one-speed members agree on it as linear maps (the vertex and cube couplings are invisible there), and phi, psi have zero rate on it (frozen constants)
  [PASS] side 4: for the three-speed member the states whose electric charge is constant in time are exactly {phi constant, d0^T E = 0} (exact unobservable subspace of (QG, G)); their charge is zero, so a charged surface (dipole rho_V) contains NO invariant subset, while the one-speed member preserves the whole charged surface
  [PASS] side 6: the maximal invariant subspace of the three-speed member inside the zero-charge electric surface is exactly {d0^T E = 0, phi constant} (dimension 164; stabilizes after 2 steps)  (dim=164)
  [PASS] side 6: with both rows, the Gauss sector of the three-speed member is exactly {d0^T E = 0, d2 B = 0, phi constant, psi constant} (dimension 112)  (dim=112)
  [PASS] side 6: the flow maps the Gauss sector into itself, the three-speed and one-speed members agree on it as linear maps (the vertex and cube couplings are invisible there), and phi, psi have zero rate on it (frozen constants)
  [PASS] side 6: for the three-speed member the states whose electric charge is constant in time are exactly {phi constant, d0^T E = 0} (exact unobservable subspace of (QG, G)); their charge is zero, so a charged surface (dipole rho_V) contains NO invariant subset, while the one-speed member preserves the whole charged surface

I. Branch count on the Gauss sector, side 6 (exact multiplicities)
------------------------------------------------------------------
  [PASS] -G^2 of the three-speed member is block diagonal by the chain identities: E-block 4 d0 d0^T + C^T C, B-block C C^T + 9 d2^T d2, phi-block 4 d0^T d0, psi-block 9 d2 d2^T
  [PASS] full space, E-block: multiplicities {0:3, 3:12, 6:24, 9:16, 12:6, 24:12, 36:8} (sum 81 = all eigenvalues of a symmetric matrix): two transverse branches at speed 1 (52 = 2 x 26) and one longitudinal branch at speed 2 (26 = 6+12+8, one per nonzero momentum)  ({0: 3, 3: 12, 6: 24, 9: 16, 12: 6, 24: 12, 36: 8})
  [PASS] full space, B-block: multiplicities {0:3, 3:12, 6:24, 9:16, 27:6, 54:12, 81:8}: the cube coupling adds a third branch at speed 3 on the face side  ({0: 3, 3: 12, 6: 24, 9: 16, 27: 6, 54: 12, 81: 8})
  [PASS] Gauss sector (d0^T E = 0), E-part: C^T C has multiplicities {0:3, 3:12, 6:24, 9:16} on it (sum 55 = dim ker d0^T): exactly two transverse branches per nonzero momentum, the longitudinal branch absent, three harmonic zero modes  ({0: 3, 3: 12, 6: 24, 9: 16})
  [PASS] Gauss sector (d2 B = 0), B-part: C C^T has the same multiplicities {0:3, 3:12, 6:24, 9:16} on it (sum 55)  ({0: 3, 3: 12, 6: 24, 9: 16})
  [PASS] the sector spectrum does not depend on the vertex and cube speeds: the E-block of -G^2 restricted to ker d0^T equals C^T C there (4 d0 d0^T vanishes on ker d0^T), i.e. the three-speed and one-speed members share it exactly
  [PASS] side 6 momentum census: 26 nonzero coarse momenta; on the sector each carries exactly two propagating modes (52 E-modes paired with 52 B-modes), and the zero modes of the restricted flow are 3 + 3 harmonic fields plus the two frozen constants

J. The coin: exact covariant class on the two-component edge/face payload and its conservative cut (side 4)
-----------------------------------------------------------------------------------------------------------
  [PASS] the 90-degree rotations about z and about x generate all 24 proper rotations (exact closure), so covariance under both is covariance under the group
  [PASS] covariant class on the two-component payload = span{onsite E, onsite B, C, C^T} (x) M_2(R) exactly: 120 patterns, nullspace dimension 16, all sixteen expected members inside with rank 16 (the coin index is inert under rotations)  (dim=16)
  [PASS] weights (1, 1, 1, 1): the conservative cut on the sixteen-dimensional coin class leaves exactly 6 free parameters -- K (x) C free (4), one skew onsite mixing theta_E on the edges and one theta_B on the faces; every diagonal onsite entry vanishes  (free=6)
  [PASS] weights (1, 2, 3, 5): the conservative cut on the sixteen-dimensional coin class leaves exactly 6 free parameters -- K (x) C free (4), one skew onsite mixing theta_E on the edges and one theta_B on the faces; every diagonal onsite entry vanishes  (free=6)
  [PASS] side 6: the complex law (onsite phase theta = 3/7) preserves both zero-charge Gauss rows for both components: on a random state of the double sector (with harmonic parts), d/dt(d0^T E) = 0 and d/dt(d2 B) = 0 exactly
  [PASS] side 6: the complex law's real generator is exactly antisymmetric (conserves sum |E|^2 + |B|^2), has support radius 1, is covariant under all 24 rotations in the doubled oriented law, its edge-to-face blocks are exactly C (gauge- and chain-compatible), and it carries two real components per site
  [PASS] side 6: ker G_theta = ker(C^T C - theta^2) + ker(C C^T - theta^2) has dimension 0 (theta^2 = 9/49 is not an eigenvalue), while two decoupled copies of the one-speed law have kernel dimension 2 x 58 = 116; a harmonic edge field (a zero mode of the one-speed law) has nonzero rate theta under the complex law -- no real change of basis decouples the coin
  [PASS] side 6: on a charged electric surface (dipole) the complex law does NOT preserve the surface: d/dt(d0^T E) = theta J (d0^T E) != 0 rotates the two-component charge, and the per-vertex modulus |rho_v|^2 has zero rate (the charge rotates, it does not decay)
  [PASS] side 6: the K (x) C law (theta = 0, K = [[1,1],[0,1]]) is antisymmetric, radius 1, covariant, and BOTH rate functionals vanish identically for both components (every charged surface preserved); its B1-from-E2 block is C (the components mix in the site basis); K^T K has characteristic polynomial lambda^2 - 3 lambda + 1 with discriminant 5, so over R it is two decoupled copies at distinct irrational speeds
  [PASS] side 6: for a generic conservative coin member (theta_E = 2/3, theta_B = -1/5, K = [[1,2],[3,-1]]) the electric rate functional is exactly (Theta_E (x) d0^T) E -- the coupling block contributes R (x) d0^T C^T = 0 -- so a charged surface is preserved iff theta_E = 0 (executed: on a dipole charge in component 1 the rate is theta_E (0, rho) != 0) while every zero-charge surface is preserved: the all-charge reading cuts exactly theta_E and theta_B (6 -> 4 parameters), never the second component

K. Hidden time: the complex law is second order on its physical pair (side 6)
-----------------------------------------------------------------------------
  [PASS] z1'' = 2 G z1' - (G^2 + theta^2) z1 exactly on a random state: the physical pair (E1, B1) obeys a closed second-order law, and the enlarged payload is its time derivative, z2 = (G z1 - z1') / theta
  [PASS] the second-order law is not nearest-neighbor: G^2 has support radius exactly 2 (C^T C reads edges at distance two) -- the hidden time payload trades locality for an extra coin, and at the linear level it IS an extra coin

L. Item 5's notion on the minimal payload against the constraint-surface notion used here (side 6)
--------------------------------------------------------------------------------------------------
  [PASS] on the minimal (E, B) payload the magnetic rate functional is u_B (d2 B) exactly: the coupling contributes q d2 C = 0 identically, so 'preserves the magnetic Gauss row' as an identity (d2 L = 0) and as surface invariance coincide on the coupling block; the surface reading additionally cuts u_B only when rho_C != 0

M. Resolution certificate
-------------------------
per_element: executed — every coefficient of the 56-pattern four-role basis and of the 120-pattern coin basis is classified exactly under the rotation group, and every Gauss-rate contribution matrix is computed coefficient by coefficient
per_site: executed — every site of the side-4 and side-6 compiled tori is role-censused and shell-counted; the vertex payload's rate is evaluated vertex by vertex (delta states, dipole charges) and shown frozen or drifting exactly
per_mode: executed — exact eigenvalue multiplicities on the side-6 torus certify two transverse branches per nonzero momentum on the Gauss sector and the longitudinal and cube branches off it; kernel dimensions 0 and 116 separate the coupled coin from decoupled copies
per_block: executed — the vertex, edge, face and cube blocks of the rate functionals, of -G^2 and of every witness generator are checked separately (chain identities, skewness, covariance, support radius)
lattice_wide: executed — every invariant-subspace, sector-restriction and background-charge statement is decided exactly on the whole side-4 and side-6 tori; no infinite-volume or continuum statement is executed

TOTAL: PASS=89 FAIL=0

```

## Fix pass after the refuting check (2026-09-05, supervisor)

The 89-check baseline and the fourteen-probe mutation table above were certified at runner sha `119500b2…`. The fold applied CK-01..CK-07 (see `REVIEW_HISTORY.md`) and the supervisor's F-B3-2: the runner gained the exact singular value decomposition of the `K (x) C` witness over `QQ(sqrt 5)` (CK-05: the SF-all coin residue is two decoupled one-speed copies), the executed capacity bound `dim_R M_2(C) = 8` (CK-03: route R7 closed here, not by an unlanded PR), and a tightened sector-independence test (F-B3-2: `4 d0 d0^T` annihilates a basis of `ker d0^T`, and `9 d2^T d2` a basis of `ker d2`, rather than only `im C^T`); the face-side branch label was reworded (CK-07). Post-fold baseline `TOTAL: PASS=91 FAIL=0`, 53 s, cache re-pinned at runner sha `aeabf99a…`. The fourteen primary mutations were run at the pre-fold sha; the runner changes since are two added checks and one tightened predicate.

Checker's planted defects (scratch copies of the pre-fold runner, `ROOT` repointed; `CHECKER_block03_findings.md`): CKM-1 magnetic rate sign flipped — `PASS=86 FAIL=3` (section F both rate identities, section L); CKM-2 the invariance test made to accept `a2 != 0` — `PASS=88 FAIL=1` (section G); CKM-3 the coin cut's coupling equations dropped — `PASS=87 FAIL=2` (section J, both weight choices); CKM-4 fidelity spot-check reproducing the primary's M13 row — `PASS=88 FAIL=1` exactly as tabled.

Checker's executed extensions (recorded, not claimed by the note beyond the qualifiers it now carries): requiring covariance under the odd shift `(1,1,1)` as well cuts the four-role class to its five self-dual members; with the sign character on the coin's second component the coin class is twelve-dimensional and the `K (x) C` witness is not covariant; the three readings of support forcing cut the four-role class to 8 (SF-all), 9 (SF-zero) and 10 (SF-0, the sector reading), coinciding under conservation.
