from pathlib import Path
from fractions import Fraction as F
import hashlib,json,types
P=Path('/private/tmp/toe-24h-probes-20260908/native-selected-principal-frame-design')
def module(name,h):
 p=P/(name+'.py');b=p.read_bytes()
 if hashlib.sha256(b).hexdigest()!=h:raise ValueError('source hash')
 m=types.ModuleType(name);exec(compile(b,str(p),'exec'),m.__dict__);return m
v=module('dyadic_residual','dadbbdd35ef09024b1e825604874ef705bce7f820e853292ea38e42a95500cfe');c=module('candidate','afcfc4b18933e4dfab777ce6cae4ee59ae902c20cbe26227d4ebc0a086c84b1f');s=module('seed','681902bc609b049ee008b1dc5ab52c2ff8a6444a0b05d61ebcb5bd34e4fdc717')
n=0
def req(x):
 global n
 if not x:raise ValueError('independent tiny predicate')
 n+=1
def reject(f):
 try:f()
 except (ValueError,TypeError):req(True)
 else:req(False)
def mm(a,b):return [[sum((x*y for x,y in zip(r,col)),F(0))for col in zip(*b)]for r in a]
def tr(a):return list(map(list,zip(*a)))
I=[[F(1),F(0)],[F(0),F(1)]];Z=[[F(0),F(0)],[F(0),F(0)]]
for eps in [F(1,2),F(1,2**20),F(1,2**60)]:
 G=[[F(1),F(1)],[F(1),1+eps*eps]];T=c.propose(G);expected=[[F(1),-1/eps],[F(0),1/eps]];req(T==expected)
 r=v.verify(G,Z,T,I);req(r['e']==0 and r['center']==expected and r['radius']==0)
 # Exact direct Gram identity, not original core implementation.
 req(mm(mm(tr(expected),G),expected)==I)
T=[[F(1),F(1,2**20)],[F(0),F(1)]];r=v.verify(I,Z,T,I);req(r['e']<1);req(r['radius']>=F(1,2**20));req(not r['width_pass'])
rad=[[F(1,10**80),F(0)],[F(0),F(1,10**80)]];stages={};r=v.verify(I,rad,I,I,lambda k,x:stages.update({k:x}));req(r['radius']>0)
a=stages['dyadic_inputs'];q=a['scale']
for i in range(2):
 for j in range(2):
  req(F(a['Gcenter'][i][j]-a['radius'][i][j],q)<=I[i][j]-rad[i][j]);req(F(a['Gcenter'][i][j]+a['radius'][i][j],q)>=I[i][j]+rad[i][j])
req(v.norm([[3,4]],1)>=5);req(v.norm([[-3,4]],1)>=5);req(v.norm([[1]],3)>=F(1,3))
reject(lambda:v.exactq(F(1,3)));reject(lambda:v.ck(True));reject(lambda:v.prod(1<<20000,1<<20000));reject(lambda:c.nearest(1<<2047,1));reject(lambda:v.verify(I,Z,[[F(1),F(0)],[F(1),F(1)]],I));reject(lambda:v.verify(I,[[-F(1),F(0)],[F(0),F(0)]],I,I))
req(v.verify(I,I,I,I)['status']=='INDETERMINATE_RESIDUAL')
for idx in range(6):
 a=s.seed(idx);chi=1 if idx//2==0 else -1;eta=-1 if idx%2==0 else 1;req(a[(idx//2,0)]==F(-eta*chi,2) and a[(3+idx//2,0)]==F(1,2))
req(type(s.seed(396)[(396,0)]) is F)
print(json.dumps({'status':'PASS','checks':n,'native_inputs_read':False,'scope':'independent tiny rational matrices, interval containment, signs and resource rejection'},indent=2))
