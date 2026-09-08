from itertools import product,combinations
from fractions import Fraction as F
from pathlib import Path
import json,time
st=time.monotonic();checks=0
def need(c,m):
 global checks
 checks+=1
 if not c:raise RuntimeError(m)
vs=list(product(range(4),repeat=3));idx={r:i for i,r in enumerate(vs)};edges=[];signs=[]
for r in vs:
 for a in range(3):
  s=list(r);s[a]=(s[a]+1)%4;i,j=sorted((idx[r],idx[tuple(s)]));edges.append((i,j));signs.append((-1)**sum(r[:a]))
left=[i for i,r in enumerate(vs) if sum(r)%2==0];right=[i for i in range(64) if i not in left];li={v:i for i,v in enumerate(left)};ri={v:i for i,v in enumerate(right)}
def gram(mask):
 B=[[0]*32 for _ in range(32)]
 for e,((v,w),s) in enumerate(zip(edges,signs)):
  z=s*(-1 if mask>>e&1 else 1)
  if v in li:B[li[v]][ri[w]]=-z
  else:B[li[w]][ri[v]]=z
 return [[sum(B[i][k]*B[j][k] for k in range(32)) for j in range(32)] for i in range(32)]
def inverse_trace(M):
 n=len(M);Q=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
 for j in range(n):
  need(Q[j][j]>0,'SPD pivot')
  z=Q[j][j];Q[j]=[v/z for v in Q[j]]
  for i in range(n):
   if i!=j:
    z=Q[i][j]
    if z:Q[i]=[a-z*b for a,b in zip(Q[i],Q[j])]
 return sum(Q[i][n+i] for i in range(n))
def cert(mask):
 A=gram(mask);need(sum(A[i][i] for i in range(32))==192,'fixed trace');c=F(5,2);M=[[F(A[i][j])+c*c*(i==j) for j in range(32)] for i in range(32)]
 trinv=inverse_trace(M);upper=(192+32*c*c)/(4*c)+c*(32-c*c*trinv)
 lower=F(2449489742783178,10**15);need(lower*lower<6,'sqrt lower')
 gap=32*lower-upper
 return {'mask_hex':hex(mask),'trace_sqrt_upper':str(upper),'gap_lower':str(gap),'gap_lower_decimal':float(gap)}
inc=[set(e for e,ab in enumerate(edges) if v in ab) for v in range(64)];v,w=0,16;bridge=next(e for e,ab in enumerate(edges) if set(ab)=={v,w});ext=sorted(inc[v]-{bridge});extw=sorted(inc[w]-{bridge});pairs=[(bridge,ext[0]),(ext[1],ext[2]),(ext[3],ext[4]),(bridge,extw[0]),(extw[1],extw[2]),(extw[3],extw[4])]
rows=[];mask=0
for k,(e,f) in enumerate(pairs[:5],1):
 mask^=(1<<e)|(1<<f)
 if k==3:
  need(mask==sum(1<<e for e in inc[v]),'singleton prefix');rows.append({'prefix':k,'mask_hex':hex(mask),'special':'opposite active parity','gap_lower':'4898979485566356/1000000000000000'})
 else:
  row=cert(mask);row['prefix']=k;need(row['gap_lower_decimal']>1/432,'improves coarse bound');rows.append(row)
# Same exact formula must not falsely certify a flux-equivalent star in the unrestricted block.
star=cert(sum(1<<e for e in inc[v]));need(F(star['gap_lower'])<0,'wrong parity scope adverse')
# scalar Newton upper identity: y2-sqrt(x)=(y1-sqrt(x))²/(2y1)>=0.
for z in [F(0),F(1),F(5,2),F(6)]:
 x=z*z;c=F(5,2);y1=(c+x/c)/2;y2=(y1+x/y1)/2;need(y2>=z,'Newton upper exact')
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'checks':checks,'rows':rows,'unrestricted_star':star,'seconds':time.monotonic()-st,'scope':'rigorous rational Newton-trace bounds at |t|=1; no coefficient solve'},indent=2)+'\n')
