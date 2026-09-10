from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
S=2**192
ALLOWED={'PASS_BOTH','RESIDUAL_PASS_COORDINATE_FAIL','PAIR_CAP','PRECISION_STALL'}
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()
def integer(x):return type(x)is int
def interval(x):return isinstance(x,(list,tuple)) and len(x)==2 and all(integer(t) for t in x) and x[0]<=x[1]
def read(p):return json.loads(Path(p).read_text())
def checkpoint(e,diag,pairs):
 req(integer(e['pairs']) and e['pairs']==pairs,'checkpoint pair count')
 req(len(diag)==399 and all(interval(x) and 0<=x[0]<=x[1]<=531*S for x in diag),'diagonal')
 raw=F(sum((2 if i<396 else 1)*x[1] for i,x in enumerate(diag)),S);req(raw==F(e['raw_residual_upper']),'weighted residual')
 coords=e['coordinate_intervals'];req(len(coords)==pairs,'coordinate pairs');sq=0
 for pair in coords:
  req(len(pair)==2,'Gamma pair')
  for row in pair:
   req(len(row)==399,'coordinate row')
   for i,x in enumerate(row):
    req(isinstance(x,(list,tuple)) and len(x)==2 and all(integer(t) for t in x) and x[1]>=0,'coordinate interval');sq+=(2 if i<396 else 1)*x[1]**2
 dsq=F(sq,S*S);req(dsq==F(e['coordinate_radius_squared']),'coordinate squared radius')
 rp=raw<=F(1,1062*10**6);cp=dsq<=F(1,40000**2)
 req(type(e['residual_pass'])is bool and type(e['coordinate_pass'])is bool and e['residual_pass']==rp and e['coordinate_pass']==cp,'gate booleans')
 return rp,cp

