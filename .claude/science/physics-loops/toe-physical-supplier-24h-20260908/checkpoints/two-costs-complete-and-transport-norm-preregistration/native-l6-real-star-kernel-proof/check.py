from fractions import Fraction as F
import json
n=3;d=1<<n;I=[[int(i==j) for j in range(d)] for i in range(d)];count=0
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(c,A):return [[c*x for x in r] for r in A]
def ck(x):
 global count
 count+=1
 if not x:raise ValueError('CAR')
A=[];B=[]
for j in range(n):
 a=[[0]*d for _ in range(d)];b=[[0]*d for _ in range(d)]
 for v in range(d):
  target=v^(1<<j);sg=(-1)**((v&((1<<j)-1)).bit_count());a[target][v]=sg;b[target][v]=sg*(2*((v>>j)&1)-1)
 A.append(a);B.append(b);ck(mm(a,a)==I);ck(mm(b,b)==scale(-1,I));ck(list(map(list,zip(*b)))==scale(-1,b))
 for k in range(j+1):ck(add(mm(a,B[k]),mm(B[k],a))==scale(0,I))
# Literal complex native pair change (-i K)(i B)A is real +K BA.
for k in (-2,2):
 complex_delta=scale(-1j*k,mm(scale(1j,B[0]),A[1]));real_delta=scale(k,mm(B[0],A[1]));ck(complex_delta==real_delta);ck(real_delta==list(map(list,zip(*real_delta))));ck(real_delta!=scale(-k,mm(B[0],A[1])))
for j in range(n):
 # H0 term -i omega/2 A(iB)=omega/2 AB, omega=2.
 ck(mm(A[j],B[j])==[[int(i==k)*(2*((i>>j)&1)-1) for k in range(d)] for i in range(d)])
print(json.dumps({'status':'PASS','predicates':count,'scope':'exact integer three-mode CAR/negative-Y/pair sign; no physical action'}))
