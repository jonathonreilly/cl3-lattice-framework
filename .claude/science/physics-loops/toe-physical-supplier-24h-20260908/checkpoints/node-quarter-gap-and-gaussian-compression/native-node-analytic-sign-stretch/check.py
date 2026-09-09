"""Exact abstract disjoint-pair algebra only; no native physical matrix."""
from fractions import Fraction as F
from itertools import combinations
import json
pairs=list(combinations(range(6),2));u={a:[F(int(i in a))-F(1,3) for i in range(6)] for a in pairs};count=0
for a in pairs:
 for i in range(6):
  if sum((u[c][i] for c in pairs if not set(a)&set(c)),F(0))!=-3*u[a][i]:raise ValueError('negative eigenchannel')
  count+=1
s=F(0)
for a in pairs:
 for c in pairs:
  if not set(a)&set(c):
   dot=sum(x*y for x,y in zip(u[a],u[c]));
   if dot!=F(-2,3):raise ValueError('disjoint scalar')
   s+=1+4*dot;count+=1
if s!=-150:raise ValueError('counterexample')
print(json.dumps({'status':'PASS','checks':count+1,'abstract_positive_inverse_counterexample':str(s),'physical_runs':0},indent=2))
