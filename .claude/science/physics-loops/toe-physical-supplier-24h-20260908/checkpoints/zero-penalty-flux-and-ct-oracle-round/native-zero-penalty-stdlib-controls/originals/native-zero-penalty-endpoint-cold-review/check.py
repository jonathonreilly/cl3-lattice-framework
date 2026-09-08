from pathlib import Path
from itertools import product
import json,hashlib
nchecks=0
def need(c,m):
 global nchecks
 if not c:raise RuntimeError(m)
 nchecks+=1
def plus(out,k,x):
 out[k]=out.get(k,0)+x
 if out[k]==0:del out[k]
def gamma(n,i):return n^(1<<i),(-1)**((n&((1<<i)-1)).bit_count())
def Hmatter(n,edges,xi):
 out={}
 for e,(i,j) in enumerate(edges):
  k,s=gamma(n,j);l,t=gamma(k,i);plus(out,l,-1j*s*t*xi[e])
 return out
rows=[]
for v,edges in [(2,[(0,1)]),(3,[(0,1),(1,2)]),(3,[(0,1),(1,2),(0,2)]),(4,[(0,1),(1,2),(2,3),(0,3)])]:
 e=len(edges);cols={};norm=2**(-(v-1)/2)
 for chord in product((1,-1),repeat=e-v+1):
  xi=(1,)*(v-1)+chord
  for occ in range(1<<v):
   if occ.bit_count()%2:continue
   vec={}
   for gauge in range(1<<(v-1)):
    x=tuple(z*(-1)**(((gauge>>i)&1)+((gauge>>j)&1)) for z,(i,j) in zip(xi,edges));amp=(-1)**((gauge&occ).bit_count())
    vec[occ,x]=amp # unnormalized integer column; norm has 2^(v-1) identical entries
   need(len(vec)==1<<(v-1),'orbit size')
   for i in range(v):
    transformed={}
    for (nn,x),amp in vec.items():
     y=tuple(-z if i in ab else z for z,ab in zip(x,edges));plus(transformed,(nn,y),amp*(-1)**((nn>>i)&1))
    need(transformed==vec,'all Gauss including omitted generator')
   lhs={}
   for (nn,x),amp in vec.items():
    for nn2,h in Hmatter(nn,edges,x).items():plus(lhs,(nn2,x),amp*h)
   rhs={}
   for nn2,h in Hmatter(occ,edges,xi).items():
    for gauge in range(1<<(v-1)):
     x=tuple(z*(-1)**(((gauge>>i)&1)+((gauge>>j)&1)) for z,(i,j) in zip(xi,edges));plus(rhs,(nn2,x),h*(-1)**((gauge&nn2).bit_count()))
   need(lhs==rhs,'full column Hamiltonian intertwining');cols[chord,occ]=vec
 values=list(cols.values())
 for i,a in enumerate(values):
  for j,b in enumerate(values):need(sum(x.conjugate()*b.get(k,0) for k,x in a.items())==((1<<(v-1)) if i==j else 0),'Gram')
 need(len(cols)==1<<e,'whole dimension');rows.append({'v':v,'e':e,'physical_dimension':len(cols)})
out={'checks':nchecks,'rows':rows,'method':'explicit all-Gauss group-average integer columns in matter/link-X basis; no author import'};Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(nchecks)
