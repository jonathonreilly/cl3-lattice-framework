"""Independent s-coordinate support arithmetic plus actual corrected operand controls.

The mathematical partition does not import model computations. The controls call
its actual receipt/terminal functions because those are the behavior under test.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json,copy
import affine_5957_model as model
AUDIT_INPUT_PATHS = ('docs/FINITE_AFFINE_SUPPORT_AND_CONDITIONAL_RESPONSE_CYCLE895_BOUNDED_THEOREM_NOTE_2026-07-28.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/affine_5957_model.py')
INPUT_SHA256 = {'docs/FINITE_AFFINE_SUPPORT_AND_CONDITIONAL_RESPONSE_CYCLE895_BOUNDED_THEOREM_NOTE_2026-07-28.md': '2b6f174bb8318711253a94c7e9ed643f5c887f8b044c6cb93acdf8b5c8758a5c', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'scripts/affine_5957_model.py': '7db252b967937f4c16cbb4c661f2d635584f483bd86b6087696e679c25ccee6c'}


def input_guard():
    root=Path(__file__).resolve().parents[1]
    for path,want in INPUT_SHA256.items():
        if sha256((root/path).read_bytes()).hexdigest()!=want:raise RuntimeError('missing or changed input: '+path)


def independent_partition():
    # In s=1+t coordinates the direct ledger is m+s*f+(2-s)*a-d.
    dirs=[]
    for axis in range(3):
        for sign in (1,-1):dirs.append(tuple(sign if j==axis else 0 for j in range(3)))
    out={'all':[],'never':[],'roots':{}}
    for flat in range(6**4):
        ix=[];n=flat
        for _ in range(4):ix.insert(0,n%6);n//=6
        d,m,f,a=(dirs[j] for j in ix)
        constant=[m[j]+2*a[j]-d[j] for j in range(3)]
        slope=[f[j]-a[j] for j in range(3)]
        pivot=next((j for j in range(3) if slope[j]),None)
        if pivot is None:kind='all' if constant==[0,0,0] else 'never';root=None
        else:
            s=-F(constant[pivot],slope[pivot]);valid=all(m[j]+s*f[j]+(2-s)*a[j]==d[j] for j in range(3))
            kind='roots' if valid else 'never';root=str(s-1)
        if kind=='roots':out[kind].setdefault(root,[]).append(tuple(ix))
        else:out[kind].append(tuple(ix))
    return out


def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def comm(a,b):
    x,y=mul(a,b),mul(b,a);return [[x[i][j]-y[i][j] for j in range(2)] for i in range(2)]
def norm2(a):return sum(v*v for row in a for v in row)


def threshold_controls():
    X=[[F(0),F(1)],[F(1),F(0)]];Z=[[F(1),F(0)],[F(0),F(-1)]];rows=[]
    for t in (F(0),F(999,1000),F(1),F(2)):
        full=[[(-2+(1+t)+(1-t))*v for v in row] for row in Z]
        deleted=[[(t-1)*v for v in row] for row in Z]
        r=norm2(comm(X,deleted));rows.append({'t':str(t),'full_norm2':str(norm2(comm(X,full))),'deleted_norm2':str(r),'nonzero':r>0,'above_0_7':r>F(49,100)})
    return rows


def controls(rows=None,table=None):
    input_guard();rows=model.records() if rows is None else rows
    if table is None:table=model.classify({str(t):model.row_values(rows,t) for t in (F(-1),F(0),F(1),F(2))})
    independent=independent_partition();derived=model.partition(rows)
    clean=model.summary(table);forged_state=copy.deepcopy(clean);forged_state['decision_surface_state']='EXHAUSTIVE_RETIREMENT'
    forged_count=copy.deepcopy(clean);forged_count['uniform_count']+=1
    changed_table=copy.deepcopy(table);target='C880_318_TWO_SECTOR_SUPPORT_LAWFUL';changed_table[target]['classification']='T_UNIFORM'
    baseline=model.validate_receipt(clean,table)
    mutations={'baseline':baseline,'changed_state_rejected':not model.validate_receipt(forged_state,table),
               'changed_count_rejected':not model.validate_receipt(forged_count,table),
               'changed_classification_rejected':not model.validate_receipt(clean,changed_table)}
    tr=threshold_controls()
    gate_cases={'clean':model.accepted({'partition':True},[]),'failed':model.accepted({'partition':False},[]),
                'empty':model.accepted({},[]),'refuted':model.accepted({'partition':True},['actual mismatch'])}
    checks={'independent_s_coordinate_matches_all_supports':independent==derived,
            'exact_partition_counts':len(independent['all'])==6 and len(independent['never'])==1146 and {k:len(v) for k,v in independent['roots'].items()}=={'0':84,'-1':30,'1':30},
            'actual_threshold_differs_from_nonzero':all(r['full_norm2']=='0' for r in tr) and tr[0]['above_0_7'] and tr[1]['nonzero'] and not tr[1]['above_0_7'] and not tr[2]['nonzero'],
            'clean_baseline_and_changed_operands':all(mutations.values()),
            'actual_terminal_rejects_failure_empty_refutation':gate_cases=={'clean':True,'failed':False,'empty':False,'refuted':False}}
    return checks,{'partition_counts':{k:len(v) for k,v in independent.items() if k!='roots'},'root_counts':{k:len(v) for k,v in independent['roots'].items()},'threshold_rows':tr,'actual_receipt_controls':mutations,'actual_terminal_controls':gate_cases}


def main():
    checks,details=controls();refutations=[k for k,v in checks.items() if not v]
    print(json.dumps({'details':details,'refutations':refutations},sort_keys=True))
    for name,ok in checks.items():print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"TOTAL: PASS={sum(checks.values())} FAIL={len(checks)-sum(checks.values())}")
    return int(not model.accepted(checks,refutations))

if __name__=='__main__':raise SystemExit(main())
