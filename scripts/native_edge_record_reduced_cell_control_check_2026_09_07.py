#!/usr/bin/env python3
"""Independent reduced native-cell boundary and coherent control checks."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.linalg import expm
import native_edge_record_autonomous_head_native_ladder_check_2026_09_07 as n
import argparse,json,time,resource,signal,sys,hashlib
from pathlib import Path
AUDIT_INPUT_PATHS=('scripts/native_edge_record_autonomous_head_native_ladder_check_2026_09_07.py',)

def parent_boundary():
 E=np.eye(16)[:,[4,12]];X=np.array([[0,1],[1,0]]);Z=np.diag([1,-1]);Y=np.array([[0,-1j],[1j,0]])
 tests={'B0':(E.T@n.B[0]@E,Z),'B1':(E.T@n.B[1]@E,-Z),'A01':(E.T@n.A(0,1)@E,X),'h01':(E.T@n.HOPS[0]@E,Y),'total_N':(E.T@n.N@E,2*np.eye(2)),'old12':(n.Z[1]@E,-E),'old23':(n.Z[2]@E,E),'old03':(n.Z[3]@E,E)}
 res={k:float(np.max(abs(a-b))) for k,(a,b) in tests.items()};assert max(res.values())<1e-12
 source=('11000','11011');accepted=('00101','00110');dist={a+'->'+b:sum(x!=y for x,y in zip(a,b)) for a in source for b in accepted};assert min(dist.values())==4
 return {'native_parent_residuals':res,'bit_order':'f,hv,hw,l0,l1','cross_distances':dist}

def three_site():
 I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);q=np.diag([0.,1.]);p=(I+Y)/2
 swap=np.zeros((4,4));swap[1,2]=swap[2,1]=1
 H1=np.kron(p,swap);H2=np.kron(np.kron(X,I-q),I)
 K=np.kron(np.kron(I+Y,q),I)+2*np.kron(np.eye(4),q)
 U1=np.eye(8)-1j*H1-H1@H1;U2=np.eye(8)+(np.cos(np.pi/4)-1)*H2@H2-1j*np.sin(np.pi/4)*H2
 source=np.kron(np.kron(np.array([1,1j])/np.sqrt(2),np.array([0,1])),np.array([1,0]));after1=-1j*np.kron(np.kron(np.array([1,1j])/np.sqrt(2),np.array([1,0])),np.array([0,1]));after2=-1j*np.eye(8)[:,1]
 checks={}
 def ck(a,b,name):
  err=float(np.max(abs(a-b)));assert np.isfinite(err) and err<1e-12,(name,err);checks[name]=err
 ck(H1@K,K@H1,'H1 full energy');ck(H2@K,K@H2,'H2 full energy');ck(H1@H1@H1,H1,'H1 cubic');ck(H2@H2,np.kron(np.kron(I,I-q),I),'H2 square');ck(U1,expm(-1j*np.pi*H1/2),'U1 physical exponential');ck(U2,expm(-1j*np.pi*H2/4),'U2 physical exponential');ck(U1.conj().T@U1,np.eye(8),'U1 unitary');ck(U2.conj().T@U2,np.eye(8),'U2 unitary');ck(U1@source,after1,'first exact state');ck(U2@U1@source,after2,'second exact state')
 U3=expm(-1j*np.pi*swap/2);U4=expm(-1j*np.pi*np.kron(I,X)/2)
 ck(U3@np.eye(4)[:,2],-1j*np.eye(4)[:,1],'head state');ck(U4@np.eye(4)[:,0],-1j*np.eye(4)[:,1],'label state')
 final=np.kron(np.kron(U2@U1@source,U3@np.eye(4)[:,2]),U4@np.eye(4)[:,0]);target=np.kron(np.kron(np.eye(8)[:,1],np.eye(4)[:,1]),np.eye(4)[:,1]);ck(final,1j*target,'final coherent phase')
 bad=np.kron(I,swap);defect=float(np.linalg.norm(bad@K-K@bad,2));assert defect==2
 return {'checks':checks,'uncontrolled_exchange_energy_defect':defect,'final_phase':'i','largest_exponentiated_matrix_dimension':8,'scope':'Factorized exact pulse check; r and b0 spectators unchanged, no full 512-state simulation'}

def state_specific():
 I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1.]);q=(I-Z)/2
 # Active order x,f,b1, then head(hv,hw), then label(l0,l1).
 # Fixed r=0 and b0=0 are unchanged tensor factors, not simulated qubits.
 k8=np.kron(np.kron(I+Y,q),I)+2*np.kron(np.eye(4),q)+.5*np.eye(8)
 h1=(np.kron(np.kron(Z,I),X)-np.kron(np.kron(X,I),Y))/2
 h2=np.kron(np.kron((I-Y)/2,X),I)
 h3=np.kron(np.kron(X,I-q),I)
 swap=np.zeros((4,4));swap[1,2]=swap[2,1]=1
 hs=[np.kron(h,np.eye(16)) for h in (h1,h2,h3)]+[np.kron(np.kron(np.eye(8),swap),np.eye(4)),np.kron(np.eye(32),np.kron(I,X))]
 K=np.kron(k8,np.eye(16));headN=np.kron(np.kron(np.eye(8),np.kron(q,I)+np.kron(I,q)),np.eye(4))
 source=np.kron(np.kron(np.kron(np.kron(np.array([1,1j])/np.sqrt(2),np.array([0,1])),np.array([1,0])),np.eye(4)[:,2]),np.eye(4)[:,0])
 target=np.kron(np.kron(np.eye(8)[:,1],np.eye(4)[:,1]),np.eye(4)[:,1])
 times=[np.pi/2,np.pi/2,-np.pi/4,np.pi/2,np.pi/2];checks={};rows=[];psi=source
 def ck(a,b,label):
  assert label not in checks,('duplicate check',label)
  e=float(np.max(abs(np.asarray(a)-np.asarray(b)),initial=0));assert np.isfinite(e) and e<2e-12,(label,e);checks[label]=e
 for j,(H,t) in enumerate(zip(hs,times),1):
  ck(H@H@H,H,f'pulse{j} cubic');ck(H@headN,headN@H,f'pulse{j} head number')
  comm=float(np.linalg.norm(H@K-K@H,2))
  if j==1:ck(comm,2.,'first globally noncommuting energy control')
  else:ck(comm,0.,f'pulse{j} global energy')
  # Independent full cyclic-span projector from psi,Hpsi,H²psi.
  U,s,_=np.linalg.svd(np.column_stack([psi,H@psi,H@H@psi]),full_matrices=False);basis=U[:,s>1e-11];P=basis@basis.conj().T
  ck(K@basis,2.5*basis,f'pulse{j} entire cyclic span energy')
  ck(H@basis,P@H@basis,f'pulse{j} cyclic span invariant')
  for m in range(9):
   theta=t*m/8;unitary=np.eye(128)-1j*np.sin(theta)*H+(np.cos(theta)-1)*H@H
   state=unitary@psi
   ck(np.linalg.norm(state),1.,f'pulse{j} sample{m} norm');ck(K@state,2.5*state,f'pulse{j} sample{m} energy support');ck(headN@state,state,f'pulse{j} sample{m} one head')
  exact=expm(-1j*t*H);ck(exact.conj().T@exact,np.eye(128),f'pulse{j} actual unitary');ck(exact@psi,state,f'pulse{j} actual exponential')
  psi=state;rows.append(dict(pulse=j,cyclic_dimension=basis.shape[1],global_energy_commutator_norm=comm))
 ck(psi,target,'final phase +1 target')
 return dict(checks=checks,pulses=rows,final_phase='+1',matrix_dimension=128,folded_fixed_spectators=['r=0','b0=0'],scope='Fixed-input cyclic energy preservation; first pulse is NOT a globally energy-commuting control and does not contradict the two-site invariant.')

def main():
 signal.alarm(180);start=time.monotonic()
 result=dict(parent_boundary=parent_boundary(),globally_commuting_three_site=three_site(),state_specific_two_site=state_specific())
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-start
 if rss>=180 or elapsed>=180:raise AssertionError(('resources',rss,elapsed))
 result.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={AUDIT_INPUT_PATHS[0]:hashlib.sha256(Path(n.__file__).read_bytes()).hexdigest()},seconds=elapsed,rss_MiB=rss,resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1))
 return result

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--json',action='store_true');args=parser.parse_args();result=main()
 if args.json:print(json.dumps(result,indent=2,allow_nan=False))
 else:
  print('PASS independent reduced native-cell boundary and coherent control checks')
  print('RESULT '+json.dumps(result,sort_keys=True,allow_nan=False))
  print('per_element: actual parent boundary Pauli identities, exact pulse exponentials and cyclic projectors are checked.')
  print('per_site: fixed square boundary reduction and unchanged old Record; complete interaction graph only.')
  print('per_mode: three-site global energy commutation versus two-site fixed-input energy support are distinguished.')
  print('per_block: each occupied cyclic subspace is invariant at energy5/2; first two-site pulse globally fails energy commutation.')
  print('lattice_wide: checked and not executed -- no full instrument, native nearest-neighbor synthesis, permanent new Record or all48-qubit simulation.')
  print('SOURCE_SHA256 '+result['source_sha256']);print('DEPENDENCIES '+json.dumps(result['dependencies'],sort_keys=True));print('TOTAL: PASS FAIL=0')
