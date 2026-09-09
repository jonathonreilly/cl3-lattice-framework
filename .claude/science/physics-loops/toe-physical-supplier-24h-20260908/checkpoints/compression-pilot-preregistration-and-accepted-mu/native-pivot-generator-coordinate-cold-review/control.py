from fractions import Fraction as F
import json
N=6
J=lambda x: [-x[i+3] for i in range(3)]+x[:3]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
add=lambda a,b:[x+y for x,y in zip(a,b)]
scale=lambda c,a:[c*x for x in a]
sub=lambda a,b:add(a,scale(-1,b))
e=[[F(i==j) for i in range(N)] for j in range(N)]
f=[e[0],add(e[1],add(scale(2,e[0]),scale(3,e[3]))),add(e[2],add(scale(-1,e[0]),add(e[3],scale(2,e[4]))))]
carrier=f+[J(v) for v in f]
apply=lambda c:[sum(carrier[j][i]*c[j] for j in range(N)) for i in range(N)]
# An independently specified real skew action. No imported producer helper.
K=[[F((i+1)*(j+2)) if i<j else F(-(j+1)*(i+2)) if i>j else F(0) for j in range(N)] for i in range(N)]
kapply=lambda x:[dot(r,x) for r in K]
checks=0;bad=0;basis=[];betas=[];hist=[]
for h in range(3):
 seed=e[h];physical=f[h];beta=seed[:];direct=physical[:]
 for a,b in enumerate(basis):
  g=dot(b,physical);j=dot(b,J(physical));r=dot(b,b)
  direct=sub(direct,add(scale(g/r,b),scale(-j/r,J(b))))
  beta=add(sub(beta,scale(g/r,betas[a])),scale(j/r,J(betas[a])))
 assert apply(beta)==direct;checks+=1
 assert dot(direct,direct)==1;checks+=1
 for b in basis:
  assert dot(direct,b)==dot(direct,J(b))==0;checks+=2
 assert dot(direct,J(direct))==0;checks+=1
 if h:
  wrong=seed[:]
  for a,b in enumerate(basis):
   g=dot(b,physical);j=dot(b,J(physical));wrong=sub(sub(wrong,scale(g,betas[a])),scale(j,J(betas[a])))
  assert apply(wrong)!=direct;bad+=1;checks+=1
 basis.append(direct);betas.append(beta)
 V=[q for b in basis for q in (b,J(b))];C=[q for b in betas for q in (b,J(b))]
 for c,v in zip(C,V):assert apply(c)==v;checks+=1
 Av=[[dot(u,kapply(v)) for v in V] for u in V]
 action=[kapply(v) for v in V]
 residual=[sub(action[j],[sum(V[a][i]*Av[a][j] for a in range(len(V))) for i in range(N)]) for j in range(len(V))]
 for i in range(len(V)):
  for j in range(len(V)):
   # H=iK, so Hcompression^2=-Av^2. Direct residual differs by i only.
   lhs=dot(action[i],action[j])+sum(Av[i][a]*Av[a][j] for a in range(len(V)))
   assert lhs==dot(residual[i],residual[j]);checks+=1
   if h==2:assert lhs==0;checks+=1
print(json.dumps({'status':'PASS_TINY_INDEPENDENT_COEFFICIENT_ACTION_IDENTITIES','predicates':checks,'wrong_J_sign_discriminations':bad,'dimension':N,'native_calls':0,'saved_history_loads':0}))
