---
claim_id: native_local_natural_ring_dynamics_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied full native H=UD+g sum lambda_e A_e on even cubic tori: finite-order local unitary reduction and uniform-in-volume O(epsilon^2) expectation error at fixed natural fourth-order ring time, for dressed ice states and consistently dressed local observables. Explicit recursive small-coupling constants; no bare-ice preparation, global isolated band, phase or physical selection."
upstream_dependencies:
  - native_virtual_pair_ring_mechanism_note_2026-09-08
runner: scripts/native_local_natural_ring_dynamics_2026_09_08.py
---

# Native ring dynamics on its natural timescale

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

For the supplied full native Hamiltonian, a finite local unitary transformation gives a controlled fourth-order ring approximation for any fixed number of ring-time units. The expectation error is $O(\epsilon^2)$, uniformly in lattice volume, when the initial ice state and the measured local observable are dressed consistently. The constants and sufficient coupling regime below are explicit but deliberately conservative. This supplies no preparation mechanism, phase conclusion or physical coupling selection.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Uniform local dynamical estimate under the supplied Hamiltonian and dressed preparation."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Model and theorem

Use the [full-carrier mechanism](NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md), the [native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), and its [instrument algebra](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). These are provisional mathematical dependencies. Work on finite periodic cubic graphs with every extent even and at least four, full edge-qubit carrier, relaxed magnetic-cycle constraint and no fixed winding sector. Define

\[
x_e=(1-Z_e)/2,\qquad Q_v=(-1)^{v_1+v_2+v_3}\left(\sum_{e\ni v}x_e-3\right),
\qquad D=\sum_v Q_v^2,
\]

\[
H=UD+g\sum_e\lambda_e A_e,\qquad U>0,\quad
\lambda_* =\sup_e|\lambda_e|,\quad z=\frac{g\lambda_*}{U},\quad
\epsilon=|z|,\quad b_e=\lambda_e/\lambda_*.
\]

The case $g\lambda_*=0$ is exact and needs no ring-time rescaling. Otherwise write $H/U=D+zV$, $V=\sum_e b_eA_e$. Neither the penalty, perturbation, couplings nor preparations are selected by the axioms. This is not a substitution of $A_e$ for the original number-preserving $T$ without declaring it.

There are volume-independent constants $\rho>0$ and $C_X,B,B'>0$, constructed below, and an exact finite-volume unitary $Y_{14}$, such that for $0<\epsilon\le\rho/2$, every density matrix $\varrho=P\varrho P$ on the complete ice space $P=1_{D=0}$, and every observable $O_X$ supported on a fixed finite set $X$,

