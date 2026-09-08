---
claim_id: native_u1_pair_operator_and_all_low_support_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Exact off-defect-number pair operator in the supplied redundant U1 carrier and constructive connectivity of all low native A support. No sign-free, mixing, energy, physical occurrence or coupling-selection conclusion."
upstream_dependencies:
  - native_low_charge_u1_dictionary_note_2026-09-08
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/native_u1_pair_and_all_low_support_2026_09_08.py
---

# Native pair channels and connected low-charge support

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

The low-projected native edge operator has both hopping and opposite-charge pair channels, with a phase fixed by the corrected unitary dictionary. Allowing every such edge move connects the full low-charge support on any connected finite simple six-regular bipartite graph. Connectivity does not remove the closed fermionic phase obstruction.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite operator/support statements under the supplied native algebra and low-domain restriction."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Dependencies and model dictionary

Use the [corrected signed-defect U1 dictionary](NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md) and [full native fermion/Z2 dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), with the [native instrument Pauli conventions](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). The physical carrier remains the original edge-bit Hilbert space; two species and electric links are constrained redundant coordinates, not added physical registers. Magnetic-cycle constraints are relaxed and the low-charge projection is supplied. Signed Gauss charge is distinct from the prior conserved defect-number quantity. An A coupling need not preserve that quantity.

The two complete reviewed proofs below retain their original statements and provenance. Part I uses the even cubic torus scope of its dictionary parent. Part II's support-only theorem applies more generally to the stated six-regular bipartite graphs. Its phase witness is established on the actual cubic carrier and independently on K6,6; no universal sign-frustration claim for every graph is needed.

## Part I: exact pair operator

# Native low-projected A edge includes gauge-invariant pair channels

## Frozen premises and orientation

Use the actual full native dictionary W A_ij W†=-i gamma_i gamma_j X_e (i<j), and the corrected signed-defect U1 map of native-low-charge-u1-dictionary/DERIVATION.md a70724ba. The latter uses site-major species CAR f_{v,+},f_{v,-}, no double occupancy, spin-half links E=x-1/2 and exact Gauss divE=rho=n_+-n_-. Its unitary phase is d(x)s0(I)b_D, where s0=(-1)^sumI is the correct increasing-hole basis phase and b_D=(-1)^[D(D-1)/2] is an explicitly optional block phase. The graph is the stated even cubic torus, all extents>=4, full low-charge domain and relaxed cycle constraints. This note keeps b_D exactly as previously tested; off-D signs therefore require a new derivation.

Orient a physical edge from black b to white w. L^+=|1><0| raises E and L^-=|0><1| lowers it. Define A_bw by the native antisymmetric convention; for the physical ascending edge i<j, A_ij=kappa A_bw, with kappa=+1 if b<w and -1 otherwise. This orientation factor must not be silently dropped.

## Complete projected operator

Let P_nd impose no-double occupancy and define the ordered bilinear

    B_bw = f†_{b,+} f_{w,+} + f_{b,-} f†_{w,-}
           - f†_{b,+} f†_{w,-} - f_{b,-} f_{w,+}.

Then on the exact Gauss/no-double subspace,

    mathcal W (P_low A_bw P_low) mathcal W†
       = -i P_nd [B_bw L^+ - B_bw† L^-] P_nd.

Multiply by kappa for the ascending native edge operator. This is manifestly Hermitian since link and matter operators commute. Products of different-site fermion operators retain their displayed order. P_nd can be replaced by its two endpoint factors on the constrained domain. Projected flavor operators themselves are not asserted to satisfy full CAR.

For comparison, without the optional b_D phase the plus-ladder bilinear would be

    B0_bw = (f†_{b,+}+f_{b,-})(f_{w,+}+f†_{w,-}),

with all four expansion signs positive. The full operator is again -i(B0 L^+ - B0† L^-). The change is exactly the minus on both pair terms, not an adjustable hopping sign.

## Derivation and support table

