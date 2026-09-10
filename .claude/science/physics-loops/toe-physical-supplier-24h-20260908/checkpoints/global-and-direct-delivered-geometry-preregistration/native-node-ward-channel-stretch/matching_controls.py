from fractions import Fraction as F
import json
# Clifford mask and i-parity; coefficients real rational, i²=-1.
def add(*xs):
 o={}
 for x in xs:
  for k,v in x.items():o[k]=o.get(k,F(0))+v
 return {k:v for k,v in o.items() if v}
def scale(x,a):return {k:v*a for k,v in x.items() if v*a}
def mul(x,y):
 o={}
 for (a,i),v in x.items():
  for (b,j),w in y.items():
   swaps=sum((b&((1<<k)-1)).bit_count() for k in range(3) if a>>k&1)
   k=(a^b,(i+j)%2);o[k]=o.get(k,F(0))+v*w*(-1)**(swaps+(i+j)//2)
 return {k:v for k,v in o.items() if v}
def comm(x,y):return add(mul(x,y),scale(mul(y,x),-1))
def product(*xs):
 out=one
 for x in xs:out=mul(out,x)
 return out
one={(0,0):F(1)};g=[{(1<<i,0):F(1)} for i in range(3)]
P={(3,1):F(1)};Q={(6,1):F(1)};u=-F(3,5);z=F(4,5)
H=add(scale(P,u),scale(Q,z));D0=add(one,H)
def expect(x):
 v=mul(add(one,scale(H,-1)),x)
 if v.get((0,1),0):raise AssertionError('imaginary expectation')
 return v.get((0,0),F(0))
checks=0
def ok(x):
 global checks
 if not x:raise AssertionError('Clifford identity')
 checks+=1
ok(mul(H,H)==one)
ts=[F(1,5),F(2,5),F(3,5)];Ds=[];Rs=[];Ws=[];Js=[];Vs=[]
for t in ts:
 a=u+t;det=1-a*a-z*z;ok(det>0)
 D=add(one,scale(P,a),scale(Q,z));R=scale(add(one,scale(P,-a),scale(Q,-z)),-1/det)
 W=add(scale(g[0],2),scale(g[2],(2*u+3*t)/z));J={(2,1):2*t};V=add(W,scale(g[0],-2))
 ok(mul(D,R)==scale(one,-1));ok(comm(W,D)==scale(J,-1));ok(add(mul(W,g[0]),mul(g[0],W))==scale(one,4))
 Ds.append(D);Rs.append(R);Ws.append(W);Js.append(J);Vs.append(V)
ok(add(*Ws)==scale(g[0],6));ok(add(*Vs)=={})
for V in Vs:
 for t in ts:ok(comm(V,scale(P,t))=={})
ok(add(*Ds)==add(scale(D0,2),product(g[0],D0,g[0])))
direct=correction=tail=F(0)
for a in range(3):
 for c in range(3):
  if a==c:continue
  RA,RC=Rs[a],Rs[c]
  direct+=expect(product(RC,RA))
  correction+=F(1,2)*(expect(product(RC,Js[c],RC,g[0],RA))-expect(product(RC,g[0],RA,Js[a],RA)))
  FC=comm(RC,Vs[c]);FA=comm(RA,Vs[a])
  tail+=F(1,2)*(expect(product(FC,g[0],RA))-expect(product(RC,g[0],FA)))
ok(correction!=0);ok(tail==0)
print(json.dumps({'status':'PASS','checks':checks,'scope':'nonnative finite Clifford matching falsifier of exact cancellation only','direct':str(direct),'full_Ward_correction':str(correction),'centerless_tail_correction':str(tail),'matching_soft_sum':str(direct+correction),'native_alpha_evaluated':False},indent=2))
