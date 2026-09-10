from pathlib import Path
from fractions import Fraction as F
import sys,types,json,time
P=Path('/private/tmp/toe-24h-probes-20260908/native-coarse-occupied-witness-runtime-design');start=time.monotonic()
for name in ['interval','witness']:
 m=types.ModuleType(name);m.__file__=str(P/(name+'.py'));sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),m.__file__,'exec'),m.__dict__)
mm=sys.modules['witness'].mm;rnd=sys.modules['interval'].rnd
T=[[F(1),F(1,3),F(-2,5)],[F(0),F(2),F(1,7)],[F(0),F(0),F(3)]];L=[[F(1),F(2),F(-1)],[F(0),F(-3),F(2)]];X=[[F(2),F(-1),F(3)]]
def exact(a,b):return [[sum((x*y for x,y in zip(r,c)),F(0))for c in zip(*b)]for r in a]
def tr(x):return list(map(list,zip(*x)))
def boxes(x):return [[rnd(v,v)for v in row]for row in x]
local=exact(L,T);truth=exact(exact(X,T),tr(local));old=mm(mm(boxes(X),boxes(T)),tr(mm(boxes(L),boxes(T))));new=mm(boxes(X),mm(boxes(T),tr(mm(boxes(L),boxes(T)))))
checks=0
for j,v in enumerate(truth[0]):assert old[0][j][0]<=v<=old[0][j][1] and new[0][j][0]<=v<=new[0][j][1];checks+=1
for row,br in zip(T,boxes(T)):
 for x,(l,h) in zip(row,br):assert l<=x<=h;checks+=1
assert exact(exact(X,T),tr(local))==exact(X,exact(T,tr(local)));checks+=1
print(json.dumps({'status':'PASS','checks':checks,'seconds':time.monotonic()-start,'scope':'tiny rectangular rational reassociation and outward T boxes; no actualT/IDs, no nativecost forecast'}))
