import sympy as s,json
r=s.Rational(3,5);basis=[(0,0,1),(1,0,0),(0,1,0),(1,1,1)];I=s.eye(4);n=[s.diag(*[b[j]for b in basis])for j in range(3)];t=s.zeros(4);t[1,2]=t[2,1]=1;D=n[0]-n[1];c=s.sqrt(2)/2;U=I+(c-1)*t*t-s.I*c*t;R=I+(c-1)*D*D-s.I*c*D;W=R*U
H=t+2*n[0]*n[1];K=s.simplify(W*s.diag(*[r**(2*b[0]+b[2])for b in basis])*W.H);pm=(t*t-t)/2;pp=(t*t+t)/2;pz=I-t*t;target=pm+r*r*pp+r*pz+(r**3-r)*n[0]*n[1]
checks={'restricted_identity':n[0]*n[1]==(sum(n,s.zeros(4))-I)/2,'W_mapping':s.simplify(W*D*W.H)==t,'complete_K':K==target,'energy_spectrum':sorted(H.eigenvals().keys())==[-1,0,1,2]}
p=s.trace(K.H*K)/4;energy=s.simplify(s.trace(K.H*H*K)/(4*p));kin=s.simplify(s.trace(K.H*t*K)/(4*p));checks.update(probability=p==s.Rational(6001,15625),energy=energy==-s.Rational(6071,12002),kinetic=kin==-s.Rational(200,353))
assert all(checks.values());print(json.dumps({'checks':checks,'probability':str(p),'energy':str(energy),'kinetic':str(kin)},indent=2))
