"""Exact4state rational resolvent shift; algebra fixture, not native spectral data."""
from fractions import Fraction as F
import json,signal
if __name__=="__main__": signal.alarm(30)
n=4
I=[[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
def sc(c,a):return [[c*x for x in r] for r in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def inv(a):
 z=[r.copy()+I[j].copy() for j,r in enumerate(a)]
 for j in range(n):
  k=next(k for k in range(j,n) if z[k][j]);z[j],z[k]=z[k],z[j];c=z[j][j];z[j]=[x/c for x in z[j]]
  for k in range(n):
   if k!=j:
    c=z[k][j];z[k]=[x-c*y for x,y in zip(z[k],z[j])]
 return [r[n:] for r in z]
a=[[F(0)]*n for _ in range(n)]
for x in range(n):
 if x&1:a[x^1][x]=1
at=[list(r) for r in zip(*a)];g=add(a,at);H=[[F((2*(i&1)+3*((i>>1)&1)) if i==j else 0) for j in range(n)] for i in range(n)]
Bs=[]
for c,u,v in [(6,1,2),(7,-2,1)]:
 B=sc(c,I);B[0][3]=B[3][0]=F(u);B[1][2]=B[2][1]=F(v);Bs.append(B)
Rs=[];count=0;wrong=0
for B in Bs:
 D=add(H,B);R=sc(-1,inv(D));Rm=sc(-1,inv(add(D,sc(2,I))));L=add(mm(a,B),sc(-1,mm(B,a)))
 left=mm(a,R);right=add(mm(Rm,a),mm(Rm,mm(L,R)));bad=add(mm(R,a),mm(R,mm(L,R)))
 for i in range(n):
  for j in range(n):
   if left[i][j]!=right[i][j]:raise ValueError('shifted identity')
   count+=1;wrong+=left[i][j]!=bad[i][j]
 Rs.append((R,Rm,L))
RA,RAm,LA=Rs[0];RC,RCm,LC=Rs[1];left=mm(a,mm(RC,mm(g,RA)))[0][0];right=add(mm(RCm,RA),add(mm(RCm,mm(LC,mm(RC,mm(g,RA)))),sc(-1,mm(RCm,mm(g,mm(RAm,mm(LA,RA)))))))[0][0]
if left!=right or not wrong:raise ValueError('two inverse or adverse')
print(json.dumps({'status':'PASS','entry_checks':count,'two_inverse_vacuum_check':1,'omitted_shift_mismatches':wrong,'physical_runs':0},indent=2))
