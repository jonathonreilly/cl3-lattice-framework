import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np,json
from scipy.linalg import expm
I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);q=np.diag([0.,1.]);p=(I+Y)/2
swap=np.zeros((4,4));swap[1,2]=swap[2,1]=1
H1=np.kron(p,swap);H2=np.kron(np.kron(X,I-q),I)
K=np.kron(np.kron(I+Y,q),I)+2*np.kron(np.eye(4),q)
U1=np.eye(8)-1j*H1-H1@H1;U2=np.eye(8)+(np.cos(np.pi/4)-1)*H2@H2-1j*np.sin(np.pi/4)*H2
source=np.kron(np.kron(np.array([1,1j])/np.sqrt(2),np.array([0,1])),np.array([1,0]));after1=-1j*np.kron(np.kron(np.array([1,1j])/np.sqrt(2),np.array([1,0])),np.array([0,1]));after2=-1j*np.eye(8)[:,1]
checks={}
def ck(a,b,name):
 err=float(np.max(abs(a-b)));assert err<1e-12,(name,err);checks[name]=err
ck(H1@K,K@H1,'H1 full energy');ck(H2@K,K@H2,'H2 full energy');ck(H1@H1@H1,H1,'H1 cubic');ck(H2@H2,np.kron(np.kron(I,I-q),I),'H2 square');ck(U1,expm(-1j*np.pi*H1/2),'U1 physical exponential');ck(U2,expm(-1j*np.pi*H2/4),'U2 physical exponential');ck(U1.conj().T@U1,np.eye(8),'U1 unitary');ck(U2.conj().T@U2,np.eye(8),'U2 unitary');ck(U1@source,after1,'first exact state');ck(U2@U1@source,after2,'second exact state')
U3=expm(-1j*np.pi*swap/2);U4=expm(-1j*np.pi*np.kron(I,X)/2)
ck(U3@np.eye(4)[:,2],-1j*np.eye(4)[:,1],'head state');ck(U4@np.eye(4)[:,0],-1j*np.eye(4)[:,1],'label state')
final=np.kron(np.kron(U2@U1@source,U3@np.eye(4)[:,2]),U4@np.eye(4)[:,0]);target=np.kron(np.kron(np.eye(8)[:,1],np.eye(4)[:,1]),np.eye(4)[:,1]);ck(final,1j*target,'final coherent phase')
bad=np.kron(I,swap);defect=float(np.linalg.norm(bad@K-K@bad,2));assert defect==2
print(json.dumps({'checks':checks,'uncontrolled_exchange_energy_defect':defect,'final_phase':'i','largest_exponentiated_matrix_dimension':8,'scope':'Factorized exact pulse check; r and b0 spectators unchanged, no full 512-state simulation'},indent=2))
