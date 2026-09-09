"""NOTREADY: accepted-source binder design; import performs no data loading."""
import json,math
from pathlib import Path
from fractions import Fraction as F
import append_binder
sha=append_binder.sha

def load(plan):
 if plan.get('status')!='ROOT_REVIEWED_FIRST_ACTION_APPEND':raise ValueError('NOTREADY: independent source/runtime review required')
 pins=plan['inputs']
 def read(path):
  if path not in pins or sha(path)!=pins[path]:raise ValueError('input pin '+path)
  return json.loads(Path(path).read_text())
 for path,digest in pins.items():
  if sha(path)!=digest:raise ValueError('input closure')
 app=read(plan['append_binding'])
 for path,digest in app['inputs'].items():
  if pins.get(path)!=digest:raise ValueError('transitive scalar closure')
 poles,values,alpha,a0,c,_=append_binder.load(app)
 def accepted(role,status):
  d=plan[role];post=read(d['post']);root=read(d['root']);result=read(d['result']);worker=read(d['worker'])
  if post['status']!=status or post['original_root_acceptance_sha256']!=sha(d['root']) or post['result_sha256']!=sha(d['result']):raise ValueError('post acceptance '+role)
  if root['status']!=d['root_status'] or root['result_sha256']!=sha(d['result']) or root['worker_freeze']!=d['worker_freeze']:raise ValueError('root acceptance '+role)
  runtime=read(d['runtime'])
  if sha(d['runtime'])!=d['worker_freeze'] or runtime['inputs'].get(d['binding'])!=sha(d['binding']):raise ValueError('runtime binding '+role)
  field='freeze_sha256' if role=='ward' else 'runtime_sha256'
  if worker['result_sha256']!=sha(d['result']) or worker[field]!=d['worker_freeze']:raise ValueError('worker binding '+role)
  if role=='ward' and worker['binding_sha256']!=sha(d['binding']):raise ValueError('ward binding')
  if worker['status']!=d['worker_status'] or result['status']!=d['result_status']:raise ValueError('completed science '+role)
  read(post['post_result_path'])
  if post['post_result_sha256']!=sha(post['post_result_path']):raise ValueError('saved reconciliation')
  for value,cap in ((root['external_seconds'],30),(root['sampled_whole_tree_peak'],384*1048576),(worker['seconds'],30),(worker['rss_bytes'],384*1048576)):
   if type(value) not in (int,float) or not math.isfinite(value) or not 0<value<=cap:raise ValueError('accepted resources')
  return result
 old=accepted('ward','ACCEPTED_WARD_APPEND_EXECUTION_AND_ALL_SAVED_ENTRIES')
 if plan['ward']['binding']!=plan['append_binding'] or old['entries']!=5970 or old['rows']!=1995 or len(old['orbits'])!=5:raise ValueError('original798 source identity')
 murow=accepted('mu','ACCEPTED_MU_EXECUTION_AND_SAVED_RECONCILIATION')
 if len(murow['interval'])!=2:raise ValueError('mu shape')
 lo,hi=map(F,murow['interval']);eta=(hi-lo)/2
 if not 0<lo<=hi or eta>F(1,10**19) or hi>=4:raise ValueError('mu radius/normalization')
 return poles,values,alpha,c,(lo+hi)/2,old,{'eta_mu':str(eta),'mu_interval':murow['interval']}
