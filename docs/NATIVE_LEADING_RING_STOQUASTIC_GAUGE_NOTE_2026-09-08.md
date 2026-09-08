---
claim_id: native_leading_ring_stoquastic_gauge_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Explicit diagonal gauge of the supplied native H4 ice operator to negative cycle adjacency; plaquette-only V0 at even extents at least six, winding extras at extent four, with coherent state/readout mapping. Not the full finite-coupling Hamiltonian."
upstream_dependencies:
  - native_virtual_pair_ring_mechanism_note_2026-09-08
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/native_leading_ring_stoquastic_gauge_2026_09_08.py
---

# Explicit diagonal gauge of the leading native ring operator

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

The supplied fourth-order ice operator has an explicit diagonal phase transformation to negative cycle adjacency. On even tori with every extent at least six, its nonconstant part is the ordinary pure-kinetic plaquette operator at the supplied scale. Extent-four winding terms remain additional, and coherent initial states must transform with the operator.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Finite supplied leading-coefficient operator identity."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Premises and exact map

Use the [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), its [native instrument algebra](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md), and the [supplied fourth-order mechanism](NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md). The degree-three domain and numerical plaquette definition are those of the [ice parent](SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md); its numerical phase estimates are not premises. No new Hamiltonian or state preparation is selected here.

For lexicographic vertices, the parent's quadratic bit phase and a specified linear bit phase give

\[
\mathcal U|x\rangle=(-1)^{q(x)+\sum_{r,a}(\sum_{b<a}r_b)x_{r,a}}|x\rangle,
\qquad q(x)=\sum_{e<f}M_{ef}x_ex_f.
\]

On ice the omitted factor $(-i)^{|x|}$ is common to every state. With $B_C$ the sequential canonical native product restricted to alternating support,

\[
\mathcal U B_C\mathcal U^\dagger=-F_C X_C,\qquad
\mathcal U H^{(4)}_{\rm nonconstant}\mathcal U^\dagger
=-\frac{g^4\lambda^4}{2U^3}\sum_{C\in\mathcal C_4}F_C X_C.
\]

Here $U>0$ in the denominator is the supplied charge penalty, whereas $\mathcal U$ is the phase transformation. Every simple four-cycle is counted once. The following proof retains the canonical orientation and all finite winding terms.

## Complete proof

Consider the supplied full native H4 on finite periodic cubic geometry with even extents at least4. The native A operators use the parent's canonical endpoint orientation and any fixed neighbor orders. The full W dictionary supplies d(x)=(-i)^|x|(-1)^q(x), q(x)=sum_(e<f)Mef x_e x_f, M_e=w_e XOR ell_e, where ell_e sums incidence rows of vertices from the lower endpoint up to but excluding the higher. M is symmetric off diagonal and has diagonal1. This dictionary is a phase-decorated basis bijection, not an arbitrary basis change.

Every ice string has exactly3N/2 occupied edges and n_v(x)=1 at every vertex. Thus W restricted to ice identifies it with the same electric bitstring and a fixed full matter occupation; its d phase is a constant times(-1)^q(x). Since W S_C W†=X_C, the ordinary electric-basis map U_d|x>=d(x)|x> sends S_C to the unsigned cycle flip. Equivalently d(y)/d(x) times the native S matrix element equals1 for y=x XOR C. Flippability is diagonal and unchanged.

Let eta_C be the product of the signs comparing the traversal direction of each edge with its lower-to-higher endpoint orientation. At length4, i^4=1 and reversal of the sequential native product crosses four anticommuting adjacent pairs, giving+1. Hence S_C=eta_C B_C, or U_d B_C U_d†=eta_C X_C. This step retains rather than discards the native oriented-cycle convention.

Choose coordinate axes0,1,2 and the static sign background

 xi_(r,a)=(-1)^(sum_(b<a) r_b).

