from pathlib import Path
from fractions import Fraction as F
from math import isqrt,isfinite
import json,re,hashlib

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def rat(x):
 req(type(x)is str and len(x)<=20000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');q=F(x);req(str(q)==x and max(abs(q.numerator).bit_length(),q.denominator.bit_length())<=32768,'rational cap');return q
def box(x):
 req(type(x)is list and len(x)==2,'box shape');a,b=map(rat,x);req(a<=b,'box order');return a,b
def upperroot(q):
 req(q>=0,'nonnegative root');u=1<<256;a,r=divmod(q.numerator*u*u,q.denominator);k=isqrt(a)
 if k*k!=a or r:k+=1
 return F(k,u)
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return[enc(v)for v in x]
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 return x
def same(a,b):return json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True)
def calculate(s,mode):
 p,o=box(s['s0']['P']),box(s['s0']['O']);qp,qo=rat(s['q']['P']),rat(s['q']['O']);req(min(p[1],o[1])>=0,'norm upper');aa=(12*p[1]+3*o[1])/8;bb=12*qp*qp*p[1]+3*qo*qo*o[1];a,b=upperroot(aa),upperroot(bb);g=s['gate'];EE,FF=box(g['E']),box(g['F']);req(EE[0]>=0 and FF[0]>=0,'residual sign');E,Verr=EE[1],FF[1];X=4*upperroot(F(15));V=32*upperroot(F(30));chi=min(X,a+E);psi=min(V,b+Verr);qterm=E*(a+chi);mix=[E*b+chi*Verr,E*psi+a*Verr];error=6*(qterm+min(mix));nom=box(g['nominal']);alpha=((nom[0]-error)/8,(nom[1]+error)/8)
 r={'a_squared_upper':aa,'b_squared_upper':bb,'a_upper':a,'b_upper':b,'E_upper':E,'F_upper':Verr,'X_upper':X,'V_upper':V,'chi_upper':chi,'psi_upper':psi,'quadratic_term':qterm,'mixed_bounds':mix,'error_upper':error,'nominal':nom,'alpha_interval':alpha,'status':'POSITIVE_CERTIFICATE'if alpha[0]>0 else('NEGATIVE_CERTIFICATE'if alpha[1]<0 else'INDETERMINATE_SIGN'),'mode':mode}
 out=enc(r)
 # Validate all emitted rational operands through independent bounded parser.
 for k,v in out.items():
  if k in ['status','mode']:continue
  if type(v)is list:
   for x in v:rat(x)
  else:rat(v)
 return out

