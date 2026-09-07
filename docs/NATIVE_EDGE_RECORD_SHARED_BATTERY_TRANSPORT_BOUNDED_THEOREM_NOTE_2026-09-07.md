---
claim_id: native_edge_record_shared_battery_transport_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional shared continuous-battery dynamics for the fixed five-event open-cube native Record/CAR fixture with arbitrary nonstationary input and directly contracted battery energy. Controlled matter-only and laboratory-free dwells are distinguished. A dimension-independent observable bound and exact-rational ideal margins give sufficient controlled-protocol widths 125 and 260 for the stated current, density and energy tests. Width-one outcomes are finite observations. The carrier, preparation, apparatus, event model and schedule are supplied; spatially local autonomous realization and continuum matter are outside this theorem."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
  - native_edge_record_local_cycle_transport_and_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_edge_record_shared_battery_transport_2026_09_07.py
---

# Native edge Record transport with one shared continuous battery

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained

The proposal is for the explicitly conditional result below. Its actual
current-surface status is **conditional-support**, and independent audit is
unset. The author proposal does not assign an audit verdict or effective grade.

## Target and premise account

The downstream consumer is the fixed local Record-front transport protocol
in the [parent transport note](NATIVE_EDGE_RECORD_LOCAL_CYCLE_TRANSPORT_AND_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md).
Its next action is to supply a physical energy apparatus on the same carrier.
This note evaluates the actual shared continuous apparatus from the
[parent instrument note](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
on that protocol. The phase-pulsed input is nonstationary, so the parent's
stationary-input reduced-channel comparison cannot be substituted here.

~~~yaml
packet_helper_runner:
  - scripts/native_edge_record_shared_battery_transport_independent_check_2026_09_07.py
  - scripts/native_edge_record_transport_ideal_margin_certificate_2026_09_07.py
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Explicit conditional apparatus formula and finite transport computation."
trace_class: upstream_support
target_claim_id: native_edge_record_local_cycle_transport_and_ledger_bounded_theorem_note_2026-09-05
target_blocker_text: "Supply autonomous formation/renewal and a physical finite or continuous energy apparatus on this same carrier."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Quantify the apparatus coherence resource and construct a spatially local autonomous realization."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

| Premise | Role | Derivation obligation outside this result |
|---|---|---|
| Eight-vertex native edge carrier and faithful CAR identification | Inherited finite algebra | Selection and realization from the framework axioms |
| Half-filled ground state and phase pulse | Supplied preparation | Physical preparation law and resource realization |
| Five nonbridge edges, endpoint port orders and dwell times | Supplied protocol | Autonomous event occurrence and schedule |
| Born/Lueders Record isometries and hopping deletion | Supplied instrument | Formation and renewal |
| Sine battery and total-energy spectral lift | Supplied apparatus model | Preparation and spatially local implementation |

These are a dependency account, not a claim of five independent impossibility
walls. No new axiom, primitive, empirical value or fitted selector is used.
The inherited carrier and schedule are unratified parent dependencies. Their
source notes, runners and evidence are carried in this main-based landing
delta and were included in the independent conditional-algebra review.
Their original proposals are PR #7983 and PR #7996; no parent branch is edited.

## Frozen fixture and measurement times

The fixed particle sector has eight sites, four fermions and dimension 70.
The ordered edges and hopping coefficients are

~~~text
edges        = (01,02,04,13,15,23,26,37,45,46,57,67)
coefficients = (-1,-1,-1,-1,-1,+1,-1,-1,+1,+1,+1,-1)
deletions    = (0,3,5,6,9)
dwells       = (0.41,0.37,0.29,0.23,0.19)
pulse        = exp[-i 0.7 (n_0-n_1)]
~~~

For the live edge set after event j, let

\[
H_j=\sum_{e=(u,v)\text{ live}}c_e(c_u^\dagger c_v+c_v^\dagger c_u),
\qquad J_e=ic_e(c_u^\dagger c_v-c_v^\dagger c_u).
\]

Write D_j=exp(-i d_j H_{j-1}) and U_j=D_j ... D_1. The surface j-minus
is after dwell j and before deleting its edge. The surface j-plus is
immediately after deletion. The parent column called `Jpre` was before the
dwell; its `Jpost` was j-minus. Here surviving-edge post-event currents
are separately identified as j-plus.

The original transport test requires at least four live edges with
|J_e| >= 0.02 at every j-minus surface and at least one selected front
current of magnitude >= 0.05. The density window is [0.10,0.90]. We also
report j-plus transport and require every post-event matter energy to be
negative. These stronger diagnostics are not silently substituted for the
original gate.

## Shared apparatus formula for nonstationary input

Let P_in(a), P_out(b) denote the finite system energy projectors. For an
isometry W between input and output matter/Record sectors, use the lift

\[
\widetilde W=\sum_{a,b}P_{\rm out}(b)W P_{\rm in}(a)\otimes T_{a-b},
\qquad (T_u\beta)(E)=\beta(E-u).
\]

Each summand conserves total energy because b+(E+a-b)=E+a. On the
uncapped energy line, Fourier transformation gives the isometric fiber
exp(-i tau H_out) W exp(i tau H_in). This proves the lift is an isometry;
it does not merely assert that its energy expectation is conserved.

The same battery is retained at all events. In the faithful CAR identification,
each normalized nonbridge Record branch is identity on matter. Multiplying
the Fourier fibers makes adjacent Hamiltonian conjugations cancel, since
each dwell commutes with its current Hamiltonian. For a prefix surface s,
with ideal matter map U_s and current Hamiltonian H_s, the resulting fiber is

\[
V_s(\tau)=e^{-i\tau H_s}U_s e^{i\tau H_0},\qquad
\rho_s=\int_{\mathbb R}|\widehat\beta(\tau)|^2
V_s(\tau)\rho_0V_s(\tau)^\dagger\,d\tau. \tag{1}
\]

The supplied dwell operation here is D_j tensor I_B, which is itself
total-energy conserving and is the lift of the parent's ideal dwell.
It is not an assertion about uncontrolled laboratory evolution under
H_{j-1}+E_B. If the battery evolves freely in the laboratory, its phase
must also be propagated and the event control convention specified.
Energy conservation of these gates does not supply that phase control
or a clock implementation.

For j-minus use U_s=U_j and H_s=H_{j-1}; for j-plus use U_s=U_j and
H_s=H_j. Equation (1) holds for arbitrary input density operators by
linearity. In particular, e^{i tau H_0} rho_0 e^{-i tau H_0} cannot be
removed for the supplied phase-pulsed sea. At the first j-minus surface
the two conjugations cancel with D_1, giving exactly D_1 rho_0 D_1^dagger.
This is an independent timing control.

For pure input psi_0, define

\[
x_{ab}=P_s(b)U_sP_0(a)\psi_0,\qquad u_{ab}=a-b.
\]

The joint state is sum_{a,b} x_{ab} tensor T_{u_{ab}} beta. Its reduced
state is the finite contraction

\[
\rho_s=\sum_{a,b,a',b'}x_{ab}x_{a'b'}^\dagger
K_w(u_{ab}-u_{a'b'}). \tag{2}
\]

This contraction includes the initial energy coherences and the battery
correlations accumulated across events. It is not a sequence of independently
reset reduced channels.

## Continuous packet, energy moment and cap

The frozen baseline has

\[
\beta_w(E)=\sqrt{2/w}\sin[\pi(E-24)/w]\,1_{[24,24+w]}(E),
\qquad w=1.
\]

For x=|s|/w, elementary integration on the overlap interval gives

\[
K_w(s)=\begin{cases}
(1-x)\cos(\pi x)+\sin(\pi x)/\pi,&x<1,\\
0,&x\ge1.
\end{cases} \tag{3}
\]

The product beta_w(E-u) beta_w(E-v) is symmetric about
m=24+w/2+(u+v)/2. Its odd first moment therefore vanishes, proving

\[
\langle T_v\beta_w|E_B|T_u\beta_w\rangle
=\left[24+\frac w2+\frac{u+v}{2}\right]K_w(u-v). \tag{4}
\]

The battery energy is calculated by contracting (4) with
<x_{a'b'}|x_{ab}>. Only after that computation is it added to the matter
energy and compared with the initial total. Defining the battery energy
as the compensating difference would not test this apparatus.

The parent norm bound is ||H_j|| <= 12. Initial battery support [24,25]
therefore gives total-energy support [12,37]. Every reachable prefix
battery support lies in [0,49]. Restricting the lifted instrument to this
reachable sector produces no cap refusal. This is a spectral support
argument; a battery mean inside the cap would not suffice. The interval is
bounded, but L2([0,49]) is infinite-dimensional.

Each selected edge is a nonbridge. In the physical representation its two
Kraus branches are 1/sqrt(2) times isometries into orthogonal Record sectors.
The energy lift preserves this property even for a correlated input battery.
Consequently all 2^j prefix histories have weight 2^-j; pulled-back matter
states agree across them. Physical branch vectors need not agree. Number
and old Record sectors are preserved by the conditional Hamiltonians and
their spectral projectors. The numerical CAR computation checks number;
the native Record statement uses this inherited algebraic proof, not a
numerical test of the tautology 2^j 2^-j=1.

The spectral projectors in the lift generally act on the connected matter
graph. Bounded support of the original h_e and Q_e does not establish spatial
locality of this apparatus. Its implementation by the framework's native
nearest-neighbor law remains a separate constructive task.

## Free battery evolution is a separate protocol

For laboratory free dwells, define
F_j=exp[-i d_j(H_{j-1}+E_B)] and retain the same fixed event lifts.
Total-energy intertwining implies

\[
\widetilde W_jF_j\cdots\widetilde W_1F_1
=e^{-it_j(H_j+E_B)}\widetilde W_j\cdots\widetilde W_1,
\qquad t_j=\sum_{r=1}^j d_r. \tag{5}
\]

For normalized nonbridge branches in the common CAR gauge, the last product
is the lift of identity from H_0 to H_j. Removing the final battery-only
unitary inside a partial trace leaves the same formula (2), with
U_s=exp(-i t_j H_s). At j-minus use H_s=H_{j-1}; at j-plus use H_s=H_j.
This is also valid for the battery-energy expectation, which commutes with
the removed free battery unitary. The first j-minus control is unchanged.

Equation (5) was derived and the comparison specified before its numerical
execution. Both protocols retain the same packet, pulse, edges and dwell
durations. Neither derives event occurrence or clock control. The two
reduced-state formulas differ physically; moving to an interaction picture
requires transforming the event controls as well as naming that picture.

## Sufficient coherence resource for the controlled dwell protocol

The exact target of this theorem is: under the supplied D_j tensor I_B
protocol, every finite set of strict ideal observable margins is preserved
by a sufficiently wide, explicitly priced sine packet, for arbitrary
initial matter state. This is a sufficient bound, not an optimal battery
or a search over actual transport outputs.

At a fixed prefix let A=H_s, U=U_s,
C=A-U H_0 U^dagger, delta=(lambda_max(C)-lambda_min(C))/2,
kappa=||[A,C]||, and omega(O)=(lambda_max(O)-lambda_min(O))/2 for
Hermitian O. Then

\[
|\operatorname{Tr}O(\rho_{s,w}-U\rho_0U^\dagger)|
\le\frac{\pi^2}{w^2}\omega(O)(\kappa+2\delta^2). \tag{6}
\]

To prove (6), set C(tau)=exp(-i tau A) C exp(i tau A) and
rho(tau)=V_s(tau) rho_0 V_s(tau)^dagger. Differentiation gives
rho'=-i[C(tau),rho]. For f(tau)=Tr O rho(tau),

\[
f''(\tau)=\operatorname{Tr}\rho(\tau)
\left([[A,C(\tau)],O]-[C(\tau),[C(\tau),O]]\right).
\]

Subtract scalar centers from C and O in these commutators. Operator-norm
submultiplicativity then gives |f''| <= 2 omega(O)(kappa+2 delta^2).
The sine packet has an even Fourier probability density and
integral tau^2 |beta_hat(tau)|^2 d tau = ||beta'_w||_2^2 = pi^2/w^2.
Its linear Taylor term integrates to zero. Integrating the uniform second
derivative remainder proves (6). The compactly supported sine lies in H1;
its endpoint derivative discontinuity does not invalidate this second
moment. No fourth moment is needed.

An entirely analytic bound avoids numerical operator-norm estimation.
After k deleted edges, telescope the deletion intertwining defects, each
of norm at most t. Dwells commute with the current Hamiltonian, so
||C|| <= kt and ||A|| <= (L-k)t. Hence

\[
\kappa+2\delta^2\le 2kLt^2,\qquad
|\Delta\langle O\rangle_s|
\le\frac{2\pi^2 kLt^2\omega(O)}{w^2}. \tag{7}
\]

Here L=12 and t=1. At j-minus, k=j-1; at j-plus, k=j. For density
omega(n_v)=1/2, and for unit-strength signed bond current omega(J_e)=1.
The first j-minus bound vanishes exactly. For energy, the safe bound
omega(H_s) <= L-k suffices.

For each required current, density or energy witness let m>0 be a
certified ideal slack and c the corresponding coefficient in (7).
Choose w once so that w^2 > max(c/m). Then every selected margin remains
strictly positive. Four distinct current witnesses at each j-minus surface
preserve the original support count. A separately selected front current
preserves the original front threshold. Fixed-N variational nonnegativity
holds for every positive state in that sector and needs no margin.

This price is explicit: support [24,24+w], initial mean 24+w/2 and cap
[0,48+w]. These resources belong to the wider packet, not the frozen
width-one test. The theorem does not promise an added post-event current
gate unless the ideal protocol itself has the needed strict margins.
For the free-battery protocol, the broad-packet limit instead uses
exp(-i t_j H_s); (6)-(7) as stated target the controlled ordered-dwell
protocol and are not silently transferred to that different ideal limit.

### Exact rational ideal margins and sufficient widths

The independent [ideal-margin certificate](../scripts/native_edge_record_transport_ideal_margin_certificate_2026_09_07.py)
uses the eight-mode covariance rather than the primary's 70-dimensional
fixed-N construction. It verifies h_0^2=3I exactly, so the half-filled
ground covariance is C_0=(I-h_0/sqrt(3))/2. The negative spectrum has
multiplicity four because Tr h_0=0. It applies the same phase pulse and
ordered dwells to this covariance.

All scientific enclosure calculations use integers and exact fractions.
An integer-square-root bracket encloses sqrt(3) in an interval of width
10^-24. Each exponential uses its degree-30 Taylor polynomial P and
the norm remainder

\[
r\le\frac{x^{31}}{31!}\frac1{1-x/32},\qquad
x=|d|\,\|h\|_{\rm bound}<32.
\]

Here ||h|| <= 3 for every remaining hopping matrix and the pulse generator
has norm one. If epsilon bounds covariance error before an approximate
unitary step, then

\[
\epsilon'\le(1+r)^2\epsilon+r(2+r),
\]

because the true covariance is an orthogonal projector of norm one and
||P|| <= 1+r. The resulting enclosures are below 10^-22 at every prefix.
Current error is at most 2 epsilon, density error at most epsilon, and
energy error at most 2q epsilon with q live bonds. Printed decimals are
rounded down; width selection uses the exact fractions.

| Prefix | Certified pre-current slack | Certified post-current slack | Certified density slack |
|---:|---:|---:|---:|
| 1 | >= 0.0605543062 | >= 0.0605543062 | >= 0.0253038929 |
| 2 | >= 0.2362774875 | >= 0.0114396402 | >= 0.0993008023 |
| 3 | >= 0.0492056499 | >= 0.0492056499 | >= 0.1903481533 |
| 4 | >= 0.1732355474 | >= 0.1732355474 | >= 0.2731483199 |
| 5 | >= 0.1376858185 | >= 0.1376858185 | >= 0.2472171339 |

Each current entry is a lower bound on the fourth-largest ideal current
magnitude minus 0.02. The front witness is edge 3 at the second j-minus
surface, with slack >= 0.2062774875 above 0.05. The initial and every
post-event energy are certified below -10^-6; the intervening pre-event
energies inherit the preceding energy through a commuting dwell. In the
ideal CAR identification, deletion does not change the state, so each
listed density margin applies both before and after that deletion.

Using (7) and the elementary upper bound pi^2 < 16 gives the sufficient
resource prescriptions below. They were calculated from the exact ideal
slacks before any actual calculation at these widths.

| Guaranteed controlled-protocol tests | Sufficient width | Initial support | Initial mean | Cap |
|---|---:|---|---:|---:|
| Original pre-event current/front tests, both density surfaces and all-prefix negative energy | 125 | [24,149] | 86.5 | 173 |
| The same tests plus post-event surviving-current support | 260 | [24,284] | 154 | 308 |

The limiting inequalities are the third pre-event current for width 125
and the second post-event current for width 260. These are conservative
sufficient widths, not minimum requirements or empirical fits. The
width-one records remain separate observations.

## Frozen protocol results

The primary fixed-N spectral-group contraction and independent eight-mode
finite-frequency calculation agree on the following support counts. The
independent checker also reconstructs its own 70-dimensional Slater/CAR
state to contract the battery moment directly. It imports no primary code
or cache. No battery width, phase pulse, edge or dwell was searched against
the actual outcomes.

| Dwell protocol and packet width | j-minus support counts | j-plus support counts | Largest selected front current magnitude | Original pre-event test | Added post-event test |
|---|---|---|---:|---|---|
| Controlled, w=1 | (7,6,5,0,2) | (0,5,6,5,5) | 0.135911 | FAIL | FAIL |
| Laboratory free, w=1 | (7,6,5,4,5) | (0,5,7,1,4) | 0.134999 | PASS | FAIL |
| Controlled, w=125 | (7,6,4,6,7) | (6,5,4,6,6) | 0.255986 | PASS | PASS |
| Controlled, w=260 | (7,6,4,6,7) | (6,5,4,6,6) | 0.256209 | PASS | PASS |

All four cases satisfy the stated pre/post density window, all-prefix
negative-energy test, fixed-N variational bound and spectral cap. The
width-125 post-event result is an additional observation; the independently
derived sufficient prescription for that stronger test remains width 260.

| Dwell protocol and width | Initial battery mean | Final directly contracted battery mean | Final matter energy |
|---|---:|---:|---:|
| Controlled, w=1 | 24.5 | 22.192208 | -3.598118 |
| Laboratory free, w=1 | 24.5 | 22.159009 | -3.564919 |
| Controlled, w=125 | 86.5 | 84.177983 | -3.583893 |
| Controlled, w=260 | 154 | 151.677942 | -3.583852 |

The initial matter energy is -5.905910 in every case. Unrounded numerical
total-energy drifts are below 2e-12 in the reported primary and independent
runs. This agreement is a floating-point cross-check of the exact
termwise conservation proof, not an interval proof of each decimal.
The exact-rational certificate establishes the ideal slacks and sufficient
width guarantees independently of these actual-width numbers.

The first j-minus surface reproduces the original dwell in both conventions.
Immediately after the first event, the width-one calculations have zero
surviving bonds above the declared 0.02 threshold. Their later j-minus
counts differ under the two specified free-evolution rules. Thus the
pre-event and post-event results must remain separate; no bound on every
instant between sampled surfaces is asserted.

## Proof obligations and evidence boundary

| Obligation | Evidence route | Status in this draft |
|---|---|---|
| Nonstationary retained-battery prefix formula | Fourier-fiber cancellation and spectral expansion (1)-(2) | Derived above |
| Overlap and direct battery energy | Exact interval integral and symmetry (3)-(4) | Derived above |
| Cap refusal, fixed N and old Records | Spectral support and parent nonbridge sector algebra | Conditional on parent carrier |
| Free-battery prefix identity | Total-energy intertwining (5) | Derived above |
| Finite sufficient coherence width | Uniform curvature, Fourier second moment and defect telescoping (6)-(7) | Derived above |
| Frozen transport and density diagnostics | Independent 70-dimensional and eight-mode computations | Outcomes agree; finite numerical evidence |
| Spatially local autonomous apparatus | Explicit local dilation with priced resources | Open constructive target |

## No-Go Discipline Gate

The scientific outputs are a conditional construction, a sufficient
resource theorem and observed finite-fixture outcomes. A universal no-go
interpretation is rejected. The following record applies the repository's
negative-claim discipline without pretending that untested routes are closed.

**N1 — Alternative routes.** Five materially different ways to pursue the
downstream apparatus/transport task are: retain the battery with controlled
dwells (ATTEMPTED here), include laboratory free battery evolution
(ATTEMPTED here), supply a wider coherent packet with an analytic error bound
(ATTEMPTED here), construct a local energy-exchanging collision reservoir
(UNTESTED here), and replace the prescribed event schedule with an autonomous
head/fuel generator (UNTESTED here). The first three have the explicit
formulas and computations above. The latter two are constructive tasks,
not exclusions. No route is marked RULED OUT BY PRIOR: the unratified parent
notes cannot supply that authority. Thus the five-closed-route requirement
for a broad no-go is not met, and no such claim is submitted. The width-one
table reports its measured currents; it does not quantify over all apparatuses.

**N2 — Dependency relations.** The five premise rows above are not presented
as independent walls. Preparation and apparatus phase control may be
implemented by a common controller; schedule and event occurrence may be
supplied by one generator; carrier selection is upstream of both. Closing
any one of those implementation questions has no asserted implication for
the others. There is no numerical wall count in the theorem or headline.

**N3 — Hidden conditions.** Re-reading the proof identifies the common CAR
identification, nonbridge isometries, product battery preparation, chosen
dwell convention and finite spectral bound as load-bearing conditions.
Each is explicit in the premise account or proof. The exact-rational
certificate uses free-fermion quadratic dynamics and the supplied sea;
that hypothesis is stated where its covariance formula is introduced.
No phrase about a canonical or standard construction substitutes for a
framework derivation.

**N4 — Residual matching.** The instrument parent supplies the carrier,
nonbridge branch algebra and energy lift. The transport parent supplies
the fixed protocol and its observable thresholds. Neither is cited as
a witness excluding apparatus transport. This note computes the joined
nonstationary process directly. There are zero prior no-go witnesses to
count or inherit.

**N5 — Resolution.** Individual live-bond current expectations and site
densities are evaluated on the eight-site, N=4 fixture. Finite spectral
modes are used to evaluate its conditional channel. Five specified event
prefixes are compared. No spatially infinite lattice, arbitrary event
sequence or continuum limit is executed. The primary output carries the
matching resolution statements. These finite observations carry no
lattice-wide exclusion.

**N6 — Partial closure.** The current axiom/primitive registry supplies no
numerical packet width in this calculation; width follows from the displayed
conditional theorem and certified ideal slack. The difference between
controlled and free dwells is a physical control specification, not a new
axiom proposal. A convention alone does not implement either control, but
neither construction asks for an axiom or primitive amendment. Existing
instrument and transport parents remain explicit upstream inputs.

**N7 — Steelman against an overbroad negative reading.** A reviewer should
reject any claim that this battery prevents viable Record transport:
the controlled width-one table is only one preparation and control
protocol. Free battery evolution changes the exact prefix map through
energy intertwining, and (6)-(7) give a concrete wider-packet route with
certified positive ideal margins. Those are actionable counterarguments
within the supplied apparatus model. This note pursues them and reports
their separate resource and control premises.

**N8 — Prior-cycle comparison.** The parent transport note explicitly left
the physical apparatus task open, while the parent instrument note
constructed the shared lift and restricted its simpler reduced-state
comparison to stationary full inputs. The present calculation extends
that input treatment and tests the downstream fixture. Their open tasks
are not treated as retained impossibility results. The branch-local
route search also found no earlier joined nonstationary transport
calculation on this frozen fixture as of the campaign's pinned main.

Disposition: retain the conditional positive theorem and finite
observations; reject the broader no-go framing. The unfinished local
reservoir and autonomous-generator routes remain constructive next work.

## Review record and reproducibility

Independent cold proof and code reviews found no blocking mathematical
defect in equations (1)-(7), the rational enclosure, or the two finite
representations. The code reviewer additionally integrated a nonstationary
two-level joint wavefunction directly in battery energy, retaining the
laboratory free phase. Density differences were below 1.3e-15 and direct
battery-energy differences below 5e-14. The reviewers used GPT-6-Astra at
low reasoning, following the user's setting. The final comparison interface passed incremental review, including malformed
and failed subprocess controls. Initial repository pipeline, strict lint and
changed-evidence readiness passed; final landing checks are recorded in the
campaign review packet. This source-side
record does not set an audit grade.
The load-bearing runners are the declared primary, the independent
one-particle/fixed-N checker, and the exact-rational ideal-margin certificate.
All use a declared 180-second timeout. The primary and rational certificate
have 180 MiB execution ceilings; the independent checker declares 256 MiB.

The required claim-scoped helper registration is a hard landing condition:

~~~python
"native_edge_record_shared_battery_transport_bounded_theorem_note_2026-09-07": [
    "scripts/native_edge_record_shared_battery_transport_independent_check_2026_09_07.py",
    "scripts/native_edge_record_transport_ideal_margin_certificate_2026_09_07.py",
],
~~~

It belongs in `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
`docs/audit/scripts/build_citation_graph.py`. The current
`audit_science_fingerprint.py` contains the owner-approved claim-scoped
registry normalization; every other builder byte remains governed. The
review approved the additive mapping. Root integration verified its exact
installation, preservation of every other registration, and unchanged
governed builder fingerprint
`235e8b82fd460d29f0798f13df129d2f896aa31d4c14566f179e200dc6194c5b`.
Parent dependencies must be part of the reviewed
landing tree. No audit ledger or effective-status surface is an author output.

Canonical caches are generated only through
`scripts/runner_cache.py` `execute_and_write_cache`, using each runner's
declared timeout and final source bytes. The exploratory experiment source
and its machine-written `nonzero_exit` receipt from commit `c1b7b95e8a`
are preserved unchanged under
`.claude/science/physics-loops/record-battery-transport-20260907/primary/historical/`.
That invocation recorded three unmet width-one physical thresholds and zero
numerical failures; it is not relabeled as successful evidence.

The reviewed remedy gives the final primary a comparison-validation
contract: numerical validity, the proved wider-packet requirements, and
live agreement with the independently implemented checker on all forty
prefix surfaces. The three width-one threshold failures remain printed
as benchmark outcomes. Malformed or missing checker output, a failed
checker execution, or a numerical disagreement is a validation failure.
The primary's declared input closure binds the checker source bytes.
A new receipt for this new contract is separate from the historical
failed experiment receipt. Physical benchmark outcomes and successful
comparison validation must not be conflated.
