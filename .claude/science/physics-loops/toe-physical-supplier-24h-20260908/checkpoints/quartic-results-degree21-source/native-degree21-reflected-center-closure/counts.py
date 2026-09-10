"""Formal mask census only. No source Gram or scalar evaluation."""
from fractions import Fraction as F
from itertools import product
from math import factorial
import json

def keys(mask):return list(product(*(range(n+1)for n in mask)))
def multiply(P,Q,mask):
 out={}
 for a,row in P.items():
  for b,col in Q.items():
   n=tuple(x+y for x,y in zip(a,b))
   if any(x>m for x,m in zip(n,mask)):continue
   R=out.setdefault(n,{})
   for w,c in row.items():
    for v,d in col.items():R[w+v]=R.get(w+v,F(0))+c*d
 return {n:{w:c for w,c in row.items()if c}for n,row in out.items()}
def exp(variable,mask,letters,sign):
 out={}
 for n in range(mask[variable]+1):out[tuple(n if j==variable else 0 for j in range(len(mask)))]= {w:F(sign**n,factorial(n))for w in product(letters,repeat=n)}
 return out
def census(mask,rank,kind):
 U={}
 for a in keys(mask):
  if kind=='nominal'and a[3]:continue
  den=1
  for n in a:den*=factorial(n)
  U[a]={(0,)*sum(a):F(1,den)}
 factors=[(0,(0,1),-1),(2,(0,2),-1)]
 if kind=='nominal':factors +=[(3,(3,),2),(1,(0,3),-1)]
 else:factors +=[(1,(0,1),-1)]
 for v,letters,sign in factors:U=multiply(U,exp(v,mask,letters,sign),mask)
 assert all(not any(all(z==0 for z in w)for w in row)for a,row in U.items()if sum(a))
 W=sum(map(len,U.values()));nonzero=[a for a in keys(mask)if sum(a)];E=lambda d:rank*rank*(d+1)*(d+2)//2 if d>=0 else 0
 products=0
 for m in range(2,sum(mask)+1):
  for alpha in nonzero:
   for beta in nonzero:
    gamma=tuple(x-y for x,y in zip(alpha,beta))
    if min(gamma)<0 or sum(gamma)<m-1:continue
    products+=2*E(sum(beta)-1)*E(sum(gamma)-(m-1))
 trace=sum(E(sum(a)-m)for a in nonzero for m in range(1,sum(a)+1));operator=W*(2*rank**4*(sum(mask)-1)+rank**2);scalar=3*len(keys(mask))**2
 return {'mask':mask,'rank':rank,'coefficients':len(U),'formal_words':W,'log_products_upper':products,'trace_upper':trace,'factor_upper':operator,'scalar_upper':scalar,'complex_product_upper':products+trace+operator+scalar,'one_matrix_family_entries':sum(E(sum(a)-1)for a in nonzero)}
r={'nominal':census((2,2,1,1),4,'nominal'),'inner':census((2,2,4),3,'inner')};r['all_five_nominal_two_inner_product_upper']=5*r['nominal']['complex_product_upper']+2*r['inner']['complex_product_upper'];r['native_values']=0
print(json.dumps(r,indent=2))
