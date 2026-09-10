from pathlib import Path
from fractions import Fraction as F
import json
namespace={};source=Path('/private/tmp/toe-24h-probes-20260908/native-low-degree-ward-moment-design/core.py');exec(compile(source.read_bytes(),str(source),'exec'),namespace)
add,scale,mul,imag,gamma,advance=[namespace[k]for k in ['add','scale','mul','imag','gamma','advance']]
one=namespace['ONE'];g=[gamma(i)for i in range(4)];K={0:{1:F(-2)},1:{0:F(2)},2:{3:F(-4)},3:{2:F(4)}}
a=g[0];d=add(scale(g[1],-1),g[3]);k=scale(g[1],-2);v=add(scale(g[0],-2),scale(g[2],4));z=scale(a,-4);w=add(scale(g[1],4),scale(g[3],-16));B=imag(mul(a,d));J=scale(imag(d),2)
checks=0
for u,V in [(F(1),F(0)),(F(0),F(1)),(F(2,3),F(-5,7))]:
 b=add(scale(J,u),scale(a,V));Db=advance(b,K,B)
 formula1=add(scale(add(scale(v,-2),scale(a,-4)),u),scale(imag(add(k,scale(d,-1))),V))
 assert Db==formula1;checks+=1
 D2b=advance(Db,K,B)
 formula2=add(scale(imag(add(scale(w,-2),scale(mul(mul(a,d),v),-2),scale(k,-4),scale(d,4))),u),scale(add(scale(z,-1),scale(mul(mul(a,d),k),-1),v,scale(a,2)),V))
 assert D2b==formula2;checks+=1
 if u:
  wrong=add(formula2,scale(imag(mul(mul(a,d),v)),4*u))
  assert wrong!=D2b;checks+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ALGEBRA_ONLY','checks':checks,'native_moment_calls':0,'scope':'four-Majorana two-bond D²b identity; no native moment substitution'},indent=2))
