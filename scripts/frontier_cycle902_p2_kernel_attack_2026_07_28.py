#!/usr/bin/env python3
"""Cycle902: bounded original-fixture calculation after explicit scope repair."""
import json
from pathlib import Path
from hashlib import sha256
import time_windows_6009_model as model
import frontier_cycle902_p2_kernel_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/P2_PARTIAL_IF1_TERMINAL_CYCLE902_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'scripts/time_windows_6009_model.py', 'scripts/time_windows_6009_independent.py', 'scripts/frontier_cycle902_p2_kernel_independent_check_2026_07_28.py')
INPUT_SHA256 = {'docs/P2_PARTIAL_IF1_TERMINAL_CYCLE902_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'dde38ae415aabf906bdc3d13ec869f043d407a995ed35aaf593c0aac8e6d4536', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/GBW1B_PRICED_QUADRATIC_GAUGE_BREAK_CYCLE892_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'ff0c9c990de319a35e5b122afec809caf54cfc60c218db3c43865f16946a01e8', 'scripts/time_windows_6009_model.py': '2f8e20e3af19821decf986f8e125282eed54e0ecc9826d61b872f2dd0a0b8c2f', 'scripts/time_windows_6009_independent.py': 'f8396cf2f96bb40146b996908178de4d23ecd0d6795659d9d4151e0c7f5245cf', 'scripts/frontier_cycle902_p2_kernel_independent_check_2026_07_28.py': '27e845654995284bd0f1d7711d04f63fd7069c52a89d43928d09ee12076a8992'}

def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,expected in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=expected:
            raise RuntimeError(f"missing or changed input: {path}")

def main():
    input_guard()
    result=model.spectrum_results()
    checks=independent.confirm(result)
    per=result['per_configuration'];counts={s:sum(r['systems'][s]['consistent'] for r in per.values()) for s in ['bridge','bridge_content','bridge_null','all','theta_free']}
    checks += [('original rank and separating evaluation',result['realized_span_rank']==result['five_point_evaluation_rank']==5 and result['spectrum_rows']==108),('canonical full-grid reconstruction',result['canonical_grid_cells']==648 and result['canonical_grid_violations']==0),('original conditional linear consistency table',counts=={'bridge':12,'bridge_content':1,'bridge_null':12,'all':1,'theta_free':5}),('canonical bridge and null equations hold',all(r['systems'][s]['canonical_residual_nonzero']==0 for r in per.values() for s in ['bridge','bridge_null'])),('single canonical content rows hold with fixed-normalizer nullity zero',per['single']['systems']['all']['canonical_residual_nonzero']==0 and per['single']['systems']['all']['nullity']==0)]
    print(json.dumps(result,sort_keys=True,default=str))
    for label,ok in checks:print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(bool(ok) for _,ok in checks)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed!=len(checks))

if __name__=='__main__':raise SystemExit(main())
