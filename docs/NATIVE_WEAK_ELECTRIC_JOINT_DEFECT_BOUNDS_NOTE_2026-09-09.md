---
claim_id: native_weak_electric_joint_defect_bounds_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied full native Hamiltonian: ground-state joint-defect bounds in a finite-volume coupling window and above an extensive cutoff at fixed small coupling. No fixed-U local thermodynamic stability or spectral gap."
upstream_dependencies:
  - native_weak_electric_defect_density_note_2026-09-08
  - native_uniform_cubic_flux_defect_stiffness_note_2026-09-08
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
runner: scripts/native_weak_electric_joint_defect_bounds_2026_09_09.py
---

# Joint flux-defect bounds with a weak electric penalty

**Status:** conditional-support on the supplied Hamiltonian and upstream stiffness.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Full native H_U=H_0+UD and certified positive stiffness κ."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

The [weak-electric density theorem](NATIVE_WEAK_ELECTRIC_DEFECT_DENSITY_NOTE_2026-09-08.md), [uniform zero-penalty stiffness](NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md), and [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) imply the following joint-event statements. These concern every ground-state density operator, including mixtures in a degenerate ground space. They do not require a uniform active or winding gap.

## Results

Work on the supplied periodic cubic torus with even \(L\ge4\) and \(N=L^3\),
\[
H_U=H_0+UD,\qquad D=\frac32N+V,\qquad
V=\frac12\sum_j W_j,\qquad U\ge0.
\]
Let \(P_f=(1-S_f)/2\) be the commuting bad-face projectors in the canonical magnetic convention, \(K=\sum_fP_f\), and assume the upstream bound \(H_0\ge E_0+\kappa K\), with \(\kappa>0\). For a prescribed face set \(C\), put
\[
m=|C|,\qquad Q_C=\prod_{f\in C}P_f,\qquad p(C)=\operatorname{Tr}(\rho_UQ_C).
\]

**Finite-volume local bound.** If \(0<U\le\kappa/(3N)\) and \(q=32U/\kappa<1\), then
\[
p(C)\le q^{2\lceil m/8\rceil}\quad(m\ge1).
\]
At \(U=0\), \(p(C)=0\) for every nonempty \(C\).

**Macroscopic bound.** For any \(0<U<\kappa/32\), define the integer
\[
m_0=\max\{0,\lceil300N(U/\kappa)^2\rceil-1\}.
\]
Then
\[
p(C)\le
\begin{cases}
1,&m\le m_0,\\
q^{2\lceil(m-m_0)/8\rceil},&m>m_0.
\end{cases}
\]
This second statement allows fixed small coupling but retains an extensive cutoff. It is not a local infinite-volume contour theorem. For \(L=4M\), \(M\ge32\), one may use the explicit upstream value \(\kappa=1161h/204800\), with \(h=2|g\lambda|\).

## Exact local selection and a conditional recursion

