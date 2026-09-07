"""Prototype for the fold: multiset coefficient; Lipschitz lemma along a line (constant 6/u); direct bisection certificate of
6c_1 < 1 on [u,v]; competitor sweep on an isolating interval with the same constant. Exact. Timing printed."""
from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr, combinations, product
import sympy as sp, time
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def orb(a,b):
    d=sum(x*y for x,y in zip(MENU[a],MENU[b])); return 0 if d==1 else (1 if d==-1 else 2)
PAIRS=list(combinations(range(M),2)); SHELLS=list(cwr(range(M),5))
def phi_of(tr): return [[tr[orb(a,b)] for b in range(M)] for a in range(M)]
def scaled(tr):
    fr=[F(x) for x in tr]; L=1
    for x in fr: L=L*x.denominator//__import__('math').gcd(L,x.denominator)
    return tuple(int(x*L) for x in fr)
def c1_multiset(tr):
    """sup over the 252 shell multisets x 15 pairs (integer hot loop); returns (Fraction, argmax, ties, all values dict)."""
    phi=phi_of(tr); bn,bd,arg,ties=0,1,None,0
    for eta in SHELLS:
        base=[1]*M
        for s in range(M):
            for e in eta: base[s]*=phi[s][e]
        w=[[base[s]*phi[s][t] for s in range(M)] for t in range(M)]; Z=[sum(x) for x in w]
        for ta,tb in PAIRS:
            n=sum(abs(w[ta][s]*Z[tb]-w[tb][s]*Z[ta]) for s in range(M)); d=2*Z[ta]*Z[tb]
            if n*bd>bn*d: bn,bd,arg,ties=n,d,(eta,ta,tb),1
            elif n*bd==bn*d: ties+=1
    return F(bn,bd),arg,ties
def line_tr(line,t): return scaled(tuple(t if x=='t' else 1 for x in line))
def tv_pattern(tr,eta,ta,tb):
    phi=phi_of(tr); base=[1]*M
    for s in range(M):
        for e in eta: base[s]*=phi[s][e]
    wa=[base[s]*phi[s][ta] for s in range(M)]; wb=[base[s]*phi[s][tb] for s in range(M)]
    Za,Zb=sum(wa),sum(wb); return F(sum(abs(wa[s]*Zb-wb[s]*Za) for s in range(M)),2*Za*Zb)
# Lipschitz lemma: on a line with weights in {t,1}, w_s = t^{k_s}, 0<=k_s<=6; t a_s' = a_s (k_s - kbar); sum_s |a_s'| <= 6/t;
# TV of a fixed shell/pair, and c_1 = max of finitely many, are Lipschitz with constant 6/u on [u,v].
def certify_region(line,u,v,depth=0):
    """certify 6c_1(t) < 1 for all t in [u,v] by bisection with exact endpoint values; returns #intervals or -1."""
    cu=c1_multiset(line_tr(line,u))[0]; cv=c1_multiset(line_tr(line,v))[0]
    if 6*cu>=1 or 6*cv>=1: return -1
    if max(6*cu,6*cv)-1+6*F(6)/u*(v-u)<0: return 1
    if depth>90: return -1
    m=(u+v)/2; a=certify_region(line,u,m,depth+1)
    if a<0: return -1
    b=certify_region(line,m,v,depth+1)
    return -1 if b<0 else a+b
def certify_region_iter(line,u,v):
    """same, iterative, evaluating c_1 once per endpoint (cache)."""
    cache={}
    def c(t):
        if t not in cache: cache[t]=6*c1_multiset(line_tr(line,t))[0]-1
        return cache[t]
    stack=[(u,v)]; n=0
    while stack:
        a,b=stack.pop()
        ca,cb=c(a),c(b)
        if ca>=0 or cb>=0: return -1,len(cache)
        if max(ca,cb)+36*(b-a)/a<0: n+=1; continue
        if b-a<F(1,10**40): return -1,len(cache)
        m=(a+b)/2; stack.append((a,m)); stack.append((m,b))
    return n,len(cache)
