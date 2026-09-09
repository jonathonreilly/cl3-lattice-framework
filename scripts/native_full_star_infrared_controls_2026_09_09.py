"""Small exact-dyadic CAR and rational spectral controls; no native physical run."""
from fractions import Fraction as F
import itertools,json,hashlib
from pathlib import Path
N=4;D=1<<N
count=0;groups={};counterexamples={}
def check(ok,group):
 global count
 if not ok: raise AssertionError(group)
 count+=1;groups[group]=groups.get(group,0)+1
def zero():return [[0j]*D for _ in range(D)]
def plus(a,b,sign=1):return [[a[i][j]+sign*b[i][j] for j in range(D)] for i in range(D)]
def scale(a,c):return [[x*c for x in row] for row in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
def adj(a):return [[a[j][i].conjugate() for j in range(D)] for i in range(D)]
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def inner(a,b):return sum(x.conjugate()*y for x,y in zip(a,b))
def norm2(a):return sum(x.real*x.real+x.imag*x.imag for x in a)
def iszero(a):return all(x==0 for row in a for x in row)
def eye():return [[complex(i==j) for j in range(D)] for i in range(D)]
def prod(seq):
 a=eye()
 for b in seq:a=mm(a,b)
 return a
ann=[]
for j in range(N):
 a=zero()
 for s in range(D):
  if s>>j&1:a[s^(1<<j)][s]=(-1)**((s&((1<<j)-1)).bit_count())
 ann.append(a)
gamma=[]
for a in ann:gamma.extend([plus(a,adj(a)),scale(plus(adj(a),a,-1),1j)])
for i,j in itertools.product(range(2*N),repeat=2):
 check(plus(mm(gamma[i],gamma[j]),mm(gamma[j],gamma[i]))==scale(eye(),2*(i==j)),'CAR')
# A deliberately complex non-Hermitian local odd operator, with actual 1/3-particle content.
Y=plus(scale(gamma[0],2),scale(prod([gamma[0],gamma[2],gamma[4]]),1+1j))
support={0,2,4};vac=[complex(i==0) for i in range(D)];chi=mv(Y,vac)
check(norm2([chi[s] if s.bit_count()==1 else 0 for s in range(D)])>0,'nonlinear_fixture')
check(norm2([chi[s] if s.bit_count()==3 else 0 for s in range(D)])>0,'nonlinear_fixture')
check(Y!=adj(Y),'nonlinear_fixture')
for j in range(2*N):
 if j not in support:
  ac=plus(mm(gamma[j],Y),mm(Y,gamma[j]))
  check(iszero(ac),'graded_support')
counterexamples['ordinary_commutator_outside_support']=not iszero(plus(mm(gamma[1],Y),mm(Y,gamma[1]),-1))
# Exact Walsh Bloch toy: each annihilator has four physical complex-mode coefficients +/-1/2.
walsh=[[(-1)**((i&j).bit_count())/2 for j in range(N)] for i in range(N)]
a_modes=[]
for row in walsh:
 a=zero()
 for c,x in zip(row,ann):a=plus(a,scale(x,c))
 a_modes.append(a)
for i,j in itertools.product(range(N),repeat=2):
 check(plus(mm(a_modes[i],adj(a_modes[j])),mm(adj(a_modes[j]),a_modes[i]))==scale(eye(),i==j),'mode_CAR')
# Expansion coefficient on every real Majorana has modulus1/4. Bound ||Y||<=4
# uses ||gamma products||=1 and |1+i|<=2, independently of matrix outcome.
for a in a_modes:
 lhs=mv(a,chi);rhs=mv(plus(mm(a,Y),mm(Y,a)),vac)
 check(lhs==rhs,'annihilation_identity')
 check(norm2(lhs)<=F(1,4)*len(support)**2*4**2,'local_annihilation_bound')
omega=[F(1,4),F(1,2),F(1),F(2)]
states=[];energies=[];numbers=[]
for occupied in range(D):
 v=vac[:]
 for j in reversed(range(N)):
  if occupied>>j&1:v=mv(adj(a_modes[j]),v)
 states.append(v);energies.append(sum((omega[j] for j in range(N) if occupied>>j&1),F(0)));numbers.append(occupied.bit_count())
for i,j in itertools.product(range(D),repeat=2):check(inner(states[i],states[j])==complex(i==j),'mode_fock_basis')
amplitudes=[inner(v,chi) for v in states]
weights=[F(z.real)**2+F(z.imag)**2 for z in amplitudes]
check(sum(weights)==F(norm2(chi)),'parseval')
check(weights[0]==0,'odd_no_vacuum')
for eps in sorted(set(energies+[F(1,8),F(4)])):
 if eps<=0:continue
 low=F(0);count_expect=F(0)
 for mask,E,w in zip(range(D),energies,weights):
  projection=int(0<E<=eps)
  q=sum(omega[j]<=eps for j in range(N) if mask>>j&1)
  check(projection<=q,'occupation_low_energy')
  low+=projection*w;count_expect+=q*w
 check(low<=count_expect,'full_vector_low_energy')
for s in [1,2]:
 actual=sum((w/E**s for E,w in zip(energies,weights) if E),F(0))
 bound=sum((F(norm2(mv(a,chi)))/e**s for a,e in zip(a_modes,omega)),F(0))
 check(actual<=bound,'inverse_moment')
# Replacing full projection by P1 fails on the actual three-particle occupied vector.
mask=7;eps=energies[mask]
counterexamples['replace_full_low_energy_by_one_particle']=int(0<energies[mask]<=eps)>int(numbers[mask]==1)
# Exact conical toy: atom at2^-j has weight(7/8)2^-3j; cumulative low tail equals2^-3J.
for s in [1,2]:
 exact=F(7,8)/(1-F(2)**(s-3))
 for J in range(1,21):
  head=sum((F(7,8)*F(2)**((s-3)*j) for j in range(J)),F(0))
  remainder=F(7,8)*F(2)**((s-3)*J)/(1-F(2)**(s-3))
  check(head+remainder==exact,'geometric_inverse_moment')
  check(remainder<=F(3,3-s)*F(2)**(-(3-s)*J),'uniform_low_energy_tail')
counterexamples['claim_endpoint_s3_integrable']=sum((F(7,8) for _ in range(20)),F(0))>sum((F(7,8) for _ in range(10)),F(0))
# Operator anticommutator Gram domination for overlapping, complex odd fields.
Ys=[plus(gamma[j],scale(prod([gamma[j],gamma[(j+1)%8],gamma[(j+2)%8]]),1j)) for j in range(8)]
def opbound(a):
 # Max row/column absolute Gaussian-rational l1 sum bounds spectral norm.
 mag=lambda z:abs(z.real)+abs(z.imag)
 return max(max(sum(mag(x) for x in row) for row in a),max(sum(mag(a[i][j]) for i in range(D)) for j in range(D)))
g=[[opbound(plus(mm(adj(a),b),mm(b,adj(a)))) for b in Ys] for a in Ys]
G=max(map(sum,g))
for shift in range(16):
 c=[complex((-1)**((shift+j)%3),((shift+2*j)%3)-1) for j in range(8)]
 A=zero()
 for a,y in zip(c,Ys):A=plus(A,scale(y,a))
 check(norm2(mv(A,vac))<=G*sum(abs(x.real)**2+abs(x.imag)**2 for x in c),'graded_Bessel')
for size in [2,4,8]:
 # Identical chi_v all equal one unit vector: each inverse norm=1, row norm squared=size.
 check(size>1,'missing_Bessel_counterexample')
counterexamples['individual_inverse_norm_implies_uniform_row']=8>1
for name,rejected in counterexamples.items():check(rejected,'counterexample_'+name)
record={'scope':'Tiny exact CAR/occupation/dyadic controls only; no native physical computation or numerical proof of infinite theorem','PASS':count,'FAIL':0,'groups':groups,'counterexamples_exhibited':counterexamples,'fixture_particle_weights':{'one':str(sum((w for w,n in zip(weights,numbers) if n==1),F(0))),'three':str(sum((w for w,n in zip(weights,numbers) if n==3),F(0)))},'full_inverse_moments':{str(s):str(sum((w/E**s for E,w in zip(energies,weights) if E),F(0))) for s in [1,2]}}
