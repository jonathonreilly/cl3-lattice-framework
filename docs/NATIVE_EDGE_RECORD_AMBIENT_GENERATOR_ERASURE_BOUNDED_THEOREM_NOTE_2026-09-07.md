---
claim_id: native_edge_record_ambient_generator_erasure_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional common native edge-qubit, local fuel and one-head generator; exact CPTP erasure of chronological system copies; capped sign-summed code invariance and timed physical-trajectory equivalence. The energy lift and Markov reservoir remain supplied apparatus."
upstream_dependencies:
  - native_edge_record_autonomous_head_shared_battery_bounded_theorem_note_2026-09-07
  - native_edge_record_occupation_feedback_shared_battery_bounded_theorem_note_2026-09-07
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_edge_record_ambient_generator_erasure_2026_09_07.py
---

# A present-state native generator suffices for the supplied Record laws

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is conditional-support; independent audit is
unset. This construction removes the explicit chronological system register
from two previously supplied generators. It preserves their physical
trajectory instruments. It does not derive either generator from the axioms
or remove the environmental record and its physical resource obligations.

## Question, dependencies and supplied roles

The [complete Record law](NATIVE_EDGE_RECORD_AUTONOMOUS_HEAD_SHARED_BATTERY_BOUNDED_THEOREM_NOTE_2026-09-07.md)
and [occupation-feedback law](NATIVE_EDGE_RECORD_OCCUPATION_FEEDBACK_SHARED_BATTERY_BOUNDED_THEOREM_NOTE_2026-09-07.md)
were calculated in a direct sum of chronological sectors. A history-indexed
projector is not a local physical control. Here the present fuel mask, head
and actual edge Records supply the controls, using the
[native carrier](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md).

Native edge-qubit preparation, one fuel qubit per edge, a one-excitation head
register, their placement, hopping coefficients, fuel gap, coherent energy
battery, absorbing refusal flag, external time and a GKSL reservoir remain
supplied. The bath can retain chronological edge/sign/time outcomes even
when the system no longer contains a separate copy of their order. No
entropy, reset, replenishment or indefinite formation theorem is supplied.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Explicit physical operator construction and CPTP generator/instrument intertwiner, with a native finite-matrix witness."
trace_class: upstream_support
target_claim_id: native_edge_record_autonomous_head_shared_battery_bounded_theorem_note_2026-09-07
target_blocker_text: "Replace chronological system controls by present native local degrees of freedom."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Quantify spatial truncation and finite-battery approximation of this ambient generator."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

## Common ambient Hamiltonian and native seeds

Let q_e be the live-fuel projector and f_e its lowering operator. At vertex v
let d_v lower the head qubit. The prepared one-head subspace is invariant;
there is no one-head projector multiplying the Hamiltonian. For a directed
edge e=(v,w), write M_vw=d_w^dagger d_v. On the common tensor product define

\[
A=\sum_e q_e(h_e+\Delta I),\qquad h_e=a_eT_e,\quad |a_e|\le t.
\]

The head Hamiltonian is zero. Each h_e is the **whole** native hopping,
including the terms needed to preserve N. For Delta>=t, positivity of every
summand gives 0<=A<=L(Delta+t), where L is the number of fuel edges. This
finite-volume spectral enclosure is an extensive bound; it is not a
volume-independent resource estimate.

Use the physical projectors Q_ez=(I+zZ_e)/2. The two bare laws are

\[
B_{vw,z}=M_{vw}f_eQ_{e,z}q_e,
\qquad B^{\rm fb}_{vw,z}=M_{vw}f_eQ_{e,z}J_{vw}q_e,
\]

with the explicit native even operator

\[
J_{vw}=T_e n_v(1-n_w),\qquad n_v=(I-B_v)/2.
\]

