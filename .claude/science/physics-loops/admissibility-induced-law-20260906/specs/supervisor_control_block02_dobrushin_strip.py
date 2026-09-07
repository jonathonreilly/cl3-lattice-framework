"""Supervisor control for block 02: exact Dobrushin coefficient of the covariant NN product rule on the Z^3 shell,
and the width-3 strip: formation chain (row sweep) stationary law vs static strip law."""
from fractions import Fraction as F
from itertools import product
import sys, time
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def dot(a,b): return sum(x*y for x,y in zip(MENU[a],MENU[b]))
def orb(a,b): d=dot(a,b); return 0 if d==1 else (1 if d==-1 else 2)
def phi_of(tr): return [[tr[orb(a,b)] for b in range(M)] for a in range(M)]

def dobrushin(tr):
    phi=phi_of(tr)
    # C_{xy}: sup over the other five neighbours' values (eta5) and a pair (t,t') at y of TV(r(.|eta5,t), r(.|eta5,t'))
    best=F(0); arg=None
    for eta5 in product(range(M), repeat=5):
        base=[1]*M
        for s in range(M):
            for e in eta5: base[s]*=phi[s][e]
        conds=[]
        for t in range(M):
            w=[base[s]*phi[s][t] for s in range(M)]; Z=sum(w)
            conds.append([F(x,Z) for x in w])
        for t in range(M):
            for t2 in range(t+1,M):
                tv=sum(abs(conds[t][s]-conds[t2][s]) for s in range(M))/2
                if tv>best: best=tv; arg=(eta5,t,t2)
    return best,arg

for tr in [(3,1,2),(5,2,4),(2,1,2),(3,2,2),(5,4,4),(11,10,10),(4,1,3)]:
    t0=time.time(); c,arg=dobrushin(tr)
    print(f"triple {tr}: C = {c} = {float(c):.5f};  6C = {6*c} = {float(6*c):.4f}  {'UNIQUE (6C<1)' if 6*c<1 else 'criterion silent'}   argmax {arg}  [{time.time()-t0:.1f}s]")
sys.stdout.flush()

# ---- width-3 strip -------------------------------------------------------
W=3
rows=list(product(range(M), repeat=W)); R=len(rows); idx={r:i for i,r in enumerate(rows)}
def strip(tr):
    phi=phi_of(tr)
    def A(r):
        w=1
        for j in range(W-1): w*=phi[r[j]][r[j+1]]
        return w
    def V(r,r2):
        w=1
        for j in range(W): w*=phi[r[j]][r2[j]]
        return w
    # formation chain: first row law and row-to-row kernel under the row sweep (left to right), records-only
    def rule(s, rec):
        w=[1]*M
        for t in range(M):
            for e in rec: w[t]*=phi[t][e]
        return F(w[s], sum(w))
    p0=[F(1)]*R
    for i,r in enumerate(rows):
        for j in range(W):
            p0[i]*=rule(r[j], [r[j-1]] if j>0 else [])
    P=[[F(1)]*R for _ in range(R)]
    for i,r in enumerate(rows):
        for k,r2 in enumerate(rows):
            for j in range(W):
                rec=[r[j]] + ([r2[j-1]] if j>0 else [])
                P[i][k]*=rule(r2[j], rec)
    # stationary law: solve pi P = pi, sum pi = 1 exactly
    # build (P^T - I) with an extra normalisation row
    n=R
    Aeq=[[P[i][k]-(1 if i==k else 0) for i in range(n)] for k in range(n)]  # rows: k, cols: i  (pi_i coefficients)
    Aeq[-1]=[F(1)]*n; b=[F(0)]*n; b[-1]=F(1)
    # gaussian elimination
    Mx=[row[:]+[b[k]] for k,row in enumerate(Aeq)]
    for col in range(n):
        piv=next(r for r in range(col,n) if Mx[r][col]!=0)
        Mx[col],Mx[piv]=Mx[piv],Mx[col]
        pv=Mx[col][col]; Mx[col]=[x/pv for x in Mx[col]]
        for r in range(n):
            if r!=col and Mx[r][col]!=0:
                f=Mx[r][col]; Mx[r]=[a-f*bb for a,bb in zip(Mx[r],Mx[col])]
    pi=[Mx[i][n] for i in range(n)]
    assert all(x>0 for x in pi) and sum(pi)==1
    # check stationarity
    assert all(sum(pi[i]*P[i][k] for i in range(n))==pi[k] for k in range(n))
    # statistics on a row law: prob that sites 0,1 of the row are parallel (same value); prob antiparallel
    def stat(law):
        return (sum(law[i] for i,r in enumerate(rows) if r[0]==r[1]), sum(law[i] for i,r in enumerate(rows) if orb(r[0],r[1])==1))
    # formation law at row i (distribution after i steps) for the finite strip is p0 P^i (rows above do not affect earlier rows)
    # static law on n rows: weight A(r0) prod V(r_i, r_{i+1}) A(r_{i+1}); center row marginal via transfer products
    T=[[V(r,r2)*A(r2) for r2 in rows] for r in rows]
    def static_center(n):
        c=n//2
        left=[A(r) for r in rows]           # weight vector after row 0
        for _ in range(c): left=[sum(left[i]*T[i][k] for i in range(R)) for k in range(R)]
        right=[1]*R
        for _ in range(n-1-c): right=[sum(T[k][i]*right[i] for i in range(R)) for k in range(R)]
        w=[left[k]*right[k] for k in range(R)]; Z=sum(w)
        return [F(x,Z) for x in w]
    print(f"\nstrip width 3, triple {tr}: formation stationary row law: (P[parallel pair], P[antiparallel pair]) = {stat(pi)}  = ({float(stat(pi)[0]):.6f}, {float(stat(pi)[1]):.6f})")
    # formation finite: distribution of row i
    law=p0
    for i in range(1,9):
        law=[sum(law[j]*P[j][k] for j in range(R)) for k in range(R)]
        if i in (1,2,4,8): print(f"   formation row {i}: {tuple(float(x) for x in stat(law))}")
    for n in (3,5,7,9,11,13):
        s=stat(static_center(n)); print(f"   static n={n} center row: ({float(s[0]):.6f}, {float(s[1]):.6f})  exact {s[0]}")
    sys.stdout.flush()
for tr in [(3,1,2),(5,2,4)]:
    strip(tr)
