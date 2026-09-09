from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
S=2**192;ALLOWED={'PASS_BOTH','RESIDUAL_PASS_COORDINATE_FAIL','PAIR_CAP','PRECISION_STALL'}
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def integer(x):return type(x)is int
def interval(x):return isinstance(x,(list,tuple)) and len(x)==2 and all(integer(y) for y in x) and x[0]<=x[1]
def check(out,rf,elapsed):
 out=Path(out);read=lambda n:json.loads((out/n).read_text());r=read('RESULT.json');w=read('WORKER_COMPLETE.json');context=read('CONTEXT.json');auth=read('STARTED.json')
 req(not any((out/n).exists() for n in ('FAILURE.json','DISPATCH_FAILURE.json','IMMUTABILITY_FAILURE.json')),'no failure files')
 req(auth==rf['authorization'],'exact startup authorization');req(w['status']=='COMPLETE_COST_PRECISION_PROBE_ONLY' and w['freeze_sha256']==rf['worker_freeze'] and w['binding_sha256']==rf['authorization']['binding_sha256'] and w['result_sha256']==sha(out/'RESULT.json'),'worker source/result')
 req(all(type(t) in(int,float) and math.isfinite(t) and t>0 for t in (r['seconds'],w['seconds'],elapsed)) and r['seconds']<=w['seconds']<119 and w['seconds']<=elapsed<=120,'times');req(integer(w['rss_bytes']) and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(context['binding_sha256']==rf['authorization']['binding_sha256'] and context['source_freeze_sha256']==rf['source_ast_sha256'],'context')
 caps={'etaA':F(1,10**30),'etaB':F(1,10**19),'etac':F(1,10**19),'etaa0':F(1,10**30),'alpha_max':F(12)}
 req(set(context['radii'])==set(caps) and all(0<=F(context['radii'][k])<=v for k,v in caps.items()) and F(context['radii']['alpha_max'])>0,'radii')
 req(r['status']=='COMPLETE_FIXED_FOUR_PAIR_PROBE' and len(r['orbits'])==5,'result census');summaries=[];last=None
 for oi,outer in enumerate(r['orbits']):
  req(integer(outer['orbit']) and outer['orbit']==oi,'orbit order');d=out/f'ORBIT_{oi}';inner=json.loads((d/'RESULT.json').read_text());req(outer['result_sha256']==sha(d/'RESULT.json') and outer['events_sha256']==sha(d/'EVENTS.ndjson'),'orbit hashes')
  status=inner['status'];pairs=inner['pairs'];req(status in ALLOWED and integer(pairs) and 0<=pairs<=4 and outer['status']==status and integer(outer['pairs']) and outer['pairs']==pairs,'status/pairs');req(status!='PAIR_CAP' or pairs==4,'pair cap')
  hist=inner['history'];req(len(hist)==pairs,'history size');selected=set()
  for h in hist:
   i=h['index'];req(integer(i) and 0<=i<399 and i not in selected,'history index');selected.add(i);chi=1 if i>=396 else(-1 if i%2==0 else 1);req(integer(h['chirality']) and h['chirality']==chi and interval(h['r']) and h['r'][0]>0,'history pivot')
   for key in ('g','j'):req(len(h[key])==399 and all(interval(x) for x in h[key]),'history row')
  if pairs:
   saved=json.loads((d/'HISTORY.json').read_text());req(saved=={'context':context,'orbit':oi,'history':hist},'saved history')
  else:req(not(d/'HISTORY.json').exists(),'zero history absent')
  hp=[];diag=None;checkpoint=None;pending=False
  with(d/'EVENTS.ndjson').open() as stream:
   for line in stream:
    e=json.loads(line);req(integer(e['orbit']) and e['orbit']==oi,'event orbit');last=e;stage=e['stage']
    req(stage!='FAILED','failed event')
    if stage=='pivot_saved':
     req(not pending,'pivot before prior checkpoint');hp.append({k:e[k] for k in ('index','chirality','r','g','j')});pending=True
    if stage=='diagonals_complete':
     diag=e['diagonals'];req(len(diag)==399 and all(interval(x) and x[0]>=0 for x in diag),'diagonal intervals')
    if stage=='checkpoint':
     req(integer(e['pairs']) and e['pairs']==len(hp) and diag is not None,'checkpoint order');pending=False
     raw=F(sum((2 if j<396 else 1)*x[1] for j,x in enumerate(diag)),S);req(F(e['raw_residual_upper'])==raw,'weighted residual')
     coords=e['coordinate_intervals'];req(len(coords)==len(hp),'coordinate pairs');sq=0
     for pair in coords:
      req(len(pair)==2,'two coordinate rows')
      for row in pair:
       req(len(row)==399,'coordinate count')
       for j,x in enumerate(row):req(len(x)==2 and all(integer(v) for v in x) and x[1]>=0,'coordinate interval');sq+=(2 if j<396 else 1)*x[1]**2
     dsq=F(sq,S*S);req(F(e['coordinate_radius_squared'])==dsq,'coordinate squared radius');rp=raw<=F(1,1062*10**6);cp=dsq<=F(1,40000**2);req(type(e['residual_pass'])is bool and type(e['coordinate_pass'])is bool and e['residual_pass']==rp and e['coordinate_pass']==cp,'checkpoint booleans');checkpoint=e
  req(hp==hist and not pending and checkpoint is not None and checkpoint==last and checkpoint['pairs']==pairs,'terminal checkpoint/history')
  rp,cp=checkpoint['residual_pass'],checkpoint['coordinate_pass'];req((status=='PASS_BOTH' and rp and cp) or(status=='RESIDUAL_PASS_COORDINATE_FAIL' and rp and not cp) or(status in('PAIR_CAP','PRECISION_STALL') and not rp),'scientific classification')
  if rp:req(inner['coordinate_radius_squared']==checkpoint['coordinate_radius_squared'],'returned coordinate radius')
  summaries.append({'orbit':oi,'status':status,'pairs':pairs,'residual_pass':rp,'coordinate_pass':cp})
 req(read('PARTIAL.json')==last,'final partial');req(type(w['all_scientific_targets_met'])is bool and w['all_scientific_targets_met']==all(x['status']=='PASS_BOTH' for x in summaries),'allpass flag')
 return {'status':'PASS_COMPLETE_FIXED_PROBE_SCHEMA','orbits':summaries,'all_scientific_targets_met':w['all_scientific_targets_met'],'result_sha256':sha(out/'RESULT.json'),'native_arithmetic_replayed':False}
