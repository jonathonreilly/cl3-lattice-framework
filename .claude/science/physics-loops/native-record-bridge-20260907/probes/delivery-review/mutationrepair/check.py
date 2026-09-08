import sympy as s, itertools, json, hashlib
from pathlib import Path
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1)
edges=[(0,1),(0,3),(1,2),(2,3)]
def op(k,m):return s.kronecker_product(*[m if j==k else I for j in range(4)])
E=s.eye(16); zs=[op(k,Z) for k in range(4)]; xs=[op(k,X) for k in range(4)]
B={v:s.prod([zs[k] for k,e in enumerate(edges) if v in e],start=E) for v in range(4)}
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
checks={
 'cycle_involution':S*S==E,'cycle_hermitian':S.H==S,'code_rank8':s.trace(P)==8,
 'projector':P*P==P,'code_hop_commute':P*H==H*P,
 'all_hop_cubics':all(t**3==t for t in T.values()),
 'disjoint_commute':T[0,1]*T[2,3]==T[2,3]*T[0,1],
 'even_native_trace':tr==sum(layers[::2]),
 'parity_projected_determinants':tr==(plus+minus)/2,
 'full_trace_layers':plus==sum(layers),'odd_trace':sum(layers[1::2])==(plus-minus)/2,
 'normalized_full_candidate_rejected':tr/8!=plus/16,
 'fixedN2_candidate_distinct':layers[2]/6!=tr/8,
 'vacuum_candidate_distinct':layers[0]!=tr/8,
 'independent_copy_changes_trace':tr*tr!=tr,
 'nonzero_parity_twist':minus!=0,
 'tau0_normalization':sum(1 for n in range(5) for _ in itertools.combinations(range(4),n) if n%2==0)==8,
}
# Since T^3=T and T is Hermitian, its spectrum is contained in {-1,0,1}.
# At tau=log(2), exp(-tau*lambda)=2**(-lambda), independently of F's coefficients.
for edge in [(0,1),(2,3)]:
 t=T[edge]
 checks['used_hop_hermitian_'+str(edge)]=t.H==t
 checks['used_hop_cubic_'+str(edge)]=t**3==t
 for lam,proj in [(-1,(t*t-t)/2),(0,E-t*t),(1,(t*t+t)/2)]:
  checks['spectral_exponential_'+str(edge)+'_'+str(lam)]=F(t)*proj==s.Integer(2)**(-lam)*proj
assert all(checks.values()), checks
out={'scope':'Exact conditional native-code closure algebra, no physical measure or formation law supplied','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'pass_count':len(checks),'values':{k:str(v) for k,v in {'native_even_trace':tr,'full_trace':plus,'parity_twisted_trace':minus,'native_normalized':tr/8,'full_normalized':plus/16,'fixedN2_normalized':layers[2]/6,'independent_copy_trace':tr*tr}.items()},'particle_layers':list(map(str,layers))}
print(json.dumps(out,indent=2,allow_nan=False))
