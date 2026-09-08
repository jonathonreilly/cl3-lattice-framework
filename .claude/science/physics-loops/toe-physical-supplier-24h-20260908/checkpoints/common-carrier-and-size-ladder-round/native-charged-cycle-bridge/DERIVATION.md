# Conditional charged-cycle operator bridge

The proposed support and conservation identities hold on the literal shared edge-qubit carrier. They give a constrained link-spin hopping model with signed divergence defects. They do not yet identify independent fermionic matter coupled to a Wilson electric field.

## Authority and domain

Read the complete positive bridge in `native-cycle-projected-ice-review/DERIVATION.md` and the native matter/instrument source Definitions, equations (1)–(4), and Theorem 1 in main's `NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER` note. The imported ambient operators are B_v=product incident Z, A_ij=X_ij times ordered diagonal Z dressings, and T_ij=i A_ij(B_i−B_j)/2. Native cycle S_p is a Hermitian monomial involution, toggling the four face bits and commuting with native A/B. No unsigned replacement of its phase is made here.

Take an even periodic cubic lattice of size L>=4, with six incident edges per vertex and bipartite sign epsilon_v. Put n_e=(1−Z_e)/2, G_v=sum_incident n_e−3 and Q_v=epsilon_v G_v. Supply the diagonal low-charge projector P onto all |G_v|<=1. Also relax the original fixed-cycle code: the state space here is P times the ambient edge Hilbert space. These are changed physical constraints, not deductions from the native axioms or a unitary mapping of the original code.

Since B_v=(-1)^(G_v+3)=−(-1)^G_v, on P the native hole projector h_v=(1+B_v)/2 equals G_v^2=Q_v^2. Thus N_native=sum(1−B_v)/2=|V|−sum Q_v^2. This is the complement, not the charge count itself. Globally sum Q_v=0 on this closed bipartite lattice, because each occupied edge contributes opposite signs at its endpoints and sum epsilon_v=0. Consequently positive and negative defects occur in equal numbers; arbitrary isolated single-charge states are not available on the torus.

## Exact hopping support and orientation

T_ij has a nonzero matrix element on a bit string precisely when B_i differs from B_j. Its sole bit toggle is n_ij, with magnitude one and its actual native complex Pauli phase retained. Within P, differing B means exactly one charged endpoint. Let initially G_i=s in {−1,+1}, G_j=0, and delta=1−2n_ij. The toggle sends both endpoint G values to G+delta. Survival of the final low-charge projection requires s+delta=0; otherwise the charged endpoint would have magnitude two. Therefore delta=−s and the final values are (0,−s). Since epsilon_j=−epsilon_i, the final Q_j=epsilon_j(−s)=epsilon_i s=Q_i. The same signed charge moves to the neighbor. The reverse case is identical.

Accordingly P T_ij P preserves separately the number of Q=+1 and Q=−1 defects, hence also native N. This is stronger than conservation of signed total charge alone, but does not permit pair creation. Its nonzero matrix element remains magnitude one; projection deletes inadmissible transitions, rather than changing their native phase.

For an edge directed i to j define E_ij=epsilon_i(n_ij−1/2), E_ji=−E_ij. Then Q_i=sum_j E_ij, an exact lattice divergence identity. On an i-to-j charge move of signed value q, delta E_ij=−q, so divergence loses q at i and gains q at j. This is the link-spin Gauss bookkeeping of the hopping. It supplies no extra electric energy term or continuum Maxwell normalization.

## Gated cycles and Hamiltonian

Let F_p select the two alternating face patterns. At each corner, a face toggle changes G by 2−2(n_previous+n_next). This vanishes at every corner exactly for alternating patterns. Diagonal Pauli dressing does not alter this statement. Hence F_p S_p commutes with every G_v, Q_v, B_v, native N, and P. Since S_p exchanges the two alternating patterns, [F_p,S_p]=0 and F_p S_p is Hermitian.

For real supplied V,J,t the finite restricted operator

H = sum_p [V F_p−J F_p S_p] + t sum_edges P T_ij P

is therefore self-adjoint on P and conserves both signed defect species. The hopping term need only use the two endpoint low-charge gates: other vertex G operators commute with T_ij. Thus this expression has bounded graph support, including the native ordered-star Z dressing; a global projection notation does not require a global gate in this finite algebraic construction. Physical midpoint placement still does not turn graph locality into a permitted nearest-neighbor microscopic interaction.

The gates are load-bearing. Ungated native T can move a low-charge input to |G|=2; ungated cycle S can alter corner charges. Neither is the stated restricted dynamics. Moreover P and F generally fail to preserve the original simultaneous cycle code. Retaining that code is not a silent additional option.

## What is and is not established

The result is an exact conditional operator structure: spin-half link divergence defects, charge-preserving face dynamics, and signed defect transport with native phases. The supplied low-charge constraint, relaxed code, gating, coupling constants and dynamical use are new assumptions. Hole occupations are functions of the same link bits, not an independent matter tensor factor. The original CAR theorem applies on its selected fixed-cycle code; it cannot simply be cited as a proof of fermionic exchange statistics for the new projected ambient model. Establishing a compatible matter/gauge factorization or a statistics-preserving dictionary would require a further theorem. No Wilson minimal-coupling, photon phase, action selection, Record occurrence or physical unification claim follows.

The existing positive ice bridge treated G=0 and vanishing native hopping. This extension identifies the exact nonzero charged support and its species conservation; no exhaustive repository novelty claim is made.

## Independent bounded controls

The prospective truth table enumerates all 2048 assignments of two six-edge stars sharing an edge, plus both bipartite orientations for accepted transitions and all 16 face patterns. It checks charge, species, hole count, oriented divergence and the necessity of face alternation. The rejected active low-charge transitions are retained as an adverse control. These checks certify diagonal transition support only; they do not pretend to reconstruct full native Pauli phases or prove statistics. The analytical proof above retains those phases explicitly.
