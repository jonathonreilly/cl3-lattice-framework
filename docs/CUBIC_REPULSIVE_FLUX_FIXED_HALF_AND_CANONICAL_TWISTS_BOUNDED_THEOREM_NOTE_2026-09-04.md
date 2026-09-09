---
claim_id: cubic_repulsive_flux_fixed_half_and_canonical_twists_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "For the declared spinless fermion Hamiltonian with uniform nearest-neighbor hopping magnitude t>0 and uniform repulsion V>=0 on a rectangular three-dimensional torus whose side lengths are even and at least four, a canonical background field with pi flux through every elementary plaquette and Wilson sign (-1)^(L_i/2-1) in direction i minimizes the ground energy at exactly half filling over all U(1) hopping phases. The fixed-number statement follows from a charge-preserving polar reflection inequality and the established flux-phase reflection construction. At V=0 the canonical finite-volume field has the stated zero-free staggered spectrum. This is a supplied-model theorem and an application of established literature, not dynamical flux selection, uniqueness of the interacting minimizer, or a Record-formation theorem."
upstream_dependencies: []
runner: scripts/cubic_repulsive_flux_fixed_half_2026_09_04.py
---

# Fixed-half-filled repulsive matter: a global cubic flux minimum

**Date:** 2026-09-04

**Type:** bounded_theorem

**Status:** proposed_retained

**Audit:** unset. This is an author proposal; independent audit determines any effective status.

**Primary runner:** [fixed-half flux checks](../scripts/cubic_repulsive_flux_fixed_half_2026_09_04.py), with [computed cache](../logs/runner-cache/cubic_repulsive_flux_fixed_half_2026_09_04.txt).

**Independent checker:** [Pauli-tensor and exact-algebra checks](../scripts/cubic_repulsive_flux_fixed_half_independent_check_2026_09_04.py), with [computed cache](../logs/runner-cache/cubic_repulsive_flux_fixed_half_independent_check_2026_09_04.txt).

