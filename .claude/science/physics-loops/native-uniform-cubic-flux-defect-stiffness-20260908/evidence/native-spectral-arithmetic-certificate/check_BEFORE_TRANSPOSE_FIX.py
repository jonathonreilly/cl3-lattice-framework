from fractions import Fraction as F
import json
class Z:
 def __init__(self,r=0,i=0):self.r=F(r);self.i=F(i)
 def __add__(a,b):return Z(a.r+b.r,a.i+b.i)
 def __sub__(a,b):return Z(a.r-b.r,a.i-b.i)
 def __mul__(a,b):return Z(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
 def conj(a):return Z(a.r,-a.i)
 def mag(a):return abs(a.r)+abs(a.i)
def mat(A,B):return [[sum((a*b for a,b in zip(row,col)),Z()) for col in zip(*B)] for row in A]
def adj(A):return [[a.conj() for a in row] for row in zip(*A)]
def diff(A,B):return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def norm(A):return max(max(sum(a.mag() for a in row) for row in A),max(sum(a.mag() for a in col) for col in zip(*A)))
U=[[Z(F(3,5)),Z(0,F(4,5))],[Z(0,F(4,5)),Z(F(3,5))]];I=[[Z(1),Z()],[Z(),Z(1)]];L0=[[Z(),Z()],[Z(),Z(9)]];A=mat(mat(U,L0),adj(U));n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
ck(norm(diff(mat(adj(U),U),I))==0)
for eps in (F(0),F(1,1000000),F(-1,1000000)):
 Q=[[Z(z.r,z.i) for z in row] for row in U];Q[0][0]=Q[0][0]+Z(eps,eps)
 lam=[F(1,100000),F(9)-F(1,100000)];Ld=[[Z(lam[0]),Z()],[Z(),Z(lam[1])]]
 eta=norm(diff(mat(adj(Q),Q),I));r=norm(diff(mat(A,Q),mat(Q,Ld)));delta=2*r+4*max(abs(x) for x in lam)*eta
 ck(eta<=F(1,2));ck(abs(lam[0])<=delta);ck(abs(lam[1]-9)<=delta)
 ck(lam[0]+delta>=0)
# Bad nonunitary candidate must not enter the polar certificate.
Q=[[Z(2)*z for z in row] for row in U];ck(norm(diff(mat(adj(Q),Q),I))>F(1,2))
# Omitting complex conjugation gives a false Gram matrix; actual exact control kills it.
wrong=mat([list(x) for x in zip(U)],U);ck(norm(diff(wrong,I))>0)
print(json.dumps({'checks':n,'scope':'exact synthetic complex matrices including zero eigenvalue; no physical spectra or RNG'}))
