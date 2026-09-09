#!/usr/bin/env python3
"""Fine attractive bracket on 2x2x3 (all 512) and uniform-pair sweep."""
import mb, numpy as np, itertools, time
t0=time.time()
L=mb.Lat((2,2,3),False); F=L.faces(); bl=mb.bond_list(L); N=6
st,ix=mb.basis(L.nv,N); D=len(st)
rows=[];cols=[];bidx=[];sgn=[];dc=np.zeros(D)
for k,s in enumerate(st):
    d=0
    for bi,(i,j,key) in enumerate(bl):
        if ((s>>i)&1) and ((s>>j)&1): d+=1
        for (a,b) in ((i,j),(j,i)):
            r=mb.hop_apply(s,a,b)
            if r is None: continue
            ns,sg=r; rows.append(ix[ns]);cols.append(k);bidx.append(bi);sgn.append(sg)
    dc[k]=d
rows=np.array(rows);cols=np.array(cols);bidx=np.array(bidx);sgn=np.array(sgn,float)
def HM(v,g):
    H=np.zeros((D,D)); np.add.at(H,(rows,cols),-v[bidx]*sgn); H[np.arange(D),np.arange(D)]+=g*dc; return H
sects=[]
for fv in itertools.product([1,-1],repeat=len(F)):
    eta,ok=mb.sector_eta(L,fv)
    if ok: sects.append((fv,np.array([eta[key] for (_,_,key) in bl],float),sum(1 for x in fv if x==-1)))
IM=[k for k,s in enumerate(sects) if all(x==-1 for x in s[0])][0]
IP=[k for k,s in enumerate(sects) if all(x==1 for x in s[0])][0]
print("=== fine attractive bracket, all 512 sectors ===")
for g in (-2.1,-2.2,-2.3,-2.4):
    E=np.array([np.linalg.eigvalsh(HM(v,g))[0] for (_,v,_) in sects])
    o=np.argsort(E); emin=E[o[0]]; nmin=int(np.sum(E<emin+1e-10))
    print(f"  g={g:>6}: nmin={nmin} minflux={sorted(set(sects[k][2] for k in np.where(E<emin+1e-10)[0]))} "
          f"unique_all-(-1)={nmin==1 and o[0]==IM} rank(-)={int(np.where(o==IM)[0][0])} "
          f"E(-)-Emin={E[IM]-emin:+.6e}   t=%.0fs"%(time.time()-t0))
print()
print("=== uniform pair only, wide g ===")
vm=sects[IM][1]; vp=sects[IP][1]
for g in (-64.,-32.,-16.,-8.,-6.,-4.,-2.,0.,2.,4.,8.,16.,64.):
    a=np.linalg.eigvalsh(HM(vm,g))[0]; b=np.linalg.eigvalsh(HM(vp,g))[0]
    print(f"   g={g:>7.1f}  E0(-)={a:.9f}  E0(+)={b:.9f}  dE={a-b:+.6e}")
print("elapsed %.1fs"%(time.time()-t0))
