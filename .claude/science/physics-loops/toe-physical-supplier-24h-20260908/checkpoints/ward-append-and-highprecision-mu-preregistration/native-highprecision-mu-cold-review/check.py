from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json
n=0
def ck(x):
 global n
 if not x:raise ValueError('exact algebra predicate')
 n+=1
ck(F(31,40)**2-F(21,40)**2>0)
ck(F(3200,2759)<F(27,25)**2)
ck(6/F(31,40)**2==F(9600,961))
R=F(20,3)*(4+F(4800,961))*F(4,25)**26
width=F(100,157)*(2*R+F(12**27,53*8**53)+F(1,2**64)+F(1,10**25))+F(1,10**35)
ck(width<F(2,10**19))
q=Path('/private/tmp/toe-24h-probes-20260908/native-highprecision-mu-catalog-design');v=json.loads((q/'PROSPECTIVE_WIDTH.json').read_text());ck(F(v['radius'])==R);ck(F(v['full_width_upper'])==width)
for x in (F(0),F(1,3),F(6),F(12)):
 for t in (F(8),F(31,3),F(32)):
  partial=sum((-1)**j*x**(j+1)/t**(2*j+2) for j in range(26));rem=x**27/(t**52*(t*t+x))
  ck(partial+rem==x/(t*t+x));ck(0<=rem<=12**27/t**54)
# Bound propagated node uncertainty with exact rational interval product width.
dt=F(1,2**140);dA=F(2,10**30)+dt/3
ck(64*dA+16*dt*F(17,60)<F(2,10**28))
ck(9*F(2,10**28)+1742*dt+F(100000,2**192)<F(1,10**25))
f=json.loads((q/'RUNTIME_FREEZE.json').read_text());bad=[]
for p,h in f['inputs'].items():
 if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h:bad.append(p)
ck(not bad)
print(json.dumps({'status':'PASS','predicates':n,'pins':len(f['inputs']),'bad':bad,'width_decimal_display':float(width),'physical_calls':0},indent=2))
