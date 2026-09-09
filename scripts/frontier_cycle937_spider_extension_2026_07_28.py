#!/usr/bin/env python3
"""Bounded Cycle937 model evidence; historical tables are explicitly separate."""
import json
import math
from pathlib import Path
from hashlib import sha256
import numpy as np
import spider_6008_model as model
import frontier_cycle937_spider_extension_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = ('docs/SPIDER_SYMMETRY_REDUCTION_AND_FINITE_COMPARISONS_CYCLE937_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/spider_6008_model.py', 'scripts/frontier_cycle937_spider_extension_independent_check_2026_07_28.py', '.claude/science/physics-loops/spider-6008-correction-20260909/bodies/739fbb660482963d53df6b0f3bee9652a8e6b87e', '.claude/science/physics-loops/spider-6008-correction-20260909/inputs/scripts/frontier_cycle932_persistence_razor_2026_07_28.py', '.claude/science/physics-loops/spider-6008-correction-20260909/inputs/outputs/persistence_razor_cycle932_receipt_2026_07_28.json')
INPUT_SHA256 = {'docs/SPIDER_SYMMETRY_REDUCTION_AND_FINITE_COMPARISONS_CYCLE937_BOUNDED_THEOREM_NOTE_2026-07-28.md': '761cab9b3d1bb2d85d949fb0a7c42d839daa38913c85c61679e9684feb3d6195', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/spider_6008_model.py': '898c8acd3f07c07b33b5a06726884bf2e923502e857caa47307747745903b95e', 'scripts/frontier_cycle937_spider_extension_independent_check_2026_07_28.py': 'c57f59b9466228f542eadb1988086cb50529d60e4227ed8feef6beaeeaa5a13b', '.claude/science/physics-loops/spider-6008-correction-20260909/bodies/739fbb660482963d53df6b0f3bee9652a8e6b87e': 'd532781f8dffadd3340cd97afb39dc4b2fb33bb55623ded7d139cc7ef8beba5d', '.claude/science/physics-loops/spider-6008-correction-20260909/inputs/scripts/frontier_cycle932_persistence_razor_2026_07_28.py': '6975d2215149116c26392039b04b8b5a6d91236d023a1a37e8dfa602d6abce40', '.claude/science/physics-loops/spider-6008-correction-20260909/inputs/outputs/persistence_razor_cycle932_receipt_2026_07_28.json': 'a82b93d79b8b4f5b768b94ff5376abc4f6c28cda43dde7d7d7b263c4bb1d6f14'}
HISTORY = '.claude/science/physics-loops/spider-6008-correction-20260909'
ORIGINAL_RECEIPT = HISTORY+'/bodies/739fbb660482963d53df6b0f3bee9652a8e6b87e'
VENDOR_RECEIPT = HISTORY+'/inputs/outputs/persistence_razor_cycle932_receipt_2026_07_28.json'


def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,expected in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=expected:
            raise RuntimeError('missing or changed input: '+path)


def historical_finite_tables():
    """Read immutable source evidence; do not claim fresh underlying simulations."""
    root=Path(__file__).resolve().parents[1]
    r=json.loads((root/ORIGINAL_RECEIPT).read_text())
    q=r['Q2_saturation_derived'];ladder=q['depth_graded_lambda_ladder'];rows=[]
    for family,entry in ladder['families'].items():
        for step in entry['steps']:
            lambdas=ladder['fit_lambdas'];values=[step['delta_by_lambda']['%g'%x] for x in lambdas]
            fit=model.fit_power_with_log(lambdas,[v if abs(v)>ladder['floor'] else None for v in values])
            rows.append({'family':family,'step':step['step'],'site_depth':step['site_added_at_depth'],
                         'historical_delta_by_lambda':step['delta_by_lambda'],'fresh_rescore_of_historical_values':fit,
                         'historical_winner':step['winning_exponent'],
                         'score_reproduction':fit==({k:v for k,v in step['fit'].items() if k!='resolved_at_double_precision'}|{'at_least_five_supplied_points':step['fit']['resolved_at_double_precision']}) if fit else step['fit'] is None})
    lc=q['light_cone_candidate']
    vendor=json.loads((root/VENDOR_RECEIPT).read_text())
    vendor_rows={k:vendor['Q1_curves']['per_cell'][k] for k in ['G1@0.05','G1@0.075','G1@0.1']}
    return {'status':'Underlying tables are historical outputs, not rerun or asymptotic evidence.',
            'ladder_floor':ladder['floor'],'ladder_rows':rows,
            'finite_one_variable_ansatz_rows':lc['test_1_scaling_collapse']['rows'],
            'long_time_rows':lc['test_2_long_time']['rows'],
            'saturation_threshold_rows':q['cashed_against_927']['rows'],
            'G1_rows':r['Q3_boundary_and_closure']['G1_closure']['rows'],
            'original_seal_predictions':r['seal']['predictions'],
            '932_frozen_historical_comparison_rows':vendor_rows}


def main():
    input_guard();history=historical_finite_tables()
    checks={};rows=[]
    fixtures=[(2,1,[],.13,.7),(2,2,[(0,1)],.13,.7),(3,2,[(0,1)],.13,.7),
              (2,3,[(0,1),(0,2)],.1,.7),(2,3,[(0,1),(1,2),(2,0)],.13,.7)]
    for spec in fixtures:rows.append(independent.compare(*spec))
    # Actual G1 chain9 cells, at each original field's own pinned ceiling time.
    g1=[]
    for prior in history['G1_rows']:
        row=independent.compare(2,4,[(0,1),(1,2),(2,3)],prior['field'],prior['pinned_927_ceiling_jt'])
        row['historical_value']=prior['pinned_927_SPk2L4_ceiling_row']
        row['historical_comparator_difference']=abs(row['C_pair']-row['historical_value']);g1.append(row)
    required=['isometry_residual','projection_residual','intertwining_residual','initial_residual','state_residual','entropy_residual','complement_residual']
    checks['finite_reduction_hankel_complement_agreement']=all(row[k]<1e-10 for row in rows+g1 for k in required)
    checks['G1_actual_field_specific_comparators']=all(r['historical_comparator_difference']<1e-10 for r in g1)
    # L-ZERO comparison includes loopy identical and nonisomorphic arms.
    zero=[]
    for arms in [[(3,[(0,1),(1,2),(2,0)])]*2,[(1,[]),(3,[(0,1),(1,2)])]]:
        for t in [.7,12.,50.]:
            F,v=independent.full_system(arms,0.,.35);state=model.evolve(F,v,t)
            s=independent.full_profile(state,[L for L,edges in arms])
            H,c,basis=model.reduced(2,1,[],0.,.35);star=model.profile(model.evolve(H,c,t),basis,2,1)
            zero.append({'arms':arms,'t':t,'max_profile_difference':max(abs(a-b) for a,b in zip(s,star))})
    checks['L_zero_supplied_preparation_graph_comparisons']=all(r['max_profile_difference']<1e-10 for r in zero)
    on1=independent.compare(2,1,[],.1,.7);on2=independent.compare(2,2,[(0,1)],.1,.7)
    field_on_difference=abs(on1['C_pair']-on2['C_pair'])
    checks['arm_field_on_changes_star_comparison']=field_on_difference>1e-8
    checks['historical_finite_scores_reproduced']=all(r['score_reproduction'] for r in history['ladder_rows'])
    # Changed source branch cannot redefine these two recovered vendor blobs.
    pinned_vendor=HISTORY+'/inputs/scripts/frontier_cycle932_persistence_razor_2026_07_28.py'
    old=INPUT_SHA256[pinned_vendor];INPUT_SHA256[pinned_vendor]='0'*64
    try:input_guard();caught=False
    except RuntimeError:caught=True
    finally:INPUT_SHA256[pinned_vendor]=old
    checks['actual_vendor_guard_rejects_wrong_expected_hash']=caught
    independent_checks,control=independent.controls();checks.update(independent_checks)
    refutations=[name for name,ok in checks.items() if not ok]
    result={'scope':'Supplied finite Hamiltonian and preparation only; no physical supplier or asymptotic claim.',
            'fresh_reduction_rows':rows,'fresh_G1_rows':g1,'fresh_L_zero_rows':zero,
            'field_on_C_pair_difference':field_on_difference,'actual_controls':control,'historical_tables':history,'refutations':refutations}
    print(json.dumps(result,sort_keys=True))
    for name,ok in checks.items():print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"TOTAL: PASS={sum(checks.values())} FAIL={len(checks)-sum(checks.values())}")
    return int(not model.accepted(checks,refutations))

if __name__=='__main__':raise SystemExit(main())
