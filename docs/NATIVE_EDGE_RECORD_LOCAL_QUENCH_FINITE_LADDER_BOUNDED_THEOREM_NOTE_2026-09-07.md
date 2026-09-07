---
claim_id: native_edge_record_local_quench_finite_ladder_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional native-CAR local-quench approximation and full-line energy-mean defect bounds; a positive finite-ladder approximation of the complete cube Record generator on its invariant safe input class, with retained-output trace-norm and original-energy mean certificates. Finite storage does not supply a local bath or axiomatic dynamics."
upstream_dependencies:
  - native_edge_record_ambient_generator_erasure_bounded_theorem_note_2026-09-07
  - native_edge_record_autonomous_head_shared_battery_bounded_theorem_note_2026-09-07
runner: scripts/native_edge_record_local_quench_finite_ladder_2026_09_07.py
---

# Local quench bounds and a finite positive battery for the complete Record law

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is conditional-support; independent audit is
unset. The construction approximates a supplied generator. It does not
derive its initial state, native hopping, head/fuel roles or event law from
the axioms, and it does not supply a local physical reservoir.

## Concrete result and remaining inputs

For the [complete autonomous cube law](NATIVE_EDGE_RECORD_AUTONOMOUS_HEAD_SHARED_BATTERY_BOUNDED_THEOREM_NOTE_2026-09-07.md),
keep its original sine packet[48,49], cap[0,97], hopping/fuel/rate parameters
and free matter Hamiltonian. At laboratory time T=1, a finite battery of
31040positive levels suffices for retained-output trace-norm error below
221/2240<0.1 and original total-energy mean error at most481/51200<0.01.
This battery occupies15qubits. With the
[ambient native representation](NATIVE_EDGE_RECORD_AMBIENT_GENERATOR_ERASURE_BOUNDED_THEOREM_NOTE_2026-09-07.md),
the specified system registers occupy48qubits in total, excluding bath,
clock, preparation and implementation hardware. This is an analytic
finite-dimensional GKSL construction, not a numerical simulation of48qubits.

A separate family result bounds how far the energy-dressed operation spreads
into matter. It uses the native CAR hopping structure rather than an
extensive many-body Hamiltonian norm. The spatially truncated full-line law
has an explicit global energy-mean defect tending to zero with radius. That
mean-defect result is not automatically transferred to a cap or rounded
energy spectrum. The finite whole-cube energy certificate has its own proof.

~~~yaml
packet_helper_runner:
  - scripts/native_edge_record_quench_orbital_check_2026_09_07.py
  - scripts/native_edge_record_finite_ladder_check_2026_09_07.py
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Explicit local-quench norm estimates, safe-reference finite-ladder channel comparison and rational finite-resource certificates, checked by independent CAR and native matrix witnesses."
trace_class: upstream_support
target_claim_id: native_edge_record_autonomous_head_shared_battery_bounded_theorem_note_2026-09-07
target_blocker_text: "Replace the continuous spectrally global energy apparatus with quantified spatial and finite-resource approximations."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Construct the finite-time reservoir/controller and price its locality, coupling and fresh-record resources."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

The native carrier and preparation, local role assignment, coherent battery
preparation, spectral controls, external time and Markov law remain supplied.
The finite storage count does not absorb an uncounted chronological system
register: its removal uses the actual CPTP ambient construction above.

## Native local-quench identity

Fix one eligible source code and selected edge e=(v,w). Write
H_in=H_rem+h_e, suppressing the scalar fuel energy. The complete two-sign
native column K satisfies K^dagger K=I and intertwines the surviving
Hamiltonian. These identities include bridges with their actual parity
branches; no additional fair-sign factor is inserted. In Fourier convention
exp(+i tau E), the lifted column is

\[
Y(\tau)=e^{i\Delta\tau}K E(\tau),\qquad
E(\tau)=e^{-iH_{rem}\tau}e^{i(H_{rem}+h_e)\tau}.
\]

Its derivative is E'=i h_e^-(tau)E with
h_e^-(tau)=exp(-iH_rem tau)h_e exp(iH_rem tau). This is negative ordinary
Heisenberg time. The fuel phase remains in the joint battery operation.

Retain a subset of **whole** surviving hopping terms near e, always keeping
h_e itself. Denote the resulting echo E_R and column Y_R. Both echoes are
unitary on the legal source code. Truncation omits virtual couplings; it does
not spend other fuels or impose extra physical Records.

