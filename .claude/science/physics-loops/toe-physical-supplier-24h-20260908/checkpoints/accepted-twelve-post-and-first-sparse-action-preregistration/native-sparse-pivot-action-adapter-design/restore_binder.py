"""Accepted pilot restoration. No entry/index/pivot calls; native dispatcher only."""
import json,math
from pathlib import Path
from fractions import Fraction as F
import pilot_binder
sha=pilot_binder.sha
S=2**192
def req(x,message):
 if not x:raise ValueError(message)
def interval(x):return isinstance(x,(list,tuple)) and len(x)==2 and all(type(t)is int for t in x) and x[0]<=x[1]
def load(plan):
 req(plan['status']=='ROOT_REVIEWED_FOUR_TO_TWELVE_CONTINUATION','authorization stage')
 pins=plan['inputs']
 def read(path):
  req(path in pins and sha(path)==pins[path],'pin '+path);return json.loads(Path(path).read_text())
 for path,digest in pins.items():req(sha(path)==digest,'input closure '+path)
 post=read(plan['post']);root=read(plan['root']);out=Path(plan['pilot_output']);result=read(str(out/'RESULT.json'));worker=read(str(out/'WORKER_COMPLETE.json'));context=read(str(out/'CONTEXT.json'))
 req(post['status']=='ACCEPTED_COMPRESSION_PILOT_AND_SAVED_HISTORY_COORDINATES' and post['original_root_acceptance_sha256']==sha(plan['root']) and post['result_sha256']==sha(out/'RESULT.json'),'POST acceptance')
 read(post['post_result_path']);req(post['post_result_sha256']==sha(post['post_result_path']),'POST result')
 req(root['status']=='ACCEPTED_COMPLETE_FIXED_COMPRESSION_PILOT' and root['result_sha256']==sha(out/'RESULT.json') and root['worker_freeze']==plan['pilot_runtime_sha256'],'root acceptance')
 req(worker['status']=='COMPLETE_COST_PRECISION_PROBE_ONLY' and worker['freeze_sha256']==plan['pilot_runtime_sha256'] and worker['result_sha256']==sha(out/'RESULT.json') and worker['binding_sha256']==sha(plan['pilot_binding']),'worker')
 for v,cap in ((root['external_seconds'],120),(root['sampled_whole_tree_peak'],384*1048576),(worker['seconds'],119),(worker['rss_bytes'],384*1048576)):
  req(type(v) in(int,float) and math.isfinite(v) and 0<v<=cap,'accepted resources')
 pp=read(plan['pilot_binding'])
 for path,digest in pp['inputs'].items():req(pins.get(path)==digest,'same input closure')
 cp,ap,radii=pilot_binder.load(pp)
 req(context['binding_sha256']==sha(plan['pilot_binding']) and context['source_freeze_sha256']==plan['pilot_source_sha256'],'original source context')
 req(context['radii']=={k:str(v) for k,v in radii.items()},'identical actual physical radii')
 req(result['status']=='COMPLETE_FIXED_FOUR_PAIR_PROBE' and len(result['orbits'])==5,'pilot census')
 states=[]
 for oi,outer in enumerate(result['orbits']):
  req(type(outer['orbit'])is int and outer['orbit']==oi and type(outer['pairs'])is int and outer['pairs']==4 and outer['status']=='PAIR_CAP','fixed completed four')
  d=out/('ORBIT_%d'%oi);inner=read(str(d/'RESULT.json'));saved=read(str(d/'HISTORY.json'))
  req(sha(d/'RESULT.json')==outer['result_sha256'] and sha(d/'EVENTS.ndjson')==outer['events_sha256'],'saved orbit digests')
  req(type(inner['pairs'])is int and inner['pairs']==4 and inner['status']=='PAIR_CAP','inner four')
  hist=inner['history'];req(len(hist)==4 and saved=={'context':context,'orbit':oi,'history':hist},'complete history context')
  selected=set()
  for h in hist:
   i=h['index'];req(type(i)is int and 0<=i<399 and i not in selected,'history index');selected.add(i)
   req(type(h['chirality'])is int and h['chirality']==(1 if i>=396 else(-1 if i%2==0 else 1)) and interval(h['r']) and h['r'][0]>0,'history pivot')
   for key in ('g','j'):req(len(h[key])==399 and all(interval(x) for x in h[key]),'history intervals')
  ep=str(d/'EVENTS.ndjson');req(ep in pins,'events membership');last=None;diag=None;checkpoint=None;hp=[]
  with Path(ep).open() as f:
   for line in f:
    e=json.loads(line);req(type(e['orbit'])is int and e['orbit']==oi and e['stage']!='FAILED','event orbit/status');last=e
    if e['stage']=='pivot_saved':hp.append({k:e[k] for k in ('index','chirality','r','g','j')})
    if e['stage']=='diagonals_complete':
     req(type(e['step'])is int,'diagonal step')
     if e['step']==4:diag=e['diagonals']
    if e['stage']=='checkpoint':
     req(type(e['pairs'])is int,'checkpoint pairs')
     if e['pairs']==4:checkpoint=e
  req(hp==hist and checkpoint is not None and last==checkpoint and type(last['pairs'])is int and last['pairs']==4,'terminal four checkpoint')
  req(diag is not None and len(diag)==399 and all(interval(x) and 0<=x[0]<=x[1]<=531*S for x in diag),'terminal diagonal shape')
  req(all(diag[i]==[0,0] for i in selected),'selected exact zeros')
  raw=F(sum((2 if i<396 else 1)*x[1] for i,x in enumerate(diag)),S)
  req(raw==F(checkpoint['raw_residual_upper']),'terminal weighted residual')
  coords=checkpoint['coordinate_intervals'];req(len(coords)==4,'terminal coordinate pairs');sq=0
  for pair in coords:
   req(len(pair)==2,'two coordinates')
   for row in pair:
    req(len(row)==399,'coordinate length')
    for j,x in enumerate(row):
     req(isinstance(x,list) and len(x)==2 and all(type(t)is int for t in x) and x[1]>=0,'coordinate shape');sq+=(2 if j<396 else 1)*x[1]**2
  dsq=F(sq,S*S);req(dsq==F(checkpoint['coordinate_radius_squared']),'terminal coordinate radius')
  req(type(checkpoint['residual_pass'])is bool and type(checkpoint['coordinate_pass'])is bool and checkpoint['residual_pass']==(raw<=F(1,1062*10**6)) and checkpoint['coordinate_pass']==(dsq<=F(1,40000**2)),'exact gate bools')
  req(checkpoint['residual_pass'] is False,'original four cap is not target pass')
  states.append({'orbit':oi,'history':hist,'checkpoint':{**checkpoint,'diagonals':diag},'original_context':context,'history_sha256':sha(d/'HISTORY.json'),'events_sha256':sha(d/'EVENTS.ndjson')})
 return cp,ap,radii,states
