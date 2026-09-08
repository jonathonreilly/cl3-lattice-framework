from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json, hashlib
T=((1,0,0),(2,1,0),(1,2,0),(0,1,0)); c=(1,1,0)
def adj(a,b): return sum(abs(x-y) for x,y in zip(a,b))==1
def law(order, targets=T, initial=None):
    states=[(dict(initial or {}), F(1))]
    for x in order:
        new=[]
        for state,p in states:
            ns=[v for y,v in state.items() if adj(x,y)]
            pp=F(ns.count(-1),len(ns)) if ns else F(1,2)
            for v,q in ((1,pp),(-1,1-pp)):
                if q:
                    out=state.copy(); out[x]=v; new.append((out,p*q))
        states=new
    result={}
    for state,p in states:
        key=tuple(state[x] for x in targets); result[key]=result.get(key,F(0))+p
    assert sum(result.values())==1
    return result
def desired(n): return {(1,)*n:F(1,2),(-1,)*n:F(1,2)}
def tv(a,b): return sum(abs(a.get(k,0)-b.get(k,0)) for k in a.keys()|b.keys())/2
def ser(d): return {','.join(map(str,k)):str(v) for k,v in sorted(d.items())}
checks=[]
def check(name,value):
    assert value,name; checks.append(name)
check('targets-pairwise-not-nearest-neighbors',all(not adj(a,b) for a,b in permutations(T,2)))
check('one-center-adjacent-all-four',all(adj(c,x) for x in T))
no=[law(o) for o in permutations(T)]
check('all-no-relay-orders-uniform-product',all(d=={k:F(1,16) for k in product((-1,1),repeat=4)} for d in no))
check('no-relay-TV-seven-eighths',all(tv(d,desired(4))==F(7,8) for d in no))
rows=[]
for order in permutations(T+(c,)):
    d=law(order); rows.append({'order':[list(x) for x in order], 'distribution':ser(d),'TV':str(tv(d,desired(4)))})
passed=sum(r['TV']=='0' for r in rows)
check('all-center-first-orders-pass',all(law((c,)+o)==desired(4) for o in permutations(T)))
check('all-first-target-then-center-orders-pass',all(law((o[0],c)+o[1:])==desired(4) for o in permutations(T)))
check('relay-last-fails',law(T+(c,))!=desired(4))
# Prospective count was not specified; report actual result without retuning.
paths=[]
for L in range(1,7):
    sites=tuple((i,0,0) for i in range(L+1)); d=law(sites,(sites[0],sites[-1]))
    check('path-distance-'+str(L),d==desired(2)); paths.append({'distance':L,'auxiliary_count':L-1,'distribution':ser(d)})
shared=desired(4)
check('shared-seed-adverse-violates-factorization',shared[(1,)*4]!=F(1,2)**4)
background=law((c,)+T,initial={(1,1,1):1})
check('fixed-plus-background-biases-unmodified-rule',background=={(1,)*4:F(1)})
result={'checks':checks,'TOTAL':len(checks),'no_relay_orders':len(no),'relay_orders':len(rows),'relay_exact_matches':passed,'relay_rows':rows,'paths':paths,'fixed_background_adverse':ser(background),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('relay_rows','checks')},indent=2))
