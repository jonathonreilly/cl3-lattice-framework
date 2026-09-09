---
claim_id: repeated_record_matter_and_energy_conserving_apparatus_bounded_theorem_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "For a supplied finite one-species hopping carrier of M sites and degree at most six with sharp total particle number N0, uniform live-site selection and history-preserving dwell, repeated energy-conserving occupation-Record events with one shared positive continuous battery have exact ensemble energy survival and hypergeometric live-particle count laws, independently of packet coherence width. Energy variance after K events is at most its initial value plus 6t^2 K. From a half-filled regular bipartite degree-six negative sea, live filling and negative energy density concentrate at fixed deletion fraction below one. A symmetric compact packet of width t can be prepared with mean battery energy 6tM+t/2. Alternatively a broader sine packet of mean Mt(6+3pi/sqrt(epsilon)) approximates the complete ideal history instrument within half-diamond epsilon. For an initial full nonbattery state commuting with H0, prepared independently of a packet on the declared zero-refusal support, all complete Record-history probabilities and conditional final energy distributions agree exactly with the ideal instrument. Old Records and total number are preserved exactly, and cap refusal is zero on reachable states. The carrier, scheduler, spectral gates, resource preparation and readout are supplied."
upstream_dependencies: []
runner: scripts/repeated_record_matter_energy_apparatus_2026_09_05.py
---

# Repeated Record matter with one energy-conserving battery

**Date:** 2026-09-05

**Type:** bounded_theorem

**Status:** proposed_retained

This is an author proposal for conditional mathematical support. Independent
audit remains required to assign effective status.

**Primary runner:** [repeated_record_matter_energy_apparatus_2026_09_05.py](../scripts/repeated_record_matter_energy_apparatus_2026_09_05.py).

**Independent checker:** [repeated_record_matter_energy_apparatus_independent_check_2026_09_05.py](../scripts/repeated_record_matter_energy_apparatus_independent_check_2026_09_05.py).

## Target and physical meaning

We prove that the specified implemented occupation-Record process preserves
exact bulk particle and energy laws, with fluctuations controlled over a finite
deletion fraction, while one supplied battery accounts exactly for energy.
For a stationary full nonbattery input prepared independently of a packet
on the declared zero-refusal support, complete Record-history and energy
statistics coincide exactly with the ideal process. A separately stated
broader packet approximates the entire ideal history state for general inputs.

The construction connects three objects on the same carrier: the state after
earlier Records, its subsequent matter evolution, and the apparatus that pays
for the next event. It removes a fresh-ground-state reset, an unaccounted
ideal switch, and a separately prepared battery for every event from this
finite-history model. The bulk-statistics theorem also removes the requirement
to approximate the ideal instantaneous measurement accurately at every event.

The physical Hamiltonian and fermion carrier, occupation-to-edge-qubit Record
compiler, spatial implementation of the spectral gate, event clock, coherent
resource preparation, blank control cells and readout interpretation remain
supplied or open. The result establishes specified particle-count and energy
distributions; transport, quasiparticle survival, autonomous formation and a
stationary matter background require further work.

Open PR #7978, pinned at
c2555295e9f0211d7e04d7229d72e741c1c1f9ad, motivates the question through its
one-event energy and overlap calculation. No result from that unmerged note
is required below. All mathematical reductions used here are reconstructed.

## Machine status and inputs

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Repeated local Record formation sustaining a viable matter background with consistent energy accounting."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Seek a local implementation and a renewal or stationary mechanism for the connected matter-Record process."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Finite-history construction with explicit supplied dynamics, resource preparation and analytic error bounds."
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/repeated_record_matter_energy_apparatus_independent_check_2026_09_05.py
~~~

The downstream consumer is a physical repeated-formation model on the framework
carrier. This note supplies a finite-history energy and matter construction for
that consumer; it makes no framework-wide promotion.

| Input | Role | Provenance | Open physical bridge |
|---|---|---|---|
| Finite one-species fermion modes and hopping Hamiltonian | Matter domain | Supplied explicitly below | Physical carrier and Hamiltonian selection |
| Occupation PVM, probability rule and hop deletion | Ideal Record event | Supplied definition below | Edge-qubit Record compiler |
| Live-site schedule and dwell | Repeated-event control | Declared protocol | Autonomous clock and local controller |
| Positive continuous battery and coherent sine state | Energy and coherence resource | Explicit construction below | Physical preparation and local coupling |
| Blank history/readout cells with degenerate energies | Record and control capacity | Declared apparatus | Physical memory and its preparation |
| Energy-translation lift and sine/coherence estimates | Mathematical machinery | Prior literature credited below; required bounds proved here | No independent physical premise supplied by mathematical precedent |

