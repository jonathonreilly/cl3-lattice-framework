import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np,scipy.sparse as s,json,hashlib
from pathlib import Path
I=s.eye(512,format='csr');pa={'I':np.eye(2),'X':np.array([[0,1],[1,0]]),'Y':np.array([[0,-1j],[1j,0]]),'Z':np.diag([1,-1])}
def op(i,a):
 out=s.csr_matrix([[1.]])
 for j in range(9):out=s.kron(out,pa[a if j==i else 'I'],format='csr')
 return out
X=[op(i,'X') for i in range(9)];Y=[op(i,'Y') for i in range(9)];Z=[op(i,'Z') for i in range(9)];n=[(I-z)/2 for z in Z]
K=n[4]@(I+Y[3])+I/2+n[5]+2*n[6]
H=[(Z[3]@X[6]-X[3]@Y[6])/2,X[4]@(I-Y[3])/2,(I-n[4])@X[3],(X[1]@X[2]+Y[1]@Y[2])/2,X[8]]
times=[np.pi/2,np.pi/2,-np.pi/4,np.pi/2,np.pi/2]
def ket(parts):
 out=np.array([1.+0j])
 for p in parts:out=np.kron(out,p)
 return out
z0=np.array([1,0]);z1=np.array([0,1]);yp=np.array([1,1j])/np.sqrt(2)
psi=ket([z0,z1,z0,yp,z1,z0,z0,z0,z0]);target=ket([z0,z0,z1,z0,z0,z0,z1,z0,z1])
rows=[];comms=[];worst=0
for j,(h,t) in enumerate(zip(H,times)):
 poly=h@h@h-h;assert np.max(abs(poly.data),initial=0)<1e-13
 comm=h@K-K@h;comms.append(float(np.sqrt(sum(abs(comm.data)**2))))
 # Exact occupied Krylov subspace is span psi,Hpsi,H²psi by H³=H.
 for vec in [psi,h@psi,h@(h@psi)]:
  assert np.linalg.norm(K@vec-2.5*vec)<1e-12
 for fraction in np.linspace(0,1,9):
  u=fraction*t;v=psi-1j*np.sin(u)*(h@psi)+(np.cos(u)-1)*(h@(h@psi))
  residual=float(np.linalg.norm(K@v-2.5*v));worst=max(worst,residual)
  assert residual<1e-12 and abs(np.vdot(v,v)-1)<1e-12
  assert np.linalg.norm(Z[0]@v-v)<1e-12 and np.linalg.norm((n[1]+n[2])@v-v)<1e-12
  rows.append(dict(pulse=j+1,fraction=float(fraction),energy_mean=float(np.vdot(v,K@v).real),energy_variance=float(np.linalg.norm(K@v-2.5*v)**2),energy_distribution={'2.5':float(np.vdot(v,v).real)},eigenstate_residual=residual))
 psi=v
assert comms[0]>1 and max(comms[1:])<1e-12
assert np.linalg.norm(psi-target)<1e-12
print(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),global_commutator_frobenius=comms,final_target_error=float(np.linalg.norm(psi-target)),worst_energy_eigenstate_residual=worst,rows=rows),indent=2,allow_nan=False))
