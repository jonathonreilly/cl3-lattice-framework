from fractions import Fraction as F
import json
n=0
def req(x):
 global n
 if not x:raise ValueError('tiny algebra')
 n+=1
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)]for row in a]
I=[[F(1),F(0)],[F(0),F(1)]]
for eps in [F(1,4),F(1,2**20),F(1,2**60)]:
 S=[[F(1),F(1)],[F(0),eps]];G=mm(tr(S),S);C=[[F(1),-1/eps],[F(0),1/eps]]
 req(mm(mm(tr(C),G),C)==I);req(mm(S,C)==I)
 # Artificial independent-box subtraction has positive width; exact repeated symbol cancels.
 d=eps*eps;req(4*d>0);req(eps*eps+d-d==eps*eps)
# Nontrivial upper triangular candidate, with exact correction preserving gauge.
T=[[F(1),F(3)],[F(0),F(1)]];Ti=[[F(1),F(-3)],[F(0),F(1)]]
H=[[F(9,16),F(0)],[F(0),F(1)]];G=mm(mm(tr(Ti),H),Ti);Ri=[[F(4,3),F(0)],[F(0),F(1)]];C=mm(T,Ri)
req(mm(mm(tr(C),G),C)==I);req(C[1][0]==0 and C[0][0]>0 and C[1][1]>0)
delta=F(7,16);bound=delta/(1-delta)**2;req(F(1,3)<=bound)
# Symmetric half map Frobenius inequality without square roots.
for a,b,c in [(1,2,3),(-3,7,0),(0,0,5)]:
 req(F(a*a+c*c,4)+b*b<=F(a*a+c*c+2*b*b,2))
# Sharp interval obstruction on square endpoints.
req(F(1,2)-F(1,3)==F(1,6));req(F(1,4)-F(1,6)==F(1,12))
req(4*24**2==2304);req(4*48*49//2==4704)
print(json.dumps({'status':'PASS','checks':n,'scope':'tiny exact correlated and triangular examples only; no selected native inputs'},indent=2))
