---
claim_id: gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
claim_scope: "Exact low physical electric spectrum, two-dimensional Ritz interacting gap certificate and local small-coupling slopes on the fixed full compact SU3 cube."
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

The [full compact Hamiltonian parent](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the actual physical Gauss Hilbert space, K+V operator and supplied a,v conventions. The [exact scalar/graph runner](../scripts/gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_2026_09_07.py) performs 18 actual named checks including its resource guard. The analytical all-label, Haar and operator-domain proofs below are not replaced by a finite numerical truncation.

# Exact low electric spectrum and a finite interacting-cube gap bound

This proof follows PREREGISTRATION.md. Root supplied the candidate levels, Ritz matrix and threshold before computation; candidate exposure is explicit. The exact graph and character checks were then independently reconstructed, without a spectral fit. The result is conditional on the full compact physical-Gauss Hamiltonian of block29, not a bare-source compression or a boundary Gaussian model.

## 1. Operator and Gauss domain

On normalized product Haar L2(SU3^12), impose gauge invariance at all eight vertices of the open cube, with no external charges. Let the physical subspace be Hphys. With Hermitian generators normalized by Tr(TaTb)=delta_ab, put

    K=-(3/(2a)) sum_(12 edges) Delta_e,
    V=v W,  W=sum_(6 faces)(1-ReTr U_f/3),
    H=K+V,  a>0, v>=0.

The full compact-Hamiltonian parent supplies this operator and its domain. Directly, K is a nonnegative elliptic Laplacian on a compact connected product group and has compact resolvent. The gauge projector commutes with it; the physical restriction has discrete finite-multiplicity spectrum and compact resolvent. W is smooth, gauge invariant, bounded and nonnegative (0<=W<=12 suffices). Bounded perturbation preserves selfadjointness and compact resolvent on the physical subspace. Write E0<=E1<=... with multiplicities. The constant function1 has norm one.

## 2. All-representation electric lower bound

The Peter-Weyl decomposition on each edge labels matrix coefficients by SU3 irreducibles (p,q), p,q nonnegative integers. In the trace-one generator convention the weight Gram matrix is [[2/3,1/3],[1/3,2/3]]. Applying the quadratic Casimir to highest weight p omega1+q omega2 gives

    C(p,q)=<lambda,lambda+2rho>
          =(2/3)(p²+q²+pq+3p+3q).

Thus the edge kinetic energy is [p²+q²+pq+3p+3q]/a. This is at least4/a for every nontrivial representation, with equality precisely (1,0) or(0,1). The polynomial is strictly increasing under either coordinate increment. Every other nontrivial label is above one of (1,1),(2,0),(0,2), whose dimensionless energies are9,10,10. This is an all-label inequality, not a finite representation truncation.

Gauge averaging acts at a vertex on the tensor product of incident representation factors, dualized according to edge orientation. An occupied degree-one vertex has a single nontrivial irreducible factor and hence no invariant vector. Therefore every nonzero physical spin-network component has support with no degree-one vertex. At a degree-two vertex, Schur's lemma requires matching representations along the path, with a one-dimensional intertwiner. These statements follow directly by decomposing the finite tensor product and projecting onto its invariant subspace; no independent degrees of freedom are assigned to a nonexistent vertex invariant.

The cube has girth four. Every finite nonempty graph with no degree-one vertex in its nonisolated part contains a cycle, so support has at least four edges. Its four-edge cycles are exactly the six faces. Consequently every nonconstant physical electric state has energy at least16/a. Equality forces a face cycle with four fundamental or antifundamental labels. Degree-two invariants close to the trace character, giving exactly two states per face, chi_f=Tr U_f and its conjugate. These twelve states are orthonormal as shown below. Thus

    spec_low(K): 0 (multiplicity1), 16/a (multiplicity12), 24/a next.

There is no five-edge admissible support: an odd five-cycle is impossible on the bipartite cube; a four-cycle plus one extra distinct edge has a leaf. A four-cycle with a nonfundamental representation costs at least36/a, since degree-two matching forces the same irreducible all around it. Hence no energy lies strictly between16/a and24/a. A six-cycle in the cube with fundamental flow attains24/a. The complete4096-support census additionally finds sixteen six-edge admissible supports, all cycles, so the level24/a has multiplicity32. This last multiplicity also uses the same degree-two invariant argument; it is not needed for the interacting bound.

The census retains every support mask and all eight degrees. Its nonempty admissible histogram is {4:6,6:16,7:12,8:33,9:52,10:42,11:12,12:1}. It supplements the all-representation proof. Omitting vertex Gauss invariance would invalidate the result: a single-edge matrix coefficient already has energy4/a. No external-charge or partially gauged domain is included.

## 3. Exact character moments, beyond center selection

Let the twelve signed face characters be chi_i, one fundamental and one conjugate per face, and S=sum_i chi_i. Then S is real, and W=6-S/6.

Multiplying any one oriented edge variable by the SU3 center omega I preserves Haar and multiplies chi_i by omega to the signed face-incidence exponent. Thus an integral of a character product vanishes unless all twelve edge exponents sum to0 modulo3. The exact prospective enumeration keeps all144 ordered pairs and1728 ordered triples. Pair survivors are precisely conjugate pairs on the same face. Triple survivors are precisely the twelve same-oriented-face cubes chi_i³. In particular no mixed-face contribution is silently discarded by a fitted approximation.

Center neutrality is only a necessary selection rule. For the surviving integrals, a face holonomy is itself Haar distributed: conditional on its other three edge variables, the remaining edge is Haar and multiplication/inversion preserves Haar. Schur orthogonality gives integral chi_f conjugate(chi_f)=1. Also integral chi_f³=1, because Haar averaging U^tensor3 is the orthogonal projector onto invariant tensors in (C3)^tensor3. This invariant space is one-dimensional, generated by epsilon_abc. Explicitly diagonal torus invariance restricts a rank-three invariant tensor to permutations of three distinct basis indices; the elementary SU2 rotations in each coordinate plane force their coefficients to be alternating, leaving only epsilon. Conversely epsilon is SU3 invariant since detU=1. The conjugate cube has the same integral. Taking the trace of the Haar projector therefore gives1, not3 or6.

It follows that

    integral S=0, integral S²=12, integral S³=12,
    <chi_i,chi_j>=delta_ij,
    K S=(16/a) S.

This provides actual Haar values for every center-allowed term, rather than treating center selection as a proof of a nonzero value.

## 4. Rigorous interacting gap certificate

Since V>=0, min-max on the common form domain gives E1(H)>=E1(K)=16/a. The vacuum Rayleigh quotient gives E0(H)<=6v, hence the simple bound gap(H)>=16/a-6v, positive for av<8/3.

Use instead the orthonormal trial pair {1,S/sqrt12}. Its exact Ritz matrix is

    R=[[6v, -v/sqrt3],[-v/sqrt3,16/a+35v/6]].

The diagonal and off-diagonal entries follow from the three exact moments above: the upper entry is6v; the off-diagonal is -(v/6)sqrt12; the lower potential entry is6v-(v/6)(12/12)=35v/6. No outcome is selected or normalized separately.

Set x=av and define

    mu(x)=[16+71x/6-sqrt((16-x/6)²+4x²/3)]/2,
    G(x)=16-mu(x).

Rayleigh-Ritz gives E0(H)<=mu(x)/a. Together with min-max,

    E1(H)-E0(H) >= G(av)/a.

This is a rigorous finite-cube interacting bound, not merely a perturbative prediction. It is strictly positive for 0<=av<35/13, including gap16/a atv0. To check the endpoint without squaring an inequality ambiguously, the determinant of aR-16I is (8x/3)(13x-35). For 0<x<35/13 it is negative, so its lower eigenvalue is negative. At x=35/13 its other eigenvalue is positive. For larger x its leading diagonal is positive and determinant nonnegative, so this particular lower bound is no longer positive. This is the threshold of the certificate, not a claim that the actual gap closes there. The interval35/13 is slightly larger than8/3.

## 5. Local small-coupling coefficients

These additional statements concern x=av tending to0, not the entire certified interval. Write aH=T+xW with T=aK. Its isolated simple ground at0 and isolated twelve-dimensional level16 are separated from the next free level24. Since W is bounded, the resolvent Neumann expansion on fixed contours yields analytic spectral projections for small |x|; finite-dimensional reduction of the level16 cluster has first matrix PWP and an O(x²) remainder. This justifies ordinary degenerate perturbation without assuming that its first-order multiplicity persists.

The ground expectation is6, and (W-6)1=-S/6 lies wholly in the free level16 with squared norm1/3. Its second coefficient is therefore -(1/3)/16=-1/48:

    E0(H)=6v-a v²/48+O(a² v³).

For the first electric subspace, the exact triple moments give P S P as six independent [[0,1],[1,0]] blocks pairing conjugate face characters. Consequently PWP has eigenvalues35/6 and37/6, each sixfold. For v approaching0 from above, the lowest excited cluster therefore has

    E1(H)=16/a+35v/6+O(a v²),
    gap(H)=16/a-v/6+O(a v²).

The sixfold first-order slope may split at higher orders; no exact interacting multiplicity is asserted. The second-order ground coefficient agrees with the Ritz expansion but is proved by the spectral projection calculation, not inferred from an upper bound alone. No numerical small-coupling onset or global monotonicity follows from these expansions.

## 6. Evidence, provenance and scope

The standalone scratch runner makes eighteen actual checks in about0.25seconds at62.34MiB. It retains all4096 supports,144 pair center patterns,1728 triple patterns, survivors, first-level insertion matrix and symbolic Ritz arithmetic. The SU3 Haar survivor proof and infinite representation support are analytic; the finite certificate does not replace them. No failed scientific control occurred in this run. All supplied candidate exposure is in the preregistration.

Gauge-invariant SU3 vertex/loop Hilbert-space methods are established, not a new general formalism; see Anishetty, Mathur and Raychowdhury, [Prepotential formulation of SU(3) lattice gauge theory](https://arxiv.org/abs/0909.2394), which constructs invariant vertex spaces and loop states. This reference is provenance only. The particular all-support census, normalization, Haar moments and variational bound are derived above within the stated supplied cube model.

This is a positive finite-volume gap certificate for the full physical Gauss space of the fixed interacting compact model. It does not prove a spatial continuum or thermodynamic gap, QCD/Yang-Mills mass gap, physical units/coupling choice, or a gap derived from minimal Record axioms. It also does not identify a source-compressed operator with this full Hamiltonian. These different domains remain explicit.
