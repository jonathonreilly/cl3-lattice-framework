import sympy as s,json,hashlib
from pathlib import Path
I=s.eye(2);Z=s.diag(1,-1);Y=s.Matrix([[0,-s.I],[s.I,0]]);Id=s.eye(8)
def op(a,k):return s.kronecker_product(*[a if j==k else I for j in range(3)])
z=[op(Z,k) for k in range(3)];T=[op(Y,0)*(Id-z[1])/2,op(Y,1)*(Id-z[0]*z[2])/2,op(Y,2)*(Id-z[1])/2];B=[z[0],z[0]*z[1],z[1]*z[2],z[2]];n=[(Id-b)/2 for b in B]
def basis(bits):
 # Incidence inversion: edge bits are prefix occupation parity.
 edges=[sum(bits[:j+1])%2 for j in range(3)];idx=4*edges[0]+2*edges[1]+edges[2];return Id[:,idx]
Vin=s.Matrix.hstack(*[basis([int(a==0),int(b==0),int(a==1),int(b==1)]) for a in [0,1] for b in [0,1]])
Vout=s.Matrix.hstack(*[basis([int(a==0),int(a==1),int(b==0),int(b==1)]) for a in [0,1] for b in [0,1]])
def U(k,c,v):return Id+(c-1)*T[k]**2-s.I*v*T[k]
def eq(a,b):return all(s.simplify(x)==0 for x in a-b)
c=s.sqrt(2)/2;S=U(1,0,1);GA=S*U(0,c,c)*S.H;GB=S.H*U(2,c,c)*S;psi=GB*GA*basis([1,1,0,0]);Q=(Id-z[1])/2;K=s.diag(0,1,1,0);post=Q*psi;bell=Vout*s.Matrix([0,1,1,0])/s.sqrt(2);R=U(2,c,c)*U(0,c,c)
checks={}
def ck(k,b):
 if not b:raise AssertionError(k)
 checks[k]=True
ck('fullcomplex_K',eq(Q*Vin,Vout*K));ck('fullcomplex_input',eq(psi,Vin*s.ones(4,1)/2));ck('fullcomplex_output',eq(post,bell/s.sqrt(2)));ck('full_input_complete',eq(Vin.H*(Q+(Id-Q))*Vin,s.eye(4)))
ck('ownrail_preservation',eq(GA*(n[0]+n[2]),(n[0]+n[2])*GA) and eq(GB*(n[1]+n[3]),(n[1]+n[3])*GB))
ck('unitaries',eq(GA.H*GA,Id) and eq(GB.H*GB,Id));ck('probhalf',s.simplify((post.H*post)[0])==s.Rational(1,2))
Zobs=Vout.H*z[0]*z[2]*Vout;Xobs=s.simplify(Vout.H*R.H*z[0]*z[2]*R*Vout);XX=s.kronecker_product(s.Matrix([[0,1],[1,0]]),s.Matrix([[0,1],[1,0]]));ZZ=s.kronecker_product(Z,Z)
ck('bare_ZZ_sign',eq(Zobs,-ZZ));ck('rotated_XX_exact',eq(Xobs,XX));ck('oldrecord_permanent',eq(R*z[1],z[1]*R))
W=Zobs+Xobs;v=s.Matrix([0,1,1,0])/s.sqrt(2);ck('witness2',s.simplify((v.H*W*v)[0])==2);ck('witness_spectrum',sorted(W.eigenvals().keys())==[-2,0,2])

Vfail=s.Matrix.hstack(basis([1,1,0,0]),basis([0,0,1,1]));Kplus=s.Matrix([[1,0,0,0],[0,0,0,1]])
ck('exact_full_failure_columns',eq((Id-Q)*Vin,Vfail*Kplus) and eq(K.H*K+Kplus.H*Kplus,s.eye(4)))
def obs(k,t):
 a=U(k,s.cos(t),s.sin(t));return s.simplify(a.H*z[k]*a)
AA=[obs(0,0),obs(0,s.pi/4)];BB=[obs(2,s.pi/8),obs(2,-s.pi/8)]
CC=s.Matrix([[s.simplify((bell.H*a*b*bell)[0]) for b in BB] for a in AA])
ck('exact_CHSH_matrix',eq(CC,s.Matrix([[1,1],[1,-1]])/s.sqrt(2)))
ck('exact_CHSH_local_commutation',all(eq(a*b,b*a) for a in AA for b in BB))
result={'status':'PASS','checks':checks,'input_complex':[str(x) for x in Vin.H*psi],'K_complex':[[str(K[i,j]) for j in range(4)] for i in range(4)],'Kplus':[[str(Kplus[i,j]) for j in range(4)] for i in range(2)],'CHSH_exact':[[str(x) for x in CC.row(i)] for i in range(2)],'witness_eigenvalues':{str(k):v for k,v in W.eigenvals().items()},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
root=Path(__file__).resolve().parents[1]
(root/'outputs'/'native_parity_entangler_exact_2026_09_08.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps(result,allow_nan=False))
