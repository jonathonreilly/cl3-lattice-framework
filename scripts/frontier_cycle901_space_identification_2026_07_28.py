#!/usr/bin/env python3
"""Cycle901 bounded corrected finite evidence; no physical or audit verdict."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
import time_readout_6009_algebra as algebra
import time_readout_6009_walks as walks
import frontier_cycle901_space_identification_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/SPACE_IDENTIFICATION_DECIDED_FDIM_CYCLE901_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_readout_6009_algebra.py', 'scripts/time_readout_6009_walks.py', 'scripts/time_readout_6009_independent.py', 'scripts/frontier_cycle901_space_identification_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/SPACE_IDENTIFICATION_DECIDED_FDIM_CYCLE901_BOUNDED_THEOREM_NOTE_2026-07-28.md': '49a62033c8a866f8880d104d0afa1be0249e6e5717e516b8fa76b69499413538', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'd364eb166bb24588f219d4e43b364b4897551bac8ddb93b1a586c28a58f40e4b', 'scripts/time_readout_6009_algebra.py': '774824bf82119ba34e838831c7e5fa373f883416268063560bbce246f56b7fb0', 'scripts/time_readout_6009_walks.py': '367a63de4a0d43882f86ff8e5b2ae218290ca584611fd40f4f1fd69f589e6794', 'scripts/time_readout_6009_independent.py': 'b2b682742681fe00851e69853af7d740acf7531aa23c89a6387c6e2d7a23a4f4', 'scripts/frontier_cycle901_space_identification_independent_check_2026_07_28.py': 'c9fd63e6d383bd868bce92bc108afd92b807a69508bb7ca3995f5188c72c6146'}
def input_guard():
    root=Path(__file__).resolve().parents[1]
    for p,h in INPUT_SHA256.items():
        if sha256((root/p).read_bytes()).hexdigest()!=h:raise RuntimeError(f'missing or changed input: {p}')

def main():
    input_guard()
    result=algebra.scope_results()
    checks=independent.confirm(result)+[('all cubic subgroup domain rows',len(result['subgroups'])==30 and sum(r['normal_plane_value']=='1/8' for r in result['subgroups'])==9),('finite seven-form filter',sum(r['anchor']=='2/9' and r['scope_constant'] and r['total'] for r in result['forms'])==1),('actual scope distinction',any(r['simply_transitive'] and r['value']=='5/16' for r in result['scope_ladder']) and any(r['simply_transitive'] and r['value'] is None for r in result['scope_ladder']))]
    print(json.dumps(result,sort_keys=True))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))
if __name__=='__main__':raise SystemExit(main())
