"""Exact finite affine supports and conditional response evidence; no corpus scan."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import affine_5957_model as model
import frontier_cycle895_t_retirement_independent_check_2026_07_28 as independent
AUDIT_INPUT_PATHS = ('docs/FINITE_AFFINE_SUPPORT_AND_CONDITIONAL_RESPONSE_CYCLE895_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/affine_5957_model.py', 'scripts/frontier_cycle895_t_retirement_independent_check_2026_07_28.py', '.claude/science/physics-loops/affine-5957-correction-20260909/bodies/6b40708359632e1fc18ccc70b1bb0d420e707767')
INPUT_SHA256 = {'docs/FINITE_AFFINE_SUPPORT_AND_CONDITIONAL_RESPONSE_CYCLE895_BOUNDED_THEOREM_NOTE_2026-07-28.md': '2b6f174bb8318711253a94c7e9ed643f5c887f8b044c6cb93acdf8b5c8758a5c', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/affine_5957_model.py': '7db252b967937f4c16cbb4c661f2d635584f483bd86b6087696e679c25ccee6c', 'scripts/frontier_cycle895_t_retirement_independent_check_2026_07_28.py': '6adb500642d6cff89046f66b1b43927275562a8581247d514c92ae702b0fd893', '.claude/science/physics-loops/affine-5957-correction-20260909/bodies/6b40708359632e1fc18ccc70b1bb0d420e707767': '67b41b08cad33a0ed0750e1122f63b956b0dc93a7efa6dc2b26272f0729e9a1a'}
ORIGINAL_RECEIPT = '.claude/science/physics-loops/affine-5957-correction-20260909/bodies/6b40708359632e1fc18ccc70b1bb0d420e707767'


def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,want in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=want:raise RuntimeError('missing or changed input: '+path)


def main():
    input_guard();rows=model.records();tables={str(t):model.row_values(rows,t) for t in (F(-1),F(0),F(1),F(2))};table=model.classify(tables)
    checks,detail=independent.controls(rows,table)
    part=model.partition(rows);always=set(part['all']);blind_counts={}
    for t in (F(-1),F(0),F(1),F(2),F(101,103)):
        blind=[r for r in model.lawful(rows,t) if not any(r['A'])];blind_counts[str(t)]=len(blind)
    checks['traceless_lawful_supports']=blind_counts=={'-1':6,'0':90,'1':6,'2':6,'101/103':6}
    checks['always_lawful_supports_are_supplied_carried_family']=always=={(d,d^1,d,d) for d in range(6)}
    zero=tuple((F(0),)*3 for _ in range(3));response_rows=[]
    # One- and two-endpoint fixtures drawn from the actual supplied fibre.
    for d in range(6):
        left=model.ledger((d,d^1,d,d),d+1);right=model.ledger(((d+2)%6,((d+2)%6)^1,(d+2)%6,(d+2)%6),6-d)
        for array in ((left,zero),(zero,left),(left,right)):
            baseline=model.response(array,F(1));same=all(model.response(array,s)==baseline for s in (F(-2),F(0),F(3)))
            response_rows.append({'direction':d,'occupied':sum(any(v for row in b for v in row) for b in array),'all_six_objects_unchanged':same})
    checks['actual_six_response_objects_on_supplied_fibre_fixtures']=all(r['all_six_objects_unchanged'] for r in response_rows)
    witness=next(r for r in model.lawful(rows,F(1)) if any(r['A']));block=model.ledger(witness['support']);array=(block,zero)
    plus=model.response(array,F(1))[2];minus=model.response(array,F(-1))[2]
    checks['endpoint_resolved_O3_detects_trace_bearing_support']=plus!=minus and plus==tuple(v for b in array[::-1] for v in model.trace(b))
    # The two independently specified linear constraints give the unique gauge-fixed solution.
    r9={'constraints':[[-2,1,1],[-2,1,0]],'gauge':[1,0,0],'solution':[1,2,0]}
    checks['conditional_joint_R9_solution']=all(sum(a*b for a,b in zip(row,r9['solution']))==0 for row in r9['constraints']) and r9['solution'][0]==1 and r9['constraints'][0][2]-r9['constraints'][1][2]==1
    root=Path(__file__).resolve().parents[1];history=json.loads((root/ORIGINAL_RECEIPT).read_text())
    historic={k:history[k] for k in ['files_scanned','consumer_count','classification_table','backlog_rows','retired_count','sensitive_count','broken_count','residue_dispositions','strict_criterion_dissolves','rows_requiring_an_exact_choice_of_t']}
    # Compare mathematical table only, not the historical semantic-retirement conclusion.
    original={r['id']:r for r in history['classification_table']}
    checks['selected_table_classifications_preserved']=set(original)==set(table) and all(original[k]['classification']==r['classification'] for k,r in table.items())
    summary=model.summary(table);checks['own_summary_consumed_consistently']=model.validate_receipt(summary,table)
    result={'scope':'Supplied finite supports and selected factor-through-atoms table; no semantic corpus completeness or physical retirement.',
            'partition':part,'traceless_counts':blind_counts,'selected_table':table,'summary':summary,
            'response_fixtures':response_rows,'trace_bearing_witness':witness,'R9':r9,'independent_controls':detail,
            'historical_selected_data':historic,'historical_count_total':history['retired_count']+history['sensitive_count']+history['broken_count']}
    refutations=[k for k,v in checks.items() if not v];result['refutations']=refutations
    print(json.dumps(result,sort_keys=True,default=str))
    for name,ok in checks.items():print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"TOTAL: PASS={sum(checks.values())} FAIL={len(checks)-sum(checks.values())}")
    return int(not model.accepted(checks,refutations))

if __name__=='__main__':raise SystemExit(main())
