import json, tempfile, pathlib, hashlib, types, copy
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-sparse-action-saved-root-review');m=types.ModuleType('schema');exec(compile((P/'schema.py').read_bytes(),str(P/'schema.py'),'exec'),m.__dict__)
def write(p,x):p.write_text(json.dumps(x)+'\n')
with tempfile.TemporaryDirectory() as td:
 t=pathlib.Path(td);old=t/'old';old.mkdir();out=t/'out';out.mkdir();rows=[];inputs={};auth={'synthetic':True}
 for i in range(5):
  d=old/f'ORBIT_{i}';d.mkdir();events=[]
  for s,n in m.STAGES.items():
   for k in range(n):
    e={'stage':s,'orbit':i,('pair' if s.startswith('coefficient') else 'impurity_bare_index'):(k if n==4 else 399+k),'synthetic_matrix':[[i,k]]};events.append(e)
    write(out/f'ORBIT_{i}_{len(events)-1}_{s}.json',{a:b for a,b in e.items() if a not in ('stage','orbit')})
  p=d/'EVENTS.ndjson';p.write_text(''.join(json.dumps(e)+'\n' for e in events));inputs[str(p)]=m.sha(p)
  rows.append({'orbit':i,'original_pairs':4,'arithmetic_events':16,'leakage_pass':[False,False]})
 b=t/'binding.json';write(b,{'output':str(old),'inputs':inputs});rf={'binding_path':str(b),'authorization':{'binding_sha256':'synthetic'},'worker_freeze':'synthetic'}
 write(out/'STARTED.json',rf['authorization']);r={'status':'PASS_SAVED_FOUR_ACTION_ARITHMETIC','native_calls':0,'events_checked':80,'seconds':1,'orbits':rows};w={'status':'COMPLETE_SAVED_ONLY','runtime_sha256':'synthetic','binding_sha256':'synthetic','seconds':2,'rss_bytes':1000}
 def seal():
  write(out/'RESULT.json',r);w['result_sha256']=m.sha(out/'RESULT.json');write(out/'WORKER_COMPLETE.json',w);write(out/'PARTIAL.json',{'stage':'orbit_complete','rows':r['orbits']})
 seal();m.check(out,rf,3);checks=1
 for key,value in [('native_calls',False),('events_checked',79),('seconds',True)]:
  save=r[key];r[key]=value;seal()
  try:m.check(out,rf,3)
  except (ValueError,TypeError):checks+=1
  else:raise AssertionError(key)
  r[key]=save
 for value in (True,0):
  r['orbits'][0]['leakage_pass'][0]=value;seal()
  try:m.check(out,rf,3)
  except ValueError:checks+=1
  else:raise AssertionError('leakage bool')
 r['orbits'][0]['leakage_pass'][0]=False;seal()
 p=out/'ORBIT_0_0_coefficient.json';save=p.read_bytes();write(p,{'pair':0,'synthetic_matrix':[[999]]})
 try:m.check(out,rf,3)
 except ValueError:checks+=1
 else:raise AssertionError('retained mismatch')
 p.write_bytes(save);write(out/'EXTRA.json',{})
 try:m.check(out,rf,3)
 except ValueError:checks+=1
 else:raise AssertionError('membership')
 print(json.dumps({'status':'PASS','synthetic_predicates':checks,'native_or_saved_arithmetic_calls':0}))
