from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
import json,gzip,hashlib
P=Path('/private/tmp/toe-24h-probes-20260908');O=P/'native-reference-vacuum-scalar-run-e46bc';S=2**192;n=0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(v):
 global n
 if not v:raise ValueError('saved certificate mismatch')
 n+=1
def q(a,b=None):
 b=a if b is None else b;a=F(a);b=F(b)
 return (F((a*S).numerator//(a*S).denominator,S),F(-((-b*S).numerator//(-b*S).denominator),S))
def plus(a,b):return q(a[0]+b[0],a[1]+b[1])
def times(a,b):
 v=[x*y for x in a for y in b];return q(min(v),max(v))
def scale(a,b):return times(a,q(b))
def neg(a):return(-a[1],-a[0])
def readiv(a):return tuple(map(F,a))
r=json.loads((O/'RESULT.json').read_text());d=json.loads((O/'WORKER_COMPLETE.json').read_text());inp=json.loads((P/'native-reference-vacuum-scalar-design/INPUTS.json').read_text());ck(d['result_sha256']==sha(O/'RESULT.json'));ck(d['status']=='COMPLETE');ck(r['status']=='CERTIFIED_TARGET')
roles={k:v for k,v in inp.items() if k!='decompressed_sha256'};ck(set(r['input_hashes'])==set(roles))
for k,v in roles.items():ck(sha(v)==r['input_hashes'][k])
b=gzip.decompress(Path(inp['catalogue']).read_bytes());ck(hashlib.sha256(b).hexdigest()==inp['decompressed_sha256']);cat=json.loads(b);rule=json.loads(Path(inp['gauss']).read_text())['rule'];acc=q(0);idx=2
ck(len(r['panels'])==31)
for j,row in zip(range(-28,3),r['panels']):
 a=F(2)**j;piece=q(0)
 for nodes,weights in rule:
  l,u=[a*(3+F(t))/2 for t in nodes];left,right=cat[f'{idx:04d}.json'],cat[f'{idx+1:04d}.json'];idx+=2
  ck(F(left['s'])==l and F(right['s'])==u)
  ai=q(F(right['A'][0]),F(left['A'][1]));value=plus(q(1),neg(times(times(q(l,u),q(l,u)),ai)));piece=plus(piece,times(q(*readiv(weights)),value))
 piece=scale(piece,a/2);acc=plus(acc,piece);ck(row['j']==j);ck(readiv(row['integral'])==piece);ck(readiv(row['cumulative'])==acc)
ck(idx==746)
def mom(k):return sum(F(factorial(k),factorial(a)*factorial(b)*factorial(k-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(k-a-b),k-a-b) for a in range(k+1) for b in range(k-a+1))
tail=q(0)
for k in range(16):tail=plus(tail,q(F((-1)**k)*mom(k+1)/((2*k+1)*8**(2*k+1))))
radius=F(400,9)*F(4,25)**12;rem=F(12**17,33*8**33);ck(F(r['middle_radius'])==radius);ck(F(r['high_remainder'])==rem)
def atan(z):
 a=sum((F((-1)**k,(2*k+1)*z**(2*k+1)) for k in range(48)),F(0));return q(a,a+F(1,97*z**97))
pi=plus(scale(atan(5),16),scale(atan(239),-4));inv=q(1/pi[1],1/pi[0]);mu=times(scale(inv,2),plus(plus(acc,tail),q(-radius,radius+F(1,2**28)+rem)));ck(mu==readiv(r['mu']));ca=scale(mu,F(1,3));ck(ca==readiv(r['cA']));ck(ca[0]<=mu[0]/3<=mu[1]/3<=ca[1]);ck(mu[1]-mu[0]==F(r['width'])<=F(1,10**6));ck(ca[1]-ca[0]<F(1,10**6));ck(mu[0]>0)
old=(mu[0]/3-ca[0]<=F(1,S) and ca[1]-mu[1]/3<=F(1,S));ck(not old)
print(json.dumps({'status':'PASS_SAVED_ARITHMETIC','predicates':n,'physical_oracle_calls':0,'new_integration':False,'original_monitor_status':'FAILED_REFERENCE_CONSTANT_INTERVAL_PRESERVED','old_one_ulp_guard':old,'result_sha256':sha(O/'RESULT.json'),'mu':r['mu'],'cA':r['cA']},indent=2))
