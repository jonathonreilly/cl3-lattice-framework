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
   swaps=sum((b&((1<<k)-1)).bit_count() for k in range(8) if a>>k&1)
   k=(a^b,(i+j)%2);o[k]=o.get(k,F(0))+v*w*(-1)**(swaps+(i+j)//2)
 return {k:v for k,v in o.items() if v}
def comm(x,y):return add(mul(x,y),scale(mul(y,x),-1))
def product(*xs):
 out=one
 for x in xs:out=mul(out,x)
 return out
one={(0,0):F(1)};g=[{(1<<i,0):F(1)} for i in range(8)]
def imag(x):return {(m,(j+1)%2):v*(-1)**j for (m,j),v in x.items()}
checks=0
def ok(x):
 global checks
 if not x:raise AssertionError('Clifford identity')
 checks+=1
def solve(A,b):
 rows=[list(r)+[v] for r,v in zip(A,b)];n=len(A[0]);piv=[];r=0
 for c in range(n):
  k=next((k for k in range(r,len(rows)) if rows[k][c]),None)
  if k is None:continue
  rows[r],rows[k]=rows[k],rows[r];v=rows[r][c];rows[r]=[x/v for x in rows[r]]
  for k in range(len(rows)):
   if k!=r and rows[k][c]:
    v=rows[k][c];rows[k]=[x-v*y for x,y in zip(rows[k],rows[r])]
  piv.append((r,c));r+=1
 for row in rows:ok(any(row[:-1]) or row[-1]==0)
 out=[F(0)]*n
 for r,c in piv:out[c]=rows[r][-1]
 return out
white=[0,2,4,6];black=[1,3,5]
M=[[F(v,2) for v in r] for r in ((1,1,1),(1,-1,1),(1,1,-1),(1,-1,-1))]
def ham(M):return add(*(scale(imag(mul(g[white[i]],g[black[j]])),M[i][j]) for i in range(4) for j in range(3)))
Pj=[ham([[M[i][j] if k==j else F(0)for k in range(3)]for i in range(4)])for j in range(3)]
for P in Pj:ok(mul(P,P)==one)
for i in range(3):
 for j in range(i):ok(comm(Pj[i],Pj[j])=={})
H0=add(*Pj);D0=add(scale(one,3),H0);density=product(*(add(one,scale(P,-1))for P in Pj))
def expect(x):
 v=mul(density,x);ok(v.get((0,1),0)==0);return v.get((0,0),F(0))
Ds=[];Rs=[];Ws=[];Js=[];Vs=[];Bs=[]
for a in range(3):
 b=[F(j==a,2)for j in range(3)];Mt=[r[:]for r in M];Mt[0]=[M[0][j]-2*b[j]for j in range(3)]
 H=ham(Mt);D=add(scale(one,3),H)
 # The Gram has trace3 and is not I. Positive principal minors and strict sqrt concavity prove sum singular values<3.
 gram=[[sum(Mt[k][i]*Mt[k][j]for k in range(4))for j in range(3)]for i in range(3)]
 det=(gram[0][0]*(gram[1][1]*gram[2][2]-gram[1][2]*gram[2][1])-gram[0][1]*(gram[1][0]*gram[2][2]-gram[1][2]*gram[2][0])+gram[0][2]*(gram[1][0]*gram[2][1]-gram[1][1]*gram[2][0]))
 ok(sum(gram[i][i]for i in range(3))==3 and det>0 and gram[0][0]*gram[1][1]-gram[0][1]**2>0 and gram!=[[F(i==j)for j in range(3)]for i in range(3)])
 powers=[];t=one
 for k in range(8):t=mul(D,t);powers.append(t)
 keys=sorted(set().union(*(set(t)for t in powers),set(one)))
 coeff=solve([[t.get(key,F(0))for t in powers]for key in keys],[one.get(key,F(0))for key in keys])
 R={};t=one
 for c in coeff:R=add(R,scale(t,-c));t=mul(D,t)
 ok(mul(D,R)==scale(one,-1))
 tail=solve([[M[i][j]for i in range(1,4)]for j in range(3)],[b[j]-M[0][j]/3 for j in range(3)])
 V=add(*(scale(g[white[i+1]],6*tail[i])for i in range(3)));W=add(scale(g[0],2),V);B=add(D,scale(D0,-1));J=scale(imag(add(*(scale(g[black[j]],b[j])for j in range(3)))),-4)
 ok(comm(W,D)==scale(J,-1));ok(mul(B,B)==one)
 Ds.append(D);Rs.append(R);Ws.append(W);Js.append(J);Vs.append(V);Bs.append(B)
ok(add(*Ws)==scale(g[0],6));ok(add(*Vs)=={});ok(add(*Ds)==add(scale(D0,2),product(g[0],D0,g[0])))
for i in range(3):
 for j in range(i):ok(add(mul(Bs[i],Bs[j]),mul(Bs[j],Bs[i]))=={})
for V in Vs:
 for B in Bs:ok(comm(V,B)=={})
direct=correction=tail=F(0)
for a in range(3):
 for c in range(3):
  if a==c:continue
  RA,RC=Rs[a],Rs[c];direct+=expect(product(RC,RA))
  correction+=F(1,2)*(expect(product(RC,Js[c],RC,g[0],RA))-expect(product(RC,g[0],RA,Js[a],RA)))
  tail+=F(1,2)*(expect(product(comm(RC,Vs[c]),g[0],RA))-expect(product(RC,g[0],comm(RA,Vs[a]))))
print(json.dumps({'status':'PASS_IDENTITIES','checks':checks,'scope':'nonnative8-Majorana Clifford-triple matching','direct':str(direct),'full_Ward_correction':str(correction),'centerless_tail_correction':str(tail),'tail_zero':tail==0,'native_alpha_evaluated':False},indent=2))
