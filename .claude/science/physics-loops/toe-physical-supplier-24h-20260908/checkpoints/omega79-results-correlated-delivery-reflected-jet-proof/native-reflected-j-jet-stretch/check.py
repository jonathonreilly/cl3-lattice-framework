"""Finite Clifford operator checks; no vacuum or native moment evaluated."""
import json
I2=[[1,0],[0,1]];X=[[0,1],[1,0]];Y=[[0,-1j],[1j,0]];Z=[[1,0],[0,-1]]
def kron(a,b):return[[a[i//len(b)][j//len(b)]*b[i%len(b)][j%len(b)]for j in range(len(a)*len(b))]for i in range(len(a)*len(b))]
g=[kron(X,I2),kron(Y,I2),kron(Z,X),kron(Z,Y)];I=kron(I2,I2)
def add(a,b):return[[a[i][j]+b[i][j]for j in range(len(a))]for i in range(len(a))]
def scale(a,c):return[[c*x for x in r]for r in a]
def mul(a,b):return[[sum(a[i][k]*b[k][j]for k in range(len(a)))for j in range(len(a))]for i in range(len(a))]
def zero(n):return[[0]*n for _ in range(n)]
def field(v):
 z=zero(4)
 for x,y in zip(v,g):z=add(z,scale(y,x))
 return z
K=[[0,1,2,0],[-1,0,0,-1],[-2,0,0,3],[0,1,-3,0]];a=[1,0,0,0];d=[0,1,1,0];kd=[sum(K[i][j]*d[j]for j in range(4))for i in range(4)];gd=field(d);ga=field(a)
def quad(h):
 z=zero(4)
 for i in range(4):
  for j in range(4):z=add(z,scale(mul(g[i],g[j]),h[i][j]/4))
 return z
h=scale(K,1j);V=[[2j*(a[i]*d[j]-d[i]*a[j])for j in range(4)]for i in range(4)];H0=add(quad(h),scale(I,-2));B=scale(mul(ga,gd),1j);D=add(H0,B);Dp=scale(mul(mul(gd,D),gd),.5)
expected=add(add(H0,scale(B,-1)),scale(mul(gd,field(kd)),.5j));assert Dp==expected
R=[[int(i==j)-d[i]*d[j]for j in range(4)]for i in range(4)];hp=mul(mul(R,add(h,V)),R);assert Dp==add(quad(hp),scale(I,-2))
J=scale(gd,2j);Jstar=scale(gd,-2j);assert mul(Jstar,J)==scale(I,8)
A=I;C=I;checks=3
for n in range(5):
 assert mul(mul(Jstar,A),J)==scale(C,8);checks+=1;A=mul(A,D);C=mul(C,Dp)
wrong=add(add(H0,scale(B,-1)),scale(mul(gd,field(kd)),-.5j));assert wrong!=Dp;checks+=1
# All entries above are Gaussian integers/dyadics exactly representable in this small control.
print(json.dumps({'status':'PASS','checks':checks,'native_moments':False,'finite_clifford_dimension':4,'vacuum_expectation_evaluated':False}))