def check(out,rf,elapsed):
 out=Path(out);r=read(out/'RESULT.json');w=read(out/'WORKER_COMPLETE.json');context=read(out/'CONTEXT.json')
 req(not any((out/n).exists() for n in ('FAILURE.json','DISPATCH_FAILURE.json','IMMUTABILITY_FAILURE.json')),'no failures')
 req(read(out/'STARTED.json')==rf['authorization'],'startup')
 req(w['status']=='COMPLETE_CONTINUATION_COST_PRECISION_PROBE_ONLY' and w['freeze_sha256']==rf['worker_freeze'] and w['binding_sha256']==rf['authorization']['binding_sha256'] and w['result_sha256']==sha(out/'RESULT.json'),'worker binding')
 req(all(type(t) in(int,float) and math.isfinite(t) and t>0 for t in (r['seconds'],w['seconds'],elapsed)) and r['seconds']<=w['seconds']<=elapsed<=120 and w['seconds']<119,'time nesting')
 req(integer(w['rss_bytes']) and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(context['binding_sha256']==rf['authorization']['binding_sha256'] and context['source_freeze_sha256']==rf['source_ast_sha256'],'current context')
 plan=read(rf['binding_path']);old=Path(plan['pilot_output']);oldctx=read(old/'CONTEXT.json');post=read(plan['post'])
 req(post['status']=='ACCEPTED_COMPRESSION_PILOT_AND_SAVED_HISTORY_COORDINATES' and sha(plan['post'])==rf['pilot_post_sha256'],'original POST')
 req(context['radii']==oldctx['radii'],'same physical family/radii')
 req(r['status']=='COMPLETE_FIXED_CONTINUATION_PROBE' and len(r['orbits'])==5,'five orbits')
 summaries=[];last=None
 for oi,outer in enumerate(r['orbits']):
  req(integer(outer['orbit']) and outer['orbit']==oi,'orbit ordering')
  d=out/('ORBIT_%d'%oi);prev=old/('ORBIT_%d'%oi);inner=read(d/'RESULT.json');rest=read(d/'RESTORED_STATE.json');oldhist=read(prev/'HISTORY.json')
  req(sha(d/'RESULT.json')==outer['result_sha256'] and sha(d/'EVENTS.ndjson')==outer['events_sha256'],'orbit digests')
  req(integer(rest['orbit']) and rest['orbit']==oi and rest['history']==oldhist['history'] and len(rest['history'])==4 and rest['original_context']==oldctx and oldhist['context']==oldctx,'original history/context identity')
  req(rest['history_sha256']==sha(prev/'HISTORY.json') and rest['events_sha256']==sha(prev/'EVENTS.ndjson'),'restored digests')
  # Independently require the exact accepted terminal checkpoint and diagonals.
  od=None;oc=None;olast=None
  with (prev/'EVENTS.ndjson').open() as f:
   for line in f:
    e=json.loads(line);olast=e
    if e['stage']=='diagonals_complete' and e['step']==4:od=e['diagonals']
    if e['stage']=='checkpoint' and e['pairs']==4:oc=e
  req(oc is not None and olast==oc and rest['checkpoint']=={**oc,'diagonals':od},'exact original terminal state')
  initial=rest['checkpoint'];rp,cp=checkpoint(initial,od,4)
  hist=inner['history'];pairs=inner['pairs'];status=inner['status']
  req(integer(pairs) and 4<=pairs<=12 and len(hist)==pairs and hist[:4]==rest['history'] and status in ALLOWED,'cumulative history')
  req(integer(outer['pairs']) and outer['pairs']==pairs and outer['status']==status,'outer status')
  selected=set()
  for h in hist:
   i=h['index'];req(integer(i) and 0<=i<399 and i not in selected,'unique pivot');selected.add(i)
   req(integer(h['chirality']) and h['chirality']==(1 if i>=396 else(-1 if i%2==0 else 1)) and interval(h['r']) and h['r'][0]>0,'pivot')
   for key in ('g','j'):req(len(h[key])==399 and all(interval(x) for x in h[key]),'pivot intervals')
  if pairs>4:req(read(d/'HISTORY.json')=={'context':context,'orbit':oi,'history':hist},'cumulative saved history')
  else:req(not(d/'HISTORY.json').exists(),'no assumption early return writes HISTORY')
  hp=list(rest['history']);diag=od;terminal=initial;pending=False;first=True;fresh_diagonal_step=None
  with (d/'EVENTS.ndjson').open() as f:
   for line in f:
    e=json.loads(line);last=e;stage=e['stage'];req(integer(e['orbit']) and e['orbit']==oi and stage!='FAILED','event metadata')
    if first:
     expected={'orbit':oi,'stage':'restored_checkpoint','pairs':4,'raw_residual_upper':initial['raw_residual_upper'],'coordinate_radius_squared':initial['coordinate_radius_squared'],'residual_pass':initial['residual_pass'],'coordinate_pass':initial['coordinate_pass']}
     req(integer(e['pairs']) and type(e['residual_pass'])is bool and type(e['coordinate_pass'])is bool and e==expected,'first event restored checkpoint');first=False;continue
    req(stage!='restored_checkpoint','no duplicate restoration')
    if stage in ('diagonals','diagonal','diagonals_complete'):req(integer(e['step']) and 5<=e['step']<=12,'no initial diagonal replay')
    if stage in ('pivot_row','pivot_entry','pivot_row_complete'):req(integer(e['step']) and 4<=e['step']<=11 and integer(e['index']) and e['index'] not in [h['index'] for h in hp],'new row only')
    if stage=='pivot_saved':
     req(not pending,'new pivot before checkpoint');h={k:e[k] for k in ('index','chirality','r','g','j')};req(h==hist[len(hp)] and h['index'] not in [x['index'] for x in hp],'new row history');hp.append(h);pending=True;fresh_diagonal_step=None
    if stage=='diagonals_complete':
     req(pending and integer(e['step']) and e['step']==len(hp) and fresh_diagonal_step is None,'fresh diagonal after new pivot');diag=e['diagonals'];fresh_diagonal_step=e['step']
    if stage=='checkpoint':
     req(pending and len(hp)>=5 and fresh_diagonal_step==len(hp),'new checkpoint requires fresh pivot and diagonals');rp,cp=checkpoint(e,diag,len(hp));terminal=e;pending=False;fresh_diagonal_step=None
  req(not first and hp==hist and not pending and (last['stage']=='restored_checkpoint' if pairs==4 else last==terminal),'terminal cumulative state')
  req((status=='PAIR_CAP' and pairs==12 and not rp) or(status=='PRECISION_STALL' and not rp) or(status=='PASS_BOTH' and rp and cp) or(status=='RESIDUAL_PASS_COORDINATE_FAIL' and rp and not cp),'scientific classification')
  summaries.append({'orbit':oi,'pairs':pairs,'new_pairs':pairs-4,'status':status,'residual_pass':rp,'coordinate_pass':cp})
 req(read(out/'PARTIAL.json')==last,'last retained partial')
 req(type(w['all_scientific_targets_met'])is bool and w['all_scientific_targets_met']==all(x['status']=='PASS_BOTH' for x in summaries),'overall scientific flag')
 return {'status':'PASS_CONTINUATION_SCHEMA','orbits':summaries,'result_sha256':sha(out/'RESULT.json'),'native_arithmetic_replayed':False,'prior_pilot_seconds':5.97}
