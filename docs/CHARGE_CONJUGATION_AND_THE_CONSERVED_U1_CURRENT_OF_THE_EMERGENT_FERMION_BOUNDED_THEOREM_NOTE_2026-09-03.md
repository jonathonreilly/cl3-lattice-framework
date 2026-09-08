---
claim_id: charge_conjugation_and_the_conserved_u1_current_of_the_emergent_fermion_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "Conditional finite encoded-fermion algebra for supplied real t,m: exact continuity with J=i t eta T B_j=-i t eta T B_i=(t eta/4)A(B_i-B_j)^2, gauge-legal current and incident-star charge readout. Two-monomial/support and nonzero naive-residual claims require t!=0. Named connected blocks have explicit matching conjugators; a T-join flipping every corner exists iff each component has even order. Equal matching conjugation is proved on encoded generators, scalar equality only checked on the cube +face code. The antiperiodic 4^3 zero-mode-free negative spectral projector and t=1 cube state are finite conditional examples, not physical vacuum selection. Actual Z_E anticommutation supplies spectral reflection at m=0. Equal full fixed-Z statistics can have opposite current, so no current readout or permanent-record dynamics is derived. No gauge-field, continuum or photon result."
upstream_dependencies: ["minimal_axioms"]
runner: scripts/charge_conjugation_and_conserved_u1_current_check_2026_09_03.py
---

# Charge conjugation and the conserved `U(1)` current of the emergent fermion

**Date:** 2026-09-03
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** conditional-support for the supplied finite model
**Status boundary:** source-side conditional mathematical support; no applied audit or retained status. The axioms and framework rules are unchanged.
**Primary runner:**
[`scripts/charge_conjugation_and_conserved_u1_current_check_2026_09_03.py`](../scripts/charge_conjugation_and_conserved_u1_current_check_2026_09_03.py)
**Runner cache:**
[`logs/runner-cache/charge_conjugation_and_conserved_u1_current_check_2026_09_03.txt`](../logs/runner-cache/charge_conjugation_and_conserved_u1_current_check_2026_09_03.txt)
**Premises:** the finite mathematical objects are declared here. The quoted axioms and current comparison notes constrain interpretation; they supply no physical realization theorem. The primary program is self-contained and reads no mutable input files.

The coarse-lattice emergent fermion has a number operator, a hop, and a mass term. What it has not been given is the pair of objects a conserved quantity actually
consists of: a charge and the local flow of that charge between neighbouring corners. The question here is what that pair is inside the readable algebra, what
conjugation exchanges matter and its absence, and which of the two the records register. The charge turns out to be a parity count on the incident records at a corner,
readable directly; for nonzero `t`, the current is a two-monomial bond operator with no record-diagonal part at all.

## Machine status

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional finite encoded-fermion algebra for supplied real t,m: exact continuity with J=i t eta T B_j=-i t eta T B_i=(t eta/4)A(B_i-B_j)^2, gauge-legal current and incident-star charge readout. Two-monomial/support and nonzero naive-residual claims require t!=0. Named connected blocks have explicit matching conjugators; a T-join flipping every corner exists iff each component has even order. Equal matching conjugation is proved on encoded generators, scalar equality only checked on the cube +face code. The antiperiodic 4^3 zero-mode-free negative spectral projector and t=1 cube state are finite conditional examples, not physical vacuum selection. Actual Z_E anticommutation supplies spectral reflection at m=0. Equal full fixed-Z statistics can have opposite current, so no current readout or permanent-record dynamics is derived. No gauge-field, continuum or photon result."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "No physical realization, admissibility formation law, or additional current-readout protocol is supplied; finite conditional algebra does not discharge that consumer."
source_of_blocker_text: review_loop
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Carry the explicit finite assumptions and open physical obligations to any later consumer; independent source review precedes integration. Formal audit remains deferred."
conditional_surface_status: "Conditional on the supplied encoding, carrier, Hamiltonian, finite geometry and stated parameter domain."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the five statements below, exactly the runner's check groups `A`-`E`. Groups `A`, `B`, `C` and `D` are exact -- Gaussian-rational
coefficients on symplectic Pauli monomials, `F2` supports and `Z4` phases, complete sweeps, and integer record arithmetic, with no floating-point step anywhere --
and the items tagged `[numerical]` in group `E` are floating-point cross-checks at the stated tolerance.

