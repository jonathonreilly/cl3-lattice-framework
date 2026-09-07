---
claim_id: native_edge_record_autonomous_head_shared_battery_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional time-homogeneous native Record head/fuel generator with a retained continuous energy battery, complete bridge instruments and absorbing cap refusal. Exact modeled energy-distribution conservation and nonnegative nonselective battery drift on an invariant safe domain. Complete four-event path-conditioned event-epoch transport calculation on the frozen signed cube; finite observed support failures and graph-only trapping census. Supplied carrier, preparation, spectral apparatus and irreversible Markov law remain explicit premises."
upstream_dependencies:
  - native_edge_record_shared_battery_transport_bounded_theorem_note_2026-09-07
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_edge_record_autonomous_head_shared_battery_2026_09_07.py
---

# A fixed native Record head with fuel and one retained energy battery

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is **conditional-support**. Independent audit is
unset. The theorem constructs and evaluates a supplied generator; it does not
derive a formation law from the framework axioms.

## Target and premises

The [shared-battery transport result](NATIVE_EDGE_RECORD_SHARED_BATTERY_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-07.md)
uses a prescribed edge list and dwell durations. Here one fixed generator
chooses the next incident live edge and its waiting time. The
[native instrument](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
supplies the physical Record/code maps, including bridges. Both dependencies
remain provisional conditional premises. Their source-side independent checks
support the implications used here; they have not received a new audit grade.

~~~yaml
packet_helper_runner:
  - scripts/native_edge_record_autonomous_head_orbital_check_2026_09_07.py
  - scripts/native_edge_record_autonomous_head_native_ladder_check_2026_09_07.py
  - scripts/native_edge_record_autonomous_head_ablation_diagnosis_2026_09_07.py
  - scripts/native_edge_record_autonomous_head_ablation_orbital_check_2026_09_07.py
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Explicit conditional generator, energy identities and complete finite transport calculation."
trace_class: upstream_support
target_claim_id: native_edge_record_shared_battery_transport_bounded_theorem_note_2026-09-07
target_blocker_text: "Supply autonomous formation/renewal and a physical energy apparatus on this same carrier."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Separate clock averaging from battery dephasing, then attack a spatially local implementation or renewal mechanism."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

| Supplied premise | Exact role | Remaining derivation |
|---|---|---|
| Native edge carrier, CAR dictionary and Record instrument | Finite Hilbert spaces and branch maps | Physical selection and formation mechanism |
| Half-filled phase-pulsed sea | Initial matter state | Preparation and its resource account |
| Definite head, twelve live fuels and degenerate history labels | Legal routing sectors | Formation of the role scaffold and memory |
| Positive fuel gap and coherent continuous battery | Energy exchange | Preparation and spatially local apparatus |
| Rate gamma, external time and GKSL law | Event occurrence and waiting law | Physical reservoir, entropy accounting and renewal |

Removing the edge/dwell schedules leaves these premises. A time-homogeneous
open-system law is the meaning of autonomous used here. No closed finite
unitary realization, nearest-neighbor realization, entropy-free operation,
indefinite transport or TOE closure follows.

## Fixed generator and energy theorem

Let s label a legal history, head v, live-edge set R and compatible native
Record code. Histories and head labels have zero Hamiltonian. Each live edge
carries one fuel of energy Delta. The sector Hamiltonian is

\[
A_s=H_R+|R|\Delta I,\qquad H_R=\sum_{e\in R}h_e,\qquad\|h_e\|\le t.
\]

For a live edge e=(v,w), the native instrument maps K_(s,e,z) move the head
to w, spend that edge's fuel and append its Record. The two target sectors
are orthogonal. They obey sum_z K_z^*K_z=I and preserve particle number and
old Records. A nonbridge has K_z=J_z/sqrt(2), with J_z an isometry. A bridge
has the signed component-parity projector from the native parent; inserting
another fair-sign factor there is incorrect.

On the full-line battery let T_u|E>=|E+u>. Define, using **full** sector energies,

\[
V_z=\sum_{a,b}\Pi_{s'}(b)K_z\Pi_s(a)\otimes T_{a-b}.
\]

Thus, when a and b instead denote matter energies, the shift is a-b+Delta.
The fuel contribution occurs once. For total sector energy A_s+E_B,

\[
(A_{s'}+E_B)V_z=V_z(A_s+E_B),\qquad \sum_zV_z^*V_z=I.
\]

The second identity follows in Fourier fibers from
Y_z(tau)=exp(-i tau A_(s')) K_z exp(i tau A_s), including bridge branches.

Cap the battery with P=`1_[0,C](E_B)`. Let S_z=P V_z P and, per eligible
source/edge pair (s,e), form **one** F_(s,e)=(I-sum_z S_z^*S_z)^(1/2),
where I is the capped source-sector identity, into an absorbing copy with
the same Hamiltonian. Caps commute with energy; S_z intertwine total energy,
and F commutes with source total energy. Therefore the completed column is
trace preserving and preserves every bounded Borel function of total energy.
Separate complements for each sign would give the wrong total rate.

In the common orthogonal direct sum set L_(s,e,z)=sqrt(gamma) S_z and include
sqrt(gamma) F for each eligible edge. Add the free total-Hamiltonian term.
There are finitely many legal histories on this finite graph; the cap is
continuous, hence still infinite dimensional. The resulting bounded GKSL
generator satisfies

\[
\mathcal L^*(f(H_{\rm total}))=0
\]

for every bounded Borel f. This is conservation of the entire modeled energy
distribution, not just its first moment. Refusal copies have no outgoing
jumps. Same total Hamiltonian does not imply that a refusal separately leaves
matter and battery energies unchanged.

## Safe support and positive battery drift

If Delta>=t, then 0<=A_s<=L(Delta+t)I for L initial edges. This follows by
summing 0<=Delta I+h_e<=(Delta+t)I, without requiring commuting hoppings.
Initial battery support [b,b+w] gives total support within
[b,b+w+L(Delta+t)]. Intertwining confines the battery at every prefix to
[b-L(Delta+t), b+w+L(Delta+t)]. Choose the cap to contain that interval.
Explicitly, with M=L(Delta+t), the common total-energy projector
`Q=1_[b,b+w+M](H_total)` is invariant. The full-line outgoing battery support
of Q is within [b-M,b+w+M], so S_z Q=V_z Q and F_(s,e) Q=0. This also
specifies the correlated-input safe domain used below.

For the frozen L=12, Delta=t=1 packet [48,49], this sharper sufficient
enclosure is [24,73], inside cap [0,97]. The original preregistration used
the weaker symmetric norm bound and is unchanged. As an analytical resource
bound only, a translated preparation [24,25] would fit cap [0,49]; no such
replacement is used in the reported experiment and neither bound is optimal.

On a legal input code, all surviving hoppings commute with the measured
physical Z_e. Consequently sum_z K_z^* A_(s',z) K_z equals the input-code
compression of H_R-h_e+(|R|-1)Delta I. Its difference from A_s is
Delta I+h_e>=0. With Fourier convention exp(+i tau E), E_B=-i d/dtau,

\[
\sum_z[-iY_z^*Y_z']
=e^{-i\tau A_s}(\Delta I+h_e)e^{i\tau A_s}\succeq0.
\]

Integrating this fiber expectation proves nonnegative **sign-summed mean**
battery increment for arbitrary joint matter-battery input, including
correlations, on the invariant safe domain. Free dwells leave E_B unchanged.
Summing over eligible edges gives nonnegative ensemble drift for the supplied
generator. This is not monotonicity for individual measured battery energies
or every conditioned bridge outcome. The claim is not extended to cap-unsafe
inputs: the refusal operator need not commute with E_B separately.

## Waiting law and complete path census

On a safe definite head/mask sector, sum_(e,z) L^*L=gamma d_R(v) I. The wait
is exponential with rate gamma d_R(v), and each live incident edge has
conditional probability 1/d_R(v). There is no matter-dependent rate in this
particular law. A degree-zero head traps; its probability is retained.

Use the eight-vertex cube, ordered edges and hopping coefficients of the
shared-battery parent, hopping t=1, N=4, and initial pulse
exp[-i0.7(n_0-n_1)] on its half-filled sea. Preregistered parameters are
head0, gamma=Delta=1, twelve live fuels, sine battery
sqrt(2)sin(pi(E-48)) on [48,49], mean48.5, cap[0,97]. The four-event
analysis horizon is not a counter in the generator.

Exact enumeration gives 3,6,12,24 prefixes through events1..4, full mass1
at each depth. Every such prefix remains connected, so all its deletions
are nonbridges. Every four-event edge path has probability1/24, waiting
rates(3,2,2,2), and16 fair-sign histories of probability1/384 each.

The graph-only continuation, summing complete sign instruments without
assuming fair bridge signs, terminates in186 edge trails:

| Terminal event count | Trails | Probability |
|---|---:|---:|
| 5 | 6 | 1/8 |
| 6 | 12 | 1/8 |
| 7 | 48 | 11/32 |
| 8 | 60 | 1/4 |
| 9 | 60 | 5/32 |

This includes all trap mass. It is a finite depletion result for this graph
and routing rule, not an impossibility theorem for other formation laws.

## Event-epoch states and independent battery moments

Condition on an edge path. Exact intertwining moves all free dwells to the
final side of the retained joint instrument. In the nonbridge CAR gauge the
matter state is exp(-iT H_R) sigma_R exp(iT H_R), where sigma_R is the
zero-dwell reduction using the same retained battery, never a reset battery.
At event j-minus include j waits and j-1 deletions; at j-plus include j waits
and j deletions. The head at j-minus is the source of the selected edge.

In final energy coordinates, event-epoch averaging multiplies element(b,b') by
product_l r_l/(r_l+i(E_b-E_b')). These are path-conditioned averaged states.
They are neither fixed laboratory-time ensembles nor guarantees for every
realized wait. Thresholds are applied to their mean currents; averages of
absolute currents or of threshold indicators would be different statistics.

For shifts u=a-b+kDelta and v=a'-b+kDelta, the direct battery first-moment
kernel is [48.5+(u+v)/2]K_1(u-v). Initial-energy coherences a,a' are retained.
The primary contracts the actual joint state with this kernel, then compares
its result with the energy ledger.

The independent checker diagonalizes only8-mode orbital Hamiltonians. It
uses Slater determinant overlaps over the70 four-particle occupation subsets
to construct p_B(E)=sum_J|sum_I D_(JI) A_I beta(E-u_(JI))|^2 and integrates
E p_B(E) directly over translated packet intervals. It independently averages
the one-body matrix against the convolution density of the exponential waits,
with tail bound P(T_4>20)<9.73e-15 and two quadrature families/refinements.
The reduced state is a mixture of Slater states, generally not Gaussian.
This reduction is used only for the verified first-four nonbridge domain.

## Finite transport result

The inherited comparator requires four live edges with |mean J_e|>=0.02 at
every pre-event surface, at least one selected pre-event front current of
magnitude>=0.05 along the complete path, densities in[0.1,0.9], and negative
post-event matter energy. Post-event current support is an additional
diagnostic. There are90 path-prefix/side surfaces; repeated ancestral states
are intentionally represented under each selected next edge.

| Event | Pre support range | Post support range | Largest selected pre front |
|---|---:|---:|---:|
| 1 | 5 | 0..6 | 0.210516 |
| 2 | 0..3 | 1..3 | 0.004303 |
| 3 | 2..4 | 0..5 | 0.085398 |
| 4 | 0..1 | 0..2 | 0.019027 |

All24 complete paths pass the **maximum-along-path** front criterion and
all24 fail the pre-support criterion. A low front current at an individual
later event is not a failure of the maximum-along-path criterion. All density,
particle-number, negative matter-energy and energy-ledger checks pass.
Seventy-one of90 individual surfaces fail support>=4; these are surfaces,
not71 independent trajectories.

At the fourth post-event epoch, path-weighted matter energy is
-3.988522230596 and directly computed battery energy is50.582612399697.
Eight fuel units remain. Together these equal initial matter energy
-5.905909830899 plus initial battery48.5 plus initial fuel12, within numerical
tolerance. All90 primary/checker comparisons agree below2e-12.

The separate native finite witness constructs physical16-dimensional Pauli
code sectors on a square and an actual34-level battery. It checks108 native
mask/sign/edge cases, all head positions, joint refusal, a reachable
nonbridge-to-deterministic-bridge sequence on one energy20 fiber, and every
total-energy spectral indicator. This commensurate dimer witness checks
implementation; it does not replace the continuous cube theorem or assert a
finite-dimensional realization of its irrational energy shifts.

## Evidence and next discriminator

Primary and both independent checks are linked through the runner/helper
mapping and canonical runner-cache receipts. Mutation controls cover path
mass, gap sign, mean-rate substitution, omitted pre-wait, wrong masks, battery
reset, fuel omission/doubling, bridge normalization, separate refusal, Record
and N corruption, and malformed live comparison evidence. Numerical
quadrature agreement is convergence evidence, not exact roundoff certification.

The observed support failure is not a universal no-go. A preregistered matched
comparison holds all paths and the input fixed. A is the actual channel with
event waits; B is the finite retained battery with zero waits; C is the formal
ideal-coherence channel with event waits; D is ideal coherence with zero waits.
The ideal cases set the overlap kernel to one: they are not normalized
finite-energy battery preparations. Zero waits are endpoint comparisons, not
another realization of the declared finite-rate generator.

| Surface | Prefixes | A support passes | B | C | D |
|---|---:|---:|---:|---:|---:|
| pre1 | 3 | 3 | 3 | 3 | 3 |
| post1 | 3 | 2 | 3 | 3 | 3 |
| pre2 | 6 | 0 | 6 | 4 | 6 |
| post2 | 6 | 0 | 6 | 6 | 4 |
| pre3 | 12 | 8 | 12 | 12 | 8 |
| post3 | 12 | 6 | 12 | 12 | 6 |
| pre4 | 24 | 0 | 24 | 24 | 12 |
| post4 | 24 | 0 | 20 | 18 | 10 |

All360 surfaces and96 trajectory front values were independently reproduced.
Complete-path pre-support passes are0/24,24/24,16/24,12/24 respectively; all
four cases pass the maximum-along-path front and density tests. The nearest
unrounded current magnitude to the0.02 threshold is more than2.45e-5 away.

At pre4, removing either finite-battery dephasing or wait averaging restores
support on every path. Removing both restores only half. The effects are
nonadditive: mixing and evolution can redistribute current onto additional
live edges. In D the state remains the prepared state and only the list of
live observables changes, so its support loss is precisely deletion of
initially carrying edges. This is not an additive decomposition of A's losses.
Energy exhaustion and cap refusal do not explain A's failed comparator:
fuel remains, refusal is zero and its allowed edge rate stays gamma.

Reality of H does not force finite positive-time averaged currents to vanish.
Complex input coherences and generally complex Laplace factors remain.
Infinite Cesaro averaging for nondegenerate real H would leave a real
diagonal energy state and zero bond currents. Degenerate complex blocks can
survive and carry stationary current; that limiting argument is not used for
this degenerate finite event-epoch calculation.

The next route couples Record formation to an actual directed matter hop,
rather than this matter-independent head hazard. It is a different supplied
law whose rates, dark states and conditioned energy budgets must be derived
anew. Any proposed physical upgrade
must then confront the supplied global energy lift, irreversible reservoir,
state preparation and finite-record depletion. Energy conservation alone
does not resolve those obligations.

## No-Go Discipline Gate

The [source-linked N1-N8 scope review](../.claude/science/physics-loops/record-autonomous-head-20260907/NO_GO_DISCIPLINE_CHECKLIST.md)
records three real work families and open alternatives. It does **not** claim
the heavy negative-claim packet PASS: five closed route families are not
established. The submitted result is a positive conditional theorem with
finite comparator observations and a partial attempt on general formation.
This submission limitation does not disprove the conditional mathematics;
no universal impossibility claim or future audit verdict is proposed.
