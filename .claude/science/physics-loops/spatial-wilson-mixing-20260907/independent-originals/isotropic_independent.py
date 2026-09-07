from itertools import combinations,product
from fractions import Fraction as F
import json,math
edges=sorted((v,v+(1<<a)) for v in range(8) for a in range(3) if not v&(1<<a));ei={e:i for i,e in enumerate(edges)}
def boundary(a,b,fixed):
 c=3-a-b;v=fixed<<c;cycle=[v,v+(1<<a),v+(1<<a)+(1<<b),v+(1<<b)]
 r=[0]*12
 for u,v in zip(cycle,cycle[1:]+cycle[:1]):r[ei[tuple(sorted((u,v)))]]+=1 if u<v else -1
 return r
src=boundary(0,1,0)+[0]*12
faces=[];names=[]
for layer in range(2):
 for a,b in combinations(range(3),2):
  for f in range(2):
   if (a,b,f)==(0,1,0):continue
   v=boundary(a,b,f);faces.append(v+[0]*12 if layer==0 else [0]*12+v);names.append([layer,a,b,f])
for i in range(12):
 v=[0]*24;v[i]=-1;v[i+12]=1;faces.append(v);names.append(['temporal',edges[i]])
A=[[faces[j][i]%3 for j in range(22)]+[-src[i]%3] for i in range(24)]
piv=[];row=0
for j in range(22):
 p=next((i for i in range(row,24) if A[i][j]),None)
 if p is None:continue
 A[row],A[p]=A[p],A[row];inv=pow(A[row][j],-1,3);A[row]=[(v*inv)%3 for v in A[row]]
 for i in range(24):
  if i!=row:
   m=A[i][j];A[i]=[(u-m*v)%3 for u,v in zip(A[i],A[row])]
 piv.append(j);row+=1
assert not any(all(v==0 for v in r[:22]) and r[22] for r in A)
free=[j for j in range(22) if j not in piv];hist={};low=[]
for vals in product(range(3),repeat=len(free)):
 x=[0]*22
 for j,v in zip(free,vals):x[j]=v
 for i,j in enumerate(piv):x[j]=(A[i][22]-sum(A[i][k]*x[k] for k in free))%3
 assert all((sum(faces[j][i]*x[j] for j in range(22))+src[i])%3==0 for i in range(24))
 w=sum(v!=0 for v in x);hist[w]=hist.get(w,0)+1
 if w<=5:low.append([(names[j],1 if v==1 else -1) for j,v in enumerate(x) if v])
assert min(hist)==5 and hist[5]==1
assert all(n[0]==0 for n,s in low[0])
b=F(1,10**14);leading=F(1,12**5*81);remainder=F(17**6,120)*b
assert remainder<leading
out={'rank':row,'nullity':len(free),'all_residue_solutions':sum(hist.values()),'support_histogram':hist,'support_at_most5':low,'signed_subsets_through5':sum(math.comb(22,k)*2**k for k in range(6)),'relative_remainder_ceiling':str(remainder/leading)}
print(json.dumps(out,indent=2))
