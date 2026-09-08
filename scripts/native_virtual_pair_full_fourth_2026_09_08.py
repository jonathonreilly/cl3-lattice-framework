"""Portable exact native mechanism controls; proof is separate."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/NATIVE_VIRTUAL_PAIR_RING_MECHANISM_NOTE_2026-09-08.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md')
import argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    import signal
    signal.alarm(AUDIT_TIMEOUT_SEC)
    parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args()
import itertools,json,time,signal,resource,sys,hashlib
from fractions import Fraction as F
from pathlib import Path
start=time.monotonic();checks=0
def req(v,msg):
 global checks
 checks+=1
 if not v:raise RuntimeError(msg)
vs=list(itertools.product(range(4),repeat=3));vi={v:i for i,v in enumerate(vs)};es=set()
for i,v in enumerate(vs):
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;es.add(tuple(sorted((i,vi[tuple(w)]))))
es=sorted(es);ei={e:k for k,e in enumerate(es)};inc=[sum(1<<e for e,ends in enumerate(es) if v in ends) for v in range(64)];masks=[]
for e,(i,j) in enumerate(es):
 mask=0
 for a,b in ((i,j),(j,i)):
  for f,(u,v) in enumerate(es):
   if a==u and v<b or a==v and u<b:mask^=1<<f
 masks.append(mask)
def degree(z):return [(z&row).bit_count() for row in inc]
def D(z):
 ds=degree(z)
 return sum((d-3)**2 for d in ds)
def apply(z,e,native=True):return z^(1<<e),(-1)**((z&masks[e]).bit_count()) if native else 1
def path(z,word,native=True,detail=False):
 amp=1;den=1;levels=[];states=[]
 for k,e in enumerate(word):
  z,phase=apply(z,e,native);amp*=phase;d=D(z);levels.append(d);states.append(format(z,'0192b'))
  if d is None:return F(0),levels,states,'low-refusal'
  if k<len(word)-1:
   if d==0:return F(0),levels,states,'reducible'
   den*=d
  elif d!=0:return F(0),levels,states,'nonice-end'
 return -F(amp,den),levels,states,'irreducible'
def edges(C):return [ei[tuple(sorted((a,b)))] for a,b in zip(C,C[1:]+C[:1])]
def Samp(z,C):
 amp=1
 for a,b in reversed(list(zip(C,C[1:]+C[:1]))):
  z,s=apply(z,ei[tuple(sorted((a,b)))]);amp*=s*(-1 if a>b else 1)
 return amp # i^4=1
faces=[]
for v in vs:
 for a,b in itertools.combinations(range(3),2):
  x=list(v);y=list(v);xy=list(v);x[a]=(x[a]+1)%4;y[b]=(y[b]+1)%4;xy[a]=(xy[a]+1)%4;xy[b]=(xy[b]+1)%4
  faces.append([vi[v],vi[tuple(x)],vi[tuple(xy)],vi[tuple(y)]])
seed=0
for e,(i,j) in enumerate(es):
 a=next(a for a in range(3) if vs[i][a]!=vs[j][a]);o=i if (vs[i][a]+1)%4==vs[j][a] else j;seed|=(vs[o][a]%2)<<e
req(D(seed)==0,'ice seed')
def alternating(z,C):
 bits=[z>>e&1 for e in edges(C)];return all(bits[k]!=bits[(k+1)%4] for k in range(4))
backgrounds=[seed];z=seed
for index in (0,17,41):
 C=next(C for C in faces[index:]+faces[:index] if alternating(z,C));z^=sum(1<<e for e in edges(C));req(D(z)==0,'ring-built ice background');backgrounds.append(z)
rows=[];example=None
for bi,z in enumerate(backgrounds):
 for ci,C in enumerate(faces):
  if not alternating(z,C):continue
  word=edges(C);native=F(0);bare=F(0);tapes=[];parts={2:F(0),4:F(0)}
  for order in itertools.permutations(word):
   a,ds,states,status=path(z,order);b,_,_,_=path(z,order,False);req(status=='irreducible','alternating support');req(ds in ([2,2,2,0],[2,4,2,0]),'D denominators');native+=a;bare+=b;parts[ds[1]]+=a
   if example is None:tapes.append(dict(order=order,D=ds,coefficient=str(a),states=states))
  eta=(-1)**sum(a>b for a,b in zip(C,C[1:]+C[:1]));ring=Samp(z,C)
  req(native==F(eta*ring,2),'native fourth ring coefficient');req(bare==F(-5,2),'bare X fourth coefficient');req(parts[2]==0 and parts[4]==native,'adjacent cancellation')
  rows.append(dict(background=bi,face=ci,eta=eta,S_amplitude=ring,native_coefficient=str(native),bare_coefficient=str(bare)))
  if example is None:example=dict(initial_bits=format(z,'0192b'),cycle=C,edges=word,tapes=tapes)
# Exact repeated-edge diagonal coefficients for all unordered physical edge pairs on one full ice background.
diagonal=[];types={};z=seed
for e,f in itertools.combinations(range(192),2):
 native=F(0);bare=F(0);statuses={}
 for word in sorted(set(itertools.permutations((e,e,f,f)))):
  a,ds,states,status=path(z,word);b,_,_,_=path(z,word,False);native+=a;bare+=b;statuses[status]=statuses.get(status,0)+1
 adjacent=bool(set(es[e])&set(es[f]));different=((z>>e)^(z>>f))&1
 folded=F(1,4)
 expected=F(1,4) if adjacent else F(0)
 req(native+folded==expected,'native diagonal folded coefficient')
 expectedX=(F(-1,4) if different else F(1,12)) if adjacent else F(0)
 req(bare+folded==expectedX,'bare diagonal coefficient')
 key=f'{adjacent}:{different}';types[key]=types.get(key,0)+1
 diagonal.append(dict(edges=(e,f),irreducible=str(native),folded=str(folded),native_total=str(native+folded),bare_total=str(bare+folded),statuses=statuses))
for e in range(192):
 a,ds,states,status=path(seed,(e,e,e,e));req(a==0 and status=='reducible','single-edge folded-only');req(path(seed,(e,e))[0]==F(-1,2),'second-order constant')
# Straight winding four-cycle is a distinct allowed length-four loop at extent4.
C=[vi[(a,0,0)] for a in range(4)];req(alternating(seed,C),'winding alternating');val=sum((path(seed,p)[0] for p in itertools.permutations(edges(C))),F(0));eta=(-1)**sum(a>b for a,b in zip(C,C[1:]+C[:1]));req(val==F(eta*Samp(seed,C),2) and eta==-1,'winding orientation')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(0<rss<384 and time.monotonic()-start<180,'resources')
out=dict(checks=checks,seconds=time.monotonic()-start,rss_MiB=rss,vertices=vs,edges=es,background_bits=[format(z,'0192b') for z in backgrounds],plaquette_rows=rows,example_all24=example,diagonal_pairs=diagonal,pair_types=types,winding=dict(cycle=C,eta=eta,coefficient=str(val)),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(out,indent=2))
