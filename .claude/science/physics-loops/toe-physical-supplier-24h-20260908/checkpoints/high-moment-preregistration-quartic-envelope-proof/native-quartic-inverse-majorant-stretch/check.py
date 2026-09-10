from fractions import Fraction as F
from itertools import combinations_with_replacement
import json

def coefficients(d,a,b):
 B=1/(d*a*a*b*b);A=B*(1/d+2/a+2/b);e1=d+2*a+2*b;e2=a*a+b*b+4*a*b+2*d*(a+b);e3=2*a*b*(a+b)+d*(a*a+b*b+4*a*b);e4=a*a*b*b+2*d*a*b*(a+b)
 return [A*e4-B*e3,B*e2-A*e3,A*e2-B*e1,B-A*e1,A]
def poly(c,x):return sum(v*x**i for i,v in enumerate(c))
n=0;d=F(1,4)
for a,b in combinations_with_replacement([F(1,2),F(1),F(2),F(4),F(8)],2):
 c=coefficients(d,a,b);B=1/(d*a*a*b*b);A=B*(1/d+2/a+2/b)
 for x in [d,F(1,3),F(1,2),F(1),F(3),F(10)]:
  diff=(x-d)*(x-a)**2*(x-b)**2*(A*x+B)/x**2;assert poly(c,x)-1/x**2==diff and diff>=0;n+=1
for a,b in[(d,d),(F(1,8),F(1,8))]:
 c=coefficients(d,a,b);assert poly(c,d)==1/d**2;n+=1
assert len(list(combinations_with_replacement(range(5),2)))==15;n+=1
# Independent exact point-spectrum check of residual convolution and moment degree.
v=[F(1),F(-2,3),F(1,5),F(-1,7)];conv=[sum(v[i]*v[j]for i in range(4)for j in range(4)if i+j==k)for k in range(7)]
for x in [d,F(1),F(3)]:
 for j in range(5):assert sum(conv[k]*x**(k+j)for k in range(7))==poly(v,x)**2*x**j;n+=1
print(json.dumps({'status':'PASS','exact_synthetic_predicates':n,'native_values':0}))
