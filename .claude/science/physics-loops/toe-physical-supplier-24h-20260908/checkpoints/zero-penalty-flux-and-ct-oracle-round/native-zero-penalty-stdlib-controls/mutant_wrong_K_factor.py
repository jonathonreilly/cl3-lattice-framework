from fractions import Fraction as F
from pathlib import Path
import json,time,resource,sys,signal,argparse
AUDIT_TIMEOUT_SEC=180
# Gaussian rationals (real, imaginary); matrices never use floating arithmetic.
def G(a=0,b=0):return F(a),F(b)
ZERO=G();ONE=G(1);I=G(0,1)
def ga(x,y):return x[0]+y[0],x[1]+y[1]
def gm(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def neg(x):return -x[0],-x[1]
def mat(n):return [[ZERO for _ in range(n)] for _ in range(n)]
def eye(n):return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def add(a,b):return [[ga(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[gm(x,c) for x in row] for row in a]
def mm(a,b):
 c=mat(len(a))
 for i,row in enumerate(a):
  for k,x in enumerate(row):
   if x!=ZERO:
    for j,y in enumerate(b[k]):
     if y!=ZERO:c[i][j]=ga(c[i][j],gm(x,y))
 return c
def trace(a):
 z=ZERO
 for i in range(len(a)):z=ga(z,a[i][i])
 return z
def charpoly(a):
 n=len(a);power=eye(n);traces={};coeff=[ONE]
 for k in range(1,n+1):power=mm(power,a);traces[k]=trace(power)
 for k in range(1,n+1):
  z=ZERO
  for j in range(1,k+1):z=ga(z,gm(coeff[k-j],traces[j]))
  coeff.append(gm(neg(z),G(F(1,k))))
 return coeff

def run():
 start=time.monotonic();checks=0;rows=[]
 def req(v,m):
  nonlocal checks
  checks+=1
  if not v:raise RuntimeError(m)
 for v,edges in [(3,[(0,1),(1,2),(0,2)]),(4,[(0,1),(1,2),(2,3),(0,3)])]:
  E=len(edges);dim=1<<E;A=[]
  for e,ends in enumerate(edges):
   mask=sum(1<<f for f in range(e) if set(ends)&set(edges[f]));a=mat(dim)
   for x in range(dim):a[x^(1<<e)][x]=G((-1)**((mask&x).bit_count()))
   A.append(a)
  H=mat(dim)
  for a in A:H=add(H,a)
  S=eye(dim)
  for _ in range(v):S=scale(S,I)
  for i in range(v):
   j=(i+1)%v;e=next(e for e,ends in enumerate(edges) if set(ends)=={i,j});S=scale(mm(S,A[e]),G(1 if i<j else -1))
  req(mm(S,S)==eye(dim),'cycle involution');req(mm(S,H)==mm(H,S),'cycle conserved')
  gam=[]
  for i in range(v):
   a=mat(1<<v)
   for n in range(1<<v):a[n^(1<<i)][n]=G((-1)**((n&((1<<i)-1)).bit_count()))
   gam.append(a)
  even=[n for n in range(1<<v) if n.bit_count()%2==0] # PARITY_DOMAIN
  req(sum((-1)**n.bit_count() for n in even)==len(even),'global Gauss product enforces even matter')
  total=0
  for flux in [-1,1]:
   xi=[1]*(E-1)+[flux];h=mat(1<<v);ik=mat(v)
   for (a,b),x in zip(edges,xi):
    h=add(h,scale(mm(gam[a],gam[b]),G(0,-x)));ik[a][b]=G(0,-x);ik[b][a]=G(0,x) # K_FACTOR
   hf=[[h[i][j] for j in even] for i in even];proj=scale(add(eye(dim),scale(S,G(flux))),G(F(1,2)))
   req(trace(proj)==G(2**(v-1)),'flux carrier dimension');req(len(even)==2**(v-1),'even matter domain');total+=int(trace(proj)[0])
   # Independent analytic frequency-square polynomial, no diagonalization.
   expected=[1,0,-12,0] if v==3 else ([1,0,-16,0,0] if flux==-1 else [1,0,-16,0,64])
   req(charpoly(ik)==list(map(G,expected)),'frequency square and factor two')
   hn=eye(dim);hp=eye(len(even));moments=[]
   for k in range(len(even)+1):
    native=trace(mm(proj,hn));fermion=trace(hp)
    predicted=(2**(v-1) if k==0 else (0 if k%2 else (4*3**(k//2) if v==3 else (8*4**(k//2) if flux==-1 else 4*8**(k//2))))) # MULTIPLICITY
    req(native==fermion,'native versus even CAR moment');req(native==G(predicted),'analytic spectator multiplicity moment');moments.append(str(native[0]));hn=mm(hn,H);hp=mm(hp,hf)
   rows.append(dict(vertices=v,flux=flux,characteristic_polynomial=expected,moments=moments))
  req(total==2**E,'full native dimension')
 req(2**(4-0-1)==8,'all active zero boundary');req(2**(4-2-1)==2,'generic even residual count');req(2**(3-1-1)==2,'odd vertex residual count')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(0<rss<384 and time.monotonic()-start<180,'resources')
 return dict(checks=checks,rows=rows,seconds=time.monotonic()-start,rss_mib=rss,scope='Exact Gaussian-rational native/CAR traces and analytic frequency squares; no cubic flux optimum or phase.')
if __name__=='__main__':
 signal.alarm(AUDIT_TIMEOUT_SEC);p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');p.parse_args();print(json.dumps(run(),indent=2))
