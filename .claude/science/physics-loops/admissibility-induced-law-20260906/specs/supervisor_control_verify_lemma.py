"""Supervisor check of the single-site variation lemma (general proof of the (=>) direction)
and of the marginal-reading window dependence. Exact rationals + sympy."""
from fractions import Fraction as F
from itertools import product, permutations
import sympy as sp
MENU = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]; M=6
def dot(a,b): return sum(x*y for x,y in zip(MENU[a],MENU[b]))
def orb(a,b): d=dot(a,b); return 'par' if d==1 else ('anti' if d==-1 else 'orth')
P,Q,R = sp.symbols('p q r', positive=True)
def phis(a,b): return {'par':P,'anti':Q,'orth':R}[orb(a,b)]
# f_j(orbit) = sum_s phi(s,v) phi(s,Ref)^j  with Ref = menu 0
Ref = 0
for j in (1,2,3):
    vals = {}
    for v in range(M):
        vals.setdefault(orb(v,Ref), sp.expand(sum(phis(s,v)*phis(s,Ref)**j for s in range(M))))
    d1 = sp.factor(vals['par']-vals['anti']); d2 = sp.factor(vals['anti']-vals['orth'])
    pred1 = sp.factor((P-Q)*(P**j-Q**j)); pred2 = sp.factor((P-R)*(Q**j-R**j)+(Q-R)*(P**j-R**j))
    print(f"j={j}: par-anti = {d1}  [pred {pred1}] ok={sp.simplify(d1-pred1)==0};  anti-orth = {d2}  [pred {pred2}] ok={sp.simplify(d2-pred2)==0}")
    with_pq = sp.factor((vals['anti']-vals['orth']).subs(Q,P)); print(f"       with p=q: anti-orth = {with_pq}")

# exact classification check on cube8 with the single-site-variation restriction
def nbrs(E,n):
    N={i:set() for i in range(n)}
    for i,j in E: N[i].add(j); N[j].add(i)
    return N
CUBE=[(a,b) for a in range(8) for b in range(a+1,8) if bin(a^b).count('1')==1]
N=nbrs(CUBE,8)
p,q,r = F(3),F(1),F(2)
def phi(a,b): return {'par':p,'anti':q,'orth':r}[orb(a,b)]
def Zk(A, v):  # local normaliser at a site given recorded nbr values
    return sum(__import__('functools').reduce(lambda acc,y: acc*phi(s,v[y]), A, F(1)) for s in range(M))
def Pprod(order, v):
    formed=[]; tot=F(1)
    for x in order:
        A=[y for y in N[x] if y in formed]; tot*=Zk(A,v); formed.append(x)
    return tot
import random
random.seed(1)
orders=[tuple(range(8)), tuple(range(7,-1,-1)), (0,3,5,6,1,2,4,7), (0,7,1,6,2,5,3,4)] + [tuple(random.sample(range(8),8)) for _ in range(4)]
for order in orders:
    # find first site with >=2 recorded nbrs, pick y in A_m
    formed=[]; m=None
    for x in order:
        A=[y for y in N[x] if y in formed]
        if len(A)>=2 and m is None: m=x; y=A[0]
        formed.append(x)
    vals=set()
    for vy in range(M):
        v=[Ref]*8; v[y]=vy; vals.add(Pprod(order, v))
    print(f"order {order}: first >=2-recorded site {m}, vary y={y}: distinct P values across 6 menu values = {len(vals)} (non-constant: {len(vals)>1})")

# marginal-reading window dependence: static law's conditional of x given ONE recorded neighbour y
def static_cond_one_nbr(E,n,x,y):
    Nn=nbrs(E,n); out={}
    for vy in range(M):
        w=[F(0)]*M
        for v in product(range(M), repeat=n):
            if v[y]!=vy: continue
            wt=F(1)
            for (i,j) in E: wt*=phi(v[i],v[j])
            w[v[x]]+=wt
        tot=sum(w); out[vy]=tuple(c/tot for c in w)
    return out
rule_one = {vy: tuple(phi(s,vy)/sum(phi(t,vy) for t in range(M)) for s in range(M)) for vy in range(M)}
path3=[(0,1),(1,2)]; cyc4=[(0,1),(1,2),(2,3),(3,0)]
c_path = static_cond_one_nbr(path3,3,0,1); c_cyc = static_cond_one_nbr(cyc4,4,0,1)
print("path3: static conditional of site0 given site1 equals the rule's one-neighbour conditional:", c_path==rule_one)
print("cycle4: static conditional of site0 given site1 equals the rule's one-neighbour conditional:", c_cyc==rule_one)
print("  cycle4 vs path3 conditionals equal:", c_cyc==c_path, " example vy=0:", c_cyc[0], "vs rule", rule_one[0])
