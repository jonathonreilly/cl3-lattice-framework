import os,sys,time,signal,resource,json,hashlib,argparse
from pathlib import Path
p=Path(__file__).resolve().parent;start=time.monotonic();signal.alarm(180)
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
sys.path[:0]=[str(p),str(p.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from kernel import prepare
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,vertex_degrees,electric_flux

def source_coefficients(cr,ci,h):
 if h not in (1,2):raise ValueError('harmonic')
 sl=slice(0,6)
 return np.vstack((cr[sl],ci[sl]))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--population',type=int,choices=(512,1024),required=True);ap.add_argument('--case',type=int,choices=range(8),required=True);a=ap.parse_args()
 cases=[(h,l) for h in (1,2) for l in (-.02,.02,-.01,.01)];h,lam=cases[a.case];g=prod.build_geometry(4);cr,ci,modes=prod.transverse_coefficients(4,(1,2));co=source_coefficients(cr,ci,h);rows=[]
 for rep in range(8):
  seed=4500000+10000*(a.population==1024)+rep
  st,ct,ob,ns,xs,ess,drift,div=prepare(initial_ice(4).ravel(),0.,lam,96*abs(lam),a.population,20,160,co,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,seed)
  literal=prod.evaluate_observables(st,cr[6*(h-1):6*h],ci[6*(h-1):6*h]);error=float(np.max(abs(ob[:,:6]+1j*ob[:,6:]-literal)))
  if not np.isfinite(error) or error>1e-10 or not np.isfinite(drift) or drift>1e-10:raise ValueError('cache check')
  if not np.all((st==0)|(st==1)):raise ValueError('binary state')
  for s,n in zip(st,ct):
   if prod.count_flippable(s,g.plaquette_links)!=n or not np.all(vertex_degrees(s.reshape(4,4,4,3))==3) or electric_flux(s.reshape(4,4,4,3))!=(0,0,0):raise ValueError('state invariants')
  en=lam*xs
  if len(en)!=40 or not np.isfinite(en).all():raise ValueError('energy window')
  rows.append(dict(replica=rep,seed=seed,Nf_window=ns.tolist(),X_window=xs.tolist(),energy_window=en.tolist(),physical_energy=float(en.mean()),shifted_energy=float(en.mean()-96*abs(lam)),cache_drift=drift,final_literal_error=error,resampling_weight_ESS=ess,ancestral_diversity=div,postconditions=True))
 elapsed=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
 if not 0<rss<384 or elapsed>=180:raise ValueError('resources')
 paths=[p/'driver.py',p/'kernel.py',p/'PREREGISTRATION.md',Path(prod.__file__)]
 print(json.dumps(dict(L=4,V=1.,harmonic=h,lambda_value=lam,shift=96*abs(lam),case=a.case,population=a.population,replicas=rows,seconds=elapsed,rss_mib=rss,hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in paths}),allow_nan=False))
if __name__=='__main__':main()
