"""Fabricated metadata only; no native inputs, entries, recurrence or worker."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json,copy
import types
schema=types.ModuleType('schema');exec(compile((Path('/private/tmp/toe-24h-probes-20260908/native-compression-24-root-review/schema.py')).read_bytes(),'schema.py','exec'),schema.__dict__)
checks=0
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x)+'\n')
def events(p,es):p.write_text('\n'.join(json.dumps(e) for e in es)+'\n')
with TemporaryDirectory(prefix='continuation-schema-') as td:
 b=Path(td);o=b/'out';old=b/'old';o.mkdir();old.mkdir();ctx={'binding_sha256':'b','source_freeze_sha256':'s','radii':{'synthetic':'1'}};oldctx={'synthetic':True,'radii':ctx['radii']};write(old/'CONTEXT.json',oldctx)
 post=b/'post.json';write(post,{'status':'ACCEPTED_TWELVE_CONTINUATION_AND_NEW_SAVED_HISTORY_COORDINATES'})
 plan=b/'plan.json';write(plan,{'pilot_output':str(old),'post':str(post)})
 rf={'authorization':{'binding_sha256':'b'},'worker_freeze':'w','source_ast_sha256':'s','binding_path':str(plan),'pilot_post_sha256':schema.sha(post)}
 write(o/'STARTED.json',rf['authorization']);write(o/'CONTEXT.json',ctx);rows=[]
 for oi in range(5):
  d=o/f'ORBIT_{oi}';v=old/f'ORBIT_{oi}';d.mkdir();v.mkdir()
  hist=[{'index':i,'chirality':-1 if i%2==0 else 1,'r':[schema.S,schema.S],'g':[[0,0]]*399,'j':[[0,0]]*399} for i in range(12)]
  diag=[[0,0]]*12+[[0,schema.S]]*387;raw=str(sum((2 if i<396 else 1)*x[1] for i,x in enumerate(diag))//schema.S)
  cp={'orbit':oi,'stage':'checkpoint','pairs':12,'raw_residual_upper':raw,'coordinate_radius_squared':'0','residual_pass':False,'coordinate_pass':True,'coordinate_intervals':[[[[0,0] for _ in range(399)] for _ in range(2)] for _ in range(12)]}
  events(v/'EVENTS.ndjson',[{'stage':'diagonals_complete','step':12,'diagonals':diag},cp]);write(v/'HISTORY.json',{'context':oldctx,'orbit':oi,'history':hist})
  write(d/'RESTORED_STATE.json',{'orbit':oi,'history':hist,'checkpoint':{**cp,'diagonals':diag},'original_context':oldctx,'history_sha256':schema.sha(v/'HISTORY.json'),'events_sha256':schema.sha(v/'EVENTS.ndjson')})
  e={k:cp[k] for k in ('orbit','pairs','raw_residual_upper','coordinate_radius_squared','residual_pass','coordinate_pass')};e['stage']='restored_checkpoint';events(d/'EVENTS.ndjson',[e]);write(d/'RESULT.json',{'status':'PRECISION_STALL','pairs':12,'history':hist})
  rows.append({'orbit':oi,'pairs':12,'status':'PRECISION_STALL','result_sha256':schema.sha(d/'RESULT.json'),'events_sha256':schema.sha(d/'EVENTS.ndjson')})
 write(o/'PARTIAL.json',e);r={'status':'COMPLETE_FIXED_CONTINUATION_PROBE','seconds':1,'orbits':rows};write(o/'RESULT.json',r)
 w={'status':'COMPLETE_CONTINUATION_COST_PRECISION_PROBE_ONLY','freeze_sha256':'w','binding_sha256':'b','result_sha256':schema.sha(o/'RESULT.json'),'seconds':2,'rss_bytes':100,'all_scientific_targets_met':False};write(o/'WORKER_COMPLETE.json',w)
 # Extend each fabricated orbit by exactly one NEW row and terminal pass.
 for oi in range(5):
  d=o/f'ORBIT_{oi}';rr=json.loads((d/'RESULT.json').read_text());hh=rr['history'];hh.append({'index':12,'chirality':-1,'r':[schema.S,schema.S],'g':[[0,0]]*399,'j':[[0,0]]*399})
  first=json.loads((d/'EVENTS.ndjson').read_text());cpnew={'orbit':oi,'stage':'checkpoint','pairs':13,'raw_residual_upper':'0','coordinate_radius_squared':'0','residual_pass':True,'coordinate_pass':True,'coordinate_intervals':[[[[0,0] for _ in range(399)] for _ in range(2)] for _ in range(13)]}
  ev=[first,{'orbit':oi,'stage':'pivot_row','step':12,'index':12},{'orbit':oi,'stage':'pivot_saved',**hh[-1]},{'orbit':oi,'stage':'diagonals_complete','step':13,'diagonals':[[0,0]]*399},cpnew]
  events(d/'EVENTS.ndjson',ev);write(d/'HISTORY.json',{'context':ctx,'orbit':oi,'history':hh});write(d/'RESULT.json',{'status':'PASS_BOTH','pairs':13,'history':hh,'coordinate_radius_squared':'0'})
  r['orbits'][oi].update(pairs=13,status='PASS_BOTH',result_sha256=schema.sha(d/'RESULT.json'),events_sha256=schema.sha(d/'EVENTS.ndjson'))
 write(o/'PARTIAL.json',cpnew);write(o/'RESULT.json',r);w.update(result_sha256=schema.sha(o/'RESULT.json'),all_scientific_targets_met=True);write(o/'WORKER_COMPLETE.json',w)
 schema.check(o,rf,3);checks+=1
 d=o/'ORBIT_0';original=[json.loads(l) for l in(d/'EVENTS.ndjson').read_text().splitlines()]
 outcomes=[]
 for name in ('old_row','step4_diagonal','repeat_restore','initial_coordinate_checkpoint','duplicate_diag','missing_diag','wrong_fresh_step','wrong_gate'):
  es=copy.deepcopy(original)
  if name=='old_row':es[1]['index']=0
  elif name=='step4_diagonal':es[3]['step']=12
  elif name=='repeat_restore':es.insert(1,copy.deepcopy(es[0]))
  elif name=='initial_coordinate_checkpoint':es.insert(1,{k:v for k,v in json.loads((d/'RESTORED_STATE.json').read_text())['checkpoint'].items() if k!='diagonals'})
  elif name=='duplicate_diag':es.insert(4,copy.deepcopy(es[3]))
  elif name=='missing_diag':es.pop(3)
  elif name=='wrong_fresh_step':es[3]['step']=14
  else:es[-1]['coordinate_pass']=False
  events(d/'EVENTS.ndjson',es);r['orbits'][0]['events_sha256']=schema.sha(d/'EVENTS.ndjson');write(o/'RESULT.json',r);w['result_sha256']=schema.sha(o/'RESULT.json');write(o/'WORKER_COMPLETE.json',w)
  try:schema.check(o,rf,3)
  except ValueError:outcomes.append([name,'REJECTED'])
  else:outcomes.append([name,'ACCEPTED'])
 assert all(x[1]=='REJECTED' for x in outcomes),outcomes
 print(json.dumps({'new_history_fixture':'PASS','adverses':outcomes,'native_calls':0}))
