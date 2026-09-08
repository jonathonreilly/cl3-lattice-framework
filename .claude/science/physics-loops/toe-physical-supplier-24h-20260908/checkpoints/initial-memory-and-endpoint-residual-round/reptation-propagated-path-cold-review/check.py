import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,pathlib,hashlib,json,itertools,importlib.util
import numpy as np
sys.dont_write_bytecode=True
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-propagated-path-initializer');sys.path.insert(0,str(p))
from initialize import initialize
f=json.loads((p/'FINAL_HASHES.json').read_text())
for n,h in f.items():
 if hashlib.sha256((p/n).read_bytes()).hexdigest()!=h:raise RuntimeError('binding')
class Tape:
 def __init__(self,M):self.i=0;self.j=0;self.M=M
 def integers(self,M):
  z=(7*self.i+3)%M;self.i+=1;return z
 def random(self):
  z=((37*self.j+11)%101+.5)/101;self.j+=1;return z
rows=[]
for L in (2,4):
 sites=list(itertools.product(range(L),repeat=3));edges=[(r,d) for r in sites for d in range(3)];ix={x:i for i,x in enumerate(edges)};faces=[]
 for d,e in itertools.combinations(range(3),2):
  for r in sites:
   rd=list(r);re=list(r);rd[d]=(rd[d]+1)%L;re[e]=(re[e]+1)%L
   faces.append([ix[r,d],ix[tuple(rd),e],ix[tuple(re),d],ix[r,e]])
 def can(x,z):return list(x[z]) in ([0,1,0,1],[1,0,1,0])
 def nf(x):return sum(can(x,z) for z in faces)
 M=len(faces);x=np.array([r[d]%2 for r,d in edges],dtype=np.uint8);t=Tape(M)
 for _ in range(M):
  z=faces[t.integers(M)]
  if can(x,z):x[z]^=1
 paths=[x.copy()];labels=[]
 for j in range(12):
  u=t.random()*(M+.05*nf(x));k=int(u) if u<M else -1
  label=k if k>=0 and can(x,faces[k]) else -1
  if label>=0:x[faces[label]]^=1
  labels.append(label);paths.append(x.copy())
 a,info=initialize(L,12,Tape(M),1)
 if list(a.labels)!=labels:raise RuntimeError('actual tape labels')
 for k,j in enumerate((0,6,12)):
  if not np.array_equal(a.states[k],paths[j]) or a.nf[k]!=nf(paths[j]):raise RuntimeError('cache')
  cs=[]
  for h in ((1,) if L==2 else (1,2)):
   for d in range(3):
    for pol in range(3):
     if pol==d:continue
     cs.append(sum((-1)**sum(r)*np.exp(2j*np.pi*h*r[d]/L)*(int(paths[j][i])-.5) for i,(r,e) in enumerate(edges) if e==pol)/np.sqrt(L**3))
  if max(abs(a.O[k]-cs))>1e-12:raise RuntimeError('Fourier cache')
 # Actual midpoint assignment mutant must disagree with literal path when nontrivial.
 mutant=a.states[1].copy();mutant[0]^=1
 if np.array_equal(mutant,paths[6]):raise RuntimeError('mutant survived')
 rows.append({'L':L,'n':12,'labels':labels,'NF':[nf(paths[j]) for j in (0,6,12)],'cache_mutant_rejected':True})
# Independent exact three-state symmetric G: row normalization is not the product-G law.
from fractions import Fraction as Q
G=[[Q(1),Q(1,4),0],[Q(1,4),Q(1),Q(1,2)],[0,Q(1,2),Q(1)]];b=list(map(sum,G));Z=sum(x*x for x in b)
pp=[];qq=[]
for i,j,k in itertools.product(range(3),repeat=3):
 pp.append(G[i][j]*G[j][k]/Z);qq.append(G[i][j]*G[j][k]/(3*b[i]*b[j]))
if sum(pp)!=1 or sum(qq)!=1 or pp==qq:raise RuntimeError('law adverse')
out={'bindings':f,'literal_tape_fixtures':rows,'tiny_exact_Q_vs_pi_TV':str(sum(abs(x-y) for x,y in zip(pp,qq))/2),'scope':'Deterministic tape only; no production or stochastic micro.'}
pathlib.Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
