---
claim_id: native_zero_penalty_l6_flux_isolation_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied uniform full-native 6^3 zero-electric-penalty model: unique minimizing Z2 flux orbit, proved by strict reflection equality, boundary CAR rigidity and exact canonical Schmidt-rank certificate. Existential positive wrong-orbit separation only; no numerical gap, general-volume or nonzero-penalty phase."
upstream_dependencies:
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
runner: scripts/native_zero_penalty_l6_flux_isolation_2026_09_08.py
---

# Strict flux isolation on the supplied finite L6 model

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

For the supplied uniform full-native Hamiltonian at zero electric penalty on the 6×6×6 torus, the canonical π-plaquette, positive-native-winding flux orbit is the unique minimizing Z2 orbit. The proof strengthens the imported minimality theorem by an equality argument and an exact finite Schmidt-rank certificate. Finiteness gives a positive wrong-orbit energy separation, but this note does not calculate a lower bound for it.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied uniform finite full-native Hamiltonian and exact auxiliary dictionary; imported reflection minimality."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Supplied premises and precise conclusion

Use the [optimal-flux and exact-dispersion theorem](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md), [full fixed-flux endpoint dictionary](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md), and [Gauss/CAR carrier dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md). The auxiliary full-Fock complex hopping ground energy equals twice the native fixed-flux energy. Uniform nonzero hopping is essential. Set |t|=1 for the certificate; other magnitudes scale all energies by |t|. The canonical real skew matrix K uses lexicographic coordinates and K_ij=−2ξ_ij at ordered endpoints i<j.

The imported canonical spectrum of −K² on L6 is {12,24,36,48}, with multiplicities64,96,48,8. Thus the auxiliary one-particle matrix iK has no zero modes and its full-Fock ground is a unique negative-mode Slater state. The native minimum energy is −72−40√3−48√6. Its fixed canonical orbit retains the spectator ground multiplicity2^107. Unique flux orbit does not mean unique native many-body ground at zero penalty.

The new conclusion is that no other Z2 gauge orbit has this minimum energy. Because the finite graph has finitely many Z2 orbits, their minimum energy excess Δ_flux is strictly positive. It is not assigned a numerical value. The active excitation gap in the canonical orbit is √12 |t| by the endpoint dictionary, so the full ground family is isolated by a positive gap, at least min(Δ_flux,√12 |t|). No nonzero-electric-penalty ground selection is proved here.

## Equality with a faithful reflected child

The reflection representation uses H=A⊗I+I⊗B−Σ_μ C_μ⊗C_μ. The half Hamiltonians A,B are Hermitian. Each C_μ is real, and annihilation/creation channels occur in transpose pairs with positive boundary weights. These conditions make H Hermitian. Identify the two half CAR spaces by reflection, and vectorize a normalized ground vector as a matrix X=UΣV†. Its norm is the Hilbert–Schmidt norm. Put Y=UΣU† and Z=VΣV†.

Define the reflected children H_L=H(A,bar A) and H_R=H(bar B,B), with the same channels. Direct cyclic trace gives

⟨X,H X⟩−[⟨Y,H_L Y⟩+⟨Z,H_R Z⟩]/2
= (1/2) Σ_μ ||Σ^(1/2)(U†C_μU−V†C_μV)Σ^(1/2)||_HS².

Indeed the A/B contributions cancel. With A_μ=U†C_μU and B_μ=V†C_μV, the original cross term is Re Tr(ΣA_μΣB_μ†), whereas the two reflected terms are the weighted squared norms. Completing the square proves the identity; no occupation-basis positivity assumption is involved.

Suppose a parent and its two children all attain the common global minimum E*. If one child has a unique ground with full Schmidt rank across that cut, the corresponding variational matrix Y or Z must be that ground up to phase. Hence Σ is invertible. Every square then vanishes, and R=UV† commutes with all boundary channels, including each boundary annihilator and creator separately.

For a faithful right child, the original eigenmatrix equation is AX+XB^T−Σ C_μXC_μ^T=E*X. Write X=RZ, multiply by R†, and subtract the right-child equation. Since R commutes with every C_μ, this gives (R†AR−bar B)Z=0. Invertibility of Z yields R†AR=bar B. The faithful-left case is symmetric. Thus the parent is equivalent to the child by a half-system unitary fixing every boundary CAR generator.

## Boundary rigidity on the three-layer half

Each coordinate half of L6 has three layers. Its two outer layers are the reflection boundary, and each boundary site has exactly one neighbor in the middle layer. Write the two half hopping Hamiltonians A and C=bar B in the same CAR basis. They have the same graph and equal nonzero edge magnitudes. The unitary R fixes every boundary c_x and obeys R†AR=C.

