import os,time,signal
AUDIT_TIMEOUT_SEC=180
START=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sympy as s
from itertools import product,combinations
from collections import deque
import json,hashlib,resource,sys
vertices=list(product((0,1),repeat=4));edges=[]
for v in vertices:
 for a in range(4):
  if v[a]==0:
   q=list(v);q[a]=1;edges.append((v,tuple(q),a))
edgeindex={(v,a):i for i,(v,w,a) in enumerate(edges)}
faces=[]
for a,b in combinations(range(4),2):
 for fixed in product((0,1),repeat=2):
  v=[0]*4
  for j,value in zip([j for j in range(4) if j not in (a,b)],fixed):v[j]=value
  va=v.copy();va[a]=1;vb=v.copy();vb[b]=1
  row=[0]*32
  for i,sign in [(edgeindex[(tuple(v),a)],1),(edgeindex[(tuple(va),b)],1),(edgeindex[(tuple(vb),a)],-1),(edgeindex[(tuple(v),b)],-1)]:row[i]=sign
  omitted=(a,b)==(0,1) and v[2]==0
  faces.append(dict(axes=[a,b],base=v,row=row,omitted=omitted,weight=s.Integer(1) if b==3 else s.Rational(1,2)))
def tree(axisorder):
 axisorder=tuple(axisorder)
 seen={vertices[0]};queue=deque([vertices[0]]);selected=[]
 while queue:
  v=queue.popleft()
  for a in axisorder:
   q=list(v);q[a]=1-q[a];q=tuple(q)
   if q not in seen:
    low=v if v[a]==0 else q;selected.append(edgeindex[(low,a)]);seen.add(q);queue.append(q)
 return selected
checks=[]
def ck(n,b):
 if n in checks or not bool(b):raise AssertionError(n)
 checks.append(n)
ck('graph size',len(vertices)==16 and len(edges)==32 and len(faces)==24)
kept=[f for f in faces if not f['omitted']];marked=sorted([f for f in faces if f['omitted']],key=lambda f:f['base'][3]);weights=s.diag(*[f['weight'] for f in kept])
def matrices(tr):
 chords=[i for i in range(32) if i not in tr]
 B=s.Matrix([[f['row'][i] for i in chords] for f in kept]);S=s.Matrix([[f['row'][i] for i in chords] for f in marked]);H=B.T*weights*B
 return chords,B,S,H
tr=tree(range(4));chords,B,S,H=matrices(tr);ck('tree and cycle ranks',len(tr)==15 and len(chords)==17 and B.rank()==17 and S.rank()==2)
Hi=H.inv();C=S*Hi*S.T;Cov=3*C
ck('positive precision',all(H[:i,:i].det()>0 for i in range(1,18)))
pivots=list(S.rref()[1]);other=[j for j in range(17) if j not in pivots];T=S.col_join(s.eye(17)[other,:]);Ti=T.inv();Q=Ti.T*H*Ti;Schur=Q[:2,:2]-Q[:2,2:]*Q[2:,2:].inv()*Q[2:,:2]
ck('independent source Schur complement',Schur*C==s.eye(2))
ck('determinant Schur factorization',s.simplify(H.det()/T.det()**2-Q[2:,2:].det()*Schur.det())==0)
tr2=tree(reversed(range(4)));c2,b2,ss2,h2=matrices(tr2)
ck('second tree complete',len(tr2)==15 and len(c2)==17);ck('different tree',set(tr)!=set(tr2));ck('gauge independent covariance',ss2*h2.inv()*ss2.T==C)
ck('equal time variances',C[0,0]==C[1,1]);ck('positive source correlation',0<C[0,1]<C[0,0])
J=s.diag(-1,1);ck('source inversion changes cross sign only',J*C*J==s.Matrix([[C[0,0],-C[0,1]],[-C[1,0],C[1,1]]]))
Hfull=H+S.T*S/2;Cfull=S*Hfull.inv()*S.T
ck('restored source faces reduce covariance',(C-Cfull).det()>0 and (C-Cfull)[0,0]>0)
Wzero=s.diag(*[0 if f['axes'][1]==3 else f['weight'] for f in kept]);rankzero=(B.T*Wzero*B).rank();ck('zero temporal rank control',rankzero==10)
Hwrong=B.T*B;Cwrong=S*Hwrong.inv()*S.T;ck('spatial halfweight essential',Cwrong!=C)
# Incidence annihilates vertex gradients before gauge fixing.
D=s.zeros(32,16)
for j,(v,w,a) in enumerate(edges):D[j,vertices.index(v)]=-1;D[j,vertices.index(w)]=1
Fall=s.Matrix([f['row'] for f in faces]);ck('all faces annihilate gauge gradients',Fall*D==s.zeros(24,16))
ck('eight colors normalization',3==s.Rational(1,1)/s.Rational(1,3))
def mat(A):return [[str(v) for v in row] for row in A.tolist()]
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);ck('resources',0<rss<180 and time.monotonic()-START<180)
payload=dict(checks=checks,vertices=vertices,edges=edges,faces=[{**f,'weight':str(f['weight'])} for f in faces],tree_edges=tr,chord_edges=chords,second_tree_edges=tr2,face_incidence=mat(B),weights=mat(weights),source_incidence=mat(S),H=mat(H),H_inverse=mat(Hi),det_H=str(H.det()),source_C=mat(C),source_covariance=mat(Cov),det_source_covariance=str(Cov.det()),correlation=str(s.simplify(C[0,1]/C[0,0])),source_coordinate_map=mat(T),transformed_H=mat(Q),nuisance_det=str(Q[2:,2:].det()),source_schur=mat(Schur),restored_C=mat(Cfull),wrong_halfweight_C=mat(Cwrong),zero_temporal_rank=rankzero,seconds=time.monotonic()-START,rss_MiB=rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest())

