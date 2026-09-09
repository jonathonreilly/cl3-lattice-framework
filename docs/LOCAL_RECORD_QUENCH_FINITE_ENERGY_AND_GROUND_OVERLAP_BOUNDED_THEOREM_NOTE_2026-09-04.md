---
claim_id: local_record_quench_finite_energy_and_ground_overlap_bounded_theorem_note_2026-09-04
claim_type: bounded_theorem
claim_scope: "For a supplied invertible finite bipartite free-fermion Hamiltonian, its filled negative sea, and occupation projections on one sublattice followed by incident-hop deletion: every branch has the stated reduced covariance and the same post-event mean energy; excess above its fixed-number reduced ground energy is nonnegative, vanishes exactly for a reducing deletion, and is bounded by the sum of deleted diagonal entries of sqrt(Q Q-dagger). For one deletion on cubic pi-flux tori of side 2N, N>=2, with physical boundary sign (-1)^(N-1) in each axis: scalar resolvent formulas give excess energy and excitation count; excess has a strictly positive finite thermodynamic limit in hopping units; the matching fixed-number Slater ground-state squared overlap has liminf at least 1-9pi/32. This is one supplied free-fermion quench, not a physical Record-formation mechanism or a many-event vacuum."
upstream_dependencies: []
runner: scripts/local_record_quench_energy_and_ground_overlap_2026_09_04.py
---

# Local Record quench: finite energy and a positive ground-state overlap

**Date:** 2026-09-04

**Type:** bounded_theorem

**Status:** proposed_retained

This author proposal is conditional mathematical support at the supplied-model scope below. Audit is unset; only independent audit may assign effective status.

**Primary runner:** [local_record_quench_energy_and_ground_overlap_2026_09_04.py](../scripts/local_record_quench_energy_and_ground_overlap_2026_09_04.py).

**Independent checker:** [local_record_quench_energy_and_ground_overlap_independent_check_2026_09_04.py](../scripts/local_record_quench_energy_and_ground_overlap_independent_check_2026_09_04.py).

## Question and physical boundary

A spatially finite occupation Record leaves controlled matter excitations on the free model and canonical sequence specified here: a fixed-size deletion has bounded excess energy, and a singleton has a bounded excitation count and a strictly positive lower bound on its ground-state probability as the volume grows, even when exact sea preservation fails.

