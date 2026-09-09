"""DATA-only accepted family; no histories or selected coefficients."""
import json,math
from pathlib import Path
from fractions import Fraction as F
import pilot_binder,action_binder
sha=pilot_binder.sha

def load(plan):
 if plan['status']!='ROOT_REVIEWED_COORDINATE_FREE_DATA':raise ValueError('NOTREADY')
 pins=plan['inputs']
 def read(p):
  if p not in pins or sha(p)!=pins[p]:raise ValueError('bound input')
  return json.loads(Path(p).read_text())
 for p,h in pins.items():
  if sha(p)!=h:raise ValueError('input closure '+p)
 family=read(plan['original_family_binding'])
 for p,h in family['inputs'].items():
  if pins.get(p)!=h:raise ValueError('family closure')
 cp,ap,radii=pilot_binder.load(family)
 data=read(plan['data_binding']);data['status']='ROOT_REVIEWED_FIRST_ACTION_APPEND'
 for p,h in data['inputs'].items():
  if pins.get(p)!=h:raise ValueError('DATA closure')
 poles,values,alpha,c,mu,old,physical=action_binder.load(data)
 d=plan['data'];post=read(d['post']);root=read(d['root']);result=read(d['result']);worker=read(d['worker']);runtime=read(d['runtime'])
 if post['status']!='ACCEPTED_FIRST_ACTION_DATA_AND_ALL_SAVED_ENTRIES' or post['original_root_acceptance_sha256']!=sha(d['root']) or post['result_sha256']!=sha(d['result']):raise ValueError('DATA POST')
 if root['status']!='ACCEPTED_FIRST_ACTION_DATA_APPEND_MIDPOINT_ARITHMETIC' or root['result_sha256']!=sha(d['result']) or root['worker_freeze']!=sha(d['runtime']):raise ValueError('DATA root')
 if worker['result_sha256']!=sha(d['result']) or worker['freeze_sha256']!=sha(d['runtime']):raise ValueError('DATA worker')
 for p,h in runtime['inputs'].items():
  if pins.get(p)!=h:raise ValueError('DATA full source')
 read(post['post_result_path'])
 if sha(post['post_result_path'])!=post['post_result_sha256']:raise ValueError('DATA saved result')
 for x in (root['external_seconds'],worker['seconds']):
  if type(x)not in(int,float) or not math.isfinite(x) or not 0<x<=30:raise ValueError('DATA time')
 for x in(root['sampled_whole_tree_peak'],worker['rss_bytes']):
  if type(x)is not int or not 0<x<=384*1048576:raise ValueError('DATA RSS')
 if result['entries']!=6015 or result['rows']!=2010 or len(result['orbits'])!=5 or result['append_sha256']!=sha(d['stream']):raise ValueError('DATA census')
 if result['physical_input_metadata']!=physical:raise ValueError('same mu metadata')
 if data['append_binding']!=family['append_binding']:raise ValueError('same Ward/cache family')
 # Action binder and original pilot binder obtain alpha from the SAME accepted
 # Ward/cache binding above, no replacement Gauss root/pi family.
 return cp,ap,d['stream'],radii,poles,alpha,F(physical['eta_mu'])
