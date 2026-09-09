"""Focused independent arithmetic routes; fixture/map definitions are shared openly.

The DFS enumerator does not call the layered walk implementation. The ordered
cross-term spectrum route differs from the model's absolute-difference sum.
This is finite implementation evidence, not independent physical premise review.
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter
from itertools import combinations
import time_windows_6009_model as model

@lru_cache(None)
def dfs(sites,barrier):
    counts=[Counter() for _ in range(model.D+1)]
    stack=[(x,0) for x in model.sources(sites)]
    while stack:
        x,depth=stack.pop();counts[depth][x]+=1
        if depth==model.D:continue
        for step in reversed(model.NEIGHBOURS):
            y=tuple(x[i]+step[i] for i in range(3))
            if y in model.BOX and y not in barrier:stack.append((y,depth+1))
    return counts


def independent_spectrum(cfg,window,barrier=None):
    sites=tuple(cfg['sites']);barrier=frozenset(sites) if barrier is None else frozenset(barrier)
    counts=dfs(sites,barrier);n=len(model.sources(sites));out=[Fraction(0)]*5
    for x in set(window)&model.BOX:
        c=[Fraction(row.get(x,0),n) for row in counts]
        out[0]+=sum(v*v for v in c)
        for i in range(5):
            for j in range(i+1,5):out[j-i]+=2*c[i]*c[j]
    return tuple(out)


def modular_rank(rows,prime=1000003):
    a=[[int(Fraction(x).numerator)%prime*pow(int(Fraction(x).denominator),-1,prime)%prime for x in row] for row in rows];r=0
    for col in range(len(a[0]) if a else 0):
        p=next((i for i in range(r,len(a)) if a[i][col]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];v=pow(a[r][col],-1,prime);a[r]=[x*v%prime for x in a[r]]
        for i in range(r+1,len(a)):
            v=a[i][col];a[i]=[(x-v*y)%prime for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def controls(cycle):
    checks=[]
    if cycle==885:
        a={(0,0,0)};b=a|{(1,0,0)}
        wa=model.site_boundary({'sites':tuple(a)});wb=model.site_boundary({'sites':tuple(b)})
        checks.append(('nonempty disjoint shell violates all-superset monotonicity',(1,0,0) in wa and (1,0,0) not in wb))
        cfg=model.FAMILY[0];checks.append(('DFS reproduces actual depth-four seed and walk counts',dfs(cfg['sites'],frozenset(cfg['sites']))==model.layers(cfg['sites'],frozenset(cfg['sites']))))
    elif cycle==893:
        p=[{1,2},{3,4}];q=[{1,3},{2,4}]
        checks.append(('equal-count partitions are incomparable',model.partition_relation(p,q)=='incomparable'))
        cfg=model.FAMILY[0];bar=frozenset(cfg['sites']);ls=dfs(cfg['sites'],bar)
        checks.append(('barrier blocks positive-length arrival but permits zero-step seed',sum(row.get((0,0,0),0) for row in ls[1:])==0 and ls[0][(0,0,0)]==1))
    elif cycle==894:
        mu={'a':Fraction(0),'b':Fraction(1)};phi={x:x for x in mu}
        pull=lambda w:sum(mu[x] for x in mu if phi[x] in w)
        checks.append(('fixed map and weights allow varying target-window masses',pull({'a'})==0 and pull({'b'})==1))
        checks.append(('positive event mass permits empty target fibre',sum([Fraction(1)] if 'a' in {'b'} else [])==0))
        checks.append(('positive common normalizer can absorb scalar theta dependence',all(Fraction(2)*n/n==2 for n in [Fraction(1),Fraction(3,2)])))
    elif cycle==902:
        rows=[[0,1,2],[0,2,4],[0,0,0]]
        checks.append(('skipped-pivot rank-deficient control',modular_rank(rows)==model.rref(rows,3)[2]==1))
        # p=cos(phi)=0, a single amplitude1+u^2 cancels. Positive Chebyshev
        # coefficients do not individually imply a strictly positive mass.
        checks.append(('squared-amplitude cancellation endpoint',model.evaluate((2,0,2,0,0),Fraction(1))==0))
    return checks


def confirm(cycle,result):
    checks=controls(cycle)
    if cycle==885:
        checks.append(('all twelve support spectra match DFS',all(independent_spectrum(c,c['sites'])==model.spectrum(c,c['sites']) for c in model.FAMILY)))
    elif cycle==893:
        checked=0;ok=True
        for name,fn in model.BARRIERS+model.NEW_BARRIERS:
            for c in model.FAMILY:
                barrier=frozenset(fn(c));ok &= dfs(c['sites'],barrier)==model.layers(c['sites'],barrier);checked+=1
        checks.append((f'DFS agrees on every layer of {checked} original barrier/configuration fixtures',ok))
        checks.append(('refinement labels follow actual block containment',all(row['partition_relation_to_support']==('same' if {frozenset(x) for x in row['partition']}=={frozenset(x) for x in result['B_supp__THE_IDENTIFICATION']['partition']} else 'finer' if all(any(set(x)<=set(y) for y in result['B_supp__THE_IDENTIFICATION']['partition']) for x in row['partition']) else 'coarser' if all(any(set(y)<=set(x) for x in row['partition']) for y in result['B_supp__THE_IDENTIFICATION']['partition']) else 'incomparable') for row in result.values())))
    elif cycle==894:
        checks.append(('all108 window spectra reconstructed through DFS and ordered cross terms',all(independent_spectrum(c,fn(c))==model.spectrum(c,fn(c)) for c in model.FAMILY for fn in model.WINDOWS.values())))
        witness=result['fixed_set_witness'];w={tuple(x) for x in witness['target_sites']};cfgs=[next(c for c in model.FAMILY if c['name']==n) for n in witness['configurations']]
        checks.append(('literal same target set gives actual0/1 masses',all(str(sum(model.direct_masses(c,model.THETAS[0]).get(x,0) for x in w))==v for c,v in zip(cfgs,witness['masses'])) and witness['masses']==['0','1']))
    elif cycle==902:
        rows=[independent_spectrum(c,fn(c)) for fn in model.WINDOWS.values() for c in model.FAMILY]
        checks.append(('independent DFS spectra give modular lower bound five and rational upper bound five',modular_rank(rows)==result['realized_span_rank']==5))
        # In the declared coefficient system the support window is present,
        # so identifying its mass with supplied content requires this equality.
        expected=[c['name'] for c in model.FAMILY if independent_spectrum(c,c['sites'])[0]==model.readout(c)]
        got=[n for n,r in result['per_configuration'].items() if r['systems']['bridge_content']['consistent']]
        checks.append(('conditional content-identification consistency matches independently computed seed mass',sorted(expected)==sorted(got)==['single']))
    return checks
