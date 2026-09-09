from fractions import Fraction as F
import json
from pathlib import Path
C=0
def check(x):
 global C
 if not x: raise ValueError('exact predicate failed')
 C+=1
def zero(n):return [[F(0) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def add(*aa):return [[sum(a[i][j] for a in aa) for j in range(len(aa[0]))] for i in range(len(aa[0]))]
def sc(c,a):return [[c*x for x in r] for r in a]
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
r=F(99,100)
check(99*(1-r*r)<2*r)
for n in (2,4):
 D=[[F((i+2)*(j+3)%7-3,5) for j in range(n)] for i in range(n)]
 H=sc(F(1,2),add(D,tr(D))); K=sc(F(-1,2),add(D,sc(-1,tr(D))))
 for q in (1,2,7):
  Z=[[F((i-j)*(i+j+q),11) for j in range(n)] for i in range(n)]
  Zd=add(sc(-1,K),sc(-1,mul(H,Z)),sc(-1,mul(Z,H)),sc(-1,mul(mul(Z,K),Z)))
  Md=add(mul(Zd,Z),mul(Z,Zd)); M=add(sc(r*r,eye(n)),mul(Z,Z)); A=add(H,mul(Z,K))
  forcing=add(sc(2*r*r,H),sc(-2,mul(mul(Z,H),Z)),sc(-(1-r*r),add(mul(K,Z),mul(Z,K))))
  rhs=add(forcing,sc(-1,mul(A,M)),sc(-1,mul(M,tr(A))))
  check(Md==rhs)
 N=1<<n; fs=[]
 for j in range(n):
  f=zero(N)
  for b in range(N):
   if b>>j&1:f[b^(1<<j)][b]=F((-1)**((b&((1<<j)-1)).bit_count()))
  fs.append(f)
 orig=zero(N); decom=zero(N)
 for i in range(n):
  for j in range(n):
   # a=f+f*, b=i(f*−f); therefore i aDb/2=−aD(f*−f)/2.
   orig=add(orig,sc(-D[i][j]/2,mul(add(fs[i],tr(fs[i])),add(tr(fs[j]),sc(-1,fs[j])))))
   decom=add(decom,sc(H[i][j],mul(tr(fs[i]),fs[j])),sc(K[i][j]/2,mul(tr(fs[i]),tr(fs[j]))),sc(K[j][i]/2,mul(fs[i],fs[j])))
 check(orig==add(decom,sc(-sum(D[i][i] for i in range(n))/2,eye(N))))
 check(orig!=add(sc(-1,decom),sc(-sum(D[i][i] for i in range(n))/2,eye(N))))
print(json.dumps({'status':'PASS','exact_predicates':C,'scope':'synthetic 2/4 modes only; no native matrices'}))
