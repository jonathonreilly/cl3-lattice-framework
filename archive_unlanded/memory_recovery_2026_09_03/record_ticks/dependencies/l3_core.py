#!/usr/bin/env python3
"""L3 -- route B extended to the 3D-relevant clusters of the composition discriminator.

Clusters: cube (2x2x2, 8 vertices, 12 edges) and grid3x3 (9 vertices, 12 edges),
plus grid3x3 + one pendant auxiliary mode (10 vertices, 13 edges) to reach the
ODD record sector N=3 that the 12-qubit code cannot carry (prod_i B_i = I forces
N even).

Everything exact: Pauli algebra in the symplectic representation (phase mod 4),
amplitudes are Gaussian integers held as Python complex with integral parts
(asserted), sector matrices exact, ground states exact over Q(sqrt2) via sympy
Slater determinants.
"""
import itertools, sys, time
from functools import reduce
import numpy as np
import sympy as sp
from sympy import Rational, sqrt, Matrix, zeros as spzeros, eye as speye

T0 = time.time()
def hdr(s):
    print(); print("="*100); print(s); print("="*100)

def pc(n): return bin(n).count("1")

# ------------------------------------------------------------------ Pauli
class P:
    """i^k * prod_q X_q^{x_q} Z_q^{z_q}  (X before Z on every qubit)."""
    __slots__ = ("k","x","z")
    def __init__(s,k,x,z): s.k=k%4; s.x=x; s.z=z
    def __mul__(a,b): return P(a.k+b.k+2*pc(a.z & b.x), a.x^b.x, a.z^b.z)
    def neg(s): return P(s.k+2, s.x, s.z)
    def mul_i(s): return P(s.k+1, s.x, s.z)
    def dag(s): return P(-s.k+2*pc(s.x & s.z), s.x, s.z)
    def __eq__(a,b): return a.k==b.k and a.x==b.x and a.z==b.z
    def __hash__(s): return hash((s.k,s.x,s.z))
    def is_herm(s): return s.k%2 == pc(s.x & s.z)%2
    def is_id(s): return s.x==0 and s.z==0 and s.k==0
    def is_mid(s): return s.x==0 and s.z==0 and s.k==2
ID = P(0,0,0)
def comm(a,b): return (pc(a.x&b.z)+pc(a.z&b.x))%2==0
PH = [1+0j, 1j, -1+0j, -1j]
def pact(p,b):
    """P|b> = amp |b^p.x>, amp a unit Gaussian integer."""
    return b ^ p.x, PH[p.k]*((-1)**(pc(p.z & b)%2))

# ------------------------------------------------------------------ clusters
def grid_cluster(nr,nc):
    idx = {(r,c): nc*r+c for r in range(nr) for c in range(nc)}
    B=[]
    for r in range(nr):
        for c in range(nc):
            if c+1<nc: B.append((idx[(r,c)],idx[(r,c+1)]))
            if r+1<nr: B.append((idx[(r,c)],idx[(r+1,c)]))
    return nr*nc, sorted((min(u,v),max(u,v)) for u,v in B)

def cube_cluster():
    B=[(s, s^bit) for s in range(8) for bit in (4,2,1) if s^bit>s]
    return 8, sorted(B)

def cube_faces():
    """the six 4-cycles of the 2x2x2 cube; index = 4x+2y+z."""
    out=[]
    for ax in range(3):                       # fixed axis: 0->x(bit4),1->y(bit2),2->z(bit1)
        bits=[4,2,1]; fb=bits[ax]; ob=[b for b in bits if b!=fb]
        for val in (0,fb):
            cyc=[val, val|ob[1], val|ob[0]|ob[1], val|ob[0]]
            out.append(tuple(cyc))
    return out

def grid_faces(nr,nc):
    idx={(r,c):nc*r+c for r in range(nr) for c in range(nc)}
    return [ (idx[(r,c)],idx[(r,c+1)],idx[(r+1,c+1)],idx[(r+1,c)])
             for r in range(nr-1) for c in range(nc-1) ]

