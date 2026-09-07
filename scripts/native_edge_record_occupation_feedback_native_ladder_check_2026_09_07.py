#!/usr/bin/env python3
"""Native finite-ladder occupation-feedback check, independent of cube runners.

Uses the frozen independent native checker as a declared carrier dependency;
its main is not executed. New tests use actual joint matrices for energy,
no-jump evolution, negative battery drift and conditional energy selection.
The supplied irreversible generator has no identity-refusal completion.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import resource
import signal
import sys
import time
import native_edge_record_autonomous_head_native_ladder_check_2026_09_07 as n
import numpy as np
from scipy.linalg import eigh,expm

AUDIT_INPUT_PATHS = (
    'scripts/native_edge_record_autonomous_head_native_ladder_check_2026_09_07.py',
)
AUDIT_TIMEOUT_SEC = 180
RSS_LIMIT_MIB = 180
I=n.I; CAP=n.CAP
checks=0; worst=0.
def check(a,b,label,tol=2e-9):
 global checks,worst
 err=float(np.max(np.abs(np.asarray(a)-np.asarray(b)),initial=0))
 if err>tol:raise AssertionError(f'{label}: {err}')
 checks+=1;worst=max(worst,err)

def directed(edge,head):
 u,v=n.EDGES[edge];target=v if head==u else u
 nw=(I-n.B[target])/2
 # Independent algebra: [n_w,T]=J-J*, so this is c_w* c_v.
 hop=n.HOPS[edge]
 return (hop+nw@hop-hop@nw)/2

def embed(h,E):
 a,v=eigh(h); out=np.zeros((len(h)*CAP,len(h)),complex)
 for j,energy in enumerate(a):
  slot=int(round(E-energy))
  if 0<=slot<CAP:out+=np.kron(np.outer(v[:,j],v[:,j].conj()),np.eye(CAP)[:,slot:slot+1])
 return out

def build(records,head):
 q,h,live=n.sector(records); lifts=[]; outs=[]; M=np.zeros_like(h)
 incident=[e for e in live if head in n.EDGES[e]]
 for e in incident:
  J=directed(e,head);j=q.conj().T@J@q
  u,v=n.EDGES[e];w=v if u==head else u
  expected=q.conj().T@((I-n.B[head])/2)@((I+n.B[w])/2)@q
  check(j.conj().T@j,expected,'directed occupancy effect')
  _,_,_,branches=n.branches(records,e)
  effect=np.zeros_like(h); branch_weights=[]
  for r,g,k in branches:
   b=k@j;effect+=b.conj().T@b;branch_weights.append(float(np.trace(b.conj().T@b).real))
   check(r.conj().T@n.N@r@b,b@q.conj().T@n.N@q,'directed native N')
   for old,z in records.items():check(n.Z[old]@r@b,z*r@b,'directed old Record')
   # n.lift constructs actual finite translations and checks Hout L=L Hin.
   L=n.lift(h,g,b);lifts.append(L);outs.append(g)
   Nout=np.kron(r.conj().T@n.N@r,np.eye(CAP));Nin=np.kron(q.conj().T@n.N@q,np.eye(CAP))
   check(Nout@L,L@Nin,'lifted native N')
  check(effect,expected,'noncomplete directed two-sign effect')
  if records=={0:1} and head==1 and e==1:
   if branch_weights[0]<.5:raise AssertionError('reachable directed bridge inactive')
   check(branch_weights[1],0,'directed bridge projects post-hop parity, not input parity')
  M+=expected
 R=sum(L.conj().T@L for L in lifts)
 H=n.total(h)
 check(H@R,R@H,'rate commutes total H')
 # Full energy spectral indicators, including boundary cap inputs.
 vals,V=eigh(H)
 out_spectra=[eigh(n.total(g)) for g in outs]
 for energy in np.unique(np.rint(vals)):
  p=V[:,abs(vals-energy)<1e-9];p=p@p.conj().T
  adj=-(R@p+p@R)/2
  for L,(a,v) in zip(lifts,out_spectra):
   po=v[:,abs(a-energy)<1e-9];po=po@po.conj().T
   adj+=L.conj().T@po@L
  check(adj,0,'GKSL preserves every total-energy indicator')
 check(sum(L.conj().T@L for L in lifts)-R,0,'GKSL trace preservation without refusal')
 W=embed(h,20)
 check(W.conj().T@W,np.eye(len(h)),'safe fiber isometry')
 check(H@W,20*W,'literal safe total-energy fiber')
 check(R@W,W@M,'safe fiber exact matter-dependent rate')
 return q,h,M,H,R,lifts,outs,W,len(incident)

def main():
    global checks,worst
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args()
    signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('180 second audit limit')))
    signal.alarm(AUDIT_TIMEOUT_SEC)
    start=time.monotonic()
    checks=0;worst=0.
    native_start=n.checks
    q,h,M,H,R,Ls,outs,W,degree=build({},0)
    # Additional bridge sector with an old Record, head1 reached after edge01.
    bridge=build({0:1},1)
    del bridge
    # Full physical occupation selector x0=(1,0,0,1), x1=(0,1,0,1).
    P=I.copy()
    for v,occ in enumerate((1,0,0,1)):P=P@((I+(1-2*occ)*n.B[v])/2)
    a,V=eigh(q.conj().T@P@q);x0=V[:,np.argmax(a)]
    check(a.max(),1,'native N2 occupancy exists')
    x1=q.conj().T@n.HOPS[0]@q@x0
    check(np.linalg.norm(x1),1,'native edge partner normalized')
    C=np.column_stack([x0,x1]);check(C.conj().T@C,np.eye(2),'native two-configuration orthonormality')
    check(q.conj().T@n.N@q@C,2*C,'negative witness fixed N2')
    check(C.conj().T@M@C,np.diag([1,0]),'other outgoing head edge blocked')
    # Compute the full actual battery adjoint, including the no-jump anticommutator.
    EB=np.kron(np.eye(len(h)),np.diag(np.arange(CAP)))
    drift=-(R@EB+EB@R)/2
    for L,g in zip(Ls,outs):drift+=L.conj().T@np.kron(np.eye(len(g)),np.diag(np.arange(CAP)))@L
    D2=C.conj().T@W.conj().T@drift@W@C
    check(D2,np.array([[1,.5],[.5,0]]),'actual joint drift Rayleigh matrix')
    a,V=eigh(np.array([[1.,.5],[.5,0.]]));chi=C@V[:,0];state=W@chi
    negative=float(np.vdot(state,drift@state).real)
    check(np.linalg.norm(state),1,'negative witness normalized')
    check(H@state,20*state,'negative witness safe E20')
    check(negative,(1-np.sqrt(2))/2,'negative battery drift eigenvalue')
    # No-jump comparison is actual full physical matrix exponential.
    t=.73
    actual=expm((-1j*H-R/2)*t)@state
    reference=W@expm(-M*t/2)@chi*np.exp(-20j*t)
    check(actual,reference,'physical no-jump vs energy-fiber exponential')
    _,U=eigh(M);dark=U[:,np.linalg.eigvalsh(M)<1e-9];darkmass=float(np.linalg.norm(dark.conj().T@chi)**2)
    if darkmass<=.1:raise AssertionError('dark survival absent')
    longsurvival=float(np.linalg.norm(expm(-M*40/2)@chi)**2)
    check(longsurvival,darkmass,'positive limiting no-jump survival')
    # Noncommutation with EB demonstrates why anticommutator affects battery.
    ebcomm=float(np.max(abs(R@EB-EB@R)))
    if ebcomm<.1:raise AssertionError('battery rate commutator unexpectedly absent')
    mutations={}
    def reject(label,wrong,right):
     try:check(wrong,right,label)
     except AssertionError as exc:mutations[label]=str(exc)
     else:raise AssertionError('undetected '+label)
    reject('wrong_scalar_degree_nojump',np.exp(-degree*t/2)*state*np.exp(-20j*t),reference)
    # Completing each edge's contraction to identity forces degree I on safe input.
    reject('fake_identity_refusal_rate',degree*W,W@M)
    reject('omit_battery_anticommutator',sum(np.vdot(L@state,np.kron(np.eye(len(g)),np.diag(np.arange(CAP)))@(L@state)).real for L,g in zip(Ls,outs)),negative)
    # Explicit separate 2-state correlated-input selective-energy calculation.
    h2=np.array([[1.,1.],[1.,1.]]);g2=np.zeros((2,2));j2=np.array([[0.,0.],[1.,0.]])
    l2=n.lift(h2,g2,j2);H2=n.total(h2);G2=n.total(g2)
    active=embed(h2,10)@np.array([1.,0.]);darkstate=embed(h2,20)@np.array([0.,1.])
    rho=(np.outer(active,active.conj())+np.outer(darkstate,darkstate.conj()))/2
    jump=l2@rho@l2.conj().T;weight=float(np.trace(jump).real)
    unconditional=float(np.trace(H2@rho).real);conditional=float(np.trace(G2@jump).real/weight)
    check(weight,.5,'correlated active selection weight')
    check(unconditional,15,'correlated unconditional total energy')
    check(conditional,10,'correlated conditional total energy')
    check(np.linalg.norm(l2@darkstate),0,'correlated dark branch absent')
    # Here active rate1 and dark rate0 make these also eventual first-event values.
    if abs(unconditional-conditional)<1:raise AssertionError('conditional energy filtering absent')
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
    assert rss<RSS_LIMIT_MIB and time.monotonic()-start<AUDIT_TIMEOUT_SEC
    result=dict(checks=checks,native_checks=n.checks-native_start,worst=max(worst,n.worst),negative_drift=negative,rayleigh_matrix=D2.real.tolist(),dark_survival=darkmass,battery_rate_commutator=ebcomm,conditional_energy=dict(unconditional=unconditional,first_event=conditional,event_probability=weight),mutations=mutations,seconds=time.monotonic()-start,rss_MiB=rss,scope='Native square N2, opposite dimer hopping, fuel gap1, retained ladder0..33; separate two-state correlated selection; not full cube computation',source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),carrier_sha256=hashlib.sha256(open(n.__file__,'rb').read()).hexdigest())
    result.update(
        contract=dict(timeout_seconds=AUDIT_TIMEOUT_SEC,blas_threads=1,rss_limit_MiB=RSS_LIMIT_MIB),
        dependencies={AUDIT_INPUT_PATHS[0]:result['carrier_sha256']},
        native_counter_semantics='On-demand assertions inside imported branches/lift functions only; baseline main and its full census were not executed.',
        state_construction=dict(
            occupations_x0=[1,0,0,1],occupations_x1=[0,1,0,1],
            relative_phase='x1=T01*x0',
            coefficients=[-float(np.sin(np.pi/8)),float(np.cos(np.pi/8))],
            joint_embedding='sum_a Pi_a chi tensor |20-a>, with full system A=H_live+4 I',
            total_energy=20,particle_number=2,fuel_gap=1,battery_levels=[0,33],
            hopping_edges=[[0,1],[2,3]],head=0,
            rayleigh_expected=[[1,.5],[.5,0]],
            no_jump_time=t),
        conditional_energy_model=dict(
            input_A=h2.tolist(),output_A=g2.tolist(),directed_J=j2.tolist(),
            active_total_energy=10,dark_total_energy=20,mixture_weights=[.5,.5]),
    )
    if args.json:
        print(json.dumps(result,indent=2,allow_nan=False))
    else:
        print('NATIVE OCCUPATION FEEDBACK: square, opposite unit dimers, fuel gap1, retained battery0..33; no identity refusal')
        print('STATE '+json.dumps(result['state_construction']))
        print('DRIFT '+json.dumps(dict(actual_matrix=result['rayleigh_matrix'],negative_eigenvalue=negative,battery_rate_commutator=ebcomm)))
        print('NOJUMP '+json.dumps(dict(time=t,physical_matrix_exponential_matches_fiber=True,dark_survival=darkmass)))
        print('CONDITIONAL_ENERGY '+json.dumps(dict(model=result['conditional_energy_model'],observations=result['conditional_energy'])))
        print('PASS literal total-energy matrix intertwiners and every spectral-indicator GKSL adjoint; native N/old Records and post-hop bridge parity')
        print('MUTATIONS '+json.dumps(mutations))
        print(f'PASS new_assertions={checks} carrier_assertions={n.checks-native_start} worst={result["worst"]:.3e}')
        print('COUNTER_SCOPE '+result['native_counter_semantics'])
        print('per_element: checked native directed-edge effects and actual energy-shifted jump matrix entries on the finite ladder.')
        print('per_site: checked all four native occupation labels for the N2 witness and old physical edge Record persistence.')
        print('per_mode: checked commensurate sector spectra and every modeled total-energy spectral indicator on the finite battery.')
        print('per_block: checked initial and reachable bridge sectors, actual no-jump matrices, and separate correlated two-state energy filtering.')
        print('lattice_wide: checked and not executed -- this finite square witness does not compute the full cube or an infinite-lattice feedback law.')
        print('RESOURCES '+json.dumps(dict(seconds=result['seconds'],rss_MiB=rss,contract=result['contract'])))
        print('SOURCE_SHA256 '+result['source_sha256'])
        print('DEPENDENCIES '+json.dumps(result['dependencies']))
        print('SCOPE '+result['scope'])
    return 0

if __name__=='__main__':
    raise SystemExit(main())
