#!/usr/bin/env python3
"""Cycle885: bounded original-fixture calculation after explicit scope repair."""
import json
from pathlib import Path
from hashlib import sha256
import time_windows_6009_model as model
import frontier_cycle885_gbw1_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/GBW1_RECORD_WINDOW_CYCLE885_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_windows_6009_model.py', 'scripts/time_windows_6009_independent.py', 'scripts/frontier_cycle885_gbw1_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/GBW1_RECORD_WINDOW_CYCLE885_BOUNDED_THEOREM_NOTE_2026-07-28.md': '1d6c08d5cafd27e09d666e3bdd2f068752cd72cfe6682288b4143bd6de6ad195', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'scripts/time_windows_6009_model.py': '2f8e20e3af19821decf986f8e125282eed54e0ecc9826d61b872f2dd0a0b8c2f', 'scripts/time_windows_6009_independent.py': 'f8396cf2f96bb40146b996908178de4d23ecd0d6795659d9d4151e0c7f5245cf', 'scripts/frontier_cycle885_gbw1_independent_check_2026_07_28.py': '330e5b424fe8f4323c1e900b341ac8814836ea3a51723e7790950240a24a9488'}

def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,expected in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=expected:
            raise RuntimeError(f"missing or changed input: {path}")

def main():
    input_guard()
    result=model.window_results()
    checks=independent.confirm(result)
    checks += [('original support equivariance',result['finite_map_checks']['support']['equivariance_failures']==0),('original fixed-cube translation failures',result['finite_map_checks']['constant_cube']['equivariance_failures']==1152 and result['finite_map_checks']['constant_cube']['rotation_only_failures']==0),('original boundary retractions',result['finite_map_checks']['boundary_shell']['monotonicity_failures']==24),('original centre and boundary theta counts',len(result['centre_disagreement_configurations'])==4 and len(result['boundary_theta_moving'])==7),('support mass is exact zero-step seed mass',all(r['support_mass']==r['seed_mass_on_support'] and r['positive_length_landings_on_support']==0 for r in result['support_seed_rows']))]
    print(json.dumps(result,sort_keys=True,default=str))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))

if __name__=='__main__':raise SystemExit(main())
