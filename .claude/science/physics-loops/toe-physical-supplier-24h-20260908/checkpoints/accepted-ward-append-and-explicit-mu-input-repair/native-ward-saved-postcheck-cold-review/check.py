from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import ast,json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/native-ward-append-saved-postcheck/check.py');tree=ast.parse(p.read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main');body=next(n for n in fn.body if isinstance(n,ast.Try)).body
start=next(i for i,n in enumerate(body) if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='I')
end=next(i for i,n in enumerate(body) if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='expected')
env={'F':F};exec(compile(ast.Module(body=body[start:end],type_ignores=[]),'pure_literal_geometry','exec'),env)
count=0
for (oa,oc,k),(I,O,T,N) in zip(((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1)),env['geom']):
 expectedI=((1,0,0),(0,2,0),(0,0,2));expectedO=((0,0,0),(0,-2*oa,-k),(0,-k,-2*oc));expectedT=((0,-2,-2),(2,0,0),(2,0,0))
 for actual,expected in ((I,expectedI),(O,expectedO),(T,expectedT)):
  for a,b in zip(sum(actual,[]),sum((list(r) for r in expected),[])):
   if a!=b:raise ValueError('literal sign')
   count+=1
 for i in range(3):
  for j in range(3):
   if N[i][j]!=I[i][j]+O[i][j]:raise ValueError('N')
   count+=1
Q=2**256
for a in (F(1),F(2),F(1,3),F(35,17),F(1,2**200)):
 lo=isqrt(a.numerator*Q*Q//a.denominator);hi=lo if F(lo*lo,Q*Q)==a else lo+1
 if not F(lo*lo,Q*Q)<=a<=F(hi*hi,Q*Q):raise ValueError('root')
 count+=1
 for v in (F(-7,3),F(0),F(5,11)):
  ends=sorted((v*F(lo,Q),v*F(hi,Q)))
  if v>0 and ends[0]<0 or v<0 and ends[1]>0:raise ValueError('signed product')
  count+=1
print(json.dumps({'status':'PASS_TINY_LITERAL_GEOMETRY_ROOTS','predicates':count,'main_calls':0,'physical_inputs_read':0},indent=2))
