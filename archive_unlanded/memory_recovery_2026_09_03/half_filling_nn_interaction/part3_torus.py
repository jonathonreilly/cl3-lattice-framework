#!/usr/bin/env python3
"""Item 3: uniform sectors on L^3 coarse tori.  Free Fermi sea, 1st-order
   PT in V, crossing g_c, and MBPT2 on 4^3."""
import mb, numpy as np, itertools, time
from common import EX, eta_ks
t0=time.time()

def torus(Lsz):
    return mb.Lat((Lsz,Lsz,Lsz), True)

def eta_field(L, kind, twist):
    """kind '+' plain, '-' Kawamoto-Smit; twist = (tx,ty,tz) in {+1,-1}:
       flip every bond that wraps in that direction."""
    eta={}
    for (v,ax) in L.E:
        w = L.step(v,EX[ax])
        e = 1 if kind=='+' else eta_ks(v,ax)
        # wrapping bond: v[ax] == dims[ax]-1
        if v[ax]==L.dims[ax]-1:
            e *= twist[ax]
        eta[(v,ax)] = e
    return eta

def analyse(L, eta, verbose=False):
    M = mb.one_particle(L, eta)                 # M_ij = eta_ij  (hopping matrix)
    w, C = np.linalg.eigh(-M)                   # H_kin = -t sum eta (bipartite: same spectrum)
    V = L.nv; Nh = V//2
    Efree = w[:Nh].sum()
    shell_gap = w[Nh]-w[Nh-1]
    Cocc = C[:,:Nh]
    P = Cocc @ Cocc.T
    bl = mb.bond_list(L)
    A = 0.0
    for (i,j,key) in bl:
        A += P[i,i]*P[j,j] - P[i,j]**2
    return dict(Efree=Efree, gap=shell_gap, A=A, w=w, C=C, P=P, bl=bl, V=V, Nh=Nh)

print("=== free part + first-order <sum_bonds n_i n_j> at half filling ===")
store={}
for Lsz in (4,6,8):
    L = torus(Lsz)
    for kind in ('+','-'):
        best=None
        for tw in itertools.product([1,-1],repeat=3):
            eta = eta_field(L,kind,tw)
            r = analyse(L,eta)
            if best is None or r['Efree'] < best[1]['Efree']-1e-12:
                best=(tw,r)
        tw,r=best
        store[(Lsz,kind)]=r
        V=r['V']; NB=len(r['bl'])
        print(f"L={Lsz} sector {kind} best twist {tw}: Efree={r['Efree']:.9f} ({r['Efree']/V:+.9f}/site) "
              f"shell gap={r['gap']:.6f}  A=sum<n n>={r['A']:.9f} ({r['A']/V:.9f}/site)  bonds={NB}  "
              f"free-mean {NB/4/V:.6f}/site")
    rp, rm = store[(Lsz,'+')], store[(Lsz,'-')]
    dE = rm['Efree']-rp['Efree']; dA = rm['A']-rp['A']; V=rp['V']
    gc = -dE/dA if abs(dA)>1e-12 else None
    print(f"  L={Lsz}: dEfree={dE:+.9f} ({dE/V:+.9f}/site)  dA={dA:+.9f} ({dA/V:+.9f}/site) "
          f" g_c(1st order) = {gc if gc is None else round(gc,9)}")
    print()

# ---------------- MBPT2 on 4^3 ----------------
print("=== MBPT2 on 4^3 (both uniform sectors, optimal twist) ===")
for kind in ('+','-'):
    r = store[(4,kind)]
    w=r['w']; C=r['C']; Nh=r['Nh']; V=r['V']; bl=r['bl']; P=r['P']
    W = np.zeros((V,V))
    for (i,j,key) in bl:
        W[i,j]=1.0; W[j,i]=1.0          # sum_{i<j} W_ij n_i n_j  with W=V on bonds
    occ=np.arange(Nh); vir=np.arange(Nh,V)
    Co=C[:,occ]; Cv=C[:,vir]
    # Y[i,a,m] = C[m,i]*C[m,a]
    Y = np.einsum('mi,ma->iam', Co, Cv)         # (No,Nv,V)
    Yf = Y.reshape(Nh*(V-Nh), V)
    Mmat = Yf @ W @ Yf.T                        # <ij|ab> = M[(i,a),(j,b)]
    No=Nh; Nv=V-Nh
    Mm = Mmat.reshape(No,Nv,No,Nv)
    iajb = Mm                                   # <ij|ab>
    ibja = np.transpose(Mm, (0,3,2,1))          # M[(i,b),(j,a)] = <ij|ba>
    anti = iajb - ibja                          # <ij||ab>, index order i,a,j,b
    eo=w[occ]; ev=w[vir]
    den = eo[:,None,None,None]-ev[None,:,None,None]+eo[None,None,:,None]-ev[None,None,None,:]
    E2_2body = 0.25*np.sum(anti**2/den)
    # one-body (non-HF reference) term
    f = np.einsum('iam,mn,n->ia', Y, W, np.diag(P)) - np.einsum('mi,na,mn,mn->ia', Co, Cv, W, P)
    E2_1body = np.sum(f**2/(eo[:,None]-ev[None,:]))
    r['c2']=E2_2body+E2_1body; r['c2a']=E2_2body; r['c2b']=E2_1body
    print(f"  sector {kind}: E2/V_int^2 = {r['c2']:.9f}  (2-body {E2_2body:.9f}, 1-body {E2_1body:.9f}) "
          f" per site {r['c2']/V:.9f}")
rp,rm=store[(4,'+')],store[(4,'-')]
a=rm['c2']-rp['c2']; b=rm['A']-rp['A']; c=rm['Efree']-rp['Efree']
print(f"  4^3 dE(g) = {c:+.9f} + {b:+.9f} g + {a:+.9f} g^2")
disc=b*b-4*a*c
if disc>=0 and abs(a)>1e-14:
    r1=(-b+np.sqrt(disc))/(2*a); r2=(-b-np.sqrt(disc))/(2*a)
    print(f"  roots of the 2nd-order truncation: g = {r1:.6f}, {r2:.6f}")
else:
    print("  no real root of the 2nd-order truncation")
print("elapsed %.1fs"%(time.time()-t0))
