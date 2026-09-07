#!/usr/bin/env python3
import time,signal,resource,sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
START=time.monotonic();signal.alarm(180)
checks=[];counts={}
def check(group,n,b):
 if not b:raise AssertionError(n)
 checks.append(n);counts[group]=counts.get(group,0)+1
def mm(A,B):return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def tr(A):return list(map(list,zip(*A)))
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def diag(xs):return [[F(x) if i==j else F(0) for j in range(len(xs))] for i,x in enumerate(xs)]
def ext(A):
 ps=list(combinations(range(len(A)),2));return [[A[i][k]*A[j][l]-A[i][l]*A[j][k] for k,l in ps] for i,j in ps]
v=[1,2,2];O=[[F(i==j)-F(2*v[i]*v[j],9) for j in range(3)] for i in range(3)]
check('geometry','rational Householder orthogonal',mm(O,tr(O))==eye(3))
triples=[(F(1,4),F(1,2),F(3,4)),(F(-2,3),F(1,3),F(1)),(F(-1),F(-1,2),F(-1,4)),(F(-1),F(0),F(1)),(F(1),F(1),F(1)),(F(3,5),F(-5,13),F(8,17))]
records=[]
for n,lam in enumerate(triples):
 A=mm(mm(O,diag(lam)),tr(O));B=ext(A);vals=[lam[i]*lam[j] for i,j in combinations(range(3),2)]
 score=-B[0][0]+B[1][1]+B[2][2];upper=sum(vals)-2*min(vals)
 check('contraction',f'case{n} Hermitian nonexpansive spectrum',A==tr(A) and all(abs(x)<=1 for x in lam))
 check('contraction',f'case{n} exterior eigenvalue trace',sum(B[i][i] for i in range(3))==sum(vals))
 check('contraction',f'case{n} score spectral upper and one',score<=upper<=1)
 errors=[(1-t*B[i][i])/2 for i,t in enumerate([-1,1,1])]
 check('contraction',f'case{n} exact wrong probability conversion',sum(errors)==(3-score)/2 and sum(errors)>=1 and all(0<=x<=1 for x in errors))
 records.append(dict(eigenvalues=lam,A=A,B=B,score=score,upper=upper,pair_errors=errors))
lam=triples[-1];ss=[F(4,5),F(12,13),F(15,17)]
check('native','Pythagorean dilation identity',all(a*a+b*b==1 for a,b in zip(lam,ss)))
A=mm(mm(O,diag(lam)),tr(O));S=mm(mm(O,diag(ss)),tr(O))
R=[[F(0) for j in range(9)] for i in range(9)]
for i in range(3):
 for j in range(3):R[i][j]=A[i][j];R[i][j+3]=S[i][j];R[i+3][j]=S[i][j];R[i+3][j+3]=-A[i][j]
for i,x in enumerate([-1,1,1],6):R[i][i]=F(x)
check('native','literal9mode Hermitian reflection',R==tr(R) and mm(R,R)==eye(9))
check('native','native bridge reflection rank4',sum(R[i][i] for i in range(9))==1)
W=ext(R);check('native','all36 exterior columns orthonormal',mm(tr(W),W)==eye(36))
pairs=list(combinations(range(9),2));indices=[pairs.index(p) for p in [(0,1),(0,2),(1,2)]]
check('native','actual pair compression equals exterior principal block',[[W[i][j] for j in indices] for i in indices]==ext(A))
firsts=[[1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1]];orient=[1,1,1,-1];table=[]
for n,(first,eta) in enumerate(zip(firsts,orient)):
 need=4-first.count(-1);rs=first+[-1]*need+[1]*(6-need)
 check('mixture',f'rule{n} native rank4 reflection',len(rs)==9 and rs.count(-1)==4)
 obs=[eta]+[eta*rs[i]*rs[j] for i,j in [(0,1),(0,2),(1,2)]]
 target=[1,-1,1,1];err=[F(1-t*x,2) for t,x in zip(target,obs)]
 check('mixture',f'rule{n} exactly one wrong on four tests',sum(err)==1)
 table.append(err)
uniform=[sum(row[j] for row in table)/4 for j in range(4)]
check('mixture','fixed input independent mixture four errors quarter',uniform==[F(1,4)]*4)
check('mixture','fixedpositive three rule mixture pair errors third',[sum(table[i][j] for i in range(3))/3 for j in range(1,4)]==[F(1,3)]*3)
choices=[next(i for i,row in enumerate(table) if row[j]==0) for j in range(4)]
check('adverse','input dependent oracle violates shared mixture premise',all(table[i][j]==0 for j,i in enumerate(choices)))
seconds=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not(math.isfinite(seconds) and math.isfinite(rss) and seconds<180 and rss<180):raise RuntimeError('resource cap failed')
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return [encode(a) for a in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x
out=encode(dict(status='PASS',**{'per_'+k+'_checks':n for k,n in counts.items()},TOTAL=len(checks),checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),contraction_cases=records,native_R=R,four_test_error_table=table,uniform_errors=uniform,input_dependent_oracle_choices=choices,seconds=seconds,rss_MiB=rss))
assert out['TOTAL']==sum(counts.values())
if '--json' in sys.argv:print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS: '+str(out['TOTAL'])+' exact contraction, native exterior-power and mixture checks.')
 print('N5: Fixed positive orientation has three-pair mean error at least one third.')
 print('N5: Input-independent orientation mixtures have four-test worst error at least one quarter.')
 print('N5: The finite four-test saturation control does not prove global256input minimax optimality.')
 print('N5: Product-ready full-line battery mixtures qualify; input-dependent oracle selection does not.')
 print('N5: No adaptive or multiple-event, extra-readout, cap-refusal or general apparatus no-go is claimed.')
 print('source_sha256='+out['source_sha256'])
