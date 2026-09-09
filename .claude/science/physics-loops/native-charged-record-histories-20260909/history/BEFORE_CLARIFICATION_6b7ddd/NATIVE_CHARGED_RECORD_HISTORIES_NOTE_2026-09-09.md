---
claim_id: native_charged_record_histories_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied full native edge carrier and Record instrument: local gauge-frame correction, charged history maps, projective order phases and transported matter observables. No formation-law or Born selection."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_charged_record_histories_2026_09_09.py
---

**Status:** conditional-support. **Type:** bounded_theorem.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: supplied native carrier, phase convention and Born/Lueders Record instrument
trace_class: frontier_discovery
reachability_to_target: supports
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

The load-bearing parents are the [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) and the [native Record instrument](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). This branch is stacked on the actual unmerged dictionary revision86e03ef9; latest main was inspected for overlap, not imported as generated audit state. The construction adds no physical site factor. It does not supply a preferred placement, initial state, event law or control pulse.

# Constructive local correction for a full-carrier native edge Record

Finite conditional theorem, supported by the exact controls reported below. Supplied premises: finite simple ordered native edge graph, ordinary tensor composition, the phase-correct8038 dictionary, and the stipulated physical Z/Born Record instrument. No formation probability, rate, covariant role placement or axiomatic Born rule is supplied by this construction. It applies to arbitrary full-carrier states, including coherent Wilson-sector superpositions.

Use8038 conventions: W_G|x>=d_G(x)|∂x>_f|x>_g, d_G(x)=(-i)^|x|(-1)^q_G(x), M=w⊕ell, q=Σe<f Mef xe xf. For e=(i,j), i<j, w_e is its ordered-star mask and ell_e is the sum of incidence rows from i through j−1. Native A_e=X_e Z_{w_e}; enlarged A_e=(-iγ_iγ_j)X_e^g. Relative orders on surviving edges and neighbor lists are inherited after deletion.

Write x_e=a∈{0,1}, z=(-1)^a, G'=G−e, and y for the remaining electric bits. The raw contraction L_e^a=<a|_e maps the all-positive Gauss space of G into the charged Gauss space on G' with charges z at i,j. This is the most direct gauge-correct map: retain these two signs as record content. Every old Record is unchanged. The maps have complete effects (L_e^a)†L_e^a=Π_e^a on the constrained input.

If an all-positive Gauss frame on G' is desired, let C_e=-iγ_iγ_j. It is an even Hermitian involution and flips precisely the two endpoint Gauss signs. Thus (C_e)^a L_e^a maps into the all-positive sector. It is an algebraic frame correction; it is not asserted to be a permitted standalone gauge-invariant operation on the original G physical space. Its conjugation also changes the endpoint occupation convention, so the original number observable must be transported rather than renamed as the new bare number.

## The local cancellation identity