1. `T1` (`A`). The lattice continuity equation, the bond current, and what the naive candidate does instead.
2. `T2` (`B`). Charge conjugation `C = Z_E C_0` and the full transformation table, with the `C_0` and `Z_E` columns.
3. `T3` (`C`). The parity condition: an edge-flip operator exists exactly when each connected component has even order; the named even blocks have explicit perfect matchings.
4. `T4` (`D`). The charge as a record readout: an incident-star parity count per corner (three records on the cube).
5. `T5` (`E`). The declared finite half-filled state is C-invariant under its stated domain; the empty state is not.

## Imports and authority

Current interpretation and dependency sources:

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md).

The finite model is redeclared and the primary does not import another program. Historical context carries no inherited acceptance. The Bravyi-Kitaev superfast encoding, the Kawamoto-Smit staggering, the Majorana form of fermionic charge
conjugation, and the T-join characterisation of a degree-parity edge set are standard methodology; every object is redeclared here and the runner recomputes the stated finite checks. No observational value, no fitted number and no framework premise enters any proof. Historical context pointers, without imported scientific grade (the axioms remain the actual vocabulary source):

- `A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md` (historical PR #7890): the Hamiltonian `H(t,m)`, the
  grading `eps_v`, and the `4^3` one-particle machinery. Its `T8`, that conjugation by the grading exchanges `+-m` on the one-particle operator, is the one-particle
  shadow of what `T2` here establishes at the operator level.
- `THE_VACUUM_QUESTION_IS_ONE_COEFFICIENT_OF_THE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md` (historical PR #7885): `sum_i B_i` commutes with every hop, and the occupancy term
  read as a chemical potential.
- `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md` (historical PR #7879): the sea, and
  `<n_v> = 1/2` exactly.
- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (historical PR #7844) and
  `EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md` (historical PR #7834): the encoding, the superlattice
  role pattern, and the coarse sublattice `2Z^3`.
- `MINIMAL_AXIOMS_2026-06-29.md`: the four framework axioms quoted in "Setting". No grade of theirs is cited and no hypothesis is adopted.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has
algebraic presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic
rotations", and "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" -- the law
supplies the odds. **Record**: "Records form", "a record locks exactly one admissible local possibility", "records are permanent", "Only records are readable", and
"A readout value is determined by record content alone."

The lattice is physical. Everything below reads the Kawamoto-Smit sign field on the coarse lattice `2Z^3`, one fermionic mode per coarse vertex, on the superlattice
role pattern's sublattice. Composition is **ordinary** throughout: the algebra of a region is the tensor product of its sites' algebras and no graded clause is used
anywhere.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the KS sign field
on it, the superfast encoding with its face stabilizers, the encoded hop, the grading `eps_v`, and the Hamiltonian `H(t,m)` with its supplied coefficients. `P1`
(`A`) is the continuity equation and the bond current; `P2` (`B`) the conjugation operator and its table; `P3` (`C`) the parity condition on the region; `P4` (`D`)
the record readout of the charge; `P5` (`E`) the supplied finite conjugation-invariant state. `P2` uses `P0` only; `P3` uses the single relation among the `B_v` established in it; `P4`
uses `P1`'s form of `Q`; `P5` uses `P2`. The strongest supported scope is precisely `P0`-`P5`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` along `e_a` sits at the fine site `2v + e_a`. The **KS
sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`, `eta_3(v) = (-1)^{v_1 + v_2}`. The **encoding** is the Bravyi-Kitaev superfast
encoding on the coarse lattice, code qubits on the coarse edges, direction order `-x < -y < -z < +x < +y < +z`.

```text
A_ij = X(edge (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),  A_ji = -A_ij
B_v  = the product of the incident Z's at corner v = I - 2 n_v,   S_f = the ordered product of the four A's around a coarse face f
n_v  = (I - B_v)/2                     the occupation of coarse vertex v; B_v = -1 marks the excitation
T_ij = (i/2) A_ij (B_i - B_j)          the encoded hop across (i, j),  T_ji = +T_ij
eps_v = (-1)^{v_1+v_2+v_3}             the supplied corner grading
H(t,m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v          THE DECLARED LAW; t and m are supplied real numbers
J_ij = eta_ij (t/2) A_ij (I - B_i B_j)                            THE BOND CURRENT
N = sum_v n_v,   Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v         the number and the charge
C_0 = prod over a perfect matching M of A_ij,  Z_E = prod over all edges of Z_e,  C = Z_E C_0
```

The **star** of a corner is the set of edge sites incident to it, six in the bulk. A **record pattern** is one assignment of a value to every edge record; the record
basis is the joint eigenbasis of the `Z_e`. An operator is **record-diagonal** when it is diagonal in that basis, so that its value is fixed by record content alone.
A **perfect matching** is a set of bonds meeting every corner exactly once; a **T-join with `T = V`** is an edge subset of odd degree at every corner.

## Theorem 1 -- the continuity equation and the bond current

**Conclusion.** For real `t,m`, with the nonzero monomial/support and naive-failure statements restricted to `t != 0` (the original fixtures use `t = 1`; at `t = 0`, `J = 0`): (1) `dn_i/dt = i[H, n_i] = - sum_{j~i} J_ij` with `J_ij = eta_ij (t/2) A_ij (I - B_i B_j)`, at residual identically `0` at all `27` corners of the
open `3x3x3` block and all `64` corners of the `4^3` torus. (2) Equivalently, on every bond, `J_ij = i t eta_ij T_ij B_j = -i t eta_ij T_ij B_i = (t eta_ij/4) A_ij (B_i -
B_j)^2`. (3) The candidate `(t/2) A_ij (B_i + B_j)` fails structurally: `B_i + B_j` annihilates the sector `B_i = -B_j` in which the hop acts, and the residual
carries `12` and `24` nonzero Pauli terms on the two lattices. (4) Every `J_ij` is Hermitian; `J_ji = -J_ij` while `T_ji = +T_ij`; it is exactly two Pauli monomials
with `X`-support on exactly one qubit, its own edge site, and total support `11` qubits in the bulk, `= star(i) union star(j)`, and `6`, `8` or `10` at the open
boundary. (5) `[J_ij, S_f] = 0` for every bond-face pair on both lattices. (6) Every monomial of `J_ij` carries nonzero `X`-support, so its record-diagonal part is
identically zero -- confirmed over all `12` bonds and all `4096` record patterns of the `2x2x2` cube. (7) `[H, N] = [H, Q] = 0`, the corner equations summed with the
bond currents cancelling in pairs, and `Q` is a pure `Z`-operator.

**Proof.** Item 1 expands `i[H, n_i]` and `sum_j J_ij` as Pauli sums with Gaussian-rational coefficients and compares key by key; both sides carry two monomials per
incident bond, by item 4, and the keys and coefficients agree. Items 2 and 3 are the same comparison on one bond and at one corner. Items 4 to 7 are `F2`
support arithmetic with `Z4` phases: a monomial commutes with another exactly when their symplectic form vanishes, and a monomial is diagonal exactly when its
`X`-support is empty. All exact.

**Reading, not theorem.** The quantity that flows is the same corner parity that says whether a particle is there. What flows along one bond is an operator supported
on the two corner stars that meet at it, and its Pauli action flips that edge basis bit. This algebraic action is not established dynamics of permanent records, and fixed-record probabilities do not determine its expectation. The natural first guess, the sum of
the two corner parities, is exactly wrong: it vanishes precisely where a particle would be passing.

## Theorem 2 -- charge conjugation, and the whole transformation table

**Conclusion.** With `C_0` the product over a perfect matching of the `A_ij` and `Z_E = prod_e Z_e = prod over the odd-sublattice corners of B_v = (-1)^{N_odd}`, the
operator `C = Z_E C_0` acts, on the `2x2x2` cube, the open `4x4x4` block and the `4^3` torus, with `x`-dimers and independently with `y`-dimers, as:

```text
                B_v      n_v        rho_v    A_ij     S_f     T_ij     H_hop     H_m     J_ij     Q
   C            -B_v     I - n_v    -rho_v   -A_ij    +S_f    +T_ij    +H_hop    -H_m    -J_ij    -Q
   C_0          -B_v     I - n_v    -rho_v   +A_ij    +S_f    -T_ij    -H_hop    -H_m    +J_ij    -Q
   Z_E          +B_v     n_v        +rho_v   -A_ij    +S_f    -T_ij    -H_hop    +H_m    -J_ij    +Q
```

Hence `C H(t,m) C^-1 = H(t,-m)`, an exact symmetry at `m = 0`; `C^2 = +I`; `S_f -> +S_f` with no sign, so the code space is preserved; the grading `eps_v` is a
supplied corner label and is unchanged; the two matchings have identical conjugation on the encoded generators; and the whole table is independent of the bond weights, holding verbatim for
the KS signs, for all-`+1` weights and for generic rational weights.

**Proof.** Fermionic conjugation is the particle-hole map on the Majoranas, implemented by their total product; pairing the Majoranas along any perfect matching and
using `gamma_i gamma_j = i A_ij` gives the purely Pauli operator `C_0`, and `Z_E` is the diagonal dressing that restores the sign of the hop. Every entry is then
conjugation of a Pauli sum by a Pauli monomial, a sign per key fixed by the symplectic form, compared exactly. Equal conjugation is checked directly by rebuilding
`C` from a second matching; their ratio is nonscalar in the ambient edge register but scalar on the cube +face code (E9). No unrestricted torus-cycle phase identity is claimed. Weight-independence by rebuilding `H_hop` with two further weight assignments. All exact.

**Reading, not theorem.** The encoded particle-hole unitary flips every corner parity as an algebraic transformation; no operation on permanent records is supplied. Doing it along a set of edges that
touches every corner once is enough. The law's hopping part does not notice; the price term reverses; so the sign of a mass is not something the exchange preserves,
and at zero mass the exchange is an exact symmetry of the law.

## Theorem 3 -- when such an exchange exists on a finite region

**Conclusion.** (1) The product over all corners of `B_v` equals `I` identically, on every block and torus tested: each edge carries a `Z` from both of its
endpoints. This is the one relation the encoded corner operators obey. (2) Hence `B_v -> -B_v` at every corner forces `I -> (-1)^{|V|} I`: on a region with an odd
number of corners -- the open `3x3x3` block, `|V| = 27` -- no unitary `C` exists on the code space at all, not merely no Pauli one. Equivalently, the code space is a
single fermion-parity sector and `C` sends `N -> |V| - N`, changing parity by `(-1)^{|V|}`. (3) In edge-flip form the same condition reads: flipping every `B_v`
requires an edge subset of odd degree at every corner, a T-join with `T = V`, while `sum_v deg_S(v) = 2|S|` is even. Such a subset exists iff each connected component has even order. On the named connected even blocks the explicit perfect matchings of Theorem 2 give minimal witnesses; a general even connected graph need not have a perfect matching.

**Proof.** Item 1 is `F2` support arithmetic: the symmetric difference of all corner stars is empty. Item 2 is item 1 conjugated. Item 3 requires the handshake identity separately on each component. Sufficiency follows on a spanning tree: work from leaves toward the root, selecting the parent edge exactly when the leaf needs odd degree after its child edges; an even component size makes the final root condition automatic. All exact.

**Reading, not theorem.** Whether matter and its absence can be exchanged at all is a property of the region, not of the law: each connected component needs an even number of corners for the edge-flip condition. On
a block with an odd count there is no such operation to be had, and the parity of the corner count is worth stating whenever a finite block is used for anything
downstream.

## Theorem 4 -- the charge is a record readout

**Conclusion.** `Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v` is conserved, `C`-odd, and a pure `Z`-operator, hence record-diagonal. On all `4096` record patterns of
the `2x2x2` cube, `Q` equals the number of corners whose three incident edge records hold an odd number of the value `1`, minus `|V|/2`, at deviation `0`; it takes the
integer values `-4, -2, 0, 2, 4`, symmetric about `0`. By contrast every `J_ij` has an identically zero diagonal over all `12` bonds and all `4096` patterns.

**Proof.** `n_v = (I - B_v)/2` and `B_v` is the product of the incident `Z`'s, whose eigenvalue on a record pattern is `+1` or `-1` according to the parity of the incident values
read there; summing gives the count. Conservation and `C`-oddness are Theorems 1 and 2. The current's zero diagonal is Theorem 1 item 6. Exact integer arithmetic
throughout; the spectrum is even-valued because the relation of Theorem 3 item 1 makes the total number of odd corners even.

**Reading, not theorem.** Count, at each corner, whether an odd number of its incident records read `1`. That count minus half the corners is a conserved charge, and it
can be read straight off the records. The flow of that charge between two corners is also an exact lattice quantity, but no single pattern of records shows it; it
is not determined even by the full joint statistics of those fixed records. E10 gives two cube +code states with identical joint Z probabilities and currents +1 and -1.

## Theorem 5 -- supplied finite conjugation-invariant states

**Conclusion.** The one-particle `4^3` fixture uses antiperiodic seam signs in all three directions. Its real Hermitian hopping matrix obeys `{M,Eps}=0` and has no zero modes. With `P(m)` the strictly negative spectral projector of `M+m Eps`, `Eps(I-P(m))Eps=P(-m)` at the tested `m=0,0.5,1,2`, and at zero mass the diagonal occupancy is `1/2`. The general projector identity requires the strict-negative split to have no zero eigenvalues: spectral conjugation exchanges negative and positive spaces, and only then is the positive projector `I-P`. The periodic fixture has eight zero modes, negative rank28 and residual `1/8`; it is outside this convention. A gapped but nonchiral shift is also outside the hypotheses.

On the cube's `128`-dimensional joint +face code, at supplied `t=1`, `C` is unitary, `C N C^-1=8-N`, and `C H(t,m) C^-1=H(t,-m)` at `m=0,0.7,1.5`. At `m=0`, the actual `Z_E` anticommutes with `H`, which proves spectral reflection; `C` commuting with `H` alone would not. The runner compares the actual ordered spectrum with its negative reversal, rather than a tautology. The finite zero-mass ground energy numerically agrees with `-4 sqrt(3)`, approximately `-6.928203230`, with `<N>=4`, unit C-overlap and zero current on every bond. The empty state is mapped wholly to `N=8` and is orthogonal to itself.

**Proof and numerical scope.** The 64-dimensional one-particle matrix is diagonalized with the declared seams. The cube matrices are restricted by the actual face projector and diagonalized in its 128-dimensional image. Exact conjugation/anticommutation identities give the structural statements; the projector checks use `1e-12` and cube matrix checks use `1e-10`, the ground energy/occupancy fixture uses `1e-8`, and spectral reflection uses `1e-9`. E8 retains the periodic and nonchiral boundaries; E9 checks the matching ratio on the actual cube code; E11 rejects an asymmetric spectrum. These statements concern supplied finite states and do not select a physical vacuum or establish uniqueness among possible physical preparations.

## Corollary -- a readable charge and an unreadable current

Within the setting declared above, and on the finite blocks and tori named:

1. A global `U(1)` with an exactly conserved, gauge-legal, local bond current exists in the emergent matter. The charge is readable from the records -- an incident-star
   parity count at each corner -- and the current is not: it has no record-diagonal part at all, and has no supplied fixed-record readout (E10).
2. `C = Z_E C_0` is an exact symmetry at `m = 0` and exchanges `+-m`, so a mass sign is a `C`-odd supplied datum. The one-particle statement of PR #7890, that
   conjugation by the grading exchanges `+m` and `-m`, is the shadow of this operator-level table.
3. The all-corner edge-flip condition requires even order in every connected component; explicit conjugators exist on the named matching-equipped blocks. This is a boundary of the encoding worth stating for any finite block used
   downstream, and it is a property of the region rather than of the law.
4. Neither the charge nor the current is coupled to any gauge field here. The gauge structure of the encoding is `Z2`; no photon is claimed, and nothing here
   identifies this `U(1)` with electromagnetism.
5. Read with the vacuum ruling of PR #7885 and the sea of PR #7879: the named finite ground state has conjugation symmetry; no physical vacuum selection follows.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted.
- Only source-side conditional status is stated; no audit verdict, retained status, primitive or premise registry is applied. The coordinator owns citation publication.
- Nothing here is derived from the axioms; the coarse lattice, the encoding, the sign field and the Hamiltonian are declared objects, and no coefficient is derived:
  `t` and `m` are supplied, and no update rule, formation site, formation rate, coupling, or absolute unit appears. Which Hamiltonian applies is designed, not
  derived -- see PR #7834.
- No interaction term is added, no second species appears, and no continuum limit is taken.

## Interfaces named for other lanes, not moved here

- **`T` and `CPT`.** Not computed. Only `C` is built; time reversal and the combined operation are untouched, and nothing here bears on either.
- **Coupling to a gauge field.** Nothing couples to this `U(1)` in the declared law. What would gauge it, and whether the encoding's own `Z2` structure obstructs
  that, is a question for the lane that owns the dynamical clause.
- **The continuum current.** Everything is a lattice operator. Whether `J_ij` has a continuum limit, and what it is, is not shown here.
- **Anomalies.** No anomaly statement is made or implied. The chiral structure of the staggered fermion is not analysed here at all.

## Remaining live routes

1. Larger blocks and other geometries. The `2x2x2` cube, the open `3x3x3` and `4x4x4` blocks and the `4^3` torus are what is proved; nothing is claimed beyond them.
2. The many-body statements at nonzero `m`. Theorems 1 to 4 are exact at every `m`; the many-body spectral statements of Theorem 5 are on the eight-corner cube only.
3. Current-current operator correlations and additional measurement protocols remain open. Correlations of the same fixed Z records cannot determine current, as E10 proves.
4. Other conserved quantities. Only `N` and `Q` are examined; whether the declared law carries further local conservation laws is not treated.

## Executable claim block

```text
setting: supplied real t,m; ordinary tensor composition and the declared finite BK/KS model
continuity: J=eta(t/2)A(I-B_i B_j)=i t eta T B_j=-i t eta T B_i=(t eta/4)A(B_i-B_j)^2
parameter_boundary: original t=1 fixtures retained; A8 also checks t=0,2,-3/2; t=0 gives J=0; two monomials/full support/nonzero naive residual require t!=0
geometry: open3^3 and 4^3 torus exact continuity, named cube/open4^3/torus conjugation; Q counts incident-star parity (z=3 on cube,6 in bulk)
conjugation: original full C/C0/ZE table and weight controls retained; equal matching conjugation on encoded generators, ambient ratio nonscalar and cube +code ratio scalar
component_boundary: all-corner T-join iff every component even; perfect matching explicitly supplied on the named even blocks; odd27 forbids all-corner conjugation
record_boundary: current diagonal zero; E10 equal complete fixed-Z statistics/current +/-1 rules out recovery from those statistics
sea_domain: antiperiodic4^3, real Hermitian chiral matrix without zero modes; periodic8-zero-mode and gapped nonchiral controls rejected
cube: t=1,+face code dimension128; C conjugates +/-m; ZE anticommutes at m=0; actual reflected spectrum checked; finite E0=-4sqrt3, <N>=4 and zero mean current
authority: no physical vacuum selection, permanent-record update law, additional readout, photon, axiom amendment or applied audit
evidence: all 32 original checks retained with corrected F3 oracle; five added checks A8,E8,E9,E10,E11; 37 checks expected; actual current cache required
```

## Proof boundary

Everything is proved on the **coarse** lattice `2Z^3`: the `2x2x2` cube, the open `3x3x3` and `4x4x4` blocks, and the `4^3` torus. Nothing is claimed for `Z^3` and
nothing is claimed for any larger region.

The content is **free hopping plus one declared diagonal term**. No interaction appears, and the coefficients `t` and `m` are **supplied**: derived from no axiom and
fixed by no clause quoted here. Which Hamiltonian applies is a designed choice, not an axiom consequence.

The operator identities of Theorems 1 to 4 hold for real `t,m`; nonzero-current support/count statements require `t != 0`. Theorem 5's cube statements come from **one** eight-corner many-body
diagonalisation on a `128`-dimensional code space, and its one-particle statements from `64x64` tori; no larger many-body region is treated.

No continuum limit is taken, and no continuum current is constructed. No anomaly statement is made. No claim is made that this `U(1)` is electromagnetism or that
anything couples to it; the encoding's own gauge structure is `Z2` and no photon appears anywhere. The parity result of Theorem 3 is a condition on the region and is
stated as such: it states the component-wise edge-flip obstruction and the named explicit witnesses, and nothing about whether some other operation on some other region would serve.

## Current correction boundary

The dated [correction and historical review record](../.claude/science/review-fixes/u1-matter-links-2026-09-07/CORRECTION.md) preserves the original September 3 review text and identifies the superseding source corrections. Those historical acceptance counts and claims are not current verdicts. The final source and actual cache identity govern the executable evidence. Independent source confirmation and coordinator gates remain separate; formal audit is deferred.
