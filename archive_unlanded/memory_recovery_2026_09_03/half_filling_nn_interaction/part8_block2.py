#!/usr/bin/env python3
"""2x2x3 at larger |g|: minimiser over all 512 sectors, plus the 1/g^3 fit
   and the degeneracy-averaged density in the 2-fold plain ground space."""
import mb, numpy as np, itertools, time
t0=time.time()
L = mb.Lat((2,2,3), False); F=L.faces(); NF=len(F); bl=mb.bond_list(L); N=6
st,ix = mb.basis(L.nv,N); D=len(st)
rows=[];cols=[];bidx=[];sgn=[];diagcnt=np.zeros(D)
for k,s in enumerate(st):
    d=0
    for bi,(i,j,key) in enumerate(bl):
        if ((s>>i)&1) and ((s>>j)&1): d+=1
        for (a,b) in ((i,j),(j,i)):
            r=mb.hop_apply(s,a,b)
            if r is None: continue
            ns,sg=r; rows.append(ix[ns]);cols.append(k);bidx.append(bi);sgn.append(sg)
    diagcnt[k]=d
rows=np.array(rows);cols=np.array(cols);bidx=np.array(bidx);sgn=np.array(sgn,float)
def HM(v,g):
    H=np.zeros((D,D)); np.add.at(H,(rows,cols),-v[bidx]*sgn)
    H[np.arange(D),np.arange(D)]+=g*diagcnt; return H
sects=[]
for fv in itertools.product([1,-1],repeat=NF):
    eta,ok=mb.sector_eta(L,fv)
    if ok: sects.append((fv,np.array([eta[key] for (_,_,key) in bl],float),sum(1 for x in fv if x==-1)))
IM=[k for k,s in enumerate(sects) if all(x==-1 for x in s[0])][0]
IP=[k for k,s in enumerate(sects) if all(x==1 for x in s[0])][0]
print("=== 2x2x3 N=6: minimiser over all 512 consistent sectors ===")
for g in (-4.0,-2.0,-1.0,8.0,16.0):
    E=np.array([np.linalg.eigvalsh(HM(v,g))[0] for (_,v,_) in sects])
    o=np.argsort(E); emin=E[o[0]]; nmin=int(np.sum(E<emin+1e-10))
    print(f"  g={g:>6}: Emin={emin:.9f} nmin={nmin} minflux={sorted(set(sects[k][2] for k in np.where(E<emin+1e-10)[0]))} "
          f"unique_all-(-1)={nmin==1 and o[0]==IM} rank(-)={int(np.where(o==IM)[0][0])} rank(+)={int(np.where(o==IP)[0][0])} "
          f"margin={E[o][nmin]-emin:.4e} dE={E[IM]-E[IP]:+.6e}   t=%.0fs"%(time.time()-t0))
print()
print("=== 2x2x3: 1/g^3 tail of E0(-)-E0(+) ===")
vm=sects[IM][1]; vp=sects[IP][1]
for g in (16.,32.,64.,128.,256.):
    d=np.linalg.eigvalsh(HM(vm,g))[0]-np.linalg.eigvalsh(HM(vp,g))[0]
    print(f"   g={g:>6.0f}  dE={d:+.6e}  g^3*dE={d*g**3:.6f}")
print()
print("=== 2x2x3 plain sector: ground space is 2-fold; degeneracy-averaged density ===")
sub=np.array([(v[0]+v[1]+v[2])&1 for v in L.V]); sg2=1-2*sub
occ=np.array([[(s>>i)&1 for i in range(L.nv)] for s in st],float)
for g in (0.,4.,8.):
    for lab,v in (('+',vp),('-',vm)):
        w,U=np.linalg.eigh(HM(v,g)); deg=int(np.sum(w<w[0]+1e-9))
        P=U[:,:deg]@U[:,:deg].T/deg
        n=np.einsum('kk,kj->j',P,occ) if False else (np.diag(P)@occ)
        O=(occ-0.5)@sg2/L.nv
        m2=float(np.diag(P)@(O**2))
        print(f"   g={g:>4} sector {lab} deg={deg}: n_i in [{n.min():.8f},{n.max():.8f}]  m^2={m2:.8f}")
print("elapsed %.1fs"%(time.time()-t0))
