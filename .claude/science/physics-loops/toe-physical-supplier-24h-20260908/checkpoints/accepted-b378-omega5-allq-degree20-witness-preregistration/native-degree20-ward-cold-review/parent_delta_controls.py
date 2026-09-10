"""Fabricated metadata only: no producer formula, accepted input, or native table."""
import json,tempfile,hashlib,types,copy
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
S=Path('/private/tmp/toe-24h-probes-20260908/native-degree20-ward-root-review/schema.py')
m=types.ModuleType('schema');exec(compile(S.read_text(),str(S),'exec'),m.__dict__)
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,(list,tuple)):return [enc(x)for x in v]
 if isinstance(v,dict):return {k:enc(x)for k,x in v.items()}
 return v
def wr(p,x):p.write_text(json.dumps(enc(x)))
def point(x):return (F(x),F(x))
with tempfile.TemporaryDirectory()as tmp:
 p=Path(tmp);o=p/'out';o.mkdir();w=p/'worker';w.mkdir();m.__file__=str(p/'schema.py');auth={};wr(p/'WORKER_AUTHORIZATION.json',auth);wr(o/'STARTED.json',auth)
 wr(p/'source.json',{'rows':[{}, {'interval':point(F(12,5))},{'interval':point(15)}]});wr(p/'omega.json',{'interval':point(100)})
 wr(w/'BINDING.json',{'files':{'result':str(p/'source.json')},'omega5':{'result':str(p/'omega.json')}});bh=m.sha(w/'BINDING.json');rf={'worker_freeze':'synthetic','worker_path':str(w)}
 ev=[];rows=[];mode=None
 def emit(st,d):ev.append({'sequence':len(ev)+1,'choice':mode,'stage':st,'data':enc(d)})
 emit('binding',{'binding_sha256':bh,'native_oracle_calls':0});emit('scalar_inputs',{'c':point(F(4,5)),'nu':point(15),'omega5':point(100)})
 z=point(0);cx=[z,z];G=[[cx for _ in range(6)]for _ in range(6)];op=[[[],[point(1),z]]]
 for mode in ['residual','variational']:
  emit('choice_start',{'mode':mode});cls={}
  for k in ['P','O']:
   emit('vacuum_inputs',{'kind':k,'table':G,'operators':[op]*4})
   for n in range(7):emit('vacuum_moment_raw',{'kind':k,'index':n,'real':z,'imaginary':z})
   emit('first_polynomial',{'kind':k,'coefficients':[F(0)]*3,'certified_pivots':[point(1)]*3});emit('source_inputs',{'kind':k,'b':op,'Db':op})
   for n in range(3):emit('source_moment_raw',{'kind':k,'index':n,'real':z,'imaginary':z})
   ct={'wick_states':1,'complex_products':1};emit('residual_raw',{'kind':k,'q':F(0),'r2':z,'t2':z,'counts':ct});cls[k]={'p':[F(0)]*3,'q':F(0),'r2':z,'t2':z,'counts':ct}
  seen=set();orbit={};count=0
  labels=list(combinations(range(6),2))
  for C in labels:
   for A in labels:
    if set(C)&set(A):continue
    kc='O'if C[0]//2==C[1]//2 else'P';ka='O'if A[0]//2==A[1]//2 else'P';ell=sum((2*k in C and 2*k+1 in A)or(2*k+1 in C and 2*k in A)for k in range(3));tag=kc+ka+(str(ell)if kc==ka=='P'else'')
    if tag not in seen:emit('cross_wick_raw',{'classes':[kc,ka],'ell':ell,'table':G,'OC':op,'OA':op,'base':cx,'correction':cx,'value':z});seen.add(tag)
    count+=1;emit('ordered_word',{'index':count,'C':C,'A':A,'ell':ell,'orbit':tag,'value':z,'cumulative':z});v=orbit.setdefault(tag,{'count':0,'sum':z});v['count']+=1
  emit('gate_inputs',{'rows':cls,'orbits':orbit,'nominal':z,'E':z,'F':z,'error':z})
  row={'mode':mode,'status':'INDETERMINATE_SIGN','nominal':z,'error':z,'alpha_interval':z,'ordered_words':90,'cross_wick_classes':5,'orbits':orbit};rows.append(enc(row));wr(o/(mode+'.json'),row);emit('choice_complete',{'row':row})
 mode=None;emit('complete',{'rows':rows});assert len(ev)==255
 r={'status':'COMPLETE_FIXED_DEGREE20_CERTIFICATE','rows':rows,'choices':2,'oracle_calls':0,'new_covariance_calls':0,'binding_sha256':bh,'sign_certified':False,'seconds':1,'events':255}
 def save():
  wr(o/'RESULT.json',r);wr(o/'WORKER_COMPLETE.json',{'status':'COMPLETE_NEW_DEGREE20_ONLY','runtime_sha256':'synthetic','result_sha256':m.sha(o/'RESULT.json'),'binding_sha256':bh,'seconds':2,'rss_bytes':1000});wr(o/'PARTIAL.json',{'stage':'complete','sequence':255,'choice':None,'rows':r['rows'],'event':ev[-1],'seconds':.9});(o/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev))
 save();checks=[]
 try:m.check(o,rf,1.5,lambda _:None)
 except ValueError as exc:assert str(exc)=='worker times';checks.append('done later than root rejected')
 else:raise AssertionError('root time')
 for event in ev:
  if event['stage']=='choice_complete':
   event['data']=copy.deepcopy(event['data']);event['data']['row']['ordered_words']=90.0;break
 save()
 try:m.check(o,rf,3,lambda _:None)
 except ValueError as exc:assert str(exc)=='choice complete';checks.append('float nested event copy rejected')
 else:raise AssertionError('typed event copy')
 print(json.dumps({'scope':'two affected fabricated255 cases only','passed':checks,'native_inputs':0}))
