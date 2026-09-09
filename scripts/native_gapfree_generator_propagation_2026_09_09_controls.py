"""Exact small synthetic support only; no native operator evaluation."""
from fractions import Fraction as F
from math import factorial

def controls():
 count=0;adverse=0
 def ck(x):
  nonlocal count
  if not x:raise ValueError('supporting exact predicate')
  count+=1
 def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),F()) for col in zip(*b)] for row in a]
 def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
 def tr(a):return list(map(list,zip(*a)))
 I=[[F(1),F(0)],[F(0),F(1)]];zero=[[F(0)]*2 for _ in range(2)]
 for a in (F(1),F(3,2),F(7)):
  K=[[F(0),-a],[a,F(0)]];Gamma=[[F(0),F(1)],[F(-1),F(0)]]
  ck(mm(Gamma,K)==[[a,0],[0,a]]);ck(mm(Gamma,Gamma)==[[-1,0],[0,-1]])
  wrong=[[-x for x in row] for row in Gamma];ck(mm(wrong,K)!=[[a,0],[0,a]]);adverse+=1
  for s in (F(1,3),F(2)):
   for sig in(-1,1):
    # Exact inverse of K-sigma*s*I, negated as y=-iR.
    Y=[[sig*s/(a*a+s*s),-a/(a*a+s*s)],[a/(a*a+s*s),sig*s/(a*a+s*s)]]
    rhs=[[sig*s*Y[i][j]-I[i][j] for j in range(2)] for i in range(2)]
    ck(mm(K,Y)==rhs);ck(mm(K,[[-x for x in row] for row in Y])!=rhs);adverse+=1
 # Independent first-action Gram identity for a literal signed Hermitian fixture.
 H=[[F(2),F(1),F(1,3),F(-1,5)],[F(1),F(-3),F(2,7),F(1,4)],[F(1,3),F(2,7),F(4),F(2)],[F(-1,5),F(1,4),F(2),F(-1)]]
 A=[r[:2] for r in H[:2]];R=[r[:2] for r in H[2:]];H2=mm(H,H);ck(sub([r[:2] for r in H2[:2]],mm(A,A))==mm(tr(R),R))
 ck(sub([r[:2] for r in H2[:2]],mm(A,A))!=zero)
 B=lambda z,m:z*(F(7,30)+F(7*m,15))+F(4,3*2**m)
 ck(sum((F(7,10)**j/factorial(j) for j in range(5)),F())>2)
 ck(B(F(1,10000),15)<F(765,10**6)<F(1,1000));ck(B(F(1,10**7),25)<F(123,10**8));ck(398*B(F(1,10**7),25)<F(1,1000))
 ck(F(120000000000,10**6)>100000)
 for m in (0,1,15,25):ck(B(F(1,10**7),m)<B(F(1,10000),m))
 return {'status':'PASS_SUPPORTING_EXACT','predicates':count,'wrong_sign_discriminations':adverse,'physical_calls':0,'scope':'small rational identities and sufficient-condition arithmetic; not a native leakage or semigroup evaluation'}
