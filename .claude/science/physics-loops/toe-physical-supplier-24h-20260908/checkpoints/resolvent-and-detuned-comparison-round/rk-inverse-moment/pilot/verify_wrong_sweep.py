import os,sys,signal,json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True;signal.alarm(180)
sys.path[:0]=[str(p.parent.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
from numba import njit
import producer_original as prod
from wrong_sweep import apply_face,endpoint,observe,generate_lags
raw=np.load(p.parent.parent/'energy-source-structure/raw.npz');states=((raw['states'][:,None]>>np.arange(24))&1).astype(np.uint8);g=prod.build_geometry(2);cr,ci,_=prod.transverse_coefficients(2,(1,));coeff=cr+1j*ci;calls=0
@njit(cache=True)
def firstface(seed,M):np.random.seed(seed);return np.random.randint(M)
for k,x in enumerate(states):
 if np.max(abs(observe(x,coeff)-raw['O'][k]))>1e-12:raise AssertionError('literal source')
 counts={}
 for f,face in enumerate(g.plaquette_links):
  y=x.copy();apply_face(y,g.plaquette_links,f);literal=x.copy()
  if prod.is_flippable(x,face):literal[face]^=1
  if not np.array_equal(y,literal):raise AssertionError('elementary transition')
  key=tuple(y);counts[key]=counts.get(key,0)+1;calls+=1
 if counts.get(tuple(x),0)!=24-int(raw['nf'][k]):raise AssertionError('diagonal self probability')
x=states[0]
if not np.array_equal(endpoint(x,g.plaquette_links,0,999),x):raise AssertionError('zero endpoint')
for seed in range(64):
 f=firstface(seed,24);want=x.copy();apply_face(want,g.plaquette_links,f)
 if not np.array_equal(endpoint(x,g.plaquette_links,1,seed),want):raise AssertionError('one elementary step not sweep')
for M in [24,192]:
 for a in [.25,.5,1.]:
  q=M/(M+a)
  for k in [0,1,2,16,64,128]:
   U=1-(q**k+q**(k+1))/2
   if int(generate_lags(np.array(U),q))!=k:raise AssertionError('geometric support offset')
(p/'VERIFY.json').write_text(json.dumps({'all_elementary_proposals':calls,'source_rows':864,'one_step_seeds':64,'geometric_CDF_midpoints':36,'all_pass':True,'kernel_sha256':hashlib.sha256((p/'kernel.py').read_bytes()).hexdigest()},indent=2)+'\n')
