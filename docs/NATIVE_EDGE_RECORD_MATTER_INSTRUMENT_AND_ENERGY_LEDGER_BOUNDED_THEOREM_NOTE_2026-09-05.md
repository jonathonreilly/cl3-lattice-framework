---
claim_id: native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "Conditional on the explicitly supplied finite ordinary-composition physical edge-qubit carrier, BKSF code, real hopping Hamiltonians, initial state, Born/Lueders event model and schedule: native single-site edge-Z events act as fair isometries preserving the surviving CAR state on nonbridges, and as signed component-parity projections on bridges. The updated code and original total number dictionary remain compatible through every history. Uniform live-edge selection gives the exact energy mean and variance bound stated below. A separately supplied positive-energy shared apparatus implements the history with exact total-energy accounting and the same moment bounds; with full initial nonbattery stationarity and independent cap-safe battery preparation it also has the ideal complete-history and conditional energy distributions. This is an alternative to occupation-site deletion, not its implementation or a derivation of formation, covariant carrier selection, nearest-neighbor admissibility, transport, renewal, or autonomous apparatus dynamics."
upstream_dependencies: []
runner: scripts/native_edge_record_matter_instrument_2026_09_05.py
---

# Native physical edge Records, fermion parity, and a common energy ledger

**Date:** 2026-09-05

**Type:** bounded_theorem

**Status:** conditional-support; independent audit unset

**Audit:** unset; the independent audit lane owns any verdict.

## Target and supplied physical meaning

This result connects an existing physical edge-qubit Record model to its
fermion dynamics through repeated events. A local edge Record has two exact
fermion meanings. While its edge lies on a remaining cycle it leaves the
surviving CAR state unchanged. When its edge disconnects a component it
projects that component's fermion parity. Both operations preserve the
original total particle number and admit the energy account proved below.

The construction needs no separate occupation-to-physical-Record compiler
for this native edge instrument. It changes the instrument used in an
occupation-site-deletion model: vertices remain, edges cease to hop, and
component parities can be measured. It does not realize that different
site-deletion process. BKSF encoding and one-bond deletion are established
ingredients, not the contribution claimed here.

Let a finite nearest-neighbor graph have virtual vertices at $2v$ and the
qubit for $(v,v+e_a)$ at physical lattice site $2v+e_a$. Distinct edges have
distinct centers; these are actual $M_2(\mathbb C)$ site factors in ordinary
tensor composition. Every other site is a spectator. This explicit
placement supplies a periodic choice of roles, a coarse cell, and a Pauli
basis. It does not derive a preferred origin, covariant role selection, or
the framework's nearest-neighbor admissibility distribution. A bounded
support Hamiltonian is not, by itself, that admissibility law.

The ideal event's projector is on one physical site and needs no extra clean
local pointer factor. Its occurrence, Born probabilities, and Lueders state
update are supplied. The energy apparatus is an additional construction:
it preserves the final Record values but generally changes conditional
matter coherences. Its control, energy carrier, preparation, and spatial
implementation remain supplied. A coherent history dilation may use
degenerate storage; no bound on all controller memory is claimed.

## Machine status and premise account

