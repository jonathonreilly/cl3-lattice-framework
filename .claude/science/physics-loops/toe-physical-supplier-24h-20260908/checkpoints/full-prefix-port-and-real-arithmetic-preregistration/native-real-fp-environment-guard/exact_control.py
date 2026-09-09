from pathlib import Path
from fractions import Fraction as F
import ast,json
p=Path(__file__).parent;tree=ast.parse((p/'guard.py').read_text());node=next(x for x in ast.walk(tree) if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='cases' for t in x.targets));cases=eval(compile(ast.Expression(node.value),'literal integer test cases','eval'),{'__builtins__':{}})
def value(b):
 sign=-1 if b>>63 else 1;e=(b>>52)&2047;m=b&((1<<52)-1)
 return sign*F(m if e==0 else m+(1<<52))*F(2)**((-1074) if e==0 else e-1023-52)
def nearest(v,negative_zero):
 if not v:return (1<<63) if negative_zero else 0
 sign=(1<<63) if v<0 else 0;v=abs(v);lo=0;hi=0x7fefffffffffffff
 while lo<hi:
  mid=(lo+hi+1)//2
  if value(mid)<=v:lo=mid
  else:hi=mid-1
 if value(lo)==v:return sign|lo
 a=v-value(lo);b=value(lo+1)-v
 return sign|(lo if a<b or (a==b and lo%2==0) else lo+1)
checks=0
for name,op,a,b,expected in cases:
 for x,y,z in zip(a,b,expected):
  v=value(x)+value(y) if op=='add' else value(x)*value(y);negzero=(bool(x>>63) and bool(y>>63)) if op=='add' else bool((x^y)>>63)
  if nearest(v,negzero)!=z:raise ValueError(name)
  checks+=1
print(json.dumps({'status':'PASS','exact_bit_expectations':checks,'method':'Fraction exact operation plus nearest-even binary-search rounding, including signed zeros'}))
