#!/usr/bin/env python3
"""Item 2: open 2x2x3 block, all 512 consistent sectors, N=6 (924-dim)."""
import mb, numpy as np, itertools, time, pickle

t0=time.time()
L = mb.Lat((2,2,3), False)
F = L.faces(); NF=len(F)
bl = mb.bond_list(L); NB=len(bl)
N = 6
st, ix = mb.basis(L.nv, N); D=len(st)
print(f"2x2x3: nv={L.nv} edges={L.nq} faces={NF} bonds={NB} N={N} dim={D}")

# precompute hopping structure: (row, col, bond_index, sign)
rows=[]; cols=[]; bidx=[]; sgn=[]
diag = np.zeros(D)
diagcnt = np.zeros(D)
for k,s in enumerate(st):
    d=0
    for bi,(i,j,key) in enumerate(bl):
        if ((s>>i)&1) and ((s>>j)&1): d+=1
        for (a,b) in ((i,j),(j,i)):
            r = mb.hop_apply(s,a,b)
            if r is None: continue
            ns,sg = r
            rows.append(ix[ns]); cols.append(k); bidx.append(bi); sgn.append(sg)
    diagcnt[k]=d
rows=np.array(rows); cols=np.array(cols); bidx=np.array(bidx); sgn=np.array(sgn,dtype=float)
print("hopping nnz:", len(rows), " build %.1fs"%(time.time()-t0))

def sector_matrix(etavec, g):
    H = np.zeros((D,D))
    np.add.at(H,(rows,cols), -etavec[bidx]*sgn)
    H[np.arange(D),np.arange(D)] += g*diagcnt
    return H

# enumerate all consistent sectors
sects=[]
for fv in itertools.product([1,-1],repeat=NF):
    eta,ok = mb.sector_eta(L,fv)
    if ok:
        v=np.array([eta[key] for (_,_,key) in bl],dtype=float)
        sects.append((fv,v,sum(1 for x in fv if x==-1)))
print("consistent sectors:",len(sects), " %.1fs"%(time.time()-t0))
PLUS = [k for k,(fv,v,n) in enumerate(sects) if all(x==1 for x in fv)][0]
MINUS= [k for k,(fv,v,n) in enumerate(sects) if all(x==-1 for x in fv)][0]

out={}
for g in (0.0,0.5,1.0,2.0,4.0):
    E0=np.empty(len(sects)); E1=np.empty(len(sects)); DEG=np.empty(len(sects),dtype=int)
    for k,(fv,v,nf) in enumerate(sects):
        ev=np.linalg.eigvalsh(sector_matrix(v,g))
        E0[k]=ev[0]; E1[k]=ev[1]
        DEG[k]=int(np.sum(ev < ev[0]+1e-9))
    order=np.argsort(E0)
    emin=E0[order[0]]
    nmin=int(np.sum(E0<emin+1e-9))
    nxt=E0[order][np.searchsorted(E0[order],emin+1e-9)] if nmin<len(E0) else None
    rank_minus=int(np.where(order==MINUS)[0][0]); rank_plus=int(np.where(order==PLUS)[0][0])
    out[g]=dict(emin=emin,nmin=nmin,margin=(nxt-emin),E_minus=E0[MINUS],E_plus=E0[PLUS],
                deg_minus=DEG[MINUS],deg_plus=DEG[PLUS],rank_minus=rank_minus,rank_plus=rank_plus,
                minflux=sorted(set(sects[k][2] for k in np.where(E0<emin+1e-9)[0])),
                mbgap_minus=E1[MINUS]-E0[MINUS], deg_min=DEG[order[0]],
                emax=E0[order[-1]])
    r=out[g]
    print(f"g={g:>4} Emin={emin:.9f} nmin={r['nmin']} minflux={r['minflux']} margin={r['margin']:.8f} "
          f"E(-)={r['E_minus']:.9f}[rank {rank_minus}, deg {r['deg_minus']}] "
          f"E(+)={r['E_plus']:.9f}[rank {rank_plus}, deg {r['deg_plus']}] dE={r['E_minus']-r['E_plus']:+.9f} "
          f"spread={r['emax']-emin:.6f}  t=%.0fs"%(time.time()-t0))
pickle.dump(out, open("part2_out.pkl","wb"))
print("elapsed %.1fs"%(time.time()-t0))
