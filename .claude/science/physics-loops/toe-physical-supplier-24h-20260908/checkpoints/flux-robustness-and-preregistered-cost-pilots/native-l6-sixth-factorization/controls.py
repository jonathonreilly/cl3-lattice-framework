from itertools import product,permutations
from fractions import Fraction as F
import json,time
start=time.monotonic();vs=list(product(range(6),repeat=3));ids={v:i for i,v in enumerate(vs)};K=[{} for v in vs];edges=[]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;i,j=sorted((ids[v],ids[tuple(w)]));z=-2*(-1)**sum(v[:a]);K[i][j]=z;K[j][i]=-z;edges.append((i,j))
i=0;j=ids[(1,0,0)];cube=sum(a*b*K[k].get(j,0) for l,a in K[i].items() for k,b in K[l].items())
if cube!=-28*K[i][j]:raise ValueError('actual K cubic')
zero_matrix_entry=F(cube+12*K[i][j],16)
sign_matrix_entry=F(-cube-30*K[i][j],2)
if zero_matrix_entry!=2 or sign_matrix_entry!=2:raise ValueError('same positive adjacent coefficient')
v=0;w=ids[(3,0,0)];sv=[e for e,ab in enumerate(edges) if v in ab];sw=[e for e,ab in enumerate(edges) if w in ab]
if set(sv)&set(sw) or len(sv)!=6 or len(sw)!=6:raise ValueError('two disjoint stars')
pairs=[tuple(sv[k:k+2]) for k in (0,2,4)]+[tuple(sw[k:k+2]) for k in (0,2,4)];starv=sum(1<<e for e in sv);starw=sum(1<<e for e in sw);count=0;nonstar=0
for order in permutations(range(6)):
 mask=0
 for k in order[:3]:
  for e in pairs[k]:mask^=1<<e
 if mask in (starv,starw):count+=1
 else:nonstar+=1
if (count,nonstar)!=(72,648):raise ValueError('shuffle accounting')
# Exact polynomial arithmetic in x=u², truncated above x³.
def add(a,b):return [a[i]+b[i] for i in range(4)]
def scale(a,c):return [c*x for x in a]
def mul(a,b):return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(4)]
one=[F(1),F(0),F(0),F(0)];x=[F(0),F(1),F(0),F(0)]
for s in (F(0),F(1),F(7,3)):
 E=[F(0),F(-1),F(0),1-s];d0=one;d1=scale(E,-1);factor=add(one,scale(E,-1));d2=add(mul(factor,d1),scale(x,-1));d3=add(mul(factor,d2),scale(mul(x,d1),-1));d4=add(mul(factor,d3),scale(mul(x,d2),-s))
 if any(d4):raise ValueError('ladder coefficient identity')
print(json.dumps({'canonical_adjacent_K':K[i][j],'canonical_adjacent_K_cubed':cube,'two_test_skew_entries':[str(zero_matrix_entry),str(sign_matrix_entry)],'midpoint_singleton_orders':count,'midpoint_nonstar_orders':nonstar,'formal_ladder_controls':3,'seconds':time.monotonic()-start,'scope':'structural exact controls only; no native sixth coefficient or integration'},indent=2))
