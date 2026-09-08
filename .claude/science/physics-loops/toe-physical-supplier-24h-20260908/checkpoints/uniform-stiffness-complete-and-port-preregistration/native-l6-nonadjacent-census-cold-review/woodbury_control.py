from fractions import Fraction as F
import json
def T(A):return list(map(list,zip(*A)))
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def neg(A):return [[-x for x in row] for row in A]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(A):
 n=len(A);M=[list(map(F,row))+e for row,e in zip(A,eye(n))]
 for j in range(n):
  k=next(k for k in range(j,n) if M[k][j]);M[j],M[k]=M[k],M[j];v=M[j][j];M[j]=[x/v for x in M[j]]
  for k in range(n):
   if k!=j:v=M[k][j];M[k]=[x-v*y for x,y in zip(M[k],M[j])]
 return [row[n:] for row in M]
def tr(A):return sum(A[i][i] for i in range(len(A)))
B=[[1,0,1,0],[0,1,0,1],[1,1,1,0],[0,0,1,1]];F0=[[1,0],[0,2],[0,-2],[0,0]];G=[[0,0],[-2,0],[0,0],[0,1]];Delta=mul(F0,T(G));Bn=add(B,Delta);BG=mul(B,G);U=[a+b for a,b in zip(F0,BG)];GG=mul(T(G),G);C=[GG[i]+eye(2)[i] for i in range(2)]+[eye(2)[i]+[F(0)]*2 for i in range(2)]
if add(mul(Bn,T(Bn)),neg(mul(B,T(B))))!=mul(mul(U,C),T(U)):raise ValueError('rank4 Gram')
shift=[[F(25,4)*x for x in row] for row in eye(4)];R=inv(add(mul(B,T(B)),shift));direct=inv(add(mul(Bn,T(Bn)),shift));small=inv(add(eye(4),mul(mul(C,T(U)),mul(R,U))));correction=mul(mul(small,C),mul(mul(T(U),mul(R,R)),U))
if tr(direct)!=tr(R)-tr(correction):raise ValueError('inverse trace')
if mul(add(mul(Bn,T(Bn)),shift),direct)!=eye(4):raise ValueError('direct inverse')
print(json.dumps({'controls':3,'scope':'independent exact rational rank4 Gram/Woodbury/direct inverse toy; no native gap scan'}))
