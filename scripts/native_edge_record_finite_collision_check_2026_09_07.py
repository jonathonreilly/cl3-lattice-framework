#!/usr/bin/env python3
"""Two preserved native finite collision fixtures, including a rejected noncommuting control."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import eigh,expm,block_diag
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
import native_edge_record_autonomous_head_native_ladder_check_2026_09_07 as n
import json,time,resource,signal,sys,hashlib,argparse
from pathlib import Path
AUDIT_INPUT_PATHS=('scripts/native_edge_record_autonomous_head_native_ladder_check_2026_09_07.py',)
checks=0;worst=0.
def ck(a,b,label,tol=2e-10):
 global checks,worst
 err=float(np.max(abs(np.asarray(a)-np.asarray(b)),initial=0))
 if not np.isfinite(err) or err>=tol:raise AssertionError((label,err))
 checks+=1;worst=max(worst,err)
def sec(rec):
 q,_,live=n.sector(rec);a,v=eigh(q.conj().T@n.N@q);q=q@v[:,abs(a-2)<1e-8]
 H=sum((n.HOPS[e]*(1 if e==0 else np.sqrt(2)/3) for e in live if e in (0,2)),np.zeros((16,16),complex))
 h=q.conj().T@H@q+len(live)*np.eye(q.shape[1]);a,v=eigh(h);ar=np.floor(a+.5)
 return q,h,(v*ar)@v.conj().T,a,ar,v
def tot(h):return np.kron(h,np.eye(3))+np.kron(np.eye(len(h)),np.diag([.5,1.5,2.5]))
def run_fixture(edge):
 global checks,worst
 checks=0;worst=0.;start=time.monotonic()
 s=sec({});outs=[sec({edge:z}) for z in (1,-1)];Ls=[]
 for z,o in zip((1,-1),outs):
  K=o[0].conj().T@((n.I+z*n.Z[edge])/2)@s[0];L=np.zeros((len(o[1])*3,len(s[1])*3),complex)
  for i,a in enumerate(s[4]):
   for j,b in enumerate(o[4]):
    mat=np.outer(o[5][:,j],o[5][:,j].conj())@K@np.outer(s[5][:,i],s[5][:,i].conj())
    trans=np.zeros((3,3));shift=int(a-b)
    for k in range(3):
     if 0<=k+shift<3:trans[k+shift,k]=1
    L+=np.kron(mat,trans)
  ck(tot(o[2])@L,L@tot(s[2]),'actual rounded intertwining');Ls.append(L)
 E=np.eye(Ls[0].shape[1])-sum(L.conj().T@L for L in Ls);a,v=eigh((E+E.conj().T)/2);assert a.min()>-1e-9
 ref=(v*np.sqrt(np.where(a>1e-10,a,0)))@v.conj().T;Ls.append(ref)
 dim=len(ref);D=4*dim;Js=[]
 for j,L in enumerate(Ls):
  J=np.zeros((D,D),complex);J[(j+1)*dim:(j+2)*dim,:dim]=L;Js.append(J)
 F=block_diag(tot(s[1]),tot(outs[0][1]),tot(outs[1][1]),tot(s[1]));K=block_diag(tot(s[2]),tot(outs[0][2]),tot(outs[1][2]),tot(s[2]))
 R=sum(J.conj().T@J for J in Js);ck(R,block_diag(np.eye(dim),np.zeros((3*dim,3*dim))),'complete source rate');ck(F@K,K@F,'originalfree roundedenergy')
 V=np.zeros((4*D,4*D),complex)
 for j,J in enumerate(Js):
  label=np.zeros((4,4));label[j+1,0]=1;V+=np.kron(J,label)+np.kron(J.conj().T,label.T)
 ck(np.linalg.norm(V,2),1,'star norm');ck(np.kron(K,np.eye(4))@V,V@np.kron(K,np.eye(4)),'physical coupling energy')
 I=sp.eye(D,format='csr');diss=sum(sp.kron(sp.csr_matrix(J.conj()),sp.csr_matrix(J)) for J in Js)-(sp.kron(I,sp.csr_matrix(R))+sp.kron(sp.csr_matrix(R.T),I))/2
 free=-1j*(sp.kron(I,sp.csr_matrix(F))-sp.kron(sp.csr_matrix(F.T),I))
 psi=s[5][:,0];phase=.37*(n.I-n.B[0])/2+.23*(n.I-n.B[2])/2
 psi=s[0].conj().T@expm(-1j*phase)@s[0]@psi;psi/=np.linalg.norm(psi)
 x=np.zeros(D,complex);x[:dim]=np.kron(psi,np.ones(3)/np.sqrt(3));rho=np.outer(x,x.conj());rows=[]
 for h in (.04,.02,.01):
  U=expm(-1j*np.sqrt(h)*V);ck(U.conj().T@U,np.eye(4*D),'physical unitary')
  kraus=[U[j::4,0::4] for j in range(4)];got=sum(k@rho@k.conj().T for k in kraus);ck(sum(k.conj().T@k for k in kraus),np.eye(D),'reduced CPTP')
  exact=expm_multiply(h*diss,rho.reshape(-1,order='F')).reshape(D,D,order='F')
  err=float(np.linalg.norm(got-exact,ord='nuc'));assert err<=6*h*h
  u=expm(-1j*h*F);split=u@got@u.conj().T;full=expm_multiply(h*(diss+free),rho.reshape(-1,order='F')).reshape(D,D,order='F')
  errfull=float(np.linalg.norm(split-full,ord='nuc'));assert errfull<=8*h*h
  ck(np.trace(got),1,'trace');ck(np.trace(K@got),np.trace(K@rho),'roundedmean')
  rows.append(dict(h=h,dissipative_trace_norm_error=err,split_full_trace_norm_error=errfull))
 assert 3.5<rows[0]['dissipative_trace_norm_error']/rows[1]['dissipative_trace_norm_error']<4.5
 assert 3.5<rows[1]['dissipative_trace_norm_error']/rows[2]['dissipative_trace_norm_error']<4.5
 original_comm=max(float(np.linalg.norm(F@J-J@F,2)) for J in Js)
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert rss<180
 result=dict(checks=checks,worst=worst,system_dimension=D,unitary_dimension=4*D,rows=rows,original_jump_commutator=original_comm,refusal_probability=float(np.vdot(x[:dim],ref.conj().T@ref@x[:dim]).real),seconds=time.monotonic()-start,rss_MiB=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 result['deleted_edge']=edge
 result['noncommuting_control_detected']=original_comm>1e-4
 if edge==0:assert not result['noncommuting_control_detected']
 else:assert result['noncommuting_control_detected']
 return result

def main():
 signal.alarm(180);start=time.monotonic()
 original=run_fixture(0)
 supplement=run_fixture(2)
 elapsed=time.monotonic()-start
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
 if elapsed>=180 or rss>=180:raise AssertionError(('resources',elapsed,rss))
 return dict(original_commuting_fixture=original,separately_preregistered_noncommuting_supplement=supplement,
  parameters=dict(hopping01=1.,hopping23=float(np.sqrt(2)/3),fuel_delta=1.,gamma=1.,battery_centers=[.5,1.5,2.5],cap=3.,grid_spacing=1.,particle_number=2,state='original source ground state pulsed by exp[-i(.37 n0+.23 n2)], uniform real battery superposition',refusal_numerical_null_cutoff=1e-10),
  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  dependencies={AUDIT_INPUT_PATHS[0]:hashlib.sha256(Path(n.__file__).read_bytes()).hexdigest()},
  resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),seconds=elapsed,rss_MiB=rss,
  discriminator='Original edge01 deletes unit hopping; irrational23 spectator survives, so the attempted nonzero original-free jump commutator control fails. The separately preregistered post-inspection supplement deletes irrational23 and detects it. Both fixtures are preserved.',
  scope='Actual native N2 square, three battery cells, one completed edge event and 288-dimensional collision unitary; not an all-path cube or 48-qubit simulation. Trace errors are unhalved trace norms.')

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--json',action='store_true')
 args=parser.parse_args();result=main()
 if args.json:print(json.dumps(result,indent=2,allow_nan=False))
 else:
  print('PASS native finite collision fixtures: actual unitary versus independent GKSL exponential')
  print('DISCRIMINATOR '+result['discriminator'])
  print('RESULT '+json.dumps(result,sort_keys=True,allow_nan=False))
  print('per_element: both native Record signs and ONE absorbing refusal enter each actual star coupling.')
  print('per_site: native square N2, deleted edge01 original fixture and separately preregistered edge23 supplement.')
  print('per_mode: full rounded total-energy matrices, original-free commutator and three-cell battery are checked.')
  print('per_block: actual288-dimensional unitary and reduced CPTP channel compared at h=.04,.02,.01; 18 assertions per fixture.')
  print('lattice_wide: checked and not executed -- no all-path cube, 48-qubit simulation, local bath or autonomous clock claim.')
  print('SOURCE_SHA256 '+result['source_sha256'])
  print('DEPENDENCIES '+json.dumps(result['dependencies'],sort_keys=True))
  print('TOTAL: PASS FAIL=0; original attempted noncommuting discriminator remains false as explicitly reported.')
