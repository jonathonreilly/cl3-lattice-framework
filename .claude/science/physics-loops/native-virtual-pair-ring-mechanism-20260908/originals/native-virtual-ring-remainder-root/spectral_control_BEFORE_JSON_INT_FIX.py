import hashlib,json,time,signal,resource,sys
from pathlib import Path
import numpy as np
signal.alarm(180);start=time.monotonic();p=Path(__file__).parent
src=p.parent/'native-virtual-pair-induced-ring/RESULT.json';raw=json.loads(src.read_text());edges=[tuple(e) for e in raw['edges']];verts=raw['vertices'];ei={e:k for k,e in enumerate(edges)};inc=[sum(1<<k for k,e in enumerate(edges) if v in e) for v in range(64)];masks=[]
for e,(a,b) in enumerate(edges):
 mask=0
 for v,w in [(a,b),(b,a)]:
  for f,(i,j) in enumerate(edges):
   if v in (i,j) and (j if i==v else i)<w:mask^=1<<f
 masks.append(mask)
active=raw['example_all24']['edges'];seed=int(raw['example_all24']['initial_bits'],2);states=[seed^sum(((b>>i)&1)<<e for i,e in enumerate(active)) for b in range(16)]
def charge(x):return [(x&m).bit_count()-3 for m in inc]
if any(max(map(abs,charge(x)))>1 for x in states):raise RuntimeError('literal low block')
D=np.array([sum(q*q for q in charge(x)) for x in states]);ice=np.flatnonzero(D==0);V=np.zeros((16,16));index={x:i for i,x in enumerate(states)}
for i,x in enumerate(states):
 for e in active:V[index[x^(1<<e)],i]=(-1)**((x&masks[e]).bit_count())
if len(ice)!=2 or not np.array_equal(V,V.T):raise RuntimeError('Hermitian ice block')
R=np.diag(np.divide(1.0,D,out=np.zeros(16),where=D!=0));A2=(V@R@V)[np.ix_(ice,ice)];A4=(V@R@V@R@V@R@V)[np.ix_(ice,ice)];C=4;H4=-A4+C*C/8*np.eye(2)
if not np.array_equal(A2,2*np.eye(2)) or max(abs(np.linalg.eigvalsh(H4)-[1,2]))>1e-12:raise RuntimeError('fourth coefficients')
rows=[];killed=0
for g in [.005,.01,.025,.05,.0625]:
 actual=np.linalg.eigvalsh(np.diag(D)+g*V)[:2];approx=np.linalg.eigvalsh(-g*g*A2+g**4*H4);mutant=np.linalg.eigvalsh(-g*g*A2-g**4*A4);a=4*g;bound=a**6;dist=max(min(abs(v-approx)) for v in actual);bad=max(min(abs(v-mutant)) for v in actual)
 if dist>bound+1e-13:raise RuntimeError('spectral error bound')
 killed+=bad>bound+1e-13;rows.append(dict(g=g,a=a,actual=actual.tolist(),fourth=approx.tolist(),one_sided_distance=dist,bound=bound,missing_folded_distance=bad))
if not killed:raise RuntimeError('missing-folded control survived')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
if time.monotonic()-start>=180 or rss>=384:raise RuntimeError('resources')
out=dict(PASS=True,rows=rows,missing_folded_bound_failures=killed,active_edges=active,seed_bits=format(seed,'0192b'),scope='Double-precision16-state invariant block of actual L4 native model with only four nonzero couplings; numerical control, not proof or full-spectrum census.',seconds=time.monotonic()-start,rss_MiB=rss,source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),fixture_sha=hashlib.sha256(src.read_bytes()).hexdigest(),numpy_version=np.__version__)
(p/'SPECTRAL_CONTROL.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
