from fractions import Fraction as F
import json, hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
count=0
def test(x):
 global count
 count+=1
 if not x: raise RuntimeError('predicate '+str(count))
def tr(a): return list(map(list,zip(*a)))
def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def outer(a,b): return [[x*y for y in b] for x in a]
def scale(a,s):return [[x*s for x in r] for r in a]
n=8
I=eye(n); Z=scale(I,0); C=scale(I,0)
for i in range(0,n,2): C[i][i+1]=-1; C[i+1][i]=1
Y=[[F(((i+2)*(j+3)+i*i+3*j*j)%19-9,7) for j in range(7)] for i in range(n)]
G=mul(tr(Y),Y); J=mul(mul(tr(Y),C),Y); Pi=Z
wrong_partner=False; wrong_sign=False
pivots=[]
for step in range(4):
 i=max(range(7),key=lambda k:G[k][k]); r=G[i][i]
 if not r: break
 g=G[i][:]; j=J[i][:]
 Gn=sub(G,scale(add(outer(g,g),outer(j,j)),1/r))
 Jn=sub(J,scale(sub(outer(g,j),outer(j,g)),1/r))
 R=mul(sub(I,Pi),Y); u=[row[i] for row in R]; v=[row[0] for row in mul(C,[[x] for x in u])]
 Pi=add(Pi,scale(add(outer(u,u),outer(v,v)),1/r))
 R=mul(sub(I,Pi),Y); actualG=mul(tr(R),R); actualJ=mul(mul(tr(R),C),R)
 test(Gn==actualG); test(Jn==actualJ); test(mul(Pi,Pi)==Pi); test(mul(Pi,C)==mul(C,Pi)); test(Gn[i][i]==0)
 wrong_partner |= sub(G,scale(outer(g,g),1/r))!=actualG
 wrong_sign |= add(J,scale(sub(outer(g,j),outer(j,g)),1/r))!=actualJ
 pivots.append(i);G,J=Gn,Jn
test(all(x==0 for row in G for x in row));test(wrong_partner);test(wrong_sign)
# Exact unnormalized symmetry basis; three blocks 2,3,2.
e=eye(7)
s=[ [e[1+2*a][i]+e[2+2*a][i] for i in range(7)] for a in range(3)]
w=[ [e[1+2*a][i]-e[2+2*a][i] for i in range(7)] for a in range(3)]
b=[e[0],[sum(w[a][i] for a in range(3)) for i in range(7)]]+s+[[w[0][i]-w[1][i] for i in range(7)],[w[0][i]+w[1][i]-2*w[2][i] for i in range(7)]]
O=scale(eye(7),0);T=scale(eye(7),0)
for a in range(3):
 O[1+2*a][2+2*a]=O[2+2*a][1+2*a]=1
 T[0][1+2*a]=-1;T[0][2+2*a]=1;T[1+2*a][0]=1;T[2+2*a][0]=-1
groups=[0,0,1,1,1,2,2]
for M in [eye(7),O,T]:
 B=mul(mul(b,M),tr(b))
 for i in range(7):
  for j in range(7):
   if groups[i]!=groups[j]:test(B[i][j]==0)
 for group in [[2,3,4],[5,6]]:
  ratios=[B[i][i]/sum(x*x for x in b[i]) for i in group]
  test(len(set(ratios))==1)
result={'scope':'exact synthetic rational algebra only; no physical Gram or integral','predicates':count,'paired_pivots':pivots,'adverse_controls':'direct altered recurrences, not subprocess mutants','missing_partner_rejected':wrong_partner,'wrong_cross_sign_rejected':wrong_sign}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
