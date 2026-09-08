import itertools,json,hashlib,time
from fractions import Fraction as F
from pathlib import Path
start=time.monotonic();O=Path(__file__).parent
# Actual native local Pauli strings for ascending edges on square 0-1-2-3-0.
edges=[(0,1),(1,2),(2,3),(0,3)]
masks=[]
for e,(i,j) in enumerate(edges):
 mask=0
 for a,b in ((i,j),(j,i)):
  for f,(u,v) in enumerate(edges):
   if a in (u,v) and (v if u==a else u)<b:mask^=1<<f
 masks.append(mask)
def apply(z,e):return z^(1<<e),(-1)**((z&masks[e]).bit_count())
def d(z,seed):
 deg=[sum(z>>e&1 for e,x in enumerate(edges) if v in x) for v in range(4)]
 old=[sum(seed>>e&1 for e,x in enumerate(edges) if v in x) for v in range(4)]
 q=[a-b for a,b in zip(deg,old)]
 return None if max(map(abs,q))>1 else sum(x*x for x in q)
rows=[]
for seed in (5,10):
 total=F(0)
 for word in itertools.permutations(range(4)):
  z=seed;phase=1;den=1;ds=[]
  for k,e in enumerate(word):
   z,s=apply(z,e);phase*=s
   if k<3:
    D=d(z,seed);assert D in (2,4);den*=D;ds.append(D)
  assert z==seed^15
  total-=F(phase,den);rows.append([seed,list(word),ds,phase])
 # S uses oriented final edge A30=-A03; operator acts rightmost first.
 z=seed;sphase=-1
 for e in (3,2,1,0):z,s=apply(z,e);sphase*=s
 # Ascending lambda product = minus oriented lambda product.
 assert total== -F(sphase,2)
# All diagonal words with two distinct edges. Native anticommutation if incident.
diag={}
for incident in (False,True):
 for equal in (False,True):
  total=F(0)
  for word in sorted(set(itertools.permutations((0,0,1,1)))):
   active=set();phase=1;den=1;valid=True
   for k,e in enumerate(word):
    # Clifford word reduction: moving current edge across current higher generators.
    if incident and e==0 and 1 in active:phase*=-1
    active.symmetric_difference_update({e})
    if k<3:
     if not active:valid=False;break
     if len(active)==2:
      if incident and equal:valid=False;break
      D=2 if incident else 4
     else:D=2
     den*=D
   if valid:total-=F(phase,den)
  folded=F(1,4)
  assert total+folded==(F(1,4) if incident else 0)
  diag[str((incident,equal))]={'irreducible':str(total),'folded':str(folded),'sum':str(total+folded)}
result={'PASS':True,'actual_native_square_columns':48,'rows':rows,'diagonal_cases':diag,'single_edge_fourth':'1/8','ascending_square_coefficient_relative_oriented_S':'-1/2','oriented_coupling_product_coefficient':'1/2','seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
