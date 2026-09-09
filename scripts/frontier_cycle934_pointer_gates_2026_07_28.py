#!/usr/bin/env python3
"""Conditional star statistics and finite sampled protocol; no physical verdict."""
import json
import math
from pathlib import Path
from hashlib import sha256
import numpy as np
import pointer_6005_model as model
import frontier_cycle934_pointer_gates_independent_check_2026_07_28 as independent
AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS = ('docs/POINTER_SYMMETRY_AND_SAMPLED_STAR_PROTOCOL_CYCLE934_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/pointer_6005_model.py', 'scripts/frontier_cycle934_pointer_gates_independent_check_2026_07_28.py', '.claude/science/physics-loops/pointer-6005-correction-20260909/bodies/1ba2b5a454d01f6e3046da619758fc4e3b321f5b', '.claude/science/physics-loops/pointer-6005-correction-20260909/bodies/75875bc27d2013897b3accdc347f165a68d8accd')
INPUT_SHA256 = {'docs/POINTER_SYMMETRY_AND_SAMPLED_STAR_PROTOCOL_CYCLE934_BOUNDED_THEOREM_NOTE_2026-07-28.md': 'e2fbb30f4ca053f4c1364d65ad9b3337a8e4f7bead00ebd051bc78ac9ba9cbba', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/pointer_6005_model.py': '5416b71a71bdb03843f752b03b696f07fe3158e0a3dc8a3eb0782f201102cd46', 'scripts/frontier_cycle934_pointer_gates_independent_check_2026_07_28.py': '5b218ccbf96690278740d24f63cda4933314ee9c7edc3d7b4708fabb7492a70e', '.claude/science/physics-loops/pointer-6005-correction-20260909/bodies/1ba2b5a454d01f6e3046da619758fc4e3b321f5b': 'ec21b3b2081a04ecbcd0af5b07b604f395367261d0fa53112b452223d1cab4d3', '.claude/science/physics-loops/pointer-6005-correction-20260909/bodies/75875bc27d2013897b3accdc347f165a68d8accd': 'a82b93d79b8b4f5b768b94ff5376abc4f6c28cda43dde7d7d7b263c4bb1d6f14'}
HISTORY='.claude/science/physics-loops/pointer-6005-correction-20260909'
ORIGINAL_RECEIPT=HISTORY+'/bodies/1ba2b5a454d01f6e3046da619758fc4e3b321f5b'
ORIGINAL_932_RECEIPT=HISTORY+'/bodies/75875bc27d2013897b3accdc347f165a68d8accd'


def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,want in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=want:raise RuntimeError('missing or changed input: '+path)


def historical_tables():
    root=Path(__file__).resolve().parents[1]
    r=json.loads((root/ORIGINAL_RECEIPT).read_text());p=json.loads((root/ORIGINAL_932_RECEIPT).read_text());q=r['Q2_t_open_derived'];l5=q['L5_the_backaction_order_and_the_measured_spread']
    return {'scope':'Exact original finite output values, not fresh campaign execution or physical certification.',
            'seven_field_rows':l5['rows'],'finite_fit_parameters':{k:v for k,v in l5.items() if k.startswith('fitted_') or k.endswith('drift_factor')},
            'zero_pointer_field_rows':q['L3_degree_independence_is_EXACT_at_zero_pointer_field']['rows'],
            'later_lobe_rows':q['L4_zero_field_closed_form']['L4b_content_lobes_are_periodic']['rows'],
            'clip_rows':q['L6_t_close_both_sides_derived']['rows'],
            'original_corpus_grid_rows':r['Q3_composed_star_certification_theorem']['composed_verdict_table'],
            'original_seal_predictions':r['Q3_composed_star_certification_theorem']['seal']['predictions'],
            '932_window_rows':p['Q1_curves']['per_cell'],
            '932_phase_classes_historical':p['Q2_discrimination']['e_grid_phase']['class_by_degree_at_0.10'],
            '932_widths_historical':p['Q2_discrimination']['a_window_width']['W_by_degree_at_0.10']}


def main():
    input_guard();checks,controls=independent.controls();history=historical_tables()
    # Regenerate all seven original sampled rows, using the actual original function.
    sample=[]
    for prior in history['seven_field_rows']:
        field=prior['lambda'];values={}
        for d in range(2,9):
            cell=model.StarCollective(d,field)
            values[str(d)]=model.bisect_scalar(lambda t:cell.stats(t)['chi1']-.9,.30,.78)
        if any(v is None for v in values.values()):raise RuntimeError('declared opening bracket failed')
        one=model.bisect_scalar(lambda t:model.chi1_single_arm_closed(t,field)-.9,.30,.78)
        spread=max(values.values())-min(values.values());shift=max(abs(v-one) for v in values.values())
        sample.append({'field':field,'t_open_by_degree':values,'zero_pointer_open':one,'spread':spread,'shift':shift,
                       'ratio_lambda2':spread/field**2,'ratio_lambda2_log':spread/(field**2*math.log(1/field)),
                       'original_time_difference':max(abs(v-prior['t_open_by_degree'][d]) for d,v in values.items())})
    checks['all_original_seven_field_openings_reproduced']=all(r['original_time_difference']<1e-10 for r in sample)
    ratios=[r['ratio_lambda2'] for r in sample];logs=[r['ratio_lambda2_log'] for r in sample]
    X=np.array([[math.log(r['field']),1.] for r in sample]);fit={}
    for key in ['spread','shift']:
        slope,intercept=np.linalg.lstsq(X,np.log([r[key] for r in sample]),rcond=None)[0]
        fit[key]={'slope':float(slope),'prefactor':float(math.exp(intercept))}
    diagnostics={'sampled_envelope_C':max(ratios),'scope':'Only the seven listed fields; maximum-ratio identity is not an independent bound test.',
                 'lambda2_ratio_range':[min(ratios),max(ratios)],'lambda2_log_ratio_range':[min(logs),max(logs)],
                 'lambda2_drift':max(ratios)/min(ratios),'lambda2_log_drift':max(logs)/min(logs),'finite_loglog_fits':fit}
    # Exact ablation is exercised at finite independent degrees/fields/times.
    ablation=[]
    for armfield in [0.,.1,.7]:
        for t in [0.,.7,2.4]:
            one=model.chi1_single_arm_closed(t,armfield)
            for d in [2,4,8]:
                st=model.StarCollective(d,armfield,lam_pointer=0.).stats(t)
                ablation.append({'d':d,'arm_field':armfield,'t':t,'chi':st['chi1'],'s1':st['s1'],'difference':abs(st['chi1']-one)})
    checks['zero_pointer_product_and_degree_independence']=all(r['difference']<1e-11 and abs(r['s1'])<1e-11 for r in ablation)
    zero=model.zero_field_window(.1);edge=model.StarCollective(3,0.).stats(zero['t_open'])['chi1']
    checks['zero_total_field_threshold_formula']=abs(edge-.9)<1e-11
    # Evaluate actual discrete flags: no continuous single-window assumption.
    gridrows=[]
    for d in range(1,9):
        for field in [.05,.1]:
            cell=model.StarCollective(d,field)
            for delta in [.05,.1,.2]:
                for phase in [0.,.01,.05]:
                    times=[round(.1*i+phase,12) for i in range(13)]
                    flags=[cell.cert(t,delta) for t in times]
                    result=model.sampled_verdict(flags,times,x_control_ok=True,commutator_ordering_ok=True,drift_ok=True)
                    gridrows.append({'d':d,'field':field,'delta':delta,'phase':phase,'flags':flags,'result':result})
    checks['degree_one_has_no_two_fragment_grid_event']=all(r['result']['run']==0 for r in gridrows if r['d']==1)
    scans=[]
    for d,field in [(3,0.),(3,.05),(3,.1),(5,.1)]:
        cell=model.SampledCell(model.StarCollective(d,field))
        scans.append({'d':d,'field':field,'horizon':[0.,3.],'scan_step':.025,
                      'observed_blocks':model.edges_by_brentq(cell,.025,lo=0.,hi=3.)})
    # This validates the declared continuous zero-field formula, not general uniqueness.
    first=scans[0]['observed_blocks']
    checks['zero_field_formula_matches_two_observed_lobes']=len(first)==2 and abs(first[0]['lo']-zero['t_open'])<1e-10 and abs(first[1]['lo']-zero['t_open']-math.pi/2)<1e-10
    result={'scope':'Supplied mathematical protocol. Grid results assume X-control and commutator-ordering clauses; neither is supplied by this computation.',
            'controls':controls,'fresh_seven_field_rows':sample,'finite_diagnostics':diagnostics,
            'fresh_ablation_rows':ablation,'zero_field_window':zero,'fresh_conditional_grid_rows':gridrows,
            'finite_scan_observations':scans,'historical_tables':history}
    refutations=[k for k,v in checks.items() if not v];result['refutations']=refutations
    print(json.dumps(result,sort_keys=True))
    for name,ok in checks.items():print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"TOTAL: PASS={sum(checks.values())} FAIL={len(checks)-sum(checks.values())}")
    return int(not model.accepted(checks,refutations))

if __name__=='__main__':raise SystemExit(main())
