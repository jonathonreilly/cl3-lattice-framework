"""S4: Krylov dimension by my own modular rank with DIFFERENT primes; exact certification; irreducibility timings."""
from core import *
import sympy as sp, time
P1=(1<<127)-1        # different from the controls' 2^61-1, 2^89-1
P2=1000000000000000003
def rank_mod(vecs,p):
    rows=[[x%p for x in v] for v in vecs]; r=0; nc=len(rows[0])
    for c in range(nc):
        piv=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]; inv=pow(rows[r][c],p-2,p)
        rows[r]=[(x*inv)%p for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                f=rows[i][c]; rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows): break
    return r
lam=sp.symbols('lam')
for W in (4,5):
    for tr in ((3,1,2),(5,2,4)):
        t0=time.time(); D=build(tr,W); n=D['n']; Q=D['Q']
        vecs=[[1]*n]; d=None
        while len(vecs)<=n:
            r1=rank_mod(vecs,P1)
            if r1<len(vecs):
                r2=rank_mod(vecs,P2)
                d=len(vecs)-1; break
            vecs.append([sum(Q[i][j]*vecs[-1][j] for j in range(n)) for i in range(n)])
        tk=time.time()-t0
        print(f"W={W} {tr}: n={n}  Krylov dim (p=2^127-1) = {d} ; confirm p={P2}: {rank_mod(vecs,P2)==d} [{tk:.0f}s]",flush=True)
        # exact relative minimal polynomial (rational solve, verified on ALL n rows -> proves d exactly)
        t1=time.time()
        Mx=sp.Matrix([[vecs[k][i] for k in range(d)] for i in range(n)]); rhs=sp.Matrix([-vecs[d][i] for i in range(n)])
        sol=Mx.solve_least_squares(rhs) if False else None
        # pick d rows independent mod P1
        chosen=[];basis=[]
        for i in range(n):
            cand=basis+[[vecs[k][i]%P1 for k in range(d)]]
            if rank_mod(cand,P1)==len(cand): basis=cand; chosen.append(i)
            if len(chosen)==d: break
        Ms=sp.Matrix([[vecs[k][i] for k in range(d)] for i in chosen]); rs=sp.Matrix([-vecs[d][i] for i in chosen])
        sol=Ms.LUsolve(rs)
        ok=all(sum(sol[k]*vecs[k][i] for k in range(d))==-vecs[d][i] for i in range(n))
        poly=sp.Poly(lam**d+sum(sol[k]*lam**k for k in range(d)),lam)
        print(f"   exact minpoly verified on all {n} rows: {ok}; degree {poly.degree()}; max coeff digits {max(len(str(c)) for c in poly.all_coeffs())} [{time.time()-t1:.0f}s]",flush=True)
        if d<=30:
            t2=time.time(); fl=sp.factor_list(poly.as_expr())[1]
            degs=[sp.Poly(f,lam).degree() for f,_ in fl]
            print(f"   sympy factor: degrees {degs}  irreducible {degs==[d]}  [factor time {time.time()-t2:.1f}s]",flush=True)
            t3=time.time(); rr=poly.real_roots()
            print(f"   real roots {len(rr)} of {d}: all real {len(rr)==d} [real_roots time {time.time()-t3:.1f}s]",flush=True)
        else:
            print(f"   d={d}: factorization and real-root count NOT attempted here either.",flush=True)