## Machine status

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "An interacting global-minimality certificate on tori."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review this supplied-model bridge, then construct shared Record-matter-gauge dynamics."
conditional_surface_status: "Global fixed-half flux comparison for the declared uniform repulsive model."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Known reflection-positive mathematics applied with an explicit fixed-number bridge and complete torus twists; no framework dynamics is derived."
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/cubic_repulsive_flux_fixed_half_independent_check_2026_09_04.py
```

The named downstream consumer is the interacting torus comparison left open in PR #7878, in its section "Interfaces named for other lanes, not moved here". This is an open-PR scientific residual, not a quoted audit verdict or a framework-level closure.

## Exact target and scientific value

The target is a global background-flux energy comparison for one already proposed interacting matter Hamiltonian. It replaces a finite-cluster uncertainty with an applicable established reflection-positivity argument, including the particle-number and boundary conditions needed by the repo's formulation.

[PR #7874](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7874) establishes free global minimization on a cube and one small torus; [PR #7878](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7878) studies a repulsive interaction on finite clusters and perturbatively on tori. Their descriptions of the classical flux theorem as planar-only or free-only are inaccurate: Lieb explicitly includes higher-dimensional cubic geometries and interactions, and Macris–Nachtergaele explicitly discuss spinless repulsive nearest-neighbor interactions. Their full-Fock-space formulation still requires care before invoking it at fixed particle number. [Lieb, 1994](https://arxiv.org/abs/cond-mat/9410025); [Macris–Nachtergaele, 1996](https://arxiv.org/abs/cond-mat/9604043).

The supplied carrier, Hamiltonian, filling and equilibrium comparison remain physical premises. A variational minimum does not cause transitions between conserved flux sectors. This note supplies no apparatus, formation rate, Born-law derivation, gravity source, coupling normalization or physical clock. Its purpose is to settle the precise static prerequisite so subsequent work can address those dynamical interfaces.

## Domain, imports and obligations

Let

\[
\Lambda=\mathbb Z/L_1\mathbb Z\times\mathbb Z/L_2\mathbb Z\times\mathbb Z/L_3\mathbb Z,
\quad L_i\in2\mathbb N,\quad L_i\ge4,\quad W=|\Lambda|.
\]

Every undirected nearest-neighbor bond is counted once. The graph is simple, bipartite and six-regular. There is one canonical fermion mode per vertex. For antisymmetric phases \(\phi_{yx}=-\phi_{xy}\), define

\[
H_u(\phi)=-t\sum_{\langle xy\rangle}
\left(e^{i\phi_{xy}}c_x^\dagger c_y+e^{-i\phi_{xy}}c_y^\dagger c_x\right)
+V\sum_{\langle xy\rangle}n_xn_y,
\quad t>0,\quad V\ge0.
\]

The target energy is \(E_{W/2}(\phi)=\min\operatorname{spec}(H_u(\phi)|_{N=W/2})\). Hopping phases are variable classical background parameters; their magnitudes and the interaction are fixed. No phase dynamics is implicit in this definition.

| Obligation | Resolution |
|---|---|
| Match the literature's centered interaction | Exact scalar shift inside the fixed-half-filled sector |
| Preserve fixed particle number in the comparison | Right particle–hole turns it into zero charge; both polar trial states retain zero charge |
| Establish the reflection geometry | Uniform even rectangular tori and an explicitly closed basic cycle set |
| Include global holonomies | All straight winding loops, with the length-mod-four canonical rule |
| Obtain a global minimum | Compactness and the canonical-cycle improvement argument, not a random phase search |
| Check the free finite-volume sea | Explicit staggered Bloch spectrum and canonical boundary twists |
| Connect to the physical framework | Remains conditional on this supplied model and equilibrium formulation |

The external mathematical input is the fermionic reflection construction and canonical-cycle argument in Macris–Nachtergaele, Theorem 1.4 and Section 2. The charge-restricted matrix argument is given below so fixed particle number is checked rather than inferred from mean density. This use of known reflection-positive mathematics carries no claim to a newly discovered general flux theorem.

## Centering and particle number

Write \(H_c\) for the same kinetic term with interaction \(V\sum(n_x-1/2)(n_y-1/2)\). On any regular degree-\(z\) graph,

\[
H_c=H_u-\frac{zV}{2}N+\frac{V|E|}{4}.
\]

Consequently, on this torus at \(N=W/2\),

\[
H_c|_{N=W/2}=H_u|_{N=W/2}-\frac{3VW}{4}I.
\]

Every phase comparison in that sector is unchanged. On the full Fock space the difference contains the chemical-potential term \(-3VN\); it is not a constant. The full-Fock centered model corresponds to a supplied chemical potential \(3V\), and does not derive the density of the uncentered model at zero chemical potential. On an irregular graph the correction is \(-(V/2)\sum_x d_xn_x\), which is generally nonconstant even at fixed total number.

## The charge-preserving reflection inequality

Use matching half-space Fock bases in which the number operator \(n\) is diagonal. Consider

\[
T(A,B)=A\otimes I+I\otimes B-\sum_a K_a\otimes K_a,
\]

where \(A,B\) are Hermitian and commute with \(n\), every \(K_a\) is real, and the total cross operator is Hermitian. Creation and annihilation matrices occur as a pair; a centered density matrix is also real. Positive coefficients are absorbed into the \(K_a\).

Represent a unit vector by its coefficient matrix \(C\), so \(\psi_C=\sum_{ij}C_{ij}|i\rangle|j\rangle\) and \(\operatorname{tr}C^\dagger C=1\). Set

\[
L=(CC^\dagger)^{1/2},\qquad R=(C^\dagger C)^{1/2}.
\]

Both \(\psi_L\) and \(\psi_R\) have norm one. The two local energy terms are

\[
\operatorname{tr}(AL^2)+\operatorname{tr}(B^T R^2).
\]

For a real cross matrix \(K\), the contribution before its minus sign is

\[
X(C,K)=\operatorname{tr}(C^\dagger KCK^T)
=\operatorname{tr}(C^\dagger KCK^\dagger).
\]

The transpose comes from contraction with the right tensor factor. Its equality to the adjoint uses the declared reality of \(K\).

Take an SVD \(C=UDV^\dagger\), \(D=\operatorname{diag}(d_i)\ge0\). Termwise application of \(2\operatorname{Re}(a\bar b)\le |a|^2+|b|^2\) gives

\[
\begin{split}
\operatorname{Re}X(C,K)
&=\operatorname{Re}\sum_{ij}d_id_j(U^\dagger KU)_{ij}
\overline{(V^\dagger KV)_{ij}}\\
&\le\frac12\left[\operatorname{tr}(LKLK^\dagger)+
\operatorname{tr}(RKRK^\dagger)\right].
\end{split}
\]

The sum of cross expectations is real because the Hamiltonian is Hermitian. Combining it with the exact local terms yields

\[
\mathcal E(C;A,B)\ge\frac12\left[
\mathcal E(L;A,\bar A)+\mathcal E(R;\bar B,B)\right].\tag{1}
\]

Here the bar is entrywise complex conjugation. Its placement matters even though the \(K_a\) are real.

For \(Q=n\otimes I-I\otimes n\), the condition \(Q\psi_C=0\) is \([n,C]=0\). Functional calculus then gives \([n,L]=[n,R]=0\). Thus both comparison states in (1) remain in the zero-charge sector. Taking minima in that sector proves the charge-restricted reflection inequality. This is stronger information than an average density of one half.

The proof also explains a useful separate observation: if \(nC-Cn=qC\) for any fixed \(q\), then \(CC^\dagger\) and \(C^\dagger C\) still commute with \(n\). At a reflection-symmetric Hamiltonian \(T(A,\bar A)\) that conserves \(Q\), choose a ground vector of definite \(Q\). Its two polar states lie at \(Q=0\), and (1) forces them to be ground states too. This is an existence statement for a zero-charge ground state in that centered reflection-positive model, not a claim that every ground state has that charge.

## Applying the comparison to fermions

Cut an even torus across a pair of opposite bond-centered coordinate planes. Reflection identifies the two halves, and crossing edges form a matching. The standard fermionic construction has three steps.

First, with \(P_L=(-1)^{N_L}\), put \(d_x=P_Lc_x\), \(d_x^\dagger=c_x^\dagger P_L\). Operators within either half obey CAR, whereas the two half algebras commute. Occupations are unchanged. In the left half this is a real diagonal basis change \((-1)^{N_L(N_L-1)/2}\); in the right half it cancels the usual Jordan–Wigner half-space parity. Matching real Fock matrices can therefore be used on both halves.

Second, apply particle–hole conjugation to the right half. The original total number becomes \(|R|+Q\). Since \(|L|=|R|=W/2\), original fixed half filling is exactly \(Q=0\). Centered densities on the right change sign: internal interaction terms retain their sign, while crossing repulsive density terms become negative products of matching real density matrices.

Third, use site phases to make each crossing hopping real and negative. The crossing matching makes this possible without altering fluxes. The hopping cross terms become a negative sum of matching creation–creation and annihilation–annihilation tensor products. With \(V\ge0\), both kinds of crossing term therefore have the sign required in (1). Internal half Hamiltonians conserve their own number operator.

All three transformations preserve the statement that the original sector is represented by \(Q=0\). Replacing the right transformed Hamiltonian by \(\bar A\), or the left by \(\bar B\), consequently gives an energy comparison in the original fixed-half-filled sector. Uniform density interactions are preserved by these replacements. In the original hopping matrix, after the crossing gauge is fixed, the left-reflected field keeps \(h_{LL}\) and replaces \(h_{RR}\) by \(-h_{LL}\) in reflected site order; the opposite replacement keeps the right half.

For a basic cycle of length \(2m\) cut by the plane, the phase contributions from its two halves then pair to produce \((m-1)\pi\) modulo \(2\pi\). This is \(\pi\) at length zero modulo four and zero at length two modulo four. A reflected internal cycle receives the negative of the original flux, with the orientations used in the comparison. Both canonical values are unchanged by that negation.

## Global minimization and canonical Wilson twists

Use a redundant basic set consisting of every elementary plaquette and every straight winding loop at every transverse coordinate. Plaquettes generate contractible cycle changes; the three winding directions supply the remaining integer homology generators. Thus their fluxes determine the gauge class. Including all parallel winding loops makes this finite set closed under every coordinate reflection. Every basic cycle intersecting a cut is reflected into itself up to orientation. Uniform hopping magnitudes and uniform interaction strengths satisfy the required reflection invariance.

The phase parameter space is compact and the fixed-sector ground energy is continuous. Choose an energy-minimizing field with the largest possible number of canonical basic cycles. If one basic cycle is noncanonical, choose a cut intersecting it. Inequality (1) implies that both reflected fields also minimize the energy. Their canonical-cycle counts sum to twice the old count plus twice the number of noncanonical cycles crossing the cut. At least one reflected minimizer therefore has a larger count, a contradiction. Hence a canonical minimizer exists.

Each plaquette has flux \(\pi\). A straight winding loop of length \(L_i\) has canonical phase \(\pi(L_i/2-1)\), so its Wilson sign is

\[
w_i=(-1)^{L_i/2-1}=
\begin{cases}-1,&L_i=0\pmod4,\\+1,&L_i=2\pmod4.\end{cases}
\]

An explicit representative is the Kawamoto–Smit sign field

\[
\eta_1(x)=1,\qquad\eta_2(x)=(-1)^{x_1},\qquad
\eta_3(x)=(-1)^{x_1+x_2},
\]

multiplied by \(w_i\) on one seam in each direction. Every plaquette stays negative. Since \(L_i\) is even, the untwisted straight Wilson products are positive; the seam supplies exactly \(w_i\). Parallel winding loops agree because a strip between them contains an even number of negative plaquettes.

It follows that this canonical field minimizes \(E_{W/2}\) over all U(1) phases, and hence also over the Z2 subclass containing it. This proves existence of a global minimizer, not uniqueness among all fields. The explicit length-two exclusion prevents treating a periodic multigraph as a simple six-neighbor torus.

## Free finite-volume sea

Set \(V=0\). On a two-site cell in each spatial direction, the staggered hopping has three pairwise anticommuting Hermitian Clifford matrices and Bloch energies

\[
\varepsilon_\pm(k)=\pm2t\sqrt{\cos^2k_1+\cos^2k_2+\cos^2k_3},
\]

each of multiplicity four. For a seam with twist \(\delta_i\in\{0,1/2\}\), use

\[
k_i=\frac{2\pi(m_i+\delta_i)}{L_i},\qquad
m_i=0,\ldots,L_i/2-1.
\]

The canonical rule uses \(\delta_i=1/2\) when \(L_i=0\pmod4\), and zero otherwise. In either case the closest allowed momentum to a zero of cosine has distance \(\pi/L_i\). Therefore

\[
\min|\varepsilon|=2t\sqrt{\sum_i\sin^2(\pi/L_i)}>0.
\]

The finite-volume negative sea is unique at half filling; its fixed-number excitation gap is twice this minimum. Both gaps vanish as the side lengths grow. This is a finite-volume regulator of gapless free matter, not an interacting mass-generation result.

The zero-free sea provides a compatible initial finite-volume state for polar sea-factorization calculations such as [PR #7971](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7971). Record-induced deletion changes the graph and can remove the reflection symmetry used here. No interacting post-deletion minimum, stationary state or Record-history theorem follows by combining those two statements.

## Evidence and independent review

The primary runner returns **15 PASS, 0 FAIL**. The separate checker returns **6 PASS, 0 FAIL**. Each has a declared 180-second timeout. Finite calculations check the implemented identities and fixtures; the arbitrary-volume ground-energy statement is carried by the proof and its declared hypotheses.

| Check | Actual finite evidence |
|---|---|
| Primary polar comparison | 120 zero-charge and 120 nonzero-charge fixtures; missing-conjugation control has margin -1.26463224 |
| Primary physical reflection | Direct bit-CAR construction on the open eight-site cube, fixed N=4; 48 phase/coupling cases, minimum ground-comparison margin 0.00480984757 |
| Primary torus construction | All eight twists on 4^3 and 6^3, plus canonical rectangular fields; direct/Bloch spectral residual at most 1.643e-14 |
| Primary cycle geometry | Four finite rectangular tori, 2,028 cycle and 1,620 cut-cycle instances; the arbitrary-volume reflection closure is proved in the text |
| Independent physical conversion | Full Pauli-tensor eight-mode Hamiltonian restricted to N=4 versus post-particle-hole Q=0; twelve complex-phase fixtures and both reflections, whole-spectrum residual at most 3.4e-14 |
| Independent operator contracts | All 72 Hamiltonians Hermitian and number/charge conserving to zero reported residual; polar charge closure at most 1.2e-15 |
| Independent exact algebra | SymPy missing-bar margin -8/5, positive polar cross margin 2, complex-K transpose control -1 versus invalid adjoint +1 |
| Independent free tori | Clifford square identity and canonical gap on 4^3, 4x4x6 and 6^3; gap-formula error at most 8.9e-15 |

The primary uses tolerance 2e-9 and the checker uses 3e-9; exact SymPy controls use equality. The all-periodic 4^3 control has eight free zero modes and energy 6.58613981 above the canonical free sea in the primary. This is one discriminating field, not a strict-ordering theorem for every noncanonical twist. The checker's centered full-Fock versus N=4 calculation on three open-cube couplings is explicitly diagnostic. Neither runner reads external scientific data; the checker reads its own source only to inspect imports.

Primary and checker execution use separate contexts within the same OpenAI/Codex model family. Their arithmetic and construction routes must remain separate, with no import of the primary by the checker. Root owns the theorem specification, reviews every changed line and checks the central mathematics. This is an execution-independence description, not an audit grade.

## Review record

Root read the source papers, independently derived the fixed-Q polar bridge, and reviewed every line of both implementations. A separate same-family context reviewed the proof before constructing the independent checker without reading the primary implementation. Review repaired the explicit transpose/adjoint distinction, removed a general strict-Wilson-ordering suggestion, connected the primary's geometry constructors to actual domain guards, and required the checker to declare its timeout and use the machine cache envelope.

The supplied-model statement supersedes the planar-only/free-only applicability descriptions in PRs #7874 and #7878; it preserves their finite numerical results and does not adopt their conclusions as premises. The strongest remaining physical obligation is a construction of sector-changing preparation and Record formation under the same gauge-matter dynamics, with its state, rates and energy exchange specified.

The following exact helper mapping is a reviewed **hard landing condition** in `docs/audit/scripts/build_citation_graph.py`, inside `EXPLICIT_PACKET_HELPER_RUNNER_PATHS`:

```python
"cubic_repulsive_flux_fixed_half_and_canonical_twists_bounded_theorem_note_2026-09-04": [
    "scripts/cubic_repulsive_flux_fixed_half_independent_check_2026_09_04.py",
],
```

At the declared base, the claim-scoped helper-registry carve-out in `audit_science_fingerprint.py` excludes this literal mapping from repository-wide policy bytes. The registry mapping remains a reviewed integration condition; this author branch does not alter dependency policy or audit grades. Both runner sources and both machine caches must land with this note. Independent audit remains required.

## Proof boundary and next physical question

The result concerns uniform repulsive spinless nearest-neighbor matter, even rectangular tori, a fixed half-filled sector, and background hopping phases. It supplies neither arbitrary-bond nor arbitrary-geometry coverage. Canonical finite-temperature and uncentered full-Fock claims require their own arguments. The source literature's grand-canonical result is a different ensemble and is not used to replace the fixed-sector proof.

The next physical question is a common process for gauge-sector preparation, continuing matter dynamics and permanent Records, including its energy exchange and gravity source. The present energy comparison can constrain such a process; it does not construct it.
