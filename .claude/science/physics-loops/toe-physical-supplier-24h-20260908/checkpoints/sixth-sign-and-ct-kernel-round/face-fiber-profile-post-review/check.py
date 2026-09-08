from pathlib import Path
from itertools import product,combinations
import json,hashlib,struct,cmath,math,time,signal,resource,sys
signal.alarm(180);start=time.monotonic();B=Path('/private/tmp/toe-24h-probes-20260908/face-fiber-profile');O=B/'PROFILE_OUTPUT';count=0

def need(v,m):
 global count
 count+=1
 if not v:raise RuntimeError(m)
for file in ['FINAL_FREEZE.json','RUNTIME.json','SOURCE_BINDINGS.json']:
 obj=json.loads((B/file).read_text());mapping=obj.get('files',obj)
 for path,h in mapping.items():need(hashlib.sha256((B/path).read_bytes()).hexdigest()==h,'bound bytes '+path)
L=8;vertices=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(vertices)};links=[(r,a) for r in vertices for a in range(3)]
def move(r,a):v=list(r);v[a]=(v[a]+1)%L;return tuple(v)
faces=[]
for a,b in combinations(range(3),2):
 for r in vertices:faces.append((3*idx[r]+a,3*idx[move(r,a)]+b,3*idx[move(r,b)]+a,3*idx[r]+b))
masks=[sum(1<<e for e in es) for es in faces];maskindex={m:i for i,m in enumerate(masks)}
edgefaces=[set() for _ in links]
for p,es in enumerate(faces):
 for e in es:edgefaces[e].add(p)
affected=[set.union(*(edgefaces[e] for e in es)) for es in faces]
def legal(x,p):
 es=faces[p];b=[x>>e&1 for e in es];return b[0]==b[2] and b[1]==b[3] and b[0]!=b[1]
def nf(x):return sum(legal(x,p) for p in range(1536))
seed=sum((r[a]%2)<<e for e,(r,a) in enumerate(links));results=[]
report=json.loads((O/'RESULT.json').read_text());need(report['status']=='complete','complete')
for case in range(2):
 folder=O/f'case{case}';meta=json.loads((folder/'meta.json').read_text())
 for name,h in meta['files'].items():need(hashlib.sha256((folder/name).read_bytes()).hexdigest()==h,'payload hash')
 raw=(folder/'states.bin').read_bytes();states=[int.from_bytes(raw[i:i+192],'little') for i in range(0,len(raw),192)];del raw
 counts=[v[0] for v in struct.iter_unpack('<H',(folder/'nf.bin').read_bytes())];wit=[v[0] for v in struct.iter_unpack('<H',(folder/'witness.bin').read_bytes())]
 need(len(states)==110593 and len(counts)==len(states),'complete path length')
 x=seed
 for p in wit:need(0<=p<1536 and legal(x,p),'legal witness');x^=masks[p]
 need(x==states[0],'witness endpoint');current=nf(x);total=current;need(current==counts[0],'first NF');nonself=0;activity=0
 for t,y in enumerate(states[1:],1):
  need(0<=y<1<<1536,'binary bound')
  if x!=y:
   p=maskindex.get(x^y);need(p is not None and legal(x,p),'actual positive bond');nonself+=1
   current+=sum(int(legal(y,q))-int(legal(x,q)) for q in affected[p]);activity+=(x^y).bit_count()
  need(current==counts[t],'every NF cache');total+=current;x=y
 need(total==meta['total_nf'],'total NF')
 # Independent full recount at endpoint/midpoint, not only inductive cache.
 for t in [0,len(states)//2,len(states)-1]:need(nf(states[t])==counts[t],'literal NF recount')
 mid=states[len(states)//2];S=[]
 for h in [1,2]:
  amps=[]
  for a in range(3):
   for b in range(3):
    if a==b:continue
    z=0j
    for r in vertices:
     e=3*idx[r]+b;z+=(-1)**sum(r)*(2*(mid>>e&1)-1)*cmath.exp(2j*math.pi*h*r[a]/8)
    amps.append(z/(2*math.sqrt(512)))
  S.append(sum(z.real*z.real+z.imag*z.imag for z in amps))
 measured=dict(mid_nf=counts[len(states)//2],endpoint_nf=(counts[0]+counts[-1])/2,average_nf=total/len(states),endpoint_overlap=1-2*(states[0]^states[-1]).bit_count()/1536,temporal_activity=activity/(1536*110592),S=S,total_nf=total)
 old=report['cases'][case]['measurements'][-1]
 for k,v in measured.items():
  if k=='S':need(all(abs(a-b)<1e-11 for a,b in zip(v,old[k])),'Fourier measurement')
  else:need(v==old[k],'measurement '+k)
 results.append(dict(case=case,witness_flips=len(wit),nonself_bonds=nonself,measurement=measured))
forecast=json.loads((O/'FORECAST.json').read_text());accounted=0
for row in report['cases']:
 accounted+=sum(row[k] for k in ['geometry_seconds','initializer_seconds','measurement_seconds','checkpoint_save_seconds','checkpoint_load_seconds'])+sum(b['seconds'] for b in row['blocks'])
for i,row in enumerate(report['cases']):
 maximum=max(x['seconds'] for x in row['blocks']);setup=sum(row[k] for k in ['geometry_seconds','initializer_seconds','checkpoint_save_seconds','checkpoint_load_seconds']);f=16*(setup+16*(1536*maximum+row['measurement_seconds']/4))+16*max(0,6.62-accounted)
 need(abs(f-forecast['cases'][i]['hypothetical_16chain_16sweep_seconds'])<1e-8,'independent forecast arithmetic')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);need(rss<384 and time.monotonic()-start<180,'review resources')
r=dict(checks=count,seconds=time.monotonic()-start,rss_mib=rss,cases=results,charged_profile_seconds=6.62,outer_peak_bytes=174505984,outer_peak_mib=174505984/1048576,scope='Read-only checkpoint replay and final-measurement/forecast verification, no profile rerun or new sampling.')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='cases'}))
