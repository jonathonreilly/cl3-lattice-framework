from pathlib import Path
from fractions import Fraction as F
import types,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-selected-principal-frame-design')
def load(n):
 m=types.ModuleType(n);exec(compile((P/(n+'.py')).read_bytes(),str(P/(n+'.py')),'exec'),m.__dict__);return m
c=load('candidate');r=load('core');s=load('seed');checks=0
for e in(F(1,8),F(1,2),F(2)):
 G=[[F(1),F(1)],[F(1),1+e*e]];T=c.propose(G);exact=[[F(1),-1/e],[F(0),1/e]];assert T==exact;checks+=1
 v=r.certificate(G,[[F(0)]*2 for _ in range(2)],T,[[F(1),F(0)],[F(0),F(1)]]);assert v['status']=='CERTIFIED_ENCLOSURE'and v['entry_radius']==0 and v['width_pass'];checks+=1
for i in range(396):
 n,z=divmod(i,6);v,p=divmod(z,2);eta=2*p-1;chi=1 if v==0 else-1
 for g in(0,1):assert s.seed(i,g)=={(6*n+v,g):F(-eta*chi,2),(6*n+3+v,g):F(1,2)};checks+=1
for G in ([[F(0)]],[[F(-1)]],[[F(1),F(2)],[F(2),F(1)]]):
 try:c.propose(G)
 except c.CandidateFailure:checks+=1
 else:raise AssertionError('nonpositive candidate')
x=(1<<2048)-1;assert c.nearest(x,1)==x and (2*x+1).bit_length()==2049;checks+=1
print(json.dumps({'checks':checks,'status':'PASS_MATH_WITH_CAP_FINDING','native_calls':0,'unguarded_nearest_temporary_bits':2049}))
