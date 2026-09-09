"""Independent literal Fock algebra; synthetic 2/4-mode rational pairings only."""
from fractions import Fraction as Q
import json,signal,time,resource
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29s exact controls')));signal.alarm(29)
start=time.monotonic();checks=0;wrong_sign_failures=0

def req(x,msg):
 global checks
 if not x:raise ValueError(msg)
 checks+=1

def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0)) for j in range(len(b[0]))] for i in range(len(a))]
def neg(a):return [[-x for x in r] for r in a]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def inverse(a):
 n=len(a);b=[r[:]+s for r,s in zip(a,eye(n))]
 for i in range(n):
  j=next(j for j in range(i,n) if b[j][i]);b[i],b[j]=b[j],b[i];z=b[i][i];b[i]=[v/z for v in b[i]]
  for j in range(n):
   if j!=i:
    z=b[j][i];b[j]=[x-z*y for x,y in zip(b[j],b[i])]
 return [r[n:] for r in b]
def det(a):
 a=[r[:] for r in a];v=Q(1);n=len(a)
 for i in range(n):
  inds=[j for j in range(i,n) if a[j][i]]
  if not inds:return Q(0)
  j=inds[0]
  if j!=i:a[i],a[j]=a[j],a[i];v=-v
  z=a[i][i];v*=z
  for j in range(i+1,n):
   c=a[j][i]/z;a[j]=[x-c*y for x,y in zip(a[j],a[i])]
 return v

def action(v,j,create):
 out=[Q(0)]*len(v)
 for b,x in enumerate(v):
  if bool((b>>j)&1)==(not create):out[b^(1<<j)]+=(-1)**((b&((1<<j)-1)).bit_count())*x
 return out

def state(z):
 n=len(z);v=[Q(0)]*(1<<n);v[0]=1;out=v[:]
 for k in range(1,n//2+1):
  nv=[Q(0)]*len(v)
  for i in range(n):
   for j in range(i+1,n):
    w=action(action(v,j,True),i,True)
    nv=[a+z[i][j]*b/k for a,b in zip(nv,w)]
  v=nv;out=[a+b for a,b in zip(out,v)]
 return out

def inner(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def skew(n,entries):
 z=[[Q(0)]*n for _ in range(n)]
 for i,j,v in entries:z[i][j]=Q(v);z[j][i]=-Q(v)
 return z

def cp(x,power):
 power%=4
 return (x,Q(0)) if power==0 else (Q(0),x) if power==1 else (-x,Q(0)) if power==2 else (Q(0),-x)
def ca(a,b):return a[0]+b[0],a[1]+b[1]
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def cn(a):return -a[0],-a[1]
za=skew(4,[(0,1,'1/5'),(0,2,'1/7'),(1,3,'-1/6'),(2,3,'1/8')])
zc=skew(4,[(0,1,'-1/4'),(0,3,'1/9'),(1,2,'1/5'),(2,3,'1/10')])
fixtures=[(skew(2,[(0,1,'99/100')]),skew(2,[(0,1,'-99/100')])),(za,zc),(za,za),(za,skew(4,[]))]
for za,zc in fixtures:
 n=len(za);va=state(za);vc=state(zc);ov=inner(va,vc)
 req(ov>0,'positive unnormalized overlap');req(ov*ov==det(sub(eye(n),mm(za,zc))),'det overlap square')
 req(inner(va,va)**2==det(sub(eye(n),mm(za,za))),'anchor determinant')
 A=inverse(sub(eye(n),mm(zc,za)));F=neg(mm(A,zc));B=mm(za,A);C=neg(mm(mm(za,A),zc))
 for create1,create2,expected in [(False,False,F),(False,True,A),(True,False,C),(True,True,B)]:
  for i in range(n):
   for j in range(n):
    actual=inner(va,action(action(vc,j,create2),i,create1))/ov
    req(actual==expected[i][j],'ordered CAR block')
    if not create1 and not create2 and actual and actual!=-expected[i][j]:wrong_sign_failures+=1
 def gamma(v,index):
  j=index//2;b=index%2;ann=action(v,j,False);cre=action(v,j,True)
  return [c-a if b else c+a for c,a in zip(cre,ann)]
 def literal(indices):
  v=vc
  for j in reversed(indices):v=gamma(v,j)
  return cp(inner(va,v)/ov,sum(j%2 for j in indices))
 def contraction(i,j):
  ii=i//2;jj=j//2
  u1=cp(Q(1),3 if i%2 else 0);v1=cp(Q(1),1 if i%2 else 0)
  u2=cp(Q(1),3 if j%2 else 0);v2=cp(Q(1),1 if j%2 else 0)
  out=(Q(0),Q(0))
  for x,y,z in [(u1,u2,F[ii][jj]),(u1,v2,A[ii][jj]),(v1,u2,C[ii][jj]),(v1,v2,B[ii][jj])]:out=ca(out,cm(cm(x,y),cp(z,0)))
  return out
 for i in range(2*n):
  req(literal([i])==(0,0),'odd insertion')
  for j in range(2*n):req(literal([i,j])==contraction(i,j),'complex Majorana pair')
 for q in range(64):
  m=2*n;i=q%m;j=(q//m)%m;k=(3*q+2)%m;l=(5*(q//m)+1)%m
  wick=ca(ca(cm(contraction(i,j),contraction(k,l)),cn(cm(contraction(i,k),contraction(j,l)))),cm(contraction(i,l),contraction(j,k)))
  req(literal([i,j,k,l])==wick,'ordered Wick4')
req(wrong_sign_failures>0,'wrong F sign genuinely discriminated')
r=Q(99,100);q=r*r
req(q**2049/(1-q)<Q(1,10**15),'finite Neumann tail')
req(1/(1-q)==Q(10000,199),'inverse bound')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
req(seconds<30 and rss<384*1048576,'resources')
print(json.dumps({'status':'PASS','predicates':checks,'fixtures':4,'wrong_F_sign_discriminations':wrong_sign_failures,'seconds':seconds,'rss_bytes':rss,'physical_calls':0,'scope':'literal synthetic Fock exponent, ordered CAR, overlap determinant and Majorana Wick tests; no native evolution'},indent=2))
