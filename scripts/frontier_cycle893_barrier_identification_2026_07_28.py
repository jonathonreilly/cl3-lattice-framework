#!/usr/bin/env python3
"""Cycle893: bounded original-fixture calculation after explicit scope repair."""
import json
from pathlib import Path
from hashlib import sha256
import time_windows_6009_model as model
import frontier_cycle893_barrier_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/BARRIER_IDENTIFICATION_TESTED_CYCLE893_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_windows_6009_model.py', 'scripts/time_windows_6009_independent.py', 'scripts/frontier_cycle893_barrier_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/BARRIER_IDENTIFICATION_TESTED_CYCLE893_BOUNDED_THEOREM_NOTE_2026-07-28.md': '789ab4a4b754d0942d82bfef4cbdd06e49923c7cb41158f93ab634263e50edf4', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'scripts/time_windows_6009_model.py': '2f8e20e3af19821decf986f8e125282eed54e0ecc9826d61b872f2dd0a0b8c2f', 'scripts/time_windows_6009_independent.py': 'f8396cf2f96bb40146b996908178de4d23ecd0d6795659d9d4151e0c7f5245cf', 'scripts/frontier_cycle893_barrier_independent_check_2026_07_28.py': '1c240a2cc5f4b9ae6352b6a5db010c50c2d7a15970c1cf265d3ca8902a3e7bee'}

def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,expected in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=expected:
            raise RuntimeError(f"missing or changed input: {path}")

def main():
    input_guard()
    result=model.barrier_results()
    checks=independent.confirm(result)
    original=[result[n] for n,_ in model.BARRIERS];admitted=[r for r in original if r['finite_map_checks']['finite_filter']]
    checks += [('all31 original and6 checker barrier rows retained',len(result)==37),('original finite filter count',len(admitted)==24),('original finite quadratic range',{len(r['partition']) for r in admitted}=={4,5,6,7,8}),('conditional containment forbids positive-length support landings',all(not r['contains_support'] or r['positive_length_support_landings']==0 for row in result.values() for r in row['configurations']))]
    print(json.dumps(result,sort_keys=True,default=str))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))

if __name__=='__main__':raise SystemExit(main())
