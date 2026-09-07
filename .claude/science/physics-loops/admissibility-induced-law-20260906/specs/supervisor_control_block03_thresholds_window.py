"""Fast control: exact thresholds along lines (sign-pattern route, no Abs simplification) and the 3x3 window bound check (integers)."""
from fractions import Fraction as F
from itertools import product
import sympy as sp, sys, time
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def dot(a,b): return sum(x*y for x,y in zip(MENU[a],MENU[b]))
def orb(a,b): d=dot(a,b); return 0 if d==1 else (1 if d==-1 else 2)
def phi_of(tr): return [[tr[orb(a,b)] for b in range(M)] for a in range(M)]
def coeff(tr, deg):
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
t=sp.symbols('t', positive=True)
def tv_rational_at_pattern(trsym, eta, ta, tb, signs):
    phi=[[trsym[orb(a,b)] for b in range(M)] for a in range(M)]
    base=[sp.Integer(1)]*M
    for s in range(M):
        for e in eta: base[s]*=phi[s][e]
    conds=[]
    for tt in (ta,tb):
        w=[base[s]*phi[s][tt] for s in range(M)]; Z=sum(w); conds.append([w[s]/Z for s in range(M)])
    return sp.cancel(sum(signs[s]*(conds[0][s]-conds[1][s]) for s in range(M))/2)
print("=== thresholds along lines ===", flush=True)
for line,name,vals in [((t,1,1),"(t,1,1)",[F(1)+F(k,8) for k in range(1,60)]), ((t,t,1),"(t,t,1)",[F(1)+F(k,8) for k in range(1,60)]), ((1,1,t),"(1,1,t)",[F(k,8) for k in range(1,80)])]:
    prev=None
    for val in vals:
        tr=tuple(F(str(sp.sympify(v).subs(t,sp.Rational(val.numerator,val.denominator)))) for v in line)
        c,arg=coeff(tr,6)
        if prev is not None and (6*prev[0]<1)!=(6*c<1):
            eta,ta,tb=arg
            # sign pattern at the crossing (from the exact conditionals at 'val')
            phi=phi_of(tr); base=[1]*M
            for s in range(M):
                for e in eta: base[s]*=phi[s][e]
            conds=[]
            for tt in (ta,tb):
                w=[base[s]*phi[s][tt] for s in range(M)]; Z=sum(w); conds.append([F(x,Z) for x in w])
            signs=[1 if conds[0][s]-conds[1][s]>=0 else -1 for s in range(M)]
            expr=tv_rational_at_pattern(line,eta,ta,tb,signs)
            num,den=sp.fraction(sp.together(6*expr-1))
            roots=[r for r in sp.Poly(num,t).real_roots() if r>0]
            print(f"  {name}: crossing between t={prev[1]} and t={val}; pattern {arg}; 6c1(t)-1 = {sp.factor(6*expr-1)}", flush=True)
            for r0 in roots:
                # verify: at t = r0 the sup over ALL patterns equals this pattern's value (check at a close rational)
                rr=sp.Rational(str(sp.N(r0,30))) if not r0.is_Rational else r0
                trr=tuple(F(str(sp.sympify(v).subs(t,rr))) for v in line)
                c_all,arg_all=coeff(trr,6)
                print(f"     candidate threshold t* = {r0} ~ {sp.N(r0,15)};  at t~t*: 6*sup c1 = {float(6*c_all):.9f} (pattern {arg_all})", flush=True)
            break
        prev=(c,val)
print("\n=== 3x3 planar window: exact centre-site TV for one flipped exterior slot vs the comparison bound ===", flush=True)
W=3; rows=list(product(range(M),repeat=W)); R=len(rows)
def center_marginal(tr, ext):
    phi=phi_of(tr)
    def A(i,r):
        w=1
        for j in range(W-1): w*=phi[r[j]][r[j+1]]
        for j in range(W):
            for side in ('L','R','B','T'):
                if (i,j,side) in ext: w*=phi[r[j]][ext[(i,j,side)]]
        return w
    Vm=[[phi[r[0]][r2[0]]*phi[r[1]][r2[1]]*phi[r[2]][r2[2]] for r2 in rows] for r in rows]
    A0=[A(0,r) for r in rows]; A1=[A(1,r) for r in rows]; A2=[A(2,r) for r in rows]
    # left vector after row 0 -> row 1; right vector from row 2 -> row 1
    left=[sum(A0[i0]*Vm[i0][i1] for i0 in range(R)) for i1 in range(R)]
    right=[sum(Vm[i1][i2]*A2[i2] for i2 in range(R)) for i1 in range(R)]
    marg=[0]*M
    for i1,r1 in enumerate(rows): marg[r1[1]]+=left[i1]*A1[i1]*right[i1]
    Z=sum(marg); return [F(x,Z) for x in marg]
for tr in [(2,1,2),(3,2,2),(5,4,4),(3,1,2)]:
    c4,_=coeff(tr,4); alpha=4*c4
    ext0={}
    for i in range(3): ext0[(i,0,'L')]=0; ext0[(i,2,'R')]=0
    for j in range(3): ext0[(0,j,'B')]=0; ext0[(2,j,'T')]=0
    m0=center_marginal(tr,ext0); ext1=dict(ext0); ext1[(1,0,'L')]=1; m1=center_marginal(tr,ext1)
    tv=sum(abs(a-b) for a,b in zip(m0,m1))/2
    sites=[(i,j) for i in range(3) for j in range(3)]; idx={s:k for k,s in enumerate(sites)}
    c4r=sp.Rational(c4.numerator,c4.denominator)
    Cm=sp.Matrix(9,9,lambda a,b: c4r if abs(sites[a][0]-sites[b][0])+abs(sites[a][1]-sites[b][1])==1 else 0)
    if alpha<1:
        D=(sp.eye(9)-Cm).inv(); bound=D[idx[(1,1)],idx[(1,0)]]*c4r
        print(f"  {tr}: c1^(4) = {c4} (4c1 = {float(alpha):.4f}); exact TV(centre) = {tv} = {float(tv):.7f}; bound D[centre,(1,0)]*c4 = {bound} = {float(bound):.7f}; holds: {tv<=F(str(bound))}", flush=True)
    else:
        print(f"  {tr}: c1^(4) = {c4} (4c1 = {float(alpha):.4f} >= 1, criterion silent on the window); exact TV(centre) = {tv} = {float(tv):.7f}", flush=True)
