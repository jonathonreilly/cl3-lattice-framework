import json,pathlib,types,hashlib,copy
p=pathlib.Path(__file__).resolve().parent;s=p.parent/'native-compression-pilot-saved-root-review';m=types.ModuleType('schema');exec(compile((s/'schema.py').read_bytes(),str(s/'schema.py'),'exec'),m.__dict__)
rf={'worker_freeze':'wf','authorization':{'binding_sha256':'bf'},'source_result_sha256':'source'}
base={'status':'PASS_SAVED_HISTORY_COORDINATES','source_result_sha256':'source','native_entries_replayed':False,'new_pivots_selected':False,'original_gram_loaded':False,'all_scientific_targets_met':False,'predicates':100,'histories':20,'coordinates':39900,'orbits':[{'orbit':i,'histories':4,'events':3618} for i in range(5)]}
count=0
for field,val in [(None,None),('histories',True),('coordinates',39899),('native_entries_replayed',0),('all_scientific_targets_met',True),('source_result_sha256','bad'),('predicates',True),('new_pivots_selected',1)]:
 out=p/('case'+str(count));out.mkdir();v=copy.deepcopy(base)
 if field:v[field]=val
 def write(n,x):(out/n).write_text(json.dumps(x)+'\n')
 write('RESULT.json',v);write('PARTIAL.json',{'stage':'complete','current':None,'completed_orbits':v['orbits'],'predicates':v['predicates'],'histories':v['histories'],'coordinates':v['coordinates']});write('STARTED.json',rf['authorization']);write('WORKER_COMPLETE.json',{'status':'COMPLETE_SAVED_ONLY','runtime_sha256':'wf','binding_sha256':'bf','result_sha256':hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest(),'seconds':1,'rss_bytes':1000})
 try:m.check(out,rf,2)
 except ValueError:
  if field is None:raise
 else:
  if field is not None:raise ValueError('accepted '+field)
 count+=1
(p/'RESULT.json').write_text(json.dumps({'status':'PASS','fabricated_schema_cases':count,'saved_verification_calls':0})+'\n');print(count)
