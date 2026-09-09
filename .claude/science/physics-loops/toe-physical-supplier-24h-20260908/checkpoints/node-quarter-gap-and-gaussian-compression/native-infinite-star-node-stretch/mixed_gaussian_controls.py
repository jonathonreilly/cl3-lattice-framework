"""Fixed non-native mixed Gaussian/Pfaffian versus dense CAR controls; no native calls."""
import numpy as np
import json,signal

def pfaffian(a):
 a=np.array(a,dtype=complex,copy=True);n=len(a);out=1+0j
 if n%2:raise ValueError('odd Pfaffian')
 for k in range(0,n,2):
  j=k+1+int(np.argmax(np.abs(a[k,k+1:])))
  if abs(a[k,j])<1e-14:return 0j
  if j!=k+1:
   a[[k+1,j],:]=a[[j,k+1],:];a[:,[k+1,j]]=a[:,[j,k+1]];out=-out
  pivot=a[k,k+1];out*=pivot
  x=a[k,k+2:].copy();y=a[k+1,k+2:].copy()
  a[k+2:,k+2:]+=(np.outer(y,x)-np.outer(x,y))/pivot
 return out

def gaussian(segments,insertions,gamma,wrong_cross=False,absolute_lift=False):
 d=len(gamma);blocks=[];vectors=[];positions=[];pref=1.
 for j,(k,t) in enumerate(segments):
  w,v=np.linalg.eigh(1j*k);r=(v*np.exp(-1j*t*w))@v.conj().T
  c=np.linalg.solve((r+np.eye(d)).T,(r-np.eye(d)).T).T
  a=float(np.prod(np.cos(w[d//2:]*t/2)))
  if absolute_lift:a=abs(a)
  pref*=a
  start=len(vectors);blocks.append((start,c));vectors.extend(np.eye(d,dtype=complex))
  for gap,x in insertions:
   if gap==j:positions.append(len(vectors));vectors.append(x)
 n=len(vectors);c=np.zeros((n,n),complex);w=np.zeros_like(c)
 for start,b in blocks:c[start:start+d,start:start+d]=b
 contraction=(0 if wrong_cross else np.eye(d))-1j*gamma
 for i in range(n):
  for j in range(i+1,n):w[i,j]=vectors[i]@contraction@vectors[j];w[j,i]=-w[i,j]
 mat=np.block([[c,-np.eye(n)],[np.eye(n),-w]])
 sign=(-1)**(n*(n-1)//2)
 if positions:
  if len(positions)!=2:raise ValueError('two insertions')
  i,j=positions;keep=[a for a in range(2*n) if a not in (i,j)];mat=mat[np.ix_(keep,keep)];sign*=(-1)**(i+j+1)
 return pref*sign*pfaffian(mat)

def car(n):
 gs=[];dim=1<<n
 for j in range(n):
  x=np.zeros((dim,dim),complex);y=x.copy()
  for b in range(dim):
   z=(-1)**((b&((1<<j)-1)).bit_count());x[b^(1<<j),b]=z;y[b^(1<<j),b]=1j*z*(1-2*((b>>j)&1))
  gs.extend([x,y])
 return gs

def literal(segments,ins,rho):
 gs=car(len(segments[0][0])//2);out=np.eye(len(rho),dtype=complex)
 for j,(k,t) in enumerate(segments):
  h=sum((.5j*k[a,b]*(gs[a]@gs[b]) for a in range(len(k)) for b in range(a+1,len(k))),np.zeros_like(out))
  w,v=np.linalg.eigh(h);out=out@((v*np.exp(-1j*t*w))@v.conj().T)
  for gap,x in ins:
   if gap==j:out=out@sum((x[a]*gs[a] for a in range(len(gs))),np.zeros_like(out))
 return np.trace(rho@out)

def main():
 signal.alarm(30);k=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,2],[0,0,-2,0]],float)
 b=k+np.array([[0,0,.3,.2],[0,0,0,-.1],[-.3,0,0,0],[-.2,.1,0,0]])
 x=np.array([1,0,0,0],complex);y=np.array([.3,1j,0,0],complex)
 rows=[];bad_cross=0;bad_lift=0
 for nus in [(0.,0.),(1/3,2/5),(1.,1.)]:
  gamma=np.array([[0,-nus[0],0,0],[nus[0],0,0,0],[0,0,0,-nus[1]],[0,0,nus[1],0]],float)
  rho=np.diag([np.prod([(1+nus[j]*(1-2*((bits>>j)&1)))/2 for j in range(2)]) for bits in range(4)])
  for seg in [[(k,.02),(b,.03),(k,-.05)],[(k,.8),(b,-.3),(k,-.5)],[(k,2.5)]]:
   for ins in [[],[(0,x),(len(seg)-1,y)],[(0,y),(len(seg)-1,x)]]:
    a=gaussian(seg,ins,gamma);ref=literal(seg,ins,rho);err=abs(a-ref)
    if err>2e-11:raise ValueError(('Pfaffian mismatch',nus,err,a,ref))
    bad_cross+=abs(gaussian(seg,ins,gamma,wrong_cross=True)-ref)>1e-8
    bad_lift+=abs(gaussian(seg,ins,gamma,absolute_lift=True)-ref)>1e-8
    rows.append({'nus':nus,'factors':len(seg),'insertions':len(ins),'error':err})
 if not bad_cross or not bad_lift:raise ValueError('adverse control not discriminating')
 print(json.dumps({'status':'PASS','comparisons':len(rows),'missing_cross_identity_mismatches':int(bad_cross),'absolute_lift_mismatches':int(bad_lift),'max_error':max(r['error'] for r in rows),'rows':rows,'physical_runs':0},indent=2))
if __name__=='__main__':main()
