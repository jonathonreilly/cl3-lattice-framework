from fractions import Fraction as F
from math import isqrt,isfinite
import hashlib,json

def validate(coeff,adapted,adapted_sha):
 if coeff['source_sha']!=adapted_sha:raise ValueError('adapted source binding')
 if adapted['neighbors']!=[36,180,6,30,1,5]:raise ValueError('neighbor order')
 expected={'center':[],'neighbors':{str(v):[] for v in adapted['neighbors']},'frequencies':[]};mode=0;D=1<<100
 def row(value,norm):
  value=F(value);norm=F(norm)
  if norm<=0:raise ValueError('positive exact norm')
  if value==0:return None
  square=value*value/norm;n=isqrt(square.numerator*D*D//square.denominator);lo=F(n,D);hi=F(n+1,D)
  if value<0:lo,hi=-hi,-lo
  candidate=float((lo+hi)/2)
  if not isfinite(candidate):raise ValueError('candidate finite')
  return dict(value=str(value),norm=str(norm),lower=str(lo),upper=str(hi),candidate_hex=candidate.hex(),candidate_radius=str(max(abs(F(candidate)-lo),abs(F(candidate)-hi))))
 if [s['lam'] for s in adapted['sectors']]!=[12,24,36,48]:raise ValueError('frequencies')
 for sector in adapted['sectors']:
  if len(sector['vectors'])!=6 or len(sector['norms'])!=6:raise ValueError('sector dimensions')
  for vector,norm in zip(sector['vectors'],sector['norms']):
   v=list(map(F,vector));norm=F(norm)
   if len(v)!=216 or sum(x*x for x in v)!=norm or norm<0:raise ValueError('literal Gram norm')
   if norm==0:continue
   z=row(sum(-2*v[i] for i in adapted['neighbors']),sector['lam']*norm)
   if z:expected['center'].append(dict(mode=mode,**z))
   for i in adapted['neighbors']:
    z=row(v[i],norm)
    if z:expected['neighbors'][str(i)].append(dict(mode=mode,**z))
   expected['frequencies'].append(row(sector['lam'],sector['lam']));mode+=1
 if mode!=21 or [r['mode'] for r in expected['center']]!=[0,6,12,18]:raise ValueError('center modes')
 for key,value in expected.items():
  if coeff[key]!=value:raise ValueError('exact coefficient reconstruction '+key)
 if coeff['pairs']!=[[[36,-2],[6,-2]],[[36,-2],[180,-2]]]:raise ValueError('pair signs')
 return {'status':'PASS','modes':21,'center_support':4,'neighbor_support':[len(x) for x in expected['neighbors'].values()]}