For boundary sites x,z, the CAR anticommutator {c_z†,[A,c_x]} extracts the negative hopping matrix entry. Applying R to this identity proves equality of boundary-to-boundary hopping entries of A and C. The remaining part of [A,c_x] contains just one interior term a_xy c_y. Conjugation therefore gives R†c_yR=(c_xy/a_xy)c_y for the unique inward neighbor y, with a phase of modulus one. The opposite boundary imposes the same phase on that middle site. Every annihilator is consequently mapped to itself times a site phase, with phase one on the boundary. Irreducibility of finite CAR makes R equal to the corresponding gauge implementer up to a scalar. Since boundary phases are one, cross-plane bonds remain unchanged. The full parent and child are gauge equivalent.

The half-CAR tensor convention, right particle-hole transformation and cross-bond gauge used in reflection positivity preserve Schmidt rank. The left half-CAR convention differs by a half-local occupation phase; the right parity string is the tensor factorization convention. The remaining transformations are local unitaries on one half. Undoing them preserves the stated gauge equivalence. This explicit argument is for the three-layer half; no unproved controllability claim for arbitrary graphs is used.

## Exact faithfulness of the canonical auxiliary ground

The negative-mode correlation projector is P_-=(I−iK(−K²)^(-1/2))/2. For the bipartition into equal coordinate halves, let C_L be its left restriction. The projector identity implies C_L(1−C_L)=P_LR P_RL. Thus invertibility of the108×108 cross block P_LR forces every eigenvalue of C_L into(0,1). Diagonalizing C_L gives independent entangled fermionic mode pairs; each has two strictly positive Schmidt weights. Their tensor product has full many-body Schmidt rank. This concerns the auxiliary unique Slater ground, not the spectator-degenerate native ground.

Let A=−K². The established four-point spectrum licenses polynomial interpolation of A^(-1/2) by degree3 with values1/(2√3),1/(2√6),1/6,1/(4√3) at12,24,36,48. Its coefficients lie in Q(√2,√3). Reduce the localized coefficient ring modulo97 through √2→14 and √3→10. Both square relations hold, and every interpolation and inverse-root denominator is nonzero. The live finite certificate constructs the actual216-site integer K, evaluates this polynomial modulo97 and computes

det[(K A^(-1/2))_LR] = 88 mod97.

Therefore the exact algebraic determinant is nonzero. An algebraically zero element would reduce to zero under this well-defined ring map. Multiplication by −i/2 does not change rank, so P_LR is invertible. A modular spectrum check is not a substitute for the imported characteristic-zero spectrum. The candidate and independent implementations used different integer matrix constructions and elimination routines, with the same determinant. The portable primary binds its exact inputs and reports live controls separately from archived development evidence.

The canonical flux is invariant up to site gauge under translations and coordinate permutations. These symmetries take the tested cut x_0<3 to every coordinate half cut used below and preserve Schmidt rank. Gauge-equivalent canonical children are faithful across all those cuts as well.

## Backward propagation from the canonical configuration

The imported reflection theorem and its transformations are from [Macris and Nachtergaele, Section2](https://arxiv.org/html/cond-mat/9604043). They supply minimality and a finite canonical-circuit iteration, and explicitly do not establish uniqueness. The strict equality and faithfulness steps above are additional.

Start at any minimizing Z2 assignment. It is also a minimizer in the auxiliary phase problem, since the canonical phase assignment is available in Z2 and attains the global phase minimum. For any noncanonical circuit in the generating circuit set, choose an admissible coordinate reflection. Both children remain minimizing: their mean energy cannot exceed the parent's global minimum and neither can lie below it.

Let N count canonical basic circuits, and let m be the number of previously noncanonical circuits crossing that reflection. Both children canonicalize every crossing circuit; the left and right internal counts are copied in opposite directions. Their total count is2N+2m, with m≥1. At least one minimizing child therefore has count strictly greater than N. Repeat; the finite circuit set forces termination at an assignment canonical on a generating set, hence in the canonical gauge orbit.

At the last step, the chosen child is canonical, unique as an auxiliary ground, and faithful across that cut. Equality and boundary rigidity imply its parent is gauge equivalent to it. Apply the same reasoning backward: every chosen child is now gauge canonical and hence faithful across the preceding cut. The original minimizer is canonical up to gauge. This proves uniqueness of the minimizing orbit without enumerating exponentially many flux assignments.

## Scope and evidence

The [science packet](../.claude/science/physics-loops/native-zero-penalty-l6-flux-isolation-20260908/HANDOFF.md) preserves the initial unsuccessful strictness route, exact modular certificate, equality fixture, independent review and root review. No numerical ground-state integration or unlisted search was used to select the conclusion.

The result is conditional support for the supplied finite uniform Hamiltonian. It gives no quantitative Δ_flux, arbitrary-even-volume theorem, nonzero-penalty neighborhood, thermodynamic gap or emergent gauge phase. The Hamiltonian-selection premise remains open. A future general-size proof must establish its own boundary rigidity and faithful-child conditions.
