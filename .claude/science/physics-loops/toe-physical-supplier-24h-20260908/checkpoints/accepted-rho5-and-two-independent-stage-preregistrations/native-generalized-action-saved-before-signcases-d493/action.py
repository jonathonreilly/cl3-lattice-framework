"""Independent literal seed/free/rank-two action reconstruction; no source imports."""
from fractions import Fraction as F
import stages as s

def seeds(ids):
 if len(ids)!=24 or len(set(ids))!=24 or any(type(x)is not int or not 0<=x<399 for x in ids):raise s.Incomplete('24 labels')
 columns=[]
 for index in ids:
  if index>=396:base={index:s.point(1)}
  else:
   pole,t=divmod(index,6);axis=t//2
   base={6*pole+axis:s.point(F((1 if t%2==0 else -1)*(1 if axis==0 else -1),2)),6*pole+axis+3:s.point(F(1,2))}
  for g in(0,1):columns.append({(i,g):v for i,v in base.items()})
 r=sorted({i for c in columns for i in c});u=sorted(set(r)|{(i,g)for i in(396,399,400,401)for g in(0,1)})
 e=[[c.get(i,s.point(0))for c in columns]for i in r]
 return r,u,e

def run(ids,t,m,poles,alpha,emit):
 r,u,e=seeds(ids);n=len(u);p=48;position={x:i for i,x in enumerate(u)};terms=0
 s.shape(t,p,p);s.shape(m,n,n)
 if len(poles)!=66 or len(alpha)!=66:raise s.Incomplete('66 coefficients')
 if any(t[i][i][0]<=0 or t[i][j][0]!=t[i][j][1]or(j<i and t[i][j]!=(0,0))for i in range(p)for j in range(p)):raise s.Incomplete('exact positive upper')
 if any(m[i][j]!=m[j][i]for i in range(n)for j in range(n)):raise s.Incomplete('symmetric principal')
 def product(a,b):
  nonlocal terms
  emit('matrix_product_start',dict(rows=len(a),inner=len(b),columns=len(b[0]),completed_terms=terms))
  ar=s.Arithmetic();z=ar.mm(a,b);terms+=ar.count
  emit('matrix_product_raw',dict(matrix=z,completed_terms=terms))
  if terms>4000000:raise s.Incomplete('adapter count')
  return z
 cr=product(e,t);c=[[s.point(0)for _ in range(p)]for _ in u]
 for label,row in zip(r,cr):c[position[label]]=row
 emit('embedding',dict(R=r,U=u,E=e,C_U=c))
 mc=product(m,c);h=product(s.transpose(c),mc);emit('H_raw',h);h=s.symmetric(h);results=[]
 for impurity in(399,400):
  b=[[s.point(0)for _ in range(p)]for _ in u];ar=s.Arithmetic()
  def add(label,j,v):
   k=position[label];b[k][j]=s.plus(b[k][j],v)
  for (raw,g),row in zip(r,cr):
   for j,coefficient in enumerate(row):
    if raw<396:
     pole,endpoint=divmod(raw,6);axis=endpoint%3;sp=s.pair(poles[pole]);aa=s.pair(alpha[pole])
     if sp[0]<=0:raise s.Incomplete('positive pole')
     v=ar.mul(coefficient,sp);add((raw,g),j,v if endpoint>=3 else s.neg(v))
     add(((396,399,400)[axis],g),j,ar.mul(coefficient,ar.mul(s.point(-2),s.sqrt_interval(aa))))
    else:add(((401,399,400)[raw-396],g),j,coefficient)
  # The impurity acts on physical g=0 rows only; no Gamma commutation.
  for j in range(p):
   add((396,0),j,ar.mul(s.point(8),mc[position[(impurity,0)]][j]))
   add((impurity,0),j,ar.mul(s.point(-8),mc[position[(396,0)]][j]))
  emit('action_columns',dict(impurity=impurity,B_U=b));mb=product(m,b);a=product(s.transpose(c),mb);z=product(s.transpose(b),mb)
  emit('A_Z_raw',dict(impurity=impurity,A=a,Z=z));a=s.symmetric(a,True);z=s.symmetric(z)
  d=[[s.plus(s.point(i==j),s.neg(s.midpoint(h[i][j])))for j in range(p)]for i in range(p)]
  d2=[[s.midpoint(v)for v in row]for row in product(d,d)];d3=[[s.midpoint(v)for v in row]for row in product(d2,d)]
  x=[[s.plus(s.plus(s.point(i==j),d[i][j]),s.plus(d2[i][j],d3[i][j]))for j in range(p)]for i in range(p)]
  for i in range(p):
   for j in range(i+1,p):v=(x[i][j][0]+x[j][i][0])//2;x[i][j]=x[j][i]=(v,v)
  emit('inverse_candidate',dict(impurity=impurity,X=x,terms=4))
  results.append(s.certify(h,a,z,x,lambda stage,data:emit(stage,dict(impurity=impurity,data=data))))
 return dict(status='COMPLETE_SOURCE_ONLY_ALGEBRA',results=results,adapter_terms=terms,C_width_gate_required=False,runtime_ready=False)
