#!/usr/bin/env python3
"""Cycle941 bounded corrected finite evidence; no physical or audit verdict."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
import time_readout_6009_algebra as algebra
import time_readout_6009_walks as walks
import frontier_cycle941_gbs2_attack_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/GBS2_LEDGER_RECONCILED_ALL_DIMENSIONLESS_CYCLE941_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_readout_6009_algebra.py', 'scripts/time_readout_6009_walks.py', 'scripts/time_readout_6009_independent.py', 'scripts/frontier_cycle941_gbs2_attack_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/GBS2_LEDGER_RECONCILED_ALL_DIMENSIONLESS_CYCLE941_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'a4dac57021e0cf13394c705dface20f5a52fc9ad8b60aeb524d3280613dede52', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'docs/MIXED_DEGREE_REACHES_NOT_SELECTS_CYCLE904_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'd364eb166bb24588f219d4e43b364b4897551bac8ddb93b1a586c28a58f40e4b', 'scripts/time_readout_6009_algebra.py': '774824bf82119ba34e838831c7e5fa373f883416268063560bbce246f56b7fb0', 'scripts/time_readout_6009_walks.py': '367a63de4a0d43882f86ff8e5b2ae218290ca584611fd40f4f1fd69f589e6794', 'scripts/time_readout_6009_independent.py': 'b2b682742681fe00851e69853af7d740acf7531aa23c89a6387c6e2d7a23a4f4', 'scripts/frontier_cycle941_gbs2_attack_independent_check_2026_07_28.py': 'a0204c52b5e7280c03d3d48590765a4d5d0e9317f1078e58899544e9941cb63c'}
def input_guard():
    root=Path(__file__).resolve().parents[1]
    for p,h in INPUT_SHA256.items():
        if sha256((root/p).read_bytes()).hexdigest()!=h:raise RuntimeError(f'missing or changed input: {p}')

def main():
    input_guard()
    result={'statistics':walks.statistics_results(algebra.O24,algebra.apply),'green':[]}
    for radius in [3,4,5]:
        for m in map(Fraction,['0','1/4','1','7/3']):
            G=algebra.screened_green(radius,m)
            result['green'].append({'radius':radius,'mu2':str(m),'values':[{'orbit':k,'value':str(v)} for k,v in sorted(G.items())], 'G0':str(G[(0,0,0)]),'difference':str(G[(0,0,0)]-G[(0,0,1)])})
    checks=independent.confirm(result)+[('original separate statistic retained',result['statistics']['configuration_diagonal_classes']==8),('all6144 supplied containment counts',result['statistics']['linear_cells']==6144 and all(all(n==r['support_size'] for n in r['window_counts']) for r in result['statistics']['linear_rows'])),('screened origin identity and domain',all(Fraction(r['G0'])>0 and Fraction(r['difference'])==(1-Fraction(r['mu2'])*Fraction(r['G0']))/6 and (Fraction(r['difference'])==Fraction(1,6))==(Fraction(r['mu2'])==0) for r in result['green']))]
    print(json.dumps(result,sort_keys=True))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))
if __name__=='__main__':raise SystemExit(main())
