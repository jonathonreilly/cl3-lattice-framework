---
claim_id: native_low_charge_u1_dictionary_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Exact unitary from the supplied finite low-charge native edge carrier onto a redundant two-species CAR and spin-half-link Gauss/no-double subspace, intertwining physical electric observables, projected hopping and gated rings. The corrected all-sector basis phase is explicit. No independent physical role, electromagnetic identification, circuit, occurrence law or selected action."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/native_low_charge_u1_dictionary_2026_09_08.py
---

# A redundant signed-defect U(1) quantum-link dictionary

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

The supplied native low-charge carrier admits an exact representation by two species of fermionic defect coordinates and spin-half electric links, subject to Gauss and no-double-occupancy constraints. Its native hopping and gated rings become gauge-invariant quantum-link operators with their fermionic signs intact. The representation adds no independent physical register and does not select an electromagnetic theory.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite intertwiner under the supplied low-charge domain and native algebra."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Source and domain

Use the [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) at its reviewed PR8038 source, with its vertex and neighbor orders. Its Pauli convention comes from the [native instrument source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). These are provisional mathematical dependencies, not an audit verdict or a derived physical choice of the domain.

Fix a finite periodic cubic graph with each extent even and at least four. Relax the fixed magnetic-cycle constraint and impose no winding restriction. For physical edge bits $x_e=(1-Z_e)/2$, define

\[
\epsilon_v=(-1)^{v_1+v_2+v_3},\qquad
G_v=\sum_{e\ni v}x_e-3,\qquad Q_v=\epsilon_vG_v.
\]

The physical space here is precisely the span of bit configurations satisfying $|Q_v|\le1$ at every vertex. Its dimension is the number of those configurations; the proof does not require their enumeration. The low-charge restriction, graph placement, ordinary composition and any Hamiltonian built from the operators below remain supplied.

The [earlier U1-link note](THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md) supplies a different model with an additional independent physical link role coupled to the earlier fermion-number charge. This note instead represents signed defects $Q$ redundantly on the existing edge carrier. It neither retires that earlier role-supplier obligation nor identifies $Q$ with its Noether charge.

## Redundant space and dimension equality

Introduce mathematical CAR modes $f_{v,+},f_{v,-}$ on an ordinary full Fock space, in site-major order $(0,+),(0,-),(1,+),(1,-),\ldots$, and one mathematical spin-half link for each existing edge. Orient links from black vertices ($\epsilon=+1$) to white vertices. Define

\[
E_e=x_e-\frac12=-\frac{Z_e}{2},\quad
L_e^+=|1\rangle\langle0|=\frac{X_e-iY_e}{2},\quad
L_e^-=|0\rangle\langle1|=\frac{X_e+iY_e}{2}.
\]

Thus $[E_e,L_e^\pm]=\pm L_e^\pm$, $(L_e^\pm)^2=0$ and $E_e^2=I/4$. These are nonunitary spin-half ladders, not rotor link operators. The ket definitions fix the sign convention independently of names for Pauli raising operators.

Impose simultaneously

\[
n_{v,+}n_{v,-}=0,\qquad
\mathcal G_v=(\operatorname{div}E)_v-\rho_v=0,\qquad
\rho_v=n_{v,+}-n_{v,-}.
\]

All six incident links point outward at black vertices and inward at white vertices, so $\operatorname{div}E=\epsilon_v(\sum x_e-3)=Q_v$. For each electric string, these constraints allow exactly one matter assignment if $Q_v\in\{0,+1,-1\}$ everywhere: vacant, positive or negative respectively. They allow none otherwise. Hence the constrained enlarged basis has exactly the same cardinality as the physical low-charge basis. Without no-double occupancy, a neutral vertex would permit both vacancy and the doubly occupied state, invalidating this argument. On the closed graph, $\sum_vQ_v=0$, so $N_+=N_-$ and $D=N_++N_-$ is even. No additional parity projection is missing.

## Corrected all-sector phase map

The source unitary obeys

\[
W|x\rangle=d(x)|n_c(x)\rangle\otimes|x\rangle,\qquad
n_{c,v}=\sum_{e\ni v}x_e\pmod2=1-Q_v^2,
\]

where $d(x)$ is the source-defined quadratic native phase. Put $h_v^\dagger=c_v$, $h_v=c_v^\dagger$ and let the filled electron state $|F\rangle$ be the hole vacuum. For an increasing list $I$ of hole sites,

\[
|I\rangle_h=\prod_{v\in I}^{\text{increasing}}c_v|F\rangle
=s_0(I)|n_c\rangle,\qquad s_0(I)=(-1)^{\sum_{v\in I}v}.
\]

The product acts rightmost first: each larger-index removal leaves all lower occupied indices unchanged, giving its factor $(-1)^v$. This is the absolute hole-basis identity. In particular $c_0c_1|11\rangle=-|00\rangle$.

Replace every hole at $v$ by the unique species sign $Q_v$, retaining site-major order. One may separately choose a constant phase in each $D$ block. To preserve the originally tested operator map, choose $b_D=(-1)^{D(D-1)/2}$. It is an optional block phase, not part of the preceding hole-basis identity. An explicit all-sector unitary is therefore

\[
\mathcal W|x\rangle=d(x)s_0(I(x))b_D
\left|n_{v,+}=\mathbf1_{Q_v=+1},\ n_{v,-}=\mathbf1_{Q_v=-1}\right\rangle\otimes|x\rangle.
\]

It is onto and norm-preserving because it maps each orthonormal basis element to its unique constrained basis element with a unit-modulus phase. This formula does not use the exceptional D2 charge-first ordering or remove same-species exchange signs. It gives

