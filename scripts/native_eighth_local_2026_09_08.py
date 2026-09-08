"""Portable exact H8 control, adapted from preserved research source."""
AUDIT_TIMEOUT_SEC=180
import argparse, signal
if __name__=='__main__':
 signal.alarm(AUDIT_TIMEOUT_SEC)
 parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args()
from fractions import Fraction as F
from itertools import product
import json,time,signal,resource,sys
from pathlib import Path
start=time.monotonic();checks=0
cache={}
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
def setup(edges,bits,native=True):
 size=1<<len(edges);verts=set(v for e in edges for v in e)
 energy=[]
 for z in range(size):
  delta={v:0 for v in verts}
  for e,ends in enumerate(edges):
   if z>>e&1:
    for v in ends:delta[v]+=1-2*bits[e]
  energy.append(sum(x*x for x in delta.values()))
 masks=[sum(1<<f for f in range(e) if set(edges[e])&set(edges[f])) for e in range(len(edges))]
 hops=[[(z^(1<<e),(-1)**((masks[e]&z).bit_count()) if native else 1) for e in range(len(edges))] for z in range(size)]
 return energy,hops

def scalar(en,hops,fold=True):
 req(en.count(0)==1,'scalar rank one')
 psi=[[F(int(z==0)) for z in range(len(en))]];E=[F(0)]
 for n in range(1,9):
  v=[F(0)]*len(en)
  for z,x in enumerate(psi[-1]):
   for y,s in hops[z]:v[y]+=s*x
  E.append(v[0]);p=[F(0)]*len(en)
  for z in range(1,len(en)):
   p[z]=(-v[z]+(sum(E[j]*psi[n-j][z] for j in range(1,n)) if fold else 0))/en[z]
  psi.append(p)
 return E

def contour(en,hops,k):
 # Laurent series: q zero-energy denominators and nonnegative degree d.
 total=F(0)
 for initial in range(len(en)):
  dp={(initial,0,0):F(1)}
  for step in range(k):
   nxt={}
   for (z,q,d),v in dp.items():
    if not en[z]:factors=[(q+1,d,F(1))]
    else:factors=[(q,d+j,-F(1,en[z]**(j+1))) for j in range(k-d)]
    for qq,dd,c in factors:
     # Maximum final zero count must exceed Taylor degree.
     if dd>=qq+k-step-1:continue
     for y,s in hops[z]:
      key=(y,qq,dd);nxt[key]=nxt.get(key,F(0))+v*c*s
   dp={key:v for key,v in nxt.items() if v}
  total+=sum(v for (z,q,d),v in dp.items() if z==initial and d==q-1)
 return total/k

def coeff(edges,bits):
 key=(tuple(edges),tuple(bits))
 if key in cache:return cache[key]
 en,hops=setup(edges,bits);rank=en.count(0)
 if rank==1:E=scalar(en,hops)
 else:
  req(rank==2 and len(edges)==4,'only alternating cycle rank two')
  # Product of all active Pauli A generators; map acts by full toggle.
  def S(z):
   amp=1
   for e in range(4):
    y,s=hops[z][e];z=y;amp*=s
   return z,amp
  for z in range(16):
   zz,ss=S(z);req(en[z]==en[zz],'cycle preserves D')
   for e in range(4):
    y,a=hops[z][e];y1,b=S(y);z1,c=S(z);y2,d=hops[z1][e]
    req(y1==y2 and a*b==c*d,'cycle commutes native A')
  E=[F(0)]+[contour(en,hops,n)/rank if n%2==0 else F(0) for n in range(1,9)]
 cache[key]=E;return E
shapes={'one':[(0,1)],'pair':[(0,1),(1,2)],'star3':[(0,1),(0,2),(0,3)],'path3':[(0,1),(1,2),(2,3)],'star4':[(0,1),(0,2),(0,3),(0,4)],'path4':[(0,1),(1,2),(2,3),(3,4)],'fork4':[(0,1),(0,2),(0,3),(3,4)],'cycle4':[(0,1),(1,2),(2,3),(3,0)],'disjoint':[(0,1),(2,3)]}
# Formula controls before tables.
for name in ['one','pair','star3']:
 for bits in product((0,1),repeat=len(shapes[name])):
  en,hops=setup(shapes[name],bits);E=scalar(en,hops)
  for n in [2,4,6,8]:req(contour(en,hops,n)==E[n],'contour versus energy feedback '+name)
req(coeff(shapes['one'],(0,))[8]==F(5,128),'single-edge exact sqrt coefficient')
rows=[]
for name,edges in shapes.items():
 for bits in product((0,1),repeat=len(edges)):
  E=coeff(edges,bits);connected=F(0)
  for mask in range(1,1<<len(edges)):
   ids=[e for e in range(len(edges)) if mask>>e&1]
   connected+=(-1)**(len(edges)-len(ids))*coeff([edges[e] for e in ids],[bits[e] for e in ids])[8]
  rows.append(dict(shape=name,bits=bits,rank=setup(edges,bits)[0].count(0),E=[str(v) for v in E],connected8=str(connected)))
  req(E[1]==E[3]==E[5]==E[7]==0,'odd forest/trace terms')
  if name=='disjoint':req(connected==0,'disconnected additivity')
en,h=setup(shapes['one'],(0,));req(scalar(en,h,False)[8]!=scalar(en,h)[8],'missing folds changes result')
en,h=setup(shapes['cycle4'],(0,1,0,1));good=contour(en,h,8)/2
req(contour(en,h,8)!=good,'wrong rank changes cycle value')
en,hx=setup(shapes['cycle4'],(0,1,0,1),False);req(contour(en,hx,8)/2!=good,'bare X changes actual cycle value')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(rss<384 and time.monotonic()-start<180,'resources')
r=dict(checks=checks,rows=rows,seconds=time.monotonic()-start,rss_mib=rss,scope='Full-carrier local degree-eight tables. Global motif reduction not established.')
(Path(__file__).resolve().parents[1]/'outputs/native_eighth_local_2026_09_08.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='rows'}))
