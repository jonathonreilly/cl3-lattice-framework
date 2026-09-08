---
claim_id: discrete_symmetries_p_t_and_cpt_of_the_emergent_fermion_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite supplied-model results on the open 2x2x2 coarse cube and 4^3 torus: T1 the exact CZ/cut correction for the tested improper maps; T2 shift parity and fixed-mass corner inversion; T3 the encoded antiunitary Z_E K, square +I and fixed-mass invariance; T4 the eight-dimensional massless kernel, mass matrix, four Weyl doublets and specified spectral products with their explicit mass domains; T5 the complete encoded operator table and fixed-Z diagonal classification. The spectral BDI operators apply at m=0 only; spectral CPT=I differs from the many-body CPT that reverses m. A negative antiunitary square is not by itself a fixed-energy Kramers theorem. No physical CPT, continuum limit, measurement of off-diagonal operators or permanent Record formation is derived. Every geometric law symmetry beyond proper rotations remains conditional; t, m, encoding, state and readout context are supplied."
upstream_dependencies: [minimal_axioms]
runner: scripts/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.py
---

# Discrete symmetries `P`, `T` and `CPT` of the emergent fermion

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; formal audit is deferred by owner directive until a solid TOE
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.py`](../scripts/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.txt`](../logs/runner-cache/discrete_symmetries_p_t_cpt_emergent_fermion_check_2026_09_03.txt)
**Premises:** the mathematical model is declared here. The [current minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) fixes the quoted framework boundary; historical model pointers are not proof suppliers.

**The conditional, stated first.** The Lattice axiom names *proper* cubic rotations and nothing improper. Every parity statement in this note is therefore of the form "if the improper point element is applied, the encoded algebra does *this*". Landing the note does not license adding an improper element to the axiom; it supplies exactly the evidence the owner would need to decide whether the law *could* carry one at no cost. Whether it should is an axiom-level question for the owner, and this note does not decide it.

PR #7892 built charge conjugation `C` and named `T` and `CPT` as an interface it did not compute. This note computes them, and computes parity alongside: which of `P`, `T` and `CPT` the emergent matter carries exactly, at what mass, and how the signs act in a supplied fixed-Z readout. `T` is exact at every mass with `T^2 = +1`; parity about a lattice corner is exact at every mass, costing the encoding a Clifford network but no obstruction; and on the eight-dimensional massless kernel the parity operator and the mass term are literally the same matrix.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster theorems about one declared Hamiltonian on the coarse-lattice emergent fermion: the Clifford correction that realises an improper point element on the superfast encoding, the shift-parity rule governing the mass sign, the time-reversal operator and its full table, the Dirac-point representations, and the complete C/P/T transformation table with its supplied fixed-Z classification. The symplectic Pauli statements are exact Gaussian-rational arithmetic on F2 supports with Z4 phases; the tagged numerical items are floating-point cross-checks at the stated tolerance. Every parity statement is conditional on the law carrying improper point elements, which the Lattice axiom does not name."
trace_class: frontier_discovery
target_claim_id: discrete_symmetries_p_t_and_cpt_of_the_emergent_fermion_bounded_theorem_note_2026-09-03
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

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. Groups `A`, `B`, `C` and `E` are exact -- Gaussian-rational coefficients on
symplectic Pauli monomials, `F2` supports and `Z4` phases, complete sweeps over both geometries -- and the items tagged `[numerical]` are floating-point cross-checks at the stated
tolerance.

1. `T1` (`A`). Parity needs a Clifford network on the encoding, and what that network is.
2. `T2` (`B`). Inversion about a corner is exact at every mass; the shift-parity rule for the mass sign.
3. `T3` (`C`). Time reversal `T = Z_E K`, its full table, and `T^2 = +1`.
4. `T4` (`D`). The Dirac point: the mass is the parity operator, and the specified spectral `CPT` product is the identity there, with mass domains stated below.
5. `T5` (`E`). The full transformation table, and its diagonal and off-diagonal rows in the chosen readout basis.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the Altland-Zirnbauer class labels, and the `CZ`-network form of a
diagonal Clifford are standard methodology; every mathematical object used here is redeclared. The runner checks the finite identities; the current memo is an actual input for the framework-scope quotations, not a supplier of this Hamiltonian.
Historical provenance pointers, carrying no grade or parent acceptance (including their former open-PR labels):

