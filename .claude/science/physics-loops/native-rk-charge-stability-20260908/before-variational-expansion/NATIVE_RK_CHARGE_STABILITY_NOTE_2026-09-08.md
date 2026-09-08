---
claim_id: native_rk_charge_stability_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Finite even cubic tori with extents at least four, full native edge carrier and supplied low-charge RK Hamiltonian: all-position static signed-pair support, exact static pair energy 2U, operator bound H >= (U-4|t|)D, neutral zero-energy ground states for U>=4|t| and charged-sector gap at least 2(U-4|t|) in the strict region. No physical mass, neutral gap or mobile deconfinement conclusion."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/native_rk_charge_stability_2026_09_08.py
---

# Static signed-pair support and stability under native hopping

**Date:** 2026-09-08
**Type:** bounded_theorem
**Status:** conditional-support

For a supplied finite native Hamiltonian, charges have an energy penalty that remains bounded away from zero when hopping is sufficiently weak. The proof keeps the native operator phases. It supplies a controlled charged-sector regime inside this model, not a physical particle mass or a selected law of nature.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact finite operator bounds under supplied domain, gates and couplings."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Premises and claim boundary

The [native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), its full-carrier theorem and gated-ring/low-charge corollaries, supplies the phase-correct representation and native hopping algebra. That source is a provisional, independently checked dependency on a separate science branch; its inclusion does not grant audit status. This note neither restores the fixed magnetic-cycle state constraint nor supplies a new physical axiom.

Use an even periodic cubic graph with each extent at least four, so physical edges are distinct and the graph is simple. Each edge has a binary occupation n_e=(1-Z_e)/2. Put G_v=sum_{e incident v} n_e-3, epsilon_v=(-1)^(v_1+v_2+v_3), Q_v=epsilon_v G_v, and D=sum_v Q_v^2. Restrict to |G_v|<=1. The fixed-cycle code constraint is relaxed. F_p projects onto alternating bits on geometric plaquette p; S_p is the native Hermitian cycle involution with its prescribed phase. The supplied Hamiltonian is

    H = sum_p J_p F_p(I-S_p) + U D + t T_low,
    T_low = sum_{undirected edge e} P_low T_e P_low,
    J_p >= 0, U > 0, t real.

Uniform J is a special case. No coefficient, domain or gate is inferred from the axioms. All winding sectors are available; no fixed-winding support theorem is asserted.

## Static pair support at every separation

In an ice configuration every vertex has degree three. Orient each electric edge so its arrow i->j has epsilon_i(2n_e-1)=+1. Every vertex has three incoming and three outgoing arrows. A finite connected balanced directed graph is strongly connected: in its acyclic condensation graph a source strongly connected component has no incoming edges; balance forces no outgoing edges either, so connectedness forces a single component.

For any distinct ordered pair u,v there is therefore a directed simple path from u to v. Flip its edge bits. Each traversed edge changes Q by -1 at its tail and +1 at its head. Internal path vertices cancel; the final configuration has Q_u=-1, Q_v=+1 and all other charges zero. Every path prefix stays in the low-charge domain. An explicit ice seed is n_a(r)=r_a mod 2, available on every stated even torus. This proves nonempty support for every ordered signed pair. The construction is a support witness, not a preparation by T: native hopping preserves defect number, and path flips need not preserve native fermion number from the ice sector.

A ring preserves every G_v. In the dictionary representation it is the alternating binary ring flip, with the same F_p. Thus F_p commutes with S_p and F_p(I-S_p) is positive semidefinite. In any fixed-charge ring-connected component, the uniform vector in the dictionary basis is annihilated by every term. Mapping back supplies the required native phases; an unsigned uniform vector in the original basis is not substituted.

Consequently at t=0 the minimum energy in every fixed signed-pair-position sector is exactly 2U, independent of separation. A nonempty ice ring component similarly has zero ring energy and D=0. This finite static statement does not establish a thermodynamic phase or dynamics of mobile charges.

## Hopping conservation and the four-choice bound

