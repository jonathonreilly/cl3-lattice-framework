"""Supervisor control (block 03, after the refuter lens): D1 root counts; D2 second crossings on each line;
D3 c4 > c1 at (2,5,3); D5/D6 rigorous competitor sweep (exact Lipschitz certificates) on the isolating
intervals and on the region intervals of each line. Exact arithmetic only (Fractions, sympy Poly)."""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr, combinations
import sympy as sp, time, sys
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def orb(a,b):
    d=sum(x*y for x,y in zip(MENU[a],MENU[b])); return 0 if d==1 else (1 if d==-1 else 2)
def conds_at(tr, eta, deg):
    """exact conditionals (list over the flipped slot value) for shell multiset eta (deg-1 entries) + slot value."""
    base=[1]*M
    for s in range(M):
        for e in eta: base[s]*=tr[orb(s,e)]
    out=[]
    for tt in range(M):
        w=[base[s]*tr[orb(s,tt)] for s in range(M)]; Z=sum(w); out.append([F(x,Z) for x in w])
    return out
def tv(a,b): return sum(abs(x-y) for x,y in zip(a,b))/2
def coeff(tr, deg):
    best=F(0); arg=None; ties=0
    for eta in cwr(range(M),deg-1):
        c=conds_at(tr,eta,deg)
        for ta,tb in combinations(range(M),2):
            v=tv(c[ta],c[tb])
            if v>best: best=v; arg=(eta,ta,tb); ties=1
            elif v==best: ties+=1
    return best,arg,ties
def line_tr(line,tval):  # line: tuple of 't' or 1
    return tuple(tval if x=='t' else F(1) for x in line)
def kexp(line,eta,s,tt):  # exponent of t in w_s for shell eta + slot tt on the line
    k=0
    for e in list(eta)+[tt]:
        if line[orb(s,e)]=='t': k+=1
    return k
# ---------- D1: real-root counts of the three contract polynomials
t=sp.symbols('t')
P1=sp.Poly(t**7-2*t**5+5*t**4-8*t**3-t**2-4,t); P2=sp.Poly(4*t**7-8*t**5+5*t**4-8*t**3-t**2-1,t); P3=sp.Poly(t**7+t**5+8*t**4-5*t**3+8*t**2-4,t)
for nm,P in [("(t,1,1)",P1),("(t,t,1)",P2),("(1,1,t)",P3)]:
    rr=P.real_roots(); print(f"D1 {nm}: real roots = {len(rr)}; positive = {[sp.N(r,20) for r in rr if r>0]}", flush=True)
# ---------- D3: c4 vs c1 at (2,5,3)
c1,_,_=coeff((F(2),F(5),F(3)),6); c4,_,_=coeff((F(2),F(5),F(3)),4)
print(f"D3 (2,5,3): c1 = {c1}, c4 = {c4}, c4 > c1: {c4>c1}", flush=True)
# ---------- D2 checks at the lens's rationals
for line,tv0 in [(('1','1','t'),F(36,25)),(('1','1','t'),F(29,20)),(('t','1','1'),F(47,100)),(('t','1','1'),F(1,2))]:
    c,_,_=coeff(line_tr(line,tv0),6); print(f"D2 {line} t={tv0}: 6c1 = {6*c} ({float(6*c):.9f}) {'<1' if 6*c<1 else '>=1'}", flush=True)
# ---------- crossings on each line by scan, then exact isolation and the competitor sweep
def sixtv_minus1_poly(line,eta,ta,tb,S):
    """numerator/denominator polynomials (sympy Poly in t) of 6*sum_{s in S}(a_s-b_s)-1 on the line."""
    ka=[kexp(line,eta,s,ta) for s in range(M)]; kb=[kexp(line,eta,s,tb) for s in range(M)]
    Za=sum(t**k for k in ka); Zb=sum(t**k for k in kb)
    num=6*sum((t**ka[s])*Zb-(t**kb[s])*Za for s in range(M) if S[s])-Za*Zb
    return sp.Poly(sp.expand(num),t), sp.Poly(sp.expand(Za*Zb),t)
