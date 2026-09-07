"""Supervisor control, block 05 (Pickard structure of the monotone-order formation law). Exact Fractions."""
from fractions import Fraction as F
from itertools import product, permutations
import time, sys
MENU=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def orb(a,b):
    d=sum(u*v for u,v in zip(MENU[a],MENU[b])); return 0 if d==1 else (1 if d==-1 else 2)
TR=(3,1,2); phi=[[TR[orb(a,b)] for b in range(M)] for a in range(M)]; Z1=sum(phi[0])
K=[[F(phi[a][b],Z1) for b in range(M)] for a in range(M)]
K2=[[sum(K[a][s]*K[s][b] for s in range(M)) for b in range(M)] for a in range(M)]
def r_cond(s, recorded):
    w=[1]*M
    for t in range(M):
        for v in recorded: w[t]*=phi[t][v]
    return F(w[s], sum(w))
# 1 bridge identity
ok=all(r_cond(s,[a,b])==K[a][s]*K[s][b]/K2[a][b] for a in range(M) for b in range(M) for s in range(M))
print("1 bridge identity r(s|a,b) = K(a,s)K(s,b)/K^2(a,b):", ok)
# formation law on an n x W rectangle for a given order (list of sites), block 01's definition
def formation_law(n,W,order):
    pos={site:k for k,site in enumerate(order)}
    nbrs={}
    for (i,j) in order:
        rec=[(i2,j2) for (i2,j2) in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)] if 0<=i2<n and 0<=j2<W and pos[(i2,j2)]<pos[(i,j)]]
        nbrs[(i,j)]=rec
    law={}
    for conf in product(range(M),repeat=n*W):
        v={(i,j):conf[i*W+j] for i in range(n) for j in range(W)}
        p=F(1)
        for site in order:
            p*=r_cond(v[site],[v[y] for y in nbrs[site]])
        law[conf]=p
    return law,nbrs
def linear_extensions(n,W):
    sites=[(i,j) for i in range(n) for j in range(W)]
    out=[]
    def rec(chosen,remaining):
        if not remaining: out.append(list(chosen)); return
        for s in remaining:
            i,j=s
            if (j==0 or (i,j-1) in chosen) and (i==0 or (i-1,j) in chosen):
                rec(chosen+[s],[t for t in remaining if t!=s])
    rec([],sites); return out
# 2 monotone-order class on 2x3: all linear extensions give the same law; recorded sets = {left, above}
n,W=2,3; exts=linear_extensions(n,W); print("2 linear extensions of 2x3:",len(exts))
laws=[]; sets_ok=True
for e in exts:
    law,nb=formation_law(n,W,e); laws.append(law)
    for (i,j),rec in nb.items():
        sets_ok = sets_ok and set(rec)=={(i2,j2) for (i2,j2) in [(i,j-1),(i-1,j)] if i2>=0 and j2>=0}
print("  recorded sets = {left, above} for every extension:",sets_ok,"; all laws equal:",all(l==laws[0] for l in laws))
muP=laws[0]
# 3 transpose symmetry on 2x3 vs 3x2 (row sweep)
row_order=lambda n,W:[(i,j) for i in range(n) for j in range(W)]
lawT,_=formation_law(3,2,row_order(3,2))
def transpose_conf(conf,n,W): # conf on n x W -> conf on W x n
    v={(i,j):conf[i*W+j] for i in range(n) for j in range(W)}
    return tuple(v[(i,j)] for j in range(W) for i in range(n))
print("3 transpose symmetry mu_row(2x3)(v) == mu_row(3x2)(v^T):", all(muP[c]==lawT[transpose_conf(c,2,3)] for c in muP))
# 4 columns are K-chains on 2x3 (column j: (v0j,v1j) ~ (1/6)K) and rows (3-site chain)
def marginal(law,n,W,sites):
    out={}
    for conf,p in law.items():
        key=tuple(conf[i*W+j] for (i,j) in sites); out[key]=out.get(key,0)+p
    return out
