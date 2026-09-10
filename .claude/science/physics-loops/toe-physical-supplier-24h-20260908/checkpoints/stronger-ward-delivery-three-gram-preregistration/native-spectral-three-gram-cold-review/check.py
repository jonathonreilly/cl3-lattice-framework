# Independent tiny Pauli realization only. No accepted values or native loaders.
import pathlib,sys,hashlib,json
from fractions import Fraction as F
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-spectral-three-gram-saved-design')
sys.path.insert(0,str(P));import gram
I=[[1,0],[0,1]];X=[[0,1],[1,0]];Y=[[0,-1j],[1j,0]];Z=[[1,0],[0,-1]]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(2)]for i in range(2)]
def scale(a,c):return [[c*x for x in row]for row in a]
def mul(a,b):return [[sum(a[i][k]*b[k][j]for k in range(2))for j in range(2)]for i in range(2)]
def adj(a):return [[a[j][i].conjugate()for j in range(2)]for i in range(2)]
def ev(a):return sum(mul(rho,a)[i][i]for i in range(2)).real
rho=scale(add(I,scale(Y,-.25)),.5);c=F(1,4);count=0
for dC,dA,n in [(add(X,Y),add(X,Y),2),(add(X,Y),add(X,scale(Y,-1)),0),(add(X,Y),X,1)]:
 for cs,aas in [((1,2,3),(2,-1,1)),((-2,1,-1),(3,2,2))]:
  u,w,q=cs;v,z,t=aas
  BC=scale(mul(Z,dC),1j);BA=scale(mul(Z,dA),1j)
  xC=scale(add(scale(I,u),scale(BC,w)),-1);xA=scale(add(scale(I,v),scale(BA,z)),-1)
  vC=scale(add(scale(dC,2j*u),scale(Z,4*w)),q);vA=scale(add(scale(dA,2j*v),scale(Z,4*z)),t)
  # Formula J B=4a requires norm(d)=2, so mixed norm-one case is tested only xx.
  exact=[ev(mul(adj(xC),xA)),ev(mul(adj(vC),vA)),ev(mul(mul(adj(xC),Z),vA))]
  vals=gram.kernels(tuple(gram.P(x)for x in cs),tuple(gram.P(x)for x in aas),gram.P(c),n)
  for a,b in zip(exact,vals):assert b[0]==b[1]==F(a);count+=1
labels=gram.LABELS;T=[[int(not(set(a)&set(b)))for b in labels]for a in labels]
for i,a in enumerate(labels):
 for j,b in enumerate(labels):assert sum(T[i][k]*T[k][j]for k in range(15))==(6 if i==j else 1 if not(set(a)&set(b))else 3);count+=1
logs=[];ans=gram.evaluate({'c':['1/4','1/4'],'nominal':['-2','-1'],'spectral_alpha_interval':['-5','5'],'E_upper':'1','F_upper':'1','coefficients':{}},lambda *x:logs.append(x));assert ans['ordered_pairs']==0 and len(logs)==1;count+=1
print(json.dumps({'checks':count,'scope':'synthetic Pauli kernels, graph weights, screened zero-kernel branch','native_calls':0}))
