from fractions import Fraction as F
import json
# Laurent-series Riesz extraction for a seven-state chain. Endpoint P has
# dimension2, mirror symmetry makes all lower endpoint corrections scalar.
# This is independent of DP; every entry and coefficient is exact rational.
d=[0,1,2,3,2,1,0];N=7;order=6;lo=-7;hi=6
V=[[F(abs(i-j)==1) for j in range(N)] for i in range(N)]
R=[]
for x in d:
 R.append({-1:F(1)} if x==0 else {k:-F(1,x**(k+1)) for k in range(hi+1)})
# P entries of (z-H0)^-1[V(z-H0)^-1]^n, polynomial dictionary per entry.
A=[[[{} for j in range(N)] for i in range(N)]]
for i in range(N):A[0][i][i]=R[i]
for n in range(1,order+1):
 prev=A[-1];cur=[[{} for j in range(N)] for i in range(N)]
 for i in range(N):
  for j in range(N):
   out=cur[i][j]
   for k in range(N):
    if V[k][j]:
     for a,x in prev[i][k].items():
      for b,y in R[j].items():
       z=a+b
       if lo<=z<=hi:out[z]=out.get(z,0)+x*y
 A.append(cur)
# C=P H Pi P = contour z resolvent, coefficient z^-2.
# A=P Pi P = coefficient z^-1; all C<6 offdiagonals vanish,
# so normalized sixth offdiagonal equals C6 directly.
c=[a[0][6].get(-2,F(0)) for a in A]
if any(c[:6]) or c[6]!=-F(1,12):raise RuntimeError(c)
for n,a in enumerate(A):
 if a[0][0].get(-1,0)!=a[6][6].get(-1,0):raise RuntimeError('mirror overlap')
 if a[0][0].get(-2,0)!=a[6][6].get(-2,0):raise RuntimeError('mirror energy')
print(json.dumps({'PASS':True,'canonical_sixth_offdiagonal':str(c[6]),'raw_chain':str(F(-1,1*2*3*2*1)),'scope':'Exact Riesz canonical-normalization mock, not native coefficient'},indent=2))
