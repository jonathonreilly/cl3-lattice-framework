"""Independent finite-fixture reconstruction; no repository or SymPy imports.

Derives Q=mH+D^T H-H D from d=iD using sparse rational scattering.
Tests the complete grouped maps, not a copied subblock predicate.
Known comparison values were disclosed in the original review; this is not blind.
"""
from fractions import Fraction as F
from collections import Counter
import json
import time

FIELD = [(F(0), F(1)), (F(3,5), F(4,5)), (F(5,13), F(12,13)),
         (F(8,17), F(15,17)), (F(7,25), F(24,25)),
         (F(20,29), F(21,29)), (F(12,37), F(35,37)), (F(9,41), F(40,41))]

def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]

def rank(rows):
    a = [list(r) for r in rows]
    n = len(a); m = len(a[0]); pivot = 0
    for col in range(m):
        selected = next((r for r in range(pivot, n) if a[r][col]), None)
        if selected is None: continue
        a[pivot], a[selected] = a[selected], a[pivot]
        divisor = a[pivot][col]
        a[pivot] = [x / divisor for x in a[pivot]]
        for r in range(pivot+1, n):
            factor = a[r][col]
            if factor:
                a[r] = [x-factor*y for x,y in zip(a[r],a[pivot])]
        pivot += 1
        if pivot == n: break
    return pivot

def index(t, x): return (t % 8)*4+x%4
def corners(t,x): return [index(t,x),index(t,x+1),index(t+1,x),index(t+1,x+1)]

def hodge():
    h = zeros(32)
    for t in range(8):
        for x in range(4):
            s,v = FIELD[(3*(t%4)+x)%8]
            local = {(0,0):v,(1,1):v/(1-s*s),(2,2):v/(1-s*s),
                     (1,2):-v*s/(1-s*s),(2,1):-v*s/(1-s*s),(3,3):1/v}
            ids = corners(t,x)
            for (r,c), value in local.items(): h[ids[r]][ids[c]] += value/4
    return h

def action(h, origin, wrong_exterior_sign=False):
    d = {}
    for t in range(origin[0],8,2):
        for x in range(origin[1],4,2):
            ids = corners(t,x)
            for r,c,value in [(1,0,F(3,5)),(3,2,F(3,5)),(2,0,F(4,5)),
                               (3,1,F(4,5) if wrong_exterior_sign else -F(4,5))]:
                d[ids[r],ids[c]] = value
    q = [[F(2,7)*v for v in row] for row in h]
    for (r,c),value in d.items():
        for k in range(32):
            q[c][k] += value*h[r][k]
            q[k][c] -= h[k][r]*value
    return q

def inspect(qs, drop_cross_blocks=False):
    output = {'raw_ranks': [], 'raw_kernel': [], 'grouped_ranks': [],
              'embedded_zero': [], 'commutator_ranks': [], 'bands': []}
    physical=[]
    for origin,q in qs:
        output['bands'].append(sorted({((c//4-r//4+4)%8)-4
            for r in range(32) for c in range(32) if q[r][c]}))
        p=[[q[r+16][c+16]-q[r+16][c] for c in range(16)] for r in range(16)]
        physical.append(p)
        a=zeros(32)
        for r in range(16):
            for c in range(16): a[r][c+16]=p[r][c]; a[c+16][r]=-p[r][c]
        shift=lambda k,delta:(k//4)*4+(k%4+delta)%4
        output['commutator_ranks'].append(rank([[a[r][shift(c,1)]-a[shift(r,-1)][c]
            for c in range(32)] for r in range(32)]))
        for direction in (2,-2):
            displacement=lambda t:t-2 if direction==2 else -t-1
            block=lambda s,t:[[q[index(s,r+displacement(s))][index(t,c+displacement(t))]
                for c in range(4)] for r in range(4)]
            for step in (1,3):
                raw=block(step,step+direction)
                output['raw_ranks'].append(rank(raw));output['raw_kernel'].append(all(r[1]==0 for r in raw))
                for start in (step-1,step):
                    g=zeros(8)
                    for row_offset in (0,1):
                        for col_offset in (0,1):
                            if drop_cross_blocks and row_offset!=col_offset:continue
                            sub=block(start+row_offset,start+direction+col_offset)
                            for r in range(4):
                                for c in range(4):g[4*row_offset+r][4*col_offset+c]=sub[r][c]
                    residual=[r[1 if start==step else 5] for r in g]
                    output['grouped_ranks'].append(rank(g));output['embedded_zero'].append(not any(residual))
                    if origin==(1,0) and direction==2 and step==1 and start==1:
                        output['counterexample']=[str(x) for x in residual]
    output['difference']=str(physical[1][10][11]-physical[0][10][11])
    return output

def matches(x):
    return (x['difference']=='-89/140' and x['bands']==[[-2,-1,0,1,2]]*2
        and x['commutator_ranks']==[32,32] and x['raw_ranks']==[3]*8 and all(x['raw_kernel'])
        and Counter(x['grouped_ranks'])=={4:12,3:4} and sum(x['embedded_zero'])==10
        and x['counterexample']==['0','0','0','0','9/80','0','0','0'])

if __name__=='__main__':
    start=time.monotonic();h=hodge();qs=[(o,action(h,o)) for o in ((1,0),(1,1))]
    result=inspect(qs);assert matches(result),result
    dropped=inspect(qs,drop_cross_blocks=True)
    exterior=inspect([(o,action(h,o,wrong_exterior_sign=True)) for o,_ in qs])
    assert not matches(dropped);assert not matches(exterior)
    print(json.dumps({'result':result,'mutations_rejected':['discard_group_cross_blocks','flip_exterior_insertion_sign'],
                      'elapsed_sec':time.monotonic()-start,'imports':'stdlib only; no primary/helper imports'},indent=2))
