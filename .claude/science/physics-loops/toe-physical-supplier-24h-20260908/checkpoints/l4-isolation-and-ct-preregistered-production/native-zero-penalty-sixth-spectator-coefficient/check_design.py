from itertools import product,combinations
from fractions import Fraction
import json,time,signal,resource
signal.alarm(180);start=time.monotonic();checks=0
def need(c,s):
 global checks
 checks+=1
 if not c:raise RuntimeError(s)
vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};N=64
edges=[];K=[[0]*N for _ in range(N)]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;w=tuple(w);i,j=sorted((ix[v],ix[w]));e=len(edges);edges.append((i,j));K[i][j]=-2*(-1)**sum(v[:a]);K[j][i]=-K[i][j]
need(all(sum(K[i][k]*K[k][j] for k in range(N))==-24*(i==j) for i in range(N) for j in range(N)),'K flat')
inc=[set() for _ in range(N)]
for e,(i,j) in enumerate(edges):inc[i].add(e);inc[j].add(e)
v,w=edges[0];cut=inc[v]^inc[w];S=sorted({x for e in cut for x in edges[e]})
cols=[[Fraction(i==s) for i in range(N)] for s in S]+[[Fraction(K[i][s]) for i in range(N)] for s in S]
def rank(cols):
 piv={}
 for col in cols:
  c=col.copy()
  for i,b in sorted(piv.items()):
   f=c[i]
   if f:c=[x-f*y for x,y in zip(c,b)]
  k=next((i for i,x in enumerate(c) if x),None)
  if k is not None:
   f=c[k];piv[k]=[x/f for x in c]
 return len(piv)
rk=rank(cols);need(rk%2==0 and rk<=2*len(S),'even invariant subspace bound')
# All extra images deltaK columns are endpoint-supported, verified literally.
bridges=[]
starA={x for e in inc[v]-inc[w] for x in edges[e]};starB={x for e in inc[w]-inc[v] for x in edges[e]}
for e,(i,j) in enumerate(edges):
 if e not in cut and ((i in starA and j in starB) or(i in starB and j in starA)):bridges.append(e)
need(len(bridges)==6,'six bridges including winding')
for e in sorted(cut|set(bridges)):
 i,j=edges[e]
 images=[]
 for c in cols:
  y=[Fraction(0)]*N;y[i]=-2*K[i][j]*c[j];y[j]=2*K[i][j]*c[i];images.append(y)
 need(rank(cols+images)==rk,'all intermediate perturbations preserve W')
# Enumerate incidence perfect matchings on a multiset of twelve occurrences.
# Repeated bridge occurrences indistinguishable; deduplicate pair-term sets.
def pairings(occ):
 if not occ:return {()}
 e=occ[0];out=set()
 for k in range(1,len(occ)):
  f=occ[k]
  if e==f or not(set(edges[e])&set(edges[f])):continue
  for p in pairings(occ[1:k]+occ[k+1:]):out.add(tuple(sorted((tuple(sorted((e,f))),)+p)))
 return out
counts={}
for e in range(len(edges)):
 occ=sorted(list(cut)+[e,e]);p=pairings(occ)
 if p:counts[e]=len(p)
 need(bool(p)==(e in bridges),'all repeated-edge cases')
need(sorted(counts.values())==[9]*5+[225],'matching counts')
need(sum(counts.values())*720==194400,'all candidate ordered words')
print(json.dumps({'checks':checks,'status':'PASS','centers':[v,w],'endpoint_vertices':S,'W_dimension':rk,'active_fock_dimension':2**(rk//2),'bridge_edges':bridges,'pairing_counts':counts,'candidate_ordered_words':sum(counts.values())*720,'seconds':time.monotonic()-start,'rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576},indent=2))