def check(O,rf,elapsed,progress):
 O=Path(O);modes=['residual','variational'];expected={'STARTED.json','WORKER_COMPLETE.json','RESULT.json','PARTIAL.json'}|{m+'_'+x+'.json'for m in modes for x in ['INPUT','NORMS','ARITHMETIC']};req(set(p.name for p in O.iterdir())==expected,'exact output census')
 read=lambda p:json.loads(p.read_text());b=read(Path(rf['worker_path'])/'BINDING.json');result=read(O/'RESULT.json');done=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');req(done['status']=='COMPLETE_NEW_POSTERIOR_ONLY'and done['runtime_sha256']==rf['worker_freeze']and done['binding_sha256']==sha(Path(rf['worker_path'])/'BINDING.json')and done['result_sha256']==sha(O/'RESULT.json'),'worker completion')
 req(same(read(O/'STARTED.json'),read(Path(__file__).parent/'WORKER_AUTHORIZATION.json')),'started authorization')
 for v in [elapsed,result['seconds'],part['seconds'],done['seconds']]:req(type(v)in(int,float)and isfinite(v)and v>0,'finite times')
 req(result['seconds']<=part['seconds']<=done['seconds']<19 and done['seconds']<=elapsed<19.5,'time order');req(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'RSS')
 req(result['status']=='COMPLETE_NEW_POSTERIOR_WARD_ESTIMATOR'and type(result['choices'])is int and result['choices']==2 and type(result['source_events'])is int and result['source_events']==255 and type(result['old_moments_recomputed'])is int and result['old_moments_recomputed']==0 and result['new_error_estimator']is True,'result scope');req(type(result['rows'])is list and len(result['rows'])==2,'result rows');req(same(part['current'],{'stage':'complete','data':{}})and type(part['completed'])is int and part['completed']==2,'partial terminal')
 path=b['files']['events'];req(sha(path['path'])==path['sha256'],'source event hash');states={m:{'s0':{},'q':{},'gate':None}for m in modes};seq=0
 with Path(path['path']).open()as stream:
  def take(stage,choice):
   nonlocal seq
   line=stream.readline();req(bool(line),'source prefix');x=json.loads(line);seq+=1;req(type(x['sequence'])is int and x['sequence']==seq and x['stage']==stage and x['choice']==choice,'source chronology');return x['data']
  take('binding',None);take('scalar_inputs',None)
  for mode in modes:
   req(take('choice_start',mode)['mode']==mode,'choice start');s=states[mode]
   for kind in ['P','O']:
    d=take('vacuum_inputs',mode);req(d['kind']==kind,'vacuum kind')
    for j in range(7):
     d=take('vacuum_moment_raw',mode);req(d['kind']==kind and type(d['index'])is int and d['index']==j,'vacuum census')
    req(take('first_polynomial',mode)['kind']==kind,'polynomial kind');req(take('source_inputs',mode)['kind']==kind,'source inputs kind')
    for j in range(3):
     d=take('source_moment_raw',mode);req(d['kind']==kind and type(d['index'])is int and d['index']==j,'source moment census')
     if j==0:s['s0'][kind]=d['real']
    d=take('residual_raw',mode);req(d['kind']==kind,'residual kind');s['q'][kind]=d['q']
   from itertools import combinations
   labels=list(combinations(range(6),2));seen=set();count=0
   for C in labels:
    for A in labels:
     if set(C)&set(A):continue
     kc='O'if C[0]//2==C[1]//2 else'P';ka='O'if A[0]//2==A[1]//2 else'P';ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag=kc+ka+(str(ell)if kc==ka=='P'else'')
     if tag not in seen:
      d=take('cross_wick_raw',mode);req(d['classes']==[kc,ka]and type(d['ell'])is int and d['ell']==ell,'cross chronology');seen.add(tag)
     count+=1;d=take('ordered_word',mode);req(type(d['index'])is int and d['index']==count and same(d['C'],list(C))and same(d['A'],list(A))and type(d['ell'])is int and d['ell']==ell and d['orbit']==tag,'ordered word census')
   req(count==90 and len(seen)==5,'five cross classes')
   s['gate']=take('gate_inputs',mode);take('choice_complete',mode)
  take('complete',None);req(not stream.read()and seq==255,'source complete')
 original=read(Path(b['files']['result']['path']));req(sha(b['files']['result']['path'])==b['files']['result']['sha256'],'original result hash')
 rows=[]
 for i,mode in enumerate(modes):
  s=states[mode];req(same(read(O/(mode+'_INPUT.json')),s),'saved input extraction');req(original['rows'][i]['mode']==mode and same(original['rows'][i]['nominal'],s['gate']['nominal']),'nominal source');req(all(s['q'][k]==s['gate']['rows'][k]['q']for k in ['P','O']),'q source')
  expected_row=calculate(s,mode);norms={k:expected_row[k]for k in ['a_squared_upper','b_squared_upper','a_upper','b_upper']};req(same(read(O/(mode+'_NORMS.json')),norms),'norm arithmetic');req(same(read(O/(mode+'_ARITHMETIC.json')),expected_row)and same(result['rows'][i],expected_row),'posterior arithmetic/copies');rows.append(expected_row);progress({'stage':'schema_choice','mode':mode})
 req(not {r['status']for r in rows}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'},'contradictory signs')
 return {'status':'ACCEPTED_NEW_POSTERIOR_SCHEMA','count':2,'events':255,'result_sha256':sha(O/'RESULT.json'),'independent_new_error_arithmetic':True,'old_moment_truth_inherited':True,'old_moments_replayed':False,'output_hashes':{p.name:sha(p)for p in O.iterdir()}}
