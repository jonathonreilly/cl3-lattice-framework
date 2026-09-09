"""Fabricated metadata only; no native inputs, entries, recurrence or worker."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json,copy
import schema
checks=0
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x)+'\n')
def events(p,es):p.write_text(''.join(json.dumps(e) for e in es)+'\n')
with TemporaryDirectory(prefix='continuation-schema-') as td:
 b=Path(td);o=b/'out';old=b/'old';o.mkdir();old.mkdir();ctx={'binding_sha256':'b','source_freeze_sha256':'s','radii':{'synthetic':'1'}};oldctx={'synthetic':True,'radii':ctx['radii']};write(old/'CONTEXT.json',oldctx)
 post=b/'post.json';write(post,{'status':'ACCEPTED_COMPRESSION_PILOT_AND_SAVED_HISTORY_COORDINATES'})
 plan=b/'plan.json';write(plan,{'pilot_output':str(old),'post':str(post)})
 rf={'authorization':{'binding_sha256':'b'},'worker_freeze':'w','source_ast_sha256':'s','binding_path':str(plan),'pilot_post_sha256':schema.sha(post)}
 write(o/'STARTED.json',rf['authorization']);write(o/'CONTEXT.json',ctx);rows=[]
 for oi in range(5):
  d=o/f'ORBIT_{oi}';v=old/f'ORBIT_{oi}';d.mkdir();v.mkdir()
  hist=[{'index':i,'chirality':-1 if i%2==0 else 1,'r':[schema.S,schema.S],'g':[[0,0]]*399,'j':[[0,0]]*399} for i in range(4)]
  diag=[[0,0]]*4+[[0,schema.S]]*395;raw=str(sum((2 if i<396 else 1)*x[1] for i,x in enumerate(diag))//schema.S)
  cp={'orbit':oi,'stage':'checkpoint','pairs':4,'raw_residual_upper':raw,'coordinate_radius_squared':'0','residual_pass':False,'coordinate_pass':True,'coordinate_intervals':[[[[0,0] for _ in range(399)] for _ in range(2)] for _ in range(4)]}
  events(v/'EVENTS.ndjson',[{'stage':'diagonals_complete','step':4,'diagonals':diag},cp]);write(v/'HISTORY.json',{'context':oldctx,'orbit':oi,'history':hist})
  write(d/'RESTORED_STATE.json',{'orbit':oi,'history':hist,'checkpoint':{**cp,'diagonals':diag},'original_context':oldctx,'history_sha256':schema.sha(v/'HISTORY.json'),'events_sha256':schema.sha(v/'EVENTS.ndjson')})
  e={k:cp[k] for k in ('orbit','pairs','raw_residual_upper','coordinate_radius_squared','residual_pass','coordinate_pass')};e['stage']='restored_checkpoint';events(d/'EVENTS.ndjson',[e]);write(d/'RESULT.json',{'status':'PRECISION_STALL','pairs':4,'history':hist})
  rows.append({'orbit':oi,'pairs':4,'status':'PRECISION_STALL','result_sha256':schema.sha(d/'RESULT.json'),'events_sha256':schema.sha(d/'EVENTS.ndjson')})
 write(o/'PARTIAL.json',e);r={'status':'COMPLETE_FIXED_CONTINUATION_PROBE','seconds':1,'orbits':rows};write(o/'RESULT.json',r)
 w={'status':'COMPLETE_CONTINUATION_COST_PRECISION_PROBE_ONLY','freeze_sha256':'w','binding_sha256':'b','result_sha256':schema.sha(o/'RESULT.json'),'seconds':2,'rss_bytes':100,'all_scientific_targets_met':False};write(o/'WORKER_COMPLETE.json',w)
 assert schema.check(o,rf,3)['status']=='PASS_CONTINUATION_SCHEMA';checks+=1
 for field,value in [('pairs',True),('orbit',True)]:
  bad=copy.deepcopy(r);bad['orbits'][0][field]=value;write(o/'RESULT.json',bad);w['result_sha256']=schema.sha(o/'RESULT.json');write(o/'WORKER_COMPLETE.json',w)
  try:schema.check(o,rf,3)
  except ValueError:checks+=1
  else:raise ValueError('accepted boolean integer mutant')
 write(o/'RESULT.json',r);w['result_sha256']=schema.sha(o/'RESULT.json');write(o/'WORKER_COMPLETE.json',w)
 for value in (float('nan'),-1,121):
  try:schema.check(o,rf,value)
  except ValueError:checks+=1
  else:raise ValueError('accepted invalid elapsed')
print(json.dumps({'status':'PASS_FABRICATED_SCHEMA','checks':checks,'physical_inputs':0,'worker_calls':0}))
