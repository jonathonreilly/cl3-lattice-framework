import sympy as s,json
from pathlib import Path
basis=[x for x in range(16) if x.bit_count()%2==0];E=s.eye(8);idx={x:i for i,x in enumerate(basis)}
N=[s.diag(*[(x>>i)&1 for x in basis]) for i in range(4)]
def hop(a,b):
 H=s.zeros(8)
 for col,x in enumerate(basis):
  for i,j in [(a,b),(b,a)]:
   if (x>>j)&1 and not (x>>i)&1:
    y=x^(1<<j);sgn=(-1)**((x&((1<<j)-1)).bit_count()+(y&((1<<i)-1)).bit_count());y^=1<<i;H[idx[y],col]=sgn
 return H
T=[hop(i,i+1) for i in range(3)]
def U(t,c,b):return E-s.I*b*t+(c-1)*t*t
v=s.zeros(8,1);v[idx[9]]=1;v=U(T[0],s.Rational(3,5),s.Rational(4,5))*v
V=U(T[0],s.Rational(5,13),s.Rational(12,13))*U(T[1],s.Rational(7,25),s.Rational(24,25))
R=s.Matrix(4,4,lambda i,j:s.simplify(s.I*(v.H*(V.H*N[i]*V*N[j]-N[j]*V.H*N[i]*V)*v)[0]))
print(json.dumps({'R':str(R),'symmetric':R==R.T,'zero':R==s.zeros(4),'preparation':str(v),'V':str(V)} ,indent=2))
