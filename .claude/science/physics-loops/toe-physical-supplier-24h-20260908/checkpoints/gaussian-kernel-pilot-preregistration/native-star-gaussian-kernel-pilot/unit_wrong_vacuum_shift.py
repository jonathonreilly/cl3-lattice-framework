"""Small Gaussian vacuum kernels; no physical work at import."""
import numpy as np

def require(ok, msg):
    if not ok: raise ValueError(msg)

def exponential_hermitian(h, scale):
    w,v=np.linalg.eigh(h)
    return (v*np.exp(scale*w))@v.conj().T

def clifford(n):
    d=1<<n; out=[]
    for j in range(n):
        x=np.zeros((d,d),complex); y=x.copy()
        for b in range(d):
            sign=(-1)**((b&((1<<j)-1)).bit_count())
            x[b^(1<<j),b]=sign
            y[b^(1<<j),b]=1j*sign*(1-2*((b>>j)&1))
        out.extend((x,y))
    return out

def fock_h(k):
    gs=clifford(len(k)//2); h=np.zeros_like(gs[0])
    for a in range(len(k)):
        for b in range(a+1,len(k)):
            h+=.5j*k[a,b]*(gs[a]@gs[b])
    return h,gs

def vacuum_kernel(segments, insertions, e0):
    """segments left-to-right; insertion (gap index, complex gamma coefficients).
    Gap i is after segment i; exactly zero or two insertions, ordered by gap.
    Returns complex vacuum matrix element and chart guard diagnostics.
    """
    n=len(segments[0][0])//2; r=np.eye(2*n,dtype=complex); coeff=[]; duration=0.
    for i,(k,t) in enumerate(segments):
        require(t>=0,'negative time')
        # Coefficient action G gamma(c) G^-1 = gamma(exp(-itK)c).
        r=r@exponential_hermitian(1j*k,-t); duration+=t
        for gap,c in insertions:
            if gap==i: coeff.append(r@c)
    require(len(coeff) in (0,2),'insertion count')
    rows=(np.eye(2*n)[::2]+1j*np.eye(2*n)[1::2])*.5
    transformed=rows@r.T
    u=transformed[:,::2]-1j*transformed[:,1::2]
    v=transformed[:,::2]+1j*transformed[:,1::2]
    distance=float(np.linalg.norm(u-np.eye(n),2))
    require(distance<.75,'outside prospectively fixed logarithm chart')
    ev=np.linalg.eigvals(u)
    require(np.all(ev.real>0),'log branch')
    c0=np.exp(-e0*duration+.5*np.log(ev).sum())
    z=-np.linalg.solve(u,v)
    require(np.linalg.norm(z+z.T)<1e-10,'Thouless skew residual')
    value=c0
    if coeff:
        x,y=coeff; ax=x[::2]-1j*x[1::2]; ay=y[::2]-1j*y[1::2]; by=y[::2]+1j*y[1::2]
        value=c0*(ax@by-ax@z@ay)
    return value, {'chart_distance':distance,'thouless_skew':float(np.linalg.norm(z+z.T))}

def literal_kernel(segments, insertions,e0):
    n=len(segments[0][0])//2; dim=1<<n; result=np.eye(dim,dtype=complex)
    for i,(k,t) in enumerate(segments):
        h,gs=fock_h(k); result=result@exponential_hermitian(h-e0*np.eye(dim),-t)
        for gap,c in insertions:
            if gap==i: result=result@sum((c[a]*gs[a] for a in range(2*n)),np.zeros_like(result))
    return result[0,0]

def physical_geometry(pair):
    coords=[(x,y,z) for x in range(4) for y in range(4) for z in range(4)]
    idx={r:i for i,r in enumerate(coords)}; k=np.zeros((64,64))
    for r in coords:
        for a in range(3):
            s=list(r); s[a]=(s[a]+1)%4; s=tuple(s)
            eta=(-1)**sum(r[:a]); ap=-1 if r[a]==3 else 1
            i,j=idx[r],idx[s]; k[i,j]=-2*eta*ap; k[j,i]=2*eta*ap
    require(np.array_equal(k@k,-24*np.eye(64)),'literal AP K square')
    center=idx[(0,0,0)]; neighbors=[idx[r] for r in [(1,0,0),(3,0,0),(0,1,0),(0,3,0),(0,0,1),(0,0,3)]]
    seeds=[center]+[neighbors[j] for j in sorted(set(pair[0]+pair[1]))]
    columns=[]; omega=np.sqrt(24.)
    for site in seeds:
        a=np.eye(64)[:,site].copy()
        for c in columns: a-=c*(c@a)
        norm=np.linalg.norm(a)
        if norm<1e-11: continue
        a/=norm; b=-k@a/omega; columns.extend([a,b])
    q=np.column_stack(columns); require(q.shape[1]<=10,'carrier exceeds five modes')
    require(np.linalg.norm(q.T@q-np.eye(q.shape[1]))<1e-11,'carrier Gram')
    require(np.linalg.norm(k@q-q@(q.T@k@q))<1e-10,'carrier invariant')
    kr=q.T@k@q; expected=np.kron(np.eye(q.shape[1]//2),[[0,omega],[-omega,0]])
    require(np.linalg.norm(kr-expected)<1e-10,'reference vacuum orientation')
    ks=[]; js=[]
    for group in pair:
        new=k.copy()
        for j in group:
            v=neighbors[j]; new[center,v]*=-1; new[v,center]*=-1
        require(np.linalg.norm((new-k)-q@(q.T@(new-k)@q)@q.T)<1e-10,'defect support')
        ks.append(q.T@new@q)
        # Delta K = center*d^T-d*center^T, B=i gamma(center)gamma(d)/2.
        d=(new-k)[center,:]; js.append(1j*(q.T@d))
    return ks,js,q.T@np.eye(64)[:,center],-omega*q.shape[1]/4,{'real_dimension':q.shape[1],'literal_K_square':True}
