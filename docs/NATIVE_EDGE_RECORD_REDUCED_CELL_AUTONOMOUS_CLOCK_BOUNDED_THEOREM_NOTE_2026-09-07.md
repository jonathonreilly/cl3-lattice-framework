---
claim_id: native_edge_record_reduced_cell_autonomous_clock_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
claim_scope: "Conditional finite autonomous clock for the full reduced-cell native sign/refusal isometry, preserving original free evolution and exact energy, with ready-input joint/system error bounds on a finite completion window. Static multi-site interactions, preparation and observation timing remain supplied; recurrence is explicit."
upstream_dependencies:
  - native_edge_record_reduced_cell_full_isometry_bounded_theorem_note_2026-09-07
runner: scripts/native_edge_record_reduced_cell_autonomous_clock_2026_09_07.py
---

# Finite autonomous clock for the native reduced-cell operation

**Date:** 2026-09-07
**Type:** bounded_theorem
**Status:** proposed_retained

Actual current-surface status is conditional-support; independent audit is unset.
A supplied static Hamiltonian executes the [complete reduced-cell sign/refusal operation](NATIVE_EDGE_RECORD_REDUCED_CELL_FULL_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md) exactly at time 1, retaining original free evolution. Throughout [0.99,1.01], its joint ready-input channel error is below 1/20 against the displayed completed-clock reference; after tracing the clock the error is below 1/1000. There are 27 reduced registers and interactions supported on at most five sites. The finite system recurs at time 2.

~~~yaml
packet_helper_runner:
  - scripts/native_edge_record_reduced_cell_autonomous_clock_check_2026_09_07.py
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact circuit-clock gauge construction with a finite-binomial completion-window certificate, actual native all-input isometry and independent sparse joint-Hamiltonian verification."
trace_class: upstream_support
target_claim_id: native_edge_record_reduced_cell_full_isometry_bounded_theorem_note_2026-09-07
target_blocker_text: "Replace the externally switched pulse sequence with an explicit finite autonomous controller and price its completion window."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Justify physical interaction locality and role preparation; distinguish finite completion from permanent Record formation and renewal."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
~~~

## Gauge and exact solution

Let U1,...,U9 be the actual native all-input pulse unitaries, U10,...,U17=I, and Wj=Uj...U1. Define D=sum_j |j><j| tensor Wj. D is unitary and gauges the clock hopping:

    Hc = D(Hpath tensor I)D†,
    Hpath_(j+1,j) = g sqrt((j+1)(17-j)).

All native Uj commute with K as full operators, so [D,K]=[Hc,K]=0. Therefore evolution under K+Hc from clock0 is

    sum_j a_j(t)|j> tensor exp(-itK)Wj psi.

This identity holds for every input, including reference entanglement, not only a selected native state.

For an elementary derivation of a_j, take17 virtual spins with Hamiltonian g sum X. In the normalized permutation-symmetric state with j ones, its matrix element to j+1 is g sqrt((j+1)(17-j)). The product rotation of all-zero spins gives

    a_j(t)=sqrt(binomial(17,j))cos(gt)^(17-j)(-i sin(gt))^j.

The virtual spins are a derivation of the18-dimensional clock matrix, not additional physical resources. At g=pi/2,t=1 only j=17 remains, with phase(-i)^17. Since W17=W9 and W9 restricted to ready inputs is V, the output is exactly |17> tensor exp(-iK)V psi up to global phase. The free evolution is not compensated or silently removed.

## Full-input retained and discarded clock bounds

Let eta(t)=sum_(j<9)|a_j|² and p=1-eta. For p>0 define the normalized completed-clock vector chi_t=p^(-1/2)sum_(j>=9)a_j|j>. It depends on time and the clock couplings, not on the input. The actual pure output has overlap sqrt(p) with chi_t tensor exp(-itK)V psi for every normalized ready-input psi and arbitrary reference. Orthogonality of clock positions proves this without a bound on individual native prefixes. Thus the joint trace-norm distance is exactly 2sqrt(eta) for every pure input; purification/contractivity gives the same upper bound on the ready-input channel diamond norm. This is not an unrestricted initial-clock diamond norm.

