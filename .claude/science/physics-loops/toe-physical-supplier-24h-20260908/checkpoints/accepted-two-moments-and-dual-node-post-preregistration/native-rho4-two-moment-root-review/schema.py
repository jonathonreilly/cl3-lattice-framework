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
def pi():
 def atan(x,n):
  a=sum(((-1)**k*x**(2*k+1)/F(2*k+1)for k in range(n)),F(0));return a,a+x**(2*n+1)/(2*n+1)
 a,b=atan(F(1,5),32),atan(F(1,239),10);return 16*a[0]-4*b[1],16*a[1]-4*b[0]
def check(out,rf,elapsed):
 out=Path(out);read=lambda n:json.loads((out/n).read_text());r=read('RESULT.json');w=read('WORKER_COMPLETE.json');p=read('PARTIAL.json');t=read('TAILS.json')
 req(set(x.name for x in out.iterdir())=={'STARTED.json','RESULT.json','WORKER_COMPLETE.json','PARTIAL.json','PANELS','TAILS.json'},'output/failures')
 req(read('STARTED.json')==rf['authorization'],'authorization')
 req(w['status']=='COMPLETE_CATALOG_INTEGRAL'and w['runtime_sha256']==rf['worker_freeze']and w['result_sha256']==sha(out/'RESULT.json'),'worker')
 req(all(type(x)in(int,float)and math.isfinite(x)and x>0 for x in(r['seconds'],p['seconds'],w['seconds'],elapsed))and r['seconds']<=p['seconds']<=w['seconds']<29 and w['seconds']<=elapsed<=30,'timing')
 req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(r['status']=='COMPLETE_NEW_RHO4_TWO_MOMENT_CERTIFICATE'and len(r['rows'])==2,'quantity')
 for k,v in [('panels',67),('nodes',1742),('tail_terms',40),('oracle_calls',0)]:req(type(r[k])is int and r[k]==v,'fixed '+k)
 req(p['stage']=='complete'and type(p['current'])is int and p['current']==2 and p['panels']==[f'PANELS/{j:02d}.json'for j in range(67)],'partial')
 req(set(x.name for x in(out/'PANELS').iterdir())=={f'{j:02d}.json'for j in range(67)},'panel census');totals=[(F(0),F(0)),(F(0),F(0))]
 for j in range(67):
  d=read(f'PANELS/{j:02d}.json');req(type(d['panel'])is int and d['panel']==j-64 and len(d['values'])==len(d['cumulatives'])==2,'panel id')
  totals=[add(totals[k],iv(d['values'][k]))for k in range(2)];req(totals==list(map(iv,d['cumulatives'])),'cumulative')
 req(totals==list(map(iv,p['sums'])),'middle')
 from math import factorial
 mm=[sum(F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b)for a in range(n+1)for b in range(n-a+1))for n in range(41)]
 req(len(t['moments'])==41 and list(map(F,t['moments']))==mm,'independent multinomial moments')
 pb=json.loads(Path(rf['producer_binding']).read_text());geom=json.loads(Path(pb['catalog_geometry_path']).read_text());first=geom['nodes'][0];eps=F(1,2**64);tl,tu=map(F,first['t_interval']);req(first['panel']==-64 and eps<tl<tu<2*eps,'first node')
 cat=json.loads((Path(pb['catalog']['directory'])/'RESULT.json').read_text());l,u=first['endpoint_ids']
 def endpoint(i):
  row=cat['rows'][i];path=Path(pb['catalog']['directory'])/row['path'];req(sha(path)==row['sha256'],'endpoint hash');return iv(json.loads(path.read_text())['A'])
 al=endpoint(u)[0];ah=endpoint(l)[1];lows=[(eps*al,eps*(ah+3*tu)),(eps-F(17,60)*eps**3/3,eps)];rads=[F(544,45)*F(1,4**52),F(128,3)*F(1,4**52)];pl,pu=pi()
 req(len(t['high_partials'])==len(t['high_remainders'])==len(t['quadrature_radii'])==len(t['low_intervals'])==2,'tail census')
 flags=[]
 for k,name in enumerate(('cminus','mu')):
  high=sum((F((-1)**n)*mm[n+k]/((2*n+1)*8**(2*n+1))for n in range(40)),F(0));rem=F(12**(40+k),81*8**81)
  req(F(t['high_partials'][k])==high and F(t['high_remainders'][k])==rem and F(t['quadrature_radii'][k])==rads[k]and iv(t['low_intervals'][k])==lows[k],'fixed tails')
  ans=mul(add(add(totals[k],(high,high+rem)),(lows[k][0]-rads[k],lows[k][1]+rads[k])),(2/pu,2/pl));row=r['rows'][k];width=ans[1]-ans[0];flag=width<=F(2,10**28);flags.append(flag)
  req(row['observable']==name and iv(row['interval'])==ans and F(row['width'])==width and F(row['target'])==F(2,10**28)and row['status']==('CERTIFIED_TARGET'if flag else'INDETERMINATE'),'new scalar certificate')
 req(type(r['all_targets_met'])is bool and r['all_targets_met']==all(flags),'overall flag')
 return {'status':'PASS_TWO_MOMENT_SAVED_SCHEMA','all_targets_met':all(flags),'result_sha256':sha(out/'RESULT.json'),'panels':67,'oracle_calls':0,'node_integrands_recomputed':False}