On the faithful source CAR representation H_rem=dGamma(h), where h has
maximum degree d and hopping magnitudes at most t_h. Thus ||h||,||h_R||<=d t_h,
independent of particle number and volume. Let r be the graph distance from
{v,w} to any endpoint of an omitted nonzero hopping in the surviving graph,
and put m=r+1. If no omitted edge is reachable the error is zero. Define
T_m(x)=sum_(n>=m)x^n/n!.

The vectors h^n|v> and h_R^n|v>, and likewise for w, agree for n<m: the walk
must reach an omitted edge before traversing it. Taylor expansion gives
one-particle errors at most2T_m(d t_h|tau|). The CAR bound ||c(f)||=||f|| and
bilinear telescoping then give ||h_e^-(s)-h_e,R^-(s)||<=8t_h T_m(d t_h|s|).
Echo Duhamel integration proves

\[
\delta_R(\tau):=\|Y(\tau)-Y_R(\tau)\|
\le\min\left\{2,\frac8d T_{m+1}(d t_h|\tau|)\right\}.
\tag{1}
\]

This is a legal-code operator bound, including fixed N, source parity and
bridges. Odd CAR symbols provide a norm estimate, not local physical odd
edge-qubit operators. No N times an extensive Hamiltonian norm is used.

For physical geometry, place cubic vertices at2v and edge qubits/fuels at
midpoints. Each whole hopping has endpoint-star support within radius2 of
its midpoint in the ambient l1 metric. Let S contain the selected endpoint
star and two head sites, and retain whole supports inside B_R(S). A safe
uniform choice is m>=floor(R/2)+1. The bound transfers through the controlled
fuel blocks and physical erasure on their legal input domain. An unrestricted
ambient operator norm would require a separate locality argument.

For a directed occupation filter J, the correct fiber contains the additional
evolved factor J^-(tau): Y_fb=exp(iDelta tau)K J^-(tau)E(tau). A valid local
fiber bound adds4T_m(d t_h|tau|) to the right side before clipping at2.
Replacing J^-(tau) by constant J is false. The complete-law finite-battery
theorem below is not extended to this noncomplete feedback law.

## Global energy-mean defect of the full-line local law

Let H_ext=H_rem-H_rem,R. For the locally truncated complete column, its
defect relative to the **full** original energy has the exact identities

\[
D_R=[E_B,Y_R]+A_{out}Y_R-Y_R A_{in}
=e^{i\Delta\tau}K[H_{ext},E_R],
\]
\[
Y_R^\dagger D_R=E_R^\dagger H_{ext}E_R-H_{ext}.
\tag{2}
\]

The latter is Hermitian. One-particle row sums give ||h_ext||<=d t_h, and
h_ext h_R^n annihilates the two seed vectors for n<r. Four CAR bilinear
commutator terms and echo integration yield

\[
\|D_R(\tau)\|\le g_R(|\tau|):=
\min\{4t_h T_m(d t_h|\tau|),\;4d t_h^2|\tau|\}.
\tag{3}
\]

With one head, summed eligibility is at most d; use Lambda=gamma d, not a
sum proportional to the number of lattice edges. For the full-line local
GKSL law with the original full free Hamiltonian, the unconditional Fourier
marginal satisfies p_s(tau)=p_0(tau-s), even after battery correlations form.
This follows from pointwise trace cancellation of multiplier dissipators.
A selected trajectory need not have that marginal.

For the width-w sine packet and U>=sqrt(2)pi/w, its tail probability and
tail first moment obey

\[
\eta(U)\le\frac{32\pi}{3w^3U^3},\qquad
\mu_{1,tail}(U)\le\frac{16\pi}{w^3U^2}.
\]

Integrating the adjoint energy drift along the actual full-line local law gives

\[
|\langle H_{total}\rangle_T-\langle H_{total}\rangle_0|
\le\Lambda T\{g_R(U+T)
 +4d t_h^2[\mu_{1,tail}(U)+T\eta(U)]\}.
\tag{4}
\]

For example U=m/(2e d t_h)-T, when positive and beyond the tail threshold,
makes the short-time term exponentially small and the leading tail decrease
as U^-2. The estimate concerns finite-volume global energy-mean differences
with uniform constants. It does not define an infinite-volume global energy
operator. Cap compression, rounding, feedback and changed free Hamiltonians
need separate energy analyses; equation(4) is not imported into those cases.