The native relations give T_e^2=(I-B_v B_w)/2 and exchange the two single
endpoint-occupation projectors. Thus J^dagger J=n_v(1-n_w), [J,N]=0 and
Z_eJ=-JZ_e on the ambient native algebra. On each faithful source code,
J=c_w^dagger c_v. This uses T_e itself, not division by the possibly zero
coefficient a_e. The new Q acts **after** J; reversing them swaps its sign.
Bridge branches keep the actual parity projector, without another fair-sign
factor.

On the one-head subspace the sign-summed effects are respectively

\[
\sum_z B_{vw,z}^\dagger B_{vw,z}=n_v^{\rm head}q_e=:E_{vw},
\qquad
\sum_z (B^{\rm fb}_{vw,z})^\dagger B^{\rm fb}_{vw,z}
=E_{vw}n_v(1-n_w).
\]

On the unrestricted head tensor product, M_vw^dagger M_vw also contains
(1-n_w^head). The simplification above is only on the invariant prepared
one-head subspace. No global chronology is consulted by these seeds.

## Legal-code invariance includes the summed loss

Present data alpha consists of live mask R, head v and old signs z_(R^c).
Its native code P_alpha imposes those old Z values and the live-graph cycle
checks. It depends on the present data, not the order of past deletions.
In that fuel block A restricts to H_R+|R|Delta. Each whole surviving hopping
and each eligible J preserves the source code and N. Q_ez maps it into the
correct new code, including when e is a bridge.

Forward branch invariance alone would not establish GKSL code invariance:
an individual Q_ez^dagger Q_ez need not preserve the **old** source code.
The necessary statement concerns the sign-summed loss, including after a
battery cap.

Lift a bare seed by the common ambient energy:

\[
V=\sum_{a,b}\Pi_A(b)B\Pi_A(a)\otimes T_{a-b}.
\]

The lift preserves its fuel/head routing. Let S=P_cap V P_cap. In the
source/target fuel blocks, the target Hamiltonian A_out omits h_e and hence
commutes with Z_e. In the pullback sum over signs, the two adjacent target
energy projectors collapse to the same b. Therefore

\[
\sum_z Q_{e,z}\Pi_{A_{out}}(b)Q_{e,z}=\Pi_{A_{out}}(b).
\]

The remaining battery factor depends on a,a',b, but not z. Every remaining
native factor, including J when present, commutes with the source code.
Consequently sum_z S_z^dagger S_z preserves that code. This proves the
no-jump and anticommutator part as well as the recycling part. Old guarded
Records remain stable after their fuels are spent; the target Hamiltonian
preserves the newly written Z value.

For the complete law use one eligibility complement per directed edge,

\[
F_{vw}=\left(E_{vw}-\sum_zS_{vw,z}^\dagger S_{vw,z}\right)^{1/2},
\]

with an absorbing active/refused flag and the same source Hamiltonian in
the refusal copy. This is positive because E_vw commutes with A and the
full-line complete column has effect E_vw. It is zero on ineligible sectors;
the full identity must not replace E_vw there. Code invariance extends to F
by functional calculus. The feedback law instead uses its actual compressed
effect in the GKSL anticommutator, without an identity-rate completion.

Every exact lifted or matched refusal jump intertwines the modeled total
energy. With a finite cap, the bounded generator consequently conserves
every bounded Borel function of that energy. The battery Hilbert space in
this statement remains continuous even though its energy interval is bounded.

## Exact erasure of chronological system copies

Let s denote an old chronological sector and W_s embed its actual native code
into the common physical fuel/head/Record/flag sector. Different orders can
have overlapping or identical images. Define

\[
\mathcal C(\rho)=\sum_s W_s\rho_{ss}W_s^\dagger.
\]

This is CPTP: its Kraus operators have orthogonal **input** history blocks,
and each W_s is an isometry. Orthogonal output images are unnecessary.
For every history transition s->u of physical label ell=(v,w,z), native
restriction and the common spectral lift give

\[
W_u L_{s,\ell}=L_\ell W_s,\quad AW_s=W_s A_s,
\quad D W_s=W_sD_s,\qquad D=\sum_\ell L_\ell^\dagger L_\ell.
\]

