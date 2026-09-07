"""Supervisor control: exact algebraic enclosure of the static infinite-strip center-row pair-parallel probability (width 3)."""
from fractions import Fraction as F
from itertools import product, permutations
import sympy as sp, sys, time
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def dot(a,b): return sum(x*y for x,y in zip(MENU[a],MENU[b]))
def orb(a,b): d=dot(a,b); return 0 if d==1 else (1 if d==-1 else 2)
def rots():
    out=[]
    for perm in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3)); det=(-1 if inv%2 else 1)*signs[0]*signs[1]*signs[2]
            if det==1: out.append((perm,signs))
    return out
ROT=rots()
def rot_menu(r,a):
    perm,signs=r; v=MENU[a]; out=[0,0,0]
    for i in range(3): out[perm[i]]=signs[i]*v[i]
    return MENU.index(tuple(out))
W=3; rows=list(product(range(M),repeat=W))
lam, s = sp.symbols('lam s')
for tr in [(3,1,2),(5,2,4)]:
    t0=time.time()
    phi=[[tr[orb(a,b)] for b in range(M)] for a in range(M)]
    A=lambda r: phi[r[0]][r[1]]*phi[r[1]][r[2]]
    V=lambda r,r2: phi[r[0]][r2[0]]*phi[r[1]][r2[1]]*phi[r[2]][r2[2]]
    seen={}; orbits=[]
    for r in rows:
        if r in seen: continue
        O=set()
        for g in ROT:
            rr=tuple(rot_menu(g,a) for a in r); O.add(rr); O.add(rr[::-1])
        for x in O: seen[x]=len(orbits)
        orbits.append(sorted(O))
    K=len(orbits)
    Q=sp.Matrix(K,K,lambda a,b: sum(V(orbits[a][0],r2)*A(r2) for r2 in orbits[b]))
    cp=sp.Poly(Q.charpoly(lam).as_expr(), lam)
    fac=sp.factor_list(cp.as_expr())
    # the Perron root: largest real root; find the irreducible factor containing it
    rr=cp.real_roots()
    lam1=max(rr)
    mfac=[f for f,_ in fac[1] if sp.Poly(f,lam).degree()>0 and abs(sp.Poly(f,lam).eval(lam1))==0 or sp.Poly(f,lam).eval(lam1)==0]
    m=sp.Poly(mfac[0],lam) if mfac else cp
    # exact isolating interval for lam1 by Sturm bisection to width 1e-32
    ivs=m.intervals(eps=sp.Rational(1,10**32))
    lo,hi=[iv for iv in ivs][-1][0]
    print(f"{tr}: K={K} orbits; charpoly factors: {fac[1]}; lam1 in [{sp.N(lo,25)}, {sp.N(hi,25)}] (width {sp.N(hi-lo,3)}), minimal poly degree {m.degree()}", flush=True)
    # eigenvector over Q(lam): adjugate column of (Q - lam I), reduced mod m(lam)
    Ml=Q-lam*sp.eye(K)
    adj=Ml.adjugate()
    col=[sp.rem(sp.expand(adj[i,0]), m.as_expr(), lam) for i in range(K)]
    if all(c==0 for c in col):
        col=[sp.rem(sp.expand(adj[i,1]), m.as_expr(), lam) for i in range(K)]
    # residual check mod m: (Q - lam I) col == 0 mod m
    res=[sp.rem(sp.expand(sum(Ml[i,j]*col[j] for j in range(K))), m.as_expr(), lam) for i in range(K)]
    print(f"   eigenvector residual mod m: {all(r==0 for r in res)}", flush=True)
    rho=lambda r: col[seen[r]]
    num=sp.rem(sp.expand(sum(A(r)*rho(r)**2*(1 if r[0]==r[1] else 0) for r in rows)), m.as_expr(), lam)
    den=sp.rem(sp.expand(sum(A(r)*rho(r)**2 for r in rows)), m.as_expr(), lam)
    R=sp.Poly(sp.resultant(m.as_expr(), sp.expand(s*den-num), lam), s)
    Rfac=sp.factor_list(R.as_expr())
    print(f"   resultant in s: degree {R.degree()}; factors {[(sp.Poly(f,s).degree(),e) for f,e in Rfac[1]]}", flush=True)
    # identify: evaluate num/den at lo and hi (rationals), bound the variation
    def sval(x): return sp.Rational(num.subs(lam,x))/sp.Rational(den.subs(lam,x))
    slo,shi=sval(lo),sval(hi)
    print(f"   s(lo)={sp.N(slo,25)}  s(hi)={sp.N(shi,25)}  |diff|={sp.N(abs(slo-shi),3)}", flush=True)
    # Lipschitz bound of s on [lo,hi]: |s'| <= (|N'||D| + |N||D'|)/D^2 with crude bounds using max |coeff| * hi^k
    N_=sp.Poly(num,lam); D_=sp.Poly(den,lam)
    def bound_abs(P_):  # sum |c_k| * hi^k  (an upper bound of |P| on [0,hi])
        return sum(abs(c)*hi**k for (k,),c in P_.terms())
    Dmin=min(abs(sp.Rational(den.subs(lam,x))) for x in (lo,hi))  # not rigorous alone; refine: D' bound
    Dp=D_.diff(lam); Np=N_.diff(lam)
    Dvar=bound_abs(Dp)*(hi-lo)
    Dlow=Dmin-Dvar
    L=(bound_abs(Np)*bound_abs(D_)+bound_abs(N_)*bound_abs(Dp))/Dlow**2
    width=L*(hi-lo)
    print(f"   rigorous: D >= {sp.N(Dlow,5)} on the interval; Lipschitz L <= {sp.N(L,5)}; |s - s(lo)| <= {sp.N(width,3)}", flush=True)
    # which real root of R lies within s(lo) +- width?
    sivs=[f for f,_ in Rfac[1]]
    for f,_ in Rfac[1]:
        Pf=sp.Poly(f,s)
        if Pf.degree()==0: continue
        for (a,b),_mult in Pf.intervals(eps=sp.Rational(1,10**30)):
            inside = (a <= slo+width and b >= slo-width)
            print(f"      real root of factor deg {Pf.degree()} in [{sp.N(a,22)},{sp.N(b,22)}]  {'<-- s_inf' if inside else ''}; contains p/(p+q+4r)={F(tr[0],tr[0]+tr[1]+4*tr[2])}? {a<=F(tr[0],tr[0]+tr[1]+4*tr[2])<=b}", flush=True)
    # second eigenvalue: other real roots of the charpoly and complex roots' moduli (numeric only here)
    others=[x for x in cp.all_roots() if x!=lam1] if cp.degree()<=8 else []
    print(f"   other roots (numeric, non-evidence): {[sp.N(abs(x),8) for x in others]}; ratio max|other|/lam1 ~ {sp.N(max(abs(x) for x in others)/lam1,6) if others else 'n/a'}   [{time.time()-t0:.1f}s]", flush=True)
