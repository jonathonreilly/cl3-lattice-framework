import sys; sys.argv=['x']
exec(open('supervisor_control_block06_feasibility.py').read().split("for W in (4,5):")[0])
from fractions import Fraction as F
import sympy as sp, time
PRIMES=(2**61-1, 2**89-1)
def rank_mod(vecs, p):
    rows=[[x % p for x in v] for v in vecs]; r=0; ncol=len(rows[0]) if rows else 0
    for c in range(ncol):
        piv=next((i for i in range(r,len(rows)) if rows[i][c]), None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]; inv=pow(rows[r][c],p-2,p)
        rows[r]=[(x*inv)%p for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                f=rows[i][c]; rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows): break
    return r
def krylov(Qm, v, maxk):
    n=len(Qm); vecs=[v[:]]
    for k in range(maxk):
        for p in PRIMES:
            pass
        r=rank_mod(vecs,PRIMES[0])
        if r<len(vecs):
            assert rank_mod(vecs,PRIMES[1])<len(vecs)
            return len(vecs)-1, vecs
        vecs.append([sum(Qm[i][j]*vecs[-1][j] for j in range(n)) for i in range(n)])
    return None, vecs
def minpoly_rel(vecs, d):
    """solve sum_{k<d} c_k x_k = -x_d exactly (Fractions) using d independent rows chosen mod p, verify on all rows."""
    n=len(vecs[0]); p=PRIMES[0]
    # choose d independent rows of the n x d matrix [x_0..x_{d-1}] mod p
    cols=[[vecs[k][i] for k in range(d)] for i in range(n)]
    chosen=[]; basis=[]
    for i in range(n):
        cand=basis+[[x%p for x in cols[i]]]
        if rank_mod(cand,p)==len(cand): basis=cand; chosen.append(i)
        if len(chosen)==d: break
    Mx=sp.Matrix([[vecs[k][i] for k in range(d)] for i in chosen]); rhs=sp.Matrix([-vecs[d][i] for i in chosen])
    sol=Mx.LUsolve(rhs)
    ok=all(sum(sol[k]*vecs[k][i] for k in range(d))==-vecs[d][i] for i in range(n))
    lam=sp.symbols('lam'); poly=sp.Poly(lam**d+sum(sol[k]*lam**k for k in range(d)),lam)
    return poly, ok
for W in (4,5):
    for tr in [(3,1,2),(5,2,4)]:
        t0=time.time(); rows,idx,A,V,reps,orbit_of,Q=build(tr,W); n=len(reps)
        d,vecs=krylov(Q,[1]*n,n+1); t1=time.time()-t0
        print(f"W={W} {tr}: orbits {n}; Krylov dimension of Q on 1 = {d} [{t1:.0f}s]", flush=True)
        t0=time.time(); poly,ok=minpoly_rel(vecs,d); fl=sp.factor_list(poly.as_expr())[1]
        print(f"   relative minimal polynomial verified on all rows: {ok}; factor degrees {[sp.Poly(f).degree() for f,_ in fl]}; coefficient digits max {max(len(str(c)) for c in poly.all_coeffs())} [{time.time()-t0:.0f}s]", flush=True)
        t0=time.time(); rr=poly.real_roots(); pos=[r for r in rr if r>0]
        print(f"   real roots {len(rr)} of degree {poly.degree()}; largest ~ {sp.N(max(pos),18)} [{time.time()-t0:.0f}s]", flush=True)
