"""Source-only same-span action contraction. No binder/native entry point."""
from fractions import Fraction as F
from math import isqrt
import leakage as l
S=l.S
Q=tuple((r,g)for r in(396,399,400,401)for g in(0,1))
def tr(M):return list(map(list,zip(*M)))
def rounded(x):x=F(x)*S;return(x.numerator//x.denominator,-((-x.numerator)//x.denominator))
def sqrtbox(x):
 if x[0]<=0:raise l.Refused('positive alpha')
 a=isqrt(x[0]*S);b=isqrt(x[1]*S);return a,b+(b*b<x[1]*S)
def seeds(indices):
 cols=[]
 if len(indices)!=24 or len(set(indices))!=24 or any(type(i)is not int or not 0<=i<399 for i in indices):raise l.Refused('fixed24order')
 for i in indices:
  if i>=396:v={(i,0):l.exact(1)}
  else:
   n,z=divmod(i,6);a,p=divmod(z,2);chi=1 if a==0 else-1;eta=2*p-1;v={(6*n+a,0):l.exact(F(-eta*chi,2)),(6*n+3+a,0):l.exact(F(1,2))}
  cols.extend((v,{(r,1):x for (r,g),x in v.items()}))
 R=tuple(sorted(set().union(*(set(c)for c in cols))));return R,[[c.get(k,(0,0))for c in cols]for k in R]
def run(indices,T,M,poles,alpha,emit=lambda stage,data:None):
 R,E=seeds(indices);U=tuple(sorted(set(R)|set(Q)));u=len(U);p=48;ar=l.Arithmetic();terms=0
 if len(T)!=p or any(len(r)!=p for r in T)or len(M)!=u or any(len(r)!=u for r in M)or len(poles)!=66 or len(alpha)!=66:raise l.Refused('shape')
 for matrix in(T,M):
  for row in matrix:
   for x in row:ar.check(x)
 if any(x[0]!=x[1]for row in T for x in row):raise l.Refused('exact candidateT')
 if any(M[i][j]!=M[j][i]for i in range(u)for j in range(u)):raise l.Refused('physical symmetric enclosure')
 def product(A,B):
  nonlocal terms
  a=l.Arithmetic();z=a.mm(A,B);terms+=a.terms
  if terms>4000000:raise l.Refused('adapter4milliontermcap')
  return z
 C_R=product(E,T);pos={k:i for i,k in enumerate(U)};C=[[(0,0)]*p for _ in U]
 for k,row in zip(R,C_R):C[pos[k]]=row
 emit('embedding',{'R':R,'U':U,'E':E,'C_U':C})
 MC=product(M,C);H=product(tr(C),MC);emit('H_raw',H)
 def symmetric(A,skew=False):
  for i in range(p):
   if skew:
    if not A[i][i][0]<=0<=A[i][i][1]:raise l.Refused('skew diagonal')
    A[i][i]=(0,0)
   for j in range(i+1,p):
    b=ar.neg(A[j][i])if skew else A[j][i];z=ar.check((max(A[i][j][0],b[0]),min(A[i][j][1],b[1])));A[i][j]=z;A[j][i]=ar.neg(z)if skew else z
  return A
 H=symmetric(H);results=[]
 for imp in(399,400):
  B=[[(0,0)]*p for _ in U]
  def acc(k,j,x):B[pos[k]][j]=ar.add(B[pos[k]][j],x)
  for k,row in zip(R,C_R):
   r,g=k
   for j,x in enumerate(row):
    if r<396:
     n,t=divmod(r,6);a=t%3;sp=ar.check(poles[n]);aa=ar.check(alpha[n]);
     if sp[0]<=0:raise l.Refused('positive pole')
     acc(k,j,ar.mul(x,sp)if t>=3 else ar.neg(ar.mul(x,sp)));acc(((396,399,400)[a],g),j,ar.mul(x,ar.mul(l.exact(-2),sqrtbox(aa))))
    else:acc(((401,399,400)[r-396],g),j,x)
  # Actual M rows handle BOTH Gamma copies; only free part commutes Gamma.
  for j in range(p):
   acc((396,0),j,ar.mul(l.exact(8),MC[pos[(imp,0)]][j]));acc((imp,0),j,ar.mul(l.exact(-8),MC[pos[(396,0)]][j]))
  emit('action_columns',{'impurity':imp,'B_U':B});MB=product(M,B);A=product(tr(C),MB);Z=product(tr(B),MB);emit('A_Z_raw',{'impurity':imp,'A':A,'Z':Z});A=symmetric(A,True);Z=symmetric(Z)
  # Four-term candidate I+D+D²+D³ at exact represented midpoints.
  point=lambda x:((x[0]+x[1])//2,)*2
  D=[[ar.add(l.exact(i==j),ar.neg(point(H[i][j])))for j in range(p)]for i in range(p)];D2=[[point(x)for x in row]for row in product(D,D)];D3=[[point(x)for x in row]for row in product(D2,D)];X=[[ar.add(ar.add(l.exact(i==j),D[i][j]),ar.add(D2[i][j],D3[i][j]))for j in range(p)]for i in range(p)]
  for i in range(p):
   for j in range(i+1,p):v=(X[i][j][0]+X[j][i][0])//2;X[i][j]=X[j][i]=(v,v)
  emit('inverse_candidate',{'impurity':imp,'X':X,'terms':4});verdict=l.certify(H,A,Z,X,lambda st,d:emit(st,{'impurity':imp,'data':d}));results.append(verdict)
 return {'status':'COMPLETE_SOURCE_ONLY_ALGEBRA','results':results,'adapter_terms':terms,'C_width_gate_required':False,'runtime_ready':False}
def native(*args,**kwargs):raise l.Refused('NOT_READY: accepted selected output and physical DATA binder absent')
