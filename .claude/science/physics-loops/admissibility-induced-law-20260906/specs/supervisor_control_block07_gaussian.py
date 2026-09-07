"""Supervisor control, block 07: the Hermitian Gaussian instance of the static/formation distinction. Exact over Q(i)."""
import sympy as sp
from itertools import permutations, product
I=sp.I
def grid(n,W):
    sites=[(i,j) for i in range(n) for j in range(W)]; idx={s:k for k,s in enumerate(sites)}
    edges=[]
    for (i,j) in sites:
        if j+1<W: edges.append(((i,j),(i,j+1),'h'))
        if i+1<n: edges.append(((i,j),(i+1,j),'v'))
    return sites,idx,edges
def precision(n,W,diag=sp.Integer(3),ch=(1+2*I)/4,cv=(2-I)/4):
    sites,idx,edges=grid(n,W); N=len(sites); P=sp.zeros(N,N)
    for k in range(N): P[k,k]=diag
    for a,b,t in edges:
        c=ch if t=='h' else cv; P[idx[a],idx[b]]=c; P[idx[b],idx[a]]=sp.conjugate(c)
    return sites,idx,edges,P
def neighbors(sites,edges,s):
    out=[]
    for a,b,_ in edges:
        if a==s: out.append(b)
        if b==s: out.append(a)
    return out
def formation_precision(P,sites,idx,edges,order):
    """records-only reading: site k draws from N(mean = -sum_{y in A_k} P_ky z_y / P_kk, var 1/P_kk); the joint density is
    exp(-z^dagger L^dagger D L z) with L unit lower-triangular in the order, L_ky = P_ky/P_kk for y in A_k."""
    N=len(sites); pos={s:t for t,s in enumerate(order)}
    L=sp.eye(N); D=sp.zeros(N,N); recorded={}
    for s in order:
        k=idx[s]; D[k,k]=P[k,k]
        A=[y for y in neighbors(sites,edges,s) if pos[y]<pos[s]]; recorded[s]=A
        for y in A: L[k,idx[y]]=P[k,idx[y]]/P[k,k]
    return sp.simplify(L.H*D*L), recorded, L, D
def support(Mx):
    return frozenset((i,j) for i in range(Mx.rows) for j in range(Mx.cols) if i!=j and sp.simplify(Mx[i,j])!=0)
def is_pd_hermitian(Mx):
    return sp.simplify(Mx-Mx.H)==sp.zeros(*Mx.shape) and all(sp.re(ev)>0 for ev in Mx.eigenvals())
# ---- plaquette
sites,idx,edges,P=precision(2,2); print("plaquette: P Hermitian PD:", sp.simplify(P-P.H)==sp.zeros(4,4), [sp.N(e,6) for e in P.eigenvals()])
orders=list(permutations(sites)); classes={}
for o in orders:
    Ps,rec,L,D=formation_precision(P,sites,idx,edges,o)
    key=tuple(sorted((s,tuple(sorted(rec[s]))) for s in sites))
    classes.setdefault(key,[]).append((o,Ps))
print(f"plaquette: {len(orders)} orders, {len(classes)} recorded-set classes")
eq_static=sum(1 for o in orders if sp.simplify(formation_precision(P,sites,idx,edges,o)[0]-P)==sp.zeros(4,4))
print("  orders with P_sigma == P:", eq_static)
same_support=0; le1=0
for key,lst in classes.items():
    Ps=lst[0][1]; maxrec=max(len(A) for _,A in key)
    ss=(support(Ps)==support(P)); same_support+=ss*len(lst); le1+=(maxrec<=1)*len(lst)
    print(f"  class with recorded sets {[ (s,len(A)) for s,A in key]}: orders {len(lst)}, max recorded {maxrec}, support(P_sigma)==support(P): {ss}, diag corrections {[sp.simplify(Ps[k,k]-P[k,k]) for k in range(4)]}")