t=sp.symbols('t')
def sixtv_num(line,eta,ta,tb,S):
    def k(s,tt): return sum(1 for e in list(eta)+[tt] if line[orb(s,e)]=='t')
    Za=sum(t**k(s,ta) for s in range(M)); Zb=sum(t**k(s,tb) for s in range(M))
    num=6*sum((t**k(s,ta))*Zb-(t**k(s,tb))*Za for s in range(M) if S[s])-Za*Zb
    P=sp.Poly(sp.expand(num),t); D=sp.Poly(sp.expand(Za*Zb),t); g=sp.gcd(P,D); return sp.Poly(sp.quo(P,g),t)
def competitor_sweep(line,a,b,displayed):
    """each (shell,pair): certified below on [a,b] by the Lipschitz bound, or identical rational function to `displayed`."""
    tra,trb=line_tr(line,a),line_tr(line,b); L=F(6)/a; cert=same=0; bad=[]
    for eta in SHELLS:
        for ta,tb in PAIRS:
            va=6*tv_pattern(tra,eta,ta,tb)-1; vb=6*tv_pattern(trb,eta,ta,tb)-1
            if max(va,vb)+6*L*(b-a)<0: cert+=1; continue
            phi=phi_of(tra); base=[1]*M
            for s in range(M):
                for e in eta: base[s]*=phi[s][e]
            wa=[base[s]*phi[s][ta] for s in range(M)]; wb=[base[s]*phi[s][tb] for s in range(M)]; Za,Zb=sum(wa),sum(wb)
            S=[wa[s]*Zb-wb[s]*Za>=0 for s in range(M)]
            P=sixtv_num(line,eta,ta,tb,S)
            if P.monic()==displayed.monic(): same+=1
            else: bad.append((eta,ta,tb,P.as_expr()))
    return cert,same,bad
LINES={'(t,1,1)':('t','1','1'),'(t,t,1)':('t','t','1'),'(1,1,t)':('1','1','t')}
POLYS={('(t,1,1)',1):sp.Poly(t**7-2*t**5+5*t**4-8*t**3-t**2-4,t),('(t,1,1)',2):sp.Poly(t**2+10*t-5,t),
       ('(t,t,1)',1):sp.Poly(4*t**7-8*t**5+5*t**4-8*t**3-t**2-1,t),('(t,t,1)',2):sp.Poly(t**5+7*t-5,t),
       ('(1,1,t)',1):sp.Poly(t**7+t**5+8*t**4-5*t**3+8*t**2-4,t),('(1,1,t)',2):sp.Poly(5*t**5-7*t**4-1,t)}
T0=time.time(); print("c1 multiset (3,1,2) =",c1_multiset((3,1,2))[0],"in %.3fs"%(time.time()-T0))
for name,line in LINES.items():
    ivs={}
    for j in (1,2):
        P=POLYS[(name,j)]; iv=[i for i in P.intervals(eps=sp.Rational(1,10**20)) if i[0][0]>0][0][0]
        ivs[j]=(F(int(iv[0].p),int(iv[0].q)),F(int(iv[1].p),int(iv[1].q)))
        T0=time.time(); cert,same,bad=competitor_sweep(line,ivs[j][0],ivs[j][1],P)
        print(f"{name} threshold {j} isolating [{float(ivs[j][0]):.15f},{float(ivs[j][1]):.15f}]: certified {cert} identical {same} distinct-uncertified {len(bad)} [{time.time()-T0:.1f}s]")
    lo=min(ivs[1],ivs[2]); hi=max(ivs[1],ivs[2]); u=lo[1]; v=hi[0]
    T0=time.time(); n,ev=certify_region_iter(line,u,v)
    print(f"{name} region certificate on [{float(u):.12f},{float(v):.12f}]: intervals {n}, c_1 evaluations {ev} [{time.time()-T0:.1f}s]")
# reciprocity checks
print("reciprocity (t,t,1)<->(1,1,t):", sp.expand(t**7*POLYS[('(t,t,1)',1)].as_expr().subs(t,1/t)) == -POLYS[('(1,1,t)',1)].as_expr(), sp.expand(t**5*POLYS[('(t,t,1)',2)].as_expr().subs(t,1/t)) == -POLYS[('(1,1,t)',2)].as_expr())
print("scale invariance c1(5/4,5/4,1) == c1(1,1,4/5):", c1_multiset(line_tr(('t','t','1'),F(5,4)))[0]==c1_multiset(line_tr(('1','1','t'),F(4,5)))[0])
print("(7,3,5):",c1_multiset((7,3,5))[:1],"(2,5,3) c1:",c1_multiset((2,5,3))[0])
