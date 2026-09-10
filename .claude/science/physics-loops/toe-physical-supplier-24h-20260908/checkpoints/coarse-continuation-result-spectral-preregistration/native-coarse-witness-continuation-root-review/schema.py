from pathlib import Path
from fractions import Fraction as F
from math import isfinite
import json,hashlib,re

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def rat(x):
 req(type(x)is str and len(x)<=40000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');q=F(x);req(str(q)==x and max(abs(q.numerator).bit_length(),q.denominator.bit_length())<=65536,'rational cap');return q
def mat(x,n,m):
 req(type(x)is list and len(x)==n and all(type(r)is list and len(r)==m for r in x),'matrix shape');out=[]
 for row in x:
  z=[]
  for v in row:
   req(type(v)is list and len(v)==2,'box shape');a,b=map(rat,v);req(a<=b,'box order');z.append((a,b))
  out.append(z)
 return out
def same(a,b):return json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True)
def check(O,rf,elapsed,progress):
 O=Path(O);expected={'RESULT.json','PARTIAL.json','WORKER_COMPLETE.json','BLOCKS.jsonl','CONTINUATION.json'}|{f'CASE_{i:02d}.json'for i in range(10)}
 req(set(p.name for p in O.iterdir())==expected,'exact output membership')
 read=lambda p:json.loads(p.read_text());result=read(O/'RESULT.json');done=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');binding=read(Path(rf['worker_path'])/'BINDING.json')
 req(done['status']=='COMPLETE'and done['freeze_sha256']==rf['worker_freeze']and done['result_sha256']==sha(O/'RESULT.json'),'worker receipt relation')
 for x in [result['seconds'],done['seconds'],elapsed]:req(type(x)in(int,float)and isfinite(x)and x>0,'finite time')
 req(result['seconds']<=done['seconds']<299 and done['seconds']<=elapsed<299.5,'time ordering');req(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'worker RSS')
 req(result['status']=='COMPLETE_COMPOSITE_COARSE_WITNESS'and type(result['cases'])is int and result['cases']==10 and result['native_Gaussian_solve']is False and result['fine_consumer_certified']is False,'scope')
 req(type(result['rows'])is list and len(result['rows'])==10,'result census');req(same(part,{'current':{'stage':'complete','case':10},'completed':10}),'terminal partial')
 req(type(result['inherited_cases'])is int and result['inherited_cases']==3 and type(result['new_nodes'])is int and result['new_nodes']==2436 and result['original_run_status']=='FAILED_ONCE_TIME_CAP_PRESERVED','continuation scope')
 pre=binding['prefix'];a=read(Path(pre['receipt']['path']));req(sha(pre['receipt']['path'])==pre['receipt']['sha256'],'failed receipt pin')
 req(a['status']=='FAILED_ONCE_TIME_CAP_PRESERVED'and a['worker_freeze']==pre['worker_freeze']and a['root_freeze']==pre['root_freeze']and a['whole_witness_certified']is False and a['partial_cases_independently_accepted']is False,'old failure remains failed')
 req(type(a['external_seconds'])in(int,float)and isfinite(a['external_seconds'])and 0<a['external_seconds']<300 and type(a['returncode'])is int and a['returncode']==-9,'old failed time/code')
 for key in ('external_rss_bytes','sampled_whole_tree_peak'):req(type(a[key])is int and 0<a[key]<=384*1048576,'old failed resources')
 req(type(a['completed_case_files'])is int and a['completed_case_files']==3 and type(a['retained_event_lines'])is int and a['retained_event_lines']==76 and a['last_panel_metadata']==['witness_panel','3','210']and a['outputs']==pre['outputs'],'old prefix relation')
 old=Path(pre['output']);req(set(x.name for x in old.iterdir())==set(pre['outputs']),'old membership')
 for name,h in pre['outputs'].items():req(sha(old/name)==h,'old retained hash')
 for i in range(3):req(sha(O/f'CASE_{i:02d}.json')==pre['outputs'][f'CASE_{i:02d}.json'],'verbatim completed case')
 with (O/'BLOCKS.jsonl').open('rb')as f:prefix_bytes=b''.join(f.readline()for _ in range(76))
 req(hashlib.sha256(prefix_bytes).hexdigest()==pre['outputs']['BLOCKS.jsonl'],'verbatim76 prefix')
 con=read(O/'CONTINUATION.json');req(same(con,{'old_status':'FAILED_ONCE_TIME_CAP_PRESERVED','prefix_outputs':pre['outputs'],'inherited_cases':3,'inherited_nodes':1344,'remaining_nodes':2436,'start_case':3,'start_node':210,'adapter_truth':'inherited reviewed original adapter; prefix grammar and final block gates checked; no prefix native recomputation'}),'continuation receipt')
 cp=binding['files']['coefficient_events'];req(sha(cp['path'])==cp['sha256'],'pi input pin');pi=None;pi_count=0
 with Path(cp['path']).open()as f:
  for line in f:
   event=json.loads(line)
   if event['stage']=='reciprocal_pi':
    pi_count+=1;pi=mat([[event['payload']['interval']]],1,1)[0][0];pi=round_box(*pi)
 req(pi_count==1 and pi[0]>0,'unique reciprocal pi')
 summaries=[];events=0
 with (O/'BLOCKS.jsonl').open()as stream:
  def take(stage,case):
   nonlocal events
   line=stream.readline();req(bool(line),'missing retained event');x=json.loads(line);events+=1;req(same(x['current'],{'stage':stage,'case':case}),'event stage/order');return x['data']
  for oi in range(5):
   x=take('mapped_T',0);req(type(x['orbit'])is int and x['orbit']==oi and x['source_sha256']==binding['files']['T_'+str(oi)]['sha256'],'mapped T identity');mat(x['mapped'],48,48);req(0<rat(x['operator_squared_upper'])<=10**8,'T norm gate')
  for case in range(10):
   x=take('factorization',case);local=mat(x['local'],7,48);mat(x['projector_columns'],48,7)
   for panel in range(18):
    x=take('witness_panel',case);req(type(x['completed'])is int and x['completed']==21*(panel+1),'panel census');direct=mat(x['direct'],7,7);mixed=mat(x['mixed'],7,7)
   x=take('witness_block',case);block=mat(x['block'],7,7);req(block==assemble(local,direct,mixed,pi,case),'independent high/mixed final assembly')
   n=sum((0 if a<=0<=b else min(abs(a),abs(b))**2 for row in block for a,b in row),F(0));radius=sum((((b-a)/2)**2 for row in block for a,b in row),F(0));precision=radius<=F(11,10**5)**2;excludes=precision and n>=F(11,500)**2
   r=read(O/f'CASE_{case:02d}.json');req(same(r,result['rows'][case]),'typed result copy');req(type(r['orbit'])is int and r['orbit']==case//2 and type(r['impurity'])is int and r['impurity']==case%2+1,'case identity');req(rat(r['squared_block_lower'])==n,'49-entry lower norm')
   req(type(r['excludes_tau_1e9'])is bool and r['excludes_tau_1e9']==excludes and r['status']==('EXCLUDED_BY_COARSE_WITNESS'if excludes else'INDETERMINATE_COARSE_WITNESS'),'case gate');req(r['stored_operator']=='minus_i_times_positive_projector_difference'and r['metric_and_tail_charged']is True,'phase/charge scope')
   summaries.append({'case':case,'radius_squared':str(radius),'norm_lower_squared':str(n),'excludes':excludes});progress({'stage':'schema_case','case':case})
  req(not stream.read(),'extra events')
 req(events==205,'full event count');req((F(11,500)-F(19,1000)-F(213,100000)-F(11,100000))**2/2>F(1,10**9),'fixed conservative tail theorem')
 return {'status':'ACCEPTED_COMPOSITE_COARSE_WITNESS_SCHEMA','cases':10,'events':events,'summaries':summaries,'result_sha256':sha(O/'RESULT.json'),'output_hashes':{p.name:sha(p)for p in O.iterdir()},'independent_49_entry_norm_and_radius':True,'raw_adapter_contractions_replayed':False,'independent_final_high_mixed_assembly':True,'old_failed_protocol_relabelled':False,'inherited_cases':3,'new_nodes':2436,'native_scalar_and_selected_truth_inherited':True,'fine_consumer_certified':False}

# Independent scalar Fraction dyadic evaluator; no producer modules imported.
def round_box(a,b):
 Q=1<<192
 return F((a.numerator*Q)//a.denominator,Q),F(-((-b.numerator*Q)//b.denominator),Q)
def plus(x,y):return round_box(x[0]+y[0],x[1]+y[1])
def times(x,y):
 a,b=x;c,d=y
 if a>=0:
  lo,hi=(a*c,b*d)if c>=0 else (b*c,a*d)if d<=0 else(b*c,b*d)
 elif b<=0:
  lo,hi=(a*d,b*c)if c>=0 else(b*d,a*c)if d<=0 else(a*d,a*c)
 else:
  lo,hi=(a*d,b*d)if c>=0 else(b*c,a*c)if d<=0 else(min(a*d,b*c),max(a*c,b*d))
 return round_box(lo,hi)
def product(A,B):
 C=[]
 for row in A:
  out=[]
  for j in range(len(B[0])):
   z=(F(0),F(0))
   for k,x in enumerate(row):z=plus(z,times(x,B[k][j]))
   out.append(z)
  C.append(out)
 return C
def assemble(local,direct,mixed,pi,case):
 pairs=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
 pair=pairs[case//2][case%2];high=[[(F(0),F(0))for _ in range(7)]for _ in range(7)]
 for j in pair:
  v=2*((-1)**(j+1));high[0][j]=times((F(v,16),F(v,16)),pi);high[j][0]=times((F(-v,16),F(-v,16)),pi)
 projected=product(high,product(local,list(map(list,zip(*local)))))
 out=[]
 for i in range(7):
  row=[]
  for j in range(7):
   x=plus(direct[i][j],high[i][j]);y=plus(mixed[i][j],projected[i][j]);row.append(plus(x,(-y[1],-y[0])))
  out.append(row)
 return out
