#!/usr/bin/env python3
"""Cycle903 focused controls; full finite comparisons execute through primary."""
from pathlib import Path
from hashlib import sha256
import time_readout_6009_independent as arithmetic
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/SIGMA_TERMINAL_THETA_CORE_EMPTY_CYCLE903_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_readout_6009_algebra.py', 'scripts/time_readout_6009_walks.py', 'scripts/time_readout_6009_independent.py')
INPUT_SHA256 = {'docs/SIGMA_TERMINAL_THETA_CORE_EMPTY_CYCLE903_BOUNDED_THEOREM_NOTE_2026-07-28.md': '5a88b8bdb56b2f75e5de7669f2f3640c03d219caa45075fb0061ece6a016b12c', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'd364eb166bb24588f219d4e43b364b4897551bac8ddb93b1a586c28a58f40e4b', 'scripts/time_readout_6009_algebra.py': '774824bf82119ba34e838831c7e5fa373f883416268063560bbce246f56b7fb0', 'scripts/time_readout_6009_walks.py': '367a63de4a0d43882f86ff8e5b2ae218290ca584611fd40f4f1fd69f589e6794', 'scripts/time_readout_6009_independent.py': 'b2b682742681fe00851e69853af7d740acf7531aa23c89a6387c6e2d7a23a4f4'}
def input_guard():
    root=Path(__file__).resolve().parents[1]
    for p,h in INPUT_SHA256.items():
        if sha256((root/p).read_bytes()).hexdigest()!=h:raise RuntimeError(f'missing or changed input: {p}')

def confirm(result):
    input_guard()
    return arithmetic.confirm(903,result)
def main():
    input_guard()
    checks=arithmetic.controls(903)
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))
if __name__=='__main__':raise SystemExit(main())
