"""Exact finite synthetic Fock controls only; no native model data."""
import sympy as S
from math import factorial
I=S.I
X=S.Matrix([[0,1],[1,0]]);Y=S.Matrix([[0,-I],[I,0]]);Z=S.diag(1,-1);ID=S.eye(2)
def kron(xs):
 r=S.ones(1)
 for x in xs:r=S.kronecker_product(r,x)
 return r

def one_case(freq,dvec,N=7):
 m=len(freq);g=[]
 for j in range(m):
  for p in [X,Y]:g.append(kron([Z]*j+[p]+[ID]*(m-j-1)))
 K=S.zeros(2*m)
 for j,k in enumerate(freq):K[2*j,2*j+1]=k;K[2*j+1,2*j]=-k
 h=I*K;P=S.diag(*([S.eye(2)]*m))
 for j,k in enumerate(freq):P[2*j:2*j+2,2*j:2*j+2]=(S.eye(2)-h[2*j:2*j+2,2*j:2*j+2]/k)/2
 a=S.eye(2*m)[:,0];d=S.Matrix(dvec);assert(a.T*d)[0]==0
 V=2*I*(a*d.T-d*a.T);ha=h+V
 H=S.zeros(2**m)
 for j in range(m):H+=I*freq[j]*g[2*j]*g[2*j+1]/2+freq[j]*S.eye(2**m)/2
 B=I*g[0]*sum((dvec[j]*g[j]for j in range(2*m)),S.zeros(2**m));D=H+B
 U=[S.eye(2*m)]
 for k in range(N):U.append(S.simplify((h*U[-1]-U[-1]*ha)/(k+1)))
 G=[S.zeros(2*m)]+[P*u for u in U[1:]];R=[S.eye(2*m)];ell=[S.Integer(0)];z=[S.Integer(1)]
 for n in range(1,N+1):
  R.append(-sum((G[k]*R[n-k]for k in range(1,n+1)),S.zeros(2*m)))
  ell.append(S.simplify(sum(((R[j]*(n-j)*G[n-j]).trace()for j in range(n)),S.Integer(0))/(2*n)))
  z.append(S.simplify(sum((k*ell[k]*z[n-k]for k in range(1,n+1)),S.Integer(0))/n))
 count=0;v=S.eye(2**m)[:,0]
 for n in range(N+1):
  expected=(S.eye(2**m)[:,0].T*v)[0];actual=S.simplify((-1)**n*factorial(n)*z[n]);assert S.simplify(actual-expected)==0,(freq,dvec,n,actual,expected);count+=1;v=D*v
 # The factor 1/2 in log Z is essential whenever first moment is nonzero.
 if B[0,0]!=0:assert S.simplify(-2*ell[1]-B[0,0])!=0;count+=1
 return count
if __name__=='__main__':
 count=sum(one_case(f,d)for f,d in [([2,5],[0,1,1,0]),([3,7],[0,0,1,1]),([2,5,7],[0,1,1,-1,1,0])])
 print({'status':'PASS_EXACT_SYNTHETIC_FOCK_VS_ONEPARTICLE_JETS','checks':count,'native_values_loaded':0,'dimension_max':8,'moment_degree_max':7})
