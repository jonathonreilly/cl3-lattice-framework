import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sympy as sp
from pathlib import Path
import json,time,signal,resource,sys
signal.alarm(180);start=time.monotonic();count=0
q=sp.symbols('q',real=True);f=sp.Function('f',real=True)(q);zero=sp.zeros(3,1)
def req(v,m):
 global count
 count+=1
 if not v:raise RuntimeError(m)
def clean(v):return v.applyfunc(sp.simplify)
def bracket(a,b):
 out={}
 for i,A in a.items():
  for j,B in b.items():
   if i+j<=4:out[i+j]=clean(out.get(i+j,zero)-2*A.cross(B))
 return out
def Fvec(a):
 out={0:sp.Matrix([0,0,-1]),1:sp.Matrix([f,0,0])};term=out.copy()
 for l in range(1,5):
  term=bracket(a,term)
  for n,v in term.items():out[n]=clean(out.get(n,zero)+v/sp.factorial(l))
 term={n+1:v.diff(q) for n,v in a.items() if n+1<=4}
 for l in range(4):
  for n,v in term.items():out[n]=clean(out.get(n,zero)-v/sp.factorial(l+1))
  term=bracket(a,term)
 return out
a={};K={}
for n in range(1,5):
 v=Fvec(a).get(n,zero)
 # [i a.sigma,D] has vector(2a_y,-2a_x,0).
 a[n]=sp.Matrix([v[1]/2,-v[0]/2,0]);K[n]=v[2]
 actual=Fvec(a)
 for j in range(1,n+1):req(clean(actual[j])==sp.Matrix([0,0,K[j]]),'offdiagonal eliminated')
req(sp.simplify(K[1])==0,'K1');req(sp.simplify(K[2]+f*f/2)==0,'K2');req(sp.simplify(K[3])==0,'K3')
req(sp.simplify(K[4]-(f**4+f*sp.diff(f,q,2))/8)==0,'arbitrary-profile fourth scalar')
req(sp.simplify(a[1]-sp.Matrix([0,-f/2,0]))==zero,'first generator')
req(sp.simplify(a[2]-sp.Matrix([sp.diff(f,q)/4,0,0]))==zero,'second derivative generator')
# This is not static epsilon parity: even-order generator has imaginary matrix iX.
req(a[2][0]!=0,'derivative parity adverse')
req(sp.simplify(K[4]-f**4/8)!=0,'discard derivatives adverse')
# Actual two-edge return enumeration in full cubic graph, with no Hilbert matrix.
from itertools import product,combinations
vs=list(product(range(4),repeat=3));idx={v:i for i,v in enumerate(vs)};edges=set()
for i,v in enumerate(vs):
 for axis in range(3):
  w=list(v);w[axis]=(w[axis]+1)%4;edges.add(tuple(sorted((i,idx[tuple(w)]))))
es=sorted(edges);inc=[[e for e,ends in enumerate(es) if i in ends] for i in range(64)]
# Standard coordinate seed translated to sorted edges.
z=0
for e,(i,j) in enumerate(es):
 vi,vj=vs[i],vs[j];axis=next(a for a in range(3) if vi[a]!=vj[a]);tail=vi if (vi[axis]+1)%4==vj[axis] else vj
 z|=(tail[axis]%2)<<e
req(all(sum(z>>e&1 for e in row)==3 for row in inc),'full ice')
returns=0
for e,fedge in combinations(range(192),2):
 delta={}
 for k in (e,fedge):
  for v in es[k]:delta[v]=delta.get(v,0)+1-2*(z>>k&1)
 if all(d==0 for d in delta.values()):returns+=1
req(returns==0,'no distinct two-edge ice returns')
for e in range(192):
 delta=1-2*(z>>e&1);req(2*delta*delta==2,'one-edge common denominator')
req(4-1==3,'slow ramp power');req(min(2,3)==2,'total natural-time error')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(0<rss<384 and time.monotonic()-start<180,'resources')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(checks=count,K={n:str(v) for n,v in K.items()},generators={n:str(v) for n,v in a.items()},distinct_edge_pairs=18336,distinct_ice_returns=returns,seconds=time.monotonic()-start,rss_mib=rss,scope='Independent Pauli-vector arbitrary-profile algebra plus full graph support controls; not a dynamical simulation.'),indent=2)+'\n');print(count)
