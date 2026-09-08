import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sympy as s, json, hashlib
from pathlib import Path
checks={}
def ck(k,b):
 checks[k]=bool(b)
 assert b,k
# Independent occupation basis, all even configurations. No author imports.
basis=[x for x in range(64) if x.bit_count()%2==0]; ix={x:i for i,x in enumerate(basis)}; E=s.eye(32)
def n(v):return s.diag(*[(x>>v)&1 for x in basis])
def hop(i,j):
 out=s.zeros(32)
 for col,x in enumerate(basis):
  for a,b in [(i,j),(j,i)]:
   if (x>>b)&1 and not((x>>a)&1):
    y=x^(1<<b); phase=(-1)**((x&((1<<b)-1)).bit_count())
    phase*=(-1)**((y&((1<<a)-1)).bit_count()); y^=1<<a
    out[ix[y],col]+=phase
 return out
edges=[(0,1),(0,3),(0,4),(1,2),(2,3),(4,5)]
T={e:hop(*e) for e in edges}; Pin=E-n(5)
# Physical conjugation becomes sublattice parity times ordinary conjugation.
D=s.diag(*[(-1)**sum((x>>v)&1 for v in []) for x in basis])
for e,h in T.items():
 ck('hermitian'+str(e),h.H==h);ck('antiunitary_flip'+str(e),D*h.conjugate()*D==-h)
t=T[4,5];c=s.Rational(3,5);b=s.Rational(4,5);q=c*c
U=E-s.I*b*t+(c-1)*t*t;Q0=E-n(5);Q1=n(5)
ck('full_filter',Q0*U*Pin==(E+(c-1)*n(4))*Pin)
ck('full_failure',Q1*U*Pin==-s.I*b*t*Pin)
ck('completeness',Pin*U.H*(Q0+Q1)*U*Pin==Pin)
ck('wrong_q_amplitude_rejected',Q0*U*Pin!=(E+(q-1)*n(4))*Pin)
ck('erase_failure_rejected',Q1*U*Pin!=s.zeros(32))
H=T[0,1]+2*T[1,2]+3*T[2,3]+4*T[0,3]
ck('disjoint_matter_commutes',H*t==t*H)
rows=[]
for fam in [0,1]:
 v=s.zeros(32,1);v[ix[5]]=1
 pairs=[(3,5,4),(3,5,4) if fam==0 else (5,13,12),(5,13,12),(7,25,24),(20,29,21),(3,5,4)]
 for e,(a,d,b) in zip([(0,4),(0,1),(1,2),(2,3),(0,3),(0,4)],pairs):
  h=T[e]; V=E-s.I*s.Rational(b,d)*h+(s.Rational(a,d)-1)*h*h
  v=V*v
 ck('state_norm'+str(fam),(v.H*v)[0]==1)
 rho=v*v.H;ck('real_structure'+str(fam),D*rho.conjugate()*D==rho)
 p=(v.H*n(4)*v)[0]; w=Q0*U*v; success=(w.H*w)[0]; posterior=(w.H*n(4)*w)[0]/success
 ck('born_success'+str(fam),success==1-(1-q)*p)
 ck('born_posterior'+str(fam),posterior==q*p/success)
 rows.append(dict(family=fam,p=str(p),success=str(success),posterior=str(posterior)))
h=T[0,1];k=T[2,3];G=Pin*(E-s.Rational(3,4)*h+s.Rational(1,4)*h*h)*(E-s.Rational(15,8)*k+s.Rational(9,8)*k*k)
z=s.trace(G);mean=s.trace((h+2*k)*G)/z
ck('gibbs_trace',z==s.Rational(225,8));ck('gibbs_energy',mean==-s.Rational(23,15))
ck('gibbs_not_in_real_structure',D*G.conjugate()*D!=G)
ck('phase_escape',D*(E+(s.I-1)*n(4)).conjugate()*D!=E+(s.I-1)*n(4))
# Actual physical midpoint separation, not virtual adjacency.
points={0:(0,0),1:(1,0),2:(1,1),3:(0,1),4:(-1,0),5:(-2,0)}
mid={e:tuple(points[e[0]][a]+points[e[1]][a] for a in range(2)) for e in edges}
ck('leaf_support_distance_two',sum(abs(a-b) for a,b in zip(mid[4,5],mid[0,4]))==2)
print(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,count=len(checks),rows=rows,z=str(z),mean=str(mean)),indent=2))
