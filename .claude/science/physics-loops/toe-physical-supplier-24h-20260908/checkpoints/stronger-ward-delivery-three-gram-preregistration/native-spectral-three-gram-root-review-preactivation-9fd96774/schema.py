"""Independent affine-c joint-form and screening validation; no producer imports."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import isqrt,isfinite
import json,hashlib
LABELS=list(combinations(range(6),2)); MODES=['residual','variational'];LIMIT=384*1048576

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def integer(x,n):req(type(x)is int and x==n,'literal integer')
def number(x,cap):req(type(x)in(int,float)and isfinite(x)and 0<x<cap,'finite positive timing')
def typed(a,b):return type(a)is type(b)and (a.keys()==b.keys()and all(typed(a[k],b[k])for k in a)if type(a)is dict else len(a)==len(b)and all(typed(x,y)for x,y in zip(a,b))if type(a)is list else a==b)
def eq(a,b,m):req(typed(a,b),m)
def rat(x):
 req(type(x)is str and len(x)<=20000,'rational string');v=F(x);req(str(v)==x and max(v.numerator.bit_length(),v.denominator.bit_length())<=32768,'canonical rational cap');return v
def box(x):
 req(type(x)is list and len(x)==2,'box');v=tuple(map(rat,x));req(v[0]<=v[1],'box order');return v
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(tuple,list)):return[enc(y)for y in x]
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 return x
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def scale(a,s):return min(a[0]*s,a[1]*s),max(a[0]*s,a[1]*s)
def upperroot(x):
 req(x>=0,'negative root');g=1<<128;n=isqrt(x.numerator*g*g//x.denominator);return F(n if n*n*x.denominator==x.numerator*g*g else n+1,g)
def lower(E,V):
 req(E>=0 and V>=0,'negative errors')
 return -3*E*E-3*E*V if V<=2*E else -6*E*E-F(3,4)*V*V if V<=4*E else 6*E*E-6*E*V

def form(C,A,c,n):
 # Independent affine-in-c expansion, avoiding producer association.
 u,w,q=C;v,z,t=A
 return[add((u*v+n*w*z,)*2,scale(c,u*z+w*v)),add((q*t*(4*n*u*v+16*w*z),)*2,scale(c,8*q*t*(u*z+w*v))),add((-t*(2*v*n*w+4*z*u),)*2,scale(c,-t*(2*v*u+4*z*w)))]
def kind(a):return'O'if a[0]//2==a[1]//2 else'P'
def extract(ev,stage,choice,k=None):
 xs=[x['data']for x in ev if x['stage']==stage and x['choice']==choice and(k is None or x['data'].get('kind')==k)];req(len(xs)==1,'source unique field');return xs[0]

def validate_choice(inp,row,events,mode):
 req(row['mode']==mode,'choice mode');c=box(inp['c']);nom=box(inp['nominal']);old=box(inp['spectral_alpha_interval']);E=rat(inp['E_upper']);V=rat(inp['F_upper']);L=lower(E,V);screen=nom[1]+L
 for key in ['true_alpha_excluded','other_duals_excluded']:
  if row['status']!='INDETERMINATE_ARITHMETIC':req(row[key]is False,'narrow scope')
 if not events:
  req(row['status']=='INDETERMINATE_ARITHMETIC'and row['stage']=='new_inputs','refusal before screen');return
 eq(events[0]['data'],enc({'E':E,'F':V,'L':L,'nominal':nom,'upper_W0_plus_L':screen}),'screen formula');req(events[0]['stage']=='necessary_screen','screen first')
 if screen<=0:
  req(len(events)==1,'no pairs after excluded screen');eq(row,enc({'status':'ZERO_DUAL_POSITIVE_CERTIFICATE_EXCLUDED','alpha_interval':old,'screen_upper':screen,'L':L,'ordered_pairs':0,'kernel_values':0,'true_alpha_excluded':False,'other_duals_excluded':False,'mode':mode}),'screen result');return
 coeff={k:tuple(rat(inp['coefficients'][k][n])for n in ['p0','p1','q'])for k in ['P','O']};G=[(F(0),F(0))for _ in range(3)];pos=1;completed=0
 for i,(C,A)in enumerate((C,A)for C in LABELS for A in LABELS):
  if pos==len(events):break
  e=events[pos];req(e['stage']=='before_pair','pair start');eq(e['data'],{'index':i,'C':list(C),'A':list(A)},'ordered pair');pos+=1
  if pos==len(events):break
  e=events[pos];req(e['stage']=='joint_pair','pair output');d=e['data'];n=len(set(C)&set(A));w=6 if C==A else 1 if n==0 else 3
  for k,v in [('index',i+1),('overlap',n),('weight',w)]:integer(d[k],v)
  eq(d['C'],list(C),'C');eq(d['A'],list(A),'A');req(type(d['values'])is list and len(d['values'])==3,'three kernels');vals=list(map(box,d['values']));truth=form(coeff[kind(C)],coeff[kind(A)],c,n)
  for j in range(3):req(vals[j][0]<=truth[j][0]<=truth[j][1]<=vals[j][1],'affine kernel containment');G[j]=add(G[j],scale(vals[j],w))
  req(type(d['cumulative'])is list and len(d['cumulative'])==3,'cumulative shape');[box(x)for x in d['cumulative']];eq(d['cumulative'],enc(G),'exact cumulative');pos+=1;completed+=1
  if i==224:break
 if pos<len(events):
  e=events[pos];req(e['stage']=='joint_grams'and completed==225,'joint grams');eq(e['data'],enc({'G':G,'pairs':225}),'retained grams');pos+=1
 req(pos==len(events),'choice event suffix')
 if row['status']=='INDETERMINATE_ARITHMETIC':
  req(row['ordered_pairs']is None and row['kernel_values']is None and type(row['error'])is str and row['error'],'arithmetic refusal');req(row['stage']==events[-1]['stage'],'refusal current');return
 req(len(events)==452 and events[-1]['stage']=='joint_grams','all225 pairs');u2=(max(F(0),G[0][0]),G[0][1]);raw=add(add(scale(G[0],4),G[1]),scale(G[2],-4));w2=(max(F(0),raw[0]),raw[1]);lin=E*upperroot(w2[1])+V*upperroot(u2[1]);lo=(nom[0]-lin+L)/8;hi=(nom[1]+lin+6*E*E+6*E*V)/8;final=max(lo,old[0]),min(hi,old[1]);req(final[0]<=final[1],'nonempty intersection');status='POSITIVE_CERTIFICATE'if final[0]>0 else'NEGATIVE_CERTIFICATE'if final[1]<0 else'INDETERMINATE_SIGN'
 eq(row,enc({'status':status,'alpha_interval':final,'spectral_alpha_interval':old,'G':G,'gradient_squared':w2,'adjoint_squared':u2,'L':L,'linear_error':lin,'ordered_pairs':225,'kernel_values':675,'screen_upper':screen,'true_alpha_excluded':False,'other_duals_excluded':False,'mode':mode}),'full certificate reconstruction')

def check(O,rf,elapsed,progress):
 O=Path(O);expected={'STARTED.json','WORKER_COMPLETE.json','RESULT.json','PARTIAL.json','EVENTS.ndjson'}|{m+s for m in MODES for s in ['.json','_INPUT.json']};req({p.name for p in O.iterdir()}==expected,'exact nine outputs')
 r=read(O/'RESULT.json');w=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');eq(read(O/'STARTED.json'),{'runtime_sha256':rf['worker_freeze'],'binding_sha256':sha(Path(rf['worker_path'])/'BINDING.json'),'output':str(O.resolve()),'no_retry':True},'started authorization')
 req(r['status']=='COMPLETE_NEW_SAVED_THREE_GRAM_ESTIMATOR'and w['status']=='COMPLETE_NEW_SAVED_THREE_GRAM_ONLY','completion');req(w['runtime_sha256']==rf['worker_freeze']and w['result_sha256']==sha(O/'RESULT.json'),'worker receipt');req(w['binding_sha256']==sha(Path(rf['worker_path'])/'BINDING.json'),'binding');number(r['seconds'],19);number(w['seconds'],19);number(elapsed,19.5);req(r['seconds']<=w['seconds']<=elapsed,'time order');req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=LIMIT,'worker RSS')
 for k,n in [('choices',2),('max_ordered_pairs',450),('max_kernel_values',1350),('native_oracle_calls',0),('old_moments_recomputed',0),('old_nominal_recomputed',0)]:integer(r[k],n)
 req(type(r['rows'])is list and len(r['rows'])==2,'two rows');events=[json.loads(s)for s in(O/'EVENTS.ndjson').read_text().splitlines()];integer(r['events'],len(events))
 for i,e in enumerate(events,1):integer(e['sequence'],i);req(set(e)=={'sequence','choice','stage','data'},'event fields')
 # Authenticate exact saved input extraction without replaying any old arithmetic.
 b=read(Path(rf['worker_path'])/'BINDING.json')
 def bound(d):req(sha(d['path'])==d['sha256'],'input hash');return read(d['path'])
 sr=bound(b['spectral']['result']);d=b['degree10']['events'];req(sha(d['path'])==d['sha256'],'source event hash');old=[json.loads(s)for s in Path(d['path']).read_text().splitlines()];req(len(old)==205,'source count');scalar=extract(old,'scalar_inputs',None)
 expected_prefix=[('before_input',{'role':k})for k in ['acceptance','receipt','root_freeze','worker','result','binding','acceptance','worker','receipt','root_freeze','result']]+[('before_source_event',{'index':i})for i in range(1,206)]
 pos=0
 for stage,data in expected_prefix:
  e=events[pos];req(e['choice']is None and e['stage']==stage,'input schedule');eq(e['data'],data,'input event');pos+=1
 for mode,spectral,row in zip(MODES,sr['rows'],r['rows']):
  req(spectral['mode']==mode,'source mode');gate=extract(old,'gate_inputs',mode);coeff={}
  for k in ['P','O']:
   p=extract(old,'polynomial',mode,k);q=extract(old,'residual_raw',mode,k);coeff[k]={'p0':p['p0'],'p1':p['p1'],'q':q['q']}
  inp={'c':scalar['c'],'coefficients':coeff,'nominal':gate['nominal'],'E_upper':spectral['E_upper'],'F_upper':spectral['F_upper'],'spectral_alpha_interval':spectral['alpha_interval']};eq(read(O/(mode+'_INPUT.json')),inp,'bound INPUT');e=events[pos];req(e['choice']==mode and e['stage']=='new_inputs','choice start');eq(e['data'],inp,'input event equality');pos+=1;start=pos
  while pos<len(events)and events[pos]['stage']!='choice_complete':req(events[pos]['choice']==mode,'choice identity');pos+=1
  req(pos<len(events),'choice complete');eq(events[pos]['data'],row,'complete copy');req(events[pos]['choice']==mode,'complete mode');eq(read(O/(mode+'.json')),row,'choice file');validate_choice(inp,row,events[start:pos],mode);pos+=1;progress({'stage':'choice_verified','choice':mode,'events':pos})
 req(len(events)==pos+1 and events[pos]['choice']is None and events[pos]['stage']=='complete'and events[pos]['data']=={},'final complete');eq(part,{'current':events[-1],'completed':2},'final partial');req(not {x['status']for x in r['rows']}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'},'contradictory signs')
 return{'status':'ACCEPTED_NEW_SAVED_THREE_GRAM_SCHEMA','count':2,'events':len(events),'result_sha256':sha(O/'RESULT.json'),'independent_screen_affine_forms_cumulatives_final_arithmetic':True,'original_scalar_moment_spectral_truth_inherited':True,'native_replay':False}
