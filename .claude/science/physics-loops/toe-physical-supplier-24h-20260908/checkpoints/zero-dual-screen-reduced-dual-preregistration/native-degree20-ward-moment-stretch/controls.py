from pathlib import Path
from fractions import Fraction as F
import json
ns={};p=Path('/private/tmp/toe-24h-probes-20260908/native-low-degree-ward-moment-design/core.py');exec(compile(p.read_bytes(),str(p),'exec'),ns)
add,scale,mul,imag,gamma,advance=[ns[k]for k in ['add','scale','mul','imag','gamma','advance']]
one=ns['ONE'];g=[gamma(i)for i in range(4)];K={0:{1:F(-2)},1:{0:F(2)},2:{3:F(-4)},3:{2:F(4)}}
a=g[0];d=add(scale(g[1],-1),g[3]);k=scale(g[1],-2);v=add(scale(g[0],-2),scale(g[2],4));z=scale(a,-4);w=add(scale(g[1],4),scale(g[3],-16));B=imag(mul(a,d));J=scale(imag(d),2)
O2=add(scale(one,2),scale(mul(k,d),-1),scale(mul(a,v),-1))
O3=add(scale(B,-2),scale(imag(mul(a,k)),2),imag(mul(d,v)),scale(imag(mul(z,d)),-1),scale(imag(mul(k,v)),-2),scale(imag(mul(a,w)),-1))
assert advance(B,K,B)==O2
assert advance(O2,K,B)==O3
assert ns['dagger'](O2)!=O2
M=add(scale(v,-2),scale(a,-8));O=add(one,scale(B,F(2,3)),scale(O2,F(-1,7)));b=mul(J,O)
Db=add(mul(J,add(B,scale(O2,F(2,3)),scale(O3,F(-1,7)))),mul(M,O))
assert advance(b,K,B)==Db
print(json.dumps({'status':'PASS_NONNATIVE_CLIFFORD_ONLY','checks':4,'native_moment_calls':0},indent=2))
