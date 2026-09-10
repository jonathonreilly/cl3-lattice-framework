"""Fabricated formal radial sequence, not any native moment evaluation."""
import json
import tables
import arithmetic as a
from fractions import Fraction as F
R=lambda n:a.point(n+2)
D,B=tables.radial_tables(R,2,0,0,1)
def has(z,re=0,im=0):return all(F(lo,a.S)<=v<=F(hi,a.S)for(lo,hi),v in zip(z,(F(re),F(im))))
assert has(D(0,1,2),F(4,6)-2)
assert not has(D(0,1,2),2-F(4,6))
assert has(D(0,1,1),F(4,3))
assert has(D(1,0,1),0,F(-4,3))
assert has(B(0,0,1),0,F(3,6))
assert has(B(1,1,2),-((F(5,6)-3)/2))
assert has(B(1,0,1),0,F(-4,6))
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','formal_radial_checks':7,'native_moments':0}))