colok=all(marginal(muP,2,3,[(0,j),(1,j)])[(a,b)]==F(1,6)*K[a][b] for j in range(3) for a in range(M) for b in range(M))
print("4 columns of 2x3 are (1/6)K pairs:",colok)
# 5 the 2x2 marginal formula and corner conditional independence on 2x3 (columns 0,1 and 1,2)
def pick(c,b,a,d): return F(1,6)*K[c][a]*K[c][b]*K[a][d]*K[d][b]/K2[a][b]
ok5=True
for j in (1,2):
    m=marginal(muP,2,3,[(0,j-1),(0,j),(1,j-1),(1,j)])
    ok5=ok5 and all(m[(c,b,a,d)]==pick(c,b,a,d) for c in range(M) for b in range(M) for a in range(M) for d in range(M))
print("5 2x2 marginals = (1/6)K(c,a)K(c,b)K(a,d)K(d,b)/K^2(a,b) at both column pairs:",ok5)
# 6 three rows, W=3 via row transfer: column chain and staircase chain
def p0_row(rho):
    p=F(1,6)
    for j in range(1,len(rho)): p*=K[rho[j-1]][rho[j]]
    return p
def P_row(beta,alpha):
    p=K[beta[0]][alpha[0]]
    for j in range(1,len(alpha)): p*=K[alpha[j-1]][alpha[j]]*K[alpha[j]][beta[j]]/K2[alpha[j-1]][beta[j]]
    return p
rows=list(product(range(M),repeat=3)); t0=time.time()
P={(b,a):P_row(b,a) for b in rows for a in rows}; p0={r:p0_row(r) for r in rows}
# three-row joint restricted to selected sites: accumulate
def three_row_marginal(sites):  # sites: list of (i,j), i in 0..2
    out={}
    for r0 in rows:
        w0=p0[r0]
        for r1 in rows:
            w1=w0*P[(r0,r1)]
            if w1==0: continue
            for r2 in rows:
                w=w1*P[(r1,r2)]
                key=tuple((r0,r1,r2)[i][j] for (i,j) in sites); out[key]=out.get(key,0)+w
    return out
col=three_row_marginal([(0,1),(1,1),(2,1)])
print("6a column 1 of 3x3 is the K-chain:", all(col[(a,b,c)]==F(1,6)*K[a][b]*K[b][c] for a in range(M) for b in range(M) for c in range(M)), "[%.0fs]"%(time.time()-t0))
st=three_row_marginal([(0,0),(0,1),(1,1),(1,2),(2,2)])
isch=all(st[k]==F(1,6)*K[k[0]][k[1]]*K[k[1]][k[2]]*K[k[2]][k[3]]*K[k[3]][k[4]] for k in st)
print("6b staircase (0,0)(0,1)(1,1)(1,2)(2,2) of 3x3 is a K-chain:", isch)
st2=three_row_marginal([(0,0),(1,0),(1,1),(2,1),(2,2)])
print("6c staircase (0,0)(1,0)(1,1)(2,1)(2,2) is a K-chain:", all(st2[k]==F(1,6)*K[k[0]][k[1]]*K[k[1]][k[2]]*K[k[2]][k[3]]*K[k[3]][k[4]] for k in st2))
# 7 snake order on 2x3: columns differ from (1/6)K
snake=[(0,0),(0,1),(0,2),(1,2),(1,1),(1,0)]
lawS,nbS=formation_law(2,3,snake)
print("7 snake 2x3 recorded sets:",nbS)
diffs=[j for j in range(3) if any(marginal(lawS,2,3,[(0,j),(1,j)])[(a,b)]!=F(1,6)*K[a][b] for a in range(M) for b in range(M))]
print("  snake columns differing from (1/6)K:",diffs, "; rows of snake are p0:", marginal(lawS,2,3,[(1,0),(1,1),(1,2)])=={k:p0_row(k) for k in product(range(M),repeat=3)})
# 8 the mirrored class (rows right-to-left): law differs from muP on 2x3
mirror=[(0,2),(0,1),(0,0),(1,2),(1,1),(1,0)]
lawM,_=formation_law(2,3,mirror)
print("8 mirrored monotone class law == muP:", lawM==muP, "; its column pairs (1/6)K:", all(marginal(lawM,2,3,[(0,j),(1,j)])[(a,b)]==F(1,6)*K[a][b] for j in range(3) for a in range(M) for b in range(M)))
