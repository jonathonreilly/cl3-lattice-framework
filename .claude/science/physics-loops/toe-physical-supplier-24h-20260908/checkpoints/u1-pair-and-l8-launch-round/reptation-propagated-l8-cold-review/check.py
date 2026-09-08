import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import pathlib,sys,json,hashlib,importlib.util,numpy as np
sys.dont_write_bytecode=True
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-propagated-l8-design');O=pathlib.Path(__file__).parent
sys.path.insert(0,str(P));from checkpoint import load
from analysis_core import stats
f=json.loads((P/'PRODUCTION_FREEZE.json').read_text())
for n,h in f.items():
 if hashlib.sha256((P/n).read_bytes()).hexdigest()!=h:raise RuntimeError('freeze')
runtime=json.loads((P/'RUNTIME.json').read_text())
for n,h in runtime['files'].items():
 if hashlib.sha256(pathlib.Path(n).read_bytes()).hexdigest()!=h:raise RuntimeError('runtime')
a=np.array([[400+i,2+.01*i,3+.02*i,-20+.005*i,405+.03*i,-39+.02*i,-58+.04*i,8+.01*i,15+.02*i] for i in range(16)])
def fun(x):
 N,S,T,E,H2,SE,TE,S2,T2=x;out=[]
 for q,z,ze,z2 in ((2-np.sqrt(2),S,SE,S2),(2,T,TE,T2)):
  d=q*(.95*N-E)/(512*z);c=ze/z-E;out.extend([d,d+c,c,H2-E*E,z2-z*z])
 return np.array(out)
m=a.mean(0);J=np.empty((10,9))
for i in range(9):
 z=m.astype(complex);z[i]+=1e-25j;J[:,i]=fun(z).imag/1e-25
v=fun(m);C=J@np.cov(a,rowvar=False)@J.T/16;out=stats(a);av=np.array([r[k] for r in out['rows'] for k in ('D','R','correction','VarH','VarX')])
if max(abs(v-av))>1e-10 or np.max(abs(C-out['estimator_covariance']))>1e-10:raise RuntimeError('cov')
with np.load(P/'ROUNDTRIP.npz',allow_pickle=False) as f:raw={k:f[k].copy() for k in f.files}
raw['O'][0,0]=complex(float('nan'),0);np.savez_compressed(O/'NAN_O.npz',**raw)
try:load(O/'NAN_O.npz')
except ValueError:nan='rejected'
else:nan='ACCEPTED: repair required'
result={'freeze_sha':hashlib.sha256((P/'PRODUCTION_FREEZE.json').read_bytes()).hexdigest(),'runtime_files_verified':len(runtime['files']),'estimate_residual':float(max(abs(v-av))),'covariance_residual':float(np.max(abs(C-out['estimator_covariance']))),'NaN_O_mutant':nan,'scope':'Existing checkpoint read only; synthetic math and malformed checkpoint controls, no sampling.'}
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
