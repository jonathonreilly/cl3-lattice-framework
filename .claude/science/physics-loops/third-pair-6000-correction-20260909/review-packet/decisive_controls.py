import ast, hashlib, json
from pathlib import Path
E=Path(__file__).resolve().parent
S=E/'originals/scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py'
I=E/'originals/scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py'
bindings={}
def lift(path,names):
    tree=ast.parse(path.read_text()); nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes}==set(names)
    ns={'MIN_STABLE_EVENTS':8,'MIN_PERIOD_REPEATS':2}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),'exec'),ns)
    bindings[path.name]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'exact_lifted_functions':sorted(names)}
    return ns
p=lift(S,['tail_periods','reference_tail_periods','reject_reason'])
i=lift(I,['clean_intervals','dirty_intervals','iv_clip','iv_sub','iv_len','interval_detector','literal_detector'])
mask=sum(1<<t for t in range(0,15,2)); length=18; period=2
# Independent finite definition: equality throughout the last 2P+1 positions
# of the whole supplied stretch, rather than through its final clean position.
whole_tail=all(((mask>>t)&1)==((mask>>(t+period))&1) for t in range(length-1-2*period,length-period))
a=p['tail_periods'](mask,[period]); checker_result=i['interval_detector'](mask,length,[period])
assert a==checker_result=={2:(0,8,1)} and p['reject_reason'](mask,period)=='ACCEPT' and whole_tail is False
assert p['reference_tail_periods'](mask,[period])==a and i['literal_detector'](mask,length,[period])==a
# Exact original tooth-9 statement block, executed on its actual stated B5/b3 fixture.
src=I.read_text(); start=src.index('    dirty2 = set(dirty)',src.index('# 9 --'))
end=src.index('\n\n',src.index('"strict_definition_also_sees_it"',start))
block=src[start:end]; block='\n'.join(x[4:] if x.startswith('    ') else x for x in block.splitlines())
def tooth(offset):
    ns=dict(i); ns.update({'P5':8,'N5':35,'s1':17,'s2':25,'t1':18,'L':130,'teeth':[]})
    ns['dirty']={x for t in range(18,130,8) if t+2<130 for x in [t,t+1,t+2]}
    code=block if offset==3 else block.replace('inject = t1 + 3','inject = t1 + '+str(offset))
    exec(compile(code,str(I)+':tooth9','exec'),ns)
    return ns['teeth'][-1],ns['iv2']
original_tooth,original_intervals=tooth(3); separated_tooth,separated_intervals=tooth(4)
assert original_tooth['fires'] and original_tooth['strict_definition_also_sees_it']
assert separated_tooth['fires'] and not separated_tooth['strict_definition_also_sees_it']
# Independent coordinate checks supplement the elementary sorted-row proof.
checked=0
for B in range(3,25):
 for b in range(1,B-1):
    N=8*B-5; P=8*(B-1-b)
    hf=lambda e:2+5*e; f=lambda e:4+5*e; r=lambda e:8*B-9-3*e; hr=lambda e:r(e)+2
    rows=[hf(b-1),f(b-1),hf(b),f(b),r(b),hr(b),r(b-1),hr(b-1)]
    gaps=[(rows[(j+1)%8]-rows[j])%N for j in range(8)]
    assert rows==sorted(set(rows)) and gaps==[2,3,2,8*(B-b)-13,2,1,2,8*b-4]
    pairs=[(f(b-1),r(b)),(f(b),hr(b-1)),(hf(b),r(b-1))]
    assert all((v-u)%N==P for u,v in pairs)
    assert [((v-1)%N in rows) for u,v in pairs]==[False,False,True]
    assert all((u-1)%N not in rows for u,v in pairs)
    assert (hr(b)-P)%N==5*b+1 and 5*b+1 not in rows
    fixed={x for x in rows if (x+P)%N in rows}; first={u for u,v in pairs}; extra=fixed-first
    assert extra==({r(b-1) if B%2 else r(b)} if b==(B-1)//2 else set())
    checked+=1
assert checked==253
print(json.dumps({'scope':'Exact AST-lifted pure component checks, not execution of original producers or validation of controller reachability/campaign counts. No original pin bypass is represented as a full run.','source_bindings':bindings,'tail_witness':{'length':length,'clean_ticks':list(range(0,15,2)),'period':period,'primary':a,'checker':checker_result,'actual_rejection':'ACCEPT','whole_stretch_tail_exact':whole_tail},'widening_original_tooth':original_tooth,'widening_separated_run_control':separated_tooth,'widening_block_sha256':hashlib.sha256(block.encode()).hexdigest(),'station_cells_checked':checked},indent=2))
