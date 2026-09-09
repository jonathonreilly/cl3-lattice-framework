from pathlib import Path
from fractions import Fraction as F
import json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/native-stationary-pole-scalar-batch-design/POLES.json')
r=json.loads(p.read_text())['rows'];n=0
def ck(x):
 global n
 if not x:raise ValueError('exact ledger gate')
 n+=1
lo=[];hi=[]
for x in r:
 a,b=map(F,x['s_interval']);c,d=map(F,x['weight']);lo.append(a);hi.append(b)
 ck(F(1,128)<=a<=b<=16);ck(F(1,2048)<=c<=d<=2);ck((b-a)/2<=F(1,2**140));ck((d-c)/2<=F(1,2**140))
for i in range(66):
 for j in range(i+1,66):ck(lo[j]-hi[i]>=F(1,2048))
g=lambda s:4*(s+(s+1)*s*s/6)
g1=lambda s:4*((1+s)+(s*s+(s+1)*(2*s+s*s))/6)
ck(2*g(F(16))*2048<2**24);ck(g1(F(16))<2**24)
eA=F(2**37,10**30);en=F(1,2**60)
# Square rational upper comparisons; no square-root evaluation.
for e,target in [(eA,F(1,10**6)),(en,F(2,10**6))]:
 ck(target>1056*e);ck(4*318*1056*e<(target-1056*e)**2)
ck(F(3005,10**6)<F(1,200));ck(528*F(2,7)*F(7,8)**256<F(1,10**10))
print(json.dumps({'status':'PASS_GEOMETRY_AND_RATIONAL_ONLY','predicates':n,'pole_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'physical_calls':0}))
