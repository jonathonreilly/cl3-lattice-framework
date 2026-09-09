from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
nchecks=0
def require(x):
 global nchecks
 nchecks+=1
 if not x:raise ValueError('predicate '+str(nchecks))
N=32
partial=F(0)
for n in range(N+1):
 p=F(comb(2*n,n)*sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1)),6**(2*n))
 c=F(comb(4*n,2*n),4**(2*n))
 partial+=p*c
 # Elementary c_m^2(3m+1)<=1 induction step checked by exact polynomial identity.
 m=2*n
 require((2*m+1)**2*(3*m+4)-(2*m+2)**2*(3*m+1)==-m)
require(F(2449,1000)**2<6)
upper=partial*F(1000,2449)+F(1,6*N)
result={'N':N,'partial':str(partial),'C0_h_upper':str(upper),'comparison_7_over_15':upper<F(7,15),'physical_matrix_calls':0,'physical_integral_calls':0}
require(upper<F(7,15));require(F(99,70)**2>2);require(F(14,15)*F(99,70)==F(33,25));require(F(2,3)-F(33,50)==F(1,150));require(F(1,150)/F(58,25)==F(1,348));require(F(14,9)<F(33,25)**2)
examples=[]
def det(M):return M[0][0]*M[1][1]-M[0][1]*M[1][0]
for n in (1,2,4,16):
 S=[[F(6*n*n),0],[0,F(1)]];D=[[-F(6*n*n),F(4*n)],[-F(4*n),F(7,3)]];E=[[D[i][j]-S[i][j] for j in range(2)] for i in range(2)]
 require(det(E)==0);require(det(D)/det(S)==F(1,3))
 for lam in (F(0),F(1,2),F(1)):
  V=[[S[i][j]+lam*E[i][j] for j in range(2)] for i in range(2)];require(det(V)/det(S)==1-2*lam/3)
 tr=D[0][0]+D[1][1];skew=D[1][0]-D[0][1];require(tr<0)
 examples.append({'n':n,'polar_cos_negative':True,'cos_squared':str(tr*tr/(tr*tr+skew*skew)),'scaled_norm_F_squared':str(sum(x*x for row in D for x in row)/(6*n*n)**2)})
result.update({'status':'PASS','predicates':nchecks,'nonnative_rank_one_examples':examples})
result['summands']=N+1
result['scope']='finite exact supporting controls; no physical evaluation'
