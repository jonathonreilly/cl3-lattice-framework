import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F

def check(out,rf,elapsed):
 out=Path(out)
 def req(x,m):
  if not x:raise ValueError(m)
 def read(n):return json.loads((out/n).read_text())
 r,w,p=read('RESULT.json'),read('WORKER_COMPLETE.json'),read('PARTIAL.json')
 req(read('STARTED.json')==rf['authorization'],'start')
 req(w['status']=='COMPLETE_GENERALIZED_SAVED'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['authorization']['binding_sha256']and w['result_sha256']==hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest(),'completion identity')
 for v,cap in((r['seconds'],119),(w['seconds'],119),(elapsed,120)):req(type(v)in(int,float)and math.isfinite(v)and 0<v<cap,'time')
 req(r['seconds']<=w['seconds']<=elapsed and type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'resources')
 req(r['status']=='PASS_INDEPENDENT_GENERALIZED_STAGES'and r['inherited_native_entry_truth']is True and len(r['rows'])==5,'scope')
 req(p==dict(current={'stage':'complete'},rows=r['rows']),'final partial')
 plan=json.loads(Path(rf['binding_path']).read_text());schedule=[('binding',None)];finals=[]
 for oi,files in enumerate(plan['events']):
  schedule.append(('orbit_start',None))
  for j,path in enumerate(files):
   stage=Path(path).stem.split('_',1)[1]
   if stage=='acquired_raw':
    schedule.extend([('before_saved_parse',dict(index=j,path=path)),('authenticated_inherited_raw',None)])
   else:schedule.extend([('independent_'+stage,None),('before_saved_parse',dict(index=j,path=path))])
  schedule.extend([('independent_final',None),('orbit_complete',None)])
  row=r['rows'][oi];req(type(row['orbit'])is int and row['orbit']==oi and row['status']=='PASS_INDEPENDENT_STREAMED_STAGES'and row['inherited_entry_truth']is True and type(row['stages'])is int and row['stages']==len(files),'orbit')
 req(type(r['stage_files'])is int and r['stage_files']==len(schedule)<=25000,'stage count')
 expected={'RESULT.json','WORKER_COMPLETE.json','PARTIAL.json','STARTED.json'}|{f'{j:05d}_{s}.json'for j,(s,d)in enumerate(schedule)}
 req({x.name for x in out.iterdir()}==expected,'exact output membership')
 def walk(x):
  if type(x)is int:req(abs(x).bit_length()<=65536,'integer cap')
  elif isinstance(x,list):
   for v in x:walk(v)
  elif isinstance(x,dict):
   for v in x.values():walk(v)
  elif type(x)is str:
   try:q=F(x)
   except ValueError:return
   req(max(abs(q.numerator).bit_length(),q.denominator.bit_length())<=65536,'fraction cap')
  elif type(x)is not bool and x is not None:raise ValueError('payload type')
 def matrix(a):
  req(isinstance(a,list)and 0<len(a)<=104 and all(isinstance(row,list)and len(row)==len(a[0])for row in a)and 0<len(a[0])<=104,'matrix shape')
  for row in a:
   for x in row:req(isinstance(x,list)and len(x)==2 and all(type(v)is int and abs(v).bit_length()<=4096 for v in x)and x[0]<=x[1],'matrix endpoints')
 for j,(stage,meta)in enumerate(schedule):
  data=read(f'{j:05d}_{stage}.json');walk(data)
  if meta is not None:req(data==meta,'saved stage provenance')
  if stage=='independent_matrix_product_raw':matrix(data['matrix'])
  if stage=='independent_physical_principal':matrix(data['M'])
  if stage=='independent_H_raw':matrix(data)
  if stage=='independent_action_columns':matrix(data['B_U'])
  if stage=='independent_A_Z_raw':matrix(data['A']);matrix(data['Z'])
  if stage=='independent_inverse_candidate':matrix(data['X'])
  if stage in('independent_AXA','independent_N_raw'):matrix(data['data'])
  if stage=='independent_final':finals.append(data)
 req(len(finals)==5,'five final payloads')
 for result in finals:
  req(result['status']=='COMPLETE_SOURCE_ONLY_ALGEBRA'and result['C_width_gate_required']is False and len(result['results'])==2,'final scope')
  for v in result['results']:
   req(v['status']=='CERTIFIED_GENERALIZED_LEAKAGE_BOUND'and 0<=F(v['e'])<1 and v['entrywise_C_claim']is False,'certificate')
   lo,hi=F(v['delta_squared_lower']),F(v['delta_squared_upper']);target=F(1,10**12)
   req(0<=lo<=hi and F(v['target_squared'])==target and type(v['leakage_pass'])is bool and v['leakage_pass']==(hi<=target)and type(v['target_excluded'])is bool and v['target_excluded']==(lo>target),'target flags')
 return dict(status='PASS_SAVED_GENERALIZED_OUTPUT_SCHEMA',orbits=5,arithmetic_replayed_by_root=False)
