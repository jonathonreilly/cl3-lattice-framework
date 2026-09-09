#!/usr/bin/env python3
"""Exact ordering of the two uniform-sector ground energies on the cube:
   CRootOf comparison of the exact minimal polynomials (no floating point)."""
import mb, numpy as np, sympy as sp, time
t0=time.time(); x=sp.Symbol('x')
L=mb.Lat((2,2,2),False)
def uni(s):
    e,ok=mb.sector_eta(L,tuple([s]*6)); assert ok; return e
E={}
for s in (1,-1):
    eta=uni(s)
    for g in (-8,-4,-2,-1,0,1,2,4,8,16,32,64):
        H,_,_=mb.build_H(L,eta,4,g,dtype=np.int64)
        p=sp.Matrix(H.tolist()).charpoly(x).as_expr()
        r=sp.real_roots(sp.Poly(p,x))
        E[(s,g)]=min(r)
print(" g   E0(+) exact-min-poly deg   E0(-) deg   sign(E0(-)-E0(+))  [exact CRootOf]")
for g in (-8,-4,-2,-1,0,1,2,4,8,16,32,64):
    a=E[(-1,g)]; b=E[(1,g)]
    da = sp.minimal_polynomial(a,x); db = sp.minimal_polynomial(b,x)
    lt = bool(a < b); eq = bool(sp.Eq(a,b))
    print(f"{g:>4}  deg(+)={sp.Poly(db,x).degree()}  deg(-)={sp.Poly(da,x).degree()}   "
          f"E0(-)<E0(+): {lt}   equal: {eq}   dE={float(a-b):+.9e}")
print("elapsed %.1fs"%(time.time()-t0))
