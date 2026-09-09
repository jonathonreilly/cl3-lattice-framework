import ast,pathlib,json
from fractions import Fraction as F
from math import isqrt
p=pathlib.Path(__file__).resolve().parent;source=p.parent/'native-compression-pilot-saved-postcheck/check.py'
tree=ast.parse(source.read_text());node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='normalized');ns={'F':F,'isqrt':isqrt,'S':1<<192};exec(compile(ast.Module(body=[node],type_ignores=[]),str(source),'exec'),ns)
S=1<<192;count=0
for a,b in [(-7,-3),(-2,5),(0,0),(3,9)]:
 for c,d in [(1,1),(4,4),(9,9)]:
  x=[a*S,b*S];r=[c*S,d*S];m,radius=ns['normalized'](x,r)
  lower=F(a,isqrt(c));upper=F(b,isqrt(c))
  if not F(m-radius,S)<=lower<=upper<=F(m+radius,S):raise ValueError('containment')
  count+=1
  z=ns['normalized']([-x[1],-x[0]],r)
  if not F(z[0]-z[1],S)<=-upper<=-lower<=F(z[0]+z[1],S):raise ValueError('minus J')
  count+=1
result={'status':'PASS_TINY_NORMALIZATION','predicates':count,'checker_run_calls':0,'saved_history_reads':0,'scope':'AST-selected pure function only'}
(p/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
