import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True;signal.alarm(180);start=time.monotonic()
sys.path[:0]=[str(p.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from tilted_kernel import prepare
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,vertex_degrees,electric_flux
ap=argparse.ArgumentParser();ap.add_argument('--population',type=int,choices=[1024,2048],required=True);ap.add_argument('--case',type=int,choices=range(7),required=True);args=ap.parse_args()
cases=[(.93,0.),(.95,0.),(.97,0.),(.95,-.02),(.95,.02),(.95,-.01),(.95,.01)];V,lam=cases[args.case];shift=12*abs(lam);g=prod.build_geometry(2);cr,ci,modes=prod.transverse_coefficients(2,(1,));assert np.max(abs(ci))<1e-14
rows=[];pi=[1024,2048].index(args.population)
for rep in range(16):
 seed=3400000+10000*pi+rep
 st,ct,obs,ns,xs,ess,drift,div=prepare(initial_ice(2).ravel(),V-1,lam,shift,args.population,20,80,cr,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,seed)
 assert drift<1e-10
 assert all(prod.count_flippable(x,g.plaquette_links)==n for x,n in zip(st,ct))
 assert all(np.all(vertex_degrees(x)==3) and electric_flux(x)==(0,0,0) for x in st.reshape((-1,2,2,2,3)))
 physical=(V-1)*ns+lam*xs
 rows.append({'replica':rep,'seed':seed,'physical_energy':float(np.mean(physical)),'energy_window':physical.tolist(),'Nf_window':ns.tolist(),'X_window':xs.tolist(),'shifted_energy':float(np.mean(physical)-shift),'ESS':float(ess),'cache_drift':float(drift),'ancestral_diversity':float(div),'postconditions':True})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert 0<rss<384 and time.monotonic()-start<180
print(json.dumps({'V':V,'lambda':lam,'shift':shift,'population':args.population,'replicas':rows,'modes':modes,'seconds':time.monotonic()-start,'rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'kernel_sha256':hashlib.sha256((p/'tilted_kernel.py').read_bytes()).hexdigest()},allow_nan=False))
