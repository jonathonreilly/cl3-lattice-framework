---
claim_id: gauge_wilson_static_source_geodesic_perturbation_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/gauge_wilson_static_source_geodesic_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
claim_scope: "Supplied finite static fundamental source sector: complete free geodesic eigenspace and exact first-order plaquette-flip operator, with finite-volume perturbative remainder."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The [compact Hamiltonian parent](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the lattice action. Static external color representations and their zero rest/kinetic energy are additional declared probes. The [primary exact planar runner](../scripts/gauge_wilson_static_source_geodesic_2026_09_07.py) has34 named checks and the [independent cube/source helper](../scripts/gauge_wilson_static_source_geodesic_cube_check_2026_09_07.py) has37; each includes one resource control. The source's all-representation classification and perturbation argument remain analytical. Neither runner computes a full interacting charged spectrum or a uniform remainder. Both independently frozen derivations, candidate timing and prior-art review remain in the evidence packet.

# Root finite-volume static-source geodesic perturbation

Prospectively derived after20:39UTC contract and before primary's independent result. Prior-art search immediately found Kogut, Sinclair, Pearson, Richardson and Shigemitsu, Phys.Rev.D23,2945(1981), https://journals.aps.org/prd/abstract/10.1103/PhysRevD.23.2945 . Its abstract establishes prior Hamiltonian fluctuating-string/fermion work; this note does not claim that general construction is new or import quantitative formulas from its inaccessible full text. The purpose here is to fix the actual model normalization, all-representation minimal sector and finite-volume scope. Static source representation spaces are additional supplied probes, not derived dynamical matter.

## Covariant carrier and free minimum

Use a finite open cubic box containing x and y and every Manhattan geodesic between them, with all elementary faces. Let x!=y and L=|y-x|_1. Define the charged carrier as matrix-valued functions Psi(U) satisfying Psi(U^g)=g_x Psi(U)g_y^dagger, with inner product integral Tr(Psi^dagger Psi)/3. This explicitly fixes the endpoint representation convention. It is equivalent to the invariant part of the full link tensor space with conjugate endpoint source representations. K and multiplication by each J_f=ReTr(U_f)/3 preserve this carrier. No source kinetic or rest-energy term is included. The source-free comparison carrier is the ordinary Gauss-invariant sector on exactly the same graph.

On one nontrivial Peter–Weyl link the electric energy is [p²+pq+q²+3p+3q]/a>=4/a, with equality exactly the fundamental and antifundamental representations. Decompose the charged carrier into spin-network representation assignments and vertex invariant tensors. Mark occupied links carrying nontrivial irreducible representations. In any connected occupied component, simultaneous center gauge transformations at all of its vertices cancel every internal link center phase. Gauss covariance therefore requires total endpoint triality in that component to vanish. A component containing just x or just y has triality+1 or-1 and is impossible. The two sources must belong to the same occupied component, which consequently contains an x-y path of at least L edges. Thus K>=4L/a on the entire charged carrier, including all higher representations and baryonic vertices.

Equality requires exactly L occupied links in total, all with energy4/a. The component containing x,y must then itself be a shortest simple path, with no branches, cycles or additional occupied components. Degree-two invariant tensors force a consistent fundamental line along that path; the endpoint covariance fixes its orientation, and Schur's lemma gives one tensor contraction per path. Therefore the entire free ground eigenspace is spanned by Psi_P(U)=U_P, one for each oriented shortest path P from x to y. Every path state has norm1 since U_P is unitary. Distinct paths are orthogonal: some link is present in only one path, and its nontrivial fundamental matrix integrates to zero. This also proves completeness of the geodesic basis, not just existence of low-energy trial strings. Baryonic branching is allowed in the full space but cannot occur at equality.

For displacement (n1,n2,n3) after reflections, all ni>=0, the number of basis paths is L!/(n1!n2!n3!). They are words in three directions with the fixed letter counts. All-label energies are integers/a, so this finite-rank ground level is isolated by at least1/a, even without determining the next exact level. Compact resolvent follows from the finite product of compact-group Laplacians with finite source multiplicity.

## Exact first-order plaquette matrix

Write h(u)=aH=h0+u(F-S), u=av, S=sum_f J_f and F the face count. Let P_geo be the whole free charged ground projection. For any geodesic P, the pointwise color-summed squared norm is1, so <P|J_f|P>=integral J_f=0.

For two distinct geodesics P,Q, independent link-center phases require the signed current difference P-Q to be canceled by one oriented face boundary for a matrix element of J_f to survive. Both geodesics are monotone in the same directions, hence each difference coefficient is in{-1,0,1}. Adding one signed face coefficient has magnitude at most2, so zero modulo3 forces equality over the integers. Thus P-Q is exactly plus or minus boundary f. Equal lengths then force an exchange of the two consecutive steps around one elementary square; a one-edge/three-edge replacement changes length and is excluded. Conversely every adjacent swap of unequal direction letters gives exactly one such face flip.

For a flip the common prefix and suffix cancel inside the trace, leaving

 <Q|J_f|P>= integral [Tr(U_Q^dagger U_P)/3] [chi_f+bar chi_f]/6 =1/18.

The last equality uses that the four-link plaquette product is Haar, integral|chi_f|²=1 and integral chi_f²=0. The orientation chooses which of the two conjugate terms survives; there is no extra factor2. The normalized source trace1/3 is load bearing. This calculation is on the actual source-index Hilbert space and actual plaquette multiplication, not a fitted path model.

Let A_geo be the simple graph adjacency on geodesic words, joining adjacent swaps of unequal letters. Then exactly

 P_geo (F-S) P_geo = F I - A_geo/18.

This graph is connected by sorting adjacent swaps. Hence its nonnegative adjacency has a simple largest eigenvalue rho, with a strictly positive eigenvector. Degenerate analytic perturbation theory implies that for each fixed finite box and u down to0, the lowest charged eigenvalue is

 a E_xy(u)=4L+u(F-rho/18)+O_(box,x,y)(u²).

The source-free vacuum has a E_vac(u)=uF+O_box(u²). Therefore the finite-volume static energy difference obeys

 E_xy(v)-E_vac(v)=4L/a - v rho(A_geo)/18 + O_(box,x,y)(a v²).

The right-hand derivative at0 is exact. For more than one geodesic the degeneracy is lifted at first order and the selected lowest branch is simple for sufficiently small positive v. A unique geodesic has rho0, so its first derivative vanishes. None of these finite-volume Taylor remainders is asserted uniform in box size or source separation.

## Planar displacement: exact flip spectrum

Take n3=0, n1=r, n2=s, L=r+s, with r,s>=0 and L>=1. Encode each direction-2 step as a particle on its position in the length-L word. The flip adjacency moves one particle to a neighboring empty position with amplitude1. Ordered positions 1<=j1<...<js<=L identify the carrier with the s-fold antisymmetric exterior power of C^L. The second-quantized open-chain hopping T, T_(j,j+1)=T_(j+1,j)=1, has exactly the same matrix: a permitted nearest-neighbor hop cannot cross another occupied site, so its fermionic reordering sign is positive. This is an adjacency operator, not the degree-minus-adjacency Markov generator.

One-particle normalized sine modes sqrt(2/(L+1)) sin(pi k j/(L+1)) have eigenvalues lambda_k=2cos(pi k/(L+1)), k=1,...,L. The whole s-particle adjacency spectrum is all sums of s distinct lambda_k. The maximum is

 rho_(r,s)=2 sum_(k=1)^s cos(pi k/(L+1)).

It is symmetric under r<->s by particle-hole symmetry and vanishes if r=0 or s=0. Examples: rho_(1,1)=1, rho_(2,1)=sqrt2, rho_(2,2)=sqrt5. Hence the corresponding derivatives of the static energy are -1/18, -sqrt2/18 and -sqrt5/18, respectively, in units of v. These identities concern the actual first-order projected charged Hamiltonian, not the exact interacting spectrum at finite v.

If s/L tends to eta in[0,1], the finite-dimensional spectral formula gives rho/L -> (2/pi)sin(pi eta) by a Riemann sum. This is an asymptotic of the derivative coefficient, not permission to interchange the large-distance limit with the interacting Taylor expansion. The naive statement that every shortest path keeps energy4L/a to first order is false whenever r,s>0; the actual ground chooses a superposition of paths.

## Scope and unresolved extension

This constructs a static-probe sector and an exact first derivative of its energy cost at finite volume, including the source normalization. It does not derive sources, temporal Wilson-loop insertions, physical matter masses or a universal string tension from the axioms. An interacting confinement claim requires volume- and separation-uniform control of charged versus neutral energies, including cancellation of vacuum energy beyond first order. Neither the global bounded-perturbation norm nor spatial-loop suppression alone supplies that result. The known general strong-electric string mechanism is prior art; this is a conditional, auditable bridge within the campaign's supplied compact Hamiltonian.