- `CHARGE_CONJUGATION_AND_THE_CONSERVED_U1_CURRENT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7892): `C = Z_E C_0`, the bond current `J_ij`, the charge `Q`,
  and the table format used here. Its named interface "`T` and `CPT`" is what this note computes.
- `A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7890): `H(t,m)`, the grading `eps_v`, and its `T2` on
  translations and the 24 proper rotations, of which `T2` here is the improper analogue.
- `LORENTZ_AT_THE_DIRAC_POINT_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (open PR #7888): the 8-fold Dirac point and the `2x2x2` cell basis reused in `T4`.
- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844) and
  `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7834): the encoding, the sign field, the superlattice role
  pattern, and the coarse sublattice `2Z^3`.
The current memo linked above is the only off-note premise input. No parent campaign, physical encoding bridge, or historical status is accepted by these pointers.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and
proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has algebraic presentation `M_2(C)`".
**Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations", and "For each site, the probability
distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" -- the law supplies the odds. **Record**: "Records form", "a record locks exactly
one admissible local possibility", "records are permanent", "Only records are readable", and "A readout value is determined by record content alone."

That symmetry clause, and the identical clause in Admissibility, name **"proper cubic rotations"** and no improper element; grepping the axioms file for
`reflect|inversion|improper|parity|O_h|octahedral|point group` returns nothing. So every `P` statement below is conditional, as stated at the top.

