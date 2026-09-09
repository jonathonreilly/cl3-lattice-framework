from fractions import Fraction as F
import pathlib,json
p=pathlib.Path(__file__).resolve().parent;n=0
def req(x):
 global n
 if not x:raise ValueError(n)
 n+=1
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tr(a):return list(map(list,zip(*a)))
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
C=[[F(3,5),0],[0,F(3,5)],[F(4,5),0],[0,F(4,5)]];A=tr(C);L=[[F((i==j)*(2 if i<2 else 3))for j in range(4)]for i in range(4)];Z=mm(A,mm(L,C));I=[[int(i==j)for j in range(4)]for i in range(4)];P=mm(C,A);R=sub(I,P)
req(sub(mm(L,C),mm(C,Z))==mm(R,mm(L,C)))
req(Z[0][0]!=0);req(Z==tr(Z)) # disproves generally skew restriction
J=[[0,-1],[1,0]];req(mm(J,Z)==mm(Z,J))
for g,j in [(F(2),F(3)),(F(-7,3),F(5,2)),(F(0),F(-1))]:
 f=[g,-j];gf=[j,g];req(mm(J,[[f[0]],[f[1]]])==[[gf[0]],[gf[1]]])
for chi in(-1,1):
 zp,zm=F(7,3),F(-5,2);fm=(zp+chi*zm)/2;fp=(zp-chi*zm)/2;req(fm+fp==zp);req(chi*(fm-fp)==zm)
req(48**2*96==221184);req(24**2*48==27648)
(p/'RESULT.json').write_text(json.dumps({'status':'PASS_TINY_FORWARD_SHIFT','predicates':n,'native_calls':0},indent=2)+'\n');print(n)
