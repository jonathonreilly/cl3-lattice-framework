import json,itertools,hashlib,time,signal,resource,sys
from fractions import Fraction as F
from pathlib import Path
signal.alarm(180);start=time.monotonic();checks=0
def req(x,msg):
 global checks
 checks+=1
 if not x:raise RuntimeError(msg)
p=Path(__file__).resolve().parent;input=p.parent/'native-virtual-pair-induced-ring/RESULT.json';raw=json.loads(input.read_text());vs=[tuple(x) for x in raw['vertices']];vi={v:i for i,v in enumerate(vs)};es=[tuple(e) for e in raw['edges']];ei={e:k for k,e in enumerate(es)}
expected=set()
for i,v in enumerate(vs):
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;expected.add(tuple(sorted((i,vi[tuple(w)]))))
req(es==sorted(expected),'full graph');nb=[[] for _ in vs];inc=[[] for _ in vs]
for e,(a,b) in enumerate(es):nb[a].append(b);nb[b].append(a);inc[a].append(e);inc[b].append(e)
masks=[]
for e,(a,b) in enumerate(es):
 mask=0
 for v,w in ((a,b),(b,a)):
  for u in nb[v]:
   if u<w:mask^=1<<ei[tuple(sorted((v,u)))]
 masks.append(mask)
def energy6(z,active):
 states=[];ener={};full={}
 for m in range(1<<len(active)):
  zz=z
  for j,e in enumerate(active):
   if m>>j&1:zz^=1<<e
  delta=[sum(zz>>e&1 for e in row)-3 for row in inc]
  if max(map(abs,delta))<=1:states.append(m);ener[m]=sum(d*d for d in delta);full[m]=zz
 req([m for m in states if ener[m]==0]==[0],'unique ice full forest')
 psi=[{m:F(int(m==0)) for m in states}];E=[F(0)]
 for n in range(1,7):
  v={m:F(0) for m in states}
  for m,value in psi[-1].items():
   for j,e in enumerate(active):
    mm=m^(1<<j)
    if mm in ener:v[mm]+=value*(-1)**((full[m]&masks[e]).bit_count())
  E.append(v[0]);psi.append({m:(-v[m]+F(0))/ener[m] if m else F(0) for m in states})
 return E
rows=[]
for bi,string in enumerate(raw['background_bits']):
 z=int(string,2);req(all(sum(z>>e&1 for e in row)==3 for row in inc),'full ice background')
 stars=[];paths=[];pairs=[]
 for v,row in enumerate(inc):
  pairs.extend(itertools.combinations(row,2));stars.extend(itertools.combinations(row,3))
 for e,(u,v) in enumerate(es):
  for a in nb[u]:
   if a==v:continue
   for b in nb[v]:
    if b==u:continue
    paths.append((ei[tuple(sorted((a,u)))],e,ei[tuple(sorted((v,b)))]))
 req(len(set(tuple(sorted(s)) for s in stars))==20*64,'star uniqueness')
 req(len(set(tuple(sorted(s)) for s in paths))==25*192,'path uniqueness')
 alt=sum(((z>>a&1)==(z>>c&1)!=(z>>b&1)) for a,b,c in paths)
 req(alt==9*192,'alternating path exact count')
 # Actual global Pauli/degree recursion for each pattern appearing in each shape.
 samples=[]
 for name,sets in [('pair',pairs),('star',stars),('path',paths)]:
  seen=set()
  for active in sets:
   bits=tuple(z>>e&1 for e in active)
   if bits in seen:continue
   seen.add(bits);E=energy6(z,active)
   if name=='pair':expected=F(-1,2)
   elif name=='star':expected=F(-27,16)
   else:expected=-F(35+int(bits[0]==bits[2]!=bits[1]),32)
   req(E[6]==expected,'actual native sixth energy');samples.append(dict(shape=name,edges=active,bits=bits,E=[str(e) for e in E]))
 total=-F(192,16)-F(3*len(pairs),8)-F(3*len(stars),8)-F(5*len(paths)+alt,32)
 req(total==F(-207*64,8),'uniform full coefficient')
 rows.append(dict(background=bi,initial_bits=string,stars=len(stars),paths=len(paths),alternating_paths=alt,adjacent_pairs=len(pairs),total=str(total),samples=samples))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(0<rss<384 and time.monotonic()-start<180,'resources')
print(json.dumps(dict(checks=checks,rows=rows,input_sha256=hashlib.sha256(input.read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_MiB=rss),indent=2))
