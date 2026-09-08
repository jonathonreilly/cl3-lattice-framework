import os,sys,time,signal,resource,json,argparse,ast,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
signal.alarm(180);start=time.monotonic()
sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
import numpy as np
import producer_original as prod
from measurement_derivative import measure_raw_block
from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import build_geometry,count_flippable
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,electric_flux,vertex_degrees
ap=argparse.ArgumentParser();ap.add_argument('--population',type=int,default=512);ap.add_argument('--burn',type=int,default=20);ap.add_argument('--vi',type=int,default=0);ap.add_argument('--verify',action='store_true');args=ap.parse_args()
assert args.population in [512,1024,2048] and args.burn in [20,40] and args.vi in [0,1]
geom=build_geometry(2);cr,ci,modes=prod.transverse_coefficients(2,(1,));delta=[-.05,0.][args.vi]
ex=np.load(p/'exact_data.npz');assert np.array_equal(ex['faces'],geom.plaquette_links)
# AST equality on all actually called geometry/count definitions across fetched/current producer inputs.
a=ast.parse(Path('/private/tmp/toe-24h-probes-20260908/ice-physics/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py').read_text());b=ast.parse(Path('/private/tmp/toe-physical-supplier-24h-20260908/scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py').read_text())
for name in ['link_index','build_geometry','is_flippable','count_flippable','flip_and_update_count']:
 get=lambda t:ast.dump(next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name==name),include_attributes=False)
 assert get(a)==get(b),name
# Check actual observable all864 states, not only expected labels.
allstates=((ex['states'][:,None]>>np.arange(24))&1).astype(np.uint8)
actual=prod.evaluate_observables(allstates,cr,ci)
assert modes[0]==(1,0,1) and np.max(abs(actual[:,0]-ex['O']))<1e-14

def prepare(seed,pop=None):return prod.prepare_population(initial_ice(2).ravel(),delta,args.population if pop is None else pop,20,args.burn,geom.plaquette_links,geom.affected_plaquettes,geom.affected_counts,8,seed)
def measure(states,counts,fn):return fn(states,counts,delta,16,6,cr,ci,geom.plaquette_links,geom.affected_plaquettes,geom.affected_counts,8)
if args.verify:
 st,ct,_,_=prepare(910001,64);old=measure(st,ct,prod.measure_correlation_block)
 st,ct,_,_=prepare(910001,64);new=measure(st,ct,measure_raw_block)
 assert np.array_equal(old[0],new[0]) and np.array_equal(old[1],new[1])
 assert np.array_equal(old[2],new[2]/new[2][0].real)
 for i in range(3,7):assert np.array_equal(old[i],new[i])
 out={'verification':'exact same seed states, counts, normalized correlations, ESS and all genealogy fields match','observable_all_states':True,'used_dependency_AST_match':True}
else:
 records=[];pi=[512,1024,2048].index(args.population);bi=[20,40].index(args.burn)
 for replica in range(8):
  seed=810000+100000*args.vi+10000*pi+1000*bi+replica
  st,ct,mc,eff=prepare(seed);blocks=[]
  for origin in range(4):
   st,ct,raw,ess,finalsurv,div,surv=measure(st,ct,measure_raw_block)
   assert np.max(abs(raw.imag))<1e-12
   blocks.append({'raw_product_means':raw.real.tolist(),'raw_product_sums':(raw.real*args.population).tolist(),'denominator_means':raw[0].real.tolist(),'minimum_ESS':float(ess),'final_origin_count':float(finalsurv*args.population),'origin_counts_by_tau':(div*args.population).tolist(),'suffix_distinct_counts_by_tau':(surv*args.population).tolist()})
   if origin<3:
    anc=np.arange(args.population,dtype=np.int32);labels=np.full((1,args.population),-1,dtype=np.int32)
    for _ in range(3):st,ct,anc,labels,_=prod.propagate_sweep(st,ct,anc,labels,delta,geom.plaquette_links,geom.affected_plaquettes,geom.affected_counts,8)
  assert all(count_flippable(x,geom.plaquette_links)==n for x,n in zip(st,ct))
  shaped=st.reshape((-1,2,2,2,3));assert all(np.all(vertex_degrees(x)==3) and electric_flux(x)==(0,0,0) for x in shaped)
  records.append({'replica':replica,'seed':seed,'mixed_energy':float(delta*mc),'burn_minimum_ESS':float(eff),'blocks':blocks})
 out={'V':1+delta,'population':args.population,'burn':args.burn,'classical_warmup':20,'F':6,'modes':modes,'replicas':records}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert 0<rss<384,rss
out.update(seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(out,allow_nan=False))
