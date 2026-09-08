import json,hashlib
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parent
load=lambda f:json.loads((p/f).read_text(),parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def se(x):return float(np.std(x,ddof=1)/np.sqrt(len(x)))
def ratio(B,T):
 b=float(np.mean(B));t=float(np.mean(T))
 if t<=0:return {'valid':False,'reason':'nonpositive pooled source derivative'}
 infl=.5/t*((B-b)-(b/t)*(T-t))
 return {'valid':True,'value':.5*b/t,'SE':se(infl),'influence':infl}
exact=load('RESULT.json');out={};primary={};cases=[(.93,0.),(.95,0.),(.97,0.),(.95,-.02),(.95,.02),(.95,-.01),(.95,.01)]
for pi,pop in enumerate([1024,2048]):
 cells=[load(f'production_p{pop}_c{c}.json') for c in range(7)]
 for k,c in enumerate(cells):
  assert (c['V'],c['lambda'])==cases[k] and c['population']==pop and c['shift']==12*abs(c['lambda'])
  assert len(c['replicas'])==16 and 0<c['seconds']<180 and 0<c['rss_mib']<384
  for r,rep in enumerate(c['replicas']):
   assert rep['replica']==r and rep['seed']==3400000+10000*pi+r and rep['postconditions'] is True
   assert len(rep['Nf_window'])==len(rep['X_window'])==len(rep['energy_window'])==40
   expected=(c['V']-1)*np.array(rep['Nf_window'])+c['lambda']*np.array(rep['X_window'])
   assert np.max(abs(expected-rep['energy_window']))<1e-12 and abs(np.mean(expected)-rep['physical_energy'])<1e-12
   assert abs(rep['shifted_energy']+c['shift']-rep['physical_energy'])<1e-12 and rep['cache_drift']<1e-10
 E=np.array([[r['physical_energy'] for r in c['replicas']] for c in cells]).T;assert np.isfinite(E).all()
 B=.95*(E[:,2]-E[:,0])/.04-E[:,1];rows=[];values={}
 for h,minus,plus in [(.02,3,4),(.01,5,6)]:
  T=(E[:,plus]-E[:,minus])/(2*h);a=ratio(B,T);values[h]=a;target=next(x['moment_two_response'] for x in exact['two_response_moments'] if x['source_h']==h);pure=exact['two_response_moments'][0]['pure_moment']
  row={k:v for k,v in a.items() if k!='influence'};row.update(h=h,kinetic_mean=float(np.mean(B)),kinetic_SE=se(B),source_derivative_mean=float(np.mean(T)),source_derivative_SE=se(T),minimum_replica_T=float(min(T)),nonpositive_replica_T=int(sum(T<=0)),negative_replica_B=int(sum(B<0)),exact_finite_stencil=target,pure_target=pure)
  if a['valid']:row.update(consistency_nominal=abs(a['value']-target)<=4*a['SE']+1e-8,precision_nominal=4*a['SE']<=.05*pure,pure_error=a['value']-pure)
  rows.append(row)
 a,b=values[.02],values[.01];sensitivity={'valid':a['valid'] and b['valid']}
 if sensitivity['valid']:
  diff=a['value']-b['value'];ss=se(a['influence']-b['influence']);sensitivity.update(difference=diff,SE=ss,exceeds4SE=abs(diff)>4*ss+1e-8)
 out[str(pop)]={'energy_means':np.mean(E,axis=0).tolist(),'energy_SE':(np.std(E,axis=0,ddof=1)/4).tolist(),'energy_sample_covariance':np.cov(E,rowvar=False,ddof=1).tolist(),'moments':rows,'paired_step_sensitivity':sensitivity};primary[pop]=values[.02]
a,b=primary[1024],primary[2048];comparison={'valid':a['valid'] and b['valid']}
if comparison['valid']:
 diff=a['value']-b['value'];ss=float(np.hypot(a['SE'],b['SE']));comparison.update(difference=diff,SE=ss,exceeds4SE=abs(diff)>4*ss+1e-8)
report={'populations':out,'population_comparison':comparison,'scope':'nominal finite-replica energy-response calibration, no rigorous bias/mixing/pole guarantee','analysis_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'PRODUCTION_ANALYSIS.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,indent=2,allow_nan=False))
