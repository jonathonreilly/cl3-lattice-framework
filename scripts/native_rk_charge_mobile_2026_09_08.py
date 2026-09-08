AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ()
import signal,time,resource,sys,json,hashlib
start=time.monotonic()
if __name__ == "__main__":signal.alarm(180)
from pathlib import Path
from itertools import combinations
checks={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise RuntimeError(k)
# All local source bit patterns, assuming neutral targets only for this capacity count.
local=[]
for bits in range(64):
 G=bits.bit_count()-3
 if abs(G)!=1:continue
 permitted=[j for j in range(6) if 1-2*((bits>>j)&1)==-G]
 ck('source_capacity_'+str(bits),len(permitted)==4);local.append(bits)
L=4;coords=[(v//16,v//4%4,v%4) for v in range(64)]
def vid(c):return 16*c[0]+4*c[1]+c[2]
# Actual directed positive-axis physical links, then native neighbor order by vertex label.
edges=[]
for v,c in enumerate(coords):
 for a in range(3):
  d=list(c);d[a]=(d[a]+1)%4;edges.append((v,vid(d)))
inc=[[] for _ in range(64)]
for e,(i,j) in enumerate(edges):inc[i].append((j,e));inc[j].append((i,e))
for z in inc:z.sort()
eps=[(-1)**sum(c) for c in coords]
def degrees(x):return [sum((x>>e)&1 for _,e in z) for z in inc]
def charges(x):return [eps[v]*(d-3) for v,d in enumerate(degrees(x))]
def transitions(x):
 deg=degrees(x);Q=[eps[i]*(z-3) for i,z in enumerate(deg)];ans=[]
 for e,(u,v) in enumerate(edges):
  i,j=sorted((u,v));bi=(-1)**deg[i];bj=(-1)**deg[j]
  if bi==bj:continue
  y=x^(1<<e);delta=1-2*((x>>e)&1)
  if abs(deg[i]+delta-3)>1 or abs(deg[j]+delta-3)>1:continue
  sign=1
  for a,b in [(i,j),(j,i)]:
   for nb,f in inc[a]:
    if nb<b and ((x>>f)&1):sign=-sign
  # Exact Gaussian-integer coefficient: amplitude = i * imag.
  imag=sign*(bi-bj)//2
  ans.append((y,e,imag))
 return ans
seed=sum((c[a]%2)<<(3*v+a) for v,c in enumerate(coords) for a in range(3));ck('ice_seed',charges(seed)==[0]*64);ck('ice_T_zero',transitions(seed)==[])
# Directed electric path (0,0,0)->(3,0,0)->(2,0,0), fixed before evaluation.
u=vid((0,0,0));v=vid((2,0,0));pair=seed^(1<<(3*vid((3,0,0))))^(1<<(3*vid((2,0,0))))
Q=charges(pair);ck('literal_pair_support',Q[u]==-1 and Q[v]==1 and sum(abs(x) for x in Q)==2);ck('row_capacity_attained',len(transitions(pair))==8)
visited={pair};front={pair};records=[]
for depth in range(3):
 nxt=set()
 for x in front:
  Q=charges(x);D=sum(z*z for z in Q);out=transitions(x)
  ck('row_bound_'+str(len(records)),len(out)<=4*D)
  for y,e,amp in out:
   q=charges(y);ck('support_'+str(len(records))+'_'+str(e),all(abs(z)<=1 for z in q) and sorted(q)==sorted(Q) and sum(q)==0)
   reverse=[a for z,f,a in transitions(y) if f==e and z==x];ck('native_phase_'+str(len(records))+'_'+str(e),abs(amp)==1 and reverse==[-amp])
   nxt.add(y)
  records.append({'depth':depth,'outdegree':len(out),'D':D})
 visited|=nxt;front=nxt-set(x for x in []) # deliberately bounded path-depth neighborhoods, duplicate tests disclosed
# Independent exact pairwise row-form inequality 2|uv|<=|u|²+|v|² is the only norm step; no finite neighborhood spectrum asserted.
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384:raise RuntimeError('resource')
print(json.dumps({'checks':checks,'count':len(checks),'source_patterns':len(local),'tested_rows_including_depth_repeats':len(records),'distinct_visited_configurations':len(visited),'initial_pair_outdegree':8,'max_outdegree':max(x['outdegree'] for x in records),'scope':'bounded actual L4 configuration neighborhoods, not a complete D2 sector or spectral saturation proof','seconds':time.monotonic()-start,'rss_mib':rss,'source_sha':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
