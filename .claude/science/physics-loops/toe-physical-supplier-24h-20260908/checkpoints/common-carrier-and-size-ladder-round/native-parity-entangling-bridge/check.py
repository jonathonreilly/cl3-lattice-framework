import os,time,json,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS']:os.environ[k]='1'
import numpy as np
from functools import reduce
p=Path(__file__).resolve().parent;I=np.eye(8,dtype=complex);z=np.diag([1,-1]);x=np.array([[0,1],[1,0]]);edges=[(0,1),(1,2),(2,3)]
def local(a,k):return reduce(np.kron,[a if j==k else np.eye(2) for j in range(3)])
Z=[local(z,k) for k in range(3)];B=[reduce(np.matmul,[Z[k] for k,e in enumerate(edges) if v in e],I) for v in range(4)];n=[(I-b)/2 for b in B];T=[]
for k,(i,j) in enumerate(edges):
 a=local(x,k)
 for v,w in ((i,j),(j,i)):
  for q,e in enumerate(edges):
   if q!=k and v in e and (e[1] if e[0]==v else e[0])<w:a=a@Z[q]
 T.append(1j*a@(B[i]-B[j])/2)
def pulse(k,c,s):return I+(c-1)*(T[k]@T[k])-1j*s*T[k]
def basis(occ):
 ids=[j for j in range(8) if all(abs(n[v][j,j]-occ[v])<1e-12 for v in range(4))]
 if len(ids)!=1:raise AssertionError('physical occupation')
 return np.eye(8)[:,ids[0]]
checks={}
def ck(k,v):
 if not bool(v):raise AssertionError(k)
 checks[k]=True
def eq(a,b):return np.max(abs(a-b))<1e-11
# Two logical input rails: ordering00,01,10,11 by mode occupation.
Vin=np.column_stack([basis([int(a==0),int(b==0),int(a==1),int(b==1)]) for a in (0,1) for b in (0,1)])
Vout=np.column_stack([basis([int(a==0),int(a==1),int(b==0),int(b==1)]) for a in (0,1) for b in (0,1)])
Q=(I-Z[1])/2;F=(I+Z[1])/2;K=Vout.conj().T@Q@Vin
ck('fullsuccesscolumns',eq(Q@Vin,Vout@K));ck('completeinstrument',eq(Vin.conj().T@(Q+F)@Vin,np.eye(4)))
ck('oddparityprojector',eq(K.conj().T@K,np.diag([0,1,1,0])))
ck('surviving_local_readout',eq(T[0]@Z[1],Z[1]@T[0]) and eq(T[2]@Z[1],Z[1]@T[2]))
# Actual prep from occupation01 by conjugated adjacent rotations. Cross-mode rotations implemented before recording.
S=pulse(1,0,1);c=1/np.sqrt(2)
G02=S@pulse(0,c,c)@S.conj().T;G13=S.conj().T@pulse(2,c,c)@S
ck('independent_input_rotations',eq(G02@G13,G13@G02))
ck('input_rotations_preserve_each_rail_number',eq((n[0]+n[2])@G13,G13@(n[0]+n[2])) and eq((n[1]+n[3])@G02,G02@(n[1]+n[3])))
psi=G13@G02@basis([1,1,0,0]);inp=Vin.conj().T@psi
ck('prep_stays_inputdomain',eq(Vin@inp,psi))
# Physical occupation basis has a nontrivial CAR sign convention: calibrate tensor-factor phases independently below.
post=Q@psi;prob=float(np.vdot(post,post).real);out=Vout.conj().T@post/np.sqrt(prob)
ck('success_half',abs(prob-.5)<1e-11);ck('output_Bell_concurrence',abs(2*abs(out[0]*out[3]-out[1]*out[2])-1)<1e-11)
read=T[0]@T[2];coherent=float(np.vdot(post,read@post).real/prob);deph=sum(abs(out[j])**2*float(np.vdot(Vout[:,j],read@Vout[:,j]).real) for j in range(4))
ck('readable_coherence',abs(coherent-deph)>.9)
Rread=pulse(2,c,c)@pulse(0,c,c);obs=Rread.conj().T@Z[0]@Z[2]@Rread
operational=float(np.vdot(post,obs@post).real/prob)
classical=sum(abs(out[j])**2*float(np.vdot(Vout[:,j],obs@Vout[:,j]).real) for j in range(4))
ck('operational_hop_then_Z_readout',abs(operational-classical)>.9)
ck('readout_preserves_cut',eq(Rread@Z[1],Z[1]@Rread))
ck('forbidden_bridge_reuse',not eq(T[1]@Z[1],Z[1]@T[1]))
ck('permanent_both_outcomes',eq(Z[1]@post,-post) and eq(Z[1]@F@psi,F@psi))
outdata={'checks':checks,'input_amplitudes':inp.real.tolist(),'output_amplitudes':out.real.tolist(),'K_real':K.real.tolist(),'probability':prob,'surviving_T01T23':coherent,'dephased_readout':deph,'operational_rotated_Z_correlation':operational,'operational_dephased_correlation':classical,'source_sha':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(p/'RESULT.json').write_text(json.dumps(outdata,indent=2)+'\n');print(outdata)
