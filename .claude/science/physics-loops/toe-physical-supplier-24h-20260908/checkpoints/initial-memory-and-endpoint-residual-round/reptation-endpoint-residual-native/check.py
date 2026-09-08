import time,signal,resource,json,sys
start=time.monotonic();signal.alarm(180)
import sympy as s
from itertools import product
A=s.Matrix([[0,1,0],[1,0,2],[0,2,0]]);N=s.diag(1,3,2);H=s.Rational(3,4)*N-A;G=s.eye(3)-H/4;one=s.ones(3,1);h=H*one
checks=0

def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('exact identity failed')
req(all(x>=0 for x in G));rows=[]
for n in (2,4,6):
 psi=G**(n//2)*one;Z=(psi.T*psi)[0];E=(psi.T*H*psi)[0]/Z;VH=(psi.T*H*H*psi)[0]/Z-E**2
 for obs in ([s.Matrix([0,1+s.I,2-s.I])],[s.Matrix([0,1+s.I,2-s.I]),s.Matrix([1,0,s.I])],[one]):
  X=s.Matrix([sum(s.expand_complex(s.conjugate(o[i])*o[i]) for o in obs) for i in range(3)])
  totals=[s.S(0)]*6
  for path in product(range(3),repeat=n+1):
   w=s.prod(G[path[j],path[j+1]] for j in range(n))/Z
   vals=[h[path[0]],h[path[0]]*h[path[-1]],X[path[n//2]]*(h[path[0]]+h[path[-1]])/2,X[path[n//2]],X[path[n//2]]**2,h[path[n//2]]**2]
   totals=[a+w*b for a,b in zip(totals,vals)]
  S=totals[3];C=totals[2]-S*E;VX=totals[4]-S**2
  req(totals[0]==E);req(totals[1]-E**2==VH);req(totals[2]==(psi.T*s.diag(*X)*H*psi)[0]/Z)
  D=sum(A[x,y]*psi[x]*psi[y]*sum(s.expand_complex(s.conjugate(o[x]-o[y])*(o[x]-o[y])) for o in obs) for x in range(3) for y in range(3))/(2*Z*S)
  R=sum(((s.diag(*o)*psi).conjugate().T*(H-E*s.eye(3))*(s.diag(*o)*psi))[0] for o in obs)/(Z*S)
  req(s.simplify(R-D-C/S)==0);req(s.simplify(VX*VH-C**2)>=0)
  if len(obs)==1 and obs[0]==one:req(C==0 and R==0 and D==0)
  else:req(C!=0);req(totals[5]!=(psi.T*H*H*psi)[0]/Z)
  rows.append(dict(n=n,modes=len(obs),constant=obs[0]==one,E=str(E),variance_H=str(VH),D=str(D),R=str(s.simplify(R)),correction=str(C/S)))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
print(json.dumps(dict(checks=checks,rows=rows,seconds=time.monotonic()-start,peak_MiB=rss),indent=2))
