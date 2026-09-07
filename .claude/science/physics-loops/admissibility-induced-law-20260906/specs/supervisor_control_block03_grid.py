"""Supervisor control for block 03: the Dobrushin coefficient of the covariant product rule, exactly; the region; thresholds;
and a finite-window comparison-bound sanity check (3x3 planar window by row transfer)."""
from fractions import Fraction as F
from itertools import product
import sympy as sp, sys, time
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def dot(a,b): return sum(x*y for x,y in zip(MENU[a],MENU[b]))
def orb(a,b): d=dot(a,b); return 0 if d==1 else (1 if d==-1 else 2)
def phi_of(tr): return [[tr[orb(a,b)] for b in range(M)] for a in range(M)]

def coeff(tr, deg):
    """c1 = sup over the other deg-1 neighbours' values and a pair (t,t') at one neighbour of TV(r(.|eta,t), r(.|eta,t'))."""
    phi=phi_of(tr); best=F(0); arg=None
    for eta in product(range(M), repeat=deg-1):
        base=[1]*M
        for s in range(M):
            for e in eta: base[s]*=phi[s][e]
        conds=[]
        for t in range(M):
            w=[base[s]*phi[s][t] for s in range(M)]; Z=sum(w); conds.append([F(x,Z) for x in w])
        for t in range(M):
            for t2 in range(t+1,M):
                tv=sum(abs(conds[t][s]-conds[t2][s]) for s in range(M))/2
                if tv>best: best=tv; arg=(eta,t,t2)
    return best,arg

print("=== grid: r=4, p,q in 1..12 (6-neighbour shell); cells with 6c1<1 marked U ===")
t0=time.time(); grid={}
for p in range(1,13):
    row=""
    for q in range(1,13):
        c,arg=coeff((p,q,4),6); grid[(p,q)]=(c,arg); row += (" U" if 6*c<1 else " .")
    print(f"p={p:2d}: {row}")
print(f"[grid {time.time()-t0:.0f}s]  symmetric p<->q? {all(grid[(p,q)][0]==grid[(q,p)][0] for p in range(1,13) for q in range(1,13))}")
# argmax pattern classes near the boundary
from collections import Counter
cnt=Counter()
for (p,q),(c,arg) in grid.items():
    eta,t,t2=arg; cnt[(tuple(sorted(orb(e,0) for e in eta)), orb(t,t2))]+=1
print("argmax pattern classes (orbits of the 5 other neighbours relative to +x, and the orbit of the flipped pair):", cnt.most_common(6))
sys.stdout.flush()

print("\n=== thresholds along lines (exact) ===")
t=sp.symbols('t', positive=True)
def coeff_symbolic_at_pattern(trsym, eta, tpair, deg):
    phi=[[trsym[orb(a,b)] for b in range(M)] for a in range(M)]
    base=[sp.Integer(1)]*M
    for s in range(M):
        for e in eta: base[s]*=phi[s][e]
    conds=[]
    for tt in tpair:
        w=[base[s]*phi[s][tt] for s in range(M)]; Z=sum(w); conds.append([w[s]/Z for s in range(M)])
    return sp.simplify(sum(sp.Abs(conds[0][s]-conds[1][s]) for s in range(M))/2)
for line,name in [((t,1,1),"(t,1,1): parallel weight t, others 1"), ((t,t,1),"(t,t,1): parallel=antiparallel t, orthogonal 1"), ((1,1,t),"(1,1,t): orthogonal weight t")]:
    # numeric scan to locate the crossing and the maximizing pattern there
    prev=None
    for k in range(1,80):
        val=F(k,8) if name.startswith("(1,1,t)") else F(1)+F(k,8)
        tr=tuple(F(v).subs(t,val) if hasattr(v,'subs') else F(v) for v in line)
        tr=tuple(F(str(x)) for x in tr)
        c,arg=coeff(tr,6)
        if prev is not None and (6*prev[0]<1)!=(6*c<1):
            print(f"  {name}: 6c1 crosses 1 between t={prev[1]} and t={val}; pattern at crossing {arg}")
            eta,ta,tb=arg
            expr=coeff_symbolic_at_pattern(line,eta,(ta,tb),6)
            sols=[sp.nsimplify(s_) for s_ in sp.solve(sp.Eq(6*expr,1), t) if s_.is_real and s_>0]
            print(f"     6*c1(t) at that pattern = {sp.simplify(6*expr)};  exact threshold(s): {sols}  ~ {[sp.N(s_,12) for s_ in sols]}")
            break
        prev=(c,val)
