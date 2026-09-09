from pathlib import Path
from fractions import Fraction as F
import json
O=Path('/private/tmp/toe-24h-probes-20260908/native-elliptic-b-run-76350');D=Path(__file__).resolve().parent
r=[(tuple(map(F,x)),tuple(map(F,w))) for x,w in json.loads((O/'GAUSS.json').read_text())['rule']]
def a(x,y):return x[0]+y[0],x[1]+y[1]
def m(x,y):
 z=[u*v for u in x for v in y];return min(z),max(z)
def c(x):return F(x),F(x)
def p(n,x):
 aa=c(1);bb=x
 if n==0:return aa
 for j in range(1,n):aa,bb=bb,m(a(m(m(x,bb),c(2*j+1)),m(aa,c(-j))),c(F(1,j+1)))
 return bb
checks=0
for x,w in r:
 one=a(c(1),m(m(x,x),c(-1)));num=m(a(p(11,x),m(m(x,p(12,x)),c(-1))),c(12));dd=m(num,(1/one[1],1/one[0]));sq=min(dd[0]**2,dd[1]**2),max(dd[0]**2,dd[1]**2);den=m(one,sq);assert w==(2/den[1],2/den[0]);checks+=1
for degree in range(24):
 total=c(0)
 for x,w in r:
  power=c(1)
  for _ in range(degree):power=m(power,x)
  total=a(total,m(w,power))
 target=F(0) if degree%2 else F(2,degree+1)
 assert total[0]<=target<=total[1];checks+=1
(D/'GAUSS_RECEIPT.json').write_text(json.dumps({'status':'PASS','checks':checks,'saved_weight_formulas_exact':12,'polynomial_moment_containments':24,'oracle_or_physical_integral_calls':0},indent=2)+'\n')
