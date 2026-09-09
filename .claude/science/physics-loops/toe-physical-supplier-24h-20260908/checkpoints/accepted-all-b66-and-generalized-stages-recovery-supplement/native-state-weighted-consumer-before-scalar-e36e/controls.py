from fractions import Fraction as F
from math import isqrt
import json
n=0
def ck(x):
 global n
 assert x;n+=1
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def upperroot(x):
 q=1<<64;i=isqrt((x*q*q).numerator//(x*q*q).denominator);return F(i+(F(i*i,q*q)<x),q)
# Two-mode paired state 3/5 vacuum +4/5 pair, contractions T,U.
matrices=[[[F(1,2),F(0)],[F(0),F(1,3)]],[[F(3,10),F(-2,5)],[F(2,5),F(3,10)]],[[F(0),F(0)],[F(0),F(0)]]]
for T in matrices:
 for U in matrices:
  es=[upperroot(sum((T[j][i]-U[j][i])**2 for j in range(2)))for i in range(2)]
  actual=F(4,5)*abs(det(T)-det(U));bound=F(4,5)*sum(es);ck(actual<=bound)
  E=[[T[j][i]-U[j][i]for i in range(2)]for j in range(2)]
  for t in [F(0),F(1,3),F(1)]:
   A=[[U[j][i]+t*E[j][i]for i in range(2)]for j in range(2)]
   derivative=E[0][0]*A[1][1]+A[0][0]*E[1][1]-E[0][1]*A[1][0]-A[0][1]*E[1][0]
   c1=det([[E[0][0],U[0][1]],[E[1][0],U[1][1]]])+det([[U[0][0],E[0][1]],[U[1][0],E[1][1]]]);ck(derivative==c1+2*t*det(E))
# Occupation-weighted Cauchy identity inequality, exact rational.
for w in [(F(1,5),F(4,5)),(F(1),F(1))]:
 e=(F(2,3),F(1,4));ck(sum(w[i]*e[i]for i in range(2))**2<=sum(w)*sum(w[i]*e[i]**2 for i in range(2)))
print(json.dumps({'status':'PASS','predicates':n,'scope':'two-mode exterior derivative and occupation-weighted bounds only; no native inputs'}))
