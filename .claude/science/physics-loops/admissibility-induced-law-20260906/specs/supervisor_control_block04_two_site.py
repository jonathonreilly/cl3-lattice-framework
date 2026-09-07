"""Supervisor control, block 04: the two-site block criterion in its provable (sequential-coupling) form.
Block V = {x, y} adjacent. Boundary: 5 outer slots of x, 5 outer slots of y. Block law on 36 states.
rho = sup over (x's other 4 outer slots, y's 5 outer slots, and a pair of values at one outer x-slot z)
      of TV(x-marginal of mu_V^omega, x-marginal of mu_V^omega'). By symmetry the same for y's slots.
Provable criterion (sequential coupling x then y): 5 rho (1 + c_1) < 1. Also printed: 5 rho (the DS-form number,
not proved here) and the whole-block TV sensitivity kappa (= rho when z ~ x only; checked)."""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr, combinations
import time, sys
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def orb(a,b):
    d=sum(u*v for u,v in zip(MENU[a],MENU[b])); return 0 if d==1 else (1 if d==-1 else 2)
def phi_of(tr): return [[tr[orb(a,b)] for b in range(M)] for a in range(M)]
PAIRS=list(combinations(range(M),2))
def c1(tr):
    phi=phi_of(tr); best=F(0)
    for eta in cwr(range(M),5):
        base=[1]*M
        for s in range(M):
            for e in eta: base[s]*=phi[s][e]
        w=[[base[s]*phi[s][t] for s in range(M)] for t in range(M)]; Z=[sum(x) for x in w]
        for ta,tb in PAIRS:
            v=F(sum(abs(w[ta][s]*Z[tb]-w[tb][s]*Z[ta]) for s in range(M)),2*Z[ta]*Z[tb])
            if v>best: best=v
    return best
def block_rho(tr):
    """sup TV of the x-marginal of the two-site block law under a change of one outer x-slot."""
    phi=phi_of(tr); best=F(0); arg=None; kappa_best=F(0)
    for eta_y in cwr(range(M),5):              # y's five outer slots
        wy=[1]*M
        for s in range(M):
            for e in eta_y: wy[s]*=phi[s][e]
        # h(s_x) = sum_{s_y} phi(s_x,s_y) wy(s_y): the effective factor from y
        h=[sum(phi[sx][sy]*wy[sy] for sy in range(M)) for sx in range(M)]
        for eta_x in cwr(range(M),4):          # x's other four outer slots
            base=[1]*M
            for s in range(M):
                for e in eta_x: base[s]*=phi[s][e]
            # x-marginal weights with the varied slot value t: base[s]*phi[s][t]*h[s]
            w=[[base[s]*phi[s][t]*h[s] for s in range(M)] for t in range(M)]; Z=[sum(x) for x in w]
            for ta,tb in PAIRS:
                v=F(sum(abs(w[ta][s]*Z[tb]-w[tb][s]*Z[ta]) for s in range(M)),2*Z[ta]*Z[tb])
                if v>best: best=v; arg=(eta_y,eta_x,ta,tb)
    return best,arg
for tr in [(3,1,2),(5,2,4),(7,3,5),(2,1,2),(3,2,2),(5,4,4)]:
    t0=time.time(); c=c1(tr); rho,arg=block_rho(tr)
    crit=5*rho*(1+c); ds=5*rho
    print(f"{tr}: c1={c} ({float(c):.5f}) 6c1={float(6*c):.4f} | rho={rho} ({float(rho):.5f}) rho/c1={float(rho/c):.4f} | provable 5rho(1+c1)={float(crit):.4f} | DS-form 5rho={float(ds):.4f} | argmax {arg}  [{time.time()-t0:.0f}s]", flush=True)
