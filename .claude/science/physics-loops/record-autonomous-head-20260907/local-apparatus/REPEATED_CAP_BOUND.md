# Repeated intermediate cap tests for the complete native law

> Corrected domain (source-sector uniformization erratum): every fixed-time
> Poisson/uniformization claim in this memo is restricted to a definite legal
> initial head/fuel/Record source sector, with arbitrary matter/battery/reference
> coherence within that sector, or a classical mixture of such sectors. The
> dynamics must preserve this block-diagonal class. Fixed-battery diamond norms
> mean maps from admissible matter inputs in that declared source class, not
> arbitrary coherent inputs across the whole source-sector direct sum. See
> UNIFORMIZATION_ERRATUM.md and the preserved historical version. Single-event
> transfer bounds and the sequential-projection lemma themselves are unchanged.


A rigorous bound is available without resets. An elementary sequential-projection
argument is stronger than the amplitude-sum estimate: it gives failure<=4 times
the SUM of ideal prefix leakage probabilities. This is a quantum union bound,
proved below rather than treating endpoint leakage as first exit. It controls
the actual repeated-test process and its accepted output. All probabilities
refer to complete native sign columns, not normalized favorable sign histories.

## Setup and ideal prefix leakage

Let P be the battery projection onto[0,Ecap]. Start from any normalized input
supported on I=[b,b+w] strictly inside that cap; write u=Ecap-b-w>0 and
 S=b^-2+u^-2.
Let V_j be complete event isometries, with any free unitary segments absorbed
into them, and suppose ||[EB,V_j]||<=c. Free segments commute strongly with EB
and cost zero. The shared battery is retained throughout. The ideal prefix
Psi_j=V_j...V_1 psi has leakage
 q_j=||(I-P)Psi_j||²<=min{1,j² c² S}.
This follows from the bounded-commutator/Sylvester lemma, not a hard support
bound. All ideal paths in the column and any reference system are included.

The actual accepted branch is
 Phi_n=P V_n P V_(n-1)...P V_1 psi.
Its squared norm is the probability that EVERY intermediate cap test accepts.
Completing each accepted column with one absorbing refusal complement produces
precisely this success branch. Subsequent operations after a refusal can be
arbitrary CPTP evolution within its absorbing sector; they do not alter the
first-refusal probability or the accepted branch.

## Elementary sequential-projection lemma

Dilate each V_j to a unitary on a common Hilbert space with fresh environment
registers. Existing Record/environment registers are retained. Pull each cap
projector back by the IDEAL unitary prefix. This gives orthogonal projectors
P_1,...,P_n on one initial Hilbert space, with
 q_j=||(I-P_j)psi||²,
 phi=P_n...P_1 psi,
 p=||phi||²=||Phi_n||².
The pullback identity is exact: pushing the final ideal unitary forward recovers
the accepted physical sequence. The unitary extension outside the occupied
input subspace need not be a physical implementation; it is a proof dilation.

Put phi_0=psi, phi_j=P_j phi_(j-1), and
 ell_j=(I-P_j)phi_(j-1).
Orthogonality at each projection gives
 f:=1-p=sum_j||ell_j||²,
 psi-phi=sum_j ell_j.
Define a=1-Re<psi,phi> and Q=sum_j q_j. Since ell_j lies in the range of
I-P_j, Cauchy-Schwarz gives
 a=sum_j Re<(I-P_j)psi,ell_j>
   <=sqrt(Q) sqrt(f).
Also d²:=||psi-phi||²=2a-f. Consequently
 d²+(sqrt(f)-sqrt(Q))²<=Q.                              (1)
In particular
 f<=min{1,4Q}, and d²<=Q.                               (2)
No commutation between the different P_j was used. In particular this is not
a classical union bound and does not replace the actual state by the ideal
state at each test.

For the local transfer bound above, define
 B_n=c² S sum_(j=1)^n j²
    =c² S n(n+1)(2n+1)/6.
One may replace B_n by the tighter sum_j min(1,j² c² S). Uniformly over allowed
inputs and reference entanglement, (2) implies
 Prob(at least one refusal through n events)<=min{1,4B_n}. (3)
Thus actual all-tests success is at least max{0,1-4B_n}. This uses ideal PREFIX
leakages at every test, not solely final leakage q_n.

## Output disturbance: subnormalized and complete processes

For the accepted, UNNORMALIZED output, the rank-one telescoping bound gives
 || |Phi_n><Phi_n|-|Psi_n><Psi_n| ||_1
 <=(||Phi_n||+1)||Phi_n-Psi_n||<=2sqrt(B_n).              (4)
Purification and trace contraction make this a diamond-norm bound on the
accepted CP trace-nonincreasing map versus the ideal channel, restricted to
the declared initial battery-support subspace. Include min(2,right side).
This is a genuine shared-battery output bound, not just a matter marginal.

For the complete capped-with-absorbing-refusal channel, retain a first-refusal
flag in a common dilation. The ideal state has only the all-success flag. The
capped dilation has success amplitude Phi_n and orthogonal refusal amplitudes
of total squared norm f. Their squared vector distance is
 ||Phi_n-Psi_n||²+f=2a<=2sqrt(Qf)<=4Q.
