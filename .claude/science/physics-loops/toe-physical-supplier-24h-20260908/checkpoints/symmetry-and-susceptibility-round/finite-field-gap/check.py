import os,time
start=time.monotonic()
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import runpy,contextlib,io,json,resource,hashlib
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import eigsh
from scipy import sparse
inp=Path('/private/tmp/toe-24h-probes-20260908/detuned-energy-moment/check.py')
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(inp))
rows=[]
for V in [.95,1.]:
 H=V*d['N']-d['A'];e,u=eigsh(H,k=2,which='SA',tol=1e-13,v0=1+np.arange(864)/864);idx=np.argsort(e);e=e[idx];psi=u[:,idx[0]];F=d['O'][0];mean=float(psi**2@F);S=float(psi**2@(F*F));R=max(abs(F));gap=e[1]-e[0]
 if abs(mean)>1e-10:raise AssertionError('mean')
 for xi in [.05,.1,.2,.4]:
  ex=eigsh(H+sparse.diags(xi*F),k=1,which='SA',tol=1e-13,v0=1+np.arange(864)/864)[0][0];delta=e[0]-ex;bound=xi*xi*S/delta+abs(xi)*R-delta
  if delta<=0 or gap>bound+1e-9:raise AssertionError('bound')
  rows.append(dict(V=V,xi=xi,delta=float(delta),S=S,R=float(R),full_gap=float(gap),gap_upper=float(bound),schur_lower=float(gap+delta-abs(xi)*R)))
print(json.dumps(dict(rows=rows,seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest()),indent=2))
