#!/usr/bin/env python3
"""Item 5: CDW order in the two uniform sectors, cube and 2x2x3; and the
   large-g ring-exchange scaling of E_0(-) - E_0(+) on the cube."""
import mb, numpy as np, itertools, time
t0=time.time()

def uniform(L, s):
    fv = tuple([s]*len(L.faces()))
    eta, ok = mb.sector_eta(L, fv); assert ok
    return eta

def cdw(L, eta, N, g):
    H, st, ix = mb.build_H(L, eta, N, float(g))
    w, U = np.linalg.eigh(H)
    deg = int(np.sum(w < w[0]+1e-9))
    psi = U[:,0]; p = psi**2
    sub = np.array([ (v[0]+v[1]+v[2]) & 1 for v in L.V ])       # sublattice
    sgn = 1 - 2*sub
    occ = np.array([[ (s>>i)&1 for i in range(L.nv)] for s in st], dtype=float)
    n = p @ occ
    O = (occ - 0.5) @ sgn / L.nv                                # staggered op eigenvalue per basis state
    m2 = float(p @ (O**2))
    # Neel weight
    neelA = sum(1<<i for i in range(L.nv) if sub[i]==0)
    neelB = sum(1<<i for i in range(L.nv) if sub[i]==1)
    wN = (p[ix[neelA]]+p[ix[neelB]]) if (neelA in ix and neelB in ix) else float('nan')
    return dict(E0=w[0], deg=deg, gap=w[1]-w[0], n=n, m2=m2, neelw=wN,
                nmin=n.min(), nmax=n.max())

print("=== CDW order parameter at half filling ===")
for dims, N in (((2,2,2),4), ((2,2,3),6)):
    L = mb.Lat(dims, False)
    for g in (0,4,8,16,32):
        line=[]
        for s in (1,-1):
            r = cdw(L, uniform(L,s), N, g)
            line.append((s,r))
        (sp,rp),(sm,rm)=line
        print(f"{dims} N={N} g={g:>3}: "
              f"n_i in [{rp['nmin']:.6f},{rp['nmax']:.6f}](+) [{rm['nmin']:.6f},{rm['nmax']:.6f}](-)  "
              f"m^2 = {rp['m2']:.8f}(+) {rm['m2']:.8f}(-)  "
              f"Neel weight = {rp['neelw']:.6f}(+) {rm['neelw']:.6f}(-)  "
              f"E0(-)-E0(+) = {rm['E0']-rp['E0']:+.10e}  deg {rp['deg']}/{rm['deg']}  "
              f"lowgap {rp['gap']:.4e}/{rm['gap']:.4e}")
    print()

print("=== large-g scaling of E_0(-) - E_0(+) on the 2x2x2 cube, N=4 ===")
L = mb.Lat((2,2,2), False)
ep, em = uniform(L,1), uniform(L,-1)
import mpmath as mp
mp.mp.dps = 50
def exact_gs(eta, g):
    H, st, ix = mb.build_H(L, eta, 4, int(g), dtype=np.int64)
    A = mp.matrix(H.tolist())
    e, _ = mp.mp.eigsy(A, eigvals_only=True), None
    return min(e)
rows=[]
for g in (8,16,32,64,128):
    a = exact_gs(em,g); b = exact_gs(ep,g)
    d = a-b
    rows.append((g,a,b,d))
    print(f"g={g:>4}  E0(-)={mp.nstr(a,20)}  E0(+)={mp.nstr(b,20)}  dE={mp.nstr(d,15)}  "
          f"dE*g^3={mp.nstr(d*g**3,12)}  dE*g^2={mp.nstr(d*g*g,10)}")
# fit dE = c3/g^3 (+ c4/g^4 + c5/g^5) on the four required points
gs=[8,16,32,64]
ds=[r[3] for r in rows if r[0] in gs]
Amat = mp.matrix([[mp.mpf(1)/g**3, mp.mpf(1)/g**4, mp.mpf(1)/g**5, mp.mpf(1)/g**6] for g in gs])
cvec = mp.lu_solve(Amat, mp.matrix(ds))
print("4-point fit dE = c3/g^3 + c4/g^4 + c5/g^5 + c6/g^6 :")
for k,c in zip((3,4,5,6), cvec):
    print(f"   c{k} = {mp.nstr(c,15)}")
print("   sign(c3) =", "NEGATIVE (staggered lower)" if cvec[0]<0 else "POSITIVE (plain lower)")
# Richardson: c3 estimate from consecutive pairs assuming pure power p
for i in range(len(rows)-1):
    g1,_,_,d1 = rows[i]; g2,_,_,d2 = rows[i+1]
    p = mp.log(d1/d2)/mp.log(mp.mpf(g2)/g1)
    print(f"   local exponent between g={g1} and {g2}: p = {mp.nstr(p,10)}   c_p = {mp.nstr(d1*g1**p,10)}")
print("elapsed %.1fs"%(time.time()-t0))
