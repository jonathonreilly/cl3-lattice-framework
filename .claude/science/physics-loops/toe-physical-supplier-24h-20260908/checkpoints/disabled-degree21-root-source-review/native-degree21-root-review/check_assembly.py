"""Tiny synthetic source-interface comparison; no native inputs."""
import sys,importlib.util,json,copy
from pathlib import Path
from fractions import Fraction as F
import independent as I
import assembly as ours
import tables as T
P=Path('/private/tmp/toe-24h-probes-20260908/native-degree21-masked-jet-prototype')
# Hold independent modules before installing the producer's isolated synthetic names.
for name in ['arithmetic','core','interval','assembly','certificate','radial','tables']:
 spec=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
A=sys.modules['assembly'];C=sys.modules['certificate'];tab=sys.modules['tables'];checks=0
s=[I.c(x)for x in [1,2,5,14,42]];got=[];want=[]
r=ours.choose(s,F(1,2),lambda a,b:got.append((a,copy.deepcopy(b))));p=A.choose(s,F(1,2),lambda a,b:want.append((a,copy.deepcopy(b))));assert got==want and r==p;checks+=len(got)+1
R=lambda n:I.c(n+1)
for kind,left,right,o in [('inner','P','P',0),('inner','O','O',0)]+[('nominal',a,b,c)for a,b,c,_ in T.SIGS]:
 a,b=T.build(R,kind,left,right,o);aa,bb=tab.inner(R,right)if kind=='inner'else tab.nominal(R,left,right,o);rank=3 if kind=='inner'else 4;limit=6 if kind=='inner'else 4
 for n in range(limit+1):
  for i in range(rank):
   for j in range(rank):assert a(n,i,j)==aa(n,i,j)and b(n,i,j)==bb(n,i,j);checks+=1
pp={'P':[F(1),F(1,4),F(1,16)],'O':[F(1),F(1,8),F(1,32)]};jets={}
for a,b,o,_ in T.SIGS:jets[a,b,o]={alpha:I.c(F(1,10))for alpha in I.indices((2,2,1,1))}
kwargs=(pp,{'P':r,'O':r},jets,{'P':F(1,100),'O':F(1,50)},(F(1),F(1)),(F(-10**6),F(10**6)))
got=[];want=[];x=ours.finish(*kwargs,lambda a,b:got.append((a,copy.deepcopy(b))));y=C.finish(*kwargs,lambda a,b:want.append((a,copy.deepcopy(b))));
for aa,bb in zip(got,want):
 if aa!=bb:print('DIFFERENCE',aa,bb)
assert got==want and x==y;checks+=len(got)+1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'native_calls':0}))
