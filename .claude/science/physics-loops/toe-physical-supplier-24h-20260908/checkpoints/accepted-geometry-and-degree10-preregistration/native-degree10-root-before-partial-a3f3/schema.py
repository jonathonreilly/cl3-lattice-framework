from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import isqrt,isfinite
import json,hashlib,re

def req(v,s):
 if not v:raise ValueError(s)
def rat(x):
 req(type(x)is str and len(x)<21000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');v=F(x);req(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=32768,'rational bound');return v
def box(x):
 req(type(x)is list and len(x)==2,'interval shape');a,b=map(rat,x);req(a<=b,'interval order');return(a,b)
def pt(x):return(F(x),F(x))
def add(*bs):return(sum((x[0]for x in bs),F(0)),sum((x[1]for x in bs),F(0)))
def scale(b,q):return(min(b[0]*q,b[1]*q),max(b[0]*q,b[1]*q))
def mul(a,b):
 vs=[x*y for x in a for y in b];return min(vs),max(vs)
def sqrt(b):
 req(b[0]>=0,'root positivity');S=1<<128;ends=[]
 for i,v in enumerate(b):
  k=isqrt(v.numerator*S*S//v.denominator)
  if i and k*k*v.denominator<v.numerator*S*S:k+=1
  ends.append(F(k,S))
 return tuple(ends)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(O,rf,elapsed,progress):
 O=Path(O);req(set(p.name for p in O.iterdir())=={'STARTED.json','EVENTS.ndjson','PARTIAL.json','RESULT.json','WORKER_COMPLETE.json','residual.json','variational.json'},'output census')
 r=json.loads((O/'RESULT.json').read_text());done=json.loads((O/'WORKER_COMPLETE.json').read_text());part=json.loads((O/'PARTIAL.json').read_text());ev=[json.loads(l)for l in(O/'EVENTS.ndjson').read_text().splitlines()]
 req(r['status']=='COMPLETE_FIXED_DEGREE10_CERTIFICATE' and type(r['choices'])is int and r['choices']==2 and len(r['rows'])==2,'result census')
 for k in('oracle_calls','new_covariance_calls'):req(type(r[k])is int and r[k]==0,'scope')
 req(done['status']=='COMPLETE_NEW_DEGREE10_ONLY'and done['runtime_sha256']==rf['worker_freeze']and done['result_sha256']==sha(O/'RESULT.json'),'completion pins')
 req(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'worker RSS')
 req(type(done['seconds'])in(int,float)and type(r['seconds'])in(int,float)and isfinite(done['seconds'])and 0<r['seconds']<=done['seconds']<19,'worker times')
 P=Path(rf['worker_path']);bh=sha(P/'BINDING.json');req(r['binding_sha256']==done['binding_sha256']==bh,'binding copies');auth=json.loads((Path(__file__).parent/'WORKER_AUTHORIZATION.json').read_text());req(json.loads((O/'STARTED.json').read_text())==auth,'start authorization')
 for i,e in enumerate(ev):req(type(e['sequence'])is int and e['sequence']==i+1 and set(e)=={'sequence','choice','stage','data'},'event structure')
 req(type(r['events'])is int and r['events']==len(ev)and 7<=len(ev)<=205,'event count')
 req(ev[0]=={'sequence':1,'choice':None,'stage':'binding','data':{'binding_sha256':bh,'native_oracle_calls':0}},'binding event');req(ev[1]['choice']is None and ev[1]['stage']=='scalar_inputs','scalar event')
 c=box(ev[1]['data']['c']);nu=box(ev[1]['data']['nu']);req(F(3,4)<c[0]<=c[1]<F(49,60)and 0<nu[0]<=nu[1]<16,'native scalar ranges')
 bind=json.loads((P/'BINDING.json').read_text());source=json.loads(Path(bind['files']['result']).read_text());req(c==scale(box(source['rows'][1]['interval']),F(1,3))and nu==box(source['rows'][2]['interval']),'accepted scalar copies')
 idx=2;statuses=[];pairlabels=list(combinations(range(6),2));pairs=[(C,A)for C in pairlabels for A in pairlabels if not set(C)&set(A)]
 stages=['moments','polynomial','source_moments','residual_raw']*2+['ordered_word']*90+['gate_inputs']
 for mode,row in zip(('residual','variational'),r['rows']):
  req(row==json.loads((O/(mode+'.json')).read_text())and row['mode']==mode,'choice copy')
  req(ev[idx]['choice']==mode and ev[idx]['stage']=='choice_start'and ev[idx]['data']=={'mode':mode},'choice start');idx+=1;body=[]
  while idx<len(ev)and ev[idx]['stage']!='choice_complete':body.append(ev[idx]);idx+=1
  req(idx<len(ev)and ev[idx]['choice']==mode and ev[idx]['data']=={'row':row},'choice complete');idx+=1
  req(all(e['choice']==mode for e in body)and[e['stage']for e in body]==stages[:len(body)],'choice stage prefix')
  status=row['status'];statuses.append(status)
  if status=='INDETERMINATE_ARITHMETIC':
   req(type(row['error'])is str and row['failed_stage']==(body[-1]['stage']if body else'choice_start')and len(body)<=len(stages),'arithmetic indeterminate');continue
  req(len(body)==99 and status in('INDETERMINATE_SIGN','POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'),'completed choice grammar')
  cls={}
  for off,k in((0,'P'),(4,'O')):
   for e in body[off:off+4]:req(e['data']['kind']==k,'class event')
   poly=body[off+1]['data'];raw=body[off+3]['data'];rr=box(raw['r2']);tt=box(raw['t2']);req(rr[1]>=0 and tt[1]>=0,'norm upper')
   cls[k]={'p0':rat(poly['p0']),'p1':rat(poly['p1']),'q':rat(raw['q']),'r2':(max(F(0),rr[0]),rr[1]),'t2':(max(F(0),tt[0]),tt[1])}
  nominal=pt(0);orbits={}
  for j,((C,A),e)in enumerate(zip(pairs,body[8:98])):
   d=e['data'];req(type(d['index'])is int and d['index']==j+1 and d['C']==list(C)and d['A']==list(A)and all(type(z)is int for z in d['C']+d['A']),'ordered pair census')
   kc='O'if C[0]//2==C[1]//2 else'P';ka='O'if A[0]//2==A[1]//2 else'P';tag=kc+ka
   if tag=='PP':tag+=''+str(sum({2*k,2*k+1}<=(set(C)|set(A))for k in range(3)))
   u,v=cls[kc]['p0'],cls[kc]['p1'];a,b,q=cls[ka]['p0'],cls[ka]['p1'],cls[ka]['q'];val=add(pt(u*a+4*q*u*b),scale(c,u*b+v*a+q*(2*u*a+4*v*b)))
   nominal=add(nominal,val);req(box(d['value'])==val and box(d['cumulative'])==nominal and d['orbit']==tag,'word arithmetic')
   old=orbits.setdefault(tag,{'count':0,'sum':pt(0)});old['count']+=1;old['sum']=add(old['sum'],val)
  gate=body[-1]['data'];req(box(gate['nominal'])==box(row['nominal'])==nominal,'nominal final')
  for k in('P','O'):
   for name in('p0','p1','q'):req(rat(gate['rows'][k][name])==cls[k][name],'candidate copies')
   for name in('r2','t2'):req(box(gate['rows'][k][name])==cls[k][name],'residual copies')
  E=sqrt(scale(add(scale(cls['P']['r2'],12),scale(cls['O']['r2'],3)),16));fs=pt(0)
  for k,n in(('P',12),('O',3)):
   e=scale(sqrt(cls[k]['r2']),4);f=scale(add(mul(scale(sqrt(pt(2)),2),e),sqrt(cls[k]['t2'])),4);fs=add(fs,scale(mul(f,f),n))
  FF=sqrt(fs);X=scale(sqrt(pt(15)),4);V=scale(sqrt(pt(30)),32);error=scale(add(mul(E,add(scale(X,2),E)),mul(E,V),mul(add(X,E),FF)),6)
  req(box(gate['E'])==E and box(gate['F'])==FF and box(gate['error'])==box(row['error'])==error,'propagation error')
  expected='POSITIVE_CERTIFICATE'if nominal[0]>error[1]else('NEGATIVE_CERTIFICATE'if nominal[1]<-error[1]else'INDETERMINATE_SIGN');req(status==expected,'sign gate')
  req(box(row['alpha_interval'])==((nominal[0]-error[1])/8,(nominal[1]+error[1])/8),'alpha interval')
  req(type(row['ordered_words'])is int and row['ordered_words']==90 and set(row['orbits'])==set(gate['orbits'])==set(orbits),'orbit membership')
  for k,v in orbits.items():
   for obj in(row['orbits'][k],gate['orbits'][k]):req(type(obj['count'])is int and obj['count']==v['count']and box(obj['sum'])==v['sum'],'orbit sums')
  progress({'stage':'schema_choice','mode':mode,'status':status})
 req(idx==len(ev)-1 and ev[-1]['choice']is None and ev[-1]['stage']=='complete'and ev[-1]['data']=={'rows':r['rows']},'completion event')
 req(part['stage']=='complete'and type(part['sequence'])is int and part['sequence']==len(ev)and part['choice']is None and part['rows']==r['rows']and part['event']==ev[-1],'partial final')
 req(not('POSITIVE_CERTIFICATE'in statuses and'NEGATIVE_CERTIFICATE'in statuses),'contradictory signs');req(type(r['sign_certified'])is bool and r['sign_certified']==any(x in('POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE')for x in statuses),'sign summary')
 return {'status':'ACCEPTED_DEGREE10_WARD_SCHEMA','count':2,'events':len(ev),'result_sha256':sha(O/'RESULT.json'),'events_sha256':sha(O/'EVENTS.ndjson'),'choice_statuses':statuses,'sign_certified':r['sign_certified'],'independent_word_and_error_reconciliation':True,'native_moment_identities_inherited':True,'native_oracle_calls':0}