\[
Z_e=-2E_e,\quad Q_v=\rho_v,\quad
D=\sum_v\rho_v^2=N_++N_-,\quad
B_v=2\rho_v^2-1,\quad N_c=|V|-D.
\]

## Hopping with its particle-hole sign

For a black-to-white edge $i\to j$, let $P_{\rm nd}$ be the no-double projector and define

\[
K_e=-P_{\rm nd}\left[
 f_{j,+}^\dagger f_{i,+}L_e^-
 +f_{j,-}^\dagger f_{i,-}L_e^+
 +\mathrm{h.c.}\right]P_{\rm nd}.
\]

On the simultaneous Gauss/no-double space,

\[
\mathcal W(P_{\rm low}T_eP_{\rm low})\mathcal W^\dagger=K_e.
\]

Indeed the source $W$ gives $(c_i^\dagger c_j+c_j^\dagger c_i)X_e$. For distinct sites, particle-hole conversion gives $c_i^\dagger c_j=-h_j^\dagger h_i$. A permitted low-charge move transfers one hole from a charged source to a neutral target and preserves its signed $Q$. In site-major species order, its species bilinear has exactly the single-hole CAR sign: every intervening occupied site contributes one fermion, regardless of species, while the unused endpoint slots are empty. Transport of charge $s$ from black to white changes $E$ by $-s$, selecting $L^-$ for positive and $L^+$ for negative. Reverse moves are adjoints.

This checks both amplitudes and support: two occupied endpoints either vanish by Pauli exclusion or are killed by the no-double projection, and Gauss fixes the permitted link change. The phase $d(x)s_0(I)b_D$ and ordinary species CAR retain the native signs. Every listed hop and gated ring preserves $D$, so the optional $b_D$ cancels in all claimed intertwining identities.

The unprojected $f$ operators obey CAR on the enlarged Fock space. Their projections into Gauss/no-double space are not claimed to obey full CAR. The displayed $K_e$ is an even projected bilinear; its global no-double notation may be replaced by endpoint factors on the constrained domain. This does not furnish a fine-lattice native circuit.

## Rings and compact gauge redundancy

For an oriented simple even cycle $C$, let $R_C$ be the product of $L^+$ on edges traversed black-to-white and $L^-$ on edges traversed in reverse. Then $R_C+R_C^\dagger$ is the alternating ring toggle. For each elementary plaquette,

\[
\mathcal W(F_pS_p)\mathcal W^\dagger=R_p+R_p^\dagger.
\]

The source $W$ removes the native cycle dressing, and an alternating ring preserves $Q$, the matter labels and all additional phases. The ungated ambient $S_p$ is not identified with this partial ladder ring: it can change labels or leave the low-charge domain.

The commuting generators $\mathcal G_v$ define $\exp(i\sum_v\theta_v\mathcal G_v)$. Their spectra are integers on the six-valent spin-half domain, so each angle is $2\pi$-periodic. Under conjugation,

\[
f_{v,s}\mapsto e^{is\theta_v}f_{v,s},\qquad
L_{ij}^+\mapsto e^{i(\theta_i-\theta_j)}L_{ij}^+.
\]

The phases cancel in each hopping monomial and closed ring; $P_{\rm nd}$ commutes with all generators. Thus these operators commute with every $\mathcal G_v$, also as ambient operators with no-double projection. Gauge transformations act trivially on the constrained physical states, as a redundancy should.

This is a compact U1 quantum-link presentation, not an independent physical matter/link factorization, rotor theory or electromagnetism. The signed charge differs from total hole number. Separate conservation of species under the displayed hopping does not identify those generators with the earlier Noether charge.

## Evidence, correction and prior art

The paired runner executes 31232 explicit helper predicates under optimization: 8003 author, 22359 independent, 512 absolute-phase and 358 domain predicates. Counts include support/resource guards and repeated columns, not distinct physical states. The author controls compare direct native phases against species CAR and link ladders on 24 actual L4 configurations spanning $D=0,2,\ldots,16,64$, including the complete delivered D4 exchange seed. All 256 permitted hop columns and 2348 alternating ring columns agree. A separate six-site label enumeration checks 4860 CAR columns. Independent different-label/different-neighbor-order controls check 400 hops and 2096 rings on 22 configurations. These are selected physical columns, not a full L4 census. The basis proof supplies the all-sector result.

Root found an actual error in the original absolute hole-basis prose. Earlier bytes remain in the [packet](../.claude/science/physics-loops/native-low-charge-u1-dictionary-20260908/HANDOFF.md): the extra $b_D$ had been incorrectly included in the hole-basis identity. Conserving-operator controls could not detect it because they preserve $D$. The corrected identity $s_0=(-1)^{\sum I}$ is separately tested by literal Fock annihilation on all 510 subsets for one through eight modes; the old identity fails 255. The existing tested map is preserved by declaring $b_D$ separately. No off-diagonal-in-$D$ operator identity is inferred from the old tests. New portable controls also check the Gauss/no-double domain and execute actual minus-sign, Gauss-sign, no-double and absolute-phase mutants.

The preserved primary-source comparison identifies standard methodology: [Chandrasekharan and Wiese](https://arxiv.org/abs/hep-lat/9609042) construct spin quantum links; [Zohar and Cirac](https://arxiv.org/abs/1805.05347) and their [later matter-removal work](https://arxiv.org/abs/1905.00652) explain constrained transfer of matter/statistics into gauge variables. Their different matter and link hypotheses are not imported wholesale as a proof here. The independent comparison records the exact sections read; this port does not claim a fresh complete literature search or historical priority.

Graph placement, relaxed code constraints, low-charge gates, coefficients, physical preparation and occurrence remain supplied or unresolved. A Hilbert-space unitary does not select an action, identify a physical photon, derive a local schedule or implement a circuit. No old physical-role obligation is declared retired.
