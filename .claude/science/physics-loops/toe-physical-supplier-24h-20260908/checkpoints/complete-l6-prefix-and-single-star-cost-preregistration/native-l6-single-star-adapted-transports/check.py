from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,time,signal,resource
P=Path(__file__).parent;start=time.monotonic();signal.alarm(29);N=216;V=list(product(range(6),repeat=3));ix={v:i for i,v in enumerate(V)};K=[{} for _ in V];checks=0
def ck(x,s):
 global checks
 checks+=1
 if not x:raise ValueError(s)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mul(a):return [sum(z*a[j] for j,z in row.items()) for row in K]
for v in V:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;i,j=sorted((ix[v],ix[tuple(w)]));z=-2*(-1)**sum(v[:a]);K[i][j]=z;K[j][i]=-z
neighbors=[ix[tuple(s if a==axis else 0 for a in range(3))] for axis in range(3) for s in (1,5)];eta=[K[0][v]//2 for v in neighbors]
U=[[1]*6,[1,1,-1,-1,0,0],[1,1,1,1,-2,-2],[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1]];labels=['A1','E1','E2','T1','T2','T3'];lam=(12,24,36,48);sectors=[]
for l in lam:
 bs=[]
 for u in U:
  x=[F(0)]*N
  for v,e,z in zip(neighbors,eta,u):x[v]=F(e*z)
  for m in lam:
   if m!=l:
    y=mul(mul(x));x=[(-a-m*b)/(l-m) for a,b in zip(y,x)]
  bs.append(x)
 norms=[dot(x,x) for x in bs]
 for i in range(6):
  ck(mul(mul(bs[i]))==[-l*z for z in bs[i]],'sector')
  for j in range(i):ck(dot(bs[i],bs[j])==0,'irrep orthogonal')
 sectors.append(dict(lam=l,norms=list(map(str,norms)),gram_eigenvalues=[str(norms[i]/dot(U[i],U[i])) for i in range(6)],vectors=[[str(z) for z in x] for x in bs]))
# Previous exact signed site ledger is an input, not executed.
a=json.loads((P/'PRE_FREEZE.json').read_text());source=Path(a['transport_path']);ck(hashlib.sha256(source.read_bytes()).hexdigest()==a['transport_sha'],'transport input');trans=json.loads(source.read_text());maps=[]
for t in trans['automorphisms']:
 phi=t['site_map'];sign=t['site_signs'];cols=[]
 for u in U:
  coeff=[0]*6
  for j,v in enumerate(neighbors):coeff[neighbors.index(phi[v])]=u[j]*eta[j]*sign[v]//eta[neighbors.index(phi[v])]
  z=[F(dot(u0,coeff),dot(u0,u0)) for u0 in U];cols.append(z)
 ck(cols[0]==[F(1),F(0),F(0),F(0),F(0),F(0)],'A1 fixed')
 for j in (1,2):ck(all(cols[j][i]==0 for i in (0,3,4,5)),'E closed')
 for j in (3,4,5):ck(sum(v!=0 for v in cols[j])==1 and all(cols[j][i]==0 for i in (0,1,2)) and sum(abs(v) for v in cols[j])==1,'T signed monomial')
 for s in sectors:
  bs=[[F(z) for z in x] for x in s['vectors']]
  for j,x in enumerate(bs):
   tx=[F(0)]*N
   for i,z in enumerate(x):tx[phi[i]]=sign[i]*z
   target=[sum(cols[j][k]*bs[k][i] for k in range(6)) for i in range(N)];ck(tx==target,'actual sector transport')
 maps.append(dict(permutation=t['permutation'],signs=t['signs'],columns=[[str(z) for z in c] for c in cols]))
ck([sum(F(n)>0 for n in s['norms']) for s in sectors]==[6,6,6,3],'ranks');ck(time.monotonic()-start<29 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<384*1048576,'cap');(P/'ADAPTED.json').write_text(json.dumps(dict(neighbors=neighbors,eta=eta,U=U,labels=labels,sectors=sectors,transforms=maps),separators=(',',':'))+'\n');r=dict(status='PASS',predicates=checks,seconds=time.monotonic()-start,sectors=[{k:v for k,v in s.items() if k!='vectors'} for s in sectors]);(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
