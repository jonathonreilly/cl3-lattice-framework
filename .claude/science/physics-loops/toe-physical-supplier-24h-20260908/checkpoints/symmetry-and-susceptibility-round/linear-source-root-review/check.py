import os,sys,itertools,json,time,signal,hashlib
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
sys.path[:0]=['/private/tmp/toe-24h-probes-20260908/infrared-discriminator/linear-source','/private/tmp/toe-24h-probes-20260908/detuned-energy-moment','/private/tmp/toe-physical-supplier-24h-20260908/scripts']
os.environ['NUMBA_CACHE_DIR']='/private/tmp/toe-24h-probes-20260908/linear-source-root-review/numba-cache'
import numpy as np
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import eigsh
import population_kernel as k
signal.alarm(180);start=time.monotonic();L=2;coords=list(itertools.product(range(L),repeat=3));index=lambda r,a:3*((r[0]%L)*L*L+(r[1]%L)*L+r[2]%L)+a
faces=[]
for r in coords:
 for a,b in ((0,1),(0,2),(1,2)):
  x=list(r);x[a]+=1;y=list(r);y[b]+=1
  faces.append([index(r,a),index(x,b),index(y,a),index(r,b)])
coeff=np.zeros(24)
for r in coords:coeff[index(r,1)]=(-1)**(sum(r)+r[0])/np.sqrt(8)
raw=np.load('/private/tmp/toe-24h-probes-20260908/energy-source-structure/raw.npz');codes=[int(x) for x in raw['states']];lookup={x:j for j,x in enumerate(codes)};F=[];counts=[];rows=[];cols=[];controls=0
for j,x in enumerate(codes):
 state=np.array([(x>>i)&1 for i in range(24)],dtype=np.uint8);fval=float(coeff@(state.astype(float)-.5));F.append(fval);n=0
 for face in faces:
  bits=state[face]
  if bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1]:
   y=x
   for i in face:y^=1<<i
   rows.append(j);cols.append(lookup[y]);n+=1
 counts.append(n)
 observed=k.literal_O(state,coeff[None,:])
 if abs(observed[0]-fval)>1e-13 or abs(k.source_norm(observed)-fval)>1e-13:raise ValueError('literal linear source')
 for xi in (0.,-.01,.01,-.005,.005,-.0025,.0025):
  shift=abs(xi)*np.sqrt(8)/2;b=k.branch_value(n,fval,-.05,xi,shift,24)
  if b<1-1e-13 or abs(b-n/24-(1-(.95*n+xi*fval-shift)/24))>1e-13:raise ValueError('actual G')
  if abs(b*(1/(24*b))-1/24)>1e-15:raise ValueError('offdiagonal G')
  controls+=1
A=coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(864,864)).tocsr();F=np.array(F);counts=np.array(counts)
energies={}
for xi in (0.,-.01,.01,-.005,.005,-.0025,.0025):
 H=diags(.95*counts+xi*F)-A
 val,vec=eigsh(H,k=1,which='SA',tol=1e-13,v0=np.linspace(.7,1.3,864));psi=vec[:,0];psi*=np.sign(psi.sum());energy=float(val[0]);local=float(psi@(-.05*counts+xi*F)/psi.sum())
 if abs(local-energy)>3e-12:raise ValueError('mixed local energy')
 if np.linalg.norm(H@psi-energy*psi)>3e-11:raise ValueError('eigen residual')
 energies[str(xi)]=energy
curvatures={str(h):-(energies[str(h)]+energies[str(-h)]-2*energies['0.0'])/h**2 for h in (.01,.005,.0025)}
result={'status':'PASS','branch_rows':controls,'actual_graph_moves':len(rows),'energies':energies,'curvatures':curvatures,'kernel_sha256':hashlib.sha256(Path(k.__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'scope':'literal L2 coordinates and actual linear functions; sparse floating eigenreference, not interval certificate'}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
