#!/usr/bin/env python3
"""Independent complete F3 incidence-system certificate for the actual cube slab.

Bit-vertex geometry and row reduction are independent of signed-subset enumeration.
Center selection is necessary; the surviving Haar coefficient is source-proved.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,resource,signal,sys,time
from pathlib import Path
AUDIT_TIMEOUT_SEC=180
signal.alarm(AUDIT_TIMEOUT_SEC)
started=time.monotonic()
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--json',action='store_true')
args=parser.parse_args()
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
free=[j for j in range(22) if j not in piv];hist={};low=[];solutions=[]
for vals in product(range(3),repeat=len(free)):
 x=[0]*22
 for j,v in zip(free,vals):x[j]=v
 for i,j in enumerate(piv):x[j]=(A[i][22]-sum(A[i][k]*x[k] for k in free))%3
 assert all((sum(faces[j][i]*x[j] for j in range(22))+src[i])%3==0 for i in range(24))
 solutions.append(x)
 w=sum(v!=0 for v in x);hist[w]=hist.get(w,0)+1
 if w<=5:low.append([(names[j],1 if v==1 else -1) for j,v in enumerate(x) if v])
assert min(hist)==5 and hist[5]==1
assert all(n[0]==0 for n,s in low[0])
b=F(1,10**14);leading=F(1,12**5*81);remainder=F(17**6,120)*b
assert remainder<leading
out={'rank':row,'nullity':len(free),'all_residue_solutions':sum(hist.values()),'support_histogram':hist,'support_at_most5':low,'signed_subsets_through5':sum(math.comb(22,k)*2**k for k in range(6)),'relative_remainder_ceiling':str(remainder/leading)}

checks=[]
def ck(name,condition):
    if name in checks or not condition:raise AssertionError(name)
    checks.append(name)
particular=[0]*22
for i,j in enumerate(piv):particular[j]=A[i][22]
basis=[]
for k in free:
    v=[0]*22;v[k]=1
    for i,j in enumerate(piv):v[j]=-A[i][k]%3
    basis.append(v)
ck('twelve spatial edges',len(edges)==12 and len(set(edges))==12)
ck('twenty-four Haar link rows',len(A)==24 and len(src)==24)
ck('twenty-two action columns',len(faces)==22 and all(len(v)==24 for v in faces))
ck('affine rank seventeen',row==17)
ck('nullity five',len(free)==5)
ck('all free assignments exhausted',len(solutions)==3**len(free)==243)
ck('all solutions unique',len({tuple(x) for x in solutions})==243)
ck('all 5832 link congruences',all((sum(faces[j][i]*x[j] for j in range(22))+src[i])%3==0 for x in solutions for i in range(24)))
ck('particular solution',all((sum(faces[j][i]*particular[j] for j in range(22))+src[i])%3==0 for i in range(24)))
ck('five homogeneous basis vectors',all(sum(faces[j][i]*v[j] for j in range(22))%3==0 for v in basis for i in range(24)))
ck('unique minimal support five',min(hist)==5 and hist[5]==1)
ck('next support nine',sorted(hist)[1]==9)
ck('minimal cap on input slice',len(low)==1 and all(n[0]==0 for n,sgn in low[0]))
ck('signed subset comparison count',out['signed_subsets_through5']==973017)
ck('explicit isotropic remainder margin',remainder<leading)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
elapsed=time.monotonic()-started
if not(math.isfinite(rss) and 0<rss<180 and math.isfinite(elapsed) and 0<=elapsed<180):raise AssertionError('resource contract')
out.update(checks=checks,check_count=len(checks),minimum_support=5,next_support=9,
    edges=edges,vertex_dictionary='v=x+2y+4z; each bit coordinate is0 or1',face_names=names,
    source_incidence=src,face_incidence=faces,pivot_columns=piv,free_columns=free,
    augmented_rref=A,particular_solution=particular,homogeneous_basis=basis,solutions=solutions,
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies={},
    seconds=elapsed,rss_MiB=rss,resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),
    scope='Complete exact F3 center-selection system on the supplied actual cube-slab graph. No Haar integral is numerically evaluated; source Schur gluing supplies the surviving coefficient. The displayed Taylor comparison is for the unnormalized numerator; positive temporal partition division preserves its sign. No beta6 or dressed-environment identification.')
if args.json:print(json.dumps(out,indent=2,allow_nan=False))
else:
    print('PASS independent actual cube-slab F3 system:',len(checks),'named checks')
    print('per_element:24 Haar links,22 action faces; all5832 solution-link congruences verified.')
    print('per_site: bit-vertex geometry, rank17/nullity5; all243 affine residue solutions retained in JSON.')
    print('per_mode: support histogram',json.dumps(hist,sort_keys=True))
    print('per_block: unique input cap',json.dumps(low[0]),'; minimum5, next9.')
    print('lattice_wide: necessary center selection plus exact scalar remainder comparison; Haar coefficient remains source proof.')
    print('REMAINDER_TO_LEADING_CEILING',out['relative_remainder_ceiling'])
    print('SOURCE_SHA256',out['source_sha256']);print('DEPENDENCIES {}')
    print('RESOURCES',elapsed,rss,'seconds/MiB;180 limits, BLAS1')
    print('TOTAL: PASS FAIL=0')
