from fractions import Fraction as F
import json
n=0
def ck(x):
 global n
 assert x;n+=1
for f in [[[F(1),F(1,2)],[F(1,3),F(1)]],[[F(0),F(1)],[F(1),F(0)]]]:
 for c in [(F(2),F(-1)),(F(1,3),F(2,5))]:
  A=[[sum(f[i][k]*c[k]*f[j][k]for k in range(2))for j in range(2)]for i in range(2)]
  left=sum(abs(c[k])*sum(f[i][k]**2 for i in range(2))for k in range(2))
  for col in [0,1]:
   right=sum(abs(c[k])*f[col][k]**2 for k in range(2));ck(sum(A[i][col]**2 for i in range(2))<=left*right)
for x in [F(1),F(3),F(7)]:
 for s,t in [(F(1,2),F(2)),(F(1),F(3))]:
  # No square root needed: cancel common sqrt(X) in B kernel identity.
  ck((1/(x+s*s)-1/(x+t*t))/(t*t-s*s)==1/((x+s*s)*(x+t*t)))
  ck((1-F(s*s)/(x+s*s))/s**2==x/(s*s*(x+s*s)))
print(json.dumps({'status':'PASS','predicates':n,'scope':'two-column signed factor Holder and scalar rational identities only'}))