In hole variables h†=c, h=c†, gamma=h+h†. In the site-major no-double encoding, an allowed change of signed charge by+1 at b is represented by f†_{b,+}+f_{b,-}; a change by-1 at w is represented by f_{w,+}+f†_{w,-}. The source factor -i gamma_b gamma_w fixes operator order. The ladder L^+ changes Qb by+1 and Qw by-1. Its complete allowed input/output table is

    (Qb,Qw)=(0,+1)  ->(+1,0): positive hole hops w->b;
    (-1,0)         ->(0,-1): negative hole hops b->w;
    (0,0)          ->(+1,-1): opposite pair creation;
    (-1,+1)        ->(0,0): opposite pair annihilation.

It requires x_e=0. The L^- table is its reversed transitions and requires x_e=1. Every other endpoint/bit combination either has zero ladder/CAR support, is killed by no-double projection, or would have |Q|>1 and is absent from the source low-projected column. These are all possibilities, because each toggle shifts the two signed charges oppositely by exactly one.

The electron-to-hole basis conversion is the corrected s0, not the earlier erroneous absolute phase formula. The extra b_D contributes b_{D±2}/b_D=-1 to pair creation or annihilation and contributes+1 to the hopping channels. That gives B_bw above. This matters even though all global physical D are even. It was invisible to the prior D-conserving hopping/ring tests and is independently checked here.

The Gauss transformation multiplies B_bw by exp[-i(theta_b-theta_w)] and L^+ by the inverse. Both hopping and pair monomials therefore commute with every Gauss generator. Pair creation has opposite charges, so gauge invariance does not require defect-number conservation. This is not gauge breaking of the old magnetic code: that code constraint is already relaxed, and the exact integer Gauss condition belongs to the redundant representation.

## Sector and Hamiltonian implications

The operator has nonzero D0->D2, D2->D0 and D2->D4 matrix elements on the actual carrier, with Hermitian reverses. Hence D and each species number are not conserved under a general supplied nonzero A coupling; pair terms change N+ and N- together. Their difference and all exact Gauss constraints remain conserved. This contrasts with the earlier T-only Hamiltonian, which preserves each signed species separately. Existing D-sector energy and connectivity theorems must not be transferred to a Hamiltonian containing these pair terms without a new argument.

P_low A P_low is not generally an involution on the low domain: forbidden toggles are killed by the intermediate projection, even though ambient A²=I. It connects the exhibited D sectors, but this note alone does not establish connectivity of the entire low domain. Adding real coefficients times these Hermitian operators is a new supplied Hamiltonian choice, not a derivation of occurrence, pair-production dynamics, coupling strength, relativistic particles or physical preparation.

## Exact bounded controls

The preregistered standalone checker directly evaluates native Pauli-string phases and compares them with the four-term species-CAR/ladders after the full d*s0*b_D map. It does not import the old executable or rely on its D-conserving outcomes. Twenty-four actual L4 initial configurations span D0 through16 and64; all192 initial edge columns are considered. Five hundred four forbidden initial columns are zero. Allowed columns are also checked at fixed non-backtracking second-edge selections, giving24596 composed two-edge paths including0->2->4 and2->0->2. The source phase and mapped phase agree at every tested step, not just after squaring one edge. Counts including repeated composition columns are disclosed in RESULT.json.

The deliberate omission of the b_D pair signs fails26918 tested pair-channel comparisons; conserving columns are not falsely expected to fail it. The run used9.58s and18.39MiB, below180s/384MiB. This is a selected-column/full-bit physical control, not an exhaustive L4 Hilbert-space census. The exact operator proof, rather than the finite count, supplies the general identity.

## Part II: constructive support theorem

# Connectivity of the full low-charge carrier under native edge moves

Conditional theorem. Let G be a connected finite simple six-regular bipartite graph, with the native fixed vertex/neighbor ordering and unrestricted magnetic-cycle carrier. Orient each occupied edge bit from black to white and each unoccupied edge oppositely. The allowed space consists of orientations with outdegree 3+Q_v, Q_v in {-1,0,1}. Consider the support graph of all nonzero P_low A_e P_low matrix elements, with every edge generator available. This support graph is connected. Even cubic tori with extents at least four satisfy these premises. This theorem concerns the support graph, not phases, a physical formation law or a selected Hamiltonian.

