from fractions import Fraction as F
import json
n=0
for N in [1,64,216,2097152]:
 for x in [F(1,10**6),F(1,1000),F(1,100),F(1,32),F(1,10)]:
  A=300*N*x*x;m0=max(0,-(-A.numerator//A.denominator)-1)
  if not F(m0)<A<=m0+1:raise ValueError('threshold')
  for m in range(m0+1,m0+18):
   if F(m)<A or 75*N*x*x*F(m)>F(m*m,4):raise ValueError('compression square')
   for d in range(1,min(8,m)+1):
    e=max(0,-(-(m-m0)//8));old=max(0,-(-(m-d-m0)//8))
    if old<e-1:raise ValueError('recursion')
   if F(3,4)*m-75*N*x*x<F(m,2):raise ValueError('Young compression')
   n+=1
for A in [F(1),F(2),F(8),F(9),F(100)]:
 m0=-(-A.numerator//A.denominator)-1
 if m0!=A-1:raise ValueError('equality endpoint')
for theta in [F(1,4),F(1,2),F(3,4)]:
 b=(1-theta)/2;threshold=F(75)/(1-theta)**2
 if (1-b-theta)*threshold!=F(75)/(4*b):raise ValueError('optimized Young')
print(json.dumps({'status':'PASS','threshold_compression_cases':n,'exact_integer_endpoints':5,'optimized_Young':3,'physical_calls':0}))
