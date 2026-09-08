from itertools import product,combinations
from pathlib import Path
import json,time,signal,resource,sys,hashlib
if __name__=='__main__':signal.alarm(180)
start=time.monotonic();checks=0
def need(c,msg):
 global checks
 checks+=1
 if not c:raise RuntimeError(msg)
L=4;vs=list(product(range(L),repeat=3));ix={v:i for i,v in enumerate(vs)}
edges=[]
for v in vs:
 for a in range(3):
  q=list(v);q[a]=(q[a]+1)%L;edges.append((ix[v],ix[tuple(q)]))
inc=[set() for _ in vs]
for e,(v,w) in enumerate(edges):inc[v].add(e);inc[w].add(e)
for k in (1,2,3):
 for S in combinations(range(len(vs)),k):
  cut=set()
  for v in S:cut.symmetric_difference_update(inc[v])
  internal=sum(v in S and w in S for v,w in edges)
  need(len(cut)==6*k-2*internal,'boundary identity')
  need(len(cut)>10 or k==1 or (k==2 and internal==1),'small subset classification support')
v,w=edges[0];cut=sorted(inc[v]^inc[w]);internal=(inc[v]&inc[w]).pop()
def matching(es):
 if not es:return True
 e=es[0]
 return any(set(edges[e])&set(edges[f]) and matching([x for x in es[1:] if x!=f]) for f in es[1:])
need(not matching(cut),'actual five-pair support obstruction')
pairs=[]
for x in (v,w):
 ext=sorted(inc[x]-{internal});pairs += [(internal,ext[0]),(ext[1],ext[2]),(ext[3],ext[4])]
toggle=set()
for e,f in pairs:
 need(bool(set(edges[e])&set(edges[f])),'legal incident pair')
 toggle.symmetric_difference_update((e,f))
need(toggle==set(cut),'six-insertion possible support')
# Independent finite CAR projector. N=4 physical matter modes. Active gammas
# gamma_0,...,gamma_3; choose a full-rank paired quadratic vacuum.
n=4;dim=1<<n
I=[[complex(i==j) for j in range(dim)] for i in range(dim)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(dim)) for j in range(dim)] for i in range(dim)]
def gamma(a):
 A=[[0j]*dim for _ in range(dim)]
 for b in range(dim):A[b^(1<<a)][b]=(-1)**((b&((1<<a)-1)).bit_count())
 return A
P=I
for a in (0,2):
 C=mm(gamma(a),gamma(a+1));F=[[(I[i][j]+1j*C[i][j])/2 for j in range(dim)] for i in range(dim)];P=mm(P,F)
# Restrict physical total even parity.
for i in range(dim):
 for j in range(dim):
  if i.bit_count()%2 or j.bit_count()%2:P[i][j]=0j
need(mm(P,P)==P,'active vacuum and physical parity projector')
need(sum(P[i][i] for i in range(dim))==2,'spectator dimension')
non_scalar=[]
for mask in range(dim):
 A=[[P[i][j]*(-1)**((j&mask).bit_count()) for j in range(dim)] for i in range(dim)]
 B=mm(A,P)
 if mask.bit_count()%2:need(all(z==0 for row in B for z in row),'odd-cut active parity exclusion')
 if mask in (0,dim-1):need(B==P,'trivial cut identity')
 if mask.bit_count()==2:
  ratios={B[i][j]/P[i][j] for i in range(dim) for j in range(dim) if P[i][j]}
  if len(ratios)>1 or any(B[i][j] and not P[i][j] for i in range(dim) for j in range(dim)):non_scalar.append(mask)
need(3 in non_scalar,'allowed even cut need not project to scalar')
result={'checks':checks,'status':'PASS','five_pair_matching':False,'six_pairs':pairs,'non_scalar_even_masks':non_scalar,'seconds':time.monotonic()-start,'rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024),'scope':'Finite support and Clifford controls; no sixth-order coefficient or cubic spectral-isolation test'}
out=result
if __name__=='__main__':print(json.dumps(out,indent=2))
