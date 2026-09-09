#!/usr/bin/env python3
"""Cycle894: bounded original-fixture calculation after explicit scope repair."""
import json
from pathlib import Path
from hashlib import sha256
import time_windows_6009_model as model
import frontier_cycle894_interface_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/FIXED_SET_AND_CONFIGURATION_BRIDGE_RESTRICTIONS_CYCLE894_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_windows_6009_model.py', 'scripts/time_windows_6009_independent.py', 'scripts/frontier_cycle894_interface_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/FIXED_SET_AND_CONFIGURATION_BRIDGE_RESTRICTIONS_CYCLE894_BOUNDED_THEOREM_NOTE_2026-07-28.md': '4a3e85a323f8742ee480e24ffbb18900a2c2ee6b5ea289565724e7dead12f72d', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'scripts/time_windows_6009_model.py': '2f8e20e3af19821decf986f8e125282eed54e0ecc9826d61b872f2dd0a0b8c2f', 'scripts/time_windows_6009_independent.py': 'f8396cf2f96bb40146b996908178de4d23ecd0d6795659d9d4151e0c7f5245cf', 'scripts/frontier_cycle894_interface_independent_check_2026_07_28.py': 'dd79d7a0e05e954b2b033a2a83722c42add7936424da464a3deb6aa05f10e8df'}

def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,expected in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=expected:
            raise RuntimeError(f"missing or changed input: {path}")

def main():
    input_guard()
    result=model.bridge_results()
    result['synthetic_weightings']=model.synthetic_weighting_profile()
    checks=independent.confirm(result)
    checks += [('actual fixed target-set witness',result['fixed_set_witness']['contains_both_supports'] and result['fixed_set_witness']['masses']==['0','1']),('full original ratio grid',result['grid_cells']==648 and all(r['total_pairs']==36 for r in result['per_configuration'].values())),('original restricted ratio incidence',len(result['restricted_bridge_rejected_configurations'])==7),('original synthetic zero counts, not878 identity',[v['zero_atoms'] for v in result['synthetic_weightings']['weightings'].values()]==[0,0,73088,73088,76184])]
    print(json.dumps(result,sort_keys=True,default=str))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))

if __name__=='__main__':raise SystemExit(main())
