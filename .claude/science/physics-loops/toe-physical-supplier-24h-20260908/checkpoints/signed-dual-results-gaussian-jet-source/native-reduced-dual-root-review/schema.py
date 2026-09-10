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

SCALES=[F(0),F(1,2),F(1),F(3,2),F(2)]
NAMES=[('w','Hw','Ju','HJu'),('u','Hu')]
ENTRY_ORDER=[(a,b)for names in NAMES for i,a in enumerate(names)for b in names[i:]]+[('r','w'),('r','Ju'),('s','u')]
def kind(a):return 'O'if a[0]//2==a[1]//2 else'P'
def extract(ev,stage,choice,k=None):
 xs=[x['data']for x in ev if x['stage']==stage and x['choice']==choice and(k is None or x['data'].get('kind')==k)];req(len(xs)==1,'source unique field');return xs[0]
def capped(x):req(max(x.numerator.bit_length(),x.denominator.bit_length())<=32768,'proposal rational cap');return x
def midpoint(x):return capped((x[0]+x[1])/2)
def propose(M):
 def grid(n,d):
  if d<=0:return F(0)
  x=max(F(0),min(F(4),capped(n/d)));q=1<<64;return capped(F(x.numerator*q//x.denominator,q))
 try:
  B=M['B'];G=M['A'];t=grid(midpoint(B[0][1]),midpoint(B[1][1]));g=[[midpoint(x)for x in row]for row in G];n=capped(g[0][1]-t*(g[0][3]+g[1][2])+t*t*g[2][3]);d=capped(g[1][1]-2*t*g[1][3]+t*t*g[3][3]);s=grid(n,d);return t,s,False
 except(ValueError,ZeroDivisionError):return F(0),F(0),True

def qform(G,c):
 z=(F(0),F(0))
 for i,x in enumerate(c):
  z=add(z,scale(G[i][i],x*x))
  for j in range(i+1,len(c)):z=add(z,scale(G[i][j],2*x*c[j]))
 return z
def channel(M,t,s,l):
 a=qform(M['A'],[F(1),-l*s,-l*t,l*s*t]);b=qform(M['B'],[F(-1),l*t]);v=M['correction'];cor=scale(add(add(scale(v[0],s),scale(v[1],-s*t)),scale(v[2],-t)),l);return a,b,cor

def counts(x,old=None):
 req(set(x)=={'wick_states','complex_products'},'count fields')
 for k,cap in [('wick_states',8192),('complex_products',200000)]:req(type(x[k])is int and 0<=x[k]<=cap,'literal Wick bounds');req(old is None or x[k]>=old[k],'count monotonic')

def validate_choice(inp,row,ev,mode):
 req(row['mode']==mode,'row mode');cache={};classkeys={};channels=[];sums=[[(F(0),F(0))for _ in range(3)]for _ in SCALES];pos=0
 refused=row['status']=='INDETERMINATE_ARITHMETIC'
 def take(stage):
  nonlocal pos
  if pos==len(ev):raise EOFError()
  e=ev[pos];req(e['stage']==stage,'stage '+stage);pos+=1;d=e['data'];req(type(d)is dict,'stage data')
  if stage in ['raw_channel_forms','certified_channel','aggregate_scale_forms','scale_certificate']:
   for k in ['a2','b2','correction']:box(d[k])
   if stage=='scale_certificate':box(d['alpha_interval']);rat(d['a_upper']);rat(d['b_upper'])
  return d
 try:
  for index,label in enumerate(LABELS):
   eq(take('before_channel'),{'index':index,'label':list(label)},'fixed channel');cl=kind(label)
   if pos<len(ev)and ev[pos]['stage']=='new_dual_covariance':
    d=take('new_dual_covariance');integer(d['index'],index);req(d['class']==cl,'covariance class');raw={'G':d['G'],'operators':d['operators']};key=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest();req(d['key']==key and key not in cache,'new signature');req(cl not in classkeys or classkeys[cl]==key,'class key')
    req(type(raw['G'])is list and len(raw['G'])==9,'nine dependent vectors')
    for rr in raw['G']:
     req(type(rr)is list and len(rr)==9,'covariance shape')
     for value in rr:req(type(value)is list and len(value)==2,'complex box');box(value[0]);box(value[1])
    req(set(raw['operators'])=={'w','Hw','Ju','HJu','u','Hu','r','s'},'operator labels')
    sizes={'w':2,'Hw':4,'Ju':2,'HJu':6,'u':2,'Hu':3,'r':4,'s':4}
    for name,terms in raw['operators'].items():
     req(type(terms)is list and len(terms)==sizes[name],'operator count')
     for term in terms:
      req(type(term)is list and len(term)==2 and type(term[0])is list and len(term[0])<=3,'operator term');req(all(type(i)is int and 0<=i<9 for i in term[0]),'word indices');req(type(term[1])is list and len(term[1])==2,'complex coefficient');box(term[1][0]);box(term[1][1])
    A=[[None]*4 for _ in range(4)];B=[[None]*2 for _ in range(2)];cor=[];prev=None
    for j,(left,right)in enumerate(ENTRY_ORDER):
     eq(take('before_dual_entry'),{'left':left,'right':right},'entry schedule');d=take('dual_entry');req(d['left']==left and d['right']==right,'entry identity');req(type(d['value'])is list and len(d['value'])==2,'complex entry');re,im=map(box,d['value']);counts(d['counts'],prev);prev=d['counts']
     if j<13:
      names=NAMES[0]if j<10 else NAMES[1];matrix=A if j<10 else B;i1=names.index(left);i2=names.index(right)
      if i1==i2:
       if not(im[0]<=0<=im[1]and re[1]>=0):req(refused and pos==len(ev),'diagonal refusal');raise EOFError()
       re=(max(F(0),re[0]),re[1])
      matrix[i1][i2]=matrix[i2][i1]=re
     else:cor.append(re)
    M={'A':A,'B':B,'correction':cor,'words':171,'counts':prev};d=take('new_dual_grams');eq(d,enc({'key':key,'data':M}),'full Gram from entries');cache[key]=M;req(len(cache)<=2,'two cached signatures');classkeys[cl]=key
   else:
    d=take('inherited_identical_channel_grams');integer(d['index'],index);key=d['key'];req(key in cache and classkeys.get(cl)==key,'existing exact class signature')
   M=cache[key];t,s,fallback=propose(M);d=take('dyadic_proposal');integer(d['index'],index);eq(d['t'],str(t),'proposal t');eq(d['s'],str(s),'proposal s');req(type(d['fallback'])is str and d['fallback'] if fallback else d['fallback']is None,'proposal fallback')
   for j,l in enumerate(SCALES):
    a,b,cor=channel(M,t,s,l);eq(take('raw_channel_forms'),enc({'t':t,'s':s,'lambda':l,'a2':a,'b2':b,'correction':cor}),'raw forms');
    if a[1]<0 or b[1]<0:
     req(refused and pos==len(ev),'negative upper refusal');raise EOFError()
    a=(max(F(0),a[0]),a[1]);b=(max(F(0),b[0]),b[1]);d=take('certified_channel');eq(d,enc({'index':index,'candidate':j,'t':t,'s':s,'lambda':l,'a2':a,'b2':b,'correction':cor}),'certified channel')
    for k,z in enumerate([a,b,cor]):sums[j][k]=add(sums[j][k],z)
   channels.append({'label':list(label),'key':key,'t':t,'s':s})
  E=rat(inp['E_upper']);V=rat(inp['F_upper']);L=lower(E,V);nom=box(inp['nominal']);old=box(inp['spectral_alpha_interval']);lo,hi=old;certs=[]
  for l,(a2,b2,cor)in zip(SCALES,sums):
   eq(take('aggregate_scale_forms'),enc({'lambda':l,'a2':a2,'b2':b2,'correction':cor,'E':E,'F':V,'remainder':L,'nominal':nom}),'aggregate forms');a=upperroot(a2[1]);b=upperroot(b2[1]);lin=E*a+V*b;al=((nom[0]+cor[0]-lin+L)/8,(nom[1]+cor[1]+lin+6*E*E+6*E*V)/8);eq(take('scale_certificate'),enc({'lambda':l,'a2':a2,'b2':b2,'correction':cor,'a_upper':a,'b_upper':b,'alpha_interval':al}),'scale certificate');certs.append({'lambda':l,'a2':a2,'b2':b2,'correction':cor,'linear_error':lin,'alpha_interval':al});lo=max(lo,al[0]);hi=min(hi,al[1])
  if lo>hi:req(refused and pos==len(ev),'intersection refusal');raise EOFError()
  expected={'status':'POSITIVE_CERTIFICATE'if lo>0 else'NEGATIVE_CERTIFICATE'if hi<0 else'INDETERMINATE_SIGN','alpha_interval':(lo,hi),'spectral_alpha_interval':old,'candidates':certs,'channels':channels,'unique_gram_sets':len(cache),'actual_Wick_words':171*len(cache),'logical_Wick_words':2565,'sharp_remainder_lower':L,'physical_trial_changed':False,'mode':mode};eq(row,enc(expected),'final signed-dual result');req(pos==len(ev),'no extra events')
 except EOFError:
  req(refused,'truncated non-refusal')
 if refused:
  req(pos==len(ev)and row['unique_gram_sets']is None and row['actual_Wick_words']is None and type(row['error'])is str and row['error'],'refusal fields');req(row['stage']==(ev[-1]['stage']if ev else'new_inputs'),'refusal current')

def check(O,rf,elapsed,progress):
 O=Path(O);expected={'STARTED.json','WORKER_COMPLETE.json','RESULT.json','PARTIAL.json','EVENTS.ndjson'}|{m+s for m in MODES for s in ['.json','_INPUT.json']};req({p.name for p in O.iterdir()}==expected,'exact nine outputs')
 r=read(O/'RESULT.json');w=read(O/'WORKER_COMPLETE.json');part=read(O/'PARTIAL.json');eq(read(O/'STARTED.json'),{'runtime_sha256':rf['worker_freeze'],'binding_sha256':sha(Path(rf['worker_path'])/'BINDING.json'),'output':str(O.resolve()),'no_retry':True},'started authorization')
 req(r['status']=='COMPLETE_NEW_REDUCED_DUAL_ESTIMATOR'and w['status']=='COMPLETE_NEW_REDUCED_DUAL_ONLY','completion');req(w['runtime_sha256']==rf['worker_freeze']and w['result_sha256']==sha(O/'RESULT.json'),'worker receipt');req(w['binding_sha256']==sha(Path(rf['worker_path'])/'BINDING.json'),'binding');number(r['seconds'],29);number(w['seconds'],29);number(elapsed,29.5);req(r['seconds']<=w['seconds']<=elapsed,'time order');req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=LIMIT,'worker RSS')
 for k,n in [('choices',2),('max_unique_gram_sets',4),('max_actual_Wick_words',684),('logical_Wick_words',5130),('native_oracle_calls',0),('old_moments_recomputed',0),('old_nominal_recomputed',0)]:integer(r[k],n)
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
  inp={'c':scalar['c'],'nu':scalar['nu'],'coefficients':coeff,'nominal':gate['nominal'],'E_upper':spectral['E_upper'],'F_upper':spectral['F_upper'],'spectral_alpha_interval':spectral['alpha_interval']};eq(read(O/(mode+'_INPUT.json')),inp,'bound INPUT');e=events[pos];req(e['choice']==mode and e['stage']=='new_inputs','choice start');eq(e['data'],inp,'input event equality');pos+=1;start=pos
  while pos<len(events)and events[pos]['stage']!='choice_complete':req(events[pos]['choice']==mode,'choice identity');pos+=1
  req(pos<len(events),'choice complete');eq(events[pos]['data'],row,'complete copy');req(events[pos]['choice']==mode,'complete mode');eq(read(O/(mode+'.json')),row,'choice file');validate_choice(inp,row,events[start:pos],mode);pos+=1;progress({'stage':'choice_verified','choice':mode,'events':pos})
 req(len(events)==pos+1 and events[pos]['choice']is None and events[pos]['stage']=='complete'and events[pos]['data']=={},'final complete');eq(part,{'current':events[-1],'completed':2},'final partial');req(not {x['status']for x in r['rows']}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'},'contradictory signs')
 return{'status':'ACCEPTED_NEW_REDUCED_DUAL_SCHEMA','count':2,'events':len(events),'result_sha256':sha(O/'RESULT.json'),'independent_proposal_forms_correction_intersection':True,'raw_Wick_and_original_scalar_spectral_truth_inherited':True,'native_replay':False}
