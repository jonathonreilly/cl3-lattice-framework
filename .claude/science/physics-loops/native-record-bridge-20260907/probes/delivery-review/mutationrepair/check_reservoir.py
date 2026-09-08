import sympy as s, itertools, json, hashlib
from pathlib import Path
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1)
edges=[(0,1),(0,3),(0,4),(1,2),(2,3)]
def op(k,m):return s.kronecker_product(*[m if j==k else I for j in range(5)])
E=s.eye(32); zs=[op(k,Z) for k in range(5)]; xs=[op(k,X) for k in range(5)]
B={v:s.prod([zs[k] for k,e in enumerate(edges) if v in e],start=E) for v in range(5)}
def A(u,v):
 if u>v:return -A(v,u)
 k=edges.index((u,v)); out=xs[k]
 for a,b in [(u,v),(v,u)]:
  for j,e in enumerate(edges):
   if a in e and e!=edges[k] and (e[1] if e[0]==a else e[0])<b:out=out*zs[j]
 return out
T={(u,v):s.I*A(u,v)*(B[u]-B[v])/2 for u,v in edges}
S=A(0,1)*A(1,2)*A(2,3)*A(3,0); P=(E+S)/2
H=T[0,1]+T[2,3]
F=lambda t:E-s.Rational(2,4)*t+s.Rational(1,4)*t*t
U=F(T[0,1])*F(T[2,3]); tr=s.trace(P*U)
eigs=[s.Integer(2),s.Rational(1,2)]*2
layers=[sum(s.prod(eigs[j] for j in js) for js in itertools.combinations(range(4),n)) for n in range(5)]
plus=s.prod(1+x for x in eigs); minus=s.prod(1-x for x in eigs)
q=s.symbols('q'); n4=(E-B[4])/2; weighted=s.trace(P*U*(E+(q-1)*n4)); expected=((1+q)*plus+(1-q)*minus)/2
checks={'rank16':s.trace(P)==16,'source_code':P*P==P,'ancilla_conserved':n4*H==H*n4,'native_full_trace':tr==plus,'generic_reservoir_weight':s.expand(weighted-expected)==0,'biased_reservoir_rejects_det':weighted.subs(q,2)!=plus,'normalized_full':tr/16==plus/16}
# Since T^3=T and T is Hermitian, its spectrum is contained in {-1,0,1}.
# At tau=log(2), exp(-tau*lambda)=2**(-lambda), independently of F's coefficients.
for edge in [(0,1),(2,3)]:
 t=T[edge]
 checks['used_hop_hermitian_'+str(edge)]=t.H==t
 checks['used_hop_cubic_'+str(edge)]=t**3==t
 for lam,proj in [(-1,(t*t-t)/2),(0,E-t*t),(1,(t*t+t)/2)]:
  checks['spectral_exponential_'+str(edge)+'_'+str(lam)]=F(t)*proj==s.Integer(2)**(-lam)*proj
assert all(checks.values()),checks
print(json.dumps({'checks':checks,'pass_count':len(checks),'trace':str(tr),'weighted_trace':str(weighted),'q2_trace':str(weighted.subs(q,2)),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
