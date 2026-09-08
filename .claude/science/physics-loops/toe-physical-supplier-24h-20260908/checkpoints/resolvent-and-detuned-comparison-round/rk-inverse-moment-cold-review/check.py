import os,sys
os.environ['OPENBLAS_NUM_THREADS']='1';sys.dont_write_bytecode=True
sys.path.insert(0,'/private/tmp/toe-24h-probes-20260908/detuned-energy-moment');sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
from pathlib import Path
import numpy as np,runpy,io,contextlib,json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/rk-inverse-moment/pilot');src=(p/'kernel.py').read_text();scope={};exec(src.replace('@njit(cache=True)',''),scope)
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path('/private/tmp/toe-24h-probes-20260908/detuned-energy-moment/check.py')
faces=np.array(d['faces']);coeff=np.array([[(-1)**(sum(r)+r[a])/np.sqrt(8) if b==z else 0 for r,z in d['links']] for a,b in d['modes']],complex);x=np.array([(d['states'][0]>>j)&1 for j in range(24)],np.uint8)
checks={};q=np.array([24/24.25,24/24.5,24/25]);caps=np.array([800,368,169]);lags=np.array([[0,1,2],[4,7,9],[801,369,170],[3,5,8]])
a,b,s=scope['collect'](x,faces,coeff,lags,caps,2,2);a2,b2,s2=scope['collect'](x,faces,coeff,lags+3,caps,2,2)
checks['origin_rng_independent_of_lags']=bool(np.array_equal(s,s2) and np.array_equal(a,a2));checks['tail_zero']=bool(np.all(b[2]==0))
for i in [0,1,3]:
 for j in range(3):
  np.random.seed(100000000+2000+3*i+j);y=s[i].copy()
  for _ in range(lags[i,j]):
   f=np.random.randint(24);bits=y[faces[f]]
   if bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1]:y[faces[f]]^=1
  expect=np.conjugate(a[i])*(coeff@(y-.5));checks[f'endpoint_{i}_{j}']=bool(np.max(abs(expect-b[i,j]))<1e-12)
checks['shifted_fake_narrow']=((1005)*(.5/1001+.5/1009)-1)<2e-5
if not all(checks.values()):raise AssertionError(checks)
print(json.dumps(dict(checks=checks,count=len(checks),kernel_sha256=hashlib.sha256(src.encode()).hexdigest(),scope='actual source Python body without njit decorator; production compiled path reviewed separately'),indent=2))
