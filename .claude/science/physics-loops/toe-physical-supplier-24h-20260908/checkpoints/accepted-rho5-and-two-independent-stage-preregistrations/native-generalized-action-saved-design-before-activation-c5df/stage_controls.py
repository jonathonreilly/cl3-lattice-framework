from fractions import Fraction as F
import stages as s
from action import seeds
# Noncommuting matrices and independent exact Fraction expectation for each dot.
a=[[s.point(1),s.point(F(1,2))],[s.point(0),s.point(2)]]
b=[[s.point(0),s.point(-1)],[s.point(3),s.point(0)]]
z=s.Arithmetic().mm(a,b)
assert z==[[s.point(F(3,2)),s.point(-1)],[s.point(6),s.point(0)]]
# Directed outward rounding at a non-grid exact product.
assert s.Arithmetic().mul((1,2),(1,3))==(0,1)
assert s.Arithmetic().mul((-2,-1),(1,3))==(-1,0)
# Valid generalized Schur: H=I, A skew, Z=-A²+diag(1,4).
h=[[s.point(1),s.point(0)],[s.point(0),s.point(1)]]
a=[[s.point(0),s.point(-2)],[s.point(2),s.point(0)]]
z=[[s.point(5),s.point(0)],[s.point(0),s.point(8)]]
ev=[];ans=s.certify(h,a,z,h,lambda st,d:ev.append((st,d)))
assert ans['delta_squared_lower']==4 and ans['delta_squared_upper']==4 and ans['target_excluded'] and not ans['leakage_pass']
assert [st for st,d in ev]==['frame_residual','inverse_residual','AXA','N_raw','Schur_center','Schur_center','result']
try:s.pair((True,1))
except ValueError:pass
else:raise AssertionError('bool')
r,u,e=seeds(list(range(24)));assert len(e[0])==48 and (401,1)in u
print('{"status":"PASS","cases":7,"scope":"small exact noncommuting and directed rounding, no actual input"}')
