from pathlib import Path
from fractions import Fraction as F
import types,json
p=Path('/private/tmp/toe-24h-probes-20260908/native-coarse-witness-continuation-root-review/schema.py');m=types.ModuleType('schema');exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
pairs=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)));n=0
for ci in range(10):
 L=[[F(((i+j)%3)-1,8)if j<3 else F(0)for j in range(48)]for i in range(7)]
 local=[[(x,x)for x in r]for r in L];zero=[[(F(0),F(0))for _ in range(7)]for _ in range(7)];out=m.assemble(local,zero,zero,(F(1,4),F(1,4)),ci)
 H=[[F(0)for _ in range(7)]for _ in range(7)]
 for j in pairs[ci//2][ci%2]:H[0][j]=F((-1)**(j+1),32);H[j][0]=-H[0][j]
 for i in range(7):
  for j in range(7):
   expected=H[i][j]-sum(H[i][k]*sum(L[k][a]*L[j][a]for a in range(48))for k in range(7));assert out[i][j]==(expected,expected);n+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','nonzero_local_final_assembly_entries':n,'native_prefix_values':0}))
