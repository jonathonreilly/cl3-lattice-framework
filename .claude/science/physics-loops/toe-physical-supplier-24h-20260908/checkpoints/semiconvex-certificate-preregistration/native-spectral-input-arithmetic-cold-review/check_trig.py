"""Alternate exact pi identity and monotone endpoint sine intervals."""
from fractions import Fraction as F
from pathlib import Path
import json,time,signal
signal.alarm(180);start=time.monotonic();n=0
def ck(x,label):
 global n;n+=1
 if not x:raise RuntimeError(label)
def atan(inv):
 x=F(1,inv);s=F(0);term=x
 for j in range(112):s+=(-1)**j*term/(2*j+1);term*=x*x
 return s,s+term/225
# atan(1/2)+atan(1/3)=pi/4 by tangent addition and first-quadrant branch.
a,b=atan(2);c,d=atan(3);pl,pu=4*(a+c),4*(b+d);scale=1<<160
pl=F(pl.numerator*scale//pl.denominator,scale);pu=F(-((-pu.numerator*scale)//pu.denominator),scale)
ck(F(3)<pl<pu<F(22,7),'alternate pi branch/range')
def sine(x):
 term=x;s=F(0)
 for j in range(50):
  s+=(-1)**j*term
  term*=x*x/F((2*j+2)*(2*j+3))
 return s,s+term
src=Path('/private/tmp/toe-24h-probes-20260908/native-spectral-rational-trig/INPUTS.json');data=json.loads(src.read_text());rows=[]
for r in data['rows']:
 j=r['j'];a=min(j,31-j);xl=pl*F(2*a+1,64);xu=pu*F(2*a+1,64)
 ck(F(0)<xl<xu<pl/2,'monotone sine interval')
 lo=2*sine(xl)[0];hi=2*sine(xu)[1];oldlo=F(r['lower_numerator'],r['denominator']);oldhi=F(r['upper_numerator'],r['denominator'])
 ck(oldlo<=lo<=hi<=oldhi,'alternate enclosure inside supplied interval')
 center=F.from_float(float.fromhex(r['q_hex']));radius=F(r['center_error_numerator'],r['center_error_denominator'])
 ck(center-radius<=oldlo<=oldhi<=center+radius,'actual binary center radius')
 den=1<<120; rows.append({'j':j,'alternate_lower_numerator':lo.numerator*den//lo.denominator,'alternate_upper_numerator':-((-hi.numerator*den)//hi.denominator),'denominator':den})
print(json.dumps({'status':'PASS','predicates':n,'seconds':time.monotonic()-start,'method':'pi=4(atan(1/2)+atan(1/3)),112 terms,160bit outward rounding; monotone folded sine50terms','rows':rows},separators=(',',':')))
