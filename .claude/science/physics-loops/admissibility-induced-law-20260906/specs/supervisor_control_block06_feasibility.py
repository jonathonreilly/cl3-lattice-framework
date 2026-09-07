"""Feasibility control, block 06: static strip widths 4 and 5. Orbits under G (24 proper rotations x row reversal),
quotient Q, charpoly timing at W=4, Collatz-Wielandt bounds for lambda_1, the Birkhoff coefficient, finite-n center-row
pair statistic. Exact ints/Fractions; floats only as printed labels."""
from fractions import Fraction as F
from itertools import product, permutations
import time, sys
import sympy as sp
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def orb(a,b):
    d=sum(u*v for u,v in zip(MENU[a],MENU[b])); return 0 if d==1 else (1 if d==-1 else 2)
# 24 proper rotations as signed permutation matrices with det +1, acting on menu indices
def rotations():
    out=[]
    for perm in permutations(range(3)):
        for signs in product([1,-1],repeat=3):
            Mx=[[0]*3 for _ in range(3)]
            for i in range(3): Mx[i][perm[i]]=signs[i]
            det=sp.Matrix(Mx).det()
            if det==1:
                img=[]
                for v in MENU:
                    w=tuple(sum(Mx[i][j]*v[j] for j in range(3)) for i in range(3)); img.append(MENU.index(w))
                out.append(tuple(img))
    return out
ROT=rotations(); assert len(ROT)==24
def group_images(rho):
    W=len(rho); out=set()
    for g in ROT:
        r=tuple(g[x] for x in rho); out.add(r); out.add(tuple(reversed(r)))
    return out
def orbits(W):
    seen={}; reps=[]
    for rho in product(range(M),repeat=W):
        if rho in seen: continue
        imgs=group_images(rho); k=len(reps); reps.append(rho)
        for r in imgs: seen[r]=k
    return reps,seen
def build(tr,W):
    phi=[[tr[orb(a,b)] for b in range(M)] for a in range(M)]
    rows=list(product(range(M),repeat=W)); idx={r:i for i,r in enumerate(rows)}
    def A(r):
        w=1
        for j in range(W-1): w*=phi[r[j]][r[j+1]]
        return w
    def V(r,r2):
        w=1
        for j in range(W): w*=phi[r[j]][r2[j]]
        return w
    reps,orbit_of=orbits(W); n=len(reps)
    Q=[[0]*n for _ in range(n)]
    for i,rep in enumerate(reps):
        for r2 in rows:
            Q[i][orbit_of[r2]]+=V(rep,r2)*A(r2)
    return rows,idx,A,V,reps,orbit_of,Q
def cw_bounds(Q,k):
    n=len(Q); x=[1]*n
    for _ in range(k): x=[sum(Q[i][j]*x[j] for j in range(n)) for i in range(n)]
    y=[sum(Q[i][j]*x[j] for j in range(n)) for i in range(n)]
    ratios=[F(y[i],x[i]) for i in range(n)]
    return min(ratios),max(ratios),x
def birkhoff_kappa(Q):
    n=len(Q); best=F(0)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                for l in range(k+1,n):
                    c=F(Q[i][k]*Q[j][l],Q[j][k]*Q[i][l])
                    if c>best: best=c
                    if 1/c>best: best=1/c
    return best
for W in (4,5):
    for tr in [(3,1,2)]:
        t0=time.time(); rows,idx,A,V,reps,orbit_of,Q=build(tr,W); n=len(reps)
        print(f"W={W} {tr}: row states {len(rows)}, orbits {n}, Q built in {time.time()-t0:.0f}s; max entry digits {max(len(str(x)) for r in Q for x in r)}", flush=True)
        t0=time.time(); lo,hi,x=cw_bounds(Q,12); print(f"  Collatz-Wielandt after 12 powers: lambda_1 in [{float(lo):.9f}, {float(hi):.9f}] width {float(hi-lo):.3e} [{time.time()-t0:.1f}s]", flush=True)
        lo2,hi2,_=cw_bounds(Q,30); print(f"  after 30 powers: [{float(lo2):.12f}, {float(hi2):.12f}] width {float(hi2-lo2):.3e}", flush=True)
        if n<=60:
            t0=time.time(); kappa=birkhoff_kappa(Q); tau=(sp.sqrt(kappa)-1)/(sp.sqrt(kappa)+1)
            print(f"  Birkhoff cross-ratio max kappa={float(kappa):.4e}, contraction tau~{float(tau):.4f} [{time.time()-t0:.0f}s]", flush=True)
            t0=time.time(); cp=sp.Matrix(Q).charpoly(); print(f"  charpoly degree {cp.degree()} in {time.time()-t0:.0f}s; factor count {len(sp.factor_list(cp.as_expr())[1])}", flush=True)
            fac=sp.factor_list(cp.as_expr())[1]; print("  factor degrees:", [sp.Poly(f,cp.gens[0]).degree() for f,_ in fac], flush=True)
        else:
            print("  (W=5: charpoly skipped; Birkhoff on a 20x20 sample of orbits:)", flush=True)
            sub=[[Q[i][j] for j in range(20)] for i in range(20)]; kappa=birkhoff_kappa(sub); print(f"  sample kappa={float(kappa):.4e}", flush=True)
        # finite-n center-row pair-parallel statistic (exact) via full T for small n
        if W==4:
            t0=time.time()
            Avec=[A(r) for r in rows]; N=len(rows)
            Tm=[[V(r,r2)*Avec[idx[r2]] for r2 in rows] for r in rows]
            for nrows in (3,5,7):
                c=nrows//2
                left=Avec[:]
                for _ in range(c): left=[sum(left[i]*Tm[i][j] for i in range(N)) for j in range(N)]
                right=[1]*N
                for _ in range(nrows-1-c): right=[sum(Tm[i][j]*right[j] for j in range(N)) for i in range(N)]
                w=[left[i]*right[i] for i in range(N)]; Z=sum(w)
                s=F(sum(w[i] for i,r in enumerate(rows) if r[0]==r[1]),Z)
                print(f"  W=4 center-row pair-parallel (cols 0,1) n={nrows}: {float(s):.10f}", flush=True)
            print(f"  [{time.time()-t0:.0f}s]", flush=True)
