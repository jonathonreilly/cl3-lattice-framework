#!/usr/bin/env python3
"""Item 1 + 4: open 2x2x2 cube, all 32 consistent sectors, N=4,2,6."""
import mb, numpy as np, itertools, json, time
from fractions import Fraction

t0=time.time()
L = mb.Lat((2,2,2), False)
F = L.faces()
sectors=[]
for fv in itertools.product([1,-1], repeat=len(F)):
    eta, ok = mb.sector_eta(L, fv)
    if ok:
        h = mb.face_holonomy_list(L, eta)
        assert list(h)==list(fv), (fv,h)
        sectors.append((fv, eta, sum(1 for x in fv if x==-1)))
print("consistent sectors:", len(sectors))
print("flux-count histogram:", {k: sum(1 for s in sectors if s[2]==k) for k in range(7)})

GS = [-2, -1, Fraction(-1,2), 0, Fraction(1,2), 1, 2, 4, 8]
res={}
for N in (4, 2, 6):
    glist = GS if N==4 else [0,1,4]
    for g in glist:
        gg = float(g)
        rows=[]
        for (fv, eta, nf) in sectors:
            H,_,_ = mb.build_H(L, eta, N, gg)
            ev = np.linalg.eigvalsh(H)
            rows.append((ev[0], ev[1], nf, fv))
        emin = min(r[0] for r in rows)
        tol = 1e-10
        mins = [r for r in rows if r[0] < emin + tol]
        allm = [r for r in rows if r[0] >= emin + tol]
        nxt = min(r[0] for r in allm) if allm else None
        i_minus = [r for r in rows if r[3]==(-1,)*6][0]
        i_plus  = [r for r in rows if r[3]==(1,)*6][0]
        res[(N,str(g))] = dict(
            emin=emin, n_min=len(mins), min_fluxcounts=sorted(set(r[2] for r in mins)),
            margin=(nxt-emin) if nxt is not None else None,
            E_minus=i_minus[0], E_plus=i_plus[0],
            minus_is_unique=(len(mins)==1 and mins[0][3]==(-1,)*6),
            minus_rank=sorted(r[0] for r in rows).index(i_minus[0]),
            gap_minus=i_minus[1]-i_minus[0], gap_plus=i_plus[1]-i_plus[0],
            spread=max(r[0] for r in rows)-emin)
        r=res[(N,str(g))]
        print(f"N={N} g={g!s:>4} Emin={emin:.10f} nmin={r['n_min']} fluxcnt(min)={r['min_fluxcounts']} "
              f"margin={r['margin'] if r['margin'] is None else round(r['margin'],8)} "
              f"E(-)={r['E_minus']:.10f} E(+)={r['E_plus']:.10f} dE={r['E_minus']-r['E_plus']:+.10f} "
              f"unique(-)={r['minus_is_unique']} rank(-)={r['minus_rank']} mbgap(-)={r['gap_minus']:.3e}")
print("elapsed %.1fs"%(time.time()-t0))
