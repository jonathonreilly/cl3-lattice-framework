from fractions import Fraction as F
from pathlib import Path
import json,time,signal,resource,sys
signal.alarm(180);start=time.monotonic();count=0

def need(x,m):
 global count
 if not x:raise RuntimeError(m)
 count+=1

def extract(edges,bits):
 vertices=set(sum(([a,b] for a,b in edges),[]));size=1<<len(edges)
 en=[sum(sum((1-2*bits[e]) for e,ab in enumerate(edges) if v in ab and z>>e&1)**2 for v in vertices) for z in range(size)]
 P=[z for z in range(size) if en[z]==0];need(len(P)==2,'rank two')
 def moves(z):
  for e,ab in enumerate(edges):
   # Reverse active ordering; compare ratios to the corresponding B, not basis entries.
   sign=(-1)**sum((z>>f)&1 for f in range(e+1,len(edges)) if set(ab)&set(edges[f]))
   yield z^(1<<e),sign
 def resolvent(vec):
  out={}
  for (z,p),v in vec.items():
   if en[z]==0: terms=[(p-1,v)]
   else:terms=[(p+k,-v/F(en[z]**(k+1))) for k in range(7-p) ]
   for exp,x in terms:
    if -7<=exp<=6:out[z,exp]=out.get((z,exp),F(0))+x
  return {k:v for k,v in out.items() if v}
 A=[[[F(0) for _ in P] for _ in P] for n in range(7)];B=[[[F(0) for _ in P] for _ in P] for n in range(7)]
 for col,z0 in enumerate(P):
  vec=resolvent({(z0,0):F(1)})
  for n in range(7):
   for row,z in enumerate(P):A[n][row][col]=vec.get((z,-1),F(0))
   if n==6:break
   v={}
   for (z,p),x in vec.items():
    for y,s in moves(z):v[y,p]=v.get((y,p),F(0))+s*x
   for row,z in enumerate(P):B[n+1][row][col]=v.get((z,-1),F(0))
   vec=resolvent(v)
 def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
 def conv(a,b):
  out=[[[F(0)]*2 for _ in range(2)] for n in range(7)]
  for n in range(7):
   for j in range(n+1):
    v=mm(a[j],b[n-j]);out[n]=[[out[n][i][k]+v[i][k] for k in range(2)] for i in range(2)]
  return out
 ident=[[[F(0)]*2 for _ in range(2)] for n in range(7)];ident[0]=[[F(1),F(0)],[F(0),F(1)]]
 X=[[row[:] for row in m] for m in A];X[0]=[[F(0)]*2 for _ in range(2)];S=[[row[:] for row in m] for m in ident];power=ident;c=F(1)
 for k in range(1,4):
  power=conv(power,X);c*=F(-1,2)-k+1;c/=k
  for n in range(7):
   for i in range(2):
    for j in range(2):S[n][i][j]+=c*power[n][i][j]
 H=conv(conv(S,B),S);z=P[0];phase=1
 for e in range(4 if len(edges)==5 else len(edges)):
  phase*=(-1)**sum((z>>f)&1 for f in range(e+1,len(edges)) if set(edges[e])&set(edges[f]));z^=1<<e
 need(z==P[1],'B maps P')
 for n in range(7):need(H[n][0][1]==H[n][1][0],'Hermitian')
 return H,phase
rows=[];c4=[(i,(i+1)%4) for i in range(4)]
for spoke,bit in [(False,0),(True,0),(True,1)]:
 H,s=extract(c4+([(0,4)] if spoke else []),[0,1,0,1]+([bit] if spoke else []))
 need(H[6][0][0]==(F(-97,24) if spoke else F(-5,2)),'diag6');need(H[6][1][0]/s==(F(-89,48) if spoke else F(-3,2)),'B ratio6');rows.append({'spoke':spoke,'bit':bit,'H6':[[str(x) for x in row] for row in H[6]],'B':s})
H,s=extract([(i,(i+1)%6) for i in range(6)],[0,1,0,1,0,1]);need(H[6][1][0]/s==F(-3,8),'sixcycle projector result');rows.append({'sixcycle_ratio':str(H[6][1][0]/s)})
need(F(-3,2)+16*(F(-89,48)-F(-3,2))==F(-43,6),'spoke total')
out={'checks':count,'rows':rows,'seconds':time.monotonic()-start,'method':'Riesz projector Pi, A=P Pi P and B=P H Pi P; A^-1/2 B A^-1/2; reverse active-edge ordering; no author import'}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
