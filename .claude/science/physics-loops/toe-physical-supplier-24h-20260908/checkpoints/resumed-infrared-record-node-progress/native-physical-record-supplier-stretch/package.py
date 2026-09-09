from pathlib import Path
import json,hashlib,shutil
S=Path(__file__).parent;W=Path('/private/tmp/toe-native-charged-record-histories-20260909');P=W/'.claude/science/physics-loops/native-charged-record-histories-20260909';P.mkdir(parents=True,exist_ok=True);(P/'ORIGINAL').mkdir(exist_ok=True)
for n in ['DERIVATION.md','DERIVATION_BEFORE_REFINEMENT_QUALIFIER.md','REFINEMENT_CORRECTION.md','FIRST_TARGET.md','SOURCES.json','FREEZE.json','check.py','second_check.py','RESULT.json','SECOND_RESULT.json','STATUS.md']:shutil.copyfile(S/n,P/'ORIGINAL'/n)
s=(S/'check.py').read_text().replace('def main():\n','def check():\n global count\n count=0\n');a=s.index(" (P/'RESULT.json')");s=s[:a]+' return r\n';s=s.replace("'predicates':count","'predicates':count")
# No output/alarm side effects in helper. Keep exact functions and fixed fixtures.
(W/'scripts/native_charged_record_history_controls_2026_09_09.py').write_text(s)
s=(S/'second_check.py').read_text();a=s.index('for i in range(3):');b=s.index("r=dict(status='PASS'");head=s[:a];body=s[a:b];s=head+'def check():\n global checks\n checks=0\n'+''.join(' '+l+'\n' for l in body.splitlines())+" return {'status':'PASS','checks':checks,'scope':'three-mode exact CAR and two-qubit rational controls'}\n";(W/'scripts/native_charged_record_history_car_2026_09_09.py').write_text(s)
proof=(S/'DERIVATION.md').read_text();proof=proof.replace('Prospective theorem, before the finite controls.','Finite conditional theorem, supported by the exact controls reported below.');proof=proof.replace('K_f^b K_e^a = (-1)^[ab(w_ef+w_fe)] K_e^a K_f^b,','K_(G−e),f^b K_G,e^a = (-1)^[ab(w_ef+w_fe)] K_(G−f),e^a K_G,f^b,');proof=proof.replace('where both sides identify the same final output ordering.','where each K is defined using the graph indicated in its subscript, with inherited neighbor orders, and both sides identify the same final output ordering.');proof=proof.replace('Novelty scope is limited:8038 already maps the effect and8037/main already give selected fixed-code instruments.','Scope relative to prior work: the dictionary parent already maps the effect and the native instrument parent already gives fixed-code instruments.');proof=proof.replace('If a prior source contains these formulas, the result should be treated as a reconstruction rather than a new milestone.','No literature-priority claim is made.')
front='''---
claim_id: native_charged_record_histories_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied full native edge carrier and Record instrument: local gauge-frame correction, charged history maps, projective order phases and transported matter observables. No formation-law or Born selection."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_charged_record_histories_2026_09_09.py
---

**Status:** conditional-support. **Type:** bounded_theorem.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: supplied native carrier, phase convention and Born/Lueders Record instrument
trace_class: frontier_discovery
reachability_to_target: supports
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

The load-bearing parents are the [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md) and the [native Record instrument](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md). This branch is stacked on the actual unmerged dictionary revision86e03ef9; latest main was inspected for overlap, not imported as generated audit state. The construction adds no physical site factor. It does not supply a preferred placement, initial state, event law or control pulse.

'''
end='''

## Permanent outcome register and finite evidence

An instrument retains an abstract classical outcome label a with each branch. The physical recorded edge retains its fixed value; deleting its factor is a mathematical representation of the surviving degrees of freedom, not erasure of a permanent Record. A comparison that forgets a finer label is a channel on mathematical output descriptions, not a physical reversal of formation. Charged sectors with different boundary signs must remain distinguished by those labels. The positive-Gauss correction may be used as a frame change without claiming it is a physical gauge-invariant pulse on the old graph.

The primary runs416 exact one-edge full-carrier columns and736 two-edge history columns on a triangle, a path and a chorded square, with both neighbor orders. Omitting the local phase fails80 columns. The52609 structural predicate visits include repeated M-symmetry checks; they are not independent physical cases. A separate146-control exact CAR/refinement calculation checks endpoint particle-hole conjugation, transported number, and the distinction between dephasing and discard. These finite fixtures support the implementation; the displayed general algebra proves the arbitrary finite-graph statement. No large numerical dynamics or empirical experiment is used.

The initial derivation's insufficiently qualified refinement sentence is preserved with its correction in the packet. A binary |+> density matrix explicitly distinguishes forgetting a Z outcome from doing nothing. Full state-action equality is never inferred from scalar marginalization. Current physical formation locality remains open even after this finite supplier interface is constructed.
'''
(W/'docs/NATIVE_CHARGED_RECORD_HISTORIES_NOTE_2026-09-09.md').write_text(front+proof+end)
