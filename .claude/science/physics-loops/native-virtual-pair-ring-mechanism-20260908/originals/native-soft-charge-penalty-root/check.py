import itertools,json,time,signal,resource,sys
from fractions import Fraction as F
from pathlib import Path
signal.alarm(180);start=time.monotonic();count=0
def req(x,msg):
 global count
 count+=1
 if not x:raise RuntimeError(msg)
def coeff(ends,bits,native=True):
 k=len(ends);verts=sorted(set(sum((list(e) for e in ends),[])));states=[];energy={}
 for z in range(1<<k):
  delta={v:0 for v in verts}
  for e,(a,b) in enumerate(ends):
   if z>>e&1:
    delta[a]+=1-2*bits[e];delta[b]+=1-2*bits[e]
  states.append(z);energy[z]=sum(d*d for d in delta.values())
 req([z for z in states if energy[z]==0]==[0],'unique forest ice')
 # Local Pauli convention: later edge has Z on every earlier incident edge.
 masks=[sum(1<<f for f in range(e) if set(ends[e])&set(ends[f])) for e in range(k)]
 def mul(v):
  out={z:F(0) for z in states}
  for z,x in v.items():
   if not x:continue
   for e in range(k):
    zz=z^(1<<e)
    if zz in energy:out[zz]+=x*((-1)**((masks[e]&z).bit_count()) if native else 1)
  return out
 psi=[{z:F(int(z==0)) for z in states}];E=[F(0)]
 for n in range(1,7):
  v=mul(psi[n-1]);E.append(v[0]);out={0:F(0)}
  for z in states:
   if z:out[z]=(-v[z]+sum(E[j]*psi[n-j][z] for j in range(1,n)))/energy[z]
  psi.append(out)
 req(E[1]==E[3]==E[5]==0,'odd terms')
 return E
shapes={'one':[(0,1)],'pair':[(0,1),(1,2)],'disjoint':[(0,1),(2,3)],'star':[(0,1),(0,2),(0,3)],'path':[(0,1),(1,2),(2,3)],'pair_plus_disjoint':[(0,1),(1,2),(3,4)]}
rows=[];cache={}
for name,edges in shapes.items():
 for bits in itertools.product((0,1),repeat=len(edges)):
  E=coeff(edges,bits);cluster=E[6]
  # Inclusion-exclusion isolates terms using every supplied edge.
  connected=F(0)
  for mask in range(1,1<<len(edges)):
   subset=[e for e in range(len(edges)) if mask>>e&1]
   connected+=(-1)**(len(edges)-len(subset))*coeff([edges[e] for e in subset],[bits[e] for e in subset])[6]
  rows.append(dict(shape=name,bits=bits,E=[str(e) for e in E],all_edges_coefficient=str(connected)))
  cache[(name,bits)]=connected
for row in rows:
 if row['shape']=='path':
  b=row['bits'];D3=2+4*((b[0]==b[1])+(b[1]==b[2]));req(F(row['E'][6])==-(F(35)+F(2,D3))/32,'soft path E6');req(F(row['all_edges_coefficient'])==-(F(5)+F(2,D3))/32,'soft path connected')
 elif row['shape']=='one':req(F(row['all_edges_coefficient'])==F(-1,16),'one')
 elif row['shape'] in ('pair','star'):req(F(row['all_edges_coefficient'])==F(-3,8),'bright cluster')
 elif row['shape'] in ('disjoint','pair_plus_disjoint'):req(F(row['all_edges_coefficient'])==0,'tensor additivity')
weighted=9*F(2,2)+12*F(2,6)+4*F(2,10);per_vertex=-(F(3,16)+F(3*15,8)+F(3*20,8)+(5*75+3*weighted)/32);req(per_vertex==F(-1053,40),'uniform full coefficient')
out=dict(PASS=True,checks=count,rows=rows,weighted_path_sum_per_middle=str(weighted),sixth_diagonal_per_vertex=str(per_vertex),seconds=time.monotonic()-start,rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024),scope='Exact full-carrier forest energy recursion, derived from preserved hard helper by removing support refusal; not independent of that original recursion.')
print(json.dumps(out,indent=2))
