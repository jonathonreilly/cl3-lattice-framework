# Tiny literal seven-site geometry and rational budget controls only.
from fractions import Fraction as F
from itertools import combinations
import json,hashlib,pathlib
p=pathlib.Path(__file__).resolve().parent
count=0
def req(x):
 global count
 if not x: raise ValueError('predicate '+str(count))
 count+=1
I=[[int(i==j) for j in range(7)] for i in range(7)]
O=[[int(i>0 and j>0 and (i-1)//2==(j-1)//2 and i!=j) for j in range(7)] for i in range(7)]
N=[[I[i][j]+O[i][j] for j in range(7)] for i in range(7)]
T=[[0]*7 for _ in range(7)]
for j in range(1,7):T[0][j]= -1 if j%2 else 1;T[j][0]=-T[0][j]
e=[1]+[0]*6
def d(a):return [0]+[(1 if j%2 else -1) if j in a else 0 for j in range(1,7)]
def b(u,M,v):return sum(u[i]*M[i][j]*v[j] for i in range(7) for j in range(7))
D=d(range(1,7));cases=0
for aa in combinations(range(1,7),2):
 for cc in combinations([i for i in range(1,7) if i not in aa],2):
  a,c=d(aa),d(cc); cases+=1
  us=[a,c,D]
  req([[b(u,I,v) for v in us] for u in us]==[[2,0,2],[0,2,2],[2,2,6]])
  for u in us:
   req(b(u,T,e) in (2,6));req(b(u,I,e)==0)
   for v in (a,c):
    req(abs(b(u,N,v))<=2);req(abs(b(u,O,v))<=2);req(b(u,T,v)==0)
  req(sum(b(u,I,u) for u in us)==10)
req(cases==90)
req(F(48985020+804*178,10**19)<F(5,10**12))
req(2**40+804*2800<2**41)
def E_lt(e,t):
 rem=t-1608*e
 return rem>0 and 4*536*1608*e<rem*rem
req(E_lt(F(5,10**12),F(416,100000)))
req(E_lt(F(2**41,10**30),F(2,10**6)))
req(E_lt(F(1,2**60),F(2,10**6)))
req(F(416,100000)+F(4,10**6)+F(1,10**9)+F(1,10**6)<F(42,10000))
# Real sign adverse: the center covariance for d_all has negative sign.
req(-F(b(D,T,e),24)==-F(1,4));req(F(b(D,T,e),24)!=-F(1,4))
result={'status':'PASS_TINY_GEOMETRY_AND_RATIONAL_LEDGER','predicates':count,'ordered_pairs':cases,'native_entries_evaluated':False,'integrals':0,'scope':'geometry and sufficient scalar budget; no Gram, generator or leakage test'}
(p/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
