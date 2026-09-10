from fractions import Fraction as F
import json,time
import append_core as core, interval as iv,binder
start=time.monotonic();n=0

def require(x):
 global n
 if not x:raise ValueError('synthetic check')
 n+=1

def has(ivalue,q):return F(ivalue[0],iv.S)<=q<=F(ivalue[1],iv.S)
for orbit in core.ORBITS:
 I,O,T,N=core.geometry(orbit)
 for s in (F(1,128),F(2,3),F(16)):
  A,B,c=F(2,13),F(3,11),F(4,9);D=(1-s*s*A)/6
  for sig in(-1,1):
   for i in range(3):
    for v in range(3):
     g,j=core.cross(i,v,s,sig,A,B,c,orbit,iv.ONE)
     if i==0:
      exact_g=(sig*s*A*I[0][v]+D*T[0][v])/2
      exact_j=(B*I[0][v]-sig*s*B*T[0][v]/6)/2
     else:
      exact_g=(-(A*N[i][v]-D*O[i][v])+sig*s*A*T[i][v]/6)/2
      exact_j=(B*T[i][v]/6+sig*((c-B)*N[i][v]/s-s*B*O[i][v]/6))/2
     require(has(g,exact_g));require(has(j,exact_j))
     rev=core.cross(i,v,s,-sig,A,B,c,orbit,iv.ONE);chi=1 if v==0 else -1
     require(has(rev[0],-chi*exact_g));require(has(rev[1],chi*exact_j))
 for i in range(3):
  for j in range(3):
   g,z=core.self_entry(i,j,F(1,4),orbit)
   require((g,z)==core.self_entry(j,i,F(1,4),orbit));require(z==iv.ZERO)
try:binder.load({'status':'NOTREADY'})
except ValueError:require(True)
else:require(False)
require(5*(3*396+6)==5970);require(5*(3*132+3)==1995)
print(json.dumps({'status':'PASS','predicates':n,'seconds':time.monotonic()-start,'scope':'tiny synthetic midpoint containment only','native_calls':0,'full_mock_calls':0},indent=2))
