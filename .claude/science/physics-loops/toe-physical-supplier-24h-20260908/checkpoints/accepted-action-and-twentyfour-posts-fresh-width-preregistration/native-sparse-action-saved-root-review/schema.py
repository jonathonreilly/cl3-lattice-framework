import json,hashlib,math
from pathlib import Path
STAGES={'coefficient':4,'coefficient_enclosed':4,'T_raw':2,'G_action':2,'L_raw':2,'action_enclosed':2}
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def req(x,m):
 if not x:raise ValueError(m)
def check(out,rf,elapsed):
 out=Path(out);r=read(out/'RESULT.json');w=read(out/'WORKER_COMPLETE.json');b=read(rf['binding_path']);old=Path(b['output'])
 req(read(out/'STARTED.json')==rf['authorization'],'startup')
 req(w['status']=='COMPLETE_SAVED_ONLY' and w['runtime_sha256']==rf['worker_freeze'] and w['binding_sha256']==rf['authorization']['binding_sha256'] and w['result_sha256']==sha(out/'RESULT.json'),'worker binding')
 req(all(type(x)in(int,float) and math.isfinite(x) and x>0 for x in(r['seconds'],w['seconds'],elapsed)) and r['seconds']<=w['seconds']<119 and w['seconds']<=elapsed<=120,'timing')
 req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(r['status']=='PASS_SAVED_FOUR_ACTION_ARITHMETIC' and type(r['native_calls'])is int and r['native_calls']==0 and type(r['events_checked'])is int and r['events_checked']==80,'saved scope/count')
 req(len(r['orbits'])==5,'five orbits');expected={'STARTED.json','RESULT.json','WORKER_COMPLETE.json','PARTIAL.json'}
 for oi,row in enumerate(r['orbits']):
  req(type(row['orbit'])is int and row['orbit']==oi and type(row['original_pairs'])is int and row['original_pairs']==4 and type(row['arithmetic_events'])is int and row['arithmetic_events']==16,'original4 count')
  req(type(row['leakage_pass'])is list and len(row['leakage_pass'])==2 and all(x is False for x in row['leakage_pass']),'ten optional failures')
  counts={s:0 for s in STAGES};seen={s:[] for s in STAGES}
  with (old/f'ORBIT_{oi}'/'EVENTS.ndjson').open()as f:
   for j,line in enumerate(f):
    e=json.loads(line);stage=e['stage']
    if stage not in STAGES:continue
    req(type(e['orbit'])is int and e['orbit']==oi,'original event orbit');counts[stage]+=1
    key='pair' if stage.startswith('coefficient') else 'impurity_bare_index';req(type(e[key])is int,'stage key');seen[stage].append(e[key])
    n=f'ORBIT_{oi}_{j}_{stage}.json';expected.add(n);req(read(out/n)=={k:v for k,v in e.items() if k not in('stage','orbit')},'retained computed stage '+n)
  req(counts==STAGES,'stage census')
  for s,keys in seen.items():req(keys==(list(range(4)) if s.startswith('coefficient') else[399,400]),'stage sequence')
 req(read(out/'PARTIAL.json')=={'stage':'orbit_complete','rows':r['orbits']},'final partial')
 req(set(p.name for p in out.iterdir())==expected,'exact output membership/failure absence')
 for p,h in b['inputs'].items():req(sha(p)==h,'immutable saved input')
 return {'status':'PASS_SAVED_FOUR_ACTION_SCHEMA','orbits':5,'original_pairs_each':4,'arithmetic_events':80,'action_results':10,'optional_target_passes':0,'result_sha256':sha(out/'RESULT.json'),'native_arithmetic_replayed':False}
