---
claim_id: native_weak_electric_spectator_gap_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied uniform full-native 4^3 model at t=1: exact rational residual certificate gives a positive sixth-order spectator coefficient; finite magnetic symmetry fixes the full nonscalar operator and physical parity yields a unique ground for sufficiently small nonzero electric penalty, with asymptotic gap. No explicit radius or larger-volume phase."
upstream_dependencies:
  - native_zero_penalty_l4_delayed_splitting_note_2026-09-08
runner: scripts/native_weak_electric_spectator_gap_2026_09_08.py
---

# Weak electric penalty selects a unique finite-L4 ground state

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

For the supplied uniform full native Hamiltonian on the 4×4×4 torus with hopping t=1, the electric penalty first splits its zero-penalty ground family at sixth order. The ordered adjacent spectator coefficient c has the exact certified enclosure 370.7628915198<c<370.7628915199. The entire nonscalar sixth-order operator is a free Majorana quadratic form fixed by finite magnetic symmetry. Its physical ground is unique, and the full finite Hamiltonian has gap 2c√24 u^6+O(|u|^7) for sufficiently small nonzero u. No explicit neighborhood, larger-volume phase or physical selection of this Hamiltonian is asserted.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied finite full-carrier Hamiltonian and exact dictionary; t=1."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Premises and result

Use the [finite L4 isolation and delayed-splitting theorem](NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md), [fixed-flux endpoint](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md), and [full Gauss/CAR dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md). The entire edge carrier is retained. Set H(u)=Σ_e A_e+uD and D=Σ_v Q_v². The supplied zero-penalty ground space P has dimension2^31, lies in one unique π-plaquette/positive-winding flux orbit, and is separated from its full complement by at least1/432. Its active Majorana matrix obeys K0²=−24I and K0_(0,16)=−2 in the declared canonical coordinates. Coefficients through fifth order are scalar on P.

Write the canonical effective Hamiltonian as

H_eff(u)=E0P+Σ_(j=1)^6 a_j u^j P+u^6 Q+O(|u|^7),

where scalar a_2,...,a_6 are not evaluated. The nonscalar term is

Q=−(c/2)Σ_(i<j)(K0)_ij iβ_iβ_j=(i/4)βᵀ(−cK0)β.

Here β_i are spectator Majoranas in the exact dictionary and c is the coefficient of iβ_0β_16. A complete independent exact rational residual replay certifies the stated strict decimal enclosure; each decimal endpoint denotes its exact rational value. A weaker portable gate 370<c<371 is sufficient for nonzero splitting. All six bridge families and2292 proper intermediate states are included; no subset is selected by its result.

The allowed leading levels are c√24(n−16), n=0,2,...,32, with multiplicities binomial(32,n). They sum to2^31 and have a unique lowest state, separated by2c√24. Consequently the full finite H(u) has a unique ground for sufficiently small nonzero real u and gap2c√24 u^6+O(|u|^7). Excited binomial multiplicities are properties of the leading coefficient, not exact degeneracies at nonzero u.

## Complete sixth-order spectator support

A nonconstant electric insertion is (1/2) Z_e Z_f for two incident edges. An ordered word of n insertions toggles at most2n links. Returning to the original magnetic orbit is equivalent to its toggle being a cut δS. In an unreduced link representative, all resolvents act only through even active Majoranas. Closing the cut contributes ∏_(v∈S)(−iγ_vβ_v). Its active parity is |S|. Projection onto the definite-parity active vacuum kills odd |S|. Empty/full S is scalar by total physical parity.

To classify cuts with at most12 edges, let m_a count coordinate-a periodic lines containing both S and its complement. Each contributes at least two cut edges, so Σm_a≤6. No m_a is zero: a nontrivial subset descending to the other two-coordinate torus has at least four boundary edges there; lifting across at least four layers gives at least16 edges.

If some m_a=1, choose b with the larger remaining count; then m_c≤2. Every nonconstant(a,c) slice perpendicular to b contains a mixed a-line, since otherwise c variation repeats across at least four a coordinates, contradicting m_c≤2. Exactly one slice is nonconstant. All constant slices share a value, else every b-line is mixed. The exceptional sites differing from that value number m_b≤4. If no count is1, the only positive triple with sum≤6 is(2,2,2). There are at most two nonconstant perpendicular slices and at most two b-lines carrying deviations, hence at most four exceptional sites again. A three-site set has boundary≥14, and a four-site set has boundary≥16, because the graph is simple and triangle-free. Thus S or its complement has at most two vertices.

The only nonscalar sixth-order spectator supports are therefore bilinears. Adjacent-pair cuts have10 edges; nonadjacent-pair cuts have12 and are also support-allowed. They must not be discarded merely from incidence counting.