```yaml
packet_helper_runner: scripts/native_edge_record_matter_instrument_independent_check_2026_09_05.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "General finite operator proof with conditional physical placement and apparatus, supported by independent finite computations."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Repeated local Record formation sustaining a viable matter background with consistent energy accounting."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Test continuing transport and a physical event/apparatus law on the common Record-matter carrier."
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

| Input or bridge | Treatment here | Resulting obligation |
|---|---|---|
| Lattice and one-site algebra | Existing framework ontology, used for the stated placement only | No full framework model follows from this embedding |
| Ordinary tensor composition, roles, Pauli basis, BKSF code and hopping coefficients | Explicit conditions | Selection, preparation, and covariance remain open |
| Initial state and, for concentration, a sharp half-filled sea | Explicit conditions | No vacuum or state-selection rule is derived |
| Born/Lueders edge event and Hamiltonian dwell | Explicit conditions | Formation and nearest-neighbor law remain open |
| Which live edge forms next | Explicit condition; uniform only for closed bulk formulas | No rate, clock, or scheduler is derived |
| Native edge projection to surviving CAR instrument | Derived below | Separate occupation compiler is unnecessary for this alternative process |
| Shared energy apparatus and control | Explicitly constructed conditional implementation | Spatial realization, preparation, and autonomy remain open |

The current primitive registry and the source notes for scale reference,
kinetic isotropy, and realized state were read. Those approved primitives
are not classified as missing premises. None supplies the carrier, chosen
sea, event distribution, or apparatus used here. No new primitive, axiom
change, empirical value, fitted coefficient, or audit status is introduced.

## Definitions and algebra

Let $G=(V,E)$ be finite, connected, loopless and simple, with $M\ge2$
vertices and $L\ge1$ edges. Give vertices labels and each neighbor set a
fixed order. Orient $A_{ij}$ by $\epsilon_{ij}=1$ for $i<j$ and
$\epsilon_{ji}=-\epsilon_{ij}$. On the edge-qubit Hilbert space define

\[
B_i=\prod_{e\ni i}Z_e,\qquad
A_{ij}=\epsilon_{ij}X_{ij}
 \prod_{k<_i j}Z_{ik}\prod_{l<_j i}Z_{jl},\qquad
T_{ij}=\frac i2 A_{ij}(B_i-B_j).
\tag{1}
\]

Here the two ordered products omit edge $ij$. Set
$h_e=a_e T_e$, with real $|a_e|\le t$, $t>0$; set
$H_R=\sum_{e\notin R}h_e$ and $N=\sum_v(1-B_v)/2$.
All Hamiltonians use one common empty-fermion-vacuum zero; no
history-dependent scalar subtraction is permitted.

The operators $A,B$ are Hermitian involutions, $A_{ji}=-A_{ij}$,
$A_{ij}$ anticommutes with $B_i,B_j$ and commutes with other $B$'s.
Two distinct $A$'s anticommute exactly when their edges share one vertex.
These statements follow by counting the ordered $X,Z$ crossings. For a
simple oriented cycle $C=(v_0,\ldots,v_\ell=v_0)$ set

\[
S_C=i^\ell A_{v_0v_1}\cdots A_{v_{\ell-1}v_0}.
\tag{2}
\]

It is a Hermitian involution commuting with every $A,B$. Its Pauli
$X$ support is precisely the cycle. The phase is $i^\ell$, including
$i^6=-1$; a square-only phase convention is insufficient.

The initial code has every $S_C=+1$. After a history with recorded edges
$R$ and signs $z_r$, impose those old $Z_r=z_r$ and only cycles of
$G_R=(V,E\setminus R)$. Denote this code projector by $P_R$.
Let $q=L-|R|$ and let $c$ count all connected components, including
isolated vertices. All subsequent statements about a conditional state
refer to a nonzero branch; an impossible fixed-number branch is omitted.

## Theorem 1: remaining code and faithful fermion dictionary

The code dimension is $2^{M-c}$. Its component parities are

\[
\pi_C=\prod_{r\in\partial_G C}z_r,\qquad
\prod_C\pi_C=1.
\tag{3}
\]

Its surviving $A,B$ algebra is the product of the full matrix algebras on
the fixed-parity fermion sectors of the components. It is faithfully
identified with

\[
B_v=1-2c_v^\dagger c_v,\qquad
A_{ij}=-i\gamma_{2i}\gamma_{2j},\qquad
T_{ij}=c_i^\dagger c_j+c_j^\dagger c_i,
\tag{4}
\]

where $\gamma_{2i}=c_i+c_i^\dagger$ and
$\gamma_{2i+1}=-i(c_i-c_i^\dagger)$.
This concerns even CAR within each component. Odd global parity is not
represented by the unaugmented carrier because $\prod_vB_v=I$.

**Proof.** Choose a spanning forest of $G_R$. Each nontree edge gives a
fundamental cycle whose $X$ support contains that nontree edge alone among
the selected nontree coordinates. Thus the $q-M+c$ cycle checks are
independent. Old $Z$ checks add $|R|$ independent constraints: no nonempty
product of cycle checks has vanishing $X$ support, and no nonempty product
of old $Z$ checks is scalar. The commuting check group contains no $-I$.
Cycle relations from multiplication along paths generate every remaining
cycle from these fundamental cycles. Explicitly, the path operator
$U_P=i^{|P|}\prod_PA$ concatenates along consecutive paths and obeys
$U_{\bar P}U_P=I$: each immediate reverse-edge pair contributes
$i^2A_{ij}A_{ji}=I$. Insert forest paths from a component root before
and after each edge in a closed path. Successive reverse forest paths
cancel, leaving the product of its fundamental loops; these loops are
central by the displayed commutation relations. Thus no additional
independent cycle constraint has been omitted. The dimension follows from
$2^{L-(|R|+q-M+c)}$.

Multiplying $B_v$ over a component cancels internal edge $Z$ factors and
gives (3). A computational-basis assignment on live edges gives vertex
occupations by its binary incidence boundary plus the old boundary signs.
The incidence map has rank $M-c$; its image is exactly the patterns with
the component parities (3). Each such pattern has a fiber of size
$2^{q-M+c}$. The cycle checks act freely and transitively on that fiber
through their $X$ supports. The consistent $+1$ eigenspace on the fiber
therefore has dimension one.

Products of spanning-forest $A$'s connect any two occupation patterns with
the same component parities. Combining them with the one-dimensional
occupation projectors produces every matrix unit on this space. To check
that this full matrix algebra has the identification (4), use the displayed
anticommutation relations and cycle identities to reduce any word to a
product of a subset of forest $A$'s and a subset of $M-c$ independent
$B$'s. There are at most $2^{2(M-c)}$ such words. Both the physical
representation just constructed and the direct CAR representation (4)
satisfy these relations and generate a full matrix algebra of precisely
that dimension. They are faithful representations of the same quotient
algebra and are unitarily intertwined. In particular the hopping formula
in (4) follows by substituting the two Majoranas, without a fitted phase.

At fixed total $N$, the dimension is

\[
\sum_{\substack{\sum_C N_C=N\\(-1)^{N_C}=\pi_C}}
 \prod_C\binom{|C|}{N_C}.
\tag{5}
\]

This can vanish. For an initial half-filled code sea we require $M$ a
multiple of four, so $N=M/2$ belongs to global even parity.

## Theorem 2: the native Record instrument

Choose a live edge $e$ and measure the single-site projectors
$Q_{e,z}=(I+zZ_e)/2$, $z=\pm1$. Delete exactly its hopping term:
$H'=H_R-h_e$. This stipulated ideal event has the following two cases.

**Nonbridge.** Both outcomes have probability $1/2$ for every state
supported on the current code. The map $J_z=\sqrt2Q_{e,z}P_R$ is an
isometry onto the new code and preserves the state functional on the
entire surviving CAR algebra.

**Bridge.** Let $C$ be one side of the split in its former component and
$s_C=\prod_{r\in\partial_G C\cap R}z_r$. The measurement is precisely
the component-parity instrument

\[
Q_{e,z}\big|_{P_R}
=\frac12\left(I+z s_C\prod_{v\in C}B_v\right)\bigg|_{P_R}.
\tag{6}
\]

Its probabilities depend on the state and may be zero or one. Each branch
code has half the previous dimension before any fixed-$N$ restriction.
The newly fixed component parity is readable as the product of its
boundary Record values: every edge in that boundary is now recorded.
For an isolated vertex this product is $B_v$, so its occupation
$(1-B_v)/2$ is a function of Record content alone. This does not make
occupation at a vertex with unrecorded incident edges directly readable.

**Proof.** If $e$ is a nonbridge, a remaining cycle contains it. Its
stabilizer $S$ anticommutes with $Z_e$ and has $SP_R=P_R$. Consequently
$P_RZ_eP_R=0$ and $P_RQ_{e,z}P_R=P_R/2$. Surviving generators commute
with both $S$ and $Z_e$, so for every observable $O$ in their algebra,
$\operatorname{Tr}(\rho Z_eO)=0$ and

\[
\frac{\operatorname{Tr}(Q_{e,z}\rho Q_{e,z}O)}{1/2}
=\operatorname{Tr}(\rho O).
\tag{7}
\]

Deleting a nonbridge reduces $q$ and the cycle rank by one with $c$
unchanged. The new code has the old dimension, so the isometric inclusion
is onto. This identifies states through the faithful surviving algebra;
the physical branch vectors themselves are orthogonal, not equal.

For a bridge, every edge in the original cut $\partial_G C$ except $e$
is already recorded. Cancelling internal edges in $\prod_{v\in C}B_v$
gives (6), including all old signs. Here $q$ decreases and $c$ increases,
so the code dimension halves. No Gaussian closure is used. Destroyed cycle
checks must not be kept after a nonbridge event.

## Theorem 3: physical support, number, and repeated energy moments

Each $h_e$ has $X/Y$ support only on $e$, so $Q_{e,z}h_eQ_{e,z}=0$.
Every surviving $h_f$ commutes $Z_e$. Direct algebra in (1) gives

\[
[N,h_e]=[N,Z_e]=0,\qquad
h_e^2=\frac{a_e^2}{2}(I-B_iB_j),\qquad \|h_e\|\le |a_e|\le t.
\tag{8}
\]

For the first commutator, $h_e$ commutes all $B$'s except possibly those
at its endpoints; its commutator with $B_i+B_j$ vanishes because
$(B_i-B_j)(B_i+B_j)=0$. Individual Pauli summands need not conserve $N$.
All old Record values and an initially sharp total $N$ therefore persist
under every event and every current-Hamiltonian dwell.

In the midpoint placement, each factor in $h_e$ lies in the two endpoint
stars. Every edge center in these stars has Manhattan distance at most
two from the center of $e$. Thus radius two and diameter four bound the
physical support uniformly, with at most eleven site factors at degree
six. Deleting terms introduces no larger supports. This is a bound for
the stipulated matter Hamiltonian, not the full apparatus gate.

Let the next edge be uniform among the $q$ live edges, chosen after a
common dwell that may depend on the past history but not on that next
choice. Conditional on that history, selection is independent of the
current matter and battery, including their correlations. Outcome
averaging leaves powers of $H_R-h_e$ unchanged, giving

\[
\frac1q\sum_e(H_R-h_e)=(1-1/q)H_R,
\quad
\frac1q\sum_e(H_R-h_e)^2
=(1-2/q)H_R^2+\frac1q\sum_eh_e^2.
\tag{9}
\]

Let $\mu_k$ and $V_k$ be the mean and variance of energy including both
the classical history and quantum spectral distribution after $k$ events.
Since $q=L-k$ is the same at all histories, (9) yields, for $q\ge2$,

\[
\mu_{k+1}=(1-1/q)\mu_k,\quad
V_{k+1}=(1-2/q)V_k-\mu_k^2/q^2
 +\mathbb E_{R,e}\langle h_e^2\rangle\le V_k+t^2.
\tag{10}
\]

When $q=1$, the output Hamiltonian is zero; handle this endpoint directly.
Dwell preserves each incoming energy distribution. Therefore

\[
\boxed{\mu_K=\mu_0(1-K/L),\quad V_K\le V_0+Kt^2,\quad N_K=N_0.}
\tag{11}
\]

Fixed orders and nonuniform edge weights do not generally give the first
two formulas. The last formula is sharp number conservation for every
history, not merely an ensemble mean. All $M$ vertices remain in the
matter dictionary, including isolated ones. Total number thus includes
particles on inactive isolated vertices. Its conservation alone does not
bound how much matter remains on connected, propagating components.
Energy spectral distributions here are model diagnostics; no physical
energy-readout compiler is derived merely by calculating them.

For a supplied bipartite graph of maximum degree at most $d$ with all $|a_e|=t$,
let $h$ be the one-particle hopping matrix and initialize a sharp
half-filled ground sea in the allowed even sector. Its paired spectrum,
$\|h\|\le dt$, and $\operatorname{tr}h^2=2Lt^2$ imply
$E_0=-\operatorname{tr}|h|/2\le-Lt/d$; here
$|\lambda|\ge\lambda^2/(dt)$ for every eigenvalue, and zero modes
may be filled to reach half number. With $V_0=0$ and $K<L$, Chebyshev gives

\[
\mathbb P(H_K\ge0)
\le\min\left(1,\frac{d^2K}{(L-K)^2}\right).
\tag{12}
\]

This has a physical finite-volume realization without a periodic quotient.
For open cubic boxes of even side $\ell\ge2$, $M=\ell^3$,
$L=3\ell^2(\ell-1)$ and $d=6$ are valid. Thus
$E_0/M\le-(t/2)(1-1/\ell)$. At fixed recorded-edge fraction below one,
number density is exactly $1/2$, the mean energy density stays bounded
away from zero on its negative side, and $V_K/M^2$ tends to zero.
For an abstract degree-six regular graph, $L=3M$ recovers the equivalent
bound $4K/[M^2(1-K/L)^2]$; such a finite graph is not asserted to be
an open nearest-neighbor subgraph of $\mathbb Z^3$.
This does not prove transport, uniform component
density, a stationary state, or renewal of available edge sites.

## Theorem 4: shared energy apparatus and exact comparison

Include a prescribed finite schedule and degenerate control/history
storage in ideal isometries $W_k$. Histories are orthogonal output blocks;
old physical Record values are preserved. The history-block Hamiltonians
$H_k$ have $\|H_k\|\le B=tL$. For each selected edge the ideal
intertwining defect is $H_{\rm out}W-WH_{\rm in}=-Wh_e$, of norm at
most $t$.

On a comparison battery $L^2(\mathbb R,dE)$, let $T_u|E\rangle=|E+u\rangle$
and let battery energy be multiplication by $E$. For finite system
Hamiltonians define, with distinct eigenvalues grouped,

\[
\widetilde W=\sum_{a,b}\Pi_{\rm out}(b)W\Pi_{\rm in}(a)\otimes T_{a-b}.
\tag{13}
\]

In Fourier convention $T_u\mapsto e^{i\tau u}$ the fiber is
$W_\tau=e^{-i\tau H_{\rm out}}We^{i\tau H_{\rm in}}$ and hence an
isometry. Each summand proves exact total-energy intertwining. Using
the same battery for every step cancels adjacent Fourier factors, so
$\widetilde W_K\cdots\widetilde W_1=\widetilde{W_K\cdots W_1}$.
This is an operator identity and retains intermediate matter-battery
correlations.
Each incoming Hamiltonian preserves its remaining-cycle and old-Record
code, the ideal $W$ maps to the updated code, and each outgoing
Hamiltonian preserves that code. Hence every fiber, and the lifted
instrument, has the claimed updated code and sharp old Record outputs.

Prepare a normalized battery packet supported in $[2B,2B+w]$, cap its
physical energy domain to $[0,4B+w]$, and retain it. Initial total energy
is supported in $[B,3B+w]$. Since every intermediate system energy lies
in $[-B,B]$, its battery support lies in $[0,4B+w]$ at every prefix.
Thus capping removes no reachable amplitude. A completely defined
energy-intertwining gate on other inputs is obtained from the capped
contraction $S$ by adjoining the refusal component
$F=(I-S^\dagger S)^{1/2}$ in an orthogonal copy of the input sector.
$S^\dagger S$ commutes with input total energy, so does $F$; refusal
retains the input Hamiltonian. On all the reachable inputs just specified
$F=0$. This is a physical isometry with energy conservation; arbitrary
unitary/controller realization is a separate implementation problem.

For example, the normalized sine packet on this interval with $w=t$
has mean $2tL+t/2$ and cap $4tL+t$. The energy budget is extensive in
$L$, independent of the number of events $K\le L$. This bounded energy
interval is still an infinite-dimensional continuous carrier. No optimality
or finite-dimensional implementation for arbitrary incommensurate
Hamiltonians is asserted.

The pointwise pullbacks of the lifted energy moments are

\[
\frac1q\sum_e W_{e,\tau}^\dagger H'_e W_{e,\tau}=(1-1/q)H_R,
\quad
\frac1q\sum_e W_{e,\tau}^\dagger (H'_e)^2 W_{e,\tau}
=(1-2/q)H_R^2+
 e^{-i\tau H_R}\left(\frac1q\sum_eh_e^2\right)e^{i\tau H_R}.
\tag{14}
\]

The correction is bounded above by $t^2I$ at every $\tau$. These are
operator statements on arbitrary current correlated system-battery inputs,
so the exact mean, sharp number conservation, and variance bound in (11)
also hold for the implemented safe-cap process. Its second-moment
correction need not equal the ideal process's correction on a particular
state. Resetting to another safe battery would not invalidate the
pointwise bound; the retained battery supplies the single-resource budget
and whole-history composition used here. Exact total-energy accounting
means $\Delta\langle H_{\rm matter}\rangle+
\Delta\langle H_{\rm battery}\rangle=0$, with switch energy included in
the output Hamiltonian and the common zero convention.

If the full initial nonbattery state $\rho$ commutes with $H_0$ and is
prepared independently of the safe-cap battery, put
$\sigma_{\rm ideal}=W_{1:K}\rho W_{1:K}^\dagger$. Partial tracing the
shared lift gives

\[
\sigma_{\rm actual}=\int |\widehat\beta(\tau)|^2
 e^{-i\tau H_K}\sigma_{\rm ideal}e^{i\tau H_K}\,d\tau.
\tag{15}
\]

Every observable commuting with $H_K$ consequently has the same
expectation in the ideal and actual models. In particular their complete
procedural-history probabilities and conditional energy distributions
agree exactly, at every prefix. Uniform scheduling is needed for (11),
not this stationary-input comparison. Stationarity of only a reduced
matter marginal is insufficient if other nonbattery degrees of freedom
are correlated with it. A reference can be included when the joint input
commutes with $H_0\otimes I$.

Equation (15) does not imply equality of general conditional matter
coherences. The lifted gate need not be a single-site Lueders gate even
though its output has the specified sharp physical edge Record.
Procedural-history labels may include externally specified choice order;
the theorem does not make that order readable from final framework
Record content.

## Prior science and proof attribution

The BKSF generators, cycle checks and hopping conversion are standard;
see Setia and Whitfield, [Bravyi-Kitaev Superfast simulation of electronic
structure](https://arxiv.org/abs/1712.00446), equations 20–27 and 35.
The spanning-tree proof of loop-check independence is also presented in
Setia, Bravyi, Mezzacapo and Whitfield, [Superfast encodings for fermionic
quantum simulation](https://arxiv.org/abs/1810.05274), Appendix A.
The finite proofs above restate the required algebra and account for
recorded boundary signs and disconnected components explicitly.

Energy-translation coherence resources and shared-battery composition
have established precedents: [Catalytic Coherence](https://arxiv.org/abs/1304.1060),
[Coherence cost for violating conservation laws](https://arxiv.org/abs/1906.04076),
and [Fundamental energy requirement of reversible quantum operations](https://arxiv.org/abs/1908.10884).
Equations (13)–(15) rederive the needed specialization; these techniques
are not claimed as new physics.

Within the repository, the current-main finite cycle/cocircuit note and
finite cube conditioning/equality note establish relevant abstract finite
algebra. At pinned heads, PR #7883 establishes sea-specific edge/star
statistics and PR #7895 already establishes one-bond deletion. The
connection here is the general repeated nonbridge/bridge instrument on
the original number dictionary, together with its common energy account.
PR #7979 studies a different occupation-site-deletion process and the
shared-apparatus comparison. No unmerged audit grade or conclusion is
used as an authority for this self-contained proof.

## Executable evidence and independent review

The [primary source](../scripts/native_edge_record_matter_instrument_2026_09_05.py)
and [independent checker](../scripts/native_edge_record_matter_instrument_independent_check_2026_09_05.py)
were reviewed line by line by the supervising model. The checker used a
separate context of the same model family and read no primary source, output,
or cache. It uses direct small Pauli matrices, an independently solved full
intertwiner, occupation-sign CAR matrices, and an actual retained-battery
fixture; the primary uses symbolic Pauli words and physical cube code columns.
This is computational separation within one model family, not external peer
review or an audit verdict. A separate cold proof review was also completed.

The committed sources each pass nine check groups with zero failures in their
canonical [primary cache](../logs/runner-cache/native_edge_record_matter_instrument_2026_09_05.txt)
and [checker cache](../logs/runner-cache/native_edge_record_matter_instrument_independent_check_2026_09_05.txt).
Both declare a 180-second timeout and one BLAS thread. The primary's canonical
run reports 111.6 MiB peak RSS; no dense Fock square of axis 4096 is constructed.

| Evidence family | Executed finite scope |
|---|---|
| Physical cube dictionary | All 4096 edge masks and 24576 live-edge cases: 16716 bridges and 7860 nonbridges; 10199 fixed-number parity layouts, of which 358 are empty. The 4096-by-128 physical code intertwines every original A/B/T generator with independently constructed CAR matrices, including a six-cycle phase. |
| Repeated native events | Six physical-versus-CAR histories include sea and complex N=4 inputs, dwells, old boundary signs, deterministic and impossible outcomes, and a 4+4 component split. There are 52 nonzero final branches; maximum reported residual is 1.85e-13. The checker independently follows a full 384-leaf weighted edge/outcome tree, including zero-weight leaves. |
| Energy and support | Actual branch densities test both moment identities and their uniform weights; q=1 is checked directly. Open cubes of sides 2 and 4 test the finite-volume energy bound. The checker explicitly constructs the 11-site endpoint-star union, radius two and diameter four. These are matter support bounds. |
| Actual apparatus | On a physical four-edge square with Hamiltonian h_01+h_23 and the other two coefficients zero, one eight-level battery is retained through native Z_01 then Z_23 events. Exact commensurate transfers telescope on the full 8-by-4 code/packet domain. Both prefixes have zero reachable cap refusal and direct matter-plus-battery energy agreement. |
| Exact comparison and its limit | Ground and degenerate full nonbattery stationary inputs, prepared independently of the cap-safe battery, give the ideal joint history and conditional energy distributions. Independently normalized nonzero first-history matter blocks differ from their ideal counterparts by maximum Frobenius distance 0.5194; battery purity is 0.6. This is an explicit conditional-state distinction, not just a difference between coherent history vectors. |

The finite ladder fixture establishes the declared commensurate case only;
the continuous cap and arbitrary finite-Hamiltonian statements are proved
above. It does not simulate a general continuum battery on the cube.
Twenty primary fiber/defect checks and independent checker fiber moments at
q=4,3,2 test additional operator identities, including a correlated input.

Eleven primary and eighteen checker final-source scratch mutations exit 1.
The checker worker executed seventeen; root added the spectral-bound mutation
on the unchanged checker, isolating that numerical family from its self digest.
They cover hopping/orientation and loop signs, old Record signs, normalization,
selector and moment coefficients, number, physical placement, native versus
occupation projectors, battery shifts, history ordering, complex partial trace,
fiber phases, commensurability, and integrity/envelope guards. The separate
[mutation record](../.claude/science/physics-loops/record-matter-block05-20260905/MUTATION_CHECKS.md)
contains exact defects and failure outputs. One attempted primary particle-hole
mutation passed on its half-filled fixture and is explicitly excluded from the
eleven effective mutations; the checker tests the full number dictionary and
detects that defect. No unexecuted planned mutation is counted.

Final source SHA-256 values are
`05bc527d2d865acca27f55ce66b909eee8aa136eb7ab8d6d337b210addcfcf56`
(primary) and
`ebfef71248595e1cf621ee0464622fbc1d104f8028595d5334a30eab2ad314df`
(checker). Sources were committed before canonical execution. Root review
corrected an open-box versus finite-regular-graph conflation and required
conditional matter blocks to be normalized separately for the coherence
witness. All reported results use the corrected final source bytes.

## Review record and hard landing condition

The reviewed scope and corrections are recorded above. Outstanding at landing:
add the following exact claim-scoped helper entry to
`EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
`docs/audit/scripts/build_citation_graph.py`:

```python
"native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05": [
    "scripts/native_edge_record_matter_instrument_independent_check_2026_09_05.py",
],
```

This is a hard landing condition; the author branch does not edit the registry.
Before publication the complete delta plus this literal mapping is tested in a
disposable current-main tree. Readiness must name both changed sources and a
nonempty helper list containing the independent checker. It is a packet
completeness check, not an audit verdict. The independent audit lane owns any
scientific grade.
