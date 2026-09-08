import os,sys,json
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
import numpy as np
from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import build_geometry,is_flippable,count_flippable,flip_and_update_count
x=np.load(p/'exact_data.npz');g=build_geometry(2);states=x['states'];lookup={int(z):i for i,z in enumerate(states)};count=0;resid=0.
for row,z in enumerate(states):
 a=((z>>np.arange(24))&1).astype(np.uint8);nf=count_flippable(a,g.plaquette_links);assert nf==x['counts'][row]
 dest=[]
 for face,links in enumerate(g.plaquette_links):
  if is_flippable(a,links):
   b=a.copy();nc=flip_and_update_count(b,face,nf,g.plaquette_links,g.affected_plaquettes,g.affected_counts)
   zz=sum(int(bit)<<i for i,bit in enumerate(b));j=lookup[zz];assert nc==x['counts'][j];dest.append(j);count+=1
 for dv in [-.05,0.]:
  branch=1-dv*nf/24;P=np.zeros(len(states))
  for j in dest:P[j]+=1/(24*branch)
  P[row]=1-len(dest)/(24*branch)
  G=np.zeros(len(states));G[row]=1-(1+dv)*nf/24
  for j in dest:G[j]+=1/24
  resid=max(resid,float(max(abs(branch*P-G))));assert np.min(P)>=-1e-15 and abs(P.sum()-1)<1e-14
assert resid<1e-14 and count==6912
print(json.dumps({'states':864,'all_directed_flip_updates':count,'one_step_G_residual':resid,'V_cases':[.95,1.]},indent=2))
