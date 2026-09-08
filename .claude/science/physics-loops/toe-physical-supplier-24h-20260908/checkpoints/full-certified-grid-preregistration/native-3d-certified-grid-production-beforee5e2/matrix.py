from itertools import product
from fractions import Fraction as F

def build(row,gridrows):
 vertices=list(product(range(2),repeat=3));idx={v:i for i,v in enumerate(vertices)}
 edges=[(v,a) for v in vertices for a in range(3) if v[a]==0]
 signs=dict(zip(edges,row['cube_signs']));C=[[0]*8 for _ in range(8)];As=[]
 for a in range(3):
  A=[[0j]*8 for _ in range(8)]
  for v in vertices:
   w=list(v);w[a]^=1;base=list(v);base[a]=0;s=signs[tuple(base),a];i,j=idx[v],idx[tuple(w)];C[i][j]=s;A[i][j]=s*(-1j if v[a]==0 else 1j)
  As.append(A)
 base=[[sum(C[i][k]*C[k][j] for k in range(8))+3*(i==j) for j in range(8)] for i in range(8)]
 P=([[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]])
 D=[[complex(base[i//2][j//2]) if i%2==j%2 else 0j for j in range(16)] for i in range(16)];radius=F(0)
 for a,g in enumerate(gridrows):
  lo=F(g['lower_numerator'],g['denominator']);hi=F(g['upper_numerator'],g['denominator']);q=float.fromhex(g['q_hex']);exact=F(q)
  if not 0<=lo<=hi<=2:raise ValueError('physical input interval')
  radius+=max(abs(exact-lo),abs(exact-hi))
  for i in range(8):
   for j in range(8):
    for s in range(2):
     for t in range(2):
      factor=As[a][i][j]*P[a][s][t]
      if factor:
       if D[2*i+s][2*j+t]!=0:raise ValueError('disjoint exact q-entry guard')
       D[2*i+s][2*j+t]=q*factor
 return D,radius
