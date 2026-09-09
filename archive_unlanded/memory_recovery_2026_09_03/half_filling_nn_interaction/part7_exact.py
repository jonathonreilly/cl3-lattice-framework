#!/usr/bin/env python3
"""Exact (sympy) ground energies on the 2x2x2 cube, N=4, integer g,
   for the two uniform sectors: minimal polynomial of E_0 over Z."""
import mb, numpy as np, sympy as sp, time
t0=time.time()
L = mb.Lat((2,2,2), False)
def uni(s):
    eta,ok = mb.sector_eta(L, tuple([s]*6)); assert ok; return eta
x = sp.Symbol('x')
for s,lab in ((1,'plain  all-(+1)'),(-1,'stagg. all-(-1)')):
    eta=uni(s)
    for g in (0,1,2,4,8):
        H,_,_ = mb.build_H(L,eta,4,g,dtype=np.int64)
        M = sp.Matrix(H.tolist())
        pol = M.charpoly(x)
        _, facs = sp.factor_list(pol.as_expr(), x)
        e0 = float(np.linalg.eigvalsh(H.astype(float))[0])
        owner=None; odeg=999
        for f,m in facs:
            fe = f.as_expr() if isinstance(f, sp.Poly) else f
            d = sp.Poly(fe,x).degree()
            rts = sp.Poly(fe,x).nroots(n=30)
            if any(abs(complex(z).real-e0)<1e-9 and abs(complex(z).imag)<1e-9 for z in rts):
                if d<odeg: owner, odeg = fe, d
        degs=[(sp.Poly(f.as_expr() if isinstance(f,sp.Poly) else f,x).degree(), m) for f,m in facs]
        sol=None
        if odeg<=2:
            for r in sp.roots(sp.Poly(owner,x)):
                if abs(complex(r)-e0)<1e-9: sol=sp.radsimp(sp.simplify(r))
        print(f"{lab} g={g}: E0={e0:.12f}  charpoly irreducible-factor (degree,mult): {sorted(degs)}")
        print(f"     min poly of E0 (degree {odeg}): {sp.expand(owner)}")
        if sol is not None: print(f"     E0 = {sol}")
    print()
print("elapsed %.1fs"%(time.time()-t0))
