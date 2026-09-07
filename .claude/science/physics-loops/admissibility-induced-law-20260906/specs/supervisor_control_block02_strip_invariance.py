"""Control 2: (1) is the row law invariant under the sweep kernel (p0 P = p0)? (2) symmetry-reduced transfer matrix,
exact Perron root and exact/interval value of the static infinite-strip center-row statistic."""
from fractions import Fraction as F
from itertools import product, permutations
import sympy as sp, time
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def dot(a,b): return sum(x*y for x,y in zip(MENU[a],MENU[b]))
def orb(a,b): d=dot(a,b); return 0 if d==1 else (1 if d==-1 else 2)
def phi_of(tr): return [[tr[orb(a,b)] for b in range(M)] for a in range(M)]
W=3; rows=list(product(range(M),repeat=W)); R=len(rows); idx={r:i for i,r in enumerate(rows)}
# rotations as signed permutations
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

for tr in [(3,1,2),(5,2,4)]:
    phi=phi_of(tr)
    def rule(s,rec):
        w=[1]*M
        for t in range(M):
            for e in rec: w[t]*=phi[t][e]
        return F(w[s],sum(w))
    p0=[F(1)]*R
    for i,r in enumerate(rows):
        for j in range(W): p0[i]*=rule(r[j],[r[j-1]] if j>0 else [])
    P=[[F(1)]*R for _ in range(R)]
    for i,r in enumerate(rows):
        for k,r2 in enumerate(rows):
            for j in range(W):
                P[i][k]*=rule(r2[j],[r[j]]+([r2[j-1]] if j>0 else []))
    p1=[sum(p0[i]*P[i][k] for i in range(R)) for k in range(R)]
    print(f"{tr}: p0 P == p0 exactly? {p1==p0};  max|p1-p0| = {max(abs(a-b) for a,b in zip(p1,p0))}")
    # joint statistic across rows under formation: P[(i-1,0) and (i,0) parallel] at stationarity
    joint_par=sum(p0[i]*P[i][k] for i,r in enumerate(rows) for k,r2 in enumerate(rows) if r[0]==r2[0])
    joint_par_mid=sum(p0[i]*P[i][k] for i,r in enumerate(rows) for k,r2 in enumerate(rows) if r[1]==r2[1])
    print(f"   formation vertical pair parallel prob: column0 {joint_par} = {float(joint_par):.6f}; column1 {joint_par_mid} = {float(joint_par_mid):.6f};  one-edge value p/(p+q+4r) = {F(tr[0],tr[0]+tr[1]+4*tr[2])}")
    # ---- static strip: symmetry-reduced transfer matrix
    def A(r):
        w=1
        for j in range(W-1): w*=phi[r[j]][r[j+1]]
        return w
    def V(r,r2):
        w=1
        for j in range(W): w*=phi[r[j]][r2[j]]
        return w
    # orbits of rows under rotations x reflection
    seen={}; orbits=[]
    for r in rows:
        if r in seen: continue
        O=set()
        for g in ROT:
            rr=tuple(rot_menu(g,a) for a in r); O.add(rr); O.add(rr[::-1])
        for x in O: seen[x]=len(orbits)
        orbits.append(sorted(O))
    K=len(orbits); print(f"   row orbits under 24 rotations x reflection: {K}")
    # quotient matrix Q[O][O'] = sum_{r' in O'} T(r, r') for a representative r in O, T(r,r') = V(r,r') A(r')
    Q=sp.zeros(K,K)
    for a,O in enumerate(orbits):
        r=O[0]
        for b,O2 in enumerate(orbits):
            Q[a,b]=sum(V(r,r2)*A(r2) for r2 in O2)
    lam=sp.symbols('lam')
    cp=sp.factor(Q.charpoly(lam).as_expr())
    print(f"   charpoly of the {K}x{K} quotient: {cp}")
    # largest real root: isolate with sympy
    poly=sp.Poly(Q.charpoly(lam).as_expr(), lam)
    roots=sp.Poly(poly).real_roots()
    lam1=max(roots)
    minpoly=sp.minimal_polynomial(lam1, lam)
    print(f"   Perron root minimal polynomial (degree {sp.degree(minpoly,lam)}): {minpoly};  lam1 ~ {sp.N(lam1,12)}")
    # eigenvector of Q at lam1 (right eigenvector = orbit-constant values of rho)
    Ml=(Q-lam1*sp.eye(K))
    ns=Ml.nullspace()
    assert len(ns)==1
    rho_orb=ns[0]
    # center-row law w(r) ∝ A(r) rho(r)^2 ; statistic f = [r0 == r1]
    num=sum(A(r)*rho_orb[seen[r]]**2*(1 if r[0]==r[1] else 0) for r in rows)
    den=sum(A(r)*rho_orb[seen[r]]**2 for r in rows)
    s_inf=sp.nsimplify(sp.simplify(num/den))
    print(f"   static infinite-strip center-row P[parallel pair] = {sp.simplify(num/den)} ~ {sp.N(num/den,15)};  minimal polynomial: {sp.minimal_polynomial(num/den, lam)}")
    # rigorous rational interval via the minimal polynomial's isolating interval
    mp=sp.minimal_polynomial(num/den, lam)
    iv=[ (a,b) for (a,b) in sp.Poly(mp,lam).intervals() ]
    print(f"   isolating intervals of that minimal polynomial's real roots: {iv}")
    print(f"   formation value p/(p+q+4r) = {F(tr[0],tr[0]+tr[1]+4*tr[2])}")
