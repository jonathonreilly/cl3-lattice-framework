#!/usr/bin/env python3
"""Cycle898 bounded corrected finite evidence; no physical or audit verdict."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
import time_readout_6009_algebra as algebra
import time_readout_6009_walks as walks
import frontier_cycle898_escape_census_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/ESCAPE_CENSUS_COVERAGE_CYCLE898_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_readout_6009_algebra.py', 'scripts/time_readout_6009_walks.py', 'scripts/time_readout_6009_independent.py', 'scripts/frontier_cycle898_escape_census_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/ESCAPE_CENSUS_COVERAGE_CYCLE898_BOUNDED_THEOREM_NOTE_2026-07-28.md': '8d685e960926ad41b37e91d44c2826644c2058edb12435db57836500b1ad1b2e', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'd364eb166bb24588f219d4e43b364b4897551bac8ddb93b1a586c28a58f40e4b', 'scripts/time_readout_6009_algebra.py': '774824bf82119ba34e838831c7e5fa373f883416268063560bbce246f56b7fb0', 'scripts/time_readout_6009_walks.py': '367a63de4a0d43882f86ff8e5b2ae218290ca584611fd40f4f1fd69f589e6794', 'scripts/time_readout_6009_independent.py': 'b2b682742681fe00851e69853af7d740acf7531aa23c89a6387c6e2d7a23a4f4', 'scripts/frontier_cycle898_escape_census_independent_check_2026_07_28.py': 'f07d137017a19ff5753bed46ab5039328a89984d8129e3943274c1be1999f165'}
def input_guard():
    root=Path(__file__).resolve().parents[1]
    for p,h in INPUT_SHA256.items():
        if sha256((root/p).read_bytes()).hexdigest()!=h:raise RuntimeError(f'missing or changed input: {p}')

def main():
    input_guard()
    result=algebra.escape_results()
    checks=independent.confirm(result)+[('actual Fourier and projector identities',result['DFT_WWstar'] and result['DFT_W2'] and result['P0_idempotent']),('original coefficient condition',result['target_p_plus_2q']=='243/4'),('finite geometry and conditional families',result['all_edges_flip_parity'] and len(result['defect_rows'])==343)]
    print(json.dumps(result,sort_keys=True))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))
if __name__=='__main__':raise SystemExit(main())