Hence the complete capped versus ideal output channels satisfy
 ||Capped_n-Ideal_n||_diamond<=min{2,4sqrt(B_n)}.          (5)
Refusal outputs may carry the actual same-Hamiltonian absorbing-copy states;
the proof uses only their norm and orthogonal flag, not a fictitious discarded
failure branch. Tracing the battery or flags can only reduce the distance.

For a fixed input, if one deliberately normalizes the accepted state, then
its pure-state trace distance to the ideal state is at most2d/sqrt(p), by
bounding the component of phi perpendicular to psi. Thus, provided B_n<1/4,
 conditional accepted-state distance<=min{2,2sqrt(B_n/(1-4B_n))}. (6)
This is an input-state statement, not a diamond norm of a nonlinear normalized
map. Equations(3)–(5) require no postselected normalization and remain the main
operational estimates. Rare-success regimes are not given a uniform small
conditional error.

## Fixed laboratory time with Poisson uniformization

For the complete native GKSL law RESTRICTED to the invariant source-block-
diagonal class, with at most D outgoing edges per source,
use Lambda=gamma D and lambda=Lambda T. The complete uniformization column W
contains all sqrt(gamma/Lambda) native edge/sign columns and the null block
sqrt(I-R/Lambda), with R=gamma direct_sum d_s I_s. The null term commutes with
EB; source/channel orthogonality gives ||[EB,W]||<=c as in the previous lemma.
Free Hamiltonian propagation commutes with EB, but need not commute with W.

Condition on a Poisson tick count N=n and its ordered times. The actual dynamics
is a sequence of W columns INTERLEAVED with those free propagators. Apply the
same cap after each column. Null ticks add no actual refusal on already capped
inputs; counting them in the estimate is merely conservative. Free propagation
cannot carry an accepted battery out of its cap, because it commutes with P.
The conditional proof above holds for every ordered time sequence. Neither the
Poisson weights nor the ordered-time law require W to commute with free evolution.

Let
 B(lambda)=E[B_N]
 =c² S [lambda+(3/2)lambda²+(1/3)lambda³],               (7)
using E[N²]=lambda²+lambda and E[N³]=lambda³+3lambda²+lambda.
Averaging(3) and using Jensen for(4)–(5) gives
 Prob(first refusal by T)<=min{1,4B(lambda)},             (8)
 accepted-subnormalized versus ideal diamond
       <=min{2,2sqrt(B(lambda))},                       (9)
 complete absorbing-refusal versus ideal diamond
       <=min{2,4sqrt(B(lambda))}.                       (10)
These compare the actual fixed-time processes on the declared initial-source
class with one retained battery. They are not unrestricted full-source-direct-
sum diamond estimates.
They do not assume a product state after any event. A sharper bound can retain
the Poisson expectation of the clipped finite-n inequalities instead of Jensen;
no parameter optimization is performed here.

To match the physical capped generator, use separate edge-refusal branches
sqrt(gamma) F_e and the SAME null block. The accepted uniformization column is
P W P. The combined refusal effect is the sum of its edge-refusal effects;
separate absorbing labels or an equivalent combined complement have the same
success branch and failure probability. Completion restores gamma d_s on each
source even when refusal is possible, so the same Lambda uniformizes both laws.
A refusal sector has no outgoing physical jumps (only uniformization null ticks).

## Exact energy, domains and scope

The uncapped complete V_j exactly intertwines total energy. Cap projections
commute with the source/target total Hamiltonians. The complement
F_j=(I_cap-S_j*S_j)^(1/2) therefore commutes strongly with the input total
Hamiltonian, and its absorbing copy carries that SAME Hamiltonian. Each actual
accepted/refused event and the interposed free evolution preserve the modeled
total-energy distribution exactly. This is compatible with nonzero refusal.
The proof dilation itself need not be an energy-conserving physical unitary.

The unbounded EB commutators are the bounded extensions established in the
previous energy-transfer lemma; the present argument uses only bounded cap
projections and isometries after obtaining q_j. There is no additional unbounded
operator-domain step in the projection proof. Finite-time uniformization uses
the bounded jump perturbation of the strongly continuous free dynamics.

The required source/history space includes all physically permitted deletion
histories, not just four events. The number of events is bounded by finite fuel
on the finite fixture; Poisson null ticks can be arbitrarily numerous. The norm
and probability bounds are volume-uniform when c,D and the stated local native
identities are uniform. No infinite-volume global-lift existence is asserted.

These estimates concern the COMPLETE K law with full sign sums. They do not
transfer to the feedback KJ law, arbitrary rare conditioned paths, an apparatus
with reset batteries, or the approximate-locality jumps without separate energy
and cap analysis. The positive capped battery remains continuous and the model
still supplies native preparation, head/fuel/memory and an absorbing refusal
sector. No finite local-qubit implementation, resource optimum or renewal claim
is established.
