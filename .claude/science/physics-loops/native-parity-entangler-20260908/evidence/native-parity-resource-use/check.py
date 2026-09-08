import numpy as np,json,hashlib
from functools import reduce
from pathlib import Path
I=np.eye(8,dtype=complex);z=np.diag([1,-1]);x=np.array([[0,1],[1,0]]);edges=[(0,1),(1,2),(2,3)]
def site(a,k):return reduce(np.kron,[a if j==k else np.eye(2) for j in range(3)])
Z=[site(z,k) for k in range(3)];B=[reduce(np.matmul,[Z[k] for k,e in enumerate(edges) if v in e],I) for v in range(4)];T=[]
for k,(i,j) in enumerate(edges):
 A=site(x,k)
 for v,w in ((i,j),(j,i)):
  for q,e in enumerate(edges):
   if q!=k and v in e and (e[1] if e[0]==v else e[0])<w:A=A@Z[q]
 T.append(1j*A@(B[i]-B[j])/2)
def gate(k,t):return I+(np.cos(t)-1)*(T[k]@T[k])-1j*np.sin(t)*T[k]
def obs(k,t):
 U=gate(k,t);return U.conj().T@Z[k]@U
# Actual frozen native Bell: outer bits00 and11, middle recorded1.
psi=(np.eye(8)[:,2]+np.eye(8)[:,7])/np.sqrt(2)
# Check actual ready output n0+n1=n2+n3=1 and permanent middle sign.
if np.max(abs(Z[1]@psi+psi))>1e-12:raise AssertionError('middle record')
A=[obs(0,0),obs(0,np.pi/4)];BB=[obs(2,np.pi/8),obs(2,-np.pi/8)]
cor=np.array([[np.vdot(psi,a@b@psi).real for b in BB] for a in A]);vals=[]
for signs in [(1,1,1,-1),(1,1,-1,1)]:vals.append(float(np.sum(cor*np.array(signs).reshape(2,2))))
if abs(max(abs(v) for v in vals)-2*np.sqrt(2))>1e-11:raise AssertionError('CHSH settings')
for a in A:
 for b in BB:
  if np.max(abs(a@b-b@a))>1e-12:raise AssertionError('local commute')
  if np.max(abs(a@Z[1]-Z[1]@a))>1e-12 or np.max(abs(b@Z[1]-Z[1]@b))>1e-12:raise AssertionError('permanence')
  if abs(np.vdot(psi,a@psi))>1e-12 or abs(np.vdot(psi,b@psi))>1e-12:raise AssertionError('unbiased marginals')
r={'correlations':cor.tolist(),'CHSH_two_sign_choices':vals,'scope':'Actual local hop rotations and terminalZ, heralded Bell resource; setting/readout schedule supplied','source_sha':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};Path(__file__).with_name('RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
