from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import types,sys,json,hashlib
base=Path('/private/tmp/toe-24h-probes-20260908/native-fixed192-lazy-pivot-candidate')
def load(name,path):
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile(path.read_bytes(),str(path),'exec'),m.__dict__);return m
iv=load('interval',base/'interval.py');p=load('pivot',base/'pivot.py');count=0

def ck(v):
 global count
 if not v:raise ValueError('cold exact predicate')
 count+=1

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F())
def gamma(a):return(-a[1],a[0],-a[3],a[2])
v=[tuple(map(F,x)) for x in [(1,0,F(1,3),0),(0,1,0,F(1,3)),(F(1,7),0,F(2,5),0),(0,F(2,9),0,F(-1,11)),(F(1,2),0,0,0)]]
labels=(('pole',0,0,1,2),('pole',0,0,-1,2),('pole',0,1,1,2),('pole',0,1,-1,2),('append',0,0,1,1))
def fetch(i,j):return iv.rational(dot(v[i],v[j])),iv.rational(dot(v[i],gamma(v[j])))
log=[];result=p.run(fetch,labels,log.append,native=False,max_pairs=3)
ck(result['status']=='PASS_BOTH');ck(result['pairs']==2)
q=list(v);actual=[]
for saved in result['history']:
 a=q[saved['index']];b=gamma(a);r=dot(a,a);gg=[dot(a,x) for x in q];jj=[dot(a,gamma(x)) for x in q]
 def contains(x,f):return F(x[0],iv.S)<=f<=F(x[1],iv.S)
 ck(contains(saved['r'],r))
 for x,y in zip(saved['g'],gg):ck(contains(x,y))
 for x,y in zip(saved['j'],jj):ck(contains(x,y))
 actual.append((r,gg,[-x for x in jj]))
 q=[tuple(x[k]-a[k]*dot(a,x)/r-b[k]*dot(b,x)/r for k in range(4)) for x in q]
ck(all(dot(x,x)==0 for x in q))
cp=[x for x in log if x['stage']=='checkpoint'][-1]
for rows,(r,g,j) in zip(cp['coordinate_intervals'],actual):
 for row,nums in zip(rows,(g,j)):
  for (m,rad),num in zip(row,nums):
   lo,hi=F(m-rad,iv.S),F(m+rad,iv.S)
   if num==0:ck(lo<=0<=hi)
   elif num>0:ck(hi>=0 and hi*hi*r>=num*num and (lo<=0 or lo*lo*r<=num*num))
   else:ck(lo<=0 and lo*lo*r>=num*num and (hi>=0 or hi*hi*r<=num*num))
# Actual division endpoints, including negative numerator and nonexact quotient.
for a in [(-7,-2),(-3,5),(2,11)]:
 for b in [(3,7),(1,13)]:
  x=p.divide(a,b)
  for aa in a:
   for bb in b:ck(F(x[0],iv.S)<=F(aa,bb)<=F(x[1],iv.S))
# A failed entry must persist FAILED; no caller filesystem assumptions.
fail=[]
try:p.run(lambda i,j:((_ for _ in()).throw(ValueError('synthetic original-entry refusal'))),labels,fail.append,native=False)
except ValueError:ck(fail[-1]['stage']=='FAILED')
else:ck(False)
# Actual source mutation removes the minus on the second coordinate row.
source=(base/'pivot.py').read_text();bad=source.replace("[iv.neg(z) for z in h['j']]", "list(h['j'])")
ck(bad!=source);mp=Path(__file__).with_name('MUTANT_WRONG_J.py');mp.write_text(bad);mut=load('mutant',mp);ml=[];mut.run(fetch,labels,ml.append,native=False,max_pairs=3)
mc=[x for x in ml if x['stage']=='checkpoint'][-1];detected=0
for rows,(r,g,j) in zip(mc['coordinate_intervals'],actual):
 for (m,rad),num in zip(rows[1],j):
  lo,hi=F(m-rad,iv.S),F(m+rad,iv.S)
  if (num>0 and hi<0) or (num<0 and lo>0):detected+=1
ck(detected>0)
print(json.dumps({'status':'PASS','predicates':count,'four_dimensional_pairs':result['pairs'],'native_calls':0,'full_mock_calls':0},indent=2))
