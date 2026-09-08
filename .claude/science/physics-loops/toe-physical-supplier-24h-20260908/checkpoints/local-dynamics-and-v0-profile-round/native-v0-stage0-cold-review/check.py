import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,hashlib,time,signal,resource,sys,itertools
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix,diags,eye
signal.alarm(180);start=time.monotonic();base=Path('/private/tmp/toe-24h-probes-20260908/native-v0-stage0');out=Path(__file__).parent;checks=0
def req(x,m):
 global checks
 checks+=1
 if not x:raise RuntimeError(m)
freeze=json.loads((base/'FINAL_FREEZE.json').read_text());req(hashlib.sha256((base/'FINAL_FREEZE.json').read_bytes()).hexdigest()=='3f796ea36e3fb8c19cdcaab0f411b964e4c3838a680a3f3449dcf1b0fa6335bc','freeze')
for n,h in freeze.items():req(hashlib.sha256((base/n).read_bytes()).hexdigest()==h,n)
runtime=json.loads((base/'RUNTIME.json').read_text());bad=[]
for n,h in runtime['files'].items():
 if not Path(n).is_file() or hashlib.sha256(Path(n).read_bytes()).hexdigest()!=h:bad.append(n)
req(not bad,'runtime bytes')
# Own integer-bit graph: no author geometry/count/transition functions imported.
rs=list(itertools.product(range(2),repeat=3));links=[(r,a) for r in rs for a in range(3)];ix={x:i for i,x in enumerate(links)};faces=[]
for a,b in itertools.combinations(range(3),2):
 for r in rs:
  ra=list(r);rb=list(r);ra[a]^=1;rb[b]^=1
  faces.append((ix[r,a],ix[tuple(ra),b],ix[tuple(rb),a],ix[r,b]))
seed=sum((r[a]%2)<<i for i,(r,a) in enumerate(links));states=[seed];index={seed:0};edges=[];nf=[]
for z in states:
 d=0
 for a,b,c,e in faces:
  v=[z>>i&1 for i in (a,b,c,e)]
  if v in ([0,1,0,1],[1,0,1,0]):
   y=z^sum(1<<i for i in (a,b,c,e))
   if y not in index:index[y]=len(states);states.append(y)
   edges.append((len(nf),index[y]));d+=1
 nf.append(d)
req(len(states)==864 and len(edges)==6912,'own graph');nf=np.array(nf);A=csr_matrix((np.ones(len(edges)),tuple(zip(*edges))),shape=(864,864));req((A-A.T).nnz==0,'own symmetry')
O=np.array([[sum((-1)**(sum(r)+r[a])*((z>>i&1)-.5) for i,(r,b) in enumerate(links) if b==pol)/np.sqrt(8) for a in range(3) for pol in range(3) if pol!=a] for z in states]);X=(O*O).sum(1);records=[];author=json.loads((base/'RESULT.json').read_text())
for V in (0.,.95,1.):
 H=diags(V*nf)-A;G=eye(864)-H/24;h=(V-1)*nf
 for n in (2,48,192):
  p=np.ones(864);q=h.copy()
  for _ in range(n//2):
   p=G@p;q=G@q;scale=np.linalg.norm(p);p/=scale;q/=scale
  E=p@q;HH=q@q;S=p@(X*p);cross=p@(X*q);N=p@(nf*p);D=4*(V*N-E)/(8*S);R=sum((O[:,j]*p)@(H@(O[:,j]*p)) for j in range(6))/S-E
  req(abs(R-D-(cross/S-E))<3e-12,'independent residual')
  req(abs(HH-(H@p)@(H@p))<3e-12,'endpoint pair moment')
  a=next(a for a in author['oracles'] if a.get('n')==n and a['V']==V)
  for key,val in [('E',E),('S',S),('NF',N),('D',D),('R',R),('correction',cross/S-E),('VarH',HH-E*E)]:req(abs(a[key]-val)<3e-11,'oracle '+key)
  records.append(dict(V=V,n=n,E=float(E),D=float(D),R=float(R),endpoint_H2=float(HH),cross=float(cross)))
# Actual core deterministic replay at fresh irrational-like fixed tapes is independently covered by author literal tests; here no author checker replay.
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(0<rss<384 and time.monotonic()-start<180,'resources')
(out/'RESULT.json').write_text(json.dumps(dict(checks=checks,records=records,runtime_files_verified=len(runtime['files']),seconds=time.monotonic()-start,rss_mib=rss),indent=2)+'\n')
(out/'HASH_COVERAGE.json').write_text(json.dumps(freeze,indent=2)+'\n');print(checks)
