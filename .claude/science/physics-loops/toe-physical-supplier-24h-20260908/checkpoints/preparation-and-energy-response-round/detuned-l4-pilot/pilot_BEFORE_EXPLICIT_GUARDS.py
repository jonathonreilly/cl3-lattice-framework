import os,sys,time,signal,resource,json,argparse,hashlib,ast
from pathlib import Path
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--micro',action='store_true');ap.add_argument('--group',type=int,choices=range(3));ap.add_argument('--vi',type=int,choices=range(3));args=ap.parse_args()
if not args.micro and (args.group is None or args.vi is None):ap.error('production requires group and vi')
if args.micro and (args.group is not None or args.vi is not None):ap.error('micro is a distinct fixed workload')
signal.alarm(30 if args.micro else 180);start=time.monotonic()
sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
import numpy as np
from numba import njit
import producer_original as prod
from prepare_derivative import prepare_with_samples
from measurement_derivative import measure_raw_block
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,electric_flux,vertex_degrees
imports=time.monotonic()-start
L=4;g=prod.build_geometry(L);cr,ci,modes=prod.transverse_coefficients(L,(1,2));coeff=cr+1j*ci
@njit(cache=True)
def seed_rng(seed):np.random.seed(seed)
def validate(st,ct):
 assert np.all((st==0)|(st==1))
 assert all(prod.count_flippable(x,g.plaquette_links)==n for x,n in zip(st,ct))
 assert all(np.all(vertex_degrees(x)==3) and electric_flux(x)==(0,0,0) for x in st.reshape((-1,L,L,L,3)))
 return {'binary':True,'counts':True,'Gauss':True,'zero_flux':True}
