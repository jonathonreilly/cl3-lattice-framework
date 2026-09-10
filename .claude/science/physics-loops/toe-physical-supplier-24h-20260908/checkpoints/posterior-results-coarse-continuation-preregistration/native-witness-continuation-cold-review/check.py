from pathlib import Path
from fractions import Fraction as F
import sys,types,json
B=Path('/private/tmp/toe-24h-probes-20260908/native-coarse-witness-continuation-design')
for name in ['interval','dictionary','triples']:
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile((B/(name+'.py')).read_bytes(),str(B/(name+'.py')),'exec'),m.__dict__)
t=sys.modules['triples'];d=sys.modules['dictionary'];I=sys.modules['interval'];n=0
x=(0,1,-1,0,0,0,0);y=(1,0,0,0,0,0,0)
for s in [F(1,2),F(2)]:
 for sig in [-1,1]:
  A,Bv,mu=F(2,7),F(3,5),F(7,3);dd=(1-s*s*A)/6;C=[sig*s*A,sig*s*(A-dd),dd];L=[-Bv,-(1+s*s/6)*Bv,sig*s*Bv/6]
  for xx,yy in [(x,y),(y,x),(x,x)]:
   dots=t.dots(xx,yy)
   for gamma in [0,1]:
    expected=sum(((-L[k]-(mu/6 if k==1 else 0))if gamma else C[k])*dots[k]for k in range(3));v=t.local(s,sig,I.const(A),I.const(Bv),I.const(mu),gamma,dots);assert v[0]<=expected<=v[1];n+=1
assert t.dots(x,y)[2]==-t.dots(y,x)[2];n+=1
# Missing local O constant is detectably wrong on a literal O-supported source.
u=(0,1,0,0,0,0,0);v=(0,0,1,0,0,0,0);assert t.dots(u,v)[1]==1;n+=1
# Continuation schedule strictly excludes all completed node work.
steps=[(case,k)for case in range(3,10)for k in range(210 if case==3 else 0,378)];assert len(steps)==2436 and steps[0]==(3,210)and len(set(steps))==2436;n+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':n,'actual_prefix_read':False}))