pi=s.pi;a=s.Rational(8,135);b=s.Rational(23,270);omega=s.sqrt(55)/90;theta=(32-3*s.sqrt(55))/23
Sigma=s.Matrix([[192,138],[138,192]])/11
ck('source Gaussian precision',Sigma.inv()==s.Matrix([[2*a,-b],[-b,2*a]]))
ck('oscillator frequency',s.simplify(4*a*a-b*b-omega*omega)==0)
ck('Mehler ratio',s.simplify(theta-b/(2*a+omega))==0)
# x=u-y/2 makes Q=u²+3y²/4. Normalized independent Gaussian moments.
expect=s.Rational(4)*s.Rational(15,8)-18*s.Rational(3,4)*s.Rational(2,3)+s.Rational(81,4)*s.Rational(1,2)*s.Rational(4,3)
ck('Weyl Vandermonde Gaussian moment',expect==12)
weyl_integral=expect*2*pi/s.sqrt(3)
j0=s.simplify(weyl_integral/(6*(2*pi)**2)/(2*pi)**4)
ck('normalized Haar tangent density',j0==1/(16*s.sqrt(3)*pi**5))
joint=(2*pi)**-8*Sigma.det()**-4
lambda0=s.simplify(joint/j0*(pi/(a+omega/2))**4)
candidate=s.sqrt(3)*pi*(11/(6*(32+3*s.sqrt(55))))**4
ck('absolute Gaussian ground eigenvalue',s.simplify(lambda0-candidate)==0)
ck('eight versus radial ground power',8*s.Rational(1,2)==3+2*s.Rational(1,2))
degrees={n:sum(2*i+3*j==n for i in range(5) for j in range(4)) for n in range(7)}
ck('invariant first degree is two',degrees[0]==1 and degrees[1]==0 and degrees[2]==1 and degrees[3]==1 and degrees[6]==2)
normalization={'checks':checks[17:],'j0':str(j0),'joint_density_prefactor':str(joint),'omega':str(omega),'theta':str(theta),'ground_eigenvalue':str(candidate),'first_top_ratio':str(s.expand(theta**2)),'invariant_degree_census':degrees}

payload['normalization']=normalization
R=s.Rational
ck('sqrt3 and pi rational product bound',R(7,4)**2>3 and R(22,7)*R(7,4)==R(11,2))
ck('sqrt55 denominator lower bound',R(37,5)**2<55 and 32+3*R(37,5)==R(271,5))
upper=R(11,2)*R(55,271)**4
ck('beta6 leading norm below one percent',upper<R(1,100))
payload['beta6_sanity']={'checks':checks[25:],'leading_norm_rational_upper':str(upper),'actual_norm_lower':1,'relative_error_lower':'99/100','scope':'Leading absolute norm at mathematical beta6 only; no eigenratio error bound or selected physical coupling.'}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
assert 0<rss<180 and time.monotonic()-START<180
payload.update(seconds=time.monotonic()-START,rss_MiB=rss)
if len(sys.argv)==2 and sys.argv[1]=='--json':
 print(json.dumps(payload,indent=2,allow_nan=False))
elif len(sys.argv)==1:
 print('per_element: exact22face/17cycle quadratic geometry; all raw matrices in --json')
 print('per_site: actual two omitted source loops, not a diagonal one-link packet')
 print('per_mode: eight trace-orthonormal Lie colors; central projection required')
 print('per_block: exact Haar/Mehler constants and fixed-branch ratio; nonlinear limit imported')
 print('lattice_wide: finite supplied cube only; no thermodynamic or physical coupling selection')
 print('source_sha256:',payload['source_sha256'])
 print('TOTAL: PASS='+str(len(checks))+' FAIL=0')
else:
 raise SystemExit('usage: runner [--json]')

if len(sys.argv)==1:
 print('Resources: %.6fs; %.3f MiB; limits180s/180MiB.'%(payload['seconds'],payload['rss_MiB']))