The obligation graph is: conditional projection gives the single-event ledger;
the bounded history Hamiltonian and energy-translation composition give safe
shared-battery support; uniform-site fiber identities give the implemented
energy and particle means, exact count distribution and variance bound. These
imply the finite-density concentration statement. Separately, the sine Fourier
second moment controls the full ideal-history approximation and its bounded
ground-excess diagnostic. The
strongest open physical obligation is an autonomous local implementation with
matter renewal, using resources represented on the framework carrier.

## Finite matter domain and repeated occupation events

Let $M\ge2$ sites carry one species of fermions, with CAR generators $c_i$.
Let $h$ be a Hermitian one-particle hopping matrix with zero diagonal, maximum
graph degree six and $|h_{ij}|\le t$, where $t>0$. The energy/operator
identities hold on full Fock space. The scalar $N_0$
in (8), the single hypergeometric law (30), and its count-concentration
statements assume a sharp fixed total number $N_0$. A mixture of number
sectors instead gives the corresponding mixture of count laws.

A history records occupations $n_r\in\{0,1\}$ on a set $R$. Keep the original
$M$ modes, isolate every recorded site, and define

\[
H_R=d\Gamma(h_R)=\sum_{i,j\notin R}h_{ij}c_i^\dagger c_j,\qquad
N_{\rm live,R}=\sum_{i\notin R}c_i^\dagger c_i.
\tag{1}
\]

Thus each prior $n_r$ is sharp and commutes with every later history Hamiltonian.
Total particle number includes the archived occupations:
$N_0=N_{\rm live,R}+\sum_{r\in R}n_r$.
Equation (1) uses the same Fock normal ordering and empty-vacuum energy zero
in every history. No history-dependent scalar ground-energy subtraction is
made in the total-energy ledger. Physical selection of that Hamiltonian,
including its energy offsets, belongs to the supplied-model input.

For a live site $i$, let $P_n$ be the occupation projector at $i$ and let $V_i$
contain its incident hopping. The next Hamiltonian is

\[
H'=H_R-V_i,\qquad [H',P_n]=0.
\tag{2}
\]

The ideal event is the unconditioned classical-outcome instrument

\[
\mathcal I_i(\rho)=\sum_{n=0}^1
|R+i,n\rangle\langle R+i,n|\otimes P_n\rho P_n.
\tag{3}
\]

Its coherent append isometry is $W_i=\sum_n|R+i,n\rangle P_n$, with output
Hamiltonian $H_{\rm out}=\bigoplus_nH'$. Outcome readout of this isometry gives
(3). Probabilities are $p_n=\operatorname{Tr}(\rho P_n)$; a branch with $p_n=0$
is omitted. Deterministic $p_n=1$ events are included.

Between events, evolve the actual current state under $H_R$. A dwell time may
depend on the past history. For the ensemble laws below, choose the next site
uniformly among the live sites after that dwell, with the dwell prescription
independent of that next choice. The state is never replaced by a new ground
state. Sites, total number and Hamiltonian coefficients remain those in (1).

## Exact repeated matter ledger

For any current state, a nonzero-probability branch has