The motivation is the current formation/gravity interface. Open [PR #7974](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7974), head `710701c6a90fb5a5725ac5342eae20d60a3b4705`, finds that its local star formation unit can carry the supplied gravity rate while failing exact sea preservation. Open [PR #7968](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7968), head `94e2075c02957453d1a9b5db5e08f5874b971394`, supplies the exact-invariance criterion. Its squared Slater residual is an energy variance; it is not the mean energy above the new ground state. Neither result asserts that this mean excess is extensive. This note quantifies the different questions of energy, excitation number and overlap.

All fermion modes, the Hamiltonian, initial sea, occupation/Born instrument, and immediate hopping deletion are **supplied**. The word Record refers here to the declared permanent occupation outcome; a compiler into the framework's physical edge-qubit Records is not proved. No apparatus, switching controller, rate, time rule, interaction, gravity source, or physical coupling scale is inferred from the axioms. This is the cubic free-fermion carrier, not the distinct degree-three SU(2) rishon star. No photon calculation is made.

## Machine status and inputs

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Can spatially local Record formation carry finite matter excitations without requiring exact sea preservation?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Use the bounded local quench as a candidate input for repeated formation, spatial response and apparatus/source accounting."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Self-contained conditional free-fermion theorem with an analytic canonical-volume lower bound and finite executable checks."
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/local_record_quench_energy_and_ground_overlap_independent_check_2026_09_04.py
```

The downstream consumer is the proposed repeated Record-formation model coupling matter evolution to an explicit apparatus and source; it does not yet have a claim identifier. This result supplies its one-event free-matter estimate and does not close that physical construction.

| Input | Role | Provenance | Open physical bridge |
|---|---|---|---|
| Finite fermion modes, invertible Q, negative sea | Mathematical domain | Declared here; predecessor models are compared below and reconstructed here | Physical carrier and preparation |
| Occupation/Born projection and hop deletion | Event prescription | Supplied in this note | Edge-qubit Record compiler, switch, apparatus and rate |
| Cubic hopping, coefficient and boundary signs | Specialization | Explicit definition below | Interaction and physical scale selection |
| Covariance, Slater, trace-norm and resolvent identities | Mathematical machinery | Standard identities; needed reductions proved here | No physical authority follows merely from the machinery |
| Gravity-rate/star interface | Motivation | Pinned open-PR scopes above | Source identification and repeated energy-complete dynamics |

## Finite domain and conditional covariance

The obligation graph is: polar orbitals imply (1); conditional particle counting and trace inequalities imply (2)–(6); determinant/resolvent identities imply (7)–(8); reduced polar geometry and the Slater determinant imply (9)–(12); canonical dispersion, Jensen, shell convergence and an elementary cube integral imply (13)–(17). Each mathematical step is proved here. The strongest missing physical obligation is a single implemented formation process whose repeated events preserve earlier Records and account for matter evolution, timing and total energy.

Let there be $m$ modes on each sublattice, with

\[
h=\begin{pmatrix}0&Q\\Q^\dagger&0\end{pmatrix},
\quad K=(QQ^\dagger)^{1/2}>0,\quad U=K^{-1}Q.
\]

Assume square invertible $Q$; then $U$ is unitary. Use covariance convention $C_{ij}=\langle c_j^\dagger c_i\rangle$. The initial negative sea fills the columns of

\[
F=2^{-1/2}\begin{pmatrix}I\\-U^\dagger\end{pmatrix}.
\]

In the second-sublattice basis $\widetilde b=Ub$, this is one occupied orbital $(a_i^\dagger-\widetilde b_i^\dagger)/\sqrt2$ per $i$. Measure occupations $n_i\in\{0,1\}$ on any first-sublattice coordinate subset $S$, and let $T=S^c$. Each outcome has probability $2^{-|S|}$. An occupied $a_i$ leaves its partner empty; an empty $a_i$ leaves its partner occupied. Therefore on the unmeasured $a_T,b$ carrier,

\[
C_{S,n}=\begin{pmatrix}
I_T/2&-U_T/2\\
-U_T^\dagger/2&I_b/2+U_S^\dagger D_nU_S
\end{pmatrix},\qquad D_n=\operatorname{diag}(1/2-n_i).
\tag{1}
\]

Here $U_T,U_S$ are row restrictions. This covariance is a projector of rank $m-\sum_i n_i$. The measured modes may be retained as isolated zero modes with their fixed occupations, or omitted as in (1); either convention preserves the original total particle number when the fixed Records are counted. No condition $[P_S,K]=0$ is used in (1).

Delete the measured sites' incident hopping, so the unmeasured one-particle Hamiltonian is

\[
h_R=\begin{pmatrix}0&Q_T\\Q_T^\dagger&0\end{pmatrix}.
\]

There is no evolution interval between successive measurements in this single event. The later Hamiltonian commutes with the omitted/fixed occupation Records by construction. This mathematical deletion prescription is not an autonomous physical switch.

## Energy theorem for arbitrary same-sublattice deletion

Every outcome in (1) has

\[
E_{\rm post}=\operatorname{Tr}(h_RC_{S,n})=-\operatorname{Tr}(P_TK).
\tag{2}
\]

Only the off-diagonal covariance enters the trace, and $Q_TU_T^\dagger=K_{TT}$, proving (2). Since $Q_T$ has full row rank, $h_R$ has $|T|$ positive levels, $|T|$ negative levels and $|S|$ zero levels. Its minimum at the conditional particle number $m-\sum_i n_i=|T|+|S|-\sum_i n_i$ fills all negative levels and the requisite number of zero levels. Thus

\[
E_{0,R}=-\|Q_T\|_*
=-\operatorname{Tr}\sqrt{(K^2)_{TT}},
\qquad
\Delta_S=E_{\rm post}-E_{0,R}
=\operatorname{Tr}\sqrt{(K^2)_{TT}}-\operatorname{Tr}K_{TT}.
\tag{3}
\]

The trace and square root in (3) are on $T$; an empty block has trace zero. The original energy is $E_0=-\operatorname{Tr}K$. Distinguish the **total system jump** $J_S$ from the **excess above the changed Hamiltonian's ground energy** $\Delta_S$:

\[
J_S=E_{\rm post}-E_0=\operatorname{Tr}(P_SK),
\quad G_S=E_{0,R}-E_0,
\quad J_S=G_S+\Delta_S.
\tag{4}
\]

Both $G_S$ and $\Delta_S$ are nonnegative. To prove the latter and characterize equality, write

\[
K=\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix}_{T+S}.
\]

Then $(K^2)_{TT}=A^2+BB^\dagger$. Operator monotonicity of the square root gives $\sqrt{A^2+BB^\dagger}\succeq A$. A zero trace of this positive difference forces equality; squaring gives $BB^\dagger=0$. Conversely $B=0$ gives equality. Nuclear-norm contraction under row projection gives $\|Q_T\|_*\le\|Q\|_*=\operatorname{Tr}K$. Consequently

\[
0\le\Delta_S\le J_S,\qquad
\Delta_S=0\ \Longleftrightarrow\ [P_S,K]=0.
\tag{5}
\]

For six distinct nearest neighbors of hopping magnitude $t>0$,

\[
K_{ii}\le\sqrt{(K^2)_{ii}}=\sqrt6\,t,
\quad 0\le\Delta_S\le J_S\le |S|\sqrt6\,t.
\tag{6}
\]

Thus fixed $|S|$ gives vanishing excess energy per lattice site as volume grows. This does not assert small local disturbance or negligible heating at finite event density. An apparatus-complete implementation must account for $J_S$, including the Hamiltonian change; $\Delta_S$ alone is not its work cost. Measurement energy accounting is established methodology, with apparatus-dependent conditional bookkeeping, e.g. [Mohammady and Romito](https://arxiv.org/abs/1809.09010). No thermodynamic novelty is claimed for that general distinction.

## Singleton resolvent formula

Set $S=\{i\}$, $M=K^2$, and $g(s)=\langle i|(s+M)^{-1}|i\rangle$. Jacobi's determinant identity and its logarithmic derivative give

\[
\det(s+M_{TT})=\det(s+M)g(s),\quad
\operatorname{Tr}(s+M)^{-1}-\operatorname{Tr}(s+M_{TT})^{-1}=-g'(s)/g(s).
\]

Insert these identities into $\sqrt{x}=\pi^{-1}\int_0^\infty s^{-1/2}x/(s+x)\,ds$ and subtract (4) to obtain

\[
\Delta_i={1\over\pi}\int_0^\infty\sqrt{s}
\left[-{g'(s)\over g(s)}-g(s)\right]ds.
\tag{7}
\]

Under the local spectral probability measure of $M$, let $r_s=(s+\lambda)^{-1}$. The bracket is

\[
{\operatorname{Var}(r_s)\over\mathbb E r_s}\ge0.
\tag{8}
\]

For positive finite $M$, the integrand is integrable at both endpoints. It vanishes exactly when the local spectral measure is a point mass, consistent with (5). Equation (7) is useful because it uses the undeleted local spectral measure rather than a large deleted-lattice diagonalization.

## Excitation count and squared ground-state overlap

For the singleton assume $m\ge2$ and write $K=[[A,b],[b^\dagger,d]]_{T+i}$, $B=(A^2+bb^\dagger)^{1/2}$, and $V=B^{-1}Q_T$. Then $VV^\dagger=I_T$. In this section $B$ denotes that positive square root, not the off-diagonal block used in the proof of (5).

The unique normalized remaining zero mode, on the $b$ sublattice, and its overlap with the measured partner are

\[
z={U^\dagger K^{-1}e_i\over\sqrt{\langle i|K^{-2}|i\rangle}},
\quad u=U^\dagger e_i,
\quad\beta=|\langle z,u\rangle|^2
={\langle i|K^{-1}|i\rangle^2\over\langle i|K^{-2}|i\rangle},
\quad\alpha=1-\beta\in[0,1].
\]

The positive/negative projectors and a scalar count are

\[
P_\pm={1\over2}\begin{pmatrix}I_T&\pm V\\\pm V^\dagger&V^\dagger V\end{pmatrix},
\qquad\mathcal L=(m-1)-\operatorname{Tr}(B^{-1}A).
\]

Here $V^\dagger V=I-|z\rangle\langle z|$. Direct block traces of (1) give

\[
N_+=\operatorname{Tr}(P_+C_n)={\mathcal L\over2}+{(1-2n)\alpha\over4},
\quad N_h=\operatorname{Tr}[P_-(I-C_n)]={\mathcal L\over2}-{(1-2n)\alpha\over4},
\tag{9}
\]

and zero-mode occupation $1/2+(1/2-n)\beta$. $N_++N_h=\mathcal L$ excludes the zero mode. The matching fixed-number ground projector is

\[
G_n=P_-+(1-n)|0_T,z\rangle\langle0_T,z|.
\]

Its particle number equals that of $C_n$, including the occupied zero mode for $n=0$. The expected missing ground-orbital occupation and projector distance are

\[
\ell=\operatorname{Tr}[G_n(I-C_n)]={\mathcal L\over2}+{\alpha\over4},
\quad\|C_n-G_n\|_F^2=2\ell.
\tag{10}
\]

For any orthonormal occupied frame $W_n$ of $G_n$, the **squared** Slater overlap is

\[
F_n=|\langle\Omega_{0,R,n}|\Omega_{R,n}\rangle|^2
=\det(W_n^\dagger C_nW_n)\ge\max(0,1-\ell).
\tag{11}
\]

Indeed its eigenvalues are $1-x_j\in[0,1]$, with $\sum_jx_j=\ell$, and $\prod_j(1-x_j)\ge1-\sum_jx_j$. This comparison uses both ground and conditional states on the same remaining carrier and in the same particle-number sector. Dropping the required occupied zero mode would change the comparison.

For a second resolvent formula let

\[
h_2(s)=\mathbb E{\sqrt\lambda\over(s+\lambda)^2}.
\]

Writing $R=(s+M)^{-1}$, the inverse principal block is $(s+M_{TT})^{-1}=R_{TT}-R_{Ti}R_{iT}/g$. Expanding the omitted blocks of $K$ gives

\[
\operatorname{Tr}[A(s+M_{TT})^{-1}]
=\operatorname{Tr}[K(s+M)^{-1}]-h_2(s)/g(s).
\]

Integration of the inverse square root, using $\operatorname{Tr}(KM^{-1/2})=m$, yields

\[
\mathcal L=-1+{2\over\pi}\int_0^\infty {h_2(x^2)\over g(x^2)}\,dx.
\tag{12}
\]

The local covariance, energy and count formulas apply to general complex $Q$; the following thermodynamic bounds use the specified cubic model.

## Cubic sequence and thermodynamic statements

Set $t=1$ temporarily. On a cubic torus of side $L=2N$, $N\ge2$, supply real nearest-neighbor hopping signs

\[
\eta_1(x)=1,\quad\eta_2(x)=(-1)^{x_1},\quad\eta_3(x)=(-1)^{x_1+x_2},
\]

and wrap sign $w_N=(-1)^{N-1}$ in **each** axis. Equivalently the physical boundary phase is $\phi_N=\pi$ for even $N$, and $0$ for odd $N$. Each plaquette has pi flux. Anticommutation of the signed directional hoppings gives $h^2$ the scalar local spectral measure

\[
\lambda(k)=4\sum_\mu\cos^2 k_\mu,
\quad k_\mu={2\pi j_\mu+\phi_N\over2N}\ (\bmod\pi).
\]

Every sublattice coordinate has uniform weights on that momentum grid; the four parity classes within the first sublattice reproduce it with multiplicity four. Put $q_\mu=2k_\mu-\pi$. The above parity-dependent boundary phase makes $q$ the antiperiodic $N^3$ grid, and

\[
\lambda(q)=2\sum_\mu(1-\cos q_\mu),\quad
q_\mu={(2j_\mu+1)\pi\over N}\ (\bmod2\pi),\quad\mathbb E_N\lambda=6.
\tag{13}
\]

The finite one-particle gap is $2\sqrt3\sin(\pi/(2N))>0$; it tends to zero. No lower bound uniform in volume is used below.

First, the singleton excess has a **strictly positive finite limit**. With $s=x^2$, (7) has integrand $f_N(x)=(2/\pi)x^2\operatorname{Var}r/\mathbb Er$, where $r=(x^2+\lambda)^{-1}$, $0\le\lambda\le12$. For $x>0$, $x^2\operatorname{Var}r/\mathbb Er\le x^2\max r\le1$. For $x\ge1$, the range bound gives $\operatorname{Var}r\le36/x^8$, while $\mathbb Er\ge1/(x^2+12)$; hence this same ratio is at most $468/x^4$. These are volume-independent integrable majorants. Fixed-$x>0$ Riemann sums converge, so dominated convergence gives the finite limit integral. The continuum dispersion is nonconstant, making its variance integrand strictly positive for every $x>0$. No numerical extrapolation is needed for existence or positivity.

Second, put $g_{0,N}=\mathbb E_N(1/\lambda)$. Jensen's inequality gives $g(x^2)\ge1/(x^2+6)$. Substituting into (12) and integrating each spectral value gives

\[
\mathcal L+1\le{2\over\pi}\mathbb E_N\int_0^\infty
{(x^2+6)\sqrt\lambda\over(x^2+\lambda)^2}\,dx
={1\over2}+3g_{0,N},
\quad\ell\le{3\over2}g_{0,N}.
\tag{14}
\]

To justify convergence at zero frequency, represent the grid near zero as $q=(2\pi/N)a$, $a\in(\mathbb Z+1/2)^3$. On the Brillouin cube,
$\lambda(q)\ge4|q|^2/\pi^2$. The max-norm shell of half-integer radius $j+1/2$ contains at most $C(j+1)^2$ points. After the $N^{-3}$ normalization each shell contributes at most $C'/N$ to the sum of $1/\lambda$. At most $C''N\delta+1$ shells meet $|q|<\delta$, so that part is at most $C'''(\delta+1/N)$. The continuum contribution is likewise $O(\delta)$. Ordinary Riemann convergence away from zero, followed by $\delta\downarrow0$, proves

\[
g_{0,N}\longrightarrow g_{0,\infty}
={1\over(2\pi)^3}\int_{[-\pi,\pi]^3}
{d^3q\over2\sum_\mu(1-\cos q_\mu)}<\infty.
\tag{15}
\]

An elementary bound suffices. Scale $q=\pi y$ in the inverse-quadratic bound:

\[
g_{0,\infty}\le{1\over32}\int_{[-1,1]^3}{d^3y\over|y|^2}
={24\over32}\int_0^1\int_0^1{dy\,dz\over1+y^2+z^2}
\le{3\pi\over16}.
\tag{16}
\]

The equality follows from $\nabla\cdot(y/|y|^2)=1/|y|^2$ and the divergence theorem after excising a small sphere; its inner-boundary term tends to zero. Dropping $z^2$ bounds the double integral by $\pi/4$. Combining (11), (14) and (16), for **both** outcomes,

\[
\boxed{\liminf_{N\to\infty}F_{n,N}\ge1-{9\pi\over32}
=0.116427\ldots>0.}
\tag{17}
\]

Also $\limsup\ell\le9\pi/32$ and $\limsup\mathcal L\le9\pi/16-1/2$, so both $\mathcal L$ and $\ell$ remain bounded on this sequence. Equation (17) is a conservative lower bound, not an estimate of the limiting fidelity; it does not assert that the fidelity itself converges. Restoring $t>0$ multiplies energies and $\Delta$ by $t$; excitation counts and overlaps are unchanged.

## Executable evidence and review

The primary computes the initial sea by full one-particle eigendecomposition and applies sequential Gaussian conditioning before comparison with (1). It covers a nonreducing complex example, all empty/full/two-site outcome branches, positive-jump/zero-excess controls, actual cubic matrices at $L=4,6,8$, both zero-mode sectors, determinant-versus-orbital squared overlap, and scalar grids through $L=32$. Numerical tolerances are declared in its source. Quadrature errors are diagnostic estimates, not certified interval enclosures.

| Physical side | System jump $J_i/t$ | Excess $\Delta_i/t$ | Squared ground overlap, either outcome |
|---:|---:|---:|---:|
| 4 | 2.449489743 | 0 | 1 |
| 6 | 2.396829074 | 0.054323624 | 0.976412406 |
| 8 | 2.389889720 | 0.072903415 | 0.961111349 |

At $L=4$ the canonical squared dispersion is exactly flat, so a singleton reduces $K$. That cancellation is an explicit control, not a general stationarity claim. The proof of (17) is analytic; finite tables do not establish a thermodynamic limit.

The primary and checker are built in separate contexts of the **same model family**. The checker may not read or import the primary source/cache: it uses exact complex finite matrices, tiny exterior/Fock occupation projections and separate scalar/Schur calculations. Root reviewed the central mathematics independently; completed source, cache and mutation checks are recorded in the accompanying loop pack before publication. This is not independent audit status.

## Review record

For audit packet completeness, a hard landing condition is the claim-scoped helper registration
`local_record_quench_finite_energy_and_ground_overlap_bounded_theorem_note_2026-09-04 -> scripts/local_record_quench_energy_and_ground_overlap_independent_check_2026_09_04.py`
in the existing `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` mechanism. Both source files and machine caches must land with this note. The author branch does not edit the audit registry or apply a verdict.

## Prior work and what this result changes

Open [PR #7902](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7902), head `206b63213a2d181f653afccdced710c91bc714cb`, already computes branch-independent energies after logical-star/vertex conditioning on small fixtures. Open [PR #7895](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7895), head `9d045e6225def0e9b89772b4175477275fab9079`, compares conditional states with a stipulated reduced-ground-state reset. Open [PR #7971](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/7971), head `2f63762523c76b349e0daee90cc09239e38f5030`, proves complete sea/zero-mode factorization when the measured set reduces $K$. These are scope-bearing comparisons, not imported unmerged authority: equations (1)–(17) and the runners reconstruct the mathematical objects here.

The new conjunction removes the reducing-set restriction from the energy calculation, quantifies the excitation count and ground probability for a singleton, and proves finite thermodynamic bounds on the actual cubic sequence. It supplies a controlled alternative target to exact post-event sea preservation. It does not correct the previous exact-invariance theorem or claim that those notes proved extensive energetic failure.

There is still no spatial-localization theorem for the excitation cloud, no derivation of relaxation, no repeated-event stationary vacuum, no event-rate selection or renewal mechanism, and no apparatus-complete energy conservation. The finite-energy result holds at fixed hopping and lattice units, not a continuum dimensional scaling limit. Connecting an occupation projection/deletion to physical Records and connecting its energy/current to the supplied gravity source remain separate obligations. No axiom or approved primitive is amended or treated as implicitly enlarged.
