"""Portable metadata and synthetic algebra only; no native arrays or Wick imports."""
import json,hashlib,math,pathlib,copy
from fractions import Fraction as F
D=pathlib.Path(__file__).resolve().parent
H=lambda b:hashlib.sha256(b).hexdigest()
def need(x):
 if not x:raise ValueError('packet validation failed')
def integer(x,n):need(type(x) is int and x==n)
def seconds(x,cap):need(type(x) in (int,float) and math.isfinite(x) and 0<x<cap)
def rss(x):need(type(x) is int and 0<x<=384*1024**2)
def validate(tag,b):
 o={k:json.loads(v) for k,v in b.items()};r=o['RESULT'];a=o['ROOT_ACCEPTANCE'];w=o['WORKER_COMPLETE'];e=o['RECEIPT'];s=o['SCHEMA_ACCEPTANCE'];rf=o['ROOT_FREEZE']
 need(a['status']==('ACCEPTED_NEW_SPECTRAL_RESIDUAL_ESTIMATOR_ONCE' if tag=='spectral-residual' else 'ACCEPTED_NEW_NATIVE_'+tag.upper().replace('-','_')+'_ROOT_REVIEW_ONCE'));need(a['once'] is True)
 need(a['result_sha256']==w['result_sha256']==s['result_sha256']==H(b['RESULT']))
 need(a['worker_freeze']==w['runtime_sha256']==e['worker_freeze']==rf['worker_freeze']==H(b['RUNTIME_FREEZE']))
 need(a['root_freeze']==H(b['ROOT_FREEZE']));need(a['schema_sha256']==H(b['SCHEMA_ACCEPTANCE']));need(a['schema']==s)
 need(w['binding_sha256']==H(b['BINDING']));need(e['pass'] is True and e['failure'] is None);integer(e['returncode'],0)
 for x,cap in [(r['seconds'],29 if tag=='spectral-residual' else 19),(w['seconds'],29 if tag=='spectral-residual' else 19),(e['seconds'],29.5 if tag=='spectral-residual' else 19.5),(a['external_seconds'],30 if tag=='spectral-residual' else 20)]:seconds(x,cap)
 need(r['seconds']<=w['seconds']<=e['seconds']<=a['external_seconds'])
 for x in [w['rss_bytes'],e['sampled_whole_tree_peak'],a['sampled_whole_tree_peak'],a['external_rss_bytes']]:rss(x)
 need(e['sampled_whole_tree_peak']==a['sampled_whole_tree_peak']);integer(r['choices'],2);need(len(r['rows'])==2)
 need([x['mode'] for x in r['rows']]==['residual','variational']);need(all(x['status']=='INDETERMINATE_SIGN' for x in r['rows']))
 if tag=='spectral-residual':
  need(r['status']=='COMPLETE_NEW_SPECTRAL_RESIDUAL_ESTIMATOR');need(w['status']=='COMPLETE_NEW_SPECTRAL_RESIDUAL_ONLY');integer(r['events'],588);integer(s['events'],588);integer(r['max_new_source_moments'],8)
  for key in ['native_oracle_calls','s0_s2_recomputed','vacuum_moments_recomputed']:integer(r[key],0)
  need(s['status']=='ACCEPTED_NEW_SPECTRAL_RESIDUAL_SCHEMA')
  for key in ['independent_residual_majorant_posterior_arithmetic','new_s3_s4_wick_truth_inherited','old_moment_truth_inherited']:need(s[key] is True)
 elif tag=='degree20-ward':
  need(r['status']=='COMPLETE_FIXED_DEGREE20_CERTIFICATE');need(w['status']=='COMPLETE_NEW_DEGREE20_ONLY');integer(r['events'],255);integer(r['oracle_calls'],0);integer(r['new_covariance_calls'],0);need(r['sign_certified'] is False)
 else:
  need(r['status']=='COMPLETE_NEW_POSTERIOR_WARD_ESTIMATOR');need(w['status']=='COMPLETE_NEW_POSTERIOR_ONLY');integer(r['source_events'],205 if tag=='degree10-posterior' else 255);integer(r['old_moments_recomputed'],0);need(r['new_error_estimator'] is True)
 return True
def encode(x):return json.dumps(x,sort_keys=True).encode()
def mutate_result(b,edit):
 b=copy.deepcopy(b);r=json.loads(b['RESULT']);edit(r);b['RESULT']=encode(r)
 for k in ['WORKER_COMPLETE','SCHEMA_ACCEPTANCE']:
  o=json.loads(b[k]);o['result_sha256']=H(b['RESULT']);b[k]=encode(o)
 a=json.loads(b['ROOT_ACCEPTANCE']);a['result_sha256']=H(b['RESULT']);a['schema']=json.loads(b['SCHEMA_ACCEPTANCE']);a['schema_sha256']=H(b['SCHEMA_ACCEPTANCE']);b['ROOT_ACCEPTANCE']=encode(a);return b
def reject(fn):
 try:fn()
 except ValueError:return
 raise AssertionError('mutant accepted')
def main():
 pins=json.loads((D/'PACKET_INPUTS.json').read_text())
 for p,m in pins.items():need(H((D/p).read_bytes())==m['sha256'])
 checks=0
 for tag in ['degree20-ward','degree10-posterior','degree20-posterior','spectral-residual']:
  b={p.stem:p.read_bytes() for p in (D/'evidence'/tag).glob('*.json')};validate(tag,b);checks+=1
  for edit in [lambda r:r.update(choices=True),lambda r:r['rows'][0].update(status='CERTIFIED_POSITIVE'),lambda r:r.update(seconds=False)]:reject(lambda:validate(tag,mutate_result(b,edit)));checks+=1
  q=copy.deepcopy(b);a=json.loads(q['ROOT_ACCEPTANCE']);a['once']=False;q['ROOT_ACCEPTANCE']=encode(a);reject(lambda:validate(tag,q));checks+=1
 # Exact inverse-square majorant identity, all numbers synthetic.
 for delta,tau,lam in [(F(1,4),F(2),F(3)),(F(1),F(3,2),F(2))]:
  A=(tau+2*delta)/(delta**2*tau**3);Q=(3*tau-2*lam)/tau**3+A*(lam-tau)**2
  rhs=(lam-delta)*(lam-tau)**2*((tau+2*delta)*lam+delta*tau)/(delta**2*tau**3*lam**2)
  need(Q-1/lam**2==rhs);reject(lambda:need(Q+F(1,7)-1/lam**2==rhs));checks+=2
 # Posterior mixed bounds derive from two different telescoping orders.
 E,Fv,a,b,chi,psi=map(F,[2,3,5,7,6,8]);x=E*b+chi*Fv;y=E*psi+a*Fv
 need(min(x,y)<=x and min(x,y)<=y);reject(lambda:need(max(x,y)==min(x,y)));checks+=2
 return {'status':'PASS_COMPACT_METADATA_AND_SYNTHETIC_ONLY','checks':checks,'native_replay':False,'spectral_outcome':'ACCEPTED_EXECUTION_BOTH_INDETERMINATE_SIGN'}
if __name__=='__main__':print(json.dumps(main(),indent=2))
