from fractions import Fraction as F
import json
# Two real Majorana source coordinates with d=sqrt2 e1, represented
# by its normalized direction to verify orthogonal reflection signs.
R=[[1,0],[0,-1]];h=[[0,1],[-1,0]]
mul=lambda A,B:[[sum(A[i][k]*B[k][j]for k in range(2))for j in range(2)]for i in range(2)]
assert mul(mul(R,h),R)==[[-x for x in row]for row in h]
assert 3+2+3==8 and 8-2+2==8 and 8+1==9
assert 4*4*3*2==96
# Exact least-squares residual identity, no actual source moments.
for s0,s1,s2 in [(F(5),F(3),F(2)),(F(2),F(2),F(3))]:
 q=s1/s2;assert s0-2*q*s1+q*q*s2==s0-s1*s1/s2
print(json.dumps({'status':'PASS','synthetic_checks':5,'native_values':0}))
