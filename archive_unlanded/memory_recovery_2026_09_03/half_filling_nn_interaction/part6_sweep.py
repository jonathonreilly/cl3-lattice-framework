#!/usr/bin/env python3
"""Fine g-sweep of the cube minimiser over all 32 sectors (incl. strong
   attraction), 2x2x3 minimiser at larger g, and the -27/g^3 extrapolation."""
import mb, numpy as np, itertools, time
t0=time.time()
L = mb.Lat((2,2,2), False)
sect=[]
for fv in itertools.product([1,-1],repeat=6):
    eta,ok = mb.sector_eta(L,fv)
    if ok: sect.append((fv,eta,sum(1 for x in fv if x==-1)))
IM=[k for k,s in enumerate(sect) if all(x==-1 for x in s[0])][0]
IP=[k for k,s in enumerate(sect) if all(x==1 for x in s[0])][0]

print("=== cube N=4: is all-(-1) the unique minimiser of all 32 sectors? ===")
gs = [-64,-32,-16,-12,-10,-8,-6,-5,-4,-3,-2,-1,-0.5,0,0.5,1,2,3,4,6,8,12,16,32,64,128,256]
flip=[]
for g in gs:
    E=np.array([np.linalg.eigvalsh(mb.build_H(L,e,4,float(g))[0])[0] for (_,e,_) in sect])
    o=np.argsort(E); emin=E[o[0]]
    nmin=int(np.sum(E<emin+1e-11))
    uniq = (nmin==1 and o[0]==IM)
    if not uniq: flip.append(g)
    print(f"  g={g:>8}: Emin={emin:.10f} nmin={nmin} minflux={sorted(set(sect[k][2] for k in np.where(E<emin+1e-11)[0]))} "
          f"unique_all-(-1)={uniq} rank(-)={int(np.where(o==IM)[0][0])} rank(+)={int(np.where(o==IP)[0][0])} "
          f"margin={E[o][nmin]-emin:.3e} dE(-,+)={E[IM]-E[IP]:+.6e}")
print("  g where all-(-1) is NOT the unique minimiser:", flip)
print()

print("=== cube: extrapolation of g^3 * (E0(-) - E0(+)) ===")
import mpmath as mp
mp.mp.dps=60
def gsE(eta,g):
    H,_,_ = mb.build_H(L,eta,4,int(g),dtype=np.int64)
    return min(mp.mp.eigsy(mp.matrix(H.tolist()), eigvals_only=True))
em=sect[IM][1]; ep=sect[IP][1]
G=[64,128,256,512]
S=[ (gsE(em,g)-gsE(ep,g))*g**3 for g in G]
for g,s in zip(G,S): print(f"   g={g:>4}  g^3*dE = {mp.nstr(s,20)}")
# Richardson in 1/g^2
A=mp.matrix([[mp.mpf(1), mp.mpf(1)/g**2, mp.mpf(1)/g**3, mp.mpf(1)/g**4] for g in G])
c=mp.lu_solve(A, mp.matrix(S))
print("   extrapolated c3 =", mp.nstr(c[0],25), "  (corrections", mp.nstr(c[1],8), mp.nstr(c[2],8), ")")
print("   c3 + 27 =", mp.nstr(c[0]+27,10))
print("elapsed %.1fs"%(time.time()-t0))
