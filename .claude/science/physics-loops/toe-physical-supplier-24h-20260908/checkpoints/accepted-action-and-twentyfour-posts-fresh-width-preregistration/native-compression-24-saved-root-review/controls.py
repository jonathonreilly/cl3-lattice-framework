import types,json,tempfile,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent;m=types.ModuleType('schema');exec(compile((p/'schema.py').read_bytes(),str(p/'schema.py'),'exec'),m.__dict__)
def write(p,x):p.write_text(json.dumps(x)+'\n')
with tempfile.TemporaryDirectory() as t:
 o=Path(t);rf={'authorization':{},'worker_freeze':'w','source_result_sha256':'r'};rf['authorization']['binding_sha256']='b';write(o/'STARTED.json',rf['authorization'])
 v={'status':'PASS_NEW_SAVED_HISTORY_COORDINATES','source_result_sha256':'r','native_entries_replayed':False,'new_pivots_selected':False,'original_gram_loaded':False,'all_scientific_targets_met':False,'predicates':1,'histories':60,'coordinates':885780,'orbits':[{'orbit':i,'histories':24,'events':9649}for i in range(5)],'prior_pilot_seconds':'17.94','continuation_seconds':'21.25','cumulative_physical_seconds':'39.19'}
 p={'stage':'complete','current':None,'completed_orbits':v['orbits'],'predicates':1,'coordinates':885780,'histories':60};w={'status':'COMPLETE_SAVED_ONLY','runtime_sha256':'w','binding_sha256':'b','seconds':1,'rss_bytes':100}
 def put(vv,pp,ww):
  write(o/'RESULT.json',vv);write(o/'PARTIAL.json',pp);ww['result_sha256']=hashlib.sha256((o/'RESULT.json').read_bytes()).hexdigest();write(o/'WORKER_COMPLETE.json',ww)
 put(v,p,w);m.check(o,rf,2);n=1
 for kind in ('histories','coordinates','oldprefix','events','flag','partial','time','provenance'):
  a=json.loads(json.dumps(v));b=json.loads(json.dumps(p));c=dict(w)
  if kind=='histories':a['histories']=40
  elif kind=='coordinates':a['coordinates']=271320
  elif kind=='oldprefix':a['orbits'][0]['histories']=12
  elif kind=='events':a['orbits'][0]['events']=6433
  elif kind=='flag':a['new_pivots_selected']=0
  elif kind=='partial':b['current']={}
  elif kind=='time':c['seconds']=30
  else:a['cumulative_physical_seconds']='17.94'
  put(a,b,c)
  try:m.check(o,rf,2)
  except ValueError:n+=1
  else:raise AssertionError(kind)
 print(json.dumps({'status':'PASS_FABRICATED_METADATA','checks':n,'native_calls':0,'saved_arithmetic_calls':0}))
