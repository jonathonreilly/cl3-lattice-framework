from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import numpy as np,json,time,signal,resource
t=time.monotonic();P=Path(__file__).parent;census=json.loads((P/'CENSUS.json').read_text());V=list(product(range(6),repeat=3));black=[i for i,v in enumerate(V) if sum(v)%2==0];white=[i for i,v in enumerate(V) if sum(v)%2];bi={v:i for i,v in enumerate(black)};wi={v:i for i,v in enumerate(white)};B=np.zeros((108,108),dtype=np.int64)
for e,(i,j) in enumerate(census['edges']):
 tail=V[e//3];sgn=-(-1)**sum(tail[:e%3]);a,b=(i,j) if i in bi else (j,i);B[bi[a],wi[b]]=sgn if i in bi else -sgn
A=B@B.T;nodes=[3,6,9,12];mult=[32,48,24,4];I=np.eye(108,dtype=np.int64);powers=[I,A,A@A,A@A@A];coeff=[F(0)]*4;s=F(25,4)
for x in nodes:
 poly=[F(1)];den=F(1)
 for y in nodes:
  if y==x:continue
  new=[F(0)]*(len(poly)+1)
  for k,z in enumerate(poly):new[k]-=y*z;new[k+1]+=z
  poly=new;den*=x-y
 for k,z in enumerate(poly):coeff[k]+=z/den/(x+s)
R=[[sum(coeff[k]*int(powers[k][i,j]) for k in range(4)) for j in range(108)] for i in range(108)]
def mm(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def inv(A):
 n=len(A);M=[r[:]+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  k=next(i for i in range(j,n) if M[i][j]);M[j],M[k]=M[k],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for i in range(n):
   if i!=j:q=M[i][j];M[i]=[a-q*b for a,b in zip(M[i],M[j])]
 return [r[n:] for r in M]
def lowerroot(x):return F(isqrt(x*10**60),10**30)
canonical=72+40*lowerroot(3)+48*lowerroot(6)

def certify(mask,controls=False):
 D=np.zeros_like(B)
 for e,(a,b) in enumerate(census['edges']):
  if mask>>e&1:
   if a not in bi:a,b=b,a
   D[bi[a],wi[b]]=-2*B[bi[a],wi[b]]
 z=D[bi[0],:].copy();u=D[:,wi[36]].copy();u[bi[0]]=0;ev=np.zeros(108,dtype=np.int64);ev[bi[0]]=1;ew=np.zeros(108,dtype=np.int64);ew[wi[36]]=1
 rem=D-np.outer(ev,z)-np.outer(u,ew);nz=np.argwhere(rem)
 f=np.zeros(108,dtype=np.int64);g=np.zeros(108,dtype=np.int64)
 if len(nz):
  if len(nz)!=1:raise ValueError('rank3 defect')
  ii,jj=nz[0];f[ii]=rem[ii,jj];g[jj]=1
 FF=np.column_stack((ev,u,f));GG=np.column_stack((z,ew,g));U=np.column_stack((FF,B@GG));GGram=GG.T@GG
 C=[[F(int(GGram[i,j])) if i<3 and j<3 else F(i==j+3 or j==i+3) for j in range(6)] for i in range(6)]
 if controls:
  literal=(B+D)@(B+D).T-A
  exact=U@np.array(C,dtype=object)@U.T
  if any(F(int(literal[i,j]))!=exact[i,j] for i in range(108) for j in range(108)):raise ValueError('exact Gram factorization')
 U=[[F(int(x)) for x in r] for r in U];Ut=list(map(list,zip(*U)));RU=mm(R,U);G=mm(Ut,RU);H=mm(list(map(list,zip(*RU))),RU);CG=mm(C,G);M=[[CG[i][j]+F(i==j) for j in range(6)] for i in range(6)];Mi=inv(M)
 if controls and mm(M,Mi)!=[[F(i==j) for j in range(6)] for i in range(6)]:raise ValueError('inverse residual')
 corr=mm(mm(Mi,C),H);trace=sum(F(m)/(x+s) for m,x in zip(mult,nodes))-sum(corr[i][i] for i in range(6));upper=F(648+675,10)+F(5,2)*(108-F(25,4)*trace);gap=canonical-upper
 return dict(mask=str(mask),gap_lower=str(gap),positive=gap>0,display=float(gap))
