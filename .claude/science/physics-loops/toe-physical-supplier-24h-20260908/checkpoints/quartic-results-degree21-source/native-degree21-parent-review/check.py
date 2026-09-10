# Independent finite Clifford identities; no producer arithmetic or native inputs.
from itertools import combinations
N=4
eye=lambda:[[complex(i==j)for j in range(N)]for i in range(N)]
zero=lambda:[[0j]*N for _ in range(N)]
def add(*xs):return [[sum(x[i][j]for x in xs)for j in range(N)]for i in range(N)]
def mul(a,b):return [[sum(a[i][k]*b[k][j]for k in range(N))for j in range(N)]for i in range(N)]
def scl(a,c):return [[v*c for v in row]for row in a]
def kron(a,b):return [[a[i][j]*b[k][l]for j in range(2)for l in range(2)]for i in range(2)for k in range(2)]
I=[[1,0],[0,1]];X=[[0,1],[1,0]];Y=[[0,-1j],[1j,0]];Z=[[1,0],[0,-1]]
G=[kron(X,I),kron(Y,I),kron(Z,X),kron(Z,Y)]
def gam(v):return add(*(scl(G[i],v[i])for i in range(N)))
def power(a,k):
 x=eye()
 for _ in range(k):x=mul(x,a)
 return x
def quad(h):return add(*(scl(mul(G[i],G[j]),h[i][j]/4)for i in range(N)for j in range(N)))
checks=0
for vals in [(1,2,0,1,-1,2),(2,-1,1,0,3,-2)]:
 K=zero()
 for (i,j),v in zip(combinations(range(N),2),vals):K[i][j]=v;K[j][i]=-v
 h=scl(K,1j);H=add(quad(h),scl(eye(),1.5));a=[1,0,0,0];d=[0,1,1,0];ga=gam(a);gd=gam(d)
 B=scl(mul(ga,gd),1j);D=add(H,B);Da=mul(mul(ga,D),ga);Dd=scl(mul(mul(gd,D),gd),.5)
 kv=lambda v:[sum(K[i][j]*v[j]for j in range(N))for i in range(N)]
 assert Da==add(H,scl(B,-1),scl(mul(ga,gam(kv(a))),1j));checks+=1
 assert Dd==add(H,scl(B,-1),scl(mul(gd,gam(kv(d))),.5j));checks+=1
 J=scl(gd,2j)
 for k in range(5):
  assert mul(mul(scl(J,-1),power(D,k)),J)==scl(power(Dd,k),8);checks+=1
 for q0,q1 in [(1,-.25),(.5,.125)]:
  q=add(scl(eye(),q0),scl(D,q1));qa=add(scl(eye(),q0),scl(Da,q1))
  assert mul(mul(ga,q),J)==mul(qa,scl(B,2));checks+=1
  res=add(eye(),scl(D,-q0),scl(power(D,2),-q1))
  expansion=add(eye(),scl(D,-2*q0),scl(power(D,2),q0*q0-2*q1),scl(power(D,3),2*q0*q1),scl(power(D,4),q1*q1))
  assert mul(res,res)==expansion;checks+=1
# Exact dyadic complex operations above have small integer numerators: no transcendentals or division by non-powers of two.
# Independent parity routing for each table type, allowing all free powers up to the proved cap.
nominal_odd=set();nominal_even=set()
for j in range(5):
 for left,right in [(0,0),(0,1),(1,0),(1,1)]:
  for sl in ([0,1]if left==0 else[0]):
   for sr in ([0,1]if right==0 else[0]):
    n=j+sl+sr
    if left==right==0:
     (nominal_even if n%2==0 else nominal_odd).add(n)
    elif left!=right:
     (nominal_even if n%2 else nominal_odd).add(n+1)
    else:
     target=nominal_even if n%2==0 else nominal_odd;target.update([n,n+2])
assert max(nominal_odd)==5 and max(nominal_even)==6;checks+=1
print({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'native_values':0,'nominal_max_odd':5,'nominal_max_even':6})
