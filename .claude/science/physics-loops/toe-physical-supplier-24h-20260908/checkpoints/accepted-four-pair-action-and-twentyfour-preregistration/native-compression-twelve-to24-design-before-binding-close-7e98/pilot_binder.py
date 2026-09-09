"""Saved-scalar/input checks only; no entry, index, oracle or pivot construction."""
import json,math
from pathlib import Path
from fractions import Fraction as F
import append_binder
sha=append_binder.sha

def load(plan):
 pins=plan['inputs']
 def read(path):
  if path not in pins or sha(path)!=pins[path]:raise ValueError('bound input '+path)
  return json.loads(Path(path).read_text())
 for path,digest in pins.items():
  if sha(path)!=digest:raise ValueError('input changed '+path)
 app=read(plan['append_binding'])
 for path,digest in app['inputs'].items():
  if pins.get(path)!=digest:raise ValueError('append closure')
 poles,values,alpha,a0,c,cache_result=append_binder.load(app)
 post=read(plan['append_post']);root=read(plan['append_root']);result=read(plan['append_result']);w=read(plan['append_worker'])
 if post['status']!='ACCEPTED_WARD_APPEND_EXECUTION_AND_ALL_SAVED_ENTRIES' or post['result_sha256']!=sha(plan['append_result']) or post['original_root_acceptance_sha256']!=sha(plan['append_root']):raise ValueError('append post acceptance')
 if post['post_result_sha256']!=sha(post['post_result_path']) or post['post_result_path'] not in pins:raise ValueError('post result')
 if root.get('status')!='ACCEPTED_WARD_APPEND_MIDPOINT_ARITHMETIC' or w.get('status')!='COMPLETE_APPEND_MIDPOINT_ONLY':raise ValueError('execution receipt status')
 for value,cap in ((root['external_seconds'],30),(root['sampled_whole_tree_peak'],384*1048576),(w['seconds'],30),(w['rss_bytes'],384*1048576)):
  if type(value) not in (int,float) or not math.isfinite(value) or not 0<value<=cap:raise ValueError('accepted resources')
 if root['result_sha256']!=sha(plan['append_result']) or root['worker_freeze']!=plan['append_runtime_sha256']:raise ValueError('root binding')
 if w['binding_sha256']!=sha(plan['append_binding']) or w['result_sha256']!=sha(plan['append_result']) or w['freeze_sha256']!=plan['append_runtime_sha256']:raise ValueError('worker binding')
 if result['status']!='COMPLETE_APPEND_MIDPOINT_ARITHMETIC' or result['entries']!=5970 or result['rows']!=1995:raise ValueError('append census')
 if sha(plan['append_rows'])!=post['append_sha256'] or sha(app['cache_rows'])!=cache_result['cache_sha256']:raise ValueError('raw identity')
 poleplan=read(app['pole_binding']);arows=read(poleplan['a_result'])['rows'];brows=read(poleplan['summary'])['rows']
 def radius(x):
  if len(x)!=2:raise ValueError('interval shape')
  lo,hi=map(F,x)
  if lo>hi:raise ValueError('interval order')
  return (hi-lo)/2
 etaA=max(radius(r['oracle'][k]) for r in arows for k in ('A','Aprime'))
 etaB=max(radius(r[k]) for r in brows for k in ('B','Bprime'))
 def scalar(role):
  d=app['roles'][role];obj=read(d['result'])
  for key in d['interval_path']:obj=obj[key]
  return radius(obj)
 radii=dict(etaA=etaA,etaB=etaB,etac=scalar('cminus'),etaa0=scalar('a0'),alpha_max=max(alpha))
 if not 0<radii['alpha_max']<=12 or etaA>F(1,10**30) or etaB>F(1,10**19) or radii['etac']>F(1,10**19) or radii['etaa0']>F(1,10**30):raise ValueError('physical radius budget')
 return app['cache_rows'],plan['append_rows'],radii