1. A native A_e has one nonzero unit-modulus Pauli-string coefficient per bit column, toggling edge e. Projection retains exactly those toggles whose resulting endpoint charges remain in the low domain. An arrow a→b reversed by such a toggle changes Q_a by -1 and Q_b by +1. All other Q remain fixed. Thus a positive charge can move forward through neutral sites and can annihilate on arrival at a negative site. Reverses create an opposite-charge pair. The T-only model excluded these pair moves by its number-conserving operator choice.

2. If D=sum Q²>0, choose any positive vertex p. Let R be the vertices reachable from p by directed paths in the current orientation. No arrow leaves R. If R had no negative vertex, sum_R Q would be positive. But sum_R 2Q equals the number of outgoing boundary arrows minus incoming boundary arrows, which is nonpositive. Contradiction. There is therefore a simple directed path from a positive to a negative vertex. Stop at the first negative along it and retain the suffix beginning at the last preceding positive. Its interior is entirely neutral. Reverse its edges in path order. The positive moves through every neutral interior vertex and then annihilates with the final negative. Every intermediate is in the low domain and D decreases by exactly two. Repeating reaches an ice orientation. The number of toggles is at most D(V-1)/2. No min-cut-six condition is used.

3. Any two ice orientations differ on a balanced directed subgraph of the first: at every vertex the number of changed outgoing edges equals changed incoming edges. Decompose those changed edges into directed simple cycles. Reverse one cycle by toggling its edges consecutively around its arrow direction. The first toggle creates a negative charge at its tail and a positive at its head; the positive follows the rest of the cycle through neutral sites and annihilates at the initial tail. This uses exactly the cycle length toggles, remains in the low domain, and changes no other edge. After a cycle is removed, remaining changed directed cycles are unaffected. Hence any two ice orientations connect using at most E toggles. Six-regular finite graphs have an Eulerian orientation, so the ice domain is nonempty.

4. Reduce x and y separately to ice orientations, join those by step 3, and reverse the reduction path for y. This proves full support connectivity, with a path length at most (D_x+D_y)(V-1)/2+E, hence at most V(V-1)+E. This is a constructive upper bound on graph distance, not a mixing or spectral-gap bound.

An exact unitary dictionary, including the corrected U1 phase map, preserves this support connectivity. Off-D amplitudes still need a separate phase proof: the optional b_D phase now changes, so D-preserving controls cannot supply the operator formula. The supplied Hamiltonian H_A=sum_e lambda_e P_low A_e P_low, with every lambda_e real and nonzero, has this connected support: different edges toggle different bit columns, so these terms cannot cancel one another. No sign-free representation or Perron ground-state uniqueness follows. The existing D4 witness supplies an allowed six-edge word a,b,c,a,b,c on three distinct incident edges. Native canonical A_a,A_b,A_c pairwise anticommute and square to identity, so this word has product -I. Thus the A support also contains a closed phase -1, independently of any T-to-A phase conversion. This is an obstruction to diagonal sign erasure, not a general unitary obstruction. Pair creation is an operator channel here; no relativistic pair production or physical event protocol is inferred.

## Executable boundary and provenance

The primary runner reads and hashes this note, its three mathematical source parents, four live exact helpers, and the preserved D4 seed fixture. It executes both author and independent implementations. The author pair helper tests actual L4 native columns and composed paths; the independent helper uses a different vertex labeling and neighbor ordering and forms the adjoint automatically. The support helpers construct explicit paths on L4 and independently on K6,6. The closed minus word and omitted-pair-sign adverse controls are mathematical failures of the altered formulas, not intended failures of the theorem. Predicate totals count actual condition evaluations, including repeated columns; they are neither Hilbert dimensions nor exhaustive state counts.

The original scripts, prospective contracts, raw results, failed variants, corrected absolute-phase parent, nonzero-coupling qualifier history, and hash-specific cold reviews are preserved in the associated research packet. Canonical changes are reporting, portable paths, and explicit predicates that remain active under Python optimization. No source-side audit verdict is assigned.

The premises do not provide a probability rule, preparation instrument, physical A coupling, or its magnitude. Neither connected support nor the conditional U1 coordinates establish sign-free dynamics, ground-state uniqueness, a spectral gap, mixing, deconfinement, electromagnetic identification, or relativistic pair production. Fixed-D results from a T-only Hamiltonian do not transfer to the pair Hamiltonian.
