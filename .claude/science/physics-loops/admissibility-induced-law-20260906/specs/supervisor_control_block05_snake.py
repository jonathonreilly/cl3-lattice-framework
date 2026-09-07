import sys; sys.argv=['x']
src=open('supervisor_control_block05_pickard.py').read().split("# 1 bridge identity")[0]
exec(src)
from itertools import product
import time
# linear extension counts (standard Young tableaux of the rectangle)
def count_ext(n,W):
    sites=[(i,j) for i in range(n) for j in range(W)]
    from functools import lru_cache
    @lru_cache(None)
    def rec(chosen):
        if len(chosen)==len(sites): return 1
        tot=0
        for s in sites:
            if s in chosen: continue
            i,j=s
            if (j==0 or (i,j-1) in chosen) and (i==0 or (i-1,j) in chosen): tot+=rec(chosen|{s})
        return tot
    return rec(frozenset())
print("linear extensions: 2x3", count_ext(2,3), "3x3", count_ext(3,3), "3x4", count_ext(3,4), "4x4", count_ext(4,4))
# snake on 3 rows, W=3: rows 0 and 2 left-to-right, row 1 right-to-left; column-1 three-chain
def p0_row(rho):
    p=F(1,6)
    for j in range(1,len(rho)): p*=K[rho[j-1]][rho[j]]
    return p
def P_lr(beta,alpha):
    p=K[beta[0]][alpha[0]]
    for j in range(1,len(alpha)): p*=K[alpha[j-1]][alpha[j]]*K[alpha[j]][beta[j]]/K2[alpha[j-1]][beta[j]]
    return p
def P_rl(beta,alpha):  # row formed right to left: site W-1 first with the single recorded neighbour above
    Wd=len(alpha); p=K[beta[Wd-1]][alpha[Wd-1]]
    for j in range(Wd-2,-1,-1): p*=K[alpha[j+1]][alpha[j]]*K[alpha[j]][beta[j]]/K2[alpha[j+1]][beta[j]]
    return p
rows=list(product(range(M),repeat=3)); t0=time.time()
# check: rows sum to one and p0 P_rl = p0
print("P_rl rows sum to 1:", all(sum(P_rl(b,a) for a in rows)==1 for b in rows[:20]), "; p0 P_rl = p0:", all(sum(p0_row(b)*P_rl(b,a) for b in rows)==p0_row(a) for a in rows[:30]))
Plr={(b,a):P_lr(b,a) for b in rows for a in rows}; Prl={(b,a):P_rl(b,a) for b in rows for a in rows}; p0={r:p0_row(r) for r in rows}
def col_marg(Pa,Pb,j):
    out={}
    for r0 in rows:
        for r1 in rows:
            w1=p0[r0]*Pa[(r0,r1)]
            if w1==0: continue
            for r2 in rows:
                key=(r0[j],r1[j],r2[j]); out[key]=out.get(key,0)+w1*Pb[(r1,r2)]
    return out
for j in range(3):
    c=col_marg(Plr,Prl,j)
    chain=all(c[(a,b,d)]==F(1,6)*K[a][b]*K[b][d] for a in range(M) for b in range(M) for d in range(M))
    pairs=all(sum(c[(a,b,d)] for d in range(M))==F(1,6)*K[a][b] for a in range(M) for b in range(M)) and all(sum(c[(a,b,d)] for a in range(M))==F(1,6)*K[b][d] for b in range(M) for d in range(M))
    print(f"snake 3x3 column {j}: three-chain = K-chain: {chain}; both vertical pairs (1/6)K: {pairs}")
print("[%.0fs]"%(time.time()-t0))
# the monotone law's column-1 chain across rows 0..2 was True (control 1, 6a); diagonal pair law (1/6)K^2 check on 2x3
