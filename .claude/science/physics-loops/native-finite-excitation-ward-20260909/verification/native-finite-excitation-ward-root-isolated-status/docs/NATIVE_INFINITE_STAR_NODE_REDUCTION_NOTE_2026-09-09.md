---
claim_id: native_infinite_star_node_reduction_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied canonical infinite Gaussian reference: real scalar native star node, exact soft-resolvent and Laplace representation, and infinite two-link impurity gap h/4. The scalar remains unevaluated."
upstream_dependencies:
  - native_star_thermodynamic_limit_note_2026-09-09
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
  - native_uniform_cubic_flux_defect_stiffness_note_2026-09-08
runner: scripts/native_infinite_star_node_reduction_2026_09_09.py
---

# A scalar node target with controlled native impurity resolvents

**Status:** conditional-support; trace class frontier_discovery. This theorem does not determine whether the node scalar is zero.

Use the [thermodynamic star theorem](NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md), [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [canonical dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md), and [uniform stiffness](NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md). The model, canonical pure Gaussian reference, preparation, and Hamiltonian are supplied. Finite approximants are cubic antiperiodic tori \(L=4M\), \(M\ge32\), with nonzero hopping and the parent's full-active wrong-pair gap relative to the **same** reference energy. Their infinite Gaussian GNS limit is used below. No uniform active-fermion gap is assumed.

Put \(h=2|t_{\rm hop}|>0\). For a two-edge star subset \(A\), let \(B_A\) reverse precisely those two real nearest-neighbor Majorana couplings and write \(H_A=H+B_A\). Initially the parent supplies \(D_A=H_A-E_0\ge\delta I\), \(\delta=6\kappa>0\). The present theorem strengthens the **infinite** inequality to
\[
D_A\ge \frac h4 I.
\]
It also identifies a unique real number \(\alpha\) at the folded Dirac node and expresses it through bounded impurity resolvents, with an explicit imaginary-time tail. Neither a finite-\(L\) threshold for \(h/4\), a value of \(\alpha\), a free effective interacting model, nor a bulk phase follows.

## 1. The actual star transition and its unique node value

The actual third-order vacuum transition is
\[
\chi_v=\frac18\sum_{A\cap C=\varnothing}R_C\gamma_vR_A\Omega,
\qquad R_A=(E_0-H_A)^{-1}=-D_A^{-1}.
\]
There are \(\binom62\binom42=90\) ordered terms. The thermodynamic parent provides a quasi-local odd creator \(Y_v\), \(Y_v\Omega=\chi_v\), and coefficients
\(c_{vj}=\langle\{\gamma_j,Y_v\}\rangle/2\) with every fixed weighted \(\ell^1\) moment finite. Thus the unprojected cell symbol \(C(k)\) is smooth. A creator or its unprojected coefficients need not be unique away from a node.

In a smooth doubled-cell gauge equal to the identity at zero, the active symbol is
\[
\mathsf h(k)=4t_{\rm hop}\sum_{a=1}^3\sin(k_a/2)\Gamma_a,
\qquad \Gamma_a=\Bigl(\prod_{b<a}Z_b\Bigr)X_a.
\]
The \(\Gamma_a\) anticommute and square to the identity. If two smooth coefficient symbols represent the same one-particle vacuum transition, their difference \(D(k)\) obeys \(P_+(k)D(k)=0\) almost everywhere, up to the equivalent row convention. The directional positive-frequency projectors on opposite rays into zero are complementary. Continuity forces both to annihilate \(D(0)\), hence \(D(0)=0\). No value is assigned to the discontinuous band projector at the node.

Magnetic translations act there as \(M_a=X_a\prod_{b>a}Z_b\). Site-centered reflection in coordinate \(a\), restored by vertex gauge \((-1)^{r_a}\), acts as \(Z_a\). These are signed symmetries of the actual Hamiltonian, its defect family, and the canonical Gaussian state. Thus \(C(0)\) commutes with all these matrices. The reflections force a diagonal matrix, and translations connect its eight diagonal entries. Therefore
\[
C(0)=\alpha I_8.
\]
The anti-linear bipartite CAR automorphism \(i\mapsto-i\), \(\gamma_r\mapsto(-1)^{r_1+r_2+r_3}\gamma_r\) preserves the reference and defect Hamiltonians. It gives \(c_{vj}^*=\epsilon_v\epsilon_jc_{vj}\), so \(\alpha\in\mathbb R\). Equivalently one uses this covariance together with uniqueness of the node value.

In this cell convention,
\[
\alpha=\sum_{r\in2\mathbb Z^3}c_{0r},
\]
an absolutely convergent signed sum. Neither a nonzero one-particle norm nor higher-particle weight decides it. Symmetry permits both \(\gamma_v\), with nonzero node value, and \([H,[H,\gamma_v]]\), with vanishing node value. These are comparisons, not replacements for the native star.

## 2. Five ordered pair classes

Name the neighbors \(+x,-x,+y,-y,+z,-z\). Centered cubic signed symmetries partition the ordered disjoint pairs into the following classes:

| \(A\) | \(C\) | Multiplicity |
|---|---|---:|
| \(\{+x,-x\}\) | \(\{+y,-y\}\) | 6 |
| \(\{+x,-x\}\) | \(\{+y,+z\}\) | 12 |
| \(\{+x,+y\}\) | \(\{+z,-z\}\) | 12 |
| \(\{+x,+y\}\) | \(\{-x,-y\}\) | 12 |
| \(\{+x,+y\}\) | \(\{-x,+z\}\) | 48 |

Adjacent-coordinate swaps are restored by \((-1)^{r_ar_b}\). General permutations compose these generators in successively permuted coordinates; for example \(x\leftrightarrow z\) needs \((-1)^{xy+xz+yz}\), not merely \((-1)^{xz}\). All these gauges equal one at the origin and on \(2\mathbb Z^3\). They preserve the local node extraction and map the complete defect families covariantly. The five signed scalar kernels can therefore replace the 90 terms with these weights. No exchange symmetry between \(A\) and \(C\), and no positivity of individual kernels, is assumed. The original overly broad swap wording is preserved in the evidence history.

## 3. A soft annihilator identity without an unbounded zero-mode operator

On a finite AP torus, choose a normalized annihilator \(a_L\Omega_L=0\), \([a_L,H_L]=\omega_La_L\), and rescale it by \(\widetilde a_L=\sqrt{n_{\rm cell}/2}\,a_L\). Its local anticommutators are \(\phi_L(R,s)=e^{ik_L\cdot R}u_L(s)\) for a unit cell spinor. The operator norm grows with volume; it is never used in an estimate. Put \(L_A(\phi_L)=[\widetilde a_L,B_A]\), a fixed-local linear Majorana operator with uniformly bounded coefficients. Exact multiplication gives
\[
\widetilde a_LR_A(E)=R_A(E-\omega_L)\widetilde a_L
 +R_A(E-\omega_L)L_A(\phi_L)R_A(E).
\]
In particular the shift is **minus** \(\omega_L\). Applying this twice gives
\[
\begin{split}
\langle\widetilde a_LR_C\gamma_vR_A\rangle={}&
\phi_L(v)\langle R_C^-R_A\rangle
+\langle R_C^-L_CR_C\gamma_vR_A\rangle\\
&-\langle R_C^-\gamma_vR_A^-L_AR_A\rangle,
\end{split}
\]
where \(R_A^-=R_A(E_0-\omega_L)\). All expectations are in the original vacuum.

As \(k_L\) approaches the node, \(\omega_L\to0\). Each shift changes an inverse by at most \(\omega_L/\delta^2\). The right side contains only bounded inverses and local insertions, whose vacuum matrix elements converge by the parent's inverse-filter and local-cocycle argument, now with at most three inverses. The extra Fourier factor has modulus one and converges pointwise, so the integrable filter gives dominated convergence. The left side is independently identified by the smooth thermodynamic coefficient symbol.

The resulting identity is linear in the limiting spinor. Opposite rays supply complementary band subspaces, so it extends to the full cell space, including the real vector \(e_0\). This is not an assertion that a generalized Hermitian zero mode annihilates the vacuum. Spatial cutoff vectors \(q_R\) need not satisfy \(\|Kq_R\|\to0\), and are not used.

Let \(q_j\) denote one on \(2\mathbb Z^3\) and zero elsewhere solely as a coefficient label. Define \(J_A=2L_A(q)\). For \(B_A=(i/2)\gamma_v\gamma(d_A)\), this is the bounded local operator \(J_A=i\gamma(d_A)\), with
\(\|J_A\|=\beta=2\sqrt2h\). The exact scalar formula is
\[
\alpha=\frac18\sum_{A,C}\left\langle
R_CR_A+\frac12R_CJ_CR_C\gamma_vR_A
-\frac12R_C\gamma_vR_AJ_AR_A\right\rangle. \tag{1}
\]
The factors one-half arise from annihilator anticommutators \(\phi=q\), rather than \(2q\). Every operator in (1) is bounded in the infinite GNS representation.

## 4. Infinite two-link impurity gap

This proof compares full-active vacuum energies, with normalization \(E_0=-\operatorname{Tr}|iK|/4\). No further spectator or parity division is made.

Orient the signed sum \(u\) of the two neighboring basis vectors so \(K_{vu}=-\sqrt2h\). The defect is \(\Delta K=2\sqrt2h(vu^T-uv^T)\). Set
\[
A_L(s)=\langle v,(s^2-K^2)^{-1}v\rangle,\quad
D_L(s)=A_L(s)-G_{2,L}(s),\quad s^2A_L+6h^2D_L=1,
\]
where \(G_2\) is the same-axis two-step Green entry. On \((v,u)\), the resolvent \((s-K)^{-1}\) has matrix
\[
\begin{pmatrix}sA_L&-\sqrt2hD_L\\\sqrt2hD_L&sB_L\end{pmatrix},
\qquad B_L=A_L\ \text{(perpendicular)},\quad B_L=D_L\ \text{(opposite)}.
\]
Different cell parities eliminate the perpendicular cross entry; the signed opposite pair subtracts \(G_2\). The determinant lemma yields, with \(z=s^2A_L\),
\[
\begin{split}
d_{F,L}(s)&=\frac{\det(s-K_F)}{\det(s-K)}
=(1-4h^2D_L)^2+8h^2s^2A_LB_L,\\
d_O&=1-\frac89(1-z)^2,\qquad
d_P=\frac{(1+2z)^2}{9}+8h^2s^2A_L^2. \tag{2}
\end{split}
\]
Both ratios are at least \(1/9\). Since \(\det(s-K)=\prod_{\omega_j>0}(s^2+\omega_j^2)\), the elementary logarithmic integral gives exactly
\[
\Delta E_{F,L}=-\frac1{2\pi}\int_0^\infty\log d_{F,L}(s)\,ds. \tag{3}
\]

The infinite Green entry is
\(A(s)=\mathbb E_k[s^2+4h^2\sum_a\sin^2 k_a]^{-1}\). Folding \(2k\) and using sign symmetry gives
\[
6h^2A(0)=\sum_{n\ge0}p_{2n},\qquad
p_{2n}=6^{-2n}\sum_{a+b+c=n}\frac{(2n)!}{a!^2b!^2c!^2}.
\]
For \(\phi=(\cos x+\cos y+\cos z)/3\), split positive and negative \(\phi\), translate the latter, and use \(1-\phi\ge2|x|^2/(3\pi^2)\) on \([-\pi,\pi]^3\). Extending the Gaussian integral gives
\(p_{2n}\le3\sqrt3\pi^{3/2}/(32n^{3/2})<n^{-3/2}\).
The exact partial sum through 100 is less than \(3/2\), and the remaining integral tail is at most \(1/5\). Thus
\[
A(0)\le\frac{17}{60h^2}. \tag{4}
\]
For \(X=4h^2\sum\sin^2k_a\), \(\mathbb EX=6h^2\) and \(\mathbb EX^2=42h^4\). Cauchy-Schwarz yields
\[
1-z=\mathbb E\frac X{s^2+X}\ge\frac{6h^2}{s^2+7h^2}. \tag{5}
\]
For opposite pairs put \(g=(8/9)(1-z)^2\ge32h^4/(s^2+7h^2)^2\). Retaining two positive logarithmic terms, \(-\log(1-g)\ge g+g^2/2\), gives
\[
\frac{\Delta E_O}{h}\ge\frac1{\sqrt7}\left(\frac47+\frac{40}{343}\right)
>\frac38\left(\frac47+\frac{40}{343}\right)=\frac{177}{686}>\frac14.
\]
The integrals are \(\int_0^\infty(s^2+a^2)^{-2}ds=\pi/(4a^3)\) and \(\int_0^\infty(s^2+a^2)^{-4}ds=5\pi/(32a^7)\), from \(s=a\tan\theta\) and the cosine-power recursion. The energy prefactor remains \(1/(2\pi)\); \(\sqrt7<8/3\) supplies the rational bound.

For perpendicular pairs write \(u=s^2/h^2\). Monotonicity in \(A\) and (5) give
\(d_P\le1-(24-8/u)/(u+7)^2\le1\) when \(u\ge1/3\).
For smaller \(u\), (4) gives \(d_P(hy)\le P(y)\), where
\[
P(y)=\frac19+\left(\frac{4a}{9}+8a^2\right)y^2+\frac{4a^2}{9}y^4,
\qquad a=\frac{17}{60}.
\]
This increasing polynomial satisfies \(P(1)<1\), proving \(d_P\le1\) on the remaining range too. Therefore omitting \(s>h\) cannot discard a negative contribution. With \(w=1-P\), the exact rational integral obeys
\[
\frac{\Delta E_P}{h}\ge\frac7{44}\sum_{n=1}^{12}\frac1n\int_0^1w(y)^n\,dy
>\frac16. \tag{6}
\]
Here \(1/(2\pi)>7/44\); the rational comparison is computed directly, not fitted to a physical spectrum.

Retaining the previously omitted positive tail strengthens (6). In units \(h=1\), for \(s\ge1\),
\[
-\log d_P(s)\ge1-d_P(s)\ge\frac{24-8/s^2}{(s^2+7)^2}\ge0.
\]
For \(a_j=j/16\), \(b_j=(j+1)/16\), \(j=16,\ldots,319\), a lower rectangle on \([a_j,b_j]\) uses the increasing numerator at \(a_j\) and denominator at \(b_j\). Thus the contribution over \([1,20]\) is at least
\[
c_{\rm tail}=\frac7{44}\sum_{j=16}^{319}\frac1{16}
\frac{24-8/a_j^2}{(b_j^2+7)^2}.
\]
Adding this exact rational number to the right side of (6) gives more than \(1/4\). No monotonicity of their ratio is assumed. The omitted contribution beyond 20 is nonnegative. Therefore \(\Delta E_P>h/4\) as well. The earlier \(h/6\) proof and source are preserved in the packet; this improvement uses the same Green-function bound and adds positive contributions.

For every \(s>0\), AP Riemann sums give \(A_L(s)\to A(s)\). The parent's shifted-grid inverse-square bound controls \(A_L(0)\) uniformly; together with \(d_{F,L}\ge1/9\) it bounds the logarithms near zero. The unchanged \(\operatorname{Tr}K^2\), or direct expansion of (2), gives a uniform \(O(s^{-4})\) logarithmic tail. Dominated convergence identifies the limit of (3). Finite inequalities \(H_L+B_A-E_{0,L}\ge\Delta E_{A,L}\) then pass on local polynomial vectors to the infinite GNS quadratic form. The parent's local core and bounded perturbation extend this to \(D_A\ge h/4\). No impurity ground vector, Bogoliubov implementability, or explicit finite-size threshold is needed.

## 5. Laplace target and explicit tail

Define \(E_A(s)=e^{-sD_A}\) and the bounded insertion
\[
Z_A(s)=-\int_0^sE_A(s-r)J_AE_A(r)\,dr.
\]
Expanding the negative inverses in (1) gives
\[
\alpha=\frac18\sum_{A,C}\int_0^\infty\!dt\int_0^\infty\!ds\,
\left\langle E_C(t)E_A(s)+\frac12Z_C(t)\gamma_vE_A(s)
-\frac12E_C(t)\gamma_vZ_A(s)\right\rangle. \tag{7}
\]
The minus sign in \(Z_A\) is essential. For \(\delta=h/4\), the absolute integrand is at most
\(e^{-\delta(t+s)}[1+\beta(t+s)/2]\). Consequently the complete 90-term error outside \([0,T]^2\) is at most
\[
\frac{90}{8}e^{-\delta T}
\left(\frac2{\delta^2}+\frac{\beta T}{\delta^2}+\frac{2\beta}{\delta^3}\right). \tag{8}
\]
Using \(\beta<3h\), the fixed choice \(T=100/h\) makes (8) less than \(10^{-6}/h^2\). The supporting runner verifies this with an exact rational lower Taylor bound on the exponential. This is a tail certificate, not a pointwise Gaussian arithmetic, quadrature, or finite-box certificate.

## 6. Evidence and remaining obligation

The portable runner checks the little-group algebra, exact ordered-pair orbit census, a rational shifted-resolvent fixture including an omitted-shift adverse comparison, the return/logarithm inequalities, and the improved tail. These finite checks support sensitive steps; they do not prove the all-size analytic limits by enumeration. Original derivations, independent reviews, gauge correction, and earlier conservative tail are retained in the dated packet. No physical kernel pilot or numerical value is included in this theorem.

The remaining target is the signed native scalar \(\alpha\). Formula (7) gives a bounded route to it, but rigorous pointwise evaluation, spatial approximation, and integration error remain separate obligations. In particular the theorem neither deletes nonlinear star terms nor identifies the full sixth-order spectator coefficient or an interacting bulk phase.