After tracing the clock, the channel is a mixture of prefix channels. The completed terms sum to p times the target; remaining terms have total weight eta. Hence the system-only diamond error is at most 2eta. No postselection or normalization of a native outcome is used. The normalized chi_t is only the comparison state's clock factor; the actual clock is retained unmeasured.

Missing steps17-j have binomial mean17cos²(gt). Unfinished j<9 implies17-j>=9, so

    eta <= (17/9)cos²(gt)
        = (17/9)sin²(g(t-1))
        <= 17pi²/360000 < 1/2000

for |t-1|<=1/100. With pi<22/7, the displayed upper bound is exact rational arithmetic. Consequently2sqrt(eta)<1/20 and2eta<1/1000. These are conservative sufficient bounds, not optimized clock length or window.

## Resources, energy and locality

There are 18 one-hot clock registers plus the 9 reduced native registers, total 27 qubits, initially with one clock excitation at0. The natural static Hamiltonian is a sum of clock-exchange terms tensor the specific native Uj and their adjoints. Each Uj has support on at most 3 native sites, so each Hermitian term has support at most 5 sites including two clock sites. This is a supplied multi-site complete-connectivity interaction, not a nearest-neighbor primitive or a compiled two-site realization.

On the invariant one-hot clock sector, ||Hc||=17pi/2<27, maximum coupling=9pi/2<15, and ||K+Hc||<=17pi/2+11/2<33. These are legal-sector bounds. On the full 27-qubit register space the natural sum of clock exchanges remains a well-defined local-support Hermitian extension, conserves clock excitation and K, and has the coarse bound ||Hc||<=sum g_j<255, hence ||K+Hc||<261. It does not require a global one-hot projector or an inert extension to exist. Its behavior on unused clock sectors is not the claimed computation.

Both K and total energy K+Hc are conserved. The interaction Hamiltonian is part of the actual autonomous model; no energy-cost or formation derivation follows from giving its norm. Static engineered position-dependent couplings, the exact Uj coefficients, supplied roles, pure ready clock and native preparation remain physical inputs. Observation within the stated window is still a supplied timing condition, though no external sequence of nine switching pulses occurs.

## Recurrence and numerical scope

At t=2 the clock returns 0 with phase(-1)^17 and W0=I; the circuit has coherently undone its completed native operation up to free evolution. Thus the completed label is not permanently locked in this closed model. Padding supplies a finite retention window, not irreversibility or renewal.

The runner revalidates the actual native 163 exact assertions, then independently exponentiates the 18x18 path and compares amplitudes/spectrum to the analytic construction, including both window endpoints and recurrence. It checks the exact rational inequalities and resource bounds. It does not allocate or simulate the full 2^27 apparatus. Native all-input equality plus the gauge proof supplies the arbitrary-input/reference statement; small-matrix agreement alone is not a numerical diamond-norm certificate.

The [independent literal native-clock helper](../scripts/native_edge_record_reduced_cell_autonomous_clock_check_2026_09_07.py) constructs the sparse 4,608-dimensional joint Hamiltonian, folding only the unchanged old sentinel. It checks all eight ready-input columns and their full 144-column gauge embedding, original free-energy commutation, and direct joint evolution at the two window endpoints, exact arrival and recurrence. Its 56 clock checks are separate from 62 revalidated native-isometry checks. The two canonical runners pass unchanged 180-second and 180-MiB limits and declare all source dependencies. Small matrix residuals support the analytic proof; they are not measured diamond norms.

The [N1–N8 discipline checklist](../.claude/science/physics-loops/record-autonomous-clock-20260907/NO_GO_DISCIPLINE_CHECKLIST.md) records the supplied inputs, partial closure and explicit heavy negative-packet NOT PASS.
