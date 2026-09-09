"""Synthetic exact controls only, no native scalar data."""
from fractions import Fraction as F
from pathlib import Path
import sys,json
import interval as iv
from core import coefficients,woodbury
from assemble import assemble_class
n=0
def ck(x):
 global n
 if not x:raise ValueError('toy predicate')
 n+=1
def encl(a,x):ck(F(a[0],iv.S)<=x<=F(a[1],iv.S))
for a in [F(-7,3),F(-1,7),F(0),F(2,3),F(11,5)]:
 for b in [F(-9,5),F(-1,3),F(1,11),F(8,3)]:
  encl(iv.add(iv.rational(a),iv.rational(b)),a+b);encl(iv.mul(iv.rational(a),iv.rational(b)),a*b);encl(iv.div(iv.rational(a),iv.rational(b)),a/b)
for x in [F(0),F(1,7),F(2),F(49,9)]:
 a=iv.sqrt(iv.rational(x));ck(F(a[0],iv.S)**2<=x<=F(a[1],iv.S)**2)
N=[[int(i==j) for j in range(7)] for i in range(7)];O=[[0]*7 for _ in range(7)];T=[[0]*7 for _ in range(7)]
for k in range(3):
 a=1+2*k;b=a+1;N[a][b]=N[b][a]=O[a][b]=O[b][a]=1;T[0][a]=-1;T[0][b]=1;T[a][0]=1;T[b][0]=-1
rows=[]
for s in [F(1),F(2)]:
 A=1/(9+s*s);Ap=-2*s/(9+s*s)**2;B=3*A;Bp=3*Ap;D=(1-s*s*A)/6;Dp=-(2*s*A+s*s*Ap)/6
 rows.append(dict(s=str(s),weight='1/10',A=str(A),Aprime=str(Ap),B=str(B),Bprime=str(Bp)))
 for kind,d in [('P',[0,1,0,1,0,0,0]),('O',[0,1,-1,0,0,0,0])]:
  vectors=[[1,0,0,0,0,0,0],d]
  for sig in(-1,1):
   mats=[]
   for typ in range(4):
    full=[]
    for i in range(7):
     row=[]
     for j in range(7):
      E=A*N[i][j]-D*O[i][j];Ep=Ap*N[i][j]-Dp*O[i][j]
      vals=[sig*s*E+D*T[i][j],sig*(E+s*Ep)+Dp*T[i][j],-B*N[i][j]-s*s*B*O[i][j]/6+sig*s*B*T[i][j]/6,-Bp*N[i][j]-(2*s*B+s*s*Bp)*O[i][j]/6+sig*(B+s*Bp)*T[i][j]/6]
      row.append(vals[typ])
     full.append(row)
    mats.append([[sum(vectors[a][i]*full[i][j]*vectors[b][j] for i in range(7) for j in range(7)) for b in range(2)] for a in range(2)])
   actual=coefficients(s,sig,(A,Ap,B,Bp),kind)
   for a,e in zip(actual,mats):
    for i in range(2):
     for j in range(2):encl(a[i][j],e[i][j])
   ck(mats[2][0][1]!=-mats[2][0][1])
  signed,det,res=woodbury(s,(A,Ap,B,Bp),kind)
  ck(all(iv.contains_zero(x) for r in res for x in r))
out=Path(sys.argv[1]);out.mkdir()
for kind in('P','O'):
 r=assemble_class(rows,F(22,7),kind,out/kind);ck(r['status']=='CERTIFIED_MIDPOINT_ARITHMETIC_ONLY');ck(r['raw_dimension']==8)
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','predicates':n,'oracle_calls':0,'native_matrix_calls':0,'source':'same assembly kernel, two synthetic poles, both classes; exact seven-source contractions'}))
