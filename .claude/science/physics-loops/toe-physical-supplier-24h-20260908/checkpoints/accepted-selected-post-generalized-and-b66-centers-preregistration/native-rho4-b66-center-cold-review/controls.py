from pathlib import Path
from fractions import Fraction as F
import json
p=Path('/private/tmp/toe-24h-probes-20260908/native-rho4-b66-center-certificate-design');c={};exec(compile((p/'core.py').read_bytes(),str(p/'core.py'),'exec'),c)
n=0;S=c['S']
# Synthetic one-point spectral measures; no native moments/catalog.
for X in (F(1,3),F(2),F(7)):
 for s,t in ((F(1,2),F(3,2)),(F(3),F(1)),(F(2),F(5))):
  A=1/(X+s*s);Ap=-2*s/(X+s*s)**2;At=1/(X+t*t);w=F(2,7)
  g,h=c['center'](s,(t,t),(At,At),(A,A),(Ap,Ap),(w,w))
  exactg=w*X/((X+s*s)*(X+t*t));exacth=w*2*s*X/((X+s*s)**2*(X+t*t))
  assert 0<=exactg-g<F(1,S);assert 0<=exacth-h<F(1,S);n+=2
  assert exacth>0;n+=1
# Final factor and derivative negation must enclose both signs.
for x in (F(-2),F(3)):
 out=c['finalize']((x,x),(F(1,100),F(1,100)),(F(31415,10000),F(31416,10000)))
 for pi in (F(31415,10000),F(31416,10000)):
  for y in (x-F(1,100),x+F(1,100)):
   assert out[0][0]<=2*y/pi<=out[0][1];assert out[1][0]<=-2*y/pi<=out[1][1];n+=2
assert F(1744,2**256)<F(1,10**35);n+=1
print(json.dumps({'synthetic_predicates':n,'native_calls':0,'moment_calls':0}))