## Exact safe reference for the finite cube

The remainder concerns the complete original finite cube, with d=3,
gamma=t_h=Delta=1. Its full ambient system energy satisfies0<=A<=24.
The initial packet[48,49] therefore gives Q support within[48,73]. Exact
total-energy conservation bounds subsequent battery support within[24,73],
strictly inside the original cap[0,97]. Every exact refusal amplitude vanishes.
The exact capped evolution agrees with the full-line evolution on this class.

Fix the initial legal head/fuel/Record sector and allow arbitrary admissible
matter/reference input, with this fixed product battery. Later all native
signs and trapped outcomes are retained. Classical mixtures of legal sectors
obeying the same safe enclosure are also allowed. No general statement on
coherent superpositions of distinct initial source sectors is required.

Round full finite-sector energies to multiples of delta, with a fixed tie
convention and the same eigenvectors. Call the result A^delta. Then
||A-A^delta||<=delta/2. The complete rounded full-line column W obeys

\[
\|V_e(\tau)-W_e(\tau)\|\le\delta|\tau|.
\tag{5}
\]

Both spectral exponentials contribute delta|tau|/2. Full fuel energy is
included once. Define S_e=P_cap W_e P_cap and one absorbing refusal
complement F_e=(E_e-S_e^dagger S_e)^1/2, where E_e is the source eligibility
effect. The approximate complete instrument has precisely the original
effect, so the two GKSL anticommutator terms cancel in their difference.

## Capped comparison along the exact evolution

For a reference source-block state rho of trace p, put
alpha_e^2=Tr[(V_e-W_e)^dagger(V_e-W_e)rho]. Exact reference safety gives

\[
\|(S_e-V_e)\sqrt\rho\|_2\le\alpha_e,
\qquad \operatorname{Tr}(F_e^\dagger F_e\rho)\le\alpha_e^2.
\]

The completed isometries therefore differ on sqrt(rho) by at most
sqrt(2)alpha_e, including the exact zero-refusal branch. Their output
trace-norm difference is at most2sqrt(2)sqrt(p)alpha_e. Summing source blocks
and at most3eligible edges, Cauchy-Schwarz gives the generator estimate

\[
\|(G_{approx}-G_{exact})(\rho_s)\|_1
\le2\sqrt2\Lambda\delta
 \sqrt{\int\tau^2p_s(\tau)d\tau},\qquad\Lambda=3.
\tag{6}
\]

Duhamel applies the difference to the **exact** safe evolution and then
propagates it with the approximate CPTP map. The approximate process need
not remain safe or have a translating Fourier marginal. For the exact
reference, p_0 is even and its second moment is pi^2/w^2; hence the moment
at time s is pi^2/w^2+s^2. Integration bounds the retained-output difference by
2sqrt(2)Lambda delta T sqrt(pi^2/w^2+T^2).

This proof uses no Poisson construction, endpoint-leakage substitution or
product-battery reset. A prior broader Poisson statement was corrected:
scalar sector rates alone do not justify its action on coherences between
different-rate sectors. The [preserved erratum](../.claude/science/physics-loops/record-autonomous-head-20260907/local-apparatus/UNIFORMIZATION_ERRATUM.md)
contains the counterexample and original hashes. That shortcut is not a
premise of equations(5)–(6).

## Finite cells, free evolution and resource certificate

Embed the ladder basis as normalized constants on cells
[j delta,(j+1)delta), with energy centers(j+1/2)delta. Choose97=M delta.
Rounded energy differences are integer shifts; these, the aligned cap and
the complementary square root preserve the step-function subspace and its
orthogonal complement. Replacing free E_B by its cell-center operator costs
at most delta T in trace norm, since their operator difference is at most
delta/2. The original free matter A is retained.

Finally project the original sine to normalized cell averages beta_delta.
Cellwise Poincare gives ||beta-P_delta beta||<=delta/w, so preparation costs
at most2delta/w in trace norm. This substitution occurs **after** the safe
reference comparison; no claim of projected-input exact safety is needed.
The final model restricted to M cells is finite and positive. Altogether

\[
\|\Phi^{finite}_T-\Phi^{exact}_T\|_{\diamond,\,fixed\ battery}
\le\delta\left[\frac2w+T+
 2\sqrt2\Lambda T\sqrt{\pi^2/w^2+T^2}\right].
\tag{7}
\]