It is periodic for every even extent. A plaquette in plane a<b has holonomy-1: changing r_a flips exactly the b-edge sign, while the other changes cancel. At a periodic seam the change1-L_a is odd and gives the same result. A straight winding cycle of length4 has holonomy+1 because the transverse exponent is repeated four times. For lexicographic vertex labels, every elementary plaquette has eta_C=+1, including seam plaquettes: each axis contributes one forward and one backward canonical sign, with paired wrapping signs. A straight extent-four cycle has three increasing edges and one decreasing wrap, hence eta_C=-1.

Define f(x)=product_e xi_e^x_e and U|x>=f(x)d(x)|x>. Then

 U B_C U†=eta_C product_(e in C)xi_e times X_C=-X_C

for every simple four-cycle on this domain. All simple four-cycles are elementary plaquettes or straight windings along extent-four axes. The explicit global bit formula on ice, after dropping the common(-i)^(3N/2), is

 U|x>=(-1)^[sum_(e<f)Mef x_e x_f + sum_(r,a)sum_(b<a)r_b x_(r,a)] |x>.

This single-valued diagonal phase proves consistency around every configuration relation automatically: phase ratios telescope. No assumed configuration connectivity or flux-only identification enters. Any reordering of native stars changes the supplied quadratic phase, not the result. The map preserves each exact support component and every diagonal observable.

With the parent's H4 coefficient +g^4 lambda^4/(2U^3) sum_C B_C (uniform positive native coefficients), the transformed leading nonconstant operator is -J sum_C X_C, J=g^4 lambda^4/(2U^3), plus the unchanged scalar. For arbitrary fixed real coupling signs at uniform magnitude, absorb their edge product into f as an additional linear bit sign. This still maps every leading cycle term to the same negative adjacency. It does not remove H6's closed-loop obstruction; its six-cycle terms transform too and retain that invariant negative product.

If every extent>=6, C4 consists only of elementary plaquettes, so this is exactly the supplied ordinary pure-kinetic plaquette Hamiltonian V0, up to scalar and time/energy scale, on the same ice component. If an extent is4, the full H4 also contains straight winding4 flips. The gauge makes those negative as well, but it does not remove them. Therefore the full L4 H4 is not identical to a numerical target that includes only elementary plaquettes. Removing winding terms would be an additional supplied modification. L2 is outside this simple-graph domain.

This is an exact leading-coefficient operator identity in the canonical convention, not equality of the full finite-coupling Hamiltonian, a selected action, a locality claim for the quadratic diagonal unitary, a ground-state result, or a Coulomb-phase inference. It does identify the precise leading supplied V0 comparison at L6 and larger even extents without pretending H6 remains stoquastic.

## Coherent states and readout

The diagonal gauge U commutes with every diagonal electric/ice observable. A classical mixture of ice basis states is unchanged; a general coherent density matrix must be transformed to U rho U†. Spectra and corresponding ground subspaces are unitarily identified, but initial coherent amplitudes cannot be left unchanged while comparing dynamical expectations. In particular the numerical free-endpoint vector1 corresponds to native U†1, not automatically to a positive uniform native vector. No preparation of that coherent boundary state is supplied by this dictionary. The equality concerns leading H4 with its stated scale/scalar; it neither equates the full finite-coupling models nor removes H6's sign obstruction.


## Evidence and remaining scope

The portable live control retains all 6253 original predicates and full fixture bitstrings, including 132 legal winding transitions. The original three failed L4 fixture selections are preserved. The independent cold proof review supplies 805 additional controls as archived evidence, not as an added live count. The actual trivial-background subprocess mutant must fail a native transition predicate. These finite checks do not replace the general dictionary argument.

The diagonal phase construction is standard basis mathematics. No physical implementation of its generally nonlocal quadratic phase, preparation of its coherent free-endpoint state, full finite-coupling equivalence, phase selection or electromagnetic identification is derived. The [packet](../.claude/science/physics-loops/native-leading-ring-stoquastic-gauge-20260908/HANDOFF.md) preserves source proofs, failures, review, live data and closure receipts. Canonical review remains separate from retained-grade audit.
