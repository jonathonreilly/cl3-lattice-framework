---
claim_id: native_uniform_quasilocal_star_vertex_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied full native cubic model with uniform flux stiffness: a rapidly quasi-local exact star vacuum creator, uniformly bounded one-particle form factor and singleton inverse-kernel rows. No interacting phase or full effective-operator locality."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
  - native_uniform_cubic_flux_defect_stiffness_note_2026-09-08
  - native_weak_electric_joint_defect_bounds_note_2026-09-09
runner: scripts/native_uniform_quasilocal_star_vertex_2026_09_09.py
---

# A uniformly quasi-local native star vacuum vertex

**Status:** conditional-support on the supplied Hamiltonian, canonical Gaussian reference and uniform flux stiffness. Trace class: frontier_discovery. No audit verdict or axiom closure is asserted.

The [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [canonical endpoint dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md) and [uniform flux stiffness](NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md) give the following uniform bound without a uniform active-fermion gap. It addresses a missing input to the [local joint-defect problem](NATIVE_WEAK_ELECTRIC_JOINT_DEFECT_BOUNDS_NOTE_2026-09-09.md), but does not resolve that interacting problem.

## Domain and theorem

Take the supplied uniform full native model on cubic tori of side \(L=4M\), \(M\ge32\), with nonzero hopping scale \(h=2|t|\). Use the canonical minimizing pi-flux orbit, its pure active Gaussian vacuum \(\Omega\), and the canonical antiperiodic grids. The active frequencies are
\[
\omega(k)=4|t|\sqrt{\sin^2 k_1+\sin^2 k_2+\sin^2 k_3},
\qquad k_a=2\pi(n_a+1/2)/L.
\]
These grids contain no active zero modes. The physical Gauss quotient and spectators are those of the full dictionary, not a separately supplied low-charge model. The reference energy \(E_0\) is the canonical global minimum in the stiffness theorem. Its bound is
\[
H_0\ge E_0+\kappa K_{\rm def},\qquad
\kappa=1161h/204800>0.
\]
The proof also works with any uniform positive stiffness satisfying these same hypotheses.

Let \(A\) be a two-edge subset of the six-edge star at \(v\), let \(H_A\) reverse those two links in the active Hamiltonian, and put \(R_A=(E_0-H_A)^{-1}\). On the **full active space, in both parities, relative to this same \(E_0\)**,
\[
H_A-E_0\ge6\kappa I.
\]
The physical spectator freedom realizes either active parity, so a physical sector lower bound applies to the whole active spectrum. Opposite pairs have eight bad faces; perpendicular pairs have six. A reference with a different higher energy would not license this inequality.

Define the actual third-order singleton-star vacuum transition
\[
\chi_v=O_v\Omega,\qquad
O_v=\frac18\sum_{A\cap C=\varnothing}R_C\gamma_vR_A,
\tag{1}
\]
where \(A,C\) range over two-edge subsets of that star. There are \(15\cdot6=90\) ordered terms. There exist odd operators \(Y_v\), not necessarily Hermitian, with
\[
Y_v\Omega=\chi_v,\quad \|Y_v\|\le C_0,\quad
\|Y_v-Y_{v,r}\|\le C_p(1+r)^{-p}\quad(p>0),
\tag{2}
\]
where \(Y_{v,r}\) is supported in the radius-\(r\) ball. Constants depend on \(p,h,\kappa\), not \(L\). This is an exact vacuum-creating representative; it is not equality \(Y_v=O_v\) on excited states.

The one-particle vector has a representation
\[
P_1\chi_v=\sum_j c_{vj}\gamma_j\Omega,
\qquad \sum_j|c_{vj}|\le C_1,
\tag{3}
\]
uniformly in volume. Magnetic translates give a uniformly bounded fixed-cell Fourier form factor. The one-particle singleton inverse kernel
\[
T_{vw}=\langle P_1\chi_v,(H_0-E_0)^{-1}P_1\chi_w\rangle
\tag{4}
\]
has uniformly bounded row \(\ell^2\) norm. It follows that its corresponding linear spectator fields, and local CAR commutators of its self-adjoint quadratic part, are uniformly bounded. No row \(\ell^1\) estimate, node value, full sixth coefficient, extensive operator norm or interacting phase follows.

## Why (1) is the native star transition

The nonconstant electric penalty is \(V=\frac12\sum Z_eZ_{e'}\), over distinct incident edge pairs. Three insertions toggling a singleton star must partition its six edges into three pairs, all centered at the same vertex: the outer neighbors are mutually nonadjacent. There are fifteen partitions and six orders. Nonempty one- and two-pair prefixes are not gauge cuts. If \(C\) is the last pair, complementing its star is vertex gauge, so
\[
H_{{\rm star}\setminus C}=\gamma_vH_C\gamma_v.
\]
The full Gauss closure is \(-i\gamma_v\beta_v\), with the dictionary convention \(\beta=i(c^\dagger-c)\). The chronological two resolvents and closure therefore produce the actual term \(-iO_v\beta_v\), including the electric factor \(1/8\). Exchanging \(A,C\) proves \(O_v\) Hermitian; it is odd in active CAR. Zero-toggle histories and mixed sixth-order histories are separate terms and are not discarded by this definition. This energy-dependent vacuum transition does not posit a gapped all-active Schrieffer-Wolff block.

## Smooth inverse and local cocycles

Set \(\delta=6\kappa\). Choose real odd smooth \(f\), zero for \(|x|\le\delta/2\), equal to \(-1/x\) for \(|x|\ge\delta\). It has a Fourier representation
\[
f(x)=\int_{\mathbb R}w(s)e^{-isx}\,ds,
\qquad M_p=\int(1+|s|)^p|w(s)|\,ds<\infty
\]
for every fixed \(p\). For completeness, subtract a scaled \(-x/(1+x^2)\): the difference is integrable, and the rational summand has bounded exponentially decreasing Fourier transform on either half-line. Every positive derivative of \(f\) is integrable. Distributional integration by parts gives arbitrary inverse powers at large \(|s|\), while the subtraction bounds the transform near zero. There is no ultraviolet spectral cutoff.

Functional calculus gives \(R_A=f(H_A-E_0)\) exactly. Write \(H_A=H+B_A\), \(H=H_\pi\). The even quadratic \(B_A\) is supported on the star and has bounded norm. Define
\[
U_A(s)=e^{-isH_A}e^{isH},\qquad
\tau_s(X)=e^{-isH}Xe^{isH}.
\]
Since \(H\Omega=E_0\Omega\),
\[
R_AX\Omega=\int w(s)U_A(s)\tau_s(X)\Omega\,ds.
\]
In particular an exact choice in (2) is
\[
Y_v=\frac18\sum_{A\cap C=\varnothing}\int ds\,dt\,
 w(s)w(t)U_C(t)\tau_t\!\left(\gamma_vU_A(s)\right).
\tag{5}
\]
Unitarity gives \(\|Y_v\|\le(90/8)M_0^2\).

Finite-range bounded quadratic CAR propagation follows directly by summing hopping paths in the one-particle exponential. For fixed \(\mu>0\), tails beyond distance \(r\) have bounds proportional to \(e^{v|s|-\mu r}\), with \(v\) independent of volume. This bounds evolved local quadratic perturbations and the odd center Majorana using graded locality. Construct ball-truncated cocycles with Hermitian truncated generators. Duhamel comparison of their unitary evolutions bounds the error by the integral of the generator error, with polynomial time factors and no volume exponential.

For (5), allocate fixed fractions of the radius to its finitely many factors. On \(|s|+|t|\le cr\), choose \(c\) sufficiently small that the propagation errors are exponentially small in \(r\). On the complement use arbitrary moments \(M_p\), retaining norm one for the unitary factors. This proves (2) for every \(p\). Parity-preserving truncation supplies odd approximants. Finite-torus balls eventually equal the whole torus. Twisted seam signs change no local norm bound, but the spectral and no-zero assumptions remain essential.

## Gaussian extraction and infrared estimate

For any finite-support odd operator \(Y\), complex or non-Hermitian, Gaussian Wick contraction gives
\[
P_1Y\Omega=\sum_j\frac12\langle\Omega,\{\gamma_j,Y\}\Omega\rangle\gamma_j\Omega.
\tag{6}
\]
For a distinct-index odd monomial, the anticommutator removes exactly one leg with its CAR sign; vacuum expectation contracts all remaining legs. These are precisely the one-particle Wick terms. Clifford reduction handles repetitions and linearity handles all local operators. Coefficients vanish outside the support and have modulus at most \(\|Y\|\).

Use dyadic approximants to \(Y_v\). Their successive differences have norm \(O(2^{-np})\) and at most \(O(2^{3n})\) supported sites. For \(p>3\) their extracted coefficient \(\ell^1\) norms are summable. The last whole-torus shell obeys the same estimate. This proves (3), with absolute convergence of the represented vectors. Translated ball constructions preserve magnetic covariance; no continuous choice of band eigenvector at a node is needed.

In a fixed magnetic cell the symbol of (4) is bounded by a fixed constant times \(1/\omega(k)\). Parseval reduces its squared row norm to a constant times the normalized sum of \(\omega(k)^{-2}\). Near each of the finitely many conical zeros, a shifted shell of index \(j\) has \(O((j+1)^2)\) points and inverse frequency squared \(O(L^2/(j+1)^2)\). After multiplication by \(L^{-3}\), summing \(O(L)\) shells is uniformly bounded. The complement is separated from zero. This argument would not apply to a grid with an exact zero mode.

For a real row \(a\), CAR gives \(\|\sum a_j\beta_j\|=\|a\|_2\). For complex \(c=a+ib\), the valid bound is
\[
\left\|\sum c_j\beta_j\right\|\le\|a\|_2+\|b\|_2\le\sqrt2\|c\|_2.
\]
For \(H_b=(i/4)\sum b_{jk}\beta_j\beta_k\) with real antisymmetric \(b\), \([H_b,\beta_v]=-i\sum_k b_{vk}\beta_k\). Realification, or the displayed complex bound, therefore gives the stated local commutator control. This is not a propagation theorem for the interacting system.

## Related local perturbative coefficient

Let \(\psi(U)\) be any finite-volume analytic ground branch from the \(U=0\) ground space, and let \(p_f(U)\) be its bad-face probability. Distinct incident pairs have distinct flipped-face sets \(F_j\): their symmetric difference has at most four edges, whereas any included edge has four incident plaquettes, each requiring a different other edge to give even plaquette intersection. Distinct edges share at most one elementary face for \(L\ge4\), including seams. Thus that nonempty difference would need at least five edges.

The nonempty-sector derivative equation is
\[
P_f\psi'(0)=-\frac12\sum_{j:f\in F_j}(H_0-E_0)^{-1}W_j\psi(0).
\]
Its summands lie in orthogonal exact defect sectors. There are 24 size-six and 8 size-eight pairs through a face, so
\[
\sup_L\limsup_{U\to0^+}\frac{\kappa^2p_f(U)}{U^2}
\le\frac14\left(\frac{24}{6^2}+\frac8{8^2}\right)=\frac{19}{96}.
\]
Ground-subspace derivatives are killed by \(P_f\). The finite set of Rellich branches at each volume also bounds arbitrary ground-state mixtures, including coupling-dependent weights. The order of limits is essential: no uniform remainder, fixed-coupling local joint bound or interchanged limit is claimed.

## Evidence and remaining scope

The portable controls exercise complex odd Gaussian extraction, CAR norm factors, actual periodic face-pair counts and exact shifted-shell arithmetic. They do not numerically prove the infinite family of locality estimates or manufacture numerical values for \(C_p\). The proof uses standard functional calculus, CAR, Wick contraction and finite-range propagation, with their needed steps given above. Original proofs and independent reviews, including the complex-CAR clarification, are preserved in the packet. Node values, higher odd sectors, mixed histories and all-order interacting control remain open. Preparation of the supplied Hamiltonian and Gaussian reference is not derived here.
