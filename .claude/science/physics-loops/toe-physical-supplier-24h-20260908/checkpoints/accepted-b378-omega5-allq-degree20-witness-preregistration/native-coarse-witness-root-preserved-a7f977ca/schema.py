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
 O=Path(O);expected={'RESULT.json','PARTIAL.json','WORKER_COMPLETE.json','BLOCKS.jsonl'}|{f'CASE_{i:02d}.json'for i in range(10)}
 req(set(p.name for p in O.iterdir())==expected,'exact output membership')
 read=lambda p:json.loads(p.read_text());result=read(O/'RESULT.json');done=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');binding=read(Path(rf['worker_path'])/'BINDING.json')
 req(done['status']=='COMPLETE'and done['freeze_sha256']==rf['worker_freeze']and done['result_sha256']==sha(O/'RESULT.json'),'worker receipt relation')
 for x in [result['seconds'],done['seconds'],elapsed]:req(type(x)in(int,float)and isfinite(x)and x>0,'finite time')
 req(result['seconds']<=done['seconds']<=elapsed<299.5,'time ordering');req(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'worker RSS')
 req(result['status']=='COMPLETE_FIXED_COARSE_WITNESS'and type(result['cases'])is int and result['cases']==10 and result['native_Gaussian_solve']is False and result['fine_consumer_certified']is False,'scope')
 req(type(result['rows'])is list and len(result['rows'])==10,'result census');req(same(part,{'current':{'stage':'complete','case':10},'completed':10}),'terminal partial')
 summaries=[];events=0
 with (O/'BLOCKS.jsonl').open()as stream:
  def take(stage,case):
   nonlocal events
   line=stream.readline();req(bool(line),'missing retained event');x=json.loads(line);events+=1;req(same(x['current'],{'stage':stage,'case':case}),'event stage/order');return x['data']
  for oi in range(5):
   x=take('mapped_T',0);req(type(x['orbit'])is int and x['orbit']==oi and x['source_sha256']==binding['files']['T_'+str(oi)]['sha256'],'mapped T identity');mat(x['mapped'],48,48);req(0<rat(x['operator_squared_upper'])<=10**8,'T norm gate')
  for case in range(10):
   x=take('factorization',case);mat(x['local'],7,48);mat(x['projector_columns'],48,7)
   for panel in range(18):
    x=take('witness_panel',case);req(type(x['completed'])is int and x['completed']==21*(panel+1),'panel census');mat(x['direct'],7,7);mat(x['mixed'],7,7)
   x=take('witness_block',case);block=mat(x['block'],7,7)
   n=sum((0 if a<=0<=b else min(abs(a),abs(b))**2 for row in block for a,b in row),F(0));radius=sum((((b-a)/2)**2 for row in block for a,b in row),F(0));precision=radius<=F(11,10**5)**2;excludes=precision and n>=F(11,500)**2
   r=read(O/f'CASE_{case:02d}.json');req(same(r,result['rows'][case]),'typed result copy');req(type(r['orbit'])is int and r['orbit']==case//2 and type(r['impurity'])is int and r['impurity']==case%2+1,'case identity');req(rat(r['squared_block_lower'])==n,'49-entry lower norm')
   req(type(r['excludes_tau_1e9'])is bool and r['excludes_tau_1e9']==excludes and r['status']==('EXCLUDED_BY_COARSE_WITNESS'if excludes else'INDETERMINATE_COARSE_WITNESS'),'case gate');req(r['stored_operator']=='minus_i_times_positive_projector_difference'and r['metric_and_tail_charged']is True,'phase/charge scope')
   summaries.append({'case':case,'radius_squared':str(radius),'norm_lower_squared':str(n),'excludes':excludes});progress({'stage':'schema_case','case':case})
  req(not stream.read(),'extra events')
 req(events==205,'full event count');req((F(11,500)-F(19,1000)-F(213,100000)-F(11,100000))**2/2>F(1,10**9),'fixed conservative tail theorem')
 return {'status':'ACCEPTED_FIXED_COARSE_WITNESS_SCHEMA','cases':10,'events':events,'summaries':summaries,'result_sha256':sha(O/'RESULT.json'),'output_hashes':{p.name:sha(p)for p in O.iterdir()},'independent_49_entry_norm_and_radius':True,'raw_adapter_contractions_replayed':False,'native_scalar_and_selected_truth_inherited':True,'fine_consumer_certified':False}