sys.stdout.flush()

print("\n=== 3x3 planar window: exact centre-site sensitivity to one exterior slot vs the comparison bound ===")
W=3; rows=list(product(range(M),repeat=W)); R=len(rows)
def center_marginal(tr, ext):
    """ext: dict (row i, col j, side) -> menu value for exterior slots: side in {'L','R','B','T'} ('B' below row0, 'T' above row2)."""
    phi=phi_of(tr)
    def A(i,r):
        w=1
        for j in range(W-1): w*=phi[r[j]][r[j+1]]
        for j in range(W):
            for side in ('L','R'):
                if (i,j,side) in ext: w*=phi[r[j]][ext[(i,j,side)]]
        if i==0:
            for j in range(W):
                if (0,j,'B') in ext: w*=phi[r[j]][ext[(0,j,'B')]]
        if i==2:
            for j in range(W):
                if (2,j,'T') in ext: w*=phi[r[j]][ext[(2,j,'T')]]
        return w
    V=lambda r,r2: phi[r[0]][r2[0]]*phi[r[1]][r2[1]]*phi[r[2]][r2[2]]
    marg=[0]*M
    for i0,r0 in enumerate(rows):
        a0=A(0,r0)
        for i1,r1 in enumerate(rows):
            a1=A(1,r1)*V(r0,r1)
            for i2,r2 in enumerate(rows):
                w=a0*a1*V(r1,r2)*A(2,r2)
                marg[r1[1]]+=w
    Z=sum(marg); return [F(x,Z) for x in marg]
for tr in [(2,1,2),(3,2,2),(3,1,2)]:
    c4,_=coeff(tr,4)   # the window's own coefficient (4 neighbours)
    alpha=4*c4
    ext0={}
    for i in range(3):
        ext0[(i,0,'L')]=0; ext0[(i,2,'R')]=0
    for j in range(3): ext0[(0,j,'B')]=0; ext0[(2,j,'T')]=0
    m0=center_marginal(tr, ext0)
    ext1=dict(ext0); ext1[(1,0,'L')]=1        # flip the exterior slot left of the middle-left site to P(-e_x)
    m1=center_marginal(tr, ext1)
    tv=sum(abs(a-b) for a,b in zip(m0,m1))/2
    # comparison bound: D = sum_n C^n on the 3x3 grid with C = c4 * adjacency; b nonzero only at site (1,0): b = c4 (one changed exterior neighbour)
    import itertools
    sites=[(i,j) for i in range(3) for j in range(3)]; idx={s:k for k,s in enumerate(sites)}
    Cm=sp.zeros(9,9)
    for (i,j) in sites:
        for (i2,j2) in sites:
            if abs(i-i2)+abs(j-j2)==1: Cm[idx[(i,j)],idx[(i2,j2)]]=sp.Rational(c4.numerator,c4.denominator)
    if alpha<1:
        D=(sp.eye(9)-Cm).inv()
        bound=D[idx[(1,1)],idx[(1,0)]]*sp.Rational(c4.numerator,c4.denominator)
        print(f"  {tr}: c1^(4) = {c4} (4c1 = {float(alpha):.4f}); exact TV(centre) for one flipped exterior slot = {tv} = {float(tv):.6f}; comparison bound D[centre,(1,0)]*c4 = {bound} = {float(bound):.6f};  bound holds: {tv<=F(str(bound))}")
    else:
        print(f"  {tr}: c1^(4) = {c4} (4c1 = {float(alpha):.4f} >= 1: criterion silent on this window); exact TV(centre) = {tv} = {float(tv):.6f}")
    sys.stdout.flush()
