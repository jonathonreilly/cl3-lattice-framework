from fractions import Fraction as F
from pathlib import Path
import json
# Real rational SVD fixture, distinct full-rank singular values.
def tr(A):return sum(A[i][i] for i in range(len(A)))
def T(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def add(A,B):return [[x+y for x,y in zip(r,s)] for r,s in zip(A,B)]
def sub(A,B):return [[x-y for x,y in zip(r,s)] for r,s in zip(A,B)]
U=[[F(3,5),F(-4,5)],[F(4,5),F(3,5)]];V=[[F(5,13),F(-12,13)],[F(12,13),F(5,13)]];S=[[F(2),F(0)],[F(0),F(3)]];A=[[F(1),F(2)],[F(2),F(-1)]];B=[[F(3),F(-1)],[F(-1),F(4)]];C=[[[F(0),F(1)],[F(0),F(0)]],[[F(0),F(0)],[F(1),F(0)]]]
X=mm(mm(U,S),T(V));Y=mm(mm(U,S),T(U));Z=mm(mm(V,S),T(V))
def energy(X,A,B):return tr(mm(mm(T(X),A),X))+tr(mm(mm(T(X),X),T(B)))-sum(tr(mm(mm(mm(T(X),c),X),T(c))) for c in C)
left=energy(X,A,B)-(energy(Y,A,A)+energy(Z,B,B))/2
right=F(0)
for c in C:
 d=sub(mm(mm(T(U),c),U),mm(mm(T(V),c),V));right+=tr(mm(mm(mm(S,d),S),T(d)))/2
if left!=right or left<=0:raise ValueError('defect identity')
Path(__file__).with_name('EQUALITY_RESULT.json').write_text(json.dumps({'exact_defect':str(left),'identity':True,'scope':'one rational noncommuting fixture; analytical proof not inferred from fixture'},indent=2)+'\n')
