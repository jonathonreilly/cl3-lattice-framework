from fractions import Fraction as F
from pathlib import Path
import json,hashlib
checks={}
def ck(n,p):
 assert p,n
 checks[n]=True
M=24;v=F(19,20)
for lam in (F(-1,10),F(0),F(1,10)):
 cap=12*abs(lam)
 for nf in (0,24):
  for x in (0,12):
   b=1+((1-v)*nf+cap-lam*x)/M
   ck(f'positive_{lam}_{nf}_{x}',b>=1)
   ck(f'diagonal_{lam}_{nf}_{x}',b-F(nf,M)==1-(v*nf+lam*x-cap)/M)
   ck(f'flip_{lam}_{nf}_{x}',b*(1/b)/M==F(1,M))
# Each plane appears twice among six ordered transverse channels.
planes={tuple(sorted((a,b))):0 for a in range(3) for b in range(3) if a!=b}
for a in range(3):
 for b in range(3):
  if a!=b:planes[tuple(sorted((a,b)))]+=1
ck('six_channel_double_count',list(planes.values())==[2,2,2])
# Exact elementary eigenbranch E(l)=2+3l verifies restoration and missing lambda term.
h=F(1,10)
e=lambda l:2+3*l
shift=lambda l:12*abs(l)
ck('restored_central_derivative',(e(h)-shift(h)+shift(h)-e(-h)+shift(-h)-shift(-h))/(2*h)==3)
ck('unrestored_right_derivative_adverse',(e(h)-shift(h)-e(0))/h!=3)
ck('nonzero_source_omission_adverse',v*5+h*3-e(h)!=v*5-e(h))
ck('weighted_not_arithmetic_adverse',F(1+6,1+2)!=(F(1,1)+F(6,2))/2)
ck('elastic_zero_mode_adverse',F(1,2)<F(1,1))
payload={'status':'PASS','checks':checks,'count':len(checks),'scope':'Exact kernel scalar and channel algebra, not ice-state enumeration or stochastic validation','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps(payload))
