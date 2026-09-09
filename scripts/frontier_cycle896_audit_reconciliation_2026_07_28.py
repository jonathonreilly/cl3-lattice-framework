#!/usr/bin/env python3
"""Cycle896 bounded corrected finite evidence; no physical or audit verdict."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
import time_readout_6009_algebra as algebra
import time_readout_6009_walks as walks
import frontier_cycle896_audit_reconciliation_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/AUDIT_FLAGS_RECONCILED_CYCLE896_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_readout_6009_algebra.py', 'scripts/time_readout_6009_walks.py', 'scripts/time_readout_6009_independent.py', 'scripts/frontier_cycle896_audit_reconciliation_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/AUDIT_FLAGS_RECONCILED_CYCLE896_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'c291515186412b13b1ddb912de814927dd63f3e23c4ef83a9aaeebaf1ca3134b', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'd364eb166bb24588f219d4e43b364b4897551bac8ddb93b1a586c28a58f40e4b', 'scripts/time_readout_6009_algebra.py': '774824bf82119ba34e838831c7e5fa373f883416268063560bbce246f56b7fb0', 'scripts/time_readout_6009_walks.py': '367a63de4a0d43882f86ff8e5b2ae218290ca584611fd40f4f1fd69f589e6794', 'scripts/time_readout_6009_independent.py': 'b2b682742681fe00851e69853af7d740acf7531aa23c89a6387c6e2d7a23a4f4', 'scripts/frontier_cycle896_audit_reconciliation_independent_check_2026_07_28.py': 'b1e8cb63a7ad511a74f0821b012f07760bd7aa1dcd7f36727e6403c8296d862a'}
def input_guard():
    root=Path(__file__).resolve().parents[1]
    for p,h in INPUT_SHA256.items():
        if sha256((root/p).read_bytes()).hexdigest()!=h:raise RuntimeError(f'missing or changed input: {p}')

def main():
    input_guard()
    result=algebra.reconciliation_results()
    checks=independent.confirm(result)+[('supplied chart arithmetic',result['declared_chart_counts']==[8,10] and result['orbit_sum']==27 and result['augmented_label_sum']==30),('finite invariant counts',len(result['window_orbits'])==16 and result['linear_C3_invariant_dimension']==1)]
    print(json.dumps(result,sort_keys=True))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))
if __name__=='__main__':raise SystemExit(main())