\[
\begin{aligned}
E'_n&=\frac{\operatorname{Tr}(\rho P_nH')}{p_n},\\
J_n&=E'_n-\operatorname{Tr}(\rho H_R)
=-\operatorname{Tr}(\rho V_i)
+\frac{\operatorname{Cov}_\rho(P_n,H')}{p_n},
\end{aligned}
\tag{4}
\]

where $\operatorname{Cov}_\rho(P_n,H')=
\operatorname{Tr}(\rho P_nH')-
\operatorname{Tr}(\rho P_n)\operatorname{Tr}(\rho H')$.
It is real because $P_n$ and $H'$ commute. Averaging the outcome gives

\[
\sum_np_nJ_n=-\operatorname{Tr}(\rho V_i).
\tag{5}
\]

Equation (4) follows by inserting $H_R=H'+V_i$ and subtracting
$\operatorname{Tr}(\rho H')$. It retains the branch-selection term. Its
outcome average vanishes because $\sum_nP_n=I$. The quantity $J_n$ is a
system-energy change. The apparatus ledger is supplied separately below.

Every live bond is incident on exactly two live vertices, hence
$\sum_{i\notin R}V_i=2H_R$. With $k=|R|$ and a uniform next vertex, (5) gives

\[
\mathbb E[E_{k+1}\mid \text{current history}]
=\left(1-\frac2{M-k}\right)E_k.
\tag{6}
\]

Dwell preserves $E_k$. Starting at $R=\varnothing$, induction yields

\[
\boxed{\mathbb E E_k
=E_0\,\frac{(M-k)(M-k-1)}{M(M-1)}},
\qquad 0\le k\le M.
\tag{7}
\]

When one live site remains, its hopping energy is zero. The $k=M$ endpoint
in (7) follows directly from $H_R=0$; no division by a zero live-site count is
used.

Likewise, outcome averaging of the selected occupation gives
$\sum_np_nn=\operatorname{Tr}(\rho n_i)$. Uniform choice and
$[H_R,N_{\rm live,R}]=0$ imply

\[
\boxed{\mathbb E N_{{\rm live},k}
=N_0\frac{M-k}{M}}.
\tag{8}
\]

At $N_0=M/2$, the mean live occupation per surviving site is exactly $1/2$.
This average allows correlations between outcomes, prior Records and the
current matter state.

An alternative supplied schedule gives each live vertex an independent
constant-rate clock $\gamma$. The hybrid quantum/classical generator has
energy drift $\gamma\sum_i(-\langle V_i\rangle)=-2\gamma E$ and live-number
drift $-\gamma N_{\rm live}$. Its finite-system expectations are therefore
$E_0e^{-2\gamma s}$ and $N_0e^{-\gamma s}$ at time $s$. A state-dependent rate,
onsite energy or interaction requires its own generator calculation.

## The local energy defect

On any current history, (2) and the output projectors give

\[
D_i=H_{\rm out}W_i-W_iH_R=-W_iV_i.
\tag{9}
\]

Write the one-particle star as
$v_i=|i\rangle\langle q|+|q\rangle\langle i|$, with
$q_j=h_{ji}$ and $q_i=0$. Its eigenvalues are
$+\kappa_i,-\kappa_i$ and zero, where

\[
\kappa_i=\|q\|=\sqrt{\sum_j|h_{ij}|^2}\le\sqrt6\,t.
\tag{10}
\]

Fermionic sums of these eigenvalues are $0,\pm\kappa_i$; thus
$\|V_i\|=\kappa_i$ on full Fock space, and restriction to fixed number can
only lower the norm. In particular $\|D_i\|\le\kappa_i$.

The second defect is

\[
K_i=H_{\rm out}D_i-D_iH_R=W_i(V_i^2+[V_i,H_R]).
\tag{11}
\]

For $h'=h_R-v_i$, put $r=h'q$. Since $h'|i\rangle=0$,
$[v_i,h']=|i\rangle\langle r|-|r\rangle\langle i|$. Its two nonzero
eigenvalues are $\pm i\|r\|$. The identity
$[d\Gamma(v_i),d\Gamma(h')]=d\Gamma([v_i,h'])$ gives
$\|[V_i,H_R]\|\le\|r\|\le6t\kappa_i$. Therefore

\[
C_i:=\frac{\|K_i\|+\|D_i\|^2}{2}
\le\kappa_i^2+3t\kappa_i\le(6+3\sqrt6)t^2.
\tag{12}
\]

These estimates use the actual current graph and arbitrary current states.
They do not use a sea, a gap or a one-event preparation.

## Energy-preserving lift and its reduced-channel error

For finite input/output Hamiltonians $H_A,H_B$ and an isometry $W:A\to B$,
introduce a mathematical comparison battery $L^2(\mathbb R,dE)$ with energy
multiplication $H_{\rm bat}$. Define $T_q|E\rangle=|E+q\rangle$ and

\[
\widetilde W
=\sum_{e,f}\Pi_B(f)W\Pi_A(e)\otimes T_{e-f}.
\tag{13}
\]

The sum is over distinct eigenvalues, so degeneracies remain grouped. In the
Fourier convention $T_q\mapsto e^{i\tau q}$, its fibers are

\[
W_\tau=e^{-i\tau H_B}We^{i\tau H_A}.
\tag{14}
\]

Every fiber is an isometry. Also
$(H_B+H_{\rm bat})\widetilde W
=\widetilde W(H_A+H_{\rm bat})$ exactly. This identity includes the Hamiltonian
change as an output history block, rather than an omitted switch energy.

Prepare the real normalized sine amplitude

\[
\beta_{a,w}(E)=\sqrt{\frac2w}
\sin\!\left(\frac{\pi(E-a)}w\right)\mathbf1_{[a,a+w]}(E),
\qquad a,w>0.
\tag{15}
\]

Its mean energy is $a+w/2$ and its variance is
$w^2(1/12-1/(2\pi^2))$. Its zero extension is in $H^1(\mathbb R)$, and
$\|\beta'\|_2^2=\pi^2/w^2$. Reality makes
$p(\tau)=|\widehat\beta(\tau)|^2$ even. Thus
$\int\tau p(\tau)d\tau=0$ and $\int\tau^2p(\tau)d\tau=\pi^2/w^2$.

Tracing the battery in (13) gives the channel
$\overline\Phi=\int p(\tau)\operatorname{Ad}_{W_\tau}d\tau$. Put
$D=H_BW-WH_A$ and $K=H_BD-DH_A$. Differentiation yields
$W_\tau'=-iD_\tau$, $W_\tau''=-K_\tau$, with unchanged operator norms.
For $\Phi_\tau=\operatorname{Ad}_{W_\tau}$,

\[
\|\Phi_\tau''\|_\diamond\le2\|K\|+2\|D\|^2.
\tag{16}
\]

Indeed its three terms are $-K_\tau XW_\tau^\dagger$,
$2D_\tau XD_\tau^\dagger$, and $-W_\tau XK_\tau^\dagger$.
The completely bounded trace norm of $X\mapsto AXB^\dagger$ is at most
$\|A\|\|B\|$. Taylor's integral remainder and the zero first moment give

\[
\boxed{\frac12\|\overline\Phi-\operatorname{Ad}_W\|_\diamond
\le\frac{\|K\|+\|D\|^2}{2}\frac{\pi^2}{w^2}}.
\tag{17}
\]

The bound includes arbitrary external references. Only the second Fourier
moment is used. Outcome readout applied to both channels preserves the bound
by contractivity.

## Physical cap, refusal and the readout convention

Take the physical battery to be $L^2([0,b])$, with $b=a+w+c$ and $c>0$.
For the corresponding spectral projection $P_C$, set

\[
S=P_C\widetilde W P_C,\qquad F=(I-S^\dagger S)^{1/2}.
\tag{18}
\]

The operator $S$ intertwines capped total energies. Consequently
$S^\dagger S$ and $F$ commute with input total energy. Append disjoint
ready, success and refusal sectors, with the refusal sector carrying $H_A$.
The isometry $J$ maps a ready input to $S$ in success and $F$ in refusal.
Writing $P$ for the ready projector and extending $J$ by zero off ready,

\[
U=J+J^\dagger+I-P-JJ^\dagger
\tag{19}
\]

is a unitary involution. To verify this, use $J^\dagger J=P$,
$(JJ^\dagger)^2=JJ^\dagger$ and $PJJ^\dagger=0$: $U$ swaps the ready space
with the range of $J$ and fixes their orthogonal complement. Each term
commutes with the enlarged block total energy. For the occupation append,
old Record projectors intertwine $W$, commute with both Hamiltonians and
therefore also intertwine $S$ and $J$. The same argument applies to total
particle number. Successful new labels match the measured occupations
because $H'$ commutes with their projectors.

For completeness, the local construction has a useful margin estimate.
The bounded commutator
$\|H_{\rm bat}\widetilde W-\widetilde W H_{\rm bat}\|=\|D\|$
gives

\[
p_{\rm refusal}\le \|D\|^2(a^{-2}+c^{-2}).
\tag{20}
\]

For the lower tail, put $X=P_{(-\infty,0)}\widetilde W P_{[a,a+w]}$.
The separated energy restrictions satisfy $AX-XB=Y$, $\|Y\|\le\|D\|$,
and
$X=-\int_0^\infty e^{uA}Ye^{-uB}du$ gives $\|X\|\le\|D\|/a$.
The upper tail gives $\|D\|/c$ in the same way. Their ranges are orthogonal,
so the squared bounds add. The commutator is initially defined on the energy
domain and extends boundedly through (14).

The local *instrument* reads success versus refusal: copy this commuting
status into a fresh degenerate cell and trace or read that cell. This copy
can be extended to a unitary commuting with energy. For this explicitly
dephased status channel, replacing the outside-cap CP branch by refusal has
half-diamond distance at most (20). Both CP branches have the same effect
operator; for every input and reference their orthogonal-block difference
has half trace norm equal to the lost probability. With (17), the local
instrument error is bounded by

\[
C_i\pi^2/w^2+\kappa_i^2(a^{-2}+c^{-2}).
\tag{21}
\]

The status readout is part of this comparison. A concrete check of that
convention uses a total-energy-one vector
$\sqrt{1-p}|u,1\rangle+\sqrt p|v,-1\rangle$, where the success-system
energies of $u,v$ are $0,2$. Refusal replaces the second amplitude by
$\sqrt p|x,1\rangle$ in the old-system sector. Retaining coherent status
gives half trace distance $(p+\sqrt{4p-3p^2})/2$ from the battery-traced
bilateral output, while reading status gives $p$. This is a finite
constructed witness, not a general obstruction claim.

The shared-battery construction next uses a sector on which refusal is
exactly zero; it therefore needs no probability approximation at the caps.

## One shared battery for the complete finite history

Let $H_k$ be the direct sum of all matter Hamiltonians reachable after $k$
events, with degenerate history, control and readout registers included.
Every edge term in (1) has norm at most $t$, and there are at most $3M$
edges. Thus a common bound is

\[
\|H_k\|\le B:=3tM
\tag{22}
\]

for every step and history, including fixed-number restrictions.

Dilate the prescribed finite schedule into coherent controlled isometries
$W_k$ that preserve all earlier Records. Dwell, site selection and occupation
append can be included in these maps. Readout can be deferred: later maps
are block diagonal in every earlier Record, so copying those labels into
degenerate environment cells earlier gives the same final reduced history
instrument. Uniform random choices can similarly be represented by prepared
finite control registers. Their preparation and storage are supplied.

Use the *same* battery throughout, retaining its correlations with matter.
For the untruncated lifts, the Fourier factors cancel exactly:

\[
\widetilde W_K\cdots\widetilde W_1
=\widetilde{W_{\rm hist}},\qquad W_{\rm hist}=W_K\cdots W_1.
\tag{23}
\]

Indeed multiplying (14) cancels adjacent
$e^{i\tau H_j}e^{-i\tau H_j}$. This is an operator identity on correlated
inputs; no product-state approximation at later steps is used.

Prepare (15) independently of the initial system and reference, choose
$a=c=2B$, and set $b=4B+w$. Initial total energy has support in
$[a-B,a+w+B]$. Exact total-energy intertwining preserves this support.
Since each intermediate system energy lies in $[-B,B]$, every intermediate
battery state has support in

\[
[a-2B,a+w+2B]=[0,b].
\tag{24}
\]

This spectral statement also holds for superpositions and entangled
intermediate states: $H_k$ and battery energy commute, and the total-energy
projection vanishes outside the initial interval. Therefore capping after
each lift removes no reachable amplitude. Equation (18) has $F=0$ on
each reachable input, because its successful norm equals the full input
norm. The completed physical gates (19) reproduce (23) there exactly.
There is no battery reset, no independent-step leakage sum, and no refusal
on the declared reachable sector.

For $W_{\rm hist}$, (22) gives $\|D_{\rm hist}\|\le2B$ and
$\|K_{\rm hist}\|\le4B^2$. Equation (17) consequently gives the entire
history error, including final outcome readout,

\[
\frac12\|\mathcal E_{\rm hist}-\mathcal I_{\rm hist}\|_\diamond
\le\frac{4\pi^2B^2}{w^2}.
\tag{25}
\]

For $0<\epsilon\le1$, choose

\[
w=\frac{2\pi B}{\sqrt\epsilon},\quad
b=4B+\frac{2\pi B}{\sqrt\epsilon},\quad
\boxed{\langle H_{\rm bat}\rangle
=2B+\frac{\pi B}{\sqrt\epsilon}
=Mt\left(6+\frac{3\pi}{\sqrt\epsilon}\right)}.
\tag{26}
\]

This sufficient initial mean and capacity are extensive in $M$ at fixed
accuracy and independent of the finite number $K\le M$ of events. The
battery has bounded positive energy but an infinite-dimensional continuous
carrier. Finite-dimensional commensurate examples below are separate
realizations. The budget is not asserted optimal. Outcome cells are supplied
per event, and the full site/order controller may require additional storage;
no extensive bound on all control memory is claimed.

## Exact implemented statistics with the shared battery

For these statistics, replace the broad sine in (26) by any normalized compact
wavefunction supported in $[2B,2B+w_0]$, with physical cap $[0,4B+w_0]$.
The support proof (24) still applies. No differentiability, Fourier-moment or
whole-history accuracy condition is required. A symmetric sine of width
$w_0=t$ has initial mean $6tM+t/2$ and capacity $12tM+t$.
These are normalizable wavefunctions; an energy eigenket of the continuous
battery is not used.

Fix a history with $m=M-|R|>0$ live sites, write $H=H_R$ and
$N=N_{\rm live,R}$, and let $N_i'=N-n_i$. The output energy and number commute
with their output Hamiltonian. Their pullbacks in each Fourier fiber are

\[
\begin{aligned}
W_{i,\tau}^\dagger H_{{\rm out},i}W_{i,\tau}
 &=H-e^{-i\tau H}V_i e^{i\tau H},\\
W_{i,\tau}^\dagger N_i'W_{i,\tau}
 &=N-e^{-i\tau H}n_i e^{i\tau H}.
\end{aligned}
\tag{27}
\]

Using $\sum_iV_i=2H$, $\sum_in_i=N$ and $[H,N]=0$, uniform site averaging
cancels the conjugation for every real $\tau$:

\[
\begin{aligned}
\frac1m\sum_i W_{i,\tau}^\dagger H_{{\rm out},i}W_{i,\tau}
 &=\left(1-\frac2m\right)H,\\
\frac1m\sum_i W_{i,\tau}^\dagger N_i'W_{i,\tau}
 &=\left(1-\frac1m\right)N.
\end{aligned}
\tag{28}
\]

Direct integration of this pointwise operator identity gives the corresponding
joint matter-battery identity, with an identity on the battery on the right.
Thus it applies to arbitrary correlations already created between battery,
matter and past Records, rather than only to product inputs. All cap
contractions agree with the bilateral lifts on the reachable subspace.
Reading occupation/site Records commutes with the displayed observables.

Consequently the *actual implemented process* obeys (7) and (8) exactly,
with no $\epsilon$ allowance. This conclusion retains the uniform selector
and the common preselection dwell. Detailed site/outcome probabilities and
conditional states are those of the implemented instrument; approximating
the complete ideal instrument uses the separate broad-packet theorem (25).

The same calculation for the output projector $Q_{i,1}$ onto a new occupied
Record gives

\[
\frac1m\sum_i W_{i,\tau}^\dagger Q_{i,1}W_{i,\tau}=\frac Nm.
\tag{29}
\]

On a prior history containing $x$ occupied Records, the live number is sharply
$N_0-x$. Hence the next recorded value is one with probability
$(N_0-x)/(M-k)$ after averaging the uniform site, conditional on that entire
past history. This is exactly the recurrence for drawing from an urn of $M$
entries with $N_0$ occupied entries without replacement. Therefore

\[
\begin{aligned}
\Pr(N_{{\rm live},K}=\ell)
 &=\frac{\binom{N_0}{\ell}\binom{M-N_0}{M-K-\ell}}
         {\binom M{M-K}},\\
\operatorname{Var}(N_{{\rm live},K})
 &=\frac{N_0}{M}\left(1-\frac{N_0}{M}\right)
   \frac{(M-K)K}{M-1}.
\end{aligned}
\tag{30}
\]

Binomial coefficients outside their allowed range are zero. The mass function
solves the stated one-step recurrence with initial live number $N_0$.
Its variance follows by representing a uniform subset of size $m=M-K$
using inclusion indicators: each has probability $m/M$, and each distinct
pair has probability $m(m-1)/(M(M-1))$. Summing the first and second moments
over the $N_0$ occupied entries gives (30). This representation proves the
count law; it imposes no classical spatial configuration on the quantum state.

For the energy second moment, the same fiber pullback yields

\[
\begin{aligned}
\frac1m\sum_i W_{i,\tau}^\dagger H_{{\rm out},i}^2W_{i,\tau}
 &=\left(1-\frac4m\right)H^2
 +\frac1m\sum_i e^{-i\tau H}V_i^2e^{i\tau H}\\
 &\le\left(1-\frac4m\right)H^2+6t^2I.
\end{aligned}
\tag{31}
\]

To derive the equality, expand $(H-V_i)^2$ and retain both ordered cross
terms. Their sum is $H(2H)+(2H)H=4H^2$. Inequality (10) bounds every
$V_i^2$ by $6t^2I$. Taking the correlated joint state and using exact mean
$e_{k+1}=(1-2/m)e_k$ gives, for variance $\sigma_k^2$ of the entire
history-block matter-energy observable,

\[
\sigma_{k+1}^2
\le\left(1-\frac4m\right)\sigma_k^2
-\frac{4e_k^2}{m^2}+6t^2
\le\sigma_k^2+6t^2.
\tag{32}
\]

The last inequality uses only $\sigma_k^2\ge0$ and is valid also at $m<4$.
At an empty live set the process stops. Induction gives

\[
\boxed{\sigma_K^2\le\sigma_0^2+6t^2K}.
\tag{33}
\]

This variance includes quantum energy spread and variation between histories.
It is distinct from the sample standard error in a finite simulation.

## Finite-density concentration and exact energy accounting

All implemented gates commute with the fixed total block energy, and the
same is true of dwell and copying commuting Records to degenerate cells.
Retain the spent battery and cells in the total ledger even when their
reduced states are discarded for observation. Then exactly

\[
\Delta\langle H_{\rm bat}\rangle
=-\Delta\langle H_{\rm matter}\rangle.
\tag{34}
\]

Old Records, their occupation consistency and total $N_0$ are exact. At half
filling, the actual count distribution (30) gives

\[
\mathbb E\frac{N_{\rm live}}{M-K}=\frac12,\qquad
\operatorname{Var}\!\left(\frac{N_{\rm live}}{M-K}\right)
=\frac{K}{4(M-1)(M-K)},\qquad K<M.
\tag{35}
\]

For an initially regular bipartite degree-six graph with every hopping
magnitude $t$, take the filled negative sea and occupy enough zero levels,
if present, to reach half filling. Spectral symmetry gives
$E_0=-\tfrac12\operatorname{Tr}|h|$. Since
$\operatorname{Tr}h^2=6t^2M$ and $\|h\|\le6t$,
$\operatorname{Tr}|h|\ge\operatorname{Tr}h^2/\|h\|\ge tM$.
Thus $E_0/M\le-t/2$, and this initial sea has sharp energy, including any
occupied zero modes. Writing $r_{M,K}=(M-K)(M-K-1)/(M(M-1))$, the exact
implemented energy law and (33) give

\[
\frac{e_K}M=\frac{E_0}M r_{M,K}\le-\frac t2 r_{M,K},\qquad
\operatorname{Var}(H_K/M)\le\frac{6t^2K}{M^2}.
\tag{36}
\]

For any $\delta>0$, Chebyshev gives the explicit spectral-weight bounds

\[
\begin{aligned}
\Pr\!\left(\left|\frac{N_{\rm live}}{M-K}-\frac12\right|\ge\delta\right)
 &\le \min\left\{1,\frac{K}{4\delta^2(M-1)(M-K)}\right\},\\
\Pr(H_K\ge0)
 &\le \min\left\{1,\frac{24K}{M^2r_{M,K}^2}\right\},\qquad K<M-1.
\end{aligned}
\tag{37}
\]

More quantitatively,
$\Pr(|H_K/M-e_K/M|\ge\delta t)\le
\min\{1,6K/(\delta^2M^2)\}$. At $K/M\to f<1$, the live fraction remains
positive, $r_{M,K}\to(1-f)^2$, and the two measured densities concentrate
about half filling and a negative value with fluctuations vanishing as
$M$ grows. Energy and live-number commute in each history block, so their
joint measurement may also be bounded by the sum of the two tail bounds.
These are bulk finite-density statements, with no uniform assertion about
every normalized history or about spatial transport.

For ground-excess diagnostics, each history uses the ground energy in its
actual fixed live-number sector, with all archived occupations counted.
The norm of the resulting direct-sum excess observable is at most $2B$.
If the broad sine in (26) is used, the conservative per-original-site
discrepancy between actual and ideal mean excess is at most $12t\epsilon$.
This separate readout uses the full-history approximation; (28) supplies
exactness only for its stated averaged operators. Ground-excess values
in the finite ideal pilot are computed directly.


## Exact history and energy comparison for stationary initial matter

A stronger comparison applies to an initial nonbattery state $\rho$ with
$[\rho,H_0]=0$, initially independent of the battery. With no earlier
Records this is the matter state, including any degenerate ready controls.
If earlier Records are included, stationarity refers to the full history-plus-
matter input under its block Hamiltonian, or to one sharp history block;
stationarity of a reduced matter marginal alone is insufficient. This includes
the sharp filled sea used above and stationary mixtures within fixed number.
Write $\sigma_{\rm ideal}=W_{\rm hist}\rho W_{\rm hist}^\dagger$ for the
complete coherent ideal history. From the fibers (14), the composition
identity (23), and the zero-refusal support (24),

\[
\boxed{\sigma_{\rm actual}
=\int |\widehat\beta(\tau)|^2
 e^{-i\tau H_K}\sigma_{\rm ideal}e^{i\tau H_K}\,d\tau.}
\tag{38}
\]

Indeed $e^{i\tau H_0}\rho e^{-i\tau H_0}=\rho$, so only the output
conjugation remains in the battery partial trace. The compact packet needs
no broad-width or Fourier-moment condition. Equation (38) is an energy
phase-averaging channel; it need not remove every off-diagonal matrix element.

For every bounded observable $A$ commuting with the final direct-sum
Hamiltonian $H_K$, cyclicity of the trace and normalization of the packet give

\[
\operatorname{Tr}(A\sigma_{\rm actual})
=\operatorname{Tr}(A\sigma_{\rm ideal}).
\tag{39}
\]

Take $A$ to be a complete Record-history projector multiplied by a spectral
projector of that history's final energy. These operators commute with $H_K$.
Their joint probabilities agree exactly, hence every complete history
probability and every conditional final energy distribution agree, omitting
zero-probability histories. The history-dependent ground-excess observable
also commutes with $H_K$, including its fixed live-number sector. Earlier
readouts may be deferred as above or applied to both sides: their commuting
projectors preserve (38) and (39).

This comparison allows an arbitrary supplied history-controlled schedule;
uniform selection is needed for the closed-form bulk laws, not for (38).
The statement concerns the full nonbattery input just specified. A retained external
reference admits the same joint formula when its joint input commutes with
$H_0\otimes I$. No initial matter-battery correlation is assumed here.
Final observables that fail to commute with $H_K$, including generic live-site
occupations and conditional state tomography, are outside (39).

Equations (38)-(39) apply separately to every prefix $W_{1:k}$ with
its final Hamiltonian $H_k$, using the same stationary initial state.
Every initial segment of the ideal 216-mode sea pilot therefore has the same
Record-history and energy statistics as the implemented model, by this
analytic bridge. Its ground-excess comparisons have zero actual-versus-ideal
discrepancy in this stationary-input case. The pilot remains an ideal Gaussian
computation, not a 216-mode apparatus simulation; its finite Monte Carlo
uncertainties are unchanged. Local matter coherence, transport and renewal
still require separate tests.

## Relation to earlier science

Energy-translation batteries, coherent overlap factors and repeated operation
are established machinery. Åberg's
[Catalytic Coherence](https://arxiv.org/abs/1304.1060) supplies the translation
construction and distinguishes reservoir state changes from preserved uses
of coherence. Tajima, Shiraishi and Saito's
[Coherence cost for violating conservation laws](https://arxiv.org/abs/1906.04076)
relates operation asymmetry to coherent resources and gives a Gaussian
construction. Chiribella, Yang and Renner's
[Fundamental energy requirement of reversible quantum operations](https://arxiv.org/abs/1908.10884)
provides bounded sine batteries and explicitly recycles a shared battery
through composed gates, particularly its Eq. (19).

The present contribution connects changing Record-history Hamiltonians to
the implemented process's exact uniform-site moment identities,
hypergeometric count law, finite-density concentration and stationary-input
history/energy comparison, alongside a
state-uniform continuous-battery estimate for the complete ideal history.
The local defect in (9) is an application of the established asymmetry
machinery. No priority or new general battery principle is claimed.

## Executable evidence and review record

The primary runner has 16 PASS and zero FAIL. Its complex Gaussian probes
directly form conditioned covariances and average their post-event energy,
live-number and energy-square expectations after earlier Records. A separate
216-mode cubic pi-flux pilot uses the ideal occupation/deletion instrument,
with 16 trajectories of 27 events at each dwell time 0 and 0.5. The actual
conditional state is reused throughout. Its exact event-27 mean energy is
-198.056118; the finite samples are -198.351462 +/- 0.279467 and
-198.124831 +/- 0.194630. These uncertainties are trajectory standard errors,
not pass windows. Ground references use the actual remaining particle sector.
No 216-mode battery apparatus is simulated.

The primary's apparatus evidence is a separate four-mode, two-particle,
complex two-dimer model with commensurate energies. A five-level discrete
battery tests nonzero refusal and CP completion. A 57-level battery is reused
for two events with intermediate dwell: sequential and directly composed
lifts agree to 1.421e-14, with intermediate Schmidt rank 3. Matter energies
-1.583929, -0.791965 and 0 are paired with directly computed battery energies
28, 27.208035 and 26.416071.

The independent checker has eight PASS and zero FAIL. It uses direct signed
fixed-number Fock matrices and a separate pi-flux square with polynomial
spectral projectors, rather than Gaussian covariance conditioning and the
primary's spectral eigendecomposition. Nine prior-Record/phase cases test
operator identities for energy, energy squared, live number and occupied
outcome effect; maximum residuals are 2.12e-15, 1.14e-14, 2.93e-15 and
1.03e-15. A correlated finite Fourier register additionally tests the joint
operator identities. Exact event enumeration checks the hypergeometric law.

Its 13-level commensurate battery retains correlations through two events,
with intermediate reduced-battery purity 0.864386720. Total energy stays
8.885281374 while matter energies 0.4, 0.6 and 0 are balanced by direct
battery expectations 8.485281, 8.285281 and 8.885281. Sparse refusal/swap
completion and an energy-commuting status copy are checked. Dense matrices
have dimension at most 312. The finite coherent-status example at p=0.04
gives distance 0.216977156 before readout and 0.04 after it.

A width-three packet also checks (38)-(39) for a ground state and a pure
zero-energy eigenstate in the initial degenerate subspace. First-event joint
Record-energy probabilities agree to 5.55e-17 and conditional ground excess
to 1.50e-16; complete two-event histories agree to 1.11e-16. The zero-energy
input has a first-stage state trace distance 0.375 despite these exact
commuting statistics. Its energy-commutator residual is 1.5. The ground
control happens to have no first-stage energy coherence, and the zero final
Hamiltonian makes final-state equality specific to this fixture.

These finite-dimensional commensurate realizations are separate from the
continuous battery proof. Numerical sine quadrature is a probe, and normalized
Choi trace distances are witnesses; neither is a diamond-bound proof.
The analytic proofs establish the general history and concentration claims.

The implementations were developed in separate contexts of the same model
family. The checker did not read or import the primary source, cache or pilot.
Root reviewed every source line, final repair diff, complete cache and all
27 actual failing scratch mutations (11 primary, 16 checker), as well as the
load-bearing mathematics. Separate-context algebraic refutations and a cold
note review were read in full. The latter's four bounded text findings were
repaired: sufficiency wording, the covariance definition, the obligation
graph and the finite-evidence reference. These are author-side reviews;
independent audit remains required for effective status.

Hard landing condition: register
repeated_record_matter_and_energy_conserving_apparatus_bounded_theorem_note_2026-09-05
with helper
scripts/repeated_record_matter_energy_apparatus_independent_check_2026_09_05.py.
The author branch does not edit that registry. Before publication, a disposable
current-main-plus-delta tree must show the checker in both the claim's changed
surfaces and populated helper-runner paths.
