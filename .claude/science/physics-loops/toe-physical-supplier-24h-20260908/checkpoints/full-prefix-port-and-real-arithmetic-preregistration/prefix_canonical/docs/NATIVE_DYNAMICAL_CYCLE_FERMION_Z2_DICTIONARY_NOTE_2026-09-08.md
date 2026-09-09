---
claim_id: native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Exact finite unitary from the full native edge-qubit carrier onto the all-positive Gauss sector of CAR modes and Z2 link qubits, intertwining A, B, physical Z, hopping and every simple cycle. Conditional corollaries identify gated ice rings, low-charge signed transport and its three-hop exchange algebra. Relaxed cycle constraints, gates and Hamiltonian coefficients are supplied; no U1 identification, selected dynamics, deconfinement or axiom closure."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
  - spin_half_cubic_ice_finite_detuning_projector_maxwell_stiffness_bounded_theorem_note_2026-09-03
runner: scripts/native_dynamical_cycle_dictionary_2026_09_08.py
---

# The full native edge carrier as fermions and constrained Z2 links

**Date:** 2026-09-08
**Type:** bounded_theorem
**Status:** conditional-support

The full native edge-qubit space has an exact, phase-correct dictionary into a constrained fermion–link space. The physical edge $Z$ observable becomes the electric link observable, native hopping becomes fermion hopping dressed by a $Z_2$ link, and native cycles become magnetic Wilson loops. This uses the existing carrier: the larger tensor product is a redundant mathematical representation, not a new physical role assignment.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite operator dictionary for the supplied native graph and algebra; gated Hamiltonian corollaries require the stated additional constraints and couplings."
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Determine which Hamiltonian, state domain and Record dynamics the native physical premises actually supply."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Supplied algebra and exact target

The [native instrument parent](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md), equations 1–4 and Theorem 1, supplies the graph, neighbor orders and ambient Pauli algebra. Let the graph be finite, connected, loopless and simple, with $m\ge2$ vertices and $E$ edges. Label its vertices and fix an order on each neighbor list. For $i<j$,

\[
B_i=\prod_{e\ni i}Z_e,\qquad
A_{ij}=X_{ij}\prod_{k<_i j}Z_{ik}\prod_{l<_j i}Z_{jl},
\qquad A_{ji}=-A_{ij},
\]
\[
T_{ij}=\frac{i}{2}A_{ij}(B_i-B_j),\qquad
S_C=i^{|C|}\prod_{(i,j)\in C}^{\rm ordered}A_{ij}.
\]

Each $A$ flips only its own edge bit. Distinct $A$'s anticommute exactly when their edges meet. The cycle phase is $i^{|C|}$, including odd cycles and $i^6=-1$. All cycle operators commute with $A,B$. The theorem below concerns the **entire** $2^E$-dimensional edge space. It does not retain the original simultaneous $S_C=+1$ state constraint.

The [ice parent](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md), section “Exact conditional finite-component identities,” supplies only the literal degree-three binary-link domain and alternating geometric ring definition used in the corollaries. Its stochastic estimates, phase comparisons and physical interpretations are not inputs to this proof. No target value or fitted parameter enters.

## Theorem: full constrained-space dictionary

Introduce a finite CAR Fock space with operators $c_i$, parity $P_i^f=1-2c_i^\dagger c_i$, and Majorana $\gamma_i=c_i+c_i^\dagger$. Tensor it mathematically with one link qubit per edge. Define

\[
\mathcal G_i=P_i^f\prod_{e\ni i}Z_e^g,
\qquad
\widetilde A_{ij}=-i\gamma_i\gamma_jX_{ij}^g,
\qquad \widetilde B_i=P_i^f,
\qquad \widetilde Z_e=Z_e^g.
\]

Let $\mathcal H_G$ be the simultaneous $\mathcal G_i=+1$ subspace. There is an explicit unitary $W:\mathcal H_{\rm edge}\to\mathcal H_G$ satisfying

\[
W A_{ij}W^\dagger=\widetilde A_{ij},\quad
W B_iW^\dagger=P_i^f,\quad
W Z_eW^\dagger=Z_e^g,
\]
\[
W T_{ij}W^\dagger=(c_i^\dagger c_j+c_j^\dagger c_i)X_{ij}^g,
\qquad
W S_CW^\dagger=\prod_{e\in C}X_e^g,
\]

where all right-hand operators are restricted to $\mathcal H_G$.

### Gauss basis and dimension

Write electric edge bits as $x\in\{0,1\}^E$. The constraints uniquely fix

\[
n_i(x)=\sum_{e\ni i}x_e\pmod2.
\]

Therefore $\{|n(x)\rangle_f\otimes|x\rangle_g\}_x$ is an orthonormal basis of $\mathcal H_G$, which has dimension $2^E$. All $m$ Gauss constraints are independent on the enlarged $2^{m+E}$-dimensional tensor product. Their product is total fermion parity, not the identity on that enlarged space; on $\mathcal H_G$, it enforces even parity. This construction does not supply an independent odd-parity sector.