# ------------------------------------------------------------------ encoding
class Enc:
    def __init__(self, V, EDGES, FACES, name):
        self.name=name; self.V=V; self.EDGES=list(EDGES); self.FACES=list(FACES)
        self.NQ=len(EDGES); self.DIM=1<<self.NQ
        self.EIDX={}
        for q,(i,j) in enumerate(self.EDGES):
            self.EIDX[(i,j)]=q; self.EIDX[(j,i)]=q
        self.NBR={i:sorted(j for (a,b) in self.EDGES for j in ((b,) if a==i else ((a,) if b==i else ())))
                  for i in range(V)}
        self.STAR={i:[self.EIDX[(i,k)] for k in self.NBR[i]] for i in range(V)}
        self.STARMASK={i: reduce(lambda a,b:a|(1<<b), self.STAR[i], 0) for i in range(V)}

    # --- the verified route-B convention: Z tail on edges ordered BEFORE, at BOTH ends
    def A_unsigned(self,i,j):
        x = 1<<self.EIDX[(i,j)]; z=0
        for k in self.NBR[i]:
            if k!=j and k<j: z ^= 1<<self.EIDX[(i,k)]
        for l in self.NBR[j]:
            if l!=i and l<i: z ^= 1<<self.EIDX[(j,l)]
        return P(pc(x&z)%2, x, z)
    def A(self,i,j):
        p=self.A_unsigned(i,j)
        return p if i<j else p.neg()
    def B(self,i): return P(0,0,self.STARMASK[i])
    def loop(self,cyc):
        out=ID; n=len(cyc)
        for a in range(n): out = out*self.A(cyc[a],cyc[(a+1)%n])
        return out
    def record(self,z): return tuple(pc(z & self.STARMASK[i])%2 for i in range(self.V))

    # --- hopping (i/2) A_ij (B_i - B_j) : returns per-edge (P1,P2)
    def hop_pauli(self,i,j):
        A=self.A(i,j); return A*self.B(i), A*self.B(j)
    def hop_amp(self,P1,P2,y):
        b1,a1 = pact(P1,y); b2,a2 = pact(P2,y)
        assert b1==b2
        v = 0.5j*(a1-a2)
        assert abs(v.real-round(v.real))<1e-12 and abs(v.imag-round(v.imag))<1e-12
        return b1, complex(round(v.real), round(v.imag))

# ------------------------------------------------------------------ R0-R4 audit
def audit(E):
    R={}
    A={e:E.A(*e) for e in E.EDGES}
    Bv={i:E.B(i) for i in range(E.V)}
    R["R0_welldef"]=all(E.A_unsigned(i,j)==E.A_unsigned(j,i) for (i,j) in E.EDGES)
    R["R0_antisym"]=all(E.A(j,i)==E.A(i,j).neg() for (i,j) in E.EDGES)
    R["R1"]=(all(A[e].is_herm() and (A[e]*A[e]).is_id() for e in E.EDGES)
             and all(Bv[i].is_herm() and (Bv[i]*Bv[i]).is_id() for i in range(E.V)))
    r2=True
    for i,j in itertools.combinations(range(E.V),2): r2 &= comm(Bv[i],Bv[j])
    for e in E.EDGES:
        for v in range(E.V):
            r2 &= (comm(A[e],Bv[v]) != (v in e))
    R["R2"]=bool(r2)
    r3=True
    for e,f in itertools.combinations(E.EDGES,2):
        r3 &= (comm(A[e],A[f]) != (len(set(e)&set(f))==1))
    R["R3"]=bool(r3)
    S=[E.loop(f) for f in E.FACES]
    r4=True
    for s in S:
        r4 &= s.is_herm() and (s*s).is_id()
        for e in E.EDGES: r4 &= comm(s,A[e])
        for v in range(E.V): r4 &= comm(s,Bv[v])
    for a,b in itertools.combinations(S,2): r4 &= comm(a,b)
    R["R4"]=bool(r4); R["S_all"]=S
    R["prodB"]=reduce(lambda a,b:a*b,[Bv[i] for i in range(E.V)])
    # independent generators of the stabilizer group (over the X-parts = cycle space)
    gens=[]; basis=[]                       # gaussian elimination on x-parts
    for s in S:
        v=s.x
        for b in basis: v=min(v, v^b)
        if v!=0: basis.append(v); basis.sort(reverse=True); gens.append(s)
    R["k"]=len(gens); R["gens"]=gens
    # relations among the faces
    rel=[]
    for r in range(2,len(S)+1):
        for sub in itertools.combinations(range(len(S)),r):
            p=reduce(lambda a,b:a*b,[S[t] for t in sub])
            if p.x==0 and p.z==0: rel.append((sub, "+I" if p.k==0 else "-I" if p.k==2 else "?%d"%p.k))
    R["relations"]=rel
    # group of order 2^k, no -I, only identity has zero X-part
    grp=[]
    for m in range(1<<len(gens)):
        p=ID
        for t in range(len(gens)):
            if (m>>t)&1: p=p*gens[t]
        grp.append(p)
    R["grp"]=grp
    R["grp_ok"]=(not any(g.is_mid() for g in grp)) and sum(1 for g in grp if g.x==0)==1
    R["code_dim"]=E.DIM>>len(gens)
    return R

# ------------------------------------------------------------------ code space
def code_space(E,R):
    """cosets of the cycle space; phi[z] = unit coefficient of |z> in its coset vector."""
    grp=R["grp"]; k=R["k"]
    phi=np.zeros(E.DIM,dtype=complex); cid=-np.ones(E.DIM,dtype=np.int64)
    reps=[]; 
    for z0 in range(E.DIM):
        if cid[z0]>=0: continue
        c=len(reps); reps.append(z0)
        for g in grp:
            b,a=pact(g,z0)
            assert cid[b]<0
            cid[b]=c; phi[b]=a
    assert (cid>=0).all()
    recs=[E.record(reps[c]) for c in range(len(reps))]
    # records constant on cosets
    for z in range(E.DIM): assert E.record(z)==recs[cid[z]], "record not constant on coset"
    return cid, phi, reps, recs

