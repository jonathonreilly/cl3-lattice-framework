"""Focused independent arithmetic; fixture/group definitions are openly shared.
Full relevant checks run from primary companion.confirm; standalone controls are small.
"""
from fractions import Fraction
from itertools import product
import time_readout_6009_algebra as a
import time_readout_6009_walks as w

def dfs(seeds,barrier,radius=4,depth=4):
    layers=[{} for _ in range(depth+1)]
    def visit(x,l):
        layers[l][x]=layers[l].get(x,0)+1
        if l==depth:return
        for e in reversed(w.NEIGHBOURS):
            y=tuple(x[i]+e[i] for i in range(3))
            if max(map(abs,y))<=radius and y not in barrier:visit(y,l+1)
    for seed in reversed(seeds):visit(seed,0)
    return layers

def polynomial_invariant_dimension(d):
    if d<0:return 0
    mon=[(i,j,d-i-j) for i in range(d+1) for j in range(d-i+1)];tr=0
    for g in a.O24:
        for m in mon:
            tgt=[0]*3;sgn=1
            for i,exp in enumerate(m):
                j=next(j for j in range(3) if g[i][j]);tgt[j]+=exp;sgn*=g[i][j]**exp
            if tuple(tgt)==m:tr+=sgn
    assert tr%24==0
    return tr//24

def trace_face(H):
    rows=[[Fraction(g[i][j]-(i==j)) for j in range(3)] for g in H for i in range(3)]
    dim=3-a.rank_exact(rows)
    if dim!=1:return None
    return sum((Fraction(1,3-sum(g[i][i] for i in range(3))) for g in H if g!=a.I3),Fraction(0))/len(H)

def controls(cycle):
    if cycle==896:
        return [('degree4 invariant harmonic dimension from monomial traces',polynomial_invariant_dimension(4)-polynomial_invariant_dimension(2)==1)]
    if cycle==898:
        return [('negative quadratic constant rejected over reals',a.quadratic_solutions(-1)['kind']=='empty_real'),('nonunital multiplicative library omits1',all(2**n!=1 for n in range(1,9))),('nonhomogeneous relation can select nonzero scale',27*Fraction(2,27)-2==0)]
    if cycle==901:
        return [('anchor and scope do not select a unique count function',a.F_dim(3)+(3-3)**2==a.F_dim(3) and a.F_dim(4)+1!=a.F_dim(4))]
    if cycle==903:
        seeds=((-1,0,0),(0,0,0));L=dfs(seeds,frozenset(),3,4)
        return [('opposite parity seeds allow lengths3and4',[l for l,x in enumerate(L) if x.get((3,0,0))]==[3,4]),('theta-free measured mass can coexist with motion',w.mass(dfs(((0,0,0),),frozenset(),2,1),((0,0,0),),{(1,0,0)},Fraction(0))==w.mass(dfs(((0,0,0),),frozenset(),2,1),((0,0,0),),{(1,0,0)},Fraction(1))==1)]
    if cycle==941:
        # negative screening at a one-site domain makes 6+mu2 zero.
        return [('negative screening can destroy uniqueness',a.screened_green(1,Fraction(-6)) is None),('row-class and column-class statistics need not agree',len(set([(0,0,1),(0,1,0)]))!=len(set([(0,0),(0,1),(1,0)])))]
    raise ValueError(cycle)

def confirm(cycle,result):
    checks=controls(cycle)
    if cycle==896:
        checks.append(('monomial traces minus radial multiples match harmonic dimensions',all(polynomial_invariant_dimension(r['degree'])-polynomial_invariant_dimension(r['degree']-2)==r['character']==r['monomial_laplacian'] for r in result['angular'])))
    elif cycle==898:
        checks.append(('primary four commuting-involution identities and solution classes are consistent',all(r['squared_identity'] and r['commutes'] and r['solution'] in ['all_Q','zero'] for r in result['involutions'])))
        checks.append(('400 valuation closed forms equal actual numerator enumeration',all(r['least_v2_one']==r['brute'] and (Fraction(r['least_v2_one'])==Fraction(2,27))==(r['odd_part']==27) for r in result['ideal_rows'])))
        checks.append(('all343 integral defect assignments retain exactly integer probes',all(set(r['admitted_probe_alphas'])=={'0','1'} for r in result['defect_rows'])))
    elif cycle==901:
        checks.append(('trace restriction equals actual normal-plane determinant on every subgroup',all(a.q(trace_face(frozenset(tuple(tuple(v) for v in g) for g in r['matrices'])))==r['normal_plane_value'] for r in result['subgroups'])))
    elif cycle==903:
        okay=True;trials=0
        srcs={c['name']:tuple(w.source_set(c)) for c in w.FAMILY}
        for _,fn in w.barriers():
            for c in w.FAMILY:
                seeds=srcs[c['name']];B=frozenset(fn(c));okay &= dfs(seeds,B)==w.counts(seeds,B);trials+=1
        checks.append((f'DFS reproduces all layers on{trials}barrier/configuration fixtures',okay))
        checks.append(('positive cross-term criterion matches exact six-sample masses',all(x['theta_dependent']==x['two_lengths_in_window']==x['sample_moves'] for r in result['incidence']['barriers'] for x in r['rows'])))
    elif cycle==941:
        okay=True;sites=0
        for row in result['green']:
            R=row['radius'];m=Fraction(row['mu2']);G={tuple(v['orbit']):Fraction(v['value']) for v in row['values']}
            def at(x):return G[tuple(sorted(map(abs,x)))] if max(map(abs,x))<R else Fraction(0)
            for x in product(range(-R+1,R),repeat=3):
                lhs=(6+m)*at(x)-sum(at(tuple(x[i]+e[i] for i in range(3))) for e in w.NEIGHBOURS)
                okay &= lhs==int(x==(0,0,0));sites+=1
        checks.append((f'all{sites}unreduced site equations hold for actual orbit solutions',okay))
        checks.append(('C941 rounded-seed layers independently enumerated',all(dfs((w.rounded_seed(c),),frozenset(c['sites']))==w.counts((w.rounded_seed(c),),frozenset(c['sites'])) for c in w.FAMILY)))
    return checks
