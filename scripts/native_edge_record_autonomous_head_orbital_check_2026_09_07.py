#!/usr/bin/env python3
"""Independent orbital/determinant event-epoch checker; no primary imports.

C_R is a mixture of Slaters, generally not Gaussian. In orbital bases,
C_R[a,b] = sum_mn U[a,m] C0[m,n] U[b,n]*
 * K(e0[m]-e0[n]-eR[a]+eR[b]). K is obtained by integrating two
translated sine packets, not from a many-body eigensystem. Event averaging
uses direct positive-time quadrature, never rational Laplace multipliers.
Battery density uses all 70 by 70 Slater determinant overlaps with complex
phases retained. Equal initial energy groups are summed coherently; every
group is retained. Fuel shifts each translated packet by k Delta.
"""
import os
for _v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[_v]='1'
os.environ.setdefault('AUDIT_TIMEOUT_SEC','180')
import argparse, itertools, json, math, resource, signal, sys, time
from fractions import Fraction
import numpy as np
from numpy.polynomial.legendre import leggauss

# s is minus the hopping coefficient; current below equals 2*h_uv*Im(C_uv).
EDGES=[(a,b,-c) for (a,b),c in zip([(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)],[-1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1])]
SUB=np.array(list(itertools.combinations(range(8),4)))

def hamiltonian(mask):
    h=np.zeros((8,8))
    for i,(a,b,s) in enumerate(EDGES):
        if not mask>>i&1: h[a,b]=h[b,a]=-s
    return h

def kernel(d):
    x=np.abs(d)
    return np.where(x<1,(1-x)*np.cos(np.pi*x)+np.sin(np.pi*x)/np.pi,0.)

def density(t,j):
    if j==1:return 3*np.exp(-3*t)
    if j==2:return 6*np.exp(-2*t)*(-np.expm1(-t))
    # Remainders evaluated by a convergent Taylor series near zero.
    a=np.expm1(-t)+t if j==3 else t*t-2*t-2*np.expm1(-t)
    small=t<.1
    ts=t[small]; r=np.zeros_like(ts)
    for n in range(2 if j==3 else 3,22):
        r+=((-1.)**n/math.factorial(n) if j==3 else -2*(-1.)**n/math.factorial(n))*ts**n
    a[small]=r
    return 12*np.exp(-2*t)*a

def tail(j,t=20):
    return [math.exp(-3*t),3*math.exp(-2*t)-2*math.exp(-3*t),(6*t-3)*math.exp(-2*t)+4*math.exp(-3*t),(6*t*t-6*t+9)*math.exp(-2*t)-8*math.exp(-3*t)][j-1]

def mesh(order,cells):
    x,w=leggauss(order); edges=np.linspace(0,20,cells+1)
    return ((edges[:-1,None]+edges[1:,None])/2+x*(10/cells)).ravel(),np.tile(w*(10/cells),cells)

def average(cr,ev,vec,j,order=16,cells=40,reverse=False):
    t,w=mesh(order,cells); weights=w*density(t,j)
    # Explicit exp(-i h t) covariance dynamics, evaluated in its orbital basis.
    phase=np.exp((-1j if not reverse else 1j)*t[:,None]*ev)
    cov=np.einsum('t,ta,ab,tb->ab',weights,phase,cr,phase.conj())
    return vec@cov@vec.conj().T

