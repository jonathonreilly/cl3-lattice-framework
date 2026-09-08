from itertools import combinations,permutations
import json
pairs=list(map(frozenset,combinations(range(6),2)));words=[(a,frozenset(range(6))-a-c,c) for a in pairs for c in pairs if not a&c];n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
ck(len(words)==90);ck(len(set(words))==90)
for c in pairs:ck(sum(z==c for a,b,z in words)==6)
ck(sum(len(set(p[:3]))==3 and (set(p[:3])<=set(range(3)) or set(p[:3])<=set(range(3,6))) for p in permutations(range(6)))==72)
def mat(A,B):return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def add(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(c,A):return [[c*x for x in r] for r in A]
def adj(A):return [[x.conjugate() if isinstance(x,complex) else x for x in r] for r in zip(*A)]
def kron(A,B):return [[A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])] for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
I=[[1,0],[0,1]];X=[[0,1],[1,0]];Z=[[1,0],[0,-1]];g=kron(X,I);beta=kron(Z,X);Pv=scale(-1j,mat(g,beta));RA=kron([[-2,0],[0,-3]],I);RC=kron([[-5,0],[0,-7]],I)
left=mat(mat(Pv,mat(mat(g,RC),g)),RA);right=scale(-1j,mat(mat(mat(RC,g),RA),beta));ck(left==right)
O=add(mat(mat(RC,g),RA),mat(mat(RA,g),RC));H=scale(-1j,mat(O,beta));ck(O==adj(O));ck(H==adj(H));ck(add(mat(O,beta),mat(beta,O))==[[0]*4 for _ in range(4)])
ck(left!=scale(1j,mat(mat(mat(RC,g),RA),beta)))
print(json.dumps({'controls':n,'scope':'90/72 exact combinatorics and Gaussianinteger Clifford sign/Hermiticity, no physical solve'}))
