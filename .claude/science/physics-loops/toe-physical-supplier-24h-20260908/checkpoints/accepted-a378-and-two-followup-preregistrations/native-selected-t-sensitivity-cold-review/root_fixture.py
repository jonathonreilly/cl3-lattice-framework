from pathlib import Path
import tempfile,json,hashlib
from fractions import Fraction as F
root=Path('/private/tmp/toe-24h-probes-20260908/native-saved-t-sensitivity-root-review');e={};exec(compile((root/'schema.py').read_text(),'<schema>','exec'),e);cases=[]
with tempfile.TemporaryDirectory() as td:
 p=Path(td);o=p/'out';o.mkdir();put=lambda n,x:(o/n).write_text(json.dumps(x));h=lambda q:hashlib.sha256(q.read_bytes()).hexdigest();b=p/'binding.json';b.write_text(json.dumps({'candidates':[{'path':f'/synthetic/ORBIT_{i}/CANDIDATE.json','sha256':'a'*64}for i in range(5)]}));rf={'binding_path':str(b),'binding_sha256':h(b),'worker_freeze':'x'};rows=[]
 for i in range(5):
  put(f'NORM_{i}.json',{'orbit':i,'dimension':48,'row_l1':['1']*48,'column_l1':['1']*48,'frobenius_squared':'48','operator_norm_squared_upper':'1'});row={'orbit':i,'candidate_sha256':'a'*64,'metric_gain':'48','eta_metric_for_unit_trace_tau':str(F(1,48*10**9)),'eta_metric_for_unit_trace_r2':str(F(1,48*10**16)),'scope':'unit-trace PSD consumer only; actual consumer multiplier remains required'};put(f'BUDGET_{i}.json',row);rows.append(row)
 result={'status':'COMPLETE_NEW_T_SENSITIVITY','actual_consumer_precision_decided':False,'scope':'exact savedT norm and normalized-consumer sufficient thresholds only','rows':rows,'seconds':1};put('RESULT.json',result);put('PARTIAL.json',{'current':{'stage':'complete','orbit':4},'completed':5});complete={'status':'COMPLETE','freeze_sha256':'x','seconds':2,'rss_bytes':100,'result_sha256':h(o/'RESULT.json')};put('WORKER_COMPLETE.json',complete)
 def call():e['check'](o,rf,3,lambda _:None)
 call();cases.append('five-orbit synthetic accepted')
 for name,change in [('worker_time',{'seconds':19}),('bool_RSS',{'rss_bytes':True}),('bad_status',{'status':'FAILED'})]:
  put('WORKER_COMPLETE.json',dict(complete,**change))
  try:call()
  except ValueError:cases.append(name+' rejected')
  else:raise AssertionError(name)
 put('WORKER_COMPLETE.json',complete);orig=(o/'BUDGET_0.json').read_text();row=json.loads(orig);row['metric_gain']='47';put('BUDGET_0.json',row)
 try:call()
 except ValueError:cases.append('wrong exact gain rejected')
 else:raise AssertionError
 (o/'BUDGET_0.json').write_text(orig);put('FAILURE.json',{})
 try:call()
 except ValueError:cases.append('failure artifact rejected')
 else:raise AssertionError
print(json.dumps({'scope':'fabricated identity norm metadata only, no actual T reads or census','cases':cases},indent=2))
