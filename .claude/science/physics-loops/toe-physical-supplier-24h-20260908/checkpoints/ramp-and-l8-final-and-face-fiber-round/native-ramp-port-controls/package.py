from pathlib import Path
import shutil,json,hashlib
w=Path('/private/tmp/toe-native-same-hamiltonian-ramp-20260908');p=w/'.claude/science/physics-loops/native-same-hamiltonian-ramp-20260908';p.mkdir(parents=True,exist_ok=True)
base=Path('/private/tmp/toe-24h-probes-20260908')
for d in ['native-same-hamiltonian-ramp-root','native-same-hamiltonian-ramp-cold-proof','native-ramp-initial-ice-control','native-ramp-initial-ice-cold-review','native-ramp-port-controls','native-ramp-port-cold-review']:
 shutil.copytree(base/d,p/'originals'/d,ignore=shutil.ignore_patterns('__pycache__','originals','package.py','*.pdf'),dirs_exist_ok=True)
helper='native_same_hamiltonian_ramp_jets_2026_09_08.py';shutil.copy2(base/'native-ramp-port-controls/check.py',w/'scripts'/helper)
header=r'''---
claim_id: native_same_hamiltonian_ramp_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "Supplied smooth ramp of the full native Hamiltonian from bare ice, followed by a fixed natural ring time: volume-independent O(epsilon^2) local expectation comparison to ring dynamics from the original ice density matrix, for dressed final observables."
upstream_dependencies:
  - native_local_natural_ring_dynamics_note_2026-09-08
runner: scripts/native_same_hamiltonian_ramp_2026_09_08.py
---

# Same-Hamiltonian ramp and the original ice initial state

**Date:** 2026-09-08  
**Type:** bounded_theorem  
**Status:** conditional-support

A smooth change of the coefficient of the supplied native Hamiltonian prepares the required effective ice sector without a separately programmed dressing unitary. After a fixed number of natural ring-time units, dressed local expectations agree with ring evolution of the **original** supplied ice density matrix to $O(\epsilon^2)$, uniformly in volume. This is neither cooling nor a ground-state preparation theorem.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Same-Hamiltonian ramp, supplied bare ice and dressed final readout."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## Precise theorem and dependencies

Use the full carrier, even periodic cubic extents at least four, native $A_e$, strong-support norm and homological gauge of the [local natural-ring theorem](NATIVE_LOCAL_NATURAL_RING_DYNAMICS_NOTE_2026-09-08.md), including its [full-carrier mechanism](NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md), [dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) and [instrument](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md) dependencies. There is no fixed magnetic-cycle or winding sector, and no hard low-charge projection.

Write $H/U=D+\epsilon V$, $V=\sum_e b_eA_e$, real $|b_e|\leq1$, $U>0$, $\epsilon>0$. For each fixed local $O_X$, each finite $\tau_*>0$, all sufficiently small $\epsilon$ and every ice-supported density matrix $\rho_0$, the ramp below followed by a hold of duration $\tau/(U\epsilon^4)$, $0\leq\tau\leq\tau_*$, satisfies

\[
\left|\operatorname{Tr}(\rho_{\mathrm{lab,end}}Y_{14}^{\dagger}O_XY_{14})
-\operatorname{Tr}(\rho_0e^{i\tau J_4}O_Xe^{-i\tau J_4})\right|
\leq C_{X,\tau_*}\|O_X\|\epsilon^2.
\]

The constants and sufficient small-coupling radius depend on the fixed profile, order and geometry, not on volume or $U$. $Y_{14}$ is the static endpoint frame and $J_4$ the parent's signed fourth-cycle operator, including extent-four winding cycles. For a bare final observable the additional dressing cost is $O(\epsilon)$. No global trace-norm, global isolated-band or phase conclusion is implied.

'''
# Preserve complete reviewed arguments as source sections; notation in original prose is retained where readable.
r=(base/'native-same-hamiltonian-ramp-root/DERIVATION.md').read_text();r=r[r.index('## Protocol'):r.index('## Primary prior art')]
i=(base/'native-ramp-initial-ice-control/DERIVATION.md').read_text();i=i[i.index('## Correct joint grading'):i.index('## Evidence and scope')]
footer='''
## Evidence, provenance and remaining imports

The live standard-library runner checks 18,626 exact predicates: arbitrary-profile sparse Fraction jets through order four, normalized beta14 endpoint flatness, time exponents and literal full-L4 two-edge supports. Three actual isolated `-OO` mutants fail: reversed moving-frame sign, omitted derivative terms and deletion of the derivative-driven second generator. All are tested against the correct transformed generator. No blanket odd-order deletion mutant is claimed discriminating where the tested coefficient vanishes. Finite controls support, but do not replace, the local analytical proof.

Complete original root and independent ramp proofs, original extension, original SymPy evidence, source-bound reviews and raw failures are preserved in the [durable packet](../.claude/science/physics-loops/native-same-hamiltonian-ramp-20260908/REVIEW_HISTORY.md). The standard-library port changes representation, not the arbitrary-profile mathematical target. No third-party PDF is vendored.

Time-dependent local frame methods are standard. Ho and Abanin, [primary paper](https://arxiv.org/abs/1611.05024), provide contextual prior art on slowly ramped Floquet systems; their theorem is not imported to establish this result. The root research record reports reading Sections I–II.B (PDF pages 1–4). This port does not assert a new full-paper reading or historical novelty.

The Hamiltonian, common-coupling control, schedule, initial ice state and final dressed readout remain supplied. The moving frame is an analytical device rather than an additional preparation operation. Nothing here selects couplings, an occurrence law, physical time, a ground state, a Coulomb phase or an electromagnetic interpretation.
'''
(w/'docs/NATIVE_SAME_HAMILTONIAN_RAMP_NOTE_2026-09-08.md').write_text(header+r+'\n## Replacing the effective ramp state by the original state\n\n'+i+footer)
