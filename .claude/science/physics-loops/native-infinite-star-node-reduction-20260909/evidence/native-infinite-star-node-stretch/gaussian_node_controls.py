"""Fixed3mode scaled-integer CAR test of node-sum cancellation. Cap30s."""
import json,signal
signal.alarm(30)
d=8
I=[[int(i==j) for j in range(d)] for i in range(d)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(d)] for i in range(d)]
def scale(c,a):return [[c*z for z in row] for row in a]
g=[]
for j in range(6):
 a=[[0j]*d for _ in range(d)]
 for x in range(d):a[x^(1<<(j//2))][x]=(-1)**((x&((1<<(j//2))-1)).bit_count())*(1 if j%2==0 else 1j*(1-2*((x>>(j//2))&1)))
 g.append(a)
def gamma(q):return [[sum(q[k]*g[k][i][j] for k in range(6)) for j in range(d)] for i in range(d)]
B=mm(g[0],g[1]);G=add(scale(3,I),scale(4,B));GD=add(scale(3,I),scale(-4,B))
if mm(G,GD)!=scale(25,I):raise ValueError('scaled unitary')
R=[]
for a in range(6):
 row=[]
 for b in range(6):
  z=mm(g[a],mm(G,mm(g[b],GD)));tr=sum(z[i][i] for i in range(d));v=tr/d
  if v.imag or not v.real.is_integer():raise ValueError('integer rotation')
  row.append(int(v.real))
 R.append(row)
qs=[[int(a==b) for a in range(6)] for b in range(6)]+[[2,-1,3,0,1,-2]];count=0;omission_failed=0
for q in qs:
 for l in qs:
  Q=gamma(q);L=gamma(l);Dq=[sum(R[i][j]*q[j] for j in range(6))-25*q[i] for i in range(6)]
  left=scale(25,add(mm(Q,mm(L,G)),mm(L,mm(G,Q))))
  right=add(scale(50*sum(a*b for a,b in zip(q,l)),G),mm(L,mm(gamma(Dq),G)))
  if left!=right:raise ValueError('node CAR cancellation')
  count+=1
  if left!=scale(50*sum(a*b for a,b in zip(q,l)),G):omission_failed+=1
if not omission_failed:raise ValueError('omission not discriminating')
print(json.dumps({'status':'PASS','exact_scaled_integer_checks':count,'omitted_rotation_term_mismatches':omission_failed,'physical_runs':0},indent=2))
