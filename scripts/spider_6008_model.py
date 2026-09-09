"""Supplied finite spin model; occupation/Hankel definitions from Cycle937.
The finite symmetric construction is not a physical dynamics supplier.
"""
import itertools
import math
from functools import lru_cache
import numpy as np


def occupations(d, D):
    if D == 1:
        return [(d,)]
    return [(k,) + tail for k in range(d + 1)
            for tail in occupations(d-k, D-1)]


def multinomial(n):
    return math.factorial(sum(n)) // math.prod(math.factorial(x) for x in n)


def arm_operators(L, edges, field):
    D = 2**L
    z = np.array([[1-2*((a >> p) & 1) for p in range(L)] for a in range(D)])
    h = np.diag([-sum(z[a,u]*z[a,v] for u,v in edges) for a in range(D)]).astype(float)
    for a in range(D):
        for p in range(L):
            h[a,a^(1<<p)] -= field
    return z[:,0], h


def gamma(operator, basis):
    pos = {n:i for i,n in enumerate(basis)}
    H = np.zeros((len(basis),len(basis)))
    for j,n in enumerate(basis):
        for b,nb in enumerate(n):
            if not nb:
                continue
            for a in range(len(n)):
                if a == b:
                    H[j,j] += nb*operator[b,b]
                elif operator[a,b]:
                    m=list(n);m[b]-=1;m[a]+=1
                    H[pos[tuple(m)],j] += operator[a,b]*math.sqrt(nb*m[a])
    return H


def reduced(d, L, edges, arm_field, pointer_field):
    if d < 1 or L < 1 or 2*math.comb(d+2**L-1,d)>600:
        raise ValueError('bounded runner dimension outside declared cap')
    basis=occupations(d,2**L)
    r,h=arm_operators(L,edges,arm_field)
    G=gamma(h,basis);R=gamma(np.diag(r),basis);N=len(basis)
    H=np.block([[G-R,-pointer_field*np.eye(N)],[-pointer_field*np.eye(N),G+R]])
    v=np.zeros(2**L);v[:2]=1/math.sqrt(2)
    c=np.array([math.sqrt(multinomial(n))*math.prod(v[a]**n[a] for a in range(len(n))) for n in basis])
    return H,np.concatenate([c,c])/math.sqrt(2),basis


def evolve(H, initial, t):
    w,V=np.linalg.eigh(H)
    return V@(np.exp(-1j*w*t)*(V.conj().T@initial))


def entropy(matrix):
    values=np.linalg.svd(matrix,compute_uv=False)**2
    total=float(values.sum())
    if total <= 0:
        raise ValueError('zero probability branch has no normalized entropy')
    values=values/total
    return float(-sum(x*math.log2(x) for x in values if x>0))


def hankel(c, basis, d, D, k):
    f={n:c[j]/math.sqrt(multinomial(n)) for j,n in enumerate(basis)}
    left=occupations(k,D);right=occupations(d-k,D)
    return np.array([[math.sqrt(multinomial(p)*multinomial(q))*f[tuple(a+b for a,b in zip(p,q))] for q in right] for p in left])


def profile(c, basis, d, L):
    N=len(basis);out=np.zeros(d+1);probabilities=[]
    for branch in [c[:N],c[N:]]:
        p=float(np.vdot(branch,branch).real);probabilities.append(p)
        if p==0:
            continue
        for k in range(d+1):
            out[k]+=p*entropy(hankel(branch,basis,d,2**L,k))
    return (out/sum(probabilities)).tolist()


def accepted(checks, refutations):
    """One actual terminal rule for every required scientific outcome."""
    return bool(checks) and all(value is True for value in checks.values()) and not refutations


def fit_power_with_log(lams, deltas, pmin=2, pmax=12):
    """Declared protocol.  Model  delta = c * lambda^p * (ln(1/lambda) + b),
    p an INTEGER, b >= 0 a shape parameter.  For each p the best b minimises the
    spread of  ln|delta| - p ln(lambda) - ln(ln(1/lambda)+b)  over the fitted
    points; the winning p is the one with the smallest spread.  RIVALS
    (pure power, p half-integer) are scored on the same footing."""
    xs = [(l, abs(dv)) for l, dv in zip(lams, deltas) if dv is not None and abs(dv) > 0]
    if len(xs) < 3:
        return None
    scores = {}
    for p in range(pmin, pmax + 1):
        best = None
        for b in [0.0 + 0.02 * i for i in range(151)]:
            r = [math.log(v) - p * math.log(l) - math.log(math.log(1.0 / l) + b)
                 for l, v in xs]
            spread = max(r) - min(r)
            if best is None or spread < best[0]:
                best = (spread, b, sum(r) / len(r))
        scores["p=%d_log" % p] = {"spread": best[0], "b": best[1],
                                  "ln_c": best[2]}
    for p in range(pmin, pmax + 1):
        r = [math.log(v) - p * math.log(l) for l, v in xs]
        scores["p=%d_pure" % p] = {"spread": max(r) - min(r), "b": None,
                                   "ln_c": sum(r) / len(r)}
    for ph in [x * 0.5 for x in range(2 * pmin, 2 * pmax + 1)]:
        if abs(ph - round(ph)) < 1e-9:
            continue
        r = [math.log(v) - ph * math.log(l) for l, v in xs]
        scores["p=%.1f_pure" % ph] = {"spread": max(r) - min(r), "b": None,
                                      "ln_c": sum(r) / len(r)}
    win = min(scores, key=lambda k: scores[k]["spread"])
    # a free-exponent least-squares slope, for reference only
    n = len(xs)
    sx = sum(math.log(l) for l, _ in xs)
    sy = sum(math.log(v) for _, v in xs)
    sxx = sum(math.log(l) ** 2 for l, _ in xs)
    sxy = sum(math.log(l) * math.log(v) for l, v in xs)
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    local = []
    for i in range(1, len(xs)):
        (l0, v0), (l1, v1) = xs[i - 1], xs[i]
        local.append({"between": [l0, l1],
                      "local_loglog_slope": math.log(v0 / v1) / math.log(l0 / l1)})
    return {"n_points": n, "lambdas": [l for l, _ in xs],
            "free_loglog_slope": slope, "local_loglog_slopes": local,
            "winner": win, "scores": scores,
            "winning_spread": scores[win]["spread"],
            "at_least_five_supplied_points": bool(n >= 5)}
