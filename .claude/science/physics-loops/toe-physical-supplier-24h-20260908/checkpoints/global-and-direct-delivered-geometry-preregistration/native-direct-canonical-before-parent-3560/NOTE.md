---
claim_id: native_ward_direct_overlap_note_2026-09-10
claim_type: bounded_theorem
claim_scope: "Supplied infinite native Gaussian reference: the ninety-term direct two-link resolvent overlap exceeds 160/h^2; the full Ward node scalar remains undetermined."
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

**Status: conditional-support.** In the supplied infinite native model, the sum of the ninety ordered disjoint-pair resolvent overlaps is strictly greater than \(160/h^2\). This is a bound on the direct term. It establishes neither the sign nor the nonvanishing of the full node scalar \(\alpha\).

Use the same original pure Gaussian reference \(\Omega\), normalization \(h=2|t_{\mathrm{hop}}|>0\), and local two-link defects as the [native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [free dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md), [infinite node theorem](NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md), and [bounded Ward identity](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md). In particular the imported impurity bound is \(D_A\ge h/4\), with the **same reference vacuum energy** for every \(A\). No uniform gap in the free active bath or finite-volume threshold is assumed.

## The direct term

Work first at \(h=1\). Let \(A\) range over the fifteen two-subsets of the six star legs, \(R_A=-D_A^{-1}\), and

\[
 Q=\sum_{A\cap C=\varnothing}\langle\Omega,R_C R_A\Omega\rangle .
\]

The sum is ordered and has ninety terms. Each individual cross overlap need not be positive.

Write \(D_A=H_0+B_A\), with \(H_0\Omega=0\). In the action convention \(B_A=i\gamma_0\gamma(d_A)\), where \(d_A\) is orthogonal to the center and \(|d_A|^2=2\). The CAR therefore give \(B_A^2=2I\). Signed cubic symmetry and the canonical dispersion give

\[
 c=\langle B_A\rangle=\mu/3,\qquad
 \mu=\mathbb E\sqrt X,\quad \mathbb EX=6,
 \qquad \frac14\le c\le\frac{\sqrt6}{3}<\frac{49}{60}.
\]

This is the reference expectation, not the impurity ground-energy shift. No acquired scalar value is used. The free one-particle generator has norm at most \(6\). The quadratic perturbation creates only vacuum and two-particle components, so all displayed third moments are well-defined.

For real orthogonal Majorana vectors \(a,d\), with \(\|a\|=1\), the CAR and \([H_0,\gamma(a)]=i\gamma(K_0a)\) give

\[
 \langle B\Omega,H_0B\Omega\rangle
 =\|d\|^2\langle a,|h_0|a\rangle+
 \langle d,|h_0|d\rangle+2(a^TK_0d)\langle B\rangle.
\]

Here \(B=i\gamma(a)\gamma(d)\). The native signed source obeys \(e_0^TK_0d_A=-2\). The perpendicular neighbor measure is twice the center measure; the opposite neighbor measure is \(X/3\) times that measure. Thus, writing \(\nu=\mathbb E X^{3/2}\),

\[
 \langle D_A^2\rangle=2,\qquad
 \langle D_P^3\rangle=10c,\qquad
 \langle D_O^3\rangle=4c+\nu/3. \tag{1}
\]

The dispersion gives \(\mathbb EX=6\), \(\mathbb EX^2=42\). Hölder and Cauchy imply \(\mu\ge6/\sqrt7\) and \(\nu\le6\sqrt7<16\). Hence \(3/4<c<49/60\) and both third moments are strictly below \(M=43/5\). These identities use the original Gaussian vacuum and bounded perturbation, not an impurity vacuum or a gap in the free bath.

Put \(m_A=\langle D_A^{-1}\rangle\). Cauchy–Schwarz applied to \(D_A^{-1/2}\Omega\) and \(D_A^{1/2}(a+bD_A)\Omega\) gives

\[
 m_A\ge\frac{(a+bc)^2}{ca^2+4ab+Mb^2}
 \geq 0.
\]

The denominator majorant is positive definite since \(Mc-4>0\). Optimizing over \((a,b)\) yields

\[
 m_A\ge f_M(c)=\frac{M-4c+c^3}{Mc-4}
 \ge m_1=\frac{1269649}{653040}>\frac43. \tag{2}
\]

Its derivative numerator \(2Mc^3-12c^2+16-M^2\) is negative on the stated interval, even upon bounding it above by \(2M+16-M^2<0\).

Let \(T_{CA}=1\) for disjoint pairs and \(0\) otherwise. This Kneser adjacency matrix has spectrum \(6,-3,1\), with multiplicities \(1,5,9\). Decompose \(D_A^{-1}\Omega=m_A\Omega+u_A^\perp\). Since \(T\ge-3I\) and \(D_A^{-2}\le4D_A^{-1}\),

\[
 Q\ge m^*(T+3I)m-12\sum_A m_A.
\]

Writing \(m=m_1\mathbf1+t\), with each \(t_A\ge0\), and using the positive semidefiniteness and row sum \(9\) of \(T+3I\), the remaining correction is
\((18m_1-12)\sum_A t_A+t^*(T+3I)t\ge0\). Consequently

\[
 Q\ge135m_1^2-180m_1
 =\frac{506499805921}{3158972160}>160. \tag{3}
\]

Restoring units proves \(Q>160/h^2\). This argument does not assume equal \(m_A\) or eliminate any vector-valued negative channel.

## Where the full node problem remains

The bounded native identities are \([W_A,D_A]=-J_A\), \(\{W_A,\gamma_0\}=4\), with \(W_A\) Hermitian and \(J_A\) anti-Hermitian. Define vectors in the direct sum of fifteen copies of the original Hilbert space:

\[
 x_A=R_A\Omega,\qquad
 v_A=R_AJ_AR_A\Omega=(R_AW_A-W_AR_A)\Omega,\qquad
 p_A=\gamma_0v_A.
\]

Retaining both Ward boundary terms gives the exact identity

\[
 8\alpha=\langle x,Tx\rangle-\operatorname{Re}\langle x,Tp\rangle. \tag{4}
\]

For the incidence matrix \(L_{Ai}=1_{i\in A}-1/3\), set
\(E_0=\mathbf1\mathbf1^*/15\), \(E_1=LL^*/4\), and \(E_2=I-E_0-E_1\). These are orthogonal projections and \(T=6E_0-3E_1+E_2\). With \(y=x-p/2\), equation (4) becomes

\[
 8\alpha=\sum_{j=0}^2\lambda_j
 \left(\|E_jy\|^2-\frac14\|E_jp\|^2\right),
 \qquad (\lambda_0,\lambda_1,\lambda_2)=(6,-3,1). \tag{5}
\]

Thus six nonnegative squared norms give a possible certificate, but their signed combination is not determined by positivity alone. Cubic symmetry annihilates the negative channel of the **scalar vacuum components**, which depend only on opposite versus perpendicular pairs. It does not annihilate \(E_1x\) or \(E_1p\) as Hilbert-space vectors. The direct lower bound (3) supplies no upper bound on the correction in (4).

For a perfect matching \(A,C,D\), the inverse-source identity gives \(W_A+W_C+W_D=6\gamma_0\). Hence \(V_A=W_A-2\gamma_0\) sums to zero and has zero center coefficient. Its white-sublattice CAR field commutes with every quadratic pair perturbation \(B_C\), so \([V_A,D_C]=[V_A,H_0]\). These useful identities do not make the different resolvents commute and do not cancel the correction in (4).

## Evidence boundary

The paired standard-library runner checks exact rational constants, the fifteen-pair projections, and all ninety terms of a nonphysical two-dimensional Ward boundary fixture. Semantic controls reject a wrong boundary sign and a wrong Kneser eigenvalue. These checks support the algebra; the infinite native assumptions and domain proof are supplied above and through the named imports. No physical Gaussian kernels, scalar acquisition, spectra, or native operator calculations are run. The packet preserves the original research source and independent source review. Canonical review, integration and formal audit are separate statuses; no audit verdict is supplied here.
