import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
signal.alarm(180);start=time.monotonic();sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
import numpy as np
import producer_original as prod
from measurement_derivative import measure_raw_block
from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import build_geometry,count_flippable
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
ap=argparse.ArgumentParser();ap.add_argument('--population',type=int,required=True);ap.add_argument('--batch',type=int,required=True);a=ap.parse_args();assert a.population in[512,2048] and a.batch in range(4)
g=build_geometry(2);cr,ci,modes=prod.transverse_coefficients(2,(1,));rows=[]
for rep in range(a.batch*32,(a.batch+1)*32):
 seed=1200000+a.population*1000+rep
 st,ct,_,_=prod.prepare_population(initial_ice(2).ravel(),-.05,a.population,20,40,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,seed);blocks=[]
 for origin in range(4):
  st,ct,raw,ess,final,div,surv=measure_raw_block(st,ct,-.05,3,6,cr,ci,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
  assert np.max(abs(raw.imag))<1e-12
  blocks.append({'raw':raw.real.tolist(),'raw_sums':(raw.real*a.population).tolist(),'minimum_ESS':float(ess),'origin_counts':(div*a.population).tolist(),'suffix_counts':(surv*a.population).tolist()})
  if origin<3:
   anc=np.arange(a.population,dtype=np.int32);labels=np.full((1,a.population),-1,dtype=np.int32)
   for _ in range(3):st,ct,anc,labels,_=prod.propagate_sweep(st,ct,anc,labels,-.05,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
 assert all(count_flippable(x,g.plaquette_links)==n for x,n in zip(st,ct))
 rows.append({'replica':rep,'seed':seed,'blocks':blocks})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert 0<rss<384
print(json.dumps({'population':a.population,'batch':a.batch,'replicas':rows,'seconds':time.monotonic()-start,'rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},allow_nan=False))