print("  orders with same support:", same_support, "; orders with <=1 recorded neighbour everywhere:", le1)
# all orders in a class give the same P_sigma
print("  within-class equality:", all(all(sp.simplify(Ps-lst[0][1])==sp.zeros(4,4) for _,Ps in lst) for lst in classes.values()))
# the path (2x1... use 1x3): P_sigma vs P
sites3,idx3,edges3,P3=precision(1,3)
for o in [((0,0),(0,1),(0,2)),((0,1),(0,0),(0,2)),((0,0),(0,2),(0,1))]:
    Ps,rec,L,D=formation_precision(P3,sites3,idx3,edges3,o)
    print(f"path 1x3 order {o}: recorded {[len(rec[s]) for s in sites3]}, P_sigma==P: {sp.simplify(Ps-P3)==sp.zeros(3,3)}, support equal: {support(Ps)==support(P3)}, diag corr {[sp.simplify(Ps[k,k]-P3[k,k]) for k in range(3)]}")
# ---- 2x3: monotone class vs snake vs mirror; covariances and read-slice blocks
sites,idx,edges,P=precision(2,3); N=6
def is_ext(o):
    pos={s:t for t,s in enumerate(o)}
    return all((j==0 or pos[(i,j-1)]<pos[(i,j)]) and (i==0 or pos[(i-1,j)]<pos[(i,j)]) for (i,j) in sites)
exts=[o for o in permutations(sites) if is_ext(o)]
Pm=[formation_precision(P,sites,idx,edges,o)[0] for o in exts]
print(f"2x3: monotone orders {len(exts)}; one P_sigma: {all(sp.simplify(x-Pm[0])==sp.zeros(N,N) for x in Pm)}")
snake=[(0,0),(0,1),(0,2),(1,2),(1,1),(1,0)]; mirror=[(0,2),(0,1),(0,0),(1,2),(1,1),(1,0)]
Ps_snake=formation_precision(P,sites,idx,edges,snake)[0]; Ps_mirror=formation_precision(P,sites,idx,edges,mirror)[0]
print("  snake P_sigma == monotone:", sp.simplify(Ps_snake-Pm[0])==sp.zeros(N,N), "; mirror == monotone:", sp.simplify(Ps_mirror-Pm[0])==sp.zeros(N,N))
Cs=sp.simplify(Pm[0].inv()); Cstat=sp.simplify(P.inv())
row1=[idx[(1,j)] for j in range(3)]; row0=[idx[(0,j)] for j in range(3)]
print("  read slice (row 1) covariance: static marginal block of P^-1 vs formation block of P_sigma^-1 equal:", sp.simplify(Cs.extract(row1,row1)-Cstat.extract(row1,row1))==sp.zeros(3,3))
# the lane's pinned object: condition on row 0 (records pinned) -> conditional covariance of row 1 = (P_11block)^-1
P11=P.extract(row1,row1); print("  pinned-static conditional covariance (P_AA)^-1 vs marginal block of P^-1 equal:", sp.simplify(P11.inv()-Cstat.extract(row1,row1))==sp.zeros(3,3))
# formation law conditioned on row 0: its row-1 block: the formation precision restricted (rows formed after row 0 with row 0 recorded): P_sigma's row1 block
print("  formation conditional-on-row-0 precision block == P_AA:", sp.simplify(Pm[0].extract(row1,row1)-P11)==sp.zeros(3,3), "; diag of P_sigma row1 block:", [sp.simplify(Pm[0][k,k]) for k in row1])
print("  formation P_sigma diag corrections (all sites):", [sp.simplify(Pm[0][k,k]-P[k,k]) for k in range(N)])
print("  fill-in pairs (nonzero P_sigma entries at non-edges):", sorted((sites[i],sites[j]) for i in range(N) for j in range(i+1,N) if (i,j) not in {(idx[a],idx[b]) for a,b,_ in edges} and sp.simplify(Pm[0][i,j])!=0))
# herm(Q^-1) != (herm Q)^-1 for a non-Hermitian Q (the lane's point), exact witness
Qn=sp.Matrix([[1,1],[-1,1]]); print("  herm(Q^-1) == (herm Q)^-1 for Q=[[1,1],[-1,1]]:", sp.simplify((Qn.inv()+Qn.inv().H)/2-((Qn+Qn.H)/2).inv())==sp.zeros(2,2))
