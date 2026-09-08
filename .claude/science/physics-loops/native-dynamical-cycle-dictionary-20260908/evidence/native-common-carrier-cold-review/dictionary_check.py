import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import numpy as np,itertools,json,time,hashlib
from pathlib import Path
start=time.monotonic();v=5;edges=[(2,4),(0,4),(1,2),(0,1),(3,4),(2,3)];E=len(edges);D=1<<E
# Deliberately nonlexicographic edge order and heterogeneous local neighbor orders.
order={0:[4,1],1:[0,2],2:[3,1,4],3:[4,2],4:[2,0,3]}
Z=np.diag([1,-1]);X=np.array([[0,1],[1,0]]);I=np.eye(2)
def kron(factors):
 o=np.array([[1.]])
 for f in factors:o=np.kron(o,f)
 return o
# Little-endian bit labels, direct dense Jordan-Wigner matrices independent of author's bit-action gamma.
gam=[kron([X if j==i else Z if j<i else I for j in reversed(range(v))]) for i in range(v)]
occ=[]
for x in range(D):occ.append(sum((sum((x>>e)&1 for e,ends in enumerate(edges) if i in ends)%2)<<i for i in range(v)))
masks=[]
for e,(i,j) in enumerate(edges):
 w=0
 for a,b in [(i,j),(j,i)]:
  for nb in order[a][:order[a].index(b)]:w^=1<<edges.index(tuple(sorted((a,nb))))
 ell=0
 for f,(a,b) in enumerate(edges):
  if ((i<=a<j)+(i<=b<j))%2:ell|=1<<f
 masks.append(w^ell)
phase=[]
for x in range(D):phase.append((-1j)**x.bit_count()*(-1)**sum(((masks[e]>>f)&1)*((x>>e)&1)*((x>>f)&1) for e in range(E) for f in range(e+1,E)))
A={};B=[np.diag([1-2*((n>>i)&1) for n in occ]) for i in range(v)];checks=0;badphase=0
for e,(i,j) in enumerate(edges):
 mat=np.zeros((D,D),complex);target=np.zeros_like(mat);cg=-1j*gam[i]@gam[j]
 for x in range(D):
  w=0
  for a,b in [(i,j),(j,i)]:
   for nb in order[a][:order[a].index(b)]:w^=1<<edges.index(tuple(sorted((a,nb))))
  y=x^(1<<e);mat[y,x]=(-1)**((w&x).bit_count());target[y,x]=cg[occ[y],occ[x]]
 transformed=np.diag(phase)@mat@np.diag(np.conjugate(phase))
 if not np.array_equal(transformed,target):raise RuntimeError('quadratic intertwiner')
 badphase+=not np.array_equal(mat,target);A[i,j]=mat;A[j,i]=-mat;checks+=1
 t=1j/2*mat@(B[i]-B[j]);tg=1j/2*target@(B[i]-B[j])
 if not np.array_equal(np.diag(phase)@t@np.diag(np.conjugate(phase)),tg):raise RuntimeError('T')
 checks+=1
cycles=[[0,1,2,3,4],[0,1,2,4],[2,3,4]]
for cycle in cycles:
 s=np.eye(D,dtype=complex);mask=0
 for a,b in zip(cycle,cycle[1:]+cycle[:1]):s=s@A[a,b];mask^=1<<edges.index(tuple(sorted((a,b))))
 s*=1j**len(cycle);u=np.diag(phase)@s@np.diag(np.conjugate(phase));expected=np.zeros_like(u)
 for x in range(D):expected[x^mask,x]=1
 if not np.array_equal(u,expected):raise RuntimeError('cycle')
 checks+=1
# Explicit enlarged-basis all+Gauss census; do not assume m-1 independent equations.
allowed=[]
for n in range(1<<v):
 for x in range(D):
  if all(((n>>i)&1)==sum((x>>e)&1 for e,ends in enumerate(edges) if i in ends)%2 for i in range(v)):allowed.append((n,x))
if len(allowed)!=D or any(n.bit_count()%2 for n,x in allowed):raise RuntimeError('Gauss dimension')
if not badphase:raise RuntimeError('missing-phase adverse inert')
out=dict(graph=edges,neighbor_orders=order,cycles=cycles,exact_matrix_groups=checks,Gauss_dimension=len(allowed),enlarged_dimension=2**(v+E),missing_phase_failures=badphase,seconds=time.monotonic()-start)
Path(__file__).with_name('DICTIONARY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