The last identity uses the summed-loss proof above. Summing recycling,
anticommutator and free terms yields
C composed with G_history = G_ambient composed with C. The same identities
hold separately for the no-jump semigroup and each physical edge/sign jump
instrument. Starting in the declared definite sector, all timed trajectory
probabilities and their physical conditional states therefore agree.

More generally, the channel intertwiner kills cross-history blocks, which
do not feed recycling diagonals in the separately labelled history model.
This does not claim equivalence for an invented coherent sum of historical
amplitudes. When orders merge, their physical density matrices add; the
ambient generator acts linearly on that mixture. Consistent physical W_s
embeddings also fix dictionary phases; no extra path-dependent phase is
silently discarded.

Erasure is not reversible. On a square, opposite complete tours can return
the head with the same spent fuels and Record signs. On safe support their
Record-only bare Q products commute, so equal accumulated dwell time gives
the same **normalized** physical conditional state. An old order-register
observable can still distinguish the histories. That order remains readable
from the environmental trajectory record, not necessarily the final system.

Complete timed Kraus amplitudes also contain
exp[-gamma sum_l degree_l dwell_l/2]. Equal total time does not fix this
scalar. The equality of normalized states must not be strengthened to an
equality of timed probability densities. Unsafe intermediate cap projections
and noncommuting feedback paths do not inherit the safe Record-only product
identity.

## Independent native matrix witness

The runner assembles the ambient lift with grouped energy projectors and
literal battery-index writes, independently of its imported source-code lift.
It compares all capped source columns on the physical four-edge square,
opposite dimer Hamiltonian and34-level ladder. Eight branch restrictions
cover the complete and feedback laws, initial and old-Record/bridge sectors.
It checks native J identities, recycling, summed loss, free terms,
anticommutator and complete-law refusal effects.

An individual capped-loss code leakage is0.353553390593274, whereas the
sign-summed leakage is below5e-16. Thus the code cancellation is nontrivial.
The witness also propagates two actual four-event merging trails stage by
stage, using a native N2 input coherent between safe total energies19 and20.
Equal total time1 gives equal normalized outputs, but the timed probability
ratio is exp(-0.3). Changing accumulated time by1 gives retained-state trace
norm distance2sin(0.5), confirming that the total-energy phase remains physical.
Incorrect coherent addition of histories gives a nonzero density error.

The independent scientific payload contains417new checks and72on-demand
imported carrier assertions, with largest residual below4e-15. The parent
main and its full census are not rerun. This is a square/dimer native witness,
not a full-cube numerical computation or a local reservoir construction.

## Physical locality and next obligation

In doubled cubic coordinates, a whole hopping has endpoint-star support
of radius2 and diameter4. Co-locating its fuel at the edge midpoint retains
that range; head qubits occupy the endpoint vertices. Bare seeds therefore
have bounded physical support, and A is a finite-range ambient interaction
without a hidden global history or code projector multiplying its terms.

The exact energy lift still uses all Fourier times of conjugation by A.
The local bare construction alone does not make that dressed operation
finite-range. A spatial truncation needs a quantified retained-battery error;
a continuous capped battery still needs a finite-dimensional realization or
an approximation theorem. Those are the next constructive obligations.
Covariant one-site admissibility, a physical bath and renewed blank fuel/
Records remain open. The present theorem retires chronological **system**
storage under the supplied laws and establishes their common local bare
algebra, with the stated remaining apparatus assumptions.

## No-Go Discipline Gate

The [source-linked scope record](../.claude/science/physics-loops/record-autonomous-head-20260907/ambient-erasure/NO_GO_DISCIPLINE_CHECKLIST.md)
keeps the positive construction, finite noninvertibility example and open
alternatives separate. Heavy negative-packet five-family PASS is not asserted.
No general impossibility of local apparatus or sustained formation follows
from the order-erasure example.
