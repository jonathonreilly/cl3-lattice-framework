"""Formal finite2x2 coefficient test, no native operator/scalar input."""
from fractions import Fraction as F
import json
Z=lambda:[[F(0)for _ in range(2)]for _ in range(2)]
def add(a,b):return[[a[i][j]+b[i][j]for j in range(2)]for i in range(2)]
def mul(a,b):return[[sum(a[i][k]*b[k][j]for k in range(2))for j in range(2)]for i in range(2)]
def sc(a,c):return[[c*x for x in row]for row in a]
def tr(a):return a[0][0]+a[1][1]
h=[[F(-2),F(0)],[F(0),F(3)]];v=[[F(1),F(2)],[F(2),F(-1)]];P=[[F(1),F(0)],[F(0),F(0)]];ident=[[F(1),F(0)],[F(0),F(1)]];N=10
U=[{0:ident}]
for n in range(N):
 nxt={}
 for p,a in U[n].items():
  nxt[p]=add(nxt.get(p,Z()),sc(add(mul(h,a),sc(mul(a,h),-1)),F(1,n+1)))
  nxt[p+1]=add(nxt.get(p+1,Z()),sc(mul(a,v),F(-1,n+1)))
 U.append(nxt)
checks=0
for n in range(1,N+1):assert U[n][0]==Z();checks+=1
G={(n,p):mul(P,a)for n in range(1,N+1)for p,a in U[n].items()if p}
def convolution(A,B):
 C={}
 for (n,p),a in A.items():
  for (m,q),b in B.items():
   if n+m<=N:C[n+m,p+q]=add(C.get((n+m,p+q),Z()),mul(a,b))
 return C
power=G;ell={}
for m in range(1,N+1):
 for key,a in power.items():ell[key]=ell.get(key,F(0))+F((-1)**(m+1),2*m)*tr(a)
 power=convolution(power,G)
for n in range(2,N+1):
 assert ell.get((n,1),F(0))==0;assert all(p>=2 for (order,p),x in ell.items()if order==n and x);checks+=2
bad=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]];assert tr(mul(bad,U[3][1]))!=0;checks+=1
# Scalar requirement extraction from parity formulas, without moment values.
for N,podd,oodd,ev in [(7,5,7,6),(8,7,7,8),(9,7,9,8),(10,9,9,10)]:
 oddP=[];oddO=[];even=[]
 for j in range(N-1):
  if j%2==0:oddP+=[j+1];oddO+=[j+1];even+=[j,j+2]
  else:oddP+=[j];oddO+=[j+2];even+=[j+1]
 assert(max(oddP),max(oddO),max(even))==(podd,oodd,ev);checks+=1
print(json.dumps({'status':'PASS','checks':checks,'native_values':False,'formal_matrix_dimension':2,'max_jet_order':10}))
