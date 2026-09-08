import os,sys,json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent;old=p.parent/'ice-estimator-calibration'
for k in['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True;sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
import numpy as np
import producer_original as prod
from measurement_derivative import measure_raw_block
from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import build_geometry
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
for f in['producer_original.py','measurement_derivative.py']:assert(p/f).read_bytes()==(old/f).read_bytes()
g=build_geometry(2);cr,ci,_=prod.transverse_coefficients(2,(1,));out=[]
for tau in[16,3]:
 st,ct,_,_=prod.prepare_population(initial_ice(2).ravel(),-.05,64,20,40,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,331190)
 r=measure_raw_block(st,ct,-.05,tau,6,cr,ci,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8);out.append(r)
assert np.array_equal(out[0][2][:4],out[1][2])
assert np.array_equal(out[0][5][:4],out[1][5]) and np.array_equal(out[0][6][:4],out[1][6])
print(json.dumps({'unchanged_sources':True,'same_seed_tau0_to3_raw_and_genealogy_exact_match':True,'finite_F_endpoint':'tau3 uses exactly9sweeps in both; suffix6 and origin distribution unchanged','hashes':{f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in['producer_original.py','measurement_derivative.py']}},indent=2))