On the low-charge domain B_v=(-1)^(3+G_v). Native T_ij=(i/2)A_ij(B_i-B_j) is nonzero only when exactly one endpoint is charged. If its G is s=+1 or -1 and the other endpoint has G=0, toggling the common edge changes both by delta=1-2n_e. The low-charge projection requires delta=-s. The final G pair is (0,-s). Since epsilon changes sign across the edge, the same signed Q moves to the other endpoint. Positive and negative defect counts and D are conserved. Each nonzero amplitude has modulus one and its reverse is the complex conjugate; native phases are retained.

A source with G=+1 has four occupied edges and only those may flip. A source with G=-1 has four vacant edges and only those may flip. Requiring a neutral target can only reduce the number. Thus a configuration with D charges has at most 4D permitted hops. Each undirected edge is counted once at its unique charged endpoint and distinct edges give distinct resulting configurations.

In a fixed-D block the Hermitian hopping matrix has absolute row and column sums at most 4D. The elementary inequality 2|a b|<=|a|^2+|b|^2, applied to every unordered off-diagonal pair, gives

    |<z,T_D z>| <= 4D ||z||^2.

Combining blocks and ring positivity proves the operator inequality

    H >= (U-4|t|)D.

The proof permits nonuniform nonnegative J_p. The literal control below attains the row count 4D, but it does not establish saturation of the spectral norm or optimality of the coupling threshold.

## Ground and charged-sector energies

On ice every B_v=-1, so hopping vanishes. Each phase-correct uniform ice ring-component vector remains an exact zero-energy vector at every t. If U>=4|t| the operator bound is nonnegative, so these are ground states. This does not give uniqueness, and at equality additional charged zero modes are not excluded.

Because the torus is closed and bipartite, sum_v Q_v=0. Since Q_v is 0 or +/-1, D is even, and every charged block has D>=2. For U>4|t| the full charged-sector energy satisfies

    inf spec(H restricted to D>0) - E_0 >= 2(U-4|t|),  E_0=0.

This bounds only the charged sector, not neutral excitations. It does not order the lowest energies of different positive-D sectors.

For a fixed pair-position sector, choose a phase-correct uniform ring-component vector phi. Its ring energy is zero and D=2. Every nonzero hop changes the charge-position vector, so T_low maps its support into orthogonal fixed-position sectors. Hence <phi,T_low phi>=0, and the variational principle yields

    2(U-4|t|) <= inf spec(H restricted to D=2) <= 2U.

At nonzero t, phi is a trial state and generally not an eigenstate. The upper bound is not a fixed-position spectral comparison for mobile dynamics. At t=0 both bounds recover the exact static energy.

## Reproduction and bounded controls

Run `python3 scripts/native_rk_charge_stability_2026_09_08.py` from the repository. The paired runner hashes its note, declared dependency and helpers, then executes explicit predicates that remain active under `python3 -I -OO`.

The static helper constructs two ice configurations on each of 4x4x4, 4x4x6 and 8x8x8. It checks every ordered pair on the first two geometries and one opposite target per source on the last, including direct final-charge recomputation. Its 16-state plaquette matrix obeys R^2=2R, has zero row sums, and gives a negative-energy witness if J is made negative. These are finite controls of the general proof, not a full ice-sector census.

The mobile helper checks all thirty degree-two/degree-four local patterns. On an actual 4x4x4 seed, flipping the directed electric path (0,0,0)->(3,0,0)->(2,0,0) creates a signed pair with eight legal hops. Three bounded depth neighborhoods check native phase conjugation, charge conservation and the row bound. Repeated neighborhoods are disclosed; the reachable set is not the entire charged sector. No spectral diagonalization is performed.

Changing the domain to parallel-edge graphs, permitting larger |G|, removing the low-charge projection, allowing negative J_p, or reinstating fixed-cycle constraints requires a new analysis. Physical Hamiltonian selection, charge preparation, neutral excitation behavior, mobility, deconfinement and continuum interpretation remain open. No observed value, fit or stochastic estimate enters the theorem.
