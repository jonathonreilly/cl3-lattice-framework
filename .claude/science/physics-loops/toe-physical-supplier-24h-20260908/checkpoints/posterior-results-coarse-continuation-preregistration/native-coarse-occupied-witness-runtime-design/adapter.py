"""Fixed rational-half adapter. Inert import; no data loading or scalar calls."""
from fractions import Fraction as F
from functools import lru_cache
from interval import const,add,mul,neg,inv,sqrt
from dictionary import pole,local_append,I,O,T,N
from witness import mm

@lru_cache(maxsize=66)
def balance(alpha):return sqrt(alpha)

def scale(a,q):return mul(a,const(q))
def sub(a,b):return add(a,neg(b))
def dot(x,m,y):
 z=const(0)
 for i,a in enumerate(x):
  for j,b in enumerate(y):
   if a and b:z=add(z,scale(m[i][j],a*b))
 return z

def seed(index,gamma):
 if type(index)is not int or not 0<=index<399 or type(gamma)is not int or gamma not in(0,1):raise ValueError('seed')
 if index>=396:return {(index,gamma):F(1)}
 n,t=divmod(index,6);v=t//2;chi=1 if v==0 else -1;eta=(-1,1)[t%2]
 return {(6*n+v,gamma):F(-eta*chi,2),(6*n+3+v,gamma):F(1,2)}

def raw_local(label,sources,old,c,mu):
 index,gamma=label
 if index>=396:
  g,j=local_append(sources[index-396],c,mu);return j if gamma else g
 n,k=divmod(index,6);sigma=-1 if k<3 else 1;v=k%3;r=old[n]
 C,L=pole(r['s'],sigma,r['A'],r['B']);matrix=[[sub(neg(L[i][j]),scale(mu,F(O[i][j],6))) for j in range(7)] for i in range(7)] if gamma else C
 bal=balance(r['alpha'])
 return [mul(bal,dot([int(z==i) for z in range(7)],matrix,sources[v])) for i in range(7)]

def local_selected(ids,transform,sources,old,c,mu):
 if len(ids)!=24 or len(transform)!=48:raise ValueError('fixed selected dimension')
 columns=[]
 for index in ids:
  for gamma in (0,1):
   col=[const(0) for _ in range(7)]
   for label,q in seed(index,gamma).items():
    v=raw_local(label,sources,old,c,mu);col=[add(a,scale(b,q)) for a,b in zip(col,v)]
   columns.append(col)
 return mm([[columns[j][i] for j in range(48)] for i in range(7)],transform)

def new_raw_cross(s,sigma,source,label,sources,old,A,B,c):
 index,gamma=label
 if index<396:
  n,k=divmod(index,6);tau=-1 if k<3 else 1;v=k%3;r=old[n]
  den=F(sigma)*F(s)+F(tau)*F(r['s'])
  if not den:raise ValueError('uncontracted confluence')
  Ct,Lt=pole(r['s'],tau,r['A'],r['B']);Cs,Ls=pole(s,-sigma,A,B)
  mat=[[scale(sub(Lt[i][j],Ls[i][j]),-1/den) if gamma else scale(sub(Ct[i][j],Cs[i][j]),1/den) for j in range(7)] for i in range(7)]
  return mul(balance(r['alpha']),dot(source,mat,sources[v]))
 kind=index-396;e=sources[kind];iv=dot(e,[[const(x) for x in row] for row in I],source);ov=dot(e,[[const(x) for x in row] for row in O],source);tv=dot(e,[[const(x) for x in row] for row in T],source);nv=add(iv,ov);d=scale(sub(const(1),scale(A,F(s)**2)),F(1,6))
 if kind==0:
  g=add(scale(mul(A,iv),sigma*F(s)),mul(d,tv));j=sub(mul(B,iv),scale(mul(B,tv),sigma*F(s)/6))
 else:
  g=add(sub(mul(d,ov),mul(A,nv)),scale(mul(A,tv),sigma*F(s)/6))
  j=add(scale(mul(B,tv),F(1,6)),scale(sub(scale(mul(sub(c,B),nv),1/F(s)),scale(mul(B,ov),F(s)/6)),sigma))
 # append-to-new covariance is j; reverse new-to-Gammaappend is -j.
 return scale(neg(j) if gamma else g,F(1,2))

def new_seed_cross(s,sigma,source,ids,sources,old,A,B,c):
 row=[]
 for index in ids:
  for gamma in (0,1):
   x=const(0)
   for label,q in seed(index,gamma).items():x=add(x,scale(new_raw_cross(s,sigma,source,label,sources,old,A,B,c),q))
   row.append(x)
 return row

def transpose(a):return list(map(list,zip(*a)))
def plus(a,b):return [[add(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def zeros(n,m):return [[const(0) for _ in range(m)] for _ in range(n)]
def evaluate(ids,transform,sources,old,new,c,mu,impurity_real,reciprocal_pi,emit):
 """Compute -i times physical Dbar. Accepted coefficient blocks are positive_imaginary."""
 from witness import coarse_block,norm_lower_squared
 if len(new)!=378 or len(old)!=66:raise ValueError('fixed banks')
 local=local_selected(ids,transform,sources,old,c,mu);sx=transpose(local);projector_columns=mm(transform,sx)
 emit('factorization',{'local':local,'projector_columns':projector_columns})
 direct=zeros(7,7);mixed=zeros(7,7)
 # Exactly one chosen impurity source in each call, explicitly passed as source index1 or2.
 for k,row in enumerate(new):
  emit('before_witness_node',{'id':k})
  selector=row['impurity_selector']
  if type(selector)is not int or selector not in(1,2):raise ValueError('impurity selector')
  cols=[];cross=[]
  for sigma in (1,-1):
   C,L=pole(row['s'],sigma,row['A'],row['B'])
   for source in (sources[0],sources[selector]):
    cols.append([dot([int(z==i) for z in range(7)],C,source) for i in range(7)])
    cross.append(new_seed_cross(row['s'],sigma,source,ids,sources,old,row['A'],row['B'],c))
  zf=transpose(cols);K=row['positive_imaginary']
  if len(K)!=4 or any(len(r)!=4 for r in K):raise ValueError('coefficient block')
  left=mm(zf,K);direct=plus(direct,mm(left,transpose(zf)));mixed=plus(mixed,mm(left,mm(cross,projector_columns)))
  if (k+1)%21==0:emit('witness_panel',{'completed':k+1,'direct':direct,'mixed':mixed})
 # impurity_real=-i(hA-h0), supported on the seven star sites.
 high=[[mul(scale(x,F(1,16)),reciprocal_pi) for x in row] for row in impurity_real]
 high_projected=mm(high,mm(local,sx))
 block=[[sub(add(direct[i][j],high[i][j]),add(mixed[i][j],high_projected[i][j])) for j in range(7)] for i in range(7)]
 emit('witness_block',{'block':block})
 norm2=norm_lower_squared(block)
 radius2=sum(((hi-lo)/2)**2 for row in block for lo,hi in row)
 precision_ok=radius2<=F(11,10**5)**2
 # Scalar+finite arithmetic already enclosed in block; .00213 metric and .019 tail remain external.
 # Require the stricter documented .022 center/interval gate unchanged.
 return {'squared_block_lower':str(norm2),'excludes_tau_1e9':precision_ok and norm2>=F(11,500)**2,'status':'EXCLUDED_BY_COARSE_WITNESS' if precision_ok and norm2>=F(11,500)**2 else 'INDETERMINATE_COARSE_WITNESS','stored_operator':'minus_i_times_positive_projector_difference','metric_and_tail_charged':True}
