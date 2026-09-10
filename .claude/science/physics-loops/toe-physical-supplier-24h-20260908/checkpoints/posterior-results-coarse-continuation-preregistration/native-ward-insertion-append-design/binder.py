"""Future binder. No acceptance guessed; current BINDING remains NOTREADY."""
import json
from pathlib import Path
from fractions import Fraction as F
import cache_binder
sha=cache_binder.sha
ROLES=('common_cache','a0','cminus')
def load(plan):
 if plan.get('status')!='ACCEPTED_APPEND_INPUTS_BOUND':raise ValueError('NOTREADY: accepted common cache and cminus bindings required')
 pins=plan['inputs']
 def read(path):
  if path not in pins or sha(path)!=pins[path]:raise ValueError('input pin '+str(path))
  return json.loads(Path(path).read_text())
 for path,h in pins.items():
  if sha(path)!=h:raise ValueError('input closure')
 # Future reviewed descriptors bind literal acceptance status and its result-hash field.
 # They may only be populated after actual formats and acceptances exist.
 for role in ROLES:
  d=plan['roles'][role]
  if not d['accepted_status'] or not d['result_hash_key']:raise ValueError('missing reviewed acceptance descriptor')
  accept=read(d['acceptance']);result=read(d['result'])
  if accept.get('status')!=d['accepted_status'] or accept.get(d['result_hash_key'])!=sha(d['result']):raise ValueError('accepted '+role)
  if role!='common_cache':
   obj=result
   for key in d['interval_path']:obj=obj[key]
   if len(obj)!=2:raise ValueError('scalar interval')
   lo,hi=map(F,obj);cap=F(2,10**30) if role=='a0' else F(2,10**19)
   if not 0<lo<=hi or hi-lo>cap:raise ValueError('scalar radius')
   if role=='a0':a0=(lo+hi)/2
   else:c=(lo+hi)/2
 if a0>F(17,60) or c>F(7,15):raise ValueError('scalar normalization h=1')
 pole_plan=read(plan['pole_binding']);poles,values,alpha=cache_binder.load(pole_plan)
 for path,h in pole_plan['inputs'].items():
  if pins.get(path)!=h:raise ValueError('transitive pole closure')
 for role in ('cache_rows','cache_coefficients'):
  if plan[role] not in pins:raise ValueError('missing saved artifact pin')
 result=read(plan['roles']['common_cache']['result'])
 if result['status']!='COMPLETE_COMMON_CACHE_MIDPOINT_ARITHMETIC' or result['entries']!=52536 or result['coefficients']!=132:raise ValueError('cache result census')
 if result['cache_sha256']!=sha(plan['cache_rows']) or result['coefficient_sha256']!=sha(plan['cache_coefficients']):raise ValueError('saved cache data binding')
 # Cache original worker must bind the same exact pole plan, not just similar values.
 worker=read(plan['cache_worker'])
 if worker['binding_sha256']!=sha(plan['pole_binding']) or worker['result_sha256']!=sha(plan['roles']['common_cache']['result']):raise ValueError('cache source identity')
 if len(result['orbits'])!=5:raise ValueError('orbit census')
 return poles,values,alpha,a0,c,result