The full-carrier electric expansion has \(15N\) incident-edge pairs \(W_j=Z_eZ_{e'}\). Each is a Hermitian unitary. Its flipped-face set \(F_j\) has size six for a perpendicular pair and eight for an opposite pair. Every fixed face is flipped by 24 perpendicular and eight opposite pairs. These counts hold at periodic \(L=4\) seams: every edge belongs to four distinct faces, perpendicular incident edges share exactly one face, and opposite incident edges share none. Consequently at most \(32m\) terms meet a set of \(m\) faces.

First suppose, only for the sets to which a recursion is applied, that
\[
Q_C(H_U-E_U)Q_C\ge\kappa_*mQ_C.\tag{1}
\]
This is a compression inequality, not a commutation assertion. For a normalized ground vector \(\psi\), projection of its eigen-equation gives
\[
Q_C(H_U-E_U)Q_CQ_C\psi=-UQ_CVR_C\psi,
\qquad R_C=I-Q_C.
\]
The inverse on the range of \(Q_C\) has norm at most \(1/(\kappa_*m)\). Terms with \(F_j\cap C=\varnothing\) have zero off-block action. For every remaining term,
\[
\|Q_CW_jR_C\psi\|\le\|Q_{C\setminus F_j}\psi\|.
\]
Indeed \(Q_CW_j=W_jQ'_C\), where \(Q'_C\) demands good faces on \(C\cap F_j\) and bad faces on \(C\setminus F_j\). These projectors commute with \(R_C\), and \(Q'_CR_C\le Q_{C\setminus F_j}\). This controls interference without requiring a flux-diagonal state. Therefore
\[
\sqrt{p(C)}\le\frac{U}{2\kappa_*m}
\sum_{j:F_j\cap C\ne\varnothing}\sqrt{p(C\setminus F_j)}
\le\frac{16U}{\kappa_*}\max_j\sqrt{p(C\setminus F_j)}.\tag{2}
\]
Each removal deletes between one and eight faces. If (1) holds for all integer sizes above a stopping value \(m_0\), and \(16U/\kappa_*<1\), induction from the bound \(p\le1\) below that cutoff yields
\[
p(C)\le(16U/\kappa_*)^{2\lceil(m-m_0)/8\rceil}\quad(m>m_0).\tag{3}
\]
Disconnected subsets must be included: removal can disconnect \(C\). The result holds for every ground vector and hence for any ground-state mixture by linearity. A zero compression range is harmless.

## Proving the two actual compression regimes

Positivity \(D\ge0\) and the canonical-flux variational trial give
\[
E_U\le E_0+\tfrac32UN,
\qquad Q_C(H_U-E_U)Q_C\ge(\kappa m-\tfrac32UN)Q_C.
\]
If \(U\le\kappa/(3N)\), this is at least \(\kappa m/2\) for every \(m\ge1\). Equation (3) with \(\kappa_*=\kappa/2\), \(m_0=0\), proves the finite-volume claim. The coupling window shrinks as \(1/N\); no thermodynamic fixed-coupling assertion is hidden here.

For the stronger macroscopic statement, shift the scalar:
\[
H'=H_0+UV,\qquad E'=E_U-\tfrac32UN\le E_0.
\]
The upstream statewise inequality is
\[
|\langle V\rangle|\le\sqrt{75N\langle K\rangle}.
\]
For every normalized vector in the range of \(Q_C\), let \(k=\langle K\rangle\ge m\). Then
\[
\langle H'-E'\rangle\ge\kappa k-U\sqrt{75Nk}\ge\frac\kappa2 k
\]
whenever \(m\ge300N(U/\kappa)^2\). This proves (1) with \(\kappa_*=\kappa/2\) for precisely the needed sizes. The chosen \(m_0\) ensures every integer \(m>m_0\) meets that real threshold, including equality when the threshold is an integer. Each recursion step reduces \(m\) by at most eight, proving the stated exponent.

This expectation argument can also be expressed as an affine operator inequality. Young's inequality with coefficient \(b=1/4\) gives
\[
H'-E'\ge\frac{3\kappa}{4}K-\frac{75NU^2}{\kappa}I.
\]
It produces the same cutoff. No invalid nonlinear operator inequality involving \(\sqrt{\langle K\rangle}\) is used.

## Contours and the remaining boundary

A connected defective dual-edge set of \(m\) edges through a specified vertex can be encoded by a deterministic Euler tour after doubling **all** its edges. The tour has length \(2m\), recovers cycle-closing edges as well as tree edges, and gives at most \(6^{2m}=36^m\) possibilities. Let \(a=36q^{1/4}<1\). In the finite-volume local regime the probability of a connected defective set through that vertex with at least \(\ell\) edges is at most
\[
\min\{1,a^\ell/(1-a)\}.
\]
In the macroscopic regime, for \(\ell>m_0\), the safe bound is
\[
\min\{1,q^{-m_0/4}a^\ell/(1-a)\}.
\]
The extensive prefactor prevents a fixed-\(U\) local thermodynamic conclusion. Pure winding defects with no bad elementary faces are outside these statements. Finite temperature is not covered by the projected ground-state argument.

A volume-uniform version of (1) for all finite \(C\) at fixed nonzero \(U\) would give a stronger local theorem, but remains unproved. The known mean-density estimate alone cannot supply it. On the same full carrier, mix a canonical flux state with weight \(1-p\) and a state with all elementary faces bad with weight \(p\). Both flux sectors exist on even cubic tori, using staggered canonical and uniform link signs. Every face marginal is \(p\), yet every nonempty joint event has probability \(p\), regardless of size. Translation averaging preserves these identities. These are counterexamples to an inference from mean density, **not** claimed ground states of \(H_U\).

The exact runner checks small geometry, projection-selection identities, integer thresholds and recursion arithmetic. Such finite controls support the explicit general proof; they do not establish it by enumerating examples or solve a perturbed ground state. The original proof and independent reviews are preserved in the branch-local packet. Independent audit status remains pending.
