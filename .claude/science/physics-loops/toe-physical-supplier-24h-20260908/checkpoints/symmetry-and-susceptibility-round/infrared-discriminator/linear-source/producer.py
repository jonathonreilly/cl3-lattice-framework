import os,sys,time,signal,resource,json,hashlib,argparse
from pathlib import Path
p=Path(__file__).resolve().parent;start=time.monotonic();signal.alarm(180)
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
sys.path[:0]=[str(p),'/private/tmp/toe-24h-probes-20260908/detuned-energy-moment','/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from population_kernel import prepare,literal_O
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,vertex_degrees,electric_flux
GRID=(0.,-.01,.01,-.005,.005,-.0025,.0025)
def run(pop,xi,reps=16,classical=20,burn=80):
 g=prod.build_geometry(2);cr,ci,modes=prod.transverse_coefficients(2,(1,));co=cr[:1].copy();rows=[];shift=abs(xi)*np.sqrt(8)/2
 for rep in range(reps):
  seed=5700000+10000*(pop==256)+rep
  st,ct,ob,ns,fs,ess,drift,div=prepare(initial_ice(2).ravel(),-.05,xi,shift,pop,classical,burn,co,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,seed)
  error=float(np.max(abs(ob-prod.evaluate_observables(st,cr[:1],ci[:1]).real)))
  if not np.isfinite(error) or error>1e-10 or not np.isfinite(drift) or drift>1e-10:raise ValueError('cache')
  if not np.all((st==0)|(st==1)):raise ValueError('binary')
  for s,n in zip(st,ct):
   if prod.count_flippable(s,g.plaquette_links)!=n or not np.all(vertex_degrees(s.reshape(2,2,2,3))==3) or electric_flux(s.reshape(2,2,2,3))!=(0,0,0):raise ValueError('invariants')
  en=-.05*ns+xi*fs
  if len(en)!=min(40,burn) or not np.isfinite(en).all():raise ValueError('window')
  rows.append(dict(replica=rep,seed=seed,Nf_window=ns.tolist(),F_window=fs.tolist(),energy_window=en.tolist(),physical_energy=float(en.mean()),shifted_energy=float(en.mean()-shift),cache_drift=drift,literal_error=error,ESS=ess,ancestral_diversity=div,postconditions=True))
 return rows
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--population',type=int,choices=(128,256),required=True);ap.add_argument('--case',type=int,choices=range(7),required=True);a=ap.parse_args();xi=GRID[a.case];rows=run(a.population,xi)
 elapsed=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
 if not 0<rss<384 or elapsed>=180:raise ValueError('resources')
 paths=[p/'producer.py',p/'population_kernel.py',Path(prod.__file__)]
 print(json.dumps(dict(V=.95,xi=xi,shift=abs(xi)*np.sqrt(8)/2,population=a.population,case=a.case,primary_h=.01,rows=rows,seconds=elapsed,rss_mib=rss,hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in paths}),allow_nan=False))
