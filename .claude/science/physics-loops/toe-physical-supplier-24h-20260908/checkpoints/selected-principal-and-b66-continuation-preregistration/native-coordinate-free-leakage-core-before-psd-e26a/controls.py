import core
from fractions import Fraction as F
def mat(A):return [[core.exact(F(x))for x in row]for row in A]
I=mat([[1,0],[0,1]]);A=mat([[0,-2],[2,0]]);Z=mat([[5,0],[0,4]])
r=core.certify(I,A,Z,I);assert r['delta_squared_upper']==1 and r['delta_squared_lower']==1 and r['target_excluded']and not r['leakage_pass']
r=core.certify(I,A,mat([[4,0],[0,4]]),I);assert r['delta_squared_upper']==0 and r['leakage_pass']
r=core.certify(mat([[0,0],[0,1]]),A,Z,I);assert r['status']=='INDETERMINATE_FRAME'
try:core.certify(I,mat([[0,2],[2,0]]),Z,I)
except core.Refused:pass
else:raise AssertionError('wrong skew')
assert 2*104**2*48+3*104*48**2==1757184
print({'status':'PASS_TINY_SCHUR','checks':5,'native_calls':0})
