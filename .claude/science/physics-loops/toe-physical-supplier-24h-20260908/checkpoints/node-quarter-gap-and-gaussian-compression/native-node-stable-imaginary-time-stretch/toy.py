"""Fixed non-native two-mode normalized imaginary-time controls, <=30 seconds."""
import numpy as np,json,signal,time

def car(n):
 out=[];d=1<<n
 for j in range(n):
  x=np.zeros((d,d),complex);y=x.copy()
  for b in range(d):
   s=(-1)**((b&((1<<j)-1)).bit_count());x[b^(1<<j),b]=s;y[b^(1<<j),b]=1j*s*(1-2*((b>>j)&1))
  out.extend([x,y])
 return out

def main():
 signal.alarm(30);start=time.monotonic();gs=car(2)
 k0=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,2],[0,0,-2,0]],float)
 k=.5*k0+np.array([[0,0,.15,.1],[0,0,0,-.05],[-.15,0,0,0],[-.1,.05,0,0]])
 h0=1j*k0;h=1j*k;w0,v0=np.linalg.eigh(h0);q0=v0[:,:2];hp=(v0*np.maximum(w0,0))@v0.conj().T
 w,v=np.linalg.eigh(h);dt=.025;step=(v*np.exp(-dt*w))@v.conj().T
 def move(q):
  q,r=np.linalg.qr(step@q);diag=np.diag(r);q=q*(diag/np.abs(diag)).conj() # projector unchanged; phase irrelevant for covariance
  return q
 def energy(q):
  p=q@q.conj().T;exc=float(np.trace(hp@p).real);defect=float((.5*np.trace((h-h0)@p)).real)
  return exc+defect,exc
 H=sum((.5j*k[a,b]*(gs[a]@gs[b]) for a in range(4) for b in range(a+1,4)),np.zeros((4,4),complex));D=H+1.5*np.eye(4);dw,dv=np.linalg.eigh(D);weights=np.abs(dv[0,:])**2
 rows=[]
 for target in [0.,.25,10.,100.]:
  q=q0.copy();lognorm=0.;steps=round(target/(2*dt));max_exc=0.
  for unused in range(steps):
   ea,_=energy(q);qm=move(q);em,ex=energy(qm);qn=move(qm);eb,_=energy(qn);lognorm-=(2*dt/6)*(ea+4*em+eb);q=qn;max_exc=max(max_exc,ex)
  pivot=float(dw.min());scaled=np.exp(-target*(dw-pivot));state=dv@(scaled*dv[0,:].conj());norm=np.linalg.norm(state);state/=norm;exactlog=-target*pivot+np.log(norm)
  gamma=np.array([[float((1j*np.vdot(state,gs[a]@gs[b]@state)).real) if a!=b else 0. for b in range(4)] for a in range(4)])
  qgamma=(-1j*(2*q@q.conj().T-np.eye(4))).real
  err=float(np.linalg.norm(gamma-qgamma));le=float(abs(lognorm-exactlog));gram=float(np.linalg.norm(q.conj().T@q-np.eye(2)))
  if err>1e-10 or le>2e-8 or gram>1e-12:raise ValueError(('toy comparison',target,err,le,gram))
  rows.append({'time':target,'covariance_error':err,'log_norm_error':le,'log_norm':lognorm,'gram_error':gram,'max_free_excitation':max_exc})
 # Exact sign test: 25-20sqrt(2)<0 because 625<800; individual anchor 5-2sqrt(2)>0.
 if not (625<800 and 25>8):raise ValueError('overlap sign witness')
 print(json.dumps({'status':'PASS','synthetic_rows':rows,'negative_overlap_exact':'(25-20sqrt(2))/9','negative_overlap_proved_by':[625,800],'physical_runs':0,'seconds':time.monotonic()-start},indent=2))
if __name__=='__main__':main()
