from pathlib import Path
import sys,json,hashlib,importlib.util,shutil,copy
from fractions import Fraction as F
S=Path('/private/tmp/toe-24h-probes-20260908');R=S/'native-coarse-witness-continuation-root-review';E=S/'native-coarse-witness-continuation-evidence';D=E/'synthetic-root';D.mkdir(exist_ok=True);O=D/'output';O.mkdir(exist_ok=True);old=D/'old';old.mkdir(exist_ok=True);W=D/'worker';W.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('schema',R/'schema.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def save(p,x):p.write_text(json.dumps(x,default=str)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def z(n,k):return [[(F(0),F(0))for _ in range(k)]for _ in range(n)]
events=[];rows=[]
def put(stage,ci,d):events.append({'current':{'stage':stage,'case':ci},'data':d})
b={'files':{'T_'+str(i):{'sha256':str(i)*64}for i in range(5)}}
for i in range(5):put('mapped_T',0,{'orbit':i,'source_sha256':str(i)*64,'mapped':z(48,48),'operator_squared_upper':'1'})
for ci in range(10):
 local=z(7,48);direct=z(7,7);mixed=z(7,7);put('factorization',ci,{'local':local,'projector_columns':z(48,7)})
 for k in range(21,379,21):put('witness_panel',ci,{'completed':k,'direct':direct,'mixed':mixed})
 block=m.assemble(local,direct,mixed,(F(1,4),F(1,4)),ci);put('witness_block',ci,{'block':block})
 n=sum((0 if a<=0<=b else min(abs(a),abs(b))**2 for r in block for a,b in r),F(0));flag=n>=F(11,500)**2
 row={'squared_block_lower':str(n),'excludes_tau_1e9':flag,'status':'EXCLUDED_BY_COARSE_WITNESS'if flag else'INDETERMINATE_COARSE_WITNESS','stored_operator':'minus_i_times_positive_projector_difference','metric_and_tail_charged':True,'orbit':ci//2,'impurity':ci%2+1};rows.append(row);save(O/f'CASE_{ci:02d}.json',row)
 if ci<3:shutil.copyfile(O/f'CASE_{ci:02d}.json',old/f'CASE_{ci:02d}.json')
lines=[json.dumps(e,default=str)+'\n'for e in events];(O/'BLOCKS.jsonl').write_text(''.join(lines));(old/'BLOCKS.jsonl').write_text(''.join(lines[:76]));save(old/'PARTIAL.json',{'synthetic':True})
outputs={p.name:sha(p)for p in old.iterdir()};a={'status':'FAILED_ONCE_TIME_CAP_PRESERVED','worker_freeze':'a'*64,'root_freeze':'b'*64,'whole_witness_certified':False,'partial_cases_independently_accepted':False,'external_seconds':299.83,'returncode':-9,'external_rss_bytes':1000000,'sampled_whole_tree_peak':2000000,'completed_case_files':3,'retained_event_lines':76,'last_panel_metadata':['witness_panel','3','210'],'outputs':outputs};save(D/'FAILED.json',a)
b['prefix']={'receipt':{'path':str(D/'FAILED.json'),'sha256':sha(D/'FAILED.json')},'worker_freeze':'a'*64,'root_freeze':'b'*64,'output':str(old),'outputs':outputs}
save(D/'COEF.jsonl',{'stage':'reciprocal_pi','payload':{'interval':['1/4','1/4']}});b['files']['coefficient_events']={'path':str(D/'COEF.jsonl'),'sha256':sha(D/'COEF.jsonl')};save(W/'BINDING.json',b)
con={'old_status':'FAILED_ONCE_TIME_CAP_PRESERVED','prefix_outputs':outputs,'inherited_cases':3,'inherited_nodes':1344,'remaining_nodes':2436,'start_case':3,'start_node':210,'adapter_truth':'inherited reviewed original adapter; prefix grammar and final block gates checked; no prefix native recomputation'};save(O/'CONTINUATION.json',con)
result={'status':'COMPLETE_COMPOSITE_COARSE_WITNESS','cases':10,'rows':rows,'seconds':1,'native_Gaussian_solve':False,'fine_consumer_certified':False,'inherited_cases':3,'new_nodes':2436,'original_run_status':'FAILED_ONCE_TIME_CAP_PRESERVED'};save(O/'RESULT.json',result)
done={'status':'COMPLETE','freeze_sha256':'c'*64,'result_sha256':sha(O/'RESULT.json'),'seconds':2,'rss_bytes':1000000};save(O/'WORKER_COMPLETE.json',done);save(O/'PARTIAL.json',{'current':{'stage':'complete','case':10},'completed':10})
rf={'worker_path':str(W),'worker_freeze':'c'*64};m.check(O,rf,3,lambda *_:None);count=1
for kind in range(5):
 original={p:p.read_bytes()for p in O.iterdir()}
 if kind==0:save(O/'FAILURE.json',{})
 if kind==1:
  r=copy.deepcopy(result);r['new_nodes']=2436.0;save(O/'RESULT.json',r);d=dict(done,result_sha256=sha(O/'RESULT.json'));save(O/'WORKER_COMPLETE.json',d)
 if kind==2:
  e=copy.deepcopy(events);e[-1]['data']['block'][0][0]=(F(1),F(1));(O/'BLOCKS.jsonl').write_text(''.join(json.dumps(x,default=str)+'\n'for x in e))
 if kind==3:
  r=copy.deepcopy(result);r['rows'][3]['excludes_tau_1e9']=1;save(O/'CASE_03.json',r['rows'][3]);save(O/'RESULT.json',r);save(O/'WORKER_COMPLETE.json',dict(done,result_sha256=sha(O/'RESULT.json')))
 if kind==4:save(O/'WORKER_COMPLETE.json',dict(done,seconds=4))
 try:m.check(O,rf,3,lambda *_:None)
 except ValueError:count+=1
 else:raise AssertionError('adverse accepted '+str(kind))
 for p in O.iterdir():
  if p not in original:p.unlink()
 for p,raw in original.items():p.write_bytes(raw)
# Exhaustive independent sign-case rounding enclosure vs all four products.
for a in range(-3,4):
 for b0 in range(a,4):
  for c in range(-3,4):
   for d in range(c,4):
    x=(F(a,7),F(b0,7));y=(F(c,11),F(d,11));v=m.times(x,y);products=[u*w for u in x for w in y];assert v[0]<=min(products)<=max(products)<=v[1];count+=1
print(json.dumps({'status':'PASS','predicates':count,'full_synthetic_cases':10,'actual_saved_values':0,'native_calls':0}))