The framework lattice is physical; the following coarse encoding is a supplied conditional model. Everything below reads the Kawamoto-Smit sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, on the superlattice role pattern's
sublattice. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the sign field on it, the superfast
encoding with its face stabilizers, the encoded hop, the grading `eps_v`, and `H(t,m)` with its supplied coefficients. `P1` (`A`) is the Clifford correction `U_P` and its action; `P2`
(`B`) the shift-parity rule; `P3` (`C`) time reversal; `P4` (`D`) the Dirac-point representations; `P5` (`E`) the full table and the record reading. `P2` uses `P1`; `P3` uses `P0` only;
`P4` uses `P0` and the one-particle reduction; `P5` uses `P1`, `P2`, `P3` and `C`, rebuilt here. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **sign field** of the
coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`. The **encoding** is the Bravyi-Kitaev superfast encoding on the coarse lattice, code
qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`.

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_v  = the product of the six Z's at corner v = I - 2 n_v,   S_f = the ordered product of the four A's around a coarse face f
n_v  = (I - B_v)/2,   T_ij = (i/2) A_ij (B_i - B_j),   eps_v = (-1)^{v_1+v_2+v_3},   Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v
H(t,m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v          THE DECLARED LAW; t and m are supplied
J_ij = eta_ij (t/2) A_ij (I - B_i B_j)                            the bond current of PR #7892
C    = Z_E C_0,  C_0 = prod over a perfect matching of A_ij,  Z_E = prod over all edges of Z_e     conjugation, from PR #7892
P: v -> M v + c    a signed permutation M and an integer shift c; improper when det M = -1
V_P  = the bare relabelling of the code qubits induced by P        D_CZ = prod_{{e,f} in N} CZ_ef
G_g  = prod_{v in S} B_v, the Z2 gauge factor                      U_P  = G_g . D_CZ . V_P          THE PARITY OPERATOR
T    = Z_E . K,  K complex conjugation in the record basis         THE TIME-REVERSAL OPERATOR
```

The **star** of a corner is the set of edge sites incident to it, six in the bulk. Here **record pattern** is only shorthand for a supplied complete fixed-Z outcome string; no physical Record formation is constructed. The record basis is the joint
eigenbasis of the `Z_e`. An operator is **record-diagonal** when it is diagonal in that basis; one whose every Pauli monomial carries `X`-support has identically zero record-basis
diagonal; its expectation cannot in general be reconstructed even from the entire fixed-Z joint law. A **cut** is an edge set `XOR_{v in S} star(v)`. The two geometries are the **open `2x2x2` coarse cube** (8 corners, 12 code qubits,
4096-dimensional, 6 faces, 128-dimensional code space) and the **`4^3` coarse torus** (64 corners, 192 code qubits, 192 bonds, 192 faces).

## Theorem 1 -- parity needs a Clifford network on the encoding

**Conclusion.** Conditional on the improper element being applied: (1) `4` of the `10` point maps tested are automorphisms of the open cube -- the corner-centred ones leave the block --
and all `10` are automorphisms of the torus; each induces a permutation of the code qubits. (2) Inversion carries the direction order `-x < -y < -z < +x < +y < +z` cyclically by three,
so the bare relabelling `V_P` does **not** send `A_ij` to `+-A_{P(i)P(j)}`: the exact discrepancy is a **pure `Z`** factor, nontrivial on all `192` torus bonds. (3) No product of `Z`'s
can absorb it: a `Z`-Pauli only supplies a **sign** to `A_e`, whose `X`-support is its own edge. The factor depends only on the **image edge** and is exactly the three
positive-direction edges at its upper endpoint together with the three negative-direction edges at its lower endpoint -- degree `6` on the torus, truncated at the open boundary. (4)
That adjacency is symmetric and loop-free for every map and geometry, so it is realised by the diagonal Clifford `D_CZ = prod CZ_ef`. (5) Hence `U_P = G_g D_CZ V_P` satisfies
`U_P A_ij U_P^-1 = sigma_ij A_{P(i)P(j)}` with `sigma_ij = eta_ij eta_{P(i)P(j)}` on every bond, `G_g`'s `Z`-mask always solving as a cut -- `|S| = 32` for both torus inversions -- so
`G_g` is a `Z2` gauge factor, diagonal in the record basis. (6) `U_P B_v U_P^-1 = +B_{P(v)}` with no sign at any corner, so `n_v -> n_{P(v)}` and `Q -> +Q`; and
`U_P S_f U_P^-1 = +S_{P(f)}` on every face, zero sign flips, so `U_P` is legal in the `pi`-flux code space. (7) `U_P J_ij U_P^-1 = o_ij J_{P(i)P(j)}` with `o` the image-bond
orientation: both inversions reverse all `192` bonds and the `x`-reflections only the `64` `x`-bonds, so the current is a polar vector.

**Proof.** Items 1 and 2 are `F2` support arithmetic on the induced edge permutation, with the residual monomial's `X`-part and phase parity read off directly. Item 3's necessity is the
fact that conjugation by a `Z`-Pauli changes no `Z`-tail; the neighbourhood claim is checked edge by edge against the closed form. Item 4 is a symmetry and loop test. Item 5 conjugates
each `A_ij` by the assembled Clifford, compares monomials exactly, then solves the mask over `F2` against the corner stars. Items 6 and 7 are the same comparison on the corner
operators, face loops and bond currents. All exact.

**Reading, not theorem.** The encoding fixes an order on the six directions at each site, and that order is not itself symmetric under a mirror. Repairing the mismatch is not a matter
of signs: it takes a fixed pattern of two-record couplings, one per pair of neighbouring edges. Once that pattern is in place, the mirror is a legal operation of the code -- no face
constraint is disturbed, and no record is ever flipped, only relabelled.

## Theorem 2 -- inversion about a corner, and the shift-parity rule

**Conclusion.** Conditional as above: (1) For inversion about a **corner**, `sigma_ij = +1` on every one of the `192` torus bonds, while inversion about a **cube centre** carries `-1`
on `64` and the `x = 1/2` reflection on `128` -- a bond-dependent pattern, not a uniform sign. (2) The sign field is carried to **itself** bond by bond by corner inversion, `0` of `192`
differing, and with `0` flipped corners in the one-particle gauge: it is not merely gauge-equivalent to its image. The odd-shift maps differ on `64` and `128` bonds and need a genuine
gauge factor, `32` of the `64` corners at `g_v = -1`. (3) `U_P H_hop U_P^-1 = H_hop` **exactly** for every map on both geometries. (4)
`eps_{P(v)} = (-1)^{sum of the shift components} eps_v` at every corner: the rule depends only on the shift parity, never on the rotation or reflection part, because a signed
permutation preserves `v_1 + v_2 + v_3 mod 2`. (5) Hence `U_P H_m U_P^-1 = (-1)^{sum c} H_m`: `H(t,m)` is **exactly** `P`-symmetric at every `t` and `m` under corner inversion and the
corner-plane reflections, and `P`-symmetric only with `m -> -m` under cube-centre inversion and the mid-plane reflections.

**Proof.** Item 1 reads the signs produced by Theorem 1's construction. Item 2 compares `eta` bond by bond under the induced edge map, and independently solves the one-particle gauge by
propagation over the torus. Item 3 conjugates the kinetic sum, item 5 the mass term. Item 4 is the parity of a signed permutation on the coordinate sum. All exact.

**Reading, not theorem.** There are two kinds of mirror on this lattice: those centred on a corner and those centred half a cell away. The first kind leaves the sign field alone, bond
for bond, and leaves the whole law alone at any mass. The second kind reverses the mass and nothing else. Which kind a given mirror is depends on one bit -- the parity of its shift --
and on nothing else about it, which is the same bit that governs the translations of PR #7890.

## Theorem 3 -- time reversal, exactly, at every mass

**Conclusion.** (1) Every `A_ij` is a **real** Pauli, so `K A_ij K = +A_ij`, `K T_ij K = -T_ij` and `K H_hop K = -H_hop`: bare conjugation is an *anti*-symmetry of the hop, not a
symmetry. (2) `Z_E = prod_e Z_e = prod over the corners with eps_v = -1 of B_v` as Pauli operators, an exact identity because the lattice is bipartite and every edge is covered once;
and it is the **unique** pure-`Z` repair, since `A_ij` has `X`-support exactly its own edge and the bond-to-edge map is onto. (3) `T = Z_E K` acts as `A_ij -> -A_ij`, `B_v -> +B_v` --
the records are `T`-even -- `n_v -> n_v`, `T_ij -> +T_ij`, and `S_f -> +S_f` on every face, so the `pi`-flux code space is `T`-invariant. (4) `T H(t,m) T^-1 = H(t,m)` for **every** `t`
and **every** `m`, with no `m -> -m`. (5) `T J_ij T^-1 = -J_ij` on every bond, so the conserved bond current is `T`-odd, while `T Q T^-1 = +Q`. (6) `T^2 = +1` exactly: `Z_E` is a real
diagonal involution on the `4096`-dimensional cube space, so `T^2 = Z_E Z_E^* = +I`; the code projector is real of rank exactly `128` and commutes with `Z_E`, so `T` carries the code
space onto itself; and `T H T^-1 = Z_E H^* Z_E = H` at residual `0` for `m = 0, 0.7`. `[numerical, 1e-12]` for item 6.

**Proof.** Item 1 is the reality of each monomial's coefficient after the phase is folded in. Item 2 is `F2` support arithmetic; the `X`-support condition is one linear equation per
edge. Items 3 to 5 conjugate Pauli sums by `Z_E` and conjugate coefficients, key by key. Item 6 builds the `4096`-dimensional sparse algebra, projects onto the joint `+1` eigenspace of
the six face stabilizers, and compares `Z_E H^* Z_E` with `H`.

**Reading, not theorem.** Running the law backwards is not simply conjugating the numbers: doing that alone reverses the hopping term. The repair is a single fixed pattern of signs over
the records -- the same object that distinguishes the two sublattices -- and once it is included, the law reads the same backwards as forwards, at any mass. Doing it twice returns
exactly what one started with, so nothing here forces the doubling that a spin-half particle would show.

## Theorem 4 -- the finite massless kernel and distinct symmetry domains

**Conclusion.** On the `4^3` torus at `t=1`, `h(m)=h_0+m Eps` is real symmetric, `{h_0,Eps}=0`, and `Eps^2=I`. It has eight zero modes at `m=0`, with gap `2|m|` after adding a nonzero real mass. The original tests `m=0.2,0.5,1.0` and their residuals are retained; negative masses are tested separately. The real cell vectors `psi_s(v)=(-1)^{sum(v div 2)} delta_{v mod 2,s}/sqrt(8)` form the kernel basis and give the `q=(pi,pi,pi)` block, with velocities `M_a=-Gamma_a`.

The restricted chirality `X=-(Y x X x Y)` has four `+1` and four `-1` eigenvalues. Thus there are two two-component Weyl doublets per handedness, four total (two Dirac tastes) in this finite representation. The mass is `eps=Z1 Z2 Z3`, anticommutes with `X`, and equals corner inversion in this basis. This is a matrix analogue of `gamma^0`, not a physical Lorentz or continuum conclusion. The original restrictions of both inversions, both x-reflections and `C4` retain `U h_0 U^T=h_0`, `U Eps U^T=(-1)^{sum c} Eps`, with zero flipped corners at a corner and 32 at a cube centre.

**Spectral operators.** Here `T_spec=K`, `C_spec=Eps K`, and `S=Eps`. Both antiunitary squares are `+I`, but

```text
T_spec h(m) T_spec^-1 = h(m)
C_spec h(m) C_spec^-1 = -h(-m)
Eps h(m) Eps + h(m) = 2m Eps.
```

The specified BDI particle-hole and chiral relations therefore hold at `m=0` only. No classification of a differently chosen massive symmetry representation is asserted. On the restricted kernel `C_spec P_corner T_spec=+I` is a linear product of two antiunitaries. Among the four listed improper restrictions (corner inversion, cube-centre inversion, x=0 and x=1/2 reflections), only the corner product is scalar; `C4` is a proper contrast. The complete named list and antiunitary flags are checked, not just the corner entry.

For an odd-shift representation `U`, `U` commutes with `h_0` and anticommutes with `Eps`. For the actual cube-centre `P T_spec=U K`, the square is `-I` at every mass, while commutation with `h(m)` holds only at `m=0`. For the actual x=1/2 `C_spec P=Eps U K`, the square is also `-I` at every mass, and the operator anticommutes with `h(m)` at every mass. The latter pairs energies `E` and `-E`; its square alone proves no same-energy Kramers degeneracy away from zero energy. The corner comparison squares remain `+I`.

**Proof.** The kernel, chirality and map restrictions are the original explicit matrix calculations. The mass-domain equations follow by multiplying `{h_0,Eps}=0` and `U Eps=-Eps U`, using reality. The actual matrices are tested at `m=0` and `m=0.7` as well as the original mass grid. Multiplication of `(A K)(B K)=A B*` gives the squares independently of the Hamiltonian. A commuting antiunitary with square `-I` preserves each eigenspace and makes a vector orthogonal to its transform; an anticommuting one generally preserves only the zero eigenspace.

The many-body `C` in Theorem 5 is **unitary**, distinct from `C_spec`. Its corner `CPT` is antiunitary and sends `m` to `-m`. Composing this many-body `C` with an odd-shift parity flips the mass twice and preserves fixed `m`. These are separate representation statements; none supplies physical CPT or spin from the axioms.

## Theorem 5 -- the full table and fixed-Z diagonal classification

**Conclusion.** Exact on the `4^3` torus, for the rows `B_v, n_v, A_ij, S_f, T_ij, H_hop, H_m, H(t,m), J_ij, Q, eps_v` and the columns `C`, `P` about a corner, `P` about a cube centre,
the `x = 1/2` mid-plane reflection, `T`, `CP`, `CT`, `PT` and `CPT` (the products using corner inversion):

```text
        C     Pcor  Pcen  Ref   T     CP    CT    PT    CPT
B_v     -1    +1    +1    +1    +1    -1    -1    +1    -1
n_v     1-nP  n_P   n_P   n_P   n_P   1-nP  1-nP  n_P   1-nP
A_ij    -1    +1    e.e'  e.e'  -1    -1    +1    -1    +1
S_f     +1    +1    +1    +1    +1    +1    +1    +1    +1
T_ij    +1    +1    e.e'  e.e'  +1    +1    +1    +1    +1
H_hop   +1    +1    +1    +1    +1    +1    +1    +1    +1
H_m     -1    +1    -1    -1    +1    -1    -1    +1    -1
H(t,m)  -m    inv   -m    -m    inv   -m    -m    inv   -m
J_ij    -1    +1    e.e'  e.e'  -1    -1    +1    -1    +1
Q       -1    +1    +1    +1    +1    -1    -1    +1    -1
eps_v   +1    +1    -1    -1    +1    +1    +1    +1    +1
```

(1) Every entry is a sign on the **same** operator at the image index -- `B_v -> s B_{P(v)}`, `A_ij -> s A_{P(i)P(j)}`, `S_f -> s S_{P(f)}`, `T_ij -> s T_{P(i)P(j)}`,
`J_ij -> s J_{P(i)P(j)}` at the ordered image bond -- and no entry is lost; `B_v`, `S_f`, `H_hop`, `H_m`, `Q` and `eps_v` are uniform in every column. (2) In the two **odd-shift**
columns the rows `A_ij`, `T_ij` and `J_ij` are *not* a uniform sign but the bond-dependent pattern `sigma_ij = eta_ij eta_{P(i)P(j)}`, at `-1` on `64` of the `192` bonds for the
cube-centre inversion and on `128` for the `x = 1/2` reflection; `e.e'` marks that pattern in the table. (3) `H(t,m)` is invariant under `P` about a corner, under `T` and under `PT`,
and goes to `H(t,-m)` under `C`, the two odd-shift parities, `CP`, `CT` and `CPT`. (4) `S_f -> +S_f` in every column. (5) **Fixed-Z diagonal classification**: `B_v`, `Q` and `H_m` are pure
`Z`, hence record-diagonal, and carry the table's `P` and `T` signs; `A_ij`, `S_f`, `T_ij` and `J_ij` have identically zero record-basis diagonal on both geometries, so no fixed-Z outcome law determines their general expectation. Since both inversions reverse every bond, the current *vector* is carried to its opposite even where the table reads `+1`.

**Proof.** Every column is a conjugation of Pauli sums, exact and compared key by key against the image operator; the antiunitary columns compose by `(A K)(B K) = A B^*`. The record
statements are the `X`-support test on each Pauli sum, swept over both geometries. All exact.

**Readout boundary.** The Pauli table establishes covariance of specified operators and, after a state and measurement context are supplied, of that fixed readout. It gives no instrument for off-diagonal observables. For example, `|+>` and `|->` have the same complete Z outcome law `(1/2,1/2)` yet X expectations `+1` and `-1`; even all fixed-Z correlations cannot recover X. The runner checks this witness. No physical permanent Record process, history covariance, measurement context or Born weighting follows from the table.

## Corollary -- conditional finite symmetries, with no physical CPT bridge

1. The chosen many-body `H(t,m)` is invariant under corner parity and `Z_E K` for all supplied real `t,m` on the applicable finite geometries. The table's many-body `C`, corner `CP`, `CT` and `CPT` reverse the mass; at nonzero fixed mass these are not unbroken symmetries.
2. The tested improper maps admit the stated Clifford/cut construction preserving the face code. This is a conditional model construction; no new symmetry is added to the Lattice axiom.
3. The massless kernel has four Weyl doublets, and its corner parity equals the mass matrix. Its spectral `C_spec P T_spec=I` and the negative squares have exactly the distinct domains stated in Theorem 4.
4. Pure-Z versus zero-diagonal classification is retained. Physical readout, time reversal of a record-production process and measurement of off-diagonal operators remain supplied/open.
5. No weak-sector, physical spin, interacting theory or continuum claim follows from these finite identities.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. In particular the Lattice axiom's symmetry clause is quoted as it stands, and no improper
  element is added to it.
- No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is created or edited.
- Nothing here is derived from the axioms; the coarse lattice, the encoding, the sign field and the Hamiltonian are declared objects, and no coefficient is derived: `t` and `m` are
  supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears. Which Hamiltonian applies is designed, not derived -- see PR #7834.
- No interaction term is added, no second species appears, no chiral sector is constructed, and no continuum limit is taken.

## Interfaces named for other lanes, not moved here

- **The weak sector.** Nothing here bears on it. The construction has no chiral sector at all: the emergent content is four finite Weyl doublets, and a parity-symmetric vector-like
  theory says nothing about a sector that is not.
- **The continuum.** Everything is a lattice operator or a finite-matrix restriction. Whether `U_P`, `T` or the `CPT` product has a continuum limit, and what it is, is not shown here.
- **The fine `(4,2,2)` pattern's own improper symmetries.** Not examined. Everything here is on the coarse lattice; what the fine superlattice role pattern does under an improper
  element is a separate question.
- **Whether the designed marker rule of PR #7834 is inversion-symmetric.** Not examined. This note treats the encoded algebra and the declared Hamiltonian only.

## Remaining live routes

1. Larger blocks and other geometries. The open `2x2x2` cube and the `4^3` torus are what is proved; nothing is claimed beyond them.
2. The many-body statements at nonzero `m` beyond the cube. Theorems 1, 2, 3 and 5 are exact at every `t` and `m`; the dense confirmation of `T^2 = +1` is on the eight-corner cube only.
3. The other improper elements of the full point group. Two inversions and six reflections are tested, with a proper rotation and a translation for contrast; the remaining improper
   elements are not enumerated here.
4. Correlation structure. Fixed-Z data do not determine off-diagonal expectations; an additional readout protocol would have to be supplied and checked.

## Executable claim block

```text
setting: supplied coarse encoding, KS signs and H(t,m), open 2x2x2 cube and 4^3 torus; current memo supplies only framework-scope quotations
A_B_C: original exact Clifford/cut, shift-parity and Z_E K identities retained with all original check IDs
D: eight kernel modes; gap2|m|; four Weyl doublets; P_corner=eps; specified spectral BDI at m0 only; complete four-improper scalar comparison plus proper C4 contrast
negative_squares: independent of m; cube-centre PT commutes only at m0; x-half C_spec P anticommutes allm, hence opposite energies outside zero
E: original full Pauli table retained; many-body C is unitary, corner CPT reverses mass; many-body C times odd-shift P preserves mass
readout: pureZ or zeroZdiagonal only; identical Z laws can have opposite X expectations; no permanent Record formation or physical CPT derived
checks: all33 original IDs retained, affected predicates strengthened, additional source-bound controls; current totals are in the genuinely executed cache
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3`, on exactly two finite geometries: the open `2x2x2` coarse cube and the `4^3` coarse torus. Nothing is claimed for `Z^3`, for the
fine lattice, or for any larger region, and no thermodynamic limit is taken.

**Every parity statement is conditional on the law carrying improper point elements.** The Lattice axiom names proper cubic rotations only. What is proved is what the encoded algebra
does when an improper map is applied, together with the fact that applying it costs the encoding nothing: `H_hop` is invariant, every face stabilizer is carried to itself with no sign,
and the correction is a fixed Clifford network. That is evidence the law *could* carry improper elements at no cost; it is not a licence to add them, and whether to add them is an
axiom-level question for the owner. Time reversal carries no such condition: `T = Z_E K` is built from the encoding's own objects.

The content is **free hopping plus one declared diagonal term**. No interaction appears, and the coefficients `t` and `m` are **supplied**: derived from no axiom and fixed by no clause
quoted here. No sign statement anywhere depends on `t`. Which Hamiltonian applies is a designed choice, not an axiom consequence.

Theorems 1, 2, 3 and 5 are many-body statements in the encoded algebra, exact at every `t` and `m`. Theorem 3's dense confirmation is one `4096`-dimensional cube computation; Theorem 4
is a `64x64` one-particle computation and `8x8` restrictions of it, about the exact zero-mode subspace of a finite matrix and the locally declared `O(p)` Bloch matrix. **No
continuum limit is taken**, and no physical Lorentz covariance, interacting theory or anomaly result is asserted. The `CZ` network is a
construction on the encoding, not an axiom object. The chosen matching construction of many-body `C` uses an even corner count; both geometries satisfy it. No parent's physical interpretation is imported.

## Review record

The 2026-09-08 correction retains the original finite data and 33 check identities, narrows the mass, multiplicity and readout claims, and adds decisive controls. Both this note and the exact current memo are declared runtime inputs with live hash checks. The current cache records the final source, complete input fingerprint, actual exit status and full stdout under the original 90-second cap. Original note/runner/cache and failed scientific mutants are preserved in the external review/repair packets; the dated correction record identifies that provenance. Formal audit is deferred until a solid TOE. Neither a cache success nor this author correction grants scientific acceptance.