Each $\widetilde A$ commutes with every $\mathcal G_i$: at each endpoint its Majorana and link $X$ contribute two cancelling signs. Its $A$-$A$ and $A$-$Z$ commutation relations equal the native ones. On $\mathcal H_G$, $P_i^f=\prod_{e\ni i}Z_e^g$.

### Explicit phase and absence of a global sign obstruction

Use the Fock convention $|n\rangle=\prod_i(c_i^\dagger)^{n_i}|0\rangle$ in increasing label order. For $i<j$, direct right-to-left Majorana action gives

\[
\gamma_i\gamma_j|n\rangle
=(-1)^{\sum_{i\le v<j}n_v}|n\oplus e_i\oplus e_j\rangle.
\]

For the edge $e=(i,j)$, let $w_e$ be its native ordered-star mask, and let $\ell_e$ be the mod-two sum of incidence rows of vertices $i,\ldots,j-1$. Native and enlarged edge-toggle amplitudes are respectively

\[
a_e(x)=(-1)^{w_e\cdot x},\qquad
b_e(x)=-i(-1)^{\ell_e\cdot x}.
\]

Set $M_e=w_e\oplus\ell_e$. Then $M_{ee}=1$: edge $e$ crosses that vertex interval once and is omitted from its own ordered-star mask. For distinct edges $M_{ef}=M_{fe}$. Indeed, native and enlarged amplitudes have the same pairwise commutation sign; dividing their two elementary-square identities cancels that sign and gives this symmetry.

Define

\[
d(x)=(-i)^{|x|}(-1)^{\sum_{e<f}M_{ef}x_ex_f},
\qquad
W|x\rangle=d(x)|n(x)\rangle_f\otimes|x\rangle_g.
\]

Its toggle ratio is

\[
\frac{d(x\oplus e)}{d(x)}=-i(-1)^{M_e\cdot x}
=\frac{b_e(x)}{a_e(x)}.
\]

This includes the reverse toggle $x_e=1$. It proves $WA_{ij}=\widetilde A_{ij}W$; diagonal $B,Z$ intertwining is immediate. Equivalently, the ratio is a flat phase on the edge-bit hypercube: involution cancels backtracking and matching pair commutators cancel elementary squares. These generate all path relations. No additional Jordan–Wigner or winding phase assumption is needed. The displayed $W$ is not asserted to be a local physical circuit.

### Hopping, loops and the full algebra

Expanding the Majoranas with $P_i^f$ gives the displayed dressed CAR hopping. Along an oriented simple cycle, neighboring Majoranas cancel in their existing order, without a permutation:

\[
i^r\prod_{a=0}^{r-1}
(-i\gamma_{v_a}\gamma_{v_{a+1}}X_{e_a}^g)
=i^r(-i)^r\prod_{a=0}^{r-1}X_{e_a}^g
=\prod_{e\in C}X_e^g.
\]

The construction therefore covers every simple cycle, not only elementary squares. Products of $Z$'s generate individual electric-basis projectors; products of $A$'s connect every pair of edge strings with nonzero amplitude. Together they generate all matrix units. Thus the identities give an isomorphism of the full physical matrix algebras, not merely matching dimensions or a few generators on selected states.

The old fixed $S_C=+1$ code is the corresponding fixed positive Wilson-loop sector. Pure native hopping still commutes with every $S_C$, so retaining all sectors does not alone make their flux dynamic. Electric terms or the gates below can mix them. Literal Record projectors $(I+zZ_e)/2$ map to the same electric-link projectors; this supplies no event-occurrence law and does not authorize changing permanent Records.

## Corollary: gated ice rings on the same carrier

On an even periodic cubic graph with $L\ge4$, set $n_e=(1-Z_e)/2$ and restrict to exactly three occupied incident edges per vertex. Let $F_p$ select alternating face patterns $0101,1010$. Toggling a face changes its corner degree by

\[
2-2(n_{\rm previous}+n_{\rm next}).
\]

All four changes vanish exactly for those alternating patterns. Since $S_p$ toggles precisely the face bits, its diagonal Pauli dressing does not change this criterion. Hence

\[
P_{\rm ice}S_pP_{\rm ice}=F_pS_p\big|_{\mathcal H_{\rm ice}},
\qquad [F_p,S_p]=0,
\]
\[
W(F_pS_p)W^\dagger=F_p\prod_{e\in p}X_e^g.
\]

The last operator is the ordinary partial ring toggle. Thus the restricted Hamiltonian $\sum_p(VF_p-JF_pS_p)$ has exactly that ring dictionary. The ice constraint, gate, relaxed cycle state space and real $V,J$ are supplied. Ungated ambient $S_p$ generally leaves ice. On the ice space $B_v=-1$, so native $T_{ij}$ vanishes; ring kinetics is not generated by those zero hopping terms.

## Corollary: low-charge signed transport

Keep the six-valent bipartite graph and define

\[
G_v=\sum_{e\ni v}n_e-3,\qquad
Q_v=\epsilon_vG_v,\qquad
\epsilon_v=(-1)^{v_1+v_2+v_3}.
\]

Supply $P_{\rm low}$, the diagonal projector onto $|G_v|\le1$. Then

