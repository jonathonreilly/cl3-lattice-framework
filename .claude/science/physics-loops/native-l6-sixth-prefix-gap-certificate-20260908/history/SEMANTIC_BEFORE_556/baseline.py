"""Ported independent rank-four/rank-six inverse-trace replay; no author core import."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt,isfinite
from itertools import product
import json,hashlib,sys,signal,time,resource
def ck(x,msg):
 if not x:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def transpose(A):return list(map(list,zip(*A)))
def mat(A,B):
 cols=transpose(B);return [[sum(x*y for x,y in zip(row,col) if x and y) for col in cols] for row in A]
def inv(A):
 n=len(A);M=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for j in range(n):
  k=next(k for k in range(j,n) if M[k][j]);M[j],M[k]=M[k],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for k in range(n):
   if k!=j:q=M[k][j];M[k]=[a-q*b for a,b in zip(M[k],M[j])]
 return [r[n:] for r in M]
def baseline(census):
 V=list(product(range(6),repeat=3));black=[i for i,v in enumerate(V) if sum(v)%2==0];white=[i for i,v in enumerate(V) if sum(v)%2];bi={v:i for i,v in enumerate(black)};wi={v:i for i,v in enumerate(white)};B=[[0]*108 for _ in range(108)]
 for e,(i,j) in enumerate(census['edges']):
  xi=(-1)**sum(V[e//3][:e%3]);sign=-xi
  if i in bi:B[bi[i]][wi[j]]=sign
  else:B[bi[j]][wi[i]]=-sign
 A=mat(B,transpose(B));I=[[int(i==j) for j in range(108)] for i in range(108)];powers=[I,A]
 for k in range(2,4):powers.append(mat(powers[-1],A))
 # Vandermonde interpolation independently solves the four coefficients.
 nodes=(3,6,9,12);VI=inv([[F(x)**k for k in range(4)] for x in nodes]);coef=[sum(v/F(x+F(25,4)) for v,x in zip(row,nodes)) for row in VI];R=[[sum(coef[k]*powers[k][i][j] for k in range(4)) for j in range(108)] for i in range(108)]
 for i in range(108):
  nz=[(k,a) for k,a in enumerate(A[i]) if a]
  for j in range(108):ck(sum(a*R[k][j] for k,a in nz)+F(25,4)*R[i][j]==int(i==j),'baseline inverse')
 return B,R,bi,wi

def gap(mask,center,census,B,R,bi,wi):
 delta=[[0]*108 for _ in range(108)]
 for e,(a,b) in enumerate(census['edges']):
  if mask>>e&1:
   if a not in bi:a,b=b,a
   delta[bi[a]][wi[b]]=-2*B[bi[a]][wi[b]]
 row=delta[bi[0]];column=[delta[i][wi[center]] if i!=bi[0] else 0 for i in range(108)];F0=[[int(i==bi[0]),column[i]] for i in range(108)];G=[[row[j],int(j==wi[center])] for j in range(108)]
 residual=[[delta[i][j]-int(i==bi[0])*row[j]-column[i]*int(j==wi[center]) for j in range(108)] for i in range(108)]
 nz=[(i,j) for i in range(108) for j in range(108) if residual[i][j]]
 ck(len(nz)<=1,'at most one external bridge entry')
 if nz:
  ii,jj=nz[0]
  for i in range(108):F0[i].append(residual[ii][jj]*int(i==ii));G[i].append(int(i==jj))
 rank=len(F0[0]);size=2*rank
 ck(mat(F0,transpose(G))==delta,'literal rank factorization')
 BG=mat(B,G);U=[a+b for a,b in zip(F0,BG)];RU=mat(R,U);UtRU=mat(transpose(U),RU);UtR2U=mat(transpose(RU),RU);GG=mat(transpose(G),G)
 # C^-1=[[0,I],[I,-G*G]], avoiding author's I+C*G inverse formula.
 Ci=[[F(0) if i<rank and j<rank else F(int(i==j+rank or j==i+rank)) if (i<rank)!=(j<rank) else -F(GG[i-rank][j-rank]) for j in range(size)] for i in range(size)]
 S=[[Ci[i][j]+UtRU[i][j] for j in range(size)] for i in range(size)];Si=inv(S);ck(mat(S,Si)==[[F(i==j) for j in range(size)] for i in range(size)],'small inverse');correction=mat(Si,UtR2U);trace=sum(R[i][i] for i in range(108))-sum(correction[i][i] for i in range(size));upper=F(1323,10)+F(5,2)*(108-F(25,4)*trace);canonical=72+40*F(isqrt(3*10**60),10**30)+48*F(isqrt(6*10**60),10**30);return canonical-upper,max(x.denominator.bit_length() for row in mat(Si,Ci) for x in row)

