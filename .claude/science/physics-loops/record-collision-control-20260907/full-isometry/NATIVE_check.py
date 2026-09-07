import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import expm
import time,resource,signal,sys,json,hashlib
import native_edge_record_autonomous_head_native_ladder_check_2026_09_07 as native
signal.alarm(180);start=time.monotonic()
# Actual boundary compression supplies the three reduced Pauli operators.
E=np.eye(16)[:,[4,12]];X=E.T@native.A(0,1)@E;Y=E.T@native.HOPS[0]@E;Z=E.T@native.Z[0]@E;I=np.eye(2)
DIM=256;Id=np.eye(DIM);checks={}
def ck(a,b,label):
 assert label not in checks
 err=float(np.max(abs(np.asarray(a)-np.asarray(b)),initial=0));assert np.isfinite(err) and err<3e-12,(label,err);checks[label]=err
# Order x,f,b0,b1,hv,hw,l0,l1; old r0 fixed and omitted.
def word(ops):
 out=np.ones((1,1))
 for i in range(8):out=np.kron(out,ops.get(i,I))
 return out
q=(Id-word({1:Z}))/2;q0=Id-q;p=(Id+word({0:Y}))/2;pm=Id-p
K=q@(Id+word({0:Y}))+.5*Id+(Id-word({2:Z}))/2+2*(Id-word({3:Z}))/2
Nhead=(Id-word({4:Z}))/2+(Id-word({5:Z}))/2
swapfb=(word({1:X,3:X})+word({1:Y,3:Y}))/2
swaph=(word({4:X,5:X})+word({4:Y,5:Y}))/2
Hs=[p@swapfb,pm@word({1:X}),q0@swaph,q0@(Id+word({0:Z}))/2@word({7:X}),q0@(Id-word({0:Z}))/2@word({6:X}),q@word({6:X}),q@word({7:X}),Id+q]
maxsupports=[3,2,3,3,3,2,2,1]
# Eight input columns use x computational basis, battery numeric order0..3.
def embedding(f,hv,hw,l0,l1):
 out=np.zeros((DIM,8))
 for x in range(2):
  for b in range(4):
   bits=[x,f,b%2,b//2,hv,hw,l0,l1];idx=sum(bit*2**(7-j) for j,bit in enumerate(bits));out[idx,4*x+b]=1
 return out
W=embedding(1,1,0,0,0);Wp=embedding(0,0,1,0,1);Wm=embedding(0,0,1,1,0);Wr=embedding(1,1,0,1,1)
T2=np.zeros((4,4));T2[2,0]=T2[3,1]=1
py=(I+Y)/2;my=(I-Y)/2;Pplus=(I+Z)/2;Pminus=(I-Z)/2
Sp=np.kron(Pplus@py,T2)+np.kron(Pplus@my,np.eye(4));Sm=np.kron(Pminus@py,T2)+np.kron(Pminus@my,np.eye(4));F=np.kron(py,np.diag([0,0,1,1]))
target=Wp@Sp+Wm@Sm+Wr@F
ck(Sp.conj().T@Sp+Sm.conj().T@Sm+F.conj().T@F,np.eye(8),'native combined completion')
ck(target.conj().T@target,np.eye(8),'target isometry');ck(K@target,target@(W.T@K@W),'all target energy columns')
ck(word({0:Z})@Wp@Sp,Wp@Sp,'accepted plus native Record');ck(word({0:Z})@Wm@Sm,-Wm@Sm,'accepted minus native Record')
state=W.astype(complex);pulse_rows=[]
for j,H in enumerate(Hs,1):
 ck(H,H.conj().T,f'pulse{j} hermitian');ck(K@H,H@K,f'pulse{j} global energy');ck(Nhead@H,H@Nhead,f'pulse{j} head number')
 U=expm(-1j*np.pi*H/2);ck(U.conj().T@U,Id,f'pulse{j} unitary')
 if j<8:
  ck(H@H@H,H,f'pulse{j} cubic');polynomial=Id-1j*H-H@H;ck(U,polynomial,f'pulse{j} actual exponential')
 else:ck(U,-1j*q0-q,'final fixed phase')
 state=U@state;ck(K@state,state@(W.T@K@W),f'pulse{j} all occupied energy columns')
 pulse_rows.append(dict(pulse=j,max_pauli_support=maxsupports[j-1]))
ck(state,target,'all8 complex target columns exact phase')
# Load-bearing distinction from independently frozen single target result.
refusal_rank=int(np.linalg.matrix_rank(F));ck(refusal_rank,2,'two refused bright upper-cell modes')
resource_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert resource_rss<180 and time.monotonic()-start<180
print(json.dumps(dict(checks=checks,pulses=pulse_rows,all_column_max_error=float(np.max(abs(state-target))),input_columns=8,refusal_rank=refusal_rank,zero_energy_label_qubits=2,additional_ancillas=0,matrix_dimension=DIM,seconds=time.monotonic()-start,rss_MiB=resource_rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),scope='Full source-column native isometry under supplied globally conserving support<=3 completegraph pulses; fixed old boundary Record sector, no NN or permanent formation claim'),indent=2,allow_nan=False))
