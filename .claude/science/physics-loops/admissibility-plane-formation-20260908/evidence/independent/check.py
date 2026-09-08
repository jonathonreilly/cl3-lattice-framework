from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json,hashlib,time
from pathlib import Path
start=time.monotonic();checks={}
def kernels(p,q,r):
 Z=p+q+4*r;K=[[F(p if i==j else q if i//2==j//2 else r,Z) for j in range(6)] for i in range(6)];H=[[sum(K[i][k]*K[k][j] for k in range(6)) for j in range(6)] for i in range(6)];return K,H
def law(x,h,w,K,H):
 z=F(1,6)
 for i in range(h):
  for j in range(w):
   s=x[i*w+j]
   if i:z*=K[x[(i-1)*w+j]][s]
   if j:z*=K[x[i*w+j-1]][s]
   if i and j:z/=H[x[i*w+j-1]][x[(i-1)*w+j]]
 return z
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise RuntimeError(k)
K,H=kernels(3,1,2);mu={x:law(x,2,3,K,H) for x in product(range(6),repeat=6)};ck('full_2x3_normalization',sum(mu.values())==1)
for name,inds,h,w in [('left',[0,1,3,4],2,2),('right',[1,2,4,5],2,2),('top',[0,1,2],1,3),('bottom',[3,4,5],1,3)]:
 m=defaultdict(F)
 for x,z in mu.items():m[tuple(x[i] for i in inds)]+=z
 ck('translated_'+name,all(z==law(x,h,w,K,H) for x,z in m.items()))
ck('opposite_corner_all_46656',all(z==mu[tuple(reversed(x))] for x,z in mu.items()))
mirror=sum(z!=mu[(x[2],x[1],x[0],x[5],x[4],x[3])] for x,z in mu.items());ck('two_corner_classes',mirror==32616)
records=[]
for triple in [(3,1,2),(5,2,4),(2,2,1),(2,2,2)]:
 K,H=kernels(*triple)
 for c in range(6):
  vals=[]
  for s in range(6):
   x=[c]*9;x[4]=s;vals.append(law(x,3,3,K,H))
  actual=[v/sum(vals) for v in vals];v=[K[s][c]**4/H[s][c]**2 for s in range(6)];expanded=[z/sum(v) for z in v];v=[K[s][c]**4 for s in range(6)];static=[z/sum(v) for z in v]
  ck('six_neighbor_'+str(triple)+str(c),actual==expanded)
  ck('static_equal_iff_constant_'+str(triple)+str(c),(actual==static)==(len(set(triple))==1))
  if c==0:records.append({'triple':triple,'expanded':[str(v) for v in actual],'static':[str(v) for v in static]})
 # Nonuniform boundaries check denominator locations independently against causal formula.
 for t in range(12):
  x=[(i*i+t*i+t)%6 for i in range(9)];a=[]
  for s in range(6):x[4]=s;a.append(law(x,3,3,K,H))
  e=[K[s][x[1]]*K[s][x[3]]*K[s][x[5]]*K[s][x[7]]/(H[s][x[2]]*H[s][x[6]]) for s in range(6)]
  ck('nonuniform_boundary_'+str(triple)+str(t),[v/sum(a) for v in a]==[v/sum(e) for v in e])
print(json.dumps({'checks':checks,'count':len(checks),'complete_2x3_configurations':len(mu),'mirror_differences':mirror,'all_c_conditionals':records,'seconds':time.monotonic()-start,'source_sha':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
