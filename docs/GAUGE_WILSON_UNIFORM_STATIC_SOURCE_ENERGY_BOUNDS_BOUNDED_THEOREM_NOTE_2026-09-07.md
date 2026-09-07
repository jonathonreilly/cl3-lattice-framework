---
claim_id: gauge_wilson_uniform_static_source_energy_bounds_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_static_source_sector_controls_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
  - gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_bounded_theorem_note_2026-09-07
  - gauge_wilson_static_source_geodesic_perturbation_bounded_theorem_note_2026-09-07
claim_scope: "Explicit sector-restricted dressed-coordinate import gives graph/separation-uniform weak-av linear static-source energy bounds; exact all-coupling open-line upper trial in the supplied compact SU3 model."
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

For supplied fundamental endpoint probes separated by actual graph distance L in a finite compact SU(3) link model, sufficiently small av gives

 (4/a)(1−3cr)L <= E_xy−E_0 <= 4L/a,  r=3av/4,

with c and the allowed r threshold independent of graph volume and source separation. The upper bound and nonnegativity hold at every finite v>=0. The proof uses the actual sector-restricted dressed-coordinate estimate, not an assignment of charge labels to a global spectral inclusion. The endpoint species, a,v, operator and Gauss boundary conditions are supplied; no infinite-volume static-potential limit or physical numerical string tension is inferred.