def lip_bound(line,eta,ta,tb,u,v):
    """exact upper bound on the Lipschitz constant of TV(t) (this shell/pair) on [u,v], 0<u<=v."""
    L=F(0)
    for tt in (ta,tb):
        ks=[kexp(line,eta,s,tt) for s in range(M)]
        Zu=sum(u**k for k in ks); Zv=sum(v**k for k in ks); dZv=sum(k*v**(k-1) for k in ks if k>0)
        for k in ks: L+=(k*v**(k-1)*Zv if k>0 else F(0))+ (v**k)*dZv
        L=L/(Zu*Zu) if False else L  # placeholder to keep structure simple
    return L
def lip_bound2(line,eta,ta,tb,u,v):
    tot=F(0)
    for tt in (ta,tb):
        ks=[kexp(line,eta,s,tt) for s in range(M)]
        Zu=sum(u**k for k in ks); Zv=sum(v**k for k in ks); dZv=sum(k*v**(k-1) for k in ks if k>0)
        for k in ks:
            tot+=((k*v**(k-1) if k>0 else F(0))*Zv + (v**k)*dZv)/(Zu*Zu)
    return tot/2
def certify_below(line,eta,ta,tb,u,v,depth=0,maxdepth=80):
    """certify 6*TV(t)-1 < 0 for all t in [u,v] by exact endpoint values + Lipschitz bound, bisecting; returns #intervals or -1."""
    tru=line_tr(line,u); trv=line_tr(line,v)
    cu=conds_at(tru,eta,6); cv=conds_at(trv,eta,6)
    vu=6*tv(cu[ta],cu[tb])-1; vv=6*tv(cv[ta],cv[tb])-1
    if vu>=0 or vv>=0: return -1
    L=lip_bound2(line,eta,ta,tb,u,v)
    if max(vu,vv)+6*L*(v-u)<0: return 1
    if depth>=maxdepth: return -1
    m=(u+v)/2
    a=certify_below(line,eta,ta,tb,u,m,depth+1,maxdepth)
    if a<0: return -1
    b=certify_below(line,eta,ta,tb,m,v,depth+1,maxdepth)
    if b<0: return -1
    return a+b
shells=list(cwr(range(M),5)); pairs=list(combinations(range(M),2))
def sweep_interval(line,u,v,exclude_poly=None,label=""):
    """for every (shell,pair): certify 6TV-1<0 on [u,v], unless its rational function (sign pattern at u) equals exclude_poly."""
    t0=time.time(); n_ok=0; n_same=0; bad=[]; ints=0
    for eta in shells:
        for ta,tb in pairs:
            r=certify_below(line,eta,ta,tb,u,v)
            if r>0: n_ok+=1; ints+=r; continue
            # not certified: compare the rational function to the displayed one
            cu=conds_at(line_tr(line,u),eta,6); S=[cu[ta][s]-cu[tb][s]>=0 for s in range(M)]
            num,den=sixtv_minus1_poly(line,eta,ta,tb,S)
            g=sp.gcd(num,den); num=sp.Poly(sp.quo(num,g),t)
            if exclude_poly is not None and (sp.Poly(num,t).monic()==exclude_poly.monic()): n_same+=1
            else: bad.append((eta,ta,tb,num.as_expr()))
    print(f"   sweep {label} on [{float(u):.15f},{float(v):.15f}]: certified below {n_ok} ({ints} subintervals), identical-to-displayed {n_same}, uncertified distinct {len(bad)}  [{time.time()-t0:.0f}s]", flush=True)
    for b in bad[:5]: print("      UNCERTIFIED:",b, flush=True)
    return len(bad)==0
def find_crossing(line,scan):
    prev=None
    for val in scan:
        c,arg,ties=coeff(line_tr(line,val),6)
        if prev is not None and (6*prev[0]<1)!=(6*c<1):
            return prev[1],val,(arg if 6*c<1 else prev[2]),ties
        prev=(c,val,arg)
    return None
