from pathlib import Path
from fractions import Fraction as F
import tempfile,json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/native-global-a378-root-review');e={};exec(compile((p/'schema.py').read_text(),'<schema-only>','exec'),e);records=[]
with tempfile.TemporaryDirectory() as td:
 o=Path(td);put=lambda n,x:(o/n).write_text(json.dumps(x));h=lambda n:hashlib.sha256((o/n).read_bytes()).hexdigest();nodes=[];rows=[]
 for j in range(-16,2):
  a=F(4)**j
  for k in range(21):
   x=F(k-10,11);s=a*(5+3*x)/2;w=3*a/21;i=len(nodes);nodes.append({'id':i,'panel':j,'root':k,'s_interval':[str(s)]*2,'weight_interval':[str(w)]*2,'s':str(s),'weight':str(w)});raw={'id':i,'seconds':.001,'raw':{'s':str(s),'A':['1','1'],'Aprime':['-1','-1'],'widths':['0','0'],'terms':160}};put(f'RAW_{i:03d}.json',raw);rows.append(dict(raw,target_met=True))
 events=[{'stage':'scan_start','grid_intervals':2048}]+[{'stage':'scan','grid_index':j}for j in range(128,2049,128)]
 for i in range(10):
  x=F(i+1,11);a=F((x*2048).__floor__(),2048);events.extend([{'stage':'before_root','index':i,'bracket':[str(a),str(a+F(1,2048))]},{'stage':'root','index':i,'bracket':[str(x)]*2}])
 put('NODES.json',{'count':378,'rows':nodes});(o/'ROOT_PROGRESS.jsonl').write_text(''.join(json.dumps(x)+'\n'for x in events));put('RESULT.json',{'status':'COMPLETE','scope':'A-only378scalar acquisition','count':378,'rows':rows,'all_targets_met':True,'seconds':1});put('PARTIAL.json',{'current':{'stage':'retained','id':377},'completed':378,'target_met':True});c={'status':'COMPLETE','result_sha256':h('RESULT.json'),'nodes_sha256':h('NODES.json'),'freeze_sha256':'x','seconds':2,'rss_bytes':100};put('WORKER_COMPLETE.json',c)
 def call():return e['check'](o,{'worker_freeze':'x'},3,lambda x:None)
 call();records.append('synthetic complete accepted')
 for name,mut in [('failed_completion',{'status':'FAILED'}),('worker_over179',{'seconds':179.9}),('zero_worker_time',{'seconds':0}),('result_time_exceeds_worker',{'seconds':.5})]:
  put('WORKER_COMPLETE.json',dict(c,**mut))
  try:call()
  except (ValueError,TypeError):records.append(name+' rejected')
  else:raise AssertionError(name)
 put('WORKER_COMPLETE.json',c);put('DISPATCH_FAILURE.json',{'error':'synthetic'})
 try:call()
 except ValueError:records.append('failure artifact rejected')
 else:raise AssertionError('extra failure')
print(json.dumps({'scope':'Fabricated equally spaced non-Gauss geometry and constant scalar metadata; no physical evaluations. Prior first fixture was interrupted by contemporaneous schema update requiring full37events; this corrected fixture includes37syntheticevents.','outcomes':records},indent=2))
