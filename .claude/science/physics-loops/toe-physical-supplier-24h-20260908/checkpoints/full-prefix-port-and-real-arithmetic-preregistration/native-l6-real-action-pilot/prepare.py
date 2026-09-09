from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib
P=Path(__file__).parent;source=P.parent/'native-l6-single-star-adapted-transports/ADAPTED.json';a=json.loads(source.read_text());D=1<<100

def coeff(value,norm):
 value=F(value);norm=F(norm)
 if not value:return None
 square=value*value/norm;n=isqrt((square.numerator*D*D)//square.denominator);lo=F(n,D);hi=F(n+1,D)
 if value<0:lo,hi=-hi,-lo
 candidate=float((lo+hi)/2)
 return {'value':str(value),'norm':str(norm),'lower':str(lo),'upper':str(hi),'candidate_hex':candidate.hex(),'candidate_radius':str(max(abs(F(candidate)-lo),abs(F(candidate)-hi)))}
center=[];neighbors={str(v):[] for v in a['neighbors']};frequencies=[];mode=0
for sec in a['sectors']:
 for row,norm in zip(sec['vectors'],sec['norms']):
  if not F(norm):continue
  # Canonical row K0v=-2 for all six center neighbors.
  kr0=sum(-2*F(row[v]) for v in a['neighbors']);z=coeff(kr0,F(sec['lam'])*F(norm))
  if z:center.append(dict(mode=mode,**z))
  for v in a['neighbors']:
   z=coeff(row[v],norm)
   if z:neighbors[str(v)].append(dict(mode=mode,**z))
  frequencies.append(coeff(sec['lam'],sec['lam']));mode+=1
if mode!=21 or [z['mode'] for z in center]!=[0,6,12,18]:raise ValueError('support')
if [len(neighbors[str(v)]) for v in a['neighbors']]!=[15,15,15,15,11,11]:raise ValueError('neighbor support')
(P/'COEFFICIENTS.json').write_text(json.dumps(dict(source_sha=hashlib.sha256(source.read_bytes()).hexdigest(),center=center,neighbors=neighbors,frequencies=frequencies,pairs=[[[36,-2],[6,-2]],[[36,-2],[180,-2]]]),indent=2)+'\n')