def battery(ev,vr,e0,v0,X,k,order=16,fuel=1,phase_mutation=False):
    a=np.linalg.det(np.stack([v0[:,ii].conj().T@X for ii in SUB]))
    overlaps=vr.conj().T@v0
    d=np.linalg.det(overlaps[SUB[:,None,:,None],SUB[None,:,None,:]])
    coeff=d*a[None,:]
    if phase_mutation:coeff=np.abs(coeff)
    initial=e0[SUB].sum(axis=1); final=ev[SUB].sum(axis=1)
    # Group only exact-degeneracy sums within roundoff; verify grouping width.
    labels=np.round(initial,11); groups=np.unique(labels)
    centers=np.array([initial[labels==g].mean() for g in groups])
    width=max(float(np.ptp(initial[labels==g])) for g in groups)
    assert width<1e-12
    grouped=np.stack([coeff[:,labels==g].sum(axis=1) for g in groups],axis=1)
    x,w=leggauss(order); norm=moment=0.; lower=math.inf; upper=-math.inf
    for j in range(70):
        shifts=centers-final[j]+k*fuel
        starts=48+shifts; ends=49+shifts
        lower=min(lower,float(starts.min()));upper=max(upper,float(ends.max()))
        knots=np.unique(np.clip(np.r_[starts,ends,0.,97.],0,97))
        lo=knots[:-1];hi=knots[1:]
        E=((lo+hi)[:,None]/2+(hi-lo)[:,None]/2*x).ravel()
        W=((hi-lo)[:,None]/2*w).ravel()
        u=E[:,None]-starts[None,:]
        beta=np.where((u>=0)&(u<=1),np.sqrt(2)*np.sin(np.pi*u),0)
        g=beta@grouped[j]; prob=np.abs(g)**2
        norm+=float(W@prob);moment+=float((W*E)@prob)
    return dict(norm=norm,mean=moment,support=[lower,upper],energy_groups=len(groups),group_width=width)

def connected(mask):
    seen={0}
    while True:
        old=len(seen)
        for i,(a,b,s) in enumerate(EDGES):
            if not mask>>i&1 and (a in seen or b in seen):seen.update((a,b))
        if len(seen)==old:return len(seen)==8

def paths():
    levels=[[((),0,0,Fraction(1),())]]
    for j in range(4):
        out=[]
        for p,head,mask,w,rates in levels[-1]:
            incident=[i for i,(a,b,s) in enumerate(EDGES) if head in (a,b) and not mask>>i&1]
            for i in incident:
                a,b,s=EDGES[i];out.append((p+(i,),a^b^head,mask|1<<i,w/len(incident),rates+(len(incident),)))
        levels.append(out)
    return levels

