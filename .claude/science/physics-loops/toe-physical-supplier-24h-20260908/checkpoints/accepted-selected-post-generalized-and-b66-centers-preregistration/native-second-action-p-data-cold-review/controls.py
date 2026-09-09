from pathlib import Path
from fractions import Fraction as F
import json
p=Path('/private/tmp/toe-24h-probes-20260908/native-second-action-p-data-append-design');c={};exec(compile((p/'core.py').read_bytes(),str(p/'core.py'),'exec'),c)
n=0
# Independent opposite-axis matrix, not core.form.
O=[[int(i//2==j//2 and i!=j)for j in range(6)]for i in range(6)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def opposite(a,b):return sum(a[i]*O[i][j]*b[j]for i in range(6)for j in range(6))
def contains(b,x):return F(b[0],c['S'])<=x<=F(b[1],c['S'])
for a,b in c['PAIRS']:
 ds=[[F((1 if i%2==0 else -1)*(i+1 in z))for i in range(6)]for z in (a,b,range(1,7))]
 oi=c['PAIRS'].index((a,b));orbit=c['ORBITS'][oi];trace=0
 for i,u in enumerate(ds):
  for j,v in enumerate(ds):
   I=dot(u,v);opp=opposite(u,v)
   assert contains(c['selfpair'](i,j,orbit)[0],(6*I-opp)/4);n+=1
   assert contains(c['qpair'](i,j,F(7,3),F(31,2),orbit)[1],-F(7,3)*(I+opp)/4+F(31,2)*opp/24);n+=1
   assert contains(c['ward'](i,j,orbit)[0],-dot(u,ds[(2,0,1)[j]])/4);n+=1
  trace+=(6*dot(u,u)-opposite(u,u))/2
 assert trace in (33,34,35);n+=1
assert 5*(3*66*2+3*2+3)==2025 and 5*(3*396+18+6)==6060;n+=1
print(json.dumps({'independent_predicates':n,'native_calls':0,'stream_calls':0}))
