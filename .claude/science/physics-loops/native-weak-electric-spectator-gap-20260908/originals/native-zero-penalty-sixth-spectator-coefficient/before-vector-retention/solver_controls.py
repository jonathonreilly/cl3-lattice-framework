from pathlib import Path
from fractions import Fraction as F
import json,signal,time,hashlib
import solver_core as c
signal.alarm(180);start=time.monotonic();p=Path(__file__).resolve().parent;checks=0
def need(v,s):
 global checks
 checks+=1
 if not v:raise RuntimeError(s)
for n in range(-10,11):
 for den in (F(1),F(2),F(5,12),F(24),F(1728,5)):
  z,e=c.algebraic(n,den);lo=F.from_float(z)-F.from_float(e);hi=F.from_float(z)+F.from_float(e)
  if n>=0:need(hi>=0 and hi*hi*den>=n*n and (lo<=0 or lo*lo*den<=n*n),'exact sqrt enclosure')
  else:need(lo<=0 and lo*lo*den>=n*n and (hi>=0 or hi*hi*den<=n*n),'negative exact enclosure')
raw=json.loads((p/'PREFIXES.json').read_text());m=c.Model(raw);need(m.norms==[F(x) for x in json.loads((p/'FRAME_RESULT.json').read_text())['norms']],'exact frame predecessor')
A,err=m.matrix(0);expected=c.np.diag([m.omega*int(b).bit_count() for b in m.states]);need(c.np.max(c.np.sum(abs(A-expected),axis=1))<err,'base model with bound')
# Full literal JW verification of all100 basic cross-Majorana generators.
def maj(b,i,kind):
 s=(-1)**((b&((1<<i)-1)).bit_count())
 if kind:s*=1j*(1-2*((b>>i)&1))
 return b^(1<<i),s
idx={int(b):i for i,b in enumerate(m.states)}
for i in range(10):
 for j in range(10):
  M=c.np.zeros((10,10));M[i,j]=2;H,_=m.fock(M)
  for col,b in enumerate(m.states):
   q,z=maj(int(b),j,1);q,y=maj(q,i,0);value=1j*y*z
   need(H[idx[q],col]==value and c.np.count_nonzero(H[:,col])==1,'all literal Clifford columns')
# Existing independent exact inverse-trace fixtures only; no all-prefix scan.
a=Path('/private/tmp/toe-24h-probes-20260908/native-sixth-spectator-gap-certificates/RESULT.json');r=json.loads(a.read_text())
for x in r['rows']:
 mask=int(x['mask_hex'],16);g=m.gap(mask)
 if 'gap_lower' in x:need(F(m.gap_records[str(mask)]['gap'])==F(x['gap_lower']),'independent rational certificate equality')
 need(F.from_float(g)<=F(m.gap_records[str(mask)]['gap']),'downward conversion')
# Prefix metadata closure and all word support masks.
for row in raw['rows']:
 bridge=row['bridge_edge']
 for x in row['prefixes']:
  bd=int(x['boundary_used_mask']);bc=x['bridge_count'];mask=bd^((1<<bridge) if bc%2 else 0)
  need(mask==int(x['full_toggle_mask']) and bd.bit_count()+bc==2*x['k'],'prefix metadata')
print(json.dumps({'checks':checks,'PASS':True,'seconds':time.monotonic()-start,'scope':'deterministic coefficient enclosures, full JW matrix columns and five existing exact gap fixtures; no coefficient solve','solver_sha256':hashlib.sha256((p/'solver_core.py').read_bytes()).hexdigest()},indent=2))
