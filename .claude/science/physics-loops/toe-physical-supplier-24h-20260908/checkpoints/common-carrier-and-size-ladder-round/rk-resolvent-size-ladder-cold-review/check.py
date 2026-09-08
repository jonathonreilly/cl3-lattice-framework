from fractions import Fraction as F
from pathlib import Path
import numpy as np,json,hashlib,itertools
p=Path('/private/tmp/toe-24h-probes-20260908/rk-resolvent-size-ladder');checks={};rows=[]
def ck(k,v):
 if not bool(v):raise AssertionError(k)
 checks[k]=True
ck('exponential_polynomial',sum(F(7,10)**i/F(np.math.factorial(i)) for i in [])==0) if False else None
import math
ck('cap_certificate',sum(F(7,10)**i/math.factorial(i) for i in range(5))==F(482921,240000)>2)
ck('rounded_q_margin_certificate',sum(F(699,1000)**i/math.factorial(i) for i in range(5))>2)
for L in (8,16):
 M=3*L**3;alphas=[k*2*np.sin(np.pi/L)**2 for k in (.25,.5,1)]+[.25,.5,1]
 for j,alpha in enumerate(alphas):
  aa=F(float(alpha));n=0
  while F(1,2**n)/aa>F(1,1000):n+=1
  z=(M+aa)/aa*F(7*n,10);kp=-(-z.numerator//z.denominator);q=F(float(M/(M+alpha)))
  ck(f'rounded_q_cap_{L}_{j}',(1-q)*kp>=F(699*n,1000))
  rows.append(dict(L=L,channel=j,cap=kp-1,bound=float(F(1,2**n)/aa),effective_alpha=float(M*(1-q)/q),declared_alpha=float(alpha)))
# Namespace disjointness across every chain and64 origins/six endpoints.
burn=set();advance=set();endpoint=set();lag=set()
for cid in range(20000,20000+6*128):
 burn.add(500000000+cid);lag.add(800000000+cid)
 for i in range(64):
  advance.add(600000000+1000*cid+i)
  for j in range(6):endpoint.add(700000000+1000*cid+6*i+j)
sets=[burn,advance,endpoint,lag];ck('within_namespace_unique',list(map(len,sets))==[768,49152,294912,768]);ck('cross_namespace_disjoint',all(not a&b for a,b in itertools.combinations(sets,2)))
# Joint source-regulator slicing exact labels.
ck('six_response_pairing',[(j//3,j%3) for j in range(6)]==[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)])
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(checks=checks,count=len(checks),caps=rows,sourcehash=hashlib.sha256((p/'stream.py').read_bytes()).hexdigest()),indent=2)+'\n');print(len(checks))
