import json,hashlib
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parent
load=lambda f:json.loads((p/f).read_text(),parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
exact=load('RESULT.json');out={};internal={}
def se(x):return float(np.std(x,ddof=1)/np.sqrt(len(x)))
def ratio(B,T):
 b=float(np.mean(B));t=float(np.mean(T))
 if t<=0:return {'valid':False,'reason':'nonpositive denominator'}
 mu=.5*b/t;infl=.5/t*((B-b)-(b/t)*(T-t));return {'valid':True,'value':mu,'SE':se(infl),'influence':infl}
for pop in [1024,2048]:
 cells=[load(f'production_p{pop}_v{vi}.json') for vi in range(5)];Vs=[.93,.94,.95,.96,.97]
 for vi,c in enumerate(cells):
  assert abs(c['V']-Vs[vi])<1e-12 and c['population']==pop and len(c['replicas'])==16
  assert [r['replica'] for r in c['replicas']]==list(range(16))
  assert 0<c['rss_mib']<384 and 0<c['seconds']<180
  for r in c['replicas']:
   assert all(all(v is True for v in f.values()) for f in r['postconditions'])
   assert len(r['count_samples_last40'])==40
   assert abs(r['mixed_energy']-(c['V']-1)*np.mean(r['count_samples_last40']))<1e-12
   assert len(r['blocks'])==(8 if vi==2 else 0)
 E=np.array([[r['mixed_energy'] for r in c['replicas']] for c in cells]).T
 assert np.isfinite(E).all()
 T={F:np.array([np.mean([sum(b['C0_six']) for b in r['blocks'] if b['F']==F]) for r in cells[2]['replicas']]) for F in [6,12]}
 result={'energy_rows':[{'V':v,'mean':float(np.mean(E[:,j])),'SE':se(E[:,j]),'exact':exact['energies'][str(v)]} for j,v in enumerate(Vs)],'energy_covariance':np.cov(E,rowvar=False,ddof=1).tolist(),'moments':[]}
 values={}
 for h,minus,plus in [(.02,0,4),(.01,1,3)]:
  B=.95*(E[:,plus]-E[:,minus])/(2*h)-E[:,2]
  for F in [6,12]:
   a=ratio(B,T[F]);values[h,F]=a
   targetrow=next(x for x in exact['stencils'] if x['h']==h)
   # F12 is reported against pure denominator; exact F12 target is not claimed supplied.
   target=.5*targetrow['kinetic2']/sum(exact['S_F6_six'] if F==6 else exact['S_six'])
   row={k:v for k,v in a.items() if k!='influence'};row.update(h=h,F=F,target=target,target_scope='finite-stencil/F6' if F==6 else 'finite-stencil/pure (F12 sensitivity)',kinetic_mean=float(np.mean(B)),kinetic_SE=se(B),denominator_mean=float(np.mean(T[F])),denominator_SE=se(T[F]))
   if a['valid']:
    row.update(consistency_nominal=abs(a['value']-target)<=4*a['SE']+1e-8,precision_nominal=4*a['SE']<=.05*exact['pooled_moment'],pure_error=a['value']-exact['pooled_moment'])
   result['moments'].append(row)
 result['denominator_diagnostics']={}
 for F in [6,12]:
  block=np.array([sum(b['C0_six']) for r in cells[2]['replicas'] for b in r['blocks'] if b['F']==F])
  result['denominator_diagnostics'][str(F)]={'minimum_origin_sum':float(min(block)),'nonpositive_origin_count':int(sum(block<=0)),'minimum_replica_sum':float(min(T[F])),'nonpositive_replica_count':int(sum(T[F]<=0))}
 result['paired_sensitivities']=[]
 for name,k1,k2 in [('step',(.02,6),(.01,6)),('forward',(.02,6),(.02,12))]:
  a,b=values[k1],values[k2]
  if a['valid'] and b['valid']:
   ss=se(a['influence']-b['influence']);diff=a['value']-b['value'];result['paired_sensitivities'].append({'name':name,'difference':diff,'SE':ss,'exceeds4SE':abs(diff)>4*ss+1e-8})
 lo=.95*(E[:,4]-E[:,2])/.02-E[:,2];hi=.95*(E[:,2]-E[:,0])/.02-E[:,2]
 rl=ratio(lo,T[6]);rh=ratio(hi,T[6])
 result['noisy_concavity_endpoints']={'lower':rl.get('value'),'upper':rh.get('value'),'valid':rl['valid'] and rh['valid'],'scope':'Noisy nominal estimates, not certified bounds.'}
 out[str(pop)]=result;internal[pop]=values[.02,6]
a,b=internal[1024],internal[2048]
comparison={'valid':a['valid'] and b['valid']}
if comparison['valid']:
 comparison.update(difference=a['value']-b['value'],combined_SE=float(np.hypot(a['SE'],b['SE'])))
 comparison['exceeds4SE']=abs(comparison['difference'])>4*comparison['combined_SE']+1e-8
else:comparison['reason']='Nonpositive pooled denominator; no population ratio comparison.'
report={'populations':out,'population_comparison':comparison,'scope':'Nominal independent-replica calibration; no bias/convergence confidence theorem, gap or pole.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'PRODUCTION_ANALYSIS.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
print(json.dumps(report,indent=2,allow_nan=False))
