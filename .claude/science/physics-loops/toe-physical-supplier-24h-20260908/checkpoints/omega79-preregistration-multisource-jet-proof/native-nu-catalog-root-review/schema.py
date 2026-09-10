from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib,math
S=1<<192
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def iv(a):req(isinstance(a,list)and len(a)==2,'endpoints');x,y=map(F,a);req(x<=y,'ordered');return x,y
def rnd(a,b):return F((a*S).__floor__(),S),F((b*S).__ceil__(),S)
def add(a,b):return rnd(a[0]+b[0],a[1]+b[1])
def mul(a,b):q=[x*y for x in a for y in b];return rnd(min(q),max(q))
def moments():
 # Independent binomial convolution of three identical one-coordinate moments.
 single=[comb(2*n,n)for n in range(42)];two=[sum(comb(n,k)*single[k]*single[n-k]for k in range(n+1))for n in range(42)]
 return {n:sum(comb(n,k)*two[k]*single[n-k]for k in range(n+1))for n in range(2,42)}
def pi():
 def atan(x,n):
  a=sum(((-1)**k*x**(2*k+1)/F(2*k+1)for k in range(n)),F(0));return a,a+x**(2*n+1)/(2*n+1)
 a,b=atan(F(1,5),32),atan(F(1,239),10);return 16*a[0]-4*b[1],16*a[1]-4*b[0]
def check(out,rf,elapsed):
 out=Path(out);read=lambda n:json.loads((out/n).read_text());r=read('RESULT.json');w=read('WORKER_COMPLETE.json');p=read('PARTIAL.json');t=read('TAIL.json')
 req(set(x.name for x in out.iterdir())=={'STARTED.json','RESULT.json','WORKER_COMPLETE.json','PARTIAL.json','PANELS','TAIL.json'},'output/failures')
 req(read('STARTED.json')==rf['authorization'],'authorization')
 req(w['status']=='COMPLETE_CATALOG_INTEGRAL'and w['runtime_sha256']==rf['worker_freeze']and w['result_sha256']==sha(out/'RESULT.json'),'worker')
 req(all(type(x)in(int,float)and math.isfinite(x)and x>0 for x in(r['seconds'],p['seconds'],w['seconds'],elapsed))and r['seconds']<=p['seconds']<=w['seconds']<29 and w['seconds']<=elapsed<=30,'timing')
 req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(r['observable']=='nu=E_X_power_3_over_2'and type(r['middle_width_gate'])is bool,'quantity')
 for k,v in [('panels',67),('nodes',1742),('tail_terms',40),('oracle_calls',0)]:req(type(r[k])is int and r[k]==v,'fixed '+k)
 req(r['new_catalog_only_integral']is True,'new integral scope')
 req(p['stage']=='complete'and type(p['current'])is int and p['current']==2 and p['panels']==[f'PANELS/{j:02d}.json'for j in range(67)],'partial')
 req(set(x.name for x in(out/'PANELS').iterdir())=={f'{j:02d}.json'for j in range(67)},'panel census');total=(F(0),F(0))
 for j in range(67):
  d=read(f'PANELS/{j:02d}.json');req(type(d['panel'])is int and d['panel']==j-64,'panel id');total=add(total,iv(d['value']));req(total==iv(d['cumulative']),'cumulative')
 req(total==iv(r['middle'])==iv(p['sum']),'middle')
 mm=moments();req(set(t['moments'])=={str(k)for k in mm}and all(F(t['moments'][str(k)])==v for k,v in mm.items()),'40 exact moments')
 high=sum((F((-1)**n)*mm[n+2]/((2*n+1)*8**(2*n+1))for n in range(40)),F(0));rem=F(12**42,81*8**81);rad=F(256,4**52);eps=F(1,2**64);low=6*eps-eps**3/3;lowhi=low+F(17,60)*eps**5/5
 for key,x in [('high_partial',high),('high_remainder',rem),('quadrature_radius',rad)]:req(F(r[key])==F(t[key])==x,'tail '+key)
 req(iv(r['low_interval'])==iv(t['low_interval'])==(low,lowhi),'low subtraction')
 pl,pu=pi();expected=mul(add(add(total,(high,high+rem)),(low-rad,lowhi+rad)),(2/pu,2/pl));req(iv(r['interval'])==expected,'Machin final interval')
 width=expected[1]-expected[0];gate=total[1]-total[0]<=F(2,10**25);req(r['middle_width_gate']==gate and F(r['width'])==width and F(r['target'])==F(2,10**19),'width gates');req(r['status']==('CERTIFIED_TARGET'if gate and width<=F(2,10**19)else'INDETERMINATE'),'honest scientific status')
 return {'status':'PASS_NU_SAVED_SCHEMA','scientific_status':r['status'],'result_sha256':sha(out/'RESULT.json'),'panels':67,'tail_terms':40,'oracle_calls':0,'individual_panel_integrands_recomputed':False}
