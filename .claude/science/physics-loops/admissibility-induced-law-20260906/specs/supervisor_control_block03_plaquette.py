# Supervisor control (block 03, family D): the one-step TV inequality on the plaquette with exterior,
# with the four-neighbor coefficient, and the maximal-coupling agreement identity. Exact.
from fractions import Fraction as F
from itertools import product
import sys, time
AX=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def orbit(a,b):
    d=sum(x*y for x,y in zip(AX[a],AX[b]))
    return 0 if d==1 else (1 if d==-1 else 2)
def cond(s_list_w, nbrs):  # nbrs: list of menu indices (any length); returns dict s->prob
    p,q,r=s_list_w
    w=[p,q,r]
    num=[]
    for s in range(6):
        v=1
        for y in nbrs: v*=w[orbit(s,y)]
        num.append(v)
    Z=sum(num)
    return [F(n,Z) for n in num]
def tv(a,b): return sum(abs(x-y) for x,y in zip(a,b))/2
def coef(wts,k):  # k-neighbor coefficient: sup over shells differing at one neighbor
    best=F(0)
    for shell in product(range(6),repeat=k):
        base=cond(wts,list(shell))
        for j in range(k):
            for t in range(6):
                if t==shell[j]: continue
                sh2=list(shell); sh2[j]=t
                d=tv(base,cond(wts,sh2))
                if d>best: best=d
    return best
# plaquette: sites 0..3 at (0,0),(1,0),(1,1),(0,1); interior nbrs; exterior slots: two per site
sites=[(0,0),(1,0),(1,1),(0,1)]
def nb(i):
    x,y=sites[i]; out=[]
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        p=(x+dx,y+dy)
        if p in sites: out.append(('i',sites.index(p)))
        else: out.append(('e',(i,(dx,dy))))
    return out
NB=[nb(i) for i in range(4)]
EXT=[e for i in range(4) for k,e in NB[i] if k=='e']
def run(wts):
    c4=coef(wts,4)
    base_ext={e:0 for e in EXT}           # all P(e_x) = index 0
    flip_ext=dict(base_ext); flip_ext[(0,(-1,0))]=1   # site 0's left slot -> P(-e_x)
    worst=F(0); viol=0; n=0; agree_ok=True
    confs=list(product(range(6),repeat=4))
    for eta in confs:
        for eta2 in confs:
            diff=[i for i in range(4) if eta[i]!=eta2[i]]
            if len(diff)>2: continue
            for x in range(4):
                nb1=[eta[j] if k=='i' else base_ext[j] for k,j in NB[x]]
                nb2=[eta2[j] if k=='i' else flip_ext[j] for k,j in NB[x]]
                a=cond(wts,nb1); b=cond(wts,nb2)
                d=tv(a,b)
                bound=c4*sum(1 for k,j in NB[x] if k=='i' and eta[j]!=eta2[j]) + c4*(1 if any(k=='e' and j==(0,(-1,0)) for k,j in NB[x]) else 0)
                n+=1
                if d>bound: viol+=1
                if bound>0 and d/bound>worst: worst=d/bound
                if sum(min(u,v) for u,v in zip(a,b))!=1-d: agree_ok=False
    return c4,n,viol,worst,agree_ok
for wts in [(2,1,2),(3,2,2),(5,4,4),(3,1,2)]:
    t=time.time(); c4,n,viol,worst,ok=run(wts)
    print(wts,'c4=',c4,'instances=',n,'violations=',viol,'worst ratio=',worst,'agree identity ok=',ok,'%.1fs'%(time.time()-t))
