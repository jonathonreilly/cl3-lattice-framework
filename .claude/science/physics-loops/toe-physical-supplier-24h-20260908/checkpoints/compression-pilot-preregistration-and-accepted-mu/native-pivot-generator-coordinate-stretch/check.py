from fractions import Fraction as F
import json,pathlib
p=pathlib.Path(__file__).resolve().parent
count=0
def req(v):
 global count
 if not v:raise ValueError(count)
 count+=1
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def J(a):return [-a[2],-a[3],a[0],a[1]]
def add(a,b):return [x+y for x,y in zip(a,b)]
def scale(a,t):return [x*t for x in a]
# Literal nonorthogonal real seeds; Euclidean carrier is identity for this toy.
seeds=list(map(lambda x:list(map(F,x)),[(1,0,1,0),(1,1,0,2)]))
beta=[];r=[];rows=[];wrong=None
for i,s in enumerate(seeds):
 b=s[:];bad=s[:]
 for a in range(i):
  g,j=rows[a][i]
  b=add(b,add(scale(beta[a],-g/r[a]),scale(J(beta[a]),j/r[a])))
  bad=add(bad,add(scale(beta[a],-g/r[a]),scale(J(beta[a]),-j/r[a])))
 for v in beta:req(dot(b,v)==0);req(dot(b,J(v))==0)
 req(dot(b,J(b))==0);req(dot(b,b)>0)
 if i:wrong=bad
 beta.append(b);r.append(dot(b,b));rows.append([(dot(b,x),dot(b,J(x))) for x in seeds])
req(dot(wrong,J(beta[0]))!=0)
# Exact paired projector identity and residual coefficients on independent vectors.
for s in list(map(lambda x:list(map(F,x)),[(2,3,5,7),(0,1,0,0),(-1,2,0,4)])):
 residual=s[:]
 for b,rr in zip(beta,r):
  residual=add(residual,add(scale(b,-dot(b,s)/rr),scale(J(b),-dot(J(b),s)/rr)))
 req(residual==[0]*4)
req(sum(r)>0)
result={'status':'PASS_TINY_EXACT_COEFFICIENT_IDENTITIES','predicates':count,'native_history_loads':0,'native_gram_calls':0,'wrong_J_sign_discriminated':True}
(p/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
