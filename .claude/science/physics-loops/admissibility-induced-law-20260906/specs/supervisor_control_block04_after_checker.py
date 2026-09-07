"""Control 3 (after the checker): sigma = sup over instances of TV(m_x)+TV(m_y) (one supremum), B_V = 10 sigma exactly;
the disjoint-support coupling attaining W_1 = TV(m_x)+TV(m_y) built explicitly and checked on instances."""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr, combinations
import time
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def orb(a,b):
    d=sum(u*v for u,v in zip(MENU[a],MENU[b])); return 0 if d==1 else (1 if d==-1 else 2)
def phi_of(tr): return [[tr[orb(a,b)] for b in range(M)] for a in range(M)]
PAIRS=list(combinations(range(M),2))
def joint(phi,eta_y,eta_x_slot):
    wy=[1]*M; wx=[1]*M
    for s in range(M):
        for e in eta_y: wy[s]*=phi[s][e]
        for e in eta_x_slot: wx[s]*=phi[s][e]
    return [[wx[a]*phi[a][b]*wy[b] for b in range(M)] for a in range(M)]
def margs(J):
    Z=sum(map(sum,J)); return [F(sum(J[a]),Z) for a in range(M)],[F(sum(J[a][b] for a in range(M)),Z) for b in range(M)],Z
def tv(p,q): return sum(abs(x-y) for x,y in zip(p,q))/2
def sigma_of(tr):
    phi=phi_of(tr); best=F(0); arg=None
    for eta_y in cwr(range(M),5):
        for eta_x in cwr(range(M),4):
            ms=[margs(joint(phi,eta_y,eta_x+(t,))) for t in range(M)]
            for ta,tb in PAIRS:
                v=tv(ms[ta][0],ms[tb][0])+tv(ms[ta][1],ms[tb][1])
                if v>best: best=v; arg=(eta_y,eta_x,ta,tb)
    return best,arg
def optimal_coupling(J,J2):
    """x maximal; residual x-mass paired through the y-residual measures' maximal coupling with posteriors on s, s'."""
    Z,Z2=sum(map(sum,J)),sum(map(sum,J2))
    mu={(a,b):F(J[a][b],Z) for a in range(M) for b in range(M)}; nu={(a,b):F(J2[a][b],Z2) for a in range(M) for b in range(M)}
    mx=[sum(mu[(a,b)] for b in range(M)) for a in range(M)]; nx=[sum(nu[(a,b)] for b in range(M)) for a in range(M)]
    K=[[mu[(a,b)]/mx[a] for b in range(M)] for a in range(M)]   # same kernel for both (x-slot change)
    cp={}
    for a in range(M):                       # common x mass: y agrees
        c=min(mx[a],nx[a])
        for b in range(M):
            if c*K[a][b]>0: cp[((a,b),(a,b))]=cp.get(((a,b),(a,b)),0)+c*K[a][b]
    pe=[max(mx[a]-nx[a],0) for a in range(M)]; qe=[max(nx[a]-mx[a],0) for a in range(M)]
    R=[sum(pe[a]*K[a][b] for a in range(M)) for b in range(M)]; R2=[sum(qe[a]*K[a][b] for a in range(M)) for b in range(M)]
    mass=sum(pe)
    if mass>0:
        # maximal coupling of the residual y-measures R, R2 (equal mass)
        m=[min(R[b],R2[b]) for b in range(M)]; cm=sum(m)
        ycp={}
        for b in range(M):
            if m[b]>0: ycp[(b,b)]=ycp.get((b,b),0)+m[b]
        Re=[R[b]-m[b] for b in range(M)]; Re2=[R2[b]-m[b] for b in range(M)]; rest=mass-cm
        if rest>0:
            for b in range(M):
                for b2 in range(M):
                    if Re[b]>0 and Re2[b2]>0: ycp[(b,b2)]=ycp.get((b,b2),0)+Re[b]*Re2[b2]/rest
        for (b,b2),p in ycp.items():
            for a in range(M):
                if pe[a]*K[a][b]==0: continue
                pa=pe[a]*K[a][b]/R[b]
                for a2 in range(M):
                    if qe[a2]*K[a2][b2]==0: continue
                    pa2=qe[a2]*K[a2][b2]/R2[b2]
                    cp[((a,b),(a2,b2))]=cp.get(((a,b),(a2,b2)),0)+p*pa*pa2
    left={}; right={}
    for (u,v),p in cp.items(): left[u]=left.get(u,0)+p; right[v]=right.get(v,0)+p
    ok=all(left.get(k,0)==mu[k] for k in mu) and all(right.get(k,0)==nu[k] for k in nu) and all(p>=0 for p in cp.values())
    dH=sum(p*((u[0]!=v[0])+(u[1]!=v[1])) for (u,v),p in cp.items())
    my=[sum(mu[(a,b)] for a in range(M)) for b in range(M)]; ny=[sum(nu[(a,b)] for a in range(M)) for b in range(M)]
    return ok,dH,tv(mx,nx)+tv(my,ny)
CHECKER={(3,1,2):F(152203860,48008647),(5,2,4):F(124859962305,55627392667),(7,3,5):F(14627647143900,6157201570091)}
for tr in [(3,1,2),(5,2,4),(7,3,5),(2,1,2),(3,2,2),(5,4,4)]:
    t0=time.time(); s,arg=sigma_of(tr); B=10*s
    chk = (B==CHECKER[tr]) if tr in CHECKER else None
    print(f"{tr}: sigma={s} B_V=10sigma={B} ({float(B):.10f}) >2: {B>2}; matches checker: {chk}; argmax {arg} [{time.time()-t0:.0f}s]", flush=True)
# optimal coupling check on instances at (5,2,4)
phi=phi_of((5,2,4)); import random; random.seed(7); bad=0; n=0
for _ in range(300):
    eta_y=tuple(sorted(random.randrange(M) for _ in range(5))); eta_x=tuple(sorted(random.randrange(M) for _ in range(4))); ta,tb=random.sample(range(M),2)
    ok,dH,lb=optimal_coupling(joint(phi,eta_y,eta_x+(ta,)),joint(phi,eta_y,eta_x+(tb,))); n+=1
    if not ok or dH!=lb: bad+=1
print(f"optimal coupling at (5,2,4): {n} instances, marginals+equality failures: {bad}")
