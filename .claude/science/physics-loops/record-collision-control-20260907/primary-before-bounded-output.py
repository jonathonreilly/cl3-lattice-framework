#!/usr/bin/env python3
"""Exact-rational collision certificate and strict live native witness binding."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,math,hashlib,subprocess,sys,time,signal,resource,copy
from pathlib import Path
from fractions import Fraction as F
signal.alarm(180)
start=time.monotonic()
ROOT=Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS=('scripts/native_edge_record_finite_collision_check_2026_09_07.py','scripts/native_edge_record_autonomous_head_native_ladder_check_2026_09_07.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok,label):
 if not ok:raise AssertionError(label)
def unique(pairs):
 d={}
 for k,v in pairs:
  require(k not in d,'duplicate JSON key');d[k]=v
 return d
def reject(x):raise ValueError('nonfinite JSON '+x)
def finite(x):
 if isinstance(x,float):require(math.isfinite(x),'nonfinite')
 elif isinstance(x,dict):
  for v in x.values():finite(v)
 elif isinstance(x,list):
  for v in x:finite(v)
def keys(d,ks):require(type(d) is dict and set(d)==set(ks),'schema')
def same_typed(a,b):
 if type(a) is not type(b):return False
 if isinstance(a,dict):return set(a)==set(b) and all(same_typed(a[k],b[k]) for k in a)
 if isinstance(a,list):return len(a)==len(b) and all(same_typed(x,y) for x,y in zip(a,b))
 return a==b
def num(x):return type(x) in (int,float) and math.isfinite(x)
def bounded(x,a,b):return num(x) and a<=x<b
FIX=['original_commuting_fixture','separately_preregistered_noncommuting_supplement']
def validate(d,hashes):
 finite(d)
 keys(d,FIX+['parameters','source_sha256','dependencies','resources','seconds','rss_MiB','discriminator','scope'])
 require(d['source_sha256']==hashes[AUDIT_INPUT_PATHS[0]],'helper identity')
 require(d['dependencies']=={AUDIT_INPUT_PATHS[1]:hashes[AUDIT_INPUT_PATHS[1]]},'dependency identity')
 require(same_typed(d['resources'],dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1)),'resource schema')
 require(bounded(d['seconds'],0,180) and bounded(d['rss_MiB'],0,180),'resources')
 require(type(d['scope']) is str and type(d['discriminator']) is str,'scope type')
 p=d['parameters'];keys(p,['hopping01','hopping23','fuel_delta','gamma','battery_centers','cap','grid_spacing','particle_number','state','refusal_numerical_null_cutoff'])
 expected=dict(hopping01=1.,hopping23=math.sqrt(2)/3,fuel_delta=1.,gamma=1.,battery_centers=[.5,1.5,2.5],cap=3.,grid_spacing=1.,particle_number=2,state='original source ground state pulsed by exp[-i(.37 n0+.23 n2)], uniform real battery superposition',refusal_numerical_null_cutoff=1e-10)
 require(same_typed(p,expected),'fixture parameters')
 for idx,name in enumerate(FIX):
  f=d[name];keys(f,['checks','worst','system_dimension','unitary_dimension','rows','original_jump_commutator','refusal_probability','seconds','rss_MiB','source_sha256','deleted_edge','noncommuting_control_detected'])
  for k,v in [('checks',18),('system_dimension',72),('unitary_dimension',288),('deleted_edge',2*idx)]:require(type(f[k]) is int and f[k]==v,k)
  require(type(f['noncommuting_control_detected']) is bool and f['noncommuting_control_detected']==bool(idx),'true/false discriminator')
  require(f['source_sha256']==d['source_sha256'],'fixture source')
  require(bounded(f['worst'],0,2e-10) and bounded(f['seconds'],0,180) and bounded(f['rss_MiB'],0,180),'fixture resources/residual')
  comm=f['original_jump_commutator'];require(num(comm) and (abs(comm-1/3)<1e-10 if idx else abs(comm)<1e-10),'commutator contrast')
  ref=f['refusal_probability'];require(num(ref) and (abs(ref-1/3)<1e-10 if idx else .02<ref<.03),'nonzero refusal')
  require(type(f['rows']) is list and len(f['rows'])==3,'row coverage')
  for row,h in zip(f['rows'],[.04,.02,.01]):
   keys(row,['h','dissipative_trace_norm_error','split_full_trace_norm_error'])
   require(type(row['h']) is float and row['h']==h,'h order/coverage')
   a=row['dissipative_trace_norm_error'];b=row['split_full_trace_norm_error']
   require(bounded(a,0,6*h*h) and a>0 and bounded(b,0,8*h*h),'local bounds')
   require(b>a*1.01 if idx else abs(a-b)<1e-10,'split contrast')
  for k in ['dissipative_trace_norm_error','split_full_trace_norm_error']:
   vals=[r[k] for r in f['rows']]
   require(all(3.5<a/b<4.5 for a,b in zip(vals,vals[1:])),'h squared scaling')

# All certificate calculations below are independent of helper results.
checks=0
def exact(ok):
 global checks
 require(ok,'rational certificate');checks+=1
delta=F(1,320);lam=F(3);T=F(1);eps=F(1,100)
# ad_D <= delta; L <= 2 Lambda; commutator <= 2 delta*2Lambda.
comm=2*delta*(2*lam);split=comm/2
exact(comm==4*delta*lam);exact(split==2*delta*lam)
c=6*lam**2+split;n=math.ceil(max(4*lam*T,c*T*T/eps))
exact(c==F(8643,160));exact(n==5402);exact(T*lam/n<=F(1,4))
exact(c*T*T/n==F(8643,864320));exact(c*T*T/n<eps)
exact(24*(2+1)==72);exact(2**6<73<=2**7);exact(48+7*n==37862)
exact(F(221,2240)+eps==F(1217,11200))
# Elementary series certificates: e^.5<2 via term ratio <=1/4 after k=1;
# cosh1<2 via even-term ratio <=1/12 after k=1.
ehalf_upper=1+F(1,2)/(1-F(1,4));cosh_upper=1+F(1,2)/(1-F(1,12))
exact(ehalf_upper<2);exact(cosh_upper<2);exact(F(2,3)*cosh_upper+2*ehalf_upper<6)
hashes={p:sha(ROOT/p) for p in AUDIT_INPUT_PATHS}
env=dict(os.environ);env['PYTHONPATH']=str(ROOT/'scripts')
proc=subprocess.run([sys.executable,str(ROOT/AUDIT_INPUT_PATHS[0]),'--json'],capture_output=True,text=True,env=env,timeout=170)
require(proc.returncode==0,'helper failed: '+proc.stderr[-1500:]);require(not proc.stderr.strip(),'helper stderr')
d=json.loads(proc.stdout,object_pairs_hook=unique,parse_constant=reject)
require(hashes=={p:sha(ROOT/p) for p in AUDIT_INPUT_PATHS},'dependency changed during run')
validate(d,hashes)
mutations=[]
def mutation(name,fn):
 x=copy.deepcopy(d);fn(x)
 try:validate(x,hashes)
 except (AssertionError,ValueError,TypeError,KeyError):mutations.append(name);return
 raise AssertionError('undetected mutation '+name)
mutation('dropped row',lambda x:x[FIX[0]]['rows'].pop())
mutation('NaN error',lambda x:x[FIX[0]]['rows'][0].update(dissipative_trace_norm_error=float('nan')))
mutation('Inf residual',lambda x:x[FIX[0]].update(worst=float('inf')))
mutation('swapped fixtures',lambda x:x.update({FIX[0]:x[FIX[1]],FIX[1]:x[FIX[0]]}))
mutation('false original claim',lambda x:x[FIX[0]].update(noncommuting_control_detected=True))
mutation('wrong supplement commutator',lambda x:x[FIX[1]].update(original_jump_commutator=0.))
mutation('wrong energy residual',lambda x:x[FIX[1]].update(worst=.01))
mutation('wrong error',lambda x:x[FIX[1]]['rows'][0].update(split_full_trace_norm_error=1.))
mutation('wrong hash',lambda x:x.update(source_sha256='0'*64))
mutation('wrong resource',lambda x:x['resources'].update(blas_threads=2))
for bad in ['{"a":1,"a":2}','{"a":NaN}','{"a":Infinity}']:
 try:json.loads(bad,object_pairs_hook=unique,parse_constant=reject)
 except (AssertionError,ValueError):mutations.append('strict JSON '+bad);continue
 raise AssertionError('parser accepted malformed JSON')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-start
require(rss<180 and elapsed<180,'primary resources')
result=dict(certificate=dict(delta=str(delta),Lambda=str(lam),T=str(T),collision_budget=str(eps),local_coefficient=str(c),collisions=n,collision_upper=str(c/n),ancilla_qubits_per_collision=7,total_storage_plus_ancilla_qubits=48+7*n,separate_finite_battery_upper='221/2240',combined_upper='1217/11200',commutator_upper=str(comm),splitting_coefficient=str(split)),rational_assertions=checks,malformed_controls=mutations,native_witness=d,dependencies=hashes,source_sha256=sha(Path(__file__)),resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),seconds=elapsed,rss_MiB=rss)
if '--json' in sys.argv:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS finite collision rational certificate and fresh native matrix witness')
 print('per_element: accepted signs and one refusal are bound to the live native helper; original false discriminator is preserved.')
 print('per_site: native square evidence is separate from the cube48-register storage certificate.')
 print('per_mode: actual free F differs from conserved K; commutator/splitting constants verified exactly.')
 print('per_block:5402 collisions,7 fresh ancillary qubits each,37862 storage-plus-ancilla qubits; separate combined budget1217/11200.')
 print('lattice_wide: not executed; clock, preparation, global jump synthesis and nearest-neighbor realization remain supplied.')
 print('CHECKS',checks,'rational;',len(mutations),'malformed controls; native18 per fixture')
 print('SOURCE_SHA256',result['source_sha256']);print('DEPENDENCIES',json.dumps(hashes,sort_keys=True))
 print('RESOURCES',elapsed,rss,'seconds/MiB;180 limits, BLAS1')
 print('TOTAL: PASS FAIL=0')
