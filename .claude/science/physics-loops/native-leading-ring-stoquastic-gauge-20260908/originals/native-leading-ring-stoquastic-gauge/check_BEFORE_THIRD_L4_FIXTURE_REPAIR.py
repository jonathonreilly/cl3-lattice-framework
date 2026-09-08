from pathlib import Path
from itertools import product,combinations
import json,hashlib,time,signal,resource,sys
signal.alarm(180);start=time.monotonic();checks=0

def need(c,m):
 global checks
 if not c:raise RuntimeError(m)
 checks+=1
results=[]
for L in [4,6]:
 vs=list(product(range(L),repeat=3));index={v:i for i,v in enumerate(vs)};labels=[(v,a) for v in vs for a in range(3)];li={x:i for i,x in enumerate(labels)}
 def shift(v,a):q=list(v);q[a]=(q[a]+1)%L;return tuple(q)
 edges=[(index[v],index[shift(v,a)]) for v,a in labels];E=len(edges);native=[];upper=[];linear=0
 for e,ab in enumerate(edges):
  w=sum(1<<f for f in range(e) if set(ab)&set(edges[f]));native.append(w);i,j=sorted(ab)
  ell=sum(1<<f for f,(u,v) in enumerate(edges) if (i<=u<j)!=(i<=v<j));M=w^ell;upper.append(M&~((1<<(e+1))-1))
  need((M>>e)&1,'M diagonal')
  v,a=labels[e]
  if sum(v[:a])%2:linear|=1<<e
 def d(x):return (-1)**sum((upper[e]&x).bit_count() for e in range(E) if x>>e&1)
 def phase(x):return d(x)*(-1)**((linear&x).bit_count())
 faces=[tuple(li[v,a] for _ in [0])+ (li[shift(v,a),b],li[shift(v,b),a],li[v,b]) for a,b in combinations(range(3),2) for v in vs]
 cycles=faces.copy()
 if L==4:
  for a in range(3):
   for v in vs:
    if v[a]==0:
     z=v;es=[]
     for _ in range(4):es.append(li[z,a]);z=shift(z,a)
     cycles.append(tuple(es))
 def legal(x,es):return all(((x>>es[k])&1)!=((x>>es[(k+1)%4])&1) for k in range(4))
 seed=sum((v[a]%2)<<e for e,(v,a) in enumerate(labels));states=[seed]
 for p in ([6,258] if L==6 else [0,None]):
  x=states[-1]
  if p is None:p=next(j for j,es in enumerate(faces) if j!=0 and legal(x,es))
  if not legal(x,faces[p]):raise RuntimeError('fixed prep not legal')
  states.append(x^sum(1<<e for e in faces[p]))
 tests=0;wrong=False;wind=0
 for x in states:
  for ci,es in enumerate(cycles):
   # background holonomy uses actual distinct physical edge labels.
   hol=(-1)**sum((linear>>e)&1 for e in es);need(hol==(-1 if ci<len(faces) else 1),'pi background')
   if not legal(x,es):continue
   y=x;amp=1
   for e in es:amp*=(-1)**((native[e]&y).bit_count());y^=1<<e
   transformed=amp*phase(y)*phase(x);need(transformed==-1,'actual full native transition')
   eta=1 if ci<len(faces) else -1;need(amp*d(y)*d(x)==eta,'W orientation ratio');tests+=1
   if ci>=len(faces):wind+=1
   if ci<len(faces) and amp*d(y)*d(x)!=-1:wrong=True
 need(wrong,'trivial background actual failure')
 results.append({'L':L,'fixtures_sha256':[hashlib.sha256(x.to_bytes((E+7)//8,'little')).hexdigest() for x in states],'all_legal_transition_controls':tests,'legal_winding_transitions':wind,'cycle_count':len(cycles)})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);need(rss<384,'RSS');out={'checks':checks,'results':results,'seconds':time.monotonic()-start,'rss_mib':rss,'scope':'fixed actual full-bit fixtures, every legal H4 transition; no sampling'};Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
