from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial,isfinite
import json,hashlib,signal,time,resource,re
start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('50s saved arithmetic')));signal.alarm(50)
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-elliptic-b-transform-stretch';O=B/'native-elliptic-b-run-76350';R=B/'native-elliptic-b-root-review';D=Path(__file__).resolve().parent
checks=0;stage='pins'
def need(b,msg):
 global checks
 checks+=1
 if not b:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(n,d):(D/n).write_text(json.dumps(d,indent=2)+'\n')
Q=1<<192
def rnd(a,b):return F(a.__floor__() if False else (a*Q).__floor__(),Q),F((b*Q).__ceil__(),Q)
def iv(x):return (F(x),F(x))
def rd(x):return tuple(map(F,x))
def add(a,b):return rnd(a[0]+b[0],a[1]+b[1])
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[x*y for x in a for y in b];return rnd(min(z),max(z))
def inv(a):
 need(not a[0]<=0<=a[1],'nonzero divisor');return rnd(1/a[1],1/a[0])
def scale(a,x):return mul(a,iv(x))
def poly(n,x):
 # exact polynomial interval recurrence, no root-finding or physical call
 a=(F(1),F(1));b=x
 def aa(a,b):return a[0]+b[0],a[1]+b[1]
 def mm(a,b):
  z=[u*v for u in a for v in b];return min(z),max(z)
 if n==0:return a
 for k in range(1,n):a,b=b,mm(aa(mm(mm(x,b),iv(2*k+1)),mm(a,iv(-k))),iv(F(1,k+1)))
 return b
