"""Fixed synthetic production rectangles; no physical source/value imports."""
import signal,time,json,resource
from fractions import Fraction as F
from math import factorial
import core as C
start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('30s synthetic ceiling')));signal.alarm(30)
checks=0;events=[]
def table(n,i,j):
 if n:return C.ZERO
 return ((C.GRID-int(i==j),C.GRID+1),(0,0))if i==j else C.ZERO
# Tiny nonzero input radii contain identity D/P; this is artificial P=I,h=0.
J={1:{(0,0):C.c(2)},2:{(1,1):C.c(4)},3:{(2,2):C.c(-2)}}
records=[]
for kind,mask,factors,slopes in [
 ('nominal',(2,2,1,1),[(0,(0,),1),(1,(0,),1),(2,(0,),1),(0,(0,2),-1),(2,(0,3),-1),(3,(1,),2),(1,(0,1),-1)],[-2,-1,1,2]),
 ('inner',(2,2,4),[(0,(0,),1),(1,(0,),1),(2,(0,),1),(0,(0,1),-1),(2,(0,2),-1),(1,(0,1),-1)],[-1,-1,-2])]:
 seen=[];z=C.reconstruct(mask,factors,J,table,table,lambda stage,data:seen.append((stage,data['alpha'])))
 for alpha,value in z.items():
  expected=F(1)
  for k,x in zip(alpha,slopes):expected*=F(x**k,factorial(k))
  assert F(value[0][0],C.GRID)<=expected<=F(value[0][1],C.GRID)and value[1][0]<=0<=value[1][1];checks+=1
 records.append({'kind':kind,'coefficients':len(z),'events':len(seen)})
# Independent endpoint corners for all sign configurations.
for a in [(-7,-2),(-3,4),(0,6),(2,8)]:
 for b in [(-9,-1),(-2,5),(0,3),(3,11)]:
  p=[x*y for x in a for y in b];assert C.product_bounds(a,b)==(min(p)//C.GRID,-((-max(p))//C.GRID));checks+=1
assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<384*1048576
signal.alarm(0)
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'records':records,'seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'native_values':0}))
