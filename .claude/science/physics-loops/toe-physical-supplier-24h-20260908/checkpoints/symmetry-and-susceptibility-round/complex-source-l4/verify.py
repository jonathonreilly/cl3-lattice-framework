import os,sys,time,signal,resource,json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True;signal.alarm(180);start=time.monotonic()
sys.path[:0]=[str(p),str(p.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from kernel import prepare,literal_O,flip_cached,branch_value,resample,source_norm
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
checks={}
def ck(k,v):
 if not bool(v):raise AssertionError(k)
 checks[k]=True
# L2 full source/move coverage, actual concatenated cache functions.
g=prod.build_geometry(2);cr,ci,_=prod.transverse_coefficients(2,(1,));coef=np.vstack((cr,ci));raw=np.load(p.parent/'energy-source-structure/raw.npz');states=((raw['states'][:,None]>>np.arange(24))&1).astype(np.uint8);moves=0
for k,state in enumerate(states):
 o=literal_O(state,coef);nf=prod.count_flippable(state,g.plaquette_links)
 if np.max(abs(o[:6]-raw['O'][k]))>1e-12:raise AssertionError('L2_source')
 for f,face in enumerate(g.plaquette_links):
  if prod.is_flippable(state,face):
   st=state.copy();oo=o.copy();n=flip_cached(st,nf,oo,f,coef,g.plaquette_links,g.affected_plaquettes,g.affected_counts)
   if np.max(abs(oo-literal_O(st,coef)))>1e-12 or n!=prod.count_flippable(st,g.plaquette_links):raise AssertionError('L2_flip')
   moves+=1
ck('L2_all864_6912',moves==6912)
old=prod.prepare_population(initial_ice(2).ravel(),-.05,32,2,8,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,4600010)
new=prepare(initial_ice(2).ravel(),-.05,0.,0.,32,2,8,coef,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,4600010)
ck('L2_seed_compatibility',np.array_equal(old[0],new[0]) and np.array_equal(old[1],new[1]) and old[3]==new[5])
# Independent fixed legal L4 visited states. Validate every flippable face, plane and seam.
g=prod.build_geometry(4);cr,ci,_=prod.transverse_coefficients(4,(1,2));rng=np.random.default_rng(4600020);state=initial_ice(4).ravel();visited=[]
for step in range(192*16):
 f=int(rng.integers(192))
 if prod.is_flippable(state,g.plaquette_links[f]):state[g.plaquette_links[f]]^=1
 if step%192==191:visited.append(state.copy())
count=0;wrong=False
for h in (1,2):
 sl=slice((h-1)*6,h*6);coef=np.vstack((cr[sl],ci[sl]))
 for state in visited:
  o=literal_O(state,coef);direct=prod.evaluate_observables(state[None,:],cr[sl],ci[sl])[0]
  ck(f'complex_{h}_{count}',np.max(abs(o[:6]+1j*o[6:]-direct))<1e-12)
  if abs(source_norm(o)-float(np.sum(abs(direct)**2)))>1e-12:raise AssertionError('actual_source_norm')
  wrong=wrong or abs(o@o-o[:6]@o[:6])>1e-8
  nf=prod.count_flippable(state,g.plaquette_links)
  for lam in (-.02,.02,-.01,.01):
   b=branch_value(nf,o@o,0.,lam,96*abs(lam),192)
   if b<1 or abs(b-nf/192-(1-(nf+lam*(o@o)-96*abs(lam))/192))>1e-12:raise AssertionError('L4_branch')
  for f,face in enumerate(g.plaquette_links):
   if prod.is_flippable(state,face):
    st=state.copy();oo=o.copy();n=flip_cached(st,nf,oo,f,coef,g.plaquette_links,g.affected_plaquettes,g.affected_counts)
    if np.max(abs(oo-literal_O(st,coef)))>1e-12 or n!=prod.count_flippable(st,g.plaquette_links):raise AssertionError('L4_flip')
    count+=1
ck('real_only_adverse',wrong)
aa=np.arange(12,dtype=np.uint8).reshape(3,4);cc=np.array([2,3,4]);oo=np.arange(36.).reshape(3,12);an=np.arange(3)
zz=resample(aa,cc,oo,an,np.array([-1000.,0.,-1000.]))
ck('nontrivial_cache_resampling',np.array_equal(zz[2],np.repeat(oo[1:2],3,axis=0)) and np.all(zz[3]==1))
coef=np.vstack((cr[:6],ci[:6]));old=prod.prepare_population(initial_ice(4).ravel(),0.,16,1,2,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,4600030);new=prepare(initial_ice(4).ravel(),0.,0.,0.,16,1,2,coef,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,4600030)
ck('RK_lambda0_old_reference',np.array_equal(old[0],new[0]) and np.array_equal(old[1],new[1]) and old[3]==new[5])
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck('resources',0<rss<384 and time.monotonic()-start<180)
out={'checks':checks,'L4_checked_flips':count,'seconds':time.monotonic()-start,'rss_mib':rss,'kernel_hash':hashlib.sha256((p/'kernel.py').read_bytes()).hexdigest()};(p/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
