#!/usr/bin/env python3
"""Cycle903 bounded corrected finite evidence; no physical or audit verdict."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
import time_readout_6009_algebra as algebra
import time_readout_6009_walks as walks
import frontier_cycle903_sigma_theta_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/SIGMA_TERMINAL_THETA_CORE_EMPTY_CYCLE903_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_readout_6009_algebra.py', 'scripts/time_readout_6009_walks.py', 'scripts/time_readout_6009_independent.py', 'scripts/frontier_cycle903_sigma_theta_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/SIGMA_TERMINAL_THETA_CORE_EMPTY_CYCLE903_BOUNDED_THEOREM_NOTE_2026-07-28.md': '5a88b8bdb56b2f75e5de7669f2f3640c03d219caa45075fb0061ece6a016b12c', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'd364eb166bb24588f219d4e43b364b4897551bac8ddb93b1a586c28a58f40e4b', 'scripts/time_readout_6009_algebra.py': '774824bf82119ba34e838831c7e5fa373f883416268063560bbce246f56b7fb0', 'scripts/time_readout_6009_walks.py': '367a63de4a0d43882f86ff8e5b2ae218290ca584611fd40f4f1fd69f589e6794', 'scripts/time_readout_6009_independent.py': 'b2b682742681fe00851e69853af7d740acf7531aa23c89a6387c6e2d7a23a4f4', 'scripts/frontier_cycle903_sigma_theta_independent_check_2026_07_28.py': 'ec8a1163d59b6f514653f850a216bce5d62350800fc73ffbcc4598611f0750e7'}
def input_guard():
    root=Path(__file__).resolve().parents[1]
    for p,h in INPUT_SHA256.items():
        if sha256((root/p).read_bytes()).hexdigest()!=h:raise RuntimeError(f'missing or changed input: {p}')

def main():
    input_guard()
    result={'action':algebra.action_results(),'incidence':walks.interference_results()}
    checks=independent.confirm(result)+[('actual mixed-seed masses',result['incidence']['mixed_seed_control']['mass_theta0']=='1' and result['incidence']['mixed_seed_control']['mass_theta1']=='1/2'),('original finite incidence', [len(r['theta_moving']) for r in result['incidence']['barriers'][:4]]==[7,1,0,7]),('product action and involution property',len({tuple(r['actions']) for r in result['action']['product_rows']})==1 and result['action']['off_product5']!=result['action']['product_rows'][0]['actions'] and all(not(r['preserves_sum'] and r['sum_constant_on_fixed_set']) for r in result['action']['involutions']))]
    print(json.dumps(result,sort_keys=True))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))
if __name__=='__main__':raise SystemExit(main())
