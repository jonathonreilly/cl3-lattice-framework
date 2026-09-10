"""Prospective authenticated label reader; no import side effects."""
import json,hashlib,math
import pilot_binder
from pathlib import Path
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def load(plan):
 if plan['status']!='ROOT_REVIEWED_SELECTED_PRINCIPAL':raise ValueError('NOT_READY')
 pins=plan['inputs']
 def read(p):
  if pins.get(p)!=sha(p):raise ValueError('bound input')
  return json.loads(Path(p).read_text())
 for p,h in pins.items():
  if sha(p)!=h:raise ValueError('closure')
 post=read(plan['post']);root=read(plan['acceptance']);result=read(plan['result']);wc=read(plan['worker']);runtime=read(plan['runtime']);context=read(plan['context'])
 if post['status']!='ACCEPTED_TWENTYFOUR_CONTINUATION_AND_NEW_SAVED_HISTORY_COORDINATES' or post['original_root_acceptance_sha256']!=sha(plan['acceptance'])or post['result_sha256']!=sha(plan['result']):raise ValueError('accepted24 POST')
 if sha(post['post_result_path'])!=post['post_result_sha256']or post['post_result_path']not in pins:raise ValueError('POST result')
 read(post['post_result_path'])
 if root['result_sha256']!=sha(plan['result'])or wc['result_sha256']!=sha(plan['result'])or wc['freeze_sha256']!=sha(plan['runtime'])or root['worker_freeze']!=sha(plan['runtime']):raise ValueError('source result')
 for p,h in runtime['inputs'].items():
  if pins.get(p)!=h:raise ValueError('transitive closure')
 if len(plan['histories'])!=5 or len(result['orbits'])!=5:raise ValueError('five')
 base=read(plan['original_family_binding'])
 for path,digest in base['inputs'].items():
  if pins.get(path)!=digest:raise ValueError('original family closure')
 cp,ap,radii=pilot_binder.load(base)
 cb=read(plan['source_binding'])
 if cb['original_input_binding']!=plan['original_family_binding']or wc['binding_sha256']!=sha(plan['source_binding'])or context['binding_sha256']!=sha(plan['source_binding']):raise ValueError('same accepted family/context')
 if context['radii']!={k:str(v)for k,v in radii.items()}:raise ValueError('same physical radii')
 for value,cap in ((root['external_seconds'],120),(wc['seconds'],119)):
  if type(value)not in(int,float)or not math.isfinite(value)or not 0<value<=cap:raise ValueError('resource time')
 for value in(root['sampled_whole_tree_peak'],wc['rss_bytes']):
  if type(value)is not int or not 0<value<=384*1048576:raise ValueError('resource RSS')
 selected=[]
 for i,path in enumerate(plan['histories']):
  d=read(path);h=d['history'];row=result['orbits'][i]
  if type(d['orbit'])is not int or d['orbit']!=i or d['context']!=context or len(h)!=24 or type(row['pairs'])is not int or row['pairs']!=24:raise ValueError('fixed24 context')
  inner=read(str(Path(path).with_name('RESULT.json')))
  if sha(Path(path).with_name('RESULT.json'))!=row['result_sha256']or inner['history']!=h or type(row['orbit'])is not int or row['orbit']!=i:raise ValueError('orbit result identity')
  ids=[r['index']for r in h]
  if any(type(x)is not int or not 0<=x<399 for x in ids)or len(set(ids))!=24:raise ValueError('selected labels')
  selected.append(ids)
 return cp,ap,radii,selected
