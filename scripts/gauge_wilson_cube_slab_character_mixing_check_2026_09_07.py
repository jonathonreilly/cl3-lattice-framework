import os,time,signal
start=time.monotonic();signal.alarm(180)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import itertools,json,resource,sys,hashlib
from pathlib import Path
import numpy as np
from fractions import Fraction as F
import math
vertices=list(itertools.product((0,1),repeat=3));edges=[]
for v in vertices:
 for a in range(3):
  if v[a]==0:
   w=list(v);w[a]=1;edges.append((v,tuple(w)))
assert len(edges)==12
index={e:i for i,e in enumerate(edges)}
def square(a,b,fixed):
 c=({0,1,2}-{a,b}).pop();v=[0,0,0];v[c]=fixed
 p=[tuple(v)];v[a]=1;p.append(tuple(v));v[b]=1;p.append(tuple(v));v[a]=0;p.append(tuple(v))
 out=np.zeros(12,dtype=np.int8)
 for v,w in zip(p,p[1:]+p[:1]):
  if (v,w) in index:out[index[v,w]]+=1
  else:out[index[w,v]]-=1
 return out
source=np.zeros(24,dtype=np.int8);source[:12]=square(0,1,0)
cols=[];names=[]
for layer in (0,1):
 for a,b in ((0,1),(0,2),(1,2)):
  for fixed in (0,1):
   if (a,b,fixed)==(0,1,0):continue
   z=np.zeros(24,dtype=np.int8);z[12*layer:12*(layer+1)]=square(a,b,fixed)
   cols.append(z);names.append(f'spatial_t{layer}_axes{a}{b}_fixed{fixed}')
for e in range(12):
 z=np.zeros(24,dtype=np.int8);z[e]=-1;z[12+e]=1;cols.append(z);names.append(f'temporal_edge{e}')
cols=np.asarray(cols);records=[];tested=0
for k in range(6):
 signs=np.asarray(list(itertools.product((-1,1),repeat=k)),dtype=np.int8).reshape(2**k,k)
 solutions=[];count=0
 for ids in itertools.combinations(range(22),k):
  flux=signs@cols[list(ids)]+source
  matches=np.flatnonzero(np.all(flux%3==0,axis=1));count+=len(signs)
  for m in matches:solutions.append([(names[i],int(s)) for i,s in zip(ids,signs[m])])
 tested+=count;records.append(dict(degree=k,signed_subsets_tested=count,solutions=solutions))
assert all(not r['solutions'] for r in records[:5])
assert len(records[5]['solutions'])==1
assert all(name.startswith('spatial_t0') for name,s in records[5]['solutions'][0])
# Exact rational controls supplement, rather than replace, the Haar proof.
partial=sum((F(5)**n/F(math.factorial(n)) for n in range(21)),F())
exp5upper=partial+F(5)**21/F(math.factorial(21))/(1-F(5,22))
assert exp5upper<149
leading=F(1,12**5*81);anisotropic_error=F(10728,10**12)
assert anisotropic_error<leading
b=F(1,10**14);isotropic_error_over_b5=F(17**6,120)*b
assert 17*b<F(1,2);assert isotropic_error_over_b5<leading
assert tested==973017
assert len(set(names))==22
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert math.isfinite(rss) and 0<rss<180;assert time.monotonic()-start<180
out=dict(status='PASS',rational_checks=4,structural_assertions=6,runtime_input_files=[],normalization='Unnormalized temporal Wilson product; positive normalization preserves sign, not the displayed absolute remainder bound.',anisotropic_lower=str(leading),anisotropic_error_upper=str(anisotropic_error),isotropic_b=str(b),isotropic_coefficient=str(leading),isotropic_remainder_over_b5_upper=str(isotropic_error_over_b5),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),edges=edges,source_incidence=source.tolist(),face_names=names,face_incidence=cols.tolist(),records=records,total_signed_subsets=tested,seconds=time.monotonic()-start,rss_MiB=rss,scope='Exact necessary SU3 center selection; surviving actual Haar coefficient evaluated separately by disk gluing.')
if '--json' in sys.argv:print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS: 973017 exact signed subsets; unique degree-five cap, four rational controls.')
 print('N5: Actual two-slice cube Wilson/Haar source compression, supplied action and embedding.')
 print('N5: Center flux is a necessary selection rule; source proof supplies actual Haar contraction.')
 print('N5: Anisotropic and isotropic tiny positive points are derived rational corollaries.')
 print('N5: Positive normalization preserves mixing; no beta6, dressed-map or continuum identification.')
 print('N5: Runtime file inputs none; source SHA '+out['source_sha256'])