def prep(dv,pop,burn,classical,seed):return prepare_with_samples(initial_ice(L).ravel(),dv,pop,classical,burn,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,seed)
def measure(st,ct,dv,F,seed):
 seed_rng(seed)
 return measure_raw_block(st.copy(),ct.copy(),dv,0,F,cr,ci,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
def advance(st,ct,dv,seed):
 seed_rng(seed);anc=np.arange(len(st),dtype=np.int32);labels=np.full((1,len(st)),-1,dtype=np.int32)
 for _ in range(3):st,ct,anc,labels,_=prod.propagate_sweep(st,ct,anc,labels,dv,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
 return st,ct
checks={}
def ck(name,test):
 if not bool(test):raise AssertionError(name)
 checks[name]=True
# Extract only the reviewed RK pilot's literal coefficient function; no pilot execution.
rkpath=Path('/private/tmp/toe-24h-probes-20260908/ice-spectral-moments/pilot/pilot.py')
s=rkpath.read_text();fn=next(n for n in ast.parse(s).body if isinstance(n,ast.FunctionDef) and n.name=='coefficients');ns={'np':np};exec(compile(ast.Module(body=[fn],type_ignores=[]),str(rkpath),'exec'),ns)
rkc,planes,scales,rkm=ns['coefficients'](4)
ck('all12mode_labels',modes==rkm and len(modes)==12)
ck('all2304complex_coefficients',np.max(abs(coeff-rkc))<1e-14)
ck('harmonic1_genuinely_complex',np.max(abs(coeff[:6].imag))>.1)
ck('conjugation_mutant_discriminated',np.max(abs(coeff[:6].conjugate()-rkc[:6]))>.1)
wrong=coeff.copy()
for j in range(192):wrong[:,j]*=(-1)**sum(np.unravel_index(j,(4,4,4,3))[:3])
ck('stagger_mutant_discriminated',np.max(abs(wrong-rkc))>.1)
ck('plane_mutant_discriminated',np.max(abs(coeff[0]-rkc[1]))>.1)
# Exact AST contraction of preparation instrumentation.
a=next(n for n in ast.parse((p/'producer_original.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='prepare_population')
b=next(n for n in ast.parse((p/'prepare_derivative.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='prepare_with_samples');b.name=a.name;b.body[-1].value.elts.pop()
ck('preparation_AST_only_added_samples',ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False))
if args.micro:
 t=time.monotonic();st,ct,mc,ess,samples=prep(-.05,128,8,2,4130000);prep_seconds=time.monotonic()-t;flags=validate(st,ct)
 t=time.monotonic();obs=prod.evaluate_observables(st,cr,ci);obs_first=time.monotonic()-t
 t=time.monotonic();obs2=prod.evaluate_observables(st,cr,ci);obs_hot=time.monotonic()-t
 ck('observable_literal_values',np.max(abs(obs-(st-.5)@rkc.T))<1e-12)
 flipcases=0
 for state in st[:8]:
  old=(state-.5)@coeff.T
  for f,face in enumerate(g.plaquette_links):
   if prod.is_flippable(state,face):
    new=state.copy();new[face]^=1;actual=(new-.5)@coeff.T-old;local=coeff[:,face]@(1.-2.*state[face])
    ck('signed_flip_'+str(flipcases),np.max(abs(actual-local))<1e-12)
    expected=np.array([4*np.sin(np.pi*h/4)**2/64 if planes[j]==f//64 else 0 for j,(h,a,b) in enumerate(modes)])
    ck('flip_modulus_'+str(flipcases),np.max(abs(abs(actual)**2-expected))<1e-12);flipcases+=1
 t=time.monotonic();blocks=[]
 for fi,F in enumerate([12,24]):
  end,counts,raw,ef,surv,div,suffix=measure(st,ct,-.05,F,4130001+fi);validate(end,counts)
  ck('C0_real_'+str(F),np.max(abs(raw.imag))<1e-12)
  blocks.append({'F':F,'raw_C0':raw[0].real.tolist(),'ESS':float(ef),'survival':float(surv)})
 suffix_seconds=time.monotonic()-t
 # Forecast uses measured whole suffix time as a conservative per-population/sweep proxy,
 # not a claimed isolated update cost; cold preparation/JIT is charged once per cell.
 unit=suffix_seconds/(128*36);forecasts=[]
 for gi,(P,B) in enumerate([(512,160),(1024,160),(1024,320)]):
  for vi in range(3):
   hot=P*8*(20+B+(4*36+9 if vi==1 else 0))*unit
   forecasts.append({'group':gi,'vi':vi,'seconds_with_50pct_headroom':1.5*(imports+prep_seconds+hot)})
 total=sum(x['seconds_with_50pct_headroom'] for x in forecasts)
 out={'mode':'micro_NOT_physics_estimate','checks':checks,'visited_flip_cases':flipcases,'postconditions':flags,'timing':{'imports':imports,'preparation_including_first_JIT':prep_seconds,'first_observable_including_JIT':obs_first,'hot_observable':obs_hot,'whole_suffix_pair_not_isolated_kernel':suffix_seconds},'blocks':blocks,'mixed_origin_means_real':obs.mean(0).real.tolist(),'mixed_origin_means_imag':obs.mean(0).imag.tolist(),'forecast':forecasts,'forecast_total':total,'forecast_gate':max(x['seconds_with_50pct_headroom'] for x in forecasts)<=120 and total<=500,'forecast_scope':'Heuristic uses actual suffix overhead; not a runtime guarantee. No production authorization inferred.'}
else:
 gi=args.group;vi=args.vi;P,B=[(512,160),(1024,160),(1024,320)][gi];V=[.93,.95,.97][vi];dv=V-1;records=[]
 for rep in range(8):
  seed=1030000+10000*gi+rep;st,ct,mc,eff,samples=prep(dv,P,B,20,seed);flags=[validate(st,ct)];blocks=[]
  if vi==1:
   for origin in range(4):
    means=prod.evaluate_observables(st,cr,ci).mean(0)
    for fi,F in enumerate([12,24]):
     ms=2030000+100000*gi+1000*rep+10*origin+fi
     end,counts,raw,ef,surv,div,suffix=measure(st,ct,dv,F,ms);flags.append(validate(end,counts));assert np.max(abs(raw.imag))<1e-12
     blocks.append({'origin':origin,'F':F,'seed':ms,'C0_12':raw[0].real.tolist(),'raw_sums_12':(P*raw[0].real).tolist(),'mixed_origin_mean_real':means.real.tolist(),'mixed_origin_mean_imag':means.imag.tolist(),'ESS':float(ef),'survival':float(surv),'suffix':suffix.tolist()})
    if origin<3:st,ct=advance(st,ct,dv,3030000+100000*gi+1000*rep+origin);flags.append(validate(st,ct))
  records.append({'replica':rep,'seed':seed,'mixed_energy':float(dv*mc),'count_samples_last40':samples.tolist(),'half_window_energy':[float(dv*np.mean(samples[:20])),float(dv*np.mean(samples[20:]))],'burn_ESS':float(eff),'postconditions':flags,'blocks':blocks})
 out={'mode':'production','L':4,'group':gi,'V':V,'population':P,'burn':B,'modes':modes,'checks':checks,'replicas':records}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-start
if not 0<rss<384 or elapsed>(30 if args.micro else 180):raise RuntimeError('resource envelope')
out.update(elapsed_seconds=elapsed,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rk_source_sha256=hashlib.sha256(rkpath.read_bytes()).hexdigest())
print(json.dumps(out,allow_nan=False))
