from pathlib import Path
import json,hashlib,types,tempfile
p=Path('/private/tmp/toe-24h-probes-20260908/native-cminus-saved-post-root-review/schema.py');m=types.ModuleType('schema');exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
count=0;observed=[]
def fixture(change):
 global count
 with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as name:
  d=Path(name);v={'status':'PASS_SAVED_RECONSTRUCTION','node_integrals_replayed':False,'oracle_calls':0,'scientific_status':'CERTIFIED_TARGET','predicates':1};w={'status':'COMPLETE_SAVED_ONLY','runtime_sha256':'toy','seconds':.1,'rss_bytes':100}
  change(v,w);(d/'RESULT.json').write_text(json.dumps(v));w['result_sha256']=hashlib.sha256((d/'RESULT.json').read_bytes()).hexdigest();(d/'WORKER_COMPLETE.json').write_text(json.dumps(w))
  try:m.check(d,'toy',1);result='PASS'
  except (ValueError,TypeError):result='REJECT'
  count+=1;return result
if fixture(lambda v,w:None)!='PASS':raise ValueError('valid')
for key,val in [('status','bad'),('node_integrals_replayed',True),('oracle_calls',1),('scientific_status','INDETERMINATE'),('predicates',0),('predicates',1.5)]:
 if fixture(lambda v,w,k=key,x=val:v.update({k:x}))!='REJECT':raise ValueError(key)
for key,val in [('seconds',float('nan')),('seconds',31),('rss_bytes',385*1048576),('runtime_sha256','bad')]:
 if fixture(lambda v,w,k=key,x=val:w.update({k:x}))!='REJECT':raise ValueError(key)
observed.append({'boolean_predicates':fixture(lambda v,w:v.update(predicates=True))})
print(json.dumps({'synthetic_schema_cases':count,'observed':observed,'physical_calls':0},indent=2))
