from pathlib import Path
import json
source=Path('/private/tmp/toe-24h-probes-20260908/native-degree11-independent-review/check.py').read_text();exec(source[:source.index('n=0\n')])
one={():1};O2=add(scale(one,2),scale(mul(k,d),-1),scale(mul(a,v),-1))
O3=add(scale(B,-2),scale(mul(a,k),2j),scale(mul(d,v),1j),scale(mul(z,d),-1j),scale(mul(k,v),-2j),scale(mul(a,w),-1j))
assert D(one)==B;assert D(B)==O2;assert D(O2)==O3
J=scale(d,2j);M=add(scale(v,-2),scale(a,-8));assert add(act(J),mul(B,J),scale(mul(J,B),-1))==M
for coeff in [(1,2,-3),(-2,1,4),(0,0,1)]:
 p0,p1,p2=coeff;O=add(scale(one,p0),scale(B,p1),scale(O2,p2));DO=add(scale(B,p0),scale(O2,p1),scale(O3,p2));assert D(mul(J,O))==add(mul(J,DO),mul(M,O))
def dagger(poly):
 out={}
 for word,c in poly.items():z,s=norm(tuple(reversed(word)));out=add(out,{z:complex(c).conjugate()*s})
 return out
assert dagger(O2)!=O2;assert dagger(dagger(O2))==O2
print(json.dumps({'status':'PASS','checks':9,'scope':'independent ordered-word Clifford recursion, commutator, and adjoint; no native moments'}))
