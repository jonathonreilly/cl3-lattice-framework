from fractions import Fraction as F
from math import comb,factorial
import time,json,hashlib
from pathlib import Path
start=time.monotonic();ncheck=0

def ck(x):
 global ncheck
 if not x:raise ValueError('exact tiny check')
 ncheck+=1
p={0:1};one=[]
for n in range(26):
 one.append(p.get(0,0));ck(one[-1]==comb(2*n,n))
 q={}
 for k,v in p.items():
  for step,c in ((0,2),(1,-1),(-1,-1)):q[k+step]=q.get(k+step,0)+c*v
 p=q
mom=[F(1)]+[F(0)]*25
for axis in range(3):mom=[sum(F(comb(n,k))*mom[k]*one[n-k] for k in range(n+1)) for n in range(26)]
for n in range(26):
 alt=sum(F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1))
 ck(mom[n]==alt);ck(mom[n]<=12**n)
# Exact signed geometric remainder for arbitrary non-native scalar nodes.
for x in (F(0),F(1,3),F(5),F(12)):
 for t in (F(8),F(17,2),F(32)):
  q=sum((-1)**n*x**n/t**(2*n+2) for n in range(26));r=x**26/(t**52*(t*t+x))
  ck(q+r==1/(t*t+x));ck(0<=r<=12**26/t**54)
S=1<<192
for x in (F(-11,7),F(-1,S*3),F(0),F(5,9)):
 lo=F((x*S).__floor__(),S);hi=F((x*S).__ceil__(),S)
 ck(lo<=x<=hi);ck(hi-lo<=F(1,S))
runtime=Path('/private/tmp/toe-24h-probes-20260908/native-cminus-saved-postcheck/RUNTIME_FREEZE.json')
f=json.loads(runtime.read_text());bad=[]
for path,h in f['inputs'].items():
 digest=hashlib.sha256(Path(path).read_bytes()).hexdigest()
 if digest!=h:bad.append(path)
ck(not bad)
print(json.dumps({'status':'PASS','exact_predicates':ncheck,'runtime_pins':len(f['inputs']),'bad_pins':bad,'seconds':time.monotonic()-start,'scope':'synthetic moments/tail/rounding and source pins; no check.run call','physical_calls':0},indent=2))
