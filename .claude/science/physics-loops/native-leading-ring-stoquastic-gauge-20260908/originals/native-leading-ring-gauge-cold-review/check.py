from itertools import product,combinations
import json,time
from pathlib import Path
st=time.monotonic();n=0
def check(c,m):
 global n
 if not c:raise RuntimeError(m)
 n+=1
rows=[]
for L in [(4,6,4),(6,4,6)]:
 vs=list(product(*(range(l) for l in L)));ix={r:i for i,r in enumerate(vs)}
 def shift(r,a,k=1):
  s=list(r);s[a]=(s[a]+k)%L[a];return tuple(s)
 def edge(r,a):return frozenset((r,shift(r,a)))
 def xi(r,a):return (-1)**sum(r[:a])
 c=0
 for r in vs:
  for a,b in combinations(range(3),2):
   vertices=[r,shift(r,a),shift(shift(r,a),b),shift(r,b)]
   eta=1
   for j in range(4):eta*=1 if ix[vertices[(j+1)%4]]>ix[vertices[j]] else -1
   hol=xi(r,a)*xi(shift(r,a),b)*xi(shift(r,b),a)*xi(r,b)
   check(eta==1 and hol==-1,'seam plaquette eta and hol');c+=1
  for a in range(3):
   if L[a]==4 and r[a]==0:
    v=[shift(r,a,k) for k in range(4)]
    eta=1;hol=1
    for k in range(4):
     eta*=1 if ix[v[(k+1)%4]]>ix[v[k]] else -1;hol*=xi(v[k],a)
    check(eta==-1 and hol==1,'winding eta hol');c+=1
 rows.append({'L':L,'cycles':c})
# Coherent boundary adverse: H=-X, U=Z. |+> unchanged would incorrectly exchange -1 and +1 energy.
H=[[0,-1],[-1,0]]; U=[1,-1]; psi=[1,1]
def energy(x):return sum(x[i]*H[i][j]*x[j] for i in range(2) for j in range(2))/sum(t*t for t in x)
check(energy(psi)==-1 and energy([U[i]*psi[i] for i in range(2)])==1,'untransformed coherent boundary changes energy')
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'checks':n,'rows':rows,'seconds':time.monotonic()-st},indent=2)+'\n')
