from pathlib import Path
import ast,json
from fractions import Fraction as F
from math import isqrt
P=Path(__file__).resolve().parent.parent/'native-compression-pilot-saved-postcheck/check.py'
tree=ast.parse(P.read_text());fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='normalized');S=1<<192;ns={'F':F,'isqrt':isqrt,'S':S};exec(compile(ast.Module(body=[fn],type_ignores=[]),str(P),'exec'),ns)
n=0
for a,b in ((1,1),(1,2),(2,3),(3,5),(7,9),(11,13)):
 for lo,hi in ((-5,-1),(-2,3),(0,0),(2,7),(1,1),(-1,-1)):
  mid,rad=ns['normalized']([lo*S,hi*S],[a*a*S,b*b*S]);lower=F(mid-rad,S);upper=F(mid+rad,S);bounds=[F(x,y) for x in (lo,hi) for y in (a,b)]
  assert lower<=min(bounds)<=max(bounds)<=upper;n+=1
  assert min(bounds)-lower<=F(2,S) and upper-max(bounds)<=F(2,S);n+=1
# Irrational square root: exact squaring brackets 1/sqrt(2), no floating expected value.
m,r=ns['normalized']([S,S],[2*S,2*S]);lo=F(m-r,S);hi=F(m+r,S);assert 0<=lo and lo*lo<=F(1,2)<=hi*hi;n+=1
print(json.dumps(dict(status='PASS_INDEPENDENT_NORMALIZATION',predicates=n,source_ast_only=True,native_calls=0,saved_check_calls=0)))
