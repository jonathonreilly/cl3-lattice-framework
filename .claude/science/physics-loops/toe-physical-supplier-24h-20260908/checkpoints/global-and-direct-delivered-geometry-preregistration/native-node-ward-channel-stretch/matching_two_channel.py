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
   swaps=sum((b&((1<<k)-1)).bit_count() for k in range(6) if a>>k&1)
   k=(a^b,(i+j)%2);o[k]=o.get(k,F(0))+v*w*(-1)**(swaps+(i+j)//2)
 return {k:v for k,v in o.items() if v}
def comm(x,y):return add(mul(x,y),scale(mul(y,x),-1))
def product(*xs):
 out=one
 for x in xs:out=mul(out,x)
 return out
one={(0,0):F(1)};g=[{(1<<i,0):F(1)} for i in range(6)]
def imag(x):
 return {(mask,(j+1)%2):v*(-1)**j for (mask,j),v in x.items()}
checks=0
def ok(x):
 global checks
 if not x:raise AssertionError('Clifford identity')
 checks+=1
white=[0,2,4];black=[1,3]
M=[[F(3,5),F(12,25)],[F(4,5),-F(9,25)],[F(0),F(4,5)]]
def hamiltonian(M):
 return add(*(scale(imag(mul(g[white[i]],g[black[j]])),M[i][j]) for i in range(3) for j in range(2)))
Pj=[hamiltonian([[M[i][j] if k==j else F(0) for k in range(2)] for i in range(3)])for j in range(2)]
ok(mul(Pj[0],Pj[0])==one);ok(mul(Pj[1],Pj[1])==one);ok(comm(*Pj)=={})
H0=add(*Pj);D0=add(scale(one,2),H0);density=mul(add(one,scale(Pj[0],-1)),add(one,scale(Pj[1],-1)))
def expect(x):
 v=mul(density,x)
 if v.get((0,1),0):raise AssertionError('imaginary expectation')
 return v.get((0,0),F(0))
grow=M[0];e=F(1,100);ds=[(e,F(0)),(F(0),e),(-e,-e)];bs=[[grow[j]/3+d[j]for j in range(2)]for d in ds]
Ds=[];Rs=[];Ws=[];Js=[];Vs=[]
for b,d in zip(bs,ds):
 Mt=[row[:] for row in M];Mt[0]=[grow[j]-2*b[j]for j in range(2)]
 H=hamiltonian(Mt);D=add(scale(one,2),H)
 S=sum(v*v for row in Mt for v in row);aa=sum(row[0]**2 for row in Mt);bb=sum(row[1]**2 for row in Mt);ab=sum(row[0]*row[1] for row in Mt);prod=aa*bb-ab*ab;den=(4-S)**2-4*prod
 ok(4-S>0 and den>0 and prod>0)
 R=scale(product(add(scale(one,2),scale(H,-1)),add(scale(one,4-2*S),mul(H,H))),-1/den)
 ok(mul(D,R)==scale(one,-1))
 # C^T tail=d with C=[[4/5,-9/25],[0,4/5]].
 t0=d[0]*F(5,4);t1=(d[1]+F(9,25)*t0)*F(5,4)
 V=add(scale(g[2],6*t0),scale(g[4],6*t1));W=add(scale(g[0],2),V)
 J=scale(imag(add(*(scale(g[black[j]],b[j])for j in range(2)))),-4)
 ok(comm(W,D)==scale(J,-1));ok(add(mul(W,g[0]),mul(g[0],W))==scale(one,4))
 Ds.append(D);Rs.append(R);Ws.append(W);Js.append(J);Vs.append(V)
ok(add(*Ws)==scale(g[0],6));ok(add(*Vs)=={});ok(add(*Ds)==add(scale(D0,2),product(g[0],D0,g[0])))
for V in Vs:
 for D in Ds:ok(comm(V,add(D,scale(D0,-1)))=={})
direct=correction=tail=F(0)
for a in range(3):
 for c in range(3):
  if a==c:continue
  RA,RC=Rs[a],Rs[c];direct+=expect(product(RC,RA))
  correction+=F(1,2)*(expect(product(RC,Js[c],RC,g[0],RA))-expect(product(RC,g[0],RA,Js[a],RA)))
  tail+=F(1,2)*(expect(product(comm(RC,Vs[c]),g[0],RA))-expect(product(RC,g[0],comm(RA,Vs[a]))))
print(json.dumps({'status':'PASS_IDENTITIES','checks':checks,'scope':'nonnative two-channel exact Clifford matching','direct':str(direct),'full_Ward_correction':str(correction),'centerless_tail_correction':str(tail),'tail_zero':tail==0,'native_alpha_evaluated':False},indent=2))