try:
 pf='76350a2216507351cfbcbced2751b706de62025e723a006abfafd4b096b3d6ed';need(sha(P/'FREEZE.json')==pf,'freeze')
 pins=json.loads((P/'FREEZE.json').read_text())['inputs']
 for n,h in pins.items():need(sha(n)==h,n)
 result=json.loads((O/'RESULT.json').read_text());done=json.loads((O/'WORKER_COMPLETE.json').read_text());acc=json.loads((R/'ROOT_ACCEPTANCE.json').read_text())
 need(sha(O/'RESULT.json')==done['result_sha256']==acc['result_sha256'],'result binding');need(done['freeze_sha256']==pf==acc['worker_freeze'],'source binding')
 paths=sorted((O/'ORACLES').glob('*.json'));need([p.name for p in paths]==[f'{i:04d}.json' for i in range(746)],'catalog files')
 catalog=[];lookup={}
 for p in paths:
  row=json.loads(p.read_text());s=F(row['s']);need(s>0 and s not in lookup,'catalog s');need(row['terms']==160 and row['derivative_side']=='ordinary' and row['status']=='CERTIFIED_TARGET','oracle schema')
  for key,width in zip(['A','Aprime'],row['widths']):
   a=rd(row[key]);need(a[0]<=a[1] and a[1]-a[0]==F(width)<=F(1,10**30),'oracle width')
  need(len(row['widths'])==2 and len(row['A'])==len(row['Aprime'])==2,'shape');need(F(row['A'][0])>0 and F(row['Aprime'][1])<0 and isfinite(row['seconds']) and row['seconds']>0,'sign/time')
  need(F(row['A'][0])<=F(17,60) and F(row['A'][1])>=1/(s*s+6),'analytic consistency')
  lookup[s]=row;catalog.append(s)
 rule0=json.loads((O/'GAUSS.json').read_text());rule=[(rd(a),rd(w)) for a,w in rule0['rule']];need(len(rule)==12,'rule size')
 for k,(x,w) in enumerate(rule):
  need(-1<x[0]<x[1]<1 and w[0]>0 and w[0]<=w[1],'rule intervals');need(poly(12,iv(x[0]))[0]*poly(12,iv(x[1]))[0]<0,'root bracket')
  if k:need(rule[k-1][0][1]<x[0],'root distinct')
 expected=[F(1),F(2)]
 for j in range(-28,3):
  a=F(2)**j
  for x,w in rule:expected.extend([a*(x[0]+3)/2,a*(x[1]+3)/2])
 need(catalog==expected,'all input coordinates/order')
 need([p['j'] for p in result['panels']]==list(range(-28,3)),'panels')
 sums={s:[iv(0),iv(0)] for s in [F(1),F(2)]}
 for saved in result['panels']:
  j=saved['j'];stage='panel '+str(j);a=F(2)**j;panel={s:[iv(0),iv(0)] for s in sums}
  for x,w in rule:
   tl=a*(x[0]+3)/2;th=a*(x[1]+3)/2;t=(tl,th);at=(F(lookup[th]['A'][0]),F(lookup[tl]['A'][1]));weight=scale(w,a/2);tt=mul(t,t)
   for s in sums:
    aa=rd(lookup[s]['A']);ap=rd(lookup[s]['Aprime']);den=sub(tt,iv(s*s));num=sub(mul(tt,at),scale(aa,s*s));g=mul(num,inv(den));hn=sub(mul(add(scale(aa,2*s),scale(ap,s*s)),den),scale(num,2*s));hh=mul(hn,inv(mul(den,den)))
    for k,v in enumerate([g,hh]):panel[s][k]=add(panel[s][k],mul(weight,v))
  for s in sums:
   for k in range(2):
    need(panel[s][k]==rd(saved['panel'][str(s)][k]),'panel interval');sums[s][k]=add(sums[s][k],panel[s][k]);need(sums[s][k]==rd(saved['cumulative'][str(s)][k]),'cumulative')
  need(isfinite(saved['seconds']) and saved['seconds']>0,'panel time')
 def atan(x,n):
  v=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)),F(0));return v,v+x**(2*n+1)/F(2*n+1)
 aa,bb=atan(F(1,5),32),atan(F(1,239),10);pi=(16*aa[0]-4*bb[1],16*aa[1]-4*bb[0]);factor=(2/pi[1],2/pi[0]);radius=F(1000,27)*F(4,25)**12
 def moment(n):return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1)),F(0))
 coarse=json.loads((B/'native-star-local-green-gram-run-41ebe'/'RESULT.json').read_text())['rows'];out=[]
 for row in result['rows']:
  s=F(row['s']);stage='final '+str(s);aa=rd(lookup[s]['A']);ap=rd(lookup[s]['Aprime']);c=sub(iv(1),scale(aa,s*s));e=add(scale(aa,2*s),scale(ap,s*s));tails=[iv(0),iv(0)]
  for n in range(16):
   weight=F((-1)**n,(2*n+1)*8**(2*n+1));tails=[add(tails[0],scale(c,weight)),add(tails[1],scale(e,weight))];c,e=sub(iv(moment(n+1)),scale(c,s*s)),sub(scale(c,2*s),scale(e,s*s))
  rem=F(12**16,33*8**33);tails=[add(tails[0],(F(0),rem)),add(tails[1],(F(0),rem/(2*s)))]
  for k,key in enumerate(['B','Bprime']):
   low=F(1,2**28)*(1/s**2 if k==0 else 2/s**3);v=mul(add(add(sums[s][k],tails[k]),(-radius,radius+low)),factor)
   if k:v=neg(v)
   need(v==rd(row[key]),'final interval');need(v[1]-v[0]==F(row['widths'][k])<=F(1,10**6),'final width');old=rd(coarse[1 if s==1 else 3]['bounds'][k]);need(old[0]<=v[0]<=v[1]<=old[1],'coarse containment')
  out.append({'s':str(s),'widths':row['widths'],'midpoints_display':[float(sum(rd(row[k]))/2) for k in ['B','Bprime']]})
 need(result['oracle_count']==746 and result['all_targets_met'] and not result['alpha_computed'],'final scope')
 partial=json.loads((O/'PARTIAL.json').read_text());need(partial['rows']==result['rows'] and partial['panels']==result['panels'],'final partial')
 need(sum(p['seconds'] for p in result['panels'])<=result['seconds']<=done['seconds']<60,'nested times');need(acc['external_shell_seconds']<60 and acc['sampled_whole_tree_peak']<=384*1048576,'resource receipt')
 reads={str(p):sha(p) for folder in [O,R] for p in folder.rglob('*') if p.is_file()};reads[str(P/'FREEZE.json')]=pf;write('READ_HASHES.json',reads)
 write('RESULT.json',{'status':'PASS_SAVED_ARITHMETIC','predicates':checks,'oracle_rows':746,'panels':31,'rows':out,'seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'oracle_or_integral_reruns':0});print('PASS',checks,time.monotonic()-start)
except BaseException as e:write('FAILURE.json',{'stage':stage,'error':repr(e)});raise
