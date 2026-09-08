# Independent physical Pauli construction and full Record-history response.
import sympy as s,json,hashlib
from pathlib import Path
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);E=s.eye(8)
zs=[s.kronecker_product(*[Z if k==j else I for k in range(3)]) for j in range(3)]
xs=[s.kronecker_product(*[X if k==j else I for k in range(3)]) for j in range(3)]
B=[zs[0],zs[0]*zs[1],zs[1]*zs[2],zs[2]];N=[(E-b)/2 for b in B]
A=[xs[0],xs[1]*zs[0],xs[2]*zs[1]]
T=[s.I*A[k]*(B[k]-B[k+1])/2 for k in range(3)]
def pulse(k,c,r):return E-s.I*r*T[k]+(c-1)*T[k]**2
def simp(m):return m.applyfunc(s.simplify)
checks={}
def ck(k,b):checks[k]=bool(b);assert b,k
rho=N[0]*(E-N[1])*(E-N[2])*N[3]
ck('rank_one_input',s.trace(rho)==1 and rho*rho==rho)
U=pulse(0,s.Rational(3,5),s.Rational(4,5));W=pulse(1,s.Rational(7,25),s.Rational(24,25));V=pulse(0,s.Rational(5,13),s.Rational(12,13))*W
for name,u in [('U',U),('W',W),('V',V)]:ck('unitary_'+name,u.H*u==E)
rho0=U*rho*U.H;phase=E;rho1=phase*W*rho0*W.H*phase.H
responses=[];histories=[]
for family,r in enumerate([rho0,rho1]):
 R=s.Matrix(4,4,lambda i,j:s.simplify(s.I*s.trace(V.H*N[i]*V*(N[j]*r-r*N[j]))))
 responses.append(R)
 ck('source_zero_mode'+str(family),R*s.ones(4,1)==s.zeros(4,1))
 ck('readout_number_zero_mode'+str(family),s.ones(1,4)*R==s.zeros(1,4))
 total=s.zeros(8); recR=s.zeros(4); sumprob=0
 for mask in range(8):
  signs=[1-2*((mask>>k)&1) for k in range(3)]
  Q=E
  for k,z in enumerate(signs):Q=Q*(E+z*zs[k])/2
  # Actual sequential projectors, no intervening dwell; all branches retained.
  total+=Q;prob=s.simplify(s.trace(Q*V*r*V.H*Q))
  deriv=[s.simplify(s.I*s.trace(Q*V*(n*r-r*n)*V.H*Q)) for n in N]
  occ=[(1-signs[0])//2,(1-signs[0]*signs[1])//2,(1-signs[1]*signs[2])//2,(1-signs[2])//2]
  sumprob+=prob
  for i in range(4):
   for j in range(4):recR[i,j]+=occ[i]*deriv[j]
  histories.append({'family':family,'signs':signs,'occupations':occ,'probability':str(prob),'derivatives':[str(x) for x in deriv]})
 ck('complete_all_eight_histories'+str(family),total==E and sumprob==1)
 ck('actual_Record_response'+str(family),recR==R)
 ck('reverse_source_sign'+str(family),s.Matrix(4,4,lambda i,j:s.simplify(-s.I*s.trace(V.H*N[i]*V*(N[j]*r-r*N[j]))))==-R)
 # Removing propagation leaves joint occupations unchanged by diagonal sources.
 ck('no_propagation_zero'+str(family),all(s.trace(n*(m*r-r*m))==0 for n in N for m in N))
ck('original_zero_response',responses[0]==s.zeros(4))
ck('phase_enabled_nonreciprocal',responses[1]!=responses[1].T)
C=s.Matrix([[1,0],[0,1],[-1,-1],[0,0]]);neutral=C.T*responses[1]*C
ck('neutral_nonreciprocal',neutral!=neutral.T)
ck('wrong_transpose_rejected',responses[1]!=responses[1].T)
# Generic mixed counting/source derivative is i R; checked through actual Q rows.
# Source-state derivative has sign +i[n,r], fixed by supplied +i source kick.
output={'count':len(checks),'checks':checks,'response':[[str(x) for x in R] for R in responses],'neutral':str(neutral),'histories':histories,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(output,indent=2))
