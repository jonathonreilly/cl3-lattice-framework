import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
import numpy as np,json,hashlib
from scipy.sparse import coo_matrix,diags,eye
from scipy.sparse.linalg import eigsh
p=Path('/private/tmp/toe-24h-probes-20260908/energy-source-structure');d=np.load(p/'raw.npz');r=json.loads((p/'RESULT.json').read_text());checks={}
def ck(n,v):
 assert v,n
 checks[n]=True
states=list(map(int,d['states']));lookup={x:i for i,x in enumerate(states)}
# Infer Cartesian labels directly from index encoding r=(i//12,(i//6)%2,(i//3)%2), direction=i%3.
coords=[(i//12,(i//6)%2,(i//3)%2) for i in range(24)]
obs=np.zeros((864,6));modes=[(a,b) for a in range(3) for b in range(3) if a!=b]
for k,x in enumerate(states):
 for m,(a,b) in enumerate(modes):
  obs[k,m]=sum((-1)**(sum(coords[i])+coords[i][a])*(2*((x>>i)&1)-1) for i in range(24) if i%3==b)/np.sqrt(32)
ck('independent_all_source_values',np.max(abs(obs-d['O']))<1e-13)
# Every recorded directed move must be a genuine four-bit alternating square, and all eligible faces present.
pairs=[]
for i,x in enumerate(states):
 for face in d['faces']:
  bits=[(x>>int(j))&1 for j in face]
  if bits in ([0,1,0,1],[1,0,1,0]):
   y=x
   for j in face:y^=1<<int(j)
   pairs.append((lookup[y],i))
ck('all_geometric_moves',sorted(pairs)==sorted(zip(map(int,d['rows']),map(int,d['columns']))))
A=coo_matrix((np.ones(len(pairs)),tuple(zip(*pairs))),shape=(864,864)).tocsr();nf=np.asarray(A.sum(0)).ravel();X=np.sum(obs**2,axis=1)
for row in r['rows']:
 v,l=row['V'],row['lambda'];H=diags(v*nf+l*X)-A
 es,ps=eigsh(H,k=1,which='SA',tol=1e-12,v0=np.linspace(2,1,864));psi=ps[:,0];psi*=np.sign(psi.sum());e=es[0]
 ck(f'energy_{v}_{l}',abs(e-row['E'])<1e-11)
 ck(f'pure_and_mixed_{v}_{l}',abs(np.dot(psi**2,X)-row['pure_X'])<1e-10 and abs(np.dot(psi,X)/sum(psi)-row['mixed_X'])<1e-10)
 ck(f'zero_means_{v}_{l}',np.max(abs(psi**2@obs))<1e-10)
 # Direct shifted row residual on independent Perron vector.
 cap=12*abs(l);b=1+((1-v)*nf+cap-l*X)/24
 kernel=A/24+diags(b-nf/24)
 ck(f'shifted_eigen_{v}_{l}',np.linalg.norm(kernel@psi-(1-(e-cap)/24)*psi)<1e-10)
for path,sha in json.loads((p/'SOURCE_BINDING.json').read_text())['actually_used_inputs'].items():ck('hash_'+Path(path).name,hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha)
out={'checks':checks,'count':len(checks),'coverage':'all864 source rows and6912 moves;14 independent eigenproblems; author modules not imported','hashes':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ['check.py','DERIVATION.md','raw.npz','RESULT.json','PREREGISTRATION.md']}}
Path(__file__).with_name('ACTUAL_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
