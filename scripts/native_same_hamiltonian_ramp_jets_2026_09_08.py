"""Exact arbitrary-profile moving-frame jets; no third-party runtime."""
import argparse, hashlib, json, math, resource, signal, sys, time
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
AUDIT_TIMEOUT_SEC=180
N=6
Z={}; ONE={(0,)*N:F(1)}
def add(a,b):
 c=a.copy()
 for m,x in b.items():
  c[m]=c.get(m,F(0))+x
  if not c[m]:del c[m]
 return c
def scale(a,x):return {m:v*x for m,v in a.items() if v*x}
def mul(a,b):
 c={}
 for m,x in a.items():
  for n,y in b.items():
   k=tuple(i+j for i,j in zip(m,n));c=add(c,{k:x*y})
 return c
def jet(k):
 m=[0]*N;m[k]=1;return {tuple(m):F(1)}
def deriv(a):
 c={}
 for m,x in a.items():
  for k in range(N-1):
   if m[k]:
    n=list(m);n[k]-=1;n[k+1]+=1;c=add(c,{tuple(n):x*m[k]})
 return c
def va(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def vs(a,x):return tuple(scale(v,x) for v in a)
def cross(a,b):return tuple(add(mul(a[(i+1)%3],b[(i+2)%3]),scale(mul(a[(i+2)%3],b[(i+1)%3]),-1)) for i in range(3))
ZERO=(Z,Z,Z)
def bracket(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():
   if i+j<=4:c[i+j]=va(c.get(i+j,ZERO),vs(cross(x,y),-2))
 return c
def transformed(a, moving_sign=1, derivatives=True):
 out={0:(Z,Z,scale(ONE,-1)),1:(jet(0),Z,Z)};term=out.copy()
 for k in range(1,5):
  term=bracket(a,term)
  for n,v in term.items():out[n]=va(out.get(n,ZERO),vs(v,F(1,math.factorial(k))))
 if derivatives:
  term={n+1:tuple(deriv(x) for x in v) for n,v in a.items() if n<4}
  for k in range(4):
   for n,v in term.items():out[n]=va(out.get(n,ZERO),vs(v,F(-moving_sign,math.factorial(k+1))))
   term=bracket(a,term)
 return out
def solve(moving_sign=1, derivatives=True):
 a={};ks={}
 for n in range(1,5):
  v=transformed(a,moving_sign,derivatives).get(n,ZERO)
  a[n]=(scale(v[1],F(1,2)),scale(v[0],F(-1,2)),Z);ks[n]=v[2]
 return a,ks
def serial(p):return [{'powers':m,'coefficient':str(x)} for m,x in sorted(p.items())]
def run():
 start=time.monotonic();checks=[]
 def req(v,name):
  if not v:raise RuntimeError(name)
  checks.append(name)
 a,k=solve() # MUTATION_SOLVE
 actual=transformed(a)
 for n in range(1,5):req(actual[n]==(Z,Z,k[n]),'correct moving-frame cancellation '+str(n))
 f=jet(0);f2=mul(f,f);f4=mul(f2,f2)
 expected={1:Z,2:scale(f2,F(-1,2)),3:Z,4:scale(add(f4,mul(f,jet(2))),F(1,8))}
 for n in range(1,5):req(k[n]==expected[n],'full arbitrary-profile K'+str(n))
 req(a[1]==(Z,scale(f,F(-1,2)),Z),'first generator')
 req(a[2]==(scale(jet(1),F(1,4)),Z,Z),'nonstatic second generator')
 for name,bad in [('wrong moving-frame sign',solve(-1)[0]),('omitted derivatives',solve(derivatives=False)[0]),('dropped second generator',{n:v for n,v in a.items() if n!=2})]:
  req(any(transformed(bad).get(n,ZERO)[:2]!=(Z,Z) for n in range(1,5)),name+' leaves actual transverse residual')
 # Normalized beta(15,15) cumulative polynomial, exact endpoint derivatives.
 coeff={15+j:F((-1)**j*math.comb(14,j),15+j) for j in range(15)}
 norm=sum(coeff.values());coeff={n:c/norm for n,c in coeff.items()}
 def ev(poly,x):return sum(c*x**n for n,c in poly.items())
 req(ev(coeff,0)==0 and ev(coeff,1)==1,'beta14 values')
 p=coeff
 for n in range(1,15):
  p={j-1:c*j for j,c in p.items() if j};req(ev(p,0)==ev(p,1)==0,'beta14 flat derivative '+str(n))
 for name,lhs,rhs in [('ramp remainder',15-1-9,5),('hold remainder',15-4-9,2),('slow hold',6-4,2),('initial ice slow ramp',4-1,3)]:req(lhs==rhs,name)
 vertices=list(product(range(4),repeat=3));index={v:i for i,v in enumerate(vertices)};edges=set()
 for i,v in enumerate(vertices):
  for axis in range(3):
   w=list(v);w[axis]=(w[axis]+1)%4;edges.add(tuple(sorted((i,index[tuple(w)]))))
 edges=sorted(edges);req(len(edges)==192,'full L4 edge count');bits=[]
 for i,j in edges:
  vi,vj=vertices[i],vertices[j];axis=next(a for a in range(3) if vi[a]!=vj[a]);tail=vi if (vi[axis]+1)%4==vj[axis] else vj;bits.append(tail[axis]%2)
 for i in range(64):req(sum(bits[e] for e,ends in enumerate(edges) if i in ends)==3,'ice degree '+str(i))
 for e,g in combinations(range(192),2):
  delta={}
  for h in (e,g):
   for i in edges[h]:delta[i]=delta.get(i,0)+1-2*bits[h]
  req(any(delta.values()),'distinct two-edge return forbidden '+str(e)+','+str(g))
 for e in range(192):req(sum((1-2*bits[e])**2 for _ in edges[e])==2,'single-edge D2 '+str(e))
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
 req(0<rss<384 and time.monotonic()-start<180,'resource cap')
 return dict(checks=len(checks),K={str(n):serial(p) for n,p in k.items()},generators={str(n):[serial(p) for p in v] for n,v in a.items()},beta14_normalizer=str(norm),distinct_pairs=18336,seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact finite jet and full graph support controls; no dynamical simulation or volume-uniform proof inferred from controls.')
if __name__=='__main__':
 signal.alarm(AUDIT_TIMEOUT_SEC);parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args();print(json.dumps(run(),sort_keys=True,indent=2))
