---
claim_id: native_ward_direct_overlap_note_2026-09-10
claim_type: bounded_theorem
claim_scope: "Supplied infinite native Gaussian reference: the ninety-term direct two-link resolvent overlap exceeds 3/h^2; the full Ward node scalar remains undetermined."
upstream_dependencies:
  - native_infinite_star_node_reduction_note_2026-09-09
  - native_finite_excitation_ward_note_2026-09-09
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
runner: scripts/native_ward_direct_overlap_2026_09_10.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Positive direct overlap with the full Ward correction retained

Claim type: bounded_theorem

**Status: conditional-support.** In the supplied infinite native model, the sum of the ninety ordered disjoint-pair resolvent overlaps is strictly greater than (3/h^2). This is a bound on the direct term. It establishes neither the sign nor the nonvanishing of the full node scalar (alpha).

Use the same original pure Gaussian reference (Omega), normalization (h=2|t_{mathrm{hop}}|>0), and local two-link defects as the [native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [free dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md), [infinite node theorem](NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md), and [bounded Ward identity](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md). In particular the imported impurity bound is (D_Age h/4), with the **same reference vacuum energy** for every (A). No uniform gap in the free active bath or finite-volume threshold is assumed.

## The direct term

Work first at (h=1). Let (A) range over the fifteen two-subsets of the six star legs, (R_A=-D_A^{-1}), and

\[
 Q=\sum_{A\cap C=\varnothing}\langle\Omega,R_C R_A\Omega\rangle .
\]

The sum is ordered and has ninety terms. Each individual cross overlap need not be positive.

Write (D_A=H_0+B_A), with (H_0Omega=0). In the action convention (B_A=igamma_0gamma(d_A)), where (d_A) is orthogonal to the center and (|d_A|^2=2). The CAR therefore give (B_A^2=2I). Signed cubic symmetry and the canonical dispersion give

\[
 c=\langle B_A\rangle=\mu/3,\qquad
 \mu=\mathbb E\sqrt X,\quad \mathbb EX=6,
 \qquad \frac14\le c\le\frac{\sqrt6}{3}<\frac{49}{60}.
\]

This is the reference expectation, not the impurity ground-energy shift. No acquired scalar value is used. The free one-particle generator has norm at most (6). A local quadratic (B_A) applied to a pure Gaussian vacuum has only vacuum and two-particle components, with free energy at most (12). Thus the relevant moments are well-defined and

\[
 \langle D_A\rangle=c,\qquad \langle D_A^2\rangle=2,\qquad
 \langle D_A^3\rangle
 =\langle B_A\Omega,H_0B_A\Omega\rangle+2c
 \le24+2c<26. \tag{1}
\]

The domain assertion follows from this finite-particle energy support and the bounded local perturbation; it does not require a gap for (H_0).

Put (m_A=langle D_A^{-1}angle). Cauchy–Schwarz applied to (D_A^{-1/2}Omega) and (D_A^{1/2}(a+bD_A)Omega) yields

\[
 m_A\ge\frac{(a+bc)^2}{ca^2+4ab+26b^2}.
\]

The replacement of the third moment by (26) enlarges the denominator. Its matrix is positive definite for (cge1/4). Optimizing over ((a,b)) gives

\[
 m_A\ge f(c)=\frac{26-4c+c^3}{26c-4}
 \ge m_0=\frac{5028049}{3722400}>\frac43. \tag{2}
\]

Indeed the derivative numerator of (f) is (52c^3-12c^2-660<0) on the stated interval.

Let (T_{CA}=1) for disjoint pairs and (0) otherwise. This Kneser adjacency matrix has spectrum (6,-3,1), with multiplicities (1,5,9). Decompose (D_A^{-1}Omega=m_AOmega+u_A^perp). Since (Tge-3I) and (D_A^{-2}le4D_A^{-1}),

\[
 Q\ge m^*(T+3I)m-12\sum_A m_A.
\]

Writing (m=m_0\mathbf1+t), with each (t_Age0), and using the positive semidefiniteness and row sum (9) of (T+3I), the remaining correction is
((18m_0-12)\sum_A t_A+t^*(T+3I)t\ge0). Consequently

\[
 Q\ge135m_0^2-180m_0
 =\frac{326063949601}{102638976000}>3. \tag{3}
\]

Restoring units proves (Q>3/h^2). This argument does not assume equal (m_A) or eliminate any vector-valued negative channel.

## Where the full node problem remains

The bounded native identities are ([W_A,D_A]=-J_A), ({W_A,gamma_0}=4), with (W_A) Hermitian and (J_A) anti-Hermitian. Define vectors in the direct sum of fifteen copies of the original Hilbert space:

\[
 x_A=R_A\Omega,\qquad
 v_A=R_AJ_AR_A\Omega=(R_AW_A-W_AR_A)\Omega,\qquad
 p_A=\gamma_0v_A.
\]

Retaining both Ward boundary terms gives the exact identity

\[
 8\alpha=\langle x,Tx\rangle-\operatorname{Re}\langle x,Tp\rangle. \tag{4}
\]

For the incidence matrix (L_{Ai}=1_{i\in A}-1/3), set
(E_0=\mathbf1\mathbf1^*/15), (E_1=LL^*/4), and (E_2=I-E_0-E_1). These are orthogonal projections and (T=6E_0-3E_1+E_2). With (y=x-p/2), equation (4) becomes

\[
 8\alpha=\sum_{j=0}^2\lambda_j
 \left(\|E_jy\|^2-\frac14\|E_jp\|^2\right),
 \qquad (\lambda_0,\lambda_1,\lambda_2)=(6,-3,1). \tag{5}
\]

Thus six nonnegative squared norms give a possible certificate, but their signed combination is not determined by positivity alone. Cubic symmetry annihilates the negative channel of the **scalar vacuum components**, which depend only on opposite versus perpendicular pairs. It does not annihilate (E_1x) or (E_1p) as Hilbert-space vectors. The direct lower bound (3) supplies no upper bound on the correction in (4).

For a perfect matching (A,C,D), the inverse-source identity gives (W_A+W_C+W_D=6gamma_0). Hence (V_A=W_A-2gamma_0) sums to zero and has zero center coefficient. Its white-sublattice CAR field commutes with every quadratic pair perturbation (B_C), so ([V_A,D_C]=[V_A,H_0]). These useful identities do not make the different resolvents commute and do not cancel the correction in (4).

## Evidence boundary

The paired standard-library runner checks exact rational constants, the fifteen-pair projections, and all ninety terms of a nonphysical two-dimensional Ward boundary fixture. Semantic controls reject a wrong boundary sign and a wrong Kneser eigenvalue. These checks support the algebra; the infinite native assumptions and domain proof are supplied above and through the named imports. No physical Gaussian kernels, scalar acquisition, spectra, or native operator calculations are run. The packet preserves the original research source and independent source review. Canonical review, integration and formal audit are separate statuses; no audit verdict is supplied here.
