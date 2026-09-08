import os,sys,time,signal,resource,json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent;start=time.monotonic();signal.alarm(30)
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
sys.path[:0]=[str(p),str(p.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from kernel import prepare
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
import_seconds=time.monotonic()-start;g=prod.build_geometry(4);cr,ci,modes=prod.transverse_coefficients(4,(1,2));rows=[]
for h,lam,seed in [(1,.02,4600000),(2,-.02,4600001)]:
 sl=slice(6*(h-1),6*h);coeff=np.vstack((cr[sl],ci[sl]));t=time.monotonic()
 z=prepare(initial_ice(4).ravel(),0.,lam,96*abs(lam),128,2,8,coeff,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,seed)
 elapsed=time.monotonic()-t;literal=prod.evaluate_observables(z[0],cr[sl],ci[sl]);drift=float(np.max(abs(z[2][:,:6]+1j*z[2][:,6:]-literal)))
 if drift>1e-10 or not np.isfinite(drift):raise AssertionError('micro_cache')
 rows.append({'harmonic':h,'lambda':lam,'seed':seed,'work_seconds':elapsed,'cache_drift':drift,'physical_energy':float(lam*np.mean(z[4])),'scope':'timing/control only, not a physics estimate'})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384 or time.monotonic()-start>=30:raise AssertionError('resources')
# The first call includes cached-JIT load. Conservatively use slower of two whole calls as hot upper proxy.
unit=max(r['work_seconds'] for r in rows);forecasts={}
for pop in (512,1024):forecasts[str(pop)]=1.5*unit*(pop/128)*((20+160)/(2+8))*8+import_seconds
out={'rows':rows,'import_seconds':import_seconds,'first_call_includes_cached_JIT_load':True,'forecast_method':'slower measured whole call;18x sweeps, population factor,8replicas,50% headroom plus import','forecast_cell_seconds':forecasts,'forecast_16_cells_seconds':8*sum(forecasts.values()),'seconds':time.monotonic()-start,'rss_mib':rss,'kernel_hash':hashlib.sha256((p/'kernel.py').read_bytes()).hexdigest()}
(p/'MICRO.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
