from fractions import Fraction as F
from itertools import combinations_with_replacement
import json
n=0
def prod(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def val(a,x):return sum(c*x**i for i,c in enumerate(a))
for d in [F(1,4),F(1),F(3,2)]:
 for t,u in combinations_with_replacement([F(1,4),F(1),F(3)],2):
  P=[-d,F(1)]
  for z in [t,t,u,u]:P=prod(P,[-z,F(1)])
  b=1/(d*t*t*u*u);a=b*(1/d+2/t+2/u);A=prod(P,[b,a]);A[0]+=1;assert A[:2]==[0,0];n+=1;Q=A[2:]
  for x in [d,d+F(1,7),d+1,d+7]:
   assert val(Q,x)-1/x**2==val(P,x)*(a*x+b)/x**2>=0;n+=1
  assert val(Q,d)==1/d**2 and val(Q,t)==1/t**2 and val(Q,u)==1/u**2;n+=1
print(json.dumps({'status':'PASS','checks':n,'native_values':0,'fixture':'abstract positive rational contacts only'}))
