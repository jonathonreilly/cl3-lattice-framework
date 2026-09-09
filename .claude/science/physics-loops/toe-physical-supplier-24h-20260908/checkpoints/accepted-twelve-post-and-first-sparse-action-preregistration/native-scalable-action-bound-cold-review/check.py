from fractions import Fraction as F
import json,pathlib
p=pathlib.Path(__file__).resolve().parent
n=0
def req(b):
 global n
 if not b:raise ValueError(n)
 n+=1
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tr(a):return list(map(list,zip(*a)))
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
C=[[F(3,5),0],[0,F(3,5)],[F(4,5),0],[0,F(4,5)]];P=mm(C,tr(C));I=[[F(i==j) for j in range(4)]for i in range(4)];R=sub(I,P);L=[[F((i==j)*(2 if i<2 else 3))for j in range(4)]for i in range(4)];LC=mm(L,C)
req(mm(tr(C),C)==[[1,0],[0,1]]);req(mm(R,C)==[[0,0]]*4)
base=mm(R,LC)
for Z in ([[0,0],[0,0]],[[2,0],[0,2]],[[F(7,3),F(2,5)],[-1,4]]):req(mm(R,sub(LC,mm(C,Z)))==base)
Q=[[1,0],[0,1],[0,1],[1,0]];A=mm(tr(C),Q);G=sub(mm(tr(Q),Q),mm(tr(A),A));req(G==mm(tr(Q),mm(R,Q)))
Y=[[F(2,3),F(1,7)],[F(-1,3),F(4,7)]];src=mm(R,mm(Q,Y));Gsrc=mm(tr(Y),mm(G,Y));req(sum(Gsrc[i][i] for i in range(2))==sum(x*x for row in src for x in row))
for k,expected in((4,164),(12,420),(24,804)):req(8*(4*k)+36==expected)
req(48*96*8==36864);req(8*8*48==3072);req(96*48*48==221184)
(p/'RESULT.json').write_text(json.dumps({'status':'PASS_EXACT_SHIFT_SOURCE_GRAM_AND_COUNTS','predicates':n,'native_calls':0},indent=2)+'\n');print(n)
