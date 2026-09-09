#!/usr/bin/env python3
"""Bloch cross-check of the free part, and larger tori for the
   thermodynamic limit of the first-order crossing."""
import mb, numpy as np, itertools, time
from common import EX, eta_ks
t0=time.time()

def eta_field(L,kind,twist):
    eta={}
    for (v,ax) in L.E:
        e = 1 if kind=='+' else eta_ks(v,ax)
        if v[ax]==L.dims[ax]-1: e*=twist[ax]
        eta[(v,ax)]=e
    return eta

def sea(L,eta):
    M=mb.one_particle(L,eta)
    w,C=np.linalg.eigh(-M)
    Nh=L.nv//2; Cocc=C[:,:Nh]; P=Cocc@Cocc.T
    A=sum(P[i,i]*P[j,j]-P[i,j]**2 for (i,j,_) in mb.bond_list(L))
    return w[:Nh].sum(), w[Nh]-w[Nh-1], A

print("=== Bloch cross-check of the free half-filling energies ===")
for Lz in (4,6,8):
    for kind,delta in (('+',(1,1,1)),):
        q=[2*np.pi*(np.arange(Lz)+0.5)/Lz]
        pass
for Lz in (4,6,8):
    # plain, fully antiperiodic (delta=1) and periodic (delta=0)
    for d in (0,1):
        qs=2*np.pi*(np.arange(Lz)+d/2)/Lz
        c=np.cos(qs)
        E=2*(c[:,None,None]+c[None,:,None]+c[None,None,:]).ravel()
        E.sort(); Eb=E[:Lz**3//2].sum()
        # staggered:  +- sqrt(6 + 2 sum cos q) on the same grid, half the modes each
        s=6+2*(c[:,None,None]+c[None,:,None]+c[None,None,:]).ravel()
        s=np.clip(s,0,None)
        Es=-np.sqrt(s); Es.sort(); Esb=Es[:Lz**3//2].sum()/1.0
        # the staggered band structure doubles the cell: half as many q, both bands
        print(f"  L={Lz} delta={d}: plain Bloch E_half={Eb:.9f}   staggered lower band sum={Esb/2:.9f}")
print()
print("=== larger tori: free part, first-order coefficient, crossing ===")
res={}
for Lz in (4,6,8,10,12):
    row={}
    for kind in ('+','-'):
        best=None
        for tw in itertools.product([1,-1],repeat=3):
            L=mb.Lat((Lz,)*3,True)
            E,gap,A=sea(L,eta_field(L,kind,tw))
            if best is None or E<best[0]-1e-11: best=(E,gap,A,tw)
        row[kind]=best
        V=Lz**3
        print(f"  L={Lz:>2} {kind}: twist {best[3]} Efree/V={best[0]/V:+.9f} gap={best[1]:.6f} A/V={best[2]/V:.9f}")
    V=Lz**3
    dE=(row['-'][0]-row['+'][0])/V; dA=(row['-'][2]-row['+'][2])/V
    res[Lz]=(dE,dA,-dE/dA)
    print(f"    dEfree/V={dE:+.9f}  dA/V={dA:+.9f}  g_c = {-dE/dA:+.9f}    t=%.0fs"%(time.time()-t0))
print()
Ls=sorted(res); 
print("Richardson-ish limits (linear in 1/L^2 on the last three):")
import numpy as np
for k,name in ((0,'dEfree/V'),(1,'dA/V'),(2,'g_c')):
    y=np.array([res[l][k] for l in Ls[-3:]]); xx=np.array([1.0/l**2 for l in Ls[-3:]])
    p=np.polyfit(xx,y,2) if len(xx)>2 else None
    print(f"  {name}: values {[round(res[l][k],7) for l in Ls]}  -> extrap {np.polyval(p,0.0):.7f}")
print("elapsed %.1fs"%(time.time()-t0))