def sector_matrix(E,R,cid,phi,reps,recs,keep,ham_edges=None):
    """exact H_enc restricted to the code space, rows/cols = cosets with keep(record)."""
    k=R["k"]; grp=R["grp"]
    HE = list(E.EDGES) if ham_edges is None else list(ham_edges)
    sel=[c for c in range(len(reps)) if keep(recs[c])]
    pos={c:a for a,c in enumerate(sel)}
    n=len(sel)
    Hoff=np.zeros((n,n),dtype=complex)
    hp={e:E.hop_pauli(*e) for e in HE}
    bondcount=np.zeros(n)
    signstats={"pos":0,"neg":0}; sign_detail=[]
    for c in sel:
        a=pos[c]
        rec=recs[c]
        bondcount[a]=sum(1 for (u,v) in HE if rec[u] and rec[v])
        for g in grp:
            y,ay=pact(g,reps[c])
            assert abs(phi[y]-ay)<1e-12
            for e in HE:
                P1,P2=hp[e]
                yy,amp=E.hop_amp(P1,P2,y)
                if amp==0: continue
                # amp = i * s with s = +-1 (P1,P2 are real anti-hermitian Pauli strings)
                assert abs(amp.real)<1e-12 and abs(abs(amp.imag)-1)<1e-12
                s_ = int(round(amp.imag))
                if s_>0: signstats["pos"]+=1
                else: signstats["neg"]+=1
                sign_detail.append((e,y,s_))
                cc=cid[yy]
                if cc not in pos: continue
                Hoff[pos[cc],a]+= (2.0**(-k))*np.conj(phi[yy])*amp*phi[y]
    # exactness: entries are Gaussian rationals with denominator 2^k -> check integrality of 2^k*H
    Q=Hoff*(2.0**k)
    assert np.all(np.abs(Q-np.round(Q.real)-1j*np.round(Q.imag))<1e-9)
    Hoff=(np.round(Q.real)+1j*np.round(Q.imag))/(2.0**k)
    return sel,pos,Hoff,bondcount,signstats,sign_detail

# ------------------------------------------------------------------ fermionic reference
def jw_sign(S,src,dst):
    lo,hi=min(src,dst),max(src,dst)
    return (-1)**sum(1 for kk in range(lo+1,hi) if kk in S)

def fermi_sector(EDGES, patterns):
    """H_F off-diagonal (t=1) and bond-count diagonal on the given occupation patterns."""
    idx={p:i for i,p in enumerate(patterns)}
    n=len(patterns)
    T=np.zeros((n,n)); D=np.zeros(n)
    for p in patterns:
        S=frozenset(i for i,b in enumerate(p) if b); i0=idx[p]
        D[i0]=sum(1 for (u,v) in EDGES if u in S and v in S)
        for (u,v) in EDGES:
            for (src,dst) in ((u,v),(v,u)):
                if src in S and dst not in S:
                    T2=frozenset((S-{src})|{dst})
                    tp=tuple(1 if q in T2 else 0 for q in range(len(p)))
                    T[idx[tp],i0]+= -jw_sign(S,src,dst)
    assert np.allclose(T,T.T)
    return idx,T,D

def gauge_match(Hs,Hf):
    """diagonal unitary d (entries i^k) with conj(d_a) Hs[a,b] d_b = Hf[a,b]."""
    n=Hs.shape[0]
    def unit(c):
        for kk,u in enumerate(PH):
            if abs(c-u)<1e-9: return kk
        return None
    supp_s={(a,b) for a in range(n) for b in range(n) if a!=b and abs(Hs[a,b])>1e-9}
    supp_f={(a,b) for a in range(n) for b in range(n) if a!=b and abs(Hf[a,b])>1e-9}
    if supp_s!=supp_f: return None,"support mismatch (%d vs %d)"%(len(supp_s),len(supp_f))
    e=[None]*n
    for root in range(n):
        if e[root] is not None: continue
        e[root]=0; st=[root]
        while st:
            a=st.pop()
            for b in range(n):
                if b==a or abs(Hs[a,b])<1e-9: continue
                s=unit(Hs[a,b]); f=unit(Hf[a,b])
                if s is None or f is None: return None,"entry not a unit"
                want=(e[a]+f-s)%4
                if e[b] is None: e[b]=want; st.append(b)
                elif e[b]!=want: return None,"inconsistent gauge"
    d=np.array([PH[t] for t in e])
    M=np.conj(d)[:,None]*Hs*d[None,:]
    if np.max(np.abs(M-Hf))>1e-9: return None,"verification failed"
    return d,"ok"
