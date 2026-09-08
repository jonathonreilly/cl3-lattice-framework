import runpy,json,math,time,signal
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).parent;t=runpy.run_path(str(P/'transport.py'));signal.alarm(29);start=time.monotonic();count=0
Z=(F(0),F(0));ONE=(F(1),F(0))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def mul(a,b):return(a[0]*b[0]+3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def neg(a):return(-a[0],-a[1])
def ck(x,m):
 global count
 count+=1
 if not x:raise ValueError(m)
def mm(A,B):
 n=len(A);out=[[Z]*n for _ in range(n)]
 for i in range(n):
  for k in range(n):
   if A[i][k]!=Z:
    for j in range(n):
     if B[k][j]!=Z:out[i][j]=add(out[i][j],mul(A[i][k],B[k][j]))
 return out
def creator(n,j):
 a=[[Z]*(1<<n) for _ in range(1<<n)]
 for b in range(1<<n):
  if not b>>j&1:a[b|1<<j][b]=((-1)**((b&((1<<j)-1)).bit_count()),F(0))
 return a
def lift(index):
 E,T,d=t['blocks'](index);L=[[ONE,Z,Z,Z],[Z,E[0][0],E[0][1],Z],[Z,E[1][0],E[1][1],Z],[Z,Z,Z,(F(d),F(0))]];A=[[Z]*32 for _ in range(32)]
 for b in range(32):
  target,sgn=T[b&7]
  for e in range(4):A[target+8*e][b]=mul((F(sgn),F(0)),L[e][b>>3])
 return A
As=[];Ms=[]
for k in range(48):
 A=lift(k);As.append(A);E,T,d=t['blocks'](k);M=[[Z]*5 for _ in range(5)]
 for j in range(3):i,s=T[1<<j];M[i.bit_length()-1][j]=(F(s),F(0))
 for i in range(2):
  for j in range(2):M[i+3][j+3]=E[i][j]
 Ms.append(M)
 for j in range(5):
  right=[[Z]*32 for _ in range(32)]
  for i in range(5):
   ci=creator(5,i)
   for r in range(32):
    for c in range(32):right[r][c]=add(right[r][c],mul(M[i][j],ci[r][c]))
  ck(mm(A,creator(5,j))==mm(right,A),'32CAR')
 ck(A[0][0]==ONE and sum(x!=Z for x in A[0])==1,'vacuum')
lookup={str(M):i for i,M in enumerate(Ms)}
for i in range(48):
 for j in range(48):
  target=lookup[str(mm(Ms[i],Ms[j]))];ck(mm(As[i],As[j])==As[target],'48group on32')
# Actual candidate local kernels on tiny arrays, compared to exact exterior matrices.
import numpy as np
for k in range(48):
 E,T,d=t['blocks'](k);R=np.array([[float(a)+float(b)*math.sqrt(3) for a,b in row] for row in E]);A=np.array([[float(a)+float(b)*math.sqrt(3) for a,b in row] for row in As[k]])
 for parity in (0,1):
  fullbits=[b|((parity^(b.bit_count()%2))<<4) for b in range(16)];v=np.arange(16,dtype=float)-7;expected=A[np.ix_(fullbits,fullbits)]@v;out=v.copy();t['_triplet'](out,0,T);t['_last_eg'](out,3,parity,R,d);ck(np.max(np.abs(out-expected))<1e-12,'actual compressed top Eg')
# Deliberate missing determinant breaks a CAR intertwiner.
k=next(i for i in range(48) if t['blocks'](i)[2]==-1);bad=[r[:] for r in As[k]]
for i in range(24,32):
 for j in range(24,32):bad[i][j]=neg(bad[i][j])
ck(bad!=As[k],'missing determinant differs');ck(mm(bad,creator(5,3))!=mm(As[k],creator(5,3)),'missing determinant adverse')
print(json.dumps({'status':'PASS','predicates':count,'seconds':time.monotonic()-start,'scope':'exact32CAR/group plus tiny actual compressed kernels; no physical vector action'}))
