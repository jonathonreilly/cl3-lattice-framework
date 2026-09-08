"""Portable exact sixth-order control; original source preserved in packet."""
AUDIT_TIMEOUT_SEC=180
import argparse,signal
if __name__=='__main__':
 signal.alarm(AUDIT_TIMEOUT_SEC)
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');p.parse_args()
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json,time,signal,resource,sys
start=time.monotonic();checks=0
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
def zero(r,c):return [[F(0) for _ in range(c)] for _ in range(r)]
def plus(a,b):return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def scale(a,s):return [[s*x for x in row] for row in a]
def mm(a,b):
 out=zero(len(a),len(b[0]))
 for i,row in enumerate(a):
  for k,x in enumerate(row):
   if x:
    for j,y in enumerate(b[k]):
     if y:out[i][j]+=x*y
 return out
def tr(a):return [list(x) for x in zip(*a)]
def setup(edges,bits):
 en=[];v=zero(1<<len(edges),1<<len(edges));verts=set(x for e in edges for x in e)
 masks=[sum(1<<f for f in range(e) if set(edges[e])&set(edges[f])) for e in range(len(edges))]
 for z in range(len(v)):
  delta={x:0 for x in verts}
  for e,ends in enumerate(edges):
   if z>>e&1:
    for x in ends:delta[x]+=1-2*bits[e]
  en.append(sum(x*x for x in delta.values()))
  for e,mask in enumerate(masks):v[z^(1<<e)][z]=F((-1)**((mask&z).bit_count()))
 return en,v

def canonical(edges,bits):
 en,v=setup(edges,bits);p=[z for z,d in enumerate(en) if d==0];q=[z for z,d in enumerate(en) if d];r=len(p);nq=len(q)
 req(r==2,'rank-two alternating cycle')
 B=[[v[x][y] for y in p] for x in q];C=tr(B);A=[[v[x][y] for y in q] for x in q]
 chi={};HB={}
 for n in range(1,6):
  rhs=B if n==1 else mm(A,chi[n-1])
  for a in range(1,n-1):
   b=n-1-a
   if b>=1:rhs=plus(rhs,scale(mm(mm(chi[a],C),chi[b]),-1))
  chi[n]=[[-x/en[q[i]] for x in row] for i,row in enumerate(rhs)];HB[n+1]=mm(C,chi[n])
  # Actual graph-invariance coefficient, separate sign arrangement.
  residual=[[en[q[i]]*x for x in row] for i,row in enumerate(chi[n])]
  residual=plus(residual,B if n==1 else mm(A,chi[n-1]))
  for a in range(1,n-1):
   b=n-1-a
   if b>=1:residual=plus(residual,scale(mm(mm(chi[a],C),chi[b]),-1))
  req(residual==zero(nq,r),'wave graph equation '+str(n))
 I=[[F(i==j) for j in range(r)] for i in range(r)]
 M={}
 for a in chi:
  for b in chi:
   if a+b<=6:M[a+b]=plus(M.get(a+b,zero(r,r)),mm(tr(chi[a]),chi[b]))
 def conv(a,b):
  out={}
  for i,x in a.items():
   for j,y in b.items():
    if i+j<=6:out[i+j]=plus(out.get(i+j,zero(r,r)),mm(x,y))
  return out
 def power(alpha):
  out={0:I};term={0:I};coef=F(1)
  for j in range(1,4):
   coef*=F(alpha-j+1,j);term=conv(term,M)
   for n,x in term.items():out[n]=plus(out.get(n,zero(r,r)),scale(x,coef))
  return out
 left,right=power(F(1,2)),power(F(-1,2));he=conv(conv(left,HB),right)
 for n,x in he.items():req(x==tr(x),'canonical Hermitian '+str(n))
 inv=conv(left,right)
 for n,x in inv.items():req(x==(I if n==0 else zero(r,r)),'metric inverse '+str(n))
 return he,HB
c4=[(0,1),(1,2),(2,3),(3,0)]
rows=[]
for spoke in [False,True]:
 for bit in ([0,1] if spoke else [0]):
  edges=c4+([(0,4)] if spoke else []);bits=[0,1,0,1]+([bit] if spoke else [])
  he,hb=canonical(edges,bits)
  rows.append(dict(spoke=spoke,bit=bit,H={str(n):[[str(x) for x in row] for row in m] for n,m in he.items()},bloch6=[[str(x) for x in row] for row in hb[6]]))
# Six-cycle all720 orderings, actual signs and full energies; ordered A product convention explicit.
c6=[(i,(i+1)%6) for i in range(6)];en,v=setup(c6,[0,1,0,1,0,1]);total=F(0);values={}
for order in permutations(range(6)):
 z=0;amp=F(1)
 for j,e in enumerate(order):
  y=z^(1<<e);amp*=v[y][z];z=y
  if j<5:
   req(en[z]>0,'proper cycle subset outside ice');amp/=-en[z]
 total+=amp;values[str(amp)]=values.get(str(amp),0)+1
req(z==63,'six final toggle')
ordered=F(1);z=0
for e in range(6):y=z^(1<<e);ordered*=v[y][z];z=y
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(rss<384 and time.monotonic()-start<180,'resources')
out=dict(checks=checks,rows=rows,six_cycle_amplitude=str(total),ordered_product_amplitude=str(ordered),ratio_to_ordered_product=str(total/ordered),permutation_weights=values,seconds=time.monotonic()-start,rss_mib=rss)
(Path(__file__).resolve().parents[1]/'outputs/native_sixth_coefficients_2026_09_08.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
