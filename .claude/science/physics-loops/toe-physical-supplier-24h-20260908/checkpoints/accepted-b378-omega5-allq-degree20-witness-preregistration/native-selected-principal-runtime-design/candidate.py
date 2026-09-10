"""Bounded dyadic proposal only. Never establishes positive physical Gram."""
from fractions import Fraction as F
from math import isqrt
BITS=256;Q=1<<BITS;CAP=2048
class CandidateFailure(ValueError):pass
def bounded(x):
 if type(x)is not int or x.bit_length()>CAP:raise CandidateFailure('integer bit cap')
 return x
def nearest(n,d):
 bounded(n);bounded(d)
 if d<=0:raise CandidateFailure('divisor')
 return bounded(bounded(bounded(2*n)+d)//bounded(2*d))
def propose(G,persist=lambda stage,data:None):
 n=len(G)
 if not 0<n<=48 or any(len(r)!=n for r in G):raise CandidateFailure('dimension')
 A=[]
 for row in G:
  a=[]
  for x in row:
   if type(x)is not F:raise CandidateFailure('Fraction input')
   bounded(x.numerator);bounded(x.denominator);a.append(nearest(bounded(x.numerator*Q),x.denominator))
  A.append(a)
 if any(A[i][j]!=A[j][i]for i in range(n)for j in range(n)):raise CandidateFailure('symmetry')
 L=[[0]*n for _ in range(n)]
 for i in range(n):
  for j in range(i+1):
   z=bounded(A[i][j]*Q)
   for k in range(j):z=bounded(z-bounded(L[i][k]*L[j][k]))
   persist('candidate_pivot',{'i':i,'j':j,'radicand_or_numerator':z,'partial_L':L})
   if i==j:
    if z<=0:raise CandidateFailure('nonpositive rounded pivot')
    L[i][j]=bounded(isqrt(z))
    if L[i][j]==0:raise CandidateFailure('zero rounded pivot')
   else:L[i][j]=nearest(z,L[j][j])
  persist('candidate_factor_row',{'row':i,'L':L})
 # Solve L^T T=I, column by column, all entries same dyadic scale.
 T=[[0]*n for _ in range(n)]
 for j in range(n):
  for i in range(j,-1,-1):
   z=Q*Q if i==j else 0
   for k in range(i+1,j+1):z=bounded(z-bounded(L[k][i]*T[k][j]))
   T[i][j]=nearest(z,L[i][i]);persist('candidate_inverse_entry',{'i':i,'j':j,'T':T})
  if T[j][j]<=0:raise CandidateFailure('nonpositive inverse diagonal')
 return [[F(x,Q)for x in row]for row in T]