The [compact Hamiltonian source](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the operator and trace convention. The [all-label electric source](GAUGE_WILSON_COMPACT_CUBE_LOW_ELECTRIC_SPECTRUM_RITZ_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the representation-wide Casimir minimum. The [static-source geodesic source](GAUGE_WILSON_STATIC_SOURCE_GEODESIC_PERTURBATION_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the finite source sector and separately studies its free geodesic eigenspace and finite-volume first-order operator. The uniform bound here does not follow from that finite-volume perturbation radius.

The [sector helper](../scripts/gauge_wilson_static_source_sector_controls_2026_09_07.py) performs32 exact graph, source-norm and explicitly toy resolvent controls. The [Dirichlet helper](../scripts/gauge_wilson_static_source_dirichlet_controls_2026_09_07.py) performs42 exact SU3 and finite creation/projector controls. Neither proves the imported infinite-dimensional coordinate theorem. Their full scientific payloads, original sources, prospective contracts, root syntax-only failure and proof reviews are preserved in the [durable packet](../.claude/science/physics-loops/static-charge-uniform-20260907/PROOF_REVIEW.md).

The complete independent derivation follows. References to not having read the other completed proof concern its original freeze time; both proofs were subsequently cold-reviewed. Root's separately written full proof and all reviews are retained in the packet. The ghost-padding and upper-trial candidates were exposed before the supplements were derived, with that timing explicitly recorded. The normalized tensor-vector convention below, with components Omega U_ab/sqrt3, is equivalent to the matrix carrier with inner product integral Tr(Psi†Psi)/3. Neither source convention introduces a factor3 in the physical energy; the factor3 in the lower-bound estimate comes only from the nine-dimensional Banach-norm amplification.

# Equivariant dressed coordinates and two-sided static-source energy bounds

2026-09-07. Independent derivation after the exposed root candidate, before reading root's completed proof. Original prospective contract and later supplement timing are retained. This is a conditional theorem for the supplied compact SU(3) Hamiltonian and supplied static endpoint representations. It explicitly imports a quantitative dressed-coordinate estimate; the global spectral-circle statement alone would not justify the result.

## 1. Statement and finite model

Let G be a finite oriented cubic-lattice link subgraph. Retain any subset of its actual elementary plaquettes. Gauge transformations act at ALL vertices incident on actual links, including boundary vertices. Let x≠y lie in the same connected component and L=d_G(x,y). On full Haar link space set

 H=K+V, K=(3/(2a))Σ_e(−Δ_e), V=vΣ_f[1−ReTr(U_f)/3], a>0, v≥0, u=av.

The convention Tr(T_A T_B)=δ_AB gives one-link energies [p²+pq+q²+3p+3q]/a. Every nontrivial irrep therefore costs at least4/a. Put E=C³_x⊗conjugate(C³)_y and impose invariance under the link gauge action together with this external representation (or interchange endpoints/conjugate the path; the energy is the same). The charged Hilbert space is the joint fixed space in H_links⊗E. The Hamiltonian on it is the restriction of H⊗I_E. Let E_0 be the ordinary neutral ground energy, and E_xy the bottom of the charged spectrum.

There exist geometry-dependent constants δ>0 and c>0, independent of G, its volume, x,y and L, such that whenever r=3u/4<δ and η=3cr<1,

 (4/a)(1−η)L ≤ E_xy−E_0 ≤ (4/a)L.                 (1)

In particular η≤1/2 yields a lower bound2L/a. The upper bound holds at every finite v≥0. Constants are not evaluated numerically. This does not prove an infinite-volume static-potential limit, a continuum theorem, an axiom-selected coupling/time, or confinement in an unspecified physical model. The full Gauss condition at boundary vertices is essential; allowing boundary charge leakage changes the free threshold.

## 2. Exact free charged threshold

Resolve each actual link into full Peter–Weyl isotypic projections; these commute with Gauss transformations and K. For a fixed label assignment, call a link occupied if its representation is nontrivial. Consider any connected component of the occupied-link graph, including isolated endpoint vertices. Apply the same center element ζI to every vertex of that component and identity elsewhere. Internal link actions cancel, while every link crossing its boundary has the trivial representation. Thus the link state is unchanged. The external tensor acquires a nontrivial center phase if exactly one of x,y belongs to the component. Such a component cannot support an invariant vector. Hence a nonzero charged label block must connect x to y through occupied links and has at least L occupied links. Its free energy is at least4L/a.

A simple shortest path carrying a fundamental parallel transporter, with endpoint tensor indices contracted against the dual external representation and all other links constant, realizes this threshold. Thus the free charged minimum is exactly4L/a. This proof handles branching, triality-zero nontrivial irreps and periodic alternatives: it uses occupied components, not a claim that every occupied edge carries fundamental triality. No fixed-particle-number simplification is used.

## 3. Imported quantitative coordinate estimate and normalization

The explicit mathematical input is Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*, arXiv:math-ph/0411042, Section2, equations(8)–(15): https://arxiv.org/pdf/math-ph/0411042 . Its preliminary stability results are attributed there to earlier work; we import the stated coordinate estimates, not an independent reconstruction of that general theory.

For a finite set of cells Λ, each cell contains three outgoing full SU(3) links. Set h_z=(a/4)Σ_{e tail z}K_e, so h_z has unique constant vacuum Ω_z and gap1. Group centered plaquette terms as φ_z=−(u/4)Σ_{i<j, retained}ReTr(U_(z,ij))/3. Their common support lies in Λ_0+z for Λ_0={0,e_1,e_2,e_3}, and sup||φ_z||≤r=3u/4. The classical part here is ONSITE, matching0411042; do not substitute the different four-cell block normalization used for the spatial-loop theorem0412040.

The imported construction gives the vacuum-overlap-normalized interacting ground Ω~=SΩ_0, with

 S=exp(Σ_{∅≠I⊂Λ} hat v_I),  hat v_I=|v_I><Ω_(I,0)|⊗I_(Λ\I),

where v_I belongs to H'_I=⊗_{z∈I}(H_z⊖Ω_z), lies in Dom H_(I,0), and satisfies the small weighted bound in(8). The creation operators commute and products with overlapping supports vanish. In the bare direct-sum coordinate space, for the renormalized Hamiltonian,

 S^(−1)(H_scaled−E_scaled)S = H_0+F.

Choose the auxiliary decay parameter in(14) once below one. Dropping its weights yields the load-bearing column estimate

 Σ_J ||F_(JI) w_I|| ≤ c r |I| ||w_I||,          (2)

with c independent of volume and I, for sufficiently small r. All subsequent restriction and source-tensor arguments are proved below; they are not consequences of the unlabelled spectral inclusion in Theorem1.

The neutral scaled ground is unique and has nonzero overlap with Ω_0 in this regime. Since the gauge group commutes with the Hamiltonian and fixes Ω_0, overlap normalization forces every gauge transformation to fix Ω~ exactly. No unproved phase choice is needed.

## 4. Dressing equivariance and domains

Although one vertex acts on several links, for each full gauge assignment g the link unitary factors across outgoing cells: U(g)=⊗_z U_z(g). Each U_z(g) fixes Ω_z. Consequently the orthogonal bare excitation projectors Q_I onto H'_I⊗Ω_(Λ\I,0) commute with U(g), as does H_0.

Conjugating S by U(g) replaces v_I by U_I(g)v_I. The resulting creation exponential still maps Ω_0 to Ω~, because both vectors are invariant. Uniqueness of the finite nilpotent creation-log coordinates therefore gives U_I(g)v_I=v_I separately for every I. It follows that every hat v_I, S and S^(−1) commute with all gauge transformations. This is stronger than mere invariance of the resulting ground vector and is the necessary sector-preserving step.

For finite Λ, the sum of bounded creation operators is nilpotent, so S and S^(−1) are finite polynomials and bounded invertible operators. They need not be unitary, and their Hilbert norms need not be uniform in volume. Because v_I∈Dom H_(I,0),

 [H_0,hat v_I]=|H_(I,0)v_I><Ω_(I,0)|⊗I_(Λ\I)

is bounded. Finite products show S and S^(−1) preserve Dom H_0. Thus the displayed similarity is an operator identity on that domain, not only a formal identity on vacuum vectors. Finite-volume equivalence of Hilbert and coefficient-l1 norms suffices for spectral conclusions; no uniform equivalence constant is invoked.

## 5. Extension by the endpoint tensor and the restricted resolvent

Tensor all maps with I_E, where dim E=9. For w_I=Σ_{α=1}^9 w_(Iα)⊗e_α, triangle inequality, (2) and Cauchy–Schwarz give

 Σ_J ||(F_(JI)⊗I_E)w_I||
 ≤ Σ_αΣ_J||F_(JI)w_(Iα)||
 ≤ c r |I|Σ_α||w_(Iα)||
 ≤3cr |I| ||w_I||.                            (3)

This establishes the fixed factor3 without claiming a dimension-free tensor amplification. Use the norm ||w||_1=Σ_I||w_I|| on the finite direct sum. Since H_(I,0)≥|I|, (3) implies

 ||Fw||_1≤η||H_0w||_1, η=3cr.                 (4)

Every Q_I commutes with combined link/source Gauss action, so the charged fixed space decomposes into invariant coefficient blocks. S⊗I_E preserves that fixed space by equivariance. Each nonzero charged block has free threshold L in scaled units by Section2. In particular the I=∅ block is zero for distinct source vertices. H_0 and F preserve the full charged coefficient subspace, even though F can mix I blocks.

For real 0≤z<(1−η)L, the free restricted resolvent obeys

 ||H_0(H_0−z)^(−1)||_1 ≤ sup_{s≥L} s/(s−z)=L/(L−z),

and therefore ||F(H_0−z)^(−1)||_1<1. Its Neumann series gives the restricted resolvent of H_0+F. For z<0 the same norm ratio is at most one, so these points also lie in the resolvent. The free resolvent maps the coefficient space into Dom H_0 with its graph norm; the series therefore defines a genuine inverse on that domain. At each finite volume the coefficient norm is equivalent to Hilbert norm, and S is a bounded domain-preserving similarity. Hence the selfadjoint charged restriction of H_scaled−E_scaled has no spectrum below(1−η)L. Rescaling by4/a proves the lower bound in(1).

This explicitly subtracts the exact neutral ground energy before the estimate. There is no volume-sized comparison of ground energies and no assumption that a nonunitary similarity preserves quadratic forms. The argument proves spectral exclusion, which suffices for the lower energy bound.

## 6. Arbitrary actual finite graph via ghost-vacuum padding

To fit the literal finite whole-range family in the paper, enlarge the finite cell set so that it contains all actual link tails and all Λ_0 translates of retained plaquette anchors. Complete each cell's three outgoing link registers, calling missing actual links ghosts. Set φ_z to contain only the actual retained faces, and zero otherwise. These are allowed inhomogeneous fixed-range terms with the same bound r. The augmented Hamiltonian factorizes as the actual Hamiltonian plus independent ghost electric operators, up to the same centered scalar.

Its ground is Ω_actual⊗Ω_ghost, and its neutral ground energy is the actual one. Every bare Q_I preserves ghost vacuum. The unique creation logarithm therefore has v_I supported on ghost vacuum in every ghost factor inside I. For each such factor, hat v_I=P_ghost hat v_I P_ghost; outside I it acts as identity. Thus S and S^(−1) commute with EVERY ghost-vacuum projector. H_0, F and combined Gauss transformations do too.

Restrict the preceding resolvent argument jointly to the charged fixed space and all ghosts in vacuum. This joint sector is exactly the actual charged model. Its free threshold is the actual graph distance L, because ghost links cannot be occupied and cannot provide shortcuts. No estimate is obtained by allowing flux to escape through auxiliary or unprojected boundary links. This finite padding uses the inhomogeneous finite theorem only; it does not assert a thermodynamic theorem for volume-dependent interactions.

## 7. Exact open-line upper bound

This supplement was exposed by root and then independently checked here; its timing is recorded separately. Let Ω be the normalized neutral ground of the finite actual Hamiltonian. At arbitrary finite v its existence and a positive gauge-invariant choice follow from the compact connected link manifold, elliptic electric operator and real bounded potential (equivalently the positivity-improving heat semigroup). In the small regime the imported unique ground already supplies this. Choose a simple shortest path p and its SU(3) transporter U_p. Regard

 Ψ_ab(U)=Ω(U)(U_p(U))_ab/√3

as a vector in the dual endpoint source tensor, with endpoint orientation chosen to match the fixed sector. The covariance U_p→g_x U_p g_y^† gives the required combined Gauss invariance. Reversing/conjugating the path handles the opposite convention. Pointwise Σ_ab|Ψ_ab|²=|Ω|², so Ψ is normalized and has exactly the same potential expectation as Ω.

For each path link e and Lie generator T_A, the product rule gives a mixed kinetic term proportional to Tr(U_p^†D_e^A U_p), which is zero because T_A is traceless. This holds also for an inversely oriented link, with the conjugated negative generator. The remaining extra Dirichlet-form term is

 (3/(2a)) |Ω|² (1/3)Σ_A Tr[(D_e^A U_p)^†D_e^A U_p]
 = (3/(2a))|Ω|²(8/3)= (4/a)|Ω|².

Every link occurs once in the simple path. Nonpath links contribute no extra term. Multiplication by the smooth bounded transporter preserves the electric form domain, so this identity is valid for the ground vector without assuming pointwise differentiability. Integration yields <Ψ,HΨ>=E_0+4L/a, and the variational principle proves the upper bound. No expectation of an open line in the neutral state or positivity of a spatial Wilson loop is used.

## 8. Scope and actual unresolved extensions

The result is a uniform finite-volume/separation bound for externally supplied fundamental endpoint probes in the supplied compact Hamiltonian. It gives a genuine linear energetic cost in this model at sufficiently small av. It does not establish convergence of E_xy−E_0 as the volume grows, physical quark dynamics, a temporal Wilson-loop identity, numerical thresholds, a continuum limit or axiom selection. The gap paper's global circles alone would not label static sectors; the new ingredients are equivariant creation coordinates, finite source-tensor amplification, joint ghost-vacuum restriction and the actual free charged threshold. No finite-matrix test has been substituted for these operator/domain arguments.
