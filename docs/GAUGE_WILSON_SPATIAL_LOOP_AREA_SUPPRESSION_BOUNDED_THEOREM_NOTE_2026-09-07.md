---
claim_id: gauge_wilson_spatial_loop_area_suppression_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_spatial_loop_area_chain_check_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
  - gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_bounded_theorem_note_2026-09-07
claim_scope: "Explicit imported marked-cluster construction yields volume-uniform small-av spatial-loop area suppression for the supplied compact SU3 Hamiltonian; separate open-geometry first two real-loop Taylor coefficients."
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

For the supplied compact SU(3) Hamiltonian, there are unspecified positive constants u_0 and C_0 such that every qualifying planar rectangle satisfies |omega_u(W_C)|<=C_0^P(u/u_0)^A at sufficiently small u=av, uniformly in periodic volume and in its selected thermodynamic limit. Here A=RS, P=2(R+S), and W_C may be either the complex normalized trace Tr(U_C)/3 or the real normalized trace ReTr(U_C)/3. The proof explicitly imports the complex marked-polymer construction and a pinned-cluster convergence theorem. It does not infer the uniform bound from finite Taylor selection alone.

Separate exact open-geometry formulas for the REAL normalized trace are omega_u(W_square)=u/144+O(u²) and omega_u(W_two-adjacent-faces)=(7/124416)u²+O(u³). These coefficients are not asserted for small periodic boxes with additional minimal fillings. They do not compute u_0, C_0 or a finite-coupling string tension.

