import os,time,json,hashlib,resource,sys,signal
signal.alarm(180)
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from itertools import product
import sympy as s
import numpy as np
from scipy.sparse import csr_matrix,diags
start=time.monotonic();checks={}
def ck(name,c):
 checks[name]=bool(c)
 if not c:raise RuntimeError(name)
A=s.Matrix([[0,1,0],[1,0,1],[0,1,0]]);H=s.Rational(4,5)*s.diag(1,2,1)-A;G=s.eye(3)-H/3;one=s.ones(3,1);h=H*one;psi=G**2*one;Z=(psi.T*psi)[0];O=s.diag(1,s.I,2-s.I);X=s.diag(1,1,5);E=(psi.T*H*psi)[0]/Z;S=(psi.T*X*psi)[0]/Z
mom=[0]*6
for x in product(range(3),repeat=5):
 w=s.prod(G[x[j],x[j+1]] for j in range(4))/Z
 for k,v in enumerate([h[x[0]],h[x[0]]*h[x[-1]],X[x[2],x[2]]*(h[x[0]]+h[x[-1]])/2,h[x[2]],h[x[0]]**2,X[x[2],x[2]]]):mom[k]+=w*v
ck('tiny_endpoint_E',s.simplify(mom[0]-E)==0);ck('tiny_endpoint_product_H2',s.simplify(mom[1]-(psi.T*H**2*psi)[0]/Z)==0);ck('tiny_midpoint_cross_XH',s.simplify(mom[2]-(psi.T*X*H*psi)[0]/Z)==0)
D=sum(A[i,j]*psi[i]*psi[j]*s.Abs(O[i,i]-O[j,j])**2 for i in range(3) for j in range(3))/(2*Z*S);cov=mom[2]-S*E;R=((O*psi).conjugate().T*(H-E*s.eye(3))*(O*psi))[0]/(Z*S)
ck('tiny_complex_Rayleigh_plus_covariance',s.simplify(R-D-cov/S)==0);ck('tiny_omit_covariance_mutant',cov!=0);ck('tiny_wrong_midpoint_endpoint_mutant',mom[3]!=E);ck('tiny_wrong_endpoint_square_mutant',mom[4]!=mom[1]);varH=(psi.T*(H-E*s.eye(3))**2*psi)[0]/Z;varX=(psi.T*X**2*psi)[0]/Z-S*S;ck('tiny_sharper_bound',s.simplify(varH*varX-cov*cov)>=0)
tiny={'E':str(E),'H_variance':str(varH),'D':str(s.simplify(D)),'correction':str(s.simplify(cov/S)),'R_E':str(s.simplify(R))}
# Literal L2 graph, no author module or stored energy values.
coords=[(v//4,v//2%2,v%2) for v in range(8)]
def edge(c,a):return 3*(4*c[0]+2*c[1]+c[2])+a
faces=[]
for a,b in [(0,1),(0,2),(1,2)]:
 for c in coords:
  ca=list(c);cb=list(c);ca[a]^=1;cb[b]^=1;faces.append([edge(c,a),edge(ca,b),edge(cb,a),edge(c,b)])
x0=sum(c[a]<<edge(c,a) for c in coords for a in range(3));states=[x0];idx={x0:0};rows=[];cols=[];labels=[]
for x in states:
 for lab,f in enumerate(faces):
  if tuple((x>>e)&1 for e in f) in [(0,1,0,1),(1,0,1,0)]:
   y=x^sum(1<<e for e in f)
   if y not in idx:idx[y]=len(states);states.append(y)
   rows.append(idx[x]);cols.append(idx[y]);labels.append(lab)
ck('literal_component',len(states)==864 and len(rows)==6912)
A=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(864,864));nf=np.asarray(A.sum(1)).ravel();H=.95*diags(nf)-A;G=diags(np.ones(864))-H/24;h=-.05*nf
O=np.array([[sum((-1)**(sum(c)+c[a])*(((x>>edge(c,b))&1)-.5) for c in coords)/np.sqrt(8) for a in range(3) for b in range(3) if a!=b] for x in states]);X=(O*O).sum(1)
increments=((O[np.array(rows)]-O[np.array(cols)])**2).sum(1);ck('literal_all6912_summed_flip_increments',np.max(abs(increments-1))<1e-14) # 2*qhat²/Vol=1
out=[]
for n in [2,48,192]:
 v=np.ones(864);u=h.copy();mid=None;umid=None
 for j in range(n):
  v=G@v;u=G@u;scale=np.linalg.norm(v);v/=scale;u/=scale
  if j+1==n//2:mid=v.copy();umid=u.copy()
 E=float(mid@(H@mid));H2=float(np.linalg.norm(H@mid)**2);S=float((mid*mid)@X);cross=float((mid*X)@umid);ep=float(h@v/v.sum());prod=float(h@u/v.sum());cov=cross-S*E
 ck('endpoint_identity_'+str(n),abs(ep-E)<1e-12 and abs(prod-H2)<1e-12 and np.max(abs(umid-H@mid))<1e-12)
 D=.5*(.95*float((mid*mid)@nf)-E)/S
 R=sum(float((mid*O[:,a])@(H@(mid*O[:,a])))-E*float(np.linalg.norm(mid*O[:,a])**2) for a in range(6))/S
 ck('literal_Rayleigh_correction_'+str(n),abs(R-D-cov/S)<1e-12)
 varH=float(np.linalg.norm(H@mid-E*mid)**2);varX=float((mid*mid)@((X-S)**2));bound=np.sqrt(varH*varX)/S
 ck('residual_bound_'+str(n),abs(cov/S)<=bound+1e-12)
 out.append(dict(n=n,E=E,H2=H2,endpoint_product=prod,variance_direct=varH,variance_endpoint_subtraction=prod-ep*ep,S=S,D=D,correction=cov/S,R_E=R,sharper_bound=bound))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384:raise RuntimeError('RSS')
print(json.dumps({'rss_mib':rss,'checks':checks,'count':len(checks),'tiny_exact':tiny,'L2':out,'seconds':time.monotonic()-start,'source_sha':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2,allow_nan=False))
