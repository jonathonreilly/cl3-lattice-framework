#!/usr/bin/env python3
"""Exact supporting algebra only: no native state, spectrum, or Gaussian evaluation."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse,json,hashlib
P=Path(__file__).resolve().parents[1]/'.claude/science/physics-loops/native-ward-direct-overlap-20260910'
def mm(a,b):return [[sum((a[i][k]*b[k][j]for k in range(len(b))),F(0))for j in range(len(b[0]))]for i in range(len(a))]
def add(a,b):return [[x+y for x,y in zip(r,s)]for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r]for r in a]
def controls(boundary_sign=-1,negative_eigenvalue=-3):
 n=0
 def check(v):
  nonlocal n
  if not v:raise ValueError('support predicate '+str(n))
  n+=1
 pairs=list(combinations(range(6),2));T=[[F(not(set(a)&set(b)))for b in pairs]for a in pairs];check(sum(map(sum,T))==90)
 L=[[F(int(i in a))-F(1,3)for i in range(6)]for a in pairs];Lt=list(map(list,zip(*L)));E0=[[F(1,15)]*15 for _ in range(15)];E1=scale(mm(L,Lt),F(1,4));I=[[F(i==j)for j in range(15)]for i in range(15)];E2=add(add(I,scale(E0,-1)),scale(E1,-1));check(add(add(scale(E0,6),scale(E1,negative_eigenvalue)),E2)==T)
 for E in(E0,E1,E2):check(mm(E,E)==E)
 for E,G in((E0,E1),(E0,E2),(E1,E2)):check(mm(E,G)==[[0]*15 for _ in range(15)])
 check([sum(E[i][i]for i in range(15))for E in(E0,E1,E2)]==[1,5,9])
 c=F(49,60);M=F(43,5);m=(M-4*c+c**3)/(M*c-4);lower=135*m*m-180*m
 check(c*c>F(2,3));check(m==F(1269649,653040));check(m>F(4,3));check(lower==F(506499805921,3158972160));check(lower>160)
 # Strict derivative sign uses the improved third-moment majorant.
 check(c<1 and 2*M+16-M*M<0);check(M*F(3,4)-4>0)
 check(F(36,7)>F(81,16));check(252<256)
 for k,l,t,u in [(F(1),F(2),F(3,5),F(4,5)),(F(3,2),F(5,4),F(-2),F(1,3))]:
  check(u*u*(k+l)==(t*t+u*u)*k+t*t*k+u*u*l+2*k*t*(-t))
 for support in([F(1,4),F(2)],[F(1),F(4)],[F(1,2),F(3),F(5)]):
  k=len(support);a=sum(support)/k;b=sum(x*x for x in support)/k;d=sum(x**3 for x in support)/k
  check(sum(1/x for x in support)/k >= (d-2*a*b+a**3)/(a*d-b*b))
 gamma=[[F(1),F(0)],[F(0),F(-1)]];R=[];W=[]
 for k in range(15):
  R.append([[F(-2),F(k,100)],[F(k,100),F(-3)]]);W.append([[F(2),F(k+1,17)],[F(k+1,17),F(-2)]]);check(add(mm(W[-1],gamma),mm(gamma,W[-1]))==[[4,0],[0,4]])
 original=channel=F(0)
 for c in range(15):
  for a in range(15):
   if not T[c][a]:continue
   direct=mm(R[c],R[a])[0][0]
   middle=mm(mm(mm(R[c],gamma),add(W[a],scale(W[c],-1))),R[a])[0][0]
   left=mm(mm(mm(W[c],R[c]),gamma),R[a])[0][0];right=mm(mm(mm(R[c],gamma),R[a]),W[a])[0][0]
   original+=3*direct+(middle-left-right)/2
   v=add(mm(R[a],W[a]),scale(mm(W[a],R[a]),-1));channel+=direct+boundary_sign*mm(mm(R[c],gamma),v)[0][0]
 check(original==channel)
 return {'predicates':n,'m1':str(m),'direct_lower':str(lower),'ordered_words':90,'synthetic_ward_value':str(original)}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--json',action='store_true');ap.parse_args()
 manifest=json.loads((P/'IMPORT_PROVENANCE.json').read_text())
 for name,x in manifest.items():
  if hashlib.sha256((P/'imports'/name).read_bytes()).hexdigest()!=x['sha256']:raise ValueError('import hash '+name)
 result=controls();mutants=[]
 for kwargs in({'boundary_sign':1},{'negative_eigenvalue':3}):
  try:controls(**kwargs)
  except ValueError:mutants.append(kwargs)
  else:raise AssertionError('semantic mutant survived')
 print(json.dumps({'status':'PASS_EXACT_ALGEBRA_SUPPORT',**result,'semantic_mutants_rejected':mutants,'import_hashes_checked':len(manifest),'native_evaluations':0,'full_alpha_established':False},indent=2))
if __name__=='__main__':main()
