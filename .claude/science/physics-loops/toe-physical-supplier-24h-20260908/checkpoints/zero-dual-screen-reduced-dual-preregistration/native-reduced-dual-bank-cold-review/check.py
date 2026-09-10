from itertools import combinations
from fractions import Fraction as F
import json
pairs=list(combinations(range(6),2));kind=lambda x:'O'if x[0]//2==x[1]//2 else'P'
vec=lambda ids:[int(i in ids)for i in range(6)]
def n(x,y):return sum(a*b for a,b in zip(x,y))
def o(x,y):return sum(x[i]*y[i^1]for i in range(6))
checks=0
for A in pairs:
 d=vec(A);k=[1]*6;neighbors=[C for C in pairs if not set(C)&set(A)]
 assert len(neighbors)==6
 for wp,wo in [(1,0),(0,1),(F(-3,2),F(7,3))]:
  W=[sum((wo if kind(C)=='O'else wp)*int(i in C)for C in neighbors)for i in range(6)]
  if kind(A)=='O':expected=[(2*wp+wo)*(1-d[i])for i in range(6)]
  else:
   axis=next(j for j in range(3)if 2*j not in A and 2*j+1 not in A);e=vec([2*axis,2*axis+1]);expected=[3*wp*(1-d[i])+(wo-wp)*e[i]for i in range(6)]
  assert W==expected;checks+=1
for tag,d,e,expected in [('P',vec([0,2]),vec([4,5]),[[12,14,0],[14,42,14],[0,14,14]]),('O',vec([0,1]),None,[[14,14],[14,42]])]:
 bank=[d,[1]*6]+([e]if e else[])
 assert [[6*n(x,y)+o(x,y)for y in bank]for x in bank]==expected;checks+=1
 # Store symbolic c and nu coefficient pairs, not actual values.
 K=[[(3*(n(x,y)-o(x,y)),F(o(x,y),6))for y in bank]for x in bank]
 target=[[(6,F(0)),(0,F(1,3)),(0,F(0))],[(0,F(1,3)),(0,F(1)),(0,F(1,3))],[(0,F(0)),(0,F(1,3)),(0,F(1,3))]]if tag=='P'else[[(0,F(1,3)),(0,F(1,3))],[(0,F(1,3)),(0,F(1))]]
 assert K==target;checks+=1
print(json.dumps({'checks':checks,'native_values':False,'status':'PASS'}))
