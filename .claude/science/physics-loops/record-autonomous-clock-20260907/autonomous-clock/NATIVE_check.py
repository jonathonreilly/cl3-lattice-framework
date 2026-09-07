import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np,scipy.sparse as sp
from scipy.linalg import expm
from scipy.sparse.linalg import expm_multiply
import runpy,io,contextlib,time,signal,resource,sys,json,math,hashlib
signal.alarm(180);start=time.monotonic()
with contextlib.redirect_stdout(io.StringIO()):native=runpy.run_path('/private/tmp/toe-autonomous-native-ladder-20260907/full-instrument/check.py')
I=native['Id'];q=native['q'];a=I-q;p=native['p'];word=native['word'];X=native['X'];Z=native['Z'];K=native['K'];W=native['W'];target=native['target'];dim=256
b=(I-word({3:Z}))/2;zm=(I-word({0:Z}))/2
C=lambda P,l:I-P+P@word({l:X})
bright=native['Hs'][0];dark=native['Hs'][1];head=native['Hs'][2]
U=[C(p@b,6),C(p@b,7),I-1j*bright-bright@bright,I-1j*dark-dark@dark,C(a,7),C(a@zm,6),C(a@zm,7),I-1j*head-head@head,I-2*a]+[I]*8
checks={}
def ck(x,y,label,tol=2e-11):
 assert label not in checks
 err=float(np.max(abs(np.asarray(x)-np.asarray(y)),initial=0));assert np.isfinite(err) and err<tol,(label,err);checks[label]=err
prefix=[W.astype(complex)]
for j,u in enumerate(U):
 ck(u.conj().T@u,I,f'gate{j+1} unitary');ck(K@u,u@K,f'gate{j+1} originalfree commutation');prefix.append(u@prefix[-1])
ck(prefix[9],target,'nine actual native gates all8 target columns')
L=17;g=np.pi/2;coupling=g*np.sqrt(np.arange(1,18)*np.arange(17,0,-1));hc=np.diag(coupling,1)+np.diag(coupling,-1)
ck(np.linalg.eigvalsh(hc),g*np.arange(-17,18,2),'spin spectrum');ck(np.linalg.norm(hc,2),17*g,'clock exact norm')
Hc=sp.csr_matrix((18*dim,18*dim),dtype=complex)
for j,u in enumerate(U):
 e=sp.csr_matrix(([coupling[j]],([j+1],[j])),shape=(18,18));piece=sp.kron(e,sp.csr_matrix(u),format='csr');Hc+=piece+piece.conj().T
free=sp.kron(sp.eye(18),sp.csr_matrix(K),format='csr');H=free+Hc
comm=free@Hc-Hc@free;ck(comm.data,0.,'literal joint original energy commutator')
G=sp.block_diag([sp.csr_matrix(w) for w in prefix],format='csr');kin=W.T@K@W;reduced=sp.kron(sp.eye(18),sp.csr_matrix(kin))+sp.kron(sp.csr_matrix(hc),sp.eye(8))
ck((H@G-G@reduced).toarray(),0.,'actual allcolumn gauge Hamiltonian intertwining')
initial=np.vstack([W]+[np.zeros_like(W)]*17).astype(complex);rows=[]
for t in (.99,1.,1.01,2.):
 amp=np.array([np.sqrt(math.comb(17,j))*np.cos(g*t)**(17-j)*(-1j*np.sin(g*t))**j for j in range(18)])
 ck(expm(-1j*t*hc)[:,0],amp,f't{t} independently exponentiated clock amplitudes')
 inputfree=expm(-1j*t*kin);expected=np.vstack([amp[j]*prefix[j]@inputfree for j in range(18)])
 actual=expm_multiply(-1j*t*H,initial);ck(actual,expected,f't{t} literal native clock evolution')
 ck(actual.conj().T@actual,np.eye(8),f't{t} allinput isometry')
 eta=float(np.sum(abs(amp[:9])**2));row=dict(t=t,unfinished_probability=eta)
 if t<1.1:
  completed=np.zeros(18,complex);completed[9:]=amp[9:]/np.sqrt(1-eta)
  comparison=np.vstack([completed[j]*target@inputfree for j in range(18)])
  overlap=actual.conj().T@comparison;ck(overlap,np.sqrt(1-eta)*np.eye(8),f't{t} readyinput reference overlap')
  row.update(retained_trace_norm_formula=2*np.sqrt(eta),system_only_bound=2*eta,mean_missing_steps=float(np.sum(np.arange(17,-1,-1)*abs(amp)**2)))
 if t==1.:ck(actual,np.vstack([np.zeros_like(W)]*17+[(-1j)**17*target@inputfree]),'peak terminal full native isometry')
 if t==2.:ck(actual,-np.vstack([W@inputfree]+[np.zeros_like(W)]*17),'recurrence original source with free phase')
 rows.append(row)
eta_bound=17*(22/7)**2/360000;assert eta_bound<1/2000 and 4*eta_bound<1/400
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert rss<180 and time.monotonic()-start<180
print(json.dumps(dict(checks=checks,rows=rows,clock_edges=17,clock_positions=18,native_dimension=dim,joint_dimension=18*dim,clock_norm=17*g,max_edge=float(max(coupling)),legal_total_norm_bound=17*g+5.5,natural_extension_sum_bound=float(sum(coupling)),window_eta_rational_bound=eta_bound,seconds=time.monotonic()-start,rss_MiB=rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest()),indent=2,allow_nan=False))