def observables(c,mask):
    current=[float(2*s*c[b,a].imag) if not mask>>i&1 else 0. for i,(a,b,s) in enumerate(EDGES)]
    live=[abs(v) for i,v in enumerate(current) if not mask>>i&1]
    return dict(density=c.diagonal().real.tolist(),currents=current,N=float(np.trace(c).real),eigenvalues=np.linalg.eigvalsh(c).tolist(),energy=float(np.trace(hamiltonian(mask)@c).real),hermiticity=float(np.max(abs(c-c.conj().T))),support_count=sum(v>=.02 for v in live),current_max=max(live),density_pass=bool(np.min(c.diagonal().real)>=.1 and np.max(c.diagonal().real)<=.9))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args()
    signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180 second audit contract')));signal.alarm(int(os.environ['AUDIT_TIMEOUT_SEC']))
    start=time.monotonic();e0,v0=np.linalg.eigh(hamiltonian(0));X=v0[:,:4].astype(complex);X[0]*=np.exp(-.7j);X[1]*=np.exp(.7j)
    c0=X@X.conj().T; c0eig=v0.conj().T@c0@v0; Einit=float(np.trace(hamiltonian(0)@c0).real)
    levels=paths(); cache={}; rows=[]; maxconv=0.; ebconv=0.; checks=[]
    for j in range(1,5):
        t,w=mesh(16,40);f=density(t,j);m=[float(w@(f*t**n)) for n in range(3)];mean=1/3+(j-1)/2;var=1/9+(j-1)/4
        checks.append(dict(event=j,tail=tail(j),integrals=m,normalization_error=abs(m[0]+tail(j)-1),mean_error=abs(m[1]-mean),variance_error=abs(m[2]-m[1]**2-var)))
        assert sum(p[3] for p in levels[j])==1
        for p,head,mask,weight,rates in levels[j]:
            assert rates==(3,)+(2,)*(j-1)
            for surface,k,mask2 in [('pre',j-1,mask^(1<<p[-1])),('post',j,mask)]:
                assert connected(mask2)
                key=(mask2,k)
                if key not in cache:
                    ev,vr=np.linalg.eigh(hamiltonian(mask2));U=vr.conj().T@v0
                    gaps=e0[None,None,:,None]-e0[None,None,None,:]-ev[:,None,None,None]+ev[None,:,None,None]
                    cr=np.einsum('am,mn,bn,abmn->ab',U,c0eig,U.conj(),kernel(gaps))
                    b=battery(ev,vr,e0,v0,X,k);b32=battery(ev,vr,e0,v0,X,k,32)
                    ebconv=max(ebconv,abs(b['mean']-b32['mean']),abs(b['norm']-b32['norm']))
                    cache[key]=(ev,vr,cr,b32)
                ev,vr,cr,b=cache[key]
                c=average(cr,ev,vr,j);fine=average(cr,ev,vr,j,32,80)
                maxconv=max(maxconv,float(np.max(abs(c-fine))))
                o=observables(fine,mask2);o.update(event=j,surface=surface,path=list(p),head=(head^EDGES[p[-1]][0]^EDGES[p[-1]][1]) if surface=='pre' else head,selected_destination=head,mask=mask2,mask_convention='deleted_edge_bits',deletions=k,weight=str(weight),rates=list(rates),battery=b,ledger_residual=o['energy']+b['mean']-k-Einit-48.5)
                expected_head=0
                for edge_id in p[:k]:
                    edge_a,edge_b,_=EDGES[edge_id];assert expected_head in (edge_a,edge_b);expected_head^=edge_a^edge_b
                assert o['head']==expected_head
                if surface=='pre':assert o['head']!=o['selected_destination']
                o['selected_edge_current']=o['currents'][p[-1]] if surface=='pre' else None
                o['front005_pass']=abs(o['selected_edge_current'])>=.05 if surface=='pre' else None
                assert abs(o['N']-4)<1e-10 and o['hermiticity']<1e-12
                assert min(o['eigenvalues'])>-1e-12 and max(o['eigenvalues'])<1+1e-12
                assert b['support'][0]>=0 and b['support'][1]<=97
                rows.append(o)
    result=dict(contract=dict(timeout_seconds=180,blas_threads=1,rss_limit_MiB=180),edges=EDGES,initial_energy=Einit,path_counts=[len(x) for x in levels],time_checks=checks,time_mesh_convergence=maxconv,battery_quadrature_convergence=ebconv,rows=rows,totals=[])
    for j in range(1,5):
        for surface in ('pre','post'):
            rr=[r for r in rows if r['event']==j and r['surface']==surface]
            result['totals'].append(dict(event=j,surface=surface,weight=str(sum(Fraction(r['weight']) for r in rr)),mean_energy=sum(float(Fraction(r['weight']))*r['energy'] for r in rr),mean_battery=sum(float(Fraction(r['weight']))*r['battery']['mean'] for r in rr),support4_count=sum(r['support_count']>=4 for r in rr),front005_count=sum(r['front005_pass'] for r in rr) if surface=='pre' else None,density_pass_count=sum(r['density_pass'] for r in rr)))
    # Trajectory comparator uses the selected edge before each deletion.
    trajectory_front=[]
    for path,head,mask,weight,rates in levels[4]:
        selected=[next(r for r in rows if r['surface']=='pre' and r['event']==j and tuple(r['path'])==path[:j])['selected_edge_current'] for j in range(1,5)]
        trajectory_front.append(dict(path=list(path),weight=str(weight),selected_pre_currents=selected,front_max=max(abs(x) for x in selected),front005_pass=max(abs(x) for x in selected)>=.05))
    result['trajectory_front']=trajectory_front
    result['trajectory_front005_count']=sum(r['front005_pass'] for r in trajectory_front)
    # Manual indexing cross-check and corruption of the selected-edge definition.
    assert all(r['selected_edge_current']==r['currents'][r['path'][-1]] for r in rows if r['surface']=='pre')
    result['front_definition_mutation']=dict(discrepancy=max(abs(abs(r['selected_edge_current'])-r['current_max']) for r in rows if r['surface']=='pre'))
    assert result['front_definition_mutation']['discrepancy']>1e-8
    # Independent adaptive time quadrature family on a nontrivial endpoint.
    from scipy.integrate import quad_vec, quad
    mask,k=next(key for key in cache if key[1]==4)
    ev,vr,cr,b=cache[(mask,k)]
    def integrand(t):
        z=np.exp(-1j*ev*t)
        return density(np.array([t]),4)[0]*(z[:,None]*cr*z.conj()[None,:])
    adapt,adapt_error=quad_vec(integrand,0,20,epsabs=1e-12,epsrel=1e-12)
    baseline=average(cr,ev,vr,4,32,80)
    adaptive_delta=float(np.max(abs(vr@adapt@vr.conj().T-baseline)))
    # Direct sine overlap quadrature independently checks the finite kernel.
    kernel_errors=[]
    for d in (-1.1,-.9,-.25,0.,.15,.8,1.1):
        lo=max(0.,d);hi=min(1.,1+d)
        direct=quad(lambda x:2*np.sin(np.pi*x)*np.sin(np.pi*(x-d)),lo,hi,epsabs=1e-13)[0] if hi>lo else 0.
        kernel_errors.append(abs(direct-float(kernel(np.array(d)))))
    result['second_time_family']=dict(adaptive_error_estimate=float(adapt_error),difference=adaptive_delta)
    result['kernel_direct_integral_error']=max(kernel_errors)
    mutants={}
    def record(name,value,threshold=1e-8):
        mutants[name]=dict(discrepancy=float(value),detected=bool(value>threshold))
    record('omit_event_wait',np.max(abs(vr@cr@vr.conj().T-baseline)))
    record('reverse_time_gap',np.max(abs(average(cr,ev,vr,4,reverse=True)-baseline)))
    # Time rescaling doubles every waiting rate, preserving normalization but changing means.
    t,w=mesh(32,80);z=np.exp(-1j*t[:,None]*ev/2)
    wrong=np.einsum('t,ta,ab,tb->ab',w*density(t,4),z,cr,z.conj())
    record('double_wait_rates',np.max(abs(vr@wrong@vr.conj().T-baseline)))
    for fuel in (0,2):
        wrongb=battery(ev,vr,e0,v0,X,k,32,fuel=fuel)
        record('fuel_offset_'+str(fuel),abs(wrongb['mean']-b['mean']))
    wrongb=battery(ev,vr,e0,v0,X,k,32,phase_mutation=True)
    record('discard_determinant_phases',max(abs(wrongb['norm']-1),abs(wrongb['mean']-b['mean'])))
    U=vr.conj().T@v0
    coherent=U@c0eig@U.conj().T
    record('replace_battery_kernel_by_one',np.max(abs(average(coherent,ev,vr,4)-baseline)))
    gaps=e0[None,None,:,None]-e0[None,None,None,:]-ev[:,None,None,None]+ev[None,:,None,None]
    no_pulse=v0[:,:4]@v0[:,:4].conj().T
    no_pulse_eig=v0.conj().T@no_pulse@v0
    wrongcr=np.einsum('am,mn,bn,abmn->ab',U,no_pulse_eig,U.conj(),kernel(gaps))
    record('omit_input_pulse',np.max(abs(average(wrongcr,ev,vr,4)-baseline)))
    record('double_path_weight',abs(sum(float(p[3])*2 for p in levels[4])-1))
    record('cap_tail_false_zero',tail(4,2),1e-4)
    # A false narrow cap cuts declared support; it cannot claim the safe-domain theorem.
    record('cap_upper_49',max(0.,b['support'][1]-49))
    record('reuse_initial_mask',np.max(abs(hamiltonian(mask)-hamiltonian(0))))
    record('N3_input',abs(np.trace(v0[:,:3]@v0[:,:3].conj().T).real-4))
    result['mutations']=mutants
    assert all(x['detected'] for x in mutants.values())
    assert adaptive_delta<2e-11 and max(kernel_errors)<2e-12
    result['max_ledger_residual']=max(abs(r['ledger_residual']) for r in rows)
    result['max_battery_norm_error']=max(abs(r['battery']['norm']-1) for r in rows)
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024 if sys.platform=='darwin' else 1024)
    result['resources']=dict(seconds=time.monotonic()-start,peak_rss_MiB=rss)
    assert rss<180 and maxconv<2e-11 and ebconv<2e-10 and result['max_ledger_residual']<2e-9 and result['max_battery_norm_error']<2e-10
    print(json.dumps(result,indent=None if args.json else 2) if args.json else json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