The [compact Hamiltonian source](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the supplied action and kinetic normalization. The [all-label electric source](GAUGE_WILSON_COMPACT_CUBE_LOW_ELECTRIC_SPECTRUM_RITZ_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the representation-wide gap used in the applicability map. The [chain helper](../scripts/gauge_wilson_spatial_loop_area_chain_check_2026_09_07.py) performs19 finite checks; the [coefficient helper](../scripts/gauge_wilson_spatial_loop_area_coefficients_check_2026_09_07.py) performs33. Neither proves the imported cluster theorem. Their source hashes, unchanged scientific payloads, original defect, prospective controls and independent reviews are in the [durable packet](../.claude/science/physics-loops/spatial-loop-area-20260907/PROOF_REVIEW.md).

## Proof and provenance conventions

The following two complete derivations are retained as separate parts. Part I was independently written from the exposed marked-expansion route and reviewed by root and primary; Part II is the primary lane's independently derived selection/coefficient proof. Statements about what had or had not been read refer to the frozen original derivation time, before the subsequent cold reviews preserved in the packet. No independent-discovery claim is made for the shared proposed route. Root's separate conservative reserve uses C_0=2ce²; Part I uses C_0=2ce. Both are existential geometry constants from distinct safe reserves, not conflicting physical numbers.

The finite Haar-index table checks a supplied exact contraction and its transpose adverse control; it is not an independent derivation of SU(3) Haar integration. The actual analytic shared-link identity is displayed in Part II. The initial incorrect index checker and its spuriously passing raw output are preserved, not relabeled as validation.

# Part I. Spatial Wilson-loop suppression from a uniform marked expansion

2026-09-07. Conditional mathematical result for the supplied compact Hamiltonian. Root supplied the proposed marked-polymer route before the prospective contract; the detailed weighted pinned-cluster argument below was developed in this lane. This is an explicit mathematical import, not an axiom derivation or a new general cluster-expansion theorem. The primary worker's selection proof and root's completed derivation have not been read before freezing this file.

## Model and precise boundary family

Use cubic periodic volumes with three outgoing SU(3) link spaces per cell. The electric operator is K_e=−3Δ_e/(2a), with all-label energies [p²+pq+q²+3p+3q]/a. Thus its constant vacuum is unique and its first positive energy is 4/a. Put r_f=Re Tr(U_f)/3, H=ΣK_e+vΣ_f(1−r_f), and u=av. The parameter a is the supplied kinetic/temporal-scaling parameter, not a spatial lattice spacing.

For a contractible R×S planar rectangle C, W_C=Tr(U_C)/3 has norm at most one. Write A=RS and P=2(R+S). Take torus side lengths sufficiently large, for example all at least 2max(R,S)+2; more generally the necessary projected condition is A≤L_xL_y/2. The theorem concerns these finite periodic ground states and their selected thermodynamic limit. It does not silently identify different boundary-selected infinite states.

There exist constants u_0>0 and C_0≥1, depending only on the fixed interaction geometry and the imported expansion, such that

|ω_u(W_C)| ≤ C_0^P (|u|/u_0)^A,  0≤u<u_0.

In particular, for 0≤u<u_0/C_0^4, the right side is at most [C_0^4 u/u_0]^A. The constants are not computed numerically. This is a spatial-loop upper bound, not a lower bound, a temporal-loop/static-charge confinement theorem, or a continuum limit.

## Exact applicability of the external expansion

The load-bearing source is Yarotsky, arXiv:math-ph/0412040, Theorem 1 and Section 2 (especially the ordinary polymer bound/count and the marked-insertion argument on printed pages 10–11): https://arxiv.org/pdf/math-ph/0412040 . Infinite-dimensional local spaces and unbounded classical local Hamiltonians are explicitly allowed. The paper treats periodic translation-invariant finite volumes. Its weak-star analyticity statement alone is NOT used as the needed support-dependent bound.

To match its block-vacuum hypothesis rather than merely its terminology, set h_x=(a/4)Σ_{i=1}^3K_(x,i), Λ_0={0,e_1,e_2,e_3}, and tilde h_x=Σ_{y∈x+Λ_0}h_y. Each tilde h_x is classical in a product Peter–Weyl basis, has a unique whole-block vacuum, and gap at least one. On a periodic volume Σ tilde h_x=4Σh_x. The perturbation tilde φ_x(z)=−zΣ_{i<j}r_(x,ij) has norm at most 3|z|. Hence Σ tilde h_x+Σ tilde φ_x(u)=aH−3u|Λ|. It has exactly the desired ground vector. Choose the source's relative-bound parameter small and fixed and then |z| small; bounded perturbations satisfy its form bound. No finite-dimensional truncation is needed.

The source gives ordinary activities bounded by ε^{|γ|}, with ε made arbitrarily small by its time-step and perturbation choices; the number of support/decorated polymers of size n through one point is at most c^n. For a bounded insertion O supported on S it gives marked activity bound ||O|| ε^{|γ_O|−|S|}. These norm estimates extend to complex bounded local couplings by the same sectorial-semigroup estimates and holomorphic bounded perturbation expansion used in Section 2. They are not estimates of a conjugated complex ground vector.

For W_C choose S to be ALL perimeter vertices viewed as outgoing cells, including the otherwise unused corner. This set is connected and |S|=P. Every ordinary component in the marked polymer attaches, directly or through other components, to this connected set. Their union is therefore connected on the fixed finite-range support graph. The bounded-degree animal count applies: after enlarging the geometry constant c, marked supports of size n≥P containing S number at most c^n. Internal Hilbert-space matrix indices are controlled by operator norms, not counted as finitely many spin colors.

## Uniform complex bound and zero-free normalization

For clarity the pinned-cluster estimate is an additional explicit standard mathematical import: the Kotecký–Preiss criterion in Fernández–Procacci, arXiv:math-ph/0605041, equations (2.7), (2.15), https://arxiv.org/pdf/math-ph/0605041 . If Σ_{γ incompatible γ_0}ρ_γ e^{a_γ}≤a_{γ_0}, the absolute pinned cluster sum is at most e^{a_{γ_0}}. The distinguished root may have zero activity; its pinned sum depends only on the ordinary activities.

Choose q=ceε≤1/4. Apply the criterion to weighted ordinary majorants ρ_γ=ε^{|γ|}e^{|γ|/2}, a_γ=|γ|/2. Overcounting incompatibility by a point in γ_0 gives

Σ_{γ incompatible γ_0}ρ_γ e^{a_γ} ≤ |γ_0|Σ_{n≥1}q^n ≤ |γ_0|/3 ≤ a_{γ_0}.

Thus the pinned sum is at most e^{|γ_0|/2}. Multiplying the marked root weight by e^{|γ_0|/2} as well controls an exponential weight in the TOTAL cluster size. Summing roots of size n≥P gives

Σ absolute marked clusters × e^{total size/2}
 ≤ ||O|| ε^(−P)Σ_{n≥P}(ceε)^n
 = ||O||(ce)^P/(1−q) ≤ ||O||(2ce)^P.

Set C_0=2ce, enlarged to at least one. This also gives an exponentially small tail in total cluster size. It supplies normal convergence uniformly in volume and imaginary-time extent, and the local thermodynamic/time limits uniformly on compact complex disks. Large wrapping or distant-boundary clusters are included in that tail, rather than ignored.

The finite-time complex expression is the fixed-vacuum quotient

<Ω_0,e^(−Nt_0 H(z)) O e^(−Nt_0 H(z))Ω_0> / <Ω_0,e^(−2Nt_0 H(z))Ω_0>.

Both semigroups use the SAME z; no adjoint or conjugated z occurs. The ordinary cluster expansion exponentiates the logarithm of the denominator and establishes its nonvanishing on the common disk. Introducing I+λO at the middle and differentiating log at λ=0 selects exactly one marked root. This explains both cancellation of vacuum clusters and the pinned estimate; one does not assume that the marked activity itself is small. For real u the time limit is the unique ground expectation. For complex z the normally convergent marked sum defines its holomorphic continuation and agrees, after the time limit, with its finite-volume analytic ground germ near zero. Uniform complex spectral isolation on the entire disk is not needed or asserted.

## All-order center selection, including repeated insertions

Each independent link-center action U_e→ζU_e, ζ³=1, commutes with K, fixes the electric vacuum, and is compatible with Gauss invariance. Split each r_f into its fundamental and antifundamental characters. Every perturbation insertion carries ±∂f as an F_3 edge chain. An order-n term with W_C can survive only if C+Σ_{j=1}^n σ_j∂f_j=0 over F_3. Repeated plaquettes and opposite orientations are allowed.

This follows directly in the finite-time bounded-perturbation Dyson integrals: the free semigroups commute with the center actions, so a nonneutral vacuum matrix element is zero. It avoids taking traces of individual non-trace-class resolvent products. The denominator has nonzero constant coefficient; therefore division cannot introduce coefficients below the numerator's vanishing order. Uniform complex convergence passes these vanishing derivatives to the ground and thermodynamic limits.

Project chains onto the rectangle's coordinate plane: horizontal faces map to their unit cells, vertical faces to zero. This is a chain map. On the infinite plane a finite 2-chain with prescribed rectangle boundary is unique, because a boundary-free finite chain has equal adjacent coefficients and hence is zero. It has A nonzero cells. Each such cell requires at least one actual horizontal plaquette insertion; hence n≥A even if the chosen faces leave the plane.

On a periodic plane the kernel consists of constant sheets. The three possible projected fillings have support sizes A, L_xL_y−A, L_xL_y. Thus n≥min(A,L_xL_y−A), and the stated half-area restriction gives n≥A. The restriction is substantive: on a 4×4 torus a 3×3 rectangle has a seven-face complementary filling.

## Completion of the estimate

The holomorphic expectation F_C(z) is bounded by C_0^P on |z|<u_0 and has a zero of order at least A at zero. The higher-order Schwarz lemma, applied after division by C_0^P and rescaling the disk, gives |F_C(u)|≤C_0^P(|u|/u_0)^A. No geometric-series denominator is needed. Since P≤4A for positive integer side lengths, the additional smallness u<u_0/C_0^4 gives the stated pure area bound.

The hard imported input is the uniform complex marked expansion, including its norm estimate and ordinary support counting. Finite selection checks alone would not establish the theorem: analytic functions sin(Nz)^A are bounded on the real axis with the same vanishing order but have no uniform complex bound as N grows.

## Finite controls and provenance

The preregistered check.py verifies 19 exact finite identities/controls on the actual 192 oriented positive faces of a 4³ torus, projected boundary rank 15, all three affine fillings for four frozen rectangles, actual lifted boundaries, the adverse complement, repeated triple charge cancellation, and insufficiency of total flux alone. It uses 17.875 MiB and 0.0017 seconds in the preserved run. These are chain/arithmetic checks, not proofs of the external polymer estimates, and do not select u_0 or C_0. Original preregistration and raw JSON are retained. This derivation was frozen before reading the other lanes' completed proofs; root's proposed route and later scheduling messages were available and are credited.


# Part II. All-order rectangular area selection and the first two actual spatial loop coefficients

This is a finite-volume Taylor selection theorem for the supplied compact cubic Hamiltonian. It does not by itself give a uniform complex radius, an area law, a temporal string potential, or physical confinement. Root exposed the one-face u/144 candidate before calculation. The two-face candidate below was independently derived and prospectively frozen before exact checks. Root subsequently requested the separately preregistered periodic half-area extension. No coefficient fitting was used.

## 1. Analytic object and its domain

Take a finite open cubic link graph, with any subset of its actual elementary faces retained, and full link Hilbert space. Put u=av and

 h(u)=h0+u V, h0=a sum_e K_e,
 V=sum_f(1-ReTr(U_f)/3).

The constant face count changes eigenvalues, not ground projections, so use instead V_c=-S/6 with S=sum_f(chi_f+bar chi_f). Here chi_f=Tr(U_f) in the fundamental representation. The free vacuum is the normalized constant0, unique on full link space, and h0 has gap at least4. The bounded centered perturbation has norm at most the face count F. A contour about0 of radius smaller than the free gap defines the analytic Riesz projection P(u) for sufficiently small complex u. Its rank remains1. On real u sufficiently close to0 it is the ground projection; the local eigenvalue and eigenvector branches are isolated. The physical Gauss restriction gives the same ground expectation because the vacuum and perturbation are gauge invariant and this simple branch remains physical.

For a bounded loop observable W define the holomorphic expectation

 f_W(u)=Tr(W P(u))/Tr(P(u))=Tr(W P(u)).             (1)

The equality holds because rankP(u)=TrP(u)=1, also for the non-self-adjoint complex projection. Formula(1), rather than a conjugate-u vector norm, is the analytic continuation. A finite-volume radius follows from the bounded resolvent Neumann series but may shrink with F. No volume-independent analyticity is inferred.

A technical trace point matters. Individual free resolvents need not be trace class. Expand each resolvent factor as P0/z plus Q(z-h0)^(-1)Q. The term containing only Q resolvents is holomorphic inside the contour and integrates to zero. Every other term has a P0 factor and is finite rank, so its contour integral and trace against W are well defined. Thus at order n the coefficient is a finite sum of legitimate finite-rank traces, with precisely n factors of V_c and free resolvents/projectors. This justifies the charge argument without illegally tracing a non-trace-class resolvent integrand.

## 2. Independent edge-center selection

For every link e independently, multiply U_e by zeta=exp(2pi i/3). This is a unitary on Haar L2, commutes with h0 and its resolvents, fixes the constant vacuum and commutes with all vertex gauge actions. An oriented fundamental face character transforms by zeta raised to its signed incidence on that link; its conjugate has the opposite charge. The same holds for an oriented loop character.

Resolve each of the n perturbation factors into a character of one oriented face, with sign sigma_j in{+1,-1}; resolve W_C=(chi_C+bar chi_C)/6 into observable sign sigma_C. Conjugating a finite-rank trace term by each link-center unitary shows it is zero unless

 sigma_C C+sum_(j=1)^n sigma_j partial f_j=0 mod3               (2)

as a one-chain on edges. Repeated insertions count with multiplicity n. Resolvents cannot absorb center charge. Scalar perturbation insertions, if one kept the uncentered V, only decrease the number of available charged faces and cannot improve the lower bound.

Let C be the boundary of an R by S planar xy rectangle at fixed z, with R,S positive integers. Project the finite three-dimensional chain onto the infinite xy square lattice: xy faces go to their base-coordinate squares, xz/yz faces go to zero, x/y edges project normally and z edges go to zero. This is a chain map, including for vertical faces whose two horizontal projected edges cancel. The projected two-chain b over F3 therefore satisfies

 partial b=-sigma_C partial I_rect.              (3)

A finitely supported two-cycle on the infinite square plane is zero. Indeed its edge equations equate the coefficients of neighboring squares; a finite-support constant is zero. Hence b=-sigma_C I_rect. Each of the RS interior squares has nonzero coefficient. Each requires at least one inserted xy face above that square. A face contributes to only one projected square, regardless of its height or orientation. Thus n>=RS.

Consequently every Taylor coefficient of f_(W_C)(u) below order RS vanishes. This conclusion is all-order and geometric; it does not rely on a finite census. The independent phases are Z3 center phases, not a fictitious U1 symmetry. Mod3 cancellation, repeated faces and nonplanar fillings are all included by(2)–(3).

## 3. Periodic variant and its necessary qualification

For a cubic torus project onto its Lx by Ly xy torus. Assume the rectangle is nonwrapping and fits strictly inside the periods as a contractible rectangular loop. Two planar solutions of(3) differ by a constant F3 two-cycle. The three possible coefficient supports have sizes

 A=RS, LxLy-A, LxLy.

Thus the same order-n vanishing for n<A follows if A<=LxLy/2. Without that condition the argument only gives n>=min(A,LxLy-A), and the complementary surface can genuinely be smaller. For example a4by4 rectangle on a5by5 torus has area16 but complement9. No unqualified periodic area16 selection is asserted. The leading coefficients in the next sections are for open geometry, not for small periodic boxes where a second minimal filling could contribute.

## 4. Actual single-face coefficient

Use intermediate normalization for the real-u ground vector, writing psi=0+u psi1+u²psi2+..., with <0,psij>=0 for j>=1. Let R0=Q h0^(-1)Q. Since each elementary face character has four nontrivial fundamental links, it is an exact h0 eigenvector with energy16. Haar meanS=0. Therefore

 psi1=-R0 V_c 0=S/96,
 psi2=-R0 V_c psi1=R0 S²/576.                   (4)

For a retained face p, W_p=(chi_p+bar chi_p)/6 has mean0. At first order only p and its conjugate survive edge-center selection. Haar orthogonality gives integral chi_p bar chi_p=1 and integral chi_p²=0. Hence

 f_(W_p)(u)=u [2*(1/6)*(1/96)*2]+O(u²)
           =u/144+O(u²).                       (5)

This agrees with the exposed root candidate but was obtained directly from the actual character eigenstates and Haar contraction. It is independent of other retained faces at this order.

## 5. Actual two-adjacent-face six-link rectangle

Assume the two adjacent planar faces p,q are retained in an open cubic graph. The rectangle has six distinct exterior links, so W_C0 is an exact free eigenvector of energy24. There is only one projected area-two filling. At order2 condition(2) forces the actual p,q at the loop's height, one insertion of each with opposite orientation to the observable; their exterior charged edges exclude displaced-height fillings. There are two orders and two conjugate choices, four terms in total. No other face pair can contribute.

The Haar value of each term is1/3. To see this on the actual seven-link union of p,q, write the shared link as U and the products of the other three edges of each face as A,B, choosing cyclic order so the face characters are Tr(AU),Tr(U†B) and the rectangle is Tr(AB). Fundamental Haar orthogonality gives

 integral_dU Tr(AU)Tr(U†B)=Tr(AB)/3.

Here the coefficient of A_ij B_kl is delta_jk delta_il/3. Integrating the remaining six independent links gives integral|Tr(AB)|²=1, since their product is Haar. Therefore

 I=integral W_C S²=(4/6)*(1/3)=2/9.             (6)

The u² expectation has a middle term and two endpoint terms. From(4), self-adjointness of R0 and the exact energy24 of W_C0,

 <psi1,W_C psi1>=I/96²=1/41472,
 2 Re<0,W_C psi2>=2I/(576*24)=1/31104.

Normalization of the real ground vector contributes nothing at this order because <0,W_C0>=0 and the first-order expectation vanishes. Thus

 f_(W_C)(u)=(7/124416)u²+O(u³).                 (7)

The two free denominators16 and24 are different and load bearing. Replacing the final rectangle energy24 by16 gives a different, incorrect coefficient. This calculation does not approximate the Hamiltonian by commuting classical plaquette fields: the noncommuting free resolvent is explicitly retained. It computes a spatial loop expectation in the supplied ground state, not a temporal transfer or string energy.

## 6. Independent exact checks and preserved defect

The checker constructs the actual two-cube open graph with12 vertices,20 links and11 faces. Order0/1/2 center-charge censuses give0/0/4 survivors for the six-link rectangle, with all four exactly the planar pair. It verifies shared-link Haar index coefficients, rational free denominators, one-face coefficient, two-face coefficient and a wrong-denominator adverse case. Separate planar/periodic chain checks support indexing only; the all-order proof is Sections2–3.

Self-review before result exposure found that the first Haar tensor checker compared the same incorrectly transposed Kronecker indices on both sides and therefore passed spuriously. The original source/raw are preserved. The corrected index formula and an E01/E10 adverse control distinguish the erroneous transpose. The physical Haar identity, analytic candidates and center census did not change. This failure is recorded rather than presented as an independent validation success.

A uniform analytic bound or marked-cluster result could combine with this selection rule to imply controlled area suppression. That extra theorem is not proved here. Finite-volume Taylor vanishing alone does not establish an area law, an infinite-volume analytic radius, physical confinement or a continuum limit.
