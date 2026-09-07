"""Control 2: (a) rho_yz = sensitivity of the y-marginal of the pair block to an outer x-slot (second order);
(b) exact W1 lower bound rho + rho_yz and the sequential upper bound rho(1+c1) at the silent triples;
(c) the two-site provable criterion 5*rho*(1+c1) along the lines (t,1,1) and (t,t,1): the crossing vs the one-site t*."""
import sys; sys.path.insert(0,'.')
exec(open('control_b04.py').read().split("for tr in [(3,1,2)")[0])
def block_marginals(tr, eta_y, eta_x, t):
    phi=phi_of(tr)
    wy=[1]*M
    for s in range(M):
        for e in eta_y: wy[s]*=phi[s][e]
    wx=[1]*M
    for s in range(M):
        for e in list(eta_x)+[t]: wx[s]*=phi[s][e]
    joint=[[wx[a]*phi[a][b]*wy[b] for b in range(M)] for a in range(M)]
    Z=sum(sum(r) for r in joint)
    mx=[F(sum(joint[a]),Z) for a in range(M)]; my=[F(sum(joint[a][b] for a in range(M)),Z) for b in range(M)]
    return mx,my
def rho_yz(tr):
    best=F(0)
    for eta_y in cwr(range(M),5):
        for eta_x in cwr(range(M),4):
            mys=[block_marginals(tr,eta_y,eta_x,t)[1] for t in range(M)]
            for ta,tb in PAIRS:
                v=sum(abs(a-b) for a,b in zip(mys[ta],mys[tb]))/2
                if v>best: best=v
    return best
for tr in []:
    t0=time.time(); c=c1(tr); rho,_=block_rho(tr); ryz=rho_yz(tr)
    print(f"{tr}: rho={float(rho):.5f} rho_yz={ryz} ({float(ryz):.5f}); W1 per slot in [{float(rho+ryz):.5f}, {float(rho*(1+c)):.5f}]; block sum B/|V| in [{float(5*(rho+ryz)):.4f}, {float(5*rho*(1+c)):.4f}]  [{time.time()-t0:.0f}s]", flush=True)
def line_tr(line,t):
    fr=[t if x=='t' else F(1) for x in line]; L=1
    import math
    for x in fr: L=L*x.denominator//math.gcd(L,x.denominator)
    return tuple(int(x*L) for x in fr)
for line,name in [(('t','1','1'),"(t,1,1)"),(('t','t','1'),"(t,t,1)")]:
    prev=None
    for k in range(42,80,2):
        t=F(k,40); tr=line_tr(line,t); c=c1(tr); rho,_=block_rho(tr); two=5*rho*(1+c); one=6*c
        flag=""
        if prev is not None and (prev[1]<1)!=(two<1): flag=" <-- two-site crossing"
        if prev is not None and (prev[2]<1)!=(one<1): flag+=" <-- one-site crossing"
        print(f"  {name} t={t}: 6c1={float(one):.4f} 5rho(1+c1)={float(two):.4f} rho/c1={float(rho/c):.4f}{flag}", flush=True)
        prev=(t,two,one)
