from core import coefficient,tails,plan
from fractions import Fraction as F
from math import factorial
import json
checks=0
for n in range(9):
 direct=sum(F(factorial(2*n),factorial(j)**2*factorial(k)**2*factorial(n-j-k)**2) for j in range(n+1) for k in range(n-j+1))
 if coefficient(n)!=direct or coefficient(n)>6**(2*n):raise ValueError('combinatorial identity')
 checks+=2
for r in (F(1,4),F(1,2),F(3,4)):
 for m in range(5):
  bound=r**m*((2*m+1)/(1-r)+2*r/(1-r)**2)
  partial=sum((2*n+1)*r**n for n in range(m,m+20))
  if not 0<partial<bound:raise ValueError('weighted tail')
  checks+=1
# Planning only: tail bounds, not evaluation of any physical partial sum.
rows=[{'s':str(s),'target':str(t),'terms':plan(s,t)} for s in (F(1),F(2),F(1,2)) for t in (F(1,10**6),F(1,10**12))]
print(json.dumps({'status':'PASS','checks':checks,'plans':rows,'physical_series_evaluations':0},indent=2))
