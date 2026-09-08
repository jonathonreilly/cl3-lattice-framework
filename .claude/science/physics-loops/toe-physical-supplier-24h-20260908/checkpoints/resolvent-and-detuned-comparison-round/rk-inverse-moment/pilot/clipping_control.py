import os,sys,json
from pathlib import Path
p=Path(__file__).resolve().parent;os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
sys.path[:0]=[str(p.parent.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from kernel import collect
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
g=prod.build_geometry(4);cr,ci,_=prod.transverse_coefficients(4,(1,2));c=cr+1j*ci;start=initial_ice(4).ravel();cap=np.zeros(3,np.int64)
a=collect(start,g.plaquette_links,c,np.zeros((1,3),np.int64),cap,0,901);b=collect(start,g.plaquette_links,c,np.ones((1,3),np.int64),cap,0,901)
if not np.array_equal(a[0],b[0]) or np.max(abs(a[0]))<=.01:raise AssertionError('nonzero unchanged origin')
if np.max(abs(a[1]-abs(a[0][:,None,:])**2))>1e-12 or np.max(abs(b[1]))!=0:raise AssertionError('clipping not replacement')
(p/'CLIPPING_CONTROL.json').write_text(json.dumps({'zero_lag_is_C0':True,'clipped_contribution_zero_not_capped_endpoint':True,'origin_unchanged':True,'not_physics_sample':True},indent=2)+'\n')