Define D_e^a=(Z_{w_e restricted to E−e})^a on surviving native edge qubits. Then, column by column,

    C_e^a L_e^a W_G = W_{G'} D_e^a <a|_e.                 (1)

For a=0 the restricted phases agree. For a=1, M_G restricted to surviving rows/columns equals M_G' because removal preserves neighbor orders and incidence restrictions. Hence

    d_G(y,1)/d_G'(y)=(-i)(-1)^(Σf≠e Mef yf).

The fermion occupation before correction is n=∂y⊕e_i⊕e_j. Direct CAR gives C_e|n>=-i(-1)^(Σi≤v<j nv)|n⊕e_i⊕e_j>. The interval contains i and not j, so its extra endpoint contribution is1. Multiplying the two phases yields

    (-i) i (-1)^((M_e⊕ell_e)·y)=(-1)^(w_e·y),

which is exactly D_e. No uncancelled long Jordan–Wigner string survives in this native correction. Its support is within the two endpoint stars, at most deg(i)+deg(j)−2 edges. It is a product of commuting native Z phase operators; using it as physical feedforward would still require a supplied control law. Equation(1) itself is a dictionary/state-action theorem without that control assumption.

## Complete instrument and adjacent-history phase

The corrected native Kraus map is K_e^a=D_e^a<a|_e. It is a coisometry from its outcome subspace to the surviving full native carrier and Σa K_e^{a†}K_e^a=I. Arbitrary initial states have arbitrary legal Born outcome probabilities; the fixed-cycle nonbridge fair-isometry result cannot be extended to them. For example an electric basis state fixes every outcome, even if e lies on a cycle.

For two different edges e,f and outcomes a,b, compare the corrected maps in the two orders, inheriting all surviving orders. Their final diagonal factors on the remaining edges agree. The only discrepancy is the phase from the first correction on the edge that is subsequently recorded:

    K_(G−e),f^b K_G,e^a = (-1)^[ab(w_ef+w_fe)] K_(G−f),e^a K_G,f^b,

where each K is defined using the graph indicated in its subscript, with inherited neighbor orders, and both sides identify the same final output ordering. Native A commutation gives w_ef+w_fe=1 exactly when e,f meet, and0 otherwise. Consequently the branch CP maps commute exactly even when the Kraus amplitudes acquire a minus sign. The sign cannot be dropped in a coherent history dilation; it is an outcome/history-dependent scalar cocycle. Adjacent transpositions generate the full permutation relation, so the sign for any order is the parity of inversions among recorded-one edges that share a vertex. This gives a complete computable history correction rather than an assumed phase-free composition rule.

The raw charged-sector deletion maps commute as actual contractions. Choosing positive-Gauss frames trades that simple composition for the explicitly tracked projective sign. This distinction explains why a correction is needed and does not introduce a physical gauge anomaly.

## Indexed refinement supplied and unsupplied

For a finite recorded set R, the native Born outcome probabilities have exact marginalization over finer outcome lists. At the state-action level the output carriers differ: the raw deletion instrument satisfies the precise relation

    Σ_b J_S^b (J_R^a ρ J_R^{a†}) J_S^{b†} = Tr_S(J_R^a ρ J_R^{a†}),

for S disjoint from R, with J the ordinary tensor contractions. This is refinement compatibility through the stated discard channel, not equality of the coarse and fine postmeasurement states on a common unchanged carrier. If recorded qubits are retained instead of deleted, forgetting their outcomes leaves dephasing, not the original state. In the positive-Gauss corrected frame the corresponding connecting channel is the explicit outcome-controlled correction followed by discard. This is a genuine finite physical-carrier CP diagram, but it does not license treating different experiments as the same state-action merely because their scalar effects refine.

The ordinary number observable is also transported: for recorded boundary bit b_v=Σ_{e∈R,e incident v} a_e mod2, original occupation is b_v+(−1)^b_v n'_v in the positive-Gauss frame. Renaming Σn'_v as the old number would incorrectly claim number-changing Record dynamics. Charged sectors retain the old occupation convention directly.

This supplies a finite indexed instrument construction on the stated native carrier. It does not derive which R forms, a nearest-neighbor admissibility law for the quantum state, a scheduler or a permanent-record dynamical realization.

Scope relative to prior work: the dictionary parent already maps the effect and the native instrument parent already gives fixed-code instruments. The proposed increment is the local cancellation(1), full-carrier charged-frame update and all-history projective composition. No literature-priority claim is made.

## Surviving matter dynamics and uniqueness of the frame correction

For a finite history (R,a), define b=∂a on vertices and

    W_R^a|y>=d_G(y,a)|∂y⊕b>_f |y>_g.

This is onto the charged sector G'_v=(-1)^b_v, has dimension2^|E−R| even when the remaining graph is disconnected, and is an exact branch dictionary. Original surviving A_f and B_v are obtained by substituting every recorded Z_e=(-1)^a_e in the original native words. Their enlarged charged-sector representatives remain −iγ_iγ_j X_f and fermion parity P_v. Therefore a prescribed native hopping dwell after any history is represented by the same charged-sector number-conserving CAR hopping, with all original particle observables retained. No inverse, fixed Wilson state or Gaussian assumption enters.

An all-positive-frame transformation flips the occupation convention at vertices with b_v=1. For a single recorded-one edge, C_e c_v C_e is −c_v† at either endpoint and c_v elsewhere. A hopping term with exactly one corrected endpoint consequently becomes a pairing-form term in the new coordinate variables. This is not physical production of particles: the conserved original number is Σ_v[b_v+(−1)^b_v n'_v], not Σ_v n'_v. Keeping the charged dictionary is often the cleaner physical description.

At one deletion, once both phase conventions W_G and W_G' and the endpoint correction C_e are fixed, equation(1) determines D_e up to an outcome-only scalar. The surviving full native algebra is a full matrix algebra, so any other unitary intertwining the complete same observable map differs by a scalar. This is a conditional uniqueness of a dictionary correction, not uniqueness of a Record instrument among all operations with the same binary effect.

## A usable finite instrument supplier, and the unclosed physical step

The data (original graph, phase convention, recorded configuration) now determine the output carrier, all charged Gauss constraints, branch state map, observable dictionary, original number, and surviving hopping action. No extra blank pointer factor is introduced. These are explicit, composable functions of the actual Record outcomes, and they remain valid for non-Gaussian input and coherent magnetic sectors. The raw charged maps compose exactly; the standardized positive-frame maps compose with the displayed scalar cocycle.

This is useful as a supplier interface for a downstream physical law, but it cannot identify that law from the axioms: the choice of carrier/roles, initial quantum state, Born instrument, occurrence and dwell remain supplied. In particular the construction has not shown that its general Born conditional outcome probability is a function only of nearest-neighbor Record conditions. It would be incorrect to relabel an arbitrary quantum posterior as the axiom's local admissibility distribution. The exact next positive target is a specified native state/dwell family for which that conditional locality and a physical formation mechanism can both be proved; an arbitrary controller or a newly chosen scalar menu would not discharge it.


## Permanent outcome register and finite evidence

An instrument retains an abstract classical outcome label a with each branch. The physical recorded edge retains its fixed value; deleting its factor is a mathematical representation of the surviving degrees of freedom, not erasure of a permanent Record. A comparison that forgets a finer label is a channel on mathematical output descriptions, not a physical reversal of formation. Charged sectors with different boundary signs must remain distinguished by those labels. The positive-Gauss correction may be used as a frame change without claiming it is a physical gauge-invariant pulse on the old graph.

The primary runs416 exact one-edge full-carrier columns and736 two-edge history columns on a triangle, a path and a chorded square, with both neighbor orders. Omitting the local phase fails80 columns. The52609 structural predicate visits include repeated M-symmetry checks; they are not independent physical cases. A separate146-control exact CAR/refinement calculation checks endpoint particle-hole conjugation, transported number, and the distinction between dephasing and discard. These finite fixtures support the implementation; the displayed general algebra proves the arbitrary finite-graph statement. No large numerical dynamics or empirical experiment is used.

The initial derivation's insufficiently qualified refinement sentence is preserved with its correction in the packet. A binary |+> density matrix explicitly distinguishes forgetting a Z outcome from doing nothing. Full state-action equality is never inferred from scalar marginalization. Current physical formation locality remains open even after this finite supplier interface is constructed.
