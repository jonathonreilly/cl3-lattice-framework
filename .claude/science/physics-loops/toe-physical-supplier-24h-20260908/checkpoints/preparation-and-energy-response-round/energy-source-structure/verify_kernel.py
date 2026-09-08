import os,sys,signal,time,json,resource,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True;signal.alarm(180);start=time.monotonic()
sys.path[:0]=[str(p.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from tilted_kernel import prepare,branch_value,literal_O,flip_cached
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
raw=np.load(p/'raw.npz');states=((raw['states'][:,None]>>np.arange(24))&1).astype(np.uint8);g=prod.build_geometry(2);cr,ci,_=prod.transverse_coefficients(2,(1,));checks={}
def ck(k,b):
 if not bool(b):raise AssertionError(k)
 checks[k]=True
moves=0;rows=0;cases=[(.93,0.),(.95,0.),(.97,0.),(.95,-.02),(.95,.02),(.95,-.01),(.95,.01)]
for k,state in enumerate(states):
 o=literal_O(state,cr);ck('source_'+str(k),np.max(abs(o-raw['O'][k]))<1e-12);nf=prod.count_flippable(state,g.plaquette_links)
 for V,lam in cases:
  b=branch_value(nf,float(o@o),V-1,lam,12*abs(lam),24);diag=b-nf/24;target=1-(V*nf+lam*(o@o)-12*abs(lam))/24
  assert b>=1 and abs(diag-target)<1e-12 and 0<=1-nf/(24*b)<=1
  assert abs(b/(24*b)-1/24)<1e-14;rows+=1
 for f,links in enumerate(g.plaquette_links):
  if prod.is_flippable(state,links):
   copy=state.copy();ob=o.copy();count=flip_cached(copy,nf,ob,f,cr,g.plaquette_links,g.affected_plaquettes,g.affected_counts)
   literal=state.copy();literal[links]^=1
   assert np.array_equal(copy,literal) and count==prod.count_flippable(literal,g.plaquette_links)
   assert np.max(abs(ob-literal_O(literal,cr)))<1e-12;assert abs(ob@ob-raw['X'][np.flatnonzero(raw['states']==sum(int(z)<<i for i,z in enumerate(literal)))[0]])<1e-12;moves+=1
ck('all_moves',moves==6912);ck('all_source_rows',rows==6048)
for V in [.93,.95,.97]:
 a=prod.prepare_population(initial_ice(2).ravel(),V-1,64,20,80,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,3400000)
 b=prepare(initial_ice(2).ravel(),V-1,0.,0.,64,20,80,cr,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,3400000)
 ck('lambda0_bit_exact_'+str(V),np.array_equal(a[0],b[0]) and np.array_equal(a[1],b[1]) and a[2]==np.mean(b[3]) and a[3]==b[5])
for lam in [-.02,.02,-.01,.01]:
 b=prepare(initial_ice(2).ravel(),-.05,lam,12*abs(lam),64,20,80,cr,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,3400001)
 ck('tilted_drift_'+str(lam),b[6]<1e-10 and np.max(abs(b[2]-prod.evaluate_observables(b[0],cr,ci).real))<1e-10)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert rss<384
out={'check_groups':len(checks),'all_group_pass':all(checks.values()),'states':len(states),'moves':moves,'branch_source_rows':rows,'seconds':time.monotonic()-start,'rss_mib':rss,'kernel_sha256':hashlib.sha256((p/'tilted_kernel.py').read_bytes()).hexdigest()};(p/'KERNEL_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