\[
B_v=-(-1)^{G_v},\qquad
\frac{I+B_v}{2}=Q_v^2,\qquad
N_{\rm native}=|V|-\sum_vQ_v^2.
\]

A nonzero native edge hop requires differing endpoint $B$'s, so on this domain exactly one endpoint is charged. If initially $G_i=s=\pm1,G_j=0$, toggling the common bit changes both values by $\delta=1-2n_{ij}$. The final low-charge gate requires $\delta=-s$, giving $(G_i',G_j')=(0,-s)$. Because $\epsilon_j=-\epsilon_i$, the same signed $Q$ moves from $i$ to $j$. The reversed case is identical. Thus $P_{\rm low}T_{ij}P_{\rm low}$ preserves separately the positive and negative defect counts and native number. The native phase is retained; allowed amplitudes have magnitude one.

For an oriented edge define $E_{ij}=\epsilon_i(n_{ij}-1/2)=-E_{ji}$. Then $Q_i=\sum_jE_{ij}$. A signed charge $q$ moving $i\to j$ changes $E_{ij}$ by $-q$. On the closed bipartite torus $\sum_vQ_v=0$ identically; isolated single-charge states are not part of this domain. This integer divergence is a link-state identity, not a new independent matter Gauss generator.

Every $F_pS_p$ commutes with all $G_v,Q_v$ and $P_{\rm low}$. Consequently the finite supplied Hamiltonian

\[
H=\sum_p(VF_p-JF_pS_p)
+t\sum_{\langle ij\rangle}P_{\rm low}T_{ij}P_{\rm low},
\qquad V,J,t\in\mathbb R,
\]

is self-adjoint on the low-charge space and preserves both signed species. The hopping gate can be localized to its two endpoint low-charge projectors, since all other $G_v$'s commute with that hop. The graph support is bounded, including ordered-star dressings; this is not a proof of allowed fine-lattice nearest-neighbor dynamics.

Under $W$, the hopping is precisely the low-charge projection of the CAR–$Z_2$-link term, and $c_v^\dagger c_v=1-Q_v^2$. The mobile defects are holes relative to the filled fermion background. Their signs depend on the electric configuration, not on two independent on-site CAR species. The integer low-charge restriction is stronger than the mod-two Gauss equation.

## Corollary: directed three-hop exchange algebra

Let $t^s_{ab}$ denote the projected hop with source $b$, target $a$, and initial $Q_b=s,Q_a=0$. For distinct neighbors $j,k,l$ of $i$,

\[
t^s_{il}t^s_{ki}t^s_{ij}
=-t^s_{ij}t^s_{ki}t^s_{il}.
\]

Both orders have the same initial support: $Q_j=Q_l=s,Q_i=Q_k=0$, with toggles $\delta_{ij}=\delta_{il}=\epsilon_i s$ and $\delta_{ik}=-\epsilon_i s$. Distinct edges do not change each other's bit condition. In both histories the center has successive charges $0,s,0,s$, so either both intermediate paths survive or both products vanish. Each permitted directed hole move has initial $B_{\rm target}=-1,B_{\rm source}=+1$, hence equals $-iA_{\rm target,source}$ on its domain. Reversing the three pairwise-anticommuting incident $A$'s contributes minus one. This proves the full operator identity, not just its transition probabilities. It does not establish a deconfined quasiparticle or relativistic statistics interpretation.

## Imports, scope and prior work

Fermion encodings and constrained gauge representations are standard mathematical ideas. This note establishes the explicit native phase convention and full electric/loop dictionary; it does not claim historical priority. The earlier [supplied U1-link construction](THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md) adds a second designed physical link role. Here the enlarged tensor space is redundant and constrained. The exact $Z_2$ dictionary neither replaces that distinct model nor derives an independent $U(1)$ matter–link factorization.

The native graph and role placement, ordinary tensor composition and Pauli dictionary are supplied. The corollaries additionally supply relaxed fixed-cycle constraints, ice/low-charge gates, Hamiltonian use and coefficients. No formation probabilities, physical action selector, continuum limit, photon, deconfinement or TOE closure is established. Record readout maps algebraically; occurrence and control selection remain open. No negative overlap theorem is a claim of this block.

## Live and independent evidence

The [primary runner](../scripts/native_dynamical_cycle_dictionary_2026_09_08.py) executes the three local helpers and records their actual scientific payloads and hashes. The author helper covers every column on triangle, square, intersecting-cycle square, reversed neighbor orders and hexagon: 6,712 exact checks. A separately implemented dense Jordan–Wigner pentagon/chord helper checks 15 exact matrix groups plus the Gauss census and missing-phase adverse guard. The independent local exchange helper checks 1,188 low-charge count representatives and two guards; its two nonzero local domains fail the unsigned identity. Those boundary representatives are supporting local phase controls, not a global state-existence census.

The [durable packet](../.claude/science/physics-loops/native-dynamical-cycle-dictionary-20260908/HANDOFF.md) preserves the original proofs, prospective contracts, raw results, quadratic supplement, independent review and actual mutation outputs. Finite checks support the general proofs; no numerical phase-of-matter inference is made. Canonical review and formal audit remain separate.
