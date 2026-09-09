from fractions import Fraction as F
import json
# C=[[0,2],[0,0]], |C|=diag(0,2), Y=[[2,1],[1,2]],
# P projects onto(1,1). All computations exact and noncommuting.
C=[[F(0),F(2)],[F(0),F(0)]];Q=[[F(0),F(0)],[F(0),F(2)]];Y=[[F(2),F(1)],[F(1),F(2)]];R=[[F(1,2),F(-1,2)],[F(-1,2),F(1,2)]]
def mm(a,b):return [[sum(a[i][k]*b[k][j]for k in range(2))for j in range(2)]for i in range(2)]
def trace(a):return a[0][0]+a[1][1]
def hs2(a):return sum(x*x for r in a for x in r)
assert trace(mm(Q,Y))==4;assert hs2(mm(C,Y))==20;assert 4**2<=20
assert trace(mm(R,Q))==1;assert hs2(mm(C,R))==2;assert 1<=2
assert mm(Q,Y)!=mm(Y,Q);assert mm(C,R)!=[[0,0],[0,0]]
# Exactly approximated C still has nonzero projection tail unless right support holds.
assert trace(mm(R,Q))>0
print(json.dumps({'exact_noncommuting_predicates':9,'native_calls':0}))