Choose a bipartite active Fock representation with black γ real and white γ imaginary. Every real-sign active hopping matrix, real-energy resolvent and canonical projector coefficient is real in this representation, and the simple active vacuum can be chosen real. For a same-sublattice pair, γ_vγ_w is real, so its full coefficient multiplying β_vβ_w is real. But β_vβ_w is anti-Hermitian; Hermiticity requires a purely imaginary coefficient. Distinct spectator bilinears remain linearly independent in the allowed parity space: their distinct products have Clifford grade2 or4, neither0 nor64, so both full and parity-weighted traces vanish. Hence every same-sublattice bilinear coefficient is zero. This concerns the complete canonical coefficient, not individual ordered words.

## Physical magnetic symmetry fixes the remaining matrix

For a graph automorphism f, define κ_e=+1 when f preserves the canonical endpoint order i<j of e, and−1 otherwise. Permute complex matter modes c_i→c_f(i), permute link qubits e→f(e), and conjugate an image link by Z when κ_e=−1. Then X_e→κ_eX_f(e), while Z_e merely permutes. The orientation signs cancel in −iγ_iγ_jX_e. Uniform hopping, D, total parity and all Gauss constraints are preserved. This is a symmetry of the full supplied Hamiltonian.

In the unique minimizing orbit fix ξ and K0. For each generator find vertex signs g_i satisfying K0_(f(i),f(j))=g_i g_j K0_(i,j). After the symmetry, the link representative is κ_eξ_e on the image edge. The gauge return with sign g_i at image vertex f(i) restores ξ because g_i g_jκ_eξ_e=ξ_f(e). Its fixed-representative action is c_i→g_i c_f(i), so active and spectator Majoranas transform by the SAME signed permutation O. The global ambiguity g→−g drops from bilinears.

O preserves K0 and its simple active vacuum. An orthogonal transformation commuting with the full-rank complex structure belongs to its unitary subgroup and has real determinant+1; active and spectator parity are preserved. The full symmetry commutes with H(u), P, its contour projector Π(u), and the positive-overlap polar factors. The canonical effective Hamiltonian inherits it at every order.

Write its sixth bilinear as Σ_(i<j)b_ij iβ_iβ_j with real antisymmetric b. Covariance gives b_(f(i),f(j))=g_i g_j b_ij, including the sign from re-sorting an image pair. An inconsistent signed orbit forces that orbit to zero. The live exact finite certificate constructs three unit translations, three coordinate reflections and two adjacent-axis swaps, solves their signs, checks every64×64 matrix entry, and exhausts all1024 opposite-sublattice pairs. Its four orbits have sizes192,384,256,192. Only the nearest-neighbor orbit192 is free; the two distance3 orbits and distance5 orbit are forced to zero. Thus the invariant antisymmetric space has dimension1. K0 itself is nonzero in that space, so b=−(c/2)K0 from its(0,16) entry. This finite certificate is not extrapolated to other extents or anisotropic coefficients.

## Canonical sixth coefficient and all bridge supports

Subtract E0 and the scalar first-order part of D. With A=PΠP and C=P(H−E0)ΠP, the positive-overlap canonical matrix is A^(−1/2) C A^(−1/2). All coefficients through order5 are scalar. Its sixth nonscalar coefficient therefore comes from C6; A6 cannot contribute through C0=0. In the contour expansion, every term split by an intermediate P is a product of returning subwords of order≤5, hence scalar or zero by the same support/parity rule, including higher resolvent powers. Only the complete irreducible chain contributes to a sixth bilinear:

P V R V R V R V R V R V P,  R=Q(E0−H0)^(−1)Q.

For the adjacent cut δ{0,16}, ten boundary edges occur oddly among twelve occurrences. Either a boundary edge occurs three times, or one other edge occurs twice. The triple-boundary case leaves two odd disconnected incidence stars and cannot be paired into six incident pairs. A repeated nonboundary edge must connect those stars. There are exactly six possibilities on L4: the internal edge, four opposite square edges, and the opposite straight-winding edge. Internal support has15×15=225 unordered pair sets; each external support has3×3=9. Every set has720 orders, totaling194400. All six supports are included.

No proper nonempty prefix of these monomials has zero toggle or an even nontrivial returning cut. A singleton return is possible, but its gauge-transformed active vacuum has opposite initial parity. The unreduced-link word stays in its initial active parity, so its denominator remains invertible there, with gap√24 for that singleton case. Ordinary inverses in that parity block are legitimate for these monomials, not a universal replacement of the reduced resolvent.

## Exact finite active reduction and rational residual certificate

Let J=K0/√24. For the union S of the relevant edge endpoints, W=span{e_v,J e_v:v∈S} is J-invariant. Every changed hopping matrix preserves W and equals K0 on W-perpendicular. The exact common dimension is20. The complement vacuum is unchanged. With ten active complex modes, the reduced starting energy is−5√24; omitting this offset would give wrong denominators. The fixed active-parity block has dimension512.

