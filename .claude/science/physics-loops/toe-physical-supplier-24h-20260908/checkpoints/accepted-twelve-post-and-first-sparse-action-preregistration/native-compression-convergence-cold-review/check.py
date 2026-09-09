from fractions import Fraction as F
import pathlib,json
p=pathlib.Path(__file__).resolve().parent
n=0
def req(x):
 global n
 if not x:raise ValueError(n)
 n+=1
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
I=[[int(i==j) for j in range(6)] for i in range(6)];J=[[0]*6 for _ in range(6)];K=[[0]*6 for _ in range(6)]
for a in (0,2,4):J[a+1][a]=1;J[a][a+1]=-1
K[4][2]=K[5][3]=1;K[2][4]=K[3][5]=-1
req(mm(J,K)==mm(K,J));req(tr(K)==[[-x for x in row] for row in K]);req(mm(J,J)==[[-x for x in row] for row in I])
V=[[int(i==j) for j in range(4)] for i in range(6)];KV=mm(K,V);R=[[0]*4 for _ in range(4)]+KV[4:]
req(mm(tr(R),R)==[[int(i==j and i>=2) for j in range(4)] for i in range(4)])
req(mm(tr(V),V)==[[int(i==j) for j in range(4)] for i in range(4)])
# Half-column parallelogram with arbitrary projected residual vectors.
a=[F(2),F(-3),F(1)];b=[F(5),F(2),F(-4)];norm=lambda x:sum(t*t for t in x)
hp=[(x+y)/2 for x,y in zip(a,b)];hm=[(x-y)/2 for x,y in zip(a,b)]
req(norm(a)+norm(b)==2*(norm(hp)+norm(hm)))
for k,expect in ((4,614400),(12,33546240),(24,479232000)):req(10*(2*k)**2*((4*k)*(4*k+8)+(4*k+8)**2)==expect)
for eps in (F(1,2),F(1,100),F(1,1000000)):
 req(F(1)/eps>=2);req((1/eps)*eps==1)
(p/'RESULT.json').write_text(json.dumps({'status':'PASS_TINY_COUNTEREXAMPLE_AND_COUNTS','predicates':n,'native_calls':0},indent=2)+'\n');print(n)
