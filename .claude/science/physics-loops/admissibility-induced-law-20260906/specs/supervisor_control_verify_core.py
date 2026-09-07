"""Supervisor control computation (exact rationals): the core claims of T1/T2."""
from fractions import Fraction as F
from itertools import product, permutations
import sympy as sp

# six Bloch-axis pure states as unit vectors
MENU = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
M = len(MENU)
def dot(a,b): return sum(x*y for x,y in zip(MENU[a],MENU[b]))
def orbit(a,b):
    d = dot(a,b); return 'par' if d==1 else ('anti' if d==-1 else 'orth')

def phi_factory(p,q,r):
    return lambda a,b: {'par':p,'anti':q,'orth':r}[orbit(a,b)]

def gibbs(graph_edges, n, phi):
    mu = {}
    for v in product(range(M), repeat=n):
        w = F(1)
        for (i,j) in graph_edges: w *= phi(v[i],v[j])
        mu[v] = w
    Z = sum(mu.values())
    return {v: w/Z for v,w in mu.items()}, Z

def nbrs(graph_edges, n):
    N = {i:set() for i in range(n)}
    for i,j in graph_edges: N[i].add(j); N[j].add(i)
    return N

def rule_product(phi, s, recorded_vals):
    return phi, s, recorded_vals

def formation(graph_edges, n, phi, order):
    N = nbrs(graph_edges, n)
    mu = {}
    for v in product(range(M), repeat=n):
        w = F(1); formed = []
        for x in order:
            A = [y for y in N[x] if y in formed]
            num = F(1)
            for y in A: num *= phi(v[x], v[y])
            Zk = sum((lambda s: (lambda t: t)(F(1)))(s) for s in range(M))  # placeholder
            Zk = F(0)
            for s in range(M):
                t = F(1)
                for y in A: t *= phi(s, v[y])
                Zk += t
            w *= num/Zk
            formed.append(x)
        mu[v] = w
    assert sum(mu.values()) == 1
    return mu

def full_conditionals_match(graph_edges, n, phi, mu):
    N = nbrs(graph_edges, n)
    for v in mu:
        for x in range(n):
            tot = sum(mu[v[:x]+(s,)+v[x+1:]] for s in range(M))
            # rule with all nbrs recorded
            Zx = sum(__import__('functools').reduce(lambda acc,y: acc*phi(s,v[y]), N[x], F(1)) for s in range(M))
            rx = __import__('functools').reduce(lambda acc,y: acc*phi(v[x],v[y]), N[x], F(1))/Zx
            if mu[v]/tot != rx: return False
    return True

p,q,r = F(3),F(1),F(2)
phi = phi_factory(p,q,r)
graphs = {'path3': ([(0,1),(1,2)],3), 'star4': ([(0,1),(0,2),(0,3)],4), 'cycle4': ([(0,1),(1,2),(2,3),(3,0)],4)}
for name,(E,n) in graphs.items():
    mu, Z = gibbs(E,n,phi)
    print(f"{name}: static law full conditionals == product rule: {full_conditionals_match(E,n,phi,mu)}  Z={Z}")
    laws = {}
    for order in permutations(range(n)):
        ms = formation(E,n,phi,order)
        eq = (ms == mu)
        key = tuple(sorted(ms.items()))
        laws.setdefault(key, []).append(order)
        if name!='cycle4' or order in [(0,1,2,3),(0,2,1,3),(0,1,3,2)]:
            print(f"   order {order}: equals static? {eq}")
    print(f"   distinct formation laws over all {len(list(permutations(range(n))))} orders: {len(laws)}; any equal to static: {any(tuple(sorted(mu.items()))==k for k in laws)}")

# two-neighbour normaliser spread symbolic
P,Q,R = sp.symbols('p q r', positive=True)
phis = lambda a,b: {'par':P,'anti':Q,'orth':R}[orbit(a,b)]
def Z2(b,c): return sp.expand(sum(phis(s,b)*phis(s,c) for s in range(M)))
vals = {}
for b in range(M):
    for c in range(M):
        vals.setdefault(orbit(b,c), Z2(b,c))
print("Z2 by pair orbit:", vals)
print("Z2(par)-Z2(anti) =", sp.factor(vals['par']-vals['anti']))
print("Z2(par)-Z2(orth) =", sp.factor(vals['par']-vals['orth']))
print("Z2(anti)-Z2(orth) =", sp.factor(vals['anti']-vals['orth']))
Z1 = {orbit(0,b): sp.expand(sum(phis(s,b) for s in range(M))) for b in range(M)}
print("one-neighbour normaliser by b (should be constant):", set(Z1.values()))

# sum rule inconsistency on the 3-path: Brook cycle 1->2->1->2
lam = sp.Rational(1,4)
def rsum(s, recs):  # recs: list of menu indices of recorded nbrs
    w = [1 + lam*sum(dot(t,y) for y in recs) for t in range(M)]
    return w[s]/sum(w)
best = None
for a,a2,b,b2,c in product(range(M), repeat=5):
    if a==a2 or b==b2: continue
    num = rsum(a2,[b])*rsum(b2,[a2,c])*rsum(a,[b2])*rsum(b,[a,c])
    den = rsum(a,[b])*rsum(b,[a2,c])*rsum(a2,[b2])*rsum(b2,[a,c])
    ratio = sp.nsimplify(num/den)
    if ratio != 1:
        best = ((a,a2,b,b2,c), ratio); break
print("sum rule Brook-cycle witness (lambda=1/4):", best)
# product rule: same cycle must be 1
def rprod(s, recs):
    w = [sp.Integer(1)*__import__('functools').reduce(lambda acc,y: acc*phis(t,y), recs, sp.Integer(1)) for t in range(M)]
    return w[s]/sum(w)
bad = 0
for a,a2,b,b2,c in product(range(M), repeat=5):
    if a==a2 or b==b2: continue
    num = rprod(a2,[b])*rprod(b2,[a2,c])*rprod(a,[b2])*rprod(b,[a,c])
    den = rprod(a,[b])*rprod(b,[a2,c])*rprod(a2,[b2])*rprod(b2,[a,c])
    if sp.simplify(num/den - 1) != 0: bad += 1
print("product rule Brook-cycle violations (symbolic p,q,r):", bad)