\[
\begin{aligned}
&\left|\operatorname{Tr}\!\left[Y_{14}^{\dagger}\varrho Y_{14}\,
 e^{itH}Y_{14}^{\dagger}O_XY_{14}e^{-itH}\right]
-\operatorname{Tr}\!\left[\varrho e^{i\tau J_4}O_Xe^{-i\tau J_4}\right]\right|\\
&\hspace{1cm}\le C_X\|O_X\|\epsilon^2 |\tau|
\left[(1+B|\tau|)^3+(1+B'|\tau|)^3\right],
\qquad t=\frac{\tau}{U\epsilon^4}.
\end{aligned}
\]

Constants may depend on the fixed support, geometry and the explicit majorants; they do not depend on volume, $U,\epsilon,t$, or the ice density matrix. The dimensionless ring extension is

\[
J_4=\sum_{C\text{ unoriented simple four-cycle}}
\frac{\eta_C\prod_{e\in C}b_e}{2}F_CS_C,
\qquad \eta_C=\prod_{a=0}^3\operatorname{sign}(v_{a+1}-v_a).
\]

Each cycle is counted once, $F_C$ enforces alternation and $S_C$ is the native cycle operator in the parent convention. Straight winding four-cycles at extent four are included. The theorem is an expectation statement for dressed ice preparation, not a global operator-norm approximation to the ring Hamiltonian on arbitrary charge states.

## Local harmonics and strong support

Native $A_e$ has $X$ only on its edge and $Z$ factors on other edges of the two endpoint stars. For $e=(i,j)$, let $r_i,r_j$ count the other five occupied edges at each endpoint. On an input bit $x=x_e$, direct subtraction gives

\[
\Delta_eD=2(1-2x)(r_i+r_j-5).
\]

Let $P_{e,m}$ be the spectral projector of the diagonal operator $M_e=(1-2x_e)(r_i+r_j-5)$. With the projector on the input column,

\[
A_{e,m}=A_eP_{e,m},\quad [D,A_{e,m}]=2mA_{e,m},\quad
A_{e,m}^{\dagger}=A_{e,-m},\quad m=-5,\ldots,5.
\]

Their sum is $A_e$, each has norm at most one, and only $m=1$ acts on ice. The $m=0$ component is nonzero on excited states: it cannot be dropped when bounding the propagation speed of the whole effective Hamiltonian. Signed neutrality gives integer even $D$, although integer spectrum alone suffices below.

Use physical edges as tensor sites, adjacent if they meet at a vertex. Assign $A_e$ the full union $S_e$ of its endpoint stars, size eleven. An operator on $S$ is **strongly supported** when it commutes with every charge-star term whose support is not contained in $S$. $A_e$ has this property because it commutes with all charge stars except its two endpoints. Charge averaging preserves strong support. Commutators are strongly supported on unions and vanish for disjoint supports. In particular $[B_S,D]$ is supported on $S$, without a new support enlargement. Products with the diagonal charge projectors used in the harmonic decomposition also preserve this property.

These facts follow from the commuting diagonal charge stars, not an assumption that they are onsite. Supports from nested nonzero commutators remain connected. A physical edge belongs to at most eleven endpoint-star unions. For a specified interaction decomposition define

\[
\|\Phi\|_\kappa=\sup_i\sum_{S\ni i}e^{\kappa|S|}\|\Phi_S\|.
\]

Then $\|D\|_0\le18$, since each edge meets two charge stars of norm at most nine, and $\|V\|_0\le11$. No volume factor appears. For maximum support sizes $b,c$, assigning commutators to unions gives

\[
\|[B,C]\|_\kappa\le2(b+c)\|B\|_\kappa\|C\|_\kappa.
\]

For a fixed marked site, split overlapping support pairs according to which support contains it, and sum the partner through an intersection site. This costs at most $b+c$; the operator commutator costs two and the exponential weights multiply. The norm refers to this constructed potential, not to a unique decomposition of an operator.

## Fourteen finite homological steps

For a strongly supported term define

\[
\mathcal A(B)=\frac1{2\pi}\int_0^{2\pi}e^{itD}Be^{-itD}\,dt,
\qquad
\Gamma(B)=\frac1{2\pi}\int_0^{2\pi}i(t-\pi)e^{itD}Be^{-itD}\,dt.
\]

For nonzero integer energy difference $m$, $\Gamma$ multiplies the matrix element by $1/m$. Thus

\[
[\Gamma(B),D]=-(B-\mathcal A(B)),\quad
\|\mathcal A(B)\|\le\|B\|,\quad
\|\Gamma(B)\|\le(\pi/2)\|B\|<4\|B\|.
\]

Both maps preserve each assigned strong support, and $\Gamma(B)$ is anti-Hermitian for Hermitian $B$. Construct

\[
S(z)=\sum_{j=1}^{14}z^jS_j,\qquad
F_n=[z^n]e^{\operatorname{ad}(\sum_{j<n}z^jS_j)}(D+zV),
\quad S_n=\Gamma(F_n),\quad K_n=\mathcal A(F_n).
\]

Adding $S_n$ changes the coefficient at order $n$ to $F_n+[S_n,D]=K_n$, leaving lower orders unchanged. Every assigned $K_n$ term commutes with $D$. All coefficient supports have size at most $11n$: the innermost commutator with $D$ does not enlarge strong support and all other supports add. For real $z$, $Y_{14}=e^{S(z)}$ is an actual unitary.

An explicit finite rational recursion bounds these coefficients. Put $s_n=4f_n$. For an ordered positive composition $(i_1,\ldots,i_l)$, put $p_j=i_1+\cdots+i_j$. Define, for $n=1,\ldots,14$,

\[
\begin{aligned}
f_n={}&\sum_{\substack{l\ge2\\i_1+\cdots+i_l=n}}
\frac{2f_{i_1}}{l!}\prod_{j=2}^l(22p_js_{i_j})\\
&+11\sum_{\substack{l\ge0\\i_1+\cdots+i_l=n-1}}
\frac1{l!}\prod_{j=1}^l(22(1+p_j)s_{i_j}).
\end{aligned}
\]

The empty second composition contributes eleven only for $n=1$; all other indices are less than $n$. The first factor uses the exact identity $[S_i,D]=-(F_i-\mathcal A(F_i))$, bounded by $2f_i$, rather than commuting against all of $D$. The remaining factors use the support-size bound above. Induction proves $\|F_n\|_0\le f_n$, $\|S_n\|_0\le s_n$. This is a finite recursion, not an assumed convergent infinite perturbation series.

Let

\[
m=154,\quad \kappa=1/154,\quad s=\sum_{j=1}^{14}s_j,\quad
\rho=\min\left(1,\frac1{24m\max(1,s)}\right),\quad M=174.
\]

For complex $|z|\le\rho$,

\[
\|S(z)\|_\kappa\le3|z|s\le\frac1{8m}.
\]

Here $e^{11j\kappa}<3$. For a potential $B$ of maximum support $b$, repeated commutators obey

\[
\frac{\|\operatorname{ad}_S^l B\|_\kappa}{l!}
\le\|B\|_\kappa(2m\|S\|_\kappa)^l
\frac{\prod_{j=1}^l(j+b/m)}{l!}.
\]

The sum is $(1-2m\|S\|_\kappa)^{-1-b/m}<2$ for $b=6,11$. Since $\|D\|_\kappa\le54$, $\|V\|_\kappa\le33$, the exact Lie potential is analytic in this disk and bounded by $M=2(54+33)$. It agrees with finite-volume unitary conjugation for real $z$. Cauchy's estimate and the geometric tail now give an exact decomposition for $\epsilon\le\rho/2$:

\[
Y_{14}HY_{14}^{\dagger}=UD+K+R,\qquad
K=U\sum_{j=1}^{14}z^jK_j,\qquad [K,D]=0,
\]

\[
\|R\|_\kappa\le\frac{2M}{\rho^{15}}U\epsilon^{15},\qquad
\|K\|_\kappa\le\frac{2M}{\rho}U\epsilon.
\]

All coefficients and constants are independent of volume. The sufficient regime is deliberately very small. The complex disk is an analytic device, not a physical nonunitary dynamics. This construction needs neither an optimal prethermal theorem nor a volume-uniform isolated ice band.

## Ice restriction and a slow local comparison Hamiltonian

Global bit parity $\prod_e Z_e$ commutes with $D$ and negates $V$. Averaging and the homological inverse respect this grading, so $K_j$ has parity $(-1)^j$. All ice strings have exactly $3N/2$ occupied edges, making bit parity scalar on $P$. Hence $PK_jP=0$ for every odd $j$. The second coefficient is the scalar $-\sum_e b_e^2/2$ on ice.

The fourth coefficient is the parent's canonical fourth coefficient, not an unidentified fourth-order gauge. At each fixed finite volume, compare the formal block diagonalization with canonical direct rotation for its ice projection. A further correction beginning beyond the retained order gives an exact local-in-parameter block map in a sufficiently small spectral neighborhood. The two ice effective Hamiltonians differ by a near-identity unitary within $P$; since all lower coefficients are zero or scalar, that unitary cannot change the fourth coefficient. This temporary coefficient-identification neighborhood may shrink with volume. It is not the norm regime used above and supplies no uniform global band. The argument does not identify a sixth-order diagonal in this different gauge.

Therefore

\[
K|_P=U z^2 c_2 I_P+U z^4 c_4 I_P+
\left(Uz^4J_4+U\sum_{j=6}^{14}z^jK_j\right)\bigg|_P.
\]

Define on the full carrier the local operator

\[
L=Uz^4J_4+U\sum_{j=6}^{14}z^jK_j.
\]

No compression map is necessary. Every retained term commutes with $D$, and each alternating ring preserves all $Q_v$. Thus $L$ preserves ice, and the evolved density matrices of an ice-supported initial state under $UD+K$ and under $L$ are identical: their restrictions differ only by scalar phases. This remains true for an observable that does not commute with $D$. Equality outside ice is not claimed.

A bound $\|J_4\|_\kappa\le84$ suffices: a four-cycle uses at most forty-four assigned edge sites, each edge belongs to at most fifty-five such supports, and each coefficient has magnitude at most $1/2$. This includes the possible straight winding four-cycles. Consequently

\[
\|L-Uz^4J_4\|_\kappa\le C_6U\epsilon^6,\qquad
\|L\|_\kappa\le(84+C_6)U\epsilon^4,\qquad C_6=2M/\rho^6,
\]

using $\epsilon\le1$. The full $K$ has a fast $O(U\epsilon)$ interaction norm; the ice-equivalent $L$ has a slow $O(U\epsilon^4)$ norm. Dropping the fast terms is justified only after the ice-state restriction.

## Local dynamics, two light cones, and dressing

Here is the locality estimate used in both comparisons. For the edge-adjacency metric use

\[
F(r)=\frac{e^{-r/616}}{(1+r)^4},\qquad C_F=9216,
\qquad C_0=(2464/3)^4.
\]

Connected support diameter is at most cardinality, and $(1+a)^4e^{-3a/616}\le(2464/3)^4$. Thus a potential's interaction $F$-norm is bounded by $C_0\|\Phi\|_\kappa$. A line-graph sphere of radius $r\ge1$ is covered by edges at cubic distance $r-1$ from either endpoint of its central edge; cubic shells have at most $4r^2+2$ sites. This gives the conservative uniform shell bound $72(r+1)^2$, also on periodic shortest-distance shells. Hence $\sup_x\sum_y(1+d(x,y))^{-4}\le288$. Splitting an intermediate vertex according to which of its distances is at least half the total proves

\[
\sum_w F(d(x,w))F(d(w,y))\le C_F F(d(x,y)).
\]

The iterated commutator/Duhamel expansion, with its time-simplex factorials, sums these convolution chains to an exponential light cone with time exponent $2C_FC_0\|\Phi\|_\kappa|t|$. Cap the commutator by twice the product of operator norms. Summing supports inside the cone and exponentially decaying shells outside gives, for fixed local $O_X$,

\[
\sum_S\|[R_S,\alpha_t^{\Phi}(O_X)]\|
\le C_X\|O_X\|\|R\|_\kappa(1+v|t|)^3,
\qquad v=1232C_FC_0\|\Phi\|_\kappa.
\]

The inequality $\min(1,\sum_{i\in S}a_i)\le\sum_{i\in S}\min(1,a_i)$ allows anchoring each term at a site and using the local norm; there is no volume factor. Fixed support and shell constants are absorbed in $C_X$. Time-dependent remainder terms obey the same estimate if their assigned supports and norms are unchanged. This is the usual local commutator proof, not a new general Lieb–Robinson theorem.

For the first comparison, remove $UD$ in the interaction picture. Each $K_j$ term commutes with $D$, and each strongly supported remainder term stays on its support under $e^{itUD}$, with unchanged norm. A generic local observable's free-$D$ rotation enlarges its support only by the charge stars meeting its original support: all stars commute, so the enlargement occurs once, not at a speed proportional to $U$. Duhamel and the fast $K$ cone therefore give

\[
\text{error}_1\le A_X\|O_X\|U\epsilon^{15}|t|
(1+B U\epsilon|t|)^3.
\]

This bound is valid for arbitrary states. For an initial ice state, replace $UD+K$ by $L$ exactly in expectations. Comparing $L$ with $Uz^4J_4$ then uses the slow cone and the order-six difference:

\[
\text{error}_2\le A'_X\|O_X\|U\epsilon^6|t|
(1+B'U\epsilon^4|t|)^3.
\]

For $t=\tau/(U\epsilon^4)$, $\epsilon\le1$, the first power is $\epsilon^{15-4-9}=\epsilon^2$, and the second is $\epsilon^{6-4}=\epsilon^2$. This proves the theorem. The original order-five estimate would instead give $\epsilon^{6-4-9}=\epsilon^{-7}$; it did not justify a natural ring period. Thirteen elimination steps suffice for a vanishing $O(\epsilon)$ first error, while fourteen give the stated $O(\epsilon^2)$.

Laboratory states and observables must be transformed consistently. Local dressing satisfies $\|Y_{14}O_XY_{14}^{\dagger}-O_X\|\le C'_X\epsilon\|O_X\|$ by the same convergent commutator series. The transformed observable has a summable quasi-local tail, allowing the estimates at a slightly smaller positive weight. Thus a bare local observable has an additional $O(\epsilon)$ dressing error. A bare ice initial state cannot simply be substituted globally for its dressed preparation: local dressing does not bound an extensive state's norm difference or the probability of any defect anywhere.

## Evidence and scientific boundary

The live standard-library controls include an actual sixteen-state native four-cycle with fourteen exact Fraction elimination steps, all energy blocks and its nontrivial two-dimensional ice block. They compare the fourth coefficient with a separate folded-resolvent calculation, check the slow-extension restriction and retain a nonzero fast excited-sector term. Separate controls enumerate all 2,048 endpoint-star bitstrings and L4/L6 support geometry, and evaluate the finite fourteen-step constants and time exponents exactly. These are finite controls of the stated construction, not numerical evidence for a phase or a many-body propagation theorem.

The [packet](../.claude/science/physics-loops/native-local-ring-dynamics-20260908/HANDOFF.md) preserves the original five-step bounds, sharper constants, independent thirteen/fourteen-step arguments, mutual reviews, harmonic proof and raw controls. The new fourteen-step matrix implementation is explicitly adapted from root's thirteen-step implementation; it is not called an independent implementation. Actual subprocess mutations and the isolated runtime/premise closure are recorded separately. New canonical bytes require their own independent review.

Optimal-prethermal results are contextual only: [Abanin et al.](https://arxiv.org/abs/1509.05386) and the strong-support extension in [Else et al.](https://arxiv.org/abs/1704.08703) address high-order dressed conservation. Their theorem constants and conclusions are not needed for this finite construction. The archived applicability review records its exact primary-source coverage; no third-party paper text is duplicated here. Standard finite Schrieffer–Wolff mathematics and local commutator methods are not claimed as historical novelties.

The result controls the supplied kinetic-ring model, including finite-size winding terms, at fixed rescaled time. It does not add the RK diagonal potential, identify a sixth-order coefficient in a different gauge, select a native occurrence law or physical action, prove deconfinement or photons, or establish a uniform global ice band. The Hamiltonian, dressed preparation and couplings remain explicit physical imports.
