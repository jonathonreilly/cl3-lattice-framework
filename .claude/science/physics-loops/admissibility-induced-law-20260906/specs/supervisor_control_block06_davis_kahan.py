"""Control 4: the self-adjoint Davis-Kahan route to rigorous rational enclosures of the deep-row pair statistics."""
import sys; sys.argv=['x']
exec(open('supervisor_control_block06_feasibility.py').read().split("for W in (4,5):")[0])
from fractions import Fraction as F
import time
def isqrt_upper(x: F):
    """rational u with u^2 >= x (u >= 0), tight to 1e-40 by bisection on integers scaled."""
    from math import isqrt
    scale=10**80; n=x.numerator*scale*scale//x.denominator+1; u=isqrt(n)+1; return F(u,scale)
for W in (4,5):
    for tr in [(3,1,2),(5,2,4)]:
        t0=time.time(); rows,idx,A,V,reps,orbit_of,Q=build(tr,W); n=len(reps)
        size=[0]*n
        for r in rows: size[orbit_of[r]]+=1
        Avec=[A(rep) for rep in reps]; w=[size[o]*Avec[o] for o in range(n)]
        # self-adjointness in <.,.>_w : w_O Q_{OO'} == w_O' Q_{O'O}
        sa=all(w[o]*Q[o][p]==w[p]*Q[p][o] for o in range(n) for p in range(n))
        mid=(W//2-1,W//2)
        cmid=[F(sum(1 for r in rows if orbit_of[r]==o and r[mid[0]]==r[mid[1]]),size[o]) for o in range(n)]
        cedge=[F(sum(1 for r in rows if orbit_of[r]==o and r[0]==r[1]),size[o]) for o in range(n)]
        trQ2=sum(Q[o][p]*Q[p][o] for o in range(n) for p in range(n))
        y=[1]*n
        for _ in range(40): y=[sum(Q[i][j]*y[j] for j in range(n)) for i in range(n)]
        Qy=[sum(Q[i][j]*y[j] for j in range(n)) for i in range(n)]
        ny=sum(w[o]*y[o]*y[o] for o in range(n))            # ||y||_w^2 (integer)
        mu=F(sum(w[o]*y[o]*Qy[o] for o in range(n)),ny)     # Rayleigh quotient
        res2=F(sum(w[o]*(Qy[o]-mu*y[o])**2 for o in range(n)),ny)   # ||Qy - mu y||_w^2 / ||y||_w^2
        lo=min(F(Qy[o],y[o]) for o in range(n)); hi=max(F(Qy[o],y[o]) for o in range(n))   # Collatz-Wielandt
        lam2_bound=isqrt_upper(F(trQ2)-lo*lo)                # lambda_2 <= sqrt(tr Q^2 - lambda_1^2)
        delta=mu-lam2_bound
        eps=isqrt_upper(res2)/delta                          # sin theta <= r/delta
        dist=isqrt_upper(F(2))*eps                           # ||x - y||_w <= sqrt2 sin theta (unit vectors)
        s_mid=F(sum(w[o]*y[o]*y[o]*cmid[o].numerator*1 for o in range(n)),1)  # placeholder
        smid=sum(F(w[o]*y[o]*y[o],ny)*cmid[o] for o in range(n)); sedge=sum(F(w[o]*y[o]*y[o],ny)*cedge[o] for o in range(n))
        f=F(tr[0],tr[0]+tr[1]+4*tr[2])
        print(f"W={W} {tr}: orbits {n}; self-adjoint in <,>_w: {sa}; lambda_1 CW [{float(lo):.12f},{float(hi):.12f}]; mu={float(mu):.12f}; lambda_2 bound {float(lam2_bound):.6e} (ratio {float(lam2_bound/lo):.4f}); residual {float(isqrt_upper(res2)):.3e}; sin-theta bound {float(eps):.3e}", flush=True)
        print(f"   s_mid in [{float(smid-2*dist):.20f}, {float(smid+2*dist):.20f}]; s_edge in [{float(sedge-2*dist):.20f}, {float(sedge+2*dist):.20f}]; formation f={float(f):.12f}; excluded: {not (smid-2*dist<=f<=smid+2*dist)} [{time.time()-t0:.0f}s]", flush=True)