The input of these maps is the matter in the fixed initial legal sector,
including arbitrary reference entanglement; output includes the retained
battery, all physical sectors and refusal flag. This is not an unrestricted
battery-input diamond norm. Conventional state trace distance is half the
trace norm used here.

Take delta=1/320, w=T=1, Lambda=3. The original cap and packet endpoints align
exactly, and Delta=1 is320mesh steps. Using pi<22/7, sqrt(2)<10/7 and
sqrt(pi^2+1)<10/3, the coefficient in brackets is strictly below221/7.
Thus equation(7) is below221/2240<0.1. The number of positive half-cell levels
is97*320=31040, with1728unused codes in15qubits. Choose an inert
trace-preserving extension on those unused codes; the declared preparation
and dynamics never enter them. Native12edge qubits,
12fuel qubits,8one-hot head qubits and1refusal flag give48storage qubits.
No physical bath, fresh collision ancillas, controller or gate-synthesis
resources are included in that storage count.

For this **whole** finite model A^delta is a spectral function of A. Therefore
the original free A+E_B^delta commutes with the conserved rounded total
energy A^delta+E_B^delta, even though they are unequal. Every rounded jump
and matched refusal also conserves that energy distribution exactly.
Original energy differs from rounded energy by at most delta under the cell
embedding. Two endpoints and the preparation error give the conservative
original total-energy mean bound

\[
3\delta+2\delta^2/w=481/51200<0.01.
\tag{8}
\]

The aligned projected packet actually has exactly the original mean48.5 by
reflection symmetry; the stated conservative bound remains valid. No exact
unrounded energy-distribution conservation is claimed. A rounded local
truncation generally does not commute with the full free A; equation(8)
must not be transferred to that different construction.

Equations(1) and(6) also compose: replace delta|tau| by the sum of the local
quench error and local rounding error and integrate its RMS along the exact
safe marginal. The cap/refusal argument remains valid. This supplies a
finite-battery local-jump trace approximation with full free evolution, but
global energy error and actual physical control locality remain separately
priced obligations.

## Independent executable checks

The primary builds all64Fock matrices for a fixed six-mode chain and32cut/
Fourier-time cases. An independent six-by-six calculation obtains echo norms
from exterior eigenvalue products and energy-defect norms from Hermitian
subset sums. All32keyed rows agree below3e-15. It does not import the Fock
primary. The live primary validates source hash, exact case coverage,
resource contract and16malformed controls. The169residual checks and96further
bound assertions are distinct counts. Feedback norm bounds are internally
checked and algebraically reviewed; they are not independently numerically
compared by that six-mode helper. Exact rational arithmetic checks equations
(7)–(8) and the level/register counts; it does not propagate48qubits.

A separately preregistered native N2 square uses opposite-dimer coefficients
1 and sqrt(2)/3, original sine[4,5], cap12, spacing1/4 and48positive levels.
All signs of a fixed three-event sequence retain the battery and use the
original free Hamiltonian. Its519checks cover rounded energy indicators,
cap/refusal, native code, continuous-energy quadrature and adverse controls.
Rounded energy is invariant, while original energy changes by-0.02562305.
An unsafe input refuses with probability0.13076572. The coarse-grid final
retained trace-norm difference from the continuous reference is0.49031779.
This is an actual coarse comparison, not a numerical small-error claim or
an all-path fixed-time cube computation. Resetting the battery changes its
energy result; per-sign refusal and the unrestricted Poisson extension fail
their controls. These fixed witness parameters are not fitted to the cube
certificate.

## Scope and next construction

The results replace an infinite-dimensional battery input with a quantified
finite approximation on the stated finite-time class and establish explicit
native spatial error bounds. They preserve the original failed transport
diagnostics; no new transport success is inferred from an apparatus theorem.
Globally spectral cube jumps, preparation and the Markov reservoir remain
supplied. A finite-time unitary reservoir/controller construction must price
fresh ancillary purity, clock accuracy, coupling strength and spatial
implementation. Renewal and a formation law derived from the axioms remain
open constructive tasks.

## No-Go Discipline Gate

The [source-linked scope checklist](../.claude/science/physics-loops/record-autonomous-head-20260907/local-apparatus/NO_GO_DISCIPLINE_CHECKLIST.md)
records actual constructive attempts and the corrected overextension.
Heavy negative-packet five-family PASS is not asserted. Finite errors and
resource bounds establish no universal impossibility of other apparatuses.
