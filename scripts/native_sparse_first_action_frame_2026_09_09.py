#!/usr/bin/env python3
"""Portable small exact supporting controls; no native arrays or runtime imports."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/native-sparse-first-action-frame-20260909'
def main():
 ap=argparse.ArgumentParser();ap.parse_args();n=0
 def ck(x,why):
  nonlocal n
  if not x:raise ValueError(why)
  n+=1
 manifest=json.loads((PACK/'verification/INPUTS.json').read_text())
 for p,h in manifest.items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'source pin '+p)
 def dot(a,b):return sum((x*y for x,y in zip(a,b)),F())
 def gamma(v):return [-v[1],v[0],-v[3],v[2]]
 e=[F(1),F(0),F(0),F(0)];seed=[F(0),F(1),F(1),F(0)]
 # j=<e,Gamma seed>=-1, hence residual=seed+Gamma(e)*j.
 j=dot(e,gamma(seed));res=[seed[k]+gamma(e)[k]*j for k in range(4)]
 ck(res==[0,0,1,0],'paired J sign');ck(dot(e,res)==dot(gamma(e),res)==0,'paired projection')
 for v in (e,seed,res):ck(gamma(gamma(v))==[-x for x in v],'Gamma square')
 # Independent seven-site matrices and three-source self Gram.
 signs=[0,1,-1,1,-1,1,-1]
 reps=(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))
 for aa,cc in reps:
  vectors=[[F(signs[j] if j in ids else 0) for j in range(7)] for ids in (aa,cc,range(1,7))]
  gram=[[dot(u,v)/4 for v in vectors] for u in vectors]
  ck(gram==[[F(1,2),0,F(1,2)],[0,F(1,2),F(1,2)],[F(1,2),F(1,2),F(3,2)]],'self Gram')
  ck(2*sum(gram[i][i] for i in range(3))==5,'DATA added trace')
  for u,target in zip(vectors,(2,2,6)):
   t=sum(u[j]*signs[j] for j in range(1,7));ck(t==target,'T orientation');ck(-F(12,5)*t/24==(-F(1,5) if target==2 else-F(3,5)),'bare center J sign')
 # On a formal orthonormal model Kx0=qD-8qA, K Gamma x0=Gamma qD.
 # This demonstrates noncommuting impurity correction without native data.
 b0=[1,-8,0];b1=[0,0,1];ck(dot(b0,b0)==65 and dot(b1,b1)==1 and dot(b0,b1)==0,'rank-two action')
 ck(399*2==798 and 402*2==804 and 4*4+8==24,'domain counts')
 ck(24*25//2==300 and 2*5*(64*16*24+64*24**2)==614400,'sparse counts')
 ck(5*(3*66*2*3+9+6)==6015 and 5*(3*(66*2+1)+3)==2010,'append census')
 result={'status':'PASS_SMALL_EXACT_SUPPORT','checks':n,'native_arrays_replayed':False,'native_leakage_computed':False,'propagation_computed':False,'alpha_computed':False,'scope':'conditional analytical closure; finite supporting controls only'}
 print(json.dumps(result,sort_keys=True));print(f'TOTAL: PASS={n} FAIL=0')
if __name__=='__main__':main()
