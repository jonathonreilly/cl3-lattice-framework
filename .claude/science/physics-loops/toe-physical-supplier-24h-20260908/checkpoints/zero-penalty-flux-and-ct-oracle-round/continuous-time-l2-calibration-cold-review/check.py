from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,math,hashlib,signal,time,resource,sys
signal.alarm(180);start=time.monotonic();B=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l2-calibration-design');N=0
def need(c,s):
 global N
 if not c:raise RuntimeError(s)
 N+=1
raw=json.loads((B/'BACKWARD_POWERS.json').read_text());oracle=json.loads((B/'ORACLE.json').read_text());parse=lambda z:F(int(z['numerator']),int(z['denominator']))
vs=list(product(range(2),repeat=3));links=[(v,a) for v in vs for a in range(3)];ix={x:i for i,x in enumerate(links)}
def shift(v,a):q=list(v);q[a]^=1;return tuple(q)
faces=[(ix[v,a],ix[shift(v,a),b],ix[shift(v,b),a],ix[v,b]) for a,b in combinations(range(3),2) for v in vs];masks=[sum(1<<e for e in f) for f in faces]
def legal(x,f):b=[(x>>e)&1 for e in f];return b in ([0,1,0,1],[1,0,1,0])
seed=sum((v[a]%2)<<i for i,(v,a) in enumerate(links));states=[seed];seen={seed}
for x in states:
 for f,m in zip(faces,masks):
  if legal(x,f) and x^m not in seen:seen.add(x^m);states.append(x^m)
need(len(seen)==864 and set(raw['states'])==seen,'component exact')
index={x:i for i,x in enumerate(raw['states'])};nf=[];ns=[]
for i,x in enumerate(raw['states']):
 neighbors=[index[x^m] for f,m in zip(faces,masks) if legal(x,f)];ns.append(neighbors);nf.append(len(neighbors));need(neighbors==raw['neighbors'][i],'adjacency');need(raw['diag'][i]==480-19*len(neighbors),'480G diag')
 if i:need(raw['states'][raw['parents'][i]]^masks[raw['parent_face'][i]]==x and legal(raw['states'][raw['parents'][i]],faces[raw['parent_face'][i]]),'BFS witness')
for name,initial in [('h',[1]*864),('h_NF',nf)]:
 need(raw[name][0]==initial,'initial power')
 for k in range(1,len(raw[name])):
  prev=raw[name][k-1];need(raw[name][k]==[(480-19*nf[i])*prev[i]+20*sum(prev[j] for j in ns[i]) for i in range(864)],'whole power '+name+str(k))
for row in oracle['targets']:
 T=F(row['T_total']);x=24*T;lam=F(21,20)*x;J=math.ceil(x)+64;lower=sum((x**j/F(math.factorial(j)) for j in range(J+1)),F(0));K=row['K']
 def bound(k):return lam**(k+1)/math.factorial(k+1)/(1-lam/F(k+2))/lower
 need(bound(K)==parse(row['TV_upper']) and bound(K)<=F(1,10**14)<bound(K-1),'minimal exact cap')
 need(lam**(K+1)/math.factorial(K)/(1-lam/F(K+1))/lower==parse(row['count_tail_moment_upper']),'first moment tail')
 coef=[int(20/T)**(K-k)*math.factorial(K)//math.factorial(k) for k in range(K+1)];weights=[coef[k]*sum(raw['h'][k]) for k in range(K+1)];need(weights==list(map(int,row['count_weights_integer'])),'integer count weights');Z=sum(weights);need(Z==int(row['count_normalizer_integer']),'Z')
 # Independent midpoint coefficient from a binomial distribution over split index.
 mid=sum((F(coef[k]*math.comb(k,j),2**k)*sum(raw['h'][j][i]*nf[i]*raw['h'][k-j][i] for i in range(864)) for k in range(K+1) for j in range(k+1)),F(0))/Z
 need(mid==parse(row['moments']['mid_NF']),'exact midpoint NF')
 # Endpoint energy independently uses row sums: H1=-NF/20.
 end=-F(sum(coef[k]*sum(nf[i]*raw['h'][k][i] for i in range(864)) for k in range(K+1)),20*Z);need(end==parse(row['moments']['endpoint_h']),'endpoint h')
freeze=json.loads((B/'FINAL_FREEZE.json').read_text())
for name,h in freeze['files'].items():need(hashlib.sha256((B/name).read_bytes()).hexdigest()==h,'freeze '+name)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);need(rss<384,'RSS');out={'checks':N,'seconds':time.monotonic()-start,'rss_mib':rss,'scope':'deterministic coordinate BFS, all integer columns, exact cap/count/NF/endpoint replay; no author imports or sampling'};O=Path(__file__).parent;(O/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');(O/'READ_HASHES.json').write_text(json.dumps({str(B/f):h for f,h in freeze['files'].items()},indent=2)+'\n');print(out)