Use rational orthogonal black columns r_i with squared norms d_i>0, normalized B_i=r_i/√d_i and C_i=−K0r_i/(2√6√d_i). For occupation bits b, S_b=∏d_i^(b_i/2) and metric W_b=S_b². Diagonal similarity removes the frame radicals: S^(−1)H_F S=√6 J_F, with rational J_F, and WJ_F=J_FᵀW. The denominator is √6 S A_F S^(−1), A_F=J_F+10I. Explicitly q_ij=−r_iᵀK_FK0r_j/12, (J_F)_bb=Σ_i(q_ii/d_i)(b_i−1/2). For a=b XOR2^i XOR2^j with i<j, (J_F)_ab=[sgn(b;i,j)/2][q_ji(1−2b_i)−q_ij(1−2b_j)]d_i^(b_i−1)d_j^(b_j−1), where sgn=(−1)^(popcount(b below i)+popcount(b below j)). The quotient S_b/S_a cancels the two square-root norms, proving rationality. The live helper reconstructs this formula from exact canonical K and rational frame data; the packet preserves its complete original derivation.

At inverse level k define rational coordinates z_k=(√6)^k S^(−1)x_k. The exact recurrence is A_s z_s=−(1/2)Σ_predecessors z_prev. Dynamic-programming keys retain ten boundary usage bits and bridge multiplicity0,1,2; they do not collapse to flux masks alone. There are2292 proper inverse states across the six bridges. The final target is an unsolved half-sum of fifth-level vectors.

Saved binary64 vectors merely choose arbitrary dyadic candidate z-hats. No assumption about their forward error, frame rounding or BLAS residual is needed for the independent certificate. The helper forms exact sparse rational residuals, using common integer denominators, and exact squared norms in W. If the incoming certified error is e_in, residual norm upper bound r, positive physical denominator lower bound δ, and rational u6>√6, then

e_s≤(u6/δ)(e_in+r).

For p/q≥0, the norm square root is bounded outward by n/10^50 with n²q≥p10^100, using integer square roots. All error propagation and final endpoint sums are rational.

The physical gap δ is independently bounded from the FULL32-mode Gram matrix. At t=1 write K_F=2[[0,B],[-Bᵀ,0]], so its active ground energy is−Tr√(BBᵀ), including the unchanged vacuum complement. For rational c0=5/2, two Newton square-root majorants give

Tr√A≤(TrA+32c0²)/(4c0)+c0[32−c0²Tr(A+c0²I)^(−1)].

Exact LDL with positive pivots computes the inverse trace; a rational lower bound ℓ<√6 gives δ≥32ℓ−that upper bound. A nonpositive bound falls back prospectively to the proved1/432 full gap; singleton cuts use2ℓ from their parity gap. No floating eigenvalue is used. The closing row L=−i√6 S^(−1)γ_0γ_16 S is rational and has exact weighted dual norm squared6. Its coefficient is (e0ᵀL z_target)/216; its error is at most u6 e_target/216. The six factors1/2, five negative resolvents, closure orientation and factor216 are retained.

The original solver used an independently reviewed numerical enclosure, but the theorem's nonzero certificate comes from the exact rational replay of all six candidate artifacts. The original replay completed in49.61s and enclosed c in the stated exact decimal interval. The portable runner repeats the arithmetic from the frozen candidates, checks the full prefix/word coverage, and separately executes the magnetic orbit certificate. A result containing zero would be inconclusive, never an exact cancellation.

## Physical parity and the full finite gap

For64 complex matter modes, P_total=∏_i(−iγ_iβ_i)=P_γP_β: moving β factors to the right gives(−1)^(64·63/2)=+1 and the relevant powers of−i are1. Use the SAME orthogonal frame on both Majorana sets; their determinant factors cancel. If the active vacuum chirality is s, the spectator quadratic−cK0 has vacuum chirality s for either sign of nonzero c, because sign reversal fills all32 modes and preserves parity. Thus its unconstrained vacuum obeys physical P_total=+1. Only even spectator excitation counts are allowed, giving the levels and gap above.

Subtract the scalar Taylor polynomial through degree6 from the canonical matrix and divide by u^6. It extends analytically to Q+O(u) at0. Q has a simple ground and positive gap2c√24; eigenvalue norm continuity preserves that simple bottom for sufficiently small nonzero u. Other unperturbed clusters remain separated by a positive constant. This establishes full finite-H ground uniqueness and gap2c√24 u^6+O(|u|^7). It supplies no explicit radius, thermodynamic gap or excited-multiplet protection at finite u.

## Evidence and scope

The [packet](../.claude/science/physics-loops/native-weak-electric-spectator-gap-20260908/HANDOFF.md) preserves original proofs, exact fixtures, failed synthetic controls, numerical candidate generation, independent rational replay, signed-orbit reviews and parity review. Source hashes and the runnable input closure distinguish live checks from archived development counts. Floating displays are not substituted for rational interval endpoints.

All Hamiltonian choices remain supplied. The result concerns the specified finite uniformL4 endpoint at t=1. It establishes neither an emergent electromagnetic phase nor a theory of everything, and does not remove the Hamiltonian-selection premise. Larger-torus flux isolation and the nonzero-penalty bulk phase remain open.
