import sys,json
sys.dont_write_bytecode=True
from fractions import Fraction as F
from itertools import product
import independent as I
count=0
for t,u in I.PAIRS:
 c=I.coefficients(t,u);d=I.DELTA;B=1/(d*t*t*u*u);A=B*(1/d+2/t+2/u)
 for x in[d,F(1),F(3),F(20)]:
  assert sum(v*x**j for j,v in enumerate(c))-1/x**2==(x-d)*(x-t)**2*(x-u)**2*(A*x+B)/x**2;count+=1
 boxes=[(F(j),F(j+1))for j in range(5)];acc=(F(0),F(0))
 for b,v in zip(boxes,c):acc=I.summed(acc,I.scaled(b,v))
 vertices=[sum(v*x for v,x in zip(c,corner))for corner in product(*boxes)];assert acc==(min(vertices),max(vertices));count+=1
for box in[(F(0),F(1)),(F(2),F(3)),(F(1,7),F(9,7))]:
 a,b=I.root(box);assert a*a<=box[0]and b*b>=box[1];count+=1
print(json.dumps({'status':'PASS','independent_predicates':count,'native_values':0}))
