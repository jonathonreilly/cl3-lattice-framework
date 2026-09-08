import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
signal.alarm(180);start=time.monotonic()
sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
import numpy as np
from numba import njit
import producer_original as prod
from prepare_derivative import prepare_with_samples
from measurement_derivative import measure_raw_block
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,electric_flux,vertex_degrees
ap=argparse.ArgumentParser();ap.add_argument('--population',type=int,choices=[1024,2048],required=True);ap.add_argument('--vi',type=int,choices=range(5),required=True);ap.add_argument('--verify',action='store_true');args=ap.parse_args()
Vs=[.93,.94,.95,.96,.97];V=Vs[args.vi];dv=V-1;pi=[1024,2048].index(args.population)
g=prod.build_geometry(2);cr,ci,modes=prod.transverse_coefficients(2,(1,))
@njit(cache=True)
def seed_rng(seed):np.random.seed(seed)
def prep(seed,pop,fn=prepare_with_samples):return fn(initial_ice(2).ravel(),dv,pop,20,80,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,seed)
def validate(st,ct):
 if not all(prod.count_flippable(x,g.plaquette_links)==n for x,n in zip(st,ct)):raise AssertionError('count dictionary')
 if not all(np.all(vertex_degrees(x)==3) and electric_flux(x)==(0,0,0) for x in st.reshape((-1,2,2,2,3))):raise AssertionError('Gauss flux')
 return {'counts':True,'Gauss':True,'zero_flux':True,'binary':bool(np.all((st==0)|(st==1)))}
def advance(st,ct,seed):
 seed_rng(seed);anc=np.arange(len(st),dtype=np.int32);labels=np.full((1,len(st)),-1,dtype=np.int32)
 for _ in range(3):st,ct,anc,labels,_=prod.propagate_sweep(st,ct,anc,labels,dv,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
 return st,ct

def measure(st,ct,F,seed):
 seed_rng(seed)
 return measure_raw_block(st.copy(),ct.copy(),dv,0,F,cr,ci,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
if args.verify:
 a=prep(930000,64,prod.prepare_population);b=prep(930000,64)
 if not all(np.array_equal(a[i],b[i]) for i in range(4)):raise AssertionError('preparation derivative mismatch')
 st,ct=b[:2];keepst=st.copy();keepct=ct.copy();x=measure(st,ct,6,1930000);y=measure(st,ct,6,1930000)
 if not all(np.array_equal(x[i],y[i]) for i in range(7)):raise AssertionError('seed repeatability')
 if not(np.array_equal(st,keepst) and np.array_equal(ct,keepct)):raise AssertionError('measurement changed origin')
 u=advance(st.copy(),ct.copy(),2930000);measure(st,ct,12,1930001);v=advance(st.copy(),ct.copy(),2930000)
 if not all(np.array_equal(u[i],v[i]) for i in range(2)):raise AssertionError('suffix RNG contaminated origin advance')
 seed_rng(1930000);old=prod.measure_correlation_block(st.copy(),ct.copy(),dv,0,6,cr,ci,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
 if not np.array_equal(old[2],x[2]/x[2][0].real):raise AssertionError('raw instrumentation')
 out={'verification':{'prepare_same_state_counts_energy_ESS':True,'same_seed_repeat':True,'origin_copy':True,'advance_seed_isolation':True,'raw_matches_original':True},'postconditions':validate(x[0],x[1])}
else:
 records=[]
 for replica in range(16):
  seed=930000+10000*pi+replica
  st,ct,mc,eff,samples=prep(seed,args.population);flags=[validate(st,ct)];blocks=[]
  if args.vi==2:
   for origin in range(4):
    for fi,F in enumerate([6,12]):
     ms=1930000+100000*pi+1000*replica+10*origin+fi
     end,counts,raw,ess,survival,div,suffix=measure(st,ct,F,ms)
     flags.append(validate(end,counts))
     if np.max(abs(raw.imag))>1e-12:raise AssertionError('imaginary C0')
     blocks.append({'origin':origin,'F':F,'seed':ms,'C0_six':raw[0].real.tolist(),'raw_sums_six':(raw[0].real*args.population).tolist(),'ESS':float(ess),'survival':float(survival),'suffix':suffix.tolist()})
    if origin<3:
     st,ct=advance(st,ct,2930000+100000*pi+1000*replica+origin);flags.append(validate(st,ct))
  records.append({'replica':replica,'seed':seed,'mixed_energy':float(dv*mc),'count_samples_last40':samples.tolist(),'burn_ESS':float(eff),'postconditions':flags,'blocks':blocks})
 out={'V':V,'population':args.population,'replicas':records,'modes':modes,'burn':80,'classical':20}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384 or time.monotonic()-start>180:raise RuntimeError('resource contract')
out.update(seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(out,allow_nan=False))