def analyze_line(line,name,scan,tag):
    fc=find_crossing(line,scan)
    if fc is None: print(f"{name} {tag}: no crossing on the scan", flush=True); return None
    lo,hi,arg,ties=fc; eta,ta,tb=arg
    # sign pattern at the in-region end
    inreg=lo if 6*coeff(line_tr(line,lo),6)[0]<1 else hi
    c=conds_at(line_tr(line,inreg),eta,6); S=[c[ta][s]-c[tb][s]>=0 for s in range(M)]
    num,den=sixtv_minus1_poly(line,eta,ta,tb,S); g=sp.gcd(num,den); num=sp.Poly(sp.quo(num,g),t)
    num=sp.Poly(num.as_expr()/sp.content(num.as_expr()) if False else num.as_expr(),t)
    roots=[r for r in num.real_roots() if min(lo,hi)<r<max(lo,hi)]
    print(f"{name} {tag}: crossing in ({lo},{hi}); pattern eta={eta} pair=({ta},{tb}) ties={ties}; polynomial (numerator of 6TV-1) = {sp.factor(num.as_expr())}; real roots total {len(num.real_roots())}; in bracket: {[sp.N(r,20) for r in roots]}", flush=True)
    r0=roots[0]
    iv=[iv for iv in num.intervals(eps=sp.Rational(1,10**15)) if iv[0][0]<=r0<=iv[0][1]][0][0]
    a=F(int(iv[0].p),int(iv[0].q)); b=F(int(iv[1].p),int(iv[1].q))
    # sup verification at both endpoints + sign change
    for ep in (a,b):
        cc,aa,tt=coeff(line_tr(line,ep),6); print(f"   endpoint t={float(ep):.16f}: 6c1-1 = {float(6*cc-1):+.3e}; argmax {aa} (ties {tt})", flush=True)
    ok=sweep_interval(line,a,b,exclude_poly=num,label=f"{name} {tag} isolating")
    print(f"   -> threshold {tag} = root of the displayed polynomial; competitor sweep on the isolating interval: {'PASS' if ok else 'FAIL'}", flush=True)
    return a,b,num
lines=[(('t','1','1'),"(t,1,1)",[F(1)+F(k,20) for k in range(1,60)],[F(1)-F(k,40) for k in range(1,39)]),
       (('t','t','1'),"(t,t,1)",[F(1)+F(k,20) for k in range(1,60)],[F(1)-F(k,40) for k in range(1,39)]),
       (('1','1','t'),"(1,1,t)",[F(1)-F(k,40) for k in range(1,39)],[F(1)+F(k,20) for k in range(1,100)])]
for line,name,scanA,scanB in lines:
    T0=time.time()
    A=analyze_line(line,name,scanA,"crossing 1"); B=analyze_line(line,name,scanB,"crossing 2")
    if A and B:
        # region interval between the two crossings: certify 6c1<1 on [inner ends]
        a1,b1,_=A; a2,b2,_=B
        lo_in=max(min(b1,b2),min(a1,a2)); hi_in=min(max(a1,a2),max(b1,b2))
        lo_in=min(b1,b2) if True else lo_in  # inner endpoints: the isolating intervals' ends facing t=1
        # determine which isolating interval is below 1 and which above
        lowiv,highiv=(A[:2],B[:2]) if A[0]<B[0] else (B[:2],A[:2])
        u=lowiv[1]; v=highiv[0]
        ok=sweep_interval(line,u,v,label=f"{name} region")
        print(f"{name}: REGION on the line = ({float(lowiv[0]):.12f}.., {float(highiv[1]):.12f}..) ; certificate 6c1<1 on [{float(u):.12f},{float(v):.12f}]: {'PASS' if ok else 'FAIL'}  [{time.time()-T0:.0f}s]", flush=True)
